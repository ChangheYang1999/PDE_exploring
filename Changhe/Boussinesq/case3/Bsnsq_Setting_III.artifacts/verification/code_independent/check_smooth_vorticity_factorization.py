#!/usr/bin/env python3
"""Own exact coupled-transport manufactures, including explicit kinematic failures."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import hashlib,json,time
V=Path('research/339_smooth_vorticity_factorization/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
x,u,q0=S.symbols('x u q',real=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,t,d=None):
 ok=bool(t);checks.append(dict(name=n,passed=ok,detail=d))
 if not ok:print('FAIL',n,d,flush=True)
def z(t):return S.expand(t)==0
def act(t,A,P):return A*x*S.diff(t,x)+P*S.diff(t,u)
f=json.loads((V/'proof_freeze.json').read_text());ck('proof_precedes',f['utc']<start);ck('proof_hash',sha(V.parent/'PROOF.md')==f['proof_sha256'])
for p,h in f['dependencies'].items():ck('dependency_'+p,sha(Path(p))==h)
cases=[]
parameters=[(2,1,1,2,3,10,6),(4,1,-2,-1,2,16,10),(S.Rational(5,2),S.Rational(1,2),S.Rational(3,7),3,-2,21,13),(S.Rational(8,3),S.Rational(1,3),-1,1,1,32,20)]
for idx,(beta,kap,k,C,D,n,m) in enumerate(parameters):
 beta,kap,k,C,D=map(S.sympify,(beta,kap,k,C,D));A=2*beta+kap;lam=beta-2;h=k/(2*A+kap);H=h*x*x;q=u-H;P=-kap*u+k*x*x
 E1=C/(kap*(m-n));den=3*A+1-kap*(n-1);E3=-C*n*h/den;Theta=C*x*x*q**n/2;Om=D*x*q**m+E1*x*q**n+E3*x**3*q**(n-1);M=1+(E1/D)*q**(n-m)+(E3/D)*x*x*q**(n-m-1);tag=f'case{idx}_'
 ck(tag+'integer_orders',(2*A-lam)/kap==n and(A+1)/kap==m)
 ck(tag+'gap_ge2',n-m>=2);ck(tag+'denominator_identity',den==A+lam+kap+1 and den>0)
 ck(tag+'divergence',z(S.diff(A*x,x)+S.diff(P,u)-2*beta))
 ck(tag+'parity',z(Theta.subs(x,-x)-Theta)and z(Om.subs(x,-x)+Om)and z(M.subs(x,-x)-M))
 ck(tag+'graph_identity',z(P.subs(u,H)-A*x*S.diff(H,x)))
 ck(tag+'root_transport',z(act(q,A,P)+kap*q))
 ck(tag+'thermal_transport',z(act(Theta,A,P)-lam*Theta))
 source=S.diff(Theta,x);ck(tag+'vorticity_transport',z(act(Om,A,P)+Om-source))
 ck(tag+'source_fixed_u_derivative',z(source-C*x*q**n+C*n*h*x**3*q**(n-1)))
 ck(tag+'factorization_consistency',z(Om-D*x*q**m*M))
 lhs=act(M,A,P)+(1+A+m*(lam-2*A)/n)*M
 rhs=C/D*(q**(n-m)+S.Rational(n,2)*x*q**(n-m-1)*S.diff(q,x))
 ck(tag+'unit_transport',z(lhs-rhs));ck(tag+'unit_at_origin',M.subs({x:0,u:0})==1)
 ck(tag+'unit_source_on_graph',rhs.subs(u,H)==0)
 axis=S.diff(Om,x).subs(x,0);ck(tag+'axis_formula',z(axis-D*u**m-E1*u**n))
 ck(tag+'axis_leading_coefficient',S.diff(axis,u,m).subs(u,0)/S.factorial(m)==D)
 ck(tag+'thermal_axis',z(S.diff(Theta,x,2).subs(x,0)-C*u**n))
 shifted=S.Poly(S.expand(Om.subs(u,q0+H)),q0);coeffs={a[0]:c for a,c in shifted.terms()}
 for j in range(m):ck(tag+'constructed_lower_coefficient_'+str(j),coeffs.get(j,0)==0)
 ck(tag+'leading_transverse_coefficient',z(coeffs.get(m,0)-D*x))
 # Prompt convention is Omega=P_x-x*a_u in signed coordinates, not conventional curl.
 kinematic=S.diff(P,x);Ekin=kinematic-Om
 ck(tag+'required_kinematic_negative',not z(Ekin))
 ck(tag+'kinematic_failure_on_graph',z(Ekin.subs(u,H)-2*k*x)and k!=0)
 # Independently manufactured bad subcritical component has a nonzero PDE residual.
 bad=Om+S.Rational(7,13)*x*q**(m-1);badres=S.expand(act(bad,A,P)+bad-source)
 ck(tag+'lower_order_negative',z(badres-S.Rational(7,13)*kap*x*q**(m-1))and badres!=0)
 for eps in [-1,1]:
  s=S.symbols('s',positive=True);incomingC=eps**n*C;incomingD=eps**m*D
  ck(tag+'orientation_'+str(eps),z(C*(eps*s)**n-incomingC*s**n)and z(D*(eps*s)**m-incomingD*s**m))
 for xx in [S.Rational(-1,20),S.Rational(1,20)]:
  for qq in [S.Rational(-1,100),S.Rational(1,100)]:
   pp={x:xx,u:H.subs(x,xx)+qq};value=Om.subs(pp);unit=M.subs(pp)
   ck(tag+'sample_sign_'+str(xx)+'_'+str(qq),unit>0 and value/(D*xx*qq**m)>0)
 cases.append(dict(beta=str(beta),kappa=str(kap),A=str(A),lambda_=str(lam),n=n,m=m,C_u=str(C),D_u=str(D),k=str(k),E1=str(E1),E3=str(E3),scope='Two exact transport equations and divergence; required prompt kinematic equation FAILS. No joint B2 solution.'))
# Sharp allowed gap-one abstract case. It is not a B2 parameter transfer.
A,kap,lam,n,m=S.Integer(2),S.Integer(1),S.Integer(0),4,3;h=S.Rational(1,5);q=u-h*x*x;P=-u+x*x;Theta=x*x*q**n/2;Om=x*q**m-q**n*x-S.Rational(1,5)*x**3*q**(n-1);M=1-q-S.Rational(1,5)*x*x
ck('abstract_gap1_transport',z(act(Theta,A,P))and z(act(Om,A,P)+Om-S.diff(Theta,x)))
ck('abstract_gap1_factorization',z(Om-x*q**m*M));ck('abstract_gap1_source_graph_nonzero',S.diff(Theta,x).subs(u,q0+h*x*x).expand().coeff(q0,m)!=0)
# Same axis data do not select the off-axis homogeneous vorticity: beta2 resonance.
q=u-x*x/11;P=-u+x*x;I=x*q**5;extra=x*q**6*I**2
ck('same_axis_homogeneous_freedom',z(act(extra,S.Integer(5),P)+extra)and S.diff(extra,x).subs(x,0)==0)
# Genuine singular homogeneous modes show why boundedness of lower jets is essential.
xp=S.symbols('xp',positive=True)
for A,kap,m in [(S.Integer(5),S.Integer(1),6),(S.Rational(11,2),S.Rational(1,2),13)]:
 for j in [0,m-1]:
  c=kap*(m-j)/A;g=xp**(-c);label=f'singular_A{A}_j{j}_'
  ck(label+'homogeneous_negative',S.simplify(A*xp*S.diff(g,xp)+kap*(m-j)*g)==0)
  ck(label+'unbounded_negative',S.limit(g,xp,0,dir='+')==S.oo)
  gv=g*S.exp(-xp*xp/2)
  ck(label+'variable_equation_negative',S.simplify(xp*S.diff(gv,xp)+(c+xp*xp)*gv)==0)
  ck(label+'variable_unbounded_negative',S.limit(gv,xp,0,dir='+')==S.oo)
# Division sign is rederived from a generic polynomial stream function, independently.
psi=x*u**2+x**3*u/3+x**5/7;beta=S.Integer(2);W1=beta*x+S.diff(psi,u);P=beta*u-S.diff(psi,x)
kin=S.diff(P,x)-S.diff(W1,u);ck('prompt_kinematic_sign',z(kin+S.diff(psi,x,2)+S.diff(psi,u,2)))
groups={'integrity':[],'constructed_identity_and_parameter_checks':[],'constructed_transverse_coefficients':[],'negative_controls':[],'sampled_signs':[],'orientation_identities':[]}
for c in checks:
 name=c['name'];group=('integrity'if name.startswith(('proof_','dependency_'))else'constructed_transverse_coefficients'if'constructed_lower_coefficient'in name or'leading_transverse_coefficient'in name else'negative_controls'if'negative'in name or'failure_on_graph'in name else'sampled_signs'if'sample_sign'in name else'orientation_identities'if'orientation'in name else'constructed_identity_and_parameter_checks');groups[group].append(name)
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(t['passed']for t in checks),total=len(checks),checks=checks,cases=cases,groups={k:len(v)for k,v in groups.items()},code_sha256=sha(Path(__file__)),proof_sha256=sha(V.parent/'PROOF.md'),scope='Exact finite manufactured consistency and negative controls, not proof or actual B2 candidates. All4B2-parameter manufactures fail prompt Poisson/curl compatibility.')
(V/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','cases']},indent=2));raise SystemExit(0 if all(t['passed']for t in checks)else 1)
