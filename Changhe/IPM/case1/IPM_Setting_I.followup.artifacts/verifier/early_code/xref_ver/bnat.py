# Verifier evaluator for request (o6): the natural-units functional B on the analytic references
#   w0(u) = -A u (1 - u^2)/(1 + u^2) + u^3 (1 - u^2)^2 q(u^2),  e = 1/x*^2,
# written independently of the lead's bref.py. Formulation used here:
#   w0 = -u (1 - u) om(u),  om = A (1 + u)/(1 + u^2) - u^2 (1 - u)(1 + u)^2 q(u^2)   (om(0) = om(1) = A),
#   psi = -A/w0 - 1/u - 1/(1 - u) = [-A/(1 + u^2) + u (1 + u)^2 q(u^2)]/om   (analytic on [0, 1] if om > 0),
#   Psi(u) = int_0^u psi,  G = u^2 om e^Psi/A,  m = -w0/G = A (1 - u) e^(-Psi)/u   (solves w0 G' = (w0' - A) G, G/u^2 -> 1),
#   lam = G'/G = 2/u + om'/om + psi,  Q = (G lam - e w0'')/(2 G^3).
# Two representations (equal by one integration by parts, since dm/du = -A/G):
#   (I)  B = ((beta - 1) A^(1 - beta)/3) f.p. int_0^1 (Q - Q(1)) m^(beta - 2) G^(-1) du,
#   (II) B = (1/(3 A^beta)) f.p. int_0^1 Q' m^(beta - 1) du.
# [0, delta]: own truncated power series at 0, finite part termwise. [delta, 1 - t1]: Gauss-Legendre panels.
# [1 - t1, 1]: t = 1 - u = s^(1/beta), so that t^(beta - 1) dt = ds/beta, graded Gauss-Legendre panels in s.
# For (I) near 1, Q - Q(1) = -t int_0^1 Q'(1 - t sigma) d sigma (Gauss-Legendre in sigma).
import mpmath as mp
import sympy as sp

def ser_mul(a, b, N):
    return [mp.fsum(a[k]*b[n - k] for k in range(n + 1)) for n in range(N + 1)]
def ser_div(a, b, N):
    c = []
    for n in range(N + 1):
        c.append((a[n] - mp.fsum(b[k]*c[n - k] for k in range(1, n + 1)))/b[0])
    return c
def ser_exp(f, N):   # f[0] = 0
    E = [mp.mpf(1)]
    for n in range(1, N + 1):
        E.append(mp.fsum(k*f[k]*E[n - k] for k in range(1, n + 1))/n)
    return E
def ser_int(f, N):
    return [mp.mpf(0)] + [f[k - 1]/k for k in range(1, N + 1)]
def ser_der(f, N):
    return [(k + 1)*f[k + 1] for k in range(N)] + [mp.mpf(0)]
def ser_binom(p, N):  # (1 - u)^p
    c = [mp.mpf(1)]
    for n in range(1, N + 1):
        c.append(c[-1]*(p - n + 1)/n*(-1))
    return c
def ser_poly(coefs, N):
    c = [mp.mpf(0)]*(N + 1)
    for k, v in enumerate(coefs):
        if k <= N: c[k] = mp.mpf(v)
    return c

