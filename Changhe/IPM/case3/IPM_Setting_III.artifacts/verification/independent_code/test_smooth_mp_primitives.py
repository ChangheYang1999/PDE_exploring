"""Independent manufactured gate for source primitives and full MP inverse."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from smooth_mp_primitives import SmoothMP,number,chebyshev_polynomial_w
from smooth_exact_high_jets import enc,cheb_to_w,solve

def inputs(alpha,L,coeff):
    return dict(alpha=enc(alpha),length=enc(L),cl=enc(F(5,2)),chebyshev_coefficients=[[enc(v)for v in row]for row in coeff])
checks=[]
def progress(phase,**data):
    row=dict(utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',phase=phase,completed_groups=len(checks),**data)
    Path('research/smooth_full_inverse_primitives/verification/manufactured_progress.json').write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps(row),flush=True)
progress('started')
for n in range(13):
    co=[F((-1)**j*(j+1),j+3)for j in range(n+1)]
    assert chebyshev_polynomial_w(co)==cheb_to_w(co)
checks.append(dict(test='independent exact Chebyshev conversion',cases=13))
# A separate closed radial stream, with derivatives taken directly by mp.diff.
radial=[]
for alpha in [F(1,5),F(3,10),F(49,100)]:
    d=inputs(alpha,F(5,4),[[F(7,3)]]);model=SmoothMP(d,75)
    for rs in ['1e-12','.1','.55','1.3','11','1e6','1e80','1e250']:
        with mp.workdps(model.working_digits):
            r=mp.mpf(rs);th=mp.mpf('.37');x=r*mp.cos(th);y=r*mp.sin(th)
            aa=number(F(7,3));al=number(alpha);L=number(F(5,4))
            def psi(s,t):
                z=(s*s+t*t)/(L*L)
                return -aa*s*t*mp.hyp2f1(al,2,3,-z)/4
            expected=[psi(x,y),-mp.diff(lambda t:psi(x,r*t)/r,y/r),mp.diff(lambda s:psi(r*s,y)/r,x/r)]
            actual=model.stream_velocity(x,y)
            errors=[abs(u-v)/max(abs(v),mp.mpf('1e-150'))for u,v in zip(actual,expected)]
            assert max(errors)<mp.mpf('1e-65'),(alpha,rs,errors)
            radial.append(dict(alpha=str(alpha),radius=rs,max_relative_error=mp.nstr(max(errors),10)))
            assert model.c==-F(7,12)
            progress('closed radial inverse',alpha=str(alpha),radius=rs,error=mp.nstr(max(errors),10))
checks.append(dict(test='closed radial full-plane stream and velocity',cases=len(radial),rows=radial))
co=[[F((-1)**(k+j)*(k+2*j+1),(k+2)*(j+3))for j in range(4)]for k in range(4)]
d=inputs(F(3,10),F(5,4),co);model=SmoothMP(d,75);exact=solve(d,3)
assert model.c==exact['c'];assert model.C==[cheb_to_w(row)for row in co]
with mp.workdps(95):
    pointchecks=[]
    for rs in ['.13','.7','2.4','19']:
        for ts in ['.13','.51','1.19']:
            r=mp.mpf(rs);t=mp.mpf(ts);x=r*mp.cos(t);y=r*mp.sin(t)
            direct=mp.diff(lambda q:model.density(q,y),x)
            angular=mp.fsum(v*mp.sin(2*j*t)for j,v in enumerate(model.source_modes(r),1))
            err=abs(direct-angular)
            assert err<mp.mpf('1e-80'),(rs,ts,err)
            pointchecks.append(dict(radius=rs,theta=ts,source_error=mp.nstr(err,8)))
checks.append(dict(test='factored source versus Cartesian derivative of separate density recurrence',cases=len(pointchecks),rows=pointchecks))
# Integrate a separately differentiated density-mode source. This check does
# not call source_modes or the finite primitive formulas in its integrand.
with mp.workdps(75):
    alpha=number(F(3,10));L=number(F(5,4));r=mp.mpf('.73')
    def g(k,s):
        if not 0<=k<len(co):return mp.mpf(0)
        z=(s/L)**2;w=(1+z)**(-alpha);t=1-2*w
        pk=mp.fsum(number(c)*mp.chebyt(j,t)for j,c in enumerate(co[k]))
        return (z/(1+z))**k*w*pk
    def f(m,s):
        k=(m-1)//2
        return s*(g(0,s)-g(1,s)/2)if k==0 else s*(g(k,s)-g(k+1,s))/2
    def independent_source(j,s):
        n=2*j
        return (mp.diff(lambda q:f(n-1,q),s)-(n-1)*f(n-1,s)/s+mp.diff(lambda q:f(n+1,q),s)+(n+1)*f(n+1,s)/s)/2
    got=model.modal_integrals(r);integrals=[]
    for j in range(1,model.M+1):
        P=mp.quad(lambda u:u**(2*j+1)*independent_source(j,r*u),[0,mp.mpf('.5'),1])
        Q=mp.quad(lambda u:u**(2*j-3)*independent_source(j,r/u),[0,mp.mpf('.5'),1])
        errors=[abs(P-got[j-1][0]),abs(Q-got[j-1][1])]
        assert max(errors)<mp.mpf('1e-45'),(j,errors)
        integrals.append(dict(mode=2*j,inner_error=mp.nstr(errors[0],8),exterior_error=mp.nstr(errors[1],8)))
        progress('independent exterior quadrature',mode=2*j,error=mp.nstr(max(errors),8))
checks.append(dict(test='independently differentiated source quadrature to infinity',cases=len(integrals),rows=integrals))
# Full residual precision and exact symmetry-zero checks, including tiny angles.
precision=[]
for xy in [('.43','.79'),('.003','3e-13'),('0','1'),('1','0'),('6e49','8e49'),('6e249','8e249')]:
    a=SmoothMP(d,65).fields(*xy);b=SmoothMP(d,100).fields(*xy)
    with mp.workdps(110):
        differences={k:abs(mp.mpf(a[k])-mp.mpf(b[k]))/max(abs(mp.mpf(b[k])),mp.mpf('1e-130'))for k in ['rho','U1','U2','rho_x','rho_y','R','Nf','Nv']if a[k]is not None}
        assert max(differences.values())<mp.mpf('1e-55'),(xy,differences)
    if xy[1]=='0':assert a['R_Nf']is None and a['R_Nv']is None and mp.mpf(a['R'])==0
    precision.append(dict(point=xy,max_relative_change=mp.nstr(max(differences.values()),8)))
    progress('residual precision',point=xy,error=mp.nstr(max(differences.values()),8))
checks.append(dict(test='full residual precision comparison and symmetry zeros',cases=len(precision),rows=precision))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),implementation_sha256=hashlib.sha256(Path('independent_code/smooth_mp_primitives.py').read_bytes()).hexdigest(),mpmath_version=mp.__version__,scope='Manufactured identity and precision tests. Quadrature and precision agreement are empirical; no interval error bound is asserted.')
p=Path('research/smooth_full_inverse_primitives/verification/manufactured.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(utc=result['utc'],status=result['status'],checks=[dict(test=r['test'],cases=r['cases'])for r in checks])),flush=True)
