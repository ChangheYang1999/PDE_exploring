# Scratch check for topic249 (exact symbolic; toy C6 model with 7th-derivative jumps at t=0).
import sympy as sp
t, th = sp.symbols('t theta', real=True)
ell0, a = sp.symbols('ell0 a', positive=True)
Th, Tz, Gh, Gz, G0, GX, rho = sp.symbols('Th Tz Gh Gz G0 GX rho')
lam = a/ell0
R = Th + Gh + a*(GX + Tz + Gz) - lam*(ell0*GX + G0 - rho)
print('(5) diff:', sp.expand(R - (Th + a*Tz + (Gh + a*Gz - lam*G0) + lam*rho)))
r = sp.exp(t); p = sp.cos(th)**2*sp.sin(th)
J = sp.symbols('J0:3'); c = sp.symbols('c0:9'); K = sp.symbols('K0:4')
def model(side):
    j = 1 if side == 'R' else 0
    s = [c[3*m] + c[3*m+1]*t + c[3*m+2]*t**2 + j*J[m]*t**7/5040 for m in range(3)]
    rho0 = r**3*p*sum(s[m]*sp.cos(2*m*th) for m in range(3))
    b1 = 1 + K[0]*t + j*K[1]*t**7/5040; b2 = 2 + K[2]*t**2 + j*K[3]*t**7/5040
    x = r*sp.cos(th); y = r*sp.sin(th)
    B1 = x*b1*(1+sp.cos(2*th)/3); B2 = y*b2*(1+sp.cos(4*th)/5)
    Br = B1*sp.cos(th)+B2*sp.sin(th); Bt = -B1*sp.sin(th)+B2*sp.cos(th)
    G = Br/r*sp.diff(rho0, t) + Bt/r*sp.diff(rho0, th) + (ell0*r)/r*sp.diff(rho0,t) - rho0
    return G, Br
GR, BrR = model('R'); GL, BrL = model('L')
dR, dL = GR, GL
for k in range(1, 7):
    dR = sp.diff(dR, t); dL = sp.diff(dL, t)
    jk = sp.expand(sp.expand_trig((dR - dL).subs(t, 0)))
    if k < 6: print('order', k, 'jump zero:', jk == 0)
S = sum(J[m]*sp.cos(2*m*th) for m in range(3))
pred = p*(ell0 + BrR.subs(t, 0))*S   # r_star=1, full transport V.e_r/r = ell0 + B.e_r/r
print('(1)/(2) diff:', sp.expand(sp.expand_trig(jk - pred)))
# 1D axis check (topic248 axis formulas, y=e^t): gamma=axis/y, axis(Q.grad rho0)=Q f'-2Q_y f, f=y*A
y = sp.Symbol('y', positive=True)
A = sp.Function('A'); W = sp.Function('W'); Z = sp.Function('Z')
f = y*A(sp.log(y))
lamb = sp.Symbol('lamb')
axisR = W(y)*sp.diff(f, y) - 2*sp.diff(W(y), y)*f + lamb*f + Z(y)
g = (axisR/y).subs(y, sp.exp(t))
g6 = sp.diff(g, t, 6)
A7 = sp.Derivative(A(t), (t, 7))
coef = sp.simplify(sp.expand(g6).coeff(A7))
print('coefficient of A^(7) in gamma_R^(6):', coef)
print('max W derivative order in gamma_R^(6):', max([d.derivative_count for d in g6.atoms(sp.Derivative) if d.expr.func == W] + [0]))
