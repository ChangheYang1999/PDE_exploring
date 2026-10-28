"""Exact reconstruction of an accepted 860-generator state (case 4) from its checkpoint.

Independent of the campaign code: only the conventions of BASIS_860_IMPLEMENTATION.md are used.
Generators chi_{m,k,j} = r^{2k} (1+r^2)^{p_j-k} cos(2 m theta), p_j = (3 + gamma - j lambda)/2, gamma = 1/cl, lambda = 1-gamma.
Canonical index I(j,m,k) = 215 j + 26 m - m(m-1)/2 + (k-m).
Internal: low (60) raw monomials (m<=4, k<=4) in order L(j,m,k) = 15 j + 5 m - m(m-1)/2 + (k-m), L=0 is a_000 (eliminated);
high (800): E_{mnj} = H_m R^{p_j-m} t^{v_m} N_n P_n(2t-1), v_m = max(5,m), order j, m, n.
a_{m, v_m+h, j} = sum_n c_{mnj} N_n (-1)^(n-h) C(n,h) C(n+h,h).
Center strain s_i = chi_xxyy(0): (0,0,j): 4 p_j (p_j-1); (0,1,j): 8 (p_j-1); (0,2,j): 8; (2,2,j): -24; else 0.
a_000 = (1 - cl - sum_{i>=1} s_i a_i)/s_0.
"""
import json, hashlib, math
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import numpy as np

def canon(j, m, k): return 215*j + 26*m - m*(m-1)//2 + (k-m)
LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]
HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]
assert len(LOW) == 60 and len(HIGH) == 800

def p_exp(cl, j):
    g = 1/cl; lam = 1-g
    return (3 + g - j*lam)/2

def strains(cl):
    s = []
    for (m, k, j) in LOW:
        p = p_exp(cl, j)
        if (m, k) == (0, 0): s.append(4*p*(p-1))
        elif (m, k) == (0, 1): s.append(8*(p-1))
        elif (m, k) == (0, 2): s.append(Fr(8))
        elif (m, k) == (2, 2): s.append(Fr(-24))
        else: s.append(Fr(0))
    return s

def legendre_monomial(n):
    return [(-1)**(n-h)*math.comb(n, h)*math.comb(n+h, h) for h in range(n+1)]

def load_state(json_path):
    d = json.load(open(json_path))
    cl = Fr(float.fromhex(d['P_hex'][0]))
    assert float(cl) == d['cl']
    P = [Fr(float.fromhex(h)) for h in d['P_hex']]
    high = [Fr(float.fromhex(h)) for h in d['high_hex']]
    NN = [Fr(float.fromhex(h)) for h in d['frozen_Nn_hex']]
    return d, cl, P, high, NN

def reconstruct(cl, P, high, NN):
    s = strains(cl)
    low = list(P); low[0] = Fr(0)
    a000 = (1 - cl - sum(s[i]*low[i] for i in range(1, 60)))/s[0]
    low[0] = a000
    a = [Fr(0)]*860
    for v, (m, k, j) in zip(low, LOW): a[canon(j, m, k)] += v
    for v, (m, n, j) in zip(high, HIGH):
        if v:
            vm = max(5, m); v2 = v*NN[n]
            for h, L in enumerate(legendre_monomial(n)): a[canon(j, m, vm+h)] += v2*L
    return a000, a

if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    d, cl, P, high, NN = load_state(path)
    a000, a = reconstruct(cl, P, high, NN)
    # checks against the checkpoint
    num, den = d['input_exact_for_checkpoint']['a000_exact'].split('/')
    print('cl exact', cl, 'matches', str(cl) == d['input_exact_for_checkpoint']['cl_exact'])
    print('a000 exact match:', a000 == Fr(int(num), int(den)))
    getcontext().prec = 60
    maxrel = 0
    for v, sref in zip(a, d['a_canonical_decimal50_rounded']):
        ref = Decimal(sref); val = Decimal(v.numerator)/Decimal(v.denominator)
        rel = abs(val-ref)/max(abs(ref), Decimal(1e-300)) if ref != 0 else abs(val)
        maxrel = max(maxrel, rel)
    print('max relative difference to 50-digit canonical coefficients:', maxrel)
    # serialization SHA variants
    target = d['input_exact_for_checkpoint']['canonical_serialization_sha256']
    variants = {
        'A': 'cl %d/%d\n' % (cl.numerator, cl.denominator) + '\n'.join('%d/%d' % (v.numerator, v.denominator) for v in a),
        'B': 'cl %d/%d\n' % (cl.numerator, cl.denominator) + '\n'.join('%d/%d' % (v.numerator, v.denominator) for v in a) + '\n',
        'C': 'cl %d/%d\n' % (cl.numerator, cl.denominator) + '\n'.join('%d\n%d' % (v.numerator, v.denominator) for v in a),
        'D': 'cl %d/%d\n' % (cl.numerator, cl.denominator) + '\n'.join('%d\n%d' % (v.numerator, v.denominator) for v in a) + '\n',
        'E': 'cl %d/%d\n' % (cl.numerator, cl.denominator) + '\n'.join('%d %d' % (v.numerator, v.denominator) for v in a),
        'F': 'cl %d/%d\n' % (cl.numerator, cl.denominator) + '\n'.join('%d %d' % (v.numerator, v.denominator) for v in a) + '\n',
    }
    for k, sv in variants.items():
        h = hashlib.sha256(sv.encode()).hexdigest()
        print('variant', k, h == target)
    # binary64 inputs sha
    Pf = np.array([float(v) for v in P]); hf = np.array([float(v) for v in high])
    b = Pf.astype('<f8').tobytes() + hf.astype('<f8').tobytes()
    print('binary64 inputs sha match:', hashlib.sha256(b).hexdigest() == d['input_exact_for_checkpoint']['binary64_inputs_sha256'])
    # save exact state
    out = {'cl': '%d/%d' % (cl.numerator, cl.denominator), 'a000': '%d/%d' % (a000.numerator, a000.denominator),
           'a_canonical': ['%d/%d' % (v.numerator, v.denominator) for v in a], 'order': 'I(j,m,k)=215j+26m-m(m-1)/2+(k-m)',
           'source': path, 'label': d['label']}
    json.dump(out, open(sys.argv[2], 'w'))
    print('a0 (stored)', d['a0'])
    print('nonzero canonical coefficients:', sum(1 for v in a if v != 0), 'max |a|', max(abs(float(v)) for v in a))
