"""Independent parser and inference audit; no producer code imported."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import bisect,json,hashlib,re
root=Path('research/dynamic_time_comparison');out=root/'verification';cols=['tau','c','cw','cx','a0s','rt1','rt10','rt100','rtall','bt','bc','ec','A1','A3','K','b3','b3p','T'];compare=['c','a0s','ec','bc','rt1','b3'];tags=['drA2_C3_N64','drA2_C3_N64_halfdt'];data={};sources={}
for tag in tags:
 p=out/(tag+'.log');text=p.read_text();rows=[]
 for line in text.splitlines():
  if not line.strip() or line.startswith('#'):continue
  w=line.split('|')[0].split()
  assert len(w)==18,(tag,line)
  rows.append(dict(zip(cols,map(F,w))))
 assert all(a['tau']<b['tau']for a,b in zip(rows,rows[1:]))
 dt=F(re.search(r'dtau ([0-9.e+-]+)',text).group(1));data[tag]=rows;sources[tag]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'first_logged_step':str(dt),'rows':len(rows),'first_tau':str(rows[0]['tau']),'last_tau':str(rows[-1]['tau'])}
def interp(rows,t):
 i=bisect.bisect_left([r['tau']for r in rows],t)
 if i<len(rows) and rows[i]['tau']==t:return dict(values=rows[i],bracket=[t,t],weight=F(0),left=rows[i],right=rows[i])
 assert 0<i<len(rows);a,b=rows[i-1:i+1];lam=(t-a['tau'])/(b['tau']-a['tau']);values={k:(1-lam)*a[k]+lam*b[k]for k in cols}
 return dict(values=values,bracket=[a['tau'],b['tau']],weight=lam,left=a,right=b)
records=[];checks=0
for t in map(F,[0,5,10,15,20]):
 parts={tag:interp(data[tag],t)for tag in tags};comparison={}
 for col in compare:
  a,b=[parts[tag]['values'][col]for tag in tags];comparison[col]={'absolute_difference':str(abs(a-b)),'relative_to_smaller_step':str(abs(a-b)/abs(b))if b else None,'full_value':str(a),'smaller_value':str(b)}
 for tag,p in parts.items():
  a,b=p['left'],p['right'];lam=p['weight'];observed=p['values']['c']*p['values']['a0s']-((1-lam)*a['c']*a['a0s']+lam*b['c']*b['a0s']);predicted=-lam*(1-lam)*(b['c']-a['c'])*(b['a0s']-a['a0s']);assert observed==predicted;checks+=1
  p['cA_interpolation_identity']={'exact_difference':observed,'predicted':predicted,'interpolated_cA_plus2':p['values']['c']*p['values']['a0s']+2}
 records.append(dict(tau=t,parts=parts,comparison=comparison))
# Compare printed table to independent rational interpolation at its printed accuracy.
current=None
for line in (out/'drA2_C3_N64_dtcheck.txt').read_text().splitlines():
 if line.startswith('--- '):current=line[4:].strip();continue
 if current and line.strip():
  words=line.split();assert len(words)==3
  t=F(words[0]);record=next(r for r in records if r['tau']==t)
  for tag,v in zip(tags,words[1:]):
   exact=record['parts'][tag]['values'][current];rounded=F(v);exp=int(v.lower().split('e')[1]);tol=F(1,2)*F(10)**(exp-6)
   assert abs(exact-rounded)<=tol*F(100001,100000),(t,current,tag,exact,rounded,tol);checks+=1
# Manufactured rational interpolation identity over independent endpoints.
for n in range(1,100):
 a0=F(n,7);a1=F(4-n,11);b0=F(2*n+1,13);b1=F(3-n,17);l=F(n,101)
 assert ((1-l)*a0+l*a1)*((1-l)*b0+l*b1)-((1-l)*a0*b0+l*a1*b1)==-l*(1-l)*(a1-a0)*(b1-b0);checks+=1

def pack(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {k:pack(x)for k,x in v.items()}
 if isinstance(v,list):return list(map(pack,v))
 return v
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':checks,'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sources':sources,'first_logged_step_ratio':str(F(sources[tags[0]]['first_logged_step'])/F(sources[tags[1]]['first_logged_step'])),'records':pack(records),'scope':'Exact rational parsing of printed finite diagnostics and interpolation, not an independent trajectory computation.'};(out/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# DR time-comparison log audit','',result['utc'],'','CONFIRMED reproduction of the published interpolation table. Printed first steps are0.093645 and0.045, ratio2.081, rather than exactly2. The table linearly interpolates separately logged diagnostics, using printed four-decimal time stamps. No same-time field comparison or order of convergence is established.','', '| tau | column | full-step interpolant | smaller-step interpolant | absolute difference | relative difference |', '|---:|:---|---:|---:|---:|---:|']
for r in records:
 for col,z in r['comparison'].items():lines.append(f"| {float(r['tau']):g} | {col} | {float(F(z['full_value'])):.9g} | {float(F(z['smaller_value'])):.9g} | {float(F(z['absolute_difference'])):.7g} | {float(F(z['relative_to_smaller_step'])) if z['relative_to_smaller_step'] else 0:.7g} |")
lines+=['','| tau | run | bracket | weight | interpolated c A +2 | pure interpolation contribution |','|---:|:---|:---|---:|---:|---:|']
for r in records:
 for tag,p in r['parts'].items():
  z=p['cA_interpolation_identity'];lines.append(f"| {float(r['tau']):g} | {tag} | {list(map(float,p['bracket']))} | {float(p['weight']):.8g} | {float(z['interpolated_cA_plus2']):.8g} | {float(z['predicted']):.8g} |")
lines+=['','The interpolation identity is exact for every printed endpoint pair and99 manufactured rational tests. It explains most of the artificial c A drift of the interpolated table. Residual endpoint rounding is retained. No measured curvature bound controls interpolation error; one refinement pair does not identify a convergence order. The rt1 column remains the producer unprojected G diagnostic, subject to result167. The finite table does not establish well-posedness, state convergence or a decisive endpoint.']
(out/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='records'}))
