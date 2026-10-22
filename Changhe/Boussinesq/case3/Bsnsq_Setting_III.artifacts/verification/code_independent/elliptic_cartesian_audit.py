"""Independent E = dy V1 - dx V2 - Omega; never use a radial ODE for E.

Seven-point Cartesian differences of whole-plane quadrature velocities.
No numerics-lane modules, no GPU, no listener, no JavaScript.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,sys
import numpy as np
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from finite_difference import safe_ratio
from r2_state_values import R2State

OFFSETS=np.arange(-3,4,dtype=float)
WEIGHTS=np.array([-1,9,-45,0,45,-9,1],dtype=float)/60

def jacobian(velocity,points,steps):
    p=np.asarray(points,float).reshape(-1,2);h=np.broadcast_to(steps,(len(p),))
    ans=np.empty((len(p),2,2))
    for ax in range(2):
        q=np.repeat(p[:,None,:],7,axis=1);q[:,:,ax]+=h[:,None]*OFFSETS
        values=np.asarray(velocity(q.reshape(-1,2))).reshape(len(p),7,2)
        # component then differentiating coordinate
        ans[:,:,ax]=np.einsum('pjc,j->pc',values,WEIGHTS)/h[:,None]
    return ans

def residuals(jac,omega):
    e=jac[:,0,1]-jac[:,1,0]-omega
    n=np.abs(jac[:,0,1])+np.abs(jac[:,1,0])+np.abs(omega)
    d=jac[:,0,0]+jac[:,1,1]
    nd=np.abs(jac[:,0,0])+np.abs(jac[:,1,1])
    return {'E':e,'N_E':n,'ratio_E':safe_ratio(e,n),'div':d,'N_div':nd,'ratio_div':safe_ratio(d,nd)}

class Manufactured:
    def __init__(self,p=5/3,weights=None):
        self.p=float(p);self.weights=np.array([.7,-.4,0,.2,0,0,-.1] if weights is None else weights,float)
        self.count=len(self.weights);self.n=np.arange(1,self.count+1,dtype=float);self.a=(self.p-self.n)/2
    def radial_source(self,r):
        if r==0:return np.zeros(self.count)
        lr=np.log(r);lt=np.logaddexp(0.,2*lr)
        inv=np.exp(-lt);f=np.exp(2*lr-lt)
        # Cancellation-free large-radius power evaluation.
        base=np.exp(self.n*lr+(self.a-1)*lt)
        return -4*self.a*self.weights*base*((self.n+1)*inv+(self.n+self.a)*f)
    def radial_velocity(self,r):
        if r==0:return np.zeros(self.count),np.zeros(self.count)
        lr=np.log(r);lt=np.logaddexp(0.,2*lr);f=np.exp(2*lr-lt)
        pr=self.weights*np.exp((self.n-1)*lr+self.a*lt)
        dp=pr*(self.n+2*self.a*f)
        em=np.expm1(self.a[0]*lt)
        pr[0]=self.weights[0]*em
        dp[0]=self.weights[0]*(em+(1+em)*2*self.a[0]*f)
        return pr,dp
    def velocity(self,points):
        p=np.asarray(points,float).reshape(-1,2);out=np.zeros_like(p)
        for i,(x,y) in enumerate(p):
            r=float(np.hypot(x,y))
            if r==0:continue
            pr,dp=self.radial_velocity(r);phi=np.arctan2(x,-y)
            ur=-(self.n*pr)@np.cos(self.n*phi);ut=dp@np.sin(self.n*phi)
            out[i]=[ur*x/r-ut*y/r,ur*y/r+ut*x/r]
        return out
    def omega(self,points):
        p=np.asarray(points,float).reshape(-1,2);out=np.zeros(len(p))
        for i,(x,y) in enumerate(p):
            r=float(np.hypot(x,y))
            if r>0:out[i]=self.radial_source(r)@np.sin(self.n*np.arctan2(x,-y))
        return out

def summarize(values,points,mask=None):
    v=np.asarray(values);p=np.asarray(points)
    if mask is None:mask=np.ones(len(v),bool)
    ix=np.flatnonzero(mask);i=ix[np.argmax(np.abs(v[ix]))]
    return {'max_abs':float(abs(v[i])),'signed_value':float(v[i]),'point':p[i].tolist(),
            'count':len(ix),'zero_count':int((v[ix]==0).sum()),'infinite_count':int(np.isinf(v[ix]).sum())}

def knot_crossing(points,h,rknots):
    p=np.asarray(points);h=np.asarray(h);rr=[]
    for ax in range(2):
        q=np.repeat(p[:,None,:],7,axis=1);q[:,:,ax]+=h[:,None]*OFFSETS
        rr.append(np.hypot(q[:,:,0],q[:,:,1]))
    rr=np.concatenate(rr,axis=1);lo=rr.min(axis=1);hi=rr.max(axis=1)
    return ((lo[:,None]<rknots)&(hi[:,None]>rknots)).any(axis=1)

def run(root):
    root=Path(root);manifest=json.loads((root/'manifest.json').read_text());t0=time.monotonic()
    out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','states':[],
         'method':'7-point Cartesian finite differences of separately integrated relative full-plane velocity; E=dy V1-dx V2-Omega',
         'scope':'finite samples and floating quadrature estimates, not certified bounds; raw physical axis ratios retained and separately reported'}
    def save():
        out['elapsed_seconds']=time.monotonic()-t0;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    save()
    for item in manifest['states']:
        archive=root/item['snapshot'];assert hashlib.sha256(archive.read_bytes()).hexdigest()==item['sha256']
        s=R2State(archive);source=R2ModeSource(s)
        # Log grid plus exact knot radii and polynomial-cell midpoint radii.
        kt=s.edges[1:-1];rkn=s.L*np.sqrt(np.expm1(-2*s.bb*np.log1p(-kt)))
        kr=rkn[(rkn>=1e-4)&(rkn<=1e5)]
        kr=kr[np.linspace(0,len(kr)-1,min(5,len(kr)),dtype=int)]
        radii=np.unique(np.r_[np.geomspace(1e-5,1e7,25),kr])
        angles=np.array([0,np.pi/6,np.pi/3,np.pi/2,2*np.pi/3,5*np.pi/6,np.pi])
        x=np.sin(angles);y=-np.cos(angles);x[[0,-1]]=0;y[len(y)//2]=0
        points=(radii[:,None,None]*np.stack((x,y),axis=-1)[None,:,:]).reshape(-1,2)
        rad=np.repeat(radii,len(angles));axis=points[:,0]==0
        omega=s.omega(*points.T)
        state={'label':item['label'],'sha256':item['sha256'],'beta':s.beta,'bb':s.bb,'K':s.K,'Nt':s.Nt,
               'point_count':len(points),'r_min':float(rad.min()),'r_max':float(rad.max()),'runs':[]}
        out['states'].append(state);save();print('state',item['label'],len(points),flush=True)
        for tol in manifest.get('tolerances',[2e-10,2e-12]):
            inv=AdaptiveModalInverse(source,source.count,ModalSettings(decay=1/s.bb,epsabs=tol,epsrel=tol,limit=3000))
            tag=f'{item["label"]}_tol{tol:.0e}';raw={'points':points,'omega':omega,'axis':axis,'knot_radii':rkn}
            for eta in manifest.get('steps',[2e-4,1e-4,5e-5]):
                ts=time.monotonic();h=eta*np.maximum(1,rad);j=jacobian(inv.relative,points,h);res=residuals(j,omega)
                cross=knot_crossing(points,h,rkn);entry={'tolerance':tol,'eta':eta,'elapsed_seconds':time.monotonic()-ts,
                  'crossing_count':int(cross.sum()),'quadrature_radial_count':len(inv.cache)}
                for k,v in res.items():
                    entry[k]=summarize(v,points);entry[k+'_offaxis']=summarize(v,points,~axis)
                    raw[f'{eta:.0e}_{k}']=v
                raw[f'{eta:.0e}_jacobian']=j;raw[f'{eta:.0e}_crosses_knot']=cross
                entry['E_smooth_stencils']=summarize(res['E'],points,~cross)
                entry['E_knot_crossing_stencils']=summarize(res['E'],points,cross) if cross.any() else None
                state['runs'].append(entry);save();print(tag,eta,'max E',entry['E']['max_abs'],'time',entry['elapsed_seconds'],flush=True)
            rawpath=root/(tag+'.npz');np.savez_compressed(rawpath,**raw)
            (root/(tag+'_quadrature.json')).write_text(json.dumps(inv.evidence,indent=2)+'\n')
            state.setdefault('quadrature',[]).append({'tolerance':tol,'radial_calls':len(inv.evidence),
              'failed_inner':sum(not z['inner_success'] for z in inv.evidence),
              'failed_outer':sum(not z['outer_success'] for z in inv.evidence),
              'raw_file':rawpath.name})
            save()
    out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['elapsed_seconds'],flush=True)

if __name__=='__main__':run(sys.argv[1])
