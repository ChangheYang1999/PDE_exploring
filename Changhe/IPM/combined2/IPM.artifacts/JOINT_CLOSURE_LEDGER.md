# JOINT CLOSURE LEDGER (combined2), version v14

Written by the coordinator, 2026-11-04T16:38:17Z (cycle X13; the final ledger of the campaign). Format: WORKSPACE_CONTRACTS.md section 8.
Supersedes v13 (coordinator/ledger_history/JOINT_CLOSURE_LEDGER_v13.md, SHA256
80abc4007b37281a8b573964d09600af7b23c5cb3b32243fd70bd0179e499234, written 2026-11-04T13:39:44Z), which is not edited.
v14 states the final state in a compact form: one row per requirement of the strongest theorem, with its numerical
status. The row-by-row history, the full constants archive, the candidate history and the input lists of v00 to v13
stay in those versions (coordinator/ledger_history) and are not repeated; where v14 and an earlier version differ, v14
holds.

Inputs new in v14: theory_audit/AUDIT_LEDGER.md through AT2967 of 2026-11-04T16:28:36Z and theory_audit/exchange through
audit_v899; the numerical audit exchange through v961 (published 2026-11-04T16:33:35Z);
exchange/theory_requirements/theory_v23.md to theory_v26.md (theory_v26 completed 2026-11-04T15:46:37Z, SHA256
2f141b0d...); THEORY_NEW_RESULTS.md version 29 (SHA256 de639e40...) and EXISTING_PROOFS_REFERENCE.md
version 5 (SHA256 55303f3f...); theory_agent_1/research/closure_check/NEAR_CHECK_v08 and v09; theory_agent_2/notes/T2_PART7_v13 to v15
and T2_CLOSURE_CHECK_v07 and v08; theory_audit/reports/SOURCE013_CHAIN_CONDITIONS_v05, FINAL_THEORY_AUDIT_v01 to
FINAL_THEORY_AUDIT_v03; numerical_audit/reports/PART_VII_NUMERICAL_AUDIT_v01 with its addendum version 1,
PART_VII_NUMERICAL_AUDIT_v03 (consolidated through AN949), AUDIT_READING_GUIDE_v08 and AUDIT_READING_GUIDE_v09; the
agent notes through the headers of 2026-11-04 at 16:17Z (the first theory agent), 15:27Z (the second theory agent), 15:52Z (the first numerics agent) and 16:09Z (the second numerics agent).
Also exchange/numerical_results/numerics_v18.md (SHA256 8a4fdb85..., 2026-11-04T13:43:22Z; the final numerics
version, with the first numerics agent's errata E46 to E51 in the first numerics agent team notes; E51, 15:41Z, CONFIRMED by numerical audit exchange v949, labels the
FLOAT cut displays of N50.4 as figures at the earlier rate tuples of NEAR_CHECK_v06 and v07),
NUMERICAL_OPTIMIZATION.md version 18 (final stamp 15:03Z, SHA256 32d45ff3...) with its dated corrections of
14:15Z, 14:32Z, 14:49Z and 15:03Z (the last repairs the two N2 citations; numerical audit exchange v938), and
numerics_agent_2/results/N2_FINAL_SUMMARY_v05.md (2026-11-04T14:31:31Z, SHA256 af14c897...; version 04 of 13:47:57Z with the
dated corrections E1 to E4 of numerical audit exchange v916 and v918, CONFIRMED by numerical audit exchange v928).

Labels: WORKSPACE_CONTRACTS.md section 1. PROVED and CONFIRMED only with a the theory auditor entry (AT-n) for theory or a the numerical auditor entry (AN-n or
exchange vNNN) for numerics; "certified by both auditors" means an executed the numerical auditor result that the theory auditor confirmed in a
distinct review and that the numerical auditor adopted. FLOAT values carry no enclosure; HEURISTIC marks a planning reading.

## (a) Verdict

COMPLETE EXISTENCE THEOREM CERTIFIED: NO.

First unresolved condition: O3, the closure inequality of the invariant ball (row 12 of section (c)). No center,
corrected or not, has a certified invariant ball. No DONE file and no CASE_SOLVED file were written.

The strongest theorem is the conditional theorem V11-2 (a) (theory_v11, carried unchanged to theory_v24, AT2879,
audit_v887, with the erratum E-v24-1 of theory_v25 for item (4); CONFIRMED as a conditional assembly, AT-978, AT-979,
with 0 < M <= 1/2 required by AT-980, and with item (4) read as two conditions, AT2917, AT2918) at the chain center
C2-N1-013 and the tuple P-S1. At 013, rows 1 and 2 of section (c) and the numerical background bounds of row 3 are
certified by both auditors (the strain condition s_* <= c - A_far/q of row 3 holds numerically with the far upper
A_far of row 7, AT2653, under the retained analytic far premises of row 7); row 5, the near upper, is supplied at the
plan of record as a numerical input that both auditors CONFIRM, under the analytic hypotheses of row 6; row 13 (the k
= 0 lifting) is PROVED as a conditional application. Rows 4 and 6 to 12 are not certified: rows 4, 6 and 8 to 11 are
the six OPEN obligations H-RC, H-N1, H4-REST, H1, H2 and H-BALL (AT2912, AT2916), row 7 keeps the far premises H-FA
as retained analytic hypotheses, and row 12 is the first unresolved condition. A stationary solution would follow at
013 once rows 4 and 6 to 12 are certified.

