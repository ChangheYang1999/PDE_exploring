# BASIS.md: complete definition of the candidate representation (branch T1_seed_cl0p74, level L2)

Generated 2026-10-29T06:47:22Z from runs/t1seedCL2_cl0p74_q2p5 by scripts/export_candidate.py. D48/n32/K32 level of the 3000-iteration 0.74 direct-seed state (L1), 1500 LM iterations; holdout rho_max 2.81 (q equation, shell 1 random points), s_core 0.66, s_far 0.60; not a solution (order-one residual)

## Coordinates
Spherical R = sqrt(r^2 + z^2), mu = z/R (mu = +1 on the positive z axis). All fields are axisymmetric scalars of (R, mu).
Reduced variables (pre-registered specification, section 1): U^r = -r d_z phi, U^z = 2 phi + r d_r phi, U^theta = r q; eta = -Delta_5 phi, Delta_5 = d_rr + (3/r) d_r + d_zz.
Formulation B: phi and q are the primary unknowns; eta is derived (R_ell = 0 identically).
c_l = 0.74 (fixed), alpha = (1 - c_l)/c_l = 0.35135135135135137.

## Elements (piecewise in R; same Legendre basis P_n(mu), n = 0..nmax = 32, in every element)
  element 0: ball R in [0, 2.0]: basis column (n, k) = P_n(mu) rho^n Q_k(2 rho^2 - 1), rho = R/2.0, for n + 2k <= D = 48,
  with Q_k = the Jacobi polynomial P_k^(0, n+1/2) (3D Zernike radial family, three-term recurrence as in field_eval.py);
  ordered n-major (n = 0..nmax, then k = 0..floor((D - n)/2)): 553 columns.  Every column is an axisymmetric Cartesian
  polynomial of degree <= D (regular in (r^2, z) at the axis and origin by construction); with nmax < D the span is the subspace
  whose solid-harmonic content has degree <= nmax (solid harmonics of degree nmax+1..D are absent).
  element 1: shell R in [2.0, 10.0], Chebyshev degree K = 32 in x = 2 ln(R/Rlo)/ln(Rhi/Rlo) - 1, Legendre degree nmax = 32; basis column (n, k) = P_n(mu) T_k(x), ordered n-major (n = 0..nmax, k = 0..K): 1089 columns
  element 2: exterior R in [10.0, infinity): basis column (n, e) = P_n(mu) (R/10.0)^(-e); the fractional power law is factored
  analytically (no compactification).  Exponent set of the node/basis union, ordered n-major then by e ascending:
  e in [0.35135135135135137, 1.3513513513513513, 1.7027027027027026, 2.7027027027027026, 3.0, 3.0540540540540544, 4.0].
  phi uses only the columns with e in [0.35135135135135137, 1.7027027027027026, 3.0, 3.0540540540540544, 4.0] (column indices phi_cols in coeffs.npz meta),
  q uses only the columns with e in [1.3513513513513513, 2.7027027027027026] (q_cols).  The exponents are of the form m alpha + k (m, k integers):
  phi: generated from {alpha} U {3, 4, 5, ...} under (a, b) -> a + b + 1 up to emax = 4.0; q: {alpha + 1} closed under (a_phi, b_q) -> a + b + 1.
  So the exterior can express R^-alpha, R^-(2 alpha + 1) (first nonlinear correction), R^-3 (5D monopole d_0, kept as a test), R^-4, R^-(3 alpha + 2), ...
  Exponents closer than merge_tol = 0.03 were merged (near-resonant pairs).
  Leading tail: phi -> R^-alpha A(mu) with A(mu) = sum_n a_n P_n(mu), a_n = coefficient(n, alpha) * Rm^alpha; q -> R^-(alpha+1) B(mu) likewise with Rm^(alpha+1).

## Coefficient arrays (coeffs.npz)
phi_el<i>, q_el<i>: float64 vectors in the column order above restricted to the column subsets phi_cols / q_cols of meta_json (exponent
sets for the exterior; Legendre-parity masks None for phi and None for q in every element).
meta_json: JSON with c_l, alpha, the element table (Rlo, Rhi, nmax, D or K or exponents, labels [n, k-or-e] per column, phi_cols, q_cols), z0.
Shapes: phi_el0: (553,), q_el0: (553,), phi_el1: (1089,), q_el1: (1089,), phi_el2: (165,), q_el2: (66,).

## Continuity, gauge, constraints (how the state was obtained; not part of the definition of the fields)
Interface rows impose phi in C^3 and q in C^2 across R = [2.0, 10.0] by least squares (weight 100.0); the jumps are
reported in the candidate's validation.  Working gauge: int_S2 |F|^2 dS = 29.371276953605268 on the leading tail; the
conversion factor to the reporting gauge int |F|^2 dS = 1 is L = (int |F|^2 dS)^(-1/(2(1 + alpha))) (fields transform as phi_L(y) = L phi(y/L), q_L(y) = q(y/L)).
S1 rows: phi_z(0, z0) = 1/2 and c_l z0 + 2 phi(0, z0) = 0 with z0 = 1.2281649016388683e-07 and q(0, z0) pinned to 2.5.

## Evaluation
field_eval.py (numpy only) implements exactly the above and reproduces samples.npz (r, z, phi, q, U^r, U^theta, U^z, P, eta).
Nothing in this file is defined by reference to code.
