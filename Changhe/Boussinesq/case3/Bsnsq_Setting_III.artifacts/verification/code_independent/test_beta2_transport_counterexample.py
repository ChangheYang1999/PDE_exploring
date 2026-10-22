from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from beta2_transport_counterexample import Counterexample
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Smooth transport-only counterexample, explicitly not a B2 solution. Floating point checks, not certified bounds.','source_sha256':hashlib.sha256(Path('code_independent/beta2_transport_counterexample.py').read_bytes()).hexdigest()}
rng=np.random.default_rng(8712);p=np.vstack((rng.uniform(-4,4,(137,2)),[[0,0],[.1,.2],[.2,-.1],[1,0],[-1,0],[1.2,0],[.1,1.5],[1.5,1.5],[3.,-1.3]]));rows=[]
for order in (32,64,96):
 f=Counterexample(order);v=f.fields(p[:,0],p[:,1]);W=2*p+np.column_stack((v['U1'],v['U2']));rt=W[:,0]*v['Theta_x']+W[:,1]*v['Theta_y']
 rows.append({'order':order,'max_analytic_temperature_residual':float(np.max(abs(rt))),'moments':f.mom.tolist(),'field_values':{k:np.asarray(z).tolist() for k,z in v.items()}})
out['points']=p.tolist();out['quadrature']=rows
out['finite_differences']=[]
for step in (.004,.002,.001):
 tx=derivative(f.theta,p,0,step);ty=derivative(f.theta,p,1,step);ox=derivative(f.omega,p,0,step);oy=derivative(f.omega,p,1,step)
 ell=-derivative(f.psi,p,0,step,order=2)-derivative(f.psi,p,1,step,order=2)-v['Omega']
 row={'step':step,'max_R_Theta':float(np.max(abs(W[:,0]*tx+W[:,1]*ty))),'max_E':float(np.max(abs(ell))),'max_R_Omega':float(np.max(abs(W[:,0]*ox+W[:,1]*oy+v['Omega']-tx))),'core_vorticity_residual':(W[:,0]*ox+W[:,1]*oy+v['Omega']-tx)[138:140].tolist()};out['finite_differences'].append(row);print(row,flush=True)
angles=np.arange(360)*2*np.pi/360;out['far_field']=[]
for radius in (10.,100.,1000.,10000.):
 q=radius*np.column_stack((np.cos(angles),np.sin(angles)));q=np.vstack((q,[[radius,1.35],[radius,1.5],[radius,1.75]]));z=f.fields(q[:,0],q[:,1]);out['far_field'].append({'r':radius,'max_rU':float(radius*np.max(np.hypot(z['U1'],z['U2']))),'max_rOmega':float(radius*np.max(abs(z['Omega'])))})
axis=np.linspace(-2,2,801);z=f.fields(axis,np.zeros_like(axis));out['axis']={'max_W_on_segment':float(np.max(abs(2*axis[abs(axis)<=1]+z['U1'][abs(axis)<=1]))),'min_signx_W_outside':float(np.min(np.sign(axis[abs(axis)>1])*(2*axis[abs(axis)>1]+z['U1'][abs(axis)>1]))),'W_y_max':float(np.max(abs(z['U2'])))}
# Near the flat cutoff, double precision may round a tiny nonzero W to zero.
out['roundoff_note']='Axis values immediately outside x=1 can round to zero; exact strict positivity is analytic, not certified by this scan.'
Path('verification/beta2_transport_counterexample_partial.json').write_text(json.dumps(out,indent=2)+'\n')
points=np.array([[.13,.27],[.73,1.21],[1.23,-.41],[2.51,1.43],[6.17,-2.31]]);out['inverse_points']=points.tolist();out['inverse']=[]
for radius in (8.,16.,32.):
 for order in (24,48,96):
  inv=CartesianInverse(f.omega,InverseSettings(radius=radius,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1.))
  full=inv.relative(points);cut=inv.relative(points,include_exterior=False);row={'radius':radius,'order':order,'full_error':float(np.max(abs(full-f.velocity(points)))),'omit_exterior_error':float(np.max(abs(cut-f.velocity(points))))};out['inverse'].append(row);print(row,flush=True)
out['ended_utc']=datetime.now(timezone.utc).isoformat();out['elapsed_seconds']=time.monotonic()-start;Path('verification/beta2_transport_counterexample.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
