"""Far-field (tail) diagnostics for 860 T1 states, version 3: EXACT RATIONAL engine (SPEC section 12 v9.3/v9.4, v9.13 (c), lead rulings 09:16Z on
verifier topics 39/43; lead pre-audit F17). Monitor only: no E_N constraint, penalty, cutoff change or loss change follows from these numbers.

Inputs: the 860 canonical coefficients a_{I(j,m,k)} as exact rationals of their stored decimal (or binary64) values, c_l as the exact rational of its
binary64 value. gamma = 1/c, lambda = 1 - gamma, p_j = (3 + gamma - j lambda)/2.
Binomial tail (r > 1): r^(2k)(1+r^2)^(p_j-k) = sum_q binom(p_j-k, q) r^(2p_j-2q); potential sector (j,q): C_{j,q}(theta) = sum_m C_{m,j,q} cos(2m theta),
C_{m,j,q} = sum_k a_{m,k,j} binom(p_j-k, q), exponent s = 2p_j - 2q = 3 + alpha_{j,q}, alpha_{j,q} = gamma - j lambda - 2q.
Density rule (rho = -d_y Lap chi): a term C r^s cos(n theta) gives -C(s^2-n^2)(s-2-n)/2 at sin((n+1)theta) and +C(s^2-n^2)(s-2+n)/2 at sin((n-1)theta), exponent s-3.
Stream rule (psi = d_x d_y chi): +C(s-n)(s-n-2)/4 at sin((n+2)theta) and -C(s+n)(s+n-2)/4 at sin((n-2)theta), exponent s-2 (negative harmonics folded, sin(-k) = -sin(k)).
Transport residual sector E_{h,q}: linear part (c alpha_{h,q} - 1) F_{h,q} (h <= 3) plus, over stream sectors (i,u) and density sectors (j,v) with i+j+1 = h, u+v = q,
(alpha_{i,u}+1) Phi_{i,u} F_{j,v}' - alpha_{j,v} Phi_{i,u}' F_{j,v}. E_{0,0} = 0 is a stated identity (c gamma = 1 and no pair feeds h = 0): structural zero.
Exact grouping of equal exponents (Fractions) over h = 0..7, q = 0..qmax; the leading power is the largest exponent with a nonzero group; it is DETERMINED only if it
exceeds the largest omitted exponent gamma - 2(qmax+1) (completeness, topic 43 step 6); otherwise it is reported only as a candidate. Growth fields are null unless
determined. Every reported float is checked for representability (overflow/underflow from a nonzero exact value -> null with the reason and a decimal string); the
report is strict-JSON safe. Norms are rounded to binary64 at the end only. The Poisson sector identity -Phi'' - (alpha+1)^2 Phi = alpha cos F - sin F' is verified
exactly for every sector (an internal consistency check of the rules).
"""
import math
from fractions import Fraction
from decimal import Decimal, localcontext

VERSION = 'farfield860_v3_exact_rational_topic43'
NEAR_COLLISION = Fraction(1, 10**6)
A_REF = 23.95065822465609
PI50 = Decimal('3.14159265358979323846264338327950288419716939937510')

def index(j, m, k):
    if not (0 <= j <= 3 and 0 <= m <= 9 and m <= k <= 25): raise ValueError('triple outside the 860 family')
    return 215*j+26*m-m*(m-1)//2+(k-m)

def frac(v):
    """Exact rational of a stored value: Decimal/str via Decimal, float via Fraction(float), int/Fraction as is."""
    if isinstance(v, Fraction): return v
    if isinstance(v, (int,)) and not isinstance(v, bool): return Fraction(v)
    if isinstance(v, float): return Fraction(v)
    return Fraction(Decimal(str(v)))

def binom(p, q):
    out = Fraction(1)
    for i in range(q): out = out*(p-i)/(i+1)
    return out

def _add(d, k, v):
    if v == 0: return
    if k < 0: k, v = -k, -v
    if k == 0: return
    d[k] = d.get(k, 0)+v
    if d[k] == 0: del d[k]

