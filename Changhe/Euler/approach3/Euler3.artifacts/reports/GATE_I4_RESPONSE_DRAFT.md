# Gate I.4 response of the numerics lane (FINAL 2026-10-25T18:30Z; drafts 2026-10-25T06:05Z, 10:21Z, 16:30Z; due 20:00Z, gate 23:09Z)

## Summary (numerics lane, 2026-10-25T18:30Z, final)
- G1 PARTIAL on the primary record (strict T05 at 1.35e-12 against 1e-12 on the GPU; 6.0e-13 on the CPU; threshold not lowered); clean suite run 8 on the CPU
  (2026-10-25T17:27Z): 24 PASS of 24, incl. the new split-accumulation test. G3 PASS for rows after 2026-10-24T19:39Z. G4 PASS in form (shortlist of 17:08Z: 581
  ranked states, 214 branches, both shell families, the 7.3b relations, the v1.21 core sets, the global balances and the far coefficients for every representative).
- Stage I candidate: NONE. The lowest primary holdout is nest8 (0.45, 1) p0 cont150 at rho_u^max 0.0437 std / 0.0433 half (4.4x the Tier S bound; independent
  reader of the parent export 0.04393 / 0.04352), with a balanced core (sigma_u^max 0.42, sigma_Om 0.42, a_max 0.50, strain ratio 0.985 at the located |Omega|
  maximum, core resolved) but both global balances failed at order one (E_ren -1.58, H_tot/int|h| -0.70) and a wrong-signed first far correction (K_E ratio -4.9,
  carried mismatch 0.067, K_H ratio +1.05). Every low-residual state of every branch shares this pattern (E_ren -1 to -4, H_tot/int|h| -0.70 to -0.88, K_E
  ratio off by factors 3 to 33 or wrong-signed): the far closure and the global balances are the open structural items, not the shell residual alone.
- Four structurally different branches are kept: (i) the D6 lineage (d6w_L8 0.0442 / 0.0543; unbalanced core sigma_u 1.8-2.1; floored in both resolution
  directions: L8 step worse, Nk 32 within 4 per cent); (ii)-(iv) the balanced-core nest rungs at (0.45, 1) (0.0437 / 0.0433 at L8), (0.45, 0.3) (0.0597 / 0.0594
  at L8) and (0.42, 0.3) (0.0622 / 0.0675 at L8), all with sampled Q_sw below 1 (0.63, 0.37, 0.53); plus the from-scratch floor states (0.25-0.5) as the control.
- R2 status per nest branch: one recorded step with q > 0.85 each ((0.45, 1) q 0.955, continuation -0.6 per cent; (0.45, 0.3) q 0.916, continuation -2.6 per
  cent; (0.42, 0.3) q 0.970 / 0.942, continuation queued). The L8 -> L10 step decides: both c_l = 0.45 branches are running at L10 with SPEC-degree channels
  (nest10 p0 runs since 17:04Z and 17:30Z, about 21 h of LM each) under the split-column J^T J accumulation validated this shift; the radial direction is closed
  at L6 (Nk 16 -> 32 within 4 per cent on both the D6 and the nest branch); the channel radial direction (Nk 4 -> 8 at L8) is running (the 3-iteration smoke moved
  the far coefficients, not the holdout).
- Resource use to 17:08Z (daily report): 879 starts, 191 jobs, 96 GPU-slot hours of completed jobs on four GPUs plus the running exclusive jobs; lane 1.1 GB of disk;
  foreign torchlean processes hold 0.5-1.6 GB on each of our GPUs (counted as 3 GB per GPU in every placement).
- Recommendation for Stage II: as in the lead's plan and the per-GPU placement below (S1 L10 on both c_l = 0.45 branches with SPEC channels and jtj_blocks 2;
  the Nk-8 channel test; the (0.42, 0.3) continuation; S10/S11/S12 at L6 from the registered lines; S9d chains from the S11 weight-1 end states; S4 omega and
  c_l paths and the all-m class at the lead's registration; the s1g/s1l/s1m L10 multistarts only if the lead keeps them). Exact lines: reports/STAGE2_QUEUE_PREP.md.

## Sections below: historical, superseded by the Summary above and the sections written on 2026-10-25 after 16:30Z (lead 18:52Z item (c))
The G1/G3/G4 sections and the branch sections were written between 06:05Z and 12:57Z and keep their original numbers (e.g. the shortlist of 12:57Z with 575 ranked states
and 12 of 66 ordered pairs); the current figures are those of the Summary (shortlist 17:08Z: 581 ranked states, 214 branches; clean suite run 8: 24 PASS of 24) and of
reports/STAGE1_SHORTLIST.md, reports/G1_TESTS.md, reports/RESOLUTION_LADDER.md as regenerated at 17:08Z and 17:35Z.

