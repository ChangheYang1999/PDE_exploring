"""verifier: request (o5) of lead NOTES 08:07Z, symbolic parts (own code).
1. fred20 transport identity (D + c) K = F (generic a, b, f with a f_x + b f_y = f, a_x + b_y = d), the axis traces
   F_1, M, the limit equation, the third axis equation, H_3 and (G_3/H_3)' = -(1/(3 A^beta)) Q' m^(beta - 1).
2. A = 2: H_5, F_5 from the hierarchy, I_5 = F_5/(w H_5), the residue formula L_5, values on three examples,
   G_3 and G_5 of R12 at L = 2.
3. S_A < 2 A on (1, 2); R12 formulas L^5 (Q - P) and J_n.
4. fred19 bending coefficient d; normalized exponents at X3.
5. Variation identity for delta [F_3/(w H_3)] (generic w, g)."""
import sympy as sp
x, y, dd, A, be = sp.symbols('x y d A beta', positive=True)
print('== 1. transport identity')
a = sp.Function('a')(x, y); b = sp.Function('b')(x, y); f = sp.Function('f')(x, y)
D = lambda u: a*sp.diff(u, x) + b*sp.diff(u, y)
c = 2*sp.diff(b, y) - 1
K = sp.diff(f, y, 2) - (sp.diff(f, y)/a)*sp.diff(a, y)
F = ((sp.diff(a, y)**2/a - sp.diff(a, y, 2))*(sp.diff(f, x) + b*sp.diff(f, y)/a)
     - 2*sp.diff(a, y)*sp.diff(f, x, y) + (sp.diff(a, x) - sp.diff(b, y))*(sp.diff(f, y)/a)*sp.diff(a, y))
E = D(K) + c*K - F
fx_rule = (f - b*sp.diff(f, y))/a          # from a f_x + b f_y = f
by_rule = dd - sp.diff(a, x)               # from a_x + b_y = d
def dif(e, nx, ny):
    vs = [x]*nx + [y]*ny
    return sp.diff(e, *vs) if vs else e
def reduce(e):
    for _ in range(12):
        rep = {}
        for dv in e.atoms(sp.Derivative):
            vc = dict(dv.variable_count); nx, ny = vc.get(x, 0), vc.get(y, 0)
            if dv.expr == f and nx >= 1: rep[dv] = dif(fx_rule, nx - 1, ny)
            elif dv.expr == b and ny >= 1: rep[dv] = dif(by_rule, nx, ny - 1)
        if not rep: return e
        e = e.xreplace(rep)
    raise RuntimeError('no convergence')
Er = sp.simplify(sp.together(reduce(sp.expand(E))))
print('(D + c) K - F after a f_x + b f_y = f, a_x + b_y = d:', Er)
# order of derivatives in F
print('max derivative order in F:', max(sum(dict(dv.variable_count).values()) for dv in F.atoms(sp.Derivative)))
# axis expansions
w, a2, a4, h, b3, g, G3, G5 = [sp.Function(n)(x) for n in ('w', 'a2', 'a4', 'h', 'b3', 'g', 'G3', 'G5')]
aser = w + a2*y**2 + a4*y**4
bser = h*y + b3*y**3
fser = g*y + G3*y**3 + G5*y**5
sub = {a: aser, b: bser, f: fser}
def onaxis(e, order):
    e2 = e.subs(sub).doit()
    return sp.series(e2, y, 0, order).removeO()
