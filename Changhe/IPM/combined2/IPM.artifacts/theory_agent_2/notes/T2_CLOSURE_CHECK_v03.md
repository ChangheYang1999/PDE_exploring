# T2_CLOSURE_CHECK_v03: the final closure check at C2-N1-013 as a conditional program (items 8 and 9 of SOURCE013_CHAIN_CONDITIONS_v01)

Written 2026-11-04 in a work session by the second theory agent, for the coordinator's notes 07:08Z item 3(a), after the theory auditor's audits of versions 01
and 02 (AT2352 to AT2357, exchange v721, 08:04:45Z; AT2367 to AT2371, v725, 08:16:37Z), the theory auditor's decision of H4-COMP
(AT2333 to AT2336, v715, 07:55:47Z) and the theory auditor's Lambda_+ audit (AT2364 to AT2366, v724, 08:16:16Z). It supersedes
T2_CLOSURE_CHECK_v02, which stays unchanged, and makes the repairs that the theory auditor requires "in a new T2 version". The
near part is the first theory agent's NEAR_CHECK_v02, bound by hash; its printed tuple is used, and it is recomputed here as a
transcription check at identical inputs. This file is a conditional program with a dry run.
The dry run uses FLOAT stand-ins and cover targets in place of open certificates, and it proves nothing.
Stationary existence, O3 and row C2 stay OPEN.

## 0. Changes against v02

the theory auditor verdicts on version 01 of this program and on H4-COMP, and what v03 does with each:

| verdict | claim (short) | v03 |
|---|---|---|
| AT2352 CONFIRMED | the arithmetic and the rational direct-test witnesses of the v01 run | kept; the v03 decisions are those of v02 |
| AT2353 CONFIRMED | the conditional implication, with the full premise list and the rate e_up + eps_rest <= beta_* - b0 | section 7 states it with that premise list |
| AT2354 REFUTED | every program row is monotone when upper inputs are improved | the claim is removed (v02 section 3 and 7(b)); replaced by the rows rule of section 3 and row N4 |
| AT2355 REFUTED | the split a_n = a_c + a_r of v01 | already repaired in v02 (a_n = -a_c + a_r); unchanged |
| AT2356 REFUTED | "G4 fails under reading (ii) at beta_* = 3/5" (v01 and v02 section 5 item 8) | item 8 rewritten; new row J1 separates E2 at the original rate from G5 at the companion |
| AT2357 OPEN | the run certifies actual source013 stationary existence | agreed; verdict CLOSURE OPEN |
| AT2333 CONFIRMED | the principal, near, far and rest estimates imply H4 when e_up + eps_rest <= beta_* - b0 | h4_reading = ii in inputs_v03.json; E2 decides |
| AT2334 REFUTED | the cap budget with beta_* >= b0 alone supplies the rate | E1 is an information row only |
| AT2335 CONFIRMED | the printed v02 near uppers need beta_* >= 0.704017099351 and 0.696851660742 | printed by E2 (exact) |
| AT2336 OPEN | the actual H4, the program and existence follow from the current records | agreed |
| AT2364 CONFIRMED | Hess a_n(0) = diag(8(2c - 1), 8), so Lambda_+(a_n) >= 8(2c - 1) = 2950576553396557/2^47 | new row T1 compares the stand-in with this lower |
| AT2365 REFUTED | the target 20.862082 can receive a same-or-better certified replacement | T1 FAILS on Lambda_plus; the value is kept for N4 (item 7) |
| AT2366 OPEN | the FLOAT value, or its maximum with the origin floor, is a global upper | agreed; H-NEARU OPEN |
| AT2367 CONFIRMED | the v02 arithmetic and the outward directions of the printed tuple | kept |
| AT2368 CONFIRMED | the conditional implication with all its hypotheses | section 7 |
| AT2369 REFUTED | v02 rows are monotone under input improvements (as AT2354) | removed (item 2) |
| AT2370 REFUTED | G4 fails under reading (ii) at unchanged b0 and mu (as AT2356) | item 4 and section 5 item 8 |
| AT2371 OPEN | the v02 dry run certifies H4, an inverse or existence | agreed; CLOSURE OPEN |
| AT2372, AT2373 CONFIRMED | M >= (704955805507/10^12) I on r^2 in [0, 17/47] and [35/93, 61/67] (roots 000 to 060 except 034) | section 4; not a whole-plane rate (AT2374 OPEN) |

