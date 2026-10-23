"""Independent Cartesian and Fourier tests of the finite residual convolution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,traceback
import mpmath as mp
from smooth_exact_high_jets import enc
from smooth_mp_primitives import SmoothMP,number
from q_mp_primitives import MPQPrimitives
from finite_angular_residual_projection import q_density_modes,q_modes,smooth_density_modes,smooth_modes,convolve,direct_angular_residual

out=Path('research/finite_angular_residual_projection/verification/manufactured.json')
report=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',checks=[],code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),implementation_sha256=hashlib.sha256(Path('independent_code/finite_angular_residual_projection.py').read_bytes()).hexdigest())
def save():out.write_text(json.dumps(report,indent=2)+'\n')
def check(name,error,tol='1e-70',**extra):
    row=dict(name=name,error=mp.nstr(abs(error),20),tolerance=tol,passed=bool(abs(error)<mp.mpf(tol)),**extra);report['checks'].append(row);save();print(json.dumps(row),flush=True);assert row['passed'],row
save()
try:
    for path in ['research/smooth_full_inverse_primitives/verification/manufactured.json','research/q_full_inverse_primitives/verification/manufactured.json']:
        assert json.loads(Path(path).read_text())['status']=='PASS'
    # Exact rational radial specialization, independent of transcendental calls.
    for ell in [F(11,10),F(2),F(19)]:
        for f,J,z in [(F(2),F(1,3),F(-3)),(F(7,4),F(-2),F(5,3))]:
            got=convolve(ell,[f],[f+z],[J],[J-f/2])[0]
            expected=(ell-J/2)*z+(ell-1)*f-f*f/4
            assert got==expected
            check('exact_radial_specialization_'+str(ell)+'_'+str(f),mp.mpf(0))
    co=[[F((-1)**(j+k)*(j+1),2**(k+3))for k in range(5)]for j in range(3)]
    with mp.workdps(125):
        q=MPQPrimitives(co,F(5,4),F(2),F(5,2))
        s=SmoothMP(dict(alpha=enc(F(3,10)),length=enc(F(5,4)),cl=enc(F(5,2)),chebyshev_coefficients=[[enc(v)for v in row]for row in co]),95)
        for kind,model,density,modes in [('Q',q,q_density_modes,q_modes),('smooth',s,smooth_density_modes,smooth_modes)]:
            ell=number(model.ell)
            for text in ['.013','.7','12','1e12']:
                r=mp.mpf(text);rows=modes(model,r);g,e,u,v=rows;c=convolve(ell,*rows)
                errors=[]
                for j in range(model.M):
                    numerical=g[j]+r*mp.diff(lambda rr:density(model,rr)[0][j],r)
                    errors.append(abs(numerical-e[j])/(1+abs(e[j])))
                check(kind+'_radial_derivatives_'+text,max(errors),'1e-90')
                errors=[]
                for theta in map(mp.mpf,['.11','.53','1.21']):
                    x=r*mp.cos(theta);y=r*mp.sin(theta)
                    if kind=='Q':R=model.at(x,y)['R_over_r']
                    else:
                        rho=model.density(x,y);gx=mp.diff(lambda z:model.density(r*z,y)/r,x/r);gy=mp.diff(lambda z:model.density(x,r*z)/r,y/r)
                        _,ux,uy=model.stream_velocity(x,y);R=((ell*x+ux)*gx+(ell*y+uy)*gy-rho)/r
                    reconstructed=mp.fsum(cc*mp.sin((2*j+1)*theta)for j,cc in enumerate(c))
                    errors.append(abs(R-reconstructed)/(1+abs(R)))
                check(kind+'_Cartesian_residual_'+text,max(errors),'1e-85')
                count=128;theta=[2*mp.pi*j/count for j in range(count)]
                direct=[direct_angular_residual(ell,*rows,t)for t in theta]
                errors=[]
                for j,cc in enumerate(c):
                    projected=2*mp.fsum(value*mp.sin((2*j+1)*t)for t,value in zip(theta,direct))/count
                    errors.append(abs(projected-cc)/(1+abs(cc)))
                check(kind+'_periodic_projection_'+text,max(errors),'1e-95')
                square=2*mp.fsum(value*value for value in direct)/count
                check(kind+'_Parseval_'+text,abs(square-mp.fsum(cc*cc for cc in c))/(1+abs(square)),'1e-95')
    report['status']='PASS';report['finished_utc']=datetime.now(timezone.utc).isoformat();report['scope']='Finite exact radial identities, scalar multiprecision differentiation, separately evaluated Cartesian residuals, and periodic projection. Numerical agreement is not an interval enclosure.';save()
except BaseException:
    report['status']='FAIL';report['finished_utc']=datetime.now(timezone.utc).isoformat();report['traceback']=traceback.format_exc();save();raise
print(json.dumps(dict(status=report['status'],checks=len(report['checks']))),flush=True)
