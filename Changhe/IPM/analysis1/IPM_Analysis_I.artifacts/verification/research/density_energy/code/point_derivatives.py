"""Exact X3 derivative balls away from the axes and knots, with span assertions."""
import os,sys,bisect,json,hashlib
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from strain_arb import Data,aa,horner,cheb,jsball
ctx.prec=180;ctx.cap=8;ctx.threads=1
class Point:
 def __init__(self):
    self.d=Data();assert len(self.d.tc)==6
 def evaluate(self,r,th):
    d=self.d;u=r/d.L;ell=(1+u*u).log();s=u*u/(1+u*u);chi=u*u/(u*u+d.r0*d.r0)
    q=1-(-(1-d.k)*ell/2).exp();qt=(1-d.k)*s*(1-q)
    span=bisect.bisect_right(d.t,F.from_float(float(q.mid())))-1
    assert q>d.ta[span] and q<d.ta[span+1],('span not proven',span,q)
    mid,rows=d.poly(d.t[span],d.t[span+1]);bs=horner(rows,q-mid).tolist()[0]
    dbs=horner([j*rows[j] for j in range(1,len(rows))],q-mid).tolist()[0]
    H=(d.k-3)*ell/2;Ht=(d.k-3)*s;Ha=arb(0)
    for m in range(d.nm):
      jp=max(0,m-1);mult=chi**jp;R=bs[m]*mult;Rt=mult*(dbs[m]*qt+2*jp*(1-chi)*bs[m])
      H+=R*(2*m*th).cos();Ht+=Rt*(2*m*th).cos();Ha+=-2*m*R*(2*m*th).sin()
    z=2*q-1;T=cheb(z,d.tc)
    # Explicit Chebyshev derivative polynomial, independently from Clenshaw.
    Td=d.tc[1]+4*d.tc[2]*z+d.tc[3]*(12*z*z-3)+d.tc[4]*(32*z**3-16*z)+d.tc[5]*(80*z**4-60*z*z+5)
    Z=s**(d.p/2)*T;Zt=d.p*(1-s)*Z+2*s**(d.p/2)*Td*qt
    co,si=th.cos(),th.sin();sing=co**(d.p-2)*si**2
    singa=2*co**(d.p-1)*si-(d.p-2)*co**(d.p-3)*si**3
    H+=Z*sing;Ht+=Zt*sing;Ha+=Z*singa
    A=co**2*si;Ap=co**3-2*co*si**2;factor=r**3*H.exp();rho=factor*A
    rhot=(3+Ht)*rho;rhoa=factor*(Ap+A*Ha)
    rx=(rhot*co-rhoa*si)/r;ry=(rhot*si+rhoa*co)/r
    return {'rho':rho,'rho_x':rx,'rho_y':ry,'H':H,'H_t':Ht,'H_theta':Ha,'span':span}
if __name__=='__main__':
 p=Point();r=aa(F(25,2));th=aa(F(31,25));values=p.evaluate(r,th);gap=(values['rho_x']-values['rho_y'])/2-(1/p.d.k+1)
 gap6=(values['rho_x']-values['rho_y'])/2-7
 assert gap>0 and gap6>aa(F(313,100)) and 1/p.d.k<6
 result={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':p.d.sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'r_exact':'25/2','theta_exact':'31/25','bits':180,'values':{k:jsball(v) if isinstance(v,arb) else v for k,v in values.items()},'positive_gap':jsball(gap),'positive_gap_for_all_cl_le_6':jsball(gap6),'status':'CONFIRMED_POINT_INEQUALITY','scope':'Refutes positive unweighted density L2 coercivity for this exact trial and every cl <= 6; no spectral, inverse or existence conclusion.'}
 (BASE/'research/density_energy/evidence/point_witness.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
