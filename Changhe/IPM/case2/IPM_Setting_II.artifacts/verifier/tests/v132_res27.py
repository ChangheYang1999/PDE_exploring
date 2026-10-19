# V132: symbolic checks of the algebraic steps in referee result 27 (Prop 3.10, Theorem 3.11, far-field 3.8(e)) and draft 9.6.
import sympy as sp
ok = []
def chk(name, cond):
    ok.append(bool(cond)); print(('OK  ' if cond else 'FAIL ') + name)
l, sig, eps, u0, v0, D, k, tau = sp.symbols('l sigma epsilon u0 v0 D k tau', positive=True)
b = 2*l + sig
# 1. linear passage model: u' = b u, v' = -sigma v, from (eps, v0) to (u0, tau); rho(exit) = e^T rho(entry)
T = sp.log(u0/eps)/b
tau_e = v0*sp.exp(-sig*T)
chk('tau_eps = v0 (eps/u0)^(sigma/b)', sp.simplify(sp.expand_log(sp.log(tau_e) - sp.log(v0*(eps/u0)**(sig/b)), force=True)) == 0)
eps_t = u0*(tau/v0)**(b/sig)
rho_exit = sp.exp(sp.log(u0/eps_t)/b)*D*eps_t**k
expo = sp.simplify(sp.diff(sp.expand_log(sp.log(rho_exit), force=True), tau)*tau)
chk('q_k = (k b - 1)/sigma', sp.simplify(expo - (k*b - 1)/sig) == 0)
q2 = ((2*b - 1)/sig)
chk('q_2 = 2 + (4l - 1)/sigma', sp.simplify(q2 - (2 + (4*l - 1)/sig)) == 0)
# 2. Taylor fact: dead side forces q_2 > m, i.e. sigma < (4l-1)/(m-2) for m >= 3
m = sp.symbols('m', positive=True)
chk('q_2 > m  <=>  sigma < (4l-1)/(m-2) (m > 2)', sp.simplify((q2 - m)*sig - ((4*l - 1) - (m - 2)*sig)) == 0)
# 3. monomial weights at the saddle, operator (b u d_u - sigma v d_v)
u, v = sp.symbols('u v')
def wt(i, j):
    f = u**i*v**j
    return sp.simplify((b*u*sp.diff(f, u) - sig*v*sp.diff(f, v))/f)
w2 = [wt(2, 0), wt(1, 1), wt(0, 2)]
chk('degree-2 weights 2b, 2l, -2 sigma', [sp.simplify(w2[0] - 2*b), sp.simplify(w2[1] - 2*l), sp.simplify(w2[2] + 2*sig)] == [0, 0, 0])
w3 = [sp.simplify(wt(3 - j, j)) for j in range(4)]
chk('degree-3 weights 3b, 4l + sigma, 2l - sigma, -3 sigma', [sp.simplify(w3[0] - 3*b), sp.simplify(w3[1] - (4*l + sig)), sp.simplify(w3[2] - (2*l - sig)), sp.simplify(w3[3] + 3*sig)] == [0, 0, 0, 0])
chk('only uv^2 resonant, at sigma = 2l - 1', sp.solve(sp.Eq(w3[2], 1), sig) == [2*l - 1])
# counterexample rho = u v^2, V = ((4l-1)u, -(2l-1)v)
V1, V2 = (4*l - 1)*u, -(2*l - 1)*v
rho = u*v**2
chk('counterexample: V.grad rho = rho', sp.simplify(V1*sp.diff(rho, u) + V2*sp.diff(rho, v) - rho) == 0)
chk('counterexample: div V = 2l', sp.simplify(sp.diff(V1, u) + sp.diff(V2, v) - 2*l) == 0)
# uv^2 killed: graph u = h_s(v) = O(v^2), d_u rho = c v^2 + o(v^2) on the branch
c, a2 = sp.symbols('c a2')
hs = a2*v**2
chk('d_u(c u v^2) on u = a2 v^2 equals c v^2', sp.simplify(sp.diff(c*u*v**2, u).subs(u, hs) - c*v**2) == 0)
# 4. Theorem 3.11(b): q_m = q_2 forces m = 2; q_2 = N gives sigma = (4l-1)/(N-2)
N = sp.symbols('N', positive=True)
chk('q_m = q_2  =>  m = 2', sp.solve(sp.Eq((m*b - 1)/sig, q2), m) == [2])
chk('q_2 = N  =>  sigma = (4l-1)/(N-2)', sp.simplify(sp.solve(sp.Eq(q2, N), sig)[0] - (4*l - 1)/(N - 2)) == 0)
# sign: d K = (-1)^N C0 with K, C0 > 0
chk('d > 0 iff N even (N = 3..8)', all(((-1)**n > 0) == (n % 2 == 0) for n in range(3, 9)))
# 5. Theorem 3.11(c): W = (-psi_y, psi_x), V = l X + W; on the axis DV = diag(2l - B', B'), B' = l + psi_xy
x, y = sp.symbols('x y')
psi = sp.Function('psi')(x, y)
W = sp.Matrix([-sp.diff(psi, y), sp.diff(psi, x)])
Vf = sp.Matrix([l*x, l*y]) + W
DV = Vf.jacobian([x, y])
chk('DV_22 = l + psi_xy', sp.simplify(DV[1, 1] - (l + sp.diff(psi, x, y))) == 0)
chk('tr DV = 2l (so DV_11 = 2l - DV_22)', sp.simplify(DV.trace() - 2*l) == 0)
chk('B\'(y_Y) = -sigma gives psi_xy(Y) = -(l + sigma)', sp.simplify((-sig) - l + (l + sig)) == 0)
# 6. Theorem 3.11(e): A(Theta) = L^-p f0 with f0(a0) = f0'(a0) = 0 gives A'' = L^-p f0'' / Theta'^2
a, p = sp.symbols('a p', positive=True)
Th = sp.Function('Theta'); L = sp.Function('L'); f0 = sp.Function('f0')
rhs = L(a)**(-p)*f0(a)
F2 = sp.symbols('F2')
chk('first derivative: (A o Theta)\' = (L^-p f0)\' = 0 at a0 when f0 = f0\' = 0',
    sp.simplify(sp.diff(rhs, a).subs(sp.Derivative(f0(a), a), 0).subs(f0(a), 0)) == 0)
