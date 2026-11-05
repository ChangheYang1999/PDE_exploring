"""Rigorous finite origin/far expansions and uniform remainder majorants.

All expansion coefficients are exact fmpq values.  Remainders follow from
Cauchy's coefficient bound in the analytic variable s=r² (origin) or u=r^-2
(far).  Homogeneous Cartesian differentiation is performed before norms.
"""
from collections import defaultdict
from functools import lru_cache
import math
from flint import fmpq as Q,arb
from fields013 import Evaluator,C,rational_arb

def exterior_gradient_bound(evaluator,R):
    """Coarse global |rho_x|+|rho_y| bound for every r>=R.

    Bound each original potential group on the complex disk |z-r|<=r/4
    by C r^tau, with C independent of r>=R; Cauchy estimates then
    control all radial derivatives in the polar formulas.  All relevant
    tau-d are strictly negative, so substitution r=R is uniform.
    """
    R=arb(R);total=arb(0)
    for kind,n,b,t,v,p in evaluator.groups:
        pp=arb(0)
        for a in reversed(p.coeffs()):pp=pp*arb(25)/8+arb(abs(a))
        fac=arb(5,0)**n/arb(4)**n
        fac*=(arb(1)/2 if b<0 else 1/R**2+arb(25)/16)**rational_arb(b)
        fac*=(arb(1)/2 if v>=0 else rational_arb(t)/R**2+arb(25)/16)**(-v)
        fac*=pp
        exponent=n+2*b-2*v
        for i,j in [(1,0),(0,1)]:
            ops=[(i+2,j+1),(i,j+3)] if kind=='c' else [(i+2,j),(i,j+2)]
            for dx,dy in ops:
                degree=dx+dy;assert exponent-degree<0
                local=arb(0)
                from fields013 import derivative_series
                for (a,bb,nn,tt),vv in derivative_series(kind,n,dx,dy).items():
                    local+=arb(abs(vv))*math.factorial(a)*arb(4)**a
                total+=local*fac*R**rational_arb(exponent-degree)
    return total

def binom(a,n):
    ans=Q(1)
    for j in range(n):ans*=Q(a-j,j+1)
    return ans

def hdiff(modes,exponent,axis):
    """Differentiate r^exponent * angular modes, reducing exponent by one."""
    out=defaultdict(Q)
    def add(kind,n,v):
        if n<0:n=-n;v=-v if kind=='s' else v
        if n==0 and kind=='s':return
        out[kind,n]+=v
    for (kind,n),a in modes.items():
        if axis=='x':
            add(kind,n+1,a*(exponent-n)/2);add(kind,n-1,a*(exponent+n)/2)
        elif kind=='s':
            add('c',n-1,a*(exponent+n)/2);add('c',n+1,a*(n-exponent)/2)
        else:
            add('s',n+1,a*(exponent-n)/2);add('s',n-1,-a*(exponent+n)/2)
    return {k:v for k,v in out.items()if v}

@lru_cache(None)
def homog_series(kind,n,exponent,i,j):
    m={(kind,n):Q(1)}
    for axis in 'x'*i+'y'*j:m=hdiff(m,exponent,axis);exponent-=1
    return m

