#!/usr/bin/env python
"""S14 stage (ii) reading, v2 (lead d128 KO, 2026-10-26T23:27:38Z; replaces s14_stage2_reading.py bbdf8c93, which was not accepted).
For ONE finished registered S14 stage (ii) job (L6 all-m promotion of a stage (i) L4 start; reports/S14_ENQUEUE_20261026.md) it reports, fail-closed:
 (1) the end state's holdout rho_u^max on both shell families, V10, LM status / iterations / seconds, whole-job seconds (stdout.log START and JOB DONE stamps);
 (2) the S14R-1 collapse check: N_core, N_F, e_core, e_F of the L6 end state against the L4 promoted start (its results.jsonl row, found through init_from),
     ratios L6 / L4 and the SPEC 7.4 flags ('collapsing' = any ratio below 0.5; 'warning' = any L6 value below its guard N 1e-2 / e 1e-4); every L4 value must
     be finite and positive and every L6 value finite, else the verdict is 'OPEN (missing or non-finite: names)' and the JSON flags are null (never 'not collapsing');
 (3) the odd-m content of the L6 end state and of the L4 start from reports/oddm/*.json (scripts/odd_m_fraction.py), each file bound to its state through the
     'start' path and the L / Nk / m_parity / c_l / omega fields (unbound or missing: OPEN);
 (4) the even-class L6 comparator (mandatory at the three comparator points and fixed to the registered nest6 p0 job; its arm_reading JSON must already exist
     and is not regenerated: its sha256 and code versions are recorded; (0.48, 1) is coverage-only and takes no comparator): the holdout on both families, the
     ratios, and the SPEC 7.3b relation through scripts/order_73b.py bound to THIS call (the target's arm_reading JSON must not exist before the call; any earlier
     order JSON for the pair is deleted; the return code is checked; the single pair is read from the order JSON written by the call; shas recorded), printed with
     max_iter, the time limit, the iterations run and the stop status of both states and the sentence on the shared quadrature / core-resolution condition.
Preconditions (exit code 2 on failure): the target is one of the four registered s14b jobs with the full registered configuration (L 6, Nk 16, Nr 48, all-m,
channels NkB/NkD/NkE 4 at degrees 15/14/6, closure rows 1e-3, all5far, max_iter 300, time limit 7200 s); the source is an L4 all-m start at the same c_l and
omega; the comparator (where required) has the registered id and the same representation with even parity and max_iter 600. --smoke (lead KQ) is accepted ONLY for the
target nest6_L6_cl0.45_om+1.0_fixed_p1_om+1.0s31s0 (an L4 -> L6 lineage) against nest6 p0 s43s0 and relaxes EXACTLY four checks: registered-set membership, target m_parity (even), target
max_iter (600), source m_parity (even); every other check is unchanged; each relaxation is printed as a SMOKE line with the registered and the found value and listed by name in the JSON. Non-finite numbers are written as null in the JSON. CPU only; reads saved files; makes no promotion decision.
Usage: .venv/bin/python scripts/s14_stage2_reading_v2.py <job_id> [--comparator <job_id>] [--json] [--smoke]"""
import sys, os, json, re, math, hashlib, subprocess, argparse, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PY = os.path.join(ROOT, ".venv", "bin", "python")
REGISTERED_TARGETS = ["s14b_L6_cl0.45_om+0.3_fixed_p0_om+0.3s6", "s14b_L6_cl0.45_om+1.0_fixed_p0_om+1.0s5", "s14b_L6_cl0.42_om+0.3_fixed_p0_om+0.3s5", "s14b_L6_cl0.48_om+1.0_fixed_p0_om+1.0s7"]
COMPARATOR_AT = {(0.45, 0.3): "nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0", (0.45, 1.0): "nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0", (0.42, 0.3): "nest6_L6_cl0.42_om+0.3_fixed_p0_om+0.3s12s0", (0.48, 1.0): None}
REG_TARGET = dict(L=6, Nk=16, Nr=48, m_parity="all", channels=dict(NkB=4, NkD=4, NkE=4, LB=15, LD=14, LE=6), closure_lambda=1e-3, nl_denominator="all5far", max_iter=300, time_limit_per_start=7200.0)
REG_COMPARATOR = dict(REG_TARGET, m_parity="even", max_iter=600)
GUARDS = dict(N_core=1e-2, N_F=1e-2, e_core=1e-4, e_F=1e-4)
SMOKE_TARGET = "nest6_L6_cl0.45_om+1.0_fixed_p1_om+1.0s31s0"; SMOKE_COMPARATOR = "nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0"   # lead KQ: --smoke is accepted for this pair only
SMOKE_RELAXED = ("registered-set membership", "target m_parity (even)", "target max_iter (600)", "source m_parity (even)")   # exactly these four checks (lead KQ item 2)
QUADRATURE_SENTENCE = "same degree 6, Nk 16, Nr 48: same holdout quadrature; conditional on verified core resolution (core flags primary-reported)"