Statement (setting and notation as in section (b)). Assume (1) RC-1 to RC-10 of the re-centered framework (AT-123)
for h_*; (2) certified bounds ||F_*||_2 <= f and N(F_*) <= n, and a certified cover with N_q* <= -beta_* I on R^2,
beta_* >= 3/5, g_* <= 1/4 and s_* <= c - A_far/q, where A_far is a certified far upper of the far route used; (3) a
certified near upper (Proposition HF1-NEAR) and the far upper A_far, combined in the frozen H4 estimate; (4) R_* =
f/beta_0* <= Rbar = 17/8750000 and Mbar = 1/2; the reference-ball condition betaK_* >= beta_* - ell_KB > 0, where
ell_KB < 0.152070 is the matrix loss of Lemma KB on that rectangle (AT-598, AT-832); and, separately, the self-map
inequality C0 R_*^2 <= M[(b0 - L_B(R_*, Kbar; B_CE, A_CE)) M - n] for some 0 < M <= Mbar, with b0 - L_B(R_*, Kbar;
B_CE, A_CE) > 0, n >= N(F_*) and Kbar a strict root witness of Corollary CE-B, an admitted graph witness
Kbar > M + E(R_*, Kbar) (Corollary HF-Q-CE, AT-273), every full-generator, inverse, source and H4 premise retained
(the wording of erratum E-v24-1, CONFIRMED by AT2930 and numerical audit exchange v943). Here A_far is the far-field upper, (B_CE, A_CE)
is an admitted CE pair, and the independent cutoffs T_S and T_V of Lemma KB, in q S(T_S) + V(T_V), satisfy T_S,
T_V > 8q; for the current CE pair (B_CE, A_CE) = (13/25, 18959/1000), A_far < 3/2 < A_CE and B_CE < 8q = 84/5
(AT2938). Then the profile problem has a stationary solution h = h_* + k, rho = rho_bar + h, with k real and
S1, ||k||_2 <= Rbar and ||J^(21/10)(W k)||_2 <= M <= 1/2, and <X> h is in C^(1,1/10)(R^2). The H4 step of (3) is the
composition e_up + eps_rest <= beta_* - b0 and C0 >= P + C_rest (AT-2333 CONFIRMED; AT-2334 REFUTES the reading with
beta_* >= b0 alone). Item (4) has two distinct losses: L_B > (9/20) Kbar > (9/20) M, so L_B > 0.17415 at M = 387/1000
and L_B > 0.16245 at M = 361/1000, above the Lemma KB number 0.152070 (AT2917 REFUTES the earlier wording that
attached 0.152070 to the loss of the closure inequality; AT2918 CONFIRMS the two-condition statement and the
unchanged closure arithmetic; numerical audit exchange v940; erratum E-v24-1 of theory_v25).

## (b) Constants block

Decimal displays shortened from certified enclosures are rounded outward unless the row says otherwise; for endpoints
use the full digits or the cited record.

