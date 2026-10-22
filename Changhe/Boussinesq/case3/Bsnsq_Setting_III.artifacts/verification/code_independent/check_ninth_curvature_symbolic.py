"""P311 independent finite symbolic residue identities and Cartesian PDE expansion."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,time,hashlib
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
s,k,C,H,c,a,e,x=S.symbols('s k C H c a e x');P=1+k*s

def ck(n,b,d=None):checks.append(dict(name=n,passed=bool(b),detail=d))
def eq(n,l,r):ck(n,S.simplify(l-r)==0,str(S.factor(l)))
def res(f):return S.expand(f).coeff(s,-1)
J=sum((-1)**(n-4)*S.binomial(n-2,2)*k**(n-4)*s**n/S.Integer(n)for n in range(4,13))
L=s**8-S.Rational(2,9)*k*s**9-S.Rational(2,5)*k**2*s**10+S.Rational(10,11)*k**3*s**11
B=s*P+e*s**9;q=(8+2*S.diff(B,s))/B;h=(5+S.diff(B,s))/B
qvar=S.diff(q,e).subs(e,0);hvar=S.diff(h,e).subs(e,0)
eq('log_t_variation',qvar,s**7*(8+14*k*s)/P**2)
eq('log_Y_variation',hvar,s**7*(3+7*k*s)/P**2)
Ldef=S.expand(P**2*S.diff(L,s)-s**7*(8+14*k*s))
ck('L_first_four_coefficients',all(Ldef.coeff(s,n)==0 for n in range(11)))
Qcurv=12*k/C*s**-12*(10+4*k*s)*P**4
QH=4*H/C*s**-6*(9+4*k*s)
QJ=-4*s**-6*(9+4*k*s)*J
# The last rational term needs only its coefficient of s at a pole s^-2.
eq('quadratic_D_residue',res(Qcurv+QH+QJ)-8*k,S.Rational(48,5)*k)
eq('quadratic_gamma_Dpart',C**2*res(J*(Qcurv+QH)),-S.Rational(88,5)*C*H*k-S.Rational(16,385)*C*k**8)
eq('quadratic_gamma_linear_eta',res(-6*C*k*J*s**-12*(6+2*k*s)*P**4),C*k**8/55)
eq('quadratic_gamma_quadratic_eta',res(2*s**-6*(6+2*k*s)*(H-C*J)**2)+4*C*H*k,S.Rational(82,5)*C*H*k)
quadratic_g=-S.Rational(6,5)*C*H*k-S.Rational(9,385)*C*k**8
eq('quadratic_gamma_sum',-S.Rational(88,5)*C*H*k-S.Rational(16,385)*C*k**8+C*k**8/55+S.Rational(82,5)*C*H*k,quadratic_g)
eq('D_c_explicit_derivatives',res(288*c/C*s**-5*P**4*(8-k*s)),1152*c*k**4/C)
eq('D_c_q_B_denominator',res(24*k*c/C*s**-4*P**3*(-1+5*k*s)),336*c*k**4/C)
SD=S.expand((10+4*k*s)*P**4*L).coeff(s,11)
eq('D_c_unit_finite_sum',SD,k**3*(64-S.Rational(152,9)-S.Rational(88,5)+S.Rational(100,11)))
rDc=S.simplify(1152*c*k**4/C+336*c*k**4/C-12*k*c/C*SD)
eq('D_c_total',rDc,S.Rational(169088,165)*c*k**4/C)
eq('D_a_total',(-4*1716+6*156*10)*a/C,2496*a/C)
eq('gamma_cH_explicit',res(72*c*H*s**-5*P**4*(11-k*s)),504*c*H*k**4)
eq('gamma_cH_h_B_denominator',res(6*k*c*H*s**-4*P**3*(-3+5*k*s)),72*c*H*k**4)
SG=S.expand((6+2*k*s)*P**4*L).coeff(s,11)
eq('gamma_cH_unit_finite_sum',SG,k**3*(36-S.Rational(88,9)-S.Rational(52,5)+S.Rational(60,11)))
rGcH=S.simplify(576*c*H*k**4-6*c*H*k*SG)
eq('gamma_cH_total',rGcH,S.Rational(517832,1155)*c*H*k**4)
eq('gamma_a_total',(-1716+3*156*6)*a*H,1092*a*H)
eq('gamma_Cc_D',S.Rational(2304,4)*C*c,576*C*c)
eq('gamma_Cc_first_nonthermal',-S.Rational(-504+3*72*6,4)*C*c,-198*C*c)
eq('gamma_Cc_second_nonthermal',-3*72*C*c,-216*C*c)
eq('gamma_Cc_total',(576-198-216)*C*c,162*C*c)
rD=S.Rational(48,5)*k+2496*a/C+rDc
rG=quadratic_g+1092*a*H+rGcH+162*C*c
alead=-C*k/260-S.Rational(2642,6435)*c*k**4
ctuned=k*(231*H+k**7)/6930
eq('D_tuned_a',rD.subs(a,alead),0)
eq('gamma_after_a',rG.subs(a,alead),162*C*c-9*C*k*(231*H+k**7)/385)
eq('gamma_tuned_c',rG.subs(a,alead).subs(c,ctuned),0)
eq('cH_exact_cancellation',1092*S.Rational(2642,6435),S.Rational(517832,1155))
eq('lead_D_formula',rD,16*(99*C*k+25740*a+10568*c*k**4)/(165*C))
eq('lead_gamma_formula',rG,(-1386*C*H*k+187110*C*c-27*C*k**8+1261260*H*a+517832*H*c*k**4)/1155)
# Direct independent Cartesian polynomial coefficient extraction.
B=S.Function('B')(s);v=S.Function('v')(s);p=S.Function('p')(s);T=S.Function('T')(s);D=S.Function('D')(s);eta=S.Function('eta')(s);gamma=S.Function('gamma')(s)
W1=(4+S.diff(B,s))*x+S.diff(v,s)*x**3/3+S.diff(p,s)*x**5/5;W2=B+v*x**2+p*x**4
Theta=T*x**2/2+D*x**4/24;Omega=eta*x+gamma*x**3/6
RT=S.expand(W1*S.diff(Theta,x)-W2*S.diff(Theta,s));RO=S.expand(W1*S.diff(Omega,x)-W2*S.diff(Omega,s)+Omega-S.diff(Theta,x))
eq('Cartesian_T_equation',2*RT.coeff(x,2),-B*S.diff(T,s)+(8+2*S.diff(B,s))*T)
eq('Cartesian_D_equation',24*RT.coeff(x,4),-B*S.diff(D,s)+(16+4*S.diff(B,s))*D+8*S.diff(v,s)*T-12*v*S.diff(T,s))
eq('Cartesian_eta_equation',RO.coeff(x,1),-B*S.diff(eta,s)+(5+S.diff(B,s))*eta-T)
eq('Cartesian_gamma_equation',6*RO.coeff(x,3),-B*S.diff(gamma,s)+(13+3*S.diff(B,s))*gamma-D+2*S.diff(v,s)*eta-6*v*S.diff(eta,s))
curl=S.expand(-S.diff(W1,s)-S.diff(W2,x))
eq('Cartesian_curl_x',curl.coeff(x,1),-S.diff(B,s,2)-2*v)
eq('Cartesian_curl_x3',curl.coeff(x,3),-S.diff(v,s,2)/3-4*p)
eq('Cartesian_divergence',S.diff(W1,x)-S.diff(W2,s),4)
# k=0 exact primitive from the proof, not the invalid zero multiple of s^-11.
eta0=H*s**6-C*s**10/4;Qzero=(36*eta0)/(C*s**12)+4/s**2;Izero=-36*H/(5*C)*s**-5+5/s
eq('zero_curvature_I_exact',S.diff(Izero,s),Qzero)
V=Path('research/311_ninth_order_curvature/verification');fr=json.loads((V/'freeze.json').read_text());ck('proof_precedes_controls',fr['utc']<start);ck('proof_hash',hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==fr['proof_sha256'])
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),general_D_residue=str(S.factor(rD)),general_gamma_residue=str(S.factor(rG)))
(V/'symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='checks'},indent=2));print('FAILED',[x for x in checks if not x['passed']])
