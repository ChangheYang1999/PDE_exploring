# Prompt-consistency audit of S2_THEORY_18H_REPORT.md

Report audited: S2_THEORY_18H_REPORT.md, 2004 lines.
Version line (line 3): "Version of 2026-10-28T14:34Z. This report is self-contained. Proofs, computations, code and data are in the"
SHA256 of the audited file: 601e0c70a91f165e78160d3d46a09b72389313ffde1b57d6d9e0af87a40fc456

Note on the snapshot. The file changed while this audit was running. At the start it had 1995 lines and SHA256
fc81144cf7b9ba059108c59ffa0495dd979f96e57c71147ec6b5e73f34371e3e. It was rewritten at 14:37:40Z to the version above,
and the version line was not changed. Every line number below refers to the 601e0c70 version, which stayed the same for
the rest of the audit. Three earlier observations are already fixed in this version: V219 is in section 0 (lines
103 to 107), V210 is in section 0 (lines 114 to 116), and the semilinear scope of Lemma N'' is in 3.4 (lines 1023 to 1025).

Sources checked: PROMPT.md sections 3.6, 4.5, 5.5, 6.8, 7, 10 and 11. Verifier records V200 to V226. Records V222 to V226
are newer than the scope given for this audit; V225 and V226 are dated 14:38:37Z, which is after the version stamp.

## Findings

Severity: H means a contradiction or an overclaim that a reader would act on. M means stale or understated content,
or a label that does not match the evidence. L means presentation.

1. (H) Section 0 contradicts itself on Hoelder inverses. Line 46 to 47: "Ruled out, each by an explicit counterexample
   confirmed by the verifier: bounded inverses in isotropic, radial and Hoelder formulations". Lines 79 to 80 of the same
   section say "the localized whole-plane operator is invertible on C^alpha_2 for every alpha < 1 (THEOREMS ...)", and
   lines 89 to 91 give source inverses on C^alpha intersected with L^2 (V203 to V207, V213 to V215). What V028 rules out
   is the isotropic C^alpha inverse at the saddle for alpha > 1/D, together with the conjugacy transfer and the
   indicator cutoff. It does not rule out Hoelder inverses in general.
   Suggested replacement: "Ruled out, each by an explicit counterexample confirmed by the verifier: bounded inverses in
   isotropic L^2 and radial formulations, the isotropic C^alpha inverse of the frozen saddle for alpha > 1/D = 0.0469,
   the transfer of the frozen Hoelder estimate by a conjugacy, a fixed cubic coefficient (index -1), ..."

2. (H) Section 0 overstates the nonlinear Hoelder obstruction. Lines 147 to 148: "a series of sharp negative results,
   each with an explicit counterexample, that rule out isotropic, radial and Hoelder formulations of the nonlinear
   problem". The record scopes are narrower. V048 says Lemma N does not refute a stronger quasilinear norm. V218 limits
   Lemma N'' (V211) to the fixed semilinear maps N and L_delta^{-1} N and says "This does not exclude a quasilinear
   scheme absorbing U[h].grad into the transport". As worded, the sentence turns an obstruction to one method into a
   claim that a whole class of formulations is impossible, which conflicts with PROMPT section 11 ("Do not confuse the
   absence of a proof with a proof of nonexistence").
   Suggested replacement: "a series of sharp negative results, each with an explicit counterexample, that rule out
   isotropic and radial formulations and every semilinear perturbative fixed-point map in Hoelder solution norms,
   including the C^alpha_2 graph of the localized origin inverse (V030, V211); a quasilinear Hoelder scheme that
   absorbs U[h].grad into the transport is not excluded (V048, V218);"

3. (M) The section 0 answer to "Is C^alpha(h_x) genuinely unnecessary?" leaves out the V218 scope that the body now
   states. Lines 95 to 96: "Hoelder solution norms alone cannot close it (Lemmas N and N', THEOREMS), and this persists
   in the C^alpha_2 graph of the localized origin inverse (Lemma N'', THEOREM, V211)". The body at lines 1023 to 1025
   restricts this to "the semilinear perturbative fixed-point map on balls of this graph". Lines 1943 to 1944 in 6.5
   repeat the unqualified form: "Lemmas N and N' show that Hoelder norms alone cannot close the nonlinear problem (in
   that very graph too, Lemma N'', V211)".
   Suggested replacement for lines 95 to 96: "no for a semilinear perturbative map: Hoelder solution norms that control
   C^alpha of h, U[h] and c do not close it (Lemmas N and N', THEOREMS), nor does the C^alpha_2 graph of the localized
   origin inverse (Lemma N'', THEOREM, V211, V218); a quasilinear iteration that absorbs U[h].grad into the transport is
   not excluded;". Make the same change at lines 1943 to 1944.

4. (M) The section 0 summary of the off-basis method says more than the body. Line 121: "Off-basis residual bounds.
   The method is proved". The body at line 1243 says "Method (DERIVED, structure confirmed in V020 and V027)". V020 and
   V027 confirm the tail-compensation and matrix identities and the listed repairs. Neither confirms the Gram-converted
   off-basis bound ||(I - Q_M) L P_N|| <= |t^|_2/(1 - ||E||_inf)^{1/2} as a whole.
   Suggested replacement: "Off-basis residual bounds. The method is DERIVED (its algebraic ingredients are confirmed in
   V020 and V027); no off-basis bound has been computed at this version (5.3)."

