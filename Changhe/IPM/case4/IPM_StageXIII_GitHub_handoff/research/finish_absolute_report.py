#!/usr/bin/env python3
"""Render a factual absolute-loss report from available recorded JSON only.

Standard library only. No numerical engine, optimizer, candidate writer, or
resource-session mutation is imported. --complete is an explicit finalization
request and refuses missing/partial evidence or a missing preservation audit.
"""
import argparse
import csv
from datetime import datetime
from decimal import Decimal, localcontext
import hashlib
import json
import math
from pathlib import Path
import shlex
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parent
CASES=['stage11','combined','local','global']
LABELS={'stage11':'Stage XI','combined':'Stage XII combined','local':'Stage XII localized','global':'Stage XII global'}


def read(path):
    path=Path(path)
    if not path.exists():return None
    try:return json.loads(path.read_text())
    except (ValueError,OSError):return None


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path,text):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.partial')
    temporary.write_text(text)
    temporary.replace(path)


def num(value,precision=10):
    if value is None:return 'pending'
    try:return format(float(value),'.'+str(precision)+'g')
    except (ValueError,TypeError):return str(value)


def table(headers,rows):
    rows=list(rows)
    if not rows:return 'Pending recorded results.\n'
    return '\n'.join(['| '+' | '.join(str(x).replace('|','\\|') for x in headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(str(x).replace('|','\\|') for x in row)+' |' for row in rows])+'\n'


def csvfile(name,rows):
    rows=list(rows)
    path=ROOT/'tables'/name;path.parent.mkdir(parents=True,exist_ok=True)
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields)
        writer.writeheader();writer.writerows(rows)


def link(relative,label=None):
    return '['+(label or relative)+']('+str(ROOT/relative)+')'


def assessment_dilation(record):
    """Accept an implicit lambda=1 only for the independently archived v1 source."""
    if 'exact_spatial_dilation' in record:return float(record['exact_spatial_dilation'])
    old_source=ROOT/'provenance/source_versions/assess_candidates_v1.py'
    bound=record.get('source_identity',{}).get('new_sources',{}).get('assess_candidates.py')
    if old_source.exists() and bound==sha(old_source):return 1.
    return None


def planned_dilation_assessments():
    records={}
    for path in (ROOT/'provenance').glob('*jobs*.json'):
        if path.name.endswith('.state.json'):continue
        for job in (read(path) or {}).get('jobs',[]):
            if job.get('worker')!='assess_candidates.py':continue
            arguments=job.get('arguments',[])
            if 'evaluate' not in arguments:continue
            def value(option,default=None):
                return arguments[arguments.index(option)+1] if option in arguments else default
            case=value('--case');label=value('--label',case);dilation=float(value('--dilation',1))
            if label and (label not in CASES or dilation!=1):records[label]={'case':case,'dilation':dilation}
    return records


def derivative_variants():
    """Keep original reports and explicit recovery versions side by side."""
    rows=[]
    for case in CASES:
        path=ROOT/'results/derivatives'/case/'checks.json'
        rows.append((case,case,path,read(path) or {}))
    for path in sorted((ROOT/'results/derivatives').glob('*/checks.json')):
        label=path.parent.name
        if label in CASES:continue
        record=read(path) or {}
        for case in CASES:
            if label.startswith(case+'_') and record.get('candidate_sha256')==sha(ROOT/'inputs'/(case+'.json')):
                rows.append((case,label,path,record));break
    return rows


def global_recovery_passed():
    record=read(ROOT/'results/derivatives/global_recovery/checks.json') or {}
    return bool(record.get('completed') is True and record.get('passed') is True
        and record.get('candidate_sha256')==sha(ROOT/'inputs/global.json')
        and record.get('recovery_bindings_unchanged') is True)


def evidence():
    rows=[]
    def add(name,path,completion=None,acceptance=None,expected_dilation=None):
        record=read(ROOT/path)
        complete=bool(record is not None and (record.get(completion) is True if completion else True))
        if complete and expected_dilation is not None:complete=assessment_dilation(record)==expected_dilation
        passed=None if not complete or acceptance is None else record.get(acceptance) is True
        rows.append({'name':name,'path':path,'exists':record is not None,'completed':complete,'passed':passed,
                     'sha256':sha(ROOT/path) if (ROOT/path).exists() else None})
    add('Native field and independent Taylor verification','results/field_tests.json','complete','passed')
    add('Independent manufactured integration references','results/manufactured_tests.json',acceptance='passed')
    add('Actual adaptive integration driver','results/integration_driver_tests.json',acceptance='passed')
    add('Uniform outer-envelope implementation','results/tail_envelope_tests.json',acceptance='passed')
    add('Candidate center and Taylor semantics','results/candidate_semantics.json','completed')
    add('Assessment source-version/timing provenance','provenance/source_versions/assessment_versions.json')
    add('Native/arithmetic/model comparison and fresh old loss','results/arithmetic_comparison.json','completed','passed')
    add('Analytic asymptotic comparisons','results/far_asymptotic_checks.json','completed')
    add('Exact field dilation covariance','results/exact_dilation_checks.json','completed','passed')
    if (ROOT/'absolute_chart_v2.py').exists():
        add('Explicit global v2 coordinate diagnostic','results/chart_diagnostics_v2/global_chart_v2.json','completed','passed')
    if (ROOT/'absolute_derivative_checks_v2.py').exists():
        add('Explicit global v2 derivative recovery','results/derivatives/global_recovery/checks.json','completed','passed')
    for case in CASES:
        add(case+' whole-radius integral','results/integrals/'+case+'.json','finite_whole_axis','numerical_error_checks_passed')
        add(case+' frozen independent grids','results/assessments/'+case+'.json','completed',expected_dilation=1.)
        add(case+' full derivative preparation','results/derivatives/'+case+'/checks.json','completed','passed')
        add(case+' transformed whole-axis residual mesh','results/whole_axis_preparation/'+case+'/preparation.json','completed','passed')
    for dilation in [2,16,256,1024]:
        add('Stage XI exact dilation '+str(dilation),'results/integrals/stage11_lambda_'+str(dilation)+'.json','finite_whole_axis','numerical_error_checks_passed')
    for case,label,path,record in derivative_variants():
        if label!=case and record.get('completed') is True and not any(r['path']==str(path.relative_to(ROOT)) for r in rows):
            add(case+' explicit derivative version '+label,str(path.relative_to(ROOT)),'completed','passed')
    for label,planned in planned_dilation_assessments().items():
        add(label+' fixed-grid exact-dilation assessment','results/assessments/'+label+'.json','completed',expected_dilation=planned['dilation'])
    add('Protected-file audit','provenance/preservation_latest.json',acceptance='passed')
    if global_recovery_passed():
        for row in rows:
            if row['path']=='results/derivatives/global/checks.json' and row['passed'] is False:
                row['resolved_by']='results/derivatives/global_recovery/checks.json'
                row['original_failed_result_preserved']=True
    return rows


