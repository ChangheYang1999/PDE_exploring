# FAILURE_ANALYSIS.md (primary numerical search). Updated 2026-10-28T19:54:05Z; later sections carry their own dates.

Run directories named below (runs/...) belong to the full run archive (runs/, checkpoints/), not published; scratch scripts and test logs
cited below belong to the run records (not published). "Pre-registered specification x.y" cites section x.y of the pre-registered specification.

## 1. Swirl-free collapse (first pilot runs, generic Gaussian cores, c_l = 0.6)
Unconstrained least squares from Gaussian cores converged toward swirl-free potential-like fields with a fictitious
decaying tail made of cancelling exterior powers. Cause: the zero field and swirl-free fields are exact solutions of the
reduced system (CIV's remark excludes smooth decaying swirl-free profiles with a nonzero tail, but the optimizer sees
only the collocation residual), and nothing in the loss rewards swirl. Mitigations: swirl gauge (int F_theta^2 dS fixed)
as a working gauge, separate exponent sets for phi and q, Tikhonov on non-leading exterior coefficients, exterior nodes
over several decades.

## 2. Levenberg-Marquardt stall from row scaling (pilot sweep)
With interface weight 10 and PDE rows unnormalized, the interface block dominated the initial cost (1e9) and the
damping parameter stayed at 1e3 to 1e4 (steps too small to matter). Fix: interface weight 100, S1 weight 300, and PDE
rows divided by the norm of their linear term at the seed (auto_row_scale). The solver then runs at damping 1e-6 to 1e-8
(Gauss-Newton regime), interfaces match to 1e-4 relative and the S1 rows hold to 1e-5. The far-field node range
(1e2 vs 1e4 R_m) was irrelevant to the stall.

