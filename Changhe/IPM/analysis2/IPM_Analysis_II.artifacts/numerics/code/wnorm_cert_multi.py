"""CERTIFIED lower bound for L_R(F) = ||w_R F||_{Hdot^-1(R^2)}, w_R = (1 + r^2/R^2)^(-11/10), for the exact state-131 residual, with the VERIFIER's
combined test function (V084/V089/V096; lead's request 06:29Z), recomputed independently from this lane's exact far-field sectors and rigorous
binomial tails (same inputs/methods as code/wnorm_cert.py):
    phi(X) = chi(r/R) sum_{m odd, 1 <= m <= 39} (e_m/d_m) sin(m theta),  chi(t) = (t-1)^2 (2-t)^2 on [1, 2], 0 outside,  d_m = 1/35 + m^2/630,
    e_m = exact sin(m theta) coefficient of the leading residual sector E_(1,0) (exponent p2 = 2 gamma - 1).
L_R(F) >= |<w_R F, phi>| / ||D phi||_2, <w_R F, phi> = pi sum_m (e_m/d_m) int_R^{2R} w_R(r) f_m(r) chi(r/R) r dr (f_m = sin(m theta) coefficient of F_Q,
all exact sectors h <= 7, q <= Q), remainder |<w_R (F - F_Q), phi>| <= B_tail(R) * int_R^{2R} w_R chi r^(1+p2) dr * 2 pi sum_m |e_m/d_m|,
||D phi||_2^2 = pi sum_m (e_m/d_m)^2 int_1^2 [chi'(t)^2 + m^2 chi(t)^2/t^2] t dt.  All integrals by acb.integral (rigorous), 256 bits; published decimals
rounded down and checked by arb comparison.  Usage: wnorm_cert_multi.py state_exact.json Q R_log2_list"""
import sys, os, json, math, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
from flint import arb, acb, ctx, fmpq
import farfield_exact as FE
from wnorm_cert import tail_bound_coeff, Aq

def chi_c(t): return (t - 1)**2*(2 - t)**2
def dchi_c(t): return 2*(t - 1)*(2 - t)**2 - 2*(t - 1)**2*(2 - t)

if __name__ == '__main__':
    path = sys.argv[1]; d = json.load(open(path)); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    Q = int(sys.argv[2]); Rs = [2**int(v) for v in sys.argv[3].split(',')]
    ctx.prec = 256
    g = Fr(1)/cl; lam = 1-g; p = [(3+g-j*lam)/2 for j in range(4)]; p2 = 2*g-1
    X = FE.expand(cl, a, qmax=Q, hmax=7)
    E1 = X['E'][(1, 0)]; modes = sorted(k for k in E1 if E1[k] != 0)
    sha = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    print('input %s sha256 %s ; leading sector modes %s' % (path, sha, modes))
    coef = {m: {(h, q): X['E'][(h, q)].get(m, Fr(0)) for (h, q) in X['E'] if X['E'][(h, q)].get(m, Fr(0)) != 0} for m in modes}
    am = {m: E1[m]/(Fr(1, 35) + Fr(m*m, 630)) for m in modes}
    # gradient norm (R-independent)
    def integrand_D(z, analytic):
        if analytic and not (z.real > 0): return acb('nan')
        return chi_c(z)**2/z
    def integrand_Dp(z, analytic):
        if analytic and not (z.real > 0): return acb('nan')
        return dchi_c(z)**2*z
    I_chi2_over_t = acb.integral(integrand_D, 1, 2).real; I_dchi2_t = acb.integral(integrand_Dp, 1, 2).real
    print('int chi^2/t dt = %s ; int chi\'^2 t dt = %s (lead quotes 1/630 and 1/35: %s %s)' % (I_chi2_over_t.str(15), I_dchi2_t.str(15), (arb(1)/630).str(10), (arb(1)/35).str(10)))
    normD2 = arb.pi()*sum((Aq(am[m])**2*(I_dchi2_t + m*m*I_chi2_over_t) for m in modes), arb(0)); normD = normD2.sqrt()
    out = {'input_sha256': sha, 'test': 'chi(r/R) sum_m (e_m/d_m) sin(m theta), chi = (t-1)^2(2-t)^2 on [1,2], d_m = 1/35 + m^2/630', 'normDphi_ball': normD.str(25), 'Q': Q, 'results': {}}
    print('||D phi||_2 = %s' % normD.str(20))
    for R in Rs:
        Rz = arb(R); lo, hi = Rz, 2*Rz
        Btail = tail_bound_coeff(cl, a, p, Q, float(lo))
        total = acb(0)
        for m in modes:
            def integrand(z, analytic, m=m):
                if analytic and not (z.real > 0): return acb('nan')
                w = (1 + z*z/(Rz*Rz))**(-arb(11)/10)
                fm = sum((Aq(v)*z**Aq(X['alpha'](h, q)) for (h, q), v in coef[m].items()), acb(0))
                return w*fm*chi_c(z/Rz)*z
            I = acb.integral(integrand, lo, hi)
            total += Aq(am[m])*I
        pairing = acb.pi()*total.real
        def integrand_tail(z, analytic):
            if analytic and not (z.real > 0): return acb('nan')
            w = (1 + z*z/(Rz*Rz))**(-arb(11)/10)
            return w*chi_c(z/Rz)*z*z**Aq(p2)
        I_t = acb.integral(integrand_tail, lo, hi).real
        rem = Btail*I_t*2*arb.pi()*sum((abs(Aq(am[m])) for m in modes), arb(0))
        lower = arb((arb(abs(pairing).lower()) - arb(rem.upper()))/arb(normD.upper())).lower(); lower = arb(lower)
        from decimal import Decimal, ROUND_FLOOR
        def pub(v, sig=7):
            dd = Decimal(float(v.lower())); e = dd.adjusted(); q = Decimal(1).scaleb(e - sig + 1); c = dd.quantize(q, rounding=ROUND_FLOOR)
            while not (arb(str(c)) < v): c -= q
            return str(c)
        Lint = int(math.floor(float(lower.lower())))
        while not (arb(Lint) < lower): Lint -= 1
        Lc = arb((lower*arb(2)**(arb(53)/2)/6).lower())
        print('R = 2^%d: pairing <w F_Q, phi> = %s ; remainder <= %s ; B_tail(R) <= %s' % (round(math.log2(R)), pairing.str(20), rem.str(5), Btail.str(5)))
        print('   CERTIFIED: L_R(F) >= %s (integer %d) ; (2^(53/2)/6) L_R(F) >= %s' % (pub(lower), Lint, pub(Lc)))
        out['results']['2^%d' % round(math.log2(R))] = {'pairing_ball': pairing.str(25), 'remainder_upper': rem.str(5), 'B_tail_upper': Btail.str(5), 'L_lower_pub': pub(lower), 'L_lower_int': Lint, 'L_lower_exact_binary_man_exp': [str(lower.lower().man_exp()[0]), int(lower.lower().man_exp()[1])], 'N_lower_pub_2^26.5_over_6': pub(Lc)}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'wnorm_cert_multi_131.json'), 'w'), indent=1)
    print('written data/wnorm_cert_multi_131.json')
