#!/usr/bin/env python
"""D6FP G3 add-on (lead note 2026-10-28T22:17Z item 2; SPEC v1.5 3.0 (b')(2) seven-step ladder, v1.7 3.0 (b')(3) gauge-subtracted estimator).
For every G3 direction of validation/gates.py (same cases, seed 11 and direction construction) evaluate the self-consistent residual at
X +- h v, X +- 2h v for h in 1e-3 ... 1e-9, record O1 and the gauge row g (last row) at each stencil point, and report four outcomes per
direction: O1 on the v1.4 ladder (1e-3..1e-7), O1 on the seven-step ladder, O~(t) = O1 - (g(t) - g(0))^2 / 2 on both ladders, each with the
errors of both stencils against the complete gradient d = g_c . v, the Richardson pair, the floor F = 1e-3 ||r|| ||J_c v||, the absolute-only
flag, the base-point active set, g(0) and |g(0)| / max(|d|, F). J_c v: forward-mode jvp of the weights-differentiated residual along v with
the closure block replaced by the five-point difference (h 1e-4) of the fresh closure rows along v (closure target and patterns refreshed).
Writes validation/g3_addon_<tag>.json."""
import sys, os, time, json, math, argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT, code_hashes
from src.optimization.lm import jacobian_fwd, param_columns
HS7 = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9]; HS5 = HS7[:5]


def pass_rule(errs, errs4, hs, valid, tau=1e-6):
    """two consecutive VALID steps (SPEC 3.0 (e): a step is valid when all four stencil points share the base active set) within tau, for each stencil."""
    hs = sorted(hs, reverse=True)
    pairs = [(hs[i], hs[i + 1]) for i in range(len(hs) - 1) if valid[hs[i]] and valid[hs[i + 1]]]
    ok2 = any(errs[a] <= tau and errs[b] <= tau for a, b in pairs)
    ok4 = any(errs4[a] <= tau and errs4[b] <= tau for a, b in pairs)
    return ok2, ok4, pairs


def ladder_report(vals, g0_vals, dpred, Fl, hs, subtract_gauge, valid):
    """vals[t] = O1(X + t v), g0_vals[t] = gauge row at t, valid[h] = all four stencil points of step h share the base active set.
    Returns errors of both stencils, Richardson (the best over all passing pairs of consecutive valid steps; v2), pass flags, absolute-only flag, OPEN flag."""
    def O(t):
        o = vals[t]
        if subtract_gauge:
            o = o - 0.5 * (g0_vals[t] - g0_vals[0.0]) ** 2
        return o
    D2 = {}; D4s = {}
    for h in hs:
        D2[h] = (O(h) - O(-h)) / (2 * h); D4s[h] = (8 * (O(h) - O(-h)) - (O(2 * h) - O(-2 * h))) / (12 * h)
    def decide(F):
        errs = {h: abs(D2[h] - dpred) / max(abs(dpred), abs(D2[h]), F) for h in hs}; errs4 = {h: abs(D4s[h] - dpred) / max(abs(dpred), abs(D4s[h]), F) for h in hs}
        ok2, ok4, pairs = pass_rule(errs, errs4, hs, valid)
        rich = None; pair = None
        for a, b in pairs:                                                   # v2 (V187, SPEC 3.0 (d)): every adjacent passing valid pair is inspected; the smallest Richardson error counts
            if errs[a] <= 1e-6 and errs[b] <= 1e-6:
                R = D2[b] + (D2[b] - D2[a]) / 99.0; r_ = abs(R - dpred) / max(abs(dpred), abs(R), F)
                if rich is None or r_ < rich:
                    rich = r_; pair = (a, b)
        open_ = len(pairs) == 0
        return errs, errs4, ok2, ok4, pairs, rich, pair, open_, bool((not open_) and ok2 and ok4 and rich is not None and rich <= 1e-6)
    errs, errs4, ok2, ok4, pairs, rich, pair, open_, PASS = decide(Fl)                     # the registered decision (with the floor)
    errs0, errs40, ok2_0, ok4_0, _, rich0, pair0, _, PASS_rel = decide(0.0)                 # F = 0 (SPEC 3.0 (c), lead 23:24Z item 3)
    return dict(errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, fd_values={f"{h:.0e}": D2[h] for h in hs},
                fd_values_five_point={f"{h:.0e}": D4s[h] for h in hs}, errors_second_order_F0={f"{h:.0e}": errs0[h] for h in hs}, errors_five_point_F0={f"{h:.0e}": errs40[h] for h in hs},
                step_valid={f"{h:.0e}": bool(valid[h]) for h in hs}, n_consecutive_valid_pairs=len(pairs), OPEN=bool(open_),
                pass_second_order=ok2, pass_five_point=ok4, richardson_error=rich, richardson_pair=pair,
                pass_second_order_F0=ok2_0, pass_five_point_F0=ok4_0, richardson_error_F0=rich0, richardson_pair_F0=pair0,
                PASS=bool(PASS), PASS_rel=bool(PASS_rel), absolute_only=bool(PASS and not PASS_rel))


