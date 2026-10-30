"""Exact whole-plane residual norms of finite rational potentials (lane c1-n3, N3).

Self-contained reimplementation of the Beta-integral method of analysis2 (S1_PROOFS.md, P12) with
general radial weights. No code is imported from the read-only sources.

Reference: chi = sum_(j,m,k) a_(j,m,k) cos(2m theta) t^k (1+r^2)^(p_j), t = r^2/(1+r^2),
p_j = (3+gamma-j delta)/2, gamma = 1/c, delta = 1-gamma, k >= m >= 0 (canonical form).
rho = -d_y Delta chi, U = (-chi_xyy, chi_xxy), F = (c X + U).grad rho - rho.

Compactified representation of a degree-d derivative component (P12.1, section 2):
  even d:  r (1-t)^(d/2)       sum_(ell,n,kind) w^ell P(t) T_(n,kind)(theta)
  odd d:   (1-t)^((d-1)/2)     sum_(ell,n,kind) w^ell P(t) T_(n,kind)(theta)
with w = (1-t)^(delta/2), T = cos or sin, P exact rational polynomials in t.
A dictionary D[(ell, kind, n)] = fmpq_poly holds one component.

Squared norm with weight W(t)^2 = (1-t)^a t^b prod_i (1+c_i t)^(alpha_i):
  int |D^d F|^2 W^2 dX = (pi/2) sum over pairs ... exact Beta integrals, with the non-rational factors
  (1+c_i t)^(alpha_i) enclosed by binomial series with rigorous remainders (P12.1, section 4).
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)

Z = fmpq_poly([0, 1]); ONE = fmpq_poly([1]); OM = ONE - Z

def fq(x):
    if isinstance(x, fmpq): return x
    q = Q(x); return fmpq(q.numerator, q.denominator)
def aq(x):
    q = Q(str(x)) if not isinstance(q := x, Q) else x
    return arb(q.numerator) / q.denominator

# ---------------------------------------------------------------- references
def legendre_monomials(n):
    """P_n(2t-1) = sum_h (-1)^(n-h) C(n,h) C(n+h,h) t^h (shifted Legendre)."""
    return {h: Q((-1) ** (n - h) * comb(n, h) * comb(n + h, h)) for h in range(n + 1)}

def load_reference(path):
    """Return (c, A, source_sha256, canonical_sha256, meta). A maps (j,m,k) -> Fraction, canonical form."""
    path = Path(path); raw = path.read_bytes(); d = json.loads(raw)
    A = {}
    if 'generators' in d:
        c = Q(d['cl'] if 'cl' in d else d['cl_exact'])
        for g in d['generators']:
            j, m, v = g['j'], g['m'], Q(g['coef']); s = g['spec']
            if s[0] == 'mono': poly = {s[1]: Q(1)}
            else:
                assert s[0] == 'leg'; w, n = s[1:]
                poly = {w + h: b for h, b in legendre_monomials(n).items()}
            for h, b in poly.items():
                k = m + h; assert k >= m >= 0 and j >= 0
                A[(j, m, k)] = A.get((j, m, k), Q(0)) + v * b
    elif 'a_canonical' in d:
        c = Q(d['cl']); vals = d['a_canonical']
        # order I(j,m,k)=215j+26m-m(m-1)/2+(k-m): j<4, m<=9, m<=k<=25 (state 131 / 088 layout)
        assert d['order'] == 'I(j,m,k)=215j+26m-m(m-1)/2+(k-m)', d['order']
        assert len(vals) == 860
        for j in range(4):
            for m in range(10):
                for k in range(m, 26):
                    I = 215 * j + 26 * m - m * (m - 1) // 2 + (k - m)
                    v = Q(vals[I])
                    if v: A[(j, m, k)] = v
    elif 'canonical_order' in d:
        c = Q(d['cl'] if 'cl' in d else d['exact_parameters']['cl'])
        for key, v in zip(d['canonical_order'], d['canonical_coefficients']):
            v = Q(v)
            if v: A[tuple(key)] = v
    else:
        raise ValueError('unknown reference format')
    A = {k: v for k, v in A.items() if v}
    serial = '\n'.join(','.join(map(str, k)) + ':' + str(v) for k, v in sorted(A.items())) + '\n'
    meta = {'path': str(path), 'terms': len(A), 'max_j': max(k[0] for k in A), 'max_m': max(k[1] for k in A),
            'max_k': max(k[2] for k in A), 'cl': str(c)}
    return c, A, hashlib.sha256(raw).hexdigest(), hashlib.sha256(serial.encode()).hexdigest(), meta

# ---------------------------------------------------------------- exact polar derivatives of chi generators
def _addT(T, kind, n, l, value):
    if n < 0:
        n = -n
        if kind == 's': value = -value
    if not value or (kind == 's' and n == 0): return
    key = (kind, n, l)
    T[key] = T.get(key, Q(0)) + value
    if T[key] == 0: del T[key]

def gen_derivative(T, p, k, d, axis):
    """One Cartesian derivative of terms v * trig(n theta) * r^(2k-d+2l) * (1+r^2)^(p-k-l)."""
    out = {}
    for (kind, n, l), v in T.items():
        s = 2 * k - d + 2 * l; u = p - k - l
        if axis == 'x':
            _addT(out, kind, n + 1, l, v * (s - n) / 2); _addT(out, kind, n - 1, l, v * (s + n) / 2)
            _addT(out, kind, n + 1, l + 1, v * u);        _addT(out, kind, n - 1, l + 1, v * u)
        elif kind == 'c':
            _addT(out, 's', n + 1, l, v * (s - n) / 2);  _addT(out, 's', n - 1, l, -v * (s + n) / 2)
            _addT(out, 's', n + 1, l + 1, v * u);         _addT(out, 's', n - 1, l + 1, -v * u)
        else:
            _addT(out, 'c', n - 1, l, v * (s + n) / 2);  _addT(out, 'c', n + 1, l, -v * (s - n) / 2)
            _addT(out, 'c', n - 1, l + 1, v * u);         _addT(out, 'c', n + 1, l + 1, -v * u)
    return out

def add(D, ell, kind, n, p):
    if n < 0:
        n = -n
        if kind == 's': p = -p
    if not p or (kind == 's' and n == 0): return
    key = (ell, kind, n)
    D[key] = D.get(key, fmpq_poly([])) + p
    if not D[key]: del D[key]

def chi_compact(A, c, d, nx):
    """Compactified polynomials of d_x^nx d_y^(d-nx) chi, d in {3,4}: keys (ell=j+1, kind, n) -> poly in t.
    Degree 3 carries the factor r, degree 4 none (both with w^ell)."""
    gamma = 1 / c; delta = 1 - gamma; out = {}
    for (j, m, k), a in A.items():
        p = (3 + gamma - j * delta) / 2
        T = {('c', 2 * m, 0): a}
        for di, axis in enumerate('x' * nx + 'y' * (d - nx)):
            T = gen_derivative(T, p, k, di, axis)
        for (kind, n, l), v in T.items():
            P = out.setdefault((j + 1, kind, n), {})
            power = k - 2 + l
            P[power] = P.get(power, Q(0)) + v
    ans = {}
    for (ell, kind, n), P in out.items():
        P = {i: v for i, v in P.items() if v}
        assert all(i >= 0 for i in P), (d, nx, ell, kind, n, min(P))
        if P: add(ans, ell, kind, n, fmpq_poly([fq(P.get(i, 0)) for i in range(max(P) + 1)]))
    return ans

def plus(*terms):
    out = {}
    for scale, D in terms:
        for (ell, kind, n), p in D.items(): add(out, ell, kind, n, p * fq(scale))
    return out

def trigprod(k, n, l, m):
    if k == 'c' and l == 'c': return [('c', n + m, Q(1, 2)), ('c', n - m, Q(1, 2))]
    if k == 's' and l == 's': return [('c', n - m, Q(1, 2)), ('c', n + m, -Q(1, 2))]
    if k == 's': return [('s', n + m, Q(1, 2)), ('s', n - m, Q(1, 2))]
    return [('s', n + m, Q(1, 2)), ('s', n - m, -Q(1, 2))]

def mul(D, E):
    out = {}
    for (ell, k, n), p in D.items():
        for (ell2, l, m), q in E.items():
            v = p * q
            for kind, mode, factor in trigprod(k, n, l, m): add(out, ell + ell2, kind, mode, v * fq(factor))
    return out

def diff(D, d, axis, delta):
    """One Cartesian derivative of a degree-d compactified component (P12.1 section 2)."""
    out = {}
    for (ell, kind, n), p in D.items():
        if d % 2 == 0:
            rad = (ONE - Z * fq(d + ell * delta)) * p + 2 * Z * OM * p.derivative(); ang = p
        else:
            rad = -fq(d - 1 + ell * delta) * p + 2 * OM * p.derivative()
            if n:
                ang, rem = divmod(p, Z); assert not rem, ('origin pole', d, ell, kind, n)
            else: ang = fmpq_poly([])
        rk = 'c' if axis == 'x' else 's'
        for kk, nn, factor in trigprod(rk, 1, kind, n): add(out, ell, kk, nn, rad * fq(factor))
        if n:
            ak = 's' if axis == 'x' else 'c'; dk = 's' if kind == 'c' else 'c'
            sign = (-1 if kind == 'c' else 1) * (-1 if axis == 'x' else 1)
            for kk, nn, factor in trigprod(ak, 1, dk, n): add(out, ell, kk, nn, ang * fq(sign * n * factor))
    return out

def residual_polynomials(A, c, max_order=3, log=print):
    """All compactified components D[(d, nx)] of d_x^nx d_y^(d-nx) F for d <= max_order."""
    delta = 1 - 1 / c; start = time.monotonic(); j3 = {}; j4 = {}
    for d, save in [(3, j3), (4, j4)]:
        for nx in range(d):
            save[nx] = chi_compact(A, c, d, nx)
    log(f'chi derivatives done {time.monotonic()-start:.1f}s')
    rho = plus((-1, j3[0]), (-1, j3[2])); u1 = plus((-1, j3[1])); u2 = j3[2]
    rx = plus((-1, j4[1]), (-1, j4[3])); ry = plus((-1, j4[0]), (-1, j4[2]))
    cx = {(0, 'c', 1): ONE}; sy = {(0, 's', 1): ONE}
    F = plus((c, mul(cx, rx)), (c, mul(sy, ry)), (-1, rho), (1, mul(u1, rx)), (1, mul(u2, ry)))
    log(f'F assembled {time.monotonic()-start:.1f}s, components {len(F)}')
    D = {(0, 0): F}
    for d in range(max_order):
        for nx in range(d + 2):
            D[d + 1, nx] = diff(D[d, 0], d, 'y', delta) if nx == 0 else diff(D[d, nx - 1], d, 'x', delta)
        for nx in range(1, d + 1):
            assert D[d + 1, nx] == diff(D[d, nx], d, 'y', delta), ('mixed derivative mismatch', d, nx)
        log(f'derivative order {d+1} done {time.monotonic()-start:.1f}s')
    fields = {'rho': rho, 'u1': u1, 'u2': u2, 'rho_x': rx, 'rho_y': ry}
    return D, fields

# ---------------------------------------------------------------- exact integration
def endpoint(p):
    q = 0
    while p and p(1) == 0:
        p, rem = divmod(p, OM); assert not rem; q += 1
    assert p and p(1) != 0
    return q, p

def series_factor(cc, alpha, N):
    """(1+cc t)^alpha on [0,1] = pref * (1+z)^alpha, z = (cc t - cc/2)/(1+cc/2) in [-z0, z0], z0 = cc/(2+cc).
    Returns (pref as Fraction base and exponent, polynomial G_N(t), rigorous uniform remainder eps)."""
    cc = Q(cc); alpha = Q(alpha); assert cc > 0
    mid = 1 + cc / 2; z0 = cc / (2 + cc)
    z = (fq(cc) * Z - fq(cc / 2)) * fq(1 / mid)
    p = ONE; term = ONE; coef = fmpq(1)
    for n in range(1, N + 1):
        coef *= fq(alpha - n + 1) / n; term *= z; p += coef * term
    nextcoef = coef * fq(alpha - N) / (N + 1)
    # |binom(alpha,n)| decreasing for n > alpha+1 ... ratio |alpha-n|/(n+1) < 1 for n >= alpha; geometric tail bound
    assert N >= 1 and abs(alpha - N) < N + 1
    eps = abs(nextcoef) * fq(z0 ** (N + 1)) / fq(1 - z0)
    return mid, alpha, p, eps

def integral(p, b, cache):
    """int_0^1 t^n (1-t)^b dt summed over the polynomial p (exact rational), b > -1 rational."""
    need = p.degree() + 1
    if b not in cache: cache[b] = [fq(1 / (b + 1))]
    bet = cache[b]
    while len(bet) < need:
        n = len(bet); bet.append(bet[-1] * n / fq(b + n + 1))
    return sum((coef * bet[n] for n, coef in enumerate(p.coeffs())), fmpq(0))

def norm(D, d, delta, a_shift=Q(0), t_power=0, series=(), N=56, label=''):
    """Enclosure of || W D^d F ||_2 with W^2 = (1-t)^a_shift t^t_power prod (1+c t)^alpha.
    a_shift and t_power are exact; series = [(c, alpha), ...] rigorous binomial enclosures.
    Returns a dict with status FINITE (norm_lower, norm_upper as decimal strings of arb bounds) or INFINITE."""
    start = time.monotonic(); groups = {}; bad = []; facts = []
    a_shift = Q(a_shift)
    for nx in range(d + 1):
        modes = {}
        for (ell, kind, n), p in D[d, nx].items():
            q, p2 = endpoint(p)
            modes.setdefault((kind, n), []).append((ell, q, p2))
            b = Q(d - 3) + ell * delta + 2 * q + a_shift
            facts.append({'nx': nx, 'ell': ell, 'kind': kind, 'mode': n, 'order': q, 'diagonal_exponent': str(b)})
            if b <= -1: bad.append(facts[-1])
        ells = {ell for rows in modes.values() for ell, q, p in rows}
        for l in ells:
            for m in ells:
                if l != m: assert ((l - m) * delta / 2).denominator != 1, 'resonant branches'
        if bad: continue
        for (kind, n), rows in modes.items():
            for i, (ell, q, p) in enumerate(rows):
                for j in range(i, len(rows)):
                    ell2, q2, p2 = rows[j]
                    b = Q(d - 3) + (ell + ell2) * delta / 2 + q + q2 + a_shift
                    factor = comb(d, nx) * (2 if n == 0 and kind == 'c' else 1) * (1 if i == j else 2)
                    v = p * p2 * factor
                    if d % 2 == 0: v *= Z
                    if t_power: v *= Z ** t_power
                    groups[b] = groups.get(b, fmpq_poly([])) + v
    if bad:
        return {'label': label, 'status': 'INFINITE', 'bad_sectors': bad[:20], 'n_bad': len(bad),
                'scope': 'exact nonzero endpoint sector with square exponent <= -1 (nonresonant branches)'}
    cache = {}; S = fmpq(0); T = fmpq(0)
    wp = ONE; eps_total = fmpq(0); pref = arb(1); sdesc = []
    for cc, alpha in series:
        mid, al, p, eps = series_factor(cc, alpha, N)
        wp = wp * p; eps_total = eps_total + eps  # products of enclosures handled below (single factor expected)
        pref *= aq(mid) ** aq(al); sdesc.append({'c': str(cc), 'alpha': str(alpha), 'N': N, 'eps': str(eps)})
    assert len(series) <= 1, 'one series factor supported in this version'
    for i, (b, p) in enumerate(sorted(groups.items())):
        assert b > -1
        S += integral(p, b, cache)
        if series: T += integral(p * wp, b, cache)
    assert S >= 0
    if series:
        lo = T - eps_total * S; hi = T + eps_total * S; assert lo >= 0
    else:
        T = S; lo = hi = S
    sqlo = arb.pi() / 2 * pref * aq(Q(str(lo))); sqhi = arb.pi() / 2 * pref * aq(Q(str(hi)))
    assert sqlo.is_finite() and sqhi.is_finite() and sqlo >= 0
    nl = sqlo.sqrt(); nh = sqhi.sqrt()
    return {'label': label, 'status': 'FINITE', 'norm_lower': str(nl.lower()), 'norm_upper': str(nh.upper()),
            'norm_lower_ball': nl.str(40), 'norm_upper_ball': nh.str(40),
            'base_beta_sum': str(S), 'weighted_beta_sum': str(T), 'series': sdesc,
            'a_shift': str(a_shift), 't_power': t_power, 'n_groups': len(groups),
            'elapsed_seconds': time.monotonic() - start}

# ---------------------------------------------------------------- standard norm sets
OMEGA = [(Q(3), Q(4, 5))]          # omega^2 = (1+4r^2)^(4/5) = (1+3t)^(4/5) (1-t)^(-4/5)
def standard_norms(D, delta, N=56, log=print, on_update=None):
    """NORM-A2-E2 components (G0, G1, P2), NORM-A2-Q3, the Hdot^-1 proxy ||rF||_2 (>= ||F||_H for odd-in-y F),
    and the weighted components of NORM-A2-Nw: P_1 = ||<r>^(-1/5) DF||_2 (exact), P_2 = P2."""
    out = {}
    specs = [
        ('G0', 0, Q(0), 0, ()),                 # ||F||_2
        ('rF', 0, Q(-1), 1, ()),                # ||r F||_2 : r^2 = t/(1-t)
        ('G1', 1, Q(0), 0, ()),                 # ||grad F||_2
        ('P2', 2, Q(-4, 5), 0, OMEGA),          # ||omega D^2 F||_2
        ('Q3', 3, Q(-4, 5), 0, OMEGA),          # ||omega D^3 F||_2
        ('Pw1', 1, Q(1, 5), 0, ()),             # ||<r>^(-1/5) D F||_2 : <r>^(-2/5) = (1-t)^(1/5)
        ('D2', 2, Q(0), 0, ()),                 # ||D^2 F||_2 (unweighted)
        ('rD2', 2, Q(-1), 1, ()),               # ||r D^2 F||_2
    ]
    for label, d, a, tp, ser in specs:
        if (d, 0) not in D: continue
        out[label] = norm(D, d, delta, a, tp, ser, N, label)
        if on_update: on_update(out)
        r = out[label]; log(f"{label}: {r['status']} {r.get('norm_lower_ball','')} {r.get('norm_upper_ball','')} ({r.get('elapsed_seconds',0):.1f}s)")
    return out

def e2_assembly(norms, s_list=(Q(1, 2 ** 18), Q(1, 2 ** 28))):
    """Certified E_2 upper and lower bounds and N_s upper bound (P12.1 section 6, P8.1) from component enclosures."""
    ctx_prec = ctx.prec
    need = ['G0', 'G1', 'P2', 'rF']
    res = {}
    if any(norms.get(k, {}).get('status') != 'FINITE' for k in need):
        res['E2_status'] = 'INFINITE_OR_UNKNOWN'; return res
    up = {k: arb(norms[k]['norm_upper']) for k in need + (['Q3'] if norms.get('Q3', {}).get('status') == 'FINITE' else [])}
    lo = {k: arb(norms[k]['norm_lower']) for k in need}
    E2_up = (up['P2'] ** 2 + 2 ** 14 * up['G1'] ** 2 + 2 ** 18 * up['G0'] ** 2 + 2 ** 18 * arb(20) / 21 * up['rF'] ** 2).sqrt()
    # lower bound: drop the H component (>= 0), use component lower bounds
    E2_lo = (lo['P2'] ** 2 + 2 ** 14 * lo['G1'] ** 2 + 2 ** 18 * lo['G0'] ** 2).sqrt()
    res['E2_upper_with_rF_for_H'] = str(E2_up.upper()); res['E2_lower_without_H'] = str(E2_lo.lower())
    res['E2_components_upper'] = {k: str(v.upper()) for k, v in up.items()}
    res['E2_weighted_squares_upper'] = {'P2^2': str((up['P2'] ** 2).upper()), '2^14 G1^2': str((2 ** 14 * up['G1'] ** 2).upper()),
                                        '2^18 G0^2': str((2 ** 18 * up['G0'] ** 2).upper()),
                                        '2^18 (20/21) rF^2': str((2 ** 18 * arb(20) / 21 * up['rF'] ** 2).upper())}
    if 'Q3' in up:
        for s in s_list:
            sa = aq(s); E = E2_up; Qv = up['Q3']
            Ns = E ** (1 - sa) * (2 * Qv ** 2 + 16410 * E ** 2) ** (sa / 2) + 34 * sa * E
            res[f'Ns_upper_s={s}'] = str(Ns.upper())
            res[f'Ns_lower_s={s}'] = str(((1 - 34 * sa) * E2_lo).lower())
    return res

def run(path, name, outdir, N=56, max_order=3, prec=512):
    ctx.prec = prec; outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    logf = open(outdir / f'{name}_e2norms.log', 'a')
    def log(*a):
        msg = ' '.join(str(x) for x in a); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    t0 = time.monotonic()
    c, A, src_sha, can_sha, meta = load_reference(path)
    delta = 1 - 1 / c
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {name}: {meta} source_sha256={src_sha} canonical_sha256={can_sha}')
    D, fields = residual_polynomials(A, c, max_order, log)
    rec = {'utc_start': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'name': name, 'source_path': str(path),
           'source_sha256': src_sha, 'canonical_sha256': can_sha, 'reference_meta': meta, 'cl': str(c), 'delta': str(delta),
           'precision_bits': prec, 'series_degree': N, 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'norms': {}, 'status': 'RUNNING'}
    dest = outdir / f'{name}_e2norms.json'
    def save():
        rec['utc_updated'] = datetime.now(timezone.utc).isoformat(timespec='seconds'); rec['elapsed_seconds'] = time.monotonic() - t0
        dest.write_text(json.dumps(rec, indent=1) + '\n')
    def on_update(partial):
        rec['norms'] = partial; save()
    rec['norms'] = standard_norms(D, delta, N, log, on_update); save()
    rec['assembly'] = e2_assembly(rec['norms']); rec['status'] = 'COMPLETE'; save()
    log(json.dumps(rec['assembly'], indent=1)); log(f'DONE {name} {time.monotonic()-t0:.1f}s')
    # compact record of the residual polynomials (degree 0 only; derivatives are regenerated by the audit)
    poly = {'0,0': [{'ell': ell, 'kind': kind, 'mode': n, 'coeff': [str(v) for v in p.coeffs()]}
                    for (ell, kind, n), p in sorted(D[0, 0].items())]}
    (outdir / f'{name}_Fpoly.json').write_text(json.dumps({'name': name, 'canonical_sha256': can_sha, 'delta': str(delta),
                                                           'cl': str(c), 'polynomials': poly}, separators=(',', ':')) + '\n')
    return rec

if __name__ == '__main__':
    path, name, outdir = sys.argv[1:4]
    N = int(sys.argv[4]) if len(sys.argv) > 4 else 56
    run(path, name, outdir, N)
