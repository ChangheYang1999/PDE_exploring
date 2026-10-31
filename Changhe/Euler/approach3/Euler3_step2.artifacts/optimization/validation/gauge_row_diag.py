#!/usr/bin/env python
"""SPEC v1.22 3.6 (n) (4) diagnostic (lead 14:44:24Z item 2 (c), 14:54:54Z item 1 (d)): the gauge row g = w (sqrt(N) - 1), N = Problem.tail_norm2 (the analytic
modal energy N = sum_q [ l(l+1) t_q^2 + (l^2 (l+1)^2 + l(l+1)((2 - alpha)^2 + (m omega / c_l)^2)) s_q^2 ], t_q = R0^(alpha + l) sum_k A[k, q],
s_q = R0^(alpha + l - 1) sum_k C[k, q]), at the manu_a base point, for the reduced optimizer coefficient columns 189 and 186. Records:
 (1) the production gauge-row entries of J_f (frozen weights), J_cw (weights differentiated) and J_c (= J_cw at the gauge row: the closure correction touches
     the closure rows only) by forward-mode jvp along e_j, and the production float64 values N and g with their ulps (g compared bitwise with the residual's row);
 (2) an independent value of the same derivative: the closed form dg/dq_j = w (dN/dq_j) / (2 sqrt N) with dN/dq_j = sum_q [2 wT_q t_q dt_q + 2 wS_q s_q ds_q],
     evaluated in mpmath at 50 digits from (a) the production float64 inputs: A, C (hex-exact), the exact tangents dA, dC of the LINEAR map q -> (A, C)
     (jvp of tc.expand o pm.expand along e_j), and the production float64 constants R0^(alpha+l), R0^(alpha+l-1), wT, wS held exactly ('same-function'
     constants, v1.22 (5) (i)); (b) the same with every constant recomputed exactly in mpmath from the hex-exact c_l, omega, R0 ('exact modal');
     and the difference identity (N(q + h e) - N(q - h e)) in mpmath from the float64 arrays at q +- h e (h = 1e-3 s_j, 1e-4 s_j);
 (3) the spread of g over summation orders (production GPU torch sum, CPU torch, sequential forward, sequential reverse, ascending and descending by
     magnitude, numpy pairwise, math.fsum of the float64 terms) at the base and at q +- 1e-3 s_j e_j, and the spread of the resulting centered differences.
Saved inputs (verifier V341): mode lists l, m; A, C; dA, dC per column; hex of c_l, omega, R0, alpha, w; z_opt; s_j; gauge-row index; A, C at the stencil points.
v2 (15:3xZ, V355): the summation-order terms are the production float64 terms from prob.mode_tail_energies (v1 recomputed them as t**2 * wT, a different multiplication order; v1 record kept as gauge_row_diag_manu_a.json). The closed form takes dA, dC from the production jvp of the coordinate map: it checks the modal differentiation, not the map (the verifier's rational map check is separate). Diagnostic only: no gate, threshold, floor, ladder or pass rule changes. Usage: python validation/gauge_row_diag.py [device] [columns, default 189,186]"""
import sys, os, json, time, math, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np, torch, mpmath as mp
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT, code_hashes
from src.equations.fields import alpha_of

DPS = 50


def ulp(x):
    return math.ulp(float(x))


def hexs(x):
    return float(x).hex()


