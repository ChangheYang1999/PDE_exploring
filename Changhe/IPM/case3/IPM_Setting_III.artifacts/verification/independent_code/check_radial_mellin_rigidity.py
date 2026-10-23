"""Independent finite exact checks supporting the written radial theorem."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,math
checks=[]
def rec(name,condition,**data):
    checks.append(dict(name=name,passed=bool(condition),**data))
    assert condition,name
# Integrate independently after u=sin(theta)^2. Values normalized by pi.
def avg(p):return sum((v*F(2*math.comb(2*k,k),4**k) for k,v in p.items()),F(0))
I0=avg({1:F(1)});I1=avg({1:F(1),2:F(-2)});I2=avg({1:F(2),2:F(-2)})
rec('three_angular_integrals',(I0,I1,I2)==(F(1),-F(1,2),F(1,2)),values=list(map(str,(I0,I1,I2))))
# Independent tensor monomial coefficients of U.grad rho/(pi r), variables J,f,z=r*f'.
coeff={(1,1,0):I1+I2,(1,0,1):I1,(0,2,0):-I2/2}
coeff={k:v for k,v in coeff.items() if v}
rec('nonlinear_projection',coeff=={(1,0,1):-F(1,2),(0,2,0):-F(1,4)},coefficients={str(k):str(v) for k,v in coeff.items()})
for k in range(0,22,2):
    j=F(1,k+4);stream=-j/2
    rec('source_monomial_'+str(k),-((k+2)**2-4)*stream==F(k,2))
    rec('radial_moment_ode_'+str(k),k*j==1-4*j)
rec('center_coefficient',-2*F(1,8)==-F(1,4))
for ell in [F(101,100),F(11,10),F(3,2),F(2),F(5),F(19),F(1000)]:
    D=ell-1;a=4*D;J=D;den=4*ell-2*J;lam=a/den
    rec('origin_exponent_'+str(ell),den==2*ell+2 and 0<lam<2 and 2-lam==4/(ell+1),ell=str(ell),exponent=str(lam),gap=str(2-lam))
# Verify the exact cubic gradient norm separately by polynomial multiplication.
def mul(p,q):
    out={}
    for (i,j),c in p.items():
        for (k,l),d in q.items():out[(i+k,j+l)]=out.get((i+k,j+l),F(0))+c*d
    return out
def add(p,q):
    out=p.copy()
    for k,v in q.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
Hx={(1,1):F(2)};Hy={(2,0):F(1),(0,2):F(7,2)}
G=add(mul(Hx,Hx),mul(Hy,Hy));expected={(4,0):F(1),(2,2):F(11),(0,4):F(49,4)}
rec('cubic_gradient_square',G==expected)
bound={(4,0):F(49,4),(2,2):F(49,2),(0,4):F(49,4)}
diff=add(bound,{k:-v for k,v in G.items()})
rec('cubic_nonnegative_remainder',diff=={(4,0):F(45,4),(2,2):F(27,2)},coefficients={str(k):str(v) for k,v in diff.items()})
rec('cubic_radius_squared',F(49,4)*F(8,49)==2)
report=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,check_count=len(checks),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Finite exact identities; the contradiction and canonical growth argument are proved in PROOF.md. No numerical candidate is certified.')
out=Path('research/radial_mellin_rigidity/verification/checks.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(utc=report['utc'],status=report['status'],check_count=len(checks)),indent=2))
