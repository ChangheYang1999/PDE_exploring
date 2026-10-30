# numerics_v14 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v14; UTC time: 2026-10-29T14:44:45Z; supersedes numerics_v13 (sha256 7ae8af1782e3d8e80205d16104dda60ee086152e87f074be8aaefba968b11952) and earlier versions.
- consulted (v14): theory_v06.md (the T1/T3 theory worker, 09:18:15Z; ACK 09:19Z); theory_v07.md (the T1/T3 theory worker, 11:20Z; sha256 42eb222a38caadac...; ACK 11:52Z in status file); the coordinator team notes through 2026-10-29T14:29 (H18 checkpoint; matrix v135: 001 to 026 except 011 RULED OUT; 027 OPEN, FLOAT only);
  the T4 theory auditor T4-374, T4-390 (NUMERICS_FINAL audits, applied 10:12Z and 10:49Z); the N4 numerical auditor through 2026-10-29T14:42; the N3 numerics worker through 2026-10-29T14:45. Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by
  ID; the new numbers are the N1/N2 numerics worker's FLOAT values offered for certification.
- theory version followed: theory_v07 (section 6 requests 1 to 6; the R-HOLDOUT per-probe reporting of theory_v05/v06 and R-TANGENT per-step norms retained; theory_v08 is expected 15:30Z to 16:20Z and will be ACKed within the hour). Candidate IDs new in v14: C1-N1-027 (snapshot 2026-10-29T14:13:51Z); C1-N1-028 is the reserved ID of the run legqs25_nin24_m9to15_gpu_m16 (exact JSON sha256 70afa847...; its snapshot follows its diag2 and is announced in numerics_v15). Chart PRIMARY;
  c_l and Theta_0 of state 131 EXACT, center relation EXACT, a_0 free; coefficient files working file candidate_snapshots (not published)/<ID>/<tag>_exact.json (sha256 in SHA256SUMS).
- Every number below is FLOAT (MID 32 rule unless marked MID 16 = optimizer report, or LOSS) unless cited by a working file the N3 numerics worker (not published) ID. Every comparison is a trial comparison
  at the tested probes: no inference about spans, angular-band mass, stationarity, causes or what a basis 'can' reach is drawn (T4-340, T4-356, T4-374, T4-390).

## 0. Corrections to numerics_v13 (the coordinator 13:41Z item 8, N4-372; matrix v130, v131)
(a) 025 is RULED OUT in every ball of rows 99 and 100 since matrix v130: The N4 numerical auditor's N4-362 to N4-364 reproduced by T4-438 to T4-441 (registered distance > 0.002065801265578052 at
    (19,1800), 4.518 times the graded ceiling, 724.9 times the sharpw family ceiling), accepted N4-370, N4-371; structure CONFIRMED both ways (T4-436, N4-365, T4-444). v13
    called 025 'FLOAT only' (stale at publication).
(b) 026 (rows 101, 102): C1-N1-026 is RULED OUT for every ball of the registered frameworks since matrix v132/v133 (2026-10-29T13:47Z/13:56Z): point gaps (N4-367 with T4-447; uniform graded point gap > 0.0594 at (1/10, 73/100)), first four density profiles equal 007's (N4-368 with T4-449; pinning T4-189 with T4-210), and the CONFIRMED fixed-c L^2 distance > 0.001355907204057457 from the registered held-out probe (19, 1800) (N4-369 with T4-450; 2.965 times the graded ceiling 25/54684 and 475.8 times the sharpw family ceiling 2.8496e-6); the N4 numerical auditor's N4-377 to N4-379 accept T4-446 to T4-450 (13:55:18Z), so the structure, prefix and distance are CONFIRMED in both directions. The distance is one registered necessary witness, not an estimate of the correction distance; neither L^2 floor implies a dyadic exclusion. v13 called 026 'OPEN pending the T4 theory auditor's replay' (true at 13:13Z; superseded at 13:47Z).
(c) N4-372 corrections of v13 summaries (all 300 table values agree with the stored FLOAT data): 024 against 016 has 18 increases and 7 decreases (ratio 6.27 at (19,600)); 025's
    decreases run 0.0341788 to 0.598336 and its K >= 1800 ratios 1.40496 to 2.84680; 026 against 022 has 9 decreases and 16 increases, the largest decrease 0.965082 at
    (19,2400); the held-in row values quoted in the tables are weak_tests3 m proxies, not raw pairings I (the raw final pairings are in the run logs: 025 8e-10 to 9.9e-8,
    026 4e-10 to 3.5e-8); the 024 MID16 label is wrong (MID 32 rule); three optimizer lines were truncated in v13's tables (a fixed-offset slice of the FINAL log line in fill_v13.py; v14 prints the full line after the rule prefix); the per-step density step norms are FLOAT mesh
    values of this lane, not certified bounds; '016 seven-cell pending' was stale (the N3 numerics worker's exact modes-1+3 values agree, CLAIMED pending the N4 numerical auditor).
(d) 027 and 028: snapshots and per-probe tables in sections 2c and 2d (027 held-out table was reported 13:38Z as a trial comparison before its snapshot).

## 1. C1-N1-024 (MID 32 rule control of 016; 12 steps; held-out file heldout/HELDOUT_024.md, current sha256 e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab; RULED OUT, section 0 (a))
Run: the same start (exact quotient of 013 + 252 legqs R0 = 25 in m = 9..15, zero start; 2174 generators), the same 67 rows (weight 1e12) and the same 12 GN steps as 016, but the optimization objective evaluated on the MID 32 radial rule (016: MID 16) and on the GPU (016: CPU; N4-342 notes the backend change). HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}. Snapshot C1-N1-024-rulem32-legqs25 (11:31:32Z).
Exact JSON sha256 3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d; 2174 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  11 obj 1.512497e+07 -> 1.509028e+07 ACC pred 3.665e+04 lam 4.1e-03 dRho2 1.470e-03 dCoef 8.080e-06 parts F 1.322e+07 G 2.219e+05 P 4.392e+04 K 1.6.
Optimizer report (MID 32): P2 2.095659e+02 G1 3.680307e+00 G0 3.275353e-01 rF 7.170395e+00 supF 1.8588e-01
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
Optimizer report (MID 16): P2 2.453457e+02 G1 4.059903e+00 G0 3.045846e-01 rF 5.867089e+00 supF 1.4928e-01
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

