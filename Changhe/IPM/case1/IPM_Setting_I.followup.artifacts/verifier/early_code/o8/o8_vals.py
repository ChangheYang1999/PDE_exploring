# (o8) items 2 and 3 (values), own code: closed forms on the rational family (q = 0) in two forms, the own
# quadrature evaluator bnat.py (code/xref_ver) at both references, A- and e-derivatives, DB(phi_j) at R12 by
# central differences in the q-family (phi_j = u^3 (1 - u^2)^2 q_j(u^2), q_3 = 1 + 2t + 3t^2, q_5 = t + 2t^2, q_7 = t^2),
# g(1) by the referee's closed form (41) against the own reconstruction, and B on the degree-12 fitted reference.
import sys, time, json
sys.path.insert(0, 'verifier/early_code/xref_ver')
import mpmath as mp
from bnat import Ref, B_value
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
mp.mp.dps = 40
out = {}
def CA(A):
    b = 2/A
    return (16 - b)/(3*A*(4 + b))*mp.beta(2 - b/2, b)
def SA(A):
    return 6*A*(4*A - 3)/(8*A - 1)
def Bclosed(A, e):
    return CA(A)*(1 - SA(A)*e)
def B34(A, e):   # referee (34): P5 I3 + P3 I2, I_n = Beta(n - beta/2, beta)
    b = 2/A
    return (mp.mpf(5)/(6*A) - 5*e)*mp.beta(3 - b/2, b) + (1/(2*A) + e)*mp.beta(2 - b/2, b)
refs = [('R12', mp.mpf('10.150725'), mp.mpf('0.0135206')), ('A4', mp.mpf(4), mp.mpf(1)/16)]
if mode in ('all', 'closed'):
    for name, A, e in refs:
        v = Bclosed(A, e); v34 = B34(A, e)
        BA = mp.diff(lambda a: Bclosed(a, e), A); Be = -CA(A)*SA(A)
        BAA = mp.diff(lambda a: Bclosed(a, e), A, 2); BAe = mp.diff(lambda a: -CA(a)*SA(a), A)
        out[name] = dict(B=mp.nstr(v, 20), B34_minus_closed=mp.nstr(v34 - v, 3), B_A=mp.nstr(BA, 18), B_e=mp.nstr(Be, 20),
                         B_AA=mp.nstr(BAA, 10), B_Ae=mp.nstr(BAe, 10))
        print(name, out[name], flush=True)
    for L in ['8.6000638', '8.6']:
        print('L = %s: closed form B at A0 = %s' % (L, mp.nstr(Bclosed(mp.mpf('10.150725'), 1/mp.mpf(L)**2), 18)), flush=True)
    # sampled maxima over the parameter boxes of |B_A|, |B_e|, |B_AA|, |B_Ae| and |B - B0| (closed form) against the referee's bounds
    for name, A0, e0 in refs:
        for (h, hp) in ([(mp.mpf('0.06'), mp.mpf('0.0003'))] + ([(0, 0)] if name == 'A4' else [])):
            pts = [(A0 + h*i/4, e0 + hp*j/4) for i in range(-4, 5) for j in range(-4, 5)]
            B0 = Bclosed(A0, e0)
            mx = dict(BA=max(abs(mp.diff(lambda a: Bclosed(a, ee), aa)) for aa, ee in pts),
                      Be=max(abs(CA(aa)*SA(aa)) for aa, ee in pts),
                      BAA=max(abs(mp.diff(lambda a: Bclosed(a, ee), aa, 2)) for aa, ee in pts),
                      BAe=max(abs(mp.diff(lambda a: CA(a)*SA(a), aa)) for aa, ee in pts),
                      dB=max(abs(Bclosed(aa, ee) - B0) for aa, ee in pts))
            print('  box %s h %s hp %s: sampled max %s' % (name, h, hp, {k: mp.nstr(v, 8) for k, v in mx.items()}), flush=True)
            out['box_%s_%s' % (name, h)] = {k: mp.nstr(v, 10) for k, v in mx.items()}
