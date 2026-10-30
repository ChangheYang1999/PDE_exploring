"""Exact rational machinery for the S1/IPM profile family (lane c1-n1, own implementation).

Generators: chi = H_m R^(p-m) T(t) cos-structure, H_m = Re (x+iy)^(2m), R = 1+r^2, t = r^2/R,
T(t) = t^h ('mono', h) or t^w P_n(2t-1) ('leg', w, n).  In canonical monomial form a generator is
(m, k, p) with chi = r^(2k) R^(p-k) cos(2m theta), k >= m.  p is an exact rational (mpq).
Fields: psi = chi_xy, rho = -d_y Lap chi = y f, U = (-psi_y, psi_x).
Residual: F(rho) = (c X + U).grad rho - rho, c = c_l.

Far field (r>1): r^(2k) R^(p-k) = sum_q binom(p-k, q) r^(2p-2q).  Potential sector at exponent s=2p-2q is
C(theta) = sum_m C_m cos(2m theta) with C_m = sum_k a_(m,k,p) binom(p-k,q).  Rules for one term C r^s cos(n theta):
  density (exponent s-3):  -C(s^2-n^2)(s-2-n)/2 sin((n+1)th) + C(s^2-n^2)(s-2+n)/2 sin((n-1)th)
  stream  (exponent s-2):  +C(s-n)(s-n-2)/4 sin((n+2)th)     - C(s+n)(s+n-2)/4 sin((n-2)th)
Advection of r^alpha G(theta) (density) by stream r^sigma Phi(theta): r^(sigma+alpha-2) [sigma Phi G' - alpha Phi' G].
Transport: (c r d_r - 1) r^alpha G = (c alpha - 1) r^alpha G.
All of this is verified below by an independent polar derivation (see ipm_eval.py for the numerical fields).
"""
import json, math, hashlib
from fractions import Fraction
from gmpy2 import mpq, mpz
import gmpy2

def Q(x):
    """exact rational of int / Fraction / float / str('num/den' or decimal) / mpq"""
    if isinstance(x, type(mpq(1))): return x
    if isinstance(x, bool): raise TypeError
    if isinstance(x, int): return mpq(x)
    if isinstance(x, Fraction): return mpq(x.numerator, x.denominator)
    if isinstance(x, float):
        f = Fraction(x); return mpq(f.numerator, f.denominator)
    if isinstance(x, str):
        if '/' in x:
            n, d = x.split('/'); return mpq(mpz(n), mpz(d))
        f = Fraction(x); return mpq(f.numerator, f.denominator)
    raise TypeError(type(x))

def qstr(x):
    x = Q(x); return '%s/%s' % (x.numerator, x.denominator)

def qfloat(x): return float(Fraction(int(x.numerator), int(x.denominator)))

def binom_q(p, q):
    out = mpq(1)
    for i in range(q): out = out*(p-i)/(i+1)
    return out

def legendre_monomial(n):
    """P_n(2t-1) = sum_h L[h] t^h (exact integers)."""
    return [(-1)**(n-h)*math.comb(n, h)*math.comb(n+h, h) for h in range(n+1)]

# ---------------------------------------------------------------- series dicts (harmonic -> mpq)
def sadd(d, k, v):
    if v == 0: return
    if k < 0: k, v = -k, -v        # sin(-k) = -sin(k)
    if k == 0: return              # sin 0 = 0
    nv = d.get(k, 0)+v
    if nv == 0: d.pop(k, None)
    else: d[k] = nv

def cadd(d, k, v):
    if v == 0: return
    if k < 0: k = -k               # cos(-k) = cos(k)
    nv = d.get(k, 0)+v
    if nv == 0: d.pop(k, None)
    else: d[k] = nv

def density_from_potential(C, s):
    F = {}
    for n, c in C.items():
        sadd(F, n+1, -c*(s*s-n*n)*(s-2-n)/2); sadd(F, n-1, c*(s*s-n*n)*(s-2+n)/2)
    return F

