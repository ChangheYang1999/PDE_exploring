"""D6FP D1 variant v2 (lead 23:08Z item 2): the velocity gradient DU on the product grid ACCUMULATED in double-double from the float64 radial
derivative arrays (Model.radial_derivs: Chebyshev envelopes, twist, coefficients) and the float64 angular tables (A0, A1, A2; double-double
tables rounded once), the pressure source f = tr(DU^2) formed in double-double and kept unrounded (hi, lo) for the double-double pressure chain
(PressureSolver.solve_dd). All products are error-free (two_prod, Ozaki matrix products) and all sums are two_sum accumulations; the only
float64 roundings left are those of the inputs. _SourceDD wraps the evaluation as an autograd Function: forward-mode tangents use the same
double-double accumulation for the coefficient part (DU is linear in the coefficients at fixed parameters) and the float64 forward-mode
derivative of Model.fields_grid for the (c_l, omega) part; reverse mode uses the float64 graph."""
import torch
from ..pressure.exact_matmul import matmul_dd, dd_mul_f, dd_add, dd_div_f, _two_prod_err

DT = torch.float64
EPS_LIST = [[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]], [[0.0, 0.0, -1.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]], [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 0.0]]]


def dd_mul_dd(h1, l1, h2, l2):
    p = h1 * h2; e = _two_prod_err(h1, h2, p); e = e + (h1 * l2 + l1 * h2)
    s = p + e
    return s, e - (s - p)


def matmul_dd_x(Ah, Al, B):
    """(Ah + Al) @ B: Ozaki product for the high part, plain float64 product for the low part (its rounding is 2^-53 |Al| |B|, below the
    double-double level)."""
    h, l = matmul_dd(Ah, B)
    return dd_add(h, l, torch.matmul(Al, B), torch.zeros_like(h))


def _z(x):
    return torch.zeros_like(x)


def scalar_sets_dd(gT, gS, l, rho):
    """Double-double versions of Model.scalar_sets for T, K, D (the sets needed for U and DU). gT = (gTh, gTl), gS = (gSh, gSl): double-double
    radial derivative arrays (K+1, Nr, Nq)."""
    rho = rho[:, None]; l = l[None, :]
    (gTh, gTl), (gSh, gSl) = gT, gS
    def comb(k1, c1, k2, c2):                                                  # c1 * gS[k1] + c2 * gS[k2] with exact products
        h1, l1 = dd_mul_f(gSh[k1], gSl[k1], c1); h2, l2 = dd_mul_f(gSh[k2], gSl[k2], c2)
        return dd_add(h1, l1, h2, l2)
    T = ((gTh[0], gTl[0]), (gTh[1], gTl[1]), (gTh[2], gTl[2]))
    K = (comb(0, l + 1, 1, 2 * rho), comb(1, l + 3, 2, 2 * rho), comb(2, l + 5, 3, 2 * rho))
    D = (comb(1, 6 + 4 * l, 2, 4 * rho), comb(2, 10 + 4 * l, 3, 4 * rho), comb(3, 14 + 4 * l, 4, 4 * rho))
    return T, K, D


