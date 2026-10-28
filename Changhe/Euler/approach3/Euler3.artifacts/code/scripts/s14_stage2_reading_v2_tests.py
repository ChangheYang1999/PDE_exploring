#!/usr/bin/env python
"""Negative tests of the factored check functions of scripts/s14_stage2_reading_v2.py (lead d128 KO item 5). Each case must raise Precondition or return an
OPEN / unbound verdict; the script prints PASS / FAIL per case and exits non-zero if any case fails. Run after the positive --smoke run; output is saved
beside v2 by the caller. Usage: .venv/bin/python scripts/s14_stage2_reading_v2_tests.py"""
import sys, os, json, math, tempfile, types
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import s14_stage2_reading_v2 as M
NAN = float("nan")
L4 = dict(N_core=1.5, N_F=1.2, e_core=0.9, e_F=0.8, rho_u_max_holdout=0.31, rho_u_max_holdout_half=0.30)
L6 = dict(N_core=1.4, N_F=1.1, e_core=0.85, e_F=0.7, rho_u_max_holdout=0.2, rho_u_max_holdout_half=0.21)
REG_T = dict(L=6, Nk=16, Nr=48, m_parity="all", channels=dict(NkB=4, NkD=4, NkE=4, LB=15, LD=14, LE=6, core_damp=2), closure_lambda=1e-3, nl_denominator="all5far", max_iter=300, time_limit_per_start=7200.0, c_l=0.45, omega=1.0)
REG_C = dict(REG_T, m_parity="even", max_iter=600)
results = []
def case(name, fn, expect):
    """expect: 'raise' (Precondition) or a predicate on the return value"""
    try:
        out = fn()
        if expect == "raise":
            results.append((name, False, f"returned {out!r} instead of raising")); return
        ok = expect(out)
        results.append((name, bool(ok), f"returned {json.dumps(M.sanitize(out), default=str)[:160]}"))
    except M.Precondition as e:
        results.append((name, expect == "raise", f"Precondition: {str(e)[:160]}"))
    except Exception as e:
        results.append((name, False, f"UNEXPECTED {type(e).__name__}: {str(e)[:160]}"))
