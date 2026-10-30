# numerics_v10 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v10; UTC time: 2026-10-29T08:47:14Z; supersedes numerics_v09 (sha256 e77839d57014df0345334a0de15a32b3419292a775647823f2ce1db1fd564862) and earlier versions.
- consulted (v10): theory_v05.md (the T1/T3 theory worker, 06:39:59Z; ACK 07:13Z; theory_v06 not published at 2026-10-29T08:47:14Z); the coordinator team notes through 08:30Z (H12 checkpoint;
  08:13Z item 2 T4-340 repair request; 08:06Z item 2(c)); the T4 theory auditor T4-340 (audit record numerics_final_h12_audit, proof); the T1/T3 theory worker's ACK of numerics_v09 (eight items);
  the N4 numerical auditor status file/NOTES through 08:20Z (ledger to N4-274: N4-272 018 floors, N4-273 016/017 partition, N4-274 mixed-scale dimension 2426, N4-264 backend);
  the N3 numerics worker status file through 08:16Z (legqs exact extension in progress, target about 13:00Z). Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by ID; the new
  numbers are the N1/N2 numerics worker's FLOAT values offered for certification.
- theory version followed: theory_v05 (R-HOLDOUT (i)-(iii) reporting format; R-TANGENT; section 6 items). Candidate IDs new in v10: C1-N1-019-legqs50-cont12
  (08:28:42Z) and C1-N1-020-legqs25p50-quot013 (2026-10-29T08:46:18Z). Chart PRIMARY for both: c_l = 4076476460239181/2^51 and Theta_0 of state 131 EXACT, center relation
  EXACT, a_0 free (FLOAT value in each MANIFEST); coefficient file path: working file candidate_snapshots (not published)/<ID>/<tag>_exact.json (sha256 in SHA256SUMS).
- Every number below is FLOAT (MID 32 rule: radial Gauss 32 per unit log-panel x angular midpoint 180 on 0.02 <= r <= 8356.47, exterior from the exact sectors)
  unless labelled EXACT, LOSS (optimizer objective, MID 16) or cited by a working file the N3 numerics worker (not published) ID. Every comparison is a trial comparison: no inference about
  spans, angular-band mass or stationarity is drawn (T4-340).

## 0. Summary of what is new
1. Repairs (T4-340, the T1/T3 theory worker ACK of v09) applied to NUMERICS_FINAL.md at 08:50Z (marked [R]): the 'span limit' and 'mass into modes 33 to 47' inferences of
   numerics_v08/v09 and of the 08:02Z draft are WITHDRAWN (finite probes bound nothing; a better trial in an enlarged basis gives no lower bound for the old
   family); the Newton-step dampings give only the range observed at the two tested values; the quadrature statement is a calibration on the tested
   integrands, not an error bound; the exclusion scope is the matrix scope (every registered scalar ball and original graded box through 018 except the FLOAT
   comparison 011; dyadic only at 131, d2, 007 to 010; localized route incomplete); the legqs blocks m = 9..15 carry density modes 17 to 31 (N4-248/T4-321),
   so the 'held-out' probes of 016/017 in mode 19 and above are held out while mode 17 is an objective row; the eleven-sector list is ten nonautomatic
   cancellations (old index (h,0), h = 1..7, (0,1), (1,1), (2,1); global K = h + 1) plus the automatic leading sector; 004 cancels only old (1,0), (2,0), (3,0).
   Section 4b: the 'linearized' values 0.200 (016) and 0.217 (017) are linear-model values ||F + J delta||_2, not evaluated residuals; a certified pairing at
   any probe remains a rigorous necessary test whether or not the probe was an objective row (014 and 015 optimized angular pairings and still carry
   certified violations).
2. C1-N1-019 (017 continued 12 CPU steps, unchanged objective): held-out values within -8/+9 percent of 017's; G0 0.3251 (017 0.3209). Same pattern as 018.
3. C1-N1-020 (016 basis + 252 legqs R0 = 50 functions = scales 25 and 50 together, 2426 generators, 67 rows, 12 CPU steps): LOSS 1.7475e7 -> 1.3502e7, the lowest
   objective of the campaign, G0 0.3201 (MID 32), but the registered held-out probes at K >= 1200 are 10 to 20 percent ABOVE 016/017 ((19,1800) 1.14e-3 against
   9.0e-4 / 1.03e-3) and several small-r held-out probes in modes 19 to 31 (K0 = 0, 8, 32; r 3 to 6) rose by up to 8x: the objective gain went into rF and
   the derivative terms, not into the held-out mid-field pairings. Not a certification target.
4. GPU 7 is available to this lane again (GPU_UPDATE.md 02:51Z, used from 08:32Z). Two pre-registered GPU runs are in progress (section 4): 021 (020 basis
   with 14 held-in mid-field rows; 40 steps) and 022 (016 + 240 legqs functions in the higher blocks m = 16..23; 12 then 40 steps).