## 2b. C1-N1-026 (022 continued with the 14 mid-field rows at weight 1e16; 60 steps)
Run: the 022 state (2414 generators; no new functions) continued 60 GN steps with the 81 rows of 025 (the 14 mid-field rows at weight 1e16); HELD-OUT as 025 (file heldout/HELDOUT_026.md, sha256 2016d960c982aeffa2b1bef5aaece9b7394e97139d9688b5f6abec3274606d15, written before the 11:31Z launch). Separates the row effect from the scale-100 basis effect of 025.
Exact JSON sha256 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3; 2414 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  60 obj 1.389229e+07 -> 1.389191e+07 ACC pred 2.700e+05 lam 8.2e-06 dRho2 1.550e-03 dCoef 4.125e-04 parts F 1.202e+07 G 2.146e+05 P 5.005e+04 K 1.6.
Optimizer report (MID 16): P2 2.237107e+02 G1 3.619349e+00 G0 2.783357e-01 rF 6.836564e+00 supF 1.3863e-01
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

## 2c. C1-N1-027 (control for 026: 022 continued 60 steps with the plain 67 rows; held-out file heldout/HELDOUT_027.md sha256 c99eb804dc6c390c4db9d9cfb7a5231a9b982a93f1c1b2b501e9b20af4829d7e, written before launch)
Run: the 022 state (2414 generators) continued 60 GN steps with the plain 67 rows of 016 (weight 1e12; no held-in rows), MID 16, GPU 7: the control for 026 (same start, steps and rule; only the 14 rows at 1e16 differ). HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}.
Exact JSON sha256 a3bd6a5152716b05baf2c377c9bb253e73e20024515558632349119157624b40; 2414 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  60 obj 1.357063e+07 -> 1.356835e+07 ACC pred 2.160e+03 lam 7.4e-03 dRho2 4.246e-04 dCoef 1.943e-06 parts F 1.174e+07 G 1.915e+05 P 3.998e+04 K 1.6.
Optimizer report (MID 16): P2 1.999569e+02 G1 3.418411e+00 G0 2.756878e-01 rF 6.764741e+00 supF 1.2346e-01
FLOAT (diag2, MID 32): G0 0.2762 (016 0.3089, 022 0.2816, 023 0.3228), G1 3.426, P2 199.7, rF 6.820, H 0.6101, sup|F| 0.1240, theta_inner 0.0114, kappa_inner 0.7301 ((B-L2) margin +0.0689).
First-mode weak probes (27 sampled k <= 4096, objective rows): largest sampled value 1.78e-04 at k = 2048 (a sampled maximum, not a bound; 016 1.50e-4 at k = 2048).
| probe (n, K) | r_peak | 016 | 022 | 026 | 027 |
|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | 8.18e-06 | 5.91e-05 | 1.48e-04 | 4.88e-05 |
| (19, 900) [registered, HELD OUT] | 25 | 5.31e-04 | 5.23e-04 | 5.94e-04 | 5.15e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | 8.16e-04 | 7.61e-04 | 8.06e-04 | 7.54e-04 |
| (19, 1800) [registered, HELD OUT] | 35 | 9.02e-04 | 8.30e-04 | 8.32e-04 | 8.25e-04 |
| (19, 2400) [registered, HELD OUT] | 40 | 7.44e-04 | 6.90e-04 | 6.66e-04 | 6.88e-04 |
| (23, 600) [registered, HELD OUT] | 20 | 2.17e-04 | 1.65e-04 | 3.27e-05 | 1.80e-04 |
| (23, 900) [registered, HELD OUT] | 25 | 2.80e-05 | 7.74e-05 | 2.59e-04 | 6.55e-05 |
| (23, 1200) [registered, HELD OUT] | 28 | 2.97e-04 | 3.19e-04 | 4.67e-04 | 3.09e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | 5.94e-04 | 5.85e-04 | 6.74e-04 | 5.76e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | 6.50e-04 | 6.44e-04 | 6.95e-04 | 6.37e-04 |
| (25, 600) [registered, HELD OUT] | 20 | 1.94e-04 | 1.64e-04 | 3.53e-06 | 1.81e-04 |
| (25, 900) [registered, HELD OUT] | 25 | 8.93e-05 | 4.02e-05 | 1.08e-04 | 5.39e-05 |
| (25, 1200) [registered, HELD OUT] | 28 | 1.16e-04 | 1.49e-04 | 2.69e-04 | 1.35e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | 4.19e-04 | 4.18e-04 | 4.84e-04 | 4.05e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | 5.37e-04 | 5.27e-04 | 5.52e-04 | 5.13e-04 |
| (29, 600) [registered, HELD OUT] | 20 | 8.70e-05 | 9.78e-05 | 3.00e-05 | 1.14e-04 |
| (29, 900) [registered, HELD OUT] | 25 | 1.62e-04 | 1.24e-04 | 5.69e-05 | 1.35e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | 9.65e-05 | 4.64e-05 | 1.05e-05 | 5.57e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | 1.19e-04 | 1.52e-04 | 1.85e-04 | 1.45e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | 2.72e-04 | 2.85e-04 | 2.98e-04 | 2.82e-04 |
| (31, 600) [registered, HELD OUT] | 20 | 7.85e-05 | 6.17e-05 | 2.93e-05 | 7.73e-05 |
| (31, 900) [registered, HELD OUT] | 25 | 1.66e-04 | 1.22e-04 | 8.64e-05 | 1.32e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | 1.27e-04 | 8.98e-05 | 5.56e-05 | 9.67e-05 |
| (31, 1800) [registered, HELD OUT] | 35 | 5.42e-05 | 6.01e-05 | 8.47e-05 | 5.66e-05 |
| (31, 2400) [registered, HELD OUT] | 40 | 1.99e-04 | 1.88e-04 | 2.03e-04 | 1.87e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.69e-04 | 8.72e-05 | 2.56e-07 | 9.88e-05 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 2.33e-04 | 1.66e-04 | 1.85e-06 | 1.88e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 2.32e-04 | 1.94e-04 | 2.04e-06 | 2.11e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 1.70e-04 | 1.58e-04 | 1.66e-06 | 1.76e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 1.04e-04 | 1.15e-04 | 1.15e-06 | 1.32e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 3.77e-05 | 6.60e-05 | 5.72e-07 | 8.44e-05 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 3.26e-05 | 3.06e-05 | 1.92e-07 | 4.80e-05 |
| (19, 137) [N4-160 K0 = 128, HELD OUT] | 10 | 1.26e-04 | 2.76e-05 | 1.49e-08 | 2.07e-05 |
| (21, 138) [N4-160 K0 = 128, HELD OUT] | 10 | 1.91e-04 | 9.59e-05 | 5.31e-08 | 6.00e-05 |
| (23, 139) [N4-160 K0 = 128, HELD OUT] | 10 | 1.55e-04 | 7.69e-05 | 4.96e-08 | 5.37e-05 |
| (25, 140) [N4-160 K0 = 128, HELD OUT] | 10 | 1.08e-04 | 6.07e-05 | 3.85e-08 | 4.08e-05 |
| (27, 141) [N4-160 K0 = 128, HELD OUT] | 10 | 7.21e-05 | 5.45e-05 | 2.64e-08 | 3.68e-05 |
| (29, 142) [N4-160 K0 = 128, HELD OUT] | 10 | 5.48e-05 | 3.94e-05 | 1.29e-08 | 2.79e-05 |
| (31, 143) [N4-160 K0 = 128, HELD OUT] | 10 | 5.25e-05 | 2.66e-05 | 4.62e-09 | 2.15e-05 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.06e-05 | 2.48e-05 | 5.84e-05 | 4.98e-05 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 4.61e-05 | 4.54e-06 | 1.57e-04 | 1.83e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.36e-05 | 2.38e-05 | 8.95e-05 | 1.88e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 5.36e-05 | 9.22e-06 | 9.91e-05 | 5.45e-06 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 1.83e-06 | 3.96e-06 | 4.65e-05 | 1.55e-05 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 1.25e-05 | 2.10e-05 | 2.09e-05 | 2.56e-06 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 1.01e-05 | 6.28e-06 | 9.35e-06 | 1.77e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 6.21e-06 | 1.12e-04 | 9.74e-05 | 1.03e-04 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 2.04e-05 | 4.39e-05 | 1.32e-04 | 3.95e-05 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.84e-06 | 8.89e-06 | 6.08e-05 | 2.22e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 3.15e-05 | 2.21e-05 | 3.32e-05 | 9.52e-06 |
Largest held-out value over the 25 registered probes: (19, 1800) 8.25e-04; 7 of 25 above the graded ceiling 4.5717e-4 (016: (19, 1800) 9.02e-4, 7 of 25; 022: 8.30e-4, 7; 023: 1.62e-3, 10).
Per-probe statements (FLOAT, MID 32; the 25 registered probes, value old -> value new (factor)); 027 against 022 reproduces the N4-375 reading (extrema 0.8259 at (19,600) and 1.3432 at (25,900); 16 decreases, 9 increases; all ten K >= 1800 probes decrease). No uniform statement across the probes is made.
- 027 vs 022 (022 -> 027): (19, 600) 5.91e-05 -> 4.88e-05 (x0.83); (19, 900) 5.23e-04 -> 5.15e-04 (x0.98); (19, 1200) 7.61e-04 -> 7.54e-04 (x0.99); (19, 1800) 8.30e-04 -> 8.25e-04 (x0.99); (19, 2400) 6.90e-04 -> 6.88e-04 (x1.00); (23, 600) 1.65e-04 -> 1.80e-04 (x1.09); (23, 900) 7.74e-05 -> 6.55e-05 (x0.85); (23, 1200) 3.19e-04 -> 3.09e-04 (x0.97); (23, 1800) 5.85e-04 -> 5.76e-04 (x0.99); (23, 2400) 6.44e-04 -> 6.37e-04 (x0.99); (25, 600) 1.64e-04 -> 1.81e-04 (x1.10); (25, 900) 4.02e-05 -> 5.39e-05 (x1.34); (25, 1200) 1.49e-04 -> 1.35e-04 (x0.91); (25, 1800) 4.18e-04 -> 4.05e-04 (x0.97); (25, 2400) 5.27e-04 -> 5.13e-04 (x0.97); (29, 600) 9.78e-05 -> 1.14e-04 (x1.17); (29, 900) 1.24e-04 -> 1.35e-04 (x1.09); (29, 1200) 4.64e-05 -> 5.57e-05 (x1.20); (29, 1800) 1.52e-04 -> 1.45e-04 (x0.96); (29, 2400) 2.85e-04 -> 2.82e-04 (x0.99); (31, 600) 6.17e-05 -> 7.73e-05 (x1.25); (31, 900) 1.22e-04 -> 1.32e-04 (x1.08); (31, 1200) 8.98e-05 -> 9.67e-05 (x1.08); (31, 1800) 6.01e-05 -> 5.66e-05 (x0.94); (31, 2400) 1.88e-04 -> 1.87e-04 (x0.99) Counts and factors:decreases 16, increases 9; min factor 0.8259 at (19, 600), max 1.3432 at (25, 900); K >= 1800 factors: (19, 1800) 0.9946, (19, 2400) 0.9969, (23, 1800) 0.9851, (23, 2400) 0.9892, (25, 1800) 0.9679, (25, 2400) 0.9745, (29, 1800) 0.9587, (29, 2400) 0.9878, (31, 1800) 0.9415, (31, 2400) 0.9929.
- 027 vs 026 (026 -> 027; same start, steps and rule; the row set differs): (19, 600) 1.48e-04 -> 4.88e-05 (x0.33); (19, 900) 5.94e-04 -> 5.15e-04 (x0.87); (19, 1200) 8.06e-04 -> 7.54e-04 (x0.94); (19, 1800) 8.32e-04 -> 8.25e-04 (x0.99); (19, 2400) 6.66e-04 -> 6.88e-04 (x1.03); (23, 600) 3.27e-05 -> 1.80e-04 (x5.51); (23, 900) 2.59e-04 -> 6.55e-05 (x0.25); (23, 1200) 4.67e-04 -> 3.09e-04 (x0.66); (23, 1800) 6.74e-04 -> 5.76e-04 (x0.86); (23, 2400) 6.95e-04 -> 6.37e-04 (x0.92); (25, 600) 3.53e-06 -> 1.81e-04 (x51.29); (25, 900) 1.08e-04 -> 5.39e-05 (x0.50); (25, 1200) 2.69e-04 -> 1.35e-04 (x0.50); (25, 1800) 4.84e-04 -> 4.05e-04 (x0.84); (25, 2400) 5.52e-04 -> 5.13e-04 (x0.93); (29, 600) 3.00e-05 -> 1.14e-04 (x3.81); (29, 900) 5.69e-05 -> 1.35e-04 (x2.38); (29, 1200) 1.05e-05 -> 5.57e-05 (x5.32); (29, 1800) 1.85e-04 -> 1.45e-04 (x0.79); (29, 2400) 2.98e-04 -> 2.82e-04 (x0.95); (31, 600) 2.93e-05 -> 7.73e-05 (x2.64); (31, 900) 8.64e-05 -> 1.32e-04 (x1.53); (31, 1200) 5.56e-05 -> 9.67e-05 (x1.74); (31, 1800) 8.47e-05 -> 5.66e-05 (x0.67); (31, 2400) 2.03e-04 -> 1.87e-04 (x0.92) Counts and factors:decreases 16, increases 9; min factor 0.2532 at (23, 900), max 51.2914 at (25, 600); K >= 1800 factors: (19, 1800) 0.9921, (19, 2400) 1.0330, (23, 1800) 0.8551, (23, 2400) 0.9168, (25, 1800) 0.8368, (25, 2400) 0.9291, (29, 1800) 0.7866, (29, 2400) 0.9451, (31, 1800) 0.6675, (31, 2400) 0.9223.

