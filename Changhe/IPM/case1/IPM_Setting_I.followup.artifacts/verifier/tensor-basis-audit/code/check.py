from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sys,json,hashlib
import numpy as np
import mpmath as mp
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inner-cutoff/code'))
sys.path.insert(0,str(ROOT.parent/'center-moment/code'))
from hessian import tensor_coefficients,EnclosedDensity
from certify import moment
ctx.prec=256
out={'utc':datetime.now(timezone.utc).isoformat(),'basis':[],'moments':[],'hessian_diagnostics':[],'dtype_audits':[]}
a=np.array([.5,-1.,.5])
for N,n,rv in [(2,0,[1,1,1]),(2,1,[-1,0,1]),(2,2,[1,-1,1]),(4,4,[1,-1,1,-1,1])]:
 for m,av in [(0,np.ones(3)),(2,a)]:
  b=np.outer(rv,av);co=tensor_coefficients(b)
  checks=[co[i][j].contains(1 if (i,j)==(n,m) else 0) for i in range(N+1) for j in range(3)]
  assert all(checks)
  out['basis'].append({'N':N,'M':3,'n':n,'m':m,'all_exact_targets_enclosed':True,'target':co[n][m].str(30),'largest_spurious_upper':max(float(co[i][j].abs_upper()) for i in range(N+1) for j in range(3) if (i,j)!=(n,m))})
for n,rv,sgn,expected in [(2,[1,-1,1],-1,Fraction(13,10)),(1,[-1,0,1],1,Fraction(9,8)),(4,[1,-1,1,-1,1],-1,Fraction(32,25))]:
 b=1+np.outer(np.array(rv)+sgn,a)/8;assert np.all(b[0]==1)
 co=tensor_coefficients(b);actual=moment(co,arb(2),arb(6),arb(0));exact=arb(expected.numerator)/expected.denominator;assert (actual-exact).contains(0)
 out['moments'].append({'n':n,'expected':str(expected),'enclosure':actual.str(50),'contains_exact':True})
with mp.workdps(100):
 bp,bq=float(.9).as_integer_ratio();beta=mp.mpf(bp)/bq
 def density(x,y):
  t=mp.atan(y/x);s=mp.findroot(lambda z:z+beta*mp.sin(2*z)/2-t,(t/2,t),tol=mp.eps/16,maxsteps=100)
  S=1+(x*x+y*y)/4;z=1-2*S**(-mp.mpf(5)/12);c=mp.cos(2*s)
  return x*x*y*S**(-mp.mpf(17)/12)*z*c
 for pt in [(1.,.5),(.5,1.),(2.,.25)]:
  obj=EnclosedDensity(co=[[arb(0),arb(0)],[arb(0),arb(1)]],L=2,cl=6,beta=.9)
  record,H=obj.hessian(list(pt),Fraction(0))
  for i in range(2):
   for j in range(2):
    ex=mp.diff(density,tuple(mp.mpf(x) for x in pt),(int(i==0)+int(j==0),int(i==1)+int(j==1)))
    reference=arb(mp.nstr(ex,90),'1e-60');assert (reference-H[i][j]).contains(0),(pt,i,j,str(ex),H[i][j])
    out['hessian_diagnostics'].append({'point':pt,'entry':[i,j],'enclosure':H[i][j].str(45),'mpmath_derivative':mp.nstr(ex,80),'overlaps_reference_with_1e-60_diagnostic_radius':True})
for rel in ['grid-states/data/dnB_n96m40S.npz','ritz-resolution/data/dnSB_n120m48.npz','domain-states/data/dnB_n96m40SL4.npz','domain16/data/dnB_n96m40SL16.npz','third-grid-actions/data/dnB_n72m30S.npz','refreshed-third-grid/data/dnC_n72m30S.npz']:
 p=ROOT.parent/rel
 if not p.exists():
  out['dtype_audits'].append({'file':rel,'not_found':True});continue
 with np.load(p) as z:
  d={k:str(z[k].dtype) for k in ('b','L','c_l','beta')};assert all(x=='float64' for x in d.values());N=int(z['N']);M=int(z['M']);assert z['b'].shape==(N+1,M)
  out['dtype_audits'].append({'file':rel,'dtypes':d,'shape':list(z['b'].shape),'N':N,'M':M,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
out['dependencies']={str(p.relative_to(ROOT.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'PROOF.md',ROOT.parent/'inner-cutoff/code/hessian.py',ROOT.parent/'center-moment/code/certify.py',ROOT.parent/'exact-data/code/nodal_input.py']}
out['end_utc']=datetime.now(timezone.utc).isoformat();out['scope']='Exact binary basis targets are interval enclosures; arbitrary-precision implicit Hessian comparisons are diagnostics, not rigorous references. Dtype inspection covers only listed files.'
(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(out['basis']),'basis',len(out['moments']),'moments',len(out['hessian_diagnostics']),'Hessian entries')
print(json.dumps(out['dtype_audits'],indent=2))
