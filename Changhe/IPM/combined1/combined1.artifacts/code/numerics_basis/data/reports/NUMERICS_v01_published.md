# numerics_v01 (batch N publication; author the N1/N2 numerics worker)

Header
- version: numerics_v01; UTC time: 2026-10-28T21:53:10Z; author: The N1/N2 numerics worker (N1 far field, N2 optimization; batch N publisher).
- consulted lanes and files: The N3 numerics worker (status file, team notes 21:14Z table of VALIDATED components), the N4 numerical auditor (VERDICT_LEDGER.md N4-001..N4-024,
  team notes 21:25Z angular-rule finding), the coordinator (the run contracts v01+v02+v03, team notes 21:25Z, closure_matrix.md v02).
- supersedes: none. Candidate IDs: C1-BASE-S131, C1-BASE-S088, C1-A2-d2 (checked), C1-N1-001-refit860-jabs (new), C1-N1-002-7branch-frf (new, seven-branch).
- norm IDs used: NORM-A2-E2 components G0, rF (Hardy upper bound for H), G1, P2, H; the case4 training loss J_abs (LOSS only).
- theory version followed: none published yet (theory_v01 expected 22:15Z-22:30Z). Response to theory_vMM: not applicable (v01).

## 1. Source checkpoint and candidate IDs

State identification (prompt section 7). The read-only case4 tree holds two archived 860-generator states: state 088 (the last state checked
independently by the case4 team, data cut 2026-10-26T04:00Z) and state 131 (the last state the optimizer accepted before termination at
13:28Z on 2026-10-26, "explicitly unverified" by that team). No accepted state newer than 131 exists in the archive (checkpoints/ holds only
088 and 131; snapshots 1..88 are JSON only; the run record ends at trial 157 in progress). analysis2 analysed state 131; the run contracts section 2
fixes the PRIMARY chart at state 131. We use state 131 (C1-BASE-S131) as the reference and record state 088 (C1-BASE-S088) for comparison.

| quantity | state 131 (C1-BASE-S131) | state 088 (C1-BASE-S088) |
|---|---|---|
| c_l | 1.810319210199998 = 4076476460239181/2^51 (EXACT) | 1.8085383949271123 = 4072466420739489/2^51 |
| a_0 = rho_y(0) | 12102479225522702540364244077864789/1174964343508337542719888806641664 = 10.30029489183... (EXACT, reproduced) | 10.29757491765872 |
| center (B0n) | sum_i a_i chi_i,xxyy(0) = 1 - c_l EXACT (analytic a_000; reproduced: difference 0 in rational arithmetic) | same construction |
| canonical sha256 of the 860 exact coefficients | 4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01 (reproduced by my own code) | not recomputed |
| J_abs (LOSS, training mesh 944 x 96) | 1.2673066866466649e-11 (saved) | 2.7441060958610383e-11 |
| five Taylor defects (origin, quadratic+quartic R_f coefficients) | 1.99e-15, 4.33e-14, 2.09e-13, 1.29e-13, -1.29e-13 (reproduced exactly) | max 1.13e-12 |

Independent recomputation of the state-131 residual (prompt section 7; FLOAT): my own polar evaluator (numerics/lib/ipm_eval.py; float64,
GPU; separable radial x angular representation, stable linear transport, no code shared with case4) gives on the case4 training mesh
excluding the origin block r < 0.02 (where binary64 cancellation makes a direct evaluation meaningless; the block contributes 3.4e-22 to J_abs):
J_abs = 1.26730668564e-11 (saved values on the same nodes: 1.26730668661e-11; pointwise agreement 6e-11 absolute for 0.1 <= r < 1, 1e-12 for
1 <= r < 10, 1e-14 beyond). Denser rule (origin 48 / middle 64 per unit log-radius panel / infinity 512, angular Gauss 192; 1888 x 192 nodes,
r >= 0.02): J_abs = 1.26730668441e-11. The quadrature is converged to about 2e-9 relative; J_abs is a LOSS, not a norm (the N4 numerical auditor N4-005/N4-006
give the exact full-axis value 1.2673066866466506e-11).

## 2. Exact far-field sector table of state 131 (EXACT, rational arithmetic on the exact coefficients)

