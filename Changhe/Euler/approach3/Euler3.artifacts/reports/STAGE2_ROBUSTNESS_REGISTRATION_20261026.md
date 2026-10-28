# Registration: Stage II robustness re-solves (twist radius R0 by a factor 2; matching radius R_far by a factor 4)

Registered 2026-10-26T09:50:49Z by the numerics lane, before any launch, under the lead's approval d128 EQ (2026-10-26T09:47:39Z): Stage II robustness
work under PROMPT II.2 (matching radii varied over factors of two) and SPEC 7.11 X3 (R_far moved by a factor 4 each way). Queue priority 6
(below every registered arm), no preemption, GPUs 0, 1, 4 and 5 only, one job per GPU (exclusive). These re-solves do not replace the Stage III
single-change re-solves of the lead's reports/stage3_plan_draft.md section 3; Stage III reuses the results where they apply. Nothing here is a
candidate, a Tier S reading, a floor, a trend or a convergence claim: each re-solved state is read against its own same-budget control, plainly
and with its failures, after its full battery.

## Solver and tools (unchanged solver; only R0 or far_radii change)
- scripts/worker.py sha256 1db489a1a0f5f82c96dfe4b798d980370ed126a8f81c3d8aa87e42336c709496; src/optimization/transfer.py c7df63cb2706fdbee74230276681160a7a5ac1414827da7bc4a940032f3f2dfb;
  scripts/enqueue_continuation.py 4e5370e04475a91a394a064604f24ff9823c80d7ee43a385839e580edd0c2f03.
