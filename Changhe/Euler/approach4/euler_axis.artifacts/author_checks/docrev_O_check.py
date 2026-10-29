# Checks for the v9 revision of ORIGIN_AND_AXIS_REGULARITY.md (independent mathematical review, findings 3, 9, 14).
# Single-threaded sympy, exact arithmetic except where a float is printed for comparison.
# Run: nice python3 checks/docrev_O_check.py ; writes checks/docrev_O_check_output.json
import json, os, time
import sympy as S

t0 = time.process_time()
res = []

def report(name, ok, detail=''):
    res.append({'check': name, 'pass': bool(ok), 'detail': str(detail)})
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + str(detail)) if detail != '' else ''))

x, y, z = S.symbols('x y z', real=True)
r = S.sqrt(x**2 + y**2)
chi = S.Function('chi')
X = chi(x**2 + y**2 + z**2)

# Exact sample points on circles of radius rho (Pythagorean directions, so r is rational).
dirs = [(1, 0), (0, 1), (S.Rational(3, 5), S.Rational(4, 5)), (S.Rational(5, 13), S.Rational(12, 13)),
        (S.Rational(-8, 17), S.Rational(15, 17)), (S.Rational(-3, 5), S.Rational(-4, 5))]

def all_partials(f, m):
    out = []
    for i in range(m + 1):
        d = f
        if i: d = S.diff(d, x, i)
        if m - i: d = S.diff(d, y, m - i)
        out.append(d)
    return out

def degree_test(f, d, m, rho_pair=(1, 4)):
    """f homogeneous of degree d in (x, y), smooth off the axis. Returns (homogeneity ok, angular values at rho=1)."""
    ok, vals = True, []
    r1, r2 = rho_pair
    for D in all_partials(f, m):
        for (cx, sy) in dirs:
            v1 = S.nsimplify(S.simplify(D.subs({x: r1*cx, y: r1*sy})))
            v2 = S.nsimplify(S.simplify(D.subs({x: r2*cx, y: r2*sy})))
            if S.simplify(v2 - S.Integer(r2)**(d - m) * v1 * S.Integer(r1)**(m - d)) != 0:
                ok = False
            vals.append(v1)
    return ok, vals

# ---- Finding 3: U = chi (-y r^3, x r^3, 0) (phi = 0, q = r^3 chi)
Ux, Uy = -y*r**3*X, x*r**3*X
div = S.simplify(S.diff(Ux, x) + S.diff(Uy, y))
report('q = r^3 chi: U = chi(-y r^3, x r^3, 0) is divergence-free', div == 0, div)
f = y*r**3   # transverse factor of U_x (U_y analogous by symmetry), homogeneous of degree 4
ok3, v3 = degree_test(f, 4, 3)
report('y r^3: all third derivatives homogeneous of degree 1 (continuous, zero on the axis), so C^3', ok3)
ok4, v4 = degree_test(f, 4, 4)
nonconst4 = any(S.simplify(a - b) != 0 for a, b in zip(v4[:len(dirs)], v4[1:len(dirs)]))
report('y r^3: fourth derivatives homogeneous of degree 0 and nonconstant on the circle, so not C^4', ok4 and nonconst4)
qs = S.Symbol('s', positive=True)
report('q = r^3 = s^(3/2) is C^1 but not C^2 in s (q_ss = (3/4) s^(-1/2))',
       S.simplify(S.diff(qs**S.Rational(3, 2), qs, 2) - S.Rational(3, 4)*qs**S.Rational(-1, 2)) == 0)

# ---- Finding 3: q = r^(3/2) chi
Vx, Vy = -y*r**S.Rational(3, 2)*X, x*r**S.Rational(3, 2)*X
report('q = r^(3/2) chi: U divergence-free', S.simplify(S.diff(Vx, x) + S.diff(Vy, y)) == 0)
g = y*r**S.Rational(3, 2)  # degree 5/2
ok2, _ = degree_test(g, S.Rational(5, 2), 2)
report('y r^(3/2): second derivatives homogeneous of degree 1/2 (continuous), so C^2', ok2)
ok3b, v3b = degree_test(g, S.Rational(5, 2), 3)
report('y r^(3/2): third derivatives homogeneous of degree -1/2 and not all zero, so unbounded (not C^3)',
       ok3b and any(v != 0 for v in v3b))
