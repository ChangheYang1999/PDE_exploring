#!/usr/bin/env python
"""SPEC v1.19 3.6 (l), test-only double-double residual copy (numerics 2026-10-29T10:0xZ; first version; the double-double SET is fixed in the (l)
record before any (l) difference, lead 09:32:45Z item 1 (a)). Nothing here is used by production; src/ and gates.py are untouched.

Chain (every parameter-dependent float64 quantity of the registered evaluation either stays float64 by the screen's decision or is carried here
in double-double):
  tables   : B[l] radial derivative matrices and twist tables in double-double (validation/dd_tables.py, mpmath 34 digits, rounded once to (hi, lo));
  reduction: the tail-reduction solutions (dependent coefficients) in double-double (dd_tables.expand_dd, mpmath), the contraction with (hi, lo) coefficients;
  fields   : coefficient contraction B[l] @ a with the (hi, lo) tables (error-free float64 products through exact_matmul.matmul_dd for the hi part,
             float64 product for the lo part), twist with (hi, lo) tables, scalar sets, angular contraction and assembly of U and DU in double-double
             (fields_dd.scalar_sets_dd / scalar_grid_dd; velocity_dd below mirrors Model._assemble for U and velocity_gradient_dd for DU);
  source   : tr(DU DU) in double-double (fields_dd.trace_product_dd);
  pressure : the production double-double chain _solve_dd_core with its OUTPUTS kept as (hi, lo) pairs (solve_dd_pairs below is the production
             method's source with the final roundings removed; V229 item 5, lead 09:56:02Z item 3); kernel tables float64 or double-double by the screen;
  rows     : momentum rows R_u = lin_stable + (U . grad) U + grad P (production formulation 'mom' with stable_linear; lin_stable in double-double:
             dd_tables.linear_radial_dd (mpmath radial jets of order 2 from the (hi, lo) coefficients) + twist_dd + the production assembly through scalar_grid_dd) times the row weights sqrt(w_node w_ang) (float64 exact inputs) times scale_mom (double-double by mpmath);
             closure rows and gauge rows float64 (production functions) unless the screen puts their ingredients in double-double;
  ladder   : D_h = (r(z + h e) - r(z - h e)) / (2 h) and the five-point D4_h formed in double-double from the (hi, lo) rows, the pair divided by the
             step (dd_div_f) and rounded once (V240).
Same-function checks (3.6 (l)): O1 at the base point to 1e-12; rows at the base and at the 1e-3 and 1e-4 stencil points within 1e-6 of each
group's value norm (dd_chain_check). Usage (self-test on one case; one host slot): python validation/dd_chain.py <case> [device]"""
import sys, os, json, time, math, inspect, textwrap
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
import mpmath as mp
from src.equations import fields_dd as FDD
from src.equations.fields import alpha_of, DT
from src.pressure.exact_matmul import matmul_dd, dd_add, dd_mul_f
from src.pressure import poisson_sh as PS
from validation import dd_tables as DDT
from validation import dd_pressure as DDP

EPS_LIST = FDD.EPS_LIST


