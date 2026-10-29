"""Candidate diagnostics; all reported defects are measurements of approximations."""
from __future__ import annotations
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import minimize
from independent_pressure import GreenPoisson,DirectNewtonPressure,geometric_edges,shell_nodes
from independent_identities import vorticity_and_jacobian,finite_ball_balance,characteristic_balance
from independent_tail_audit import tail_audit,scalar_cancellation

LEVELS={
    'pilot':dict(lmax=12,nangle=32,nradial=20),
    'medium':dict(lmax=20,nangle=56,nradial=32),
    'fine':dict(lmax=32,nangle=88,nradial=48),
}


def weighted_rms(values,w):
    values=np.asarray(values)
    if values.ndim>1:values=np.sum(values*values,axis=-1)
    else:values=values*values
    return float(np.sqrt(np.dot(w,values)/np.sum(w)))


def residual_norms(residual,terms,w):
    rms=weighted_rms(residual,w)
    term_rms=[weighted_rms(terms[...,j],w) for j in range(terms.shape[-1])]
    denom=sum(term_rms)
    return {'rms':rms,'max':float(np.max(np.abs(residual))),
            'relative_rms':rms/denom if denom>0 else 0.,'term_rms':term_rms}


def shell_diagnostics(field,radii,mu,w,pressure):
    P,grad=pressure.on_spheres(radii,mu)
    r=np.asarray(radii)[:,None]*np.sqrt(1-mu[None,:]**2)
    z=np.asarray(radii)[:,None]*mu[None,:]
    d=field.cylindrical(r,z)
    red=field.reduced(r,z)
    primitive=field.primitive_cylindrical(r,z,grad)
    ur,ut,uz=np.moveaxis(d['U'],-1,0)
    c=field.c_l
    linear=(1-c)*d['U']
    Wr=c*r+ur;Wz=c*z+uz
    advection=np.stack((Wr*d['ur_r']+Wz*d['ur_z']-r*d['q'][0,0]**2,
                        Wr*d['ut_r']+Wz*d['ut_z']+d['ur_over_r']*ut,
                        Wr*d['uz_r']+Wz*d['uz_z']),axis=-1)
    gp=np.stack((grad[...,0],np.zeros_like(r),grad[...,1]),axis=-1)
    dilation=np.stack((c*r*d['ur_r']+c*z*d['ur_z'],c*r*d['ut_r']+c*z*d['ut_z'],c*r*d['uz_r']+c*z*d['uz_z']),axis=-1)
    nonlinear=advection-dilation
    xyz=np.stack((r,np.zeros_like(r),z),axis=-1)
    primitive_cartesian=field.primitive_cartesian(xyz,gp)
    rows=[]
    for k,R in enumerate(radii):
        pnorm=weighted_rms(primitive[k],w)
        term_norms=[weighted_rms(term[k],w) for term in [linear,dilation,nonlinear,gp]]
        denom=sum(term_norms)
        velocity=weighted_rms(d['U'][k],w)
        swirl=weighted_rms(ut[k],w)
        rows.append({'R':float(R),'q':residual_norms(red['q'][k],red['q_terms'][k],w),
                     'eta':residual_norms(red['eta'][k],red['eta_terms'][k],w),
                     'primitive_rms':pnorm,'primitive_max':float(np.max(np.linalg.norm(primitive[k],axis=-1))),
                     'primitive_relative_rms':pnorm/denom if denom else 0.,
                     'primitive_term_rms':term_norms,
                     'cartesian_cylindrical_max_difference':float(np.max(np.abs(primitive[k]-primitive_cartesian[k]))),
                     'primitive_scaled_rms':float(R**(2*field.alpha+1)*pnorm),
                     'q_scaled_rms':float(R**(2*field.alpha+2)*weighted_rms(red['q'][k],w)),
                     'eta_scaled_rms':float(R**(2*field.alpha+3)*weighted_rms(red['eta'][k],w)),
                     'velocity_rms':velocity,'swirl_rms':swirl,'swirl_ratio':swirl/velocity if velocity else 0.,
                     'scaled_velocity_rms':float(R**field.alpha*velocity),
                     'divergence_max':float(np.max(np.abs(red['divergence'][k]))),
                     'circulation_equivalence_error':float(np.max(np.abs(red['gamma'][k]-r[k]**2*red['q'][k])))})
    arrays={'radii':np.asarray(radii),'mu':mu,'weights':w,'U':d['U'],'pressure':P,'pressure_gradient':grad,
            'primitive_residual':primitive,'q_residual':red['q'],'eta_residual':red['eta']}
    return rows,arrays


