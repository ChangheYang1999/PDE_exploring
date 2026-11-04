# Stationary IPM existence around Candidate 007: final report of the coordinated campaign (48-hour budget)

**Status: final. A complete fixed-parameter existence theorem was NOT reached.** The strongest result is a conditional
existence theorem at the corrected center 013, confirmed as a conditional assembly by the independent theory
auditor; its first unresolved condition is O3, the closure inequality of the invariant ball, and its nearest quantitative
obstruction is the H4 rest term (H4-REST). No sharp constant and no definitive closure ratio is claimed.

## Summary

- **Verdict.** No center, corrected or not, has a certified invariant ball. All closure numbers below are conditional
  calculations at certified inputs with the uncertified hypotheses kept, or FLOAT readings.
- **Fixed data.** c = c_l = 4076476460239181/2251799813685248 (about 1.810319210200), not varied; Candidate 007 unchanged.
  Center 013: h_* = -Delta phi with phi an exact odd-potential correction of 007 (A + 3B = 0, ell(h_*) = 0 exactly).
  Tuple P-S1: q = 21/10, sigma = 1, r0 = 1/2, W(X) = (1 + 4|X|^2)^(1/2), N(G) = ||J^(21/10)(W G)||_2, J = (1 - Delta)^(1/2).
- **Proved (theory auditor CONFIRMED, under the stated hypotheses).**
  (1) O1, k = 0 lifting for the full variable-coefficient operator (NR-1): under (B-L2) with beta_0 > 0 and a BG-q cover
  N_q <= -beta on R^2 (2 < q < 3), the L2 solution of L h0 = -F obeys ||<D>^q(W h0)|| <= ||<D>^q(W F)||/beta_1 + C_1 ||F||
  for 0 < beta_1 < min(beta, beta_0), and <X>^sigma h0 is in C^(1,alpha), 0 < alpha <= q - 2; C_1 is finite, not computed.
  Applied to 007 at four certified tuples and conditionally to 013 (NR-31: L2 inverse norm below 0.570726,
  <X> k0 in C^(1,1/10)), retaining the generator, semigroup, common-domain and decay premises of section A, row 13.
  (2) O2 for 007 only on restricted balls N(k) <= 3/(20 D) with gap >= 3/20 (D symbolic; not a self-map theorem).
  (3) Theorem V11-2 (a) at 013 (every hypothesis listed in section A): with its certified inputs in place, if H-RC,
  H-N1, H-FA, H4-REST, H1, H2, H-BALL and the closure inequality C0 R_*^2 <= M[(b0 - L_B) M - n] with b0 - L_B > 0,
  0 < M <= 1/2 and a strict graph witness hold, a stationary solution h = h_* + k exists, k real and S1, ||k||_2 <=
  17/8750000, N(k) <= M, and <X> h is in C^(1,1/10).
  (4) Ceilings: NR-6 (for unchanged 007 the coarse criterion needs N(F) < N_*(21/10) <= 1.097831), NR-7, NR-3 item 6.
- **Certified numbers (both auditors).** ||F||_2 at 007 is approximately 0.3766893247. At 013: ||F_*||_2 in [7.959400186993612e-7,
  7.961206656880281e-7] (about 4.7e5 times smaller) and N(F_*) in [0.0035510975483434412497, 0.0055545729030073655758].
  At 009: ||F||_2 in [2.818778457305e-6, 2.818982922317e-6]. Whole-plane background at 013 (under the admitted complete-source
  containment and balanced-root hypotheses): matrix rate >= 704955805507/10^12, |grad h_*| <= 1/4, ||Sym Du_*||_op <= 137/125; far strain margin
  q(c - 137/125) - A_far = 71675071190082633/5629499534213120000 (about 0.012732, under the retained far premises).
  Near coefficient (under the admitted Schwartz-decay, Plancherel and retained regional hypotheses): D4 < 444.1942,
  D5 < 4186.3521, D6 < 63050.3928; from them e_up = 152627111489/10^12 at the plan of record (conditional arithmetic,
  under H-N1). Conditional closure arithmetic gives R_* <= 4.54926094679e-7 < 17/8750000. The numerical auditor
  certified strict lower bounds of the Hoelder quantity S_F for 007 (for example 112.785157863859 at (alpha, delta,
  sigma) = (1/2, 2/5, 7/4)); no certified upper of S_F exists for any center.
- **Best states.** Accepted center 013 (certified above); earlier alternative 009 (certified, larger
  residual) and FLOAT research states down to 3.4755e-7 (b28s), not certified and used by no theorem.
- **Exact remaining gap.** The first missing inequality is the H4 step e_up + eps_rest <= beta_* - b0 with
  C0 >= P + C_rest: no piece of eps_rest or C_rest has a certified bound. Needed: eps_rest <= 1164347009/(5*10^11)
  (about 2.328694018e-3) and C_rest <= 9941475955 at (b0, mu) = (11/20, 72), or eps_rest <= 1970913581/(2*10^11) and
  C_rest <= 47277952671/5 at (103/200, 68) with audited mu 68 kernels. Also open: H-N1, H-RC, H1 (actual generator),
  H2 (uniform small-k inverse at 013), H-BALL, and the retained far premises H-FA; then O3 with certified C0.
- **Where the prompt's questions are answered.** What the theory team proved: section 1. What the numerical team
  improved: section 2. Communication: section 3. Parameter optimization: section 4. Closure: section 5 (no). Smallest
  gap: section B. Next work: section 6. Every requirement of the strongest theorem with its status: section A.

## Run record

- T0 (logged start) 2026-11-02T18:05:30Z. The team was stopped at 2026-11-04T17:05:30Z, 47 hours into the 48-hour
  budget, so that this write-up finishes inside the budget. This report was finalized at T_end = 2026-11-04T17:27:49Z, an elapsed
  time of about 47 hours 22 minutes from T0.
- Agents, working concurrently for the whole run: a coordinator, two theory agents and two numerics agents, and two independent auditors from a second model family, one for theory and one for numerics. Each agent worked in
  restartable sessions of at most six hours and kept its state in files. The coordinator also used an external referee
  (a second model) on its drafts; its answers were treated as claims and checked.
- Review of this text. Both auditors reviewed and CONFIRMED the installed final report, the final ledger (version 14)
  and the bundle of the five required reports before the team stop (theory audit AT2968 to AT2970 and AT2975 to
  AT2977; numerical audit exchanges v962, v964 and v967 to v969). After the stop, the coordinator added this status line, the summary and this run record,
  condensed the verification history and the process sections, and replaced internal agent, file and path names with
  descriptions of the accompanying artifacts. No mathematical statement, number, status or hypothesis was
  changed; these final edits were not re-audited.

Labels. PROVED and CONFIRMED are used only with an entry of the theory auditor (AT-n) or of the numerical auditor
(AN-n, or a numerical audit exchange vNNN); both ledgers are in the accompanying artifacts. "Certified by both auditors"
means an executed result of the numerical auditor that the theory auditor confirmed in a distinct review and that the
numerical auditor adopted. "Conditional" means under the hypotheses named with the statement. FLOAT is a floating-point
value without an enclosure, HEURISTIC a planning reading, OPEN a statement without a settling verdict, and REFUTED a
statement that an auditor showed to be false as stated. Times are UTC, read from the clock, cited to the second.
Hash values quoted below identify the archived source versions reviewed by the auditors; the accompanying artifacts
include publication copies, with their current checksums listed separately.

## Verdict

**A complete fixed-parameter existence theorem is not certified.** No completion declaration was made.

