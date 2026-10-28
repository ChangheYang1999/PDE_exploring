# Stage II queue preparation (numerics; written 2026-10-25T10:31Z, S10/S11 added 11:07Z, S12 11:34Z, before the gate; nothing here is enqueued until the lead's gate decision at 2026-10-25T23:09Z)

Arms and readings: the lead's reports/stage2_plan_draft.md (S1-S9b, R1-R10). Measured costs: reports/STAGE2_FEASIBILITY_DRAFT.md. All jobs use the
current worker (SPEC-degree channels, closure rows, all5far weighting, tail constraints, full battery incl. the v1.24 far coefficients). Exclusive
jobs (L >= 8, chdeg) hold a whole GPU; at most four run at once. Commands run from rotating_euler_96h with .venv/bin/python.

## S1 resolution ladder (about 80 GPU-h; R1 gates each level: core-resolved and holdout rho_u^max <= 0.1; R2 floors a branch after two steps with q > 0.85)
- nest (0.45, 1): L8 rung DONE 12:50Z (0.0439 / 0.0435, q 0.955; R1 holds); per the lead's 12:54Z rule the bounded continuation (cont150) and the channel-Nk 4 -> 8 test come
  BEFORE any L10 rung; the L10 source is then the continued state (runs/nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/starts/start_000.pt). L10 Nk24 with SPEC channels B23/D22/E10 (estimate 10-17 GPU-h, 50-70 GB, exclusive;
  memory to be verified with a 3-iteration smoke job first):
      scripts/enqueue_continuation.py --src runs/nest8_L8_cl0.45_om+1.0_fixed_p0/starts/start_000.pt --tag nest10 --L 10 --Nk 24 --channels 4,4,4 --chdeg 23,22,10 \
          --closure_lambda 1e-3 --nl_den all5far --max_iter 300 --time_limit 60000 --chunk 64 --exclusive --priority 15 --suffix _p0
  Smoke first: the same with --max_iter 3 --time_limit 1200 --suffix _smoke (read the GPU memory in its worker.log; if > 75 GB, use --chunk 32).
  MEMORY (analysis 14:59Z; smokes nest10smoke_* queued at priority 20 from the two cont150 states): the LM stores the dense Jacobian (1.3 M rows x about 5000 columns
  = 52 GB at L10 with SPEC channels B23/D22/E10, against 17 GB at L8), so L10 with SPEC-degree channels is expected not to fit an 80 GB GPU whatever the chunk.
  Reductions that keep the objective: channel degrees 19/18/8 at L10 (about 3500 columns, J 36 GB; smaller carried span, same rows), or a matrix-free
  Gauss-Newton (CG on the normal equations with JVP/VJP pairs; Stage II implementation, about half a shift). The battery can run on the CPU if only it overflows.
- L10 WITH SPEC-DEGREE CHANNELS, FINAL FORM (16:35Z; lead 16:26Z: a SPEC-channel L10 run that completes under jtj_blocks 2 is read under the plain R2 rule): the dense
  Jacobian (43.3 GiB at 4515 unknowns) is replaced by the split-column J^T J accumulation (lm_solve(jtj_blocks=2), validated at L8: steps equal to 4.6e-11, costs to
  2e-15; time 1.44x, memory J/2). Enqueue lines (after the jtj2 smoke confirms the peak memory; chunk 64; 300 iterations about 300 x 240 s = 20 h plus the battery,
  so time_limit 90000; exclusive; priority 15; one job per cont150 state):
      scripts/enqueue_continuation.py --src runs/nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/starts/start_000.pt --tag nest10 --L 10 --Nk 24 --channels 4,4,4 --chdeg 23,22,10 \
          --closure_lambda 1e-3 --nl_den all5far --max_iter 300 --time_limit 90000 --chunk 64 --jtj_blocks 2 --exclusive --priority 15 --suffix _p0
      scripts/enqueue_continuation.py --src runs/nest8_L8_cl0.45_om+0.3_fixed_p0_cont150/starts/start_000.pt --tag nest10 --L 10 --Nk 24 --channels 4,4,4 --chdeg 23,22,10 \
          --closure_lambda 1e-3 --nl_den all5far --max_iter 300 --time_limit 90000 --chunk 64 --jtj_blocks 2 --exclusive --priority 15 --suffix _p0
  If the dense2 smoke shows the dense path with the J release holds 3 iterations under 80 GB, --jtj_blocks 1 (160 s per iteration, 13 h) is the faster
  alternative with no memory margin for the battery on the GPU (then the battery runs on the CPU: reevaluate_holdout.py --device cpu); the split form is the
  safe default. The ch19 form (--chdeg 19,18,8, 95 s per iteration, J 29 GB) stays available with the registered reduced-channel R2 reading.
