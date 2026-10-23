"""
hs_solve.py -- least-squares solve of the HYDROSTATIC profile problem (eps = 0 of FINAL_REPORT 3.72; lead 08:04Z task HS (2), (3)) in the smooth Q basis.
Unknowns: Chebyshev coefficients u of g = y w(t) sum_k sigma^k beta_k(t) cos 2k theta (local per-mode basis of dr.py; map exponent gamma = 1/c_map), and
optionally c.  The hydrostatic inverse V[g] = (V_1, V_2) (hs.hydro_V, vertical-line integrals) is LINEAR in g, so its values at the collocation points are
precomputed once per model as matrices M1, M2 (npts x nu) by applying hydro_V to every basis function (g_xx by central differences in x, step 1e-5 (1+|x|));
likewise G, Gx, Gy.  Residual rows at the collocation points (Radau nodes i >= 1 x the M quadrant angles, Cartesian (x, y)):
    R_h = (c x + M1 u) * (Gx u) + (c y + M2 u) * (Gy u) - G u,
plus the centre row beta_0(-1) = 1 (g_y(0) = 1) and the gauge row K = 1 (y-axis tail amplitude; the 3.72(a) slice K = a0), optionally the centre condition
int_0^inf g_xixi(0, t) dt = 1 - c (= (M2 u)_y(0) + ... evaluated as c - 1 + V_2,y(0) where V_2,y(0) = -Phi_xiy(0) ... here through the residual's own limit
R_h(0) -> (c - 1 + dV_2/dy(0)) a0, included as the row at the first Radau node only when 'centre=keep').  Gauss-Newton with SVD least-squares steps and
backtracking; the Jacobian is exact (R_h is quadratic in u, linear in c).  Diagnostics after the solve: sampled residual maxima by region with N_f-type
normalisation N_f = |(c x + V_1) g_x| + |(c y + V_2) g_y| + |g| on a between-node set, c, a0, K, E = e/a0 (cubic coefficient of g(0, y)), axis diagnostics
max |v G' - G| (G = g(0, .), v = c y + V_2(0, .)), int_0^R (1 - t/R) g_xixi(0, t) dt - (1 - v(R)/R) at R = 1, 10, 100, sign of g_xixi(0, .), min g_y on the
x-axis, and the smallest singular values of the Jacobian (with and without the gauge/centre rows).
usage: python3 src/hs_solve.py N=48 M=12 c=3.0 [cfree=0|1] [centre=drop|keep] [start=simple|<regauge: state.pt>] [maxit=40] [tag=...] [n_in=24 n_tail=80]
"""
import sys, math, time, json, numpy as np, torch
sys.path.insert(0, 'numerics/src')
import ipm3, ipm3s, ipm3q, ipm3ql, dr, hs
torch.set_default_dtype(torch.float64)
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def bary_interp_matrix_torch(xn, wn, xi, dev):
    """vectorised barycentric interpolation matrix (P x n) from nodes xn (weights wn) to points xi."""
    xn = torch.tensor(np.asarray(xn), device=dev); wn = torch.tensor(np.asarray(wn), device=dev); xi = torch.tensor(np.asarray(xi, dtype=np.float64), device=dev)
    d = xi[:, None] - xn[None, :]; hit = d.abs() < 1e-14
    d = torch.where(hit, torch.ones_like(d), d); P = wn[None, :] / d; P = P / P.sum(1, keepdim=True)
    anyhit = hit.any(1)
    P[anyhit] = hit[anyhit].to(P.dtype)
    return P


