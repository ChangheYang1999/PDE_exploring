# START_HERE_NEW_RUN.md (numerics lane c4-num) — updated each shift (last 2026-10-25T07:40Z)

## 1. Where things are

| Item | Path |
|---|---|
| Original READ-ONLY handoff (protected; never written, never executed) | `@SOURCE_REALPATH@` |
| Task prompt (protected copy and lane copy) | `.../case4/IPM_case4.prompt.md`, `c4-num/PROMPT.md` |
| Independent working copy (cp -a, 217 files, checksums equal, 0 symlinks) | `@WORK_REALPATH@` |
| Outputs (checks, qualification, diagnostics, tests, manifests, campaign) | `@OUTPUT_REALPATH@` |
| Python environment (3.9.25, numpy 1.23.5, scipy 1.9.3, psutil 6.0.0, threadpoolctl 3.6.0) | `@NUM_DIR@/env` |
| New 860 code (versioned modules outside the frozen closure) | `@WORK_REALPATH@/research860` (pre-G2 drafts; rewritten after release) |
| Team contract and gates | `c4-lead/SPEC.md` (v5), `c4-lead/NOTES_FOR_TEAM.md`; verifier `c4-ver/VERIFY_REPORT.md` |
| Lane reports | `LINUX_QUALIFICATION.md`, `BASIS_860_IMPLEMENTATION.md`, `EMBEDDING_TESTS.md`, `OPTIMIZATION_860_LOG.md`, `RUNBOOK_860.md`, `RESULTS_860.md` (after the run), `NUM_REPORT.md` |

## 2. Verified understanding of the handoff (what the code actually does; verified items marked)

- PDE: (c_l X + U).grad rho = rho, U = (-psi_y, psi_x), -Lap psi = rho_x on the plane; rho even in x, odd in y, rho = y f.
  Potential chi (even-even): psi = chi_xy, rho = -d_y Lap chi, so Poisson holds identically; canonical whole-plane
  inverse without free harmonic strain (verifier: uniqueness proof and Green quadrature CONFIRMED).
- Residual R_f = w_x f_x + w_y f_y + q f, w_x = c_l x - psi_y, w_y = c_l y + psi_x, q = c_l - 1 + psi_x/y with analytic axis
  extensions; R_rho = y R_f. Objective J_abs = (pi a_ref^2)^{-1} int int R_f^2 dr/r dtheta, a_ref = 23.95065822465609 fixed;
  training residual r_i = sqrt(2 w_i/(pi a_ref^2)) R_f(X_i) on a frozen three-block 90,624-node log-radius mesh
  (origin r = 0.02 u, middle log r in [log 0.02, 16], infinity r = e^16/u); refined mesh 241,664 nodes.
- Basis (verified in source): 24 core generators H_m R^{A - m - sigma_s}, sigma in (0, 1, 2, delta, 2 delta, 3 delta),
  A = (3 + 1/c_l)/2, delta = (1 - 1/c_l)/2, m = 0..3; 162 Global generators H_m R^{A-m} t^{max(5-m,0)} N_n P_n(2t - 1),
  m = 0..8, n = 0..17 minus (3,0), plus (9,0); N_n = exp(-lognorm/2) from SciPy gammaln (binary64, up to 25 ulps from
  sqrt(2n+1) on this host). c0 is eliminated analytically from the center condition psi_xy(0) = 1 - c_l at Decimal
  precision 90; the five Taylor compatibility equations E_x, E_y, D_1, D_2, D_3 are solved by an implicit chart with
  coefficient-only normal corrections (c_l bit pattern preserved), leaving 19 + 162 = 181 feasible variables; c_l and
  a_0 = f(0) are both free; bounds 1.02 <= c_l <= 10, |c_j| <= 100 on the 23 core coefficients only.
- Fields for r <= 0.02 come from order-20 Decimal Taylor polynomials (production) and orders 20/24 (checks); the
  independent whole-axis integral uses an analytic origin integral, an 85-digit overlap check, an outer envelope with
  interval expansion, Gauss radial orders 16..128 and two angular rules; epoch policy: absolute target 2.5e-15,
  relative accuracy 2.5e-7, initial upper log radius 44.
