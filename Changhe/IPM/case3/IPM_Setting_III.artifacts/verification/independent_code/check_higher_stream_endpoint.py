#!/usr/bin/env python3
"""Exact integer checks of the general logarithmic tensor coefficient."""
from pathlib import Path
from math import prod,comb
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,time
from check_local_two_projection_construction import P
root=Path(__file__).resolve().parents[1]
out=root/'research/interpolated_inverse_regularity/higher_endpoint/verification'
count=0

def check(b):
    global count
    count+=1
    if not b:raise AssertionError(count)

def main():
    started=time.monotonic()
    for q in range(0,13):
        k=q+1
        for n in range(1,31):
            J=prod(n+q-2*h for h in range(q+1));total=0
            for j in range(k+1):
                v=prod(q-n-2*i for i in range(j))*prod(q+n-2*h for h in range(k-j))
                check(v==(-1)**j*J);total+=comb(k,j)*v*v
            check(total==2**k*J*J)
            check((J==0)==(n<=q and (q-n)%2==0))
    # Independent Cartesian quotient derivative of r^6 sin8(theta)=Im(x+iy)^8/(x^2+y^2).
    x,y=P('x'),P('y');r2=x*x+y*y
    def imaginary_power(n):
        return sum(((-1)**((j-1)//2)*comb(n,j)*x**(n-j)*y**j for j in range(1,n+1,2)),P())
    p8=imaginary_power(8)
    numerator=p8.derivative({'x':P(1)})*r2-2*x*p8
    # r^5 sin7=P7/r^2; r^5 sin9=P9/r^4.
    check(numerator==7*imaginary_power(7)*r2-imaginary_power(9))
    check(numerator!=7*imaginary_power(7)*r2+imaginary_power(9))
    j7=prod(7+5-2*h for h in range(6));j9=prod(9+5-2*h for h in range(6))
    check(j7==46080 and j9==322560)
    coefficient=49*j7*j7+j9*j9
    check(coefficient==208089907200)
    # Mode8 really is not a degree6 polynomial: if r2 divided P8, P8(i,1)=0.
    # In Q(i), encode i powers exactly as pairs.
    def ipow(n):return [(1,0),(0,1),(-1,0),(0,-1)][n%4]
    value=[0,0]
    for mon,v in p8.d.items():
        zz=ipow(mon.count('x'))
        value[0]+=v*zz[0];value[1]+=v*zz[1]
    check(value!=[0,0])
    proof=out.parent/'PROOF.md';before=json.loads((out/'proof_before_code.json').read_text())
    check(hashlib.sha256(proof.read_bytes()).hexdigest()==before['sha256'])
    record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':count,'seconds':time.monotonic()-started,
            'proof_sha256':before['sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'D6_log_coefficient_without_pi_a2_tau2':coefficient,'cartesian_divisibility_negative_control':list(map(str,value)),
            'scope':'Exact formula and manufactured noncanonical interpolant. No numerical producer coefficient is certified.'}
    (out/'exact_checks.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
if __name__=='__main__':main()
