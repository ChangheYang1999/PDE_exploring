"""Separate exact witness consumer and finite stage comparison for P248."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,time
import numpy as np
R=Path('research/248_k40_vertex_regional/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prod(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def power(z,n):
 if n<0:
  d=z[0]**2+z[1]**2;z=(z[0]/d,-z[1]/d);n=-n
 out=(Q(1),Q(0))
 while n:
  if n&1:out=prod(out,z)
  z=prod(z,z);n//=2
 return out
def evaluate(poly,x,y,derivative=False):
 out=(Q(0),Q(0))
 for n,c in poly.items():
  n=int(n);v=tuple(map(Q,c))
  if derivative:v=(-n*v[1],n*v[0])
  v=prod(v,power((x,y),n));out=(out[0]+v[0],out[1]+v[1])
 return out
manifest=json.loads((R/'manifest.json').read_text());known={s['sha256']:s for s in manifest['states']}
tail=json.loads((R/'exact_native_tail.json').read_text())
for s in tail['states']:
 src=known[s['archive_sha256']];check('archive',h(R/src['snapshot'])==s['archive_sha256'],src['label'])
 beta=Q(s['beta_exact']);check('exponent_order',1-3/beta>Q(2,3)-2/beta>0>1-4/beta,str(beta))
 for key,w in s['exact_witnesses'].items():
  x,y=Q(w['cos_theta']),Q(w['sin_theta']);check('unit_witness',x*x+y*y==1,[src['label'],key]);val=evaluate(s['coefficients'][key],x,y)
  check('exact_nonzero_witness',val[1]==0 and val[0]==Q(w['exact_value']) and val[0]!=0,[src['label'],key,float(val[0])])
 for axis in s['source_axes']:
  y=Q(axis['sin_theta']);v=evaluate(s['coefficients']['PS0'],Q(0),y);dv=evaluate(s['coefficients']['PS0'],Q(0),y,True)
  check('source_simple_axis_zero',v==(0,0) and dv[1]==0 and dv[0]==Q(axis['PS_derivative']) and dv[0]!=0,[src['label'],str(y),float(dv[0])])

paths=[R/s['snapshot'] for s in manifest['states']]
cf=json.loads((R/'comparators_freeze.json').read_text())
for s in cf['inputs']:check('comparator_archive',h(R/s['snapshot'])==s['sha256'],s['snapshot']);paths.append(R/s['snapshot'])
records=[]
for p in paths:
 with np.load(p,allow_pickle=False)as z:
  a={k:z[k].item() for k in ['beta','lam','K','Nt','a0','strain_mismatch']}
  a.update(file=str(p),sha256=h(p),seed_coefficients_sha256=hashlib.sha256(z['cG_f'].tobytes()).hexdigest(),seed_geometry={k:z[k].item()for k in z.files if k.startswith('seed_') and z[k].shape==()},F0=float(z['cF'].flat[0]),G0=float(z['cG'].flat[0]));records.append(a)
check('common_source',len({a['seed_coefficients_sha256']for a in records})==1 and all(a['seed_geometry']==records[0]['seed_geometry']for a in records))
comparisons=[]
for beta in [3.085,3.1]:
 row=sorted([a for a in records if a['beta']==beta],key=lambda a:a['K']);vals=[a['lam']for a in row];check('three_angular_resolutions', [a['K']for a in row]==[24,32,40],beta);check('finite_lambda_range_below_1e_minus6',max(vals)-min(vals)<=1e-6,[beta,vals]);comparisons.append({'beta':beta,'records':row,'lambda_range':max(vals)-min(vals),'K40_minus_K24':vals[2]-vals[0],'K40_minus_K32':vals[2]-vals[1]})
log=(R/'blamL2B40.out').read_text();stages=[]
for line in log.splitlines():
 if line.startswith('  secant '):
  m=re.search(r'secant (\d+): beta=([\d.]+) lambda=([\d.]+) m=([+\deE.-]+).*iters=(\d+)',line)
  if m:stages.append({'secant':int(m[1]),'beta':float(m[2]),'lambda_rounded':float(m[3]),'m_rounded':float(m[4]),'iterations':int(m[5])})
check('outer_stage_counts',[(b,len([s for s in stages if s['beta']==b]))for b in [3.0925,3.085,3.1]]==[(3.0925,1),(3.085,3),(3.1,3)])
check('inherited_center_one_inner_iteration',stages[0]['secant']==0 and stages[0]['iterations']==1)
slopes=[]
for beta in [3.085,3.1]:
 ss=[s for s in stages if s['beta']==beta];slope=(ss[1]['m_rounded']-ss[0]['m_rounded'])/(ss[1]['lambda_rounded']-ss[0]['lambda_rounded']);slopes.append({'beta':beta,'logged_secant_slope':slope,'scope':'rounded log endpoints; finite secant, not derivative or root'})
consumer=json.loads((R/'center_certificates/checks.json').read_text());mcomparisons=[]
for rec in records:
 if rec['K']!=40:continue
 exact=next(s for s in consumer['checks']if s['sha256']==rec['sha256'])['inverse']['forced']['m'];diff=exact-rec['strain_mismatch'];check('saved_vs_exact_mismatch',abs(diff)<6e-7,[rec['beta'],exact,rec['strain_mismatch'],diff]);mcomparisons.append({'beta':rec['beta'],'saved_m':rec['strain_mismatch'],'exact_m_decimal':exact,'difference':diff})
result={'started_utc':started,'elapsed_seconds':time.monotonic()-t0,'checks':checks,'passed':sum(c['passed']for c in checks),'total':len(checks),'stage_comparisons':comparisons,'secants':stages,'secant_slopes':slopes,'saved_mismatch_comparisons':mcomparisons,'script_sha256':h(__file__),'tail_input_sha256':h(R/'exact_native_tail.json'),'log_input_sha256':h(R/'blamL2B40.out'),'scope':'Exact witness verification and finite logged-stage comparison. No derivative, root, fold, continuum limit or unforced profile is inferred.'}
result['ended_utc']=datetime.now(timezone.utc).isoformat();(R/'tail_stage_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result['passed'],result['total']);print('comparisons',[(r['beta'],r['lambda_range'])for r in comparisons]);print('failures',[c for c in checks if not c['passed']])
