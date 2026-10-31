#!/usr/bin/env python
"""SPEC v1.19 3.6 (l) (5), power check (lead 10:15:00Z item 3): the G8 controls (i) kernel tables frozen and (iii) far rows parameter-frozen,
built exactly as validation/g8_controls.py builds their Jacobian columns (physical coordinates, both parameters), are judged against the (l)
differences (the double-double residual copy's ladder, J_f reference: weights and closure target held, as the registered G8 reference
residual_vector_rebuild) with the registered harness machinery (gates.column_test with the ladder replaced). Each control must still fail by at least 100 tau in the group it excites: 1e-4 for the whole column (tau 1e-6) and 1e-3 for an individual group
(tau_group 1e-5), as in g8_controls.py (verifier 10:23:46Z); the group is recorded with the case. V245: accepted scope sha256 bound, double-double
classes enforced, same-function evidence (J_f, physical coordinates, same sources) required, active-set recorder passed. Requires validation/l_scope.json (accepted scope). Output:
validation/l_power_<case>.json (exclusive create). Usage: python validation/l_power.py <case> <accepted l_scope.json sha256> [device]"""
import sys, os, json, time, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation import gates as G
from validation.gates import Case, PAIRS, ROOT, column_test
from validation import dd_chain as DC
from src.optimization.lm import param_columns
import src.optimization.problem as problem_mod

CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
              "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"])}
