from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
B=Path(__file__).resolve().parents[1];start=time.monotonic()
x,y=S.symbols('x y',real=True);rr=x*x+y*y
p=y/rr
assert S.cancel(S.diff(p,x,y)+2*(x**3-3*x*y*y)/rr**3)==0
assert S.cancel(S.diff(p,x,2)-2*(3*x*x*y-y**3)/rr**3)==0
u1=(x**3-3*x*y*y)/rr**3;u2=(3*x*x*y-y**3)/rr**3
assert S.cancel(S.diff(u1,x)+S.diff(u2,y))==0
assert S.cancel(x*u1+y*u2-(x*x-y*y)/rr**2)==0
assert S.cancel(-y*u1+x*u2-2*x*y/rr**2)==0
r=S.symbols('r',positive=True);A=S.Function('A')(r);D=S.Function('D')(r);eta=S.Function('eta')(r)
v=-(A/r+r*D)/2
L=S.diff(v,r,2)+S.diff(v,r)/r-v/r**2
L=L.subs({S.diff(A,r,2):2*r*eta+r*r*S.diff(eta,r),S.diff(D,r,2):-S.diff(eta,r),S.diff(A,r):r*r*eta,S.diff(D,r):-eta})
assert S.simplify(L-eta)==0
assert Q(32770_28,100)==1+Q(32,25)+2**15
exponents={'density_L2':Q(-2),'gradient_L2':Q(-3),'weighted_Hessian':Q(-2)-2+Q(4,5),'weighted_third_derivative':Q(-2)-3+Q(4,5),'nonlinear_L2':Q(-6)}
assert exponents['weighted_Hessian']==Q(-16,5)
assert exponents['weighted_third_derivative']==Q(-21,5)
assert all(v<=-2 for v in exponents.values())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),
'dependency_sha256':sha(B.parent/'sharp_l2_audit/PROOF.md'),
'cartesian_dipole_derivatives':True,'divergence_free':True,'polar_components':True,'radial_Green_identity':True,
'exact_scaling_exponents':{k:str(v) for k,v in exponents.items()},'Cw_exact':'819257/25',
'analytic_construction_open_independent_review':True}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
