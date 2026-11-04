# T2_CLOSURE_CHECK_v01: the final closure check at C2-N1-013 as a conditional program (items 8 and 9 of SOURCE013_CHAIN_CONDITIONS_v01)

Written 2026-11-04 in a work session by the second theory agent, for the coordinator's notes 07:08Z item 3(a). The near part is the first theory agent's NEAR_CHECK_v01
(the first theory agent's notes 83, 84), bound by hash and recomputed here as a transcription check. This file is a conditional program
with a dry run. The dry run uses FLOAT stand-ins and cover targets in place of open certificates, and it proves
nothing. Stationary existence, O3 and row C2 stay OPEN.

## 0. Summary

1. The program research/closure_check/closure_check.py reads every input from research/closure_check/inputs_v01.json.
   Each input is a named parameter with a value, a sense (upper, lower, exact, choice), a status and a source. The
   program decides, in exact rational or outward arb arithmetic:
   - the cover premise;
   - beta_0*, betaK_* and the far route F-a inequality;
   - R_* <= Rbar;
   - (R1) in two readings;
   - the H4-R bound C0 on C^opt(b0);
   - the hypotheses H5' and M <= Mbar of Theorem B;
   - the direct test C0 R_*^2 <= M [(b0 - L_B) M - n].
   It does this for the plan of record (b0, mu) = (11/20, 72) and for the registered fallback (103/200, 68). It
   then prints the named hypotheses, a verdict and the statement that would follow. The run took 7.8 s on one core
   (2026-11-04 07:42:42Z to 07:42:50Z).
2. Verdict of the dry run: CLOSURE OPEN. The cover premise is OPEN: the both-auditor union leaves the strain gap
   57/71 < r^2 < 49/15, and the gap 15/17 < r^2 < 49/15 remains even with the roots certified without a union. Ten
   named hypotheses are OPEN. Every computed check passes only with stand-ins (PASS-COND), except the source check
   C1 and the transcription checks N1 to N3, which PASS.
3. Transcription. This program's independent evaluation of e_up and P_HF agrees with NEAR_CHECK_v01 to 1e-10 and to
   1 in absolute terms, in both cases (N2, N3 PASS). The first theory agent need not re-check the transcription, but is invited to.
4. The join (NEAR_CHECK_v01 hypothesis H4, named H4-COMP here) is not confirmed. Theorem H4-R as stated (AT-364)
   charges the near e-term to beta_* - eps_R - b0. This is also the theory auditor's reading in AT1687 ("reserves the
   nonnegative Fourier-tail losses within beta_* - eps_R - b0"). It does not charge the near e-term to
   c + 1 - q - b0, which is the reading of theory_v20 V10-4 (a) and of NEAR_CHECK_v01 (a). The two readings agree
   only at beta_* = c + 1 - q, the largest rate AT-211 allows. The program decides both readings (section 4):
   - Under reading (i), (R1) passes at the plan of record with margin >= 0.00630211 (FLOAT).
   - Under reading (ii) at the cover target beta_* = 3/5, (R1) fails, with margin <= -0.104017 (FLOAT). It would
     pass if a whole-plane beta_* >= 0.70401710 were certified.
   The theory auditor and the first theory agent are asked which implication is accepted (section 8).
5. The other remainder pieces of H4-R, T_IS, C_tr and C_vs1 to C_vs3, have no 013 bound (H4-REST). They enter as
   the stand-ins eps_rest = 0 and C_rest = 0.
6. Theorem B at the certified f and n is evaluated with the first theory agent's budget_013h CE code, unchanged. At beta_0* = 7/4 the
   allowance is D >= 1.2336979e11 at b0 = 11/20, against 1.22e11 at the stipulated inputs of AT-831. The direct test
   holds with C0/D <= 0.91822133 (FLOAT C0) at the plan of record and 0.90397785 at the fallback.

## 1. Files

All paths are relative to the second theory agent agent. Run with Python 3.12.13 and python-flint, from research/closure_check/:
`python3 -B closure_check.py > closure_check_v01.out`.

| file | role | SHA256 |
|---|---|---|
| research/closure_check/closure_check.py | the program (blocks N, A to I) | e0ffc304f7f92b8c1857e05aa9cecba3212120543399227031f623e84c11772b |
| research/closure_check/inputs_v01.json | every input, with sense, status and source | 337f237bd52c578430c566b63f27e4584c5ad138dfc02c4a6d2dfa3fae4f4af7 |
| research/closure_check/closure_check_v01.out | the dry run | 9bce4ec0333b1f8ab6a944e8cd19ad576588e95861931834eb9b70c04bdbaead |
| research/closure_check/closure_check_v01.json | the machine-readable result | cb7d2bd85ee05e2b193a255b985ab1aa14f365731b1d5a646d7b8409e4f361cc |
| research/closure_check/ps1copy/ps1/ce_gen.py | The first theory agent budget_013h/ps1/ce_gen.py, unchanged copy | 9416d497073c7cc6fe9dc00fb52f47f426632d7c0d4f3e566b20401ef472a878 |
| research/closure_check/ps1copy/hf/hfq_witness.py | The first theory agent budget_013h/hf/hfq_witness.py, unchanged copy | 6ee1b853d81c399c24e2b4fc9a593fc3e99bccc8cab213579268b8dd44405642 |
| research/closure_check/ps1copy/budget_013i.py, budget_013i.out, ERRATA.md | The first theory agent budget_013h/ files of the same names, unchanged reference copies; not imported | 28bfd5ce0dcc72d149be350c1706c3273aa2decd286502fc0ad49414c54efda8, 988cc20f78b710928d2839ad6accdb0e5274803d8eb814e05c596242f5a380c8, d43943a40b8b2675adb2281306ddb1cd700b36507184e6c98ea3478ce24446b3 |
| research/closure_check/ps1copy/r1_read_ref.py | The first theory agent research/kernel_n6/r1_read.py, unchanged reference copy; not imported | b4811848c0d1440fa4815c6f5850d65baecf2a89ecb649a505d4634f0fbe39a7 |
| research/closure_check/nearcopy/ | The first theory agent research/closure_check/ (NEAR_CHECK_v01 and its four files), unchanged copies | as the first theory agent SHA256SUMS_v01; pinned in inputs_v01.json and checked by N1 |

## 2. Inputs (inputs_v01.json)

Statuses:
- CONFIRMED: audited as cited.
- STANDIN-FLOAT: a FLOAT number in place of an open certified bound.
- STANDIN-TARGET: a cover target in place of an open whole-plane certificate.
- CHOICE: a free parameter of the construction.
A check that uses any stand-in is reported PASS-COND, never PASS.

| name | sense | value | status | source |
|---|---|---|---|---|
| q, sigma, r0 | exact | 21/10, 1, 1/2 | CONFIRMED | P-S1 |
| c | exact | 4076476460239181/2^51 | CONFIRMED | Candidate 007 reference value, unchanged |
| c_W | upper | 9619/5000 | CONFIRMED | AT-170 |
| f (\|\|F_*\|\|_2) | upper | 7.961206656880281e-7 | CONFIRMED | AT-1413 (ledger v11 rows G1, L) |
| n (N_(21/10)(F_*)) | upper | 0.0055545729030073655758 | CONFIRMED | AT-1430, AT-1431 |
| beta_0 | lower | 2.00215453 | CONFIRMED | AN-010 |
| beta_* (lambda_max H <= -beta_*) | lower | 3/5 | STANDIN-TARGET | chain item 3; regional only |
| g_* (\|grad h_*\|) | upper | 1/4 | STANDIN-TARGET | chain item 3 |
| s_* (\|\|Sym Du\|\|_op) | upper | 137/125 | STANDIN-TARGET | route F-a strain input |
| regions (cutoff 07:30Z) | | [0, 57/71] and [49/15, inf): union CONFIRMED (AN637, AT2240, AT2241); roots 57, 58, 59 on [57/71, 15/17]: CONFIRMED without a union (AT2243, AT2244; AT2252, AT2253; AT2268, AT2269) | | |
| SC^+, A_E^+, S_W^+, OMF^+ | upper | exact dyadics of T2_PART7_v07 section 2 | CONFIRMED | AT1366, AT1367; AT1891; AT1928, AT1929; AT-1336 to AT-1338, AT-1341 |
| Rbar, Mbar | exact | 17/8750000, 1/2 | CONFIRMED | Lemma KB rectangle, AT-772 |
| loss_KB | upper | 0.152070 | CONFIRMED | AT-772 (under the center matrix premise) |
| b0, mu | choice | (11/20, 72) and (103/200, 68) | CHOICE | plan of record; registered fallback |
| nu, t | choice | 1/40, 1/10 | CHOICE | NR-27; HF1-NEAR |
| Lambda_+(a_n) | upper | 20.862082 | STANDIN-FLOAT | used as max(value, 8 (2c - 1)); 8 (2c - 1) = 20.9651074 is a certified lower (AT-575) |
| \|\|(a_n)_+\|\|_1 | upper | 4.0442822 | STANDIN-FLOAT | The second theory agent 2026-11-03 11:32Z |
| D4, D5, D6 of a_n | upper | 444.194, 4186.35, 63050.4 | STANDIN-FLOAT | certified lower D6 >= 62748 (AT-1467) |
| sup(\|a_n\| W^2), sup((a_n)_+ W^2) | upper | 8.6524467, 8.5262260 | STANDIN-FLOAT | The second theory agent 2026-11-03 11:32Z |
| kappa_0, kappa_2q, kappa_j at mu 72 | upper | 3.20696761, 1059792560, 37912 | CONFIRMED | AT-1491, AT-1492 |
| kappa_0, kappa_2q, kappa_j at mu 68 | upper | 3.2126528, 836515933, 33926.469 | STANDIN-FLOAT | The first theory agent arb runs, unaudited |
| C_D | exact | 80127/40000 | CONFIRMED | AT-428 |
| K_4, K_5, K_6 | lower | exact endpoint differences | CONFIRMED | AT-1453, AT-1454 |
| eps_rest, C_rest | upper | 0, 0 | STANDIN-FLOAT | H4-REST; no 013 bound exists |
| beta_0* | lower | 7/4 | derived | beta_0 - g_* >= 7/4 needs g_* <= 1/4 (A2) |
| h4_reading | | undecided | | H4-COMP, section 4 |

Monotonicity. Each check is monotone in the direction of each parameter. A PASS-COND therefore becomes a PASS when
every stand-in is replaced by a certified bound in its direction that is at least as good as its value, and the
cover premise A1 is supplied.

## 3. The checks

Block N (binding).
- N1: the NEAR_CHECK_v01 files match the pinned hashes, and the result file names the pinned program and parameters.
- N2: the e_up upper of this program agrees with NEAR_CHECK_v01 to within 1e-10.
- N3: the P_HF upper of this program agrees with NEAR_CHECK_v01 to within 1.
The decisions below use the larger of the two uppers.

Block A (background; chain items 3 and 7; T2.7; AT-211).
- A1: the union of both auditors' regional certificates covers r^2 in [0, infinity).
- A2: beta_0 - g_* >= 7/4.
- A3: b0 <= beta_*, which is necessary (HF-NEC, AT-211) and is RC-5.
- A4: beta_* - loss_KB > 0.
- A5: beta_* <= c + 1 - q, a consistency check against AT-211.

Block B (route F-a, exact).
- B1: max(SC^+, A_E^+) + S_W^+ + OMF^+ <= q (c - s_*).
- B2: s_* <= s_max = c - (max(SC^+, A_E^+) + S_W^+ + OMF^+)/q. Here s_max >= 1.102062881091, the far slack is zero
  at equality, and any certified whole-plane strain bound up to s_max serves.
- B3: s_* < c.
- The exact margin at s_* = 137/125 is 71675071190082633/5629499534213120000, which is >= 0.0127320502923.

Blocks C and D.
- C1: f and n are certified.
- D1: R_* = f/beta_0* <= Rbar. The value is R_* <= 4.54926094679e-7 at beta_0* = 7/4.

Block E: (R1) of HF1-NEAR (AT-691) with tail B (AT-757), the quartic cut (AT-1094, AT-1134), the core split
a_n = a_c + a_r (NR-25, NR-30), the K_m (AT-1453, AT-1454) and NR-32 (AT-1512, AT-1513). The upper is

    e_up = (1 + q^2) max(Lambda_+, 8 (2c - 1))/(2 mu^2) + A4c (1024 c + M4^+(a_r))/mu^4
           + tail_B(a_c) + tail_B(a_r) + t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi)).

