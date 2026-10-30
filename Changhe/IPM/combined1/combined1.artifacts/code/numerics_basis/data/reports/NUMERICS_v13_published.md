# numerics_v13 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v13; UTC time: 2026-10-29T13:13:19Z; supersedes numerics_v12 (sha256 20763c86645a954697bb617b57efc7d81f7afbbcd3aa173d5ee4d00d352bae9c) and earlier versions.
- consulted (v13): theory_v06.md (the T1/T3 theory worker, 09:18:15Z; ACK 09:19Z); theory_v07.md (the T1/T3 theory worker, 11:20Z; sha256 42eb222a38caadac...; ACK 11:52Z in status file); the coordinator team notes through 2026-10-29T13:07 (matrix v110: 021 RULED OUT; T4-390 wording);
  the T4 theory auditor T4-374, T4-390 (NUMERICS_FINAL audits, applied 10:12Z and 10:49Z); the N4 numerical auditor through 2026-10-29T11:17:21.; the N3 numerics worker through 2026-10-29T13:04. Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by
  ID; the new numbers are the N1/N2 numerics worker's FLOAT values offered for certification.
- theory version followed: theory_v06 (R-HOLDOUT; R-TANGENT per-step reporting, request 4; NC-T-ORIGIN-INV proxies, request 5). Candidate IDs new in v13: C1-N1-025-combined-heldin1e16 (12:50:59Z), C1-N1-026-heldin1e16-legqs25-m16to23 (13:12:37Z); 027 and 028 are running (snapshots in numerics_v14). Chart PRIMARY;
  c_l and Theta_0 of state 131 EXACT, center relation EXACT, a_0 free; coefficient files working file candidate_snapshots (not published)/<ID>/<tag>_exact.json (sha256 in SHA256SUMS).
- Every number below is FLOAT (MID 32 rule unless marked MID 16 = optimizer report, or LOSS) unless cited by a working file the N3 numerics worker (not published) ID. Every comparison is a trial comparison
  at the tested probes: no inference about spans, angular-band mass, stationarity, causes or what a basis 'can' reach is drawn (T4-340, T4-356, T4-374, T4-390).

## 0. Corrections to numerics_v12 (the coordinator 12:36Z item 1, matrix v124)
(a) C1-N1-024 is RULED OUT in every ball of rows 96 and 97: The N4 numerical auditor's N4-342 to N4-345 reproduced by T4-427 to T4-431 (registered distance > 0.001556067368832641 at (19,1800),
    3.403 times the graded ceiling and 546.0 times the sharpw family ceiling; the six scalar point gaps; uniform graded gap 0.0748700; origin and complete prefix). Every
    snapshot C1-N1-001 to 024 except the FLOAT comparison 011 is RULED OUT in every registered scalar ball and original graded box.
(b) The INDEX line of C1-N1-024 carries the labels 'LOSS (MID 16)' and 'optimizer report (MID 16)'; both are wrong (024 optimized on the MID 32 rule; T4-427, N4-342). INDEX
    lines are immutable; this version and NUMERICS_FINAL state the correction.
(c) 024 held-out hash (narrower statement, N4-346): the INDEX line and my 11:00Z note cite 58586004...; the current heldout/HELDOUT_024.md has sha256 e171c051...; undoing the
    one stated edit of its objective-row line reproduces 58586004... with all 60 probe pairs unchanged (N4-346 CONFIRMED); the two save times (09:13:13Z, 09:13:43Z) are my
    record and are not independently witnessed.
(d) Lower-bound factors are rounded down everywhere (023: 5.763 and 924.6; 024: 3.403 and 546.0).
(e) The v12 section 2 held-out table of 025 and its reading are unchanged; this version adds 025's MID 32 norms and snapshot, 026 and the control 027.
(f) The 025 MANIFEST fields basis.description and loss.definition end at 'at weight ' without the value: the 14 mid-field rows carry weight 1e16 and the other 67 rows
    1e12 (T4-436 CONFIRMS the exact structure, 81 rows with weights 1e12 and 1e16); the truncation came from a 300-character cut of the objective text in my snapshot script
    (fixed for 026 on).
(g) Every FLOAT comparison in this version is stated per probe (T4-435, N4-356 refute the blanket ranges of v12 and of my 12:35Z and 12:57Z notes): see sections 1, 2, 2b, 2c.
    Graded gaps are printed as lower displays (023: 0.06288; 024: 0.07487). The objective share: the F part of the balanced objective is 2^18 G0^2 + 2^18 (20/21) ||rF||_2^2 +
    2^18 100 int F^2 ds dtheta; for 016 at MID 16 the rF term is 1.26e7 of 1.34e7 (about 94 percent).
(h) Launch records to the second (the N4 numerical auditor 12:59Z): 026 launched at 11:31:32.966Z (creation time of numerics/optimization/logs/chain026.out, the stdout file of the setsid
    launch, which the chain never writes to; HELDOUT_026.md header 'Written 11:31:32Z' is the `date -u` taken in the same shell command, in the same second, before the launch command);
    027 at 12:34:48.114Z (logs/chain027.out; HELDOUT_027.md written 12:28Z); 028 at 12:51:53.866Z (logs/chain028.out; HELDOUT_028.md written 12:51Z, same shell command).

