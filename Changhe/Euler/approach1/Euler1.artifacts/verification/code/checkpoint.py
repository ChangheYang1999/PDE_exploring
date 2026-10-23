"""Independent forward reconstruction of the documented potential/pressure MLP.

Only saved data are loaded from the numerics lane. No numerics module is imported.
First derivatives of A use explicitly propagated tangents; residual derivatives
are taken by the independent finite-difference code in core.py.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path
import numpy as np
from core import Q,curl,sha256,differentiate,stats
from evaluate import evaluate,atomic_json,ROOT


def as_numpy(x):
    if hasattr(x,'detach'):
        return x.detach().cpu().numpy().astype(np.float64)
    return np.asarray(x,dtype=np.float64)


def metadata_for_json(value):
    """Preserve nonfinite diagnostic metadata explicitly without invalid JSON."""
    if isinstance(value,dict):return {str(k):metadata_for_json(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [metadata_for_json(v) for v in value]
    if isinstance(value,(float,np.floating)) and not np.isfinite(value):
        return {"nonfinite_saved_metadata":str(value)}
    return value


class PotentialMLP:
    def __init__(self,cfg,state,radial_kind=None):
        self.cfg=cfg
        self.original_dtypes={k:str(v.dtype) for k,v in state.items() if hasattr(v,'dtype')}
        self.state={k:as_numpy(v) for k,v in state.items()}
        self.fp64_state=all(v in ('float64','torch.float64') for v in self.original_dtypes.values())
        self.m=cfg['model'];scfg=cfg.get('seed',{})
        if cfg.get('cl_trainable',False):
            lo,hi=cfg.get('cl_bounds',[.4,.5]);t=float(self.state['cl_theta'])
            logistic=(1/(1+np.exp(-t))) if t>=0 else np.exp(t)/(1+np.exp(t))
            self.c_l=float(lo+(hi-lo)*logistic)
        else:
            self.c_l=float(self.state['cl_fixed'])
        self.C=float(cfg.get('C',0.))
        self.l_in=float(self.m.get('l_in',1.));self.xi_scale=float(self.m.get('xi_scale',3.))
        self.l_env=float(self.m.get('l_env',1.));self.out_scale=float(self.m.get('out_scale',1.))
        self.feature_set=self.m.get('feature_set')
        if self.feature_set is not None and self.feature_set not in ['dir_tau','dir_log','asinh','both']:
            raise ValueError('Unsupported feature_set '+str(self.feature_set))
        self.radial=bool(self.m.get('radial_feature',True)) if self.feature_set is None else True
        self.radial_kind=('bounded_tau' if self.feature_set=='dir_tau' else 'log1p_full' if self.feature_set else radial_kind or self.m.get('radial_feature_kind'))
        if self.radial and self.radial_kind not in ['legacy_sqrt','log1p','log1p_full','bounded_tau']:
            raise ValueError('Radial feature formula must be identified explicitly: legacy_sqrt or log1p. Refusing an undocumented architecture guess.')
        self.use_seed=bool(scfg.get('use',True))
        abc=self.state['seed_abc'];scale=float(self.state.get('seed_scale',1.))
        self.M=scale*np.array([[abc[0],abc[1],0.],[abc[2],-1-abc[0],0.],[0.,0.,1.]])
        self.S=self.M+self.M@self.M
        self.netA=self.layers('netA');self.netP=self.layers('netP')
        self.n_tail=int(self.m.get('n_tail',2 if self.feature_set=='dir_tau' else 1))
        if self.n_tail<1 or self.netA[-1][0].shape[0]!=3*self.n_tail or self.netP[-1][0].shape[0]!=self.n_tail:
            raise ValueError('Tail term count and saved output widths disagree')
        feature_count=(7 if self.feature_set=='both' else 4) if self.feature_set else (4 if self.radial else 3)
        if self.netA[0][0].shape[1]!=feature_count or self.netP[0][0].shape[1]!=feature_count:
            raise ValueError('Feature metadata and network input widths disagree')
        blobs=cfg.get('blobs') or {}
        self.use_blobs=bool(blobs.get('list',[]))
        self.blob_centers=np.empty((0,3));self.blob_moments=np.empty((0,3));self.blob_sigmas=np.empty(0)
        known={'cl_fixed','cl_theta','seed_abc','seed_scale'}
        for prefix,layers in [('netA',self.netA),('netP',self.netP)]:
            for i in range(len(layers)):
                known.update([f'{prefix}.lins.{i}.weight',f'{prefix}.lins.{i}.bias'])
        if self.use_blobs:
            known.update(['blob_centers','blob_moments','blob_logsig'])
            self.blob_centers=self.state['blob_centers'];self.blob_moments=self.state['blob_moments']
            self.blob_sigmas=np.exp(self.state['blob_logsig'])
            count=len(blobs['list'])
            if self.blob_centers.shape!=(count,3) or self.blob_moments.shape!=(count,3) or self.blob_sigmas.shape!=(count,):
                raise ValueError('Blob metadata and saved array dimensions disagree')
            if not np.all(np.isfinite(self.blob_sigmas)) or np.any(self.blob_sigmas<=0):
                raise ValueError('Blob widths must be finite and positive')
        unknown=set(self.state)-known
        if unknown:
            raise ValueError('Undocumented saved state keys; refusing to omit fields: '+str(sorted(unknown)))
        if any(not np.all(np.isfinite(value)) for value in self.state.values()):
            raise ValueError('Nonfinite saved model state')
        self.metadata=dict(kind='saved potential/pressure MLP',c_l=self.c_l,C=self.C,config=cfg,
                           feature_set=self.feature_set,n_tail=self.n_tail,use_blobs=self.use_blobs,
                           blob_count=len(self.blob_sigmas),fp64_state=self.fp64_state,original_dtypes=self.original_dtypes,radial_feature_kind=self.radial_kind,derivative_method='hand-propagated potential tangents and physical finite differences')
    def layers(self,prefix):
        layers=[]
        index=0
        while f'{prefix}.lins.{index}.weight' in self.state:
            W=self.state[f'{prefix}.lins.{index}.weight'];b=self.state[f'{prefix}.lins.{index}.bias']
            if W.ndim!=2 or b.shape!=(W.shape[0],):
                raise ValueError('Invalid linear-layer shapes')
            if layers and W.shape[1]!=layers[-1][0].shape[0]:
                raise ValueError('Mismatched layer shapes')
            layers.append((W,b));index+=1
        if not layers:
            raise ValueError('Missing network '+prefix)
        return layers
    def features(self,y):
        N=len(y)
        if self.feature_set:
            s=np.sum(y*y,axis=1);base=self.l_in**2+s
            values=[];derivatives=[]
            if self.feature_set in ('dir_tau','dir_log','both'):
                root=np.sqrt(base)
                values.append(y/root[:,None])
                derivatives.append(np.eye(3)[None,:,:]/root[:,None,None]-y[:,:,None]*y[:,None,:]/root[:,None,None]**3)
            if self.feature_set in ('asinh','both'):
                values.append(np.arcsinh(y/self.l_in)/self.xi_scale)
                D=np.zeros((N,3,3));D[:,np.arange(3),np.arange(3)]=1/(self.xi_scale*np.sqrt(self.l_in**2+y*y))
                derivatives.append(D)
            if self.feature_set=='dir_tau':
                values.append((s/base)[:,None])
                derivatives.append((2*self.l_in**2*y/base[:,None]**2)[:,None,:])
            else:
                values.append(np.log1p(s/self.l_in**2)[:,None]/self.xi_scale)
                derivatives.append((2*y/(self.xi_scale*base)[:,None])[:,None,:])
            return np.concatenate(values,axis=1),np.concatenate(derivatives,axis=1)
        xi=np.arcsinh(y/self.l_in)/self.xi_scale
        D=np.zeros((N,3,3))
        D[:,np.arange(3),np.arange(3)]=1/(self.xi_scale*np.sqrt(self.l_in**2+y*y))
        if self.radial:
            s=np.sum(y*y,axis=1)
            if self.radial_kind in ('log1p','log1p_full'):
                factor=.5 if self.radial_kind=='log1p' else 1.
                radius=factor*np.log1p(s/self.l_in**2)/self.xi_scale
                grad=2*factor*y/(self.xi_scale*(self.l_in**2+s))[:,None]
            else:
                R=np.sqrt(s+1e-300)
                radius=np.arcsinh(R/self.l_in)/self.xi_scale
                grad=y/(self.xi_scale*R*np.sqrt(self.l_in**2+R*R))[:,None]
            xi=np.column_stack([xi,radius]);D=np.concatenate([D,grad[:,None,:]],axis=1)
        return xi,D
    def mlp(self,inputs,layers,tangents=None):
        value=inputs
        tangent=tangents
        N=len(value)
        for index,(W,b) in enumerate(layers):
            value=value@W.T+b
            if tangent is not None:
                tangent=(tangent.transpose(0,2,1).reshape(-1,W.shape[1])@W.T).reshape(N,3,W.shape[0]).transpose(0,2,1)
            if index<len(layers)-1:
                value=np.tanh(value)
                if tangent is not None:
                    tangent*=1-value[:,:,None]**2
        return value*self.out_scale,(tangent*self.out_scale if tangent is not None else None)
    def fields_and_potential_gradient(self,y):
        x,D=self.features(y);qx,qD=self.features(y*Q)
        A,DA=self.mlp(x,self.netA,D);Aq,DAq=self.mlp(qx,self.netA,qD)
        P,_=self.mlp(x,self.netP);Pq,_=self.mlp(qx,self.netP)
        N=len(y);K=self.n_tail
        A=A.reshape(N,K,3);Aq=Aq.reshape(N,K,3)
        DA=DA.reshape(N,K,3,3);DAq=DAq.reshape(N,K,3,3)
        A=.5*(A+Aq*Q)
        DA=.5*(DA+DAq*Q[None,None,:,None]*Q[None,None,None,:])
        P=.5*(P+Pq)
        d=1-1/self.c_l;s=np.sum(y*y,axis=1);k=np.arange(K)
        pA=.5*(d+1+k*(d-1)+float(self.m.get('a_env_shift',0.)))
        pP=d+.5*k*(d-1)+.5*float(self.m.get('p_env_shift',0.))
        base=1+s/self.l_env**2;envA=base[:,None]**pA;envP=base[:,None]**pP
        grad_envA=2*pA[None,:,None]*envA[:,:,None]*y[:,None,:]/(self.l_env**2+s)[:,None,None]
        J=np.sum(envA[:,:,None,None]*DA+A[:,:,:,None]*grad_envA[:,:,None,:],axis=1)
        return np.sum(envA[:,:,None]*A,axis=1),np.sum(envP*P,axis=1),J
    def potential_pressure(self,y):
        y=np.asarray(y,dtype=np.float64)
        A,P,_=self.fields_and_potential_gradient(y)
        if self.use_blobs:
            Ab,_=self.blob_fields(y);A+=Ab
        if self.use_seed:
            s=np.sum(y*y,axis=1);chi=(1+s)**(-1/(2*self.c_l))
            A-=chi[:,None]*np.cross(y,y@self.M.T)/3
            P-=.5*chi**2*np.einsum('ni,ij,nj->n',y,self.S,y)
        return np.column_stack([A,P])
    def __call__(self,y):
        y=np.asarray(y,dtype=np.float64)
        _,P,J=self.fields_and_potential_gradient(y)
        U=curl(J)
        if self.use_blobs:
            _,Ub=self.blob_fields(y);U+=Ub
        if self.use_seed:
            s=np.sum(y*y,axis=1);chi=(1+s)**(-1/(2*self.c_l));My=y@self.M.T;q=np.sum(y*My,axis=1)
            U+=chi[:,None]*((1-s/(3*self.c_l*(1+s)))[:,None]*My+(q/(3*self.c_l*(1+s)))[:,None]*y)
            P-=.5*chi**2*np.einsum('ni,ij,nj->n',y,self.S,y)
        return np.column_stack([U,P])

    def blob_fields(self,y):
        """Explicit Gaussian potential and curl, independent of trainer AD."""
        A=np.zeros_like(y);U=np.zeros_like(y)
        for center,moment,sigma in zip(self.blob_centers,self.blob_moments,self.blob_sigmas):
            for q in (np.ones(3),Q):
                displacement=y-center*q
                gaussian=np.exp(-np.sum(displacement**2,axis=1)/(2*sigma**2))
                A+=gaussian[:,None]*(moment*q)
                U-=gaussian[:,None]*np.cross(displacement,moment*q)/sigma**2
        return A,U


def load(path,radial_kind=None):
    path=Path(path)
    saved_bytes=path.read_bytes()
    input_hash=hashlib.sha256(saved_bytes).hexdigest()
    if path.suffix=='.npz':
        with np.load(io.BytesIO(saved_bytes),allow_pickle=False) as data:
            state={k:data[k] for k in data.files if k not in ['config_json','metadata_json']}
            cfg=json.loads(str(data['config_json']))
            meta=json.loads(str(data['metadata_json'])) if 'metadata_json' in data.files else {}
    else:
        import torch
        torch.set_num_threads(1)
        # Local colleague-produced checkpoint data are trusted. No trainer modules are imported.
        saved=torch.load(io.BytesIO(saved_bytes),map_location='cpu',weights_only=False)
        cfg=saved.get('cfg',saved.get('config'))
        state=saved.get('model_state',saved.get('model_state_dict',saved.get('model')))
        if cfg is None or state is None:
            raise ValueError('Checkpoint requires cfg/config and model_state/model_state_dict/model')
        meta={k:v for k,v in saved.items() if k in ['step','epoch','experiment_id','exp_id','metrics','active_seconds','state','val','saved']}
    model=PotentialMLP(cfg,state,radial_kind)
    model.metadata.update(checkpoint_path=str(path),checkpoint_sha256=input_hash,checkpoint_metadata=metadata_for_json(meta))
    return model


def forward_selfcheck(model):
    rng=np.random.default_rng(25129)
    points=rng.uniform(-1.5,1.5,(64,3))
    points=np.concatenate([points,np.zeros((1,3))])
    _,J,_=differentiate(model.potential_pressure,points,step=.001,order=6,hessian=False)
    diff=model(points)[:,:3]-curl(J[:,:3])
    return dict(velocity_vs_finite_difference_potential_curl=stats(diff),sample_count=len(points),
                passed=bool(np.max(abs(diff))<1e-7),
                scope='Checks handwritten tangents against finite differences; trainer forward-reference comparison remains separate.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('checkpoint',type=Path)
    parser.add_argument('--radial-kind',choices=['legacy_sqrt','log1p'])
    parser.add_argument('--n',type=int,default=512)
    parser.add_argument('--holdout-seed',type=int,default=736291)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--selfcheck-only',action='store_true')
    args=parser.parse_args()
    model=load(args.checkpoint,args.radial_kind)
    check=forward_selfcheck(model)
    if args.selfcheck_only:
        result=dict(model_metadata=model.metadata,forward_selfcheck=check)
    else:
        if not check['passed']:
            raise RuntimeError('Independent forward tangent check failed: '+json.dumps(check))
        experiment='checkpoint-'+model.metadata['checkpoint_sha256'][:16]
        result=evaluate(model,experiment,args.n,args.holdout_seed,model.metadata['checkpoint_sha256'])
        result['forward_selfcheck']=check
        if not model.fp64_state:
            result['assessment']['status']='NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH'
            result['assessment']['reasons'].append('checkpoint contains non-FP64 state; see original_dtypes')
        if model.radial and model.radial_kind=='legacy_sqrt':
            result['assessment']['status']='NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH'
            result['assessment']['reasons'].append('unresolved radial sqrt regularization scale at origin')
    dest=args.output or ROOT/'evidence'/('checkpoint-'+model.metadata['checkpoint_sha256'][:16]+'.json')
    atomic_json(dest,result)
    print(json.dumps(dict(output=str(dest),selfcheck=check,assessment=result.get('assessment')),indent=2))

if __name__=='__main__':
    main()
