"""Raw generating-function differentiation through order five.

All coefficients are exact dyadics from the frozen file. Physical derivatives
use a separate second-order dual algebra. No numerical-lane code is imported.
"""
import mpmath as mp
import numpy as np


def exact(value):
    n, d = value.as_integer_ratio()
    return mp.mpf(n)/d


class Jet2:
    def __init__(self, v, x=0, e=0, xx=0, xe=0, ee=0):
        self.v, self.x, self.e, self.xx, self.xe, self.ee = map(mp.mpf, (v,x,e,xx,xe,ee))

    @staticmethod
    def cast(v):
        return v if isinstance(v,Jet2) else Jet2(v)

    def __add__(self,b):
        b=self.cast(b)
        return Jet2(*(getattr(self,k)+getattr(b,k) for k in ('v','x','e','xx','xe','ee')))
    __radd__=__add__
    def __neg__(self):
        return Jet2(*(-getattr(self,k) for k in ('v','x','e','xx','xe','ee')))
    def __sub__(self,b):
        return self+-self.cast(b)
    def __rsub__(self,b):
        return self.cast(b)+-self
    def __mul__(self,b):
        b=self.cast(b)
        return Jet2(self.v*b.v, self.x*b.v+self.v*b.x, self.e*b.v+self.v*b.e,
                    self.xx*b.v+2*self.x*b.x+self.v*b.xx,
                    self.xe*b.v+self.x*b.e+self.e*b.x+self.v*b.xe,
                    self.ee*b.v+2*self.e*b.e+self.v*b.ee)
    __rmul__=__mul__
    def __pow__(self,n):
        v=self.v**n; f=n*self.v**(n-1); ff=n*(n-1)*self.v**(n-2)
        return Jet2(v,f*self.x,f*self.e,f*self.xx+ff*self.x**2,
                    f*self.xe+ff*self.x*self.e,f*self.ee+ff*self.e**2)
    def __truediv__(self,b):
        return self*self.cast(b)**-1
    def __rtruediv__(self,b):
        return self.cast(b)*self**-1


def cheb(z,n):
    result=[mp.mpf(1),z]
    for _ in range(2,n):
        result.append(2*z*result[-1]-result[-2])
    return result[:n]


def load_G(source):
    with np.load(source,allow_pickle=False) as z:
        if float(z['beta'])!=3 or int(z['m'])!=3 or float(z['gam'])!=0:
            raise ValueError('Only beta3 logarithmic gam0 sources')
        coeff=[[exact(float(v)) for v in row] for row in z['c'].reshape(int(z['J'])+1,int(z['Kw'])+1)]
        se,alpha,amplitude=[exact(float(z[k])) for k in ('se','alpha','a0')]
    def G(x,e):
        E=1+x*x+(e/se)**6; T=E**(-mp.mpf(1)/6)
        t=-mp.log1p(mp.expm1(-alpha)*T)/alpha if alpha else T
        w=(e/se)**2*E**(-mp.mpf(1)/3)
        tx,te=cheb(2*t-1,len(coeff)),cheb(2*w-1,len(coeff[0]))
        return x*e*E**(mp.mpf(1)/3)*mp.fsum(coeff[i][j]*tx[i]*te[j]
                    for i in range(len(coeff)) for j in range(len(coeff[0])))
    return G,amplitude


def differentiate(G,x,e,i,j):
    sx,se=1+abs(x),1+abs(e)
    return mp.diff(lambda u,v:G(x+sx*u,e+se*v),(mp.mpf(0),mp.mpf(0)),(i,j))/(sx**i*se**j)


def invert(G,x,y,guess):
    if not y:
        return mp.mpf(0),mp.mpf(0)
    e=guess
    for _ in range(30):
        err=differentiate(G,x,e,1,0)-y
        if abs(err)/(1+abs(y))<mp.mpf('1e-65'):
            return e,err
        A=differentiate(G,x,e,1,1)
        if A<=0:
            raise ArithmeticError('Nonpositive MP chart')
        trial=e-err/A
        e=trial if trial*y>0 else e/2
    raise ArithmeticError('MP inverse failed')