- First unresolved condition: O3, the closure inequality of the invariant ball. No center, corrected or not, has a
  certified invariant ball, and no definitive closure ratio was computed. The closure numbers in this report are
  conditional calculations at certified inputs with the uncertified hypotheses retained, or FLOAT and HEURISTIC
  readings.
- The strongest statement proved is the conditional theorem V11-2 (a) at the chain center 013 (section A), an
  assembly of accepted implications CONFIRMED by the theory auditor (AT-978, AT-979). At 013 its source-norm hypotheses and the
  numerical background bounds of H-B are certified by both auditors (the strain condition of H-B holds numerically
  with the far upper A_far of row 7, with exact margin 71675071190082633/5629499534213120000, under the retained
  analytic far premises, AT2653), and so are the whole-plane derivative norms of the near coefficient; the near upper
  computed from them at the plan of record is CONFIRMED as conditional arithmetic by both auditors, under the
  retained analytic hypothesis H-N1. The far upper, the rest term of the H4 step, H-N1, the actual-generator,
  uniform-inverse and ball premises, and the closure inequality are not certified.
- O1, the k = 0 regularity lifting, is proved as a conditional theorem for the full variable-coefficient operator
  (NR-1, AT-031). It is applied with certified covers to Candidate 007 at four tuples (AT-056, AT-074, AT-097,
  AT-172), and at 013 with the certified whole-plane background under its retained analytic hypotheses (NR-31;
  AT-1483, AT-1484, AT-2541, AT-2599). O2 is proved for 007 on restricted balls of symbolic size only; the uniform
  small-k inverse at 013 is OPEN.
- The residual ||F||_2 fell from 0.3766893247 at Candidate 007 (certified) to the certified interval [7.959400e-7,
  7.961207e-7] at the chain center 013, a factor of about 4.7e5, and to 3.4755e-7 FLOAT at the best research state
  b28s, which is not certified.

## A. The strongest theorem and the status of each requirement

Setting. c = c_l = 4076476460239181/2251799813685248 = 1.81031921019999808564..., the binary64 number of the
Candidate 007 file (the prompt gives c_l about 1.81031921); c_l is not varied. Candidate 007 is the unchanged
background (rho_bar, u_bar) with residual F. The chain center 013 (coordinator decision 2026-11-03T11:25Z;
frozen) has h_* = -Delta phi, with phi the exact odd-potential correction b18s2 of 007, rho_* = rho_bar + h_*, u_* =
u_bar + U[h_*] and F_* = F + L h_* + U[h_*].grad h_*. The tuple is P-S1: q = 21/10, sigma = 1, r0 = 1/2, W(X) =
(1 + 4|X|^2)^(1/2), and N(G) = ||J^(21/10)(W G)||_2 with J = (1 - Delta)^(1/2). The ball is the full real S1 ball
B(Rbar, Mbar) = {k real, even in x, odd in y : ||k||_2 <= Rbar, N(k) <= Mbar}, with Rbar = 17/8750000 and Mbar = 1/2.

Theorem V11-2 (theory exchange version 11, carried unchanged to theory exchange version 24, AT2879, theory audit exchange v887; route Q with the CE variant; with the
errata E-v11-1, 0 < M <= Mbar, and E-v11-2, the full fixed-k operator, and the erratum E-v24-1 of theory exchange version 25 for item
4, the two losses; CONFIRMED as a conditional assembly, AT-978, AT-979, with 0 < M <= 1/2 required by AT-980; AT-978
holds in the scope of its standalone proof, which keeps the nonlinear loss of item 4, AT2917). (a) Assume:

1. RC-1 to RC-10 of the re-centered framework (AT-123) for h_*;
2. certified bounds ||F_*||_2 <= f and N(F_*) <= n, and a certified cover with N_q* <= -beta_* I on R^2,
   beta_* >= 3/5, g_* <= 1/4 and s_* <= c - A_far/q, where A_far is a certified far upper of the far route used;
3. a certified near upper (Proposition HF1-NEAR) and the far upper A_far, combined in the frozen H4 estimate;
4. R_* = f/beta_0* <= Rbar = 17/8750000 and Mbar = 1/2; the reference-ball condition betaK_* >= beta_* - ell_KB > 0,
   where ell_KB < 0.152070 is the matrix loss of Lemma KB on that rectangle (AT-598, AT-832); and, separately, the
   self-map inequality C0 R_*^2 <= M[(b0 - L_B(R_*, Kbar; B_CE, A_CE)) M - n] for some 0 < M <= Mbar, with
   b0 - L_B(R_*, Kbar; B_CE, A_CE) > 0, n >= N(F_*) and Kbar a strict root witness of Corollary CE-B, an admitted
   graph witness Kbar > M + E(R_*, Kbar) (Corollary HF-Q-CE, AT-273), every full-generator, inverse, source and H4
   premise retained (the wording of erratum E-v24-1, CONFIRMED by AT2930 and numerical audit exchange v943); b0 is the rate of the
   closure test. Here A_far is the far-field upper, (B_CE, A_CE) is an admitted CE pair, and the independent cutoffs
   T_S and T_V of Lemma KB, in q S(T_S) + V(T_V), satisfy T_S, T_V > 8q; for the current CE pair (B_CE, A_CE) =
   (13/25, 18959/1000), A_far < 3/2 < A_CE and B_CE < 8q = 84/5 (AT2938).

Then the profile problem has a stationary solution h = h_* + k, rho = rho_bar + h, with k real and S1, ||k||_2 <=
Rbar and ||J^(21/10)(W k)||_2 <= M <= 1/2, and L_* + U[k].grad has the full L2 inverse with rate beta_0*. (b) With no
further premise, <X> h is in C^(1,1/10)(R^2); alpha = q - 2 = 1/10 is the Sobolev endpoint at q = 21/10. (c) The k =
0 statement at 013 is NR-31 (row 13 below). (d) A stronger Hoelder lifting is OPEN: the frozen route R6.4 needs
alpha/(2c - 2) < delta < 1 and 1 < nu < 2 (at alpha = 1/10, delta above 562949953421312/9123383232769665, about
0.0617041), and the heavier-weight route needs a finite-radius margin mu_R > 0, which is not evaluated for 013.

The two losses of item 4 are distinct. L_B is the nonlinear loss of the HF-Q/CE-B energy argument; its core term
alone gives L_B > (9/20) Kbar > (9/20) M, a lower on the sufficient loss formula, so L_B > 0.17415 at M = 387/1000
and L_B > 0.16245 at M = 361/1000, both above 0.152070. Closure check version 8 uses the uppers L_B <= 0.3651689966
(plan of record) and L_B <= 0.3412910741 (fallback) in its self-map rows and ell_KB only in its matrix row. Earlier
wordings of item 4, in theory exchange versions 11 to 24 and in drafts of this report and of the ledger, attached the
Lemma KB number to the loss of the closure inequality; the theory auditor REFUTES that identification (AT2917) and
CONFIRMS the two-condition statement with unchanged closure arithmetic (AT2918), the numerical auditor confirms both
independently (v940), and the theory erratum E-v24-1 of theory exchange version 25 records the correction (CONFIRMED,
AT2930). Both auditors reviewed the repaired account of this report and of the ledger at each later revision (AT2937,
AT2940, AT2941, AT2955, AT2956, AT2964, AT2965; numerical audit exchanges v946, v952, v955, v959) and CONFIRMED the
installed final text (AT2975; v967, v969); the post-stop edits described in the run record were not re-audited.

