"""Independent vectorized Cartesian differences, no inverse or solver code."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,time
import numpy as np
from numpy.polynomial.chebyshev import chebder,chebval2d
from scipy.fft import dct
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
from collocation import NodalDensity
from density import gradient_fd
OUT=ROOT/'verification'
raw=(OUT/'actions.json').read_bytes(); base=json.loads(raw);assert base.get('complete')
pts=np.array(base['points']); steps=[1/4000,1/8000,1/16000,1/32000]
obj={'date_start':datetime.now(timezone.utc).isoformat(),'base_actions_sha256':hashlib.sha256(raw).hexdigest(),
     'points':base['points'],'steps':steps,'states':[],'scope':'Signed Cartesian eighth-order gradient refinements; not interval-certified.'}
start=time.monotonic()
for tag,name in [('n96m40S','dnB_n96m40S.npz'),('n120m48_S','dnSB_n120m48.npz')]:
 d=NodalDensity(ROOT/'data'/name); V=np.load(ROOT/'data'/('directions_'+tag+'.npz'))['V'];K=V.shape[1]
 values=np.zeros((d.N+1,d.M,K));values[1:]=V[:-2].reshape(d.N,d.M,K)
 co=dct(values[::-1],type=1,axis=0)/d.N;co[[0,-1]]*=.5
 co=dct(co,type=2,axis=1)/d.M;co[:,0]*=.5
 bqc=2*chebder(d.co,axis=0)
 def fields(x,y):
  x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float)); rr=x*x+y*y
  ell=np.log1p(rr/d.L**2);q=-np.expm1(-.5*(1-d.k)*ell)
  z=2*q-1;c=np.cos(2*d.map_inverse(np.arctan2(abs(y),abs(x))))
  delta=chebval2d(z,c,co);b=chebval2d(z,c,d.co);bq=chebval2d(z,c,bqc)
  sh=(K,)+(1,)*x.ndim
  delta=delta+(-V[-2]/d.cl**2).reshape(sh)*(.5*ell*(b-(1-q)*bq))
  pref=x*x*y*np.exp(.5*(d.k-3)*ell)
  return np.concatenate(((pref*b)[None],pref*delta),axis=0)
 val=fields(pts[:,0],pts[:,1]).T
 original=next(s for s in base['states'] if s['tag']==tag)
 scalar=np.array([[r['rho'],*r['delta_rho']] for r in original['rows']])
 error=float(np.max(abs(val-scalar)/(1+abs(scalar))))
 assert error<5e-13
 row={'tag':tag,'state_md5':d.md5,'scalar_value_relative_check':error,'gradient_steps':[]}
 for rel in steps:
  h=rel*np.maximum(1,np.max(abs(pts),axis=1));gg=[]
  for axis in (0,1):
   total=np.zeros((K+1,len(pts)))
   for j,w in enumerate([4/5,-1/5,4/105,-1/280],1):
    shift=np.zeros_like(pts);shift[:,axis]=j*h
    total+=w*(fields(*(pts+shift).T)-fields(*(pts-shift).T))
   gg.append(total/h)
  grads=np.stack(gg,axis=-1).transpose(1,0,2)
  # Scalar independent call of the same mathematical stencil on base at the
  # difficult point protects the vectorized axis/point/channel ordering.
  scalar_g=gradient_fd(d,*pts[5],relative_step=rel)
  assert np.max(abs(grads[5,0]-scalar_g))<1e-12
  row['gradient_steps'].append({'relative_step':rel,'base_gradient':grads[:,0].tolist(),
                               'delta_gradient':grads[:,1:].tolist(),'date':datetime.now(timezone.utc).isoformat()})
  print(tag,rel,'seconds',time.monotonic()-start,flush=True)
 obj['states'].append(row)
 (OUT/'gradients_refined.json.tmp').write_text(json.dumps(obj,indent=2)+'\n')
 (OUT/'gradients_refined.json.tmp').replace(OUT/'gradients_refined.json')
obj['date_end']=datetime.now(timezone.utc).isoformat();obj['complete']=True
(OUT/'gradients_refined.json').write_text(json.dumps(obj,indent=2)+'\n')
print('COMPLETE',obj['date_end'],flush=True)
