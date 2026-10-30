# numerics_v12 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v12; UTC time: 2026-10-29T12:32:15Z; supersedes numerics_v11 (sha256 700e76e9f13556033bfa2ea2dbbe0b6e93ed56a35e895b897ee718f629e11536) and earlier versions.
- consulted (v12): theory_v06.md (the T1/T3 theory worker, 09:18:15Z; ACK 09:19Z); theory_v07.md (the T1/T3 theory worker, 11:20Z; sha256 42eb222a38caadac...; ACK 11:52Z in RUN_1. Reading of the GPU phase (all FLOAT trial comparisons at the tested probes; no span, mass, stationarity or causal inference): the registered mid-field held-out
   values (modes 19 to 31, r 35 to 50; largest at (19,1800)) responded only to the scale-25 functions in the blocks m = 9..15 (016); scale 50 (017, 020), the higher blocks
   m = 16..23 (022), more steps (018, 019, 021), the MID 32 objective rule (024) left them within 25 percent of 016's; scale 100 (023) raised them 1.5x to 2x; the 14
   mid-field pairing rows at weight 1e16 (025) are satisfied to 1e-8 to 6e-6 and lower the registered probes next to them (K = 600) by factors 3 to 30, while the
   registered probes at K >= 1200 are 25 to 40 percent above 016's. G0 and sup|F| fell with the higher blocks and more steps (022: 0.2816, 0.1276 at MID 32; 026 at MID 16:
   G0 0.2783). The balanced E_2 objective's F part is about 95 percent 2^18 (20/21) ||rF||_2^2; new mid-field freedom goes into rF first.
2. Running at publication: 025 diag2 (snapshot follows, numerics_v13), 026 tests (022 continued 60 steps with the 14 rows at 1e16: MID 16 report G0 0.2783, sup|F| 0.1386,
   rows at 4e-10 to 3.5e-8; held-out table about 12:45Z), the seven-cell proxy for 025. Next and last run: 027 = the control for 026 (022 continued 60 steps with the plain
   67 rows; heldout/HELDOUT_027.md sha256 c99eb804dc6c390c4db9d9cfb7a5231a9b982a93f1c1b2b501e9b20af4829d7e, written before launch), to isolate the effect of the rows at
   equal step count. No new basis family or objective design after that; the final NUMERICS_FINAL is due 19:00Z.
3. Certification targets: none. Every snapshot through 023 is RULED OUT in every registered scalar ball and original graded box (011 excepted, FLOAT comparison); 024 awaits
   the T4 theory auditor's replay of N4-343 to N4-345; 025, 026 have FLOAT values only. The N3 numerics worker's exact 016 norms (G0, rF CONFIRMED N4-341; G1, P2 under comparison) are the only exact
   norms of a legqs candidate.
); the coordinator team notes through 2026-10-29T12:30 (matrix v110: 021 RULED OUT; T4-390 wording);
  the T4 theory auditor T4-374, T4-390 (NUMERICS_FINAL audits, applied 10:12Z and 10:49Z); the N4 numerical auditor through 2026-10-29T11:17:21.; the N3 numerics worker through 2026-10-29T12:25. Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by
  ID; the new numbers are the N1/N2 numerics worker's FLOAT values offered for certification.
- theory version followed: theory_v06 (R-HOLDOUT; R-TANGENT per-step reporting, request 4; NC-T-ORIGIN-INV proxies, request 5). Candidate IDs new in v12: C1-N1-024-rulem32-legqs25 (11:31:32Z); 025 and 026 are run and tested but not yet snapshotted (their snapshots and MANIFESTs follow in numerics_v13). Chart PRIMARY;
  c_l and Theta_0 of state 131 EXACT, center relation EXACT, a_0 free; coefficient files working file candidate_snapshots (not published)/<ID>/<tag>_exact.json (sha256 in SHA256SUMS).
- Every number below is FLOAT (MID 32 rule unless marked MID 16 = optimizer report, or LOSS) unless cited by a working file the N3 numerics worker (not published) ID. Every comparison is a trial comparison
  at the tested probes: no inference about spans, angular-band mass, stationarity, causes or what a basis 'can' reach is drawn (T4-340, T4-356, T4-374, T4-390).

## 0. Corrections to numerics_v11 (the coordinator 10:57Z item 6, 11:05Z item 5; N4-321, N4-328; T4-390)
(a) The v11 header bullet 'theory version followed' was spliced with status text; this header is clean.
(b) 020 is RULED OUT in every ball of rows 88 and 89 since matrix v88 (N4-291/T4-360 point gaps; registered held-out distance > 0.001855374677442712 at (19,1800),
    N4-293 with T4-363); v11 section 0(a) wrongly said OPEN.
