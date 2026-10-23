"""Independent Cartesian finite differences and Euler profile diagnostics.

No import from the training project. J[n,i,j] = partial_j U_i.
Finite samples and FP64 are numerical evidence, never a global proof.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import numpy as np

Q = np.array([-1., -1., 1.])


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def stencil(order=4):
    if order == 4:
        nodes = np.array([-2, -1, 0, 1, 2])
        first = np.array([1/12, -2/3, 0, 2/3, -1/12])
        second = np.array([-1/12, 4/3, -5/2, 4/3, -1/12])
    elif order == 6:
        nodes = np.arange(-3, 4)
        first = np.array([-1/60, 3/20, -3/4, 0, 3/4, -3/20, 1/60])
        second = np.array([1/90, -3/20, 3/2, -49/18, 3/2, -3/20, 1/90])
    else:
        raise ValueError('order must be 4 or 6')
    return nodes, first, second


def differentiate(forward, x, step=0.003, order=4, hessian=True, steps=None):
    """Centered physical-coordinate derivatives of an arbitrary vector forward.

    Each sample has a fixed stencil scale. It is not differentiated as a field.
    Mixed partials use a tensor product of first derivative stencils.
    """
    x = np.asarray(x, dtype=np.float64)
    f = np.asarray(forward(x), dtype=np.float64)
    if f.ndim == 1:
        f = f[:, None]
    if steps is None:
        h = np.repeat((step*np.maximum(1., np.linalg.norm(x, axis=1)))[:, None], 3, axis=1)
    else:
        h = np.broadcast_to(np.asarray(steps), x.shape)
    if np.any(h <= 0):
        raise ValueError('strictly positive step sizes required')
    n, dim = f.shape
    J = np.zeros((n, dim, 3))
    H = np.zeros((n, dim, 3, 3)) if hessian else None
    nodes, w1, w2 = stencil(order)
    for j in range(3):
        for k, a, b in zip(nodes, w1, w2):
            if k == 0:
                value = f
            else:
                point = x.copy()
                point[:, j] += k*h[:, j]
                value = np.asarray(forward(point)).reshape(n, dim)
            if a:
                J[:, :, j] += a*(value-f)/h[:, j, None]
            if hessian and b:
                # Subtracting f reduces cancellation; stencil weights sum to zero.
                H[:, :, j, j] += b*(value-f)/h[:, j, None]**2
    if hessian:
        for j in range(3):
            for k in range(j+1, 3):
                for a, wa in zip(nodes, w1):
                    if not wa:
                        continue
                    for b, wb in zip(nodes, w1):
                        if not wb:
                            continue
                        point = x.copy()
                        point[:, j] += a*h[:, j]
                        point[:, k] += b*h[:, k]
                        value = np.asarray(forward(point)).reshape(n, dim)
                        H[:, :, j, k] += wa*wb*(value-f)/(h[:, j]*h[:, k])[:, None]
                H[:, :, k, j] = H[:, :, j, k]
    return f, J, H


def curl(J):
    return np.stack([J[:, 2, 1]-J[:, 1, 2], J[:, 0, 2]-J[:, 2, 0], J[:, 1, 0]-J[:, 0, 1]], axis=1)


def residuals(x, values, J_all, H_all, c_l, C=0.):
    U, P = values[:, :3], values[:, 3]
    J, gp = J_all[:, :3], J_all[:, 3]
    V = c_l*x+U
    V[:, 2] += C
    linear = (1-c_l)*U
    dilation = c_l*np.einsum('nij,nj->ni', J, x)
    drift = C*J[:, :, 2]
    convection = np.einsum('nij,nj->ni', J, U)
    rm = linear+dilation+drift+convection+gp
    delta = np.trace(J, axis1=1, axis2=2)
    om = curl(J)
    result = dict(U=U, P=P, J=J, grad_P=gp, V=V, Omega=om, momentum=rm,
                  divergence=delta, momentum_terms=[linear, dilation, drift, convection, gp])
    if H_all is not None:
        H = H_all[:, :3]
        Hp = H_all[:, 3]
        Jo = np.stack([H[:, 2, 1]-H[:, 1, 2], H[:, 0, 2]-H[:, 2, 0], H[:, 1, 0]-H[:, 0, 1]], axis=1)
        adv_o = np.einsum('nij,nj->ni', Jo, V)
        stretch = np.einsum('nij,nj->ni', J, om)
        rw = om+adv_o-stretch
        lap_p = np.trace(Hp, axis1=1, axis2=2)
        trJ2 = np.einsum('nij,nji->n', J, J)
        rp = -lap_p-trJ2
        lap_u = np.trace(H, axis1=2, axis2=3)
        grad_delta = np.einsum('niik->nk', H)
        # Derivative of R_m from separately computed J and H, for index checks.
        Jrm = J+np.einsum('nij,njk->nik', J, J)+np.einsum('nj,nijk->nik', V, H)+Hp
        result.update(H=H, J_Omega=Jo, vorticity=rw, pressure_poisson=rp,
                      vorticity_terms=[om, adv_o, -stretch], pressure_terms=[-lap_p, -trJ2],
                      laplacian_U=lap_u, curvature=H, stretching=stretch,
                      grad_divergence=grad_delta,
                      curl_identity_defect=curl(Jrm)-rw-delta[:, None]*om,
                      divergence_identity_defect=np.trace(Jrm, axis1=1, axis2=2)-delta-np.einsum('ni,ni->n', V, grad_delta)+rp)
    return result


def amplitudes(a):
    a = np.asarray(a)
    return np.abs(a) if a.ndim == 1 else np.linalg.norm(a.reshape(len(a), -1), axis=1)


def stats(a):
    norm = amplitudes(a)
    return dict(rms=float(np.sqrt(np.mean(norm**2))), q50=float(np.quantile(norm, .5)),
                q90=float(np.quantile(norm, .9)), q99=float(np.quantile(norm, .99)), q999=float(np.quantile(norm, .999)),
                sampled_max=float(np.max(norm)))


def term_relative(residual, terms):
    numerator = stats(residual)['rms']
    term_rms = [stats(t)['rms'] for t in terms]
    denominator = sum(term_rms)
    return dict(absolute=stats(residual), term_rms=term_rms, denominator=denominator,
                relative_rms=(numerator/denominator if denominator > 0 else None),
                denominator_zero=(denominator == 0))


def summarize(r, volume=None):
    out = {k: stats(r[k]) for k in ['U','Omega','J']}
    out['momentum'] = term_relative(r['momentum'], r['momentum_terms'])
    out['divergence'] = term_relative(r['divergence'], [r['J']])
    if 'vorticity' in r:
        out['vorticity'] = term_relative(r['vorticity'], r['vorticity_terms'])
        out['pressure_poisson'] = term_relative(r['pressure_poisson'], r['pressure_terms'])
        for k in ['laplacian_U','curvature','curl_identity_defect','divergence_identity_defect']:
            out[k] = stats(r[k])
    out['sample_count'] = len(r['U'])
    out['physical_volume'] = volume
    out['measure'] = 'uniform physical volume' if volume is not None else 'diagnostic sample measure; not a 3D volume norm'
    if volume is not None:
        out['momentum_L2_estimate'] = math.sqrt(volume)*out['momentum']['absolute']['rms']
        out['velocity_L2_estimate'] = math.sqrt(volume)*out['U']['rms']
    return out


def uniform_shell(rng, n, inner, outer):
    direction = rng.normal(size=(n, 3))
    direction /= np.linalg.norm(direction, axis=1)[:, None]
    r = (inner**3+rng.random(n)*(outer**3-inner**3))**(1/3)
    return direction*r[:, None]


def holdout_regions(seed=736291, n=512):
    rng = np.random.default_rng(seed)
    out = {}
    for inner, outer in [(0, .25),(.25,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64)]:
        label = f'shell_{inner:g}_{outer:g}'
        out[label] = (uniform_shell(rng,n,inner,outer), 4*math.pi/3*(outer**3-inner**3))
    # Cartesian deterministic interior grid is an additional diagnostic, not reused training points.
    axis = np.linspace(-1.,1.,11)
    out['cartesian_grid_core']=(np.stack(np.meshgrid(axis,axis,axis,indexing='ij'),axis=-1).reshape(-1,3),None)
    z = np.linspace(-4.,4.,129)
    out['axis_line']=(np.stack([np.zeros_like(z),np.zeros_like(z),z],axis=1),None)
    return out


def to_cylindrical(U, theta):
    cs, sn = np.cos(theta), np.sin(theta)
    return np.stack([cs*U[:,0]+sn*U[:,1],-sn*U[:,0]+cs*U[:,1],U[:,2]],axis=1)


def from_cylindrical(U, theta):
    cs, sn = np.cos(theta), np.sin(theta)
    return np.stack([cs*U[:,0]-sn*U[:,1],sn*U[:,0]+cs*U[:,1],U[:,2]],axis=1)


def cylindrical_residual(forward, points, c_l, C=0., step=.002, order=4):
    r = np.hypot(points[:,0],points[:,1])
    if np.any(r <= 0):
        raise ValueError('Cylindrical comparison only away from the axis')
    theta = np.arctan2(points[:,1],points[:,0])
    q = np.stack([r,theta,points[:,2]],axis=1)
    def fc(q):
        rr, tt, zz = q.T
        xyz=np.stack([rr*np.cos(tt),rr*np.sin(tt),zz],axis=1)
        f=forward(xyz)
        return np.column_stack([to_cylindrical(f[:,:3],tt), f[:,3]])
    local_scale=np.maximum(1.,np.linalg.norm(points,axis=1))
    steps=np.stack([np.minimum(step*local_scale,r/4),np.full(len(q),step),step*local_scale],axis=1)
    f, J, _=differentiate(fc,q,order=order,hessian=False,steps=steps)
    U=f[:,:3]
    V=np.column_stack([c_l*r+U[:,0],U[:,1]/r,c_l*q[:,2]+C+U[:,2]])
    R=(1-c_l)*U+np.einsum('nij,nj->ni',J[:,:3],V)
    R[:,0]+=-U[:,1]**2/r+J[:,3,0]
    R[:,1]+=U[:,0]*U[:,1]/r+J[:,3,1]/r
    R[:,2]+=J[:,3,2]
    div=J[:,0,0]+U[:,0]/r+J[:,1,1]/r+J[:,2,2]
    return from_cylindrical(R,theta),div


def affine_fit(x, U):
    X=np.column_stack([np.ones(len(x)),x])
    coefficients=np.linalg.lstsq(X,U,rcond=None)[0]
    error=U-X@coefficients
    denom=stats(U)['rms']
    return dict(offset=coefficients[0].tolist(),matrix=coefficients[1:].T.tolist(),
                remainder=stats(error),relative_remainder=(stats(error)['rms']/denom if denom else None))


def angular_diagnostics(forward, radii=(.25,.5,1,2,4,8,16,32), zlevels=(-1.,-.25,0.,.4,1.3), ntheta=128):
    theta=2*math.pi*np.arange(ntheta)/ntheta
    rings=[]
    total_energy=nonaxi=n2=0.
    for r in radii:
        for z in zlevels:
            x=np.column_stack([r*np.cos(theta),r*np.sin(theta),np.full(ntheta,z)])
            f=forward(x)
            uc=to_cylindrical(f[:,:3],theta)
            coeff=np.fft.fft(uc,axis=0)/ntheta
            energy=np.sum(abs(coeff)**2,axis=1)
            e=float(energy.sum()); na=float(energy[1:].sum()); two=float(energy[2]+energy[-2])
            total_energy+=e; nonaxi+=na; n2+=two
            rings.append(dict(r=r,z=z,total_velocity_energy=e,nonaxisymmetric_energy=na,n2_energy=two,
                              low_modes={str(k):float(energy[k]+(energy[-k] if k else 0)) for k in range(17)},
                              top_quarter_frequency_energy=float(energy[ntheta//4:3*ntheta//4+1].sum()),
                              odd_frequency_energy=float(energy[1::2].sum()),
                              n2_cosine=(-0+2*coeff[2].real).tolist(),n2_sine=(-2*coeff[2].imag).tolist()))
    return dict(ntheta=ntheta,measure='equal ring weights, not physical volume',
                nonaxisymmetric_fraction=(nonaxi/total_energy if total_energy else None),
                n2_fraction=(n2/total_energy if total_energy else None),rings=rings)


def symmetry_diagnostics(forward, points):
    f=forward(points); fq=forward(points*Q)
    velocity=fq[:,:3]-f[:,:3]*Q
    pressure=fq[:,3]-f[:,3]
    Uden=stats(f[:,:3])['rms']; Pden=stats(f[:,3])['rms']
    extra={}
    # Improper reflections are only diagnostics of accidentally enforced restrictions.
    for name,S in [('x_reflection',np.array([-1.,1.,1.])),('y_reflection',np.array([1.,-1.,1.])),('z_reflection',np.array([1.,1.,-1.])),('full_inversion',-np.ones(3))]:
        fs=forward(points*S)
        extra[name]=term_relative(fs[:,:3]-f[:,:3]*S,[f[:,:3]])
    return dict(Q_velocity=stats(velocity),Q_pressure=stats(pressure),
                Q_velocity_relative=(stats(velocity)['rms']/Uden if Uden else None),
                Q_pressure_relative=(stats(pressure)['rms']/Pden if Pden else None),extra_symmetry_defects=extra)


def axis_diagnostics(forward, step=.002, order=4):
    z=np.linspace(-2,2,33)
    axis=np.column_stack([np.zeros(len(z)),np.zeros(len(z)),z])
    f,J,H=differentiate(forward,axis,step=step,order=order)
    records=[]
    theta=2*math.pi*np.arange(32)/32
    for r in [1e-1,3e-2,1e-2,3e-3,1e-3,3e-4,1e-4]:
        zz=np.repeat(z,len(theta)); tt=np.tile(theta,len(z))
        x=np.column_stack([r*np.cos(tt),r*np.sin(tt),zz]); ff=forward(x)
        fa=np.repeat(f,len(theta),axis=0); ja=np.repeat(J,len(theta),axis=0)
        dx=x-np.column_stack([np.zeros(len(x)),np.zeros(len(x)),zz])
        linear=np.einsum('nij,nj->ni',ja[:,:3],dx)
        horizontal=ff[:,:2]-fa[:,:2]-linear[:,:2]
        vertical=ff[:,2]-fa[:,2]
        records.append(dict(r=r,horizontal_cubic_remainder=stats(horizontal),
                            horizontal_remainder_div_r3=stats(horizontal/r**3),
                            vertical_quadratic_remainder=stats(vertical),
                            vertical_remainder_div_r2=stats(vertical/r**2)))
    offblock=np.column_stack([J[:,0,2],J[:,1,2],J[:,2,0],J[:,2,1]])
    return dict(axis_horizontal_velocity=stats(f[:,:2]),axis_jacobian_offblock=stats(offblock),
                axis_divergence=stats(np.trace(J[:,:3],axis1=1,axis2=2)),axis_curvature=stats(H[:,:3]),
                tubes=records,scope='finite z interval and sampled tubes; derivative convergence checked separately')


def exponent_sensitivity(x, r, c_l, C=0.):
    # Holding physical fields fixed. This is not an exponent refit of a profile family.
    G=-r['U']+np.einsum('nij,nj->ni',r['J'],x)
    gg=float(np.sum(G*G))
    offset=float(np.sum(r['momentum']*G))
    signal=stats(G)['rms']
    scale=stats(r['U'])['rms']
    identifiable=(gg>0 and signal>1e-8*scale)
    optimum=c_l-offset/gg if identifiable else None
    curve=[]
    for c in [c_l-.01,c_l-.005,c_l,c_l+.005,c_l+.01,.5]:
        rr=r['momentum']+(c-c_l)*G
        curve.append(dict(c_l=c,momentum=stats(rr)))
    return dict(method='fixed physical fields; analytic partial R_m/partial c_l = -U + y.grad U',
                fixed_field_least_squares_c_l=optimum,derivative_rms=signal,
                fixed_field_derivative_resolved=identifiable,
                original_gap_to_half=.5-c_l,curve=curve,
                verdict='OPEN: cannot establish a resolved free exponent without retraining/refinement')


def directional_dependence(r):
    J=r['J']
    gram=np.einsum('nij,nik->jk',J,J)/len(J)
    eig,vec=np.linalg.eigh(gram)
    trace=float(np.trace(gram))
    return dict(derivative_gram=gram.tolist(),eigenvalues=eig.tolist(),
                least_varying_direction=vec[:,0].tolist(),
                minimum_fraction=float(eig[0]/trace) if trace else None,
                interpretation='A small minimum may indicate near independence of a spatial direction on this sampled region.')


def vector_group_average(forward,points,nangle=128):
    """Correct SO(2) action: rotate points, evaluate, rotate vectors back."""
    original=forward(points)[:,:3]
    averaged=np.zeros_like(original);coarse=np.zeros_like(original)
    for index,alpha in enumerate(2*math.pi*np.arange(nangle)/nangle):
        ca,sa=np.cos(alpha),np.sin(alpha)
        rot=points.copy()
        rot[:,0]=ca*points[:,0]-sa*points[:,1]
        rot[:,1]=sa*points[:,0]+ca*points[:,1]
        U=forward(rot)[:,:3]
        pulled=U.copy()
        pulled[:,0]=ca*U[:,0]+sa*U[:,1]
        pulled[:,1]=-sa*U[:,0]+ca*U[:,1]
        averaged+=pulled/nangle
        if index%2==0:coarse+=pulled/(nangle//2)
    nonaxi=original-averaged
    energy=float(np.mean(np.sum(original*original,axis=1)))
    nonenergy=float(np.mean(np.sum(nonaxi*nonaxi,axis=1)))
    return dict(nangle=nangle,axisymmetric_part=stats(averaged),nonaxisymmetric_part=stats(nonaxi),
                nonaxisymmetric_energy_fraction=(nonenergy/energy if energy else None),
                angular_refinement_difference=stats(averaged-coarse),
                method='mean_alpha R_minus_alpha U(R_alpha y)',
                measure='same physical-volume core holdout points as input')


def volume_angular_spectra(forward,inner=0.,outer=1.,nrad=6,nmu=10,ntheta=64):
    """Cylindrical Fourier energies with physical ball/shell volume weights."""
    nodes,weights=np.polynomial.legendre.leggauss(nrad)
    rho=inner+(nodes+1)*(outer-inner)/2
    wr=weights*(outer-inner)/2*rho**2
    mu,wm=np.polynomial.legendre.leggauss(nmu)
    R,M=np.meshgrid(rho,mu,indexing='ij');W=(wr[:,None]*wm[None,:]).reshape(-1)
    radius=(R*np.sqrt(1-M*M)).reshape(-1);z=(R*M).reshape(-1)
    theta=2*math.pi*np.arange(ntheta)/ntheta
    rr=np.repeat(radius,ntheta);zz=np.repeat(z,ntheta);tt=np.tile(theta,len(z))
    points=np.column_stack([rr*np.cos(tt),rr*np.sin(tt),zz])
    f,J,_=differentiate(forward,points,step=.001,order=6,hessian=False)
    fields={'velocity':to_cylindrical(f[:,:3],tt),'vorticity':to_cylindrical(curl(J[:,:3]),tt)}
    # Remove one regional pressure constant for gauge-invariant modal energy ratios.
    pressure=f[:,3].reshape(-1,ntheta)
    pmean=float(np.sum(W*np.mean(pressure,axis=1))/np.sum(W))
    fields['pressure_minus_regional_mean']=(pressure-pmean).reshape(-1,1)
    output={}
    for name,values in fields.items():
        ringvalues=values.reshape(-1,ntheta,values.shape[-1])
        coeff=np.fft.fft(ringvalues,axis=1)/ntheta
        modal=2*math.pi*np.einsum('r,rk->k',W,np.sum(abs(coeff)**2,axis=-1))
        total=float(modal.sum());two=float(modal[2]+modal[-2])
        coarse=np.fft.fft(ringvalues[:,::2],axis=1)/(ntheta//2)
        coarsetotal=float(2*math.pi*np.einsum('r,rk->',W,np.sum(abs(coarse)**2,axis=-1)))
        output[name]=dict(physical_L2_squared=total,n2_energy=two,n2_fraction=two/total if total else None,
                          nonaxisymmetric_fraction=float(modal[1:].sum())/total if total else None,
                          modal_energies={str(k):float(modal[k]+(modal[-k] if k else 0)) for k in range(min(17,ntheta//2))},
                          odd_energy=float(modal[1::2].sum()),high_frequency_energy=float(modal[ntheta//4:3*ntheta//4+1].sum()),
                          coarse_theta_total_energy=coarsetotal,angular_total_energy_difference=abs(total-coarsetotal))
    return dict(inner_radius=inner,outer_radius=outer,physical_volume=4*math.pi*(outer**3-inner**3)/3,
                quadrature=dict(nrad=nrad,nmu=nmu,ntheta=ntheta),sample_count=len(points),pressure_regional_mean=pmean,
                fields=output,measure='Gauss quadrature rho^2 d_rho d_mu and periodic d_theta; full physical 3D volume',
                scope='finite quadrature, with angular subsampling comparison; radial/mu refinement remains a separate check')