| quantity | value | label | audit / source |
|---|---|---|---|
| c = c_l | 4076476460239181/2251799813685248, about 1.8103192102; not varied | EXACT | AT-001 |
| a_0 = d_y rho_bar(0) (007) | 10.311999021064395... (exact rational) | EXACT, CONFIRMED-AN | AN-001 |
| theta, kappa (R1, 007) | theta <= 2/25; kappa < 0.72816468018232542729 | UB, CONFIRMED-AN | AN-010, AN-008 |
| beta_0 = c_l + 1 - theta - kappa (007) | > 2.0021545300176726583587 | LB, CONFIRMED-AN | AN-010 |
| beta_0* at 013 | >= 7/4 (from beta_0 and g_* <= 1/4) | LB, CONFIRMED as a conditional calculation | closure check v06 (theory_agent_2/notes/T2_CLOSURE_CHECK_v06.md); AT-2617 to AT-2619 |
| tuple P-S1 = (q, sigma, r0) | (21/10, 1, 1/2); W(X) = (1 + 4\|X\|^2)^(1/2); N(G) = \|\|J^(21/10)(W G)\|\|_2, J = (1 - Delta)^(1/2) | EXACT; the choice is HEURISTIC | AT-142 |
| alpha | q - 2 = 1/10, the Sobolev endpoint of V11-2 (b) | EXACT | theory_v11 V11-2 (b) |
| delta (V11-2 (d), route R6.4 only) | needs alpha/(2c - 2) < delta < 1: delta above 562949953421312/9123383232769665, about 0.0617041; route R6.4 also needs 1 < nu < 2 | EXACT threshold; the lifting is OPEN | AT-979; theory_v11 V11-2 (d) |
| nu (low cut of the near window) | 1/40 | EXACT parameter | closure check v06 |
| \|\|F\|\|_2 (007) | in (0.37668932470589426194, 0.37668932470589426195) | VALIDATED, CONFIRMED-AN | AN-005 |
| S_F(1/2, 2/5, 7/4) (007) | > 112.785157863859; FLOAT diagnostics [112.84, 158.54] | LB CONFIRMED-AN; upper not certified | AN-012 (strict lower bounds for 007 at six parameter triples, numerical audit exchange v927); numerics_agent_2/results/N2_FINAL_SUMMARY_v05.md section 3 |
| S_F(1/2, 2/5, 7/4) (013) | FLOAT diagnostics about 0.0068 and 0.0083 (binary64, uncontrolled roundoff); S_F is not binding in any theorem of the campaign | FLOAT | N2_FINAL_SUMMARY_v05 section 3 |
| f: \|\|F_*\|\|_2 (013) | in [7.959400186993612e-7, 7.961206656880281e-7] | certified by both auditors | numerical audit exchange v302, v305; AT-1411 to AT-1413 |
| n: N(F_*) at P-S1 (013) | in [0.0035510975483434412497, 0.0055545729030073655758]; the safe coarse form is [0.0035510, 0.0055546], not [0.0035511, 0.0055546] (numerical audit exchange v916) | certified by both auditors | numerical audit exchange v307, v317; AT-1430, AT-1431 |
| background at 013 | M_B >= (704955805507/10^12) I, \|grad h_*\| <= 1/4 and \|\|Sym Du_*\|\|_op <= 137/125 at every point of the plane, under the admitted complete-source containment and balanced-root hypotheses, for the background matrix M_B = (c + 1 + V.X/(1/4 + \|X\|^2)) I - q Sym DV + [[(rho_*)_y, -(rho_*)_x/2], [-(rho_*)_x/2, 0]] with V = cX + u_* (theory_audit/reports/SOURCE013_CHAIN_CONDITIONS_v05.md, where it is named M; it is not the ball bound M = 387/1000); \|grad h_*\| <= 71/500 on 124 of the 128 radial indices (not on 98, 100, 102, 104) | certified by both auditors | numerical audit exchange v749, v755; AT-2534 to AT-2536 (AT-2537 OPEN) |
| ball | Rbar = 17/8750000, Mbar = 1/2; plan-cell M = 387/1000 | EXACT parameters | theory_v11 V11-2; closure check v06 |
| R_* = f/beta_0* (013) | <= 4.54926094679e-7, below Rbar | UB, CONFIRMED as a conditional calculation | closure check v06 section 4; AT-2617 to AT-2619 |
| matrix loss ell_KB of Lemma KB | < 0.152070 on the 013 rectangle; it enters only the matrix condition betaK_* >= beta_* - ell_KB > 0 of item (4) | PROVED conditionally | AT-598, AT-832 (the repaired and clamped CE witnesses fit its domain: AT-727, AT-772) |
| nonlinear loss L_B of the self-map inequality (013) | L_B > (9/20) Kbar > (9/20) M, so L_B > 0.17415 at M = 387/1000 and L_B > 0.16245 at M = 361/1000; closure check v08 uses the uppers 0.3651689966 (plan of record) and 0.3412910741 (fallback) | lower on the sufficient loss formula, not on an optimal operator loss, and uppers, confirmed by both auditors (AT2917, AT2918; numerical audit exchange v940) | audit_v885; numerical audit exchange v940 |
| near window | (b0, mu) = (11/20, 72), the plan of record; fallback (103/200, 68) | EXACT parameters; HEURISTIC choice | closure check v06; NEAR_CHECK_v07 |
| near coefficient a_n (013), whole plane | D4 < 444.194167252431246601983285, D5 < 4186.352092180269533722245282, D6 < 63050.392730580225839237053713 (24-decimal brackets), M4(a_n) < 2691.963673338907009954203108 under NR-25, under the admitted Schwartz-decay and full-plane Plancherel premises and every retained source-containment, analytic-tail, regularity and Fourier-normalization hypothesis; lowers D6(a_r) >= 45543, D6(a_n) >= 62748 | certified by both auditors: executed by the numerical auditor (v912), CONFIRMED by the theory auditor (AT2869 to AT2871), adopted by the numerical auditor (v917; AT2885); AT2872 and AT2886 OPEN: inputs only, no H4, inverse or self-map step follows by itself | numerical audit exchange v912, v917; the theory auditor audit_v872, audit_v876 |
| near upper and rate rooms at the certified near inputs (NEAR_CHECK_v08) | plan of record: e_up = 154030213826/10^12, eps_rest room 925591681/10^12; fallback: e_up = 181864770976/10^12, eps_rest room 8091034531/10^12; superseded by the next row | CONFIRMED as conditional scalar arithmetic by both auditors, with the actual derivative input (numerical audit exchange v920; AT2887) | theory_agent_1/research/closure_check/NEAR_CHECK_v08.md; the first theory agent's note 116; numerical audit exchange v920; the theory auditor audit_v877 |
| the near record: the same with the direct NR-25 bound of M4(a_n) (NEAR_CHECK_v09) | plan of record: e_up = 152627111489/10^12, eps_rest room 1164347009/(5*10^11), about 2.328694018e-3; fallback: e_up = 180101237602/10^12, eps_rest room 1970913581/(2*10^11), about 9.854567905e-3 (also needs the unaudited mu 68 kernel uppers); eps_rest is the only numerical input of the plan-of-record check that is not certified; the near upper also needs H-N1 (row 6) | CONFIRMED as conditional scalar arithmetic by both auditors (numerical audit exchange v922, v925; AT2890, AT2891) | theory_agent_1/research/closure_check/NEAR_CHECK_v09.md; numerical audit exchange v922, v925; the theory auditor audit_v878 |
| price rooms of closure checks v06 to v08 | plan of record: C_rest <= 9941475955; fallback: C_rest <= 47277952671/5; the exact rooms D_out - P, with P the near price (D_out - C0 of the checks, where C_rest = 0 stands in), the same in v06 (FLOAT D4 to D6), v07 (NEAR_CHECK_v08) and v08 (NEAR_CHECK_v09); the printed 9941475900 and 9455590500 of v07 and v08 are conservative lower displays | CONFIRMED as conditional calculations (v06: AT-2617 to AT-2619; v07, v08: AT2894 to AT2896) | closure check v06; theory_agent_2/notes/T2_CLOSURE_CHECK_v07.md, T2_CLOSURE_CHECK_v08.md; the theory auditor audit_v879 |
| margins at the ceiling rate c + 1 - q | conditional lower displays (cap-level margin, lower): 6.28897137799e-3 (plan of record) and 1.34544099599e-2 (fallback) at NEAR_CHECK_v07; 0.00628899637399 and 0.0134544392239 at NEAR_CHECK_v08 (numerical audit exchange v920); 7.69209871099e-3 and 1.52179725979e-2 at NEAR_CHECK_v09; using the ceiling in place of beta_* needs an additional principal or joint estimate, and no matrix recount can exceed it | not an available room | audit_v760; AT-211; theory_v23 |
| H4-REST lowers | under the admitted Fourier hypotheses (valid differentiation and inversion formulas, finite moments, the stated Fourier and matrix-norm conventions and no unaccounted zero-frequency polynomial contribution): u_3 >= 3.799152003154 from the origin calculation (AT-2564), u_3 >= 5.123210549166463 from the strain-axis point (AT-2753) and M_S >= 10529.58564315332 (AT-2456 to AT-2458, AT-2622 to AT-2624); K_half floors of the HI' estimate, under the Fourier hypotheses of NR-34 Corollary (c): 240.870095739 (plan) and 81.467708428 (fallback) at the older rate (AT-2752 to AT-2754), [240.866843317484, 240.866843317485] and [81.467561100353, 81.467561100354] at the NEAR_CHECK_v08 rate (numerical audit exchange v921; AT2888), and [151.855500860944, 151.855500860945] and [73.818964551323, 73.818964551324] at the rate of the near record, NEAR_CHECK_v09 (numerical audit exchange v923, v925; AT2892); each floor holds only at its rate | CONFIRMED lowers of sufficient estimates | as cited |
| far gap (route F-a, strain 137/125) | 71675071190082633/5629499534213120000, about 0.012732, under the retained analytic far premises | CONFIRMED as a conditional inequality | AT-2653; window R = W = 200 and CS-B: AT-1921, AT-1922, AT-1928, AT-1929, numerical audit exchange v529, v532 |
| NR-31 inverse at 013 | L2 inverse norm < 0.570726; N(k0) <= N(F_*)/beta_1 + C_1 \|\|F_*\|\|_2 for 0 < beta_1 < 704955805507/10^12, C_1 finite and not computed | PROVED as a conditional application | AT-1483, AT-1484, AT-2541, AT-2599 |

