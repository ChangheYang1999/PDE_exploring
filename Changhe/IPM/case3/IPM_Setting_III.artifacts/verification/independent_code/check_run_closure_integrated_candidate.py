from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
import hashlib,json,re,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/run_closure';V=R/'verification';dest=V/'INTEGRATED_CANDIDATE_CHECKS.json';assert not dest.exists();checks=[];bindings={};observations=[]
def ck(n,b):checks.append(dict(name=n,passed=bool(b)))
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('current identity '+str(p),p.read_bytes()==b and(h is None or h==a));bindings[str(p)]=a;return b
for p in [__file__,R/'PROOF.md',R/'CANDIDATE_TIMING_REPAIR.md',R/'SYNTHESIS_REVIEW_RESOLUTION.md',V/'INTEGRATED_CURATED_INPUTS.json',V/'SOURCE_OBSERVATION.json',V/'NUMERICS_HEADER_CHECK.json']:bind(p)
I=json.loads((V/'INTEGRATED_CURATED_INPUTS.json').read_text())
for ent in I['manifests']:
 d=json.loads(bind(ent['path'],ent['sha256']));ck('prior acceptance '+ent['path'],d['status']==ent['status']and d['count']==ent['count']==len(d['checks'])and all(x['passed']for x in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
 observations.append({k:ent[k]for k in ['path','sha256','status','count']})
for p in I['reading_order']:ck('reading proof exists '+p,Path(p).is_file());bind(p)
syn=V/'SYNTHESIS_INTEGRATED_CANDIDATE.md';text=bind(syn).decode();ck('primary verdict unresolved','**Verdict: UNRESOLVED for the smooth, nondegenerate primary class.**'in text);ck('actual end not invented','Actual T_end: **NOT YET REACHED**'in text);ck('no em dash','\u2014'not in text)
old=json.loads(bind(ROOT/'research/primary_common_mp_sample/verification/CHECKS.json'));fresh=json.loads(bind(ROOT/'research/primary_fresh_sample/verification/CHECKS.json'));direct=json.loads(bind(ROOT/'research/primary_direct_quadrature_spotcheck/verification/CHECKS.json'))
numchecks=[]
def rounded(name,shown,exact):
 e=Decimal(shown).as_tuple().exponent;tol=F(51,100)*(F(10)**e);delta=abs(F(shown)-F(exact));ck('rounded table '+name,delta<=tol);numchecks.append(dict(name=name,shown=shown,exact=str(exact),absolute_difference=float(delta),rounding_tolerance=float(tol)))
for line,row in zip([s for s in text.splitlines()if re.match(r'^\|(36|40|44)\|',s)],old['rows']):
 cells=line.strip('|').split('|');ck('table state '+str(row['N']),int(cells[0])==row['N']);inside=next(a for a in row['extents']if F(a['radius'])==100)
 actual=[row['a_exact'],row['delta_exact'],row['all']['maxima']['R_Nf']['displayed_fields']['R_Nf'],row['all']['maxima']['R_Nv']['displayed_fields']['R_Nv'],inside['maxima']['abs_R']['displayed_fields']['abs_R']]
 for k,shown,true in zip(['a','delta','Rf','Rv','abs_R_r100'],cells[1:],actual):rounded(str(row['N'])+' '+k,shown,true)
ck('three table states',len([s for s in text.splitlines()if re.match(r'^\|(36|40|44)\|',s)])==3)
for row in fresh['rows']:
 for k in ['R_Nf','R_Nv']:ck('fresh maximum index '+str((row['N'],k)),row['all']['maxima'][k]['index']==20)
ck('fresh ratios increase',all(a['all']['maxima'][k]['value']<b['all']['maxima'][k]['value']for a,b in zip(fresh['rows'],fresh['rows'][1:])for k in ['R_Nf','R_Nv']))
ck('direct residual difference bound',max(abs(x['differences']['R'])for x in direct['rows'])<9.12e-14);ck('direct normalized difference bound',max(abs(x['normalized_residual_difference'])for x in direct['rows'])<4.20e-15)
ck('direct three results included',all(format(x['R'],'.10e').replace('e-06','e-6') in text for x in direct['rows']))
log=bind(ROOT/'shifts/shifts.log').decode();t0=datetime.fromisoformat('2026-10-20T12:44:21+00:00');cap=datetime.fromisoformat('2026-10-22T12:44:21+00:00');ck('first shift start',next(x for x in log.splitlines()if re.search(r'shift \d+ start',x)).startswith('2026-10-20T12:44:21Z shift 1 start'));ck('actual48hdeadline',(cap-t0).total_seconds()==172800);ck('currentshift admitted','2026-10-22T07:09:48Z shift 9 start (referee)'in log)
for p,h in bindings.items():ck('stable after check '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
failed=[c['name']for c in checks if not c['passed']];out=dict(status='PASS_CURATED_CLOSURE_CANDIDATE'if not failed else'FAIL_CURATED_CLOSURE_CANDIDATE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,failed=failed,bindings=bindings,accepted_manifests=observations,table_comparisons=numchecks,primary_verdict='UNRESOLVED',scope='Current byte identity for14selected accepted manifests and their bindings, curated reading paths, rounded primary table and scoped finite maxima. Synthesis model review and actual end remain pending.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','failed']},indent=2));raise SystemExit(bool(failed))
