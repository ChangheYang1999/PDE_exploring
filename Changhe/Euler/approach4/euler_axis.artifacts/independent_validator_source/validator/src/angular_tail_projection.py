"""Orthogonal fixed-leading-field projection of a first velocity correction."""
import numpy as np
from scipy.special import eval_gegenbauer,eval_legendre


def columns(p,mu,degree):
    mu=np.asarray(mu);s=np.sqrt(1-mu*mu);stream=[];swirl=[];D=[];E=[]
    for j in range(degree+1):
        k=j+1;C=eval_gegenbauer(j,1.5,mu)
        stream.append(np.stack((k*(k+1)*eval_legendre(k,mu),(p-2)*s*C,np.zeros_like(mu)),axis=-1))
        swirl.append(np.stack((np.zeros_like(mu),np.zeros_like(mu),s*C),axis=-1))
        e=4*np.pi*k*(k+1)/(2*k+1);E.append(e);D.append(e*(k*(k+1)+(p-2)**2))
    return np.array(stream),np.array(swirl),np.array(D),np.array(E)


def project(p,mu,w,G,degree_A,degree_B,H=None):
    if min(degree_A,degree_B)<0:raise ValueError('nonnegative degree limits required')
    mu=np.asarray(mu);w=np.asarray(w);G=np.asarray(G)
    va,vb,da,db=columns(p,mu,max(degree_A,degree_B))
    va=va[:degree_A+1];vb=vb[:degree_B+1];da=da[:degree_A+1];db=db[:degree_B+1]
    a=2*np.pi*np.einsum('i,jik,ik->j',w,va,G)/da
    b=2*np.pi*np.einsum('i,jik,ik->j',w,vb,G)/db
    projection=np.einsum('j,jik->ik',a,va)+np.einsum('j,jik->ik',b,vb)
    def square(V):return float(2*np.pi*np.sum(w[:,None]*V*V))
    total=square(G);missing=square(G-projection)
    result=dict(degree_A=degree_A,degree_B=degree_B,projection_A_gegenbauer=a.tolist(),projection_B_gegenbauer=b.tolist(),
        G_norm=total**.5,omitted_norm=missing**.5,omitted_relative_norm=None if total==0 else (missing/total)**.5,
        orthogonality_max=float(max(np.max(abs(2*np.pi*np.einsum('i,jik,ik->j',w,va,G-projection))),np.max(abs(2*np.pi*np.einsum('i,jik,ik->j',w,vb,G-projection))))))
    if H is not None:
        error=square(np.asarray(H)-G);represented=square(np.asarray(H)-projection)
        result.update(saved_mismatch_norm=error**.5,represented_mismatch_norm=represented**.5,
            pythagoras_defect=error-missing-represented,omitted_fraction_of_squared_mismatch=None if error==0 else missing/error)
    return result
