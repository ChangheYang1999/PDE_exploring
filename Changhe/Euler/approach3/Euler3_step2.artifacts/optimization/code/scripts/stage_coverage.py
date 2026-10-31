#!/usr/bin/env python
"""Stage coverage snapshot (lead request 2026-10-25T21:42:35Z; PROMPT section 8 coverage and resource use by stage).
Counts ledger RECORDS up to a boundary time: jobs (launched, completed, failed, running at the boundary), start_result rows
(by status, degree, radial dofs, symmetry class, seed family, formulation, denominator, solver version, (c_l, omega) point),
exclusions from ranking with the reason (the shortlist's filters, applied in the shortlist's order), ranked states and
descriptor bins (shortlist.branch_key), and GPU-hours per GPU from the ledger wall times (launch -> first exit record of the
same job; 1 to 3 processes shared a GPU: the time-weighted concurrency is reported). These are counts of records, not of
distinct random starts or accepted states. Rows with ts after the boundary are not counted (they belong to the next stage).
Usage: stage_coverage.py --boundary 2026-10-25T23:09:12Z --label stage1 [--since 2026-10-24T17:09:14Z]
Writes reports/COVERAGE_<label>_<boundary>.md and .json."""
import sys, os, json, time, argparse, collections, calendar
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
from src.campaign import ledger