Its ingredients:
- A4c = pi^2 (1 + c_aw/2) + C_D/2, with c_aw = 2 q^2 (sinh(x0)/x0)^2 and x0 = (q/2) log 2.
- M4^+(a_r) = ((D4 D6 + D5^2)/(2 pi))^(1/2) at D_m(a_r) = (D_m(a_n)^2 - K_m)^(1/2).
- tail_B(a) = (4/3)^q T_q(a; 3mu/4) + (8/mu)^q T_q(a; mu/2).
- T_q(a_c; v) <= c pi^(1/2) v^(q + 3/2) e^(-v/2)/(2 (v - 2q - 1)) for v > 2q + 1.
- T_q(a_r; v) <= v^(q - 5) D6(a_r)/(4 pi (5 - q))^(1/2).

The checks of block E:
- E0: the side conditions: mu >= 1, 0 < 2 nu <= mu, 0 < t < 1, D_m(a_n)^2 > K_m, and mu/2 > 2q + 1.
- E1, reading (i): e_up + eps_rest <= c + 1 - q - b0.
- E2, reading (ii): e_up + eps_rest <= beta_* - b0.
- The program also prints the beta_* that reading (ii) needs: beta_* >= b0 + eps_rest + e_up.

Block F (Theorem H4-R, AT-364; Proposition FG, AT-513; HF1-NEAR).
- F1: C^opt(b0) <= C0 = C_rest + P_HF, with

      P_HF = 2^sigma [sup(|a_n| W^2) kappa_0 kappa_2q + (1 - t)^-1 sup((a_n)_+ W^2) (kappa_1^2 + kappa_2^2)],

  where sup(|a_n| W^2) = max(sup((a_n)_- W^2), sup((a_n)_+ W^2)) and kappa_1 = kappa_2 = kappa_j (by rotation).
