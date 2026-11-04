# Theorem CE-G and the HF-Q loss for a general weight W = (1 + |X|^2/r0^2)^(sigma/2), q = 21/10, in outward Arb arithmetic
# (python-flint, 200 bits); notes/T2_PS1_v01.md. Same integrals and certificate as research/x4/ce_witness.py, with sigma
# as a parameter and the dilation factors r0^(s-q); the P-S2 case (7/5, 1) is a regression test against that file.
#   K <= N(k) + E(R, K),  E = sum_s r0^(s-q) c_s(sigma; rho1, rho2) X_s,  X_s = R^(1-s/q) K^(s/q),
# with rho1, rho2 in units of r0, and
#   L_B(R, K) = q Csym R^th K^(1-th) + (53/100) Score K + (g + A L0) Ca R^(1-1/q) K^(1/q)
#               + B Sw [g K + q 2^(q-2) (L1 R^(1/q) K^(1-1/q) + Lq R)],   g = sigma/(2 r0),
#   L_t = sigma 2^t Gamma((t+1)/2) Gamma((t+3)/2) r0^(-1-t).
# Inputs b0, beta0, ||F||_2 and N(F) are stipulated numbers, not certified properties of any background or source.
import math, os, sys
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
getcontext().prec = 60
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hf"))
import hfq_witness as H
from flint import arb, fmpq, ctx
ctx.prec = 200
A_, q, pi, fl = H.A_, H.q, H.pi, H.fl
al = q - 2; th = (q - 2)/q
c_al = arb(2)**al*(1 + al/2).gamma()/(pi*abs((-al/2).gamma()))
kap = arb(2)**al*(1 + al/2).gamma()/((1 - al)*(1 - al/2).gamma())
NSUB = 256
def Lw(sg): return 8*sg*125/(216*arb(5).sqrt()) + sg**2/4   # sup |grad w| <= Lw for 0 < sigma <= 4 (crude form, as at P-S2)
def cw(sg): return kap*Lw(sg)**al*(2*sg)**(1 - al)
def Xi(r, sg): return (sg*(r/2).asinh()).exp()
def S(t): return 3*t*t - 2*t**3
def S1(t): return 6*t - 6*t*t
def S2(t): return 6 - 12*t
def ball(lo, hi): return A_(lo).union(A_(hi))
def ub_riemann(f, rho, n=NSUB):
    tot = arb(0)
    for i in range(n):
        lo, hi = rho*(1 + Fr(i, n)), rho*(1 + Fr(i + 1, n))
        r = ball(lo, hi); t = (r - A_(rho))/A_(rho)
        tot += A_(hi - lo)*f(r, t).upper()
    return tot
def phis(r, t, rho):
    rho = A_(rho); e, e1, e2 = S(t), S1(t)/rho, S2(t)/rho**2
    g, g1, g2 = r**(-2 - al), -(2 + al)*r**(-3 - al), (2 + al)*(3 + al)*r**(-4 - al)
    f1 = e1*g + e*g1
    return abs(e*g), abs(f1), abs(e2*g + 2*e1*g1 + e*g2 + f1/r)
def A_n(rho, sg):
    return 2*pi*sg*(A_(rho)**(1 - al)/(1 - al) + ub_riemann(lambda r, t: (1 - S(t))*r**(-al), rho))
def A_f(rho, sg):
    assert 2*rho <= 1
    def f(r, t):
        p0, p1, _ = phis(r, t, rho); return (2*sg*p0 + sg*r*p1)*r
    a = 2*A_(rho)
    return 2*pi*(ub_riemann(f, rho) + 2*sg*a**(-al)/al + sg*(2 + al)*((a**(-al) - 1)/al + 1/(1 + al)))
def I_n(rho, sg):
    return 2*pi*((sg/2)*Xi(A_(rho), sg)*A_(rho)**(1 - al)/(1 - al)
                 + ub_riemann(lambda r, t: (1 - S(t))*(Xi(r, sg) - 1)*r**(-1 - al), rho))
def tail_Xi(a, sg, J=320):
    tot = arb(0); ra = A_(a)
    for j in range(J):
        r0_, r1_ = ra*arb(2)**(arb(j)/8), ra*arb(2)**(arb(j + 1)/8)
        tot += (Xi(r1_, sg) - 1)*(2 + al)*(r0_**(-2 - al) - r1_**(-2 - al))
    T = ra*arb(2)**(arb(J)/8)
    assert sg < 2 + al
    return tot + ((1 + T)/T)**sg*(2 + al)**2*T**(sg - 2 - al)/(2 + al - sg)
def I_f(rho, sg):
    def f(r, t):
        p0, p1, p2 = phis(r, t, rho); return (2*sg*p0 + sg*p1 + (Xi(r, sg) - 1)*p2)*r
    a = 2*A_(rho)
    return 2*pi*(ub_riemann(f, rho) + 2*sg*a**(-al)/al + sg*(2 + al)*a**(-1 - al)/(1 + al) + tail_Xi(2*rho, sg))
CACHE = {}
def cached(f, rho, sgq):
    key = (f.__name__, rho, sgq)
    if key not in CACHE: CACHE[key] = f(rho, A_(sgq))
    return CACHE[key]