Exponents e(h,q) = gamma - h delta - 2q with gamma = 2^51/4076476460239181, delta = 1 - gamma. Quarter-plane L^2 norms of the angular sine
polynomials E_(h,q)(theta) (full circle = 2x). Code numerics/lib/ipm_exact.py (own derivation of the density and stream rules, checked by
the exact Poisson identity in every sector and against case4 farfield860.py and the analysis2 numbers).

| (h,q) | exponent | status | max harmonic | quarter L^2 | full-circle L^2 |
|---|---|---|---|---|---|
| (0,0) | +0.5523887690 | EXACT-ZERO (identity c gamma = 1) | - | 0 | 0 |
| (1,0) | +0.1047775380 (= 427123167131315/4076476460239181) | EXACT-NONZERO | 39 | 0.0910394455355629 | 0.1820788910711258 |
| (2,0) | -0.3428336930 | EXACT-NONZERO | 39 | 2.1264082517 | 4.2528165034 |
| (3,0) | -0.7904449240 | EXACT-NONZERO | 39 | 16.646258398 | 33.292516796 |
| (4,0) | -1.2380561551 | EXACT-NONZERO | 39 | 51.957478234 | 103.91495647 |
| (0,1) | -1.4476112310 | EXACT-NONZERO (= -2 c_l G_(0,1); ||G_(0,1)|| = 15.41715954657126) | 19 | 55.819960188 | 111.63992038 |
| (5,0) | -1.6856673861 | EXACT-NONZERO | 39 | 55.992444377 | 111.98488875 |
| (1,1) | -1.8952224620 | EXACT-NONZERO (||G_(1,1)|| = 40.01760144955358) | 39 | 103.77091464 | 207.54182929 |
| (6,0) | -2.1332786171 | EXACT-NONZERO (first admissible exponent) | 39 | 67.796199218 | 135.59239844 |

All eight forbidden sectors (exponent >= -2) are nonzero: F(state 131) is not in Hdot^-1, L^2 or N_s (A2-THEOREM Corollary E1); only
P2 = ||omega D^2 F||_2 = 25.189... and Q3 are finite (the N3 numerics worker VALIDATED enclosures, the N4 numerical auditor confirmed). Leading coefficients of E_(1,0):
e_1 = 0.0026452404461014, e_3 = -0.0241094173386129, ..., e_39 = -7.698363346447813e-7 (all agree with analysis2 P3 and the N4 numerical auditor N4-002).

## 3. Exact stationary recursion from Theta_0 of state 131 (N1; EXACT to order 12)

G_0 = Theta_0 (odd sine harmonics 1..19; quarter norm 16.57100026302882), alpha_n = gamma - n delta, and for n >= 1
G_n = [ sum_{i+j=n-1} ((alpha_i+1) Phi_i G_j' - alpha_j Phi_i' G_j) ] / (n (c_l - 1)),  Phi_n from the exact potential inversion
(stream rule), checked against the angular Poisson identity -Phi'' - (alpha+1)^2 Phi = alpha cos theta G - sin theta G' in every order.
File numerics/far_field/state131_stationary_orders_0_12.json (exact rationals, densities G_n, streams Phi_n, potentials C_n).

| n | alpha_n | quarter ||G_n|| | ratio | max harmonic | n(c_l-1)||G_n|| = norm of the residual sector (n,0) if branch n is absent (quarter) |
|---|---|---|---|---|---|
| 0 | +0.5524 | 16.571 | - | 19 | 0 |
| 1 | +0.1048 | 6.8326 | 0.41 | 39 | 5.5366 |
| 2 | -0.3428 | 9.5149 | 1.39 | 59 | 15.420 |
| 3 | -0.7904 | 20.391 | 2.14 | 79 | 49.569 |
| 4 | -1.2381 | 53.324 | 2.62 | 99 | 172.84 |
| 5 | -1.6857 | 129.00 | 2.42 | 119 | 522.67 |
| 6 | -2.1333 | 316.88 | 2.46 | 139 | 1540.64 (A2 P27 / the N4 numerical auditor N4-003: 3081.274 full circle) |
| 7 | -2.5809 | 853.28 | 2.69 | 159 | 4839.98 (A2 P32: 9679.97 full circle) |
| 8 | -3.0285 | 2714.4 | 3.18 | 179 | 17596 (the N4 numerical auditor N4-003: 35192.4 full circle) |
| 9 | -3.4761 | 43090 | 15.9 | 199 | 314247 |
| 10 | -3.9237 | 56197 | 1.30 | 219 | 455376 |
| 11 | -4.3713 | 201191 | 3.58 | 239 | 1.7933e6 |
| 12 | -4.8189 | 552227 | 2.75 | 259 | 5.3698e6 |