def axis_audit(field,zvalues):
    zvalues=np.asarray(zvalues,dtype=np.float64)
    zero=np.zeros_like(zvalues)
    red=field.reduced(zero,zvalues)
    xyz=np.stack((zero,zero,zvalues),axis=-1)
    U,J=field.cartesian(xyz,True)
    p=field.phi.jet(zero,zvalues,3);q=field.q.jet(zero,zvalues,2)
    explicit_q=(1-2*p[0,1])*q[0,0]+(field.c_l*zvalues+2*p[0,0])*q[0,1]
    eta=-8*p[1,0]-p[0,2]
    eta_z=-8*p[1,1]-p[0,3]
    explicit_eta=(1+field.c_l)*eta+(field.c_l*zvalues+2*p[0,0])*eta_z-2*q[0,0]*q[0,1]
    hvalues=[1e-2,3e-3,1e-3,3e-4]
    fd=[]
    collars=[]
    for h in hvalues:
        Jfd=np.empty_like(J)
        for j in range(3):
            step=np.zeros(3);step[j]=h
            Jfd[...,j]=(-field.cartesian(xyz+2*step)+8*field.cartesian(xyz+step)-8*field.cartesian(xyz-step)+field.cartesian(xyz-2*step))/(12*h)
        fd.append(float(np.max(np.abs(Jfd-J))))
    for radius in [0.,1e-9,1e-7,1e-5,1e-3,.03]:
        cr=field.reduced(np.full_like(zvalues,radius),zvalues)
        collars.append({'r':radius,'q_max':float(np.max(np.abs(cr['q']))),'eta_max':float(np.max(np.abs(cr['eta']))),
                        'q_relative_rms':residual_norms(cr['q'],cr['q_terms'],np.ones_like(zvalues))['relative_rms'],
                        'eta_relative_rms':residual_norms(cr['eta'],cr['eta_terms'],np.ones_like(zvalues))['relative_rms']})
    p4=field.phi.jet(zero,zvalues,4);q2=field.q.jet(zero,zvalues,2)
    W0=field.c_l*zvalues+2*p4[0,0]
    eta_s=-12*p4[2,0]-p4[1,2]
    eta_sz=-12*p4[2,1]-p4[1,3]
    rq_s=(1+2*field.c_l-4*p4[0,1])*q2[1,0]+4*p4[1,0]*q2[0,1]+W0*q2[1,1]-2*p4[1,1]*q2[0,0]
    re_s=(1+3*field.c_l-2*p4[0,1])*eta_s+4*p4[1,0]*eta_z+W0*eta_sz-2*q2[1,0]*q2[0,1]-2*q2[0,0]*q2[1,1]
    taylor=[]
    for radius in [.04,.02,.01,.005]:
        value=field.reduced(np.full_like(zvalues,radius),zvalues)
        taylor.append({'r':radius,'q_quadratic_remainder_max':float(np.max(np.abs(value['q']-red['q']-radius**2*rq_s))),
                       'eta_quadratic_remainder_max':float(np.max(np.abs(value['eta']-red['eta']-radius**2*re_s)))})
    return {'zvalues':zvalues.tolist(),'q_residual':red['q'].tolist(),'eta_residual':red['eta'].tolist(),
            'q_residual_s_derivative_at_axis':rq_s.tolist(),'eta_residual_s_derivative_at_axis':re_s.tolist(),
            'quadratic_taylor_remainders':taylor,
            'q_values':q[0,0].tolist(),'axial_velocity':U[:,2].tolist(),
            'explicit_q_error':float(np.max(np.abs(red['q']-explicit_q))),
            'explicit_eta_error':float(np.max(np.abs(red['eta']-explicit_eta))),
            'fd_steps':hvalues,'fd_jacobian_errors':fd,'collars':collars,
            'regularity_basis_statement':'Smooth monomial-envelope functions of r squared and z; no cylindrical divisions in the Cartesian evaluator.'}


def vorticity_maximum(field,Rmax=12.):
    rs=np.r_[0.,np.geomspace(.01,Rmax,14)]
    zs=np.linspace(-Rmax,Rmax,25)
    r,z=np.meshgrid(rs,zs,indexing='ij')
    xyz=np.stack((r.ravel(),np.zeros(r.size),z.ravel()),axis=-1)
    omega,_=vorticity_and_jacobian(field,xyz)
    order=np.argsort(-np.sum(omega*omega,axis=-1))[:6]
    def obj(v):
        pt=np.array([v[0],0.,v[1]])
        o,jo=vorticity_and_jacobian(field,pt)
        gradient=-2*o@jo
        return -float(o@o),gradient[[0,2]]
    best=None
    records=[]
    for i in order:
        initial=[xyz[i,0],xyz[i,2]]
        result=minimize(obj,initial,jac=True,method='L-BFGS-B',bounds=[(0.,Rmax),(-Rmax,Rmax)],options={'ftol':1e-14,'gtol':1e-11,'maxiter':150})
        records.append({'initial':initial,'point':result.x.tolist(),'success':bool(result.success),'norm':float(np.sqrt(max(0.,-result.fun)))})
        if best is None or result.fun<best.fun:best=result
    pt=np.array([best.x[0],0.,best.x[1]])
    U,JU=field.cartesian(pt,True);o,JO=vorticity_and_jacobian(field,pt)
    n2=float(o@o)
    stretching=float(o@JU@o/n2) if n2>0 else None
    gradnorm=float(np.linalg.norm(2*o@JO))
    return {'search_radius':Rmax,'point_r_z':best.x.tolist(),'vorticity_norm':float(np.sqrt(n2)),
            'stretching_ratio':stretching,'stretching_defect':None if stretching is None else stretching-1,
            'gradient_vorticity_squared_norm':gradnorm,
            'at_search_boundary':bool(best.x[0]>.999*Rmax or abs(best.x[1])>.999*Rmax),
            'global_maximum_proved':False,'starts':records}


