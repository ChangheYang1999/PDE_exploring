"""V23 symbolic checks of referee result 6 results 01, 02 (forced far-field correction)."""
import sympy as sp
r, th, p, t, a, s = sp.symbols('r theta p t a s', positive=True)
A = sp.Function('A')(th); Psi = sp.Function('Psi')(th)
out = []
def chk(name, e):
    e = sp.simplify(e); out.append((name, e)); print(name, '->', e)
# (i) psi_F = r^{p+1} Psi: -Lap psi_F - d_x F = -r^{p-1} [Psi'' + (p+1)^2 Psi - ((sin A)' - (p+1) cos A)]
F = r**p*A; psiF = r**(p+1)*Psi
lap = sp.diff(psiF, r, 2) + sp.diff(psiF, r)/r + sp.diff(psiF, th, 2)/r**2
dxF = sp.cos(th)*sp.diff(F, r) - sp.sin(th)/r*sp.diff(F, th)
eq1 = sp.diff(Psi, th, 2) + (p+1)**2*Psi - (sp.diff(sp.sin(th)*A, th) - (p+1)*sp.cos(th)*A)
chk('01(1): -Lap psi_F - d_x F + r^{p-1} (1)', -lap - dxF + r**(p-1)*eq1)
# (ii) W = (-psi_y, psi_x) = J grad psi: polar components (W_r, W_th) = (-psi_th/r, psi_r)
Wr = -sp.diff(psiF, th)/r; Wt = sp.diff(psiF, r)
chk('01(2): W_r - (-r^p Psi\')', Wr + r**p*sp.diff(Psi, th)); chk('01(2): W_th - (p+1) r^p Psi', Wt - (p+1)*r**p*Psi)
divH = sp.diff(r*Wr, r)/r + sp.diff(Wt, th)/r
chk('div H', divH)
# (iii) div(F H) = r^{2p-1} J_p, both forms; grad F . H same
divFH = sp.diff(r*F*Wr, r)/r + sp.diff(F*Wt, th)/r
J2 = (p+1)*sp.diff(A*Psi, th) - (2*p+1)*A*sp.diff(Psi, th)
J1 = (p+1)*Psi*sp.diff(A, th) - p*sp.diff(Psi, th)*A
chk('02(2): div(FH) - r^{2p-1} J (product form)', divFH - r**(2*p-1)*J2)
chk('02(2): product form - C^1 form', J2 - J1)
gFH = sp.diff(F, r)*Wr + sp.diff(F, th)/r*Wt
chk('02(8): grad F . H - r^{2p-1} J', gFH - r**(2*p-1)*J1)
# (iv) rescaled transport (9): f_t(X) = e^{-pt} rho(e^t X), with l X.grad rho + W.grad rho = rho
#     check in polar form: d_t f = -p f + r f_r; transport at radius e^t r gives r f_r = p f - l^{-1} e^{-(1-p)t} w.grad f
T, l = sp.symbols('T l', positive=True)
rho = sp.Function('rho'); w1 = sp.Function('w1'); w2 = sp.Function('w2')     # W in polar comps at (R, th)
R = sp.exp(T)*r
f = sp.exp(-p*T)*rho(R, th)
ft = sp.diff(f, T)
# transport at (R, th): l R rho_R + W_r rho_R + W_th/R rho_th = rho, solve for rho_R
rR, rT, WR, WT = sp.symbols('rho_R rho_th W_R W_th')
rhoR = sp.solve(sp.Eq(l*R*rR + WR*rR + WT/R*rT, rho(R, th)), rR)[0]
# f_t = -p f + e^{-pT} R rho_R ; claimed = -l^{-1} e^{-(1-p)T} w_t.grad f_t, w_t = e^{-pT} W, grad f_t = e^{(1-p)T} (rho_R, rho_th/R) e^{... }
lhs = -p*f + sp.exp(-p*T)*R*rhoR
grad_f = (sp.exp(-p*T)*sp.exp(T)*rR, sp.exp(-p*T)*sp.exp(T)*rT/R)   # (d_r f_t, (1/r) d_th f_t) at X = r e_th
rhs = -sp.exp(-(1-p)*T)/l*(sp.exp(-p*T)*WR*grad_f[0] + sp.exp(-p*T)*WT*grad_f[1])
chk('02(9) with p = 1/l (after solving transport for rho_R)', (lhs - rhs).subs(p, 1/l).subs(rR, rhoR))
chk('l (1-p) - (l-1) at p = 1/l', (l*(1-p) - (l-1)).subs(p, 1/l))
# (v) Lemma expansions: integrate (1) once from beta with A = a t^2 + a3 t^3 + a4 t^4, Psi = o(t^4) (set 0 up to t^4)
a3, a4 = sp.symbols('a3 a4')
for beta, name in ((sp.Symbol('beta'), 'sin(beta) != 0'), (sp.S(0), 'beta = 0'), (sp.pi, 'beta = pi')):
    Aloc = a*t**2 + a3*t**3 + a4*t**4
    psip = sp.sin(beta+t)*Aloc - (p+1)*sp.integrate(sp.cos(beta+s)*Aloc.subs(t, s), (s, 0, t))
    ser = sp.series(psip, t, 0, 4).removeO()
    print('Lemma (16)', name, ': Psi\'(beta+t) =', sp.factor(sp.expand(ser)))
    if name == 'sin(beta) != 0':
        chk('  t^2 coefficient - a sin(beta)', ser.coeff(t, 2) - a*sp.sin(beta))
    else:
        chk('  t^3 coefficient - a (2-p) cos(beta)/3', sp.simplify(ser.coeff(t, 3) - a*(2-p)*sp.cos(beta)/3))
        chk('  t^2 coefficient', ser.coeff(t, 2))
chk('2(p+1)/p - 4 - (2/p - 2) (>0 for p < 1)', 2*(p+1)/p - 4 - (2/p - 2))
# (vi) (19): int_R^{2R} r^{4p-1} dr = R^{4p} (2^{4p} - 1)/(4p)
Rs = sp.Symbol('R', positive=True)
chk('02(19) radial integral', sp.integrate(r**(4*p-1), (r, Rs, 2*Rs)) - Rs**(4*p)*(2**(4*p)-1)/(4*p))
# (vii) example rho_0 - F_0 = O(r^{p-2}): x^2 [(1+r^2)^{(p-2)/2} - r^{p-2}] / (x^2 r^{p-4}) -> (p-2)/2
x = sp.Symbol('x')
print('rho_0 - F_0 leading (times r^{4-p}/x^2) ->', sp.limit(((1+r**2)**((p-2)/2) - r**(p-2))*r**(4-p), r, sp.oo))
# (viii) L^q range: R^{1-2p-2/q} ||.||_q >= c  ->  annulus norm >= c R^{2p-1+2/q}; exponent >= 0 iff 2 + q (2p-1) >= 0
q = sp.Symbol('q', positive=True)
chk('q (2p - 1 + 2/q) - (2 + q(2p-1))', sp.expand(q*(2*p-1+2/q) - (2 + q*(2*p-1))))
print('ALL ZERO' if all(e == 0 for _, e in out) else 'NONZERO PRESENT')