- scripts/reexpand_state.py cf7a514749320fec93e94ed279fe2c96536df4db499d79502ee1a145a28de2aa (re-expansion across a change of R0: linear least-squares fit of the source velocity
  on the destination training grid in the tail-constrained coordinates; the output is a WARM START, never a reading; its fit error is in the start
  file's meta and below).
- scripts/compare_fields.py 87b5ec51dee7682659b5df366dfbcf7f53f426a05fffd5b5007c096e9b2c782a (SPEC 7.10 gauge-aligned comparison: rotation about e_3 aligned by minimizing
  ||V||_*; ||V||_* over the 7.1 shells plus the far spheres; ||V||_*,1 with DU and Omega; F-gauge of both states).
- Smoke of both tools: runs/stage3_smoke/smoke_20261026T092440Z.log (NUM_REPORT 'Shift 8: Stage III tooling').

## Start states (sha256 of the start files)
- St-A: nest6 (0.45, 1) p0 = runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt, sha 83aa4c6e9473c8bd76524600ec758fa4202840972ff242f27c5806411101dbcd (c_l 0.45, omega 1, omega/c_l 20/9; L6 Nk16 Nr48, R0 0.3,
  channels NkB/NkD/NkE 4/4/4 with degrees 15/14/6, tail constraints, closure rows 1e-3, all5far denominator, far_radii 4096/16384/65536 R0; its own
  holdout rho_u^max 0.04604 std / 0.04630 half; LM status max_iter at 600 iterations, V10 0.061).
- St-B: nest6 (0.45, 0.3) p0 = runs/nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0/starts/start_000.pt, sha efb370e082fe6a1f5195ce66f3c7c7055afe7cea1b40eb7e4b9d3f27ba21ef1c (omega/c_l 2/3; same representation; holdout 0.06687 / 0.06753).
- St-C: nest8 (0.45, 1) p0 cont150 = runs/nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/starts/start_000.pt, sha 76d4624af76070eb2be9c42cdcf2f4cd652a47dd9d3763d59e05d96bc4e9e83e (L8 Nk20 Nr60, R0 0.3, channels 4/4/4 with degrees
  19/18/8, chunk 128; holdout 0.04367 / 0.04331; status ftol at 150 iterations).
- Re-expanded warm starts of St-A (written by reexpand_state.py, L6 Nk16, tail constraints): R0 0.6 = runs/stage3_smoke/nest6_R0_0.6.pt, sha
  527888767b08d0fbab11a4695a54429122b67fed343c9e2558851c3c13bde641 (relative L2 fit error 2.62e-2, max pointwise 8.7e-2 at r 0.456, compare_fields ||V||_* 5.3e-2 against St-A, ||V||_*,1
  0.21, F-gauge 0.99978); R0 0.15 = runs/stage3_smoke/nest6_R0_0.15.pt, sha 847cd4e52b4d4bcfc274a0ff03384960f63bd8fdd05b837a940f63aaea3ba475 (fit error 9.0e-3, max 3.6e-2 at r 1.28,
  ||V||_* 1.6e-2, ||V||_*,1 0.098, F-gauge 1.00014).
- Re-expanded warm starts of St-B (R0 0.6, 0.15) and St-C (R0 0.6, 0.15): runs/stage3_prep/ (being written at registration time by
  runs/stage3_prep/run_prep.sh with the same script; their shas and fit errors are appended to this file before their jobs are enqueued).

## Jobs (all: c_l and omega fixed, even class, 'mom' formulation with the full-space pressure, closure rows 1e-3, all5far, tail constraints,
## nl_weighting, ftol 1e-7, chunk 512 at L6 and 128 at L8, exclusive, priority 6, max_retries 6)
Group (i), from St-A, 300 LM iterations each, time_limit_per_start 7200 s, about 1.1-1.3 GPU-h each including the battery:
- s5ctl_L6_cl0.45_om+1.0_fixed_R0p3_ctl: CONTROL = St-A continued unchanged (R0 0.3, far_radii 4096/16384/65536 R0; exact embedding).
- s5r0_L6_cl0.45_om+1.0_fixed_R0p6: the R0 0.6 warm start, R0 0.6 (far anchors at 4096/16384/65536 x 0.6, the dyadic holdout shells from R0 2^-5).
- s5r0_L6_cl0.45_om+1.0_fixed_R0p15: the R0 0.15 warm start, R0 0.15.
Group (iii), from St-A by exact embedding (R0 0.3), 300 iterations, 7200 s, read against the control of (i):
- s5far_L6_cl0.45_om+1.0_fixed_farx0.25: far_radii 1024/4096/16384 R0 (R_far / 4).
- s5far_L6_cl0.45_om+1.0_fixed_farx4: far_radii 16384/65536/262144 R0 (R_far x 4).
Group (ii), from St-B: the three jobs of (i) with omega 0.3 (ids s5ctl_L6_cl0.45_om+0.3_fixed_R0p3_ctl, s5r0_L6_cl0.45_om+0.3_fixed_R0p6,
  s5r0_L6_cl0.45_om+0.3_fixed_R0p15), enqueued when their warm starts are written and appended below.
Group (iv), from St-C at degree 8, 150 LM iterations each, time_limit_per_start 9000 s, about 4.5 GPU-h each: s5ctl_L8_cl0.45_om+1.0_fixed_R0p3_ctl
  (control = cont150 continued unchanged), s5r0_L8_cl0.45_om+1.0_fixed_R0p6, s5r0_L8_cl0.45_om+1.0_fixed_R0p15; enqueued only if (i) to (iii) are
  done or running and every job of (iv) can end before the limit below.
Order of launch (priority 6, ties by creation time): (i), (iii), (ii), (iv). Budget: about 8 x 1.2 + 3 x 4.5 = 23 GPU-h.

## Absolute end and non-launch rules
- Every job must END (battery included) before 2026-10-27T17:00:00Z. Rule enforced by the numerics shifts: an L6 job of (i)-(iii) not started by
  2026-10-27T13:00Z and an L8 job of (iv) not started by 2026-10-27T10:00Z is moved to queue/hold (not launched); a job still running at
  2026-10-27T16:30Z is stopped (SIGTERM checkpoints it) and its checkpoint is recorded as 'stopped at the Stage II limit, not read as a re-solve'.
- Coefficients frozen before 2026-10-27T17:09:12Z count as Stage II work; anything after is charged to Stage III.

## Readings (per re-solved state, against its own same-budget control; primary-reported until the verifier evaluates them)
- The standing lines of NUM_REPORT (both shell families, rho_nl^max, single sphere, rho_lin, sigma_u^max (shells and core sets), sigma_Om, a_max
  (shells and core sets), a_eff and core resolution, strain ratio, holdout rho_Om^max, tau_F, delta_G, sampled Q_sw, e_core, e_F, N_core, N_F,
  E_ren, max E_F and its radius, H_tot/int|h|, carried mismatch m and the K_E / K_H ratios (closure rows at 1e-3: carried values, not R12 readings),
  kappa finite radius, radial-lambda share, V10, iterations / status / seconds, CODE VERSIONS, battery memory), from scripts/arm_reading.py.
- compare_fields.py of the re-solved variant against the re-solved control (the control is the reference): aligned angle, ||V||_* (U) and
  ||V||_*,1 (DU, Omega) with the per-shell table, the F-gauge of both. For R0 variants the grid uses the control's R0 (0.3) for the shells.
- Representation-dependence flag (descriptive, registered here): a variant whose ||V||_* against the control exceeds the control's own holdout
  rho_u^max (standard family) is recorded as 'R0 (or R_far) change moves the re-solved state by more than its residual level'; below that it is
  recorded as 'within the residual level'. The flag is a description of this pair of solves, not a convergence statement.
- SPEC 7.11 X3 thresholds for group (iii) (each read separately, met / not met): (X3a) holdout rho_u^max of the variant within a factor 2 of the
  control's on both shell families; (X3b) rho_nl^max within a factor 2 on both families; (X3c) the leading-tail coefficients: the compare_fields U
  ratio on the three far spheres of the control's radii (4096, 16384, 65536 R0) at most the control's holdout rho_u^max (the stated uncertainty of
  the tail at the residual level), and the carried K_E and K_H ratios of the variant within 0.1 of the control's. X3 is 'met' only if (X3a)-(X3c)
  all hold; a 'not met' is recorded with its numbers and is a failure-map entry, not an exclusion.
- Failures are recorded as such (OOM, time limit, LM status, battery holdout missing). No ordering ahead of the control except under SPEC 7.3b.

## Appendix A (2026-10-26T10:04:27Z): group (ii) warm starts and enqueue; worker loading smoke
- Worker loading smoke (CPU, disposable, never ranked): job smoke_s5r0_R0p6_load (the s5r0 R0 0.6 configuration with max_iter 1, lm_only) loaded the re-expanded start
  through init_from (embedding identity; projected warm start relative change of U 0; cost blocks pde 4.482e-8, non-pde rows 0.3699) and completed one LM iteration
  (JOB DONE, 510 s on 4 CPU threads; runs/stage3_smoke/worker_smoke_20261026T095234Z.log). The init_from path for re-expanded starts works.
- Re-expanded warm starts of St-B (nest6 (0.45, 0.3) p0, sha efb370e082fe6a1f...), written by runs/stage3_prep/run_prep.sh (reexpand_state.py, L6 Nk16, tail constraints):
  R0 0.6 = runs/stage3_prep/nest6_om03_R0_0.6.pt, sha 0adee45d1d1940e1b35371d5dfd701e35ea7dc8f28e3e2e3055c132a96dabf6e (relative L2 fit error 1.79e-2, max pointwise 7.2e-2
  at r 0.456, compare_fields ||V||_* 3.0e-2 against St-B, ||V||_*,1 0.139, F-gauge 1.00017; 379 s);
  R0 0.15 = runs/stage3_prep/nest6_om03_R0_0.15.pt, sha c2391cbb1ad7073ca2d2686b45abab40d6f5a08d7f26376bb80db67caff040d2 (fit error 8.6e-3, max 2.6e-2 at r 0.142, ||V||_*
  1.06e-2, ||V||_*,1 0.129, F-gauge 1.00052; 425 s).
- Group (ii) jobs enqueued at 2026-10-26T10:04:27Z (priority 6, same settings as group (i); 300 iterations, 7200 s): s5ctl_L6_cl0.45_om+0.3_fixed_R0p3_ctl (control = St-B continued
  unchanged), s5r0_L6_cl0.45_om+0.3_fixed_R0p6, s5r0_L6_cl0.45_om+0.3_fixed_R0p15.

## Appendix B (2026-10-26T10:20:44Z): corrections after the astra referee pass (astra/tools_review/answer.md; before any robustness job has started)
- X3 wording. The far_radii change moves the far ANCHOR residual rows (the far checkpoints of the residual, each a shell of weight 1/(n_shells + n_far), and the
  holdout's outermost node); the pressure solver's exterior extrapolation starts at the last Chebyshev source node independently of far_radii, and the compactified basis
  has no analytic matching boundary. So group (iii) tests the sensitivity to the far anchor radii (x 1/4, x 4), not the motion of an analytic matching radius R_far.
  Criterion (X3c) is a far-field sensitivity PROXY (far-sphere velocity ratio against the control plus the carried K_E and K_H ratios); the stability of the fitted
  pressure-multipole coefficients C_lm of SPEC 7.11 X3 is not measured by it and is recorded as unevaluated. 'X3 met' in the readings therefore means 'X3a, X3b and the X3c
  proxy met'. X3a and X3b use the strict inequality (ratio strictly between 1/2 and 2).
- Representation-dependence flag: reported as 'field discrepancy above / below the registered residual-number threshold (the control's holdout rho_u^max)'; it is a
  descriptive threshold, not a solution-error or representation-independence statement. Readings with an incomplete battery, a failure flag or a non-finite value are
  'unevaluated', never met or not met.
- Domains: compare_fields uses the worker's holdout shells of the control (core ball below R0 2^-5 rounded down to a dyadic radius, dyadic shells to the control's outermost
  node) plus single spheres at the control's far anchor radii; this is the registered comparison domain, not the literal SPEC 7.1 r_core / thin-shell definition. The states'
  own holdout maxima (worker batteries) are over shell sets that differ when R0 or far_radii differ (the innermost core ball and the outermost shells); the reading also
  lists the per-shell holdout rho_u on the shells with identical edges and names the shells present in only one state.