Observation (HEURISTIC): ||G_n||^(1/n) is about 3.0 at n = 12, so the formal tail series rho ~ sum_n r^(alpha_n) G_n(theta) converges only for
r^delta > about 3, i.e. r > about 12 (root test on 13 terms; the jump at n = 9 shows the ratios are irregular). Consequences for closure (exact
formula, FLOAT evaluation): a candidate whose far field is the stationary tail truncated after branch N (every sector (h,0), h <= N, and the
descendants with exponent >= -2 cancelled exactly) has the invariant residual sector (N+1,0) with the norm in the last column, and for r > R
contributes to the E_2 components at least
  ||F||_{L^2(r>R)} = ||E_(N+1,0)||_full R^(alpha_(N+1)+1) / sqrt(-2 alpha_(N+1) - 2),   ||rF||_{L^2(r>R)} = ||E||_full R^(alpha+2) / sqrt(-2 alpha - 4),
e.g. (N = 6, R = 100): ||rF||_{r>100} = 309, ||F||_{r>100} = 1.9e-3; (N = 7, R = 100): 107 and 2.9e-3; (N = 12, R = 100): 5.2 and 7e-4.
The Hdot^-1 component is dominated by the same sectors (the N4 numerical auditor N4-020: ||F_d2||_H = 390.2 with first surviving sector (6,0)); for the Hdot^-1
norm the harmonic-1 coefficient dominates through the kernel 1/(2n). These floors are far above every registered threshold; they are the
quantitative form of the obstruction for any finite-branch family and they make the far-field weight of the forcing norm the decisive
question for batch T (see section 8). For the L^2 low metric of the T4 theory auditor T4-019 (no H component; the coordinator 21:34Z) only ||F||_{L^2(r>R)} matters:
with N branches cancelled and onset radius R it is ||E_(N+1,0)||_full R^(alpha_(N+1)+1)/sqrt(-2 alpha_(N+1)-2) (FLOAT evaluation of the exact
formula): N = 3 (first surviving (4,0), exponent -1.238): 501 R^(-0.238) = 167 (R = 100), 56 (1e4); N = 4: 893 R^(-0.686) = 38, 1.6;
N = 5: 2045 R^(-1.133) = 11, 0.06; N = 6: 5445 R^(-1.58) = 3.7, 2.5e-3; N = 7: 17466 R^(-2.03) = 1.5, 1.3e-5; N = 8: 2.8e5 R^(-2.476) =
3.1, 1.2e-5; N = 9: 3.8e5 R^(-2.92) = 0.55, 7e-7. The onset radius is not free: the tail series converges only for r > about 12, and the
inner basis (Legendre degree <= 25 in t = r^2/(1+r^2)) resolves the mid field only to r of order 20-25; between there and R the residual
is the truncated-tail residual sum_{n>N} n(c-1)|G_n| r^(alpha_n) (at r = 20: 3.8 for N = 10; at r = 50: 0.07; at r = 100: 3e-3).
Extending the inner resolution to r of order 100 (higher Legendre degree) is therefore part of the plan (section 8).

## 4. Candidates (far-field repair, prompt section 8)

