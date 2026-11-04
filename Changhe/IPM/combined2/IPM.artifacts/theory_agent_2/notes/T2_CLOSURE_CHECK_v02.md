# T2_CLOSURE_CHECK_v02: the final closure check at C2-N1-013 as a conditional program (items 8 and 9 of SOURCE013_CHAIN_CONDITIONS_v01)

Written 2026-11-04 in a work session by the second theory agent, for the coordinator's notes 07:08Z item 3(a) and the first theory agent's note 87 ("please bind v02,
not v01, in the closure program, and use the printed tuple, not an internal ball"). It supersedes
T2_CLOSURE_CHECK_v01, which stays unchanged. The near part is the first theory agent's NEAR_CHECK_v02. It is bound by hash, its
printed tuple is used, and it is recomputed here as a transcription check. This file is a conditional program with
a dry run. The dry run uses FLOAT stand-ins and cover targets in place of open certificates, and it proves nothing.
Stationary existence, O3 and row C2 stay OPEN.

## 0. Changes against v01

1. Binding. The program binds NEAR_CHECK_v02 (copied unchanged into research/closure_check/nearcopy_v02/; the five
   hashes are pinned in inputs_v02.json and checked by N1). The decisions use the printed NEAR_CHECK_v02 values
   e_up and C_N_upper as exact rationals, and no internal ball (the first theory agent's note 87; NEAR_CHECK_v02 section 0 item 2).
2. Sign of the core split. v01 wrote "a_n = a_c + a_r" in the header of block E and in section 3. The correct split
   is a_n = -a_c + a_r with a_r = a_n + a_c and a_c = c/(1 + 4|x|^2) (NR-30 Remark 5; AT2298 REFUTED, AT2299
   CONFIRMED). The arithmetic of v01 already had this meaning: it subtracts K_m from D_m(a_n)^2, which AT2299
   confirms for a_r = a_n + a_c, and the triangle bounds hold for both signs. No value changes.
3. Rounding interface (after AT2307 and AT2308 REFUTED and AT2309 CONFIRMED for NEAR_CHECK_v01; the same defect is
   present in v01 of this program, erratum E-CC-v01-1 below). In v02 every value that enters a decision is an exact
   rational:
   - e_up and C_N_upper are the printed NEAR_CHECK_v02 uppers; C0 = C_rest + C_N_upper exactly;
   - D_out is a 10-digit decimal certified <= the arb ball of D = Z/R_*^2 (the program checks D_out <= D in arb);
   - the (R1) margins are exact, (cap - b0) - eps_rest - e_up and (beta_* - b0) - eps_rest - e_up, and are
     displayed rounded down; E1 and E2 pass iff the exact margin is >= 0;
   - the beta_* needed under reading (ii), b0 + eps_rest + e_up, is printed exactly and displayed rounded up;
   - G4 passes iff C0 <= D_out; the room is D_out - C0 rounded down, and C0/D_out is rounded up;
   - arb balls are used only inside the CE cell and the transcription checks.
4. Transcription checks. N2 and N3 now require that this program's independent ball lies below the printed
   NEAR_CHECK_v02 upper, in addition to the agreement to 1e-10 (e_up) and to 1 (C_N_upper).
5. Section 4 adds a HEURISTIC planning scan of reading (ii) and the 013 data on background margins.

Erratum E-CC-v01-1 (T2_CLOSURE_CHECK_v01, closure_check.py, closure_check_v01.out and .json). The displayed
tuple of v01 was not consistent as a tuple, which is the class of AT2307. Each displayed value was rounded outward
on its own, but the room was the lower endpoint of the ball D - C0, not a lower bound for the displayed D minus the
displayed C0. At the plan of record v01 displays D >= 1.2336979e11 (JSON 123369790000), C0 <= 113280774400 and
room >= 10089018000. The displayed difference is 10089015600, which is 2400 below the displayed room. At the
fallback the excess is 80. In addition, when its own ball was not wholly above the printed near upper, v01 used
max(printed, float(upper endpoint)), and float() of an arb point rounds to nearest, not upward. The decisions of v01
are not affected: every margin exceeds these effects by many orders, and v02 gives the same decisions with the same
leading digits (section 6). Use v02.

## 1. Summary

1. The program research/closure_check/closure_check_v02.py reads every input from
   research/closure_check/inputs_v02.json. Each input is a named parameter with a value, a sense (upper, lower,
   exact, choice), a status and a source. The program decides, in exact rational or outward arb arithmetic:
   - the cover premise;
   - beta_0*, betaK_* and the far route F-a inequality;
   - R_* <= Rbar;
   - (R1) in two readings;
   - the H4-R bound C0 on C^opt(b0);
   - the hypotheses H5' and M <= Mbar of Theorem B;
   - the direct test C0 R_*^2 <= M [(b0 - L_B) M - n].
   It does this for the plan of record (b0, mu) = (11/20, 72) and for the registered fallback (103/200, 68). It
   then prints the named hypotheses, a verdict and the statement that would follow. The run took 4.7 s on one core
   (2026-11-04 07:56:52Z to 07:56:57Z).
2. Verdict of the dry run: CLOSURE OPEN. The cover premise is OPEN: the both-auditor union leaves the strain gap
   57/71 < r^2 < 49/15, and the gap 15/17 < r^2 < 49/15 remains even with the roots certified without a union
   (cutoff 07:30Z, unchanged at 07:55Z). Ten named hypotheses are OPEN. Every computed check passes only with
   stand-ins (PASS-COND), except the source check C1 and the transcription checks N1 to N3, which PASS.
3. Transcription. This program's independent balls for e_up and P_HF lie below the printed NEAR_CHECK_v02 uppers
   and agree with them to 1e-10 and to 1 in absolute terms, in both cases (N2, N3 PASS).
4. The join (NEAR_CHECK_v02 hypothesis H4, named H4-COMP here) is not confirmed. Theorem H4-R as stated (AT-364)
   charges the near e-term to beta_* - eps_R - b0. This is also the theory auditor's reading in AT1687 ("reserves the
   nonnegative Fourier-tail losses within beta_* - eps_R - b0"). It does not charge the near e-term to
   c + 1 - q - b0, which is the reading of theory_v20 V10-4 (a) and of NEAR_CHECK_v02 (a) and H4. The two readings
   agree only at beta_* = c + 1 - q, the largest rate AT-211 allows. The program decides both readings (section 4):
   - Under reading (i), (R1) passes at the plan of record with exact margin >= 0.0063021108 (FLOAT inputs).
   - Under reading (ii) at the cover target beta_* = 3/5, (R1) fails, with margin <= -0.10401709 (FLOAT inputs).
     It would pass if a whole-plane beta_* >= 704017099351/10^12 (<= 0.704017100) were certified.
   - A HEURISTIC scan over (b0, mu) finds no window under reading (ii) below beta_* of about 0.6798 (section 4).
   The theory auditor and the first theory agent are asked which implication is accepted (section 8).
5. The other remainder pieces of H4-R, T_IS, C_tr and C_vs1 to C_vs3, have no 013 bound (H4-REST). They enter as
   the stand-ins eps_rest = 0 and C_rest = 0.
6. Theorem B at the certified f and n is evaluated with the first theory agent's budget_013h CE code, unchanged. At beta_0* = 7/4
   the allowance at b0 = 11/20 is D >= D_out = 123369792300, against D_lower = 1.22e11 at the stipulated inputs of
   NEAR_CHECK_v02 (AT-831). The direct test holds with C0/D_out <= 0.91822133 (FLOAT C0) at the plan of record and
   0.90397785 at the fallback.

## 2. Files

All paths are relative to the second theory agent agent. Run with Python 3.12.13 and python-flint, from research/closure_check/:
`python3 -B closure_check_v02.py > closure_check_v02.out`. The hashes of every file, including this note, are in
research/closure_check/SHA256SUMS_v02 (`sha256sum -c SHA256SUMS_v02` from research/closure_check/).

| file | role | SHA256 |
|---|---|---|
| research/closure_check/closure_check_v02.py | the program (blocks N, A to I) | 011f67dc84055321f2263c3057304fd2bfdf44ade9cd676931bd2a925a834ddc |
| research/closure_check/inputs_v02.json | every input, with sense, status and source | cf67e521da43d8d8ede76ce47eb73f2bef590f1aede6a6b7f000ef0129980da9 |
| research/closure_check/closure_check_v02.out | the dry run | 0f09d4da6f2395b4437523de7432f503a8ef874730dab88e471801be60dcdadf |
| research/closure_check/closure_check_v02.json | the machine-readable result, with the interface field | 1eeeb3ebac809733aed72de6e277baff425aca8abba1528e13521b869dbe71e2 |
| research/closure_check/nearcopy_v02/ | The first theory agent research/closure_check/ NEAR_CHECK_v02.md, SHA256SUMS_v02, near_check_v02.py, near_check_v02.out, near_check_v02.result.json and near_params_v01.json, unchanged copies | as the first theory agent SHA256SUMS_v02 (checked); near_check_v02.py 0170560ec8ff6952e2c3458c35ec0a1f7ce639ef096200a186e297f6832f298b; pinned in inputs_v02.json and checked by N1 |
| research/closure_check/ps1copy/ | The first theory agent budget_013h CE code and reference copies, unchanged, as in v01 section 1 | as T2_CLOSURE_CHECK_v01 section 1 and SHA256SUMS_v01 |
| scratch/h4comp_window_scan.py, scratch/h4comp_window_scan.out | HEURISTIC planning scan of section 4 | da633c165457d0ac8dca114d271035fb8c7b8ec27870fb101d45692bd6c685c5, f7635f23fa07b18636f6fa5da0ef977bf57bbce0225fc2fbfbca2a44d107b115 |

The v01 files (closure_check.py, inputs_v01.json, closure_check_v01.out, closure_check_v01.json, nearcopy/,
SHA256SUMS_v01) are unchanged and read-only.

## 3. Inputs and checks

Inputs. inputs_v02.json is inputs_v01.json (T2_CLOSURE_CHECK_v01 section 2) with three changes: the title version,
the regions cutoff note "2026-11-04T07:30Z (unchanged at 2026-11-04T07:55Z: no new union or root certificate)", and
the near binding (directory nearcopy_v02, result near_check_v02.result.json, program near_check_v02.py, parameters
near_params_v01.json, and the hashes of the five files). Every numerical input is unchanged. NEAR_CHECK_v02 uses
near_params_v01.json unchanged. The statuses are CONFIRMED, STANDIN-FLOAT, STANDIN-TARGET and CHOICE, as in v01. A
check that uses any stand-in is reported PASS-COND, never PASS. Each check is monotone in the direction of each
parameter, so a PASS-COND becomes a PASS when every stand-in is replaced by a certified bound in its direction that
is at least as good as its value, and the cover premise A1 is supplied.

Block N (binding).
- N1: the NEAR_CHECK_v02 files match the pinned hashes, and the result file names the pinned program and parameter
  file, both by name and by hash.
- N2: this program's e_HF ball lies below the printed NEAR_CHECK_v02 e_up, and its midpoint agrees with it to 1e-10.
- N3: this program's P_HF ball lies below the printed NEAR_CHECK_v02 C_N_upper, and agrees with it to 1.
- The decisions below use the printed values.

Blocks A to D are as in v01 section 3:
- A1: the cover;
- A2: beta_0 - g_* >= 7/4;
- A3: b0 <= beta_*;
- A4: beta_* - loss_KB > 0;
- A5: beta_* <= c + 1 - q;
- B1 to B3: route F-a, exact margin 71675071190082633/5629499534213120000 >= 0.0127320502923 at s_* = 137/125,
  and s_max >= 1.102062881091;
- C1: f and n;
- D1: R_* <= 4.54926094679e-7 <= Rbar.

Block E: (R1) of HF1-NEAR (AT-691) with tail B (AT-757), the quartic cut (AT-1094, AT-1134), the core split
a_n = -a_c + a_r, a_r = a_n + a_c (NR-25, NR-30 Remark 5, AT2299), the K_m (AT-1453, AT-1454) and NR-32 (AT-1512,
AT-1513). The upper e_up is the formula of NEAR_CHECK_v02 section 2(a), with M4^+(a_r) at
D_m(a_r) = (D_m(a_n)^2 - K_m)^(1/2). The checks:
- E0: the side conditions mu >= 1, 0 < 2 nu <= mu, 0 < t < 1, D_m(a_n)^2 > K_m and mu/2 > 2q + 1.
- E1, reading (i): (c + 1 - q - b0) - eps_rest - e_up >= 0, exact.
- E2, reading (ii): (beta_* - b0) - eps_rest - e_up >= 0, exact.
- The program prints the exact beta_* that reading (ii) needs, b0 + eps_rest + e_up.

Block F (Theorem H4-R, AT-364; Proposition FG, AT-513; HF1-NEAR).
- F1: C^opt(b0) <= C0 = C_rest + C_N_upper exactly, where C_N_upper >= P_HF and

      P_HF = 2^sigma [sup(|a_n| W^2) kappa_0 kappa_2q + (1 - t)^-1 sup((a_n)_+ W^2) (kappa_1^2 + kappa_2^2)].

- This needs H4-COMP, H4-REST and the far side B1 under FG (section 5).

Block G (Theorem B, AT-273; the CE input AT-306; the first theory agent's budget_013h code, unchanged).
- Setting: R_* = f/beta_0*, with the certified f and n, not the stipulated 7.97e-7 and 0.006 of AT-831.
- The CE cell is as in v01: M = rat3(M) clamped to Mbar, a rational Kbar certified in arb, and L_B in arb.
- G1: Kbar is certified.
- G2: B > 1/2 and b' = b0 - L_B > 0 (H5').
- G3: 0 < M <= Mbar (E-v11-1).
- G4: the direct test of chain item 8, C0 R_*^2 <= M [(b0 - L_B) M - n], decided as C0 <= D_out, with
  D_out <= D = Z/R_*^2 certified in arb.
- G5 (information only, not used in the verdict): the largest b0 on a 1/100 grid at which reading (ii) holds at
  beta_*, and the direct test there, with the same interface.

## 4. H4-COMP: which budget the near e-term uses

The H4 of Theorem B is E(g) <= -b0 ||g||^2 + C0 ||h||^2 for all tests, with E(g) = Re<J^q L_W J^(-q) g, g> and
g = J^q W h. Its composition at 013 runs through T2_H4_v01 (Lemma 2.0, Propositions P0 and DR, Theorem H4-R;
AT-364).

1. Exact decomposition. E(g) = int v^T H v + D_rem(g), with v = Rg and H = qA + K - dI. Here K is the
   velocity-source symbol and d = c + 1 + a_W. The remainder is D_rem = T_I + T_II + C_tr + C_aw + C_vs, with
   T_I <= -q (c - s_*) ||J^(-1) g||^2 + T_IS.
2. Principal part. P0 under N0 gives int v^T H v <= -beta_* ||g||^2.
3. Weight terms. The weight coefficient atil = a_W - sigma c is split into near and far parts, atil = a_n + a_f.
   - The near part (TII + C_aw)[a_n] is at most e_up ||g||^2 + P_HF ||h||^2 (HF1-NEAR).
   - The far part is charged to the free gain q (c - s_*) ||J^(-1) g||^2 (Proposition FG, AT-513, AT-624). Route
     F-a certifies this through B1.
4. The other pieces. T_IS, C_tr and C_vs1 to C_vs3 are at most eps_rest ||g||^2 + C_rest ||h||^2. Under FG, part of
   them may instead go to the far slack G - A_far (H4-REST).
5. Sum. E(g) <= -(beta_* - e_up - eps_rest) ||g||^2 + (P_HF + C_rest) ||h||^2.

So H4 at rate b0 follows from this composition when e_up + eps_rest <= beta_* - b0. That is reading (ii). It is the
slack condition of Theorem H4-R, and AT1687 reads H4-R the same way. The terms e_up ||g||^2 are full L^2 terms, not
J^(-1) terms, so the free gain cannot absorb them.

Reading (i) is e_up <= c + 1 - q - b0 together with a separate RC-5 condition beta_* >= b0. It is the reading of
theory_v20 V10-4 (a), of the theory_v20 table row "near test of V10-4 (a): e_HF <= cap - b0, P_HF <= D(b0) ... no
background quantity enters except through D", and of NEAR_CHECK_v02 (a) and H4. In the chain above, reading (i)
follows only if P0 gives -(c + 1 - q) ||g||^2, that is, beta_* = c + 1 - q. At the origin, H(0) has the yy entry
-(c + 1 - q), because a_W(0) = 0, s(0) = c - 1 and K_yy(0) = 0. Hence beta_* <= c + 1 - q (AT-211), and reading (i)
is the most favourable case of reading (ii).

The second theory agent has not found a step that charges the near e-term to c + 1 - q - b0 independently of beta_*. The texts read
were T2_H4_v01 sections 2 and 4, the statement of HF1-NEAR, V10-4 (a) and the AT1687 proof. If such a step exists,
reading (i) stands and this section is void. The program keeps both readings and a parameter h4_reading. The
verdict needs an accepted reading.

Consequences in the dry run (FLOAT inputs, exact interface):
- Under reading (ii), the plan of record needs a certified whole-plane beta_* >= 704017099351/10^12
  (<= 0.704017100), which is within 0.0063 of c + 1 - q = 0.7103192102. The fallback needs
  beta_* >= 348425830371/(5 10^11) (<= 0.696851661). The cover certificates were run at target 3/5.
- At beta_* = 3/5, reading (ii) holds at mu 72 only for b0 <= 0.4459. The companion row b0 = 11/25 gives
  D_out = 59354136770 and C0/D_out <= 1.9085574, so the direct test fails. At mu 68 and b0 = 41/100:
  D_out = 46849591720 and C0/D_out <= 1.9236532.

Planning scan (HEURISTIC, proves nothing; scratch/h4comp_window_scan.py and .out, 36.9 s). The question is whether
any (b0, mu) passes reading (ii) and the direct test at a beta_* below the plan-of-record value. The model:
- e_up(mu) is the HF1-NEAR formula of the program at the FLOAT near stand-ins (identical in inputs_v01.json and
  inputs_v02.json);
- C0(mu) = P_HF(mu) with C_rest = 0, and with each kernel upper interpolated as a power of mu through mu = 68 and
  72 (kappa_0 ~ mu^-0.0310, kappa_2q ~ mu^4.1391, kappa_j ~ mu^1.9432). Only the mu 72 uppers are audited, and the
  power law is a guess outside [68, 72];
- D(b0) is the CE cell of the program at the certified f and n and beta_0* = 7/4.
For each b0 on the 1/100 grid from 19/50 to 71/100, the scan takes the largest mu with C0(mu) <= D(b0), since e_up
decreases and C0 increases in mu, and reports beta_needed(b0) = b0 + e_up(mu). The minimum over the grid is
beta_needed = 0.67984082 at b0 = 12/25, mu = 65.837 (e_up = 0.19984082, D = 7.919221e10). That mu is outside
[68, 72], so the kernel uppers there are extrapolated. Selected rows:

| b0 | D(b0) | M | L_B | mu_max | e_up(mu_max) | beta_needed |
|---|---:|---:|---:|---:|---:|---:|
| 2/5 | 4.309343e10 | 11/40 | 0.2619 | 56.545 | 0.31275036 | 0.71275036 |
| 11/25 | 5.935414e10 | 153/500 | 0.2907 | 61.258 | 0.24687798 | 0.68687798 |
| 12/25 | 7.919221e10 | 67/200 | 0.3174 | 65.837 | 0.19984082 | 0.67984082 |
| 1/2 | 9.053310e10 | 7/20 | 0.3312 | 68.077 | 0.18125300 | 0.68125300 |
| 11/20 | 1.233698e11 | 387/1000 | 0.3652 | 73.551 | 0.14479728 | 0.69479728 |
| 3/5 | 1.631389e11 | 53/125 | 0.3991 | 78.870 | 0.11838359 | 0.71838359 |

So, in this model, reading (ii) has no window at the cover target 3/5. A window would need a certified whole-plane
beta_* of about 0.68 or more, with eps_rest = 0 and the near stand-ins as given. A failed sufficient test excludes
nothing, and the scan is not a certificate of either outcome.

013 data on the background margin (for planning; none of it is a whole-plane certificate):
- At the origin the margin is exactly c + 1 - q. The exact origin margin of a normalized background is
  c + 1 - q - max(q (2c - 2) - a_0, 0) (JOINT_CLOSURE_LEDGER, rows "BG-q origin cap" and "exact origin margin"),
  and for 013 the ledger row of C2-N1-013 records the origin cap CONFIRMED with a_* about 10.297, above
  q (2c - 2), which is about 3.403.
- The second numerics agent BANDMARGINS_013_v01 (FLOAT, "ALL FLOAT ORIENTATION, NOT BOUNDS"; the second numerics agent's team notes entry of that name)
  gives min over theta of lambda_min(M) on 63 sampled circles from r = 0.5 outward. Its smallest sampled value is
  0.789, at r = 300. It has no samples with 0 < r < 0.5.
- No certificate tests a level above 3/5: the root and union certificates of chain item 3 were run at 3/5 only.
- theory_v18 lines 6925 and 6926 already note that rows at 0.65, 0.70 and 0.7103 "need a matrix cover with a larger
  margin beta*".
These FLOAT data make a cover at about 0.68 plausible but do not certify it. Under reading (ii) the closure needs a
new cover run at that level (chain item 3), in addition to the items of section 5.

## 5. Named hypotheses (block H) and items 1 to 9 of SOURCE013_CHAIN_CONDITIONS_v01

Named hypotheses. The status in parentheses is that of the dry run. They are those of v01 section 5, with H-N1 and
H4-COMP now referring to NEAR_CHECK_v02.
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
- H4-COMP (OPEN): section 4; NEAR_CHECK_v02 H4.
- H4-REST (OPEN): T_IS, C_tr and C_vs1 to C_vs3 of D_rem^n in NE form (T2_H4_v01 NE-lo, NE-vs).
- H-N1 (OPEN): NEAR_CHECK_v02 H1 to H3, that is, N1 for the actual a_n, the whole-plane core split
  a_n = -a_c + a_r with a_r = a_n + a_c (NR-30 Remark 5, AT2299), and the theory auditor's condition 4 for the erflog cut.
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
3. Global background: OPEN (A1). Under reading (ii) the level needed is about 0.68 or more, not 3/5 (section 4).
4. Near estimate: OPEN (H-N1, H-NEARU, H4-COMP, H4-REST). The sign of the core split is settled (AT2299); the
   review of NEAR_CHECK_v02 as a whole is AT2300 OPEN.
5. Far estimate: route F-a is CONFIRMED conditional on H-FA, at any certified s_* <= s_max (B1, B2). Its premise s_*
   is item 3.
6. Transfer option: not used.
7. Uniform reference ball: the rectangle and loss are CONFIRMED. D1 and A4 hold given items 3 (g_*, beta_*) and the
   center premise.
8. Final closure: G4 is PASS-COND under reading (i) and fails under reading (ii) at beta_* = 3/5 (FLOAT). OPEN.
9. Regularity: section 7. V11-2 (d) is OPEN.

## 6. Dry run (closure_check_v02.out; FLOAT stand-ins and cover targets, so it proves nothing)

Every entry is a printed value of the exact interface of section 0 item 3.

| quantity | (11/20, 72), plan of record | (103/200, 68), fallback |
|---|---:|---:|
| e_up (printed NEAR_CHECK_v02 upper, exact) | 1.54017099351e-1 | 1.81851660742e-1 |
| (R1) reading (i) margin, exact, rounded down | >= 0.0063021108 | >= 0.013467549 |
| (R1) reading (ii) margin at beta_* = 3/5, rounded up | <= -0.10401709 | <= -0.096851660 |
| beta_* needed for reading (ii), exact | 704017099351/10^12 (<= 0.704017100) | 348425830371/(5 10^11) (<= 0.696851661) |
| C0 = C_rest + C_N_upper, exact (C_rest = 0) | 113280774322 | 450611820869/5 (= 90122364173.8) |
| CE cell: M, (B, A) | 387/1000, (13/25, 18959/1000) | 361/1000, (13/25, 18959/1000) |
| Kbar/M, upper | 1.004094 | 1.004232 |
| L_B(R_*, Kbar), upper | 0.3651689966 | 0.3412910741 |
| Z = M (b' M - n), lower | 0.025532334 | 0.020632720 |
| D_out <= D = Z/R_*^2 (certified f, n) | 123369792300 | 99695324090 |
| D_lower at the stipulated inputs (NEAR_CHECK_v02) | 1.22000000000e11 (AT-831) | 9.86935000000e10 (unaudited) |
| C0/D_out, rounded up | 0.91822133 | 0.90397785 |
| room D_out - C0, rounded down | 10089017000 | 9572959900 |
| reading (ii) companion: b0, D_out, C0/D_out | 11/25, 59354136770, 1.9085574 | 41/100, 46849591720, 1.9236532 |

The exact differences are D_out - C0 = 10089017978 and 9572959916.2, so each room is a lower bound for the
difference of the displayed pair, and each ratio is an upper bound for the quotient of the displayed pair (checked
in exact arithmetic on closure_check_v02.json). Common values: the far margin of B1 is >= 0.0127320502923;
s_max >= 1.102062881091; R_* <= 4.54926094679e-7.

## 7. The statement that would follow

Suppose:
- (a) every hypothesis of section 5 is supplied by an accepted certificate, and h4_reading is the accepted reading;
- (b) for one case (b0, mu), every STANDIN parameter is replaced by a certified bound in its direction that is at
  least as good as its value, and the near tuple is the printed tuple of a NEAR_CHECK run at those parameters;
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
  - Review v02 in place of v01: the conditional implication of sections 3, 5 and 7, the exact interface of section 0
    item 3 and erratum E-CC-v01-1, behind the root, near-chunk and job 8 reviews of the coordinator's order.
  - State, in a v02 of SOURCE013_CHAIN_CONDITIONS, which of items 1 to 9 remain open.
  - Decide H4-COMP: is the near e-term charged to beta_* - eps_R - b0 (Theorem H4-R as stated; AT1687) or to
    c + 1 - q - b0 (V10-4 (a); NEAR_CHECK_v02 H4)?
  The new code to review is block G's use of the unchanged budget_013h CE code at the certified f and n, the
  rounding helpers qdn, qup and bdn, and the check logic. The near formulas are those of NEAR_CHECK_v02.
- To the first theory agent:
  - Does a step exist that charges the near e-term to c + 1 - q - b0 independently of beta_*? If not, theory_v20
    row 8 ("no background quantity enters except through D") and NEAR_CHECK_v02 H4 need the beta_* dependence of
    section 4.
  - The transcription check is automatic (N2, N3); no action is needed.
- To the coordinator: under reading (ii), chain item 3 needs a cover at a level of about 0.68 or more (section 4), which no
  current certificate tests.
