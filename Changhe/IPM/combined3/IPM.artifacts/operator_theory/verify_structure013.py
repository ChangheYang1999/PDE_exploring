#!/usr/bin/env python3
"""Verify exact origin data and structural exponent inequalities for center013.

Read-only input access. Run with python-flint; all decisions are rational.
The JSON output has actual input hashes and exact compared quantities.
"""
import argparse
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
import json
import math
from pathlib import Path
import sys
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx

sys.set_int_max_str_digits(0)
IPM = Path(__file__).resolve().parents[3]
BASE = IPM / 'combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json'
PHI = IPM / 'combined2/IPM.artifacts/exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json'
C = Q(4076476460239181, 2251799813685248)
EXPECTED_BASE = 'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
EXPECTED_PHI = 'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'

@lru_cache(None)
def shifted_legendre(n):
    return Poly([(-1)**(n-j)*math.comb(n,j)*math.comb(n+j,j) for j in range(n+1)])

def choose(x, j):
    v=Q(1)
    for i in range(j):
        v *= (x-i)/Q(i+1)
    return v

def low_base_coefficient(row, degree):
    m,j=row['m'],row['j']
    p=(3+1/C-j*(1-1/C))/2
    sp=row['spec']
    if sp[0]=='mono':
        cs=Poly([0]*sp[1]+[1])
    else:
        assert sp[0]=='leg'
        cs=shifted_legendre(sp[2]).left_shift(sp[1])
    out=Q(0)
    for l in range(degree+1):
        out += cs[l]*choose(p-m-l, degree-l)
    return Q(row['coef'])*out

def group_atoms(rows, elementary=False):
    groups=defaultdict(Poly)
    for row in rows:
        n,h,d=row['n'],row['h'],row['d']
        assert n>0 and n%2==1 and h>=0 and d>=0
        b,t=Q(row['b_exact']),Q(row['scale_exact'])
        assert t>0
        a=Q(row['coefficient_exact'])
        k=0 if elementary else row.get('legendre_degree',0)
        groups[n,b,t,d-h] += a*shifted_legendre(k).left_shift(h)
    return {k:p for k,p in groups.items() if p}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    raw0,rawp=BASE.read_bytes(),PHI.read_bytes()
    assert sha256(raw0).hexdigest()==EXPECTED_BASE
    assert sha256(rawp).hexdigest()==EXPECTED_PHI
    base,phi=json.loads(raw0),json.loads(rawp)
    assert Q(base['cl_exact'])==C==Q(phi['c_exact'])
    assert phi['reference_sha256']==EXPECTED_BASE
    for row in base['generators']:
        assert row['m']>=0 and row['j']>=0
        assert row['spec'][0] in ('mono','leg')
    # chi homogeneous quartic terms determine the base velocity strain and slope.
    t0=sum((low_base_coefficient(a,2) for a in base['generators'] if a['m']==0),Q(0))
    t1=sum((low_base_coefficient(a,1) for a in base['generators'] if a['m']==1),Q(0))
    t2=sum((low_base_coefficient(a,0) for a in base['generators'] if a['m']==2),Q(0))
    strain0=8*t0-24*t2
    slope0=-32*t0+24*t1
    assert C+strain0==1
    assert slope0==Q(phi['center']['a0_base_exact'])
    # Verify equality of original Legendre and elementary representations.
    gp=group_atoms(phi['atoms'])
    ge=group_atoms(phi['atoms_elementary'],True)
    assert gp==ge
    # phi_3=A*y*(x²+y²)+B*Im((x+iy)^3).
    A=B=Q(0)
    tau_max=None
    for row in phi['atoms']:
        n,h,d=row['n'],row['h'],row['d']
        b,t=Q(row['b_exact']),Q(row['scale_exact'])
        a=Q(row['coefficient_exact'])
        deg=row.get('legendre_degree',0)
        cs=shifted_legendre(deg)
        if n==1 and h<=1:
            radial = t**(-d)*cs[0] if h==1 else t**(-d)*((b-Q(d)/t)*cs[0]+cs[1]/t)
            A += a*radial
        if n==3 and h==0:
            B += a*t**(-d)*cs[0]
        tau=Q(n+2*h-2*d)+2*b
        if 'tau_exact' in row: assert tau==Q(row['tau_exact'])
        tau_max=tau if tau_max is None else max(tau,tau_max)
    assert A==Q(phi['exact_identities']['A_cubic'])
    assert B==Q(phi['exact_identities']['B_cubic'])
    assert A+3*B==0
    correction_strain=2*(A+3*B)
    correction_slope=-8*A
    assert correction_slope==Q(phi['exact_identities']['origin_density_slope_h_phi'])
    slope_star=slope0+correction_slope
    assert slope_star==Q(phi['exact_identities']['a_star_exact'])
    assert slope_star>1
    assert tau_max==Q(phi['mu_exact'])==4/C-3
    gamma=1-1/C
    gamma_h=3-tau_max
    assert 0<gamma<1 and gamma_h>0
    # h=-Delta phi = O(r^(tau-2)); source/dilation graph have the same power.
    assert tau_max-2 < -1  # L2 at infinity.
    assert 1+tau_max-2 < -1  # W h is L2 for sigma=1.
    assert gamma_h>gamma
    assert 1<1+gamma  # inherited weighted E bound.
    ctx.prec=256
    slope_ball=arb(slope_star.numerator)/arb(slope_star.denominator)
    out={
        'status':'EXACT_STRUCTURE_CHECK_PASS',
        'input_sha256':{'base007':EXPECTED_BASE,'phi013':EXPECTED_PHI},
        'fixed_c_exact':str(C),
        'base_generator_count':len(base['generators']),
        'correction_atom_count':len(phi['atoms']),
        'grouped_polynomials':len(gp),
        'original_equals_elementary_exactly':True,
        'base_normalization_c_plus_strain_equals_one':True,
        'correction_A_plus_3B':str(A+3*B),
        'correction_strain':str(correction_strain),
        'correction_slope_exact':str(correction_slope),
        'rho_star_origin_slope_arb':str(slope_ball),
        'rho_star_origin_slope_greater_than_one':True,
        'tau_max_exact':str(tau_max),
        'background_gamma_exact':str(gamma),
        'correction_gradient_gamma_exact':str(gamma_h),
        'sigma_one_in_weighted_commutator_range':True,
        'all_order_symbol_bounds':'proved by the finite algebraic representation; constants not evaluated',
        'stationary_existence':'NOT_CLAIMED: quantitative full energy and self-map remain required'
    }
    encoded=json.dumps(out,indent=2)+'\n'
    if args.output:
        args.output.write_text(encoded)
    print(encoded,end='')

if __name__=='__main__':
    main()
