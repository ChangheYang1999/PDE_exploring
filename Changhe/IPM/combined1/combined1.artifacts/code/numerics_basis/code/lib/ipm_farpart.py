"""Exact-formula far-field contributions of the residual sectors beyond a radius R (lane c1-n1).
F(r,theta) = sum_s r^(alpha_s) E_s(theta) for r > 1 (sector expansion, finite in h for a finite basis, truncated in q at qmax).
int_{r>R} int_0^{2pi} w(r)^2 F^2 r dr dtheta with w = 1 (||F||_2^2) or w = r (||rF||_2^2):
 = sum_{s,s'} <E_s, E_s'> R^(alpha_s+alpha_s'+2+2k) / (-(alpha_s+alpha_s'+2+2k)),  <E_s,E_s'> = pi sum_m e_m e'_m (full circle), k = 0 or 1.
Requires alpha_s + alpha_s' + 2 + 2k < 0 for every pair with nonzero product (otherwise infinite).  Evaluated with mpmath at 50 digits.
"""
import mpmath as mp
import ipm_exact as X
mp.mp.dps = 50

def far_parts(E, R, kpow=(0, 1)):
    """E: dict exponent(mpq) -> sine dict (mpq). Returns dict kpow -> mpf value of the integral (or inf), and the list of exponents used."""
    keys = [ex for ex in E if E[ex]]
    out = {}
    for k in kpow:
        tot = mp.mpf(0); infinite = False
        for i, a in enumerate(keys):
            for b in keys[i:]:
                ip = sum((X.qfloat(E[a].get(m, 0))*X.qfloat(v) for m, v in E[b].items()), 0.0)
                # exact inner product with mpf for precision
                ipm = mp.mpf(0)
                for m, v in E[b].items():
                    u = E[a].get(m, None)
                    if u is not None: ipm += mp.mpf(int(u.numerator))/int(u.denominator)*mp.mpf(int(v.numerator))/int(v.denominator)
                if ipm == 0: continue
                ex = mp.mpf(int((a+b).numerator))/int((a+b).denominator)+2+2*k
                if ex >= 0: infinite = True; continue
                term = mp.pi*ipm*mp.power(R, ex)/(-ex)
                tot += term if a == b else 2*term
        out[k] = mp.inf if infinite else tot
    return out

def report_far(c, terms, R, qmax=8, exp_min=None):
    """exp_min: sectors below it are dropped (their contribution beyond R is bounded by the next omitted exponent; default -6)"""
    if exp_min is None: exp_min = X.mpq(-6)
    E, dens, strm, moments = X.residual_sectors(c, terms, qmax, exp_min=exp_min)
    fp = far_parts(E, R)
    return {'R': R, 'qmax': qmax, 'F2_far': (None if fp[0] == mp.inf else float(fp[0])), 'rF2_far': (None if fp[1] == mp.inf else float(fp[1])),
            'F2_far_str': mp.nstr(fp[0], 20), 'rF2_far_str': mp.nstr(fp[1], 20)}


def hminus1_far_sector(E, e, T):
    """Exact Hdot^-1 norm squared of the zero-extended exterior sector 1_{r>T} r^e E(theta), E = sum_k b_k sin(k theta) (full circle):
    pi T^(2e+4)/(-2e-4) sum_k b_k^2/(k (k - e - 2))  for e < -2 (referee formula, astra 2026-10-28T23:44Z; consistent with the mode kernel (1/2k)(r_</r_>)^k).
    Returns mpf (inf if e >= -2)."""
    ef = mp.mpf(int(e.numerator))/int(e.denominator) if hasattr(e, 'numerator') else mp.mpf(e)
    if ef >= -2: return mp.inf
    tot = mp.mpf(0)
    for k, v in E.items():
        bk = mp.mpf(int(v.numerator))/int(v.denominator)
        tot += bk*bk/(k*(k-ef-2))
    return mp.pi*mp.power(T, 2*ef+4)/(-2*ef-4)*tot
