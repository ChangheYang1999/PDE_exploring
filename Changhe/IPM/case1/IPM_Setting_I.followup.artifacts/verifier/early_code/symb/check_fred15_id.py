"""verifier: fred15 03-quantitative-exclusion, the exact identities (7), (9) and the representation (28) of B_3.
(a) sympy: with z = -w/(A x), E' = (1/z - 1)/x, g = x^2 z e^E, m = A e^(-E)/x:
    compatibility w g' = (w' - A) g, m = -w/g, dm/dx = -A/g, and identity (9)
    (Q - Q*) m^(beta-2)/g = A^(beta-2) (x^(-5-beta) T - Q* x^(-beta) V),  Q = (g' - w'')/(2 g^3).
(b) mpmath: B_3 by (28) with the finite part (10), for
    - R12 references (A, L) = (4, 4) [claimed (23/110592) B(7/4,1/2)] and (10.15, 8.6) [closed form (38)-(39)],
    - a non-R12 odd trace w = w_R12 + eps x^3 (L^2 - x^2)^2, at three split radii r (value must not depend on r)."""
import sympy as sp, mpmath as mp
mp.mp.dps = 40
x, A, be, Qs = sp.symbols('x A beta Q_s', positive=True)
z = sp.Function('z')(x)
E = sp.Function('E')(x)
w = -A*x*z
subsE = {sp.Derivative(E, x): (1/z - 1)/x}
g = x**2*z*sp.exp(E)
m = A*sp.exp(-E)/x
def D(f): return sp.diff(f, x).subs(subsE)
print('(a) compatibility residual:', sp.simplify(w*D(g) - (D(w) - A)*g))
print('    m + w/g =', sp.simplify(m + w/g), '   dm/dx + A/g =', sp.simplify(D(m) + A/g))
gp = D(g); wpp = D(D(w))
Q = (gp - wpp)/(2*g**3)
Dz = x*sp.diff(z, x); J = 2*sp.diff(z, x)/x + sp.diff(z, x, 2)
print('    J + w\'\'/(A x) =', sp.simplify(J + wpp/(A*x)))
T = z**-4/2*(sp.exp(-(be+1)*E)*(1 + z + Dz) + A*sp.exp(-(be+2)*E)*J)
V = sp.exp((1-be)*E)/z
lhs = (Q - Qs)*m**(be-2)/g
rhs = A**(be-2)*(x**(-5-be)*T - Qs*x**(-be)*V)
print("    identity (9): lhs/rhs - 1 =", sp.simplify(sp.powsimp(sp.expand_power_base(lhs/rhs, force=True), force=True).subs(E, sp.Symbol("e0", real=True)).rewrite(sp.exp) - 1))

