"""Exact obstruction functional B (natural units B_3 x*^(4 + beta)) on an analytic compatible reference trace in
normalized variables u = x/x*:
    w(u) = -A u (1 - u^2)/(1 + u^2) + u^3 (1 - u^2)^2 q(u^2),   e = x*^(-2),
g rebuilt from w (w g' = (w' - A) g, g/u^2 -> 1), Q = (g' - e w'')/(2 g^3), m = -w/g, and (6.3.1 (i))
    B = ((beta - 1) A^(1 - beta)/3) f.p. int_0^1 (Q - Q(1)) m^(beta - 2) g^(-1) du.
Finite part at 0 from the Taylor series at 0 on (0, uc]; mpmath quadrature on [uc, 1 - de]; Taylor series at 1 on
[1 - de, 1] (integrand s^(beta - 1) Phi(s), s = 1 - u, Phi analytic). log(g/u^2) by quadrature of the analytic
function h = (w' - A)/w - 2/u (removable singularities at 0 and 1).
Usage as a module: B(A, e, qcoef, dps=40) with qcoef the monomial coefficients of q (exact decimal strings or mpf)."""
import mpmath as mp


# ---------- truncated power series (lists of mpf, index = power) ----------
def smul(a, b, N):
    c = [mp.mpf(0)] * N
    for i, ai in enumerate(a[:N]):
        if ai == 0:
            continue
        for j in range(min(len(b), N - i)):
            c[i + j] += ai * b[j]
    return c


def sdiv(a, b, N):
    a = list(a[:N]) + [mp.mpf(0)] * (N - len(a[:N]))
    c = [mp.mpf(0)] * N
    for n in range(N):
        s = a[n] - sum(c[k] * b[n - k] for k in range(max(0, n - len(b) + 1), n))
        c[n] = s / b[0]
    return c


def sder(a):
    return [k * a[k] for k in range(1, len(a))] + [mp.mpf(0)]


def sint(a, N):
    return [mp.mpf(0)] + [a[k] / (k + 1) for k in range(N - 1)]


def sexp(a, N):
    # exp of series with a[0] arbitrary: y' = a' y
    y = [mp.mpf(0)] * N
    y[0] = mp.exp(a[0])
    da = sder(a)
    for n in range(1, N):
        y[n] = sum((k + 1) * a[k + 1] * y[n - 1 - k] for k in range(n)) / n
    return y


def spow(a, p, N):
    # a[0] > 0
    la = slog(a, N)
    return sexp([p * v for v in la], N)


def slog(a, N):
    q = sdiv(sder(a)[:N], a, N)
    s = sint(q, N)
    s[0] = mp.log(a[0])
    return s


def pshift(P, c):
    """coefficients of P(c + t) from coefficients of P(t)."""
    n = len(P)
    out = [mp.mpf(0)] * n
    for k in range(n):
        out[k] = sum(mp.binomial(j, k) * P[j] * c ** (j - k) for j in range(k, n))
    return out


def peval(P, t):
    return mp.polyval(P[::-1], t)