def resource_summary():
    records=[];minimum_available=None;minimum_disk=None
    for path in sorted((ROOT/'resource_session/runs').glob('*/result.json')):
        value=read(path)
        if value:records.append(value)
    for path in (ROOT/'resource_session/runs').glob('*/resources.jsonl'):
        for line in path.read_text().splitlines():
            try:row=json.loads(line).get('snapshot',{})
            except ValueError:continue
            if row.get('available_mib') is not None:
                value=row['available_mib'];minimum_available=value if minimum_available is None else min(value,minimum_available)
            if row.get('disk_free_gib') is not None:
                value=row['disk_free_gib'];minimum_disk=value if minimum_disk is None else min(value,minimum_disk)
    return {'finished_jobs':len(records),'worker_returncode_failures':[{'run_id':r.get('run_id'),'returncode':r.get('returncode'),'stop_reasons':r.get('stop_reasons')} for r in records if r.get('returncode')!=0],
            'resource_stops':[r.get('run_id') for r in records if r.get('stop_reasons')],
            'peak_family_rss_mib':max([r.get('peak_family_rss_mib',0) or 0 for r in records],default=0),
            'guarded_wall_seconds':sum(r.get('wall_seconds',0) or 0 for r in records),
            'minimum_available_mib':minimum_available,'minimum_disk_free_gib':minimum_disk}


def commands_document():
    path=ROOT/'provenance/commands.jsonl';lines=[]
    if path.exists():
        for index,line in enumerate(path.read_text().splitlines(),1):
            try:row=json.loads(line)
            except ValueError:continue
            stamp=datetime.fromtimestamp(row['epoch'],ZoneInfo('America/Los_Angeles')).isoformat()
            lines.extend(['### '+str(index)+'. '+stamp,'','Worker SHA-256: `'+row.get('worker_sha256','unrecorded')+'`.','',
                          '```sh',shlex.join(row['command']),'```',''])
    write(ROOT/'EXECUTED_COMMANDS.md','# Executed validation argument vectors\n\n'+
          'These are the exact recorded commands; each runner specifies its independent work and resource-session directory. Completed-run return codes, stdout, stderr and resource telemetry are retained under `resource_session/runs`.\n\n'+'\n'.join(lines))


