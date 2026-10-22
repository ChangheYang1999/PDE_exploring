"""Own exact algebra for the previously written proofs87 and88.
No fitting-lane code, numerical inverse, server or external execution.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,time,hashlib
start=time.monotonic();started=datetime.now(timezone.utc).isoformat()
r=S.symbols('r',positive=True);z=S.symbols('z',nonzero=True)
I=S.I;pi=S.pi
cs=lambda n:(z**n+z**(-n))/2
sn=lambda n:(z**n-z**(-n))/(2*I)
th=lambda e:S.expand(I*z*S.diff(e,z))
angular=lambda e:S.expand(e).coeff(z,0)*2*pi
p=S.symbols('p1 p2 p4',real=True);dp=S.symbols('dp1 dp2 dp4',real=True);q=S.symbols('q1 q2 q4',real=True)
fs=[cs(1),sn(2),sn(4)]
K=sn(2)/(2*r**2)
checks=[]
def check(label,expr):
 result=expr
 for _ in range(3):
  result=S.expand(result).replace(lambda node:isinstance(node,S.Pow),lambda node:node.base**S.cancel(node.exp))
  result=S.simplify(S.powsimp(result,force=True))
 checks.append({'check':label,'difference':str(result),'passed':result==0})
 if result!=0:raise AssertionError((label,result))
N=0;pair={}
for i in range(3):
 for j in range(3):
  val=S.factor(angular(q[i]*fs[i]*(-p[j]*th(fs[j])/r*S.diff(K,r)+dp[j]*fs[j]*th(K)/r)*r))
  pair[f'{[1,2,4][i]}_source_{[1,2,4][j]}_stream']=str(val)
  N+=val
  if (i,j) not in [(0,0),(1,2),(2,1)]:check('vanishing_pair_'+str((i,j)),val)
check('mode1_square_integrand',angular(q[0]*fs[0]*(-p[0]*th(fs[0])/r*S.diff(K,r)+dp[0]*fs[0]*th(K)/r)*r)-pi*q[0]*(dp[0]-p[0]/r)/(2*r**2))
c,b=S.symbols('c b',real=True)
plateau=S.factor(N.subs({p[0]:0,dp[0]:0,q[0]:0,p[1]:c*r**2/2,dp[1]:c*r,p[2]:b*r**2,dp[2]:2*b*r,q[1]:0,q[2]:12*b}))
check('plateau_12pi_cb',plateau-12*pi*c*b/r)
h=S.Function('h')(r)
check('negative_square_IBP_integrand',(-r*S.diff(h,r,2)-3*S.diff(h,r))*S.diff(h,r)/r+S.diff(S.diff(h,r)**2/2,r)+3*S.diff(h,r)**2/r)
chi=S.Function('chi')(S.log(r));eta=S.Function('eta')(S.log(r))
for mode,amp,cut in [(2,c/2,chi),(4,b,eta*chi)]:
 radial=amp*r**2*cut
 lap=-S.diff(radial,r,2)-S.diff(radial,r)/r+mode**2*radial/r**2
 expected=amp*((mode**2-4)*cut-5*r*S.diff(cut,r)-r**2*S.diff(cut,r,2))
 check('radial_laplacian_'+str(mode),lap-expected)
s=S.symbols('s',positive=True);beta=1/s;mu=S.symbols('mu',real=True)
qtail=mu*r*(1+r**2)**(-(1+s)/2)
check('horizontal_ray_tail_cancellation',S.powsimp(beta*r*S.diff(qtail,r)+qtail-mu*(beta+1)*r*(1+r**2)**(-(3+s)/2),force=True))
K0=S.symbols('K0',positive=True)
check('logarithmic_coefficient',-3*pi/2*(K0*b/3)**2+12*pi*c*b-pi*(12*c*b-K0**2*b**2/6))
root=Path('research/87_positive_transport_strain_construction/verification')
result={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks.copy(),'angular_pair_integrands_with_dr':pair,'plateau_integrand':str(plateau),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact identities only. Smooth flow, bounds, continuity and IVT are checked in the informal proof, not by symbolic algebra.'}
(root/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
checks=[];t=S.symbols('t',real=True);C,D=S.symbols('C D',real=True);F=S.Function('F',positive=True)(t)
k=2-s;m=1-2*s
check('exponents_m_s_k',m+s-k+1)
check('axis_second_coefficient_identity',2*k-m-3)
check('axis_fourth_coefficient_identity',2*k-3*m-(1+4*s))
for sig in [1,-1]:
 f=sig*F;ht=C*F**(m/k)
 at=C*m/k*S.sin(t)*sig*F**(-(1+s)/k)+D*F**(-s/k)
 ddef=k*f*S.diff(ht,t)-m*S.diff(f,t)*ht
 bdef=k*f*S.diff(at,t)+s*S.diff(f,t)*at-m*S.cos(t)*ht+S.sin(t)*S.diff(ht,t)
 check('angular_transport_sign_'+str(sig),S.powsimp(S.factor(ddef),force=True))
 check('angular_antiderivative_sign_'+str(sig),S.powsimp(S.factor(bdef),force=True))
A,B,P,H=S.symbols('A B P H',real=True)
f=A*t+B*t**3/6;ht=P*t**2/2+H*t**4/24
ddef=S.expand(k*f*S.diff(ht,t)-m*S.diff(f,t)*ht)
check('axis_quadratic_coefficient',ddef.coeff(t,2)-3*A*P/2)
check('axis_quartic_after_A_zero',ddef.subs(A,0).coeff(t,4)-B*P*(1+4*s)/12)
check('axis_vorticity_slope',S.diff(-S.diff(f,t,2)-k**2*f,t).subs(t,0)+B+k**2*A)
result={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'total_elapsed_seconds':time.monotonic()-start,'checks':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact angular and Taylor identities; topological endpoint and boundedness arguments are in PROOF.md.'}
Path('research/88_nonstationary_homogeneous_limit/verification/exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'ALL_PASSED','packet87_checks':13,'packet88_checks':len(checks),'actual_total_seconds':time.monotonic()-start},indent=2))
