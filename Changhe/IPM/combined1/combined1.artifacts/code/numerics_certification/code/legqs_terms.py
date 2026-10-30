"""Term algebra for potentials with multi-scale (legqs) functions (lane c1-n3; see notes/LEGQS_EXTENSION_PLAN.md).

A term is  coef * trig(n theta) * r^s * (1+r^2)^(p_j - i) * prod_R (R^2 + r^2)^(-N_R),  keyed by (j, kind, n, s, i, Ns) where
Ns is a tuple of nonnegative integers, one per scale in SCALES (sorted list of R0 values present), p_j = (3 + gamma - j delta)/2.
Fields are dicts key -> Fraction. Cartesian derivatives follow e2norms.gen_derivative for the r^s and (1+r^2)^u factors and the analogous
rule d/dx (R^2+r^2)^(-N) = -2 N x (R^2+r^2)^(-N-1) (x = r cos theta) for the scale factors. Products add the exponents.

Validation (self test, python3 legqs_terms.py): with no scale factors the derivatives agree with e2norms.gen_derivative on random fields,
and a legqs generator with R0 = 1 equals the ordinary generator sum_i b_i r^(2m+2i) (1+r^2)^(p-m-i) cos(2m theta).
"""
from fractions import Fraction as Q
from math import comb
import sys, json, random
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E

def legendre_monomials(n): return E.legendre_monomials(n)

def add(T, key, v):
    j, kind, n, s, i, Ns = key
    if n < 0:
        n = -n
        if kind == 's': v = -v
    if not v or (kind == 's' and n == 0): return
    key = (j, kind, n, s, i, Ns)
    T[key] = T.get(key, Q(0)) + v
    if T[key] == 0: del T[key]

def load_generators(path):
    """Return (c, SCALES, terms of chi as a field dict with s = 2k, i = k - m ... ) from a c1-n1 generator list (mono, leg, legqs specs)."""
    d = json.loads(Path(path).read_text()); c = Q(d['cl'] if 'cl' in d else d['cl_exact'])
    scales = sorted({Q(g['spec'][4]) for g in d['generators'] if g['spec'][0] == 'legqs'})
    nsc = len(scales); chi = {}
    for g in d['generators']:
        j, m, v = g['j'], g['m'], Q(g['coef']); sp = g['spec']
        if sp[0] == 'mono':
            h = sp[1]; add(chi, (j, 'c', 2 * m, 2 * (m + h), m + h, (0,) * nsc), v)      # r^(2m) cos(2m th) t^h (1+r^2)^p = r^(2(m+h)) (1+r^2)^(p-m-h)
        elif sp[0] == 'leg':
            w, n = sp[1:]
            for h, b in legendre_monomials(n).items():
                add(chi, (j, 'c', 2 * m, 2 * (m + w + h), m + w + h, (0,) * nsc), v * b)
        elif sp[0] == 'legqs':
            w, n, qpow, R0 = sp[1], sp[2], sp[3], Q(sp[4]); idx = scales.index(R0)
            # t_R^w u_R^qpow P_n(2 t_R - 1) = sum_i b_i t_R^i,  t_R = r^2/(R0^2+r^2), u_R = R0^2/(R0^2+r^2) = 1 - t_R
            poly = {}
            for h, b in legendre_monomials(n).items():          # P_n(2 t_R - 1) = sum_h b t_R^h
                # multiply by t_R^w (1 - t_R)^qpow
                for q in range(qpow + 1):
                    e = w + h + q; coef = b * comb(qpow, q) * (-1) ** q
                    poly[e] = poly.get(e, Q(0)) + coef
            for e, b in poly.items():
                if not b: continue
                Ns = [0] * nsc; Ns[idx] = e
                # H_m (1+r^2)^(p-m) r^(2e) (R0^2+r^2)^(-e): s = 2m + 2e, i = m
                add(chi, (j, 'c', 2 * m, 2 * (m + e), m, tuple(Ns)), v * b)
        else: raise ValueError(sp)
    return c, scales, chi

