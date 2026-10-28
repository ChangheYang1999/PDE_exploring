# Addendum 1 to the lead review of the Stage III replication registration

Date 2026-10-26T18:36Z. Reviewer: lead lane (us.anthropic.claude-opus-5-5). This file adds to REVIEW.md (sha 1f027b8e293b265b1f314a7be211b2454ac3c752ebacedcbe85f9b85fd35d88e, note IE). It does not replace it.

- **Source.** The verifier audit report_reviews/20261026T183416Z_StageIII_replication_registration_audit/REVIEW.md (sha 1ed8428752badcce8f2911679c46685d0445a04a56ff36694c8e304f760e67f0), on the same registration e9617f57.
- **Parameters.** c_l = 0.45, omega = 1, nominal omega/c_l = 20/9 throughout.
- **Decision.** The registration stays ACCEPTED WITH CONDITIONS, now S3-1 to S3-21. Nothing is enqueued before II.4.

## 1. What I checked against the source

I checked each verifier claim against the files that are current now:
- supervisor.py 53f53cfd;
- perturb_start.py 51a8b1cc;
- compare_fields.py c77b9645;
- worker.py 1db489a1.

Findings:
- **RIII-2.** supervisor.py check_running (lines 108 to 125) kills a running job only for RSS above the limit or a stale heartbeat. There is no elapsed or absolute-end test. worker.py passes time_limit_per_start to the solver only; the battery after the LM is not bounded by it. Confirmed.
- **RIII-5.** perturb_start.py line 96 has tail_check = (tail_change <= 1e-12 and abs(F1 - F0) <= 1e-12). F0 and F1 are tail_norm2 before and after (line 65). Neither is compared with 1. Confirmed.
- **RIII-6.** Line 61 computes rel_hold = (Uh1 - Uh0).norm() / Uh0.norm(), an unweighted Euclidean norm of the sampled holdout values. Confirmed.
- **RIII-8.** worker.py lines 403 to 410 divide all n_coef coefficients by nF = sqrt(tail_norm2) after the LM, under gauge F. Confirmed.
- **RIII-1.** compare_fields.py prints and stores domains = "worker holdout shells (r_core = R0_ref, dyadic) plus far anchor spheres ...; not the literal SPEC 7.1 r_core / thin-shell definition". Its definition string still cites the 7.1 shells. Confirmed.
- **RIII-7 arithmetic.**
  - sqrt(1.05) - 1 = 0.0246951 > 0.02.
  - |sqrt(int|F|^2) - 1| <= 0.02 is equivalent to int|F|^2 in [0.9604, 1.0404].
  - The two R3 predicates are therefore not equivalent. Confirmed.
- **RIII-4.** The cfg_match term is `not S.get("free_params")`, from the saved state. The SVD is over every column of M. This was already my IE finding (i). Confirmed.

## 2. Corrections to my earlier notes

- **IA item on the R0 accounting.** It said the enforced total equals the per-worker caps, at most 8.0 reserved GPU-h. That is wrong.
  - The four 7200 s values are LM time limits. The LM checks them after each iteration, so it can overshoot by up to one iteration. The battery afterwards is not bounded.
  - 8.0 GPU-h is a planning figure, not an enforced bound.
  - The R0 variants keep their launch-by 06:00Z, end-by 10:00Z and readings-by 12:00Z windows. The numerics operator enforces the end by hand (S3-14 (b)), and the actual occupied seconds are recorded and summed.
- **IE condition S3-3.** The caps 3.4 GPU-h (R2a 4.6) and R3's 8 GPU-h are planning figures until a reviewed enforcement mechanism exists (S3-14). The equal-time-limit part of S3-3 stands as written.

## 3. New conditions

- **S3-13 (RIII-1). Comparison domains.**
  - Every returned or not-returned reading states that compare_fields distances are taken on the worker holdout shells plus the far anchor spheres, not on the literal SPEC 7.1 domains.
  - The alignment angle is an estimated minimum from a coarse search with golden-section refinement, not a certified minimizer.
  - The distance is a robustness diagnostic, not an acceptance norm.
