"""Independent exact stationary far-tail recurrence and checkpoint descendant audit.
Only this lane's recovered exact coefficient files are read. No original code is run.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import gcd
import json, sys
from check_tail import add_sine, density_stream, advection
from flint import arb, ctx

BASE = Path(__file__).resolve().parents[2]
ctx.prec = 320
sys.set_int_max_str_digits(0)

def enc(q):
    return str(q.numerator) + '/' + str(q.denominator)

def ball(q):
    return arb(q.numerator) / arb(q.denominator)

def norm_series(F):
    square = sum((v*v for v in F.values()), Q(0)) / 4
    return {'squared_divided_by_pi': enc(square), 'arb': (ball(square)*arb.pi()).sqrt().str(45)}

def stream_from_density(F, p):
    source = {}
    for k, v in F.items():
        add_sine(source, k+1, (p-k)*v/2)
        add_sine(source, k-1, (p+k)*v/2)
    P = {}
    for k, v in source.items():
        den = k*k-(p+1)**2
        assert den != 0, ('angular resonance', p, k)
        P[k] = v / den
    return P

def clean(F):
    return {k:v for k,v in F.items() if v}

def run(state, N=6):
    d = json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
    c = Q(d['exact_parameters']['cl']); gamma = 1/c; delta = 1-gamma
    a = list(map(Q, d['canonical_coefficients']))
    density = {}; streams = {}
    for j in range(4):
        for q in range(2):
            C = {}
            for v, (jj,m,k) in zip(a, d['canonical_order']):
                if jj == j:
                    weight = Q(1) if q == 0 else (3+gamma-j*delta)/2-k
                    C[2*m] = C.get(2*m, Q(0)) + v*weight
            p = gamma-j*delta-2*q
            F,P = density_stream(C, p+3)
            density[j,q] = clean(F); streams[j,q] = clean(P)
            assert stream_from_density(F, p) == streams[j,q]
    theta = {1:density[0,0]}; psi = {1:streams[0,0]}
    powers = {n:1-n*delta for n in range(1,N+2)}
    defects = {}
    for n in range(2,N+1):
        S = {}
        for i in range(1,n):
            j = n-i
            term = advection(psi[i], theta[j], powers[i]+1, powers[j])
            for k,v in term.items(): add_sine(S,k,v)
        theta[n] = clean({k:v/((n-1)*(c-1)) for k,v in S.items()})
        psi[n] = stream_from_density(theta[n], powers[n])
        check = {k:(c*powers[n]-1)*v for k,v in theta[n].items()}
        for k,v in S.items(): add_sine(check,k,v)
        assert not clean(check)
        if n <= 4:
            D = dict(theta[n])
            for k,v in density[n-1,0].items(): add_sine(D,k,-v)
            defects[n] = norm_series(clean(D))
        print(state, 'completed exact order', n, 'max harmonic', max(theta[n]), flush=True)
    descendants = {}
    for j in range(2):
        F = density[j,1]; p = gamma-j*delta-2
        assert p > -2 and F
        descendants[f'{j},1'] = {'power':enc(p), 'power_display':float(p),
            'coefficients':{str(k):enc(v) for k,v in F.items()}, 'norm':norm_series(F)}
    output = {'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'state':state,
        'input_sha256':d['canonical_serialization_sha256'], 'c':enc(c), 'gamma':enc(gamma),
        'N':N, 'first_omitted_power':enc(powers[N+1]),
        'first_omitted_power_display':float(powers[N+1]),
        'stationary_density_orders':{str(n):{'power':enc(powers[n]),
            'coefficients':{str(k):enc(v) for k,v in theta[n].items()}, 'norm':norm_series(theta[n]),
            'max_harmonic':max(theta[n])} for n in theta},
        'stationary_stream_orders':{str(n):{str(k):enc(v) for k,v in psi[n].items()} for n in psi},
        'checkpoint_primary_order_differences':defects,
        'checkpoint_additional_nonintegrable_descendants':descendants,
        'scope':'Exact finite formal stationary jet, not convergence or an exact solution. Canonical stream multipoles after radial cutoff are of velocity order at most r^-3 and cannot affect the displayed orders.'}
    dest = Path(__file__).parent/f'state{state:03d}_formal_tail.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print(state, 'descendant powers/norms', [(k, v['power_display'], v['norm']['arb']) for k,v in descendants.items()], flush=True)
    print(state, 'formal tail file bytes', dest.stat().st_size, flush=True)

if __name__ == '__main__':
    for state in (88,131): run(state)