5. Answer to the coordinator 08:06Z item 2(c): neither 019 nor 020 is a certification target; if the N4 numerical auditor wants one mixed-scale snapshot for the N4-264 backend, 020 is
   the one (structure and point gaps suffice for its row).

## 1. C1-N1-019-legqs50-cont12 (continuation of 017; snapshot 08:28:42Z; exact JSON sha256 ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419)
Basis and rows identical to 017 (2174 generators = exact quotient of 013 (1922) + 252 legqs R0 = 50 in j = 1..3, m = 9..15; 421 exact rows; ten nonautomatic
EXACT-ZERO sectors, first survivor (3,1) at exponent -2.7904 (old index), full-circle 4905.4). Objective rows (R-HOLDOUT (i)): the 27 first-mode k in
{0..8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096} and the 40 N4-160 probes with n <= 17 (K = (n-1)/2 + {0, 8, 32, 128, 512}),
weight 1e12. HELD-OUT (ii): the N4-160 probes n = 19..31 at the same K0 and the 25 registered probes n in {19, 23, 25, 29, 31} x K in {600, 900, 1200, 1800, 2400}.
LOSS 1.4400e7 -> 1.42514e7 (12 steps, 160 s each on CPU). FLOAT (MID 32): G0 0.32505, G1 3.5868, P2 202.20, rF 7.0007, H 0.61416, sup|F| 0.1578; (B-L2) theta_inner
0.0114, kappa_inner 0.7284, margin +0.0705. First-mode weak probe (weak_tests2): max over the 27 sampled k 1.5e-4 (FLOAT).
| held-out probe (n, K) | 017 | 019 |
|---|---|---|
| (21, 522) | 3.36e-4 | 3.55e-4 |
| (23, 523) | 3.22e-4 | 3.36e-4 |
| (25, 524) | 2.43e-4 | 2.51e-4 |
| (29, 526) | 8.95e-5 | 9.78e-5 |
| (23, 1200) | 2.72e-4 | 2.51e-4 |
| (23, 1800) | 5.76e-4 | 5.66e-4 |
| (23, 2400) | 6.35e-4 | 6.34e-4 |
| (25, 2400) | 5.30e-4 | 5.25e-4 |
| (19, 1800) (largest) | 1.03e-3 | 1.02e-3 |
Reading (trial comparison): under the unchanged balanced objective the continuation moves the held-out values by less than 10 percent either way while the
objective falls 1 percent and G0 rises 1 percent; the pattern of 018 (016 continued) repeats. Not a certification target (every held-out value is above the
graded ceiling 4.5717e-4 or far above the sharpw ceiling 2.84e-6).

## 2. C1-N1-020-legqs25p50-quot013 (scales 25 and 50 together; snapshot 2026-10-29T08:46:18Z; exact JSON sha256 bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf)
Start = 016's exact JSON (2174 generators) + 252 legqs R0 = 50 functions (Q = 4, 12 per block, zero start) in the same blocks j = 1..3, m = 9..15: 2426 generators
(N4-274 proves the abstract potential and density dimension 2426 for old + R25 + R50), 421 exact rows, ten nonautomatic EXACT-ZERO sectors, first survivor
(3,1) at -2.7904. Same 67 objective rows and the same HELD-OUT set as 016/017/019 (section 1). LOSS 1.7475e7 -> 1.3502e7 (12 CPU steps, 180 to 195 s each);
MID 16 report G0 0.3197, rF 6.69, P2 227, G1 3.91. FLOAT (MID 32, diag2): G0 0.32006 (016 0.3089, 017 0.3209), G1 3.913, P2 226.9, rF 6.744 (016 7.146), H 0.6113, sup|F| 0.1996 (016 0.150: the largest of the legqs family), theta_inner 0.0114, kappa_inner 0.7374 ((B-L2) margin +0.0615). The objective gain of 020 against 016 sits in rF and the near-field log term; G0 and sup|F| are worse.
| held-out probe (n, K) | 013 | 016 | 017 | 020 |
|---|---|---|---|---|
| (21, 522) | 1.12e-3 | 2.33e-4 | 3.36e-4 | 2.94e-4 |
| (23, 523) | 7.58e-4 | 2.32e-4 | 3.22e-4 | 2.99e-4 |
| (25, 524) | 5.28e-4 | 1.70e-4 | 2.43e-4 | 2.36e-4 |
| (27, 525) | 3.10e-4 | 1.04e-4 | 1.60e-4 | 1.66e-4 |
| (29, 526) | 2.00e-4 | 3.77e-5 | 8.95e-5 | 1.03e-4 |
| (31, 527) | 1.19e-4 | 3.26e-5 | 5.82e-5 | 6.17e-5 |
| (23, 1200) | - | 2.97e-4 | 2.72e-4 | 3.43e-4 |
| (23, 1800) | - | 5.94e-4 | 5.76e-4 | 6.83e-4 |
| (23, 2400) | - | 6.50e-4 | 6.35e-4 | 7.59e-4 |
| (25, 2400) | - | 5.37e-4 | 5.30e-4 | 6.34e-4 |
| (29, 2400) | - | 2.72e-4 | 3.05e-4 | 3.68e-4 |
| (31, 2400) | - | 1.99e-4 | 2.53e-4 | 3.15e-4 |
| (19, 1800) (largest) | - | 9.02e-4 | 1.03e-3 | 1.14e-3 |
Small-r held-out probes (K0 = 0, 8, 32, r about 3 to 6) in modes 19 to 31, 016 -> 020: (19, 9) 2.1e-5 -> 1.68e-4; (23, 19) 2.0e-5 -> 1.39e-4; (27, 21)
3.8e-6 -> 1.45e-4; (29, 22) 3.2e-5 -> 8.5e-5; (31, 15) 1.0e-5 -> 6.4e-5 (013 values 2e-5, 1.9e-5, 3.2e-6, 5.9e-7, 6.5e-6). Reading (trial comparison): the second
scale lowered the objective (rF, derivative terms) but did not lower any registered held-out probe below 016's; the held-out pairings at r 3 to 6 in the modes
of the added blocks rose by up to 8x, i.e. the balanced objective does not control angular pairings that are not rows at any radius. 020 is OPEN and not a
certification target; it is the natural reproduction target for the N4-264 mixed-scale backend if the N4 numerical auditor wants one.

