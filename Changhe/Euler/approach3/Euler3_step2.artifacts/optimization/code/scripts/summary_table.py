#!/usr/bin/env python
"""v2.1 (2026-10-30T09:2xZ; V708): the record of a run is found by the exact run path state.source (v2 read run_path, a diagnostics dictionary, so every record column was empty). v2 (2026-10-30T09:1xZ): the lineage grouping is read from configs/lineage_status.txt (LINEAGE | RUN | STATUS | NOTE) instead of the stale hard-coded list of v1 (which omitted every run after 2026-10-29T21:39Z: cont2_s6, p3_s2b, p3c_s2b, cont3free, cont4free, F1 m3/m4, F2 m3/m4, the bracket pilot, the breadth pilots, strategy 2, the perturbation repeat and the PROFILE runs); runs with an end record that are not listed there are appended under "other production runs" (smoke, resume-test and segment-test runs excluded by name); the 6.3 (a) record of a run is found from the run_path of validation/records_63a/*.json (latest version by ts; its .decision.txt when present).
Deliverable A (PROMPT 11.A) numerics table from the worker end records (results.jsonl start_result rows) of every production run: per run and per lineage
(segments in order). Columns: run, label, initial (c_l, omega), final (c_l, omega), O1 initial and final, rho_u^max on the training grid, the dyadic holdout
family and the half-offset family, sigma_u^max, a_max_core (both weights), N_core, N_F, accepted iterations (cumulative for lineages), LM seconds, stop reason,
6.3 (a) record state (validation/records_63a/<tag>.json: exclusions, flags, wrapper decision file). Values are the worker's own (optimizer) values; the
independently checked values are the verifier's (VERIFY_REPORT). Usage: python scripts/summary_table.py -> validation/summary_runs.json and prints markdown."""
import os, sys, json, glob, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
def _load_lineages():
    import collections
    cfg = os.path.join(ROOT, "configs", "lineage_status.txt"); L = collections.OrderedDict(); status = {}
    for line in open(cfg):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [q.strip() for q in line.split("|")]
        if len(parts) < 3:
            continue
        L.setdefault(parts[0], []).append(parts[1]); status[parts[1]] = parts[2]
    listed = {r for v in L.values() for r in v}; others = []
    for d in sorted(os.listdir(os.path.join(ROOT, "runs"))):
        if d in listed or d.startswith("INVALID"):
            continue
        if any(d.startswith(x) for x in ("s2smoke_", "smk", "g7_", "resume_test_", "segA_", "segB_", "segC_")):
            continue
        if os.path.isfile(os.path.join(ROOT, "runs", d, "results.jsonl")) or os.path.isfile(os.path.join(ROOT, "runs", d, "worker.log")):
            others.append(d)
    if others:
        L["other production runs (not in configs/lineage_status.txt)"] = others
    return L, status


LINEAGES, STATUS_WORDS = _load_lineages()


def _end_records():
    """run name -> (tag, start reference) from the run_path of the records (latest version by ts)"""
    out = {}
    for p in glob.glob(os.path.join(ROOT, "validation", "records_63a", "*.json")):
        try:
            d = json.load(open(p))
        except Exception:
            continue
        if d.get("is_start_reference") or (d.get("state") or {}).get("mode") != "end":
            continue
        # v2.1 (V708): the run is the exact path state.source (run_path is a diagnostics dictionary in these records); start_reference is a list of {path, sha256, tag, ...}
        src = str((d.get("state") or {}).get("source") or ""); run = os.path.basename(src.rstrip("/"))
        if not run or not os.path.isdir(os.path.join(ROOT, "runs", run)):
            continue
        tag = os.path.basename(p)[:-5]; sr_ = d.get("start_reference"); ref = None
        if isinstance(sr_, list) and sr_:
            ref = ", ".join(str(x.get("tag")) for x in sr_ if isinstance(x, dict))
        elif isinstance(sr_, dict):
            ref = sr_.get("tag")
        elif sr_:
            ref = str(sr_)
        prev = out.get(run)
        if prev is None or str(d.get("ts", "")) > prev[2]:
            out[run] = (tag, ref, str(d.get("ts", "")))
    return {k: (v[0], v[1]) for k, v in out.items()}


