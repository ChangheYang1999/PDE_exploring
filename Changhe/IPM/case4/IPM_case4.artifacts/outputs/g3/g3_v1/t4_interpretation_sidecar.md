# T4 (g3_v1, session s3) interpretation sidecar (numerics lane; written 2026-10-24T17:2xZ; does not alter the frozen record)

Run 20261024T133215Z_1792848735809499497_g3_t4; t4.json sha256 f48311553b85264aed5da663ebf89d30ab649be44a3ab896a09329d7d18dacab (102924 bytes);
result.json success true, returncode 0, stop_reasons [], wall 13049.98 s (13:32:15Z to 17:09:45Z), peak_family_rss_mib 120629.30 (guard RSS sum during the
8-worker Jacobian fork pool; the worker's own VmHWM was 24.4 GiB and its steady RSS 15.7 GiB). Strict verdict: FAIL (passed False; 27 of 29 checks PASS;
failing T4.5_all_directions_pass_baseline_thresholds_best_step and T4.5_all_directions_pass_baseline_all_completed_steps_and_lifted_C5, failing directions
weakest_singular_0, weakest_singular_1, weakest_singular_2). Lead ruling T4-R1 (17:12Z; c4-lead reviews/g3_t4_s3_lead_read.md): the three weak rows are a
resolution-scope defect of the frozen predicate, recorded as exception E-T4.5w; no rerun, no predicate change; FINAL reports FAIL plus the exception.
Session s1 of the same step (run 20261024T125001Z) was a lead-ordered budget stop at 13:31:47Z with no verdict (policy v3, 3 h); s3 ran under
outputs/g3_t4_policy.json (8 h) on identical bytes.

## 1. Factor two in the dilation norms (verifier 13:14Z, lead 13:19Z item 2)
model860 defines r_i = sqrt(2 w_i/(pi a_ref^2)) R_f(X_i) and J_mesh = r.r/2, so a column's squared norm is 2 x the H-norm squared with weight 1/(pi a_ref^2)
used by the verifier's topic 17. t4.json dilation.my_squared_norms (projected 1095821582639997.6, leak 1095821582640157.2, exact_FD 2.398349169550835e-07)
divided by 2 give 547910791319998.8 / 547910791320078.6 / 1.1991745847754174e-07 against the topic 17 references 547910791319997.4 / 547910791320078.3 /
1.199175682129626e-07 (relative differences 2.6e-15, 5.5e-16 and 7.8e-7, the last one a finite-difference versus exact comparison). dJ per unit log L:
projected D +19.33673805912303, k = 26 leak -19.336738059124272, exact dilation (FD column) 1.2e-15 (dilation invariance of J_abs). The projected dilation
direction itself passes the FD check (best 7.9e-13). The k = 26 leakage coefficient of (j, m, k) = (0, 8, 26) is 60583.22645785234.

## 2. The weak-direction rows (E-T4.5w)
Spectrum of the column-scaled feasible matrix A (90624 x 855): sigma_max 9.620401082045419, median 2.0590476845382898e-15, s_min 4.1408300181957735e-18;
eps sigma_max = 2.14e-15. For the three computed weakest right singular vectors v (unit in scaled feasible coordinates) ||A v|| is 3.58e-15, 3.64e-15 and
2.52e-15: not s_min but the numerical null-space floor, because singular vectors with s below eps sigma_max are determined only to that level. The central
differences carry the binary64 rounding noise of the residual divided by 2h and the h^2 curvature terms; their absolute discrepancies ||fd - A v|| are
9.4e-12 / 1.6e-11 / 2.4e-10 (weakest_0), 1.2e-11 / 2.6e-11 / 2.4e-10 (weakest_1) and 5.5e-12 / 4.4e-11 / 8.5e-11 (weakest_2) at h = 1e-4, 1e-5, 1e-6,
with max_abs_error per node 1.8e-13 to 8.5e-12. The passing unit low tangents have larger absolute discrepancies (low_tangent_38: 1.5e-9 / 1.1e-10 / 1.3e-9;
cl_along_chart: 2.4e-8 / 2.8e-10 / 7.0e-10; projected_dilation_D: 1.6e-12 / 2.0e-11 / 4.7e-10). The relative error 2e3 to 7e4 is therefore the denominator
||A v|| ~ 3e-15, not a Jacobian defect; the ratios (error growing toward h = 1e-6) are the rounding-dominated signature. The lifted C5 maxima at every FD point
are 4.4e-14 to 3.6e-13 (< 1e-10). Source of the predicate: g3_t4.py:189 applied the handoff baseline feasible threshold 1e-3 (absolute_derivative_checks_v2,
19 core and 4 mixed directions, none near-null) to rows that SPEC.md section 10 asks to report with their convergence ratio and best agreement.

## 3. Everything else in T4
Seed arrays equal the sealed JSON; reduced C5 rank 5 of 5 x 60 and unreduced center + C5 rank 6 of 6 x 61 (singular values 1.20e5 ... 53); tangent rank 55,
complete rank 60, G T 1.16e-11; the old 19 tangents lie inside the new 55 (1.05e-15) and the embedded 855 (1.11e-15); three random lifts with C5 max
< 1.8e-13, c_l bits preserved, FD tangents 5.8e-11 to 2.8e-10; 855 positive singular values, A 90624 x 855; dilation tangency rows 3.8e-19; zero step bitwise at
the seed, through the chart and through campaign860.feasible_trial with the cache cleared (recomputed, not a cache hit); 6 c_l-moving chart directions best
1.06e-10 to 1.92e-10 and 16 high directions best 2.1e-16 to 6.8e-15, all steps within thresholds.

## 4. Timing
cache_record: 39 single-threaded basis cache builds, 7754 s (199 s each); order-48 origin series 4235 s; longdouble assembly 400 s; Jacobian 61 s.
Per c_l-moving FD direction about 22.4 min (6 rebuilds plus two 85-digit lifted C5 reports per step); per high direction about 2.9 min.