class Precondition(Exception):
    pass


def finite(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def sanitize(o):
    """non-finite floats -> None, recursively (JSON null)"""
    if isinstance(o, float):
        return o if math.isfinite(o) else None
    if isinstance(o, dict):
        return {k: sanitize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sanitize(v) for v in o]
    return o


def sha256_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def ts(s):
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


def check_target_registered(job, smoke=False):
    """production: one of the four registered s14b jobs; --smoke: ONLY the registered smoke target (lead KQ item 1), relaxing the registered-set check"""
    if smoke:
        if job != SMOKE_TARGET:
            raise Precondition(f"--smoke is accepted only for the target {SMOKE_TARGET}; got {job}")
        return "SMOKE: registered-set membership relaxed (registered: one of the four s14b jobs; found: the registered smoke target)"
    if job not in REGISTERED_TARGETS:
        raise Precondition(f"target {job} is not one of the four registered S14 stage (ii) jobs")
    return "registered"


def check_cfg_registered(cfg, reg, label, relax=(), relaxations=None):
    """compare a job configuration with a registered one; raises Precondition listing every mismatch. relax = keys whose mismatch is tolerated (--smoke only:
    the target's m_parity and max_iter, lead KQ item 2); each tolerated mismatch is appended to relaxations as (check, registered, found)."""
    bad = []
    for k, v in reg.items():
        if k in relax:
            if cfg.get(k) != v and relaxations is not None:
                relaxations.append((f"{label} {k}", v, cfg.get(k)))
            continue
        if k == "channels":
            ch = cfg.get("channels") or {}
            for ck, cv in v.items():
                if ch.get(ck) != cv:
                    bad.append(f"channels.{ck}={ch.get(ck)!r} (registered {cv!r})")
        else:
            got = cfg.get(k)
            if isinstance(v, float):
                ok = finite(got) and abs(float(got) - v) <= 1e-12 * max(1.0, abs(v))
            else:
                ok = (got == v)
            if not ok:
                bad.append(f"{k}={got!r} (registered {v!r})")
    if bad:
        raise Precondition(f"{label}: configuration differs from the registered one: " + "; ".join(bad))
    return "registered configuration"


def check_source(l4cfg, cfg, smoke=False, relaxations=None):
    """the promoted start must be an L4 all-m start at the same c_l and omega; --smoke relaxes the source parity only (lead KQ item 2)"""
    bad = []
    if l4cfg.get("L") != 4:
        bad.append(f"source L={l4cfg.get('L')!r} (expected 4)")
    if l4cfg.get("m_parity") != "all":
        if smoke:
            if relaxations is not None:
                relaxations.append(("source m_parity", "all", l4cfg.get("m_parity")))
        else:
            bad.append(f"source m_parity={l4cfg.get('m_parity')!r} (expected 'all')")
    for k in ("c_l", "omega"):
        if not (finite(l4cfg.get(k)) and finite(cfg.get(k)) and abs(float(l4cfg[k]) - float(cfg[k])) <= 1e-12):
            bad.append(f"source {k}={l4cfg.get(k)!r} differs from the target's {cfg.get(k)!r}")
    if bad:
        raise Precondition("source start: " + "; ".join(bad))
    return "L4 source at the same point" + (" (SMOKE: parity relaxed)" if smoke else "")


def check_comparator_id(c_l, omega, comparator):
    """the comparator is mandatory and fixed at the three comparator points; none is allowed at (0.48, 1)"""
    key = next((k for k in COMPARATOR_AT if abs(k[0] - float(c_l)) <= 1e-12 and abs(k[1] - float(omega)) <= 1e-12), None)
    if key is None:
        raise Precondition(f"(c_l, omega) = ({c_l}, {omega}) is not a registered S14 point")
    reg = COMPARATOR_AT[key]
    if reg is None:
        if comparator is not None:
            raise Precondition(f"no even-class L6 comparator is registered at ({c_l}, {omega}); --comparator must be absent (coverage reading only)")
        return None
    if comparator is None:
        raise Precondition(f"--comparator is mandatory at ({c_l}, {omega}); the registered comparator is {reg}")
    if comparator != reg:
        raise Precondition(f"comparator {comparator} is not the registered comparator {reg} at ({c_l}, {omega})")
    return reg


def collapse_check(l4row, l6row):
    """S14R-1: ratios L6 / L4 of the four SPEC 7.4 quantities; fail-closed"""
    vals = {}; missing = []
    for n in GUARDS:
        v4, v6 = l4row.get(n), l6row.get(n)
        ok4 = finite(v4) and v4 > 0; ok6 = finite(v6)
        if not ok4:
            missing.append(f"L4 {n}" + ("" if v4 is None else f" ({v4!r})"))
        if not ok6:
            missing.append(f"L6 {n}" + ("" if v6 is None else f" ({v6!r})"))
        ratio = (v6 / v4) if (ok4 and ok6) else None
        vals[n] = dict(L4=(v4 if finite(v4) else None), L6=(v6 if finite(v6) else None), ratio_L6_over_L4=ratio, collapsing=((ratio < 0.5) if ratio is not None else None), warning=((v6 < GUARDS[n]) if ok6 else None))
    if missing:
        return dict(values=vals, collapsing=None, warning=None, verdict="OPEN (missing or non-finite: " + ", ".join(missing) + ")")
    coll = any(c["collapsing"] for c in vals.values()); warn = any(c["warning"] for c in vals.values())
    return dict(values=vals, collapsing=coll, warning=warn, verdict=("collapsing" if coll else "not collapsing") + ("; warning (below a guard value)" if warn else ""))


def holdout_values(row):
    """both shell families, fail-closed"""
    std, half = row.get("rho_u_max_holdout"), row.get("rho_u_max_holdout_half")
    missing = [n for n, v in (("rho_u_max_holdout", std), ("rho_u_max_holdout_half", half)) if not finite(v)]
    return dict(std=(std if finite(std) else None), half=(half if finite(half) else None), open=("OPEN (missing or non-finite: " + ", ".join(missing) + ")") if missing else None)


def bind_oddm(path, zfile, cfg):
    """an odd-m JSON counts only if its start path and L / Nk / m_parity / c_l / omega equal the state's"""
    if not os.path.exists(path):
        return dict(path=path, bound=False, reason="missing", values=None)
    od = json.load(open(path))
    bad = []
    if os.path.abspath(os.path.join(ROOT, od.get("start", ""))) != os.path.abspath(os.path.join(ROOT, zfile)):
        bad.append(f"start {od.get('start')!r} is not {zfile!r}")
    for k in ("L", "Nk", "m_parity"):
        if od.get(k) != cfg.get(k):
            bad.append(f"{k} {od.get(k)!r} != {cfg.get(k)!r}")
    for k in ("c_l", "omega"):
        if not (finite(od.get(k)) and finite(cfg.get(k)) and abs(float(od[k]) - float(cfg[k])) <= 1e-12):
            bad.append(f"{k} {od.get(k)!r} != {cfg.get(k)!r}")
    if bad:
        return dict(path=path, bound=False, reason="unbound: " + "; ".join(bad), values=None)
    e = od.get("energy_fraction_odd") or {}; r = od.get("ratio_all") or {}
    vals = dict(energy_all=e.get("all"), energy_core=e.get("core_r_lt_0p125"), energy_tail=e.get("tail_r_ge_8"), amp_U=r.get("U"), amp_Omega=r.get("Omega"), amp_DU=r.get("DU"), coef_norm_fraction=od.get("coef_norm_fraction_odd"))
    nf = [k for k, v in vals.items() if not finite(v)]
    return dict(path=path, sha256=sha256_file(path), bound=(not nf), reason=("non-finite: " + ", ".join(nf)) if nf else "bound", values=sanitize(vals))


def precondition_no_arm_reading(job):
    fn = os.path.join(ROOT, "reports", f"arm_reading_{job}.json")
    if os.path.exists(fn):
        raise Precondition(f"the target's arm_reading JSON {fn} exists before the call; the ordering must be bound to this call (move it away first)")
    return fn


def run_order(job, comparator, runner=None):
    """SPEC 7.3b relation bound to this call: delete any earlier order JSON for the pair, run order_73b.py, check rc, read the single pair"""
    out = os.path.join(ROOT, "reports", f"order_73b_{job}__vs__{comparator}.json")
    if os.path.exists(out):
        os.remove(out)
    cmd = [PY, os.path.join(ROOT, "scripts", "order_73b.py"), job, comparator, "--json", out]
    res = (runner or (lambda c: subprocess.run(c, cwd=ROOT, env=dict(os.environ, CUDA_VISIBLE_DEVICES="-1"), capture_output=True, text=True)))(cmd)
    if res.returncode != 0:
        raise Precondition(f"order_73b.py failed with return code {res.returncode}: {(res.stderr or res.stdout)[-400:]}")
    if not os.path.exists(out):
        raise Precondition(f"order_73b.py wrote no JSON at {out}")
    oj = json.load(open(out))
    pairs = [p for p in oj.get("pairs", []) if p.get("X") == job and p.get("Y") == comparator]
    if len(pairs) != 1 or len(oj.get("pairs", [])) != 1:
        raise Precondition(f"the order JSON must hold exactly the single pair ({job}, {comparator}); found {len(oj.get('pairs', []))} pairs")
    p = pairs[0]
    rat = p.get("ratios")
    if rat is None or len(rat) != 5 or not all(finite(v) for v in rat) or p.get("relation") == "?":
        rel = dict(relation="OPEN (missing or non-finite 7.3b field, or core unresolved)", words=p.get("words"), ratios=sanitize(rat) if rat else None)
    else:
        rel = dict(relation=p["relation"], words=p["words"], ratios=rat)
    return dict(order_json=out, order_json_sha256=sha256_file(out), command=" ".join(cmd), returncode=res.returncode, pair=rel, stdout_table=[l for l in res.stdout.splitlines() if l.startswith("| ")], tool_sha256=sha256_file(os.path.join(ROOT, "scripts", "order_73b.py")))


def load_cfg_from_queue(job):
    for d in ("done", "running", "pending", "failed", "cancelled", "hold", "hold_lowprio"):
        p = os.path.join(ROOT, "queue", d, job + ".json")
        if os.path.exists(p):
            return json.load(open(p)).get("config", {}), p
    raise Precondition(f"no queue file for {job}")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("job"); ap.add_argument("--comparator", default=None); ap.add_argument("--json", action="store_true"); ap.add_argument("--smoke", action="store_true"); a = ap.parse_args()
    P = "SMOKE " if a.smoke else ""
    job = a.job; rdir = os.path.join(ROOT, "runs", job); relaxations = []
    try:
        reg = check_target_registered(job, a.smoke)
        if a.smoke:
            relaxations.append(("registered-set membership", "one of " + ", ".join(REGISTERED_TARGETS), job))
            if a.comparator != SMOKE_COMPARATOR:
                raise Precondition(f"--smoke is accepted only against the comparator {SMOKE_COMPARATOR}; got {a.comparator}")
        for fn in (os.path.join(rdir, "stdout.log"), os.path.join(rdir, "results.jsonl")):
            if not os.path.exists(fn):
                raise Precondition(f"missing file {fn}: the job is not finished or does not exist")
        log = open(os.path.join(rdir, "stdout.log")).read().splitlines()
        start_line = next((l for l in log if " START job " in l), None)
        if start_line is None:
            raise Precondition("no START line in stdout.log")
        cfg = json.loads(re.search(r"cfg=(\{.*\})\s*$", start_line).group(1))
        check_cfg_registered(cfg, REG_TARGET, "target", relax=(("m_parity", "max_iter") if a.smoke else ()), relaxations=relaxations)
        rows = [json.loads(l) for l in open(os.path.join(rdir, "results.jsonl")) if l.strip()]
        rows = [r for r in rows if r.get("kind") == "start_result"]
        if len(rows) != 1:
            raise Precondition(f"expected exactly one start_result row, found {len(rows)}")
        r = rows[0]
        if r.get("failure"):
            raise Precondition(f"the target row carries a failure flag: {r.get('failure')!r}")
        done_line = next((l for l in log if "JOB DONE" in l), None)
        if done_line is None:
            raise Precondition("no JOB DONE line: the job is not finished")
        t0, t1 = ts(start_line[:20]), ts(done_line[:20]); whole = (t1 - t0).total_seconds()
        src = cfg.get("init_from") or ""
        m = re.search(r"runs/([^/]+)/starts/start_(\d+)\.pt$", src)
        if not m:
            raise Precondition(f"init_from {src!r} is not a runs/<job>/starts/start_NNN.pt path")
        l4_job, l4_k = m.group(1), int(m.group(2))
        for fn in (os.path.join(ROOT, "runs", l4_job, "stdout.log"), os.path.join(ROOT, "runs", l4_job, "results.jsonl")):
            if not os.path.exists(fn):
                raise Precondition(f"missing source file {fn}")
        l4_log = open(os.path.join(ROOT, "runs", l4_job, "stdout.log")).read().splitlines()
        l4_start = next((l for l in l4_log if " START job " in l), None)
        if l4_start is None:
            raise Precondition(f"no START line for the source job {l4_job}")
        l4cfg = json.loads(re.search(r"cfg=(\{.*\})\s*$", l4_start).group(1))
        check_source(l4cfg, cfg, a.smoke, relaxations)
        l4rows = [json.loads(l) for l in open(os.path.join(ROOT, "runs", l4_job, "results.jsonl")) if l.strip()]
        l4 = [x for x in l4rows if x.get("kind") == "start_result" and x.get("start") == l4_k]
        if len(l4) != 1:
            raise Precondition(f"source start {l4_k} of {l4_job}: {len(l4)} result rows")
        l4 = l4[0]
        if os.path.abspath(os.path.join(ROOT, l4.get("zfile", ""))) != os.path.abspath(src):
            raise Precondition(f"the source row's zfile {l4.get('zfile')!r} is not init_from {src!r}")
        comparator = check_comparator_id(cfg["c_l"], cfg["omega"], a.comparator)
        comp = None
        if comparator is not None:
            ccfg, cqueue = load_cfg_from_queue(comparator)
            check_cfg_registered(ccfg, REG_COMPARATOR, "comparator")
            cfn = os.path.join(ROOT, "reports", f"arm_reading_{comparator}.json")
            if not os.path.exists(cfn):
                raise Precondition(f"the comparator's arm_reading JSON {cfn} does not exist; it is not generated by this tool")
            csha_before = sha256_file(cfn); crow = json.load(open(cfn)).get("row", {})
            precondition_no_arm_reading(job)
            order = run_order(job, comparator)
            csha_after = sha256_file(cfn)
            if csha_after != csha_before:
                raise Precondition("the comparator's arm_reading JSON changed during the call")
            tfn = os.path.join(ROOT, "reports", f"arm_reading_{job}.json")
            ch = holdout_values(crow)
            comp = dict(comparator=comparator, queue_file=cqueue, arm_reading_json=cfn, arm_reading_sha256=csha_before, code_versions=sanitize(crow.get("code_versions")), holdout=ch,
                        max_iter=ccfg.get("max_iter"), time_limit_per_start=ccfg.get("time_limit_per_start"), iterations=crow.get("iterations"), status=crow.get("status"),
                        target_arm_reading_json=tfn, target_arm_reading_sha256=(sha256_file(tfn) if os.path.exists(tfn) else None), order=order, quadrature_sentence=QUADRATURE_SENTENCE)
            hv = holdout_values(r)
            comp["ratio_std"] = (hv["std"] / ch["std"]) if (hv["std"] is not None and ch["std"] not in (None, 0)) else None
            comp["ratio_half"] = (hv["half"] / ch["half"]) if (hv["half"] is not None and ch["half"] not in (None, 0)) else None
    except Precondition as e:
        print(f"{P}PRECONDITION FAILED: {e}"); sys.exit(2)
    hv = holdout_values(r); l4hv = holdout_values(l4)
    coll = collapse_check(l4, r)
    od6 = bind_oddm(os.path.join(ROOT, "reports", "oddm", f"oddm_{job}_0.json"), r.get("zfile", ""), cfg)
    od4 = bind_oddm(os.path.join(ROOT, "reports", "oddm", f"oddm_{l4_job}_{l4_k}.json"), l4.get("zfile", ""), l4cfg)
    cv = r.get("code_versions") or {}
    ch = cfg.get("channels") or {}
    res = dict(tool="s14_stage2_reading_v2.py", tool_sha256=sha256_file(os.path.abspath(__file__)), smoke=a.smoke, smoke_relaxed_checks=([dict(check=c, registered=r_, found=f_) for c, r_, f_ in relaxations] if a.smoke else []), job=job, registered=reg, c_l=cfg["c_l"], omega=cfg["omega"],
               config=dict(L=cfg["L"], Nk=cfg["Nk"], Nr=cfg["Nr"], m_parity=cfg["m_parity"], channels=ch, closure_lambda=cfg.get("closure_lambda"), nl_denominator=cfg.get("nl_denominator"), max_iter=cfg.get("max_iter"), time_limit_per_start=cfg.get("time_limit_per_start"), chunk=cfg.get("chunk")),
               init_from=src, source=dict(job=l4_job, start=l4_k, family=l4.get("family"), rng_seed=l4.get("rng_seed"), L=l4cfg.get("L"), Nk=l4cfg.get("Nk"), m_parity=l4cfg.get("m_parity"), holdout=l4hv, status=l4.get("status"), iterations=l4.get("iterations"), max_iter=l4cfg.get("max_iter"), time_limit_per_start=l4cfg.get("time_limit_per_start")),
               status=r.get("status"), iterations=r.get("iterations"), lm_seconds=r.get("seconds"), job_start=t0.strftime("%Y-%m-%dT%H:%M:%SZ"), job_done=t1.strftime("%Y-%m-%dT%H:%M:%SZ"), whole_job_seconds=whole,
               holdout=hv, v10=r.get("v10_last_tenth_rel_decrease"), rms_mom=r.get("rms_mom"), cost_final=r.get("cost_final"), rho_nl_max_holdout=r.get("rho_nl_max_holdout"), max_U=r.get("max_U"), max_abs_Omega=r.get("max_abs_Omega"),
               core_resolved=r.get("core_resolved"), a_max_core=r.get("a_max_core"), sigma_u_max_core=r.get("sigma_u_max_core"), sigma_Om=r.get("sigma_Om"), a_eff=r.get("a_eff"), E_ren=r.get("E_ren"), H_tot_over_abs=r.get("H_tot_over_abs"),
               K_E_ratio=r.get("K_ratio_direct"), K_H_ratio=r.get("K_H_ratio_direct"), G_carried_mismatch_rel=r.get("G_carried_mismatch_rel"), Q_sw=r.get("Q_sw"), tau_F_R8=r.get("tau_F_R8"), rotation_content_rel=r.get("rotation_content_rel"),
               collapse_check=dict(coll, rule="SPEC 7.4: warning if N_core < 1e-2, N_F < 1e-2, e_core < 1e-4 or e_F < 1e-4; collapsing if any of the four decreases by more than 2x per refinement level (L4 -> L6); OPEN if any input is missing or non-finite or an L4 value is not positive"),
               odd_m_L6=od6, odd_m_L4=od4, comparator=comp, code_versions={k: (v.get("sha256_12") if isinstance(v, dict) else v) for k, v in cv.items()} if isinstance(cv, dict) else cv)
    res = sanitize(res)
    def f(v, fmt="%.4f"):
        return (fmt % v) if finite(v) else "n/a"
    for c, r_, f_ in relaxations:
        print(f"{P}relaxed check: {c}: registered {r_!r}, found {f_!r}")
    print(f"{P}# S14 stage (ii) reading v2: {job} ({reg}; c_l {cfg['c_l']}, omega {cfg['omega']}; L {cfg['L']} Nk {cfg['Nk']} Nr {cfg['Nr']} {cfg['m_parity']} basis, channels {ch.get('NkB')}/{ch.get('NkD')}/{ch.get('NkE')} at degrees {ch.get('LB')}/{ch.get('LD')}/{ch.get('LE')}, closure {cfg.get('closure_lambda')}, {cfg.get('nl_denominator')}, max_iter {cfg.get('max_iter')}, time limit {cfg.get('time_limit_per_start')} s)")
    print(f"{P}SOURCE: {l4_job} start {l4_k} ({l4.get('family')}, seed {l4.get('rng_seed')}; L {l4cfg.get('L')} Nk {l4cfg.get('Nk')} {l4cfg.get('m_parity')}; {l4.get('status')} after {l4.get('iterations')} iterations of max_iter {l4cfg.get('max_iter')}); holdout std / half {f(l4hv['std'])} / {f(l4hv['half'])}{(' ' + l4hv['open']) if l4hv['open'] else ''}")
    print(f"{P}END STATE: {r.get('status')} after {r.get('iterations')} iterations (max_iter {cfg.get('max_iter')}, time limit {cfg.get('time_limit_per_start')} s), LM {f(r.get('seconds'), '%.0f')} s, whole job {t0:%Y-%m-%dT%H:%M:%SZ} -> {t1:%Y-%m-%dT%H:%M:%SZ} = {whole:.0f} s = {whole / 3600:.2f} GPU-h")
    print(f"{P}HOLDOUT rho_u^max std / half: {f(hv['std'])} / {f(hv['half'])}{(' ' + hv['open']) if hv['open'] else ''}; ratio to the L4 start {f(hv['std'] / l4hv['std'] if (hv['std'] is not None and l4hv['std']) else None, '%.3f')} / {f(hv['half'] / l4hv['half'] if (hv['half'] is not None and l4hv['half']) else None, '%.3f')}; V10 {f(r.get('v10_last_tenth_rel_decrease'), '%.2e')}; rms_mom {f(r.get('rms_mom'), '%.4g')}; rho_nl^max {f(r.get('rho_nl_max_holdout'), '%.3g')}")
    print(f"{P}COLLAPSE CHECK (S14R-1): " + "; ".join(f"{n} L4 {f(c['L4'], '%.3g')} -> L6 {f(c['L6'], '%.3g')} (x{f(c['ratio_L6_over_L4'], '%.2f')})" for n, c in coll["values"].items()) + f" -> {coll['verdict']}")
    for lab, od in (("L6", od6), ("L4 start", od4)):
        v = od["values"]
        print(f"{P}ODD-M {lab}: " + (f"energy all / core / tail {f(v['energy_all'], '%.3f')} / {f(v['energy_core'], '%.3f')} / {f(v['energy_tail'], '%.3f')}; amplitude U / Omega / DU {f(v['amp_U'], '%.3f')} / {f(v['amp_Omega'], '%.3f')} / {f(v['amp_DU'], '%.3f')} (file {os.path.basename(od['path'])} sha {od.get('sha256', '')[:12]})" if od["bound"] else f"OPEN ({od['reason']}; {od['path']})"))
    print(f"{P}CORE / BALANCES: core resolved {r.get('core_resolved')}; core-set a_max {f(r.get('a_max_core'), '%.3g')}, sigma_u {f(r.get('sigma_u_max_core'), '%.3g')}, sigma_Om {f(r.get('sigma_Om'), '%.3g')}, a_eff {f(r.get('a_eff'), '%.3g')}; max|U| {f(r.get('max_U'), '%.3f')}, max|Omega| {f(r.get('max_abs_Omega'), '%.3g')}; E_ren {f(r.get('E_ren'), '%.3g')}, H_tot/int|h| {f(r.get('H_tot_over_abs'), '%.3g')}; K_E / K_H ratio {f(r.get('K_ratio_direct'), '%.3g')} / {f(r.get('K_H_ratio_direct'), '%.3g')}, carried mismatch m {f(r.get('G_carried_mismatch_rel'), '%.3g')}; Q_sw {f(r.get('Q_sw'), '%.3g')}; tau_F {f(r.get('tau_F_R8'), '%.3g')}; rotation content {f(r.get('rotation_content_rel'), '%.3g')}")
    if comp:
        c = comp; chv = c["holdout"]
        print(f"{P}COMPARATOR {c['comparator']} (registered even-class L6 state; arm_reading sha {c['arm_reading_sha256'][:12]}, not regenerated; code versions {json.dumps(c['code_versions'], sort_keys=True) if c['code_versions'] else 'n/a'}): holdout std / half {f(chv['std'])} / {f(chv['half'])}{(' ' + chv['open']) if chv['open'] else ''}; ratios target / comparator {f(c['ratio_std'], '%.3f')} / {f(c['ratio_half'], '%.3f')}")
        print(f"{P}BUDGETS: target max_iter {cfg.get('max_iter')}, time limit {cfg.get('time_limit_per_start')} s, {r.get('status')} after {r.get('iterations')} iterations; comparator max_iter {c['max_iter']}, time limit {c['time_limit_per_start']} s, {c['status']} after {c['iterations']} iterations")
        print(f"{P}ORDER 7.3b (bound to this call; order_73b.py sha {c['order']['tool_sha256'][:12]}, rc {c['order']['returncode']}; order JSON {os.path.basename(c['order']['order_json'])} sha {c['order']['order_json_sha256'][:12]}; target arm_reading sha {(c['target_arm_reading_sha256'] or 'n/a')[:12]}): {c['order']['pair']['relation'] if str(c['order']['pair']['relation']).startswith('OPEN') else c['order']['pair']['words']}; ratios (target / comparator: holdout std, half, core sigma_u, sigma_Om, core a_max) {c['order']['pair']['ratios']}; {QUADRATURE_SENTENCE}")
    else:
        print(f"{P}COMPARATOR: none registered at ({cfg['c_l']}, {cfg['omega']}): coverage reading only")
    print(f"{P}CODE VERSIONS (target): " + (json.dumps(res["code_versions"], sort_keys=True) if res["code_versions"] else "not recorded in the results row"))
    if a.json:
        fn = os.path.join(ROOT, "reports", f"s14_stage2_reading_v2_{job}{'_SMOKE' if a.smoke else ''}.json")
        json.dump(res, open(fn, "w"), indent=1, allow_nan=False); print(f"{P}written {fn} sha256 {sha256_file(fn)}")


if __name__ == "__main__":
    main()
