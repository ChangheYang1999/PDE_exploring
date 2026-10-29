#!/usr/bin/env python3
"""One-command independent registered validation of a documented saved export.

Exit 0: measured A1/A2/A8 checks pass; full acceptance is still OPEN.
Exit 2: completed registered checks reject this approximation.
Exit 3: preflight failed, so the claimed exported state was not validated.
Exit 1: execution/input failure. See summary.json for the precise scope.
"""
from pathlib import Path
import argparse,datetime,json,subprocess,sys,time
from export_preflight import preflight
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('export',type=Path)
    ap.add_argument('--source-result',type=Path)
    ap.add_argument('--output',required=True,type=Path)
    ap.add_argument('--resume',action='store_true')
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    if (out/'summary.json').exists():raise FileExistsError('completed validation is immutable')
    if out.exists() and not a.resume:raise FileExistsError('use --resume for unfinished work')
    out.mkdir(parents=True,exist_ok=True);start=time.perf_counter()
    checks=preflight(a.export,a.source_result)
    if (out/'preflight.json').exists():
        previous=json.loads((out/'preflight.json').read_text())
        if previous['input_sha256']!=checks['input_sha256']:raise ValueError('resume input changed')
        if previous['source_sha256']!=checks['source_sha256']:raise ValueError('resume evaluator changed')
    else:atomic_json(out/'preflight.json',checks)
    summary=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        input_sha256=checks['input_sha256'],c_l=checks['c_l'],alpha=checks['alpha'],
        accepted_as_A=False,acceptance_status='OPEN: residual checks alone do not establish full acceptance',
        validation_driver_sha256=sha256(__file__))
    if checks['status']!='PASS':
        summary.update(status='PREFLIGHT_FAILED',issues=checks['issues'],exit_code=3,
            scope='The claimed saved state was not passed to Euler validation.')
        atomic_json(out/'summary.json',summary);print(json.dumps(summary),flush=True);return 3
    coefficient=a.export.resolve()/'coeffs.npz'
    registered=out/'registered'
    if not (registered/'summary.json').exists():
        command=[sys.executable,str(ROOT/'registered_piecewise.py'),str(coefficient),'--output',str(registered)]
        if (registered/'metadata.json').exists():command.append('--resume')
        with (out/'registered.log').open('ab') as log:
            subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,check=True)
    record=json.loads((registered/'summary.json').read_text())
    if record['candidate_sha256']!=checks['input_sha256']['coeffs.npz']:raise ValueError('wrong registered coefficients')
    verify_source_identity(ROOT,record['source_sha256'])
    tail=out/'tail.json'
    if not tail.exists():
        command=[sys.executable,str(ROOT/'coefficient_tail_audit.py'),str(coefficient),'--output',str(tail)]
        with (out/'tail.log').open('ab') as log:
            subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,check=True)
    tail_record=json.loads(tail.read_text())
    if tail_record['input_sha256']!=checks['input_sha256']['coeffs.npz']:raise ValueError('wrong tail coefficients')
    verify_source_identity(ROOT,tail_record['source_sha256'])
    passed=bool(record['complete_required_shell_set'] and record['aggregate']['A1_measured_pass']
        and record['aggregate']['A2_measured_pass'] and record['interface_summary']['all_A8_interface_checks_pass'])
    summary.update(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        current_process_wall_seconds=time.perf_counter()-start,
        status='MEASURED_A1_A2_A8_PASS' if passed else 'REJECTED_BY_REQUIRED_CHECKS',exit_code=0 if passed else 2,
        aggregate=record['aggregate'],interface_summary=record['interface_summary'],
        correction_relative_to_Euler=tail_record['correction_relative_to_Euler'],
        reports={'preflight':'preflight.json','registered':'registered/summary.json','tail':'tail.json'},
        scope='Independent reduced and primitive residuals with bulk full-space pressure, all registered shells and origin, interface regularity and coefficient tail audit. Pressure refinement, a second discretization, energy/helicity/maximum identities, continuation, nontriviality and full A/B acceptance remain separate audits.')
    atomic_json(out/'summary.json',summary);print(json.dumps(summary),flush=True);return summary['exit_code']
if __name__=='__main__':raise SystemExit(main())