def stream_from_potential(C, s):
    P = {}
    for n, c in C.items():
        sadd(P, n+2, c*(s-n)*(s-n-2)/4); sadd(P, n-2, -c*(s+n)*(s+n-2)/4)
    return P

def dsin(S):
    """d/dtheta of a sine series -> cosine dict"""
    return {k: k*v for k, v in S.items()}

def sin_times_cos(S, Cc):
    out = {}
    for a, sa in S.items():
        for b, cb in Cc.items():
            sadd(out, a+b, sa*cb/2); sadd(out, a-b, sa*cb/2)
    return out

def series_sum(*dicts):
    out = {}
    for d in dicts:
        for k, v in d.items(): sadd(out, k, v)
    return out

def scale(d, f): return {k: v*f for k, v in d.items()} if f != 0 else {}

def quarter_norm2_over_pi(S):
    """||sum s_k sin k theta||^2_{L2(0,pi/2)} = (pi/4) sum s_k^2 for odd k (all k odd here) -> returns sum s_k^2/4"""
    return sum((v*v for v in S.values()), mpq(0))/4

def quarter_norm(S):
    return math.sqrt(math.pi*qfloat(quarter_norm2_over_pi(S))) if S else 0.0

def advect(Phi, sigma, G, alpha):
    """[sigma Phi G' - alpha Phi' G] as sine dict; Phi, G sine dicts (stream exponent sigma, density exponent alpha)."""
    return series_sum(scale(sin_times_cos(Phi, dsin(G)), sigma), scale(sin_times_cos(G, dsin(Phi)), -alpha))

# ---------------------------------------------------------------- state 131 / 88 exact reconstruction (case4 T1 checkpoints)
def canonical_index(j, m, k):
    assert 0 <= j <= 3 and 0 <= m <= 9 and m <= k <= 25
    return 215*j+26*m-m*(m-1)//2+(k-m)

LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]
HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]

def p_branch(c, j):
    gamma = 1/c; lam = 1-gamma
    return (3+gamma-j*lam)/2

def strain_values(c):
    """center strain chi_xxyy(0) of the 60 low monomials (exact in c)."""
    s = []
    for (m, k, j) in LOW:
        p = p_branch(c, j)
        if (m, k) == (0, 0): s.append(4*p*(p-1))
        elif (m, k) == (0, 1): s.append(8*(p-1))
        elif (m, k) == (0, 2): s.append(mpq(8))
        elif (m, k) == (2, 2): s.append(mpq(-24))
        else: s.append(mpq(0))
    return s

def load_case4_state(path):
    """Exact canonical coefficients (860 mpq, order I(j,m,k)) and c_l from a case4 T1 checkpoint JSON (P_hex, high_hex, frozen_Nn_hex)."""
    J = json.load(open(path))
    P = [float.fromhex(h) for h in J['P_hex']]; high = [float.fromhex(h) for h in J['high_hex']]
    NN = [Q(float.fromhex(h)) for h in J['frozen_Nn_hex']]
    assert len(P) == 60 and len(high) == 800 and len(NN) == 26
    c = Q(P[0]); s = strain_values(c)
    low = [Q(v) for v in P]
    low[0] = (1-c-sum((s[k]*low[k] for k in range(1, 60)), mpq(0)))/s[0]
    a = [mpq(0)]*860
    for v, (m, k, j) in zip(low, LOW): a[canonical_index(j, m, k)] += v
    for v, (m, n, j) in zip(high, HIGH):
        v = Q(v)
        if v:
            v *= NN[n]; vm = max(5, m)
            for h, L in enumerate(legendre_monomial(n)): a[canonical_index(j, m, vm+h)] += v*L
    ser = ('cl %d/%d\n' % (c.numerator, c.denominator)+'\n'.join('%d/%d' % (x.numerator, x.denominator) for x in a)).encode()
    sha = hashlib.sha256(ser).hexdigest()
    rec = {'cl_exact': qstr(c), 'cl': P[0], 'a000_exact': qstr(low[0]), 'a000_float': qfloat(low[0]),
           'canonical_serialization_sha256': sha, 'reported_sha256': J.get('input_exact_for_checkpoint', {}).get('canonical_serialization_sha256'),
           'label': J.get('label'), 'a0_reported': J.get('a0'), 'J_abs_mesh_reported': J.get('objectives', {}).get('J_abs_mesh')}
    # canonical term list (m, k, p, coef)
    terms = []
    for j in range(4):
        p = p_branch(c, j)
        for m in range(10):
            for k in range(m, 26):
                v = a[canonical_index(j, m, k)]
                if v: terms.append({'m': m, 'k': k, 'p': p, 'j': j, 'coef': v})
    return c, terms, rec, {'P': P, 'high': high, 'low_exact': low}

