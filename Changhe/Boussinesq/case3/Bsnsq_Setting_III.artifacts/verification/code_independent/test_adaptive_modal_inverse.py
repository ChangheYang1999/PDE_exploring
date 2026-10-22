from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time
import numpy as np
import scipy
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings

root=Path('verification/adaptive_modal_inverse');root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();nu=1/3
n=np.arange(1,5);powers=n.copy();powers[0]=3
b=(powers-2+nu)/2;amps=np.array([-.5,.3,.1,-.08])
def pdata(r):
 s=r*r
 pp=amps*r**powers*(1+s)**(-b)
 dp=pp*(powers/r-2*b*r/(1+s))
 return pp,dp
def manufactured_source(r):
 p,dp=pdata(r);s=r*r
 return -p*((powers*powers-n*n)/(r*r)-4*b*(powers+1)/(1+s)+4*b*(b+1)*s/(1+s)**2)
def expected(points):
 ans=[]
 for x,y in points:
  r=np.hypot(x,y)
  if r==0:ans.append([0.,0.]);continue
  phi=np.arctan2(x,-y);p,dp=pdata(r)
  vr=-np.dot(n*p/r,np.cos(n*phi));vt=np.dot(dp,np.sin(n*phi))
  ans.append([vr*x/r-vt*y/r,vr*y/r+vt*x/r])
 return np.array(ans)
rads=np.array([1e-5,.001,.031,.37,1.,3.1,17.,101.,1e4,1e6])
ang=np.array([.0,.23,.89,1.41,2.21,3.02])
pts=np.array([[r*np.sin(a),-r*np.cos(a)] for r in rads for a in ang])
out={'started_utc':datetime.now(timezone.utc).isoformat(),'numpy':np.__version__,'scipy':scipy.__version__,
 'official_documentation':'https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad_vec.html',
 'manufactured':[],'source_product':[],'cross_inverse':[],'status':'RUNNING'}
def save():
 out['elapsed_seconds']=time.monotonic()-start
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for tol in [1e-8,2e-11]:
 inv=AdaptiveModalInverse(manufactured_source,4,ModalSettings(nu,tol,tol))
 got=inv.relative(pts);want=expected(pts);err=got-want
 out['manufactured'].append({'tolerance':tol,'points':pts.tolist(),'expected':want.tolist(),'computed':got.tolist(),
  'max_abs_error':float(abs(err).max()),'max_error_over_1_plus_r':float((abs(err)/(1+np.linalg.norm(pts,axis=1)[:,None])).max()),
  'quadrature':inv.evidence});save()
 print('manufacture',tol,out['manufactured'][-1]['max_abs_error'],out['manufactured'][-1]['max_error_over_1_plus_r'],flush=True)
s=R2State('verification/manufactured_20261020T1915/snapshots/man_pic1.npz');src=R2ModeSource(s)
for r in [.00013,.03,.71,3.1,10.,1000.,1e6]:
 a=np.linspace(0,2*np.pi,51,endpoint=False)+.013
 actual=s.omega(r*np.sin(a),-r*np.cos(a))
 from_modes=src(r)@np.sin(np.arange(1,src.count+1)[:,None]*a[None,:])
 out['source_product'].append({'r':r,'max_abs_error':float(abs(actual-from_modes).max()),'scale':float(abs(actual).max())})
print('mode extraction max',max(v['max_abs_error'] for v in out['source_product']),flush=True)
p=np.array([[.13,.27],[.63,-.42],[1.13,.73],[0.,.81],[.47,0.],[2.03,-1.17],[4.7,8.2]])
cart=CartesianInverse(s.omega,InverseSettings(radius=24.,core_radial_order=64,core_angular_order=64,exterior_radial_order=64,exterior_angular_order=64,decay_power=nu))
vc=cart.relative(p)
for tol in [1e-8,2e-11]:
 inv=AdaptiveModalInverse(src,src.count,ModalSettings(nu,tol,tol));vm=inv.relative(p)
 out['cross_inverse'].append({'tolerance':tol,'points':p.tolist(),'cartesian':vc.tolist(),'adaptive':vm.tolist(),
  'max_abs_difference':float(abs(vc-vm).max()),'quadrature':inv.evidence});save()
 print('cross inverse',tol,out['cross_inverse'][-1]['max_abs_difference'],flush=True)
out['code_hashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path('code_independent/adaptive_modal_inverse.py'),Path(__file__)]}
out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save()
assert max(v['max_error_over_1_plus_r'] for v in out['manufactured'])<1e-7
assert max(v['max_abs_error'] for v in out['source_product'])<1e-11
assert out['cross_inverse'][-1]['max_abs_difference']<1e-7
print('PASS',out['elapsed_seconds'],flush=True)
