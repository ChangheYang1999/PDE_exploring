# Independent symbolic and grid checks for Proposition 2.6 / Section 9.23 (report preview 9e5c0463).
# Written by verifier; does not use the lead analyst's or the referee's code.
import sympy as sp, random
from fractions import Fraction as Fr
t, g, d, p, k = sp.symbols('t gamma delta p k', positive=True)
ok = []
# Step 2: int_{|T|<=2} |log|T|| dT and the constant (1/(2pi)) * that integral
I = 2*sp.pi*(sp.integrate(-t*sp.log(t), (t, 0, 1)) + sp.integrate(t*sp.log(t), (t, 1, 2)))
ok.append(('step2 integral', sp.simplify(I - 2*sp.pi*(2*sp.log(2) - sp.Rational(1, 2))) == 0))
c = sp.N(I/(2*sp.pi), 20); ok.append(('step2 coeff %.12f < 0.9' % c, c < 0.9))
ok.append(('step2 total 2*0.9+1 < 3', 2*sp.Rational(9, 10) + 1 < 3))
# Step 3: theta = (3-gamma-delta)/2, q - theta = gamma - 2 + theta = kappa
q = 1 - d; th = (3 - g - d)/2; kap = (g - 1 - d)/2
ok.append(('step3 q-theta', sp.simplify(q - th - kap) == 0))
ok.append(('step3 gamma-2+theta', sp.simplify(g - 2 + th - kap) == 0))
# Step 7 identity
ok.append(('step7 2d+(1-d)p = 2-q(2-p)', sp.expand(2*d + (1 - d)*p - (2 - q*(2 - p))) == 0))
ok.append(('step7 gap', sp.expand((p + 1 + d) - (2*d + (1 - d)*p) - (1 - d + d*p)) == 0))
# Step 8 critical gaps
ok.append(('step8 gap1', sp.expand(2*d + (1 - d)*g - g - d*(2 - g)) == 0))
ok.append(('step8 gap2', sp.expand(3*d + 2*g - 1 - g - (3*d + g - 1)) == 0))
# Rational grid: equivalences of Step 6, implication of Step 7, existence of k, ranges of Step 8
random.seed(20261019)
n = nc = 0; bad = []
for _ in range(20000):
    G = Fr(random.randint(100, 199), 100)            # gamma in [1, 2)
    D = Fr(random.randint(1, 100), 100)              # delta in (0, 1]
    P = Fr(random.randint(1, int(G*100)), 100)       # p in (0, gamma]
    B = 1/P; Q = max(P/2, 1 - D); K = (G - 1 - D)/2
    n += 1
    e1 = (P > Q + G - 1) == (B*G < 1 + min(B - Fr(1, 2), B*D))
    e2 = (P > Q + K) == ((G < P + 1 + D) and (G < 2*P - 1 + 3*D))
    cond = G < min(2*D + (1 - D)*P, 3*D + 2*P - 1)
    imp = (not cond) or (P > Q + K)
    kk = True
    if cond:
        nc += 1
        lo, hi = 1 - D, (2 - G)/(2 - P)
        kk = lo < hi <= 1
        km = (lo + hi)/2
        kk = kk and 0 < km < 1 and km*P > G - 2 + 2*km
    r8 = True
    if D >= (G + 1)/3 or P == G:
        r8 = cond
    if not (e1 and e2 and imp and kk and r8):
        bad.append((G, D, P))
ok.append(('grid %d points, %d satisfy (c), failures %d' % (n, nc, len(bad)), not bad))
for name, v in ok:
    print('%-55s %s' % (name, v))
print('ALL', all(v for _, v in ok))