# ---------------------------------------------------------------- generic generator lists
QMAX_SERIES = 14   # far-field moments q <= QMAX_SERIES are carried for 'series' terms (legqs generators)

def legqs_moments(p, m, w, n, Qd, R0, qmax=QMAX_SERIES):
    """Far-field moments of Y = r^(2m)(1+r^2)^(p-m) ts^w us^Q P_n(2ts-1), ts = r^2/(R0^2+r^2), us = R0^2/(R0^2+r^2):
    Y = r^(2p) sum_{q'} M[q'] r^(-2q'),  M[q'] = sum_{q+l+i=q'} binom(p-m,q) T_l R0^(2l) binom(-l,i) R0^(2i),  T(u) = u^Q (1-u)^w P_n(1-2u) = sum_l T_l u^l."""
    R0 = Q(R0); R02 = R0*R0
    # T(u) coefficients: u^Q * (1-u)^w * P_n(1-2u); P_n(1-2u) = P_n(2t-1) with t = 1-u: use P_n(2t-1) = sum_h L_h t^h, t = 1-u
    L = legendre_monomial(n)
    poly_t = {h: mpq(L[h]) for h in range(n+1)}            # in t
    # convert to u: t^h = (1-u)^h
    Tu = {}
    for h, v in poly_t.items():
        for i in range(h+1):
            Tu[i] = Tu.get(i, mpq(0))+v*((-1)**i*math.comb(h, i))
    # times (1-u)^w
    Tw = {}
    for l, v in Tu.items():
        for i in range(w+1):
            Tw[l+i] = Tw.get(l+i, mpq(0))+v*((-1)**i*math.comb(w, i))
    T = {l+Qd: v for l, v in Tw.items()}                   # times u^Q
    M = [mpq(0)]*(qmax+1)
    for qp in range(qmax+1):
        tot = mpq(0)
        for l, Tl in T.items():
            if Tl == 0 or l > qp: continue
            for i in range(qp-l+1):
                q = qp-l-i
                tot += binom_q(p-m, q)*Tl*R02**l*binom_q(mpq(-l), i)*R02**i
        M[qp] = tot
    return M