- This needs H4-COMP, H4-REST and the far side B1 under FG (section 5).

Block G (Theorem B, AT-273; the CE input AT-306; the first theory agent's budget_013h code, unchanged).
- Setting: R_* = f/beta_0*, with the certified f and n, not the stipulated 7.97e-7 and 0.006 of AT-831.
- A float search over M and the pairs (B, A) is followed by a rational M = rat3(M), clamped to Mbar.
- Kbar is rational, with Kbar - M - E(R_*, Kbar) > 0 in arb, or Kbar = c_W M. L_B = loss(R_*, Kbar, B, A) is
  evaluated in arb.
- G1: Kbar is certified.
- G2: B > 1/2 and b' = b0 - L_B > 0 (H5').
- G3: 0 < M <= Mbar (E-v11-1).
- G4: the direct test of chain item 8: C0 R_*^2 <= M [(b0 - L_B) M - n], that is, C0 <= D = Z/R_*^2.
- G5 (information only, not used in the verdict): the largest b0 on a 1/100 grid at which reading (ii) holds at
  beta_*, and the direct test there.

## 4. H4-COMP: which budget the near e-term uses

The H4 of Theorem B is E(g) <= -b0 ||g||^2 + C0 ||h||^2 for all tests, with E(g) = Re<J^q L_W J^(-q) g, g> and
g = J^q W h. Its composition at 013 runs through T2_H4_v01 (Lemma 2.0, Propositions P0 and DR, Theorem H4-R; AT-364).

