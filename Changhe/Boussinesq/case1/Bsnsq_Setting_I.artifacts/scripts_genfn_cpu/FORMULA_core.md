Formula sheet: generating function with core patches (states with npz keys 'cc' and 'core')
Written 2026-10-21T02:06Z. Applies to the state frzE_cin_J56K30 (not published) and later states with a 'core' key.

Keys: J, Kw, m (= 3), beta (= 3), alpha, se, gam (= 0 in all core states), a0, c (length (J+1)(Kw+1), row-major in (n, k)),
core (array of rows (Jc, Kc, Rc, Lc), one row per patch), cc (concatenation over patches of (Jc+1)(Kc+1) coefficients,
row-major in (i, j)).

G(x, eta) = x eta E^(1/3) [ P(x, eta) + sum_p chi_p(x, eta) Q_p(x, eta) ],
  E = 1 + x^2 + (eta/se)^6,
  P = sum_{n <= J, k <= Kw} c_nk T_n(2 t - 1) T_k(2 w - 1),
    t = 1 - log(1 + (e^alpha - 1)(1 - E^(-1/6)))/alpha      (alpha = 3; t = 1 at the centre, t -> 1 - log(e^alpha)/alpha = 0 at infinity),
    w = (eta/se)^2 E^(-1/3)                                  (gam = 0: no angular map),
  chi_p = exp(-(x^2 + eta^2)/Lc_p^2),
  Q_p = sum_{i <= Jc_p, j <= Kc_p} d^p_ij T_i(2 xi_p - 1) T_j(2 zeta_p - 1),
    xi_p = x^2/(Rc_p^2 + x^2), zeta_p = eta^2/(Rc_p^2 + eta^2).
Here T_n(2t - 1) means the Chebyshev polynomial T_n evaluated at 2t - 1 (in model.py the variable stored as t is already the
mapped variable above; the code builds T_n(2 t - 1) by the recurrence s = 2t - 1).
The patch functions are analytic on the closed quadrant, even in x and eta inside Q_p, so G stays odd in x and in eta; chi_p
makes them superexponentially small at infinity, so the far-field class (and the far-field formulas used in your earlier
audits) is unchanged.
Centre: G = h x eta + O(|.|^4) with h = sum_nk c_nk (-1)^k + sum_p sum_ij d^p_ij (-1)^(i+j) (all T at their endpoint values,
chi_p(0) = 1). For frzE, h = 0.999999999999531 in binary64.
Everything else (B0, C, M, W, Psi, Omega, R, the normalizers N and N2, Theta = a0 eta) is as in the outer-only states.

Reference values for frzE_cin_J56K30 (binary64, my code; derivatives of G):
  (x, eta) = (0.05, 0.03):  G 1.502249877523815e-03, G_x 3.005430213865268e-02, G_x,eta 1.004499730678507e+00
                            (core contribution to G: -6.804627e-06)
  (0.3, 0.2):               G 6.398547357637718e-02, G_x 2.145972560282976e-01, G_x,eta 1.196908507199403e+00 (core 3.753688e-05)
  (1.0, 1.0):               G 3.381803677111566e+00, G_x 3.344117612778085e+00, G_x,eta 1.008573911403068e+01 (core 1.59e-08)
  (5.0, 0.5):               G 3.972303304006019e+00, G_x 8.970264357345101e-01, G_x,eta 2.484875512767999e+00
  (100.0, 30.0):            G 1.868304995510755e+08, G_x 1.866742756216507e+06, G_x,eta 1.957478313818031e+05
