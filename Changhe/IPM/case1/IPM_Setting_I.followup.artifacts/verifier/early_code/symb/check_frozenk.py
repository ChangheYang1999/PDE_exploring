"""D31: frozen kernel at P in Fourier variables (FINAL_REPORT 6.4 'The frozen kernel at P'); D30: normalization k."""
import sympy as sp
xi, eta = sp.symbols('xi eta', positive=True)   # eta > 0 branch; eta < 0 by oddness
A, gs = sp.symbols('A g_star', positive=True)
b = gs/(2*(A - 1))
Phi = sp.Function('Phi')
z2 = xi**2 + eta**2
vh = Phi(xi/eta**A)*eta**(2*b - A - 2)*z2**(-b)
# operator from FT of L_g v = (A s d_s + y d_y - 1) v + g* U_2[v], U_2 symbol -xi^2/|zeta|^2,
# FT(s d_s v) = -(v^ + xi d_xi v^), FT(y d_y v) = -(v^ + eta d_eta v^)
Lh = -(A*(vh + xi*sp.diff(vh, xi)) + (vh + eta*sp.diff(vh, eta)) + vh + gs*xi**2/z2*vh)
print('FT(L_g v) for the stated v^ (should be 0):', sp.simplify(Lh/vh))
# the stated operator form
op = A*xi*sp.diff(vh, xi) + eta*sp.diff(vh, eta) + (A + 2 + gs*xi**2/z2)*vh
print('stated operator applied (should be 0):', sp.simplify(op/vh))
# family Phi(t) = t^(lambda-1) reproduces 6.3.1 (g): v^ = xi^(lambda-1) eta^k (xi^2+eta^2)^(-b), k = 2b - 2 - A lambda
lam = sp.symbols('lambda', positive=True)
v_fam = (xi/eta**A)**(lam - 1)*eta**(2*b - A - 2)*z2**(-b)
v_g = xi**(lam - 1)*eta**(2*b - 2 - A*lam)*z2**(-b)
print('family vs 6.3.1 (g) exponents (should be 0):', sp.simplify(sp.expand_power_base(v_fam/v_g, force=True)))
# D30: normalization. H_3 = A^beta g^(3+beta) |w|^(-beta), near P: g -> g*, |w| ~ A|s|  =>  H_3 ~ g*^(3+beta) |s|^(-beta)
beta = 2/A
s = sp.symbols('s', positive=True)
H3P = A**beta*gs**(3 + beta)*(A*s)**(-beta)
print('H_3 near P / (g*^(3+beta) s^-beta) =', sp.simplify(sp.expand_power_base(H3P/(gs**(3 + beta)*s**(-beta)), force=True)))
# V of 6.3.1 (g): left G_3 = |s|^(-beta)/(12 sin(pi beta)); right term -(s^-beta/(6 pi)) y^3 log|y|
# normalized V_n = V / (G_3/H_3 limit) = V * 12 sin(pi beta) g*^(3+beta)
kk = -(1/(6*sp.pi))*12*sp.sin(sp.pi*beta)*gs**(3 + beta)
print('k (normalized right log coefficient) =', sp.simplify(kk), ' stated: -2 sin(pi beta) g*^(3+beta)/pi; diff =',
      sp.simplify(kk + 2*sp.sin(sp.pi*beta)*gs**(3 + beta)/sp.pi))
# quasi-homogeneity: v^(mu^A xi, mu eta) = mu^(-N) v^ for Phi compactly supported in t (high frequency, |xi| >> |eta|)
mu = sp.symbols('mu', positive=True)
lead = Phi(xi/eta**A)*eta**(2*b - A - 2)*xi**(-2*b)    # |zeta|^(-2b) ~ |xi|^(-2b) when |xi| ~ eta^A >> eta (A > 1)
ratio = sp.simplify(sp.expand_power_base(lead.subs({xi: mu**A*xi, eta: mu*eta}, simultaneous=True)/lead, force=True))
print('high-frequency quasi-degree: ratio =', sp.simplify(sp.powsimp(sp.expand_log(sp.log(ratio), force=True))/sp.log(mu)))
