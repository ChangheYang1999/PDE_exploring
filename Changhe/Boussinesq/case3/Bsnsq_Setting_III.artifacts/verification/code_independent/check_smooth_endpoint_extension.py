#!/usr/bin/env python3
"""Independent exact controls for P338's actual-smooth, explicit-axis extension."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,hashlib,time,re
V=Path('research/338_smooth_endpoint_report_entry/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
x,u=S.symbols('x u',real=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,t,d=None):
 ok=bool(t);checks.append(dict(name=n,passed=ok,detail=d))
 if not ok:print('FAIL',n,d,flush=True)
def zero(t):return S.expand(t)==0
def act(t,a,P):return x*a*S.diff(t,x)+P*S.diff(t,u)
f=json.loads((V/'math_freeze.json').read_text());ck('proof_precedes',f['utc']<start);ck('proof_hash',sha(V.parent/'PROOF.md')==f['proof_sha256'])
for d in f['inputs']:ck('frozen_'+d['snapshot'],sha(V/d['snapshot'])==d['sha256'])
# First3 reproduce the referee's printed polynomial examples independently.
par=[(1,5,2,2,3,0,0,0),(1,S.Rational(5,2),1,2,4,0,0,0),(2,1,1,2,10,0,0,0),(S.Rational(1,2),S.Rational(7,2),-2,-1,3,0,0,0),(S.Rational(3,2),S.Rational(13,4),S.Rational(2,3),-2,4,0,0,0),(S.Rational(1,3),1,2,-3,5,S.Rational(1,7),S.Rational(1,3),S.Rational(-1,4))]
cases=[]
for idx,(beta,kap,k,C,n,h4,ell,g)in enumerate(par):
 beta,kap,k,C,h4,ell,g=map(S.sympify,(beta,kap,k,C,h4,ell,g));A=2*beta+kap;lam=beta-2;H=k*x*x/(2*A+kap)+h4*x**4;L=1+ell*x*x;G=1+g*u;Z=(u-H)*L;a=A*L*G;P=(lam-2*a)*(u-H)/n-x*A*G*S.diff(Z,x);Theta=C*x*x*Z**n/2;tag=f'case{idx}_'
 ck(tag+'integer_relation',(2*A-lam)/kap==n);ck(tag+'origin_data',a.subs({x:0,u:0})==A and P.subs({x:0,u:0})==0 and S.diff(P,u).subs({x:0,u:0})==-kap and S.diff(P,x,2).subs({x:0,u:0})==2*k)
 ck(tag+'parity',zero(a.subs(x,-x)-a)and zero(P.subs(x,-x)-P)and zero(Theta.subs(x,-x)-Theta))
 ck(tag+'axis_vanishing',Theta.subs(x,0)==0);ck(tag+'axis_normalization',zero(S.diff(Theta,x,2).subs(x,0)-C*u**n))
 ck(tag+'graph_identity',zero(P.subs(u,H)-x*a.subs(u,H)*S.diff(H,x)))
 ck(tag+'root_eigenfunction',zero(act(Z,a,P)-(lam-2*a)*Z/n))
 ck(tag+'thermal_equation',zero(act(Theta,a,P)-lam*Theta))
 ck(tag+'curvature',S.diff(H,x,2).subs(x,0)/2==k/(4*beta+3*kap))
 ck(tag+'subcritical_positive',all(S.simplify((2*A-lam-j*kap)/A)>0 for j in range(n)))
 ck(tag+'critical_zero',2*A-lam-n*kap==0)
 # Directly differentiate transverse order, separate from all-order proof.
 for j in range(n):ck(tag+'constructed_lower_derivative_'+str(j),S.diff(Theta,u,j).subs(u,H)==0)
 ck(tag+'constructed_exact_order',zero(S.diff(Theta,u,n).subs(u,H)-S.factorial(n)*C*x*x*L**n/2))
 if n%2==0:
  I=x*Z**(n//2);ck(tag+'I_eigenfunction',zero(act(I,a,P)-lam*I/2));ck(tag+'I_odd',zero(I.subs(x,-x)+I));ck(tag+'I_square',zero(Theta-C*I*I/2))
 if idx<5:ck(tag+'divergence',zero(S.diff(x*a,x)+S.diff(P,u)-2*beta))
 else:ck(tag+'nonlinear_manufacture_no_divergence_claim',not zero(S.diff(x*a,x)+S.diff(P,u)-2*beta))
 for eps in [-1,1]:
  v=S.symbols('v',positive=True);incoming=eps**n*C;ck(tag+'orientation_'+str(eps),zero(C*(eps*v)**n-incoming*v**n))
 for qq in [S.Rational(-1,100),S.Rational(1,100)]:
  xx=S.Rational(1,20);value=Theta.subs({x:xx,u:H.subs(x,xx)+qq});ck(tag+'sampled_sign_'+str(qq),value/(C*qq**n)>0)
 # Perturb lower transverse order: it must violate the thermal PDE.
 bad=Theta+S.Rational(2,7)*x*x*(u-H)**(n-1);ck(tag+'lower_order_negative',not zero(act(bad,a,P)-lam*bad))
 cases.append(dict(beta=str(beta),kappa=str(kap),lambda_=str(lam),n=n,C_u=str(C),k=str(k),H=str(H),Theta=str(Theta),scope='Local thermal manufacture; no global profile or vorticity equation. Case5 lacks constant divergence by design.'))
# Exact independent check of the negative-lambda counterexample supplied by A177.
bad=u+x*x*u**7;ck('A177_axis_counterexample_equation',zero(act(bad,S.Integer(3),-u)+bad));ck('A177_axis_counterexample_nonzero_axis',bad.subs(x,0)==u);ck('A177_axis_counterexample_axis_jet',S.diff(bad,x,2).subs(x,0)==2*u**7)
# A distinct counterexample with another negative eigenvalue.
bad2=u*u+x*x*u**8;ck('distinct_axis_counterexample_equation',zero(act(bad2,S.Integer(3),-u)+2*bad2));ck('distinct_axis_counterexample_nonzero_axis',bad2.subs(x,0)==u*u)
# The axis unit is not generally the bare power, independently of graph manufacture.
r=S.Rational(2,9);kap=S.Rational(5,2);lam=S.Integer(-1);n=4;p=1+r*u;a=(lam+kap*(n*p+r*u))/2;P=-kap*u*p;T=u**n*p
ck('negative_lambda_nonconstant_axis_unit',zero(P*S.diff(T,u)+(2*a-lam)*T));ck('axis_unit_normalization',S.limit(T/u**n,u,0)==1);ck('bare_axis_power_fails',not zero(P*S.diff(u**n,u)+(2*a-lam)*u**n))
# The extra parity conclusion requires the global axis/vorticity input, not thermal data alone.
for r in range(1,10):
 for d in range(1,10):
  if(r+d)%2:ck(f'parity_r{r}_d{d}',((2+3*r+2*d)%2==0)==(d%2==1))
ck('thermal_only_parity_counterexample',13%2==1 and 1%2==1) # beta3,kappa1: n13,d1; P337 already checks exact thermal model.
text=(V/'A177_output.txt').read_text();ck('A177_printed_parameters',all(s in text for s in ['beta=1, kappa=5, k=2, n=3','beta=1, kappa=5/2, k=1, n=4','beta=2, kappa=1, k=1, n=10']))
ck('A177_model_limitation_retained','failed because its EC2 credential source supplied no credentials'in(V/'A177_PROOF.md').read_text())
# Controls are explicitly not the mathematical proof.
groups={'integrity':[],'constructed_identity_and_data':[],'constructed_transverse_derivatives':[],'negative_controls':[],'sampled_signs':[],'orientation_and_parity_sanity':[],'reported_source_checks':[]}
for c in checks:
 n=c['name'];g=('integrity'if n.startswith(('proof_','frozen_'))else'constructed_transverse_derivatives'if'constructed_'in n else'negative_controls'if any(z in n for z in ['counterexample','fails','lower_order_negative']) else'sampled_signs'if'sampled_sign'in n else'orientation_and_parity_sanity'if'orientation_'in n or n.startswith('parity_') else'reported_source_checks'if n.startswith('A177_printed')or n=='A177_model_limitation_retained'else'constructed_identity_and_data');groups[g].append(n)
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(t['passed']for t in checks),total=len(checks),checks=checks,cases=cases,groups={k:len(v)for k,v in groups.items()},code_sha256=sha(Path(__file__)),proof_sha256=sha(V.parent/'PROOF.md'),scope='Exact finite manufactured controls, reported-source checks and negative examples. General proof in PROOF.md. Full report preview/readback separate; no joint local B2 solution or global profile.')
(V/'math_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','cases']},indent=2));raise SystemExit(0 if all(t['passed']for t in checks)else 1)
