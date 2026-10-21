"""verifier: B_3, B_5, B_7 on analytic manufactured axis data by two power-series solutions (written for this run).

For T_j = w G_j' + (j h - 1) G_j - F_j = 0 on (0, x*):
  G_j^P = the solution analytic at P (series in z = x - x*; the recursion (n A + j - 1) gamma_n = ... never degenerates),
          which is the solution bounded at P (the other solutions carry H_j ~ |z|^(-(j-1)/A));
  G_j^0 = the solution analytic at 0 (series in x; the recursion (-n A + j(2A + 1) - 1) gamma_n = ... degenerates only at
          n = p_j, not an integer).
Both solve the same first-order linear ODE, so G_j^P - G_j^0 = B_j H_j on (0, x*), with H_j the homogeneous solution
normalized H_j ~ x^(p_j) at 0, i.e. B_j = (G_j^P(x) - G_j^0(x)) / H_j(x) for every x in the common disc of convergence.
This is the definition B_j = lim (G_j - smooth)/H_j with no finite part.  For j = 5 (7) the inputs G_3 (G_3, G_5) must be
analytic at both ends, i.e. B_3 = 0 (B_3 = B_5 = 0); otherwise F_5 is not analytic at 0.
H_j = A^(q_j) g^(j + q_j) |w|^(-q_j), q_j = (j - 1)/A (valid when T_1 = 0 and g ~ x^2, i.e. a(0) = 1).
Data: rational w, g given as polynomial pairs (numerator, denominator) in x; c_l = (A + 1)/2."""
import mpmath as mp


class S:
    """Truncated power series (list of mpf), length n."""
    def __init__(self, c, n):
        c = list(c)[:n]
        self.c = c + [mp.mpf(0)] * (n - len(c))
        self.n = n

    def __add__(self, o):
        if not isinstance(o, S):
            c = list(self.c); c[0] += o; return S(c, self.n)
        n = min(self.n, o.n)
        return S([a + b for a, b in zip(self.c[:n], o.c[:n])], n)
    __radd__ = __add__

    def __neg__(self):
        return S([-a for a in self.c], self.n)

    def __sub__(self, o):
        return self + (-o)

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, S):
            return S([a * o for a in self.c], self.n)
        n = min(self.n, o.n)
        a, b = self.c, o.c
        return S([mp.fsum(a[i] * b[k - i] for i in range(k + 1)) for k in range(n)], n)
    __rmul__ = __mul__

    def d(self):
        return S([k * self.c[k] for k in range(1, self.n)], self.n - 1)

    def div(self, o):
        n = min(self.n, o.n)
        a, b = self.c, o.c
        assert b[0] != 0
        q = []
        for k in range(n):
            q.append((a[k] - mp.fsum(q[i] * b[k - i] for i in range(k))) / b[0])
        return S(q, n)

    def __call__(self, z):
        s = mp.mpf(0)
        for a in reversed(self.c):
            s = s * z + a
        return s


def poly_at(p, x0, n):
    """Polynomial coefficients p (in x) re-expanded at x0: series in z = x - x0."""
    deg = len(p) - 1
    out = []
    for k in range(deg + 1):
        out.append(mp.fsum(mp.binomial(i, k) * p[i] * mp.mpf(x0) ** (i - k) for i in range(k, deg + 1)))
    return S(out, n)


def solve_T(w, h, F, j, A):
    """Series G with w G' + (j h - 1) G = F, w(x0) = 0 (w_0 = 0)."""
    n = min(w.n - 1, h.n, F.n)
    W, C, f = w.c, (j * h - 1).c, F.c
    assert abs(W[0]) < mp.mpf(10) ** (-mp.mp.dps + 10)
    g = []
    for m in range(n):
        s = f[m] - mp.fsum(W[i] * (m - i + 1) * g[m - i + 1] for i in range(2, m + 2) if m - i + 1 >= 0) \
            - mp.fsum(C[i] * g[m - i] for i in range(1, m + 1))
        g.append(s / (m * W[1] + C[0]))
    return S(g, n)


def hierarchy(wn, wd, gn, gd, A, x0, n, jmax=5):
    """All series at x0 (0 or x*) for rational w = wn/wd, g = gn/gd."""
    w = poly_at(wn, x0, n).div(poly_at(wd, x0, n))
    g = poly_at(gn, x0, n).div(poly_at(gd, x0, n))
    cl = (A + 1) / 2
    h = 2 * cl - w.d()
    a2 = (g.d() - w.d().d()) * mp.mpf(0.5)
    b3 = -a2.d() * (mp.mpf(1) / 3)
    F3 = -(a2 * g.d()) - b3 * g
    G3 = solve_T(w, h, F3, 3, A)
    out = dict(w=w, g=g, h=h, T1=w * g.d() + (h - 1) * g, F3=F3, G3=G3)
    if jmax >= 5:
        W14 = (b3.d() + G3.d()) * mp.mpf(0.25)
        W25 = -W14.d() * (mp.mpf(1) / 5)
        F5 = -(a2 * G3.d()) - 3 * (b3 * G3) - W14 * g.d() - W25 * g
        G5 = solve_T(w, h, F5, 5, A)
        out.update(F5=F5, G5=G5)
    if jmax >= 7:
        W16 = (W25.d() + G5.d()) * (mp.mpf(1) / 6)
        W27 = -W16.d() * (mp.mpf(1) / 7)
        F7 = -(a2 * G5.d() + W14 * G3.d() + W16 * g.d() + 5 * (b3 * G5) + 3 * (W25 * G3) + W27 * g)
        G7 = solve_T(w, h, F7, 7, A)
        out.update(F7=F7, G7=G7)
    return out


def Bj(wn, wd, gn, gd, A, xs, n, xe, jmax=5):
    """B_j natural units at the evaluation points xe (list), from the series at 0 and at xs."""
    s0 = hierarchy(wn, wd, gn, gd, A, 0, n, jmax)
    sP = hierarchy(wn, wd, gn, gd, A, xs, n, jmax)
    res = {}
    for j in [3, 5, 7][:(jmax - 1) // 2]:
        q = mp.mpf(j - 1) / A
        pj = 2 * j + q
        vals = []
        for x in xe:
            x = mp.mpf(x)
            wv = mp.polyval(list(reversed(wn)), x) / mp.polyval(list(reversed(wd)), x)
            gv = mp.polyval(list(reversed(gn)), x) / mp.polyval(list(reversed(gd)), x)
            H = A ** q * gv ** (j + q) * abs(wv) ** (-q)
            G0, GP = s0['G%d' % j](x), sP['G%d' % j](x - xs)
            vals.append(dict(x=x, B=(GP - G0) / H, Bnat=(GP - G0) / H * mp.mpf(xs) ** (pj - j + 1), G0=G0, GP=GP, H=H))
        res[j] = vals
    return res, s0, sP


def r12(A, L):
    """R12: w = -A x (1 - u^2)/(1 + u^2), g = x^2/(1 + u^2), u = x/L (numerator, denominator coefficient lists in x)."""
    L2 = mp.mpf(L) ** 2
    wn = [0, -A, 0, A / L2]
    d = [1, 0, 1 / L2]
    gn = [0, 0, 1]
    return wn, d, gn, d
