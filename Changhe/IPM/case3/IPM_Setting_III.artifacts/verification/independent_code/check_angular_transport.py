"""Exact Cartesian polynomial commutator test; no symbolic library needed."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

def add(*ps):
    z={}
    for p in ps:
        for k,v in p.items():z[k]=z.get(k,F(0))+v
    return {k:v for k,v in z.items()if v}
def scale(p,c):return {k:v*c for k,v in p.items()if v*c}
def mul(a,b):
    z={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():z[(i+k,j+l)]=z.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in z.items()if v}
def dx(p,axis):
    z={}
    for ij,v in p.items():
        if ij[axis]:
            k=list(ij);k[axis]-=1;z[tuple(k)]=v*ij[axis]
    return z
x={(1,0):F(1)};y={(0,1):F(1)}
def L(p):return add(mul(x,dx(p,1)),scale(mul(y,dx(p,0)),-1))
def adv(u,p):return add(mul(u[0],dx(p,0)),mul(u[1],dx(p,1)))
count=0
for ell in [F(3,2),F(2),F(5,2),F(3),F(9,2)]:
    for total in range(1,10,2):
        for i in range(0,total,2):
            rho={(i,total-i):F(2*i+1,total+2)}
            for degree in range(2,11,2):
                for k in range(1,degree,2):
                    psi={(k,degree-k):F(k+1,degree+3)}
                    u=[scale(dx(psi,1),-1),dx(psi,0)]
                    W=[add(scale(x,ell),u[0]),add(scale(y,ell),u[1])]
                    v=L(rho);E=add(adv(W,rho),scale(rho,-1))
                    comm=[add(L(u[0]),u[1]),add(L(u[1]),scale(u[0],-1))]
                    discrepancy=add(adv(W,v),scale(v,-1),scale(L(E),-1),adv(comm,rho))
                    assert not discrepancy,(ell,rho,psi,discrepancy)
                    assert all(i%2==1 and j%2==0 for i,j in v)
                    count+=2
assert L(y)==x;count+=1
p=Path('research/angular_transport_and_trace_audit/verification/CHECKS.json')
d={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':count,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(Path('research/angular_transport_and_trace_audit/PROOF.md').read_bytes()).hexdigest(),'method':'Exact Fraction polynomial arithmetic in Cartesian coordinates; independent of the polar proof. Checks commutator and symmetry on every selected pair of parity monomials. No source-sign or existence conclusion.'}
p.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
