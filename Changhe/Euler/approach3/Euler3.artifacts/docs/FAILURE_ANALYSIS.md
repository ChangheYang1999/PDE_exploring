# FAILURE ANALYSIS (numerics lane; updated as the campaign proceeds)

## 2026-10-24, Stage I, first 2 hours
1. Plain least squares of the vorticity residual (s1a, 210 starts, L=6, Nk=16, even m, 35 (c_l, omega) points incl.
   negative omega, five seed families): every start converges to one omega-independent axisymmetric state per c_l
   (weighted vorticity RMS 2.37e-2 at c_l=0.41 ... 2.5e-2 at 0.45; rotation content 1e-15; m != 0 tail energy 1e-31;
   max|U| = 0.03 in the F-gauge; r_core = 6; r_tail = 1870; SPEC rho_u ~ 1 in the core, rho_nl 1e2 to 1e5).
   Mechanism: the objective is minimized by a weak nearly linear field; the F-gauge constrains only the x = 1 limit of
   the tail amplitudes, so the core is emptied and the tail onset pushed outward (two artifacts of PROMPT section 5 at
   once). The omega-independence confirms the axisymmetric reduction (SPEC 2.6). Not a candidate; fails every Tier S item.
2. Nonlinear-balance reweighting with the momentum formulation (s1b, L=6): collapse removed (e_F 0.1 to 0.9, N_core
   order 1, r_core 1 to 4, max|U| 0.2 to 0.3) but all starts stall at rho_u_max 0.52 to 0.79 with the LM damping at its
   maximum: genuine local minima of the weighted least squares, residual comparable to the terms. No Tier S state.
3. Numerical defects found and fixed (both would have corrupted candidate ranking, not the discovery picture):
   pressure solver without twisted-frame treatment (grad P off by 1e-3 to 1e-1 for m != 0), grad P(0) moment bug (1.8%);
   radial aliasing of the quadratic pressure source at Nr = 1.5 Nk (4e-3).
Open: whether larger L, Nk, the SPEC 4.4 channels, odd m, free (c_l, omega), L-BFGS or continuation in the non-axisymmetric
content change the residual floor (jobs s1c-s1h queued).

## 2026-10-24 20:02Z, Stage I, hours 2 to 3
4. Strain-free local minima. Every local minimum of the reweighted least squares (momentum or vorticity formulation, all
   seed families, 300+ starts at L=6) has total stretching ratio Sigma_Z = (int Omega.S Omega / int |Omega|^2)/(1 - 3c_l/2)
   between -0.01 and 0.03 (exact profiles: 1), strain ratio Omega.S Omega/|Omega|^2 at the located global vorticity maximum
   0.004 to 0.14 (exact 1), lambda_max(S) inside the trapping radius 0.1 to 0.3 (exact >= 1), and orbit-averaged stretching
   <s>_T about 0 along backward orbits. The least squares balances the equations without vortex stretching; such states
   cannot approximate a profile (SPEC 2.1, 2.8(f), 7.8).
5. Second axisymmetric attractor: with reweighting, 5 of 150 momentum starts drift to an axisymmetric nonlinear state
   (rho_u_max 0.10 to 0.16, e_F 1e-9, lambda_max(S) 0.42 to 0.45, r_core 0.63), the non-rotating problem's best approximate
   state at this resolution; excluded by the nontriviality guards.
6. Un-normalized reweighting incident (18:53 to 19:09Z): weights growing without bound as the field shrinks made the gauge row
   negligible; 30 starts collapsed to U = 0; all marked as failures in the ledger; fixed (mean normalization, exact gauge
   projection, collapse marking).
7. Sigma_Z = 1 constraint and affine-core seeds (first pilots, 19:55Z): states acquire the right local stretching structure
   (strain ratio 0.84 to 1.38 at the located maximum, lambda_max(S) 2.8 to 5.4, a W zero with eigenvector defect 0.03) and the
   affine-core start gives the best ranked state (holdout rho_u_max 0.40, c_l 0.45, omega 1); their far fields are not in tail
   form within the sampled radii (E_F > 0.1 to r = 2000, far vorticity residual 5e-2 at r = 4096): the x = 1 limit F decouples
   from the resolved field. Remedy: far-field anchoring rows (in the queued sweeps s1k, s1l, s1m, s1n).
Open: resolution dependence (L=10 with channels queued), odd m (queued), free parameters (queued), R0 (queued).

## 2026-10-24 20:55Z, numerical defects found by independent review and fixed the same evening
8. Off-grid pressure gradient (astra review2; verifier 20:35Z: 3.4e-3 relative on the exchange spheres of the exported state): Green
   quadrature panels were not split at evaluation radii. Fixed (1e-14); all holdout rho_u values recorded before 20:50Z carry an error
   of this kind (re-evaluation records in the ledger).
