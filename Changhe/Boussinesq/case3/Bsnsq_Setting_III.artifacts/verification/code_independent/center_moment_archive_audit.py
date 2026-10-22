"""172: independent local inverse stabilization, global moments checked separately."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,sys,time,hashlib
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,R2ModeSource,ModalSettings
from center_moment_inverse import CenterMomentInverse
from compact_center_moments import moments
from elliptic_cartesian_audit import jacobian,residuals,summarize

def exact_M2(s):
    binary=lambda v:F.from_float(float(v))
    total=F(0)
    for k,sign in [(1,1),(3,-1)]:
        if k>=s.K:continue
        for j in range(s.nb):
            total+=sign*binary(s.Gs.c[j,k])*(binary(s.knots[j+s.degree+1])-binary(s.knots[j]))/(s.degree+1)
    return binary(s.bb)*binary(s.L)*total/2

def main(root):
 root=Path(root);src=Path('verification/elliptic_cartesian_20261021T1336Z');manifest=json.loads((src/'manifest.json').read_text())
 start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','states':[],'scope':'self source only; sampled floating diagnostics. E/div do not validate global harmonic moments. Exact n2 source moment, independent compact-cell quadrature and direct radial integral comparison retained.'}
 def save():
  out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
 save()
 for item in manifest['states']:
  path=src/item['snapshot'];assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'];s=R2State(path);H=R2ModeSource(s);M=exact_M2(s)
  state={'label':item['label'],'archive':str(path),'sha256':item['sha256'],'beta':s.beta,'K':s.K,'M2_exact':{'numerator':str(M.numerator),'denominator':str(M.denominator),'float':float(M)},'compact_quadrature':[],'runs':[]};out['states'].append(state);save()
  print('state',item['label'],flush=True);sw=.1
  compact=[]
  for order in [24,48,96]:
   C=moments(s,order=order,switch=sw);compact.append(C);state['compact_quadrature'].append({'order_per_cell':order,'scaled_moments':C.tolist(),'M2_error_vs_exact_rounded':float(C[0]-float(M))})
  state['compact_order_changes']=[float(np.max(abs(b-a))) for a,b in zip(compact,compact[1:])]
  Cref=compact[-1];save()
  angles=np.array([0,np.pi/6,np.pi/3,np.pi/2,2*np.pi/3,5*np.pi/6,np.pi]);uv=np.stack([np.sin(angles),-np.cos(angles)],axis=-1);uv[[0,-1],0]=0;uv[3,1]=0
  radii=np.unique(np.r_[np.geomspace(1e-6,.08,11),.003,.01,.03]);pts=(radii[:,None,None]*uv[None,:,:]).reshape(-1,2);axis=pts[:,0]==0;om=s.omega(*pts.T)
  for tol in [2e-12,2e-14]:
   inv=CenterMomentInverse(H,H.count,ModalSettings(decay=1/s.bb,epsabs=tol,epsrel=tol,limit=4000),switch=sw,exact_M2=M)
   entry={'tolerance':tol,'moment':inv.moment_evidence,'max_scaled_moment_difference_vs_compact96':float(np.max(abs(inv.C-Cref))),'cartesian':[],'point_count':len(pts)};state['runs'].append(entry)
   # This direct integral uses the previous physical-radius Gauss-Kronrod evaluator.
   # Its errors can overlap moment quadrature errors; compact GL is the independent rule.
   old=AdaptiveModalInverse(H,H.count,ModalSettings(decay=1/s.bb,epsabs=2e-13,epsrel=2e-13,limit=4000));checks=[]
   for rr in [.003,.01,.03,.1,.3,1,3]:
    a,b=inv.radial(rr);c,d=old.radial(rr);checks.append({'r':rr,'max_pr_gap':float(np.max(abs(a-c))),'max_dp_gap':float(np.max(abs(b-d)))})
   entry['direct_radial_comparison']=checks
   raw={'points':pts,'omega':om,'axis':axis,'scaled_moments':inv.C,'compact96_scaled_moments':Cref}
   for eta in [2e-4,1e-4,5e-5]:
    st=time.monotonic();jac=jacobian(inv.relative,pts,np.full(len(pts),eta));res=residuals(jac,om);row={'h':eta,'elapsed_seconds':time.monotonic()-st}
    for k,v in res.items():
     row[k]=summarize(v,pts);row[k+'_offaxis']=summarize(v,pts,~axis);raw[f'{eta:.0e}_{k}']=v
    raw[f'{eta:.0e}_jacobian']=jac;entry['cartesian'].append(row);save();print(item['label'],tol,eta,row['E']['max_abs'],row['div']['max_abs'],flush=True)
   entry['local_calls']=len(inv.local_evidence);entry['failed_local']=sum(not z['success'] for z in inv.local_evidence)
   entry['outer_direct_calls']=len(inv.evidence);entry['failed_old_calls']=sum(not z['inner_success'] or not z['outer_success'] for z in old.evidence)
   tag=f'{item["label"]}_tol{tol:.0e}';np.savez_compressed(root/(tag+'.npz'),**raw)
   (root/(tag+'_quadrature.json')).write_text(json.dumps({'moment':inv.moment_evidence,'local':inv.local_evidence,'fallback':inv.evidence,'old_direct_comparison':old.evidence},indent=2)+'\n');save()
 out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main(sys.argv[1])
