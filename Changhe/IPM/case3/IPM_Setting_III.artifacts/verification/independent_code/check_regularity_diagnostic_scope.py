"""Exact finite checks supporting result104; standard library, no numerical solver."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,math

checks=0

def eq(x,y):
    global checks
    assert x==y,(x,y)
    checks+=1

def truth(value):
    global checks
    assert value
    checks+=1

def choose(x,j):
    out=F(1)
    for k in range(j): out*= (x-k)/(k+1)
    return out

def exp_series(z):
    out=[F(1)]
    for n in range(1,len(z)):
        out.append(sum(k*z[k]*out[n-k] for k in range(1,n+1))/n)
    return out

def clean(p): return {ij:c for ij,c in p.items() if c}

def add(p,q):
    d=dict(p)
    for ij,c in q.items(): d[ij]=d.get(ij,F(0))+c
    return clean(d)

def scale(p,c): return clean({ij:c*v for ij,v in p.items()})

def dx(p,axis):
    d={}
    for ij,c in p.items():
        if ij[axis]:
            target=list(ij);target[axis]-=1
            d[tuple(target)]=c*ij[axis]
    return clean(d)

def mul(p,q):
    d={}
    for (i,j),c in p.items():
        for (k,l),v in q.items(): d[i+k,j+l]=d.get((i+k,j+l),F(0))+c*v
    return clean(d)

def radial_y(q,a,stream=False):
    out={}
    for n,c in enumerate(q):
        for k in range(n+1):
            ij=(2*k+int(stream),2*(n-k)+1)
            out[ij]=a*c*math.comb(n,k)*(-F(1,2*n+4) if stream else 1)
    return clean(out)

alpha=F(7,2);beta=alpha/2
rows=[]
for m in range(9):
    eps=F(1,4**m)
    eps_alpha=F(1,2**(7*m))
    w=[F(0)]+[choose(beta,j)*eps_alpha/(eps**(2*j)) for j in range(1,5)]
    q=exp_series([-v for v in w])
    eq(q[0],1)
    eq(q[1],-beta*F(1,2**(3*m)))
    eq(q[2],beta*beta/2*eps**3-beta*(beta-1)/2*2**m)
    eq(q[2]/2**m,beta*beta/2*eps_alpha-beta*(beta-1)/2)
    if m: truth(q[2]<0)
    for ell in [F(101,100),F(6,5),F(3,2),F(2),F(5,2),F(3),F(9,2),F(5),F(8),F(11)]:
        D=ell-1;a=4*D;A=2*ell-1
        rho=radial_y(q,a);psi=radial_y(q,a,True)
        lap=add(dx(dx(psi,0),0),dx(dx(psi,1),1))
        eq(scale(lap,-1),dx(rho,0))
        eq(rho[0,1],a);eq(psi[1,1],-D);eq(ell+psi[1,1],1)
        eq(rho[2,1],a*q[1]);eq(rho[0,3],a*q[1])
        eq(rho[4,1],a*q[2]);eq(rho[2,3],2*a*q[2]);eq(rho[0,5],a*q[2])
        vx=add({(1,0):ell},scale(dx(psi,1),-1));vy=add({(0,1):ell},dx(psi,0))
        R=add(add(mul(vx,dx(rho,0)),mul(vy,dx(rho,1))),scale(rho,-1))
        eq(R.get((0,1),0),0)
        eq(R.get((2,1),0),a*q[1]*(2*A-a/2))
        eq(R.get((0,3),0),a*q[1]*(2-a/6))
        truth(bool(R.get((2,1),0) or R.get((0,3),0)))
        lam=F(3,2)
        qscaled=[c/lam**(2*n) for n,c in enumerate(q)]
        eq(radial_y(qscaled,a),{ij:c*lam**(1-sum(ij)) for ij,c in rho.items()})
        eq(radial_y(qscaled,a,True),{ij:c*lam**(2-sum(ij)) for ij,c in psi.items()})
    rows.append({'m':m,'epsilon':str(eps),'q_r2':str(q[1]),'q_r4':str(q[2]),'normalized_q_r4':str(q[2]/2**m)})

# Smooth q = exp(-r^4), using t=r^2. Its cubic jets vanish.
q=exp_series([F(0),F(0),F(-1),F(0),F(0)])
eq(q,[F(1),F(0),F(-1),F(0),F(1,2)])
for ell in [F(6,5),F(3,2),F(2),F(3),F(8)]:
    a=4*(ell-1);A=2*ell-1
    rho=radial_y(q,a);psi=radial_y(q,a,True)
    vx=add({(1,0):ell},scale(dx(psi,1),-1));vy=add({(0,1):ell},dx(psi,0))
    R=add(add(mul(vx,dx(rho,0)),mul(vy,dx(rho,1))),scale(rho,-1))
    eq(rho.get((2,1),0),0);eq(rho.get((0,3),0),0)
    cx=a*(-4*A+5*a/8);cy=a*(-4+a/8)
    eq(R.get((4,1),0),cx);eq(R.get((2,3),0),cx+cy);eq(R.get((0,5),0),cy)
    truth(bool(cx or cy))
# Both residual coefficients cannot vanish at positive p after center normalization.
for p in [F(1,2),F(2),alpha,F(4),F(17,3),F(8)]:
    D=p/2;a=4*D
    eq(a-p*(p+4),-p*(p+2))
    truth(a!=p*(p+4))

root=Path('research/regularity_diagnostic_scope')
record={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':checks,
        'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'rows':rows,
        'scope':'Exact finite expansion, Cartesian Poisson and residual, center and dilation checks. C4 convergence and non-C5 limit are proved in PROOF.md, not by the finite checks.'}
(root/'verification/exact_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='rows'},indent=2))
