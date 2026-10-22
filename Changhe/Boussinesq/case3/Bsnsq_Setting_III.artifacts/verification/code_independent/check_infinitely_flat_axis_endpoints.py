"""P289 exact local controls; no numerical-lane imports."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,hashlib,time
v=Path('research/289_infinitely_flat_axis_endpoints/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks=[]
def ck(n,x,d=None):checks.append(dict(name=n,passed=bool(x),detail=d))
def zero(n,x):
 e=S.factor(S.cancel(S.expand(x)));ck(n,e==0,str(e))
s=S.symbols('s',positive=True);beta=S.symbols('beta',positive=True);L=3*beta+2;M=2*beta+1;d=L/2;c=3*d/beta
B,T,E,K=[S.Function(k)(s)for k in ['B','T','E','K']];bp=S.diff(B,s);tp=(L+2*bp)*T/B;ep=((M+bp)*E-T)/B
F=S.diff(B,s,2)/B;P=-c*F
for eps in [-1,1]:
 dy=lambda f:-eps*S.diff(f,s);b=eps*B;vv=-eps*S.diff(B,s,2)/2-E/2
 zero(f'eps{eps}_curl',E+dy(dy(b))+2*vv)
 zero(f'eps{eps}_thermal',(b*dy(T)+(L-2*dy(b))*T).subs(S.diff(T,s),tp))
 zero(f'eps{eps}_vorticity',(b*dy(E)+(M-dy(b))*E-T).subs(S.diff(E,s),ep))
 q=4*S.diff(B,s,3)-6*S.diff(B,s,2)*(L+2*bp)/B-eps*((10*beta+8+8*bp)*E+4*T)/B
 residual=S.expand((b*dy(K*T)+(7*beta+2-4*dy(b))*K*T-8*dy(vv)*T+12*vv*dy(T))/T)
 zero(f'eps{eps}_full_ratio_identity',residual.subs({S.diff(T,s):tp,S.diff(E,s):ep})-(-B*S.diff(K,s)+(4*beta+2*bp)*K-q))
 explicit=4*S.diff(B,s,3)+(-12+2*c)*bp*F-c*B*S.diff(F,s)-eps*((10*beta+8+8*bp)*E+4*T)/B
 zero(f'eps{eps}_curvature_error',q+B*S.diff(P,s)-(4*beta+2*bp)*P-explicit)
zero('coefficient_c',4*beta*c-6*L);zero('gap',L-M-beta-1)
t=S.Function('t')(s);J=S.Function('J')(s);C=S.symbols('C',nonzero=True);TT=C*B**2*S.exp(-L*t);EE=B*S.exp(-M*t)*J
zero('temperature_formula',(B*S.diff(TT,s)-(L+2*bp)*TT).subs(S.diff(t,s),-1/B))
zero('eta_formula',(B*S.diff(EE,s)-(M+bp)*EE+TT).subs({S.diff(t,s):-1/B,S.diff(J,s):-C*S.exp(-(L-M)*t)}))
z=S.symbols('z',positive=True);zero('time_integral_lhopital',S.limit((S.exp(z)/z**2)/S.diff(S.exp(z)/z**2,z),z,S.oo)-1)
# Work in the rational differential algebra u=sin(s^-2), w=cos(s^-2).
# This avoids expensive generic trigonometric simplification.
u,w=S.symbols('u w',real=True)
def Ds(f):return S.cancel(S.diff(f,s)-2*w/s**3*S.diff(f,u)+2*u/s**3*S.diff(f,w))
for label,h in [('B0',S.Integer(1)),('B1',2+u)]:
 jets=[h]
 for j in range(3):jets.append(S.cancel(Ds(jets[-1])+jets[-1]/s**2))
 ff=S.cancel(jets[2]/h)
 expected=s**-4-2*s**-3
 if label=='B1':expected+=(-4*s**-6*u+6*s**-4*w-4*s**-5*w)/(2+u)
 zero(label+'_exact_curvature',ff-expected)
 scaled=S.cancel(4*jets[3]+(-12+2*c)*jets[1]*ff-c*h*Ds(ff))
 ck(label+'_error_exponential_factor_rational',scaled.is_rational_function(s,u,w,beta))
 ck(label+'_curvature_polynomially_bounded_structure',expected.is_rational_function(s,u,w))
 fder=expected
 for j in range(3):
  den=S.factor(S.denom(S.cancel(fder)))
  ck(f'{label}_F_derivative{j}_denominator_nonzero_structure',all(fac in [s,u+2]for fac,power in S.factor_list(den)[1]),str(den))
  ck(f'{label}_F_derivative{j}_rational',fder.is_rational_function(s,u,w))
  ck(f'{label}_B_derivative{j}_flat_factor',jets[j].is_rational_function(s,u,w))
  fder=Ds(fder)
 if label=='B0':zero('B0_negative_leading_constant',S.cancel(s**4*(-c*expected)).subs(s,0)+c)
 else:
  zero('B1_positive_subsequence',S.cancel(s**6*(-c*expected.subs({u:1,w:0}))).subs(s,0)-4*d/beta)
  zero('B1_negative_subsequence',S.cancel(s**6*(-c*expected.subs({u:-1,w:0}))).subs(s,0)+12*d/beta)
  n=S.symbols('n',integer=True,positive=True)
  for sign,phase,sv in [('+',S.pi/2+2*S.pi*n,1),('-',3*S.pi/2+2*S.pi*n,-1)]:
   zero('sequence'+sign+'_sin',S.sin(phase)-sv);zero('sequence'+sign+'_cos',S.cos(phase));zero('sequence'+sign+'_tends_zero',S.limit(phase**(-S.Rational(1,2)),n,S.oo))
f=json.loads((v/'freeze.json').read_text());ck('proof_precedes_controls',f['utc']<start);ck('proof_unchanged',hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest()==f['proof_sha256']);ck('source_frozen',hashlib.sha256((v/'A161_public.md').read_bytes()).hexdigest()==f['source_sha256'])
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks);(v/'checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:x for k,x in r.items()if k!='checks'},indent=2));print('FAILED',json.dumps([x for x in checks if not x['passed']],indent=2))