## G1 tests (reports/G1_TESTS.md, regenerated from the newest clean-process suite log)
- Clean suite run 5 (2026-10-25T08:54Z, 22 outcomes incl. the S9b guard tests and the T12 positive-pivot assertion of SPEC v1.23): 21 PASS, the strict
  T05 FAIL at 1.35e-12 recorded. A 23rd test (tests/test_far_helicity.py, SPEC v1.24 7.8: identity closure 3e-14, two carried forms 3e-14, negative
  control 0.4-0.8, values equal to the independent route's four confirmed rows to 1e-12 relative) PASSED 2026-10-25T10:20Z and is in run_tests.sh; the
  next clean suite run includes it. Clean suite runs 6 (11:08Z) and 7 (13:04Z) on the CPU: 23 and 24 PASS of 23 and 24 (run 7 adds tests/test_S12_radial_rows.py);
  on the CPU the strict T05 value is 6.0e-13 (PASS), on the GPU 1.35e-12 (FAIL): the GPU value stays the record (G1 PARTIAL), reports/G1_TESTS.md carries the device note.
- T01-T04, T06-T10, T12 PASS on the primary record; T05 diagnostics at the strict SPEC value 1e-12 FAIL at 1.35e-12 (the ratios with the
  nonlinear denominator; roundoff amplification RMS T1 / RMS(T4 + T5) printed beside the result; field covariance 7.6e-16; threshold not
  lowered); T11 ten post-resume iterates PASS at 8.7e-11 (SPEC 1e-10) at the API level of the worker's checkpoint state (worker-level kill -9
  test compares final states bitwise); T12 pivot phase exact and soft F-gauge defect 6.3e-7 after every accepted step on a saved state, pivot
  switch invariance 2e-14. New since the 03:39Z table: T08 tau_1, tau_2 (degree-4 Taylor fit), T10 as the holdout factor-3 rule (0 of 365 ranked
  rows flagged), the AD-Jacobian tests as a supplementary row. The independent route's scope audit (verifier 05:40Z) is accepted: G1 is PARTIAL
  because of the strict T05 value; nothing else is open on the primary side.
## G3 reproducibility (reports/G3_LEDGER.md)
- Rows after 2026-10-24T19:39Z carry seed, solver version, holdout vector or failure reason; earlier rows are marked missing and are excluded
  from every ranked claim; the shortlist's 'reproducible' column is 'yes' for all 12 representatives. The verifier's provenance counts (540 finite
  experiments; 282 random, 158 affine, 100 continuations; T10 443 within factor 3 / 24 FLAG / 73 without holdout on their count) are theirs.
## G4 shortlist (HISTORICAL 12:57Z figures; current: 17:08Z, 581 states, 214 branches) (reports/STAGE1_SHORTLIST.md; regenerated 2026-10-25T12:57Z: 575 ranked states, 214 branch bins with the lineage in the key; rank 1 nest8 (0.45, 1) p0 0.0439 / 0.0435, rank 2 d6w_L8 0.0442 / 0.0543, rank 6 nest8 (0.45, 0.3) p0, rank 9 nest6 (0.42, 0.3) p0; every representative carries the balance and far-coefficient columns)
- 12 branch representatives with the 7.3 key, both shell families, the single-term ratios, a_max, rho_sp, V10, the structure block, Q_sw,
  e_core, tau_0/1/2, a_eff and the v1.21 ball sets, E_ren / max E_F / H_tot / H_tot over int|h| / core alignment, GPU hours, reproducibility;
  pairwise 7.3b table (12 of 66 pairs ordered with the v1.21 sets); branch grouping with GPU hours per branch. Four structurally different
  branches: (i) D6-lineage descendants (best rho_u^max 0.0442 / 0.0543 d6w_L8; sigma_u^max 1.8-2.1; Q_sw 0.15-0.44); (ii) nest ladder
  (0.45, 0.3): nest6 p0 0.0669 / 0.0675 with sigma_u 0.44, a_max 0.68, tau_F 0.56, Q_sw 0.50 (L8 rung queued); (iii) nest ladder (0.45, 1) and
  (0.42, 0.3): balanced cores but Q_sw 2.0-2.6 (swirl not eddy-generated); (iv) from-scratch L6 floor states (0.25-0.5). No state near Tier S.
## The leading state of the nest ladder (lead 07:26Z item 7; values 2026-10-25T08:00Z, primary, unvalidated)
- nest6 (0.45, 1) p0 (c_l 0.45, omega 1, omega/c_l 20/9; L6 Nk16, SPEC-degree channels B15/D14/E6, closure rows 1e-3, 600 iterations): holdout
  rho_u^max 0.0460 std / 0.0463 half; sigma_u^max 0.432 / 0.400 (0.446 on the v1.21 half ball); sigma_Om 0.41; a_max 0.433 / 0.419 (0.558 ball,
  centre weight); rho_lin 0.176; rho_nl^max 0.97; tau_F 0.583; delta_G core 0.016; Q_sw 0.673; V10 6.1e-2 (not stationary); E_ren -1.543; H_tot
  -4.535, H_tot/int|h| -0.711; core alignment -0.952; max E_F 1.00005 at r 38; K_carried/K_required -32.63 (verifier -32.63); kappa finite-radius
  -32.6 at 2^14 R0; tau_0/1/2 2.9e-3 / 3.6e-2 / 0.15; a_eff 0.270, core RESOLVED. p1 (ftol, 111 iterations): 0.0516 / 0.0512, sigma_u 0.45,
  a_max 1.27, Q_sw 1.198, K ratio +29.7. Export candidates/nest6_L6_cl0.45_om1.0_p0 (with D2U_grid). Next: nest8 (0.45, 1) p0 (L8 rung, queued
  at priority 15), s1nk Nk 24/32 at L6, S9b lambda = 1. Reading: best by the shell ratios, but both global balances fail at order one and the
  carried far correction has the wrong sign; not near a profile.

