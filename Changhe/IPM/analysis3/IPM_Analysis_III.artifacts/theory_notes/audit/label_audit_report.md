# Label audit of S2_THEORY_18H_REPORT.md against the verification log

Audited report: S2_THEORY_18H_REPORT.md, version line "2026-10-28T14:34Z", 2004 lines, 216499 bytes.
SHA256: 601e0c70a91f165e78160d3d46a09b72389313ffde1b57d6d9e0af87a40fc456

Version history: the report was replaced several times while the audit ran. Earlier versions audited were 6b58cba7 (1953 lines), 12f874b4 (1973 lines; the first issue of this file, with 13 findings) and e9b9492a (1981 lines). The version above was unchanged for more than three minutes before it was re-anchored, and it was still unchanged at 14:42:54Z. All line numbers below refer to it. When last read, the verification log had records V001 to V228 (3047 lines, SHA256 42a6d5eefc730dc831684eaf5c1e8a444fd8d88326a6669d73af67a349a45439).

Summary: 5 open findings (scope overreach or misattribution 1; cross-audit claim with no record cited 2; superseded but still true bound 1, informational; internal folder name 1, informational). All 13 findings from the 12f874b4 issue are resolved; finding 13 is resolved apart from the folder name, which is carried over as open finding 5. Zero instances found of each of the following:
- a THEOREM resting on a REFUTED or PARTIAL record;
- a cited record missing from the log;
- a wrong V-number;
- an em-dash or en-dash;
- a local path;
- a team name;
- "second-model referee";
- an unconditional existence claim.

## Open findings

1. Lines 1071-1072 and 1077 (scope overreach and misattribution).

   Quotes:
   - "for small delta, against delta^(1-alpha) for the same coupling without the normalization term (V207, sharp for that operator)" (1071-1072).
   - "So in this norm the exact normalization gains the factor delta^(1+alpha)" (1077).

   Records:
   - V207 claims "the normalized localized coupling is O(delta^(3-p-alpha)) on E_p". This is an upper bound for the normalized coupling, and the record says nothing about sharpness. The report's own S(e)(ii) at lines 928-929 attributes the same bound to the normalized coupling.
   - V219: "This improves V207's delta^(1-alpha) bound for the normalized sum; the unnormalized operator still has that slower rate." Its sharpness verdict concerns the delta^2 lower bound only.
   - The V219 proof (Statement, Sharpness, Consequences) proves no lower bound for the unnormalized operator.

   No record supports "sharp for that operator". The factor delta^(1+alpha) is a gain over an upper bound, not over a proved rate.

   Correction:
   - At 1071-1072: "against the earlier bound delta^(1-alpha) of V207 for this coupling, which is the rate the record gives for the operator without the normalization term (V219)". Delete "sharp for that operator", or label that part DERIVED.
   - At 1077: "improves the earlier upper bound by the factor delta^(1+alpha)".

   Line 106 ("against delta^(1-alpha) without the term c[h] X/3 (THEOREM, V219; 4.2)") matches the V219 wording and needs no change.

2. Line 1080 (cross-audit claim with no record cited). Quote: "An independent cross-audit (14:34Z) found no mathematical gap; its remarks are cosmetic, except that the constants are not uniform in alpha and that the sharp part of the norm is the x-seminorm."

   Record V225 (added to the log after this report version): "V219 passes independent scrutiny ... PASS WITH REMARKS, no mathematical gap ... Verdict: CONFIRMED cross-audit outcome." The two remarks quoted in the report agree with the V219 proof: the constants depend on alpha, and the lower bound comes from the x Hoelder seminorm.

   Correction: replace "(14:34Z)" with "(V225)". The time stamp is a detail of the internal workflow, and the claim should cite the record.

3. Lines 959-960 (cross-audit claim with no record cited). Quote: "Independent cross-audits of V213 and of V214 and V215 found no gap."

   Records:
   - V221: "V213 passes independent scrutiny ... PASS WITH REMARKS; no mathematical gap ... CONFIRMED cross-audit outcome".
   - V223: "V214/V215 pass independent model collaboration ... PASS WITH REMARKS, no remaining mathematical correction ... CONFIRMED at the stated localized whole-plane auxiliary scope".

   The claim is correct but cites no record. Line 924 does this properly for S(e) ("V212 for V203 to V206 and V216 for V207 and V208").

   Correction: append "(V221 for V213, V223 for V214 and V215)".