9. Forbidden alpha+1 tail term (verifier: L2 coefficient 284 for the exported state with ||F|| = 1): the Chebyshev series in x produces
   rates alpha+1, alpha+2 absent from the true expansion; explains E_F > 0.1 to r = 2000 and rho_nl ~ 1e6 to 1e9 in far shells. Fixed by
   exact elimination (tail_constraints, lead's d17 moment equations); far deviation now decays like r^-3.
10. Stretching integral I under-resolved at Nr = 1.5 Nk (astra counterexample with a sign flip): Z, I now on a 4 Nk grid.
11. Reweighting without normalization collapsed to U = 0 (see 6); PDE-row-only Marquardt scaling left gauge directions undamped
    (stall at iteration 0 at L=10); a weighted phase row (1e4) drove rotation steps that broke the nonlinear rows: phase gauge now by
    exact rotation projection, standard scaling restored.

## 2026-10-24 22:01Z, continuation arms: the nonlinear-balance weighting is gamed by core inflation
12. c2x2_L8_cl0.45_om+1.0_fixed (warm start from the s1k state with holdout rho_u 0.405, L = 8, Nk = 20, Sigma_Z ramp, tail constraints)
    drove the weighted training cost from 4.7e-2 to 1.5e-6 (rms) in 300 iterations while the unweighted R_u RMS stayed at 1.05 and the
    holdout rho_u_max rose from 0.405 to 0.480. max|U| grew 1.14 -> 1.73, N_core 2.96 -> 3.73, e_F 0.66 -> 0.89, |Omega|max 4.0 -> 9.9.
    Mechanism: the per-shell weights 1/(RMS T4 + RMS T5)^2 (cap 1e3 x median, mean one) are computed from the raw nonlinear terms.
    Inflating the core makes its nonlinear terms large, its weights tiny, and the mean normalization then puts almost all weight on the far
    shells (where the state is nearly linear and easy to satisfy). The gauge ||F|| = 1 fixes only the tail amplitude, so the core is free
    to grow. This is the "artificially large balancing terms" failure the referee warned about (astra review 1, finding 6 and the closing
    remarks) and it means the training cost of these arms is not evidence of anything. Rankings were never affected (they use the holdout
    rho_u), but the resolution ladder's L = 8 fixed arm is a degradation, not a refinement.
    Fix (worker/problem option nl_denominator = "all5"): the shell denominator is the sum of the RMS of all five terms, each multiplied by the
    row scaling (1 + r^2/R0^2)^(alpha/2) that the residual rows carry, so the weighted shell cost is RMS_k(scaled R_u)/sum_i RMS_k(scaled T_i):
    a rho_u-like objective, neutral under amplitude inflation and without the extra far-shell emphasis (weights 0.07 to 1.8 on a smoke test
    instead of 1e-8 to 6). Arms c2x2c (L = 6 and 8, fixed, both states) are queued with it; the default "nl" is unchanged for the record.
    Alternative not taken: freezing the warm-start weights (consistent quadratic cost, but still the raw-term far-shell emphasis).
13. (22:40Z, lead) d6t_L6 (holdout rho_u_max 0.0552 from the fitted independent D6 state) is not ordered ahead of D6: full-shell
    rho_nl^max 3.12 (no B/D/E channels carried: NkB = NkD = NkE = 0 because enqueue_continuation.py only adds channels with --channels;
    the five-term weights cannot see the far imbalance), and the core gain is a shell-edge effect (half-offset shells 0.0766 against
    0.0769). Lessons: always carry the channels; report rho_nl^max over all shells, both shell families and the single-sphere maximum.
    Options added: nl_denominator all5far; arms d6v (L 6 fixed/free) and d6u (L 8, 10) carry channels 4,4,4 with all5far.

## 2026-10-24T23:40Z (shift 2), new items
14. Transfer-fit solver artifact (N1/R3 fits of the verifier's states): fit_field solved the normal equations with a relative Tikhonov term
    1e-10 lambda_max. The fit matrix has condition number 1e300 (the E channel's l = 1 columns are identically zero and the A/B, C/D channels
    are nearly redundant), so the regularization removed genuine directions: fit errors 1.1e-2 / 1.4e-2 / 2.5e-2 GROWING with Nk 12/16/24
    and N1 ratios 1.02 / 1.03 / 1.06 at L 6/8/10 were artifacts of the solver. Fixed (column-scaled truncated-SVD least squares, full rank):
    at L 6 the misfit is 8.6e-3 for every Nk (angular limitation of L 6 for a degree-6 Cartesian polynomial field), at L 8 it is 1.4e-7 and the
    fitted field's holdout rho_u is 0.07295 against the source 0.07287 (ratio 1.001). Lesson: report the rank and the singular value
    spectrum of every fit (scripts/fit_spectrum.py); never use relative Tikhonov on matrices with exactly zero columns.
15. c2x2c (s1k branch, all5 weighting) is a floor case: L 6 -> L 8 gives holdout rho_u 0.2496 -> 0.3537 at c_l 0.47 (worse) and 0.3858 ->
    0.3577 at c_l 0.45 (q 0.93), the same on both shell families; both arms ran 300 iterations to max_iter. Under the lead's rule (L 10 only
    if q <= 0.85) the L 10 arms were cancelled. rho_lin of the c_l 0.47 state is 0.69 in the core (near-steady Euler core, item 17).
16. Free-parameter drift to the boundary: d6u_L6 free (no channels, all5, from d6t_L6) moved c_l 0.45 -> 0.4990 and omega 0.3 -> 0.2702 in
    87 iterations (ftol), with the holdout rho_u rising 0.0552 -> 0.0611 and rho_nl falling 3.12 -> 0.86. At c_l -> 1/2 the state leaves the
    target range (alpha -> 1); this is an outcome to record (prompt II.1), not a candidate. Free arms are excluded from the ranked
    leaderboard until a fixed-parameter evaluation at their final parameters; the fixed scan c_l 0.46-0.49 (d6scan) tests monotonicity.
17. Near-steady Euler cores (lead d29, SPEC v1.14): the primary descendants share the mechanism found in the independent ladder. For
    d6t_L6 the core shells have rho_lin = RMS(R_u)/(RMS T1 + RMS T2 + RMS T3) = 0.55 (0.50 on the half-offset family) while rho_u = 0.055:
    the nonlinear terms T4 and T5 are large and cancel each other, the residual is of the order of the self-similar terms, and rho_u is
    small only through its denominator. d6t_L8: rho_lin 0.50 (r < 1); c2x2c 0.47: 0.69. rho_sp = max(rho_lin, rho_nl) is now reported in
    every summary line. Pilot remedy (lead 23:19Z): weighting "split" with shell weight 1/min(lin sum, nl sum)^2 (jobs d6split, c2x2split).
18. (2026-10-25T01:20Z) SPEC-degree channels are necessary but not sufficient for the far balance. d6w_L6 carries B up to l 15 and D up to l 14 (even
    m <= 12), so the carried span contains G[F] to 6.5e-14; yet after 300 all5far iterations (lambda 1e-2) the carried rate-(2alpha+1)
    coefficient has ||G_req - G_carried||/||G_req|| = 1.42 with correlation 0.16 (verifier independently: 1.42 / 0.16), and r^(2alpha+1)
    RMS(R_u) tends to the constant 0.257 far out (rho_nl -> 0.56 at r 2e4; d6t_L6 without channels: 0.18, rho_nl -> 0.40 as the lead's d27
    predicted). The far-imbalance weight lambda 1e-2 on shells r >= 1 is too weak against the core rows, and the cost was still falling at
    max_iter. The far-supported variant (R1 = 3.33 R0) is worse (mismatch 2.14, rho_nl 0.83). Remedies under test: 600 more iterations
    (d6w2), lambda 0.1 (d6w2 _lam1e-1), and closure residual rows G_carried(b) - G_required(F) with a lagged G_required (planned).
    Addendum 2026-10-25T02:53Z: the remedy works. d6w3_L6 (closure rows, closure_lambda 1e-3, 300 iterations from d6w_L6) brings the carried mismatch
    to 0.216 with correlation 0.977 and rho_nl^max over all shells to 0.211 std / 0.190 half, with holdout rho_u unchanged (0.0527 / 0.0695);
    600 more plain all5far iterations (d6w2) had made the mismatch WORSE (2.53, correlation 0.11; rho_nl 0.93). Lesson: a coefficient that the
    objective does not see must be imposed as a row (lagged target is enough); shell weights alone cannot steer an asymptotic amplitude.

## 2026-10-25T05:15Z (shift 3), new items
19. Backward-defect Newton (Stage II S2 prototype, lead 03:17Z item 1; reports/s2s3_newton_*.json): the Galerkin-projected bordered system for
    d(U) = U + G N(U) is ill-conditioned and gets worse with the level. Raw coefficient coordinates: cond 2.3e5 (L2, 50 unknowns), 1.3e8 (L4,
    242), 2.5e13 (L6, 674); column-scaled coordinates (basis columns of unit weighted norm): 1.3e3 / 1.3e5 / 1.5e7 against the basis's own
    conditioning 23 / 472 / 8.5e3; sigma_min(J_s) 5.0e-2 -> 1.7e-3 -> 1.1e-4 while sigma_max stays 66-1600. GMRES (restart 50) reaches 1e-3 only
    at L2 (28-30 iterations, i.e. a direct solve); at L4 and L6 it stalls at 0.1-0.2 after 2000 iterations with or without a Jacobi
    preconditioner. The damped Newton step lowers ||P_n d|| by 12 / 7 / 4 per cent and worsens the holdout rho_u^max at L4 and L6. The JVP is
    correct (central differences 1e-11 to 1e-9) and G[L U] = U holds to 1e-6, so this is the operator I + P_n G N'(U) plus the basis, not a bug.
    Reading (lead's caveat applied): compatible with the transverse derivative loss of FINAL_REPORT item 24(e) but not diagnostic of it. The
    column-scaled numbers do not split the growth between the basis geometry and the operator (verifier 05:29Z: unit-norm columns are not
    orthogonal; field-norm coordinates J_field = diag(R, I) J_s diag(R, I)^-1 are needed; computed from the retained matrices, see
    reports/s2s3_newton_*.json 'field_norm'). Lesson for Stage II: S2 needs a real preconditioner (LM normal
    matrix of the shell-weighted residual, or the linearized L) and a trust region; otherwise it is a failure-map probe only.
20. Stabilized fixed point (S3 prototype): U <- S[P_n m(U)^2 T(U)], T = -G N(U), eta = 2, from the best nest2 L2 state and the nest4 L4 state,
    with the plain normalized control: every variant leaves the basin at the first step (holdout rho_u^max 0.108 -> 0.80 / 0.66 at L2, 0.058 ->
    0.40 / 0.24 at L4), successive-change ratios 0.1-25, m(U) changes sign by the third iteration. <U, T(U)>_eta / <U, U>_eta is 0.63 (L2) and
    0.71 (L4) at the start (exact profile: 1); the projection defect of T onto the trial space is 17-36 per cent. The projected map is not
    contracting near any saved state. Not usable as a refinement arm from Stage I states.
21. The balanced-core nest states are near-axisymmetric swirl states (lead d55, FINAL_REPORT item 25): Q_sw = (1 - 2 c_l) max|Gamma_0|/max|S| is
    2.02 for nest4 (0.45, 1) and 2.63 for nest4 (0.42, 0.3) (core eddy energy fractions 0.058 and 0.062), against the exact-profile condition
    Q_sw <= 1; their mean swirl is carried by the residual, not generated by the eddy angular-momentum flux. Three nest2 L2 states at (0.45, 1)
    also fail (1.22-1.35). The D6 lineage passes (0.15-0.44) but its eddy-generated swirl is misaligned (lead d55). So the two best-balanced
    branches found by the route's own ladder fail a necessary structural condition that the ranking key rho_u^max does not see; tau_F (0.66
    for nest4) must not be read as proximity. Remedy under test: S7 probes (f_sw continuation on the D6 lineage; eddy seeding on both lineages).
22. Origin Taylor orders (SPEC 7.6, T08; tests/test_T08_origin_taylor.py): the floored ratios of the best states are tau_0 4.5e-4 (d6w_L8) to
    1.7e-3, tau_1 1.2e-2 to 3e-2, tau_2 3e-2 (D6 lineage) and 0.2-0.3 (nest4), against 1e-5 for Tier S: the origin balance fails at first and
    second order by three to four orders of magnitude even where tau_0 is small, consistent with the core (not the far field) being the limit.
23. (2026-10-25T07:21Z) Global-balance rows collapse the non-axisymmetric content (S9 lambda = 1 on the nest4 (0.45, 1) L4 state, 300 iterations): E_ren
    -2.10 -> -0.0009 and H_tot/int|h| -0.83 -> -0.0005 with holdout rho_u^max 0.0579 -> 0.0646, but the final state fails the SPEC 7.4
    non-axisymmetry guards (e_core 4.7e-9, e_F 4.5e-9, N_F 1.3e-4; approximately, not exactly, axisymmetric; max E_F 1.236 at r 3.4): the optimizer
    satisfies the two exact-profile balances by removing the eddies, which an exact profile cannot do (FINAL_REPORT item 7: axisymmetric profiles
    are trivial). Recorded under the lead's R10 (e) as 'global balance: attained by near-axisymmetric collapse' (no lambda = 10 reading). Remedy
    registered (S9b): the S9 rows plus guard rows pinning e_core and e_F at their start values.
24. (2026-10-25T07:21Z) Unpinned artificial-viscosity continuation (S8, omega free, c_l pinned, nest4 (0.45, 1) L4, nu 3.8e-3 and 3.8e-2): the LM lowers
    the core amplitude (max|U| 1.14 -> 0.034 and 0.03 of |Omega|) and moves omega (1.0 -> 0.21 and 0.53) until the viscous term is 91-99 per
    cent of the momentum terms (sigma^nu 24 and 580): failed viscous solves, an optimizer tendency of the unpinned AV problem (not a dynamical
    statement). Remedy under test (lead 06:56Z): omega fixed, core RMS pinned at its start value, nu ladder from small values (s8p runs).
25. (2026-10-25T07:21Z) Closure rows at L8 (d6w3_L8, from d6w_L8, 300 iterations, 3.5 h): the carried rate-(2 alpha + 1) coefficient is NOT fixed (mismatch
    1.33, correlation 0.59; at L6 the same rows gave 0.22 / 0.98) and the holdout rho_u^max rises 0.0442 -> 0.0568 (0.0543 -> 0.0587 half),
    rho_nl^max 1.455 -> 1.00, sigma_u^max 1.99. With L6 -> L8 at q 1.08 and the closure step at 1.29x, the D6 lineage is floored under the
    lead's R2; its best state stays d6w_L8 (time-limited, 180 iterations, no closure rows). Possible causes to test in Stage II: the closure
    target lag at the larger L8 Jacobian steps, the 128-chunk time limit (300 iterations only), and the L8 channel set (B19/D18) adding 140
    columns that the far rows do not control.
26. (2026-10-25T08:25Z) Global balances imposed with the non-axisymmetry guards (S9b on the nest4 (0.45, 1) L4 state; rows lambda E_ren, lambda H_tot/int|h|,
    100 (e_core/e_core,0 - 1), 100 (e_F/e_F,0 - 1)): lambda = 1 meets both balances at holdout rho_u^max 1.46x the start, lambda = 10 (from
    that state) meets them to 1e-4 at 1.23x (0.0713 / 0.0722 against 0.0579 / 0.0585) with sigma_u^max 0.68 (0.53) and the eddies kept
    (tail_nonaxi 0.04). The energy balance is met by an E_F overshoot (max E_F 1.31 at r 3.7, i.e. 12 R0 or about 8 core radii; weighted excess 1.15 against
    deficit 1.15), not by a core change, and the helicity balance by a sign change of h at r 0.5. R10: misses (a) narrowly (1.2x) and (b)
    (1.5x): the balances can be imposed on this branch at a 23 per cent cost in the shell key but do not point at a nearby profile. Compare
    the lead's S9c reading (scaling the carried channels alone moves E_ren -1.54 -> -0.46 at lambda_c 4 on nest6 (0.45, 1) p0 with max E_F 1.51):
    on these states the global energy balance is a far-field (channel) quantity at fixed core.

## 2026-10-25T11:09Z (shift 4), new items
27. First far-field coefficients (SPEC v1.24 7.8; reports/FAR_COEFFICIENTS.md; ten of sixteen rows independently confirmed to 4e-12): no export carries the
    first nonlinear far correction. Energy ratio K_E(carried)/K_E(required) between -2835 (d6t_L8) and +29.7 (nest6 (0.45, 1) p1), four of nine wrong-signed;
    helicity ratio K_H(carried)/K_H(required) +0.18 to +4.24 with the exact-profile sign; vector defect m = ||G_carried - G_required||/||G_required|| 0.22
    (d6w3_L6) to 4.4 (d6t_L8), of which 42-67 per cent (squared) lies along F and the rest is an angular-shape error of the same radial order (91 per cent
    for d6w_L6). States without B/D channels carry 0 (nest4, S9b, d6t_L6). Mechanism: 'far balance' at the first correction order on every branch; the
    closure rows (weight 1e-3, lagged target) reduce m to 0.06-0.22 at L6 with enough iterations (d6w3_L6, s1nk Nk24) but leave the energy ratio off by
    factors 0.16-3.3 because c = |<F, G_required>|/||G_required|| is only 0.007-0.044 (the energy projection is a near cancellation, d84), and they are
    ineffective at L8 (item 25). Remedy registered for Stage II (lead S11, R12): closure weight ladder 1e-3 -> 1e-1 -> 1 with the full vector rows and the
    F-component and orthogonal norm recorded separately.
28. Radial resolution at fixed angular degree (s1nk Nk24 on d6w3_L6, 1.6 GPU-h): Nk 16 -> 24 (Nr 48 -> 72) lowers the radial Chebyshev tails from 1e-2 to
    3e-4 (A) and 9e-4 (C) and leaves the holdout rho_u^max (0.0527 -> 0.0528 std, 0.0695 -> 0.0724 half), sigma_u^max (1.90 -> 1.80) and a_max (1.90 -> 1.81)
    unchanged within 5 per cent, with the core resolved. Reading: no improvement from the radial refinement under the tested optimizer and budget (300
    iterations); the categorical statement that the core floor is not a radial-truncation artefact stays open until the Nk 32 run and an optimizer control
    (verifier 11:30Z item 4). Together with item 25 (L6 -> L8 at q 1.08) the D6 lineage shows no decrease in either resolution direction so far.
29. The nest ladder at c_l 0.42 (nest6 (0.42, 0.3) p0, 1.9 GPU-h): the L6 rung with SPEC channels and closure rows lowers the holdout from 0.0740 to 0.0641
    and Q_sw from 2.63 to 0.72 (as at (0.45, 1): 2.02 -> 0.67), i.e. the necessary source-size condition is met once the rate-(2 alpha + 1) channels and the
    closure rows are present, at every c_l tried. It fails the global balances (E_ren -3.90, H_tot/int|h| -0.79) and the far closure (K_E +5.4, m 0.35) like
    every other state. Not a failure of a run; recorded because the balanced-core branch now spans c_l 0.42 and 0.45 and omega 0.3 and 1 with the same
    signature (balanced core, Q_sw <= 1, negative E_ren at order one, wrong first far correction), which the Stage II arms S9b/S10/S11 address.
30. (2026-10-25T11:22Z) Global-balance rows with guards on the D6 lineage (S9b lambda = 1 on d6w3_L6 at L6-ext): the LM stalls within 22 iterations (lambda climbs
    from 3e5 to above 1e10 with every step rejected; |g| 7.1 unchanged) after the first ten iterations moved E_ren -1.04 -> -0.84 and H_tot/int|h| -0.83 -> -0.47
    at the cost of the shell residual (holdout rho_u^max 0.0527 -> 0.228, sigma_u^max 1.9 -> 2.7) and of the far closure (carried mismatch 0.22 -> 2.29: the
    balance rows act through the B/D channel amplitudes, as in the lead's S9c reading). Balances not attained: R10 (c), optimizer-limited. Mechanism: 'global
    balance' rows conflict with the shell residual and the weight-100 non-axisymmetry guards on this start; the stall is a Gauss-Newton geometry fact (no
    descent direction accepted at any damping), not a time limit. On the nest4 (0.45, 1) L4 start the same rows converged (item 26). The L6 (0.45, 1) p0 run
    is in progress; if it converges, the difference is the start (balanced core, small guards) rather than the level. Possible Stage II remedies: a continuation
    in lambda from 1e-2, guard rows at weight 10, or the balance rows on the far channels only (S9c-type seed) before the LM.
31. (2026-10-25T12:45Z) Global-balance rows with guards on the balanced-core nest start at L6-ext (S9b lambda = 1 on nest6 (0.45, 1) p0; 300 iterations): the LM
    serves the balance rows (cost 1.44 -> 0.034; E_ren -1.54 -> +0.003) and destroys everything else: holdout rho_u^max 0.046 -> 0.448 (9.7x), sigma_u^max
    0.43 -> 7.5, a_max 0.43 -> 48, carried mismatch 0.35 -> 5.8, max E_F 1.25 at 35 R0, H_tot/int|h| -0.71 -> -0.19 (helicity balance not attained). The
    energy balance is bought first from the B/D channels (far E_F overshoot; FAILURE_ANALYSIS 30 saw the same on the D6 lineage before the stall) and then
    from the core amplitude (max|Omega| 12.9 -> 30), which the e_core/e_F guards do not pin. Mechanism 'global balance: attained by far-channel and core
    escape'; the scalar rows at lambda = 1 outweigh the PDE rows by 1e7 in cost. R10 (c). Remedy for Stage II: scale lambda to the PDE cost (1e-3 to 1e-2) or
    continue in lambda from 1e-4, add the S8 core-amplitude pin and the S11 closure rows at weight 1, so that the balances must come from the core shape.

## 2026-10-25T17:47Z (shift 5), new items
32. (2026-10-25T17:47Z) L10 with SPEC-degree channels did not fit the dense Levenberg-Marquardt (infrastructure, not a model failure): at L10 Nk24 with
    channels B23/D22/E10 the dense Jacobian is 1 287 900 rows x 4515 unknowns = 43.3 GiB beside the 21 GB model; three attempts of the 3-iteration smoke OOMed
    (two in the torch.cat of the column chunks, the third at the SECOND Jacobian allocation after one completed iteration of 160 s), because lm_solve kept the
    previous Jacobian bound into the next build: every dense job had held TWO Jacobians at its peak (ledger allocated peaks: Nk-8 smoke 78.0 GB for two 30.7 GB
    Jacobians; L8-ext jobs 75 GB in nvidia-smi). Repairs (16:17Z, lm.py sha256 ae98e4520350): J released right after J^T J, J^T r and the Marquardt diagonal
    (val8dense at L8 then peaks at 50.4 GB; the Nk-8 production run at 44.6 GB in its LM against 78.0 GB before); split-column J^T J accumulation lm_solve(jtj_blocks=k)
    (memory J/k, time (k+1)/2; validated at L8: two-step displacement equal to 4.6e-11, costs to 2e-15; at L10 the first-iteration cost and lam equal the dense
    attempt's); the SPEC-channel L10 runs use k = 2 (234 s per iteration, LM peak 61 GB). Lessons: a code fix saved at time T does not reach a job launched before T
    (a retry launched 3 min before the fix re-ran the old code and looked like a failed fix); every job now logs the sha256 of lm.py/worker.py/problem.py/fields.py
    at launch. The battery at L10 reserves up to 80 GB in nvidia-smi but allocates 53 GB (ch19 smoke); foreign torchlean processes hold 0.5-1.6 GB per GPU.
33. (2026-10-25T17:47Z) Radial resolution at fixed angular degree is closed on both branches (s1nk Nk 24 and Nk 32, four runs, 1.4-2.0 GPU-h each, 2 h limit
    at 238-239 iterations without GN stationarity): D6 lineage d6w3_L6 0.0527 / 0.0695 (Nk 16) -> 0.0528 / 0.0724 (Nk 24) -> 0.0508 / 0.0701 (Nk 32) with the radial
    Chebyshev tails 1e-2 -> 3e-4 -> 2e-4 and sigma_u^max 1.8, a_max 1.8 unchanged; nest (0.45, 1) 0.0460 / 0.0463 -> 0.0451 / 0.0445 -> 0.0451 / 0.0451 with
    sigma_u^max 0.43, a_max 0.46 unchanged and the balances unchanged (E_ren -1.56, H_tot/int|h| -0.70). The floors move by at most 4 per cent while the radial
    truncation falls by up to 50x: neither L6 floor is radial-resolution-limited under the tested optimizer and budget. Mechanism class 'resolution direction
    excluded'; the angular direction (L8 -> L10) and the channel radial direction (Nk 4 -> 8) remain under test.
34. (2026-10-25T17:47Z) The third nest branch at L8 (nest8 (0.42, 0.3) p0, 3.4 GPU-h): holdout 0.0622 / 0.0675 against 0.0641 / 0.0716 at L6 (q 0.970 / 0.942,
    max_iter at 300 with V10 5.8e-3): the L8 step lowers the holdout by 3-6 per cent, improves the far closure (carried mismatch 0.35 -> 0.21, K_E ratio +5.4 -> +3.9)
    and the sampled Q_sw (0.72 -> 0.53), and leaves both global balances unchanged (E_ren -3.94, H_tot/int|h| -0.79, core alignment -0.985): the same pattern as the
    two c_l = 0.45 rungs (balanced resolved core, negative renormalized energy and helicity balances, wrong far correction). The radial-lambda share of the
    momentum residual is 0.80 (lambda > 0 on 12 of 13 octaves): the residual is again mostly a positive radial multiple of U (d93). Bounded continuation queued.
35. (2026-10-25T18:50Z) Pressure source resolution (lead 17:49Z item 2 (b); verifier direct comparison: grad P global rel L2 9.2e-10 with 1.7e-4 relative at the
    outermost radius). At fixed coefficients of nest8 (0.45, 1) p0 cont150 the pressure source f = sum_ij d_i U_j d_j U_i was re-sampled on 3 Nk (the exports), 6 Nk and
    9 Nk Chebyshev-Gauss nodes and P, grad P recomputed on the export grid (scripts/pressure_source_resolution.py): 3 Nk reproduces the export exactly; 6 Nk and 9 Nk
    agree with each other and differ from 3 Nk by P rel L2 3.3e-11 and grad P rel L2 7.5e-10 globally, by 1.06e-4 relative at the outermost export radius (4.8e5 =
    1.6e6 R0) and by 4.86e-3 at one of the verifier's 224 selected points (median 5.8e-9; the other selected radii 1.3e-11 at 0.024 R0 to 1.7e-6 at 391 R0). At that
    outermost radius RMS |grad P| is 6.2e-21 against 5.2e-8 for the five momentum terms (ratio 1.2e-13). Far-shell effect on the shell ratios, five-term-normalized
    (the measurement the lead asked for 18:52Z): max over the export radii of max over the sphere of |Delta grad P| / RMS(five momentum terms on that sphere) =
    7.58e-9 for 3 Nk against 6 Nk (at r 2.16 R0) and against 9 Nk (7.58e-9, same radius), 7.09e-11 for 6 against 9 Nk (at 0.76 R0) [component max of Delta grad P over the
    unweighted node mean of the five non-pressure pieces with the rotation pieces split, the 18:52Z definition; with the SPEC 7.2 per-sphere denominator (sum of the
    weighted RMS of (1-c_l)U, c_l (y.grad)U, omega(JU - (Jy.grad)U), (U.grad)U, grad P) and the vector max: 4.0018e-9 (60 vs 120 nodes) and 3.0283e-11 (120 vs 180);
    against the nonlinear scale RMS((U.grad)U) + RMS(grad P): 1.80e-4 and 2.02e-7, both at the outermost sphere; single-sphere rho_u changes at most 1.26e-11, rho_nl
    at most 3.35e-6 (verifier 19:10Z, lead 19:16Z; the script reports both denominators from 19:20Z on)]; on the outermost sphere the
    change is 2.25e-4 of the local RMS grad P and 2.7e-17 of the five-term RMS (3 vs 6 Nk), 2.5e-7 and 3.0e-20 (6 vs 9 Nk); grad P relative L2 7.5e-10 (3 vs 6)
    and 7.7e-12 (6 vs 9). The arrays per resolution are saved with a sha256 in reports/pressure_gradP_grids_<cid>.npz for the verifier; the registered per-shell
    holdout re-evaluation with the 6 Nk source on the (0.45, 0.3) continuation (nest8 (0.45, 0.3) p0 cont150; reevaluate_holdout.py --light, 60 and 120 source nodes,
    reports/holdout_src60_*.json and holdout_src120_*.json, 20:19Z) COMPLETES this item: per shell the largest relative changes are rho_u 1.95e-7 (std, shell
    [8192, 16384) R0) and 1.89e-7 (half, [5793, 11585) R0), rho_nl 1.66e-7 / 1.73e-7, rho_sp the same, absolute fixed-gauge RMS(R_u) 1.95e-7, growing monotonically
    outward from 1e-12 for r < 32 R0; single spheres 2.06e-7 at 8266 R0; the maxima over shells change by at most 1.1e-12 (rho_u^max), 8.4e-13 (rho_nl^max), 3.6e-13
    (sigma_u^max), 6e-14 (a_max); K_E, K_H, carried mismatch and the balances are unchanged to all digits. Over every stored value above 1e-6 in magnitude
    (lead's full-JSON comparison 20:22Z, agreeing with the lane's) the largest relative change is 5.0e-7: pi_nl of the half family on shell 22 [11585, 23170) R0
    (6.741823e-2 -> 6.741819e-2), next the shell maximum of |R_u| on that shell (5.5e-7), kappa_far / Phi_F at the finite radius 2^14 R0 (4.4e-7) and the peak
    factor on shells 20-22 (3e-7 to 4e-7). No reading, 7.3b ordering or tier statement moves;
    scope: one state, one resolution step, the registered holdout construction, primary-reported. Source moments (scripts/pressure_source_moments.py; Cartesian int y_i f dy; finite = quadrature up
    to the last source node, exterior = the solver's log-s continuation beyond the last source node, where the Chebyshev interpolant of the factored source is EXTRAPOLATED at x_from_r(s, R0) (not frozen) under the envelope (sqrt(s^2 + R0^2)/R0)^(-p0), cut off at L_ext = 41.5/(p0 - 2) in log radius): moment 0 finite -6.80e-6 + exterior 6.80e-6 = -4.1e-12
    (3 Nk), -9.19e-7 + 9.19e-7 = -4.7e-14 (6 Nk); moment 1 (z) finite +7.732e-3, exterior -7.728e-3, total +4.07e-6 (3 Nk); +4.175e-3, -4.173e-3, +2.21e-6 (6 Nk):
    the total is a near-cancellation of finite and exterior parts of order 1e-3 (lead d122: the full-space monopole and dipole of f = d_i d_j (U_i U_j) vanish exactly
    for a divergence-free U ~ r^-alpha, alpha > 1; the finite-ball parts scale as R^(1-2 alpha) and R^(2-2 alpha): ratios 0.5400 / 0.5402 predicted, 0.6975 / 0.698);
    the residues 4.07e-6, 2.21e-6, 1.54e-6 (3/6/9 Nk) are 0.99511, 0.99935, 0.99981 of the exterior part times exp(-(p0 - 4) L_ext) = 5.285e-4 (lead 19:16Z after the
    verifier's 19:10Z review), i.e. the moment diagnostic's own exterior cutoff (the dipole integrand decays like exp(-(p0 - 4) t) while the cutoff L_ext = 41.5/(p0 - 2)
    was set for the l = 0 outer pressure kernel, which decays at p0 - 2 and keeps 9.5e-19; the l = 1 outer and origin kernels decay at p0 - 1, cutoff fraction 4.0e-26).
    CONFIRMED by the extended-cutoff rerun (ext_factor 3, L_ext 50.9): at 3 Nk the total dipole drops from +4.07e-6 to -2.0e-8 with the finite part (7.732021e-3),
    moment 0 (-4.09e-12) and the l = 1 kernel moment (-5.960309537982493) unchanged. The pressure itself is unaffected. No full-space dipole (which would add a harmonic
    r^-2 pressure term) is claimed. The solver's l = 1 kernel moment that feeds grad P at the origin is
    converged (-5.9603095379825 against -5.9603095379891, 1.1e-12). Mechanism class 'pressure reconstruction precision in the far field'; it matters for Tier R/A
    claims at r >= 1e5 R0, not for the Tier S ranking. Remedy if ever needed: Nr_src 6 Nk for the exports' pressure (cost about 1.5x of the pressure tables).
36. (2026-10-25T19:23Z) Data-handling incident, no campaign data lost: the pressure source-resolution diagnostic (scripts/pressure_source_resolution.py) wrote its
    outputs to fixed paths; a 3 Nk reproduction rerun started 19:12:21Z (OMP_NUM_THREADS=2, factors 3 only) overwrote at about 19:16Z the full 3/6/9 Nk results of the
    18:54-19:06Z run: reports/pressure_source_resolution_nest8_L8_cl0.45_om1.0_p0_cont150.json (pairwise metrics, selection) and reports/pressure_gradP_grids_
    nest8_L8_cl0.45_om1.0_p0_cont150.npz (sha256 a7912b0d...c87a; the full value is in the verifier's frozen snapshot PRESSURE_GRIDS.npz of 19:10:14Z in
    <independent-route directory>/independent/experiments, from which the lead's and the verifier's recomputations were made, so their readings stand on an intact copy). The numbers also
    survive in logs/adhoc/pressure_source_resolution_v2_1854.log. Repair: --tag suffix on every output (reruns never overwrite), OMP thread count and write time
    recorded in the JSON, and the full run repeated as *_v3 with 3 threads (the thread count matters: the 2-thread rerun reproduced the export's pressure only to
    P 3.6e-15 / grad P 2.0e-13 relative, the 3-thread runs bitwise, so the BLAS summation order, not the solver edit of 19:07Z (ext_factor, default path), is the
    source of the 1e-13 differences; the 3-thread v3 run with the edited solver reproduced the export bitwise at 19:22Z, and its regenerated grids npz
    (19:29:38Z) has the SAME sha256 a7912b0d12bd734347a84a080109881105b413aecb6ccc64e8716a0335b2c87a as the overwritten file: the loss is fully repaired). Lesson: diagnostic scripts take an output tag
    and refuse to overwrite; ledger and candidate files were never at risk (immutable exports, append-only ledger).
    Addendum (2026-10-25T19:35Z, lead 19:34Z / verifier l0_pressure_moment_attribution 19:29Z, lead review d127): the outer-sphere 60-to-120-node grad P difference is
    MONOPOLAR: the l = 0 share is at least 0.995 for r > 1e4; the verifier's matched l = 0 Green integral reproduces the outermost-sphere difference to 0.31 per
    cent; the solver's volume-integral monopole of the interpolated source is -4.0936e-12 (3 Nk), -5.157e-14 (6 Nk), -4.411e-14 (9 Nk), so Delta M0 (3 -> 6 Nk) =
    4.0420e-12 against 4.0418e-12 from the projected gradient difference times 4 pi r^2: the cause is the spurious full monopole of the 3 Nk interpolated source acting
    through -M0 n / (4 pi r^2); the l = 1 dipole is a minor part (l1m0 share 8.7e-5 on the outermost sphere). The 120-to-180 amplitude (about 1e-14 in M0) is at the
    arithmetic floor and stays OPEN quantitatively. Scope: a verifier-confirmed finite cause of the outer-sphere difference; no enclosure, no pressure correction
    (no fitted harmonic term is added to any pressure). Recommendation for Stage II exports (lead): write the solver volume-integral M0 (and a properly computed M1z)
    of the interpolated source into the export metadata and provide a second grad P at 6 Nk source nodes where far shells matter; the running jobs stay as they are.

## 2026-10-25T23:12Z (shift 6), new items
37. (2026-10-25T23:12Z) Correction-channel radial resolution: a partial gain with a core/far trade-off (nest8nk8, L8 (0.45, 1), omega/c_l = 20/9; B/D/E channel
    blocks at Nk 8 instead of 4 from the cont150 state; 150 iterations, max_iter, V10 8.9e-3; 4.4 GPU-h; primary-reported). Holdout rho_u^max 0.04082 / 0.04141
    against 0.04367 / 0.04331 (6.5 and 4.4 per cent lower; the L6 -> L8 step q is recomputed to 0.887 on the standard family and stands at 0.940 on the offset family,
    both above 0.85, so the branch keeps exactly one weak step and the L10 rung decides R2; lead 23:09:17Z). The far side improves by an order of magnitude (carried
    mismatch 0.067 -> 0.0079, K_E ratio -4.94 -> +0.243 with the right sign, K_H ratio 1.005, rho_nl^max 1.135 -> 0.854; the radial tails of B, D, E fall from 0.121,
    0.140, 0.204 to 0.032, 0.027, 0.115, so block E is still not radially resolved), while the core worsens (the centre-weighted ball RMS a_max on the balls at the vorticity maximum 0.604 -> 0.836
    at a_eff/2 and 0.549 -> 0.810 at a_eff/4, sigma_u 0.373 -> 0.417 at a_eff/4, strain ratio at the located maximum 0.985 -> 0.394, tau_0 4.4e-3 -> 6.0e-3, max|U| +11
    per cent, max|Omega| +16 per cent) and both global balances stay at order one (E_ren -1.36, H_tot/int|h| -0.71). Under the SPEC ordering rule the Nk-8 state is
    NOT ordered ahead of cont150: the lower shell residual is bought with a worse core. Mechanism: the correction channels at Nk 4 under-resolve the carried far
    correction (the first far coefficient had the wrong sign at Nk 4); resolving them moves the far closure but not the core single-term ratios or the balances, ; the
    measured single doubling leaves a factor of about 4 to the Tier S bound and does not justify the further doublings it would take within the current allocation (a
    resource decision, not an asymptotic obstruction: one observed doubling fixes neither a resolution limit nor a future rate; verifier qualification 23:12:52Z). Follow-ups (lead): an Nk-8 rung on the
    (0.45, 0.3) branch declined; L10 with channel Nk 8 only if the L10 reading gives q_10 in (0.85, 0.92); a 150-iteration continuation of the Nk-8 run enqueued at
    the lowest priority (does the core loss persist when the run settles; read by the ordering rule; does not reopen R2). Export: candidates/nest8nk8_L8_cl0.45_om1.0_p0
    (second pressure at 6 Nk source nodes). A floor statement for a branch with q_10 > 0.85 reads "floored at correction-channel Nk 4".
38. (2026-10-25T23:12Z; wording per the verified reading, lead d128 AO 23:28Z) Kill/resume determinism of the current worker (T11 literal criterion; CPU, 1 thread,
    three deterministic runs, runs/t11lit): over the registered window, iterations 13 to 22, T11 at 1e-10 is met with a maximum relative coefficient difference of
    1.4e-14; costs bit-equal at 7 of 10, damping and acceptance equal at 10 of 10; the iterate vectors are not bitwise equal at any of the ten steps (the hashes differ from the first post-kill iterate; the redundant startup phase projection moves the resumed vector by 1.3e-16
    relative, astra referee 23:20Z; the costs of the ten iterates differ by at most 1.6e-14, damping and acceptance exactly). Over 18 further iterations the LM amplifies the difference to 2.1e-10 in relative coefficient norm (max |dz| 5.7e-9 on max |z| 17.9)
    (outside the registered window; the field figure 4.3e-12 at five sampled points is not a SPEC comparison norm): consistent with rounding amplification by the damped reweighted Gauss-Newton iteration (an average factor of about 1.7 per
    iteration); that the difference lives in nearly null coefficient directions of the ill-conditioned basis is a hypothesis supported by five sampled field values, not
    demonstrated; the cause is OPEN. Not a gauge rotation (identical pivots; phase alignment changes nothing). Consequence: resumed and uninterrupted runs are the same state at the 1e-11
    field level, not bitwise; the historical bitwise record (2026-10-24T18:03Z) belongs to the older worker without reweighting, tail constraints and projection.
39. (2026-10-25T23:25Z) S10 primal versus curl formulation, first arm (s10_L6_cl0.45_om+1.0_fixed_both1: momentum rows plus vorticity rows at weight 1 with the full-space
    pressure, SPEC channels, closure rows 1e-3, all5far, from nest6 (0.45, 1) p0, omega/c_l = 20/9; 300 iterations max_iter, V10 -1.0e-2; 1.8 GPU-h; primary-reported).
    R11 label (registered 10:53:57Z; the lead's first label of 23:17Z, "curl residual small, momentum residual large: rejected", was corrected at the lead's request at
    23:27Z because the holdout vorticity ratio did not fall): "curl formulation, no improvement". Vorticity change mixed: holdout rho_Om^max +10 per cent (0.0697 ->
    0.0764), sigma_Om -22 per cent (0.406 -> 0.315). Momentum residual vector start -> end: holdout rho_u^max
    0.0460 / 0.0463 -> 0.2036 / 0.2065 (std / half), rho_nl^max 0.972 / 1.044 -> 1.042 / 1.069, sigma_u^max 0.432 / 0.400 -> 0.567 / 0.568 (core sets 0.446 -> 0.675),
    a_max 0.433 / 0.419 -> 0.446 / 0.444 (core sets 0.558 -> 0.500). Vorticity residual vector: holdout rho_Om^max 0.0697 -> 0.0764, sigma_Om 0.406 -> 0.315 (ball half
    0.379 -> 0.334). Guards (R10 (e)): e_core 0.112 -> 0.033, e_F 0.072 -> 0.006, N_core 0.76 -> 0.37, N_F 0.61 -> 0.16, rotation content 0.61 -> 0.18, max|U| 1.23 -> 0.88,
    sampled Q_sw 0.67 -> 2.12 (above 1), carried mismatch 0.35 -> 0.69, K_E ratio -2.27, E_ren -1.92, H_tot/int|h| -0.91. Mechanism: with both row sets at equal weight the
    LM lowers the vorticity-equation single-term ratio by shrinking the non-axisymmetric content and the amplitude, at the price of a 4.4x larger momentum residual and a
    worse far closure; the holdout vorticity ratio rho_Om^max does not fall. Not ordered ahead of its start under the SPEC rule; not a candidate. The weight-10 arm and
    the (0.45, 0.3) arms are read with both vectors; the "curl residual small" branch applies only if rho_Om^max falls on the holdout (a fall in sigma_Om alone does not
    qualify; lead 23:27Z).
40. (2026-10-26T01:14Z) S10 both formulation at weight 10, (0.45, 1), omega/c_l = 20/9 (s10_L6_cl0.45_om+1.0_fixed_both10, from nest6 (0.45, 1) p0; 300 iterations
    max_iter, V10 +0.128 (the reweighted cost still falling fast, far from stationary); 1.8 GPU-h; primary-reported): COLLAPSE to a near-trivial state. Momentum residual
    vector start -> end: holdout rho_u^max 0.0460 / 0.0463 -> 0.981 / 0.981 (std / half; the residual equals the five-term scale), rho_nl^max 0.97 -> 442, sigma_u^max
    0.432 / 0.400 -> 0.999 / 0.995, a_max 0.433 / 0.419 -> 8.48 / 8.19. Vorticity vector: holdout rho_Om^max 0.0697 -> 0.9416, sigma_Om 0.406 -> 0.498.
    Guards: max|U| 1.23 -> 0.056, max|Omega| 12.9 -> 0.045, rotation content 0.61 -> 0.0046, e_core 0.112 -> 5e-6, e_F 0.072 -> 3e-6, N_core 0.76 -> 0.005, a_eff 0.27 -> 3.5,
    sampled Q_sw 0.67 -> 3e5, carried mismatch 0.35 -> 2.8, K_E ratio -31.5, K_H ratio -243, E_ren -4.08, H_tot/int|h| -1.00; STRUCTURE near-linear True (b/a core 0.00-0.03).
    The state passes the formal nontriviality guards (max|Omega| > 1e-6, rotation content > 1e-3) but is an essentially irrotational, axisymmetric field whose velocity is
    5 per cent of the start's: the vorticity rows at weight 10 (R_Om weighted rms 0.67 against R_u 0.11 at the end) are minimised by removing the vorticity, and the
    momentum rows cannot hold the amplitude against them. R11 label: "curl formulation, no improvement" (the holdout rho_Om^max did not fall). Mechanism: amplitude
    instability (collapse toward the trivial state), as the unpinned viscous runs (item 24). Not a candidate; not ordered.
41. (2026-10-26T01:14Z) S10 both formulation at weight 1, (0.45, 0.3), omega/c_l = 2/3 (s10_L6_cl0.45_om+0.3_fixed_both1, from nest6 (0.45, 0.3) p0; 300 iterations
    max_iter, V10 -1.9e-2; 1.8 GPU-h; primary-reported). R11 label: "curl residual small, momentum residual large: rejected" (the lead's branch rule of 23:27Z applies
    because the holdout vorticity ratio fell: rho_Om^max 0.1148 -> 0.1081, -5.8 per cent; sigma_Om 0.439 -> 0.315, -28 per cent; the momentum residual rose 3.7x). Momentum vector: holdout rho_u^max 0.0669 / 0.0675 -> 0.2484 / 0.2491 (3.7x), rho_nl^max 2.54 -> 3.13, sigma_u^max 0.436 / 0.412 ->
    0.669 / 0.669 (core sets 0.599 -> 0.783), a_max 0.676 / 0.698 -> 0.733 / 0.743 (core sets 0.98 -> 0.74), a_eff 0.30 -> 0.24. Guards: e_core 0.142 -> 0.087, e_F 0.110 ->
    0.063, N_core 0.83 -> 0.61, N_F 0.77 -> 0.51, rotation content 0.75 -> 0.52, max|U| 1.12 -> 0.58, sampled Q_sw 0.50 -> 2.44 (above 1), tau_F 0.56 -> 0.87, carried
    mismatch 0.40 -> 1.58, K_E ratio -21.7, K_H ratio 5.1, E_ren -2.22, H_tot/int|h| -0.97. Same pattern as item 39 at (0.45, 1): the LM trades the momentum residual, the
    far closure, the amplitude and the non-axisymmetric content for a lower vorticity residual (here both rho_Om^max and sigma_Om fall, unlike item 39 where only sigma_Om
    fell). Not ordered ahead of its start; not a candidate. The weight-10 arm at (0.45, 0.3) (running) is read from its own data under R11.
42. (2026-10-26T03:15Z) S10 both formulation at weight 10, (0.45, 0.3), omega/c_l = 2/3 (s10_L6_cl0.45_om+0.3_fixed_both10, from nest6 (0.45, 0.3) p0; 300 iterations max_iter,
    V10 0.704; 1.7 GPU-h; primary-reported; DONE 2026-10-26T03:08:18Z): COLLAPSE toward the trivial state. Momentum vector start -> end: holdout rho_u^max
    0.06687 / 0.06753 -> 0.9989 / 0.9995 (std / half), rho_nl^max 2.543 -> 804.3, sigma_u^max 0.4364 / 0.4119 -> 1.002 / 1.003,
    a_max 0.6758 / 0.6983 -> 10.75 / 10.85. Vorticity vector: holdout rho_Om^max 0.1148 -> 0.9812, sigma_Om 0.439 -> 0.4977. R10 (e) guards FAIL (lead BN
    03:10:21Z): N_core 0.828 -> 9.23e-05, N_F 0.765 -> 0.000113, e_core 0.142 -> 2.1e-09, e_F 0.11 -> 3.16e-09; max|U| 1.12 -> 0.0497, max|Omega| 10.4 -> 0.0146,
    rotation content 0.748 -> 0.000105, a_eff n/a -> 8.7, carried mismatch 22.4, K_E ratio -5.86e+03, E_ren -4.34, H_tot/int|h| 0.176. With the
    non-axisymmetry guards failed the arm has no R11 reading; it is recorded as a collapse of the search toward the trivial state under the weight-10 vorticity rows (as
    item 40 at omega = 1). Mechanism: amplitude instability. Not a candidate; not ordered. S10 is complete with four arms (items 39-42): none is a candidate, the weight-1
    arms are rejected under R11 and the weight-10 arms collapse.

## 2026-10-26T03:44Z (shift 7), new items
43. (2026-10-26T03:44Z) S11 closure-row ladder completed at (0.45, 1), omega/c_l = 20/9 (s11_L6_cl0.45_om+1.0_fixed_cl1e-1 then s11_L6_cl0.45_om+1.0_fixed_cl1, from nest6 (0.45, 1) p0,
    holdout 0.04604 / 0.04630; L6 Nk 16 even, SPEC channels 4/4/4 deg 15/14/6, all5far; 1.30 + 0.50 reserved GPU-h). Weight 1e-1 (300 iterations, max_iter) met the far
    closure: carried mismatch m 0.346 -> 4.7e-4, K_E ratio -32.6 (nest6 start, FAR_COEFFICIENTS) -> 0.9992, K_H ratio 1.26 -> 0.9998, at holdout 0.04526 std / 0.04457 half
    (0.983 / 0.963 of the start). Weight 1 (from that end state) left the LM after 19 iterations with status ftol (relative cost decrease below 1e-7; cost 2.4257e-7 ->
    2.4248e-7; V10 1.5e-6): the end state equals the 1e-1 state to four digits on every standing line (m 3.8e-6, K_E 0.99998, K_H 1.0000; sigma_u^max 0.426 / 0.387,
    sigma_Om 0.405, a_max 0.435 / 0.384, core sets 0.613; e_core 0.127, e_F 0.086; E_ren -1.53, H_tot/int|h| -0.687; sampled Q_sw 0.705). R12 reading on the primary
    record: (a) 'far closure compatible with the floor'. WHAT IT SHOWS: the degree-6 floor of this branch does not rely on violating the first far-field correction
    equations; enforcing them exactly (to 4e-6) costs nothing on the holdout and leaves the core single-term ratios and both global balances (energy flux, helicity)
    exactly where they were. The open structural items of this branch are therefore the order-one global balance defects and the core terms, not the far closure.
    WHAT IT DOES NOT SHOW: nothing about Tier S (the state is 4.5x the bound), nothing about higher degree (L6 only), and the closure rows act on the lagged target
    G_required[F] of the current tail, so a tail that is itself wrong can be closed consistently. The state replaces its start in S1 (steering) only after the verifier's
    independent evaluation of the export candidates/s11_L6_cl0.45_om1.0_cl1. kappa(R) remainder: deviations from K_E -4.656 / -1.642 / -0.549 at 2^12 / 2^14 / 2^16 R0,
    ratios 0.353 and 0.334 against 4^(-7/9) = 0.340 (one rate on three radii; other finite-radius terms not excluded, verifier 02:34Z / 02:53Z). Mechanism (registered
    list): global balance. Not a candidate. Primary-reported, unvalidated.
44. (2026-10-26T04:51Z) S12 radial-lambda sphere rows at weight 3 (R13), both arms: s12_L6_cl0.45_om+1.0_fixed_rl3 (from nest6 (0.45, 1) p0, omega/c_l = 20/9, 1.25 reserved
    GPU-h) and s12_L6_cl0.42_om+0.3_fixed_rl3 (from nest6 (0.42, 0.3) p0, omega/c_l = 5/7, 1.00 GPU-h); L6 Nk 16 even, SPEC channels, closure rows 1e-3, all5far, 300
    iterations each (max_iter; V10 0.062 and 0.052, not stationary). The rows sqrt(w) sqrt(w_k) <U . R_u>_k / <|U|^2>_k^(1/2) on the 51 radial training nodes penalize the
    radial multiple lambda(r) U of the momentum residual (d93: 68-79 per cent of int |R_u|^2 on every nest-ladder export). RESULT: the share fell from 0.748 to 0.305 and
    from 0.793 to 0.397 (training grid, d93 definition; start values recomputed on the CPU), so R13 (c) 'not attained' at both points; the holdout rho_u^max fell by 5-15
    per cent (0.04604 / 0.04630 -> 0.04166 / 0.04428; 0.06414 / 0.07155 -> 0.05664 / 0.06078) while every other necessary-condition diagnostic got worse: core-set a_max
    0.56 -> 1.35 and 0.92 -> 2.12, sigma_Om 0.41 -> 0.57 and 0.47 -> 0.65, holdout vorticity ratio 0.070 -> 0.095 and 0.108 -> 0.305, strain ratio at the vorticity maximum
    1.03 -> 0.72 and 0.72 -> 0.28, sampled Q_sw 0.67 -> 0.20 and 0.72 -> 0.23, max|Omega| +40 and +61 per cent, far mismatch m 0.35 -> 0.54 and 0.35 -> 0.56 (K_E ratio
    372.7 and 8.4), E_ren -1.54 -> -1.13 and -3.90 -> -3.38, H_tot/int|h| unchanged at -0.71 to -0.83. WHAT IT SHOWS: on these branches the lambda(r) U component is not a
    removable artefact of the optimizer: forcing <U . R_u>_k down on every sphere moves the residual into the core single-term ratios, the vorticity balance and the far
    closure; the momentum shell ratio and the radial pairing can be traded against the other necessary conditions, which is the signature of a state that is not near a
    solution rather than of a misweighted objective. WHAT IT DOES NOT SHOW: a share of 0.2 was not reached (optimizer-limited by the registered rule), the test is at degree 6
    and weight 3 only, and the independent route has not checked the d93 share on these states. Neither state is ordered ahead of its start (SPEC 7.3b). Mechanism proposed
    for the failure map (lead's wording pending): core balance. Primary-reported, unvalidated; no candidate.
45. (2026-10-26T05:05Z) S11 closure-row ladder completed at (0.45, 0.3), omega/c_l = 2/3 (s11_L6_cl0.45_om+0.3_fixed_cl1e-1 then s11_L6_cl0.45_om+0.3_fixed_cl1, from nest6
    (0.45, 0.3) p0, holdout 0.06687 / 0.06753; L6 Nk 16 even, SPEC channels 4/4/4 deg 15/14/6, all5far; 1.05 + 0.34 reserved GPU-h). Weight 1e-1 (300 iterations,
    max_iter, V10 0.036) met the closure (m 0.399 -> 1.3e-3, K_E ratio 0.9983, K_H 1.006) at holdout 0.05795 / 0.05781 (0.867 / 0.856 of the start). Weight 1 left the LM
    after 50 iterations by ftol, but not from a plateau: the lagged-target objective made a TRANSIENT EXCURSION (iterations 9-29: the cost refreshed after each accepted
    step rose from 1.96e-7 to 1.11e-4 while every step was accepted under the frozen objective; iterations 30-40: back to 1.56e-7, below the start; 41-49 flat at
    1.5598e-7, |g| 5e-8). The end state is 20 per cent below the nest6 start on both shell families (0.05227 / 0.05368) and below the branch's degree-8 states (nest8
    p0 0.06128 / 0.06087 by 15 / 12 per cent; its cont150 0.05973 / 0.05940 by 12 / 10 per cent), with m 2.1e-6, K_E 1.000001, K_H 1.0000. R12 reading on the primary record: (a) 'far closure compatible with the floor'. WHAT IT SHOWS:
    (i) as at (0.45, 1), enforcing the first far-field correction equations exactly costs nothing on the holdout, so the degree-6 floor of this branch does not rely on
    violating them; the order-one global balance defects (E_ren -1.20, H_tot/int|h| -0.89) and the core terms remain. (ii) The lagged closure target G_required[F] can
    feed back on the tail: when the start is not stationary (V10 0.036 at the 1e-1 state) the weight-1 rows and the target refresh drive a 500-fold cost excursion before
    the state settles; here the excursion ended in a lower basin (the whole 10 per cent holdout gain of the rung happened during it), so it acted as a randomized
    continuation rather than a divergence. A diverging case would end 'stalled'; none has occurred in the four closure rungs. WHAT IT DOES NOT SHOW: nothing about Tier S
    (5.2x the bound), nothing above degree 6; the lower shell residual comes with a core-set a_max 21 per cent above the nest6 start (0.98 -> 1.19), so the state is not
    ordered ahead of its start under SPEC 7.3b; the ftol stop means 'LM-stationary at ftol 1e-7', not converged. Mechanism wording for the failure map as the lead's
    BV item 3 for the (0.45, 1) row: far balance excluded at degree 6 on this branch (R12 (a), primary); both global balances unmet at order one; global balance is the
    remaining candidate from the registered list, not established (S9d pending). Primary-reported, unvalidated; no candidate.
    ADDENDUM to items 43-45 (2026-10-26T05:28Z; after the astra referee pass ref_fa43_45, astra/ref_fa43_45/answer.md; each point below was checked against the arm_reading JSON
    files and the code before adoption; the lead's registered wordings in the failure map are reported to the lead, not changed here).
    (a) Items 43 and 45, the sentence 'the degree-6 floor of this branch does not rely on violating the first far-field correction equations' overreaches and is REPLACED
        by: at degree 6 (correction channels 15/14/6) both endpoints satisfy the measured first-correction criteria (discrete mismatch m reduced to 3.8e-6 and 2.1e-6
        against the freshly recomputed G_required[F] of the end state; K_E and K_H ratios 1.00000 and 1.0000) while keeping or lowering the holdout momentum ratios; this
        supports R12 (a) and does not exclude unresolved correction modes outside the carried span, other far-field terms, core-tail matching defects or optimizer
        limitations. 'Enforcing them exactly' is replaced by 'reducing the measured mismatch to 4e-6 / 2e-6'. The G_identity_rel entries of the rows (0.026, 0.023,
        0.017) are the ray-functional self-check G[L U] = U of src/far_field/ray_functional.py (a quadrature accuracy diagnostic of the ray functional), not a closure quantity.
    (b) Stopping rule wording: the ftol stop is a relative function-change criterion (one accepted step with relative decrease below 1e-7), not a gradient condition, and
        the frozen-objective gradient reported by the LM omits the derivative of the lagged target G_required[F]. 'LM-stationary at ftol 1e-7' is REPLACED by 'reached a
        terminal cost plateau and stopped under the relative function-change criterion ftol 1e-7; stationarity of the self-consistent objective is not established'. 'Equals
        the 1e-1 state to four digits on every standing line' (item 43) is replaced by 'unchanged to within 1e-4 relative on every standing line except the mismatch
        4.7e-4 -> 3.8e-6'.
    (c) Item 45: 'randomized continuation', 'lower basin', 'the whole 10 per cent holdout gain happened during the excursion' and 'a diverging case would end stalled' are
        WITHDRAWN: the iteration is deterministic, no intermediate holdout measurements exist (the holdout is evaluated at the end state only), and a divergent run can also
        end by the iteration limit or a numerical failure. The defensible description: an unsafeguarded lagged iteration, in which every step is accepted under the frozen
        objective (target and weights fixed) while the refreshed objective rose 500-fold and the Marquardt damping fell from 3e-3 to 1.5e-8; the excursion ended at a lower
        reported endpoint cost and lower holdout ratios. Recommended control (astra; a proposal for the lead, not run): replay from the same checkpoint with the target and
        weights frozen for blocks of five LM iterations, a common merit function with fresh G_required evaluated at block boundaries, backtracking of outer updates that
        raise it, a conservative damping restart (3e-3) after each refresh, and a record of step norms, predicted and actual reductions, frozen and refreshed costs
        (50 iterations, about 0.3 GPU-h at L6). A complete remedy would differentiate the closure rows through G_required[F].
    (d) Item 44, two premises CORRECTED: E_ren decreased in magnitude in both S12 arms (-1.543 -> -1.129, -3.895 -> -3.375), and the sampled Q_sw falling from 0.67 / 0.72
        to 0.20 / 0.23 is not a worsening of the necessary condition Q_sw <= 1 (item 21); 'every other necessary-condition diagnostic got worse' is replaced by 'the core
        single-term ratios, the holdout vorticity ratio, the strain ratio at the vorticity maximum and the far closure deteriorated; E_ren decreased in magnitude;
        H_tot/int|h| stayed negative and of order one with a slightly larger magnitude (-0.711 -> -0.740, -0.789 -> -0.831)'. 'The lambda(r) U component is not a removable
        artefact of the optimizer' and 'the signature of a state that is not near a solution rather than of a misweighted objective' are WITHDRAWN: R13 (c) is by
        registration inconclusive, the possibilities are not exclusive, and adding weight-3 projection rows changes the objective (the radial-multiple energy enters with
        weight 4 instead of 1), so a lower share with worse complementary defects is compatible with ordinary reweighting. The holdout range is 4-15 per cent (the (0.45, 1)
        half family fell 4.4 per cent). IMPORTANT QUALIFICATION: the unnormalized weighted training momentum RMS (ledger rms_mom) ROSE 23 and 25 per cent (0.09346 ->
        0.11509; 0.12684 -> 0.15886) while the normalized holdout ratios fell: the five-term denominators grew with max|U| (+27 / +34 per cent) and max|Omega| (+40 / +61
        per cent). Both runs stopped at the iteration limit with V10 0.062 / 0.052, so incomplete optimization is a live alternative. 'Redistributed, not removed' stays as an
        informal description of mixed diagnostic changes, not as a mechanism.
    (e) Item 45 arithmetic: the (0.45, 0.3) weight-1 state is 5.23x the Tier S bound on the standard family and 5.37x on the half-offset family (worse family governs);
        the holdout gain within the rung is 9.8 / 7.1 per cent (0.902 / 0.929), 21.8 / 20.5 per cent against the nest6 start; core-set a_max rose 7.2 per cent within the
        rung (1.110 -> 1.190) and 21 per cent against the nest6 start (0.982). The nest6 start values quoted in item 43 (K_E -32.6, K_H 1.26, m 0.346) come from
        reports/FAR_COEFFICIENTS.md (export of nest6 (0.45, 1) p0), not from the arm_reading rows.
    (f) Wording that belongs to the lead's registered failure map and is reported to the lead with astra's critique: 'far balance excluded at degree 6 on this branch'
        (astra: 'the measured first-correction mismatch can be made small at the observed holdout level'), 'global balance is the remaining candidate from the registered
        list' (astra: 'an untested proposed failure mechanism'; a short registered list is not exhaustive), and 'Q_sw got worse' in the S12 mechanism text (CO).

## 2026-10-26T12:45Z (shift 8), new items
46. (2026-10-26T12:45Z) S9d scaled balance chains completed at (0.45, 1), omega/c_l = 20/9, and at (0.45, 0.3), omega/c_l = 2/3 (lead registration 2026-10-25T17:20:02Z; Z0 = the S11
    weight-1 end states; balance rows lambda_k = sqrt(kappa_k C0 / b0) on E_ren and H_tot/int|h|, kappa 0.1, 1, 10, 100, 100 LM iterations per step, closure rows at weight 1,
    core RMS and e_core / e_F pinned at Z0; 4.82 reserved GPU-h in total). Curves (Z0, kappa 0.1, 1, 10, 100): (0.45, 1): E_ren -1.530, -1.311, -1.226, -1.160, -0.941;
    H_tot/int|h| -0.687, -0.677, -0.668, -0.662, -0.645; holdout rho_u^max (standard family) 0.04526, 0.04484, 0.04519, 0.04574, 0.05297; rms_mom +2.0, +3.4, +4.7, +30.2 per
    cent; far-shell rho_nl on [512, 1024) (table shell) 0.055, 0.043, 0.058, 0.348, 2.18; core-set a_max 0.613, 0.675, 0.682, 0.682, 2.85; kappa(2^12 R0) -3.66, +0.26, -0.06,
    -6.68, -45.4. (0.45, 0.3): E_ren -1.203, -1.203, -0.900, -0.649, -0.596; H_tot/int|h| -0.891, -0.891, -0.823, -0.734, -0.694; holdout 0.05227, 0.05227, 0.05266, 0.05445,
    0.07143; rms_mom +0, +7.7, +20.8, +58 per cent; far-shell rho_nl 0.074, 0.074, 0.078, 0.223, 0.742; core-set a_max 1.19, 1.19, 1.29, 1.33, 1.26; kappa(2^12 R0) +0.59, +0.59,
    +0.60, -1.37, -11.85. The R10 (e) guards (N_core, N_F, e_core, e_F) pass at every step (the non-axisymmetric fractions are pinned by construction). Three LM behaviours:
    unsafeguarded lagged-iteration excursions at kappa 0.1 and 1 (cost rising with the damping collapsing to 1e-8, then returning); near-flat total cost at kappa 10 for
    omega 1 (0.6 per cent in 100 iterations); a plateau stop (ftol) after 72 iterations at kappa 100 for omega 0.3; the terminal costs are the cost_after_reweight values.
    READING (R10, the last step's): (c) balances not attained on both chains; the lead's failure-map entry (d128 GC item 4) for (0.45, 1): 'Global balance: ... |E_ren| fell from
    1.530 to 0.941 and |H_tot|/int|h| from 0.687 to 0.645, both far above the 0.05 bounds. Over the same steps the far-shell rho_nl on [512, 1024) rose from 0.055 to 2.18, and at
    kappa 100 the holdout rho_u^max rose 17 to 22 per cent and the core-set a_max 4.7-fold. R10 (c): optimizer-limited, inconclusive.' The (0.45, 0.3) entry in the lead's wording (d128 GJ item 3, adopted 2026-10-26T12:54Z):
    'Global balance: the S9d chain at c_l = 0.45, omega = 0.3, omega/c_l = 2/3, L6, pinned core, took four kappa steps from 0.1 to 100 under the registered budgets. |E_ren| fell
    from 1.203 to 0.596 and |H_tot|/int|h| from 0.891 to 0.694, both far above the 0.05 bounds; the last step reduced |E_ren| only from 0.649 to 0.596. Over the same steps the
    far-shell rho_nl on [512, 1024) rose from 0.074 to 0.742. At kappa 100 the holdout rho_u^max was 32 to 37 per cent above Z0, rms_mom 58 per cent above, and the holdout
    vorticity ratio 1.7 times Z0's. The last step stopped on the function-change tolerance, and stationarity is not established. R10 (c): optimizer-limited, inconclusive.'
    WHAT IT SHOWS: along these two paths, at degree 6 and with pinned non-axisymmetric content, three decades of balance weight reduce |E_ren| by at most 39 and 50 per cent
    and |H_tot|/int|h| by 6 and 22 per cent; the reductions come with growth of the far-shell nonlinear-balance ratio (10- to 40-fold on the table shells, with successive
    log2 slopes close to alpha - 2 = -7/9, the SPEC 4.4 r^(alpha + 1 - j) at j = 3, and no growth of the j = 1, 2 type), a growing far remainder kappa(R) with the single-rate
    pattern intact, and at kappa 100 a higher holdout and (omega 1) a 4.7-fold core amplitude ratio: a trade-off along each path. WHAT IT DOES NOT SHOW: unattainability of the
    balances (one path at one level and one budget each), anything about Tier S, anything above degree 6, and nothing beyond r = 32768 (the three outer far shells are
    pressure-model shells). Mechanism for the failure map: global balance (R10 (c), optimizer-limited, inconclusive). Primary-reported, unvalidated; no candidate.
47. (2026-10-26T12:45Z) All-m arm from nest6 (0.45, 0.3) p0 with an m = 1 perturbation of 10 per cent of ||U|| (s4allm_L6_cl0.45_om+0.3_fixed_m1rel0.1; all-m basis 243 modes, 120 odd; 260
    iterations to the 7200 s time limit; 2.24 reserved GPU-h). The LM removed the perturbation's cost within 50 iterations (5.49e-4 -> 3.10e-7, the parent's level) and ended at
    2.978e-7 with the holdout 0.06502 / 0.06595 (0.972 / 0.977 of the start), rms_mom +0.1 per cent, both global balances unchanged (E_ren -1.716, H_tot/int|h| -0.889), core-set
    a_max 1.016 (+3.5 per cent), Q_sw 0.503, rotation content 0.751. The odd-m part of the end state, evaluated as RMS ratios of the odd-m field on the training grid: ||U_odd|| /
    ||U|| 0.082 (injected 0.10), ||Omega_odd|| / ||Omega|| 0.121, ||DU_odd|| / ||DU|| 0.148; 0.094 in the core (r < 0.125) and 0.043 in the tail (r > 8), i.e. energy fractions
    0.9 and 0.2 per cent (the worker's RAY by |m| line prints energy fractions at two decimals and shows m1 0.00 for that reason). WHAT IT SHOWS: at degree 6 on this branch an
    order-0.1 odd-m admixture is retained (neither grows nor vanishes within 260 iterations) while the holdout ends 2.8 per cent below the even-class state; no evidence that odd
    modes lower the residual materially; odd-mode states are not excluded (lead d128 HB item 4 wording, adopted 2026-10-26T14:37Z; 'floor' is reserved for R2 ladder statements). WHAT IT DOES NOT SHOW:
    anything about odd-m seeds of order one, other branches, degree 8, or Tier S. Ordered ahead of its start under SPEC 7.3b (holdout lower on both families; core ratios 0.985 /
    1.004 / 1.035, all at most 1.10; corrected 2026-10-26T13:58Z after lead d128 GU item 2: the first version said 'not ordered', misreading 7.3b). Second arm (the s7c L4 m = 1 state
    promoted to L6, omega 1) running. Primary-reported, unvalidated; no candidate.
48. (2026-10-26T13:49Z) ftol 1e-10 optimizer diagnostic on the S11 (0.45, 1) weight-1 state (s11_L6_cl0.45_om+1.0_fixed_cl1ftol; lead d128 BY: an optimizer-limitation diagnostic, not an
    R12 re-reading; 300 iterations max_iter; 1.13 reserved GPU-h). The weight-1 rung had stopped after 19 iterations under ftol 1e-7 (item 43). Continued under the same lagged
    objective with ftol 1e-10, the LM stayed on a plateau for 87 iterations (relative decreases 7e-7 to 2e-6 per iteration; minimum cost 2.4239e-7 at iteration 72, 0.04 per
    cent below the start) and then made an unsafeguarded lagged-iteration excursion: the cost rose to 5.24e-4 at iteration 186 (2160 times the start) with the damping at
    1.6e-10 and fell back only to 2.8e-6 post-step at iteration 299; terminal cost_after_reweight 1.018e-5, 42 times the start. WHAT IT SHOWS: the ftol 1e-7 stop was a genuine
    plateau of the lagged objective at this state, and the lagged-target refresh (closure target and nonlinear weights recomputed after every accepted step while the LM
    accepts on the frozen objective) can drive an excursion of three orders of magnitude that does not return within 300 iterations; this is the mechanism of items 44 and
    45 in a cleaner setting (no change of objective, only the stopping tolerance). WHAT IT DOES NOT SHOW: a lower-residual state (the end state's cost is 42 times the
    start; its lower normalized holdout, 0.03114 / 0.03330 = 0.688 / 0.747 of the start, comes with rms_mom +6.7 per cent, max|U| +37 per cent, max|Omega| +41 per cent and
    core-set a_max +49 per cent, the S12 denominator pattern), and nothing about Tier S. The end state is not read as a state and enters no ordering. A safeguarded refresh
    (shift 7 worker flag, default off) is the registered remedy; its control replay s11_L6_cl0.45_om+0.3_fixed_cl1_safeguard is pending at priority 7. Primary-reported.

49. (2026-10-26T15:05Z) S8 pinned artificial-viscosity ladder at (0.45, 0.3), omega/c_l = 2/3, complete (lead S8 registration 2026-10-25T05:14:51Z, readings R7 to R9; steering 2026-10-25T06:56Z:
    omega and c_l fixed, core RMS of U on the training nodes r < R0 pinned at its start value with row weight 100, nu ladder upward by factors of about 3). Start d6t_L6_cl0.45_om+0.3_fixed
    (inviscid holdout rho_u^max 0.05521 / 0.07482). Rungs nu 6.5e-5, 2e-4 (2026-10-25T07:38Z) and 6.5e-4, 2e-3 (2026-10-26T14:47Z), 300 LM iterations each, 0.010 to 0.32 c_l a_eff^2
    (a_eff 0.117 to 0.119). WHAT WAS OBSERVED: the viscous residual floor rho^nu_max on a fresh holdout 0.0551 / 0.0565 / 0.0613 / 0.0768, i.e. 1.00 / 1.02 / 1.11 / 1.39 times the start's
    inviscid floor (R8: at least one half at every rung, 'viscosity does not remove the floor'); the single-term ratio sigma^nu_max 2.00 to 2.77 against the R7 (a) bound 1e-2 and E_ren
    -1.09 to -1.18 against R7 (b) E_ren > 0: every rung is a 'viscous solve, not converged' ((c) and (d) not read). The viscous share of the terms is linear in nu (0.0014 / 0.0043 /
    0.0140 / 0.0429; share/nu 21.4 to 21.7), the inviscid rho_u of the viscous state rises monotonically from 0.99 to 1.17 of the start (half family 1.00 to 1.10), rms_mom from 1.04x to
    1.85x, and the core holds (max|U| and max|Omega| within 2 per cent, m = 2 tail fraction 0.05 at every rung, e_core 0.144 to 0.185, rotation content 0.47): with the pin there is no
    trace of the collapse of the unpinned free-omega runs (item 24; viscous shares 0.9 to 0.99 there). MECHANISM READING: at fixed omega, c_l and core amplitude, the AV device is a
    regular perturbation of the inviscid problem on this branch whose only effect up to nu 2e-3 is to add a residual proportional to nu; it does not open a lower-residual path, and its nu
    -> 0 end is the inviscid start itself. R8's consequence: the floor of this branch is not the transport degeneracy alone. WHAT IT DOES NOT SHOW: anything about Euler profiles (R8);
    nothing about nu above 2e-3 with the pin (not run; the unpinned runs at 3.8e-3 and above collapsed), nothing about continuation with omega free at these nu (one free-omega run at
    6.5e-4 moved omega 0.300 -> 0.323 in 129 iterations without collapse, item 24). Primary-reported. The omega 1 ladder on nest6 (0.45, 1) p0 (nu 3.5e-4 and 1e-3) is running.

50. (2026-10-26T15:05Z) S7 (c) m = 2 eddy boost at L6 on nest6 (0.45, 1) p0, omega/c_l = 20/9 (s7c_L6_cl0.45_om+1.0_fixed_m2ecore0.25; lead S7 registration, R6: promotion needs tau_F at most half
    the start's with the holdout within 1.2x and Q_sw <= 1). The boost multiplied the m = 2 eddy part by 1.622 to raise e_core from 0.1125 to 0.25; the boosted start had LM cost 15.63
    against the parent's pde block 2.7e-7 (6e7x). WHAT WAS OBSERVED: in the registered 300 iterations the LM reached 1.218e-4 (447x the parent; damping 1.8 to 9, cost still falling about
    3 per cent per 10 iterations, V10 0.131); the end state has holdout rho_u^max 0.448 / 0.556 (9.7x / 12.0x the parent), core-set a_max 25.4 (45x), max|Omega| 30.9 (2.4x), e_core
    0.526 (the target 0.25 was not held; the eddy fraction doubled again along the path), tau_F 1.55 (2.7x the parent's 0.583), Q_sw 0.138, E_ren -0.953, H_tot/int|h| -0.466, no
    collapse of the non-axisymmetric content (tail m = 2 fraction 0.12), and an unresolved radial expansion (SPECTRUM A 0.445, C 0.360 at Nk 16). READING: 'swirl condition not met'
    (R6: tau_F up, not down; holdout 10x); an amplitude excursion of the core of the kind seen in the omega 2.0 from03 arm (item 44), not read as a state, no 7.3b ordering. At L4 the
    same boost relaxed back to the even state in 69 iterations (item 24 / S7 (c) L4 row); at L6, with 3.5 times the unknowns and the boosted start 6e7 times above the parent in cost,
    the LM path did not return within 300 iterations. WHAT IT DOES NOT SHOW: that no state with e_core near 0.25 exists on this branch (the arm shows one LM path from one boosted
    start); nothing about Tier S. The S7 (c) m = 2 line at L6 is complete under the registered budget; the all-m m = 1 arm at L6 is running. Primary-reported.
    Addendum (2026-10-26T16:18Z): the companion m = 1 seeding arm at L6 (s7c_L6_cl0.45_om+1.0_fixed_m1rel0.1; all-m basis, 10 per cent of ||U|| injected into the same start; 268 iterations,
    time limit 7200 s) relaxed back: the odd admixture decayed to 3.5 per cent of ||U|| (energy fraction 0.12 per cent; Omega 4.7 and DU 5.5 per cent; by radius 3.1 to 5.3 per cent),
    every standing line returned to within 1.3 per cent of the even start (holdout 0.04593 / 0.04622 = 0.997 / 0.998 of it; tau_F 0.582 against 0.583; Q_sw 0.68; E_ren -1.539;
    H_tot/int|h| -0.711), and the state is ordered ahead of its start under 7.3b by 0.2 to 0.3 per cent on the holdout (core ratios 1.002 / 1.002 / 1.005, same degree and holdout
    grid, core flags primary). READING: 'swirl condition not met' (R6); S7 (c) at L6 is complete: on this branch the swirl generation is moved neither by boosting the m = 2 eddies
    (amplitude excursion) nor by seeding m = 1 content (relaxes back). As the third S4 all-m arm it keeps the class wording (2.8 per cent below to 4.7 per cent above the even-class
    degree-6 state; no evidence that odd modes lower the residual materially; odd-mode states are not excluded). The fresh random all-m starts of S14 (lead d128 HE) test what
    perturbation arms cannot: odd-mode starts that are not perturbations of an even-class state. Primary-reported.
    Addendum (2026-10-26T16:27Z), the omega 1 ladder: on nest6 (0.45, 1) p0 (c_l 0.45, omega 1, omega/c_l 20/9; a_eff 0.27, so c_l a_eff^2 = 3.3e-2) the two registered rungs nu 3.5e-4 and
    1e-3 (0.011 and 0.031 c_l a_eff^2) give rho^nu_max 0.04913 / 0.05666 against the start's inviscid floor 0.04604 (R8 ratios 1.067 / 1.231: 'viscosity does not remove the floor'),
    sigma^nu_max 0.462 / 0.532 against 1e-2 and E_ren -1.454 / -1.502 (R7 (a) and (b) fail: 'viscous solve, not converged'), viscous share 0.005 / 0.015 (linear in nu), inviscid
    rho_u of the viscous state 0.995 / 0.981 then 1.034 / 1.017 of the start with rms_mom +7 and +23 per cent, the pin held and no collapse. The same mechanism reading as at (0.45,
    0.3): the AV device at fixed omega, c_l and core amplitude is a regular perturbation that adds a residual proportional to nu and opens no lower-residual path; S8 is complete on both
    registered branches (4.0 reserved GPU-h in Stage II). Not evidence about Euler profiles (R8). Primary-reported.

51. (2026-10-26T16:49Z) Degree-8 closure-met rung at (0.45, 1), omega/c_l = 20/9 (nest8_L8_cl0.45_om+1.0_fixed_cl1; lead registration BV/CR: the S11 weight-1 closure state
    s11_L6_cl0.45_om+1.0_fixed_cl1 embedded exactly at L8 with the closure rows at weight 1, channels 4/4/4 at degrees 19/18/8, all5far, tail constraints, 300 iterations
    allowed). WHAT WAS OBSERVED: the LM ended by the ftol rule after 91 iterations at a terminal cost_after_reweight 5.408e-9 = 0.087 of the start's, after two unsafeguarded
    lagged-iteration excursions (peaks 4.3e-5 at iteration 15 and 2.7e-5 at 65, the mechanism of item 48, with the safeguarded refresh off) that returned. The end state has the
    lowest holdout rho_u^max of the campaign, 0.02983 / 0.03130 (0.659 / 0.702 of its start; 0.679 / 0.719 of nest8 (0.45, 1) p0; 0.711 / 0.755 of nest10 (0.45, 1); 2.98x / 3.13x
    the Tier S bound), the closure met (carried mismatch 2.7e-8, K_E and K_H ratios 1.000) with the finite-radius kappa converging to the required value at the predicted rate
    (+0.672 / +0.892 / +0.967 at 2^12 / 2^14 / 2^16 R0, deviation ratios 0.329 / 0.303 against 0.340), E_ren -1.071 (the smallest |E_ren| of any unpinned state of the branch,
    still order one), H_tot/int|h| -0.599, Q_sw 0.407, tau_F 0.427 (0.754 of the start), e_F 0.164 (doubled), rotation content 0.88, guards passing. At the same time the core
    amplitude terms doubled: core-set a_max 1.206 (1.97x the start, 2.0x nest10 and nest8 p0, 1.44x nest8nk8), core-set sigma_u^max 0.506 (+10 to +19 per cent), max|U| 1.72 (+36
    per cent) and max|Omega| 19.6 (+48 per cent) in the fixed dilation gauge, while the unnormalized training momentum RMS fell only 7 per cent (0.0857) against the 34 per cent fall
    of the normalized holdout. READING: under SPEC 7.3b the state is NOT ORDERED against any state of the branch (the holdout is lower in every pair, the core ratios exceed the 10
    per cent allowance by a factor of up to two): the 'shell gain with a core loss' pattern of nest8nk8, twice as strong. Under the registered degree-8 closure rule it reads (a')
    'far closure compatible with the floor at degree 8', and it lies 30 per cent below that floor. MECHANISM READING: with the closure rows at weight 1 and the correction channels
    at SPEC degrees, the LM lowered the normalized shell residual by moving amplitude into the core (max|Omega| +48 per cent) while keeping the tail closed; whether this is a
    different state of the same branch or a point on a slow descent is not established (terminal ftol plateau after an excursion; the damping rose from 4e-5 to 7e-3 over the
    last five accepted steps). WHAT IT DOES NOT SHOW: a candidate (2.98x the Tier S bound; balances order one; not ordered); stationarity (ftol plateau; V10 0.44 reflects the return
    from the excursion inside the last tenth); anything at degree 10 (no continuation exists). The natural next tests, the lead's call: a same-budget continuation with the
    safeguarded refresh read against an unchanged control, and the running (0.45, 0.3) sibling under the same rule. Primary-reported, unvalidated.

## 2026-10-26T18:21Z (shift 10), new items
52. (2026-10-26T18:21Z) Degree-8 closure-met rung at (0.45, 0.3), omega/c_l = 2/3 (nest8_L8_cl0.45_om+0.3_fixed_cl1; lead BV/CR, read under HS 4 (c)): the S11 weight-1 closure state
    s11_L6_cl0.45_om+0.3_fixed_cl1 (holdout 0.05227 / 0.05368, an unsafeguarded end state whose gain depended on the excursion path) embedded at L8 (Nk 20, channels 4/4/4 at 19/18/8,
    closure rows at weight 1) ran 123 iterations to an ftol plateau through two unsafeguarded lagged-iteration excursions (peaks 1.4e-5 and 2.8e-5 against 1.27e-8 at the start) that
    returned to 7.81e-9 = 0.62x the start's cost. END STATE holdout 0.03739 / 0.03940 (0.715 / 0.734 of the start; 0.61 / 0.65 of nest8 (0.45, 0.3) p0; 0.66 / 0.70 of nest10 (0.45, 0.3)),
    rms_mom 0.09224 (-5.6 per cent), core-set a_max 1.435 (1.21x the start, 1.28 to 1.39x the nest states), max|U| +17, max|Omega| +39 per cent, e_core / e_F 0.23 / 0.24 (+21 per cent),
    closure met (m 1.1e-7, K_E and K_H ratios 1.000), kappa finite radius 1.21 / 1.07 / 1.02 approaching 1 from above. READING: (a') 'far closure compatible with the floor at degree 8',
    39 per cent below it; NOT ORDERED under SPEC 7.3b against any state of the branch (the holdout lower in every pair, the core-set a_max ratio 1.21 to 1.39 above the 10 per cent
    allowance): the 'shell gain with a core loss' pattern of the (0.45, 1) sibling (item 51), on both branches. MECHANISM READING: as in 51, the LM with closure rows at weight 1 lowers the
    normalized shell residual by concentrating amplitude in the core while keeping the tail closed. WHAT IT DOES NOT SHOW: a candidate (3.7x the Tier S bound, E_ren -1.04); stationarity;
    ordering. HS 4 (c): the core-set a_max rose more than 10 per cent, so no continuation. Primary-reported, unvalidated (verifier audit requested).
53. (2026-10-26T18:21Z) Robustness group (i) R0 re-expansion FAILED (s5r0_L6_cl0.45_om+1.0_fixed_R0p6 and R0p15; registration reports/STAGE2_ROBUSTNESS_REGISTRATION_20261026.md): both
    re-solves stopped by xtol after ONE accepted step (12 and 11 s); at R0 0.6 the step raised max|U| from 1.23 to 15.25 (holdout 0.8875), at R0 0.15 it moved the state (rms_mom 0.0935
    to 0.2045, a_max 3.38). MECHANISM (CPU, scripts/block_costs.py and fix_reexpanded_start.py): the least-squares re-expansion with all channels (condition numbers 1e25 to 1e26,
    rcond 1e-12 after column scaling) represents the parent velocity as a catastrophically cancelling combination (A/C coefficient norms 6.6e5 / 1.8e6 against the control's 64 / 3.4;
    B 7.8e6, D 1.4e8, E beyond the double range in norm; zeroing B/D/E changes U by a relative 2.1e6); the closure rows (weight 1e-3) see a carried mismatch m 3049 and cost 0.37 against
    a PDE cost 4.5e-8, and the LM's first step follows them. REMEDY (lead d128 HX / HY / HZ / IA): regularized A/C-only refits (channels 0,0,0, rcond 1e-6: condition 8.5e3, full rank,
    fit error 2.0e-2 to 3.6e-2 intrinsic to the twist-radius change, B/D/E zero by construction, phase-aligned by an exact rotation) as the warm starts of four L6 variants at the
    controls' budget; the L8 pair is recorded as 'R0 re-expansion failed at L8; sensitivity to R0 not tested'. Lesson for every fitted or re-expanded start: check the block costs and
    the coefficient norms on the CPU before a GPU launch. Not a reading of R0 sensitivity.
54. (2026-10-26T18:21Z) Safeguarded diagnostic continuation nest8_L8_cl0.45_om+1.0_fixed_cl1_sgcont150 (lead HS 4 (a)) INVALID as a continuation: a pivot change at the start under a frozen
    closure target. The worker's choose_pivot selected the pair (S, q 8, amplitude 0.1437) where the parent's saved pivot was (S, q 5, amplitude 0.1336); the LM's exact phase projection
    at its first step rotated the state by a finite angle (relative coefficient change 1.44; the PDE cost invariant at 5.4079e-9) while the closure target G_required, frozen at the
    unrotated Z0 by the safeguard, was not rotated: the closure rows at weight 1 cost 3.41e-2 at the LM's first evaluation (merit at Z0 5.4079e-9; with the target refreshed at the
    rotated state the non-PDE block is 2.9e-17, m 2.7e-8). The first block lowered the artificial cost (5.38e-5 at it 0, 2.24e-7 at it 4), the boundary refresh exposed the mismatch
    (merit 3.21e-2) and the safeguard backtracked to Z0; every later trial step was rotated again and rejected (damping to 2.7e10). The end state is the parent (compare_fields to
    confirm). It is NOT a reading of the parent's plateau. In the standard mode the same pivot change gives one first step against a stale target (a transient kick at the start of any
    continuation whose largest m != 0 tail pair changed); the controls and variants of this shift were checked (the St-B control's projection is the identity). REMEDY: pre-align the
    parent to the pivot the worker will choose (scripts/phase_align_start.py, an exact symmetry, angle recorded) before any continuation; a re-run of the safeguarded continuation from
    the pre-aligned parent is proposed to the lead (1.9 GPU-h).
    ADDENDUM to 54 (2026-10-26T19:57Z): the re-run nest8_L8_cl0.45_om+1.0_fixed_cl1_sgcont150b from the pre-aligned parent (Z0 consistency met: cost0 = the posted aligned total 5.407931496e-9) found NO
    accepted step from the aligned start (stalled at iteration 0, damping above lam_max 1e10, |g| 4.04e-9); LM endpoint = Z0, battery state = Z0/||F|| (gauge defects 0 before and after the exact
    projection; compare_fields aligned parent -> end 6e-16). Reading: under the self-consistent objective at Z0 the LM finds no decreasing step, in agreement with the parent's ftol stop at the same
    point; an optimizer reading, not a stationarity statement. The parent's gain to 0.02983 passed through the unsafeguarded lagged-target path. GPU: 3717 s (1.03 GPU-h) plus the invalid run's 3718 s.

## 2026-10-28T06:20:39Z (shift 16), new item
55. (2026-10-28T06:20:39Z) The fourth compare_fields reader of the lead's R4-6 reading chain v2 (rebound start r4_nest10_1e-2_s31010_rebound.pt 19453fae -> perturbed end state 4893496b, pid 3050943, launched by the chain at 01:44:22Z Oct 28) DID NOT FINISH: 15787 s wall and 31290 s CPU (read at 06:07:29Z) against 527 s, 533 s and 535 s wall for the chain's first three compare_fields runs (end distance, start distance, control drift; the same tool 976ae378, the same thread settings OMP 3 / MKL 3, 5 tasks; all three before the operator's pin of the lane to CPUs 0,2 at 01:46:32Z). Its stdout file stayed empty (block-buffered) and no JSON was written. It was signalled under lead order RR-7 (d128 UA 05:28:00Z: one SIGTERM at 06:00:01Z, caught by the SIGTERM handler that scripts/worker.py lines 33 to 38 install at import and that compare_fields.py line 189 brings in by executing worker.py as a module; the handler only sets a STOP flag that compare_fields never reads) and stopped under RR-7a (d128 UE 06:05:16Z: one SIGKILL at 06:07:30Z; chain rc 137; R4_READING_CHAIN_DONE 06:07:30Z). CAUSE OPEN: the two-core pin alone does not explain a CPU time 9.8 times the most any of the first three could have used (the lead's UA reading); the alignment search refines up to three coarse minima by golden section (compare_fields.py --basins 3), which bounds the evaluation count at about 199 against about 115 for one refined minimum, a factor 1.7, not 10; no separating measurement exists (no profile of the process was taken; a py-spy attempt is an incident under the lead's rules). CONSEQUENCE: the perturbed drift of the R4 pair is NOT COMPUTED; the R4-6 class (i) stands on the two holdouts and the end distance (lead UF: ACCEPTED as a primary-reported late result with the chain end 06:07:30Z); no rerun (RR-2). A reading tool that must finish under a core limit should set its thread count from the limit and write progress lines unbuffered; recorded here, not changed (rule AU, no tool edits at the end of the campaign).