- Optimizer: column scales = inverse initial column norms; full thin SVD (gesdd) of the 90,624 x 181 scaled Jacobian; trust
  step q_i = -s_i (U^T r)_i/(s_i^2 + l^2) with a long-double secular solve; every positive singular direction kept;
  acceptance requires training decrease > 128 eps J, gain > 0.1, fresh independent integral with uncertainty <= 5% of the
  prediction and independent decrease > uncertainty; radius x0.25 if gain < 0.25, x2 if gain > 0.75 and step > 0.8 radius;
  durable snapshots/proposals/outcomes/commits; recovery requires the strict 64-eps replay of the saved residual.
- Authoritative state accepted278 (SHA-256 812d3446...e955): c_l = 1.8089923602744993, a_0 = 14.767729990606481,
  J_abs = 4.2683726070948805e-09, frozen E_f max 1.23849639744e-4, E_rho max 7.16582921424e-5, max Taylor defect
  4.888e-14; 278 accepted of 317 trials; campaign stopped on its 24-hour budget, not at a stationary point (verified
  descent in seven directions); the unnormalized density residual grows like r^{0.1055878642} with leading coefficient
  L2 norm 0.4403534214951 (verifier CONFIRMED); omitted E_1 fraction above harmonic 19 is 0.14464 percent for accepted278
  (the 0.145222 percent figure belongs to accepted165).
- No exact PDE solution, stationary optimizer, basis convergence or supremum certificate exists.

## 3. What happened in this run so far (details in OPTIMIZATION_860_LOG.md and LINUX_QUALIFICATION.md)

- 03:04-03:06Z: before-integrity manifest, copy, environment, standard-library checks: PASS.
- 03:06-03:12Z: guarded smoke and objective PASS; strict 64-eps replay FAIL (2.1727e-15 vs 1.3130e-18), preserved as FAIL
  (cause not uniquely isolated; see LINUX_QUALIFICATION.md 4b-4d).
- 03:15-03:54Z: old-code derivative/provider benchmark PASS; independent 32-region assessment PASS; per-node rounding model
  PASS on the predeclared raw-envelope criterion; Haswell diagnostic.
- 03:21-03:37Z: pre-G1 860 drafts written and partly run (disclosed; inadmissible; superseded by SPEC v4/v5 decisions).
- 03:40Z-: documentation (design v2, test plan v2, runbook skeleton, manifests) while waiting for the G1/G2 release.
- 04:00Z G1 released. 04:00-07:15Z (shift 1): 860 library written to the lead's SPEC v4-v9.3 (basis860, origin860, hp860, chart860, fields860,
  model860, integrate860, farfield860, assess860, campaign860, bench860); g2_v1 chain (T0-T3 PASS on the first evaluator), verifier found two
  production-accuracy defects (origin truncation, far-field cancellation) and the lead ordered the longdouble R_f path, exact exponent
  differences and falling-factorial radial jets (SPEC v9-v9.3); g2_v3 failed its own R_f gate; the repaired library passed the dev check.
- 07:28Z (shift 2): g2_v4 base manifest 6f0cf834 frozen and its chain run in parallel guarded sessions; supplements g2_v5 (corrected T0/T1),
  g2_v6 (T2.7H-X2), g2_v7 (T2.7H floor sidecars), g2_v10 (SPEC v9.7 rounding calibration: rho_max 48.37, kappa 2048); every step PASS under the
  strict verdict (runner v5+: JSON passed and every check), except g2_v4 t0t1 (superseded by g2_v5 t0t1v2), the g2_v4 supplement (one stale
  check; superseded by supplement v2) and two harness failures (g2_v8/v9 kappa, no result). Seed reproduction (t3): training residual relative
  3.3e-11, max |dR_f|/a_ref 7.5e-15, refined 3.2e-11, frozen32 E_f/E_rho 3.0e-12 relative, replay strict 64 eps in a fresh process; replay
  reference seed_860_replay_v3.npz (sha ee2ba0af...). Table: outputs/g2/G2_SUMMARY.md.
- 07:40-09:50Z: the lead's rulings SPEC v9.5-v9.16 and audit items S1-S8 implemented in the pending G3/G4 files (campaign driver v3 with F1-F22,
  acceptance arithmetic, kappa file, assessment gate, boundary metrics; farfield860 v3 exact rational engine reproducing the verifier's eight
  exact cases; assess860 v2 with completeness, spot checks and stratified nodes; supervisor v3; 29 driver fixtures and 20 far-field fixtures pass).