class HSModel:
    def __init__(self, N, M, c_map, device='cuda', n_in=24, n_tail=80, q=3, hrel=1e-5, rcond=1e-8, fine=False):
        self.m = dr.DR(N, M, c_map, device=device, basis='local', rcond=rcond); m = self.m; self.dev = m.dev; self.N, self.M = N, M
        rad = m.rad; self.c_map = c_map; self.fine = fine
        # collocation points: Radau nodes i >= 1 (the centre row is separate) x the M quadrant angles (fine=True: the M2 = 3M angles, over-determined as in 4K)
        r = rad.rR[1:].cpu().numpy(); th = m.angf.theta_np if fine else m.ang.theta_np; RR, TT = np.meshgrid(r, th, indexing='ij'); self.X = (RR * np.cos(TT)).reshape(-1); self.Y = (RR * np.sin(TT)).reshape(-1)
        self.npts = len(self.X)
        # quadrature points for the hydrostatic inverse at every collocation point
        ug, wg = np.polynomial.legendre.leggauss(n_in); ug = 0.5 * (ug + 1); wg = 0.5 * wg
        ut, wt = np.polynomial.legendre.leggauss(n_tail); ut = 0.5 * (ut + 1); wt = 0.5 * wt
        y = self.Y; Lt = 1.0 + y; s = (ut / (1 - ut)) ** q; ds = q * ut ** (q - 1) / (1 - ut) ** (q + 1)
        self.T_in = y[:, None] * ug[None, :]; self.W_in = y[:, None] * wg[None, :]
        self.T_t = y[:, None] + Lt[:, None] * s[None, :]; self.W_t = Lt[:, None] * (wt * ds)[None, :]
        self.n_in, self.n_tail, self.hrel = n_in, n_tail, hrel
        # all evaluation points: (x, t) for inner and tail, and x +- h for the FD second derivative
        Xq = np.concatenate([np.repeat(self.X[:, None], n_in, 1).reshape(-1), np.repeat(self.X[:, None], n_tail, 1).reshape(-1)])
        Tq = np.concatenate([self.T_in.reshape(-1), self.T_t.reshape(-1)])
        self.h = hrel * (1 + np.abs(Xq))
        self.pts = [(Xq, Tq), (Xq + self.h, Tq), (Xq - self.h, Tq), (self.X, self.Y)]              # last: the collocation points themselves (g, g_x, g_y)
        self.prep = []
        for (xx, yy) in self.pts:
            rr = np.hypot(xx, yy); tht = np.arctan2(yy, xx); t = rad.t_of_r(np.maximum(rr, 1e-300))
            PR = bary_interp_matrix_torch(rad.tR_np, rad.wR_np, t, self.dev)
            tt = torch.tensor(t, device=self.dev); Q = rad.Q(tt); g = (1 - tt ** 2) / Q; om = -(1 + tt) / Q; w = (1 - tt) / 2
            thT = torch.tensor(tht, device=self.dev); n = 2 * m.kk
            self.prep.append(dict(PR=PR, g=g, om=om, w=w, r=torch.tensor(rr, device=self.dev), C=torch.cos(thT[:, None] * n[None, :]), S=torch.sin(thT[:, None] * n[None, :]), cos=torch.cos(thT), sin=torch.sin(thT)))
        self.maps = None

    def _eval(self, prep, bkR, bkR_t):
        """g, g_x, g_y at a prepared point set for mode values bkR (N+1, M) [batched: bkR (B, N+1, M)]."""
        bk = prep['PR'] @ bkR; bk_t = prep['PR'] @ bkR_t
        b = (bk * prep['C']).sum(-1); rb_r = prep['g'] * (bk_t * prep['C']).sum(-1); b_th = -(bk * (2 * self.m.kk)[None, :] * prep['S']).sum(-1)
        cos, sin, w, om, r = prep['cos'], prep['sin'], prep['w'], prep['om'], prep['r']
        P = sin * b; rP_r = sin * rb_r; P_th = cos * b + sin * b_th
        gval = r * w * P; g_r = w * ((1 + om) * P + rP_r); g_th_r = w * P_th
        return gval, cos * g_r - sin * g_th_r, sin * g_r + cos * g_th_r

    def build_maps(self, batch=64, log=None):
        """M1, M2, G, Gx, Gy (npts x nu) by applying the inverse to the basis functions in batches."""
        m = self.m; nu = m.nu; dev = self.dev
        M1 = torch.zeros(self.npts, nu, device=dev); M2 = torch.zeros_like(M1); G = torch.zeros_like(M1); Gx = torch.zeros_like(M1); Gy = torch.zeros_like(M1)
        W_in = torch.tensor(self.W_in, device=dev); T_in = torch.tensor(self.T_in, device=dev); W_t = torch.tensor(self.W_t, device=dev); hq = torch.tensor(self.h, device=dev)
        yv = torch.tensor(self.Y, device=dev); t0 = time.time()
        for k0 in range(0, nu, batch):
            k1 = min(nu, k0 + batch); I = torch.zeros(k1 - k0, nu, device=dev); I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            beta = m.beta_full(I)                                                  # (B, N+1, M)
            bkR = (m.rad.sigR[None, :, None] ** m.kk[None, None, :]) * beta; bkR_t = m.rad.DR @ bkR
            _, gx0, _ = self._eval(self.prep[0], bkR, bkR_t); _, gxp, _ = self._eval(self.prep[1], bkR, bkR_t); _, gxm, _ = self._eval(self.prep[2], bkR, bkR_t)
            gxx = (gxp - gxm) / (2 * hq)                                           # (B, nq)
            nin = self.npts * self.n_in
            gxx_in = gxx[:, :nin].reshape(k1 - k0, self.npts, self.n_in); gx_t = gx0[:, nin:].reshape(k1 - k0, self.npts, self.n_tail); gxx_t = gxx[:, nin:].reshape(k1 - k0, self.npts, self.n_tail)
            I_in = (W_in[None] * T_in[None] * gxx_in).sum(-1); J1 = (W_t[None] * gx_t).sum(-1); J2 = (W_t[None] * gxx_t).sum(-1)
            M1[:, k0:k1] = (-J1).T; M2[:, k0:k1] = (I_in + yv[None] * J2).T
            gv, gxv, gyv = self._eval(self.prep[3], bkR, bkR_t); G[:, k0:k1] = gv.T; Gx[:, k0:k1] = gxv.T; Gy[:, k0:k1] = gyv.T
            if log and (k0 // batch) % 4 == 0: log.write(f"  maps: {k1}/{nu} columns, {time.time()-t0:.0f}s\n"); log.flush()
        self.maps = dict(M1=M1, M2=M2, G=G, Gx=Gx, Gy=Gy); return self.maps

    def residual(self, u, c, centre='drop'):
        mp = self.maps; X = torch.tensor(self.X, device=self.dev); Y = torch.tensor(self.Y, device=self.dev)
        V1 = mp['M1'] @ u; V2 = mp['M2'] @ u; g = mp['G'] @ u; gx = mp['Gx'] @ u; gy = mp['Gy'] @ u
        R = (c * X + V1) * gx + (c * Y + V2) * gy - g
        a0 = self.m.jets(u)[0]; K = self.m.farfield(u)['K']
        rows = [R, (a0 - 1.0).reshape(1), (K - 1.0).reshape(1)]
        return torch.cat(rows), dict(V1=V1, V2=V2, g=g, gx=gx, gy=gy, R=R, a0=a0, K=K)

    def jacobian(self, u, c, cfree):
        mp = self.maps; X = torch.tensor(self.X, device=self.dev); Y = torch.tensor(self.Y, device=self.dev)
        V1 = mp['M1'] @ u; V2 = mp['M2'] @ u; gx = mp['Gx'] @ u; gy = mp['Gy'] @ u
        JR = (c * X + V1)[:, None] * mp['Gx'] + gx[:, None] * mp['M1'] + (c * Y + V2)[:, None] * mp['Gy'] + gy[:, None] * mp['M2'] - mp['G']
        # centre and gauge rows are linear in u: finite differences of the exact linear maps via unit vectors (cheap: use autograd-free linear extraction)
        nu = self.m.nu; e = torch.eye(nu, device=self.dev)
        a0row = torch.stack([self.m.jets(e[i])[0] for i in range(nu)]) if False else None
        # jets() and farfield() are linear: evaluate on the identity in a loop-free way using their formulas
        n0 = self.m.nk[0]; n1 = self.m.nk[1]
        a0row = torch.zeros(nu, device=self.dev); b0, _ = self.m.beta_at(e[0] * 0 + 0, 0, [-1.0]) if False else (None, None)
        # beta_0(-1) = sum_j u_0j T_j(s_0(-1)) with s_0(-1) = -1 -> T_j(-1) = (-1)^j
        a0row[self.m.offs[0]:self.m.offs[1]] = torch.tensor([(-1.0) ** j for j in range(n0)], device=self.dev)
        Krow = torch.zeros(nu, device=self.dev)
        for k in range(self.m.M):
            Krow[self.m.offs[k]:self.m.offs[k + 1]] = self.m.Dff * ((-1) ** k)      # beta_k(1) = sum_j u_kj (T_j(1) = 1)
        J = torch.cat([JR, a0row[None, :], Krow[None, :]], 0)
        if cfree:
            col = torch.cat([X * gx + Y * gy, torch.zeros(2, device=self.dev)]); J = torch.cat([J, col[:, None]], 1)
        return J


def simple_start(hsm, c):
    """g = y (1 + r^2)^((p-1)/2), p = 1/c: g_y(0) = 1, K = 1 (L = 1); projected onto the basis through its mode values."""
    m = hsm.m; r = m.rad.rR; w = m.rad.wR; p = 1.0 / c
    b0 = (1 + r ** 2) ** ((p - 1) / 2) / w                                               # g/(y w)
    F = b0[:, None] * torch.ones(m.M2, device=m.dev)[None, :]
    return m.project(F)


def sampled_table(hsm, u, c):
    """between-node sampled |R_h|, |R_h|/N_f by region, recomputing V with hs.hydro_V on the evaluator GEval (independent of the maps)."""
    m = hsm.m; tR = m.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = m.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    rm = m.rad.rmap_np(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij'); X = RR * np.cos(TT); Y = RR * np.sin(TT)
    ge = hs.GEval(m, m.beta_full(u)); V1, V2 = hs.hydro_V(ge, X, Y, n_in=32, n_tail=100); g, gx, gy = ge(X, Y)
    R = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)
    out = []
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e300)]:
        msk = (RR >= lo) & (RR < hi)
        if msk.any(): out.append((lo, hi, float(np.abs(R[msk]).max()), float((np.abs(R) / Nf)[msk].max()), float(Nf[msk].max())))
    return out


