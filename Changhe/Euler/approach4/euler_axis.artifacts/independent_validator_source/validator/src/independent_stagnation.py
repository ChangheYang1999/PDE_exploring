"""Local necessary-condition diagnostics; numerical roots are not certified."""
from __future__ import annotations
import numpy as np
from scipy.optimize import root,brentq


def evaluate_transport(field,r,z):
    d=field.cylindrical(r,z,2)
    ur,ut,uz=d['U']
    W=np.array([field.c_l*r+ur,field.c_l*z+uz])
    J=np.array([[field.c_l+d['ur_r'],d['ur_z']],[d['uz_r'],field.c_l+d['uz_z']]])
    return W,J


def stagnation_audit(field,search_radius=16.):
    R=float(search_radius);roots=[]
    zs=np.linspace(-R,R,257)
    axis=np.asarray(field.c_l*zs+field.cylindrical(np.zeros_like(zs),zs,2)['U'][:,2])
    def add(r,z,kind):
        r=abs(float(r));z=float(z)
        if any(np.hypot(r-e['r'],z-e['z'])<1e-6 for e in roots):return
        W,J=evaluate_transport(field,r,z)
        if np.linalg.norm(W)>1e-7 or r>R or abs(z)>R:return
        d=field.cylindrical(r,z);red=field.reduced(r,z)
        eig=np.linalg.eigvals(J)
        q=float(d['q'][0,0]);eta=float(d['eta'])
        roots.append({'r':r,'z':z,'kind':kind,'transport_norm':float(np.linalg.norm(W)),
                      'q':q,'eta':eta,'phi_z':float(d['phi'][0,1]),'Uz_z':float(d['uz_z']),
                      'q_equation_residual':float(red['q']),'eta_equation_residual':float(red['eta']),
                      'meridional_eigenvalues':[[float(e.real),float(e.imag)] for e in eig],
                      'off_axis_swirl_obstruction':float((1-2*field.c_l)*q) if kind=='off-axis' else None,
                      'axis_q_compatibility':float((1-2*d['phi'][0,1])*q) if kind=='axis' else None})
    for k in range(len(zs)-1):
        if axis[k]==0:add(0.,zs[k],'axis')
        elif axis[k]*axis[k+1]<0:
            zz=brentq(lambda z:evaluate_transport(field,0.,z)[0][1],zs[k],zs[k+1],xtol=1e-13)
            add(0.,zz,'axis')
    for r0 in [.1,.5,1.5,4.]:
        for z0 in [-4.,-1.,0.,1.,4.]:
            def fun(x):return evaluate_transport(field,x[0],x[1])[0]
            def jac(x):return evaluate_transport(field,x[0],x[1])[1]
            answer=root(fun,[r0,z0],jac=jac,options={'maxfev':100,'xtol':1e-10})
            if abs(answer.x[0])>1e-6:add(*answer.x,'off-axis')
    return {'search_radius':R,'roots':roots,'scope':'Uncertified finite root search. Necessary conditions are exact only at an exact root of an exact profile.'}