r2 = sp.diff(rhs, a, 2).subs(sp.Derivative(f0(a), (a, 2)), F2).subs(sp.Derivative(f0(a), a), 0).subs(f0(a), 0)
chk('second derivative: (L^-p f0)\'\' = L^-p f0\'\' at a0', sp.simplify(r2 - L(a)**(-p)*F2) == 0)
t = sp.symbols('t'); Ag = sp.Function('Ag')
comp2 = sp.diff(Ag(Th(t)), t, 2)
# (A o Theta)'' = A''(Theta) Theta'^2 + A'(Theta) Theta''; with A'(beta) = 0 only the first term remains
print('   (A o Theta)\'\' =', comp2)
# 7. Theorem 3.11(c) live alpha = 1 or 1/3: j = 1/alpha odd -> rho odd under reflection
chk('j = 1/alpha in {1, 3} odd', all(sp.Integer(j) % 2 == 1 for j in (1, 3)))
# 8. I4 periodic solvability: (p+1)^2 - n^2 != 0 for 0 < p < 1
chk('(p+1)^2 - n^2 != 0 for p in (0,1), n = 0..5', all(sp.solve(sp.Eq((p + 1)**2, n**2), p) == [] or all(not (0 < s < 1) for s in sp.solve(sp.Eq((p + 1)**2, n**2), p)) for n in range(6)))
# 9. Section 6: V.n = l(n.X - d) when W.n = -l d
n1, n2, X1, X2, dd = sp.symbols('n1 n2 X1 X2 d')
chk('V.n = l (n.X - d) when W.n = -l d', sp.simplify(l*(n1*X1 + n2*X2) + (-l*dd) - l*(n1*X1 + n2*X2 - dd)) == 0)
# odd reflection: h harmonic, h(s,0) = 0; check on h = Im((s + i z)^3) + 2 s z
s_, z_ = sp.symbols('s z', real=True)
hh = sp.im(sp.expand((s_ + sp.I*z_)**3)) + 2*s_*z_
chk('example h harmonic with h(s,0) = 0', sp.simplify(sp.diff(hh, s_, 2) + sp.diff(hh, z_, 2)) == 0 and sp.simplify(hh.subs(z_, 0)) == 0)
hr = -hh.subs(z_, -z_)
chk('odd reflection agrees with h (h odd in z here)', sp.simplify(hr - hh) == 0)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