## 2d. C1-N1-028 (022 + 252 legqs R0 = 25 functions n = 12..23 in m = 9..15; 2666 generators; 67 rows; 60 steps; held-out file heldout/HELDOUT_028.md sha256 caf3517ad1961fa1587a976bb14f879a81ab54d05c1c65d68b7c9c5b58187835, written before launch)
Run: the 022 state + 252 legqs R0 = 25 functions n = 12..23 in j = 1..3, m = 9..15 (2666 generators), plain 67 rows, 60 GN steps, MID 16, GPU 7. HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}. Compared per probe with 022 and 027 (same start; 027 has the same steps and no new functions).
Exact JSON sha256 70afa847663c4ba0c6af4023800c1529171506cbd94ec0e0df542e24ae3206f2; 2666 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  60 obj 1.282224e+07 -> 1.280816e+07 ACC pred 4.871e+05 lam 2.5e-04 dRho2 1.728e-03 dCoef 1.175e-04 parts F 1.099e+07 G 1.733e+05 P 3.895e+04 K 1.6.
Optimizer report (MID 16): P2 1.973494e+02 G1 3.252719e+00 G0 2.436548e-01 rF 6.550651e+00 supF 1.2899e-01
diag2 (MID 32 norms, (B-L2) screening): PENDING.
| probe (n, K) | r_peak | 016 | 022 | 027 | 028 |
|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | 8.18e-06 | 5.91e-05 | 4.88e-05 | 6.12e-05 |
| (19, 900) [registered, HELD OUT] | 25 | 5.31e-04 | 5.23e-04 | 5.15e-04 | 4.51e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | 8.16e-04 | 7.61e-04 | 7.54e-04 | 7.18e-04 |
| (19, 1800) [registered, HELD OUT] | 35 | 9.02e-04 | 8.30e-04 | 8.25e-04 | 8.15e-04 |
| (19, 2400) [registered, HELD OUT] | 40 | 7.44e-04 | 6.90e-04 | 6.88e-04 | 6.86e-04 |
| (23, 600) [registered, HELD OUT] | 20 | 2.17e-04 | 1.65e-04 | 1.80e-04 | 2.77e-04 |
| (23, 900) [registered, HELD OUT] | 25 | 2.80e-05 | 7.74e-05 | 6.55e-05 | 3.14e-06 |
| (23, 1200) [registered, HELD OUT] | 28 | 2.97e-04 | 3.19e-04 | 3.09e-04 | 2.74e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | 5.94e-04 | 5.85e-04 | 5.76e-04 | 5.78e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | 6.50e-04 | 6.44e-04 | 6.37e-04 | 6.61e-04 |
| (25, 600) [registered, HELD OUT] | 20 | 1.94e-04 | 1.64e-04 | 1.81e-04 | 2.74e-04 |
| (25, 900) [registered, HELD OUT] | 25 | 8.93e-05 | 4.02e-05 | 5.39e-05 | 1.19e-04 |
| (25, 1200) [registered, HELD OUT] | 28 | 1.16e-04 | 1.49e-04 | 1.35e-04 | 9.47e-05 |
| (25, 1800) [registered, HELD OUT] | 35 | 4.19e-04 | 4.18e-04 | 4.05e-04 | 3.99e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | 5.37e-04 | 5.27e-04 | 5.13e-04 | 5.30e-04 |
| (29, 600) [registered, HELD OUT] | 20 | 8.70e-05 | 9.78e-05 | 1.14e-04 | 1.87e-04 |
| (29, 900) [registered, HELD OUT] | 25 | 1.62e-04 | 1.24e-04 | 1.35e-04 | 1.95e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | 9.65e-05 | 4.64e-05 | 5.57e-05 | 9.86e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | 1.19e-04 | 1.52e-04 | 1.45e-04 | 1.31e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | 2.72e-04 | 2.85e-04 | 2.82e-04 | 2.88e-04 |
| (31, 600) [registered, HELD OUT] | 20 | 7.85e-05 | 6.17e-05 | 7.73e-05 | 1.38e-04 |
| (31, 900) [registered, HELD OUT] | 25 | 1.66e-04 | 1.22e-04 | 1.32e-04 | 1.87e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | 1.27e-04 | 8.98e-05 | 9.67e-05 | 1.40e-04 |
| (31, 1800) [registered, HELD OUT] | 35 | 5.42e-05 | 6.01e-05 | 5.66e-05 | 3.55e-05 |
| (31, 2400) [registered, HELD OUT] | 40 | 1.99e-04 | 1.88e-04 | 1.87e-04 | 1.82e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.69e-04 | 8.72e-05 | 9.88e-05 | 2.24e-04 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 2.33e-04 | 1.66e-04 | 1.88e-04 | 3.04e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 2.32e-04 | 1.94e-04 | 2.11e-04 | 3.16e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 1.70e-04 | 1.58e-04 | 1.76e-04 | 2.74e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 1.04e-04 | 1.15e-04 | 1.32e-04 | 2.17e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 3.77e-05 | 6.60e-05 | 8.44e-05 | 1.58e-04 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 3.26e-05 | 3.06e-05 | 4.80e-05 | 1.07e-04 |
| (19, 137) [N4-160 K0 = 128, HELD OUT] | 10 | 1.26e-04 | 2.76e-05 | 2.07e-05 | 1.37e-04 |
| (21, 138) [N4-160 K0 = 128, HELD OUT] | 10 | 1.91e-04 | 9.59e-05 | 6.00e-05 | 3.12e-05 |
| (23, 139) [N4-160 K0 = 128, HELD OUT] | 10 | 1.55e-04 | 7.69e-05 | 5.37e-05 | 1.26e-05 |
| (25, 140) [N4-160 K0 = 128, HELD OUT] | 10 | 1.08e-04 | 6.07e-05 | 4.08e-05 | 1.41e-05 |
| (27, 141) [N4-160 K0 = 128, HELD OUT] | 10 | 7.21e-05 | 5.45e-05 | 3.68e-05 | 4.71e-05 |
| (29, 142) [N4-160 K0 = 128, HELD OUT] | 10 | 5.48e-05 | 3.94e-05 | 2.79e-05 | 4.22e-05 |
| (31, 143) [N4-160 K0 = 128, HELD OUT] | 10 | 5.25e-05 | 2.66e-05 | 2.15e-05 | 5.69e-05 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.06e-05 | 2.48e-05 | 4.98e-05 | 2.03e-04 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 4.61e-05 | 4.54e-06 | 1.83e-05 | 1.58e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.36e-05 | 2.38e-05 | 1.88e-05 | 1.00e-04 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 5.36e-05 | 9.22e-06 | 5.45e-06 | 5.53e-06 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 1.83e-06 | 3.96e-06 | 1.55e-05 | 5.33e-05 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 1.25e-05 | 2.10e-05 | 2.56e-06 | 1.72e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 1.01e-05 | 6.28e-06 | 1.77e-05 | 3.08e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 6.21e-06 | 1.12e-04 | 1.03e-04 | 2.76e-04 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 2.04e-05 | 4.39e-05 | 3.95e-05 | 1.35e-04 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.84e-06 | 8.89e-06 | 2.22e-05 | 6.20e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 3.15e-05 | 2.21e-05 | 9.52e-06 | 3.75e-06 |
Largest held-out value over the 25 registered probes: (19, 1800) 8.15e-04; 6 of 25 above the graded ceiling 4.5717e-4 (016: (19, 1800) 9.02e-4, 7 of 25; 022: 8.30e-4, 7; 023: 1.62e-3, 10).
Per-probe statements (FLOAT, MID 32; the 25 registered probes, value old -> value new (factor)). H18 check of this lane (the coordinator 14:29Z part 8): against the matched control 027, 028 moves eleven of the fifteen K <= 1200 probes by more than the 027/022 continuation band (0.826 to 1.343) in both directions and none of the ten K >= 1800 probes except (31,1800) (0.63); the earlier reading that the registered probes "did not respond to any basis change beyond 016's scale-25 functions" is therefore amended in NUMERICS_FINAL section 9 to the per-probe statement. No uniform statement across the probes is made.
- 028 vs 022 (022 -> 028): (19, 600) 5.91e-05 -> 6.12e-05 (x1.03); (19, 900) 5.23e-04 -> 4.51e-04 (x0.86); (19, 1200) 7.61e-04 -> 7.18e-04 (x0.94); (19, 1800) 8.30e-04 -> 8.15e-04 (x0.98); (19, 2400) 6.90e-04 -> 6.86e-04 (x0.99); (23, 600) 1.65e-04 -> 2.77e-04 (x1.68); (23, 900) 7.74e-05 -> 3.14e-06 (x0.04); (23, 1200) 3.19e-04 -> 2.74e-04 (x0.86); (23, 1800) 5.85e-04 -> 5.78e-04 (x0.99); (23, 2400) 6.44e-04 -> 6.61e-04 (x1.03); (25, 600) 1.64e-04 -> 2.74e-04 (x1.66); (25, 900) 4.02e-05 -> 1.19e-04 (x2.97); (25, 1200) 1.49e-04 -> 9.47e-05 (x0.64); (25, 1800) 4.18e-04 -> 3.99e-04 (x0.95); (25, 2400) 5.27e-04 -> 5.30e-04 (x1.01); (29, 600) 9.78e-05 -> 1.87e-04 (x1.91); (29, 900) 1.24e-04 -> 1.95e-04 (x1.58); (29, 1200) 4.64e-05 -> 9.86e-05 (x2.12); (29, 1800) 1.52e-04 -> 1.31e-04 (x0.86); (29, 2400) 2.85e-04 -> 2.88e-04 (x1.01); (31, 600) 6.17e-05 -> 1.38e-04 (x2.23); (31, 900) 1.22e-04 -> 1.87e-04 (x1.53); (31, 1200) 8.98e-05 -> 1.40e-04 (x1.56); (31, 1800) 6.01e-05 -> 3.55e-05 (x0.59); (31, 2400) 1.88e-04 -> 1.82e-04 (x0.97) Counts and factors:decreases 12, increases 13; min factor 0.0405 at (23, 900), max 2.9729 at (25, 900); K >= 1800 factors: (19, 1800) 0.9816, (19, 2400) 0.9947, (23, 1800) 0.9879, (23, 2400) 1.0261, (25, 1800) 0.9542, (25, 2400) 1.0070, (29, 1800) 0.8633, (29, 2400) 1.0084, (31, 1800) 0.5917, (31, 2400) 0.9651.
- 028 vs 027 (027 -> 028): (19, 600) 4.88e-05 -> 6.12e-05 (x1.25); (19, 900) 5.15e-04 -> 4.51e-04 (x0.87); (19, 1200) 7.54e-04 -> 7.18e-04 (x0.95); (19, 1800) 8.25e-04 -> 8.15e-04 (x0.99); (19, 2400) 6.88e-04 -> 6.86e-04 (x1.00); (23, 600) 1.80e-04 -> 2.77e-04 (x1.54); (23, 900) 6.55e-05 -> 3.14e-06 (x0.05); (23, 1200) 3.09e-04 -> 2.74e-04 (x0.89); (23, 1800) 5.76e-04 -> 5.78e-04 (x1.00); (23, 2400) 6.37e-04 -> 6.61e-04 (x1.04); (25, 600) 1.81e-04 -> 2.74e-04 (x1.51); (25, 900) 5.39e-05 -> 1.19e-04 (x2.21); (25, 1200) 1.35e-04 -> 9.47e-05 (x0.70); (25, 1800) 4.05e-04 -> 3.99e-04 (x0.99); (25, 2400) 5.13e-04 -> 5.30e-04 (x1.03); (29, 600) 1.14e-04 -> 1.87e-04 (x1.63); (29, 900) 1.35e-04 -> 1.95e-04 (x1.44); (29, 1200) 5.57e-05 -> 9.86e-05 (x1.77); (29, 1800) 1.45e-04 -> 1.31e-04 (x0.90); (29, 2400) 2.82e-04 -> 2.88e-04 (x1.02); (31, 600) 7.73e-05 -> 1.38e-04 (x1.78); (31, 900) 1.32e-04 -> 1.87e-04 (x1.42); (31, 1200) 9.67e-05 -> 1.40e-04 (x1.45); (31, 1800) 5.66e-05 -> 3.55e-05 (x0.63); (31, 2400) 1.87e-04 -> 1.82e-04 (x0.97) Counts and factors:decreases 11, increases 14; min factor 0.0479 at (23, 900), max 2.2133 at (25, 900); K >= 1800 factors: (19, 1800) 0.9870, (19, 2400) 0.9977, (23, 1800) 1.0029, (23, 2400) 1.0374, (25, 1800) 0.9858, (25, 2400) 1.0334, (29, 1800) 0.9005, (29, 2400) 1.0208, (31, 1800) 0.6284, (31, 2400) 0.9719.
- 028 vs 016 (016 -> 028): (19, 600) 8.18e-06 -> 6.12e-05 (x7.48); (19, 900) 5.31e-04 -> 4.51e-04 (x0.85); (19, 1200) 8.16e-04 -> 7.18e-04 (x0.88); (19, 1800) 9.02e-04 -> 8.15e-04 (x0.90); (19, 2400) 7.44e-04 -> 6.86e-04 (x0.92); (23, 600) 2.17e-04 -> 2.77e-04 (x1.28); (23, 900) 2.80e-05 -> 3.14e-06 (x0.11); (23, 1200) 2.97e-04 -> 2.74e-04 (x0.92); (23, 1800) 5.94e-04 -> 5.78e-04 (x0.97); (23, 2400) 6.50e-04 -> 6.61e-04 (x1.02); (25, 600) 1.94e-04 -> 2.74e-04 (x1.41); (25, 900) 8.93e-05 -> 1.19e-04 (x1.34); (25, 1200) 1.16e-04 -> 9.47e-05 (x0.82); (25, 1800) 4.19e-04 -> 3.99e-04 (x0.95); (25, 2400) 5.37e-04 -> 5.30e-04 (x0.99); (29, 600) 8.70e-05 -> 1.87e-04 (x2.15); (29, 900) 1.62e-04 -> 1.95e-04 (x1.21); (29, 1200) 9.65e-05 -> 9.86e-05 (x1.02); (29, 1800) 1.19e-04 -> 1.31e-04 (x1.10); (29, 2400) 2.72e-04 -> 2.88e-04 (x1.06); (31, 600) 7.85e-05 -> 1.38e-04 (x1.76); (31, 900) 1.66e-04 -> 1.87e-04 (x1.13); (31, 1200) 1.27e-04 -> 1.40e-04 (x1.10); (31, 1800) 5.42e-05 -> 3.55e-05 (x0.66); (31, 2400) 1.99e-04 -> 1.82e-04 (x0.91) Counts and factors:decreases 12, increases 13; min factor 0.1119 at (23, 900), max 7.4801 at (19, 600); K >= 1800 factors: (19, 1800) 0.9030, (19, 2400) 0.9227, (23, 1800) 0.9721, (23, 2400) 1.0181, (25, 1800) 0.9526, (25, 2400) 0.9881, (29, 1800) 1.1006, (29, 2400) 1.0564, (31, 1800) 0.6554, (31, 2400) 0.9121.

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
| C1-N1-027 | 1.356835e+07 | 0.2762 | 3.426 | 199.7 | 6.820 | 0.6101 | 0.1240 | 0.7301 | (19, 1800): 8.25e-04 | 1.88e-04 | 8.25e-04 | 6.37e-04 |
| C1-N1-028 | 1.280816e+07 | - | - | - | - | - | - | - | (19, 1800): 8.15e-04 | 3.04e-04 | 8.15e-04 | 6.61e-04 |
All FLOAT (diag2 MID 32; weak_tests3 MID 32; LOSS = last accepted objective on the MID 16 rule, comparable only within the same row set: 016 to 020, 022, 023 use 67 rows; 021 and 025 use 81 rows, so their LOSS includes 14 more penalty rows). Certified floors (CONFIRMED): 016 > 0.0014703, 017 > 0.0016718, 018 > 0.0016558, 019 > 0.0016618, 020 > 0.0018553, 021 > 0.0018646 at (19,1800); printed digits rounded down from the certified roots.

