# NUMERICAL_METHODS.md (primary numerical search). Updated 2026-10-28T19:54:05Z; later sections carry their own dates. Formulation B (phi, q primary) least squares.

## Representation (problem statement section 6; pre-registered specification sections 2 and 3.3)
Unknowns phi and q, scalars of (R, mu) smooth in (r^2, z). Three element types share one Legendre basis P_n(mu), n <= nmax:
ball R <= R1: P_n(mu) rho^n Q_k(2 rho^2 - 1), n + 2k <= D (all axisymmetric Cartesian polynomials of degree <= D: axis and
origin regularity built in), with Q_k the Jacobi polynomial P_k^(0, n+1/2) (3D Zernike radial family; campaign default since
2026-10-28T20:31:12Z) or, in the states computed before that date, the Chebyshev polynomial T_k (nearly dependent at high n: Jacobian condition 2e10,
54 near-null directions; see FAILURE_ANALYSIS.md 6 and 6b); shells: P_n(mu) T_k(x), x the log map of [Rlo, Rhi]; exterior R >= Rm: P_n(mu) (R/Rm)^-e with
the exponent set generated from {alpha} and {3, 4, ...} by (a, b) -> a + b + 1 (phi) and from {alpha + 1} (q), so R^-alpha,
R^-(2 alpha + 1), R^-3, R^-4, R^-(3 alpha + 2), ... are representable and the fractional powers are factored analytically.
Continuity rows impose phi in C^3 and q in C^2 at interfaces (velocity Cartesian C^2).

## Residual and optimizer
Rows: sqrt(w_node) scale_q R_q and sqrt(w_node) scale_eta R_eta at tensor Gauss nodes (balanced dyadic shells, no volume
factor), scale = (1 + R^2)^((2 alpha + 2 + s)/4) and (1 + R^2)^((2 alpha + 3 + s)/4) with shift s in {0, -2}; interface
rows; Tikhonov on non-leading exterior coefficients; one gauge row (int F_theta^2 dS or int |F|^2 dS = target on the
leading tail; working gauge of section 5 of the pre-registered specification, converted to int |F|^2 dS = 1 for reporting); optional S1 rows with the source
position z0 as an unknown (phi_z(0, z0) = 1/2, c_l z0 + 2 phi(0, z0) = 0, optionally q(0, z0) = q0). Analytic Jacobian
(autograd through the operator at the nodes times the basis derivative matrices; c_l column by central differences).
Optimizers: dense Levenberg-Marquardt (Cholesky normal equations on GPU, gain-ratio damping) and torch L-BFGS with
strong Wolfe line search; sequences lm and lbfgs -> lm. Float64 throughout (torch.float64 tensors checked in tests).

## Diagnostics
Holdout grids (non-integer multiples of the training resolution, exact axis points, origin collar, log-spaced far field):
unweighted R_q, R_eta, scaled far-field residuals R^(2 alpha + 2) R_q and R^(2 alpha + 3) R_eta, interface jumps, spectral
decay, tail connectedness, swirl ratios, vorticity maximum and core radius. Metrics of section 6.1 of the pre-registered specification (src/axi/validate.py): dyadic shells
in units of a_eff with Gauss, random and axis-collar sets; rho_E = RMS(R_E)/min(RMS L_E, RMS N_E) for M^r, M^theta, M^z
(with the full-space pressure), q, eta, div; m_E likewise with the maximum.

## Full-space pressure (problem statement section 7)
-Delta P = sum_ij d_i U_j d_j U_i, Legendre modes, P_l(R) = [R^-l-1 int_0^R s^l+2 f_l + R^l int_R^inf s^1-l f_l]/(2l+1),
panels following the elements plus geometric exterior panels to 1e6 Rm, f_l interpolated by Chebyshev polynomials per
panel and integrated by Gauss quadrature from the evaluation radius outward or inward (avoids the (b/R)^(l+1)
amplification of round-off), analytic power-law remainder beyond the last panel. Tests: 1e-11 to 1e-15 on manufactured P.

## Planned second method (Stage II)
Transport fixed point following the structure analysis of the report author: given W_m, integrate q along backward characteristics from the
S1 source (Koopman eigenfunction with eigenvalue 2 c_l - 1, q(y0) = q0), then eta by transport with the d_z(q^2) source,
then phi = Delta_5^-1(-eta) by the 5D Green's function with the exterior integrated to infinity, and iterate with the
resonance condition phi_z(0, z0) = 1/2 selecting c_l (or q0). This is numerically independent of the collocation solver.

## Branch machinery added 2026-10-28T20:54:15Z (following the branch analyses of the report author)
- Parity restrictions (separate experiments, labelled): Config.parity_phi / parity_q in {odd, even} keep only the Legendre degrees
  n of the corresponding parity in every element (z -> -z is mu -> -mu at fixed R).
