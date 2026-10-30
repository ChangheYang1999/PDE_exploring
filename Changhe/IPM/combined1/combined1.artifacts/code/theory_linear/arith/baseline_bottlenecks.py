"""Arithmetic behind notes/T2_routes_v01.md section 1 (baseline bottlenecks of A2 Theorem D(b) and D_w).
All inputs are constants quoted from A2 = R6/source/analysis2/IPM_Analysis_II.artifacts (S1_PROOFS P7.5, P8.4;
S1_CLOSURE 7a). Exact rationals where possible. Run: python3 -B baseline_bottlenecks.py"""
from fractions import Fraction as Fr
import math

# P8.4 constants and (1): (C,U1,U2,U3,R1,R2,R3,R4) <= (2,6,24,160,22,32,80,2048)
C, U1, U2, U3, R1, R2, R3, R4 = 2, 6, 24, 160, 22, 32, 80, 2048
K00 = 6*C + 28*U1 + 166*U2 + 17*R2
K11 = C + 28*U1 + 149*U2 + 17*R2
K22 = C + 28*U1 + 132*U2 + 17*R2
print("K00 =", K00, " parts 6C,28U1,166U2,17R2 =", 6*C, 28*U1, 166*U2, 17*R2,
      " share of 166U2 = %.3f" % (166*U2/K00))
print("K11 =", K11, " 149U2 =", 149*U2, "  K22 =", K22, " 132U2 =", 132*U2)
print("U2-proportional share of K00+K11+K22: %.3f" % ((166+149+132)*U2/(K00+K11+K22)))

# Threshold of D(b): rate mu0 - Cbg s - cU n/sqrt(s); r = mu sqrt(s)/(2 cU), eta = mu^2 sqrt(s)/(4 cU)
def eta_opt(mu0, Cbg, cU):
    s = mu0/(5*Cbg)          # maximizer of (mu0 - Cbg s)^2 sqrt(s)
    mu = mu0 - Cbg*s
    return s, mu, mu*mu*math.sqrt(s)/(4*cU)
s, mu, eta = eta_opt(0.1, 4800, 5)
print("D(b) optimal: s = %.4e  mu = %.4f  eta = %.4e (A2 P8.4 section 5: 6.53e-7)" % (s, mu, eta))
print("closed form 4/(25 sqrt5) mu0^(5/2)/(cU sqrt(Cbg)) = %.4e" % (4/(25*math.sqrt(5))*0.1**2.5/(5*math.sqrt(4800))))
s3 = Fr(1, 2**18); print("D(b) chosen (3): rate lower bound", Fr(1,10) - 4800*s3 - Fr(5,128), "=", float(Fr(1,10)-4800*s3-Fr(5,128)),
      " eta = 1/1572864 =", 1/1572864)
# component requirements (A2 S1_CLOSURE section 8): P<=eta, a<=eta/128, b<=eta/512, H<=eta/(512 sqrt(20/21))
e = 1/1572864
print("component requirements: P %.3e a %.3e b %.3e H %.3e" % (e, e/128, e/512, e/(512*math.sqrt(20/21))))

# P7.5 base decay: (1/2)P^2 - 72 E1 P - 40 E1^2 and E2^2 = P^2 + W E1^2 with E1 rate 1/2.
# Largest rate mu with the A2 Young split: 2^14 (1/2 - mu) >= 5224
print("P7.5 Young split allows mu <= %.4f (A2 uses 1/10)" % (0.5 - 5224/2**14))
# Optimal split: need 72^2 <= 4 (1/2-mu) (W (1/2-mu) - 40) for given W; minimal W for a target mu
for mu_t in (0.1, 0.2, 0.3, 0.4, 0.45):
    t = 0.5 - mu_t
    W = (72**2/(4*t) + 40)/t
    print("  target base rate %.2f needs E1 weight W >= %.4g (sqrt W = %.1f; A2: W = 2^14, sqrt 128)" % (mu_t, W, math.sqrt(W)))
print("cross coefficient 347/5 = %.1f of which 28*9/5 = %.1f (nonlocal gradient-identity term)" % (347/5, 28*9/5))

# D_w low margin (S1_CLOSURE 7a, smaller radius): mu = 2/5 - R^-d [23 + 16*190 + (11/5)(9*23 + 2*23 + 56/sqrt2)]
br = 23 + 16*190 + 2.2*(9*23 + 2*23 + 56/math.sqrt(2))
d = 4/9
Rmin = (br/(0.4-0.2))**(1/d)
print("D_w bracket = %.1f (16*190 = 3040 share %.3f); margin >= 1/5 needs R >= %.3e = 2^%.2f" % (br, 3040/br, Rmin, math.log2(Rmin)))
print("D_w rate constants 2^23 = %d (vs 4800: x%.0f), 2^19 = %d (vs 5: x%.0f)" % (2**23, 2**23/4800, 2**19, 2**19/5))
