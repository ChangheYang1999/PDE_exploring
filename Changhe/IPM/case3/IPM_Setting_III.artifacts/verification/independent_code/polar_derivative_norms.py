"""Independent positive polar tensor norms, result102/PROOF.md.

No producer differentiation, inverse or collocation code is imported.
Taylor vectors store coefficients divided by factorial, in log radius.
"""
from math import comb, factorial
from fractions import Fraction
import mpmath as mp
from q_mp_primitives import MPQPrimitives, guard_digits


def const(v, K):
    return [v]+[v*0]*K


def add(a,b):
    return [x+y for x,y in zip(a,b)]


def scale(a,c):
    return [c*x for x in a]


def shift(a,c):
    out=list(a);out[0]+=c;return out


def mul(a,b):
    return [sum((a[j]*b[n-j] for j in range(n+1)),a[0]*0) for n in range(len(a))]


def inv(a):
    out=[1/a[0]]
    for n in range(1,len(a)):
        out.append(-sum((a[j]*out[n-j] for j in range(1,n+1)),a[0]*0)/a[0])
    return out


def derivative(a):
    return [(j+1)*a[j+1] for j in range(len(a)-1)]


def map_jet(s0,kappa,K):
    s=[s0]
    for n in range(K):
        w=shift(scale(s,-1),1)
        den=shift(scale(s,2*kappa-1),1)
        g=scale(mul(mul(s,w),inv(den)),2)
        s.append(g[n]/(n+1))
    return s


def cheb_jet(cc,t):
    z=const(t[0]*0,len(t)-1);b1=z;b2=z
    for c in cc[:0:-1]:
        b0=shift(add(scale(mul(t,b1),2),scale(b2,-1)),c)
        b2,b1=b1,b0
    return shift(add(mul(t,b1),scale(b2,-1)),cc[0])


def density_jets(coeff,s,kappa):
    K=len(s)-1;t=shift(scale(s,2),-1);w=shift(scale(s,-1),1)
    B=[cheb_jet(cc,t) for cc in coeff]+[const(s[0]*0,K)]
    power=const(s[0]*0+1,K);out={}
    for j in range(len(coeff)):
        d=add(B[j],scale(mul(s,B[j+1]),-mp.mpf('.5') if j==0 else -1))
        value=mul(mul(w,power),d)
        if j:value=scale(value,mp.mpf('.5'))
        out[2*j+1]=value
        power=mul(power,s)
    return out


def differential_polynomial(k,j,n):
    """Integer coefficients of P_(k,j,n), ascending order in E."""
    out=[1]
    for a in [1-n-2*i for i in range(j)]+[1+n-2*h for h in range(k-j)]:
        new=[0]*(len(out)+1)
        for p,v in enumerate(out):new[p]+=a*v;new[p+1]+=v
        out=new
    return out


def norm_integrand(d,r,k):
    """Positive d(log r) integrand, including angular pi factor."""
    total=mp.mpf(0)
    for n,row in d.items():
        deriv=[factorial(h)*v for h,v in enumerate(row[:k+1])]
        for j in range(k+1):
            poly=differential_polynomial(k,j,n)
            val=mp.fsum(c*x for c,x in zip(poly,deriv))
            total+=comb(k,j)*val*val
    return mp.pi*mp.exp((4-2*k)*mp.log(r))*total/(2**k)


def residual_jets(d,p,ell,K):
    """d has order K+1; p maps positive even m to order K+1."""
    R={n:add(scale(row[:K+1],ell-1),scale(derivative(row),ell)) for n,row in d.items()}
    def accumulate(n,row):
        if not n:return
        if n<0:n=-n;row=scale(row,-1)
        if n in R:R[n]=add(R[n],row)
        else:R[n]=row
    for m,prow in p.items():
        q=scale(prow[:K+1],-m)
        v=add(scale(prow[:K+1],2),derivative(prow))
        for n,drow in d.items():
            left=scale(mul(q,add(drow[:K+1],derivative(drow))),mp.mpf('.5'))
            right=scale(mul(v,drow[:K+1]),mp.mpf(n)/2)
            accumulate(n+m,add(left,right))
            accumulate(n-m,left)
            accumulate(m-n,right)
    return R


class QNormEvaluator:
    def __init__(self,coeff,L,kappa,ell,dps=80,kmax=6):
        self.dps=dps;self.kmax=kmax
        N=max(map(len,coeff))-1;M=len(coeff)
        self.workdps=dps+guard_digits(N,M,Fraction(kappa))
        with mp.workdps(self.workdps):
            self.inverse=MPQPrimitives(coeff,L,kappa,ell)
        self.coeff=self.inverse.coeff
        self.ell=self.inverse.ell;self.kappa=self.inverse.kappa

    def radial(self,r):
        K=self.kmax
        with mp.workdps(self.workdps):
            r=mp.mpf(r);s0,w=self.inverse.density.coords(r)
            pv,dv=self.inverse.coefficients(r)
        with mp.workdps(self.dps):
            r=+r;s0=+s0
            s=map_jet(s0,self.kappa,K+1)
            d=density_jets(self.coeff,s,self.kappa)
            zero=const(mp.mpf(0),K+1);p={}
            for j,(v,v1) in enumerate(zip(pv,dv),1):
                m=2*j;prev=d.get(m-1,zero);nxt=d.get(m+1,zero)
                h=scale(add(add(derivative(prev),scale(prev[:K+1],2-m)),add(derivative(nxt),scale(nxt[:K+1],m+2))),mp.mpf('.5'))
                row=[+v,+(v1-2*v)]
                for n in range(K):
                    row.append((-4*(n+1)*row[n+1]+(m*m-4)*row[n]-h[n])/((n+2)*(n+1)))
                p[m]=row
            R=residual_jets(d,p,self.ell,K)
            return d,p,R

    def at_radius(self,r):
        d,p,R=self.radial(r)
        with mp.workdps(self.dps):
            return {k:dict(rho=norm_integrand(d,r,k),residual=norm_integrand(R,r,k)) for k in range(2,self.kmax+1)}
