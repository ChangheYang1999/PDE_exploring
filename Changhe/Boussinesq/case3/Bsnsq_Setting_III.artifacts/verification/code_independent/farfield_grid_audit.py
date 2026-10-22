"""Wide independent residual grid with adaptive physical-radius inversion."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,os,sys
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from finite_difference import stencil,safe_ratio

root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('verification/farfield_grid_20261020T1930')
manifest=json.loads((root/'manifest.json').read_text())
start=time.monotonic()
angles=np.r_[np.linspace(0,np.pi,49)[1:-1],-np.linspace(0,np.pi,49)[1:-1],0.,np.pi]
ax=np.arange(len(angles))>=len(angles)-2
z,weights=stencil()
def fd(fun,points,axis,steps):
 q=points[:,None,:]+np.zeros((1,len(z),2));q[:,:,axis]+=steps[:,None]*z[None,:]
 return np.asarray(fun(q[:,:,0],q[:,:,1]))@weights/steps

def circle(inv,r):
 n=inv.n;pr,dp=inv.radial(r)
 vr=-(n*pr)@np.cos(n[:,None]*angles)
 vt=dp@np.sin(n[:,None]*angles)
 sn=np.sin(angles);cs=np.cos(angles);sn[-2:]=0.;cs[-2:]=[1.,-1.]
 V=np.column_stack((vr*sn+vt*cs,-vr*cs+vt*sn))
 V[ax,0]=0.
 deriv_axis=(n*(dp-pr))@np.cos(n[:,None]*angles[ax])/r
 return V,deriv_axis

def summarize(R,N,points,mask):
 q=safe_ratio(R,N);ii=np.flatnonzero(mask)
 im=ii[np.argmax(q[mask])];ia=int(np.argmax(abs(R)))
 ans={'max_ratio':float(q[im]),'max_ratio_point':points[im].tolist(),'max_abs':float(abs(R[ia])),
      'max_abs_point':points[ia].tolist(),'zero_normalizers':int((N==0).sum()),'infinite_ratios':int(np.isinf(q[mask]).sum())}
 rad=np.linalg.norm(points,axis=1)
 ans['regions']=[]
 for lo,hi in [(0,.03),(.03,.3),(.3,3),(3,30),(30,300),(300,float('inf'))]:
  ix=np.flatnonzero(mask&(rad>=lo)&(rad<hi))
  if len(ix):
   i=ix[np.argmax(q[ix])]
   j=ix[np.argmax(abs(R[ix]))]
   ans['regions'].append({'r_min':lo,'r_max':None if hi==float('inf') else hi,'max_ratio':float(q[i]),'point':points[i].tolist(),'max_abs':float(abs(R[j])),'max_abs_point':points[j].tolist()})
 return ans,q
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','states':[],
 'method':'adaptive physical-radius full-plane sine-mode inverse, Cartesian seven-point finite differences, no denominator floor',
 'limitations':'finite grid and floating-point adaptive estimates, not rigorous bounds; no candidate or endpoint inferred'}
def save():
 out['elapsed_seconds']=time.monotonic()-start
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for item in manifest['states']:
 s=R2State(root/item['snapshot']);src=R2ModeSource(s);ext=R2ModeSource(s,True)
 s0=R2State(root/item['forcing_s0']) if 'forcing_s0' in item else None
 eps=float(s.meta.get('eps',1.))
 source_decay=1/s.bb
 transport_count=src.count
 if s.native_source:
  defect=R2ModeSource(s,kind='native_seed');lam=float(s.meta.get('lam',0.))
  transport_count=max(src.count,defect.count)
  def mixed(r):
   a=eps*src(r)+(1-eps)*ext(r);d=defect(r)
   out=np.zeros(transport_count);out[:len(a)]+=a;out[:len(d)]+=lam*d
   return out
  source_decay=min(source_decay,1/float(s.meta['beta_seed']))
  forcing_description=f'eps*stored_Omega+(1-eps)*stored_external_Omega+lam*seed_defect; source in original beta_seed={s.meta["beta_seed"]}, unknown beta_basis={s.bb}; independently integrated whole-plane inverse, not solver interpolation'
 elif s.Ds is not None:
  defect=R2ModeSource(s,kind='defect')
  mixed=lambda r:eps*src(r)+(1-eps)*ext(r)+defect(r)
  defect_key='cG_f_effective' if s.forcing_schema=='effective_stage_coefficients' else 'cG_f'
  forcing_description=f'eps*stored_Omega+(1-eps)*stored_external_Omega+{defect_key} interpreted in stage basis beta_basis={s.bb:.16g}; forcing schema={s.forcing_schema}'
 elif s0 is not None:
  src0=R2ModeSource(s0);ext0=R2ModeSource(s0,True)
  forcing_scale=float(item.get('forcing_scale',1.))
  source_decay=min(source_decay,1/s0.bb)
  mixed=lambda r:src(r)+forcing_scale*(ext0(r)-src0(r))
  forcing_description=f'stored_Omega+{forcing_scale:g}*(snapshot_external_Omega-S0_Omega) (explicit manifest reconstruction); '+item.get('forcing_scope','verified reconstruction')
 elif float(s.meta.get('lam',0.))!=0:
  raise ValueError('Nonzero lambda archive omits forcing; explicit verified S0 manifest required')
 else:
  mixed=lambda r:eps*src(r)+(1-eps)*ext(r)
  forcing_description='eps*stored_Omega+(1-eps)*stored_external_Omega'
 # Include a broad log grid and physical radii at every finite spline midpoint.
 tm=(s.edges[:-1]+s.edges[1:])/2
 rk=s.L*np.sqrt(np.expm1(-2*s.bb*np.log1p(-tm)))
 rads=np.unique(np.r_[np.geomspace(1e-5,1e8,105),rk[rk<=1e8]])
 sn=np.sin(angles);cs=np.cos(angles);sn[-2:]=0.;cs[-2:]=[1.,-1.]
 p=np.stack((rads[:,None]*sn,-rads[:,None]*cs),axis=-1).reshape(-1,2)
 axis=np.tile(ax,len(rads));rpoint=np.repeat(rads,len(angles));x=p[:,0]
 F=lambda x,y:s.divided(x,y,'F');G=lambda x,y:s.divided(x,y,'G')
 f=F(*p.T);g=G(*p.T);theta=s.theta(*p.T);omega=s.omega(*p.T)
 center=s.center()
 if s0 is not None and s.Ds is None and not s.native_source:
  center['c_reconstructed_defect']=forcing_scale*(s0.strain('external')-s0.strain())
  center['c_mixed']+=center['c_reconstructed_defect']
  a=center['F']['value'];b=center['G']['value'];A0=s.beta-center['c_mixed']
  center['strain_error']=center['c_mixed']-1-s.beta/2
  center['R_F_center']=2*A0*a-(s.beta-2)*a;center['R_G_center']=(A0+1)*b-2*a
 row={'label':item['label'],'snapshot':item['snapshot'],'sha256':s.sha256,'metadata':s.meta,
      'center':center,'forcing_description':forcing_description,'points':len(p),'radii':len(rads),'runs':[]};out['states'].append(row)
 for kind,source in [('transport',mixed),('self',src)]:
  inv=AdaptiveModalInverse(source,transport_count if kind=='transport' else src.count,ModalSettings(source_decay if kind=='transport' else 1/s.bb,1e-10,1e-10))
  velocity=[];axisder=[]
  for r in rads:
   v,da=circle(inv,r);velocity.append(v);axisder.append(da)
  V=np.array(velocity).reshape(-1,2);W=s.beta*p+V
  A=np.empty(len(p));A[~axis]=s.beta+V[~axis,0]/x[~axis]
  A[axis]=s.beta+np.asarray(axisder).ravel()
  archive={'points':p,'radii':rads,'angles':angles,'V':V,'W':W,'A':A,'F':f,'G':g}
  for step in [2e-5,1e-5]:
   hs=step*np.maximum(1.,rpoint)
   fx=fd(F,p,0,hs);fy=fd(F,p,1,hs);gx=fd(G,p,0,hs);gy=fd(G,p,1,hs)
   tx=fd(s.theta,p,0,hs);ty=fd(s.theta,p,1,hs)
   ox=fd(s.omega,p,0,hs);oy=fd(s.omega,p,1,hs)
   terms={'F':np.column_stack((A*(2*f+x*fx),W[:,1]*fy,-(s.beta-2)*f)),
          'G':np.column_stack((A*(g+x*gx),W[:,1]*gy,g,-(2*f+x*fx))),
          'Theta':np.column_stack((W[:,0]*tx,W[:,1]*ty,-(s.beta-2)*theta)),
          'Omega':np.column_stack((W[:,0]*ox,W[:,1]*oy,omega,-tx))}
   run={'kind':kind,'relative_step':step,'summary':{}}
   for name,t in terms.items():
    R=t.sum(1);N=abs(t).sum(1);mask=np.ones(len(p),bool) if name in ['F','G'] else ~axis
    summary,ratio=summarize(R,N,p,mask);run['summary'][name]=summary
    archive[f'{name}_R_h{step:g}']=R;archive[f'{name}_N_h{step:g}']=N;archive[f'{name}_ratio_h{step:g}']=ratio
   run['axis_formula']='A=beta+sum_n n(pn_prime-pn/r)cos(n phi)/r at phi=0,pi'
   row['runs'].append(run)
  failed=[e for e in inv.evidence if not(e['inner_success'] and e['outer_success'])]
  row.setdefault('quadrature',{})[kind]={'failed':failed,'evaluations':inv.evidence}
  file=item['label']+'_'+kind+'.npz';np.savez_compressed(root/file,**archive)
  row['runs'][-1]['arrays_file']=file
  save();print(item['label'],kind,[(k,v['max_ratio']) for k,v in row['runs'][-1]['summary'].items()], 'seconds',time.monotonic()-start,flush=True)
 row['status']='COMPLETE';save()
out['code_hashes']={n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['farfield_grid_audit.py','adaptive_modal_inverse.py','r2_state_values.py','finite_difference.py']}
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',out['elapsed_seconds'],flush=True)