- 10:50Z G2 RELEASED (lead; verifier concurrence). 10:50-12:45Z: pre-freeze items applied; 12:45Z G3 frozen as manifest g3_v1 (fcedf098...).
- 12:50Z-17:10Z (shifts 2 and 3): T4 (feasible chart gate) s1 stopped on the lead's budget order (13:31Z, no verdict); T4 s3 (13:32Z-17:09Z) strict
  FAIL 27/29: only the finite-difference rows on the three weakest right singular vectors fail (||A v|| 2.5e-15 to 3.6e-15 at the eps*sigma_max
  floor 2.1e-15; absolute discrepancies 5.5e-12 to 2.4e-10, below the passing low tangents'); every other check passes (C5 ranks 5/6, tangent 55,
  complete 60, 855 feasible variables = c_l + 59 low - 5 Taylor + 800 high, all 855 singular values positive, zero step bitwise, dilation tangency
  3.8e-19, 23 FD directions 2e-16 to 1.9e-10). Lead ruling T4-R1: recorded exception E-T4.5w, no rerun, G3 proceeds; verifier concurred.
- 13:25-14:11Z item F: development assessment of the seed at 8 workers from the frozen layout PASS (not evidence; 2747 s).
- 17:13-18:21Z bench s2 (4/8/12 workers): (4,4) child record written, then stopped on the lead's order (12 workers would exceed the RSS-sum guard).
- 18:22-22:20Z bench s4 ((8,4) only): child record 0d49876d (every child-level check passes; rejected trial 864 s, accepted 986 s with one Jacobian
  assembly; integral 649 s; cache rebuild 208 s; SVD 18 s), assess_0 4539 s, spot_0 485 s, assess_1 4106 s, spot_1 360 s (both assessments tight
  J_abs 4.268372607095638e-9); then the guard stopped the step on the box-wide CPU load ceiling (1-minute load 145.67 on 96 CPUs; the samples show
  the trigger, not its source): strict FAIL (no bench.json). Lead ruling G3-R2 / exception E-G3.B: no rerun (time-budget tradeoff), G3 proceeds on
  the written records. ETA computed from the child record: outputs/g3/eta/eta_child_w8_t4_g3v1_20261024T225012Z.json (RESULTS_860.md section 4).
- 22:55Z seed replay check under the guard PASS bitwise (outputs/dev_v9/replay_seed_check_20261024T225135Z.json).
- 23:04Z g4_v1 frozen (lead word G4-F1; verifier concurrence): exact supplement of g3_v1 adding bin/supervise860_v4.sh (POLICY line, two exit-code
  fixes) and outputs/campaign860/campaign_policy_v3.json (max_family_rss_mib 170997 = ceil(1.3 x the 131536 MiB RSS-sum peak), max_seconds 6600);
  manifest outputs/manifests/code_manifest_g4_v1.json sha256 0481a8ae...; lead and verifier readbacks PASS; ACTIVE_MANIFEST written 23:08Z.
- 23:11:06Z G4 PILOT LAUNCHED (lead word G4-L1): root outputs/campaign860/pilot_g4_v1, supervisor pid 3601953, slice 3300 s, 8 workers,
  max-trials 12 per slice; the cadence seed assessment runs first (about 75 min under the present load), then the trials.

- 2026-10-25T00:16Z to 01:19Z (shift 4 end, shift 5): the v1 pilot's seed assessment PASSED (3928 s; J_abs 4.268372607095638e-09, 5070 leaves identical
  to the g3 reference) and slice 1 initialized from the seed (seed replay bitwise), but the campaign worker DEADLOCKED at nearly every fork-pool exit:
  the pool children inherited the driver's flag-only SIGTERM handler, so Pool.terminate's SIGTERM was swallowed and the parent's join hung
  (outputs/diag/pilot_hang_20261025T0050Z.md). Under the lead's rulings (00:53Z option A, S1 01:03Z, addendum 01:07Z, S1-b 01:14Z) six targeted
  SIGKILLs of the idle pool child only (two by hand, four by a watchdog; records outputs/diag/interventions) let slice 1 end (0 trials) and slice 2
  run ONE ACCEPTED TRIAL (J_abs 4.2684e-9 -> 3.8583e-9; supporting fact, not pilot evidence); the STOP file then closed pilot_g4_v1 at 01:19:29Z
  (guard success, 871.9 s). Whole-family exit confirmed; watchdog stopped 01:20Z.
