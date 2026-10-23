# the real root of Lambda for (1; 3, 3, 1, 1, 1, 1, 1), d = 23: is it a real configuration? (lead)
import pickle, sympy as s, mpmath as mp
mp.mp.dps = 60
x, p, v = s.symbols('x p v')
D = pickle.load(open('case25.pkl', 'rb')); F, G, R = s.Poly(D['F'], p, x), s.Poly(D['G'], p, x), s.Poly(D['R'], x)
sh27 = s.Poly(R.as_expr().subs(x, x + 27), x).all_coeffs(); sh25 = s.Poly(R.as_expr().subs(x, x + 25), x).all_coeffs()
print('coefficients in powers of eta - 27 all positive:', all(c > 0 for c in sh27), '| in powers of eta - 25 all positive:', all(c > 0 for c in sh25),
      '| negative ones at 25:', sum(1 for c in sh25 if c < 0), '| Lambda(25) =', R.eval(25) != 0, s.sign(R.eval(25)), 'Lambda(27) sign', s.sign(R.eval(27)))
fl = s.factor_list(R.as_expr())[1]
print('linear factors:', [(f, m) for f, m in fl if s.Poly(f, x).degree() == 1])
big = [s.Poly(f, x) for f, m in fl if s.Poly(f, x).degree() > 1][0]
r = [rt for rt in big.real_roots() if rt >= 25][0]
eta = mp.mpf(str(s.N(r, 80)))
# common root p of F and G at eta
Fp = [mp.mpf(str(c)) for c in s.Poly(F.as_expr().subs(x, s.Float(str(eta), 70)), p).all_coeffs()]
Gp = [mp.mpf(str(c)) for c in s.Poly(G.as_expr().subs(x, s.Float(str(eta), 70)), p).all_coeffs()]
rf = mp.polyroots(Fp, maxsteps=500, extraprec=200); rg = mp.polyroots(Gp, maxsteps=500, extraprec=200)
print('roots of F in p:', [mp.nstr(t, 12) for t in rf])
print('roots of G in p:', [mp.nstr(t, 12) for t in rg])
best = min(((abs(a - b), a) for a in rf for b in rg), key=lambda t: t[0])
print('closest pair distance', mp.nstr(best[0], 5), 'common root p ~', mp.nstr(best[1], 20))
pickle.dump({'eta': str(eta), 'p': str(best[1])}, open('case25b.pkl', 'wb'))
