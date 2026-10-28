# Lead review of the Stage III replication registration R1 to R4

Date 2026-10-26T18:32Z. Reviewer: lead lane (us.anthropic.claude-opus-5-5). Rule AU review before any Stage III enqueue.

- Reviewed file: numerics reports/STAGE3_REPLICATION_REGISTRATION_20261026.md, sha256 e9617f578e7814172eecf85dd078fd17a4f0ffa4cef3f238562b75dbc108b97f (modified 2026-10-26T18:26:51Z, with the section 5 R1 entries).
- Parameters: c_l = 0.45, omega = 1, nominal omega/c_l = 20/9 throughout.
- Plan: the draft cites plan e86ff8ae. The current plan is c551bcb5. Its section 3 has the same case C list (R1 to R4), the same R2 items (radial map, pivot, shell weights, truncation order) and the same R4 late-result rule. The registration must cite c551bcb5 (condition S3-12).

## 1. Decision

**ACCEPTED WITH CONDITIONS S3-1 to S3-12** (section 4). Nothing is enqueued before gate II.4 (2026-10-27T17:09:12Z). Each job still needs its pre-launch record (S3-1) and a dated enqueue line in NUM_REPORT. A start or option that fails its condition is dropped and recorded as not run. It is not repaired at launch time.

What the registration can deliver is robustness readings (PROMPT III.3) of one provisional representative under one solver. It cannot deliver a tier, uniqueness, convergence or an exact profile, and the draft says so.

## 2. Checked

- **Shared objects.** St-C is the cont150 start_000.pt, sha 76d4624a.... The control s5ctl_L8_cl0.45_om+1.0_fixed_R0p3_ctl is in queue/pending. Its config is L8 Nk20 Nr60, R0 0.3, channels 4/4/4 at 19/18/8, far 4096/16384/65536, closure_lambda 1e-3, chunk 128, free_params false, max_iter 150, time_limit_per_start 9000 s. It sets no refresh_block, so it uses the default refresh after every accepted step. The draft's shared settings agree.
- **cont150 history.** Its worker.log ends "ftol, 83 its, 3409s", about 41 s per accepted iteration, with pivot defect 0.0 and gauge defect 4.4e-16. The draft's "status ftol at 150 iterations" should read "ftol at 83 of 150 iterations".
- **Worker start sequence** (scripts/worker.py lines 160 to 212). The order is:
  1. embed init_from;
  2. apply the optional perturb or perturb_m;
  3. prob.choose_pivot(z), chosen once per start and then fixed (gauge_rows only sets it when it is None);
  4. update_closure(z) and the other refreshes at the unprojected z, then cost0.

  The LM projection is tc.reduce(phase_align(tc.expand(zr))). If that projection moves the start, the frozen target no longer matches the first iterate. This is the sgcont150 mechanism (note ID). For R1 and the control it is harmless only if the start is already aligned to the pivot the worker will choose. scripts/block_costs.py --phase_align measures exactly that (rel_change_z and after_closure_refresh).
- **R1 starts.**
  - I read perturb_start.py 51a8b1cc lines 40 to 100:
    - the row-scaled SVD kernel projection;
    - the training-grid scale factor;
    - the eight acceptance tests;
    - the pivot chosen on z and on z_new;
    - the margin from mode_tail_energies.
  - The section 5 rows report all 8 tests passing:
    - pivot (S, 5) unchanged, with margin 1.203;
    - projection residual at most 2.1e-16;
    - |int F^2 - 1| at most 4.4e-16;
    - training ratio 1e-2, 3e-2 and 1e-1, with holdout ratios 5.5e-3, 1.58e-2 and 6.06e-2.
  - These are numerics-reported values; I did not recompute them.
