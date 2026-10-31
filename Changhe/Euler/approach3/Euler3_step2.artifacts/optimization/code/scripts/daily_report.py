#!/usr/bin/env python
"""Concise daily report (PROMPT section 6: 'a concise daily report and a machine-readable status summary') from the ledger, the supervisor status
and the exports: elapsed campaign time, measured resource use (GPU-slot minutes of completed jobs, GPU hours per lineage, memory), the best
states with the standing diagnostic lines (both shell families, single-term ratios, Q_sw, tau_F, balances, far coefficients), exports, failure
modes and the queue. Writes reports/DAILY_REPORT_<date>.md and reports/DAILY_STATUS_<date>.json. Usage: daily_report.py [tag]"""
import sys, os, json, time, collections, math
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
tag = sys.argv[1] if len(sys.argv) > 1 else ""
recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
T0 = time.mktime(time.strptime("2026-10-24T17:09:14Z", "%Y-%m-%dT%H:%M:%SZ")) - time.timezone
now = time.time(); elapsed_h = (now - T0) / 3600
stage = 'I' if elapsed_h < 30 else 'II' if elapsed_h < 72 else 'III'
starts = [r for r in recs if r.get("kind") == "start_result"]
jobs_done = [r for r in recs if r.get("kind") == "job_done"]
gpu_minutes = sum(r.get("minutes", 0) for r in jobs_done)
max_rss = max([r.get("max_rss_GB", 0) or 0 for r in jobs_done] + [0])
by_form = collections.Counter((r.get("formulation"), bool(r.get("nl_weighting")), r.get("optimizer", "lm")) for r in starts)
by_L = collections.Counter(r.get("L") for r in starts)
fails = collections.Counter(r.get("status") for r in starts)
errs = [r for r in recs if r.get("kind") in ("job_error", "job_retry", "job_failed")]
def lineage_of(j):
    j = str(j or "")
    if j.startswith("nest"): return "nest ladder (route's own random-start ladder L2 -> L4 -> L6 -> L8)"
    if j.startswith(("d6", "c1c", "c1b", "c1_")): return "D6 lineage (independent-route transfer d6*, continuations)"
    if j.startswith("s9"): return "S9/S9b balance arm"
    if j.startswith("s8"): return "S8 artificial viscosity (labelled viscous continuation states)"
    if j.startswith("s7"): return "S7 mean-swirl probes"
    if j.startswith(("s1", "c2x2")): return "from-scratch L6 sweeps and continuations (s1*, c2x2*)"
    return "other (smoke, tests, controls)"
hours = collections.Counter(); nst = collections.Counter()
for r in starts:
    if r.get("seconds"):
        k = lineage_of(r.get("job_id")); hours[k] += r["seconds"] / 3600.0; nst[k] += 1
fmt = lambda v, f="%.3g": (f % v) if isinstance(v, (int, float)) and v is not None and not (isinstance(v, float) and math.isnan(v)) else "n/a"
rows = ledger.leaderboard(ledger.merge_reevaluations(recs) + [r for r in recs if r.get("kind") != "start_result"], n=10**6, solver_version="all")
rows = [r for r in rows if not ledger.is_disposable(r.get("job_id")) and r.get("rho_u_max_holdout") is not None and not r.get("label")]
rows.sort(key=lambda r: r["rho_u_max_holdout"])
lines = [f"# Daily report, numerics lane, {time.strftime('%Y-%m-%d %H:%MZ', time.gmtime(now))} {tag}".rstrip(), "",
         f"Campaign elapsed: {elapsed_h:.2f} h of 96 (T0 = 2026-10-24T17:09:14Z, logged). Stage {stage}. Stage I ends 2026-10-25T23:09Z, Stage II 2026-10-27T17:09Z, Stage III 2026-10-28T17:09Z.",
         "", "## Resource use (measured)", "",
         f"- Starts completed: {len(starts)} (by degree L: {dict(sorted(by_L.items(), key=lambda kv: str(kv[0])))}); jobs completed: {len(jobs_done)}; GPU-slot minutes of completed jobs: {gpu_minutes:.0f} "
         f"= {gpu_minutes/60:.1f} GPU-slot hours (1-3 processes per GPU on GPUs 0, 1, 4, 5; exclusive L8 jobs hold a whole GPU); largest job RSS {max_rss:.1f} GB (host).",
         f"- Start types (formulation, nl_weighting, optimizer): {dict(by_form)}",
         "- GPU hours per lineage (start wall time, from the ledger):"]
