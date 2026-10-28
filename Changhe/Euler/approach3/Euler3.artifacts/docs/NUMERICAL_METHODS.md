# NUMERICAL METHODS (numerics lane; see reports/CONVENTIONS.md for the exact formulas)

## Representation
Divergence-free U = curl(T y) + curl curl(S y); real orthonormal spherical harmonics (no Condon-Shortley phase)
evaluated as regular solid harmonics P_q(y) = r^l Y_q, exact Cartesian polynomials with exact derivative ladders
(regular at origin and axis; no 1/sin theta). Radial functions: single global map x = (s-R0)/(s+R0), s = sqrt(r^2+R0^2),
shifted Chebyshev in x, envelopes (s/R0)^-(alpha+l) (T) and (s/R0)^-(alpha+l-1) (S), twist phi + omega/(2 c_l) log(1+r^2/R0^2)
applied to the potentials (cos/sin pair rotation with all radial derivatives via truncated Taylor jets). Optional
SPEC 4.4 channels: twisted rate 2alpha+1 (T, S) and untwisted harmonic s^-(2l+1) (S, l >= 2), core damped by
(r^2/(r^2+R1^2))^2. Even m (two-fold equivariance) by default; all m optional. No l = 0 modes (null).

## Residuals and pressure
R_u = (1-c_l)U + (W.grad)U + omega J U + grad P, R_Omega = Omega + (W.grad)Omega + omega J Omega - (Omega.grad)U, in
Cartesian components on a product grid (Chebyshev-Gauss radial nodes, Gauss-Legendre x uniform angular grid with
ntheta = 2L+8, nphi = 4L+14). Full-space pressure from -Lap P = tr((DU)^2) by the spherical-harmonic Green formula in
the twisted frame with oscillation-resolving composite Gauss quadrature in log r (SPEC 5.2, 5.3); grad P from the exact
radial derivative; grad P(0) from l = 1 moments. Independent cross-check: ray integral grad P = (1/4pi) int n int f.
Radial dealiasing: the quadratic source needs Nr >= 3 Nk for 1e-13 pressure accuracy (Nr = 1.5 Nk: 4e-3); momentum
discovery jobs use Nr = 2.5 Nk, validation 3 Nk and a 1.5x refined grid.

## Optimization
Least squares of the shell-balanced, fixed-gauge-scaled residual (core ball and dyadic shells with equal total weight;
scaling (1+r^2/R0^2)^(alpha/2) for R_u, (1+r^2/R0^2)^(1/(2c_l)) for R_Omega) plus gauge rows (int |F|^2 = 1, phase pivot).
Levenberg-Marquardt with dense Jacobian by chunked forward-mode AD (vmap over jvp), Cholesky normal equations, float64.
Options: nonlinear-balance reweighting (per-shell 1/(RMS T4 + RMS T5)^2, frozen within an LM iteration; a search device
against the weak-field artifact), continuation constraint on the m != 0 tail energy fraction, L-BFGS comparison,
free (c_l, omega) with bounds [0.401, 0.499] (pressure kernels rebuilt after accepted steps; their parameter derivative
is not in the Jacobian, a recorded deviation from SPEC 4.5).

