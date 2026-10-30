"""Exact angular algebra for the compensated homogeneous IPM velocity."""
from flint import fmpq as Q
from math import comb


def add(d, n, v, sine=False):
    if sine and n == 0:
        return
    if n < 0:
        n = -n
        if sine:
            v = -v
    d[n] = d.get(n, Q(0)) + v
    if not d[n]:
        del d[n]


def velocity(b, p):
    x, y = {}, {}
    for n, bn in b.items():
        assert n > 0 and n % 2 == 1
        den = 4*(p*p-n*n)
        assert den
        a = bn*(p+n)*(p+n-2)/den
        c = bn*(p-n)*(p-n-2)/den
        add(x, n-2, a)
        add(x, n+2, -c)
        add(y, n, -bn/2, True)
        add(y, n-2, -a, True)
        add(y, n+2, -c, True)
    return x, y


def prod(a, b, sine=False):
    out = {}
    for n, an in a.items():
        for m, bm in b.items():
            add(out, n-m, an*bm/2)
            add(out, n+m, (-1 if sine else 1)*an*bm/2)
    return out


def dot(a, b):
    out = prod(a[0], b[0])
    for n, v in prod(a[1], b[1], True).items():
        add(out, n, v)
    return out


def derive(j):
    c=Q(j['c']);q=1/c-4;p=q+2
    a={int(n):Q(v) for n,v in j['F12'].items()}
    b={int(n):Q(v) for n,v in j['P'].items()}
    modes=a.keys()|b.keys()
    inner=lambda f,g:sum(((q*q+n*n)*f.get(n,Q(0))*g.get(n,Q(0))/2 for n in modes),Q(0))
    s11=inner(a,a);s12=inner(a,b);s22=inner(b,b);det=s11*s22-s12*s12
    assert s11>0 and s22>0 and det>0
    va=velocity(a,p);vb=velocity(b,p)
    out={}
    for f,scale in ((dot(va,va),s22/det),(dot(va,vb),-2*s12/det),(dot(vb,vb),s11/det)):
        for n,v in f.items():add(out,n,scale*v)
    assert all(n%2==0 for n in out)
    return q,p,(s11,s12,s22),va,vb,out


def power_in_unit_interval(t):
    """T(theta) -> polynomial at u=2z-1, u=cos(2theta)."""
    degree=max(t)//2
    cheb=[[Q(1)],[Q(-1),Q(2)]]
    for k in range(2,degree+1):
        a=[Q(0)]*(k+1)
        for i,v in enumerate(cheb[-1]):
            a[i]-=2*v
            a[i+1]+=4*v
        for i,v in enumerate(cheb[-2]):a[i]-=v
        cheb.append(a)
    a=[Q(0)]*(degree+1)
    for n,v in t.items():
        for k,w in enumerate(cheb[n//2]):a[k]+=v*w
    return a


def bernstein(a):
    n=len(a)-1
    return [sum((a[i]*Q(comb(k,i),comb(n,i)) for i in range(k+1)),Q(0)) for k in range(n+1)]


def split_half(b):
    left=[b[0]];right=[b[-1]];row=b
    while len(row)>1:
        row=[(row[i]+row[i+1])/2 for i in range(len(row)-1)]
        left.append(row[0]);right.append(row[-1])
    return left,list(reversed(right))