The H4 step of item 3 is a composition (AT-2333, CONFIRMED; the reading that asks for beta_* >= b0 alone is REFUTED,
AT-2334). It needs e_up + eps_rest <= beta_* - b0 and C0 >= P + C_rest, where e_up is the near upper, b0 the rate of
the closure test, and eps_rest and C_rest the rate and the price of every other full-L2 loss of the H4 join
(H4-REST). The second theory agent's closure check version 8 (the calculation and output in the accompanying artifacts, at near check version 9; CONFIRMED as a conditional calculation, AT2895
and AT2896; AT2897 OPEN) evaluates these inequalities at the certified inputs, with stand-ins for the uncertified
ones; its verdict is CLOSURE OPEN. Its block H names the hypotheses with the same names as in version 6 (AT-2617 to
AT-2619), and the table below uses those names.

Requirements of V11-2 (a) at 013 and P-S1 (one row per hypothesis; Part VII item 4):

| # | requirement | status | evidence |
|---|---|---|---|
| 1 | f, a certified upper of \|\|F_*\|\|_2 (item 2) | CERTIFIED by both auditors: \|\|F_*\|\|_2 in [7.959400186993612e-7, 7.961206656880281e-7] | numerical audit exchange v302, v305; AT-1413 |
| 2 | n, a certified upper of N(F_*) (item 2) | CERTIFIED by both auditors: N(F_*) in [0.0035510975483434412497, 0.0055545729030073655758] | numerical audit exchange v307, v317; AT-1430, AT-1431 |
| 3 | H-B, the background cover (item 2): beta_* >= 3/5, g_* <= 1/4, s_* <= c - A_far/q | CERTIFIED by both auditors at every point of the plane, under the admitted complete-source containment and balanced-root hypotheses: M_B >= (704955805507/10^12) I, \|grad h_*\| <= 1/4 and \|\|Sym Du_*\|\|_op <= 137/125, where M_B = (c + 1 + V.X/(1/4 + \|X\|^2)) I - q Sym DV + [[(rho_*)_y, -(rho_*)_x/2], [-(rho_*)_x/2, 0]] with V = cX + u_* is the background matrix of the dependency account in the accompanying artifacts (named M there; it is not the ball bound M = 387/1000). With the far upper A_far = 13396752347393121/9007199254740992 of route F-a (row 7), the strain level meets s_* <= c - A_far/q: q(c - 137/125) - A_far = 71675071190082633/5629499534213120000, about 0.012732 (AT2653, CONFIRMED), conditional on the retained analytic far premises of row 7. The stronger \|grad h_*\| <= 71/500 is certified on 124 of the 128 radial indices, not on 98, 100, 102 and 104 | numerical audit exchange v749, v755; AT-2534 to AT-2536 (AT-2537 OPEN); AT2653 |
| 4 | H-RC, RC-1 to RC-10 for h_* (item 1) | OPEN as a whole. The structural parts come from the exact-potential class (AT-674, AT-675); RC-5 is row 3, and RC-6 is rows 1 and 2 | closure check v06, block H |
| 5 | H-NEARU, the near upper e_up (item 3) | Supplied at the plan of record as a numerical input, under the analytic hypotheses H-N1 (row 6); at the fallback the mu 68 kernel bounds and the price allowance are not audited. CONFIRMED pieces: Lambda_+(a_n), \|\|(a_n)_+\|\|_1 and the two W^2 sups (Proposition R4 version 2). The whole-plane derivative norms of a_n are certified by both auditors: the numerical auditor executed the consumer of request 314 (2026-11-04T13:35:28Z to 13:37:07Z) with its own independent arithmetic check (v912), the theory auditor's distinct actual review CONFIRMED the brackets (14:00:19Z), and the numerical auditor adopted that review (v917, 14:06:53Z; the adoption is authenticated by the theory auditor, AT2885). Under the admitted Schwartz-decay and full-plane Plancherel premises and every retained source-containment, analytic-tail, regularity and Fourier-normalization hypothesis of the five admitted regional blocks, the origin and the exterior, D4 < 444.194167252431246601983285, D5 < 4186.352092180269533722245282 and D6 < 63050.392730580225839237053713, with M4(a_n) < 2691.963673338907009954203108 under NR-25. At these uppers the first theory agent's near check version 8 (the reviewed program the accompanying artifacts' near-check program, version 3, run 2026-11-04T14:08:28Z; the first theory agent's note 116) gives e_up = 154030213826/10^12 at the plan of record and 181864770976/10^12 at the fallback, and the numerical auditor's independent recomputation CONFIRMS it as conditional scalar arithmetic (v920), and so does the theory auditor's distinct review, with the actual derivative input (AT2887; theory audit exchange v877, 14:19:31Z); near check version 9 (the program the accompanying artifacts' near-check program, version 4; the first theory agent's note 116), which bounds M4(a_n) directly through NR-25, lowers e_up to 152627111489/10^12 at the plan of record and 180101237602/10^12 at the fallback; it is CONFIRMED by both auditors (numerical audit exchange v922, v925; AT2890, AT2891, theory audit exchange v878, 14:21:09Z) and is the near record. The second theory agent's closure checks version 7 (at near check version 8; the accompanying artifacts, closure check version 7) and version 8 (at near check version 9; closure check version 8, run 2026-11-04T14:23:28Z to 14:23:31Z) mark H-NEARU as supplied and are CONFIRMED as conditional scalar calculations (AT2894 to AT2896; theory audit exchange v879, 14:27:12Z), and the numerical auditor adopts both after an independent check (numerical audit exchange v926, 14:31:48Z). The numerical input completes no H4, inverse or self-map step by itself (AT2872, AT2886, AT2893, AT2897 OPEN) | AT-2520 to AT-2522; numerical audit exchange v912, v917, v920, v922, v925; AT2869 to AT2871, AT2885, AT2887, AT2890, AT2891, AT2894 to AT2896 (AT2872, AT2886, AT2893, AT2897 OPEN); request binding AT-2866, AT-2867 |
| 6 | H-N1 (item 3) | OPEN: N1 for the actual a_n, the whole-plane core split a_n = -a_c + a_r, and condition 4 of the erflog cut | the accompanying artifacts, near check version 7, section 3 |
| 7 | H-FA, the far upper A (items 2 and 3) | RETAINED: the analytic far premises are kept as hypotheses of the theorem (closure check block H); they are not certified here and are not among the six OPEN obligations of AT2912 and AT2916. Certified by both auditors: the CS-B Schur bound and the window stage R = W = 200. Under the retained analytic far premises (AE-CS, Corollary CS-W, Proposition DW, Lemma HSB, the center-013 calculus, the tail-table certificate, the Leibniz and Faa di Bruno estimates, the singleton repair and the CS-W homogeneity) the far scalar inequality at strain 137/125 holds with the exact gap 71675071190082633/5629499534213120000, about 0.012732. The theory auditor CONFIRMS this far numerical comparison under those premises (AT2653); the far computation alone supplies no global background, inverse or existence (AT-1931 OPEN) | AT-1921, AT-1922, AT-1928, AT-1929; numerical audit exchange v529, v532; AT-1931, AT-2653 |
| 8 | H4-REST, eps_rest and C_rest (item 3, through AT-2333) | OPEN; no piece has a certified bound. The pieces are T_IS, C_tr and C_vs1 to C_vs3. Rate rooms at the near record (near check version 9 and closure check version 8, row 5): eps_rest <= 1164347009/(5*10^11), about 2.328694018e-3, at the plan of record (b0, mu) = (11/20, 72), and eps_rest <= 1970913581/(2*10^11), about 9.854567905e-3, at the fallback (103/200, 68), which also needs the mu 68 kernel uppers kappa_0, kappa_2q and kappa_j (not audited); at near check version 8 they were 925591681/10^12 and 8091034531/10^12. The price rooms are C_rest <= 9941475955 at the plan of record and C_rest <= 47277952671/5 at the fallback, the exact rooms D_out - P, with P the near price (D_out - C0 of the closure checks, where C_rest = 0 stands in), the same in closure check versions 6 to 8; the printed 9941475900 and 9455590500 of versions 7 and 8 are conservative lower displays (theory audit exchange v879). Rooms are compared only within one version | near check version 8 and v09 (the accompanying artifacts); numerical audit exchange v920, v922, v925; AT2887, AT2890, AT2891, AT2894 to AT2896; closure check v06 to v08; AT-2587, AT-2625, AT-2649 OPEN |
| 9 | H1, the actual generator: closed generator, core, weighted semigroup and graph comparison on a reference ball | OPEN; conditionally reduced to H-B and the source bounds (AT-600; Lemma KB, AT-772, AT-832) | block H |
| 10 | H2, the full L2 inverse of L_* + U[k].grad with rate beta_0* on the ball (the uniform small-k inverse, O2 at 013) | OPEN | block H |
| 11 | H-BALL, the full real S1 ball with the center matrix premise of Lemma KB (item 4) | OPEN as a premise. Lemma KB is PROVED conditionally on the rectangle, with the matrix loss ell_KB < 0.152070 (AT-598, AT-832), which enters only the matrix condition of item 4 and does not bound the nonlinear loss L_B (AT2917). At the certified f, with beta_0* >= 7/4 (beta_0 > 2.00215453, AN-010, and g_* <= 1/4), the radius is R_* <= 4.54926094679e-7, below Rbar = 17/8750000 | closure check v06, section 4 |
| 12 | the closure inequality, O3 (item 4) | UNRESOLVED; the first unresolved condition. Its price C0 is fixed only once rows 5 to 8 are certified; b0 is the chosen rate of the closure test (11/20 at the plan of record, 103/200 at the fallback), and L_B is the nonlinear loss of item 4, distinct from the Lemma KB matrix loss (AT2917, AT2918). Closure checks version 7 (at near check version 8) and version 8 (at near check version 9), with eps_rest = C_rest = 0 as the only stand-ins at the plan of record, pass their conditional rows at both tuples (M = 387/1000 at the plan of record) and give CLOSURE OPEN, with H-RC, H1, H2, H-BALL, H4-REST and H-N1 OPEN; the theory auditor CONFIRMS both as conditional scalar calculations (AT2894 to AT2896; AT2897 OPEN), and the numerical auditor adopts both after an independent check (v926); version 8 is the last closure check of the run. These are conditional calculations, not closure ratios | closure check v06 to v08; theory audit exchange v879 |
| 13 | V11-2 (c), the k = 0 lifting at 013 (NR-31) | PROVED as a conditional application: L_* k0 = -F_* has a unique L2 solution, the L2 inverse has norm below 0.570726, N(k0) <= N(F_*)/beta_1 + C_1 \|\|F_*\|\|_2 for every 0 < beta_1 < 704955805507/10^12 with C_1 finite and not computed, and <X> k0 is in C^(1,1/10). Retained: the generator, semigroup and common-domain premises, RC-2, RC-4 and the weighted decay of F_* | AT-1483, AT-1484, AT-2541, AT-2599 |
| 14 | H-REG, V11-2 (d) | OPEN; not needed for (a) and (b) | block H |