def density_from_potential(C, s):
    """sine dict (odd harmonics) of -d_y Lap (sum_n C_n r^s cos n theta), exponent s-3."""
    F = {}
    for n, c in C.items():
        _add(F, n+1, -c*(s*s-n*n)*(s-2-n)/2); _add(F, n-1, c*(s*s-n*n)*(s-2+n)/2)
    return F

def stream_from_potential(C, s):
    """sine dict (even harmonics) of d_x d_y (sum_n C_n r^s cos n theta), exponent s-2."""
    P = {}
    for n, c in C.items():
        _add(P, n+2, c*(s-n)*(s-n-2)/4); _add(P, n-2, -c*(s+n)*(s+n-2)/4)
    return P

def dsin(S):
    """theta-derivative of a sine series: cosine dict {k: k s_k}."""
    return {k: k*v for k, v in S.items()}

def sin_times_cos(S, Cc):
    """(sum s_a sin a)(sum c_b cos b) = sum s_a c_b [sin(a+b) + sin(a-b)]/2 -> sine dict."""
    out = {}
    for a, sa in S.items():
        for b, cb in Cc.items(): _add(out, a+b, sa*cb/2); _add(out, a-b, sa*cb/2)
    return out

def series_sum(*dicts):
    out = {}
    for d in dicts:
        for k, v in d.items(): _add(out, k, v)
    return out

def scale(d, f): return {k: v*f for k, v in d.items()} if f != 0 else {}

def norm2_over_pi(S):
    """||sum s_k sin k theta||^2_{L2(0,pi/2)} / pi = (1/4) sum s_k^2 for odd k (exact rational)."""
    return sum((v*v for v in S.values()), Fraction(0))/4