## Far-coefficient diagnostics (SPEC v1.24 7.8; lead d78/d84, 2026-10-25T10:21Z, updated 10:53Z; reports/FAR_COEFFICIENTS.md; primary values; ten of sixteen rows confirmed by the independent route to 4e-12, incl. both L8 states)
- Every low-residual state fails the first far-field coefficients at order one: energy ratio K_E(carried)/K_E(required) -32.6 (nest6 (0.45, 1) p0), +29.7
  (p1), -8.98 / +19.1 (nest6 (0.45, 0.3) p0 / p1), +5.38 (nest6 (0.42, 0.3) p0), -3.25 (d6w3_L6), -15.2 (d6w_L6), -434 (d6w_L8, channels B19/D18), -2835
  (d6t_L8), 0 for the states without B/D channels (nest4, d6t_L6, S9b); helicity ratio K_H(carried)/K_H(required) +1.26, +1.21, +4.24, +2.19, +1.32, +1.07,
  +0.18, +1.60, +1.39 (same order), 0 without channels. The helicity ratios have the exact-profile sign and three lie within 0.27 of 1, but the energy ratio of the same states is off by factors 3
  to 33 with four wrong signs: the two scalars are different projections of the vector defect G_carried - G_required, whose relative norm m is 0.22
  (d6w3_L6) to 4.3 (d6w_L8); 42 to 67 per cent of the squared defect lies along F and the rest is an angular-shape error of the same radial order
  (lead 10:12Z after the verifier's 10:01Z correction). Reading: no state carries the first nonlinear far correction; the far field of every state is a
  leading tail plus a wrong correction, so the far closure is open on every branch (a Stage II item for closure rows with the full vector, the F-component
  and the orthogonal norm recorded separately).

## The nest ladder at c_l 0.42 (2026-10-25T10:44Z; primary, unvalidated)
- nest6 (0.42, 0.3) p0 (omega/c_l 5/7; L6 Nk16, SPEC-degree channels B15/D14/E6, closure rows 1e-3, 600 iterations, 1.9 GPU-h): holdout rho_u^max 0.0641 std /
  0.0716 half; rho_nl^max 1.18; sigma_u^max 0.50 (0.66 half ball); sigma_Om 0.47; a_max 0.59 / 0.62 (0.90 ball centre); rho_lin 0.27; Q_sw 0.723 (2.63 at L4);
  tau_F 0.679; delta_G core 0.009; core RESOLVED (a_eff 0.27); strain ratio 0.72; E_ren -3.90; H_tot/int|h| -0.789; core alignment -0.987; max E_F 1.00007;
  K_E ratio +5.38, carried mismatch 0.35; V10 6.6e-2. The third balanced-core L6 rung with sampled Q_sw below 1 (with nest6 (0.45, 0.3) p0/p1 and (0.45, 1) p0; a sampled value has no one-sided bound); it
  fails the global balances and the far closure like every other state. R1 and the 05:21Z rule met: L8 rung enqueued (nest8 (0.42, 0.3) p0, exclusive,
  about 4 GPU-h). Exported with D2U_grid as candidates/nest6_L6_cl0.42_om0.3_p0.

## Smoke jobs for the lead's newly registered arms (S10, S11, S12; 3 LM iterations each on nest6 (0.45, 1) p0; 2026-10-25T12:01Z)
- S11 (closure weight 1): the far closure is enforced at once (m 0.346 -> 2.5e-4, K_E ratio 1.0003, K_H ratio 0.9999) at a holdout cost of 1.24x / 1.16x
  after 3 iterations; balances unchanged (E_ren -1.51); 10 s per iteration, 73 GB at the diagnostics. Usable as registered (R12 after 300 iterations).
- S10 ('both' formulation, weight 1): chunk 512 OOMs at L6-ext on a whole A100 (77.7 GB at the first Jacobian); chunk 128 fits (51 GB, about 20 s per
  iteration, about 1.7 GPU-h per 300 iterations); after 3 iterations the holdout momentum key is 1.36x the start while sigma_Om falls 0.41 -> 0.30 (R11
  after 300 iterations is the question).
- S12 (radial-lambda rows, w = 3): implemented and tested (sum identity exact, Jacobian 4e-10; d93 share 0.740 reproduced on the training grid); 3 iterations
  lower the share to 0.485 at a holdout cost of 1.05x / 1.10x with E_ren -1.54 -> -1.38; no measurable cost per iteration (R13 after 300 iterations).

## The L8 rung at (0.45, 1) (nest8 (0.45, 1) p0, DONE 12:50Z; primary, unvalidated; 4.3 GPU-h exclusive): the campaign's lowest holdout
- holdout rho_u^max 0.0439 std / 0.0435 half against 0.0460 / 0.0463 at L6 (q 0.955 / 0.94) and 0.0442 / 0.0543 for d6w_L8; rho_nl^max 1.12; sigma_u^max 0.42 /
  0.38 (0.43 core half ball), sigma_Om 0.42, a_max 0.49 / 0.45 (0.58 ball centre); core RESOLVED; strain ratio 0.987 at the located maximum; tau_F 0.5675;
  sampled Q_sw 0.647; carried mismatch 0.069 (L6 0.35), K_E ratio -5.2 (L6 -32.6), K_H ratio +1.054 (L6 +1.26); E_ren -1.59, H_tot/int|h| -0.700; V10 8e-3. Under SPEC 7.3b it is
  ordered ahead of d6w_L8 (lower on both families, single-term ratios four to five times smaller): the first nest state ordered over the D6 lineage's best.
  Still 4.4x the Tier S bound; balances unchanged at order one; far correction wrong-signed. R1 holds; R2 first step with q > 0.85 at the iteration limit
  Continuation (cont150, DONE 14:42Z, ftol after 83 iterations): holdout 0.0437 / 0.0433 (0.6 per cent lower), everything else unchanged (sigma_u 0.42, a_max
  0.50, m 0.067, K_E -4.9, K_H +1.05, E_ren -1.58, H ratio -0.700): under the lead's 12:54Z rule the L6 -> L8 step stands as recorded (q 0.955 at the first R2
  threshold crossing); the channel-Nk 4 -> 8 test (smoke running) is the remaining check before L10. Radial refinement at fixed L6 (s1nk Nk24, DONE 14:43Z):
  0.0451 / 0.0445 (2-4 per cent lower than Nk 16; m 0.045, K_E -2.2). The branch is within 5 per cent of 0.044 in both resolution directions. Exported as
  candidates/nest8_L8_cl0.45_om1.0_p0 and ..._p0_cont150 (no D2U_grid at L_ext 19) with v1.24 supplements.