class Weight:
    def __init__(self, sgq, r0q, cWq):
        self.sgq, self.r0q, self.cWq = Fr(sgq), Fr(r0q), (None if cWq is None else Fr(cWq))  # cWq None: no c_W known
        self.sg, self.r0 = A_(sgq), A_(r0q)
        self.g = self.sg/(2*self.r0)
        L = lambda t: self.sg*arb(2)**t*((t + 1)/2).gamma()*((t + 3)/2).gamma()*self.r0**(-1 - t)
        self.L0, self.L1, self.Lq = L(arb(0)), L(arb(1)), L(q)
        self.lam1 = H.c53*H.Score + H.Sw*self.g/2
    def consts(self, r1, r2):
        s = self.sgq
        return (cached(A_n, r1, s), cached(A_f, r1, s), cached(I_n, r2, s), cached(I_f, r2, s))
    def coeffs(self, r1, r2):  # c_s of E at r0 = 1 times r0^(s - q), for s = q-1, alpha, 0, 1, 2
        an, af, inn, inf_ = self.consts(r1, r2); sg = self.sg; d = lambda s: self.r0**(s - q)
        return {"qm1": d(q - 1)*sg, "al": d(al)*2*sg,
                "0": d(arb(0))*(cw(sg) + 2*c_al*af + c_al*(2*sg*inn + inf_)),
                "1": d(arb(1))*(2*c_al*an + c_al*sg*inn), "2": d(arb(2))*c_al*inn}
    def E(self, R, K, r1, r2):
        c = self.coeffs(r1, r2); X = lambda s: R**(1 - s/q)*K**(s/q)
        return c["qm1"]*X(q - 1) + c["al"]*X(al) + c["0"]*X(arb(0)) + c["1"]*X(arb(1)) + c["2"]*X(arb(2))
    def Ef(self, R, K, cf):  # float mirror for the searches (FLOAT; only the Arb checks are statements)
        X = lambda s: R**(1 - s/2.1)*K**(s/2.1)
        return cf[0]*X(1.1) + cf[1]*X(0.1) + cf[2]*X(0) + cf[3]*X(1) + cf[4]*X(2)
    def cf_of(self, r1, r2):
        c = self.coeffs(r1, r2); return tuple(fl(c[k]) for k in ("qm1", "al", "0", "1", "2"))
    def Kstar_f(self, R, M, cf):
        lo, hi = M, 2*M + 1
        for _ in range(100):
            mid = (lo + hi)/2
            if mid - M - self.Ef(R, mid, cf) > 0: hi = mid
            else: lo = mid
        return hi
    def best_rhos(self, R, M):
        best = None
        for r1 in RHOS:
            for r2 in RHOS:
                k = self.Kstar_f(R, M, self.cf_of(r1, r2))
                if best is None or k < best[0]: best = (k, r1, r2)
        return best
    def certify_K(self, Rq, M, r1, r2):  # rational Kbar with Kbar - M - E(R, Kbar) > 0 in Arb, or min(that, cW M)
        R = A_(Rq); k = self.Kstar_f(float(Rq), float(M), self.cf_of(r1, r2))
        Kb = Fr(math.ceil(k*(1 + 1e-9)*1e12), 10**12)
        while not (A_(Kb) - A_(M) - self.E(R, A_(Kb), r1, r2) > 0): Kb = Kb*Fr(1000001, 1000000)
        return Kb if self.cWq is None else min(Kb, self.cWq*M)
    def loss(self, R, K, B, A):
        B, A = A_(B), A_(A)
        return (q*H.Csym*R**th*K**(1 - th) + H.c53*H.Score*K + (self.g + A*self.L0)*H.Ca*R**(1 - 1/q)*K**(1/q)
                + B*H.Sw*(self.g*K + q*arb(2)**(q - 2)*(self.L1*R**(1/q)*K**(1 - 1/q) + self.Lq*R)))
    def cap(self, b0, R, Kb, M, B, A): return (A_(b0) - self.loss(R, A_(Kb), B, A))*A_(M)
    def search(self, b0, Rq, kfun, f):  # float search over M and the pairs; kfun(M) gives the float K-input
        top = None; R = A_(Rq)
        for B, A in H.PAIRS:
            for i in range(601):
                M = 10**(-2 + 2*i/600)
                v = f(fl(self.cap(b0, R, Fr(kfun(M)), Fr(M), B, A)), M)
                if top is None or v > top[0]: top = (v, M, B, A)
        v, M, B, A = top
        for _ in range(2):
            lo, hi = M/1.03, M*1.03
            for i in range(61):
                Mi = lo*(hi/lo)**(i/60); vi = f(fl(self.cap(b0, R, Fr(kfun(Mi)), Fr(Mi), B, A)), Mi)
                if vi > v: v, M = vi, Mi
        return M, B, A
RHOS = [Fr(1, 1000), Fr(2, 1000), Fr(4, 1000), Fr(8, 1000), Fr(16, 1000), Fr(32, 1000), Fr(64, 1000)]
def updec(x, d=6): return Fr(math.ceil(Fr(x)*10**d), 10**d)
def dec(x): x = Fr(x); return str(Decimal(x.numerator)/Decimal(x.denominator))