def run(case, out_path, quick=False):
    prob, model, pm = case.prob, case.model, case.pm
    dev = case.device; zo, zp = case.z_opt, case.z_phys; n = zo.numel()
    rng = np.random.default_rng(11)
    cols = sorted(rng.choice(n - 2, size=min(20, n - 2), replace=False).tolist())      # consumed first in gates.run_case (same seed order)
    fun = lambda q: prob.residual_vector(case.to_full_opt(q))
    J = jacobian_fwd(fun, zo, chunk=256)
    Jp = param_columns(lambda q: prob.residual_vector(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
    J[:, n - 2] = Jp[:, 0]; J[:, n - 1] = Jp[:, 1]
    colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt(); del J
    # complete gradient in optimizer coordinates (as gates.py)
    zz = zo.detach().clone().requires_grad_(True)
    rr = prob.objective_graph(case.to_full_opt(zz)); c = 0.5 * (rr @ rr); g_c, = torch.autograd.grad(c, zz); g_c = g_c.detach().clone()
    _, parts = prob.complete_gradient(case.to_full_opt(zo).detach(), return_parts=True)
    dsc = pm.describe(zo)
    if parts["pattern_fd"] is not None:
        g_c[-2] += float(parts["pattern_fd"][0]) * dsc["dcl_dzc"]; g_c[-1] += float(parts["pattern_fd"][1]) * dsc["domega_dzw"]
    E = {}
    e = torch.zeros_like(zo); e[n - 2] = 1.0; E["e_zc(optimizer)"] = e
    e = torch.zeros_like(zo); e[n - 1] = 1.0; E["e_zw(optimizer)"] = e
    for i in range(3):
        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm
    for i in range(2):
        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm
    blocks = case.block_slices
    def Jc_v(v, to_full, zbase):
        """J_c v: jvp of the weights-differentiated residual (tables in the graph) along v, closure block by five-point differences of the fresh closure rows."""
        def fun_wd(q):
            zz_ = to_full(q); tabs = prob.pressure_tables_at(zz_, differentiable=True); ev = prob.evaluate(zz_, tables=tabs)
            return prob.residual_vector(zz_, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
        col = torch.func.jvp(fun_wd, (zbase,), (v,))[1].clone()
        if "closure" in blocks:
            a0, a1 = blocks["closure"]; h = 1e-4 / max(float(v.norm()), 1e-300) * 1e-0
            crow = lambda q: prob.closure_rows(to_full(q), closure=prob.closure_state_at(to_full(q)))
            col[a0:a1] = (8 * (crow(zbase + h * v) - crow(zbase - h * v)) - (crow(zbase + 2 * h * v) - crow(zbase - 2 * h * v))) / (12 * h)
        return col
    gauge_row = blocks["gauge"][0]
    def O1_and_g(q, to_full):
        r, _ = prob.objective_at(to_full(q), need_aux=False); return 0.5 * float(r @ r), float(r[gauge_row])
    def act(q, to_full):
        zz_ = to_full(q); ev = prob.evaluate(zz_, tables=prob.pressure_tables_at(zz_)); a = prob.nl_active_set(ev); a["geometry"] = prob.pressure.geometry_id; return a
    from src.equations import residuals as res_mod
    res = dict(case=case.name, pair=case.pair, cost=case.cost, n_opt=int(n), directions={}, exterior_monopole=bool(prob.exterior_monopole), stable_linear=bool(prob.stable_linear),
               discrete_moments=prob.pressure.discrete_moments(res_mod.pressure_source(model.fields_grid(case.z_full, need_vort=False)["GU"]), lmax=1))
    hs = HS7 if not quick else HS7[:5]
    def one_direction(dname, v, to_full, zbase, dpred, chain_note):
        t0 = time.time()
        jcv = Jc_v(v, to_full, zbase); Fl = 1e-3 * float(case.r.norm()) * float(jcv.norm())
        vals = {}; gs = {}; acts = {}
        vals[0.0], gs[0.0] = O1_and_g(zbase, to_full); base_act = act(zbase, to_full); base_key = json.dumps(base_act, sort_keys=True)
        valid = {}; acts_all = {}
        for h in hs:                                                                       # active set recorded at ALL four stencil points of EVERY step (SPEC 3.0 (e))
            ok = True; acts_all[f"{h:.0e}"] = {}
            for t in (h, -h, 2 * h, -2 * h):
                vals[t], gs[t] = O1_and_g(zbase + t * v, to_full)
                a_ = act(zbase + t * v, to_full); acts_all[f"{h:.0e}"][f"{t:+.1e}"] = a_
                ok = ok and (json.dumps(a_, sort_keys=True) == base_key)
            valid[h] = ok
        outc = {}
        for lad_name, lad in (("v1.4_ladder", HS5), ("seven_step_ladder", hs)):
            for est_name, sub in (("O1", False), ("O_tilde_gauge_subtracted", True)):
                outc[f"{est_name}:{lad_name}"] = ladder_report(vals, gs, dpred, Fl, lad, sub, valid)
        g0 = gs[0.0]
        return dict(derivative_complete=dpred, floor=Fl, Jc_v_norm=float(jcv.norm()), Jc_v_method="jvp of the weights-differentiated residual with tables in the graph; closure block by five-point FD of the fresh closure rows along v",
                    g0=g0, g0_ratio=abs(g0) / max(abs(dpred), Fl), base_active_set=base_act, step_valid={f"{h:.0e}": bool(valid[h]) for h in hs}, active_sets_all_stencil_points=acts_all,
                    n_valid_steps=sum(1 for h in hs if valid[h]), chain_note=chain_note, outcomes=outc, seconds=time.time() - t0)
    for dname, v in E.items():
        dpred = float(g_c @ v)
        res["directions"][dname] = one_direction(dname, v, case.to_full_opt, zo, dpred, "optimizer coordinates")
        print(f"  {case.name} {dname}: valid steps {res['directions'][dname]['step_valid']}; " + json.dumps({k: (("OPEN" if o["OPEN"] else o["PASS"]), f"{min(o['errors_second_order'].values()):.1e}", o["richardson_error"]) for k, o in res["directions"][dname]["outcomes"].items()}), flush=True)
        json.dump(res, open(out_path, "w"), indent=1, default=str)
    # physical c_l and omega at fixed reduced coordinates
    for j, pname in enumerate(("c_l", "omega")):
        v = torch.zeros_like(zp); v[n - 2 + j] = 1.0
        chain = dsc["dcl_dzc"] if j == 0 else dsc["domega_dzw"]
        dpred = float(g_c[-2 + j]) / chain
        scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
        res["directions"][f"e_{pname}(physical)"] = one_direction(f"e_{pname}(physical)", v * scale, case.to_full_phys, zp, dpred * scale, f"physical, fixed reduced a; step scaled by {scale}")
        print(f"  {case.name} e_{pname}(physical): " + json.dumps({k: (o["PASS"], f"{min(o['errors_second_order'].values()):.1e}", o["richardson_error"]) for k, o in res["directions"][f'e_{pname}(physical)']["outcomes"].items()}), flush=True)
        json.dump(res, open(out_path, "w"), indent=1, default=str)
    return res


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,S05_own,manu_small_omega,manu_large_omega"); ap.add_argument("--quick", action="store_true")
    a = ap.parse_args(); dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
    defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")), "S11_own": dict(start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")), "S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")), "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
            "S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]), "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
            "manu_a": dict(pair=PAIRS["a"], seed=3), "manu_small_omega": dict(pair=PAIRS["small_omega"], seed=5), "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6),
            "manu_near_edge": dict(pair=PAIRS["near_edge"], seed=7), "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all")}
    allres = dict(tag=a.tag, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), code_sha256=code_hashes(), ladders=dict(v14=HS5, seven=HS7), cases={})
    for cname in a.cases.split(","):
        print(f"=== G3 add-on case {cname} ===", flush=True)
        case = Case(cname, dev, **defs[cname])
        outp = os.path.join(ROOT, "validation", f"g3_addon_{a.tag}_{cname}.json")
        allres["cases"][cname] = run(case, outp, quick=a.quick)
        json.dump(allres, open(os.path.join(ROOT, "validation", f"g3_addon_{a.tag}.json"), "w"), indent=1, default=str)
        del case; torch.cuda.empty_cache()
    print("G3 ADD-ON DONE")


if __name__ == "__main__":
    main()
