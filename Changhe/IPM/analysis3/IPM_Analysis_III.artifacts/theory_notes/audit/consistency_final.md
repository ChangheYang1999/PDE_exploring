# Consistency review of S2_THEORY_18H_REPORT.md and companions (read-only review)

Snapshot: the report and CALPHA, CLOSURE and RESTART at 16:25:05Z; NUMCERT 16:14:38Z; BASIS and C_FUNCTIONAL 16:05:17Z;
the verification report at 16:24:57Z (last record V266). S2_L2_THEORY.md was only spot-checked (it is being edited).
Line numbers refer to this snapshot. A further report edit at 16:28:03Z moved lines by +1 in section 3 and by up
to +5 in sections 5 to 8, and resolved none of A1-A8, D1 or E1 (rechecked). The documents were edited during the
review, and the 16:20Z and 16:25Z updates
already fixed several earlier findings: V256 is now THEOREM (V262), V257 is THEOREM (V265), V264 is integrated, and
m_a >= 3 (V259) appears in every document. Only the residual issues are listed. Proposals are plain ASCII, at most
4 lines each.

## A. Substantive issues, most important first

A1. V266 is not integrated in any document. The record (16:24:57Z) says the actual T alone has an infinite algebraic
cokernel on Z2 AND Z3 (= Z_cof) for every alpha > 1/A_s (this includes every alpha >= 1/10), from exact source cusps.
It is CONFIRMED as an independent derivation with the outside audit pending, so DERIVED in the report's convention.
It covers T only: the Riesz-coupled source differs, so A_0 and L_ren are not covered.
The report still presents Z_cof as the next target without this caveat: L106-109, 3.1 L1121-1129, 3.2 rows L1150
(pure transport at the source, alpha < 1/A, "illustration") and L1162-1163, 6.5 L2213-2215. The same gap is in RESTART
L375 ("audit V261 and V264, then a global inverse on Z_cof") and in CALPHA 3.4(g) and CLOSURE near L474-480.
Proposal (insert after L109 "(DERIVED, V264)."):
  For T alone, Z_2 and Z_cof are not valid targets above the source threshold: T has infinite algebraic cokernel
  on both for every alpha > 1/A_s, so every alpha >= 1/10 (DERIVED, V266, verifier proof, independent audit
  pending). The Riesz-coupled source is different, so A_0 and L_ren are not covered.
New 3.2 row: "| surjectivity of T alone onto Z_2 or Z_cof | none for alpha > 1/A_s (every alpha >= 1/10; source
cusps; A_0, L_ren not covered) | as above | DERIVED (V266, audit pending) |".
6.5 L2214: "its global inverse for A_0 and L_ren is the next open step (T alone is not onto it for alpha > 1/A_s, V266, DERIVED)".

A2. The V257 hypotheses are incomplete in the report, CLOSURE and RESTART.
- V257 and CALPHA L571-572 say: "g compactly supported, even in x, bounded and uniformly C^alpha in y". V257 also
  says the conclusion holds "on bounded x strips".
- Report L104-105 and L1117, CLOSURE L472-473 and RESTART L363 all say only "g bounded and uniformly C^alpha in y".
Proposal (all four places): "for g compactly supported, even in x, bounded and uniformly C^alpha in y, U_1[x^2 g]/x
is in the full joint C^alpha on bounded x-strips".

A3. The definition of DERIVED does not match how the label is used.
- L13 defines DERIVED as "a proof written by the theory author, with independent checking pending".
- Verifier proofs are labelled DERIVED: V261 at L108, L1121 and the L1162 row; V264 at L109 and L1126; the same in
  CLOSURE L474 and RESTART.
Proposal for L13: "- DERIVED: a proof written by the theory author or by the verifier, with independent checking
pending (for a verifier proof: confirmed by its own derivation, outside audit pending)."