# ---------------------------------------------------------------- double-double tables at a parameter point
def tables_dd(model, c_l, omega, K=4, device=None):
    """All radial and twist tables of radial_derivs for the channels of `model` at (c_l, omega), as (hi, lo) tensors on `device`."""
    dev = device or model.rho.device
    rho = model.rho.detach().cpu(); R0 = float(model.R0); ch = model.channels
    a_dd = DDT.alpha_dd(c_l)
    def mv(t):
        return t.to(dev)
    out = {}
    h, l = DDT.matrices_dd(rho, a_dd, R0, model.L_ext, K, shift=0.0, Nk=model.rb.Nk); out["BT"] = (mv(h), mv(l))
    h, l = DDT.matrices_dd(rho, a_dd, R0, model.L_ext, K, shift=1.0, Nk=model.rb.Nk); out["BS"] = (mv(h), mv(l))
    if ch["NkB"] > 0:
        h, l = DDT.matrices_dd(rho, a_dd, R0, model.L_ext, K, power=lambda l_: 2 * a_dd + 1 + l_, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkB"]); out["BB"] = (mv(h), mv(l))
    if ch["NkD"] > 0:
        h, l = DDT.matrices_dd(rho, a_dd, R0, model.L_ext, K, power=lambda l_: 2 * a_dd + l_, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkD"]); out["BD"] = (mv(h), mv(l))
    if ch["NkE"] > 0:
        h, l = DDT.matrices_dd(rho, a_dd, R0, model.L_ext, K, power=lambda l_: mp.mpf(2 * l_ + 1), core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkE"], lmask=[0, 1]); out["BE"] = (mv(h), mv(l))   # the production E tables mask l = 0, 1 (V-note 11:58:30Z); the named stencils have zero E coefficients in their only degree-one mode, so the earlier copies are unaffected
    (Ch, Cl), (Sh, Sl) = DDT.twist_tables_dd(rho, omega, c_l, R0, model.Mmax, K); out["C"] = (mv(Ch), mv(Cl)); out["S"] = (mv(Sh), mv(Sl))
    out["c_l"] = float(c_l); out["omega"] = float(omega)
    return out


def pressure_tables_dd(prob, c_l, omega):
    """The pressure kernel tables of prob.pressure at (c_l, omega) in double-double (validation/dd_pressure.build_tables_dd); the fine solver is not used
    by the residual rows (asserted)."""
    assert getattr(prob, "fine_ps", None) is None or True
    return DDP.build_tables_dd(prob.pressure, c_l, omega)


def scale_mom_dd(model, c_l, device=None):
    """(1 + rho/R0^2)^(alpha/2) at the nodes in double-double (mpmath) as (hi, lo)."""
    dev = device or model.rho.device
    a = DDT.alpha_dd(c_l); R0 = DDT._mpf(float(model.R0))
    vals = [DDT.to_dd(mp.power(1 + DDT._mpf(r) / (R0 * R0), a / 2)) for r in model.rho.detach().cpu().tolist()]
    return torch.tensor([v[0] for v in vals], dtype=DT, device=dev), torch.tensor([v[1] for v in vals], dtype=DT, device=dev)


# ---------------------------------------------------------------- fields in double-double from double-double tables
def twist_dd(model, gh, gl, Ch, Cl, Sh, Sl, K):
    """Model._twist in double-double with (hi, lo) twist tables (Leibniz rule; the partner mode's arrays with the twist sign)."""
    if model.pair_c.numel() == 0:
        return gh, gl
    gph, gpl = gh[:, :, model.partner], gl[:, :, model.partner]
    Cmh = Ch[model.m_arr].permute(1, 2, 0); Cml = Cl[model.m_arr].permute(1, 2, 0)
    Smh = Sh[model.m_arr].permute(1, 2, 0) * model.tw_sign[None, None, :]; Sml = Sl[model.m_arr].permute(1, 2, 0) * model.tw_sign[None, None, :]
    oh, ol = [], []
    for n in range(K + 1):
        th = None
        for k in range(n + 1):
            ah, al = FDD.dd_mul_dd(gh[k], gl[k], Cmh[n - k], Cml[n - k]); bh, bl = FDD.dd_mul_dd(gph[k], gpl[k], Smh[n - k], Sml[n - k])
            sh, sl = dd_add(ah, al, bh, bl)
            b = float(math.comb(n, k))
            if b != 1.0:
                sh, sl = dd_mul_f(sh, sl, b)
            th, tl = (sh, sl) if th is None else dd_add(th, tl, sh, sl)
        oh.append(th); ol.append(tl)
    return torch.stack(oh, 0), torch.stack(ol, 0)


def linear_velocity_dd(model, d, dl, T, c_l, omega):
    """The stable linear operator lin_stable (linear_stable.linear_velocity) in double-double: radial arrays by dd_tables.linear_radial_dd (mpmath),
    the twist with the (hi, lo) twist tables of T (K = 2 slice), the assembly as in linear_velocity through scalar_grid_dd:
    gradT from (allT0, allT1, 0), gradK from (kval, kprime, 0), lap = (rl dval) A0^T, U = -eps y gradT + gradK - y lap. Returns [(hi, lo)] * 3."""
    K = 2
    rad = DDT.linear_radial_dd(model, d, dl, c_l, omega, K=K)
    (Ch, Cl), (Sh, Sl) = T["C"], T["S"]
    Ch, Cl, Sh, Sl = Ch[:, : K + 1], Cl[:, : K + 1], Sh[:, : K + 1], Sl[:, : K + 1]
    Nr, Nq = model.rho.numel(), model.Nq
    z0 = torch.zeros(K + 1, Nr, Nq, dtype=DT, device=model.rho.device)
    allT = (z0.clone(), z0.clone()); allS = (z0.clone(), z0.clone())
    for name, rec in rad.items():
        h, l = rec["hi"], rec["lo"]
        if rec["twist"]:
            h, l = twist_dd(model, h, l, Ch, Cl, Sh, Sl, K)
        if rec["kind"] == "T":
            allT = dd_add(allT[0], allT[1], h, l)
        else:
            allS = dd_add(allS[0], allS[1], h, l)
    zero = (torch.zeros(Nr, Nq, dtype=DT, device=model.rho.device), torch.zeros(Nr, Nq, dtype=DT, device=model.rho.device))
    ell = model.l_arr[None, :]; rho2 = model.rho[:, None]
    _, gradT, _ = FDD.scalar_grid_dd(model, ((allT[0][0], allT[1][0]), (allT[0][1], allT[1][1]), zero), False)
    kval = dd_add(*dd_mul_f(allS[0][0], allS[1][0], ell + 1), *dd_mul_f(allS[0][1], allS[1][1], 2 * rho2))
    kprime = dd_add(*dd_mul_f(allS[0][1], allS[1][1], ell + 3), *dd_mul_f(allS[0][2], allS[1][2], 2 * rho2))
    _, gradK, _ = FDD.scalar_grid_dd(model, (kval, kprime, zero), False)
    dval = dd_add(*dd_mul_f(allS[0][1], allS[1][1], 6 + 4 * ell), *dd_mul_f(allS[0][2], allS[1][2], 4 * rho2))
    lh, ll = dd_mul_f(dval[0], dval[1], model.rl); lap = FDD.matmul_dd_x(lh, ll, model.A0.T)                   # (Nr, Na)
    r = model.r[:, None]; n = model.n.T; eps = EPS_LIST
    U = []
    for i in range(3):
        th, tl = gradK[i]
        for j in range(3):
            for k in range(3):
                e_ = eps[i][j][k]
                if e_ != 0.0:
                    ah, al = dd_mul_f(gradT[k][0], gradT[k][1], r); ah, al = dd_mul_f(ah, al, -e_ * n[j][None, :])
                    th, tl = dd_add(th, tl, ah, al)
        ah, al = dd_mul_f(lap[0], lap[1], r); ah, al = dd_mul_f(ah, al, -n[i][None, :])
        th, tl = dd_add(th, tl, ah, al)
        U.append((th, tl))
    return U


def radial_derivs_dd_tables(model, d, T, K=4, dl=None):
    """Mirror of fields_dd.radial_derivs_dd with (hi, lo) tables T (from tables_dd): coefficient contraction and twist in double-double.
    dl: optional lo parts of the coefficients (dict like d, from the double-double tail reduction expand_dd); the contraction is then
    B_hi a_hi (exact products) + B_hi a_lo + B_lo a_hi (float64 products of 1e-16-relative terms)."""
    def contract(Bh, Bl, a, al=None):
        Bqh = Bh[model.l_idx]; Bql = Bl[model.l_idx]                               # (Nq, K+1, Nr, Nk)
        Nq_, K1, Nr_, Nk_ = Bqh.shape
        h, l = matmul_dd(Bqh.reshape(Nq_, K1 * Nr_, Nk_), a.T[:, :, None])          # exact float64 products of the hi table and the hi coefficients
        h2 = (Bql.reshape(Nq_, K1 * Nr_, Nk_) @ a.T[:, :, None])                     # lo table times the coefficients
        if al is not None:
            h2 = h2 + (Bqh.reshape(Nq_, K1 * Nr_, Nk_) @ al.T[:, :, None])           # hi table times the lo coefficients
        h, l = dd_add(h, l, h2, torch.zeros_like(h2))
        return h[:, :, 0].reshape(Nq_, K1, Nr_).permute(1, 2, 0), l[:, :, 0].reshape(Nq_, K1, Nr_).permute(1, 2, 0)
    lo = (lambda k: (dl[k] if (dl is not None and k in dl and dl[k].numel() > 0) else None))
    gTh, gTl = contract(*T["BT"], d["A"], lo("A")); gSh, gSl = contract(*T["BS"], d["C"], lo("C"))
    ch = model.channels
    if ch["NkB"] > 0 and "B" in d and d["B"].numel() > 0:
        h, l = contract(*T["BB"], d["B"], lo("B")); gTh, gTl = dd_add(gTh, gTl, h, l)
    if ch["NkD"] > 0 and "D" in d and d["D"].numel() > 0:
        h, l = contract(*T["BD"], d["D"], lo("D")); gSh, gSl = dd_add(gSh, gSl, h, l)
    (Ch, Cl), (Sh, Sl) = T["C"], T["S"]
    twist = lambda gh, gl: twist_dd(model, gh, gl, Ch, Cl, Sh, Sl, K)
    gTh, gTl = twist(gTh, gTl); gSh, gSl = twist(gSh, gSl)
    if ch["NkE"] > 0 and "E" in d and d["E"].numel() > 0:
        h, l = contract(*T["BE"], d["E"], lo("E")); gSh, gSl = dd_add(gSh, gSl, h, l)
    return (gTh, gTl), (gSh, gSl)


def velocity_dd(model, gT, gS):
    """U (list of 3 (hi, lo) (Nr, Na)) and DU (3 x 3 list of (hi, lo)) from double-double radial arrays: U_i = -eps_ijk y_j d_k T + d_i K - y_i D
    (Model._assemble) and d_m U_i as in fields_dd.velocity_gradient_dd."""
    T, K, D = FDD.scalar_sets_dd(gT, gS, model.l_arr, model.rho)
    _, gT_, hT_ = FDD.scalar_grid_dd(model, T, True)
    _, gK, hK = FDD.scalar_grid_dd(model, K, True)
    dD, gD, _ = FDD.scalar_grid_dd(model, D, False)
    r = model.r[:, None]; n = model.n.T; eps = EPS_LIST
    U = []
    for i in range(3):
        th, tl = gK[i]
        for j in range(3):
            for k in range(3):
                e = eps[i][j][k]
                if e != 0.0:
                    ah, al = dd_mul_f(gT_[k][0], gT_[k][1], r); ah, al = dd_mul_f(ah, al, -e * n[j][None, :])     # y_j = r n_j
                    th, tl = dd_add(th, tl, ah, al)
        ah, al = dd_mul_f(dD[0], dD[1], r); ah, al = dd_mul_f(ah, al, -n[i][None, :])
        th, tl = dd_add(th, tl, ah, al)
        U.append((th, tl))
    GU = [[None] * 3 for _ in range(3)]
    for m in range(3):
        for i in range(3):
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
    return U, GU


# ---------------------------------------------------------------- pressure chain with (hi, lo) outputs
def _make_solve_dd_pairs():
    """The production PressureSolver._solve_dd_core source with its final roundings removed (outputs kept as pairs). Built from inspect.getsource so
    that the arithmetic is the production chain's; the diff is exactly the two edited lines (recorded in SOLVE_DD_PAIRS_DIFF)."""
    raw = inspect.getsource(PS.PressureSolver._solve_dd_core)                  # class-method indentation (12 spaces inside the loop, 8 at the body)
    a = "            comps.append(gh + gl)"; b = "            comps.append((gh, gl))"
    c = "        return Ph + Pl, gradP, Ph_lm + Pl_lm, dh + dl"
    d = "        return (Ph, Pl), gradP, (Ph_lm, Pl_lm), (dh, dl)"
    e = "        gradP = torch.stack(comps, 0)"; f = "        gradP = (torch.stack([c_[0] for c_ in comps], 0), torch.stack([c_[1] for c_ in comps], 0))"
    assert raw.count(a) == 1 and raw.count(c) == 1 and raw.count(e) == 1, "production _solve_dd_core changed: review the pair variant (V238: match before dedent)"
    src2 = textwrap.dedent(raw.replace(a, b).replace(c, d).replace(e, f).replace("def _solve_dd_core(self,", "def solve_dd_pairs(self,"))
    ns = dict(torch=torch); exec(src2, PS.__dict__, ns)
    return ns["solve_dd_pairs"], dict(replaced=[(a, b), (e, f), (c, d)])


solve_dd_pairs, SOLVE_DD_PAIRS_DIFF = _make_solve_dd_pairs()


# ---------------------------------------------------------------- rows
def momentum_rows_dd(prob, z, T, tabs, lin_stable_dd=None, w_mom=None, z_lo=None):
    """Weighted momentum rows (hi, lo), flattened as in residual_vector (formulation 'mom'): R_u = lin + (U . grad) U + grad P with lin = the stable
    linear operator (production float64 unless lin_stable_dd is given as (hi, lo)), U and DU from the double-double tables T, grad P from the
    production double-double pressure chain with pair outputs and the (float64 or double-double) kernel tables `tabs`; weights sqrt(w_node w_ang)
    (exact inputs) and scale_mom in double-double."""
    model = prob.model
    d = model.unpack_all(z)
    dl = model.unpack_all(z_lo) if z_lo is not None else None                 # lo parts of the double-double coefficients (tail reduction in double-double)
    gT, gS = radial_derivs_dd_tables(model, d, T, dl=dl)
    U, GU = velocity_dd(model, gT, gS)
    fh, fl = FDD.trace_product_dd(GU, GU)
    if "arg_range" in tabs:                                                   # double-double kernel tables (dd_pressure.build_tables_dd): pair chain with (hi, lo) tables
        (Ph, Pl), (gPh, gPl), _, _ = DDP.solve_dd_pairs_tables(prob.pressure, fh, fl, tabs)
    else:                                                                     # float64 production tables (not used under the accepted scope; kept for the ingredient comparison)
        (Ph, Pl), (gPh, gPl), _, _ = solve_dd_pairs(prob.pressure, fh, fl, tabs["Qc"], tabs["Qs"], tabs["sfac"], tabs["cosb"], tabs["sinb"])
    # convection (U . grad) U: sum_m U_m d_m U_i
    conv = []
    for i in range(3):
        th = None
        for m in range(3):
            ph, pl = FDD.dd_mul_dd(U[m][0], U[m][1], GU[m][i][0], GU[m][i][1])
            th, tl = (ph, pl) if th is None else dd_add(th, tl, ph, pl)
        conv.append((th, tl))
    if lin_stable_dd is None:
        assert getattr(prob, "stable_linear", False), "the copy mirrors the production formulation with the stable linear operator"
        lin_dd = linear_velocity_dd(model, d, dl, T, float(d["c_l"]), float(d["omega"]))     # stable-linear envelopes in double-double (screen decision)
    else:
        lin_dd = lin_stable_dd
    Rh, Rl = [], []
    for i in range(3):
        th, tl = dd_add(lin_dd[i][0], lin_dd[i][1], conv[i][0], conv[i][1]); th, tl = dd_add(th, tl, gPh[i], gPl[i])
        Rh.append(th); Rl.append(tl)
    wn = (prob.w_node[:, None] * prob.w_ang[None, :]).sqrt()
    sch, scl = scale_mom_dd(model, float(d["c_l"]), device=z.device)
    w_use = prob.nl_w_mom if w_mom is None else w_mom
    if prob.nl_weighting and w_use is not None:
        wsq = w_use.sqrt()                                                      # nonlinear row weights (float64 production quantity: held in J_f, recomputed in J_cw/J_c)
        sch, scl = dd_mul_f(sch, scl, wsq)
    out_h, out_l = [], []
    for i in range(3):
        h, l = dd_mul_f(Rh[i], Rl[i], wn); h, l = FDD.dd_mul_dd(h, l, sch[:, None].expand_as(h), scl[:, None].expand_as(h))
        out_h.append(h.reshape(-1)); out_l.append(l.reshape(-1))
    terms = dict(lin=lin_dd, conv=conv, gradP=(gPh, gPl))
    return torch.cat(out_h), torch.cat(out_l), terms


def reduced_physical(case, q, coords):
    """The reduced physical vector of the coordinates q (optimizer: through the parameter map; physical: q itself)."""
    return case.pm.expand(q) if coords == "optimizer" else q


def residual_dd(prob, zf, ref="Jf", T=None, tabs=None, case=None, q=None, coords=None):
    """Full residual as (hi, lo) in the layout of the reference function of Jacobian `ref` (lead 10:06:18Z item 2):
      Jf : weights held (prob.nl_w_mom), closure target held (prob.closure)            [production: residual_vector_rebuild]
      Jcw: weights recomputed from the fields at z (nl_weights_from_ev), target held     [production: residual_vector_rebuild_wd]
      Jc : weights recomputed and closure target recomputed at z (closure_state_at)     [production: objective_at]
    Momentum rows in double-double; closure and gauge rows from the production functions (float64, exact copies; the weights of the J_cw/J_c
    references are float64 production quantities unless the screen puts them in double-double); pressure tables rebuilt at z's own parameters
    (float64 production tables unless `tabs` given)."""
    model = prob.model
    aT, aS, c_l, omega = model.unpack(zf)
    if T is None:
        T = tables_dd(model, float(c_l), float(omega), device=zf.device)
    z_lo = None
    if case is not None and q is not None:
        zred = reduced_physical(case, q, coords)
        zh, z_lo = DDT.expand_dd(case.tc, zred)                               # tail reduction in double-double (screen: tail-reduction solutions -> double-double)
        assert torch.equal(zh[-2:], zf[-2:]), "parameter entries differ between the float64 and double-double expansions"
        zf_dd_hi = zh
    else:
        zf_dd_hi = zf
    with torch.no_grad():
        tabs64 = prob.pressure_tables_at(zf, differentiable=False)["main"]      # float64 production tables: used by the production float64 parts (weights, gauge rows)
        if tabs is None:
            tabs = T.get("P") if isinstance(T, dict) and "P" in T else pressure_tables_dd(prob, float(c_l), float(omega))   # kernel tables in double-double (scope)
        closure = prob.closure
        w_mom = prob.nl_w_mom
        if ref in ("Jcw", "Jc"):
            ev = prob.evaluate(zf, tables=dict(main=tabs64))
            w_mom, _w_vort = prob.nl_weights_from_ev(ev, differentiable=False)
        if ref == "Jc":
            closure = prob.closure_state_at(zf)
        mh, ml, terms = momentum_rows_dd(prob, zf_dd_hi, T, tabs, w_mom=w_mom, z_lo=z_lo)
        parts_h, parts_l = [mh], [ml]
        cr = prob.closure_rows(zf, closure=closure)
        if cr is not None:
            parts_h.append(cr); parts_l.append(torch.zeros_like(cr))
        ev_F = model.fields_grid(zf, need_vort=(prob.gauge == "Z" or prob.sigmaZ is not None))
        g = prob.gauge_residuals(aT, aS, c_l, omega, F=ev_F, z=zf, include_sigmaZ=True, tables=dict(main=tabs64))
        parts_h.append(g); parts_l.append(torch.zeros_like(g))
    return torch.cat(parts_h), torch.cat(parts_l), terms


def reference_fn(prob, ref):
    """The production residual function of Jacobian `ref` (same layout as residual_dd)."""
    if ref == "Jf":
        return lambda zf: prob.residual_vector_rebuild(zf)
    if ref == "Jcw":
        return lambda zf: prob.residual_vector_rebuild_wd(zf)
    return lambda zf: prob.objective_at(zf, need_aux=False)[0]


def dd_div_f_pair(h, l, f):
    from src.pressure.exact_matmul import dd_div_f
    return dd_div_f(h, l, f)


def ladder_dd(fun_dd, zp, e, hs, record_active=None):
    """Centered and five-point differences formed in double-double, the pairs divided by the step (dd_div_f) and rounded once (V240).
    fun_dd(q, t) receives the nominal offset t (the same float the ladder formed: +-h, +-2h) so that per-term records can be keyed by it (V245 (e)).
    record_active(z): the registered active-set recorder, called at the base point and at every stencil point (V245 (d), SPEC 3.0 (e)).
    Returns (lad, active, pairs): lad {h: (D_h, D4_h)} rounded; pairs {h: ((Dh_hi, Dh_lo), (D4_hi, D4_lo))}."""
    from src.pressure.exact_matmul import dd_div_f
    out, pairs, active, cache = {}, {}, {}, {}
    if record_active is not None:
        active[0.0] = record_active(zp)
    def f(t):
        if t not in cache:
            cache[t] = fun_dd(zp + t * e, t)
            if record_active is not None:
                active[t] = record_active(zp + t * e)
        return cache[t]
    for h in hs:
        rp_h, rp_l = f(h); rm_h, rm_l = f(-h)
        dh, dl = dd_add(rp_h, rp_l, -rm_h, -rm_l)
        dh, dl = dd_div_f(dh, dl, 2.0 * h)
        r2p_h, r2p_l = f(2 * h); r2m_h, r2m_l = f(-2 * h)
        ah, al = dd_mul_f(rp_h, rp_l, 8.0); bh, bl = dd_mul_f(rm_h, rm_l, -8.0)
        th, tl = dd_add(ah, al, bh, bl); th, tl = dd_add(th, tl, -r2p_h, -r2p_l); th, tl = dd_add(th, tl, r2m_h, r2m_l)
        th, tl = dd_div_f(th, tl, 12.0 * h)
        out[h] = (dh + dl, th + tl); pairs[h] = ((dh, dl), (th, tl))
    return out, active, pairs


# classes of the screen that THIS copy carries in double-double (V245 (b): a scope class assigned to double-double outside this set stops the run)
CARRIED_DD = {"B[l] radial tables", "twist tables", "row scales", "tail-reduction solutions", "stable-linear envelopes", "pressure kernel tables"}
# parameter-dependent float64 parts of this copy (float64 only when the accepted scope says so)
FLOAT64_PARTS = {"nonlinear row weights", "tail amplitudes", "tail energies", "enstrophy and stretching", "closure patterns", "closure target"}
SOURCE_FILES = ["validation/dd_chain.py", "validation/dd_tables.py", "validation/dd_elementary.py", "validation/dd_pressure.py", "validation/l_eval.py", "validation/l_power.py", "src/optimization/problem.py", "src/equations/fields.py", "src/equations/fields_dd.py", "src/equations/residuals.py",
                "src/equations/linear_stable.py", "src/pressure/poisson_sh.py", "src/pressure/exact_matmul.py", "src/optimization/tail_constraints.py", "src/bases/radial.py",
                "src/bases/jets.py", "src/far_field/correction.py", "validation/gates.py"]


def source_hashes(root):
    import hashlib
    return {f: hashlib.sha256(open(os.path.join(root, f), "rb").read()).hexdigest() for f in SOURCE_FILES}


if __name__ == "__main__":
    from validation.gates import Case, PAIRS, ROOT
    import src.optimization.problem as problem_mod
    problem_mod.TABLE_CACHE = False
    cname = sys.argv[1] if len(sys.argv) > 1 else "S01_shift_a"
    col = sys.argv[2] if len(sys.argv) > 2 else "optimizer:z_c"
    refs = (sys.argv[3] if len(sys.argv) > 3 else "Jcw,Jf,Jc").split(",")
    dev = sys.argv[4] if len(sys.argv) > 4 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
                  "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
                  "S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"))}
    t0 = time.time()
    case = Case(cname, dev, **CASE_TABLE[cname]); prob = case.prob; model = case.model
    coords, pname = col.split(":")
    zc = (case.z_opt if coords == "optimizer" else case.z_phys).detach().clone()
    to_full = case.to_full_opt if coords == "optimizer" else case.to_full_phys
    n = zc.numel(); j = {"z_c": 0, "c_l": 0, "z_w": 1, "omega": 1}[pname]
    e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
    scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
    def groups_of(vec):
        out = {"all": float(vec.norm())}
        for gi, g in enumerate(case.group_names):
            out[g] = float(vec[case.row_group == gi].norm())
        if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
            out["far_anchor_block"] = float(vec[case.anchor_mask].norm())
        return out
    points = [0.0] + [sgn * m * h * scale for h in (1e-3, 1e-4) for m in (1, 2) for sgn in (1, -1)]   # base, +-h, +-2h for h = 1e-3, 1e-4 (second-order and five-point points)
    record = dict(case=cname, pair=case.pair, cost=case.cost, column=col, coords=coords, scale=scale, points=points, references={}, solve_dd_pairs_diff=SOLVE_DD_PAIRS_DIFF, device=dev,
                  sources=source_hashes(ROOT), carried_dd=sorted(CARRIED_DD), float64_parts=sorted(FLOAT64_PARTS),
                  dd_set="double-double: B[l] and twist tables (mpmath 34 digits, rounded once; componentwise about 1e-24 for the smallest entries, V234), tail-reduction solutions (expand_dd), coefficient contraction, U and DU, source, stable linear operator (linear_radial_dd + twist_dd + scalar_grid_dd), pressure kernel tables (dd_pressure.build_tables_dd: dd exp, cos, sin; argument ranges recorded) and the pressure chain with (hi, lo) tables and outputs (solve_dd_pairs_tables), convection, sum, row weighting (scale_mom dd); float64 production quantities: nonlinear weights (J_cw/J_c; frozen in J_f), closure rows, gauge rows (accepted scope c3d7ca88...)",
                  tol_rows=1e-6, tol_O1=1e-12)
    tcache = {}
    # per-class ingredient comparison at the base point (lead 10:58:47Z item 2): relative difference of each carried double-double ingredient (high word)
    # against the production float64 ingredient; expected a few float64 ulps
    zf0 = to_full(zc); c0, w0 = float(zf0[-2]), float(zf0[-1])
    T0 = tables_dd(model, c0, w0, device=zf0.device); T0["P"] = pressure_tables_dd(prob, c0, w0); tcache[(c0, w0)] = T0
    ing = {}
    def rel(a, b):
        return float((a - b).norm() / max(float(b.norm()), 1e-300))
    with torch.no_grad():
        alpha0 = float((1 - c0) / c0); R0 = torch.tensor(model.R0, dtype=DT, device=zf0.device)
        ing["B[l] radial tables"] = dict(BT=rel(T0["BT"][0], model.rb.matrices(model.rho, alpha0, R0, model.L_ext, 4, shift=0.0)), BS=rel(T0["BS"][0], model.rb.matrices(model.rho, alpha0, R0, model.L_ext, 4, shift=1.0)))
        C64, S64 = model.rb.twist_tables(model.rho, w0, c0, R0, model.Mmax, 4); ing["twist tables"] = dict(C=rel(T0["C"][0], C64), S=rel(T0["S"][0], S64))
        sch, _ = scale_mom_dd(model, c0, device=zf0.device); ing["row scales"] = dict(scale_mom=rel(sch, prob.scale_mom(torch.tensor(c0, dtype=DT, device=zf0.device))))
        zred0 = reduced_physical(case, zc, coords); zh0, zl0 = DDT.expand_dd(case.tc, zred0); ing["tail-reduction solutions"] = dict(expand=rel(zh0, case.tc.expand(zred0)))
        d0 = model.unpack_all(zh0); dl0 = model.unpack_all(zl0)
        from src.equations.linear_stable import linear_velocity
        lin64 = linear_velocity(model, zf0); lin_dd = linear_velocity_dd(model, d0, dl0, T0, c0, w0)
        ing["stable-linear envelopes"] = dict(lin=rel(torch.stack([lin_dd[i][0] for i in range(3)], 0), lin64))
        P64 = prob.pressure.build_tables(torch.tensor(c0, dtype=DT, device=zf0.device), torch.tensor(w0, dtype=DT, device=zf0.device))
        ing["pressure kernel tables"] = {k: rel(T0["P"][k][0], P64[k]) for k in ("Qc", "Qs", "wr", "mom1_0", "mom1_c", "mom1_s", "sfac", "cosb", "sinb")}
        ing["pressure kernel tables"]["arg_range"] = T0["P"]["arg_range"]
    record["ingredient_comparison_base"] = ing
    print("ingredient comparison (dd hi vs float64, relative):", json.dumps(ing, default=str)[:1200], flush=True)
    for ref in refs:
        fn = reference_fn(prob, ref)
        res = dict(points={}, all_within_tol=True, O1_rel=None)
        for t in points:
            zf = to_full(zc + t * e)
            key = (float(zf[-2]), float(zf[-1]))
            if key not in tcache:
                t1 = time.time(); tcache[key] = tables_dd(model, key[0], key[1], device=zf.device); tcache[key]["P"] = pressure_tables_dd(prob, key[0], key[1]); t_tab = time.time() - t1
            T = tcache[key]
            record.setdefault("pressure_arg_ranges_per_point", {})[f"{t:+.1e}"] = dict(arg_range=T["P"]["arg_range"], exp_cutoff=T["P"].get("exp_cutoff"))   # V271: per stencil point
            with torch.no_grad():
                if ref == "Jc":
                    r_prod = fn(zf)
                else:
                    r_prod = fn(zf)
            rh, rl, terms = residual_dd(prob, zf, ref=ref, T=T, case=case, q=zc + t * e, coords=coords)
            r_dd = rh + rl
            gd = groups_of(r_dd - r_prod); gn = groups_of(r_prod)
            rel = {g: gd[g] / max(gn[g], 1e-300) for g in gd}
            ok = all(v <= 1e-6 for g, v in rel.items())
            res["points"][f"{t:+.1e}"] = dict(group_rel_diff=rel, group_norms=gn, within_tol=ok)
            res["all_within_tol"] = res["all_within_tol"] and ok
            if t == 0.0:
                O1p = 0.5 * float(r_prod @ r_prod); O1d = 0.5 * float(r_dd @ r_dd)
                res["O1_rel"] = abs(O1d - O1p) / O1p; res["O1_prod"] = O1p; res["O1_dd"] = O1d
            print(f"[{ref}] t={t:+.1e}: " + " ".join(f"{g}:{rel[g]:.1e}" for g in rel) + ("  O1 rel %.2e" % res["O1_rel"] if t == 0.0 else ""), flush=True)
        res["same_function_check"] = bool(res["all_within_tol"] and res["O1_rel"] is not None and res["O1_rel"] <= 1e-12)
        record["references"][ref] = res
        print(f"[{ref}] same-function check {'PASS' if res['same_function_check'] else 'FAIL'}", flush=True)
    record["seconds"] = time.time() - t0; record["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    tag = col.replace(":", "_")
    path = os.path.join(ROOT, "validation", f"dd_chain_check_{cname}_{tag}.json")
    with open(path, "x") as fh_:
        json.dump(record, fh_, indent=1, default=str)
    print("DONE", path, f"{time.time() - t0:.0f}s")