1. Exact decomposition. E(g) = int v^T H v + D_rem(g), with v = Rg and H = qA + K - dI. Here K is the velocity-source
   symbol and d = c + 1 + a_W. The remainder is D_rem = T_I + T_II + C_tr + C_aw + C_vs, with
   T_I <= -q (c - s_*) ||J^(-1) g||^2 + T_IS.
2. Principal part. P0 under N0 gives int v^T H v <= -beta_* ||g||^2.
3. Weight terms. The weight coefficient atil = a_W - sigma c is split into near and far parts, atil = a_n + a_f.
   - The near part (TII + C_aw)[a_n] is at most e_up ||g||^2 + P_HF ||h||^2 (HF1-NEAR).
   - The far part is charged to the free gain q (c - s_*) ||J^(-1) g||^2 (Proposition FG, AT-513, AT-624). Route F-a
     certifies this through B1.
4. The other pieces. T_IS, C_tr and C_vs1 to C_vs3 are at most eps_rest ||g||^2 + C_rest ||h||^2. Under FG, part of
   them may instead go to the far slack G - A_far (H4-REST).
5. Sum. E(g) <= -(beta_* - e_up - eps_rest) ||g||^2 + (P_HF + C_rest) ||h||^2.

So H4 at rate b0 follows from this composition when e_up + eps_rest <= beta_* - b0. That is reading (ii). It is the
slack condition of Theorem H4-R, and AT1687 reads H4-R the same way. The terms e_up ||g||^2 are full L^2 terms, not
J^(-1) terms, so the free gain cannot absorb them.