ap = argparse.ArgumentParser()
ap.add_argument("--boundary", required=True); ap.add_argument("--label", required=True)
ap.add_argument("--since", default="2026-10-24T17:09:12Z", help="lead T0 2026-10-24T17:09:12Z (the ledger CAMPAIGN_START is 17:09:14Z)"); ap.add_argument("--shortlist_ts", default="2026-10-25T20:17Z", help="generation time of the shortlist the gate cites; ranked rows after it are listed"); ap.add_argument("--gpus", default="0,1,4,5")
ap.add_argument("--no_bins", action="store_true", help="skip loading the start files for the descriptor bins")
a = ap.parse_args()
B, T0 = a.boundary, a.since
def ep(ts):
    return calendar.timegm(time.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S"))
eB, e0 = ep(B), ep(T0)
recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
recs = [r for r in recs if r.get("ts")]
inwin = [r for r in recs if T0 <= r["ts"] <= B]
def jid_of(r):
    if r.get("job_id"):
        return r["job_id"]
    j = r.get("job") or ""
    return os.path.splitext(os.path.basename(j))[0] if j else None

# ---- A. jobs
launches = [r for r in inwin if r["kind"] == "launch"]
jobs_launched = sorted(set(r["job_id"] for r in launches))
done_ids = sorted(set(r["job_id"] for r in inwin if r["kind"] == "job_done"))
failed_ids = sorted(set(r["job_id"] for r in inwin if r["kind"] == "job_failed"))
cancelled_ids = sorted(set(r["job_id"] for r in inwin if r["kind"] == "job_cancelled"))
terminal = set(done_ids) | set(failed_ids) | set(cancelled_ids)
_exit_kinds = ("job_end", "job_error", "job_retry", "job_done", "job_failed", "job_cancelled")
def _last_launch_open(j):            # the job's last launch before the boundary has no exit record before the boundary (consistent with the GPU interval logic below)
    L = sorted(r["ts"] for r in launches if r["job_id"] == j)
    if not L: return False
    return not any(r["kind"] in _exit_kinds and jid_of(r) == j and L[-1] <= r["ts"] <= B for r in recs)
running_at_B = [j for j in jobs_launched if j not in terminal and _last_launch_open(j)]
no_terminal_not_running = [j for j in jobs_launched if j not in terminal and not _last_launch_open(j)]   # ended (job_end/retry/error) but never filed as done/failed: supervisor restarts on 2026-10-24
retries = [r for r in inwin if r["kind"] == "job_retry"]; errors = [r for r in inwin if r["kind"] == "job_error"]; resumes = [r for r in inwin if r["kind"] == "resume"]
def tag(j):
    return str(j).split("_L")[0]
jobs_by_tag = collections.Counter(tag(j) for j in jobs_launched)
done_by_tag = collections.Counter(tag(j) for j in done_ids)
disposable_jobs = [j for j in jobs_launched if ledger.is_disposable(j)]
free_jobs = [j for j in jobs_launched if j.endswith("_free") or "_free_" in j]

# ---- B. start_result rows
starts = [r for r in inwin if r["kind"] == "start_result"]
merged = {id(r): r for r in ledger.merge_reevaluations(recs)}   # for the two-family fields (not needed for counts)
def cnt(key):
    return collections.Counter(str(r.get(key)) for r in starts)
by_status, by_L, by_Nk, by_par, by_form, by_fam, by_den = cnt("status"), cnt("L"), cnt("Nk"), cnt("m_parity"), cnt("formulation"), cnt("family"), cnt("nl_denominator")
def ver(r):
    return r.get("solver_version") or ("v2-untagged" if r.get("gauge_version") == 2 else "v1")
by_ver = collections.Counter(ver(r) for r in starts)
by_free = collections.Counter("free (c_l, omega)" if (r.get("job_id", "").endswith("_free") or "_free_" in r.get("job_id", "")) else "fixed (c_l, omega)" for r in starts)
pts = collections.Counter((round(float(r["c_l"]), 4), round(float(r["omega"]), 4)) for r in starts if r.get("c_l") is not None and r.get("omega") is not None)
by_L_par = collections.Counter((str(r.get("L")), str(r.get("m_parity"))) for r in starts)
channels = collections.Counter("with B/D/E channels" if (r.get("channels") or "chdeg" in json.dumps(r.get("job_id", ""))) else "no channel blocks" for r in starts)
# exclusions, in the shortlist's order: rank key, disposable id, free-parameter job, nontrivial filter
excl = collections.OrderedDict([("no ranking key (rho_u_max_holdout, rho_u_max and rms_final all missing)", 0), ("disposable id (smoke, lm-only, val8/wtest, resume test)", 0),
                                ("free-parameter job (ranked only after a fixed-parameter evaluation, SPEC 7.3)", 0),
                                ("trivial or failed state (max|Omega| <= 1e-6, rotation content <= 1e-3, failure flag, max|U| <= 1e-6 or gauge defect > 1e-3)", 0)])
ranked = []
for r in starts:
    rk = r.get("rho_u_max_holdout") if r.get("rho_u_max_holdout") is not None else (r.get("rho_u_max") if r.get("rho_u_max") is not None else r.get("rms_final"))
    j = str(r.get("job_id", ""))
    if rk is None:
        excl[list(excl)[0]] += 1; continue
    if ledger.is_disposable(j):
        excl[list(excl)[1]] += 1; continue
    if j.endswith("_free") or "_free_" in j:
        excl[list(excl)[2]] += 1; continue
    ok = r.get("max_abs_Omega", 0) > 1e-6 and r.get("rotation_content_rel", 0) > 1e-3 and not r.get("failure") and (r.get("max_U") is None or r.get("max_U") > 1e-6) and (r.get("gauge_defect") is None or r.get("gauge_defect") <= 1e-3)
    if not ok:
        excl[list(excl)[3]] += 1; continue
    r = dict(r); r["rank_key"] = rk; ranked.append(r)
ranked.sort(key=lambda r: r["rank_key"])
pre1939 = [r for r in ranked if r["ts"] < "2026-10-24T19:39"]
_tags = sorted(set(ver(r) for r in recs if r.get("kind") == "start_result")); _dated = [t for t in _tags if "-" in t and t.split("-", 1)[1][:2] == "20"]
latest_tag = max(_dated, key=lambda t: t.split("-", 1)[1]) if _dated else (_tags[-1] if _tags else None)   # as ledger.leaderboard('latest')
ranked_latest = [r for r in ranked if ver(r) == latest_tag]
corr = [r for r in recs if r["kind"] == "correction"]
corrected_rows = set(x for c in corr for x in (c.get("affected") or []))
ranked_corrected = [r for r in ranked if f"{r.get('job_id')}/{r.get('start')}" in corrected_rows]
# descriptor bins (shortlist.branch_key, replicated)
bins = collections.Counter(); bin_err = 0
if not a.no_bins:
    for r in ranked:
        dom_m, tor = None, None
        try:
            S = torch.load(os.path.join(ROOT, r["zfile"]), map_location="cpu", weights_only=False)
            by_m = S["diag"]["tail"]["by_m"]; dom_m = max(by_m, key=lambda k: by_m[k]); tor = S["diag"]["tail"]["toroidal_fraction"]
        except Exception:
            bin_err += 1
        rc = r.get("r_core_holdout") or r.get("r_core") or 0
        rc_class = "core<1" if rc < 1 else ("core1-3" if rc < 3 else "core>3")
        j = str(r.get("job_id", ""))
        lin = "D6" if j.startswith(("d6", "c1c", "c1b", "c1_")) else ("nest" if j.startswith("nest") else ("balance" if j.startswith("s9") else "other"))
        bins[(round(r["c_l"], 2), r["omega"], str(dom_m), ("toroidal" if (tor or 0) > 0.5 else "poloidal"), rc_class, lin)] += 1
entered_after_shortlist = [dict(job=f"{r['job_id']}/{r['start']}", ts=r['ts'], rank_key=r['rank_key'], c_l=r['c_l'], omega=r['omega'], L=r.get('L')) for r in ranked if r['ts'] > a.shortlist_ts]
ranked_pts = collections.Counter((round(float(r["c_l"]), 4), round(float(r["omega"]), 4)) for r in ranked)

# ---- C. GPU wall time per GPU from launch -> first exit record of the same job (job_end / job_error / job_retry / job_done / job_failed / job_cancelled)
exits = collections.defaultdict(list)
for r in recs:
    if r["kind"] in ("job_end", "job_error", "job_retry", "job_done", "job_failed", "job_cancelled"):
        j = jid_of(r)
        if j:
            exits[j].append(ep(r["ts"]))
launch_by_job = collections.defaultdict(list)
for r in recs:
    if r["kind"] == "launch":
        launch_by_job[r["job_id"]].append((ep(r["ts"]), int(r["gpu"]), r["job_id"]))
intervals = []; inferred_ends = []    # (gpu, start, end, job_id, clipped_running)
for j, L in launch_by_job.items():
    L.sort()
    for i, (t, g, _) in enumerate(L):
        if t > eB or t < e0:
            continue
        nxt = L[i + 1][0] if i + 1 < len(L) else None
        cands = [e for e in exits.get(j, []) if e >= t and (nxt is None or e <= nxt)]
        if cands:
            end = min(cands); clipped = end > eB
        elif nxt is not None:                    # no exit record before the relaunch (supervisor restart on 2026-10-24): the process ended by the relaunch at the latest
            end = nxt; clipped = False; inferred_ends.append((j, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t)), g))
        else:
            end = eB; clipped = True
        intervals.append((g, t, min(end, eB), j, clipped))
