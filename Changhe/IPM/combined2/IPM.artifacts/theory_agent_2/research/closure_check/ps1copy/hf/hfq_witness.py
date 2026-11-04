# Rational witnesses for the HF-Q self-map test (notes/T2_CEPS_v02a.md section 2), outward Arb arithmetic.
# Loss L_B(R, K) of AT-237 with the exact closed-form constants (not the rounded display) and the four (B, A) pairs
# confirmed by AT-235. For each stipulated input (b0, ||F||_2, beta0) a radius M is chosen by a float search and then
# rounded to a rational with three significant digits; only the Arb evaluation at that rational M is a statement.
# Capacity P(M) = (b0 - L_B(R, cW M)) M with R = ||F||_2/beta0; direct budget D(M) = M (P(M) - N)/R^2 (AT-229).
# Printed values are lower decimals of the Arb enclosures (checked by an Arb comparison). Inputs are stipulated
# numbers, not certified properties of any background or source.
import math
from fractions import Fraction as Fr
from flint import arb, fmpq, ctx
ctx.prec = 200
def A_(x): x = Fr(x); return arb(fmpq(x.numerator, x.denominator))
q, sigma, cW = A_(Fr(21, 10)), A_(Fr(7, 5)), A_(Fr(7441, 5000)); th = (q - 2)/q; pi = arb.pi()
def B_p(p):
    s = (p + 1)/q; t = 1 - s
    return (4*q*(pi*s).sin())**(-0.5)*t**(-t/2)*s**(-s/2)
Csym = B_p(arb(1))/4; Ca = B_p(arb(0))/arb(2).sqrt()
Score = 1/(2*(pi*(q - 1)*(q - 2)).sqrt()); Sw = 1/(2*pi*(q - 1)).sqrt()
def L(t): return sigma*arb(2)**t*((t + 1)/2).gamma()*((t + 3)/2).gamma()
L0, L1, Lq = L(arb(0)), L(arb(1)), L(q)
c53 = A_(Fr(53, 100))
PAIRS = [(Fr(51, 100), Fr(40919, 1000)), (Fr(13, 25), Fr(18959, 1000)), (Fr(11, 20), Fr(673, 100)), (Fr(3, 5), Fr(74, 25))]
def loss(R, K, B, A):
    B, A = A_(B), A_(A)
    return (q*Csym*R**th*K**(1 - th) + c53*Score*K + (sigma/2 + A*L0)*Ca*R**(1 - 1/q)*K**(1/q)
            + B*Sw*((sigma/2)*K + q*arb(2)**(q - 2)*(L1*R**(1/q)*K**(1 - 1/q) + Lq*R)))
def cap(b0, R, M, B, A): M = A_(M); return (A_(b0) - loss(R, cW*M, B, A))*M
def fl(x): return float(x.mid())
def rat3(x):  # three significant digits
    e = math.floor(math.log10(x)) - 2; return Fr(round(x/10**e))*Fr(10)**e
def lowdec(x, digits):  # largest decimal with `digits` significant digits that is certified below x
    v = fl(x.lower()); e = math.floor(math.log10(abs(v))) - digits + 1
    d = Fr(math.floor(v/10**e) - 1)*Fr(10)**e if e < 0 else Fr(math.floor(v/10**e) - 1)*10**e
    while A_(d + Fr(10)**e) < x: d += Fr(10)**e
    assert A_(d) < x
    return d
def best(b0, R, f):  # float search over M and the pairs for the maximum of f(P, M)
    top = None
    for B, A in PAIRS:
        for i in range(1201):
            M = 10**(-3 + 3*i/1200)
            v = f(fl(cap(b0, R, Fr(M), B, A)), M)
            if top is None or v > top[0]: top = (v, M, B, A)
    v, M, B, A = top
    # refine locally
    for _ in range(2):
        lo, hi = M/1.02, M*1.02
        for i in range(81):
            Mi = lo*(hi/lo)**(i/80); vi = f(fl(cap(b0, R, Fr(Mi), B, A)), Mi)
            if vi > v: v, M = vi, Mi
    return M, B, A
if __name__ == "__main__":
    print("prec %d bits. Constants (Arb midpoints): qCsym %.12f, (53/100)Score %.12f, Ca %.12f, Sw %.12f, L0 %.12f, "
          "L1 %.12f, Lq %.12f" % (ctx.prec, fl(q*Csym), fl(c53*Score), fl(Ca), fl(Sw), fl(L0), fl(L1), fl(Lq)))
    beta0 = Fr(209, 100)
    print("\nTable W1. Capacity witnesses P(M) at rational M; columns: b0, ||F||_2, M, B, A, certified lower decimal of P(M)")
    for F2 in (Fr(1, 10**6), Fr(1, 10**5), Fr(3, 10**5)):
        R = A_(F2/beta0)
        for b0 in (Fr(55, 100), Fr(60, 100), Fr(65, 100), Fr(1647, 2500), Fr(70, 100)):
            M, B, A = best(b0, R, lambda P, M: P)
            Mr = rat3(M); P = cap(b0, R, Mr, B, A)
            print("b0 %s | ||F||_2 %s | M %s | B %s A %s | P > %s" % (float(b0), float(F2), float(Mr), B, A, float(lowdec(P, 6))))
    print("\nTable W2. Direct budget witnesses for C0: D(M) = M (P(M) - N)/R^2 at rational M (lower decimal, 3 digits); "
          "'none' if the float maximum of P is <= N")
    for F2 in (Fr(1, 10**6), Fr(1, 10**5), Fr(3, 10**5)):
        Rq = F2/beta0; R = A_(Rq)
        for b0 in (Fr(55, 100), Fr(60, 100), Fr(65, 100), Fr(1647, 2500), Fr(70, 100)):
            cells = []
            for N in (Fr(1, 100), Fr(257, 10000), Fr(5, 100)):
                M, B, A = best(b0, R, lambda P, M: M*(P - float(N)))
                Mr = rat3(M); D = A_(Mr)*(cap(b0, R, Mr, B, A) - A_(N))/R**2
                cells.append("N %s: %s" % (float(N), "none" if not D > 0 else "%.3g (M %s, B %s)" % (float(lowdec(D, 3)), float(Mr), B)))
            print("b0 %s | ||F||_2 %s | " % (float(b0), float(F2)) + " | ".join(cells))
    lam = cW*(c53*Score + Sw*sigma/4)
    print("\nSmall-R coefficients (AT-238): lambda_* = %s; 1/(4 lambda_*) = %s" % (lam.str(12), (1/(4*lam)).str(12)))