- **S3-14 (RIII-2, RIII-3). Enforced caps.**
  - (a) Before any Stage III enqueue, numerics register a cap watcher as new tooling under rule AU, for my review by 2026-10-27T12:00Z. It must bind and log, per job:
    - the job id and the owned worker PID with its start ticks;
    - the start clock;
    - a whole-job cap covering setup, solver, battery and any GPU reading;
    - the absolute end;
    - TERM, then KILL after a stated grace.

    It also records the treatment of an incomplete battery (the state is not read), no retry, and the measured occupied GPU-seconds.
  - (b) If no reviewed watcher exists at II.4, the caps are planning figures. The numerics operator then stops every job still running at its absolute end by hand, and records the time and the reason. Every reading carries the actual occupied seconds.
  - (c) In either case, the latest launch for each job is its absolute end minus its cap:

    | Job | Latest launch (UTC) |
    |---|---|
    | R1 | 2026-10-28T00:36Z |
    | R2a | 2026-10-28T01:24Z |
    | R2b, R2c, R2d | 2026-10-28T02:36Z |
    | R3 | 2026-10-27T22:00Z |

  - (d) If the shared control s5ctl_L8 runs after II.4, it is reserved at 3.4 GPU-h. It runs before or beside the R jobs, as registered.
  - (e) The R4 pair must also be read by 10:00Z. Its latest launch is therefore 2026-10-27T21:00Z, and S3-8 applies.
- **S3-15 (RIII-4). perturb_start.py for any new start.**
  - Build M from the A/C columns only.
  - Refuse a built free-parameter model, read from model.free_params and the job config, before M is constructed.
  - This applies to the R3 kernel-projected alternative (S3-6), the R4 start and any St-C replacement.
  - The three R1 files are kept. The model is fixed-parameter, so the non-A/C columns of M are zero (RIII-4), and the A/C-only projection then equals the all-column one exactly.
  - S3-10 still requires each R1 job's log to show the built model without free parameters.
- **S3-16 (RIII-5). Unit-tail bounds.**
  - The acceptance test requires |F0 - 1| <= 1e-12 and |F1 - 1| <= 1e-12, in addition to the difference test. F means int|F|^2.
  - For the three R1 files, numerics state F_norm2_before and F_norm2_after from the saved acceptance records. Those values stay primary-reported.
  - Every new start record carries, at creation, the script sha, the source and job-config shas and the start sha.
- **S3-17 (RIII-6). Size wording.**
  - The 1e-2, 3e-2 and 1e-1 sizes are training-grid quadrature L2 ratios.
  - The holdout ratios 5.5e-3, 1.58e-2 and 6.06e-2 are unweighted Euclidean ratios of sampled holdout values.
  - Neither is a compare_fields distance. The distance-response table shows all three, labelled.
- **S3-18 (RIII-7). One R3 gauge predicate.**
  - The predicate is abs(||F|| - 1) <= 0.02 at the start, that is int|F|^2 in [0.9604, 1.0404]. This is the standing warm-start rule form. The 0.05 test on int|F|^2 is withdrawn.
  - With the kernel-projected alternative, F is unchanged to rounding and the predicate is checked as such.
  - Section 0's "every start keeps ||F|| = 1 exactly" is restricted to R1, R2 and R4.
- **S3-19 (RIII-8). Endpoint normalization wording.**
  - Replace "velocity scaling is never used" with: "no velocity scaling replaces an Euler dilation of a start; after the LM the worker divides all coefficients by ||F|| (the factor is recorded), and the battery evaluates the saved normalized endpoint".
  - Every reading reports |nF - 1|, and the optimizer gauge defect beside the projected one.
- **S3-20 (RIII-9). Reading partition.** The shared rule becomes one-sided on the holdout, per shell family k.
  - (i) **Returned within the residual level:** rho_variant,k <= 1.1 rho_control,k on both families, AND norm_star_U at most the control's holdout rho_u^max (standard family).
  - (ii) **Flagged:** the holdout condition of (i) holds, but norm_star_U is above that bound. It is reported with the start distance and the control's drift.
  - (iii) **Not returned:** rho_variant,k > 1.1 rho_control,k on either family. The sensitivity is not separable from the start distance.
  - **Lower residual (a remark, not a separate case).** In case (i) or (ii), if rho_variant,k < 0.9 rho_control,k on a family, the line reads "lower holdout residual than the control on family k". It does not order the states; ordering is through order_73b.py only.
  - The failure definitions are unchanged.
  - The same one-sided form applies to the R0 readings under HX R0-1 to R0-3.
- **S3-21 (RIII-10, RIII-11).** These are already S3-1 and S3-12 of REVIEW.md.
  - The verifier's added point stands: the phase rotation must come before any target is frozen. The closure target and the nonlinear weights both count. Pre-aligned starts with rel_change_z <= 1e-12 meet it.

## 4. Scope

The R jobs yield labelled robustness readings of approximate states. No tier, uniqueness, convergence, exact profile or obstruction follows from them. The label stays provisional C.