5. (M) A section 0 label covers the far end, whose result is only DERIVED. Line 78: "At each end of the flow, yes, in
   anisotropic classes (THEOREMS)". Line 93: "For the low-order linear theory, yes at each end (THEOREMS)". The body
   marks the far window DERIVED: table 3.2, line 977, "infinity | weighted classes with 2k - 1 < gamma < k | scaled
   C^alpha | DERIVED", and line 1003, "the far window (DERIVED)". Line 137 ("exact frozen inverses at the three ends
   of the flow (origin saddle, source points, infinity), with explicit constants") and line 1821 ("Every frozen piece
   is proved with explicit constants: ... the far window") have the same problem.
   Suggested replacement for line 78: "At the origin saddle and the source points, yes, in anisotropic classes
   (THEOREMS); at infinity in scaled weighted classes (DERIVED)." Make the corresponding change at lines 93, 137 and
   1821.

6. (M) The answers to "What is already proved?" leave out the newest confirmed results. Section 0, "What is
   established" (lines 136 to 171), does not mention S(e) (V203 to V207: localized origin inverses on C^alpha_2 for
   every alpha < 1, including the actual transport), the sharp delta^2 normalized coupling (V219), the actual
   variable-source inverse on C^alpha_b intersected with L^2 (V213 to V215), or the conformity classes of the pure
   section (V210, V220). In the body, 6.3 line 1573 reads "Hoelder: H0 and S(a) to S(d), sharp thresholds [V028];
   Lemmas N and N' [V030]." and line 1574 lists only V014, V039, V040 and the code audits under "Finite basis". The
   obstruction list at line 1768 leaves out V201, V203, V208, V211, V213, V217 and V210, although the checklist row at
   line 1957 includes them.
   Suggested addition to section 0 after line 167: "- localized Hoelder inverses near the origin, from the maximal
   domain onto C^alpha_2 for every alpha < 1, with the complete normalized coupling and the actual transport on
   B_(delta/2) (V203 to V207), where the normalized coupling has E_2 operator norm comparable to delta^2 (V219), and a
   whole-plane inverse on C^alpha_b intersected with L^2, from the maximal transport domain, for an extension equal to
   the actual unnormalized source operator on B_(delta/2) (V213 to V215); constants qualitative;". Suggested
   replacement for line 1573: "- Hoelder: H0 and S(a) to S(d), sharp thresholds [V028]; Lemmas N and N' [V030];
   corrected strain factor [V201]; S(e) [V203 to V207, cross-audits V212, V216]; sharp normalized rate [V219]; J not
   closable in the E_2 graph, relative density [V208, V216, V217]; Lemma N'' [V211, V218]; source inverses on
   C^alpha_b intersected with L^2 [V213 to V215, cross-audits V221, V223]." Add "[V200, V202, V210, V220]" to the
   finite-basis item at line 1574, and add V201, V203, V208, V211, V213, V217 and V210 to the list at line 1768.