def reproduction_document():
    root=shlex.quote(str(ROOT));py=shlex.quote('/Users/caltech/research/IPM_R2_macpro_runs/verification_20261020_01/native_venv/bin/python')
    text=f'''# Reproducing the absolute-loss checks

All existing results and resource ledgers are preserved. Numerical workers run
only through the isolated supervisor. No command below launches optimization.
The original Stage XII campaign is a protected read-only input.

## Create a fresh isolated copy

Choose an unused destination outside historical and Stage XII workspaces:

```sh
/usr/bin/python3 -B {root}/create_reproduction_workspace.py \\
  --destination "$HOME/research/IPM_R2_macpro_experiments/stage12_absolute_loss_repeat_01"
export ABS="$HOME/research/IPM_R2_macpro_experiments/stage12_absolute_loss_repeat_01"
export PY={py}
"$PY" -B "$ABS/hardware/guard.py" init \\
  --session-dir "$ABS/resource_session" --disk-path "$ABS" \\
  --policy "$ABS/inputs/resource_policy.json"
/usr/bin/python3 -B "$ABS/preservation.py" snapshot
```

The copy helper preserves source and immutable candidate bytes and updates only
snapshot-location metadata in its new input index. It also copies this guide,
assessment source-version evidence and planned job specifications needed by the
report generator. It copies no prior results, queue states, resource session,
counters, holds or telemetry. The existing native environment
and full Mac Pro verification gate remain required by `launch.py`.

## Independent mathematical, field and integration checks

```sh
/usr/bin/python3 -B "$ABS/launch.py" --label environment environment_probe.py
/usr/bin/python3 -B "$ABS/launch.py" --label fields field_tests.py
/usr/bin/python3 -B "$ABS/launch.py" --label manufactured manufactured_tests.py
/usr/bin/python3 -B "$ABS/launch.py" --label actual_driver integration_driver_tests.py
/usr/bin/python3 -B "$ABS/launch.py" --label tail_envelopes tail_envelope_tests.py
/usr/bin/python3 -B "$ABS/launch.py" --label semantics candidate_semantics.py
/usr/bin/python3 -B "$ABS/launch.py" --label arithmetic arithmetic_comparison.py
/usr/bin/python3 -B "$ABS/launch.py" --label asymptotics far_asymptotic.py
for candidate in stage11 combined local global; do
  /usr/bin/python3 -B "$ABS/launch.py" --label "integral_$candidate" \\
    integrate_candidate.py --case "$candidate" --label "$candidate"
done
for dilation in 2 16 256 1024; do
  /usr/bin/python3 -B "$ABS/launch.py" --label "scale_$dilation" \\
    integrate_candidate.py --case stage11 --label "stage11_lambda_$dilation" --dilation "$dilation"
done
/usr/bin/python3 -B "$ABS/launch.py" --label exact_covariance exact_dilation_checks.py
/usr/bin/python3 -B "$ABS/launch.py" --label combined_scale16 \\
  integrate_candidate.py --case combined --label combined_lambda_16 --dilation 16
```

Frozen assessment coordinates are copied exactly; do not run `freeze` again.
To rebuild coordinates independently, use another fresh copy without the two
absolute-assessment coordinate/design files and run `assess_candidates.py freeze`
through its supervisor before any candidate assessment.

## Independent grids, derivative checks and whole-axis residual preparation

```sh
for candidate in stage11 combined local global; do
  /usr/bin/python3 -B "$ABS/launch.py" --label "assessment_$candidate" \\
    assess_candidates.py evaluate --case "$candidate"
  /usr/bin/python3 -B "$ABS/launch.py" --label "absolute_derivative_$candidate" \\
    absolute_derivative_checks.py --candidate "$ABS/inputs/$candidate.json" \\
    --label "$candidate" --a-ref 23.95065822465609
  /usr/bin/python3 -B "$ABS/launch.py" --label "whole_axis_$candidate" \\
    prepare_whole_axis.py --case "$candidate" --label "$candidate"
done
/usr/bin/python3 -B "$ABS/record_failed_derivative.py"
/usr/bin/python3 -B "$ABS/launch.py" --label global_chart_v2 \\
  chart_diagnostics_v2.py --case global --label global_chart_v2
/usr/bin/python3 -B "$ABS/launch.py" --label global_derivative_v2 \\
  absolute_derivative_checks_v2.py --candidate "$ABS/inputs/global.json" \\
  --geometry-diagnostic "$ABS/results/chart_diagnostics_v2/global_chart_v2.json" \\
  --label global_recovery --a-ref 23.95065822465609
for dilation in 2 16 256 1024; do
  /usr/bin/python3 -B "$ABS/launch.py" --label "dilated_assessment_$dilation" \\
    assess_candidates.py evaluate --case stage11 \\
    --label "stage11_lambda_$dilation" --dilation "$dilation"
done
/usr/bin/python3 -B "$ABS/preservation.py" verify
/usr/bin/python3 -B "$ABS/audit_absolute_evidence.py" --require-complete \\
  --output "$ABS/provenance/evidence_audit_final.json"
/usr/bin/python3 -B "$ABS/finish_absolute_report.py" --complete
/usr/bin/python3 -B "$ABS/closeout_absolute_validation.py" \\
  --output "$ABS/provenance/FINAL_ABSOLUTE_LOSS_AUDIT.json"
```

The original global v1 derivative command is expected to save its failed record
and return status 2 because its inherited normal system is unresolved. Preserve
that record and arrays, then run the separately versioned v2 diagnostic and
recovery commands. The recovery worker refuses to proceed without the matching
passed diagnostic and exact preserved v1 failure/array hashes. No failed record
is overwritten, and no numerical tolerance is relaxed.

The derivative worker's `--full-coefficients` option checks every new raw
coefficient; its default checks all 24 old raw columns, representative new
columns, fixed mixed probes, all nineteen feasible core directions and four
feasible mixed directions. The whole-axis preparation additionally checks
complete `c_l` and two mixed directions across origin, middle and infinity
transformations. These are preparation checks, not stationarity tests.

`ABSOLUTE_LOSS_REPORT.md` can be refreshed as a draft by running the generator
without `--complete`. Final generation above follows all numerical output,
the protected-file check and the independent evidence audit.
Any numerical failure remains visible. The future optimization gate stays
closed without separate neighborhood-wide integration qualification.

For exact commands executed in the original validation, including worker hashes
and timestamps, see [EXECUTED_COMMANDS.md]({ROOT}/EXECUTED_COMMANDS.md) and
`provenance/commands.jsonl`. All logs and resource decisions are retained.
'''
    write(ROOT/'REPRODUCE.md',text)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--complete',action='store_true');args=parser.parse_args()
    records=evidence();pending=[r for r in records if not r['completed']];failed=[r for r in records if r['passed'] is False]
    unresolved=[r for r in failed if not r.get('resolved_by')]
    if args.complete and pending:raise SystemExit('Cannot finalize with pending evidence: '+', '.join(r['name'] for r in pending))
    if args.complete and (read(ROOT/'provenance/preservation_latest.json') or {}).get('passed') is not True:
        raise SystemExit('Cannot finalize without a passing protected-file preservation audit')
    semantics=read(ROOT/'results/candidate_semantics.json') or {}
    arithmetic=read(ROOT/'results/arithmetic_comparison.json') or {}
    index=read(ROOT/'inputs/candidates.json') or {};a_ref=index.get('a_ref')
    cases={k:read(ROOT/'inputs'/(k+'.json')) or {} for k in CASES}
    integrals={k:read(ROOT/'results/integrals'/(k+'.json')) or {} for k in CASES}
    assessments={k:read(ROOT/'results/assessments'/(k+'.json')) or {} for k in CASES}
    assessments={k:v if assessment_dilation(v)==1 else {} for k,v in assessments.items()}
    all_assessments={path.stem:read(path) or {} for path in (ROOT/'results/assessments').glob('*.json')}
    environment=read(ROOT/'results/environment.json') or {};resources=resource_summary()
    session=read(ROOT/'resource_session/session.json') or {};baseline=read(ROOT/'resource_session/session_baseline.json') or {}
    previous_setup=read(ROOT/'provenance/previous_campaign_status_at_setup.json')
    if previous_setup and previous_setup.get('active') is None:
        setup_note='The archived original-validation setup snapshot records the old Stage XII queue as inactive after its earlier endpoint verification failure. This validation neither stopped nor restarted that campaign.'
    else:
        setup_note='This validation contains no command that stops or restarts the old Stage XII campaign; any archived setup snapshot remains separate from current process state.'
    serialization_files=sorted((ROOT/'results').glob('tail_envelope_tests.serialization_failed_run*.json.partial'))
    if serialization_files:
        tail_test=read(ROOT/'results/tail_envelope_tests.json') or {}
        serialization_note=str(len(serialization_files))+' tail-envelope test attempts failed while serializing NumPy boolean values into JSON. Test-only scalar conversions were corrected; numerical kernels and tolerances were unchanged. Their guard logs and truncated artifacts '+', '.join(link(str(p.relative_to(ROOT)),p.name) for p in serialization_files)+' are retained. '
        serialization_note+=('Their computed comparisons were not accepted until the successful complete '+str(len(tail_test.get('checks',[])))+'-check rerun existed.' if tail_test.get('passed') is True else 'Their computed comparisons remain unaccepted until a successful complete rerun exists.')
    else:
        serialization_note='No JSON serialization-failure artifacts are present in this workspace. Any completed nonzero worker exits are retained and listed above.'
    comparison=[]
    baseline_old=cases['stage11'].get('objectives',{}).get('J_joint')
    baseline_abs=integrals['stage11'].get('J_abs_estimate')
    for name in CASES:
        old=cases[name].get('objectives',{}).get('J_joint');absolute=integrals[name].get('J_abs_estimate')
        comparison.append({'candidate':name,'old_J97':old,'J_abs_center_model':absolute,
            'literal_J_abs':integrals[name].get('literal_saved_profile_J_abs','pending'),
            'old_improvement_factor_vs_XI':baseline_old/old if baseline_old and old else None,
            'absolute_improvement_factor_vs_XI':baseline_abs/absolute if baseline_abs and absolute else None,
            'absolute_percent_reduction_vs_XI':100*(1-absolute/baseline_abs) if baseline_abs and absolute else None,
            'integration_error_diagnostic':integrals[name].get('total_error_diagnostic'),
            'integration_checks_passed':integrals[name].get('numerical_error_checks_passed')})
    csvfile('candidate_comparison.csv',comparison)
    regions=[]
    for assessment_label,record in all_assessments.items():
        case=record.get('case',assessment_label)
        dilation=assessment_dilation(record)
        for region,row in record.get('regions',{}).items():
            regions.append({'candidate':case,'assessment_label':assessment_label,'dilation':dilation,
                'assessment_completed':bool(record.get('completed',False) and dilation is not None),'region':region,
                'radius_min':row['radius_min'],'radius_max':row['radius_max'],'points':row['points'],
                'max_abs_Rf':row['max_abs_Rf']['value'],'max_abs_Rf_over_a_ref':row['max_abs_Rf_over_a_ref']['value'],
                'Rf_max_x':row['max_abs_Rf_over_a_ref']['xy'][0],'Rf_max_y':row['max_abs_Rf_over_a_ref']['xy'][1],
                'max_abs_Rrho_over_r_a_ref':row['max_abs_Rrho_over_r_over_a_ref']['value'],
                'density_max_x':row['max_abs_Rrho_over_r_over_a_ref']['xy'][0],'density_max_y':row['max_abs_Rrho_over_r_over_a_ref']['xy'][1],
                'relative_Rf_percent':100*row['relative_Rf_fraction']['value'],
                'relative_Rrho_percent':100*row['relative_Rrho_fraction']['value'],
                'floor_hits_f':row['floor_hits_f'],'floor_hits_rho':row['floor_hits_rho'],
                'direct_density_identity_discrepancy':row['direct_density_minus_y_Rf_max_abs']})
    csvfile('absolute_relative_regions.csv',regions)
    csvfile('radial_bands.csv',[r for r in regions if r['region'].startswith('band_')])
    c5rows=[]
    for case,row in semantics.get('candidates',{}).items():
        interpretations=row.get('interpretations',{});literal=interpretations.get('literal',{});center=interpretations.get('center_chart',{})
        coefficients=center.get('physical_residual_Taylor_coefficients_decimal',{})
        c5rows.append({'candidate':case,'literal_origin_Rf':literal.get('physical_Rf_at_origin_decimal'),
            'literal_origin_strain_defect':literal.get('physical_center_identity_defect_decimal'),
            'center_model_c0_minus_saved_c0':center.get('center_metadata',{}).get('c0_correction'),
            **{k:coefficients.get(k) for k in ['Ex','Ey','D1','D2','D3']},
            'center_model_C5_max_abs':center.get('physical_Rf_C5_max_abs'),
            'historical_C5_tolerance_passed':row.get('center_chart_all_C5_physical_residual_coefficients_pass_1e_minus10')})
    csvfile('taylor_constraints.csv',c5rows)
    dilated_taylor=[]
    base_jets=semantics.get('candidates',{}).get('stage11',{}).get('interpretations',{}).get('center_chart',{}).get('physical_residual_Taylor_coefficients_decimal',{})
    if all(key in base_jets for key in ['Ex','Ey','D1','D2','D3']):
        with localcontext() as context:
            context.prec=100
            for dilation in [1,2,16,256,1024]:
                values={key:Decimal(base_jets[key])/Decimal(dilation)**(2 if key in ['Ex','Ey'] else 4) for key in ['Ex','Ey','D1','D2','D3']}
                maximum=max(abs(value) for value in values.values())
                dilated_taylor.append({'lambda':dilation,**{key:str(value) for key,value in values.items()},
                    'max_abs':str(maximum),'tolerance_passed':maximum<=Decimal('1e-10'),
                    'method':'Analytically scaled independently measured base jets; no refit or fresh high-precision recalculation.'})
    csvfile('dilated_taylor_constraints.csv',dilated_taylor)
    scales=[];old_dilations={}
    covariance=read(ROOT/'results/exact_dilation_checks.json') or {}
    for row in covariance.get('historical_StageXI_fixed_domain_J97_under_exact_dilation',[]):old_dilations[float(row['lambda'])]=row.get('J_joint')
    for dilation in [1,2,16,256,1024]:
        record=integrals['stage11'] if dilation==1 else read(ROOT/'results/integrals'/('stage11_lambda_'+str(dilation)+'.json')) or {}
        value=record.get('J_abs_estimate')
        scales.append({'lambda':dilation,'old_native_fixed_J97':old_dilations.get(float(dilation)),
            'J_abs_center_model':value,'difference_from_lambda1':value-baseline_abs if value is not None and baseline_abs is not None else None,
            'error_diagnostic':record.get('total_error_diagnostic'),'checks_passed':record.get('numerical_error_checks_passed'),
            'whole_axis_estimate_not_exact_finite_rule':True})
    csvfile('scale_invariance.csv',scales)
    stamp=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds')
    final_evidence=read(ROOT/'provenance/evidence_audit_final.json') or {}
    accepted=bool(args.complete and not pending and not unresolved and final_evidence.get('passed') is True and final_evidence.get('complete') is True)
    status=('Final validation accepted; original failures preserved and resolved by separate checks' if accepted else 'Completed validation with unresolved verification failures or audit limitations') if args.complete else 'Validation draft; final generation has not been requested'
    all_literal_infinite=all(semantics.get('candidates',{}).get(name,{}).get('interpretations',{}).get('literal',{}).get('literal_whole_log_radius_integral_diverges_at_origin') is True for name in CASES)
    lines=['# Absolute-residual loss and scale-invariance report','',f'Generated {stamp}, America/Los_Angeles. **{status}.**','',
      'No new optimization was launched. Historical results, the previous Stage XII objective, saved candidates and function spaces remain protected. '+setup_note,'',
      '## Main finding','',
      '**All four literal saved full coefficient vectors, interpreted as analytic potentials, have J_abs = ∞ because their measured physical origin constant is nonzero.** The finite numbers below belong to the separately disclosed center-consistent analytic model; their tiny eliminated-c0 differences and retained five-condition defects are reported below.' if all_literal_infinite else 'Literal-vector versus center-model semantics remain subject to their recorded origin checks.',
      '',
      'The absolute whole-radius quantity changes the interpretation of the old fitting gains. The table compares each definition against its own Stage XI baseline; the two objectives have different definitions, so their raw magnitudes are not directly interchangeable.','',
      table(['Profile','Old J97','Old improvement factor','New J_abs, center model','New improvement factor','New reduction vs XI'],
        [[LABELS[r['candidate']],num(r['old_J97']),num(r['old_improvement_factor_vs_XI'])+'×',num(r['J_abs_center_model']),num(r['absolute_improvement_factor_vs_XI'])+'×',num(r['absolute_percent_reduction_vs_XI'])+'%'] for r in comparison]),
      'A factor below one denotes deterioration. These are saved-checkpoint comparisons without reoptimization, stationarity claims, existence claims, or continuous-error certificates.','']
    if all(integrals[x].get('J_abs_estimate') is not None for x in CASES):
        best=min(CASES,key=lambda x:integrals[x]['J_abs_estimate'])
        lines.extend([f'The smallest measured center-model J_abs among these checkpoints is **{LABELS[best]}**, {num(integrals[best]["J_abs_estimate"])}. Relative residuals remain secondary diagnostics and did not determine this ranking.',''])
        for case in CASES:
            d=read(ROOT/'results/derivatives'/case/'checks.json') or {}
            if d.get('completed') and d.get('passed') is False:
                resolution='The separate global v2 recovery has passed with unchanged physical constraints and tolerances; the original failed report is preserved.' if case=='global' and global_recovery_passed() else 'Any recovery is reported separately; no passing replacement is assumed.'
                lines.extend([f'The initial absolute-loss derivative preparation for {LABELS[case]} failed: {d.get("feasible_chart_failure","see its recorded checks")}. {resolution} Integral-value comparisons remain separate from readiness for optimization.',''])
        combined=next(row for row in comparison if row['candidate']=='combined')
        local=next(row for row in comparison if row['candidate']=='local')
        global_row=next(row for row in comparison if row['candidate']=='global')
        lines.extend([f'The combined checkpoint\'s old {num(combined["old_improvement_factor_vs_XI"])}× gain becomes {num(combined["absolute_improvement_factor_vs_XI"])}× on the absolute primary loss. The localized checkpoint, despite its {num(local["old_improvement_factor_vs_XI"])}× old fitting gain, is {num(1/local["absolute_improvement_factor_vs_XI"])}× worse in J_abs. The global checkpoint retains a {num(global_row["absolute_improvement_factor_vs_XI"])}× absolute improvement. Exact dilations demonstrate the old objective\'s scale sensitivity, but this comparison does not decompose each optimized change into dilation, amplitude and shape or assign a causal fraction to scaling.',''])
    lines.extend(['## Mathematical definition and exact invariance','',
      f'The fixed reference is **a_ref = {repr(a_ref)}**, the positive saved Stage XI amplitude. It never depends on the candidate or dilation.','',
      r'\[J_{\rm abs}=\frac1{\pi a_{\rm ref}^2}\int_0^{\pi/2}\int_{-\infty}^{\infty}|R_f(e^s,\theta)|^2\,ds\,d\theta.\]','',
      r'Under exact dilation, \(\chi_\lambda(X)=\lambda^4\chi(X/\lambda)\), \(\psi_\lambda=\lambda^2\psi(X/\lambda)\), \(\rho_\lambda=\lambda\rho(X/\lambda)\), and \(U_\lambda=\lambda U(X/\lambda)\). Therefore \(R_{f,\lambda}(X)=R_f(X/\lambda)\), and the change of variable \(s\mapsto s-\log\lambda\) proves exact whole-axis invariance. The canonical full-plane inverse, parity, growth exponents, cl and origin amplitude are preserved. No finite-basis refit is used.','',
      'An unshifted finite radial window is generally not invariant. All numerical values below are whole-radius approximations with separately recorded omitted-tail and quadrature diagnostics. The mathematical integral is exactly invariant; a finite quadrature rule is not asserted to be exactly invariant. See '+link('MATHEMATICAL_DERIVATION.md')+'.','',
      '## Literal saved vectors and the finite center-model interpretation','',
      r'For literal stored full coefficient vectors, \(R_f(0)=a_0(c_l-1+\psi_{xy}(0))\). A nonzero constant gives \(\int |R_f|^2dr/r=+\infty\) at the origin, however small its coefficient. All literal profiles are reported separately rather than silently removing their center defect.','',
      'The finite comparison retains saved cl, all 23 independent historical core coefficients and every extra coefficient, and defines the originally eliminated c0 by its exact analytic center identity. This is a separately disclosed constrained-model interpretation. Its tiny c0 difference is recorded; no saved candidate is overwritten or exported as a replacement. The old J97 uses the untouched historical rounded-exponent and stabilized-residual convention. The new analytic potential uses unrounded exponents and complete physical derivatives.','',
      table(['Profile','Literal Rf(0)','Literal whole-axis J_abs','Center-model c0 minus saved c0'],[[LABELS[r['candidate']],num(r['literal_origin_Rf']), '∞' if semantics.get('candidates',{}).get(r['candidate'],{}).get('interpretations',{}).get('literal',{}).get('literal_whole_log_radius_integral_diverges_at_origin') else 'see record',num(r['center_model_c0_minus_saved_c0'])] for r in c5rows]),
      'The ideal constrained model imposes all five compatibility equations exactly. Saved binary64 checkpoints retain the following measured degree-two/four defects; they are integrable at zero, are not silently set to zero, and are assessed against the unchanged 1e-10 historical tolerance.','',
      table(['Profile','Ex','Ey','D1','D2','D3','Maximum','Tolerance passed'],[[LABELS[r['candidate']],*[num(r[k]) for k in ['Ex','Ey','D1','D2','D3']],num(r['center_model_C5_max_abs']),str(r['historical_C5_tolerance_passed'])] for r in c5rows]),
      'For exact Stage XI dilations, residual covariance gives Ex/Ey divided by lambda² and D1/D2/D3 divided by lambda⁴. These are **analytically scaled independently measured base jets**, not fresh high-precision evaluations or fitted coefficients. The center constant remains zero in the center model; the nonzero literal constant is unchanged, so every literal dilation still has infinite whole-axis loss.','',
      table(['Stage XI dilation','Ex','Ey','D1','D2','D3','Maximum','1e-10 tolerance passed'],[[str(r['lambda']),*[num(r[key]) for key in ['Ex','Ey','D1','D2','D3']],num(r['max_abs']),str(r['tolerance_passed'])] for r in dilated_taylor]),
      'Full decimal strings and the analytic scaling method are retained in '+link('tables/dilated_taylor_constraints.csv')+'.','',
      'Full Decimal coefficients, literal and center-model Taylor series, physical parameter bounds and amplitude values are in '+link('results/candidate_semantics.json')+'.','',
      'The separate arithmetic audit reruns the original historical objective with each checkpoint\'s exact saved summation groups and compares three views: native rounded literal fields, unrounded literal analytic fields, and the analytic center model. These comparisons retain the literal physical residual rather than replacing it by the stabilized fitting reaction. Native-to-unrounded differences include exponent rounding, derivative arithmetic and summation order; they are not attributed solely to one operation.',''])
    arithmetic_rows=[];arithmetic_differences=[]
    if arithmetic.get('completed'):
        for name,value in arithmetic.get('candidates',{}).items():
            original=value['original_objective']
            arithmetic_rows.append([LABELS[name],num(original['saved']['J_joint']),num(original['fresh']['J_joint']),num(original['J_joint_difference']),num(original['unchanged_historical_comparison_tolerance']),str(original['passed']),str(original['native_derived_c0_exactly_matches_saved'])])
            regions_a=value.get('regions',{})
            differences=[]
            for pair in ['native_literal__to__unrounded_literal','unrounded_literal__to__analytic_center_chart']:
                differences.append(max((r['comparisons'][pair]['Rf']['max_absolute_difference'] for r in regions_a.values()),default=0))
            arithmetic_differences.append([LABELS[name],num(differences[0]),num(differences[1])])
    lines.extend([table(['Profile','Saved old J97','Fresh old J97','Difference','Unchanged tolerance','Passed','Native c0 matches saved'],arithmetic_rows),
      table(['Profile','Largest sampled |ΔRf| native → unrounded','Largest sampled |ΔRf| unrounded → center model'],arithmetic_differences),
      'Every field discrepancy, relative comparison floor, physical origin defect and finite-region absolute integral is retained in '+link('results/arithmetic_comparison.json')+' and its hashed arrays. Those finite-region integrals are never labeled whole-axis values.','',
      '## Whole-radius integration and error diagnostics','',
      'Integration uses unnormalized ds dtheta weights. Near zero, independent Cartesian Decimal binomial expansions are integrated analytically and checked by order refinement and direct overlap. The interval expands outward until its separately derived uniform field envelope is small enough or the declared maximum is reached. Composite radial Gauss rules, angular trapezoids and an independent angular Gauss rule are compared.','',
      table(['Profile','J_abs estimate','Origin order difference','Radial refinement','Angular refinement','Outer envelope','Total diagnostic','Numerical checks'],[[LABELS[k],num(v.get('J_abs_estimate')),num(v.get('origin_tail_error_estimate')),num(v.get('radial_quadrature_error_estimate')),num(v.get('angular_quadrature_error_estimate')),num(v.get('infinity_integral_upper_envelope')),num(v.get('total_error_diagnostic')),str(v.get('numerical_error_checks_passed','pending'))] for k,v in integrals.items()]),
      'The outer envelope is a uniform analytic inequality evaluated in ordinary binary64, using coefficient-absolute bounds, harmonic and Legendre derivative bounds, and polynomial-Gaussian local envelopes. It assumes no fitted asymptotic cancellation. It is not an outward-rounded interval certificate. The independent leading asymptotic coefficient and shell tests are diagnostics, not uniform remainder bounds.','',
      'Origin remainder and quadrature errors are numerical refinement estimates. **No rigorous continuous whole-axis error enclosure is claimed.** The reported error budget and any failed check are explicit in each '+link('results/integrals','integral JSON/NPZ directory')+'. Exact definitions and constructive tail formulas are in '+link('MATHEMATICAL_DERIVATION.md')+' and '+link('tail_envelope.py')+'.','',
      '## Exact dilation checks','',
      table(['Stage XI dilation','Old fixed-domain J97','J_abs estimate','Difference from λ=1','Error diagnostic','Numerical checks'],[[str(r['lambda']),num(r['old_native_fixed_J97']),num(r['J_abs_center_model']),num(r['difference_from_lambda1']),num(r['error_diagnostic']),str(r['checks_passed'])] for r in scales]),
      'Each dilation evaluates the exact functions at X/lambda and rescales their derivatives. No old-basis approximation or refit occurs. Direct quotient and independently assembled density covariance, as well as origin and axis cases, are recorded in '+link('results/exact_dilation_checks.json')+'. Manufactured tests also include a deliberate fixed-window noninvariance example and rejection of a nonzero 1e-30 center constant.',''])
    covariance_rows=[]
    if covariance.get('completed'):
        for name,record in covariance.get('candidates',{}).items():
            checks=record.get('checks',[])
            covariance_rows.append([LABELS[name],', '.join(num(row['lambda']) for row in checks),
                num(max((row['stable_center_Rf_covariance_per_a_ref'] for row in checks),default=None)),
                num(max((row['physical_formula_Rf_covariance_per_a_ref'] for row in checks),default=None)),
                num(max((row['density_covariance_error_divided_by_r_a_ref'] for row in checks),default=None)),str(record.get('passed'))])
    lines.extend([table(['Profile','Exact dilation factors','Largest stable Rf covariance error/a_ref','Largest direct Rf error/a_ref','Largest density error/(r a_ref)','Passed'],covariance_rows),
      'Covariance acceptance uses absolute residual errors with the recorded term-sum roundoff allowance, rather than relative error against a vanishing Taylor residual. This function-level test and the independently tail-controlled integral tests have different purposes.','',
      '## Absolute sampled maxima and separate relative diagnostics','',
      r'The primary sampled quantities are \(a_{\rm ref}^{-1}|R_f|\) and \(a_{\rm ref}^{-1}|R_\rho|/r\). Exact continuous suprema are dilation invariant; these numerical values are **sampled maxima only**, with locations, and are not rigorous continuous supremum upper bounds.',''])
    maximum_rows=[]
    for name,record in assessments.items():
        if not record.get('completed'):maximum_rows.append([LABELS[name],'pending','pending','pending','pending','pending']);continue
        q=record['dense_sampled_E_infinity'];d=record['dense_sampled_density_E_infinity']
        raw_max=max((row['max_abs_Rf']['value'] for row in record['regions'].values()),default=None)
        maximum_rows.append([LABELS[name],num(raw_max),num(q['value']),'('+', '.join(num(x) for x in q['xy'])+')',num(d['value']),'('+', '.join(num(x) for x in d['xy'])+')'])
    lines.extend([table(['Profile','Sampled raw max |Rf|','Sampled max |Rf|/a_ref','Location (x,y)','Sampled max |Rρ|/(r a_ref)','Location (x,y)'],maximum_rows),
      'The same original 30 frozen regions and two new predetermined large-radius grids carry both absolute and historical term-sum-relative diagnostics. The relative columns apply the historical formulas to the explicitly selected analytic center model; native field differences and the freshly reproduced old objective are kept separate above. The added dense log grid reaches 1e8; the additional large-radius grid reaches 1e12. Candidate amplitude appears only in the historical relative floor, never in J_abs or its absolute maxima.','',
      table(['Profile','Region','|Rf|/a_ref max','|Rρ|/(r a_ref) max','Relative Rf %','Relative Rρ %'],[[LABELS[r['candidate']],r['region'],num(r['max_abs_Rf_over_a_ref']),num(r['max_abs_Rrho_over_r_a_ref']),num(r['relative_Rf_percent']),num(r['relative_Rrho_percent'])] for r in regions if r['assessment_completed'] and r['dilation']==1 and r['region'] in ['true_H65','hires_exterior193','absolute_dense_log_radius','absolute_unseen_large_radius']]),
      'Radial-band values on the unchanged historical bands:','',
      table(['Profile','Band','|Rf|/a_ref max','|Rρ|/(r a_ref) max','Relative Rf %','Relative Rρ %'],[[LABELS[r['candidate']],r['region'],num(r['max_abs_Rf_over_a_ref']),num(r['max_abs_Rrho_over_r_a_ref']),num(r['relative_Rf_percent']),num(r['relative_Rrho_percent'])] for r in regions if r['assessment_completed'] and r['dilation']==1 and r['region'].startswith('band_')]),
      'Fixed physical-grid diagnostics for exact dilations (these fixed-grid sampled maxima need not be exactly invariant):','',
      table(['Profile','Dilation','Region','|Rf|/a_ref max','|Rρ|/(r a_ref) max','Relative Rf %','Relative Rρ %'],[[LABELS[r['candidate']],num(r['dilation']),r['region'],num(r['max_abs_Rf_over_a_ref']),num(r['max_abs_Rrho_over_r_a_ref']),num(r['relative_Rf_percent']),num(r['relative_Rrho_percent'])] for r in regions if r['assessment_completed'] and r['dilation']!=1 and r['region'] in ['true_H65','absolute_dense_log_radius','absolute_unseen_large_radius']]),
      'Every region, absolute location, independent direct-density identity discrepancy, floor hit and point count is retained in '+link('tables/absolute_relative_regions.csv')+' and '+link('results/assessments','assessment JSON/CSV files')+'.','',
      'Early assessments bind the original v1 source at execution. After the optional dilation/label interface was added, the exact v1 was recovered from the previous patch and SHA-verified against those recorded identities. A missing explicit dilation is interpreted as one only with that verified v1 binding. The corrected archival timing and source versions are retained in '+link('provenance/source_versions/assessment_versions.json')+'. Existing outputs were preserved; the default numerical field formulas remain unchanged.','',
      '## Prepared residual vector, Jacobian and future optimization boundary','',
      r'For fixed positive quadrature weights, \(z_i=\sqrt{2w_i/(\pi a_{\rm ref}^2)}R_f(X_i)\), so \(\frac12\|z\|^2\) equals the quadrature approximation to J_abs. The Jacobian includes explicit transport and reaction dependence on cl, old and new radial exponents, all spatial fields, eliminated c0 and the implicit five-condition chart. All nineteen feasible core directions and every extra coefficient remain available. No gauge or explicit scaling-direction projection is imposed; the selected finite potential span need not itself be closed under exact spatial dilation.','',
      'A separate fixed positive three-block mesh represents origin, finite middle interval and the entire compactified infinite tail. Coarse/refined values are compared against the independently validated integral. No value-only tail correction is added while omitting its derivative. A matrix-free Jv/JT interface is prepared; it has not been selected for performance or used in optimization.',''])
    derivative_rows=[];geometry_rows=[];derivative_error_rows=[];geometry_csv=[];derivative_failures=[]
    for name,variant,path,d in derivative_variants():
        w=read(ROOT/'results/whole_axis_preparation'/name/'preparation.json') or {}
        display=LABELS[name]+(' ['+variant+']' if variant!=name else '')
        derivative_rows.append([display,str(d.get('completed',False)),str(d.get('passed')) if d.get('completed') else 'pending',str(len(d.get('raw_checks',[]))),str(len(d.get('feasible_checks',[]))),str(d.get('all_extra_coefficients_directly_FD_checked','pending')),str(w.get('completed',False)),str(w.get('passed')) if w.get('completed') else 'pending'])
        if d.get('completed') and d.get('passed') is False:
            resolution='Resolved by separate global v2 PASS; original remains FAIL' if name=='global' and variant==name and global_recovery_passed() else 'No passing recovery recorded'
            derivative_failures.append([display,str(sum(row.get('passed') is True for row in d.get('raw_checks',[])))+'/'+str(len(d.get('raw_checks',[]))),str(len(d.get('feasible_checks',[]))),d.get('feasible_chart_failure','See individual failed checks'),resolution])
        if d.get('completed') and d.get('core_geometry'):
            g=d['core_geometry']
            core_steps=[s for row in d.get('feasible_checks',[]) if row['direction'].startswith('feasible_core_') for s in row['steps'] if s.get('completed')]
            feasible_steps=[s for row in d.get('feasible_checks',[]) for s in row['steps'] if s.get('completed')]
            max_h=max((s['step'] for s in core_steps),default=None)
            hp_max=max((s['maximum_HP_defect'] for s in feasible_steps),default=None)
            linear_scale=g['tangent_constraint_error']*max_h if max_h is not None else None
            geometry_rows.append([display,str(g['complete_24_rank']),num(g['complete_24_condition']),num(g['tangent_constraint_error']),num(max_h),num(linear_scale),num(hp_max)])
            geometry_csv.append({'candidate':name,'variant':variant,'complete_24_rank':g['complete_24_rank'],'complete_24_condition':g['complete_24_condition'],
                'tangent_constraint_derivative_Frobenius':g['tangent_constraint_error'],'max_unscaled_core_FD_step':max_h,
                'tangent_error_times_max_core_step':linear_scale,'maximum_lifted_probe_HP_defect':hp_max})
            raw_steps=[s for row in d.get('raw_checks',[]) for s in row['steps']]
            cl_steps=[s for row in d.get('raw_checks',[]) if row['direction']=='core_0' for s in row['steps']]
            operators=d.get('operator_checks',[])
            derivative_error_rows.append([display,num(max((s['relative_error'] for s in cl_steps),default=None)),
                num(max((s['relative_error'] for s in raw_steps),default=None)),
                num(max((s['relative_error'] for s in feasible_steps),default=None)),
                num(max((max(row['Jv_relative'],row['JT_relative']) for row in operators),default=None)),
                num(max((row['adjoint_scaled'] for row in operators),default=None))])
    csvfile('core_chart_geometry.csv',geometry_csv)
    lines.extend([table(['Profile','Derivative complete','Derivative passed','Raw probes','Feasible probes','Every extra individually FD','Whole-axis preparation complete','Preparation passed'],derivative_rows),
      'Original derivative failures and any explicit recovery reports remain separate. A passing recovery is bound to its own recorded candidate, source and chart; it does not erase the original failed attempt or certify the entire trust neighborhood.','',
      table(['Profile/version','Raw probes passed','Completed feasible probes','Recorded failure','Resolution'],derivative_failures) if derivative_failures else 'No completed derivative report records a failure.',
      '',
      'Two finite-difference step sizes and all individual errors are retained in '+link('results/derivatives','derivative records')+'. Representative new-coefficient checks must not be described as all-coefficient checks. The transformed whole-axis mesh adds complete-cl and mixed probes across all three transformed blocks.','',
      table(['Profile','Complete-cl raw FD error','Worst tested raw FD error','Worst feasible FD error','Worst Jv/JT disagreement','Worst scaled adjoint error'],derivative_error_rows),
      'The original inherited chart is poorly conditioned. Explicit recovery versions, when present, use their separately recorded coordinates and are shown alongside it. The following condition numbers describe the full 24-dimensional completion [T,N] of nineteen tangent columns and five normal columns, rather than the PDE Jacobian. G is the five-condition derivative and T is the actual tangent of that chart version. The norm ||G T|| is a derivative per chart coordinate, not the candidate\'s constraint defect. Multiplication by the actual core-coordinate finite-difference step shows its relevant linearized scale; the outer stencil uses twice that step. Independent high-precision defects are measured on the lifted probes and are distinct from the base-profile defects shown earlier.','',
      table(['Profile','Rank [T,N]','Condition [T,N]','||GT||_F','Largest core h','||GT||_F × h','Max lifted-probe C5 defect'],geometry_rows),
      'All nineteen feasible core columns and every new coefficient are retained. Derivative passes do not establish good conditioning, robust stationarity, or readiness for efficient large-dimensional optimization. The future trust-neighborhood qualification gate remains closed. Geometry values are also in '+link('tables/core_chart_geometry.csv')+'.','',
      'The whole-axis mesh preparation tests raw-cl and mixed physical derivatives, so it can pass even when an inherited implicit feasible chart is unresolved. It does not repair that chart failure.',''])
    chart_recovery=read(ROOT/'results/chart_diagnostics_v2/global_chart_v2.json') or {}
    if chart_recovery.get('completed'):
        geometry=chart_recovery['new_geometry']
        lines.extend(['The separately versioned global chart v2 changes coordinates using all five row-scaled coefficient-gradient singular pairs and all nineteen full-constraint nullspace vectors. Its normal corrections have structurally zero cl component. The base candidate, five equations, tolerances and physical bounds remain unchanged; no singular pair or physical direction is discarded. The independent geometry diagnostic records:','',
          table(['Diagnostic','Recorded result'],[
              ['Original condition of G N',num(chart_recovery['old_G_normal_condition'])],
              ['Unchanged normal-system condition limit','1e10'],
              ['V2 normal-system condition',num(geometry['raw_G_normal_condition'])],
              ['V2 full 24-coordinate condition',num(geometry['complete_24_condition'])],
              ['Row-scaled coefficient singular values',', '.join(num(x) for x in geometry['coefficient_row_scaled_singular_values'])],
              ['Original-to-new tangent map rank',str(chart_recovery['original_to_new_coordinate_rank'])],
              ['Relative tangent-span equivalence error',num(chart_recovery['relative_tangent_span_equivalence_error'])],
              ['All nineteen old feasible directions represented',str(chart_recovery['all_19_original_feasible_directions_represented'])],
              ['Base candidate corrected',str(chart_recovery['base_candidate_corrected'])],
              ['Geometry diagnostic passed',str(chart_recovery['passed'])]]),
          'A geometry diagnostic alone is not an end-to-end feasible derivative pass. Any recovery derivative report is listed separately above; the original failed report remains preserved. Exact arrays and source closure are in '+link('results/chart_diagnostics_v2/global_chart_v2.json')+'.',''])
    mesh_rows=[];block_rows=[];mesh_derivative_rows=[]
    for name in CASES:
        w=read(ROOT/'results/whole_axis_preparation'/name/'preparation.json') or {}
        if not w.get('completed'):continue
        mesh_rows.append([LABELS[name],num(w['coarse_halfnorm_J_abs']),num(w['refined_halfnorm_J_abs']),num(w['validated_J_abs']),num(w['difference_from_validated']),num(w['combined_comparison_diagnostic']),str(w['comparison_passed'])])
        for block,v in w['transformed_block_contributions'].items():
            block_rows.append([LABELS[name],block,num(v['coarse_J']),num(v['refined_J']),num(v['refinement_difference'])])
        for row in w['complete_cl_and_mixed_derivatives']['rows']:
            for step in row['steps']:
                mesh_derivative_rows.append([LABELS[name],row['direction'],num(step['step']),num(step['relative_error']),*[num(step['blocks'][block]['relative_error']) for block in ['origin','middle','infinity']],num(step['blocks']['infinity']['weighted_absolute_error_norm']),str(step['passed'])])
    lines.extend(['The three-block preparation compares actual half-squared residual norms with the independent whole-radius integral:','',
      table(['Profile','Coarse whole-axis J','Refined whole-axis J','Independent J_abs','Difference','Combined diagnostic','Comparison passed'],mesh_rows),
      table(['Profile','Transformed block','Coarse contribution','Refined contribution','Difference'],block_rows),
      'Complete raw-cl and fixed mixed derivative tests cover origin, middle and infinity blocks at both finite-difference steps. Extreme-tail relative errors are reported but are not independent acceptance tests when the weighted derivative is nearly zero; the declared threshold is the overall weighted relative error.','',
      table(['Profile','Direction','FD step','Overall relative error','Origin relative','Middle relative','Infinity relative','Infinity absolute weighted error','Passed'],mesh_derivative_rows),
      'No future optimization is authorized or launched here. The prepared gate requires separate integration qualification throughout a proposed trust neighborhood; isolated saved-profile and derivative passes do not open it. See '+link('OPTIMIZATION_PREPARATION.md')+'.','',
      '## Verification, environment, resources and preservation','',
      table(['Evidence','Completed','Acceptance status'],[[r['name'],str(r['completed']),'FAIL preserved; separate v2 PASS' if r.get('resolved_by') else 'not an acceptance test' if r['passed'] is None and r['completed'] else 'PASS' if r['passed'] is True else 'FAIL' if r['passed'] is False else 'pending'] for r in records]),
      table(['Environment','Recorded value'],[['Host',environment.get('host','pending')],['Architecture',environment.get('machine','pending')],['Platform',session.get('platform','pending')],['Logical CPUs',str(baseline.get('logical_cpus','pending'))],['Total RAM MiB',num(baseline.get('total_mib'))],['Python',environment.get('python','pending')],['NumPy',environment.get('numpy','pending')],['SciPy',environment.get('scipy','pending')],['Nice increment',str(environment.get('nice','pending'))],['BLAS', '; '.join(str(t.get('internal_api'))+' '+str(t.get('version'))+' '+str(t.get('architecture'))+' threads='+str(t.get('num_threads')) for t in environment.get('threadpools',[]))],['Finished guarded jobs',str(resources['finished_jobs'])],['Cumulative guarded wall seconds',num(resources['guarded_wall_seconds'])],['Peak sampled family RSS MiB',num(resources['peak_family_rss_mib'])],['Minimum available RAM MiB',num(resources['minimum_available_mib'])],['Minimum free disk GiB',num(resources['minimum_disk_free_gib'])],['Resource stops',str(len(resources['resource_stops']))]]),
      'Completed worker runs with nonzero exits (including preserved operational failures):','',
      table(['Run','Return code','Resource stop reasons'],[[r['run_id'],str(r['returncode']),str(r['stop_reasons'])] for r in resources['worker_returncode_failures']]),
      serialization_note,'',
      'RSS monitoring is sampled and is not a kernel hard memory cap. No resource limit was raised.','',
      'The preservation audit covers the original source, immutable migration reference, verified deployment, Stage XI research and previous Stage XII campaign, including file hashes, modes, links and nanosecond mtimes. Current audit: '+link('provenance/preservation_latest.json')+'. No ledger or hold is reset. Full resource telemetry is retained in the independent resource session.','',
      '## Reproduction and retained evidence','',
      'Use '+link('REPRODUCE.md')+' for a fresh workspace and guarded checks, '+link('EXECUTED_COMMANDS.md')+' for actual recorded argument vectors and timestamps, and '+link('provenance/commands.jsonl')+' for machine-readable commands. '+link('tables/candidate_comparison.csv')+', '+link('tables/scale_invariance.csv')+', '+link('tables/taylor_constraints.csv')+' and '+link('tables/radial_bands.csv')+' provide machine-readable tables. All numerical arrays, candidate/source hashes, integration meshes and failed/partial artifacts remain separate from historical research.',''])
    if (ROOT/'provenance/evidence_audit_final.json').exists():
        lines.extend(['The final source, array, provenance and completion audit is retained in '+link('provenance/evidence_audit_final.json')+'. This is an artifact audit, not a rigorous continuous numerical certificate.',''])
    if pending:lines.extend(['Pending records at this draft generation: '+', '.join(r['name'] for r in pending)+'.',''])
    if failed:lines.extend(['Preserved original verification failures: '+', '.join(r['name']+(' (resolved by separate v2 PASS)' if r.get('resolved_by') else ' (unresolved)') for r in failed)+'. Their original failed status is retained; no optimization gate is opened.',''])
    write(ROOT/'ABSOLUTE_LOSS_REPORT.md','\n'.join(lines))
    commands_document();reproduction_document()
    snapshot={'schema':'absolute_loss_report_status_v1','generated_los_angeles':stamp,'final_generation_requested':args.complete,
              'evidence':records,'pending':[r['name'] for r in pending],'failed':[r['name'] for r in failed],
              'resolved_failures':[{'name':r['name'],'resolved_by':r['resolved_by']} for r in failed if r.get('resolved_by')],
              'unresolved_failures':[r['name'] for r in unresolved],'final_validation_accepted':accepted,
              'optimization_performed':False,'future_optimization_gate_open':False,'resources':resources}
    write(ROOT/'results/report_status.json',json.dumps(snapshot,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(ROOT/'ABSOLUTE_LOSS_REPORT.md'),'final':args.complete,'pending':len(pending),'failed':len(failed)},indent=2))


if __name__=='__main__':main()
