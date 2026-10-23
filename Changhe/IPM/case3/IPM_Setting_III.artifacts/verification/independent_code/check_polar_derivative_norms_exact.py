"""Independent exact Cartesian Gaussian integration versus polar identity."""
from fractions import Fraction as F
from math import comb, factorial
from collections import defaultdict
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from polar_derivative_norms import differential_polynomial

# Cartesian functions are sums c x^i y^j exp(-q r^2), with positive integer q.
def clean(p):return {key:v for key,v in p.items() if v}
def add(*args):
    out=defaultdict(F)
    for p in args:
        for key,v in p.items():out[key]+=v
    return clean(out)
def scale(p,c):return clean({key:c*v for key,v in p.items()})
def dx(p,axis):
    out=defaultdict(F)
    for (i,j,q),v in p.items():
        ij=[i,j]
        if ij[axis]:
            k=list(ij);k[axis]-=1;out[k[0],k[1],q]+=ij[axis]*v
        k=list(ij);k[axis]+=1;out[k[0],k[1],q]-=2*q*v
    return clean(out)
def product(p,s):
    out=defaultdict(F)
    for (i,j,q),v in p.items():
        for (a,b,c),w in s.items():out[i+a,j+b,q+c]+=v*w
    return clean(out)
def times_x(p,axis):
    out={}
    for (i,j,q),v in p.items():out[i+(axis==0),j+(axis==1),q]=v
    return out
def oddfac(n):
    out=1
    for j in range(1,n+1,2):out*=j
    return out
def cart_integral(p):
    ans=F(0)
    for (i,j,q),v in p.items():
        if i%2 or j%2:continue
        ans+=v*F(oddfac(i-1)*oddfac(j-1),2**((i+j)//2)*q**((i+j)//2+1))
    return ans
def cart_norm(p,k):
    ans=F(0)
    for j in range(k+1):
        v=p
        for a in range(j):v=dx(v,0)
        for a in range(k-j):v=dx(v,1)
        ans+=comb(k,j)*cart_integral(product(v,v))
    return ans

def sine_modes(p):
    out=defaultdict(lambda:defaultdict(F))
    for (i,j,q),v in p.items():
        assert not i%2 and j%2
        for n in range(1,i+j+1,2):
            amp=sum(comb(i,a)*comb(j,b)*(-1)**b for a in range(i+1) for b in range(j+1) if i+j-2*(a+b)==n)
            out[n][(i+j-1)//2,q]+=v*F((-1)**((j-1)//2)*amp,2**(i+j-1))
    return {n:clean(row) for n,row in out.items()}
def E(row):
    out=defaultdict(F)
    for (power,q),v in row.items():out[power,q]+=2*power*v;out[power+1,q]-=2*q*v
    return clean(out)
def polar_norm(p,k):
    total=F(0)
    for n,row in sine_modes(p).items():
        derivatives=[row]
        for h in range(k):derivatives.append(E(derivatives[-1]))
        for j in range(k+1):
            applied=add(*(scale(v,c) for c,v in zip(differential_polynomial(k,j,n),derivatives)))
            square=defaultdict(F)
            for (a,q),v in applied.items():
                for (b,s),w in applied.items():square[a+b+1-k,q+s]+=v*w
            norm=F(0)
            for (power,q),v in clean(square).items():
                assert power>=0,(k,j,n,power)
                norm+=v*F(factorial(power),q**(power+1))
            total+=comb(k,j)*norm
    return total/F(2**(k+1))

rho={(0,1,1):F(8),(2,1,1):F(-4),(0,3,1):F(-4)}
psi={(1,1,1):F(-2)}
U1=scale(dx(psi,1),-1);U2=dx(psi,0)
assert not add(scale(add(dx(dx(psi,0),0),dx(dx(psi,1),1)),-1),scale(dx(rho,0),-1))
assert not add(dx(U1,0),dx(U2,1))
checks=[]
fields=[('canonical_density',rho)]
for ell in [F(3,2),F(5,2),F(3),F(17,3)]:
    R=add(scale(add(times_x(dx(rho,0),0),times_x(dx(rho,1),1)),ell),product(U1,dx(rho,0)),product(U2,dx(rho,1)),scale(rho,-1))
    fields.append(('canonical_residual_ell'+str(ell),R))
for i,j in [(0,1),(2,1),(0,3),(4,3),(2,5)]:fields.append(('monomial_'+str((i,j)),{(i,j,1):F(1)}))
for label,p in fields:
    for k in range(1,7):
        a=cart_norm(p,k);b=polar_norm(p,k);assert a==b,(label,k,a,b)
        checks.append(dict(field=label,k=k,cartesian_norm2_over_pi=str(a),polar_norm2_over_pi=str(b),pass_=True))
# Check the shift polynomial by action on exact radial monomials.
for k in range(1,8):
    for j in range(k+1):
        for n in range(1,12,2):
            for deg in range(n,n+8,2):
                z=deg-1;poly=differential_polynomial(k,j,n)
                lhs=sum(v*z**h for h,v in enumerate(poly))
                rhs=1
                for i in range(j):rhs*=deg-n-2*i
                for h in range(k-j):rhs*=deg+n-2*h
                assert lhs==rhs
                checks.append(dict(k=k,j=j,n=n,degree=deg,pass_=True))
root=Path('research/polar_derivative_norms/verification');root.mkdir(exist_ok=True)
record=dict(utc=datetime.now(timezone.utc).isoformat(),checks=len(checks),passed=True,proof_sha256=hashlib.sha256(Path('research/polar_derivative_norms/PROOF.md').read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),results=checks)
(root/'exact_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['utc','checks','passed','proof_sha256']}))
