# BASIS.md: complete definition of the candidate representation (branch S1_pilot, level L0)

Generated 2026-10-28T19:52:39Z from runs/p1_cl0p600_s1_sym_v2_q1p0_z0p0_sh0p0_lm by scripts/export_candidate.py. First pilot state at c_l = 0.6 (D = 24, nmax = 12); rho_max about 13: a non-solution exported only to exercise the verifier's loader.

## Coordinates
Spherical R = sqrt(r^2 + z^2), mu = z/R (mu = +1 on the positive z axis). All fields are axisymmetric scalars of (R, mu).
Reduced variables (pre-registered specification, section 1): U^r = -r d_z phi, U^z = 2 phi + r d_r phi, U^theta = r q; eta = -Delta_5 phi, Delta_5 = d_rr + (3/r) d_r + d_zz.
Formulation B: phi and q are the primary unknowns; eta is derived (R_ell = 0 identically).
c_l = 0.6 (fixed), alpha = (1 - c_l)/c_l = 0.6666666666666667.

## Elements (piecewise in R; same Legendre basis P_n(mu), n = 0..nmax = 12, in every element)
  element 0: ball R in [0, 2.0]: basis column (n, k) = P_n(mu) rho^n T_k(2 rho^2 - 1), rho = R/2.0, for n + 2k <= D = 24;
  ordered n-major (n = 0..nmax, then k = 0..floor((D - n)/2)): 127 columns.  This is exactly the space of axisymmetric
  Cartesian polynomials of degree <= D (regular in (r^2, z) at the axis and origin by construction).
  element 1: shell R in [2.0, 10.0], Chebyshev degree K = 16 in x = 2 ln(R/Rlo)/ln(Rhi/Rlo) - 1, Legendre degree nmax = 12; basis column (n, k) = P_n(mu) T_k(x), ordered n-major (n = 0..nmax, k = 0..K): 221 columns
  element 2: exterior R in [10.0, infinity): basis column (n, e) = P_n(mu) (R/10.0)^(-e); the fractional power law is factored
  analytically (no compactification).  Exponent set of the node/basis union, ordered n-major then by e ascending:
  e in [0.6666666666666667, 1.6666666666666667, 2.3333333333333335, 3.0, 3.3333333333333335, 4.0, 4.666666666666667, 5.0].
  phi uses only the columns with e in [0.6666666666666667, 2.3333333333333335, 3.0, 4.0, 4.666666666666667, 5.0] (column indices phi_cols in coeffs.npz meta),
  q uses only the columns with e in [1.6666666666666667, 3.3333333333333335, 5.0] (q_cols).  The exponents are of the form m alpha + k (m, k integers):
  phi: generated from {alpha} U {3, 4, 5, ...} under (a, b) -> a + b + 1 up to emax = 5.0; q: {alpha + 1} closed under (a_phi, b_q) -> a + b + 1.
  So the exterior can express R^-alpha, R^-(2 alpha + 1) (first nonlinear correction), R^-3 (5D monopole d_0, kept as a test), R^-4, R^-(3 alpha + 2), ...
  Exponents closer than merge_tol = 0.03 were merged (near-resonant pairs).
  Leading tail: phi -> R^-alpha A(mu) with A(mu) = sum_n a_n P_n(mu), a_n = coefficient(n, alpha) * Rm^alpha; q -> R^-(alpha+1) B(mu) likewise with Rm^(alpha+1).

## Coefficient arrays (coeffs.npz)
phi_el<i>, q_el<i>: float64 vectors in the column order above (for the exterior, restricted to phi_cols / q_cols).
meta_json: JSON with c_l, alpha, the element table (Rlo, Rhi, nmax, D or K or exponents, labels [n, k-or-e] per column, phi_cols, q_cols), z0.
Shapes: phi_el0: (127,), q_el0: (127,), phi_el1: (221,), q_el1: (221,), phi_el2: (78,), q_el2: (39,).

## Continuity, gauge, constraints (how the state was obtained; not part of the definition of the fields)
Interface rows impose phi in C^3 and q in C^2 across R = [2.0, 10.0] by least squares (weight 100.0); the jumps are
reported in the candidate's validation.  Working gauge: int_S2 |F|^2 dS = 2668.2458314553814 on the leading tail; the
conversion factor to the reporting gauge int |F|^2 dS = 1 is L = (int |F|^2 dS)^(-1/(2(1 + alpha))) (fields transform as phi_L(y) = L phi(y/L), q_L(y) = q(y/L)).
S1 rows: phi_z(0, z0) = 1/2 and c_l z0 + 2 phi(0, z0) = 0 with z0 = -0.47125588235104027.

## Evaluation
field_eval.py (numpy only) implements exactly the above and reproduces samples.npz (r, z, phi, q, U^r, U^theta, U^z, P, eta).
Nothing in this file is defined by reference to code.