## 1. C1-N1-024 (MID 32 rule control of 016; 12 steps; held-out file heldout/HELDOUT_024.md, current sha256 e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab; RULED OUT, section 0 (a))
Run: the same start (exact quotient of 013 + 252 legqs R0 = 25 in m = 9..15, zero start; 2174 generators), the same 67 rows (weight 1e12) and the same 12 GN steps as 016, but the optimization objective evaluated on the MID 32 radial rule (016: MID 16) and on the GPU (016: CPU; N4-342 notes the backend change). HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}. Snapshot C1-N1-024-rulem32-legqs25 (11:31:32Z).
Exact JSON sha256 3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d; 2174 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  11 obj 1.512497e+07 -> 1.509028e+07 ACC pred 3.665e+04 lam 4.1e-03 dRho2 1.470e-03 dCoef 8.080e-06 parts F 1.322e+07 G 2.219e+05 P 4.392e+04 K 1.6.
Optimizer report (MID 32): 95659e+02 G1 3.680307e+00 G0 3.275353e-01 rF 7.170395e+00 supF 1.8588e-01
FLOAT (diag2, MID 32): G0 0.3275 (016 0.3089, 022 0.2816, 023 0.3228), G1 3.680, P2 209.6, rF 7.220, H 0.6187, sup|F| 0.1859, theta_inner 0.0114, kappa_inner 0.7305 ((B-L2) margin +0.0684).
First-mode weak probes (27 sampled k <= 4096, objective rows): largest sampled value 1.81e-04 at k = 128 (a sampled maximum, not a bound; 016 1.50e-4 at k = 2048).
| probe (n, K) | r_peak | 016 | 022 | 023 | 024 |
|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | 8.18e-06 | 5.91e-05 | 2.14e-04 | 5.13e-05 |
| (19, 900) [registered, HELD OUT] | 25 | 5.31e-04 | 5.23e-04 | 1.04e-03 | 5.31e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | 8.16e-04 | 7.61e-04 | 1.46e-03 | 8.41e-04 |
| (19, 1800) [registered, HELD OUT] | 35 | 9.02e-04 | 8.30e-04 | 1.62e-03 | 9.55e-04 |
| (19, 2400) [registered, HELD OUT] | 40 | 7.44e-04 | 6.90e-04 | 1.44e-03 | 8.12e-04 |
| (23, 600) [registered, HELD OUT] | 20 | 2.17e-04 | 1.65e-04 | 3.48e-04 | 2.67e-04 |
| (23, 900) [registered, HELD OUT] | 25 | 2.80e-05 | 7.74e-05 | 1.41e-04 | 2.34e-06 |
| (23, 1200) [registered, HELD OUT] | 28 | 2.97e-04 | 3.19e-04 | 5.64e-04 | 2.90e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | 5.94e-04 | 5.85e-04 | 1.02e-03 | 6.03e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | 6.50e-04 | 6.44e-04 | 1.14e-03 | 6.56e-04 |
| (25, 600) [registered, HELD OUT] | 20 | 1.94e-04 | 1.64e-04 | 3.88e-04 | 2.49e-04 |
| (25, 900) [registered, HELD OUT] | 25 | 8.93e-05 | 4.02e-05 | 8.13e-05 | 1.24e-04 |
| (25, 1200) [registered, HELD OUT] | 28 | 1.16e-04 | 1.49e-04 | 2.66e-04 | 1.01e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | 4.19e-04 | 4.18e-04 | 7.32e-04 | 4.31e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | 5.37e-04 | 5.27e-04 | 9.27e-04 | 5.63e-04 |
| (29, 600) [registered, HELD OUT] | 20 | 8.70e-05 | 9.78e-05 | 3.16e-04 | 1.40e-04 |
| (29, 900) [registered, HELD OUT] | 25 | 1.62e-04 | 1.24e-04 | 2.62e-04 | 2.11e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | 9.65e-05 | 4.64e-05 | 7.98e-05 | 1.34e-04 |
| (29, 1800) [registered, HELD OUT] | 35 | 1.19e-04 | 1.52e-04 | 2.95e-04 | 9.96e-05 |
| (29, 2400) [registered, HELD OUT] | 40 | 2.72e-04 | 2.85e-04 | 5.40e-04 | 2.62e-04 |
| (31, 600) [registered, HELD OUT] | 20 | 7.85e-05 | 6.17e-05 | 2.67e-04 | 8.84e-05 |
| (31, 900) [registered, HELD OUT] | 25 | 1.66e-04 | 1.22e-04 | 2.57e-04 | 1.61e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | 1.27e-04 | 8.98e-05 | 1.26e-04 | 1.10e-04 |
| (31, 1800) [registered, HELD OUT] | 35 | 5.42e-05 | 6.01e-05 | 1.83e-04 | 8.53e-05 |
| (31, 2400) [registered, HELD OUT] | 40 | 1.99e-04 | 1.88e-04 | 4.04e-04 | 2.38e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.69e-04 | 8.72e-05 | 6.66e-05 | 2.27e-04 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 2.33e-04 | 1.66e-04 | 3.72e-04 | 2.87e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 2.32e-04 | 1.94e-04 | 4.42e-04 | 2.87e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 1.70e-04 | 1.58e-04 | 4.20e-04 | 2.27e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 1.04e-04 | 1.15e-04 | 3.64e-04 | 1.42e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 3.77e-05 | 6.60e-05 | 2.92e-04 | 8.64e-05 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 3.26e-05 | 3.06e-05 | 2.40e-04 | 4.63e-05 |
| (19, 137) [N4-160 K0 = 128, HELD OUT] | 10 | 1.26e-04 | 2.76e-05 | 4.64e-04 | 9.83e-05 |
| (21, 138) [N4-160 K0 = 128, HELD OUT] | 10 | 1.91e-04 | 9.59e-05 | 2.83e-04 | 1.39e-04 |
| (23, 139) [N4-160 K0 = 128, HELD OUT] | 10 | 1.55e-04 | 7.69e-05 | 2.27e-04 | 1.60e-04 |
| (25, 140) [N4-160 K0 = 128, HELD OUT] | 10 | 1.08e-04 | 6.07e-05 | 1.77e-04 | 7.59e-05 |
| (27, 141) [N4-160 K0 = 128, HELD OUT] | 10 | 7.21e-05 | 5.45e-05 | 1.41e-04 | 6.63e-05 |
| (29, 142) [N4-160 K0 = 128, HELD OUT] | 10 | 5.48e-05 | 3.94e-05 | 1.08e-04 | 3.02e-05 |
| (31, 143) [N4-160 K0 = 128, HELD OUT] | 10 | 5.25e-05 | 2.66e-05 | 7.73e-05 | 8.76e-06 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.06e-05 | 2.48e-05 | 2.27e-06 | 1.54e-05 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 4.61e-05 | 4.54e-06 | 5.03e-05 | 4.07e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.36e-05 | 2.38e-05 | 9.41e-06 | 4.64e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 5.36e-05 | 9.22e-06 | 6.99e-05 | 6.31e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 1.83e-06 | 3.96e-06 | 3.95e-05 | 9.32e-06 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 1.25e-05 | 2.10e-05 | 6.51e-05 | 1.84e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 1.01e-05 | 6.28e-06 | 5.16e-05 | 4.03e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 6.21e-06 | 1.12e-04 | 1.11e-05 | 1.19e-05 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 2.04e-05 | 4.39e-05 | 8.54e-06 | 5.66e-06 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.84e-06 | 8.89e-06 | 1.22e-05 | 3.18e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 3.15e-05 | 2.21e-05 | 3.97e-05 | 2.56e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 9.55e-04; 7 of 25 above the graded ceiling 4.5717e-4 (016: (19, 1800) 9.02e-4, 7 of 25; 022: 8.30e-4, 7; 023: 1.62e-3, 10).