7. (M) The body cites an audit by its time and not by its record, and one rate it gives is now superseded. Line 1080:
   "An independent cross-audit (14:34Z) found no mathematical gap". At the version stamp, V221 still lists V219 as
   "separately pending". The audit is recorded later as V225 (14:38:37Z). The header (lines 3 to 5 and 9) says records
   are cited by number. Line 1078, "that of the actual-variable one O(delta^(2-alpha))", is improved by V226 (14:38:37Z,
   CONFIRMED) to O(delta^2). This is after the version stamp, so it is not an error at 14:34Z, but it will be stale at
   the next revision.
   Suggested replacement: "An independent cross-audit found no mathematical gap (V225) ...", and "the Neumann error of
   the frozen local inverse is O(delta^2), and that of the actual-variable one is also O(delta^2) (V226)".

8. (M) Some section 0 inverse statements give no domain, which PROMPT section 11 requires ("Every inverse statement
   must specify the operator domain and range"). Line 80: "the localized whole-plane operator is invertible on
   C^alpha_2". The body (line 933) says "invertible from its maximal domain onto E_2". Lines 89 to 91: "also with the
   actual variable source transport and coupling on a neighbourhood of P, in C^alpha intersected with L^2". The proved
   statement (lines 954 to 956, V215) is a whole-plane inverse of an explicit extension that equals the actual operator
   on B_(delta/2). It is not an inverse on a neighbourhood. Line 106, "its norm on B_delta is comparable to delta^2",
   should name the operator norm E_2 -> E_2 (line 1071).
   Suggested replacements: line 80, "is invertible from its maximal domain onto C^alpha_2 for every alpha < 1 and
   small delta"; lines 89 to 91, "also, for every alpha < 1, as a whole-plane inverse from the maximal transport
   domain onto C^alpha_b intersected with L^2 of an explicit extension that equals the actual variable unnormalized
   source operator on B_(delta/2) (THEOREM, V213 to V215)"; line 106, "its E_2 -> E_2 operator norm is comparable to
   delta^2".

9. (M) The checklist in 6.6 has not been updated for the Hoelder results. The row "Every inverse states its domain and
   range" (line 1952) leaves out the frozen Hoelder saddle inverses, S(e) (maximal domain -> E_2) and the source
   inverses of V213 to V215 (maximal transport domain -> X_alpha). The row "Normalization meaningful and closed" (line
   1954) lists V012 and V032. It does not record that J is not closable in the E_2 graph (V208), that smooth inputs
   are dense only in the relative sense (V216, V217), or that c is unbounded on X_alpha (V213). These are the
   topologies of the Avenue II inverses, and they are why those inverses are stated with J unnormalized (S(e)) or with
   the operator unnormalized (V215).
   Suggested addition to line 1954: "; in the Hoelder realizations J is not closable in the E_2 graph (V208; the smooth
   kernel of J and c has the same graph closure as the smooth c = 0 domain but is not dense in the whole maximal graph,
   V216, V217) and c is unbounded on C^alpha_b intersected with L^2 (V213), so the Avenue II inverses carry no closed
   cubic normalization". Add "S(e) (maximal domain -> E_2, V207, V206); source on X_alpha (maximal transport domain ->
   X_alpha, V213, V215)" to line 1952.

10. (L) The answer about basis conformity mixes two sections. Lines 114 to 116 say "Its exact jet joins are C^3 at the
   two junctions; of the 78 pure spline columns all are low-conforming, 66 lie in the high input space and 60 in the
   high graph domain". V220 limits V210 to exactly the 78 pure columns: "the 169-column jet-joined section is
   separate". The first clause describes the S0 basis. The second describes the pure S_1 section.
   Suggested replacement: "Yes for the low realization, in its repaired form (5.1). For the high realization of
   Theorem E, the 78-column pure spline section meets the high input space in 66 columns and the high graph domain in
   60 (THEOREM, V210, V220; 5.2). The high conformity of the 169-column jet-joined sections is not classified."

