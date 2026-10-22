#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path('research/344_formal_vorticity_factorization/verification');start=datetime.now(timezone.utc).isoformat();names=['n10_r10q26_v3.json','n8_r8q22_v3.json','n5_C2khalf_r4q22_v3.json'];data=[json.loads((D/n).read_text())for n in names];checks=[]
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
for n,a in zip(names,data):ck('passed_'+n,a['passed']==a['total'])
a,b,c=data
for group in ['h','Y_graph']:
 N,M=(8,0)if group=='h'else(8,12)
 def restrict(t):return{k:v for k,v in t.items()if int(k.split(',')[0])<=N and int(k.split(',')[1])<=M}
 ck('same_'+group,restrict(a[group])==restrict(b[group]),{'rmax':N,'qmax':M,'stored_nonzero':len(restrict(b[group]))})
ck('same_resonant_data',a['unit_ode_resonant_data']==b['unit_ode_resonant_data'])
ck('nonresonant_counts',all(t['unit_ode_nonresonant_coefficients']==(t['rmax']+1)*(t['qmax_Y']+1)-len(t['unit_ode_resonant_data'])for t in data))
ck('different_parameter_sign',a['H0']=='1/231'and c['H0']=='-1/29568')
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,input_sha256={n:hashlib.sha256((D/n).read_bytes()).hexdigest()for n in names},code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact common rectangle agreement of two finite independently computed truncations. Different parameter sign checked separately, no convergence.')
(D/'precision_comparison.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if all(x['passed']for x in checks)else 1)
