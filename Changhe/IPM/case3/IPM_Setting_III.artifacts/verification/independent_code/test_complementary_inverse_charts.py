from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,math
import numpy as np
import mpmath as mp
from complementary_inverse_charts import SmoothAngular,ComplementaryQ,FullChart,point_fields
from angular_log_inverse import AngularLogInverse

out=Path('research/complementary_inverse_charts/verification');out.mkdir(parents=True,exist_ok=True)
mp.mp.dps=90
checks=[]
# Independent hypergeometric radial inverse, including far beyond subtraction precision.
for p in [.4,.75]:
 amp=1.75;path=out/f'smooth_radial_p{p}.npz'
 np.savez(path,radial=1,angular=1,exponent=p,length=1.,cl=2.5,coefficients=np.array([amp,0.]))
 model=SmoothAngular(path)
 assert model.exact_c==-F(amp)/4
 rr=np.array([1e-20,1e-8,.1,1.,10.,1e4,1e20,1e80,1e200])
 theta=np.array([.219,.771,1.499]);lr=np.repeat(np.log(rr),len(theta));tt=np.tile(theta,len(rr))
 for order in [64,128]:
  rows=point_fields(model,lr,tt,order)
  errors=[]
  for row in rows:
   r=mp.exp(mp.mpf(row['log_radius']));th=mp.mpf(row['theta']);alpha=mp.mpf(float(model.alpha))
   w=(1+r*r)**(-alpha);b=mp.mpf(amp)*w;db=-2*alpha*r*r/(1+r*r)*b
   al=mp.mpf(amp)/4*mp.hyp2f1(alpha,2,3,-r*r)
   P=-al/2;E=al-b/2
   ur=-2*P*mp.cos(2*th);ut=E*mp.sin(2*th)
   ux=ur*mp.cos(th)-ut*mp.sin(th);uy=ur*mp.sin(th)+ut*mp.cos(th)
   gx=db*mp.sin(th)*mp.cos(th);gy=b+db*mp.sin(th)**2
   refs=[ux,uy,gx,gy,b*mp.sin(th)]
   got=row['U_over_r']+row['gradient']+[row['rho_over_r']]
   error=max(abs(mp.mpf(v)-ref)/max(abs(b),mp.mpf('1e-300')) for v,ref in zip(got,refs))
   errors.append(float(error))
  if order==128:assert max(errors)<2e-10,(p,max(errors))
  checks.append(dict(test='smooth_radial_MP90_hypergeometric',p=p,order=order,points=len(rows),max_scaled_error=max(errors)))

# Exact rational radial inverse for integer-kappa Q states at rational coordinates.
for kap in [2,6]:
 amp=F(7,4);path=out/f'Q_radial_k{kap}.npz'
 np.savez(path,N=1,M=1,L=1.,p=float(kap),cl=1.2,gamma=1-1/kap,u=np.array([float(amp),0.]))
 model=ComplementaryQ(path)
 errors=[]
 for ss in [F(1,10**12),F(1,100),F(1,4),F(3,4),1-F(1,10**12),1-F(1,10**40)]:
  w=1-ss;C=2*kap-1
  inte=sum((v*(1-w**(k-4*kap+1))/F(k-4*kap+1) for k,v in enumerate([1+C,-1-2*C,C])),F(0))
  exact_alpha=amp*w**(4*kap)*inte/(2*ss*ss)
  lr=float(-mp.mpf(kap)*mp.log(2)+mp.log(mp.mpf(ss.numerator)/ss.denominator)/2-mp.mpf(kap)*mp.log(mp.mpf(w.numerator)/w.denominator))
  cf=AngularLogInverse(FullChart(model),128).coefficients(np.array([lr]))
  got=-2*cf['p'][0,0]
  err=abs(mp.mpf(got)-mp.mpf(exact_alpha.numerator)/exact_alpha.denominator)/(mp.mpf(amp.numerator)/amp.denominator*mp.mpf(w.numerator)/w.denominator)
  errors.append(float(err))
 assert max(errors)<2e-10,(kap,errors)
 checks.append(dict(test='Q_radial_exact_rational_inverse',kappa=kap,points=len(errors),max_scaled_error=max(errors)))

# Nonradial random polynomial cases distinguish the upper primitive and derivatives.
for case in [2,4,7,8]:
 source=Path('research/finite_q_exact_jets/verification')/f'manufactured_{case}.npz'
 model=ComplementaryQ(source)
 lr=model.log_core+np.array([-.8,-.2,.3,1.]);theta=np.array([.11,.7,1.2,1.5])
 full=point_fields(model,lr,theta,128,'full');defect=point_fields(model,lr,theta,128,'defect')
 err=max(abs(a-b) for f,d in zip(full,defect) for a,b in zip(f['U_over_r']+f['gradient']+[f['R_over_r']],d['U_over_r']+d['gradient']+[d['R_over_r']]))
 assert err<2e-10,(case,err)
 checks.append(dict(test='nonradial_Q_overlap',case=case,max_error=err))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,scope='Independent hypergeometric and rational radial inverses at both endpoints, plus nonradial chart overlap. This is not a uniform error certificate for candidate data.')
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
