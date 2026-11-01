# Numerical experiments: far-field series of self-similar IPM

All paths are relative to this `numerics/` directory, and every command below is run from it. The report of these
experiments is `../FARFIELD_NUMERICAL_EXPERIMENTS.md` (top level of the artifacts folder). Requirements: python-flint 0.9,
numpy, mpmath, sympy.

## Contents
- code/ffcore.py: the far-field angular recursion (problem equations 3-5): rings fmpq (exact), arb (ball arithmetic), float;
  Poisson inverse with exact resonance handling (three statuses), products by polynomial multiplication, chi reconstruction,
  statistics in scaled arithmetic (log10 fields), checkpoints (pickle, exact dyadic midpoints and radii).
- code/run_recursion.py: command-line driver (tags, rings, precision, c_l as exact rational / 'sqrt5' / 'cand007', f_1 specs,
  --resume). Writes logs/<tag>.jsonl and ckpt/<tag>.pkl.
- code/logff.py: logarithmic (polynomial in log r) series at rational delta, canonical normalization B_(n,j)(0) = 0,
  arb or exact; fast block products by Kronecker substitution. Options: --edge K (edge-only, linearized variants of the
  canonical log recursion); --reset-radii (resume a ball computation from the midpoints of a checkpoint; the continuation is
  certified only relative to the loaded midpoints, and the per-order rows carry radii_reset_at); --perturb-radii SEED (resume
  with every ball displaced to a random boundary point, a sensitivity diagnostic).
- code/extract007.py: exact extraction of (c_l, f_1) from Candidate 007 and exact comparison with its stationary branches 2..8
  (reads the read-only source project; set IPM_PROJECT_ROOT to the directory that contains `source/combined1/`).
- code/check_chi_sympy.py: direct symbolic substitution of chi_N into the stationary equation (orders 1..4, three parameter sets).
- code/evaluate_series.py: section 13 evaluation (truncated sums, weighted stationary residual and derivative residual).
- code/fit_growth.py, analyze_log.py, logseries_table.py, hump_report.py, stream_increments.py, deficit_rates.py, tprofile.py,
  diagonal_bands.py, theoremA_compare.py, fixed_angle_ratio.py, pade_continuation.py: analysis tools (log-series hump, increments,
  per-deficit rates, t-profiles in ball arithmetic, diagonal-band decomposition). code/regen_log.py [--log]: recompute statistics
  from a checkpoint (pure or logarithmic).
- code/resonance_scan.py, resonance_report.py, prime_congruence_check.py, kappa_scan_arb.py, kappa_odd_check.py: exact (fmpq) and
  ball-arithmetic compatibility coefficients at resonances, exact odd-numerator coefficients and their p-adic digits.
- code/theoremE_constants_arb.py: ball-arithmetic certificate of the Theorem E constants with outward decimal rounding.
- code/tuned_c3.py, tuned_cQ.py, tuned_general.py: the tuned pure series of the theory at rational delta (Theorem T, T_Q,
  T_{Q,h}): free multipole constants fixed by the affine response (Lemma T.1), certified-zero obstructions, interval-Newton root
  enclosures; validated against the exact H_6..H_15 and sigma_k of the theory part. tuned_general.py --f1-single M: tuned series
  with a single-harmonic leading profile eps sin(M theta) (centers of Corollary T_(Q,h).9).
- code/report_order.py, slopes_q.py, crosscheck_float_arb.py, lead_stream_ratio_modes.py (copy of the theory part's
  stream_ratio_modes script), merge_logs.py (merge the certified log <= 329 with a continuation log), table_511b.py (section 5.11b
  table), tuned_summary.py TAG (one-line summary of a tuned run), period3_decrements.py LOG n_from n_to (3-order decrements of the
  2/3 log sums), drift_fit.py (three tail models of the period-3 multiplier), cycle_diag.py, compare_pert.py,
  onestep_edge_error.py, single_slopes.py TAG n0 n1 (per-order slopes of a tuned run), export_coeffs.py (coefficient exports).
  code/test_products.py, fast2_test.py, resume23_test.py: internal tests.
- jobs/: the shell scripts with the exact command lines of the runs (records; they assume this directory layout).
- logs/: per-order statistics of the main runs (JSON lines; field names in section 1 of the report), and the printed outputs
  (.out) of selected runs.
- notes/: data tables: cand007_f1.json (exact f_1 and c_l of Candidate 007), resonance_scan_*.json, resonance_report.json,
  theoremE_constants_arb.json, eval_*.json (section 13 tables), log_*_table.json (log-series tables), prime_congruence_*.json,
  kappa_scan_arb.jsonl, tuned*_poly.json and tunedQ5_roots.json (compatibility polynomials and roots used by the tuned runs),
  tuned*_H.json (all H_n, sigma, R_k and obstruction radii of each tuned run), table_511b_*.md, cycle_diag_*.txt,
  drift_fit_*.txt, period3_decrements_300_353.txt, stream_ratio_modes_*.json, tprofile/bands text outputs.
- ckpt/: compact coefficient exports (below).

## Runs and provenance
- Tuned runs: tuned_b1_p1024, tuned_b2_p1024 (delta = 2/3), tunedQ4_r*_p1024, tunedQ5_r1..r6_p1024 (Q = 5, six roots),
  tuned49_r*_p1024 (delta = 4/9), tuned13_r1..r6_p1024 (delta = 1/3, six roots of P_12 in notes/tuned13_poly.json),
  tuned35_r*_p1024. Single-harmonic tuned runs (1024 bits, unit amplitude): single_sin7_45_p1024 (delta = 4/5, N 300),
  single_sin9_47_p1024 (4/7, N 301), single_sin11_49_p1024 (4/9, N 306), single_sin7_45_p1024_N500 (4/5, N 500, stability of
  the growth law); smoke tests smoke_sin7_45, smoke_sin11_49 (256 bits) agree with the exact sigma_k of the theory part.