Reading (i) is e_up <= c + 1 - q - b0 together with a separate RC-5 condition beta_* >= b0. It is the reading of
theory_v20 V10-4 (a) and of the theory_v20 table row "near test of V10-4 (a): e_HF <= cap - b0, P_HF <= D(b0) ... no
background quantity enters except through D", and of NEAR_CHECK_v01 (a). In the chain above, reading (i) follows
only if P0 gives -(c + 1 - q) ||g||^2, that is, beta_* = c + 1 - q. At the origin, H(0) has the yy entry
-(c + 1 - q), because a_W(0) = 0, s(0) = c - 1 and K_yy(0) = 0. Hence beta_* <= c + 1 - q (AT-211), and reading (i)
is the most favourable case of reading (ii).

The second theory agent has not found a step that charges the near e-term to c + 1 - q - b0 independently of beta_*. The texts read
were T2_H4_v01 sections 2 and 4, the statement of HF1-NEAR, V10-4 (a) and the AT1687 proof. If such a step exists,
reading (i) stands and this section is void. The program keeps both readings and a parameter h4_reading. The
verdict needs an accepted reading.

Consequences in the dry run (FLOAT):
- Under reading (ii), the plan of record needs a certified whole-plane beta_* >= 0.70401710, which is within 0.0063
  of c + 1 - q = 0.7103192. The fallback needs beta_* >= 0.69685167. The cover certificates were run at target 3/5.
- At beta_* = 3/5, reading (ii) holds at mu 72 only for b0 <= 0.4459. The companion row b0 = 11/25 gives
  D >= 5.9354136e10 and C0/D <= 1.9085574, so the direct test fails. At mu 68 and b0 = 41/100: D >= 4.6849591e10
  and C0/D <= 1.9236532.
- A pass under reading (ii) at beta_* = 3/5 would need a case (b0, mu) not computed here, with kernel uppers at that
  mu. It would also have to satisfy b' = b0 - L_B > 0, where L_B is about 0.37 at the 013 cells. No such case is
  known to the second theory agent. A failed sufficient test excludes nothing.

## 5. Named hypotheses (block H) and items 1 to 9 of SOURCE013_CHAIN_CONDITIONS_v01