def derivative(T, axis, scales, c):
    """One Cartesian derivative of a field (dict key -> Fraction)."""
    gamma = 1 / c; delta = 1 - gamma
    out = {}
    for (j, kind, n, s, i, Ns), v in T.items():
        p = (3 + gamma - j * delta) / 2; u = p - i
        def put(k2, n2, s2, i2, Ns2, val): add(out, (j, k2, n2, s2, i2, Ns2), val)
        if axis == 'x':
            if kind == 'c':
                put('c', n + 1, s - 1, i, Ns, v * (s - n) / 2); put('c', n - 1, s - 1, i, Ns, v * (s + n) / 2)
                put('c', n + 1, s + 1, i + 1, Ns, v * u);        put('c', n - 1, s + 1, i + 1, Ns, v * u)
                for idx, N in enumerate(Ns):
                    if N:
                        Ns2 = tuple(N + (1 if t == idx else 0) for t, N in enumerate(Ns)); NN = Ns[idx]
                        put('c', n + 1, s + 1, i, Ns2, -v * NN); put('c', n - 1, s + 1, i, Ns2, -v * NN)
            else:
                put('s', n + 1, s - 1, i, Ns, v * (s - n) / 2); put('s', n - 1, s - 1, i, Ns, v * (s + n) / 2)
                put('s', n + 1, s + 1, i + 1, Ns, v * u);        put('s', n - 1, s + 1, i + 1, Ns, v * u)
                for idx, N in enumerate(Ns):
                    if N:
                        Ns2 = tuple(N + (1 if t == idx else 0) for t, N in enumerate(Ns)); NN = Ns[idx]
                        put('s', n + 1, s + 1, i, Ns2, -v * NN); put('s', n - 1, s + 1, i, Ns2, -v * NN)
        else:
            if kind == 'c':
                put('s', n + 1, s - 1, i, Ns, v * (s - n) / 2);  put('s', n - 1, s - 1, i, Ns, -v * (s + n) / 2)
                put('s', n + 1, s + 1, i + 1, Ns, v * u);         put('s', n - 1, s + 1, i + 1, Ns, -v * u)
                for idx, N in enumerate(Ns):
                    if N:
                        Ns2 = tuple(N + (1 if t == idx else 0) for t, N in enumerate(Ns)); NN = Ns[idx]
                        put('s', n + 1, s + 1, i, Ns2, -v * NN); put('s', n - 1, s + 1, i, Ns2, v * NN)
            else:
                put('c', n - 1, s - 1, i, Ns, v * (s + n) / 2);  put('c', n + 1, s - 1, i, Ns, -v * (s - n) / 2)
                put('c', n - 1, s + 1, i + 1, Ns, v * u);         put('c', n + 1, s + 1, i + 1, Ns, -v * u)
                for idx, N in enumerate(Ns):
                    if N:
                        Ns2 = tuple(N + (1 if t == idx else 0) for t, N in enumerate(Ns)); NN = Ns[idx]
                        put('c', n - 1, s + 1, i, Ns2, v * NN); put('c', n + 1, s + 1, i, Ns2, -v * NN)
    return out

def scale(T, a): return {k: v * a for k, v in T.items() if v * a}

def plus(*Ts):
    out = {}
    for T in Ts:
        for k, v in T.items(): add(out, k, v)
    return out

def mul(T1, T2):
    """Product of two fields: exponents add (j classes add as j1 + j2 with p_(j1) + p_(j2) handled by the caller: we keep a pair key)."""
    out = {}
    for (j1, k1, n1, s1, i1, N1), v1 in T1.items():
        for (j2, k2, n2, s2, i2, N2), v2 in T2.items():
            Ns = tuple(a + b for a, b in zip(N1, N2))
            for kind, mode, factor in E.trigprod(k1, n1, k2, n2):
                add(out, ((j1, j2), kind, mode, s1 + s2, i1 + i2, Ns), v1 * v2 * factor)
    return out

def xy_times(T, axis):
    """Multiply a field by x (axis 'x': r cos theta) or y (r sin theta)."""
    out = {}
    rk = 'c' if axis == 'x' else 's'
    for (j, kind, n, s, i, Ns), v in T.items():
        for kind2, mode, factor in E.trigprod(rk, 1, kind, n): add(out, (j, kind2, mode, s + 1, i, Ns), v * factor)
    return out

