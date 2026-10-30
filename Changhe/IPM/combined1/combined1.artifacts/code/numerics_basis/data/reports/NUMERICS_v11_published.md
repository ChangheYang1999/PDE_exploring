# numerics_v11 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v11; UTC time: 2026-10-29T10:45:46Z; supersedes numerics_v10 (sha256 3bc798a842539d51642bab035519d20917eabe2433486385587f9e953c17b706) and earlier versions.
- consulted (v11): theory_v05.md (the T1/T3 theory worker, 06:39:59Z; ACK 07:13Z); theory_v06.md (the T1/T3 theory worker; sha256 493549a9b49ac3eb...; ACK in RUN_1. Reading of the 016 family after 021 to 023 (FLOAT, trial comparisons at the tested probes; no span, mass or stationarity inference): the registered mid-field
   held-out values (modes 19 to 31, r 35 to 50) responded to the scale-25 functions in the blocks m = 9..15 (016: factors 2.5 to 5 against 013 at K about 520, 1.2 to 1.5
   at K >= 1200) and to nothing tried since: scale 50 (017, 020), the higher blocks (022, within 10 percent), scale 100 (023: 1.5x to 2x worse), more steps (018, 019,
   021). G0 and sup|F| responded to the higher blocks and to more steps (022: 0.2816 and 0.1276 at MID 32; 007: 0.3767 and 0.138). The balanced E_2 objective is
   dominated by 2^18 (20/21) ||rF||_2^2 (about 95 percent of its F part): new mid-field freedom goes into rF (023: rF 5.88) before G0 or the pairings.
2. The 14 mid-field pairing rows of 021 were inert at weight 1e12 (I about 5e-6 per row); 025 (running; held-out file heldout/HELDOUT_025.md, sha256 6412b262...,
   written before launch) repeats them at 1e16 on the combined basis (2918 generators) with per-step density step norms (R-TANGENT). 024 (MID 32 rule control of 016,
   heldout/HELDOUT_024.md) follows on core 54. Results in numerics_v12.
3. No candidate of this lane is a certification target; the certification requests of this version are nil beyond what the N4 numerical auditor chooses for 022 (structure and point gaps
   would complete its row). The N3 numerics worker's exact legqs norms of 016/017 (target 13:00Z) and the two-scale product keys for 020 to 025 remain the only route to exact norms of
   these candidates.
4. Every FLOAT held-out value above the graded ceiling 4.5717e-4 would, if certified, exclude the candidate from every registered scalar ball and graded box, as for
   016 to 020; the smallest largest-registered-value of the family is 022's 8.30e-4 (1.8 times the graded ceiling; 291 times the unrestricted sharpw ceiling 2.8496e-6).); the coordinator team notes through 2026-10-29T10:44 (08:51Z and 08:55Z wording remarks on v10,
  applied here; matrix v85: 019 RULED OUT, 020 OPEN); the T4 theory auditor T4-340, T4-356 (NUMERICS_FINAL audits); the second model referee pass the second model/finalaudit2/answer.md (54 items, applied to
  NUMERICS_FINAL 09:08Z); the N4 numerical auditor RUN_1. Reading of the 016 family after 021 to 023 (FLOAT, trial comparisons at the tested probes; no span, mass or stationarity inference): the registered mid-field
   held-out values (modes 19 to 31, r 35 to 50) responded to the scale-25 functions in the blocks m = 9..15 (016: factors 2.5 to 5 against 013 at K about 520, 1.2 to 1.5
   at K >= 1200) and to nothing tried since: scale 50 (017, 020), the higher blocks (022, within 10 percent), scale 100 (023: 1.5x to 2x worse), more steps (018, 019,
   021). G0 and sup|F| responded to the higher blocks and to more steps (022: 0.2816 and 0.1276 at MID 32; 007: 0.3767 and 0.138). The balanced E_2 objective is
   dominated by 2^18 (20/21) ||rF||_2^2 (about 95 percent of its F part): new mid-field freedom goes into rF (023: rF 5.88) before G0 or the pairings.
2. The 14 mid-field pairing rows of 021 were inert at weight 1e12 (I about 5e-6 per row); 025 (running; held-out file heldout/HELDOUT_025.md, sha256 6412b262...,
   written before launch) repeats them at 1e16 on the combined basis (2918 generators) with per-step density step norms (R-TANGENT). 024 (MID 32 rule control of 016,
   heldout/HELDOUT_024.md) follows on core 54. Results in numerics_v12.
3. No candidate of this lane is a certification target; the certification requests of this version are nil beyond what the N4 numerical auditor chooses for 022 (structure and point gaps
   would complete its row). The N3 numerics worker's exact legqs norms of 016/017 (target 13:00Z) and the two-scale product keys for 020 to 025 remain the only route to exact norms of
   these candidates.
4. Every FLOAT held-out value above the graded ceiling 4.5717e-4 would, if certified, exclude the candidate from every registered scalar ball and graded box, as for
   016 to 020; the smallest largest-registered-value of the family is 022's 8.30e-4 (1.8 times the graded ceiling; 291 times the unrestricted sharpw ceiling 2.8496e-6)./NOTES through 2026-10-29T10:45:01. (N4-282 019 floor; N4-283; N4-264 backend); the N3 numerics worker through 2026-10-29T10:42 (legqs exact pipeline target 13:00Z).
  Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by ID; the new numbers are the N1/N2 numerics worker's FLOAT values offered for certification.
- theory version followed: theory_v05 (R-HOLDOUT (i)-(iii), R-TANGENT). Candidate IDs new in v11: C1-N1-021-heldin14-legqs25p50 (10:05:34Z), C1-N1-022-legqs25-m16to23 (10:28:22Z), C1-N1-023-legqs25p100-quot013 (10:42:28Z). Chart PRIMARY for all: c_l = 4076476460239181/2^51 and
  Theta_0 of state 131 EXACT, center relation EXACT, a_0 free; coefficient file path: working file candidate_snapshots (not published)/<ID>/<tag>_exact.json (sha256 in SHA256SUMS).