def generators_to_terms(c, gens):
    """gens: list of dicts with keys m, (j or p), spec (['mono',h] | ['leg',w,n] | ['legq',w,n,Q] | ['legqs',w,n,Q,R0]), coef (mpq/str).
    Returns terms: canonical monomial terms {'m','k','p','coef'} (moment binom(p-k,q)) merged, plus 'series' terms {'m','p','kind':'series','moments':[...],'k_origin','coef'}."""
    acc = {}; series = []
    for g in gens:
        m = int(g['m']); coef = Q(g['coef'])
        p = Q(g['p']) if 'p' in g else p_branch(c, int(g['j']))
        spec = g['spec']
        if spec[0] == 'legqs':
            w, n, Qd, R0 = int(spec[1]), int(spec[2]), int(spec[3]), Q(spec[4])
            if coef != 0: series.append({'m': m, 'p': p, 'kind': 'series', 'moments': [coef*v for v in legqs_moments(p, m, w, n, Qd, R0)], 'k_origin': m+w, 'coef': coef, 'spec': list(spec)})
            continue
        if spec[0] == 'mono':
            h = int(spec[1]); key = (m, m+h, p); acc[key] = acc.get(key, mpq(0))+coef
        elif spec[0] == 'leg':
            w, n = int(spec[1]), int(spec[2])
            for h, L in enumerate(legendre_monomial(n)):
                key = (m, m+w+h, p); acc[key] = acc.get(key, mpq(0))+coef*L
        elif spec[0] == 'legq':
            w, n, Qd = int(spec[1]), int(spec[2]), int(spec[3])
            for i in range(Qd+1):
                fac = (-1)**i*math.comb(Qd, i)
                for h, L in enumerate(legendre_monomial(n)):
                    key = (m, m+w+i+h, p); acc[key] = acc.get(key, mpq(0))+coef*L*fac
        else: raise ValueError(spec)
    return [{'m': m, 'k': k, 'p': p, 'coef': v} for (m, k, p), v in acc.items() if v != 0]+series

def term_moment(t, q):
    if t.get('kind') == 'series':
        return t['moments'][q] if q < len(t['moments']) else mpq(0)
    return t['coef']*binom_q(t['p']-t['k'], q)