## (c) Condition table

The strongest registered framework is V11-2 (a) at 013 (route Q with the CE variant at P-S1). One row per hypothesis;
rows 4 to 12 use the names of block H of theory_agent_2/research/closure_check/closure_check_v08.out (at NEAR_CHECK_v09;
CONFIRMED as a conditional calculation, AT2895 and AT2896; AT2897 OPEN), which are those of version 6 (AT-2617 to
AT-2619). The former center 009 has no chain work since the coordinator decision of 2026-11-03T11:25Z; its certified
values are in section (e).

| # | ID | exact condition | threshold (framework, status) | value at 013 (label, audit) | certified? | margin | sensitivity | improves |
|---|---|---|---|---|---|---|---|---|
| 1 | f (item 2; RC-6) | \|\|F_*\|\|_2 <= f, with R_* = f/beta_0* <= Rbar | V11-2 (a), conditional assembly (AT-978, AT-979) | [7.959400186993612e-7, 7.961206656880281e-7] (both auditors; AT-1413) | yes | R_* <= 4.54926094679e-7 against Rbar = 17/8750000 (conditional calculation) | f enters R_* and C0 R_*^2 | done; a smaller f needs a new center with its own chain (the first numerics agent, the numerical auditor) |
| 2 | n (item 2; RC-6) | N(F_*) <= n | V11-2 (a) | [0.0035510975483434412497, 0.0055545729030073655758] (both auditors; AT-1430, AT-1431) | yes | not defined until C0 is certified (row 12) | n enters (b0 - L_B) M - n | done |
| 3 | H-B (item 2; RC-5) | N_q* <= -beta_* I with beta_* >= 3/5, g_* <= 1/4, s_* <= c - A_far/q | V11-2 (a) | M_B >= (704955805507/10^12) I, \|grad h_*\| <= 1/4, \|\|Sym Du_*\|\|_op <= 137/125 on the plane (M_B of section (b); both auditors; AT-2534 to AT-2536) | yes for beta_* and g_*; s_* <= c - A_far/q holds numerically: q(c - 137/125) - A_far = 71675071190082633/5629499534213120000 for the far upper A_far of row 7, under its retained premises (AT2653) | beta_* exceeds 3/5 by at least 0.104955805507 | beta_* bounds the rate room of rows 5 and 8 | done |
| 4 | H-RC (item 1) | RC-1 to RC-10 for h_* | FW-C2-HqK-RC-v1 (AT-060, AT-123) | structural parts from the exact-potential class (AT-674, AT-675); RC-5 is row 3; RC-6 is rows 1 and 2 | no (OPEN as a whole) | none | none | The first theory agent, the theory auditor |
| 5 | H-NEARU (item 3) | the near upper e_up, with e_up + eps_rest <= beta_* - b0 | Proposition HF1-NEAR (AT-691, AT-757); Proposition R4 version 2 (AT-2520 to AT-2522) | CONFIRMED pieces Lambda_+(a_n), \|\|(a_n)_+\|\|_1 and the two W^2 sups; the whole-plane D4, D5, D6 and M4 of section (b), certified by both auditors (numerical audit exchange v917; AT2869 to AT2871, AT2885); NEAR_CHECK_v09 at those uppers, the near record: e_up = 152627111489/10^12 (plan of record) and 180101237602/10^12 (fallback), CONFIRMED as conditional scalar arithmetic by both auditors (numerical audit exchange v922, v925; AT2890, AT2891; NEAR_CHECK_v08 likewise, numerical audit exchange v920, AT2887); closure checks v07 and v08 mark H-NEARU supplied (AT2894 to AT2896; numerical audit exchange v926) | yes as a numerical input at the plan of record; its analytic premises are row 6; at the fallback the mu 68 kernel bounds and the price allowance are not audited; the input completes no H4 step by itself (AT2872, AT2886, AT2893 OPEN) | rate rooms of row 8 | D4, D5, D6, the M4 bound and the cut mu | The first theory agent |
| 6 | H-N1 (item 3) | N1 for the actual a_n, the whole-plane core split a_n = -a_c + a_r, condition 4 of the erflog cut | NEAR_CHECK_v07 section 3 | none | no (OPEN) | none | none | The first theory agent, the theory auditor |
| 7 | H-FA (items 2 and 3) | the far upper A_far with s_* <= c - A_far/q | route F-a (AT-911, AT-1017) | CS-B and the window stage R = W = 200 certified by both auditors; the far scalar inequality at strain 137/125 holds with the gap of section (b) under the retained analytic premises (AE-CS, Corollary CS-W, Proposition DW, Lemma HSB, the source013 calculus, the tail-table certificate, the Leibniz and Faa di Bruno estimates, the singleton repair, the CS-W homogeneity) | the numerical comparison yes, conditional on the retained premises (AT2653); the premises are retained hypotheses, not among the six OPEN obligations (AT2912, AT2916), and the far computation alone supplies no global background, inverse or existence (AT-1931 OPEN) | 71675071190082633/5629499534213120000, about 0.012732, conditional | strain level, window radius | The second theory agent, the first theory agent |
| 8 | H4-REST (item 3, through AT-2333) | eps_rest and C_rest of every other full-L2 loss of the H4 join (pieces T_IS, C_tr, C_vs1 to C_vs3) | H4 composition (AT-2333) | no piece bounded; the rooms and lowers of section (b); three sufficient estimates excluded at the stated budgets (TIS-FG, Lemma HI' below the K_half floors, Corollary O of T2_H4REST_v01, AT-2583) | no (OPEN; AT-2587, AT-2625, AT-2649 OPEN) | eps_rest room 1164347009/(5*10^11) and C_rest room 9941475955 at the plan of record (NEAR_CHECK_v09, closure check v08) | b0, mu, beta_* | The second theory agent, the first theory agent |
| 9 | H1 | closed generator, core, weighted semigroup and graph comparison on a reference ball | RC theorem T2.7 (AT-123) | conditionally reduced to H-B and the source bounds (AT-600; Lemma KB, AT-772, AT-832) | no (OPEN) | none | none | The first theory agent, the second theory agent |
| 10 | H2 | the full L2 inverse of L_* + U[k].grad with rate beta_0* on the ball (O2 at 013) | T2.7 (AT-123) | none at 013; O2 for 007 on restricted balls of symbolic size only (AT-097, AT-172) | no (OPEN) | none | none | The second theory agent |
| 11 | H-BALL (item 4) | the full real S1 ball with the center matrix premise of Lemma KB | Lemma KB (AT-598, AT-832) | R_* <= 4.54926094679e-7 < Rbar; matrix loss ell_KB < 0.152070, for the matrix condition only (AT2917) | no (OPEN as a premise) | not computed | Rbar, Mbar | The second theory agent, the first theory agent |
| 12 | O3 (item 4) | C0 R_*^2 <= M[(b0 - L_B(R_*, Kbar; B_CE, A_CE)) M - n] for some 0 < M <= 1/2, with b0 - L_B > 0 and an admitted CE graph witness Kbar (the nonlinear loss L_B, not the Lemma KB matrix loss; AT2917, AT2918) | V11-2 (a) item 4 (erratum E-v24-1) | C0 is fixed only once rows 5 to 8 are certified; closure checks v07 (NEAR_CHECK_v08) and v08 (NEAR_CHECK_v09), with eps_rest = C_rest = 0 as the only stand-ins at the plan of record, pass their conditional rows at both tuples (M = 387/1000 at the plan of record) and give CLOSURE OPEN, with H-RC, H1, H2, H-BALL, H4-REST and H-N1 OPEN (CONFIRMED as conditional calculations by both auditors, AT2894 to AT2896, numerical audit exchange v926; AT2897 OPEN); these are conditional calculations, not closure ratios | no: UNRESOLVED, the first unresolved condition | not computed | every row above | all agents |
| 13 | NR-31 (V11-2 (c)) | the k = 0 lifting at 013: L_* k0 = -F_* | T1.2 (AT-031) applied at 013 | unique L2 solution, inverse norm < 0.570726, N(k0) <= N(F_*)/beta_1 + C_1 \|\|F_*\|\|_2 for 0 < beta_1 < 704955805507/10^12, <X> k0 in C^(1,1/10); retained: generator, semigroup and common-domain premises, RC-2, RC-4 and the weighted decay of F_* | PROVED as a conditional application (AT-1483, AT-1484, AT-2541, AT-2599) | C_1 not computed | none | done |
| 14 | H-REG (V11-2 (d)) | a Hoelder lifting beyond C^(1,1/10) | R6.4 or the heavier-weight route | delta threshold of section (b); mu_R not evaluated for 013 | no (OPEN; not needed for (a) and (b)) | none | alpha, delta | The first theory agent |

Supplied or retained entries of block H: H3 ((R3/R5) of Theorem B, imported with their hypotheses), H4-COMP (the
implication AT-2333, CONFIRMED: principal, near, far and rest estimates on the same common domain give H4 when
e_up + eps_rest <= beta_* - b0 (row 5) and C0 >= P + C_rest, with the strict-rate and separate tail hypotheses of
H4-R retained; its component estimates are rows 5 to 8), H-N3 (certified kernel uppers at mu 72 and nu 1/40; AT-1491,
AT-1492; the fallback mu 68 kernel uppers kappa_0, kappa_2q and kappa_j are not audited) and H-TAIL (NR-25, NR-30 and
NR-32; AT-1344 to AT-1346, AT-1453, AT-1454, AT-1512, AT-1513).

## (d) Closure ratio

G = eps_theory/||F||_2: not computed. The only framework with a registered closure threshold at 013 is V11-2 (a),
whose hypotheses in rows 4 and 6 to 12 of section (c) are not certified, so its threshold is not a PROVED one. The
PASS results of closure check v06 use stand-ins for the uncertified inputs and are not closure ratios.

## (e) Candidates

Admissibility rule: WORKSPACE_CONTRACTS.md section 6 (c_l exact, (B0n) EXACT, the eleven forbidden far-field sectors EXACT-ZERO).
The full candidate history is in v13 section (e).

| ID | G0 = \|\|F\|\|_2 | strong norm | beta_0 / background | admissibility | role |
|---|---|---|---|---|---|
| C2-REF-007 (authoritative reference; unchanged) | in (0.37668932470589426194, 0.37668932470589426195) (AN-005) | S_F(1/2, 2/5, 7/4) > 112.785 (AN-012); N_q > 43.26 at P-Q2 and > 9.699 at P-S1 (AN-023, AN-033) | beta_0 > 2.0021545 (AN-010) | admissible (AN-001) | reference background |
| C2-N1-009 (007 + b14s) | in [2.818778457305e-6, 2.818982922317e-6] (both auditors; numerical audit exchange v208; AT-1065 to AT-1067) | N_(21/10)(F) at P-S1 in [0.01457238375810, 0.02971779021642] (both auditors; same records); S_F FLOAT diagnostics [0.03173, 0.03643] | global background gap OPEN (AT-445) | exact structure CONFIRMED (OBS-009-STRUCTURE-001; AT-386, AT-387) | former center; no chain work since 2026-11-03T11:25Z |
| C2-N1-013 (007 + b18s2; snapshot MANIFEST SHA256 615f09c58c07ee4845a5e1bc3f321f8cc427f06bfdde5a75b3166f0f95f6c9df) | in [7.959400186993612e-7, 7.961206656880281e-7] (both auditors; AT-1413) | N_(21/10)(F_*) in [0.0035510975483434412497, 0.0055545729030073655758] (both auditors); S_F FLOAT diagnostics about 0.0068 and 0.0083 | background bounds of section (b) (both auditors); beta_0* >= 7/4 | exact structure CONFIRMED (OBS-013-STRUCTURE-001; AT-674 to AT-676) | chain center since 2026-11-03T11:25Z (frozen) |
| b28s (research state, not a snapshot) | FLOAT 3.4755e-7 (longdouble MID 40) | not evaluated | not evaluated | same exact constraints as 013 (the first numerics agent) | not certified; not used by any theory item |

## (f) Changes since v13

1. Whole-plane near norms of a_n, now certified by both auditors: the numerical auditor executed request 314 (v912, 13:35:28Z to
   13:37:07Z), the theory auditor's distinct actual review CONFIRMED the brackets (audit_v872, 14:00:19Z; AT2869 to AT2871), the numerical auditor
   adopted that review (v917, 14:06:53Z) and the theory auditor authenticated the adoption (audit_v876, 14:12:08Z; AT2885); AT2872
   and AT2886 OPEN: they are inputs and close nothing by themselves.
2. NEAR_CHECK_v08 at those uppers (the first theory agent's note 116; run 14:08:28Z): e_up = 154030213826/10^12 and the eps_rest room
   925591681/10^12 at the plan of record, 181864770976/10^12 and 8091034531/10^12 at the fallback; CONFIRMED as
   conditional scalar arithmetic by both auditors, with the HI' K_half floors at its rate (numerical audit exchange v920, v921; AT2887,
   AT2888; audit_v877, 14:19:31Z). NEAR_CHECK_v09 (direct NR-25 bound of M4(a_n)), now the near record: e_up =
   152627111489/10^12 and 180101237602/10^12, rooms 1164347009/(5*10^11) and 1970913581/(2*10^11); CONFIRMED by both
   auditors with the HI' floors at its rate (numerical audit exchange v922, v923, v925; AT2890 to AT2892; audit_v878, 14:21:09Z).
3. The second theory agent's closure checks version 7 (T2_CLOSURE_CHECK_v07, run 14:15:15Z to 14:15:18Z, at NEAR_CHECK_v08) and version
   8 (T2_CLOSURE_CHECK_v08, run 14:23:28Z to 14:23:31Z, at NEAR_CHECK_v09): H-NEARU supplied, CLOSURE OPEN; CONFIRMED
   as conditional calculations by both auditors (AT2894 to AT2896; audit_v879, 14:27:12Z; numerical audit exchange v926, 14:31:48Z).
   T2_PART7_v13 (frozen 14:18:02Z) CONFIRMED as an integration at its stated cutoff (AT2898, AT2899; AT2900 OPEN;
   audit_v880, 14:28:22Z). T2_PART7_v14 (frozen 14:36:06Z, SHA256 e8ca8564...) and T2_PART7_v15 (frozen 14:48:06Z,
   SHA256 2d37f2c8...; the second theory agent's notes 14:48Z) bind closure check version 8 and state each HI' exclusion with its rate;
   the theory auditor CONFIRMS version 15 as the current consistent account, together with the changes of version 14 (AT2913 to
   AT2915; AT2916 OPEN; audit_v884, 14:57:34Z). At the version 8 rooms the earlier far-model exclusion at the plan of
   record (about 1.201) no longer holds; the largest saved test gives Gamma/c_star about 0.587 (plan of record) and
   0.194 (fallback) (FLOAT; AT2915; numerical audit exchange v935; no supremum or form bound); the numerical auditor CONFIRMS its numerical integration
   (v937).
4. The theory auditor's dependency account theory_audit/reports/SOURCE013_CHAIN_CONDITIONS_v05.md (frozen through AT2900; audit_v881,
   14:34:54Z) places NEAR_CHECK_v09 and closure version 8 in one chain, reconfirms the rate rooms 2328694018/10^12
   and 9854567905/10^12, the price rooms 9941475955 and 47277952671/5 and the least integer HI cuts 195, 164, 152 and
   95, 80, 74, and names six open Sobolev obligations (H-RC, H1, H2, H-BALL, H4-REST, H-N1), with H-REG additional
   for the Hoelder conclusion (AT2901 to AT2903 CONFIRMED; AT2904, the existence theorem, OPEN); the numerical auditor CONFIRMS its
   numerical integration and adopts the review (v931, 14:48:16Z).
5. The second theory agent's T2_PART7_v12 and T2_ROUTE1_v03 CONFIRMED as corrected integrations (AT2873, AT2874; audit_v873); the
   actual far-form obstruction, H4-REST, the uniform inverse, the invariant ball and existence stay OPEN (AT2875).
6. Lemma E of theory_agent_2/notes/T2_FS1_EPS_v01.md CONFIRMED: ||W^(-1) J^(-q) f||_2 <= M(f) + (q/2)||Delta f||_2 at q =
   21/10, with its dilation law (AT2876, AT2877; audit_v874); the FLOAT diagnostic is not a continuum certificate
   (AT2878 OPEN).
7. theory_v23 (the first theory agent; completed 2026-11-04T13:56:35Z, SHA256
   c81fb3a9b21dbaa9a2d09abd911a1cc0c2799dc48aa9fe59d940510632b25071): the theory auditor CONFIRMS its conditional statements,
   verdict inventory and preview arithmetic (AT2879 to AT2881), REFUTES one inference about the FFT screens (AT2882)
   and CONFIRMS the corrected scope (AT2883); AT2884 OPEN (audit_v875, 14:07:32Z). theory_v24 (completed 14:56:12Z,
   SHA256 36804e0f...; the first theory agent's note 118) adds the erratum E-v23-1, NEAR_CHECK_v09 as the near record with the rooms and
   HI' cuts of near-check versions 7 to 9 kept apart, closure checks 7 and 8, and route (1) by rooms; the theory auditor CONFIRMS
   its new sections within their conditional scope (AT2925 to AT2927) and REFUTES only the V24-3 (a) citation that
   NEAR_CHECK_v08 used near_check_v04.py, which was near_check_v03.py (AT2928; AT2929 OPEN; audit_v887, 15:11:32Z);
   the numerical auditor likewise (v941). theory_v25 (completed 15:14:21Z, SHA256 b2ab07c9...; the first theory agent's note 120) adds only the errata
   E-v24-1 (the two losses of item (4)) and E-v24-2 (that citation) with the audit records through AT2929 and the numerical auditor
   v941; the theory auditor CONFIRMS E-v24-1 (AT2930), E-v24-2 (AT2931) and the integration of the seventeen verdicts AT2913 to
   AT2929 (AT2932) and leaves stationary existence OPEN (AT2933; audit_v888, 15:16:49Z); the numerical auditor CONFIRMS its numerical
   integration (v943, 15:21:22Z). theory_v26 (completed 15:46:37Z, SHA256 2f141b0d...; the first theory agent's note 123), the last
   theory exchange of the run, adds two reading clarifications and changes no bound, room, cut, hash or certified
   status: N-v25-1, the distinct names A_far, (B_CE, A_CE) and T_S, T_V of AT2938, and N-v25-2, that the FFT-input
   cuts at the assumed u_3 = 10.4 belong to the rooms of NEAR_CHECK_v07; it records AT2930 to AT2939 and numerical audit exchange v942
   to v947. The theory auditor CONFIRMS it as a conditional integration (AT2949 to AT2951; AT2952 OPEN; audit_v894) and the numerical auditor
   CONFIRMS its numerical integration (v953).
8. numerical audit exchange v918 REFUTES three readings in section 16 of the second numerics agent's N2_FINAL_SUMMARY_v04 (the equality form of the origin
   lower of u_3, passage at the cut 208 from the old floor, and [3.799, 21.36] as a certified interval); no
   certificate changes, and the second numerics agent corrects all three in N2_FINAL_SUMMARY_v05 (errata E2 to E4; the second numerics agent's notes 14:32Z;
   CONFIRMED, numerical audit exchange v928, 14:38:34Z).
9. Display correction: numerical audit exchange v916 REFUTES [0.0035511, 0.0055546] as an outward rounding of the certified P-S1
   interval of row 2; the certificate stands, and this ledger uses the full endpoints (the first numerics agent erratum E49, 14:15Z;
   the second numerics agent erratum E1 in N2_FINAL_SUMMARY_v05).
10. S_F account: AN-012 certifies strict lower bounds of S_F for the unchanged Candidate 007 at six parameter
    triples, not only S_F(007) > 112.785157863859 at P-H, and no certified upper bound is supplied for any corrected
    center (numerical audit exchange v927, 14:38:09Z); the coordinator's 14:27Z note and NUMERICAL_OPTIMIZATION.md section 5 had called
    the P-H bound the only certified S_F statement and are corrected (coordinator note 14:50Z; the first numerics agent's notes 14:49Z).
    No certificate changes.
11. Storage: the theory auditor's duplicate of the origin baseline input was replaced by a relative link to the numerical auditor's byte-identical
    regular file under the coordinator's 13:49Z note (frozen approval_v01, 13:54:26Z; the numerical auditor semantic review v914;
    executor 13:56:06Z to 13:56:07Z; the numerical auditor postcondition CONFIRMED, v915). No numerical certificate changes.
12. Final Part VII inputs: numerics_v18 (13:43:22Z) and NUMERICAL_OPTIMIZATION.md version 18; the second numerics agent's
    N2_FINAL_SUMMARY_v05 (assembled 14:31Z, the second numerics agent's notes 14:32Z; SHA256
    af14c89792de72f36776ddedba808bc9e48dc3904f59b341dd34e7b648cf1588; version 04 of 13:47:57Z with the dated
    corrections E1 to E4); THEORY_NEW_RESULTS version 29 (completed 14:54:35Z, SHA256 de639e40...; the first theory agent's note 118),
    which changes no bound, statement or status of version 27 (version 28: the curvature word of AT2908; version 29:
    the cut displays of numerical audit exchange v932; the numerical auditor CONFIRMS version 28, v934, and the version 29 displays, v939; the theory auditor
    CONFIRMS both as exactly the declared corrections, with no identification of the two losses, AT2921 to AT2923,
    AT2924 OPEN, audit_v886); THEORY_NEW_RESULTS version 27 (completed 14:32:35Z, SHA256
    d6c90f3ccbc0b89f304b27dab9041cf6c9304778acf76bcab789305699f5e421, the first theory agent's note 117; it adds NR-35, PROVED, AT2890
    to AT2892, and Remark 8 of NR-34, AT2888), CONFIRMED as a faithful integration with NR-35 (a) to (c) and Remark 8
    (AT2905 to AT2907; one word of its Lemma E summary REFUTED without effect on Lemma E, AT2908; AT2909 OPEN;
    audit_v882, 14:42:45Z); the numerical auditor's Part VII contribution PART_VII_NUMERICAL_AUDIT_v01 (frozen 14:42:06Z; v930) with
    its addendum PART_VII_NUMERICAL_AUDIT_ADDENDUM_v01 (frozen through AN941, SHA256 bf814326...; v942) and reading
    guide AUDIT_READING_GUIDE_v08 (frozen through AN944, SHA256 e9ab7eb5...; v945; replaced as the current guide by
    version 9, frozen 16:21:24Z through AN957, SHA256 2b45f766..., v958, which changes no numerical table and asserts
    no new bound; CONFIRMED within its stated scope, AT2961 and AT2962, with existence OPEN at AT2963, audit_v898),
    consolidated with the later confirmations in PART_VII_NUMERICAL_AUDIT_v03 (frozen 15:50:32Z through AN949, SHA256
    23b54d06...; v950; CONFIRMED within its stated scope, AT2944 and AT2945, with existence OPEN at AT2946,
    audit_v892), the numerical auditor's current Part VII contribution, with version 1 and the addendum retained as the timely
    delivery; EXISTING_PROOFS_REFERENCE version 5 (SHA256 55303f3f..., unchanged; the first theory agent's note 118); the theory auditor's current
    Part VII handoff FINAL_THEORY_AUDIT_v03, its final planned revision (frozen 16:10:29Z with evidence through
    AT2957, SHA256 2cf4b2b7...; audit_v897, AT2958 and AT2959 CONFIRMED, AT2960 OPEN; numerical audit exchange v957 CONFIRMS its
    numerical integration), which replaces version 2 (frozen 15:20:47Z with evidence through AT2933, SHA256
    8fe5870f...; audit_v889, AT2934 and AT2935 CONFIRMED, AT2936 OPEN; numerical audit exchange v944; retained) and version 1 (frozen
    14:48:56Z with evidence through AT2909, SHA256 d11ebc52...; audit_v883, AT2910 and AT2911 CONFIRMED, AT2912 OPEN;
    numerical audit exchange v936; supplements audit_v885 to audit_v887; retained); NUMERICAL_OPTIMIZATION.md (final stamp 15:03Z,
    SHA256 32d45ff3...; the two N2 citations repaired, numerical audit exchange v938), the first numerics agent's Part VII input; the first numerics agent declares all its
    deliverables final (the first numerics agent 15:41Z).
13. Format: v14 is a compact final ledger; the requirement table of section (c) replaces the item tables of v13
    section (a) and the v05 condition table carried in v13 section (c).
14. The two losses of item (4) of V11-2 (a): the Lemma KB matrix loss ell_KB < 0.152070 enters only the matrix
    condition betaK_* >= beta_* - ell_KB > 0, and the nonlinear loss L_B of the self-map inequality satisfies
    L_B > (9/20) Kbar > (9/20) M, so L_B > 0.17415 at M = 387/1000 and L_B > 0.16245 at M = 361/1000; closure check
    version 8 uses the uppers 0.3651689966 and 0.3412910741. AT2917 REFUTES the earlier wording that attached
    0.152070 to the loss of the closure inequality (theory_v11 to theory_v24 and the frozen coordinator drafts named
    in audit_v885); AT2918 CONFIRMS the two-condition statement with unchanged closure arithmetic (numerical audit exchange v940); the
    erratum E-v24-1 of theory_v25 is CONFIRMED (AT2930; numerical audit exchange v943); the theory auditor and the numerical auditor CONFIRM that the drafts of this
    ledger and of the final report, as edited at 15:23:24Z, implement the repair, not that they are final files
    (AT2937; AT2939 OPEN; numerical audit exchange v946), and the theory auditor CONFIRMS the conditional account of both drafts and the budgets and
    obligations of the X13 note at the identities named in the coordinator's 15:46Z note and their 15:47:49Z
    successors (AT2940, AT2941; AT2943 OPEN; audit_v891), and the numerical auditor CONFIRMS their numerical account at the 15:47:49Z
    successors (v952); at the identities of the coordinator's 16:05Z note the theory auditor CONFIRMS them again (AT2955, AT2956;
    AT2957 OPEN; audit_v896) and so does the numerical auditor (v955, v956), and again at those of the 16:24Z note (AT2964, AT2965;
    AT2967 OPEN; audit_v899; numerical audit exchange v959). No closure number changes.
15. Far strain (row 3): the exact gap q(c - 137/125) - A_far = 71675071190082633/5629499534213120000 > 0 for the far
    upper A_far = 13396752347393121/9007199254740992 of route F-a, recorded in v13 (AT-1929; numerical audit exchange v532), is
    CONFIRMED again in the second theory agent's T2_PART7_v08 (AT2653, 2026-11-04T11:24:16Z) and in the drafts of this ledger (the numerical auditor
    v946), so the strain condition s_* <= c - A_far/q holds numerically under the retained analytic far premises H-FA
    of row 7; the earlier drafts of v14 had said that it waited on the far upper. H-FA are retained hypotheses, not
    among the six OPEN obligations (AT2912, AT2916).
16. Notation (AT2938 CONFIRMED; numerical audit exchange v948; theory_v26 N-v25-1): A_far is the far upper of items (2) and (3), (B_CE,
    A_CE) = (13/25, 18959/1000) is the CE pair at which closure check version 8 evaluates L_B, and T_S, T_V > 8q =
    84/5 are the cutoffs of Lemma KB; exactly A_far < 3/2 < A_CE and B_CE < 8q. The checked programs keep the three
    roles apart; no budget changes.
17. Rate scope of the FFT-input cuts (theory_v26 N-v25-2; numerical audit exchange v945, v946, v949): the least K_half cuts at the
    assumed u_3 = 10.4, [343.185122, 343.185123] at the plan of record and [116.072962, 116.072963] at the fallback
    (AT2721; AT2720 REFUTES the fallback figure 223), belong to the rooms of NEAR_CHECK_v07, and the FLOAT cut
    displays of numerics_v18 N50.4 belong to the rate tuples of NEAR_CHECK_v06 and v07 (the first numerics agent erratum E51, CONFIRMED
    by numerical audit exchange v949). At the NEAR_CHECK_v09 rooms the same scalar expression gives about 216.36 (plan of record) and
    105.18 (fallback) at the stipulated u_3 = 10.4 (numerical audit exchange v949); u_3 = 10.4 is not a certified value, so these
    figures are HEURISTIC and exclude nothing. The certified necessary test keeps the least integer cuts 195, 164,
    152 (plan of record) and 95, 80, 74 (fallback) of row 8.

None of these changes the verdict.