- Every number below is FLOAT (MID 32 rule unless marked MID 16 = optimizer report, or LOSS) unless cited by a working file the N3 numerics worker (not published) ID. Every comparison is a trial
  comparison at the tested probes: no inference about spans, angular-band mass, stationarity or what a basis 'can' reach is drawn (T4-340, T4-356).

## 0. Corrections to numerics_v10 wording (the coordinator 08:51Z item 3, 08:55Z item 3)
(a) 016, 017 and 018 are RULED OUT in every registered scalar ball and original graded box (matrix rows 80 to 85), as 007 to 015 except the FLOAT comparison 011;
    019 is RULED OUT in every specified ball since matrix v85 (N4-282 with T4-357); 020 is OPEN. The dyadic scheme is tested only at 131, d2 and 007 to 010.
(b) v10 section 2 ("the balanced objective does not control angular pairings that are not rows at any radius") and section 3 item 2 ("needs the mid-field pairings
    as rows") were general statements; what was observed is: for 016 to 020 the held-out pairings at the tested probes did not fall under the 67-row objective after
    the first 12 steps, and in 020 the small-r held-out pairings in modes 19 to 31 rose by factors 8 to 38. Whether held-in mid-field rows keep the mid-field values
    is the hypothesis that 021 tests (section 1).
(c) 020 against 016/017 at K >= 1200: 11 to 26 percent above the corresponding 016 or 017 value, and up to 58 percent above 016 at (31,2400) (3.15e-4 against 1.99e-4);
    the small-r increase is 8x at (19,9) and 38x at (27,21).

## 1. C1-N1-021 (020 basis + 14 held-in mid-field rows; GPU, 40 steps)
Run: start 020 (2426 generators, scales 25 and 50); balanced E_2 objective + 1e12 I^2 over 81 rows = 67 rows of 016..020 + 14 HELD-IN mid-field rows (N4-160 probes n = 19..31 at K0 = 128 and 512); HELD-OUT: the 25 registered probes and the N4-160 probes n >= 19 at K0 in {0, 8, 32}; 40 GN steps, MID 16, GPU 7 (33 s per step with three jobs on the GPU).
Exact JSON sha256 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8; 2426 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  39 obj 1.313090e+07 -> 1.312554e+07 ACC pred 1.004e+04 lam 3.5e-03 parts F 1.128e+07 G 1.985e+05 P 4.151e+04 K 1.605e+06 PAIR 4.310e+02 .
Optimizer report (MID 16): 37316e+02 G1 3.480555e+00 G0 2.991634e-01 rF 6.624130e+00 supF 1.3868e-01
FLOAT (diag2, MID 32): G0 0.2996 (016 0.3089, 017 0.3209, 020 0.3201), G1 3.489, P2 203.5, rF 6.680, H 0.6096, sup|F| 0.1398, theta_inner 0.0114, kappa_inner 0.7313 ((B-L2) margin +0.0676).
First-mode weak probe (weak_tests2, 27 sampled k <= 4096): largest sampled value 1.77e-04 at k = 2048.
| probe (n, K) | r_peak | 013 | 016 | 017 | 020 | 021 |
|---|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | - | 8.18e-06 | 3.04e-05 | 7.74e-05 | 2.16e-05 |
| (19, 900) [registered, HELD OUT] | 25 | - | 5.31e-04 | 6.02e-04 | 6.99e-04 | 6.61e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | - | 8.16e-04 | 9.18e-04 | 1.03e-03 | 1.01e-03 |
| (19, 1800) [registered, HELD OUT] | 35 | - | 9.02e-04 | 1.03e-03 | 1.14e-03 | 1.14e-03 |
| (19, 2400) [registered, HELD OUT] | 40 | - | 7.44e-04 | 8.67e-04 | 9.73e-04 | 9.93e-04 |
| (23, 600) [registered, HELD OUT] | 20 | - | 2.17e-04 | 3.01e-04 | 2.67e-04 | 3.09e-04 |
| (23, 900) [registered, HELD OUT] | 25 | - | 2.80e-05 | 1.70e-05 | 3.41e-05 | 6.59e-06 |
| (23, 1200) [registered, HELD OUT] | 28 | - | 2.97e-04 | 2.72e-04 | 3.43e-04 | 3.11e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | - | 5.94e-04 | 5.76e-04 | 6.83e-04 | 6.70e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | - | 6.50e-04 | 6.35e-04 | 7.59e-04 | 7.60e-04 |
| (25, 600) [registered, HELD OUT] | 20 | - | 1.94e-04 | 2.63e-04 | 2.49e-04 | 2.85e-04 |
| (25, 900) [registered, HELD OUT] | 25 | - | 8.93e-05 | 1.32e-04 | 9.99e-05 | 1.40e-04 |
| (25, 1200) [registered, HELD OUT] | 28 | - | 1.16e-04 | 8.77e-05 | 1.41e-04 | 1.04e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | - | 4.19e-04 | 4.04e-04 | 4.90e-04 | 4.66e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | - | 5.37e-04 | 5.30e-04 | 6.34e-04 | 6.20e-04 |
| (29, 600) [registered, HELD OUT] | 20 | - | 8.70e-05 | 1.36e-04 | 1.47e-04 | 1.61e-04 |
| (29, 900) [registered, HELD OUT] | 25 | - | 1.62e-04 | 1.92e-04 | 1.88e-04 | 2.14e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | - | 9.65e-05 | 1.10e-04 | 8.97e-05 | 1.18e-04 |
| (29, 1800) [registered, HELD OUT] | 35 | - | 1.19e-04 | 1.32e-04 | 1.78e-04 | 1.53e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | - | 2.72e-04 | 3.05e-04 | 3.68e-04 | 3.49e-04 |
| (31, 600) [registered, HELD OUT] | 20 | - | 7.85e-05 | 9.68e-05 | 9.34e-05 | 1.12e-04 |
| (31, 900) [registered, HELD OUT] | 25 | - | 1.66e-04 | 1.62e-04 | 1.36e-04 | 1.72e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | - | 1.27e-04 | 1.09e-04 | 6.83e-05 | 1.09e-04 |
| (31, 1800) [registered, HELD OUT] | 35 | - | 5.42e-05 | 9.24e-05 | 1.48e-04 | 1.11e-04 |
| (31, 2400) [registered, HELD OUT] | 40 | - | 1.99e-04 | 2.53e-04 | 3.15e-04 | 2.84e-04 |
| (19, 521) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.90e-04 | 1.69e-04 | 1.31e-04 | 1.16e-04 | 1.74e-04 |
| (21, 522) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.12e-03 | 2.33e-04 | 3.36e-04 | 2.94e-04 | 3.51e-04 |
| (23, 523) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 7.58e-04 | 2.32e-04 | 3.22e-04 | 2.99e-04 | 3.38e-04 |
| (25, 524) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 5.28e-04 | 1.70e-04 | 2.43e-04 | 2.36e-04 | 2.68e-04 |
| (27, 525) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 3.10e-04 | 1.04e-04 | 1.60e-04 | 1.66e-04 | 1.83e-04 |
| (29, 526) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 2.00e-04 | 3.77e-05 | 8.95e-05 | 1.03e-04 | 1.13e-04 |
| (31, 527) [N4-160 K0 = 512, HELD IN (objective row)] | 19 | 1.19e-04 | 3.26e-05 | 5.82e-05 | 6.17e-05 | 7.27e-05 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.00e-05 | 2.06e-05 | 6.27e-05 | 1.68e-04 | 1.79e-05 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 7.31e-06 | 4.61e-05 | 9.89e-05 | 1.36e-05 | 3.20e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.17e-05 | 1.36e-05 | 1.83e-05 | 1.03e-04 | 4.35e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 1.91e-05 | 5.36e-05 | 1.07e-05 | 2.24e-05 | 3.94e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 7.76e-06 | 1.83e-06 | 2.53e-05 | 9.09e-05 | 1.42e-05 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 3.28e-06 | 1.25e-05 | 9.00e-06 | 4.91e-05 | 2.29e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 6.54e-06 | 1.01e-05 | 1.89e-05 | 6.39e-05 | 1.57e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 2.24e-05 | 6.21e-06 | 2.78e-05 | 1.67e-04 | 3.34e-05 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 1.93e-05 | 2.04e-05 | 2.70e-05 | 1.39e-04 | 3.69e-05 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.22e-06 | 3.84e-06 | 2.91e-05 | 1.45e-04 | 2.21e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 5.86e-07 | 3.15e-05 | 1.34e-05 | 8.52e-05 | 3.00e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 1.14e-03 (016: (19, 1800) 9.02e-4; 017: 1.03e-3; 020: 1.14e-3).
Best m by mode over the N4-160 family (FLOAT; rows and held-out mixed, see the tags above): n = 1: 2.0e-04; n = 3: 5.4e-05; n = 5: 7.2e-05; n = 7: 3.2e-05; n = 9: 5.3e-05; n = 11: 7.6e-05; n = 13: 3.1e-05; n = 15: 1.4e-04; n = 17: 1.1e-04; n = 19: 1.1e-03; n = 21: 3.5e-04; n = 23: 7.6e-04; n = 25: 6.2e-04; n = 27: 1.8e-04; n = 29: 3.5e-04; n = 31: 2.8e-04.

## 2. C1-N1-022 (016 + 240 legqs R0 = 25 in the higher blocks m = 16..23; GPU; 12 steps controlled, then 40)
Phase 1 (controlled comparison with 016 at equal step count and rule): start 016 + 240 legqs R0 = 25 functions in the existing higher blocks j = 1 (m = 16..19), j = 2, 3 (m = 16..23) (2414 generators; density modes 31 to 47); same 67 rows and HELD-OUT set as 016; 12 GN steps, MID 16, GPU.
Exact JSON sha256 2a13c07969eb37af27c68a0336fa7f28a9f1747119e1f7ad4623302f58d5fd4f; 2414 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  12 obj 1.426396e+07 -> 1.411254e+07 ACC pred 4.854e+05 lam 1.4e-03 parts F 1.221e+07 G 2.349e+05 P 4.785e+04 K 1.621e+06 PAIR 5.780e+02 .
Optimizer report (MID 16): 87482e+02 G1 3.786156e+00 G0 3.015824e-01 rF 6.882194e+00 supF 1.2840e-01
diag2 (MID 32 norms, (B-L2) screening): PENDING.
| probe (n, K) | r_peak | 013 | 016 | 017 | 020 | 022 (12 steps) |
|---|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | - | 8.18e-06 | 3.04e-05 | 7.74e-05 | 1.01e-04 |
| (19, 900) [registered, HELD OUT] | 25 | - | 5.31e-04 | 6.02e-04 | 6.99e-04 | 5.53e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | - | 8.16e-04 | 9.18e-04 | 1.03e-03 | 7.83e-04 |
| (19, 1800) [registered, HELD OUT] | 35 | - | 9.02e-04 | 1.03e-03 | 1.14e-03 | 8.40e-04 |
| (19, 2400) [registered, HELD OUT] | 40 | - | 7.44e-04 | 8.67e-04 | 9.73e-04 | 6.91e-04 |
| (23, 600) [registered, HELD OUT] | 20 | - | 2.17e-04 | 3.01e-04 | 2.67e-04 | 1.28e-04 |
| (23, 900) [registered, HELD OUT] | 25 | - | 2.80e-05 | 1.70e-05 | 3.41e-05 | 1.15e-04 |
| (23, 1200) [registered, HELD OUT] | 28 | - | 2.97e-04 | 2.72e-04 | 3.43e-04 | 3.56e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | - | 5.94e-04 | 5.76e-04 | 6.83e-04 | 6.22e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | - | 6.50e-04 | 6.35e-04 | 7.59e-04 | 6.83e-04 |
| (25, 600) [registered, HELD OUT] | 20 | - | 1.94e-04 | 2.63e-04 | 2.49e-04 | 1.42e-04 |
| (25, 900) [registered, HELD OUT] | 25 | - | 8.93e-05 | 1.32e-04 | 9.99e-05 | 2.06e-05 |
| (25, 1200) [registered, HELD OUT] | 28 | - | 1.16e-04 | 8.77e-05 | 1.41e-04 | 1.64e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | - | 4.19e-04 | 4.04e-04 | 4.90e-04 | 4.28e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | - | 5.37e-04 | 5.30e-04 | 6.34e-04 | 5.32e-04 |
| (29, 600) [registered, HELD OUT] | 20 | - | 8.70e-05 | 1.36e-04 | 1.47e-04 | 9.19e-05 |
| (29, 900) [registered, HELD OUT] | 25 | - | 1.62e-04 | 1.92e-04 | 1.88e-04 | 1.23e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | - | 9.65e-05 | 1.10e-04 | 8.97e-05 | 5.24e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | - | 1.19e-04 | 1.32e-04 | 1.78e-04 | 1.33e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | - | 2.72e-04 | 3.05e-04 | 3.68e-04 | 2.57e-04 |
| (31, 600) [registered, HELD OUT] | 20 | - | 7.85e-05 | 9.68e-05 | 9.34e-05 | 5.96e-05 |
| (31, 900) [registered, HELD OUT] | 25 | - | 1.66e-04 | 1.62e-04 | 1.36e-04 | 1.20e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | - | 1.27e-04 | 1.09e-04 | 6.83e-05 | 9.08e-05 |
| (31, 1800) [registered, HELD OUT] | 35 | - | 5.42e-05 | 9.24e-05 | 1.48e-04 | 5.39e-05 |
| (31, 2400) [registered, HELD OUT] | 40 | - | 1.99e-04 | 2.53e-04 | 3.15e-04 | 1.79e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.90e-04 | 1.69e-04 | 1.31e-04 | 1.16e-04 | 4.12e-05 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 1.12e-03 | 2.33e-04 | 3.36e-04 | 2.94e-04 | 1.31e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 7.58e-04 | 2.32e-04 | 3.22e-04 | 2.99e-04 | 1.58e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 5.28e-04 | 1.70e-04 | 2.43e-04 | 2.36e-04 | 1.36e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 3.10e-04 | 1.04e-04 | 1.60e-04 | 1.66e-04 | 1.08e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 2.00e-04 | 3.77e-05 | 8.95e-05 | 1.03e-04 | 5.99e-05 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 1.19e-04 | 3.26e-05 | 5.82e-05 | 6.17e-05 | 2.92e-05 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.00e-05 | 2.06e-05 | 6.27e-05 | 1.68e-04 | 8.74e-06 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 7.31e-06 | 4.61e-05 | 9.89e-05 | 1.36e-05 | 3.56e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.17e-05 | 1.36e-05 | 1.83e-05 | 1.03e-04 | 5.97e-06 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 1.91e-05 | 5.36e-05 | 1.07e-05 | 2.24e-05 | 3.33e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 7.76e-06 | 1.83e-06 | 2.53e-05 | 9.09e-05 | 1.63e-06 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 3.28e-06 | 1.25e-05 | 9.00e-06 | 4.91e-05 | 5.41e-06 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 6.54e-06 | 1.01e-05 | 1.89e-05 | 6.39e-05 | 1.54e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 2.24e-05 | 6.21e-06 | 2.78e-05 | 1.67e-04 | 1.00e-05 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 1.93e-05 | 2.04e-05 | 2.70e-05 | 1.39e-04 | 1.38e-06 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.22e-06 | 3.84e-06 | 2.91e-05 | 1.45e-04 | 1.93e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 5.86e-07 | 3.15e-05 | 1.34e-05 | 8.52e-05 | 2.11e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 8.40e-04 (016: (19, 1800) 9.02e-4; 017: 1.03e-3; 020: 1.14e-3).
Best m by mode over the N4-160 family (FLOAT; rows and held-out mixed, see the tags above): n = 1: 1.9e-04; n = 3: 5.7e-05; n = 5: 1.3e-04; n = 7: 1.2e-04; n = 9: 1.9e-05; n = 11: 5.7e-05; n = 13: 4.0e-05; n = 15: 3.1e-05; n = 17: 1.8e-04; n = 19: 8.4e-04; n = 21: 1.3e-04; n = 23: 6.8e-04; n = 25: 5.3e-04; n = 27: 1.1e-04; n = 29: 2.6e-04; n = 31: 1.8e-04.

Phase 2: 28 more steps from the phase 1 state (same rows, same held-out set).
Exact JSON sha256 85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f; 2414 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  28 obj 1.389607e+07 -> 1.388999e+07 ACC pred 2.897e+05 lam 7.7e-04 parts F 1.203e+07 G 2.060e+05 P 4.293e+04 K 1.606e+06 PAIR 2.808e+02 .
Optimizer report (MID 16): 72000e+02 G1 3.546226e+00 G0 2.811492e-01 rF 6.845559e+00 supF 1.2618e-01
FLOAT (diag2, MID 32): G0 0.2816 (016 0.3089, 017 0.3209, 020 0.3201), G1 3.554, P2 206.9, rF 6.900, H 0.6119, sup|F| 0.1276, theta_inner 0.0114, kappa_inner 0.7315 ((B-L2) margin +0.0674).
First-mode weak probe (weak_tests2, 27 sampled k <= 4096): largest sampled value 1.65e-04 at k = 2048.
| probe (n, K) | r_peak | 013 | 016 | 017 | 020 | 022 (40 steps) |
|---|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | - | 8.18e-06 | 3.04e-05 | 7.74e-05 | 5.91e-05 |
| (19, 900) [registered, HELD OUT] | 25 | - | 5.31e-04 | 6.02e-04 | 6.99e-04 | 5.23e-04 |
| (19, 1200) [registered, HELD OUT] | 28 | - | 8.16e-04 | 9.18e-04 | 1.03e-03 | 7.61e-04 |
| (19, 1800) [registered, HELD OUT] | 35 | - | 9.02e-04 | 1.03e-03 | 1.14e-03 | 8.30e-04 |
| (19, 2400) [registered, HELD OUT] | 40 | - | 7.44e-04 | 8.67e-04 | 9.73e-04 | 6.90e-04 |
| (23, 600) [registered, HELD OUT] | 20 | - | 2.17e-04 | 3.01e-04 | 2.67e-04 | 1.65e-04 |
| (23, 900) [registered, HELD OUT] | 25 | - | 2.80e-05 | 1.70e-05 | 3.41e-05 | 7.74e-05 |
| (23, 1200) [registered, HELD OUT] | 28 | - | 2.97e-04 | 2.72e-04 | 3.43e-04 | 3.19e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | - | 5.94e-04 | 5.76e-04 | 6.83e-04 | 5.85e-04 |
| (23, 2400) [registered, HELD OUT] | 40 | - | 6.50e-04 | 6.35e-04 | 7.59e-04 | 6.44e-04 |
| (25, 600) [registered, HELD OUT] | 20 | - | 1.94e-04 | 2.63e-04 | 2.49e-04 | 1.64e-04 |
| (25, 900) [registered, HELD OUT] | 25 | - | 8.93e-05 | 1.32e-04 | 9.99e-05 | 4.02e-05 |
| (25, 1200) [registered, HELD OUT] | 28 | - | 1.16e-04 | 8.77e-05 | 1.41e-04 | 1.49e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | - | 4.19e-04 | 4.04e-04 | 4.90e-04 | 4.18e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | - | 5.37e-04 | 5.30e-04 | 6.34e-04 | 5.27e-04 |
| (29, 600) [registered, HELD OUT] | 20 | - | 8.70e-05 | 1.36e-04 | 1.47e-04 | 9.78e-05 |
| (29, 900) [registered, HELD OUT] | 25 | - | 1.62e-04 | 1.92e-04 | 1.88e-04 | 1.24e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | - | 9.65e-05 | 1.10e-04 | 8.97e-05 | 4.64e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | - | 1.19e-04 | 1.32e-04 | 1.78e-04 | 1.52e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | - | 2.72e-04 | 3.05e-04 | 3.68e-04 | 2.85e-04 |
| (31, 600) [registered, HELD OUT] | 20 | - | 7.85e-05 | 9.68e-05 | 9.34e-05 | 6.17e-05 |
| (31, 900) [registered, HELD OUT] | 25 | - | 1.66e-04 | 1.62e-04 | 1.36e-04 | 1.22e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | - | 1.27e-04 | 1.09e-04 | 6.83e-05 | 8.98e-05 |
| (31, 1800) [registered, HELD OUT] | 35 | - | 5.42e-05 | 9.24e-05 | 1.48e-04 | 6.01e-05 |
| (31, 2400) [registered, HELD OUT] | 40 | - | 1.99e-04 | 2.53e-04 | 3.15e-04 | 1.88e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.90e-04 | 1.69e-04 | 1.31e-04 | 1.16e-04 | 8.72e-05 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 1.12e-03 | 2.33e-04 | 3.36e-04 | 2.94e-04 | 1.66e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 7.58e-04 | 2.32e-04 | 3.22e-04 | 2.99e-04 | 1.94e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 5.28e-04 | 1.70e-04 | 2.43e-04 | 2.36e-04 | 1.58e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 3.10e-04 | 1.04e-04 | 1.60e-04 | 1.66e-04 | 1.15e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 2.00e-04 | 3.77e-05 | 8.95e-05 | 1.03e-04 | 6.60e-05 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 1.19e-04 | 3.26e-05 | 5.82e-05 | 6.17e-05 | 3.06e-05 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.00e-05 | 2.06e-05 | 6.27e-05 | 1.68e-04 | 2.48e-05 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 7.31e-06 | 4.61e-05 | 9.89e-05 | 1.36e-05 | 4.54e-06 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.17e-05 | 1.36e-05 | 1.83e-05 | 1.03e-04 | 2.38e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 1.91e-05 | 5.36e-05 | 1.07e-05 | 2.24e-05 | 9.22e-06 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 7.76e-06 | 1.83e-06 | 2.53e-05 | 9.09e-05 | 3.96e-06 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 3.28e-06 | 1.25e-05 | 9.00e-06 | 4.91e-05 | 2.10e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 6.54e-06 | 1.01e-05 | 1.89e-05 | 6.39e-05 | 6.28e-06 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 2.24e-05 | 6.21e-06 | 2.78e-05 | 1.67e-04 | 1.12e-04 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 1.93e-05 | 2.04e-05 | 2.70e-05 | 1.39e-04 | 4.39e-05 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.22e-06 | 3.84e-06 | 2.91e-05 | 1.45e-04 | 8.89e-06 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 5.86e-07 | 3.15e-05 | 1.34e-05 | 8.52e-05 | 2.21e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 8.30e-04 (016: (19, 1800) 9.02e-4; 017: 1.03e-3; 020: 1.14e-3).
Best m by mode over the N4-160 family (FLOAT; rows and held-out mixed, see the tags above): n = 1: 1.9e-04; n = 3: 4.0e-05; n = 5: 7.9e-05; n = 7: 6.6e-05; n = 9: 3.1e-05; n = 11: 1.1e-05; n = 13: 3.8e-05; n = 15: 1.6e-04; n = 17: 8.2e-05; n = 19: 8.3e-04; n = 21: 1.7e-04; n = 23: 6.4e-04; n = 25: 5.3e-04; n = 27: 1.1e-04; n = 29: 2.9e-04; n = 31: 1.9e-04.

## 3. C1-N1-023 (016 + 252 legqs R0 = 100: scales 25 and 100; GPU; 12 steps controlled, then 40)
Phase 1 (controlled comparison with 016 and 020 at equal step count and rule): start 016 + 252 legqs R0 = 100 functions in j = 1..3, m = 9..15 (scales 25 and 100; 2426 generators); same 67 rows and HELD-OUT set as 016; 12 GN steps, MID 16, GPU.
Exact JSON sha256 637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb; 2426 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  11 obj 1.136541e+07 -> 1.132924e+07 ACC pred 5.647e+04 lam 4.1e-03 parts F 9.338e+06 G 2.805e+05 P 6.666e+04 K 1.641e+06 PAIR 3.715e+03 .
Optimizer report (MID 16): 81840e+02 G1 4.137478e+00 G0 3.347999e-01 rF 5.951065e+00 supF 1.5888e-01
diag2 (MID 32 norms, (B-L2) screening): PENDING.
| probe (n, K) | r_peak | 013 | 016 | 017 | 020 | 023 (12 steps) |
|---|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | - | 8.18e-06 | 3.04e-05 | 7.74e-05 | 3.63e-04 |
| (19, 900) [registered, HELD OUT] | 25 | - | 5.31e-04 | 6.02e-04 | 6.99e-04 | 1.13e-03 |
| (19, 1200) [registered, HELD OUT] | 28 | - | 8.16e-04 | 9.18e-04 | 1.03e-03 | 1.50e-03 |
| (19, 1800) [registered, HELD OUT] | 35 | - | 9.02e-04 | 1.03e-03 | 1.14e-03 | 1.60e-03 |
| (19, 2400) [registered, HELD OUT] | 40 | - | 7.44e-04 | 8.67e-04 | 9.73e-04 | 1.39e-03 |
| (23, 600) [registered, HELD OUT] | 20 | - | 2.17e-04 | 3.01e-04 | 2.67e-04 | 2.36e-04 |
| (23, 900) [registered, HELD OUT] | 25 | - | 2.80e-05 | 1.70e-05 | 3.41e-05 | 2.42e-04 |
| (23, 1200) [registered, HELD OUT] | 28 | - | 2.97e-04 | 2.72e-04 | 3.43e-04 | 6.40e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | - | 5.94e-04 | 5.76e-04 | 6.83e-04 | 1.05e-03 |
| (23, 2400) [registered, HELD OUT] | 40 | - | 6.50e-04 | 6.35e-04 | 7.59e-04 | 1.14e-03 |
| (25, 600) [registered, HELD OUT] | 20 | - | 1.94e-04 | 2.63e-04 | 2.49e-04 | 2.99e-04 |
| (25, 900) [registered, HELD OUT] | 25 | - | 8.93e-05 | 1.32e-04 | 9.99e-05 | 9.63e-06 |
| (25, 1200) [registered, HELD OUT] | 28 | - | 1.16e-04 | 8.77e-05 | 1.41e-04 | 3.43e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | - | 4.19e-04 | 4.04e-04 | 4.90e-04 | 7.75e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | - | 5.37e-04 | 5.30e-04 | 6.34e-04 | 9.44e-04 |
| (29, 600) [registered, HELD OUT] | 20 | - | 8.70e-05 | 1.36e-04 | 1.47e-04 | 2.62e-04 |
| (29, 900) [registered, HELD OUT] | 25 | - | 1.62e-04 | 1.92e-04 | 1.88e-04 | 1.89e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | - | 9.65e-05 | 1.10e-04 | 8.97e-05 | 7.78e-06 |
| (29, 1800) [registered, HELD OUT] | 35 | - | 1.19e-04 | 1.32e-04 | 1.78e-04 | 3.49e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | - | 2.72e-04 | 3.05e-04 | 3.68e-04 | 5.75e-04 |
| (31, 600) [registered, HELD OUT] | 20 | - | 7.85e-05 | 9.68e-05 | 9.34e-05 | 2.28e-04 |
| (31, 900) [registered, HELD OUT] | 25 | - | 1.66e-04 | 1.62e-04 | 1.36e-04 | 2.04e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | - | 1.27e-04 | 1.09e-04 | 6.83e-05 | 7.30e-05 |
| (31, 1800) [registered, HELD OUT] | 35 | - | 5.42e-05 | 9.24e-05 | 1.48e-04 | 2.24e-04 |
| (31, 2400) [registered, HELD OUT] | 40 | - | 1.99e-04 | 2.53e-04 | 3.15e-04 | 4.30e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.90e-04 | 1.69e-04 | 1.31e-04 | 1.16e-04 | 9.63e-05 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 1.12e-03 | 2.33e-04 | 3.36e-04 | 2.94e-04 | 2.48e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 7.58e-04 | 2.32e-04 | 3.22e-04 | 2.99e-04 | 3.34e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 5.28e-04 | 1.70e-04 | 2.43e-04 | 2.36e-04 | 3.39e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 3.10e-04 | 1.04e-04 | 1.60e-04 | 1.66e-04 | 3.04e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 2.00e-04 | 3.77e-05 | 8.95e-05 | 1.03e-04 | 2.48e-04 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 1.19e-04 | 3.26e-05 | 5.82e-05 | 6.17e-05 | 2.08e-04 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.00e-05 | 2.06e-05 | 6.27e-05 | 1.68e-04 | 3.64e-05 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 7.31e-06 | 4.61e-05 | 9.89e-05 | 1.36e-05 | 4.45e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.17e-05 | 1.36e-05 | 1.83e-05 | 1.03e-04 | 3.10e-05 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 1.91e-05 | 5.36e-05 | 1.07e-05 | 2.24e-05 | 7.22e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 7.76e-06 | 1.83e-06 | 2.53e-05 | 9.09e-05 | 1.58e-05 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 3.28e-06 | 1.25e-05 | 9.00e-06 | 4.91e-05 | 2.18e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 6.54e-06 | 1.01e-05 | 1.89e-05 | 6.39e-05 | 3.82e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 2.24e-05 | 6.21e-06 | 2.78e-05 | 1.67e-04 | 2.45e-05 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 1.93e-05 | 2.04e-05 | 2.70e-05 | 1.39e-04 | 5.03e-05 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.22e-06 | 3.84e-06 | 2.91e-05 | 1.45e-04 | 4.34e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 5.86e-07 | 3.15e-05 | 1.34e-05 | 8.52e-05 | 1.22e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 1.60e-03 (016: (19, 1800) 9.02e-4; 017: 1.03e-3; 020: 1.14e-3).
Best m by mode over the N4-160 family (FLOAT; rows and held-out mixed, see the tags above): n = 1: 4.1e-04; n = 3: 4.1e-04; n = 5: 2.1e-04; n = 7: 1.4e-04; n = 9: 3.7e-04; n = 11: 1.1e-04; n = 13: 1.8e-04; n = 15: 6.2e-05; n = 17: 5.8e-04; n = 19: 1.6e-03; n = 21: 3.0e-04; n = 23: 1.1e-03; n = 25: 9.4e-04; n = 27: 3.0e-04; n = 29: 5.8e-04; n = 31: 4.3e-04.

Phase 2: 28 more steps from the phase 1 state (same rows, same held-out set).
Exact JSON sha256 d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df; 2426 generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: it  27 obj 1.103448e+07 -> 1.102322e+07 ACC pred 2.600e+04 lam 2.3e-03 parts F 9.074e+06 G 2.531e+05 P 6.158e+04 K 1.631e+06 PAIR 3.360e+03 .
Optimizer report (MID 16): 81544e+02 G1 3.930275e+00 G0 3.225189e-01 rF 5.877753e+00 supF 1.4591e-01
FLOAT (diag2, MID 32): G0 0.3228 (016 0.3089, 017 0.3209, 020 0.3201), G1 3.939, P2 247.9, rF 5.942, H 0.6121, sup|F| 0.1786, theta_inner 0.0114, kappa_inner 0.7373 ((B-L2) margin +0.0616).
First-mode weak probe (weak_tests2, 27 sampled k <= 4096): largest sampled value 3.67e-04 at k = 1536.
| probe (n, K) | r_peak | 013 | 016 | 017 | 020 | 023 (40 steps) |
|---|---|---|---|---|---|---|
| (19, 600) [registered, HELD OUT] | 20 | - | 8.18e-06 | 3.04e-05 | 7.74e-05 | 2.14e-04 |
| (19, 900) [registered, HELD OUT] | 25 | - | 5.31e-04 | 6.02e-04 | 6.99e-04 | 1.04e-03 |
| (19, 1200) [registered, HELD OUT] | 28 | - | 8.16e-04 | 9.18e-04 | 1.03e-03 | 1.46e-03 |
| (19, 1800) [registered, HELD OUT] | 35 | - | 9.02e-04 | 1.03e-03 | 1.14e-03 | 1.62e-03 |
| (19, 2400) [registered, HELD OUT] | 40 | - | 7.44e-04 | 8.67e-04 | 9.73e-04 | 1.44e-03 |
| (23, 600) [registered, HELD OUT] | 20 | - | 2.17e-04 | 3.01e-04 | 2.67e-04 | 3.48e-04 |
| (23, 900) [registered, HELD OUT] | 25 | - | 2.80e-05 | 1.70e-05 | 3.41e-05 | 1.41e-04 |
| (23, 1200) [registered, HELD OUT] | 28 | - | 2.97e-04 | 2.72e-04 | 3.43e-04 | 5.64e-04 |
| (23, 1800) [registered, HELD OUT] | 35 | - | 5.94e-04 | 5.76e-04 | 6.83e-04 | 1.02e-03 |
| (23, 2400) [registered, HELD OUT] | 40 | - | 6.50e-04 | 6.35e-04 | 7.59e-04 | 1.14e-03 |
| (25, 600) [registered, HELD OUT] | 20 | - | 1.94e-04 | 2.63e-04 | 2.49e-04 | 3.88e-04 |
| (25, 900) [registered, HELD OUT] | 25 | - | 8.93e-05 | 1.32e-04 | 9.99e-05 | 8.13e-05 |
| (25, 1200) [registered, HELD OUT] | 28 | - | 1.16e-04 | 8.77e-05 | 1.41e-04 | 2.66e-04 |
| (25, 1800) [registered, HELD OUT] | 35 | - | 4.19e-04 | 4.04e-04 | 4.90e-04 | 7.32e-04 |
| (25, 2400) [registered, HELD OUT] | 40 | - | 5.37e-04 | 5.30e-04 | 6.34e-04 | 9.27e-04 |
| (29, 600) [registered, HELD OUT] | 20 | - | 8.70e-05 | 1.36e-04 | 1.47e-04 | 3.16e-04 |
| (29, 900) [registered, HELD OUT] | 25 | - | 1.62e-04 | 1.92e-04 | 1.88e-04 | 2.62e-04 |
| (29, 1200) [registered, HELD OUT] | 28 | - | 9.65e-05 | 1.10e-04 | 8.97e-05 | 7.98e-05 |
| (29, 1800) [registered, HELD OUT] | 35 | - | 1.19e-04 | 1.32e-04 | 1.78e-04 | 2.95e-04 |
| (29, 2400) [registered, HELD OUT] | 40 | - | 2.72e-04 | 3.05e-04 | 3.68e-04 | 5.40e-04 |
| (31, 600) [registered, HELD OUT] | 20 | - | 7.85e-05 | 9.68e-05 | 9.34e-05 | 2.67e-04 |
| (31, 900) [registered, HELD OUT] | 25 | - | 1.66e-04 | 1.62e-04 | 1.36e-04 | 2.57e-04 |
| (31, 1200) [registered, HELD OUT] | 28 | - | 1.27e-04 | 1.09e-04 | 6.83e-05 | 1.26e-04 |
| (31, 1800) [registered, HELD OUT] | 35 | - | 5.42e-05 | 9.24e-05 | 1.48e-04 | 1.83e-04 |
| (31, 2400) [registered, HELD OUT] | 40 | - | 1.99e-04 | 2.53e-04 | 3.15e-04 | 4.04e-04 |
| (19, 521) [N4-160 K0 = 512, HELD OUT] | 19 | 1.90e-04 | 1.69e-04 | 1.31e-04 | 1.16e-04 | 6.66e-05 |
| (21, 522) [N4-160 K0 = 512, HELD OUT] | 19 | 1.12e-03 | 2.33e-04 | 3.36e-04 | 2.94e-04 | 3.72e-04 |
| (23, 523) [N4-160 K0 = 512, HELD OUT] | 19 | 7.58e-04 | 2.32e-04 | 3.22e-04 | 2.99e-04 | 4.42e-04 |
| (25, 524) [N4-160 K0 = 512, HELD OUT] | 19 | 5.28e-04 | 1.70e-04 | 2.43e-04 | 2.36e-04 | 4.20e-04 |
| (27, 525) [N4-160 K0 = 512, HELD OUT] | 19 | 3.10e-04 | 1.04e-04 | 1.60e-04 | 1.66e-04 | 3.64e-04 |
| (29, 526) [N4-160 K0 = 512, HELD OUT] | 19 | 2.00e-04 | 3.77e-05 | 8.95e-05 | 1.03e-04 | 2.92e-04 |
| (31, 527) [N4-160 K0 = 512, HELD OUT] | 19 | 1.19e-04 | 3.26e-05 | 5.82e-05 | 6.17e-05 | 2.40e-04 |
| (19, 9) [N4-160 small K0, HELD OUT] | 3 | 2.00e-05 | 2.06e-05 | 6.27e-05 | 1.68e-04 | 2.27e-06 |
| (21, 10) [N4-160 small K0, HELD OUT] | 3 | 7.31e-06 | 4.61e-05 | 9.89e-05 | 1.36e-05 | 5.03e-05 |
| (23, 11) [N4-160 small K0, HELD OUT] | 3 | 1.17e-05 | 1.36e-05 | 1.83e-05 | 1.03e-04 | 9.41e-06 |
| (25, 12) [N4-160 small K0, HELD OUT] | 3 | 1.91e-05 | 5.36e-05 | 1.07e-05 | 2.24e-05 | 6.99e-05 |
| (27, 13) [N4-160 small K0, HELD OUT] | 3 | 7.76e-06 | 1.83e-06 | 2.53e-05 | 9.09e-05 | 3.95e-05 |
| (29, 14) [N4-160 small K0, HELD OUT] | 3 | 3.28e-06 | 1.25e-05 | 9.00e-06 | 4.91e-05 | 6.51e-05 |
| (31, 15) [N4-160 small K0, HELD OUT] | 3 | 6.54e-06 | 1.01e-05 | 1.89e-05 | 6.39e-05 | 5.16e-05 |
| (19, 17) [N4-160 small K0, HELD OUT] | 3 | 2.24e-05 | 6.21e-06 | 2.78e-05 | 1.67e-04 | 1.11e-05 |
| (23, 19) [N4-160 small K0, HELD OUT] | 4 | 1.93e-05 | 2.04e-05 | 2.70e-05 | 1.39e-04 | 8.54e-06 |
| (27, 21) [N4-160 small K0, HELD OUT] | 4 | 3.22e-06 | 3.84e-06 | 2.91e-05 | 1.45e-04 | 1.22e-05 |
| (29, 22) [N4-160 small K0, HELD OUT] | 4 | 5.86e-07 | 3.15e-05 | 1.34e-05 | 8.52e-05 | 3.97e-05 |
Largest held-out value over the 25 registered probes: (19, 1800) 1.62e-03 (016: (19, 1800) 9.02e-4; 017: 1.03e-3; 020: 1.14e-3).
Best m by mode over the N4-160 family (FLOAT; rows and held-out mixed, see the tags above): n = 1: 4.1e-04; n = 3: 5.2e-04; n = 5: 1.9e-04; n = 7: 5.9e-05; n = 9: 3.5e-04; n = 11: 1.0e-04; n = 13: 1.4e-04; n = 15: 2.1e-04; n = 17: 3.9e-04; n = 19: 1.6e-03; n = 21: 3.7e-04; n = 23: 1.1e-03; n = 25: 9.3e-04; n = 27: 3.6e-04; n = 29: 5.4e-04; n = 31: 4.0e-04.

## 4. Summary table (FLOAT, MID 32; held-out values at the registered probes)
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
All FLOAT (diag2 MID 32; weak_tests3 MID 32; LOSS = last accepted objective on the MID 16 rule, comparable only within the same row set: 016 to 020, 022, 023 use 67 rows; 021 and 025 use 81 rows, so their LOSS includes 14 more penalty rows). Certified floors (CONFIRMED): 016 > 1.4704e-3, 017 > 1.6718e-3, 018 > 1.6558e-3, 019 > 1.6618e-3 at (19,1800).
Modes 33 to 47 (weak_tests3, IPM_NMAX=47; held out; FLOAT best value per mode): 022 1.4e-5 to 3.2e-5, 016 2.1e-5 to 1.6e-4, 013 7.6e-6 to 7.4e-5 (smaller values at the tested probes; no band-mass bound follows).

## 5. Status and next runs
1. Reading of the 016 family after 021 to 023 (FLOAT, trial comparisons at the tested probes; no span, mass or stationarity inference): the registered mid-field
   held-out values (modes 19 to 31, r 35 to 50) responded to the scale-25 functions in the blocks m = 9..15 (016: factors 2.5 to 5 against 013 at K about 520, 1.2 to 1.5
   at K >= 1200) and to nothing tried since: scale 50 (017, 020), the higher blocks (022, within 10 percent), scale 100 (023: 1.5x to 2x worse), more steps (018, 019,
   021). G0 and sup|F| responded to the higher blocks and to more steps (022: 0.2816 and 0.1276 at MID 32; 007: 0.3767 and 0.138). The balanced E_2 objective is
   dominated by 2^18 (20/21) ||rF||_2^2 (about 95 percent of its F part): new mid-field freedom goes into rF (023: rF 5.88) before G0 or the pairings.
2. The 14 mid-field pairing rows of 021 were inert at weight 1e12 (I about 5e-6 per row); 025 (running; held-out file heldout/HELDOUT_025.md, sha256 6412b262...,
   written before launch) repeats them at 1e16 on the combined basis (2918 generators) with per-step density step norms (R-TANGENT). 024 (MID 32 rule control of 016,
   heldout/HELDOUT_024.md) follows on core 54. Results in numerics_v12.
3. No candidate of this lane is a certification target; the certification requests of this version are nil beyond what the N4 numerical auditor chooses for 022 (structure and point gaps
   would complete its row). The N3 numerics worker's exact legqs norms of 016/017 (target 13:00Z) and the two-scale product keys for 020 to 025 remain the only route to exact norms of
   these candidates.
4. Every FLOAT held-out value above the graded ceiling 4.5717e-4 would, if certified, exclude the candidate from every registered scalar ball and graded box, as for
   016 to 020; the smallest largest-registered-value of the family is 022's 8.30e-4 (1.8 times the graded ceiling; 291 times the unrestricted sharpw ceiling 2.8496e-6).