def main():
    dev = sys.argv[1] if len(sys.argv) > 1 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    cols = [int(c) for c in (sys.argv[2] if len(sys.argv) > 2 else "189,186").split(",")]
    out_json = os.path.join(ROOT, "validation", "gauge_row_diag_manu_a_v2.json"); out_npz = out_json.replace(".json", "_arrays.npz")
    for p in (out_json, out_npz):
        if os.path.exists(p):
            raise FileExistsError(p)
    t0 = time.time()
    case = Case("manu_a", dev, pair=PAIRS["a"], seed=3); prob, model = case.prob, case.model
    zo = case.z_opt.detach().clone(); n = zo.numel(); to_full = case.to_full_opt
    gr = case.block_slices["gauge"][0]; w = float(prob.gauge_weight)
    zf = to_full(zo).detach()
    A, C, cc, ww = model.unpack(zf); A = A.detach(); C = C.detach(); c_l = float(cc); omega = float(ww)
    R0 = float(model.R0); a_prod = float(alpha_of(torch.tensor(c_l, dtype=torch.float64)))      # the production float64 alpha
    l = model.l_arr.to(torch.float64); m = model.m_arr.to(torch.float64)
    # production pieces (same expressions as Problem.tail_amplitudes / mode_tail_energies, on the device)
    a_t = torch.tensor(a_prod, dtype=torch.float64, device=l.device)
    powT = R0 ** (a_t + l); powS = R0 ** (a_t + l - 1)                                           # float64 constants (do not depend on the perturbed coefficient)
    wT = l * (l + 1); wS = (l ** 2 * (l + 1) ** 2 + l * (l + 1) * ((2 - a_t) ** 2 + (m * omega / c_l) ** 2))
    N_prod = float(prob.tail_norm2(A, C, cc, ww)); g_prod = w * (math.sqrt(max(N_prod, 1e-300)) - 1.0)
    r_base = case.r; g_row = float(r_base[gr])
    rec = dict(case="manu_a", pair=case.pair, cost=case.cost, device=str(dev), n_opt=int(n), gauge_row=int(gr), gauge_weight=w, gauge_form="w (sqrt(N) - 1), N = Problem.tail_norm2 (norm form; clamp_min(1e-300) before sqrt)",
               constants_hex=dict(c_l=hexs(c_l), omega=hexs(omega), R0=hexs(R0), alpha_production_float64=hexs(a_prod), w=hexs(w)),
               mode_lists=dict(l=[int(x) for x in model.l_arr.tolist()], m=[int(x) for x in model.m_arr.tolist()], Nq=int(model.Nq), Nk=int(model.Nk)),
               production=dict(N=N_prod, N_hex=hexs(N_prod), ulp_N=ulp(N_prod), g=g_prod, g_hex=hexs(g_prod), ulp_g=ulp(g_prod), residual_gauge_row=g_row, residual_gauge_row_hex=hexs(g_row), g_equals_residual_row_bitwise=(g_row == g_prod)),
               columns={})
    arrays = dict(z_opt=zo.cpu().numpy(), A=A.cpu().numpy(), C=C.cpu().numpy(), l=model.l_arr.cpu().numpy(), m=model.m_arr.cpu().numpy(), powT=powT.detach().cpu().numpy(), powS=powS.detach().cpu().numpy(), wT=wT.detach().cpu().numpy(), wS=wS.detach().cpu().numpy())
    # ---- mpmath helpers
    mp.mp.dps = DPS
    def mpf_list(t):
        t = t.detach().cpu().numpy() if torch.is_tensor(t) else t
        return [mp.mpf(float(x)) for x in np.asarray(t, dtype=np.float64).reshape(-1).tolist()]
    def N_mp(Aa, Cc, pT, pS, wTT, wSS):
        """N from float64 arrays and the given (mp) constants: t_q = pT_q sum_k A, s_q = pS_q sum_k C."""
        Nq = Aa.shape[1]; tot = mp.mpf(0); ts = []; ss = []
        for q in range(Nq):
            tq = pT[q] * mp.fsum(mp.mpf(float(x)) for x in Aa[:, q].tolist()); sq = pS[q] * mp.fsum(mp.mpf(float(x)) for x in Cc[:, q].tolist())
            ts.append(tq); ss.append(sq); tot += wTT[q] * tq * tq + wSS[q] * sq * sq
        return tot, ts, ss
    An = A.cpu().numpy(); Cn = C.cpu().numpy()
    # constants (a) production float64 held exactly; (b) exact mpmath from the hex-exact c_l, omega, R0
    pT_a = mpf_list(powT); pS_a = mpf_list(powS); wT_a = mpf_list(wT); wS_a = mpf_list(wS)
    cl_m = mp.mpf(c_l); om_m = mp.mpf(omega); R0_m = mp.mpf(R0); a_m = (1 - cl_m) / cl_m
    lq = [int(x) for x in model.l_arr.tolist()]; mq = [int(x) for x in model.m_arr.tolist()]
    pT_b = [R0_m ** (a_m + lq[q]) for q in range(len(lq))]; pS_b = [R0_m ** (a_m + lq[q] - 1) for q in range(len(lq))]
    wT_b = [mp.mpf(lq[q] * (lq[q] + 1)) for q in range(len(lq))]; wS_b = [mp.mpf(lq[q]) ** 2 * (lq[q] + 1) ** 2 + lq[q] * (lq[q] + 1) * ((2 - a_m) ** 2 + (mq[q] * om_m / cl_m) ** 2) for q in range(len(lq))]
    N_a, t_a, s_a = N_mp(An, Cn, pT_a, pS_a, wT_a, wS_a); N_b, t_b, s_b = N_mp(An, Cn, pT_b, pS_b, wT_b, wS_b)
    rec["independent"] = dict(digits=DPS, N_same_function_constants=mp.nstr(N_a, 30), N_exact_modal=mp.nstr(N_b, 30), g_same_function_constants=mp.nstr(w * (mp.sqrt(N_a) - 1), 30), g_exact_modal=mp.nstr(w * (mp.sqrt(N_b) - 1), 30),
                              N_production_minus_same_function=float(mp.mpf(N_prod) - N_a), g_production_minus_same_function=float(mp.mpf(g_prod) - w * (mp.sqrt(N_a) - 1)),
                              note="(a) 'same-function constants': R0 powers and mode weights are the production float64 values held exactly (v1.22 (5) (i)); (b) 'exact modal': every constant recomputed in mpmath from the hex-exact c_l, omega, R0; both from the hex-exact float64 arrays A, C")
    # ---- production residual functions for the jvp
    fun_f = lambda q: prob.residual_vector(to_full(q))
    def fun_wd(q):
        zz_ = to_full(q); tabs = prob.pressure_tables_at(zz_, differentiable=True); ev = prob.evaluate(zz_, tables=tabs)
        return prob.residual_vector(zz_, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
    def AC_of(q):
        zz_ = to_full(q); aT, aS, _, _ = model.unpack(zz_); return aT, aS
    # summation orders for the spread
    def g_orders(Aa, Cc):
        """g from N = sum eT + sum eS with the float64 terms eT_q = powT^2 (sum_k A)^2 wT, eS_q likewise (as production: t**2 * l(l+1)), in several orders."""
        eT, eS = prob.mode_tail_energies(Aa, Cc, cc, ww)                                   # v2 (V355): the UNCHANGED production float64 terms (t**2 * l*(l+1) etc.), so the diagnostic is about the summation order alone
        terms_dev = torch.cat([eT.detach(), eS.detach()]); terms = terms_dev.cpu().numpy().astype(np.float64)
        res = {}
        res["production_device"] = float(eT.sum() + eS.sum())
        res["torch_cpu"] = float(torch.as_tensor(terms).sum())
        acc = 0.0
        for x in terms.tolist(): acc += x
        res["sequential_forward"] = acc
        acc = 0.0
        for x in terms[::-1].tolist(): acc += x
        res["sequential_reverse"] = acc
        srt = np.sort(np.abs(terms)); sgn = terms[np.argsort(np.abs(terms))]
        acc = 0.0
        for x in sgn.tolist(): acc += x
        res["ascending_magnitude"] = acc
        acc = 0.0
        for x in sgn[::-1].tolist(): acc += x
        res["descending_magnitude"] = acc
        res["numpy_pairwise"] = float(np.sum(terms))
        res["fsum_exact_of_float64_terms"] = math.fsum(terms.tolist())
        gs = {k: w * (math.sqrt(max(v, 1e-300)) - 1.0) for k, v in res.items()}
        return dict(N=res, g=gs, g_spread=max(gs.values()) - min(gs.values()), N_spread=max(res.values()) - min(res.values()), n_terms=int(terms.size))
    rec["spread_base"] = g_orders(A, C)
    for j in cols:
        e = torch.zeros_like(zo); e[j] = 1.0
        sj = 1.0                                                                                   # the registered step scale of columns 186 and 189 (add-on record step_scale 1.0)
        col = dict(column=j, step_scale=sj)
        # (1) production entries
        Jf_col = torch.func.jvp(fun_f, (zo,), (e,))[1].detach(); Jcw_col = torch.func.jvp(fun_wd, (zo,), (e,))[1].detach()
        col["production_entries"] = dict(Jf=float(Jf_col[gr]), Jcw=float(Jcw_col[gr]), Jc="equal to Jcw at the gauge row (the closure correction of J_c replaces the closure rows only)",
                                        Jf_hex=hexs(Jf_col[gr]), Jcw_hex=hexs(Jcw_col[gr]), Jf_equals_Jcw_bitwise=bool(float(Jf_col[gr]) == float(Jcw_col[gr])),
                                        column_norm_Jf=float(Jf_col.norm()), column_norm_Jcw=float(Jcw_col.norm()), gauge_row_share_of_column_Jcw=float(abs(Jcw_col[gr]) / max(float(Jcw_col.norm()), 1e-300)))
        # (2) independent closed form
        (dA, dC) = torch.func.jvp(AC_of, (zo,), (e,))[1]; dA = dA.detach(); dC = dC.detach(); dAn = dA.cpu().numpy(); dCn = dC.cpu().numpy()
        arrays[f"dA_{j}"] = dAn; arrays[f"dC_{j}"] = dCn
        def dg_closed(ts, ss, pT, pS, wTT, wSS, Nv):
            dN = mp.mpf(0)
            for q in range(len(ts)):
                dt = pT[q] * mp.fsum(mp.mpf(float(x)) for x in dAn[:, q].tolist()); ds = pS[q] * mp.fsum(mp.mpf(float(x)) for x in dCn[:, q].tolist())
                dN += 2 * wTT[q] * ts[q] * dt + 2 * wSS[q] * ss[q] * ds
            return w * dN / (2 * mp.sqrt(Nv)), dN
        dg_a, dN_a = dg_closed(t_a, s_a, pT_a, pS_a, wT_a, wS_a, N_a); dg_b, dN_b = dg_closed(t_b, s_b, pT_b, pS_b, wT_b, wS_b, N_b)
        prod = mp.mpf(float(Jcw_col[gr]))
        col["independent_closed_form"] = dict(same_function_constants=mp.nstr(dg_a, 25), exact_modal=mp.nstr(dg_b, 25), dN_same_function=mp.nstr(dN_a, 25), dN_exact_modal=mp.nstr(dN_b, 25),
                                              rel_diff_production_vs_same_function=float((prod - dg_a) / dg_a) if dg_a != 0 else None, rel_diff_production_vs_exact_modal=float((prod - dg_b) / dg_b) if dg_b != 0 else None,
                                              rel_diff_same_function_vs_exact_modal=float((dg_a - dg_b) / dg_b) if dg_b != 0 else None,
                                              threshold_finding="a disagreement above 1e-6 of the entry is a finding against the derivative (lead 14:44:24Z item 5 (c))",
                                              nonzero_tangent_entries=dict(dA=int(np.count_nonzero(dAn)), dC=int(np.count_nonzero(dCn))), tangent_map="jvp of q -> (A, C) = model.unpack(tc.expand(pm.expand(q))) along e_j (linear in the coefficients: exact up to the rounding of the map's arithmetic)")
        # (2b) difference identity from float64 arrays at q +- h e (mpmath N of the float64 inputs)
        ident = {}
        for h in (1e-3 * sj, 1e-4 * sj):
            Ap, Cp = AC_of(zo + h * e); Am, Cm = AC_of(zo - h * e)
            Np, _, _ = N_mp(Ap.detach().cpu().numpy(), Cp.detach().cpu().numpy(), pT_a, pS_a, wT_a, wS_a); Nm, _, _ = N_mp(Am.detach().cpu().numpy(), Cm.detach().cpu().numpy(), pT_a, pS_a, wT_a, wS_a)
            Dg = w * (mp.sqrt(Np) - mp.sqrt(Nm)) / (2 * h); DN = (Np - Nm) / (2 * h)
            ident[f"{h:.0e}"] = dict(D_g=mp.nstr(Dg, 25), D_N=mp.nstr(DN, 25), rel_diff_D_g_vs_closed_form=float((Dg - dg_a) / dg_a) if dg_a != 0 else None, rel_diff_D_g_vs_production=float((Dg - prod) / prod) if prod != 0 else None)
            arrays[f"A_plus_{j}_{h:.0e}"] = Ap.detach().cpu().numpy(); arrays[f"A_minus_{j}_{h:.0e}"] = Am.detach().cpu().numpy(); arrays[f"C_plus_{j}_{h:.0e}"] = Cp.detach().cpu().numpy(); arrays[f"C_minus_{j}_{h:.0e}"] = Cm.detach().cpu().numpy()
        col["difference_identity_mpmath_from_float64_arrays"] = ident
        # (3) spread over summation orders at q +- 1e-3 s_j e and the resulting centered differences
        sp = {}
        for h in (1e-3 * sj, 1e-2 * sj):
            Ap, Cp = AC_of(zo + h * e); Am, Cm = AC_of(zo - h * e)
            gp = g_orders(Ap.detach(), Cp.detach()); gm = g_orders(Am.detach(), Cm.detach())
            D = {k: (gp["g"][k] - gm["g"][k]) / (2 * h) for k in gp["g"]}
            sp[f"{h:.0e}"] = dict(plus=gp, minus=gm, centered_difference_by_order=D, D_spread=max(D.values()) - min(D.values()),
                                   D_rel_err_vs_production_by_order={k: (v - float(Jcw_col[gr])) / float(Jcw_col[gr]) for k, v in D.items()},
                                   g_production_plus=float(prob.residual_vector(to_full(zo + h * e))[gr]), g_production_minus=float(prob.residual_vector(to_full(zo - h * e))[gr]))
            sp[f"{h:.0e}"]["D_production_rows"] = (sp[f"{h:.0e}"]["g_production_plus"] - sp[f"{h:.0e}"]["g_production_minus"]) / (2 * h)
            sp[f"{h:.0e}"]["D_production_rows_rel_err"] = (sp[f"{h:.0e}"]["D_production_rows"] - float(Jcw_col[gr])) / float(Jcw_col[gr])
        col["spread_over_summation_orders"] = sp
        rec["columns"][str(j)] = col
        print(f"column {j}: Jcw gauge entry {float(Jcw_col[gr]):.17e} | closed form (same-function constants) {mp.nstr(dg_a, 20)} rel {col['independent_closed_form']['rel_diff_production_vs_same_function']:.3e} | exact modal {mp.nstr(dg_b, 20)} rel {col['independent_closed_form']['rel_diff_production_vs_exact_modal']:.3e} | identity 1e-3: {ident['1e-03']['rel_diff_D_g_vs_production']:.3e} | g spread base {rec['spread_base']['g_spread']:.3e}, D spread 1e-3: {sp['1e-03']['D_spread']:.3e}, production-rows D rel err 1e-3: {sp['1e-03']['D_production_rows_rel_err']:.3e}", flush=True)
    np.savez_compressed(out_npz, **arrays)
    rec["arrays_npz"] = dict(path=os.path.relpath(out_npz, ROOT), sha256=hashlib.sha256(open(out_npz, "rb").read()).hexdigest(), keys=sorted(arrays))
    rec["code_sha256"] = code_hashes(); rec["launcher_manifest"] = (open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None)
    rec["seconds"] = time.time() - t0; rec["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print("DONE", out_json, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
