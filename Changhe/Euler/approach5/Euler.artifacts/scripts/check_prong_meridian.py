"""Prong-slope filling of the punctured cat-map bundle (a coordinator note, section 3).

Question: for the linear map A = [[2,1],[1,1]] on T^2 = R^2/Z^2 with its fixed point 0 removed, let x0 lie on an
eigen-ray of A at 0 (near 0), and let phi be the automorphism of pi_1(T^2 - 0, x0) given by g -> rho . A(g) . rho^-1,
where rho is the segment of that ray from x0 to A x0. Filling the punctured-torus bundle along the prong slope kills
the stable letter, so the filled group is <a, b | a = phi(a), b = phi(b)>. Is it trivial?

Method. pi_1(T^2 - 0, x0) is free on the classes dual to the two arcs e_v = {0} x [0,1] and e_h = [0,1] x {0}
(their complement in T^2 is an open square). A path in R^2 - Z^2 is recorded by its ordered crossings of the lines
x in Z (letter v, exponent = sign of dx) and y in Z (letter h, sign of dy). Generators: a = segment x0 -> x0 + e1,
b = segment x0 -> x0 + e2. phi(a), phi(b) are the crossing words of A(a), A(b); rho stays in one open unit square
and contributes nothing. Exact arithmetic in Q(sqrt 5).
Pass criteria: (1) abelianization of phi is A; (2) the filled group has order 1 (coset enumeration, a certificate);
(3) the boundary loop d of the puncture, based at x0 (crossing word of a small counterclockwise square around 0), is
fixed exactly by phi, so the prong curve t commutes with d and is a peripheral element; (4) control: the neighbouring
slopes t d^k (k = +-1, +-2) give the fillings <a, b | g = d^k phi(g) d^-k>; for k = +-1 these are +-1 surgeries on the
figure-eight knot (Brieskorn sphere Sigma(2,3,7), whose group maps onto the Hurwitz group PSL(2,7)), so they must admit
nontrivial homomorphisms to PSL(2,7). All fillings along slopes t d^k are homology spheres, so abelianization alone
cannot separate them; the PSL(2,7) count does.

Revision 2026-11-02 22:59Z. The first version (kept as check_prong_meridian_v1_float.py with its log) converted crossing
times to floats for ordering and used a 1e-12 tolerance for lattice-point avoidance, so it was not an exact
certificate (auditor A247). This version does all crossing arithmetic exactly in Q(sqrt 5): an element is a pair of
Fractions (r, s) meaning r + s sqrt 5; signs are decided by comparing r^2 with 5 s^2; floors are found by exact
comparison; lattice-point avoidance is an exact test (irrational part nonzero, or rational part not an integer).
No floating point is used anywhere in the word computation.
"""
import sympy as sp
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics import Permutation

from fractions import Fraction as Fr


class Q5:
    """r + s sqrt(5) with r, s rational; exact field operations and exact sign."""
    def __init__(self, r, s=0):
        self.r, self.s = Fr(r), Fr(s)

    def __add__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.r + o.r, self.s + o.s)
    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.r, -self.s)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Q5) else Q5(o)))

    def __rsub__(self, o):
        return Q5(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.r * o.r + 5 * self.s * o.s, self.r * o.s + self.s * o.r)
    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        n = o.r * o.r - 5 * o.s * o.s
        assert n != 0
        return self * Q5(o.r / n, -o.s / n)

    def sign(self):
        r, s = self.r, self.s
        if r >= 0 and s >= 0:
            return 0 if (r == 0 and s == 0) else 1
        if r <= 0 and s <= 0:
            return -1
        # opposite signs: compare r^2 with 5 s^2 (never equal, sqrt 5 irrational)
        return (1 if r > 0 else -1) if r * r > 5 * s * s else (1 if s > 0 else -1)

    def __lt__(self, o):
        return (self - o).sign() < 0

    def floor(self):
        n = int(self.r + self.s * Fr(2236067977, 10 ** 9))   # a guess, corrected exactly below
        while (self - n).sign() < 0:
            n -= 1
        while (self - (n + 1)).sign() >= 0:
            n += 1
        return n

    def is_integer(self):
        return self.s == 0 and self.r.denominator == 1

    def __eq__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return self.r == o.r and self.s == o.s

    def __repr__(self):
        return f'({self.r} + {self.s} sqrt5)'


