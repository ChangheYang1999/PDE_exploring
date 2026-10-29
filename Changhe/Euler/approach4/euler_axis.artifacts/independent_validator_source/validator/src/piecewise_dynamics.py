"""Finite-search dynamics diagnostics independent of the optimization code."""
from __future__ import annotations
import numpy as np
from numpy.polynomial import Legendre
from scipy.optimize import brentq
from scipy.special import roots_legendre
from independent_identities import vorticity_and_jacobian


def transport(field,r,z):
    d=field.cylindrical(r,z,2);r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float))
    W=np.stack((field.c_l*r+d['U'][...,0],field.c_l*z+d['U'][...,2]),axis=-1)
    J=np.empty(W.shape+(2,));J[...,0,0]=field.c_l+d['ur_r'];J[...,0,1]=d['ur_z']
    J[...,1,0]=d['uz_r'];J[...,1,1]=field.c_l+d['uz_z']
    return W,J


def core_swirl_fraction(field,radius,*,nradial=24,nangle=64):
    mu,wm=roots_legendre(nangle);x,wx=roots_legendre(nradial)
    edges=[0.,*sorted(a for a in field.interfaces if 0<a<radius),float(radius)]
    total=0.;swirl=0.
    for lo,hi in zip(edges[:-1],edges[1:]):
        R=(lo+hi)/2+(hi-lo)*x/2;wr=(hi-lo)*wx/2
        U=field.cylindrical(R[:,None]*np.sqrt(1-mu*mu),R[:,None]*mu,2)['U']
        weights=2*np.pi*(R*R*wr)[:,None]*wm
        total+=float(np.sum(weights*np.sum(U*U,axis=-1)));swirl+=float(np.sum(weights*U[...,1]**2))
    return dict(radius=float(radius),nradial=nradial,nangle=nangle,total_velocity_squared_integral=total,
                swirl_velocity_squared_integral=swirl,s_core=float(np.sqrt(swirl/total)) if total>0 else None)


def far_swirl_fraction(field,*,nangle=128):
    rm=float(field.elements[-1]['Rlo']);polys=[]
    for name,power in [('phi',field.alpha),('q',field.alpha+1)]:
        hits=np.flatnonzero(abs(np.asarray(field.radial_keys[2,name])-power)<1e-12)
        if len(hits)!=1:raise ValueError('one exact leading column required')
        coeff=field.matrices[2,name][:,hits[0]]*rm**power*field.dilation**(field.alpha+1)
        polys.append(Legendre(coeff))
    A,B=polys;mu,w=roots_legendre(nangle);sin=np.sqrt(1-mu*mu)
    FR=2*mu*A(mu)-(1-mu*mu)*A.deriv()(mu);FV=(field.alpha-2)*sin*A(mu);FT=sin*B(mu)
    total=float(2*np.pi*np.dot(w,FR*FR+FV*FV+FT*FT));swirl=float(2*np.pi*np.dot(w,FT*FT))
    return dict(nangle=nangle,total_leading_squared_norm=total,swirl_leading_squared_norm=swirl,s_far=float(np.sqrt(swirl/total)))


def vorticity_maximum_identity(field,point):
    r,z=map(float,point);xyz=np.array([r,0.,z]);U,J=field.cartesian(xyz,True)
    omega,JO=vorticity_and_jacobian(field,xyz);W=field.c_l*xyz+U
    norm2=float(omega@omega);stretch=float(omega@J@omega);advection=float(omega@JO@W)
    curlM=omega+JO@W-J@omega;residual=float(omega@curlM)
    scale=max(norm2,abs(stretch),1e-300)
    return dict(point_r_z=[r,z],vorticity=omega.tolist(),vorticity_squared=norm2,
                stretching=stretch,advective_half_norm_derivative=advection,
                maximum_identity_defect=stretch-norm2,relative_maximum_identity_defect=abs(stretch-norm2)/scale,
                omega_dot_curl_residual=residual,algebraic_error=residual-(norm2+advection-stretch),
                gradient_half_vorticity_squared=(omega@JO).tolist(),
                global_maximum_proved=False,scope='Necessary identity evaluated at an independently detected maximum; finite search only.')