## 3. What the 016 family says so far (FLOAT, trial comparisons; the inferences of v08/v09 withdrawn)
1. Adding resolved mid-field functions (016, 017, 020) lowers the held-out values at r 19 to 32 by factors 2.5 to 5 relative to 013 at equal step count,
   and raises mode 19 at K >= 900 (016: 5.3e-4 to 9.0e-4 against 013's 2.3e-4 at (19, 1800) in the v08 table). The gains are at the tested probes only.
2. Continuing the unchanged balanced objective (018, 019) or adding the second scale (020) does not lower the held-out values further; the objective keeps
   falling through rF and the derivative terms. An objective that holds the mid field needs the mid-field pairings as rows (021 tests this with a
   separate held-out set).
3. Every certified distance of the family (016 > 1.4704e-3, 017 > 1.6718e-3, 018 > 1.6558e-3 at (19,1800)) is above the graded ceiling by factors 3.2 to 3.7
   and above the sharpw ceiling by factors above 515: the family is RULED OUT in every registered ball, like 007 to 015.

## 4. GPU runs in progress (pre-registered in the N1/N2 numerics worker team notes 08:33Z; results in numerics_v11)
- C1-N1-021 (tag legqs25p50_heldin14_gpu_m16): start 020; objective = balanced E_2 + 1e12 I^2 over 81 rows = the 67 rows above + 14 HELD-IN mid-field rows
  (N4-160 probes n = 19..31 odd at K = (n-1)/2 + 128 and + 512, r about 12 to 15 and 23 to 32); HELD-OUT (never rows): the 25 registered probes and the
  N4-160 probes n >= 19 at K0 in {0, 8, 32}; 40 GN steps at MID 16 on GPU 7. Judged on the 25 registered probes against 016/017/020.
- C1-N1-022 (tags legqs25_m16to23_gpu_m16_s12 and legqs25_m16to23_gpu_m16): start 016 + 240 legqs R0 = 25 functions in the existing higher blocks j = 1
  (m = 16..19), j = 2, 3 (m = 16..23) -> 2414 generators (density modes 31 to 47); same 67 rows and the same HELD-OUT set as 016; 12 steps (controlled
  comparison with 016 at equal step count and rule), then 28 more.
- Later today (one run per core, GPU shared with another lane; memory checked before each launch): scale 100 functions; the MID 32 rule for the objective;
  a sup-type term; longer runs of whichever of 021/022 holds the mid field. Every run: held-out set fixed and posted before launch; MID 32 for every reported
  number; exact JSON + snapshot + MANIFEST.

## 5. Requests to batch T and to working file the N4 numerical auditor (not published)
1. The N3 numerics worker: the exact legqs E_2 components of 016 and 017 (pipeline target 13:00Z) are the only exact norms of legqs candidates; 020 (scales 25 and 50) needs
   the two-scale product keys (N4-264 backend exists on the N4 numerical auditor's side).
2. The N4 numerical auditor: no certification request for 019 or 020 beyond what the N4 numerical auditor chooses for the N4-264 backend (020 structure/point gaps). The certification requests for
   016/017 are complete (N4-253, N4-257 with T4-311, T4-331).
3. Batch T (theory_v06): the design lever that remains is the mid field at r 10 to 40 in the modes 17 to 31 and the small-r angular pairings in the same modes
   (020 shows they move by 8x under a mid-field basis change). If a forcing norm weights these regions less than the registered L^2 balls do, the numerics
   can optimize it; if not, the required factors (3.2 to 3.7 on the certified floors for the graded box; above 515 for sharpw) are the quantitative gap to report.