- Rotation alignment: the coefficient map by gamma realizes the field rotation U_gamma(y) = R_{-gamma} U(R_gamma y); the physical angle b = -gamma is reported beside gamma;
  the minimum over the rotation period is an estimated minimum (coarse grid of 72 angles, the three best coarse basins refined by golden section).
- Optimization drift: the control itself advances 300 (L8: 150) iterations; the reading adds compare_fields(original start -> continued control) so that the variant-control
  difference is read beside the control's own motion. The 'start' column of scripts/arm_reading.py for a re-expanded variant refers to the ORIGINAL state (St-A/B/C),
  whose holdout diagnostics the warm-start file carries for bookkeeping, not to the fitted start (unevaluated).
- Re-expansion fit: the fitted coefficients are a warm start only (column-scaled truncated SVD, rcond 1e-12, condition numbers 1e25-1e26, equal radial-node weights times the
  (1 + r^2/R0^2)^alpha tail factor); the recorded fit errors are grid quadrature estimates, not bounds.
- Tool versions after the corrections: scripts/compare_fields.py c77b9645ae91b167..., scripts/reexpand_state.py be90bc1fcf8f1c17...,
  scripts/robustness_reading.py a09d03e5cbeb98c3.... The warm starts of groups (i) and (ii) were written by the pre-correction reexpand_state.py
  (the corrections changed bookkeeping fields and the nu/tail-constraint consistency, not the fit); their shas above stand.