class Ref:
    def __init__(self, A, e, qstr, dps=40):
        mp.mp.dps = dps
        self.dps = dps
        self.A = mp.mpf(A); self.e = mp.mpf(e); self.beta = 2/self.A
        u = sp.Symbol('u')
        As = sp.Rational(str(A)) if not isinstance(A, str) else sp.Rational(A)
        qv = sum(sp.Rational(s)*u**(2*k) for k, s in enumerate(qstr))
        om = As*(1 + u)/(1 + u**2) - u**2*(1 - u)*(1 + u)**2*qv
        psin = -As/(1 + u**2) + u*(1 + u)**2*qv
        w0 = -As*u*(1 - u**2)/(1 + u**2) + u**3*(1 - u**2)**2*qv
        assert sp.expand(sp.together(w0 + u*(1 - u)*om)) == 0
        self.sym = dict(u=u, om=om, psin=psin, w0=w0, q=qv)
        L = lambda ex: sp.lambdify(u, ex, modules='mpmath')
        self.om = L(om); self.om1 = L(sp.diff(om, u)); self.om2 = L(sp.diff(om, u, 2))
        self.psin = L(psin); self.psin1 = L(sp.diff(psin, u))
        self.w0 = L(w0); self.w02 = L(sp.diff(w0, u, 2)); self.w03 = L(sp.diff(w0, u, 3))
        # series at 0 (coefficients as mpf from exact rationals)
        self.N = None
        self.Psi_cache = {}
        self.Psi1 = mp.quad(self.psi, [0, mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4, 1])
        self.gl_sig = gl_nodes(30)
        self.setup_Q1()

    def psi(self, u):
        return self.psin(u)/self.om(u)
    def psi1(self, u):
        o = self.om(u)
        return self.psin1(u)/o - self.psin(u)*self.om1(u)/o**2
    def Psi(self, u, t=None):
        # Psi(u) = int_0^u psi; for u > 1/2 use Psi(1) - int_0^t psi(1 - tau) d tau
        if t is None: t = 1 - u
        if u <= mp.mpf(1)/2:
            return mp.quad(self.psi, [0, u])
        return self.Psi1 - mp.quad(lambda tau: self.psi(1 - tau), [0, t])

    def fields(self, u, t=None):
        if t is None: t = 1 - u
        A, e, b = self.A, self.e, self.beta
        Ps = self.Psi(u, t)
        o, o1, o2 = self.om(u), self.om1(u), self.om2(u)
        G = u**2*o*mp.exp(Ps)/A
        lam = 2/u + o1/o + self.psi(u)
        lam1 = -2/u**2 + o2/o - (o1/o)**2 + self.psi1(u)
        w2, w3 = self.w02(u), self.w03(u)
        Q = (G*lam - e*w2)/(2*G**3)
        Qp = (G*(lam**2 + lam1) - e*w3)/(2*G**3) - 3*lam*(G*lam - e*w2)/(2*G**3)
        m = A*t*mp.exp(-Ps)/u
        return dict(G=G, Q=Q, Qp=Qp, m=m, Psi=Ps)

    def series0(self, N):
        # series at 0 of T2 = u^(5+beta) Q' m^(beta-1) and of T1a = u^(5+beta) Q m^(beta-2)/G, T1b = u^beta m^(beta-2)/G
        u = self.sym['u']
        def ps(ex):
            s = sp.series(ex, u, 0, N + 1).removeO()
            P = sp.Poly(s, u)
            c = [mp.mpf(0)]*(N + 1)
            for (k,), v in P.terms():
                c[k] = mp.mpf(sp.Rational(v).p)/mp.mpf(sp.Rational(v).q)
            return c
        A, e, b = self.A, self.e, self.beta
        om = ps(self.sym['om']); psin = ps(self.sym['psin']); w0 = ps(self.sym['w0'])
        psi = ser_div(psin, om, N)
        Ps = ser_int(psi, N)
        EP = ser_exp(Ps, N); EM = ser_exp([-c for c in Ps], N)
        Gh = [c/A for c in ser_mul(om, EP, N)]          # G = u^2 Gh
        Ghp = ser_der(Gh, N)
        # G' = 2u Gh + u^2 Gh';  (G' - e w0'')/u = 2 Gh + u Gh' - e w0''/u
        w02 = ser_der(ser_der(w0, N), N)
        w02u = w02[1:] + [mp.mpf(0)]                     # w0'' is odd
        a2h = [2*Gh[k] + (Ghp[k - 1] if k >= 1 else 0) - e*w02u[k] for k in range(N + 1)]
        Gh3 = ser_mul(ser_mul(Gh, Gh, N), Gh, N)
        Qh = [c/2 for c in ser_div(a2h, Gh3, N)]         # Q = u^(-5) Qh
        Qhp = ser_der(Qh, N)
        Tq = [-5*Qh[k] + (Qhp[k - 1] if k >= 1 else 0) for k in range(N + 1)]   # u^6 Q'
        def mhp(p):   # mh^p, mh = A (1 - u) e^(-Psi)
            Ep = ser_exp([-p*c for c in Ps], N)
            return [A**p*c for c in ser_mul(ser_binom(p, N), Ep, N)]
        T2 = ser_mul(Tq, mhp(b - 1), N)
        mb2G = ser_div(mhp(b - 2), Gh, N)
        T1a = ser_mul(Qh, mb2G, N)
        T1b = mb2G
        self.ser = dict(T2=T2, T1a=T1a, T1b=T1b, Qh=Qh, Gh=Gh)
        self.N = N
        return self.ser

    def fp0(self, delta, which):
        # finite part of int_0^delta of the integrand, termwise from the series
        b = self.beta; s = self.ser
        if which == 'II':
            return mp.fsum(c*delta**(k - 4 - b)/(k - 4 - b) for k, c in enumerate(s['T2']))
        Q1 = self.Q1
        return (mp.fsum(c*delta**(k - 4 - b)/(k - 4 - b) for k, c in enumerate(s['T1a']))
                - Q1*mp.fsum(c*delta**(k + 1 - b)/(k + 1 - b) for k, c in enumerate(s['T1b'])))

    def setup_Q1(self):
        # Q(1): G(1) = om(1) e^Psi(1)/A, lam(1) = 2 + om'(1)/om(1) + psi(1)
        A, e = self.A, self.e
        o = self.om(1); G1 = o*mp.exp(self.Psi1)/A
        lam = 2 + self.om1(1)/o + self.psi(1)
        self.Q1 = (G1*lam - e*self.w02(1))/(2*G1**3)
        self.G1 = G1
        return self.Q1

    def integrand(self, u, t, which):
        f = self.fields(u, t)
        b = self.beta
        if which == 'II':
            return f['Qp']*f['m']**(b - 1)
        if t < mp.mpf(1)/5:
            xs, ws = self.gl_sig
            dQ = -t*mp.fsum(wk*self.fields(1 - t*sk, t*sk)['Qp'] for sk, wk in zip(xs, ws))
        else:
            dQ = f['Q'] - self.Q1
        return dQ*f['m']**(b - 2)/f['G']

