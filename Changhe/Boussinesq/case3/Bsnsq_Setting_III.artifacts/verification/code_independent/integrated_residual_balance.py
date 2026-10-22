"""Full-plane moment audit using own inverse and Cartesian finite differences.

No numerics-lane program is imported or executed. Radial integration uses
Gauss-Legendre nodes in sqrt of the source compactification, separately at
all represented radial cells. All angular points are independent uniform
full circles. Spatial derivatives use the verifier's seven-point stencil.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,hashlib,shutil
import numpy as np
from numpy.polynomial.legendre import leggauss
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from finite_difference import stencil

root=Path(sys.argv[1]); manifest=json.loads((root/'manifest.json').read_text())
t0=time.monotonic();out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'states':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-t0
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
zfd,wfd=stencil()
def fd(fun,p,axis,h):
 q=p[:,None,:]+np.zeros((1,len(zfd),2));q[:,:,axis]+=h[:,None]*zfd
 return np.asarray(fun(q[:,:,0],q[:,:,1]))@wfd/h

def circle(inv,r,ang):
 pr,dp=inv.radial(r);n=inv.n
 vr=-(n*pr)@np.cos(n[:,None]*ang);vt=dp@np.sin(n[:,None]*ang)
 sn=np.sin(ang);cs=np.cos(ang)
 return np.column_stack((vr*sn+vt*cs,-vr*cs+vt*sn))

for item in manifest['states']:
 s=R2State(root/item['snapshot']);src=R2ModeSource(s);ext=R2ModeSource(s,True)
 inv=AdaptiveModalInverse(src,s.K,ModalSettings(1/s.bb,2e-11,2e-11))
 einv=AdaptiveModalInverse(ext,s.K,ModalSettings(1/s.bb,2e-11,2e-11))
 eps=float(s.meta.get('eps',1.));c=s.strain()
 row={'label':item['label'],'sha256':s.sha256,'metadata':s.meta,'center':s.center(),'runs':[]};out['states'].append(row)
 for order in manifest.get('orders',[6,10]):
  nodes,weights=leggauss(order);u_edges=np.sqrt(s.edges)
  u=np.concatenate([(a+b)/2+(b-a)/2*nodes for a,b in zip(u_edges[:-1],u_edges[1:])])
  wu=np.concatenate([(b-a)/2*weights for a,b in zip(u_edges[:-1],u_edges[1:])])
  logz=np.log1p(-u*u);r=s.L*np.sqrt(np.expm1(-2*s.bb*logz))
  wr=wu*(2*s.bb*s.L*s.L*u*np.exp(-(2*s.bb+1)*logz))
  count=int(manifest.get('angular_count',96));ang=2*np.pi*(np.arange(count)+.231)/count
  sn=np.sin(ang);cs=np.cos(ang);points=np.stack((r[:,None]*sn,-r[:,None]*cs),axis=-1).reshape(-1,2)
  area=np.repeat(wr,count)*(2*np.pi/count);rp=np.repeat(r,count);x,y=points.T
  vs=np.array([circle(inv,rr,ang) for rr in r]).reshape(-1,2)
  ve=np.array([circle(einv,rr,ang) for rr in r]).reshape(-1,2)
  theta=s.theta(x,y);omega=s.omega(x,y)
  # Exact Cartesian kernel derivatives, independently derived symbolically.
  r2=x*x+y*y;K=x*y/r2**2;gx=y*(y*y-3*x*x)/r2**3;gy=x*(x*x-3*y*y)/r2**3
  gxx=12*x*y*(x*x-y*y)/r2**4
  gxy=-3*(x**4-6*x*x*y*y+y**4)/r2**4
  gradK=np.column_stack((gx,gy));gradg=np.column_stack((gxx,gxy))
  joint={}
  for step in manifest.get('steps',[2e-5,1e-5]):
   h=step*np.maximum(1.,rp)
   tg=np.column_stack((fd(s.theta,points,0,h),fd(s.theta,points,1,h)))
   og=np.column_stack((fd(s.omega,points,0,h),fd(s.omega,points,1,h)))
   joint[step]=(tg,og)
  for kind,V in [('self',vs),('transport',eps*vs+(1-eps)*ve)]:
   W=s.beta*points+V
   N_integrand=omega*np.sum(V*gradK,axis=1);B_integrand=theta*np.sum(V*gradg,axis=1)
   N=float(area@N_integrand);B=float(area@B_integrand);pc=float(area@(K*omega));J=float(area@(gx*theta))
   D=N-.5*B-np.pi*c
   rr={'order':order,'kind':kind,'angular_count':count,'radial_nodes':len(r),'largest_radius':float(r.max()),'N':N,'B':B,'pi_c_exact_spline':float(np.pi*c),'pi_c_integrated':pc,'pi_c_integration_error':float(pc-np.pi*c),'J':J,'D':D,'residual_evaluations':[]}
   for step,(tg,og) in joint.items():
    RO=np.sum(W*og,axis=1)+omega-tg[:,0];RT=np.sum(W*tg,axis=1)-(s.beta-2)*theta
    IO=float(area@(K*RO));IT=float(area@(gx*RT));DR=.5*IT-IO
    rr['residual_evaluations'].append({'step':step,'I_Omega':IO,'I_Theta':IT,'D_from_residuals':DR,'balance_error':float(D-DR),'identity1_error':float(IO-(np.pi*c-N+J)),'identity2_error':float(IT-(2*J-B)),
       'absolute_moment_Omega':float(area@abs(K*RO)),'absolute_moment_Theta':float(area@abs(gx*RT))})
   rr['regions']=[]
   for lo,hi in [(0,.03),(.03,.3),(.3,3),(3,30),(30,300),(300,np.inf)]:
    ix=(rp>=lo)&(rp<hi);rr['regions'].append({'r_min':lo,'r_max':None if np.isinf(hi) else hi,'N':float(area[ix]@N_integrand[ix]),'B':float(area[ix]@B_integrand[ix]),'pi_c':float(area[ix]@(K[ix]*omega[ix]))})
   row['runs'].append(rr)
   print(item['label'],kind,'order',order,'D',D,'identity errors',[(a['identity1_error'],a['identity2_error']) for a in rr['residual_evaluations']],flush=True)
  save()
 row['inverse_evidence']={'self':inv.evidence,'external':einv.evidence}
 row['inverse_flags_all']=all(a['inner_success'] and a['outer_success'] for a in inv.evidence+einv.evidence)
 row['status']='COMPLETE';save()
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),limitations='Floating point full-plane quadrature, not interval-certified. Signed residual moments cannot certify a pointwise residual or a profile.')
out['code_sha256']={name:hashlib.sha256(Path('code_independent',name).read_bytes()).hexdigest() for name in ['integrated_residual_balance.py','r2_state_values.py','adaptive_modal_inverse.py','finite_difference.py']}
for name in out['code_sha256']:shutil.copyfile(Path('code_independent')/name,root/name)
save();print('COMPLETE',out['elapsed_seconds'],flush=True)