def axis_diagnostics(hsm, u, c):
    """v(y) = c y + V_2(0, y), G(y) = g(0, y): max |v G' - G| on y in [1e-3, 1e3]; centre-condition defects int_0^R (1 - t/R) g_xx(0, t) dt - (1 - v(R)/R) at R = 1, 10, 100;
    sign of g_xx(0, y); min g_y on the x-axis."""
    m = hsm.m; ge = hs.GEval(m, m.beta_full(u)); ys = np.geomspace(1e-3, 1e3, 400); zeros = np.zeros_like(ys)
    V1, V2 = hs.hydro_V(ge, zeros, ys, n_in=32, n_tail=100); g, gx, gy = ge(zeros, ys); v = c * ys + V2
    vGp_G = v * gy - g                                                                  # G' = g_y(0, y)
    h = 1e-5 * (1 + ys); _, gxp, _ = ge(zeros + h, ys); _, gxm, _ = ge(zeros - h, ys); gxx = (gxp - gxm) / (2 * h)
    out = dict(max_vGp_minus_G=float(np.abs(vGp_G).max()), max_rel=float((np.abs(vGp_G) / (np.abs(g) + 1e-300)).max()), gxx_sign_changes=int((np.sign(gxx[1:]) != np.sign(gxx[:-1])).sum()), gxx_axis_min=float(gxx.min()), gxx_axis_max=float(gxx.max()))
    for R in [1.0, 10.0, 100.0]:
        tt = np.linspace(0, R, 2001)[1:]; _, gxpR, _ = ge(1e-5 * (1 + tt), tt); _, gxmR, _ = ge(-1e-5 * (1 + tt), tt); gxxR = (gxpR - gxmR) / (2e-5 * (1 + tt))
        I = np.trapz((1 - tt / R) * gxxR, tt); _, V2R = hs.hydro_V(ge, np.array([0.0]), np.array([R]), n_in=32, n_tail=100); vR = c * R + V2R[0]
        out[f'centre_defect_R{R:g}'] = float(I - (1 - vR / R))
    xs = np.geomspace(1e-3, 1e3, 400); _, _, gy_x = ge(xs, np.zeros_like(xs)); out['min_gy_xaxis'] = float(gy_x.min()); out['argmin_gy_xaxis'] = float(xs[np.argmin(gy_x)])
    return out


