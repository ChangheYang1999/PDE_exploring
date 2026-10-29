"""The frozen SPEC 6.1/8 shell metrics, independently implemented.

No pointwise denominator is floored. Undefined zero denominators remain
explicitly unassessable rather than becoming a successful zero residual.
"""
from __future__ import annotations
import time
import numpy as np
from independent_geometry import shell_quadrature,random_shell,omega_squared

ACCEPTANCE_EQUATIONS=('M_r','M_theta','M_z','q','eta','div','ell')


def magnitude(values):
    values=np.asarray(values,dtype=np.float64)
    return np.linalg.norm(values,axis=-1) if values.ndim==2 else np.abs(values)


def rms(values,weights):
    a=magnitude(values);weights=np.asarray(weights,dtype=np.float64)
    return float(np.sqrt(np.dot(weights,a*a)/np.sum(weights)))


def ratio(numerator,denominator):
    return float(numerator/denominator) if denominator>0 else None


def metric(residual,linear,nonlinear,terms,weights,*,denominator=None):
    lr=rms(linear,weights);nr=rms(nonlinear,weights)
    d=min(lr,nr) if denominator is None else float(denominator)
    rr=rms(residual,weights);maximum=float(np.max(magnitude(residual)))
    tr=[rms(t,weights) for t in terms];td=max(tr,default=0.)
    return {'rms':rr,'maximum':maximum,'linear_rms':lr,'nonlinear_rms':nr,'denominator':d,
            'rho':ratio(rr,d),'m':ratio(maximum,d),'sigma':ratio(rr,lr),
            'nonlinear_ratio':ratio(rr,nr),'classical_per_term_ratio':ratio(rr,td),
            'term_rms':tr,'undefined_denominator':bool(d==0)}


def evaluate_set(field,r,z,weights,P,gradient):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=np.float64),np.asarray(z,dtype=np.float64))
    shape=r.shape;r=r.ravel();z=z.ravel();w=np.asarray(weights,dtype=np.float64).ravel()
    P=np.asarray(P,dtype=np.float64).ravel();gradient=np.asarray(gradient,dtype=np.float64).reshape(-1,2)
    xyz=np.stack((r,np.zeros_like(r),z),axis=-1);U,J=field.cartesian(xyz,True)
    d=field.cylindrical(r,z,3);red=field.reduced(r,z);c=field.c_l
    L=(1-c)*U;D=c*np.einsum('nij,nj->ni',J,xyz);N=np.einsum('nij,nj->ni',J,U)
    GP=np.stack((gradient[:,0],np.zeros_like(r),gradient[:,1]),axis=-1);M=L+D+N+GP
    q=d['q'][0,0];qr=2*r*d['q'][1,0];qz=d['q'][0,1]
    qt=[q,c*r*qr,c*z*qz,U[:,0]*qr,U[:,2]*qz,2*d['ur_over_r']*q]
    Nq=qt[3]+qt[4]+qt[5]
    eta=d['eta'];er=2*r*d['eta_s'];ez=d['eta_z']
    et=[(1+c)*eta,c*r*er,c*z*ez,U[:,0]*er,U[:,2]*ez,-2*q*qz]
    Ne=et[3]+et[4]+et[5]
    result={'M_vector':metric(M,L,N,[L,D,N,GP],w)}
    for j,name in enumerate(['M_r','M_theta','M_z']):
        result[name]=metric(M[:,j],L,N,[L,D,N,GP],w)
    result['q']=metric(red['q'],q,Nq,qt,w)
    result['eta']=metric(red['eta'],et[0],Ne,et,w)
    div=np.trace(J,axis1=-2,axis2=-1);Jnorm=np.linalg.norm(J,axis=(-2,-1));jd=rms(Jnorm,w)
    result['div']=metric(div,Jnorm,Jnorm,[Jnorm],w,denominator=jd)
    result['ell']=metric(red['elliptic'],eta,eta,[eta],w,denominator=rms(eta,w))
    R=np.hypot(r,z)
    scaled={'M_vector':rms(R[:,None]**(2*field.alpha+1)*M,w),
            'q':rms(R**(2*field.alpha+2)*red['q'],w),
            'eta':rms(R**(2*field.alpha+3)*red['eta'],w)}
    finite=all(np.all(np.isfinite(a)) for a in [U,J,M,red['q'],red['eta'],P,gradient])
    summary={'points':len(r),'weight_sum':float(np.sum(w)),'equations':result,'scaled_rms':scaled,
             'finite_arrays':finite,'velocity_rms':rms(U,w),'pressure_rms':rms(P,w),'pressure_maximum':float(np.max(np.abs(P))),
             'swirl_velocity_rms':rms(U[:,1],w),'q_maximum':float(np.max(np.abs(q))),
             'q_minimum':float(np.min(q)),'q_maximum_signed':float(np.max(q)),
             'cartesian_cylindrical_residual_difference':float(np.max(np.abs(M-field.primitive_cylindrical(r,z,gradient)))),
             'q_term_sum_difference':float(np.max(np.abs(red['q']-sum(qt)))),
             'eta_term_sum_difference':float(np.max(np.abs(red['eta']-sum(et))))}
    arrays={'r':r,'z':z,'weights':w,'U':U,'pressure':P,'pressure_gradient':gradient,'M':M,'q_residual':red['q'],
            'eta_residual':red['eta'],'divergence':div,'elliptic':red['elliptic'],'vorticity_norm':np.sqrt(omega_squared(field,r,z))}
    return summary,arrays