- 01:22:05Z the one-line fix (os.register_at_fork resetting SIGTERM/SIGINT in forked children; lead test 0 hangs in 690 pool exits vs 38 in 250 without)
  was installed in work/research860/campaign860.py (67fa6127...) and frozen as manifest g4_v2 (outputs/manifests/code_manifest_g4_v2.json dacb2036...,
  byte-equal to the lead-read and verifier-concurred preview; one row changed out of 111, closure identical); ACTIVE_MANIFEST -> g4_v2.
- 01:26:13Z pilot_g4_v2 LAUNCHED (lead launch word G4-L2): root outputs/campaign860/pilot_g4_v2, supervisor pid 70811 (nice 19, cores 78-89),
  slice 3300 s, 8 workers, max 12 trials per slice, no watchdog (a hang means STOP and report). The seed assessment runs first and must reproduce
  the v1 record exactly (outputs/dev_v9/compare_seed_assessment.py); then the trials. Trial 1 is compared with the v1 trial as a reproducibility fact.

- 02:19Z to 06:00Z (shift 5) pilot_g4_v2 ran five slices under manifest g4_v2 without a single pool-exit stall: seed assessment PASS (5070 leaves identical,
  J_abs 4.268372607095638e-09, 3210.8 s), initialization replay bitwise, 11 trials (10 accepted, 1 rejected), J_abs 4.2683726070956366e-09 ->
  6.465329645424404e-10 (-84.9 percent), c_l 1.8089923602744993 -> 1.8086138839289845, a_0 14.767729990606481 -> 14.284323569735315, trust radius
  4.62e-05 -> 2.96e-03 (one cut after the rejection); every step radius-limited; the gain ratio fell from 1.0 to about 0.55 to 0.69 as the radius grew.
  Cadence assessment of state 6 (the first halving) PASS 04:50Z: sampled E_f 7.0869e-05 (seed 1.2385e-04), E_rho 7.0869e-05, far field still grows
  (exponent 0.105589, E1 0.43547, E2 6.3673, E3 31.7514; unresolved E1 fraction 0.65 percent). The second-halving assessment of state 10 started 05:59:49Z.
  B2 strict replay of accepted state 1 with the g4_v2 manifest: bitwise PASS. B8 restart tests PASS on the lead's read with recorded deviations: SIGTERM
  between trials (04:53:31Z, honoured at the trial boundary 714.5 s later, process fault #1, bitwise resume) and SIGKILL inside a trial (05:22:37Z,
  worker-only kill with no live pool child, guard -9, process fault #2 with 120 s backoff, bitwise resume of state 8, interrupted trial 9 re-proposed and
  then rejected). Helpers: bin/pilot_signal_test.sh (v2, TERM) and bin/pilot_signal_test_v3.sh (v3.1, KILL; mock fixture outputs/mock_b8). Slice-2 wall
  growth (x1.45 in every phase) was diagnosed as box contention (load median 66 vs 37; hyperthread siblings 30-41 busy), not more integration work; the
  run-wide reserve rule (1.5 x the longest iteration, now 1404 s) limits a 3300 s slice to 2 or 3 trials. ETA bullet in NUM_REPORT.md.

- 07:11Z to 07:27Z (shift 6) pilot closed and G5 started. Trials 12 and 13 (slice 6) accepted: J_abs 6.4653e-10 -> 5.9074e-10 -> 5.383513548861579e-10
  (-87.39 percent vs the seed), gains 0.695 and 0.692 at the held radius 2.96e-03, c_l 1.8084187435903094, a_0 14.082433713156986, five-Taylor 1.48e-13.
  Verifier B1-B12 concurrence 07:08:26Z; lead G5 release word 07:13:26Z. Checklist C2a: STOP 07:14:38Z while slice 6 ran (live worker confirmed), slice 6
  ended stopped_by_request 07:22:07Z after trial 13 committed (guard success, bound completion record, supervisor exit 07:22:09Z, no end assessment),
  process absence confirmed 07:22:59Z, STOP renamed STOP.pilot_end_20261025T072421Z, relaunch 07:24:21Z with G5_READONLY_CODE=1 (supervisor 1270876,
  slice 7 guard 1271208 / worker 1271246, continuation replay bitwise 07:26:47Z, event 30). Pilot totals: 6 slices, 13 trials, 12 accepted, 1 rejected;
  three cadence assessments PASS (seed, state 6, state 10). ETA records outputs/g3/eta/eta_observed_g4v2_20261025T072834Z.json (3300 s) and
  eta_observed_g4v2_g5slice5000_20261025T073010Z.json (5000 s: 5 trials per slice, 4.96 trials per hour, about 118 trials per 24 h at the observed
  median iteration wall 679 s and acceptance 12/13; a compute-budget rate, not a convergence time).