The other entries of block H are supplied or retained: H3 ((R3/R5) of Theorem B, imported with their hypotheses),
H4-COMP (the implication AT-2333), H-N3 (certified kernel uppers at mu 72 and nu 1/40; AT-1491, AT-1492) and H-TAIL
(NR-25, NR-30 and NR-32; AT-1344 to AT-1346, AT-1453, AT-1454, AT-1512, AT-1513).

## B. The smallest remaining gap

The gap is not a single lemma. On the current route (route Q with the CE variant at P-S1, center 013), the theorem of
section A applies at 013, under every retained analytic premise, once rows 4 and 6 to 12 are certified
(row 5 is supplied at the plan of record as conditional arithmetic). Ordered by the coordinator's reading of their distance from certification (HEURISTIC as an ordering):

1. The near side (rows 5 and 6). The whole-plane derivative norms of a_n are certified by both auditors (numerical audit exchange v917;
   AT2869 to AT2871, AT2885), and near check version 8 at those uppers and near check version 9, with the direct NR-25 bound of
   M4(a_n), are CONFIRMED as conditional scalar arithmetic by both auditors (numerical audit exchange v920, v922, v925; AT2887, AT2890,
   AT2891); near check version 9, the near record, supplies the near upper at the plan of record and the rate rooms of row
   8; there its only numerical input that is not certified is eps_rest (the first theory agent's note 116). What remains: H-N1 (row 6),
   the analytic and localization hypotheses of the near upper, which the numerical input does not supply (AT2886),
   and at the fallback the audits of the mu 68 kernel bounds and the price allowance; at the stop the mu 68 fallback
   kernels are unreviewed (theory audit exchange v889), and the fallback price of the row mu_r = 76 is EXTRAPOLATED, with its
   band-separation premise OPEN (numerical audit exchange v943).
2. The rest term H4-REST (row 8), the nearest quantitative obstruction. What is needed: a certified eps_rest <=
   1164347009/(5*10^11) (about 2.328694018e-3) and C_rest <= 9941475955 at the plan of record, or eps_rest <=
   1970913581/(2*10^11) (about 9.854567905e-3) and C_rest <= 47277952671/5 at the fallback together with audited mu
   68 kernel uppers (the rooms of near check version 9 and closure check version 8). No piece has a bound. Three sufficient
   estimates are excluded at the stated budgets: the unsplit TIS-FG bound against the free gain
   (M_S >= 10529.58564315332 under ordinary Fourier inversion and finite moments; AT-2456 to AT-2458, AT-2622 to
   AT-2624); the Lemma HI' upper for every cut mu_r below the K_half floor, under the Fourier hypotheses of NR-34
   Corollary (c) and with the strain-axis point lower u_3 >= 5.123210549166463 (NR-34 Remark 7; AT-2752 to AT-2754):
   at the rate of the near record the floor is [151.855500860944, 151.855500860945] at the plan of record and
   [73.818964551323, 73.818964551324] at the fallback (numerical audit exchange v923, v925; AT2892), so the plan trials 208, 224 and 241
   are not excluded by this test and the fallback trial 72 is; the earlier floors 240.870095739 and 81.467708428
   (older rate; AT-2752 to AT-2754) and [240.866843317484, 240.866843317485] and [81.467561100353, 81.467561100354]
   (near check version 8 rate; numerical audit exchange v921; AT2888) hold only at their rates; and the near-check price of chi_n K alone with
   the registered kernel constants (Corollary O of the second theory agent's rest-term analysis in the accompanying artifacts; AT-2583). At the rooms of near check version 7
   and v08, on FLOAT and EXTRAPOLATED prices, no priced row gives a cut that serves both the HI' upper and the NE-lo
   price at either tuple (HEURISTIC; the new-theory account in the accompanying artifacts, S.3 (c)). At the room of NR-35 the fallback row
   mu_r = 76, priced at 0.91 times the room on the second theory agent's frequency-separated budget (EXTRAPOLATED, and conditional on
   the OPEN band separation), is no longer excluded; the HI' upper with K_half fits there only if u_3 <= 5.430421,
   and no upper of u_3 is certified (HEURISTIC; same section). These readings exclude nothing. The three exclusions
   concern sufficient estimates, not the H4 step or existence.
3. The far premises H-FA (row 7): the retained analytic premises of route F-a. The second theory agent's latest far note
   (the accompanying artifacts, far-form analysis) keeps every true far-form statement OPEN (AT-2840, AT-2862; the second theory agent's notes 13:40Z).
4. The operator premises: H1, H2 (the uniform small-k inverse), H-BALL and H-RC as a whole (rows 4, 9, 10 and 11).
5. Then O3 itself: the closure inequality of row 12 with certified constants.

## 1. What the theory team actually proved

The established results of Part 0 and Part II of the prompt are recorded, not re-proved, in
the established-proof reference in the accompanying artifacts (version 5, SHA256 55303f3f6bd1727ae59ac1e6a67847b2b402bcb69db0fe27ba472e423915aaa3). New
results are in the new-theory account in the accompanying artifacts (version 29, completed 2026-11-04T14:54:35Z, SHA256
de639e4054235ad9da9c4dc32e151d0890189b67750ee70e1e5655c7631243fb; its section S is the Part VII summary). Versions 28
and 29 change no bound, statement or status of version 27: they correct one word ("concavity" for "convexity" in the
Lemma E summary of S.5 item 3; AT2908) and two displays that rounded upward (151.8555 and 73.8189 for 151.86 and 73.82
in the S.3 cut brackets); the theory auditor CONFIRMS both as exactly the declared corrections (AT2921 to AT2923) and
the numerical auditor confirms them (v934, v939). Version 27 adds NR-35, the direct moment bound of near check version
9 (PROVED with AT2890 to AT2892; NR-35 (a) to (c) CONFIRMED, AT2905 to AT2907). The theory exchange ends at version 26
(completed 2026-11-04T15:46:37Z, SHA256 2f141b0d1c4261a33a4b1763731bca1046fe95302d2db7a2e4dceba29872a814), which adds
two reading clarifications and changes no bound, room, cut, hash or certified status (AT2949 to AT2951; v953); version
25 adds the errata E-v24-1 (the two losses of item 4 of section A; AT2930) and E-v24-2 (a program citation; AT2931).
The second theory agent's results are in its notes, with its Part VII account (version 15, frozen
2026-11-04T14:48:06Z, SHA256 2d37f2c8b9f95ef73ff79d69b92b8dcf87a67bc2f1e8f5096cdeed71a894185c; CONFIRMED as the current
consistent account, AT2913 to AT2915); at the rooms of closure check version 8 its largest saved far-model test gives
Gamma/c_star about 0.587 at the plan of record and 0.194 at the fallback (FLOAT; these tests give no supremum or form
bound). The theory auditor's ledger runs through AT2980 (2026-11-04T16:57:42Z). Its final audit report (version 3,
frozen 2026-11-04T16:10:29Z, SHA256 2cf4b2b790a098f63d332b88dab6b40b0da31a4fa83c6c3c48e9690e6921a4f8; AT2958 to
AT2960) separates proved, conditional, refuted and open statements, and its dependency account at 013 (version 5;
AT2901 to AT2903) places near check version 9 and closure check version 8 in one chain and names the six open Sobolev
obligations H-RC, H1, H2, H-BALL, H4-REST and H-N1, with H-REG additional for the Hoelder conclusion. Each item below is
CONFIRMED by the theory auditor conditionally on the hypotheses named in its entries.

