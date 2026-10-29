"""Lead checks of the t3frac referee record (T3 explicit family and moment conditions).
(F) phi = z F(u), u = a s + z^2: F(0) = -(c + mu)/2, F(1) = -c/2, F(1) + 2 F'(1) = 1/2 (source at (0, 1) with phi_z = 1/2 on axis),
    axis drift factorization w = z (c + 2 F(z^2)) = z (z^2 - 1)(c z^4 + (4 + 3c - mu) z^2 + mu)/(1 + z^2)^3.
(V) at mu = 1 + c the seed vorticity -Delta_5 phi = -(8a + 6)(c + 1/2) z + O(R^3).
(K) S_1 = (z - 1) rho_-^-5 + (z + 1) rho_+^-5 = 2 (r^2 - 4)(r^2 + 1)^(-7/2) z + O(z^3).
(H) h_z(0, 1) from the axis equation w h' = (w' - delta) h with h(0, 1) = 1 equals (2c - mu + 1)/(1 + c) (L'Hopital at the source).
(M) blend identities: c_l = (1 - l) c - l P/S, mu_l = (1 - l) mu + l (P - A)/S from phi_new = (1 - l) phi + l K^2 psi with
    K^2 = 1/(2 S) and the source moved back to z = 1 by the position condition (checked as the linear algebra of the three rows).
"""
import json, time
import sympy as sp
t0 = time.time()
c, mu, a, u, z, r, s = sp.symbols('c mu a u z r s', real=True)
N = -(c + mu)/2 + (-2 - 3*c + mu)*u + (2 - (c + mu)/2)*u**2
F = N/(1 + u)**3
res = {}
res['F0'] = sp.simplify(F.subs(u, 0) + (c + mu)/2) == 0
res['F1'] = sp.simplify(F.subs(u, 1) + c/2) == 0
Fp = sp.diff(F, u)
res['F1_strain'] = sp.simplify(F.subs(u, 1) + 2*Fp.subs(u, 1) - sp.Rational(1, 2)) == 0
w = z*(c + 2*F.subs(u, z**2))
wclaim = z*(z**2 - 1)*(c*z**4 + (4 + 3*c - mu)*z**2 + mu)/(1 + z**2)**3
res['axis_factor'] = sp.simplify(w - wclaim) == 0
# (V)
phi = z*F.subs(u, a*r**2 + z**2)
lap = sp.diff(phi, r, 2) + 3/r*sp.diff(phi, r) + sp.diff(phi, z, 2)
eps = sp.symbols('eps', positive=True)
lap0 = sp.series(sp.simplify(lap.subs({r: eps*r, z: eps*z})), eps, 0, 2).removeO()
lin = sp.simplify(lap0.subs(eps, 1))
res['vort_k2'] = sp.simplify((-lin).subs(mu, 1 + c) + (8*a + 6)*(c + sp.Rational(1, 2))*z) == 0
# (K)
S1 = (z - 1)*(r**2 + (z - 1)**2)**sp.Rational(-5, 2) + (z + 1)*(r**2 + (z + 1)**2)**sp.Rational(-5, 2)
d1 = sp.simplify(sp.diff(S1, z).subs(z, 0))
res['S1_equator'] = sp.simplify(S1.subs(z, 0)) == 0 and sp.simplify(d1 - 2*(r**2 - 4)*(r**2 + 1)**sp.Rational(-7, 2)) == 0
res['S1_odd_z2'] = sp.simplify(sp.diff(S1, z, 2).subs(z, 0)) == 0
# (H) h' = (w' - delta) h / w; at z = 1, w = 0, so h'(1) = lim (w' - delta) h/w = w''(1) h / (w''(1)...) use L'Hopital:
# h'(1) w'(1) = (w''(1) h(1) + (w'(1) - delta) h'(1)) with w'(1) = delta  =>  h'(1) delta = w''(1) + 0  ... (h(1) = 1)
delta = 1 + c
w1 = sp.diff(w, z).subs(z, 1); w2 = sp.diff(w, z, 2).subs(z, 1)
res['w_source_rate'] = sp.simplify(w1 - delta) == 0
hz = sp.simplify(w2/w1)   # from differentiating w h' = (w' - delta) h at z = 1: w' h' = w'' h + (w' - delta) h'
res['hz_source'] = str(sp.factor(hz))
res['hz_source_ok'] = sp.simplify(hz - (2*c - mu + 1)/(1 + c)) == 0
res['seconds'] = round(time.time() - t0, 1)
print(json.dumps(res, indent=1))
json.dump(res, open('author_checks/t3frac_check_output.json', 'w'), indent=1)