def annotate_and_aggregate(rows):
    # [a_eff,2 a_eff] is the explicitly chosen reference core shell. Collars
    # compare against that shell's collar, random points against its random set.
    core={row['set']:row for row in rows if row['shell_index']==0}
    flags=[];undefined=[];maximum_rho=-1.;maximum_m=-1.;rho_at=None;m_at=None
    for row in rows:
        for eq in ACCEPTANCE_EQUATIONS:
            m=row['metrics']['equations'][eq];reference=core.get(row['set'])
            if reference is not None:
                ref=reference['metrics']['equations'][eq]
                m['degenerate_linear']=bool(m['linear_rms']<1e-12*ref['linear_rms'] or m['linear_rms']==0)
                m['degenerate_nonlinear']=bool(m['nonlinear_rms']<1e-12*ref['nonlinear_rms'] or m['nonlinear_rms']==0)
            else:m['degenerate_linear']=m['linear_rms']==0;m['degenerate_nonlinear']=m['nonlinear_rms']==0
            location={'shell_index':row['shell_index'],'set':row['set'],'equation':eq}
            if m['degenerate_linear'] or m['degenerate_nonlinear']:flags.append(location)
            if m['rho'] is None or m['m'] is None:undefined.append(location);continue
            if m['rho']>maximum_rho:maximum_rho=m['rho'];rho_at=location
            if m['m']>maximum_m:maximum_m=m['m'];m_at=location
    return {'rho_max':maximum_rho if maximum_rho>=0 else None,'rho_max_at':rho_at,
            'm_max':maximum_m if maximum_m>=0 else None,'m_max_at':m_at,
            'undefined_metrics':undefined,'degenerate_metrics':flags,
            'all_required_metrics_assessable':not undefined,
            'A1_measured_pass':not undefined and 0<=maximum_rho<=1e-6,
            'A2_measured_pass':not undefined and 0<=maximum_m<=1e-4,
            'scope':'A1/A2 measured values only. Full A or B acceptance requires all remaining registered criteria.'}


def registered_shells(field,pressure,a_eff,*,nradial=8,nangle=64,nrandom=256,seed=295174,
                      shell_indices=range(-6,12),include_origin=True,callback=None,
                      resume_rows=None,resume_arrays=None):
    if nradial<8 or nangle<64 or nrandom<256:raise ValueError('below frozen minimum evaluation resolution')
    if not np.isfinite(a_eff) or a_eff<=0:raise ValueError('positive a_eff required')
    rng=np.random.default_rng(seed);rows=list(resume_rows or []);arrays=dict(resume_arrays or {});started=time.time()
    intervals=[(int(k),a_eff*2.**k,a_eff*2.**(k+1)) for k in shell_indices]
    if include_origin:intervals.insert(0,('origin',0.,a_eff*2.**-6))
    if len(rows)%3:raise ValueError('resume rows must contain complete three-set shells')
    done=len(rows)//3
    if done>len(intervals):raise ValueError('too many resumed shells')
    for i,(k,lo,hi) in enumerate(intervals):
        # Draw even for completed shells so an interrupted run retains exactly
        # the same independent holdout points as an uninterrupted run.
        random_grid=random_shell(lo,hi,rng,nrandom)
        if i<done:
            previous=rows[3*i:3*i+3]
            expected=['shell_gauss','collar_gauss','shell_random']
            if any(row['shell_index']!=k or row['set']!=name or row['lower']!=lo or row['upper']!=hi
                   for row,name in zip(previous,expected)):
                raise ValueError('resume rows do not match the requested shell prefix')
            for name in expected:
                for key in ['r','z','weights','U','pressure','pressure_gradient','M','q_residual','eta_residual','divergence','elliptic','vorticity_norm']:
                    if f'{k}_{name}_{key}' not in arrays:raise ValueError('missing resumed array')
            continue
        for collar in [False,True]:
            grid=shell_quadrature(lo,hi,nradial=nradial,nangle=nangle,collar=collar)
            P,G=pressure.on_spheres(grid['radii'],grid['mu'])
            metrics,values=evaluate_set(field,grid['r'],grid['z'],grid['weights'],P,G)
            name='collar_gauss' if collar else 'shell_gauss'
            row={'shell_index':k,'set':name,'lower':lo,'upper':hi,'measure':grid['measure'],'metrics':metrics}
            rows.append(row)
            for key,value in values.items():arrays[f'{k}_{name}_{key}']=value
        grid=random_grid;P,G=pressure.evaluate(grid['r'],grid['z'])
        metrics,values=evaluate_set(field,grid['r'],grid['z'],grid['weights'],P,G)
        rows.append({'shell_index':k,'set':'shell_random','lower':lo,'upper':hi,
                     'measure':'Independent uniform physical volume samples','metrics':metrics})
        for key,value in values.items():arrays[f'{k}_shell_random_{key}']=value
        if callback:callback(rows,arrays,{'completed_shell':k,'elapsed_seconds':time.time()-started})
    aggregate=annotate_and_aggregate(rows)
    return {'a_eff':a_eff,'seed':seed,'nradial':nradial,'nangle':nangle,'nrandom':nrandom,
            'aggregation':'Report Gauss, independent random and collar metrics separately; use the maximum over all three sets for conservative A1/A2 assessment.',
            'core_reference_shell':'[a_eff,2 a_eff] with matching set type','rows':rows,'aggregate':aggregate,
            'elapsed_seconds':time.time()-started},arrays
