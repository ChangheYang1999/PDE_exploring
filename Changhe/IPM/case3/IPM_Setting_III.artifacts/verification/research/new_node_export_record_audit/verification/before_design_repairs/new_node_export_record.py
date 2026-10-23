"""Exact finite-operand arithmetic for producer node records. No inverse reuse."""
from fractions import Fraction as Q
import math
import numpy as np
U=Q(1,2**53);GAMMA=8*U/(1-8*U);TINY=np.finfo(float).tiny

def exact(x,y,g,gx,gy,v,w):
 x,y,g,gx,gy,v,w=map(lambda z:Q(float(z)),(x,y,g,gx,gy,v,w))
 e=x*gx+y*gy;a=v*gx+w*gy;r=2*e+a-g
 nf=abs(2*x*gx+v*gx)+abs(2*y*gy+w*gy)+abs(g);nv=abs(g)+abs(e)+abs(a)
 return r,nf,nv,abs(r)/nf if nf else None,abs(r)/nv if nv else None

def normal_intermediates(x,y,g,gx,gy,v,w):
 with np.errstate(over='ignore',under='ignore',invalid='ignore'):
  ax=2*x;ay=2*y;bx=ax+v;by=ay+w;px=bx*gx;py=by*gy;plus=px+py;minus=plus-g;nf0=np.abs(px)+np.abs(py);nf=nf0+np.abs(g)
 return all(np.isfinite(t).all()and np.all((t==0)|(np.abs(t)>=TINY))for t in [ax,ay,bx,by,px,py,plus,minus,nf0,nf])

def check_rows(d):
 keys=['x','y','g','g_xi','g_y','V1','V2','R_h','N_f'];n=len(d['x'])
 if not all(d[k].shape==(n,)and d[k].dtype==np.float64 and np.isfinite(d[k]).all()for k in keys):raise ValueError('nonfinite or wrong field shape/dtype')
 args=[d[k]for k in keys[:7]]
 if not normal_intermediates(*args):raise ValueError('non-normal arithmetic intermediate')
 out=[];errR=[];errN=[]
 for i,operands in enumerate(zip(*args)):
  a=exact(*operands);r,nf=a[:2];er=abs(Q(float(d['R_h'][i]))-r);en=abs(Q(float(d['N_f'][i]))-nf)
  if er>GAMMA*nf or en>GAMMA*nf:raise ValueError(('outside gamma8 bound',i,str(er),str(en),str(nf)))
  row=[float(z)if z is not None else math.nan for z in a]
  if any(not math.isfinite(row[k])or(row[k]==0 and a[k]>0)for k in [1,2]):raise ValueError('nonrepresentable positive denominator')
  out.append(row);errR.append(float(er/nf)if nf else 0);errN.append(float(en/nf)if nf else 0)
 return np.asarray(out),dict(max_R_error_over_exact_Nf=max(errR,default=0),max_Nf_error_over_exact_Nf=max(errN,default=0),gamma8=float(GAMMA))

def regions(x,y,fields):
 radius=np.hypot(x,y);out=[]
 for name,lo,hi in [('core',0,.1),('subannulus',.1,1),('annulus',1,100),('far',100,math.inf)]:
  ids=np.flatnonzero((radius>=lo)&(radius<hi));metrics={}
  for name2,col in [('absR',0),('Rf',3),('Rv',4)]:
   vals=np.abs(fields[ids,col]);ok=np.isfinite(vals);valid=ids[ok]
   if len(valid):
    i=int(valid[np.argmax(vals[ok])]);metrics[name2]=dict(index=i,value=float(abs(fields[i,col])),x=float(x[i]),y=float(y[i]),fields=fields[i].tolist(),defined_count=int(ok.sum()),undefined_count=int((~ok).sum()))
   else:metrics[name2]=dict(index=None,value=None,defined_count=0,undefined_count=len(ids))
  out.append(dict(region=name,count=len(ids),metrics=metrics))
 return out