## The L8 rung at (0.45, 0.3) (nest8 (0.45, 0.3) p0, DONE 12:22Z; primary, unvalidated; 3.9 GPU-h exclusive)
- holdout rho_u^max 0.0613 std / 0.0609 half against 0.0669 / 0.0675 at L6 (q 0.92 / 0.90: the first S1 step above the R2 threshold 0.85 on this branch);
  rho_nl^max 2.7 (far shells); sigma_u^max 0.41 / 0.39 (0.58 core half ball), sigma_Om 0.42, a_max 0.74 / 0.73 (0.95 ball centre); core RESOLVED (a_eff 0.30);
  tau_F 0.557; sampled Q_sw 0.390; carried mismatch 0.049 (L6 0.40), K_E ratio -0.28 (L6 -9.0); E_ren -1.77, H_tot/int|h| -0.879, core alignment -0.97;
  K_H ratio +1.28 (required -0.035: small at this omega); V10 9e-3. Continuation (cont150, DONE 14:48Z, 150 more iterations): holdout 0.0597 / 0.0594 (2.6 per
  cent lower), sigma_u 0.41, a_max 0.74, m 0.047, K_E -0.22, K_H +1.26, E_ren -1.74, H ratio -0.877, V10 5e-3: under the lead's 12:54Z rule the L6 -> L8 step
  (q 0.916) stands as recorded. R1 for a further level holds (core-resolved, holdout <= 0.1); the lead reads R1/R2 at the gate. Exported as
  candidates/nest8_L8_cl0.45_om0.3_p0 and ..._p0_cont150 (no D2U_grid at L_ext 19). nest8 (0.45, 1) p0's battery and the
  nest8 (0.42, 0.3) p0 run (started 12:25Z) follow.

## The L8 rung at (0.42, 0.3) (nest8 (0.42, 0.3) p0, DONE 16:15Z; primary, unvalidated; 3.4 GPU-h LM + 22 min battery; lead's reading entered 16:2xZ)
- holdout rho_u^max 0.0622 std / 0.0675 half against 0.0641 / 0.0716 at L6 (q 0.970 / 0.942: the first R2 step above 0.85 on this branch; 300 iterations, max_iter,
  V10 5.8e-3 not GN-stationary, cost still falling 0.6 per cent over the last 30 iterations); rho_nl^max 1.12 / 1.26 (single sphere 1.30 at r 6.8); rho_lin 0.24;
  sigma_u^max 0.499 / 0.464 (core half ball 0.68, quarter 0.62), sigma_Om 0.465, a_max 0.646 / 0.661 (ball centre 1.02, upper 1.46); core RESOLVED (a_eff 0.262,
  max doubling change 7.6e-6); |Omega| max 12.31 at r 0.324, strain ratio 0.756; tau_F 0.6665; sampled Q_sw 0.530 (L6 0.723); delta_G core 0.010; G closure
  distance 1.2e-14 at degree 19/18; carried mismatch 0.210 (L6 0.349), K_E ratio +3.88 (L6 +5.38), K_H ratio +1.2135; E_ren -3.940, H_tot/int|h| -0.7875, core
  alignment -0.985, max E_F 1.00000; kappa 4.87 / 4.73 / 4.13; radial-lambda share 0.800; f_sw 0.703; SPECTRUM A 4.0e-2, C 9.5e-3, B 0.18, D 0.19, E 0.70;
  tau_0/1/2 2.1e-3 / 4.2e-2 / 0.42. Reading: 3-6 per cent lower holdout, far closure and sampled Q_sw improved, both global balances unchanged at order one;
  6x the Tier S bound. Under the R2 continuation rule the factor is read after the bounded continuation (nest8_L8_cl0.42_om+0.3_fixed_p0_cont150, 150
  iterations, priority 14, approved; after the L8 validations and the L10 smokes, ahead of the s1g/s1l/s1m sweeps, not ahead of the c_l 0.45 L10 runs).
  Exported (CPU, no D2U_grid): candidates/nest8_L8_cl0.42_om0.3_p0 with the v1.24 supplement (K_E ratio 3.8759; K_H required -0.7886, carried -0.9570,
  ratio 1.2135; identity closure 3.0e-15).

## L10 memory and the solver change (lead 14:54Z item 2, 15:53Z items 1-2; accepted 16:26Z)
- Dense Jacobian at L10 Nk24 with SPEC-degree channels B23/D22/E10: 1 287 900 rows x 4515 unknowns (after the tail constraints) x 8 B = 43.3 GiB beside the
  21 GB model and pressure tables. The smoke nest10smoke (0.45, 1) failed three times: attempts 1-2 in the torch.cat of the column chunks (a second copy of J:
  'Tried to allocate 43.50 GiB' with 44.82 GiB held; sampler peak 78.4 GB), attempt 3 (preallocated J) at the SECOND Jacobian allocation after completing one LM
  iteration at 160.5 s per Jacobian (chunk 64; 80.6 GB observed), because lm_solve kept the previous J bound through the trial evaluations into the next build.
  So every dense job held two Jacobians at its peak (the 75 GB of the L8-ext jobs were 2 x 17 GB plus the model and the chunk-128 intermediates). Fix saved
  16:16:57Z (lm.py sha256 ae98e4520350): J is released right after J^T J, J^T r and the Marquardt scaling are formed; val8dense at L8 (chunk 128) then peaks at
  50.4 GB. The remaining SPEC-channel retries were cancelled (worker cancel marker queue/cancel/<job_id>; ledger job_cancelled; job file in queue/cancelled).