for k in sorted(hours, key=lambda k: -hours[k]):
    lines.append(f"    - {k}: {nst[k]} starts, {hours[k]:.1f} h")
lines += ["", "## Best states by holdout rho_u^max (SPEC 7.3 key; standing lines; none is a candidate: no state reaches Tier S; all primary-reported, unvalidated unless stated in NUM_REPORT)", ""]
for r in rows[:10]:
    lines.append(f"- {r['job_id']}/{r.get('start')} (c_l {r['c_l']}, omega {r['omega']}, omega/c_l {r['omega']/r['c_l']:.3f}, L {r.get('L')}, Nk {r.get('Nk')}): rho_u^max {fmt(r.get('rho_u_max_holdout'), '%.4f')} std / {fmt(r.get('rho_u_max_holdout_half'), '%.4f')} half; "
                 f"rho_nl^max {fmt(r.get('rho_nl_max_holdout_both') or r.get('rho_nl_max_holdout'), '%.2f')}; sigma_u^max {fmt(r.get('sigma_u_max_core') or r.get('sigma_u_max'), '%.2f')}; sigma_Om {fmt(r.get('sigma_Om'), '%.2f')}; a_max {fmt(r.get('a_max_core') or r.get('a_max'), '%.2f')}; "
                 f"rho_lin {fmt(r.get('rho_lin_max_holdout'), '%.2f')}; Q_sw {fmt(r.get('Q_sw'), '%.3f')}; tau_F {fmt(r.get('tau_F_R8'), '%.3f')}; tau_0/1/2 {fmt(r.get('tau0_floored'), '%.1e')}/{fmt(r.get('tau1_floored'), '%.1e')}/{fmt(r.get('tau2_floored'), '%.1e')}; "
                 f"E_ren {fmt(r.get('E_ren'), '%.3f')}; H_tot/int|h| {fmt(r.get('H_tot_over_abs'), '%.3f')}; K_E ratio {fmt(r.get('K_ratio_direct'), '%.2f')}; K_H ratio {fmt(r.get('K_H_ratio_direct'), '%.2f')}; V10 {fmt(r.get('v10_last_tenth_rel_decrease'), '%.1e')}; "
                 f"{r.get('iterations')} its, {fmt((r.get('seconds') or 0)/3600, '%.2f')} GPU-h; status {r.get('status')}")
lines += ["", "## Exports (candidates/, SPEC 10 format; immutable, SHA256 manifests; v1.24 far-coefficient supplements beside meta.json)", ""]
cdir = os.path.join(ROOT, "candidates"); exports = []
for cid in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
    d = os.path.join(cdir, cid)
    if not os.path.isdir(d): continue
    sz = sum(os.path.getsize(os.path.join(d, f)) for f in os.listdir(d)) / 2 ** 20
    sup = os.path.join(d, "meta_supplement_v124.json"); kh = None
    if os.path.exists(sup):
        try:
            g = json.load(open(sup))["G_closure_v124"]; kh = (g.get("K_ratio_direct"), g.get("K_H_ratio_direct"), g.get("carried_mismatch_rel"))
        except Exception: kh = None
    exports.append(dict(id=cid, MB=round(sz, 1), K_E_ratio=kh[0] if kh else None, K_H_ratio=kh[1] if kh else None, carried_mismatch=kh[2] if kh else None))
    lines.append(f"- {cid} ({sz:.0f} MB)" + (f": K_E ratio {fmt(kh[0], '%.2f')}, K_H ratio {fmt(kh[1], '%.3f')}, carried mismatch {fmt(kh[2], '%.3f')}" if kh else ""))