_glcache = {}
def gl_nodes(n):
    # Gauss-Legendre nodes and weights on [0, 1] at the current precision (Newton on P_n)
    key = (n, mp.mp.dps)
    if key in _glcache: return _glcache[key]
    xs, ws = [], []
    for i in range(1, n + 1):
        x = mp.cos(mp.pi*(i - mp.mpf(1)/4)/(n + mp.mpf(1)/2))
        for it in range(100):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2*k - 1)*x*p1 - (k - 1)*p0)/k
            dp = n*(x*p1 - p0)/(x**2 - 1)
            dx = p1/dp; x -= dx
            if abs(dx) < mp.mpf(10)**(-mp.mp.dps - 3): break
        p0, p1 = mp.mpf(1), x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2*k - 1)*x*p1 - (k - 1)*p0)/k
        dp = n*(x*p1 - p0)/(x**2 - 1)
        xs.append((1 - x)/2); ws.append(1/((1 - x**2)*dp**2))
    _glcache[key] = (xs, ws)
    return xs, ws

def B_value(R, which, delta, t1=mp.mpf(1)/2, nmid=30, wmid=mp.mpf(1)/20, ns=30, levels=10, ratio=mp.mpf(1)/4):
    b, A = R.beta, R.A
    xs, ws = gl_nodes(nmid)
    tot = R.fp0(delta, which)
    # middle panels
    a = delta; um = 1 - t1
    edges = [a]
    while edges[-1] + wmid < um: edges.append(edges[-1] + wmid)
    edges.append(um)
    mid = mp.mpf(0)
    for lo, hi in zip(edges[:-1], edges[1:]):
        h = hi - lo
        mid += h*mp.fsum(wk*R.integrand(lo + h*xk, 1 - lo - h*xk, which) for xk, wk in zip(xs, ws))
    # end region in s, t = s^(1/beta), s in [0, t1^beta], graded panels toward s = 0
    smax = t1**b
    sed = [smax*ratio**k for k in range(levels)] + [mp.mpf(0)]
    sed = sed[::-1]
    xs2, ws2 = gl_nodes(ns)
    end = mp.mpf(0)
    for lo, hi in zip(sed[:-1], sed[1:]):
        h = hi - lo
        for xk, wk in zip(xs2, ws2):
            s = lo + h*xk
            t = s**(1/b)
            # integrand(u) dt = integrand * (1/beta) s^(1/beta - 1) ds
            end += h*wk*R.integrand(1 - t, t, which)*t/(b*s)
    tot += mid + end
    if which == 'II':
        return tot/(3*A**b), dict(fp0=R.fp0(delta, which), mid=mid, end=end)
    return (b - 1)*A**(1 - b)/3*tot, dict(fp0=R.fp0(delta, which), mid=mid, end=end)