def root_inventory(field,a_eff,*,radial_seeds=25,angular_seeds=41,iterations=40):
    a=float(a_eff);Rmax=64*a;roots=[]
    def add(r,z,method):
        r=abs(float(r));z=float(z)
        if np.hypot(r,z)>Rmax*(1+1e-10):return
        if r<1e-7*a:r=0.
        if any(np.hypot(r-p['r'],z-p['z'])<1e-6*a for p in roots):return
        W,J=transport(field,r,z)
        if np.linalg.norm(W)>1e-8*max(a,1.):return
        d=field.cylindrical(r,z,3);red=field.reduced(r,z);eig=np.linalg.eigvals(J)
        axis=r==0.;v=float(d['ur_over_r']);q=float(d['q'][0,0]);eta=float(d['eta'])
        if axis:
            lr=float(J[0,0]);lz=float(J[1,1])
            if lr>0 and lz>0:kind='axis source P'
            elif lr>0 and lz<0:kind='axis saddle A'
            elif lr<0 and lz>0:kind='axis saddle B'
            else:kind='axis degenerate or other'
        else:
            if np.all(eig.real>0):kind='off-axis source O'
            elif np.prod(eig.real)<0:kind='off-axis saddle D'
            else:kind='off-axis degenerate or other'
        roots.append(dict(r=r,z=z,method=method,kind=kind,transport_norm=float(np.linalg.norm(W)),
                    jacobian=J.tolist(),eigenvalues=[[float(e.real),float(e.imag)] for e in eig],
                    q=q,eta=eta,ur_over_r=v,q_residual=float(red['q']),eta_residual=float(red['eta']),
                    S1_strain_defect=abs(v+.5) if axis and abs(q)>1e-10 else None,
                    axis_q_constraint=(1+2*v)*q if axis else None,
                    off_axis_q_constraint=(1-2*field.c_l)*q if not axis else None,
                    jacobian_asymmetry=float(np.max(np.abs(J-J.T))),
                    nearest_interface_distance=float(np.min(np.abs(field.interfaces-np.hypot(r,z)),initial=np.inf)) if len(field.interfaces) else None))
    positive=a*np.geomspace(2**-18,64,257)
    axis_grid=np.unique(np.r_[-positive[::-1],np.linspace(-4*a,4*a,257),positive])
    values=transport(field,np.zeros_like(axis_grid),axis_grid)[0][:,1]
    for i in range(len(axis_grid)-1):
        if values[i]==0:add(0.,axis_grid[i],'axis exact scan node')
        if values[i]*values[i+1]<0:
            zz=brentq(lambda zz:float(transport(field,0.,zz)[0][1]),axis_grid[i],axis_grid[i+1],xtol=2e-13)
            add(0.,zz,'axis sign bracket')
    if values[-1]==0:add(0.,axis_grid[-1],'axis exact scan node')
    radii=a*np.geomspace(2**-8,64,radial_seeds);theta=np.linspace(.001,np.pi-.001,angular_seeds)
    points=np.stack(np.broadcast_arrays(radii[:,None]*np.sin(theta),radii[:,None]*np.cos(theta)),axis=-1).reshape(-1,2)
    active=np.ones(len(points),dtype=bool);completed=0
    for iteration in range(iterations):
        if not np.any(active):break
        ids=np.flatnonzero(active);x=points[ids];W,J=transport(field,x[:,0],x[:,1]);norm=np.linalg.norm(W,axis=1)
        done=norm<=1e-10*max(1.,a)
        for point in x[done]:add(*point,'batched two-dimensional Newton')
        completed+=int(np.sum(done));active[ids[done]]=False
        ids=ids[~done];x=x[~done];W=W[~done];J=J[~done]
        if not len(ids):continue
        det=J[:,0,0]*J[:,1,1]-J[:,0,1]*J[:,1,0];valid=np.isfinite(det)&(np.abs(det)>1e-14)
        active[ids[~valid]]=False;ids=ids[valid];x=x[valid];W=W[valid];J=J[valid];det=det[valid]
        step=np.column_stack(((J[:,1,1]*W[:,0]-J[:,0,1]*W[:,1])/det,(-J[:,1,0]*W[:,0]+J[:,0,0]*W[:,1])/det))
        limit=np.maximum(a,0.8*np.linalg.norm(x,axis=1));factor=np.minimum(1.,limit/np.maximum(np.linalg.norm(step,axis=1),1e-300))
        x=x-step*factor[:,None];x[:,0]=np.abs(x[:,0]);finite=np.all(np.isfinite(x),axis=1)
        active[ids[~finite]]=False;points[ids[finite]]=x[finite]
    for point in points[active]:add(*point,'final Newton iterate')
    roots.sort(key=lambda p:(p['r']!=0.,p['z'],p['r']))
    return dict(search_radius=Rmax,axis_grid_points=len(axis_grid),radial_seeds=radial_seeds,angular_seeds=angular_seeds,
                total_off_axis_seeds=len(points),converged_off_axis_seed_count=completed,iterations=iteration+1,
                roots=roots,all_roots_certified=False,
                scope='Multiscale axis bracketing and dense batched Newton. Tangent or unresolved roots can be missed; no complete global portrait is proved.')


def axis_branches(field,inventory,a_eff,*,points_per_branch=256):
    axis=sorted((p for p in inventory['roots'] if p['r']==0.),key=lambda p:p['z']);rows=[];Rmax=inventory['search_radius']
    for i,root in enumerate(axis):
        if root['kind']!='axis source P' or abs(root['q'])<1e-10:continue
        z0=root['z'];q0=root['q']
        for direction in [-1,1]:
            j=i+direction;end=axis[j]['z'] if 0<=j<len(axis) else direction*Rmax
            fraction=np.geomspace(2**-18,1,points_per_branch)
            if 0<=j<len(axis):fraction[-1]=1-1e-9
            z=z0+(end-z0)*fraction;d=field.cylindrical(np.zeros_like(z),z,3);q=d['q'][0,0]
            Wz=field.c_l*z+d['U'][:,2];lhs=Wz*d['eta'];rhs=2*q*(q-q0);defect=lhs-rhs;scale=float(np.max(np.abs(rhs)))
            rows.append(dict(source_z=z0,source_q=q0,direction=direction,end_z=end,
                         reaches_next_detected_axis_zero=0<=j<len(axis),point_count=len(z),z=z.tolist(),
                         lhs=lhs.tolist(),rhs=rhs.tolist(),defect=defect.tolist(),
                         max_absolute_defect=float(np.max(np.abs(defect))),reference_scale=scale,
                         relative_defect=float(np.max(np.abs(defect))/scale) if scale>0 else None,
                         q_sample_min=float(np.min(q)),q_sample_max=float(np.max(q))))
    return dict(branches=rows,scope='Finite branches out to 64 a_eff or the next detected root. No infinite-axis limit or root completeness is certified.')
