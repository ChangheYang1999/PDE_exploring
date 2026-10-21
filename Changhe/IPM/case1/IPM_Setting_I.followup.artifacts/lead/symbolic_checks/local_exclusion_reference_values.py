"""Lead checks of the local-exclusion referee numbers with bref.py (independent of the referee's code):
(a) R12 closed form values and parameter derivatives; (b) D_w B(phi_j), phi_j = u^j + (j-11)/2 u^9 + (9-j)/2 u^11, by
central differences of B(A, e, w_0 + t phi_j); (c) B and g(1) on the referee's degree-12 fitted reference, and the
closed-form reconstruction g_0(1) = exp(T(1))/2 on the lead's K = 12 reference."""
import os, sys, json
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'b3_functional', 'xref'))
import bref
mp.mp.dps = 40


def closed(A, e):
    be = 2 / A
    SA = 6 * A * (4 * A - 3) / (8 * A - 1)
    CA = (16 - be) / (3 * A * (4 + be)) * mp.beta(2 - be / 2, be)
    return CA * (1 - SA * e), CA * SA


which = sys.argv[1]
if which == 'a':
    for A, e in [(mp.mpf('10.150725'), mp.mpf('0.0135206')), (mp.mpf(4), mp.mpf(1) / 16)]:
        B, CS = closed(A, e)
        BA = mp.diff(lambda a: closed(a, e)[0], A)
        print('A', A, 'e', mp.nstr(e, 10), 'B', mp.nstr(B, 18), 'B_e', mp.nstr(-CS, 18), 'B_A|f', mp.nstr(BA, 18))
elif which == 'b':
    A = mp.mpf('10.150725'); e = mp.mpf('0.0135206')
    P = mp.polyfit if False else None
    for j in (3, 5, 7):
        # phi_j / (u^3 (1 - u^2)^2) as a polynomial in v = u^2: divide coefficients
        c = [mp.mpf(0)] * 12
        c[j] += 1; c[9] += mp.mpf(j - 11) / 2; c[11] += mp.mpf(9 - j) / 2
        # in v: phi/u^3 = sum c_k v^((k-3)/2); divide by (1 - v)^2
        num = [c[k] for k in range(3, 12, 2)]          # coefficients of v^0..v^4
        # polynomial division by 1 - 2v + v^2 (ascending): p(v) (1 - 2v + v^2) = num
        p = [mp.mpf(0)] * 3
        rem = list(num)
        for i in range(3):
            p[i] = rem[i]
            rem[i] -= p[i]; rem[i + 1] += 2 * p[i]; rem[i + 2] -= p[i]
        assert max(abs(x) for x in rem) < mp.mpf(10) ** -30, rem
        vals = []
        for t in (mp.mpf('1e-6'), mp.mpf('-1e-6'), mp.mpf('1e-7'), mp.mpf('-1e-7')):
            r = bref.Ref(A, e, [t * x for x in p], dps=40); r.setup(); vals.append(r.B())
        d6 = (vals[0] - vals[1]) / mp.mpf('2e-6'); d7 = (vals[2] - vals[3]) / mp.mpf('2e-7')
        print('j', j, 'p', [mp.nstr(x, 6) for x in p], 'DB central t=1e-6', mp.nstr(d6, 14), 't=1e-7', mp.nstr(d7, 14),
              flush=True)
elif which == 'c':
    z = json.load(open(os.path.join(HERE, '..', 'exclusion_certificates', 'reference_fit', 'data', 'fitted_reference.json')))
    q = z['q_power_coefficients_exact_decimal']
    A = mp.mpf('10.150725'); e = 1 / mp.mpf('8.6000638') ** 2
    r = bref.Ref(A, e, q, dps=30); r.setup(); B = r.B()
    print('referee K=12 fit: B', mp.nstr(B, 16), 'g(1)', mp.nstr(r.g1, 18), 'L^2 g(1)', mp.nstr(r.g1 * mp.mpf('8.6000638') ** 2, 14),
          'jets', [mp.nstr(r.ser0['W'][k], 10) for k in (1, 3, 5, 7, 9)], flush=True)
    for K in (12, 18):
        zz = json.load(open(os.path.join(HERE, '..', 'b3_functional', 'xref', 'ref_c6g_K%d.json' % K)))
        qq = [mp.mpf(s) for s in zz['q_monomial']]
        H = lambda s: A - s * (1 - s ** 2) * mp.polyval(qq[::-1], s)
        T1 = mp.quad(lambda s: (1 + s) ** 2 * mp.polyval(qq[::-1], s) / H(s), [0, 0.5, 1]) / 2
        rr = bref.Ref(A, mp.mpf(zz['e']), zz['q_monomial'], dps=30); rr.setup()
        print('K', K, 'closed-form g0(1) = exp(T(1))/2', mp.nstr(mp.exp(T1) / 2, 20), 'bref g(1)', mp.nstr(rr.g1, 20),
              'min H on grid', mp.nstr(min(H(mp.mpf(i) / 400) for i in range(401)), 10))
