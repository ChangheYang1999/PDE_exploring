"""Pressure-free rejection screen using the frozen q/eta shell definitions.

A failure rejects a saved approximation. Success cannot confer any full
acceptance status: primitive momentum and pressure are not evaluated here.
"""
from __future__ import annotations
import numpy as np
from independent_registered_metrics import metric,rms
from independent_geometry import shell_quadrature,random_shell

EQUATIONS=('q','eta')


def evaluate_reduced_set(field,r,z,weights):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=np.float64),np.asarray(z,dtype=np.float64))
    r=r.ravel();z=z.ravel();w=np.asarray(weights,dtype=np.float64).ravel()
    if len(w)!=len(r) or not np.all(w>0):raise ValueError('positive matching weights required')
    d=field.cylindrical(r,z,3);c=field.c_l;U=d['U'];q=d['q'][0,0]
    qr=2*r*d['q'][1,0];qz=d['q'][0,1];eta=d['eta'];er=2*r*d['eta_s'];ez=d['eta_z']
    Wr=c*r+U[:,0];Wz=c*z+U[:,2]
    # Preserve the reduced evaluator's grouping, independently of term metrics.
    Rq=np.sum(np.stack((q,Wr*qr,Wz*qz,2*d['ur_over_r']*q),axis=-1),axis=-1)
    Re=np.sum(np.stack(((1+c)*eta,Wr*er,Wz*ez,-2*q*qz),axis=-1),axis=-1)
    qt=[q,c*r*qr,c*z*qz,U[:,0]*qr,U[:,2]*qz,2*d['ur_over_r']*q]
    et=[(1+c)*eta,c*r*er,c*z*ez,U[:,0]*er,U[:,2]*ez,-2*q*qz]
    mq=metric(Rq,q,qt[3]+qt[4]+qt[5],qt,w)
    me=metric(Re,et[0],et[3]+et[4]+et[5],et,w)
    R=np.hypot(r,z)
    result={'points':len(r),'weight_sum':float(w.sum()),'equations':{'q':mq,'eta':me},
            'scaled_rms':{'q':rms(R**(2*field.alpha+2)*Rq,w),'eta':rms(R**(2*field.alpha+3)*Re,w)},
            'finite_arrays':all(np.all(np.isfinite(v)) for v in [r,z,U,q,eta,Rq,Re]),
            'velocity_rms':rms(U,w),'swirl_velocity_rms':rms(U[:,1],w),
            'q_term_sum_difference':float(np.max(np.abs(Rq-sum(qt)))),
            'eta_term_sum_difference':float(np.max(np.abs(Re-sum(et))))}
    arrays={'r':r,'z':z,'weights':w,'U':U,'q':q,'eta':eta,'q_residual':Rq,'eta_residual':Re}
    return result,arrays


def aggregate_reduced(rows):
    core={row['set']:row for row in rows if row['shell_index']==0}
    high={'rho':(-1.,None),'m':(-1.,None)};undefined=[];degenerate=[]
    for row in rows:
        for eq in EQUATIONS:
            m=row['metrics']['equations'][eq]
            location={'shell_index':row['shell_index'],'set':row['set'],'equation':eq}
            ref=core.get(row['set'])
            for kind in ['linear','nonlinear']:
                value=m[kind+'_rms'];floor=0. if ref is None else 1e-12*ref['metrics']['equations'][eq][kind+'_rms']
                m['degenerate_'+kind]=bool(value==0 or value<floor)
            if m['degenerate_linear'] or m['degenerate_nonlinear']:degenerate.append(location)
            if m['rho'] is None or m['m'] is None:undefined.append(location);continue
            for name in high:
                if m[name]>high[name][0]:high[name]=(m[name],location)
    failed=high['rho'][0]>1e-6 or high['m'][0]>1e-4
    return {'rho_max_reduced':high['rho'][0] if high['rho'][0]>=0 else None,'rho_max_at':high['rho'][1],
            'm_max_reduced':high['m'][0] if high['m'][0]>=0 else None,'m_max_at':high['m'][1],
            'undefined_metrics':undefined,'degenerate_metrics':degenerate,
            'rejected_by_reduced_measurements':bool(failed),'full_registered_acceptance':'NOT_EVALUATED',
            'scope':'Only q and eta on the registered points. Maxima are lower bounds for the full seven-equation measured maxima. No pressure, primitive momentum or acceptance pass is asserted.'}


def reduced_shells(field,a_eff,*,nradial=8,nangle=64,nrandom=256,seed=295174,shell_indices=range(-6,12),include_origin=True,callback=None):
    if nradial<8 or nangle<64 or nrandom<256:raise ValueError('below frozen minimum evaluation resolution')
    if not np.isfinite(a_eff) or a_eff<=0:raise ValueError('positive finite a_eff required')
    intervals=[(int(k),a_eff*2.**k,a_eff*2.**(k+1)) for k in shell_indices]
    if include_origin:intervals.insert(0,('origin',0.,a_eff*2.**-6))
    rng=np.random.default_rng(seed);rows=[];arrays={}
    for k,lo,hi in intervals:
        # Match the registered evaluator's random-number consumption exactly.
        random_grid=random_shell(lo,hi,rng,nrandom)
        for name,grid in [('shell_gauss',shell_quadrature(lo,hi,nradial=nradial,nangle=nangle)),
                          ('collar_gauss',shell_quadrature(lo,hi,nradial=nradial,nangle=nangle,collar=True)),
                          ('shell_random',random_grid)]:
            summary,values=evaluate_reduced_set(field,grid['r'],grid['z'],grid['weights'])
            rows.append({'shell_index':k,'set':name,'lower':lo,'upper':hi,
                         'measure':grid.get('measure','Independent uniform physical volume samples'),'metrics':summary})
            for key,value in values.items():arrays[f'{k}_{name}_{key}']=value
        if callback:callback(rows,arrays,{'completed_shell':k})
    return {'a_eff':a_eff,'seed':seed,'nradial':nradial,'nangle':nangle,'nrandom':nrandom,
            'rows':rows,'aggregate':aggregate_reduced(rows)},arrays