## 2. C1-N1-025 (combined basis, 14 mid-field rows at weight 1e16; 60 steps; held-out file heldout/HELDOUT_025.md sha256 6412b2627b390e88e31257cb7fd0788575c6c037aaeaaedc6343e5438a587ea0, written before launch)
Run: start 016 + legqs R0 = 50 and R0 = 100 in m = 9..15 (252 + 252) + legqs R0 = 25 in the existing higher blocks m = 16..23 (240): 2918 generators (N4-274-type dimension claim not made); 81 rows = the 67 rows of 016 at weight 1e12 + the 14 mid-field rows n = 19..31 at K0 = 128 and 512 at weight 1e16 (sensitivity run for the 021 question); 60 GN steps, MID 16, GPU 7 (50 s per step). HELD-OUT (never rows): the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32}.
Exact JSON sha256 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17; 2918 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  60 obj 1.105518e+07 -> 1.103659e+07 ACC pred 1.954e+05 lam 2.5e-04 dRho2 1.237e-03 dCoef 7.038e-05 parts F 9.061e+06 G 2.701e+05 P 6.019e+04 K 1.6.
Optimizer report (MID 16): 53457e+02 G1 4.059903e+00 G0 3.045846e-01 rF 5.867089e+00 supF 1.4928e-01
FLOAT (diag2, MID 32): G0 0.3051 (016 0.3089, 022 0.2816, 023 0.3228), G1 4.067, P2 245.1, rF 5.930, H 0.6251, sup|F| 0.1646, theta_inner 0.0114, kappa_inner 0.7388 ((B-L2) margin +0.0601).
First-mode weak probes (27 sampled k <= 4096, objective rows): largest sampled value 1.22e-03 at k = 512 (a sampled maximum, not a bound; 016 1.50e-4 at k = 2048).
| probe (n, K) | r_peak | 016 | 022 | 023 | 025 |
|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | 8.18e-06 | 5.91e-05 | 2.14e-04 | 2.04e-04 |
| (19, 900) [registered, HELD OUT] | 25 | 5.31e-04 | 5.23e-04 | 1.04e-03 | 8.21e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | 8.16e-04 | 7.61e-04 | 1.46e-03 | 1.14e-03 |
| (19, 1800) [registered, HELD OUT] | 35 | 9.02e-04 | 8.30e-04 | 1.62e-03 | 1.27e-03 |
| (19, 2400) [registered, HELD OUT] | 40 | 7.44e-04 | 6.90e-04 | 1.44e-03 | 1.14e-03 |
| (23, 600) [registered, HELD OUT] | 20 | 2.17e-04 | 1.65e-04 | 3.48e-04 | 5.60e-05 |
| (23, 900) [registered, HELD OUT] | 25 | 2.80e-05 | 7.74e-05 | 1.41e-04 | 3.81e-04 |
| (23, 1200) [registered, HELD OUT] | 28 | 2.97e-04 | 3.19e-04 | 5.64e-04 | 6.58e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | 5.94e-04 | 5.85e-04 | 1.02e-03 | 9.40e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | 6.50e-04 | 6.44e-04 | 1.14e-03 | 9.93e-04 |
| (25, 600) [registered, HELD OUT] | 20 | 1.94e-04 | 1.64e-04 | 3.88e-04 | 6.63e-06 |
| (25, 900) [registered, HELD OUT] | 25 | 8.93e-05 | 4.02e-05 | 8.13e-05 | 1.86e-04 |
| (25, 1200) [registered, HELD OUT] | 28 | 1.16e-04 | 1.49e-04 | 2.66e-04 | 4.05e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | 4.19e-04 | 4.18e-04 | 7.32e-04 | 7.00e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | 5.37e-04 | 5.27e-04 | 9.27e-04 | 8.13e-04 |
| (29, 600) [registered, HELD OUT] | 20 | 8.70e-05 | 9.78e-05 | 3.16e-04 | 3.62e-05 |
| (29, 900) [registered, HELD OUT] | 25 | 1.62e-04 | 1.24e-04 | 2.62e-04 | 4.51e-05 |
| (29, 1200) [registered, HELD OUT] | 28 | 9.65e-05 | 4.64e-05 | 7.98e-05 | 5.78e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | 1.19e-04 | 1.52e-04 | 2.95e-04 | 3.00e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | 2.72e-04 | 2.85e-04 | 5.40e-04 | 4.64e-04 |
| (31, 600) [registered, HELD OUT] | 20 | 7.85e-05 | 6.17e-05 | 2.67e-04 | 3.91e-05 |
| (31, 900) [registered, HELD OUT] | 25 | 1.66e-04 | 1.22e-04 | 2.57e-04 | 9.62e-05 |
| (31, 1200) [registered, HELD OUT] | 28 | 1.27e-04 | 8.98e-05 | 1.26e-04 | 4.22e-05 |
| (31, 1800) [registered, HELD OUT] | 35 | 5.42e-05 | 6.01e-05 | 1.83e-04 | 1.54e-04 |
| (31, 2400) [registered, HELD OUT] | 40 | 1.99e-04 | 1.88e-04 | 4.04e-04 | 3.16e-04 |
| (19, 521) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.69e-04 | 8.72e-05 | 6.66e-05 | 1.06e-06 |
| (21, 522) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 2.33e-04 | 1.66e-04 | 3.72e-04 | 5.06e-06 |
| (23, 523) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 2.32e-04 | 1.94e-04 | 4.42e-04 | 5.87e-06 |
| (25, 524) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.70e-04 | 1.58e-04 | 4.20e-04 | 5.65e-06 |
| (27, 525) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.04e-04 | 1.15e-04 | 3.64e-04 | 5.05e-06 |
| (29, 526) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 3.77e-05 | 6.60e-05 | 2.92e-04 | 4.22e-06 |
| (31, 527) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 3.26e-05 | 3.06e-05 | 2.40e-04 | 3.57e-06 |
| (19, 137) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.26e-04 | 2.76e-05 | 4.64e-04 | 1.21e-07 |
| (21, 138) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.91e-04 | 9.59e-05 | 2.83e-04 | 1.83e-08 |
| (23, 139) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.55e-04 | 7.69e-05 | 2.27e-04 | 1.00e-08 |
| (25, 140) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.08e-04 | 6.07e-05 | 1.77e-04 | 1.54e-08 |
| (27, 141) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 7.21e-05 | 5.45e-05 | 1.41e-04 | 1.57e-08 |
| (29, 142) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 5.48e-05 | 3.94e-05 | 1.08e-04 | 1.05e-08 |
| (31, 143) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 5.25e-05 | 2.66e-05 | 7.73e-05 | 1.07e-08 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.06e-05 | 2.48e-05 | 2.27e-06 | 1.84e-04 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 4.61e-05 | 4.54e-06 | 5.03e-05 | 3.13e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.36e-05 | 2.38e-05 | 9.41e-06 | 5.11e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 5.36e-05 | 9.22e-06 | 6.99e-05 | 1.15e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 1.83e-06 | 3.96e-06 | 3.95e-05 | 9.16e-07 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 1.25e-05 | 2.10e-05 | 6.51e-05 | 7.97e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 1.01e-05 | 6.28e-06 | 5.16e-05 | 1.70e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 6.21e-06 | 1.12e-04 | 1.11e-05 | 1.69e-04 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 2.04e-05 | 4.39e-05 | 8.54e-06 | 2.30e-05 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.84e-06 | 8.89e-06 | 1.22e-05 | 4.81e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 3.15e-05 | 2.21e-05 | 3.97e-05 | 6.87e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 1.27e-03; 10 of 25 above the graded ceiling 4.5717e-4 (016: (19, 1800) 9.02e-4, 7 of 25; 022: 8.30e-4, 7; 023: 1.62e-3, 10).
Per-step reporting (theory_v06 request 4, R-TANGENT; FLOAT, mesh 0.02 <= r <= 1e4, MID 16): 025: 39 accepted steps; density L2 step norm ||rho(a_new) - rho(a)||_2 on the mesh (FLOAT): first accepted step 1.54e-02, median 1.09e-03, last 1.24e-03, sum over accepted steps 8.388e-02 (an upper bound of the FLOAT mesh norm of the total density change by the triangle inequality; a certified bound is the N4 numerical auditor's); coefficient step norms 4.3e-07 to 2.8e-02. Every reported residual of this lane is either the optimizer's evaluated objective parts (MID 16) or the MID 32 diag2 re-evaluation; linear-model values ||F + J delta||_2 appear only in NUMERICS_FINAL section 4b and are labelled so. 026: 40 accepted steps; density L2 step norm ||rho(a_new) - rho(a)||_2 on the mesh (FLOAT): first accepted step 1.11e-02, median 7.09e-04, last 1.55e-03, sum over accepted steps 5.665e-02 (an upper bound of the FLOAT mesh norm of the total density change by the triangle inequality; a certified bound is the N4 numerical auditor's); coefficient step norms 5.4e-07 to 1.9e-02. Every reported residual of this lane is either the optimizer's evaluated objective parts (MID 16) or the MID 32 diag2 re-evaluation; linear-model values ||F + J delta||_2 appear only in NUMERICS_FINAL section 4b and are labelled so. 024: 5 accepted steps; density L2 step norm ||rho(a_new) - rho(a)||_2 on the mesh (FLOAT): first accepted step 2.17e-02, median 3.05e-03, last 1.47e-03, sum over accepted steps 3.029e-02 (an upper bound of the FLOAT mesh norm of the total density change by the triangle inequality; a certified bound is the N4 numerical auditor's); coefficient step norms 2.9e-06 to 7.0e-04. Every reported residual of this lane is either the optimizer's evaluated objective parts (MID 16) or the MID 32 diag2 re-evaluation; linear-model values ||F + J delta||_2 appear only in NUMERICS_FINAL section 4b and are labelled so.

## 2c. C1-N1-027 (control for 026: 022 continued 60 steps with the plain 67 rows; held-out file heldout/HELDOUT_027.md sha256 c99eb804dc6c390c4db9d9cfb7a5231a9b982a93f1c1b2b501e9b20af4829d7e, written before launch)
PENDING (027 tests running at publication).

## 2b. C1-N1-026 (022 continued with the 14 mid-field rows at weight 1e16; 60 steps)
Run: the 022 state (2414 generators; no new functions) continued 60 GN steps with the 81 rows of 025 (the 14 mid-field rows at weight 1e16); HELD-OUT as 025 (file heldout/HELDOUT_026.md, sha256 2016d960c982aeffa2b1bef5aaece9b7394e97139d9688b5f6abec3274606d15, written before the 11:31Z launch). Separates the row effect from the scale-100 basis effect of 025.
Exact JSON sha256 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3; 2414 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  60 obj 1.389229e+07 -> 1.389191e+07 ACC pred 2.700e+05 lam 8.2e-06 dRho2 1.550e-03 dCoef 4.125e-04 parts F 1.202e+07 G 2.146e+05 P 5.005e+04 K 1.6.
Optimizer report (MID 16): 37107e+02 G1 3.619349e+00 G0 2.783357e-01 rF 6.836564e+00 supF 1.3863e-01
FLOAT (diag2, MID 32): G0 0.2788 (016 0.3089, 022 0.2816, 023 0.3228), G1 3.627, P2 223.5, rF 6.891, H 0.6115, sup|F| 0.1558, theta_inner 0.0114, kappa_inner 0.7324 ((B-L2) margin +0.0665).
First-mode weak probes (27 sampled k <= 4096, objective rows): largest sampled value 1.39e-04 at k = 192 (a sampled maximum, not a bound; 016 1.50e-4 at k = 2048).
| probe (n, K) | r_peak | 016 | 022 | 023 | 026 |
|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | 8.18e-06 | 5.91e-05 | 2.14e-04 | 1.48e-04 |
| (19, 900) [registered, HELD OUT] | 25 | 5.31e-04 | 5.23e-04 | 1.04e-03 | 5.94e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | 8.16e-04 | 7.61e-04 | 1.46e-03 | 8.06e-04 |
| (19, 1800) [registered, HELD OUT] | 35 | 9.02e-04 | 8.30e-04 | 1.62e-03 | 8.32e-04 |
| (19, 2400) [registered, HELD OUT] | 40 | 7.44e-04 | 6.90e-04 | 1.44e-03 | 6.66e-04 |
| (23, 600) [registered, HELD OUT] | 20 | 2.17e-04 | 1.65e-04 | 3.48e-04 | 3.27e-05 |
| (23, 900) [registered, HELD OUT] | 25 | 2.80e-05 | 7.74e-05 | 1.41e-04 | 2.59e-04 |
| (23, 1200) [registered, HELD OUT] | 28 | 2.97e-04 | 3.19e-04 | 5.64e-04 | 4.67e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | 5.94e-04 | 5.85e-04 | 1.02e-03 | 6.74e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | 6.50e-04 | 6.44e-04 | 1.14e-03 | 6.95e-04 |
| (25, 600) [registered, HELD OUT] | 20 | 1.94e-04 | 1.64e-04 | 3.88e-04 | 3.53e-06 |
| (25, 900) [registered, HELD OUT] | 25 | 8.93e-05 | 4.02e-05 | 8.13e-05 | 1.08e-04 |
| (25, 1200) [registered, HELD OUT] | 28 | 1.16e-04 | 1.49e-04 | 2.66e-04 | 2.69e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | 4.19e-04 | 4.18e-04 | 7.32e-04 | 4.84e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | 5.37e-04 | 5.27e-04 | 9.27e-04 | 5.52e-04 |
| (29, 600) [registered, HELD OUT] | 20 | 8.70e-05 | 9.78e-05 | 3.16e-04 | 3.00e-05 |
| (29, 900) [registered, HELD OUT] | 25 | 1.62e-04 | 1.24e-04 | 2.62e-04 | 5.69e-05 |
| (29, 1200) [registered, HELD OUT] | 28 | 9.65e-05 | 4.64e-05 | 7.98e-05 | 1.05e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | 1.19e-04 | 1.52e-04 | 2.95e-04 | 1.85e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | 2.72e-04 | 2.85e-04 | 5.40e-04 | 2.98e-04 |
| (31, 600) [registered, HELD OUT] | 20 | 7.85e-05 | 6.17e-05 | 2.67e-04 | 2.93e-05 |
| (31, 900) [registered, HELD OUT] | 25 | 1.66e-04 | 1.22e-04 | 2.57e-04 | 8.64e-05 |
| (31, 1200) [registered, HELD OUT] | 28 | 1.27e-04 | 8.98e-05 | 1.26e-04 | 5.56e-05 |
| (31, 1800) [registered, HELD OUT] | 35 | 5.42e-05 | 6.01e-05 | 1.83e-04 | 8.47e-05 |
| (31, 2400) [registered, HELD OUT] | 40 | 1.99e-04 | 1.88e-04 | 4.04e-04 | 2.03e-04 |
| (19, 521) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.69e-04 | 8.72e-05 | 6.66e-05 | 2.56e-07 |
| (21, 522) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 2.33e-04 | 1.66e-04 | 3.72e-04 | 1.85e-06 |
| (23, 523) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 2.32e-04 | 1.94e-04 | 4.42e-04 | 2.04e-06 |
| (25, 524) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.70e-04 | 1.58e-04 | 4.20e-04 | 1.66e-06 |
| (27, 525) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.04e-04 | 1.15e-04 | 3.64e-04 | 1.15e-06 |
| (29, 526) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 3.77e-05 | 6.60e-05 | 2.92e-04 | 5.72e-07 |
| (31, 527) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 3.26e-05 | 3.06e-05 | 2.40e-04 | 1.92e-07 |
| (19, 137) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.26e-04 | 2.76e-05 | 4.64e-04 | 1.49e-08 |
| (21, 138) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.91e-04 | 9.59e-05 | 2.83e-04 | 5.31e-08 |
| (23, 139) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.55e-04 | 7.69e-05 | 2.27e-04 | 4.96e-08 |
| (25, 140) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 1.08e-04 | 6.07e-05 | 1.77e-04 | 3.85e-08 |
| (27, 141) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 7.21e-05 | 5.45e-05 | 1.41e-04 | 2.64e-08 |
| (29, 142) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 5.48e-05 | 3.94e-05 | 1.08e-04 | 1.29e-08 |
| (31, 143) [N4-160 K0 = 128, HELD IN (objective row)] | 10 | 5.25e-05 | 2.66e-05 | 7.73e-05 | 4.62e-09 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.06e-05 | 2.48e-05 | 2.27e-06 | 5.84e-05 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 4.61e-05 | 4.54e-06 | 5.03e-05 | 1.57e-04 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.36e-05 | 2.38e-05 | 9.41e-06 | 8.95e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 5.36e-05 | 9.22e-06 | 6.99e-05 | 9.91e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 1.83e-06 | 3.96e-06 | 3.95e-05 | 4.65e-05 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 1.25e-05 | 2.10e-05 | 6.51e-05 | 2.09e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 1.01e-05 | 6.28e-06 | 5.16e-05 | 9.35e-06 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 6.21e-06 | 1.12e-04 | 1.11e-05 | 9.74e-05 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 2.04e-05 | 4.39e-05 | 8.54e-06 | 1.32e-04 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.84e-06 | 8.89e-06 | 1.22e-05 | 6.08e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 3.15e-05 | 2.21e-05 | 3.97e-05 | 3.32e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 8.32e-04; 9 of 25 above the graded ceiling 4.5717e-4 (016: (19, 1800) 9.02e-4, 7 of 25; 022: 8.30e-4, 7; 023: 1.62e-3, 10).

## 3. NC-T-ORIGIN-INV seven-cell FLOAT proxies (theory_v06 request 5; theory_v07 request 6) for C1-N1-008 to 025
| candidate | two-mode value at the right end of the seven cells (thresholds 15.88162, 8.716729, 4.799949, 2.565236, 1.263642, 0.5028299, 0.06411577) | ratios value/threshold | min ratio | every cell excluded if the two-mode LB were certified |
|---|---|---|---|---|
| C1-N1-008 | 65.87, 59.87, 55.35, 51.77, 48.85, 46.40, 44.29 | 4.15, 6.87, 11.53, 20.18, 38.66, 92.28, 690.86 | 4.15 | yes |
| C1-N1-009 | 14.11, 11.11, 9.02, 7.51, 6.39, 5.54, 4.88 | 0.89, 1.27, 1.88, 2.93, 5.06, 11.03, 76.14 | 0.89 | NO |
| C1-N1-010 | 91.95, 82.21, 75.90, 71.26, 67.57, 64.50, 61.88 | 5.79, 9.43, 15.81, 27.78, 53.47, 128.28, 965.09 | 5.79 | yes |
| C1-N1-011 | 20.44, 17.85, 15.79, 14.13, 12.78, 11.66, 10.74 | 1.29, 2.05, 3.29, 5.51, 10.11, 23.19, 167.45 | 1.29 | yes |
| C1-N1-012 | 73.98, 63.96, 55.77, 49.00, 43.36, 38.64, 34.66 | 4.66, 7.34, 11.62, 19.10, 34.31, 76.84, 540.53 | 4.66 | yes |
| C1-N1-013 | 19.74, 17.23, 15.28, 13.73, 12.49, 11.46, 10.61 | 1.24, 1.98, 3.18, 5.35, 9.88, 22.80, 165.45 | 1.24 | yes |
| C1-N1-014 | 19.74, 17.23, 15.28, 13.74, 12.49, 11.46, 10.61 | 1.24, 1.98, 3.18, 5.35, 9.88, 22.80, 165.43 | 1.24 | yes |
| C1-N1-015 | 19.74, 17.23, 15.29, 13.74, 12.50, 11.47, 10.62 | 1.24, 1.98, 3.18, 5.36, 9.89, 22.82, 165.60 | 1.24 | yes |
| C1-N1-016 | 19.91, 17.52, 15.67, 14.20, 13.01, 12.01, 11.18 | 1.25, 2.01, 3.26, 5.54, 10.29, 23.89, 174.32 | 1.25 | yes |
| C1-N1-017 | 19.77, 17.27, 15.33, 13.79, 12.54, 11.51, 10.65 | 1.24, 1.98, 3.19, 5.37, 9.92, 22.89, 166.11 | 1.24 | yes |
| C1-N1-018 | 19.70, 17.26, 15.38, 13.90, 12.71, 11.73, 10.90 | 1.24, 1.98, 3.20, 5.42, 10.06, 23.32, 170.08 | 1.24 | yes |
| C1-N1-019 | 19.75, 17.26, 15.33, 13.79, 12.55, 11.52, 10.66 | 1.24, 1.98, 3.19, 5.38, 9.93, 22.91, 166.31 | 1.24 | yes |
| C1-N1-020 | 20.07, 17.74, 15.94, 14.51, 13.35, 12.39, 11.57 | 1.26, 2.03, 3.32, 5.66, 10.57, 24.63, 180.39 | 1.26 | yes |
| C1-N1-021 | 20.00, 17.67, 15.87, 14.45, 13.29, 12.33, 11.52 | 1.26, 2.03, 3.31, 5.63, 10.52, 24.53, 179.66 | 1.26 | yes |
| C1-N1-022 | 19.75, 17.36, 15.51, 14.04, 12.85, 11.87, 11.04 | 1.24, 1.99, 3.23, 5.47, 10.17, 23.61, 172.22 | 1.24 | yes |
| C1-N1-023 | 22.17, 19.90, 18.10, 16.62, 15.39, 14.32, 13.39 | 1.40, 2.28, 3.77, 6.48, 12.18, 28.48, 208.88 | 1.40 | yes |
| C1-N1-024 | 19.87, 17.33, 15.36, 13.79, 12.52, 11.48, 10.61 | 1.25, 1.99, 3.20, 5.38, 9.91, 22.83, 165.45 | 1.25 | yes |
| C1-N1-025 | 29.78, 26.15, 23.24, 20.87, 18.92, 17.30, 15.93 | 1.88, 3.00, 4.84, 8.14, 14.97, 34.40, 248.53 | 1.88 | yes |
FLOAT proxy (na_modes_cells.py, MID 32): projected weighted-Laplacian norm of the angular modes 1 and 3 of F at the right end of each cell (a lower bound of the full N_a when certified) against the theory_v03 section 5 thresholds at the left end. A ratio above 1 at every cell means FW-T-DYADIC-Y-v1 would be excluded for that candidate if the two-mode lower bounds were certified (the N3 numerics worker did 008 exactly; working file T4-248 (not published) as well). FLOAT; no verdict; 009's first cell is not excluded by two modes.
Remarks (the N3 numerics worker 12:35Z): the 016 FLOAT row agrees with the N3 numerics worker's exact modes-1+3 values (CLAIMED pending the N4 numerical auditor); the 'NO' of 009 is the weak two-mode lower bound only: the exact all-mode N_a excludes every cell for 009 (matrix rows 62, 63), so FW-T-DYADIC-Y-v1 is RULED OUT at 009 as well.

## 4. Mode 33 to 47 sweep for 023 (held-out probes, never rows)
Best FLOAT value per odd mode n = 33 .. 47 (weak_tests3, IPM_NMAX=47; never rows): 016: 1.0e-04, 2.1e-05, 3.3e-05, 8.6e-05, 7.5e-05, 7.9e-05, 1.6e-04, 6.0e-05; 022: 2.9e-05, 2.3e-05, 2.6e-05, 2.5e-05, 2.3e-05, 2.2e-05, 1.4e-05, 3.2e-05; 023: 1.7e-04, 1.6e-04, 1.9e-04, 8.5e-05, 5.3e-05, 9.3e-05, 3.7e-05, 5.0e-05. Largest held-out value over n <= 47: 023 (19,1800) 1.62e-03; 022 8.30e-04; 016 9.02e-04. Smaller or larger values at the tested probes; no band-mass bound follows.

## 5. Summary table (FLOAT, MID 32; held-out values at the registered probes)
| candidate | LOSS (MID 16) | G0 | G1 | P2 | rF | H | sup|F| | kappa_inner | largest registered held-out (n,K): m | (21,522) | (19,1800) | (23,2400) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1-N1-007 | 1.622513e+07 | 0.3767 | 3.439 | 190.8 | 7.828 | 0.6355 | 0.1384 | 0.7269 | - | 1.12e-03 | - | - |
| C1-N1-013 | 1.720925e+07 | 0.3722 | 3.441 | 191.2 | 7.810 | 0.6313 | 0.1437 | 0.7270 | - | 1.12e-03 | - | - |
| C1-N1-016 | 1.482665e+07 | 0.3089 | 3.727 | 218.1 | 7.146 | 0.6178 | 0.1495 | 0.7338 | (19, 1800): 9.02e-04 | 2.33e-04 | 9.02e-04 | 6.50e-04 |
| C1-N1-017 | 1.440123e+07 | 0.3209 | 3.538 | 200.5 | 7.049 | 0.6153 | 0.1565 | 0.7279 | (19, 1800): 1.03e-03 | 3.36e-04 | 1.03e-03 | 6.35e-04 |
| C1-N1-018 | 1.435008e+07 | 0.3127 | 3.856 | 223.6 | 7.000 | 0.6153 | 0.1553 | 0.7348 | (19, 1800): 1.02e-03 | 2.80e-04 | 1.02e-03 | 7.89e-04 |
| C1-N1-019 | 1.425139e+07 | 0.3251 | 3.587 | 202.2 | 7.001 | 0.6142 | 0.1578 | 0.7284 | (19, 1800): 1.02e-03 | 3.55e-04 | 1.02e-03 | 6.34e-04 |
| C1-N1-020 | 1.350190e+07 | 0.3201 | 3.913 | 226.9 | 6.744 | 0.6113 | 0.1996 | 0.7374 | (19, 1800): 1.14e-03 | 2.94e-04 | 1.14e-03 | 7.59e-04 |
| C1-N1-021 | 1.312554e+07 | 0.2996 | 3.489 | 203.5 | 6.680 | 0.6096 | 0.1398 | 0.7313 | (19, 1800): 1.14e-03 | 3.51e-04 | 1.14e-03 | 7.60e-04 |
| 022 (12 st.) | 1.411254e+07 | - | - | - | - | - | - | - | (19, 1800): 8.40e-04 | 1.31e-04 | 8.40e-04 | 6.83e-04 |
| C1-N1-022 | 1.388999e+07 | 0.2816 | 3.554 | 206.9 | 6.900 | 0.6119 | 0.1276 | 0.7315 | (19, 1800): 8.30e-04 | 1.66e-04 | 8.30e-04 | 6.44e-04 |
| 023 (12 st.) | 1.132924e+07 | - | - | - | - | - | - | - | (19, 1800): 1.60e-03 | 2.48e-04 | 1.60e-03 | 1.14e-03 |
| C1-N1-023 | 1.102322e+07 | 0.3228 | 3.939 | 247.9 | 5.942 | 0.6121 | 0.1786 | 0.7373 | (19, 1800): 1.62e-03 | 3.72e-04 | 1.62e-03 | 1.14e-03 |
| C1-N1-024 | 1.509028e+07 | 0.3275 | 3.680 | 209.6 | 7.220 | 0.6187 | 0.1859 | 0.7305 | (19, 1800): 9.55e-04 | 2.87e-04 | 9.55e-04 | 6.56e-04 |
| C1-N1-025 | 1.103659e+07 | 0.3051 | 4.067 | 245.1 | 5.930 | 0.6251 | 0.1646 | 0.7388 | (19, 1800): 1.27e-03 | 5.06e-06 | 1.27e-03 | 9.93e-04 |
| C1-N1-026 | 1.389191e+07 | 0.2788 | 3.627 | 223.5 | 6.891 | 0.6115 | 0.1558 | 0.7324 | (19, 1800): 8.32e-04 | 1.85e-06 | 8.32e-04 | 6.95e-04 |
All FLOAT (diag2 MID 32; weak_tests3 MID 32; LOSS = last accepted objective on the MID 16 rule, comparable only within the same row set: 016 to 020, 022, 023 use 67 rows; 021 and 025 use 81 rows, so their LOSS includes 14 more penalty rows). Certified floors (CONFIRMED): 016 > 0.0014703, 017 > 0.0016718, 018 > 0.0016558, 019 > 0.0016618, 020 > 0.0018553, 021 > 0.0018646 at (19,1800); printed digits rounded down from the certified roots.

## 6. Status and next runs
1. Reading of the GPU phase (FLOAT trial comparisons at the tested probes; no span, mass, stationarity or causal inference): the registered mid-field held-out values
   (modes 19 to 31, r 35 to 50; largest at (19,1800)) responded only to the scale-25 functions in the blocks m = 9..15 (016); scale 50 (017, 020), the higher blocks
   m = 16..23 (022), more steps (018, 019, 021), the MID 32 objective rule (024) raised 16 and lowered 9 of the 25 (factors 0.084 to 1.57); scale 100 (023) raised 22 of the 25 (factors 1.09 to 26.2) and lowered three; the 14
   mid-field pairing rows at weight 1e16 (025 on the combined basis, 026 on the 022 basis) are satisfied to 1e-9 to 6e-6; the per-probe changes of the 25 registered probes
   are listed in sections 2 and 2b (025 vs 016: 8 probes fall, factors 0.26 to 0.60, 17 rise, (19,600) x24.9, (23,900) x13.6, K >= 1800 x1.34 to 1.58; 026 vs 022: 7 fall,
   factors 0.02 to 0.77, 18 rise or stay, (19,600) x2.51, (23,900) x3.34, K >= 1800 x0.965 to 1.41). No uniform statement holds across the probes. G0 and sup|F| fell with the higher blocks and more steps (022: 0.2816,
   0.1276 at MID 32; 026 at MID 16: 0.2783, 0.1386). The balanced E_2 objective's F part is about 95 percent 2^18 (20/21) ||rF||_2^2; new mid-field freedom goes into rF first.
2. Running at publication (last runs of this lane): 027 = control for 026 (022 continued 60 steps with the plain 67 rows; heldout/HELDOUT_027.md sha256 c99eb804...; isolates
   the effect of the rows at equal start, steps and rule) and 028 = 022 + 252 legqs R0 = 25 functions n = 12..23 in m = 9..15 (2666 generators; more radial resolution at
   the one scale that moved the registered probes; heldout/HELDOUT_028.md sha256 caf3517a...; 67 rows, 60 steps). Both held-out files were written before launch. Their
   snapshots, held-out tables and the comparisons 026 vs 027 and 028 vs 022/027 go into numerics_v14 and NUMERICS_FINAL (due 19:00Z).
3. Certification targets: none. Every snapshot through 024 is RULED OUT in every registered scalar ball and original graded box (011 excepted, FLOAT comparison); 025, 026
   (and 027, 028) have FLOAT values only; the N4 numerical auditor audits 025 and 026 within the hour of their snapshots if it chooses. The N3 numerics worker's exact 016 norms (G0, rF CONFIRMED N4-341; G1,
   P2 under comparison) are the only exact norms of a legqs candidate; the two-scale product keys for 020 to 028 are not available.

