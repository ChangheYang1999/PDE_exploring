"""v38b: checks for referee result 11 01-forward and 04-cauchy (symmetries, trace, rough solution, centre strain).
Identities that hold for arbitrary functions are tested on explicit non-solution test functions."""
import sympy as sp
import numpy as np

res = []
def chk(name, expr):
    e = sp.simplify(sp.expand(expr))
    ok = (e == 0)
    res.append(ok)
    print(("PASS" if ok else "FAIL"), name, "" if ok else e)

x, y, t = sp.symbols('x y t', real=True)
A, B = sp.symbols('A B', positive=True)

# explicit generic test functions (not solutions)
def rho0(X, Y, T): return sp.sin(X + 2*Y)*sp.exp(T) + X*T**2 + Y**3*T
def u10(X, Y, T): return sp.cos(X*Y) + T*X**2
def u20(X, Y, T): return sp.exp(X - T) + Y*T
def P0(X, Y, T): return X**2*Y + sp.sin(T*Y)

def resid(r, v1, v2, pr):
    return [sp.diff(r, t) + v1*sp.diff(r, x) + v2*sp.diff(r, y),
            v1 + sp.diff(pr, x), v2 + sp.diff(pr, y) + r, sp.diff(v1, x) + sp.diff(v2, y)]

orig = resid(rho0(x, y, t), u10(x, y, t), u20(x, y, t), P0(x, y, t))

# (1) reversal (rho,u,P)(x,t) -> -(rho,u,P)(x,-t): T~ = T(-t), Darcy~ = -Darcy(-t), div~ = -div(-t)
rv = resid(-rho0(x, y, -t), -u10(x, y, -t), -u20(x, y, -t), -P0(x, y, -t))
o_m = [e.subs(t, -t) for e in orig]
chk("01 reversal transport", rv[0] - o_m[0])
chk("01 reversal Darcy1", rv[1] + o_m[1])
chk("01 reversal Darcy2", rv[2] + o_m[2])
chk("01 reversal div", rv[3] + o_m[3])

# (2) scaling rho~ = A rho(Bx,ABt), u~ = A u, P~ = (A/B) P
sc = resid(A*rho0(B*x, B*y, A*B*t), A*u10(B*x, B*y, A*B*t), A*u20(B*x, B*y, A*B*t), A/B*P0(B*x, B*y, A*B*t))
o_s = [e.subs({x: B*x, y: B*y, t: A*B*t}, simultaneous=True) for e in orig]
chk("01 scaling transport (factor A^2 B)", sc[0] - A**2*B*o_s[0])
chk("01 scaling Darcy1 (factor A)", sc[1] - A*o_s[1])
chk("01 scaling Darcy2 (factor A)", sc[2] - A*o_s[2])
chk("01 scaling div (factor AB)", sc[3] - A*B*o_s[3])

# (3) Galilean gauge with linear pressure -z'(t).x
z1 = sp.sin(t) + t**3; z2 = sp.exp(t)
gl = resid(rho0(x - z1, y - z2, t), u10(x - z1, y - z2, t) + sp.diff(z1, t),
           u20(x - z1, y - z2, t) + sp.diff(z2, t),
           P0(x - z1, y - z2, t) - sp.diff(z1, t)*x - sp.diff(z2, t)*y)
o_g = [e.subs({x: x - z1, y: y - z2}, simultaneous=True) for e in orig]
for i, nm in enumerate(["transport", "Darcy1", "Darcy2", "div"]):
    chk("01 Galilean " + nm, gl[i] - o_g[i])

# (4) kernel homogeneity K(BZ) = B^-2 K(Z)  => W[A f(B.)](X) = A W[f](BX)
r2 = x**2 + y**2
K = sp.Matrix([-2*x*y, x**2 - y**2])/(2*sp.pi*r2**2)
chk("01 kernel homogeneity K1", K[0].subs({x: B*x, y: B*y}, simultaneous=True) - K[0]/B**2)
chk("01 kernel homogeneity K2", K[1].subs({x: B*x, y: B*y}, simultaneous=True) - K[1]/B**2)
# kernel = (-d_x d_y Gamma, d_x^2 Gamma), Gamma = -(1/2pi) log r  (U = grad-perp psi, -Lap psi = d_x rho)
G = -sp.log(r2)/(4*sp.pi)
chk("01 kernel K1 = -Gamma_xy", K[0] + sp.diff(G, x, y))
chk("01 kernel K2 = Gamma_xx", K[1] - sp.diff(G, x, 2))

