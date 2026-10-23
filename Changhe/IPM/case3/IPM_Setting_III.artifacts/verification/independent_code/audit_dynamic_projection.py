"""Own canonical DR RHS and independently implemented nodal projection.
Read-only producer checkpoints. No producer modules are imported or executed.
"""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Fr
import hashlib,json,time
import numpy as np
from scipy.linalg import svd
from q_checkpoint_reader import QCheckpoint
from q_exact_jets import jets
from complementary_inverse_charts import ComplementaryQ,FullChart
from angular_log_inverse import AngularLogInverse

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(model,rad,theta,cw,cx,order,a,c):
    rad=np.asarray(rad);theta=np.asarray(theta);sn=np.sin(theta)[None,:];cs=np.cos(theta)[None,:]
    F=np.empty((len(rad),len(theta)));G=np.zeros_like(F)
    positive=rad>0; lr=np.log(np.maximum(rad,np.finfo(float).tiny))
    for defect in (True,False):
        ids=np.flatnonzero(positive&((lr<=model.log_core)==defect))
        if not len(ids):continue
        owner=model if defect else FullChart(model)
        z=AngularLogInverse(owner,order).fields(lr[ids],theta)
        rho_r=z['H']+owner.a*sn
        gg=cw*rho_r-(cx+z['ur'])*z['grad_radial']-z['ut']*z['grad_angular']
        _,_,w=model.stable_coordinates(lr[ids])
        F[ids]=gg/(w[:,None]*sn);G[ids]=rad[ids,None]*gg
    F[~positive]=a*(cw-cx-c)
    assert np.all(np.isfinite(F))
    return F,G

def evaluate(coeff,t,theta):
    s=(1+t)/2
    modes=np.array([s**k*np.polynomial.chebyshev.chebval(t,c) for k,c in enumerate(coeff)])
    return modes.T@np.cos(2*np.arange(len(coeff))[:,None]*theta)

def region_values(G,Gp,r,theta,Gstable=None):
    ans={}
    for name,lo,hi in [('core',0,1),('annulus',1,100),('far',100,float('inf')),('all',0,float('inf'))]:
        ids=np.flatnonzero((r>=lo)&(r<hi))
        if not len(ids):continue
        defect=Gp-G
        m=float(np.max(abs(G[ids])));p=float(np.max(abs(Gp[ids])));e=float(np.max(abs(defect[ids])))
        i,j=np.unravel_index(np.argmax(abs(defect[ids])),(len(ids),len(theta)));i=int(ids[i]);j=int(j)
        row={'canonical_rhs_sup':m,'projected_rhs_sup':p,'projection_defect_sup':e,'defect_over_rhs_sup':e/m if m else None,'defect_point':[float(r[i]*np.cos(theta[j])),float(r[i]*np.sin(theta[j]))],'radius':float(r[i]),'theta':float(theta[j]),'canonical_at_peak':float(G[i,j]),'projected_at_peak':float(Gp[i,j])}
        if Gstable is not None:row['coefficient_reconstruction_minus_stable_projection_sup']=float(np.max(abs((Gp-Gstable)[ids])))
        ans[name]=row
    return ans

