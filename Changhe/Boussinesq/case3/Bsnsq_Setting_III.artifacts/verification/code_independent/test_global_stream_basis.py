"""Manufactured checks of packet42, independent FD and physical-space inverse."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,os,hashlib
import numpy as np
from global_stream_basis import GlobalBasis,GlobalField,Resolution
from finite_difference import derivative,mixed
from cartesian_inverse import CartesianInverse,InverseSettings

root=Path('research/42_global_stream_representation/verification');start=time.monotonic()
out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'seed':42030,'scope':'Manufactured representation, derivative and inverse checks, not B2 candidates.','source_sha256':hashlib.sha256(Path('code_independent/global_stream_basis.py').read_bytes()).hexdigest(),'cases':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'manufactured.json').write_text(json.dumps(out,indent=2)+'\n')
rng=np.random.default_rng(42030);resolution=Resolution(4,2,1)
p=np.array([[0.,0.],[0.,.371],[0.,-.619],[.00013,.00027],[.137,.271],[.791,-.383],[1.137,.739],[3.173,-2.371]])
for beta in (2.,2.6,3.):
 b=GlobalBasis(p,beta,resolution);coeff=rng.normal(size=b.nvar)*.07;field=GlobalField(beta,coeff,resolution);a=b.fields(coeff)
 row={'beta':beta,'resolution':resolution.__dict__,'coefficients':coeff.tolist(),'center':{key:float(value[0]) for key,value in a.items()},'derivatives':[],'jacobian':[],'inverse':[]};out['cases'].append(row);save()
 for h in (.004,.002,.001):
  sx=derivative(field.psi,p,0,h);sy=derivative(field.psi,p,1,h);vel=np.column_stack((-sy,sx))
  ell=-derivative(field.psi,p,0,h,order=2)-derivative(field.psi,p,1,h,order=2)-field.omega(*p.T)
  fx=derivative(lambda x,y:field.fields(x,y)['F'],p,0,h);fy=derivative(lambda x,y:field.fields(x,y)['F'],p,1,h)
  gx=derivative(lambda x,y:field.fields(x,y)['G'],p,0,h);gy=derivative(lambda x,y:field.fields(x,y)['G'],p,1,h)
  row['derivatives'].append({'h':h,'velocity_max':float(abs(vel-field.velocity(p)).max()),'elliptic_max':float(abs(ell).max()),'F_gradient_max':float(max(abs(fx-a['Fx']).max(),abs(fy-a['Fy']).max())),'G_gradient_max':float(max(abs(gx-a['Gx']).max(),abs(gy-a['Gy']).max())),'c_FD':float(mixed(field.psi,[[0.,0.]],h)[0]),'b0_FD':float(derivative(field.omega,[[0.,0.]],0,h)[0])})
 rr,J=b.residual(coeff,True);direction=rng.normal(size=b.nvar);direction/=np.linalg.norm(direction)
 for h in (1e-3,1e-4,1e-5):
  fd=(b.residual(coeff+h*direction)-b.residual(coeff-h*direction))/(2*h)
  row['jacobian'].append({'h':h,'directional_max':float(abs(fd-J@direction).max())})
 pair=np.array([[.713,-.297],[-.713,-.297]]);vv=field.velocity(pair)
 row['parity']={'Theta':float(field.theta(*pair[0])-field.theta(*pair[1])),'Omega':float(field.omega(*pair[0])+field.omega(*pair[1])),'V1':float(vv[0,0]+vv[1,0]),'V2':float(vv[0,1]-vv[1,1])}
 # The beta2 n2 k1 term is exactly the logarithmic resonance.
 points=np.array([[.137,.271],[.791,-.383],[1.137,.739]])
 for core in (4.,8.,16.):
  for order in (8,16,32):
   inv=CartesianInverse(field.omega,InverseSettings(radius=core,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/beta))
   value=inv.relative(points);cut=inv.relative(points,include_exterior=False);expected=field.velocity(points)
   row['inverse'].append({'radius':core,'order':order,'points':points.tolist(),'velocity':value.tolist(),'expected':expected.tolist(),'max_error':float(abs(value-expected).max()),'omitted_exterior_max_error':float(abs(cut-expected).max())});save()
   print('beta',beta,'core',core,'order',order,'error',row['inverse'][-1]['max_error'],'elapsed',time.monotonic()-start,flush=True)
 row['status']='COMPLETE';save()
out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['elapsed_seconds'],flush=True)