Named hypotheses. The status in parentheses is that of the dry run.
- H-B (OPEN): the whole-plane background, that is, lambda_max H <= -beta_*, |grad h_*| <= g_* and
  ||Sym Du||_op <= s_* on R^2. This is chain item 3, N0 of H4-R and RC-5. Check A1 decides it.
- H-RC (OPEN): RC-1 to RC-10 of V11-2 (a). The structural part is the exact-potential class (AT-674, AT-675). The
  quantitative part is chain items 2 and 3.
- H1 (OPEN): the actual generator, that is, a closed generator, a core, the weighted semigroup and graph comparison
  on a reference ball containing K(R_*, M). It is conditionally reduced to H-B and the source bounds (AT-600;
  Lemma KB, AT-772, AT-832).
- H2 (OPEN): the full L^2 inverse of L_* + U[k].grad with rate beta_0* on the ball (T2.7, AT-123; E-v11-2), and
  ||z||_2 <= R_*. It holds through H-B (g_* <= 1/4) and H1.
- H3 (retained): (R3/R5) of Theorem B and N(F_*) < infinity. N(F_*) <= n is CONFIRMED.
- H-BALL (OPEN): the full real S1 ball B(Rbar, Mbar) with no ell restriction, under the center matrix premise of
  Lemma KB. The rectangle and the loss are CONFIRMED (AT-772). The center matrix premise is H-B.
- H4-COMP (OPEN): section 4.
- H4-REST (OPEN): T_IS, C_tr and C_vs1 to C_vs3 of D_rem^n in NE form (T2_H4_v01 NE-lo, NE-vs).
- H-N1 (OPEN): NEAR_CHECK_v01 H1 to H3, that is, N1 for the actual a_n, the whole-plane core split and the theory auditor's
  condition 4 for the erflog cut.
- H-N3 (supplied): the kernel uppers at mu 72 (AT-1491, AT-1492). The mu 68 uppers are not audited.
- H-NEARU (OPEN): certified uppers of Lambda_+, ||(a_n)_+||_1, the two sups and D4, D5, D6 of a_n (ledger row G3).
- H-TAIL (supplied): NR-25, NR-30, the radial identity with K_m, and NR-32.
- H-FA (retained): the analytic premises of route F-a. These are AE-CS (AT-1698), Corollary CS-W and Proposition
  DW, HSB (AT-695), the source013 calculus, the tail-table certificate, the Leibniz and Faa di Bruno estimates, the
  singleton repair and the CS-W homogeneity.
- H-REG (OPEN): the premises of V11-2 (d), including delta > alpha/(2c - 2). These are not needed for V11-2 (a)
  and (b).

The items of the chain account, as this program sees them. The theory auditor is asked to state its own account in a v02.
1. Exact input and evaluator: bound for f and n through their certificates. OPEN for the near uppers and for the
   cover roots not yet in a union.
2. Whole-plane source: f and n are CONFIRMED (AT-1413, AT-1430, AT-1431). This closure (Theorem B with the CE
   input) uses only f and n.
3. Global background: OPEN (A1).
4. Near estimate: OPEN (H-N1, H-NEARU, H4-COMP, H4-REST).
5. Far estimate: route F-a is CONFIRMED conditional on H-FA, at any certified s_* <= s_max (B1, B2). Its premise s_*
   is item 3.
6. Transfer option: not used.
7. Uniform reference ball: the rectangle and loss are CONFIRMED. D1 and A4 hold given items 3 (g_*, beta_*) and the
   center premise.
8. Final closure: G4 is PASS-COND under reading (i) and fails under reading (ii) at beta_* = 3/5 (FLOAT). OPEN.
9. Regularity: section 7. V11-2 (d) is OPEN.

## 6. Dry run (closure_check_v01.out; FLOAT stand-ins and cover targets, so it proves nothing)