A4. Verdict item 4 (L48-57) is stale. It lists the global Hoelder obstructions on Y and Z_sc but not the Z_2
obstruction, which is now a THEOREM (V256, V262, V257, V265).
Proposal (L57): "... and on the scaled isotropic target Z_sc, by a third; and surjectivity onto the scaled
quadratic-axis target Z_2 for every alpha > 1/2, by the simple turning height of the axis rate (sections 2 to 4 and 6.6)."

A5. Header L4 lists V263 as integrated, but neither V260 nor V263 appears in the body.
- Content: the five S1J1 outer columns shifted to t_+ + 1 meet the high input space in dimension 3 and the high graph
  in dimension 2; no single column is high. Inputs only; outputs OPEN.
- The verifier states that V263 is a theory-author cross-review and not a separate audit. It must therefore not be
  called an independent audit.
- team message board L39 and L110 defer the integration until S1J1 lands.
Either drop "V263" from L4, or insert after L151:
  The five outer columns of the S1J1 section, shifted to t_+ + 1, meet the high input space in dimension 3 and the
  high graph domain in dimension 2, while no single column is high (THEOREM, V260, V263; input scope only).

A6. Version stamps disagree. Header L3-5: 16:08Z, updated 16:14Z, 16:20Z and 16:25Z. Section 8 L2263: "This version
gives the status at 16:08Z". Replace with the last header time, for example "at 16:25Z".

A7. Numeric typo. 50/453 - k/3 is 0.0505884..., not "0.050584...". It occurs at report L2144 and CLOSURE L864.
- Recomputed with exact k = 1615536043799051/2^53: 50/453 - k/3 = 0.05058843217.
- The product with 38666592266 is 1956082280.23, so the integer 1956082280 is consistent.
- 1/9.0450253607 - k/3 = 0.0507712, so "theta <= 0.0507" is consistent.
Replace with "0.050588...".

A8. Symbol clash in table 3.2.
- Row L1151 reads "infinity | weighted classes with 2k - 1 < gamma < k". There gamma is the far scaling exponent.
- Rows L1152ff and 3.1 use beta for that exponent and gamma > 4k for the L^2 weight. Both cannot hold at once.
- CALPHA L43 ("2k - 1 < gamma < k") and L363 ("2k - 1 <= gamma") have the same clash and also disagree on < versus <=.
Proposal (L1151): "| infinity | weighted classes with 2k - 1 < beta < k (beta the far scaling exponent) | scaled
C^alpha | DERIVED |", and the same symbol in CALPHA section 3.

A9. Smaller wording issues in 3.1.
- L1119-1120: "alpha <= 1/2 for T and alpha <= 1/2 for A_0 and L_ren are OPEN" should read "alpha <= 1/2 is OPEN for
  T, A_0 and L_ren".
- "One remedy, alpha <= 1/2, is heuristic" is moot for T above 1/A_s once V266 is integrated. Add "(for T alone see V266)".
- L1041: "(... is a THEOREM, V256, V262, and the rest is DERIVED)" should read "(... THEOREM, V256, V262, V257, V265;
  Z_cof, V261 and V264, is DERIVED)".
- CALPHA L969-970, in the V256 status entry: "alpha <= 2/3 for the full operator OPEN" contradicts CALPHA L845
  (1/2 < alpha <= 2/3 THEOREM, V257, V265). Add "(1/2 < alpha <= 2/3 settled by V257, V265)".
- V261 calls the target Z3, but no document uses that name. Add "(Z3 in V261)" at L1121 for traceability.

A10. Margin wording in CLOSURE (minor).
- L817 reads "m_R >= 5/2 for mu~ (THEOREM, V086; first 0.53072 and 1.78605, V077". 0.53072 is the V077 value of m_a,
  not of m_R. Write "first 1.78605, V077 (m_a: 0.53072)".
- Naming: the report uses only m_*; CLOSURE, NUMCERT and RESTART mix m_R and m_* for the same radial margin. This is
  harmless, but one sentence such as "m_R = m_* of Theorem R" in CLOSURE would remove the doubt.

## B. PROMPT section 10 questions