HS = [1e-4, 1e-5, 1e-6]          # the G8 ladder of g8_controls.py
FAIL_LEVEL_ALL = 1e-4            # 100 tau for the whole column (tau 1e-6)
FAIL_LEVEL_GROUP = 1e-3          # 100 tau_group for each group (tau_group 1e-5), as in g8_controls.py (verifier 10:23:46Z)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    cname = sys.argv[1]; scope_sha = sys.argv[2] if len(sys.argv) > 2 else None
    dev = sys.argv[3] if len(sys.argv) > 3 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    problem_mod.TABLE_CACHE = False
    scope_path = os.path.join(ROOT, "validation", "l_scope.json")
    if not os.path.exists(scope_path) or not scope_sha or sha(scope_path) != scope_sha:
        raise SystemExit("validation/l_scope.json with the lead-accepted sha256 is required (lead 10:15:00Z item 1; V245 (a))")
    scope = json.load(open(scope_path))
    if not scope.get("screened_classes"):
        raise SystemExit("l_scope.json has no screened classes: refused (V256)")
    dd_classes = {k for k, v in scope["screened_classes"].items() if v.get("decision") == "double-double"}
    if dd_classes - DC.CARRIED_DD:
        raise SystemExit(f"scope assigns {sorted(dd_classes - DC.CARRIED_DD)} to double-double, which this copy evaluates in float64: run stopped (V245 (b))")
    chk_paths = {}
    for pcol in ("physical:c_l", "physical:omega"):                           # V252 (d): evidence for BOTH parameter stencils of this case in physical coordinates
        cp = os.path.join(ROOT, "validation", f"dd_chain_check_{cname}_{pcol.replace(':', '_')}.json")
        if not os.path.exists(cp):
            raise SystemExit(f"{cp} missing: the same-function check of the J_f reference along {pcol} must exist first")
        chk = json.load(open(cp))
        if chk.get("case") != cname or chk.get("column") != pcol or chk.get("sources") != DC.source_hashes(ROOT) or not chk["references"].get("Jf", {}).get("same_function_check"):
            raise SystemExit(f"same-function evidence for {pcol} (J_f) missing, failed, for another case, or produced with other sources (V245 (c), V252 (d))")
        chk_paths[pcol] = dict(path=os.path.relpath(cp, ROOT), sha256=sha(cp))
    out_path = os.path.join(ROOT, "validation", f"l_power_{cname}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time()
    case = Case(cname, dev, **CASE_TABLE[cname]); prob, model = case.prob, case.model
    zp = case.z_phys.detach().clone(); n = zp.numel()
    pfun = lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=True)
    Jp_ok = param_columns(pfun, zp, [n - 2, n - 1]).detach()
    # (i) kernel tables frozen at the base parameters (the Jacobian omits the table dependence)
    Jp_i = param_columns(lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=False), zp, [n - 2, n - 1]).detach()
    # (iii) far anchor rows with detached parameters (as g8_controls.py)
    orig_rv = prob.residual_vector
    def rv_far_detached(z, **kw):
        r = orig_rv(z, **kw)
        zd = torch.cat([z[:-2], z[-2:].detach()])
        kw2 = {k: v for k, v in kw.items() if k != "differentiable_pressure"}
        rd = orig_rv(zd, **kw2)
        Nr, Na = model.Nr, model.Na
        rr = r.clone()
        for c in range(3):
            a0 = c * Nr * Na + model.Nr_src * Na; a1 = c * Nr * Na + Nr * Na
            rr[a0:a1] = rd[a0:a1]
        return rr
    prob.residual_vector = rv_far_detached
    try:
        Jp_iii = param_columns(pfun, zp, [n - 2, n - 1]).detach()
    finally:
        prob.residual_vector = orig_rv
    # (l) ladder of the J_f reference (weights and closure target held)
    tcache = {}
    def fun_dd(q):
        zf = case.to_full_phys(q); key = (float(zf[-2]), float(zf[-1]))
        if key not in tcache:
            tcache[key] = DC.tables_dd(model, key[0], key[1], device=zf.device); tcache[key]["P"] = DC.pressure_tables_dd(prob, key[0], key[1])
        rh, rl, _ = DC.residual_dd(prob, zf, ref="Jf", T=tcache[key], case=case, q=q, coords="physical"); return rh, rl
    def act(zz_full):
        ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
        return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
    rec_act = lambda q: act(case.to_full_phys(q))
    orig_ladder = G.stencil_ladder
    def dd_stencil_ladder(fun, z, e_, hs_, record_active=None):
        lad, active, pairs = DC.ladder_dd(lambda q, t: fun_dd(q), z, e_, hs_, record_active=record_active); ladder_store["active"] = active; return lad, active
    G.stencil_ladder = dd_stencil_ladder
    results = {}; witnesses = {}; ladder_store = {}
    try:
        for name, Jp, note in (("i_kernel_tables_frozen", Jp_i, "the exact Green operator is parameter independent; the table dependence is a discretization-level effect"),
                               ("iii_far_rows_param_frozen", Jp_iii, f"{model.Nr - model.Nr_src} far anchor nodes (momentum rows with pressure)")):
            r = {}
            for j, pname in enumerate(("c_l", "omega")):
                e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
                scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
                t = column_test(case, f"(l) power {name} {pname}", Jp[:, j], None, zp, e, HS, ref=case.r, record_active=rec_act, scale=scale, deriv_scale=1.0)
                gmin = {g: min(h["second_order"][g] for h in t["per_group"].values()) for g in t["per_group"][f"{HS[0]:.0e}"]["second_order"]}
                omitted = float((Jp[:, j] - Jp_ok[:, j]).norm() / Jp_ok[:, j].norm())
                excited = {g: v for g, v in gmin.items() if v >= (FAIL_LEVEL_ALL if g == "all" else FAIL_LEVEL_GROUP)}
                r[pname] = dict(fails_G1_at_100tau=bool(excited), excited_groups=excited, per_group_min=gmin, min_error_all=gmin.get("all"), omitted_part_rel_norm=omitted, PASS=t["PASS"], note=note)
                witnesses[f"{name}:{pname}"] = dict(column_test=t, active_sets=ladder_store.get("active"))      # complete column_test and active-set witnesses (V252 (d))
                print(f"{name} {pname}: fails by >= 100 tau in {sorted(excited)}; omitted part {omitted:.2e}; min errors {json.dumps({g: f'{v:.1e}' for g, v in gmin.items()})}", flush=True)
            results[name] = r
    finally:
        G.stencil_ladder = orig_ladder
    rec = dict(case=cname, pair=case.pair, scope_sha256=sha(scope_path), accepted_scope_sha256=scope_sha, reference="Jf (weights and closure target held; the G8 reference residual_vector_rebuild)", steps=HS,
               fail_levels=dict(all=FAIL_LEVEL_ALL, group=FAIL_LEVEL_GROUP), sources=DC.source_hashes(ROOT), same_function_evidence=chk_paths, coordinates="physical", witnesses=witnesses,
               controls=results, power_met={k: all(v[p]["fails_G1_at_100tau"] for p in v) for k, v in results.items()},
               scripts=dict(l_power=sha(__file__), dd_chain=sha(os.path.join(ROOT, "validation", "dd_chain.py")), g8_controls=sha(os.path.join(ROOT, "validation", "g8_controls.py"))),
               seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_path, "x") as fh_:
        json.dump(rec, fh_, indent=1, default=str)
    print("DONE", out_path, rec["power_met"], f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