def fields(G,a,x,e):
    vals={(i,j):differentiate(G,x,e,i,j) for i in range(6) for j in range(6-i)}
    def g(i,j):
        return Jet2(*(vals[i+di,j+dj] for di,dj in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))))
    X,EE=Jet2(x,1,0),Jet2(e,0,1)
    A,B=g(1,1),g(2,0); Ae,Ax,Bx=g(1,2),g(2,1),g(3,0)
    b=B/A; bx=(Bx*A-B*Ax)/A**2; be=(Ax*A-B*Ae)/A**2
    Sx=-3*g(1,0)+3*X*B+EE*A; Se=-5*g(0,1)+3*X*A+EE*g(0,2)
    Sxx=3*X*Bx+EE*Ax; Sxe=-2*A+3*X*Ax+EE*Ae
    See=-4*g(0,2)+3*X*Ae+EE*g(0,3)
    omega=-Sxx+2*b*Sxe-b*b*See+(bx-b*be)*Se-See/A**2+Ae*Se/A**3
    u1=(-Se/A).v; u2=(Sx-b*Se).v
    ox=omega.x-b.v*omega.e; oy=omega.e/A.v
    oxy=(omega.xe-be.v*omega.e-b.v*omega.ee)/A.v
    c=(Sxe.v-be.v*Se.v-b.v*See.v)/A.v
    tx=-a*b.v; ty=a/A.v; txy=-a*be.v/A.v
    txx=-a*(b.x-b.v*b.e)
    txxy=-a*(b.xe-b.e*b.e-b.v*b.ee)/A.v
    y=vals[1,0]
    terms=[(3*x+u1)*ox,(3*y+u2)*oy,omega.v,-tx]
    grouped=[u1*ox,u2*oy,3*x*ox+3*y*oy+omega.v,-tx]
    if x and y:
        dterms=[v/(x*y) for v in grouped]
        prompt_dterms=[v/(x*y) for v in terms]
    elif x:
        dterms=[u1*oxy/x,c*oy/x,3*oxy+4*oy/x,-txy/x]
        prompt_dterms=[(3*x+u1)*oxy/x,(3+c)*oy/x,oy/x,-txy/x]
    elif y:
        dterms=[-c*ox/y,u2*oxy/y,3*oxy+4*ox/y,-txx/y]
        prompt_dterms=[(3-c)*ox/y,(3*y+u2)*oxy/y,ox/y,-txx/y]
    else:
        dterms=[-c*oxy,c*oxy,7*oxy,-txxy]
        prompt_dterms=[(3-c)*oxy,(3+c)*oxy,oxy,-txxy]
    R=sum(terms);N=sum(map(abs,terms));N2=sum(map(abs,grouped))
    D=sum(dterms);ND2=sum(map(abs,dterms));ND=sum(map(abs,prompt_dterms))
    result=dict(x=x,y=y,eta=e,A=A.v,Omega=omega.v,Omega_x=ox,Omega_y=oy,Omega_xy=oxy,
                U1=u1,U2=u2,c=c,Theta=a*e,Theta_x=tx,Theta_y=ty,
                Theta_xy=txy,Theta_xx=txx,Theta_xxy=txxy,
                R=R,N=N,N2=N2,D=D,ND=ND,ND2=ND2,
                regrouping_error=R-sum(grouped),
                desingularized_regrouping_error=D-sum(prompt_dterms))
    result.update(prompt_ratio=abs(R)/N if N else None,
                  grouped_ratio=abs(R)/N2 if N2 else None,
                  prompt_axis_ratio=abs(D)/ND if ND else None,
                  grouped_axis_ratio=abs(D)/ND2 if ND2 else None)
    return result,terms,grouped,dterms
