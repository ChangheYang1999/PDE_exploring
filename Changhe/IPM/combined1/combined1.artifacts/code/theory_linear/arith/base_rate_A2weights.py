"""Largest E2 decay rate mu0 that follows from the A2 P7.5 inequalities (5), (6), (10) with the A2 weights
(E2^2 = P^2 + 2^14 a^2 + 2^18 E0^2, E0^2 = b^2 + (20/21) H^2), and the resulting D(b) threshold.
Exact rational Sylvester test. Run: python3 -B base_rate_A2weights.py

Energy lower bound (b <= E0, worst case b = E0 since the b-terms enter with negative sign):
  -Re<Lh,h>_E2 >= (1/2)P^2 - (347/5) a P - 10 e P - 40 a^2 + 2^14 [ (9/10) a^2 - 6 a e + 16 (11/4) e^2 ]
We need this >= mu (P^2 + 2^14 a^2 + 2^18 e^2) for all P, a, e >= 0; sufficient: the symmetric matrix is PSD.
"""
from fractions import Fraction as Fr
import math

def gram(mu):
    W1, W0 = Fr(2**14), Fr(2**18)
    m = [[Fr(1, 2) - mu, -Fr(347, 10), -Fr(5)],
         [-Fr(347, 10), W1*Fr(9, 10) - 40 - W1*mu, -3*W1],
         [-Fr(5), -3*W1, W1*16*Fr(11, 4) - W0*mu]]
    return m

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def psd(mu):
    m = gram(mu)
    d1 = m[0][0]; d2 = m[0][0]*m[1][1]-m[0][1]**2; d3 = det3(m)
    return d1 > 0 and d2 > 0 and d3 > 0

best = None
for k in range(1, 500):
    mu = Fr(k, 1000)
    if psd(mu): best = mu
    else: break
print("largest mu0 = k/1000 with positive definite Gram matrix:", best, "=", float(best))
# A2's own split gives 1/10; check mu0 = 1/4 (clean value)
for mu in (Fr(1,10), Fr(1,5), Fr(1,4), Fr(27,100)):
    print("  mu0 =", mu, "positive definite:", psd(mu))

# D(b) threshold with rate mu0 - Cbg s - cU N_s(k)/sqrt(s), Cbg = 4800, cU = 5 (A2 P8.4 (2), valid 0 < s <= 1/1024)
def plan(mu0, Cbg=4800, cU=5):
    s = mu0/(5*Cbg); mu = mu0 - Cbg*s; r = mu*math.sqrt(s)/(2*cU); eta = mu*mu*math.sqrt(s)/(4*cU)
    cs = 1/(2*math.sqrt(math.pi*s*(1+s))); d = cs*r
    return s, mu, r, eta, d, d/(19/5 - d)
for mu0 in (0.1, float(best)):
    s, mu, r, eta, d, q = plan(mu0)
    print("mu0 %.3f: s %.3e mu %.4f r %.3e eta %.4e  d = c_s r %.2e  contraction K_L d %.2e" % (mu0, s, mu, r, eta, d, q))

# A clean dyadic choice for mu0 = 1/4: s = 2^-17, r = 2^-14 ... check rate and eta = beta r
mu0 = Fr(1, 4)
for (se, re) in ((17, 14), (16, 14), (17, 15), (16, 13)):
    s = Fr(1, 2**se); r = Fr(1, 2**re)
    sq = Fr(1, 2**(se//2)) if se % 2 == 0 else None
    # rough loss 5 r / sqrt(s): use exact sqrt for even exponents, else upper bound via float rounding up
    rough = 5*r*2**(se/2)
    beta = float(mu0 - 4800*s) - rough
    cs = 1/(2*math.sqrt(math.pi*float(s)*(1+float(s))))
    print("s=2^-%d r=2^-%d: rate >= %.5f, eta = rate*r = %.4e, d = %.2e" % (se, re, beta, beta*float(r), cs*float(r)))

# Clean parameter choice for the improved D(b): s = 2^-16, r = 3*2^-15, eta = r/10.
s = Fr(1, 2**16); r = Fr(3, 2**15)
rate = Fr(297, 1000) - 4800*s - 5*r*2**8          # sqrt(s) = 2^-8 exactly
print("improved D(b) with mu0 = 297/1000, s = 2^-16, r = 3*2^-15: rate >=", rate, "=", float(rate), "> 1/10:", rate > Fr(1, 10))
eta = r/10
print("  eta = r/10 =", eta, "=", float(eta), "; gain over 1/1572864: %.2f" % (float(eta)*1572864))
cs = 1/(2*math.sqrt(math.pi*float(s)*(1+float(s))))
print("  d = c_s r = %.4e < 1/100; contraction K_L d = %.3e; slope change |h_y(0)| <= %.4e" % (cs*float(r), cs*float(r)/(3.8-cs*float(r)), cs*float(r)))
print("  component requirements: P %.3e a %.3e b %.3e H %.3e" % (float(eta), float(eta)/128, float(eta)/512, float(eta)/(512*math.sqrt(20/21))))

# Sensitivity of mu0 to the certified top coercivity m2 (A2 (B5): m2 = 1/2), other A2 constants fixed
def psd_m2(mu, m2):
    m = gram(mu); m[0][0] = m2 - mu
    d2 = m[0][0]*m[1][1]-m[0][1]**2
    return m[0][0] > 0 and d2 > 0 and det3(m) > 0
for m2 in (Fr(1,2), Fr(3,5), Fr(7,10), Fr(4,5)):
    best = max(Fr(k,1000) for k in range(1,1000) if psd_m2(Fr(k,1000), m2))
    print("  m2 = %s: largest mu0 = %s; D(b) optimal eta (Cbg 4800, cU 5) = %.3e" % (m2, best, plan(float(best))[3]))

# Audit printout: exact leading principal minors at mu = 297/1000 and 298/1000
for mu in (Fr(297, 1000), Fr(298, 1000)):
    m = gram(mu)
    print("mu =", mu, "minors:", m[0][0], ",", m[0][0]*m[1][1]-m[0][1]**2, ",", det3(m))