- 07:24Z to 13:26Z (shifts 6 and 7) G5 long run: slices 7, 8, 9 and 10 completed (6 trials each, every trial accepted, each ended at the 1404 s time
  reserve after 3697 to 4130 s of worker time; family peak RSS 132.9 GB of the 167 GB policy cap); cadence assessments of state 18 (third halving,
  09:28:46Z, 3328 s) and state 30 (fourth halving, 12:24:05Z, 2834 s) PASSED (mode full, no scientific stop). Totals at 13:26Z: 37 trials, 36 accepted,
  1 rejected; J_abs 4.2683726070956366e-09 -> 1.017457918946082e-10 (-97.62 percent); c_l 1.8089923602744993 -> 1.807387412602369; a_0
  14.767729990606481 -> 11.760147456794964; radius fixed at 2.96e-03 since trial 10 (every step on the radius; gain ratio drifting down 0.735 at trial 28
  to 0.567 at trial 37; the relative decrease per step 0.068 -> 0.045). Far-field monitor (production exact engine) at every accepted state: leading
  density exponent positive and slowly rising (0.105588 -> 0.106550 at state 34), E1 0.4404 -> 0.2103 with its part above harmonic 19 rising 0.14 -> 2.94
  percent. Sampled E_f = E_rho maxima: 1.2385e-04 (seed, x axis r 8.7) -> 3.6931e-05 (state 18, y axis r 388) -> 2.7704e-05 (state 30, y axis r 53).
  Verifier finding 12:52Z (state 30): the unweighted training-indicator diagnostic of assess860 has exact counterexamples at 5 of 90624 nodes (ratios
  1.03 to 1.09; the weighted indicator and the exact J_abs enclosures hold there); lead diagnosis 13:06Z: a deweighting round trip (divide by the
  binary64 root weight) that the denominator does not allow for; continuation ruling: the run continues unchanged, no code or threshold change, and a
  stop raised by a later assessment's own nodes stands (pre-registered diagnosis). Slice 11 started 13:25:50Z (bitwise continuation of state 36).
  Helpers added in shift 7: bin/trial_line.py, bin/trial_apply.py, bin/slice_line.py (readers; RUNBOOK G5 section).

- 13:26Z to 19:08Z (shift 7) G5 long run: slices 10 to 14 completed (6, 6, 6, 5, 6 trials; every trial accepted; each ended at the 1404 s time reserve;
  slice 13 held 5 trials under box load 59 to 94); the fifth halving assessment (state 48; the sixth full assessment counting the seed) PASSED 16:26:23Z
  (3197 s; tight J_abs 6.235589145742595e-11; sampled E_f = E_rho maximum 1.9342e-05 at (0, 64.0); far field grows, exponent 0.106642; spot worst
  ratios 0.19 / 0.42 / 0.45, no failure). Trials 36 to 60 accepted; J_abs 1.0175e-10 -> 4.460894019569721e-11 (-98.95 percent); c_l fell at every
  accepted step through state 50 (1.807265544140473) and rose at every step since (observation about the iterates only); gain ratios rose from 0.528
  (trial 45) to 0.758 (trial 60), so trial 60 doubled the trust radius to 5.9132e-03, the first change since trial 10. Endgame documents for the lead
  (data cut 2026-10-26T04:00:00Z for FINAL): E3_STANDALONE_ASSESSMENT_FEASIBILITY.md (one standalone full assessment of the handoff state, option A,
  lead-approved, launcher bin/launch_handoff_assess.sh 8ff6b218 with window 04:00:00.000Z to 04:45:00.000Z, once) and HANDOFF_860.md (handoff of the
  running process; refreshed at the cut). Readers added: bin/assess_stop_read.py, bin/read_assessment_record.py, bin/overlap_report.py,
  bin/handoff_refresh.py, bin/eta_observed860.py (start-rule equality fix).

