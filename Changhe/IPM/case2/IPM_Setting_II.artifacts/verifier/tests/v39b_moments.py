"""V39b (referee result 12 results/03-moments): kernel derivatives, integration-by-parts kernels, X.grad phi, regularization,
C_gamma recurrence, gamma = 1 inner flux and matrix A, test-density sign, parity. PASS/FAIL per identity.
Run: OMP_NUM_THREADS=1 python3 tests/v39b_moments.py"""
import numpy as np
import sympy as sp
from scipy import integrate

x, y = sp.symbols('x y', real=True)
r, th = sp.symbols('r theta', positive=True)
lv, m = sp.symbols('l m', real=True)
res = []


def chk(name, expr):
    e = sp.simplify(expr)
    ok = (e == 0)
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), name, '' if ok else e)


def chkn(name, val, ref, tol=1e-9):
    ok = abs(val - ref) <= tol*max(1, abs(ref))
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), name, f'{val:.12g} vs {ref:.12g}')


pol = {x: r*sp.cos(th), y: r*sp.sin(th)}
R2 = x**2 + y**2
# specification kernel K1(Z) = -sin(2 th)/(2 pi |Z|^2) = -z1 z2/(pi r^4)
K1 = -x*y/(sp.pi*R2**2)
d1K1 = sp.diff(K1, x)
d2K1 = sp.diff(K1, y)
# evaluate at Z = -Y: replace (x,y) -> (-x,-y), then Y polar
chk('d_x K1(-Y) = -sin3th/(pi r^3)', sp.simplify(d1K1.subs({x: -x, y: -y}, simultaneous=True).subs(pol)
                                                 + sp.sin(3*th)/(sp.pi*r**3)))
chk('d_y K1(-Y) = +cos3th/(pi r^3)', sp.simplify(d2K1.subs({x: -x, y: -y}, simultaneous=True).subs(pol)
                                                 - sp.cos(3*th)/(sp.pi*r**3)))
# potential route: W1 = (d_1 G) * d_y rho, G = log|Z|/(2 pi); d_x W1(0) = int d_1^2 G(-Y) d_y rho dY
G = sp.log(R2)/(4*sp.pi)
d11G = sp.diff(G, x, 2)
d12G = sp.diff(G, x, y)
chk('d_1^2 G(-Y) = -cos2th/(2 pi r^2) (even)', sp.simplify(d11G.subs({x: -x, y: -y}, simultaneous=True).subs(pol)
                                                         + sp.cos(2*th)/(2*sp.pi*r**2)))
# integration by parts: int k d_y rho = - int rho d_y k + boundary; need -d_y k = d_x K1(-Y), i.e. both routes agree
chk('IBP kernel: -d_y[d_1^2 G(-Y)] = d_x K1(-Y)', sp.simplify(-sp.diff(d11G, y) - d1K1.subs({x: -x, y: -y}, simultaneous=True)))
chk('IBP kernel: -d_y[d_1 d_2 G(-Y)] = d_y K1(-Y)', sp.simplify(-sp.diff(d12G, y) - d2K1.subs({x: -x, y: -y}, simultaneous=True)))
# boundary term of the IBP on r = eps carries d_1^2 G(-Y) n_y ~ cos2th sin th; odd in th -> shear part vanishes
val = integrate.quad(lambda t: abs(np.cos(t))**0.4*np.cos(2*t)*np.sin(t), 0, 2*np.pi, limit=400)[0]
chkn('IBP boundary: int |cos|^g cos2th sin th = 0 (g = 0.4)', val, 0.0, 1e-10)

# phi = r^-3 sin 3th = y(3x^2 - y^2)/r^6, X.grad phi = -3 phi; phi_m homogeneous: X.grad phi_m = -m phi_m
phi = y*(3*x**2 - y**2)/R2**3
chk('phi = r^-3 sin 3th', sp.simplify(phi.subs(pol) - sp.sin(3*th)/r**3))
chk('X.grad phi = -3 phi', x*sp.diff(phi, x) + y*sp.diff(phi, y) + 3*phi)
Phi = sp.Function('Phi')
phim = r**(-m)*Phi(th)
chk('r d_r phi_m = -m phi_m', r*sp.diff(phim, r) + m*phim)
# div(rho V phi) with div(rho V) = (1+2l) rho: (1+2l) rho phi + rho l X.grad phi + rho W.grad phi
rho_s, Wg = sp.symbols('rho Wgradphi')
chk('annulus integrand: (1+2l)phi + l X.grad phi = (1-l) phi', (1 + 2*lv)*phi + lv*(x*sp.diff(phi, x) + y*sp.diff(phi, y))
    - (1 - lv)*phi)

# regularization F_d(t) = (t^2+d^2)^(g/2): F_d'(t) t/g = t^2 (t^2+d^2)^(g/2-1) -> |t|^g, bounded by |t|^g (g<2)
tt = np.linspace(-2, 2, 4001)
ok = True
for gg in (0.3, 0.7, 1.0, 1.5):
    for d in (1e-1, 1e-3, 1e-6):
        v = tt**2*(tt**2 + d**2)**(gg/2 - 1)
        ok &= np.all(v <= np.abs(tt)**gg + 1e-15)
    ok &= np.max(np.abs(tt**2*(tt**2 + 1e-12)**(gg/2 - 1) - np.abs(tt)**gg)) < 1e-5