- Q9 root check: q9_r10_check_p512 (delta = 2/9, c = 9/7, f_1 = sin + b sin3, b = 0.42149465856594..., the largest root of P_18,
  stored ascending in notes/tunedQ9_poly.json; 512 bits, N 99).
- Canonical 2/3 log series: certified through order 329; log_sin1_c3_from329 is a reset-radii continuation relative to the
  certified 329 midpoints (rows n >= 330 are conditional on those midpoints even where the per-order flags are missing, because
  the early code wrote the marker only into the header), continued to order 440 where it ended. log_sin1_c3_pert329 is the
  boundary-perturbed continuation from the 329 state (seed 20261031). Findings: report sections 5.11b (regime change at 330
  into a stationary period-3 cycle; orders 401..440 and drift fits).
- log_sin1_c2_p512 (1/2 canonical log run) finished at N = 300; c007_p2048 (Candidate 007 profile at 2048 bits) finished at
  N = 500 (report section 5.2: root test 3.5113 at 500).
- Float64 is not valid for the full canonical 2/3 recursion beyond about order 270 (report section 5.12); ball arithmetic with
  the radius rule disabled trims midpoint precision (section 5.11).

## Compact coefficient exports (ckpt/)
ckpt/<tag>_coeffs_n100.json (code/export_coeffs.py): per order n <= 100 the odd-sine coefficients a_(n,k) as float64 with a
log10 scale per order (value = coeffs[k] x 10^log10_scale) for the best tuned runs (tuned_b1_p1024 at c = 3, tunedQ4_r6,
tunedQ5_r6, tuned49_r5, tuned13_r6, tuned35_r4), the certified Theorem A/D parameter run sqrt5_sin1_p1024 (f_1 = sin theta,
delta = 1/sqrt5) and Candidate 007's profile at 2048 bits (c007_p2048); ckpt/log_sin1_c3_N350_coeffs_n60.json: the canonical
2/3 log series (columns by power of log r) for n <= 60. These exports are for inspection and comparison; they cannot be used
to resume a run. The full binary checkpoints (0.05 to 2.2 GB each) are not published; the commands below regenerate them,
starting from order 1 when no checkpoint is present. The exact leading data of Candidate 007 is notes/cand007_f1.json.

## Restart instructions for the long runs
- Candidate 007 profile at 2048 bits: python3 code/run_recursion.py --tag c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 cand007 --N 500 --ckpt-every 10 --resume
- Generic run: python3 code/run_recursion.py --tag <tag> --ring arb --prec 1024 --cl cand007 --f1 cand007 --N 500 --ckpt-every 10 --resume
  (resumes from ckpt/<tag>.pkl if present, otherwise starts at order 1).
- Canonical 2/3 log series continuation: python3 code/logff.py --tag log_sin1_c3_from329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 440 --ckpt-every 5
  --resume --workers 4 --stop-rel-rad 1e9 (needs ckpt/log_sin1_c3_from329.pkl, the state after order 329, 1.6 GB at order 400; not
  published). The certified part was the run log_sin1_c3_p512 (same options with --tag log_sin1_c3_p512; it starts at order 1
  when no checkpoint is present); its state after order 329, copied to ckpt/log_sin1_c3_from329.pkl, was resumed once with
  --reset-radii added (the command lines are in jobs/resume23_from329_reset.sh and jobs/resume23_345_reset.sh).
- Sensitivity diagnostic: the same command with --tag log_sin1_c3_pert329 --perturb-radii 20261031 --workers 2 --N 350 on a copy
  of the 329 state.
- Tuned series: python3 code/tuned_general.py --tag T --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.51215647362 --prec 1024 --N 300
  (delta = 1/3); --a 4 --b 9 with notes/tuned49_poly.json (delta = 4/9); python3 code/tuned_cQ.py --tag T --Q 5 --root-guess 0.5599810534719769 --prec 1024 --N 300.
- Single-harmonic tuned series: python3 code/tuned_general.py --tag T --a 4 --b 5 --f1-single 7 --prec 1024 --N 300 (sin 7theta at
  delta = 4/5); --a 4 --b 7 --f1-single 9; --a 4 --b 9 --f1-single 11. Q9 root check: python3 code/tuned_general.py --tag T --a 2 --b 9
  --poly-coeffs @notes/tunedQ9_poly.json --root-guess 0.421494658566 --prec 512 --N 99.
- Section-13 evaluation of any checkpoint: python3 code/evaluate_series.py ckpt/T.pkl --N 10,20,40,80 --R 1,2,4,8 --out notes/eval_T.json.
- The driver paths assume this layout (code/, notes/, logs/, ckpt/ side by side). The Candidate 007 source file is
  source/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json relative to the project
  root (read-only; in the repository it is under Changhe/IPM/combined1/); it is needed only by code/extract007.py, since the runs read
  notes/cand007_f1.json.

## Best candidate parameters and coefficients
- Finite-order growth fits in the tested two-mode family: f_1 = sin(theta) + a sin(3 theta) with
  a about 0.08..0.10 at c_l = 4076476460239181/2251799813685248 (L about 0.25); pure sin(theta): L = 0.4676 (see the report).
- Candidate 007 profile (exact coefficients in notes/cand007_f1.json): fitted L about 3.5 at its own c_l (apparent exterior
  radius 16..32). These are numerical diagnostics, not proved asymptotic growth constants or convergence radii.
  Convergence at the stored rational parameter remains unresolved because compatibility at its first stream resonance is open.