def vec(x, y):
    return (x if isinstance(x, Q5) else Q5(x), y if isinstance(y, Q5) else Q5(y))


def vadd(P, Q):
    return (P[0] + Q[0], P[1] + Q[1])


def vscale(P, t):
    return (P[0] * t, P[1] * t)


def Amul(P):
    return (2 * P[0] + P[1], P[0] + P[1])


K = Q5(Fr(3, 2), Fr(1, 2))
es = vec(1, Q5(Fr(-1, 2), Fr(-1, 2)))      # eigenvalue 1/K
eu = vec(1, Q5(Fr(-1, 2), Fr(1, 2)))       # eigenvalue K
assert Amul(es) == vscale(es, Q5(1) / K) and Amul(eu) == vscale(eu, K)
# cross-check with sympy symbolic eigenvectors
s5 = sp.sqrt(5)
assert sp.simplify(sp.Matrix([[2, 1], [1, 1]]) * sp.Matrix([1, -(1 + s5) / 2]) - sp.Matrix([1, -(1 + s5) / 2]) * 2 / (3 + s5)) == sp.zeros(2, 1)


def crossing_word(P, Q):
    """Ordered crossings of x in Z ('v') and y in Z ('h') along the segment P -> Q, exactly in Q(sqrt 5)."""
    ev = []
    for i, name in ((0, 'v'), (1, 'h')):
        p, q = P[i], Q[i]
        if (q - p).sign() == 0:
            continue
        lo, hi = (p, q) if p < q else (q, p)
        for k in range(lo.floor(), hi.floor() + 2):
            t = (Q5(k) - p) / (q - p)
            if t.sign() > 0 and (t - 1).sign() < 0:
                other = P[1 - i] + t * (Q[1 - i] - P[1 - i])
                assert not other.is_integer(), 'hits a lattice point'
                ev.append((t, name, (q - p).sign()))
    # exact ordering; equal times would mean a lattice point, excluded above
    for x in range(len(ev)):
        for y in range(x + 1, len(ev)):
            assert not (ev[x][0] == ev[y][0])
    ev.sort(key=lambda e: _Key(e[0]))
    return [(n, e) for _, n, e in ev]


class _Key:
    def __init__(self, t):
        self.t = t

    def __lt__(self, o):
        return self.t < o.t


F, a, b = free_group('a b')
letter = {'v': a, 'h': b}


def word(cw):
    w = F.identity
    for n, e in cw:
        w = w * letter[n] ** e
    return w


def prong_phi(x0):
    Ax0 = Amul(x0)
    pa = word(crossing_word(Ax0, vadd(Ax0, Amul(vec(1, 0)))))
    pb = word(crossing_word(Ax0, vadd(Ax0, Amul(vec(0, 1)))))
    ga = word(crossing_word(x0, vadd(x0, vec(1, 0))))
    gb = word(crossing_word(x0, vadd(x0, vec(0, 1))))
    assert ga == a and gb == b, (ga, gb)
    # the connecting segment rho from x0 to A x0 (along the eigen-ray) must cross no grid line
    assert crossing_word(x0, Ax0) == [], 'rho crosses a grid line'
    return pa, pb


def abel(w):
    va = sum(e for g, e in w.array_form if str(g) == 'a')
    vb = sum(e for g, e in w.array_form if str(g) == 'b')
    return (va, vb)


# PSL(2,7) acting on P^1(F_7) = {0..6, inf=7}
def mob(f):
    return Permutation([f(x) for x in range(8)])


