"""Exploratory Stieltjes sums for a rigorously admissible monotone axis family."""
import argparse,json,math,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
A=.5

def distance_segment(X,Y,x0,y0,x1,y1,ray=False):
 dx=x1-x0;dy=y1-y0;t=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy)
 t=np.maximum(t,0) if ray else np.clip(t,0,1)
 return np.hypot(X-x0-t*dx,Y-y0-t*dy)

def witness(X,Y,alpha,b,t,lam):
 d=np.minimum(X,distance_segment(X,Y,0,A,A,0))
 d=np.minimum(d,distance_segment(X,Y,A,0,A+b,b))
 d=np.minimum(d,distance_segment(X,Y,A+b,b,A+b+math.sqrt(3),b+1,True))
 B=np.where(X<=A,A-X,np.where(X<=A+b,X-A,(X-A+(math.sqrt(3)-1)*b)/math.sqrt(3)))
 c=2**(alpha-1);g=c*np.where(Y<B,d**alpha,-d**alpha);h=c*X**alpha
 P=(np.maximum(np.abs(X-A)-Y,0)/math.sqrt(2))**alpha
 return np.maximum(-h,np.minimum(h,np.minimum(g+t,-.5+lam*P)))

def evaluate(alpha,b,t,lam,nx,ny,left=-18,right=30):
 # Vertical bins adapt to distance from the pole. This is only a float sum.
 tv=np.exp(np.linspace(-16,20,ny+1));tm=np.sqrt(tv[:-1]*tv[1:])
 total=0.;pieces=[]
 for sign,top in [(1,right),(-1,math.log(A))]:
  ue=np.linspace(left,top,nx+1);um=(ue[:-1]+ue[1:])/2;dd=np.exp(um);dw=np.diff(np.exp(ue));subtotal=0.
  for j in range(0,nx,32):
   d=dd[j:j+32,None];X=A+sign*d;Y=d*tv[None,:]
   f=witness(X,Y,alpha,b,t,lam);mass=f[:,:-1]-f[:,1:]
   assert np.min(mass)>-1e-12,(sign,j,float(np.min(mass)))
   ym=d*tm[None,:]
   V=2*A*X*ym/(math.pi*((X*X-ym*ym-A*A)**2+4*X*X*ym*ym))
   subtotal+=float(np.sum(V*mass*dw[j:j+32,None]))
  pieces.append(subtotal);total+=subtotal
 return dict(alpha=alpha,b=b,t=t,lam=lam,nx=nx,ny=ny,log_distance_interval=[left,right],log_vertical_ratio_interval=[-16,20],value=1+4*total,pieces=pieces,status='Exploratory positive Stieltjes sum; not a certified lower bound')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--alpha',type=float,default=.5);p.add_argument('--b',type=float,default=.75);p.add_argument('--shift',type=float,default=.5);p.add_argument('--lam',type=float,default=1);p.add_argument('--nx',type=int,default=2048);p.add_argument('--ny',type=int,default=1024);a=p.parse_args();r=evaluate(a.alpha,a.b,a.shift,a.lam,a.nx,a.ny);r['time_utc']=datetime.now(timezone.utc).isoformat();print(json.dumps(r,indent=2))