def radial_derivs_dd(model, d, c_l=None, omega=None, K=4):
    """Double-double (hi, lo) radial derivative arrays gT, gS (K+1, Nr, Nq): the coefficient contraction B[l] @ a (float64 basis tables
    rb.matrices, exact coefficients) and the twist (float64 cos/sin tables) in double-double; mirrors Model.radial_derivs. d: dict with A, C, B,
    D, E (float64 (n, Nq)); c_l, omega default to d's."""
    import math
    from .fields import alpha_of
    from ..pressure.exact_matmul import matmul_dd
    c_l = d["c_l"] if c_l is None else c_l; omega = d["omega"] if omega is None else omega
    rho = model.rho; alpha = alpha_of(c_l); R0 = torch.tensor(model.R0, dtype=DT, device=rho.device); ch = model.channels
    def contract(B, a):
        Bq = B[model.l_idx]                                                      # (Nq, K+1, Nr, Nk)
        Nq_, K1, Nr_, Nk_ = Bq.shape
        h, l = matmul_dd(Bq.reshape(Nq_, K1 * Nr_, Nk_), a.T[:, :, None])       # (Nq, (K+1) Nr, 1)
        return h[:, :, 0].reshape(Nq_, K1, Nr_).permute(1, 2, 0), l[:, :, 0].reshape(Nq_, K1, Nr_).permute(1, 2, 0)
    BT = model.rb.matrices(rho, alpha, R0, model.L_ext, K, shift=0.0); BS = model.rb.matrices(rho, alpha, R0, model.L_ext, K, shift=1.0)
    gTh, gTl = contract(BT, d["A"]); gSh, gSl = contract(BS, d["C"])
    if ch["NkB"] > 0 and "B" in d and d["B"].numel() > 0:
        BB = model.rb.matrices(rho, alpha, R0, model.L_ext, K, power=lambda l: 2 * alpha + 1 + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkB"])
        h, l = contract(BB, d["B"]); gTh, gTl = dd_add(gTh, gTl, h, l)
    if ch["NkD"] > 0 and "D" in d and d["D"].numel() > 0:
        BD = model.rb.matrices(rho, alpha, R0, model.L_ext, K, power=lambda l: 2 * alpha + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkD"])
        h, l = contract(BD, d["D"]); gSh, gSl = dd_add(gSh, gSl, h, l)
    C, S = model.rb.twist_tables(rho, omega, c_l, R0, model.Mmax, K)              # (Mmax+1, K+1, Nr)
    def twist(gh, gl):
        if model.pair_c.numel() == 0:
            return gh, gl
        gph, gpl = gh[:, :, model.partner], gl[:, :, model.partner]
        Cm = C[model.m_arr].permute(1, 2, 0); Sm = S[model.m_arr].permute(1, 2, 0) * model.tw_sign[None, None, :]
        oh, ol = [], []
        for n in range(K + 1):
            th = None
            for k in range(n + 1):
                ah, al = dd_mul_f(gh[k], gl[k], Cm[n - k]); bh, bl = dd_mul_f(gph[k], gpl[k], Sm[n - k])
                sh, sl = dd_add(ah, al, bh, bl)
                b = float(math.comb(n, k))
                if b != 1.0:
                    sh, sl = dd_mul_f(sh, sl, b)
                th, tl = (sh, sl) if th is None else dd_add(th, tl, sh, sl)
            oh.append(th); ol.append(tl)
        return torch.stack(oh, 0), torch.stack(ol, 0)
    gTh, gTl = twist(gTh, gTl); gSh, gSl = twist(gSh, gSl)
    if ch["NkE"] > 0 and "E" in d and d["E"].numel() > 0:                          # untwisted harmonic channel, l >= 2
        BE = model.rb.matrices(rho, alpha, R0, model.L_ext, K, power=lambda l: torch.as_tensor(2.0 * l + 1.0, dtype=DT, device=rho.device), core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkE"], lmask=[0, 1])
        h, l = contract(BE, d["E"]); gSh, gSl = dd_add(gSh, gSl, h, l)
    return (gTh, gTl), (gSh, gSl)


def scalar_grid_dd(model, h, need_hess=True):
    """Double-double version of Model.scalar_grid: h = ((h0h, h0l), (h1h, h1l), (h2h, h2l)) radial arrays (Nr, Nq). Returns f (Nr, Na),
    grad (3, Nr, Na), hess (3, 3, Nr, Na) as (hi, lo) pairs."""
    (h0h, h0l), (h1h, h1l), (h2h, h2l) = h
    r = model.r[:, None]; rl = model.rl; n = model.n.T
    A0T = model.A0.T; A1T = [model.A1[i].T for i in range(3)]
    X0h, X0l = dd_mul_f(h0h, h0l, rl)                                         # r^l g
    f = matmul_dd_x(X0h, X0l, A0T)
    X1h, X1l = dd_mul_f(h1h, h1l, rl); X1h, X1l = dd_mul_f(X1h, X1l, r)        # r^(l+1) g'
    G1h, G1l = matmul_dd_x(X1h, X1l, A0T)
    Mh, Ml = dd_div_f(X0h, X0l, r)                                            # r^(l-1) g
    grad = []
    for i in range(3):
        ah, al = dd_mul_f(G1h, G1l, 2 * n[i][None, :])
        bh, bl = matmul_dd_x(Mh, Ml, A1T[i])
        grad.append(dd_add(ah, al, bh, bl))
    if not need_hess:
        return f, grad, None
    X2h, X2l = dd_mul_f(h2h, h2l, rl); X2h, X2l = dd_mul_f(X2h, X2l, r); X2h, X2l = dd_mul_f(X2h, X2l, r)     # r^(l+2) g''
    G2h, G2l = matmul_dd_x(X2h, X2l, A0T)
    H1h, H1l = dd_mul_f(h1h, h1l, rl)                                         # r^l g'
    H1A0 = matmul_dd_x(H1h, H1l, A0T)
    H1A1 = [matmul_dd_x(H1h, H1l, A1T[i]) for i in range(3)]
    Hm2h, Hm2l = dd_div_f(Mh, Ml, r)                                          # r^(l-2) g
    hess = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            th, tl = dd_mul_f(G2h, G2l, 4 * n[i][None, :]); th, tl = dd_mul_f(th, tl, n[j][None, :])     # two exact products (n_i n_j would round)
            if i == j:
                th, tl = dd_add(th, tl, 2 * H1A0[0], 2 * H1A0[1])
            ah, al = dd_mul_f(H1A1[j][0], H1A1[j][1], 2 * n[i][None, :]); th, tl = dd_add(th, tl, ah, al)
            ah, al = dd_mul_f(H1A1[i][0], H1A1[i][1], 2 * n[j][None, :]); th, tl = dd_add(th, tl, ah, al)
            ah, al = matmul_dd_x(Hm2h, Hm2l, model.A2[i, j].T); th, tl = dd_add(th, tl, ah, al)
            hess[i][j] = (th, tl)
    return f, grad, hess


def velocity_gradient_dd(model, gT, gS):
    """DU (index order [m, i] = d_m U_i) as lists of (hi, lo) (Nr, Na) from double-double radial arrays gT = (hi, lo), gS = (hi, lo) (K+1, Nr, Nq)."""
    T, K, D = scalar_sets_dd(gT, gS, model.l_arr, model.rho)
    _, gT_, hT_ = scalar_grid_dd(model, T, True)
    _, _, hK = scalar_grid_dd(model, K, True)
    dD, gD, _ = scalar_grid_dd(model, D, False)
    r = model.r[:, None]; n = model.n.T
    eps = EPS_LIST                                                              # Levi-Civita as Python constants (no tensor data access inside functorch transforms)
    GU = [[None] * 3 for _ in range(3)]
    for m in range(3):
        for i in range(3):
            # d_m U_i = -eps_imk d_k T - eps_ijk y_j d_m d_k T + d_m d_i K - delta_im D - y_i d_m D
            th, tl = hK[m][i]
            for k in range(3):
                e = eps[i][m][k]
                if e != 0.0:
                    th, tl = dd_add(th, tl, -e * gT_[k][0], -e * gT_[k][1])
            for j in range(3):
                for k in range(3):
                    e = eps[i][j][k]
                    if e != 0.0:
                        ah, al = dd_mul_f(hT_[m][k][0], hT_[m][k][1], r); ah, al = dd_mul_f(ah, al, -e * n[j][None, :])
                        th, tl = dd_add(th, tl, ah, al)
            if m == i:
                th, tl = dd_add(th, tl, -dD[0], -dD[1])
            ah, al = dd_mul_f(gD[m][0], gD[m][1], r); ah, al = dd_mul_f(ah, al, -n[i][None, :])
            th, tl = dd_add(th, tl, ah, al)
            GU[m][i] = (th, tl)
    return GU


def trace_product_dd(GU, GV):
    """sum_mi GU[m][i] GV[i][m] in double-double."""
    th = None
    for m in range(3):
        for i in range(3):
            ph, pl = dd_mul_dd(GU[m][i][0], GU[m][i][1], GV[i][m][0], GV[i][m][1])
            th, tl = (ph, pl) if th is None else dd_add(th, tl, ph, pl)
    return th, tl


def pressure_source_dd(model, z):
    """(fh, fl) of tr(DU^2) on the product grid for the coefficient vector z: every coefficient-dependent operation (radial contraction, twist,
    scalar sets, angular contraction, assembly, trace) in double-double from the float64 tables."""
    d = model.unpack_all(z)
    gT, gS = radial_derivs_dd(model, d)
    GU = velocity_gradient_dd(model, gT, gS)
    return trace_product_dd(GU, GU)


class _SourceDD(torch.autograd.Function):
    generate_vmap_rule = True

    @staticmethod
    def forward(z, model):
        with torch.no_grad():
            return pressure_source_dd(model, z)

    @staticmethod
    def setup_context(ctx, inputs, output):
        z, model = inputs
        ctx.model = model
        ctx.save_for_backward(z); ctx.save_for_forward(z)

    @staticmethod
    def jvp(ctx, z_dot, _model_dot):
        z, = ctx.saved_tensors; model = ctx.model
        from ..pressure import poisson_sh as _ps
        if _ps.TANGENT_FP64:                                                 # float64 tangent of the float64 source (cost option)
            from . import residuals as res
            t = torch.func.jvp(lambda zz: res.pressure_source(model.fields_grid(zz, need_vort=False)["GU"]), (z,), (z_dot,))[1]
            return t, torch.zeros_like(t)
        d = model.unpack_all(z)
        gT, gS = radial_derivs_dd(model, d)
        GU = velocity_gradient_dd(model, gT, gS)
        # coefficient part of the tangent: linear in the coefficients at the primal parameters (same double-double accumulation)
        zc = z_dot.clone()
        if model.free_params:
            zc = torch.cat([z_dot[: model.n_coef], torch.zeros(2, dtype=DT, device=z.device)])
        dc = model.unpack_all(zc)
        gTd, gSd = radial_derivs_dd(model, dc, c_l=d["c_l"], omega=d["omega"])
        GUd = velocity_gradient_dd(model, gTd, gSd)
        if model.free_params:
            # parameter part: float64 forward-mode derivative of the fields with respect to (c_l, omega) at the primal coefficients
            def fields_p(p):
                zz = torch.cat([z[: model.n_coef], p])
                return model.fields_grid(zz, need_vort=False)["GU"]
            _, GUp = torch.func.jvp(fields_p, (z[-2:],), (z_dot[-2:],))
            for m in range(3):
                for i in range(3):
                    GUd[m][i] = dd_add(GUd[m][i][0], GUd[m][i][1], GUp[m, i], torch.zeros_like(GUp[m, i]))
        th, tl = trace_product_dd(GU, GUd)
        return 2 * th, 2 * tl

    @staticmethod
    def backward(ctx, gfh, gfl):
        z, = ctx.saved_tensors; model = ctx.model
        from . import residuals as res
        with torch.enable_grad():
            zz = z.detach().requires_grad_(True)
            f = res.pressure_source(model.fields_grid(zz, need_vort=False)["GU"])
            # convention: the high part carries the derivative (the low part is the rounding residue, derivative zero); consumers use fh + fl, so
            # their adjoints for fh and fl coincide and only one of them enters
            g = gfh if gfh is not None else gfl
            gz, = torch.autograd.grad(f, zz, g)
        return gz, None


def source_dd(model, z):
    """Entry point: (fh, fl) with exact forward-mode tangents and float64 reverse mode."""
    return _SourceDD.apply(z, model)