- O1 at k = 0 (NR-1, T1-Thm-O1Hq; AT-031, with the steps AT-028 to AT-030). For L h = V.grad h - h + grad
  rho_bar.U[h] with (B-L2) at beta_0 = c + 1 - theta - kappa > 0, a BG-q cover lambda_max N_q <= -beta on R^2,
  2 < q < 3, 0 <= sigma < 1 + gamma_* and r0 > 0, the unique L2 solution of L h0 = -F satisfies ||<D>^q (W h0)|| <=
  (1/beta_1) ||<D>^q (W F)|| + C_1 ||F|| for 0 < beta_1 < min(beta, beta_0), and <X>^sigma h0 is in C^(1,alpha) for
  0 < alpha <= q - 2. For 007 the cover is certified at P-BG1 (prefactor 20, alpha <= 3/5; AT-056), P-BG2 (prefactor
  8, alpha <= 1/2; AT-074) and P-BG3 and P-BG4 (prefactor 10/3, alpha <= 1/10; AT-097, AT-172). C_1 contains the
  compact-remainder constant C_eps, which is not computed. At 013 the application is NR-31 (row 13 of section A).
- O2 for 007 on restricted balls: every real S1 k with N(k) <= 3/(20 D) gives a full weighted inverse of
  L + U[k].grad on weighted H^(21/10) with restricted gap beta_k >= 3/20 (AT-097, AT-172; at P-BG2, N(k) <= 1/(16 D),
  AT-074). D is symbolic, so this is not a self-map theorem, and these results do not transfer to a corrected center.
- The re-centered framework FW-C2-HqK-RC-v1 as an implication under RC-1 to RC-10 (AT-060, AT-123, AT-183), the exact
  correction class with its origin conditions, and the origin cap beta <= c + 1 - q (AT-119, AT-125, AT-174; NR-7,
  AT-211).
- Route Q and Theorem CE: an all-quadratic transport bound with no frequency cutoff, the conditional self-map test
  N(F) <= (b0 - L_Q(R, M)) M - C0 R^2/M (AT-227 to AT-230, AT-234 to AT-238, AT-243), Theorem CE (AT-272 to AT-275,
  AT-283) and its transfer to P-S1 (AT-303 to AT-308).
- The conditional center-013 theorem V11-2 (AT-978, AT-979) with Lemma KB on the 013 rectangle (AT-598, AT-832; the
  repaired and clamped CE witnesses fit its domain, AT-727, AT-772), and the H4 composition (AT-2333).
- Near and far lemmas of the 013 route: Proposition HF1-NEAR with tail B (AT-691, AT-757); Lemma HSB and the general
  Lemma HS (AT-695, AT-756); the corrected separated far budget of the accompanying artifacts' far-budget analysis, version 2 (AT-860; AT-857 REFUTES that the
  general separated certificate needs the stronger target A_low^+ <= SC^+); route F-a (AT-911, AT-1017); Proposition
  R4 version 2 for the near coefficient (AT-2520 to AT-2522); the tail, kernel and assembly tools NR-16 to NR-30 and
  NR-32 (the new-theory account in the accompanying artifacts, S.1 (f)); the whole-plane assembly theorems for regional certificates (AT-319,
  AT-397 to AT-399, AT-484, AT-505, AT-508).
- Necessary conditions and ceilings. NR-7: any weak energy rate at a tuple is at most its BG-q margin (AT-211). NR-6:
  for the unchanged Candidate 007, the coarse criterion of FW-C2-HqK-v1, with the certified radius floor R_floor =
  0.3766893/(c + 1), can hold only if N(F) < N_*(q), with N_*(21/10) <= 1.097831 (NR-6.3 (c); AT-095, AT-118). The
  route-Q tests have ceilings at every center (AT-271, AT-274, AT-304, AT-307, AT-335). NR-3 item 6: for the zero
  background, which is not normalized, the L2 rate is c + 1, yet the L2 solution for a smooth annular S1 forcing is
  not in H^q near the origin for q >= 1 + 1/c (about 1.5523888); so no H^q estimate with such q follows from an L2
  gap and smooth forcing alone over a class containing this background (AT-2713, AT-2714).
- Exclusions of sufficient criteria, not of existence: the listed Sobolev criteria at 007 (AT-063, AT-075, AT-080,
  AT-088, AT-124); the five named route-Q tests at the two b7 centers, caused by certified far-field lowers (AT-260,
  AT-287, AT-317, AT-324, AT-335, AT-352); the TII-0 constructions in stated ranges (AT-408, AT-423, AT-449); and the
  three H4-REST estimates of section B, item 2.
