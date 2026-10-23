from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,math
R=Path('research/hydrostatic_velocity_table_repair');V=R/'verification';O=Path('research/hydrostatic_velocity_sequence_audit/verification');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
a=json.loads((V/'ADAPTIVE.json').read_text());g=json.loads((V/'CHECKS.json').read_text());raw=json.loads((O/'RUN.json').read_text());ref=json.loads((O/'REFINEMENT.json').read_text());power=json.loads((O/'ADAPTIVE_POWER_MANUFACTURE.json').read_text());gauss=json.loads((O/'ADAPTIVE_MANUFACTURE.json').read_text())
for j,n in [(a,29),(g,555),(power,243),(gauss,54)]:ck('prior gate '+str(n),j['status']=='PASS'and len(j['checks'])==n and all(x['passed']for x in j['checks']))
ck('adaptive proof binding',a['proof_sha256']==sha(R/'ADAPTIVE_PROOF.md'));ck('adaptive driver binding',a['driver_sha256']==sha('independent_code/audit_velocity_table_adaptive.py'))
for j in [a,power,gauss]:ck('adaptive module '+str(j['count']),j['module_sha256']==sha('independent_code/adaptive_hydrostatic_velocity.py'))
ck('fresh text extraction binding',g['driver_sha256']==sha('independent_code/check_hydrostatic_velocity_table_repair.py')and g['proof_sha256']==sha(R/'PROOF.md'))
ck('fixed raw binding',a['raw_sha256']==sha(O/'RUN.json'));ck('fixed refined binding',a['refinement_sha256']==sha(O/'REFINEMENT.json'))
pmap={s['tag']:s['p']for s in raw['states']};adaptive={(s['tag'],q['index']):q for s in a['states']for q in s['points']};fine={s['tag']:{q['index']:q for q in s['levels'][-1]['points']}for s in ref['states']};rows=[]
ck('ten adaptive witnesses',len(adaptive)==10)
for d in g['disagreements']:
 q=adaptive[d['tag'],d['index']];p=pmap[d['tag']];w=(1+q['x'])**p;v=q['V'][0]/w;error=q['estimated_error'][0]/w;gap=max(F(0),abs(F(str(v))-F(d['printed']))-F(d['half_unit']));delta=abs(v-d['value'])
 ck('axis '+str((d['tag'],d['index'])),q['x']==q['r']==d['r'] and q['y']==0 and q['V'][1]==0)
 ck('finite '+str((d['tag'],d['index'])),math.isfinite(v)and math.isfinite(error))
 ck('no warning '+str((d['tag'],d['index'])),not q['messages'])
 ck('independent agreement '+str((d['tag'],d['index'])),delta<1e-10,delta)
 ck('gap exceeds discrepancy and error '+str((d['tag'],d['index'])),float(gap)>1000*max(delta,error),dict(gap=str(gap),difference=delta,estimated_error=error))
 rows.append(dict(tag=d['tag'],r=q['r'],index=d['index'],p=p,printed=d['printed'],fixed128=d['value'],adaptive=v,weighted_method_difference=delta,weighted_estimated_error=error,outside_rounding_interval_by=str(gap),correctly_rounded=format(v,'+.5f')))
ck('only x-axis disagreements',all(d['kind']=='axis'and d['component']==0 for d in g['disagreements']))
ck('all pair and scales reproduced',all(d['agrees']for d in g['comparisons']if d['kind']!='axis'))
ck('all y-axis tokens reproduced',all(d['agrees']for d in g['comparisons']if d['kind']=='axis'and d['component']==1))
ck('14 numerical changes',len(g['changes'])==14)
ck('ten new mismatches',len(rows)==10 and all(x['changed']for x in g['disagreements']))
j=dict(status='PASS',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,witnesses=rows,max_weighted_method_difference=max(r['weighted_method_difference']for r in rows),max_weighted_estimated_error=max(r['weighted_estimated_error']for r in rows),min_rounding_gap=min(float(F(r['outside_rounding_interval_by']))for r in rows),source_sha256={str(p):sha(p)for p in [V/'ADAPTIVE.json',V/'CHECKS.json',O/'ADAPTIVE_POWER_MANUFACTURE.json',O/'ADAPTIVE_MANUFACTURE.json',O/'RUN.json',O/'REFINEMENT.json']},proof_sha256=sha(R/'ADAPTIVE_PROOF.md'),driver_sha256=sha(__file__),scope='Empirical auxiliary inverse evidence, no certified errors or convergence; fullplaneUNRESOLVED')
(V/'ADAPTIVE_SUMMARY.json').write_text(json.dumps(j,indent=2)+'\n');print('PASS',len(checks),'maxdiff',j['max_weighted_method_difference'],'maxestimate',j['max_weighted_estimated_error'],'mingap',j['min_rounding_gap']);print(json.dumps(rows,indent=2))