F1 = sp.simplify(onaxis(F/y, 1))
F1_claim = -6*a2*sp.diff(g, x) + 2*a2*(g/w)*(sp.diff(w, x) - 2*h)
print('F/y at y = 0 minus claimed F_1:', sp.simplify(F1 - F1_claim))
M = sp.simplify(onaxis(K/y, 1))
print('K/y at y = 0 minus (6 G3 - 2 g a2/w):', sp.simplify(M - (6*G3 - 2*g*a2/w)))
# relations on the axis: transport orders y, y^3; div order y^0, y^2
tr = sp.expand(sp.series((aser*sp.diff(fser, x) + bser*sp.diff(fser, y) - fser), y, 0, 6).removeO())
dv_ = sp.expand(sp.series(sp.diff(aser, x) + sp.diff(bser, y) - dd, y, 0, 4).removeO())
print('div order 0, 2:', dv_.coeff(y, 0), '|', dv_.coeff(y, 2))
G3eq = sp.solve(tr.coeff(y, 3).subs(b3, -sp.diff(a2, x)/3), sp.diff(G3, x))[0]
G3eq_claim = (-a2*sp.diff(g, x) + g*sp.diff(a2, x)/3 - (3*h - 1)*G3)/w
print('third axis equation from transport order y^3 minus claim:', sp.simplify(G3eq - G3eq_claim))
gp_rule = (1 - h)*g/w
print('transport order y: w g\' + (h - 1) g =', sp.simplify(tr.coeff(y, 1)))
lim = w*sp.diff(M, x) + (3*h - 1)*M - F1_claim
lim = lim.subs(sp.diff(G3, x), G3eq_claim)
lim = lim.subs(sp.diff(g, x, 2), sp.diff(gp_rule, x)).subs(sp.diff(g, x), gp_rule)
print('w M\' + (3h - 1) M - F_1 using the axis equations:', sp.simplify(lim))
# H_3 and (G_3/H_3)'
gg = sp.Function('g')(x); ww = sp.Function('w')(x); aa = sp.Function('a2')(x)
gp = (sp.diff(ww, x) - A)*gg/ww
H3 = A**be*gg**(3 + be)*(-ww)**(-be)
hh = A + 1 - sp.diff(ww, x)
chk = (ww*sp.diff(H3, x) + (3*hh - 1)*H3).subs(sp.diff(gg, x), gp)
print('w H3\' + (3h - 1) H3 with beta = 2/A, h = A + 1 - w\':', sp.simplify(chk.subs(be, 2/A)))
m = -ww/gg; Q = aa/gg**3
F3 = -aa*sp.diff(gg, x) + gg*sp.diff(aa, x)/3
lhs = F3/(ww*H3); rhs = -sp.diff(Q, x)*m**(be - 1)/(3*A**be)
wn, gn = sp.symbols('wn gn', positive=True)   # w = -wn < 0, g = gn > 0
expr = (lhs - rhs).subs({sp.diff(aa, x): sp.Symbol('a2p'), sp.diff(gg, x): sp.Symbol('gp')}).subs({aa: sp.Symbol('a2v')}).subs({ww: -wn, gg: gn})
print('F3/(w H3) + Q\' m^(beta-1)/(3 A^beta) (w = -wn < 0, g > 0):', sp.simplify(sp.powsimp(sp.expand_power_base(expr, force=True), force=True)))
print('dm/dx + A/g:', sp.simplify((sp.diff(m, x) + A/gg).subs(sp.diff(gg, x), gp)))
print('A g\'(P) = w\'\'(P) g* (l\'Hopital, w(P) = 0, w\'(P) = A): a2(P) = (g\' - w\'\')/2 =',
      sp.simplify((sp.Symbol('wpp')*sp.Symbol('gs')/A - sp.Symbol('wpp'))/2 - sp.Symbol('wpp')*(sp.Symbol('gs') - A)/(2*A)), '(difference)')

print('== 2. A = 2 resonance')
# general H_5 = A^(4/A) g^(5 + 4/A) (-w)^(-4/A) solves w H5' + (5h - 1) H5 = 0
H5 = A**(4/A)*gg**(5 + 4/A)*(-ww)**(-4/A)
chk5 = (ww*sp.diff(H5, x) + (5*hh - 1)*H5).subs(sp.diff(gg, x), gp)
print('w H5\' + (5h - 1) H5:', sp.simplify(chk5), '; p_5 = 10 + 4/A at A = 2:', 10 + sp.Rational(4, 2),
      '; H5(A=2) =', sp.simplify(H5.subs(A, 2)))