11. (L) Section 0 does not answer two of the five final-closure questions under its own heading. The block "Final
   closure (section 6)" (lines 127 to 134) answers questions 1 and 2. "What is established" (line 136) answers question
   3. Nothing in section 0 answers "Which constants or inequalities require numerical certification?" (the answer is
   only the table in 6.4, lines 1777 to 1816). The closest-avenue answer is in "In brief" item 5 (lines 50 to 58),
   outside the answers block.
   Suggested addition after line 134: "- Constants requiring numerical certification. The finite-rank split constant
   delta, the adjoint defects and witness norms of INJ-Q, the axis suprema M_20, M_21, M_40, M_41 and the lift bounds,
   r_*, K_H, K_L, C_B, C_V and a realistic high residual norm eta_* (table in 6.4). - Closest avenue. Avenues I and III
   together, with Avenue IV used only for the complement (item 5 above; 6.5)."

12. (L) Table 6.4 does not list the constants of the new Hoelder results. V203 and V204 record "No constant C or
   cutoff radius is numerically certified". V215 and V219 record qualitative delta and C. Table 6.4 has no row for
   C_B, C_H, the origin cutoff radius delta, or the source radius delta of V215.
   Suggested row: "| C_B, C_H, origin cutoff radius delta (S(e), V203 to V207, V219); source radius delta (V215) |
   Hoelder localized inverses | qualitative, not computed; OPEN |".

13. (L) The artifact list in section 7 is out of date. Line 1965 reads "S2_CALPHA_THEORY.md: the Hoelder theory (H0,
   S(a) to S(d), the source, Lemmas N and N')." The companion's version line shows that it now also contains S(e), the
   source theory on C^alpha intersected with L^2, the relative density statement, the delta^2 rate and Lemma N''.
   Suggested replacement: "S2_CALPHA_THEORY.md: the Hoelder theory (H0, S(a) to S(e), the sharp normalized origin
   rate, the source theory including C^alpha_b intersected with L^2, Lemmas N, N' and N'')."

14. (L) The section 0 short answer for the certified finite inverse (lines 117 to 120) leaves out V200. The no-TAU S0
   bound sigma_min >= 0.020685, reproduced directly at 384 bits, is in 5.2 (line 1163) and in 6.4.
   Suggested addition: "...(V066), sigma_min >= 2.0685e-02 for the same section without TAU (V200), and sigma_min >=
   0.510914 ..."

15. (L) Notation and wording. Section 0 writes the high residual norm as eta_H (lines 39 and 43) and as eta_* (line
   44). Theorem E in the body uses eta_0 = ||f_0||_(Y_full) (lines 271 and 1530 onward). Suggest using eta_0 in the
   statement of (S) at line 39 and keeping eta_* only for the fixed equivalent norm. Line 124, "is estimated at of
   order 1e4", should read "is estimated to be of order 1e4".

16. (L) Version stamp. The content changed after 14:34Z (14:37:40Z rewrite; see the note above) and line 3 was not
   updated. Suggest bumping the stamp whenever the content changes.

17. (Informational, outside the V200 to V221 scope.) V222 and V224 (CONFIRMED, before the version stamp, with independent
   audits still pending) give a common weighted target Y = E_2 intersected with L^2(w_gamma), bounded cutoff solution
   maps (V222), a bounded global renormalized coupling with a closed maximal Y graph, and non-closability of J in that
   global graph (V224). The report does not cite them. This is defensible while the audits are pending. When they are
   integrated, the Riesz-coupling answer (line 92, "A global Hoelder treatment is OPEN") should say that the global
   coupling is bounded on this common target (V224) and that a global Hoelder inverse remains OPEN.

Style (task 4). No violations found. There are no local paths (/mnt, /home, /tmp), no team names, no "second-model referee", no
em-dashes or en-dashes, no non-ASCII characters and no ASCII double hyphens. Grep hits on "team" all come from "plane".
"robust" (lines 840, 1441, 1674) and "significant" (line 1286) are used in their technical sense, not as hype. Companion
file names such as S2_C_FUNCTIONAL.md are artifact names listed in section 7, not local paths.