def residual(path):
    """F = (c X + U).grad rho - rho with rho = -d_y Lap chi, U = (-chi_xyy, chi_xxy); returns (c, scales, F as product field)."""
    c, scales, chi = load_generators(path)
    D = lambda T, ax: derivative(T, ax, scales, c)
    cx = D(chi, 'x'); cy = D(chi, 'y'); cxx = D(cx, 'x'); cxy = D(cx, 'y'); cyy = D(cy, 'y')
    cxxy = D(cxx, 'y'); cxyy = D(cxy, 'y'); cyyy = D(cyy, 'y')
    rho = scale(plus(cxxy, cyyy), Q(-1)); u1 = scale(cxyy, Q(-1)); u2 = cxxy
    rx = D(rho, 'x'); ry = D(rho, 'y')
    # single-class fields carry j; products carry (j1, j2). Represent c X.grad rho - rho as products with the unit field (j = 0 class? no:
    # p_0 is not 0). We attach the explicit factor (1+r^2)^0 class 'unit' = ('u',) with p = 0 handled in the integrator.
    unit = {('u', 'c', 0, 0, 0, (0,) * len(scales)): Q(1)}
    F = plus(scale(mul(unit, xy_times(rx, 'x')), c), scale(mul(unit, xy_times(ry, 'y')), c), scale(mul(unit, rho), Q(-1)), mul(u1, rx), mul(u2, ry))
    return c, scales, F

if __name__ == '__main__':
    # self test 1: derivative rules against e2norms.gen_derivative on random single-class fields without scale factors
    c = Q(4076476460239181, 2251799813685248); gamma = 1 / c; delta = 1 - gamma
    random.seed(3); ok = True
    for trial in range(20):
        j = random.randint(0, 7); k = random.randint(2, 9); d = random.randint(0, 3); p = (3 + gamma - j * delta) / 2
        T = {}; mine = {}
        for _ in range(4):
            kind = random.choice('cs'); n = random.randint(1, 6); l = random.randint(0, 3); v = Q(random.randint(-9, 9), random.randint(1, 5))
            if not v: continue
            E._addT(T, kind, n, l, v); add(mine, (j, kind, n, 2 * k - d + 2 * l, k + l, ()), v)
        for axis in 'xy':
            ref = E.gen_derivative(T, p, k, d, axis); got = derivative(mine, axis, [], c)
            refm = {}
            for (kind, n, l), v in ref.items(): refm[(j, kind, n, 2 * k - (d + 1) + 2 * l, k + l, ())] = v
            if refm != got: ok = False; print('MISMATCH', trial, axis, sorted(refm.items())[:3], sorted(got.items())[:3])
    print('derivative rules agree with e2norms.gen_derivative:', ok)
    # self test 2: legqs generator with R0 = 1 equals an ordinary generator expansion (same chi as a field after mapping N -> i shift)
    import tempfile
    gens = {'cl': str(c), 'generators': [{'m': 2, 'j': 1, 'spec': ['legqs', 1, 2, 4, 1], 'coef': '3/7'}]}
    f = Path(tempfile.mkdtemp()) / 'g.json'; f.write_text(json.dumps(gens))
    c2, scales, chi = load_generators(f)
    # with R0 = 1: (1 + r^2)^(-N) merges into the (1+r^2) exponent: key (j, kind, n, s, i, (N,)) -> (j, kind, n, s, i + N, ())
    merged = {}
    for (j, kind, n, s, i, Ns), v in chi.items(): add(merged, (j, kind, n, s, i + Ns[0], ()), v)
    # ordinary expansion: t_1 = t, u_1 = 1 - t: chi = H_m (1+r^2)^(p-m) t^w (1-t)^4 P_n(2t-1) = sum over monomials t^e of coefficient b_e
    ref = {}
    for h, b in legendre_monomials(2).items():
        for q in range(5):
            e = 1 + h + q; add(ref, (1, 'c', 4, 4 + 2 * e, 2 + e, ()), Q(3, 7) * b * comb(4, q) * (-1) ** q)
    print('legqs with R0 = 1 equals the ordinary expansion:', merged == ref, len(ref), 'terms')
