from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import sys,json,hashlib
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3];D=R/'research/axis_weighted_nonlocal_mapping';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def clean(a):return {k:v for k,v in a.items() if v}
def add(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,Q(0))+v
 return clean(out)
def scale(a,v):return clean({k:v*x for k,x in a.items()})
def mul(a,b):
 out={}
 for i,u in a.items():
  for j,v in b.items():key=tuple(x+y for x,y in zip(i,j));out[key]=out.get(key,Q(0))+u*v
 return clean(out)
def deriv(a,axis):
 out={}
 for key,v in a.items():
  if key[axis]:new=list(key);new[axis]-=1;out[tuple(new)]=v*key[axis]
 return clean(out)
def serial(a):return {','.join(map(str,k)):str(v) for k,v in sorted(a.items())}
start=datetime.now(timezone.utc).isoformat();pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['proof_sha256'];parent='research/anisotropic_frozen_transport_inverse/evidence/verdict.json';want='ac665ea3c8780c0ca6b5a9590d82011af4ec6ff6de78197d13572c4bf1ed4da2';assert sha(R/parent)==want;v=load(R/parent)
for n,h in v['files'].items():assert sha(R/n)==h,n
# u,v,U,V denote the two sine functions at independent angles.
w={(1,0,0,1):Q(1),(0,1,1,0):Q(-1)};gramkernel=mul(w,w);assert gramkernel=={(2,0,0,2):Q(1),(1,1,1,1):Q(-2),(0,2,2,0):Q(1)}
# Independent angular integrations: (u^2,v^2,u*v) -> (A,D,B) in each angle.
integrated={}
lookup={(2,0):(1,0,0),(0,2):(0,0,1),(1,1):(0,1,0)}
for (u,vv,U,V),coef in gramkernel.items():
 key=tuple(a+b for a,b in zip(lookup[u,vv],lookup[U,V]));integrated[key]=integrated.get(key,Q(0))+coef
integrated=clean(integrated);assert integrated=={(1,0,1):Q(2),(0,2,0):Q(-2)}
A={(1,0,0):Q(1)};B={(0,1,0):Q(1)};DD={(0,0,1):Q(1)};zero3=add(mul(A,B),scale(mul(B,A),-1));num5=add(mul(A,DD),scale(mul(B,B),-1));assert zero3=={} and scale(num5,2)==integrated
psi={(3,1):Q(1),(1,3):Q(-1)};rho={(2,1):Q(1)};u1=scale(deriv(psi,1),-1);u2=deriv(psi,0);image=add(mul(u1,deriv(rho,0)),mul(u2,deriv(rho,1)));assert image=={(4,1):Q(1),(2,3):Q(5)};xx=deriv(deriv(image,0),0);axis={key:v for key,v in xx.items() if key[0]==0};assert axis=={(0,3):Q(10)}
parities=[]
for n in [3,5]:
 poly={(n-j,j):Q(comb(n,j)*(-1)**((j-1)//2)) for j in range(1,n+1,2)};assert all(i%2==0 and j%2==1 for i,j in poly);parities.append({'sine_mode':n,'numerator':serial(poly),'even_x_odd_y':True})
remainders=[]
for j in range(3):
 for i in range(j+1):
  exps=[(3-i)+(4-(j-i)),(5-i)+(2-(j-i)),(5-i)+(4-(j-i))];assert exps[:2]==[7-j,7-j] and exps[2]==9-j;remainders.append({'total_derivative':j,'velocity_derivative':i,'radial_orders':exps})
for a,expect in [(Q(2),False),(Q(5,2),True),(Q(6),True)]:assert (4-2*a<=-1)==expect
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_GRAM_POLYNOMIAL_AXIS_AND_POWER_ALGEBRA_REQUIRES_INDEPENDENT_CHECK','code_sha256':sha(Path(__file__)),'proof_sha256':sha(D/'PROOF.md'),'parent_path':parent,'parent_sha256':want,'parent_status':v['status'],'parent_files':v['files'],'parent_pin_count':len(v['files']),'gram_square_kernel':serial(gramkernel),'gram_double_integral':serial(integrated),'third_projection_cleared':serial(zero3),'fifth_projection_cleared':serial(num5),'velocity_cubic':[serial(u1),serial(u2)],'degree_five_image_divided_by_C':serial(image),'axis_second_derivative_divided_by_C':serial(axis),'sine_parities':parities,'remainder_product_orders':remainders,'axis_integrability_threshold_exact':'5/2','scope':'Finite algebra only. Gram strict positivity, existence of smooth bumps, analytic harmonic expansion and lower-bound divergence are supplied by PROOF.md.'}
with (E/'fraction.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','axis_second_derivative_divided_by_C','axis_integrability_threshold_exact']}))
