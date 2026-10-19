"""V22 (specification M13, referee result 5): symbolic checks of the referee result 5 formulas, own derivations (sympy).
 (1) 01 Prop 1 (3): residual of T_L rho for a profile, generic smooth rho, W (using only V.grad rho = rho).
 (2) 01 Prop 3: int cos^2 sin sin3 = pi/4 and the strain integral of d_p.
 (3) 02 (13): second Fourier coefficients of Psi_p[A] for A = sum of modes 0..5.
 (4) 02 Lemma 2 local expansions at a quadratic zero.
 (5) 03 (7), (8), (2), (11), (12) and the limit (11a) 19/320; residual cancellation (l-1) B_p = J_p.
 (6) 03 (13): exact singular family rho = a|x|^p.
 (7) M13(d) separation radii eps^(-2/eps).
"""
import sympy as sp
th, t, p, r, L, a, x, y, b = sp.symbols('theta t p r L a x y beta', real=True)
ok = True
def chk(name, expr):
    global ok
    e = sp.simplify(expr)
    print('%-60s %s' % (name, e)); ok &= (e == 0)

# (1) T_L residual. rho, W1, W2 generic functions of Y = X/L; the profile equation is used to eliminate W.grad rho.
X1, X2 = sp.symbols('X1 X2', real=True); c, l = sp.symbols('c ell', real=True)
f = sp.Function('f')(X1/L, X2/L); W1 = sp.Function('W1')(X1/L, X2/L); W2 = sp.Function('W2')(X1/L, X2/L)
lL = sp.Rational(1, 2) + L*c
TL = L**2*f; WT1 = L**2*W1; WT2 = L**2*W2
res = (lL*X1 + WT1)*sp.diff(TL, X1) + (lL*X2 + WT2)*sp.diff(TL, X2) - TL
Y1, Y2 = sp.symbols('Y1 Y2', real=True)
res = res.subs({X1: L*Y1, X2: L*Y2}).doit()
F = sp.Function('f')(Y1, Y2)
fy1 = sp.Derivative(F, Y1); fy2 = sp.Derivative(F, Y2)
# profile: (l Y + W).grad f = f, l = 1/2 + c  ->  W.grad f = f - l Y.grad f
Wgrad = sp.Function('W1')(Y1, Y2)*fy1 + sp.Function('W2')(Y1, Y2)*fy2
res = sp.expand(res)
target = L**2*(L - 1)*(F - (Y1*fy1 + Y2*fy2)/2)
diff = sp.expand(res - target)
diff = diff.subs(sp.Function('W1')(Y1, Y2)*fy1, F - (sp.Rational(1, 2) + c)*(Y1*fy1 + Y2*fy2) - sp.Function('W2')(Y1, Y2)*fy2)
chk('01 (3): T_L residual - L^2(L-1)(rho - Y.grad rho/2)', sp.expand(diff))

# (2)
chk('01 Prop 3: int cos^2 sin sin3 - pi/4', sp.integrate(sp.cos(th)**2*sp.sin(th)*sp.sin(3*th), (th, 0, 2*sp.pi)) - sp.pi/4)

# (3) Psi_p for A = a0 + sum a_j cos j + b_j sin j, j = 1..5: solve mode by mode
aj = sp.symbols('a0:6', real=True); bj = sp.symbols('b0:6', real=True)
A = aj[0] + sum(aj[j]*sp.cos(j*th) + bj[j]*sp.sin(j*th) for j in range(1, 6))
S = sp.expand(sp.expand_trig(p*sp.cos(th)*A - sp.sin(th)*sp.diff(A, th)))
S = sp.fu(sp.expand(sp.trigsimp(S)))
def coef(expr, k, kind):
    g = sp.cos(k*th) if kind == 'c' else sp.sin(k*th)
    return sp.simplify(sp.integrate(sp.expand(expr*g), (th, 0, 2*sp.pi))/sp.pi)
S2c = coef(p*sp.cos(th)*A - sp.sin(th)*sp.diff(A, th), 2, 'c'); S2s = coef(p*sp.cos(th)*A - sp.sin(th)*sp.diff(A, th), 2, 's')
P2c = -S2c/((p + 1)**2 - 4); P2s = -S2s/((p + 1)**2 - 4)
a_1, a_3 = aj[1], aj[3]; b_1, b_3 = bj[1], bj[3]   # A = a_j cos + b_j sin: these ARE the (1/pi) int A cos j coefficients
chk('02 (13) cos2', P2c - (-a_1/(2*(p + 3)) + a_3/(2*(1 - p))))
chk('02 (13) sin2', P2s - (-b_1/(2*(p + 3)) + b_3/(2*(1 - p))))

# (4) Lemma 2 local expansions (A = a t^2 + a3 t^3 polynomial model of the C^2 expansion)
a3s, beta0 = sp.symbols('a3 beta0', real=True)
Aloc = a*t**2 + a3s*t**3
rhs = -sp.cos(beta0 + t)*Aloc + sp.sin(beta0 + t)*sp.diff(Aloc, t)
ser = sp.series(rhs, t, 0, 3).removeO()
chk('02 Lemma 2: t^1 coeff of rhs - 2 a sin(beta)', sp.expand(ser).coeff(t, 1) - 2*a*sp.sin(beta0))
chk('02 Lemma 2: t^2 coeff of rhs at sin beta = 0 (beta = 0)', sp.expand(ser.subs(beta0, 0)).coeff(t, 2) - a)
chk('02 Lemma 2: t^2 coeff of rhs at beta = pi', sp.expand(sp.series(rhs.subs(beta0, sp.pi), t, 0, 3).removeO()).coeff(t, 2) + a)
chk('02 Lemma 2: (A^2)\'\' t^2 coefficient - 12 a^2', sp.expand(sp.diff(Aloc**2, t, 2)).coeff(t, 2) - 12*a**2)

