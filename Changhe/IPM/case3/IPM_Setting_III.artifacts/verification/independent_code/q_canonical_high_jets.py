"""Independent exact finite-Q jets; derivation: result96/PROOF.md.

No producer inverse, differentiation or optimizer code is used. The compact
coordinate is inverted by Lagrange coefficients, not finite differences.
"""
from fractions import Fraction as F
from math import comb
from collections import defaultdict
from q_mp_primitives import chebyshev_power_rows,convert


def rat(v):return v if isinstance(v,F)else F(v)if isinstance(v,(int,str))else F(float(v))
def p_add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for j,v in enumerate(a):out[j]+=v
    for j,v in enumerate(b):out[j]+=v
    return out

def p_scale(a,c):return [c*v for v in a]
def p_shift(a,k=1):return [F(0)]*k+list(a)
def p_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for j,v in enumerate(a):
        for k,w in enumerate(b):out[j+k]+=v*w
    return out

def beta_integral(poly,q):
    moment=1/(q+1);ans=F(0)
    for k,v in enumerate(poly):
        if k:moment*=F(k)/(q+k+1)
        ans+=v*moment
    return ans

def composed_coeff(poly,k,kappa):
    if k==0:return poly[0]if poly else F(0)
    # [u^(k-1)] G'(u)(1-u)^(2 kappa k), computed by finite convolution.
    powers=[F(1)]
    for j in range(1,k):powers.append(-powers[-1]*(2*kappa*k-j+1)/j)
    return sum((j*poly[j]*powers[k-j]for j in range(1,min(len(poly),k+1))),F(0))/k

def clean(p):return {key:v for key,v in p.items()if v}
def add(*polys):
    out=defaultdict(F)
    for p in polys:
        for key,v in p.items():out[key]+=v
    return clean(out)
def scale(p,c):return clean({key:v*c for key,v in p.items()})
def product(p,q,degree):
    out=defaultdict(F)
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            if i+j+k+l<=degree:out[(i+k,j+l)]+=v*w
    return clean(out)
def derivative(p,axis):
    out=defaultdict(F)
    for key,v in p.items():
        if key[axis]:
            new=list(key);new[axis]-=1;out[tuple(new)]+=key[axis]*v
    return clean(out)
def angular_poly(n,k):
    """(X^2+Y^2)^k Im(X+iY)^n, k>=0."""
    assert k>=0
    out=defaultdict(F)
    for j in range(1,n+1,2):
        z=(-1)**((j-1)//2)*comb(n,j)
        for t in range(k+1):out[(n-j+2*t,j+2*(k-t))]+=z*comb(k,t)
    return clean(out)

def solve(coeff,kappa,ell,order=3):
    coeff=[[rat(v)for v in row]for row in coeff];kap=rat(kappa);ell=rat(ell)
    assert coeff and kap>1 and ell>1 and order>=1
    N=max(map(len,coeff))-1;rows=chebyshev_power_rows(N)
    polys=[convert(c,rows)for c in coeff[:order+3]]
    def B(j):return polys[j]if j<len(polys)else [F(0)]
    ds=[]
    for j in range(order+2):
        d=p_add(B(j),p_scale(p_shift(B(j+1)),-F(1,2)if j==0 else -1))
        ds.append(d if j==0 else p_scale(d,F(1,2)))
    beta={}
    for j in range(order+1):
        G=p_shift(p_mul(ds[j],[F(1),F(-1)]),j)
        for k in range(j,order+1):beta[j,k]=composed_coeff(G,k,kap)
    rho={}
    for (j,k),v in beta.items():rho=add(rho,scale(angular_poly(2*j+1,k-j),v))
    stream={};harmonic=[]
    for n in range(1,order+2):
        H=p_mul(ds[n],[F(1),2*kap-1]);moment=beta_integral(H,2*kap*(n-1))/2
        value=moment/2-ds[n-1][0]/(8*n)
        harmonic.append(dict(n=n,density_exterior_moment_core=moment,leading_lower_density=ds[n-1][0],stream_harmonic_core=value))
        stream=add(stream,scale(angular_poly(2*n,0),value))
        for k in range(n,order+1):
            source=(k-n+1)*beta.get((n-1,k),F(0))+(k+n+1)*beta.get((n,k),F(0))
            pc=-source/(4*((k+1)**2-n*n))
            stream=add(stream,scale(angular_poly(2*n,k+1-n),pc))
    U1=scale(derivative(stream,1),-1);U2=derivative(stream,0)
    W1=add({(1,0):ell},U1);W2=add({(0,1):ell},U2)
    R=add(product(W1,derivative(rho,0),2*order+1),product(W2,derivative(rho,1),2*order+1),scale(rho,-1))
    poisson=add(scale(add(derivative(derivative(stream,0),0),derivative(derivative(stream,1),1)),-1),scale(derivative(rho,0),-1))
    assert not poisson,poisson
    return dict(rho=rho,psi=stream,U1=U1,U2=U2,R=R,beta=beta,harmonic=harmonic,a=rho.get((0,1),F(0)),c=stream.get((1,1),F(0)),delta=ell+stream.get((1,1),F(0))-1,ell=ell,kappa=kap,order=order,poisson=poisson)
