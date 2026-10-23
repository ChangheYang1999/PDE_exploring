"""Independent smooth manufacture: collapsed hydrostatic residual without density layer."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
import mpmath as mp
import numpy as np
from independent_hydrostatic import VerticalInverse
r=Path('research/hydrostatic_layer_diagnostic_caution');v=r/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
out={'status':'RUNNING','start_utc':utc(),'proof_sha256':sha(r/'PROOF.md'),'code_sha256':sha(__file__),'checks':[],'manufactures':[]}
def save():(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,ok,evidence=None):
 out['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
 if not ok:out['status']='FAILED';save();raise AssertionError(name)
def zero(name,e):check(name,S.factor(e)==0)
p,x,y=S.symbols('p x y',positive=True);a=(1+p)/2;n=a*p;d=2*p-1;q=n+p-1
zero('first error gap',n-d-(1-p)*(2-p)/2)
zero('angular inner exponent',2*a-2-p+1)
zero('density residual difference order',2*a+d-2-3*p+2)
zero('far homogeneous product error',2*a+2*p-3-3*p+2)
zero('manufacture defect below inner order',q-(p-2)-n-1)
g=y*(1+x*x+y*y)**((p-1)/2);V1=x*(1+x*x+y*y)**((p-1)/2)
zero('manufactured horizontal differential',S.diff(V1,y)-S.diff(g,x))
zero('manufactured inverse vertical second derivative',-S.diff(V1,x,y)+S.diff(g,x,2))
mp.mp.dps=160
for pp in [mp.mpf(1)/3,mp.mpf('.5'),mp.mpf('.75')]:
 aa=(1+pp)/2;nn=aa*pp;qq=nn+pp-1;bb=(pp-1)/2
 B0=mp.sqrt(mp.pi)*mp.gamma(-pp/2)/(2*mp.gamma((1-pp)/2));B1=mp.sqrt(mp.pi)*mp.gamma(1-pp/2)/(2*mp.gamma((3-pp)/2));Cp=-(1+pp)*B0
 check('canonical Cp beta identity '+str(pp),abs(Cp+B0+(pp-1)*B1)<mp.mpf('1e-90'))
 def integr(beta,B,Y):
  const=mp.sqrt(mp.pi)*mp.gamma(-beta-mp.mpf('.5'))/(2*mp.gamma(-beta))*B**(beta+mp.mpf('.5'))
  return const+Y**(2*beta+1)/(2*beta+1)*mp.hyp2f1(-beta-mp.mpf('.5'),-beta,mp.mpf('.5')-beta,-B/Y**2)
 def vel(X,Y):
  B=1+X*X
  return X*(B+Y*Y)**bb,-integr(bb,B,Y)-2*bb*X*X*integr(bb-1,B,Y)
 def values(X,Y):
  SS=1+X*X+Y*Y;gg=Y*SS**bb;gx=2*bb*X*Y*SS**(bb-1);gy=SS**bb+2*bb*Y*Y*SS**(bb-1)
  u1,u2=vel(X,Y);hx=(X/pp+u1)*gx;hy=(Y/pp+u2)*gy;rr=hx+hy-gg;nf=abs(hx)+abs(hy)+abs(gg)
  return rr/nf,rr,nf,gg
 for XX,YY in [(mp.mpf('.3'),mp.mpf('.2')),(mp.mpf(1),mp.mpf(2)),(mp.mpf(3),mp.mpf(20))]:
  v1,v2=vel(XX,YY);direct=-mp.quad(lambda t:(1+XX*XX+t*t)**bb+2*bb*XX*XX*(1+XX*XX+t*t)**(bb-1),[0,YY]);check('physical primitive manufacture '+str((pp,XX,YY)),abs(v2-direct)<mp.mpf('1e-85'),mp.nstr(abs(v2-direct),12))
  for be in [bb,bb-1]:check('antiderivative derivative '+str((pp,XX,YY,be)),abs(mp.diff(lambda yy:integr(be,1+XX*XX,yy),YY)-(1+XX*XX+YY*YY)**be)<mp.mpf('1e-85'))
 # Entire independent physical quadrature includes finite core panels and infinite Jacobi tail.
 pf=float(pp);bf=(pf-1)/2
 def jet(X,Y):
  X,Y=np.broadcast_arrays(np.asarray(X,float),np.asarray(Y,float));ss=1+X*X+Y*Y
  return np.stack([Y*ss**bf,2*bf*X*Y*ss**(bf-1),ss**bf+2*bf*Y*Y*ss**(bf-1),2*bf*Y*ss**(bf-1)+4*bf*(bf-1)*X*X*Y*ss**(bf-2)],axis=-1)
 inv=VerticalInverse(jet,pf,28,128,128.,.25)
 for X,Y in [(.3,.2),(1.,2.),(3.,20.),(0.,1e3)]:
  got=inv.at(X,Y)['V'];want=list(map(float,vel(mp.mpf(X),mp.mpf(Y))));err=max(abs(got[j]-want[j])for j in range(2));check('independent whole vertical inverse '+str((pp,X,Y)),err<2e-8,err)
 curves=[]
 for zz in [mp.mpf('.2'),mp.mpf(1),mp.mpf(2)]:
  target=pp*Cp*abs(zz)**pp/2;rows=[]
  for exponent in [2,4,8,16,32,48]:
   YY=mp.mpf(10)**exponent;XX=YY**aa*zz;vv,RR,NF,GG=values(XX,YY);axis=values(mp.mpf(0),YY)[0];scaled=YY**(1-nn)*(vv-axis);error=abs(scaled-target);fp=YY*(XX*XX+YY*YY)**bb;density=(GG-fp)/YY**qq
   rows.append({'log10_y':exponent,'z':str(zz),'R':mp.nstr(RR,45),'Nf':mp.nstr(NF,45),'signed_R_Nf':mp.nstr(vv,45),'axis_signed_R_Nf':mp.nstr(axis,45),'collapsed':mp.nstr(scaled,50),'target':mp.nstr(target,50),'error':mp.nstr(error,40),'inner_scaled_density_defect':mp.nstr(density,40)})
  check('collapse converges across last two extents '+str((pp,zz)),mp.mpf(rows[-1]['error'])<mp.mpf(rows[-2]['error'])/20)
  check('nonzero collapsed curve resolved '+str((pp,zz)),mp.mpf(rows[-1]['error'])<mp.mpf('2e-6'),rows[-1]['error'])
  check('density layer coefficient tends zero '+str((pp,zz)),abs(mp.mpf(rows[-1]['inner_scaled_density_defect']))<mp.mpf('1e-35'))
  curves.append(rows)
 out['manufactures'].append({'p':mp.nstr(pp,70),'Cp':mp.nstr(Cp,70),'curves':curves});save()
out.update(status='DONE',finished_utc=utc(),count=len(out['checks']));save();print(json.dumps({'status':'DONE','count':out['count']}))
