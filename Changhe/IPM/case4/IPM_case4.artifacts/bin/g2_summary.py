#!/usr/bin/env python3
"""G2 evidence summary (SPEC v9.6 item 4): for every step of the listed manifests, the runner verdict (from the guard result.json of the run
bound in run.log), the step JSON 'passed' field and the failing check names. A step passes only if all three agree. Also lists the stated
deviations the lead asked to record. Writes outputs/g2/G2_SUMMARY.json and .md. Usage: g2_summary.py <tag>[:step,step,...] ... (default g2_v4 g2_v5)"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, re, sys, hashlib, time
from pathlib import Path
LANE = Path((_artifact_root)); OUT = LANE/'outputs/g2'
DEVIATIONS = [
 'T0.5 arbiter (v9.6): the 90-digit reference is rounded to binary64 before subtracting, a stated deviation of at most about 2^-52 of the envelope.',
 'T2.7H-X (v9.5): r_b is computed in binary64 from the correctly rounded exact delta, not in 50-digit arithmetic (at most about one ulp in the location of the added sampling point; at both binary64 neighbours of 3 the value is 9065.938286185034).',
 'FIELD_METHODS.cl_derivative_cancellation (frozen basis860 g2_v4) contains the false sentence "below 1e-40 for r >= 1e3": the stated absolute size 8 (j+1) u_ld / (c_l^2 R^2) is 4.3e-31 at j = 3, c_l = 2, r = 1e3; to be corrected at the next library manifest with the formula and its value, not a bound.',
 'bin/runner_selftest.sh does not include the verifier\'s two half-second mtime fixtures (before started_time, after finished_time); the verifier\'s 20-fixture run (c4-ver reviews/g2_runner_v3_*) covers them on the frozen runner.',
 'Metadata strings (basis860.VERSION, model860.Model860.version, origin orders in manifest text) are typed copies kept consistent by hand, not generated from the code constants (v9.5 item 2 asks for generated strings); the G2 audit checks them against ORIGIN_ORDER and R_SWITCH.',
 'T1.8 (v9.8): the floats poisson_max_abs and center_abs of hp_report_float_chart are binary64 records of exact-zero Decimal quantities and are gated by the 1e-60 rule instead of bitwise (flagged in the record).',
 'Nonfinite handling in the pending campaign driver v3: a nonfinite trial residual or trial objective is the documented SPEC 11 nonfinite rejection (explicit check before any comparison), while nonfinite Jacobian/step entries are process faults; this deviates from the F16 wording (lead ruling requested).']
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
    return rows
def summarize(tag, steps=None):
    rows = verdict_lines(tag); out = []
    names = steps or sorted(rows)
    for step in names:
        rec = {'manifest_tag': tag, 'step': step}
        r = rows.get(step)
        if r is None: rec.update(runner_verdict=None, note='no runner end line (step not run or stopped)'); out.append(rec); continue
        rec.update(r)
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
    args = sys.argv[1:] or ['g2_v4', 'g2_v5']
    rows = []
    for a in args:
        tag, _, steps = a.partition(':'); rows += summarize(tag, steps.split(',') if steps else None)
    manifests = {t: hashlib.sha256((LANE/'outputs/manifests'/('code_manifest_%s.json' % t)).read_bytes()).hexdigest() for t in {r['manifest_tag'] for r in rows} if (LANE/'outputs/manifests'/('code_manifest_%s.json' % t)).exists()}
    res = {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'rule': 'a step passes only if the runner verdict is ok, the step JSON passed field is true and no check record failed (SPEC v9.6 item 4)', 'manifests_sha256': manifests, 'steps': rows, 'stated_deviations': DEVIATIONS,
           'superseded_steps': ['g2_v4 t0t1 (passed=false: T0.5 old-route arbiter x3, T1.8 Decimal tails; harness scope per SPEC v9.6; superseded by g2_v5 t0t1v2, same library hashes)']}
    (OUT/'G2_SUMMARY.json').write_text(json.dumps(res, indent=1)+'\n')
    md = ['# G2 evidence summary (generated %s by bin/g2_summary.py)' % res['utc'], '', res['rule'], '', 'Manifests: '+', '.join('%s %s' % (k, v[:16]) for k, v in sorted(manifests.items())), '',
          '| manifest | step | runner verdict | guard success/rc | JSON passed | checks | failing checks | step passes | wall s | step JSON sha256 |', '|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        v = r.get('runner_verdict') or {}; g = r.get('guard_result') or {}
        md.append('| %s | %s | %s | %s/%s | %s | %s | %s | %s | %s | %s |' % (r['manifest_tag'], r['step'], 'ok' if v.get('ok') else ('FAIL: '+'; '.join(v.get('why', [])) if v else 'none'), g.get('success'), g.get('returncode'), r.get('json_passed'), r.get('checks', ''), ', '.join(r.get('failing_checks') or []) or '-', 'PASS' if r.get('step_passes') else 'NO', round(g.get('wall_seconds') or 0), (r.get('step_json_sha256') or '')[:16]))
    md += ['', '## Superseded steps', ''] + ['- '+s for s in res['superseded_steps']] + ['', '## Stated deviations (lead requests, SPEC v9.5 to v9.8)', ''] + ['- '+s for s in DEVIATIONS]
    (OUT/'G2_SUMMARY.md').write_text('\n'.join(md)+'\n'); print('\n'.join(md))
if __name__ == '__main__': main()
