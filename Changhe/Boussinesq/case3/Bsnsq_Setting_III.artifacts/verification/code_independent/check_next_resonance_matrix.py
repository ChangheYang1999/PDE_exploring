"""Independent symbolic finite-sum proof checks for P308, separate from Fraction recurrence."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,time,hashlib
s,k,C,H,a=S.symbols('s k C H a');x,beta=S.symbols('x beta');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def ck(n,b,d=None):checks.append(dict(name=n,passed=bool(b),detail=d))
P=1+k*s;J=sum((-1)**(n-4)*S.binomial(n-2,2)*k**(n-4)*s**n/S.Integer(n)for n in range(4,13))
def residue(e):return S.expand(e).coeff(s,-1)
poly=S.expand(P**4*(56+24*k*s));coef=S.expand(poly*J).coeff(s,11);ck('six_term_curvature_coefficient',S.simplify(coef+6*k**7/385)==0,str(S.factor(coef)))
RTE=416*a+S.Rational(286,75)*C*k-S.Rational(26,15)*C*k
ROF=390*a+S.Rational(237,100)*C*k-S.Rational(33,25)*C*k
ROE=-6*k**8/S.Integer(385)-S.Rational(63,25)*H*k
rte=S.factor(RTE.subs(a,-C*k/260));rof=S.factor(ROF.subs(a,-C*k/260));roe=S.factor(ROE.subs(H,-k**7/231))
ck('theta_E_coefficient',rte==12*C*k/25,str(rte));ck('omega_F_coefficient',rof==-9*C*k/20,str(rof));ck('omega_E_coefficient',roe==-9*k**8/1925,str(roe));ck('determinant',S.factor(rte*rof)==-27*C**2*k**2/125)
ck('theta_F_residue',residue(C/S.Integer(20)*s**-6*(9+4*k*s))==0)
ck('theta_E_J_residue',S.simplify(residue(-13*C/S.Integer(15)*J*s**-6*(9+4*k*s))-286*C*k/75)==0)
ck('omega_F_J_residue',S.simplify(residue(-C/S.Integer(10)*J*s**-6*(57+22*k*s))-287*C*k/100)==0)
ck('omega_F_thermal_residue',S.simplify(residue(6*J*C/S.Integer(20)*s**-6*(9+4*k*s))+33*C*k/25)==0)
ck('omega_E_H_residue',S.simplify(residue(H/S.Integer(5)*J*s**-6*(66+36*k*s))+18*H*k/5+63*H*k/25)==0)
# Direct Cartesian coefficient expansion for generic functions and beta, without using recurrence solver.
B=S.Function('B')(s);v=[B]+[S.Function('v'+str(i))(s)for i in range(1,5)];th=[0]+[S.Function('t'+str(i))(s)for i in range(1,5)];om=[S.Function('w'+str(i))(s)for i in range(4)]
W2=sum(v[i]*x**(2*i)for i in range(5));W1=(2*beta+S.diff(B,s))*x+sum(S.diff(v[i],s)*x**(2*i+1)/S.Integer(2*i+1)for i in range(1,5));Theta=sum(th[i]*x**(2*i)for i in range(1,5));Omega=sum(om[i]*x**(2*i+1)for i in range(4))
RT=S.expand(W1*S.diff(Theta,x)-W2*S.diff(Theta,s)-(beta-2)*Theta);RO=S.expand(W1*S.diff(Omega,x)-W2*S.diff(Omega,s)+Omega-S.diff(Theta,x));ck('divergence',S.simplify(S.diff(W1,x)-S.diff(W2,s)-2*beta)==0)
for l in range(1,5):
 rhs=sum(S.Rational(2*(l-j),2*j+1)*S.diff(v[j],s)*th[l-j]-v[j]*S.diff(th[l-j],s)for j in range(1,l))
 want=-B*S.diff(th[l],s)+((4*l-1)*beta+2+2*l*S.diff(B,s))*th[l]+rhs;ck(f'thermal_recurrence{l}',S.simplify(RT.coeff(x,2*l)-want)==0)
for j in range(4):
 rhs=-(2*j+2)*th[j+1]+sum(S.Rational(2*(j-i)+1,2*i+1)*S.diff(v[i],s)*om[j-i]-v[i]*S.diff(om[j-i],s)for i in range(1,j+1))
 want=-B*S.diff(om[j],s)+((2*j+1)*(2*beta+S.diff(B,s))+1)*om[j]+rhs;ck(f'vorticity_recurrence{j}',S.simplify(RO.coeff(x,2*j+1)-want)==0)
# The curl of U equals Omega under the prompt's stream sign convention.
U1=W1-beta*x;U2=W2 # subtracting beta*y has zero x derivative
curl=S.expand(-S.diff(U1,s)-S.diff(U2,x))
for j in range(4):ck(f'curl_recurrence{j}',S.simplify(curl.coeff(x,2*j+1)+S.diff(v[j],s,2)/(2*j+1)+(2*j+2)*v[j+1])==0)
V=Path('research/308_next_two_curved_resonances/verification');out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed']for c in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),curvature_polynomial=str(poly),curvature_coefficient=str(coef),matrix=[[str(rte),'0'],[str(roe),str(rof)]])
(V/'symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='checks'},indent=2));print('FAILED',[c for c in checks if not c['passed']])