def main():
    import torch
    torch.set_num_threads(1);torch.serialization.add_safe_globals([np._core.multiarray.scalar,np.dtype,type(np.dtype('float64')),type(np.dtype('float32'))])
    root=Path('research/dynamic_projection_audit');out=root/'verification';output=out/'AUDIT.json'
    gate=Path('research/q_full_inverse_primitives/verification/manufactured.json');assert json.loads(gate.read_text())['status']=='PASS'
    result={'started_utc':utc(),'status':'RUNNING','proof_sha256':sha(root/'PROOF.md'),'code_sha256':sha(__file__),'canonical_gate_sha256':sha(gate),'cases':[],'scope':'Canonical RHS passed through the mathematically specified projector. Producer actual F/u_tau are not imported, so this is not automatically its computed trajectory derivative. Grids only; no continuum instability or profile claim.'}
    def save():result['updated_utc']=utc();output.write_text(json.dumps(result,indent=2)+'\n')
    save()
    for N in (64,96,128):
      for at in ('0000','0020'):
        source=next(Path('../numerics/runs').glob(f'drA_C3_N{N}_tau{at}*.pt'));frozen=out/source.name;frozen.write_bytes(source.read_bytes())
        q=QCheckpoint(frozen);model=ComplementaryQ(frozen);st=torch.load(frozen,map_location='cpu',weights_only=True)
        a0c=jets(q.coeff,q.kappa,q.cl);a=float(a0c['a']);c=float(a0c['c']);cw=float(st['cw']);cx=float(st['cx']);J=3*q.M
        t=-np.cos(2*np.pi*np.arange(q.N+1)/(2*q.N+1));sigma=(1+t)/2;w=(1-t)/2;r=q.L*np.sqrt(sigma)/(1-t)**q.kappa
        th=(np.arange(J)+.5)*np.pi/(2*J);cos=np.cos(2*np.arange(q.M)[:,None]*th);normal=np.r_[1.,np.full(q.M-1,2.)]/J
        tm=(t[:-1]+t[1:])/2;thm=(th[:-1]+th[1:])/2;rm=q.L*np.sqrt((1+tm)/2)/(1-tm)**q.kappa;wm=(1-tm)/2
        weight=r[:,None]*w[:,None]*np.sin(th)[None,:];weightm=rm[:,None]*wm[:,None]*np.sin(thm)[None,:]
        mats=[];gates=[]
        for k in range(q.M):
            A=sigma[:,None]**k*np.polynomial.chebyshev.chebvander(t,q.N-k)
            U,S,Vh=svd(A,full_matrices=False,lapack_driver='gesvd');mats.append((A,U,S,Vh))
            assert np.max(abs(U.T@U-np.eye(len(S))))<3e-13
            gates.append({'k':k,'max_singular':float(S[0]),'min_singular':float(S[-1]),'counts_discarded':{str(rc):int(np.count_nonzero(S<=rc*S[0]))for rc in (1e-13,1e-10,1e-8)}})
        case={'source':str(source),'frozen':str(frozen),'sha256':sha(frozen),'N':q.N,'M':q.M,'tau':float(st['tau']),'cw':cw,'cx':cx,'canonical_c':c,'a':a,'center_F_exact':str(a0c['a']*(Fr(cw)-Fr(cx)-a0c['c'])),'projection_singular_values':gates,'rows':[]}
        result['cases'].append(case);previous=None;save()
        for order in (128,256):
            F,G=canonical(model,r,th,cw,cx,order,a,c);Fm,Gm=canonical(model,rm,thm,cw,cx,order,a,c)
            modes=(F@cos.T)*normal
            row={'inverse_order':order,'projections':[]};case['rows'].append(row)
            if previous is not None:
                row['inverse_order_G_difference_sup']=float(np.max(abs(G-previous[0])))
                row['inverse_order_between_G_difference_sup']=float(np.max(abs(Gm-previous[1])))
            previous=(G,Gm)
            for rc in ((1e-13,1e-10,1e-8) if N==64 else (1e-13,)):
                cc=[];stable=[];matvalues=[];symerr=0.;idemerr=0.
                for k,(A,U,S,Vh) in enumerate(mats):
                    keep=S>rc*S[0];u=U[:,keep];uF=u.T@modes[:,k]
                    co=Vh[keep,:].T@(uF/S[keep]);cc.append(co);stable.append(u@uF);matvalues.append(A@co)
                    P=u@u.T;symerr=max(symerr,float(np.max(abs(P-P.T))));idemerr=max(idemerr,float(np.max(abs(P@P-P))))
                assert idemerr<3e-13 and symerr<3e-13
                fp=evaluate(cc,t,th);fpm=evaluate(cc,tm,thm);stablep=np.array(stable).T@cos
                Gp=weight*fp;Gpm=weightm*fpm;Gs=weight*stablep
                path=out/f'{source.stem}_o{order}_rc{rc}.npz'
                np.savez_compressed(path,**{f'coefficient_k{k}':co for k,co in enumerate(cc)},t=t,theta=th,F=F,F_projected=fp,F_stable=stablep,t_between=tm,theta_between=thm,F_between=Fm,F_projected_between=fpm,cw=cw,cx=cx)
                c0=cc[0];a_tau=float(np.dot(c0,(-1.)**np.arange(len(c0))))
                pr={'rcond':rc,'artifact':str(path),'artifact_sha256':sha(path),'symmetry_gate_error':symerr,'idempotence_gate_error':idemerr,'max_coefficient_absolute':max(float(np.max(abs(z)))for z in cc),'projected_a_tau':a_tau,'nodes':region_values(G,Gp,r,th,Gs),'between':region_values(Gm,Gpm,rm,thm)}
                row['projections'].append(pr);save()
                print(json.dumps({'utc':utc(),'case':source.name,'order':order,'rcond':rc,'core':pr['nodes']['core'],'annulus':pr['nodes']['annulus'],'between_core':pr['between']['core'],'between_annulus':pr['between']['annulus']}),flush=True)
        case['status']='COMPUTED';save()
    result['status']='COMPUTED';result['finished_utc']=utc();save()
if __name__=='__main__':main()
