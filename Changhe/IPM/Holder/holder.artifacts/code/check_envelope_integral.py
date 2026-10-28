"""Independent region decomposition for the finite-envelope diagnostic."""
from pathlib import Path
from datetime import datetime,timezone
from numpy.polynomial.legendre import leggauss
from scipy.spatial.distance import cdist
from envelope_witness import Envelope
import numpy as np,json,hashlib

def direct_kernel(q):
 X=q[...,0];Y=q[...,1]
 return ((X-.5)**2-Y*Y)/(2*np.pi*((X-.5)**2+Y*Y)**2)-((X+.5)**2-Y*Y)/(2*np.pi*((X+.5)**2+Y*Y)**2)

def check(n):
 f=Envelope();g,w=leggauss(n);parts=[]
 for center in [-.5,.5]:
  lo=np.log(1e-6);hi=np.log(.5);r=np.exp((lo+hi)/2+(hi-lo)/2*g)[:,None];th=np.pi*(g+1)[None,:]
  X=center+r*np.cos(th);Y=r*np.sin(th);q=np.stack([X,Y],axis=-1)
  fv=f.evaluate(q.reshape(-1,2))[0].reshape(X.shape);fp=f.evaluate([[center,0]])[0][0]
  own=np.cos(2*th)/(2*np.pi*r*r)*(1 if center>0 else -1)
  k=direct_kernel(q);value=(k*fv-own*fp)*r*r
  parts.append(float(np.sum(value*w[:,None]*w[None,:])*(hi-lo)*np.pi/2))
 t=np.pi*(g+1)/4;r=np.sin(t)[:,None];th=np.pi/2+t[:,None]*g[None,:]
 X=r*np.cos(th);Y=r*np.sin(th);q=np.stack([X,Y],axis=-1);fv=f.evaluate(q.reshape(-1,2))[0].reshape(X.shape)
 parts.append(float(np.sum(direct_kernel(q)*fv*r*np.cos(t)[:,None]*t[:,None]*w[:,None]*w[None,:])*np.pi/2))
 lo=0.;hi=np.log(1e6);r=np.exp((lo+hi)/2+(hi-lo)/2*g)[:,None];th=np.pi*(g+1)[None,:];X=r*np.cos(th);Y=r*np.sin(th);q=np.stack([X,Y],axis=-1)
 fv=f.evaluate(q.reshape(-1,2))[0].reshape(X.shape)
 parts.append(float(np.sum(direct_kernel(q)*fv*r*r*w[:,None]*w[None,:])*(hi-lo)*np.pi/2))
 identity=-float(f.evaluate([[.5,0]])[0][0]);return dict(order=n,parts_near_left_near_right_middle_far=parts,identity=identity,total=sum(parts)+identity)

if __name__=='__main__':
 rows=[]
 for n in [96,192]:
  row=check(n);rows.append(row);print(row,flush=True)
 paths=[Path('code/check_envelope_integral.py'),Path('code/envelope_witness.py'),Path('data/envelope_D_half_axis_nodes_symmetric.json')]
 Path('data/envelope_independent_integral.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,status='Floating diagnostics only; independent full-plane region decomposition',source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}),indent=2)+'\n')