## Appendix C (2026-10-26T10:29:13Z): lead decision on Appendix B (lead message after d128 EV; corrections accepted)
- Group (iii) is kept under the label 'far anchor radii sensitivity (x 1/4, x 4)'. No reading, note or report text calls it the motion of an analytic R_far or of a matching
  boundary.
- X3 is reported as 'X3a, X3b and the X3c proxy met / not met'; the C_lm stability of SPEC 7.11 X3 is recorded as unevaluated; the proxy counts as X3 for no tier.
- The other Appendix B corrections (b = -gamma, estimated minimum over the three best coarse basins, the stated comparison domains, verdicts gated on complete batteries and
  finite values, the control drift, the per-shell holdout rho_u on identical edges, 'start' = the original state) are noted by the lead, who checks the wording of each
  reading against this registration.

## Appendix D (2026-10-26T10:54:08Z): group (iv) warm starts and enqueue (degree 8, from St-C = cont150 (0.45, 1), sha 76d4624af76070eb...)
- Re-expanded warm starts written by runs/stage3_prep/run_prep.sh (reexpand_state.py pre-correction version, L8 Nk20 Nr60, channels 4/4/4 degrees 19/18/8, tail constraints,
  chunk 128; log runs/stage3_prep/prep_20261026T094802Z.log):
  R0 0.6 = runs/stage3_prep/cont150_om1_R0_0.6.pt, sha c16cd781ba98d24f16ee8613c51569e99e65db3b1cfd9174426a8240a1bcefbc;
      fit: weighted relative residual 1.290e-02, unweighted relative L2 error 1.325e-02, max pointwise error 5.223e-02 (max|U| 1.252), worst radius r = 0.5154 (relative error 3.742e-02); rank 2700 of 2719, cond 1.10e+27; F-gauge int|F|^2 of the fitted state 1.000013930657889; 1480.9 s
    compare_fields against St-C:   ||V||_* (U) = 2.4837e-02; ||V||_*,1: DU 1.4461e-01, Omega 1.5362e-01 (max 1.5362e-01)
  R0 0.15 = runs/stage3_prep/cont150_om1_R0_0.15.pt, sha 041c6351e3f66c89d5ccaea6acb655d437bbeb67e374d4504d2915b4b662849d;
      fit: weighted relative residual 4.979e-03, unweighted relative L2 error 4.292e-03, max pointwise error 1.773e-02 (max|U| 1.254), worst radius r = 0.5641 (relative error 9.019e-03); rank 2700 of 2719, cond 1.41e+28; F-gauge int|F|^2 of the fitted state 1.0003802002877844; 1449.3 s
    compare_fields against St-C:   ||V||_* (U) = 7.4093e-03; ||V||_*,1: DU 6.5388e-02, Omega 5.4199e-02 (max 6.5388e-02)
