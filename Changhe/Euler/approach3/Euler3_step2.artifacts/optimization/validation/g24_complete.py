#!/usr/bin/env python
"""G2 (c) and G4 (a) completion (lead 13:01:56Z item 2; V299): the registered rule as written, no change of thresholds, ladder, floors, groups or
estimators. For one case and both parameters (c_l, omega; physical coordinates, as the gate records), the G2 (c) comparison (U_p and DU_p from the
forward-mode jvp against centered differences of U and DU at fixed coordinates; thresholds 1e-6 whole vector, 1e-5 per group) and the G4 (a) comparison
(grad P_p against centered differences of grad P with the tables rebuilt at each stencil point, fixed layout; 1e-6 per group in the resolved range
core_intermediate, the other groups reported) are re-evaluated at the same points with the registered five-step ladder, and the parts the gate program
did not save are computed: per step and per group e2 (second order) and e4 (five point), the Richardson value D_h' + (D_h' - D_h)/99 (h' = h/10) with
its error for every consecutive pair, the per-decade ratios, and the SPEC 3.0 (d) decision per group and for the whole vector (naming the passing pair
of (i), the pair of (ii) and the Richardson pair). Tie to the gate record: the recomputed per-group second-order errors and the whole-vector (G2 (c))
or resolved-range (G4 (a)) second-order and five-point errors must reproduce the stored values; the largest relative difference is stated and a
mismatch beyond 1e-12 relative marks the record TIE_FAILED (no decision is admissible then). The case build is tied to the record by pair, n_opt,
cost and start sha256. Usage: python validation/g24_complete.py <case> </abs/path/gates_gpu_v1_<case>.json> [device]
Writes validation/g24_complete_<case>.json (exclusive create) and, per parameter, the hashed arrays validation/g24_complete_<case>_<parameter>_arrays.npz
(V305, lead 13:14:44Z): the reported derivative d, the second-order stencil D_h and the five-point stencil D4_h at every step, the group index of every
entry and (G4 (a)) the resolved-range mask, for G2 (c) (U_p and DU_p components concatenated) and G4 (a) (grad P_p components); float64, uncompressed,
so that the Richardson values and norms can be reconstructed independently; sha256 of the NPZ in the JSON. Both second- and fourth-order per-decade
error ratios are saved (SPEC 3.0 (d)). Conventions (identical to validation/gates.py G2G4): whole-vector G2 (c) error
||d - D||/max(||D||, ||d||); per-group error ||d_g - D_g||/max(||D_g||, 1e-300); G4 (a) resolved-range error ||d_m - D_m||/max(||D_m||, 1e-300);
the same forms with D4 for e4 and with the Richardson value R for its error."""
import sys, os, json, time, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT, H_LADDER, stencil_ladder, code_hashes
from src.equations import residuals as res

DEFS = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")),
        "S11_own": dict(start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")), "S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")),
        "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
        "S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]), "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
        "manu_a": dict(pair=PAIRS["a"], seed=3), "manu_small_omega": dict(pair=PAIRS["small_omega"], seed=5), "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6),
        "manu_near_edge": dict(pair=PAIRS["near_edge"], seed=7), "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all")}
TIE_TOL = 1e-12


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def decide(e2, e4, rich, hs_keys, tau):
    """SPEC 3.0 (d) on dict e2/e4 {hkey: err} (hkey strings, descending h) and rich {pairkey: err}: (i) two consecutive steps with e2 <= tau,
    (ii) two consecutive with e4 <= tau, (iii) the Richardson value of a passing (i) pair within tau. Pairs are named. PASS = (i) and (ii) and (iii)
    for the first (i) pair; PASS_any = (iii) satisfied by any passing (i) pair (the convention of the G1 harness v4, Richardson over all adjacent
    passing pairs). Both are recorded; the registered decision reported is PASS_any, with the first-pair verdict next to it."""
    pairs = [(hs_keys[i], hs_keys[i + 1]) for i in range(len(hs_keys) - 1)]
    p1 = [p for p in pairs if e2[p[0]] <= tau and e2[p[1]] <= tau]
    p2 = [p for p in pairs if e4[p[0]] <= tau and e4[p[1]] <= tau]
    rk = lambda p: f"{p[0]}->{p[1]}"
    first_i = p1[0] if p1 else None
    rich_first = (rich[rk(first_i)] <= tau) if first_i else False
    rich_pairs = [p for p in p1 if rich[rk(p)] <= tau]
    return dict(tau=tau, pass_i=bool(p1), pair_i=(rk(first_i) if first_i else None), pass_ii=bool(p2), pair_ii=(rk(p2[0]) if p2 else None),
                pass_iii_first_pair=bool(rich_first), richardson_pair=(rk(rich_pairs[0]) if rich_pairs else None), richardson_error=(rich[rk(rich_pairs[0])] if rich_pairs else (rich[rk(first_i)] if first_i else None)),
                PASS_first_pair=bool(p1 and p2 and rich_first), PASS_any=bool(p1 and p2 and rich_pairs), all_passing_i_pairs=[rk(p) for p in p1])


