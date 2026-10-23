"""Cross-check our angular inverse against our independent cancellation-kernel inverse.

No producer evaluation code or velocity is used. This must pass before interpreting
weighted diagnostics of Q states. Errors are floating point comparisons, not enclosures.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import numpy as np
from angular_log_inverse import QAngular,AngularLogInverse

sources=[
 ('N64','evidence/q_evaluations/drift_N64/q2.json','evidence/q_evaluations/qfree_cl1.5_N64_logwide/snapshot.npz'),
 ('N96_Lf0.125','evidence/q_evaluations/drift_N96_Lf0.125/q2.json','evidence/q_evaluations/qfree_cl1.5_N96_Lf0.125_logwide/snapshot.npz'),
 ('N96_Lf0.25','evidence/q_evaluations/drift_N96_Lf0.25/q2.json','evidence/q_evaluations/qfree_cl1.5_N96_Lf0.25_logwide/snapshot.npz'),
 ('N128','evidence/q_evaluations/drift_N128_Lf0.25/q2.json','evidence/q_evaluations/qfree_cl1.5_N128_Lf0.25_logwide/snapshot.npz')]
# Derive the snapshot path from the independently frozen diagnostic when the original tag differs.
for j,(tag,reference,snapshot) in enumerate(sources):
 if not Path(snapshot).exists():
  diag=Path('evidence/q_drift')/Path(reference).parent.name/'diagnostic.json'
  data=json.loads(diag.read_text())
  candidate=data['metadata'].get('source')
  if candidate and Path(candidate).exists():snapshot=candidate
  else:raise FileNotFoundError(snapshot)
  sources[j]=(tag,reference,snapshot)

out=[];complete=[]
for tag,reference,snapshot in sources:
 data=json.loads(Path(reference).read_text());model=QAngular(snapshot)
 # Retain the first 40 decades and the sparse 60/80-decade points. Avoid the
 # unrelated loss of tiny b in b-a+a at still larger radii.
 pts=[p for p in data['points'] if -2.0001<=math.log10(p['radius'])<=80.0001]
 r=np.array([p['radius'] for p in pts]);theta=np.arctan2([p['y'] for p in pts],[p['x'] for p in pts])
 direct=np.array([p['U'] for p in pts])/r[:,None]
 rhoref=np.array([p['rho']/p['radius'] for p in pts])
 gradref=np.array([[p['residuals'][-1]['rho_x'],p['residuals'][-1]['rho_y']] for p in pts])
 nn=np.arange(len(pts));orders=[]
 for order in [32,64,128]:
  f=AngularLogInverse(model,order).fields(np.log(r),theta)
  get=lambda k:f[k][nn,nn]
  ux=get('ur')*np.cos(theta)-get('ut')*np.sin(theta)
  uy=get('ur')*np.sin(theta)+get('ut')*np.cos(theta)
  rho=get('H')+model.a*np.sin(theta)
  gx=get('grad_radial')*np.cos(theta)-get('grad_angular')*np.sin(theta)
  gy=get('grad_radial')*np.sin(theta)+get('grad_angular')*np.cos(theta)
  vel=np.column_stack((ux,uy));grad=np.column_stack((gx,gy))
  Rr=(model.cl*np.cos(theta)+ux)*gx+(model.cl*np.sin(theta)+uy)*gy-rho
  Nf=np.abs((model.cl*np.cos(theta)+ux)*gx)+np.abs((model.cl*np.sin(theta)+uy)*gy)+abs(rho)
  refnormal=np.array([p['residuals'][-1]['R_Nf'] for p in pts])
  err=dict(velocity_over_radius=float(np.max(abs(vel-direct))),density_over_radius=float(np.max(abs(rho-rhoref))),
           density_gradient=float(np.max(abs(grad-gradref))),R_Nf=float(np.max(abs(abs(Rr)/Nf-refnormal))))
  row=dict(tag=tag,order=order,points=len(pts),log10r_window=[math.log10(min(r)),math.log10(max(r))],errors=err,
           canonical_c=model.c,reference_c=data['center_and_tail']['quadrature'][-1]['c'],snapshot=snapshot,reference=reference)
  orders.append(row);print(json.dumps(row),flush=True)
  complete.append(dict(tag=tag,order=order,points=[dict(x=p['x'],y=p['y'],radius=p['radius'],U_over_r=vel[i].tolist(),rho_over_r=rho[i],
     gradient=grad[i].tolist(),R_over_r=Rr[i],R_Nf=abs(Rr[i])/Nf[i],reference_R_Nf=refnormal[i]) for i,p in enumerate(pts)]))
  if order==128:
   assert err['velocity_over_radius']<2e-8,row
   assert err['density_over_radius']<2e-11,row
   assert err['density_gradient']<2e-8,row
   assert abs(model.c-row['reference_c'])<2e-10,row
 out.extend(orders)
 payload=dict(utc=datetime.now(timezone.utc).isoformat(),status='IN_PROGRESS',rows=out,
              scope='Finite-point floating point agreement between separately implemented angular Green and real-space cancellation inverses; analytical density derivatives versus Cartesian FD8. No interval or uniform global bound.')
 Path('evidence/angular_q_crosscheck.json').write_text(json.dumps(payload,indent=2)+'\n')
payload['status']='PASS';payload['utc']=datetime.now(timezone.utc).isoformat()
Path('evidence/angular_q_crosscheck.json').write_text(json.dumps(payload,indent=2)+'\n')
Path('evidence/angular_q_crosscheck_points.json').write_text(json.dumps(complete,indent=2)+'\n')
print(json.dumps({'status':'PASS','rows':len(out)}),flush=True)