- 19:08Z onward (shift 8): trial 61 at the doubled radius REJECTED (the step would have raised J_abs to 4.7013e-11; radius cut to 1.4783e-03), trial 62
  ACCEPTED at the quarter radius (gain 0.979; radius doubled back to 2.9566e-03), trial 63 ACCEPTED (gain 0.717; radius held). State 61 at 19:16:17Z:
  J_abs 4.2996321175788723e-11 (-98.99 percent), c_l 1.8074856465827522, a_0 10.55038494125898. Far-field monitor to state 60: exponent 0.1065340
  (maximum 0.1066442 at state 50, falling slowly since), E1 0.14345 with 0.005034 above harmonic 19 (3.51 percent; the absolute part has fallen since
  state 35, the fraction still rises). HANDOFF_860.md v5 refreshed from one read at 19:17:07Z after the verifier's v4 readback; new reader
  bin/handoff_walls.py.
  Later in shift 8 (to 01:07Z): trials 64 to 88 (slices 15 to 19 completed, slice 20 started 00:15:14Z); J_abs 3.2110341773115295e-11 at
  state 78 (-99.25 percent), c_l 1.8081490120721955, a_0 10.365533489110437; ten rejected trials in all (9 and every step proposed right
  after a doubling since trial 60: 61, 65, 68, 71, 74, 77, 80, 83, 86), a radius cycle 2.9566e-03 (accepted, gain above 0.75, doubled) ->
  5.9132e-03 (rejected, quartered) -> 1.4783e-03 (accepted, gain 0.98, doubled back) documented in RESULTS_860 section 5 as an observation;
  quarter-radius steps 75, 78, 81, 84 carried five-Taylor maxima 1.0e-12 to 3.0e-12 (gate 1e-10; recorded, no cause claimed). Far-field
  monitor to state 78. HANDOFF_860.md is now GENERATED: bash bin/handoff_read.sh (retained read with reader hashes before and after, values
  JSON, ETA record) then bin/handoff_apply.py <values.json> <read.txt>; eleven revisions after verifier and lead readbacks (v11 ae1dff63 at
  00:12Z read); it carries the cut rule for the handoff state, the stopped-state behaviour, the disk-floor behaviour and the measured
  throughput. DISK: @BUILD_VOLUME@ free fell from 193 GiB (19:07Z) to 110 GiB (23:55Z) through other tenants, then rose to 124 GiB (00:15Z); the
  guard floor is 10 GiB; if the floor stops the run nothing is relaunched (lead contingency 22:43:18Z). Lead session c4-lead-26 from 20:47Z.