rr = S.Symbol('r', positive=True)
report('q = r^(3/2): q_rr = (3/4) r^(-1/2), unbounded at the axis',
       S.simplify(S.diff(rr**S.Rational(3, 2), rr, 2) - S.Rational(3, 4)*rr**S.Rational(-1, 2)) == 0)

# ---- Finding 3: odd radial powers, n = 1 and 3, in q and in phi
for n in (1, 3):
    # q = r^n: swirl velocity r^n (-y, x), degree n + 1: C^n, not C^(n+1)
    h = y*r**n
    okA, _ = degree_test(h, n + 1, n)
    okB, vB = degree_test(h, n + 1, n + 1)
    ncB = any(S.simplify(a - b) != 0 for a, b in zip(vB[:len(dirs)], vB[1:len(dirs)]))
    report(f'q = r^{n}: swirl velocity is C^{n} but not C^{n+1}', okA and okB and ncB)
    # phi = r^n g(z): U^z = 2 phi + 2 s phi_s = (n + 2) r^n g
    sS, G = S.Symbol('s', positive=True), S.Function('g')(z)
    Phi = sS**S.Rational(n, 2)*G
    Uz = S.simplify(2*Phi + 2*sS*S.diff(Phi, sS))
    report(f'phi = r^{n} g(z): U^z = {n + 2} r^{n} g(z)', S.simplify(Uz - (n + 2)*sS**S.Rational(n, 2)*G) == 0)
    okC, _ = degree_test(r**n, n, n - 1) if n > 1 else (True, None)
    okD, vD = degree_test(r**n, n, n)
    ncD = any(S.simplify(a - b) != 0 for a, b in zip(vD[:len(dirs)], vD[1:len(dirs)]))
    report(f'r^{n}: C^{n-1} but not C^{n} in (x, y) (n-th derivatives of degree 0, nonconstant)', okC and okD and ncD)

# ---- Finding 3: invariant scalars (remark on O:10) and the stream gauge
a, b, Cz = S.symbols('a b C')
Uxg, Uyg = x*a - y*b, y*a + x*b
report('x U_x + y U_y = s a and x U_y - y U_x = s b',
       S.expand(x*Uxg + y*Uyg - (x**2 + y**2)*a) == 0 and S.expand(x*Uyg - y*Uxg - (x**2 + y**2)*b) == 0)
th = S.Symbol('theta', real=True)
Rm = S.Matrix([[S.cos(th), -S.sin(th)], [S.sin(th), S.cos(th)]])
P = Rm*S.Matrix([x, y]); W = Rm*S.Matrix([Uxg, Uyg])   # equivariant field: U(Rx) = R U(x), a, b invariant
inv1 = S.simplify(P[0]*W[0] + P[1]*W[1] - (x*Uxg + y*Uyg))
inv2 = S.simplify(P[0]*W[1] - P[1]*W[0] - (x*Uyg - y*Uxg))
report('the two scalars are rotation invariant (U_x, U_y themselves are not)', inv1 == 0 and inv2 == 0 and
       S.simplify(W[0] - Uxg) != 0)
sS = S.Symbol('s', positive=True); C0 = S.Symbol('C0')
Phi = S.Function('Phi')(sS, z)
dPhi = C0/sS
report('gauge: Phi -> Phi + C0/s leaves U^r/r = -Phi_z and U^z = 2 Phi + 2 s Phi_s unchanged',
       S.diff(dPhi, z) == 0 and S.simplify(2*dPhi + 2*sS*S.diff(dPhi, sS)) == 0)

# ---- Finding 9: pole asymptotics from W_z eta = 2 q (q - K) with W_z ~ c z, q ~ C |z|^(-1/c)
c, K, Cp, Z = S.symbols('c K C_p Z', positive=True)
qp = Cp*Z**(-1/c)
eta_up = 2*qp*(qp - K)/(c*Z)                     # z = +Z
lim_up = S.limit(S.simplify(eta_up*Z**(1 + 1/c)).subs(c, S.Rational(3, 5)), Z, S.oo)
eta_dn = 2*qp*(qp - K)/(c*(-Z))                  # z = -Z, |z| = Z
lim_dn = S.limit(S.simplify(eta_dn*Z**(1 + 1/c)).subs(c, S.Rational(3, 5)), Z, S.oo)
report('pole asymptotics (c = 3/5 sample): eta |z|^(1 + 1/c) -> -(2K/c) C_+ at +infinity, +(2K/c) C_- at -infinity',
       S.simplify(lim_up + 2*K*Cp/S.Rational(3, 5)) == 0 and S.simplify(lim_dn - 2*K*Cp/S.Rational(3, 5)) == 0,
       f'{lim_up}, {lim_dn}')

