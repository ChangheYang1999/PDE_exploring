"""Versioned 860-generator potential family (SPEC v5 T1 coordinates; v9/v9.1 extended-precision evaluator): manifest, exact maps, generator block, jets.

Generators chi_{m,k,j} = r^(2k) (1+r^2)^(p_j-k) cos(2 m theta) = H_m R^(p_j-m) t^(k-m), m=0..9, k=m..25, j=0..3,
p_j = (3 + gamma - j lambda)/2, gamma = 1/cl, lambda = 1 - gamma. Canonical order I(j,m,k) = 215 j + 26 m - m(m-1)/2 + (k-m).

Internal coordinates (T1):
  low  (60):  raw monomials a_{mkj}, k <= 4 (m <= 4); internal order L(j,m,k) = 15 j + 5 m - m(m-1)/2 + (k-m); L = 0 is a_{000}.
  high (800): E_{mnj} = H_m R^(p_j-m) t^max(5-m,0) N_n P_n(2t-1), m=0..9, n=0..25-max(5,m), j=0..3; order j, m, n.
  N_n = host-frozen binary64 constants of the old source expression (spectral_basis._radial, alpha=beta=0).
  a_{m, v_m+h, j} = sum_n c_{mnj} N_n (-1)^(n-h) C(n,h) C(n+h,h), v_m = max(5, m).
Old 186 -> new: old core (m,s), s<=2: a_{m,m+h,0} += b (-1)^h C(s,h); (3,2) h=2 term is c_{3,0,0} += b (N_0 = 1);
s>=3: a_{m,m,s-2} += b; old Global (m,n) -> c_{m,n,0} = g (one to one).
Numerical imports of the frozen closure require the resource supervisor (IPM_RESOURCE_SESSION).
"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import math
import os
import sys
from decimal import Decimal, localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent/'research'
for _p in (str(RESEARCH), str(RESEARCH/'base')):
    if _p not in sys.path: sys.path.insert(0, _p)
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('860-basis numerical work requires the resource supervisor')
import numpy as np
from scipy.special import gammaln
from absolute_fields import _harmonics, _assemble                    # frozen, validated helpers (harmonics, field assembly)

VERSION = 'basis860_v6_T1_longdouble_all860_exact_exponent_differences_centered_q_stableL_origin48_v99'
R_SWITCH = 1.0          # SPEC v9.2: centered-q direct form for 0.02 <= r < 1, stable linear transport for r >= 1 (R_f); the Jacobian columns use the same switch (recorded choice; v9.2 allows r_s = 2 for columns)
REPLAY_REFERENCE_FILE = ((_artifact_root + "/outputs") + '/campaign860/seed/seed_860_replay_v3.npz')   # SPEC v9: extended-precision R_f replay reference (Linux host)
ORIGIN_ORDER_PRODUCTION = 48      # SPEC v9.3: order 48 (potential order 52), certified uniformly on c_l in [51/50, 10]
KEYS = ('f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio')
ORDERS = {'f': 2., 'fx': 2.5, 'fy': 2.5, 'psi': 1., 'psix': 1.5, 'psiy': 1.5, 'ratio': 2.}
SIGMA_NAME = (0.0, 'delta', '2delta', '3delta')

# ---------------- canonical manifest ----------------
def canonical_index(j, m, k):
    if not (0 <= j <= 3 and 0 <= m <= 9 and m <= k <= 25): raise ValueError('triple outside the 860 family')
    return 215*j + 26*m - m*(m-1)//2 + (k-m)

CANONICAL = [(j, m, k) for j in range(4) for m in range(10) for k in range(m, 26)]
assert len(CANONICAL) == 860 and all(canonical_index(*t) == i for i, t in enumerate(CANONICAL))

# ---------------- internal coordinates ----------------
LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]                 # 60 raw monomials, LOW[0] = (0,0,0)
HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]       # 800 Legendre functions
assert len(LOW) == 60 and len(HIGH) == 800
LOW_INDEX = {t: i for i, t in enumerate(LOW)}
HIGH_INDEX = {t: i for i, t in enumerate(HIGH)}
NLOW, NHIGH, NRAW, NFEASIBLE_CLAIMED = 60, 800, 860, 855


def frozen_normalizers(nmax=25):
    """N_n exactly as the frozen spectral_basis._radial computes them (alpha=beta=0): binary64 on this host."""
    out = []
    for n in range(nmax+1):
        alpha = 0.; b = 0.
        lognorm = (gammaln(alpha+1)+gammaln(b+1)-gammaln(alpha+b+2)) if n == 0 else (gammaln(n+alpha+1)+gammaln(n+b+1)-math.log(2*n+alpha+b+1)-gammaln(n+1)-gammaln(n+alpha+b+1))
        out.append(math.exp(-.5*lognorm))
    return out

NN = frozen_normalizers()                                   # floats
NN_DECIMAL = [Decimal(v) for v in NN]                       # exact rational values of the binary64 constants


def high_modes():
    """Mode dictionaries for the frozen spectral_basis.evaluate_modes; j=0 dictionaries are byte-identical to the old Globals."""
    return [{'family': 'global', 'm': m, 'n': n, 'sigma': SIGMA_NAME[j]} for (m, n, j) in HIGH]


def pdiff(cl, j, s):
    """Exact-form exponent difference p_j - s = ((3 - j - 2 s) cl + (j + 1)) / (2 cl) for integer or half-integer s (SPEC v9.1):
    the numerator is an exact zero at an integer exponent (c_l = 2, j = 3, s = 1; c_l = 3, j = 2, s = 1) and keeps full relative
    accuracy next to it. Works for float, longdouble, complex or Decimal cl."""
    twos = 2*s
    if twos != int(twos): raise ValueError('s must be an integer or half-integer')
    twos = int(twos)
    return ((3-j-twos)*cl+(j+1))/(2*cl)

def dp_cl(cl, j):
    """dp_j/dcl = -(j+1)/(2 cl^2)."""
    return -(j+1)/(2*cl*cl)

def p_exponents(cl):
    """p_j and dp_j/dcl for float, longdouble, complex or Decimal cl (p_j = pdiff(cl, j, 0))."""
    return [pdiff(cl, j, 0) for j in range(4)], [dp_cl(cl, j) for j in range(4)]


# ---------------- old (186) -> internal (T1) ----------------
OLD_CORE_ORDER = [(m, k) for m in range(4) for k in range(5)] + [(m, 5) for m in range(4)]

def old_core_to_internal(m, s):
    """Old core (m, s) -> list of (kind, index, integer coefficient)."""
    if s >= 3: return [('low', LOW_INDEX[(m, m, s-2)], 1)]
    out = []
    for h in range(s+1):
        k = m+h; coef = (-1)**h*math.comb(s, h)
        if k <= 4: out.append(('low', LOW_INDEX[(m, k, 0)], coef))
        else:
            if (m, k) != (3, 5): raise ValueError('unexpected high-block image of an old core generator')
            out.append(('high', HIGH_INDEX[(3, 0, 0)], coef))      # chi_{3,5,0} = E_{3,0,0} since N_0 = 1 exactly
    return out

def old_mode_to_internal(mode):
    if mode['family'] != 'global' or float(mode.get('sigma', 0.)) != 0. or mode.get('alpha', 0.) or mode.get('beta', 0.) or mode.get('scale', 1.) != 1. or not mode.get('normalize', True):
        raise ValueError('Old mode outside the embedded Global family: '+str(mode))
    return HIGH_INDEX[(int(mode['m']), int(mode['n']), 0)]

def embed_old(coefficients24, extra162, modes162):
    """Exact map B: old analytic coefficients [c0..c23] (c0 analytic) and Global coefficients -> (low60, high800) floats."""
    low = np.zeros(NLOW); high = np.zeros(NHIGH)
    if len(coefficients24) != 24 or len(extra162) != len(modes162): raise ValueError('old dimensions')
    for value, (m, s) in zip(coefficients24, OLD_CORE_ORDER):
        for kind, index, f in old_core_to_internal(m, s): (low if kind == 'low' else high)[index] += f*float(value)
    for value, mode in zip(extra162, modes162): high[old_mode_to_internal(mode)] += float(value)
    return low, high

def embed_old_decimal(coefficient_strings24, extra162, modes162, digits=100):
    """Same map in Decimal from the 90-digit analytic coefficient strings (for the a_000 identity and the T1.1b check)."""
    with localcontext() as ctx:
        ctx.prec = digits
        low = [Decimal(0)]*NLOW; high = [Decimal(0)]*NHIGH
        for value, (m, s) in zip(coefficient_strings24, OLD_CORE_ORDER):
            v = Decimal(value)
            for kind, index, f in old_core_to_internal(m, s): (low if kind == 'low' else high)[index] += f*v
        for value, mode in zip(extra162, modes162): high[old_mode_to_internal(mode)] += Decimal.from_float(float(value))
        return low, high


# ---------------- internal <-> canonical (exact, frozen N_n) ----------------
def legendre_monomial(n):
    """P_n(2t-1) = sum_h L[h] t^h, exact integers."""
    return [(-1)**(n-h)*math.comb(n, h)*math.comb(n+h, h) for h in range(n+1)]

GUARD_DIGITS = 40   # the Legendre<->monomial block transforms have condition about 1e22; guard digits keep results exact to `digits`

def internal_to_canonical_exact(low, high, digits=60, round_output=True):
    """860 Decimal monomial coefficients in canonical order from internal (low, high); exact given the binary64 N_n.
    Computed with `digits`+GUARD_DIGITS working precision, results rounded to `digits` significant digits."""
    with localcontext() as ctx:
        ctx.prec = digits+GUARD_DIGITS
        a = [Decimal(0)]*NRAW
        for value, (m, k, j) in zip(low, LOW):
            v = value if isinstance(value, Decimal) else Decimal.from_float(float(value))
            a[canonical_index(j, m, k)] += v
        for value, (m, n, j) in zip(high, HIGH):
            v = value if isinstance(value, Decimal) else Decimal.from_float(float(value))
            if v:
                v *= NN_DECIMAL[n]; vm = max(5, m)
                for h, L in enumerate(legendre_monomial(n)): a[canonical_index(j, m, vm+h)] += v*L
        if not round_output: return a
        ctx.prec = digits
        return [+v for v in a]

def canonical_to_internal_exact(a, digits=60):
    """Inverse by block back substitution (upper triangular in (h, n) per (m, j)); `digits`+GUARD_DIGITS working precision."""
    with localcontext() as ctx:
        ctx.prec = digits+GUARD_DIGITS
        a = [v if isinstance(v, Decimal) else Decimal.from_float(float(v)) for v in a]
        low = [Decimal(0)]*NLOW; high = [Decimal(0)]*NHIGH
        for j in range(4):
            for m in range(10):
                if m <= 4:
                    for k in range(m, 5): low[LOW_INDEX[(m, k, j)]] = a[canonical_index(j, m, k)]
                vm = max(5, m); N = 26-vm; gt = [Decimal(0)]*N
                for n in range(N-1, -1, -1):
                    total = a[canonical_index(j, m, vm+n)]
                    for n2 in range(n+1, N): total -= gt[n2]*legendre_monomial(n2)[n]
                    gt[n] = total/legendre_monomial(n)[n]
                for n in range(N): high[HIGH_INDEX[(m, n, j)]] = gt[n]/NN_DECIMAL[n]
        ctx.prec = digits
        return [+v for v in low], [+v for v in high]

def conversion_matrix():
    """Float T (860 x 860) with a = T @ [low; high] (diagnostic; the exact maps above are authoritative)."""
    T = np.zeros((NRAW, NRAW))
    for col, (m, k, j) in enumerate(LOW): T[canonical_index(j, m, k), col] = 1.
    for col, (m, n, j) in enumerate(HIGH):
        vm = max(5, m)
        for h, L in enumerate(legendre_monomial(n)): T[canonical_index(j, m, vm+h), NLOW+col] += NN[n]*L
    return T


# ---------------- origin data: strains and Taylor jets of the low block ----------------
def strain_values(cl):
    """Center strain h_i = chi_xxyy(0) and d/dcl for the 60 low monomials (SPEC section 7); any scalar type."""
    p, dp = p_exponents(cl); zero = 0*cl
    s = []; ds = []
    for (m, k, j) in LOW:
        if (m, k) == (0, 0): s.append(4*p[j]*pdiff(cl, j, 1)); ds.append(4*(2*p[j]-1)*dp[j])
        elif (m, k) == (0, 1): s.append(8*pdiff(cl, j, 1)); ds.append(8*dp[j])
        elif (m, k) == (0, 2): s.append(8+zero); ds.append(zero)
        elif (m, k) == (2, 2): s.append(-24+zero); ds.append(zero)
        else: s.append(zero); ds.append(zero)
    return s, ds

def center_data(cl):
    s, ds = strain_values(float(cl))
    return np.asarray(s, float), np.asarray(ds, float)

JET_NAMES = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'u', 'v', 'w', 'z', 'k']

def jets(cl, decimal=False):
    """12 Taylor jets per low generator (60 lists): f jets (1,x^2,y^2,x^4,x^2y^2,y^4) then psi/(xy) jets, as taylor_jet.series.
    chi_{mkj} = H_m q^(k-m) sum_l C(p_j-k, l) q^l, truncated at potential degree 8."""
    zero = Decimal(0) if decimal else 0.*cl
    one = Decimal(1) if decimal else 1.
    L = Decimal(cl) if decimal and not isinstance(cl, Decimal) else cl
    columns = []
    for (m, k, j) in LOW:
        A = {}
        for l in range(m+1):
            angular = (-1)**l*math.comb(2*m, 2*l); choose = one
            for n in range(0, 5):
                if n: choose = choose*pdiff(L, j, k+n-1)/n          # C(p_j - k, n) with exact factors p_j - k - n + 1 (SPEC v9.1)
                N = n+k-m                                       # power of q multiplying H_m
                if 2*m+2*N > 8: break
                for qq in range(N+1):
                    key = (2*m-2*l+2*qq, 2*l+2*(N-qq)); A[key] = A.get(key, zero)+angular*choose*math.comb(N, qq)
        F = {}; H = {}
        for (ix, iy), value in A.items():
            if ix >= 2 and iy >= 2:
                key = (ix-2, iy-2); F[key] = F.get(key, zero)-ix*(ix-1)*iy*value; H[key] = H.get(key, zero)+ix*iy*value
            if iy >= 4:
                key = (ix, iy-4); F[key] = F.get(key, zero)-iy*(iy-1)*(iy-2)*value
        columns.append([F.get(key, zero) for key in [(0, 0), (2, 0), (0, 2), (4, 0), (2, 2), (0, 4)]]
                       + [H.get(key, zero) for key in [(0, 0), (2, 0), (0, 2), (4, 0), (2, 2), (0, 4)]])
    return columns

def jet_matrix(cl): return np.array(jets(cl)).T      # 12 x 60


def decimal_center(cl, low_coefficients, precision=90):
    """Analytic elimination a_000 = (1 - cl - sum_{i>=1} s_i a_i)/s_0 at Decimal precision from exact binary inputs."""
    with localcontext() as ctx:
        ctx.prec = precision
        L = Decimal.from_float(float(cl)); s, ds = strain_values(L)
        c = [Decimal.from_float(float(v)) for v in low_coefficients]
        original = c[0]
        c[0] = (1-L-sum((s[k]*c[k] for k in range(1, NLOW)), Decimal(0)))/s[0]
        dc0 = (-1-sum((ds[k]*c[k] for k in range(NLOW)), Decimal(0)))/s[0]
        return {'coefficients_decimal': [str(v) for v in c], 'strain_decimal': [str(v) for v in s],
                'strain_cl_decimal': [str(v) for v in ds], 'c0_cl_decimal': str(dc0),
                'original_c0': str(original), 'analytic_c0': str(c[0]), 'precision': precision}


def prepare(cl, low_free59, high800):
    """Prepared state. Raw chart vector P = [cl, a_1..a_59]; a_000 analytic; returns the chain dc0/dP."""
    P = np.r_[float(cl), np.asarray(low_free59, float)]
    if P.shape != (NLOW,) or not np.all(np.isfinite(P)) or P[0] <= 1: raise ValueError('Expected finite cl>1 and 59 low coefficients')
    g = np.asarray(high800, float)
    if g.shape != (NHIGH,) or not np.all(np.isfinite(g)): raise ValueError('Expected 800 finite high coefficients')
    dec = decimal_center(P[0], np.r_[0., P[1:]])
    c = np.asarray([float(v) for v in dec['coefficients_decimal']])
    strain = center_data(P[0])[0]
    dc0 = np.zeros(NLOW); dc0[0] = float(dec['c0_cl_decimal']); dc0[1:] = -strain[1:]/strain[0]
    c_ld = np.asarray(P, LD); c_ld[0] = LD(format(Decimal(dec['coefficients_decimal'][0]), '.30e'))   # analytic a_000 carried to the 64-bit significand (SPEC v9)
    return {'P': P, 'cl': P[0], 'c': c, 'g': g, 'c0_derivative': dc0, 'center': dec, 'modes': high_modes(),
            'c_ld': c_ld, 'coeff_ld': np.r_[c_ld, np.asarray(g, LD)], 'version': VERSION, '_taylor_cache': {}}


# ---------------- extended-precision generator evaluator for all 860 generators (SPEC v9 / v9.1) ----------------
LD = np.longdouble
STRAINED_LOW = {(0, 0), (0, 1), (0, 2), (2, 2)}          # (m, k) with nonzero center strain; 16 generators over the four branches
S_ORDERS = {'f': 2, 'fx': 2.5, 'fy': 2.5, 'psi': 1, 'psix': 1.5, 'psiy': 1.5, 'ratio': 2}

def legendre_t_jets(t, nmax, order=5):
    """d^h/dt^h P_n(2t-1) for n=0..nmax, h=0..order, from the h-times differentiated Bonnet recurrence (any float dtype)."""
    z = 2*t-1; jets = [np.zeros((order+1,)+t.shape, dtype=t.dtype)]; jets[0][0] = 1
    if nmax == 0: return jets
    jets.append(np.zeros_like(jets[0])); jets[1][0] = z; jets[1][1] = 2
    for n in range(1, nmax):
        row = np.zeros_like(jets[0])
        for h in range(order+1):
            term = z*jets[n][h]+(2*h*jets[n][h-1] if h else 0)
            row[h] = ((2*n+1)*term-n*jets[n-1][h])/(n+1)
        jets.append(row)
    return jets

def _icomb(n, k):
    """Exact integer binomial coefficient (Python integers; no floating-point library call on the R_f path)."""
    if k < 0 or k > n: return 0
    r = 1
    for i in range(1, k+1): r = r*(n-k+i)//i
    return r

def _ifalling(n, h):
    """Exact integer n!/(n-h)! for 0 <= h <= n."""
    r = 1
    for i in range(h): r *= n-i
    return r

def _power_jets(t, w, order=5):
    return [_ifalling(w, h)*t**(w-h) if h <= w else np.zeros_like(t) for h in range(order+1)]

def radial_jets(cl, j, m, u, T, dT=None, order=4):
    """g(q) = R^beta T(t), beta = p_j - m:  d^a g/dq^a = R^(beta-a) F_a with
         F_a = sum_{l=0}^{a} C(a,l) (beta-l)_(a-l) u^l T^(l)(t)          ((x)_n = falling factorial, u = 1/R, t = 1-u),
    every factor beta-l-i formed as pdiff(cl, j, m+l+i) (exact zero at integer exponents, SPEC v9.1).  Returns F_a and
    dF_a/dcl (exponent chain with dbeta = dp_j/dcl plus the fixed-exponent derivative dT of the t-jets, if given)."""
    dbeta = dp_cl(cl, j); e = [pdiff(cl, j, m+s) for s in range(order+1)]
    upow = [1]; 
    for l in range(order): upow.append(upow[-1]*u)
    F = []; dF = []
    for a in range(order+1):
        acc = 0; dacc = 0
        for l in range(a+1):
            prod = 1; dprod = 0
            for i in range(a-l): dprod = dprod*e[l+i]+prod; prod = prod*e[l+i]
            c = _icomb(a, l); w = c*prod*upow[l]
            acc = acc+w*T[l]; dacc = dacc+c*dprod*dbeta*upow[l]*T[l]
            if dT is not None: dacc = dacc+w*dT[l]
        F.append(acc); dF.append(dacc)
    return F, dF

def centered_ratio(m, k, cl, j, xn2, yn2, t, u, S, dtype):
    """ratio_i - s_i for the strained low generators chi = H_m R^(p_j-m) t^(k-m), s_i = ratio_i(0), as
    s_i expm1(a S) + exp(a S) B_i with a = p_j - 2, S = log R, and B_i a sum of positive-degree terms (own derivation,
    BASIS_860_IMPLEMENTATION.md section 11; equals the verifier's forms).  xn2 = x^2/R, yn2 = y^2/R."""
    p = pdiff(cl, j, 0); p1 = pdiff(cl, j, 1); p2 = pdiff(cl, j, 2); pp1 = pdiff(cl, j, -1); a = p2
    if (m, k) == (0, 0): s = 4*p*p1; Bv = 8*xn2*p*p1*p2
    elif (m, k) == (0, 1): s = 8*p1; Bv = 4*p1*p2*t+8*xn2*p1*p2*(3*u+p*t)
    elif (m, k) == (0, 2): s = dtype(8); Bv = 4*(4*p2*t*u+p2*pp1*t*t)+8*xn2*p2*(6*u*u+6*p1*t*u+p*p1*t*t)
    elif (m, k) == (2, 2):
        s = dtype(-24); b = p2; Hn = xn2*xn2-6*xn2*yn2+yn2*yn2
        Bv = b*(-96*xn2-16*yn2)+b*(b-1)*(-12*xn2*xn2-104*xn2*yn2+4*yn2*yn2)+b*(b-1)*(b-2)*8*xn2*Hn
    else: raise ValueError('not a strained generator')
    return s*np.expm1(a*S)+np.exp(a*S)*Bv

def generator_block(cl, x, y, cl_derivative=False, remainder=False, dtype=LD):
    """All 860 generator fields at points, in extended arithmetic (default longdouble; inputs cast exactly), returned in that dtype:
    keys f, fx, fy, psi, psix, psiy, ratio (N x 860, low columns first); 'qcore' (N x 60): the low-block ratio with the center value
    subtracted (expm1 forms for the 16 strained generators, plain ratio for the others), so that q = qcore @ c + ratio[:, 60:] @ g;
    with remainder: 'frem' (N x 860), the f-field of (k - p_j) u chi (low) and of H_m R^(p_j-m-1)[t T' + (m - p_j) T] (high), so that
    the stable linear transport is sum_i a_i [-j_i (cl-1) f_i + 2 cl frem_i];  with cl_derivative: 'd_<key>' and 'd_frem' at fixed
    coefficients.  Radial derivatives by radial_jets (exact exponent differences), harmonics/assembly by the frozen polynomial
    helpers _harmonics/_assemble (dtype generic).  Low T = t^(k-m); high T = N_n t^w P_n(2t-1), w = max(5-m, 0)."""
    x = np.asarray(x, dtype).ravel(); y = np.asarray(y, dtype).ravel(); n_pts = len(x); cl = dtype(cl)
    q = x*x+y*y; R = 1+q; u = 1/R; t = q*u; S = np.log1p(q); root = np.sqrt(R); xn = x/root; yn = y/root; xn2 = xn*xn; yn2 = yn*yn
    harmonics = {m: _harmonics(xn, yn, t, m) for m in range(10)}
    out = {key: np.empty((n_pts, NRAW), dtype) for key in KEYS}; out['qcore'] = np.empty((n_pts, NLOW), dtype)
    if cl_derivative:
        for key in KEYS: out['d_'+key] = np.empty((n_pts, NRAW), dtype)
    if remainder:
        out['frem'] = np.empty((n_pts, NRAW), dtype)
        if cl_derivative: out['d_frem'] = np.empty((n_pts, NRAW), dtype)
    factors = {}
    def factor(j, order):
        key = (j, order)
        if key not in factors: factors[key] = np.exp(pdiff(cl, j, order)*S)
        return factors[key]
    dp = [dp_cl(cl, j) for j in range(4)]
    def put(col, m, j, T, dT, Tq, dTq):
        F, dF = radial_jets(cl, j, m, u, T, dT)
        values = _assemble(*harmonics[m], xn, yn, t, F, 2*m); ders = _assemble(*harmonics[m], xn, yn, t, dF, 2*m) if cl_derivative else None
        for key in KEYS:
            fac = factor(j, S_ORDERS[key]); out[key][:, col] = fac*values[key]
            if cl_derivative: out['d_'+key][:, col] = fac*(ders[key]+dp[j]*S*values[key])
        if remainder:
            FQ, dFQ = radial_jets(cl, j, m+1, u, Tq, dTq); vq = _assemble(*harmonics[m], xn, yn, t, FQ, 2*m); fac = factor(j, 1+S_ORDERS['f'])
            out['frem'][:, col] = fac*vq['f']
            if cl_derivative: dq = _assemble(*harmonics[m], xn, yn, t, dFQ, 2*m); out['d_frem'][:, col] = fac*(dq['f']+dp[j]*S*vq['f'])
    tp = {w: _power_jets(t, w, 5) for w in range(6)}
    for col, (m, k, j) in enumerate(LOW):
        T = tp[k-m]; ck = -pdiff(cl, j, k)                      # (k - p_j)
        put(col, m, j, T, None, [ck*v for v in T], [-dp[j]*v for v in T])
        out['qcore'][:, col] = centered_ratio(m, k, cl, j, xn2, yn2, t, u, S, dtype) if (m, k) in STRAINED_LOW else out['ratio'][:, col]
    P = legendre_t_jets(t, 25, 5)
    for col, (m, n, j) in enumerate(HIGH):
        w = max(5-m, 0); N = dtype(NN[n])
        T = [N*sum(_icomb(h, i)*tp[w][i]*P[n][h-i] for i in range(h+1)) for h in range(6)]      # t-jets of T = t^w N_n P_n(2t-1), orders 0..5 (exact integer Leibniz weights)
        cm = -pdiff(cl, j, m)                                                                       # (m - p_j)
        Q = [t*T[h+1]+h*T[h]+cm*T[h] for h in range(5)]; dQ = [-dp[j]*T[h] for h in range(5)]
        put(NLOW+col, m, j, T, None, Q, dQ)
    return out

def low_matrices(cl, x, y, cl_derivative=False, exp=None):
    """(N x 60) float64 field matrices of the raw monomials (rounded once from the longdouble block); `exp` is ignored (kept for callers)."""
    blk = generator_block(cl, x, y, cl_derivative, False)
    mats = {key: blk[key][:, :NLOW].astype(float) for key in KEYS}
    if not cl_derivative: return mats
    return mats, {key: blk['d_'+key][:, :NLOW].astype(float) for key in KEYS}

def high_matrices(cl, x, y, cl_derivative=False, remainder=False, dtype=LD):
    """(N x 800) float64 field matrices of the T1 high generators (rounded once from the extended block); optional cl derivatives and remainders."""
    blk = generator_block(cl, x, y, cl_derivative, remainder, dtype)
    mats = {key: blk[key][:, NLOW:].astype(float) for key in KEYS}; out = [mats]
    if cl_derivative: out.append({key: blk['d_'+key][:, NLOW:].astype(float) for key in KEYS})
    if remainder: out.append(blk['frem'][:, NLOW:].astype(float))
    if remainder and cl_derivative: out.append(blk['d_frem'][:, NLOW:].astype(float))
    return tuple(out) if len(out) > 1 else mats

def low_remainder_f(cl, x, y, cl_derivative=False, exp=None, dtype=LD):
    blk = generator_block(cl, x, y, cl_derivative, True, dtype)
    return (blk['frem'][:, :NLOW].astype(float), blk['d_frem'][:, :NLOW].astype(float)) if cl_derivative else blk['frem'][:, :NLOW].astype(float)

JCOL = np.array([j for (m, k, j) in LOW]+[j for (m, n, j) in HIGH], dtype=float)   # branch index per raw generator column
JCOL_LD = JCOL.astype(LD)

def rf_path_statement():
    """SPEC v9.3 clause (a): every function on the R_f path with the arithmetic it uses; no Python math function and no float() conversion
    appears on it (the only math.* calls in basis860 are exact integer combinatorics outside the path and the frozen N_n constants, which are inputs)."""
    return {'inputs_promoted_exactly': ['coordinates x, y (binary64 -> longdouble)', 'c_l (binary64 -> longdouble)', 'free coefficients P[1:], high g (binary64 -> longdouble)', 'frozen N_n (binary64 -> longdouble)',
                                        'a_000: analytic Decimal elimination (basis860.decimal_center, 90 digits) converted to longdouble through a 31-significant-digit decimal string (prepare: c_ld); no binary64 rounding of a_000 on the path'],
            'functions': [
                {'function': 'basis860.pdiff / dp_cl', 'arithmetic': 'longdouble scalar: ((3-j-2s) cl + (j+1)) / (2 cl); -(j+1)/(2 cl^2)'},
                {'function': 'basis860.generator_block', 'arithmetic': 'longdouble arrays: q = x^2+y^2, R = 1+q, u = 1/R, t = q u, S = log1p(q) (log1pl), root = sqrt(R) (sqrtl), xn = x/root, yn = y/root; factors exp(pdiff * S) (expl)'},
                {'function': 'basis860.legendre_t_jets, _power_jets', 'arithmetic': 'longdouble arrays with exact integer weights (_ifalling, _icomb; Python integers)'},
                {'function': 'basis860.radial_jets', 'arithmetic': 'longdouble: falling-factorial products of exact pdiff factors, powers of u, exact integer binomials; product rule for the cl derivative'},
                {'function': 'spectral_basis._harmonics (frozen, dtype generic)', 'arithmetic': 'longdouble / clongdouble polynomial recurrences in xn, yn, t with Python integer coefficients'},
                {'function': 'absolute_fields._assemble (frozen, dtype generic)', 'arithmetic': 'longdouble: integer-weighted combinations of the radial jets F_a and the harmonic derivatives'},
                {'function': 'basis860.centered_ratio', 'arithmetic': 'longdouble: s_i expm1(a S) (expm1l) + exp(a S) B_i with exact pdiff factors'},
                {'function': 'model860.Model860._ensure_basis / _assemble_residual', 'arithmetic': 'longdouble cache (f, f_x, f_y, psi_x, psi_y, ratio, qcore, frem); longdouble matrix-vector products (numpy longdouble loops, no BLAS); longdouble transport products; one astype(float) of R_f'},
                {'function': 'fields860.fields_direct (dtype=LD) / residual', 'arithmetic': 'same operations per point block (stateless provider); one astype(float) of R_f'},
                {'function': 'integrate860.Integrator860.stateless / _panel', 'arithmetic': 'fields860.residual (fork pool residual_parallel, identical per-point code); root weights multiply the binary64 R_f after the single rounding'},
                {'function': 'origin860.residual_series (Decimal, 90 digits) + evaluate_series_ld', 'arithmetic': 'Decimal Taylor coefficients (exact a_000) converted to longdouble through 31-digit strings; longdouble monomial evaluation, highest degree first'}],
            'binary64_only_after_the_single_rounding': ['the weighted residual r_i = root_i R_f(X_i)', 'Jacobian columns (clause (c))', 'field multipliers of the Jacobian'],
            'field_cancellation_methods': {k: v for k, v in FIELD_METHODS.items()}}

FIELD_METHODS = {
    'common': 'implemented: every field VALUE of a generator H_m R^beta T(t) is an integer-weighted combination (frozen _assemble) of the radial jets F_a = sum_l C(a,l) (beta-l)_(a-l) u^l T^(l) (radial_jets) and harmonic-polynomial derivatives; the exact zero factors (beta-l-i = pdiff(cl, j, m+l+i)) sit inside every F_a term, so a field value whose leading radial parts vanish at an integer exponent is a sum of terms that are each exactly zero, never a difference of separately rounded nonzero terms. This statement is about the values (R_f path, clause (a)); the c_l derivatives are described under cl_derivatives and cl_derivative_cancellation',
    'cl_derivative_cancellation': 'implemented: the c_l derivatives dF_a are the product-rule derivatives of the exact falling-factorial products (no exact zero factor survives differentiation) and enter the same frozen _assemble brackets (2m+a) dF_a + t dF_(a+1) as two separately rounded terms. Double-zero intermediate (SPEC v9.5 structure): for the m = 0 shifted remainder potentials u chi at p_j = 1 (low (0,0,j) at c_l = 2, j = 3, and c_l = 3, j = 2; and the m = 0 k >= 1 and high m = 0 remainders of that branch) the c_l derivative of frem is formed as dbeta T [(1) + t (2 beta - 1)] at beta = 0, whose exact value for low (0,0,j) is 8 (j+1) / (c_l^2 R^3); it enters only the stable linear transport for r >= 1 and only the binary64 Jacobian c_l column (clause (c)); R_f never uses d_frem. No error estimate is stated here; the gates T2.6x, T2.6b, T2.6c (complete columns), T2.7H and T2.7H-X/X2 decide',
    'f': 'implemented: f = -D(0) d0 - 2 h d1 with d0 = 4((2m+1) F_1 + t F_2), d1 = 4((2m+2) F_2 + t F_3) (frozen _assemble), the brackets being sums of two separately rounded products of the falling-factorial jets F_a (no factored combination, equation (1) of c4-ver PROOF.factored-laplacian.md is not implemented)',
    'fx': 'fx = -D(1) d0 - 2 xn D(0) d1 - 2 hx d1 - 4 xn h d2, d2 = 4((2m+3) F_3 + t F_4); same brackets',
    'fy': 'fy = -Dy d0 - 4 hy d1 - 4 yn h d2; same brackets',
    'psi': 'psi = hxy F_0 + (2 yn hx + 2 xn hy) F_1 + 4 xn yn h F_2',
    'psix': 'psix = H_xxy F_0 + (4 xn hxy + 2 hy + 2 yn hxx) F_1 + (4 xn^2 hy + 8 xn yn hx + 4 yn h) F_2 + 8 xn^2 yn h F_3',
    'psiy': 'psiy = H_xyy F_0 + (4 yn hxy + 2 hx + 2 xn hyy) F_1 + (4 yn^2 hx + 8 xn yn hy + 4 xn h) F_2 + 8 xn yn^2 h F_3',
    'ratio': 'ratio = D(2) F_0 + (4 xn D(1) + 2 D(0) + 2 hxx) F_1 + (4 xn^2 D(0) + 8 xn hx + 4 h) F_2 + 8 xn^2 h F_3 (D(a) = d_x^a (d_y H_m / y), polynomial recurrences); inside r_s the 16 strained low generators use centered_ratio instead',
    'cl_derivatives': 'd/dcl of each field = exp(pdiff S) [dV + dp_j S V] with dV assembled from dF_a: dF_a = sum_l C(a,l) [d/dbeta (beta-l)_(a-l)] dp_j u^l T^(l) (+ the same weights times dT^(l) where T depends on cl): the derivative of a product of exact linear factors by the product rule (no division by beta - l); dp_j = -(j+1)/(2 cl^2); the stable remainder uses dQ = -dp_j T (d/dcl of the (m - p_j) or (k - p_j) coefficient)',
    'structural_zeros': 'at c_l = 2 (p_3 = 1) the low generators (0,0,3), (0,1,3), (1,1,3) and at c_l = 3 (p_2 = 1) the generators (0,0,2), (0,1,2), (1,1,2) have F_a = 0 exactly for the orders that enter their fields, so every field is exactly 0.0; their cl derivatives are nonzero and come from dF_a'}

def extended_arithmetic_statement():
    fi = np.finfo(LD)
    return {'dtype': str(np.dtype(LD)), 'itemsize': int(np.dtype(LD).itemsize), 'nmant': int(fi.nmant), 'significand_bits': int(fi.nmant)+1, 'eps': float(fi.eps), 'unit_roundoff': float(fi.eps)/2,
            'platform_dependency': 'x86-64 80-bit extended precision (64-bit significand) through glibc expl/logl/log1pl/expm1l/sqrtl; another longdouble format changes the bits and requires requalification (replay is defined on this host)',
            'functions_using_longdouble': ['basis860.generator_block (all 860 generator fields, cl derivatives, stable remainders, centered low ratio)', 'basis860.radial_jets, legendre_t_jets, _power_jets, centered_ratio',
                                           'model860.Model860 cache (longdouble field matrices) and residual assembly; origin series evaluated by origin860.evaluate_series_ld', 'fields860.fields_direct / residual (stateless provider) field sums, q and R_f assembly',
                                           'integrate860 (validation residual and independent integral through fields860.residual)'],
            'rounded_once_to_binary64': ['R_f (production, stateless, integrator)', 'field values used as Jacobian multipliers', 'generator values used for the binary64 Jacobian columns'],
            'thread_behavior': 'longdouble operations do not use BLAS; point blocks are evaluated independently (ThreadPoolExecutor in Model860._ensure_basis when threads > 1; fork process pool in fields860.residual_parallel); outputs go to disjoint slices, so results are bitwise independent of the thread/process count'}

def manifest():
    return {'version': VERSION, 'generator_count': NRAW, 'canonical_order': 'I(j,m,k)=215j+26m-m(m-1)/2+(k-m), j outer, m, then k',
            'canonical_triples_jmk': CANONICAL, 'internal_low_triples_mkj': LOW, 'internal_high_triples_mnj': HIGH,
            'internal_high_modes': high_modes(), 'frozen_Nn_hex': [float(v).hex() for v in NN], 'frozen_Nn_float': NN,
            'feasible_variables_claimed': NFEASIBLE_CLAIMED, 'eliminated_center_coefficient': 'internal low index 0 = a_{000} = R^{p_0}; analytic Decimal value carried to the 64-bit significand in the extended residual (prepare: c_ld)',
            'formula': 'chi_{m,k,j}=r^{2k}(1+r^2)^{p_j-k}cos(2m theta); p_j=(3+1/cl-j(1-1/cl))/2',
            'exponent_differences': 'p_j - s = ((3 - j - 2 s) cl + (j + 1)) / (2 cl) (basis860.pdiff), exact zero at integer exponents (SPEC v9.1)',
            'radial_derivatives': 'd^a/dq^a [R^beta T(t)] = R^(beta-a) sum_l C(a,l) (beta-l)_(a-l) u^l T^(l)(t), falling factorials from pdiff (basis860.radial_jets); cl derivative by the product rule on the exact factors',
            'T_version': '860-T1', 'switch_radius_r_s': R_SWITCH, 'origin_order_production': ORIGIN_ORDER_PRODUCTION, 'origin_orders_integrator': [48, 56],
            'replay_reference_file': REPLAY_REFERENCE_FILE,
            'R_f_assembly_v9': {'arithmetic': 'numpy longdouble (see extended_arithmetic), one rounding to binary64 at the end',
                                'origin_disk_r_le_0.02': 'order-48 Decimal Taylor polynomial of R_f (exact a_000), coefficients converted to longdouble, evaluated in longdouble (origin860.evaluate_series_ld)',
                                '0.02_lt_r_lt_r_s': 'direct form w_x f_x + w_y f_y + q f with the center-subtracted q = sum_i c_i (ratio_i - s_i) (expm1 forms for the 16 strained low generators, basis860.centered_ratio); r_s = 1 (SPEC v9.2)',
                                'r_ge_r_s': 'stable linear transport sum_i a_i [-j_i (cl-1) f_i + 2 cl frem_i] plus the nonlinear part -psi_y f_x + psi_x f_y + ratio f',
                                'jacobian_columns': 'binary64, formed from the extended generator values rounded once and the rounded field multipliers (w_x, w_y, q inside r_s = 1; stable L_i columns for r >= 1, the same switch as R_f, a recorded choice where v9.2 allows r_s = 2); origin columns: the 860 Decimal column polynomials (order 48, formed in a fork pool, bitwise independent of the process count) evaluated in binary64 by origin860.evaluate_series_columns (terms in a fixed order: total degree descending, then x-degree descending; no BLAS, independent of thread count)'},
            'extended_arithmetic': extended_arithmetic_statement(), 'R_f_path_v93': rf_path_statement(),
            'floors': {'generator_fields_T2.7_T2.7H_T2.7HX': '|difference| <= 1e-11 max(band_max, 1e-30): absolute 1e-41 where band_max < 1e-30, every such case listed', 'columns_and_Rf_T2.6b_T2.6c_T2.6x': 'same rule', 'structural_zeros': 'exact 0.0 expected, listed with production values, gated at absolute 1e-41'},
            'supported_production_configurations': {'Model860': 'one-point, batch and training/refined-mesh calls; cache build in blocks of 4096 nodes (remainder block allowed); cache-build threads 1, 4 or 8; BLAS workers 1, 4 or 8 (Jacobian only)',
                                                    'stateless': 'fields860.residual with block_size 2048 (tests) or 4096 (integrator), serial or fork pool with up to 8 processes', 'integrator': 'Integrator860.stateless / independent_integral panels through fields860.residual_parallel (block 4096, procs = workers)'},
            'rounding_bound_kappa_v93': {'kappa': 2**11, 'rule': 'kappa = max(2^11, 4 rho_max)', 'rho_max_dev_check': 0.18055694060540947, 'rho_u': 2.**-64, 'source': 'outputs/dev_v9/dev_points.json (R_f at the 26+2 g2_v3 points and the 23 verifier points, three shapes); to be confirmed by the g2_v4 t26 record'},
            'origin_disk_order': {'production': ORIGIN_ORDER_PRODUCTION, 'monitor_check_order': ORIGIN_ORDER_PRODUCTION+8, 'integrator_orders': [48, 56], 'certificate': 'c4-ver research/basis860-origin-truncation (order 48 uniform on c_l in [51/50, 10] at 1e-41)'},
            'low_block_provider': 'basis860.generator_block (own longdouble route: exact exponent differences, falling-factorial radial jets, frozen polynomial helpers _harmonics/_assemble)',
            'high_block_provider': 'basis860.generator_block (own Legendre derivative recurrences, frozen N_n, same radial route)',
            'linear_transport': 'SPEC v7 section 5a identity L F(chi_mkj) = -j(cl-1)F(chi) + 2cl(k-p_j)F(u chi) for r >= r_s; derivative form for the high-block remainder',
            'derivative_version': 'full analytic cl dependence through p_j (exact-factor product rule)'}
