"""Independent Cartesian expansion and exact sine projection for result105."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import math,json,hashlib
checks=0

def eq(a,b):
    global checks
    assert a==b,(a,b);checks+=1

def positive(x):
    global checks
    assert x>0,x;checks+=1

def clean(p):return {k:v for k,v in p.items() if v}

def plus(p,q):
    out=dict(p)
    for k,v in q.items():out[k]=out.get(k,Q(0))+v
    return clean(out)

def times(p,q):
    out={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():out[i+k,j+l]=out.get((i+k,j+l),Q(0))+a*b
    return clean(out)

def scale(p,c):return clean({k:c*v for k,v in p.items()})

def diff(p,k):
    out={}
    for ij,v in p.items():
        if ij[k]:
            nn=list(ij);nn[k]-=1;out[tuple(nn)]=v*ij[k]
    return clean(out)

def radial(coeff):
    out={}
    for n,v in enumerate(coeff):
        for k in range(n+1):out[2*k,2*(n-k)]=v*math.comb(n,k)
    return clean(out)

def choose(x,j):
    val=Q(1)
    for k in range(j):val*=(x-k)/(k+1)
    return val

def sine_projection(p,n):
    # Laurent expansion on the unit circle: x=(z+z^-1)/2, y=(z-z^-1)/(2i).
    out={}
    for (i,j),c in p.items():
        assert j%2==1
        total=0
        for k in range(i+1):
            for l in range(j+1):
                if 2*(k+l)-i-j==n:
                    total+=math.comb(i,k)*math.comb(j,l)*(-1)**(j-l)
        v=Q(-2*(-1)**((j+1)//2)*total,2**(i+j))*c
        out[i+j]=out.get(i+j,Q(0))+v
    return clean(out)

def seriesmul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

for beta in [Q(1,100),Q(1,50),Q(1,10),Q(1,4)]:
    for M in [Q(1,3),Q(2),Q(17,3)]:
        g=[Q(0)]+[2*beta*M*choose(-beta-1,j-1) for j in range(1,5)]
        K=[g[j]/(2*j+6) for j in range(len(g))]
        T=[M]+[-g[j]/(2*j) for j in range(1,len(g))]
        expected=seriesmul(K,[(2*j+4)*g[j] for j in range(len(g))])
        gg=seriesmul(g,g)
        expected=[v-Q(3,4)*w for v,w in zip(expected,gg)]
        target=clean({2*j+1:v for j,v in enumerate(expected)})
        eq(expected[2],0)
        eq(expected[3],-g[1]*g[1]*(1+beta)/10)
        for trial in range(6):
            ell=Q(3+trial,2)
            f=[Q(7+trial),Q(trial-3,5),Q(2-trial,7),Q(trial+1,13)]
            J=[f[j]/(2*j+4) for j in range(len(f))]
            tminusj=[T[j]-(J[j] if j<len(J) else 0) for j in range(len(T))]
            rho=plus(times({(0,1):Q(1)},radial(f)),times({(2,1):Q(3),(0,3):Q(-1)},radial(g[1:])))
            psi=plus(times({(1,1):Q(1)},radial(tminusj)),times({(3,1):Q(-2),(1,3):Q(2)},radial(K[1:])))
            eq(scale(plus(diff(diff(psi,0),0),diff(diff(psi,1),1)),-1),diff(rho,0))
            vx=plus({(1,0):ell},scale(diff(psi,1),-1));vy=plus({(0,1):ell},diff(psi,0))
            R=plus(plus(times(vx,diff(rho,0)),times(vy,diff(rho,1))),scale(rho,-1))
            eq(sine_projection(R,7),target)
        for z in [Q(1,1000),Q(1,10),Q(1),Q(10),Q(1000)]:
            d=2-2*(1+beta)*z/(1+z)
            positive(2-d);positive(d+4);positive(d+6)
            eq((d+4)/(d+6)-Q(3,4),(d-2)/(4*(d+6)))
root=Path('research/projected_unbounded_slopes_audit/seventh_mode')
record={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':checks,
        'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact Cartesian Poisson, complete seventh sine residual coefficients for arbitrary first-mode polynomials, center coefficient and sign algebra. Global strict inequality proved in PROOF.md.'}
(root/'verification/exact_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
