"""Lead check of the referee record 't1budget' (2026-10-28T22:03Z): (N) the radial negative-strain subclass
v^3 + u^n v^(2n+3) = 1, h = v^2, phi = z v^3/2, c = 1/2 + 3/(4n) solves the swirl transport equation exactly;
(A) the axis identities w e = 2h(h - 1), g = h/w, g' = -delta g/w, e = 2 w g^2 - 2 g; (L) the local closure identity at an
S1 source at the origin: phi = z/2 + p_s s z + p_z z^3 gives e = 6 p_z z/delta^2 and p_s = -(3 p_z/4)(1 + K^2/delta^2);
(P) the positive-family inequality F + s F_s >= (1 - d) F for phi = z F, F = (1 + s/L^2 + B z^2)^beta/(2 (1 + s/L^2 + z^2)^d)."""
import sympy as sp, json, time, random
t0 = time.time(); res = {}
s, z, u, K, c = sp.symbols('s z u K c', positive=True)
# (N)
for n in (4, 5, 7):
    cc = sp.Rational(1, 2) + sp.Rational(3, 4*n)
    V = sp.Function('V')
    vu = sp.symbols('vu', positive=True)
    G = vu**3 + u**n*vu**(2*n + 3) - 1
    dv = -sp.diff(G, u)/sp.diff(G, vu)  # dv/du
    # phi = z v^3/2, h = v^2 with v = v(s + z^2); derivatives via chain rule
    v_s = dv; v_z = 2*z*dv
    phi_z = vu**3/2 + z*sp.Rational(3, 2)*vu**2*v_z
    phi_s = z*sp.Rational(3, 2)*vu**2*v_s
    phi = z*vu**3/2
    h_s = 2*vu*v_s; h_z = 2*vu*v_z; h = vu**2
    Rq = (1 - 2*phi_z)*h + 2*s*(cc - phi_z)*h_s + (cc*z + 2*phi + 2*s*phi_s)*h_z
    errs = []
    random.seed(n)
    for _ in range(6):
        sv, zv = random.uniform(0.01, 3), random.uniform(-2, 2)
        uv = sv + zv**2
        root = sp.nsolve((vu**3 + uv**n*vu**(2*n + 3) - 1), vu, (1e-12, 1), solver='bisect', prec=40)  # f increasing, f(0) < 0 <= f(1)
        val = Rq.subs({u: uv}).subs({s: sv, z: zv, vu: root})
        errs.append(abs(float(val)))
    res[f'N_n{n}_max_abs_Rq'] = max(errs)
# (A) axis identities from w h' = (w' - delta) h and (w e)' + (1 + 2A) e ... use the first integral form
zz = sp.symbols('zz', positive=True); delta = 1 + c
w = sp.Function('w')(zz); h1 = sp.Function('h')(zz)
g = h1/w
hp = (sp.diff(w, zz) - delta)*h1/w
gp = sp.diff(g, zz).subs(sp.Derivative(h1, zz), hp)
res['A_gprime'] = sp.simplify(gp + delta*g/w) == 0
res['A_e_form'] = sp.simplify((2*w*g**2 - 2*g) - 2*h1*(h1 - 1)/w) == 0
# (L) local closure at the source
ps, pz = sp.symbols('p_s p_z')
phiL = z/2 + ps*s*z + pz*z**3
a1, b1, e1 = sp.symbols('a1 b1 e1')
q = K + a1*s + b1*z**2; eta = e1*z
phz = sp.diff(phiL, z); phs = sp.diff(phiL, s)
Wsd = 2*s*(c - phz); Wzd = c*z + 2*phiL + 2*s*phs
Rq = sp.expand((1 - 2*phz)*q + Wsd*sp.diff(q, s) + Wzd*sp.diff(q, z))
Re = sp.expand((1 + c)*eta + Wsd*sp.diff(eta, s) + Wzd*sp.diff(eta, z) - sp.diff(q**2, z))
eqs = [Rq.coeff(s, 1).coeff(z, 0), Rq.coeff(s, 0).coeff(z, 2), Re.coeff(s, 0).coeff(z, 1)]
sol = sp.solve(eqs, [a1, b1, e1], dict=True)[0]
res['L_e'] = str(sp.simplify(sol[e1]))
res['L_e_ok'] = sp.simplify(sol[e1] - 6*pz*K**2/delta**2) == 0
etaPhi = sp.expand(-(4*s*sp.diff(phiL, s, 2) + 8*sp.diff(phiL, s) + sp.diff(phiL, z, 2)))
ps_sol = sp.solve(sp.Eq(etaPhi.coeff(z, 1), sol[e1]), ps)[0]
res['L_ps'] = str(sp.factor(ps_sol))
res['L_ps_ok'] = sp.simplify(ps_sol + sp.Rational(3, 4)*pz*(1 + K**2/delta**2)) == 0
# (P) F + s F_s >= (1 - d) F
B, L, beta, d = sp.symbols('B L beta d', positive=True)
F = (1 + s/L**2 + B*z**2)**beta/(2*(1 + s/L**2 + z**2)**d)
ratio = sp.simplify((F + s*sp.diff(F, s))/F)
res['P_ratio'] = str(ratio)
# ratio = 1 + beta s/(L^2 X) - d s/(L^2 Y), X = 1 + s/L^2 + B z^2 >= s/L^2, Y = 1 + s/L^2 + z^2 > s/L^2, so ratio > 1 - d
mn = 10.0
random.seed(1)
for _ in range(400):
    vals = {s: random.uniform(0, 50), z: random.uniform(0, 5), B: random.uniform(1, 1e4), L: random.uniform(0.5, 30),
            beta: random.uniform(0.01, 0.2), d: random.uniform(0.5, 0.99)}
    mn = min(mn, float(ratio.subs(vals)) - (1 - float(vals[d])))
res['P_min_ratio_minus_(1-d)_sampled'] = mn
res['seconds'] = round(time.time() - t0, 2)
print(json.dumps(res, indent=1))
json.dump(res, open('author_checks/t1budget_check_output.json', 'w'), indent=1)