END_RECORDS = _end_records()


def last_result(run):
    p = os.path.join(ROOT, "runs", run, "results.jsonl")
    if not os.path.isfile(p):
        return None
    rows = [json.loads(l) for l in open(p) if l.strip()]; rs = [r for r in rows if r.get("kind") == "start_result"]
    return rs[-1] if rs else None


def running_state(run):
    """for a run without results: the last accepted iteration from worker.log"""
    import re
    p = os.path.join(ROOT, "runs", run, "worker.log")
    if not os.path.isfile(p):
        return None
    last = None
    for line in open(p):
        m = re.search(r"LM it\s+(\d+)\s+cost\s+([0-9.eE+-]+).*?c_l\s+([0-9.]+)\s+omega\s+([0-9.]+)", line)
        if m:
            last = dict(it=int(m.group(1)), cost=float(m.group(2)), c_l=float(m.group(3)), omega=float(m.group(4)), ts=line[:20])
    return last


def record_state(run):
    tag = END_RECORDS.get(run)
    if not tag:
        return None
    p = os.path.join(ROOT, "validation", "records_63a", tag[0] + ".json")
    if not os.path.isfile(p):
        return dict(tag=tag[0], present=False)
    d = json.load(open(p)); dec = None
    dp = os.path.join(ROOT, "validation", "records_63a", tag[0] + ".decision.txt")
    if os.path.isfile(dp):
        dec = open(dp).read().strip().splitlines()[-1][:40]
    else:   # v2.1: the wrapper's decision line in the chain log ("6.3 (a) decision for <run or tag>[ vs ref]: yes|no | ...")
        lg = os.path.join(ROOT, "validation", "logs", "l_slot_chain.log")
        if os.path.isfile(lg):
            for line in open(lg):
                if "6.3 (a) decision for " in line and (run in line or tag[0] in line):
                    dec = line.split(": ", 1)[1].strip()[:40] if ": " in line.split("6.3 (a) decision for ", 1)[1] else None
                    dec = line.split("6.3 (a) decision for ", 1)[1].split(": ", 1)[1].strip()[:40]
    return dict(tag=tag[0], reference=tag[1], version=d.get("version"), exclusions=[e["item"][:50] for e in d["exclusions_6_3a"] if e["raised"]], flags=[f["item"][:60] for f in d["flags_6_3b"] if f["raised"]], open=d.get("open"), wrapper=dec)


def fmt(v, f="{:.4g}"):
    return "-" if v is None else (f.format(v) if isinstance(v, (int, float)) else str(v))


out = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), lineages={}, note="worker end-record values (optimizer); independent values are the verifier's")
md = ["| Lineage / run | label | initial (c_l, omega) | final (c_l, omega) | O1 initial -> final | rho_u^max train / dyadic / half-offset | sigma_u^max | a_max_core (centre / upper) | N_core, N_F | it (cum) | LM h | stop | 6.3 (a) record |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for lin, runs in LINEAGES.items():
    segs = []; cum_it = 0; lm_s = 0.0; first_params = None; first_cost = None
    for run in runs:
        r = last_result(run)
        if r is None:
            st = running_state(run)
            if st is None:
                continue
            sw = STATUS_WORDS.get(run, "running"); inrun = os.path.isfile(os.path.join(ROOT, "queue", "running", run + ".json")) or os.path.isfile(os.path.join(ROOT, "queue", "staged", run + ".json")) or os.path.isfile(os.path.join(ROOT, "queue", "pending", run + ".json"))
            state = "RUNNING" if inrun else f"NO END RECORD ({sw})"
            segs.append(dict(run=run, running=inrun, status_word=sw, last=st)); cum_it = st["it"] if st["it"] > cum_it else cum_it
            md.append(f"| {run} ({state}) | - | - | ({st['c_l']:.6f}, {st['omega']:.6f}) at it {st['it']} | -> {st['cost']:.4e} | - | - | - | - | {st['it']} | - | {'running' if inrun else sw} | - |")
            continue
        pi = r.get("params_initial") or {}; pf = r.get("params_final") or {}
        if first_params is None:
            first_params = (pi.get("c_l", r.get("c_l")), pi.get("omega", r.get("omega"))); first_cost = r.get("cost_initial")
        it = int(r.get("iterations") or 0); cum_it = it if it > cum_it else cum_it; lm_s += float(r.get("t_lm_s") or r.get("lm_seconds") or 0.0)
        rec = record_state(run)
        row = dict(run=run, label=r.get("label"), params_initial=pi, params_final=pf, cost_initial=r.get("cost_initial"), cost_final=r.get("cost_final"), rho_u_max=r.get("rho_u_max"), rho_u_max_holdout=r.get("rho_u_max_holdout"), rho_u_max_holdout_half=r.get("rho_u_max_holdout_half"),
                   sigma_u_max=r.get("sigma_u_max"), a_max_core=r.get("a_max_core"), a_max_core_upper=r.get("a_max_core_upper"), N_core=r.get("N_core"), N_F=r.get("N_F"), max_U=r.get("max_U"), iterations=it, n_accepted=r.get("n_accepted"), n_rejected=r.get("n_rejected"), t_lm_s=r.get("t_lm_s"), stop=r.get("stop_reason") or r.get("status"),
                   core_resolved=r.get("core_resolved"), tier_S=r.get("tier_S"), tier_S_holdout=r.get("tier_S_holdout"), v10=r.get("v10_last_tenth_rel_decrease"), record_63a=rec, zfile=r.get("zfile"))
        segs.append(row)
        recs = "-" if rec is None else (("v%s %s; excl %d; flags %d; wrapper %s" % (rec.get("version"), rec["tag"], len(rec.get("exclusions") or []), len(rec.get("flags") or []), rec.get("wrapper"))) if rec.get("present", True) else f"{rec['tag']} absent")
        md.append(f"| {run} | {r.get('label')} | ({fmt(pi.get('c_l', r.get('c_l')), '{:.6f}')}, {fmt(pi.get('omega', r.get('omega')), '{:.6f}')}) | ({fmt(pf.get('c_l', r.get('c_l')), '{:.6f}')}, {fmt(pf.get('omega', r.get('omega')), '{:.6f}')}) | {fmt(r.get('cost_initial'), '{:.4e}')} -> {fmt(r.get('cost_final'), '{:.4e}')} | {fmt(r.get('rho_u_max'))} / {fmt(r.get('rho_u_max_holdout'))} / {fmt(r.get('rho_u_max_holdout_half'))} | {fmt(r.get('sigma_u_max'))} | {fmt(r.get('a_max_core'))} / {fmt(r.get('a_max_core_upper'))} | {fmt(r.get('N_core'), '{:.3f}')}, {fmt(r.get('N_F'), '{:.3f}')} | {it} | {fmt((r.get('t_lm_s') or 0) / 3600, '{:.2f}')} | {r.get('stop_reason') or r.get('status')} | {recs} |")
    if segs:
        out["lineages"][lin] = dict(segments=segs, cumulative_iterations=cum_it, lm_hours=lm_s / 3600, first_params=first_params, first_cost=first_cost)
        md.insert(len(md) - len(segs), f"| **{lin}** | | | | | | | | | **{cum_it}** | **{lm_s / 3600:.2f}** | | |")
op = os.path.join(ROOT, "validation", "summary_runs.json"); json.dump(out, open(op, "w"), indent=1, default=str)
print("\n".join(md)); print(f"\nwritten {op}")
