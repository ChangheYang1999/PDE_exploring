"""Independent regression and mismatched-source-geometry tests; Python only."""
from pathlib import Path
from datetime import datetime,timezone
import sys,time,json,hashlib,importlib.util,importlib.machinery
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
from cartesian_inverse import CartesianInverse,InverseSettings
root=Path('verification/source_geometry_20261021T0120');start=time.monotonic()
oldloader=importlib.machinery.SourceFileLoader('previous_independent_reader',str(root/'r2_state_values.py.before'))
spec=importlib.util.spec_from_loader(oldloader.name,oldloader);oldmod=importlib.util.module_from_spec(spec);oldloader.exec_module(oldmod)
points=np.array([[0.,0.],[.2,.3],[.7,-.4],[-.4,1.2],[1.7,.5],[12.,-8.]])
out={'started_utc':datetime.now(timezone.utc).isoformat(),'legacy':[],'manufactures':[]}
legacy=['verification/lambda096_K16_20261021T0110/blam16f_lambda0.96.npz','verification/gauge040_20261021T0033/bfree1os3_eps0.04.npz','verification/fixed_velocity_block_20261021T0056/archive_schema_manufacture_unknown3.003.npz']
radii=np.geomspace(1e-6,1e9,85);theta=np.linspace(-np.pi,np.pi,31)
x=(radii[:,None]*np.cos(theta)).ravel();y=(radii[:,None]*np.sin(theta)).ravel()
for path in legacy:
 s=R2State(path);old=oldmod.R2State(path);errors={}
 for kind in ['F','G','external']+(['defect'] if s.Ds is not None else [])+(['native_seed'] if s.native_source else []):
  a=s.divided(x,y,kind);b=old.divided(x,y,kind);err=float(np.max(abs(a-b)/(1+abs(b))));assert err<3e-14
  errors[kind]=err
 out['legacy'].append({'file':path,'sha256':s.sha256,'point_count':len(x),'max_relative_errors':errors})
sourceK=8;sourceNt=6;sourceDeg=3;sourceNb=sourceNt+sourceDeg
source=np.zeros((sourceK,sourceNb));source[0]=1.;source[1]=.3
for k in range(2,sourceK):source[k,k//2:]=(.03*(-1)**k)/(k+1)
reference=None
for K,Nt,degree,grade,L,beta in [(4,4,5,1.7,2.3,2.8),(12,7,3,1.,1.2,3.01),(16,9,5,2.,.4,3.5)]:
 nb=Nt+degree;path=root/f'manufacture_unknownK{K}_sourceK8.npz'
 meta=dict(cF=np.zeros(K*nb),cG=np.zeros(K*nb),cG_ext=np.zeros(K*nb),cG_f=source.ravel(),cG_f_effective=np.zeros(0),beta_seed=3.,beta=beta,beta_basis=beta,L=L,Nt=Nt,deg=degree,K=K,grade=grade,rmap='r2',eps=1.,lam=.7,source_mode='fixed_velocity_block',seed_K=sourceK,seed_Nt=sourceNt,seed_deg=sourceDeg,seed_grade=1.2,seed_L=.7,seed_rmap='r2')
 np.savez_compressed(path,**meta);s=R2State(path);ms=R2ModeSource(s,kind='native_seed');assert ms.count==8
 inv=AdaptiveModalInverse(ms,ms.count,ModalSettings(1/3,2e-12,2e-12));v=inv.relative(points)
 value=s.divided(x,y,'native_seed');strain=float(s.strain('native_seed'))
 if reference is not None:
  assert np.array_equal(v,reference[0]);assert np.array_equal(value,reference[1]);assert strain==reference[2]
 reference=(v,value,strain)
 # Angular coefficients also checked through a separate sampled orthogonality integral.
 phi=(np.arange(256)+.5)*2*np.pi/256
 angular=[]
 for r in [.1,.7,2.,100.]:
  field=r*np.sin(phi)*s.divided(r*np.sin(phi),-r*np.cos(phi),'native_seed')
  recovered=2/256*(np.sin(np.arange(1,9)[:,None]*phi)@field)
  angular.append(float(np.max(abs(recovered-ms(r)))))
 assert max(angular)<2e-14
 row={'unknown_geometry':{k:meta[k] for k in ['K','Nt','deg','grade','L','beta']},'source_geometry':{k:meta[k] for k in meta if k.startswith('seed_')},'source_strain':strain,'angular_reconstruction_errors':angular,'all_quadrature_success':all(q['inner_success'] and q['outer_success'] for q in inv.evidence),'cartesian':[]}
 if K==4:
  for order in [32,64]:
   ci=CartesianInverse(lambda xx,yy:xx*s.divided(xx,yy,'native_seed'),InverseSettings(10.,24,order,order,order,1/3))
   cv=ci.relative(points[:5]);error=float(np.max(abs(cv-v[:5])));row['cartesian'].append({'order':order,'error':error})
  assert row['cartesian'][-1]['error']<3e-7
 out['manufactures'].append(row);print('K',K,'strain',strain,'Cartesian',row['cartesian'],flush=True)
# Contradictory source length must fail rather than be interpreted in unknown geometry.
meta['seed_K']=7;p=root/'manufacture_bad_source_length.npz';np.savez_compressed(p,**meta)
try:R2State(p)
except ValueError as e:out['bad_length_rejected']=str(e)
else:raise AssertionError('invalid source accepted')
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,limitations='Manufactured source archives only; not candidate fields. Floating-point inverse comparisons are not interval certificates.')
out['code_hashes']={n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['r2_state_values.py','adaptive_modal_inverse.py','farfield_grid_audit.py','check_separate_source_geometry.py']}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
