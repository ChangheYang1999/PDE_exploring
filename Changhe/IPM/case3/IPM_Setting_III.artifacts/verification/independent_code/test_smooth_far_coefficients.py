"""Manufactured far coefficient checks, independent angular differentiation."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from smooth_mp_primitives import SmoothMP,number
from smooth_exact_high_jets import enc
from smooth_far_coefficients import coefficients
assert json.loads(Path('research/smooth_full_inverse_primitives/verification/manufactured.json').read_text())['status']=='PASS'
checks=[]
def make(alpha,ell,co):
    return SmoothMP(dict(alpha=enc(alpha),length=enc(F(5,4)),cl=enc(ell),chebyshev_coefficients=[[enc(v)for v in row]for row in co]),85)
co=[[F((-1)**(k+j)*(k+2*j+1),(k+2)*(j+3))for j in range(4)]for k in range(4)]
with mp.workdps(110):
    rows=[]
    for alpha in [F(1,5),F(3,10),F(49,100)]:
        model=make(alpha,F(5,2),co);p=number(model.p);L=number(model.L)
        def theta(t):
            # At w=0, P_k(1) is the sum of the original Chebyshev coefficients.
            return L**(1-p)*mp.sin(t)*mp.fsum(number(sum(row,F(0)))*mp.cos(2*k*t)for k,row in enumerate(co))
        for ts in ['.03','.27','.73','1.3','1.55']:
            t=mp.mpf(ts);v=coefficients(model,t)
            direct=p*mp.cos(t)*theta(t)-mp.sin(t)*mp.diff(theta,t)
            modal=mp.fsum(s*mp.sin(2*j*t)for j,s in enumerate(v['source_coefficients'],1))
            err=abs(direct-modal);assert err<mp.mpf('1e-90'),(alpha,t,err)
            rows.append(dict(alpha=str(alpha),theta=ts,error=mp.nstr(err,10)))
    checks.append(dict(test='leading source versus separate angular derivative of original coefficients',cases=len(rows),rows=rows))
    radial=[]
    for alpha in [F(1,5),F(3,10),F(49,100)]:
        p=1-2*alpha;model=make(alpha,1/p,[[F(7,3)]])
        for ts in ['.1','.4','1.2']:
            t=mp.mpf(ts);v=coefficients(model,t);amp=number(F(7,3))*number(model.L)**(1-number(p))
            expected=-amp*amp*mp.sin(t)*(mp.cos(t)**2+number(p)*mp.sin(t)**2)/(number(p)+3)
            err=abs(v['E1']-expected);assert err<mp.mpf('1e-90')
            assert v['leading_defect']==0
            radial.append(dict(alpha=str(alpha),theta=ts,error=mp.nstr(err,10)))
    checks.append(dict(test='closed radial nonlinear residual coefficient',cases=len(radial),rows=radial))
# Actual canonical inverse and residual approach the independently computed E1.
model=make(F(3,10),F(5,2),co);asymptotic=[]
with mp.workdps(model.working_digits):
    t=mp.mpf('.37');v=coefficients(model,t);p=number(model.p);ell=number(model.ell)
    for rs in ['1e4','1e8','1e12']:
        r=mp.mpf(rs);x=r*mp.cos(t);y=r*mp.sin(t)
        rho=model.density(x,y);gx=mp.diff(lambda u:model.density(u,y),x);gy=mp.diff(lambda u:model.density(x,u),y)
        _,ux,uy=model.stream_velocity(x,y);R=(ell*x+ux)*gx+(ell*y+uy)*gy-rho
        error=abs(R/r**(2*p-1)-v['E1'])/(1+abs(v['E1']))
        asymptotic.append(dict(radius=rs,normalized_coefficient_error=mp.nstr(error,15)))
    assert mp.mpf(asymptotic[-1]['normalized_coefficient_error'])<mp.mpf('1e-5')
    assert all(mp.mpf(a['normalized_coefficient_error'])>mp.mpf(b['normalized_coefficient_error'])for a,b in zip(asymptotic,asymptotic[1:]))
checks.append(dict(test='full canonical residual next asymptotic term',cases=3,rows=asymptotic))
# Exact binary-alpha defect is deliberately nonzero even at printed p=0.4.
alpha=F((1-float(.4))/2);defect=F(5,2)*(1-2*alpha)-1
assert defect==F(1,18014398509481984)
checks.append(dict(test='stored binary exponent is not repaired',cases=1,defect=str(defect)))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),implementation_sha256=hashlib.sha256(Path('independent_code/smooth_far_coefficients.py').read_bytes()).hexdigest(),scope='Manufactured identities and finite asymptotic checks; no uniform or interval residual bound.')
Path('research/smooth_far_residual_coefficient/verification/manufactured.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
