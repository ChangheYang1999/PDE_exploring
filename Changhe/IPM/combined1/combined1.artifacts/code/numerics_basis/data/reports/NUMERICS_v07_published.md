# numerics_v07 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v07; UTC time: 2026-10-29T05:29:10Z; supersedes numerics_v06 (sha256 b6b2ce9eded3326061243b570cf0c285cc0c2f5039e2bd54977ff38f924b9c73) and earlier versions.
- consulted (v07): theory_v03.md (the T1/T3 theory worker, 03:41:45Z; ACK 04:17Z); the coordinator team notes through 2026-10-29T05:26 (H8 checkpoint 04:32Z, matrix v42+); the N4 numerical auditor team notes
  and VERDICT_LEDGER.md through 2026-10-29T03:00:41. (N4-176/179/182 distances of 008, 009, 012; N4-178 constraint-nullity correction; N4-175 exact 1922-coordinate quotient);
  the N3 numerics worker team notes through 2026-10-29T04:33; the second model/weakprobe-asympt/answer.md. Batch N consultation: The N3 numerics worker and the N4 numerical auditor results cited by ID; new numbers are the N1/N2 numerics worker's FLOAT.
- theory version followed: theory_v03 (R6(b) Newton-step diagnostic, R6(c) held-out probes, R9 quotient basis, section 9 item 1 cell test, item 3 order).
  Candidate IDs new in v07: C1-N1-014-pairB-from007 (first-mode + angular pairing rows), C1-N1-015 (pairing rows on the exact quotient basis of 013; run in progress at publication, snapshot in v08 or in NUMERICS_FINAL).

## 0. Summary of what is new
1. Correction (N4-178): in numerics_v06 section 5 the 1022 zero singular values were described as the exact redundancy; the exact kernel of the reduced
   Gauss-Newton problem has dimension 1060 (all zero-potential directions lie in the constraint kernel, 2556 = 1496 + 1060) and 1022 is a floating
   threshold count; the inference that LM damping makes the physical step independent of the redundant coordinates is withdrawn. The exact quotient basis
   (1922 generators, optimization/quotient_basis.py) is used from now on: generators 2982 -> kept 1922 (removed 1060 exact zero-potential directions) in 1.8 s; physical spectrum in section 4.
2. C1-N1-014: 007 + 102 pairing rows (27 first-mode k values and the 75 angular probes n = 3..31 of the N4-160 family, uniform weight 1e12, MID 16, 12 CPU
   steps). G0 0.3726, kappa 0.7270; first-mode max m over k <= 4096 1.35e-04 (k = 2048); best N4-160-family probe 21:522 with m = 1.12e-03 (007: 2.87e-3 at (7,131); 013: 1.12e-3 at (21,522)).
3. theory_v03 R6(b) diagnostic (Galerkin L^2 Newton step in the constraint null space, LM damping 1e-6 and 1e-4, MID 24; optimization/newton_step.py):
   for 007 (lam 1e-6) ||h0||_2 = 1.845e-02, linearized residual 0.377 -> 0.338, mode-7 (7,131) pairing -1.69e-4 -> -4.41e-06 (FLOAT, MID 24); the span's L^2 floor, not the objective, limits the first Newton step.
4. theory_v03 section 9 item 1 (FW-T-DYADIC-Y-v1 cell test, modes 1 and 3, FLOAT proxy) for 008, 009, 010: FLOAT proxies computed for 008, 009, 010 (section 3); every cell ratio above 1 where marked; exact LBs are the N4 numerical auditor's.
5. Bridge probes k = 1e5 .. 1e7 for 007 (and 008, 009): PENDING.