- Group (iv) jobs enqueued at 2026-10-26T10:54:08Z (priority 6, exclusive, 150 LM iterations, time_limit_per_start 9000 s, chunk 128, closure rows 1e-3, all5far, tail constraints; about
  4.5 GPU-h each): s5ctl_L8_cl0.45_om+1.0_fixed_R0p3_ctl (control = St-C continued unchanged at R0 0.3), s5r0_L8_cl0.45_om+1.0_fixed_R0p6, s5r0_L8_cl0.45_om+1.0_fixed_R0p15.
  By creation time they start only after the eight L6 jobs of groups (i)-(iii) have started (same priority, ties by creation time), which realizes the EQ condition that (i)-(iii)
  are done or running. Non-launch rule: an L8 job not started by 2026-10-27T10:00Z goes to queue/hold; a job running at 16:30Z is stopped and not read.

## Appendix E (2026-10-26T11:09:00Z): pre-correction reexpand_state.py and reading wording (lead message on Appendix D)
- The warm starts of groups (i), (ii) and (iv) were written by reexpand_state.py before the Appendix B corrections. Those corrections do not touch the fit: the evaluation of the
  source field on the destination grid, the weighting, the tail-constrained least squares (fit_field) and the saved coefficients are identical. They changed (a) the saved
  config's tail_constraints flag (already True for every destination here, so no change), (b) nu read from the config (0 for every job here, so no change), and (c) the bookkeeping
  copy of the original source's diagnostics under 'original_source_diagnostics' (reporting only). So the pre-correction starts are the same coefficients the corrected script
  would write for these configurations; their shas stand.
- Reading wording (lead plan draft d153bec0, note d128 FG): the far_radii change is a far-anchor proxy that counts as X3 for no tier; compare_fields covers the registered domain
  only (the control's worker holdout shells and far anchor spheres). The terminal LM cost cited in every reading is history[-1]['cost_after_reweight'] (not an iteration-log
  value); the unnormalized weighted training momentum RMS rms_mom of variant and control is shown beside the holdouts.

## Appendix F (2026-10-26T11:20:10Z): evidence for 'fit untouched' (lead request) and a correction to Appendix D
- Pre-correction reexpand_state.py = scripts/reexpand_state.py.bak_1020, sha256 cf7a514749320fec93e94ed279fe2c96536df4db499d79502ee1a145a28de2aa.
  Corrected reexpand_state.py (current), sha256 be90bc1fcf8f1c1789842f970243a6b8c9ea6f4c1bc2072f0306652b680760d9.
  Unified diff: reports/reexpand_state_correction_20261026T1020Z.diff, sha256 fcde342ea9310ecb389a70fc6dcd09d65fff2eb1f54cb7c129e48a8bb1b64079 (34 lines, three hunks): (1) one added line cdst["tail_constraints"] = use_tc
  (the saved config flag; True before and after for every destination here); (2) TailConstraints(Md, nu=0.0) -> TailConstraints(Md, nu=float(cdst.get("nu", 0.0) or 0.0)) (nu is 0 for
  every job here, so the constraint maps are identical); (3) the output dict gains the key original_source_diagnostics (a copy of the original source's holdout diagnostics with a
  note). The evaluation of the source field on the destination grid, the fit_field call (chunk, expand, n_red, rcond), the weighting inside fit_field and the written
  coefficients z are not touched by the diff.
- Correction to Appendix D: the L8 warm start runs/stage3_prep/cont150_om1_R0_0.15.pt (sha 041c6351e3f66c89...) was written at 10:51:53Z by the CORRECTED script
  (the prep script started that fit after the 10:20Z patch); evidence: its file carries the key original_source_diagnostics. The other five warm starts were written by the
  pre-correction script (nest6_R0_0.6.pt 09:33:47Z, nest6_R0_0.15.pt 09:41:52Z, nest6_om03_R0_0.6.pt 09:54:22Z, nest6_om03_R0_0.15.pt 10:01:53Z, cont150_om1_R0_0.6.pt 10:26:59Z;
  none carries that key). All six have config tail_constraints True and were fitted with nu 0; by the diff above the two versions write the same coefficients for these
  configurations.
