"""FLOAT estimate (not a bound) of the low component L(F) = ||w F||_{Hdot^-1(R^2)} of the verifier's weighted norm
E2(F)^2 = ||omega2 D^2 F||^2 + 2^22 ||omega1 D F||^2 + 2^53 L(F)^2 (07_weighted/SHARP_WEIGHTED_H2_PROOF.md, V073), w = (1 + r^2/R^2)^(-11/10),
R = 2^35, for the state-131 residual F, using the EXACT far-field residual sectors F ~ sum_(h,q) r^alpha(h,q) E_(h,q)(theta) (data/state131_farfield.json,
code/farfield_exact.py; valid for r > 1). The near field r < 1 is dropped (|F| < 1e-3 there; its contribution to L is negligible against the far field).
Mode-wise: g_k(r) = w(r) sum_sectors e_k^(h,q) r^alpha; (-Delta)^-1 [g_k sin k theta] = u_k sin k theta,
u_k(r) = (1/2k) [ r^-k int_0^r t^(k+1) g_k dt + r^k int_r^inf t^(1-k) g_k dt ]; L^2 = pi sum_k int_0^inf g_k u_k r dr.
Discretisation: log grid, trapezoid, recursion for the two cumulative integrals (scaled to avoid overflow); grid refinement reported.
Also: FLOAT values of the test-function lower bound |<wF, phi>| / ||D phi||_2 <= L(F) for phi = psi(r/T) sin(theta), psi a C^1 bump on [1/2, 2],
at T = 2^20, 2^30, 2^35 (the lead's 06:10Z request to the verifier), and the leading-sector-only value for comparison with the lead's FLOAT.
Usage: wnorm_float.py farfield.json [du]"""
import sys, json, math
from fractions import Fraction as Fr
import numpy as np

def load_sectors(path, exp_min=-2.6):
    d = json.load(open(path)); E = d['residual_sectors_E']; secs = []
    for key, s in E.items():
        ex = float(Fr(s['exponent'])); ser = {int(k): v['float'] for k, v in s['series'].items()}
        if ser and ex > exp_min: secs.append((key, ex, ser))
    return secs

def L_estimate(secs, R=2.0**35, du=0.002, umin=0.0, umax=75.0, modes=None, verbose=False):
    u = np.arange(umin, umax + du/2, du); r = np.exp(u); n = len(u)
    w = (1 + (r/R)**2)**(-1.1)
    ks = sorted({k for (_, _, ser) in secs for k in ser}) if modes is None else modes
    tot = 0.0; per_mode = {}
    tw = np.full(n, du); tw[0] = tw[-1] = du/2         # trapezoid weights in u
    for k in ks:
        gk = np.zeros(n)
        for (_, ex, ser) in secs:
            if k in ser: gk += ser[k]*r**ex
        gk *= w
        wgt = gk*r*r*tw                                # g_k(t) t dt = g_k e^(2u) du
        q = math.exp(-k*du)
        A = np.empty(n); B = np.empty(n); acc = 0.0
        for i in range(n): acc = acc*q + wgt[i]; A[i] = acc          # sum_(j<=i) wgt_j (r_j/r_i)^k
        acc = 0.0
        for i in range(n-1, -1, -1): acc = acc*q + wgt[i]; B[i] = acc  # sum_(j>=i) wgt_j (r_i/r_j)^k
        uk = (A + B - wgt)/(2*k)
        val = math.pi*float(np.sum(wgt*uk)); per_mode[k] = val; tot += val
    return math.sqrt(tot), per_mode