1. H4 reading (AT2333 to AT2336; the first theory agent's note 88). inputs_v03.json sets h4_reading = ii. The verdict now requires E2,
   the rate budget e_up + eps_rest <= beta_* - b0. E1, the cap budget e_up + eps_rest <= c + 1 - q - b0, is printed
   as information only. AT2334 refutes it as a deduction of the rate; the theory auditor's notes that the cap budget follows only
   with a cap-level principal bound or another independently proved replacement estimate. The hypothesis H4-COMP is
   now "supplied as an implication (reading ii)". As the theory auditor says, its actual quantitative premises (the near, far
   and rest estimates) and H4-REST remain OPEN; they are the hypotheses H-N1, H-NEARU, H4-REST and H-FA.
2. Monotonicity claim removed (AT2354). v02 section 3 said that each check is monotone in each parameter, so that a
   PASS-COND becomes a PASS when every stand-in is replaced by a certified bound at least as good as its value.
   The theory auditor's counterexample: lowering D6_an from 63050.4 to 63050 lowers the near formula by more than 1e-6, but N2
   then fails against the pinned NEAR_CHECK_v02 result. v03 states the rule that does hold (section 3, rows rule):
   a certified bound at least as good as a stand-in value certifies that value, which is kept, so only a status
   changes; any changed value is a new input set that needs a same-input NEAR_CHECK and a new run.
3. Same-input row N4 (AT2354). N4 checks, exactly, that each of the 22 near inputs of this program equals the
   parameter of NEAR_CHECK_v02 (its near_params_v01.json) that N2 and N3 compare against. N2 and N3 now require N4.
   The scratch test of section 6 reproduces the theory auditor's input change: N4 then fails and names D6_an.
4. E2 versus G5 (AT2356). G4 does not contain beta_* and does not depend on the H4 reading; it is PASS-COND at the
   original rate in both cases. The new row J1 is the combined sufficient criterion at the original rate, E2 and G4
   together, and names the failing part (E2). G5 now prints its two parts, E2 at the companion and the direct test
   at the companion, and names the failing part (the direct test).
5. H-REG (the theory auditor v721: "Stronger Holder parameters, including delta>alpha/(2c-2), remain separate from the near-cut
   nu=1/40"). H-REG now lists the premises of both routes of theory_v19 V11-2 (d), and states that the Holder
   exponent nu of route R6.4 (1 < nu < 2) is not the near cut nu = 1/40 of HF1-NEAR.
6. Unchanged: every numerical input, the near binding, the CE code, the exact interface of v02 section 0 item 3, and
   every decision of v02. Erratum E-CC-v01-1 (v02 section 0) stands, with the theory auditor's precision (v725): it identifies
   an inconsistent portable printed tuple of v01; it does not refute v01's individually outward room, which AT2352
   independently supported.
7. Row T1 (AT2364 to AT2366). A new common row T1 checks that every upper stand-in with a known certified lower is
   at least that lower; otherwise no certificate can ever replace it at its value, and the conservative-witness
   rule of section 3 cannot apply. The two lowers are Lambda_+(a_n) >= 8(2c - 1) (AT-575, AT2364) and
   D_6(a_n) >= 62748 (AT1467, ledger row G3). T1 FAILS on Lambda_plus: the stand-in 20.862082 lies below the floor
   20.965107363 by exactly 226555169588423861/2199023255552000000 (AT2365). D6_an (63050.4 >= 62748) is feasible.
   The input value 20.862082 is kept, since N4 requires it to equal the NEAR_CHECK_v02 parameter. The near formula
   uses max(input, floor) = floor, as NEAR_CHECK_v02 does; that value is an upper only if the global supremum
   equals the floor, which is not proved (AT2366 OPEN). A coherent target is the first theory agent's revision of the NEAR_CHECK
   input (section 8). Because e_up already uses the floor, the target Lambda_+ <= 8(2c - 1), with a proof that the
   supremum is attained at the origin, would leave the printed tuple and every value of this run unchanged
   (only the input value and N4 would change, through a new NEAR_CHECK parameter file). A larger certified upper
   is a new input set: new NEAR_CHECK, new e_up, a new level of beta_*.
8. Scans (v725). The scans near beta_* = 0.68 (section 4) are HEURISTIC and do not establish a necessary threshold
   over all parameters. The fixed-case levels 0.704017099351 and 0.696851660742 are exact sums of printed values
   and concern only the two fixed cases and the route of this program.

## 1. Summary

1. The program research/closure_check/closure_check_v03.py reads every input from
   research/closure_check/inputs_v03.json. It decides, in exact rational or outward arb arithmetic, the same checks
   as v02 (the cover premise; beta_0*, betaK_* and route F-a; R_* <= Rbar; (R1); the H4-R bound C0; H5' and
   M <= Mbar; the direct test C0 R_*^2 <= M [(b0 - L_B) M - n]), plus N4, T1 and J1, for the plan of record
   (b0, mu) = (11/20, 72) and the registered fallback (103/200, 68). The run took 5.3 s on core 40 at nice 19
   (2026-11-04 08:18:22Z to 08:18:28Z).
2. Verdict of the dry run: CLOSURE OPEN. The cover premise is OPEN (A1: union gap 57/71 < r^2 < 49/15; cutoff
   07:30Z, unchanged at 07:55Z). Nine named hypotheses are OPEN: H-B, H-RC, H1, H2, H-BALL, H4-REST, H-N1, H-NEARU
   and H-REG. H4-COMP is no longer among them (AT2333). N1, N4, N2, N3 and C1 PASS; A1 is OPEN; T1 FAILS (the
   Lambda_+ target is infeasible, AT2365); E2, G5 and J1 FAIL in both cases; every other computed check is
   PASS-COND.
3. Under the decided reading (ii) at the cover target beta_* = 3/5:
   - at the original rate, G4 is PASS-COND (C0/D_out <= 0.91822133 at the plan of record) and E2 fails (margin
     <= -0.10401709), so J1 fails because of E2;
   - at the companion b0 = 11/25 (the largest b0 on the 1/100 grid with E2 at beta_* = 3/5), E2 holds (margin
     >= 0.0059829006) and the direct test fails (C0/D_out <= 1.9085574), so G5 fails because of the direct test;
   - the fallback is the same, with E2 margin <= -0.096851660 at the original rate, and companion 41/100 with E2
     margin >= 0.0081483392 and C0/D_out <= 1.9236532.
   A failed sufficient test excludes nothing.
4. The level needed. E2 at the original rate holds iff beta_* >= b0 + e_up + eps_rest. Here b0 + e_up is exactly
   704017099351/10^12 (<= 0.704017100) at the plan of record and 348425830371/(5 10^11) (<= 0.696851661) at the
   fallback (AT2335), and eps_rest is the stand-in 0. So the closure at these two cases needs a whole-plane matrix
   rate of about 0.70, close to the exact origin value c + 1 - q = 0.7103192102. The HEURISTIC scans (section 4)
   find about 0.68 at their best (b0, mu); they do not establish a necessary threshold over all parameters (v725).
   The only
   certified matrix lower above 3/5 is regional: 704955805507/10^12 on r^2 in [0, 17/47] and [35/93, 61/67]
   (AT2373; AT2374 OPEN). The fixed-case levels rest on the near tuple, whose Lambda_+ input needs revision (T1).

## 2. Files

All paths are relative to the second theory agent agent. Run with Python 3.12.13 and python-flint, from research/closure_check/:
`python3 -B closure_check_v03.py > closure_check_v03.out`. The hashes of every file, including this note, are in
research/closure_check/SHA256SUMS_v03 (`sha256sum -c SHA256SUMS_v03` from research/closure_check/).

| file | role |
|---|---|
| research/closure_check/closure_check_v03.py | the program (blocks N, A to D, T, E to G, J, H and I) |
| research/closure_check/inputs_v03.json | every input, with sense, status and source |
| research/closure_check/closure_check_v03.out | the dry run |
| research/closure_check/closure_check_v03.json | the machine-readable result, with the interface and rows_rule fields |
| research/closure_check/nearcopy_v02/ | The first theory agent NEAR_CHECK_v02 files, unchanged copies (as in v02); pinned in inputs_v03.json and checked by N1 |
| research/closure_check/ps1copy/ | The first theory agent budget_013h CE code and reference copies, unchanged (as in v01 and v02) |
| scratch/inputs_v03_D6test.json, scratch/cc_v03_D6test.out | the same-input test of section 6 (inputs_v03 with D6_an = 63050) |
| scratch/h4comp_window_scan.py, scratch/h4comp_window_scan.out | HEURISTIC planning scan of section 4 (as in v02) |
| scratch/patch_cc_v03.py | the patch that made closure_check_v03.py from closure_check_v02.py |

The SHA256 of each file is in SHA256SUMS_v03. The v01 and v02 files are unchanged and read-only.

## 3. Inputs, checks and the rows rule

Inputs. inputs_v03.json is inputs_v02.json with three changes: the title version; h4_reading = ii with its
citation (AT2333 to AT2336, exchange v715; the first theory agent's note 88); and the citation of Lambda_plus, which now records that
the target is infeasible (AT2364 to AT2366) and is kept for N4. Every numerical input and the near binding are
unchanged.
The statuses are CONFIRMED, STANDIN-FLOAT, STANDIN-TARGET and CHOICE. A check that uses any stand-in is reported
PASS-COND, never PASS.

Rows rule (replaces the monotonicity sentence of v02 section 3, refuted by AT2354). No row is claimed monotone under
a change of inputs.
- Transcription rows. N2 and N3 compare this program's independent balls with the printed NEAR_CHECK_v02 values.
  They mean something only at identical inputs, which N4 checks. They are kept apart from the sufficient
  inequalities E2, G4 and J1, which are decided on the printed NEAR_CHECK_v02 tuple.
- Conservative witness. Suppose a certified bound becomes available for a stand-in, and it is at least as good as
  the stand-in value: a certified upper at most the value, or a certified lower at least the value. Then the
  stand-in value is itself a certified bound in its direction. The input keeps its value and only its status
  changes, so every computed row, N2 to N4 included, is unchanged, and a PASS-COND whose stand-ins are all so
  certified is a PASS. This uses only the already checked witness; it does not use the improved number.
- New values. Any other use of a new number (a smaller upper, a larger lower, or a value on the wrong side of the
  stand-in) is a new input set. In particular a certified upper above an upper stand-in (the only kind possible
  for Lambda_plus, row T1) is a new input set. For the near inputs it needs a new NEAR_CHECK at those inputs, a
  new binding and a new run of this program; for other inputs (for example a certified beta_* above 3/5) it
  needs a new run. The rows of that run decide, not those of this run.

Block N (binding).
- N1: the NEAR_CHECK_v02 files match the pinned hashes, and the result file names the pinned program and parameter
  file, both by name and by hash.
- N4 (new): every near input here equals, exactly, the NEAR_CHECK_v02 parameter it is compared with. The 22 values
  are q, sigma, c, C_D, t, nu, D4_an, D5_an, D6_an, Lambda_plus, L1_plus (L1_pos there), sup_pos_an_W2
  (sup_pos_aW2), sup_abs_an_W2 (max of sup_neg_aW2 and sup_pos_aW2), the three K_LB - K_UB (K4, K5, K6), and
  kappa_0, kappa_2q, kappa_j for each case, matched by (b0, mu).
- N2: N4 holds, this program's e_HF ball lies below the printed e_up, and its midpoint agrees with it to 1e-10.
- N3: N4 holds, this program's P_HF ball lies below the printed C_N_upper, and agrees with it to 1.

Blocks A to D are as in v02 section 3 (A1 the cover; A2 beta_0 - g_* >= 7/4; A3 b0 <= beta_*; A4 beta_* - loss_KB > 0;
A5 beta_* <= c + 1 - q; B1 to B3 route F-a with exact margin >= 0.0127320502923 at s_* = 137/125 and
s_max >= 1.102062881091; C1 f and n; D1 R_* <= 4.54926094679e-7 <= Rbar).

Block T (new): T1, every upper stand-in with a known certified lower of the same quantity is at least that lower.
The lowers are Lambda_+(a_n) >= 8(2c - 1) (AT-575, AT2364) and D_6(a_n) >= 62748 (AT1467). T1 FAILS on
Lambda_plus with the exact gap 226555169588423861/2199023255552000000; D6_an is feasible. A FAIL of T1 means that
the conservative-witness rule cannot certify that input at its value; T1 is a common required row.

Block E: (R1) of HF1-NEAR with the formulas of NEAR_CHECK_v02 section 2(a), the core split a_n = -a_c + a_r,
a_r = a_n + a_c (NR-30 Remark 5, AT2299), as in v02.
- E0: the side conditions mu >= 1, 0 < 2 nu <= mu, 0 < t < 1, D_m(a_n)^2 > K_m and mu/2 > 2q + 1.
- E1 (information only): (c + 1 - q - b0) - eps_rest - e_up >= 0, exact.
- E2 (required): (beta_* - b0) - eps_rest - e_up >= 0, exact. The program prints b0 + eps_rest + e_up exactly.
- The Lambda term uses max(Lambda_plus, 8(2c - 1)) = 8(2c - 1), as NEAR_CHECK_v02 does; the program prints that
  this value is an upper only if the global supremum equals the floor (AT2366 OPEN).

Block F: F1, C^opt(b0) <= C0 = C_rest + C_N_upper exactly, with C_N_upper >= P_HF (Theorem H4-R, AT-364;
Proposition FG, AT-513; HF1-NEAR), as in v02.

Block G (Theorem B, AT-273; the first theory agent's budget_013h CE code, unchanged), as in v02: G1 Kbar certified; G2 H5'; G3
0 < M <= Mbar; G4 the direct test C0 <= D_out with D_out <= D = Z/R_*^2 certified in arb. G4 does not contain beta_*.
G5 (information only): at the companion b0, the largest on the 1/100 grid with E2 at beta_*, E2 and the direct test
together; v03 prints each part.

Block J (new): J1, the combined sufficient criterion at the original rate, E2 and G4 together (AT2353), with the
failing part named.

Block I: for reading (ii) the closure needs, for one case, PASS of A3, E0, N2, N3, E2, F1, G1 to G4 and J1, PASS of
the common rows N1, N4, A1, A2, A4, A5, B1 to B3, C1, D1 and T1, and every hypothesis of block H except H-REG supplied
(or retained, for H3 and H-FA).

## 4. H4-COMP (decided) and the level of beta_* it needs

The composition (T2_H4_v01, Theorem H4-R; AT-364), as confirmed by AT2333: the principal part gives
-beta_* ||g||^2 under N0; the far form is absorbed by the free gain q (c - s_*) ||J^(-1) g||^2 (Proposition FG,
route F-a); the near form gives e_up ||g||^2 + P_HF ||h||^2 (HF1-NEAR); the other pieces give
eps_rest ||g||^2 + C_rest ||h||^2. So

    E(g) <= -(beta_* - e_up - eps_rest) ||g||^2 + (P_HF + C_rest) ||h||^2,

and H4 at rate b0 follows when e_up + eps_rest <= beta_* - b0. The near and rest terms are full L^2 terms; a fixed
J^(-1) gain cannot absorb them (the theory auditor v715). The cap budget c + 1 - q - b0 is this condition at beta_* = c + 1 - q,
the largest rate AT-211 allows; it follows only with a cap-level principal bound (AT2334). The first theory agent withdraws it as a
general reading (note 88 item 1). NEAR_CHECK_v02 needs no new version: its section 6 conclusion is the near-form
inequality, and the join needs beta_* >= b0 + e_up + eps_rest (note 88 item 2).

Levels (FLOAT near inputs; eps_rest = 0 stand-in):
- At the fixed cases: beta_* >= 0.704017099351 + eps_rest at (11/20, 72) and >= 0.696851660742 + eps_rest at
  (103/200, 68) (exact sums of printed values; AT2335 CONFIRMED).
- The second theory agent HEURISTIC scan (scratch/h4comp_window_scan.py, model in v02 section 4; kernel uppers interpolated as powers
  of mu through mu 68 and 72): the smallest beta_* needed over b0 on the 1/100 grid from 19/50 to 71/100, with mu
  the largest such that C0(mu) <= D(b0), is 0.67984082 at b0 = 12/25, mu = 65.837 (outside [68, 72], so the kernel
  uppers there are extrapolated). Selected rows: b0 2/5 needs 0.71275036; 11/25 needs 0.68687798; 1/2 needs
  0.68125300; 11/20 needs 0.69479728; 3/5 needs 0.71838359.
- The first theory agent HEURISTIC scan (note 88 item 3): the smallest near P/D is 1.834 at beta 3/5, 1.249 at 0.65, 1.008 at 0.68,
  0.881 at 0.70 and 0.858 at 0.704.
The two models agree that, within their parameter sets and at the FLOAT near inputs, the near price fits in D only
at a whole-plane matrix rate of about 0.68 or more, before any far or remainder charge, and 0.704 at the plan of
record. The scans are HEURISTIC and do not establish a necessary threshold over all parameters (v725); they are not
certificates of either outcome. They also use the near formula with the Lambda floor, so they inherit row T1.

013 data on the background margin (planning only; none is a whole-plane certificate):
- At the origin the margin is exactly c + 1 - q = 0.7103192102 (JOINT_CLOSURE_LEDGER rows "BG-q origin cap" and
  "exact origin margin"; the C2-N1-013 row records the origin cap CONFIRMED, a_* about 10.297 > q (2c - 2), about
  3.403).
- The second numerics agent BANDMARGINS_013_v01 (FLOAT, "ALL FLOAT ORIENTATION, NOT BOUNDS"): smallest sampled min over theta of
  lambda_min(M) on r >= 0.5 is 0.789, at r = 300; there are no samples with 0 < r < 0.5. The second theory agent asked the second numerics agent for a
  FLOAT sample of 0 < r < 0.5 (notes 08:05Z).
- The root and union certificates of chain item 3 were run at 3/5. The numerical auditor's exact recount of the admitted interval
  records (no new source evaluation) gives M >= (704955805507/10^12) I on r^2 in [0, 17/47] and [35/93, 61/67],
  roots 000 to 060 except 034, minimum at root 000 (AT2372, AT2373 CONFIRMED). This is regional, not a whole-plane
  rate (AT2374 OPEN): root 034, the ordinary roots 061 to 097, the balanced and capped slab roots and the exterior
  have no recount at the stronger level. On that region the lower exceeds the fixed-case levels by exactly
  0.000938706156 at the plan of record and 0.008104144765 at the fallback, before eps_rest (the first theory agent's note 89; AT2374:
  "regional and relative to a stipulated near diagnostic"). At the origin the exact margin exceeds the plan of
  record level by c + 1 - q - 0.704017099351 >= 0.0063021108 (the E1 margin).

## 5. Named hypotheses (block H) and items 1 to 9 of SOURCE013_CHAIN_CONDITIONS_v01

Named hypotheses, with the dry-run status. They are those of v02 section 5, with two changes.
- H-B (OPEN): lambda_max H <= -beta_*, |grad h_*| <= g_* and ||Sym Du||_op <= s_* on R^2 (chain item 3; N0 of
  H4-R; RC-5). Check A1 decides it. Under reading (ii) beta_* must be about 0.70 at the fixed cases (section 4);
  the stronger lower 0.704955805507 is CONFIRMED only on a region (AT2373, AT2374 OPEN).
- H-RC (OPEN): RC-1 to RC-10 of V11-2 (a) (structural: AT-674, AT-675; quantitative: chain items 2, 3).
- H1 (OPEN): closed generator, core, weighted semigroup and graph comparison on a reference ball containing
  K(R_*, M); conditionally reduced to H-B and the source bounds (AT-600; Lemma KB, AT-772, AT-832).
- H2 (OPEN): the full L^2 inverse of L_* + U[k].grad with rate beta_0* on the ball (T2.7, AT-123; E-v11-2) and
  ||z||_2 <= R_*, through H-B (g_* <= 1/4) and H1.
- H3 (retained): (R3/R5) of Theorem B and N(F_*) < infinity; N(F_*) <= n CONFIRMED.
- H-BALL (OPEN): the full real S1 ball B(Rbar, Mbar), no ell restriction, under the center matrix premise of Lemma
  KB; rectangle and loss CONFIRMED (AT-772); the center premise is H-B.
- H4-COMP (supplied as an implication, reading ii; changed): AT2333. Its quantitative premises are H-N1, H-NEARU,
  H4-REST and H-FA, and its rate condition is E2.
- H4-REST (OPEN): T_IS, C_tr and C_vs1 to C_vs3 of D_rem^n in NE form (T2_H4_v01 NE-lo, NE-vs).
- H-N1 (OPEN): NEAR_CHECK_v02 H1 to H3 (N1 for the actual a_n, the whole-plane core split a_n = -a_c + a_r,
  the theory auditor's condition 4 for the erflog cut).
- H-N3 (supplied): the kernel uppers at mu 72 (AT-1491, AT-1492); the mu 68 uppers are not audited.
- H-NEARU (OPEN; changed): certified uppers of Lambda_+, ||(a_n)_+||_1, the two sups and D4, D5, D6 of a_n
  (ledger row G3). The Lambda_+ target 20.862082 cannot be certified: it lies below the origin value 8(2c - 1)
  (AT2364, AT2365; row T1). What is needed is a certified global upper at least 8(2c - 1), or a proof that the
  supremum equals it (AT2366 OPEN), with the near loss and the beta_* level recomputed where they change.
- H-TAIL (supplied): NR-25, NR-30, the radial identity with K_m, NR-32.
- H-FA (retained): the analytic premises of route F-a (AE-CS, AT-1698; Corollary CS-W and Proposition DW; HSB,
  AT-695; the source013 calculus; the tail-table certificate; the Leibniz and Faa di Bruno estimates; the singleton
  repair; the CS-W homogeneity).
- H-REG (OPEN; changed): V11-2 (d), stronger Holder regularity, with its own premises (theory_v19 V11-2 (d)): route
  T1.3 (a heavier weight sigma_9 > sigma with all hypotheses of R9.4 at sigma_9, including a finite-radius margin
  mu_R > 0 not evaluated for 013) or route R6.4 (alpha/(2c - 2) < delta < 1 and 1 < nu < 2; at alpha = 1/10,
  delta > 0.0617041). The Holder exponent nu of R6.4 is not the near cut nu = 1/40 of HF1-NEAR, and none of these
  premises is needed for V11-2 (a) or (b).

The items of the chain account, as this program sees them:
1. Exact input and evaluator: OPEN for the near uppers and for the cover roots not yet in a union.
2. Whole-plane source: f and n CONFIRMED (AT-1413, AT-1430, AT-1431). Theorem B with the CE input uses only f, n.
3. Global background: OPEN (A1). Under reading (ii) the level needed is about 0.70 at the fixed cases, not 3/5
   (the HEURISTIC scans give about 0.68 at best and establish no necessary threshold; section 4). The lower
   0.704955805507 is CONFIRMED on a region only (AT2373).
4. Near estimate: OPEN (H-N1, H-NEARU, H4-REST); the reading of the join is decided (AT2333); the Lambda_+ target
   needs revision (T1).
5. Far estimate: route F-a CONFIRMED conditional on H-FA, at any certified s_* <= s_max (B1, B2).
6. Transfer option: not used.
7. Uniform reference ball: rectangle and loss CONFIRMED; D1 and A4 hold given item 3 and the center premise.
8. Final closure (changed after AT2356): at the original rate the direct test G4 is PASS-COND in both cases; it
   does not contain beta_* and does not depend on the reading. What fails is E2 at the original rate, so the
   combined criterion J1 fails, and the direct test at the lower-rate companion, so G5 fails. OPEN.
9. Regularity: section 7; V11-2 (d) OPEN (H-REG).

## 6. Dry run (closure_check_v03.out; FLOAT stand-ins and cover targets, so it proves nothing)

Every entry is a printed value of the exact interface (v02 section 0 item 3). The values are those of v02; the rows
N4, T1, J1 and the companion E2 margins are new.

| quantity | (11/20, 72), plan of record | (103/200, 68), fallback |
|---|---:|---:|
| N4 (same inputs, 22 values; common row) | PASS | PASS |
| T1 (stand-in not below a certified lower; common row) | FAIL (Lambda_plus) | FAIL (Lambda_plus) |
| N2, N3 (transcription at the N4 inputs) | PASS, PASS | PASS, PASS |
| e_up (printed NEAR_CHECK_v02 upper, exact) | 1.54017099351e-1 | 1.81851660742e-1 |
| E1 margin (information only), rounded down | >= 0.0063021108 | >= 0.013467549 |
| E2 margin at beta_* = 3/5, rounded up | <= -0.10401709 (FAIL) | <= -0.096851660 (FAIL) |
| beta_* needed for E2, exact | 704017099351/10^12 (<= 0.704017100) | 348425830371/(5 10^11) (<= 0.696851661) |
| C0 = C_rest + C_N_upper, exact (C_rest = 0) | 113280774322 | 450611820869/5 |
| CE cell: M, (B, A) | 387/1000, (13/25, 18959/1000) | 361/1000, (13/25, 18959/1000) |
| D_out <= D = Z/R_*^2 (certified f, n) | 123369792300 | 99695324090 |
| G4: C0/D_out rounded up; room rounded down | 0.91822133; 10089017000 (PASS-COND) | 0.90397785; 9572959900 (PASS-COND) |
| J1 (E2 and G4 at the original rate) | FAIL, because of E2 | FAIL, because of E2 |
| companion b0 | 11/25 | 41/100 |
| companion E2 margin, rounded down | >= 0.0059829006 (holds) | >= 0.0081483392 (holds) |
| companion D_out; C0/D_out rounded up | 59354136770; 1.9085574 (fails) | 46849591720; 1.9236532 (fails) |
| G5 (information only) | FAIL, because of the direct test | FAIL, because of the direct test |

Common values: far margin of B1 >= 0.0127320502923; s_max >= 1.102062881091; R_* <= 4.54926094679e-7.

Same-input test (scratch/inputs_v03_D6test.json, scratch/cc_v03_D6test.out; 08:18:36Z to 08:18:41Z, core 40, with
the final program). The
inputs are inputs_v03.json with D6_an = 63050, the input change of AT2354, which is not a certified upper. Result:
N4 FAIL ("differ: D6_an"); N2 FAIL in both cases (this program's e_up becomes 0.154015483030 and 0.181849747734,
below the pinned printed values); N3 FAIL in both cases (because N4 fails; P_HF does not use D6); T1 FAIL as in
the dry run (63050 >= 62748, so D6_an stays feasible); every row outside block N, and every printed E, G and J
value, identical to the dry run, since they use the printed tuple; verdict CLOSURE OPEN. So a changed near input is
flagged as a stale binding by N4, and it cannot reach a PASS verdict through the old tuple. The program's own
closure_check_v03.json was restored byte for byte after this test (the test writes the same file name).

## 7. The statement that would follow

This is the conditional implication of AT2353, as this program checks it. Suppose:
- (a) every hypothesis of section 5 except H-REG is supplied by an accepted certificate (the whole-plane background
  H-B with RC-1 to RC-10; the generator, core and semigroup on B(Rbar, Mbar); the full L^2 inverse T2.7; R3/R5 and
  compactness; Lemma KB with its center premise; the near premises of NEAR_CHECK_v02; the far estimate with H-FA;
  the rest forms H4-REST);
- (b) for one case (b0, mu), every stand-in of the rows it uses is certified by the conservative-witness rule of
  section 3 (a certified bound at least as good as the stand-in value, which is kept), or the case is rerun with
  new values, with a NEAR_CHECK at those near inputs and its printed tuple bound by N1 and N4;
- (c) that run prints PASS for N1, N4, A1, A2, A4, A5, B1 to B3, C1, D1, T1 and, for the case, A3, E0, N2, N3, E2, F1,
  G1 to G4 and J1 (so e_up + eps_rest <= beta_* - b0, C0 = C_rest + C_N_upper and b' > 0 hold with the CE witness).
Then Theorem H4-R gives H4 of Theorem B with C0 as printed, and Theorem B (AT-273) gives the self-map of K(R_*, M)
and the conclusion of V11-2 (a) with errata E-v11-1 and E-v11-2:
- There is a stationary solution h = h_* + k of the 013 profile problem, with k real and S1.
- k lies in K(R_*, M), which is contained in B(Rbar, M): ||k||_2 <= R_* <= 4.54926094679e-7 <= Rbar = 17/8750000,
  and ||J^(21/10)(W k)||_2 <= M <= 1/2, with M the printed cell value.
- L_* + U[k].grad has the full L^2 inverse of T2.7 with rate beta_0* >= 7/4, and the weighted estimate of V11-2 (a).
- By V11-2 (b), <X> h is in C^(1,1/10)(R^2).
Stronger Holder regularity (V11-2 (d)) stays OPEN, with the premises of H-REG. If the run does not print PASS for
every listed check, nothing follows. A failed sufficient test excludes neither the source nor stationary existence.

## 8. Requests

- To the theory auditor: review v03 in place of v02 against your repairs of v721 (section 0): the rows rule and N4 of section 3,
  J1 and the item 8 text, the H-REG text, h4_reading = ii, and row T1 for AT2364 to AT2366. The new code is N4
  (the name mapping), T1, J1, the G5 value line and the block I list; everything else is v02 code (patch
  scratch/patch_cc_v03.py).
- To the first theory agent: a coherent Lambda_+ target for the next NEAR_CHECK parameter file (AT2364 to AT2366; row T1). The
  target Lambda_+ <= 8(2c - 1) with a proof that the supremum is attained at the origin keeps every printed value;
  a larger certified upper changes e_up and the beta_* level, and then this program is rerun on the new binding.
  The binding of NEAR_CHECK_v02 is otherwise unchanged (N4 PASS). For the Part VII entry, v03 uses reading (ii)
  and states the beta_* level of section 4.
- To the coordinator: at the two fixed cases the final closure along this route needs a whole-plane matrix rate of about
  0.704 at the plan of record and 0.697 at the fallback, plus eps_rest, not 3/5. The regional lower
  0.704955805507 (AT2373) is the first step; the remaining regions need the same level.