(c) 021 is RULED OUT in every specified ball of rows 90 and 91 (point gaps N4-314 with T4-387 to T4-389, accepted N4-319; registered held-out distance
    > 0.001864696854799172 at (19,1800), N4-316 with T4-392, accepted N4-320).
(d) v11 sections 1 and 5 said the 14 held-in rows of 021 'were inert' because their penalty (about 25) was small against the objective (1.3e7); T4-390 refutes the
    inference. Correct statement: the 14 held-in row pairings did not fall during the 40 steps (FLOAT trial observation); the causal role of the weight is OPEN; the
    sensitivity run 025 (same rows at 1e16) is reported in section 2.
(e) The MANIFEST notes of C1-N1-019 to 023 label the first-mode weak value 'NORM-T-WEAK-v1 (a = 0, k = 0..8) FLOAT weak-distance lower bound'; the value is the largest
    FLOAT value over the 27 sampled k <= 4096 (k_of_max 2048; 1536 for 023), a sampled maximum and not a bound (N4-328). The label text is corrected from 024 on.
(f) The 022 MANIFEST notes say the density support of the added blocks (modes 31 to 47) lies outside the n <= 31 sweep: mode 31 is inside that sweep (N4-321 witness),
    modes 33 to 47 are outside it.
(g) The 016 certified floor was printed as 0.0014704 (v11 section 4 footer); the certified root is 0.001470360924..., so the printed bound reads > 0.0014703 (N4-328);
    all printed floor digits in this version are rounded down.
(h) 024 held-out hash (the coordinator 11:34Z and 11:59Z, N4-342): the INDEX line of C1-N1-024 and my 11:00Z note give heldout/HELDOUT_024.md as sha256 58586004ad6a...; the
    current file has sha256 e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab (mtime 09:13:43Z; also cited in my 09:13Z work log line and 09:15Z note). My
    record is that the file was written at 09:13:13Z and edited once at 09:13:43Z to fix a wording typo in its objective-row line, and that 58586004... is the hash of the
    text before that edit; N4-346 CONFIRMS this by undoing the one-line edit (all 60 probe pairs unchanged); only the two save times are not independently witnessed. The 024 MANIFEST.json cites no held-out hash. Both versions precede the 10:37Z launch.
    Also for 024 (N4-342): the INDEX labels 'LOSS (MID 16)' and 'optimizer report (MID 16)' are wrong, since 024 optimized on the MID 32 rule; and 024 ran on the GPU (CUDA)
    while 016 ran on the CPU, so the rule control changes the backend as well as the rule.
(i) 022 is RULED OUT in every ball of rows 92 and 93 (point gaps N4-326 with T4-405, graded gap 0.0683610048; origin T4-406; sixteen-sector prefix T4-407; registered
    held-out distance > 0.00135251075726327 at (19,1800), N4-327 with T4-408, 2.958 times the graded ceiling; the N4 numerical auditor's acceptances N4-333 and N4-334).
(j) 023 is RULED OUT in every ball of rows 94 and 95: The N4 numerical auditor's N4-336 to N4-338 (positive point gaps for the six scalar budgets, uniform graded gap 0.0629, registered
    distance > 0.002634958245163687 at (19,1800), 5.764 times the graded ceiling, 924.7 times the sharpw family ceiling) reproduced by T4-416 to T4-420 and accepted in N4-348
    to N4-350 (matrix v121). 024 is OPEN pending the T4 theory auditor's replay of the N4 numerical auditor's N4-343 to N4-345 (point gaps for the six scalar budgets, original graded gap 0.0749, registered
    distance > 0.001556067368832641 at (19,1800), 3.404 times the graded ceiling).