# fifth equation from the hierarchy (transport order y^5, div order y^4, curl orders y, y^3)
b5 = sp.Function('b5')(x)
aser5 = w + a2*y**2 + a4*y**4; bser5 = h*y + b3*y**3 + b5*y**5
tr5 = sp.expand(sp.series(aser5*sp.diff(fser, x) + bser5*sp.diff(fser, y) - fser, y, 0, 7).removeO())
dv5 = sp.expand(sp.series(sp.diff(aser5, x) + sp.diff(bser5, y) - dd, y, 0, 6).removeO())
cu5 = sp.expand(sp.series(sp.diff(aser5, y) - sp.diff(bser5, x) - sp.diff(fser, x), y, 0, 5).removeO())
print('curl order y (gives a2 = (g\' - w\'\')/2 with h = d - w\'):', sp.simplify(cu5.coeff(y, 1).subs(h, dd - sp.diff(w, x))))
sol = {b3: sp.solve(dv5.coeff(y, 2), b3)[0], b5: sp.solve(dv5.coeff(y, 4), b5)[0]}
a4sol = sp.solve(cu5.coeff(y, 3).subs(sol), a4)[0]
print('a4 from curl order y^3 minus (G3\' - a2\'\'/3)/4:', sp.simplify(a4sol - (sp.diff(G3, x) - sp.diff(a2, x, 2)/3)/4))
e5 = tr5.coeff(y, 5).subs(sol)
F5 = sp.expand(-(e5 - (w*sp.diff(G5, x) + (5*h - 1)*G5)))
F5_claim = sp.diff(a2, x)*G3 - a2*sp.diff(G3, x) + g*sp.diff(a4, x)/5 - a4*sp.diff(g, x)
print('F5 (hierarchy) minus claim:', sp.simplify(F5 - F5_claim))

def jets_A2(wexpr, N=26):
    """g rebuilt from w (A = 2, g/x^2 -> 1), a2, G3 = g a2/(3w), a4; Laurent series near 0."""
    Av = 2
    rr = sp.series(sp.cancel((sp.diff(wexpr, x) - Av)/wexpr - 2/x), x, 0, N).removeO()
    gs = sp.expand(sp.series(x**2*sp.exp(sp.integrate(rr, x)), x, 0, N + 2).removeO())
    return gs
def L5_of(wexpr, N=26, direct=True):
    Av = 2
    gs = jets_A2(wexpr, N)
    ws = sp.expand(sp.series(wexpr, x, 0, N + 2).removeO())
    a2s = sp.expand((sp.diff(gs, x) - sp.diff(ws, x, 2))/2)
    Nf = sp.diff(a2s, x, 2) - sp.diff(gs*a2s/ws, x) + 20*a2s**2/ws
    res = sp.series(Nf/gs**6, x, 0, 1).removeO().coeff(x, -1)/120
    out = [sp.nsimplify(sp.simplify(res))]
    if direct:
        # directly: I5 = F5/(w H5), H5 = 4 g^7/w^2, with G3 = g a2/(3w), a4 = (G3' - a2''/3)/4
        G3s = gs*a2s/(3*ws)
        a4s = (sp.diff(G3s, x) - sp.diff(a2s, x, 2)/3)/4
        F5s = sp.diff(a2s, x)*G3s - a2s*sp.diff(G3s, x) + gs*sp.diff(a4s, x)/5 - a4s*sp.diff(gs, x)
        I5 = F5s*ws/(4*gs**7)
        out.append(sp.nsimplify(sp.simplify(sp.series(I5, x, 0, 1).removeO().coeff(x, -1))))
    return out
print('pair (c): w = -2 sin x: L5 (formula, direct I5 residue) =', L5_of(-2*sp.sin(x), 22))
Ls = sp.Symbol('L', positive=True)
wR = -2*x*(Ls**2 - x**2)/(Ls**2 + x**2)
vals = L5_of(wR, 22)
print('R12 at A = 2: L5 =', sp.factor(vals[0]), '; direct residue equal:', sp.simplify(vals[0] - vals[1]) == 0,
      '; claim difference:', sp.simplify(vals[0] + 4*(Ls**2 - 4)*(Ls**2 - 10)/(15*Ls**14)))
ep = sp.Symbol('epsilon')
wE = -2*x + ep*x**15
gs = jets_A2(wE, 20)
print('w = -2x + eps x^15: g =', sp.series(sp.expand(gs), x, 0, 19), '(series in x; first order in eps below)')
vE = L5_of(wE, 20)
print('   L5 to first order in eps:', sp.series(vE[0], ep, 0, 2), '; direct residue:', sp.series(vE[1], ep, 0, 2))
# R12 at L = 2, A = 2: g* and w''(P), G3 and G5 of the lead's formulas in the fifth equation
w2 = wR.subs(Ls, 2); g2 = x**2/(1 + x**2/4)
print('R12 L=2: compatibility w g\' - (w\' - 2) g =', sp.simplify(w2*sp.diff(g2, x) - (sp.diff(w2, x) - 2)*g2),
      '; g* =', g2.subs(x, 2), "; w''(2) =", sp.simplify(sp.diff(w2, x, 2).subs(x, 2)))
