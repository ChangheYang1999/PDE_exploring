#!/usr/bin/env python
"""SPEC v1.19 3.6 (l) copy: the pressure kernel tables of PressureSolver.build_tables in double-double (test-only), and the production double-double
pressure chain with (hi, lo) tables and (hi, lo) outputs. Mirrors build_tables statement by statement: the parameter-dependent factors are
beta_q = omega/(2 c_l) log1p_q (double-double scalar times exact float64), cos and sin of m beta_q (dd_elementary.sincos_dd), base_l = -p0 logss +
le (logs - logssabs) with p0 = 2 alpha + 2 in double-double and the parameter-independent geometry logs as exact float64 inputs, the kernels
exp(logk) w (dd_elementary.exp_dd; the production masks give exact zeros without evaluating the masked arguments; the production clamp at 700
is asserted inactive on the unmasked arguments), the Green-sum accumulations K1 @ (cm Phi), K2 @ (sm Phi) as double-double matrix products
(exact float64 products of the high parts, float64 products of the cross terms), the volume weights wr, the l = 1 moments and the node factors
sfac, cosb, sinb. The exterior-monopole branch is asserted off (production). The argument ranges of exp, cos and sin are recorded (lead
10:56:41Z item 2 (a)). solve_dd_pairs_tables is _solve_dd_core with (hi, lo) tables and pair outputs (the production chain's operations)."""
import os, sys, math, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch
from src.pressure.exact_matmul import matmul_dd, matmul_dd_x, matmul_x_dd, dd_mul_f, dd_add, dd_div_f
from src.equations.fields_dd import dd_mul_dd
from validation.dd_elementary import exp_dd, sincos_dd
from validation import dd_tables as DDT
import mpmath as mp

DT = torch.float64
ARG_RANGE = dict(exp=[float("inf"), float("-inf")], trig=[float("inf"), float("-inf")], count_exp=0, count_trig=0)


def _rng(key, t):
    if t.numel():
        ARG_RANGE[key][0] = min(ARG_RANGE[key][0], float(t.min())); ARG_RANGE[key][1] = max(ARG_RANGE[key][1], float(t.max()))
        ARG_RANGE["count_" + key] += int(t.numel())


def dd_scalar(x):
    """(hi, lo) of an mpf scalar as 0-dim tensors."""
    h, l = DDT.to_dd(x)
    return torch.tensor(h, dtype=DT), torch.tensor(l, dtype=DT)


def matmul_dd_dd(Ah, Al, Bh, Bl):
    """(Ah + Al) @ (Bh + Bl) in double-double: exact products of the high parts plus the float64 cross terms."""
    h, l = matmul_dd(Ah, Bh)
    cross = Ah @ Bl + Al @ Bh
    return dd_add(h, l, cross, torch.zeros_like(cross))