def diagnose(field,*,level='pilot',radii=None,include_direct=True):
    config=LEVELS[level]
    pressure=GreenPoisson(field.source,decay_power=2*field.alpha,**config)
    mu,w=roots_legendre(config['nangle']+7)
    if radii is None:
        radii=np.r_[np.geomspace(.012,6.,15),12.,24.,48.,96.,256.,1024.,4096.]
    rows,arrays=shell_diagnostics(field,radii,mu,w,pressure)
    axis=axis_audit(field,np.r_[-8.,-4.,-2.,-1.,-.4,0.,.4,1.,2.,4.,8.])
    balances=[]
    for R in [.25,1.,4.,16.,64.,256.]:
        # on_spheres avoids repeating identical radial inversions.
        def at_boundary(r,z):
            rr=np.hypot(r,z)
            if np.max(rr)-np.min(rr)<1e-10*max(1.,R):
                return tuple(a[0] for a in pressure.on_spheres([R],np.asarray(z)/R))
            return pressure.evaluate(r,z)
        balances.append(finite_ball_balance(field,at_boundary,R,nangle=config['nangle']+5,nradial=config['nradial']))
    direct=[]
    if include_direct:
        other=DirectNewtonPressure(field.source,decay_power=2*field.alpha,nradial=64,nangle=64)
        for r,z in [(0.,0.),(0.,.7),(.43,-.31),(1.7,.23)]:
            p,g=pressure.evaluate(r,z);p2=other.evaluate(r,z)
            direct.append({'r':r,'z':z,'green_pressure':float(p),'direct_pressure':p2,'absolute_difference':abs(float(p)-p2)})
    trajectories=[]
    for initial in [[.4,.2],[1.3,-.7]]:
        trajectories.append({'initial':initial,'checks':characteristic_balance(field,initial,(-3.,3.))})
    # Independent Cartesian finite differences at off-axis and axial points.
    points=np.array([[0.,0.,0.],[0.,0.,.73],[.31,-.27,.19],[1.23,.37,-.81],[3.1,-2.7,1.2]])
    U,J=field.cartesian(points,True)
    fd=[]
    for h in [1e-2,3e-3,1e-3,3e-4]:
        jfd=np.empty_like(J)
        for j in range(3):
            e=np.zeros(3);e[j]=h
            jfd[...,j]=(-field.cartesian(points+2*e)+8*field.cartesian(points+e)-8*field.cartesian(points-e)+field.cartesian(points-2*e))/(12*h)
        fd.append({'h':h,'jacobian_max_error':float(np.max(np.abs(jfd-J))),
                   'advection_max_error':float(np.max(np.abs(np.einsum('...ij,...j->...i',jfd-J,field.c_l*points+U))))})
    stream=GreenPoisson(field.eta,dimension=5,decay_power=field.alpha,**config)
    stream_radii=np.array([0.,.125,.5,2.,8.,32.,128.])
    smu=np.array([-1.,-.72,0.,.37,1.])
    sp,sg=stream.on_spheres(stream_radii,smu)
    sr=stream_radii[:,None]*np.sqrt(1-smu[None,:]**2);sz=stream_radii[:,None]*smu[None,:]
    ep=field.phi.evaluate(sr*sr,sz)
    eg=np.stack((2*sr*field.phi.evaluate(sr*sr,sz,1,0),field.phi.evaluate(sr*sr,sz,0,1)),axis=-1)
    stream_check={'radii':stream_radii.tolist(),'mu':smu.tolist(),
                  'value_error_max':float(np.max(np.abs(sp-ep))),
                  'gradient_error_max':float(np.max(np.abs(sg-eg))),
                  'value_reference_max':float(np.max(np.abs(ep))),
                  'gradient_reference_max':float(np.max(np.abs(eg))),
                  'method':'Independent full-space 5D Gegenbauer Green inverse of the analytically evaluated eta.'}
    farfield=tail_audit(field,np.asarray(radii),mu,w,arrays['pressure'],arrays['pressure_gradient'])
    cancellation={name:scalar_cancellation(scalar,points[:,0]**2+points[:,1]**2,points[:,2]) for name,scalar in [('phi',field.phi),('q',field.q)]}
    summary={'level':level,'configuration':config,'c_l':field.c_l,'alpha':field.alpha,'shells':rows,'axis':axis,
             'balances':balances,'pressure_cross_checks':direct,'characteristics':trajectories,
             'vorticity_maximum':vorticity_maximum(field),'cartesian_fd':fd,
             'full_space_stream_reconstruction':stream_check,'farfield':farfield,'basis_cancellation':cancellation,
             'primitive_relative_denominator':'Sum of shell L2 norms of (1-c_l)U, c_l y dot grad U, U dot grad U, and grad P.',
             'candidate_acceptance':'NOT ASSESSED: this measurement record alone does not certify refinement, field stability, or the registered acceptance conditions.'}
    return summary,arrays