- Channel-Nk test at L8 (lead 12:54Z item 1b; before L10): B/D/E blocks at Nk 8 (A/C unchanged), from the continued (0.45, 1) rung; smoke 14:42Z-15:39Z on GPU 0: 95-99 s per
  iteration (37 s at Nk 4), completed without OOM at chunk 64 with 75.0 GB observed on its GPU (about 5 GB margin); about 5 GPU-h per 150 iterations:
      scripts/enqueue_continuation.py --src runs/nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/starts/start_000.pt --tag nest8nk8 --L 8 --Nk 20 --channels 8,8,8 --chdeg 19,18,8 \
          --closure_lambda 1e-3 --nl_den all5far --max_iter 150 --time_limit 20000 --chunk 64 --exclusive --priority 13
  Reading (lead): a holdout more than 5 per cent below 0.0437 / 0.0433 makes the L6 -> L8 step channel-truncation-limited; otherwise the step stands.
- nest (0.45, 0.3): L8 rung DONE 12:22Z (0.0613 / 0.0609, q 0.916; R1 holds); the same rule: cont150 (running since 12:43Z) first, then L10 from runs/nest8_L8_cl0.45_om+0.3_fixed_p0_cont150/starts/start_000.pt (tag nest10, suffix _p0).
- D6 lineage: floored at L8 under R2 (d6w3_L8 worse than d6w_L8; FAILURE_ANALYSIS 25); no S1 level unless the lead reopens it. Stationarity runs
  (600-900 iterations) at L6/L8 for the nest rungs: re-enqueue the finished rung with --max_iter 600 from its own start file (same tag, suffix _cont).

## S4 parameters and symmetry class (about 30 GPU-h)
- omega path at c_l 0.45 from nest6 (0.45, 0.3) p0 and nest6 (0.45, 1) p0 (fixed parameters, exact embedding, SPEC channels and closure rows, 300 iterations,
  about 1 GPU-h each at L6-ext):
      for om in 0.1 0.2 0.5 2.0; do scripts/enqueue_continuation.py --src runs/nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0/starts/start_000.pt --tag s4om --L 6 --Nk 16 \
          --channels 4,4,4 --chdeg 15,14,6 --closure_lambda 1e-3 --nl_den all5far --omega $om --exclusive --priority 12 --suffix _from03; done
      (and --omega 0.5 2.0 from runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt with --suffix _from1)
- c_l path at omega 0.3 from nest6 (0.45, 0.3) p0: --c_l 0.42 0.44 0.46 0.48 (tag s4cl). Record the drift diagnostics (toward c_l 1/2, 2/5, omega 0, axisymmetry).
- all-m class (lead 05:21Z: at most 6 GPU-h; from the s7c m = 1 state, L4 -> L6):
      scripts/enqueue_continuation.py --src runs/s7c_L4_cl0.45_om+1.0_fixed_m1rel0.1/starts/start_000.pt --tag s4allm --L 6 --Nk 16 --m_parity all \
          --channels 4,4,4 --chdeg 15,14,6 --closure_lambda 1e-3 --nl_den all5far --max_iter 600 --time_limit 14400 --exclusive --priority 13
  (the all-m basis doubles the unknowns; smoke-test memory with --max_iter 3 first). Also the all-m embedding of nest6 (0.45, 0.3) p0 with a 10 per cent
  m = 1 perturbation: --m_parity all --perturb_m 1 --perturb_m_rel 0.1.

## S9b balance arm (about 3 GPU-h; R10 (e) guards; lambda = 10 only from a lambda = 1 state that passes SPEC 7.4)
- Running/queued: s9b L6 lambda = 1 on d6w3_L6 and nest6 (0.45, 1) p0 (priority 14, queue/hold until the d6w_L8 re-evaluation releases it).
- Then: scripts/enqueue_continuation.py --src runs/s9b_L6_cl0.45_om+1.0_fixed_bal1_naxpin/starts/start_000.pt --tag s9b --L 6 --Nk 16 --channels 4,4,4 --chdeg 15,14,6 \
      --closure_lambda 1e-3 --nl_den all5far --balance_lambda 10 --nonaxi_pin auto --exclusive --priority 14 --suffix _from_bal1

## S9d balance chain (lead registration 2026-10-25T17:20:02Z; replaces the unscaled S9b lambda = 1 form; priority 12, after S10-S12, not before gate I.4; 2 GPU-h per chain)
- Chain start Z0 = the end state of the S11 closure-weight-1 rung from nest6 (0.45, 1) p0 and from nest6 (0.45, 0.3) p0 (enqueue the weight-1 rungs from the s11 1e-1 end
  states first: --src runs/s11_L6_cl0.45_om+1.0_fixed_cl1e-1/starts/start_000.pt --tag s11 --closure_lambda 1 --suffix _cl1, same for om+0.3).
