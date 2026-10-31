#!/usr/bin/env python
"""SPEC v1.19 3.6 (l) evaluation (numerics 2026-10-29T10:1xZ, first version; test-only; v5 11:4xZ: the per-term weighting uses the weights of the rows, evaluated with the tables at z's own
parameters; in the S01 z_c record of 11:43Z the split's term-sum check failed (6.9e-6) because the weights were taken with the solver's base tables).
For one failing parameter column (case, Jacobian reference,
column label) it forms the finite differences D_h and D4_h of the double-double residual copy (validation/dd_chain.py) at the five registered steps,
in the registered coordinates, and judges the registered column d against them with the registered harness machinery (gates.column_test: same
groups, floors from case.r, thresholds, two-consecutive-step rule, Richardson, F = 0 variant; the ladder is replaced by the double-double ladder,
differences formed and divided in double-double and rounded once). It also recomputes the registered float64 comparison with the production
reference function for the same column (consistency with the record) and gives the per-term split of D_h - d in the far-anchor block at every step
(stable linear operator lin, convection (U . grad) U, pressure gradient; each term carried with the full row weighting so that the three parts sum to
the row). Refuses to run unless validation/l_scope.json exists (the double-double set fixed before any (l) difference, lead 09:32:45Z item 1 (a)) and
the same-function check of the reference exists and passed (dd_chain_check_<case>_<col>.json). Output: validation/l_eval_<case>_<ref>_<col>.json
(exclusive create). Usage: python validation/l_eval.py <case> <Jf|Jcw|Jc> <column label> <accepted l_scope.json sha256> [device]
V245 (lead 10:18:52Z item 2): the accepted scope sha256 is bound; a scope class assigned to double-double that this copy does not carry stops the run;
the same-function evidence must match case, coordinate, reference and the source hashes; the active-set recorder is passed to every comparison;
per-term entries are keyed by the ladder's own offsets and a missing pair stops the run; the full ladder pairs are kept and the pair sum of the terms is checked."""
import sys, os, json, time, hashlib, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation import gates as G
from validation.gates import Case, PAIRS, ROOT, column_test
from validation import dd_chain as DC
from src.optimization.lm import param_columns
from src.equations import residuals as res
from src.pressure.exact_matmul import dd_add, dd_mul_f
import src.optimization.problem as problem_mod

CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
              "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"])}
