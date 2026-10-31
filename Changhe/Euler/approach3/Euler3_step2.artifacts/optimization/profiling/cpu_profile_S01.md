CPU timing of S01 (label VALIDATION; validation/cpu_profile_S01.py, started 2026-10-29T01:04:12Z, cores [31, 32, 33, 34], start S01_nest6_cl0.45_om1.0_p0.pt): n_opt 1469, rows 433009, RSS after the build 5.35 GB (the record stores ru_maxrss KiB / 1e6; multiplied by 1.024 here, verifier remark 02:4xZ). Wall times (time.perf_counter; CPU operations are synchronous), median of n samples (n per entry; the first run used 3 samples for the cheap items and 1 or 2 for the expensive double-double items, as the verifier noted at 01:20Z). J_cw is timed on one chunk of 64 coefficient columns and extrapolated linearly to the 1469 columns.

| component | threads 1 | threads 4 |
|---|---|---|
| residual_vector_wd_fp64 | 0.58 s (min 0.58, max 0.59, n 3) | 2.29 s (min 2.12, max 2.40, n 3) |
| objective_at_fp64 | 59.34 s (min 58.46, max 60.26, n 3) | 17.29 s (min 17.02, max 18.94, n 3) |
| trial_evaluation_fp64 | 58.93 s (min 58.86, max 60.46, n 3) | 24.03 s (min 21.82, max 26.66, n 3) |
| complete_gradient_fp64 | 163.59 s (min 160.31, max 166.36, n 3) | 49.49 s (min 45.67, max 49.90, n 3) |
| objective_at_dd | 68.65 s (min 67.75, max 69.03, n 3) | 19.26 s (min 19.24, max 19.27, n 3) |
| trial_evaluation_dd | 70.34 s (min 68.80, max 70.73, n 3) | 23.22 s (min 21.59, max 24.32, n 3) |
| complete_gradient_dd | 174.83 s (min 174.83, max 174.83, n 1) | 65.17 s (min 65.17, max 65.17, n 1) |
| param_columns_fp64 | 310.12 s (min 298.43, max 315.43, n 3) | 88.56 s (min 88.35, max 89.34, n 3) |
| Jcw_chunk64_fp64 | 77.51 s (min 76.90, max 78.12, n 2); 1469 columns 1777 s | 28.47 s (min 28.43, max 28.51, n 2); 1469 columns 653 s |
| param_columns_dd | 373.87 s (min 373.87, max 373.87, n 1) | 119.37 s (min 119.37, max 119.37, n 1) |
| Jcw_chunk64_dd | 1664.64 s (min 1664.64, max 1664.64, n 1); 1469 columns 38157 s | 652.03 s (min 652.03, max 652.03, n 1); 1469 columns 14946 s |
| param_columns_dd_fp64tangent | 317.32 s (min 317.32, max 317.32, n 1) | 96.29 s (min 96.29, max 96.29, n 1) |
| Jcw_chunk64_dd_fp64tangent | 134.88 s (min 134.88, max 134.88, n 1); 1469 columns 3092 s | 48.52 s (min 48.52, max 48.52, n 1); 1469 columns 1112 s |
| param_columns_dd_fp64jac | 295.78 s (min 295.78, max 295.78, n 1) | 87.35 s (min 87.35, max 87.35, n 1) |
| Jcw_chunk64_dd_fp64jac | 77.42 s (min 77.42, max 77.42, n 1); 1469 columns 1775 s | 27.64 s (min 27.64, max 27.64, n 1); 1469 columns 634 s |
- full_Jcw_fp64_4threads: 731.3 s, shape [433009, 1469], peak RSS 12.20 GB (ru_maxrss KiB x 1024)
- normal_equations_4threads: 7.09 s (min 7.01, max 7.11, n 3)
- cholesky_solve_4threads: 0.01 s (min 0.01, max 0.01, n 3)
- normal_equations_1thread: 27.90 s (min 27.62, max 28.58, n 3)
- cholesky_solve_1thread: 0.04 s (min 0.04, max 0.05, n 3)

Projected cost per accepted LM iteration (J_cw + parameter columns + normal equations + solve + two trial evaluations + complete gradient):

| threads | mode | s per accepted iteration | accepted iterations per hour per job | ratio to fp64 (M3 limit 1.5) |
|---|---|---|---|---|
| 1 | fp64 | 2396 | 1.50 | 1.000 |
| 1 | dd | 38874 | 0.09 | 16.223 |
| 1 | dd_fp64tangent | 3752 | 0.96 | 1.566 |
| 1 | dd_fp64jac | 2414 | 1.49 | 1.007 |
| 4 | fp64 | 846 | 4.26 | 1.000 |
| 4 | dd | 15184 | 0.24 | 17.951 |
| 4 | dd_fp64tangent | 1327 | 2.71 | 1.569 |
| 4 | dd_fp64jac | 840 | 4.29 | 0.993 |

Peak RSS of the profiling process at the end: 12.20 GB (ru_maxrss KiB x 1024; includes the full float64 J_cw of 433009 x 1469, 5.1 GB).