- Weights: scripts/s9d_lambda.py <Z0 start .pt> --device cpu computes C0 (weighted momentum rows at Z0, no pin/closure/balance rows), b0 = E_ren^2 + (H_tot/int|h|)^2,
  lambda_k = sqrt(kappa_k C0 / b0) for kappa 0.1, 1, 10, 100 (fixed from Z0), writes reports/s9d_lambda_<job>.json and prints the four chained lines:
      scripts/enqueue_continuation.py --src <Z0 or previous step end state> --tag s9d --L 6 --Nk 16 --channels 4,4,4 --chdeg 15,14,6 --closure_lambda 1 --nl_den all5far \
          --balance_lambda <lambda_k> --core_pin auto --nonaxi_pin auto --max_iter 100 --time_limit 5400 --exclusive --priority 12 --suffix _k<kappa>
  Stop after the first step whose holdout rho_u^max exceeds 3x Z0's on either family, or after both |E_ren| <= 0.05 and |H_tot|/int|h| <= 0.05. Readings per step:
  R10 (a)-(e) against Z0, holdout on both families, E_ren, H_tot/int|h|, K_E and K_H ratios, sampled Q_sw, e_core, e_F, N_core, N_F, max E_F and its radius; the curve
  goes into the failure map. Test run on the S11 weight-1 smoke end state (CPU, 17:28Z): reports/s9d_lambda_s11smoke_L6_cl0.45_om+1.0_fixed_cl1.json.

## S10 primal versus curl formulation (lead 10:54Z, registered before data; R11; about 4 GPU-h)
- The worker's 'both' formulation adds the vorticity rows R_Omega (weight both_weight) to the momentum rows R_u with the full-space pressure; everything else
  (SPEC channels, closure rows 1e-3, all5far weighting, tail constraints, fixed c_l and omega) unchanged. From nest6 (0.45, 1) p0 and nest6 (0.45, 0.3) p0
  at L6 (and the L8 rungs if they pass R1), 300 iterations:
      for w in 1 10; do scripts/enqueue_continuation.py --src runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt --tag s10 --L 6 --Nk 16 \
          --formulation both --both_weight $w --channels 4,4,4 --chdeg 15,14,6 --closure_lambda 1e-3 --nl_den all5far --max_iter 300 --time_limit 7200 --exclusive --priority 12; done
      (the same with --src runs/nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0/starts/start_000.pt)
  Job ids s10_L6_cl0.45_om+1.0_fixed_both1 and _both10. MEMORY (smoke 11:22Z): at chunk 512 the both formulation at L6-ext OOMs on a whole A100 (77.7 GB in use at
  the first Jacobian; momentum-only runs use 23-45 GB); add --chunk 128 to every S10 line: at chunk 128 the first iteration takes 17.3 s (Jacobian) against 9.5 s momentum-only and the job sits at 51 GB after it (smoke 12:01Z; the end-of-start battery adds about 20 GB), so an S10 run at L6-ext costs about 1.7 GPU-h per 300 iterations, exclusive (smoke 12:25Z: 20 s per iteration; after 3 iterations holdout 1.36x the start, sigma_Om 0.41 -> 0.30).
  Time per iteration: Jacobian 12.1 s against 9.5 s for momentum-only at chunk 512 (first iteration). At L8-ext the both formulation is likely infeasible on 80 GB. Reading R11 on a fresh holdout with the full-space pressure.
