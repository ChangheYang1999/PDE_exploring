#!/usr/bin/env python
"""Controls for branch_distance v7.3 (lead 19:57:34Z item 4, 20:39:10Z item 3 (a); V433, V452, V458 item 3): v7.3 cases added: one-ULP physical difference accepted, optimizer-coordinate displacements refused, checkpoint binding.
Controls for branch_distance v7 (lead 19:57:34Z item 4, V433): offline alterations of copies of the genuine records of one endpoint, judged through the tool's
own load_state() and parameter_part() (no field evaluation; CPU). Baseline: P2 segment-4 endpoint (runs/cont2_s4_S09_.../checkpoint_segment_end.pt) with the
lead's width record v6 and the EVAL npz it names, against the F1 medium endpoint. Every altered case must give agreement None (OPEN) with the named reason;
the baseline must decide. Output: validation/branch_distance/controls_v7_<HHMMSS>.json. Usage: python scripts/branch_distance_v7_controls.py"""
import sys, os, json, shutil, tempfile, math, time, hashlib, importlib.util
import numpy as np, torch
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
spec = importlib.util.spec_from_file_location("bd", os.path.join(ROOT, "scripts", "branch_distance.py")); bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bd)
LEAD = "RUN_ROOT/lead/notes"
A = os.path.join(ROOT, "runs/cont2_s4_S09_L6_cl0.4500_om0.3000_free/starts/start_000.pt")
B = os.path.join(ROOT, "runs/f1_S05_m1_L6_cl0.4500_om0.3000_free/starts/start_000.pt")
SENS = os.path.join(LEAD, "sens_s4records_v6/cont2_s4_S09_L6_cl0.4500_om0.3000_free.json")
JCD = os.path.join(ROOT, "validation/jc_eval/cont2_s4_S09_L6_cl0.4500_om0.3000_free"); NPZ = os.path.join(JCD, "linearization_00648_eval_complete.npz")
dev = torch.device("cpu"); t0 = time.time()
_, _, ia = bd.load_state(A, dev); _, _, ib = bd.load_state(B, dev)
results = []


def case(name, expect_open, sens=SENS, jc=NPZ, st_a=None, reason_substr=None):
    st = dict(ia) if st_a is None else st_a
    try:
        r = bd.parameter_part(st, ib, sens, jc, "a", 1e-12)
    except SystemExit as e:
        r = dict(agreement=None, status=f"REFUSED: {e}")
    agr = r.get("agreement"); status = r.get("status", "")
    ok = (agr is None) if expect_open else (agr is not None)
    if ok and reason_substr:
        ok = reason_substr in status
    results.append(dict(case=name, expect_open=expect_open, agreement=agr, status=status[:600], c_over_t=r.get("c_over_t"), pass_=ok))
    print(("PASS" if ok else "FAIL"), name, "->", agr, "|", status[:160])


def tmp_copy(alter_json=None, alter_npz=None, alter_sens=None, drop_json=False):
    """copy the EVAL directory (json + npz) and the width record into a temp dir, apply alterations, return (sens_path, npz_path)."""
    d = tempfile.mkdtemp(prefix="bdctrl_", dir=os.path.join(ROOT, "validation", "branch_distance"))
    jd = os.path.join(d, "jc"); os.makedirs(jd)
    npz = os.path.join(jd, os.path.basename(NPZ)); Z = dict(np.load(NPZ, allow_pickle=True))
    if alter_npz:
        alter_npz(Z)
    np.savez(npz, **Z)
    jj = json.load(open(os.path.join(JCD, "jc_eval.json")))
    if alter_json:
        alter_json(jj)
    if not drop_json:
        json.dump(jj, open(os.path.join(jd, "jc_eval.json"), "w"))
    S = json.load(open(SENS)); S["record_meta"]["record"] = npz          # the width record must name the npz it was made from: point the copy at the copied npz
    if alter_sens:
        alter_sens(S)
    sp = os.path.join(d, "sens.json"); json.dump(sp and S, open(sp, "w"))
    return sp, npz


