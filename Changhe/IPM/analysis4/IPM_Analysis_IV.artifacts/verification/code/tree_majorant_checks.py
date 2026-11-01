"""Finite checks of the tree-packing proof and its explicit corollary.

The all-order argument is handwritten in the paired PROOF.md. These checks
use exact outward-rounded intervals for classification and Arb for positive
scalar majorants; they do not infer the theorem from finite data.
"""
from datetime import datetime, timezone
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
from flint import arb, ctx, fmpq
from potential_bound_certificate import Interval, SCALE


def main():
    sqrt_floor = isqrt(5*SCALE*SCALE)
    sqrt5 = Interval(sqrt_floor, sqrt_floor+1)
    delta = 1/sqrt5
    kappa = 1/(5+2*sqrt5)
    cap = 512
    distances = [None]
    nearest_even = [None]
    for n in range(1,cap+1):
        value = n*delta
        k = ((value.lo+value.hi)//2+SCALE)//(2*SCALE)
        d = abs(value-2*k)
        assert d.lo > 0 and d.hi <= SCALE
        assert n*d.lo >= kappa.hi
        distances.append(d)
        nearest_even.append(2*k)
    packing = []
    for power in range(1,17):
        eps_numerator = SCALE >> power
        marked = [False]*(cap+1)
        for n in range(2,cap+1):
            d=distances[n]
            assert d.hi < eps_numerator or d.lo >= eps_numerator
            marked[n] = d.hi < eps_numerator
        best = [0]*(cap+1)
        for n in range(2,cap+1):
            best[n] = int(marked[n])+max(best[i]+best[n-i] for i in range(1,n))
            assert best[n]*kappa.hi <= 2*n*eps_numerator
        packing.append({
            'epsilon':'1/'+str(1<<power),
            'all_leaf_counts_through':cap,
            'maximum_marks_at_512_leaves':best[cap],
            'marked_subtree_sizes':[n for n in range(2,cap+1) if marked[n]],
            'packing_bound_passed':True,
        })
    ctx.prec=512
    sd=arb(5).sqrt()
    da=1/sd
    ka=1/(5+2*sd)
    e=arb(1).exp()
    q=2*e/ka
    coeff=[arb(0),arb(1)]
    rows=[]
    for n in range(2,129):
        d=abs(n*da-nearest_even[n])
        bn=sum((coeff[i]*coeff[n-i] for i in range(1,n)),arb(0))/d
        coeff.append(bn)
        ratio=bn/((arb(4)**(n-1))*(q**n))
        assert ratio<1
        if n<=12 or n in (32,64,128):
            rows.append({'n':n,'b_n':str(bn),'ratio_to_proved_upper_bound':str(ratio)})
    M=10*arb(2).sqrt()*e*(2+sd)
    A=480*e*(11+5*sd)
    R_delta=(36*arb(2).log()*da).exp()
    assert M<256 and A<32768 and R_delta>65536
    out={
        'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Finite supporting checks, not the all-order proof.',
        'packing_dynamic_program':packing,
        'scalar_majorant_arithmetic_bits':512,
        'scalar_majorant_checked_through':128,
        'selected_scalar_values':rows,
        'explicit_example':{
            'f1':'sin(theta)','delta':'1/sqrt(5)','sigma':'log(2)/2',
            'M':str(M),'A':str(A),'R':'2^36','R_power_delta':str(R_delta),
            'M_lt_256':True,'A_lt_32768':True,'R_power_delta_gt_65536':True,
            'weighted_density_tail_after_N':'512*2^(-N)',
        },
    }
    path=Path('research/07_diophantine_convergence/verification/tree_and_constants.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Tree packing checked for 512 leaf counts and 16 thresholds; scalar majorant through 128; explicit constants certified.')


if __name__=='__main__':
    main()