def testfn_bound(secs, T, R=2.0**35, k=1, du=0.0005):
    """|<wF, phi>| / ||D phi||_2 for phi = psi(r/T) sin(k theta), psi(x) = bump on [1/2, 2]: psi = sin^2(pi (log2 x + 1)/2) on [1/2,2], 0 outside."""
    u = np.arange(math.log(T/2), math.log(2*T) + du/2, du); r = np.exp(u); x = r/T
    psi = np.sin(math.pi*(np.log2(x) + 1)/2)**2
    dpsi = 2*np.sin(math.pi*(np.log2(x) + 1)/2)*np.cos(math.pi*(np.log2(x) + 1)/2)*math.pi/(2*math.log(2)*x)   # d psi/dx
    w = (1 + (r/R)**2)**(-1.1); gk = np.zeros_like(r)
    for (_, ex, ser) in secs:
        if k in ser: gk += ser[k]*r**ex
    tw = np.full(len(u), du); tw[0] = tw[-1] = du/2
    num = math.pi*float(np.sum(w*gk*psi*r*r*tw))                                   # <wF, phi> = pi int g_k psi r dr
    den = math.sqrt(math.pi*float(np.sum(((dpsi/T)**2 + (k*psi/r)**2)*r*r*tw)))    # ||D phi||_2
    return abs(num)/den, num, den

if __name__ == '__main__':
    path = sys.argv[1]; du = float(sys.argv[2]) if len(sys.argv) > 2 else 0.002
    secs = load_sectors(path)
    print('sectors used (key, exponent, harmonics):', [(k, round(ex, 4), len(s)) for k, ex, s in secs])
    lead_only = [s for s in secs if s[0] == '1,0']
    for label, S in (('leading sector (1,0) only', lead_only), ('all sectors with exponent > -2.6', secs)):
        for d_ in (2*du, du):
            L, pm = L_estimate(S, du=d_)
            print('%s, du = %g: L = ||wF||_Hdot^-1 about %.4e ; 2^26.5 L about %.4e ; ratio to eta = 2^-46: %.3e ; modes k=1,3,5: %s' % (label, d_, L, 2**26.5*L, 2**26.5*L/2**-46, {k: '%.3e' % math.sqrt(pm[k]) for k in (1, 3, 5) if k in pm}))
    # sensitivity to the lower cutoff and the upper limit
    for umin, umax in ((math.log(2.0), 75.0), (0.0, 60.0), (math.log(1e4), 75.0)):
        L, _ = L_estimate(secs, du=du, umin=umin, umax=umax); print('cutoffs r in [%.3g, %.3g]: L about %.4e' % (math.exp(umin), math.exp(umax), L))
    # direct quadrature check of u_1 at one radius against scipy (independent of the recursion)
    try:
        from scipy.integrate import quad
        R = 2.0**35; k = 1
        def g1(t): return (1 + (t/R)**2)**(-1.1)*sum(ser[k]*t**ex for (_, ex, ser) in secs if k in ser)
        for r0 in (1e6, 2.0**35):
            I1 = quad(lambda v: math.exp((k+2)*v)*g1(math.exp(v)), 0.0, math.log(r0), limit=400)[0]
            I2 = quad(lambda v: math.exp((2-k)*v)*g1(math.exp(v)), math.log(r0), 75.0, limit=400)[0]
            uq = (r0**(-k)*I1 + r0**k*I2)/(2*k)
            u = np.arange(0.0, 75.0 + du/2, du); r = np.exp(u); i0 = int(round(math.log(r0)/du))
            w = (1 + (r/R)**2)**(-1.1); gk = np.zeros_like(r)
            for (_, ex, ser) in secs:
                if k in ser: gk += ser[k]*r**ex
            gk *= w; tw = np.full(len(u), du); tw[0] = tw[-1] = du/2; wgt = gk*r*r*tw; q = math.exp(-k*du)
            A = 0.0
            for i in range(i0+1): A = A*q + wgt[i]
            B = 0.0
            for i in range(len(u)-1, i0-1, -1): B = B*q + wgt[i]
            print('u_1(r=%.3g): quad %.6e recursion %.6e (rel diff %.1e)' % (r0, uq, (A + B - wgt[i0])/(2*k), abs(uq - (A+B-wgt[i0])/(2*k))/abs(uq)))
    except Exception as e: print('quad check skipped:', e)
    for T in (2.0**20, 2.0**30, 2.0**35):
        b, num, den = testfn_bound(secs, T)
        print('test function psi(r/T) sin(theta), T = 2^%d: |<wF,phi>|/||Dphi|| about %.4e (<wF,phi> %.4e, ||Dphi|| %.4e); times 2^26.5/6: %.4e' % (round(math.log2(T)), b, num, den, 2**26.5/6*b))
