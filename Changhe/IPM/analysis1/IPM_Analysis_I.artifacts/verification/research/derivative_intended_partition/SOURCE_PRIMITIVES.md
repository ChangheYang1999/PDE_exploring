# The remaining scalar primitive bindings

Mandatory supplement. The entire frozen cert_resid.py and midrad.py files accompany the review of this supplement. In cert_resid.py the import binds MR,U,ETA,BETA,succ from midrad. In midrad, U=2.0**-53 and INF=np.inf; succ is np.nextafter(x,INF). MR converts finite inputs to float arrays and stores their nonnegative radius without a numerical operation changing its value. Its mag is succ(abs(m)+r). Thus the exact scalar IEEE emulation matches the frozen primitives. These conventions do not prove every interval arithmetic operation in the derivative certificate.

Frozencert_resid.py, SHA256 1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053.
```python
20: """
21: import os, sys, json, time
22: sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
23: import numpy as np
24: from math import factorial, comb
25: from midrad import MR, mr_matmul, succ, U, ETA
26: from flint import arb, ctx
27: 
28: 
29: def mag(x):      # upper bound of |x| for an MR
30:     return x.mag()
31: 
32: 
33: class TMArr:
```
```python
391: # identities A' = -2n A + g, B' = 2n B - g (g, R exponential-polynomials differentiated exactly) and Leibniz rules.
392: # =====================================================================================================================
393: def _cell_core_deriv(self, h_up, e_ta, a_terms, A0, B0, m_ta, wfar_ta, nder=2):
394:     from math import comb as _comb
395:     Q = self.Q; n = self.n
396:     hpow = np.array([1.0] + [succ(h_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Q + 3)])
397:     f_terms, R_terms = self.f_terms_from_a(a_terms)
398:     e2 = e_ta * e_ta; e3 = e2 * e_ta; e4 = e2 * e2
399:     inv_e = MR(1.0 / e_ta.m, succ(e_ta.r / (e_ta.mig() ** 2) + U * abs(1.0 / e_ta.m))); inv_e2 = inv_e * inv_e
400: 
401:     def bc(c, r, S):
```
```python
501:     self._last_supNs = supNs
502:     return out
503: 
504: 
505: Certifier.cell_core_deriv = _cell_core_deriv
506: 
507: 
508: def cell_deriv(self, ci, nder=2):
509:     h = self.tb[ci + 1] - self.tb[ci]; h_up = h.mag()
510:     res = self.cell_core_deriv(h_up, self.e_ta[ci], [(0.0, self.T[ci])], self.A[ci], self.B[ci], self.m_ta[ci], self.wfar_ta[ci], nder)
511:     res.update(ci=ci, t_a=float(self.tb.m[ci]), h=float(h_up))
512:     return res
```
Frozenmidrad.py, SHA256 5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e.
```python
14: 
15: U = 2.0 ** -53
16: ETA = 2.0 ** -1074
17: BETA = np.nextafter(U / (1 - U), np.inf)          # upper enclosure of u/(1-u)
18: INF = np.inf
19: 
20: 
21: def succ(x):
22:     return np.nextafter(x, INF)
23: 
24: 
25: class MR:
26:     """Arrays of midpoints and radii (same shape; radii >= 0)."""
27:     __slots__ = ("m", "r")
28: 
29:     def __init__(self, m, r=None):
30:         self.m = np.asarray(m, float)
31:         self.r = np.zeros_like(self.m) if r is None else np.broadcast_to(np.asarray(r, float), self.m.shape).copy()
32:         assert np.all(self.r >= 0)
33: 
34:     @staticmethod
35:     def exact(m):
36:         return MR(m, 0.0)
37: 
```
```python
44:         rads = succ(succ(succ(rads) + succ(U * np.abs(mids))) + ETA)
45:         return MR(mids, rads)
46: 
47:     def __getitem__(self, k):
48:         return MR(self.m[k], self.r[k])
49: 
50:     @property
51:     def shape(self):
52:         return self.m.shape
53: 
54:     def __neg__(self):
55:         return MR(-self.m, self.r)
56: 
57:     def __add__(self, other):
58:         if not isinstance(other, MR): other = MR.exact(other)
59:         m = self.m + other.m
60:         r = succ(succ(succ(self.r + other.r) + succ(BETA * np.abs(m))))
61:         return MR(m, r)
62: 
63:     __radd__ = __add__
```
```python
74:         m = self.m * other.m
75:         r = succ(succ(succ(succ(succ(np.abs(self.m) * other.r) + succ(np.abs(other.m) * self.r)) + succ(self.r * other.r))
76:                       + succ(BETA * np.abs(m))) + ETA)
77:         return MR(m, r)
78: 
79:     __rmul__ = __mul__
80: 
81:     def mag(self):
82:         """Upper bound of |x| over the ball."""
83:         return succ(np.abs(self.m) + self.r)
84: 
85:     def mig(self):
86:         """Lower bound of |x| over the ball (0 if the ball contains 0): |m| - r rounded downward."""
87:         return np.maximum(np.nextafter(np.abs(self.m) - self.r, -INF), 0.0)
88:     
89:     def lower(self):
90:         return np.nextafter(self.m - self.r, -INF)
91: 
```