lines += ["", "## Optimizer exit statuses and failure modes", "", f"- Exit statuses of all starts: {dict(fails)}",
          f"- Job errors, retries and failures: {len(errs)} records" + ("" if not errs else "; last: " + "; ".join(f"{e.get('kind')} {e.get('job_id', e.get('job'))} {str(e.get('reason', e.get('error', '')))[:60]}" for e in errs[-5:])),
          "- Failure map: FAILURE_ANALYSIS.md (numbered items with mechanisms and remedies); current label provisional C (lead): no accepted candidate, no obstruction.", ""]
st_path = os.path.join(ROOT, "status", "STATUS.json"); st = None
if os.path.exists(st_path):
    st = json.load(open(st_path))
    lines += ["## Supervisor and queue (machine-readable: status/STATUS.json, updated every poll)", "",
              f"- {st['ts']}: running {len(st['running'])} ({', '.join(st['running'])}), pending {st['pending']}, done {st['done']}, failed {st['failed']}, disk free {st.get('disk_free_GB')} GB, lane {st.get('lane_usage_GB')} GB, GPUs {st.get('gpus')}", ""]
lines += ["## Pointers", "", "- NUM_REPORT.md (current summary), reports/STAGE1_SHORTLIST.md (G4 shortlist with the 7.3b pairwise table), reports/G1_TESTS.md, reports/G3_LEDGER.md, reports/FAR_COEFFICIENTS.md (SPEC v1.24 7.8), reports/GATE_I4_RESPONSE_DRAFT.md, reports/STAGE2_FEASIBILITY_DRAFT.md, reports/RESOLUTION_LADDER.md, reports/figures/."]
day = time.strftime("%Y-%m-%d", time.gmtime(now))
out = os.path.join(ROOT, "reports", f"DAILY_REPORT_{day}{('_' + tag) if tag else ''}.md")
open(out, "w").write("\n".join(lines) + "\n")
summary = dict(generated=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)), T0="2026-10-24T17:09:14Z", elapsed_hours=round(elapsed_h, 3), stage=stage, starts_completed=len(starts), jobs_completed=len(jobs_done),
               gpu_slot_minutes_completed_jobs=round(gpu_minutes, 1), max_job_rss_GB=max_rss, starts_by_L={str(k): v for k, v in by_L.items()}, gpu_hours_by_lineage={k: round(v, 2) for k, v in hours.items()}, starts_by_lineage=dict(nst),
               exit_statuses={str(k): v for k, v in fails.items()}, job_error_records=len(errs), tier_S_states=0, label="provisional C (lead)",
               best_states=[{k: r.get(k) for k in ("job_id", "start", "c_l", "omega", "L", "Nk", "rho_u_max_holdout", "rho_u_max_holdout_half", "rho_nl_max_holdout_both", "sigma_u_max_core", "sigma_Om", "a_max_core", "Q_sw", "tau_F_R8", "E_ren", "H_tot_over_abs", "K_ratio_direct", "K_H_ratio_direct", "v10_last_tenth_rel_decrease", "iterations", "seconds", "status", "zfile")} for r in rows[:10]],
               exports=exports, supervisor=(dict(ts=st["ts"], running=list(st["running"]), pending=st["pending"], done=st["done"], failed=st["failed"], disk_free_GB=st.get("disk_free_GB"), lane_GB=st.get("lane_usage_GB")) if st else None))
jout = os.path.join(ROOT, "reports", f"DAILY_STATUS_{day}{('_' + tag) if tag else ''}.json")
json.dump(summary, open(jout, "w"), indent=1, default=str)
print("\n".join(lines)); print("written", out, "and", jout)