def build_tables_dd(ps, c_l, omega, trig=None, cutoff_zero=False):
    """Double-double version of ps.build_tables(c_l, omega) (default p0 = 2 alpha + 2, exterior_monopole off). Returns dict of (hi, lo) pairs with the
    production keys plus the argument ranges OF THIS BUILD (the accumulator is reset at the start, V271) and the exp cutoff accounting (lead 11:29:05Z
    (a): count of active exp arguments with exp(x) < 1e-250, i.e. x < -575.65, per kernel, and the largest quadrature weight multiplying them).
    trig: optional callable (h, l) -> ((sin_h, sin_l), (cos_h, cos_l)) replacing dd_elementary.sincos_dd (qualification runs, lead 11:29:05Z (b)).
    cutoff_zero: qualification variant (lead 11:41:09Z; V282): EVERY exp factor of the tables (the kernels K1, K2, the volume-weight factor of wr, the l = 1
    moment factor, the node factors sfac) whose argument is below the cutoff is set to exact zero BEFORE the sums, so that the effect of the cutoff region
    on the (l) differences can be measured by replacement. Classification (V282): the implemented rule is the HIGH-WORD rule hi < -575.6462732485114
    (the binary64 nearest to ln(1e-250)); the counts are taken on the unclipped arguments in BOTH variants (so the cutoff variant reports the removed terms),
    per factor, and 'boundary_ambiguous' counts the arguments whose pair (hi, lo) lies within |lo| + one ulp of the threshold, i.e. the only arguments for
    which the high-word rule could differ from exp(hi + lo) < 1e-250; zero on all factors justifies the equivalence on these inputs."""
    assert not ps.exterior_monopole, "the double-double tables mirror the production configuration with exterior_monopole off"
    for k in ("exp", "trig"):
        ARG_RANGE[k] = [float("inf"), float("-inf")]; ARG_RANGE["count_" + k] = 0
    thr = -575.6462732485114
    cutoff = dict(threshold_x=thr, threshold_rule="high word hi < threshold_x (binary64 nearest to ln(1e-250) = -575.64627324851142100...; |ln(1e-250) - threshold_x| < 5.7e-14)",
                  count_k1=0, count_k2=0, max_weight_k1=0.0, max_weight_k2=0.0, count_wr=0, count_mom1=0, count_sfac=0, count_other=0,
                  boundary_ambiguous=dict(k1=0, k2=0, wr=0, mom1=0, sfac=0), ulp_threshold=float(abs(thr) * 2.0 ** -52), counts_on="unclipped arguments (both variants)",
                  boundary_within_1e_12=dict(k1=0, k2=0, wr=0, mom1=0, sfac=0), boundary_within_1e_12_rule="lead 12:12:12Z item 3: arguments with |x - ln(1e-250)| < 1e-12, x = hi + lo (the low word included)",
                  boundary_listing={})
    def _amb(h, l, mask=None, label=None):
        """boundary accounting: (i) arguments whose high-word classification could differ from the paired one: |hi - thr| <= |lo| + ulp(thr); (ii) the lead's count
        |hi + lo - thr| < 1e-12 (12:12:12Z item 3); the arguments of (ii) are listed (hi, lo, flat index; at most 50 per factor) so that they can be run both ways."""
        d = (h - thr) + l
        a = (h - thr).abs() <= (l.abs() + cutoff["ulp_threshold"]); b = d.abs() < 1e-12
        if mask is not None:
            a = a & mask; b = b & mask
        if label is not None:
            cutoff["boundary_within_1e_12"][label] += int(b.sum())
            if bool(b.any()):
                idx = torch.nonzero(b.reshape(-1)).reshape(-1)[:50]
                cutoff["boundary_listing"].setdefault(label, []).extend([dict(flat_index=int(i), hi=float(h.reshape(-1)[i]), lo=float(l.reshape(-1)[i]), below_threshold_high_word=bool(h.reshape(-1)[i] < thr)) for i in idx])
        return int(a.sum())
    def _cut(eh, el, argh, label):
        """cutoff_zero replacement of one exp factor: exact zero where the high word is below the threshold (no change when cutoff_zero is False)"""
        if not cutoff_zero:
            return eh, el
        keep = argh >= thr
        return torch.where(keep, eh, torch.zeros_like(eh)), torch.where(keep, el, torch.zeros_like(el))
    sincos = sincos_dd if trig is None else trig
    dev = ps.device; q = ps.q; Lfp = ps.Lf + 1; M = ps.Mmax; Ne, Nr = ps.Ne, ps.Nr_tab; Nq = q["w"].numel()
    clm = DDT._mpf(c_l); om = DDT._mpf(omega); alpha = (1 - clm) / clm; p0 = 2 * alpha + 2
    p0h, p0l = dd_scalar(p0); bh, bl = dd_scalar(om / (2 * clm))
    p0h, p0l, bh, bl = p0h.to(dev), p0l.to(dev), bh.to(dev), bl.to(dev)
    # beta at the quadrature points and the twisted-frame cos/sin tables (M+1, Nq)
    beta_h, beta_l = dd_mul_f(bh.expand(Nq), bl.expand(Nq), q["log1p_q"])
    cm_h, cm_l, sm_h, sm_l = [], [], [], []
    for m in range(M + 1):
        ah, al = dd_mul_f(beta_h, beta_l, float(m)); _rng("trig", ah)
        (sh, sl), (ch, cl) = sincos(ah, al)
        cm_h.append(ch); cm_l.append(cl); sm_h.append(sh); sm_l.append(sl)
    cm_h, cm_l, sm_h, sm_l = (torch.stack(t, 0) for t in (cm_h, cm_l, sm_h, sm_l))
    # base_l = -p0 logss + le (logs - logssabs): (Lfp, Nq) as pairs
    t1h, t1l = dd_mul_f(-p0h.expand(Nq), -p0l.expand(Nq), q["logss"])                      # -p0 logss (dd)
    fixed = ps.le_l[:, None] * (q["logs"] - q["logssabs"])[None, :]                           # parameter independent float64 (exact input)
    base_h, base_l = dd_add(t1h[None, :].expand(Lfp, Nq), t1l[None, :].expand(Lfp, Nq), fixed, torch.zeros_like(fixed))
    lv = ps.l_vals
    acc = [None, None, None, None]
    for a0 in range(0, Nq, ps.point_chunk):
        sl_ = slice(a0, min(Nq, a0 + ps.point_chunk))
        logs_c = q["logs"][sl_]; w_c = q["w"][sl_]; below_c = q["below"][:, sl_]; bh_c, bl_c = base_h[:, sl_], base_l[:, sl_]
        f1 = (lv[:, None, None] + 2.0) * (logs_c[None, None, :] - q["log_re"][None, :, None]) + q["log_re"][None, :, None]      # (Lfp, Ne, nc) fixed
        f2 = lv[:, None, None] * (q["log_re"][None, :, None] - logs_c[None, None, :]) + logs_c[None, None, :]
        k1h, k1l = dd_add(f1, torch.zeros_like(f1), bh_c[:, None, :].expand_as(f1), bl_c[:, None, :].expand_as(f1))
        k2h, k2l = dd_add(f2, torch.zeros_like(f2), bh_c[:, None, :].expand_as(f2), bl_c[:, None, :].expand_as(f2))
        m1 = below_c[None].expand_as(k1h); m2 = ~m1
        assert bool((k1h[m1] <= 700.0).all()) and bool((k2h[m2] <= 700.0).all()), "the production clamp at 700 would be active: not mirrored in double-double"
        _rng("exp", k1h[m1]); _rng("exp", k2h[m2])
        c1 = (k1h < thr) & m1; c2 = (k2h < thr) & m2                     # counts on the unclipped (production-masked) arguments, in both variants (V282)
        cutoff["count_k1"] += int(c1.sum()); cutoff["count_k2"] += int(c2.sum())
        cutoff["boundary_ambiguous"]["k1"] += _amb(k1h, k1l, m1, "k1"); cutoff["boundary_ambiguous"]["k2"] += _amb(k2h, k2l, m2, "k2")
        if cutoff_zero:
            m1 = m1 & (k1h >= thr); m2 = m2 & (k2h >= thr)                  # the replacement: the masks are extended by the cutoff region
        if bool(c1.any()):
            cutoff["max_weight_k1"] = max(cutoff["max_weight_k1"], float(w_c[None, None, :].expand_as(k1h)[c1].abs().max()))
        if bool(c2.any()):
            cutoff["max_weight_k2"] = max(cutoff["max_weight_k2"], float(w_c[None, None, :].expand_as(k2h)[c2].abs().max()))
        e1h, e1l = exp_dd(torch.where(m1, k1h, torch.zeros_like(k1h)), torch.where(m1, k1l, torch.zeros_like(k1l)))
        e2h, e2l = exp_dd(torch.where(m2, k2h, torch.zeros_like(k2h)), torch.where(m2, k2l, torch.zeros_like(k2l)))
        e1h = torch.where(m1, e1h, torch.zeros_like(e1h)); e1l = torch.where(m1, e1l, torch.zeros_like(e1l))     # masks as exact zeros
        e2h = torch.where(m2, e2h, torch.zeros_like(e2h)); e2l = torch.where(m2, e2l, torch.zeros_like(e2l))
        K1h, K1l = dd_mul_f(e1h, e1l, w_c); K2h, K2l = dd_mul_f(e2h, e2l, w_c)
        K1h, K1l, K2h, K2l = (t.reshape(Lfp * Ne, -1) for t in (K1h, K1l, K2h, K2l))
        nc = K1h.shape[1]
        Pc_h, Pc_l = dd_mul_f(cm_h[:, sl_, None].expand(M + 1, nc, Nr), cm_l[:, sl_, None].expand(M + 1, nc, Nr), q["Phi"][None, sl_, :])
        Ps_h, Ps_l = dd_mul_f(sm_h[:, sl_, None].expand(M + 1, nc, Nr), sm_l[:, sl_, None].expand(M + 1, nc, Nr), q["Phi"][None, sl_, :])
        Pc_h = Pc_h.permute(1, 0, 2).reshape(nc, (M + 1) * Nr); Pc_l = Pc_l.permute(1, 0, 2).reshape(nc, (M + 1) * Nr)
        Ps_h = Ps_h.permute(1, 0, 2).reshape(nc, (M + 1) * Nr); Ps_l = Ps_l.permute(1, 0, 2).reshape(nc, (M + 1) * Nr)
        parts = [matmul_dd_dd(K1h, K1l, Pc_h, Pc_l), matmul_dd_dd(K2h, K2l, Pc_h, Pc_l), matmul_dd_dd(K1h, K1l, Ps_h, Ps_l), matmul_dd_dd(K2h, K2l, Ps_h, Ps_l)]
        for i in range(4):
            acc[i] = parts[i] if acc[i] is None else dd_add(acc[i][0], acc[i][1], parts[i][0], parts[i][1])
    inv = 1.0 / (2.0 * lv + 1.0)
    def finish(t1, t2):
        def shape(th):
            return torch.stack([th[0].reshape(Lfp, Ne, M + 1, Nr), th[1].reshape(Lfp, Ne, M + 1, Nr)], 0).permute(1, 3, 0, 2, 4)
        Th = torch.stack([t1[0].reshape(Lfp, Ne, M + 1, Nr), t2[0].reshape(Lfp, Ne, M + 1, Nr)], 0).permute(1, 3, 0, 2, 4)
        Tl = torch.stack([t1[1].reshape(Lfp, Ne, M + 1, Nr), t2[1].reshape(Lfp, Ne, M + 1, Nr)], 0).permute(1, 3, 0, 2, 4)
        return dd_mul_f(Th, Tl, inv[:, None, None, None, None])
    Qc = finish(acc[0], acc[1]); Qs = finish(acc[2], acc[3])
    # volume weights wr = (s2 exp(-p0 logss) w) @ Phi
    e_h, e_l = exp_dd(t1h, t1l); _rng("exp", t1h); cutoff["count_wr"] += int((t1h < thr).sum()); cutoff["boundary_ambiguous"]["wr"] += _amb(t1h, t1l, None, "wr")
    e_h, e_l = _cut(e_h, e_l, t1h, "wr")
    vh, vl = dd_mul_f(e_h, e_l, q["s2"] * q["w"])
    wr = matmul_dd_x(vh[None, :], vl[None, :], q["Phi"]); wr = (wr[0][0], wr[1][0])
    # l = 1 moments: base1 = exp(-p0 logss + (logs - logssabs)) w
    g1h, g1l = dd_add(t1h, t1l, q["logs"] - q["logssabs"], torch.zeros_like(t1h)); _rng("exp", g1h)
    b1h, b1l = exp_dd(g1h, g1l); cutoff["count_mom1"] += int((g1h < thr).sum()); cutoff["boundary_ambiguous"]["mom1"] += _amb(g1h, g1l, None, "mom1")
    b1h, b1l = _cut(b1h, b1l, g1h, "mom1"); b1h, b1l = dd_mul_f(b1h, b1l, q["w"])
    (sb_h, sb_l), (cb_h, cb_l) = sincos(beta_h, beta_l); _rng("trig", beta_h)
    def mom(fh, fl):
        r_ = matmul_dd_x(fh[None, :], fl[None, :], q["Phi"]); return (r_[0][0], r_[1][0])
    mom1_0 = mom(b1h, b1l)
    xh, xl = dd_mul_dd(b1h, b1l, cb_h, cb_l); mom1_c = mom(xh, xl)
    xh, xl = dd_mul_dd(b1h, b1l, sb_h, sb_l); mom1_s = mom(xh, xl)
    # node factors
    sfh, sfl = dd_mul_f(p0h.expand_as(ps.log_s_nodes), p0l.expand_as(ps.log_s_nodes), ps.log_s_nodes); _rng("exp", sfh)
    sfac = exp_dd(sfh, sfl); cutoff["count_sfac"] += int((sfh < thr).sum()); cutoff["boundary_ambiguous"]["sfac"] += _amb(sfh, sfl, None, "sfac")
    sfac = _cut(sfac[0], sfac[1], sfh, "sfac")
    bn_h, bn_l = dd_mul_f(bh.expand_as(ps.log1p_nodes), bl.expand_as(ps.log1p_nodes), ps.log1p_nodes)
    pmf = ps.pm.to(DT)
    ah, al = dd_mul_f(bn_h[:, None].expand(-1, pmf.numel()), bn_l[:, None].expand(-1, pmf.numel()), pmf[None, :]); _rng("trig", ah)
    (sinb_h, sinb_l), (cosb_h, cosb_l) = sincos(ah, al)
    cutoff["count_other"] = cutoff["count_wr"] + cutoff["count_mom1"] + cutoff["count_sfac"]      # kept for the readers of the earlier records: the sum of the non-kernel factor counts
    cutoff["removed_terms_in_this_build"] = (dict(k1=cutoff["count_k1"], k2=cutoff["count_k2"], wr=cutoff["count_wr"], mom1=cutoff["count_mom1"], sfac=cutoff["count_sfac"]) if cutoff_zero else None)
    cutoff["boundary_ambiguous_total"] = sum(cutoff["boundary_ambiguous"].values()); cutoff["boundary_within_1e_12_total"] = sum(cutoff["boundary_within_1e_12"].values())
    return dict(Qc=Qc, Qs=Qs, wr=wr, mom1_0=mom1_0, mom1_c=mom1_c, mom1_s=mom1_s, sfac=sfac, beta_nodes=(bn_h, bn_l), cosb=(cosb_h, cosb_l), sinb=(sinb_h, sinb_l),
                c_l=float(c_l), omega=float(omega), p0=(p0h, p0l), arg_range=json.loads(json.dumps(ARG_RANGE)), exp_cutoff=cutoff, cutoff_zero=bool(cutoff_zero),
                trig_source=("dd_elementary.sincos_dd" if trig is None else "supplied (qualification)"))


