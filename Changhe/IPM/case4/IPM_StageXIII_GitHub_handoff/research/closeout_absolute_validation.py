"""Standard-library final closeout; no numerical execution or optimization."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import time

ROOT=Path(__file__).resolve().parent


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(args):
    output=args.output.resolve()
    if ROOT not in output.parents or output.exists():
        raise ValueError('Choose a new closeout record inside the absolute workspace')
    errors=[]
    evidence=read(ROOT/'provenance/evidence_audit_final.json')
    preservation=read(ROOT/'provenance/preservation_latest.json')
    status=read(ROOT/'results/report_status.json')
    if not evidence.get('passed') or not evidence.get('complete'):
        errors.append('Final source/artifact/provenance audit is incomplete or failed')
    if not preservation.get('passed') or preservation.get('errors'):
        errors.append('Protected historical files failed preservation')
    if not status.get('final_generation_requested') or status.get('pending'):
        errors.append('Report is not final or required evidence remains pending')
    if status.get('optimization_performed') or status.get('future_optimization_gate_open'):
        errors.append('Optimization boundary changed')
    if read(ROOT/'workspace.json').get('optimization_permitted') is not False:
        errors.append('Workspace optimization restriction changed')
    unresolved=[x for x in status.get('failed',[]) if x!='global full derivative preparation']
    if unresolved:
        errors.append({'unexpected_report_failures':unresolved})
    recovery=read(ROOT/'results/derivatives/global_recovery/checks.json')
    if not recovery.get('completed') or not recovery.get('passed'):
        errors.append('Separate global v2 recovery has not passed')
    allowed={'environment_probe.py','field_tests.py','manufactured_tests.py',
             'candidate_semantics.py','far_asymptotic.py','integrate_candidate.py',
             'tail_envelope_tests.py','integration_driver_tests.py','assess_candidates.py',
             'absolute_derivative_checks.py','absolute_derivative_checks_v2.py',
             'exact_dilation_checks.py','prepare_whole_axis.py',
             'arithmetic_comparison.py','chart_diagnostics_v2.py'}
    commands=[json.loads(x) for x in (ROOT/'provenance/commands.jsonl').read_text().splitlines() if x.strip()]
    workers=[]
    for row in commands:
        command=row['command']
        worker=next((Path(x) for x in reversed(command) if x.endswith('.py')),None)
        if worker is None or worker.parent!=ROOT or worker.name not in allowed:
            errors.append({'unexpected_worker':str(worker)})
        else:
            workers.append(worker.name)
        for key,want in [('--work-dir',str(ROOT)),('--session-dir',str(ROOT/'resource_session'))]:
            if key not in command or command[command.index(key)+1]!=want:
                errors.append({'invalid_command_boundary':key,'command':command})
    for case in ('stage11','combined','local','global'):
        p=ROOT/'results/whole_axis_preparation'/case/'preparation.json'
        record=read(p)
        if not record.get('passed') or record.get('future_optimization_gate_open') is not False:
            errors.append({'whole_axis_preparation':case})
    syntax=[]
    for path in sorted(ROOT.glob('*.py')):
        ast.parse(path.read_text(),filename=str(path))
        syntax.append({'path':path.name,'sha256':digest(path)})
    documents=['ABSOLUTE_LOSS_REPORT.md','MATHEMATICAL_DERIVATION.md',
               'OPTIMIZATION_PREPARATION.md','REPRODUCE.md','EXECUTED_COMMANDS.md']
    links=[]
    for name in documents:
        path=ROOT/name
        content=path.read_text()
        for target in re.findall(r'\]\(<?(/[^\n)>]+)>?\)',content):
            target=re.sub(r':\d+$','',target)
            if not Path(target).exists():
                errors.append({'broken_local_link':target,'document':name})
            links.append(target)
    resource_failures=status.get('resources',{}).get('worker_returncode_failures',[])
    for row in resource_failures:
        rid=row['run_id']
        if not (rid.endswith('_absolute_uniform_tail_tests') or
                rid.endswith('_absolute_uniform_tail_tests_repaired') or
                rid.endswith('_absolute_derivative_global')):
            errors.append({'unexpected_failed_execution':row})
    record={'schema':'absolute_loss_final_closeout_v1','epoch':time.time(),
            'passed':not errors,'errors':errors,'numerical_execution_performed':False,
            'optimization_launched':False,'future_optimization_gate_open':False,
            'validation_command_count':len(commands),'validation_workers':sorted(set(workers)),
            'protected_entries':preservation['checked_entries'],'protected_files':preservation['files'],
            'resolved_failures_remain_preserved':resource_failures,
            'report_status_sha256':digest(ROOT/'results/report_status.json'),
            'evidence_audit_sha256':digest(ROOT/'provenance/evidence_audit_final.json'),
            'preservation_sha256':digest(ROOT/'provenance/preservation_latest.json'),
            'delivered_documents':{name:digest(ROOT/name) for name in documents},
            'python_syntax_and_source_manifest':syntax,'existing_local_document_links':len(links),
            'scope':'Final artifact/provenance/preservation audit; not a continuous numerical certificate'}
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:
        json.dump(record,f,indent=2);f.write('\n')
    print(json.dumps({'passed':record['passed'],'errors':errors,'output':str(output)}))
    if errors:
        raise SystemExit(2)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    main(parser.parse_args())