# (b) numerics.  g = x^2 exp(int_0^x ((w'-A)/w - 2/t) dt) equals x^2 z e^E (checked in (a) via the log-derivative),
# and is finite up to x = L; E = log(g/(x^2 z)) on (0, r].
mp.mp.dps = 30
EE = sp.Symbol('EE')
def B3_28(Av, Lv, eps, r, a0frac='0.03'):
    Av = sp.nsimplify(Av); Lv = sp.nsimplify(Lv); eps = sp.nsimplify(eps)
    bev = 2/Av
    wx = -Av*x*(1 - x**2/Lv**2)/(1 + x**2/Lv**2) + eps*x**3*(Lv**2 - x**2)**2
    zx = sp.cancel(-wx/(Av*x))
    Eser = sp.integrate(sp.series(sp.cancel((1/zx - 1)/x), x, 0, 16).removeO(), x)
    Dzx = x*sp.diff(zx, x); Jx = 2*sp.diff(zx, x)/x + sp.diff(zx, x, 2)
    Tx = zx**-4/2*(sp.exp(-(bev+1)*EE)*(1 + zx + Dzx) + Av*sp.exp(-(bev+2)*EE)*Jx)
    Tser = sp.expand(sp.series(Tx.subs(EE, Eser), x, 0, 16).removeO())
    Tc = {j: mp.mpf(str(sp.N(Tser.coeff(x, j), 45))) for j in range(0, 16)}
    assert all(abs(Tc[j]) < mp.mpf('1e-25') for j in range(1, 16, 2))
    ratio = sp.cancel((sp.diff(wx, x) - Av)/wx)
    f_rr = sp.lambdify(x, sp.cancel(ratio - 2/x), 'mpmath')
    f_ratio = sp.lambdify(x, ratio, 'mpmath')
    f_z = sp.lambdify(x, zx, 'mpmath'); f_w = sp.lambdify(x, wx, 'mpmath')
    f_wpp = sp.lambdify(x, sp.diff(wx, x, 2), 'mpmath')
    f_Dz = sp.lambdify(x, Dzx, 'mpmath'); f_J = sp.lambdify(x, Jx, 'mpmath')
    Am, bm, Lm = [mp.mpf(str(sp.N(v, 45))) for v in (Av, bev, Lv)]
    rm = mp.mpf(r)
    def gfun(xx): return xx**2*mp.e**mp.quad(f_rr, [0, xx])
    def Efun(xx): return mp.log(gfun(xx)/(xx**2*f_z(xx)))
    def Q(xx):
        gg = gfun(xx); return (gg*f_ratio(xx) - f_wpp(xx))/(2*gg**3)
    Qst = Q(Lm)
    def Tfun(xx):
        Ee = Efun(xx); zz = f_z(xx)
        return zz**-4/2*(mp.e**(-(bm+1)*Ee)*(1 + zz + f_Dz(xx)) + Am*mp.e**(-(bm+2)*Ee)*f_J(xx))
    def Vfun(xx): return mp.e**((1-bm)*Efun(xx))/f_z(xx)
    FP = sum(Tc[j]*rm**(j-4-bm)/(j-4-bm) for j in (0, 2, 4))
    a0 = rm*mp.mpf(a0frac)
    FP += sum(Tc[j]*a0**(j-4-bm)/(j-4-bm) for j in range(6, 16, 2))
    FP += mp.quad(lambda xx: xx**(-5-bm)*(Tfun(xx) - Tc[0] - Tc[2]*xx**2 - Tc[4]*xx**4), [a0, rm/3, rm])
    origin = FP - Qst*mp.quad(lambda xx: xx**(-bm)*Vfun(xx), [0, rm])
    tail = mp.quad(lambda xx: (Q(xx) - Qst)*(-f_w(xx)/gfun(xx))**(bm-2)/gfun(xx), [rm, (rm+Lm)/2, Lm])
    # cross-check of Tfun against the series at a0
    chk = Tfun(a0) - sum(Tc[j]*a0**j for j in range(0, 16, 2))
    return (bm-1)/(3*Am)*origin + (bm-1)*Am**(1-bm)/3*tail, chk

def closed(Av, Lv):
    Am, Lm = mp.mpf(Av), mp.mpf(Lv); bm = 2/Am
    C = (16-bm)/(3*Am*(4+bm))*mp.beta(2-bm/2, bm); S = 6*Am*(4*Am-3)/(8*Am-1)
    return C*Lm**(-4-bm)*(1 - S/Lm**2)

print('(b) claimed A=4 L=4 value (23/110592) B(7/4,1/2) =', mp.nstr(mp.mpf(23)/110592*mp.beta(mp.mpf(7)/4, mp.mpf(1)/2), 25))
print('    closed (38)-(39) at A=4 L=4                 =', mp.nstr(closed(4, 4), 25))
import time
for (Av, Lv) in [('4', '4'), ('10.15', '8.6')]:
    for r in ('0.25', '0.5'):
        t0 = time.time(); v, chk = B3_28(Av, Lv, 0, r)
        print('   R12 A=%s L=%s r=%s  B3(28) = %s   closed (38) = %s   rel %s  [series chk %s, %.0fs]' % (Av, Lv, r, mp.nstr(v, 20), mp.nstr(closed(Av, Lv), 20), mp.nstr(abs(v/closed(Av, Lv)-1), 3), mp.nstr(chk, 3), time.time()-t0), flush=True)
for r in ('0.25', '0.5', '1'):
    t0 = time.time(); v, chk = B3_28('4', '4', '0.001', r)
    print('   non-R12 A=4 L=4 eps=1e-3 r=%s  B3(28) = %s  [series chk %s, %.0fs]' % (r, mp.nstr(v, 20), mp.nstr(chk, 3), time.time()-t0), flush=True)
