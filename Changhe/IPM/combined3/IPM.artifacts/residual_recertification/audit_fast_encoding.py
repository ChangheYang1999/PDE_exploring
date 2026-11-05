#!/usr/bin/env python3
"""Exact dyadic regression of every compressed angular/radial product slot."""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from flint import arb, arb_series, ctx
from finite_fast import encode_fast, powers


def main():
    ctx.prec=384
    checks=0
    rows=[]
    for K in [0,1,4,9]:
        ctx.cap=K+1
        scale=arb(3)/8
        stride=2*K+1
        for left_kind,right_kind in [('c','s'),('s','c')]:
            left={};right={};direct_left={};direct_right={}
            for kind,ns,target,direct in [(left_kind,[1,3,5],left,direct_left),
                                           (right_kind,[0,2,4],right,direct_right)]:
                for n in ns:
                    if kind=='s'and n==0:continue
                    cs=[Fraction((-1)**(k+n)*(n+2*k+1),2**(k+1))for k in range(K+1)]
                    target[kind,n]=arb_series([arb(c.numerator)/c.denominator for c in cs],prec=K+1)
                    for k,c in enumerate(cs):
                        c*=Fraction(3,8)**k/2
                        direct[n,k]=direct.get((n,k),Fraction(0))+c
                        direct[-n,k]=direct.get((-n,k),Fraction(0))+(c if kind=='c'else-c)
            exact=defaultdict(Fraction)
            for (n,k),a in direct_left.items():
                for (m,l),b in direct_right.items():exact[n+m,k+l]+=a*b
            out=encode_fast(left,K,5,stride,powers(scale,K))*encode_fast(right,K,4,stride,powers(scale,K))
            local=0
            for n in range(-9,10,2):
                for k in range(2*K+1):
                    index=(9+n)//2*stride+k
                    value=exact[n,k]
                    expected=arb(value.numerator)/value.denominator
                    assert out[index].contains(expected),(K,left_kind,right_kind,n,k)
                    checks+=1;local+=1
            rows.append({'degree':K,'kinds':[left_kind,right_kind],'checks':local})
    here=Path(__file__).resolve().parent
    result={'status':'PASS','method':'Independent Fraction Laurent/radial convolution; every coefficient including full radial degree 2K, dyadic scaling, both allowed angular parity products.',
            'coefficient_checks':checks,'rows':rows,
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'kernel_sha256':sha256((here/'finite_fast.py').read_bytes()).hexdigest()}
    (here/'fast_encoding_exact_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