### 4a. C1-N1-001-refit860-jabs: constrained refit in the EXISTING 860 basis
Snapshot SH/candidate_snapshots/C1-N1-001-refit860-jabs (MANIFEST.json, exact coefficients candA_Jabs_exact.json sha256
8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7, exact sector table). PRIMARY chart (c_l and Theta_0 exact as state 131),
(B0n) EXACT. Linear constraints (61 rows, exact): center; Theta_0 (10 leading moments of branch 0); q=1 descendant moments of branches 0,1
zero (20); leading moments of branches 1,2,3 equal to the harmonics<=19 truncation of the sequential stationary targets (30). Five Taylor
equations to 4e-11. Objective J_abs on 0.02 <= r (training mesh), 60 Gauss-Newton steps (own optimizer, GPU, ~2 s per step).
Result (EXACT sector table): (0,1) and (1,1) EXACT-ZERO; (1,0), (2,0), (3,0) reduced to their harmonics 21..39 (quarter norms 2.1033e-3,
1.6871e-2, 0.25409: these are exactly the parts the m <= 9 basis cannot represent); (4,0) and (5,0) survive with quarter norms 172.80 and
131.76 (no branches 4, 5 in the basis). NOT admissible. LOSS: J_abs = 1.2724e-3 (state 131: 1.2673e-11 on the same rule); a_0 = 19.2853
(free parameter; moved). Conclusion (prompt section 8, first comparison): the existing basis cannot cancel the forbidden sectors; the
constrained refit costs eight orders of magnitude in the training loss and is not in the forcing space.