a2_2 = sp.simplify((sp.diff(g2, x) - sp.diff(w2, x, 2))/2)
G3_2 = sp.simplify(g2*a2_2/(3*w2))
print('   G3 = g a2/(3w) minus 64x^2/(3(x^2+4)^3):', sp.simplify(G3_2 - 64*x**2/(3*(x**2 + 4)**3)))
a4_2 = (sp.diff(G3_2, x) - sp.diff(a2_2, x, 2)/3)/4
F5_2 = sp.diff(a2_2, x)*G3_2 - a2_2*sp.diff(G3_2, x) + g2*sp.diff(a4_2, x)/5 - a4_2*sp.diff(g2, x)
G5_2 = x**2*(11*x**6 + 88*x**4 - 1872*x**2 + 9984)/(90*(x**2 + 4)**5)
h2 = 3 - sp.diff(w2, x)
print('   G3 axis equation residual:', sp.simplify(w2*sp.diff(G3_2, x) + (3*h2 - 1)*G3_2 - (-a2_2*sp.diff(g2, x) + g2*sp.diff(a2_2, x)/3)))
print('   G5 fifth axis equation residual:', sp.simplify(w2*sp.diff(G5_2, x) + (5*h2 - 1)*G5_2 - F5_2))

print('== 3. S_A < 2A and the R12 formulas for 1 < A < 2')
SA = 6*A*(4*A - 3)/(8*A - 1)
print('2A - S_A =', sp.factor(sp.simplify(2*A - SA)), '(positive iff A < 2 for A > 1/8)')
u = sp.Symbol('u', positive=True); L = sp.Symbol('L', positive=True)
wr = -A*x*(1 - (x/L)**2)/(1 + (x/L)**2)
gr = x**2/(1 + (x/L)**2)
print('R12 compatibility:', sp.simplify(wr*sp.diff(gr, x) - (sp.diff(wr, x) - A)*gr))
Qr = sp.simplify((sp.diff(gr, x) - sp.diff(wr, x, 2))/(2*gr**3))
kap = A/L**2
print('L^5 Q - [(1 - 6k) u^-5 + (1 + 2k) u^-3]:', sp.simplify((L**5*Qr).subs(x, u*L) - ((1 - 6*kap)*u**-5 + (1 + 2*kap)*u**-3)))
mr = sp.simplify(-wr/gr)
print('m - (A/L)(1/u - u):', sp.simplify(mr.subs(x, u*L) - (A/L)*(1/u - u)))
v = 1/u - u
print('v^3 + 3v - (u^-3 - u^3):', sp.simplify(v**3 + 3*v - (u**-3 - u**3)), '; v^5 + 5v^3 + 5v - (u^-5 - u^5):',
      sp.simplify(v**5 + 5*v**3 + 5*v - (u**-5 - u**5)))
import mpmath as mp
mp.mp.dps = 30
for bv in (mp.mpf('1.6'), mp.mpf(4)/3, mp.mpf(10)/9):
    # t = 1 - v^(1/(beta - 1)) near t = 1 removes the (1 - t)^(beta - 2) singularity
    def Jn(n):
        q = 1/(bv - 1)
        f1 = lambda t: t**n*(1/t - t)**(bv - 2)*(1 + t**-2)
        def f2(vv):   # (1/t - t)^(beta - 2) = (1 - t)^(beta - 2) ((1 + t)/t)^(beta - 2), (1 - t) = vv^q
            t = 1 - vv**q
            return t**n*((1 + t)/t)**(bv - 2)*(1 + t**-2)*q
        return mp.quad(f1, [0, 0.5]) + mp.quad(f2, [0, mp.mpf(0.5)**(bv - 1)])
    Jc = lambda n: n/(n + bv - 1)*mp.beta((n - bv + 1)/2, bv - 1)
    print('   beta = %s: J3, J5 numeric vs closed: %s %s | %s %s ; J5/J3 - 5(4-b)/(3(b+4)) = %s' % (
        mp.nstr(bv, 6), mp.nstr(Jn(3), 15), mp.nstr(Jc(3), 15), mp.nstr(Jn(5), 15), mp.nstr(Jc(5), 15),
        mp.nstr(Jc(5)/Jc(3) - 5*(4 - bv)/(3*(bv + 4)), 3)))