def quotient_norm2_over_pi(S):
    """||E/sin theta||^2 / pi with E = sum e_k sin k theta (odd k): E/sin = d_0 + sum_{j>=1} d_j cos 2j theta, d_0 = sum e_k, d_j = 2 sum_{k>=2j+1} e_k; norm^2 = pi(d_0^2/2 + sum d_j^2/4)."""
    if not S: return Fraction(0)
    kmax = max(S); d0 = sum(S.values(), Fraction(0)); tot = d0*d0/2
    for j in range(1, (kmax-1)//2+1):
        dj = 2*sum((v for k, v in S.items() if k >= 2*j+1), Fraction(0)); tot += dj*dj/4
    return tot

def to_float(x, what):
    """Representability check: a nonzero exact value that rounds to 0 or overflows gives (None, reason, decimal string)."""
    if isinstance(x, Fraction):
        if x == 0: return 0., None, '0'
        try: f = float(x)
        except OverflowError: f = math.inf
        with localcontext() as cx:
            cx.prec = 30; dstr = str(Decimal(x.numerator)/Decimal(x.denominator))
        if math.isinf(f): return None, 'overflow: exact value not representable in binary64', dstr
        if f == 0.: return None, 'underflow: nonzero exact value rounds to 0 in binary64', dstr
        return f, None, dstr
    if isinstance(x, Decimal):
        if x == 0: return 0., None, '0'
        f = float(x); dstr = format(x, '.30e')
        if math.isinf(f): return None, 'overflow: exact value not representable in binary64', dstr
        if f == 0.: return None, 'underflow: nonzero exact value rounds to 0 in binary64', dstr
        return f, None, dstr
    raise TypeError(type(x))

def sqrt_pi_times(z, digits=60):
    """sqrt(pi z) for a nonnegative rational z, as Decimal at `digits`."""
    with localcontext() as cx:
        cx.prec = digits
        if z == 0: return Decimal(0)
        return (PI50*Decimal(z.numerator)/Decimal(z.denominator)).sqrt()

def analyze(a_values, cl, qmax=3, angular_nodes=None):
    """a_values: 860 stored coefficients in canonical order (Decimal/str/float/Fraction); cl: binary64 c_l. Returns the monitor report (strict-JSON safe)."""
    a = [frac(v) for v in a_values]
    if len(a) != 860: raise ValueError('860 canonical coefficients required')
    c = Fraction(float(cl)); gamma = 1/c; lam = 1-gamma; p = [(3+gamma-j*lam)/2 for j in range(4)]
    def alpha(h, q): return gamma-h*lam-2*q
    # potential, density and stream sectors (j <= 3)
    Cs = {}; F = {}; Phi = {}; moments = {}; exact_zero_moment = {}
    for j in range(4):
        for q in range(qmax+1):
            C = {}
            for m in range(10):
                v = sum((a[index(j, m, k)]*binom(p[j]-k, q) for k in range(m, 26)), Fraction(0))
                moments['%d,%d,%d' % (m, j, q)] = v
                if v != 0: C[2*m] = v
            s = 2*p[j]-2*q; Cs[j, q] = C; F[j, q] = density_from_potential(C, s); Phi[j, q] = stream_from_potential(C, s)
    # Poisson sector identity (exact): -Phi'' - (alpha+1)^2 Phi = alpha cos F - sin F'
    poisson_ok = True; poisson_fail = []
    for (j, q), P in Phi.items():
        al = alpha(j, q); lhs = {k: (k*k-(al+1)**2)*v for k, v in P.items() if (k*k-(al+1)**2)*v != 0}
        Fj = F[j, q]; rhs = series_sum(scale(sin_times_cos(Fj, {1: Fraction(1)}), al), scale(sin_times_cos({1: Fraction(1)}, dsin(Fj)), -1))
        if series_sum(lhs, scale(rhs, -1)): poisson_ok = False; poisson_fail.append([j, q])
    # transport residual sectors
    E = {}; parts = {}
    for h in range(8):
        for q in range(qmax+1):
            terms = []
            if h <= 3: terms.append(scale(F[h, q], c*alpha(h, q)-1))
            for i in range(4):
                jj = h-1-i
                if not (0 <= jj <= 3): continue
                for u in range(q+1):
                    v = q-u; ai = alpha(i, u); aj = alpha(jj, v)
                    terms.append(scale(sin_times_cos(Phi[i, u], dsin(F[jj, v])), ai+1)); terms.append(scale(sin_times_cos(F[jj, v], dsin(Phi[i, u])), -aj))
            E[h, q] = series_sum(*terms); parts[h, q] = len(terms)
    # sectors, exact grouping, leading power
    omitted = alpha(0, qmax+1); sectors = []; groups = {}
    for (h, q), S in E.items():
        ex = alpha(h, q); zero = not S
        if (h, q) == (0, 0): cls = 'structural_zero'; reason = 'identity: c gamma = 1 makes the linear coefficient vanish and no transport pair feeds h = 0 (SPEC section 12 stated identity)'
        elif zero: cls = 'exact_zero'; reason = 'all exact rational sine coefficients are zero (exact arithmetic on the stored inputs)'
        else: cls = 'nonzero'; reason = None
        n2 = norm2_over_pi(S); nf, nreason, nstr = to_float(sqrt_pi_times(n2), 'norm') if n2 else (0., None, '0')
        sectors.append({'h': h, 'q': q, 'exponent_exact': '%d/%d' % (ex.numerator, ex.denominator), 'exponent': float(ex), 'classification': cls, 'reason': reason, 'norm_L2': nf, 'norm_L2_null_reason': nreason, 'norm_L2_decimal': nstr, 'terms': parts[h, q], 'max_harmonic': max(S) if S else 0})
        groups.setdefault(ex, []).append((h, q))
    grouped = []
    for ex in sorted(groups, reverse=True):
        members = groups[ex]; S = series_sum(*[E[hq] for hq in members]); n2 = norm2_over_pi(S); nf, nreason, nstr = to_float(sqrt_pi_times(n2), 'norm') if n2 else (0., None, '0')
        grouped.append({'exponent_exact': '%d/%d' % (ex.numerator, ex.denominator), 'exponent': float(ex), 'members_hq': [list(m) for m in members], 'exact_collision': len(members) > 1, 'nonzero': bool(S), 'group_norm_L2': nf, 'group_norm_L2_null_reason': nreason, 'group_norm_L2_decimal': nstr, '_series': S, '_exact': ex})
    nonzero = [g for g in grouped if g['nonzero']]
    lead = nonzero[0] if nonzero else None
    determined = bool(lead is not None and lead['_exact'] > omitted)
    cand = None if lead is None else lead['_exact']
    if determined: status = 'determined: exact nonzero group above the omitted bound gamma - 2(qmax+1); every group above it is exactly zero'
    elif lead is None: status = 'undetermined: every retained sector (h <= 7, q <= qmax) is exactly zero; the leading power lies at or below the omitted bound'
    else: status = 'candidate only: the largest nonzero retained exponent does not exceed the omitted bound gamma - 2(qmax+1)'
    sign = None if not determined else ((cand > 0)-(cand < 0))
    growth = None if not determined else ('grows' if sign > 0 else ('bounded_nondecaying' if sign == 0 else 'decays'))
    lead_report = {'status': status, 'determined': determined, 'exponent': (float(cand) if determined else None), 'exponent_exact': ('%d/%d' % (cand.numerator, cand.denominator) if determined else None),
                   'candidate_exponent_exact': (None if cand is None or determined else '%d/%d' % (cand.numerator, cand.denominator)), 'candidate_exponent': (None if cand is None or determined else float(cand)),
                   'sectors_hq': (lead['members_hq'] if determined else None), 'coefficient_L2': (lead['group_norm_L2'] if determined else None), 'coefficient_L2_null_reason': (lead['group_norm_L2_null_reason'] if determined else None),
                   'growth': growth, 'largest_omitted_exponent_exact': '%d/%d' % (omitted.numerator, omitted.denominator), 'largest_omitted_exponent': float(omitted), 'qmax': qmax,
                   'nominal_E1_power_2gamma_minus_1_exact': '%d/%d' % ((2*gamma-1).numerator, (2*gamma-1).denominator), 'nominal_equals_actual': (determined and cand == 2*gamma-1) if determined else None,
                   'rule': 'exact rational arithmetic on the stored inputs (verifier topic 43, lead review 09:15Z); growth and actual-power fields are null unless determined'}
    # E_N reports (N = 1, 2, 3: sectors (N, 0)), F_0 norm, I_N in Decimal with representability checks
    f0_2 = norm2_over_pi(F[0, 0]); F0_dec = sqrt_pi_times(f0_2); f0f, f0reason, f0str = to_float(F0_dec, 'F0') if f0_2 else (0., None, '0')
    Ereps = {}
    for N in (1, 2, 3):
        S = E[N, 0]; n2 = norm2_over_pi(S); Ndec = sqrt_pi_times(n2); nf, nreason, nstr = to_float(Ndec, 'E') if n2 else (0., None, '0')
        rep2 = sum((v*v for k, v in S.items() if k <= 19), Fraction(0))/4; unr2 = sum((v*v for k, v in S.items() if k > 19), Fraction(0))/4
        repf, rep_reason, rep_dec = to_float(sqrt_pi_times(rep2), 'rep') if rep2 else (0., None, '0'); unrf, unr_reason, unr_dec = to_float(sqrt_pi_times(unr2), 'unr') if unr2 else (0., None, '0')
        I_N = None; I_reason = None; I_str = None
        if f0_2 == 0: I_reason = '||F_0|| = 0'
        elif n2 == 0: I_N = 0.
        else:
            with localcontext() as cx:
                cx.prec = 60; val = Decimal(A_REF)**N*Ndec/(F0_dec**(N+1))
            I_N, I_reason, I_str = to_float(val, 'I_N')
        coeffs = {}; unrep = {}
        for k, v in sorted(S.items()):
            fv, reason, dstr = to_float(v, 'coef')
            if fv is None: unrep[str(k)] = {'reason': reason, 'decimal': dstr}; coeffs[str(k)] = None
            else: coeffs[str(k)] = fv
        unres_frac, frac_reason, frac_dec = 0., None, '0'
        if (rep2+unr2) > 0:
            with localcontext() as cx:
                cx.prec = 60; q = Fraction(unr2)/(rep2+unr2); unres_frac, frac_reason, frac_dec = to_float((Decimal(q.numerator)/Decimal(q.denominator)).sqrt(), 'frac')   # (b): sqrt of the exact fraction before binary64
        Ereps[str(N)] = {'L2': nf, 'L2_null_reason': nreason, 'L2_decimal': nstr, 'represented_harmonics_le19_L2': repf, 'represented_harmonics_le19_L2_null_reason': rep_reason, 'represented_harmonics_le19_L2_decimal': rep_dec, 'unresolved_harmonics_gt19_L2': unrf, 'unresolved_harmonics_gt19_L2_null_reason': unr_reason, 'unresolved_harmonics_gt19_L2_decimal': unr_dec, 'unresolved_fraction': unres_frac, 'unresolved_fraction_null_reason': frac_reason, 'unresolved_fraction_decimal': frac_dec,
                        'max_harmonic': max(S) if S else 0, 'scale_invariant_ratio_I_N': I_N, 'I_N_null_reason': I_reason, 'I_N_decimal': I_str, 'density_radial_power': float(alpha(N, 0)), 'density_radial_power_exact': '%d/%d' % (alpha(N, 0).numerator, alpha(N, 0).denominator),
                        'sine_coefficients_odd': {k: v for k, v in coeffs.items() if v is None or v}, 'sine_coefficients_unrepresentable': unrep}
    # leading-sector angular profile and quotient norm (for the direct large-r cross-check and the tail estimate)
    lead_prof = None; lead_quot = None; lead_prof_unrep = None; lead_quot_reason = None
    if determined:
        S = lead['_series']; lead_prof = {}; lead_prof_unrep = {}
        for k, v in sorted(S.items()):
            fv, reason, dstr = to_float(v, 'coef')
            if fv is None: lead_prof[str(k)] = None; lead_prof_unrep[str(k)] = {'reason': reason, 'decimal': dstr}
            elif fv: lead_prof[str(k)] = fv
        lead_quot, lead_quot_reason, lead_quot_dec = to_float(sqrt_pi_times(quotient_norm2_over_pi(S)), 'quot')
    # collisions, near collisions, Poisson resonances (exact)
    near = []
    for i in range(len(grouped)):
        for j in range(i+1, len(grouped)):
            dF = abs(grouped[i]['_exact']-grouped[j]['_exact'])
            if dF != 0 and dF < NEAR_COLLISION: near.append({'exponents_exact': [grouped[i]['exponent_exact'], grouped[j]['exponent_exact']], 'difference': float(dF), 'members': [grouped[i]['members_hq'], grouped[j]['members_hq']], 'norms': [grouped[i]['group_norm_L2'], grouped[j]['group_norm_L2']], 'merged': False})
    resonances = [[list(hq), s_['exponent_exact']] for hq, s_ in zip(E.keys(), sectors) if any(alpha(*hq)+1 == n or alpha(*hq)+1 == -n for n in range(2, 60, 2))]
    for g in grouped: g.pop('_series'); g.pop('_exact')
    with localcontext() as cx:
        cx.prec = 32; moments_str = {k: (str(Decimal(v.numerator)/Decimal(v.denominator)) if v else '0') for k, v in moments.items()}
    return {'version': VERSION, 'cl': float(cl), 'cl_exact': '%d/%d' % (c.numerator, c.denominator), 'gamma': float(gamma), 'lambda': float(lam), 'p': [float(x) for x in p], 'qmax': qmax,
            'nominal_E1_density_power_2gamma_minus_1': float(2*gamma-1), 'F0_L2': f0f, 'F0_L2_null_reason': f0reason, 'F0_L2_decimal': f0str, 'E': Ereps, 'tail_moments_C_mjq': moments_str,
            'poisson_sector_identity_exact': poisson_ok, 'poisson_identity_failures': poisson_fail, 'poisson_layer_checks_passed': poisson_ok,
            'sectors': sectors, 'exponent_groups_exact': grouped, 'actual_leading_density_power': lead_report,
            'original_density_residual_grows': (None if not determined else bool(sign > 0)), 'original_density_residual_grows_note': 'null unless the leading power is determined (lead ruling 09:16Z)',
            'leading_sector_sine_coefficients_odd': lead_prof, 'leading_sector_sine_coefficients_unrepresentable': lead_prof_unrep, 'leading_sector_quotient_L2': lead_quot, 'leading_sector_quotient_L2_null_reason': lead_quot_reason,
            'exact_exponent_collisions': [[g['members_hq'], g['exponent_exact']] for g in grouped if g['exact_collision']], 'near_collisions_not_merged': near, 'poisson_resonances': resonances,
            'monitor_only': True, 'never_raises_on_finite_inputs': True}
