"""Exact full-plane contribution from |source|>R using fourfold parity."""
import numpy as np
from numpy.polynomial.legendre import leggauss


def exterior_velocity_and_strain(omega,targets,radius,tail_power,order=96):
    targets=np.atleast_2d(np.asarray(targets,float))
    if radius<=np.max(np.linalg.norm(targets,axis=1)):
        raise ValueError('Exterior source disk must contain every target strictly')
    if tail_power<=0:raise ValueError('Positive decay power required')
    node,weight=leggauss(order)
    t=(node+1)/2;wt=weight/2
    phi=(node+1)*np.pi/4;wp=weight*np.pi/4
    r=radius*np.exp(-np.log1p(-t)/tail_power)
    dr=r/(tail_power*(1-t))
    a=r[:,None]*np.cos(phi)[None,:]
    b=r[:,None]*np.sin(phi)[None,:]
    w=a+1j*b
    field=omega(np.stack([a,b],axis=-1))
    measure=wt[:,None]*wp[None,:]*r[:,None]*dr[:,None]
    # c=(4/pi) int_Q ab Omega / |w|^4 dA. The grouped form avoids r^4 overflow.
    strain=(4/np.pi)*np.sum(wt[:,None]*wp[None,:]*
             np.cos(phi)[None,:]*np.sin(phi)[None,:]*field*dr[:,None]/r[:,None])
    velocities=[]
    for x,y in targets:
        z=complex(x,y)
        denom=np.conj((z*z-w*w)*(z*z-np.conj(w)**2))
        kernel=(-4/np.pi)*a*b*np.conj(z)/denom
        value=np.sum(measure*kernel*field)
        velocities.append([value.real,value.imag])
    return np.array(velocities),float(strain)
