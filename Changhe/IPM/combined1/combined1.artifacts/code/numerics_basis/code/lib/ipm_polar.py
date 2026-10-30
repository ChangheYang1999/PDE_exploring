"""Symbolic polar derivative algebra for generator fields (lane c1-n1).

A PolarSeries is a dict  key=(a, b, N, t) -> coefficient  meaning  coef * G^(a)(r) * r^(-b) * trig_t(N theta),  t in {'s','c'}.
G is the radial function of a generator (chi = G(r) cos(n theta), n = 2m).  Operators d_x, d_y act exactly:
  d_r: G^(a) r^-b -> G^(a+1) r^-b - b G^(a) r^-(b+1);  d_theta: sin N -> N cos N, cos N -> -N sin N;
  cos theta * sin N = [sin(N+1) + sin(N-1)]/2, cos theta * cos N = [cos(N+1) + cos(N-1)]/2,
  sin theta * sin N = [cos(N-1) - cos(N+1)]/2, sin theta * cos N = [sin(N+1) - sin(N-1)]/2;
  d_x = cos th d_r - (sin th / r) d_th,  d_y = sin th d_r + (cos th / r) d_th.
Fields: psi = d_x d_y chi; rho = -d_y (d_xx + d_yy) chi; derivatives by repeated d_x, d_y.
Evaluation needs G^(a)(r), a <= AMAX (= 6), on the radial grid: radial_primitives().
"""
import math
from fractions import Fraction
import numpy as np
import torch
import sympy

DT = torch.float64
AMAX = 6

def _add(d, key, v):
    if v == 0: return
    a, b, N, t = key
    if N < 0:
        N = -N
        if t == 's': v = -v
    if N == 0 and t == 's': return
    key = (a, b, N, t)
    nv = d.get(key, 0)+v
    if nv == 0: d.pop(key, None)
    else: d[key] = nv

def d_r(S):
    out = {}
    for (a, b, N, t), v in S.items():
        _add(out, (a+1, b, N, t), v)
        if b != 0: _add(out, (a, b+1, N, t), -b*v)
    return out

def d_th(S):
    out = {}
    for (a, b, N, t), v in S.items():
        if t == 's': _add(out, (a, b, N, 'c'), N*v)
        else: _add(out, (a, b, N, 's'), -N*v)
    return out

def div_r(S): return {(a, b+1, N, t): v for (a, b, N, t), v in S.items()}

def mul_cos(S):
    out = {}
    for (a, b, N, t), v in S.items():
        _add(out, (a, b, N+1, t), v/2); _add(out, (a, b, N-1, t), v/2)
    return out

def mul_sin(S):
    out = {}
    for (a, b, N, t), v in S.items():
        if t == 's': _add(out, (a, b, N-1, 'c'), v/2); _add(out, (a, b, N+1, 'c'), -v/2)
        else: _add(out, (a, b, N+1, 's'), v/2); _add(out, (a, b, N-1, 's'), -v/2)
    return out

def add(S1, S2, f1=1, f2=1):
    out = {}
    for k, v in S1.items(): _add(out, k, f1*v)
    for k, v in S2.items(): _add(out, k, f2*v)
    return out

def d_x(S): return add(mul_cos(d_r(S)), mul_sin(div_r(d_th(S))), 1, -1)
def d_y(S): return add(mul_sin(d_r(S)), mul_cos(div_r(d_th(S))), 1, 1)

def deriv(S, i, j):
    for _ in range(i): S = d_x(S)
    for _ in range(j): S = d_y(S)
    return S

def chi_series(n): return {(0, 0, n, 'c'): Fraction(1)}

def field_series(n, dmax_rho=3, dmax_psi=3):
    """dict ('rho',(i,j)) and ('psi',(i,j)) -> PolarSeries for a generator with angular index n=2m, derivatives up to total order dmax"""
    chi = chi_series(n)
    psi = d_x(d_y(chi))
    lap = add(d_x(d_x(chi)), d_y(d_y(chi)))
    rho = {k: -v for k, v in d_y(lap).items()}
    out = {}
    for base, S, dmax in (('rho', rho, dmax_rho), ('psi', psi, dmax_psi)):
        for i in range(dmax+1):
            for j in range(dmax+1-i):
                out[(base, (i, j))] = deriv(S, i, j)
    return out