# ---- Finding 14: curvature relation and ratio
q0, h3 = S.symbols('q0 h3', positive=True)
cc = S.Symbol('c', positive=True)
qzz = 6*q0*h3/(cc + 1)
qrr = -3*q0*h3*((cc + 1)**2 + q0**2)/((2*cc - 1)*(cc + 1)**2)
report('curvature relation 4(c - 1/2)(c + 1) q_rr + [(c + 1)^2 + q0^2] q_zz = 0 for the stated q_rr, q_zz',
       S.simplify(4*(cc - S.Rational(1, 2))*(cc + 1)*qrr + ((cc + 1)**2 + q0**2)*qzz) == 0)
ratio = S.sqrt(4*(cc - S.Rational(1, 2))*(cc + 1)/((cc + 1)**2 + q0**2))
report('l_r/l_z = sqrt(|q_zz|/|q_rr|) equals the stated ratio (c > 1/2)',
       S.simplify((S.Abs(qzz)/S.Abs(qrr)).subs(cc, S.Rational(3, 5)) - ratio.subs(cc, S.Rational(3, 5))**2) == 0)
report('ratio decreases in q0 > 0', S.simplify(S.diff(ratio**2, q0) + 8*(cc - S.Rational(1, 2))*(cc + 1)*q0 /
                                           ((cc + 1)**2 + q0**2)**2) == 0)
sup505 = S.sqrt(4*S.Rational(5, 1000)/S.Rational(1505, 1000))
report('supremum at c = 0.505 (q0 -> 0) is sqrt(4(0.005)/1.505) = 2/sqrt(301) = 0.115278...',
       S.simplify(sup505 - 2/S.sqrt(301)) == 0 and S.Rational(115278, 10**6) < sup505 < S.Rational(115279, 10**6),
       S.N(sup505, 12))
report('old wording "about 0.11 or less" understates the supremum (0.115278 > 0.11)', sup505 > S.Rational(11, 100))
v06 = ratio.subs({cc: S.Rational(3, 5), q0: 1})
report('ratio at c = 0.6, q0 = 1 is 4/sqrt(89) = 0.4240 to four decimals',
       S.simplify(v06 - 4/S.sqrt(89)) == 0 and abs(S.N(v06, 15) - S.Rational(4240, 10**4)) < S.Rational(5, 10**5),
       S.N(v06, 12))

# ---- Finding 30: T3 and T2 thresholds stated in section 1
mu, nu = S.symbols('mu nu', positive=True)
delta = 1 + cc
report('T3: k = 1 + delta/mu > 2 iff mu < delta', S.simplify((1 + delta/mu - 2) - (delta - mu)/mu) == 0)
report('T2: j = delta/(2 nu) > 1/2 iff nu < delta, Cartesian degree 2j + 1 > 2',
       S.simplify(delta/(2*nu) - S.Rational(1, 2) - (delta - nu)/(2*nu)) == 0)

# ---- Kernel bound used in 6 (c): |(z - z1) r^3 rho^-5| <= rho^-1
t = S.Symbol('t', real=True)
kern = S.cos(t)*S.sin(t)**3
crit = [S.pi/3, 2*S.pi/3]
report('|cos t sin^3 t| <= 1 (kernel O(rho^-1))', all(abs(S.N(kern.subs(t, tt))) <= 1 for tt in crit + [0, S.pi/2]))

cpu = time.process_time() - t0
npass = sum(1 for e in res if e['pass'])
print(f'{npass}/{len(res)} PASS, cpu {cpu:.1f} s')
out = {'script': 'checks/docrev_O_check.py', 'n_checks': len(res), 'n_pass': npass, 'cpu_seconds': round(cpu, 2),
       'results': res}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docrev_O_check_output.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
