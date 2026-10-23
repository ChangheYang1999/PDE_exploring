#!/usr/bin/env python3
"""Exact interval checks supporting result108; no numerical-library dependency."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json
import time
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/cartesian_separation_rank/verification'
CHECKS=0

def check(test):
    global CHECKS
    CHECKS+=1
    if not test:
        raise AssertionError(f'check {CHECKS}')

def cube_floor(n):
    """Floor cube root by integer bisection, independent of floating arithmetic."""
    lo,hi=0,1 << ((n.bit_length()+2)//3)
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**3 <= n:
            lo=mid
        else:
            hi=mid
    return lo

def cube_interval(n,bits=96):
    den=1<<bits
    z=cube_floor(n*den**3)
    check(z**3<=n*den**3<(z+1)**3)
    lo=F(z,den)
    hi=lo if z**3==n*den**3 else F(z+1,den)
    check(lo**3<=n<=hi**3)
    return lo,hi

def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def mul(a,b):
    c=[x*y for x in a for y in b]
    return min(c),max(c)
def det_interval(a):
    n=len(a)
    result=(F(0),F(0))
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=(F(1),F(1))
        for i,j in enumerate(perm):
            term=mul(term,a[i][j])
        result=add(result,term if sign==1 else neg(term))
    return result

def point_matrix(a): return [[(F(v),F(v)) for v in row] for row in a]
def strings(pair): return [str(v) for v in pair]

def main():
    start=time.monotonic()
    for n in range(101):
        z=cube_floor(n)
        check(z**3<=n<(z+1)**3)
        cube_interval(n)
    check(det_interval(point_matrix([[1,2],[2,4]]))==(0,0))
    check(det_interval(point_matrix([[1,-3,4],[2,0,-1],[3,7,2]]))==(84,84))
    for n in range(1,7):
        a=[[F((i+1)**j) for j in range(n)] for i in range(n)]
        exact=1
        for i in range(n):
            for j in range(i+1,n): exact*=j-i
        check(det_interval(point_matrix(a))==(exact,exact))
        a=[[F(1,i+j+2) for j in range(n)] for i in range(n)]
        numer=1
        for i in range(n):
            for j in range(i+1,n): numer*=(j-i)**2
        denom=1
        for i in range(n):
            for j in range(n): denom*=i+j+2
        exact=F(numer,denom)
        check(det_interval(point_matrix(a))==(exact,exact))
        a=[[F((i+1)*(j+2)) for j in range(n)] for i in range(n)]
        if n>1: check(det_interval(point_matrix(a))==(0,0))
    results=[]
    for n in range(1,7):
        matrix=[]
        for x in range(n):
            row=[]
            for y in range(1,n+1):
                lo,hi=cube_interval(x*x+y*y)
                val=(F(y)/hi,F(y)/lo)
                check(0<val[0]<=val[1]<2)
                row.append(val)
            matrix.append(row)
        det=det_interval(matrix)
        check(det[0]>0)
        bound=min(F(1),det[0]/(n*factorial(n)*3**(n-1)))
        check(bound>0)
        results.append({'n':n,'excluded_rank':n-1,'x':list(range(n)),
                        'y':list(range(1,n+1)),
                        'entry_intervals':[[strings(v) for v in row] for row in matrix],
                        'determinant_interval':strings(det),
                        'determinant_float_display':[float(v) for v in det],
                        'entrywise_error_lower_bound':str(bound),
                        'error_lower_bound_float_display':float(bound)})
    proof=OUT.parent/'PROOF.md'
    manifest=json.loads((OUT/'proof_before_code.json').read_text())
    check(hashlib.sha256(proof.read_bytes()).hexdigest()==manifest['sha256'])
    data={'utc':datetime.now(timezone.utc).isoformat(),'checks':CHECKS,'verdict':'PASS',
          'method':'Integer cube-root bisection and Fraction interval Leibniz determinants',
          'cube_root_bits':96,'elapsed_seconds':time.monotonic()-start,
          'proof_sha256':manifest['sha256'],
          'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Manufactured homogeneous field, not an IPM profile. The all-rank theorem is analytic.',
          'results':results}
    (OUT/'exact_checks.json').write_text(json.dumps(data,indent=2)+'\n')
    lines=['# Exact manufactured separation-rank checks','',data['utc'], '',
           f"{CHECKS} exact checks PASS. Cube-root intervals use 96 binary digits. No floating-point value decides a sign.",
           '', '| Grid size | Determinant lower endpoint | Rank at most | Entrywise error lower bound |',
           '|---|---:|---:|---:|']
    for r in results:
        lines.append(f"| {r['n']} | {r['determinant_float_display'][0]:.12g} | {r['excluded_rank']} | {r['error_lower_bound_float_display']:.12g} |")
    lines+=['','Decimal entries are display values of exact rational bounds saved in exact_checks.json.',
            'The manufactured field is y/(x^2+y^2)^(1/3). These checks do not assert that it solves IPM.']
    (OUT/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:data[k] for k in ['utc','checks','verdict','elapsed_seconds']}))
    print('\n'.join(lines[6:]))
if __name__=='__main__': main()