def potential_sectors(terms, qmax):
    """{(p, q): cos dict (harmonic 2m -> C)} for q <= qmax; also moments dict ((m,p,q) -> value)."""
    sect = {}; moments = {}
    ps = sorted({t['p'] for t in terms}, reverse=True)
    for p in ps:
        for q in range(qmax+1):
            C = {}
            for t in terms:
                if t['p'] != p: continue
                v = term_moment(t, q)
                if v: cadd(C, 2*t['m'], v)
            for n, v in C.items(): moments[(n//2, p, q)] = v
            sect[(p, q)] = C
    return sect, moments

def residual_sectors(c, terms, qmax, extra_density=None, exp_min=None):
    """Exact far-field residual sectors of F(rho) for the potential sum(terms) (r > 1 expansion).
    Returns E: dict exponent(mpq) -> sine dict, plus the density/stream sectors and the potential moments.
    extra_density: optional list of (alpha, Gdict, Phidict) pure tail sectors (no potential) to include (for formal completions).
    exp_min: if given, sectors (and advection pairs) with exponent below exp_min are skipped (exact for the retained exponents)."""
    sect, moments = potential_sectors(terms, qmax)
    dens = {}; strm = {}
    for (p, q), C in sect.items():
        s = 2*p-2*q; alpha = s-3
        dens.setdefault(alpha, {}); strm.setdefault(alpha, {})
        dens[alpha] = series_sum(dens[alpha], density_from_potential(C, s))
        strm[alpha] = series_sum(strm[alpha], stream_from_potential(C, s))
    if extra_density:
        for alpha, G, Phi in extra_density:
            dens[alpha] = series_sum(dens.get(alpha, {}), G); strm[alpha] = series_sum(strm.get(alpha, {}), Phi)
    E = {}
    for alpha, G in dens.items():
        if exp_min is not None and alpha < exp_min: continue
        E.setdefault(alpha, {}); E[alpha] = series_sum(E[alpha], scale(G, c*alpha-1))
    alphas = list(dens.keys())
    for ai in alphas:
        Phi = strm[ai]
        if not Phi: continue
        for aj in alphas:
            G = dens[aj]
            if not G: continue
            ex = ai+aj-1
            if exp_min is not None and ex < exp_min: continue
            E.setdefault(ex, {}); E[ex] = series_sum(E[ex], advect(Phi, ai+1, G, aj))
    return E, dens, strm, moments

def sector_table(E, exp_min=None):
    rows = []
    for ex in sorted(E.keys(), reverse=True):
        if exp_min is not None and ex < exp_min: continue
        S = E[ex]
        rows.append({'exponent_exact': qstr(ex), 'exponent': qfloat(ex), 'zero': not S, 'max_harmonic': max(S) if S else 0,
                     'quarter_L2': quarter_norm(S), 'n_terms': len(S)})
    return rows

# ---------------------------------------------------------------- stationary recursion
def invert_density(F, s):
    """Given odd sine dict F at density exponent s-3, find cos dict C (harmonics 0,2,4,..) with density_from_potential(C,s) = F.
    Density rule: C_n contributes -C(s^2-n^2)(s-2-n)/2 to sin(n+1) and +C(s^2-n^2)(s-2+n)/2 to sin(n-1).
    Triangular: top harmonic N = max odd k; C_{N-1} from sin N; then descend."""
    C = {}
    if not F: return C
    F = dict(F); N = max(F)
    for n in range(N-1, -1, -2):          # n even: N-1, N-3, ..., 0
        # coefficient of sin(n+1) gets -C_n (s^2-n^2)(s-2-n)/2 plus C_{n+2} (s^2-(n+2)^2)(s-2+n+2)/2 (already known)
        target = F.get(n+1, mpq(0))
        if n+2 in C: target -= C[n+2]*(s*s-(n+2)**2)*(s+n)/2
        diag = -(s*s-n*n)*(s-2-n)/2
        if n == 0:
            # n=0 term: contributes -C(s^2)(s-2)/2 to sin(1) and +C s^2 (s-2)/2 to sin(-1) = -C s^2(s-2)/2 to sin(1): total -C s^2 (s-2)
            diag = -s*s*(s-2)
        if diag == 0: raise ZeroDivisionError('resonant inversion at n=%d, s=%s' % (n, qstr(s)))
        cn = target/diag
        if cn: C[n] = cn
    # verify
    chk = series_sum(density_from_potential(C, s), scale(F, -1))
    assert not chk, 'inversion check failed: %s' % chk
    return C

def stationary_orders(c, Theta0, nmax):
    """Formal stationary tail from leading density Theta0 (sine dict at exponent gamma).
    Orders n=1..nmax: alpha_n = gamma - n lam; E_n = -n(c-1) G_n + sum_{i+j=n-1} advect(Phi_i, alpha_i+1, G_j, alpha_j) = 0.
    Returns lists G[n], Phi[n], C[n] (potential cos dict at s = alpha_n + 3)."""
    gamma = 1/c; lam = 1-gamma
    alpha = [gamma-n*lam for n in range(nmax+1)]
    G = [None]*(nmax+1); Phi = [None]*(nmax+1); C = [None]*(nmax+1)
    C[0] = invert_density(Theta0, alpha[0]+3); G[0] = dict(Theta0); Phi[0] = stream_from_potential(C[0], alpha[0]+3)
    for n in range(1, nmax+1):
        S = {}
        for i in range(n):
            j = n-1-i
            S = series_sum(S, advect(Phi[i], alpha[i]+1, G[j], alpha[j]))
        G[n] = scale(S, mpq(1)/(n*(c-1)))
        C[n] = invert_density(G[n], alpha[n]+3)
        Phi[n] = stream_from_potential(C[n], alpha[n]+3)
    return alpha, G, Phi, C

def poisson_check(G, Phi, alpha):
    """-Phi'' - (alpha+1)^2 Phi = alpha cos F - sin F' (sine dicts). Returns residual dict."""
    lhs = {k: (k*k-(alpha+1)**2)*v for k, v in Phi.items()}
    rhs = series_sum(scale(sin_times_cos(G, {1: mpq(1)}), alpha), scale(sin_times_cos({1: mpq(1)}, dsin(G)), -1))
    return series_sum(lhs, scale(rhs, -1))

def to_float_dict(d): return {int(k): qfloat(v) for k, v in sorted(d.items())}
def dump_q_dict(d): return {str(k): qstr(v) for k, v in sorted(d.items())}