def solve_dd_pairs_tables(ps, fh, fl, T):
    """_solve_dd_core with (hi, lo) tables T (from build_tables_dd) and pair outputs: analysis, twisted frame, factored scaling, Green sums,
    synthesis of P and grad P, every table product in double-double. Returns (P pair, gradP pair (3, Ne, Na) as (hi, lo), Plm pair, dPlm pair)."""
    fh, fl = matmul_dd_x(fh[: ps.Nr_src], fl[: ps.Nr_src], ps.A0pw)
    (cbh, cbl), (sbh, sbl) = T["cosb"], T["sinb"]
    ah, al = dd_mul_dd(fh, fl, cbh, cbl)
    bh, bl = dd_mul_dd(fh[:, ps.partner], fl[:, ps.partner], -ps.sign[None, :] * sbh, -ps.sign[None, :] * sbl)
    th, tl = dd_add(ah, al, bh, bl)
    sfh, sfl = T["sfac"]
    th, tl = dd_mul_dd(th, tl, sfh[:, None].expand_as(th), sfl[:, None].expand_as(th)); th, tl = dd_mul_f(th, tl, ps.lfac)
    ph, pl_ = th[:, ps.partner], tl[:, ps.partner]
    Qch, Qcl = T["Qc"][0][ps.pl_long, ps.pm], T["Qc"][1][ps.pl_long, ps.pm]; Qsh, Qsl = T["Qs"][0][ps.pl_long, ps.pm], T["Qs"][1][ps.pl_long, ps.pm]   # (Nqp, 2, Ne, Nr)
    def green(Qh, Ql, h, l):
        H, L = matmul_x_dd(Qh, h.T[:, :, None], l.T[:, :, None])
        cross = torch.matmul(Ql, (h + l).T[:, :, None])
        H, L = dd_add(H, L, cross, torch.zeros_like(cross))
        return H[:, :, 0].T, L[:, :, 0].T
    def term(idx):
        h1, l1 = green(Qch[:, idx], Qcl[:, idx], th, tl); h2, l2 = green(Qsh[:, idx], Qsl[:, idx], ph, pl_)
        h2, l2 = dd_mul_f(h2, l2, ps.sign[None, :])
        return dd_add(h1, l1, h2, l2)
    t1h, t1l = term(0); t2h, t2l = term(1)
    Ph_lm, Pl_lm = dd_add(t1h, t1l, t2h, t2l)
    r = ps.eval_model.r[:, None]; pl = ps.pl[None, :]
    ah, al = dd_mul_f(t1h, t1l, -(pl + 1)); bh, bl = dd_mul_f(t2h, t2l, pl)
    dh, dl = dd_add(ah, al, bh, bl); dh, dl = dd_div_f(dh, dl, r)
    Ph, Pl = matmul_dd_x(Ph_lm, Pl_lm, ps.A0p.T)
    ch, cl = dd_div_f(Ph_lm, Pl_lm, r)
    eh, el = dd_mul_f(ch, cl, -pl); eh, el = dd_add(dh, dl, eh, el)
    rh, rl = matmul_dd_x(eh, el, ps.A0p.T)
    n = ps.eval_model.grid.n.T
    comps_h, comps_l = [], []
    for i in range(3):
        gh, gl = matmul_dd_x(ch, cl, ps.A1p[i].T)
        sh, sl = dd_mul_f(rh, rl, n[i][None, :])
        gh, gl = dd_add(gh, gl, sh, sl)
        comps_h.append(gh); comps_l.append(gl)
    return (Ph, Pl), (torch.stack(comps_h, 0), torch.stack(comps_l, 0)), (Ph_lm, Pl_lm), (dh, dl)


