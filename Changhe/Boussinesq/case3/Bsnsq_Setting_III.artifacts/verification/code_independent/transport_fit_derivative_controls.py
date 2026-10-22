"""P213: independent base, linearity and finite-difference controls.

Reads NUM source only to archive map conventions. No NUM imports or executions.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,os,resource,traceback
import numpy as np
from r2_state_values import R2State
from sensitive_modal_flow import C2ModalFlow,reconstruct_sensitivity
from smooth_modal_flow import reconstruct
from native_coefficient_values import divided_values
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/213_transport_fit_derivative_controls/verification'
P212=ROOT/'research/212_moment_jacobian_actions/verification'
P210=ROOT/'research/210_independent_jacobian_actions/verification'
P202=ROOT/'research/202_moment_inverse_and_flow_sensitivity/verification'
SOURCE=ROOT/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz'
MATRIX=ROOT/'research/208_saved_jacobian_audit/verification/frozen_sources/jac_L2v.npz'
POINTS=np.array([[.2,.1],[.8,.4],[1.,1.],[.3,3.],[3.,1.]])
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,j):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(j,indent=2)+'\n');t.replace(p)
def values(r):return np.r_[r['Theta'],r['gradient'],r['Omega']]
def main():
 start=time.monotonic();OUT.mkdir(parents=True,exist_ok=True)
 s=R2State(SOURCE);b=s.beta;a0=float(s.meta['a0'])
 j212=json.loads((P212/'actions.json').read_text());assert j212['status']=='COMPLETE' and j212['source_sha256']==s.sha256
 with np.load(MATRIX,allow_pickle=False) as z:JT=z['JT'];xs=z['x_star'];f0=z['f0'];active=z['act_idx'];q=z['c_act'];lam=float(z['lam']);bmat=float(z['beta'])
 with np.load(P202/'inverse_nodes.npz',allow_pickle=False) as z:r=z['radii'];base=[z[k] for k in ['pr_base','dp_base','H_base','Hp_base']]
 flow0=C2ModalFlow(b,r,*base)
 out={'started_utc':now(),'pid':os.getpid(),'priority':os.getpriority(os.PRIO_PROCESS,0),'status':'RUNNING','source_sha256':s.sha256,'matrix_sha256':sha(MATRIX),'checks':[],'base_outputs':[],'directions':[],'linearity':[],'map_conventions':{'input_projection':'same affine strain projection','output':'NUM fits temperature then integrates its derivative, then fits G; own map transports raw gradient','amplitude':'NUM free_a0=False, fixed a0 from archive','boundary':'NUM higher local jets, fixed RK4 stopping within radius; own leading jets, exact-radius event and compatible gradient','stored_r_in':float(s.meta['r_in']),'stored_dt':float(s.meta['dt'])}}
 sources=[SOURCE,MATRIX,P212/'actions.json',P202/'inverse_nodes.npz',ROOT/'research/213_transport_fit_derivative_controls/PROOF.md']
 sources += [ROOT/'code_independent'/n for n in ['transport_fit_derivative_controls.py','r2_state_values.py','sensitive_modal_flow.py','smooth_modal_flow.py','native_coefficient_values.py']]
 out['input_hashes']={str(p.relative_to(ROOT)):sha(p) for p in sources}
 raw=OUT/'source_inspection';raw.mkdir(exist_ok=True)
 for name in ['jacobian_fp.py','charnewton.py']:
  p=ROOT.parent/'numerics/code'/name;(raw/name).write_bytes(p.read_bytes())
  out['input_hashes'][str(p)]=sha(p)
 def save():
  out.update(updated_utc=now(),elapsed_seconds=time.monotonic()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss);dump(OUT/'controls.json',out)
 def check(name,error,tolerance):
  out['checks'].append({'name':name,'error':float(error),'tolerance':float(tolerance),'pass':bool(error<=tolerance)})
  if error>tolerance:raise RuntimeError(name)
 check('matrix_base_active_coefficients',max(abs(xs-s.rawG[active])),0.)
 check('matrix_beta',abs(b-bmat),0.);check('matrix_lambda',abs(lam-float(s.meta['lam'])),0.)
 q2=q@q;check('projection_array_direction',np.linalg.norm(JT@q)/np.linalg.norm(q),1e-6)
 coeffs={};nodes={};df={}
 for label in ['coefficient_weakest','physical_weakest']:
  with np.load(P210/label/'vectors.npz',allow_pickle=False) as z:v=z['v'];d=z['projected_direction'];saved=z['JT_action'];qown=z['q']
  coeffs[label]=v
  with np.load(P212/label/'inverse_nodes.npz',allow_pickle=False) as z:
   assert np.array_equal(z['radii'],r);nodes[label]=[z[k] for k in ['pr','dp','H','Hp']]
  df[label]=C2ModalFlow(0.,r,*nodes[label])
  check(label+'_q',max(abs(q-qown)),2e-14)
  check(label+'_saved_action',max(abs(saved-JT@v)),1e-13)
  check(label+'_projected_array_action',np.linalg.norm(JT@v-JT@d),abs(q@v)/q2*np.linalg.norm(JT@q)+5e-13)
 # Zeroth order is compared to the saved fitted map output, not only to the stored input.
 for X in POINTS:
  fitted=float(X[0]*divided_values(s,xs+f0,active,X[None])[0]);identity=float(s.omega(*X))
  for tol in [1e-12,3e-14]:
   ans=reconstruct(flow0,X,b,a0,cutoff=.001,rtol=tol,atol=.01*tol,compatible_seed=True)
   ans.update(saved_fitted_base_Omega=fitted,stored_input_Omega=identity,stored_input_Theta=float(s.theta(*X)))
   if ans['status']=='COMPLETE':
    den=max(abs(fitted),abs(ans['Omega']));ans.update(Omega_absolute_gap=abs(ans['Omega']-fitted),Omega_relative_gap=abs(ans['Omega']-fitted)/den if den else None)
   out['base_outputs'].append(ans);save()
 cache={};singles={}
 for label in ['coefficient_weakest','physical_weakest']:
  row={'label':label,'analytic':[],'differences':[]};out['directions'].append(row)
  def f(offset):
   key=(label,float(offset))
   if key not in cache:cache[key]=C2ModalFlow(b,r,*[x+offset*y for x,y in zip(base,nodes[label])])
   return cache[key]
  evcache={}
  for X in POINTS:
   for tol in [1e-12,3e-14]:
    ana=reconstruct_sensitivity(flow0,df[label],X,b,a0,cutoff=.001,rtol=tol,atol=.01*tol)
    row['analytic'].append(ana)
    if tol==3e-14:singles[(label,*X)]=np.array(ana['derivative_Theta_gradient_Omega'])
    for h in [.01,.003,.001]:
     ev=[]
     for mul in [-2,-1,1,2]:
      key=(*X,float(mul*h),tol)
      if key not in evcache:evcache[key]=reconstruct(f(mul*h),X,b,a0,cutoff=.001,rtol=tol,atol=.01*tol,compatible_seed=True)
      ev.append(evcache[key])
     rec={'point':X.tolist(),'step':h,'rtol':tol,'evaluations':ev}
     if all(e['status']=='COMPLETE' for e in ev):
      vv=[values(e) for e in ev];der=(vv[0]-8*vv[1]+8*vv[2]-vv[3])/(12*h);cen=(vv[2]-vv[1])/(2*h)
      ar=np.array(ana['derivative_Theta_gradient_Omega']);den=np.maximum(abs(der),abs(ar))
      rec.update(status='COMPLETE',derivative=der.tolist(),second_order=cen.tolist(),analytic=ar.tolist(),absolute_difference=abs(der-ar).tolist(),relative_difference=np.divide(abs(der-ar),den,out=np.zeros(4),where=den!=0).tolist(),zero_denominator=(den==0).tolist())
     else:rec['status']='FAILED'
     row['differences'].append(rec);save()
   print(now(),label,'point',X.tolist(),'elapsed',out['elapsed_seconds'],flush=True)
 # Linear response to the unnormalized sum; neither summand is rescaled here.
 ndsum=[x+y for x,y in zip(nodes['coefficient_weakest'],nodes['physical_weakest'])]
 dsum=C2ModalFlow(0.,r,*ndsum)
 for X in POINTS:
  ans=reconstruct_sensitivity(flow0,dsum,X,b,a0,cutoff=.001,rtol=3e-14,atol=3e-16)
  target=singles[('coefficient_weakest',*X)]+singles[('physical_weakest',*X)]
  obs=np.array(ans['derivative_Theta_gradient_Omega']);den=np.maximum(abs(obs),abs(target))
  ans.update(sum_of_separate=target.tolist(),absolute_linearity_error=abs(obs-target).tolist(),relative_linearity_error=np.divide(abs(obs-target),den,out=np.zeros(4),where=den!=0).tolist())
  out['linearity'].append(ans);save()
 out.update(status='COMPLETE',ended_utc=now());save();print(now(),'COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':
 try:main()
 except Exception:
  OUT.mkdir(parents=True,exist_ok=True);(OUT/'failure.txt').write_text(now()+'\n'+traceback.format_exc());raise