gpus = [int(v) for v in a.gpus.split(",")]
per_gpu = {}
for g in gpus:
    iv = [x for x in intervals if x[0] == g]
    hours = sum((e - s) for _, s, e, _, _ in iv) / 3600.0
    hours_running = sum((e - s) for _, s, e, _, c in iv if c) / 3600.0
    # concurrency profile
    ev = sorted([(s, 1) for _, s, e, _, _ in iv] + [(e, -1) for _, s, e, _, _ in iv])
    prof = collections.Counter(); cur = 0; last = None
    for t, d in ev:
        if last is not None and cur > 0:
            prof[cur] += (t - last)
        cur += d; last = t
    busy = sum(prof.values()) / 3600.0
    per_gpu[g] = dict(process_hours=round(hours, 2), of_which_jobs_still_running_at_boundary=round(hours_running, 2), launches=len(iv), distinct_jobs=len(set(x[3] for x in iv)),
                      busy_wall_hours=round(busy, 2), mean_concurrency_when_busy=(round(hours / busy, 2) if busy > 0 else None), max_concurrency=(max(prof) if prof else 0),
                      hours_at_concurrency={str(k): round(v / 3600.0, 2) for k, v in sorted(prof.items())}, idle_hours=round((eB - e0) / 3600.0 - busy, 2))
