from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import numpy as np
import mpmath as mp
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from finite_difference import derivative,safe_ratio
root=Path('verification/farfield_grid_20261020T1930');start=time.monotonic()
s=R2State(root/'snapshots/manufactured_picard.npz');s0=R2State(root/'snapshots/S0.npz')
data=json.loads((root/'results.json').read_text())
row=next(v for v in data['states'] if v['label']=='manufactured_picard')
rr=next(v for v in row['runs'] if v['kind']=='transport' and v['relative_step']==1e-5)
pts=[rr['summary'][v]['max_ratio_point'] for v in ['F','G']]
with np.load(root/'manufactured_picard_transport.npz',allow_pickle=False) as z:
 p=z['points'];th=p[:,0]**2*z['F'];sel=np.flatnonzero((np.linalg.norm(p,axis=1)<300)&(p[:,0]>0))
 i=sel[np.argmin(th[sel])];pts.append(p[i].tolist())
p=np.array(pts)
def source(x,y):return s.omega(x,y)+np.asarray(x)*s0.divided(x,y,'external')-s0.omega(x,y)
src=R2ModeSource(s);src0=R2ModeSource(s0);ext0=R2ModeSource(s0,True)
mod=AdaptiveModalInverse(lambda r:src(r)+ext0(r)-src0(r),src.count,ModalSettings(1/3,2e-11,2e-11))
vm=mod.relative(p)
print('points',p.tolist(),flush=True)
F=lambda x,y:s.divided(x,y,'F');G=lambda x,y:s.divided(x,y,'G')
def res(V,h):
 W=s.beta*p+V;x=p[:,0];A=W[:,0]/x
 fv=F(*p.T);gv=G(*p.T);fx=derivative(F,p,0,h);fy=derivative(F,p,1,h);gx=derivative(G,p,0,h);gy=derivative(G,p,1,h)
 tF=np.column_stack([A*(2*fv+x*fx),W[:,1]*fy,-(s.beta-2)*fv])
 tG=np.column_stack([A*(gv+x*gx),W[:,1]*gy,gv,-(2*fv+x*fx)])
 return {name:{'R':t.sum(1).tolist(),'N':abs(t).sum(1).tolist(),'ratio':safe_ratio(t.sum(1),abs(t).sum(1)).tolist()} for name,t in [('F',tF),('G',tG)]}
out={'started_utc':datetime.now(timezone.utc).isoformat(),'points':p.tolist(),'modal_velocity':vm.tolist(),'runs':[],'status':'RUNNING'}
def save():
 out['elapsed_seconds']=time.monotonic()-start
 (root/'cartesian_spotcheck.json').write_text(json.dumps(out,indent=2)+'\n')
for core,order in [(384.,64),(384.,128),(768.,128)]:
 inv=CartesianInverse(source,InverseSettings(radius=core,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/3))
 vc=inv.relative(p)
 row={'core':core,'order':order,'V':vc.tolist(),'max_difference_from_modal':float(abs(vc-vm).max()),'steps':[]}
 for h in [2e-3,1e-3]:row['steps'].append({'h':h,'residuals':res(vc,h)})
 out['runs'].append(row);save();print(core,order,row['max_difference_from_modal'],flush=True)
mp.mp.dps=90
T=[mp.mpf(float(v)) for v in s.knots]
def mp_F(x,y):
 x=mp.mpf(float(x));y=mp.mpf(float(y));L=mp.mpf(s.L);bb=mp.mpf(s.bb);r=mp.sqrt(x*x+y*y)
 logz=-mp.log1p((r/L)**2)/(2*bb);t=-mp.expm1(logz);eta=-y/r
 span=next(i for i in range(len(T)-1) if T[i]<=t<T[i+1]);deg=s.degree
 coeff=s.rawF.reshape(s.K,s.nb).copy()
 for k in range(s.K):coeff[k,:k//2]=0
 vals=[]
 for k in range(s.K):
  d=[mp.mpf(float(coeff[k,span-deg+j])) for j in range(deg+1)]
  for lev in range(1,deg+1):
   for j in range(deg,lev-1,-1):
    alpha=(t-T[span-deg+j])/(T[span+1+j-lev]-T[span-deg+j])
    d[j]=(1-alpha)*d[j-1]+alpha*d[j]
  vals.append(d[deg]*(r/mp.sqrt(r*r+L*L) if k%2 else 1))
 c=[mp.mpf(1),eta]
 for k in range(2,s.K):c.append(2*eta*c[-1]-c[-2])
 value=mp.exp((bb+2)*logz)*sum(v*ch for v,ch in zip(vals,c))
 return value,x*x*value
out['high_precision_values']=[]
for x,y in p:
 f,theta=mp_F(x,y)
 out['high_precision_values'].append({'point':[float(x),float(y)],'F_90digits':mp.nstr(f,80),'Theta_90digits':mp.nstr(theta,80),
 'F_float':float(F(x,y)),'absolute_difference':float(abs(f-mp.mpf(float(F(x,y)))))})
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',out['elapsed_seconds'],flush=True)