if mode in ('all', 'quad'):
    for name, A, e in refs:
        t0 = time.time()
        R = Ref(str(A), e, [], dps=40); R.series0(80)
        v, _ = B_value(R, 'II', mp.mpf('0.25'))
        v1, _ = B_value(R, 'I', mp.mpf('0.2'))
        R0 = Ref(str(A), 0, [], dps=40); R0.series0(80)
        b0, _ = B_value(R0, 'II', mp.mpf('0.25'))
        print('%s own quadrature: B (II) = %s, (I) - (II) = %s, closed - (II) = %s; b0 = B(e = 0) = %s (closed %s); B_e = (B - b0)/e = %s; G(1) = %s (%.0fs)'
              % (name, mp.nstr(v, 20), mp.nstr(v1 - v, 3), mp.nstr(Bclosed(A, e) - v, 3), mp.nstr(b0, 18), mp.nstr(CA(A), 18),
                 mp.nstr((v - b0)/e, 18), mp.nstr(R.G1, 18), time.time() - t0), flush=True)
        # A-derivative at fixed w/A on q = 0: central differences of the quadrature in A
        hA = mp.mpf('1e-5'); vals = []
        for s in (1, -1):
            Rs = Ref(mp.nstr(A + s*hA, 30), e, [], dps=40); Rs.series0(80)
            vals.append(B_value(Rs, 'II', mp.mpf('0.25'))[0])
        print('   dB/dA (quadrature, central h 1e-5) = %s' % mp.nstr((vals[0] - vals[1])/(2*hA), 14), flush=True)
if mode in ('all', 'phi'):
    A, e = refs[0][1], refs[0][2]
    qj = {3: ['1', '2', '3'], 5: ['0', '1', '2'], 7: ['0', '0', '1']}
    for j, q in qj.items():
        t0 = time.time()
        D = {}
        for s in ('1e-5', '2e-5'):
            vv = []
            for sg in (1, -1):
                qs = [mp.nstr(sg*mp.mpf(s)*mp.mpf(c), 30) for c in q]
                R = Ref(str(A), e, qs, dps=40); R.series0(80)
                vv.append(B_value(R, 'II', mp.mpf('0.25'))[0])
            D[s] = (vv[0] - vv[1])/(2*mp.mpf(s))
        rich = (4*D['1e-5'] - D['2e-5'])/3
        print('DB(phi_%d): central 1e-5 %s, 2e-5 %s, Richardson %s (%.0fs)' % (j, mp.nstr(D['1e-5'], 14), mp.nstr(D['2e-5'], 14), mp.nstr(rich, 14), time.time() - t0), flush=True)
        out['DB_phi%d' % j] = mp.nstr(rich, 14)
if mode in ('all', 'fit'):
    d = json.load(open('lead/exclusion_certificates/reference_fit/data/fitted_reference.json'))
    A = mp.mpf(d['A0_exact']); e = 1/mp.mpf(d['L0_exact'])**2
    q = d['q_power_coefficients_exact_decimal']
    t0 = time.time()
    R = Ref(d['A0_exact'], e, q, dps=40); R.series0(80)
    # referee (41): g0(1) = exp(T(1))/2, T(t) = (1/2) int_0^t (1 + s)^2 q(s)/H(s) ds, H(t) = A - t (1 - t^2) q(t)
    qf = lambda t: mp.fsum(mp.mpf(c)*t**k for k, c in enumerate(q))
    T1 = mp.quad(lambda t: (1 + t)**2*qf(t)/(A - t*(1 - t**2)*qf(t)), [0, mp.mpf(1)/2, 1])/2
    fine = dict(nmid=40, wmid=mp.mpf(1)/40, ns=40, levels=14)
    v, _ = B_value(R, 'II', mp.mpf('0.25'), **fine); v1, _ = B_value(R, 'I', mp.mpf('0.2'), **fine)
    v2, _ = B_value(R, 'II', mp.mpf('0.25'))
    print('fitted: B (II) default panels %s, fine minus default %s' % (mp.nstr(v2, 20), mp.nstr(v - v2, 3)), flush=True)
    print('fitted degree-12 reference: own G(1) = %s, (41) exp(T(1))/2 = %s, diff %s; B (II) = %s, (I) - (II) = %s; referee g* 0.4022279001553224429985, B 0.2840732292314196 (%.0fs)'
          % (mp.nstr(R.G1, 22), mp.nstr(mp.exp(T1)/2, 22), mp.nstr(R.G1 - mp.exp(T1)/2, 3), mp.nstr(v, 20), mp.nstr(v1 - v, 3), time.time() - t0), flush=True)
    for K in (12, 18):
        dd = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
        A = mp.mpf(repr(dd['A'])); q = dd['q_monomial']
        qf = lambda t: mp.fsum(mp.mpf(c)*t**k for k, c in enumerate(q))
        T1 = mp.quad(lambda t: (1 + t)**2*qf(t)/(A - t*(1 - t**2)*qf(t)), [0, mp.mpf(1)/2, 1])/2
        R = Ref(repr(dd['A']), 1/mp.mpf(repr(dd['x_star']))**2, q, dps=40)
        print('K=%d: own G(1) = %s, (41) = %s, diff %s' % (K, mp.nstr(R.G1, 22), mp.nstr(mp.exp(T1)/2, 22), mp.nstr(R.G1 - mp.exp(T1)/2, 3)), flush=True)
json.dump(out, open('verifier/early_runs/o8_vals_%s.json' % mode, 'w'), indent=1)
