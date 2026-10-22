"""X3 from exact JSON, own de Boor recurrence, no original evaluator imported.

Floating point exploration only. The compact strain integral represents the
formula on the entire plane without an exterior replacement.
"""
from pathlib import Path
import json
import numpy as np

BASE=Path(__file__).resolve().parents[3]

class X3:
    def __init__(self,path=None):
        d=json.loads(Path(path or BASE/'data_exact/x3.json').read_text())
        self.data=d
        for name,h in d['scalars_hex'].items():setattr(self,name,float.fromhex(h))
        for name,v in d['integers'].items():setattr(self,name,v)
        self.t=np.array([float.fromhex(h) for h in d['spline_knots_hex']])
        z=np.array([float.fromhex(h) for h in d['z_hex']])
        assert z[0]==self.k
        self.co=np.concatenate([np.zeros((self.angular+1,1)),z[1:1+(self.angular+1)*self.degree].reshape(self.angular+1,self.degree)],axis=1).T
        self.tc=z[-self.singular:]
        self.m=np.arange(self.angular+1)
        self.powers=np.maximum(self.m-1,0)
        self.p=6+2*self.k/(2-self.k)
        self.b=2/(1-self.k)
        self.dco=self.spline_order*np.diff(self.co,axis=0)/(self.t[self.spline_order+1:-1]-self.t[1:-self.spline_order-1])[:,None]

    @staticmethod
    def deboor(q, knots, coefficients, degree):
        q=np.atleast_1d(np.asarray(q,dtype=float))
        if np.any((q<0)|(q>1)):raise ValueError('q outside [0,1]')
        span=np.searchsorted(knots,q,side='right')-1
        span=np.clip(span,degree,len(coefficients)-1)
        out=coefficients[span[:,None]-degree+np.arange(degree+1)[None,:]].copy()
        for lev in range(1,degree+1):
            for j in range(degree,lev-1,-1):
                idx=span-degree+j
                alpha=(q-knots[idx])/(knots[idx+degree-lev+1]-knots[idx])
                out[:,j]=(1-alpha[:,None])*out[:,j-1]+alpha[:,None]*out[:,j]
        return out[:,-1]

    def radial(self,q,derivatives=False):
        q=np.atleast_1d(np.asarray(q,dtype=float))
        with np.errstate(divide='ignore'):
            s=-np.expm1(self.b*np.log1p(-q))
        chi=s/(s+self.origin_radius**2*(1-s))
        bs=self.deboor(q,self.t,self.co,self.spline_order)
        mult=chi[:,None]**self.powers
        rad=bs*mult
        tc=np.polynomial.chebyshev.chebval(2*q-1,self.tc)
        sg=s**(self.p/2)*tc
        if not derivatives:return rad,sg
        # t=log(u), q_t=(1-k)*s*(1-q).
        qt=(1-self.k)*s*(1-q)
        bst=self.deboor(q,self.t[1:-1],self.dco,self.spline_order-1)*qt[:,None]
        radt=(bst+2*self.powers*(1-chi[:,None])*bs)*mult
        tcd=np.polynomial.chebyshev.chebval(2*q-1,np.polynomial.chebyshev.chebder(self.tc))
        sgt=self.p*(1-s)*sg+2*s**(self.p/2)*tcd*qt
        return rad,sg,radt,sgt

    def compact(self,q,theta,derivatives=False):
        theta=np.atleast_1d(np.asarray(theta,dtype=float))
        ct=np.cos(theta);st=np.sin(theta)
        ang=np.cos(2*self.m[:,None]*theta)
        sing=np.abs(ct)**(self.p-2)*st**2
        if not derivatives:
            rad,sg=self.radial(q)
            return rad@ang+sg[:,None]*sing
        rad,sg,radt,sgt=self.radial(q,True)
        singp=2*np.abs(ct)**(self.p-2)*st*ct-(self.p-2)*np.abs(ct)**(self.p-3)*np.sign(ct)*st**3
        S=rad@ang+sg[:,None]*sing
        St=radt@ang+sgt[:,None]*sing
        Sa=rad@(-2*self.m[:,None]*np.sin(2*self.m[:,None]*theta))+sg[:,None]*singp
        return S,St,Sa

    def polar(self,r,theta):
        r=np.atleast_1d(np.asarray(r,dtype=float));theta=np.atleast_1d(np.asarray(theta,dtype=float))
        u=r/self.L;ell=np.log1p(u*u)
        q=-np.expm1(-(1-self.k)*ell/2)
        S,St,Sa=self.compact(q,theta,True)
        H=(self.k-3)*ell[:,None]/2+S
        Ht=(self.k-3)*(u*u/(1+u*u))[:,None]+St
        ct=np.cos(theta);st=np.sin(theta)
        angular=ct**2*st;angular_prime=ct**3-2*ct*st**2
        factor=r[:,None]**3*np.exp(H)
        rho=factor*angular
        rhot=(3+Ht)*rho
        rhoa=factor*(angular_prime+angular*Sa)
        rx=(rhot*ct-rhoa*st)/r[:,None]
        ry=(rhot*st+rhoa*ct)/r[:,None]
        return {'rho':rho,'rho_t':rhot,'rho_a':rhoa,'rho_x':rx,'rho_y':ry,'H':H}
