"""Packed (e2norms-style) representation of potentials with multi-scale legqs functions: generator stage (lane c1-n3).
Status 2026-10-29T07:5xZ: load_reference_legqs, gen_derivative_s and chi_compact_s are written and self-tested; diff_s, mul_s and the
norm integration (notes/LEGQS_EXTENSION_PLAN.md sections 3b and 7) are the shift-3 work.

Representation of a term during the generator stage: coef * trig(n theta) * r^s * (1+r^2)^(p-i) * Phi_N, Phi_N = (R^2+r^2)^(-N) =
v^N (1+a v)^(-N), v = 1/(1+r^2), a = R^2 - 1 (one scale per generator; products mix scales later). Keys (kind, n, s, i, N); p and a implicit.
A legqs generator H_m (1+r^2)^(p-m) t_R^w u_R^Q P_n(2 t_R - 1) = sum_e b_e r^(2(m+e)) (1+r^2)^(p-m) (R^2+r^2)^(-e) is the sum over e of the
ordinary term with k = m + e times (1 + a v)^(-e), because (1+r^2)/(R^2+r^2) = 1/(1 + a v).
Derivative of the extra factor: d/dx Phi_N = -2 N x Phi_(N+1): a term with r cos(theta) (mode n -> n +/- 1, s -> s + 1), i unchanged and
N -> N + 1, coefficient -N for each of the two trig terms; same signs as the (1+r^2) rule of e2norms.gen_derivative.
Packed polynomials: keys (ell = j+1, kind, n, N, a) -> fmpq_poly in t with power = s/2 + d/2 - 2 (= k - 2 + l for ordinary terms); the
standard (1-t) exponent of the degree form already contains the v^N of Phi_N, so the key factor is read as K_N = (1 + a v)^(-N) (plan
section 8); for N = 0 identical to e2norms.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json, sys, hashlib, random
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import fmpq, fmpq_poly
import e2norms as E
from e2norms import fq, _addT

def load_reference_legqs(path):
    """Return (c, A, A_s, src_sha, meta): A maps (j, m, k) -> Fraction for the ordinary part; A_s maps (j, m, k, N, a) -> Fraction for the
    legqs part (k = m + e, N = e, a = R0^2 - 1)."""
    path = Path(path); raw = path.read_bytes(); d = json.loads(raw)
    c = Q(d['cl'] if 'cl' in d else d['cl_exact']); A = {}; A_s = {}
    for g in d['generators']:
        j, m, v = g['j'], g['m'], Q(g['coef']); s = g['spec']
        if s[0] == 'mono':
            k = m + s[1]; A[(j, m, k)] = A.get((j, m, k), Q(0)) + v
        elif s[0] == 'leg':
            w, n = s[1:]
            for h, b in E.legendre_monomials(n).items():
                k = m + w + h; A[(j, m, k)] = A.get((j, m, k), Q(0)) + v * b
        elif s[0] == 'legqs':
            w, n, qpow, R0 = s[1], s[2], s[3], Q(s[4]); a = R0 * R0 - 1
            poly = {}
            for h, b in E.legendre_monomials(n).items():
                for q in range(qpow + 1):
                    e = w + h + q; poly[e] = poly.get(e, Q(0)) + b * comb(qpow, q) * (-1) ** q
            for e, b in poly.items():
                if not b: continue
                key = (j, m, m + e, e, a); A_s[key] = A_s.get(key, Q(0)) + v * b
        else: raise ValueError(s)
    A = {k: v for k, v in A.items() if v}; A_s = {k: v for k, v in A_s.items() if v}
    meta = {'path': str(path), 'ordinary_terms': len(A), 'legqs_terms': len(A_s), 'scales': sorted({str(k[4]) for k in A_s}), 'cl': str(c)}
    return c, A, A_s, hashlib.sha256(raw).hexdigest(), meta

def _addS(T, kind, n, s, i, N, value):
    if n < 0:
        n = -n
        if kind == 's': value = -value
    if not value or (kind == 's' and n == 0): return
    key = (kind, n, s, i, N)
    T[key] = T.get(key, Q(0)) + value
    if T[key] == 0: del T[key]

def gen_derivative_s(T, p, axis):
    """One Cartesian derivative of terms v * trig(n theta) r^s (1+r^2)^(p-i) Phi_N, Phi_N = (R^2+r^2)^(-N); keys (kind, n, s, i, N).
    Rules: r-type (s-1), (1+r^2)-type (s+1, i+1, factor u = p-i), scale-type (s+1, N+1, factor -N) since d/dx Phi_N = -2 N x Phi_(N+1)."""
    out = {}
    for (kind, n, s, i, N), v in T.items():
        u = p - i
        if axis == 'x':
            _addS(out, kind, n + 1, s - 1, i, N, v * (s - n) / 2); _addS(out, kind, n - 1, s - 1, i, N, v * (s + n) / 2)
            _addS(out, kind, n + 1, s + 1, i + 1, N, v * u);        _addS(out, kind, n - 1, s + 1, i + 1, N, v * u)
            if N: _addS(out, kind, n + 1, s + 1, i, N + 1, -v * N); _addS(out, kind, n - 1, s + 1, i, N + 1, -v * N)
        elif kind == 'c':
            _addS(out, 's', n + 1, s - 1, i, N, v * (s - n) / 2);  _addS(out, 's', n - 1, s - 1, i, N, -v * (s + n) / 2)
            _addS(out, 's', n + 1, s + 1, i + 1, N, v * u);         _addS(out, 's', n - 1, s + 1, i + 1, N, -v * u)
            if N: _addS(out, 's', n + 1, s + 1, i, N + 1, -v * N); _addS(out, 's', n - 1, s + 1, i, N + 1, v * N)
        else:
            _addS(out, 'c', n - 1, s - 1, i, N, v * (s + n) / 2);  _addS(out, 'c', n + 1, s - 1, i, N, -v * (s - n) / 2)
            _addS(out, 'c', n - 1, s + 1, i + 1, N, v * u);         _addS(out, 'c', n + 1, s + 1, i + 1, N, -v * u)
            if N: _addS(out, 'c', n - 1, s + 1, i, N + 1, -v * N); _addS(out, 'c', n + 1, s + 1, i, N + 1, v * N)
    return out

def chi_compact_s(A, A_s, c, d, nx):
    """Compactified polynomials of d_x^nx d_y^(d-nx) chi, d in {3, 4}: keys (ell = j+1, kind, n, N, a) -> fmpq_poly in t, power = s/2 + d/2 - 2.
    The (1-t) exponent i - s/2 + N equals d/2 for every term (generators have it 0 and each derivative adds 1/2), so the degree-d form of
    e2norms applies unchanged; the key factor is Phi_N = (R^2+r^2)^(-N) = v^N (1 + a v)^(-N), a = R^2 - 1. N = 0 reproduces e2norms.chi_compact."""
    gamma = 1 / c; delta = 1 - gamma; out = {}
    items = [((j, m, k), 2 * k, k, 0, Q(0), v) for (j, m, k), v in A.items()] + [((j, m, k), 2 * k, m, N, a, v) for (j, m, k, N, a), v in A_s.items()]
    for (j, m, k), s0, i0, N0, a, coef in items:
        p = (3 + gamma - j * delta) / 2
        T = {('c', 2 * m, s0, i0, N0): coef}
        for axis in 'x' * nx + 'y' * (d - nx):
            T = gen_derivative_s(T, p, axis)
        for (kind, n, s, i, N), v in T.items():
            assert i - Q(s, 2) + N == Q(d, 2), ('exponent bookkeeping', d, nx, kind, n, s, i, N)
            P = out.setdefault((j + 1, kind, n, N, a if N else Q(0)), {})
            power = Q(s, 2) + Q(d, 2) - 2; assert power.denominator == 1; power = int(power)
            P[power] = P.get(power, Q(0)) + v
    ans = {}
    for key, P in out.items():
        P = {q: v for q, v in P.items() if v}
        if not P: continue
        assert all(q >= 0 for q in P), (d, nx, key, min(P))
        # The standard (1-t) exponent of the degree-d form (i - s/2 + N = d/2) already contains the v^N of Phi_N = v^N K_N, so the packed
        # polynomial is the same in both conventions and the key factor is read as K_N = (1 + a v)^(-N) (plan section 8).
        ans[key] = fmpq_poly([fq(P.get(q, 0)) for q in range(max(P) + 1)])
    return ans

def add_s(D, key, p):
    ell, kind, n, N, a = key
    if n < 0:
        n = -n
        if kind == 's': p = -p
    if not p or (kind == 's' and n == 0): return
    key = (ell, kind, n, N, a)
    D[key] = D.get(key, fmpq_poly([])) + p
    if not D[key]: del D[key]

def diff_s(D, d, axis, delta):
    """One Cartesian derivative of a degree-d compactified component with scale keys (ell, kind, n, N, a) (K convention).
    Same radial and angular rules as e2norms.diff; the K factor adds the piece 2 N a t (1-t) P (even d) or 2 N a (1-t) P (odd d) with the
    trig product by cos(theta) (x) or sin(theta) (y) and the key N -> N+1 (plan section 8)."""
    Z, OM, ONE = E.Z, E.OM, E.ONE
    out = {}
    for (ell, kind, n, N, a), p in D.items():
        if d % 2 == 0:
            rad = (ONE - Z * fq(d + ell * delta)) * p + 2 * Z * OM * p.derivative(); ang = p
            radK = 2 * fq(N * a) * Z * OM * p if N else None
        else:
            rad = -fq(d - 1 + ell * delta) * p + 2 * OM * p.derivative()
            if n:
                ang, rem = divmod(p, Z); assert not rem, ('origin pole', d, ell, kind, n)
            else: ang = fmpq_poly([])
            radK = 2 * fq(N * a) * OM * p if N else None
        rk = 'c' if axis == 'x' else 's'
        for kk, nn, factor in E.trigprod(rk, 1, kind, n):
            add_s(out, (ell, kk, nn, N, a), rad * fq(factor))
            if radK is not None: add_s(out, (ell, kk, nn, N + 1, a), radK * fq(factor))
        if n:
            ak = 's' if axis == 'x' else 'c'; dk = 's' if kind == 'c' else 'c'
            sign = (-1 if kind == 'c' else 1) * (-1 if axis == 'x' else 1)
            for kk, nn, factor in E.trigprod(ak, 1, dk, n): add_s(out, (ell, kk, nn, N, a), ang * fq(sign * n * factor))
    return out

def canon_s(D):
    """Canonical form: the representation P K_N is not unique (K_N = (1 + a (1-t)) K_(N+1)); bring every (ell, kind, n, a) group to its
    largest N by multiplying the polynomials with (1 + a (1-t))^(Nmax - N). Exact. Needed to compare dictionaries; integration does not need it."""
    groups = {}
    for (ell, kind, n, N, a), p in D.items(): groups.setdefault((ell, kind, n, a), []).append((N, p))
    out = {}
    for (ell, kind, n, a), rows in groups.items():
        Nmax = max(N for N, p in rows); tot = fmpq_poly([])
        for N, p in rows: tot += p * (E.ONE + fq(a) * E.OM) ** (Nmax - N)
        if tot: out[(ell, kind, n, Nmax, a)] = tot
    return out

def to_tuple_key(D):
    """Single-scale keys (ell, kind, n, N, a) -> product keys (ell, kind, n, scales) with scales = tuple of (a, N) pairs, N > 0, sorted by a."""
    out = {}
    for (ell, kind, n, N, a), p in D.items():
        key = (ell, kind, n, ((a, N),) if N else ())
        out[key] = out.get(key, fmpq_poly([])) + p
    return {k: p for k, p in out.items() if p}

def _merge_scales(s1, s2):
    d = {}
    for a, N in s1 + s2: d[a] = d.get(a, 0) + N
    return tuple(sorted((a, N) for a, N in d.items() if N))

def mul_s(D1, D2):
    """Product of two packed fields in tuple-key form: ell add, trig products as e2norms.mul, scale tuples merge, polynomials multiply."""
    out = {}
    for (ell1, k1, n1, s1), p in D1.items():
        for (ell2, k2, n2, s2), q in D2.items():
            v = p * q; sc = _merge_scales(s1, s2)
            for kind, mode, factor in E.trigprod(k1, n1, k2, n2):
                nn = mode; pp = v * fq(factor)
                if nn < 0:
                    nn = -nn
                    if kind == 's': pp = -pp
                if not pp or (kind == 's' and nn == 0): continue
                key = (ell1 + ell2, kind, nn, sc)
                out[key] = out.get(key, fmpq_poly([])) + pp
    return {k: p for k, p in out.items() if p}

if __name__ == '__main__':
    c = Q(4076476460239181, 2251799813685248)
    # test 1: ordinary part identical to e2norms.chi_compact (d2 reference, all 12 derivative components)
    cc, A, src_sha, can_sha, meta = E.load_reference('source_copy/exact_refs/nb_d2_exact.json')
    ok = True
    for d in (3, 4):
        for nx in range(d):
            ref = E.chi_compact(A, cc, d, nx); mine = chi_compact_s(A, {}, cc, d, nx)
            mine2 = {(ell, kind, n): p for (ell, kind, n, N, a), p in mine.items()}
            if ref != mine2: ok = False; print('MISMATCH ordinary', d, nx)
    print('ordinary part identical to e2norms.chi_compact on d2:', ok)
    # test 2: legqs generator with R0 = 1 (a = 0): the extra factor is 1, so the result must equal the ordinary expansion of the same
    # function H_m (1+r^2)^(p-m) t^w (1-t)^4 P_n(2t-1) = sum_e b_e r^(2(m+e)) (1+r^2)^(p-m-e)  (ordinary (j, m, k = m+e) terms)
    import tempfile
    gens = {'cl': str(c), 'generators': [{'m': 2, 'j': 1, 'spec': ['legqs', 1, 2, 4, 1], 'coef': '3/7'}, {'m': 3, 'j': 0, 'spec': ['mono', 2], 'coef': '-2/5'}]}
    f = Path(tempfile.mkdtemp()) / 'g.json'; f.write_text(json.dumps(gens))
    c2, A2, A2s, _, meta2 = load_reference_legqs(f)
    # ordinary expansion of the legqs generator
    A_ref = dict(A2)
    for h, b in E.legendre_monomials(2).items():
        for q in range(5):
            e = 1 + h + q; key = (1, 2, 2 + e); A_ref[key] = A_ref.get(key, Q(0)) + Q(3, 7) * b * comb(4, q) * (-1) ** q
    A_ref = {k: v for k, v in A_ref.items() if v}
    ok2 = True
    for d in (3, 4):
        for nx in range(d):
            ref = E.chi_compact(A_ref, c2, d, nx); mine = chi_compact_s(A2, A2s, c2, d, nx)
            # with a = 0 the N slot is inert: merge keys over N (the (1+0 v)^(-N) factor is 1)
            merged = {}
            for (ell, kind, n, N, a), p in mine.items():
                k3 = (ell, kind, n); merged[k3] = merged.get(k3, fmpq_poly([])) + p
            merged = {k: p for k, p in merged.items() if p}
            if ref != merged: ok2 = False; print('MISMATCH legqs R0=1', d, nx)
    print('legqs with R0 = 1 reproduces the ordinary expansion (all 7 derivative components):', ok2, meta2)
    # test 3: the scale rule against a direct symbolic derivative (sympy) on one term
    try:
        import sympy as sp
        x, y = sp.symbols('x y', real=True); r2 = x ** 2 + y ** 2; a = Q(99); p = Q(7, 3); k = 2; N = 2
        R2 = a + 1
        expr = (r2) ** k * (1 + r2) ** (p - k) * (R2 + r2) ** (-N) * sp.cos(2 * sp.atan2(y, x))   # s = 2k, i = k, n = 2
        dx = sp.diff(expr, x)
        pt = {x: sp.Rational(3, 7), y: sp.Rational(-2, 5)}; worst = 0.0
        for kind0 in 'cs':
            for axis in 'xy':
                trig0 = sp.cos(2 * sp.atan2(y, x)) if kind0 == 'c' else sp.sin(2 * sp.atan2(y, x))
                expr = (r2) ** k * (1 + r2) ** (p - k) * (R2 + r2) ** (-N) * trig0
                dref = sp.diff(expr, x if axis == 'x' else y)
                T = {(kind0, 2, 2 * k, k, N): Q(1)}; out = gen_derivative_s(T, p, axis)
                rec = 0
                for (kind, n, ss, ii, NN), v in out.items():
                    trig = sp.cos(n * sp.atan2(y, x)) if kind == 'c' else sp.sin(n * sp.atan2(y, x))
                    rec += sp.Rational(v.numerator, v.denominator) * trig * sp.sqrt(r2) ** ss * (1 + r2) ** (p - ii) * (R2 + r2) ** (-NN)
                worst = max(worst, abs(float((dref - rec).subs(pt).evalf(40))))
        print('scale derivative rule against sympy (all kinds and axes) at a point: max |difference| =', worst)
    except Exception as ex: print('sympy check skipped:', ex)
    # test 4: diff_s consistency: d_x of the degree-3 packed fields (K convention) equals the degree-4 packed fields of the generator stage
    gens = {'cl': str(c), 'generators': [{'m': 2, 'j': 1, 'spec': ['legqs', 1, 2, 4, 25], 'coef': '3/7'}, {'m': 3, 'j': 0, 'spec': ['mono', 2], 'coef': '-2/5'},
                                         {'m': 1, 'j': 2, 'spec': ['legqs', 2, 1, 4, 10], 'coef': '5/11'}]}
    f = Path(tempfile.mkdtemp()) / 'g.json'; f.write_text(json.dumps(gens))
    c4, A4, A4s, _, meta4 = load_reference_legqs(f); delta = 1 - 1 / c4; ok4 = True
    for nx in range(3):
        D3 = chi_compact_s(A4, A4s, c4, 3, nx)
        # the chi third derivatives are stored in the residual's degree-0 (even) form "r sum w^ell P T", the fourth in the degree-1 form
        got_x = canon_s(diff_s(D3, 0, 'x', delta)); ref_x = canon_s(chi_compact_s(A4, A4s, c4, 4, nx + 1))
        got_y = canon_s(diff_s(D3, 0, 'y', delta)); ref_y = canon_s(chi_compact_s(A4, A4s, c4, 4, nx))
        if got_x != ref_x: ok4 = False; print('MISMATCH diff_s x', nx, len(got_x), len(ref_x))
        if got_y != ref_y: ok4 = False; print('MISMATCH diff_s y', nx, len(got_y), len(ref_y))
    print('diff_s (K rule) consistent with the generator stage after canonicalization, degree 3 -> 4, two scales (R0 = 25, 10):', ok4, meta4['scales'])
    # N = 0: diff_s equals e2norms.diff
    D3 = chi_compact_s(A, {}, cc, 3, 1); D3e = {(ell, kind, n): p for (ell, kind, n, N, a), p in D3.items()}
    got = {(ell, kind, n): p for (ell, kind, n, N, a), p in diff_s(D3, 0, 'y', 1 - 1 / cc).items()}
    print('diff_s equals e2norms.diff when N = 0 (d2 chi third derivatives as degree-0 forms):', got == E.diff(D3e, 0, 'y', 1 - 1 / cc))
    print('and equals the generator-stage fourth derivatives:', got == {(ell, kind, n): p for (ell, kind, n, N, a), p in chi_compact_s(A, {}, cc, 4, 1).items()})
    # test 5: mul_s equals e2norms.mul when no scale factors are present (d2 fields), and merges scale tuples in products
    D3a = chi_compact_s(A, {}, cc, 3, 1); D4a = chi_compact_s(A, {}, cc, 4, 0)
    ref = E.mul({(ell, kind, n): p for (ell, kind, n, N, a), p in D3a.items()}, {(ell, kind, n): p for (ell, kind, n, N, a), p in D4a.items()})
    got = {(ell, kind, n): p for (ell, kind, n, sc), p in mul_s(to_tuple_key(D3a), to_tuple_key(D4a)).items()}
    print('mul_s equals e2norms.mul when N = 0 (d2, degree-3 x degree-4 fields):', got == ref)
    T3 = to_tuple_key(chi_compact_s(A4, A4s, c4, 3, 0)); T4 = to_tuple_key(chi_compact_s(A4, A4s, c4, 4, 0))
    prod = mul_s(T3, T4); scales_seen = sorted({sc for (ell, kind, n, sc) in prod})
    print('mul_s scale tuples in a two-scale product (first few):', scales_seen[:4], '... total keys', len(prod))
    unit = {(0, 'c', 0, ()): E.ONE}
    print('mul_s with the unit field is the identity:', mul_s(unit, T3) == T3)