is_open = lambda d: d["collapsing"] is None and d["warning"] is None and d["verdict"].startswith("OPEN")
# control: the positive collapse case must NOT be open
case("control: finite inputs -> a verdict (not collapsing)", lambda: M.collapse_check(L4, L6), lambda d: d["verdict"] == "not collapsing" and d["collapsing"] is False)
case("control: a 3x fall is collapsing", lambda: M.collapse_check(L4, dict(L6, e_F=0.2)), lambda d: d["collapsing"] is True and d["verdict"].startswith("collapsing"))
case("missing guard (L6 e_F absent)", lambda: M.collapse_check(L4, {k: v for k, v in L6.items() if k != "e_F"}), is_open)
case("NaN guard (L6 N_core NaN)", lambda: M.collapse_check(L4, dict(L6, N_core=NAN)), is_open)
case("zero L4 guard (L4 e_core 0)", lambda: M.collapse_check(dict(L4, e_core=0.0), L6), is_open)
case("negative L4 guard", lambda: M.collapse_check(dict(L4, N_F=-1.0), L6), is_open)
case("string guard (TypeError path)", lambda: M.collapse_check(L4, dict(L6, e_F="0.7")), is_open)
case("NaN holdout (std)", lambda: M.holdout_values(dict(L6, rho_u_max_holdout=NAN)), lambda d: d["std"] is None and d["open"] and "rho_u_max_holdout" in d["open"])
case("missing half holdout", lambda: M.holdout_values({k: v for k, v in L6.items() if k != "rho_u_max_holdout_half"}), lambda d: d["half"] is None and d["open"] and "rho_u_max_holdout_half" in d["open"])
case("infinite holdout", lambda: M.holdout_values(dict(L6, rho_u_max_holdout=float("inf"))), lambda d: d["std"] is None and bool(d["open"]))
case("comparator at another point", lambda: M.check_comparator_id(0.45, 1.0, "nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0"), "raise")
case("comparator missing where mandatory", lambda: M.check_comparator_id(0.42, 0.3, None), "raise")
case("comparator given at the coverage-only point", lambda: M.check_comparator_id(0.48, 1.0, "nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0"), "raise")
case("unregistered point", lambda: M.check_comparator_id(0.47, 1.0, None), "raise")
case("control: registered comparator accepted", lambda: M.check_comparator_id(0.45, 0.3, "nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0"), lambda v: v == "nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0")
case("comparator with another representation (channel degrees 11/10/4)", lambda: M.check_cfg_registered(dict(REG_C, channels=dict(NkB=4, NkD=4, NkE=4, LB=11, LD=10, LE=4)), M.REG_COMPARATOR, "comparator"), "raise")
case("comparator with all-m parity", lambda: M.check_cfg_registered(dict(REG_C, m_parity="all"), M.REG_COMPARATOR, "comparator"), "raise")
case("comparator with closure 0.1", lambda: M.check_cfg_registered(dict(REG_C, closure_lambda=0.1), M.REG_COMPARATOR, "comparator"), "raise")
case("target with Nk 20", lambda: M.check_cfg_registered(dict(REG_T, Nk=20), M.REG_TARGET, "target"), "raise")
case("target with max_iter 150", lambda: M.check_cfg_registered(dict(REG_T, max_iter=150), M.REG_TARGET, "target"), "raise")
case("control: registered target configuration accepted", lambda: M.check_cfg_registered(REG_T, M.REG_TARGET, "target"), lambda v: v == "registered configuration")
case("unregistered target id", lambda: M.check_target_registered("s14b_L6_cl0.45_om+1.0_fixed_p1_om+1.0s6"), "raise")
case("control: registered target id", lambda: M.check_target_registered("s14b_L6_cl0.45_om+1.0_fixed_p0_om+1.0s5"), lambda v: v == "registered")
case("source at another point", lambda: M.check_source(dict(L=4, m_parity="all", c_l=0.42, omega=0.3), dict(c_l=0.45, omega=0.3)), "raise")
case("source with even parity (non-smoke)", lambda: M.check_source(dict(L=4, m_parity="even", c_l=0.45, omega=1.0), dict(c_l=0.45, omega=1.0)), "raise")
case("source at L6", lambda: M.check_source(dict(L=6, m_parity="all", c_l=0.45, omega=1.0), dict(c_l=0.45, omega=1.0)), "raise")
def failing_runner(cmd):
    return types.SimpleNamespace(returncode=1, stdout="", stderr="simulated order_73b failure")
case("failing order call (rc 1)", lambda: M.run_order("s14b_L6_cl0.45_om+1.0_fixed_p0_om+1.0s5", "nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0", runner=failing_runner), "raise")
def silent_runner(cmd):
    return types.SimpleNamespace(returncode=0, stdout="", stderr="")   # rc 0 but no JSON written
case("order call that writes no JSON", lambda: M.run_order("s14b_L6_cl0.45_om+1.0_fixed_p0_om+1.0s5", "nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0", runner=silent_runner), "raise")
def existing_arm_reading():
    fn = os.path.join(ROOT, "reports", "arm_reading_TESTONLY_s14_stage2_v2.json")
    open(fn, "w").write("{}")
    try:
        return M.precondition_no_arm_reading("TESTONLY_s14_stage2_v2")
    finally:
        os.remove(fn)
case("existing target arm_reading JSON", existing_arm_reading, "raise")
case("control: absent target arm_reading JSON passes", lambda: M.precondition_no_arm_reading("TESTONLY_absent_s14_stage2_v2"), lambda v: v.endswith("arm_reading_TESTONLY_absent_s14_stage2_v2.json"))
def unbound_oddm():
    d = tempfile.mkdtemp(); fn = os.path.join(d, "oddm.json")
    json.dump(dict(start="runs/other/starts/start_000.pt", L=6, Nk=16, m_parity="all", c_l=0.45, omega=1.0, energy_fraction_odd=dict(all=0.5, core_r_lt_0p125=0.5, tail_r_ge_8=0.5), ratio_all=dict(U=0.7, Omega=0.7, DU=0.7), coef_norm_fraction_odd=0.6), open(fn, "w"))
    return M.bind_oddm(fn, "runs/this/starts/start_000.pt", dict(L=6, Nk=16, m_parity="all", c_l=0.45, omega=1.0))
