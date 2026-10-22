"""Bivariate truncated Taylor jets (torch, float64) in the variables (x, eta).
A jet of order p at N points is a tensor c of shape (n_p, N), n_p = (p+1)(p+2)/2, holding the Taylor coefficients
d^(i+j) f / (dx^i deta^j) / (i! j!) for i + j <= p, in the order of monos(p)."""
import math, torch
DT = torch.float64

_MON = {}
def monos(p):
    if p not in _MON:
        L = [(i, d - i) for d in range(p + 1) for i in range(d, -1, -1)]
        _MON[p] = (L, {m: k for k, m in enumerate(L)})
    return _MON[p]

_MUL = {}
def _multab(p):
    if p not in _MUL:
        L, ix = monos(p)
        ko, ka, kb = [], [], []
        for (i, j) in L:
            for i1 in range(i + 1):
                for j1 in range(j + 1):
                    ko.append(ix[(i, j)]); ka.append(ix[(i1, j1)]); kb.append(ix[(i - i1, j - j1)])
        _MUL[p] = (torch.tensor(ko), torch.tensor(ka), torch.tensor(kb))
    return _MUL[p]

class Jet:
    def __init__(self, c, p):
        self.c = c; self.p = p
    @staticmethod
    def var(v, which, p):
        """jet of the coordinate x (which=0) or eta (which=1) at the points v (N,)"""
        L, ix = monos(p)
        c = torch.zeros(len(L), v.shape[0], dtype=DT)
        c[0] = v
        if p >= 1:
            c[ix[(1, 0)] if which == 0 else ix[(0, 1)]] = 1.0
        return Jet(c, p)
    @staticmethod
    def const(v, p, N=None):
        L, ix = monos(p)
        if not torch.is_tensor(v):
            v = torch.full((N,), float(v), dtype=DT)
        c = torch.zeros(len(L), v.shape[0], dtype=DT); c = c.clone(); c[0] = v
        return Jet(c, p)
    def trunc(self, p):
        if p == self.p: return self
        n = (p + 1) * (p + 2) // 2
        return Jet(self.c[:n], p)
    def __add__(self, o):
        if isinstance(o, Jet):
            p = min(self.p, o.p); return Jet(self.trunc(p).c + o.trunc(p).c, p)
        c = self.c.clone(); c[0] = c[0] + o; return Jet(c, self.p)
    __radd__ = __add__
    def __neg__(self): return Jet(-self.c, self.p)
    def __sub__(self, o): return self + (-o)
    def __rsub__(self, o): return (-self) + o
    def __mul__(self, o):
        if isinstance(o, Jet):
            p = min(self.p, o.p)
            ko, ka, kb = _multab(p)
            a = self.trunc(p).c; b = o.trunc(p).c
            out = torch.zeros_like(a)
            out = out.index_add(0, ko, a[ka] * b[kb])
            return Jet(out, p)
        if torch.is_tensor(o):
            return Jet(self.c * o[None, :], self.p)
        return Jet(self.c * o, self.p)
    __rmul__ = __mul__
    def val(self): return self.c[0]
    def dx(self):
        L, ix = monos(self.p - 1); Lp, ixp = monos(self.p)
        rows = [ (i + 1) * self.c[ixp[(i + 1, j)]] for (i, j) in L ]
        return Jet(torch.stack(rows), self.p - 1)
    def de(self):
        L, ix = monos(self.p - 1); Lp, ixp = monos(self.p)
        rows = [ (j + 1) * self.c[ixp[(i, j + 1)]] for (i, j) in L ]
        return Jet(torch.stack(rows), self.p - 1)
    def compose(self, coefs):
        """f(self) with coefs[m] = f^(m)(v)/m! (tensors (N,)) at v = self.val(), m = 0..p"""
        h = Jet(self.c.clone(), self.p); h.c = torch.cat([torch.zeros_like(self.c[:1]), self.c[1:]], 0)
        out = Jet.const(coefs[0], self.p)
        hm = None
        for m in range(1, self.p + 1):
            hm = h if hm is None else hm * h
            out = out + hm * coefs[m]
        return out
    def pow(self, q):
        v = self.val(); coefs = []
        b = 1.0
        for m in range(self.p + 1):
            coefs.append(b * v ** (q - m))
            b = b * (q - m) / (m + 1)
        return self.compose(coefs)
    def log(self):
        v = self.val(); coefs = [torch.log(v)]
        for m in range(1, self.p + 1):
            coefs.append(((-1.0) ** (m + 1)) / (m * v ** m))
        return self.compose(coefs)
    def exp(self):
        v = self.val(); ev = torch.exp(v); coefs = [ev]
        for m in range(1, self.p + 1):
            coefs.append(ev / math.factorial(m))
        return self.compose(coefs)
    def ipow(self, n):
        out = self
        for _ in range(n - 1): out = out * self
        return out

def deriv_values(J):
    """dict (i,j) -> d^(i+j)f/dx^i deta^j values"""
    L, ix = monos(J.p)
    return {(i, j): J.c[ix[(i, j)]] * math.factorial(i) * math.factorial(j) for (i, j) in L}
