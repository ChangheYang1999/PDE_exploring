"""Result107: independent exact Cartesian rational-function calculations.

No producer interpolation, spectral differentiation, or inverse code is used.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,time

start=time.monotonic()
checks=0


def require(condition,message=''):
    global checks
    if not condition:raise AssertionError(message)
    checks+=1


def clean(P):return {ij:c for ij,c in P.items() if c}


def plus(P,Q):
    out=dict(P)
    for ij,c in Q.items():out[ij]=out.get(ij,F(0))+c
    return clean(out)


def scale(P,c):return clean({ij:c*v for ij,v in P.items()})


def times(P,Q):
    out={}
    for (i,j),c in P.items():
        for (k,l),v in Q.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+c*v
    return clean(out)


def pd(P,axis):
    out={}
    for ij,c in P.items():
        if ij[axis]:
            target=list(ij);target[axis]-=1
            out[tuple(target)]=c*ij[axis]
    return clean(out)


r2={(2,0):F(1),(0,2):F(1)}
x={(1,0):F(1)};y={(0,1):F(1)}


def rpow(P,k):
    for unused in range(k):P=times(P,r2)
    return P


def imag_z(n):return {(n-j,j):F(math.comb(n,j)*(-1)**((j-1)//2)) for j in range(1,n+1,2)}


def hom(d,n):
    require((n-d)%2==0,'integer rational radial exponent')
    q=(n-d)//2
    P=imag_z(n)
    if q<0:P=rpow(P,-q);q=0
    return P,q


def rfplus(f,g):
    P,p=f;Q,q=g
    return plus(rpow(P,max(p,q)-p),rpow(Q,max(p,q)-q)),max(p,q)


def rfscale(f,c):return scale(f[0],c),f[1]


def rfd(f,axis):
    P,q=f
    return plus(times(r2,pd(P,axis)),scale(times(x if axis==0 else y,P),-2*q)),q+1


def eq(f,g):
    d=rfplus(f,rfscale(g,-1))
    require(not d[0],('rational function difference',d))


def lap(f):return rfplus(rfd(rfd(f,0),0),rfd(rfd(f,1),1))


def angular_pi(P):
    # Integral of P(cos theta,sin theta) over the full circle, divided by pi.
    out=F(0)
    for (i,j),c in P.items():
        if i%2 or j%2:continue
        a=i//2;b=j//2
        out+=c*F(2*math.factorial(2*a)*math.factorial(2*b),4**(a+b)*math.factorial(a)*math.factorial(b)*math.factorial(a+b))
    return out


def ordered_d4(f):
    out=[]
    for ny in range(5):
        g=f
        for unused in range(4-ny):g=rfd(g,0)
        for unused in range(ny):g=rfd(g,1)
        out.append(g)
    return out


def norm_pi(derivatives):
    return sum(F(math.comb(4,j))*angular_pi(times(f[0],f[0])) for j,f in enumerate(derivatives))


# Derive the angular derivative and Poisson formula by Cartesian quotient rule.
for m in range(2,22,2):
    f=hom(4,m)
    target=rfplus(rfscale(hom(3,m+1),F(4-m,2)),rfscale(hom(3,m-1),F(4+m,2)))
    eq(rfd(f,0),target)
    eq(rfscale(lap(f),-1),rfscale(hom(2,m),m*m-16))

# Independently integrate the squares of all ordered Cartesian fourth partials.
rows=[]
fields={}
for n in range(1,18,2):
    field=hom(3,n)
    derivatives=ordered_d4(field)
    fields[n]=derivatives
    value=norm_pi(derivatives)
    target=F(((n*n-9)*(n*n-1))**2)
    require(value==target,('angular fourth norm',n,value,target))
    rows.append({'n':n,'angular_norm_squared_divided_by_pi':str(value)})

# Cross-frequency cancellation is checked using the full Cartesian tensor,
# rather than being assumed component by component.
ns=list(fields)
for i,n in enumerate(ns):
    for m in ns[i+1:]:
        combination=[rfplus(rfscale(f,F(2,3)),rfscale(g,F(-5,7))) for f,g in zip(fields[n],fields[m])]
        value=norm_pi(combination)
        target=F(4,9)*((n*n-9)*(n*n-1))**2+F(25,49)*((m*m-9)*(m*m-1))**2
        require(value==target,('cross-frequency',n,m,value,target))

# The stated small Poisson-error example, checked directly in Cartesian form.
a=F(8);tau=F(3,1000)
delta=rfscale(hom(4,6),tau)
leading=rfscale(rfd(delta,0),a)
eq(leading,rfscale(rfplus(rfscale(hom(3,5),5),rfscale(hom(3,7),-1)),a*tau))
eq(rfscale(lap(delta),-1),rfscale(hom(2,6),20*tau))
value=norm_pi(ordered_d4(leading))
require(value==7372800*a*a*tau*tau,('example divergence coefficient',value))

# Highest-frequency non-cancellation in arbitrary finite quartic stream data.
for M in range(3,10):
    vm={2*j:F((-1)**j*(j+1),j+3) for j in range(1,M+1)}
    modes={n:F(1,2)*((5-n)*vm.get(n-1,0)+(n+5)*vm.get(n+1,0)) for n in range(1,2*M+2,2)}
    require(modes[2*M+1]!=0,'highest quartic stream cannot cancel')
    f=({},0)
    target=({},0)
    for m,v in vm.items():f=rfplus(f,rfscale(hom(4,m),v))
    for n,v in modes.items():target=rfplus(target,rfscale(hom(3,n),v))
    eq(rfd(f,0),target)
    require(modes[5]==5*vm[6],'frequency five')
    require(modes.get(7,0)==-vm[6]+6*vm.get(8,0),'frequency seven')

# Independent exact inverse-map limit for the map exponent 3/2. At t=2s-1,
# r^2=L^2 s/[8(1-s)^3], so (t+1)/r^2=16(1-s)^3/L^2.
map_rows=[]
for L in [F(1,2),F(1),F(2),F(7,3)]:
    previous=None
    for k in range(1,7):
        s=F(1,10**k)
        r_squared=L*L*s/(8*(1-s)**3)
        quotient=(2*s)/r_squared
        require(quotient==16*(1-s)**3/(L*L),'map factor')
        error=abs(quotient-16/(L*L))
        if previous is not None:require(error<previous/9,'map convergence')
        previous=error
    map_rows.append({'L':str(L),'expected_factor':str(16/(L*L)),'last_exact_error':str(error)})

root=Path(__file__).resolve().parents[1]
proof=root/'research/interpolated_inverse_regularity/PROOF.md'
record={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'verdict':'PASS',
        'scope':'Exact algebraic and manufactured tests only; no producer stream coefficients have been evaluated.',
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'angular_norms':rows,'example_a':str(a),'example_tau':str(tau),'example_log_coefficient_divided_by_pi':str(value),'map_tests':map_rows}
(proof.parent/'verification/exact_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['utc','elapsed_seconds','checks','verdict']},indent=2))