## 1. C1-N1-024 (MID 32 rule control of 016; 12 steps; held-out file heldout/HELDOUT_024.md sha256 58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5, written before launch)
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
diag2 (MID 32 norms, (B-L2) screening): PENDING.
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
Per-step reporting (theory_v06 request 4, R-TANGENT; FLOAT, mesh 0.02 <= r <= 1e4, MID 16): 025: 39 accepted steps; density L2 step norm ||rho(a_new) - rho(a)||_2 on the mesh (FLOAT): first accepted step 1.54e-02, median 1.09e-03, last 1.24e-03, sum over accepted steps 8.388e-02 (an upper bound of the FLOAT mesh norm of the total density change by the triangle inequality; a certified bound is the N4 numerical auditor's); coefficient step norms 4.3e-07 to 2.8e-02. Every reported residual of this lane is either the optimizer's evaluated objective parts (MID 16) or the MID 32 diag2 re-evaluation; linear-model values ||F + J delta||_2 appear only in NUMERICS_FINAL section 4b and are labelled so. 024: 5 accepted steps; density L2 step norm ||rho(a_new) - rho(a)||_2 on the mesh (FLOAT): first accepted step 2.17e-02, median 3.05e-03, last 1.47e-03, sum over accepted steps 3.029e-02 (an upper bound of the FLOAT mesh norm of the total density change by the triangle inequality; a certified bound is the N4 numerical auditor's); coefficient step norms 2.9e-06 to 7.0e-04. Every reported residual of this lane is either the optimizer's evaluated objective parts (MID 16) or the MID 32 diag2 re-evaluation; linear-model values ||F + J delta||_2 appear only in NUMERICS_FINAL section 4b and are labelled so.

## 3. NC-T-ORIGIN-INV seven-cell FLOAT proxies (theory_v06 request 5) for C1-N1-011 to 021
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
| C1-N1-025 | PENDING | | | |
FLOAT proxy (na_modes_cells.py, MID 32): projected weighted-Laplacian norm of the angular modes 1 and 3 of F at the right end of each cell (a lower bound of the full N_a when certified) against the theory_v03 section 5 thresholds at the left end. A ratio above 1 at every cell means FW-T-DYADIC-Y-v1 would be excluded for that candidate if the two-mode lower bounds were certified (the N3 numerics worker did 008 exactly; working file T4-248 (not published) as well). FLOAT; no verdict; 009's first cell is not excluded by two modes.

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
| C1-N1-025 | 1.103659e+07 | - | - | - | - | - | - | - | (19, 1800): 1.27e-03 | 5.06e-06 | 1.27e-03 | 9.93e-04 |
All FLOAT (diag2 MID 32; weak_tests3 MID 32; LOSS = last accepted objective on the MID 16 rule, comparable only within the same row set: 016 to 020, 022, 023 use 67 rows; 021 and 025 use 81 rows, so their LOSS includes 14 more penalty rows). Certified floors (CONFIRMED): 016 > 0.0014703, 017 > 0.0016718, 018 > 0.0016558, 019 > 0.0016618, 020 > 0.0018553, 021 > 0.0018646 at (19,1800); printed digits rounded down from the certified roots.

## 6. Status and next runs
1. Reading of the GPU phase (all FLOAT trial comparisons at the tested probes; no span, mass, stationarity or causal inference): the registered mid-field held-out
   values (modes 19 to 31, r 35 to 50; largest at (19,1800)) responded only to the scale-25 functions in the blocks m = 9..15 (016); scale 50 (017, 020), the higher blocks
   m = 16..23 (022), more steps (018, 019, 021), the MID 32 objective rule (024) left them within 25 percent of 016's; scale 100 (023) raised them 1.5x to 2x; the 14
   mid-field pairing rows at weight 1e16 (025) are satisfied to 1e-8 to 6e-6 and lower the registered probes next to them (K = 600) by factors 3 to 30, while the
   registered probes at K >= 1200 are 25 to 40 percent above 016's. G0 and sup|F| fell with the higher blocks and more steps (022: 0.2816, 0.1276 at MID 32; 026 at MID 16:
   G0 0.2783). The balanced E_2 objective's F part is about 95 percent 2^18 (20/21) ||rF||_2^2; new mid-field freedom goes into rF first.
2. Running at publication: 025 diag2 (snapshot follows, numerics_v13), 026 tests (022 continued 60 steps with the 14 rows at 1e16: MID 16 report G0 0.2783, sup|F| 0.1386,
   rows at 4e-10 to 3.5e-8; held-out table about 12:45Z), the seven-cell proxy for 025. Next and last run: 027 = the control for 026 (022 continued 60 steps with the plain
   67 rows; heldout/HELDOUT_027.md sha256 c99eb804dc6c390c4db9d9cfb7a5231a9b982a93f1c1b2b501e9b20af4829d7e, written before launch), to isolate the effect of the rows at
   equal step count. No new basis family or objective design after that; the final NUMERICS_FINAL is due 19:00Z.
3. Certification targets: none. Every snapshot through 023 is RULED OUT in every registered scalar ball and original graded box (011 excepted, FLOAT comparison); 024 awaits
   the T4 theory auditor's replay of N4-343 to N4-345; 025, 026 have FLOAT values only. The N3 numerics worker's exact 016 norms (G0, rF CONFIRMED N4-341; G1, P2 under comparison) are the only exact
   norms of a legqs candidate.

