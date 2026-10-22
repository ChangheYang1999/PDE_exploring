"""Exact algebra and independent angular/radial check of packet81's base moment."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,math,hashlib
import numpy as np
from scipy.integrate import quad
from scipy.special import expit
import sympy as S
r=S.symbols('r',positive=True);a=S.Function('a')(r);e=S.Function('e')(r)
ap=S.diff(a,r);ep=S.diff(e,r)
H2=-5*r*ap-r*r*S.diff(a,r,2);H4=12*e-5*r*ep-r*r*S.diff(e,r,2)
old=H4*(2*a/r+ap/2)+H2*(-e/r+ep/2)
new=24*a*e/r+9*(e*ap-a*ep)-3*r*ap*ep
primitive=-2*r*a*ep+r*e*ap-r*r*ap*ep/2+a*e
err=S.simplify(old-new-S.diff(primitive,r));assert err==0

def chi(t):
 if t<=1:return 1.,0.,0.
 if t>=2:return 0.,0.,0.
 u=t-1;v=2-t;A=1/u-1/v;D=-1/u**2-1/v**2;DD=2/u**3-2/v**3
 h=expit(A);hp=h*(1-h)*D;hpp=h*(1-h)*((1-2*h)*D*D+DD)
 return h,hp,hpp
I,errI=quad(lambda s:chi(s)[0]*(1-chi(s)[0])/s,1,2,epsabs=1e-13,epsrel=1e-13)
J,errJ=quad(lambda s:s*chi(s)[1]**2,1,2,epsabs=1e-13,epsrel=1e-13)
C=12*I+4.5+1.5*J
beta=3.;c=1+beta/2;b0=(beta-2)/32
angles=2*np.pi*(np.arange(128)+.217)/128
s2=np.sin(2*angles);co2=np.cos(2*angles);s4=np.sin(4*angles);co4=np.cos(4*angles)
rows=[]
for R in [16.,32.,64.,128.]:
 def integrand(rad):
  f,fp,fpp=chi(rad/R);fp/=R;fpp/=R*R
  ci,cip,cipp=chi(rad);eta=1-ci;etap=-cip;etapp=-cipp
  av=c*f/2;apv=c*fp/2;app=c*fpp/2
  ev=b0*eta*f;epv=b0*(etap*f+eta*fp);epp=b0*(etapp*f+2*etap*fp+eta*fpp)
  A=rad*rad*av;Aprime=2*rad*av+rad*rad*apv
  E=rad*rad*ev;Eprime=2*rad*ev+rad*rad*epv
  omega=(-5*rad*apv-rad*rad*app)*s2+(12*ev-5*rad*epv-rad*rad*epp)*s4
  vr=-(2*A*co2+4*E*co4)/rad;vt=Aprime*s2+Eprime*s4
  K_r=-s2/rad**3;K_theta_over_r=co2/rad**3
  return float(2*np.pi*np.mean(omega*(vr*K_r+vt*K_theta_over_r))*rad)
 pieces=[quad(integrand,lo,hi,epsabs=2e-11,epsrel=2e-11,limit=200) for lo,hi in [(1.,2.),(2.,R),(R,2*R)]]
 direct=sum(p[0] for p in pieces);predict=np.pi*c*b0*(12*np.log(R)-C)
 rows.append({'R':R,'A_R':float(12*np.log(R)-C),'N_direct_angular_radial':direct,'N_formula':float(predict),'difference':float(direct-predict),'N_over_pi_c':float(direct/(np.pi*c)),'quad_error_estimate':sum(p[1] for p in pieces)})
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
out={'checked_utc':datetime.now(timezone.utc).isoformat(),'exact_IBP_difference':str(err),'sympy_version':S.__version__,'C_chi':C,'C_quadrature_error_estimate':12*errI+1.5*errJ,'beta':beta,'c':c,'b0':b0,'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Base vorticity moment only. The nonprofile construction is proved by continuity in PROOF.md; these numbers do not instantiate the temperature field or certify an IVT parameter.'}
(root/'base_moment_checks.json').write_text(json.dumps(out,indent=2)+'\n');(root/'transport_strain_counterexample_check.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(out,indent=2))
