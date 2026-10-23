"""Check the NumPy decoder against a separate Torch potential implementation."""
import json
import numpy as np
import torch
from checkpoint import PotentialMLP,forward_selfcheck,load
from evaluate import atomic_json,ROOT,utc
from core import stats

def main():
    torch.set_num_threads(1);torch.set_num_interop_threads(1)
    rng=np.random.default_rng(241509);results=[]
    cases=[(False,1,False),(True,1,False),('dir_log',1,False),('asinh',1,False),('both',1,False),('dir_tau',1,False),('dir_tau',2,False),('both',2,False),('dir_tau',2,True)]
    for branch,n_tail,use_blobs in cases:
        radial=branch is not False
        cfg=dict(cl=.45,cl_trainable=True,cl_bounds=[.4,.5],C=.13,
                 model=dict(width=8,depth=2,radial_feature=radial,radial_feature_kind='log1p',n_tail=n_tail,
                            l_in=1.3,l_env=1.7,xi_scale=2.2,out_scale=.7,a_env_shift=.12,p_env_shift=-.08),seed=dict(use=True))
        if isinstance(branch,str):cfg['model']['feature_set']=branch
        state=dict(cl_theta=np.array(-.3),seed_abc=np.array([.2,-.4,.7]))
        if branch!='dir_tau':state['seed_scale']=np.array(1.3)
        if use_blobs:
            cfg['blobs']=dict(trainable=True,list=[
                dict(y0=[.7,-.2,.3],m=[-.4,.6,.1],sigma=.8),
                dict(y0=[-.1,.9,-.5],m=[.3,.2,-.8],sigma=.55)])
            # Saved trainable values deliberately differ from their initial config.
            state['blob_centers']=np.array([[.8,-.3,.4],[-.2,.7,-.6]])
            state['blob_moments']=np.array([[-.5,.65,.2],[.2,.3,-.7]])
            state['blob_logsig']=np.log(np.array([.73,.61]))
        for net,out in [('netA',3*n_tail),('netP',n_tail)]:
            dims=[7 if branch=='both' else (4 if radial else 3),8,8,out]
            for k,(a,b) in enumerate(zip(dims,dims[1:])):
                state[f'{net}.lins.{k}.weight']=rng.normal(size=(b,a))*.3
                state[f'{net}.lins.{k}.bias']=rng.normal(size=b)*.1
        model=PotentialMLP(cfg,state)
        x=rng.uniform(-2,2,(72,3));x=np.concatenate([x,np.zeros((1,3)),np.array([[0.,0.,.7]])])
        y=torch.tensor(x,dtype=torch.float64,requires_grad=True);qt=torch.tensor([-1.,-1.,1.],dtype=torch.float64)
        def raw(y,prefix):
            r2=(y*y).sum(-1,keepdim=True)
            if branch=='dir_tau':
                xi=y/torch.sqrt(1.3**2+r2);f=torch.cat([xi,(xi*xi).sum(-1,keepdim=True)],dim=1)
            elif isinstance(branch,str):
                parts=[]
                if branch in ('dir_log','both'):parts.append(y/torch.sqrt(1.3**2+r2))
                if branch in ('asinh','both'):parts.append(torch.asinh(y/1.3)/2.2)
                parts.append(torch.log1p(r2/1.3**2)/2.2);f=torch.cat(parts,dim=1)
            else:
                f=torch.asinh(y/1.3)/2.2
                if radial:f=torch.cat([f,.5*torch.log1p(r2/1.3**2)/2.2],dim=1)
            for k in range(3):
                W=torch.tensor(state[f'{prefix}.lins.{k}.weight'],dtype=torch.float64)
                b=torch.tensor(state[f'{prefix}.lins.{k}.bias'],dtype=torch.float64)
                f=f@W.T+b
                if k<2:f=torch.tanh(f)
            return f*.7
        c=.4+.1*torch.sigmoid(torch.tensor(-.3,dtype=torch.float64));d=1-1/c
        s=(y*y).sum(-1);base=1+s/1.7**2
        Ay=raw(y,'netA').reshape(len(y),n_tail,3);Aqy=raw(y*qt,'netA').reshape(len(y),n_tail,3)
        Py=raw(y,'netP');Pqy=raw(y*qt,'netP')
        A=torch.zeros_like(y);P=torch.zeros_like(s)
        for k in range(n_tail):
            A=A+.5*(Ay[:,k]+Aqy[:,k]*qt)*base[:,None]**(.5*(d+1+k*(d-1)+.12))
            P=P+.5*(Py[:,k]+Pqy[:,k])*base**(d+.5*k*(d-1)-.04)
        a,b,cm=state['seed_abc'];scale=float(state.get('seed_scale',1.))
        M=torch.tensor(scale*np.array([[a,b,0],[cm,-1-a,0],[0,0,1]]),dtype=torch.float64)
        chi=(1+s)**(-1/(2*c));A=A-chi[:,None]*torch.cross(y,y@M.T,dim=-1)/3
        P=P-.5*chi**2*(y*(y@(M+M@M).T)).sum(-1)
        if use_blobs:
            for center,moment,logsig in zip(state['blob_centers'],state['blob_moments'],state['blob_logsig']):
                center=torch.tensor(center,dtype=torch.float64);moment=torch.tensor(moment,dtype=torch.float64)
                sigma=torch.exp(torch.tensor(logsig,dtype=torch.float64))
                for transform in (torch.ones(3,dtype=torch.float64),qt):
                    delta=y-center*transform
                    A=A+torch.exp(-(delta**2).sum(-1)/(2*sigma**2))[:,None]*moment*transform
        JA=torch.stack([torch.autograd.grad(A[:,k].sum(),y,retain_graph=True)[0] for k in range(3)],dim=1)
        U=torch.stack([JA[:,2,1]-JA[:,1,2],JA[:,0,2]-JA[:,2,0],JA[:,1,0]-JA[:,0,1]],dim=1)
        expected=torch.cat([U,P[:,None]],dim=1).detach().numpy();computed=model(x)
        direct_error=stats(computed-expected);tangent=forward_selfcheck(model)
        dest=ROOT/'evidence'/f'synthetic_decoder_{branch}_tail{n_tail}_blobs{int(use_blobs)}.npz'
        np.savez(dest,**state,config_json=np.array(json.dumps(cfg)),metadata_json=np.array(json.dumps(dict(kind='synthetic decoder test; never a candidate'))))
        loaded=load(dest);reload_error=stats(loaded(x)-computed)
        results.append(dict(branch=branch,n_tail=n_tail,use_blobs=use_blobs,numpy_vs_independent_torch=direct_error,tangent_check=tangent,
                            npz_reload_error=reload_error,passed=direct_error['sampled_max']<2e-12 and tangent['passed'] and reload_error['sampled_max']==0.))
    try:
        PotentialMLP(cfg,{**state,'undocumented_extra_field':np.array(1.)})
    except ValueError as error:
        unknown_field_rejected='Undocumented saved state keys' in str(error)
    else:
        unknown_field_rejected=False
    result=dict(created_utc=utc(),tests=results,unknown_field_rejected=unknown_field_rejected,
                passed=all(r['passed'] for r in results) and unknown_field_rejected,torch_version=torch.__version__,
                scope='Synthetic nonzero weights, independent seed matrix, potential autograd versus hand tangents, no trainer modules imported.')
    atomic_json(ROOT/'evidence/checkpoint_decoder_tests.json',result)
    for row in results:print(row['branch'],row['n_tail'],row['passed'],row['numpy_vs_independent_torch']['sampled_max'])
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
