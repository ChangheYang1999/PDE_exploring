"""Finite weighted-residual derivative; see discrete_coefficient_derivative/PROOF.md."""
import numpy as np

def jj(a):return np.stack((-a[...,1],a[...,0],np.zeros_like(a[...,0])),axis=-1)
def multiply(du,u):return np.einsum('raij,raj->rai',du,u)

def weights_and_derivative(terms,tangents,geometry,c,r0,dtype=np.longdouble):
    D=dtype;r=np.asarray(geometry['radii'],dtype=D);aw=np.asarray(geometry['angular_mean_weights'],dtype=D)
    M=np.asarray(geometry['shell_mean'],dtype=D);sid=geometry['shell_id'];occ=geometry['occupied_shells']
    sc=np.exp(((D(1)-D(c))/D(c))/2*np.log1p((r/D(r0))**2))
    def quadratic(a):return M@(np.sum(np.sum(a*a,axis=-1)*aw[None,:],axis=1)*sc**2)
    squares=np.stack([quadratic(t) for t in terms]);active=squares>D('1e-300');rms=np.sqrt(np.maximum(squares,D('1e-300')))
    den=np.sum(rms,axis=0);dn=rms[3]+rms[4]
    mi=int(np.argmax(den));ni=int(np.argmax(dn));floor=max(D('1e-6')*den[mi],D('1e-300'));fn=max(D('1e-6')*dn[ni],D('1e-300'))
    far=np.asarray(geometry['shell_edges'])>=1
    v=1/(den+floor)+np.where(far,D('.01')/(dn+fn),D(0));raw=v*v
    medidx=int(occ[np.lexsort((occ,raw[occ]))[(len(occ)-1)//2]]);cap=D(1000)*raw[medidx];clamped=raw>cap
    capped=np.minimum(raw,cap);per=capped[sid];mean=np.mean(per);nw=per/mean
    sig={'median_shell':medidx,'median_ties':occ[raw[occ]==raw[medidx]].tolist(),'clamped_shells':np.flatnonzero(clamped).tolist(),'den_max_shells':np.flatnonzero(den==den[mi]).tolist(),'nonlinear_den_max_shells':np.flatnonzero(dn==dn[ni]).tolist(),'rms_floor_slots':np.argwhere(~active).tolist(),'den_absolute_floor_active':bool(D('1e-6')*den[mi]<=D('1e-300')),'nonlinear_absolute_floor_active':bool(D('1e-6')*dn[ni]<=D('1e-300'))}
    tangent=None
    if tangents is not None:
        qp=np.stack([2*M@(np.sum(np.sum(t*dt,axis=-1)*aw[None,:],axis=1)*sc**2) for t,dt in zip(terms,tangents)])
        rp=np.where(active,qp/(2*rms),D(0));dp=np.sum(rp,axis=0);dnp=rp[3]+rp[4]
        fp=D(0) if sig['den_absolute_floor_active'] else D('1e-6')*dp[mi]
        fnp=D(0) if sig['nonlinear_absolute_floor_active'] else D('1e-6')*dnp[ni]
        vp=-(dp+fp)/(den+floor)**2-np.where(far,D('.01')*(dnp+fnp)/(dn+fn)**2,D(0))
        rawp=2*v*vp;cappedp=np.where(clamped,D(1000)*rawp[medidx],rawp);perp=cappedp[sid]
        tangent=perp/mean-nw*np.mean(perp)/mean
    rowfactor=np.sqrt(np.asarray(geometry['node_weights'],dtype=D)[:,None]*aw[None,:])*sc[:,None]*np.sqrt(nw[:,None])
    return nw,tangent,rowfactor,sig

def terms(u,du,gp,c,w,y):
    return [(1-c)*u,c*multiply(du,y),w*(jj(u)-multiply(du,jj(y))),multiply(du,u),gp]

def term_tangents(u,du,v,dv,gpv,c,w,y):
    return [(1-c)*v,c*multiply(dv,y),w*(jj(v)-multiply(dv,jj(y))),multiply(dv,u)+multiply(du,v),gpv]