def run(args):
    kw = dict(a.split('=', 1) for a in args if '=' in a)
    N = int(kw.get('N', 48)); M = int(kw.get('M', 12)); c = float(kw.get('c', 3.0)); cfree = kw.get('cfree', '0') == '1'; centre = kw.get('centre', 'drop')
    maxit = int(kw.get('maxit', 40)); tag = kw.get('tag', f'hs_N{N}_c{c}'); n_in = int(kw.get('n_in', 24)); n_tail = int(kw.get('n_tail', 80)); start = kw.get('start', 'simple'); fine = kw.get('fine', '0') == '1'
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# hs_solve {now()} {kw}\n"); log.flush(); t0 = time.time()
    hsm = HSModel(N, M, c, n_in=n_in, n_tail=n_tail, fine=fine); log.write(f"# model built ({hsm.npts} collocation points, nu {hsm.m.nu}); building maps\n"); log.flush()
    hsm.build_maps(log=log); log.write(f"# maps built in {time.time()-t0:.0f}s\n"); log.flush()
    if start == 'simple': u = simple_start(hsm, c)
    else:
        st = torch.load(start, weights_only=False)  # a re-gauged chain state in the 3.72 frame is expected to be produced by hs_regauge_start (not yet)
        u = st['u'].to(hsm.dev)
    F, info = hsm.residual(u, c); nF = F.norm().item()
    log.write(f"# start: |F|2 {nF:.3e} |F|max {F.abs().max().item():.3e} a0 {info['a0'].item():.6f} K {info['K'].item():.6f} c {c}\n"); log.flush()
    for it in range(maxit):
        J = hsm.jacobian(u, c, cfree); U, S, Vh = torch.linalg.svd(J, full_matrices=False); keep = S > 1e-13 * S[0]
        du = Vh[keep].T @ ((U[:, keep].T @ (-F)) / S[keep]); lam = 1.0; acc = False
        for _ in range(30):
            un = u + lam * du[:hsm.m.nu]; cn = c + lam * du[-1].item() if cfree else c
            Fn, infon = hsm.residual(un, cn); nFn = Fn.norm().item()
            if nFn < (1 - 1e-4 * lam) * nF: acc = True; break
            lam *= 0.5
        if not acc: log.write(f"  it {it}: line search failed (lam {lam:.1e}); stop\n"); break
        u, c, F, info, nF = un, cn, Fn, infon, nFn
        log.write(f"  it {it}: |F|2 {nF:.3e} |F|max {F.abs().max().item():.3e} lam {lam:.3g} c {c:.8f} a0 {info['a0'].item():.6f} K {info['K'].item():.6f} smin {S[keep][-1].item():.2e} smax {S[0].item():.2e} ({int((~keep).sum())} dropped)\n"); log.flush()
        if F.abs().max().item() < 1e-12: break
    # diagnostics
    J = hsm.jacobian(u, c, False); S_all = torch.linalg.svdvals(J); S_res = torch.linalg.svdvals(J[:-2])          # with / without the centre+gauge rows
    a0, bc, ec = [z.item() for z in hsm.m.jets(u)]; ff = hsm.m.farfield(u)
    tab = sampled_table(hsm, u, c); ax = axis_diagnostics(hsm, u, c)
    res = dict(tag=tag, N=N, M=M, c=c, cfree=cfree, fine=fine, start=start, a0=a0, E=ec / a0, B=bc, K=ff['K'].item(), A1=ff['A1'].item(), A3=ff['A3'].item(), nodes_Fmax=F.abs().max().item(), nodes_F2=nF,
               smin_full=S_all[-1].item(), smin_rows_only=S_res[-1].item(), smin2_rows_only=S_res[-2].item(), smax=S_all[0].item(), sampled=tab, axis=ax, wall=time.time() - t0)
    log.write("# RESULT " + json.dumps(res) + "\n"); log.flush()
    torch.save(dict(u=u.cpu(), beta=hsm.m.beta_full(u).cpu(), c=c, cl=c, C=c, N=N, M=M, L=1.0, gamma=1 / c, p=hsm.m.p, basis='local', rcond=1e-8, rep='HS eps=0 state', result=res), f'runs/{tag}.pt')
    print(json.dumps(res, indent=1))
    return hsm, u, c, res


if __name__ == '__main__':
    run(sys.argv[1:])
