from pathlib import Path
from datetime import datetime,timezone
import json,sys,hashlib,shutil
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebvander,chebder
import torch
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity

def coeff(nodes):
    out=dct(nodes[::-1],type=1,axis=0)/(nodes.shape[0]-1);out[[0,-1]]*=.5
    out=dct(out,type=2,axis=1)/nodes.shape[1];out[:,0]*=.5
    return out

def evalco(co,r,t,d,c=None):
    c=d.cl if c is None else c
    q=-np.expm1(-.5*(1-1/c)*np.log1p(r*r/d.L**2))
    R=chebvander(2*q-1,co.shape[0]-1)
    T=np.cos(2*np.arange(d.M)[:,None]*d.map_inverse(t)[None,:])
    return np.einsum('rn,nmk,mt->rtk',R,co,T,optimize=True)

def fields(d,V,r,t):
    nodes=np.zeros((d.N+1,d.M,V.shape[1]));nodes[1:]=V[:-2].reshape(d.N,d.M,-1)
    dc=coeff(nodes);rat=coeff(nodes/d.b[:,:,None]);b=evalco(d.co[:,:,None],r,t,d)[:,:,0]
    db=evalco(dc,r,t,d);bq=evalco(2*chebder(d.co,axis=0)[:,:,None],r,t,d)[:,:,0]
    ell=np.log1p(r*r/d.L**2);q=-np.expm1(-.5*(1-d.k)*ell)
    quotient=db/b[:,:,None]
    physical=quotient-ell[:,None,None]*V[-2][None,None,:]/(2*d.cl**2)*(1-(1-q)[:,None,None]*bq[:,:,None]/b[:,:,None])
    return {'nodal_ratio_interpolant':evalco(rat,r,t,d),'pointwise_b_ratio':quotient,'physical_density_ratio':physical},float(np.min(abs(b))),dc

def compare(a,b,w):
    A=a.reshape(-1,a.shape[-1])*np.sqrt(w).reshape(-1,1);B=b.reshape(-1,b.shape[-1])*np.sqrt(w).reshape(-1,1)
    na=np.linalg.norm(A,axis=0);nb=np.linalg.norm(B,axis=0)
    Qa,Ra=np.linalg.qr(A,mode='reduced');Qb,Rb=np.linalg.qr(B,mode='reduced')
    return {'by_index_abs_overlap':np.abs(np.sum(A*B,axis=0)/(na*nb)).tolist(),'span_principal_cosines':np.linalg.svd(Qa.T@Qb,compute_uv=False).tolist(),'gram_condition':[(np.linalg.cond(Ra))**2,(np.linalg.cond(Rb))**2],'weighted_column_norms':[na.tolist(),nb.tolist()],'ranks':[int(np.linalg.matrix_rank(Ra)),int(np.linalg.matrix_rank(Rb))]}

sources=[('n96','numerics/runs/dnB_n96m40S.npz','numerics/runs/n96m40S_final_softvecs_node_cl400.pt'),('n120','numerics/data/dnSB_n120m48.npz','numerics/runs/n120m48_S_softvecs_node_cl400.pt')]
states=[];meta=[]
for tag,p,vp in sources:
    shutil.copyfile(p,root/'data'/(tag+'.npz'));shutil.copyfile(vp,root/'data'/(tag+'_directions.pt'))
    d=NodalDensity(root/'data'/(tag+'.npz'));z=torch.load(vp,map_location='cpu',weights_only=True);V=z['Vsoft_unscaled'][:,:6].numpy()
    states.append((d,V));meta.append({'tag':tag,'state_source':p,'state_md5':d.md5,'directions_source':vp,'directions_md5':hashlib.md5(Path(vp).read_bytes()).hexdigest(),'dcl':V[-2].tolist(),'dC':V[-1].tolist(),'coordinate_norms':np.linalg.norm(V,axis=0).tolist()})
out={'date':datetime.now(timezone.utc).isoformat(),'metadata':meta,'samples':[],'finite_parameter_checks':[]}
for nr,nt in [(160,72),(320,144)]:
    r=np.geomspace(.02,2e4,nr);t=(np.arange(nt)+.5)*np.pi/(2*nt);w=np.broadcast_to((r*np.gradient(r))[:,None]*np.pi/(2*nt),(nr,nt))
    fs=[];minimum=[]
    for d,V in states:
        f,mb,dc=fields(d,V,r,t);fs.append(f);minimum.append(mb)
    for label,mask in [('r_lt_200',r<200),('all',r>0)]:
        row={'nr':nr,'nt':nt,'window':label,'r_min':float(r[mask].min()),'r_max':float(r[mask].max()),'minimum_abs_b':minimum,'metrics':{}}
        for key in fs[0]:row['metrics'][key]=compare(fs[0][key][mask],fs[1][key][mask],w[mask])
        out['samples'].append(row);print(json.dumps(row),flush=True)
for (d,V),m in zip(states,meta):
    r=np.array([.3,10.,1e3]);t=np.array([.2,1.,1.5]);f,_,dc=fields(d,V,r,t)
    for h in [1e-4,3e-5,1e-5]:
        base=evalco(d.co[:,:,None],r,t,d)[:,:,0];ell=np.log1p(r*r/d.L**2)
        fd=[]
        for j in range(V.shape[1]):
            vals=[]
            for sign in [-1,1]:
                c=d.cl+sign*h*V[-2,j];bc=d.co+sign*h*dc[:,:,j]
                vals.append(evalco(bc[:,:,None],r,t,d,c)[:,:,0]/base*np.exp(.5*(1/c-d.k)*ell[:,None]))
            fd.append((vals[1]-vals[0])/(2*h))
        fd=np.stack(fd,axis=-1);analytic=f['physical_density_ratio'];err=abs(fd-analytic)
        row={'tag':m['tag'],'h':h,'max_absolute_error':float(err.max()),'max_relative_error_with_unit_floor':float((err/np.maximum(1.,abs(analytic))).max())};out['finite_parameter_checks'].append(row);print(json.dumps(row),flush=True)
(root/'verification/summary.json').write_text(json.dumps(out,indent=2)+'\n')
