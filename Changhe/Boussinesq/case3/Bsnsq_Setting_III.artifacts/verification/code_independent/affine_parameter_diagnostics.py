"""P202 unresolved FD discrepancy: affine evaluation, tolerances, wider steps."""
from pathlib import Path
from datetime import datetime,timezone
import os,time,json,traceback,hashlib
import numpy as np
from sensitive_modal_flow import C2ModalFlow,reconstruct_sensitivity
from smooth_modal_flow import reconstruct
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/202_moment_inverse_and_flow_sensitivity/verification'
def now():return datetime.now(timezone.utc).isoformat()
class AffineFlow:
    def __init__(self,base,direction,h):self.base=base;self.direction=direction;self.h=h
    def W(self,X):return self.base.W(X)+self.h*self.direction.W(X)
    def DW(self,X):return self.base.DW(X)+self.h*self.direction.DW(X)
def main():
    start=time.monotonic();previous=json.loads((OUT/'native_results.json').read_text());a0=previous['a0'];beta=3.0952
    with np.load(OUT/'inverse_nodes.npz',allow_pickle=False) as z: nodes={k:z[k].copy() for k in z.files}
    r=nodes['radii']; keys=['pr','dp','H','Hp']
    base=C2ModalFlow(beta,r,*[nodes[k+'_base'] for k in keys]);direction=C2ModalFlow(0.,r,*[nodes[k+'_dir'] for k in keys])
    def rebuilt(h):return C2ModalFlow(beta,r,*[nodes[k+'_base']+h*nodes[k+'_dir'] for k in keys])
    out={'started_utc':now(),'pid':os.getpid(),'priority':os.getpriority(os.PRIO_PROCESS,0),'status':'RUNNING',
      'beta':beta,'a0':a0,'cutoff':.001,'nodes_sha256':hashlib.sha256((OUT/'inverse_nodes.npz').read_bytes()).hexdigest(),
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'construction_comparisons':[],'sensitivity':[],'finite_differences':[]}
    def save():
        out['elapsed_seconds']=time.monotonic()-start;out['updated_utc']=now();p=OUT/'affine_diagnostics.json';tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p)
    points=np.array([[.2,.1],[.8,.4],[1.,1.],[.3,3.],[3.,1.]])
    checks=np.r_[points,[[rr*np.sin(ph),-rr*np.cos(ph)] for rr in np.geomspace(.0011,8.,31) for ph in [.31,1.1,2.51]]]
    for h in [1e-4,2e-4,1e-3,2e-3]:
        rp,rm=rebuilt(h),rebuilt(-h);ap,am=AffineFlow(base,direction,h),AffineFlow(base,direction,-h)
        rec={'step':h,'points':len(checks),'max_velocity_construction_difference':0.,'max_DW_construction_difference':0.,
             'max_velocity_parameter_derivative_error':0.,'max_DW_parameter_derivative_error':0.}
        for X in checks:
            rec['max_velocity_construction_difference']=max(rec['max_velocity_construction_difference'],float(max(abs(rp.W(X)-ap.W(X)))))
            rec['max_DW_construction_difference']=max(rec['max_DW_construction_difference'],float(np.max(abs(rp.DW(X)-ap.DW(X)))))
            rec['max_velocity_parameter_derivative_error']=max(rec['max_velocity_parameter_derivative_error'],float(max(abs((rp.W(X)-rm.W(X))/(2*h)-direction.W(X)))))
            rec['max_DW_parameter_derivative_error']=max(rec['max_DW_parameter_derivative_error'],float(np.max(abs((rp.DW(X)-rm.DW(X))/(2*h)-direction.DW(X)))))
        out['construction_comparisons'].append(rec);save();print(now(),'construction',rec,flush=True)
    for X in points[[2,3,4]]:
        for tol in [1e-13,3e-14]:
            row=reconstruct_sensitivity(base,direction,X,beta,a0,cutoff=.001,rtol=tol,atol=tol*.01)
            out['sensitivity'].append(row);save()
        for tol in [1e-12,1e-13]:
            for h in [2e-3,1e-3,2e-4,1e-4]:
                rows=[reconstruct(AffineFlow(base,direction,j*h),X,beta,a0,cutoff=.001,rtol=tol,atol=tol*.01,compatible_seed=True) for j in [-2,-1,1,2]]
                row={'point':X.tolist(),'step':h,'rtol':tol,'evaluations':rows}
                if all(z['status']=='COMPLETE' for z in rows):
                    vec=[np.r_[z['Theta'],z['gradient'],z['Omega']] for z in rows]
                    row.update(status='COMPLETE',derivative=((vec[0]-8*vec[1]+8*vec[2]-vec[3])/(12*h)).tolist())
                else:row['status']='FAILED'
                out['finite_differences'].append(row);save();print(now(),'FD',X.tolist(),h,tol,row['status'],'elapsed',out['elapsed_seconds'],flush=True)
    out.update(status='COMPLETE',ended_utc=now(),scope='Floating diagnostic on one prescribed finite-cutoff interpolated family. No continuum derivative, convergence certificate, fixed-point matrix or B2 endpoint.');save();print(now(),'COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':
    try:main()
    except Exception:
        (OUT/'affine_failure.txt').write_text(now()+'\n'+traceback.format_exc());raise
