"""P300: independent Cartesian polynomial differentiation and scalar endpoint checks."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,hashlib,time
V=Path('research/300_simple_endpoint_next_vorticity_jet/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks=[]
def ck(name,ok,detail=None):checks.append(dict(name=name,passed=bool(ok),detail=detail))
def zero(name,expr):
 v=S.factor(S.cancel(expr));ck(name,v==0,str(v))
x,y,s,beta,ys,u=S.symbols('x y s beta ys u',real=True)
b,T,eta,v,D,gamma,p5=[S.Function(k)(y)for k in ['b','T','eta','v','D','gamma','p5']]
Psi=(b-beta*(y-ys)+u)*x+v*x**3/3+p5*x**5/120
Th=T*x**2/2+D*x**4/24
Om=eta*x+gamma*x**3/6-S.diff(p5,y,2)*x**5/120
U1=-S.diff(Psi,y);U2=S.diff(Psi,x)
W1=beta*x+U1;W2=beta*(y-ys)+U2-u
RT=S.expand(W1*S.diff(Th,x)+W2*S.diff(Th,y)-(beta-2)*Th)
RO=S.expand(W1*S.diff(Om,x)+W2*S.diff(Om,y)+Om-S.diff(Th,x))
E=S.expand(-S.diff(Psi,x,2)-S.diff(Psi,y,2)-Om)
thermal=b*S.diff(T,y)+(3*beta+2-2*S.diff(b,y))*T
axis=b*S.diff(eta,y)+(2*beta+1-S.diff(b,y))*eta-T
fourth=b*S.diff(D,y)+(7*beta+2-4*S.diff(b,y))*D-8*S.diff(v,y)*T+12*v*S.diff(T,y)
third=b*S.diff(gamma,y)+(6*beta+1-3*S.diff(b,y))*gamma-D-2*S.diff(v,y)*eta+6*v*S.diff(eta,y)
zero('stream_x_jet',S.diff(Psi,x).subs(x,0)-(b-beta*(y-ys)+u))
zero('stream_xxx_jet',S.diff(Psi,x,3).subs(x,0)-2*v)
zero('stream_xxxxx_jet',S.diff(Psi,x,5).subs(x,0)-p5)
zero('W2_axis',W2.subs(x,0)-b)
zero('W1_linear',W1.coeff(x,1)-(2*beta-S.diff(b,y)))
zero('thermal_x2',RT.coeff(x,2)-thermal/2)
zero('thermal_x4',RT.coeff(x,4)-fourth/24)
zero('vorticity_x1',RO.coeff(x,1)-axis)
zero('vorticity_x3',RO.coeff(x,3)-third/6)
zero('Poisson_x1',E.coeff(x,1)-(-S.diff(b,y,2)-2*v-eta))
zero('Poisson_x3',E.coeff(x,3)-(-p5-2*S.diff(v,y,2)-gamma)/6)
zero('Poisson_x5',E.coeff(x,5))
for k in [0,1,3,5]:zero('thermal_parity_'+str(k),RT.coeff(x,k))
for k in [0,2,4]:zero('vorticity_parity_'+str(k),RO.coeff(x,k))
zero('Theta_axis',Th.subs(x,0))
zero('Psi_parity',Psi.subs(x,-x)+Psi)
zero('Omega_parity',Om.subs(x,-x)+Om)
zero('Theta_parity',Th.subs(x,-x)-Th)
# Signed-coordinate conversion is independent of any numerical solver code.
bs,ts,es,vs,ds,gs=[S.Function(k)(s)for k in ['B','t','e','v','d','g']]
for eps in (-1,1):
 yp={b:eps*bs,gamma:gs,D:ds,eta:es,v:vs}
 for fn,n in [(b,1),(gamma,1),(eta,1),(v,1)]:yp[S.diff(fn,y)]=-eps*S.diff(yp[fn],s)
 converted=third.subs(yp,simultaneous=True)
 target=-bs*S.diff(gs,s)+(6*beta+1+3*S.diff(bs,s))*gs-ds+2*eps*S.diff(vs,s)*es-6*eps*vs*S.diff(es,s)
 zero('signed_next_equation_'+str(eps),converted-target)
C=S.symbols('C',nonzero=True,real=True);ell=S.symbols('ell',real=True);bp=S.symbols('beta_pos',positive=True);c=3*bp+2;a=4*bp+3;a0=5-3/c
zero('a0_identity',3+(6*bp+1)/c-a0)
for q in (0,1):
 m=6-q;zero('positive_gap_identity_'+str(q),m-a0-(1-q+3/c));ck('positive_gap_'+str(q),S.ask(S.Q.positive(m-a0)))
 for eps in (-1,1):
  h0=-C/a;w0=eps*ell*C*(bp-2+q*c)/(4*(1+2*q));eta0=s**3*h0;v0=s**(4-q)*w0;D0=ell*s**m*C**2
  force=-D0+2*eps*S.diff(v0,s)*eta0-6*eps*v0*S.diff(eta0,s)
  zero(f'forcing_order_{q}_{eps}',force/s**m-(-ell*C**2-2*eps*(5+q)*w0*h0))
  expected=-ell*C**2/a if q else -ell*C**2*(3*bp+16)/(2*a*(3*bp+5))
  zero(f'leading_coefficient_{q}_{eps}',force/s**m/(c*(m-a0))-expected)
 for j in range(m,m+7):
  ck(f'coefficient_gap_q{q}_{j}',S.ask(S.Q.positive(j-a0)))
  zero(f'scalar_inverse_q{q}_{j}',s*S.diff(s**j/(j-a0),s)-a0*s**j/(j-a0)-s**j)
# The exact finite-polynomial realization uses Omega=-Delta Psi, so E is identically zero.
Om_exact=-S.diff(Psi,x,2)-S.diff(Psi,y,2)
zero('exact_Poisson_local',-S.diff(Psi,x,2)-S.diff(Psi,y,2)-Om_exact)
zero('exact_eta_jet',S.diff(Om_exact,x).subs(x,0)+S.diff(b,y,2)+2*v)
zero('exact_gamma_jet',S.diff(Om_exact,x,3).subs(x,0)+p5+2*S.diff(v,y,2))
f=json.loads((V/'freeze.json').read_text());sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
ck('proof_precedes_controls',f['proof_written_utc']<start);ck('proof_unchanged',sha(V.parent/'PROOF.md')==f['proof_sha256']);ck('P299_dependency_unchanged',sha('research/299_simple_endpoint_all_limits/PROOF.md')==f['P299_proof_sha256'])
d=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=sha(__file__))
(V/'checks.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items()if k!='checks'},indent=2));print('FAILURES',json.dumps([x for x in checks if not x['passed']],indent=2))