## 6. Status and next runs
1. Reading of the GPU phase (FLOAT trial comparisons at the tested probes; no span, mass, stationarity or causal inference): among the basis and objective changes tested
   from 016 on, the registered mid-field held-out values (modes 19 to 31, r 20 to 50; largest at (19,1800)) changed as follows, per probe (sections 1, 2, 2b, 2c, 2d and
   numerics_v11 to v13): scale 50 (017, 020) and scale 100 (023) raised most of the 25 (023: 22 of 25, factors 1.09 to 26.2); the higher blocks m = 16..23 (022) gave
   factors 0.45 to 7.2 against 016 with 0.92 at (19,1800); more steps (027 against 022: 16 decreases, 9 increases, factors 0.826 to 1.343, all ten K >= 1800 probes
   decreasing by 0.9415 to 0.9969); the 14 mid-field pairing rows at weight 1e16 (025, 026) are satisfied to 1e-9 to 6e-6 while the registered probes move in both
   directions (026 against 022: 9 decreases, 16 increases, K >= 1800 factors 0.965 to 1.41); the 252 added scale-25 radial functions n = 12..23 in m = 9..15 (028 against
   027): 11 decreases, 14 increases, K >= 1800 factors 0.63 ((31,1800)) and 0.90 to 1.04, K <= 1200 factors 0.05 ((23,900)) to 2.21 ((25,900)). No uniform statement
   holds across the probes. The largest registered value is 8.15e-4 at (19,1800) for 028 (027 8.25e-4, 022 8.30e-4, 016 9.02e-4), 1.78 times the graded ceiling 4.5717e-4;
   6 of 25 values of 028 exceed it (027, 022: 7). G0 (MID 16) fell along 016 -> 022 -> 027 -> 028: 0.3084, 0.2811, 0.2757, 0.2437; sup|F| 0.1290 for 028 against 0.1235 (027).