PROMPT 10 has 20 bullets (3 + 4 + 3 + 5 + 5), not 19. The Final closure block of section 0 has no bullet for
"What is already proved?". "Sec 0" gives the short-answer lines; "Detail" gives the detailed-answer location.

| # | Question | Sec 0 | Detail | Status |
|---|---|---|---|---|
| 1 | strongest weighted inverse | L71-76 | 2.1 L449 | OK |
| 2 | older obstructions | L77-80 | 2.2 L531 | OK |
| 3 | consistent domain | L81-83 | 2.3 L548, 2.4 L675 | OK |
| 4 | h directly in C^alpha | L86-111 | 3.1 L974-1135 | STALE (A1, A2) |
| 5 | admissible exponents | L112-116 | 3.2 L1137-1167 | INDIRECT (B5) |
| 6 | Riesz coupling and source | L117-123 | 3.3 L1169-1192 | INDIRECT, minor (B6) |
| 7 | C^alpha(h_x) unnecessary | L124-131 | 3.4 L1194-1230 | INDIRECT (B7) |
| 8 | saddle-adapted local estimate | L134-136 | 4.1 L1234 | OK |
| 9 | nonlocal remainders | L137-141 | 4.2 L1258 | OK |
| 10 | rank-one term | L142-145 | 4.3 L1299 | OK |
| 11 | conforming basis | L148-151 | 5.1, 5.2 | OK (V260/V263, A5) |
| 12 | certified finite inverse | L152-159 | 5.2 L1359 | OK |
| 13 | off-basis residual bounds | L160-161 | 5.3 L1459 | OK |
| 14 | complement | L162-165 | 5.4 L1470 | OK |
| 15 | genuine inverse theorem | L166 | 5.5 L1610 | OK |
| 16 | complete existence theorem | L169 | 6.1 L1617, 6.2 item 6 | OK (CONDITIONAL THEOREM; (I), (S) OPEN) |
| 17 | missing estimate | L170-175 | 6.2 L1620 | OK |
| 18 | what is already proved | none | Verdict L30-43; 6.3 L1787 | INDIRECT; Verdict item 4 STALE (A4) |
| 19 | constants to certify | L176-178 | 6.4 L2032 | OK |
| 20 | closest avenue | L179 | 6.5 L2074 | OK; 6.5 L2213-2215 STALE (A1) |

B5. Insert after L116 "(table in 3.2).":
  Globally no Hoelder target with an inverse is known: on Z_2, T, A_0 and L_ren are not onto for alpha > 1/2
  (THEOREM, V256, V262, V257, V265); T alone is not onto Z_2 or Z_cof for alpha > 1/A_s (DERIVED, V266); Z_cof
  carries the mapping theory for every alpha < 1 (DERIVED, V261).
B6. L122-123: after "(THEOREM, V245, V254)" add ", and on the joint-cofactor target Z_cof (DERIVED, V261)". Make the
same addition in 3.3 L1178-1181.
B7. The V264 finding (the semilinear failure persists in the Z_cof graph norms) is in L108-109 and L1126-1129, but it is
not in this short answer, in 3.4 or in the nonlinear rows of 3.2.
- After "(Lemma N'', THEOREM, V211, V218)" at L129 add "; nor do the graph norms of T, L_ren and A_0 on Z_cof (V264, DERIVED)".
- New 3.2 row: "| nonlinear closure in the graphs of T, L_ren, A_0 on Z_cof | none (N not continuous at 0, J = c = 0) |
  Z_cof graph norms | DERIVED (V264, audit pending) |".
B18. Insert after L169:
  - Already proved. Unconditionally (THEOREMS): Theorem C' and its high variable-order version, the uniform inverse
    theory of the moving-tail family up to (I), the two-norm product bounds, the residual enclosures and the
    obstructions of Verdict item 4. Conditionally: Theorem E (Verdict items 1 to 4; full list in 6.3).

## C. PROMPT 4.5 (Avenue II deliverable)