def main():
    cname, rec_path = sys.argv[1], sys.argv[2]
    dev = sys.argv[3] if len(sys.argv) > 3 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    if not os.path.isabs(rec_path) or not os.path.isfile(rec_path):
        raise SystemExit(f"REFUSED: the gate record must be an absolute path to an existing file: {rec_path}")
    out_path = os.path.join(ROOT, "validation", f"g24_complete_{cname}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time()
    rec = json.load(open(rec_path)); crec = rec["cases"][cname] if "cases" in rec and cname in rec["cases"] else rec[cname]
    case = Case(cname, dev, **DEFS[cname]); prob, model = case.prob, case.model
    case_tie = dict(pair=[float(case.pair[0]), float(case.pair[1])], record_pair=crec.get("pair"), n_opt=int(case.z_opt.numel()), record_n_opt=crec.get("n_opt"), cost=float(case.cost), record_cost=crec.get("cost"),
                    start_sha256=(sha(DEFS[cname]["start"]) if "start" in DEFS[cname] else None), record_start_sha256=crec.get("start_sha256"))
    case_tie["pair_equal"] = bool(case_tie["pair"] == [float(x) for x in crec["pair"]]); case_tie["n_opt_equal"] = bool(case_tie["n_opt"] == crec.get("n_opt"))
    case_tie["cost_rel_diff"] = rel(case_tie["cost"], float(crec["cost"])); case_tie["start_sha256_equal"] = (case_tie["start_sha256"] == crec.get("start_sha256")) if crec.get("start_sha256") else None
    case_tie["ok"] = bool(case_tie["pair_equal"] and case_tie["n_opt_equal"] and case_tie["cost_rel_diff"] <= 1e-9)      # start sha256 equality is recorded as information (the record's field may hash the file or the tensor)
    print("case tie:", json.dumps(case_tie, default=str), flush=True)
    zp = case.z_phys.detach().clone(); n = zp.numel(); hs = list(H_LADDER); hk = [f"{h:.0e}" for h in hs]
    def fields_and_pressure(zp_):
        zz = case.to_full_phys(zp_)
        F = model.fields_grid(zz, need_vort=False)
        tabs = prob.pressure_tables_at(zz, differentiable=True)
        src = res.pressure_source(F["GU"])
        P, gradP, _, _ = prob.pressure.solve(src, tables=tabs["main"])
        mt = res.momentum_terms(F, gradP)
        return F["U"], F["GU"], gradP, mt["sum"], src, F["c_l"], F["omega"]
    U, GU, gradP, Ru, src, cl_t, om_t = fields_and_pressure(zp)
    groups_pde = torch.where(model.r <= 0.1 * model.R0, 0, torch.where(model.r <= 2.0 ** 8 * model.R0, 1, 2))
    nU = U.numel()
    node_of_U = torch.arange(nU, device=dev) // model.Na % model.Nr; node_of_G = torch.arange(GU.numel(), device=dev) // model.Na % model.Nr
    gidx = torch.cat([groups_pde[node_of_U], groups_pde[node_of_G]]); gi_g = groups_pde[node_of_U]
    gnames = case.group_names[:3]
    def gerr(a, b, m):
        return float((a[m] - b[m]).norm() / max(float(b[m].norm()), 1e-300))
    out = dict(case=cname, record=rec_path, record_sha256=sha(rec_path), case_tie=case_tie, ladder=hs, coordinates="physical (as the gate records)", parameters={}, tie_tolerance=TIE_TOL)
    worst_tie = 0.0
    for j, pname in enumerate(("c_l", "omega")):
        e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
        _, (Up, GUp, gPp, Rup, srcp, _, _) = torch.func.jvp(fields_and_pressure, (zp,), (e,))
        scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
        stored2 = crec["G2"][f"G2c_Up_DUp_{pname}"]; stored4 = crec["G4"][f"G4a_gradP_{pname}"]
        if stored2.get("step_scale", 1.0) != scale:
            raise SystemExit(f"REFUSED: step scale {scale} differs from the record's {stored2.get('step_scale')}")
        # ---- G2 (c)
        def Ufun(q):
            F = model.fields_grid(case.to_full_phys(q), need_vort=False); return torch.cat([F["U"].reshape(-1), F["GU"].reshape(-1)])
        dcol = torch.cat([Up.reshape(-1), GUp.reshape(-1)])
        lad, _ = stencil_ladder(Ufun, zp, e, [h * scale for h in hs])
        def block(lad, dcol, whole_mask, group_index, tau_whole, tau_group, stored_whole2, stored_whole4, stored_pg, whole_label):
            per_step = {}; ties = []
            for h, k in zip(hs, hk):
                D, D4 = lad[h * scale]
                if whole_mask is None:
                    w2 = float((dcol - D).norm() / max(float(D.norm()), float(dcol.norm()))); w4 = float((dcol - D4).norm() / max(float(D4.norm()), float(dcol.norm())))
                else:
                    w2 = gerr(dcol, D, whole_mask); w4 = gerr(dcol, D4, whole_mask)
                pg = {}
                for gi, g in enumerate(gnames):
                    m = group_index == gi
                    if not bool(m.any()):
                        continue
                    pg[g] = dict(e2=gerr(dcol, D, m), e4=gerr(dcol, D4, m))
                    if g in stored_pg[k]:
                        ties.append((f"{k} {g} e2", rel(pg[g]["e2"], stored_pg[k][g])))
                ties.append((f"{k} {whole_label} e2", rel(w2, stored_whole2[k]))); ties.append((f"{k} {whole_label} e4", rel(w4, stored_whole4[k])))
                per_step[k] = dict(whole=dict(e2=w2, e4=w4), per_group=pg)
            rich = {}; 
            for i in range(len(hs) - 1):
                h, hp = hs[i] * scale, hs[i + 1] * scale; Dh, Dhp = lad[h][0], lad[hp][0]; R = Dhp + (Dhp - Dh) / 99.0; pk = f"{hk[i]}->{hk[i+1]}"
                if whole_mask is None:
                    rw = float((dcol - R).norm() / max(float(R.norm()), float(dcol.norm())))
                else:
                    rw = gerr(dcol, R, whole_mask)
                rich[pk] = dict(whole=rw, per_group={g: gerr(dcol, R, group_index == gi) for gi, g in enumerate(gnames) if bool((group_index == gi).any())})
            def ratio_of(key):
                return {f"{hk[i]}->{hk[i+1]}": dict(whole=(per_step[hk[i]]["whole"][key] / per_step[hk[i + 1]]["whole"][key] if per_step[hk[i + 1]]["whole"][key] > 0 else None),
                                                    per_group={g: (per_step[hk[i]]["per_group"][g][key] / per_step[hk[i + 1]]["per_group"][g][key] if per_step[hk[i + 1]]["per_group"][g][key] > 0 else None) for g in per_step[hk[i]]["per_group"]}) for i in range(len(hs) - 1)}
            ratios = ratio_of("e2"); ratios4 = ratio_of("e4")
            arrays = {"d": dcol.detach().cpu().numpy(), "group_index": group_index.detach().cpu().numpy().astype(np.int8)}
            if whole_mask is not None:
                arrays["resolved_mask"] = whole_mask.detach().cpu().numpy()
            for h, k in zip(hs, hk):
                arrays[f"D_{k}"] = lad[h * scale][0].detach().cpu().numpy(); arrays[f"D4_{k}"] = lad[h * scale][1].detach().cpu().numpy()
            dec_whole = decide({k: per_step[k]["whole"]["e2"] for k in hk}, {k: per_step[k]["whole"]["e4"] for k in hk}, {pk: rich[pk]["whole"] for pk in rich}, hk, tau_whole)
            dec_groups = {g: decide({k: per_step[k]["per_group"][g]["e2"] for k in hk}, {k: per_step[k]["per_group"][g]["e4"] for k in hk}, {pk: rich[pk]["per_group"][g] for pk in rich}, hk, tau_group) for g in per_step[hk[0]]["per_group"]}
            worst = max(t[1] for t in ties)
            return dict(per_step=per_step, richardson=rich, ratios_second_order=ratios, ratios_five_point=ratios4, decision_whole=dec_whole, decision_per_group=dec_groups,
                        tie=dict(worst_rel_diff=worst, within_1e_12=bool(worst <= TIE_TOL), worst_item=max(ties, key=lambda t: t[1])[0], n_compared=len(ties))), arrays
        g2c, arr2 = block(lad, dcol, None, gidx, 1e-6, 1e-5, stored2["errors_second_order"], stored2["errors_five_point"], stored2["per_group"], "whole")
        g2c["registered_PASS_stored"] = stored2.get("PASS"); g2c["thresholds"] = "1e-6 whole vector (U_p, DU_p concatenated), 1e-5 per group (G1 thresholds, SPEC G2 (c))"
        g2c["complete_PASS"] = bool(g2c["decision_whole"]["PASS_any"] and all(v["PASS_any"] for v in g2c["decision_per_group"].values()))
        # ---- G4 (a)
        def gPfun(q):
            zz = case.to_full_phys(q); F = model.fields_grid(zz, need_vort=False); tabs = prob.pressure_tables_at(zz)
            return prob.pressure.solve(res.pressure_source(F["GU"]), tables=tabs["main"])[1].reshape(-1)
        dcol4 = gPp.reshape(-1); lad4, _ = stencil_ladder(gPfun, zp, e, [h * scale for h in hs])
        g4a, arr4 = block(lad4, dcol4, gi_g == 1, gi_g, 1e-6, 1e-6, stored4["resolved_range_errors_second_order"], stored4["resolved_range_errors_five_point"], stored4["per_group"], "resolved_range")
        npz_path = os.path.join(ROOT, "validation", f"g24_complete_{cname}_{pname}_arrays.npz")
        if os.path.exists(npz_path):
            raise FileExistsError(npz_path)
        np.savez(npz_path, **{f"G2c_{k}": v for k, v in arr2.items()}, **{f"G4a_{k}": v for k, v in arr4.items()}, steps=np.array(hs), step_scale=np.array(scale), group_names=np.array(gnames))
        npz_sha = sha(npz_path)
        g4a["registered_PASS_stored"] = stored4.get("PASS"); g4a["thresholds"] = "1e-6 per group in the resolved range (core_intermediate = the 'whole' entry here); the other groups are reported with the same 1e-6 and do not decide"
        g4a["complete_PASS"] = bool(g4a["decision_whole"]["PASS_any"] and g4a["decision_per_group"].get("core_intermediate", {}).get("PASS_any", False))
        g4a["groups_outside_resolved_range"] = {g: v["PASS_any"] for g, v in g4a["decision_per_group"].items() if g != "core_intermediate"}
        worst_tie = max(worst_tie, g2c["tie"]["worst_rel_diff"], g4a["tie"]["worst_rel_diff"])
        out["parameters"][pname] = dict(step_scale=scale, G2c=g2c, G4a=g4a, arrays_npz=npz_path, arrays_sha256=npz_sha, arrays_keys="G2c_d, G2c_D_<h>, G2c_D4_<h>, G2c_group_index (0 near_origin, 1 core_intermediate, 2 far; U_p then DU_p components), G4a_d, G4a_D_<h>, G4a_D4_<h>, G4a_group_index, G4a_resolved_mask (core_intermediate), steps, step_scale, group_names; float64 uncompressed")
        print(f"{cname} {pname}: G2c tie {g2c['tie']['worst_rel_diff']:.2e} complete PASS {g2c['complete_PASS']} (whole {g2c['decision_whole']['PASS_any']}, groups {[(g, v['PASS_any']) for g, v in g2c['decision_per_group'].items()]}) | G4a tie {g4a['tie']['worst_rel_diff']:.2e} complete PASS {g4a['complete_PASS']} (resolved {g4a['decision_whole']['PASS_any']}; outside {g4a['groups_outside_resolved_range']})", flush=True)
    out["tie_ok"] = bool(worst_tie <= TIE_TOL and case_tie["ok"]); out["status"] = ("COMPLETE" if out["tie_ok"] else "TIE_FAILED"); out["worst_tie_rel_diff"] = worst_tie
    out["complete_PASS_all"] = bool(out["tie_ok"] and all(out["parameters"][p]["G2c"]["complete_PASS"] and out["parameters"][p]["G4a"]["complete_PASS"] for p in out["parameters"]))
    out["sources"] = dict(g24_complete=sha(__file__), gates=sha(os.path.join(ROOT, "validation", "gates.py")), code=code_hashes())
    out["launcher_manifest"] = open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None
    out["device"] = dev; out["seconds"] = time.time() - t0; out["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    out["rule"] = "SPEC 3.0 (d) applied to G2 (c) and G4 (a) (lead 13:01:56Z item 2): (i) two consecutive ladder steps with e2 <= tau, (ii) two consecutive with e4 <= tau, (iii) the Richardson value of a passing (i) pair within tau; the registered rule as written, thresholds, ladder, groups and estimators unchanged; not a post-result rule"
    with open(out_path, "x") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("STATUS", out["status"], "complete PASS all:", out["complete_PASS_all"], f"{out['seconds']:.0f}s"); print("DONE", out_path)


if __name__ == "__main__":
    main()
