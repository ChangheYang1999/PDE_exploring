#!/usr/bin/env python3
"""Verify the actual platform assumptions used by outward binary64 covers.

This is a finite platform check, not a proof of all IEEE arithmetic. The
certificate method relies on IEEE-754 correctly rounded basic operations;
the exact Fraction comparisons below detect common mode/underflow mistakes.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import platform
import random
import sys
import numpy as np
from flint import arb,ctx

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=384
    info=np.finfo(np.float64)
    assert info.nmant==52 and info.maxexp==1024 and info.minexp==-1022
    assert sys.float_info.radix==2 and sys.float_info.mant_dig==53
    assert np.nextafter(np.float64(0),np.inf)>0
    tiny=np.float64(1e-310)
    assert tiny>0 and tiny*np.float64(1)==tiny
    cases=[(1.,-1.),(1.,2.**-53),(1e-160,1e-160),(1e-300,1e-300),
           (1e-310,1.),(-1e-310,1.),(1e80,1e-80),(-1e80,1e-80)]
    rng=random.Random(20261104)
    for _ in range(2000):
        cases.append((rng.uniform(-1,1)*2.**rng.randrange(-500,501),
                      rng.uniform(-1,1)*2.**rng.randrange(-500,501)))
    checked=0
    with np.errstate(over='ignore',under='ignore',invalid='ignore'):
        for a,b in cases:
            for operation,exact in [(lambda x,y:x+y,F(a)+F(b)),
                                    (lambda x,y:x-y,F(a)-F(b)),
                                    (lambda x,y:x*y,F(a)*F(b))]:
                value=operation(np.float64(a),np.float64(b))
                assert np.isfinite(value)
                lo=np.nextafter(value,-np.inf);hi=np.nextafter(value,np.inf)
                assert F(float(lo))<=exact<=F(float(hi))
                checked+=1
    # Check endpoint conversion on the actual Arb backend used by the covers.
    balls=[arb.pi(),arb(2).sqrt(),arb(2).log(),arb('1e-310'),arb('1e80'),arb(0,1)]
    balls.extend([(arb(i)/7).sin() for i in range(1,201)])
    for ball in balls:
        lo=np.nextafter(float(ball.lower()),-np.inf)
        hi=np.nextafter(float(ball.upper()),np.inf)
        assert arb(float(lo))<=ball and ball<=arb(float(hi))
    result={'status':'PLATFORM_INTERVAL_CHECKS_PASS','basic_operation_cases':checked,
            'arb_endpoint_cases':len(balls),'numpy_version':np.__version__,
            'python_version':sys.version,'machine':platform.machine(),
            'assumption':'IEEE754 binary64 basic operations; one outward nextafter after every operation',
            'scope':'Finite exact crosschecks of this platform; no assertion about research inequalities.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
