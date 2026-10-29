"""Read-only primary CSV audit; freeze inputs and write only in this lane."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import ast, csv, hashlib, io, json, math, time
R=Path(__file__).resolve().parent.parent
now=datetime.now(timezone.utc); stamp=now.strftime('%Y%m%dT%H%M%S.%fZ')
out=R/'report_audits'/('stage1_counts_'+stamp);out.mkdir()
files={'FAILURE_MAP.csv':R.parent/'e4-num/axisymmetric_euler_24h/FAILURE_MAP.csv',
       'primary_problem.py':R.parent/'e4-num/axisymmetric_euler_24h/src/axi/problem.py',
       'primary_failure_map.py':R.parent/'e4-num/axisymmetric_euler_24h/scripts/failure_map.py',
       'lead_counts.py':R.parent/'e4-lead/checks/stage1_counts.py',
       'lead_counts_output.json':R.parent/'e4-lead/checks/stage1_counts_output.json',
       'lead_FINAL_REPORT.md':R.parent/'e4-lead/FINAL_REPORT.md'}
manifest={};checks=[]
def check(name,ok):
 checks.append({'name':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
for name,p in files.items():
 b=p.read_bytes();(out/name).write_bytes(b)
 check('stable input '+name,hashlib.sha256(b).digest()==hashlib.sha256(p.read_bytes()).digest())
 manifest[name]={'source':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
rows=list(csv.DictReader(io.StringIO((out/'FAILURE_MAP.csv').read_text())))
check('unique job IDs',len({r['job_id'] for r in rows})==len(rows))
main=[r for r in rows if r['stage']=='I'];counts=Counter(r['failure_class']for r in main)
def finite(x):
 try:v=float(x)
 except ValueError:return None
 return v if math.isfinite(v)else None
keep=[]
for r in main:
 check('target starting exponent '+r['job_id'],.5<float(r['cl_start'])<.75)
 core,far=finite(r['s_core']),finite(r['s_far'])
 retained=core is not None and far is not None and core>=.05 and far>=.05
 check('F1 versus magnitude filter '+r['job_id'],(r['failure_class']=='F1')==(not retained))
 if retained:
  check('retained finite residual '+r['job_id'],finite(r['rho_max'])is not None)
  keep.append(r)
per={}
for r in keep:
 c=r['cl_start']
 if c not in per or float(r['rho_max'])<float(per[c]['rho_max']):per[c]=r
free=[r for r in main if r['free_cl']=='True'];ranges={}
for r in free:
 d=ranges.setdefault(r['cl_start'],[]);d.append(float(r['cl_final']))
# Bounds are read using Python's parser, without importing or executing primary code.
bounds=[]
for n in ast.walk(ast.parse((out/'primary_problem.py').read_text())):
 if isinstance(n,ast.AnnAssign) and isinstance(n.target,ast.Name) and n.target.id=='cl_bounds':bounds.append(ast.literal_eval(n.value))
check('unique configured exponent bounds',bounds==[(.501,.749)])
lo,hi=bounds[0];low=[r['job_id']for r in free if abs(float(r['cl_final'])-lo)<1e-10];high=[r['job_id']for r in free if abs(float(r['cl_final'])-hi)<1e-10]
lead=json.loads((out/'lead_counts_output.json').read_text())
check('lead main count',len(main)==lead['stage_I_runs']==311)
check('lead classes',dict(counts)==lead['stage_I_failure_class']=={'F1':214,'F7':74,'F6':19,'F5':4})
check('lead retained count',len(keep)==lead['stage_I_swirl_retaining']==97)
check('lead free count',len(free)==len(lead['stage_I_free_cl'])==43)
check('bound counts',len(low)==1 and len(high)==6)
for c,r in per.items():
 lr=lead['min_rho_swirl_retaining_by_cl_start'][c]
 for key in ['job_id','dominant_eq']:check('lead minimum '+c+' '+key,r[key]==lr[key])
 for key in ['rho_max','s_core','s_far']:check('lead minimum '+c+' '+key,float(r[key])==lr[key])
phase1end=datetime(2026,10,29,0,59,44,tzinfo=timezone.utc)
before=[r for r in main if datetime.fromisoformat(r['finished'].replace('Z','+00:00'))<=phase1end]
retained_before=[r for r in keep if datetime.fromisoformat(r['finished'].replace('Z','+00:00'))<=phase1end]
result={'completed_utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','check_count':len(checks),'all_passed':all(x['passed']for x in checks),'source_rows':len(rows),'stage_labels':dict(Counter(r['stage']for r in rows)),'configuration_stage_I_count':len(main),'configuration_stage_I_finish_range':[min(r['finished']for r in main),max(r['finished']for r in main)],'class_counts':dict(counts),'swirl_magnitude_retained':len(keep),'minima_by_starting_cl':per,'free_cl_count':len(free),'free_cl_ranges':{c:{'count':len(v),'min':min(v),'max':max(v)}for c,v in ranges.items()},'lower_bound_jobs':low,'upper_bound_jobs':high,'real_stage_I_ended_utc':phase1end.isoformat(),'configuration_stage_I_finished_by_real_stage_I_end':len(before),'magnitude_retained_finished_by_real_stage_I_end':len(retained_before),'manifest':manifest,'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'scope':'Primary exported CSV arithmetic and source text only. The stage column is a run classification, not a restriction to completion before the actual seven-hour Stage I boundary. Magnitude retention does not establish B2 stability or an Euler profile. Independent coefficient validation is separate.'}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
lines=[f'# Primary Stage-I-labelled count audit\n\nCompleted {result["completed_utc"]}.\n',f'Method: froze the primary CSV, its classification script, configured c_l bounds, and the lead count/report files with two-read SHA256 checks. Recounted independently using only standard-library CSV, finite-number checks and source-text parsing. No primary program was imported or executed.\n',f'Result: {len(rows)} total CSV rows; {len(main)} labelled stage I, {dict(counts)}; {len(keep)} pass core/far magnitude >=0.05; {len(free)} free-c_l runs, {len(high)} within 1e-10 of0.749 and {len(low)} within1e-10 of0.501. All {len(checks)} checks PASS, including exact agreement of all eight minima and their equation labels with the lead output.\n','| Starting c_l | Minimum primary rho_max | Dominant equation | Job ID |\n|---|---:|---|---|']
for c,r in sorted(per.items(),key=lambda x:float(x[0])):lines.append(f'| {c} | {r["rho_max"]} | {r["dominant_eq"]} | {r["job_id"]} |')
lines.append(f'\nVerdict: CONFIRMED for these frozen primary counts and minima. Scope repair: call the population the Stage-I-labelled sweep (or the sweep begun in Stage I), not a count of runs completed in the first seven campaign hours. The labelled jobs finish from {result["configuration_stage_I_finish_range"][0]} to {result["configuration_stage_I_finish_range"][1]}; only {len(before)} finished by the actual Stage I end00:59:44Z, and {len(retained_before)} of those pass the magnitude filter. This does not change the311/97 arithmetic. F1 agrees row by row with failure of that filter, but the count alone does not establish why the optimizer removed swirl. Core/far magnitude retention is not full B2. The freeze-time final map must be audited again.\n')
(out/'REVIEW.md').write_text('\n'.join(lines))
print(str(out.relative_to(R)));print(json.dumps({k:result[k]for k in ['check_count','source_rows','class_counts','configuration_stage_I_count','swirl_magnitude_retained','free_cl_count','free_cl_ranges','configuration_stage_I_finished_by_real_stage_I_end','magnitude_retained_finished_by_real_stage_I_end']},indent=2))