# ------------------------------------------------------------------ radial primitives
_RD_TABLE = None
def rderiv_table(amax=AMAX):
    """coefficients: d^a/dr^a g(r^2) = sum_k c[a][k](r) g^(k)(u), c as list of (power of r, integer coeff)"""
    global _RD_TABLE
    if _RD_TABLE is not None: return _RD_TABLE
    r, u = sympy.symbols('r u', positive=True)
    g = sympy.Function('g')
    expr = g(r**2)
    table = []
    for a in range(amax+1):
        e = sympy.expand(expr.diff(r, a)) if a else expr
        # collect derivatives of g: terms like coeff * r^p * Derivative(g(r**2), (r**2, k))  -> substitute
        e = e.subs(r**2, u) if False else e
        terms = []
        e = sympy.expand(e)
        for term in sympy.Add.make_args(e):
            coeff, rest = term.as_independent(r, as_Add=False) if False else (1, term)
            # term = c * r**p * Subs(Derivative(g(_x), (_x, k)), _x, r**2) or Derivative(g(r**2),...)
            k = 0; c = sympy.Integer(1); p = 0
            for f in sympy.Mul.make_args(term):
                if f.is_Number: c *= f
                elif f.is_Pow and f.base == r: p += int(f.exp)
                elif f == r: p += 1
                elif isinstance(f, sympy.Subs) or isinstance(f, sympy.Derivative):
                    d = f.expr if isinstance(f, sympy.Subs) else f
                    k = sum(cnt for _, cnt in d.variable_count) if isinstance(d, sympy.Derivative) else 0
                elif f.func == g: k = 0
                else: raise ValueError(f'unexpected factor {f} in {term}')
            terms.append((p, int(c), k))
        table.append(terms)
    _RD_TABLE = table
    return table

def radial_primitives(p, Yj, mesh, amax=AMAX):
    """G^(a)(r), a<=amax, for G = R^p Y(t): u-derivatives G_u^(k) = R^(p-k) sum_l C(k,l)(p-l)_(k-l)(1-t)^l Y^(l), then the r-derivative table."""
    omt = mesh.u; Rp = torch.exp(p*mesh.logR)
    Gu = []
    for k in range(amax+1):
        acc = torch.zeros_like(mesh.t)
        for l in range(k+1):
            f = 1.0
            for i in range(k-l): f *= (p-l-i)
            acc = acc+math.comb(k, l)*f*omt**l*Yj[l]
        Gu.append(Rp*omt**k*acc)
    tab = rderiv_table(amax); r = mesh.r
    G = []
    for a in range(amax+1):
        acc = torch.zeros_like(mesh.t)
        for (pw, c, k) in tab[a]: acc = acc+c*(r**pw if pw else 1)*Gu[k]
        G.append(acc)
    return G

def series_slots(S, G, mesh):
    """evaluate a PolarSeries to slots: list of (typ, N, radial array) with typ 'sin'/'cos'"""
    rad = {}
    r = mesh.r
    for (a, b, N, t), v in S.items():
        key = ('sin' if t == 's' else 'cos', N)
        term = float(v)*G[a]*(r**(-b) if b else 1)
        rad[key] = rad[key]+term if key in rad else term
    return [(typ, N, arr) for (typ, N), arr in rad.items()]

class Tables:
    """sin(N th), cos(N th) tables"""
    def __init__(self, mesh, Nmax):
        N = torch.arange(Nmax+1, dtype=DT, device=mesh.device)[:, None]
        self.tab = {'sin': torch.sin(N*mesh.theta[None, :]), 'cos': torch.cos(N*mesh.theta[None, :])}
        self.Nmax = Nmax