- Split-column J^T J accumulation (lm_solve(jtj_blocks=k); src/optimization/lm.py jtj_split): the Jacobian is never stored whole; column block i (N/k columns)
  is built and kept while the blocks j > i are rebuilt chunk by chunk for the off-diagonal blocks of J^T J; J^T r accumulated the same way; scalar rows
  (Sigma_Z, S9 balance rows) by reverse-mode gradients as before; not combinable with the finite-difference parameter columns (free c_l, omega: k = 1).
  Same normal equations as the dense LM (no extra squaring), so the step, damping and acceptance are unchanged; memory J/k, time (k+1)/2 Jacobian builds.
  Unit test tests/test_lm.py test_jtj_split (CPU): J^T J and J^T r for 1/2/3/5 blocks with a non-aligned chunk equal to the dense values (difference 0),
  with scalar rows 2e-16; first LM step identical; recovery run identical to the dense one (7 iterations to 1.2e-29).
- L8 validation at the lead's registered thresholds (val8dense and val8split, LM-only worker mode, 2 LM iterations from the cont150 (0.45, 1) state at L8 Nk20,
  B19/D18/E8, closure rows 1e-3, chunk 128, GPUs 1 and 0, 16:15-16:23Z): two-step displacement difference |z_split - z_dense| / |z_dense - z_parent| =
  4.6e-11 (threshold 1e-6); per-iteration costs 2.130796921e-08 and 2.130752099e-08 in both runs (2e-15 relative); cost decreases from the start cost
  2.1307990e-08 (9.9736e-7 and 2.20327e-5) agree to 1.9e-9 and 1.6e-10 relative (threshold 1 per cent); Jacobian time 40.0 / 39.0 s dense against 56.8 / 58.2 s
  split (1.44x); peak GPU memory 50.4 GB against 27.3 GB. PASS; the split path is cleared for L10 (lead 16:26Z). scripts/compare_lm_only.py.
