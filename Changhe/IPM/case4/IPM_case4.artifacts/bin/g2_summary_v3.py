#!/usr/bin/env python3
"""G2 evidence summary, version 3 (new file, 2026-10-24T10:5xZ; bin/g2_summary_v2.py is listed in the g2_v10 and g2_v11 manifests and is left untouched from now on). Adds the deviation records for the files edited while a step ran, and marks superseded steps and harness failures in the table. Version 2 text: bin/g2_summary.py is frozen in g2_v6 and superseded. SPEC v9.6 item 4 plus the lead notes of 07:5xZ: for every step of the listed manifests, the runner verdict (from the guard result.json of the run
bound in run.log), the step JSON 'passed' field and the failing check names. A step passes only if all three agree. Also lists the stated
deviations the lead asked to record. Writes outputs/g2/G2_SUMMARY.json and .md. Usage: g2_summary_v2.py <tag>[:step,step,...] ... (default g2_v4 g2_v5 g2_v6)"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, re, sys, hashlib, time
from pathlib import Path
LANE = Path((_artifact_root)); OUT = LANE/'outputs/g2'
DEVIATIONS = [
 'Files edited while a step ran (lead request 10:45Z). (a) During the g2_v10 kappa step, bin/g2_summary_v2.py (in the g2_v10 manifest as 2f4e95da99a107c7..., 9226 bytes) was edited to its present form c0baedcffa61f72a... (10372 bytes, listed as such in g2_v11); the g2_v10 bytes are not kept (no file in the lane carries the old hash). (b) During the g2_v11 supplement2 step, bin/run_g3_steps.sh (dd59bf980936b15b..., 8824 bytes in the g2_v11 manifest) and bin/runner_selftest_v5.py (629dd654d246052d..., 7524 bytes) were edited to 594450e9786e3f67... and a135485ccde3a1e6...; neither file was executed by the step (the step ran bin/run_g2_steps_v10.sh and tests/g2_supplement_v2.py); the before bytes are not kept (the lane holds no file with the old hashes). None of the three files is part of the library or the frozen 181 closure, so the library and closure hashes of g2_v10 and g2_v11 are unaffected. Rule adopted: no manifest-listed file is edited while any step runs; work goes to a renamed copy (this file bin/g2_summary_v3.py is the first such copy).',
 'T0.5 arbiter (v9.6): the 90-digit reference is rounded to binary64 before subtracting, a stated deviation of at most about 2^-52 of the envelope.',
 'T2.7H-X (v9.5): r_b is computed in binary64 from the correctly rounded exact delta, not in 50-digit arithmetic (at most about one ulp in the location of the added sampling point; at both binary64 neighbours of 3 the value is 9065.938286185034).',
 'FIELD_METHODS.cl_derivative_cancellation (frozen basis860 g2_v4) contains the false sentence "below 1e-40 for r >= 1e3": the stated absolute size 8 (j+1) u_ld / (c_l^2 R^2) is 4.3e-31 at j = 3, c_l = 2, r = 1e3; to be corrected at the next library manifest with the formula and its value, not a bound.',
 'bin/runner_selftest.sh does not include the verifier\'s two half-second mtime fixtures (before started_time, after finished_time); the verifier\'s 20-fixture run (c4-ver reviews/g2_runner_v3_*) covers them on the frozen runner.',
 'Metadata strings (basis860.VERSION, model860.Model860.version, origin orders in manifest text) are typed copies kept consistent by hand, not generated from the code constants (v9.5 item 2 asks for generated strings); the G2 audit checks them against ORIGIN_ORDER and R_SWITCH.',
 'T1.8 (v9.8): the floats poisson_max_abs and center_abs of hp_report_float_chart are binary64 records of exact-zero Decimal quantities and are gated by the 1e-60 rule instead of bitwise (flagged in the record).',
 'Policy and resources (lead 08:13Z): g2_v4 t3 was first run under g2_policy_v2 (family RSS ceiling 40,960 MiB) and was terminated by the guard at 68,070 MiB peak family RSS (sidecar outputs/g2/g2_v4/t3_rss_stop_sidecar.json); the relaunch (session s7) and the supplement (s8) run under g2_policy_v3.json, which raises only max_family_rss_mib to 163,840 (note outputs/g2_policy_v3.note.md). Before the G4 manifest the G3 benchmark records peak PSS (smaps_rollup) at the production worker count, or the guard reports PSS, so the G4 limit rests on a measurement.',
 'T2.7H-X2 (lead 08:13Z): the added points r_b, r_d, r_z are gated through added_points_worst_ratio_by_kind_and_field and added_points_worst_dcl_ratio_by_kind_and_field (12 c_l x 3 kinds x 7 fields, values and c_l derivatives, each at most 1e-11), read independently by the lead and the verifier; the aggregated check records in t27hx2.json take band maxima over base and added points together. From G3 on, each added point is gated per point.',
 'The step verdicts of the g2_v4 steps were produced by runner v3 (no step-JSON reading); their JSON passed fields and check records are read independently by this summary (and by the lead and verifier); g2_v5 used runner v4 and g2_v6 runner v5 (SPEC v9.10 strict verdict).']
SUPERSEDED = {('g2_v4', 't0t1'), ('g2_v4', 'supplement')}  # see superseded_steps
HARNESS_FAILURES = {('g2_v8', 'kappa'), ('g2_v9', 'kappa')}  # guard exit 2 before any check ran: Mac epoch path (g2_v8), missing A_REF import (g2_v9); evidence from g2_v10 kappa
NOTES = [
 'farfield860.py and assess860.py are in the g2_v4 manifest but are NOT gated by G2 (lead checklist item 26); their v9.4 revisions (exact exponent grouping, F17) are pending files for the G3 manifest.',
 'T2.4 is a legacy order 20/24 origin overlap check; the production order 48 is gated by the T2.6c origin points, T2.7H and the section 13 monitor (order 48 vs 56).',
 'The SPEC v9.7 rounding calibration (production S_R per path, unrounded Rf_decimal, final rounding charged to the 2^-53 |R_f| term) is a postprocessing supplement before the G4 pilot manifest; it must cover the T2.6x, T2.6d and T3.6 R_f points or list the uncovered sets with a reason.',
 'g2_v4 t0t1 is superseded by g2_v5 t0t1v2 (identical library hashes).',
 'g2_v4 supplement (session s8) is superseded by g2_v11 supplement2 (identical library and closure hashes; lead strict read 10:45Z, review c4-lead/reviews/g2_v11_supplement_v2/REVIEW.md).',
 'g2_v8 and g2_v9 kappa are harness failures without evidence (guard exit 2 at step setup); the calibration evidence is g2_v10 kappa.']
def extra_facts():
    facts = {}
    t26 = OUT/'g2_v4'/'t26.json'
    if t26.exists():
        d = json.loads(t26.read_text()); facts['T2.6d_remainder_block_nodes'] = {k: v for k, v in d.items() if 'remainder' in k.lower() or 'chunk' in k.lower()}
    t27h = OUT/'g2_v4'/'t27h.json'
    if t27h.exists():
        d = json.loads(t27h.read_text()); over = {lab: v.get('floor_cases_count') for lab, v in (d.get('T2.7H') or {}).items() if isinstance(v, dict) and (v.get('floor_cases_count') or 0) > 300}
        facts['T2.7H_cl_values_with_floor_cases_over_300_needing_complete_sidecar'] = over
    return facts
def verdict_lines(tag):
    rows = {}
    log = OUT/tag/'run.log'
    if not log.exists(): return rows
    for line in log.read_text().splitlines():
        m = re.match(r'\[(.*?)\] end (\S+) guard_exit=(\d+) run=(\S+) verdict=(\{.*\})$', line)
        if m:
            utc, step, grc, run, verdict = m.groups()
            try: v = json.loads(verdict)
            except Exception: v = {'ok': False, 'why': ['unparsable verdict line']}
            rows[step] = {'utc': utc, 'guard_exit': int(grc), 'run_dir': run, 'runner_verdict': v}
        m2 = re.match(r'\[(.*?)\] STEP (\S+): (.*chain stopped.*)$', line)
        if m2:
            utc, step, why = m2.groups(); rows[step] = {'utc': utc, 'guard_exit': None, 'run_dir': None, 'runner_verdict': {'ok': False, 'why': ['runner stopped: '+why]}, 'harness_failure': True}
    return rows
def summarize(tag, steps=None):
    rows = verdict_lines(tag); out = []
    names = steps or sorted(rows)
    for step in names:
        rec = {'manifest_tag': tag, 'step': step}
        r = rows.get(step)
        if r is None: rec.update(runner_verdict=None, note='no runner end line (step not run or stopped)'); out.append(rec); continue
        rec.update(r)
        if r.get('harness_failure'): rec.update(step_passes=False, json_passed=None, failing_checks=None, note='harness failure: the runner stopped the chain before a verdict (no result)'); out.append(rec); continue
        try:
            res = json.loads((Path(r['run_dir'])/'result.json').read_text()); rec['guard_result'] = {k: res.get(k) for k in ('run_id', 'success', 'returncode', 'stop_reasons', 'wall_seconds', 'peak_family_rss_mib', 'started_time', 'finished_time')}
        except Exception as exc: rec['guard_result'] = {'error': str(exc)}
        sj = OUT/tag/(step+'.json')
        if sj.exists():
            d = json.loads(sj.read_text()); checks = d.get('checks', [])
            rec.update(step_json=str(sj), step_json_sha256=hashlib.sha256(sj.read_bytes()).hexdigest(), json_passed=d.get('passed'), checks=len(checks), failing_checks=[c.get('check') for c in checks if not c.get('passed')],
                       began_utc=d.get('began_utc'), finished_utc=d.get('finished_utc'), code_manifest_sha256=d.get('code_manifest_sha256'))
        else: rec.update(step_json=None, json_passed=None, failing_checks=None)
        rec['step_passes'] = bool(rec.get('runner_verdict', {}).get('ok') is True and rec.get('json_passed') is True and rec.get('failing_checks') == [])
        out.append(rec)
    return out
def main():
    args = sys.argv[1:] or ['g2_v4', 'g2_v5', 'g2_v6']
    rows = []
    for a in args:
        tag, _, steps = a.partition(':'); rows += summarize(tag, steps.split(',') if steps else None)
    manifests = {t: hashlib.sha256((LANE/'outputs/manifests'/('code_manifest_%s.json' % t)).read_bytes()).hexdigest() for t in {r['manifest_tag'] for r in rows} if (LANE/'outputs/manifests'/('code_manifest_%s.json' % t)).exists()}
    res = {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'notes': NOTES, 'facts': extra_facts(), 'rule': 'a step passes only if the runner verdict is ok, the step JSON passed field is true and no check record failed (SPEC v9.6 item 4)', 'manifests_sha256': manifests, 'steps': rows, 'stated_deviations': DEVIATIONS,
           'superseded_steps': ['g2_v4 t0t1 (passed=false: T0.5 old-route arbiter x3, T1.8 Decimal tails; harness scope per SPEC v9.6; superseded by g2_v5 t0t1v2, same library hashes)',
                                'g2_v4 supplement (session s8): expected passed=false on T2.6b_old_and_new_production_share_the_far_cancellation (g2_supplement.py:129), whose premise predates the v7/v9 repairs (t26 gates the new R_f at e^32/e^44 at 6.0e-17 / 4.2e-17); superseded by tests/g2_supplement_v2.py (gate on the new R_f at e^32/e^44 <= 1e-11 plus a diagnostic without pass/fail) in a new supplement manifest (lead ruling 09:2xZ)',
                                'g2_v8 kappa and g2_v9 kappa: harness failures (untranslated source-host epoch path; missing A_REF import), no result; replaced by g2_v10 kappa (tests/g2_kappa_v97d.py)']}
    (OUT/'G2_SUMMARY.json').write_text(json.dumps(res, indent=1)+'\n')
    md = ['# G2 evidence summary (generated %s by bin/g2_summary_v3.py)' % res['utc'], '', res['rule'], '', 'Manifests: '+', '.join('%s %s' % (k, v[:16]) for k, v in sorted(manifests.items())), '',
          '| manifest | step | runner verdict | guard success/rc | JSON passed | checks | failing checks | step passes | wall s | step JSON sha256 |', '|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        v = r.get('runner_verdict') or {}; g = r.get('guard_result') or {}
        md.append('| %s | %s | %s | %s/%s | %s | %s | %s | %s | %s | %s |' % (r['manifest_tag'], r['step'], 'ok' if v.get('ok') else ('FAIL: '+'; '.join(v.get('why', [])) if v else 'none'), g.get('success'), g.get('returncode'), r.get('json_passed'), r.get('checks', ''), ', '.join(r.get('failing_checks') or []) or '-', 'PASS' if r.get('step_passes') else ('NO (superseded)' if (r['manifest_tag'], r['step']) in SUPERSEDED else ('NO (harness failure, no evidence)' if (r['manifest_tag'], r['step']) in HARNESS_FAILURES else 'NO')), round(g.get('wall_seconds') or 0), (r.get('step_json_sha256') or '')[:16]))
    md += ['', '## Notes', ''] + ['- '+n for n in NOTES] + ['', '## Facts read from the step JSONs', '', '```', json.dumps(res['facts'], indent=1, default=str), '```'] + ['', '## Superseded steps', ''] + ['- '+s for s in res['superseded_steps']] + ['', '## Stated deviations (lead requests, SPEC v9.5 to v9.8)', ''] + ['- '+s for s in DEVIATIONS]
    (OUT/'G2_SUMMARY.md').write_text('\n'.join(md)+'\n'); print('\n'.join(md))
if __name__ == '__main__': main()