| quantity | (11/20, 72), plan of record | (103/200, 68), fallback |
|---|---:|---:|
| e_up, upper (equal to NEAR_CHECK_v01) | 0.1540170994 | 0.1818516608 |
| (R1) reading (i) margin | >= 0.0063021108 | >= 0.013467549 |
| (R1) reading (ii) margin at beta_* = 3/5 | <= -0.10401709 | <= -0.096851660 |
| beta_* needed for reading (ii) | <= 0.70401710 | <= 0.69685167 |
| C0 = P_HF + C_rest, upper (C_rest = 0) | 1.132807744e11 | 9.012236418e10 |
| CE cell: M, (B, A) | 387/1000, (13/25, 18959/1000) | 361/1000, (13/25, 18959/1000) |
| Kbar/M, upper | 1.004094 | 1.004232 |
| L_B(R_*, Kbar), upper | 0.3651689966 | 0.3412910741 |
| Z = M (b' M - n), lower | 0.025532334 | 0.020632720 |
| D = Z/R_*^2, lower (certified f, n) | 1.2336979e11 | 9.9695324e10 |
| D at the stipulated inputs (NEAR_CHECK_v01) | 1.22e11 (AT-831) | 9.86935e10 (unaudited) |
| C0/D, upper | 0.91822133 | 0.90397785 |
| room D - C0, lower | 1.0089018e10 | 9.5729599e9 |
| reading (ii) companion b0, D, C0/D | 11/25, 5.9354136e10, 1.9085574 | 41/100, 4.6849591e10, 1.9236532 |

Common values: the far margin of B1 is >= 0.0127320502923; s_max >= 1.102062881091; R_* <= 4.54926094679e-7.

## 7. The statement that would follow

Suppose:
- (a) every hypothesis of section 5 is supplied by an accepted certificate, and h4_reading is the accepted reading;
- (b) for one case (b0, mu), every STANDIN parameter is replaced by a certified bound in its direction that is at
  least as good as its value;
- (c) the program then prints PASS for N1 to N3, A1 to A5, B1 to B3, C1, D1, E0, F1, G1 to G4 and the (R1) check of
  that reading.

Then Theorem H4-R gives H4 of Theorem B with C0 as printed. Theorem B (AT-273) then gives the self-map of K(R_*, M)
and the conclusion of V11-2 (a) with errata E-v11-1 and E-v11-2:
- There is a stationary solution h = h_* + k of the 013 profile problem, with k real and S1.
- k lies in K(R_*, M), which is contained in B(Rbar, M). Here ||k||_2 <= R_* <= 4.54926094679e-7 <= Rbar =
  17/8750000, and ||J^(21/10)(W k)||_2 <= M <= 1/2, with M the printed cell value.
- L_* + U[k].grad has the full L^2 inverse of T2.7 with rate beta_0* >= 7/4, and the weighted estimate of V11-2 (a).
- By V11-2 (b), <X> h is in C^(1,1/10)(R^2).
Stronger Holder regularity (V11-2 (d)) stays OPEN. If the program does not print PASS for every listed check,
nothing follows. A failed sufficient test excludes neither the source nor stationary existence (chain item 8).

## 8. Requests

- To the theory auditor:
  - Review the conditional implication of sections 3, 5 and 7, behind the root, near-chunk and job 8 reviews of the
    coordinator's order.
  - State, in a v02 of SOURCE013_CHAIN_CONDITIONS, which of items 1 to 9 remain open.
  - Decide H4-COMP: is the near e-term charged to beta_* - eps_R - b0 (Theorem H4-R as stated; AT1687) or to
    c + 1 - q - b0 (V10-4 (a))?
  The new code to review is block G's use of the unchanged budget_013h CE code at the certified f and n, and the
  check logic. The near formulas are those of NEAR_CHECK_v01.
- To the first theory agent:
  - Does a step exist that charges the near e-term to c + 1 - q - b0 independently of beta_*? If not, theory_v20
    row 8 ("no background quantity enters except through D") needs the beta_* dependence of section 4.
  - The transcription check is automatic (N2, N3); no action is needed.
