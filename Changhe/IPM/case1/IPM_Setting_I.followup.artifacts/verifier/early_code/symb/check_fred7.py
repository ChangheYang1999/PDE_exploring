"""verifier: independent checks of fred7 01-frozen and 04-higher-jets (lead verifier/fred7/), requests (g)(ii)-(iv).
Own derivations (the referee's and the lead's scripts were not used).
 (1) conjugation identity (4): (D + c) P = P L_g, c = 2b - 1, P = |zeta|^(2b), g = 2b (A - 1), on the Fourier side for an
     arbitrary symbol V(xi, eta); D-hat = -(A xi d_xi + eta d_eta + A + 1) (checked in check_fred6 (1)).
 (2) homogeneous solutions (10) and Taylor coefficients: (D + c)(r^(-c/A) phi(y r^(-1/A))) = 0 for arbitrary phi, s = -r;
     D(s^i y^j) = (A i + j) s^i y^j; theta_m of (11) and its monotonicity; the smooth solution (6) of (D + c) u_0 = h
     on a non-polynomial h, by quadrature and finite differences.
 (3) fifth-jet example (04 (3)-(7)): Euler identity, degree, kappa range, class exponent 2b - q - 2, thresholds
     alpha_3, alpha_5; G_5 |s|^(4/A) by a physical-space route (absolutely convergent double integral, no Fourier
     moment), against -1/(240 sin(4 pi/A)).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))

# (1)
xi, eta, A, b = sp.symbols('xi eta A b', positive=True)
V = sp.Function('V')(xi, eta)
E = lambda F: A * xi * sp.diff(F, xi) + eta * sp.diff(F, eta)
Dh = lambda F: -(E(F) + (A + 1) * F)                    # symbol action of D = A s d_s + y d_y
g = 2 * b * (A - 1)
c = 2 * b - 1
p = (xi**2 + eta**2)**b
M = xi**2 / (xi**2 + eta**2)
lhs = Dh(p * V) + c * p * V                              # (D + c) P v
rhs = p * (Dh(V) - V - g * M * V)                        # P L_g v
P('(1) (D + c) P - P L_g on an arbitrary symbol V, c = 2b - 1, g = 2b(A-1): residual', sp.simplify(sp.expand(lhs - rhs)))
lhs2 = Dh(p * V) + (c + 1) * p * V
P('(1) control with c -> c + 1: residual', sp.simplify(sp.expand(lhs2 - rhs)), '(nonzero expected)')

# (2)
r, y, s, cc = sp.symbols('r y s c', positive=True)
phi = sp.Function('phi')
u = r**(-cc / A) * phi(y * r**(-sp.Integer(1) / A))
Du = A * r * sp.diff(u, r) + y * sp.diff(u, y)           # s d_s = r d_r for s = -r
P('(2) (D + c) r^(-c/A) phi(y r^(-1/A)): residual', sp.simplify(Du + cc * u))
i_, j_ = sp.symbols('i j', integer=True, nonnegative=True)
mono = s**i_ * y**j_
P('(2) D(s^i y^j) - (A i + j) s^i y^j:', sp.simplify(A * s * sp.diff(mono, s) + y * sp.diff(mono, y) - (A * i_ + j_) * mono))
Av, gv = mp.mpf('10.150725221'), mp.mpf('29.7494907')
bv = gv / (2 * (Av - 1))
cv = 2 * bv - 1
th = [m - (cv + m) / Av for m in range(1, 12, 2)]
P('(2) X3: c = 2b - 1 =', mp.nstr(cv, 10), ' lambda = c/A =', mp.nstr(cv / Av, 10), ' theta_m (m = 1, 3, .., 11):',
  [mp.nstr(t, 6) for t in th], ' increasing:', all(th[i] < th[i + 1] for i in range(len(th) - 1)))
P('(2) X3: t = beta\' - 2b for beta\' in (2, 3) lies in', (mp.nstr(2 - 2 * bv, 6), mp.nstr(3 - 2 * bv, 6)),
  '; theta_1 =', mp.nstr(th[0], 6), '> 0, so the vanishing step after (11) is vacuous at X3 (all theta_m > t)')
# smooth solution (6) on h = y/(1 + s^2) + y^3 s: u_0 = int_{-inf}^0 e^{ct} h(e^{At} s, e^t y) dt
h = lambda S, Y: Y / (1 + S**2) + Y**3 * S
u0 = lambda S, Y: mp.quad(lambda t: mp.exp(cv * t) * h(mp.exp(Av * t) * S, mp.exp(t) * Y), [-mp.inf, -5, 0])
S0, Y0, e = mp.mpf('-0.3'), mp.mpf('0.2'), mp.mpf('1e-8')
Dnum = Av * S0 * (u0(S0 + e, Y0) - u0(S0 - e, Y0)) / (2 * e) + Y0 * (u0(S0, Y0 + e) - u0(S0, Y0 - e)) / (2 * e)
P('(2) (6) at (-0.3, 0.2): (D + c) u_0 - h =', mp.nstr(Dnum + cv * u0(S0, Y0) - h(S0, Y0), 3), '(finite differences, eps 1e-8)')


# (3)
def fifth(Av, gv):
    Av, gv = mp.mpf(Av), mp.mpf(gv)
    bv = gv / (2 * (Av - 1))
    q = 4 / Av
    kap = 2 * bv - 6
    m = 2 * bv - 2
    cb = mp.gamma(1 - bv) / (4**bv * mp.pi * mp.gamma(bv))
    kc = -mp.gamma(1 + kap) * mp.cos(mp.pi * kap / 2) / mp.pi          # F^{-1}[i sgn eta |eta|^kappa], continued
    # d^5/du^5 (1 + u^2)^(m/2) by mpmath differentiation of the closed form (checked against sympy below)
    um = sp.symbols('u', positive=True)
    f5s = sp.lambdify(um, sp.diff((1 + um**2)**(sp.Float(str(m), 40) / 2), um, 5), 'mpmath')
    Cin5 = mp.quad(lambda x: x**(-1 - kap) * f5s(x), [0, 1, 10, mp.inf])
    d5 = cb * (-2 * kc * Cin5) * mp.pi / mp.sin(mp.pi * q)       # d_y^5 v(s, 0) |s|^q
    return dict(b=bv, q=q, kap=kap, cls=2 * bv - q - 2, a3=1 - 2 / Av, a5=3 - 4 / Av, G5=d5 / 120,
                ref=-1 / (240 * mp.sin(4 * mp.pi / Av)), one=4 * mp.pi * kc * cb * Cin5)


Asym, gsym, bsym = sp.symbols('A g b', positive=True)
qs = 4 / Asym
P('(3) Euler constant A(q - 1) + kappa - 2b + A + 2 with q = 4/A, kappa = 2b - 6:', sp.simplify(Asym * (qs - 1) + (2 * bsym - 6) - 2 * bsym + Asym + 2))
P('(3) isotropic degree (q - 1) + kappa - 2b + (d + 2), d = 5 - q:', sp.simplify((qs - 1) + (2 * bsym - 6) - 2 * bsym + (5 - qs) + 2))
for tag, Av, gv in [('rounded 10.1507 / 29.749', '10.1507', '29.749'), ('X3', '10.150725221', '29.7494907')]:
    F = fifth(Av, gv)
    P('(3) %s: q = 4/A %s, kappa %s (in (-3, -2): %s), 2b - q - 2 = %s, alpha_3 %s, alpha_5 %s' % (
        tag, mp.nstr(F['q'], 10), mp.nstr(F['kap'], 10), -3 < F['kap'] < -2, mp.nstr(F['cls'], 12), mp.nstr(F['a3'], 12), mp.nstr(F['a5'], 12)))
    P('(3) %s: G_5 |s|^(4/A) physical route %s ; -1/(240 sin(4 pi/A)) %s ; 4 pi kc c_b C_in5 = %s (claim <=> 1)' % (
        tag, mp.nstr(F['G5'], 15), mp.nstr(F['ref'], 15), mp.nstr(F['one'], 20)))

open('verifier/early_runs/check_fred7.log', 'w').write('\n'.join(out) + '\n')