# 0. baseline on the genuine files (the genuine width record names the genuine npz)
case("baseline genuine records (must decide)", False)
# 0b. baseline through the copy mechanism (copies unaltered; the copied EVAL json still binds to the genuine checkpoint): must decide
sp, npz = tmp_copy(); case("unaltered copies (must decide)", False, sp, npz)
# 1. width record c_l displaced by 5e-10 (about 1e9 ULP): refused by the 2-ULP map rule
sp, npz = tmp_copy(alter_sens=lambda S: S["record_meta"]["params_record"].__setitem__("c_l", S["record_meta"]["params_record"]["c_l"] + 5e-10)); case("width record c_l + 5e-10", True, sp, npz, reason_substr="not within 2 ULP")
# 2. width record omega displaced by 5e-10
sp, npz = tmp_copy(alter_sens=lambda S: S["record_meta"]["params_record"].__setitem__("omega", S["record_meta"]["params_record"]["omega"] + 5e-10)); case("width record omega + 5e-10", True, sp, npz, reason_substr="not within 2 ULP")
# 2b. width record omega displaced by ONE ULP (metadata rounding): accepted (optimizer coordinates bitwise equal; physical within 2 ULP)
sp, npz = tmp_copy(alter_sens=lambda S: S["record_meta"]["params_record"].__setitem__("omega", np.nextafter(S["record_meta"]["params_record"]["omega"], 1.0).item())); case("width record omega + 1 ULP (must decide)", False, sp, npz)
# 2c. width record z_w displaced by ONE ULP: refused (optimizer coordinates must be bitwise equal)
sp, npz = tmp_copy(alter_sens=lambda S: S["record_meta"]["params_record"].__setitem__("z_w", np.nextafter(S["record_meta"]["params_record"]["z_w"], 1.0).item())); case("width record z_w + 1 ULP", True, sp, npz, reason_substr="optimizer coordinates")
# 2d. EVAL npz z_opt tail displaced by one ULP: refused
sp, npz = tmp_copy(alter_npz=lambda Z: Z.__setitem__("z_opt", np.concatenate([np.asarray(Z["z_opt"])[:-1], [np.nextafter(float(np.asarray(Z["z_opt"])[-1]), 1.0)]]))); case("npz z_opt z_w + 1 ULP", True, sp, npz, reason_substr="z_opt tail")
# 2e. EVAL json z_c displaced by one ULP: refused
sp, npz = tmp_copy(alter_json=lambda j: j["params"].__setitem__("z_c", np.nextafter(j["params"]["z_c"], 1.0).item())); case("jc_eval.json z_c + 1 ULP", True, sp, npz, reason_substr="optimizer coordinates")
# 3. width record O1 displaced by one ulp
sp, npz = tmp_copy(alter_sens=lambda S: S.__setitem__("O1", np.nextafter(S["O1"], 1.0).item())); case("width record O1 + 1 ulp", True, sp, npz, reason_substr="not finite and exactly equal")
# 4. width record_meta.cost displaced
sp, npz = tmp_copy(alter_sens=lambda S: S["record_meta"].__setitem__("cost", S["record_meta"]["cost"] * (1 + 1e-13))); case("width record_meta.cost x (1 + 1e-13)", True, sp, npz, reason_substr="record_meta.cost")
# 5. width record_meta.it as float
sp, npz = tmp_copy(alter_sens=lambda S: S["record_meta"].__setitem__("it", float(S["record_meta"]["it"]))); case("width record it stored as float", True, sp, npz, reason_substr="not an integer")
# 6. npz it stored as float
sp, npz = tmp_copy(alter_npz=lambda Z: Z.__setitem__("it", np.asarray(Z["it"], dtype=float))); case("npz it stored as float array", True, sp, npz, reason_substr="not stored as an integer array")
# 7. npz param_positions stored as float
sp, npz = tmp_copy(alter_npz=lambda Z: Z.__setitem__("param_positions", np.asarray(Z["param_positions"], dtype=float))); case("npz param_positions stored as float array", True, sp, npz, reason_substr="param_positions")
# 8. npz c_l displaced by 5e-10
sp, npz = tmp_copy(alter_npz=lambda Z: Z.__setitem__("c_l", np.asarray(float(Z["c_l"]) + 5e-10))); case("npz c_l + 5e-10", True, sp, npz, reason_substr="not within 2 ULP")
# 9. npz cost displaced by one ulp
sp, npz = tmp_copy(alter_npz=lambda Z: Z.__setitem__("cost", np.asarray(np.nextafter(float(Z["cost"]), 1.0)))); case("npz cost + 1 ulp", True, sp, npz, reason_substr="exactly equal")
# 10. jc_eval.json missing
sp, npz = tmp_copy(drop_json=True); case("jc_eval.json absent", True, sp, npz, reason_substr="no jc_eval.json")
# 11. jc_eval.json status FAILED
sp, npz = tmp_copy(alter_json=lambda j: j.__setitem__("status", "FAILED")); case("jc_eval.json status FAILED", True, sp, npz, reason_substr="not ACCEPTED")
# 12. jc_eval.json kind not EVAL
sp, npz = tmp_copy(alter_json=lambda j: j.__setitem__("kind", "RUN")); case("jc_eval.json kind RUN", True, sp, npz, reason_substr="is not EVAL")
# 13. jc_eval.json run names another run
sp, npz = tmp_copy(alter_json=lambda j: j.__setitem__("run", j["run"].replace("cont2_s4", "cont2_s3"))); case("jc_eval.json run is another run", True, sp, npz, reason_substr="not the state's run directory")
# 14. jc_eval.json checkpoint sha altered
sp, npz = tmp_copy(alter_json=lambda j: j["checkpoint"].__setitem__("sha256", "0" * 64)); case("jc_eval.json checkpoint sha256 altered", True, sp, npz, reason_substr="differs from the sibling checkpoint")
# 15. jc_eval.json checkpoint path = another file inside the run
sp, npz = tmp_copy(alter_json=lambda j: j["checkpoint"].__setitem__("path", j["checkpoint"]["path"].replace("checkpoint_segment_end.pt", "checkpoint.pt"))); case("jc_eval.json checkpoint path is checkpoint.pt", True, sp, npz, reason_substr="not the endpoint's sibling checkpoint")
# 16. jc_eval.json cost displaced by one ulp
sp, npz = tmp_copy(alter_json=lambda j: j.__setitem__("cost", np.nextafter(j["cost"], 1.0).item())); case("jc_eval.json cost + 1 ulp", True, sp, npz, reason_substr="jc_eval.json cost")
# 17. jc_eval.json params omega displaced by 5e-10
sp, npz = tmp_copy(alter_json=lambda j: j["params"].__setitem__("omega", j["params"]["omega"] + 5e-10)); case("jc_eval.json params omega + 5e-10", True, sp, npz, reason_substr="not within 2 ULP")
# 18. state with a NaN omega
st = dict(ia); st["omega"] = float("nan"); st["params_finite"] = False; case("state omega NaN", True, st_a=st, reason_substr="not finite")
# 19. state iteration count stored as float
st = dict(ia); st["iterations"] = float(st["iterations"]); st["iterations_is_int"] = False; case("state iteration count float", True, st_a=st, reason_substr="not")
# 20. a checkpoint offered as the state: REFUSED by load_state (v7.1)
try:
    bd.load_state(os.path.join(ROOT, "runs/cont2_s4_S09_L6_cl0.4500_om0.3000_free/checkpoint_segment_end.pt"), dev); results.append(dict(case="checkpoint offered as the state", expect_open=True, agreement=None, status="NOT REFUSED", pass_=False)); print("FAIL checkpoint accepted")
