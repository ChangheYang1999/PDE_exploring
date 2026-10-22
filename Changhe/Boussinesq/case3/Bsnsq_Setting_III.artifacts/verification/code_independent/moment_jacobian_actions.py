"""P212: stable whole-plane inverse and analytic selected-input sensitivities.

All evaluator modules belong to this lane. NUM data only, no NUM code imports.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,os,traceback,resource
import numpy as np
from r2_state_values import R2State
from moment_modal_inverse import exact_moment2,R2DifferentiableModes,MomentModalInverse
from adaptive_modal_inverse import ModalSettings
from sensitive_modal_flow import C2ModalFlow,reconstruct_sensitivity
from smooth_modal_flow import reconstruct
from cartesian_inverse import CartesianInverse,InverseSettings
from native_coefficient_values import divided_values

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/212_moment_jacobian_actions/verification'
OLD=ROOT/'research/210_independent_jacobian_actions/verification'
BASE=ROOT/'research/202_moment_inverse_and_flow_sensitivity/verification'
SOURCE=ROOT/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz'
POINTS=np.array([[.2,.1],[.8,.4],[1.,1.],[.3,3.],[3.,1.]])

def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(x,indent=2)+'\n');t.replace(p)
def values(row):return np.r_[row['Theta'],row['gradient'],row['Omega']]

def main():
 start=time.monotonic();OUT.mkdir(parents=True,exist_ok=True)
 s=R2State(SOURCE);a0=float(s.meta['a0']);lam=float(s.meta['lam'])
 old=json.loads((OLD/'actions.json').read_text());base_report=json.loads((BASE/'native_results.json').read_text())
 assert old['status']=='COMPLETE' and base_report['status']=='COMPLETE'
 assert old['source_sha256']==s.sha256==base_report['source_sha256']
 with np.load(BASE/'inverse_nodes.npz',allow_pickle=False) as z:
  radii=z['radii'];pb=z['pr_base'];db=z['dp_base'];hb=z['H_base'];hpb=z['Hp_base']
 with np.load(ROOT/'research/200_projected_characteristic_response/verification/native_inverse_nodes.npz',allow_pickle=False) as z:assert np.array_equal(z['radii'],radii)
 out={'started_utc':now(),'pid':os.getpid(),'priority':os.getpriority(os.PRIO_PROCESS,0),'status':'RUNNING',
  'source_sha256':s.sha256,'a0':a0,'beta':s.beta,'lambda':lam,'directions':[],'checks':[],
  'base_cache_source':str((BASE/'inverse_nodes.npz').relative_to(ROOT)),
  'base_moment2_exact':base_report['base_moment2_exact'],
  'scope':'Independent finite-cutoff selected input derivatives. Exact second-mode moment; C2 interpolant; analytic moving-hit sensitivity and separate parameter differences. No exact-map or nonlinear-root enclosure.'}
 sources=[SOURCE,OLD/'actions.json',BASE/'inverse_nodes.npz',BASE/'native_results.json',ROOT/'research/212_moment_jacobian_actions/PROOF.md']
 sources += [ROOT/'code_independent'/n for n in ['moment_jacobian_actions.py','moment_modal_inverse.py','sensitive_modal_flow.py','smooth_modal_flow.py','r2_state_values.py','adaptive_modal_inverse.py','cartesian_inverse.py','native_coefficient_values.py']]
 out['input_hashes']={str(p.relative_to(ROOT)):sha(p) for p in sources}
 def save():
  out.update(updated_utc=now(),elapsed_seconds=time.monotonic()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  dump(OUT/'actions.json',out)
 def check(name,error,tolerance):
  out['checks'].append({'name':name,'error':float(error),'tolerance':float(tolerance),'pass':bool(error<=tolerance)})
  if error>tolerance:raise RuntimeError(name+' failed')
 decay=1/s.bb
 for label in ['coefficient_weakest','physical_weakest']:
  folder=OUT/label;folder.mkdir(exist_ok=True)
  sd=R2State(OLD/label/'direction_state.npz')
  with np.load(OLD/label/'vectors.npz',allow_pickle=False) as z:d=z['projected_direction'];q=z['q'];jv=z['JT_action'];active=z['active'];v=z['v']
  with np.load(OLD/label/'inverse_nodes.npz',allow_pickle=False) as z:
   assert np.array_equal(z['radii'],radii);oldp=z['pr'];oldd=z['dp']
  modes=R2DifferentiableModes(sd);moment=exact_moment2(sd)
  t=sd.edges[1:-1];knots=sd.L*np.sqrt(np.expm1(-2*sd.bb*np.log1p(-t)))
  inv=MomentModalInverse(modes,sd.K,ModalSettings(decay,2e-13,2e-11),moment,knots)
  row={'label':label,'stage':'mode_controls','moment2_exact':str(moment),'moment2_float':float(moment),'projected_strain_q':float(q@d),
   'direction_state_sha256':sd.sha256,'vectors_sha256':sha(OLD/label/'vectors.npz'),'mode_derivative_controls':[],
   'node_evidence':[],'interpolation_checks':[],'cartesian_inverse':[],'sensitivities':[],'parameter_differences':[]}
  out['directions'].append(row)
  check(label+'_moment_strain',abs(float(moment)+2*float(q@d)),2e-15)
  for r in [1e-4,.01,.3,1.,3.,20.]:
   h=r*1e-4;mv=[modes(r+j*h) for j in [-2,-1,1,2]]
   fd=(mv[0]-8*mv[1]+8*mv[2]-mv[3])/(12*h);direct=modes.derivative(r)
   err=np.max(abs(fd-direct));tol=5e-8*max(1.,np.max(abs(direct)))
   check(label+f'_mode_derivative_{r}',err,tol)
   row['mode_derivative_controls'].append({'r':r,'step':h,'max_absolute_error':float(err),'max_derivative':float(max(abs(direct)))})
  vals=[[],[],[],[]];nodes=folder/'inverse_nodes.npz'
  if nodes.exists():
   with np.load(nodes,allow_pickle=False) as z:
    assert np.array_equal(z['radii'],radii) and str(z['direction_sha256'])==sd.sha256
    vals=[list(z[k]) for k in ['pr','dp','H','Hp']]
   row['reused_nodes']=len(vals[0])
  def save_nodes():np.savez_compressed(nodes,radii=radii,direction_sha256=np.asarray(sd.sha256),pr=np.asarray(vals[0]),dp=np.asarray(vals[1]),H=np.asarray(vals[2]),Hp=np.asarray(vals[3]))
  row['stage']='inverse_nodes';save()
  for i in range(len(vals[0]),len(radii)):
   r=float(radii[i]);inv.settings.epsabs=2e-12*min(r,.1);pdir,ddir=inv.radial(r)
   for ar,value in zip(vals,[pdir,ddir,modes(r),modes.derivative(r)]):ar.append(value)
   row['node_evidence'].append(inv.evidence[-1])
   if i%20==0 or i+1==len(radii):
    row['nodes_completed']=i+1;save_nodes();save();print(now(),label,'nodes',i+1,'/',len(radii),'elapsed',out['elapsed_seconds'],flush=True)
  pd,dd,hd,hpd=map(np.asarray,vals)
  row['old_node_comparison']={'max_pr_difference':float(np.max(abs(pd-oldp))),'max_dp_difference':float(np.max(abs(dd-oldd)))}
  cacheflow={}
  def flow(offset=0.,grid='fine'):
   key=(float(offset),grid)
   if key not in cacheflow:
    sl=slice(None,None,2 if grid=='coarse' else 1)
    cacheflow[key]=C2ModalFlow(s.beta,radii[sl],(pb+offset*pd)[sl],(db+offset*dd)[sl],(hb+offset*hd)[sl],(hpb+offset*hpd)[sl])
   return cacheflow[key]
  direction=C2ModalFlow(0.,radii,pd,dd,hd,hpd);dircoarse=C2ModalFlow(0.,radii[::2],pd[::2],dd[::2],hd[::2],hpd[::2])
  fine=flow();coarse=flow(grid='coarse');row['stage']='inverse_validation';save()
  for X in np.r_[POINTS,[[r*np.sin(ph),-r*np.cos(ph)] for r in [.0004,.004,.04,.4,4.,20.] for ph in [.37,1.61,2.43]]]:
   inv.settings.epsabs=2e-13;exact=inv.relative(X[None])[0]
   wf,dwf,of=direction.values(X);wc,dwc,oc=dircoarse.values(X)
   row['interpolation_checks'].append({'point':X.tolist(),'fine_velocity_error':float(max(abs(wf-exact))),
    'coarse_velocity_error':float(max(abs(wc-exact))),'DW_resolution_difference':float(np.max(abs(dwf-dwc))),
    'fine_source_error':float(abs(of-sd.omega(*X))),'coarse_source_error':float(abs(oc-sd.omega(*X))),
    'divergence_error':float(abs(np.trace(dwf)))})
  for order in [24,36]:
   pts=POINTS[[0,2,4]];exact=inv.relative(pts)
   settings=InverseSettings(radius=12.,core_radial_order=order,core_angular_order=3*order,
    exterior_radial_order=4*order,exterior_angular_order=4*order,decay_power=decay)
   cart=CartesianInverse(sd.omega,settings).relative(pts)
   row['cartesian_inverse'].append({'order':order,'points':pts.tolist(),'modal':exact.tolist(),'cartesian':cart.tolist(),
    'absolute_component_errors':abs(cart-exact).tolist(),'settings':settings.__dict__})
   save();print(now(),label,'Cartesian',order,'maxerror',float(np.max(abs(cart-exact))),flush=True)
  row['stage']='sensitivities';save();evcache={}
  def evaluate(X,h):
   key=(*X,float(h))
   if key not in evcache:evcache[key]=reconstruct(flow(h),X,s.beta,a0,cutoff=.001,rtol=1e-12,atol=1e-14,compatible_seed=True)
   return evcache[key]
  for X in POINTS:
   fitted=float(X[0]*divided_values(s,jv,active,X[None])[0])
   for cutoff,grid,tol in [(.003,'fine',1e-10),(.001,'fine',1e-10),(.0003,'fine',1e-10),(.001,'coarse',1e-10),(.001,'fine',1e-12)]:
    ans=reconstruct_sensitivity(fine if grid=='fine' else coarse,direction if grid=='fine' else dircoarse,X,s.beta,a0,cutoff=cutoff,rtol=tol,atol=tol*.01)
    ans.update(grid=grid,fitted_array_Omega_action=fitted)
    if ans['status']=='COMPLETE':
     a=ans['derivative_Theta_gradient_Omega'][-1];den=max(abs(a),abs(fitted))
     ans.update(absolute_gap=float(abs(a-fitted)),relative_gap=float(abs(a-fitted)/den) if den else None,denominator=float(den))
    row['sensitivities'].append(ans);save()
   for step in [2e-4,1e-4,5e-5]:
    ev=[evaluate(X,j*step) for j in [-2,-1,1,2]]
    rec={'point':X.tolist(),'step':step,'cutoff':.001,'rtol':1e-12,'grid':'fine','evaluations':ev,'fitted_array_Omega_action':fitted}
    if all(a['status']=='COMPLETE' for a in ev):
     va=[values(a) for a in ev];der=(va[0]-8*va[1]+8*va[2]-va[3])/(12*step)
     den=max(abs(der[-1]),abs(fitted));rec.update(status='COMPLETE',derivative_Theta_gradient_Omega=der.tolist(),
      second_order_difference=((va[2]-va[1])/(2*step)).tolist(),absolute_gap=float(abs(der[-1]-fitted)),relative_gap=float(abs(der[-1]-fitted)/den) if den else None,denominator=float(den))
    else:rec['status']='FAILED'
    row['parameter_differences'].append(rec);save()
   print(now(),label,'point',X.tolist(),'elapsed',out['elapsed_seconds'],flush=True)
  row['additional_inverse_evidence']=inv.evidence;row.update(stage='COMPLETE',ended_utc=now());save()
 out.update(status='COMPLETE',ended_utc=now());save();print(now(),'COMPLETE elapsed',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
 try:main()
 except Exception:
  OUT.mkdir(parents=True,exist_ok=True);(OUT/'failure.txt').write_text(now()+'\n'+traceback.format_exc());raise