## 3. Slow crawl of the pilot sweep (800 LM iterations)
All S1-constrained pilots at c_l in {0.505, 0.525, 0.56, 0.60, 0.68} reached the iteration cap with the weighted cost
decreasing 5 to 10 percent per 50 iterations and holdout relative residuals 0.1 to 0.7 (rho_max of the pre-registered specification about 10). The S1
rows (phi_z(0, z0) = 1/2, W_z(0, z0) = 0) are satisfied, but the swirl decays during the solve (s_core = 0.002 at the end of
the best c_l = 0.6 job): the S1 condition is necessary for swirl, not sufficient. Next experiment: pin q(0, z0) = q0 and
free c_l (the report author's one-parameter-family heuristic), queued as sweep s1pin1.

## 4. Transport/elliptic Picard iteration (method 2 experiment, 2026-10-28T20:00:35Z, scratch script picard_experiment.py, not published)
Given phi^k: q = least-squares Koopman eigenfunction of W_m (pinned at the source), eta from (1 + c_l) eta + W_m . grad eta
= d_z(q^2), Phi = Delta_5^-1(-eta) by the 5D Green inverse, q0^2 = 1/(2 Phi_z(0, z0)) to enforce phi_z(0, z0) = 1/2. At
c_l = 0.6 from the s1_sym_v2 seed the iteration drifts: Phi_z(0, z0) falls monotonically (0.22, 0.14, 0.084, 0.055, 0.034,
0.018 with damping 0.2) and q0 grows (1.5 to 5.3); with damping 0.5 Phi_z turns negative at the third iteration and the
scale selection fails. The q-eigenproblem relative residual stays at 4 to 8 percent (W_m of these iterates admits no smooth
eigenfunction to better than that). Reading: the swirl-induced source d_z(q^2) of the eta equation produces, through
Delta_5^-1, an axial strain at the source that is too weak (or of the wrong sign) to sustain the Burgers value
phi_z = 1/2 unless |q| increases away from the source along the axis, which in turn (structure analysis of the report author) requires
phi_z > 1/2 next to the source. This positive feedback must close self-consistently; the plain Picard map moves away from
it and the least-squares optimizer resolves the tension by shrinking q. Check by the external referee (a second model), 2026-10-28T20:14:35Z:
the local equations do not fix the sign of q_zz at the source (q_zz < 0 with q_rr > 0 is allowed by the curvature relation),
the S1 Green condition is a signed integral over the whole half-plane (eta need not be positive on the upper axis; in the
reflection class it must change sign in z > 0), and the drift of the Picard map neither proves repulsion at a solution nor
nonexistence at this c_l; the earlier remark here that a Newton iteration 'would not have this drift' was unproved and is
withdrawn. The referee's constructive suggestion, an explicit swirl amplitude A with q = A qhat, qhat(0, z0) = 1 and the eta
rows divided by A^2 (so that shrinking the swirl no longer lowers the loss), is implemented (Config.amp_param) and runs as
sweep s1amp1.

## 5. Retro-validated pilot states (2026-10-28T20:00:35Z): rho_max of the pre-registered specification between 6.7 and 13 on all 38 validated jobs, core swirl fraction
s_core between 0.002 and 0.024 (pre-registered specification 6.4 requires >= 0.05 for labels A or B). No pilot state is a candidate.

## 6. Optimizer basin test on a forced manufactured solution (2026-10-28T20:19:54Z, tests/test_optimizer_manufactured.py)
To separate optimizer limits from the physics, the system is forced so that the S1 seed state x* is an exact zero of the
weighted residual (r_offset = r(x*)), and LM is started from x* perturbed by a relative random amount. Small problem
(D = 16, nmax = 8, nx = 438, 5 percent perturbation): converges to round-off in 146 iterations (cost 1.4e9 to 1e-20,
|x - x*|/|x*| = 3e-9). Pilot size (D = 24, nmax = 12, nx = 815): 10 percent perturbation with the amplitude unknown ends at
cost 2e8 after 200 iterations far from x* (|x - x*|/|x*| = 2.4); 5 percent perturbation with c_l free and off by 0.01 ends
at cost 2e4 after 200 iterations (|x - x*|/|x*| = 0.89, c_l error 0.02). So at pilot size the basin of attraction of an exact
solution under random coefficient perturbations is narrower than 5 to 10 percent for 200 LM iterations: the pilot sweep's
non-convergence is at least partly an optimizer limitation, not evidence about the physics. Follow-up (scratch script basin_test.py, not published;
run records): perturbation sizes 1, 3, 5, 10 percent, smooth-only perturbations, and larger initial damping.
Consequences for the campaign: (i) refinement must proceed by continuation from converged lower-resolution states, never by
cold starts at high resolution; (ii) longer runs (thousands of iterations) are justified; (iii) a globally convergent
alternative (e.g. Newton with line search on the hat variables, or homotopy in the forcing) is a Stage II priority.

## 7. Explicit-amplitude branch escapes to large swirl (2026-10-28T20:26:09Z, sweep s1amp1, first 6 jobs)
With q = A qhat, qhat(0, z0) = 1 and the eta rows divided by A^2, the optimizer drives A from 1 to 10 to 90 (core swirl
fraction 0.77 to 0.99) while the eta equation stays unsatisfied (relative residual 0.8 to 1.0, i.e. the residual equals the
source term 2 qhat qhat_z): dividing the rows by A^2 makes a large A cheap because the seed-based row scaling already
under-weights the eta rows. Together with section 3 (swirl collapse without the amplitude) and section 5, this shows that
the weighted least-squares objective has degenerate descent directions in both directions of the swirl amplitude unless the
eta equation is weighted so that neither escape is cheap. The remaining 39 s1amp1 jobs were moved to queue/held to free GPU
time; the six finished ones are kept as the record of this escape.

## 6b. Resolution of the basin problem: the ball basis was ill-conditioned (2026-10-28T20:31:12Z, scratch scripts nullspace.py and jacobi_basin.py, not published)
The right singular vectors of the column-scaled pilot Jacobian for the 54 singular values below 1e-8 sigma_max are supported on
the high-order ball modes of q and phi (Legendre degree n >= 6 with radial index k >= 3) and on the near-coincident exterior
exponents 4.67, 5.0, 4.0. The original ball basis rho^n T_k(2 rho^2 - 1) P_n(mu) is nearly linearly dependent at high n (the
rho^n factor concentrates every column near rho = 1). Replacing T_k by the Jacobi polynomial P_k^(0, n+1/2) (the 3D Zernike
radial family, orthogonal on the ball; same polynomial space) and cutting the exterior at emax = 4 gives: column-scaled
condition 1.1e8 (was 2.0e10), 2 singular values below 1e-8 (was 54), and the forced manufactured solution is recovered from a
3 percent perturbation to round-off in 125 iterations (Chebyshev: cost 27 after 300 iterations) and from a 10 percent
perturbation to cost 5e-8 within 300 iterations. Cholesky and QR steps now behave the same. Decision: ball_radial = jacobi and
emax = 4 for all new jobs (sweep pilot2 and critical2, 207 jobs, launched 2026-10-28T20:31:12Z); the held pilot1 generic jobs are not run.
The pilot1 results (sections 3, 5, 7) therefore reflect an optimizer limitation as much as the physics.

## 8. Shell-wise anatomy of the pilot2 stall states (2026-10-28T20:38:34Z; runs/p2_cl0p600_*/validation.json)
With the well-conditioned basis the c_l = 0.6 states end where the pilot1 states ended (rho_max 7 to 14, s_core 0.001 to
0.012, costs 0.09 to 0.35 after 800 iterations). Per dyadic shell (units of a_eff about 2): rho_q = 1 to 3 and rho_eta = 0.4 to
2 in the core (k <= 0); in the far shells (k >= 3) the single-term ratios sigma_E = RMS(R_E)/RMS(L_E) fall like R^-(1/c_l)
(1e-5 at k = 11, i.e. the leading homogeneous tail is in place) but rho_E stays at 0.9 to 1.7 and the scaled residuals
R^(2 alpha + 3) R_eta are constant (1.7e3): the first nonlinear far-field correction is not represented by the optimized
exterior coefficients, exactly the failure mode section 9 of the problem statement warns about. So these states are not approximate
solutions anywhere, neither in the core nor in the tail, and the universal eta relative residual of 0.60 to 0.64 reflects the
size of the eta equation's nonlinear terms, not a partial solution. Tool consistency on the same states: the 5D Green
inverse of the candidate's own eta reproduces phi to 3e-7 relative and gives phi_z(0, z0) = 0.4999981 for the imposed S1 value
1/2 (moment check of pre-registered specification 6.6), so the representation and the elliptic tools are mutually consistent.

## 9. Newton-Krylov fixed point (2026-10-28T20:40:04Z, src/axi/fixedpoint.py; log in the run records)
Unknowns (phi, q0) at c_l = 0.6, D = 16, nmax = 8, from the s1_sym_v2 seed (|F| = 3.9 at the seed; Phi_z(0, z0) = +0.21).
The first Newton step reduces |F| to 0.48 but turns Phi_z(0, z0) negative (-0.056, then -0.032), after which the scalar
equation q0^2 Phi_z = 1/2 has no real solution and the Armijo line search stalls (|F| = 0.350 for eight iterations, q0 drifting
0.22 to 0.20, q-eigenproblem relative residual 2e-2, eta transport residual 0.12). Same qualitative outcome as the Picard
iteration (section 4): the swirl-induced meridional flow has the wrong axial strain sign at the source for this seed family.
A variant with (phi, c_l) as unknowns at fixed q0 = 1 bounced c_l between the bounds 0.501 and 0.749 (|F| 3.3 to 5.0, NoConvergence after 14 Newton steps): no root of the fixed-point map near this seed in either parametrization.

## 10. Where the crawl ends: continuation to 3000 iterations (2026-10-28T21:02:58Z, runs/cont1_*)
Six pilot2 S1 states (c_l = 0.525, 0.60, 0.68; Jacobi basis) were continued for 3000 further LM iterations (0.08 s per
iteration at D = 24). The weighted cost fell from 0.09 to 0.35 down to 0.003 to 0.07, and every state lost its swirl entirely
(s_core = 0.000 to three decimals, rho_max 12 to 28, eta relative residual still 0.5 to 0.7). With the S1 rows still satisfied,
the least-squares path from these seeds ends in swirl-free fields: failure class F1 for the whole T1 single-source branch at
pilot resolution, independent of the basis conditioning. This matches the report author's structural statement that a
smooth swirling solution is a codimension-one event that an unconstrained least-squares descent does not find.

Addendum to section 10 (2026-10-28T21:38:56Z): the small continuation costs are descent toward the trivial branch (zero solves
the equations at every c_l; a swirl-free nonzero decaying profile is excluded by the CIV argument), not progress toward a solution.
Continuation jobs must keep the q0 pin (or a bounded amplitude) and the dilation gauge; their cost is not reported as approach to a solution.

## 11. Far-field row weights (test proposed by the report author; 2026-10-28T21:46:27Z; scratch script farfield_weight_test.py, not published; run records)
Three weightings were compared on the Jacobi basis: (i) divisor 4 (rows ~ R^((2 alpha + k)/2), the original choice), (ii) divisor 2
(rows ~ R^(2 alpha + k), the multipliers of the pre-registered specification), (iii) divisor 2 normalized at each dyadic-shell centre (balanced shells carrying the
scaled residual of the pre-registered specification with an O(1) factor). Manufactured recovery (forced S1 seed, 3 and 5 percent perturbations, 400 iterations):
(ii) stalls at cost 1e-9 with |x - x*|/|x*| = 0.2 to 0.4 because the far rows dominate the seed-based row scaling and the core
becomes invisible; (i) and (iii) converge comparably (|x - x*|/|x*| 0.10 and 0.11 at 5 percent after 400 iterations). Rerun of the best
s1pin2 states (fixed c_l, 400 iterations): with (i) the exterior scaled residual R^(2 alpha + 3) R_eta stays at 1.5e3 to 2.0e3 (flat
in R) as in section 8; with (iii) it stays at 2.1e3 to 2.5e3 while the core residuals remain O(1) (swirl 0.67, rel eta 0.48). So the
weighting alone does not make the optimizer resolve the first far-field correction while the core is unsolved: the far rows are a
small part of an O(1) cost everywhere. The isolated exterior-only test (below) separates representability from optimization.

Addendum (2026-10-28T21:48:18Z, scratch script exterior_fit_test.py, not published): exterior-only Gauss-Newton on the best c_l = 0.6 state (leading tail A, B and all inner
elements frozen; only the exterior correction coefficients free; exterior q and eta rows with the shell-normalized weights of the pre-registered specification) lowers
the weighted exterior cost by 2 to 4 orders of magnitude, but the unweighted scaled residual R^(2 alpha + 3) R_eta becomes larger at
large R (2e3 flat -> 1.4e3 at k = 3 but 1e4 to 5e4 at k >= 6) while R^(2 alpha + 2) R_q changes little, for emax 4 and 6 and for
nmax 12 and 18. The optimizer trades the eta rows (seed row scaling w_eta/w_q about 0.08) against the q rows: the exterior
equations cannot be satisfied together by adjusting the correction coefficients while the leading tail (A, B) is that of a
non-solution core. Conclusion of the far-field weighting test: the weighting is not the limiting factor; the first far-field correction must be slaved
algebraically to (A, B) (eta_1 = R^-(2 alpha + 2) E_1 with (c - 1) E_1 = the quadratic forcing of the leading tail, phi_1 from the
5D mode equation at exponent 2 alpha + 1), which is a Stage II representation change.

## 12. T2 branch (odd swirl, equatorial ring source), first four runs (2026-10-28T21:58:52Z, runs/t2a_*, t2_diagnostics.json)
Setup: the report author's ring_t2 seed, phi and q odd in z (parity masks), five weighted constraint rows (phi_z(0,0) = (1 + 3c)/2, phi_z(1,0) = c,
phi_sz(1,0) = -(1 + c)/2, eta_z(1,0) = 2K^2/(3c), q_z(1,0) = K), 24 axis rows q(0, z_j) = 0, ring radius as the dilation gauge,
c_l free in (0.501, 0.749), K in {1, 2}, c_l start 0.60 and 0.68, 1500 LM iterations or 1200 s (Jacobi basis, D = 24, nmax = 12).
Outcome: c_l ran to a bound in every run (0.501 once, 0.749 three times); rho_max 129 to 620; s_core 0.005 to 0.008 (collapsed);
weighted costs plateau at 4e2 to 3e3; constraint-row defects 0.001 to 0.48 (the ring rows are not met); q on the axis is zero to
2e-2 (imposed) but eta on the upper axis is not (32 to 84 in absolute value, negative far out as required but nonzero near the ring),
and min_s eta_z(s, 0) is negative (-7 to -36) where the exact portrait needs eta_z(s, 0) > 0 for all s (T2 analysis of the report author). Failure class
F1 with the F3 structural violations above. The smooth-stratum saddle rows (phi_z(0, 0) = (1 + 3c)/2) force the smooth stratum; the
C^2 class allows non-quantized saddles (analysis of the report author), so this failure map row is labelled "T2, smooth stratum".