- **Pivot margin.** The margin 1.203 is large enough that the worker's amplitude rule returns (S, 5) on every R1 start. It is the same rule perturb_start.py applies.
- **Keys.** far_weight is a real configuration key (worker.py line 63, Problem far_weight, which scales the merged far nodes). refresh_block and refresh_backtrack exist in worker.py, default off. No pivot_rank option exists in the source today, as the draft states for R2d.
- **The L8 radial map.** The R0 variants in queue/pending are all L6 (s5r0_L6_..._R0p15_refit and _R0p6_refit at omega = 0.3 and 1). At L8, therefore, no change of the radial map radius is registered anywhere.

## 3. Findings

- **(a) The Z0 condition is missing.** Every start, the control included, needs the note ID condition. Without it a rotated start can yield an invalid re-solve that still looks like a result.
- **(b) The budgets are unequal.**
  - R1, R2b, R2c and R2d have time_limit_per_start 6000 s; the control has 9000 s.
  - At about 41 s per iteration, 150 iterations take about 6150 s plus setup. A perturbed start that needs all 150 iterations would be clipped near 140 to 145, while the control would not be.
  - The time limits must be equal. Otherwise "returned" and "not returned" confound the start with the budget.
- **(c) The refresh mode is not stated.** It must be the control's: no refresh_block, so refresh after every accepted step.
- **(d) R2d changes the pivot by design.** This is the sgcont150 mechanism by construction. The worker would refresh the closure at the unrotated start and then rotate it.
- **(e) R3 has the same exposure, plus one more.**
  - perturb_m seeds m = 1 tail modes inside the worker before choose_pivot.
  - If an m = 1 pair's tail amplitude exceeds 0.1305 (the (S, 5) amplitude), the pivot becomes an m = 1 pair. The rotation to the gauge is then large, with period 2 pi instead of pi, and the start has no saved file to check.
  - The alignment of an all-m state against the even control must use the full rotation group: compare_fields with gcd(m) = 1.
- **(f) R2a is a collocation change, not a radial-map change.** The draft says so. The report must not list it as the plan's "radial map" item. The map radius was varied only at L6.
- **(g) R4 cannot run under the registered order.**
  - With equal budgets (S3-3), R1 occupies three GPUs from II.4 to about 20:35Z and R3 the fourth until about 22:40Z.
  - R2a to R2c then take the three freed GPUs, and the fourth R2 job waits for R3.
  - At 2026-10-27T22:00Z no GPU is free, let alone the two R4 needs for 12 h each.
  - Running R4 on two GPUs from II.4 would push R1 to R3 (about 33 GPU-h on the other two) past their 04:00Z and 06:00Z ends.
  - R4 is therefore expected to be recorded as "not run (GPU time)". It is not reordered ahead of R1 to R3.
- **(h) Cross-route GPU.** Plan section 3 releases one numerics GPU for cross-route verification only if a transfer tool is registered and reviewed before the gate. None is registered, so all four numerics GPUs go to R1 to R4.
- **(i) The free-parameter check reads the saved state.** As noted in IB remark (b), cfg_match in perturb_start.py reads S.get("free_params") from the saved state, not from the job. It passes trivially if the key is absent.
- **(j) The absolute tail threshold needs its normalization stated.** As noted in IB remark (d), the absolute 1e-12 tail check is meaningful only under int|F|^2 = 1 (tail amplitudes of order 0.1). The registration should say so.

## 4. Conditions

- **S3-1. Z0 record for every job, the control included.**
  - Before enqueue, run block_costs.py --phase_align on the CPU, on the exact start file and with the exact job JSON. The record must show:
    - the worker's pivot, and that it equals the start's;
    - rel_change_z at most 1e-12;
    - the phase-aligned frozen-closure total equal to the after_closure_refresh total, to relative 1e-6.
  - After launch, the worker's logged cost0 must equal that total to relative 1e-6.
  - A mismatch makes the job a tooling failure: it is stopped and recorded, not read. The record's sha goes in section 5.