2. Runs: none running after 028's diag2 (about 15:15Z; weak_tests2 since 14:24Z); 027 and 028 were the last runs of this lane (H16 line). Snapshots 027 (14:13:51Z) and 028 (after diag2) are
   immutable in working file candidate_snapshots (not published) with their pre-launch held-out files bound in the MANIFEST descriptions.
3. Certification targets: none. Every snapshot through 026 is RULED OUT in every registered scalar ball and original graded box (011 excepted, FLOAT comparison; 026 since
   matrix v132/v133 by T4-446 to T4-450 with N4-377 to N4-379); 027 and 028 have FLOAT values only and are trial comparisons (the coordinator 13:41Z item 3: audited only if a
   certification target is named; none is). The N3 numerics worker's exact 016 and 017 legqs norms (016 G0, rF, G1 CONFIRMED N4-341/N4-373, P2 under comparison; 017 complete, CLAIMED) are
   the only exact norms of legqs candidates; 017's exact H <= 0.787447783373 (the N3 numerics worker 14:17Z) against this lane's FLOAT 0.6153; 017's seven cells all excluded (the N3 numerics worker 14:22Z,
   CLAIMED), as this lane's FLOAT proxies indicated. The two-scale product keys for 020 to 028 are not available, so no exact norm of 020 to 028 exists.
4. Final deliverables of this lane: NUMERICS_FINAL.md (sections 0, 4, 7b, 9 complete, every number FLOAT-labelled or cited by ID) and artifacts/README.md by 19:00Z;
   ACK of theory_v08 within the hour of its stamp.