## 1. Snapshot C1-N1-014-pairB-from007
Run: run_pair.py from the 007 coefficients, balanced E_2 objective of 007 plus 102 rows sqrt(1e12) I (27 first-mode probes k in {0..8, 12, ..., 4096} and the 75 angular
probes phi_(n,K) = r v^2 t^K sin(n theta), n = 3..31, K = (n-1)/2 + {0, 8, 32, 128, 512} of N4-160), MID 16 radial rule, 12 CPU steps (about 270 s each).
The uniform weight 1e15 (as in 013) was wrong for the angular rows: the angular pairings of 007 are 1e-4 to 2e-3 each, so PAIR = 1.8e10 dominated the 1.7e7
objective and the first Gauss-Newton step raised the F part 20x; at 1e12 the pairing part (3.6e7 at the start) is balanced against the rest. Last accepted
step: it   7 obj 1.720774e+07 -> 1.720754e+07 ACC pred 5.593e+03 lam 3.7e-04 parts F 1.539e+07 G 1.928e+05 P 3.656e+04 K 1.586e+06 PAIR 7.468e+02 max|I_k| 1.
Snapshot C1-N1-014-pairB-from007 (exact JSON sha256 8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746; same basis and 421 exact rows as 007; eleven EXACT-ZERO sectors).
FLOAT (diag2, MID 32): G0 0.3726 (007 0.3767, 013 0.3722), G1 3.440, P2 190.9, rF 7.810, H 0.6313, sup|F| 0.1409, theta 0.0114,
kappa 0.7270 (margin +0.072), X3 516.5, E2 605.2, R_nec(2^-18) 1.021e-03.
First-mode probes (MID 32; max over k <= 4096: 007 1.31e-4, 013 1.33e-04, 014 1.35e-04 at k = 2048):
| k | m_k 007 | m_k 013 | m_k 014 |
|---|---|---|---|
| 0 | 1.62e-05 | 5.94e-08 | 3.14e-08 |
| 1 | 1.82e-05 | 7.64e-08 | 1.87e-07 |
| 2 | 2.04e-05 | 8.58e-08 | 3.28e-08 |
| 3 | 2.31e-05 | 7.91e-08 | 2.08e-08 |
| 4 | 2.62e-05 | 6.57e-08 | 2.20e-09 |
| 5 | 2.92e-05 | 5.20e-08 | 4.16e-08 |
| 6 | 3.23e-05 | 4.06e-08 | 6.98e-08 |
| 7 | 3.52e-05 | 3.16e-08 | 8.06e-08 |
| 8 | 3.79e-05 | 2.39e-08 | 7.69e-08 |
| 12 | 4.77e-05 | 5.10e-09 | 1.86e-09 |
| 16 | 5.59e-05 | 7.50e-09 | 7.76e-08 |
| 24 | 6.99e-05 | 9.66e-09 | 2.49e-07 |
| 32 | 8.18e-05 | 6.85e-08 | 5.09e-07 |
| 48 | 9.67e-05 | 6.87e-08 | 1.10e-06 |
| 64 | 9.74e-05 | 3.10e-07 | 1.45e-06 |
| 96 | 7.35e-05 | 5.83e-07 | 1.61e-06 |
| 128 | 4.40e-05 | 1.64e-06 | 4.30e-07 |
| 192 | 1.64e-06 | 3.43e-06 | 8.80e-06 |
| 256 | 1.57e-05 | 7.76e-06 | 1.54e-05 |
| 384 | 9.37e-07 | 1.12e-05 | 2.36e-06 |
| 512 | 2.91e-05 | 3.60e-05 | 2.76e-05 |
| 768 | 2.63e-05 | 2.80e-05 | 2.14e-05 |
| 1024 | 2.39e-05 | 2.44e-05 | 2.96e-05 |
| 1536 | 1.10e-04 | 1.11e-04 | 1.15e-04 |
| 2048 | 1.31e-04 | 1.33e-04 | 1.35e-04 |
| 3072 | 7.35e-05 | 7.51e-05 | 7.64e-05 |
| 4096 | 8.67e-06 | 7.33e-06 | 6.45e-06 |
Held-out and in-objective angular probes (weak_tests3, N4-160 family, FLOAT; for 014 the rows n = 3..31 at these K WERE in the objective, so only the first-mode
probes not in the list and the comparison with 013 are held-out evidence; 013 had no angular rows):
| mode n | best m 007 | best m 013 | best m 014 |
|---|---|---|---|
| 1 | 1.47e-04 | 1.49e-04 | 1.52e-04 |
| 3 | 7.19e-04 | 1.61e-04 | 1.06e-04 |
| 5 | 8.67e-04 | 4.86e-05 | 4.27e-05 |
| 7 | 2.87e-03 | 7.22e-05 | 8.42e-06 |
| 9 | 1.91e-03 | 2.68e-05 | 2.27e-05 |
| 11 | 2.01e-04 | 1.22e-05 | 9.48e-06 |
| 13 | 5.91e-05 | 2.47e-05 | 1.06e-05 |
| 15 | 3.04e-05 | 1.91e-05 | 5.57e-06 |
| 17 | 3.89e-05 | 2.47e-05 | 3.53e-05 |
| 19 | 1.50e-04 | 1.90e-04 | 1.60e-04 |
| 21 | 1.12e-03 | 1.12e-03 | 1.12e-03 |
| 23 | 7.62e-04 | 7.58e-04 | 7.58e-04 |
| 25 | 5.49e-04 | 5.28e-04 | 5.51e-04 |
| 27 | 3.23e-04 | 3.10e-04 | 3.17e-04 |
| 29 | 2.02e-04 | 2.00e-04 | 1.96e-04 |
| 31 | 1.22e-04 | 1.19e-04 | 1.23e-04 |
Best probe: 007 7:131 (2.87e-03), 013 21:522 (1.12e-03), 014 21:522 (1.12e-03).