- Generic weighted constraint rows (Config.point_rows): weighted linear functionals of phi, q or eta = -Delta_5 phi at a point (value, d_r, d_z,
  d_rr, d_rz, d_zz, d_s, d_sz), with targets that may depend on c_l and the branch amplitude K (target_expr); rebuilt when c_l
  changes in free-c_l runs, so the finite-difference c_l column of the Jacobian includes the target dependence.
- Axis rows for q (Config.axis_rows_q): q(0, z_j) = 0 at log-spaced axis points (q = s x smooth, needed by the T2 ring portrait).
- T2 (odd swirl, equatorial ring source at r = 1): rows phi_z(0, 0) = (1 + 3c)/2, phi_z(1, 0) = c, phi_sz(1, 0) = -(1 + c)/2,
  eta_z(1, 0) = 2K^2/(3c), q_z(1, 0) = K; phi, q odd; axis rows; the ring radius is the dilation gauge (tail gauge row off); c_l free.
- T3 (even swirl, S1 pair at z = +-1 with a central axial-inflow saddle): rows phi_z(0, 0) = -(1 + 2c)/2, phi_z(0, 1) = 1/2,
  phi(0, 1) = -c/2, q(0, 1) = K; phi odd, q even; 24 equator rows q(r_j, 0) = 0 (the report author's Lemma 14, AXISYMMETRIC_OBSTRUCTION_AUDIT.md); c_l free.
- Explicit swirl amplitude (Config.amp_param): q = A qhat, qhat(0, z0) = 1, eta rows divided by A^2 (suggestion of the external referee); the
  worker converts the final state back to physical q.
- Method 2 (src/axi/fixedpoint.py): the transport/elliptic fixed point phi -> q0^2 Delta_5^-1(-eta[phi]) with the S1 condition,
  solved by scipy newton_krylov (LGMRES, finite-difference Jacobian action); unknowns (phi, q0) or (phi, c_l).
- Solver tests: tests/test_optimizer_manufactured.py (forced manufactured solution recovered to round-off on the Jacobi basis).

## First far-field correction slaved to the leading tail (2026-10-28T21:53:20Z; src/axi/farfield.py, tests/test_farfield.py)
In the reduced variables the first nonlinear correction is algebraic in (A, B): with phi = R^-alpha A + R^-(2 alpha + 1) A1,
q = R^-(alpha + 1) B + R^-(2 alpha + 2) B1 and 1/c = alpha + 1, the q equation at order R^-(2 alpha + 2) has the coefficient
1 - c(2 alpha + 2) = -1 of q1, so B1 = R^(2 alpha + 2)[U0 . grad q0 + 2 (U0^r/r) q0]; the eta equation at order R^-(2 alpha + 3) has
1 + c - c(2 alpha + 3) = -1, so E1 = R^(2 alpha + 3)[U0 . grad eta0 - d_z(q0^2)]; and A1 follows from the 5D mode equation,
a1_l = e1_l/(l(l + 3) - (2 alpha + 1)(2 alpha - 2)) in Gegenbauer C_l^(3/2) modes (denominator >= 1.1 for 1/2 < c_l < 3/4: no resonance;
the pressure enters only the primitive reconstruction). Test (c_l 0.56, 0.60, 0.68, 0.74, random degree-3 A and degree-2 B): the
leading tail alone leaves R^(2 alpha + 2) R_q and R^(2 alpha + 3) R_eta constant in R; with A1, B1 both decay like R^-(1/c) between
R = 1e2 and 1e4 (measured exponent within 0.2 percent of 1/c), i.e. the residual drops by 1e-4 to 1e-5 at R = 1e3.

## Initialization families (state at 2026-10-28T22:18:54Z)
gauss_core, ring_core, flat_core, asym_dipole, swirl_dominant, poloidal_dominant, random_spectral (seeded generic cores with random
leading tails); s1_sym_v2 / s1_shift_v2 (from the report author's analysis: S1 structure at the origin or at z0 with the curvature relation built in);
ring_t2 (from the report author's analysis: odd-swirl ring source); pair_t3 (from the report author's analysis: S1 pair with central saddle,
optional saddle-strain repair proposed by the report author); t1budget (the external referee's positive-induced-strain T1 seeds, phi = z(1 + 3z^2)/(2(1 + a s + z^2)^(1 + 1/(2c))),
q = q0 h with h the unit-amplitude characteristic swirl interpolated from the referee's grids in configs/t1budget_seeds; q0 pinned
to the ladder values proposed by the report author). Every seed is an initial guess; the solve is constrained only by the documented rows.

## Stage II additions (2026-10-29T01:40Z)
- Config.z0_fixed: with the S1 rows, holds the source at z0 = z0_init (no z0 unknown); used with parity_phi = odd, parity_q = even for the
  reflection-class ladder (source at the origin; in this class d_0 = 0 and the axial pressure dipole vanish by parity). Jacobian checked
  against finite differences (1e-12) for the pinned, slaved-exterior, parity-restricted configuration.
- Variable projection (lm.VarProProblem, worker stage "varpro"): q slaved to (phi, scalars) by the hard-pinned least squares of every row
  that is linear homogeneous in q at fixed phi (PDE q rows, q interface-continuity rows, q Tikhonov rows, q-correction slave rows);
  reduced Jacobian J_outer + J_q dq*/dy with dq*/dphi = -N (AN)^+ G (Golub-Pereyra form with the inner-residual term dropped; scalar columns
  by central differences); verified against finite differences to 1e-8. Not used for production: the reduced problem has a curvature of
  order 1e20 along the gradient because q* is hypersensitive to phi under the job's row weighting (FAILURE_ANALYSIS 17).
- Frozen-phi swirl diagnostics: q_eigen_values.py (continuous q*, value-based comparison with the state's q, eta-row cost of (phi, q*),
  singular directions, B(mu), source-adaptive points) and homotopy_q_test.py (q_t = (1 - t) q_state + t q* path and phi-only refits with
  the dilation-gauge target held at its (phi, q_t) value, since the gauge is a normalization and q*'s swirl tail alone exceeds the original
  target). FrozenQProblem (phi free, q frozen) is the second optimizer wrapper used by the homotopy refits.
- Chain driver (scripts/chain_driver.py): sequential fixed-c_l continuation with least-squares transfer of the previous converged state onto
  the new exterior exponent set, level jobs (D24, D48) and matching-radius-doubled runs at selected c_l, optional per-step q0 pins.
- CPU-only mode (since 2026-10-29T00:57:59Z): supervisor slots cpu0.. with CUDA_VISIBLE_DEVICES empty and --device cpu; one LM iteration costs 0.31 s
  (D24), 1.3 s (D36), 4.4 s (D48) per core at nice 19 on the loaded box; D64 is not affordable.

## Additions of 2026-10-29T07:10Z
- Sensitivity and robustness suite for the best interior state (scripts/make_stage2_sensitivity.py, scripts/make_relative_perturbations.py;
  FAILURE_ANALYSIS 18): re-optimizations of the 0.74 direct-seed state with one setting changed each (outer interface R = 5 and 20 with the
  least-squares transfer onto the new exterior exponents; 1.5 times the automatic quadrature node counts; interface weight 1000; shell weight
  power shift s = 0; perturbed coefficients with per-coefficient relative Gaussian noise of 1e-2, 3e-2, 1e-1; torch L-BFGS with strong Wolfe
  followed by LM; q0 pins 1.8, 2.0, 3.0, 3.5). The first perturbation design (noise relative to the global RMS coefficient) was wrong for a
  basis whose exterior coefficients are orders of magnitude smaller than the ball coefficients and is recorded as such.
- Small-step chains fmE (from the 0.74 direct-seed state downward, 0.005 steps) and fmF (from the 0.68 state upward) with scripts/chain_driver.py.
- Per-class run counts (scripts/class_counts.py; its output table is in the run records, not published) by job prefix for the six classes of FINAL_REPORT 4.6; the T1-class
  table that scripts/failure_map.py writes (FAILURE_MAP.md, not published; the per-run rows are in FAILURE_MAP.csv) uses the widened selector (Stage II prefixes plus fmC, fmD, fmap, freecl_ and the Stage I ladder seeds t1lad*).
- One-command refresh of every derived table, figure and the internal artifact bundle (a packaging script of the internal bundle, not published);
  scripts/resource_totals.py also sums the bounded invocations of the nested closed-problem solves (t1nk2) from their logs (run records, not published).

## Known bookkeeping defects of the run records (recorded 2026-10-29T12:36Z, Stage III; code unchanged)
- n_iter of result.json is len(history). When a job is resumed from its checkpoint inside a Levenberg-Marquardt stage, the worker appends the
  optimizer's history, which restarts from the saved prefix, to the saved history, so n_iter double counts the prefix (the six runs resumed on CPU
  after the GPU withdrawal and the two disposable Stage III resume tests; records of the independent verifier of 2026-10-29T12:28Z and 12:31Z). The per-stage count
  stage_status[].it and the LM iteration lines of log.txt are correct; no extra optimization step took place; the recomputed last-20-percent cost
  ratios change no failure class. The table and list of the affected runs are in the run records (not published).
- elapsed_s of a resumed run is the sum of all its segments (the checkpoint stores the earlier elapsed time). For the six runs above the earlier
  segments ran on GPUs (2239 s in total), so the summed elapsed_s of the device-cpu runs (19.4 hours) is job wall time, not CPU-only time
  (CPU-only part approximately 18.8 hours of prevalidation elapsed wall time, the final validations not included; resource totals in the run records, not published). The GPU-slot hours of phase 1 count only runs finished before the withdrawal.
- The worker code was left unchanged in Stage III on purpose: the shipped supervisor/worker.py is the code that produced every record and passed
  the protected clean-process resume test of 2026-10-29T12:21:52Z to 12:26:55Z (log logs/tests/stage3_tests_20261029T122152Z.log in the run records, not published). A fix (do not re-append the
  duplicated prefix after a resume) is a one-line change for a future campaign and is not applied here.
