from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,math
import numpy as np
from q_weighted_tail_bounds import constants,tails,endpoint_division,serialize
from angular_log_inverse import QAngular,AngularLogInverse


def evaluate(cc,t):
 t0=F(1);t1=t;d0=F(0);d1=F(1)
 val=cc[0];der=F(0)
 if len(cc)>1:val+=cc[1]*t1;der+=cc[1]
 for c in cc[2:]:
  t2=2*t*t1-t0;d2=2*t1+2*t*d1-d0
  val+=c*t2;der+=c*d2;t0,t1=t1,t2;d0,d1=d1,d2
 return val,der

checks=0
for case in range(1,13):
 M=1+case%5;N=M+3
 coeff=[[F(((case+3)*(j+1)*(k+2))%17-8,32) for k in range(N-j)] for j in range(M)]
 kap=F(case+3,2);ell=F(case+7,4);c=constants(coeff,kap,ell);a,qq=endpoint_division(coeff[0])
 for u in [F(1,1000),F(1,100),F(1,10),F(1,3),F(1,2),F(3,4),F(99,100)]:
  t=2*u-1;pol=[evaluate(row,t) for row in coeff]+[(F(0),F(0)),(F(0),F(0))]
  q,_=evaluate(qq,t) if qq else (F(0),F(0))
  assert pol[0][0]-a==(t+1)*q
  for j in range(M):
   bj,dj=pol[j];bn,dn=pol[j+1];w=1-u
   if j==0:
    h=w*(bj-u*bn/2)-a
    ds=-bj+2*w*dj-((1-2*u)*bn+2*u*w*dn)/2
    power=u
   else:
    h=w*u**j*(bj-u*bn)/2
    ds=((j*w-u)*u**(j-1)*(bj-u*bn)+w*u**j*(2*dj-bn-2*u*dn))/2
    power=u**j
   dot=ds*2*u*w/(w+2*kap*u)
   assert abs(h)<=c['H'][j]*power
   assert abs(h)<=c['G'][j]
   assert abs(dot)<=c['D'][j]*power
   checks+=3
  for m in [F(5,2),F(3),F(7,2)]:
   tt=tails(c,m,-30,80);assert all(v>=0 for v in tt.values())
   checks+=1

samples=[]
paths=['evidence/q_evaluations/qfree_N64_first/snapshot.npz',
       'evidence/q_snapshots_20261020T2016/qfreeF_cl1.5_N64.pt',
       'evidence/q_snapshots_20261020T2016/qfree2_cl1.5_N96_Lf0.125_clmin1.005.pt']
for path in paths:
 model=QAngular(path);cc=constants(model.coeff,model.kappa,model.cl)
 z=np.array([-14.,-10.,-6.,-2.,0.,2.,6.,16.,60.]);theta=np.linspace(0,np.pi/2,43)
 f=AngularLogInverse(model,128).fields(z+model.log_core,theta)
 for i,zz in enumerate(z):
  factor=math.exp(2*zz) if zz<=0 else 1.
  pairs=[('H','Hsum' if zz<=0 else 'Gsum'),('dotH','Dsum'),('Htheta','Htheta' if zz<=0 else 'Gtheta'),
         ('vr','near_Vr' if zz<=0 else 'global_Vr'),('vt','near_Vtheta' if zz<=0 else 'global_Vtheta'),
         ('Fr','Fnear' if zz<=0 else 'Fglobal')]
  ratios={k:float(np.max(abs(f[k][i])))/(float(cc[key])*factor) for k,key in pairs}
  assert max(ratios.values())<=1+1e-8,(path,zz,ratios)
  samples.append(dict(path=path,z=zz,ratios=ratios))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',exact_polynomial_inequalities=checks,
            supporting_numerical_rows=samples,scope='Exact rational coefficient/derivative inequalities; floating point samples supporting separate analytic velocity and tail bounds. No annular integration certificate.')
Path('research/finite_q_weighted_tails/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