tot_proc_h = sum(v["process_hours"] for v in per_gpu.values()); tot_busy = sum(v["busy_wall_hours"] for v in per_gpu.values())
slot_minutes_done = sum(r.get("minutes", 0) for r in inwin if r["kind"] == "job_done")
start_hours = sum((r.get("seconds") or 0) for r in starts) / 3600.0
# lineage hours (daily report convention)
def lineage_of(j):
    j = str(j)
    for p in ("nest", "d6", "c1", "s1", "s4", "s7", "s8", "s9", "s10", "s11", "s12", "val", "nest10smoke", "sweep", "l4", "l6"):
        if j.startswith(p):
            return p
    return j.split("_")[0]
lin_h = collections.Counter(); lin_n = collections.Counter()
for r in starts:
    lin_h[lineage_of(r.get("job_id"))] += (r.get("seconds") or 0) / 3600.0; lin_n[lineage_of(r.get("job_id"))] += 1

now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
out = dict(generated=now, label=a.label, boundary=B, since=T0, wall_hours=round((eB - e0) / 3600.0, 3), note="counts of ledger records, not of distinct random starts or accepted states; rows with ts after the boundary are not counted",
           jobs=dict(launched_distinct=len(jobs_launched), launches_incl_retries=len(launches), completed=len(done_ids), failed=len(failed_ids), cancelled=len(cancelled_ids),
                     running_at_boundary=running_at_B, launched_without_terminal_record_not_running=no_terminal_not_running, retries=len(retries), worker_errors=len(errors), resumes_from_checkpoint=len(resumes), disposable_jobs=len(disposable_jobs),
                     free_parameter_jobs=len(free_jobs), by_tag_launched=dict(jobs_by_tag), by_tag_completed=dict(done_by_tag), failed_ids=failed_ids, cancelled_ids=cancelled_ids),
           starts=dict(total=len(starts), by_status=dict(by_status), by_L=dict(by_L), by_Nk=dict(by_Nk), by_m_parity=dict(by_par), by_L_and_parity={f"L{k[0]} {k[1]}": v for k, v in sorted(by_L_par.items())},
                       by_formulation=dict(by_form), by_seed_family=dict(by_fam), by_nl_denominator=dict(by_den), by_solver_version=dict(by_ver), by_parameter_mode=dict(by_free),
                       total_start_wall_hours=round(start_hours, 2), by_lineage_hours={k: round(v, 2) for k, v in lin_h.items()}, by_lineage_starts=dict(lin_n),
                       distinct_cl_omega_points=len(pts), cl_omega_points=[dict(c_l=k[0], omega=k[1], omega_over_cl=round(k[1] / k[0], 4), starts=v, ranked=ranked_pts.get(k, 0)) for k, v in sorted(pts.items())]),
           ranking=dict(excluded=dict(excl), ranked=len(ranked), ranked_pre_1939Z_rows_not_used_for_ranked_claims=len(pre1939), ranked_rows_flagged_by_correction_records=len(ranked_corrected),
                        ranked_latest_solver_version_only=len(ranked_latest), ranked_rows_after_shortlist_generation=dict(shortlist_generated=a.shortlist_ts, rows=entered_after_shortlist), latest_solver_version=latest_tag, descriptor_bins=(len(bins) if not a.no_bins else None), bin_load_errors=bin_err,
                        best_ranked=[dict(job=f"{r['job_id']}/{r['start']}", rank_key=r["rank_key"], c_l=r["c_l"], omega=r["omega"], L=r.get("L"), ts=r["ts"]) for r in ranked[:5]],
                        bins_by_lineage=dict(collections.Counter(k[5] for k in bins)) if not a.no_bins else None),
           gpu=dict(gpus=gpus, per_gpu={str(k): v for k, v in per_gpu.items()},
                    allocated_gpu_hours=dict(value=round(len(gpus) * (eB - e0) / 3600.0, 2), definition=f"{len(gpus)} GPUs x elapsed wall clock from T0 {T0} to the boundary {B} ({round((eB - e0) / 3600.0, 3)} h); the primary resource figure"),
                    ledger_busy_gpu_wall_hours=dict(value=round(tot_busy, 2), definition="sum over GPUs of the wall time during which at least one ledger launch -> first-exit interval was open (an activity proxy; never added to the other two figures)"),
                    ledger_process_hours=dict(value=round(tot_proc_h, 2), definition="sum over launches of (first exit record - launch), 1 to 3 processes per GPU (an activity proxy; never added to the other two figures)"),
                    jobs_without_exit_record=dict(running_at_boundary_clipped=[x[3] for x in intervals if x[4]], relaunched_without_exit_record_end_at_relaunch=inferred_ends),
                    gpu_slot_minutes_of_completed_jobs=round(slot_minutes_done, 1), launches_with_end_inferred_from_relaunch=inferred_ends, method="launch record -> first exit record (job_end/job_error/job_retry/job_done/job_failed/job_cancelled) of the same job, clipped at the boundary; 1 to 3 processes per GPU (slots_per_gpu 2 plus ad hoc evaluations are not in the ledger); exclusive jobs hold a whole GPU"))
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
stem = os.path.join(ROOT, "reports", f"COVERAGE_{a.label}_{B.replace(':', '').replace('-', '')}")
json.dump(out, open(stem + ".json", "w"), indent=1, default=str)
L = [f"# Coverage snapshot: {a.label} (boundary {B}; generated {now}; ledger status/ledger.jsonl)", "",
     f"Counts of ledger RECORDS and trajectories between T0 {T0} and {B} ({out['wall_hours']} h of wall clock), not of distinct random starts or accepted states; rows with ts after the boundary are not counted (next stage); ranked rows and bins are counted at the boundary only. Primary route only.", "",
     "## Jobs (supervisor queue)",
     f"- Launched: {len(jobs_launched)} distinct jobs ({len(launches)} process launches incl. {len(retries)} retries; {len(resumes)} resumes from checkpoint; {len(errors)} worker error records).",
     f"- Completed by the boundary: {len(done_ids)}; failed: {len(failed_ids)} ({', '.join(failed_ids) or 'none'}); cancelled: {len(cancelled_ids)} ({', '.join(cancelled_ids) or 'none'}); running at the boundary (their rows count as the next stage): {len(running_at_B)} ({', '.join(running_at_B) or 'none'}); launched but never filed as done or failed and not running (worker exit without a supervisor record, supervisor restarts on 2026-10-24): {len(no_terminal_not_running)} ({', '.join(no_terminal_not_running) or 'none'}).",
     f"- Disposable jobs (smokes, LM-only validations, resume tests; never ranked): {len(disposable_jobs)}; free-parameter jobs: {len(free_jobs)}.",
     "- Jobs by tag (launched / completed): " + ", ".join(f"{k} {v} / {done_by_tag.get(k, 0)}" for k, v in sorted(jobs_by_tag.items())) + ".", "",
     "## Recorded starts (start_result rows)",
     f"- Total {len(starts)}; by status: {dict(sorted(by_status.items()))}.",
     f"- By degree L: {dict(sorted(by_L.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 99))}; by radial Nk: {dict(sorted(by_Nk.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 99))}.",
     f"- Symmetry classes (azimuthal parity): {dict(by_par)}; by L and parity: {out['starts']['by_L_and_parity']}.",
     f"- Formulations: {dict(by_form)}; nonlinear denominators: {dict(by_den)}; parameter mode: {dict(by_free)}; solver versions: {dict(by_ver)}.",
     f"- Seed families: {dict(sorted(by_fam.items(), key=lambda kv: -kv[1]))}.",
     f"- Start wall time (ledger 'seconds'): {start_hours:.1f} process-hours; by lineage: " + ", ".join(f"{k} {lin_n[k]} starts {lin_h[k]:.1f} h" for k in sorted(lin_h, key=lambda k: -lin_h[k])) + ".", "",
     f"## Distinct (c_l, omega) points: {len(pts)}", "| c_l | omega | omega/c_l | recorded starts | ranked |", "|---|---|---|---|---|"]