class Expansion:
    def __init__(self,evaluator,side,degree=12):
        assert side in ['origin','far']
        self.e=evaluator;self.side=side;self.degree=degree
        self.radius=Q(1,32) if side=='origin' else Q(1,3600)
        self.pot=defaultdict(Q);self.majorants=[]
        for kind,n,b,t,v,p in evaluator.groups:
            coeffs=p.coeffs();cq=[Q(0)]*(degree+1)
            if side=='origin':
                for k,a in enumerate(coeffs[:degree+1]):
                    for q in range(k,degree+1):
                        cq[q]+=a*sum((binom(b,i)*binom(-v-k,q-k-i)*t**(-v-q+i) for i in range(q-k+1)),Q(0))
                exponent=Q(n)
            else:
                for k,a in enumerate(coeffs):
                    for q in range(degree+1):
                        cq[q]+=a*sum((binom(b,i)*binom(-v-k,q-i)*t**(q-i) for i in range(q+1)),Q(0))
                exponent=n+2*b-2*v
            for q,a in enumerate(cq):
                if a:self.pot[kind,n,exponent+(2*q if side=='origin' else -2*q)]+=a
            # majorant for the analytic factor on |s|=radius or |u|=radius.
            rad=rational_arb(self.radius)
            one_lo,one_hi=1-rad,1+rad
            bfac=(one_lo if b<0 else one_hi)**rational_arb(b)
            if side=='origin':
                tlo,thi=rational_arb(t)-rad,rational_arb(t)+rad
                z=rad/tlo
            else:
                tlo,thi=1-rational_arb(t)*rad,1+rational_arb(t)*rad
                z=1/tlo
            poly=arb(0)
            for a in reversed(coeffs):poly=poly*z+arb(abs(a))
            bound=bfac*(tlo if v>=0 else thi)**(-v)*poly
            self.majorants.append((kind,n,exponent,bound))
        self.pot={k:v for k,v in self.pot.items()if v}
        self._fields={}

    def field(self,name,i,j):
        key=name,i,j
        if key in self._fields:return self._fields[key]
        out=defaultdict(Q)
        for (kind,n,exponent),a in self.pot.items():
            if name=='rho':ops=[(-1,i+2,j+1),(-1,i,j+3)] if kind=='c' else [(-1,i+2,j),(-1,i,j+2)]
            elif name=='u1':ops=[(-1,i+1,j+2)] if kind=='c' else [(-1,i+1,j+1)]
            elif name=='u2':ops=[(1,i+2,j+1)] if kind=='c' else [(1,i+2,j)]
            else:raise ValueError(name)
            for sign,dx,dy in ops:
                for (k,m),v in homog_series(kind,n,exponent,dx,dy).items():
                    out[k,m,exponent-dx-dy]+=sign*a*v
        out={k:v for k,v in out.items()if v}
        self._fields[key]=out
        return out

    def remainder_terms(self,name,i,j,r):
        """List (positive coefficient, power): pointwise |tail|<=sum C r^power.

        For a fixed endpoint r, each returned coefficient remains valid on
        0<r'<=r (origin) or r'>=r (far).  The sum of absolute Fourier
        coefficients is bounded, so the estimate is uniform in angle.
        """
        r=arb(r);rad=rational_arb(self.radius);N=self.degree+1
        z=r*r/rad if self.side=='origin' else 1/(r*r*rad)
        assert z<arb(1)/4
        out=[]
        for kind,n,exponent,M in self.majorants:
            if name=='rho':ds=[(i+j+3,2)] if kind=='c' else [(i+j+2,2)]
            else:ds=[(i+j+3,1)] if kind=='c' else [(i+j+2,1)]
            for d,count in ds:
                aa=abs(exponent)+2*N+n+d
                # Successive tail-term ratios are <= 2*z when N>=2*d.
                assert N>=2*d
                coeff=count*M*rational_arb(aa)**d/rad**N/(1-2*z)
                power=exponent-d+(2*N if self.side=='origin' else -2*N)
                out.append((coeff,power))
        return out

    def point_bound(self,name,i,j,r,exclude_constant=False):
        r=arb(r);ans=arb(0)
        for (kind,n,power),a in self.field(name,i,j).items():
            if exclude_constant and power==0:continue
            assert power>=0 if self.side=='origin' else power<0
            ans+=arb(abs(a))*r**rational_arb(power)
        for a,power in self.remainder_terms(name,i,j,r):ans+=a*r**rational_arb(power)
        return ans

    def tail_L2_bound(self,name,i,j,r):
        """Minkowski bound on the full-plane origin/exterior L² norm."""
        r=arb(r);ans=arb(0)
        for (kind,n,power),a in self.field(name,i,j).items():
            den=2*power+2 if self.side=='origin' else -2*power-2
            assert den>0
            ans+=arb(abs(a))*r**rational_arb(power+1)/rational_arb(den).sqrt()
        for a,power in self.remainder_terms(name,i,j,r):
            den=2*power+2 if self.side=='origin' else -2*power-2
            assert den>0
            ans+=a*r**rational_arb(power+1)/rational_arb(den).sqrt()
        return (2*arb.pi()).sqrt()*ans

    def modes_at(self,name,i,j,r):
        r=arb(r);out=defaultdict(lambda:arb(0))
        for (kind,n,power),a in self.field(name,i,j).items():out[kind,n]+=arb(a)*r**rational_arb(power)
        return dict(out)

if __name__=='__main__':
    import time
    e=Evaluator(max_density_order=2);tick=time.monotonic()
    for side,r in [('origin','1e-5'),('far','1e10')]:
        a=Expansion(e,side,degree=12)
        print(side,'built',time.monotonic()-tick,flush=True)
        for f,i,j in [('rho',1,0),('rho',0,1),('rho',2,0),('rho',1,1),('rho',0,2)]:
            print(f,i,j,'point',a.point_bound(f,i,j,r),'L2' if i+j==2 else '',a.tail_L2_bound(f,i,j,r)if i+j==2 else'',flush=True)