# (5) exponents
l = sp.symbols('ell', positive=True); p = 1/l; a = 1/(l - 1); b = l/(l - 1)
chk("01 a = b p (trace homogeneity)", a - b*p)
chk("01 a - b = -1 (gradient ~ h^-1, centre strain ~ 1/h)", a - b + 1)
# centre strain: grad u_+ = -h^(a-b) DW(0) = diag(c,-c)/h with DW(0)=diag(-c,c)
c, h = sp.symbols('c h', positive=True)
DW0 = sp.diag(-c, c)
chk("04 centre strain", sp.Matrix(-h**(a - b)*DW0 - sp.diag(c, -c)/h).applyfunc(sp.simplify).norm())

# (6) 04: rescaling rho_lam = lam^-p rho(lam x, lam^(1-p) t) is the A,B scaling with A=lam^-p, B=lam
lam, tt, pp = sp.symbols('lambda tau p', positive=True)
chk("04 AB = lam^(1-p)", sp.powsimp(lam**(-pp)*lam - lam**(1 - pp)))
L0 = tt**(-1/(1 - pp))
# exponents of t (lam = t^e, e = -1/(1-p)): lam^(1-p) t has exponent e(1-p)+1; lam^-p has exponent -p e
e_ = -1/(1 - pp)
chk("04 lam^(1-p) t = 1 at lam = t^(-1/(1-p)) (exponent)", e_*(1 - pp) + 1)
chk("04 prefactor lam^-p = t^(p/(1-p)) (exponent)", -pp*e_ - pp/(1 - pp))
chk("04 spatial argument lam x = x/t^(1/(1-p)) (exponent)", e_ + 1/(1 - pp))

# (7) 04: rough stationary IPM solution rho=-|x|^p, u=(0,|x|^p), P=0 ; both sides of x=0
s = sp.symbols('s', positive=True)
for sgn, X1 in [(+1, s), (-1, -s)]:
    absx = s**pp
    rr = -absx; v1 = sp.Integer(0); v2 = absx
    # derivatives in x: d/dx = sgn d/ds
    rx = sgn*sp.diff(rr, s); v2x = sgn*sp.diff(v2, s)
    chk(f"04 rough sol transport (side {sgn})", v1*rx + v2*0)        # rho_y = 0, rho_t = 0
    chk(f"04 rough sol Darcy2 u2 + P_y + rho (side {sgn})", v2 + 0 + rr)
    chk(f"04 rough sol curl u = -rho_x (side {sgn})", v2x - 0 + rx)
    chk(f"04 rough sol conservative flux d_y(rho u2)=0 (side {sgn})", sp.diff(rr*v2, y))

# (8) 01: |u_+| <= C(1+|log t|) on compacts: h^a (1+|x|/h^b)^p log(2+|x|/h^b) bounded by C(1+|log h|)
lv = 1.7; av = 1/(lv - 1); bv = lv/(lv - 1); pv = 1/lv
hs = np.logspace(-12, 0, 200); xs = np.linspace(0, 3, 61)
ratio = max(np.max(hs**av*(1 + xx/hs**bv)**pv*np.log(2 + xx/hs**bv)/(1 + abs(np.log(hs)))) for xx in xs)
ok = ratio < 50
res.append(ok); print(("PASS" if ok else "FAIL"), "01 log bound on velocity (max ratio %.3f)" % ratio)

# (9) 01: Holder exponent min(p,delta) of F=r^p A(theta) near vertex, numeric sample with A=|sin|^delta
rng = np.random.default_rng(0)
for pv_, dv in [(0.6, 0.3), (0.4, 0.8)]:
    def F(P):
        r = np.hypot(P[..., 0], P[..., 1]); th = np.arctan2(P[..., 1], P[..., 0])
        return r**pv_*(np.abs(np.sin(th))**dv + 0.5)
    P1 = rng.uniform(-1, 1, (200000, 2)); P2 = P1 + rng.normal(0, 1, (200000, 2))*10**rng.uniform(-6, 0, (200000, 1))
    ex = min(pv_, dv)
    q = np.abs(F(P1) - F(P2))/np.linalg.norm(P1 - P2, axis=1)**ex
    ok = np.max(q) < 20
    res.append(ok); print(("PASS" if ok else "FAIL"), f"01 Holder quotient exponent min(p,delta), p={pv_}, delta={dv}: max {np.max(q):.3f}")

print("SUMMARY: %d/%d PASS" % (sum(res), len(res)))