| Item | Where | Status |
|---|---|---|
| admissible alpha interval | 3.2 L1137-1167; sec 0 L112-116 | OK in 3.2; INDIRECT in sec 0 (B5) |
| exact spaces and constraints | 3.1 L1036-1135 (E_2, Y, Z_sc, Z_2, Z_cof; 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k) | OK except A8 and the Z3 alias (A9) |
| explicit inverse or a priori constants | scattered: S(c) L989; c bounds L1006, L1043; source L^2 bound L1021; exterior cost k/(k - beta) L1087; qualitative constants 6.4 L2062 | INDIRECT (C3) |
| regularity loss | L999-1001 (no derivative of h near 0); source loss L1014-1017; Prop F4 row L1167 | OK |
| role of c[h] | L1003-1006 (strain cancellation, delta^2, V219); L1036 (p + alpha > 1); L1031-1033; L1046-1049; J not closable L1012 | OK |
| required numerical coefficient bounds | scattered: rho~ in C^4 near 0 (S(d), V036); homological denominators > 0.1507 (V214) L1023-1025; d_y rho~ in (29, 30) L1186; y_* and y d_y a (V256) L1111-1112 | INDIRECT (C6) |
| rigorous obstructions | 3.1 S(a)/(b), (v), (vi); Lemmas N, N', N''; 3.2 | OK except V266 (A1) and V264 in 3.2/3.4 (B7) |

C3. Insert after the 3.2 table:
  Explicit constants: S(c) with equality in the sharpness; |c[h]| <= (4/pi) max(1, 1/(p + alpha - 1)) ||h||_{E_p}
  and |c[h]| <= (4/pi) ||h||_Y; the exterior seminorm cost k/(k - beta); the source L^2 bound 1/[1 + (A + mu)/2].
  The constants and radii of the localized and global statements are qualitative (6.4).
C6. New 6.4 row: "| y_* in (9.1465, 9.1468) and y d_y a there; homological denominators > 0.1507; d_y rho~ at the
source in (29, 30); rho~ in C^4 near 0 | Hoelder obstructions, source conjugacy, S(d) | certified (V256, V214, V036) |".
Before adding it, check the record number for the (29, 30) source value against 3.3.

Same-order inverse check: OK. Every Hoelder inverse is stated from a maximal transport or graph domain onto the target:
S(e) L1007-1008, the source L1029-1030, the exterior L1105-1108. Same-class bounds are claimed only for the frozen saddle
and the frozen source (THEOREMS V028, V013, V029) and for the far window (DERIVED). No global or same-order inverse of
A_0 or L_ren is claimed (L109-111, L979-985, 6.5).

## D. Style

The script scan of the report and the six companions found:
- no non-ASCII characters and no em-dashes or en-dashes;
- no local paths (the only hits were "rho~/" and "V~/" inside formulas);
- no team names, "second-model referee", topic numbers or model or person names;
- no hype words (the one hit, "significant (|grad rho~| > 0.3)" at L1506, is technical).
Remaining items:
- D1. Section 8 uses "agent" six times: L2264 "Three agents", L2265 "a numerics agent", L2266 "Each agent", L2269
  "| Agent |", L2276 "each agent", L2277 "the numerics agent". Use "role" or "team"; see E2.
- D2. L2257: "the author's residual, margin, ..." should read "the theory author's residual, margin, ...".
- D3. RESTART L64 has "variable LANE at the top of each script". This is a code identifier, so it is acceptable;
  "the path variable at the top of each script" would avoid the word.
- D4. Verifier records use the word "independent auditor" and topic numbers. Do not copy them: the report and companions currently
  say "independent audit recorded as V262/V265", which is fine.

## E. Section 8 (L2260-2280) against the three shifts logs

All three logs show the loops starting at 00:21:14Z with a 19 h cap.
- Theory author: 00:21:14-06:21:15, 06:21:45-12:21:45, then 12:22:15 to now.
- Numerics team: 00:21:14-03:31:23 (exit 1 after 190 min), 03:31:53-09:31:53, 09:32:23-15:32:23 (360 min), then
  15:32:53 to now.