Labels (task 3). Every THEOREM in section 0 maps to a CONFIRMED verdict: V022, V028, V030, V034, V038, V039, V047 with
V049 to V053, V055, V062, V063 with V080, V073, V076, V077, V086, V087 (index part), V151, V152, V164, V170, V174, V175,
V176, V179, V182, V192, V203 to V207, V210, V211, V213 to V215 and V219. V069 is cited for its counterexample, which is
the confirmed part. The only label problem is finding 5, where the THEOREMS label covers the far window, which is
DERIVED.

## Table of the 21 required questions

Lines refer to the 601e0c70 version. "Answered" rates the section 0 answer.

| No. | Question | Answered | Section 0 lines | Body lines | Consistency notes |
|---|---|---|---|---|---|
| I.1 | Strongest weighted inverse estimate | yes | 63-68 | 385-463 (2.1) | consistent |
| I.2 | Older obstructions still applying | yes | 69-72 | 465-480 (2.2) | consistent |
| I.3 | Consistent domain | yes | 73-75 | 482-605 (2.3), 606 on (2.4) | consistent |
| II.1 | Direct C^alpha control of h | yes | 78-82 | 904-961 (3.1) | domain not stated (8); far end labelled THEOREM (5) |
| II.2 | Admissible exponent range | yes | 83-87 | 963-980 (3.2) | consistent; 0.5227 correctly marked REFUTED as a barrier |
| II.3 | Riesz coupling and source | yes | 88-92 | 982-999 (3.3), 943-960 | "on a neighbourhood of P" imprecise (8); V224 not yet integrated (17) |
| II.4 | C^alpha(h_x) unnecessary | yes | 93-97 | 1001-1035 (3.4) | V218 semilinear scope missing in section 0 (3); far end label (5) |
| III.1 | Saddle-adapted local weighted estimate | yes | 100-102 | 1039-1061 (4.1) | consistent |
| III.2 | Absorbing nonlocal velocity remainders | yes | 103-107 | 1063-1097 (4.2) | V219 integrated; audit citation and V226 rate (7) |
| III.3 | Rank-one reduction | yes | 108-111 | 1098-1141 (4.3) | consistent |
| IV.1 | Finite basis conforming | yes | 114-116 | 1144-1157 (5.1), 1229-1241 | two sections conflated (10) |
| IV.2 | Finite inverse certified | yes | 117-120 | 1158-1241 (5.2) | V200 omitted (14) |
| IV.3 | Off-basis residual bounds | yes, overstated | 121 | 1242-1252 (5.3) | "proved" against DERIVED in body (4) |
| IV.4 | Infinite-dimensional complement | yes | 122-124 | 1253-1385 (5.4) | consistent |
| IV.5 | Genuine inverse theorem | yes | 125 | 1386-1390 (5.5) | consistent |
| F.1 | Complete nonlinear existence theorem | yes | 19-26, 128 | 1393-1395 (6.1), 1530-1557 | consistent |
| F.2 | Precise missing estimate | yes | 129-134 | 1396-1557 (6.2) | consistent |
| F.3 | What is already proved | partial | 136-171 | 1558-1776 (6.3) | newest results V200 to V221 missing in section 0 and 6.3 (6); Hoelder ruled-out overstatement (2) |
| F.4 | Constants needing numerical certification | partial | 129-131 (implicit only) | 1777-1816 (6.4) | no explicit section 0 answer (11); Hoelder constants missing from 6.4 (12) |
| F.5 | Closest avenue and why | yes (outside answers block) | 50-58 | 1817-1946 (6.5) | lines 1943-1944 lack V218 scope (3) |

Summary: 17 findings: 2 H (1, 2), 7 M (3 to 9), 7 L (10 to 16) and 1 informational (17). 19 of the 21 questions have
an explicit section 0 answer. F.3 and F.4 are partial.