bb = sp.Symbol('b', positive=True)
rho_ = 5*(4 - bb)/(3*(bb + 4))
print('S_A/A from J5/J3 minus 6(4A - 3)/(8A - 1):', sp.simplify(((6*rho_ - 2)/(rho_ + 1)).subs(bb, 2/A) - 6*(4*A - 3)/(8*A - 1)))
print('at L^2 = S_A: L^5(Q - P) at u = 1 equals 2 - 4 kappa; kappa = A/S_A > 1/2 for A < 2 (2A - S_A > 0)')

print('== 4. bending coefficient')
s, Y = sp.symbols('s Y')
wP = sp.Function('wt')(s); a2P = sp.Function('a2t')(s); hP = sp.Function('ht')(s); sg = sp.Function('sig')(s); dS = sp.Function('dS')(s)
Sfun = sg + dS*Y**2
WS = (wP + a2P*Y**2)*sp.diff(Sfun, s) + (hP*Y)*sp.diff(Sfun, Y) - A*Sfun
o2 = sp.expand(WS).coeff(Y, 2)
# at s = 0: w = 0, sigma' = 1, h = d - w' = (A + 1) - A = 1
o2P = o2.subs({wP: 0}).subs({sp.diff(sg, s): 1, hP: 1})
dPsol = sp.solve(o2P, dS)[0]
wpp, gs_ = sp.symbols('wpp gs')
print('y^2 order of W.grad S = A S at P gives d =', dPsol, '; with a2(P) = wpp (gs - A)/(2A):',
      sp.simplify(dPsol.subs(a2P, wpp*(gs_ - A)/(2*A)) - (gs_/A - 1)*wpp/(2*(A - 2))), '(difference from claim)')
AX, GX = sp.Rational('10.150725'), sp.Rational('29.74949')
print('normalized exponents (g* - a(A - 2))/A at X3, a = 1..4:', [sp.N((GX - k*(AX - 2))/AX, 6) for k in (1, 2, 3, 4)])
print('structural-zero orders j + ceil(p_j), p_j = 2j + (j - 1)/A at X3:', [j + sp.ceiling(2*j + sp.Rational(j - 1)/AX) for j in (3, 5, 7)])

print('== 5. variation identity (generic w, g; A fixed)')
eps = sp.Symbol('eps')
w0 = sp.Function('w0')(x); g0 = sp.Function('g0')(x); V = sp.Function('V')(x); eta = sp.Function('eta')(x)
wv = w0 + eps*V; gv = g0*(1 + eps*eta)
g0p = (sp.diff(w0, x) - A)*g0/w0
etap = (sp.diff(V, x) - (g0p/g0)*V)/w0
# compatibility of the perturbed pair to first order
comp = sp.expand(wv*sp.diff(gv, x) - (sp.diff(wv, x) - A)*gv)
c1 = comp.coeff(eps, 1)
c1 = c1.subs(sp.diff(eta, x), etap).subs(sp.diff(g0, x), g0p)
print('first-order compatibility with eta\' = (V\' - (g\'/g) V)/w:', sp.simplify(c1))
def F3H3(wf, gf):
    a2f = (sp.diff(gf, x) - sp.diff(wf, x, 2))/2
    F3f = -a2f*sp.diff(gf, x) + sp.diff(a2f, x)*gf/3
    H3f = A**be*gf**(3 + be)*(-wf)**(-be)
    return F3f/(wf*H3f), F3f, H3f
full, F3f, H3f = F3H3(wv, gv)
dfull = sp.diff(full, eps).subs(eps, 0)
base, F30, H30 = F3H3(w0, g0)
dF3 = sp.diff(F3f, eps).subs(eps, 0)
formula = dF3/(w0*H30) - base*(V/w0 + (3 + be)*eta - be*V/w0)
print('d/deps [F3/(w H3)] - formula:', sp.simplify(sp.powsimp(sp.expand(dfull - formula), force=True)))