case("odd-m file bound to another start", unbound_oddm, lambda d: d["bound"] is False and d["reason"].startswith("unbound"))
def wrong_cfg_oddm():
    d = tempfile.mkdtemp(); fn = os.path.join(d, "oddm.json")
    json.dump(dict(start="runs/this/starts/start_000.pt", L=4, Nk=12, m_parity="all", c_l=0.45, omega=1.0, energy_fraction_odd=dict(all=0.5, core_r_lt_0p125=0.5, tail_r_ge_8=0.5), ratio_all=dict(U=0.7, Omega=0.7, DU=0.7), coef_norm_fraction_odd=0.6), open(fn, "w"))
    return M.bind_oddm(fn, "runs/this/starts/start_000.pt", dict(L=6, Nk=16, m_parity="all", c_l=0.45, omega=1.0))
case("odd-m file with another L / Nk", wrong_cfg_oddm, lambda d: d["bound"] is False)
case("odd-m file missing", lambda: M.bind_oddm("/nonexistent/oddm.json", "runs/this/starts/start_000.pt", dict(L=6, Nk=16, m_parity="all", c_l=0.45, omega=1.0)), lambda d: d["bound"] is False and d["reason"] == "missing")
case("sanitize writes non-finite as null", lambda: M.sanitize(dict(a=NAN, b=[1.0, float("inf")], c=dict(d=2.0))), lambda d: d["a"] is None and d["b"][1] is None and d["c"]["d"] == 2.0)
case("--smoke with another (registered) job id", lambda: M.check_target_registered("s14b_L6_cl0.45_om+1.0_fixed_p0_om+1.0s5", smoke=True), "raise")
case("control: --smoke with the registered smoke target", lambda: M.check_target_registered(M.SMOKE_TARGET, smoke=True), lambda v: v.startswith("SMOKE"))
case("relaxation record: target max_iter 600 under smoke", lambda: (lambda rl: (M.check_cfg_registered(dict(REG_T, m_parity="even", max_iter=600), M.REG_TARGET, "target", relax=("m_parity", "max_iter"), relaxations=rl), rl)[1])([]), lambda rl: [r[0] for r in rl] == ["target m_parity", "target max_iter"] and rl[1][1] == 300 and rl[1][2] == 600)
case("time limit is NOT relaxed under smoke", lambda: M.check_cfg_registered(dict(REG_T, m_parity="even", max_iter=600, time_limit_per_start=3600.0), M.REG_TARGET, "target", relax=("m_parity", "max_iter"), relaxations=[]), "raise")
import subprocess
def run_cli(args):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "s14_stage2_reading_v2.py")] + args, cwd=ROOT, env=dict(os.environ, CUDA_VISIBLE_DEVICES="-1"), capture_output=True, text=True)
    return dict(rc=r.returncode, out=(r.stdout + r.stderr).strip().splitlines()[-1][:200] if (r.stdout + r.stderr).strip() else "")
case("CLI: --smoke with another job id exits 2", lambda: run_cli(["s14b_L6_cl0.45_om+1.0_fixed_p0_om+1.0s5", "--comparator", M.SMOKE_COMPARATOR, "--smoke"]), lambda d: d["rc"] == 2 and "PRECONDITION FAILED" in d["out"])
case("CLI: the smoke target without --smoke exits 2", lambda: run_cli([M.SMOKE_TARGET, "--comparator", M.SMOKE_COMPARATOR]), lambda d: d["rc"] == 2 and "PRECONDITION FAILED" in d["out"])
case("CLI: --smoke against another comparator exits 2", lambda: run_cli([M.SMOKE_TARGET, "--comparator", "nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0", "--smoke"]), lambda d: d["rc"] == 2 and "PRECONDITION FAILED" in d["out"])
bad = [r for r in results if not r[1]]
for name, ok, msg in results:
    print(f"{'PASS' if ok else 'FAIL'} | {name} | {msg}")
print(f"{len(results) - len(bad)} passed, {len(bad)} failed")
sys.exit(1 if bad else 0)
