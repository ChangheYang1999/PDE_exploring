# Independent checks for Proposition 2.6(d) / Section 9.23 Step 9 (preview 52b, cc98d57c). verifier; own code.
import sympy as sp, random
from fractions import Fraction as Fr
g, d, p, k, h, R = sp.symbols('gamma delta p k h R', positive=True)
ok = []
# Taylor algebra of (9.23.7), (9.23.8) with a generic quadratic remainder: f(g0 +- h) = f1*(+-h) + c_+- h^2 / 2
f1, cp, cm = sp.symbols('f1 cp cm')
fp = f1*h + cp*h**2/2; fm = -f1*h + cm*h**2/2
ok.append(('9.23.7 sum = (cp+cm) h^2/2', sp.expand(fp + fm - (cp + cm)*h**2/2) == 0))
ok.append(('9.23.8 diff - 2h f1 = (cp-cm) h^2/2', sp.expand(fp - fm - 2*h*f1 - (cp - cm)*h**2/2) == 0))
# exponent: R^(gamma-2+k) = o(R^(k(p-1))) iff gamma - 2 + 2k < kp
ok.append(('exponent identity', sp.expand((k*(p - 1) - (g - 2 + k)) - (k*p - (g - 2 + 2*k))) == 0))
# beta = 1: A_+ Y_+ + A_- (-Y)_+ with A_- = -A_+ equals A_+ Y
Y, Ap = sp.symbols('Y A_p', real=True)
e = Ap*sp.Max(Y, 0) - Ap*sp.Max(-Y, 0) - Ap*Y
ok.append(('p = 1 formula (Y>0, Y<0)', sp.simplify(e.subs(Y, 3)) == 0 and sp.simplify(e.subs(Y, -2)) == 0))
random.seed(1019)
bad = 0; nc = 0; nb = 0
for _ in range(20000):
    G = Fr(random.randint(100, 199), 100); D = Fr(random.randint(1, 100), 100)
    P = Fr(random.randint(1, int(G*100)), 100); q = 1 - D
    cond = G < min(2*D + (1 - D)*P, 3*D + 2*P - 1)
    if D == 1:
        nb += 1
        if not cond: bad += 1           # bounded W_2: every gamma in [1,2), every p in (0, gamma]
    if not cond: continue
    nc += 1
    lo, hi = q, (2 - G)/(2 - P)
    if not (lo < hi <= 1): bad += 1; continue
    k1 = lo + (hi - lo)/3; k2 = lo + 2*(hi - lo)/3
    for kk in (k1, kk2 := k2):
        if not (q < kk < 1 and kk*P > G - 2 + 2*kk and G - 2 + kk < kk*(P - 1)): bad += 1
    if ((k2 - k1)*(P - 1) != 0) != (P != 1): bad += 1
    # p > Q + kappa (Step 6 hypothesis) follows
    if not P > max(P/2, q) + (G - 1 - D)/2: bad += 1
ok.append(('grid 20000, %d satisfy (c), %d with delta = 1, failures %d' % (nc, nb, bad), bad == 0))
for nme, v in ok: print('%-60s %s' % (nme, v))
print('ALL', all(v for _, v in ok))