except SystemExit as e:
    results.append(dict(case="checkpoint offered as the state", expect_open=True, agreement=None, status=f"REFUSED: {e}"[:300], pass_=True)); print("PASS checkpoint offered as the state -> REFUSED")
# 20b. the state's saved tensor omega displaced by 5 ULP relative to the map (simulated): refused by the 2-ULP rule
st = dict(ia); st["tensor_vs_map_ulps"] = [0.0, 5.0]; case("state tensor omega 5 ULP from the map", True, st_a=st, reason_substr="not within 2 ULP")
# 20c. the state's optimizer coordinates displaced by one ULP (simulated): refused (checkpoint/EVAL bindings are bitwise)
st = dict(ia); st["z_opt_params"] = [ia["z_opt_params"][0], float(np.nextafter(ia["z_opt_params"][1], 1.0))]; case("state z_w + 1 ULP", True, st_a=st, reason_substr="optimizer coordinates")
# 20d. endpoint mapping not established (simulated): refused
st = dict(ia); mp = dict(ia["endpoint_mapping"]); mp["checked"] = False; mp["problems"] = ["simulated"]; st["endpoint_mapping"] = mp; case("checkpoint-to-endpoint mapping not established", True, st_a=st, reason_substr="mapping not established")
# 21. state cost displaced
st = dict(ia); st["state_cost_final"] = st["state_cost_final"] * (1 + 1e-15); case("state cost x (1 + 1e-15)", True, st_a=st, reason_substr="exactly")
n_pass = sum(1 for r in results if r["pass_"]); out = dict(kind="branch_distance v7 controls", tool_sha256=bd.sha(os.path.join(ROOT, "scripts", "branch_distance.py")), tool_version=bd.VERSION, baseline=dict(a=A, b=B, sens=SENS, npz=NPZ),
                                                          a_endpoint_mapping=ia["endpoint_mapping"], a_tensor_vs_map_ulps=ia.get("tensor_vs_map_ulps"), b_tensor_vs_map_ulps=ib.get("tensor_vs_map_ulps"), b_endpoint_mapping=ib["endpoint_mapping"], n_cases=len(results), n_pass=n_pass, all_pass=(n_pass == len(results)), cases=results, seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
op = os.path.join(ROOT, "validation", "branch_distance", f"controls_v7_{time.strftime('%H%M%S', time.gmtime())}.json"); json.dump(out, open(op, "w"), indent=1, default=str)
for d_ in [p for p in os.listdir(os.path.join(ROOT, "validation", "branch_distance")) if p.startswith("bdctrl_")]:
    shutil.rmtree(os.path.join(ROOT, "validation", "branch_distance", d_), ignore_errors=True)
print(f"{n_pass}/{len(results)} controls pass; {out['seconds']:.0f} s; {op} {bd.sha(op)[:16]}")