for p in out["starts"]["cl_omega_points"]:
    L.append(f"| {p['c_l']} | {p['omega']} | {p['omega_over_cl']} | {p['starts']} | {p['ranked']} |")
L += ["", "## Ranking (shortlist filters, applied in order)"]
for k, v in excl.items():
    L.append(f"- excluded: {v} rows: {k}")
L += [f"- Ranked nontrivial states: {len(ranked)} (all solver versions, as in STAGE1_SHORTLIST.md); {len(ranked_latest)} under the latest solver version only ({latest_tag}); {len(pre1939)} of the ranked rows predate 2026-10-24T19:39Z and are not used for ranked claims (G3); {len(ranked_corrected)} ranked rows are flagged by a ledger correction record.",
      (f"- Descriptor bins (shortlist branch key: (c_l, omega) rounded, dominant tail m, toroidal/poloidal, core-radius class, lineage): {len(bins)} ({bin_err} start files unreadable); by lineage: {dict(collections.Counter(k[5] for k in bins))}." if not a.no_bins else "- Descriptor bins: not computed (--no_bins)."),
      f"- Ranked rows that entered after the cited shortlist generation ({a.shortlist_ts}): {len(entered_after_shortlist)}: " + ("; ".join(f"{e['job']} ({e['ts']}, {e['rank_key']:.4g}, c_l {e['c_l']}, omega {e['omega']}, L {e['L']})" for e in entered_after_shortlist) or "none") + ".",
      "- Lowest ranked rows at the boundary: " + "; ".join(f"{b['job']} {b['rank_key']:.4g} (c_l {b['c_l']}, omega {b['omega']}, L {b['L']})" for b in out["ranking"]["best_ranked"]) + ".", "",
      "## GPU use from the ledger wall times (launch -> first exit record of the same job, clipped at the boundary)",
      "| GPU | process-hours | of which still running at the boundary | launches | distinct jobs | busy wall-hours | mean concurrency when busy | max concurrency | hours at concurrency 1 / 2 / 3+ | idle hours |", "|---|---|---|---|---|---|---|---|---|---|"]
