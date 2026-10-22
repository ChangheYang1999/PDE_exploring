"""P286 supplementary exact controls, derived directly in both orientations."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
V=Path('research/286_finite_order_axis_endpoint/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();C=[]
def ck(name,ok,detail=None):C.append(dict(name=name,passed=bool(ok),detail=detail))
def zero(name,x):
 e=S.factor(S.cancel(S.expand(x)));ck(name,e==0,str(e))
s=S.symbols('s',positive=True);beta,a=S.symbols('beta a',positive=True);L=3*beta+2;M=2*beta+1;d=L/2
B,T,E,K=[S.Function(k)(s)for k in ['B','T','E','K']];bp=S.diff(B,s);tp=(L+2*bp)*T/B;ep=((M+bp)*E-T)/B
for eps in [-1,1]:
 dy=lambda x:-eps*S.diff(x,s);b=eps*B;v=-(dy(dy(b))+E)/2
 zero(f'orientation{eps}_bprime',dy(b)+bp);zero(f'orientation{eps}_bsecond',dy(dy(b))-eps*S.diff(B,s,2));zero(f'orientation{eps}_curl',E+dy(dy(b))+2*v)
 tr=b*dy(T)+(L-2*dy(b))*T;er=b*dy(E)+(M-dy(b))*E-T
 zero(f'orientation{eps}_thermal',tr.subs(S.diff(T,s),tp));zero(f'orientation{eps}_vorticity',er.subs(S.diff(E,s),ep))
 D=K*T;full=b*dy(D)+(7*beta+2-4*dy(b))*D-8*dy(v)*T+12*v*dy(T)
 reduced=S.expand(full/T).subs({S.diff(T,s):tp,S.diff(E,s):ep})
 q=4*S.diff(B,s,3)-6*S.diff(B,s,2)*(L+2*bp)/B-eps*((10*beta+8+8*bp)*E+4*T)/B
 target=-B*S.diff(K,s)+(4*beta+2*bp)*K-q
 zero(f'orientation{eps}_full_D_equation_reduction',reduced-target)
 zero(f'orientation{eps}_weighted_Z_equation',-B*S.diff(s**2*K,s)+(4*beta+2*bp+2*B/s)*s**2*K-s**2*(-B*S.diff(K,s)+(4*beta+2*bp)*K))
zero('coefficient_identity',4*M-6*L+10*beta+8);zero('limiting_constant',-6*L/(4*beta)+3*d/beta)
# Jet induction: isolate the highest unknown derivative after all lower jets vanish.
y=S.symbols('y');b0=S.Function('b')(y);f=S.Function('f')(y)
for name,lam,weight in [('T',L,2),('eta',M,1),('D',7*beta+2,4)]:
 for order in range(9):
  expr=S.diff(b0*S.diff(f,y)+(lam-weight*S.diff(b0,y))*f,y,order)
  # Replace jets atomically by independent symbols before setting lower jets to zero.
  # subs(f,0) would also replace f inside its still-needed highest derivative.
  bj=S.symbols('b0:'+str(order+2));fj=S.symbols('f0:'+str(order+2))
  jets={S.diff(b0,y,j)if j else b0:bj[j] for j in range(order+2)}
  jets.update({S.diff(f,y,j)if j else f:fj[j] for j in range(order+2)})
  expr=S.expand(expr).xreplace(jets)
  rules={bj[0]:0,bj[1]:0};rules.update({fj[j]:0 for j in range(order)})
  zero(f'flatness_{name}_order{order}',expr.subs(rules,simultaneous=True)-lam*fj[order])
# Generic integrating factors. t_s=-1/B, and H_s=-C exp(-(L-M)t).
t=S.Function('t')(s);h=S.Function('h')(s);coef=S.symbols('C',nonzero=True);tt=coef*B**2*S.exp(-L*t);ee=B*S.exp(-M*t)*h
zero('exact_thermal_integrating_factor',(B*S.diff(tt,s)-(L+2*bp)*tt).subs(S.diff(t,s),-1/B))
zero('exact_eta_integrating_factor',(B*S.diff(ee,s)-(M+bp)*ee+tt).subs({S.diff(t,s):-1/B,S.diff(h,s):-coef*S.exp(-(L-M)*t)}))
zero('positive_gap_identity',L-M-beta-1)
# Six finite orders, including quadratic and odd crossing zeros, with general a>0.
for p in range(2,8):
 Bp=a*s**p;der=[S.diff(Bp,s,j)for j in range(4)];geom=4*der[3]-6*der[2]*(L+2*der[1])/Bp
 zero(f'p{p}_curvature_coefficient',s**2*der[2]/Bp-p*(p-1))
 zero(f'p{p}_forcing_limit',S.limit(s**2*geom,s,0,dir='+')+6*L*p*(p-1))
 zero(f'p{p}_stable_coefficient_limit',S.limit(4*beta+2*der[1]+2*Bp/s,s,0,dir='+')-4*beta)
 texp=s**(1-p)/(a*(p-1));zero(f'p{p}_time_derivative',S.diff(texp,s)+1/Bp)
 logabsT=2*S.log(Bp)-L*texp;zero(f'p{p}_log_temperature_leading',S.limit(s**(p-1)*logabsT,s,0,dir='+')+L/(a*(p-1)))
 wrong=2*S.log(Bp)+L*texp;zero(f'p{p}_wrong_sign_growth',S.limit(s**(p-1)*wrong,s,0,dir='+')-L/(a*(p-1)))
 zero(f'p{p}_ratio_constant',-6*L*p*(p-1)/(4*beta)+3*d*p*(p-1)/beta)
ystar,yy=S.symbols('ystar yy',real=True)
for eps in [-1,1]:
 for p in range(2,8):
  polynomial=eps*a*(eps*(ystar-yy))**p
  zero(f'local_extension_eps{eps}_p{p}_interior_match',polynomial.subs(yy,ystar-eps*s)-eps*a*s**p)
  zero(f'local_extension_eps{eps}_p{p}_endpoint',polynomial.subs(yy,ystar))
frozen=json.loads((V/'freeze.json').read_text());ck('proof_written_before_controls',frozen['utc']<start and hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==frozen['proof_sha256']);ck('source_frozen',hashlib.sha256((V/'A161_public.md').read_bytes()).hexdigest()==frozen['source_sha256'])
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(c['passed']for c in C),total=len(C),checks=C,verdict='CONFIRMED'if all(c['passed']for c in C)else'OPEN');(V/'checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='checks'},indent=2));print('FAIL',json.dumps([c for c in C if not c['passed']],indent=2))
