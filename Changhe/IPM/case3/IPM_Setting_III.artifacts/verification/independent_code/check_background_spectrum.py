"""Small manufactured nonconstant-background gate before full spectral runs."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Fr
import json,numpy as np,mpmath as mp
from independent_background_spectrum import FrozenBackgroundCompression
from independent_dynamic_spectrum import utc,sha
from q_mp_primitives import MPQPrimitives,mf
root=Path('research/independent_dynamic_spectrum/verification/background_gate');root.mkdir(parents=True,exist_ok=True)
N=8;M=3;co=[np.r_[2.,.1,-.03,np.zeros(N-2)],np.r_[.03,-.02,np.zeros(N-2)],np.r_[-.01,np.zeros(N-2)]]
p=root/'manufacture.npz';np.savez(p,N=N,M=M,u=np.concatenate(co),basis='cheb',L=1.,p=1/(1-1/3),cl=3.)
m=FrozenBackgroundCompression(N,M,p);B,DrB,DaB,br,bt=m.background_fields(20)
assert max(x['mode_abs_error']for x in m.base_conversion)<1e-13
with mp.workdps(70):
 pp=MPQPrimitives([list(map(Fr,c))for c in co],Fr(1),Fr(m.kappa),Fr(3))
 err=0.
 for ir in [0,3,7]:
  for ia in [0,3,8]:
   r=mf(float(m.r[ir+1]));theta=mf(float(m.theta[ia]));v=pp.at(r*mp.cos(theta),r*mp.sin(theta));ux,uy=v['U']
   ref=[float((ux*mp.cos(theta)+uy*mp.sin(theta))/r),float((-ux*mp.sin(theta)+uy*mp.cos(theta))/r)]
   err=max(err,abs(ref[0]-br[ir,ia]),abs(ref[1]-bt[ir,ia]))
 assert err<1e-10;strainerr=abs(m.base_c-float(pp.c));assert strainerr<1e-12
rows=[]
for k in range(M):
 coef=np.array([(-1.)**j/(j+9)for j in range(N+1-k)])[:,None];H,Ht=m.mode_fields(k,m.t[1:],coef);h=H[:,0,None]*m.angular[k];ht=Ht[:,0,None]*m.angular[k];ha=H[:,0,None]*m.angular_d[k]
 Q=m.w[1:]+2*m.kappa*m.s[1:];Z=(1-2*m.s[1:]/Q)[:,None];T=(4*m.s[1:]*m.w[1:]/Q)[:,None];dh=Z*h+T*ht;da=1/np.tan(m.theta)*h+ha
 ur,ut=m.polar_inverse(k,coef,m.lr,m.theta,20);ur=ur[:,:,0];ut=ut[:,:,0];ch=float(m.strain(k,coef)[0])
 ref=m.cw*h-(m.cx+br)*dh-bt*da-ur*DrB-ut*DaB-ch/(m.C-1)*(B-m.C*DrB)
 def rhs(t):
  cw=-(m.base_c+t*ch)/(m.C-1);cx=m.C*cw
  return cw*(B+t*h)-(cx+br+t*ur)*(DrB+t*dh)-(bt+t*ut)*(DaB+t*da)
 errors=[]
 for step in [1e-2,1e-3,1e-4]:errors.append(float(np.max(abs((rhs(step)-rhs(-step))/(2*step)-ref))))
 assert errors[0]<1e-10;rows.append(dict(k=k,steps=[1e-2,1e-3,1e-4],errors=errors))
out=dict(utc=utc(),status='PASS',base_inverse_mp70_max_abs_error=err,strain_error=strainerr,embedding=m.base_conversion,directional=rows,code_sha256=sha('independent_code/independent_background_spectrum.py'))
(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
