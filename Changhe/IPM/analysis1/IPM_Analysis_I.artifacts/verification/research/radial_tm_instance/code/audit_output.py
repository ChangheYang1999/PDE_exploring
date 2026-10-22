"""Full saved verdict audit and fresh particular-polynomial spot calculation."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,math,sys
import numpy as np
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/radial_tm_instance';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def ends(v):
 assert v.is_finite()
 def cv(z):m,e=z.man_exp();return F(int(m))*F(2)**int(e)
 return cv(v.lower()),cv(v.upper())
def box(m,r):
 m,r=F(float(m)),F(float(r));assert r>=0;return qa(m-r).union(qa(m+r))
def mag(x):a,b=ends(x);return max(abs(a),abs(b))
def particular_weight(j,k,lam,sign):
 if lam==2:
  return F(sign*2**(j-k-1),(k+1)*math.factorial(j-k-1)) if j>=k+1 else F(0)
 qq=[F(sign*(-1)**(k-v)*math.factorial(k),math.factorial(v)*(2-lam)**(k-v+1)) for v in range(k+1)]
 return sum((qq[v]*F(2**(j-v),math.factorial(j-v)) for v in range(min(j,k)+1)),F())-qq[0]*F(lam**j,math.factorial(j))
def poly_derivative_bound(poly,N,h):
 return sum((mag(x)*math.comb(N,v)*2**(N-v)*F(math.factorial(k),math.factorial(k-v))*h**(k-v) for k,x in enumerate(poly) for v in range(min(N,k)+1)),F())
def derivative(q0,Z,FF,lam,sign,N,h):
 if lam==2:
  poly=[q0]+[sign*Z*x/(k+1) for k,x in enumerate(FF)]
  return (2*qa(h)).exp()*qa(poly_derivative_bound(poly,N,h))
 poly=[arb(0) for x in FF]
 for k in range(len(FF)-1,-1,-1):poly[k]=(sign*FF[k]-((k+1)*poly[k+1] if k+1<len(FF) else 0))/(2-lam)
 c=q0-Z*poly[0]
 return abs(lam)**N*(qa(max(lam,0)*h)).exp()*qa(mag(c))+qa(mag(Z))*(2*qa(h)).exp()*qa(poly_derivative_bound(poly,N,h))
obj=json.loads((E/'selected_v3_checks.json').read_text());assert obj['status']=='PASS_LOCAL_RADIAL_ODE_BOXES' and obj['failures']==[] and obj['cells']==[0,4102,7808] and obj['modes']==list(range(1,262)) and obj['Q']==12 and obj['higher_remainder_order']==20
counts=Counter();files={}
for p,v in obj['files'].items():assert sha(p)==v,p;counts['input_and_candidate_pins']+=1
arr={ci:np.load(E/('selected_v3_cell_%04d.npz'%ci)) for ci in obj['cells']}
for ci,data in arr.items():
 old=np.load(E/('selected_v2_cell_%04d.npz'%ci))
 assert set(old.files)==set(data.files)
 for key in data.files:
  assert np.array_equal(data[key],old[key]),(ci,key);counts['unchanged_candidate_arrays']+=1
  assert np.isfinite(data[key]).all();counts['finite_arrays']+=1
  if key.endswith(('_rad','_rem')):assert (data[key]>=0).all();counts['nonnegative_arrays']+=1
seen=set()
for row in obj['records']:
 ci,n,eng=row['cell'],row['n'],row['engine'];key=(ci,n,eng);assert key not in seen;seen.add(key)
 assert row['coefficient_failures']==[] and row['remainder_pass']=={'P':True,'R':True}
 for family in ['P','R']:
  rr=row['family_remainder'][family];l,u=F(rr['lower_exact']),F(rr['upper_exact']);budget=F(float(arr[ci][family+'_rem'][n-1]));assert 0<=l<=u<=budget;counts['saved_remainder_exact_comparisons']+=1
assert seen=={(ci,n,en) for ci in obj['cells'] for n in range(1,262) for en in ['arb512','iv180']}
for en in ['arb512','iv180']:
 assert obj['counts'][en+'_coefficient_comparisons']==obj['counts'][en+'_coefficient_pass']==20358
 assert obj['counts'][en+'_remainder_comparisons']==obj['counts'][en+'_remainder_pass']==1566
counts['complete_record_coverage']=len(seen)
records=[]
for ci,data in arr.items():
 h,em,er=map(lambda x:F(float(x)),data['scalar'][:3]);EZ=box(em,er);Z=EZ**2
 for n in [1,2,6,47,261]:
  A=box(data['A_mid'][n-1],data['A_rad'][n-1]);BB=box(data['B_mid'][n-1],data['B_rad'][n-1]);FF=[box(m,r) for m,r in zip(data['F_mid'][n-1],data['F_rad'][n-1])]
  lp,lm=2*n-2,-2*n-2;pp=[];rr=[]
  for j in range(23):
   wp=[particular_weight(j,k,lp,-1) for k in range(8)];wm=[particular_weight(j,k,lm,1) for k in range(8)]
   ab=qa(F(lm**j,2*math.factorial(j)))*A;bb=qa(F(lp**j,2*math.factorial(j)))*BB
   pp.append((ab+bb)/Z+Z*sum((x*qa((a+b)/2) for x,a,b in zip(FF,wp,wm)),arb(0)))
   rr.append((bb-ab)/Z+Z*sum((x*qa((a-b)/2) for x,a,b in zip(FF,wp,wm)),arb(0)))
  dp=derivative(BB/Z,Z,FF,lp,-1,23,h);dm=derivative(A/Z,Z,FF,lm,1,23,h);H=(dp+dm)*qa(h**23/F(2*math.factorial(23)))
  for fam,seq in [('P',pp),('R',rr)]:
   for j,x in enumerate(seq[:13]):
    a,b=ends(x);m,r=F(float(data[fam+'_mid'][n-1,j])),F(float(data[fam+'_rad'][n-1,j]));assert m-r<=a<=b<=m+r,(ci,n,fam,j);counts['fresh_coefficient_contains']+=1
   rem=H+qa(sum((mag(seq[j])*h**j for j in range(13,23)),F()));a,b=ends(rem);budget=F(float(data[fam+'_rem'][n-1]));assert 0<=a<=b<=budget,(ci,n,fam,float(b/budget));counts['fresh_remainder_contains']+=1
   records.append({'cell':ci,'n':n,'family':fam,'fresh_rem_lower':str(a),'fresh_rem_upper':str(b),'producer_budget':str(budget)})
for p in [Path(__file__),D/'AUDIT_METHOD.md',E/'selected_v3_checks.json',E/'selected_v2_checks.json',E/'smoke_checks.json',E/'smoke_v2_checks.json',E/'smoke_v3_checks.json']:
 files[str(p.relative_to(B))]=sha(p)
summary={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FULL_OUTPUT_AND_FRESH_PARTICULAR_AUDIT','counts':dict(counts),'fresh_modes':[1,2,6,47,261],'fresh_arb_bits':1536,'fresh_order':22,'records':records,'files':files,'scope':'Every saved output verdict audited; supplementary fresh particular-polynomial calculations at15 selected cell-mode pairs. Only3 cells accepted for local finite input ODEs, not canonical data or full field.'}
(E/'output_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
compact={k:v for k,v in summary.items() if k not in ['records']};compact['primary_status']=obj['status'];compact['primary_counts']=obj['counts'];compact['primary_cells']=obj['cells'];compact['primary_modes_count']=len(obj['modes']);compact['runtime']=obj['runtime']
(E/'review_summary.json').write_text(json.dumps(compact,indent=2)+'\n');print(json.dumps({k:v for k,v in compact.items() if k not in ['files','runtime']}))
