# Budgets available to the H4-REST pieces (T_IS, C_tr, C_vs1 to C_vs3 of D_rem^n) at the two fixed cases of
# NEAR_CHECK_v02/v03, from the printed near tuple (exact rationals) and the route F-a margin of theory_agent_2's
# T2_CLOSURE_CHECK_v02 (B1). Exact rationals except the Lemma HI' constant, which is an arb upper (256 bits).
#   (A) rate room for full-L^2 losses: R(U) = B - e_up - k (U - F), k = (1 + q^2)/(2 mu^2), with
#       B = beta_* - b0 at the regional lower beta_* = 704955805507/10^12 (AT2373, AT2386; not whole-plane), and
#       B = c + 1 - q - b0, the ceiling at the largest rate that AT-211 allows (every beta_* gives at most this).
#   (B) unused free gain for pieces <= C ||J^-1 g||^2: q (s_max - s_*) at s_* = 137/125 (Proposition FG, AT-513).
#   (C) price allowance for C_rest: D_lower - C_N_upper (NEAR_CHECK_v02 printed).
# Also the largest third Fourier moment u_3 of ubar at which the Lemma HI' high-frequency bound of T_IS + C_tr
# alone, phi mu_r^-2 (c_tr' + 5q/2) u_3, fits in R(U) at cut mu_r (tail term dropped, so this is a ceiling).
import json
from fractions import Fraction as Fr
from flint import arb, ctx
ctx.prec = 256
q = Fr(21, 10); c = Fr(4076476460239181, 2251799813685248); F = 8*(2*c - 1)
BETA = Fr(704955805507, 10**12)
FGM = Fr(71675071190082633, 5629499534213120000)        # theory_agent_2 v02 B1 exact margin, = q (s_max - s_*)
r = json.load(open('research/closure_check/near_check_v02.result.json'))
qa = arb(21)/10; l2 = arb(2).log()
ctr = 4*((qa*l2).sinh() - qa*l2.sinh())/l2**3
phi = (1 + arb(5).sqrt())/2
K = ctr + 5*qa/2
print('F = %.10f; c_tr\' = %s; c_tr\' + 5q/2 = %s; phi = %s' % (float(F), ctr.str(10), K.str(10), phi.str(10)))
print('(B) unused free gain q (s_max - s_*) >= %s = %.13f (both cases)' % (FGM, float(FGM)))
for cs in r['cases']:
    b0, mu, e = Fr(cs['b0']), Fr(cs['mu']), Fr(cs['e_up'])
    k = (1 + q**2)/(2*mu**2)
    print('\n%s (b0 %s, mu %s): k = %.9e per unit of U above F' % (cs['label'], cs['b0'], cs['mu'], float(k)))
    print('(C) price allowance D_lower - C_N_upper >= %s' % cs['room_D_minus_P_lower'])
    for name, B in (('regional beta_* 0.704955805507', BETA - b0), ('ceiling beta_* = c + 1 - q', c + 1 - q - b0)):
        R0 = B - e
        print('(A) %s: R(F) = %.12f; R(U) = 0 at U = %.6f' % (name, float(R0), float(F + R0/k)))
        for U in (F, Fr(21), Fr(43, 2), Fr(22), Fr(45, 2), Fr(23), Fr(25), Fr(30)):
            RU = R0 - k*(U - F)
            if RU < 0:
                print('    U = %-10.6f R(U) < 0' % float(U)); continue
            caps = []
            for mr in (72, 100, 200, 400, 1000):
                caps.append('mu_r %d: u_3 <= %s' % (mr, (arb(RU.numerator)/RU.denominator*mr**2/(phi*K)).str(4)))
            print('    U = %-10.6f R(U) = %.12f; %s' % (float(U), float(RU), '; '.join(caps)))