## 2. Newton-step diagnostic (R6(b), R9(e))
Definition (theory_v03 R6(b)): min over delta in the constraint null space (421 exact rows and the 5 linearized Taylor rows) of ||F(a) + J delta||_(L^2(0.02 <= r <= 1e4)),
J = dF/da, so J delta = L h0 with h0 the density of delta (the quadratic term is reported separately); solved by the column-scaled normal equations with
Levenberg-Marquardt damping lam (the undamped solve, lam = 1e-10, gives a meaningless step in this rank-deficient basis: linearized residual 0.66 > 0.38,
||h0||_2 0.053, negative predicted reduction). MID 24 rule, midpoint 180. FLOAT.
| candidate | LM lam | ||F||_2 | linearized ||F + J delta||_2 | ||F(a + delta)||_2 | ||h0||_2 | mode-7 (7,131) pairing F -> F + J delta | mode-1 k = 0 pairing |
|---|---|---|---|---|---|---|---|
| C1-N1-007 | 1e-6 | 0.3767 | 0.3383 | 0.3383 | 1.845e-02 | -1.690e-04 -> -4.406e-06 | +1.551e-04 -> +3.487e-05 |
| C1-N1-007 | 1e-4 | 0.3767 | 0.3465 | 0.3464 | 1.675e-02 | -1.690e-04 -> -1.863e-05 | +1.551e-04 -> +3.936e-04 |
| C1-N1-013 | 1e-6 | 0.3722 | 0.3384 | 0.3384 | 1.411e-02 | -3.846e-07 -> -4.515e-06 | -5.688e-07 -> +2.533e-05 |
Reading: in the 007 generator span the Galerkin L^2 Newton step has ||h0||_2 of order 1.7e-2 to 1.8e-2 (T4-185 proves > 0.0047694 for every L^2 Newton step from 007;
consistent) and reduces the L^2 residual only from 0.377 to 0.34: this is the L^2 floor of the span, the same limitation as the optimizer plateau. The step
reduces the (7, 131) pairing of the linearized residual by a factor 10 to 40, within R9(e)'s bound |<F + L h0, phi>| >= |I| - D ||h0||_2. These numbers are
the design objective theory_v03 asks for; they say that no basis of this family brings the first Newton step near a registered ball (factor 4e3 to the
largest scalar budget), i.e. the obstruction is the span, not the objective. Note (the T1/T3 theory worker, numerics_v06 ACK): the coordinate-invariant step uses the physical
Gram on the admissible tangent (T4-229); the Euclidean damping used here is basis-dependent, so the two lam values bracket the FLOAT answer.