4. Lines 1077-1078 (informational; the bound is true but superseded). Quote: "the Neumann error of the frozen local inverse is O(delta^2) and that of the actual-variable one O(delta^(2-alpha))".

   Records:
   - V219: "The actual-variable factorization error is O(delta^(2-alpha))". The report matches this.
   - V226 (CONFIRMED, added later): the reciprocal-transport multiplier is O(delta^2), so "with V219 the complete actual-variable factorization error is quadratic"; the scope is the actual localized extension only.

   Optional correction: "and that of the actual-variable one also O(delta^2) (V226)".

5. Line 1982 (informational; carried over from finding 13 of the earlier issue). Quote: "lead_work/ (the working notes on the high-norm theory ...".

   This is an artifact folder name, not one of the team names theory author, numerics team or verifier, but it names the internal role. The other role words have been removed: lines 1714 and 1721 now read "A separate floating check" and line 1983 reads "the author's".

   Optional correction: rename the folder in the description, for example "theory_notes/", if the artifact folder can be renamed to match.

## Findings of the earlier issue (12f874b4), now resolved

| # | Earlier finding | Current text and line(s) |
|---|---|---|
| 1 | V184, V185 and V194 tests labelled THEOREM | "CONDITIONAL THEOREM, a necessary test under (I) and (S), V184" (54-55, 1841); "CONDITIONAL THEOREMS, V185, V194" (56); "CONDITIONAL THEOREM, V185" and "CONDITIONAL THEOREM, V194" (1553-1554); "CONDITIONAL THEOREMS for the test, V185 and V194" (1874-1875) |
| 2 | Opening stated leading term x^2 y | "cubic jet (1 + J) x^2 y ... after a scaling its leading term is exactly x^2 y provided \|J\| < 1" (22-23) |
| 3 | Smallness without r <= r_* and the J clause | "K_H eta_0 <= r <= r_*, ... cubic jet (1 + J) x^2 y (leading term exactly x^2 y after a scaling if \|J\| < 1)" (271-273) |
| 4 | V156 with no alpha range | "for alpha < 1/20 (THEOREM, V156)" (252) |
| 5 | V171 alone for the whole interval | "V171 with the affine interpolation of V172" (288-289), "V171 with V172" (1497), "[V171, V172]" (1689), "(V171, V172)" (1837) |
| 6 | Record range "V156 to V163" | "V156 to V161 and V163, with the sign correction of V162" (1446, 1516) |
| 7 | U_2 attributed to V203 | "V203 for U_1/x, V207 for U_2 and the endpoint p = 2" (926) |
| 8 | S(e) cross-audit claim without records | "V212 for V203 to V206 and V216 for V207 and V208" (924) |
| 9 | V117 among "refuted parts" | "the endpoint counterexample of V117" (1769) |
| 10 | "computed once" for the 2.0685e-02 bound | "reproduced independently as a conditional matrix certificate (V200)" (1801) |
| 11 | K identities under-labelled as DERIVED | "THEOREM for these formal identities, V198; scaling covariance V087" (369) |
| 12 | Theorem C' with no record number | "(THEOREM, V047 with V049 to V053, V077, V086)" (1407) |
| 13 | Role words "theory author" | "A separate floating check" (1714, 1721), "the author's" (1983); the folder name is open finding 5 |

## Checked and found consistent