- Identities and lowers for the H4 rest term: u_3 = 2 m_2(S) and, under the admitted Fourier hypotheses (valid
  differentiation and inversion formulas, finite moments, the stated Fourier and matrix-norm conventions and no
  unaccounted zero-frequency polynomial contribution), the origin lower u_3 >= 3.799152003154 (AT-2564) and the
  strain-axis lower u_3 >= 5.123210549166463 (AT-2753); the T_IS coefficient K_half = c_tr' + q/2 (AT-2565); the
  identities and Corollary O of the second theory agent's rest-term analysis in the accompanying artifacts (AT-2580 to AT-2583); NR-33 and NR-34 (AT-2600, AT-2601). The
  FFT screens of u_3 near 10.3 are HEURISTIC. For the exact center-013 field, the ideal exact-sample normalized
  absolute FFT sums on each fixed square [-16,16]^2 and [-32,32]^2 diverge as the resolution tends to infinity
  (AT-2744, AT-2745); this bounds neither the finite-grid error nor the whole-plane Fourier moment and does not imply
  that the moment diverges (theory audit exchange v831; AT-2746 OPEN).

Not proved: a bound of eps_rest or C_rest, the analytic far premises, H1, H2, the invariant ball, existence, and a
Hoelder lifting beyond C^(1,1/10) at 013. Refuted or withdrawn readings are listed in section 8.

## 2. What the numerical team actually improved

The L2 residual of the center, in the order reached (from the numerical account in the accompanying artifacts, version 18, section 4;
every value FLOAT unless labelled certified):

