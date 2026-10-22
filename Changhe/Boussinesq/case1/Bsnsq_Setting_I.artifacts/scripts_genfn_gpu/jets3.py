"""Truncated Taylor jets (torch, float64) in three variables (xh, eh, s): monomials xh^i eh^j s^k with i + j <= P, k <= Q.
A jet at N points is a tensor c of shape (n, N) holding d^(i+j+k) f / (dxh^i deh^j ds^k) / (i! j! k!).
Used by desing.py: (xh, eh) are the dilated chart coordinates and s is the far-field variable sigma = lambda^(-1/beta)."""
import math, torch
DT = torch.float64
DEV3 = torch.device('cpu')     # device for jets created from python scalars / numpy input (2026-10-21: set to the CUDA device by the GPU solvers)

_MON = {}
def monos3(P, Q):
    if (P, Q) not in _MON:
        L = [(i, d - i, k) for k in range(Q + 1) for d in range(P + 1) for i in range(d, -1, -1)]
        _MON[(P, Q)] = (L, {m: n for n, m in enumerate(L)})
    return _MON[(P, Q)]

_MUL = {}
def _multab(P, Q, dev=None):
    dev = torch.device('cpu') if dev is None else torch.device(dev)
    key = (P, Q, str(dev))
    if key not in _MUL:
        L, ix = monos3(P, Q)
        ko, ka, kb = [], [], []
        for (i, j, k) in L:
            for i1 in range(i + 1):
                for j1 in range(j + 1):
                    for k1 in range(k + 1):
                        ko.append(ix[(i, j, k)]); ka.append(ix[(i1, j1, k1)]); kb.append(ix[(i - i1, j - j1, k - k1)])
        _MUL[key] = (torch.tensor(ko, device=dev), torch.tensor(ka, device=dev), torch.tensor(kb, device=dev))
    return _MUL[key]

def _sub(c, PQ, PQn):
    """coefficients of a (P, Q) jet restricted to the monomials of (Pn, Qn)"""
    if PQ == PQn: return c
    L, ix = monos3(*PQn); _, ixo = monos3(*PQ)
    return c[torch.tensor([ixo[m] for m in L], device=c.device)]

class Jet3:
    def __init__(self, c, P, Q):
        self.c = c; self.P = P; self.Q = Q
    @staticmethod
    def var(v, which, P, Q):
        L, ix = monos3(P, Q)
        c = torch.zeros(len(L), v.shape[0], dtype=DT, device=v.device); c[0] = v
        key = [(1, 0, 0), (0, 1, 0), (0, 0, 1)][which]
        if key in ix: c[ix[key]] = 1.0
        return Jet3(c, P, Q)
    @staticmethod
    def const(v, P, Q, N=None):
        L, ix = monos3(P, Q)
        if not torch.is_tensor(v): v = torch.full((N,), float(v), dtype=DT, device=DEV3)
        c = torch.zeros(len(L), v.shape[0], dtype=DT, device=v.device); c[0] = v
        return Jet3(c, P, Q)
    def trunc(self, P, Q):
        return Jet3(_sub(self.c, (self.P, self.Q), (P, Q)), P, Q)
    def _common(self, o):
        P, Q = min(self.P, o.P), min(self.Q, o.Q)
        return P, Q, _sub(self.c, (self.P, self.Q), (P, Q)), _sub(o.c, (o.P, o.Q), (P, Q))
    def __add__(self, o):
        if isinstance(o, Jet3):
            P, Q, a, b = self._common(o); return Jet3(a + b, P, Q)
        c = self.c.clone(); c[0] = c[0] + o; return Jet3(c, self.P, self.Q)
    __radd__ = __add__
    def __neg__(self): return Jet3(-self.c, self.P, self.Q)
    def __sub__(self, o): return self + (-o)
    def __rsub__(self, o): return (-self) + o
    def __mul__(self, o):
        if isinstance(o, Jet3):
            P, Q, a, b = self._common(o)
            ko, ka, kb = _multab(P, Q, a.device)
            out = torch.zeros_like(a).index_add(0, ko, a[ka] * b[kb])
            return Jet3(out, P, Q)
        if torch.is_tensor(o): return Jet3(self.c * o[None, :], self.P, self.Q)
        return Jet3(self.c * o, self.P, self.Q)
    __rmul__ = __mul__
    def val(self): return self.c[0]
    def _d(self, which):
        P, Q = (self.P - 1, self.Q) if which < 2 else (self.P, self.Q - 1)
        L, _ = monos3(P, Q); _, ixp = monos3(self.P, self.Q)
        rows = []
        for (i, j, k) in L:
            if which == 0: rows.append((i + 1) * self.c[ixp[(i + 1, j, k)]])
            elif which == 1: rows.append((j + 1) * self.c[ixp[(i, j + 1, k)]])
            else: rows.append((k + 1) * self.c[ixp[(i, j, k + 1)]])
        return Jet3(torch.stack(rows), P, Q)
    def dx(self): return self._d(0)
    def de(self): return self._d(1)
    def ds(self): return self._d(2)
    def compose(self, coefs):
        """f(self), coefs[n] = f^(n)(v)/n! at v = self.val(), n = 0..P+Q"""
        h = Jet3(self.c.clone(), self.P, self.Q); h.c[0] = 0.0
        out = Jet3.const(coefs[0], self.P, self.Q)
        hm = None
        for n in range(1, self.P + self.Q + 1):
            hm = h if hm is None else hm * h
            out = out + hm * coefs[n]
        return out
    def pow(self, q):
        v = self.val(); coefs = []; b = 1.0
        for n in range(self.P + self.Q + 1):
            coefs.append(b * v ** (q - n)); b = b * (q - n) / (n + 1)
        return self.compose(coefs)
    def log(self):
        v = self.val(); coefs = [torch.log(v)]
        for n in range(1, self.P + self.Q + 1): coefs.append(((-1.0) ** (n + 1)) / (n * v ** n))
        return self.compose(coefs)
    def exp(self):
        v = self.val(); ev = torch.exp(v); coefs = [ev]
        for n in range(1, self.P + self.Q + 1): coefs.append(ev / math.factorial(n))
        return self.compose(coefs)
    def ipow(self, n):
        out = self
        for _ in range(n - 1): out = out * self
        return out
