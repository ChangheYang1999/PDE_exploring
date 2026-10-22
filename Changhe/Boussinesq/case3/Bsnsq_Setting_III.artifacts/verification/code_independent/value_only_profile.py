"""Read a rational coefficient file without importing its fitting basis code.

Values use the displayed monomial/radial-power formula. Vorticity uses a
separately derived closed-form Laplacian. Field differentiation for PDE
checks belongs to finite_difference.py, not this module.
"""
import json
from pathlib import Path
import numpy as np


class ValueProfile:
    def __init__(self,data,extended=True):
        if data['format']!='verification-rational-v1':
            raise ValueError('unsupported coefficient format')
        self.data=data
        self.beta=float(data['beta'])
        self.dtype=np.longdouble if extended else np.float64
        self.psi_terms=data['psi_terms'];self.theta_terms=data['theta_terms']
        self.psi_coeff=data['psi_coeff'];self.theta_coeff=data['theta_coeff']

    @classmethod
    def load(cls,path,extended=True):
        return cls(json.loads(Path(path).read_text()),extended)

    def field(self,x,y,kind):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=self.dtype),np.asarray(y,dtype=self.dtype))
        r2=x*x+y*y
        out=np.zeros(x.shape,dtype=self.dtype)
        xp={0:np.ones_like(x)};yp={0:np.ones_like(y)}
        max_power=max(t['i']+t['j'] for t in self.psi_terms+self.theta_terms)
        for n in range(1,max_power+1):
            xp[n]=xp[n-1]*x;yp[n]=yp[n-1]*y
        radial={}
        istheta=kind=='theta'
        terms=self.theta_terms if istheta else self.psi_terms
        coefficients=self.theta_coeff if istheta else self.psi_coeff
        for term,coefficient in zip(terms,coefficients):
            i,j=term['i'],term['j'];L=self.dtype(term['scale']);k=term['tail_order']
            target=self.dtype(1)-(k+1)/self.dtype(self.beta) if istheta else self.dtype(2)-k/self.dtype(self.beta)
            q=(target-i-j)/2
            amp=1 if istheta else 2
            C=self.dtype(coefficient)*L**(amp-i-j)
            S=1+r2/(L*L)
            def power(shift):
                key=(L,k,i+j+2*shift)
                if key not in radial:radial[key]=S**(q-shift)
                return radial[key]
            m=xp[i]*yp[j]
            if kind!='omega':
                out+=C*m*power(0)
            else:
                lap_poly=np.zeros(x.shape,dtype=self.dtype)
                if i>=2:lap_poly+=i*(i-1)*xp[i-2]*yp[j]
                if j>=2:lap_poly+=j*(j-1)*xp[i]*yp[j-2]
                out-=C*(lap_poly*power(0)+4*q*(i+j+1)/(L*L)*m*power(1)
                         +4*q*(q-1)/(L**4)*m*r2*power(2))
        return out

    def psi(self,x,y):return self.field(x,y,'psi')
    def theta(self,x,y):return self.field(x,y,'theta')
    def omega(self,x,y):return self.field(x,y,'omega')

    def center(self):
        a=c=b=v=self.dtype(0)
        for term,coeff in zip(self.theta_terms,self.theta_coeff):
            if term['i']==2 and term['j']==0:a+=self.dtype(coeff)/term['scale']
        for term,coeff in zip(self.psi_terms,self.psi_coeff):
            i,j,L,k=term['i'],term['j'],self.dtype(term['scale']),term['tail_order']
            C=self.dtype(coeff)*L**(2-i-j)
            q=(self.dtype(2)-k/self.dtype(self.beta)-i-j)/2
            if (i,j)==(1,1):c+=C
            if (i,j)==(3,0):b-=6*C
            if (i,j)==(1,2):b-=2*C
            if (i,j)==(1,0):
                b-=8*C*q/L**2
                v+=C
        return {'a0':float(a),'c':float(c),'b0':float(b),'stream_v0':float(v),
                'a0_error':float(a-1),'c_error':float(c-(1+self.beta/2)),
                'b0_error':float(b-4/self.beta)}
