"""Independent native-basis source checks, including analytic and Cartesian inverses."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,time,hashlib,shutil
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from cartesian_inverse import CartesianInverse,InverseSettings
root=Path('verification/fixed_velocity_block_20261021T0056');start=time.monotonic()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','manufactured':[],'archived':[]}
points=np.array([[0.,0.],[.2,.3],[.7,-.4],[-.4,1.2],[1.7,.5]])
for bs in [2.5,3.]:
 ref=None
 for bu in [2.1,2.6,3.2]:
  Nt=4;deg=3;K=4;nb=Nt+deg
  source=np.zeros((K,nb));source[0]=1.
  p=root/f'manufacture_source{bs}_unknown{bu}.npz'
  np.savez_compressed(p,cF=np.zeros(K*nb),cG=np.zeros(K*nb),cG_ext=np.zeros(K*nb),cG_f=source.ravel(),cG_f_effective=np.zeros(0),beta_seed=bs,beta=bu,beta_basis=bu,L=1.,Nt=Nt,deg=deg,K=K,grade=1.,rmap='r2',eps=1.,lam=.7,source_mode='fixed_velocity_block')
  s=R2State(p);m=R2ModeSource(s,kind='native_seed')
  inv=AdaptiveModalInverse(m,K,ModalSettings(1/bs,2e-12,2e-12));actual=inv.relative(points)
  a=(bs+1)/(2*bs);analytic=[]
  for x,y in points:
   r=np.hypot(x,y)
   if r==0:analytic.append([0.,0.]);continue
   ll=np.log1p(r*r)
   C=np.expm1((1-a)*ll)/(2*(1-a))
   I2=.5*(np.expm1((2-a)*ll)/(2-a)-np.expm1((1-a)*ll)/(1-a))
   pr=.5*(I2/r**2-C);dp=-.5*(I2/r**2+C)
   vr=pr*y/r;vt=dp*x/r
   analytic.append([vr*x/r-vt*y/r,vr*y/r+vt*x/r])
  error=float(np.max(np.abs(actual-np.array(analytic))))
  assert error<3e-11,error
  if ref is not None:assert np.array_equal(actual,ref)
  ref=actual
  row=dict(source_beta=bs,unknown_beta=bu,modal_analytic_max_error=error,source_strain=float(s.strain('native_seed')),source_field_error=float(np.max(np.abs(s.mixed_omega(*points.T)-.7*points[:,0]*(1+(points**2).sum(1))**(-a)))),inverse_flags_all=all(q['inner_success'] and q['outer_success'] for q in inv.evidence))
  assert row['source_field_error']<1e-14
  if bu==2.6:
   row['cartesian']=[]
   for R in [8.,16.]:
    ci=CartesianInverse(lambda x,y:s.divided(x,y,'native_seed')*x,InverseSettings(R,16,32,48,48,1/bs))
    cv=ci.relative(points)
    ce=float(np.max(np.abs(cv-actual)));row['cartesian'].append(dict(radius=R,max_component_error=ce))
    assert ce<2e-9,ce
  out['manufactured'].append(row)
  print('manufacture',bs,bu,error,flush=True)
# Actual archived source, duplicated into explicit new-schema test archives only.
seed=Path('verification/additive_driver_20261020T2128/lambda_seed_snapshot.npz')
with np.load(seed,allow_pickle=False) as z:original={k:z[k].copy() for k in z.files}
# Preserve original seed coefficients and geometry; only the UNKNOWN exponent changes.
bs=float(original['beta_basis']);f=original['cG_ext']-original['cG'];reference=None
for bu in [2.6,3.003,3.4]:
 d=dict(original);d.update(cG_f=f,cG_f_effective=np.zeros(0),beta_seed=np.array(bs),beta=np.array(bu),beta_basis=np.array(bu),source_mode=np.array('fixed_velocity_block'),eps=np.array(1.),lam=np.array(.99))
 p=root/f'archive_schema_manufacture_unknown{bu}.npz';np.savez_compressed(p,**d)
 s=R2State(p);m=R2ModeSource(s,kind='native_seed');inv=AdaptiveModalInverse(m,s.K,ModalSettings(1/bs,1e-11,1e-11));v=inv.relative(points)
 if reference is not None:assert np.array_equal(v,reference)
 reference=v
 row=dict(unknown_beta=bu,seed_beta=bs,source_sha256=hashlib.sha256(seed.read_bytes()).hexdigest(),synthetic_schema_sha256=s.sha256,source_strain=float(s.strain('native_seed')),inverse_flags_all=all(q['inner_success'] and q['outer_success'] for q in inv.evidence),cartesian=[])
 if bu==3.003:
  for order in [32,64]:
   ci=CartesianInverse(lambda x,y:s.divided(x,y,'native_seed')*x,InverseSettings(12.,24,order,order,order,1/bs));vc=ci.relative(points)
   row['cartesian'].append(dict(order=order,max_component_error=float(np.max(np.abs(vc-v)))))
 out['archived'].append(row);print('archive',bu,row['cartesian'],flush=True)
# Legacy archive still means effective source in the stage basis.
p=Path('verification/lambda096_K12_20261021T0050')
manifest=json.loads((p/'manifest.json').read_text());s=R2State(p/manifest['states'][0]['snapshot'])
assert not s.native_source and s.Ds is not None
radii=np.geomspace(1e-5,1e8,50);new=R2ModeSource(s);old=[]
for r in radii:
 t=-np.expm1(-np.log1p((r/s.L)**2)/(2*s.bb));a=np.asarray(s.Gs(t)).copy();a[1::2]*=r/np.hypot(r,s.L);D=np.exp(-(s.bb+1)*np.log1p((r/s.L)**2)/(2*s.bb));c=np.zeros(s.K);c[0]+=a[0]
 for k in range(1,len(a)):
  c[k]+=.5*a[k]
  if k>=2:c[k-2]-=.5*a[k]
 old.append(r*D*c)
old=np.array(old);new=np.array([new(r) for r in radii]);err=float(np.max(abs(new-old)/(1+abs(old))))
assert err<3e-14,err
out['legacy_mode_regression_error']=err
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,limitations='Finite precision and sampled quadrature, not rigorous certification. Schema manufactures are not numerics candidates and are named accordingly. No fitting-lane code imported or executed.')
out['code_hashes']={f:hashlib.sha256((Path('code_independent')/f).read_bytes()).hexdigest() for f in ['check_native_source_schema.py','r2_state_values.py','adaptive_modal_inverse.py','cartesian_inverse.py','farfield_grid_audit.py']}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for f in out['code_hashes']:shutil.copyfile(Path('code_independent')/f,root/f)
print('COMPLETE',out['elapsed_seconds'],flush=True)
