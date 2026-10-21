# Frozen kernel at P in Fourier variables. Checks (sympy):
# (1) F[L_g v] = -(A xi d_xi + eta d_eta + A + 2 + g xi^2/|zeta|^2) vhat  (convention vhat = int e^{-i X.zeta} v)
# (2) vhat = Phi(xi/|eta|^A) |eta|^(2b-A-2) |zeta|^(-2b), b = g/(2(A-1)), solves it on eta > 0
# (3) high frequency: on t fixed, |eta| -> inf, vhat ~ Phi(t)|t|^(-2b) |eta|^(-(g+A+2)), quasi-degree -(g+A+2)
# (4) low frequency: vhat ~ Phi(t) |eta|^(-A-2): after d xi = |eta|^A dt the eta-integrand is |eta|^(-2)
# (5) v_d of 6.3.1 (g) is Phi = |t|^(lambda-1), lambda = (d-1)/(A-1): isotropic degree -(d+2)
import sympy as sp
xi, eta, A, g, t, lam, mu = sp.symbols('xi eta A g t lambda mu', positive=True)
b = g/(2*(A-1))
Phi = sp.Function('Phi')
z2 = xi**2 + eta**2
# (1) the Fourier rules: F[s f_s] = -(f^ + xi f^_xi), F[y f_y] = -(f^ + eta f^_eta), F[U_2 f] = -xi^2/z2 f^
f = sp.Function('f')(xi, eta)
Lhat = A*(-(f + xi*sp.diff(f, xi))) + (-(f + eta*sp.diff(f, eta))) - f - g*xi**2/z2*f
target = -(A*xi*sp.diff(f, xi) + eta*sp.diff(f, eta) + (A + 2 + g*xi**2/z2)*f)
print('(1) Fourier form of L_g:', sp.simplify(Lhat - target) == 0)
# (2) on eta > 0
vh = Phi(xi/eta**A)*eta**(2*b - A - 2)*z2**(-b)
res = A*xi*sp.diff(vh, xi) + eta*sp.diff(vh, eta) + (A + 2 + g*xi**2/z2)*vh
print('(2) solves on eta>0:', sp.simplify(res/vh) == 0)
# also with Phi replaced by a generic power, to test the eta<0 branch via eta -> -eta symmetry of the operator
e2 = sp.symbols('e2', negative=True)
vh2 = sp.Function('Psi')(xi/(-e2)**A)*(-e2)**(2*b - A - 2)*(xi**2 + e2**2)**(-b)
res2 = A*xi*sp.diff(vh2, xi) + e2*sp.diff(vh2, e2) + (A + 2 + g*xi**2/(xi**2 + e2**2))*vh2
print('(2b) solves on eta<0:', sp.simplify(res2/vh2) == 0)
# (3) quasi-homogeneous leading term at high frequency: substitute xi = t eta^A, factor
expr = (eta**(2*b - A - 2)*(t**2*eta**(2*A) + eta**2)**(-b))
lead = t**(-2*b)*eta**(-(g + A + 2))
ratio = sp.simplify(sp.powsimp(sp.expand_power_base(expr/lead, force=True), force=True))
print('(3) ratio vhat/lead =', ratio, '-> 1 as eta -> inf since A > 1')
r3 = sp.simplify(ratio.subs({A: sp.Rational(10150725, 1000000)}).subs(eta, 10**8).subs(t, 1).subs(g, 29.75))
print('    numeric ratio at eta=1e8, t=1, X3 values:', sp.N(r3))
# quasi-degree in physical space: v(mu^A s, mu y) = mu^(D - A - 1) v, D = g + A + 2
print('    physical quasi-degree D - A - 1 =', sp.simplify((g + A + 2) - A - 1))
# (4) low frequency
lowlead = eta**(-A - 2)
r4 = sp.simplify(sp.powsimp(sp.expand_power_base(expr/lowlead, force=True), force=True))
print('(4) ratio at low frequency =', r4, '-> 1 as eta -> 0;  times |eta|^A (dxi) gives eta^(-2)')
# (5) v_d
d = sp.symbols('d', positive=True)
lam_d = (d - 1)/(A - 1)
vd = (xi/eta**A)**(lam_d - 1)*eta**(2*b - A - 2)*z2**(-b)
hom = sp.simplify(sp.powsimp(sp.expand_power_base(vd.subs({xi: mu*xi, eta: mu*eta})/vd, force=True), force=True))
print('(5) v_d scaling factor:', sp.simplify(sp.log(hom)/sp.log(mu)), ' (expect -(d+2))')
# exponent of |eta| in 6.3.1 (g): k = 2b - 2 - A*lambda, vhat = |xi|^(-(1 - lambda))... compare:
# here vd = xi^(lam-1) eta^(-A(lam-1) + 2b - A - 2) z2^-b; 6.3.1(g) has a-hat(xi) ~ |xi|^(lam - 1) and |eta|^k
kk = sp.simplify(-A*(lam_d - 1) + 2*b - A - 2 - (2*b - 2 - A*lam_d))
print('    |eta| exponent minus (2b - 2 - A lambda) =', kk)
# regularity numbers at X3
Av = 10.150725; gv = 29.74949
print('X3: b =', gv/(2*(Av-1)), ' (1+g*)/A =', (1+gv)/Av, ' (g*-2)/A =', (gv-2)/Av, ' -2/A =', -2/Av)
# resonance check of the homogeneous extension of the leading term: g*+1 = A a1 + a2 ?
print('resonance values (g*+1) - A a1 for a1=0..3:', [round(gv+1-Av*a1, 4) for a1 in range(4)])