- **S3-2. One attempt.**
  - max_retries 0. The control's Stage II queue entry has max_retries 6; that is acceptable only if it runs before II.4 under Stage II rules.
  - A Stage III relaunch needs a dated lead note naming an infrastructure failure before the first accepted step.
- **S3-3. Equal budgets.**
  - R1, R2b, R2c and R2d get max_iter 150 and time_limit_per_start 9000 s, the same as the control. R2a gets 13500 s (1.5x rows), and the 1.5x ratio is stated.
  - Caps: 3.4 GPU-h each, and 4.6 for R2a. R1 totals 10.2, R2 14.8 and R3 8, about 33 GPU-h before R4.
  - Every end state reports its iteration count and stop reason. A time-limited job is read as "time-limited at k iterations", with k stated, and never as returned.
- **S3-4. Refresh mode.** Every job states refresh_block absent (0) and refresh_backtrack false, identical to the control.
- **S3-5. R2d** is registered only if all of the following hold:
  - pivot_rank is implemented in choose_pivot and smoke-tested on a disposable L4 CPU job by 2026-10-27T12:00Z;
  - phase_align_start.py honours the job's pivot_rank;
  - the start is pre-aligned to the rank-2 pivot and saved, with the rank-2/rank-3 margin recorded (drop R2d if it is below 1.05);
  - it passes S3-1 under the rank-2 pivot.

  The reading compares gauge-aligned fields. It measures dependence on the gauge-fixing choice, not on the solution.
- **S3-6. R3.**
  - Build the start offline on the CPU: the worker's perturb_m code with seed 31030 and field-relative 0.1, on the all-m embedding of St-C. Save it with its sha, the pivot and the int|F|^2 change.
  - If the pivot is no longer (S, 5), pre-align with phase_align_start.py and refresh the closure.
  - Pass S3-1. Launch from the saved file with perturb_m off, keeping the registered |int|F|^2 - 1| <= 0.05 rule.
  - Preferred alternative, if smoke-tested by 2026-10-27T12:00Z: an odd-m perturbation projected onto the kernel of the leading-tail map, as in R1. It leaves F, int|F|^2 = 1 and the pivot unchanged. Its odd-m leading tail is zero at the start and free during the solve.
  - Either way: compare_fields uses the full rotation group; odd-m content is reported at the start and the end; "odd-mode states are not excluded" remains the wording.
- **S3-7. R2a wording.** Report it as "radial collocation density 60 -> 90". In the robustness table, record "radial map radius not varied at L8 (varied at L6 only)".
- **S3-8. R4.** It stays registered under its conditions. If no two GPUs are free by 2026-10-27T22:00Z, record "not run (GPU time)". R1 to R3 are not delayed or reordered for it. Any output after 06:00Z is a late result only (plan section 6) and cannot change the label after the 14:00Z claims freeze.
- **S3-9. Cross-route GPU.** No transfer tool is registered, so all four numerics GPUs (0, 1, 4 and 5) serve R1 to R4. A tool registered and reviewed before II.4 would need its own lead note to take one GPU, taken from R2.
- **S3-10. Free parameters.**
  - Each enqueued job JSON has free_params false.
  - The worker log of each job shows the built model without free parameters (no c_l or omega coordinates in n_z).
  - perturb_start.py's check is recorded as a check of the saved state only.
- **S3-11. Normalization statement.** The section 5 header states that the absolute 1e-12 tail and int F^2 checks are under int|F|^2 = 1, with the (S, 5) pivot amplitude 0.1305 as the scale.
- **S3-12. Bookkeeping.**
  - Cite plan c551bcb5.
  - Correct the cont150 status to "ftol at 83 of 150 iterations".
  - If the St-C replacement rule fires (nest8nk8 ordered ahead under SPEC 7.3b by 14:00Z), the R1 starts are regenerated with the acceptance tests, the control is re-registered, and S3-1 is repeated. All of this needs a dated section 5 entry and a lead note before II.4.
  - The standing lines and order_73b.py remain the only ordering route.
