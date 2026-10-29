"""Finite multistart zero inventory and reflected boundary-degree diagnostics.

No numerical search here certifies completeness. Exact topology is available
separately for the seed family through ring_seed_certificate.py.
"""
import numpy as np
from scipy.optimize import brentq,root,minimize_scalar
from scipy.ndimage import minimum_filter

def transport(field,r,z,jacobian=False):
    d=field.cylindrical(r,z,2);W=field.c_l*np.stack(np.broadcast_arrays(r,z),axis=-1)+d['U'][...,[0,2]]
    if not jacobian:return W
    J=np.empty(W.shape[:-1]+(2,2));J[...,0,0]=field.c_l+d['ur_r'];J[...,0,1]=d['ur_z'];J[...,1,0]=d['uz_r'];J[...,1,1]=field.c_l+d['uz_z']
    return W,J

def winding(values):
    v=values[...,0]+1j*values[...,1]
    if np.any(abs(v)<1e-14):return None
    return float(np.sum(np.angle(np.roll(v,-1)/v))/(2*np.pi))

def inventory(field,*,radius=32.,inner_radius=1e-4,nradial=97,nangle=129,max_starts=64,root_tolerance=1e-9):
    R=float(radius);roots=[]
    def add(r,z):
        r=abs(float(r));z=float(z)
        if np.hypot(r,z)>R or not np.isfinite(r+z):return
        if r<1e-7:r=0.
        W,J=transport(field,r,z,True)
        if np.linalg.norm(W)>root_tolerance*(1+np.hypot(r,z)):return
        if any(np.hypot(r-v['r'],z-v['z'])<1e-6*(1+np.hypot(r,z)) for v in roots):return
        ev=np.linalg.eigvals(J);det=float(np.linalg.det(J));d=field.cylindrical(r,z,3);q=float(d['q'][0,0])
        tolerance=1e-7*max(1.,float(np.linalg.norm(J)))
        if r==0:
            lr,lz=float(J[0,0]),float(J[1,1])
            label='P' if min(lr,lz)>tolerance else 'A' if lr>tolerance and lz<-tolerance else 'B' if lr<-tolerance and lz>tolerance else 'unresolved'
        else:label='O' if det>tolerance and np.min(ev.real)>tolerance else 'D' if det<-tolerance else 'unresolved'
        gradgamma=np.array([2*r*q+2*r**3*d['q'][1,0],r*r*d['q'][0,1]],dtype=float)
        resonance=gradgamma@J-(2*field.c_l-1)*gradgamma
        red=field.reduced(r,z)
        distance=min([abs(np.hypot(r,z)-a) for a in getattr(field,'interfaces',[])],default=float('inf'))
        roots.append(dict(r=r,z=z,location='axis' if r==0 else 'off_axis',classification=label,
            transport_norm=float(np.linalg.norm(W)),jacobian=J.tolist(),determinant=det,
            eigenvalues=[[float(v.real),float(v.imag)] for v in ev],index=int(np.sign(det)) if abs(det)>tolerance else None,
            q=q,eta=float(d['eta']),phi_z=float(d['phi'][0,1]),q_residual=float(red['q']),eta_residual=float(red['eta']),
            circulation_gradient=gradgamma.tolist(),linear_circulation_resonance_defect=resonance.tolist(),
            near_interface=bool(distance<1e-6*max(1.,R)),
            axis_S1_strain_defect=float(d['phi'][0,1]-.5) if r==0 and abs(q)>1e-10 else None))
    rr=np.geomspace(inner_radius,R,nradial)
    zz=np.r_[-rr[::-1],0.,rr]
    aw=transport(field,np.zeros_like(zz),zz)[:,1]
    for j in range(len(zz)-1):
        if aw[j]==0:add(0.,zz[j])
        if aw[j]*aw[j+1]<0:
            add(0.,brentq(lambda t:transport(field,0.,t)[1],zz[j],zz[j+1],xtol=1e-13))
    if aw[-1]==0:add(0.,zz[-1])
    # Near-zero local minima can reveal even-multiplicity roots, but cannot
    # certify that other degenerate roots are absent.
    for j in range(1,len(zz)-1):
        if abs(aw[j])<min(abs(aw[j-1]),abs(aw[j+1])) and abs(aw[j])<1e-3:
            opt=minimize_scalar(lambda t:transport(field,0.,t)[1]**2,bounds=(zz[j-1],zz[j+1]),method='bounded',options={'xatol':1e-13})
            add(0.,opt.x)
    theta=np.linspace(.002,np.pi-.002,nangle);rad,ang=np.meshgrid(rr,theta,indexing='ij')
    rg=rad*np.sin(ang);zg=rad*np.cos(ang);W=transport(field,rg,zg);measure=np.linalg.norm(W,axis=-1)/(1+rad)
    local=(measure==minimum_filter(measure,size=3,mode='nearest'))
    starts=[(float(rg[i,j]),float(zg[i,j]),float(measure[i,j])) for i,j in zip(*np.nonzero(local))]
    vc=W[...,0]+1j*W[...,1];corners=np.stack([vc[:-1,:-1],vc[1:,:-1],vc[1:,1:],vc[:-1,1:]],axis=-1)
    wind=np.sum(np.angle(np.roll(corners,-1,axis=-1)/corners),axis=-1)/(2*np.pi)
    for i,j in zip(*np.nonzero(abs(wind)>.5)):
        starts.append((float((rg[i,j]+rg[i+1,j+1])/2),float((zg[i,j]+zg[i+1,j+1])/2),float(measure[i,j])))
    starts.sort(key=lambda t:t[2]);attempts=[]
    for r0,z0,_ in starts[:max_starts]:
        ans=root(lambda x:transport(field,x[0],x[1]),[r0,z0],jac=lambda x:transport(field,x[0],x[1],True)[1],options={'maxfev':100,'xtol':1e-10})
        if np.all(np.isfinite(ans.x)):add(*ans.x)
        attempts.append(dict(start=[r0,z0],result=ans.x.tolist(),success=bool(ans.success)))
    angle=np.linspace(0,2*np.pi,4*nangle,endpoint=False);boundary=transport(field,R*np.cos(angle),R*np.sin(angle))
    counts={k:sum(x['classification']==k for x in roots) for k in ['P','A','B','O','D','unresolved']}
    index_sum=sum(v['index']*(1 if v['location']=='axis' else 2) for v in roots if v['index'] is not None)
    return dict(radius=R,inner_radius=inner_radius,nradial=nradial,nangle=nangle,roots=sorted(roots,key=lambda x:(x['r'],x['z'])),counts=counts,
        reflected_index_sum=index_sum,boundary_winding=winding(boundary),boundary_min_norm=float(np.min(np.linalg.norm(boundary,axis=-1))),
        attempts=attempts,grid_winding_cells=int(np.sum(abs(wind)>.5)),
        completeness_proved=False,scope='Finite numerical inventory. Boundary winding is sampled. Missing roots or small hyperbolic eigenvalues remain possible; exact parameter/source theorems require separate hypotheses.')
