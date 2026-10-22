#!/usr/bin/env python3
"""Exact manufactured tests of P337. No teammate code or data is used."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import sympy as S
V=Path('research/337_general_smooth_endpoint/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
x,u=S.symbols('x u',real=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,t,d=None):
 ok=bool(t);checks.append(dict(name=n,passed=ok,detail=d))
 if not ok:print('FAIL',n,d,flush=True)
def zero(t):return S.expand(t)==0
def D(f,a,P):return x*a*S.diff(f,x)+P*S.diff(f,u)
f=json.loads((V/'proof_freeze.json').read_text());ck('proof_precedes',datetime.fromisoformat(f['utc'])<datetime.fromisoformat(start));ck('proof_hash',sha(V.parent/'PROOF.md')==f['proof_sha256'])
for name,value in f['dependencies'].items():ck('dependency_'+name,sha(Path(name))==value)
cases=[]
for idx,(beta,kap,C,k,n,h4,ell,g) in enumerate([(2,1,2,1,10,0,0,0),(3,1,1,-2,13,0,0,0),(4,1,-1,S.Rational(1,3),16,0,0,0),(3,S.Rational(11,3),-2,2,5,S.Rational(1,7),S.Rational(1,3),S.Rational(-1,4))]):
 beta,kap,C,k,h4,ell,g=map(S.sympify,(beta,kap,C,k,h4,ell,g));A=2*beta+kap;lam=beta-2;H=k*x*x/(2*A+kap)+h4*x**4;L=1+ell*x*x;G=1+g*u;Z=(u-H)*L;a=A*L*G;P=(lam-2*a)*(u-H)/n-x*A*G*S.diff(Z,x);theta=C*x*x*Z**n/2;tag=f'case{idx}_';origin={x:0,u:0}
 ck(tag+'integer_relation',S.simplify((2*A-lam)/kap)==n)
 ck(tag+'hyperbolic_data',a.subs(origin)==A and P.subs(origin)==0 and S.diff(P,u).subs(origin)==-kap and S.diff(P,x,2).subs(origin)/2==k)
 ck(tag+'parity',zero(a.subs(x,-x)-a)and zero(P.subs(x,-x)-P)and zero(theta.subs(x,-x)-theta))
 ck(tag+'consistency_graph',zero(P.subs(u,H)-x*a.subs(u,H)*S.diff(H,x)))
 ck(tag+'consistency_root_eigenfunction',zero(D(Z,a,P)-(lam-2*a)*Z/n))
 ck(tag+'consistency_temperature',zero(D(theta,a,P)-lam*theta))
 axis=S.expand(S.diff(theta,x,2).subs(x,0)/2);ck(tag+'axis_exact',axis==C*u**n/2)
 ck(tag+'subcritical_positive',all(S.simplify((2*A-lam-j*kap)/A)>0 for j in range(n)))
 ck(tag+'critical_zero',S.simplify(2*A-lam-n*kap)==0)
 xx=S.Rational(1,20);hh=H.subs(x,xx);dv=S.Rational(1,100);plus=theta.subs({x:xx,u:hh+dv});minus=theta.subs({x:xx,u:hh-dv})
 ck(tag+'sign_both_sides',plus/C>0 and (-1)**n*minus/C>0)
 if n%2==0:
  I=x*Z**(n//2);ck(tag+'consistency_odd_I_eigenvalue',zero(D(I,a,P)-lam*I/2)and zero(I.subs(x,-x)+I));ck(tag+'consistency_square_identity',zero(theta-C*I*I/2))
 else:ck(tag+'odd_n_sign_change',plus*minus<0)
 bad=theta+S.Rational(7,13)*x*x*(u-H)**(n-1);ck(tag+'lower_order_rejected',not zero(D(bad,a,P)-lam*bad))
 if idx<3:ck(tag+'divergence_2beta',zero(S.diff(x*a,x)+S.diff(P,u)-2*beta))
 cases.append({'beta':str(beta),'kappa':str(kap),'A':str(A),'lambda':str(lam),'n':n,'C_u':str(C),'k':str(k),'H':str(H),'L':str(L),'G':str(G),'scope':'Local thermal manufacture only; nonlinear case need not have constant divergence, and no vorticity or global inverse claim.'})
# Smooth nonconstant axis units, independently derived without a graph manufacture.
r=S.Rational(3,7);nu=S.Integer(13);kap=S.Integer(1);lam=S.Integer(1);pu=1+r*u;au=(lam+kap*(nu*pu+r*u))/2;pp=-kap*u*pu
# Here the independently prescribed axis unit is R=1+ru.
axis=u**nu*pu;ck('nonconstant_axis_unit',S.expand(pp*S.diff(axis,u)+(2*au-lam)*axis)==0)
ck('nonconstant_axis_normalization',S.limit(axis/u**nu,u,0)==1)
# The naive bare power fails when the regular coefficient changes.
ck('bare_power_negative',S.expand(pp*S.diff(u**nu,u)+(2*au-lam)*u**nu)!=0)
# A half-integer exponent has an unbounded next derivative on the positive side.
v=S.symbols('v',positive=True);nu2=S.Rational(7,2)
ck('fractional_next_derivative',S.diff(v**nu2,v,4)==S.Rational(105,16)/S.sqrt(v))
ck('fractional_unbounded',S.limit(S.diff(v**nu2,v,4),v,0,dir='+')==S.oo)
# Separate the incoming distance convention from the signed coordinate.
for n in [5,10,13,16]:
 for eps in [-1,1]:
  ck(f'identity_sanity_orientation_n{n}_eps{eps}',S.expand((eps**n)*(eps*u)**n-u**n)==0)
# Flat actual first integral; this is distinct from P334's deliberately invalid PDE perturbation.
E=S.exp(-1/(x*x*u**10));ck('flat_actual_transport',S.simplify(D(E,S.Integer(5),-u))==0)
ck('smoke_fixed_positive_u_axis_limit',S.limit(E.subs(u,v),x,0)==0)
# For beta>2 the unbounded axis solution is rejected by continuity.
ck('positive_lambda_axis_blowup',S.limit(v**(-S.Rational(3,5)),v,0,dir='+')==S.oo)
groups={'file_integrity':[],'manufactured_consistency_and_data':[],'sampled_signs':[],'single_perturbation_negatives':[],'orientation_identity_sanity':[],'other_exact_or_smoke':[]}
for z in checks:
 name=z['name'];g=('file_integrity' if name.startswith(('proof_','dependency_')) else 'sampled_signs' if ('sign_both_sides' in name or 'odd_n_sign_change' in name) else 'single_perturbation_negatives' if 'lower_order_rejected' in name else 'orientation_identity_sanity' if name.startswith('identity_sanity_orientation_') else 'manufactured_consistency_and_data' if name.startswith('case') else 'other_exact_or_smoke');groups[g].append(name)
out={'check_groups':{k:len(z)for k,z in groups.items()},'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(z['passed']for z in checks),'total':len(checks),'checks':checks,'cases':cases,'code_sha256':sha(Path(__file__)),'proof_sha256':sha(V.parent/'PROOF.md'),'scope':'Finite exact manufactured/negative controls. General smooth factorization and integrality are proved separately in PROOF.md. No actual B2 profile or convergence claim.'};(V/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','cases']},indent=2));raise SystemExit(0 if all(z['passed']for z in checks)else 1)
