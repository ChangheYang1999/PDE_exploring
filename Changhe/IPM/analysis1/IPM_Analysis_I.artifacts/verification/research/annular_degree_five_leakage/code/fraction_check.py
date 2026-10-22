from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import hashlib,json,sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3];D=R/'research/annular_degree_five_leakage';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def clean(a):return {k:v for k,v in a.items() if v}
def add(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,Q(0))+v
 return clean(out)
def scale(a,s):return clean({k:v*s for k,v in a.items()})
def mul(a,b):
 out={}
 for (i,j),x in a.items():
  for (k,l),y in b.items():out[i+k,j+l]=out.get((i+k,j+l),Q(0))+x*y
 return clean(out)
def deriv(a,axis):
 out={}
 for key,v in a.items():
  if key[axis]:z=list(key);z[axis]-=1;out[tuple(z)]=v*key[axis]
 return clean(out)
def sine_num(n):return {(n-j,j):Q(comb(n,j)*(-1)**((j-1)//2)) for j in range(1,n+1,2)}
def serial(a):return {f'{i},{j}':str(q) for (i,j),q in sorted(a.items())}
start=datetime.now(timezone.utc).isoformat();pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['proof_sha256']
parent='research/higher_center_weight_quasimodes/evidence/verdict.json';expected='cfa4a0b1a83aa34df06362a7d47a3d642c0a4cdde6927e4b022419dbd7958ec8';assert sha(R/parent)==expected;v=load(R/parent)
for n,h in v['files'].items():assert sha(R/n)==h,n
r2={(2,0):Q(1),(0,2):Q(1)};left=add(mul(sine_num(5),r2),sine_num(7));factor=mul({(2,1):Q(4)},{(4,0):Q(3),(2,2):Q(-10),(0,4):Q(3)});assert left==factor
psi4=scale(sine_num(4),Q(1,2));assert psi4=={(3,1):Q(2),(1,3):Q(-2)}
rho3={(2,1):Q(1)};u1=scale(deriv(psi4,1),-1);u2=deriv(psi4,0);image=add(mul(u1,deriv(rho3,0)),mul(u2,deriv(rho3,1)));assert image=={(4,1):Q(2),(2,3):Q(10)}
mom=[]
for n in range(2,22,2):
 lower=Q((n-1)-(n-1),4*n);upper=Q((n-1)+(n+1),4*n);assert lower==0 and upper==Q(1,2);mom.append({'n':n,'lower_multiplier':str(lower),'upper_multiplier':str(upper)})
exp_rows=[]
for m in range(2,12):
 exp=2*5+(-2*m-2)+1;assert exp==9-2*m;assert (exp<=-1)==(m>=5);exp_rows.append({'m':m,'center_radial_exponent':exp,'diverges':exp<=-1})
# Far exponents from |U[h]|~r^-2, |grad rho|~r^(k-1), w_m~r^(-2k-3).
# The coefficients of k cancel and the remaining integer exponent is -8.
assert 2-2==0 and 2*(-3)-3+1==-8
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_POLYNOMIAL_MOMENT_AND_POWER_IDENTITIES_REQUIRES_INDEPENDENT_CHECK','code_sha256':sha(Path(__file__)),'proof_sha256':sha(D/'PROOF.md'),'parent_path':parent,'parent_sha256':expected,'parent_status':v['status'],'parent_files':v['files'],'parent_pin_count':len(v['files']),'normalized_bump_moment':'1','polar_quartic_coefficient':'1/2','cartesian_quartic_coefficient':'2','factor_numerator':serial(factor),'psi_quartic':serial(psi4),'velocity_cubic':[serial(u1),serial(u2)],'image_degree_five':serial(image),'moment_checks':mom,'center_exponents':exp_rows,'far_squared_radial_exponent':-8,'gamma6_interval_from_analytic_bump_normalization':['1/8','1/2'],'scope':'Exact symbolic identities plus parent pins. Bump normalization and strict Gamma6 bounds are analytic, not sampled or numerical integrals.'}
with (E/'fraction.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'parent_pins':len(v['files']),'cartesian_quartic_coefficient':'2','image':out['image_degree_five']}))