| stage | state | \|\|F\|\|_2 | label |
|---|---|---|---|
| baseline | Candidate 007 (reference 007) | 0.3766893247 | certified (the previous campaign's numerics agent 3 N4-139) |
| existing basis, pure L2 | 003 | 0.1107 | FLOAT; its complete norm is certified (AN-054) |
| basis expansion (N2) | E6a (expanded-basis candidate 001) | 0.02542 | FLOAT |
| exact odd-potential correction of 007 | 007 | 1.25e-5 | FLOAT |
| far-field-first correction | 009 | 2.86e-6 (binary64), 2.82e-6 (longdouble) | certified by both auditors: [2.818778457305e-6, 2.818982922317e-6] (AT-1065 to AT-1067) |
| D8 dictionary with lattice tails | 012 | 1.278e-6 (longdouble) | FLOAT |
| D8 with near-field P-S1 rows (the chain center) | 013 | 7.96e-7 (longdouble) | certified by both auditors: [7.959400e-7, 7.961207e-7] (AT-1411 to AT-1413) |
| research states with the same exact constraints | b21w2, b25s, b26s, b27s, b28s | 4.907e-7 down to 3.4755e-7 | FLOAT; not certified, not used by any theory item |

- Factors: from 007 to 013 about 4.7e5, certified at both ends; to b28s about 1.08e6 (FLOAT). The constraints depend
  on the stage. The E-series fits of the existing basis (the second numerics agent) keep the 421 exact far-field and origin rows and the
  eleven EXACT-ZERO far-field sectors of 007. The odd-potential corrections carry A + 3B = 0 and ell(h_*) = 0
  exactly, the eleven forbidden sectors of 007 cancel exactly in the base, and from 008 on their far field is
  also controlled by budget-weighted soft rows: the sine coefficients of the twelve far-field classes from e =
  -2.7904 to -4.3713, 807 rows with the dictionary D8 (010 to 013); exact cancellation of these classes is not
  claimed (the accompanying artifacts' candidate index; the numerical account in the accompanying artifacts).
- Strong norms: at 013, N_(21/10)(F_*) is certified by both auditors in [0.0035510975483434412497,
  0.0055545729030073655758] (row 2 of section A; the coarser [0.0035510, 0.0055546] is a safe outward rounding, while
  [0.0035511, 0.0055546] is not, numerical audit exchange v916); at 009, N_(21/10)(F) in [0.01457238375810, 0.02971779021642] (AT-1065
  to AT-1067). The prompt's Hoelder quantity S_F: AN-012 certifies strict lower bounds for the unchanged Candidate
  007 at six parameter triples, 112.785157863859 at (alpha, delta, sigma) = (1/2, 2/5, 7/4), 49.229794743454 at
  (3/10, 3/10, 7/4), 657.367864566556 at (1/2, 3/5, 7/4), 164.888904500253 at (1/2, 2/5, 9/4), 298.629414897243 at
  (1/2, 2/5, 5/2) and 86.781584053442 at (1/2, 2/5, 1) (ordered-Frobenius sum convention of
  the accompanying artifacts' strong-norm proof; numerical audit exchange v927), and no certified upper bound of S_F is supplied for any
  corrected center. At P-H = (1/2, 2/5, 7/4), the second numerics agent's FLOAT diagnostics fall from [112.84, 158.54] at 007 to
  [0.03173, 0.03643] at 009 and about [0.0068, 0.0083] at 013; at the D8 centers they carry an uncontrolled binary64
  roundoff error, and since no theorem of the campaign made S_F binding, no certified upper was attempted
  (the second numerics agent's final summary, version 5, section 3, in the accompanying artifacts).
- Certified fields at 013 (both auditors): the whole-plane background bounds of row 3 of section A, and the near
  lower bounds D6(a_r) >= 45543 and D6(a_n) >= 62748. The whole-plane near brackets of D4, D5 and D6 of a_n are
  certified by both auditors as well (row 5; numerical audit exchange v917).
- Levers that worked: the longdouble residual as the training objective (the binary64 floor is 6e-7 to 9e-7),
  far-field-first sector rows, lattice tails for the modes above 47, near-field P-S1 Sobolev rows, and dictionary
  scales aimed at the dominant dyadic band. Negative results: diminishing returns of the row weight below 1e-8, the
  D9 deep classes, the raised-cut re-solve, and b29s, whose export is the same function as b28s (the numerical audit exchange
  v552). The far bands 300 <= r <= 1e4 carry 53 percent of the b28s residual energy on the fixed meshes (FLOAT).
- A research center would need its own certified chain. For 013 the observed durations were about 6.5 hours to the
  whole-plane norms, about 18 hours of near-cover owner computations and about 19 hours for the background route
  (observed, not predictions).
- The second numerics agent's part (basis expansion, the S_F and strong-norm evaluators, near-cover owner jobs, mode
  jets in 40-digit arithmetic) is summarized in its final summary, version 5 (assembled 2026-11-04T14:31Z, SHA256
  af14c89792de72f36776ddedba808bc9e48dc3904f59b341dd34e7b648cf1588), whose four dated corrections E1 to E4 the
  numerical auditor CONFIRMS (v928). the numerical account in the accompanying artifacts (final stamp 2026-11-04T15:03Z, SHA256
  32d45ff376c0501a34b93efe273dbb0f11e1e637b2448d4e282404e799d5502b) is the first numerics agent's Part VII report; the
  numerics exchange ends at version 18 (2026-11-04T13:43:22Z), read with its errata E46 to E51 (E51 labels the FLOAT
  cut displays of N50.4 as figures at the earlier rate tuples of near check versions 6 and 7).

## 3. How the teams communicated

- Agents and roles (the working conventions in the accompanying artifacts, written in the first hours: norm definitions, normalization conventions,
  candidate ID and hash rules, the ledger format and the writer of each exchange file). The first theory agent: O1 and
  the parameter optimization of section 14 of the prompt; theory publisher. The second theory agent: O2 and O3. The
  first numerics agent: N1, existing-basis optimization with exact constraints; numerics publisher. The second numerics
  agent: N2, basis expansion, and the evaluator of the strong residual norm S_F. Two independent auditors, one for
  theory and one for numerics (independent recomputation of residual norms, constraints and certificates). The
  coordinator: the joint ledger, dated reallocation notes, the mid-campaign report and this report. All seven worked
  concurrently for the whole run; each wrote only in its own working directory and its assigned exchange files.
- Exchange, read-only once written: theory requirement versions 1 to 26 (the first theory agent; the last completed
  2026-11-04T15:46:37Z), numerical result versions 1 to 18 (the first numerics agent; the last published
  2026-11-04T13:43:22Z), immutable candidate snapshots (15 snapshots, each with a manifest SHA256, and 5 exact
  far-sector supplements, all listed in the candidate index) and the joint closure ledger (the coordinator only; every
  version kept).
- Audits. Each auditor kept an append-only ledger of dated verdicts (AT entries for theory, AN entries for numerics)
  with numbered exchange files. The numerical auditor's Part VII report (version 3, frozen 2026-11-04T15:50:32Z, SHA256
  23b54d0626fb998d50b491ef0cba4213d217b999594233ba27a999024cfa7dcc; CONFIRMED within its scope by the theory auditor,
  AT2944, AT2945), its reading guide (version 9, frozen 2026-11-04T16:21:24Z; AT2961, AT2962) and its final cutoff note
  (frozen 2026-11-04T16:44:17Z; AT2972, AT2973) give the final numerical account. Computations on certified paths ran
  through a fixed chain: a frozen request, the theory auditor's binding review, an executor with pending and completed
  receipts, a distinct actual review, and adoption. Results entered the ledger only after an auditor verdict.
- Ledger cycles (every 4 hours, plus two setup versions):

| version | written (UTC) | cycle |
|---|---|---|
| v00 | 2026-11-02T18:13Z | setup |
| v01 | 2026-11-02T18:20Z | setup |
| v02 | 2026-11-02T22:06:03Z | X1 |
| v03 | 2026-11-03T02:06:03Z | X2 |
| v04 | 2026-11-03T05:40:08Z | X3 |
| v05 | 2026-11-03T10:05:30Z | X4 |
| v06 | 2026-11-03T14:05:30Z | X5 |
| v07 | 2026-11-03T18:03:59Z | X6 |
| v08 | 2026-11-03T21:52:13Z | X7 |
| v09 | 2026-11-04T00:37:46Z | X8 |
| v10 | 2026-11-04T04:08:54Z | X9 |
| v11 | 2026-11-04T06:17:33Z | X10 |
| v12 | 2026-11-04T09:59:25Z | X11 |
| v13 | 2026-11-04T13:39:44Z | X12 |
| v14 | 2026-11-04T16:38:17Z | X13 (final) |

- Coordinator notes: 126 dated reallocation notes, from 2026-11-02T18:16Z to 2026-11-04T16:38Z, with interim notes
  between cycles and corrections by dated errata. Drafts of notes and ledger versions had an external referee pass by
  a second model before or after publication (166 questions, 165 answered); its answers were treated as claims and
  checked. The mid-campaign report was published at 2026-11-03T09:35:35Z, 15.5 hours after the start.
- Scheduling: the coordinator, the two theory agents and the theory auditor shared two CPU cores, with at most one busy
  computation each; each numerics agent had four cores with up to four computations, and the numerical auditor one
  core. The coordinator ran no heavy computation. Idle cores of the numerics agents could host auditor runs under a
  host method that the theory auditor confirmed and the numerical auditor admitted; no hosted job was to start at or
  after 16:00Z on the last day. To keep each agent under its disk limit, duplicate retained inputs of the auditors were
  replaced by relative links to byte-identical files of other agents after independent byte reviews (the last executed
  2026-11-04T13:56:06Z to 13:56:07Z, postcondition CONFIRMED, v915).

## 4. How parameters were optimized

- Fixed: c_l and the authoritative Candidate 007.
- Tuple. P-S1 = (21/10, 1, 1/2) was adopted on 2026-11-02T20:59Z, P-S2 = (21/10, 7/5, 1) was promoted to the primary
  tuple on 2026-11-02T23:01Z with P-S1 kept as a target, and after the P-S2 tests were excluded at the b7 centers the
  P-S1 CE test became the route for new centers (2026-11-03T04:11Z). The choice is HEURISTIC (AT-142). The reasons:
  the cap c + 1 - q falls one for one with q, so q just above 2 keeps the most rate room, and alpha = q - 2 = 1/10;
  sigma = 1 meets Lemma E (sigma < 2 - 1/c, room about 0.4476) and the origin condition sigma >= q(1 - 1/c) (room
  about 0.06); r0 = 1/2 fixes c_W and the constants of NR-14.
- Center. Optimized within the exact correction class: the existing basis, an expanded basis, exact odd-potential
  corrections with exact far-field sector rows, far-field-first weighting, then the D8 dictionary with near-field
  rows. 013 was frozen as the chain center on 2026-11-03T11:25Z on FLOAT and HEURISTIC headroom; it is not a
  certified comparison and does not exclude 009.
- Rate and near cut. The background target was beta_* >= 3/5 with g_* <= 1/4 (giving beta_0* >= 7/4). The near window
  uses b0 = 11/20 at the cut mu = 72 (plan of record), with the fallback (103/200, 68) and the low cut nu = 1/40.
  FLOAT planning scans of (b0, mu) found no window below beta_* of about 0.68 (HEURISTIC). For the H4-REST cut mu_r,
  at the rate room of near check version 7 (the new-theory account in the accompanying artifacts version 29, S.3 (c)), the cut this route would need
  lies between the certified necessary lower 240.870095739 (under the Fourier hypotheses of NR-34 Corollary (c)) and
  the HEURISTIC sufficient value of about 492 for the principal part at the plan of record, and between 81.467708428
  and about 166 at the fallback; at that room the fallback is the cheaper tuple, with a rate room about 8.74 times
  that of the plan of record and a least cut about 0.338 times. At the room of the near record near check version 9 the
  certified necessary lowers fall to [151.855500860944, 151.855500860945] and [73.818964551323, 73.818964551324]
  (NR-35 (c); AT2892), the HEURISTIC upper ends to about 310 and about 150, and the two ratios become about 4.232 and
  0.486 (version 29, S.3 (c); rounded displays, numerical audit exchange v932).
- Localization. Far and near split at erflog 8 and rho 1 (theory exchange version 22, V11-3); far window R = W = 200; near tail
  points 54 and 36; split radius R0 = 16/mu.
- No margin of O3 is certified, so no parameter is optimal in a certified sense.

## 5. Whether theorem closure was obtained

No. See the Verdict and sections A and B.

## 6. Work that should continue next

1. Finish the near side: H-N1 (the analytic and localization hypotheses of the near upper), and the audits of the mu
   68 kernel bounds and price allowance if the fallback is used.
2. H4-REST, the deciding item: a certified upper of u_3 (at the fallback the row mu_r = 76 would fit the HI' upper if
   u_3 <= 5.430421; HEURISTIC, the new-theory account in the accompanying artifacts, S.3 (c)) or of the T_IS piece, a certified NE-lo price,
   or a larger rate room through a joint principal estimate that allows the ceiling c + 1 - q in place of beta_*
   (rooms at least 7.69209871099e-3 at the plan of record and 1.52179725979e-2 at the fallback, the conditional lower
   displays of near check version 9, the near record; theory audit exchange v760). At the fallback the mu 68 kernel uppers need an audit.
3. The retained analytic premises of route F-a (H-FA).
4. The operator premises at 013: the actual generator H1, the uniform small-k inverse H2, the ball premise H-BALL and
   the RC conditions as a whole.
5. Only then the closure inequality O3 with certified constants.
6. Numerics: a better center (b28s or later) helps only with its own certified chain; S_F of the corrected centers
   has FLOAT diagnostics only, with no certified upper; the far bands 300 <= r <= 1e4 dominate the b28s residual
   (FLOAT).
7. Regularity beyond C^(1,1/10) at 013 (V11-2 (d)).

## 7. Part VII outputs and the restartable workspace

The accompanying artifacts contain the five required reports: the established-proof reference, the new-theory
account, the numerical account, the joint closure ledger (version 14, written 2026-11-04T16:38:17Z,
SHA256 6413c8897966b392fa72b5288a18ab9dcf7b83cee3bdcf0b27c389dcd57fe461) and a copy of this report,
with the mid-campaign report and the working conventions. They also retain the two audit ledgers and the auditors'
final reports; the latest exchanges (theory version 26, numerics version 18); the candidate index and snapshots of
accepted center 013 and alternatives 009 and 012, with their exact coefficients, constraints and manifests; and
proof notes, programs and outputs for the near and closure checks.

The guide to the accompanying artifacts gives exact commands, setup and restart instructions, and lists the omitted
material: run logs, scratch, caches, exact far-sector supplements of about 113 MB each, large fixed-background
meshes, and the source data of Candidate 007 and the previous campaign. The publication copies reproduce the
retained closure arithmetic, but some original audit bindings fail because scripts and notes were edited for
publication. Full certificate replay requires the omitted inputs and original versions identified by those bindings.
The published checksums identify the current copies; they do not replace the original audit evidence.
Restart from 013 or research state b28s follows section 15 of the numerical account in the accompanying artifacts;
any new center needs its own certified chain.

## 8. Refuted or withdrawn readings

These statements were proposed during the campaign and are REFUTED as stated, or withdrawn; the conditions on which
the surviving results rest are the ones in section A.

- The H4 test with beta_* >= b0 alone, the cap-level budget of reading (i) (AT-2334).
- Four displays of theory exchange version 22 as implications of the cited bounds: the lowers 3.80 for u_3, 10529.6 for M_S and 3.398
  for rhobar_y(0), and an equality in the fallback price ratio (AT-2678 to AT-2681); the safe displays
  3.799152003154, 10529.58564315332, 3.397977278 and a fallback ratio of at least 1.93 are CONFIRMED (AT-2682).
- The inference from exterior agreement to the same rate-price estimate on the whole homogeneous dilation class
  (cutoff counterexample, AT-2839), and the claim that with P = 0 the model upper fails at every individual test with
  a positive form value (AT-2861).
- The fallback least cut of about 223 at the assumed u_3 = 10.4 (the value lies between 116 and 117, AT-2720; both
  figures belong to the rooms of near check version 7, not to the current near check version 9 rate rooms, and the assumed u_3 is
  unproved; theory exchange version 26 N-v25-2; numerical audit exchange v945, v946, v949), and 4.0016 as an exact criterion for the HI' upper at mu 72
  (AT-2648).
- The claim that the sampled far decay proves that no window radius works (AT-2585).
- The statement of the new-theory account in the accompanying artifacts version 23 that the cited C_vs2 has no form (AT-2634; corrected in version 24,
  AT-2716), the time declarations of theory exchange version 21 (AT-2544) and a certification wording of theory exchange version 20 (AT-2432).
- In the far and near band work: osc(b) alone as a bound of the full low-pass form (AT-805), the band constant as a
  finite-dimensional problem (AT-697), a universal sharp-low-pass oscillation floor (AT-873), a universal cubic cost
  of certified dense uppers (AT-874), and a universal gain of a modified origin majorant (AT-846).
- Three orders of decay as sufficient for RC-2 (AT-123), and FLOAT agreement of 009 and 013 far quantities to 1e-7
  (AT-877).
- Coordinator readings: a status flag read as a 1/4 failure when it tested 71/500 (AT-2200); the prior-review
  condition for the removal of two diagnostic archives (AT-2138; section 9).
- A strict endpoint stated in AT-2038 was withdrawn by the theory auditor in AT-2043.
- The interval [0.0035511, 0.0055546] as an outward rounding of the certified P-S1 interval of row 2 (numerical audit exchange v916);
  the norm certificate itself stands, and the first numerics agent (erratum E49) and the second numerics agent (final numerical summary, version 5, in the accompanying artifacts, erratum E1) correct
  their displays.
- The inference in theory exchange version 23 (V23-0, requirement 4 (iii), and V23-1 (b)) from the divergence of the ideal
  exact-sample FFT sums to a nonconvergent sequence of production screen values (AT2882); the ideal divergence
  stands, and production convergence and its error stay OPEN (AT2883).
- The identification of the Lemma KB matrix loss ell_KB < 0.152070 with the nonlinear loss of the closure inequality,
  in the wording of item 4 of V11-2 (a) in theory exchange versions 11 to 24 and in the frozen coordinator drafts named in
  theory audit exchange v885 (AT2917); the two-condition statement is CONFIRMED (AT2918), the theory erratum E-v24-1 of theory exchange version 25 is
  CONFIRMED (AT2930), and section A item 4 carries it. The citation of the accompanying artifacts' near-check program, version 4, as the program of
  near check version 8 in V24-3 (a) of theory exchange version 24, which was the accompanying artifacts' near-check program, version 3 (AT2928; erratum E-v24-2, CONFIRMED,
  AT2931). The word "convexity" for the concave function 1 - (1 + u)^(-q/2) in S.5 item 3 of the new-theory account in the accompanying artifacts
  version 27 (AT2908; corrected in version 28, AT2921); Lemma E and the tangent upper bound remain valid.
- Three readings in section 16 of the second numerics agent's final numerical summary, version 4, in the accompanying artifacts: the equality u_3 >= 2 ||Delta S(0)||_op =
  3.799152003154 (the exact value strictly exceeds 3.799152003154, so the decimal is a lower bound), the passage at
  the cut 208 from the old floor of about 207.422, and [3.799, 21.36] as a certified interval for u_3 (21.36 is a
  FLOAT estimate) (numerical audit exchange v918); the second numerics agent corrects all three in the accompanying artifacts' final numerical summary, version 5 (errata E2 to E4; CONFIRMED, the numerical auditor
  v928).