res.append(bool(ok))
print(('PASS' if ok else 'FAIL'), 'regularization: F_d\'(xi) xi/g <= |xi|^g and -> |xi|^g (g = 0.3, 0.7, 1, 1.5)')
t_ = sp.symbols('t', real=True)
d_, g_ = sp.symbols('d g', positive=True)
Fd = (t_**2 + d_**2)**(g_/2)
chk('regularization: F_d\'(t) t/g = t^2 (t^2+d^2)^(g/2-1)', sp.diff(Fd, t_)*t_/g_ - t_**2*(t_**2 + d_**2)**(g_/2 - 1))

# C_gamma = int |cos|^(2g) sin th sin 3th = 3g/(g+2) int |cos|^(2g) sin^2 ; weighted mean of cos^2 = (2g+1)/(2g+4)
for gg in (0.15, 0.3, 0.5, 0.8, 1.0, 1.7):
    Cg = integrate.quad(lambda t: abs(np.cos(t))**(2*gg)*np.sin(t)*np.sin(3*t), 0, 2*np.pi, limit=400)[0]
    S2 = integrate.quad(lambda t: abs(np.cos(t))**(2*gg)*np.sin(t)**2, 0, 2*np.pi, limit=400)[0]
    C2 = integrate.quad(lambda t: abs(np.cos(t))**(2*gg)*np.sin(t)**2*np.cos(t)**2, 0, 2*np.pi, limit=400)[0]
    I4 = integrate.quad(lambda t: abs(np.cos(t))**(2*gg)*np.cos(4*t), 0, 2*np.pi, limit=400)[0]
    chkn(f'C_g recurrence g={gg}', Cg, 3*gg/(gg + 2)*S2)
    chkn(f'weighted mean cos^2 g={gg}', C2/S2, (2*gg + 1)/(2*gg + 4))
    if gg < 1:
        chkn(f'C_g = -3 I4/(2-2g) (V39 form) g={gg}', Cg, -3*I4/(2 - 2*gg))
    ok = Cg > 0
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), f'C_g > 0 at g={gg}: {Cg:.6f}')
# B_eps of the exact shear from its definition equals -C_g eps^(2g-2)
for gg in (0.3, 0.6):
    e = 1e-3
    l_ = 1/gg
    fB = lambda t: (e*abs(np.cos(t)))**gg*(l_*e - (e*abs(np.cos(t)))**gg*np.sin(t))*np.sin(3*t)
    B = e**-2*sum(integrate.quad(fB, k*np.pi/2, (k + 1)*np.pi/2, limit=400, epsabs=0, epsrel=1e-13)[0] for k in range(4))
    Cg = integrate.quad(lambda t: abs(np.cos(t))**(2*gg)*np.sin(t)*np.sin(3*t), 0, 2*np.pi, limit=400)[0]
    chkn(f'shear B_eps = -C_g eps^(2g-2), g={gg}', B, -Cg*e**(2*gg - 2), 1e-8)

# gamma = 1: shear part of the inner flux and the matrix A
chk('g=1: -int cos^2 sin sin3 = -pi/4', -sp.integrate(sp.cos(th)**2*sp.sin(th)*sp.sin(3*th), (th, 0, 2*sp.pi)) + sp.pi/4)
a11, a12, a21, a22 = sp.symbols('a11 a12 a21 a22', real=True)
Am = sp.Matrix([[a11, a12], [a21, a22]])
e_ = sp.Matrix([sp.cos(th), sp.sin(th)])
inner = sp.integrate(sp.Abs(sp.cos(th))*(lv + (e_.T*Am*e_)[0])*sp.sin(3*th), (th, 0, 2*sp.pi))
chk('g=1: lX + AX part of B_eps has zero angular integral (any A)', inner)
# transport at g=1: (l x + A11 x + A12 y)(1+O(r)) = x + o(r)  => A11 = 1-l, A12 = 0; tr A = 0, A21 = A12
solA = sp.solve([lv + a11 - 1, a12, a11 + a22, a21 - a12], [a11, a12, a21, a22], dict=True)[0]
chk('g=1: A = diag(1-l, l-1)', (Am.subs(solA) - sp.diag(1 - lv, lv - 1)).norm())
chk('g=1: c = -A11 = l - 1 = l - 1/gamma', -solA[a11] - (lv - 1))
chk('g=1: lim Q = pi(l-1)c + pi/4 = pi(l-1)^2 + pi/4', sp.pi*(lv - 1)*(lv - 1) + sp.pi/4 - (sp.pi*(lv - 1)**2 + sp.pi/4))

# test densities xi_t = x A(r)(1 + t y chi): d/dt rho_t = g |xA|^g y chi; angular factor int |cos|^g sin sin3 = C_{g/2} > 0
for gg in (0.3, 0.7, 2.0):
    ang = integrate.quad(lambda t: abs(np.cos(t))**gg*np.sin(t)*np.sin(3*t), 0, 2*np.pi, limit=400)[0]
    ok = ang > 0
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), f'test density angular factor C_(g/2) > 0 at g={gg}: {ang:.6f}')
tq, gq = sp.symbols('t_q g_q', positive=True)
Xa, ych = sp.symbols('xA ychi', positive=True)
chk('test density: d/dt |xA(1+t y chi)|^g at 0 = g |xA|^g y chi', sp.diff((Xa*(1 + tq*ych))**gq, tq).subs(tq, 0)
    - gq*Xa**gq*ych)
# parity: phi(-X) = -phi(X), phi(x,-y) = -phi(x,y)
chk('parity: phi(-X) = -phi(X)', phi.subs({x: -x, y: -y}, simultaneous=True) + phi)
chk('parity: phi(x,-y) = -phi(x,y)', phi.subs(y, -y) + phi)

print(f'SUMMARY {sum(res)}/{len(res)} PASS')
