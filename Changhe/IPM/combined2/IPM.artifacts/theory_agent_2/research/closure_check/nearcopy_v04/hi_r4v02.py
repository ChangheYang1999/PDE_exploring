# Rate room R, HI' u_3 ceilings and the least cut mu_min at the (R4) v02 inputs (theory_agent_2 T2_NEAR_R4_v02, Proposition R4,
# UNAUDITED), from the printed e_up of near_check_v03.py on near_params_v03.json (near_check_v04.out); R = beta - b0
# - e_up exactly; ceiling(mu_r) = R mu_r^2/(phi K), K = c_tr' + 5q/2; mu_min = (u3lo phi K/R)^(1/2) with the exact
# origin lower u3lo = 1024389316421/10^12 (numerical_audit AN725; theory_audit AT2457, which needs finite moments and valid
# nonunitary inverse derivative formulas). arb, 256 bits; printed as midpoints (radius below 1e-60).
# Usage (lane root): python3 -B research/closure_check/hi_r4v02.py
from fractions import Fraction as Fr
from flint import arb, ctx
ctx.prec = 256
q = Fr(21, 10); c = Fr(4076476460239181, 2251799813685248)
BETA = Fr(704955805507, 10**12)
U3LO = Fr(1024389316421, 10**12)
EUP = {"plan (11/20, 72)": (Fr(11, 20), Fr(154030238822, 10**12)),
       "fallback (103/200, 68)": (Fr(103, 200), Fr(181864800240, 10**12))}
A = lambda f: arb(f.numerator)/f.denominator
qa = arb(21)/10; l2 = arb(2).log()
ctr = 4*((qa*l2).sinh() - qa*l2.sinh())/l2**3
phi = (1 + arb(5).sqrt())/2
K = ctr + 5*qa/2
print("K = c_tr' + 5q/2 =", K.str(15, radius=False))
for case, (b0, e) in EUP.items():
    for name, beta in (("regional beta_* lower", BETA), ("ceiling c + 1 - q", c + 1 - q)):
        R = beta - b0 - e
        print("%s, %s: R = %s = %.12e" % (case, name, R, float(R)))
        print("   u_3 ceilings: " + "; ".join("mu_r %d: %s" % (mr, (A(R)*mr**2/(phi*K)).str(10, radius=False))
                                                for mr in (72, 100, 140, 200, 400, 1000)))
        m = (A(U3LO)*phi*K/A(R)).sqrt()
        print("   mu_min at u_3 >= 1024389316421/10^12: %s" % m.str(12, radius=False))
