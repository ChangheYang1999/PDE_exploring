"""Independent reconstruction of all5far nonlinear weights and switch records.

The formulas are read from the frozen production objective definition. This
module uses NumPy copies of the field terms and never calls nl_active_set.
"""
import hashlib
import numpy as np
import torch

def switch_record(prob,model,full,auxiliary):
    with torch.no_grad():ev=prob.evaluate(full,tables=auxiliary['tables'])
    F=ev['F'];U=F['U'].cpu().numpy();DU=F['GU'].cpu().numpy();y=model.y.permute(2,0,1).cpu().numpy();c=float(full[-2]);w=float(full[-1])
    def jj(a):return np.stack([-a[1],a[0],np.zeros_like(a[0])])
    terms=[(1-c)*U,c*np.einsum('mra,mira->ira',y,DU),w*(jj(U)-np.einsum('mra,mira->ira',jj(y),DU)),np.einsum('mra,mira->ira',U,DU),ev['gradP'].cpu().numpy()]
    sc=np.exp(((1-c)/c)/2*np.log1p((model.r.cpu().numpy()/model.R0)**2));aw=prob.w_ang.cpu().numpy();M=prob._shell_mean.cpu().numpy();occ=prob._shell_occupied.cpu().numpy()
    squares=np.stack([M@(((t*t).sum(0)*aw).sum(1)*sc*sc) for t in terms]);rms=np.sqrt(np.maximum(squares,1e-300));den=rms.sum(0);dn=rms[3]+rms[4];floor=max(1e-6*den.max(),1e-300);fn=max(1e-6*dn.max(),1e-300)
    raw=1/(den+floor)**2;far=np.asarray(prob.shell_edges)>=1;raw=np.where(far,(1/(den+floor)+prob.far_lambda/(dn+fn))**2,raw)
    order=np.lexsort((occ,raw[occ]));medidx=int(occ[order[(len(occ)-1)//2]]);med=raw[medidx];clamped=np.flatnonzero(raw>prob.nl_weight_cap*med)
    pred=np.minimum(raw,prob.nl_weight_cap*med)[prob.shell_id.cpu().numpy()];pred/=pred.mean();actual=auxiliary['nl_w'][0].cpu().numpy()
    sig={'median_shell':medidx,'median_ties':occ[raw[occ]==med].tolist(),'clamped_shells':clamped.tolist(),'den_max_shells':np.flatnonzero(den==den.max()).tolist(),'nonlinear_den_max_shells':np.flatnonzero(dn==dn.max()).tolist(),'rms_floor_slots':np.argwhere(squares<=1e-300).tolist(),'den_absolute_floor_active':bool(1e-6*den.max()<=1e-300),'nonlinear_absolute_floor_active':bool(1e-6*dn.max()<=1e-300),'geometry_sha256':hashlib.sha256(prob.pressure._quad['s'].tobytes()+prob.pressure._quad['w'].tobytes()).hexdigest(),'geometry_covered':bool(prob.pressure.geometry_ok(c,w)),'open_domain':bool(.4<c<.5 and w>0),'phase_pivot':prob.pivot}
    return sig,float(np.linalg.norm(pred-actual)/max(np.linalg.norm(actual),1e-300))
