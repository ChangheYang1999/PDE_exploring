# Lead check of the referee's Taylor separation: |dc3| + |dc5| + |dc7| between aligned references (lower bound for N-distance)
import os, json, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 40
A0 = mp.mpf('10.150725')
def jet(A, q, scale):
    # w = -A u (1 - u^2)/(1 + u^2) + u^3 (1 - u^2)^2 q(u^2); coefficients of u^3, u^5, u^7, times scale
    # -A u (1 - u^2) sum (-1)^k u^(2k): coefficient of u^(2m+1) for m >= 1: -A [(-1)^m - (-1)^(m-1)] = -2A(-1)^m
    c = {}
    for m, j in ((1, 3), (2, 5), (3, 7)):
        r = -2 * A * (-1) ** m
        # u^3 (1 - 2u^2 + u^4) q(u^2): coefficient of u^j, with q = sum q_k s^k
        b = {0: 1, 1: -2, 2: 1}
        r += sum(b[i] * q[k] for i in b for k in range(len(q)) if 3 + 2 * i + 2 * k == j)
        c[j] = r * scale
    return c
refs = {}
for K in (12, 18):
    d = json.load(open(os.path.join(HERE, '..', 'b3_functional', 'xref', 'ref_c6g_K%d.json' % K)))
    A = mp.mpf(d['A']); q = [mp.mpf(v) for v in d['q_monomial']]
    refs['K%d' % K] = jet(A, q, A0 / A)
    print('K', K, 'A_i', repr(d['A']))
f = json.load(open(os.path.join(HERE, '..', 'exclusion_certificates', 'reference_fit', 'data', 'fitted_reference.json')))
refs['fit'] = jet(A0, [mp.mpf(v) for v in f['q_power_coefficients_exact_decimal']], 1)
for k, v in refs.items():
    print(k, [mp.nstr(v[j], 12) for j in (3, 5, 7)])
for a, b in (('K12', 'K18'), ('K12', 'fit'), ('K18', 'fit')):
    print(a, b, mp.nstr(sum(abs(refs[a][j] - refs[b][j]) for j in (3, 5, 7)), 10))