class Ref:
    def __init__(self, A, e, qcoef, dps=40):
        mp.mp.dps = dps
        self.A = A = mp.mpf(A)
        self.e = mp.mpf(e)
        self.beta = 2 / A
        q = [mp.mpf(c) for c in qcoef]
        # N(t) = -A t (1 - t^2) + t^3 (1 - t^2)^2 (1 + t^2) q(t^2), D(t) = 1 + t^2, w = N/D
        nq = len(q)
        deg = 3 + 6 + 2 * (nq - 1) + 1
        Np = [mp.mpf(0)] * (deg + 1)
        Np[1] += -A
        Np[3] += A
        # (1 - t^2)^2 (1 + t^2) = 1 - t^2 - t^4 + t^6
        base = {0: 1, 2: -1, 4: -1, 6: 1}
        for k, qk in enumerate(q):
            for p, b in base.items():
                Np[3 + p + 2 * k] += b * qk
        self.Np = Np
        self.Dp = [mp.mpf(1), mp.mpf(0), mp.mpf(1)]

    # pointwise
    def w(self, t, d=0):
        return self.wser(t, d + 1)[d] * mp.factorial(d)

    def wser(self, c, N):
        Nc = pshift(self.Np, c) + [mp.mpf(0)] * N
        Dc = pshift(self.Dp, c) + [mp.mpf(0)] * N
        return sdiv(Nc[:N], Dc[:N], N)

    def h(self, t):
        # (w' - A)/w - 2/t, rational
        Nv = peval(self.Np, t); Dv = 1 + t ** 2
        dN = peval([k * self.Np[k] for k in range(1, len(self.Np))], t)
        wv = Nv / Dv
        wpv = (dN * Dv - Nv * 2 * t) / Dv ** 2
        return (wpv - self.A) / wv - 2 / t

    def radii(self):
        """distances from 0 and from 1 to the nearest other zero of the numerator N (and to +-i)."""
        import numpy as np
        P = [float(v) for v in self.Np]
        while P and P[-1] == 0:
            P.pop()
        roots = list(np.roots(P[::-1])) + [1j, -1j]
        nz = [z for z in roots if abs(z) > 1e-8 and abs(z - 1) > 1e-6 and abs(z + 1) > 1e-6]
        return min(abs(z) for z in nz), min(abs(z - 1) for z in nz)

    def setup(self, uc=None, de=None, N=80):
        A, e, be = self.A, self.e, self.beta
        d0, d1 = self.radii()
        if uc is None:
            uc = min(mp.mpf('0.25'), mp.mpf(0.4 * d0))
        if de is None:
            de = min(mp.mpf('0.25'), mp.mpf(0.4 * d1))
        self.uc, self.de, self.N = uc, de, N
        # ---- series at 0 ----
        W = self.wser(0, N + 2)
        W1 = W[1:N + 1]                                  # W/t
        Wp = sder(W)[:N + 1]
        WpA = list(Wp); WpA[0] -= A
        rho = sdiv(WpA[:N], W1, N)                       # (w' - A)/(w/t)
        lG1 = sint(rho[1:] + [mp.mpf(0)], N)             # log(g/t^2) = int_0^t sum_{k>=1} rho_k s^(k-1)
        G1 = sexp(lG1, N)
        self.lG1_0 = lG1
        self.ser0 = dict(W=W, W1=W1, rho=rho, G1=G1)
        # log G1 at uc from the series (check against quadrature later)
        self.lG1_uc = sum(lG1[k] * uc ** k for k in range(N))
        # log g(1)/1 = lG1(uc) + int_uc^1 h
        self.lG1_1 = self.lG1_uc + mp.quad(self.h, [uc, (uc + 1) / 2, 1])
        g1 = mp.exp(self.lG1_1)
        w2_1 = self.w(mp.mpf(1), 2)
        # at u = 1: g' = g (w' - A)/w -> g w''(1)/A
        self.Q1 = (g1 * w2_1 / A - e * w2_1) / (2 * g1 ** 3)
        self.g1 = g1
        # F(t) = [t^5 Q - Q1 t^5] (t m)^(beta - 2)/G1, t^5 Q = (G1 rho - e W''/t)/(2 G1^3)
        Wpp = sder(sder(W))
        Wpp_t = Wpp[1:N + 1]
        num = [G - e * v for G, v in zip(smul(G1, rho, N), Wpp_t)]
        t5Q = sdiv(num, smul(smul(G1, G1, N), [2 * v for v in G1], N), N)
        t5Q[5] -= self.Q1
        tm = sdiv([-v for v in W1[:N]], G1, N)          # t m = -w1/G1, tm(0) = A
        F = smul(smul(t5Q, spow(tm, be - 2, N), N), sdiv([mp.mpf(1)] + [mp.mpf(0)] * (N - 1), G1, N), N)
        self.F0 = F
        self.I0 = sum(F[k] * uc ** (k - 4 - be) / (k - 4 - be) for k in range(N))
        self.F0tail = [abs(F[k] * uc ** k) for k in range(N - 5, N)]
        # ---- series at 1 (tau = u - 1) ----
        W = self.wser(1, N + 2)                          # W[0] = 0, W[1] = A
        Wt = W[1:N + 1]                                  # W/tau
        Wp = sder(W)[:N + 1]
        WpA = list(Wp); WpA[0] -= A                      # WpA[0] = 0
        h1 = sdiv(WpA[1:N + 1], Wt, N)                   # (w' - A)/w, analytic
        lg = sint(h1, N); lg[0] = self.lG1_1             # log g (g = u^2 G1 = G1 at u = 1)
        g = sexp(lg, N)
        gp = sder(g)
        Wpp = sder(sder(W))
        num = [a - e * b for a, b in zip(gp[:N], Wpp[:N])]
        Q = sdiv(num, [2 * v for v in smul(smul(g, g, N), g, N)], N)
        D = Q[1:] + [mp.mpf(0)]                          # (Q - Q(1))/tau
        M = sdiv(Wt, g, N)                               # m = -tau M, M(0) = A/g(1)
        Phi = smul(smul(D, spow(M, be - 2, N), N), sdiv([mp.mpf(-1)] + [mp.mpf(0)] * (N - 1), g, N), N)
        self.Q1_check = Q[0]
        self.I1 = sum(Phi[k] * (-1) ** k * de ** (k + be) / (k + be) for k in range(N))
        self.F1tail = [abs(Phi[k] * de ** k) for k in range(N - 5, N)]

    def integrand(self, u):
        A, e, be = self.A, self.e, self.beta
        lG1 = self.lG1_uc + mp.quad(self.h, [self.uc, u])
        g = u ** 2 * mp.exp(lG1)
        wv = self.w(u, 0); wp = self.w(u, 1); wpp = self.w(u, 2)
        gp = g * (wp - A) / wv
        Q = (gp - e * wpp) / (2 * g ** 3)
        m = -wv / g
        return (Q - self.Q1) * m ** (be - 2) / g

    def B(self):
        A, be = self.A, self.beta
        Imid = mp.quad(self.integrand, [self.uc, (self.uc + 1 - self.de) / 2, 1 - self.de])
        self.Imid = Imid
        tot = self.I0 + Imid + self.I1
        return (be - 1) * A ** (1 - be) / 3 * tot


if __name__ == '__main__':
    import sys
    # sanity: R12 at L = 8.6000638, A = 10.150725 (q = 0): expected C_A (1 - S_A e)
    A = mp.mpf('10.150725'); L = mp.mpf('8.6000638')
    r = Ref(A, 1 / L ** 2, [0], dps=30)
    r.setup()
    b = r.B()
    be = 2 / A
    SA = 6 * A * (4 * A - 3) / (8 * A - 1)
    CA = (16 - be) / (3 * A * (4 + be)) * mp.beta(2 - be / 2, be)
    print('R12 B =', b, ' closed form C_A (1 - S_A e) =', CA * (1 - SA / L ** 2), ' Q1', r.Q1, r.Q1_check,
          'tails', [mp.nstr(v, 3) for v in r.F0tail[-2:] + r.F1tail[-2:]])