## 9. Process deviations

- The numerical auditor removed two diagnostic archives of the 009 chain (437055889 bytes) at 2026-11-04T05:28:45Z to
  05:28:50Z, before the review that the coordinator's 05:28Z condition required; AT-2138 REFUTES that the condition was
  met, and AT-2139 keeps their recovery OPEN. Exact byte recovery of those archives is not demonstrated; their content
  is reproducible only by regeneration.
- Coordinator slips: on 2026-11-02 at 20:28Z a backup copy of the coordinator notes was written to the system temporary
  directory and deleted within a minute, and at 22:00Z an edit script was written there and moved into the coordinator's
  directory at once; on 2026-11-03 at 21:18:42Z a stray copy command put a copy of the coordinator notes into the
  exchange directory, removed at 21:18:55Z after a byte-identical check; on 2026-11-04 at 14:50:51Z an interim note was
  posted with the typed header time 14:52Z, a planned minute, and corrected to 14:50Z at 14:51:06Z; and the bundle
  program of 15:45:38Z paired the numerical auditor's Part VII report version 3 with the bindings manifest of version 1
  (AT2948 CONFIRMED), repaired at 15:59:54Z, before any bundle was written (AT2953 CONFIRMED); AT2947 REFUTES the further
  reading of AT2942 that the program admitted publication wrappers.
- Storage links (section 3) replaced retained duplicate inputs of the auditors; the linked owner files stay as regular
  files, and the bundle of the required reports copies no linked file.
- The post-stop edits of this report (status line, summary, run record, condensed sections 1, 3, 7 and 9, and the
  replacement of internal names) were made after the team stop and were not re-audited; see the run record.