- Verifier: 00:21:14-06:21:14, 06:21:44-12:21:45, then 12:22:15 to now.

E1. Numerics row L2272 is wrong: it omits the third session's end and the fourth session (NUMERICS_REPORT L87, "a session
(15:33Z-)", agrees with the log), and "09:33" should be 09:32. Replace with:
  | numerics team | 00:21:14 to 03:31:23 (the session ended early, after 190 minutes); 03:31:53 to 09:31:53;
  09:32:23 to 15:32:23; 15:32:53 to the end of the window |
E2. L2264-2266 and L2269: use the roles. For example "Three roles worked concurrently and communicated only through
files: the theory author (...), the numerics team (the Avenue IV computations) and the verifier (...). Each ran in
consecutive sessions of at most six hours." Header "| Role | Sessions |". L2276-2277: "each role ran ...; the
numerics team ran up to four single-thread worker processes".
E3. Verifier row L2273: replace "about 06:21" and "about 12:21" with the logged ends 06:21:14 and 12:21:45. The starts
00:21:18 and 12:22:19 are 4 s after the shift-log starts 00:21:14 and 12:22:15, so either use the log times or say
they are first session-log entries.
E4. Theory-author row L2271 differs from the log by 1-2 s (00:21:15 vs 00:21:14; 06:21:14 vs 06:21:15; 06:21:47 vs
06:21:45; 12:22:17 vs 12:22:15). Use the shift-log times, or add "(session-log times, within 2 s of the shift log)".
E5. The stamp at L2263 is "16:08Z" (A6). The window "00:20:16 to 18:20:16" cannot be checked from the shifts logs
(first entry 00:21:14 in all three), but they do not contradict it. "At most six hours" agrees with the 360-minute
shifts.

## F. Checks that passed (no action)

- m_a: every mention of 2.9270 is framed as superseded by V259 (report L204, L580, L664, L1509, L1624, L1840, L2037;
  CLOSURE L127, L641, L783, L817; RESTART L183; S2_L2_THEORY L546, L1932, L2209). "3.000000" appears only as the
  numerics team's floating value (NUMCERT L80). m_* (m_R) >= 5/2 (V086) is unchanged everywhere.
- V256/V257: THEOREM with V262/V265 in the report (L101-106, L982, L1110, L1116, L1159-1161, L1180, L1820-1821,
  L2212), CALPHA, CLOSURE and RESTART. The phrase "audit pending" no longer appears for either record.
  The thresholds agree: T for alpha > 1/2; A_0 and L_ren for alpha > 2/3 by V256 and for alpha > 1/2 by V257.
- eta_*: 3.866e10 < eta_* < 6.321e129 (V192, V182) is consistent in the report (L46, L172, the Theorem E text, 6.4),
  CLOSURE, BASIS L446, RESTART and NUMCERT. 38666592266 and 1956082280 are consistent (see A7).
- Theorem E: CONDITIONAL THEOREM (V178) with (I) and (S) OPEN everywhere (report L20-43, L169, 6.1, 6.2 item 6; CLOSURE
  section 1 and 5 item 6). No unconditional existence claim was found; "unconditional" is used only for Theorems R and C'.
- Labels of the Y, Z_sc and Z_2 results:
  - Y not onto: THEOREM (V232, V234, V241, V247).
  - Z_sc not onto: THEOREM (V243, V249).
  - Z_2 mapping and exterior inverse: THEOREM (V245, V254).
  - Global Hoelder inverse: OPEN.
  These agree across sections 0, 3.1, 3.2, 3.3, 6.3 and 6.5 and in the companions.
- S1 values agree in the report (5.2, L157, 6.4), NUMCERT L96/L98, BASIS L355-393 and RESTART L204-212: 4.155
  (42 columns), 3.4557/3.456 (52 columns), 2.7655 (S1M4P, 78 columns, V252; 2.7662 on c = 0) and 2.766.