### 4b. C1-N1-002-7branch-frf: seven-branch exact-cancellation candidate (branches j = 0..6)
Snapshot SH/candidate_snapshots/C1-N1-002-7branch-frf (exact coefficients candB_j6_exact.json, sha256
74f3b4cbcb3cb83289f518ce25e27a54273959dc78f637b6b9e12efb41c8669b; exact sector table; FLOAT diagnostics file). PRIMARY chart, (B0n) EXACT.
Basis: the 860 T1 generators plus new blocks (branches 1,2,3 for m = 10..10j+9; branches 4,5,6 for m = 0..10j+9), four Legendre radial
functions H_m R^(p_j-m) t^max(5-m,0) P_n(2t-1), n = 0..3, per new block: 1820 generators, angular maximum m = 69 (density harmonics to 139).
341 exact linear constraints: center; Theta_0 (10); q=1 descendants of branches 0, 1, 2 zero (60); leading moments of branches 1..6 equal to
the exact stationary potentials C_1..C_6 (270). Objective ||F||_2^2 + ||rF||_2^2 on 0.02 <= r <= 1e4 (angular Gauss 160 during the run;
the run started before the N4 numerical auditor's bandwidth finding; re-evaluation on midpoint 200 reproduces the loss to five digits), 80 steps.
EXACT sector table: (h,0) for h = 0..6, (0,1), (1,1), (2,1) all EXACT-ZERO; first surviving sector (7,0), exponent -2.5808898481,
quarter norm 4839.983 (full circle 9679.966: the invariant of every seven-branch family, A2 P32 and the N4 numerical auditor N4-003); then (3,1) at
-2.7904 (quarter 23524.8; d2 has 71294.2), (8,0) 9364.9, (4,1) 1.577e5, (0,2) at -3.4476 1.686e6, (9,0) 3.222e4. F is in Hdot^-1, L^2, N_s.
FLOAT (midpoint 200, 0.02 <= r <= 1e4, far parts beyond 1e4 from the exact sectors, qmax 6): ||F||_2 = 312.17 (far part 2.1e-3),
||rF||_2 = 634.37 (far part 34.74), J_abs on the region 480.08, sup|F| = 465.0 at (r, theta) = (0.469, 0.412) where |V| = 3.54 and
|grad rho| = 131.2; a_0 = 31.492. The inner region is badly deformed: the r^4-weighted objective does not see r < 1. Compared with
C1-A2-d2 (||F||_2 = 4.989, ||rF||_2 = 2331.6, sup|F| = 0.105): better far field (the (6,0) sector is gone), far worse mid field.
NOT a closure candidate; it shows that exact admissibility through seven branches is cheap to impose and that the objective must include
the inner region (gradient and Hessian components), which is what the running candidates do (4c).

### 4c. Running at publication time (results in numerics_v02)
- candB_j7 (eight branches j <= 7, 2140 generators, midpoint 200, same objective): optimization finished (loss 3.18e4 against 4.99e5 for
  seven branches on the same objective), exact finalization and diagnostics in progress.
- e2_j6_n4_d012_mid160_s131: seven-branch basis, objective = NORM-A2-E2 proxy 2^18(||F||^2 + (20/21)||rF||^2) + 2^14 ||grad F||^2 +
  ||omega D^2 F||^2 on 0.02 <= r <= 1e4 (||F||_H replaced by its Hardy bound; A2-THEOREM), from the min-norm feasible projection of state 131.
- x_j3_n4_L2fw_mid80_s131: FOUR-branch candidate for the L^2 framework of the T4 theory auditor T4-019 (the coordinator request 21:34Z): 1100 generators
  (860 plus branches 1,2,3 for m = 10..19, 10..29, 10..39), constraints center, Theta_0, exact leading moments of branches 1,2,3
  (all harmonics to 39, 59, 79: 90 rows), objective 2^18 ||F||^2 + 2^14 ||grad F||^2 + ||omega D^2 F||^2 (no H). Answer to the request:
  exact cancellation of (1,0), (2,0), (3,0) with all harmonics is feasible with 60 extra (m, j) blocks beyond the 860 family (one radial
  function per block suffices for the leading moment; four allow the descendants q <= 3 to vanish as well); this run will show the cost.

## 4d. Validation of the FLOAT machinery on C1-A2-d2 (own code, no code shared with analysis2 or case4)
Exact sector engine: all d2 sector norms reproduce the r5 verifier (quarter (6,0) 1540.637, (7,0) 2165.579, (3,1) 71294.22, (8,0) 7577.80).
Far part beyond 1e4 by the exact sector formula: ||rF||_{r>1e4} = 1696.23 (analysis2: 1.70e3). E_2 components by the symbolic polar
derivative layer (numerics/lib/ipm_polar.py; midpoint 160; 0.02 <= r <= 1e4): P2 = 20.5367651400 (the N3 numerics worker VALIDATED [20.53676513985447,
20.53676513985447]), G1 = 1.0291418707 (1.029141871453669), G0 = 4.9885144420 and with the exact far part (F2_far = 3.062e-3)
G0 = 4.988817 (4.988817004568025), sup|F| = 0.10525 (analysis2 0.1051). The E_2-proxy optimizer therefore measures the right quantities.

## 5. Residual table

| candidate ID | norm ID | component | value | label | audit | method and precision | reproduction command |
|---|---|---|---|---|---|---|---|
| C1-BASE-S131 | case4 J_abs | loss, training mesh excl. r<0.02 | 1.26730668564e-11 | FLOAT (LOSS) | PENDING-N4 (N4-005 gives the exact full-axis value 1.2673066866466506e-11) | own polar evaluator, float64 GPU, 944 x 96 Gauss | python3 -B numerics/optimization/run_sanity.py (first lines) |
| C1-BASE-S131 | case4 J_abs | denser rule 1888 x 192, r >= 0.02 | 1.26730668441e-11 | FLOAT (LOSS) | PENDING-N4 | same | see work log 21:08Z block |
| C1-BASE-S131 | NORM-A2-E2 | sectors (1,0)..(5,0),(0,1),(1,1) | nonzero (table section 2) | EXACT | CONFIRMED-N4 (N4-002 for E_1) | rational arithmetic | numerics/lib/ipm_exact.py |
| C1-N1-001-refit860-jabs | case4 J_abs | loss, r >= 0.02 | 1.2724e-3 | LOSS | PENDING-N4 | float64 GPU | run_candA.py Jabs 60 |
| C1-N1-001-refit860-jabs | sectors | (0,1),(1,1) | 0 | EXACT-ZERO | PENDING-N4 | rational | snapshot sector_table.json |
| C1-N1-001-refit860-jabs | sectors | (1,0),(2,0),(3,0),(4,0),(5,0) quarter norms | 2.1033e-3, 1.6871e-2, 0.25409, 172.80, 131.76 | EXACT (nonzero) | PENDING-N4 | rational | same |
| C1-N1-002-7branch-frf | sectors | (h,0) h<=6, (0,1),(1,1),(2,1) | 0 | EXACT-ZERO | PENDING-N4 | rational | snapshot sector_table.json |
| C1-N1-002-7branch-frf | sectors | (7,0) quarter / full | 4839.983 / 9679.966 | EXACT (nonzero, invariant) | matches A2 P32 and N4-003 | rational | same |
| C1-N1-002-7branch-frf | NORM-A2-E2 | G0 = ||F||_2 | 312.17 | FLOAT (midpoint 200 + exact far part) | PENDING-N4 | float64 GPU, r in [0.02,1e4], qmax 6 beyond | candidate_diag.py <json> 200 mid 1e4 |
| C1-N1-002-7branch-frf | NORM-A2-E2 | rF = ||rF||_2 (>= H) | 634.37 | FLOAT | PENDING-N4 | same | same |
| C1-N1-002-7branch-frf | pointwise | sup|F| | 465.0 at r=0.469 | FLOAT | PENDING-N4 | same | same |
| C1-A2-d2 (check) | NORM-A2-E2 | P2, G1, G0 | 20.53676514, 1.02914187, 4.988817 | FLOAT (agrees with the N3 numerics worker VALIDATED) | n/a | ipm_polar layer, midpoint 160 | optimization/d2_e2check.py |

## 6. Locations and scales dominating the residual
- State 131: J_abs mass per decade (training rule): 0.1-1: 2.53e-12, 1-10: 2.85e-12, 10-100: 2.54e-12, 100-1e4: 4.63e-12, beyond 1e4: 1.04e-13;
  the Hessian component P2^2 on r <= 1e4 is 107 of the whole-plane 634.4 (= 25.189^2): P2 of state 131 is dominated by r > 1e3 (growing sector).
- C1-N1-002: sup|F| = 465 at r = 0.47, theta = 0.41 (|V| = 3.54, |grad rho| = 131); the FLOAT octave profile is in the snapshot's
  candB_j6_n4_d012_FrF_R1e4_gauss160_diag_mid200.json. The far field beyond 1e4 contributes 2e-3 to ||F||_2 and 35 to ||rF||_2.
- C1-A2-d2: ||rF||_2 = 2331.6 of which 1696 from r > 1e4 (sector (6,0)); P2 and G1 are mid-field quantities.

## 7. Background hypotheses
Not yet screened for the new candidates (planned: the matrix conditions (B1)-(B6) on a polar grid, FLOAT, then handed to working file the N4 numerical auditor (not published) for
certification). State 131 and d2 values: see the N3 numerics worker and the N4 numerical auditor tables.

## 8. Next proposed numerical improvement and requests to batch T
1. Candidate C (in preparation): fixed exact tail with branches to j = 8..10 and ALL descendant moments q = 1..3 zeroed in every block (so
   the residual's far field is exactly the invariant sector (N+1,0) plus O(r^(gamma-8))); since every new block then has as many moment
   conditions as radial functions, the tail is one fixed potential and the unknowns are the 860 inner functions plus inner functions with
   vanishing far-field moments ((1-t)^4 P_n(2t-1) R^(p_j-m) H_m, n to about 60) for resolution to r of order 100; objective = the E_2
   proxy (gradient and Hessian components included; H by its Hardy bound, later by the exact mode-wise Green quadratic form) and, for
   T4-019, the same without the H term.
2. Request to batch T: the far-field floors of section 3 show that in NORM-A2-E2 the component H is controlled by the stationary tail
   beyond the mid field and cannot be reduced below O(1) with any finite number of branches that we can realistically optimize; in the
   L^2 framework of T4-019 the floor is smaller by the factor R^(-1)-ish shown above and eight or more branches with onset about 100
   give ||F||_{L^2(r>100)} of order 1. Please state (a) whether a forcing norm with a far-field weight decaying at least like r^(-2) (or an
   exponentially localized weight) can carry a complete theorem (this is where numerics can deliver small residuals), (b) whether Route T-E
   (first sectors as coordinates) can absorb the invariant sector (N+1,0) for some N <= 8, and (c) for T4-019, which sectors must vanish
   exactly (we read: (1,0), (2,0), (3,0) only) and whether (B0n) and the fixed Theta_0 are still the normalization.
3. Request to the N3 numerics worker: VALIDATED component table for C1-N1-002 (exact JSON and sha256 given in the snapshot).