## S11 asymptotic coefficient equations (lead 10:54Z; R12; about 4 GPU-h)
- Closure rows: the rows are closure_lambda / ||G_required|| times sqrt(w_a) (G_carried(b) - G_required[F])(n_a) for every Gauss node n_a of the (2L+10) x (4L+18)
  angular grid and every Cartesian component, i.e. the FULL VECTOR equation on the sphere (3 x Na rows, Na = 924 at L6), not a projection; G_required is the
  lagged target recomputed from the current leading tail after every accepted step (problem.py _init_closure / update_closure / closure_rows). Weights used so
  far: 1e-3 (19 jobs) and 1e-2 (one job, d6w3_L6_cl1e-2: holdout 0.0523 / 0.0704, mismatch 0.006); 1e-1 and 1 are untested (smoke job s11smoke measures the first
  LM steps at weight 1). Ladder 1e-3 -> 1e-1 -> 1, each 300 iterations from the previous end state, from nest6 (0.45, 1) p0 and nest6 (0.45, 0.3) p0:
      scripts/enqueue_continuation.py --src runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt --tag s11 --L 6 --Nk 16 --channels 4,4,4 --chdeg 15,14,6 \
          --closure_lambda 1e-1 --nl_den all5far --max_iter 300 --time_limit 7200 --exclusive --priority 12 --suffix _cl1e-1
      then --src runs/s11_L6_cl0.45_om+1.0_fixed_cl1e-1/starts/start_000.pt --closure_lambda 1 --suffix _cl1 (the same chain from the (0.45, 0.3) p0 start).
  SMOKE (11:59Z, 3 iterations at weight 1 from nest6 (0.45, 1) p0): m 0.346 -> 2.5e-4, K_E ratio 1.0003, K_H ratio 0.9999 at holdout 0.0569 / 0.0538 (1.24x / 1.16x
  the start), balances unchanged; about 10 s per iteration, 73 GB at the diagnostics (exclusive). The weight-1 rows are therefore usable directly.
  The worker records m, the F-component and the orthogonal norm of the defect (G-CLOSURE and FAR HELICITY lines, ledger fields G_carried_mismatch_rel,
  G_defect_F_component, G_defect_orth_rel, G_defect_parallel_rel, K_ratio_direct, K_H_ratio_direct) for the R12 reading.

## S12 radial-lambda rows (lead 11:27Z, registered before data; R13; about 4 GPU-h from the reserve)
- Implemented (Problem option radial_lambda_w; tests/test_S12_radial_rows.py PASS): rows sqrt(w) sqrt(w_k) sc_k <U.R_u>_k / <|U|^2>_k^(1/2) on all Nr radial
  training nodes, sc_k the fixed-gauge scaling and nonlinear shell weight of the momentum rows (sum of squares = w x the radial-lambda part of the weighted
  squared momentum residual). From nest6 (0.45, 1) p0 and nest6 (0.42, 0.3) p0 at L6, w = 3, 300 iterations, c_l and omega fixed:
      scripts/enqueue_continuation.py --src runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt --tag s12 --L 6 --Nk 16 --channels 4,4,4 --chdeg 15,14,6 \
          --closure_lambda 1e-3 --nl_den all5far --radial_lambda_w 3 --max_iter 300 --time_limit 7200 --exclusive --priority 12
      scripts/enqueue_continuation.py --src runs/nest6_L6_cl0.42_om+0.3_fixed_p0_om+0.3s12s0/starts/start_000.pt --tag s12 --L 6 --Nk 16 --channels 4,4,4 --chdeg 15,14,6 \
          --closure_lambda 1e-3 --nl_den all5far --radial_lambda_w 3 --max_iter 300 --time_limit 7200 --exclusive --priority 12
  Job ids s12_L6_cl0.45_om+1.0_fixed_rl3 and s12_L6_cl0.42_om+0.3_fixed_rl3. The worker's RADIAL LAMBDA line (share, pointwise share, lambda max, octave signs)
  on the training grid and the holdout rho_u^max give the R13 reading. SMOKE (12:48Z, w = 3, 3 iterations): share 0.740 -> 0.485, holdout 1.05x / 1.10x, E_ren -1.54 -> -1.38;
  10 s per iteration (no measurable cost); the lines above are usable as written.

## S8 pinned artificial-viscosity ladder (12 GPU-h after the gate; the lead decides; every state labelled viscous)
- d6t_L6 with omega fixed and the core RMS pinned: --nu 6.5e-4, 1e-3, 2e-3 (--core_pin auto, --pin_c_l not needed with fixed parameters), 300 iterations, about 0.5 GPU-h each.

## S5 (R_0 variation within E1, cheap) and S2/S3 probes (about 6 GPU-h)
- R_0 variation: the nest6 (0.45, 1) p0 configuration re-run with R0 0.15 and 0.6 (new enqueue_stage1 configs; exact embedding not available across R0: random starts
  at L4 with the nest seeds, then the L6 rung). S2/S3: scripts/s2s3_prototype.py on each S1 product (field-norm singular values and GMRES counts, 1 GPU-h per level).

## Queue policy for the gate window (23:09Z)
- Before the gate: the exclusive queue (s9b L6, s1nk Nk32/Nk24-om1/Nk32-om1, s1g/s1l/s1m L10) drains by about 15:00-18:00Z; scripts/release_lowprio.sh returns the 55
  parked L6 sweeps when a GPU would otherwise idle (Stage I discovery starts; non-exclusive, 2-3 per GPU).
- At the gate: park the remaining low-priority sweeps again (queue/hold_lowprio) and enqueue the S1/S4/S9b items above at priorities 15/12-13/14.