- Task 1: all 79 lines carrying THEOREM, THEOREMS or CONDITIONAL THEOREM with a V-number of 150 or more. Apart from open findings 1 to 3, verdict and scope match the records.
  - Theorem E (V178) as CONDITIONAL THEOREM: lines 20-23, 38-41, 128, 269-273, 1393-1394, 1528-1556, 1698-1703, 1838.
  - High theory:
    - V146 to V150: lines 232, 396, 1442.
    - V151: lines 238, 397, 816.
    - V152: lines 65, 240, 398, 833, 898.
    - V154 and V155: lines 245-246, 843-844.
    - V156 (alpha < 1/20): line 252.
    - V157 and V158.
    - V159 and V160: lines 256, 849-850.
    - V166 with the sign of V167.
    - V168, V169 and V170, with the inverses conditional on base injectivity: lines 261-267, 1520-1527.
    - V175, V176 and V177: lines 1543-1544, 1528.
  - Residual norms:
    - V164 (6049.11 to 8601.42): lines 280, 1454.
    - V174 and V179 (3.270 to 485.632): lines 291, 1501.
    - V182 and V192 (3.866e10 < eta_* < 6.321e129): lines 274, 294, 1547.
    - V197 (2.9270): line 517.
    - V172: lines 290, 1499.
  - Hoelder origin theory:
    - V203 to V208: lines 923-935, 969-970, 1005.
    - V210 (66 and 60 columns): line 1232.
    - V211 (graph-only scope) with V218 (semilinear map only; quasilinear scheme not excluded): lines 96, 979, 1016-1025.
    - V219 (c_0 delta^2 <= norm <= C delta^2 on E_2, fixed alpha < 1, actual C^(4,1) background): lines 105-107, 930, 971, 1069-1070.
  - Source theory, V213 to V215 (unnormalized, localized whole-plane extension, strain column only as prescribed forcing, X_alpha unboundedness of c with no source-graph assertion, as V221 requires): lines 91, 943-960, 974-975, 986.
  - V217: line 1952.
  - The 6.3 list entries for V180, V181, V184, V185, V190, V194, V198 and V199 use the record verdict wording, refuted parts included.
  - The report makes no compact-patching claim that V227 would contradict ("no global patching", line 959; "A global Hoelder treatment of the coupling is OPEN", line 989).
- Task 1 spot check of 26 THEOREM citations of V001 to V149, all matching their records.
  - Section 1:
    - V002 (334).
    - V018 (340).
    - V005 (346-347).
    - V036 (348): C^{4,1}, not C^5.
    - V017 (352).
    - V038 (363).
    - V002 and V008 (366).
    - V087 (369, 373): index -1.
    - V025 and V038 (376).
  - Section 2:
    - V022 (400): the refuted pointwise reading is stated.
    - V011, V021 and V024 (420-428).
    - V064 (426): 3.5785.
    - V023 and V031 with V077 (430).
    - V077 and V086: 1.78605 and 5/2.
    - V032 (445).
    - V025 N1 (449): "strictly" marked REFUTED.
    - V041 (489): stated under (A).
    - V047 with V049 to V053.
    - V046 Lemma C'2 (522): kappa_* >= 5/2 by V086.
    - V067 (613, 623).
    - V063, conditional with (Z) from V080 (626-635).
    - V070 (641).
    - V079 (654).
    - V103 and V104 (667).
    - V110 (278).
    - V126, V129, V130, V132, V141 (as CONDITIONAL THEOREM) and V144 (211-230, 394-395).
  - Section 6:
    - V092 (1410).
    - V086 (1788).
    - V090 (1797).
    - V087 (1639; the THEOREM label for the index and scaling statements, with the onto theorem on {J = 0} REFUTED, is at 1126-1128 in section 4).
- Task 2: every other THEOREM label has a V-number in the same item. The following are exempt:
  - The label definitions (lines 8, 10).
  - The section 0 short answers that cite a section number, as line 8 allows (68, 75, 78, 80, 89, 93, 101, 104, 109).
  - The 6.3 heading.
  - Lines 29 and 869, whose items carry their V-numbers on the following lines.
- Task 3, style:
  - 0 em-dashes, 0 en-dashes and no non-ASCII characters.
  - No /mnt, /home, /tmp or /Users. The matches at 564, 568 and 1123 are the notation "rho~/".
  - No theory author, numerics team or verifier. The single pattern match, "S2_NUMERICAL_CERTIFICATES.md" at 1969, is a companion file name.
  - No "second-model referee".
  - No standalone word "theory author" outside the folder name of open finding 5.
- Task 4: the report never claims unconditional existence. Lines 19-25, 38-41, 128, 269-273, 1393-1394, 1533-1556, 1698-1703 and 1838 all state conditional existence under (I) and (S), with both hypotheses OPEN. Line 1512 is the abstract iteration theorem of V062, which the record also states conditionally.
- Citations: all 218 distinct V-numbers cited in the report exist in the log, and the highest cited is V219. Records V220 to V228 are not cited. Of these, V221, V223 and V225 would back open findings 3 and 2, and V226 open finding 4.
