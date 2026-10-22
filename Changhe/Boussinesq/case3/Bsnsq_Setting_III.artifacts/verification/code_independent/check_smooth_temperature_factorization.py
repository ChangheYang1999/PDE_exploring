#!/usr/bin/env python3
"""Independent symbolic manufactured controls. No teammate code is imported."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
V=Path('research/334_smooth_temperature_factorization/verification')
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
x,s=S.symbols('x s',real=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,t,detail=None):
 ok=bool(t);checks.append(dict(name=n,passed=ok,detail=detail))
 if not ok:print('FAIL',n,detail,flush=True)
def zero(z):return S.Poly(S.expand(z),x,s).is_zero
def W(z,a,P):return x*a*S.diff(z,x)+P*S.diff(z,s)
f=json.loads((V/'proof_freeze.json').read_text());ck('proof_precedes_controls',datetime.fromisoformat(f['utc'])<datetime.fromisoformat(start));ck('proof_hash',f['sha256']==sha(V.parent/'PROOF.md'))
ck('source_pdf_hash',f['source_pdf_sha256']==sha(V.parent/'sources/dutilleul_1804.06126.pdf'))
ck('source_text_hash',f['source_text_sha256']==sha(V.parent/'sources/dutilleul_1804.06126.txt'))
cases=[]
# Choose a known first integral and a vector field tangent to it. These are
# consistency tests, not independent solutions of the B2 equations.
for ix,(C,k,h4,lx,ls,gx,gs) in enumerate([(2,1,0,0,0,0,0),(-2,-3,0,0,0,0,0),(S.Rational(3,2),S.Rational(-2,5),S.Rational(1,7),S.Rational(1,3),S.Rational(-1,4),S.Rational(1,5),S.Rational(1,11)),(-1,2,S.Rational(-1,9),S.Rational(-1,4),S.Rational(1,6),0,S.Rational(-1,12))]):
 C,k=map(S.sympify,(C,k));H=k*x*x/11+h4*x**4;L=1+lx*x*x+ls*s;G=1+gx*x*x+gs*s*s;Z=(s-H)*L
 a=5*S.diff(Z,s)*G;P=-G*(Z+5*x*S.diff(Z,x));Theta=C*x*x*Z**10/2;I=x*Z**5
 name=f'case{ix}_';ck(name+'reflection',zero(a.subs(x,-x)-a)and zero(P.subs(x,-x)-P)and zero(Z.subs(x,-x)-Z))
 origin={x:0,s:0};ck(name+'hyperbolic_data',a.subs(origin)==5 and P.subs(origin)==0 and S.diff(P,s).subs(origin)==-1 and S.diff(P,x,2).subs(origin)/2==k)
 ck(name+'graph_equation',S.expand(P.subs(s,H)-x*a.subs(s,H)*S.diff(H,x))==0)
 ck(name+'root_transport',zero(W(Z,a,P)+a*Z/5))
 # Factor before expansion to avoid manufacturing artificial large numerals.
 ck(name+'thermal_transport',S.expand(S.diff(Theta,x)*x*a+S.diff(Theta,s)*P)==0)
 ck(name+'odd_first_integral',zero(W(I,a,P)) and S.expand(I.subs(x,-x)+I)==0)
 axis=S.diff(Theta,x,2).subs(x,0)/2
 ck(name+'axis_tenth_jet',S.Poly(S.expand(axis),s).nth(10)==C/2 and all(S.Poly(S.expand(axis),s).nth(j)==0 for j in range(10)))
 # All sample points lie in a small box where the prescribed L is positive.
 points=[(S.Rational(1,10),S.Rational(1,20)),(-S.Rational(1,10),S.Rational(-1,20)),(S.Rational(1,11),S.Rational(1,30))]
 vals=[]
 for xx,ss in points:
  val=Theta.subs({x:xx,s:ss});ll=L.subs({x:xx,s:ss});zz=Z.subs({x:xx,s:ss});vals.append(bool(ll>0 and zz!=0 and val/C>0))
 ck(name+'finite_sign_samples',all(vals))
 bad=Theta+S.Rational(7,13)*x*x*(s-H)**9
 ck(name+'wrong_ninth_order_rejected',not zero(W(bad,a,P)))
 cases.append({'C':str(C),'k':str(k),'H':str(H),'L':str(L),'G':str(G),'a':str(a),'P':str(P),'scope':'Manufactured local thermal field. No canonical inverse or vorticity solution asserted.'})
# The positive indicial exponents are the exact hypothesis in the ODE proof.
ck('ten_positive_indicial_exponents',all(S.Rational(2)-S.Rational(j,5)>0 for j in range(10)))
ck('critical_order_ten',S.Rational(2)-S.Rational(10,5)==0)
q=S.symbols('q');fj=S.Function('f');alpha,d=S.symbols('alpha d')
for j in [0,1,5,9,10]:
 op=x*alpha*S.diff(fj(x)*q**j,x)+q*d*S.diff(fj(x)*q**j,q)+2*alpha*fj(x)*q**j
 expected=q**j*(x*alpha*S.diff(fj(x),x)+(2*alpha+j*d)*fj(x))
 ck('indicial_operator_'+str(j),S.expand(op-expected)==0)
# x!=0 exact expression, paired with the proof of smooth extension at x=0.
phi=S.exp(-1/x**2);test=x*x*(s**10-phi)
flatres=S.simplify(W(test,S.Integer(5),-s)+(10*x*x+10)*phi)
ck('flat_perturbation_residual',flatres==0)
ck('flat_perturbation_negative_on_graph',S.simplify(test.subs(s,0)/(-x*x*phi))==1)
# Repeated derivative form certifies that every fixed-order derivative is flat.
z=S.symbols('z');poly=S.Integer(1);flat_polys=[]
for n in range(13):
 flat_polys.append(str(poly));poly=S.expand(-z*z*S.diff(poly,z)+2*z**3*poly)
ck('flat_derivative_recurrence',S.simplify(S.diff(phi,x,5)-S.sympify(flat_polys[5]).subs(z,1/x)*phi)==0)
# A normalized positive power root is necessary: -Z violates the normalization.
ck('negative_root_normalization',S.diff(-(s-x*x/11),s).subs({x:0,s:0})==-1)
# The simple manufactured field does obey div W=4, but its vorticity equation fails.
a=S.Integer(5);P=-s+x*x;Z=s-x*x/11;theta=x*x*Z**10
# Physical y=-s: U1=3x, U2=s-x^2, minus 2y gives 3s-x^2;
# Omega=-curl_y U=2x. In these coordinates scalar transport uses P.
omega=2*x
ck('simple_divergence_four',S.diff(x*a,x)+S.diff(P,s)==4)
ck('simple_not_B2',not zero(W(omega,a,P)+omega-S.diff(theta,x)))
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'cases':cases,'flat_derivative_polynomials_in_inverse_x':flat_polys,'proof_sha256':sha(V.parent/'PROOF.md'),'code_sha256':sha(Path(__file__)),'scope':'Exact manufactured consistency and explicit negative controls. The general C-infinity theorem is proved in PROOF.md, not inferred from these finite computations.'}
(V/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','cases','flat_derivative_polynomials_in_inverse_x']},indent=2));raise SystemExit(0 if all(c['passed']for c in checks)else 1)
