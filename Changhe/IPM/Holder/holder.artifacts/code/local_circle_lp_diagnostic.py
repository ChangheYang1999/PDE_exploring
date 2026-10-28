"""Floating paired-local-circle transport. Diagnostic only."""
from pathlib import Path
from datetime import datetime,timezone
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from scipy.spatial.distance import cdist
from numpy.polynomial.legendre import leggauss
import numpy as np,json,time,argparse

def ring(alpha,r,phase,n=48,power=None):
 th=phase/2+np.pi/4+(np.arange(n)+.5)*2*np.pi/n
 z=.5+r*np.exp(1j*th)
 w=(np.cos(2*th-phase)-r*r*(np.exp(1j*phase)/(1+r*np.exp(1j*th))**2).real)/n
 z=np.concatenate([z,-z]);mass=np.concatenate([w,-w])
 if power is not None:
  lam=power/2*(2*r)**power
  z=np.concatenate([z,[.5,-.5]]);mass=np.concatenate([mass,[-lam,lam]])
 pos=mass>1e-15;neg=mass<-1e-15;P=z[pos];Q=z[neg];a=mass[pos];b=-mass[neg]
 ni=len(P);nj=len(Q);I,J=np.indices((ni,nj));cols=np.arange(ni*nj)
 mat=coo_matrix((np.ones(2*ni*nj),(np.concatenate([I.ravel(),ni+J.ravel()]),np.concatenate([cols,cols]))),shape=(ni+nj,ni*nj)).tocsr()
 cost=abs(P[:,None]-Q[None,:])**alpha
 sol=linprog(cost.ravel(),A_eq=mat,b_eq=np.concatenate([a,b]),bounds=(0,None),method='highs',options={'time_limit':20})
 assert sol.success,sol.message
 return sol.fun

def evaluate(alpha,phase,n=48,nr=40,power=None):
 g,w=leggauss(nr);lo=np.log(1e-7);hi=np.log(.5);u=(lo+hi)/2+(hi-lo)/2*g
 values=[ring(alpha,float(np.exp(t)),phase,n,power) for t in u]
 return float(np.dot(values,w)*(hi-lo)/2)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=48);p.add_argument('--nr',type=int,default=40);p.add_argument('--out',default='data/local_circle_lp_diagnostic.json');args=p.parse_args();start=time.monotonic();rows=[]
 for phase in [0,np.pi/4,np.pi/2,3*np.pi/4,np.pi]:
  for power in [None,1.,2.,4.]:
   value=evaluate(.5,phase,args.n,args.nr,power);row=dict(alpha=.5,phase=float(phase),power=power,local_transport=value,n=args.n,nr=args.nr);rows.append(row);print(row,time.monotonic()-start,flush=True)
 Path(args.out).write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,status='Floating transport diagnostics, not certified upper bounds',elapsed_seconds=time.monotonic()-start),indent=2)+'\n')
