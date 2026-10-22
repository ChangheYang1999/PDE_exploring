"""Independent symbolic Cartesian variations and arbitrary-n residue controls.
No teammate imports or execution. No PDE or convergence claim.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,time,hashlib
start=datetime.now(timezone.utc).isoformat(); tick=time.monotonic(); checks=[]
def ck(name,e):
 d=S.factor(e);checks.append({'name':name,'passed':d==0,'defect':str(d)})
n=S.symbols('n',integer=True,positive=True)
b,b1,b2,b3,t,Y,J,C,H,k,a,s=S.symbols('b b1 b2 b3 t Y J C H k a s',nonzero=True)
q=(8+2*b1)/b; h=(5+b1)/b; z=(n-1)*q+h
Ddata={b:b1,b1:b2,b2:b3,t:t*q,Y:Y*h,J:t/(b*Y)}
def D(e):return sum(S.diff(e,x)*dx for x,dx in Ddata.items())
eta=Y*(H-C*J);v1=-(b2+eta)/2;theta1=C*t/2;Z=t**(n-1)*Y
K=Y/t*(7+2*b1)/b**2;A=n/S.Integer(3)+1/(2*n+1)
p=(3-2*n)*(n+1)/(6*n);r=(n*(2*n+1)-1)/(2*n*(2*n+1))
gE=n*(-b3/3+b2*q/2)/(b*t)+n*H*K/3-C*A*J*K+C*A/b**2
gF=C*K/(2*n*(2*n+1))
hF=(-(2*n-1)*b3/6+b2*z/2+p*D(eta)+r*eta*z)/(b*t)
for label,dt,dw,dv in [('E',t**n,-2*n*Z*J,Z*J),('F',0,Z,-Z/(2*n))]:
 directT=(2*n*S.Rational(1,3)*D(v1)*dt-v1*D(dt)+2*D(dv)*theta1/(2*n+1)-dv*D(theta1))/(b*t**(n+1))
 wantT=gE if label=='E' else gF
 ck(label+'_thermal_cartesian_variation',S.powsimp(directT-wantT,force=False))
 directO=((2*n-1)*D(v1)*dw/3-v1*D(dw)+D(dv)*eta/(2*n+1)-dv*D(eta))/(b*t**n*Y)
 wantO=hF if label=='F' else -2*n*J*hF-(n*b2+(n-1/(2*n+1))*eta)*D(J)/(b*t)
 ck(label+'_vorticity_cartesian_variation',S.powsimp(directO-wantO,force=False))
 ck(label+'_prior_vorticity_equation',b*D(dw)-((2*n-1)*(4+b1)+1)*dw+2*n*dt)
 ck(label+'_poisson_variation',dv+dw/(2*n))
ck('theta_homogeneous_factor',b*D(t**n)-(8*n+2*n*b1)*t**n)
ck('omega_homogeneous_factor',b*D(Z)-((2*n-1)*(4+b1)+1)*Z)
P=1+k*s;B0=s*P;t0=s**10/P**6;Y0=s**6/P**4
J0=sum((-1)**(j-4)*S.binomial(j-2,2)*k**(j-4)*s**j/S.Integer(j)for j in range(4,13))
def res(e):return S.residue(e,s,0)
sub={b:B0,b1:S.diff(B0,s),b2:S.diff(B0,s,2),b3:0,t:t0,Y:Y0,J:J0}
gF0=S.cancel(gF.subs(sub));gE0=S.cancel(gE.subs(sub));hF0=S.cancel(hF.subs(sub))
# Expand only the finite terms which can contain s^-1; analytic denominators are expanded to order12.
def laurent_res(e):return S.expand(S.series(e,s,0,1).removeO()).coeff(s,-1)
# K is a Laurent polynomial; the sole extra denominator is P^-2 from B^-2.
N0=10*r*(n-1)+6*(p+r);N1=4*r*(n-1)+2*(p+r)
curvT=208*n*a;curvO=(208*n-26)*a
rTE0=-C*A*res(J0*s**-6*(9+4*k*s))-2*C*A*k
rOFeta=-C*res(J0*s**-6*(N0+N1*k*s))+2*p*C*k
rOFthermal=2*(n+1)*res(J0*gF0)
rTE=S.factor((curvT+rTE0).subs(a,-C*k/260))
rOF=S.factor((curvO+rOFeta+rOFthermal).subs(a,-C*k/260))
ck('theta_F_residue',res(gF0))
ck('theta_E_diagonal',rTE-12*C*k/(5*(2*n+1)))
ck('omega_F_diagonal',rOF+9*C*k/(10*n))
ck('explicit_general_n_eta_thermal_identity',3*N0/5-N1/4+2*p-22*(n+1)/(5*n*(2*n+1))-(n+1)*(8*n-9)/(10*n))
ck('determinant',rTE*rOF+54*C*C*k*k/(25*n*(2*n+1)))
ck('curvature_thermal_explicit',n*(-S.Rational(1716,3)+S.Rational(1560,2))*a-curvT)
ck('curvature_vorticity_explicit',(-(2*n-1)*S.Rational(1716,6)+78*(10*n-4))*a-curvO)
# For the lower off-diagonal, factors J force all a corrections beyond the residue;
# terms involving eta's -CJ are analytic. Keep only unperturbed curvature and H terms.
gE_keep=n*k*(10+4*k*s)*P**4*s**-12+n*H*s**-6*(9+4*k*s)/3
hF_keep=k*((10*n-4)+(4*n-2)*k*s)*P**4*s**-12+H*s**-6*(N0+N1*k*s)
last_curv=2*n*k*s**-8*P**2
# eta*J'/(B*t)=H/(B^2) at unperturbed order; residue is -2Hk.
rOE=S.factor(res(2*(n+1)*J0*gE_keep-2*n*J0*hF_keep-last_curv)+2*(n-1/(2*n+1))*H*k)
rOE_tuned=S.factor(rOE.subs(H,-k**7/231))
ck('offdiag_arbitrary_n',rOE_tuned+k**8*(2*n+5)/(385*(2*n+1)))
ck('offdiag_untuned_formula',rOE+3*n*k**8/385+3*H*k*(n+1)*(6*n-5)/(5*(2*n+1)))
ck('offdiag_n2_P308',rOE_tuned.subs(n,2)+9*k**8/1925)
ck('diagonal_n2_P308_T',rTE.subs(n,2)-12*C*k/25)
ck('diagonal_n2_P308_O',rOF.subs(n,2)+9*C*k/20)
# Integer sign/nonvanishing controls are supplemental, not the general proof.
for m in range(2,41):
 ck('n'+str(m)+'_diagonal_product',S.factor((rTE*rOF).subs({n:m,C:3,k:-S.Rational(2,3)}))+S.Rational(216,25*m*(2*m+1)))
V=Path('research/321_all_order_formal_resonance/verification');freeze=json.loads((V/'freeze.json').read_text())
checks.append({'name':'complete_argument_precedes_independent_checks','passed':freeze['utc']<start})
checks.append({'name':'frozen_proof_hash','passed':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==freeze['proof_sha256']})
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(x['passed'] for x in checks),'total':len(checks),'checks':checks,'matrix':[[str(rTE),'0'],[str(rOE_tuned),str(rOF)]],'offdiag_untuned':str(rOE),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact symbolic arbitrary-n identities; finite controls supplement the proof. Formal analytic germs only, no convergence or global B2 claim.'}
(V/'symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2));print('FAILED',[x for x in checks if not x['passed']])