Solver versions (ledger field solver_version): v1 plain least squares; v2 un-normalized reweighting (collapsed, marked); v3 mean-normalized
reweighting, holdout diagnostics, critical points; v4 phase gauge by exact rotation projection after each accepted step, dilation row weight
100 plus exact final projection, merged far nodes; v5 (2026-10-24T21:05Z) Green panels split at evaluation radii, exact alpha+1/alpha+2
tail-moment constraints (reduced parametrization, lead's d17 equations), Sigma_Z row on a 4 Nk radial grid as a scalar row with a
reverse-mode gradient and a target ramp (continuation), rebuilt-pressure parameter columns and rebuilt trial costs for free parameters.
Memory: L=8 jobs need 32 to 43 GB and L=10 jobs 58 to 70 GB (Nr = 3 Nk, far nodes, chunk 256); they run one per GPU.

v5 addendum (2026-10-24T22:05Z, no version bump: the LM default path is unchanged): job option nl_denominator = "all5" replaces the
per-shell weight denominator RMS(T4) + RMS(T5) (raw terms) by the sum of the RMS of all five momentum terms multiplied by the row scaling
(1 + r^2/R0^2)^(alpha/2), giving a rho_u-like weighted objective that cannot be gamed by core amplitude inflation (FAILURE_ANALYSIS item 12);
the ledger records nl_denominator per start. "all5far" (lead 22:40Z request b) adds lambda/den_nl, lambda = 1e-2, to the row scaling
on shells with lower edge r >= 1 so that a far nonlinear imbalance costs something (smoke test weights 1e-4 to 7.6 against 0.07 to 1.8 for
all5: the core is de-emphasized again, by design of the request; judge arms by holdout numbers only). The L-BFGS branch now minimizes the complete residual (Sigma_Z row included) and refuses free
parameters (falls through to LM with a logged notice).

## Diagnostics (SPEC 7.2-7.5, src/validation/spec_diagnostics.py)
5-term split T1..T5, absolute dyadic shells with volume measure, rho_u, rho_nl, pi_u, pi_nl, peak, rho_Om, rho_Om_nl,
rho_div, A_u, A_Om, N_k, e_k, N_core, e_core, N_F, e_F, r_core (argmax r^3 <|Omega|^2>), enstrophy radii, r_tail (E_F <= 0.1
against the state's own leading tail), vorticity-maximum strain identity, lambda_max(S), gauge defect, Tier S check.
Also: holdout grid (core ball + dyadic shells with Gauss radii, exact volume weights, rotated denser angular grid, pressure evaluated
there from the training-node source), located maxima of |Omega|^2 (Newton, Hessian classified) with strain ratio and transport term,
zeros of W with the DW spectrum and eigenvector defect, SPEC 7.13 strength quantities, SPEC 7.12 (O1) orbit averages, X5-style
off-grid vorticity maxima (scaled), Z, I, Sigma_Z on a 4 Nk grid, origin tau_0. Ranking key: holdout rho_u_max.

## Tests performed (SPEC 7.9)
T01 whole-field assembly vs independent sympy construction (4e-16, incl. axis and near-origin points; even m) and
divergence-free to 1e-15; T02 curl R_u0 = R_Omega (1e-9 by 4th-order FD), div W = 3 c_l (1e-14); T03 Green solver on
manufactured m = 0 (5e-15), twisted (1e-13, omega/c_l up to 24) and product (1e-14 at Nr >= 3 Nk) sources; independent
ray-integral cross-check 1e-13; T04 dilation covariance of U, Omega, R_u (L-scaling), R_Omega (invariant) to 1e-15, and of the
SPEC diagnostics on rescaled holdout shells (invariants to 1e-11, covariant scalings exact; A_u, A_Om are F-gauge quantities); T05 rotation covariance 1e-15; T06 reflection omega -> -omega
exact; T07 L[r^-alpha F] = 0 for the seed (1e-16, sign flips break it) and random (sigma, tau) up to the O(R0^2/r^2)
envelope term; T08 origin: fields and residuals evaluated at y = 0 (finite, consistent) in validate_candidate.py;
T09/T10 refined-grid and holdout evaluation in validate_candidate.py; T11 kill -9 and resume: bitwise identical
coefficients to the uninterrupted run; T12 gauge rows reported per start. AD Jacobian vs central differences at four
step sizes (1e-7 -> 3e-11 -> roundoff) and 4th-order differences in c_l, omega (1e-12).

## Benchmarks (one A100 80GB, float64; status/benchmark.json, logs/profile_chunks.log)
Residual 40-100 ms (kernel-launch bound). Jacobian: L=6/Nk=16 (768 unknowns) 0.6 s at chunk 512 (fixed parameters),
L=10/Nk=24 (2882 unknowns) about 5 s, L=14/Nk=36 (8066 unknowns, free parameters, chunk 128) 100 s and 44 GB.
LM start at L=6: 1 to 4 minutes; two worker slots per GPU.

Mixed-channel pressure (SPEC 4.4 channels on): the untwisted E channel breaks the exact twisted-frame structure of the
source; measured against the ray integral at core points the Green solution is still accurate to 1e-11 (B), 1e-10 (D) and
1e-8 (E channel with O(0.3) coefficients) because those channels are core damped and decay fast; without channels 1e-14.

## Known limitations
Exterior corrections with non-integer rates are only approximated algebraically unless the B/D/E channels are on;
no analytic tail model beyond the last node yet (SPEC 4.4 "beyond R_far"); E_G, E_H, E_D, Taylor ratios tau_1, tau_2,
energy/helicity identities and the candidate exchange format (SPEC 10) are not implemented yet (no candidate exists);
pressure kernels are frozen within LM iterations for free parameters.

## Addendum 2026-10-24T23:40Z (shift 2)
- Two shell families and single spheres (SPEC v1.11 7.3a): HoldoutGrid(edges=half_offset_edges(R0, r_max)) builds the family
  [2^(j+1/2), 2^(j+3/2)); sphere_diagnostics evaluates rho_u, rho_nl on the exchange radii R0 2^(j/4) with a rotated Gauss grid (pressure
  from the training-node source). Every start logs TWO-FAMILY; ledger fields rho_u_max_holdout_half/_both, sphere_rho_u_max, ...
- rho_lin, rho_sp (SPEC v1.14): rho_lin = RMS(R_u)/(RMS T1 + RMS T2 + RMS T3), rho_sp = max(rho_lin, rho_nl), per shell, global max over
  all shells and over shells with r_hi <= 1.
- Channel angular degrees (SPEC 4.4 angular closure): Model(channels=dict(..., LB, LD, LE, Mch)); union mode list, per-channel columns
  chan_cols, scatter in unpack_all / gather in pack; all grids and Lf sized by L_ext = max(L, LB, LD, LE); tail constraints, holdout grids,
  the far model and the diagnostics follow. Default (LB = LD = LE = L) is bitwise the old behaviour (tests/test_channel_degrees.py).
  Cost at L 6 with LB 15, LD 14, NkB = NkD = NkE = 4: n_red 1467 unknowns, 430k residual rows, Jacobian 11-18 s (A100), 23 GB; at L 8
  with LB 19, LD 18: 2719 unknowns, 782k rows, 45 s (chunk 128), 33 GB. Exclusive GPU jobs.
- G[F] closure (src/far_field/correction.py): G[F] = R0^(2alpha+1)[(U_0.grad)U_0 + grad P_0](R0 n) with the closed-form homogeneous tail
  U_0 (autograd derivatives) and the particular pressure P_0 = r^-2alpha Q solved mode by mode in the twisted frame (eigenvalues
  (-2alpha + i m kappa)(1 - 2alpha + i m kappa) - l(l+1), kappa = omega/c_l). Carried span: asymptotic velocity patterns of the B and D
  columns at r = R0; dist by weighted least squares on the sphere. Cross-check: ||G[F]|| = 0.609959 for d6t_L6 against the verifier's
  independent 0.6099595; the SPEC-degree span contains G[F] to 7e-14 (degree-L span: 14 per cent missing).
- Weighting "split" (pilot): per-shell weight 1/min(RMS T1 + RMS T2 + RMS T3, RMS T4 + RMS T5)^2 with the scaled terms.
- Transfer fit: column-scaled truncated-SVD least squares (rcond 1e-12), rank and spectrum reported (item 14 of FAILURE_ANALYSIS).
- Odd-m test: worker options perturb_m, perturb_m_rel add a random perturbation on the modes with m = perturb_m (A, C channels) of relative
  coefficient norm perturb_m_rel after the exact embedding into the all-m basis.

## Shift 4 additions (2026-10-25)
- First far-field coefficients (SPEC v1.24 7.8, src/far_field/correction.py): on the exact homogeneous tail at r = R0 the leading vorticity coefficient H (autograd
  gradient of the potentials) and the pressure coefficient Q give K_H(required) = (1 - 3 alpha) Psi_F; the carried value uses the sphere form 2 int G_c.H - (1 - 3 alpha)
  int n.(F x G_c) (divergence theorem on a shell for the degree-(3 alpha + 1) field V_1 x U_0) and, as a check, the direct curl of the carried B/D field; the vector
  defect G_carried - G_required is split into its component along F and its orthogonal part. The second exterior helicity term K_H R^(1 - 3 alpha)/(3 alpha - 1) is
  added to H_tot (4e-16 at R_end = 2^20 R0). Agreement with the independent route: ten export rows to 4e-12.
- S12 rows (src/optimization/problem.py radial_lambda_rows): sqrt(w) sqrt(w_k) sc_k <U.R_u>_k / <|U|^2>_k^(1/2) per radial training node, with the momentum rows'
  fixed-gauge scaling and nonlinear weight, so that their squares sum to w times the radial-lambda part of the weighted squared momentum residual (test K1 exact,
  Jacobian 4e-10). radial_lambda_diagnostics reports the share, the pointwise along-U share, lambda max, the shell-balanced negative radial-average fraction and
  lambda by octave.
- Robustness: the worker beats its heartbeat during the end-of-start battery; PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True is set before the torch import;
  the shortlist's branch key carries the lineage (D6 transfer, nest ladder, balance arm); reports/RESOLUTION_LADDER.md has a nest-ladder section with q per level.

## Shift 5 additions (2026-10-25T16:35Z)
- Memory of the dense LM: the stored Jacobian is released right after the normal equations J^T J, J^T r and the Marquardt diagonal are formed (src/optimization/lm.py).
  Until 16:17Z the previous Jacobian stayed bound through the trial evaluations into the next build, so every job held two Jacobians at its peak: at L8-ext
  (782k rows x 2719 unknowns, 17 GB each) this was the 75 GB observed with chunk 128 (now 50.4 GB); at L10 Nk24 with SPEC-degree channels B23/D22/E10
  (1.288 M rows x 4515 unknowns, 43.3 GiB) it OOMed at the second iteration after a first Jacobian of 160 s (chunk 64). The chunk bounds only the forward-mode
  intermediates (about 16 GB at L10 with chunk 64, about 19 GB at L8 with chunk 128), not the stored J.
- Split-column J^T J accumulation (jtj_split; lm_solve(jtj_blocks=k)): the unknowns are cut into k column blocks; block i (N/k columns of J, by the same chunked
  forward-mode vmap) is built and kept while the blocks j > i are rebuilt chunk by chunk, each chunk contributing J[:, chunk]^T J[:, block i] to the off-diagonal
  blocks of J^T J; J^T r is accumulated block by block; scalar rows (Sigma_Z, S9 balance rows) enter by reverse-mode gradients as in the dense path. The normal
  equations, the Marquardt damping, the Cholesky solve and the acceptance test are those of the dense LM (no additional squaring), so the iterates coincide to
  roundoff: unit test (L2 problem, CPU) J^T J and J^T r for 1/2/3/5 blocks with a non-aligned chunk equal to the dense values (difference 0; with scalar rows 2e-16),
  first LM step identical, recovery run identical; L8 validation from the cont150 (0.45, 1) state (2 LM iterations, chunk 128): two-step displacement difference
  4.6e-11 relative, per-iteration costs equal to 2e-15, cost decreases to 2e-9 (thresholds 1e-6 and 1 per cent); Jacobian time 40 s dense against 57 s split
  (1.44x against the nominal (k+1)/2 = 1.5), peak memory 50.4 GB against 27.3 GB. The finite-difference parameter columns of the free-parameter runs
  (SPEC 4.5) need the whole J and are not supported with k > 1.
- Worker additions: lm_only mode (LM without the battery, for solver validations; ledger lm_only_result), operator cancel marker queue/cancel/<job_id>, and the
  CODE VERSIONS record (sha256 of lm.py, worker.py, problem.py, fields.py per launch) so that the solver version of every start is recoverable from the ledger.

## Shift 7 additions (2026-10-26T06:34Z)
- Safeguarded lagged-target refresh (lead d128 CV item 4; default OFF). The closure rows impose G_carried(b) = G_required[F] with a lagged target that the worker
  recomputes from the current leading tail after every accepted Levenberg-Marquardt step, together with the nonlinear shell weights. Because the acceptance test of the
  LM sees only the frozen objective, a run can accept every step while the refreshed objective rises (the s11 (0.45, 0.3) weight-1 rung rose 500-fold between iterations 9
  and 29 before settling; FAILURE_ANALYSIS 45 and addendum). With cfg refresh_block = N > 0 (enqueue_continuation.py --refresh_block N [--refresh_backtrack]) the target
  and the weights are frozen inside blocks of N accepted iterations (the weights keep their Z0 values for the whole run), the target is refreshed at the block boundary,
  and the merit function (the cost of the refreshed objective; its closure-row part is logged) is compared with the previous boundary's; with refresh_backtrack the LM's
  own iterate (the reduced vector under tail constraints) is restored in place to the previous boundary when the merit rose and the damping restarts at max(lam, lam0) x 10
  (max(lam, lam0) after an accepted boundary). The LM callback contract was extended so that the callback may return a dict with a damping value (src/optimization/lm.py);
  a bool return keeps the old behaviour. Validation: a disposable L4 job run under the previous worker and under the new worker with the flag off is bitwise identical over
  six LM iterations (cost, damping, acceptance, iterate hash; runs/sgsmoke A/B); the flag-on runs C and D show the boundary bookkeeping and a forced backtrack (test-only
  environment hook E3_SG_TEST_FORCE_BACKTRACK) restoring the previous boundary exactly. The only production use is the registered control replay
  s11_L6_cl0.45_om+0.3_fixed_cl1_safeguard (50 iterations, one attempt, read with the lead's 5 per cent rule against 0.05227 / 0.05368).
- Reading conventions adopted after the astra referee pass of FAILURE_ANALYSIS items 43-45: the LM 'ftol' stop is a relative function-change criterion (one accepted step
  with relative decrease below ftol), described as 'a terminal cost plateau under the relative function-change criterion', never as stationarity (the frozen-objective
  gradient omits the derivative of the lagged target); the LM log line 'LM it k' reports the cost AFTER the step of iteration k; for arms that reweight the objective the
  unnormalized weighted training momentum RMS (ledger rms_mom) is reported beside the normalized holdout ratio; a sampled Q_sw below 1 that changes is a change, not a
  violation of the necessary condition Q_sw <= 1.
- New CPU helpers: scripts/kappa_ratio_check.py (kappa(R) remainder ratios against 4^(-(2 - alpha))), scripts/radial_lambda_of_state.py (d93 radial-lambda diagnostics of
  a saved state), scripts/radial_lambda_octaves.py (lambda by octave for a job and its start), scripts/arm_reading.py --json, scripts/failure_map_rows.py --mark_incomplete.
  Supervisor: per-job gpus_allowed (effective after a restart), dispatch loop scans every free GPU.