inv7 = {x: pow(x, 5, 7) for x in range(1, 7)}
T = mob(lambda x: 7 if x == 7 else (x + 1) % 7)
Sg = mob(lambda x: 0 if x == 7 else (7 if x == 0 else (-inv7[x]) % 7))
from sympy.combinatorics import PermutationGroup
PSL27 = PermutationGroup([T, Sg])
assert PSL27.order() == 168
elems = list(PSL27.elements)


def evalw(w, ia, ib):
    r = Permutation(list(range(8)))
    for g, e in w.array_form:
        base = ia if str(g) == 'a' else ib
        r = r * (base ** e)
    return r


def count_homs(rels):
    n = 0
    idp = Permutation(list(range(8)))
    for ia in elems:
        for ib in elems:
            if all(evalw(r, ia, ib) == idp for r in rels):
                n += 1
    return n


ok = True
cases = {'stable ray +': vscale(es, Q5(Fr(1, 5))), 'stable ray -': vscale(es, Q5(Fr(-1, 5))),
         'unstable ray +': vscale(eu, Q5(Fr(1, 5))), 'unstable ray -': vscale(eu, Q5(Fr(-1, 5)))}
for name, x0 in cases.items():
    pa, pb = prong_phi(x0)
    ab_ok = (abel(pa), abel(pb)) == ((2, 1), (1, 1))
    G = FpGroup(F, [a ** -1 * pa, b ** -1 * pb])
    order = G.order()
    print(f'{name:15s} phi(a) = {pa}, phi(b) = {pb}; abelianization A: {ab_ok}; filled group order {order}')
    ok = ok and ab_ok and order == 1

SQ = [vec(Fr(2 * u, 5), Fr(2 * v, 5)) for u, v in ((1, 1), (-1, 1), (-1, -1), (1, -1))]  # ccw, quadrants I..IV


def boundary_loop(x0):
    q = {(1, 1): 0, (-1, 1): 1, (-1, -1): 2, (1, -1): 3}[(x0[0].sign(), x0[1].sign())]
    pts = [x0] + [SQ[(q + j) % 4] for j in range(5)] + [x0]
    w = F.identity
    for P, Q in zip(pts[:-1], pts[1:]):
        w = w * word(crossing_word(P, Q))
    return w


def apply_phi(w, pa, pb):
    r = F.identity
    for g, e in w.array_form:
        r = r * ((pa if str(g) == 'a' else pb) ** e)
    return r


print('boundary loop d and peripherality phi(d) = d:')
for name, x0 in cases.items():
    pa_, pb_ = prong_phi(x0)
    d = boundary_loop(x0)
    fix = apply_phi(d, pa_, pb_) == d
    print(f'  {name:15s} d = {d}; phi(d) == d: {fix}')
    ok = ok and fix and d != F.identity

print('base point independence along the rays (same words for x0 = e/5, e/50, e/500):')
for e, nm in ((es, '+e_s'), (vscale(es, Q5(-1)), '-e_s'), (eu, '+e_u'), (vscale(eu, Q5(-1)), '-e_u')):
    ws = {tuple(str(w) for w in prong_phi(vscale(e, Q5(Fr(1, n))))) for n in (5, 50, 500)}
    print(f'  {nm}: {ws}')
    ok = ok and len(ws) == 1

pa, pb = prong_phi(cases['stable ray +'])
d = boundary_loop(cases['stable ray +'])
print('control: fillings along t d^k (base point on the + stable ray)')
for k in (-2, -1, 1, 2):
    dk = d ** k
    rels = [a ** -1 * dk * pa * dk ** -1, b ** -1 * dk * pb * dk ** -1]
    n = count_homs(rels)
    print(f'  k = {k:+d}: homomorphisms to PSL(2,7): {n}')
    if abs(k) == 1:
        ok = ok and n > 1
rels0 = [a ** -1 * pa, b ** -1 * pb]
n0 = count_homs(rels0)
print(f'  k =  0: homomorphisms to PSL(2,7): {n0}')
ok = ok and n0 == 1
print()
print('ALL PASS' if ok else 'SOME FAILED')