Second addendum (2026-10-28T22:12:19Z, runs/slv1_s1pin2_*): the best s1pin2 states were continued for 2000 iterations with the first far-field
correction slaved to (A, B) (Config.slave_correction, rows satisfied to 1e-9 to 6e-6 of the weighted cost) and the Tikhonov exemption.
Outcome: rho_max 6.4 to 25, s_core 0.009 to 0.051, s_far <= 0.035 (B2 fails), c_l drifting downward (0.56 -> 0.537 and 0.508;
0.68 -> 0.656; 0.72 -> 0.704; 0.74 -> 0.730); the exterior scaled residual R^(2 alpha + 3) R_eta is 350 to 1900 (was 2000), with the
remaining exterior eta cost 1e-3 to 1e-2 of the total: for these cores the exterior cannot be made consistent because the
leading tail itself is not that of a solution (and the correction's angular content beyond degree nmax = 12 is truncated).
The verdict of section 11 stands: the far-field treatment is now correct by construction at the first nonlinear order, and the stall is
in the core; failure class F1 for all five reruns.

## 13. Pinned-q0 ladder from the referee's positive-strain seeds (2026-10-28T22:22:59Z, runs/t1lad_*, t1lad2_*)
These seeds, forwarded by the report author (phi = z(1 + 3z^2)/(2(1 + a s + z^2)^(1 + 1/(2c))), q = q0 h with the characteristic swirl h) carry a narrow
axial swirl column (radial aspect a = 8 at c_l = 0.60: h drops from 1.18 on the axis to 0.84 at mu = 0.99 at R = 0.5). At the pilot
resolution (nmax = 12) the seed is under-resolved: ball fit error of q 16 percent, exterior 26 percent, q jump across R = 2 of 0.6 of
its scale, initial interface cost 6e13. The first such run (c_l = 0.60, q0 = 12) ended at cost 2.4e8 with c_l at the bound 0.749,
rho_max 9.7e3 and s_core 0.90 (a meaningless state). The remaining nmax-12 ladder jobs were held; the ladder is rerun at D = 36,
nmax = 24 (t1lad2, 9 jobs).

Interim (2026-10-28T22:33:56Z, runs/t1lad2_*): at D = 36, nmax = 24 the c_l = 0.74 ladder seeds (aspect a = 1, q0 2.5 and 3.5) fit and optimize
normally (weighted cost 0.43 and 0.86 at 500 iterations), whereas the c_l = 0.60 (a = 8, q0 4 and 12) and 0.68 (a = 2, q0 3) seeds start
at interface costs of 1e15 and are still at 1e10 to 1e13 after 400 to 750 iterations: the Levenberg-Marquardt path from these
under-resolved, sharply peaked seeds does not even recover element continuity. The joint seed fit (interface rows included) now in
Problem.fit_function lowers the starting interface cost by three orders of magnitude for future runs but does not change these.

Result (2026-10-28T22:48:33Z, runs/t1lad2_cl0p740_q2p5_freecl_lm, exported as candidates/T1_ladder/L0): the c_l = 0.74 ladder seed with q0 = 2.5
(aspect a = 1) is the first state of the campaign that passes B2: s_core = 0.84, s_far = 0.84, rho_max = 4.6 (M^z in the core shell
k = -3; q 2.75, eta 4.07), m_max = 31, weighted cost 0.42 after 1200 iterations (still decreasing slowly), c_l driven to the upper
bound 0.749. Structure: exactly one zero of W_m in the half-plane, an S1 source at the origin with A = -1/2 and q0 = 2.5 (the
pinned value); |q| grows along the axis to 3.44 at z = -1.08 (max|q|/K = 1.38), where U^r/r = -0.447 (swirl-maximum condition
defect 0.053); the source is a saddle of q (q_rr = -17.4, q_zz = +5.9); the source jet has p_z = +0.61 (positive axial cubic, the
sign the referee's analysis requires) and p_s = -0.82, jet ratio 0.81 against the closure value K^2/(1 + c)^2 = 2.04; eta is positive
just above the source and changes sign; the 5D Green moments reproduce phi(0, 0) and phi_z(0, 0) = 0.499988. The residuals are O(1)
in the core shells (rho 1 to 4 for k = -3..1) and 0.63 for eta in the far shells (scaled R^(2 alpha + 3) R_eta = 36, flat), so this
is not an approximate solution; it is the branch to continue (lad2cont, fixed c_l = 0.749 and 0.74), to refine (lad2ref: D 48,
nmax 32), and to run with a wider c_l range as an exploratory check of the class boundary. The q0 = 3.5 companion ends at
rho_max 9.5, s_core 0.91. The c_l = 0.60 and 0.68 ladder seeds (a = 8 and 2) fail as described above (rho 3e2 to 1e6).
Structural check (2026-10-28T22:49:28Z): the leading tail of this state has a sign-changing B(mu) (negative near the equator, positive near the poles; the
U^theta field shows a negative band around z = 0 for r > 3), whereas the single-source rule (MATHEMATICAL_FORMULATION
section 6c) requires one-signed B when the only zero of W_m is an S1 source. So the state violates an exact necessary condition
(failure class F3 besides the O(1) residuals); the equatorial counter-swirl is the first thing the continuation must remove.

## 14. T3 branch (S1 pair at z = +-1, central saddle), three runs (2026-10-28T22:50:48Z, runs/t3a_*, t3_diagnostics.json)
Setup: the report author's pair_t3 seed (separated form, saddle sign defect uncorrected), phi odd and q even in z, rows phi_z(0,0) = -(1 + 2c)/2,
phi_z(0,1) = 1/2, phi(0,1) = -c/2, q(0,1) = K = 1, 24 equator rows q(r_j, 0) = 0, c_l free from 0.60, 0.64, 0.68 (Jacobi basis,
D = 24, nmax = 12, 1500 iterations). Outcome: c_l ran to the upper bound 0.749 in all three; rho_max 239, 2.4e4, 800; s_core 0.012 to
0.042 (B2 fails); weighted costs 1.7e3 to 5e4 at the iteration cap: failure class F1 (smooth stratum, saddle rows imposed). The
T3 diagnostics of the report author (Q, e versus 2KQ/(1 + c), axis first integral, finite part, equator relation) are in each run's
t3_diagnostics.json; a repaired-seed variant (t3b, saddle sign fix proposed by the report author) is available but was not run before the Stage I
deadline because the T1 ladder branch took priority.

Continuation at fixed c_l = 0.749 (2026-10-28T23:11:18Z, runs/lad2cont_*): 3000 further LM iterations lower the weighted cost from 0.42 to 0.0088
(q0 = 2.5) and from 0.86 to 0.0042 (q0 = 3.5), still decreasing. Holdout: q0 = 2.5: rho_max 4.24 (M^z; q 2.18, eta 2.52), s_core 0.54,
s_far 0.62, relative residuals q 0.081, eta 0.046; q0 = 3.5: rho_max 1.88 (the lowest of the campaign), s_core 0.60, s_far 0.59, q 0.068,
eta 0.022. The eta equation is now satisfied to a few percent while the momentum equation with the full-space pressure still fails by
O(1) in the core shells. Exported as candidates/T1_ladder/L1 (q0 = 3.5). Follow-ups queued at the top of the queue: another 3000
iterations for both, a refinement level (D 48, nmax 32) from the q0 = 3.5 state, a q0 = 4.5 pin and a c_l = 0.745 neighbour.
q0 and c_l neighbours (2026-10-28T23:19:16Z, runs/lad2q*, lad2c07*): from the q0 = 2.5 ladder state, 2500 to 3000 iterations at fixed c_l = 0.749 with the
pin moved give rho_max 4.01 (q0 = 2.0, s_core 0.49), 4.24 (2.5), 3.36 (3.0, s_core 0.57), and the separately seeded q0 = 3.5 branch
1.88: the residual floor decreases with q0 over the tested range. At fixed c_l = 0.74 the q0 = 2.5 state ends at 5.97 (versus 4.24 at
0.749): the branch prefers the upper end of the class. The refinement level D 48 / nmax 32 from the q0 = 2.5 state and the c_l = 0.73
and wider-c_l runs are pending.
Refinement level (2026-10-28T23:21:38Z, runs/lad2ref_*): the q0 = 2.5 state refined from D 36 / nmax 24 / K 24 to D 48 / nmax 32 / K 32 (2000 iterations) gives rho_max 2.79 versus 4.24 at the coarser level (s_core 0.51, eta 0.044, q 0.086): an improvement by 1.5, below the factor 2 the refinement reading of pre-registered specification 9.1 requires for a decreasing floor; a third level is needed before the branch can be read.
c_l neighbour at 0.73 (2026-10-28T23:25:01Z, runs/lad2c073_*): rho_max 36 (s_core 0.50, eta 0.049, q 0.082) versus 5.97 at 0.74 and 4.24 at 0.749 from the same q0 = 2.5 state: the residual floor of this branch rises steeply as c_l decreases from the upper end of the class, which is continuation evidence that the branch, if it closes at all, does so at or above c_l = 3/4 (the exploratory run with bounds up to 0.80 is pending).
Exploratory run beyond the class (2026-10-28T23:31:12Z, runs/lad2wide_*, c_l bounds widened to 0.80, free c_l, 2000 iterations from the pre-continuation q0 = 2.5 state): c_l drifted to the new bound 0.80 while the weighted cost stayed at 0.46 (from 0.42) and rho_max ended at 6.6 (s_core 0.81): the free-c_l direction is nearly flat for this branch and moving c_l above 3/4 brought no improvement, so the preference for the upper end of the class seen at fixed c_l (36 at 0.73, 6.0 at 0.74, 4.2 at 0.749) is not evidence of a solution beyond 3/4. Reported separately from the in-class search.
Second continuation (2026-10-28T23:33:12Z, runs/lad3cont_*q3p5): after 6000 iterations in total at fixed c_l = 0.749 the q0 = 3.5 state has eta relative residual 0.0052 and q 0.081 (holdout), while the rho_max of the pre-registered specification, carried by the axial momentum with the full-space pressure in the core shells, is 2.55 (was 1.88 after 3000): the least-squares objective keeps lowering the reduced residuals but the primitive momentum residual does not follow, so the reduced equations are not being satisfied as a system in the core (the q equation is stuck near 8 percent).
q0 = 4.5 (2026-10-28T23:37:41Z, runs/lad3q4p5_*): from the continued q0 = 3.5 state, 2500 iterations with the pin moved to 4.5 give eta 0.0029 and q 0.057 (holdout), rho_M 1.16 but rho_max 4.30 carried by the q equation in the core shells: the q (circulation) equation, not the momentum, is now the limiting residual. Branch table: scripts/branch_table.py (its output table is in the run records, not published).
Refinement and c_l neighbour of the q0 = 3.5 branch (2026-10-28T23:42:38Z, runs/lad3ref_*, lad3c0745_*): D 48 / nmax 32 / K 32 from the 6000-iteration D 36 state gives rho_max 2.33 (was 2.55; eta 0.0040, q 0.083, s_core 0.68): a refinement factor of only 1.09, so under the reading of pre-registered specification 9.1 the floor is plateaued, not decreasing (the q equation stays at 8 percent at every level and the stall rule of the pre-registered specification applies if the third level, lad3ref64, does not halve it); c_l = 0.745 gives rho_max 2.39 versus 2.55 at 0.749: flat within 0.005 of the upper end.
Matching radius (2026-10-28T23:48:44Z, runs/lad3rm20_*): moving the shell/exterior interface from R = 10 to 20 (shell K 32, transfer of the q0 = 3.5 D 36 state, 2500 iterations) gives rho_max 8.4 (eta 0.011, q 0.080): worse than 2.55 at R_m = 10 after the same budget, so the matching radius is not the limiting factor of this branch; the q equation is.

## 15. Loader bug (fixed 2026-10-28T23:52:48Z) and the merged dipole column near c_l = 3/4
(a) Every script that rebuilt a Problem from a saved free-c_l state used the START value of c_l, so the exterior exponents were slightly
wrong in re-evaluations and exports (the in-job validation on the live Problem was correct). Fixed by Problem.from_state (c_l and
exponents from the final coefficient vector); candidates/T1_ladder/L0, L1, L2 re-exported with c_l = 0.749 in their metadata; the
retro-validations of free-c_l runs are being redone.
(b) The exterior exponent set merges exponents closer than 0.03. At c_l = 0.749 the forced second correction alpha + 2/c_l = 3.0053
and the irrotational dipole exponent 3 are merged into ONE column (at 0.745: 3.027, also merged; at 0.74: 3.054, separate). So at
the two c_l values where the ladder branch is best, the basis cannot distinguish the R^-3 dipole (which an exact profile must not have
in the open range, pre-registered specification 3.5) from the forced correction, and the d_0 = 0 test cannot be made there. This realizes the report author's
endpoint-resonance hypothesis in the representation itself: the branch's preference for c_l >= 0.745 may be the optimizer
using the merged column to absorb a dipole. Test queued: the best 0.749 state rerun with merge_tol = 0.002 (separate columns).
Structural signs after continuation (2026-10-28T23:54:39Z, branch table of scripts/branch_table.py): the equatorial counter-swirl of the first ladder state is gone in the continued and refined q0 = 3.5 states (min B(mu)/max|B| = -0.01 and +0.00, i.e. B is one-signed to the plotting accuracy) and the leading upper-axis eta tail is negative at R = 50, 200 and 1000, as the exact single-source conditions derived by the report author require; the source jet has p_z > 0 and the jet ratio 2.3 to 3.2 against the closure value 4.0. What remains wrong is quantitative: q equation at 8 percent, axial momentum O(1) in the core, and the merged dipole column at c_l >= 0.745 (section 15).

Third level and small-step c_l chain (2026-10-29T00:12:41Z, runs/lad3ref64_*, chain074_*): the q0 = 2.5 branch at D 64 / nmax 43 / K 43 (2500 iterations from
the D 48 state) has rho_max 3.37 (q equation; M 2.72) against 2.79 at D 48 and 4.24 at D 36: the floor does not decrease under the third
refinement, so by the reading of pre-registered specification 9.1 the branch is plateaued (stalled under the stall rule) at this q0. The small-step continuation
0.749 -> 0.745 -> 0.74 from the converged 0.745 state gives rho_max 10.7 at 0.74 (eta 0.0075, q 0.068), against 2.39 at 0.745: the steep
rise of the floor into the interval is confirmed by continuation and is not a cold-start failure. Together with the merged dipole column
at c_l >= 0.745 (section 15), the Stage I reading of this branch is: an endpoint phenomenon of the class boundary c_l = 3/4 whose residual
plateaus at O(1) in the q equation and the core momentum; the separated-column test (lad4sep) decides whether the 0.749 states depend on
the merged dipole column.

Separated dipole column (2026-10-29T00:15:55Z, runs/lad4sep_*): the D 48 q0 = 3.5 state continued 2500 iterations with merge_tol = 0.002 (the R^-3 dipole
column and the forced alpha + 2/c_l = 3.005 column kept separate) ends at rho_max 3.15 (eta 0.0047, q 0.073, s_core 0.64) against 2.33
with the merged column: the fit does not depend critically on the merged column, so the merged dipole explains at most a factor 1.4 of
the 0.749 advantage, not the branch itself. The R^-3 (l = 0) exterior coefficient of this state is reported above the table as the
d_0 diagnostic requested by the report author (printed in the run records at 2026-10-29T00:15:55Z).
d_0 diagnostic (2026-10-29T00:16:32Z): the l = 0, R^-3 exterior coefficient (5D monopole d_0 of phi, which must vanish for an exact profile with
1/2 < c_l < 3/4, pre-registered specification 3.5) is -20.8 for the D 48 merged-column state and -26.4 for the separated-column state (units in which the leading
coefficient max_n |A_n| is 1.3 to 1.35), i.e. the dipole term is about 4 percent of the leading tail at the matching radius R_m = 10
and the separated forced column (exponent 3.005) carries another -8.8: a nonzero dipole of the size of the state's other residuals,
consistent with the report author's endpoint-resonance reading at the few-percent level. The D 48 continuation lad4cont (3000 more
iterations) ends at rho_max 3.19 (eta 0.0046, q 0.072) against 2.33 before: the holdout residual no longer follows the falling cost.

## 16. Decisive diagnostic proposed by the report author: the frozen-phi q eigenproblem (2026-10-29T00:20:15Z, scripts/q_eigen_floor.py, runs/*/q_eigen_floor.json)
For the frozen (phi, c_l) of T1_ladder/L1 (D 36) and L2 (D 48), the linear homogeneous q equation with the pin q(0, z0) = 3.5 as a hard
row (null-space elimination) and the job's row weights has a least-squares floor of rel R_q = 1.1e-5 (L1) and 7.9e-7 (L2) on the holdout
grid (worst shell k = 3, the matching shell, 6e-4 and 2.6e-4), against 0.068 and 0.083 for the states' own q. The eigen-solved q differs
from the states' q by 83 and 80 percent in coefficient norm. Reading (following the report author's analysis): the 6 to 8 percent q residual of the ladder states is
a trade-off against the eta rows in the coupled least squares, not a representation defect of the q basis; the right Stage II solver is
variable projection (q slaved to phi by this linear solve, outer Levenberg-Marquardt on phi and c_l).
Variable projection, first test (2026-10-29T00:21:41Z, lm.VarProProblem, worker stage "varpro"): slaving q to the hard-pinned eigenfunction of the current
phi of L1 raises the weighted cost from 4.2e-3 (coupled state) to 1.03e6, because the eigenfunction differs from the state's q by 80 percent
and feeds a very different d_z(q^2) into the eta rows; 15 outer LM iterations with Kaufman's Jacobian (the variation of q* dropped) reduce
it only to 1.03e6 with the damping at 1.6e6, i.e. the Kaufman model is useless here: q* is extremely sensitive to phi (a transport
eigenfunction), so the full Golub-Pereyra reduced Jacobian (with dq*/dphi from the linear solve) or a damped alternating/homotopy scheme
is needed. No varpro jobs were queued; the stage exists for a later extension.
Note for the failure map (2026-10-29T00:24:25Z): the single-step transfer of the best 0.749 state to c_l = 0.70 (fmap0p70) starts at a weighted cost of 1.7e7 (the exterior exponents and the pinned structure change too much in one step); the fixed-c_l failure-map entries at 0.70 and below should be produced by the small-step chain (0.749 -> 0.745 -> 0.74 -> 0.735 -> 0.73 -> ... , chain* jobs) or from the generic/S1 seeds at those c_l (pilot2 results), not by this jump.
Chain step 0.74 -> 0.735 (2026-10-29T00:35:32Z, runs/chain0735_*): rho_max 15.3 (eta 0.011, q 0.056, s_core 0.59) after 10.7 at 0.74 and 2.39 at 0.745, each from the previous converged state: the floor of the q0 = 3.5 branch rises monotonically as c_l moves into the interval by small steps (2.4, 10.7, 15.3 at 0.745, 0.74, 0.735).
q0 scan upward (2026-10-29T00:37:34Z, runs/lad4q*): from the 6000-iteration q0 = 3.5 state at fixed c_l = 0.749, 3000 iterations with the pin moved give rho_max 2.32 (q0 = 4.0; eta 0.0056, q 0.061) and 2.04 (q0 = 5.0; momentum rho 0.91, eta 0.0041, q 0.049, s_core 0.78): the floor eases slowly with q0 and the momentum residual drops below 1 for the first time, while the q equation (5 to 6 percent) now carries rho_max.
q0 = 6.0 (2026-10-29T00:39:27Z, runs/lad4q6p0_*): rho_max 5.83 (q equation; momentum 1.40, eta 0.0045, q 0.040, s_core 0.81): the q0 scan at c_l = 0.749 has its minimum near q0 = 5 (2.04) and rises again at 6.0; the momentum residual keeps falling with q0 (0.91 at 5.0, 1.40 at 6.0 within noise) while the q equation stays at 4 to 6 percent at every q0.

