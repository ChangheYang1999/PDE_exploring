# (o6)/(o8) item 5: on the references ref_c6g_K<K>.json (K = 0: q = 0 at the same A, x*), own evaluator bnat.py:
# b0 = B(e = 0), mu0 = -e B_e/b0 = 1 - B/b0 (B is affine in e), and the sampled sign of R = Q - P(m) - Q(1) on (0, 1),
# P(m) = pi1 m + pi3 m^3 + pi5 m^5 the polynomial with Q - P(m) = O(u) at 0 (from the own series at 0).
import sys, time, json
sys.path.insert(0, 'verifier/early_code/xref_ver')
import mpmath as mp
from bnat import Ref, B_value, ser_mul
Ks = [int(k) for k in sys.argv[1].split(',')]
out = {}
for K in Ks:
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % (K if K else 4)))
    mp.mp.dps = 40
    A = repr(d['A']); xs = mp.mpf(repr(d['x_star'])); e = 1/xs**2
    q = d['q_monomial'] if K else []
    t0 = time.time()
    R = Ref(A, e, q, dps=40); N = 80; R.series0(N)
    B, _ = B_value(R, 'II', mp.mpf('0.25'))
    R0 = Ref(A, 0, q, dps=40); R0.series0(N)
    b0, _ = B_value(R0, 'II', mp.mpf('0.25'))
    mu0 = 1 - B/b0
    # P(m): Q = u^-5 Qh(u), m = mh(u)/u, mh = A (1 - u) e^-Psi; recompute mh from the series data: mh = A u^2/(u^2 Gh) * (-w0/u^3)...
    # use m = -w0/G directly: mh = (-w0/u)/Gh
    import sympy as sp
    u = R.sym['u']
    s = sp.series(-R.sym['w0']/u, u, 0, N + 1).removeO()
    wu = [mp.mpf(0)]*(N + 1)
    for (k,), v in sp.Poly(s, u).terms():
        wu[k] = mp.mpf(sp.Rational(v).p)/mp.mpf(sp.Rational(v).q)
    from bnat import ser_div
    Gh = R.ser['Gh']; Qh = R.ser['Qh']
    mh = ser_div(wu, Gh, N)
    m3 = ser_mul(ser_mul(mh, mh, N), mh, N); m5 = ser_mul(ser_mul(m3, mh, N), mh, N)
    pi5 = Qh[0]/m5[0]
    pi3 = (Qh[2] - pi5*m5[2])/m3[0]
    pi1 = (Qh[4] - pi5*m5[4] - pi3*m3[2])/mh[0]
    # remainder series: R + Q(1) = sum_k c_k u^(k - 5), c_k = Qh_k - pi5 m5_k - pi3 m3_(k-2) - pi1 mh_(k-4)
    c = [Qh[k] - pi5*m5[k] - (pi3*m3[k - 2] if k >= 2 else 0) - (pi1*mh[k - 4] if k >= 4 else 0) for k in range(N + 1)]
    lowc = [mp.nstr(c[k], 6) for k in range(0, 8)]
    Q1 = R.Q1
    def Rser(x):
        return mp.fsum(c[k]*x**(k - 5) for k in range(6, N + 1)) - Q1
    def Rdir(x, tt):
        f = R.fields(x, tt)
        m = f['m']
        return f['Q'] - (pi1*m + pi3*m**3 + pi5*m**5) - Q1
    samples = []
    for i in range(1, 401):
        x = mp.mpf(i)/401
        samples.append((x, Rdir(x, 1 - x)))
    for k in range(1, 16):
        tt = mp.mpf(10)**(-k)
        samples.append((1 - tt, Rdir(1 - tt, tt)))
    ser_s = [(mp.mpf(10)**(-k), Rser(mp.mpf(10)**(-k))) for k in range(1, 9)]
    # consistency of series and direct evaluation at u = 0.05, 0.1
    cons = [mp.nstr(Rser(mp.mpf(x)) - Rdir(mp.mpf(x), 1 - mp.mpf(x)), 3) for x in ('0.05', '0.1', '0.2')]
    npos = sum(1 for x, v in samples + ser_s if v >= 0)
    vmax = max(samples + ser_s, key=lambda p: p[1])
    near1 = [(mp.nstr(1 - x, 3), mp.nstr(v/(1 - x), 8)) for x, v in samples[-15:][::5]]
    res = dict(K=K, B=mp.nstr(B, 20), b0=mp.nstr(b0, 20), mu0=mp.nstr(mu0, 10), pi=[mp.nstr(p, 12) for p in (pi1, pi3, pi5)],
               remainder_low_coeffs_k0_7=lowc, Q1=mp.nstr(Q1, 15), n_samples=len(samples) + len(ser_s), n_nonneg=npos,
               R_max=(mp.nstr(vmax[0], 8), mp.nstr(vmax[1], 8)), series_minus_direct=cons, R_over_1mu_near1=near1,
               R_at_series_points=[(mp.nstr(x, 3), mp.nstr(v, 10)) for x, v in ser_s[::3]])
    if K == 0:
        res['SA_e'] = mp.nstr(6*R.A*(4*R.A - 3)/(8*R.A - 1)*e, 10)
    print(json.dumps(res), '(%.0fs)' % (time.time() - t0), flush=True)
    out[K] = res
json.dump(out, open('verifier/early_runs/o6b_%s.json' % sys.argv[1].replace(',', '_'), 'w'), indent=1)