HS = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    cname, ref, col = sys.argv[1], sys.argv[2], sys.argv[3]
    scope_sha = sys.argv[4] if len(sys.argv) > 4 else None
    dev = sys.argv[5] if len(sys.argv) > 5 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    problem_mod.TABLE_CACHE = False
    scope_path = os.path.join(ROOT, "validation", "l_scope.json")
    if not os.path.exists(scope_path) or not scope_sha:
        raise SystemExit("validation/l_scope.json and the lead-accepted sha256 are required (lead 09:32:45Z item 1 (a), 10:15:00Z item 1, V245 (a))")
    if sha(scope_path) != scope_sha:
        raise SystemExit(f"l_scope.json sha256 {sha(scope_path)} differs from the accepted {scope_sha}: refused (V245 (a))")
    scope = json.load(open(scope_path))
    if not scope.get("screened_classes"):
        raise SystemExit("l_scope.json has no screened classes: refused (V245 (a))")
    dd_classes = {k for k, v in scope["screened_classes"].items() if v.get("decision") == "double-double"}
    not_carried = dd_classes - DC.CARRIED_DD
    if not_carried:
        raise SystemExit(f"scope assigns {sorted(not_carried)} to double-double, which this copy evaluates in float64: run stopped (V245 (b))")
    tag = col.replace(":", "_")
    chk_path = os.path.join(ROOT, "validation", f"dd_chain_check_{cname}_{tag}.json")
    if not os.path.exists(chk_path):
        raise SystemExit(f"{chk_path} missing: the same-function check must exist first (3.6 (l) (3))")
    chk = json.load(open(chk_path))
    if chk.get("case") != cname or chk.get("column") != col or ref not in (chk.get("references") or {}):
        raise SystemExit("same-function evidence is for another case, column or reference (V245 (c))")
    cur = DC.source_hashes(ROOT); cur_eval = sha(__file__)
    if chk.get("sources") != cur:
        diff_ = [k for k in set(cur) | set(chk.get("sources") or {}) if cur.get(k) != (chk.get("sources") or {}).get(k)]
        raise SystemExit(f"same-function evidence was produced with other sources {diff_}: rerun dd_chain first (V245 (c))")
    if not chk["references"].get(ref, {}).get("same_function_check"):
        raise SystemExit(f"same-function check for {ref} did not pass: (l) is not evaluated for this Jacobian (3.6 (l) (3), last sentence)")
    out_path = os.path.join(ROOT, "validation", f"l_eval_{cname}_{ref}_{tag}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time()
    case = Case(cname, dev, **CASE_TABLE[cname]); prob = case.prob; model = case.model
    coords, pname = col.split(":")
    zc = (case.z_opt if coords == "optimizer" else case.z_phys).detach().clone()
    to_full = case.to_full_opt if coords == "optimizer" else case.to_full_phys
    n = zc.numel(); j = {"z_c": 0, "c_l": 0, "z_w": 1, "omega": 1}[pname]
    e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
    scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
    # ---- the registered column d of this Jacobian (as the harness builds it)
    if ref == "Jf":
        pfun = lambda q: prob.residual_vector(to_full(q), differentiable_pressure=True)
        d = param_columns(pfun, zc, [n - 2 + j])[:, 0]
        ref_fun = lambda q: prob.residual_vector_rebuild(to_full(q))
    elif ref == "Jcw":
        pfun = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
        d = param_columns(pfun, zc, [n - 2 + j])[:, 0]
        ref_fun = lambda q: prob.residual_vector_rebuild_wd(to_full(q))
    else:
        def fun_wd(q):
            zz = to_full(q)
            tabs = prob.pressure_tables_at(zz, differentiable=True)
            ev = prob.evaluate(zz, tables=tabs)
            nl_w = prob.nl_weights_from_ev(ev, differentiable=True)
            return prob.residual_vector(zz, tables=tabs, nl_w=nl_w, closure=prob.closure, ev=ev)
        d = torch.func.jvp(fun_wd, (zc,), (e,))[1]
        if "closure" in case.block_slices:
            a0, a1 = case.block_slices["closure"]
            def crow(q):
                zz = to_full(q); return prob.closure_rows(zz, closure=prob.closure_state_at(zz))
            h = 1e-4
            d = d.clone(); d[a0:a1] = (8 * (crow(zc + h * e) - crow(zc - h * e)) - (crow(zc + 2 * h * e) - crow(zc - 2 * h * e))) / (12 * h)
        ref_fun = lambda q: prob.objective_at(to_full(q), need_aux=False)[0]
    d = d.detach()
    def act(zz_full):                                                        # the registered active-set recorder (gates.py; SPEC 3.0 (e), V187)
        ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
        return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
    rec_act = lambda q: act(to_full(q))
    # ---- registered comparison recomputed (float64 ladder of the production reference, with the active-set recorder)
    orig_ladder = G.stencil_ladder
    t_reg = column_test(case, f"registered {ref} {col}", d, ref_fun, zc, e, HS, ref=case.r, record_active=rec_act, scale=scale, deriv_scale=1.0)
    # ---- (l) comparison: the double-double ladder
    tcache = {}; term_store = {}; ladder_store = {}
    def fun_dd(q, t):
        zf = to_full(q)
        key = (float(zf[-2]), float(zf[-1]))
        if key not in tcache:
            tcache[key] = DC.tables_dd(model, key[0], key[1], device=zf.device); tcache[key]["P"] = DC.pressure_tables_dd(prob, key[0], key[1])
            fun_dd.ranges[f"{t:+.3e}"] = dict(arg_range=tcache[key]["P"]["arg_range"], exp_cutoff=tcache[key]["P"].get("exp_cutoff"))   # V271: per stencil point
        rh, rl, terms = DC.residual_dd(prob, zf, ref=ref, T=tcache[key], case=case, q=q, coords=coords)
        term_store[t] = (terms, zf)                                           # keyed by the ladder's own nominal offset (V245 (e))
        return rh, rl
    fun_dd.ranges = {}
    def dd_stencil_ladder(fun, z, e_, hs_, record_active=None):
        lad, active, pairs = DC.ladder_dd(fun_dd, z, e_, hs_, record_active=record_active)
        ladder_store["pairs"] = pairs; ladder_store["active"] = active
        return lad, active
    G.stencil_ladder = dd_stencil_ladder
    try:
        t_l = column_test(case, f"(l) double-double differences {ref} {col}", d, None, zc, e, HS, ref=case.r, record_active=rec_act, scale=scale, deriv_scale=1.0)
    finally:
        G.stencil_ladder = orig_ladder
    pairs = ladder_store["pairs"]
    # ---- per-term split of D_h - d in the far-anchor block (both stencils; pairs kept; term-sum check in double-double, V252 (b), (c))
    split = {}; arrays = {}
    named = (cname, ref, col) in {("S01_shift_a", "Jcw", "optimizer:z_c"), ("S05_shift_c", "Jcw", "physical:c_l")}
    TERM_SUM_TOL = 1e-12                                                      # relative to the full difference pair norm in the far-anchor block
    for h in HS:
        hh = h * scale
        (Dh_hi, Dh_lo), (D4_hi, D4_lo) = pairs[hh]
        if named:
            arrays[f"D_hi_{h:.0e}"] = Dh_hi.cpu().numpy(); arrays[f"D_lo_{h:.0e}"] = Dh_lo.cpu().numpy(); arrays[f"D4_hi_{h:.0e}"] = D4_hi.cpu().numpy(); arrays[f"D4_lo_{h:.0e}"] = D4_lo.cpu().numpy()
    arrays["d_column"] = d.cpu().numpy(); arrays["row_groups"] = case.row_group.cpu().numpy()
    if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
        am = case.anchor_mask
        npde = int(prob.w_node.numel() * prob.w_ang.numel() * 3)
        amp = am[:npde]
        arrays["anchor_mask"] = am.cpu().numpy()
        wn = (prob.w_node[:, None] * prob.w_ang[None, :]).sqrt()
        def weighted_terms_dd(zf, terms):
            c_l = float(zf[-2]); sch, scl = DC.scale_mom_dd(model, c_l, device=zf.device)
            if prob.nl_weighting:
                if ref == "Jf":
                    w = prob.nl_w_mom
                else:
                    with torch.no_grad():
                        tabs64 = prob.pressure_tables_at(zf, differentiable=False)["main"]          # the SAME weights as the rows: evaluated with the tables at z's own parameters (residual_dd)
                        ev = prob.evaluate(zf, tables=dict(main=tabs64)); w = prob.nl_weights_from_ev(ev, differentiable=False)[0]
                sch, scl = dd_mul_f(sch, scl, w.sqrt())
            out = {}
            for k, parts in (("lin", terms["lin"]), ("conv", terms["conv"]), ("gradP", [(terms["gradP"][0][i], terms["gradP"][1][i]) for i in range(3)])):
                hs_, ls_ = [], []
                for i in range(3):
                    h_, l_ = dd_mul_f(parts[i][0], parts[i][1], wn); h_, l_ = DC.FDD.dd_mul_dd(h_, l_, sch[:, None].expand_as(h_), scl[:, None].expand_as(h_))
                    hs_.append(h_.reshape(-1)); ls_.append(l_.reshape(-1))
                out[k] = (torch.cat(hs_), torch.cat(ls_))
            return out
        def term_funs(q):
            zz = to_full(q); dd_ = model.unpack_all(zz); c_l = dd_["c_l"]
            F = model.fields_grid(zz, need_vort=False)
            from src.equations.linear_stable import linear_velocity
            lin = linear_velocity(model, zz)
            conv = torch.einsum('m...,mi...->i...', F['U'], F['GU'])
            tabs = prob.pressure_tables_at(zz, differentiable=True)["main"]
            f = res.pressure_source(F['GU'])
            _, gradP, _, _ = (prob.pressure._solve_fp64(f, tables=tabs) if getattr(prob, "jacobian_fp64", False) else prob.pressure.solve(f, tables=tabs))
            sc = prob.scale_mom(c_l)
            if prob.nl_weighting:
                if ref == "Jf":
                    w = prob.nl_w_mom
                else:
                    ev = prob.evaluate(zz, tables=dict(main=tabs)); w = prob.nl_weights_from_ev(ev, differentiable=True)[0]
                sc = sc * w.sqrt()
            W = (wn * sc[:, None])[None]
            return torch.stack([(lin * W).reshape(-1), (conv * W).reshape(-1), (gradP * W).reshape(-1)], 0)
        d_terms = torch.func.jvp(term_funs, (zc,), (e,))[1].detach()        # (3, npde) analytic term derivatives (float64 jvp, the reference's weight semantics)
        arrays["d_terms"] = d_terms.cpu().numpy()
        consistency = float((d_terms.sum(0) - d[:npde]).norm() / max(float(d[:npde].norm()), 1e-300))
        split["analytic_term_sum_vs_column_rel"] = consistency
        split["analytic_term_sum_decision"] = bool(consistency <= 1e-10)
        all_ok = True
        for h in HS:
            hh = h * scale
            for t_ in (hh, -hh, 2 * hh, -2 * hh):
                if t_ not in term_store:
                    raise SystemExit(f"per-term record missing for the stencil point {t_}: run stopped (V245 (e))")
            W = {t_: weighted_terms_dd(term_store[t_][1], term_store[t_][0]) for t_ in (hh, -hh, 2 * hh, -2 * hh)}
            row = {}
            sum2 = None; sum4 = None
            for ki, k in enumerate(("lin", "conv", "gradP")):
                # centered pair
                c_h, c_l_ = dd_add(W[hh][k][0], W[hh][k][1], -W[-hh][k][0], -W[-hh][k][1]); c_h, c_l_ = DC.dd_div_f_pair(c_h, c_l_, 2.0 * hh)
                # five-point pair: (8 r+ - 8 r- - r2+ + r2-) / (12 h)
                a_h, a_l = dd_mul_f(W[hh][k][0], W[hh][k][1], 8.0); b_h, b_l = dd_mul_f(W[-hh][k][0], W[-hh][k][1], -8.0)
                f_h, f_l = dd_add(a_h, a_l, b_h, b_l); f_h, f_l = dd_add(f_h, f_l, -W[2 * hh][k][0], -W[2 * hh][k][1]); f_h, f_l = dd_add(f_h, f_l, W[-2 * hh][k][0], W[-2 * hh][k][1])
                f_h, f_l = DC.dd_div_f_pair(f_h, f_l, 12.0 * hh)
                Dk = (c_h + c_l_)[amp]; D4k = (f_h + f_l)[amp]; dk = d_terms[ki][amp]
                row[k] = dict(norm_D=float(Dk.norm()), norm_D4=float(D4k.norm()), norm_d=float(dk.norm()), norm_D_minus_d=float((Dk - dk).norm()), norm_D4_minus_d=float((D4k - dk).norm()))
                arrays[f"term_{k}_D_hi_{h:.0e}"] = c_h[amp].cpu().numpy(); arrays[f"term_{k}_D_lo_{h:.0e}"] = c_l_[amp].cpu().numpy()
                arrays[f"term_{k}_D4_hi_{h:.0e}"] = f_h[amp].cpu().numpy(); arrays[f"term_{k}_D4_lo_{h:.0e}"] = f_l[amp].cpu().numpy()
                sum2 = (c_h, c_l_) if sum2 is None else dd_add(sum2[0], sum2[1], c_h, c_l_)
                sum4 = (f_h, f_l) if sum4 is None else dd_add(sum4[0], sum4[1], f_h, f_l)
            (Dh_hi, Dh_lo), (D4_hi, D4_lo) = pairs[hh]
            # term-sum check in double-double before rounding (V252 (c)): (sum of term pairs) - (full pair) on the far-anchor rows
            r2h, r2l = dd_add(sum2[0][amp], sum2[1][amp], -Dh_hi[:npde][amp], -Dh_lo[:npde][amp]); r4h, r4l = dd_add(sum4[0][amp], sum4[1][amp], -D4_hi[:npde][amp], -D4_lo[:npde][amp])
            full2 = float((Dh_hi[:npde][amp] + Dh_lo[:npde][amp]).norm()); full4 = float((D4_hi[:npde][amp] + D4_lo[:npde][amp]).norm())
            rel2 = float((r2h + r2l).norm()) / max(full2, 1e-300); rel4 = float((r4h + r4l).norm()) / max(full4, 1e-300)
            ok = bool(rel2 <= TERM_SUM_TOL and rel4 <= TERM_SUM_TOL)
            all_ok = all_ok and ok
            row["term_sum_check"] = dict(centered_rel=rel2, five_point_rel=rel4, tolerance=TERM_SUM_TOL, decision=("PASS" if ok else "FAIL"))
            if not named:
                arrays[f"D_hi_far_{h:.0e}"] = Dh_hi[:npde][amp].cpu().numpy(); arrays[f"D_lo_far_{h:.0e}"] = Dh_lo[:npde][amp].cpu().numpy()
                arrays[f"D4_hi_far_{h:.0e}"] = D4_hi[:npde][amp].cpu().numpy(); arrays[f"D4_lo_far_{h:.0e}"] = D4_lo[:npde][amp].cpu().numpy()
            split[f"{h:.0e}"] = row
        split["term_split_valid"] = bool(all_ok and split["analytic_term_sum_decision"])
        split["note"] = "a failed term-sum check makes the per-term split invalid; the (l) outcome rests on the full difference (lead 10:34:22Z item 2 (c))"
    npz_path = os.path.join(ROOT, "validation", f"l_eval_{cname}_{ref}_{tag}_arrays.npz")
    if os.path.exists(npz_path):
        raise FileExistsError(npz_path)
    np.savez_compressed(npz_path, **arrays)
    npz_sha = sha(npz_path)
    rec = dict(case=cname, pair=case.pair, cost=case.cost, reference=ref, column=col, coords=coords, scale=scale, steps=HS, scope=scope, scope_sha256=sha(scope_path),
               same_function_check=dict(path=chk_path, sha256=sha(chk_path), passed=True, detail=chk["references"][ref]),
               column_norm=float(d.norm()), registered_recomputed=t_reg, l_outcome=t_l, far_anchor_term_split=split,
               arrays_npz=dict(path=os.path.relpath(npz_path, ROOT), sha256=npz_sha, keys=sorted(arrays), named_comparison_full_rows=named,
                               content=("full (hi, lo) arrays of D_h and D4_h at every step for all rows" if named else "far-anchor-block (hi, lo) arrays of D_h and D4_h at every step") + "; per-term (hi, lo) arrays (centered and five-point) on the far-anchor block; d column; analytic term derivatives; row groups; anchor mask"),
               ladder_pairs={f"{h:.0e}": dict(D_hi_norm=float(pairs[h * scale][0][0].norm()), D_lo_norm=float(pairs[h * scale][0][1].norm()), D4_hi_norm=float(pairs[h * scale][1][0].norm()), D4_lo_norm=float(pairs[h * scale][1][1].norm()),
                                             ) for h in HS},
               active_sets=dict(base_and_stencil=ladder_store.get("active"), identical=t_l.get("active_sets_identical")),
               pressure_arg_ranges_per_point=fun_dd.ranges,
               sources=cur, l_eval_sha256=cur_eval, accepted_scope_sha256=scope_sha,
               labels=dict(registered="registered rule (float64 ladder of the production reference, recomputed here)", l="pass/fail under the post-result rule 3.6 (l) (double-double differences; test-only copy); a FAIL is a possible derivative defect under 3.4 (d)"),
               nonlinear_weights_Jf_status="inactive by construction in J_f (weights frozen); decided on J_cw and J_c by the screen",
               arithmetic=dict(differences="D_h = (r+ - r-) and D4_h = (8 r+ - 8 r- - r2+ + r2-) formed as (hi, lo) pairs from the double-double rows; the pairs are divided by 2h and 12h with exact_matmul.dd_div_f and rounded to float64 once (lead 10:13:16Z, V240)",
                               richardson="formed by the registered harness (gates.best_richardson) from the float64-rounded D_h values, as in the registered evaluation (no pair Richardson is formed)",
                               noise_level="if ||D_h - d|| 2h is recomputed from these differences, D_h is the once-rounded value above; the subtraction D_h - d is float64 as in the registered harness",
                               per_term_split="term pairs divided by 2h with dd_div_f and rounded once; analytic term derivatives by float64 jvp"),

               seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_path, "x") as fh_:
        json.dump(rec, fh_, indent=1, default=str)
    def summ(t):
        return dict(PASS=t.get("PASS"), PASS_rel=t.get("PASS_rel"), absolute_only=t.get("absolute_only"), far_anchor=(t.get("group_pass") or {}).get("far_anchor_block", {}).get("PASS"),
                    far_e2={h: (t["per_group"][h]["second_order"].get("far_anchor_block")) for h in t["per_group"]})
    print("registered:", json.dumps(summ(t_reg), default=str)); print("(l):", json.dumps(summ(t_l), default=str)); print("split:", json.dumps(split, default=str)[:1500])
    print("DONE", out_path, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