## 3. Cell test proxy for 008, 009, 010 (section 9 item 1)
Cells [l, h] of a: [0,1/4], [1/4,1/2], [1/2,3/4], [3/4,1], [1,5/4], [5/4,3/2], [3/2,7/4]; thresholds at l (theory_v03 section 5): 15.88162, 8.716729, 4.799949, 2.565236, 1.263642, 0.5028299, 0.06411577. Entry: FLOAT mode 1+3 projected N_h at the right end (ratio to the threshold); a cell is excluded when a certified LB exceeds the threshold.
| candidate | [0,1/4] | [1/4,1/2] | [1/2,3/4] | [3/4,1] | [1,5/4] | [5/4,3/2] | [3/2,7/4] | FLOAT verdict |
|---|---|---|---|---|---|---|---|---|
| C1-N1-008 | 65.9 (4.15) | 59.9 (6.87) | 55.3 (11.53) | 51.8 (20.18) | 48.9 (38.66) | 46.4 (92.28) | 44.3 (690.86) | all cells excluded (FLOAT) |
| C1-N1-009 | 14.1 (0.89) | 11.1 (1.27) | 9.02 (1.88) | 7.51 (2.93) | 6.39 (5.06) | 5.54 (11.03) | 4.88 (76.14) | NOT all excluded |
| C1-N1-010 | 92 (5.79) | 82.2 (9.43) | 75.9 (15.81) | 71.3 (27.78) | 67.6 (53.47) | 64.5 (128.28) | 61.9 (965.09) | all cells excluded (FLOAT) |
(the N4 numerical auditor's N4-186 found 008 fails the seven-cell test exactly; these FLOAT values are proxies for 009 and 010 pending the N4 numerical auditor.)

## 4. Exact quotient basis and the physical Gauss-Newton spectrum (R9)
optimization/quotient_basis.py: block-diagonal exact rref (python-flint) of the canonical-term matrix of the generators, pivot generators kept, coefficients re-expressed exactly; verification: identical merged canonical terms. Output for 007: generators 2982 -> kept 1922 (removed 1060 exact zero-potential directions) in 1.8 s / exact check passed: identical canonical monomial terms (1922)
Physical Gauss-Newton spectrum on the quotient basis (gn_spectrum.py, MID 16, balanced objective): reduced dimension 1496 (constraint rank 426), scaled singular values: min 0.000e+00, 1 percent 0.000e+00, 10 percent 0.000e+00, median 3.697e-03, max 1.067e+01; raw condition number inf; reduced gradient norm relative 8.21e-04. Resolution of a binary64 normal-matrix spectrum is about 1.5e-8 of the largest singular value (theory_v03 R9(c)); no inverse bound is claimed (R9(d)).
Counts on the quotient basis: 494 of the 1496 admissible directions have scaled singular values below 1e-8 of the largest (at or below the resolution
floor: they may be anywhere between 0 and 1e-8), 497 below 1e-6 and 628 below 1e-4. These are NOT exact zero potentials (those 1060 were removed exactly);
they are directions whose effect on the balanced weighted residual on the mesh is below the binary64 resolution, so the Gauss-Newton problem on the physical
tangent space is itself strongly ill-conditioned and the Levenberg-Marquardt damping acts substantially in a third of the directions. Consequence for the
reading of the plateaus: the relative reduced gradient 8.2e-4 is FLOAT evidence of near-stationarity in the well-conditioned directions only; whether the
plateau at 1.72e7 is a conditioning stall in the remaining directions cannot be decided from a normal-equation spectrum (an extended-precision QR of the
G-orthonormalized design matrix would be needed, R9(c)). This supersedes the numerics_v06 section 5 sentence that the plateaus are 'genuine'.

## 5. Bridge probes
PENDING.

## 6. Status and next steps
Published 2026-10-29T05:29:10Z. Best candidate unchanged: C1-N1-007 (certified: G0 0.37669, G1, P2, Q3, (B-L2); distance 0.004769 in mode 7; forcing gap 3.6e6 in sharpw with
The N3 numerics worker's complete components). New snapshots: C1-N1-013-pairU-from007 (04:39:56Z) and C1-N1-014-pairB-from007 (05:22:50Z), both design experiments (rows
in the objective; theory_v03 R6(c)) and not certification targets. What they establish (FLOAT): the weak pairings of every tested family (first mode k <= 128,
angular modes 3 to 15 at K <= 131) are removable by one to three orders of magnitude at r <= 10 at no cost in G0, kappa or sup|F|, and every probe localized
at r >= 20 (first mode k >= 384, N4-160 probes at K about 520 for modes 19 to 31, m about 1.1e-3) is unchanged even when it is a row of the objective:
the fixed-c distance of the 007 family has a mid-field floor of order 1e-3 set by the reachability of the inner basis (about r = 10 to 20), consistent with
the Newton-step diagnostic (the span's L^2 floor 0.34, ||h0||_2 about 1.5e-2) and with the dyadic profiles. Running at publication: the first optimization on
the exact quotient basis (1922 generators, 013 start, 102 pairing rows; core 52) -> C1-N1-015, to test whether the redundancy affected the plateaus (N4-178
leaves this OPEN); its result goes to NUMERICS_FINAL.md (and v08 if time permits). Requests to batch T: none new; theory_v04 will be ACKed within the
hour. Requests to the N4 numerical auditor: held-out exact probes (21, 522), (23, 523), (25, 524) and the frozen T4-182/T4-185 vectors on 013 and 014 (expected about 1e-3 for
the first group); the 009 first cell [0, 1/4] needs modes beyond 1 and 3 or the full N_a (FLOAT ratio 0.889 with modes 1 and 3).
