"""Finite nonlinear origin Taylor chart. NOT an infinite-tail certificate.
Coefficients store x^j y^(degree-j). Free parameter e_k multiplies x^(2k+1)y.
Parameters are scaled to the actual inner cutoff radius: e_k = physical_e_k*rmin^(2k).
"""
import numpy as np

def dx(p):
    p=np.asarray(p);return np.arange(1,len(p))*p[1:]
def dy(p):
    p=np.asarray(p);n=len(p)-1;return (n-np.arange(n))*p[:-1]
def bracket(p,r):
    return np.convolve(dx(p),dy(r))-np.convolve(dy(p),dx(r))

def origin_jets(c,a,free):
    free=np.asarray(free);dt=np.result_type(free,c,a,float)
    rho=[np.array([a,0],dtype=dt)]
    psi=[np.array([0,1-c,0],dtype=dt)]
    for k in range(1,len(free)+1):
        n=2*k+1
        rhs=np.zeros(n+1,dtype=dt)
        for i in range(1,k):rhs-=bracket(psi[i],rho[k-i])
        q=rhs[::2]
        lam=2*k+4*np.arange(k+1)*(c-1)
        e=np.zeros(k+1,dtype=dt);e[k]=free[k-1]
        for j in range(k-1,-1,-1):
            aa=(2*k-2*j+1)*(2*k-2*j)
            bb=(2*j+3)*(2*j+2)*(1-a/lam[j+1])
            e[j]=(-2*(j+1)*q[j+1]/lam[j+1]-bb*e[j+1])/aa
        d=(q-a*(2*np.arange(k+1)+1)*e)/lam
        rh=np.zeros(n+1,dtype=dt);rh[::2]=d
        ps=np.zeros(n+2,dtype=dt);ps[1::2]=e
        rho.append(rh);psi.append(ps)
    return rho,psi

def make_maps(prob,order):
    ct=np.cos(prob.theta);st=np.sin(prob.theta)
    ro=[];po=[]
    for k in range(order+1):
        n=2*k+1
        mon=np.array([ct**j*st**(n-j) for j in range(n+1)]).T
        ro.append(prob.Po@mon)
        m=n+1
        mon=np.array([ct**j*st**(m-j) for j in range(m+1)]).T
        po.append(prob.Pe@mon)
    return ro,po

def evaluate_origin(c,a,free,prob):
    order=len(free)
    key=('origin_maps',order)
    if not hasattr(prob,'_jet_maps'):prob._jet_maps={}
    if key not in prob._jet_maps:prob._jet_maps[key]=make_maps(prob,order)
    ro,po=prob._jet_maps[key]
    rho,psi=origin_jets(c,a,free)
    dt=np.result_type(c,a,free,float)
    y=np.zeros(3*prob.M,dtype=dt)
    for k in range(order+1):
        y[:prob.M]+=ro[k]@rho[k]
        g=po[k]@psi[k]
        y[prob.M:2*prob.M]+=g
        y[2*prob.M:]+=(2*k+2)*g
    return y