Shift 9 (2026-10-26T01:04Z onward). The long run continued unchanged: slice 20 (00:15:14Z to 01:27:48Z) committed trials 89 to 94 (4 accepted; states 79 to 82; J_abs 3.012936296667831e-11 at state 82, -99.29 percent below the seed; c_l 1.808308265463122, a_0 10.33688083145218). The sixth halving threshold 3.1177945728713005e-11 was crossed at trial 91 and the cadence check at the slice-20 end started the SIXTH HALVING ASSESSMENT at 01:27:55Z on state 82 (guard run 20261026T012755Z_1792978075405207207_g5_assess; record assessments/assessment_J_abs_halved_1792978075566889128.json). The handoff generator (bin/handoff_values.py, bin/handoff_apply.py) was revised to version 3 and then version 4 (after the verifier's source findings of 01:27Z: unknown-time events, the launcher comparison in every branch, exact nanosecond cut comparisons) for the lead's review of HANDOFF v11 (c4-lead/reviews/handoff_860_v11_review.md e8493447; findings 1 to 7): supervisor identity by process arguments; the run in progress identified by the live guard of running.json bound to its run directory (eleven checks including creation-time consistency and PID-reuse protection); values restated at the 04:00Z cut when the read is after it; no None budget dates; a failed cut rule handled; the launcher dry run compared with the generator. HANDOFF_860.md v13 (e7930279) was generated from the retained read outputs/handoff_reads/refresh_20261026T012025Z; the earlier versions and scripts are kept under outputs/handoff_reads/. The far-field monitor was extended to states 79 to 82 (RESULTS_860 5a). Box memory-pressure episodes from other tenants (PSI full avg10 36.65 at 01:18Z and 45.62 at 01:21Z, run guard ceiling 60.0) did not stop the run. Endgame executed in this shift: the data cut 2026-10-26T04:00:00Z fell in slice 22; the paired v7 read at 04:00:05Z made HANDOFF_860.md v14 (55f1fe5d) and named the HANDOFF STATE by the exact cut rule: accepted state 88 from trial 103 (event 154, committed 03:48:47Z; accepted_00000088.json 70b06bc6c95869a2ef0bf5dcc6e8bdfc605fab4399a89752dc89b8346abfa4ab; J_abs independent 2.7441060958610147e-11, 99.36 percent below the seed; c_l 1.8085383949271123, a_0 10.29757491765872); at the cut 104 trials, 88 accepted, 16 rejected; the launcher dry run in the same read selected the same event. E3 (one standalone full assessment of the handoff state, lead option A) was launched once at 04:00:37Z by bin/launch_handoff_assess.sh (claim 04:00:37.549872994Z; guard 497965, assess860 498011, 8 workers, cores 78 to 89) and finished at 04:56:39Z with success: record outputs/handoff_assess/20261026T040037Z_state88/assessment_state88.json (sha256 8eed6fd2c3d7276900a4514b7ec0298297f2c743eac2f568baf4521a6a1642e4), mode full, complete, no scientific stop, tight J_abs 2.7441060958610037e-11, sampled E_f = E_rho 1.2197e-05 at (0, 74.3), spot worst ratios 0.150, 0.301, 0.305, far-field exponent 0.1058654 (the unnormalized residual still grows), E1 0.12113 with 3.33 percent above harmonic 19; guard wall 3362 s, peak 18.4 GiB; the long run was not touched and its reserve stayed 1404.159 s. The post-E3 refresh (paired v8 read 05:03:02Z) made HANDOFF_860.md v15 (70e06d2c). The generator went through versions 3 to 8 during the shift after lead and verifier reviews (bin/handoff_values.py 14cc3eed, bin/handoff_apply.py 4889003f at the end; every replaced version kept under outputs/handoff_reads/ except 76a529c3, which the verifier reconstructed). States 89 to 93 (trials 105 to 111) were accepted after the cut and are not in FINAL. Lead FINAL by 08:00Z; the campaign loop cap is about 15:03Z.

## 4. Next steps (state at 2026-10-25T19:21:48Z)

G5 runs detached and unchanged (supervisor pid 1270876, slice 15 since 18:43:51Z; the lead's continuation ruling of 13:06:30Z stands: never touch the
run, a stop raised by an assessment's own nodes stands and is reported, relaunch nothing). The sixth halving assessment is due when an accepted J_abs
is at or below 3.1177945728713005e-11 (half of the ledger row's validated J_abs of state 48) or at 100 accepted trials: at the present 1.7 percent
decrease per accepted step about 19 more accepted steps, roughly 3.5 hours of slice time from 19:16Z (about 22:45Z to 23:30Z), or about 02:30Z by the
100-trial rule; it runs between slices and takes 47 to 67 minutes. Endgame (lead ENDGAME PLAN): the data cut for FINAL is 2026-10-26T04:00:00Z; the
shift covering 04:00Z to 04:45Z launches the one standalone assessment of the handoff state with `bash bin/launch_handoff_assess.sh` (dry run first;
once; never relaunch; report its LAUNCH.md and, within 30 minutes of its end, its record) and refreshes HANDOFF_860.md (section 11: handoff_refresh.py,
handoff_walls.py, the launcher dry run, a retained process read with a captured timestamp) with its final sha256 to the lead before 05:00Z. The 48 h
minimum of genuine campaign work is reached at 2026-10-26T03:05Z at the earliest; the shift loop cap is 2026-10-26T15:03Z. The last shift must leave:
RUN_STATUS, NUM_REPORT, RESULTS_860 (sections 4a, 5, 5a, 5b), the ETA record, artifacts/ rebuilt, and the verified PID / log / checkpoint facts of the
running process.

Earlier "Next steps" text (13:33Z) follows: G5 runs detached (supervisor pid 1270876, slice 11 since 13:25:50Z); the fifth halving assessment is due
when an accepted J_abs is at or below 6.804395e-11 (about 10 or more accepted steps from 13:26Z, roughly 2 to 4 hours of slice time; a stop from its own
spot-rule nodes would stand and must be reported, not relaunched).

Earlier "Next steps" text (07:40Z) follows.
### Earlier next-steps text (state at 2026-10-25T07:40Z)

G5 is running: the long run continues detached on the pilot root outputs/campaign860/pilot_g4_v2 (supervisor pid 1270876, label g5, 5000 s slices,
8 workers, no trial cap, manifest g4_v2, code directory read-only) since 07:24:21Z, resumed bitwise from accepted state 12 (J_abs 5.3835e-10). Each
shift: health check by process table and heartbeat, report every commit and slice end to the lead, read every cadence assessment row, refresh the
ETA (bin/eta_observed860.py <root> <out> --slice-seconds 5000 --reserve 1404), update NUM_REPORT / RESULTS_860 / OPTIMIZATION_860_LOG, rebuild
artifacts/. Safe stop is the STOP file while a slice runs; resume is the launch line of the RUNBOOK G5 section; no signals, no code change (a change
needs a new manifest, the lead's word and a new root seeded from the last accepted snapshot). The 48 h minimum of genuine campaign work is reached
at 2026-10-26T03:05Z at the earliest (verifier accounting); the run then continues under the supervisor until a STOP, a marker or the budget.

Earlier text (06:15Z) follows. The pilot continued detached (supervisor pid 70811) with no watchdog and no further signals. Open on the lead's side: the B1-B12 release of the pilot
and the G5 transition (RUNBOOK shift 4 section with v2 names; a G5 driver revision list R1/R2 sits in OPTIMIZATION_860_LOG.md and must not be applied
to the frozen pilot driver without a new manifest and the lead's word). Each shift: report every commit and slice end, the cadence assessment results,
refresh the ETA (bin/eta_observed860.py <root> <out> --reserve 1404), rebuild artifacts/.

The pilot root is now pilot_g4_v2 (manifest g4_v2); read "pilot_g4_v1" and "g4_v1" below as pilot_g4_v2 and g4_v2. The lead's checklist is B1-B12.

The pilot (G4) is running from the immutable 860 seed. Its pass criteria are the lead's checklist B1-B11 (c4-lead/reviews/lead_g4_checklist.md):
at least 10 trials with at least 3 accepted (or every rejection with a legitimate reason), zero-step equality at the seed and the first accepted
state (strict 64 eps replay, outputs/dev_v9/replay_snapshot_check.py with --manifest code_manifest_g4_v1.json), KKT <= 1e-8, converged C5 lifts with
raw C5 < 1e-10, logged predicted and measured decreases with consistent gain ratios, logged c_l/a_0/W_x/W_y changes, independent integration
uncertainty <= 5 percent of the predicted decrease, the manifest hash in every event, restart tests (SIGTERM between trials, SIGKILL inside a trial;
bin/pilot_signal_test.sh records PIDs and times; the lead's checks/pilot_lead_read.py reads the commits), a resource projection over at least 72 h
inside the 40 GB lane budget, and the verifier's re-evaluation of one accepted state. Then the G5 release and the pilot-to-G5 transition of
RUNBOOK_860.md (shift 4 section, checklist C2a): STOP while a slice runs, confirm the committed completion, rename STOP, relaunch the same root
with G5_READONLY_CODE=1, slice 5000 s, 8 workers, no cap. The long run then continues through the shifts; each shift records PID, heartbeat age,
last event, trials and accepted, best accepted J_abs, radius, disk and a refreshed ETA from the measured trial walls and acceptance rate
(bin/eta_from_bench.py gives the budget model; RESULTS_860.md section 4). Before the run ends: bin/make_artifacts.py rebuilds artifacts/.
Standing rules: no edit to any manifest-listed file; new files only; every launch under nice; every poll reads the process table; RUN_STATUS
before the shift ends; WORKLOG hourly. Time budget: the 48 h minimum of genuine campaign work is reached at 2026-10-26T03:05Z; the run cap is
2026-10-26T15:03Z.
