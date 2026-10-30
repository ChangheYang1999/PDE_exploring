"""Rigorous two-sided bounds for the homogeneous Hdot^-1 norm ||F||_H of an exact residual (lane c1-n3).

Method. Modes sin(n theta), n odd, are orthogonal in Hdot^-1. For each mode an approximate potential
phi_n = sum_i c_i psi_i, psi_i = r^3 (1-t)^beta_i t^k_i sin(n theta), is fitted (Galerkin for -Delta phi = F_n) at high
precision, its coefficients are rounded to exact rationals, and then with g = F_n + Delta phi (exact in the family):
    LB:  ||F_n||_H^2 >= <F_n, phi>^2 / ||grad phi||_2^2                        (duality, any phi)
    UB:  ||F_n||_H^2 <= ||grad phi||_2^2 + 2 <phi, g> + ||g||_H^2 <= ||grad phi||_2^2 + 2 <phi, g> + ||r g||_2^2
         and also ||F_n||_H <= ||grad phi||_2 + ||r g||_2,
using the exact identity ||grad(phi_true)||^2 = ||grad phi||^2 + 2<phi, g> + ||g||_H^2 and the parity Hardy inequality
||g||_H <= ||r g||_2 for functions without angular mode 0 (A2-THEOREM, S1_CLOSURE.md section 7a, last paragraph).
Every pairing and norm is an exact Beta integral (rational multiple of pi) in the compactified variable t = r^2/(1+r^2).

Representation. A field component of even degree d is r (1-t)^(d/2) sum (1-t)^beta P(t) T_n(theta), odd degree d is
(1-t)^((d-1)/2) sum (1-t)^beta P(t) T_n(theta); keys (beta: Fraction, kind, n). Degree -2 is used for potentials
(r^3 (1-t)^b S = r (1-t)^(-1) (1-t)^b t S). The branch exponents beta are rationals; keys whose beta differ by an
integer are merged (normalize) so that the endpoint-order extraction sees cancellations.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb, floor
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, arb_mat, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E
from e2norms import fq, aq, Z, ONE, OM, trigprod, endpoint, integral

# ------------------------------------------------------------------ representation with rational beta
def addB(D, beta, kind, n, p):
    if n < 0:
        n = -n
        if kind == 's': p = -p
    if not p or (kind == 's' and n == 0): return
    key = (beta, kind, n)
    D[key] = D.get(key, fmpq_poly([])) + p
    if not D[key]: del D[key]

def from_ell(D, delta):
    out = {}
    for (ell, kind, n), p in D.items(): addB(out, Q(ell) * delta / 2, kind, n, p)
    return out

def normalize(D):
    """Merge keys with integer beta differences onto the smallest beta of each class."""
    classes = {}
    for (beta, kind, n), p in D.items():
        classes.setdefault((beta - floor(beta), kind, n), []).append((beta, p))
    out = {}
    for (frac, kind, n), rows in classes.items():
        bmin = min(b for b, p in rows); tot = fmpq_poly([])
        for b, p in rows:
            e = b - bmin; assert e.denominator == 1 and e >= 0
            tot += p * OM ** int(e)
        if tot: out[(bmin, kind, n)] = tot
    return out

def scale(D, s):
    return {k: p * fq(s) for k, p in D.items() if p}

def plusB(*Ds):
    out = {}
    for D in Ds:
        for (beta, kind, n), p in D.items(): addB(out, beta, kind, n, p)
    return out

def diffB(D, d, axis):
    """One Cartesian derivative of a degree-d object (d any integer, parity decides the form)."""
    out = {}
    for (beta, kind, n), p in D.items():
        if d % 2 == 0:
            rad = (ONE - Z * fq(d + 2 * beta)) * p + 2 * Z * OM * p.derivative(); ang = p
        else:
            rad = -fq(d - 1 + 2 * beta) * p + 2 * OM * p.derivative()
            if n:
                ang, rem = divmod(p, Z); assert not rem, ('origin pole', d, beta, kind, n)
            else: ang = fmpq_poly([])
        rk = 'c' if axis == 'x' else 's'
        for kk, nn, factor in trigprod(rk, 1, kind, n): addB(out, beta, kk, nn, rad * fq(factor))
        if n:
            ak = 's' if axis == 'x' else 'c'; dk = 's' if kind == 'c' else 'c'
            sign = (-1 if kind == 'c' else 1) * (-1 if axis == 'x' else 1)
            for kk, nn, factor in trigprod(ak, 1, dk, n): addB(out, beta, kk, nn, ang * fq(sign * n * factor))
    return out

def laplacian(D, d):
    """Delta of a degree-d (even) object, returned as degree d+2 object."""
    assert d % 2 == 0
    dx = diffB(D, d, 'x'); dy = diffB(D, d, 'y')
    return normalize(plusB(diffB(dx, d + 1, 'x'), diffB(dy, d + 1, 'y')))

def pair(D1, d1, D2, d2):
    """int D1 D2 dX / pi for two even-degree objects (exact rational), or None if a diagonal exponent is <= -1.
    (This requires both objects to have the same angular parity structure; cross modes vanish.)
    Products are grouped by the exponent b and integrated once per group (the per-pair summation of 10^4-digit
    rationals was the bottleneck; same exact result)."""
    assert d1 % 2 == 0 and d2 % 2 == 0
    idx = {}
    for (beta, kind, n), p in D2.items(): idx.setdefault((kind, n), []).append((beta, p))
    groups = {}; cache = {}
    for (beta, kind, n), p in D1.items():
        q1, p1 = endpoint(p)
        for beta2, p2raw in idx.get((kind, n), []):
            q2, p2 = endpoint(p2raw)
            b = Q(d1 + d2, 2) - 3 + beta + beta2 + q1 + q2
            if b <= -1: return None
            factor = Q(1, 2) * (2 if (kind == 'c' and n == 0) else 1)
            groups[b] = groups.get(b, fmpq_poly([])) + p1 * p2 * Z * fq(factor)
    total = fmpq(0)
    for b, v in groups.items(): total += integral(v, b, cache)
    return total

def normB(D, d, a_shift=Q(0), t_power=0):
    """||D^d-object||_2^2 / pi (exact rational) with weight (1-t)^a_shift t^t_power; None if divergent.
    D is a dict component -> dict (for tensor components) or a single dict. Multiplicity given by caller.
    Products are grouped by the exponent b and integrated once per group (same exact result, far fewer big-rational sums)."""
    cache = {}; groups = {}
    comps = D if isinstance(D, list) else [(1, D)]
    for mult, comp in comps:
        modes = {}
        for (beta, kind, n), p in comp.items():
            q, p2 = endpoint(p); modes.setdefault((kind, n), []).append((beta, q, p2))
        for (kind, n), rows in modes.items():
            for i, (beta, q, p) in enumerate(rows):
                for j in range(i, len(rows)):
                    beta2, q2, p2 = rows[j]
                    b = Q(d - 3) + beta + beta2 + q + q2 + a_shift
                    if b <= -1: return None
                    factor = Q(mult) * (2 if (kind == 'c' and n == 0) else 1) * (1 if i == j else 2) * Q(1, 2)
                    v = p * p2 * fq(factor)
                    if d % 2 == 0: v *= Z
                    if t_power: v *= Z ** t_power
                    groups[b] = groups.get(b, fmpq_poly([])) + v
    total = fmpq(0)
    for b, v in groups.items(): total += integral(v, b, cache)
    return total

def grad_sq(Dm2):
    """||grad phi||_2^2/pi for a degree -2 object."""
    gx = diffB(Dm2, -2, 'x'); gy = diffB(Dm2, -2, 'y')
    return normB([(1, gx), (1, gy)], -1)

# ------------------------------------------------------------------ Galerkin potential per mode
def basis_mode(n, betas, kmax):
    """Potentials psi = r^3 (1-t)^b t^k sin(n theta) as degree -2 objects: r (1-t)^(-1) (1-t)^b t^(k+1).
    Origin regularity: psi = O(r^n) requires 3 + 2k >= n."""
    kmin = -1 if n == 1 else max(0, (n - 3 + 1) // 2)      # mode 1 potentials behave like r at the origin: allow t^0
    out = []
    for b in betas:
        for k in range(kmin, kmax + 1):
            D = {}
            addB(D, b, 's', n, Z ** (k + 1))          # r^3 (1-t)^b t^k = r (1-t)^(-1) (1-t)^b t^(k+1)
            out.append(((str(b), k), normalize(D)))
    return out

def mode_component(F, n):
    return {key: p for key, p in F.items() if key[1] == 's' and key[2] == n}

def rationalize(x, bits=256):
    """Round an arb to a dyadic rational with the given number of fractional bits: exact midpoint extraction
    (mantissa, exponent) followed by rounding (any rational is admissible; rounding only affects the remainder)."""
    man, exp = x.mid().man_exp()
    q = Q(int(man)) * (Q(2) ** int(exp))
    return Q(round(q * 2 ** bits), 2 ** bits)

def classes_of(Fn):
    """Branch exponent classes (minimal beta of each class) present in a mode component of F."""
    return sorted({beta for (beta, kind, n) in Fn})

def solve_exact(G, bvec, bits=400, prec=2500):
    """Solve the Galerkin system: ball arithmetic at high precision (fast), exact rational fallback; the solution is
    rounded to dyadic rationals with the given number of fractional bits (any rounding is absorbed by the exact bounds)."""
    from flint import fmpq_mat
    m = len(bvec)
    old = ctx.prec; ctx.prec = prec
    try:
        Ga = arb_mat([[aq(Q(int(G[i][j].p), int(G[i][j].q))) for j in range(m)] for i in range(m)])
        ba = arb_mat([[aq(Q(int(bvec[i].p), int(bvec[i].q)))] for i in range(m)])
        ca = Ga.solve(ba)
        out = [rationalize(ca[i, 0], bits) for i in range(m)]
        ctx.prec = old
        return out
    except Exception:
        ctx.prec = old
    Gq = fmpq_mat(m, m, [G[i][j] for i in range(m) for j in range(m)]); bq = fmpq_mat(m, 1, list(bvec))
    cq = Gq.solve(bq)
    out = []
    for i in range(m):
        v = Q(int(cq[i, 0].p), int(cq[i, 0].q))
        out.append(Q(round(v * 2 ** bits), 2 ** bits))
    return out

def gram_and_load(Fn, basis):
    laps = []
    for lab, psi in basis:
        lap = laplacian(psi, -2); assert len(lap) == 1
        (bl, kl, nl), P = next(iter(lap.items())); laps.append((bl, [fq(v) for v in P.coeffs()]))
    keys = []
    for lab, psi in basis:
        assert len(psi) == 1
        (bk, kk, nk), P = next(iter(psi.items())); co = P.coeffs()
        shift = next(i for i, v in enumerate(co) if v); assert all(v == 0 for v in co[:shift]) and len(co) == shift + 1
        keys.append((bk, shift, fq(co[shift])))
    cache = {}
    def beta_table(b, need):
        if b not in cache: cache[b] = [fq(1 / (b + 1))]
        bet = cache[b]
        while len(bet) < need:
            k = len(bet); bet.append(bet[-1] * k / fq(b + k + 1))
        return bet
    m = len(basis); G = [[None] * m for _ in range(m)]; bvec = [None] * m
    for i, (lab, psi) in enumerate(basis):
        bi = pair(Fn, 0, psi, -2); assert bi is not None, ('F-psi pairing divergent', lab)
        bvec[i] = bi
        bi_, si, ci = keys[i]
        for j in range(i, m):
            bj, Pj = laps[j]
            b = Q(-1) - 3 + bi_ + bj
            bet = beta_table(b, si + 1 + len(Pj) + 1)
            val = sum((Pj[k] * bet[si + 1 + k] for k in range(len(Pj)) if Pj[k]), fmpq(0)) * ci / 2
            G[i][j] = G[j][i] = -val
    return G, bvec

def particular_recursion(Qred, beta, n, prec=3000, rbits=800):
    """Approximate polynomial P_phi = t S_p (list of dyadic fmpq, powers t^0, t^1, ...) with M_n^(beta) S_p = Qred up to
    a remainder of degree <= j_low + 1 (plus a tiny rounding tail), by top-down recursion in ball arithmetic at prec
    bits, rounded to rbits fractional bits. j_low = -1 for n = 1 (phi ~ r at the origin), (n-3)/2 for n >= 3.
    M_n(t^k) = [(2k+3)^2 - n^2] t^k - 8(k+2)(k+beta) t^(k+1) + 4(k+beta)(k+beta+1) t^(k+2)  (phi = r^3 (1-t)^beta S sin n theta).
    Any choice of S_p gives rigorous bounds; accuracy only affects the size of the exact remainder."""
    q = Qred.coeffs(); D = len(q) - 1
    j_low = -1 if n == 1 else (n - 3) // 2
    if D - 2 < j_low: return None
    old = ctx.prec; ctx.prec = prec
    bq = aq(beta); s = {}
    qa = [aq(Q(int(v.p), int(v.q))) for v in q]
    for j in range(D, j_low + 1, -1):
        acc = qa[j] if j < len(qa) else arb(0)
        acc -= ((2 * j + 3) ** 2 - n * n) * s.get(j, arb(0))
        acc += 8 * (j + 1) * (j - 1 + bq) * s.get(j - 1, arb(0))
        s[j - 2] = acc / (4 * (j - 2 + bq) * (j - 1 + bq))
    out = [fq(rationalize(s.get(j, arb(0)), rbits)) if j in s else fmpq(0) for j in range(-1, D - 1)]
    ctx.prec = old
    return out

def galerkin_mode_classwise(Fn, n, delta, kmax, log=print, bits=400, small=20, rbits=800):
    """Exact potential for one mode: per F-branch class, exact top-down recursion for the polynomial part plus a small
    two-class Galerkin (class exponent and the integer class r^-n) for the low-degree remainder; then rigorous bounds."""
    start = time.monotonic()
    phi = {}; nbasis = 0; nclasses = 0; recursion_degrees = []
    for beta_c in classes_of(Fn):
        Fc = {key: p for key, p in Fn.items() if key[0] == beta_c}
        assert len(Fc) == 1
        (bc, kc, nc), Pfull = next(iter(Fc.items()))
        qz, Pred = endpoint(Pfull)                     # Pfull = (1-t)^qz Pred, Pred(1) != 0
        b = beta_c + qz                                # actual decay class of this part of F; b > 3/2 for admissible F
        assert b > Q(3, 2), ('class not decaying enough for a square-integrable gradient', b)
        src = {(b, 's', n): Pred}                      # same function as Fc, written in class b
        phi_c = {}
        if Pred.degree() > small:
            Sp = particular_recursion(-Pred, b, n, rbits=rbits)   # M_n S_p = -Qred up to a low-degree remainder
            if Sp:
                phi_p = {}
                addB(phi_p, b, 's', n, fmpq_poly(Sp))          # r^3 (1-t)^b S_p = r (1-t)^(-1) (1-t)^b (t S_p); list = t S_p
                lap = laplacian(phi_p, -2)
                rem = normalize(plusB(src, lap))               # Qred - M_n S_p: low-degree part plus a tiny rounding tail
                assert set(k[0] for k in rem) <= {b} or not rem, rem.keys()
                remdeg = max((p.degree() for p in rem.values()), default=-1)
                recursion_degrees.append((str(b), Pred.degree(), remdeg))
                phi_c = phi_p; src = rem
        if src:
            kk = (-1 if n == 1 else (n - 3) // 2) + small       # 'small' monomials above the minimal admissible degree
            basis = basis_mode(n, [b, Q(n + 3, 2)], kk)
            G, bvec = gram_and_load(src, basis)
            coeffs = solve_exact(G, bvec, bits)
            for c, (lab, psi) in zip(coeffs, basis):
                if c: phi_c = plusB(phi_c, scale(psi, c))
            nbasis += len(basis)
        phi = plusB(phi, phi_c); nclasses += 1
    phi = normalize(phi)
    num = pair(Fn, 0, phi, -2) if phi else fmpq(0)                  # <F, phi>/pi
    den = grad_sq(phi) if phi else fmpq(0)                           # ||grad phi||^2/pi
    lap = laplacian(phi, -2) if phi else {}
    g = normalize(plusB(Fn, lap))
    rg2 = normB(g, 0, Q(-1), 1)
    pg = pair(phi, -2, g, 0) if phi else fmpq(0)
    lb = max((num * num / den) if den > 0 else fmpq(0), 2 * num - den, fmpq(0))
    res = {'n': n, 'basis_size': nbasis, 'classes': nclasses, 'kmax': kmax, 'method': 'classwise exact recursion + two-class Galerkin',
           'recursion': recursion_degrees,
           'F_phi_over_pi': str(num), 'grad_phi_sq_over_pi': str(den), 'phi_g_over_pi': str(pg) if pg is not None else None,
           'rg_sq_over_pi': str(rg2) if rg2 is not None else None, 'elapsed': time.monotonic() - start, 'lb_sq_over_pi': str(lb)}
    if rg2 is None or pg is None:
        res['status'] = 'UB_UNAVAILABLE'; return res, lb, None
    res['status'] = 'OK'; res['ub_sq_identity_over_pi'] = str(den + 2 * pg + rg2)
    log(f'  mode {n}: LB^2/pi={float(lb):.10e} UB^2/pi={float(den+2*pg+rg2):.10e} (|grad phi|^2={float(den):.6e}, |rg|^2={float(rg2):.3e}, 2<phi,g>={float(2*pg):.3e}) classes {nclasses} galerkin basis {nbasis} {time.monotonic()-start:.1f}s')
    return res, lb, (den, rg2, pg)

def galerkin_mode(Fn, n, delta, ells, kmax, prec=3000, log=print, int_branch=True):
    start = time.monotonic()
    # branch exponents b = ell delta/2 + q', q' minimal with b > 3/2 (so that grad psi is square integrable)
    betas = []
    for ell in ells:
        b = Q(ell) * delta / 2
        while b <= Q(3, 2): b += 1
        betas.append(b)
    if int_branch: betas.append(Q(n + 3, 2))
    basis = basis_mode(n, betas, kmax)
    m = len(basis)
    # exact Gram <grad psi_i, grad psi_j>/pi = -<psi_i, Delta psi_j>/pi (integration by parts; boundary terms vanish
    # because beta_i + beta_j > 3) and load <F, psi_i>/pi, all single Beta sums.
    laps = []
    for lab, psi in basis:
        lap = laplacian(psi, -2); assert len(lap) == 1
        (bl, kl, nl), P = next(iter(lap.items())); laps.append((bl, [fq(v) for v in P.coeffs()]))
    keys = []
    for lab, psi in basis:
        assert len(psi) == 1
        (bk, kk, nk), P = next(iter(psi.items())); co = P.coeffs()
        shift = next(i for i, v in enumerate(co) if v); assert all(v == 0 for v in co[:shift]) and len(co) == shift + 1
        keys.append((bk, shift, fq(co[shift])))
    cache = {}
    def beta_table(b, need):
        if b not in cache: cache[b] = [fq(1 / (b + 1))]
        bet = cache[b]
        while len(bet) < need:
            k = len(bet); bet.append(bet[-1] * k / fq(b + k + 1))
        return bet
    G = [[None] * m for _ in range(m)]; bvec = [None] * m
    for i, (lab, psi) in enumerate(basis):
        bi = pair(Fn, 0, psi, -2); assert bi is not None, ('F-psi pairing divergent', lab)
        bvec[i] = bi
        bi_, si, ci = keys[i]
        for j in range(i, m):
            bj, Pj = laps[j]
            b = Q(-2 + 0, 2) - 3 + bi_ + bj                      # (d1+d2)/2 - 3 with d1 = -2, d2 = 0
            bet = beta_table(b, si + 1 + len(Pj) + 1)
            # pair(psi_i, -2, Delta psi_j, 0) = (1/2) int t^(si+1) (1-t)^b sum_m Pj[m] t^m dt  (the extra t is r^2)
            val = sum((Pj[k] * bet[si + 1 + k] for k in range(len(Pj)) if Pj[k]), fmpq(0)) * ci / 2
            G[i][j] = G[j][i] = -val
    log(f'  mode {n}: basis {m}, Gram built {time.monotonic()-start:.1f}s')
    # high-precision solve
    old = ctx.prec; ctx.prec = prec
    Ga = arb_mat([[aq(G[i][j]) for j in range(m)] for i in range(m)]); ba = arb_mat([[aq(bvec[i])] for i in range(m)])
    try:
        ca = Ga.solve(ba)
        coeffs = [rationalize(ca[i, 0], 400) for i in range(m)]
    except Exception as ex:
        log(f'  mode {n}: solve failed ({ex}); using zero potential'); coeffs = [Q(0)] * m
    ctx.prec = old
    # exact evaluation
    phi = {}
    for c, (lab, psi) in zip(coeffs, basis):
        if c: phi = plusB(phi, scale(psi, c))
    phi = normalize(phi)
    num = sum((fq(c) * bvec[i] for i, c in enumerate(coeffs)), fmpq(0))             # <F, phi>/pi
    den = fmpq(0)
    for i, ci in enumerate(coeffs):
        if not ci: continue
        for j, cj in enumerate(coeffs):
            if cj: den += fq(ci) * fq(cj) * G[i][j]                                  # ||grad phi||^2/pi
    lap = laplacian(phi, -2) if phi else {}
    g = normalize(plusB(Fn, lap))                                                     # remainder F + Delta phi
    rg2 = normB(g, 0, Q(-1), 1)                                                       # ||r g||^2/pi
    pg = pair(phi, -2, g, 0) if phi else fmpq(0)                                      # <phi, g>/pi
    res = {'n': n, 'basis_size': m, 'ells': list(ells), 'kmax': kmax, 'int_branch': int_branch,
           'F_phi_over_pi': str(num), 'grad_phi_sq_over_pi': str(den), 'phi_g_over_pi': str(pg) if pg is not None else None,
           'rg_sq_over_pi': str(rg2) if rg2 is not None else None, 'elapsed': time.monotonic() - start}
    # bounds on ||F_n||_H^2 / pi
    lb = (num * num / den) if den > 0 else fmpq(0)
    lb2 = 2 * num - den
    lb = max(lb, lb2, fmpq(0))
    if rg2 is None or pg is None:
        res['status'] = 'UB_UNAVAILABLE'; res['lb_sq_over_pi'] = str(lb); return res, lb, None
    ub_sq = den + 2 * pg + rg2
    # triangle alternative: (sqrt(den) + sqrt(rg2))^2 (evaluated in arb later); keep both
    res.update({'status': 'OK', 'lb_sq_over_pi': str(lb), 'ub_sq_identity_over_pi': str(ub_sq)})
    log(f'  mode {n}: LB^2/pi={float(lb):.6e} UB^2/pi={float(ub_sq):.6e} (|grad phi|^2={float(den):.6e}, |rg|^2={float(rg2):.6e}, 2<phi,g>={float(2*pg):.3e}) {time.monotonic()-start:.1f}s')
    return res, lb, (den, rg2, pg)

def pair_odd(D1, D2):
    """int D1 D2 dX / pi for two odd-degree (-1) objects (gradient components); exact rational."""
    idx = {}
    for (beta, kind, n), p in D2.items(): idx.setdefault((kind, n), []).append((beta, p))
    total = fmpq(0); cache = {}
    for (beta, kind, n), p in D1.items():
        q1, p1 = endpoint(p)
        for beta2, p2raw in idx.get((kind, n), []):
            q2, p2 = endpoint(p2raw)
            b = Q(-1 - 3) + beta + beta2 + q1 + q2
            assert b > -1, ('divergent gradient pairing', beta, beta2, q1, q2)
            factor = Q(1, 2) * (2 if (kind == 'c' and n == 0) else 1)
            total += integral(p1 * p2, b, cache) * fq(factor)
    return total

def split_round(Fn, fbits=800):
    """Fn = F_round + F_err per key, keeping the exact endpoint factor (1-t)^q: P = (1-t)^q Pred, Pred rounded to fbits
    fractional bits. Returns (F_round, err_terms) with err_terms = [(beta + q, n, [exact tiny error coefficients])]."""
    Fr = {}; errs = []
    for (beta, kind, n), P in Fn.items():
        q, Pred = endpoint(P)
        rc = [fq(Q(round(Q(int(v.p), int(v.q)) * 2 ** fbits), 2 ** fbits)) for v in Pred.coeffs()]
        Pr = fmpq_poly(rc)
        e = [a - b for a, b in zip(Pred.coeffs(), rc)]
        if Pr: Fr[(beta, kind, n)] = Pr * OM ** q
        if any(e): errs.append((beta + q, n, e))
    return Fr, errs

def err_hardy_bound(errs):
    """Upper bound (arb) of ||r F_err||_2 >= ||F_err||_H by the triangle inequality over keys and monomials:
    ||r (1-t)^b t^k sin(n theta)||_2^2 = (pi/2) B(2k+3, 2b-3) (exact rational Beta value; needs b > 3/2)."""
    total = arb(0)
    for b, n, e in errs:
        bb = 2 * b - 4                                    # (1-t) exponent of the squared integrand: 2b - 4 (> -1)
        assert bb > -1
        bet = [fq(1 / (bb + 1))]
        for k in range(len(e) + 2):
            m = len(bet); bet.append(bet[-1] * m / fq(bb + m + 1))
        for k, ek in enumerate(e):
            if ek: total += abs(aq(Q(int(ek.p), int(ek.q)))) * (arb.pi() / 2 * aq(Q(str(bet[2 + k])))).sqrt()
    return total

def hminus1(F_ell, delta, kmax=30, prec=3000, log=print, modes=None, ell_filter=None, fbits=800, small=20, max_mode=None):
    """F_ell: degree-0 residual dict with ell keys (from e2norms). Returns record with LB, UB for ||F||_H.
    Per mode n: F_n = F_round + F_err (exact split); bounds for F_round from the Galerkin potential; the parity Hardy
    inequality ||F_err||_H <= ||r F_err||_2 (A2-THEOREM) transfers them to F_n:
    ||F_n||_H in [LB_round - e_n, UB_round + e_n], e_n = ||r F_err||_2 (exact Beta integral)."""
    F = normalize(from_ell(F_ell, delta))
    ns = sorted({n for (b, k, n) in F})
    assert all(k == 's' and n % 2 == 1 for (b, k, n) in F), 'F must have only odd sine modes'
    if modes is not None: ns = [n for n in ns if n in modes]
    tail_modes = []
    if max_mode is not None:
        tail_modes = [n for n in ns if n > max_mode]; ns = [n for n in ns if n <= max_mode]
    LBsq = arb(0); UBsq = arb(0); rows = []; ok = True
    old = ctx.prec
    tail = None
    if tail_modes:
        # modes above max_mode: Hdot^-1 norm bounded by the parity Hardy inequality ||G||_H <= ||r G||_2 (exact Beta
        # integral of the exact mode-filtered residual); lower bound 0.
        ctx.prec = 512
        Ft = {key: p for key, p in F.items() if key[2] in tail_modes}
        Ftr, terrs = split_round(Ft, fbits)
        tsq = normB(Ftr, 0, Q(-1), 1) if Ftr else fmpq(0)
        if tsq is None: ok = False; tail = {'modes': tail_modes, 'status': 'rF divergent'}
        else:
            tail_ub = (arb.pi() * aq(Q(str(tsq)))).sqrt() + err_hardy_bound(terrs); UBsq += tail_ub ** 2
            tail = {'modes': tail_modes, 'rF_norm_UB': str(tail_ub.upper()), 'method': 'Hardy bound ||F_tail||_H <= ||r F_tail||_2 (exact)'}
            log(f'  tail modes {tail_modes[0]}..{tail_modes[-1]} ({len(tail_modes)}): ||F_tail||_H <= ||r F_tail||_2 = {tail_ub.upper()}')
        ctx.prec = old
    for n in ns:
        Fn = mode_component(F, n)
        Fr, errs = split_round(Fn, fbits)
        res, lb, extra = galerkin_mode_classwise(Fr, n, delta, kmax, log, small=small)
        ctx.prec = 512
        e_n = err_hardy_bound(errs)                                   # >= ||F_err||_H (parity Hardy, coefficient-wise)
        res['round_bits'] = fbits; res['err_Hardy_norm'] = str(e_n.upper()) if e_n is not None else 'INF'
        lbn = (arb.pi() * aq(Q(str(lb)))).sqrt()
        if extra is None or e_n is None:
            ok = False; rows.append(res); LBsq += (lbn - e_n) ** 2 if e_n is not None and lbn > e_n else arb(0); ctx.prec = old; continue
        den, rg2, pg = extra
        ubn1 = (arb.pi() * aq(Q(str(den + 2 * pg + rg2)))).sqrt()
        ubn2 = (arb.pi() * aq(Q(str(den)))).sqrt() + (arb.pi() * aq(Q(str(rg2)))).sqrt()
        ubn = ubn1 if ubn1.upper() < ubn2.upper() else ubn2
        lo_n = lbn - e_n; lo_n = lo_n if lo_n.lower() > 0 else arb(0)
        hi_n = ubn + e_n
        res['mode_norm_LB'] = str(lo_n.lower()); res['mode_norm_UB'] = str(hi_n.upper())
        LBsq += lo_n ** 2; UBsq += hi_n ** 2
        rows.append(res)
        log(f'  mode {n}: ||F_n||_H in [{lo_n.lower()}, {hi_n.upper()}] (rounding error term {e_n.upper()})')
        ctx.prec = old
    ctx.prec = 512
    out = {'modes': ns, 'kmax': kmax, 'small': small, 'max_mode': max_mode, 'tail': tail, 'rows': rows, 'method': 'per mode: exact split F = F_round + F_err; class-wise exact recursion + two-class Galerkin potential for F_round; duality LB and identity/Hardy UB; Hardy bound for F_err'}
    out['H_lower'] = str(LBsq.sqrt().lower())
    out['H_upper'] = str(UBsq.sqrt().upper()) if ok else None
    ctx.prec = old
    return out

def load_F(path, log):
    """Return (F_ell, delta, canonical_sha, source_sha) from an exact reference (regenerated) or an *_Fpoly.json record."""
    raw = json.loads(Path(path).read_text())
    if 'polynomials' in raw:
        delta = Q(raw['delta'])
        F_ell = {(r['ell'], r['kind'], r['mode']): fmpq_poly([fmpq(v) for v in r['coeff']]) for r in raw['polynomials']['0,0']}
        return F_ell, delta, raw['canonical_sha256'], None
    c, A, src_sha, can_sha, meta = E.load_reference(path)
    cached = Path(path).resolve().parent.parent.parent / 'certification' / 'results' / (Path(path).stem + '_Fpoly_cache.json')
    if cached.exists():
        raw = json.loads(cached.read_text())
        if raw.get('canonical_sha256') == can_sha:
            log(f'loaded cached F record {cached}')
            F_ell = {(r['ell'], r['kind'], r['mode']): fmpq_poly([fmpq(v) for v in r['coeff']]) for r in raw['polynomials']['0,0']}
            return F_ell, 1 - 1 / c, can_sha, src_sha
    log(f'regenerating F from exact source {meta}')
    D, fields = E.residual_polynomials(A, c, 0, log)
    try:
        poly = {'0,0': [{'ell': ell, 'kind': kind, 'mode': n, 'coeff': [str(v) for v in p.coeffs()]} for (ell, kind, n), p in sorted(D[0, 0].items())]}
        cached.write_text(json.dumps({'canonical_sha256': can_sha, 'delta': str(1 - 1 / c), 'polynomials': poly}, separators=(',', ':')) + '\n')
        log(f'cached F record {cached} ({cached.stat().st_size/1e6:.1f} MB)')
    except Exception as ex: log(f'cache write failed: {ex}')
    return D[0, 0], 1 - 1 / c, can_sha, src_sha

def run(name, path, outdir, kmax=30, prec=3000, small=20, max_mode=None):
    outdir = Path(outdir); logf = open(outdir / f'{name}_hminus1.log', 'a')
    def log(*a):
        msg = ' '.join(str(x) for x in a); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    ctx.prec = 512; t0 = time.monotonic()
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {name}: Hdot^-1 enclosure, kmax={kmax}, input {path}')
    F_ell, delta, can_sha, src_sha = load_F(path, log)
    log(f'F components {len(F_ell)} ({time.monotonic()-t0:.1f}s)')
    out = hminus1(F_ell, delta, kmax, prec, log, small=small, max_mode=max_mode)
    out.update({'name': name, 'canonical_sha256': can_sha, 'source_sha256': src_sha, 'input': str(path),
                'input_sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'elapsed_seconds': time.monotonic() - t0,
                'utc': datetime.now(timezone.utc).isoformat(timespec='seconds')})
    (outdir / f'{name}_hminus1.json').write_text(json.dumps(out, indent=1) + '\n')
    log(f"RESULT {name}: ||F||_H in [{out['H_lower']}, {out['H_upper']}] ({time.monotonic()-t0:.1f}s)")
    return out

def totals_from_rows(rows, tail=None):
    ctx.prec = 512
    LBsq = arb(0); UBsq = arb(0); ok = True
    if tail:
        if 'rF_norm_UB' in tail: UBsq += arb(tail['rF_norm_UB']) ** 2
        else: ok = False
    for r in rows:
        if 'mode_norm_LB' not in r: ok = False; continue
        LBsq += arb(r['mode_norm_LB']) ** 2; UBsq += arb(r['mode_norm_UB']) ** 2
    return str(LBsq.sqrt().lower()), (str(UBsq.sqrt().upper()) if ok else None)

def rerun_modes(name, path, outdir, modes, small, kmax=24, prec=3000):
    """Recompute the listed modes with a larger Galerkin degree range and merge them into <name>_hminus1.json."""
    outdir = Path(outdir); logf = open(outdir / f'{name}_hminus1.log', 'a')
    def log(*a):
        msg = ' '.join(str(x) for x in a); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    ctx.prec = 512; t0 = time.monotonic()
    rec = json.loads((outdir / f'{name}_hminus1.json').read_text())
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {name}: rerun of modes {modes} with small={small}')
    F_ell, delta, can_sha, src_sha = load_F(path, log)
    assert can_sha == rec['canonical_sha256']
    out = hminus1(F_ell, delta, kmax, prec, log, modes=modes, small=small)
    newrows = {r['n']: r for r in out['rows']}
    rec['rows'] = [newrows.get(r['n'], r) for r in rec['rows']]
    rec['H_lower'], rec['H_upper'] = totals_from_rows(rec['rows'], rec.get('tail'))
    rec.setdefault('reruns', []).append({'modes': modes, 'small': small, 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds')})
    rec['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (outdir / f'{name}_hminus1.json').write_text(json.dumps(rec, indent=1) + '\n')
    log(f"RESULT after rerun {name}: ||F||_H in [{rec['H_lower']}, {rec['H_upper']}] ({time.monotonic()-t0:.1f}s)")

if __name__ == '__main__':
    if sys.argv[1] == 'rerun':
        name, path, outdir = sys.argv[2:5]; modes = [int(x) for x in sys.argv[5].split(',')]; small = int(sys.argv[6])
        rerun_modes(name, path, outdir, modes, small)
    else:
        name, path, outdir = sys.argv[1:4]
        kmax = int(sys.argv[4]) if len(sys.argv) > 4 else 30
        small = int(sys.argv[5]) if len(sys.argv) > 5 else 20
        max_mode = int(sys.argv[6]) if len(sys.argv) > 6 else None
        run(name, path, outdir, kmax, small=small, max_mode=max_mode)