- Code versions per job: since 16:20:40Z every worker logs at START the sha256 (first 12 hex digits) and mtime of lm.py, worker.py, problem.py and fields.py
  (worker.log CODE VERSIONS; ledger job_code_versions; start_result and lm_only_result records carry code_versions and jtj_blocks). Table for the L10 attempts
  (lm.py imported): attempt 1 (launched 15:39:42Z) and attempt 2 (15:50:32Z): the version before 15:53Z (torch.cat of the chunks); attempt 3 (16:01:24Z): the
  15:53Z version (preallocated J, previous J kept alive); ch19 attempt 1 (16:14:18Z, killed by hand at 16:17Z before its first Jacobian): the 16:07Z version
  (split accumulation added, J kept alive); every launch from 16:21:05Z on (ch19 retry 1, jtj2, dense2, the validations' successors): ae98e4520350 (16:16:57Z).
  The validation pair itself: val8dense (16:15:19Z) imported the 16:07Z version (dense path unchanged by the J release), val8split (16:17:21Z) ae98e4520350;
  their steps agree to 4.6e-11, which also shows the J release changes no value.
- L10 smokes (3 iterations each from the cont150 (0.45, 1) state 0.0437 / 0.0433, chunk 64, exclusive, lm.py ae98e4520350; a smoke is not an R2 reading):
  ch19 (channels 19/18/8, dense with the J release, GPU 1 16:21-17:30Z; 4556 -> 3937 unknowns, 931 500 rows): 94.9 s per Jacobian, LM peak 50.8 GB, battery 60 min,
  allocated peak of the whole job 52.6 GB (ledger job_end; nvidia-smi showed 80.4 GB because the caching allocator keeps freed blocks reserved, plus about 1 GB of
  foreign torchlean use); holdout 0.04362 std / 0.04323 half, rho_nl^max 1.135 / 1.130, sigma_u^max 0.418 / 0.372, sigma_Om 0.421, a_max 0.496 / 0.447, strain ratio
  0.990 at the located maximum, tau_F 0.5702, sampled Q_sw 0.628, G closure distance 6.8e-8 at degree 19/18 (379 columns; a weak test here: an L8 state embedded at
  L10 has essentially no l = 9, 10 tail content after 3 iterations, so the registered closure reading becomes informative only once an L10 run develops it), carried
  mismatch 0.0666, K_E ratio -4.89, K_H as logged, E_ren -1.5827, H_tot/int|h| -0.7000, SPECTRUM A 2.3e-3, C 3.4e-3 (Nk 24).
  jtj2 (SPEC channels B23/D22/E10, jtj_blocks 2, GPU 0 16:24-18:27Z; 5300 -> 4515 unknowns, 1 287 900 rows): model build 8.7 min (21.8 GB); 234.5 s per iteration
  (3 iterations 757 s; dense attempt 3: 160.5 s; ratio 1.46 against the nominal 1.5); first-iteration cost 1.804870e-08 and lam 1.2e+01 identical to the dense
  attempt; LM peak 61.3 GB (nvidia-smi); battery 101 min (box load average 75 from other users' nice-10 builds; our nice-19 battery items are CPU-bound);
  ALLOCATED PEAK of the whole job 73.4 GB (ledger job_end, torch max_memory_allocated), i.e. the SPEC-grid L10 battery allocates about 12 GB more than the LM
  and 21 GB more than the ch19 battery (52.6 GB): with 3 GB of foreign use the margin on an 80 GB device is about 3.5 GB. After 3 iterations: holdout 0.04358 std /
  0.04316 half (start 0.0437 / 0.0433), rho_nl^max 1.135 / 1.130, sigma_u^max 0.417 / 0.373, sigma_Om 0.420, a_max 0.496 / 0.447, strain ratio 0.9935, tau_F 0.5638,
  sampled Q_sw 0.654, G closure distance 6.7e-14 at degree 23/22 (545 columns, rank 545; SPEC-degree closure, so the registered reduced-channel caveat does not
  apply), carried mismatch 0.0663, K_E ratio -4.84, kappa -5.8 / -5.1 / -4.9, E_ren -1.5826, H_tot/int|h| -0.7000, core RESOLVED (a_eff 0.266), SPECTRUM A 3.8e-3,
  C 5.3e-3 (Nk 24). Reading: the SPEC-channel L10 configuration under the split accumulation runs (memory, time) and reproduces the dense LM; the production runs
  carry it. Battery memory plan for the production runs (their batteries fall on 2026-10-26 about 14:00-16:00Z): every battery item is try/except-wrapped (an OOM
  loses one item, logged 'failed'); a lost holdout item is re-evaluated on the CPU (reevaluate_holdout.py --device cpu, same objective); an OOM coinciding with
  foreign use is an environment failure (lead 17:13Z); the next shift may also add torch.cuda.empty_cache() between items and chunk the heaviest item before the
  batteries run (RESUME_HERE).
  dense2 (SPEC channels, dense with the fix): CANCELLED before launch by the lead (16:4xZ): the dense path needs 21 + 43.5 + about 16 GB at the Jacobian fill, too
  thin a margin for a 13-20 h run once the split path is validated.
- Decision taken under the lead's 16:26Z rule: both L10 production runs use the SPEC-degree channels with jtj_blocks 2 (nest10_L10_cl0.45_om+1.0_fixed_p0 on GPU 5
  since 17:04:37Z, first Jacobian 253.9 s, peak 60.3 GB; nest10_L10_cl0.45_om+0.3_fixed_p0 on GPU 1 since 17:30:29Z), 300 iterations (about 21 h of LM each) plus
  the battery, checkpoint every 14 min (every 4th iteration), resume at the checkpointed iteration; read under the plain R2 rule (q_10 against the cont150
  holdouts). No ch19 production run.
- Nk-8 channel test (lead 17:13Z question: radial resolution or transient?): the embedding Nk 4 -> 8 is exact, so at iteration 0 the far coefficients are the
  cont150 ones (K_E ratio -4.94, carried mismatch 0.067); after 3 LM iterations the carried mismatch is 0.0100, K_E ratio +0.289, K_H ratio 1.0057, while the holdout
  (0.0439 against 0.0437) and the LM cost (2.140e-8) did not move. Reading: at channel Nk 4 the carried correction was representation-limited (the closure rows at
  weight 1e-3 and the PDE rows compete over four radial functions per channel column); +0.29 is a transient of a still-moving quantity; where K_E settles under the
  Nk-8 blocks and whether the holdout moves under the 5 per cent rule at fixed L8 is the reading of the 150-iteration run (nest8nk8, priority 14, about 5 GPU-h;
  its allocated peak before the J release was 78.0 GB for two Jacobians of 30.7 GB, now about 47 GB).

## Radial refinement at fixed L (s1nk Nk 24 / Nk 32; lead 07:14Z item 5; primary, unvalidated; the four runs cost 1.4-2.0 GPU-h each)
- D6 lineage (d6w3_L6 at L6): Nk 16 0.0527 / 0.0695 -> Nk 24 0.0528 / 0.0724 -> Nk 32 0.0508 / 0.0701 (time_limit after 239 iterations); radial Chebyshev tails
  1e-2 -> 3e-4 -> 2e-4; sigma_u^max 1.8, a_max 1.8, sigma_Om 1.3 unchanged; sampled Q_sw 0.188; E_ren -1.06, H_tot/int|h| -0.82; carried mismatch 0.085, K_E ratio -0.53.
- nest (0.45, 1) (nest6 p0 at L6): Nk 16 0.0460 / 0.0463 -> Nk 24 0.0451 / 0.0445 -> Nk 32 0.0451 / 0.0451 (time_limit after 238 iterations); tails 1e-2 -> 5e-3 ->
  4e-3 (A), 8e-4 -> 7e-4 (C); sigma_u^max 0.43, a_max 0.46, sigma_Om 0.42 unchanged; sampled Q_sw 0.673 -> 0.637 -> 0.628; E_ren -1.56, H_tot/int|h| -0.70;
  carried mismatch 0.059, K_E ratio -3.23; V10 1.2e-2.
- Reading: on both branches the radial refinement at fixed L6 moves the holdout by at most 4 per cent on either family while the radial truncation falls by up to
  50x and the core single-term ratios and the global balances do not move: neither L6 floor is radial-resolution-limited under the tested optimizer and budget
  (both Nk 32 runs hit the 2 h limit at about 238 iterations without GN stationarity, so a longer run could still lower them by the per-iteration rate of about
  1 per cent per 50 iterations seen at L8).

## Per-GPU placement for the first 24 h of Stage II (23:09Z Oct 25 to 23:09Z Oct 26; durations measured this shift; the lead may reorder)
- GPU 5: nest10 (0.45, 1) p0 (SPEC channels, jtj_blocks 2) since 17:04Z: LM 300 x about 254 s = 21 h to about 14:15Z Oct 26, battery about 1.5 h, export and far
  supplement on the CPU; then the S11 weight-1 rungs / S9d chain (0.45, 1) or the next S1 decision.
- GPU 1: nest10 (0.45, 0.3) p0 since 17:30Z: LM to about 14:45Z Oct 26, battery to about 16:15Z; then S9d chain (0.45, 0.3) or the lead's S4 path.
- GPU 4 (free about 17:40Z after the s1nk Nk32 (0.45, 1) battery): nest8nk8 Nk-8 150 iterations (150 x 95 s = 4 h plus a 50 min battery, to about 22:40Z); then the
  structural arms s10 both1/both10 (0.45, 1), s11 1e-1 (0.45, 1), s12 (0.45, 1) (about 1.7 + 1.7 + 1 + 1 GPU-h, to about 04:30Z Oct 26); then s11 weight-1 rungs,
  S9d chains (2 GPU-h each), S4 omega/c_l paths at L6 (about 1 GPU-h per point) as the lead registers them.
- GPU 0 (free when the jtj2 battery ends, about 18:00Z): nest8 (0.42, 0.3) cont150 (150 x 37 s = 1.5 h plus a 25 min battery, to about 20:00Z); then s10 both1/both10
  (0.45, 0.3), s11 1e-1 (0.45, 0.3), s12 (0.42, 0.3) (to about 02:00Z Oct 26); then the all-m class arm (S4; smoke first) and the s1g/s1l/s1m L10 multistarts only if
  the lead keeps them (they are not released by the numerics lane).
- Memory accounting per GPU: an exclusive job per GPU; 3 GB of foreign torchlean use counted; L10 LM about 61 GB (split path), batteries 52.6 GB allocated
  at L10 ch19 and 73.4 GB at the L10 SPEC grid (jtj2), L8 dense LM about 50 GB with the J release, L6-ext batteries 70-73 GB (nvidia-smi, reserved). Any OOM that coincides with foreign use is
  recorded as an environment failure (lead 17:13Z); a battery OOM on the holdout item is followed by reevaluate_holdout.py --device cpu (no change of objective).
  Reading rules (lead 15:53Z, 16:26Z): a SPEC-channel L10 run that completes under jtj_blocks 2 is read under the plain R2 rule; a ch19 run keeps the
  reduced-channel reading (q_10 > 0.85 floors the branch only if the closure distance at L10 is at most 0.05 or a SPEC-degree run confirms).

## Stage II feasibility per arm (reports/STAGE2_FEASIBILITY_DRAFT.md; measured costs, one A100, float64)
- S1: 0.7-1.2 GPU-h per 300 iterations at L6 with SPEC-degree channels and closure rows (exclusive, 23-38 GB); 3-5 GPU-h at L8 (33-75 GB,
  exclusive; measured 14:42Z-14:48Z: 37 s per iteration, 150 iterations plus battery about 2 GPU-h); L10 with SPEC-degree channels: the dense Jacobian alone is
  about 52 GB (1.3 M rows x 5000 columns) against 17 GB at L8, so L10 does not fit 80 GB with SPEC-degree channels: the L10 smoke (nest10smoke (0.45, 1), chunk 64, 15:39Z-15:50Z) OOMed in its first dense Jacobian at
  73.9 GB after the model build (21 GB) and no LM iteration completed; reductions that keep the objective are channel degrees 19/18/8 at L10 (J about 36 GB) or a matrix-free
  Gauss-Newton (Stage II implementation). Channel Nk 4 -> 8 at L8: 95-99 s per iteration; the smoke (done 15:39Z, GPU 0) completed its LM and battery without OOM with nvidia-smi showing 75.0 GB on its GPU (about 5 GB margin; chunk 64); the 150-iteration run (about 5 GPU-h) is
  queued at priority 13 and is read by the lead's 5 per cent rule at fixed L. Stationarity (V10) needs 600-900 iterations,
  so three levels for one branch cost about 25-45 GPU-h. Feasible for 2-3 branches, not 5. Recommended branches: D6 lineage (d6w3 at L8:
  running), nest (0.45, 0.3) (nest8 queued), and the independent route's best as a third if the verifier promotes one.
- S2: failure-map probe only (field-norm cond 1.3e3 / 2.5e4 / 3.8e5 at L2 / L4 / L6; GMRES fails beyond L2; damped steps worsen the holdout at
  L4 and L6); about 1 GPU-h per level; a preconditioned attempt at L4 at most 4 GPU-h (not started).
- S3: control only (0.1 GPU-h per S1 product); not contracting from Stage I states.
- S4: 0.1-1.2 GPU-h per 300-iteration L6 arm; a 10-point path per branch 1-12 GPU-h; the all-m basis doubles the unknowns; 30 GPU-h covers
  two branches with one omega path and one c_l path each plus odd-m arms.
- S5: E1 exists (tail constraints, far anchoring, channels, closure rows); R_0 variation 0.1-1 GPU-h per point; E2 (factored compactified
  exterior) needs 1-2 shifts of implementation before any run (not started; the budget line '5 GPU-h plus implementation' is right).
- S7: 0.1-0.15 GPU-h per L6 probe with channels at degree L (9 probes done or queued, about 1.5 GPU-h); f_sw continuation on the D6 lineage
  destroys the state below f_sw 0.8 (0.8 triples rho_u); eddy seeding running. 15 GPU-h is ample (about 100 probes).
- S8: implemented and tested (I1-I4); free-omega iterations cost 4-6x (L4 about 3 s, L6 with channels about 8 s per iteration); the four L4/L6
  prototype runs fit in 2 GPU-h (1 h limit each); 12 GPU-h after the gate covers about 8 L6 runs or 2-3 L8 runs.
- S9: implemented and tested (J1-J4; corrected absolute-helicity exterior term and J4 sign per verifier 05:54Z); the two lambda = 1 runs cost
  about 1.2 GPU-h (d6w3_L6 with closure rows 1 GPU-h; nest4 L4 0.05), lambda = 10 the same: within the 3 GPU-h.
- Diagnostics overhead per finished start: 30-130 s at L6-ext, about 10-15 min at L8-ext (CPU-bound pressure tables); full re-evaluations of
  L6-ext/L8-ext states need 40 GB and a held GPU (scripts/hold_exclusive.sh).
## Budget split check (lead's plan: S1 about 80, S4 30, S7 15, S8 2 + 12, S5 5 + implementation, S2/S3 6; about 150 of 168 GPU-h)
- Consistent with the measured costs above. Two remarks: (1) the S1 80 GPU-h buys three levels for two branches (D6 lineage, nest (0.45, 0.3))
  with 600-900 iterations at L6/L8 and ONE L10-ext level each (10-17 GPU-h), or three branches without L10; (2) exclusive L8/L10 jobs occupy a
  whole GPU, so at most 4 run at once and wall-clock, not GPU-h, limits S1: a 300-iteration L8-ext run is 3-5 h, an L10-ext run 10-17 h.
  Reserve 18 GPU-h is adequate.
## Structural arms started before the gate (status 2026-10-25T08:14Z)
- S7 (9 probes, about 1.5 GPU-h): f_sw continuation on the D6 lineage fails below 0.8 (0.8 triples rho_u; 0.5/0.2/0.0 destroy the state); eddy
  seeding on d6t_L6 to e_core 0.25 lowers Q_sw to 0.10 but triples rho_u, 0.4 destroys the state; on nest4 (0.45, 1) the m = 2 boost relaxes back,
  the m = 1 seeding (all-m basis) brings Q_sw 2.0 -> 0.42 at rho_u 1.07x and tau_F 0.66 -> 0.63 (not promoted under R6, the clearest structural
  lead: carry the all-m basis on this branch in Stage II). The nest6 L6 rungs with SPEC channels and closure rows have sampled Q_sw 0.50 and 0.38 ((0.45, 0.3)) and 0.67 and 1.20 ((0.45, 1)) on
  their own (a sampled value has no one-sided bound).
- S8 (about 2.0 GPU-h, cap used): unpinned (omega free) at viscous shares 0.9-0.99 the LM destroys the core; pinned (omega fixed, core RMS pinned)
  at shares below 2 per cent nothing changes. Stage II question: the pinned ladder at intermediate nu (reports/S8_PROTOTYPE.md).
- S9/S9b (about 0.6 GPU-h so far): plain S9 lambda = 1 met both balances by near-axisymmetric collapse (guards fail; R10 (e)); S9b with guard
  rows: lambda = 1 met both balances at rho_u 1.46x (E_F overshoot 1.35 at 12 R0, about 8 core radii), lambda = 10 from it met them to 1e-4 at rho_u 1.23x
  (0.0713 / 0.0722 against 0.0579 / 0.0585): R10 (d), inconclusive, by both routes (verifier 09:46Z: 1.2317 / 1.2348 on its independent common shells;
  balances E_ren +1.3e-4, H_tot -3.1e-5 on its whole-field quadrature; Q_sw 0.987 primary / 0.996 dense theory route). Exported as
  candidates/s9b_L4_cl0.45_om1.0_bal10 (not a candidate: no rate-(2 alpha + 1) term, both far coefficients fail at order one). The two L6 runs (S9b rows with
  the closure rows 1e-3, 12:45Z): on d6w3_L6 the LM stalls after 22 iterations (balances moved only to -0.84 / -0.47 at holdout 4.3x; R10 (c)); on nest6 (0.45, 1)
  p0 the LM meets E_ren (+0.003) but not the helicity balance (-0.19) and destroys the state (holdout 9.7x, sigma_u 7.5, carried mismatch 5.8, max E_F 1.25 at
  35 R0; R10 (c)). At lambda = 1 the two scalar rows outweigh the PDE rows by 1e7 in cost and the balances are bought from the far channels and the core
  amplitude (FAILURE_ANALYSIS 30-31). Stage II form to register: lambda scaled to the PDE cost (1e-3 to 1e-2 or a continuation from 1e-4) with the S8
  core-amplitude pin and S11 closure rows at weight 1.
- Resolution study at fixed L (lead 07:14Z item 5): s1nk Nk24 on d6w3_L6 DONE 11:04Z (1.6 GPU-h): holdout 0.0528 / 0.0724 against 0.0527 / 0.0695 at Nk16,
  sigma_u^max 1.80, a_max 1.81, radial Chebyshev tails 30x smaller (A 3.4e-4, C 9.3e-4): no improvement from the radial refinement in this run (tested optimizer and
  budget; the categorical reading waits for Nk32 and an optimizer control); the far closure improves with the extra iterations (m 0.22 -> 0.06, K_E ratio -3.25 -> -0.16). Nk32 on d6w3_L6 and Nk24/32 on nest6 (0.45, 1) p0 are queued.
- L8 rungs of the nest ladder: nest8 (0.45, 1) p0 (priority 15) and nest8 (0.45, 0.3) p0 queued (3-5 GPU-h each, exclusive); read under R1/R2.
- Queue policy: 55 low-priority from-scratch L6 sweeps parked (queue/hold_lowprio) so that the exclusive rungs get whole GPUs; released when idle.

## Open items carried into Stage II
- d6w3_L8 and nest6/nest8 results (R1/R2 decisions); re-evaluation of d6w3_L8, nest6 p0/p1 and the (0.45, 1) nest6 rung for Q_sw, core sets
  and balances; the S8 and S9 lambda = 1 readings (R7, R10 after lambda 10); S7 eddy seeding (R6).
- E2 exterior implementation; preconditioned S2 attempt (optional); the verifier's independent G1 table (T03 high-omega far pressure, T06, T09).