for g, v in per_gpu.items():
    hc = v["hours_at_concurrency"]; h3 = sum(float(x) for k, x in hc.items() if int(k) >= 3)
    L.append(f"| {g} | {v['process_hours']} | {v['of_which_jobs_still_running_at_boundary']} | {v['launches']} | {v['distinct_jobs']} | {v['busy_wall_hours']} | {v['mean_concurrency_when_busy']} | {v['max_concurrency']} | {hc.get('1', 0)} / {hc.get('2', 0)} / {round(h3, 2)} | {v['idle_hours']} |")
L += ["- Three hour figures, side by side, with distinct definitions; they are never added together:",
      f"    - ALLOCATED GPU-hours (primary resource figure): {out['gpu']['allocated_gpu_hours']['value']} = {len(gpus)} GPUs x {out['wall_hours']} h from T0 {T0} to {B}.",
      f"    - LEDGER BUSY GPU WALL-HOURS (activity proxy): {tot_busy:.1f} = sum over GPUs of the wall time with at least one launch -> first-exit interval open.",
      f"    - LEDGER PROCESS-HOURS (activity proxy): {tot_proc_h:.1f} = sum over launches of (first exit record - launch); 1 to 3 processes shared a GPU.",
      f"- For reference only, the supervisor's 'minutes' of completed jobs (daily-report convention): {slot_minutes_done:.0f} GPU-slot minutes = {slot_minutes_done / 60:.1f} h.",
      f"- Jobs without an exit record: the ledger figures miss nothing else; the jobs running at the boundary ({', '.join(sorted(set(x[3] for x in intervals if x[4]))) or 'none'}) are clipped at the boundary and their rows count as the next stage.",
      f"- {len(inferred_ends)} launches have no exit record before a relaunch of the same job (supervisor restarts on 2026-10-24); their wall time ends at the relaunch: {inferred_ends}.",
      "- 1 to 3 processes shared a GPU (slots_per_gpu 2 for non-exclusive jobs; exclusive L >= 8 and SPEC-channel jobs hold a whole GPU); ad hoc CPU/GPU evaluations outside the queue (exports, re-evaluations, pressure studies) are not in these wall times. Foreign processes (0.5 to 1.6 GB) are not ours and are not counted."]
open(stem + ".md", "w").write("\n".join(L) + "\n")
print("\n".join(L)); print("\nwritten", stem + ".md", stem + ".json")