## 17. Near-null space of the frozen-phi swirl operator, source jets, and the D64 level (2026-10-29T01:10Z, scripts/q_eigen_nullspace.py, runs/*/q_eigen_nullspace.json)
The report author asked whether the 80 percent distance between the eigen-solved swirl q* (section 16) and the states' q is a near-null
mode of the pinned swirl operator.  For T1_ladder/L1 (D36, 2400 PDE q rows x 994 q columns) and L2 (D48, 3724 x 1708), the pinned,
null-space-reduced, column-normalized operator has relative singular values (smallest ten) 7.3e-4 ... 6.9e-7 (L1; one below 1e-6,
condition 1.5e6) and 1.2e-5 ... 7.9e-8 (L2; four below 1e-6, condition 1.3e7).  The difference q* - q_state has essentially NO
component along the small singular directions: the ten smallest carry 0.1 percent (L1) and 0.0 percent (L2) of its norm; 99 percent of
it needs the 20 (L1) or 50 (L2) smallest directions, i.e. ordinary well-determined modes.  Truncated-SVD solutions with the 1, 2, 3, 5 or
10 smallest directions removed are identical to q* (holdout rel R_q 1.1e-5 and 7.9e-7, distance to the state's q 0.83 and 0.80 unchanged);
removing 20 directions at D36 raises the floor to 4e-2.  So q* is robust: the gap is a genuine difference between the coupled state's q
and the transport eigenfunction of its own phi, not a near-null artefact.
Source jets (Richardson finite differences at (0, z0), h = 2e-3 and 1e-3; AXISYMMETRIC_OBSTRUCTION_AUDIT.md 5e (vii) (d) closure q_z = 4 K h_2/delta with
h_2 = phi_zz(0, z0)/2, delta = 1 + c_l): the eigen-solved q satisfies the closure exactly (q_z = 0.0351 vs predicted 0.0351 for L1;
0.0430 vs 0.0430 for L2), while the states' q has q_z = -0.0126 (L1) and -0.1126 (L2): the WRONG SIGN of the axial swirl gradient at the
source.  Radial curvature q_rr at the source: states -24.3 / -25.1, eigen -10.2 / -10.3 (the states' swirl columns are 2.4 times too
narrow for the transport by their own meridional field).  Terms of the curvature identity (for the report author): 4 delta q_rr = -170 / -176 (state),
-71 / -72 (eigen); (delta^2 + K^2) q_zz = 12.2 / 15.0 (state), 40.3 / 29.3 (eigen); 3 (delta^2 + 2K^2) q_z^2 / (2K) = 0.002 / 0.15 (state), 0.015 / 0.022 (eigen).
Residual restricted to R < 0.1 (fine polar grid) and to the source collar |y - (0, z0)| < 0.1: states rel R_q 1.3e-3 / 1.2e-3 (max 4.7e-3 /
4.1e-3) and 2.1e-3 / 2.2e-3; eigen 1.5e-6 / 1.4e-7 and 2.2e-6 / 2.2e-7.  The states' 7 to 8 percent q residual sits in the dyadic shells
k = -2 to 2 (R from 0.5 to 16: core and matching region), not at the source (per-shell table in runs/*/q_eigen_floor.json).
Consequence: the variable-projection route is legitimate (q* well defined); the right regularity rows are not needed for q*.  What the
diagnostic says about the coupled states is that their swirl is not transported by their own meridional field anywhere in the core.
Third level for the q0 = 3.5 branch (2026-10-29T00:55:55Z, runs/lad4ref64_*, D64/n43/K43, 2500 iterations from the D48 state): rho_max 2.83
(axial momentum), m_max 5.04, s_core 0.66, rel R_q 0.075, rel R_eta 0.0044, weighted cost 3.41e-3.  Levels D36 / D48 / D64: 2.55 / 2.33 / 2.83
(2.55 after 6000 iterations at D36; 1.88 after 3000): no improvement with resolution.  Both q0 branches (2.5: 4.24 / 2.79 / 3.37; 3.5:
2.55 / 2.33 / 2.83) are unsuccessful finite searches whose per-run class under pre-registered specification 9.1 is F7 with the axial momentum dominant (the
formal plateau/stall labels are not applied to these level sequences, whose resolution ratio is 4/3 per level).

Variable projection with the full reduced Jacobian (2026-10-29T01:00Z, lm.VarProProblem rewritten; scratch script varpro_test2.py, not published; run records).
Inner rows: PDE q rows, q interface-continuity rows, q Tikhonov rows and the q-correction slave rows (all verified linear homogeneous in
q at fixed phi to round-off); hard pin by null-space elimination; dq*/dphi = -N (AN)^+ G with G the phi-derivative of the inner rows at
(phi, q*) (Golub-Pereyra form with the inner-residual term dropped; the inner floor is 2.7e-5).  Check: J_red v against central
differences of the reduced residual, relative error 2e-8 to 2e-7 in random directions; the dq*/dphi contribution is 4e-5 to 1e-4 of
|J v| in random directions, which is why Kaufman's approximation (section 16) is not what failed.  On L1 (GPU, before the revocation) the
outer cost fell 2.3e7 -> 4.5e6 -> 1.7e5 -> 5.3e4 -> 4.0e4 in four iterations and then every damped step was rejected up to lambda 5e6.
Diagnosis at the stalled point: the gradient and the Gauss-Newton model are right (FD check 1e-7), but along the gradient the cost is
0.5 t^2 x 4e20 (measured for t from 1e-9 to 1e-6): the reduced problem has a curvature of order 1e20 along the near-null directions of
the swirl operator (q* moves by 1/sigma_min ~ 1e6 to 1e7 times the phi change there), so the normal-equations Cholesky step breaks
down.  Remedies tested: (i) Tikhonov on the column-scaled inner coordinates with mu = 1e-5 ||M||_F destroys the inner solve (floor
0.33, outer cost 1e15: the pinned particular solution needs large components; not usable); (ii) the QR step of lm_solve without inner
regularization: CPU test running (run records).  If (ii) does not progress, the remaining option is a truncated-SVD
inner solve (drop sigma_rel < 1e-5: identical q*, see above) with the derivative taken through the truncated pseudo-inverse.

GPU revocation (2026-10-29T00:57:59Z; notice in the run records): all GPUs withdrawn; running jobs were killed by the guard at 00:58:14Z after writing
their checkpoints (worker SIGTERM path); the supervisor was restarted at 01:06:41Z with five CPU slots (supervisor/gpus.txt cpu0..cpu4,
CUDA_VISIBLE_DEVICES empty, --device cpu, one thread each) and resumed the six interrupted jobs from their checkpoints.  Measured CPU cost
per LM iteration (nice 19, loaded box): D24 0.31 s, D36 1.3 s, D48 4.4 s (one thread); 0.40 / 0.88 / 2.3 s with two threads.  Budgets were
cut accordingly: chain steps 1000 iterations (D36, about 22 min each), the two running reflection-class D48 jobs to 1600 iterations,
D48 level jobs to 1000 iterations; D64 is no longer affordable.  The failure-map chains were restarted with larger steps
(fmA: 0.73, 0.72, 0.70, 0.65, 0.60, 0.55 with levels at 0.70, 0.60, 0.55 and Rm 20 at 0.70; fmB from the q0 = 5.0 state: 0.74, 0.72, 0.70,
0.65, 0.60, 0.55 with levels at 0.70, 0.60).

CORRECTION (2026-10-29T01:30Z, scripts/q_eigen_values.py, runs/lad2cont_*/q_eigen_values_{pde,full}.json).  The "eigen-solved q*" of section 16
and of the first part of section 17 was the hard-pinned least-squares solution of the PDE q rows ONLY.  Those rows contain no interface
continuity, so each element solves the homogeneous transport equation on its own: the ball carries the pinned swirl, and in the shell and
the exterior the least-squares solution is q* = 0 exactly (max |q*| = 0.000 for R >= 2 in the value table).  That q* is discontinuous at
R = 2 and is not a global swirl; its floor 1.1e-5 (L1) / 7.9e-7 (L2), the 80 percent coefficient distance, the "1e6 cost jump" of the first
VarPro test and the near-null-mode discussion above refer to it and are superseded by the following numbers for L1 with the CONTINUOUS
slaved swirl (inner rows: PDE q rows, q interface-continuity rows, q Tikhonov rows, q-correction slave rows; hard pin; 2605 rows x 994):
  (floor) weighted PDE q-row cost 9.6e-7 against 3.1e-3 for the state's q; holdout rel R_q 3.8e-4 against 6.8e-2; per shell (state / q*):
  R < 0.06: 1.7e-3 / 1.8e-6; 0.125 to 2: 1e-2 to 1e-1 / 1e-5 to 1e-4; 2 to 8: 7e-2, 2e-2 / 9e-5, 1.5e-4; the matching shell 8 to 16: 6.9e-2 /
  5.1e-3; 16 to 64: 1.4e-3, 4.8e-4 / 1.9e-3, 4.5e-4.  The q basis represents the transport eigenfunction of the frozen phi to 4e-4
  globally, limited by the matching shell; the state's q is 170 times further from it.
  (a) values on the holdout grid: sup |q* - q| = 1.83 (at R = 1 to 4), L2 relative difference 0.475 on the inner grid, max |q*| 3.62 against
  max |q| 3.82; per shell the L2 difference grows from 0.016 (R < 0.06) to 0.87 to 0.89 at R = 1 to 4 and is 0.1 at R = 16 to 32 where
  |q| is 0.07: the two swirls agree only at the source; the state's swirl column is narrower (max |grad q| 3.9 to 4.1 against 1.7 to 2.1).
  (b) eta rows at (phi_L1, q*): weighted cost 0.363 against 1.1e-3 (factor 330), 0.285 in the ball and 0.078 in the shell, concentrated at
  R = 0.5 to 4 (shells -2, -1, 0: 0.107, 0.121, 0.069) with the largest rows at R = 0.65, mu = +-0.93 to 0.96 (near-axis core).  The total
  cost 2.3e7 at (phi, q*) is NOT physics: 4.5e7/2 of it is the single dilation-gauge row (q*'s tail integral differs from the gauge target)
  and 5.6e5/2 the phi-correction slave rows; PDE q rows 2e-6, interface rows 3e-7.
  (c) the pinned, column-normalized full inner operator has condition 1.7e10; the ten smallest singular directions (5.9e-11 to 2.6e-10
  relative) live in the ball (72 to 99 percent of their norm) with the rest in the shell and nothing in the exterior leading column.
  (d) leading far-swirl coefficient B(mu): state min -0.016, max 10.09, four sign changes near zero; q*: min 8.45, max 10.14, no sign
  change (one-signed, as an exact single-source profile requires).
Source jets (section 17 first part) were computed for the PDE-only q*; in the ball the two definitions coincide up to the influence of the
interface rows, and the qualitative statements there (closure sign, narrower column) are unchanged in sign but the numbers should be
re-read from q_eigen_values_full.json.  The reading of section 16 ("trade-off against the eta rows, not a representation defect") stands
with the corrected floor 3.8e-4; the reading that "q* is robust under truncation" was about the wrong operator and is withdrawn.
The homotopy test proposed by the report author (scripts/homotopy_q_test.py: q_t = (1 - t) q_state + t q*, coupled cost and holdout residuals
along t, then phi-only refits at t = 0.5 and 1 with 1000 LM iterations and validation per the pre-registered specification) is running on CPU with this q*
(log in the run records, result runs/lad2cont_*/homotopy_q_test.json).

## 17b. Corrected frozen-phi swirl comparison for L1 and L2 and the homotopy test; 2026-10-29T01:48Z
Continuous q* (inner rows: PDE q rows + q interface-continuity rows + q Tikhonov rows + q-correction slave rows at the job weights; hard pin;
the q-interface cost of q* is 2.96e-7 (L1) and of the same order for L2, against 1.02e6 for the disconnected solve of section 16).
Scripts: q_eigen_values.py --inner full (runs/*/q_eigen_values_full.json), homotopy_q_test.py (runs/lad2cont_*/homotopy_q_test.json).
| quantity | L1 (D36, c_l 0.749) | L2 (D48, c_l 0.749) |
|---|---|---|
| PDE q-row weighted cost, state / q* | 3.1e-3 / 9.6e-7 | 4.4e-3 / 1.1e-7 |
| holdout rel R_q (inner), state / q* | 6.8e-2 / 3.8e-4 | 8.3e-2 / 1.4e-4 |
| worst shell of q* (rel R_q) | matching shell 8 to 16: 5.1e-3 | matching shell 8 to 16: 2.5e-3 |
| sup |q* - q| on the inner holdout grid (values) | 1.83 (at R = 1 to 4) | 1.65 |
| L2 relative difference of values, inner grid | 0.475 | 0.439 |
| max |grad q| state / q* in the core shells | 3.9 to 4.1 / 1.7 to 2.1 | similar |
| eta-row weighted cost, state / (phi, q*) | 1.1e-3 / 0.363 (ball 0.285, shell 0.078) | 3.5e-4 / 2.18 (ball 1.98, shell 0.20) |
| B(mu) leading swirl tail, state / q* | min -0.016 max 10.1, 4 sign changes / 8.4 to 10.1, one-signed | 0.013 to 8.33, one-signed / 5.6 to 8.3, one-signed |
| source jet q_z: closure 4 K h_2/delta / state / q* | +0.0351 / -0.0126 / +0.0352 | +0.0430 / -0.1126 / +0.0430 |
| source jet q_rr: state / q* | -24.3 / -10.2 | -25.1 / -10.3 |
| source-adaptive sup |q* - q| at 0.1, 0.01, 0.001 a_eff | 0.35, 0.005, 1e-4 | 0.33, 0.006, 4e-4 |
| max |grad q| at 0.1 and 0.01 a_eff, state / q* | 3.6, 0.65 / 1.9, 0.27 | 3.7, 0.64 / 1.9, 0.26 |
Reading: the q basis represents the transport eigenfunction of the frozen phi to 1e-4 (L2) to 4e-4 (L1), limited by the matching shell;
the states' swirl differs from it by 44 to 48 percent in values (sup 1.6 to 1.8 at R = 1 to 4) with the wrong sign of q_z at the source
(closure defect confirmed by the independent verifier) and a column 2.4 times narrower in q_rr; no gradient growth toward the source,
so no source-local near-null mode is involved.  These numbers replace the section 17 statements made with the disconnected solve.
Homotopy test (L1, phi frozen, q_t = (1 - t) q_state + t q*; the dilation-gauge row held at its (phi, q_t) value during the refits because
q*'s swirl tail alone exceeds the original target; it is a normalization only):
| t | eta rows (weighted) | q rows | rel R_q | rel R_eta | worst eta shell |
|---|---|---|---|---|---|
| 0 (state) | 2.2e-3 | 6.2e-3 | 0.068 | 0.022 | shell 1 (R 4 to 8): 0.039 |
| 0.5 | 0.130 | 1.6e-3 | 0.031 | 0.200 | origin ball R < 0.06: 0.37 |
| 1 (q*) | 0.725 | 1.9e-6 | 3.8e-4 | 0.416 | shell -2 (R 0.5 to 1): 0.56 |
phi-only refits (q frozen, S1 rows and slaved exterior kept, 1000 LM iterations, CPU):
| refit | iterations to convergence | eta rows | q rows | rel R_q | rel R_eta | pre-registered rho_max (eq) | s_core |
|---|---|---|---|---|---|---|---|
| t = 0.5 | ftol at 103 | 1.68e-2 | 9.5e-3 | 0.086 | 0.042 | 6.73 (Mz; eta 2.50, q 0.98) | |
| t = 1 | flat from iteration 100 (cost 9.4153e-2 for 900 more) | 0.148 | 4.1e-2 | 0.121 | 0.101 | 17.1 (Mz; eta 2.95, q 2.23, Mr 1.76) | 0.79 |
Reading (the closure question of FINAL_REPORT 4.5 in the primary basis): with the swirl held at the transport eigenfunction of the L1 field,
re-optimizing phi (and the source position) cannot bring the eta rows below 0.15 weighted (relative 0.10), 67 times the coupled state's
value, and the refitted phi no longer transports q* (q rows 4e-2).  The tested phi-only refits did not close the eta equation (two finite
refits, not a neighbourhood statement); the coupled states buy their small eta residual with a swirl that is not transported.  This is the quantitative
failure mechanism asked for by the report author; it agrees with the external referee's independent characteristic reconstruction (the
transported vorticity induces strain of the wrong sign at the source).
VarPro gate (set by the report author): not passed and the line is closed.  The disconnected inner solve has been replaced; the truncated-SVD
derivative omits the inner-residual and rotating-subspace terms (noted by the independent verifier) and no variant descended below cost 4.0e4 from L1
(sections 17 and above); with the homotopy outcome there is no reason to expect a (phi, q*(phi)) minimum near the ladder states.

## 18. Sensitivity and robustness of the best interior state (0.74 direct positive-strain seed; 2026-10-29T06:35Z to 07:00Z, scripts/make_stage2_sensitivity.py, make_relative_perturbations.py)
Parent: runs/t1seedC_cl0p74_q2p5 (c_l 0.74 fixed, q0 pin 2.5, D36/n24/K24, outer interface R = 10, 3000 LM iterations; holdout rho_max 2.86, q
equation; exported as candidates/T1_seed_cl0p74/L1). Every variant is a re-optimization from this state (1000 to 1500 LM iterations, GPU)
with one setting changed; the values are the holdout rho_max of pre-registered specification 6.1 (dominant equation) with s_core / s_far. Cost convention (independent verifier, 2026-10-29T08:14Z):
'optimizer cost' is the LM objective (half the weighted squared-residual sum, as logged); 'cost_breakdown.total' in result.json is the unhalved sum,
twice the objective. In this section and section 19 the numbers 1.46e-2 (parent), 1.40e-2 (L-BFGS), 1.24e-2 / 1.17e-2 / 1.21e-2 (RPert) and
1.12e-2 (6000 iterations) are optimizer costs; 0.58 / 0.31 / 0.25 / 0.062 for the critical jobs and 1.2 / 0.36 / 1.7 / 0.20 / 10.7 / 3.0e9 for the
unrelated starts are cost_breakdown.total values (optimizer costs are half of these).
| variant | change | rho_max (eq) | reduced-eq value | s_core / s_far | a_eff | reading |
|---|---|---|---|---|---|---|
| parent | none | 2.86 (q) | 2.86 | 0.66 / 0.61 | 2.50 | |
| t1seedCL2 (D48) | D48/n32/K32 from this state | 2.81 (q) | 2.81 | 0.66 / 0.60 | 2.50 | three levels 2.86 / 2.81 / 2.95: flat |
| t1seedL3 (D64) | D64/n43/K43 from this state | 2.95 (q) | 2.95 | 0.67 / 0.61 | 2.50 | no decrease with resolution |
| t1seedL2 (D48, from the 1500-iteration parent) | D48 from the L0 state (3.55) | 2.85 (q) | 2.85 | 0.66 / 0.60 | 2.50 | same floor from the earlier parent |
| t1seedQuad | 1.5x quadrature nodes (nR_ball 40, nR_shell 52, nmu 45) | 2.83 (M_z) | 2.70 | 0.67 / 0.61 | 2.42 | unchanged under this one quadrature refinement |
| t1seedWint | interface weight 100 -> 1000 | 2.79 (M_z) | 2.57 | 0.67 / 0.61 | 2.42 | unchanged; interface cost 6.8e-9 |
| t1seedShift | scale_power_shift -2 -> 0 (radial-shell weights) | 7.55 (M_z) | 0.70 | 0.69 / 0.60 | 1.71 | order-one dependence on the shell weights: momentum up 2.6x while the reduced value falls 4x |
| t1seedShiftL2 | D48 level of the scale_power_shift 0 variant | 14.5 (M_z) | 0.71 | 0.68 / 0.56 | 1.49 | reduced residual unchanged at 0.7, primitive momentum doubles with resolution, core shrinks: the small-reduced / large-primitive case the problem statement warns about |
| t1seedRm5 | outer interface R = 5 | 8.23 (M_z) | 1.95 | 0.74 / 0.84 | 2.27 | order-one dependence on the matching radius |
| t1seedRm20 | outer interface R = 20 (K 32) | 8.54 (M_z) | 8.50 | 0.66 / 0.51 | 2.49 | same, in the other direction |
| t1seedPert1 | Gaussian noise 1e-2 of the GLOBAL RMS coefficient | 6.2e3 (M_z) | 1.5e3 | 0.02 / 0.05 | 5.7 | wrongly scaled test: the exterior coefficients are far below the global RMS; the tail was destroyed (initial cost 2e15), LM did not recover in 1500 iterations |
| t1seedPert2, Pert3 | 5e-2 and 2e-1 of the global RMS | final costs 1e11, 1e12 | | | | same design flaw; recorded as wrongly scaled tests |
| t1seedNoS1 | S1 rows and q0 pin removed (gauge row only), 1000 LM | 3.02 (q) | 3.02 | 0.67 / 0.63 | 2.50 | the swirl does not collapse within these 1000 iterations without the rows (status max_iter; no stationarity measured): the rows selected the basin; whether they are needed to hold it was not established |
| t1seedSep | separated exterior columns (no slaved correction, merge_tol 0.002), 1000 LM | 12.6 (q) | 12.6 | 0.69 / 0.45 | 2.50 | the second outer-domain treatment raises the value fourfold at 0.74 |
| freeclmid | free c_l, bounds [0.70, 0.745], 1500 LM (ftol at 55) | 2.60 (M_z) at c_l 0.745 | 2.50 | 0.67 / 0.62 | 2.42 | c_l goes to the new upper bound (0.745); with bounds 0.749 and 0.80 it went to those: in the three tested runs c_l moved to the imposed upper bound (not a statement about every bound) |
| t1seedRPert1 / 2 / 3 | per-coefficient relative noise 1e-2 / 3e-2 / 1e-1, then 1500 LM | 2.85 / 2.75 / 3.12 (M_z) | 2.55 / 2.53 / 2.53 | 0.67 / 0.61 | 2.42 | the three tested restarts returned to 2.75 to 3.12 (final costs 1.24e-2, 1.17e-2, 1.21e-2, below the parent's 1.46e-2); a statement about these three perturbations only |
| t1seedLB | L-BFGS (strong Wolfe) then LM 500 | 2.65 (M_z) | 2.59 | 0.67 / 0.61 | 2.42 | no accepted L-BFGS step in the tested run (twelve outer calls at the printed cost 1.400394e-2, status stalled; no gradient-norm or stationarity test reported); 500 LM steps reduced the cost to 1.313515e-2 and left the held-out defect at 2.65 |
| q0 scan at 0.74 (direct seeds, 1500 its) | q0 1.8 / 2.0 / 2.5 / 3.0 / 3.5 | 5.57 (M_r) / 4.70 (M_r) / 3.55 (M_z) / 2.87 (M_z) / 4.60 (M_z) | 5.32 / 4.48 / 2.87 / 1.66 / 1.54 | 0.38 / 0.42 / 0.50 / 0.56 / 0.59 core | 3.08 / 2.98 / 2.88 / 2.78 / 2.78 | a shallow bowl of order-one values in the pin; no pin gives a qualitatively better state (the q0 2.5 state reached 2.86 after 3000 iterations) |
Small-step chains from this state (fmE, 0.005 steps, 1000 iterations each): 13.7, 25.5, 35.8, 35.9, 23.9, 31.3 at 0.735, 0.73, 0.725, 0.72, 0.71,
0.70 (and from the 0.68 state upward, fmF: 7.5, 16.5, 33.4, 110, 163 at 0.685, 0.69, 0.695, 0.70, 0.71): the tested 1000-iteration steps did not
carry the low values to the neighbouring c_l (failed steps; they do not show that no continuation exists; direct seeds within 0.005 of 0.74
give 3 to 11, section 19 (e)). Free c_l from the state with the bound widened to 0.80 (freeclwide_t1seedC_cl0p74): c_l goes to
0.80 (rho_max 3.09) as the 0.749 ladder did, and the run's own optimizer cost fell from 0.0140 to 0.0121 (independent verifier, 08:20Z; the parent's saved
0.0146 is not the same objective because the row scales are reset). In the three tested free-c_l optimizer runs from this state (bounds 0.749,
0.80, 0.745) the final c_l reached the imposed upper bound; this does not locate or exclude an admissible exponent.
Jacobian conditioning (scripts/jacobian_svals.py, 09:20Z): column-scaled gauged Jacobian condition numbers 3.2e9 (0.74, D36), 4.0e9 (0.68, D36),
1.9e11 (0.74, D64), five smallest singular values over the largest 3e-10 (D36) and 5e-12 (D64); the ladder state L1 has 5.7e9 (section 17): the
direct-seed states are as ill-conditioned as the ladder state (singular values only; no singular-vector comparison was made, so nothing is
said about shared directions), consistent with the LM crawl and the noisy floors.
Reading: the value 2.8 to 3.0 at c_l 0.74
persisted under the particular checks made (three ball degrees, one quadrature refinement by a factor 1.5, one tenfold interface weight,
one optimizer change, three perturbation amplitudes); while in the
tested reoptimizations with the outer interface at R = 5 or R = 20, with separated exterior columns or with the shifted radial-shell weighting
the holdout value changed by a factor 2.6 to 5 (7.5 to 14.5), and every value stays far above the thresholds (B1 fails by at least 2.6e3).
Together with the interface derivative jumps above 1e-3 (F5 secondary) and the swirl-transport closure defect of section 17b, the tested
direct-seed states behave as weighted least-squares compromises of the discretized problem whose held-out value moves with the weights and
the interface position.

## 19. Late Stage II tests (2026-10-29T07:45Z to 09:00Z, scripts/make_critical_levels.py, scripts/make_stage2_late.py)
(a) c_l = 1/2 experiment, second level and continuation (the separate critical experiment had 46 runs at D24/n12/K16; FINAL_REPORT 4.6 row
"c_l = 1/2"). For the two best swirl-retaining D24 states (crit1_cl0p500_s1_sym_v2_q2p0_z0p0_sh-2p0_lm, holdout rho_max 12.5, s_core 0.13,
s_far 0.053, exported as candidates/critical/L0; and ..._sh0p0_lm, 16.9, 0.16 / 0.052):
| job | change | rho_max (eq) | s_core / s_far | cost_breakdown.total (unhalved sum) | reading |
|---|---|---|---|---|---|
| critref ..sh-2p0 | D32/n16/K22 refinement, 1500 LM | 7.49 (M_z) | 0.090 / 0.057 | 0.58 (optimizer cost 0.289) | value down, swirl fading toward the filter; exported as candidates/critical/L1 |
| critcont ..sh-2p0 | 2000 more LM at D24 | 12.05 (M_z) | 0.060 / 0.032 | 0.31 | swirl below the filter (s_far < 0.05) |
| critref ..sh0p0 | D32/n16/K22 refinement, 1500 LM | 41.8 (M_z) | 0.064 / 0.021 | 0.25 (optimizer cost 0.125) | swirl collapsed; exported as candidates/critical/L1b |
| critcont ..sh0p0 | 2000 more LM at D24 | 48.2 (eta) | 0.016 / 0.005 | 0.062 | swirl collapsed (F1) |
Reading: of the four critical follow-up runs three fall below the swirl magnitude filter (both continuations and the D32 level of the second
state); the fourth, the D32 level of the first state (critical/L1), passes it marginally with the core fraction reduced from 0.13 to 0.090 and the
far fraction 0.057 (parent 0.053); passing the magnitude filter is not B2 refinement stability. The costs (0.06 to 0.6) are 4 to 40 times those
of the 0.74 states. This is the Stage I swirl-collapse mechanism (section 1) at the critical exponent, consistent with the report author's audit (AXISYMMETRIC_OBSTRUCTION_AUDIT.md; the
countable-circulation-image argument at c_l = 1/2).
(b) Unrelated initializations at fixed c_l 0.74 with the direct-seed rows (S1 rows, q0 pin 2.5, slaved exterior, D36/n24/K24, 1500 LM
iterations; the referee seed reaches cost 1.5e-2 and holdout 3.55 in the same budget):
| family | cost_breakdown.total after 1500 (unhalved) | rho_max (eq) | a_eff | s_core / s_far | reading |
|---|---|---|---|---|---|
| gauss_core | 1.2 | 22.4 (M_z) | 7.6 | 0.52 / 0.96 | core moved outward |
| ring_core | 0.36 | 18.9 (q) | 2.7 | 0.59 / 0.97 | |
| asym_dipole | 1.7 | 11.0 (M_z) | 5.4 | 0.48 / 0.98 | core moved outward |
| swirl_dominant | 0.20 | 16.5 (q) | 3.5 | 0.59 / 0.94 | |
| poloidal_dominant | 10.7 | 109 (eta) | 2.0 | 0.73 / 0.64 | far from any floor |
| random_spectral | 3.0e9 | 5.7e3 (M_z) | 3.5 | 0.45 / 0.86 | diverged |
Reading: none of the six unrelated starts comes within a factor 4 of the 2.8 floor at 0.74 with the same rows (11 to 5.7e3 after 1500 iterations);
every tested run that reached the floor started from the referee's positive-strain seed (a statement about these tested starts only).
(c) Fresh-level direct seeds at 0.74 (the referee seed optimized directly at D24/n12/K16 and D48/n32/K32, no transfer from D36, 1500 LM iterations):
D24 / D36 / D48 = 5.41 / 3.55 / 3.32 (M_z; s_core 0.52 / 0.50 / 0.49; unhalved sums 2.6e-2 / 2.9e-2 / 2.1e-2): the fresh levels decrease mildly and
flatten toward the 2.8 to 3.3 band that the transferred levels reach with more iterations (D36 2.86 at 3000, D48 2.81, D64 2.95); the chain from
0.749 gave 14.6 / 10.7 / 8.0 at the same degrees. No level sequence of this state approaches the threshold.
(e) Direct seeds near the tabulated c_l (the 0.74 seed at fixed c_l 0.7375 / 0.74 / 0.7425 / 0.745, q0 2.5, D36, 1500 LM iterations): rho_max
10.7 / 3.55 / 6.89 / 3.09 (M_z, M_z, M_z, M_r; reduced-equation values 2.28 / 2.87 / 3.40 / 2.96; s_core 0.50 to 0.51; a_eff 2.88). The direct-seed
route within 0.005 of 0.74 gives order-3 to order-10 values with no systematic dependence on c_l (the momentum holdout maxima fluctuate while the
reduced values stay at 2.3 to 3.4), against 14 to 36 for the transferred 0.005-step chain (section 18). Whether a direct seed lands at 3 or at 10
after 1500 iterations is not predicted by c_l; continuation of the 0.74 case to 3000 iterations gave 2.86.
(d) Sensitivity suite for the 0.68 state (parent t1seedC2_cl0p68, 3.38 at D36, R = 10; 1000 to 1500 LM iterations each): interface R = 5 6.39
(M_z; s_core 0.75, s_far 0.87), R = 20 17.0 (q; 0.67 / 0.65), 1.5x quadrature 6.78 (q; 0.69 / 0.69), shell-weight power shift s = 0 16.9 (M_z, reduced 1.46,
a_eff 2.34 -> 1.49; 0.68 / 0.53). The 0.68 state behaves like the 0.74 state (section 18): order-one dependence on the interface position and on
the shell weights; the quadrature change stays inside the 3.4 to 6.8 fluctuation band of the 0.68 continuations.