if __name__ == "__main__":
    # unit test on one case: dd tables against float64 build_tables (hi parts agree to float64 rounding), pair solve against solve_dd_pairs with the float64 tables
    from validation.gates import Case, PAIRS, ROOT
    from validation import dd_chain as DC
    import time
    cname = sys.argv[1] if len(sys.argv) > 1 else "S01_shift_a"; dev = sys.argv[2] if len(sys.argv) > 2 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]), "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"])}
    t0 = time.time(); case = Case(cname, dev, **CASE_TABLE[cname]); ps = case.prob.pressure
    T64 = ps.build_tables(torch.tensor(case.pair[0], dtype=DT, device=dev), torch.tensor(case.pair[1], dtype=DT, device=dev))
    t1 = time.time(); Tdd = build_tables_dd(ps, case.pair[0], case.pair[1]); t_dd = time.time() - t1
    rep = dict(case=cname, pair=case.pair, seconds_dd=t_dd, arg_range=Tdd["arg_range"], tables={})
    for k in ("Qc", "Qs", "wr", "mom1_0", "mom1_c", "mom1_s", "sfac", "cosb", "sinb"):
        h, l = Tdd[k]; d = (T64[k] - h).abs(); sc = T64[k].abs().max()
        rep["tables"][k] = dict(max_abs_dev_hi=float(d.max()), table_scale=float(sc), rel_to_scale=float(d.max() / sc) if sc > 0 else None, max_lo_over_hi=float((l.abs() / (h.abs() + 1e-300)).max()))
        print(f"{k:8s} float64 vs dd(hi): max |dev| {float(d.max()):.3e} (table scale {float(sc):.3e}, rel {float(d.max() / sc) if sc > 0 else float('nan'):.2e}); max |lo/hi| {rep['tables'][k]['max_lo_over_hi']:.2e}")
    # pair solve with dd tables vs the production dd chain with float64 tables on the double-double source at the base point
    from src.equations.fields_dd import source_dd
    with torch.no_grad():
        fh, fl = source_dd(case.model, case.to_full_phys(case.z_phys))
        (P1, _), (g1, g1l), _, _ = solve_dd_pairs_tables(ps, fh, fl, Tdd)
        (P0h, P0l), (g0h, g0l), _, _ = DC.solve_dd_pairs(ps, fh, fl, T64["Qc"], T64["Qs"], T64["sfac"], T64["cosb"], T64["sinb"])
    rep["gradP_dd_tables_vs_float64_tables_rel"] = float(((g1 + g1l) - (g0h + g0l)).norm() / (g0h + g0l).norm())
    print("gradP with dd tables vs production dd chain with float64 tables: rel diff", rep["gradP_dd_tables_vs_float64_tables_rel"], f"; dd tables built in {t_dd:.1f} s")
    rep["seconds"] = time.time() - t0
    json.dump(rep, open(os.path.join(ROOT, "validation", f"dd_pressure_test_{cname}.json"), "w"), indent=1)
    print("DONE", f"{time.time() - t0:.0f}s")
