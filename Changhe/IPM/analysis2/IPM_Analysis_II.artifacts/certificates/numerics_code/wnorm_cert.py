"""CERTIFIED lower bound for the weighted negative-order norm of the exact state-131 residual by a test function.
  L(F) := ||w F||_{Hdot^-1(R^2)} >= |<w F, phi>| / ||D phi||_2   for every phi in Hdot^1 (duality),
  w = (1 + r^2/R^2)^(-11/10), R = 2^35 (verifier V073/V081 weight), phi = psi(r/T) sin(theta), psi(x) = sin^2(pi (log2 x + 1)/2) on [1/2, 2], 0 outside
  (C^1 with piecewise-smooth derivative, compactly supported in the annulus T/2 <= r <= 2T: phi is in Hdot^1 and in the odd-y even-x parity class).
Inputs: exact state file (cl, 860 canonical rationals), the exact far-field expansion F = sum_{h<=7, q<=Q} r^alpha(h,q) E_(h,q)(theta) (farfield_exact.expand,
valid for r > 1) with the rigorous remainder bound |F - F_Q| <= B_tail(R0) r^(p2) for r >= R0 (farfield_F_cert.py pieces (a), (b), (c); p2 = 2 gamma - 1).
<w F, phi> = pi int_{T/2}^{2T} w(r) f_1(r) psi(r/T) r dr with f_1 the sin(theta) coefficient of F_Q, plus the remainder, bounded in absolute value by
4 int w psi r B_tail r^p2 dr (|sin theta| integrates to 4 over the circle). All integrals by rigorous arb integration (acb.integral, python-flint).
||D phi||_2^2 = pi int_{1/2}^{2} [psi'(x)^2 + psi(x)^2/x^2] x dx (independent of T; the x-derivative of psi is continuous and piecewise analytic).
Output: certified lower bound L(F) >= lower(T) for T in the list; also the FLOAT value for comparison.
Usage: wnorm_cert.py state_exact.json Q T_log2_list(comma)   e.g. wnorm_cert.py data/state131_exact.json 3 20,30,35"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
from flint import arb, acb, ctx, fmpq
import farfield_exact as FE

import farfield_F_cert as FC
from farfield_bounds import sector_fields, sup_trig, A

def Aq(fr): return arb(fmpq(fr.numerator, fr.denominator))

def tail_bound_coeff(cl, a, p, Q, R0):
    """B_tail(R0): |F - F_Q| <= B_tail r^p2 for all r >= R0 (pieces (a) linear tail, (b) cross terms u+v > Q, (c) nonlinear tails), copied from farfield_F_cert.py."""
    g = Fr(1)/cl; lam = 1-g; p2 = 2*g-1
    def alpha(h, q): return g - h*lam - 2*q
    Rz = arb(R0); sectors, _ = sector_fields(cl, a, Q)
    lin = arb(0)
    for j in range(4):
        for q in range(Q+1, Q+41):
            s = 2*p[j] - 2*q; al = s - 3
            lin += (A(cl)*abs(A(al)) + 1)*FC.tail_coeff_bound(cl, a, p, j, q, 3)*Rz**A(al - p2)
        qq = Q+41; s = 2*p[j] - 2*qq; al = s - 3
        ratio = (1 + arb(27)/(qq+1))*(1 + arb(2)/(2*qq - 2))**4*Rz**-2
        assert ratio < 1
        lin += (A(cl)*abs(A(al)) + 1)*FC.tail_coeff_bound(cl, a, p, j, qq, 3)*Rz**A(al - p2)/(1 - ratio)
    supU = {}; supG = {}
    for (j, q), f in sectors.items():
        supU[(j, q)] = sup_trig(f['U1'][1]) + sup_trig(f['U2'][1]); supG[(j, q)] = sup_trig(f['rho_x'][1]) + sup_trig(f['rho_y'][1])
    cross = arb(0)
    for (i, u) in sectors:
        for (jj, v) in sectors:
            if u + v <= Q: continue
            cross += supU[(i, u)]*supG[(jj, v)]*Rz**A(alpha(i, u) + alpha(jj, v) - 1 - p2)
    tails = arb(0); UT = {}; GT = {}
    for j in range(4):
        UT[j] = (FC.tail_sum(cl, a, p, j, 3, Q, R0, 2*p[j] - 2*(Q+1) - 3), 2*p[j] - 2*(Q+1) - 3)
        GT[j] = (FC.tail_sum(cl, a, p, j, 4, Q, R0, 2*p[j] - 2*(Q+1) - 4), 2*p[j] - 2*(Q+1) - 4)
    for (i, u) in sectors:
        for j in range(4):
            tails += supU[(i, u)]*GT[j][0]*Rz**A(alpha(i, u) + GT[j][1] - p2)
            tails += UT[j][0]*supG[(i, u)]*Rz**A(UT[j][1] + alpha(i, u) - 1 - p2)
    for i in range(4):
        for j in range(4): tails += UT[i][0]*GT[j][0]*Rz**A(UT[i][1] + GT[j][1] - p2)
    return lin + cross + tails

def psi_c(z):            # psi as an analytic function of complex z near the positive reals (restricted to [1/2, 2] by the integration limits)
    return (acb.pi()*(z.log()/arb(2).log() + 1)/2).sin()**2
def dpsi_c(z):           # d psi / dx
    u = acb.pi()*(z.log()/arb(2).log() + 1)/2
    return 2*u.sin()*u.cos()*acb.pi()/(2*arb(2).log()*z)

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    Q = int(sys.argv[2]); Ts = [2.0**int(v) for v in sys.argv[3].split(',')]
    ctx.prec = 256
    g = Fr(1)/cl; lam = 1-g; p = [(3+g-j*lam)/2 for j in range(4)]; p2 = 2*g-1
    X = FE.expand(cl, a, qmax=Q, hmax=7)
    e1 = {(h, q): X['E'][(h, q)].get(1, Fr(0)) for (h, q) in X['E']}
    e1 = {k: v for k, v in e1.items() if v != 0}
    print('k = 1 sine coefficients of the exact sectors (h,q):', {k: '%.6e' % float(v) for k, v in sorted(e1.items())})
    R = arb(2)**35
    # ||D phi||_2 (T-independent)
    def integrand_D(z, analytic):
        if analytic and not (z.real > 0): return acb('nan')          # all expressions are analytic on Re z > 0 (astra referee: guard required by the acb_calc contract)
        return (dpsi_c(z)**2 + psi_c(z)**2/z**2)*z
    I_D = acb.integral(integrand_D, arb(1)/2, 2)
    normD = (acb.pi()*I_D).real.sqrt()
    print('||D phi||_2 = ', normD.str(20), '(ball)')
    out = {'weight': 'w = (1 + r^2/2^70)^(-11/10)', 'phi': 'psi(r/T) sin(theta), psi = sin^2(pi (log2(r/T) + 1)/2) on [T/2, 2T] (C^1, not C^2)', 'normDphi_ball': normD.str(25), 'normDphi_closed_form': 'sqrt(pi/4 (pi^2/log 2 + 3 log 2)) (astra)', 'Q': Q, 'results': {}}
    for T in Ts:
        Tz = arb(T); lo, hi = Tz/2, 2*Tz
        Btail = tail_bound_coeff(cl, a, p, Q, float(lo))
        def integrand(z, analytic):
            if analytic and not (z.real > 0): return acb('nan')
            w = (1 + z*z/(R*R))**(-arb(11)/10)
            f1 = sum((Aq(v)*z**Aq(X['alpha'](h, q)) for (h, q), v in e1.items()), acb(0))
            return w*f1*psi_c(z/Tz)*z
        I = acb.integral(integrand, lo, hi)
        main = acb.pi()*I
        def integrand_tail(z, analytic):
            if analytic and not (z.real > 0): return acb('nan')
            w = (1 + z*z/(R*R))**(-arb(11)/10)
            return w*psi_c(z/Tz)*z*z**Aq(p2)
        I_t = acb.integral(integrand_tail, lo, hi)
        rem = 4*Btail*I_t.real                       # |<w (F - F_Q), phi>| <= 4 B_tail int w psi r^(1+p2) dr
        pairing_abs_lower = arb(abs(main.real).lower()) - arb(rem.upper())
        lower = arb((pairing_abs_lower/arb(normD.upper())).lower())         # certified lower endpoint (exact binary number)
        def pub(v, sig=7):
            # largest decimal with `sig` significant digits that is certainly below the arb lower endpoint v (checked with arb comparison)
            from decimal import Decimal, ROUND_FLOOR
            d = Decimal(float(v.lower())); e = d.adjusted(); q = Decimal(1).scaleb(e - sig + 1); c = d.quantize(q, rounding=ROUND_FLOOR)
            while not (arb(str(c)) < v): c -= q
            return str(c)
        def pub_up(v, sig=5):
            from decimal import Decimal, ROUND_CEILING
            d = Decimal(float(v.upper())); e = d.adjusted(); q = Decimal(1).scaleb(e - sig + 1); c = d.quantize(q, rounding=ROUND_CEILING)
            while not (arb(str(c)) > v): c += q
            return str(c)
        L_pub = pub(lower); Lc_pub = pub(arb((lower*arb(2)**(arb(53)/2)/6).lower()))
        print('T = 2^%d: <w F_Q, phi> = %s ; remainder bound <= %s ; B_tail(T/2) <= %s' % (round(math.log2(T)), main.real.str(15), pub_up(rem), pub_up(Btail)))
        print('   CERTIFIED (decimals rounded DOWN, checked by arb comparison): L(F) = ||wF||_Hdot^-1 >= %s ; (2^(53/2)/6) L(F) >= %s' % (L_pub, Lc_pub))
        out['results']['2^%d' % round(math.log2(T))] = {'pairing_ball': main.real.str(20), 'remainder_upper_pub': pub_up(rem), 'B_tail_upper_pub': pub_up(Btail), 'L_lower_pub': L_pub, 'L_lower_times_2^26.5_over_6_pub': Lc_pub, 'L_lower_exact_binary_man_exp': [str(lower.lower().man_exp()[0]), int(lower.lower().man_exp()[1])], 'note': 'L_lower_exact_binary_man_exp = [m, e] is the exact binary lower endpoint m*2^e of the certified quotient (replaces the earlier decimal diagnostic, which was a rounded midpoint; verifier V113)'}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'wnorm_cert_131.json'), 'w'), indent=1)
    print('written data/wnorm_cert_131.json')
