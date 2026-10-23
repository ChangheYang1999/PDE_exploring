"""Apply the independent direct full-plane kernel to many smooth basis fields.

This assembles linear velocity matrices from Cartesian source quadratures.
There is no modal Poisson solve or density differentiation in this inverse.
"""
import numpy as np
from scipy.special import betainc
from direct_inverse import DirectInverse,kernel_difference_scaled


class KernelBasis:
    def __init__(self,basis,config,batch=4096):
        self.basis=basis;self.q=DirectInverse(lambda x,y:0.,config);self.config=config;self.batch=batch

    def _accumulate(self,x,y,weights):
        x,y=np.broadcast_arrays(np.asarray(x),np.asarray(y))
        flatx=x.reshape(-1);flaty=y.reshape(-1)
        ww=np.broadcast_to(weights,x.shape+(2,)).reshape(-1,2)
        out=np.zeros((2,self.basis.size))
        for lo in range(0,len(flatx),self.batch):
            hi=min(lo+self.batch,len(flatx))
            out+=ww[lo:hi].T@self.basis.evaluate(flatx[lo:hi],flaty[lo:hi])
        return out

    def velocity_matrix(self,x,y):
        x=float(x);y=float(y);q=self.q
        mag=np.hypot(x,y);scale=max(self.config.length,mag)
        radius=self.config.outer_factor*scale;local=.5*scale
        if radius<=mag+local:raise ValueError('Invalid outer factor')
        b0=self.basis.evaluate(x,y)
        out=np.zeros((2,self.basis.size));out[1]=-b0/2
        half=self.config.angular//2
        rr=(local*q.t)[:,None];ex=q.ex[:half][None,:];ey=q.ey[:half][None,:]
        nearw=q.wt[:,None,None]/q.t[:,None,None]*q.k[None,:half,:]*q.dtheta
        # Pairing is performed before reduction to retain local cancellation.
        px=(x+rr*ex).reshape(-1);py=(y+rr*ey).reshape(-1)
        nx=(x-rr*ex).reshape(-1);ny=(y-rr*ey).reshape(-1)
        ww=np.broadcast_to(nearw,rr.shape[:1]+(half,2)).reshape(-1,2)
        for lo in range(0,len(px),self.batch):
            hi=min(lo+self.batch,len(px))
            vals=self.basis.evaluate(px[lo:hi],py[lo:hi])+self.basis.evaluate(nx[lo:hi],ny[lo:hi])-2*b0
            out+=ww[lo:hi].T@vals
        dot=x*q.ex+y*q.ey
        smax=-dot+np.sqrt(dot*dot+radius*radius-mag*mag)
        span=np.log(smax/local)
        rr=local*np.exp(q.mt[:,None]*span[None,:])
        mx=x+rr*q.ex[None,:];my=y+rr*q.ey[None,:]
        middlew=q.mw[:,None,None]*span[None,:,None]*q.k[None,:,:]*q.dtheta
        if mag>4*self.config.length:
            core=mag/2
            def cut(t):return 1-betainc(10,10,np.clip(2*t-1,0,1))
            middlew=middlew*(1-cut(np.hypot(mx,my)/core))[...,None]
            edges=[0.,min(self.config.length,core)]
            while edges[-1]<core:edges.append(min(2*edges[-1],core))
            for lo,hi in zip(edges[:-1],edges[1:]):
                cr=lo+(hi-lo)*q.t
                cx=cr[:,None]*q.ex[None,:];cy=cr[:,None]*q.ey[None,:]
                kw=kernel_difference_scaled(-cx/mag,-cy/mag,-x/mag,-y/mag)/(mag*mag)
                kw*=((hi-lo)*q.wt*cr*cut(cr/core))[:,None,None]*q.dtheta
                out+=self._accumulate(cx,cy,kw)
        out+=self._accumulate(mx,my,middlew)
        tail=max(radius,self.config.exterior_start);current=radius
        while current<tail:
            nxt=min(2*current,tail);step=np.log(nxt/current);cr=current*np.exp(q.t*step)
            kd=kernel_difference_scaled(x/cr[:,None],y/cr[:,None],q.ex[None,:],q.ey[None,:])
            out+=self._accumulate(cr[:,None]*q.ex[None,:],cr[:,None]*q.ey[None,:],kd*(step*q.wt)[:,None,None]*q.dtheta)
            current=nxt
        cr=tail*q.jt**(-q.power)
        kd=kernel_difference_scaled(x/cr[:,None],y/cr[:,None],q.ex[None,:],q.ey[None,:])
        weight=q.power*q.jw/q.jt**(1+q.beta)
        out+=self._accumulate(cr[:,None]*q.ex[None,:],cr[:,None]*q.ey[None,:],kd*weight[:,None,None]*q.dtheta)
        return out
