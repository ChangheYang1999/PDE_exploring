"""Manufactured numerical gate for result102, different differentiation paths."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import comb,factorial
import json,hashlib,traceback,time
import mpmath as mp
from polar_derivative_norms import QNormEvaluator,norm_integrand
from q_mp_primitives import MPQPrimitives,mf

root=Path('research/polar_derivative_norms/verification');root.mkdir(exist_ok=True)
out=root/'manufactured.json'
report=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',checks=[],code_sha256=hashlib.sha256(Path('independent_code/polar_derivative_norms.py').read_bytes()).hexdigest(),test_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(Path('research/polar_derivative_norms/PROOF.md').read_bytes()).hexdigest())
def save():out.write_text(json.dumps(report,indent=2)+'\n')
def check(name,error,tol='1e-55'):
    error=abs(error);row=dict(name=name,scaled_absolute_error=mp.nstr(error,30),tolerance=tol,passed=bool(error<mp.mpf(tol)));report['checks'].append(row);save();assert row['passed'],row
save()
try:
    with mp.workdps(100):
        # Whole angular integral by a trapezoid exact for these finite modes,
        # using direct Cartesian numerical differentiation of the Gaussian.
        for rt in ['.037','.6','3']:
            r=mp.mpf(rt);f=lambda x,y:y*mp.exp(-x*x-y*y)
            d={1:mp.taylor(lambda t:mp.exp(-mp.exp(2*t)),mp.log(r),6)}
            for k in range(1,7):
                total=mp.mpf(0);Ntheta=32
                for j in range(Ntheta):
                    th=2*mp.pi*j/Ntheta;x=r*mp.cos(th);y=r*mp.sin(th)
                    total+=mp.fsum(comb(k,a)*mp.diff(f,(x,y),(a,k-a))**2 for a in range(k+1))
                angular=2*mp.pi*total/Ntheta
                polar=norm_integrand(d,r,k)/(r*r)
                check('Gaussian_Cartesian_tensor_'+rt+'_'+str(k),(polar-angular)/(1+abs(angular)))
        coeff=[[F(7,4),F(-1,8),F(3,32)],[F(1,5),F(-1,10)],[F(-1,16)]]
        evaluator=QNormEvaluator(coeff,1,F(3,2),3,dps=90,kmax=6)
        direct=MPQPrimitives(coeff,1,F(3,2),3)
        for rt in ['.13','2.1']:
            r=mp.mpf(rt);t=mp.log(r);dd,pp,rr=evaluator.radial(r)
            def mode(n,t):
                rad=mp.exp(t);s,w=direct.density.coords(rad)
                return direct.density_modes(s,w)[(n-1)//2]
            for n in [1,3,5]:
                for k in range(8):
                    value=mp.diff(lambda u:mode(n,u),t,k)
                    check('Q_log_density_'+rt+'_'+str((n,k)),(factorial(k)*dd[n][k]-value)/(1+abs(value)),'1e-65')
            for m in [2,4,6]:
                for k in range(5):
                    value=mp.diff(lambda u:direct.coefficients(mp.exp(u))[0][m//2-1],t,k)
                    check('Q_log_stream_'+rt+'_'+str((m,k)),(factorial(k)*pp[m][k]-value)/(1+abs(value)),'1e-60')
            for tt in ['.001','.43','1.1']:
                th=mp.mpf(tt);sample=direct.at(r*mp.cos(th),r*mp.sin(th))
                val=mp.fsum(row[0]*mp.sin(n*th) for n,row in rr.items())
                check('Q_residual_modes_'+rt+'_'+tt,(val-sample['R_over_r'])/(1+abs(sample['R_over_r'])),'1e-65')
        # Scale all physical lengths by 2, evaluating corresponding radii.
        scaled=QNormEvaluator(coeff,2,F(3,2),3,dps=90,kmax=6)
        for rt in ['.015','.7','19']:
            r=mp.mpf(rt);a=evaluator.at_radius(r);b=scaled.at_radius(2*r)
            for k in range(2,7):
                for field in ['rho','residual']:
                    target=2**(4-2*k)*a[k][field]
                    check('scaling_integrand_'+rt+'_'+str((k,field)),(b[k][field]-target)/(1+abs(target)),'1e-65')
    report['status']='PASS';report['finished_utc']=datetime.now(timezone.utc).isoformat();report['scope']='Independent Cartesian Gaussian differentiation, Q logarithmic finite-difference derivatives, canonical pointwise residual, and dilation covariance. Empirical precision checks; not interval bounds.';save()
except BaseException:
    report['status']='FAIL';report['finished_utc']=datetime.now(timezone.utc).isoformat();report['traceback']=traceback.format_exc();save();raise
print(json.dumps(dict(status=report['status'],checks=len(report['checks']),utc=report['finished_utc'])),flush=True)
