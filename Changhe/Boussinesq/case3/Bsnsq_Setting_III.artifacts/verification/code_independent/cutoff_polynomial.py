"""Adversarial manufactured field: exact B2 polynomial inside a smooth cutoff.

It is a compactly supported, correctly inverted field, not a B2 solution.
Its transported-equation defect is deliberately outside the observation disk.
"""
import numpy as np


def cutoff(s):
    s=np.asarray(s,dtype=float)
    c=np.zeros_like(s);cp=np.zeros_like(s);cpp=np.zeros_like(s)
    c[s<=1]=1
    active=(s>1)&(s<4)
    z=s[active]
    D=-1/(z-1)+1/(4-z)
    A=1/(z-1)**2+1/(4-z)**2
    Ap=-2/(z-1)**3+2/(4-z)**3
    e=np.exp(-np.abs(D));cc=np.where(D>=0,e/(1+e),1/(1+e));p=e/(1+e)**2
    c[active]=cc;cp[active]=-p*A;cpp[active]=p*((1-2*cc)*A*A-Ap)
    return c,cp,cpp


class CutoffPolynomial:
    def __init__(self,radius,beta=3.,a0=1.,v0=1.):
        self.radius=radius;self.beta=beta;self.a0=a0;self.v0=v0
        self.c=1+beta/2;self.b=4*a0/beta

    def ingredients(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
        rr=x*x+y*y;R2=self.radius**2
        C,Cp,Cpp=cutoff(rr/R2)
        P=self.c*x*y-self.b*x**3/6+self.v0*x
        Px=self.c*y-self.b*x*x/2+self.v0;Py=self.c*x
        Cx=2*x/R2*Cp;Cy=2*y/R2*Cp
        lapC=4/R2*Cp+4*rr/(R2*R2)*Cpp
        return x,y,C,P,Px,Py,Cx,Cy,lapC

    def psi(self,x,y):
        x,y,C,P,Px,Py,Cx,Cy,lapC=self.ingredients(x,y)
        return C*P

    def theta(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
        return self.a0*x*x*cutoff((x*x+y*y)/self.radius**2)[0]

    def omega(self,x,y):
        x,y,C,P,Px,Py,Cx,Cy,lapC=self.ingredients(x,y)
        return C*self.b*x-2*(Cx*Px+Cy*Py)-P*lapC

    def velocity(self,points,relative=True):
        p=np.asarray(points);x,y,C,P,Px,Py,Cx,Cy,lapC=self.ingredients(p[:,0],p[:,1])
        return np.column_stack((-(C*Py+Cy*P),C*Px+Cx*P-(self.v0 if relative else 0)))
