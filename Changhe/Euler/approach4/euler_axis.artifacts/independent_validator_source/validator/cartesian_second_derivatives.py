"""Cartesian velocity Hessian from regular (s,z) potential derivatives."""
import numpy as np

def scalar_cartesian(x,y,fs,fz,fss,fsz,fzz):
    shape=np.broadcast_shapes(np.shape(x),np.shape(y),np.shape(fs))
    g=np.empty(shape+(3,));H=np.empty(shape+(3,3))
    g[...,0]=2*x*fs;g[...,1]=2*y*fs;g[...,2]=fz
    H[...,0,0]=2*fs+4*x*x*fss;H[...,1,1]=2*fs+4*y*y*fss
    H[...,0,1]=H[...,1,0]=4*x*y*fss
    H[...,0,2]=H[...,2,0]=2*x*fsz;H[...,1,2]=H[...,2,1]=2*y*fsz;H[...,2,2]=fzz
    return g,H

def velocity_hessian(field,xyz):
    xyz=np.asarray(xyz,dtype=float);x,y,z=np.moveaxis(xyz,-1,0);s=x*x+y*y
    p=field.phi.jet(s,z,3);q=field.q.jet(s,z,2)
    ga,ha=scalar_cartesian(x,y,p[1,1],p[0,2],p[2,1],p[1,2],p[0,3])
    gb,hb=scalar_cartesian(x,y,q[1,0],q[0,1],q[2,0],q[1,1],q[0,2])
    _,hc=scalar_cartesian(x,y,4*p[1,0]+2*s*p[2,0],2*p[0,1]+2*s*p[1,1],
                         6*p[2,0]+2*s*p[3,0],4*p[1,1]+2*s*p[2,1],2*p[0,2]+2*s*p[1,2])
    eye=np.eye(3)
    def product(k,value,g,h):
        return value[...,None,None]*h+eye[k,:,None]*g[...,None,:]+g[..., :,None]*eye[k,None,:]
    return np.stack((-product(0,x,ga,ha)-product(1,y,gb,hb),
                     -product(1,y,ga,ha)+product(0,x,gb,hb),hc),axis=-3)