# (5) exterior family
A0 = sp.cos(th)**2
Psi = -(3*p + 2)/(4*p*(p + 2))*sp.cos(th) - sp.cos(3*th)/(4*(p + 4))
chk('03 (7): Psi_p ODE residual', sp.simplify(sp.diff(Psi, th, 2) + (p + 1)**2*Psi + (p*sp.cos(th)*A0 - sp.sin(th)*sp.diff(A0, th))))
chk('03 source identity', sp.simplify(sp.expand_trig(p*sp.cos(th)*A0 - sp.sin(th)*sp.diff(A0, th) - ((3*p + 2)/4*sp.cos(th) + (p - 2)/4*sp.cos(3*th)))))
J = (p + 1)*Psi*sp.diff(A0, th) - p*sp.diff(Psi, th)*A0
Jclaim = sp.sin(th)*sp.cos(th)**2/(p + 4)*(2*(p + 1)/p + (2 - p)*sp.cos(th)**2)
chk('03 (8): J_p - claim', sp.simplify(sp.expand_trig(J - Jclaim)))
# J_p via polar components: H.grad(r^p A) with H = r^p(-Psi' e_r + (p+1) Psi e_th)
Hr = -r**p*sp.diff(Psi, th); Ht = (p + 1)*r**p*Psi; Fd = r**p*A0
chk('03 (8) from H.grad', sp.simplify(sp.expand_trig(Hr*sp.diff(Fd, r) + Ht*sp.diff(Fd, th)/r - r**(2*p - 1)*Jclaim)))
lval = 1/p
Bp = sp.sin(th)*sp.cos(th)**2/((1 - p)*(p + 4))*(2*(p + 1) + p*(2 - p)*sp.cos(th)**2)
chk('03 (2): (l-1) B_p - J_p', sp.simplify((lval - 1)*Bp - Jclaim))
# dilation residual of r^q B, q = 2p-1
q = 2*p - 1
chk('03 dilation: (l X.grad - 1) r^q B + (l-1) r^q B', sp.simplify(lval*r*sp.diff(r**q*Bp, r) - r**q*Bp + (lval - 1)*r**q*Bp))
I11 = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(Bp*sp.sin(3*th))), (th, 0, 2*sp.pi))/sp.pi)
chk('03 (11): (1/pi) int B_p sin3 - claim', sp.simplify(I11 - (-3*p**2 + 14*p + 8)/(16*(1 - p)*(p + 4))))
Rr = sp.symbols('R', positive=True)
# strain from r^q B beyond R: (1/pi) int_R^inf r^{q-2} dr int B sin3 = R^{q-1}/(1-q) * I11
chk('03 (12)', sp.simplify(Rr**(q - 1)/(1 - q)*I11 - (-3*p**2 + 14*p + 8)/(32*(1 - p)**2*(p + 4))*Rr**(-2*(1 - p))))
b1B = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(Bp*sp.sin(th))), (th, 0, 2*sp.pi))/sp.pi)
P2 = -b1B/(2*(q + 3)) + I11/(2*(1 - q))
lim = sp.limit((1 - p)**2*P2, p, 1, '-')
chk('03 (11a): lim eps^2 [Psi_q[B_p]]_sin2 - 19/320', lim - sp.Rational(19, 320))
# direct ODE solve of Psi_q[B_p] mode 2 (independent of (13)): project source on sin 2
Sq = q*sp.cos(th)*Bp - sp.sin(th)*sp.diff(Bp, th)
S2 = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(Sq*sp.sin(2*th))), (th, 0, 2*sp.pi))/sp.pi)
P2d = -S2/((q + 1)**2 - 4)
chk('03 (11a) via direct projection', sp.limit((1 - p)**2*P2d, p, 1, '-') - sp.Rational(19, 320))

# (6) singular family, x > 0 and x < 0 separately
for sgn in (1, -1):
    X = sgn*sp.Symbol('u', positive=True)
    u = sp.Symbol('u', positive=True)
    Fs = a*u**p; psi = -a/(p + 1)*sgn*u*u**p     # x = sgn u, |x| = u, d/dx = sgn d/du
    dx = lambda e: sgn*sp.diff(e, u)
    chk('03 (13) Poisson -psi_xx - F_x, sgn %d' % sgn, sp.simplify(-dx(dx(psi)) - dx(Fs)))
    chk('03 (13) W2 = psi_x + a|x|^p, sgn %d' % sgn, sp.simplify(dx(psi) + a*u**p))
    chk('03 (13) transport (1/p) x F_x - F, sgn %d' % sgn, sp.simplify((1/p)*(sgn*u)*dx(Fs) - Fs))

# (7) radii
for cl in [2, sp.Rational(3, 2), sp.Rational(5, 4), sp.Rational(11, 10), sp.Rational(21, 20)]:
    e = 1 - 1/sp.nsimplify(cl)
    print('c_l = %-6s eps = %-6s eps^(-2/eps) = %.4g (log %.2f)' % (cl, e, float(e**(-2/e)), float(sp.log(e**(-2/e)))))
print('ALL ZERO' if ok else 'SOME CHECK FAILED')
