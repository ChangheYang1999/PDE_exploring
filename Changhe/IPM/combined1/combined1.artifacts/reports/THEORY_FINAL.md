# THEORY_FINAL (batch T): a posteriori theory for the S1 / IPM case 4 profile

Version final (18:25Z; batch T final, draft 65; N4-433; H18 defaults on the frozen matrix v170 copy), UTC
2026-10-29T18:25Z.

Author the T1/T3 theory worker (batch T publisher, agents T1 and T3), written from the batch T record: theory_v01 to theory_v07
(working file theory_requirements (not published); theory_v07 published 2026-10-29T11:20Z, sha256 42eb222a38caadac...), the T4 theory auditor ledger
through T4-504 (verdict ledger entry of 18:23:51Z, with the full audits of theory_v04, of draft 12, of drafts 15, 17 and
21 (T4-336, T4-341, T4-347), of draft 24 (T4-358), of the published theory_v06 (T4-373), of preview1 of theory_v07
(T4-399), of the published theory_v07 (T4-412), of draft 34 (T4-433, sha256 febf6c09...), of draft 38 (T4-442, sha256
ccaa8623...), of drafts 39 and 43 (T4-453, T4-456), of preview1 and preview2 of theory_v08 (T4-445, T4-455), of the
published theory_v08 with draft 52 (T4-471), of draft 53 (T4-482, sha256 51647b68...) of draft 55 (T4-487, sha256
aa2d3063...) of draft 58 (T4-493, sha256 f76c41fb...) and of draft 60 (T4-497, sha256 8bac7dfc...) in
research/theory_v04_audit, research/theory_final_h12_audit, research/theory_final_draft15_audit,
research/theory_v06_draft_audit, research/published_v06_audit, research/theory_v07_audit, research/published_v07_audit,
research/theory_final_draft34_audit, research/theory_final_draft38_audit, research/theory_final_draft39_audit,
research/theory_final_draft43_audit, research/theory_v08_preview1_audit, research/theory_v08_preview2_audit,
research/theory_v08_published_audit, research/theory_final_draft53_audit, research/theory_final_draft55_audit,
research/theory_final_draft58_audit and research/theory_final_draft60_audit), the N4 numerical auditor ledger through N4-332 (the N4 numerical auditor
verdict ledger; N4-333 to N4-433 as summarized in closure matrix v170, 18:22Z, with N4-381 to N4-433 also read in the
ledger), the T2 theory worker notes/the T2 final summary, its handoff through section BV (18:18Z) and its reviews (through
the review of T4-402, the review of T4-410, the review of T4-414, the review of T4-415 (sha256 ee7b1b1b... of 12:37Z), the review of T4-459
(sha256 e140e6c0... of 14:55Z), the review of T4-458 (sha256 ca936460... of 15:06Z) and the review of T4-462 (sha256 2cb6f7e6... of
15:15Z) and the review of T4-469 (sha256 cfe759ad..., written 15:59Z, revised 16:04Z; revision 2, 3eb37f0f..., 16:28:35Z,
accepted in T4-489), the review of T4-474 (620c2928..., 16:28:42Z) and the T2 check of T4-479 (sharpw max) (dae1f389..., 16:35:59Z) and
The T2 check of T4-479 (report repair) (d9f9e96f..., 16:49:15Z; accepted in T4-489) and the T2 check of N4-017 (residual identity)
revision 1 (2ce07426..., 18:14:51Z; accepted in T4-503); the review of T4-414 is the 12:08Z save 221b1135..., restored after
the 12:12Z incident, with the review of T4-381 and T4-384 revision 2 and the review of T4-375 revision 2; and its check the T2 theory worker
The T2 falsification review of the endpoint and the report summary of draft 36, revision 2, sha256 660b089b... of 13:42Z, which makes the wording repairs of
T4-443, the audit of revision 1, CHECK_T1_v08_FACTORS revision 2, sha256 09e274f6..., and the FALSIFY revision 3 note of
handoff BI, sha256 de588453..., CONFIRMED by the T4 theory auditor in T4-464), the N1/N2 numerics worker snapshot INDEX through C1-N1-028 with
numerics_v06 to numerics_v16 (16:06:03Z, the final batch N version), and the T1/T3 theory worker reviews R1-001 to R1-054
(review set 54; review set 52 and review set 55 have errata only) with the errata of review set 23, review set 27, review set 30,
review set 35, review set 36, review set 37, review set 43, review set 47, review set 48, review set 49, review set 50, review set 51,
review set 52 and review set 55. The coordinator notes are read through 18:14Z. This is the batch T final for the 19:00Z
collection; a later correction would go into a the T1/T3 theory worker team note. Sources for every statement are named inline; the frozen
texts are the reference.

Here the run directory = working file r6 (not published) and A2 = source data (read-only, not included): analysis2/IPM_Analysis_II.artifacts; section
numbers "A2 Pn" refer to A2/S1_CLOSURE.md.

Status labels (the run contracts section 0, Amendment v03). A2-THEOREM: proved in analysis2. AUDITED: a proof written by one
lane and checked step by step by another (only A2-THEOREM and AUDITED results are called proved here). AUDITED
conditional: an implication that is proved, whose hypotheses are not verified for any candidate. CLAIMED: proof
written, not yet reviewed by another lane. CONFIRMED: a number reproduced independently. OPEN: not decided.
HEURISTIC: an argument without proof. FLOAT: a floating-point value without enclosure. REFUTED: shown false.
RULED OUT: an AUDITED result with CONFIRMED numbers shows that a framework cannot be applied to a reference within
its exact assumptions. When the failed hypothesis is a sufficient one (smallness, a background inequality), RULED OUT
says nothing about existence of a profile.

## 0. Direct answer

1. No closure. No reference profile of the campaign is shown to satisfy the hypotheses of any registered existence
   theorem. For every snapshot C1-N1-001 to C1-N1-010, C1-N1-012 and C1-N1-013 and every A2 reference (state 131, d2,
   Mpen2, b6) the closure matrix (since v101; v140 at this draft) records RULED OUT in each framework of its rows (the
   A2-type balls, the T4L2 balls and the graded boxes), by point gaps, by the fixed-c L^2 distance or by a failed
   hypothesis. The one exception is row 34 (state 131 in the weighted low space of T4-022), which is OPEN as a route
   only: it has no high inverse or nonlinear estimate, so it is not a closure theorem. FW-T-DYADIC-Y-v1 is RULED OUT at
   state 131, d2, 007, 008, 009 and 010 (008 and 009 by N4-186 and N4-187, CONFIRMED by T4-248, T4-250 and N4-193; 010
   by N4-231, CONFIRMED by T4-303 and N4-244, matrix row 79) and at 016 (N4-355: The N4 numerical auditor's own complete computation of the
   mode 1 and 3 norms J(1/4) and J(7/4), which independently verifies the N3 numerics worker's CLAIMED seven-cell record; minimum ratio
   above 1.253908386497; conditional on the hypotheses of the origin inverse theorem; matrix row 98, v126), and at 015
   and 017 (next sentences); it was not evaluated at the other references (T4-219). At 015 the N4 numerical auditor's N4-382 (14:11Z)
   independently reproduces the N3 numerics worker's seven-cell record of 13:27Z (exact mode 1 and mode 3 projected energies, every
   contributing background mode retained, 2048 bits): every cell fails, minimum ratio above 1.242922259074, CONFIRMED
   under the hypotheses of the FW-T-DYADIC-Y-v1 argument; closure matrix row 105 (v135) records 015 RULED OUT in
   FW-T-DYADIC-Y-v1 for every 0 < a < 2, 0 < s < 1 and finite Rw under the audited framework hypotheses and the
   candidate hypotheses checked in N4-382. The T4 theory auditor's T4-461 (14:52Z) reproduces N4-382 independently (739 checks). At 017
   the N4 numerical auditor's N4-389 (14:56Z) CONFIRMS the N3 numerics worker's seven-cell record (CLAIMED, 14:22Z) by its own complete computation of
   J(1/4) and J(7/4): under the same hypotheses every cell of 0 < a < 1 + 1/c fails, minimum ratio above 1.221854480167
   (two-evaluation cover); closure matrix row 106 (v138) records 017 RULED OUT in FW-T-DYADIC-Y-v1 on this basis, one
   sufficient scheme removed, not a profile; the T4 theory auditor's T4-463 (15:05Z, 1070 checks at 1024 bits) CONFIRMS N4-389
   independently, so row 106 is accepted both ways (v139). C1-N1-010 is excluded from every ball, the statL and bL balls
   included, by its CONFIRMED distance above 0.022479506978 (N4-205, T4-270, N4-215). C1-N1-013 (design experiment, not
   a certification target) is excluded by its held-out distance above 0.00199234339 (T4-255, CONFIRMED by N4-204), 4.357
   times the graded ceiling, and its point gaps (N4-201, CONFIRMED by T4-266 and N4-208). C1-N1-014 (design experiment)
   is RULED OUT in every point-tested ball and original graded box by its point gaps (N4-213, CONFIRMED by T4-279), and
   its distance above 0.00198301351067 (N4-214, CONFIRMED by T4-280) exceeds every registered ceiling, so it is RULED
   OUT in the statL and bL balls too. C1-N1-015 (conditioning control, registered 06:18:19Z, structure CONFIRMED by
   N4-233 and T4-306) is RULED OUT in every registered scalar ball and graded box by its point gaps (N4-234, CONFIRMED
   by T4-299) and its held-out distances above 0.000351804115950603 at (19, 600) (T4-298) and above 0.001232449584356253
   at (23, 600) (N4-237, CONFIRMED by T4-304 and N4-245); the second alone exceeds the graded ceiling. C1-N1-016 (design
   test of mid-field resolution, registered 06:46:04Z) fails the point test at (1/10, 73/100) for all six registered
   scalar budgets and the original graded box (N4-242, CONFIRMED by T4-307): matrix row 81 is RULED OUT, and row 80 is
   RULED OUT in its point-tested balls (N4-251 accepts T4-307). Its held-out distances above 0.001092633159 at the
   registered probe (23, 2400) and above 0.001470360924 at (19, 1800) (N4-246, CONFIRMED by T4-310 and T4-311, both
   accepted in N4-253; matrix v66) exceed every registered ceiling, so 016 is RULED OUT in every ball of rows 80 and 81,
   the statL and bL balls included; T4-313 and N4-258 CONFIRM its sector prefix, and T4-321 CONFIRMS its exact potential
   rank 2174 (N4-248). C1-N1-017 (scale comparison at R0 = 50, registered 07:11:15Z with numerics_v09) is RULED OUT in
   every ball of rows 82 and 83, the statL and bL balls included (matrix v70, 07:32Z): its exact structure and its
   positive gaps for every registered point budget (F(1/10, 73/100) = 0.0899392743, uniform graded gap 0.0695362257;
   N4-254, CONFIRMED by T4-319 along an independent polar path), its sector prefix (nonzero sectors down to
   exponent -7/2 exactly (4, 1), (9, 0), (5, 1), (1, 2) and (10, 0); T4-323), the objective-span separation of its
   registered probes (N4-255) and its held-out distance above 0.001068502321536437 at (23, 2400) (N4-256, CONFIRMED by
   T4-320), more than 2.337 times the graded ceiling, are CONFIRMED (the N4 numerical auditor accepts the reproductions in N4-260 to
   N4-262). Its larger bound above 0.00167183069831928 at the registered probe (19, 1800) (N4-257) is CONFIRMED by
   T4-331 (accepted in N4-267), 3.656 times the graded ceiling; the diagnostic bound above 0.000596123050327423 at (21,
   522) (N4-259, not a preregistered probe) is CONFIRMED by its independent reproduction N4-384, accepted in T4-460
   (14:47Z), and stays outside the 25 registered probes; no verdict needs it. Every campaign snapshot through C1-N1-022
   except C1-N1-011 (controlled comparison, FLOAT values only, no proposed exclusion, not a certification target) is now
   RULED OUT in every registered scalar ball and original graded box. C1-N1-018 (a continuation of 016 by 12 steps,
   registered 08:02:27Z, a design experiment) is RULED OUT in every ball of matrix rows 84 and 85 (v80 to v88), the
   statL and bL balls included. Its positive point gaps for the six tested scalar balls and the original graded bound
   (residual 0.0958788144 at (1/10, 73/100), uniform graded gap 0.0754729725; N4-270) are CONFIRMED by an independent
   polar construction (T4-342), its sector prefix by T4-343, its exact origin normalization (c + partial_y u2(0) = 1,
   density slope in (10.3106636255510647, 10.3106636255510648)) by T4-346, and the separation of its 25 registered
   probes from the objective span (N4-271); the N4 numerical auditor accepts these audits in N4-275 to N4-278. Its registered held-out
   distance above 0.001655825792 at (19, 1800) (N4-272), more than 3.621 times the graded ceiling, is CONFIRMED by
   T4-345 by an independent polar path; this distance, not the point gaps, gives the exclusion from the remaining balls
   of row 84 (v80; T4-347); the bound above 0.001328016044 at (23, 2400) (ratio 2.904; N4-272) is CONFIRMED by T4-349
   (accepted in N4-283) and is weaker. C1-N1-019 (017 continued by 12 steps, registered 08:28:42Z, a trial comparison,
   not a certification target) is RULED OUT in every ball of matrix rows 86 and 87 (v84, v85): its exact structure and
   point gaps (N4-279, CONFIRMED by T4-353), its exact origin normalization (T4-354), its complete sector prefix
   (T4-355), the separation of its registered probes from the objective span (N4-280) and its registered held-out
   distance above 0.001661806967 at (19, 1800) (N4-282, CONFIRMED by T4-357; more than 3.634 times the graded ceiling)
   are CONFIRMED, and the N4 numerical auditor accepts the reproductions (N4-287 to N4-290). C1-N1-020 (scales 25 and 50 together, 2426
   generators, registered 08:46:18Z with numerics_v10, a trial comparison, not a certification target) is RULED OUT in
   every ball of matrix rows 88 and 89 (v88): its point fields and gaps (N4-291, CONFIRMED by T4-360), its exact origin
   normalization (T4-361), its complete sector prefix (T4-362), its actual shapes and the separation of its registered
   probes from the current objective span (N4-292, T4-364) and its registered held-out distance above
   0.001855374677442712 at (19, 1800) (N4-293, CONFIRMED by T4-363; more than 4.058 times the graded ceiling) are
   CONFIRMED, and the N4 numerical auditor accepts the reproductions (N4-296 to N4-299). C1-N1-021 (020 with 14 held-in mid-field rows,
   2426 generators, registered 10:05:34Z) is RULED OUT in every ball of matrix rows 90 and 91 (v110): its point fields
   and gaps, its exact origin normalization and its complete sector prefix (N4-314, CONFIRMED by T4-387 to T4-389 and
   accepted in N4-319), its actual shapes and the separation of its registered probes from its objective span (N4-315,
   T4-395) and its distance above 0.001864696854799172 at the registered probe (19, 1800) (N4-316, CONFIRMED by T4-392
   and accepted in N4-320; more than 4.078 times the graded ceiling) are CONFIRMED. C1-N1-022 (016 with 240 radius-25
   functions in the angular blocks m = 16 to 23, 2414 generators, registered 10:28:22Z) is RULED OUT in every ball of
   matrix rows 92 and 93 (v116): its point fields and gaps (F(1/10, 73/100) = 0.08875964289635570284..., graded gap
   0.06836100482471213789...), its exact origin normalization and its complete sector prefix (N4-326, CONFIRMED by
   T4-405 to T4-407), its actual shapes and the separation of its registered probes from its objective span (N4-321,
   CONFIRMED by T4-403 and accepted in N4-331) and its distance above 0.00135251075726327 at the registered probe (19,
   1800) (N4-327, CONFIRMED by T4-408; more than 2.958 times the graded ceiling) are CONFIRMED. C1-N1-023 (016 plus 252
   radius-100 functions in the same blocks, 2426 generators, registered 10:42:28Z) is RULED OUT in every ball of matrix
   rows 94 and 95 (v122): its dimension and objective, its point fields and gaps (F(1/10, 73/100) =
   0.083280868582953659827..., graded gap 0.062882815459541270946...), its exact origin normalization, its complete
   far-field prefix and its distance above 0.002634958245163687 at the registered probe (19, 1800) (more than 5.763
   times the graded ceiling) are the N4 numerical auditor's N4-336 to N4-339, reproduced independently by the T4 theory auditor in T4-416 to T4-420, and
   the N4 numerical auditor accepts the reproductions (N4-348 to N4-350). C1-N1-024 (a rule control of 016, registered 11:31:32Z) is RULED
   OUT in every ball of rows 96 and 97 (v124): its basis and rows, its point gaps (F(1/10, 73/100) =
   0.095280877528863606879..., graded gap 0.074870039634554045471...), its origin normalization, its complete prefix
   through -7/2 and its distance above 0.001556067368832641 at (19, 1800) (more than 3.403 times the graded ceiling) are
   the N4 numerical auditor's N4-342 to N4-345, reproduced independently by the T4 theory auditor in T4-427 to T4-431, and the N4 numerical auditor accepts the reproductions
   (N4-357 to N4-359, v126). C1-N1-025 (registered 12:50:59Z) is RULED OUT in every ball of rows 99 and 100 (v130): its
   structure (T4-436, CONFIRMED independently in N4-361 and N4-365, accepted in T4-444), its point gaps, origin
   normalization, complete prefix through -7/2 and distance above 0.002065801265578052 at (19, 1800) (more than 4.518
   times the graded ceiling) are the N4 numerical auditor's N4-362 to N4-364, reproduced independently by the T4 theory auditor in T4-438 to T4-441, and
   the N4 numerical auditor accepts the reproductions (N4-370, N4-371). C1-N1-026 (registered 13:12:37Z) is RULED OUT in every ball of rows
   101 and 102 (v132): its structure, point gaps, origin normalization, complete prefix and distance above
   0.001355907204057457 at (19, 1800) (more than 2.965 times the graded ceiling) are the N4 numerical auditor's N4-366 to N4-369,
   reproduced independently by the T4 theory auditor in T4-446 to T4-450, and the N4 numerical auditor accepts the reproductions (N4-377 to N4-379, v133).
   So every snapshot C1-N1-002 to C1-N1-026 except 011 (the FLOAT comparison) has no exact solution at its reference c
   in any registered scalar ball or original graded box with a positive top-row budget. The T4 theory auditor's T4-459 (CONFIRMED by
   the T2 theory worker the review of T4-459, accepted in T4-462, and reciprocally by the N4 numerical auditor in N4-390) composes this as one finite statement:
   each of these 24 snapshots has fixed-c L^2 distance above 1/1000 by its accepted weak inequality (the least of the 24
   strict floors is 0.001232449584, 015), above the eight scalar ceilings, the original graded ceiling 25/54684 and, for
   every trans/statL parameter choice with m2 > 0, the radius 25/(54684 512) < 8.93e-7. With the T2 theory worker's bL margin cap
   (handoff BK2, CONFIRMED in T4-462) the same holds for every bL ball permitted by the unweighted margin, at every
   weight pair: its L^2 radius is below 4.1069e-6 at the registered floors (section 2.8). Neither covers the weighted
   margin (B-L2-w), other floors or constants, a dyadic ball, separate weights on b and on the H part of E0, other
   Gram schemes, or balls whose L^2 control is not sqrt(w2) ||h||_2 (the T2 theory worker BH3, BO5). For 002, 003 and 004 the matrix
   rows 36, 40 and 42 name
   specified balls only; the other balls follow because the fixed-c L^2 distances above 1.56361352, 0.22988134 and
   1.40009623 (N4-069, N4-070, CONFIRMED by T4-068) exceed the L^2 radius of every registered scalar ball at its
   registered weights, at most 3.7930e-6 (rounded up; theory_v03 section 6, exact ceilings in T4-454; T4-471),
   and of every graded box with a positive top-row budget, below 1/2000 (T4-070, row 55). In matrix row 35, C1-N1-001 is
   RULED OUT as framework inapplicability (its residual is not in the forcing space of any unweighted framework)
   and, since v140, by the stronger affine L^2 exclusion at every real c, AUDITED via T4-465. The stronger statement is
   the T4 theory auditor's T4-458, CONFIRMED by the T1/T3 theory worker's review R1-046 (review set 44, with an independent exact check,
   artifacts/checks/check_T4458.py) and by the T2 theory worker's review of T4-458 (handoff BL), both accepted by the T4 theory auditor in T4-465 (15:11Z,
   957 checks): the exact leading residual of 001 at q = 2 gamma - 1 = 0.10477... > 0 is r^q E(theta) with E nonzero
   (sine modes 21 to 39 only; branch 1 cancels the modes 1 to 19), so by the annular argument of T4-049 no h in L^2(R^2)
   solves the correction equation in distributions at any real c. This excludes exact solutions in the affine class
   rho + L^2 with the snapshot's own far field, so in every registered scalar ball and every original graded box with a
   positive top-row budget, whatever its radius; it does not cover
   FW-T-DYADIC-Y-v1, weighted or non-L^2 repairs, profiles with a different far field, or a snapshot whose branch-1 span
   reaches mode 39. For c != c0 the test function is R^-1 eta(r/R) G0(theta): the angular factor is the leading density
   profile G0 (sine modes 1 to 19), not E, which is orthogonal to G0 (the T2 theory worker BL2; T4-458 ERRATA_v01; R1-046 uses G0).
   T4-465 also confirms R1-046's extension to an added constant background velocity. Matrix v140 (15:22Z) records the
   statement in row 35. The FW-T-DYADIC-Y-v1 list above is separate. C1-N1-027 (registered 14:13:51Z) has FLOAT values
   only and is untested (rows 103 and 104 OPEN, v138). It continues the 022 state 60 steps with the plain 67 rows of
   016, as a control for 026; the N1/N2 numerics worker calls it not a certification target. C1-N1-028 (an ID reserved in numerics_v14
   for the 022 state plus 252 radial functions in m = 9..15) was registered at 15:24:01Z (matrix rows 107 and 108,
   OPEN) and has FLOAT values only (numerics_v15); it is a trial comparison, not a certification target. Six of its 25
   registered held-out FLOAT values exceed the graded ceiling 4.5717e-4 (largest 8.15e-4 at (19, 1800), team note
   v53); no certified distance for 028 exists. No compactly supported L^2 correction makes
   007, 013 or 014 stationary (T4-281, AUDITED through the T1/T3 theory worker R1-033; second review the T2 theory worker the review of T4-281): three residual
   sectors above gamma - 4 are nonzero, and the endpoint sector at gamma - 4 is not of the dipole form that an exact
   compact correction requires (the T2 theory worker the review of T4-281 R2, AUDITED through the T1/T3 theory worker R1-034 and the T4 theory auditor T4-305). The exact
   branch-3 correction of T4-295 (AUDITED through the T1/T3 theory worker R1-034, accepted in T4-315) removes the sector (4, 1) but leaves
   (9, 0), (5, 1) and the endpoint, and it moves the reference by more than 4373 in L^2 (T4-316; section 2.7). That size
   belongs to the global polynomial formula, not to the cancellation: a smooth far-out cutoff of the same tail cancels
   the same sector at L^2 cost C_00 L^(q+1), which tends to 0 as the cutoff radius L grows (T4-314, AUDITED through
   the T1/T3 theory worker R1-035, accepted in T4-325; the cost is below epsilon exactly when L > (C_00/epsilon)^(1/(-q-1)), and for 007
   the FLOAT value C_00 = 215936.9... puts the radius for epsilon = 1e-3 near 45174, far outside the N1/N2 numerics worker mesh;
   T4-329). The price appears in the weighted classes E_a with a <= 4 gamma - 4, where the residual norm of the repaired
   reference grows without bound as the cost tends to 0 (R1-035 remark (b), CONFIRMED by T4-326 with explicit
   finite-annulus bounds; a trade-off of this construction, not a lower bound for every repair). A second cutoff at a
   larger radius removes the next sector (9, 0) in the same way, leaving a residual O(r^(-1-5 delta)) (T4-324, AUDITED
   through the T2 theory worker the review of T4-324, accepted in T4-337; section 2.7). A third cutoff removes (5, 1) and leaves the endpoint
   (1, 2) as the only leading residual sector (T4-338, which CONFIRMS the T2 theory worker's review of T4-324 R2 and R3 under stated
   finite angular, remainder and growth hypotheses; the third cutoff for 007, 013 and 014 is AUDITED through the T2 theory worker
   the review of T4-338, accepted in T4-365). The endpoint consequence after three cutoffs (T4-339) is AUDITED through the same
   review (T4-365; its other input, the moment-resolved endpoint theorem T4-335, is AUDITED through the T2 theory worker the review of T4-335,
   accepted in T4-350): every stationary real S1 C^1 correction k of the three-times repaired reference with
   H_(gamma-4)(k) finite has an r^(gamma
   - 4) angular coefficient of circle norm at least 85017, 85018 and 85016 for 007, 013 and 014, a statement about tail
   coefficients relative to that reference and not an L^2 distance bound; a fourth cutoff can remove the endpoint (with
   zero first moment at arbitrarily small L^2 cost; the T2 theory worker the review of T4-338 R4, CONFIRMED by T4-368), so no obstruction to
   finite reference design is claimed. An exact correction with weighted C^1 decay r^q, q = -1 - 4 delta, has the forced
   tail -r^q Theta_(4,1) + lower order (T4-294, AUDITED through the T2 theory worker the review of T4-294, accepted in T4-315; section 3.4);
   after the T4-295 repair the forced tail moves to the sector (9, 0) (the T2 theory worker the review of T4-294 R2, AUDITED through T4-317).
   Under the endpoint hypotheses of T4-335 the closure inequality of the T2 theory worker the review of T4-335 R3 (CONFIRMED by T4-351) can
   certify no L^2 distance above 9.28e-11 with the original T4-335 velocity coefficient E_q* = 133.004... of T4-335 (i)
   (the value of an upper-bound formula, not a lower bound on valid constants), far below every family ceiling (section
   3.4). With the current constants (E = 1.747261, H >= 999745) it certifies none above 1.66122e-8, or 1.89061e-9 with
   the radial shape, below every registered radius (the T2 theory worker the T2 falsification review of the endpoint and the report summary section 3, CONFIRMED in T4-443).
   By the T1/T3 theory worker R1-038 (review set 35 and review set 37, CONFIRMED by T4-379) the endpoint bound of T4-339 gives an L^2
   exclusion only together with an a priori weighted budget H_max for every stationary correction in the balls (not
   presently proved and not excluded; OPEN) and a velocity constant E with E sqrt(2 pi) H_max/B < Emax(b), with b the
   ceiling and B the endpoint angular constant of section 3.4 (G7) (c), where Emax(b) is below 7.9417 at the printed
   graded target 25/54684 (above 7.942167 at the exact ceiling, T4-443). Since H_max >= B/sqrt(2 pi), this implies the
   shorter necessary condition E < Emax(b), which hides the normalization (T4-453). The proved constant was 133.004...
   at R1-038, and a valid universal constant below 1.747261 now exists (T4-411). Since a budget valid for any stationary
   correction is at least 999745 (T4-380), the condition needs E below 0.2694533 at 25/54684, below Etest, so it fails
   for every valid constant (the T2 theory worker the T2 falsification review of the endpoint and the report summary section 4); the moment bounds of T4-371 and T4-372 (the
   sharp constant, AUDITED through the T1/T3 theory worker R1-039) do not change this reach. T4-375 (AUDITED through the T2 theory worker the review of T4-375,
   accepted in T4-385) with the pointwise minimization of T4-380 (CONFIRMED) raises the necessary budget to
   H_(gamma-4) > 999745 for all three endpoint data. Every velocity constant valid in T4-335 (1) for all real S1 C^1
   corrections with finite H_(gamma-4) is at least Etest = 0.793036506422514088... (T4-381, AUDITED through the T1/T3 theory worker R1-040
   and T4-391; second review the T2 theory worker the review of T4-381 and T4-384), also on smooth normalized S1 functions of arbitrarily small L^2
   norm (T4-384, AUDITED through the review of T4-381 and T4-384 and T4-396), and in every fixed ball of X_(s,w) with c[h] = 0, the
   selected sharpw ball included (T4-397, AUDITED through the T1/T3 theory worker R1-042, accepted in T4-409). Reaching the fixed sharpw
   radius 1351/1024000000 would need E < 0.785064. So no valid universal velocity constant lets the T4-351 inequality
   reach, for 007, 013 or 014, any registered radius from 3.5125e-7 up (with the retained shape of T4-414; the crude
   T4-380 cutoff covers 1351/1024000000 and above), or 2^-23 when V >= |U_lead(0)| = 0.99148... (NC-T-UNIV-E, section
   3.4 (G7) (e); the T2 theory worker the T2 falsification review of the endpoint and the report summary section 1, CONFIRMED in T4-443; the T2 theory worker handoff AU4 as corrected in
   AZ4). At the FW-A2-Db radii 2^-25 and 6.8626e-8 the necessary thresholds are at least 1.020385 and 0.8711127, above
   Etest, so this argument proves nothing there; whether an improved valid constant reaches them is OPEN (T4-443: Etest
   is a lower bound on valid constants, not a proved admissible one). 007, 013 and 014 are excluded from those two balls
   by NC-T-DIST, by factors above 28895 (distance floors of T4-185, T4-255 and N4-214 divided by the radius; the T2 theory worker
   CHECK_T1_v08_FACTORS section 3). The current tail list with the floor min(1.747261, lambda (5/s)^delta) reaches no
   registered radius (whole CI value below 2.66323e-8 < 2^-25; the T2 theory worker the T2 falsification review of the endpoint and the report summary section 2 (c),
   CONFIRMED in T4-443). This bounds one certificate and excludes nothing; velocity estimates that use the stationary
   equation, and an a priori H_(gamma-4) bound, are undecided. The optimal universal constant lies in [Etest, 1.747261]
   (T4-411: a valid universal constant below 1.747261 exists; valid constants are upward closed, so their set has no
   upper bound). The profile-specific limit of T4-402 (AUDITED: The T2 theory worker the review of T4-402, accepted in T4-413) is 583/1000 <
   Etest, but only as r tends to infinity. Even with zero remainder and V = 0 it fails the complete radial integral of
   the test, which needs a coefficient below 0.527596 (fixed sharpw ball), 0.458292 (sharpw family), 0.434940 (TB) and
   0.181070 (graded) (T4-414, AUDITED: The T2 theory worker the review of T4-414, accepted in T4-423). This withdraws the answer "in principle
   yes" for 583/1000 in the review of T4-402 section 4 (the review of T4-414; the coordinator 12:12Z item 4); the cutoff-radius rooms
   0.09893906 H and 0.06419100 H of that section are necessary, not sufficient (T4-413). T4-415 proves the pointwise
   coefficient 93/250 on the endpoint spans, again only as a limit (AUDITED: The T2 theory worker the review of T4-415, accepted in T4-434; no
   constant below 0.3714757 satisfies the angular inequality N(z) <= E G(z) on the whole span of z); with zero remainder
   it passes the three scalar thresholds and not the graded one (T4-422, AUDITED in the same way). T4-410 (AUDITED:
   The T1/T3 theory worker R1-043, accepted in T4-424) gives an explicit finite-radius remainder, but with the only proved tail bound,
   T4-335 (7), it exceeds 2.74 H at every radius up to 18860, above every room and above 1.747261. No constant use of it
   (T4-421, R1-043 step 9), no radius-dependent use spliced with any universal constant (T4-425, AUDITED: The T1/T3 theory worker R1-045,
   accepted in T4-432; at its four targets, the fixed sharpw ball and the sharpw, TB-sharp and graded ceilings; at the
   FW-A2-Db radii an improved valid constant is OPEN, T4-443) and no use of its outer amplitude alone (R1-044, CONFIRMED
   by T4-426) makes the test integrand positive below r_beta, for any profile coefficient >= 0 (NC-T-TWO-WEIGHT, section
   3.4 (G7) (e)). The endpoint route is therefore blocked with the present inputs. This concerns the proved tail input,
   not existence. Lifting it needs a tail bound for stationary corrections with all exponents well above delta = 1 -
   1/c, or a velocity or H_q estimate specific to stationary corrections; the T1/T3 theory worker, the T2 theory worker and the T4 theory auditor judge that neither is
   worth hours 16 to 22 (the coordinator 12:30Z item 2). R1-038 also gives a screening rule for continuations of registered
   snapshots (R-SCREEN, section 3.4). No exact solution near any candidate has been shown to exist.
2. Strongest proved a posteriori estimate (AUDITED conditional): FW-T-T4L2-sharpw-v1 (section 2.1). It closes the
   fixed-point problem at fixed c whenever the background satisfies the signed L^2 margin (B-L2) and the A2-type
   coefficient bounds, and the residual satisfies X_(s,w)(F) <= 2.1035e-4 in the forcing norm NORM-T-Xw5184-v1 (s =
   1/5184, weights 2^15, 2^20). Against A2 Theorem D(b) (FW-A2-Db, N_s(F) <= 6.3578e-7, A2-THEOREM) the stated tolerance
   is 330.8 times larger, but the two tolerances are in different norms and the two forcing spaces are incomparable
   (T4-259, AUDITED through the T2 theory worker the review of T4-259 and T4-283): X_(s,w) has no Hdot^-1 component, so a residual needs only
   three far-field conditions, the sectors (2,0), (3,0), (4,0) (the sectors with exponent at least -1 are (1,0) to
   (4,0)), against seven for N_s (the eight sectors (1,0) to (6,0), (1,1) and (2,1) with exponent at least -2), in each
   list less the leading sector (1,0) at exponent gamma, which vanishes identically (labels corrected in draft 15,
   T4-328, exact enumeration), but it asks for slightly more fractional regularity (s = 1/5184 against 2^-18). The ratio
   is not an enlargement of one residual ball. On residuals in E_3 with Q3 <= 10^6 E_2, the A2 condition at 163.88 times
   the A2 tolerance implies the sharpw smallness, and the converse fails (the T2 theory worker the review of T4-259 R2, AUDITED through
   T4-284; section 4).
3. The binding obstruction is the fixed-c L^2 distance of the candidates from the solution set, not the linear
   constants. A ball of radius r in a norm X with X(h) >= sqrt(W2) ||h||_2 can contain only corrections with ||h||_2 <=
   r/sqrt(W2), and a positive rate on the ball caps r. No ball of a registered scalar family with a positive rate
   contains a correction of L^2 norm above 3.7930e-6 (the universal family ceiling of FW-T-TB-sharp-v1; the stated fixed
   balls are smaller, for example 1.3193359375e-6 for sharpw, T4-262), and no graded box one above 4.5717e-4 (NC-T-DIST,
   AUDITED ceiling formula). For 007, the best observed candidate (the most complete hypothesis record; the smallest
   CONFIRMED G0 is now that of 016, 0.3088864451... against 0.37668932, N4-341; its distance lower bound is not the
   smallest, and lower bounds do not order the actual distances; E2(007) < E2(016) at the registered E2 weights and
   H(016) < H(007) are CONFIRMED and accepted both ways, pairwise statements about one norm only, with gaps above
   21.759869525 and 0.017627007636152, N4-430 and N4-431 with T4-502 and R1-054, earlier 0.017571422145091 of N4-416 to
   N4-418, T4-486, T4-488 and R1-052 and N4-396, N4-410, T4-480, N4-412 and T4-483; section 7), every real S1 correction
   h in L^2 with F(rho + h; c) = 0 has ||h||_2 > 0.004769166867 (T4-185, AUDITED by the T1/T3 theory worker R1-022, number CONFIRMED by
   N4-157). That is more than 1257 times the largest scalar ceiling and more than 10.43 times the graded ceiling. The
   forcing alone also fails: X_(s,w)(F) > 756.5312630768 against 2.1035e-4, a factor above 3596535.57 (the N3 numerics worker with all
   complete components, CONFIRMED by N4-180 and T4-238; G0 and G1 alone give 3.48e6, T4-197).
4. A free exponent does not help in the same chart. If the leading far-field profile Theta_0 is nonzero, the affine
   class rho + L^2((1 + r^2)^(-a)), 0 <= a <= 1 + 1/c, contains no stationary solution at any c' other than c (T4-189,
   AUDITED; T4-201, T4-213). For 007 and for state 131, d2 and 005 to 012 the leading profile is the same nonzero exact
   profile (T4-203, T4-213 with N4-172 CONFIRMED). So the 007 exclusions hold at every c' in the chart.
5. A weaker high space does not help at the origin. FW-T-DYADIC-Y-v1 (a weighted dyadic space with a decaying low
   weight, whose norm is not shown to dominate ||h||_2) is RULED OUT (AUDITED conditional) at state 131, d2 and 007 (and
   at 008 and 009, T4-248, T4-250) for every admissible parameter: its high inverse is impossible for s >= c - 1 and
   costs M >= 1/(c - 1 - s) below, which with the far-field cap gives a residual ceiling that 007 misses on every cell
   (NC-T-ORIGIN-INV, T4-146, T4-147). NC-T-ORIGIN-specification and NC-T-E3 give the same obstruction for H^q energies with q >=
   c + 1 and for the third-order endpoint E3 of A2 Route U.
6. First failing inequality for 007 in the best framework: membership and the forcing ball are satisfied in form ((2,0),
   (3,0), (4,0) vanish exactly; (B-L2) holds with rate > 2.00215, N4-111, T4-162), the smallness X_(s,w)(F) <= 2.1035e-4
   fails by a factor above 3596535.57 (T4-238), and independently NC-T-DIST fails by a factor above 1673 (sharpw
   universal family ceiling 2.8496e-6). The far-field decay hypothesis (A) and the coefficient lists (B0n), (B4), (B5),
   (B7) and (B9c) are not checked for 007 (closure matrix row 56); they would matter only for a candidate within the
   budgets.
7. Smallest remaining obstacle. A candidate whose certified fixed-c L^2 distance lower bound is below 3.7930e-6 (any
   scalar ball; the common upper bound of the family ceilings, T4-454; the rounded 3.79e-6 is not a valid cap, since an
   exact TB-sharp parameter budget admits 3.791e-6, T4-491) or below 4.5717e-4 with a passing point test (graded box),
   and whose forcing norm is below the threshold. For 007 the distance would have to fall by a factor above 1257
   (scalar) or 10.43 (graded). On the theory side, the endpoint route of item 1 is blocked with the present tail input
   (NC-T-TWO-WEIGHT), and two routes are not blocked by an AUDITED obstruction. (i) The localized orbit-weight route of
   the T2 theory worker (section 2.7): with the normalization inf psi = 0 its weight is at least 1, so its ball radius must exceed
   0.004769166867 for 007 (T4-260); no upper ceiling on that radius is proved, so the route is not excluded. Localizing
   a registered norm does not lift the ceilings: for corrections supported at r from 20 to 32 in the odd modes from 19
   the sharpw bound improves by 0.55 percent (T4-278), and a graded box, also with a localized low row (T4-277), admits
   less than 4.5717e-4 anywhere (section 2.7). (ii) A new chart (Route T-E, section 8): a reference with a different
   tail exponent or a different leading angular profile, with its own subcritical remainder space, normalization,
   inverse and nonlinear estimates. A finite augmentation by the lower tail amplitudes at fixed c and fixed leading
   profile adds no solution in the a = 0 class (T4-234 AUDITED by the T1/T3 theory worker R1-030 and T4-246; T4-235 CONFIRMED by N4-189;
   the consequence accepted in T4-246 and N4-192; section 8.2), so it cannot lift NC-T-DIST. Neither route has a
   framework or a candidate evaluation.
8. Recommendation for the next campaign (quantitative reasons in section 9). Priority 1: numerical refinement of the
   reference aimed at the fixed-c distance (the mid-field residual in the odd angular modes above 1, where the 007
   distance is created; the 013 and 014 runs motivate basis functions concentrated at r from about 20 to 100), measured
   by held-out exact probes and by the first L^2 Newton step (Lemma W). Priority 2: sharper constants are not the lever.
   Better state 131 matrix floors raise the sharp and sharpw thresholds by at most 2.2 and 1.81 with all other constants
   fixed (T4-119; ceilings, not attainable improvements), and no weights, base rate or s raise the L^2 budget
   of T2-R3 balls above 1.1746 times the sharpw ceiling (beta 2), or that of T2-R1 TB-sharp balls with E0 as one
   component above 1.0612 times the TB-sharp ceiling (beta 11/4), at the registered floors and under the other
   hypotheses of section 2.8 (the T2 theory worker Proposition WU3, CONFIRMED by the T4 theory auditor T4-462, whose exact weight elimination is
   CONFIRMED by the T1/T3 theory worker R1-047 and the T2 theory worker the review of T4-462, both accepted in T4-468, and independently by the N4 numerical auditor N4-395;
   section 2.8). Priority 3 (speculative): a Route T-E chart. A new norm of type "weaker high space" must first pass the
   origin tests of section 6. On the theory side, a tail bound for stationary corrections with all exponents above delta
   = 1 - 1/c is the input that every finite-radius endpoint route of this campaign lacked (section 3.4 (G7) (e)); which
   such bound is provable should be settled before further endpoint or remainder work, and an a priori H_(gamma-4) bound
   is a separate task.
9. Regularity and far field required by the best framework (section 2.1, :H1 and :H5): an S1 reference with the
   exact origin normalization (O1), |D^j rho| = O(r^(gamma' - j)) for some gamma' < 1 and j = 0, 1, 2 outside a
   ball (the candidates have the algebraic far field r^gamma Theta_0 plus lower tails r^(e_j) Theta_j, j < N), the
   finite norms in (B-L2) and the A2 lists, and a residual whose sectors (2,0), (3,0), (4,0) vanish exactly with Q3
   finite. The correction h lies in X_(s,w): J^s h with s = 1/5184 has omega D^2, D and L^2 components with weights
   (1, 2^15, 2^20). In the L^2 class the lower tails are not free: an exact solution forces Theta_1 to Theta_(N-1)
   from Theta_0 (G6, T4-234).

the prompt section 15 questions and where they are answered: (1) strongest estimate, item 2 and section 3; (2) how much
weaker than analysis2, item 2 and section 4; (3) best reference, item 3 and section 7; (4) regularity and far field,
item 9 and sections 3.4, 8; (5) residual norm, items 3 and 6 and section 9.1; (6) closure and the first failing
inequality, items 1 and 6 and section 9.1; (7) smallest obstacle, item 7 and section 9.2; (8) priority, item 8 and
section 9.4.

## 1. Setting and notation

- Unknown: a density rho on R^2 with the S1 symmetry (even in x, odd in y), velocity U[rho] = (-R1 R2 rho, R1^2 rho)
  (symbol sigma(xi) = (xi1 xi2, -xi1^2)/|xi|^2), and the stationary self-similar equation
    F(rho; c) = (c X + U[rho]).grad rho - rho = 0.
  The campaign exponent is c = c_l = 4076476460239181/2^51 = 1.81031921, gamma = 1/c = 0.552388769,
  delta = 1 - gamma = 0.447611231.
- Linearization at a reference rho: L h = V.grad h + U[h].grad rho - h, V = c X + U[rho]. Correction equation:
  L h + U[h].grad h = -F. Every framework below solves it by a contraction or Newton argument in a ball
  B = {X(h) <= r, c[h] = 0}, where c[h] = 0 fixes the origin normalization (O1) below.
- Origin normalization (O1): V(0) = 0, DV(0) = diag(2c - 1, 1), grad rho(0) = (0, a0), equivalent to
  c + d_y U[rho]_2(0) = 1. For 007, a0 = 10.31199902106439505 (T4-147, N4-128).
- Far field: the reference has rho = r^gamma Theta_0(theta) + o(r^gamma), and the residual is a sum of sectors r^e
  E(theta) with e = 1 - l delta - 2q, indexed (l, q): the leading term is (1, 0) with e = gamma, the first residual
  sector of 007 is (4, 1) with e = 4 gamma - 5, and (9, 0), (5, 1), (1, 2) have e = 1 - 9 delta, 5 gamma - 6 and gamma -
  4. Membership of F in a forcing space is a statement about which sectors vanish exactly (section 4).
- Fixed c and fixed leading profile. Every framework here keeps c and the leading far-field profile fixed (the prompt
  line 119). Section 8 shows why this is the right gauge for the campaign candidates and what an alternative chart
  would require.
- Rates. beta_inf(a) = 1 + c - c a is the far-field cap of a low energy rate in H_a = L^2((1 + r^2)^(-a)) (NC-T-WRATE).
  J = (1 - Delta)^(1/2), omega = (1 + 4 r^2)^(2/5), c_s = [2 sqrt(pi s (1 + s))]^(-1).

## 2. Closure theorems (conditional)

Each entry gives the statement, the hypotheses by name, the constants, the status and the source. Every threshold is
a sufficient condition at fixed c. None is verified for any candidate.

### 2.1 Main conditional theorem: FW-T-T4L2-sharpw-v1 (and FW-T-T4L2-sharp-v1)

Source: The T2 theory worker notes/T2_T4L2_sharp.md (T2-R3), built on the T4 theory auditor audit record l2_closure, proof (T4-019). Status: AUDITED
conditional (T4-042 with the T1/T3 theory worker R1-006; numbers CONFIRMED by N4-054; the T1/T3 theory worker exact Gram and row-sum certificate
artifacts/checks/check_T2R3.py).

- Spaces. Forcing and correction norm X_(s,w)(f) = E_w(J^s f), E_w(g)^2 = ||omega D^2 g||_2^2 + w1 ||D g||_2^2 +
  w2 ||g||_2^2 (NORM-T-XSW-v1[s, w1, w2]); no Hdot^-1 component. Low metric L^2. Ball
  B_r = {X_(s,w)(k) <= r, c[k] = 0}.
- Hypotheses on the reference rho (whole plane, fixed c):
  - :H1 (= T4-019 :A, structure): 9/5 < c < 37/20; c + d_y u2(0) = 1; the A2 (B0) boundedness list;
    for j = 0, 1, 2, |D^j rho| = O(r^(gamma' - j)) outside a ball, for some gamma' < 1.
  - :H2 (= :B, signed L^2 margin (B-L2)): c + 1 - theta - kappa >= 2, theta = ess sup (|grad rho| - rho_y)/2,
    kappa^2 = [(log 2 - 1/2) ||D rho_x||_2^2 + (3 log 2 - 2) ||D rho_y||_2^2]/(16 pi). kappa bounds the
    Hilbert-Schmidt norm of the symmetric remainder of U[.].grad rho (T4-016, AUDITED).
  - :H3 (= :C): M1 >= (9/10) I, M2 >= (1/2) I and the A2 (B7) list.
  - :H4 (= :D): the A2 (B9c) component sums (2, 6, 24, 160, 22, 32, 80, 2048).
  - :H5: F in X_(s,w), which requires (2,0), (3,0), (4,0) EXACT-ZERO at every harmonic present, and Q3 finite.
  - :H6: X_(s,w)(F) <= eta (threshold below).
- Conclusion. There is a unique h in B_r with F(rho + h; c) = 0, c[h] = 0. The semigroup of A_k = L + U[k].grad on
  X_(s,w) has rate mu0 - C' s - (8/5) X_(s,w)(k)/sqrt(s) for every k in B_r, where mu0 is a certified
  positive-definite point of
    G_w(mu) = [[1/2 - mu, -347/10, -5], [-347/10, w1 (9/10 - mu) - 40, -3 w1], [-5, -3 w1, w2 (beta_L - mu)]],
  beta_L = 2, and C' bounds the symmetric row sums of the commutator matrix. The L^2 inverse norm is at most
  1/beta_L = 1/2 for every k, and the L^2 contraction ratio is c_s r/2.
- Constants (exact rationals unless stated; check_T2R3.out: row sums 400.99788 < 401 and 396.66411 < 397):

  | quantity | FW-T-T4L2-sharp-v1 | FW-T-T4L2-sharpw-v1 |
  |---|---|---|
  | forcing norm | NORM-T-X7744-v1 (XSW[1/7744, 2^14, 2^18]) | NORM-T-Xw5184-v1 (XSW[1/5184, 2^15, 2^20]) |
  | mu0, C' | 259/1000, 401 | 97/250, 397 |
  | ball radius r | 147/200000 | 1351/10^6 |
  | rate on the ball beta >= | 1037/10000 | 1557/10000 |
  | K_H = 1/beta <= | 9.6432 | 6.4226 |
  | threshold eta | 76219/10^9 = 7.6219e-5 | 4207/(2 * 10^7) = 2.1035e-4 |
  | implied gamma_1 <= eta/sqrt(w1) | 5.954609375e-7 | 1.16203056e-6 |
  | implied gamma_0 <= eta/sqrt(w2) | 1.48865234375e-7 | 2.05419921875e-7 |
  | L^2 contraction c_s r/2 <= | 0.00912295 | 0.0137200 |
  | L^2 universal family ceiling (NC-T-DIST) | 3.0927e-6 | 2.8496e-6 |
  | L^2 radius of the fixed ball, r/sqrt(w2) (T4-262) | 1.435546875e-6 | 1.3193359375e-6 |

- The sharpw threshold 2.1035e-4 is the value selected at r = 1351/10^6 with the rate rounded down to 1557/10000:
  (1557/10000)(1351/10^6) = 2.103507e-4. The exact rate there is beta(r) = mu - A r = 63092119/405000000, and beta(r) r
  = 85237452769/405000000000000 > 2.1046e-4 (N4-415; the T1/T3 theory worker check_v50.py). It is not the largest residual these s and
  w admit: beta(r) r = eta* - A (r - r*)^2 with mu = mu0 - C' s = 201799/648000 and A = (8/5)/sqrt(s) = 576/5, so the
  supremum over r is eta* = mu^2/(4A) = 40722836401/193491763200000 (2.1046e-4 rounded down) at r* = 201799/149299200,
  where the contraction is below 0.01373 (T4-479; the T2 theory worker the T2 check of T4-479 (sharpw max), 17 exact checks, accepted in
  T4-485; the T1/T3 theory worker checked eta* = mu^2/(4A) exactly). This is the g = 0 case of FW-T-T4L2-defect-v1 (section 2.3). Unless
  expressly compared with eta*, the sharpw forcing factors in this report use the selected threshold 2.1035e-4 (T4-487,
  T4-493); against eta* the 007 factor is above 3594606 (matrix v151; N4-415, T4-485). No verdict changes.

- Closure inequality in the form of PROMPT section 6: K_H eta <= r with beta(r) > 0, the L^2 contraction c_s r/beta_L
  < 1 and the slope margin 7/10 - c_s r > 0, with positivity G_w(mu0) > 0 and (B-L2) (the T2 theory worker notes/T2_T4L2_sharp.md
  section 3). At the selected radii beta >= 1037/10000 and 1557/10000 and the slope margins are at least 0.6817 and
  0.6725.
- Necessary conditions it inherits (section 6): NC-T-DIST (family ceiling above), NC-T-PT point tests, and
  X_(s,w)(F) >= (2^15 G1^2 + 2^20 G0^2)^(1/2) for every s >= 0 (Plancherel and (1 + |xi|^2)^s >= 1).
- Finite-family exclusion (T4-043, CONFIRMED): the four-branch full-residual L^2 floor exceeds these thresholds for
  every polynomial degree K <= 6886 (sharp) and K <= 5814 (sharpw).

### 2.2 FW-T-T4L2-bL-v1[beta_L, w] (the T1/T3 theory worker TP-5; AUDITED conditional: T4-113)

- Statement: keep :H1, :H3, :H4, :H5 of 2.1 with weights w and constant C', and replace (B-L2) by
  (B-L2)_(beta_L): c + 1 - theta - kappa >= beta_L for a given beta_L > 0. If G_w(mu0) (with this beta_L) is positive
  definite, the conclusion of 2.1 holds with beta = mu0 - C' s - (8/5) r/sqrt(s), eta <= beta r, L^2 inverse bound
  1/beta_L and contraction c_s r/beta_L < 1. (B-L2) enters T4-019 only through its energy identity (7).
- Exact critical rates (T4-113): G_w(0) is positive definite if and only if beta_L > 3829321675/5037023232 =
  0.7602350632 (sharp weights) and beta_L > 15208393675/44307283968 = 0.3432481595 (sharpw weights).
- Certified instances (sharpw weights, C' = 397):

  | beta_L | mu0 | s | r | beta >= | eta | K_H <= | L^2 family ceiling |
  |---|---|---|---|---|---|---|---|
  | 7/5 | 359/1000 | 1/5476 | 1213/10^6 | 279/2000 | 423/2500000 = 1.692e-4 | 7.1685 | 2.5362e-6 |
  | 1 | 151/500 | 1/6561 | 459/500000 | 581/5000 | 533/5000000 = 1.066e-4 | 8.6059 | 1.9568e-6 |

- Reading: (B-L2) is a normalization, not a hard threshold. beta_L = 1 keeps about half the threshold of beta_L = 2.

### 2.3 FW-T-T4L2-defect-v1 (the T2 theory worker M4 with moment constant 24/5; AUDITED conditional: T4-065)

- Statement: on the balls of 2.1, let g be a smooth zero-strain correction with X(g) <= m, X(F + L g) <= epsilon and
  ||M^w_g + s K^w_g|| <= B (the defect matrices of NORM-T-DEFECTG-v1, theory_v03 section 3). If
  beta_r = mu0 - C' s - (8/5) r/sqrt(s) > 0 and m + (epsilon + B r)/beta_r <= r, there is a unique exact solution
  rho + h with X(h) <= r and c[h] = 0.
- Feasibility (T4-065): with A = (8/5)/sqrt(s) and mu = mu0 - C' s, a radius r exists if and only if both
  mu - A m - B > 0 and epsilon <= epsilon_max = ((mu - A m - B)^2 - 4 A B m)/(4 A). The first condition alone is not
  sufficient (theory_v03 section 3 printed it as equivalent; REFUTED by T4-216: A = m = B = 1, mu = 3 gives
  epsilon_max = -3/4). Values of epsilon_max for sharpw:
  2.1046e-4 (g = 0; exactly eta* = 40722836401/193491763200000 at r* = 201799/149299200, section 2.1, T4-479),
  1.5964e-4 (m = 2^-12, B = 1/100), 6.7687e-5 (m = 2^-10, B = 1/100). Contraction q < 0.01373 to
  0.01824 (arb, T4-065). The inequality implies m <= r, so the family ceiling of 2.1 still applies.

### 2.4 FW-T-T4L2-trans-v1 and FW-T-T4L2-statL-v1[K_L] (the T4 theory auditor T4-051; the T1/T3 theory worker TP-1)

- trans (AUDITED conditional: The T1/T3 theory worker R1-009 and T4-057; constants CONFIRMED by T4-067). T4-019 with :B replaced by the
  transient bound (L): ||exp(t A_k)||_(L^2 -> L^2) <= 2 e^(-t) for all t >= 0, uniformly on
  {X_s(k) <= R, c[k] = 0}, NORM-T-X3-v1 at s = 2^-17, R = 2^-14. Threshold X_s(F) <= R/||N||,
  ||N|| <= 7.66822167 (the T1/T3 theory worker R1-009), that is X_s(F) <= 7.959492e-6. Picard ratio < 0.012467, K_X < 11.490384.
- statL (AUDITED: T4-059). (L) replaced by the stationary hypothesis (L0): for every k in the ball, every real
  lambda >= 0 is in the resolvent set of the maximal L^2 realization of A_k and ||A_k^-1||_(L^2 -> L^2) <= K_L. If
  K_L c_s R < 1 and X_s(F) <= R/||N(K_L)||, the conclusions hold with Picard ratio K_L c_s R. With R = 21/10^5:
  thresholds 3.0322015e-5 (K_L = 1/2), 2.4186857e-5 (1), 1.5344622e-5 (2), 8.31687e-6 (4), 4.251374e-6 (8),
  2.137754e-6 (16) (check_T4051.out).
- Woodbury bound (TP-1b; formula CONFIRMED by T4-059, column bound T4-073): if A_0 = D_0 + K_F with K_F of rank n
  and Re <D_0 h, h> <= -beta_D ||h||^2, then K_L <= 1/beta_D + ||Psi|| ||Phi||/(beta_D^2 epsilon) for a certified
  margin sigma_min(M_k(0)) >= epsilon. This bounds K_L once (L0) is known; a certificate at lambda = 0 does not imply
  (L0) (T4-258, REFUTED as a sufficient implication; counterexample D = -I, A = D + 2P with P a rank-one projection:
  M(0) = -1 and ||A^-1|| = 1, but lambda = 1 is an eigenvalue). A sufficient certificate of (L0) needs consistent
  maximal low and high generators, ||(D_k - lambda)^-1|| <= 1/(beta_D + lambda) for every k in the ball and every
  lambda >= 0, a certificate of M_k(lambda) uniform in k on the whole half line (for example a finite interval cover
  and a large-lambda Neumann bound), and then the Woodbury bound at zero.
- (L) and (L0) are not verified for any candidate. L^2 radii of the fixed balls, R/sqrt(w2): 1.1921e-7 (trans),
  4.1016e-7 (statL).

### 2.5 Other registered frameworks (statements in theory_v01 and theory_v03 section 3)

| framework | forcing norm | threshold | L^2 ceiling | status |
|---|---|---|---|---|
| FW-A2-Db (A2 Theorem D(b)) | N_s, s = 2^-18 | 6.3578e-7 | 6.8626e-8 | A2-THEOREM |
| FW-T-TB-rebal-v1 (T2-R1) | N_s | 3/327680 (below 9.1553e-6) | 3.5126e-7 (see below) | AUDITED (T4-012) |
| FW-T-TB-sharp-v1 (T2-R2) | N_s | 1.0578e-4 | 3.7930e-6 | AUDITED (T4-028) |
| FW-T-TB-graded-v1 (per-level boxes) | graded components | box-dependent | 4.5717e-4 | AUDITED (T4-013) |
| FW-T-TB-gradedL2-v1 | graded components, no H | box-dependent | 4.5717e-4 | AUDITED conditional (T4-039) |
| FW-T-T4L2-v1 (T4-019) | NORM-T-X3-v1, s = 2^-17 | 1/163840 (above 6.1035e-6) | fixed ball r = 2^-14: 2^-23 | AUDITED conditional |
| FW-T-T4ALT-defect-v1 | defect form | epsilon_max 1.8938e-7 (box below) | not computed | AUDITED conditional (T4-062) |
| FW-T-TE-eqthr-v1 | equal-threshold weighted | none | - | OPEN (no high inverse) |
| FW-T-TC-woodbury-v1 | finite-rank | none | - | OPEN (used in statL) |
| FW-T-TB-frac-v1 | fractional commutator | none | - | HEURISTIC |

The FW-T-T4ALT-defect-v1 value epsilon_max 1.8938e-7 is for the box m = 2^-17, B = 1/100, s = 2^-18; for m = 2^-16,
B = 1/200 it is 6.1967e-8 (the T2 theory worker handoff M2).
The TB-rebal ceiling is 3.51254748112...e-7 (the T2 theory worker handoff BE1 and BE3, Arb at 256 bits; CONFIRMED by the T4 theory auditor T4-454,
which also proves 3.5125e-7 < ceiling < 3.5126e-7), so the earlier display 3.5125e-7 rounds to nearest, not up;
3.5126e-7 is the upward rounding (section 11 item 75). The other ceilings of this table are upward roundings of their
exact values (BE2, CONFIRMED by T4-454). Statements "from 3.5125e-7 up" include the exact TB-rebal radius, and since the
velocity thresholds decrease as the radius grows (BE3), upper bounds computed at 3.5125e-7 hold there.
At the exact radius b = 3.512547481120918...e-7, the T2 theory worker's FALSIFY revision 3 (handoff BI, CONFIRMED by the T4 theory auditor in
T4-464, 199 checks at 768 bits) bounds the 007 endpoint row: the retained-shape cutoff is at most 0.6720573 and, with
V >= v0, it lies in [0.6372611, 0.6372960]; over the bracket [3.5125e-7, 3.5126e-7] these are at most 0.6720590 and
[0.6372593, 0.6372977]. All lie below Emin = 0.7930365..., so the retained-shape obstruction stands; the crude cutoffs
stay above Emin and are inconclusive. T4-464 REFUTES the earlier 007 lower end 0.6372628 as an exact-radius bound (at b
the value is below 0.6372612); the earlier upper ends stay conservative. No verdict changes.

For 007, the N3 numerics worker's complete enclosure 606.818151 < E_2(F) < 606.820219 and its four registered N_s values are CONFIRMED
(N4-252, from the CONFIRMED components G0, G1, P2, Q3 and the H enclosure); each of the four N_s smallness tests fails,
the smallest ratio to its threshold being above 5712796. The rebalanced threshold is exactly 3/327680; the earlier
display 9.1553e-6 is its upward rounding (N4-252). The FW-T-T4L2-v1 threshold is exactly 1/163840 = 6.103515625e-6;
the display 6.1035e-6 is its downward rounding, so a ratio to it must be formed with the exact value. The N3 numerics worker (17:56Z)
regenerated its 007 record with both exact thresholds; N4-429 CONFIRMS the corrected 007 ratio floors 84699685 (X3)
and 66246337 (rebal) and REFUTES the earlier 84699902 as the quotient by 1/163840 (not as a bound on the norm). This
document quotes neither ratio. These are failures of sufficient conditions, not distance bounds.

### 2.6 A weaker high space: FW-T-DYADIC-Y-v1[a, s, Rw] (the T4 theory auditor T4-058; AUDITED conditional: the review of T4-058, T4-095)

- Space: Y = NORM-T-DYADIC-Y-v1[a, s, Rw], a scale-adapted dyadic H^(2+s) norm with low space H_a = L^2(w_a^2) (w_a =
  (1 + r^2)^(-a/2)) and low-weight radius Rw. The low weight decays, so the norm does not control ||h||_2 and the L^2
  distance does not transfer to its ball; a weighted probe is needed (NC-T-WDIST; T4-260). It is the one registered
  framework of the "weaker space" type of PROMPT section 5.
- Hypotheses: :H1 velocity ||w U[h]||_2 <= C_U ||w h||_2; :H2 background (smooth S1, V globally Lipschitz and
  complete, u sublinear, D rho bounded, a0 > 0, c + d_y u2(0) = 1); :H3 low energy
  Re <L h, h>_(H_a) <= -beta ||h||_(H_a)^2; :H4 high resolvent: Y(A_k^-1 f) <= M Y(f) for every k in B_R and every
  f in Y with f_y(0) = 0; :H5 F in Y; :H6 closure M Y(F) <= R, C1 R (C_U + a) < beta, C1 R < a0, with
  C1 = [4 pi s (1 + s)]^(-1/2).
- Conclusion: a unique h in B_R with rho + h an exact stationary profile; threshold
  eta_max = min(beta/(C1 (C_U + a)), a0/C1)/M.
- Status: :H4 is OPEN for every candidate and is impossible at the origin for s >= c - 1 (NC-T-ORIGIN-INV). RULED OUT
  (AUDITED conditional) at state 131 for every a, s, Rw (T4-099 chain, T4-114, the T1/T3 theory worker R1-013), at d2 for every 0 < a < 2,
  0 < s < 1 and finite Rw (T4-112, T4-120, R1-014), and at 007 for every 0 < a < 2, 0 < s < 1, Rw > 0 (T4-127 on 4/5 <=
  a < 1 + 1/c, T4-147 on (0, 1 + 1/c), NC-T-WRATE above). At 008 every one of the seven cells fails (N4-186, minimum
  ratio > 4.64864536, CONFIRMED by T4-248); at 009 every cell fails with minimum ratio > 1.02032822 (N4-187, CONFIRMED
  by T4-250; both accepted in N4-193); at 010 every cell fails with minimum ratio > 5.78998556 (N4-231, CONFIRMED by
  T4-303 and N4-244). At 016 (N4-355: The N4 numerical auditor's own complete computation of the mode 1 and 3 norms J(1/4) and J(7/4),
  which independently verifies the N3 numerics worker's CLAIMED seven-cell record; minimum ratio above 1.253908386497; conditional on the
  hypotheses of the origin inverse theorem; matrix row 98, v126) every cell fails; the two-evaluation test of N4-355
  uses J(1/4) on the first cell and J(7/4) on the other six, valid since J is nonincreasing in a, after the 007
  calibration N4-354. At 015 the N4 numerical auditor's N4-382 (14:11Z) independently reproduces the N3 numerics worker's seven-cell record of 13:27Z (exact
  mode 1 and mode 3 projected energies, every contributing background mode retained, 2048 bits): every cell fails,
  minimum ratio above 1.242922259074, CONFIRMED under the hypotheses of the FW-T-DYADIC-Y-v1 argument; closure matrix
  row 105 (v135) records 015 RULED OUT in FW-T-DYADIC-Y-v1 for every 0 < a < 2, 0 < s < 1 and finite Rw under the
  audited framework hypotheses and the candidate hypotheses checked in N4-382. The T4 theory auditor's T4-461 (14:52Z) reproduces N4-382
  independently (739 checks). At 017 the N4 numerical auditor's N4-389 (14:56Z) CONFIRMS the N3 numerics worker's seven-cell record (CLAIMED, 14:22Z) by its
  own complete computation of J(1/4) and J(7/4): under the same hypotheses every cell of 0 < a < 1 + 1/c fails, minimum
  ratio above 1.221854480167 (two-evaluation cover); closure matrix row 106 (v138) records 017 RULED OUT in
  FW-T-DYADIC-Y-v1 on this basis, one sufficient scheme removed, not a profile; the T4 theory auditor's T4-463 (15:05Z, 1070 checks at
  1024 bits) CONFIRMS N4-389 independently, so row 106 is accepted both ways (v139). Not tested at 011 to 014 and 018
  to 027. No full-family L^2 result transfers to the decaying-weight dyadic ball.

### 2.7 Localized low-energy route (the T2 theory worker note on the localized (B-L2) margin; ingredients, no framework)

- L1 (AUDITED, T4-157): in L^2 the best energy rate of A_0 lies in [1 + c - sup theta - kappa, 1 + c - sup theta].
- Lemma C and L2 (AUDITED, T4-157): with theta <= theta_c + theta_1, theta_1 >= 0, and w = e^psi, psi bounded,
  g = V.grad psi, the rate in L^2(w^2) is at least
  ess inf(1 + c + g - theta_1) - theta_c - kappa - C_T ||grad theta_1||_2 - omega,
  C_T = sqrt((4 log 2 - 1)/(8 pi)) = 0.2655730865568873, omega <= ||grad rho||_inf (e^(osc psi) - 1) or its
  Hilbert-Schmidt replacement (T4-163, T4-176 AUDITED).
- L3 (AUDITED, T4-168): a rate beta in L^2(w^2) forces V.grad psi >= theta - (1 + c - beta) almost everywhere.
- Weights exist under a global Lipschitz outward flow (T4-170, the T1/T3 theory worker R1-020, T4-180, T4-183).
- Relation to the distance. After the normalization inf psi = 0, ||h||_2 <= ||e^psi h||_2, so a localized ball of
  radius r contains only corrections with ||h||_2 <= r, and the necessary radius transfers with constant 1 (T4-260).
  For 007 a framework on this route therefore needs an admissible radius above 0.004769166867. No upper ceiling on
  the admissible radius of this route is proved, so it is not excluded; no theorem with such a radius exists, and no
  weight has been constructed for any candidate.
- Localized corrections in the registered norms (theory_v04 R2 item 6, answering the coordinator 05:33Z item 3;
  artifacts/checks/annulus_admissible.py). Lemma A (elementary, CLAIMED by the T1/T3 theory worker): if h in H^2(R^2) is supported in r <=
  R_out and has only sine modes n >= n0, then ||D^2 h||_2 = ||Delta h||_2 >= (n0/R_out)^2 ||h||_2. Lemma A and the
  fixed-ball bound are CONFIRMED by T4-278. For globally H^2 corrections supported at 20 <= r <= 32 with only sine
  frequencies n >= 19 this raises the sharpw bound E_w(h)/||h||_2 only from 1024 to 1029.647... (at most 1029.648), so
  the sharpw fixed ball admits ||h||_2 <= 1.312585972e-6 and every ball of the sharpw family with a positive margin
  admits ||h||_2 < 2.839272409e-6 (the conservative uniform repair of T4-278, since the X ceiling is attained at s =
  3.258e-4 > 1/5184; draft 5 printed 2.835e-6, REFUTED as a family ceiling): more than 701 times below the 013 distance
  and 1679 times below the 007 distance. The hypotheses concern the correction h itself, not the residual, and the bound
  holds only under them (T4-373): the unrestricted sharpw family ceiling is (2 mu0/3) sqrt(mu0/(3 C'))/((8/5) 1024) =
  2.84957773827575...e-6, mu0 = 97/250, C' = 397 (rounded up 2.8496e-6); the two numbers bound different classes. A
  graded box admits less than 50/(651 sqrt(28248)) < 4.5717e-4 in any location (factors 4.357 and 10.43), and so does a
  graded box whose low row is replaced by ||w J^s h||_2 with w >= 1 while the original high row and top margin are kept
  (T4-277, AUDITED through the T1/T3 theory worker R1-032, second review the T2 theory worker the review of T4-277: ||h||_2 <= ||h||_(H^(2+s)) < 25/54684). For
  decaying low weights there is only a HEURISTIC extrapolation at the limit exponents (at most 1.638e-4, factors above
  12.16 and 29.12; the excluded critical top weight (1 + r^2)^((1 - gamma)/2) would give at most 2.169e-3). No general
  statement about substantially different norms (a new high-row estimate, decaying weights with their own inverse) is
  proved (T4-278). The T2 theory worker adds (handoff AJ2, CONFIRMED by the T4 theory auditor T4-290 under the unchanged high-row margin and
  norm-domination hypotheses) that localizing only the low row of a T4L2 ball leaves b_fam unchanged when its radius cap
  comes from the high row. For an exactly compactly supported correction the T4 theory auditor proves more: the zero mass of an S1
  compact correction gives F = O(r^(gamma - 4)) outside its support, while 007, 013 and 014 have an exactly nonzero
  residual sector at the exponent -11375183046454913/4076476460239181 = -2.79044 > gamma - 4, so none of them has a
  compactly supported L^2 correction (T4-281, AUDITED through the T1/T3 theory worker R1-033, review set 30; the T1/T3 theory worker exact code and the N1/N2 numerics worker
  sector tables give the same coefficient). Mostly annular corrections with nonzero tails are not covered. Of the
  fourteen residual sectors above gamma - 4, three are exactly nonzero for all three candidates, (l, q) = (4, 1), (9, 0)
  and (5, 1) at exponents 1 - l delta - 2q; a design that admits compactly supported corrections must make all three
  vanish. The T2 theory worker (the review of T4-281, a second review that CONFIRMS T4-281) adds R2 (AUDITED through the T1/T3 theory worker R1-034 and the T4 theory auditor
  T4-305, numbers CONFIRMED): an exact compact correction forces the endpoint sector (1, 2) at gamma - 4 to be -(M_y/pi)
  P with P = gamma cos(2 theta) Theta_0 + sin(2 theta) Theta_0' (M_y = int y h), and then ||h||_2 >= 2 sqrt(pi)
  |lambda|/A^2 if F_(1,2) = lambda P and supp h lies in the disk of radius A. For 007, 013 and 014 the sector is not of
  that form (relative residual 0.629386, 0.629396, 0.629385 after the best multiple). That sector comes from
  branch j = 0 only, so a redesign confined to branch j = 3 leaves this second obstruction unchanged. R2 is a necessary
  condition for exactly compact S1 L^2 corrections at fixed c only; it does not exclude the noncompact tail direction of
  T4-295 (T4-305 scope). T4-295 (the T4 theory auditor research/forced_integrable_tail section 3; AUDITED through the T1/T3 theory worker R1-034,
  review set 31, accepted in T4-315, numbers CONFIRMED by artifacts/checks/check_T4295.py) is such a redesign: with
  chi_3 = (1 + r^2)^p sum_m P_m(t) cos(2m theta), p = 2 gamma and A1_m = p P_m(1) - P_m'(1), the potential
  eta_chi = -(1 + r^2)^p sum_m A1_m t^(m+4) (1 - t) cos(2m theta) cancels the density and stream sectors (4, 1) exactly,
  keeps every leading sector and the origin data through cubic order, and leaves no nonzero residual sector of exponent
  at least -3. The first one is (9, 0) at -3 - epsilon_1, epsilon_1 = 116183978028673/4076476460239181, so the residual
  of R + eta lies in E_a at infinity for every a > -2. It is a design operation, not a candidate: ||eta||_2 > 4373.34
  for each of 007, 013 and 014 (T4-316, CONFIRMED), so no certified number transfers to R + eta; the (5, 1) residual
  grows from 175465 to 191042 (circle L^2); (9, 0), (5, 1) and the endpoint (1, 2) still exclude compact corrections of
  R + eta; and T4-294, which needs a first exponent in (-3, 0), gives no forced tail for R + eta as stated; the T2 theory worker
  the review of T4-294 R2 (AUDITED through T4-317) extends it below -3 with a dipole velocity bound and finds a forced (9, 0)
  tail (section 3.4). The same cancellation is the set of 40 exact linear constraints A1_m = 0 on the branch-3
  generators, which an optimizer can impose directly (R1-034 remark (e)). T4-314 (the T4 theory auditor research/far_out_tail_repair;
  AUDITED through the T1/T3 theory worker R1-035, review set 32, numbers checked by artifacts/checks/check_T4314.py; accepted in T4-325;
  second review the T2 theory worker the review of T4-314, accepted in T4-333) shows that the size of eta is not the cost of the cancellation.
  For -3 < q < -1, a finite cosine sum A(theta) = sum A_m cos(2 m theta) and a smooth cutoff zeta (0 on r <= 1, 1 on
  r >= 2), the potential chi_L = -zeta(r/L) r^(q+3) A(theta) gives h_L = -d_y Lap chi_L, which is smooth, S1, zero on
  r <= L and exactly homogeneous of degree q on r >= 2L, with canonical velocity v_L = (-d_y psi_L, d_x psi_L), psi_L =
  d_x d_y chi_L, and ||h_L||_2 = C_00 L^(q+1). With A_m = A1_m of T4-295 and q = 4 gamma - 5, R + h_L has zero density
  and stream (4, 1) sectors, first residual sector (9, 0) and the origin jets of R, and h_L lies in E_a exactly for a >
  4 gamma - 4. The residual change has the exponents q + 1, q + gamma and 2q in L, under growth bounds on U[R] and grad
  R for r >= R_0 whose constants are not computed for any candidate, so it is a limit statement. For 007, C_00 is about
  215936.9 (mpmath, 40 digits, not interval certified), and ||h_L||_2 < epsilon holds exactly when L >
  (C_00/epsilon)^(1/(-q-1)); for epsilon = 1e-3 the FLOAT value of this radius is about 45174.312 (T4-329: a FLOAT
  estimate for this cutoff family, not a radius needed by every repair), far beyond the N1/N2 numerics worker mesh (r <= 8356). Any
  certified distance exclusion whose margin exceeds ||h_L||_2 transfers to R + h_L by the triangle inequality. The
  trade-off is in the weighted classes (R1-035 remark (b), CONFIRMED by T4-326, the T4 theory auditor
  audit record tail_cutoff_weighted_cost, proof, with explicit finite-annulus lower bounds and the logarithmic endpoint
  a = q + 1): for -2 < a < 4 gamma - 4 and M = ||F_(4,1)||_(L^2(d theta)) (M = 4905.09... for 007), ||F(R +
  h_L)||_(E_a) >= (1 - o(1)) M (2 (q + 1 - a))^(-1/2) L^(q+1-a) as L tends to infinity, so the weighted residual grows
  without bound as ||h_L||_2 tends to 0; the registered L^2-based frameworks (a = 0) are not affected. This is a
  trade-off of this construction, not a lower bound for every tail repair or every framework (T4-326). Other norms
  (the T2 theory worker the review of T4-314 R2 and R3, CONFIRMED by T4-334, the T4 theory auditor audit record cutoff_norm_extensions, proof): for q < -2 and
  0 < sigma <= 1, ||h_L||_(Hdot^-sigma) <= L^(q+1+sigma) C_00^(1-sigma) ||h_1||_(Hdot^-1)^sigma, which tends to 0; in
  the weighted C^1 norm H_q of T4-294 the cost does not vanish, ||B||_infinity <= H_q(h_L) <= 2^(1-q) J_q(h_1) with B
  the nonzero exterior profile of h_1, so the cutoff is small in L^2 and in Hdot^-sigma but not in the class of the
  forced-tail theorems. For fixed L the residuals F(R + h_L) and F(R + eta) have identical coefficients at every
  exponent at or above gamma - 4, the endpoint sector (1, 2) included; the first remaining sector is (9, 0), and the
  others at or above gamma - 4 are (5, 1) and (1, 2). The forced (9, 0) tail of section 3.4 applies to a new correction
  k of R + h_L only under H_(1-9 delta)(k) < infinity (T4-334). T4-324 (the T4 theory auditor research/homogeneous_tail_surgery; AUDITED
  through the T2 theory worker the review of T4-324, accepted in T4-337; the numerical cutoff constants and radii are FLOAT, and the second
  radius and its background constants depend on the first repair) extends the construction. For q < -1, a = q + 3
  outside {0, +-2, ..., +-2M} and an odd sine polynomial B(theta) = sum_(l <= M) b_l sin((2l + 1) theta), there is a
  unique even cosine polynomial P(theta) = sum_(m <= M) p_m cos(2 m theta) with -d_y Lap[r^a P] = r^q B, given by an
  explicit upper bidiagonal recursion; a smooth cutoff of r^a P at a large radius realizes the tail r^q B at arbitrarily
  small L^2 cost, with vanishing first moments for q < -3. Applied twice to 007, 013 and 014, first to (4, 1) (its 40
  coefficients per candidate agree with the accepted A1_m) and then to the forced (9, 0) sector (90 exact coefficients
  per candidate), it leaves a residual O(r^(-1-5 delta)), the exponent q3 = -1 - 5 delta of the sector (5, 1). The first
  cutoff changes the (5, 1) coefficient (its mixed exponent is q1 - delta = q3, q1 = 4 gamma - 5); the second preserves
  it, since its mixed and quadratic exponents q2 - delta = 1 - 10 delta and 2 q2 - 1 = 1 - 18 delta lie strictly below
  q3 (delta > 2/5; T4-336, as in the source proof of T4-324). T4-338 (the T4 theory auditor research/finite_tail_surgery) CONFIRMS
  the T2 theory worker's review of T4-324 R2 and R3 under explicit finite angular, differentiated remainder and growth hypotheses:
  finitely many cutoffs clear every residual sector above a fixed nonresonant exponent. Its third cutoff (exact sector
  checks for 007, 013 and 014; AUDITED through the T2 theory worker the review of T4-338, accepted in T4-365) removes (5, 1) and preserves (1,
  2), which is then the only leading sector; the common third angular density coefficient has circle norm in (27840,
  27842). T4-339 (AUDITED through the same review, T4-365; T4-335 is AUDITED, T4-350) excludes every stationary weighted
  C^1 correction decaying faster than r^(gamma - 4) for this reference (circle-norm lower bounds 85017, 85018 and 85016
  of the angular coefficient; the floors of d/(4c) are 85018, 85019 and 85017, the review of T4-338 check (h)); a fourth cutoff
  can remove the endpoint (the review of T4-338 R4, CONFIRMED by T4-368, which also CONFIRMS the two-term endpoint expansion
  with the (10, 0) forcing term and leaves a finite-radius remainder bound OPEN), so no obstruction to finite reference
  design is claimed. Neither construction gives a stationary solution or makes a fixed nonzero residual tend to 0. The
  cutoff lies outside the present polynomial basis; the cost of the 40 constraints A1_m = 0 inside the basis is OPEN.
  The lever the evidence indicates is the basis at r from 20 to 100.

### 2.8 Thresholds against analysis2

| framework | threshold | ratio to FW-A2-Db | L^2 family ceiling | ratio to FW-A2-Db ceiling |
|---|---|---|---|---|
| FW-A2-Db | 6.3578e-7 (N_s) | 1 | 6.8626e-8 | 1 |
| FW-T-TB-sharp-v1 | 1.0578e-4 (N_s, s = 2^-13) | 166.3 | 3.7930e-6 | 55.2 |
| FW-T-T4L2-sharp-v1 | 7.6219e-5 (X_(s,w)) | 119.8 | 3.0927e-6 | 45.0 |
| FW-T-T4L2-sharpw-v1 | 2.1035e-4 (X_(s,w)) | 330.8 | 2.8496e-6 | 41.5 |
| FW-T-T4L2-bL-v1[7/5] | 1.692e-4 (X_(s,w)) | 266.1 | 2.5362e-6 | 36.9 |
| FW-T-T4L2-defect-v1 (sharpw, g = 0) | 2.1046e-4 | 331.0 | 2.8496e-6 | 41.5 |

Ratios are rounded down. The defect row at g = 0 prints eta* (section 2.1) rounded down. The thresholds are in
different norms, and their ratios compare tolerances, not residual balls:
at s = 2^-18 and t = 1/5184 neither forcing space contains the other (T4-259; the multiplier (1 + |xi|^2)^((t - s)/2) is
unbounded at high frequency and |xi|^-1 at low frequency). The X_(s,w) frameworks need fewer far-field cancellations and
slightly more fractional regularity; the same caution applies to FW-T-TB-sharp-v1 (N_s at s = 2^-13). The best constants
cannot gain much more: better state 131 matrix floors raise the sharp and sharpw thresholds by at most 2.2 and 1.81
times with all other constants fixed (T4-119; ceilings, not attainable improvements; for the weights, the T2 theory worker's
Proposition WU3 (handoff BJ2; CONFIRMED by the T4 theory auditor T4-462 with an exact elimination of both weights, w2 >= [1440 p + (6
O + 5 a)^2]/((beta - mu) p a^2), p = m2 - mu, a = m1 - mu, O = 347/10, itself CONFIRMED by the T1/T3 theory worker R1-047 and by the T2 theory worker
the review of T4-462 (handoff BM, which records WU, WU3 and the bL cap as AUDITED), both accepted by the T4 theory auditor in T4-468, and
derived independently by the N4 numerical auditor in N4-395) gives, with the registered state 131 floors M1 >= (9/10) I and M2 >= (1/2) I
(:H3), w1 >= 2, w2 >= 1, C >= K00 > 390.68, c_U >= A' + B' > 1.5871 and X(h) >= sqrt(w2) ||h||_2, at every weight pair:
T2-R3 balls (beta 2) have ||h||_2 < 3.3469e-6, at most 1.1746 times the sharpw ceiling, and balls of the T2-R1 TB-sharp
matrix with E0 as one component (beta 11/4) have ||h||_2 < 4.0249e-6, at most 1.0612 times the TB-sharp ceiling (the T2 theory worker
BH3, BO5), so 007 is excluded at every weight by factors above 1424.9 and 1184.9; its sampling test reaches 0.9994 and
0.9995 of these bounds, FLOAT, for the relaxed algebraic problem with C = K and c_U = v only (the T2 theory worker BM2 displays suprema
3.34629e-6 and 4.02421e-6 to six digits; T4-468 certifies these displays only for the relaxation with the rounded
constants k = 390.68 and u = 1.5871, as rounding cells, not as exact suprema with the exact K and v and not as directed
bounds), so sharpness for the full scheme, whose commutator constant usually exceeds K, is OPEN (T4-462); since the
unweighted bL margin forces beta_L <= 1 + c < 57/20, the same bound at beta 57/20 covers every bL ball at every weight
pair, ||h||_2 < 4.1069e-6 (4.0746e-6 at 1 + c0), 1161.2 times below the 007 distance (handoff BK2, CONFIRMED in T4-462;
not the weighted margin (B-L2-w), separate weights on b and on the H part of E0, other Gram schemes, or balls whose L^2
control is not sqrt(w2) ||h||_2, handoff BH3 and BO5); the weaker Proposition WU of handoff BH3, 6.7691e-6, stays true),
and the ceiling formula gives b_fam = (2 mu0/3) sqrt(mu0/(3 C))/(c_U sqrt(W2)), so the ceiling grows only like mu0^(3/2).
G_w(mu0) > 0 needs mu0 < 1/2, so with c_U = 8/5 and w2 = 2^20 fixed, lifting the sharpw ceiling above the 007 distance
needs (mu0/(97/250))^(3/2) (397/C')^(1/2) > 1673, hence C' < 397 (125/97)^3/1673^2 = 775390625/2554506927217 < 3.04e-4,
more than six orders of magnitude below the certified C' = 397 (CONFIRMED by T4-358 for this family formula with c_U and
w2 fixed; it says nothing about other high-row estimates).

## 3. Strongest new estimates

Each item gives the statement, its status and its source. "Elementary" means a short proof given in the source.

### 3.1 Velocity bounds

- (V0) ||U[h]||_2 <= ||h||_2 for every h in L^2, since |sigma(xi)|^2 = xi1^2/|xi|^2 <= 1. Elementary.
- (V1) Weighted L^2 (T4-177, AUDITED through the T2 theory worker the review of T4-177): for centrally odd h (every S1 function is
  centrally odd) and w_p = (1 + r^2/R^2)^(p/2), |p| < 2, ||w_p U[h]||_2 <= 2/(2 - |p|) ||w_p h||_2. This makes the
  velocity hypothesis of T4-189 automatic on S1 (the T1/T3 theory worker R1-023 R1).
- (V2) Derivative tensors (T4-206, AUDITED by the T1/T3 theory worker R1-026, accepted in T4-223): for compact real centrally odd h,
  w = (1 + r^2/R^2)^(1/2) and the full ordered derivative tensor D^k,
    ||w D^k U[h]||_2 <= sqrt(1 + 2/(k + 1)) ||w D^k h||_2, k = 0, 1, 2, ...
  (sqrt 3, sqrt 2, sqrt(5/3) for k = 0, 1, 2). The sharp constant is sqrt(max(1, Lambda_k)) with Lambda_k the top
  of an explicit angular generalized eigenvalue problem (R1-026 R2; variational formula CONFIRMED by T4-224); the
  values Lambda_0 = 1.892365 and Lambda_2 = 1.255295 are FLOAT (artifacts/checks/t4206_angular_sup.out), giving
  about 1.3756 (k = 0), 1.1869 (k = 1) and 1.1204 (k = 2). No inverse uses (V2) yet; it is an input for a
  compatible derivative hierarchy.
- (V3) In FW-T-T4L2-sharp-v1, sharpw-v1 and the bL variants the velocity product constant is c_U = 8/5 (sharp kernel
  constants T2-R2, AUDITED with these frameworks, T4-042 and R1-006), against 5 in A2 and in the trans and statL
  variants.

### 3.2 Signed L^2 coercivity

- (C1) T4-016 (AUDITED): the symmetric remainder of h -> U[h].grad rho in L^2 is Hilbert-Schmidt with norm at most
  kappa, kappa^2 = [(log 2 - 1/2) ||D rho_x||_2^2 + (3 log 2 - 2) ||D rho_y||_2^2]/(16 pi). Together with
  theta = ess sup (|grad rho| - rho_y)/2 this gives the low rate c + 1 - theta - kappa of (B-L2) (T4-019, the S1
  form of the Hou-Nguyen-Wang L^2 coercivity, TM-23).
- (C2) Compression (the T1/T3 theory worker R1-016 with T4-128 to T4-138, AUDITED; scope T4-261): with the Gram matrix G and compression B
  of an angular block, the trace tr(G^-1 B G^-1 B) may be subtracted from kappa_HS^2 for the parity blocks complementary
  to S1 only. A compression inside S1 needs the signed repair: sup spec(K|S1) <= sqrt(kappa_HS^2 - T_other - T_S1 +
  q^2), where T_other and T_S1 are the compression traces of the complementary blocks and of the S1 block, q >= 0 and q
  G - B is positive semidefinite; this is a quadratic-form upper bound, not an operator norm bound (T4-133; T4-138
  combines overlapping compressions; the T4 theory auditor signed_compression_budget). For 008 the combined signed bound
  0.78617626895254670632 (T4-143 with N4-126 and N4-127, numbers accepted in T4-151) is AUDITED conditional, against
  kappa_HS = 0.84604142762615305 (N4-107, T4-126). It relaxes (B-L2) only.
- (C3) Values: 007 kappa_HS = 0.72816468018232542728 (N4-092 with T4-111, CONFIRMED) and (B-L2) holds for the exact 007
  with rate > 2.00215 (N4-111, T4-162). 009 kappa_HS = 0.71321453930810894999 (N4-121, T4-166). For the exact 017, the N4 numerical auditor
  N4-309 reports a complete 247-leaf rational cover with theta <= 2/25, so that with kappa < 0.729080538628955349
  (T4-366, accepted in N4-303) the rate c + 1 - theta - kappa exceeds 2.00123867. Its reconstruction N4-284 is CONFIRMED
  by T4-378 and its range theorem N4-285 by T4-377, and every leaf is replayed independently at 2048 bits by T4-400
  (accepted in N4-329), so the cover is CONFIRMED. It is a structural hypothesis for a candidate that stays RULED OUT by
  its distance certificates.
- (C4) Localized rates (T4-157, T4-163, T4-168, T4-176, AUDITED): Lemma C, L2 and L3 of section 2.7 with
  C_T = sqrt((4 log 2 - 1)/(8 pi)) = 0.2655730865568873.

### 3.3 The distance obstruction and the Newton step

- (D1) Probe inequality (T4-064 for a = 0, T4-081 weighted, AUDITED; angular form T4-185, AUDITED by the T1/T3 theory worker R1-022).
  For a smooth S1 probe phi of the NORM-T-WEAK-v1 class put I_phi = <F(rho; c), phi>,
  M_phi = (2c + 1) phi + (cX + U[rho]).grad phi and D_phi = ||M_phi||_2 + C_U ||phi grad rho||_2 (C_U = 1 at a = 0).
  Every real S1 h in L^2 with F(rho + h; c) = 0 satisfies |I_phi| <= D_phi ||h||_2 + H_phi ||h||_2^2, with H_phi the
  certified constant of the quadratic pairing. So the closed ball ||h||_2 <= b contains no solution if
  |I_phi| > D_phi b + H_phi b^2. The inequality must be strict for a closed ball (T4-217; with equality only the
  open ball is excluded); every exclusion in this report has a strict positive gap.
- (D2) Budget (the T2 theory worker O3, AUDITED by T4-065): a framework whose ball is {X(h) <= r} with X(h) >= sqrt(W2) ||h||_2 and
  whose rate is mu0 - C s - c_U r/sqrt(s) admits only corrections with
  ||h||_2 <= b_fam = (2 mu0/3) sqrt(mu0/(3C))/(c_U sqrt(W2)). b_fam is a universal family ceiling: no ball of the
  family with a positive rate contains a correction of larger L^2 norm; a stated fixed ball of radius r gives the
  smaller r/sqrt(W2) (T4-262). Values: 6.8626e-8 (FW-A2-Db) to 3.7930e-6 (FW-T-TB-sharp-v1, the largest scalar
  ceiling); 4.5717e-4 for the graded boxes (NC-T-GRADED-L2; it bounds the full H^(2+s) norm, T4-261).
- (D3) 007: every real S1 correction h in L^2 with F(rho_007 + h; c) = 0 has ||h||_2 > 0.004769166867 (T4-185 with
  the mode-7 probe phi_7 = r W^2 P(t) sin(7 theta); AUDITED by R1-022, CONFIRMED by N4-157). With T4-211 (R1-028)
  the same holds, up to 3.424e-12, around the Taylor-repaired reference.
- (D4) Lemma W (the T1/T3 theory worker, theory_v03 R6(a); CONFIRMED by T4-214, so AUDITED). If h0 in L^2 is S1 and L h0 = -F holds
  tested against a probe phi of (D1), then |I_phi| <= D_phi ||h0||_2. So every exact L^2 Newton step from 007 has
  norm > 0.0047694 (I/D = 0.00476940290877443236, 512-bit Arb, T4-214). No inverse or convergence is implied.
- (D5) Held-out bound (theory_v03 R9(e), CONFIRMED by T4-214): for every S1 h0 in L^2,
  |<F + L h0, phi>| >= |I_phi| - D_phi ||h0||_2. A Gauss-Newton step from 007 with ||h0||_2 < 0.0047694 leaves the
  mode-7 pairing of the linearized residual at least 1.7647e-5 (1 - ||h0||_2/0.0047694) in absolute value.
- (D6) Reading of the weak tests (theory_v03 R6(b), corrected domain, T4-214). If L: D(L) -> L^2 is closed and densely
  defined with bounded inverse on the S1 part of L^2, and the probe space has dense image under L*, then
  sup over phi of |I_phi|/||L* phi||_2 = ||L^-1 F||_2, and D_phi >= ||L* phi||_2. The weak tests are lower estimates
  of the first L^2 Newton step; they are not a statement that L is invertible.

### 3.4 Exponent, dilation and chart geometry

- (G1) Exponent pinning (T4-189, AUDITED by the T1/T3 theory worker R1-023 and the T2 theory worker the review of T4-189). Let 0 < gamma < 1 and rho be a
  smooth S1 density with |u| <= C r^gamma, |grad rho| <= C r^(gamma - 1) and rho = r^gamma Theta + o(r^gamma)
  uniformly, Theta not zero. If h and U[h] are in L^2((1 + r^2)^(-a)), 0 <= a <= 1 + gamma, and rho + h solves the
  stationary equation at c' in the divergence form, then c' gamma = 1. Sharp: for a > 1 + gamma, h = -rho works.
- (G2) Common leading profile (T4-203 with N4-165; T4-210 with N4-172, accepted in T4-213): state 131, d2 and
  005 to 012 share the exact nonzero leading profile of 007 (first sine coefficient 18.5678222975).
- (G3) Exponent changes are not linear (T4-205, AUDITED by the T1/T3 theory worker R1-025, accepted in T4-220). For E_a =
  L^2((1 + r^2)^(-a)) and T_gamma = chi r^gamma Theta, gamma >= a - 1: the classes of T_gamma are independent modulo
  E_a, no finite logarithmic Taylor correction represents an exponent change, and gamma -> T_gamma is smooth into
  E_b, b > 1 + max gamma, with ||d_gamma^N T_gamma||_(E_b)^2 <= ||Theta||^2 (2N)!/(2 eps)^(2N+1),
  eps = b - 1 - max gamma. The exponent is uniquely determined on the union of the affine classes but not continuous
  in E_b (R1-025 R1, CONFIRMED by T4-221).
- (G4) Dilation (T4-222, AUDITED: CONFIRMED by the T1/T3 theory worker R1-027, accepted in T4-232). For 007, the fixed-c dilation orbit
  rho_lambda(X) = lambda rho(X/lambda) satisfies rho_lambda - rho - sum_(j in J_a) (lambda^((j+1) delta) - 1) T_j in
  E_a, T_j = chi r^(e_j) Theta_j, e_j = 1 - (j + 1) delta, J_a = {j <= 3: e_j >= a - 1}. The quotient span of the orbit
  is exactly |J_a|-dimensional: 4 for 0 <= a <= 4 gamma - 2 = 0.2095550..., 3 up to 3 gamma - 1 = 0.6571663..., 2 up to
  2 gamma = 1.1047775..., 1 up to 1 + gamma = 1.5523887..., 0 beyond. One tangent column Lambda rho is never enough for
  0 <= a <= 2 gamma (R1-025 R3, CONFIRMED by T4-221). The first sine harmonics of Theta_0, ..., Theta_7 are exactly
  nonzero (two independent exact routes, artifacts/checks/check_T4222.out).
- (G5) Lemma S (the T1/T3 theory worker, theory_v03 R7(a); CONFIRMED by T4-218 for the canonical velocity and finite norms). The
  dilation commutes with U and F, preserves S1, a0 and the strain, and scales ||g||_2 by lambda^2 and the NC-T-DIST
  radius by lambda^2. The asymptotic form of Lambda rho needs a differentiated remainder bound, which the algebraic
  candidates have.
- (G6) Forced lower tails (T4-234, AUDITED: reviewed by the T1/T3 theory worker R1-030, review set 26, accepted in T4-246). Let 0 < gamma <
  1, N = floor(2/delta), R = sum_(j<N) chi r^(e_j) Theta_j with smooth S1 profiles, and let the velocity of R + h, h in
  L^2, be the canonical one: U[R] = grad-perp(sum_j chi r^(e_j+1) Psi_j) minus the Biot-Savart field of the compact
  zero-mean curl defect, plus the Fourier U[h]. Here Psi_j is the sine-even solution of [d_theta^2 + (e_j+1)^2] Psi_j =
  -e_j cos(theta) Theta_j + sin(theta) Theta_j' (nonresonant since 0 <= e_j + 1 < 2). If R + h solves F = 0 in
  distributions, then for j = 1..N-1 j(c-1) Theta_j = sum_(l+m=j-1) [-e_m Psi_l' Theta_m + (e_l+1) Psi_l Theta_m'], so
  Theta_1..Theta_(N-1) are determined by Theta_0 (Theta_j of degree j+1); conversely these equations make F[R] square
  integrable. The velocity is unique among fields with div 0, curl -d_x rho, S1 parity and growth O(r^gamma) plus L^2
  (R1-030 R1, confirmed in T4-246); the excluded field is the strain alpha(x, -y). For 007 (N = 4), T4-235 (exact,
  CONFIRMED by N4-189) finds all 90 sector coefficients zero, and the T1/T3 theory worker reproduces this exactly from the raw generators:
  the recurrence seeded with Theta_0 alone gives Theta_1, Theta_2, Theta_3 (20, 30, 40 odd harmonics through 39, 59, 79;
  artifacts/checks/check_T4235x.out). No existence, inverse or estimate follows. A second review (the T2 theory worker
  reviews/the review of T4-234, CONFIRMED) adds, by exact arithmetic on the frozen data (its R3): d2, Mpen2, 005 and 007
  have the same c and exactly the same Theta_0 to Theta_3, so their pairwise differences are in L^2 and the four lie in
  one affine L^2 class; state 131 has the same c and Theta_0 but E_1 has 20 nonzero sine coefficients, so state131 + L^2
  contains no exact solution with the canonical velocity (as T4-202 already gives). Its remarks R1 (the candidates' own
  velocities are the canonical ones), R2 (among finite pure-power far fields with exponents in [-1, 1) an exact solution
  forces the ladder e_0, ..., e_(N-1)) and R4 (in L^2((1 + r^2)^(-a)), 0 <= a < 2, exactly the equations with a <= 1 +
  e_j are forced) are CONFIRMED by the T4 theory auditor (T4-254). T4-249 (weighted forced tails for -2 < a <= 1 + gamma) is AUDITED
  through the T2 theory worker the review of T4-249 (T4-268), and T4-256 (finite polynomial-logarithmic tails carry no logarithmic data, c >
  1, -2 < a <= 1 + gamma) is AUDITED through the T2 theory worker reviews/T2_256 (T4-271; scope of its resonance remark, T4-272). By
  the T2 theory worker exact arithmetic (handoff AG2, the review of T4-249 R3, CONFIRMED by the independent exact computation T4-291), no
  exact solution lies in candidate + L^2((1 + r^2)^(-a)) for state 131 at -2 < a <= 2 gamma, for d2 and Mpen2 at a in
  (-2, 7 gamma - 5] (7 gamma - 5 = -1.1332786170...), and for 005 and 007 at -2 < a <= 4 gamma - 4 = -1.7904449240...;
  for larger a T4-249 gives neither an obstruction nor existence. T4-292 (CONFIRMED, N4-240 and T4-308) finds the same
  first sector (4, 1), hence the same endpoint 4 gamma - 4, for 006, 008, 009, 012, 013 and 014, and T4-313 (exact, from
  the raw generators) finds it for 016, whose nonzero sectors down to exponent -7/2 are exactly (4, 1), (9, 0), (5, 1),
  (1, 2) and (10, 0). The T4-295 correction eta (section 2.7) lies in E_a exactly when a > 4 gamma - 4, so for -2 < a <=
  4 gamma - 4 the affine classes R + E_a and R + eta + E_a are different. The correction does not evade the exclusion
  above; it changes the class in which the exclusion was proved (the T4 theory auditor PROOF.md section 3; the T1/T3 theory worker R1-034). T4-294 (the T4 theory auditor
  research/forced_integrable_tail sections 1 and 2; AUDITED through the T2 theory worker the review of T4-294, CONFIRMED, accepted in T4-315;
  the T1/T3 theory worker found no error in a reading, review set 31). Let -3 < q < 0, let the reference R be C^1 and S1 with canonical
  velocity satisfying |U[R]| <= V r^gamma and |grad R| <= G r^(gamma - 1) for r >= R_0 >= 2 (true for the present
  algebraic references, whose far field is r^gamma Theta_0 plus lower tails; stated explicitly since T4-329), and let h
  be a centrally odd C^1 function with H = H_q(h) = max(sup (1 + |X|)^(-q) |h|, sup (1 + |X|)^(1 - q) |grad h|) finite.
  Then |U[h](X)| <= C_q H r^q for every r > 0, with C_q = 1/2 + 2^(-q) + 2^(1 - q)/(q + 3) + 2^(3 - q) + 2^(q + 2)/(-q);
  at q = -1 - 4 delta, 129.002791 < C_q < 129.002792. If R + h is exact at the same c and F(R) = r^q A + O(r^(q - eps)),
  then h = r^q A/(1 - c q) + O(r^(q - eps')), eps' = min(eps, delta, 1 - q). For 007, 013 and 014, A = F_(4,1) = (c q -
  1) Theta_(4,1), so h = -r^q Theta_(4,1) + O(r^(q - eps')) with eps' = 5 delta - 2 > 0.238: an exact correction in this
  class has a forced integrable tail. Consequences (the T2 theory worker the review of T4-294; AUDITED through T4-317 and T4-318, with the
  standalone proof the T4 theory auditor audit record dipole_forced_tail, proof): R3, no such h with H_q'(h) finite for some q' < -1 - 4
  delta makes R + h exact; R2, for gamma - 4 < q < -3 and r >= 2 the dipole bound |U[k]| <= C'_q H_q(k) r^(-3) holds;
  applied to the repaired reference R_eta = R + eta (same growth hypotheses) and a new centrally odd C^1 correction k
  with H_q2(k) finite, q2 = 1 - 9 delta, exactness of R_eta + k at the same c forces k = r^q2 F_(9,0)/(1 - c q2) +
  o(r^q2), with F_(9,0) the (9, 0) residual profile of R_eta; the total correction from R is h = eta + k (T4-329). The
  hypothesis H_q1(h) < infinity of T4-294, q1 = -1 - 4 delta, does not give H_q2(k), and an O(r^q2) value remainder
  alone does not give the derivative bound. The dipole constant is C'_q2 = D_q2 in (610.805532899, 610.805532900) (the T2 theory worker
  handoff AN3, T4-317). The forced (9, 0) profile has circle L^2 norm 5428.790031389... for each of 007, 013 and 014
  (T4-317). R3 holds in the weighted C^1 scope stated above (T4-318). R2 answers the T1/T3 theory worker R1-034 remark (d); the endpoint
  q = gamma - 4 is not covered. Moment-resolved endpoint theorem (T4-335, audit record moment_resolved_tail, proof with
  DOMAIN_ADDENDUM.md; AUDITED through the T2 theory worker the review of T4-335, accepted in T4-350). (i) Let -5 < q < -3 and let h be real,
  centrally odd and C^1 with H = H_q(h) = max(sup (1 + |X|)^(-q) |h|, sup (1 + |X|)^(1-q) |grad h|) finite. Then M =
  integral Y h(Y) dY converges absolutely and |U[h](X) + DK(X) M| <= E_q H r^q for r >= 2, with K the canonical kernel
  (contact term included) and E_q = 1/2 + 2^(-q) + 2^(3-q) + 2^(q+2)/(-q) + 2^(-q-2)/(-q-3) + 2^(2-q)/(q+5); E_q =
  133.0042547837... at q = gamma - 4 (Arb, the review of T4-335). Hence U[h] = O(r^q) if and only if M = 0. (ii) Let c > 1,
  q* = gamma - 4, and let R be a real C^1 S1 reference with continuous angular A, C^1 angular Theta, epsilon, eta > 0,
  finite V, G, E_F, E_R >= 0 and R0 >= 2 such that for r >= R0: |U_R| <= V r^gamma, |grad R| <= G r^(gamma-1), |F(R) -
  r^q* A| <= E_F r^(q*-epsilon) and |grad R - r^(gamma-1)(gamma Theta e_r + Theta' e_theta)| <= E_R r^(gamma-1-eta)
  (hypotheses (5)). If h is real, C^1 and S1 with H_q*(h) finite and R + h is stationary at the same c, then for r >=
  R0, uniformly in theta, h = r^q* [A + (m/pi) P]/(4c) + e, with m = integral y h, P = gamma cos(2 theta) Theta + sin(2
  theta) Theta', and e bounded explicitly by (7) of the source, so e = O(r^(q* - epsilon*)), epsilon* = min(epsilon,
  eta, delta, 4, 1 - q*). (iii) If moreover H_q'(h) is finite for some q' < q*, then A = -(m/pi) P; so no such
  faster-decaying stationary correction exists when A is not in span P, and the limit of ||r^(-q*) h(r, .)||_L2(circle)
  is at least d/(4c), d = dist_L2(circle)(A, span P). For the exact angular data of 007, 013 and 014, d/(4c) exceeds
  85017, 85018 and 85016 (T4-335; the review's exact floors are 85018, 85019 and 85017); this is an angular coefficient,
  not an L^2(R^2) distance. No reference of the campaign is shown to satisfy (5): R, R + eta and the doubly repaired
  reference have slower residual sectors (T4-335). The review's additions are CONFIRMED by T4-351 under (5)
  (audit record endpoint_closure_inequality, proof): |m| <= mu H with mu = 8/((-q*-1)(-q*-2)(-q*-3)) < 5.04423; the
  necessary budget H >= d/(4c sqrt(2 pi)) > 33917 for each of the three angular pairs; and an L^2 closure inequality
  whose right side, with the original T4-335 velocity coefficient E_q* = 133.004... of T4-335 (i) and G >= |Theta'(0)| >
  28.5227, has square root below 9.28e-11 for every admissible H and R1. That number bounds what this test can certify;
  it bounds no correction and no distance. With the current constants this route gives no L^2 exclusion at the family
  ceilings 2.8496e-6 to 4.5717e-4, and NC-T-DIST remains the binding L^2 obstruction. No verdict in this document
  depends on (i) to (iii). The converse direction is T4-359 (research/annular_moment_adjustment; AUDITED through the T2 theory worker
  the review of T4-359, handoff AT, accepted in T4-370; the T1/T3 theory worker R1-037, review set 34, is a second review, CONFIRMED in T4-373):
  with f = eta(r) sin(theta), eta >= 0 smooth and supported in 1 < r < 2, pi int r^2 eta dr = 1, the S1 density h_R = m
  R^-3 f(X/R), R >= 1, has int y h_R = m, zero velocity on r < R, exterior velocity m (cos 3theta, sin 3theta)/(pi r^3)
  on r > 2R, ||h_R||_2 = |m| R^-2 ||f||_2 and X_(s,w)(h_R) <= CX |m| R^-2, and under (5) it shifts the endpoint
  coefficient A by exactly (m/pi) P while every interior density and velocity value stays fixed. So the component of A
  along P is free at arbitrarily small L^2 and X_(s,w) cost; every compactly supported S1 correction moves A only along
  P (R1-037 remark (b), with the T2 theory worker the review of T4-281 R2), so d is invariant under compact corrections; and X_(s,w) bounds
  H_q for no q < -1 (R1-037 remark (a); remarks (a) to (c) CONFIRMED in T4-373). The complete residual change of h_R has
  L^2 norm asymptotic to |m| A_c R^-2, A_c >= (c + 1) ||f||_2 > 0, from the drift term (c X.grad - 1) h_R (T4-373, which
  REFUTES the O(R^(gamma-3)) of R1-037 remark (d); erratum 64); a lower bound at a given finite R needs background
  constants that are not certified. Given both an L^2 budget beta and a weighted amplitude budget |h| <= H (1 + |X|)^q,
  q < -3, the first moment is bounded by C beta^theta H^(1 - theta) with optimal exponent theta = dq/(2 + dq), dq = -q -
  3 (the review of T4-359 R2, CONFIRMED in T4-371; at q* the split constant is 9.4238258909662014...; T4-372 proves the sharp
  constant 9.15513474115363927... in the larger amplitude class |h| <= H r^q, attained by sign(y) min(lambda |y|, H
  r^q); AUDITED through the T1/T3 theory worker R1-039, review set 36, with artifacts/checks/check_T4372.py, 26 checks; accepted in T4-382.
  Sharpness is not claimed in the weighted C^1 class, where that extremizer has unbounded weighted gradient). The moment
  is controlled only when both budgets are given, and the present L^2 and sharpw balls give no amplitude budget for q <
  -3 on arbitrary elements (T4-359); this does not exclude an a priori bound for the stationary corrections in them,
  which is OPEN. T4-371 also CONFIRMS the minimizing endpoint moment (R3) and the interior harmonic formulas (R4), and
  leaves OPEN the step from the drift-term comparison of R3 to the complete annular residual change for every R. This is
  reference design and changes no verdict.
- (G7) Screening and the endpoint route (the T1/T3 theory worker R1-038, review set 35 with the replacement texts of review set 37; CONFIRMED
  by T4-379, research/reference_screening_audit, except one inference of (c) (iii), which it REFUTES, erratum 65;
  arithmetic artifacts/checks/check_TP6.py, 12 checks). Hypothesis (S) for references R and R' at the same c: g = R' - R
  lies in the correction class and U_(R') = U_R + U[g], with compatible distributional domains. Equal coefficients in
  the nonintegrable far-field sectors (1, 0) to (4, 0), with the remainder bounds and local smoothness of finite
  generators, give g in L^2 but do not by themselves give (S) (T4-379). (a) Under (S), S(R') = S(R) - g for the solution
  sets of corrections, so dist(R) - ||g||_2 <= dist(R') <= dist(R) + ||g||_2 in the extended reals. Rule R-SCREEN: if R'
  satisfies (S) with a registered R_j of certified distance above d_j and tau is a certified upper bound for ||R' -
  R_j||_2 with tau <= d_j - b, then R' is RULED OUT in every ball of ceiling b without a new held-out certificate; a
  FLOAT difference norm is not a bound. The graded radii d_j - 25/54684 are positive for every snapshot with a certified
  distance floor in the table of section 7 (011 has a FLOAT value only; 023 and 024 have 2.17778e-3 and 1.09889e-3), the
  smallest 7.75277e-4 (015); for the parents of the running continuations they are 1.39820e-3 (020) and 1.01318e-3
  (016). A sufficient condition for (S) (the N4 numerical auditor research/reference_difference; CONFIRMED by the T1/T3 theory worker R1-041, review set 39,
  artifacts/checks/check_N4refdiff.py, 11 checks, and by T4-393): for finite exact sums of the campaign generators at
  the same c, hypothesis (P) that for each l = 1 to 4 and each m the amplitude sums of the generators with that l, that
  m and q = 0 agree for the two references. Under (P), g and V = U[g] are smooth, S1 and O(r^(1 - 5 delta - k)) in every
  derivative of order k, and ||g||_2^2 is a finite sum of exact integrals. (P) transfers L^2 statements only. For 021
  and its parent 020, (P) holds and ||rho_021 - rho_020||_2 = 0.00734925324971972... (N4-313, CONFIRMED by T4-394)
  exceeds 1.39820e-3, so R-SCREEN decides nothing for 021, which is excluded by its own certificates (section 7). (b)
  For the three-times repaired reference R3 of 007, 013 or 014 and the fourth cutoff h4_L (the review of T4-338 R4, T4-368),
  dist(R3 + h4_L) tends to dist(R3) as L tends to infinity (and is infinite for every L if dist(R3) is), so the endpoint
  bound of T4-339 carries no L^2 information by itself. (c) If every stationary correction in the balls of a framework
  of ceiling b has H_q*(k) <= H_max with H_max >= B/sqrt(2 pi), B = d/(4c), the test of T4-351 can exclude every
  correction of norm at most b only if E sqrt(2 pi) H_max/B < Emax(b), with Emax(b) below 7.9417 (the printed graded
  target 25/54684; above 7.942167 at the exact graded ceiling, T4-443), 20.1006 (sharpw) and 19.0764 (TB-sharp); with
  the original T4-335 coefficient E_q* = 133.004... of T4-335 (i) this fails at every ceiling (the current universal
  estimate is below 1.747261, T4-411, and the separate obstruction NC-T-UNIV-E uses the improved endpoint lower bound
  H >= Phi of T4-380). A budget valid for any stationary correction is at least 999745 (T4-380); then the left side is
  at least Etest sqrt(2 pi) 999745/B >= 23.37502 for every valid constant, above all three Emax(b), so the two
  conditions are not independent: given a budget, the velocity condition fails for every valid constant (at 25/54684 it
  needs E below 0.2694533) (the T2 theory worker the T2 falsification review of the endpoint and the report summary section 4). No a priori H_q* budget for the stationary
  corrections is presently proved; that the X norm and the present balls give no H_q budget for arbitrary corrections
  does not exclude one derived from the equation (erratum 65). A stationary budget H_max < B/sqrt(2 pi) would exclude
  every stationary correction directly, without a better E (T4-379). The cap and this condition use only the moment-free
  term H (V + E G) r^(-delta)/D_delta of the error function of T4-351, so T4-371 and T4-372 (AUDITED, R1-039) cannot
  give an exclusion at b through this cap before the condition holds; they can raise a certified bound that stays below
  b (T4-379). (d) NC-T-ENDPT-Y. A contraction theorem about R3 in a norm Y >= H_q* needs a radius above every valid
  lower bound H0 of H_q* on the stationary corrections, and a Newton-Kantorovich theorem in Y with K eta <= 1/2 needs
  eta > H0/2 and, if its Lipschitz constant K is positive, K < 1/H0 (since t* <= 2 eta and t* <= 1/K); if K = 0 the
  majorant is linear, t* = eta, and eta > H0 (T4-399). T4-375 (the T4 theory auditor, research/endpoint_gradient_budget; AUDITED through
  the T2 theory worker the review of T4-375, accepted in T4-385 at its 10:19:20Z version; its revisions 1 and 2, displays and labels only, are
  accepted in T4-398 and T4-404) proves from the uniform tail limit that 4c H_q >= |u + t v| at every angle, with u = (q
  A, A'), v = (q P, P') and t the first moment over pi; T4-380 (the T4 theory auditor, research/endpoint_pointwise_budget, CONFIRMED)
  eliminates t pointwise: H_q >= |q| |A P' - A' P|/(4c (q^2 P^2 + P'^2)^(1/2)). At three rational angles this gives
  H_(gamma-4) > 999775, 999745 and 999748 for 007, 013 and 014, so H0 = 999745, radius > 999745, eta > 499872.5 and, for
  K > 0, K < 1/999745 < 1.00026e-6. (e) NC-T-UNIV-E. T4-381 (the T4 theory auditor, research/universal_velocity_lower; AUDITED through
  the T1/T3 theory worker R1-040, review set 38, artifacts/checks/check_T4381.py, 25 checks, and T4-391; second review the T2 theory worker
  the review of T4-381 and T4-384) tests T4-335 (1) with the C^1 function h = y (1 + r)^(q-1)/(-q), for which H_q(h) = 1, and proves
  that every E valid for all real centrally odd (or S1) C^1 h with finite H_q satisfies E >= Etest(q) = (-q - 1)/(2 (-q)
  (-q - 3)), which is 0.793036506422514088... at q = gamma - 4. T4-384 (AUDITED through the review of T4-381 and T4-384 and T4-396)
  keeps this bound on smooth S1 h with c[h] = 0, finite H_q and first absolute moment and ||h||_2 <= beta, for every
  beta > 0 and every R0. By T4-380 (3), reaching a radius beta by the test of T4-351 with v0 = 0 needs E below D B
  (B/(beta sqrt(-2q - 2)))^(delta/(-q - 1))/(sqrt(2 pi) H0 g0), with g0 the reference-gradient lower bound; over 007,
  013 and 014 this is below 0.785064 for the fixed sharpw radius 1351/1024000000 (at most 0.785063779293793... with the
  integer H0, T4-399) and at most 0.6819391, 0.6471910 and 0.2694314 at the sharpw, TB-sharp and graded ceilings
  (outward-rounded; the T2 theory worker handoff AU3, T4-404), all below Etest. At E = Etest the square root of the right side of the
  test is below 1.2485e-6, and below 1.421e-7 with the radial shape of the error term. So NC-T-UNIV-E holds at every
  registered radius from 3.5125e-7 up (the radial shape covers 3.5125e-7 and 21/(512 10^5); the crude cap covers
  1351/1024000000 and above), and at 2^-23 under the T4-414 hypothesis V >= |U_lead(0)| = 0.99148... (whole CI value
  below 1.14141e-7 with H >= Phi). The cap 1.421e-7 is for one constant coefficient; for the radius-dependent
  coefficients of T4-425 with the floor Etest, H >= H0 and V = 0 the whole CI value is below 1.43912e-7, and the bound
  1.14141e-7 at 2^-23 is of this second kind (the T2 theory worker the T2 falsification review of the endpoint and the report summary section 2 (c), CONFIRMED in T4-443;
  the T4 theory auditor T4-455 asks that the two stay distinguished). At the FW-A2-Db radii 2^-25 and 6.8626e-8 the T4-414 thresholds
  are at least 1.020385 and 0.8711127, above Etest, so the argument proves nothing there; an improved valid constant
  might pass this necessary test, and whether one reaches these radii is OPEN (the T2 theory worker the T2 falsification review of the endpoint and the report summary
  section 1, CONFIRMED in T4-443, which REFUTES the reading that a threshold above Etest disproves the obstruction:
  Etest is a lower bound on valid constants, not a proved admissible constant). With the T4-351 bound H >= B/sqrt(2 pi)
  alone the crude cap exceeds 100 (check_T4381.py B9), so the condition rests on T4-375. NC-T-UNIV-E bounds one
  certificate: it excludes no small distance, gives no upper H_q budget, and does not concern velocity estimates that
  use the stationary equation or a correction-specific tail expansion, which are undecided. T4-397 (the T4 theory auditor,
  research/fractional_ball_velocity_lower; AUDITED through the T1/T3 theory worker R1-042, review set 40, artifacts/checks/check_T4397.py,
  24 checks, accepted in T4-409; its finite-R numbers are FLOAT diagnostics) extends T4-384 to every fixed ball of
  X_(s,w) with c[h] = 0, an L^2 bound and any prescribed H_q, the selected sharpw ball included. An estimate sharp
  enough to evade NC-T-UNIV-E must therefore use restrictions that exclude the universal test sequence; an estimate
  restricted to stationary corrections need not fail on that test, since the universal estimate restricted to them is
  one (T4-399). T4-402 (the T4 theory auditor; CONFIRMED by the T2 theory worker the review of T4-402 with an independent exact recomputation and the Arb
  bound sqrt(max T) <= 0.5822393; accepted in T4-413, so AUDITED) gives the limit V_q[b] of r^(-q)(U[h] + DK M) when the
  rescaled tail r^(-q) h tends uniformly to a finite odd-sine polynomial b, with |V_q[b]| <= (583/1000) H_q on the
  endpoint subspaces span(A, P) of 007, 013 and 014. It is a limit as r tends to infinity with no finite-radius
  remainder, so it gives no constant for the T4-351 test. By the review of T4-402 section 4 (F2), a remainder rho(r*) for r* <=
  r_grad turns 583/1000 into an endpoint constant below the T4-380 threshold only if rho/H < 0.09893906 (sharpw ceiling,
  V = 0) or rho/H < 0.06419100 (TB ceiling), upper bounds over 007, 013 and 014; at the graded ceiling the threshold
  0.2694175 is below 583/1000. These rooms belong to the cutoff-radius form of the test and are necessary, not
  sufficient (T4-413). T4-414 (the T4 theory auditor, research/profile_velocity_shape_cap; CONFIRMED by the T2 theory worker the review of T4-414, accepted in
  T4-423, so AUDITED) applies the radial-shape identity (8) of T4-381 with the coefficient 583/1000, zero remainder and
  V = 0: the test then reaches at most 7.643e-7, below the fixed sharpw radius 1.3193359375e-6, and reaching the targets
  needs a coefficient below 0.527596 (fixed sharpw ball), 0.458292 (sharpw family ceiling), 0.434940 (TB ceiling) and
  0.181070 (graded ceiling). the review of T4-414 therefore withdraws the answer "in principle yes" for 583/1000 in
  the review of T4-402 section 4, whose (F2) room came from the crude cap (7) of T4-381 (the coordinator 12:12Z item 4). T4-415
  (the T4 theory auditor, research/pointwise_profile_velocity; CONFIRMED by the T2 theory worker the review of T4-415, accepted in T4-434, which reconstructs
  all 78336 rectangles of the review's certificate, so AUDITED) proves N(z) <= (93/250) G(z) for all real z, and hence
  the limit coefficient 93/250 on the same spans, below the first three thresholds and above the graded one; it gives no
  remainder, no finite radius and no bound on H. The constant is nearly sharp: at one rational z per candidate
  N(z)/G(z) >= 0.3714757 / 0.3714938 / 0.3715026 (Arb, the review of T4-415 section 4), so no smaller constant satisfies this
  angular inequality for all real z, and 93/250 exceeds these by at most 5.25e-4. As T4-434 notes, this bounds the
  angular inequality on the whole span only; a stationary restriction on t or a larger independent lower bound on H
  could change the comparison, and none is supplied. T4-422 (the T4 theory auditor; CONFIRMED by the T2 theory worker the review of T4-415, 114 Arb checks,
  accepted in T4-434, so AUDITED) evaluates the complete radial integral with 93/250, V = 0 and zero remainder: the caps
  are about 8.914e-6, which is 6.756, 3.128 and 2.350 times the fixed sharpw, sharpw family and TB targets and 0.0195
  times the graded one. This is a hypothetical ceiling, not a distance certificate. With the proved tail input the
  T4-410 remainder J(R)/H at R <= r_beta exceeds the room that 93/250 leaves by factors above 22.19 (fixed sharpw),
  46.06 (sharpw family) and 66.54 (TB), and the graded target leaves no room (the review of T4-415 section 7, from the bounds
  of the review of T4-410). the review of T4-415 section 7 also withdraws the pointwise step of the review of T4-414 section 4,
  third bullet, in favour of the radial average of T4-425; its conclusion is unchanged. NC-T-TWO-WEIGHT. T4-410 (the T4 theory auditor,
  research/two_weight_velocity_remainder; CONFIRMED as stated by the T1/T3 theory worker R1-043, review set 41,
  artifacts/checks/check_T4410.py, 22 checks; accepted in T4-424, so AUDITED, with outward repairs of printed digits,
  section 11 item 70) bounds the compensated error r^(-q) |U[h] + DK M_h - r^q V_q[b]| for r >= R >= L0 = 2 R0 by J(R) +
  B_b (L0/R)^(q+5), with J(R) = A R^(-epsilon) [C_a + 2^(1-a) (1 + log_+(k R^epsilon))], when h minus the cutoff model
  has amplitude weight a = q - epsilon and gradient weight q - 1. With the only proved tail bound, T4-335 (7), whose
  term H (V + E G) r^(q-delta)/D_delta forces epsilon <= delta, the bound at radius r is at least H lambda (5/r)^delta
  for r >= max(L0, 5) and at least H lambda for L0 <= r < 5, lambda = 1/2 + 5 2^(1-q) (the piecewise form of the cited
  derivation, T4-433 section 3): more than 3.16 H on [L0, 13761.58] and more than 2.74 H on [L0, 18860] (Arb). Reaching
  a target needs a radius below r_beta, and every r_beta is below 18850 (the fixed sharpw ball has the largest,
  18849.62; the review of T4-402 (F1)). So the bound exceeds 1.747261, every threshold above (at most 0.785064) and every room,
  for every profile coefficient >= 0, and also when the velocity coefficient may depend on the radius inside the T4-335
  integral (with the fixed universal fallback Eu = 1.747261 the effective coefficient is above 1.72; this is a numerical
  illustration, and the general bound for every admissible fallback is Eeff > 0.79303, item (i) below). With r_grad
  computed from the same V, E and G, J(R) > 51 Kcrit for L0 <= R <= r_grad, independently of H, E, V and t; a
  certificate need not start at R <= r_grad (only max(R, r_grad) <= r_beta is necessary, T4-421), so this factor applies
  only to such starts. The T2 theory worker the review of T4-410 derives the main obstruction independently with the sharper factor
  3.97 H at the sharpw ceiling; T4-421 CONFIRMS it with all 180 finite checks and REFUTES only its side assertion that a
  certificate must start at R <= r_grad (the T1/T3 theory worker R1-044 section 1 agrees). Two further results close the remaining forms
  of this certificate. (i) Radial averaging: T4-425 (the T4 theory auditor, research/radial_averaged_remainder_obstruction; CONFIRMED by
  the T1/T3 theory worker R1-045, review set 43, artifacts/checks/check_T4425.py, 16 checks; accepted in T4-432, so AUDITED). Integrating
  the T4-335 forcing from r to infinity, a radius-dependent coefficient E(s) enters the error bound as (H G/D)
  r^(q-delta) Eeff(r), with Eeff(r) = kappa r^kappa times the integral of E(s) s^(-kappa-1) over (r, infinity), kappa =
  4 + delta and D = c kappa. The premise is the current tail list of T4-335 (7), which contains the positive term H (V +
  E G) r^(q-delta)/D and so forces 0 < epsilon <= delta; tail-restricted or stationary-only velocity estimates are not
  in the class. Every coefficient allowed there (T4-410 estimates with any R0 and epsilon, their envelopes, and any
  norm-class universal constant, which is at least Emin = Etest = 0.79303650642...) satisfies E(s) >= min(Emin, lambda
  (5/s)^delta), lambda = 1/2 + 5 2^(1-q) = 109.60242254... > 109.6024. The average of this envelope is Emin [1 -
  delta/(kappa + delta) (r/r_u)^kappa] for r <= r_u = 302748.40..., which is above 0.79303 at r = 18860, while every
  Kcrit/Phi is below 0.785064. So the CI integrand vanishes up to r_beta for all twelve reference-target pairs, with no
  assumption R <= r_grad. By R1-045 remark R1 (derived independently in T4-432) this also holds with A_out alone, with
  Eeff > 0.79303648 at each target, provided V >= 0, G >= g0 and the input coefficient of the fixed tail list satisfies
  E >= Emin. Neither bound is a lower bound on the actual compensated velocity. (ii) Outer amplitude alone: The T1/T3 theory worker R1-044
  (review set 42, artifacts/checks/check_R1044.py; CONFIRMED by T4-426 with the repairs of section 11 item 70) proves
  J(R) >= lam1 H (V + E G) R^(-delta)/D >= lam1 E g0 H R^(-delta)/D for R >= L0 from A_out alone. So an inner multipole
  treatment that removes A_in leaves J/H above 3.756 (fixed sharpw), 4.324 (sharpw), 4.556 (TB) and 10.94 (graded) at
  R <= r_beta, and in the radius-dependent use the outer part alone exceeds every Kcrit/H by a factor above 4.34; this
  factor is without the universal fallback, whose version is the separate inequality Eeff > 0.79303648 of (i). This
  limits one sufficient certificate; it is not a lower bound on the velocity. A usable remainder needs a tail bound with
  all exponents well above delta (FLOAT, the T1/T3 theory worker's estimate in R1-044, review set 41 item 9(g): with exponents near q + 5
  the A_in part would be about 0.015 H;
  the review of T4-410 puts the threshold near 1.05, FLOAT, for its specified replacement-tail model only; it is not a
  necessary exponent for every stationary estimate, T4-442) and, for a certificate that starts at R <= r_grad, a
  velocity constant on the C^0 tail term below 23.14, where T4-410 has more than 1195. If a two-weight estimate replaced
  the bracket of T4-410 (2) by a constant Lam, the CI would need Lam below 8.647 (sharpw), 7.287 (TB) and 13.27 (fixed
  sharpw ball; 14.41 with the universal fallback) for Eprof = 93/250, with no room at the graded ceiling (R1-044 section
  3 (c), CONFIRMED by T4-426); T4-410 has Lam >= 109.6. These conditions are necessary only (Arb upper bounds computed
  with deliberately optimistic inputs; passing them is not a sufficient CI criterion, T4-426, T4-433), and a smaller
  constant alone does not remove the delta exponent, since the coefficient contains H V/D (T4-426). The T1/T3 theory worker (R1-044
  section 4), the T2 theory worker (12:10Z) and the T4 theory auditor (H16_CHECKPOINT) judge that neither way out, such a tail bound or an inner
  multipole treatment, is worth hours 16 to 22, and the coordinator accepts this (12:30Z item 2). The endpoint route is
  recorded as blocked with the present inputs; this is a statement about the proved tail input, not a nonexistence
  result. The optimal universal constant lies in [Etest, 1.747261]: T4-411 (the T4 theory auditor, research/folded_velocity_upper_audit)
  CONFIRMS the folded-kernel bound 1.749109 of the T2 theory worker the review of T4-375 R3 with its own certificate that a valid universal
  constant E < 1.747261 exists (valid constants are upward closed). No verdict changes.

### 3.5 Finite-span structure of the candidates

- (S1) Injectivity (T4-199, AUDITED by the T1/T3 theory worker R1-024 with the errata of review set 23): rho = -d_y Delta chi is injective
  on the generator class V (branches j = 0..7, any m and polynomial Q). The 007 density span has dimension 1922; the
  coefficient map has kernel of dimension exactly 1060. For the radius-scaled extensions of 016 (R0 = 25) and 017 (R0 =
  50), the exact potential rank is 2174 (N4-248, CONFIRMED by T4-321), and T4-322 (the T4 theory auditor
  audit record scaled_rank_audit, proof section 4; AUDITED through the T1/T3 theory worker R1-036, review set 33, checks in
  artifacts/checks/check_T4322.py; accepted in T4-332) extends the injectivity to both augmented spaces (density rank
  2174): a density zero forces Lap chi = K by the decay of D^4 chi (growth O(r^(3 + gamma))), so chi = A + B (x^2 -
  y^2) + K r^2/4 by Liouville and parity, and the non-integer branch exponents p_j force every coefficient to vanish.
  This concerns the representation only, not the linearized operator; any new dimension count needs its own independence
  argument, and no inverse or objective floor follows (T4-332).
- (S2) Admissible span (T4-215). The full 1922-dimensional span contains 007 itself, which is not in L^2, so an L^2
  Gram matrix of the full span is undefined (the theory_v03 R9(c) statement is REFUTED as written). The 420 tail
  constraints leave a 1502-dimensional subspace inside L^2; the strain condition gives 1501 and the five Taylor
  differentials 1496. Only on such an admissible W does the finite-span inverse obstruction of theory_v03 R9(d) hold:
  if the rows dominate a norm Y on L W with constant c_R, every inverse of L on a space containing W has
  ||L^-1||_(Y -> L^2) >= c_R/sigma_min. Zero modes must be counted as nullity >= 1060 (or zero eigenvalues of J*J).
- (S3) Taylor projection (T4-211, theorem CONFIRMED by the T1/T3 theory worker R1-028, arithmetic CONFIRMED by N4-173). Five directions
  eta_(i,j) = x^(2i) y^(2j) (1 + r^2)^(p - i - j - 2), (i, j) in {(2,1), (0,3), (3,1), (1,3), (0,4)}, remove the five
  nonconstant Taylor coefficients of F/y through degree 4 by a triangular system with diagonal 24(a - 4c + 2), -240,
  60(a - 8c + 4), -480c, -1344, preserve a0, the strain and all tail rows, and change the 007 density by less than
  3.424e-12 in L^2. This is the S1 form of the Chen-Hou Taylor-correction idea (TM-19, TM-22). The repair eta is
  nonlinear: C(ref) + DC(ref)[eta] = (0, 0, 192 alpha^2, 8640 alpha beta, 0) (T4-241). The affine lift z = eta + tau,
  tau = -(192 alpha^2/K) e_31 + (18 alpha beta/c) e_13 + ((a - 4)/112)(18 alpha beta/c) e_04, K = 60(a - 8c + 4), is the
  unique element of the span with C(ref) + DC(ref)[z] = 0 (T4-251, AUDITED through the T1/T3 theory worker R1-031, accepted in T4-269, for
  every real c != 0 with (a - 4c + 2)(a - 8c + 4) != 0). For 007, ||rho[tau]||_2 < 1.3466e-26 (N4-198, R1-031), so z is
  the exact particular step that the T4-229 normal equation needs.

## 4. Comparison with analysis2

A2 = Theorem D(b) of analysis2 (FW-A2-Db, A2-THEOREM). Best batch T theorem = FW-T-T4L2-sharpw-v1 (AUDITED
conditional). Values from sections 2.1, 2.8 and theory_v01 section 1.

| quantity | A2 (FW-A2-Db) | batch T (sharpw) | change |
|---|---|---|---|
| residual tolerance | N_s(F) <= 6.3578e-7, s = 2^-18 | X_(s,w)(F) <= 2.1035e-4, s = 1/5184 | 330.8, different norms |
| L^2 universal family ceiling | 6.8626e-8 | 2.8496e-6 | 41.5 times larger |
| L^2 radius of the stated fixed ball | 2^-25 = 2.98023e-8 | 1.3193359375e-6 | 44.2 times larger |
| base rate mu0 | 1/10 | 97/250 (sharp: 259/1000) | 3.88 (2.59) |
| commutator row-sum constant | 4800 | 397 (sharp: 401) | 12.1 times smaller |
| velocity product constant | 5 | 8/5 | 3.125 times smaller |
| forcing space | with Hdot^-1 component | no Hdot^-1 component | incomparable (T4-259) |
| far-field conditions | 7 (exponent >= -2) | 3: (2,0), (3,0), (4,0) | 3 against 7 |
| low block | H-type conditions (B1) to (B3) | signed L^2 margin (B-L2) | different, not weaker |
| other background lists | (B0), (B4), (B5), (B7), (B9c) | the same lists (:H1, :H3, :H4) | unchanged |

- What is stronger: the L^2 ceiling (41.5 times) and the far-field requirement, three conditions instead of seven: the
  Hdot^-1 component of N_s needs the eight sectors with exponent at least -2 ((1,0) to (6,0), (1,1), (2,1)) to vanish,
  L^2 needs the four with exponent at least -1 ((1,0) to (4,0); T4-328), and in both lists the sector at exponent gamma
  vanishes identically (the T2 theory worker handoff AI3). The tolerance ratio 330.8 compares different norms, and the forcing spaces
  are incomparable: X_(s,w) needs fewer far-field cancellations but slightly more fractional regularity (T4-259, AUDITED
  through the T2 theory worker the review of T4-259 and T4-283). At a common exponent u, X_u <= 2 N_u and the inclusion is strict (T4-283). On
  the residuals f in the A2 space E_3 with Q3(f) = ||omega D^3 f||_2 <= 10^6 E_2(f), X_(s,w)(f) <= 2.018851 N(f), N the
  A2 norm at 2^-18, so there N(F) <= 163.88 times the A2 tolerance implies the sharpw smallness and the converse fails:
  the enlargement on that class is about 164, not 330.8 (the T2 theory worker the review of T4-259 R2, AUDITED through T4-284, which encloses
  kappa = 2.01885036527... and the factor 163.88135945...; the T1/T3 theory worker reproduced kappa(10^6) = 2 [(2 10^12 + 16410)^(t/2) +
  34 t]/(1 - 34 s) = 2.0188503652... for t = 1/5184, s = 2^-18). The three-condition requirement is easy for the
  candidates: d2 has all eight H-route sectors EXACT-ZERO, and 007, 008 and 009 have eleven EXACT-ZERO sectors.
- What is not weaker: (B-L2) is a different low condition, theta <= c + 1 - kappa - beta_L. At beta_L = 2 this is
  theta <= 0.08215453 for 007 and theta <= 0.09710467 for 009 (rounded down). It holds for state131 (low rate >
  2.04956566, T4-019 with T4-018), d2 (N4-051 with T4-053) and 007 (margin > 0.00215453, N4-111 with T4-162). With
  kappa_HS alone it fails at beta_L = 2 for 008 and for 010 (FLOAT, INDEX); for 008 the compression bound (C2) lowers
  the requirement to a full-plane theta bound below 0.02414294, not certified as of theory_v03. The A2 coefficient lists
  are inherited unchanged.
- How much more is possible in this family: for state 131 with all other constants fixed, at most a factor of about 2
  (ceilings, not attainable improvements). No admissible improvement of the background floors raises the sharp threshold
  by more than 2.2 or the sharpw threshold by more than 1.81 (TP-5 Part D with T4-119, FLOAT eta values on certified
  caps).
- The binding comparison is not the threshold. Against the distance, the best ceiling (3.7930e-6, TB-sharp) is 1257
  times too small for 007, and the graded ceiling 4.5717e-4 is 10.43 times too small.

## 5. Hou-derived ideas: what transferred and what did not

Row statuses are those of TRANSFER_MATRIX.md; S1 instances carry their own status. Sources: Chen-Hou Part I
(arXiv 2210.07191) and Part II (2305.05660), Chen-Hou analytic finite-rank corrections (2607.15256) and
Hou-Nguyen-Wang L^2 stability (2404.09410). Full rows TM-01 to TM-25 with TeX line references are in
working file TRANSFER_MATRIX.md. (not published)

- TM-23, weighted L^2 coercivity with an explicit gap (HNW). S1 result: (B-L2) and the L^2 low block of every T4L2
  framework (T4-019). Status: AUDITED in S1 form (T4-035). This is the transfer that carried the program.
- TM-17, stationary finite-rank (Woodbury) lemma. Row status in the file: CLAIMED. Its S1 instance
  FW-T-T4L2-statL-v1[K_L] is AUDITED (T4-059); the hypothesis (L0) is OPEN for every candidate, and a finite-rank
  certificate at lambda = 0 alone does not imply it (T4-258, section 2.4).
- TM-17b, finite-rank removal of the Hilbert-Schmidt commutator. Direct substitution in the T4-019 proof does not
  transfer (T4-050: its eq. (7) uses the Gram energy); the finite-rank lemma itself stays valid and no universal
  impossibility is claimed. Status: CONDITIONAL. The AUDITED replacement is the compression bound (C2).
- TM-19 and TM-22, analytic Taylor corrections, one parameter per removed Taylor coefficient. S1 result: the T4-211
  triangular projection (S3). Row status: HEURISTIC; the S1 instance T4-211 has its theorem CONFIRMED (R1-028) and
  its arithmetic CONFIRMED (N4-173). The TM-19 cell bound for Taylor remainders is PROVED in the source and portable.
- TM-07 and TM-13, profile residual reduced by exact far-field correctors. S1 result: exact sector cancellation by
  added branches (005 to 012 have eleven EXACT-ZERO sectors). Status: TM-07 CONDITIONAL, TM-13 HEURISTIC; the sector
  identities themselves are CONFIRMED.
- TM-08, origin normalization of the scaling modes. In S1 the scaling tangent is not in the L^2 class (Lemma S) and
  the gauge is the far-field amplitude (G4, G5). Status: HEURISTIC as a transfer; the S1 facts are AUDITED or
  CONFIRMED.
- TM-01 to TM-03, TM-10, TM-14, outgoing weighted L^inf and C^(1/2) machinery with sharp constants. It runs in the
  opposite time direction from the S1 L^2 inverse, and the order-zero coupling a0 R1^2 is not small in C^(1/2).
  Status: HEURISTIC, not used.
- TM-25, bootstrap with an algebraically decaying small parameter: not applicable (S1 has no small parameter).
- All other rows (TM-04 to TM-06, TM-09, TM-11, TM-12, TM-15, TM-16, TM-18, TM-20, TM-21, TM-24): HEURISTIC.

- Main structural fact (TRANSFER_MATRIX section 0, DERIVED): in gradient variables, S1 IPM is the Chen-Hou
  (eta, xi) subsystem with slaved vorticity, U[h] = u_CH[d_x h]. The decisive difference is the order-zero coupling
  a0 R1^2 at the origin (a0 = 10.31 for 007), coercive only in L^2. This is why the L^2 route (TM-23) is the one that
  transferred and the max-norm route did not.
- Finite rank cannot move the order-zero symbol or the top-level rate (TRANSFER_MATRIX section 0 item 4); in the
  T4L2 frameworks the top block binds, so finite-rank tools act only on the low block.

## 6. Obstructions and necessary conditions

All conditions are at the fixed reference c of the candidate; by T4-189 and T4-210 (section 3.4) the exclusions that
use them hold at every c' in the same affine chart for state 131, d2 and 005 to 012. Full statements: theory_v03
section 5. "Applies to" names the frameworks a condition can exclude.

| ID | content | status | applies to |
|---|---|---|---|
| NC-T-DIST | universal L^2 family ceiling b_fam against a weak distance lower bound (D1, D2) | AUDITED | balls, boxes |
| NC-T-WDIST | the same with ||w_a h||_2 (T4-081) | AUDITED | weighted balls, DYADIC |
| NC-T-GRADED-L2 | every graded box has ||h||_(H^(2+s)) < 4.5717e-4 | AUDITED | graded boxes |
| NC-T-PT | one-point tests with symmetric constants | AUDITED | balls, boxes |
| NC-T-TAILCOST | cost of an isolated fixed far-field sector | AUDITED | exact-sector designs |
| NC-T-PACKET | energy rate <= inf lambda_min(M_(q,w)) | AUDITED conditional | H^q energies |
| NC-T-ORIGIN | contractive H^q energy needs q < c + 1 | AUDITED conditional | H^q, q >= 3 |
| NC-T-ORIGIN-specification | origin lines alpha_v, alpha_h in the spectrum (T4-145) | AUDITED | H^q semigroups |
| NC-T-ORIGIN-INV | Y inverse needs s < c - 1, M >= 1/(c - 1 - s) (T4-146) | AUDITED | DYADIC-Y |
| NC-T-E3 | no bounded Z3 stationary inverse (T4-153) | AUDITED | A2 Route U endpoint |
| NC-T-WRATE | low rate in H_a at most beta_inf(a) = 1 + c - c a | AUDITED | weighted low spaces |
| NC-T-DYADIC-R, -FLOOR, -LAP | radius ceiling, M >= 1/beta_inf(a), Laplacian test | AUDITED (cond.) | DYADIC-Y |
| NC-T-SCREEN | (S) and a certified ||R' - R_j||_2 <= d_j - b rule out R' at ceiling b (R1-038) | CONFIRMED | new refs |
| NC-T-ENDPT-Y | a framework about R3 in Y >= H_q* needs radius > 999745 (T4-375, T4-380) | AUDITED | weighted C^1 |
| NC-T-UNIV-E | no valid universal constant lets the T4-351 test reach a radius >= 3.5125e-7 | AUDITED | endpoint CI |
| NC-T-TWO-WEIGHT | T4-410 with the T4-335 (7) tail bound fails the T4-351 test below r_beta | AUDITED | endpoint CI |

Comments on what each obstruction means.

- The distance (NC-T-DIST) is the binding one. It is a property of the reference and the equation, not of the norm,
  and it is invariant under every change of norm that dominates a multiple of ||h||_2. It transfers with constant 1
  to every norm with X(h) >= ||h||_2, the localized orbit weights with inf psi = 0 included (T4-260; no upper ceiling
  on their radius is proved). It does not transfer to a norm with a decaying low weight, such as that of
  FW-T-DYADIC-Y-v1, which needs its own weighted probe (NC-T-WDIST).
- The origin conditions. No H^q energy with q >= c + 1 = 2.8103 is contractive, for any even weight (NC-T-ORIGIN).
  At q = 3 with the origin data (O1) and a0 >= 5c - 4 the origin lines satisfy alpha_h <= 0 <= alpha_v, so 0 lies in
  the closed strip of approximate point spectrum and no bounded H^3 stationary inverse exists (NC-T-ORIGIN-specification,
  NC-T-E3). In the dyadic space a bounded inverse needs s < c - 1 and costs M >= 1/(c - 1 - s) (NC-T-ORIGIN-INV).
  This is why the T4L2 frameworks work at order 2 + s with s near 0.
- The far-field cap beta_inf(a) = 1 + c - c a of NC-T-WRATE vanishes at the critical weight a = 1 + 1/c = 1.5524,
  and no positive low rate exists for a >= 1 + 1/c. For 0 < a < 1 + 1/c, T4-124 (AUDITED; it assumes
  beta_inf(a) > 0) puts the line Re z = -beta_inf(a) in the approximate point spectrum of L + K on Y for every
  bounded compact K, with weakly null test sequences, so every stationary inverse has norm at least 1/beta_inf(a),
  which tends to infinity at the critical weight. This is the S1 form of the critical far-field obstruction that
  PROMPT Route T-E asks not to ignore. A subcritical remainder space has a < 1 + 1/c, and then neither the dilation
  tangent nor the c tangent is in it (section 8).
- Screening and the endpoint (R1-038, CONFIRMED by T4-379; section 3.4 (G7)). NC-T-SCREEN carries a distance exclusion
  from a registered snapshot to a snapshot that continues it, with no new probe, when hypothesis (S) holds and the
  difference norm is certified; it is a sufficient condition only. NC-T-ENDPT-Y concerns the three-times repaired
  references of 007, 013 and 014; it bounds the radius of a framework, not a distance, and adds no exclusion (the radius
  33917 of R1-038 (d) rises to 999745 by T4-375 and T4-380). NC-T-UNIV-E limits one certificate, the T4-351 inequality
  with a universal velocity constant, at the registered radii from 3.5125e-7 up and at 2^-23 when V >= |U_lead(0)|; at
  the FW-A2-Db radii 2^-25 and 6.8626e-8 it is not proved (OPEN, section 3.4 (G7) (e)). It excludes no distance, and
  velocity estimates that use the stationary equation, a correction-specific tail expansion (T4-402, AUDITED as a limit
  only through the review of T4-402 and T4-413; the finite-radius remainder of T4-410 is AUDITED through R1-043 and T4-424 but
  too large with the T4-335 (7) tail bound: NC-T-TWO-WEIGHT, proved in R1-043 step 9 and independently in the T2 theory worker
  the review of T4-410, whose main obstruction T4-421 CONFIRMS, for the outer amplitude alone in R1-044 (CONFIRMED by
  T4-426), and for radius-dependent coefficients spliced with any universal constant in T4-425 (AUDITED: The T1/T3 theory worker R1-045,
  accepted in T4-432)) or further hypotheses that exclude the universal test sequence are not covered (T4-399).
- Floors on the inverse are not removed by finite rank. T4-124 items 2 and 3 cover compact and finite-rank repairs,
  and the T4-131 approximate-inverse version gives ||B|| >= (1 - kappa_E)/|Re z + beta_inf(a)|.

## 7. Candidates

Distances are certified lower bounds of the fixed-c L^2 distance from the reference to the solution set (NC-T-DIST);
ratios are rounded down and use the universal family ceilings rounded up, so each ratio above 1 is an exclusion (the
divisors 3.7930e-6, 2.8496e-6 and 25/54684 are upper bounds of the exact TB-sharp, sharpw and graded ceilings: The T2 theory worker
handoff BE2, CONFIRMED by the T4 theory auditor T4-454; the T2 theory worker BF3). Lower bounds do not order the actual distances (T4-219). Closure
matrix v138 (15:00Z; verdict changes since v52: 015 RULED OUT, rows 77 and 78; the dyadic scheme RULED OUT for 010, row
79; 016 RULED OUT in every ball of rows 80 and 81, v62 to v65; 017 RULED OUT in every ball of rows 82 and 83, v70; the N4 numerical auditor
accepts the 017 reproductions in N4-260 to N4-262, v72; 018 RULED OUT in row 85 and the point-tested balls of row 84,
v79, whose other row 84 labels were OPEN and are now historical, and in every ball of rows 84 and 85, v80; 019 RULED OUT
in every ball of rows 86 and 87, v84 and v85; 020 RULED OUT in every ball of rows 88 and 89, v88; 021 RULED OUT in every
ball of rows 90 and 91, v110; 022 RULED OUT in every ball of rows 92 and 93, v116; 023 RULED OUT in every ball of rows
94 and 95, v122; 024 RULED OUT in every ball of rows 96 and 97, v124; the dyadic scheme RULED OUT for 016, row 98, v126;
025 RULED OUT in every ball of rows 99 and 100, v130; 026 RULED OUT in every ball of rows 101 and 102, v132, accepted
both ways in v133; the dyadic scheme RULED OUT for 015, row 105, v135, and for 017, row 106, v138). The 016 row uses the
registered probe (19, 1800) of N4-246, CONFIRMED by T4-311 and accepted in N4-253 (the (23, 2400) value 0.001092633159,
T4-310, gives 288.0, 383.4 and 2.389). The 017 row uses the registered probe (19, 1800) of N4-257, CONFIRMED by T4-331
(the (23, 2400) value 0.001068502321, N4-256, T4-320, gives 281.7, 374.9 and 2.337).

| candidate | L^2 distance > | / TB-sharp | / sharpw | / graded | other CONFIRMED exclusions |
|---|---|---|---|---|---|
| state 131 | no exact L^2 correction at any c (N4-055, T4-049) | - | - | - | - |
| d2 | 0.29552675 (N4-065, T4-064) | 7.791e4 | 1.037e5 | 646.4 | point gap (N4-017); smallness |
| Mpen2 | 0.55006675 (N4-065, T4-064) | 1.450e5 | 1.930e5 | 1203 | see matrix |
| 002 | 1.56361352 (N4-070, T4-068; k = 0) | 4.122e5 | 5.487e5 | 3420 | point gap 465.79 (T4-037, N4-059) |
| 003 | 0.22988134 (N4-070, T4-068; k = 0) | 6.060e4 | 8.067e4 | 502.8 | point gaps (rows 40, 50; T4-055, N4-071) |
| 004 | 1.40009623 (N4-070, T4-068; k = 1024) | 3.691e5 | 4.913e5 | 3062 | point gaps (row 42; T4-038, T4-055) |
| 005 | 0.02436463 (T4-175 with w <= 1; theory_v03 5.2) | 6423 | 8550 | 53.29 | point gap (N4-076) |
| 006 | 0.52622436 (theory_v03 5.2) | 1.387e5 | 1.846e5 | 1151 | see matrix |
| 007 | 0.004769166867 (T4-185, N4-157) | 1257 | 1673 | 10.43 | graded point gap > 0.0707 (N4-102) |
| 008 | 0.0363233974 (the N3 numerics worker, N4-238; K = 2048) | 9576 | 1.274e4 | 79.45 | point gap (N4-106, T4-125) |
| 009 | 0.016967603955 (N4-179, T4-231) | 4473 | 5954 | 37.11 | point gap (N4-115, T4-144) |
| 010 | 0.022479506978 (N4-205, T4-270, N4-215) | 5926 | 7888 | 49.17 | point gap (N4-123, T4-155) |
| 012 | 0.018641021006 (N4-182, T4-236) | 4914 | 6541 | 40.77 | point gap (N4-155, T4-204) |
| 013 | 0.00199234339 (T4-255, N4-204) | 525.2 | 699.1 | 4.357 | point gaps (N4-201, T4-266) |
| 014 | 0.00198301351067 (N4-214, T4-280; design row) | 522.8 | 695.8 | 4.337 | point gaps (N4-213, T4-279) |
| 015 | 0.001232449584356253 (N4-237, T4-304; (23, 600)) | 324.9 | 432.4 | 2.695 | point gaps (N4-234, T4-299) |
| 016 | 0.001470360924 (N4-246, T4-311; held-out (19, 1800)) | 387.6 | 515.9 | 3.216 | point gaps (N4-242, T4-307) |
| 017 | 0.001671830698 (N4-257, T4-331; held-out (19, 1800)) | 440.7 | 586.6 | 3.656 | point gaps (N4-254, T4-319) |
| 018 | 0.001655825792 (N4-272, T4-345; held-out (19, 1800)) | 436.5 | 581.0 | 3.621 | point gaps (N4-270, T4-342) |
| 019 | 0.001661806967 (N4-282, T4-357; held-out (19, 1800)) | 438.1 | 583.1 | 3.634 | point gaps (N4-279, T4-353) |
| 020 | 0.001855374677 (N4-293, T4-363; held-out (19, 1800)) | 489.1 | 651.1 | 4.058 | point gaps (N4-291, T4-360) |
| 021 | 0.001864696854 (N4-316, T4-392; probe (19, 1800)) | 491.6 | 654.3 | 4.078 | point gaps (N4-314, T4-387) |
| 022 | 0.001352510757 (N4-327, T4-408; probe (19, 1800)) | 356.5 | 474.6 | 2.958 | point gaps (N4-326, T4-405) |
| 023 | 0.002634958245 (N4-338, T4-420; probe (19, 1800)) | 694.6 | 924.6 | 5.763 | point gaps (N4-337, T4-417) |
| 024 | 0.001556067368 (N4-344, T4-431; probe (19, 1800)) | 410.2 | 546.0 | 3.403 | point gaps (N4-343, T4-428) |
| 025 | 0.002065801265 (N4-364, T4-441; probe (19, 1800)) | 544.6 | 724.9 | 4.518 | point gaps (N4-362, T4-438) |
| 026 | 0.001355907204 (N4-369, T4-450; probe (19, 1800)) | 357.4 | 475.8 | 2.965 | point gaps (N4-367, T4-447) |
| 027 | none certified (registered 14:13:51Z; FLOAT values only; rows 103, 104 OPEN, v138) | - | - | - | none yet |

- 001 to 004 and b6 are RULED OUT in every specified ball by point tests or failed hypotheses (closure matrix v70). The
  002, 003 and 004 rows above use the fixed-c L^2 distances of N4-069 and N4-070 (k = 0, 0 and 1024), CONFIRMED by
  T4-068 with 84 component overlaps; they extend those exclusions to every registered scalar ball and every graded box
  with a positive top-row budget at the reference c. 001 has no certified distance: row 35 records only that its
  residual is not in the forcing space (row 41 records the same for 004 in the N_s-type frameworks), which is framework
  inapplicability, not an exclusion of exact solutions (the T4 theory auditor H18_PREPARATION, team note 233). The exclusion of exact
  solutions near 001 in the affine L^2 class is the annular application T4-458, CONFIRMED by R1-046 and the T2 theory worker's
  the review of T4-458 and accepted in T4-465 (section 0 item 1); it is not a distance and has no ratio in this table. 012 and
  011 are controlled comparisons, not certification targets; 012 has CONFIRMED structure, point value and distance
  (N4-155, T4-204, N4-167, N4-182, T4-236), 011 is OPEN with FLOAT values only. 013 (registered 04:39:56Z, pairing rows
  in the objective) is a design experiment, not a certification target. Its source, sectors and origin strain are
  CONFIRMED (N4-197). The held-out probe r (1 - t)^2 t^522 sin(21 theta) gives 0.00199234339 (T4-255, CONFIRMED by
  N4-204) and, with a cruder norm bound, 0.001123713803 (N4-200, CONFIRMED by T4-263), with the same signed pairing in
  both lanes, while the frozen mode-7 and mode-1 probes give only 5.6754744e-5 and 6.590501e-6 (T4-253, OPEN peer); with
  its point gaps (N4-201, CONFIRMED by T4-266 and N4-208) 013 is RULED OUT in every registered scalar ball and graded
  box (section 9.3 item 1). 014 (registered 05:22:50Z; 102 pairing rows in the objective, angular rows included) is a
  design experiment: structure CONFIRMED (N4-212); point gaps at (1/10, 73/100) (N4-213, CONFIRMED by T4-279: F =
  0.0907733101863..., uniform graded gap 0.0703693497775...) and the distance above 0.00198301351067 at (21, 522)
  (N4-214, CONFIRMED by T4-280), so 014 is RULED OUT in every point-tested ball and original graded box (closure matrix
  v70) and its distance exceeds every registered ceiling, the statL and bL balls included (rows 75, 76). (21, 522) is
  one of its objective rows (N4-211), so this is a valid lower bound but not a held-out measurement.
- 005. T4-175 (CONFIRMED) gives ||w h||_2 > 0.02436463 with w = (1 + r^2)^(-3/5) (T2-W4 at a = 6/5, CONFIRMED in
  T4-172 under the T4-081 hypotheses). Every S1 correction in L^2 satisfies those hypotheses and w <= 1, so
  ||h||_2 > 0.02436463 (theory_v03 5.2). The unweighted probe alone gives 0.01625064 (N4-076, T4-082), the value of
  the closure matrix L^2 row; no verdict depends on the choice.
- Every listed candidate is RULED OUT in every specified ball of its matrix rows (closure matrix v70; row 34 stays OPEN
  as a route without a high inverse; the statL and bL cells of 014 follow from T4-280); 011 (FLOAT values only) is OPEN.
  015 (rows 77 and 78) is RULED OUT; its (23, 600) distance (N4-237, T4-304, N4-245) exceeds the graded ceiling, and its
  point gaps exclude it as well (T4-299; the earlier (19, 600) value 0.000351804115950603, T4-298, was below the graded
  ceiling). 016 fails the point test in the six scalar balls and the original graded box (N4-242, CONFIRMED by T4-307),
  so row 81 and the point-tested balls of row 80 are RULED OUT (v62); its held-out distances above 0.001092633159 at
  (23, 2400) and above 0.001470360924 at (19, 1800) (N4-246, CONFIRMED by T4-310 and T4-311, accepted in N4-253) exceed
  every registered ceiling and exclude the statL and bL balls of row 80 (v65 through T4-310; the (19, 1800) confirmation
  entered v66). 017 (R0 = 50, numerics_v09 section 1b; FLOAT G0 0.3209, kappa 0.7279) has exact structure and positive
  gaps for every registered point budget (N4-254, CONFIRMED by T4-319), the sector prefix (4, 1), (9, 0), (5, 1), (1,
  2), (10, 0) (T4-323), a CONFIRMED objective-span separation of its registered probes (N4-255) and a held-out distance
  above 0.001068502321536437 at (23, 2400) (N4-256, CONFIRMED by T4-320), so rows 82 and 83 are RULED OUT in every ball
  (v70); its bound above 0.00167183069831928 at (19, 1800) (N4-257) is CONFIRMED by T4-331, and the bound above
  0.000596123050327423 at (21, 522) (N4-259, a diagnostic probe outside the preregistered set) is CONFIRMED by N4-384
  with T4-460 (1.303 times the graded ceiling; the probe stays outside the 25 registered probes). The 008 row now
  uses the N3 numerics worker certificate at K = 2048 (N4-238; 0.0040334973 at K = 512); the earlier 0.001938714194 (N4-176, T4-225)
  stays valid. C1-N1-018 (continuation of 016) is RULED OUT in every ball of rows 84 and 85 (v80): its point gaps
  (N4-270) are CONFIRMED by T4-342, its sector prefix by T4-343, its exact origin normalization by T4-346 and its probe
  separation by N4-271; its registered held-out distance above 0.001655825792 at (19, 1800) (ratios 436.5, 581.0, 3.621;
  N4-272) is CONFIRMED by T4-345, and the one above 0.001328016044 at (23, 2400) (ratios 350.1, 466.0, 2.904; N4-272) by
  T4-349 (accepted in N4-283). C1-N1-019 (017 continued by 12 steps, registered 08:28:42Z) is a trial comparison, not a
  certification target (INDEX). It is RULED OUT in every ball of rows 86 and 87 (v84, v85): its structure and point gaps
  (N4-279) are CONFIRMED by T4-353, its origin normalization by T4-354, its sector prefix by T4-355, its probe
  separation by N4-280, and its registered held-out distance above 0.001661806967 at (19, 1800) (N4-282; ratios 438.1,
  583.1 and 3.634, table row) by T4-357; the N4 numerical auditor accepts these in N4-287 to N4-290. C1-N1-020 (the 016 basis with 252
  radius-50 functions, 2426 generators, registered 08:46:18Z) has the lowest objective of the campaign (FLOAT), but its
  seven FLOAT registered values at K >= 1200 are 1.107 to 1.583 times those of 016 or 017 (numerics_v10 section 2); it
  is a trial comparison, not a certification target (INDEX). It is RULED OUT in every ball of rows 88 and 89 (v88): its
  point fields and gaps (N4-291) are CONFIRMED by T4-360, its origin normalization by T4-361, its sector prefix by
  T4-362, its actual shapes and probe separation by N4-292 and T4-364, and its registered held-out distance above
  0.001855374677442712 at (19, 1800) (N4-293; ratios 489.1, 651.1 and 4.058, table row) by T4-363; the N4 numerical auditor accepts these
  in N4-296 to N4-299. C1-N1-021 (020 with 14 held-in mid-field rows, registered 10:05:34Z) is RULED OUT in every ball
  of rows 90 and 91 (v110): its point fields and gaps, origin normalization and sector prefix (N4-314) are CONFIRMED by
  T4-387 to T4-389 (accepted in N4-319), its shapes and probe separation by N4-315 and T4-395, and its distance above
  0.001864696854799172 at the registered probe (19, 1800) (N4-316; ratios 491.6, 654.3 and 4.078, table row) by T4-392
  (accepted in N4-320). Since its held-out set was declared after launch (erratum 63), the registered probe, not a
  held-out set, carries this distance. R-SCREEN from 020 decides nothing for 021 (T4-394; section 3.4 (G7)). C1-N1-022
  (016 with 240 radius-25 functions in the angular blocks m = 16 to 23, registered 10:28:22Z) is RULED OUT in every ball
  of rows 92 and 93 (v116): its point fields and gaps, origin normalization and sector prefix (N4-326) are CONFIRMED by
  T4-405 to T4-407, its shapes and probe separation by N4-321 and T4-403 (accepted in N4-331), and its distance above
  0.00135251075726327 at the registered probe (19, 1800) (N4-327; ratios 356.5, 474.6 and 2.958, table row) by T4-408.
  As for 021, the registered probe, not a held-out set, carries this distance. R-SCREEN from 016 decides nothing for
  022: ||rho_022 - rho_016||_2 = 0.0088109875626... (N4-325, the N4 numerical auditor's own computation, replay OPEN) exceeds the graded
  radius 1.01318e-3 of 016. C1-N1-023 (registered 10:42:28Z; rows 94 and 95) is RULED OUT in every ball of these rows
  (v122): its structure, point gaps, origin normalization, prefix and distance (N4-336 to N4-339) are reproduced by
  the T4 theory auditor in T4-416 to T4-420, and the N4 numerical auditor accepts the reproductions (N4-348 to N4-350). Its distance above
  0.002634958245163687 at (19, 1800) exceeds the graded ceiling by a factor greater than 5.763. 023 is a trial
  comparison, not a certification target. C1-N1-024 (a rule control of 016: the same start, rows and steps, with the
  objective on the MID 32 radial rule; registered 11:31:32Z; rows 96 and 97) is RULED OUT in every ball of these rows
  (v124): its basis and rows, point gaps (F = 0.0952808775288636068... at (1/10, 73/100), original graded gap
  0.074870039634554045...), origin normalization, prefix and distance above 0.001556067368832641 at (19, 1800) (N4-342
  to N4-345, 3.403 times the graded ceiling) are reproduced by the T4 theory auditor in T4-427 to T4-431, and the N4 numerical auditor accepts the
  reproductions (N4-357 to N4-359). Its FLOAT held-out values have 7 of 25 above the graded budget. 024 changes both the
  radial rule and the backend (CPU to CUDA) against 016, so no one-variable comparison follows (N4-342, T4-427).
  C1-N1-025 (016 plus the scale 50 and 100 functions of blocks m = 9 to 15 and the scale 25 functions of the higher
  blocks, 2918 generators, with 14 mid-field rows at weight 1e16; snapshot 12:50:59Z; rows 99 and 100) is RULED OUT in
  every ball of these rows (v130): its structure (T4-436, N4-361, N4-365, T4-444), point gaps (six scalar gaps positive,
  uniform graded gap 0.0698812708...), origin normalization, complete prefix through -7/2 and distance above
  0.002065801265578052 at (19, 1800) (N4-362 to N4-364; ratios 544.6, 724.9 and 4.518) are reproduced by the T4 theory auditor in T4-438
  to T4-441, and the N4 numerical auditor accepts the reproductions (N4-370, N4-371). C1-N1-026 (the 022 state continued 60 steps with the
  81 rows of 025; snapshot 13:12:37Z; rows 101 and 102) is RULED OUT in every ball of these rows (v132): The N4 numerical auditor's own
  N4-366 to N4-369 give 2414 shapes with 81 objective rows and all 46 probes outside their span, F(1/10, 73/100) =
  0.0799019876430402887... with graded gap 0.0594850343605722625... and six positive scalar gaps, exact origin
  normalization, the complete sixteen-sector prefix and distance above 0.001355907204057457 at (19, 1800) (ratios 357.4,
  475.8 and 2.965), and the T4 theory auditor reproduces all of them independently in T4-446 to T4-450 (13:45Z), with the same strict
  floor (T4-450: 63 whole-plane moments at 2048 bits, no spatial truncation); the N4 numerical auditor accepts the reproductions (N4-377 to
  N4-379, v133). The dyadic rows of 025 and 026 are untested. C1-N1-027-cont60-legqs25-m16to23 (registered 14:13:51Z; a
  control for 026: the 022 state, 2414 generators, continued 60 steps with the plain 67 rows of 016; the N1/N2 numerics worker NOTES 14:13Z)
  has FLOAT values only (G0 0.2762 at MID 32; 7 of the 25 held-out probes above the graded ceiling, the largest 8.25e-4
  at (19, 1800)) and is untested (rows 103 and 104 OPEN, v138); the N1/N2 numerics worker calls it not a certification target.
- Affine classes. d2, Mpen2, 005 and 007 lie in one affine L^2 class (exact, the T2 theory worker the review of T4-234 R3), so their
  fixed-c distances refer to the same solution set; state131 + L^2 contains no exact solution at all (T4-202, and
  T4-234 with the same R3).
- Best observed candidate: 007, by its hypothesis record: G0 = ||F||_2 = 0.37668932 (N4-139; the smallest CONFIRMED G0
  is now that of 016, in [0.308886445142, 0.308886445143], N4-341, a later result), a complete theta cover with (B-L2)
  at rate > 2.00215, and exact cancellation of the three sectors required by the T4L2 frameworks. Its certified distance
  lower bound is not the smallest: the probe frozen for 007 gives 0.0019387 for 008 against 0.0047691 for 007. 008 is
  excluded by a point value and is worse than 007 in every reported FLOAT component. Lower bounds from probes tuned to
  007 do not order the actual distances.
- First failing inequality for 007 (FW-T-T4L2-sharpw-v1): :H6 smallness, X_(s,w)(F) > 756.53 against 2.1035e-4 (T4-238).
  The independent necessary condition NC-T-DIST fails by more than 1673 for the same family.
- C1-N1-016, negative norm and E2 (drafts 52 to 56). Both sides are accepted both ways: 0.616733500735 < H(016) <
  0.617952953855 and 628.580088525 < E2(016) < 628.879024750 (directed displays of the T4 theory auditor's T4-486; exact endpoints
  308366750368225240013184170643/(5 10^29), 154488238463271634620877708271/(2.5 10^29), 628580088526341/10^12 and
  314439512374259/(5 10^11) in the N4 numerical auditor's N4-418). The sharpest uppers accepted both ways, H(016) < 0.617897369 and E2(016)
  < 628.865389, are those of the prefix 63 below (N4-431, T4-502). The N4 numerical auditor's N4-416 builds the 16 dual and divergence-free
  tests of the odd modes 1 to 31 from the raw source (6925 checks; 2130 group intervals at 650 digits), the T4 theory auditor replays
  them independently and composes the complete bound in T4-486 (13380 checks), the T4 theory auditor's T4-488 accepts N4-417 and N4-418
  reciprocally (121 checks; its own upper square is smaller by less than 10^-500), and the T1/T3 theory worker's R1-052 (review set 51)
  recomposes N4-417 and N4-418 exactly from the saved endpoints; the N4 numerical auditor's N4-421 compares the two assemblies (180 checks:
  equal lower squares and selected floors, upper squares differing by less than 10^-500). They supersede, in sharpness
  only, the two-mode enclosure 0.529469576110 < H(016) < 0.619652 and 608.392385921614 < E2(016) < 629.296113 of N4-410
  (T4-480, R1-051, T4-483), which stays valid (matrix v170, row 80).
  - Lower side: H(016)^2 > sum L_n^2 >= 0.380360210930, with L_n the strict floor of |int F psi_n|/||grad psi_n||_2 for
    one test psi_n at each odd frequency n <= 31 (in modes 1 and 3 the better of two accepted trials); tests of distinct
    frequencies have orthogonal gradients (T4-466). So E2(016) > 628.580088525 > 606.820219 > E2(007) under identical
    weights. The earlier two-mode bound H(016) > 0.529469576110 (N4-396; CONFIRMED by T4-470, N4-400, N4-402 and the T1/T3 theory worker
    R1-048 with the full-precision pairing premise) already gives this E2 ordering, which holds once H(016) >
    0.522193054 (sufficient; T4-482).
  - Upper side, analytic part. The T4 theory auditor's T4-469 (H(F)^2 <= M2 + 2 t b + t^2 a for every real t, with A_F the angular
    right inverse, M2 = ||A_F||^2 and the divergence-free correction Z = A_(Delta psi) - grad psi) is AUDITED (the T2 theory worker
    the review of T4-469, the T1/T3 theory worker R1-049, T4-475, N4-404). The T4 theory auditor's prefix bound T4-474 (with S = ||rF||_2^2 and every odd mode n <
    N included, M2 <= B_N = S/N^2 + sum_(n<N) (1/n^2 - 1/N^2) S_n and 0 <= B_N - M2 <= S/N^2; an outward form with
    upper data; the scalar sum of improvements only for tests of distinct frequencies) is CONFIRMED under its hypotheses
    (F real, locally integrable, even in x, odd in y, rF in L^2) by the T2 theory worker's review of T4-474 and the T1/T3 theory worker's R1-050
    (review set 47), and the T4 theory auditor accepts both reviews in T4-481. The residual of 016 has the finitely many odd modes 1, 3,
    ..., 319, so its bounds need only the finite form of the tail step, a finite sum of nonnegative terms (the coordinator
    16:45Z item 2).
  - Upper side, numbers. N4-409 integrates the 16 modes 1, 3, ..., 31 exactly (484 group certificates) and bounds the
    other 144 modes by the outward form at N = 33: M2 <= 0.622626936301, of which the tail term costs at most 0.000525,
    and plain H(016) < 0.789068. N4-398's T4-469 improvements in modes 1 and 3 (strict floors summing to
    59664789113139289718803/(2.5 10^23) > 0.2386591564; T4-472, N4-402, R1-049) gave H(016) < 0.619652 and E2(016) <
    629.296113 (N4-410). N4-417 keeps the same prefix data and M2 upper and subtracts the floors J_n of 16
    divergence-free tests Z_n of distinct frequencies (the scalar sum of T4-469 gains that T4-474 allows), J = sum J_n >
    0.240761083124: H(016)^2 <= 0.381865853176, H(016) < 0.617952953855 and E2(016) < 628.879024750. J_1 + J_3 equals
    the N4-398 floor exactly, so the gain comes from modes 5 to 31. The four-mode assembly N4-403 (T4-476, N4-407) is
    superseded. The T1/T3 theory worker's R1-051 (review set 48; artifacts/checks/check_N4409.py, 54 checks) and R1-052 (review set 51;
    check_N4418.py, 89 checks since review set 52) recompose these values exactly from the saved endpoints; they recompute
    no mode integral or group interval and do not replace T4-480, T4-486 or T4-488.
  - Sharper upper (since draft 61). The N4 numerical auditor's N4-427 integrates the 24 modes 1, 3, ..., 47 (708 group intervals) and
    bounds the other 136 modes by the same outward form at N = 49; N4-428 combines it with the same 16 tests:
    H(016) < 617899375474255800449928932337/10^30 < 0.617899376 and E2(016) < 125773176230483/(2 10^11) < 628.865882,
    with the lower bounds unchanged. The T4 theory auditor's T4-498 (6234 checks; all 708 groups resummed at 8192 bits) CONFIRMS both.
    The T1/T3 theory worker's R1-054 (review set 54; artifacts/checks/check_N4427.py, 272 checks) recomposes both exactly from the saved
    endpoints. The N4-418 uppers above stay valid.
  - Prefix 63 (since draft 63). The N4 numerical auditor's Hardy run stopped after mode 63 (18:07Z). N4-430 integrates the 32 modes 1, 3,
    ..., 63 (920 group intervals) and bounds the other 128 modes at N = 65; N4-431 combines it with the same 16 tests:
    H(016) < 308948684181969723952067879861/(5 10^29) < 0.617897369 and E2(016) < 39304086799647/62500000000 <
    628.865389, with the lower bounds unchanged and H(007) - H(016) > 0.017627007636152. Since draft 64, the T4 theory auditor's T4-502
    (7564 checks; all 920 groups resummed at 8192 bits, 8 new mode records frozen) CONFIRMS both, and the T1/T3 theory worker's R1-054
    recomposes both exactly from the saved endpoints, so these are the sharpest uppers accepted both ways; the N4 numerical auditor's
    N4-433 (1099 checks) accepts T4-502 reciprocally. The N4-428 and N4-418 uppers stay valid. R1-054 also splits the
    width of the H^2 enclosure, about 1.44e-3, exactly: about two thirds of it (FLOAT shares 0.681 and 0.683) is the
    gap, in the modes 1 to 31, between the squared dual floors and the improved mode uppers U_n/n^2 - J_n, so further
    Hardy modes alone cannot narrow it much. The T4 theory auditor's T4-504 (473 checks) CONFIRMS this identity and R1-054; it REFUTES
    only R1-054's reading that these gaps sit in the lower bound, since each mode gap is the sum of the lower and the
    upper slack (review set 55 E15).
  - Orderings with 007. H(007) - H(016) > 0.017571422145091 and E2(016) - E2(007) > 21.759869525 (T4-486, T4-488; N4-418,
    R1-052; H(007) > 0.6355243760, N4-249 and N4-252), H(007) - H(016) > 0.017625000525836 with the N4-428 upper
    (T4-498) and H(007) - H(016) > 0.017627007636152 with the N4-431 upper (T4-502, R1-054); the earlier gaps
    0.015873038675998 and 1.572166921614 (N4-412, T4-483) stay valid. So H and E2 order 007 and 016 oppositely. Each is
    a statement about one norm of two fixed candidates at the frozen weights. Neither orders correction distances. 016
    stays RULED OUT (row 80: point gaps in the point-tested balls, CONFIRMED distances in the others). At the FLOAT
    level (numerics_v15 section 5 displays, the T1/T3 theory worker arithmetic, not bounds) 013, 017, 021, 022, 027 and 028 have E2 below
    007's 606.80, so 007 is not shown to minimize E2.
  - Where the width is. H(016)^2 lies in [0.380360210930, 0.381865853176], a width below 0.001505643 (in H below
    0.001219454). The width splits exactly into the 16 mode terms U_n/n^2 - J_n - L_n^2 and the tail term (R_U -
    Q_U)/33^2 (R1-052 V7). The modes 1 to 15 together contribute at most 1e-9 (about 2.5e-24 in each of modes 1 and 3),
    the modes 17 to 31 at most 0.000980734 and the tail term at most 0.000524909 (FLOAT shares 0.651 and 0.349). A
    sharper enclosure needs better tests in modes 17 to 31 and integrated modes beyond 31. In modes 1 and 3 the optimal
    coefficient t* = -b_n/a_n differs from 1 by about 2.0e-38 and 1.8e-36; t = 1 is valid and changes no floor (T4-482).
  - The N3 numerics worker values (CLAIMED, not imported; the N3 numerics worker notes 16:37Z and 16:47Z): H(016) in [0.6167972322, 0.6189603636] and
    E2(016) in [628.5957005, 629.1263188]. The lower ends, which use dual tests in modes 33 to 63 that no audit lane has
    replayed, lie inside the accepted enclosure (FLOAT: about 6.37e-5 above its H lower and 0.0156 above its E2 lower);
    the upper ends lie above the accepted uppers and are superseded (R1-052 V8). The N3 numerics worker's 16-mode lower 0.6167335007 is
    the N4-416 value. H(017) in [0.6144195987, 0.6165956396] and E2(017) in [605.4068697, 605.9589546]. The
    latter would put E2(017) below the CONFIRMED E2(007) range [606.8181534, 606.8202172] (N4-249, N4-252) by more
    than 0.8591. N4-413 CONFIRMS only the conditional arithmetic of these 017 totals, and the T4 theory auditor accepts it as such in
    T4-484 (E2(007) - E2(017) > 0.8591964, CONDITIONAL on C1 to C3). The source premises C1 to C3 are OPEN; the N4 numerical auditor's 017
    replay N4-425 (accepted both ways in T4-495 and N4-426; the T1/T3 theory worker R1-053, review set 53, artifacts/checks/check_N4425.py,
    79 checks) CONFIRMS H(017) > 307209799380023711068567013529/(5 10^29) > 0.614419598760 from all 16 dual trials
    (distinct frequencies 1 to 31) and the mode enclosures 0.3759840488468 < H(F_1) < 0.3759983211623 and
    0.3718015564841 < H(F_3) < 0.3718071978901 from two residual trials; R1-053 also checks the residual identity Rn^2 =
    Qn + 2n^2(b - p) + n^2(a + d) and the bounds max(0, sqrt(d) - Rn/n, |p|/sqrt(d)) <= H(F_n) <= sqrt(d) + Rn/n that
    give them (as T4-484 did). Since draft 64, the N4 numerical auditor's N4-432 (2290 checks) and the T4 theory auditor's T4-503 (4710 checks) accept the
    identity from both audit lanes and discharge the T2 theory worker's origin condition R3 for the actual 017 source: all 2174 exact
    generators are smooth, so F is odd in y and every angular projection is O(r) at the origin. The T2 theory worker's revision 1 of
    the T2 check of N4-017 (residual identity) (handoff BV) corrects its auxiliary cross bound to n sqrt(Qn (a + d)) (T4-503,
    N4-433); N4-432 REFUTES the old bound without n by the example n = 3 (cross term 64/35 against 64/105). N4-432 also
    finds all 16 mode records of the T1/T3 theory worker's extract and both residual endpoints equal to those of N4-425. This does not
    discharge C1 to C3 (14 residual trials, 158 Hardy squares and G0, G1, P2 are not reproduced), so the H(017) upper,
    E2(017) and the order E2(017) < E2(007) stay CLAIMED. 017 stays RULED OUT by its CONFIRMED distances. None of this
    gives an inverse, a correction distance or an existence statement.

## 8. Scaling, exponent and tail coordinates (design rule for Route T-E)

### 8.1 Why c and the leading far-field profile are fixed

- In the L^2 class nothing is lost by fixing c: by (G1) (T4-189, AUDITED) and the common nonzero leading profile (G2),
  every stationary solution in rho + L^2((1 + r^2)^(-a)), 0 <= a <= 1 + 1/c, has the same c. This also holds for
  state 131, d2 and 005 to 012.
- Nothing is lost by fixing the leading amplitude either. The fixed-c dilation orbit moves the four tail amplitudes of
  T_0 to T_3 together, as lambda^((j+1) delta) (G4, T4-222). Fixing the amplitude of T_0 (the leading far-field
  profile, which the prompt line 119 keeps fixed) fixes lambda, so it is a complete gauge for the dilation. The L^2
  class (a = 0) already fixes all four amplitudes, since none of T_0, ..., T_3 is in L^2 (e_j >= -1 for j <= 3).
  This costs nothing beyond the gauge: by (G6) (T4-234) and T4-235, an exact solution in the a = 0 class whose
  leading profile is p_0 Theta_0 of 007 has lower amplitudes p_j = p_0^(j+1), j = 1, 2, 3, which is the dilation
  orbit; fixing p_0 = 1 loses no solution of that class with p_0 > 0, up to dilation (R1-030 R3, accepted in T4-246
  as valid given the exact candidate profiles, which T4-235 provides, CONFIRMED by N4-189; accepted in N4-192).
- The scaling direction is not in any admissible correction space: Lambda rho is in L^2((1 + r^2)^(-a)) only for
  a > 1 + 1/c, where no positive low rate exists (NC-T-WRATE). One tangent column is not enough to represent the
  orbit modulo E_a (R1-025 R3); the finite |J_a|-dimensional augmentation of (G4) does represent it (T4-222).
- So the S1 analysis keeps c_l and the leading far-field angular profile fixed, as the prompt line 119 requires; no
  alternative normalization has been derived that is continuous in a subcritical space.

### 8.2 What an augmented (tail-coordinate) chart must contain

- Exponent changes cannot be linearized modulo E_a (G3, T4-205): the classes of T_gamma are independent, no finite
  log-Taylor correction represents an exponent change, and the exponent is uniquely determined on the union of the
  affine classes but is not continuous in the weaker space E_b (R1-025 R1). A chart with c as an unknown therefore
  needs c as a separate coordinate with the product topology on R x E_a and the nonlinear tail map
  gamma -> T_gamma into E_b of (G3). PROMPT section 16 forbids a normalization that is not continuous in the
  selected space.
- A finite augmentation at fixed c is possible: (G4) gives a |J_a|-dimensional span, with the angular profiles Theta_j
  of 007 fixed, that contains the dilation orbit modulo E_a. A free angular profile in a sector would be an
  infinite-dimensional augmentation. At a = 0 the amplitude augmentation adds no solution: by (G6) and T4-235 every
  exact solution in rho + span(T_1, T_2, T_3) + L^2 with the T_0 amplitude fixed has p_1 = p_2 = p_3 = 1, so it lies
  in rho + L^2 (the T1/T3 theory worker R1-030 R3, accepted in T4-246 and N4-192; T4-234 is AUDITED and T4-235 is CONFIRMED by
  N4-189, with an exact cross-check by the T1/T3 theory worker). The only remaining freedom at fixed c is the leading angular
  profile Theta_0 itself, which the S1 analysis fixes (the prompt line 119).
- What a T-E theorem must supply (PROMPT Route T-E), with the constraints proved here:
  1. Remainder space X: strictly subcritical, that is a weight a < 1 + 1/c with beta_inf(a) > 0 (NC-T-WRATE), and a
     high norm below the origin floors (order 2 + s with s < c - 1, NC-T-ORIGIN, NC-T-ORIGIN-INV).
  2. Normalization: continuous on R^k x X. The T_0 amplitude and the strain condition (O1) are continuous; the
     exponent read off from a tail is not (R1-025 R1).
  3. Inverse: the block operator [DF(rho_p) restricted to X, d_p F(rho_p)] from R^k x X onto a range space Y that
     contains the images of the tail columns. A Schur-complement bound needs the L^2 inverse on X (as in 2.1) and a
     certified k x k complement, and it must respect the T4-124 floor.
  4. Nonlinear estimates: Lipschitz bounds of (p, h) -> F(rho_p + h; c(p)) into Y on a ball, including the tail
     derivatives (bound (1) of T4-205 gives them in E_b).
- A minimal closure lemma for such a chart (standard contraction; elementary, stated by the T1/T3 theory worker for use in a T-E
  design). Let Z = R^k x X with a norm, z0 in Z, Phi: Z -> Y C^1 on the closed ball B(z0, r), and A: Y -> Z
  bounded and injective. If ||A Phi(z0)||_Z <= eta, ||I - A DPhi(z0)|| <= kappa and
  ||A (DPhi(z) - DPhi(z0))|| <= K ||z - z0||_Z on B(z0, r), with q = kappa + K r < 1 and eta <= (1 - q) r, then Phi
  has exactly one zero in B(z0, r). Proof: T(z) = z - A Phi(z) has ||DT(z)|| <= q on the ball, so T is a
  q-contraction there, and ||T(z) - z0|| <= q ||z - z0|| + eta <= r; Banach's theorem gives one fixed point, which is
  a zero of Phi because A is injective, and every zero in the ball is a fixed point (X must be a Banach space). In
  the PROMPT section 6 form, with K_H = ||A||_(Y -> Z) and the residual norm epsilon = ||Phi(z0)||_Y, eta <= K_H
  epsilon, and sufficient closure inequalities are kappa + K r < 1 and K_H epsilon <= (1 - kappa - K r) r.
- The distance obstruction does not move with an amplitude augmentation. Since every exact solution of the augmented
  a = 0 class has p = (1, 1, 1) (previous bullets), the L^2 bounds of section 7 apply to it unchanged: NC-T-DIST (>
  1673 for 007 against sharpw) holds in rho + span(T_1, T_2, T_3) + L^2 as well, and no minimization of the weak
  radius over the amplitudes p is needed for this chart. A T-E chart that could lift NC-T-DIST must change the leading
  profile Theta_0 or the exponent (with the product topology of the first bullet), or work in a weighted class E_a,
  a > 0, where some tails are absorbed (the E_a analog of (G6) is T4-249, AUDITED through the T2 theory worker the review of T4-249,
  T4-268: only the equations with a <= 1 + e_j are forced; with T4-256, AUDITED, no logarithmic tail adds a
  coordinate). In each case the weak radius must be recomputed for the new
  reference before a framework is written.

## 9. Unresolved inequalities, quantities to measure next, and priorities

### 9.1 Hypothesis record of 007 in the best framework (FW-T-T4L2-sharpw-v1, section 2.1)

| hypothesis | content | status for 007 | source |
|---|---|---|---|
| :H1 structure | 9/5 < c < 37/20, c + d_y u2(0) = 1 | holds (exact c and strain) | check_T4182, row 56 |
| :H1 decay (A) | far-field decay of D^j rho, j <= 2 | not checked | closure matrix row 56 |
| :H1 list | A2 (B0n) boundedness list | not checked | row 56 |
| :H2 (B-L2) | c + 1 - theta - kappa >= 2 | holds, rate > 2.00215 | N4-111, T4-162 |
| :H3 | M1 >= (9/10) I, M2 >= (1/2) I, (B4), (B5), (B7) | not checked | row 56 |
| :H4 | (B9c) component sums | not checked | row 56 |
| :H5 membership | (2,0), (3,0), (4,0) EXACT-ZERO, Q3 finite | holds (eleven sectors EXACT-ZERO) | N4-090, N4-166 (Q3) |
| :H6 smallness | X_(s,w)(F) <= 2.1035e-4 | fails: > 756.5312630768, factor > 3596535.57 | The N3 numerics worker, N4-180, T4-238 |
| NC-T-DIST (necessary) | distance below ceiling 2.8496e-6 | fails, > 0.004769166867 (> 1673 times) | T4-185, N4-157 |

So the first failing sufficient inequality is :H6, and independently the necessary condition NC-T-DIST fails. The
unchecked items :H1 (A), :H1 (B0n), :H3 and :H4 do not affect this verdict; they matter only for a candidate within both
ceilings.

### 9.2 Unresolved inequalities and open items

1. Distance (binding). For a scalar ball the certified L^2 distance lower bound of the reference must be below the
   universal family ceiling 3.7930e-6 (TB-sharp), 2.8496e-6 (sharpw) or 3.0927e-6 (sharp); for a graded box below
   4.5717e-4 together with a passing point test. No registered snapshot meets any of these (section 7). The factor for
   007 is above 1257, 1673 and 10.43 respectively; these are lower bounds for the factor, since the true distance can
   exceed every certified probe value.
2. Smallness. X_(s,w)(F) <= 2.1035e-4 (sharpw), 7.6219e-5 (sharp). For 007 the elementary bound
   (2^15 G1^2 + 2^20 G0^2)^(1/2) > 732.35 already fails it; with all complete components X_(s,w)(F) > 756.53.
3. Inverse. In the T4L2 frameworks the L^2 inverse bound 1/beta_L = 1/2 and the X_(s,w) rate are conditional on :H1 to
   :H4. For 007 only :H2, :H5 and the structural identities of :H1 (exact c and strain) are certified. No framework
   has an inverse that is unconditional for a registered candidate. A complete closure check also needs the positive
   rate beta(r) > 0 and the slope margin 7/10 - c_s r > 0 at the chosen radius (section 2.1; T4-491).
4. Route T-E (section 8.2). No such framework has been constructed or verified in this program. A chart that can lift
   NC-T-DIST must vary the leading angular profile or the exponent, or use a weighted class E_a with a > 0; the
   amplitude augmentation at a = 0 adds no solution (G6). Each of the four T-E requirements (subcritical remainder,
   continuous normalization, inverse that respects T4-124, Lipschitz bounds) is unmet.
5. Localized orbit-weight route (the T2 theory worker, section 2.7). Its admissible radius must exceed 0.004769166867 for 007 by
   norm domination with constant 1 (T4-219, T4-260); no upper ceiling on that radius is proved, and no such radius is
   certified.
6. Endpoint route (007, 013 and 014; section 3.4 (G7) (e)). With a universal velocity constant the T4-351 test needs E <
   0.785064 (fixed sharpw ball) against the proved floor Etest = 0.7930365 (NC-T-UNIV-E, AUDITED, at every registered
   radius from 3.5125e-7 up; at the FW-A2-Db radii 2^-25 and 6.8626e-8 it is OPEN whether an improved valid constant
   reaches them). With a profile-specific coefficient it needs a finite-radius remainder below the rooms of
   the review of T4-402 and T4-414; with the only proved tail bound, T4-335 (7), the remainder of T4-410 is at least lambda H
   (5/r)^delta for r >= max(L0, 5) and at least lambda H for L0 <= r < 5 (lambda > 109.6024 as in section 3.4 (G7) (e)
   (i)), so above 2.74 H on [L0, 18860] (R1-043 step 9, T4-421), at least 3.756 H from the outer amplitude alone at the
   fixed sharpw ball (R1-044, T4-426), and its radius average stays above 0.79303 while every Kcrit/Phi is below
   0.785064 (T4-425, AUDITED through R1-045 and T4-432); with 93/250 (T4-415, AUDITED through the review of T4-415 and T4-434)
   the remainder exceeds the room by factors above 22.19, 46.06 and 66.54 for the fixed sharpw, sharpw family and TB
   targets, and there is no graded room (NC-T-TWO-WEIGHT). The missing input is a tail bound for stationary corrections
   with all exponents well above delta = 1 - 1/c (in the replacement-tail model of the review of T4-410 the FLOAT
   threshold is near 1.05; that figure belongs to the model and is not a necessary exponent for every stationary
   estimate, T4-442), or a velocity or H_(gamma-4) estimate that uses stationarity. None is proved or disproved; the
   route is blocked with the present inputs.
7. FW-T-DYADIC-Y-v1 is RULED OUT at state 131, d2, 007, 008 and 009 (all seven cells fail; the minimum ratio is above
   4.64864536 for 008, N4-186 CONFIRMED by T4-248, and above 1.02032822 for 009, N4-187 CONFIRMED by T4-250, both
   accepted in N4-193), and at 010 (N4-231, minimum ratio above 5.78998556, CONFIRMED by T4-303 and N4-244; matrix row
   79; the cells cover 0 < a < 1 + 1/c and the audited nonpositive far-field rate covers 1 + 1/c <= a < 2), and at 016
   (N4-355: The N4 numerical auditor's own complete computation of the mode 1 and 3 norms J(1/4) and J(7/4), which independently verifies
   the N3 numerics worker's CLAIMED seven-cell record; minimum ratio above 1.253908386497; conditional on the hypotheses of the origin
   inverse theorem; matrix row 98, v126). At 015 the N4 numerical auditor's N4-382 (14:11Z) independently reproduces the N3 numerics worker's seven-cell
   record of 13:27Z (exact mode 1 and mode 3 projected energies, every contributing background mode retained, 2048
   bits): every cell fails, minimum ratio above 1.242922259074, CONFIRMED under the hypotheses of the FW-T-DYADIC-Y-v1
   argument; closure matrix row 105 (v135) records 015 RULED OUT in FW-T-DYADIC-Y-v1 for every 0 < a < 2, 0 < s < 1 and
   finite Rw under the audited framework hypotheses and the candidate hypotheses checked in N4-382. The T4 theory auditor's T4-461
   (14:52Z) reproduces N4-382 independently (739 checks). At 017 the N4 numerical auditor's N4-389 (14:56Z) CONFIRMS the N3 numerics worker's seven-cell
   record (CLAIMED, 14:22Z) by its own complete computation of J(1/4) and J(7/4): under the same hypotheses every cell
   of 0 < a < 1 + 1/c fails, minimum ratio above 1.221854480167 (two-evaluation cover); closure matrix row 106 (v138)
   records 017 RULED OUT in FW-T-DYADIC-Y-v1 on this basis, one sufficient scheme removed, not a profile; the T4 theory auditor's T4-463
   (15:05Z, 1070 checks at 1024 bits) CONFIRMS N4-389 independently, so row 106 is accepted both ways (v139). 011 to 014
   and 018 to 028 are not tested; no full-family L^2 result transfers to the decaying-weight dyadic ball.
8. 010 is RULED OUT in every registered scalar ball and original graded box since closure matrix v48 (distance above
   0.022479506978, N4-205, CONFIRMED by T4-270 and N4-215). 014: structure CONFIRMED (N4-212), point gaps (N4-213)
   CONFIRMED by T4-279, design-probe distance above 0.00198301351067 (N4-214) CONFIRMED by T4-280.
9. Results awaiting review: The N3 numerics worker's 016 Hardy bound of 12:15Z and its full duality bound H(016) >= 0.6167972322 (modes 1
   to 63, 16:30Z; CLAIMED pending the N4 numerical auditor, row 80; its modes 1 to 31 value 0.6167335007 is CONFIRMED by N4-416 and T4-486)
   (N4-353 and N4-360 CONFIRM the six weak probes, N4-355 the seven cells, N4-341 the whole-plane G0 and rF, N4-373 G1
   and N4-392 (15:10Z) P2, which completes the four norms G0, rF, G1 and P2; N4-393
   then CONFIRMS ten named sufficient forcing-test failures of 016 and five orderings 007 < 016 of identical-parameter
   XSW forcing norms, from conservative bounds, with no E2 or distance ordering, and T4-467 (15:18Z, 8874 checks at 2048
   bits) CONFIRMS both, with gaps above 30.172542254537 (sharp), 18.235303194523 (sharpw), 18.306105182355 (bL at 7/5),
   18.513960661750 (bL at 1) and 30.726383186740 (trans); the actual homogeneous negative norm H, for which the Hardy
   bound is a proxy, is not CONFIRMED. T4-466 (15:13Z) CONFIRMS the analytic proof that a negative-norm dual test vector
   gives H^2 >= sum p_n^2/d_n; the new 016 dual values stay OPEN until reproduced, and N4-394 (15:18Z) REFUTES the
   inference that 12-digit agreement after a basis enlargement proves the 016 dual-to-Hardy ratio is intrinsic slack; it
   remains numerical evidence); N4-396 (15:23Z, 38 checks at 4096 bits) then CONFIRMS, from the N3 numerics worker's mode 1 and mode 3
   test coefficients taken as exact rational data, H(016) > 0.5294695761 and E2(016) > 608.392385921614, above the
   accepted upper bound 606.820219 of E2(007), so E2(007) < E2(016) under identical energy weights (a difference of
   conservative bounds; the T1/T3 theory worker's analytic review R1-048, review set 46, CONFIRMS it with the full-precision pairing
   premise, which T4-470, N4-399, T4-472 and N4-402 corroborate; the ordering holds once H(016) > 0.522193054, so it rests
   on the dual bound, with a margin above 1.39 percent in H (T4-482); no distance or existence conclusion; section 7) and
   017's weak probes (five of six, the N3 numerics worker 13:49Z), G0, rF and G1 (CLAIMED pending the N4 numerical auditor), N4-356 and N4-372 (audits of
   numerics_v12 and numerics_v13: they CONFIRM the tables against their FLOAT sources and REFUTE literal summaries,
   counts, ranges and the 024 MID16 labels; no exclusion changes), N4-325 (||rho_022 - rho_016||_2; replay OPEN), the
   four the N3 numerics worker component norms behind N4-332 (CLAIMED), the step from the drift-term comparison of the review of T4-359 R3 to
   the complete annular residual change for every R (OPEN in T4-371), N4-286 (the 021 and 022 objective spans; the
   actual applications are CONFIRMED in N4-315 with T4-395 and in N4-321 with T4-403), a finite-radius bound on the
   complete remainder of the two-term endpoint expansion (OPEN in T4-368), N4-266 (complete angular-envelope comparison
   for 016 and 017, no verdict change), N4-265 (016 diagnostic at (21, 522),
   above 0.000412454461, OPEN; not needed), N4-264 (backend for snapshots mixing the scales 25 and 50; fixtures pass,
   OPEN as a backend; its application to 020, N4-293, is CONFIRMED by T4-363), T4-253 (frozen 013 probes, OPEN peer),
   N4-174, T4-188, N4-239 (015 above 0.003033479200692 at (23, 2400), OPEN), N4-247
   (R0 = 50 backend calibration, OPEN). CONFIRMED or AUDITED since draft 43: T4-458 (AUDITED through the T1/T3 theory worker R1-046 and
   the T2 theory worker the review of T4-458, accepted in T4-465; section 0 item 1), T4-462 with the T2 theory worker Proposition WU3 (CONFIRMED by R1-047
   and the review of T4-462, accepted in T4-468, and by N4-395; section 2.8), T4-469 (AUDITED: the review of T4-469, R1-049, T4-475,
   N4-404), N4-398 (T4-472, N4-402), T4-474 (CONFIRMED by the review of T4-474 and R1-050, accepted in T4-481; reciprocally
   N4-414), N4-409 and N4-410 (T4-480, R1-051, T4-483), N4-412 (T4-483), N4-416 to N4-418 (T4-486, T4-488, R1-052,
   N4-421), T4-479 (the T2 check of T4-479 (sharpw max), N4-415, T4-485), the review of T4-469 revision 2 and
   the T2 check of T4-479 (report repair) (T4-489), N4-419 (T4-490, N4-423), N4-420 (T4-492), the finite repairs of N4-422, the T2 theory worker
   handoff BS (T4-491; section 11 item 89), N4-413 (conditional arithmetic only, T4-484) and the audits T4-471 (the
   published theory_v08 with draft 52), T4-482 (draft 53), T4-487 (draft 55), T4-493 (draft 58, with R1-052) and T4-497
   (draft 60, with review set 52), T4-494 (N4-422) and T4-496 (N4-424), N4-425 (T4-495, N4-426, R1-053; R1-053 accepted in
   T4-501), N4-427 and N4-428 (T4-498, R1-054), N4-429 (the N3 numerics worker's corrected 007 ratio displays; T4-500) and N4-430 and
   N4-431 (T4-502, N4-433, R1-054), N4-432 (the 017 residual identity and origin condition; T4-503); section 7. REFUTED
   since draft 43: the exponent 7/10 of R1-049 V6 (T4-477, N4-408; 7/5 is correct), the inward decimals of R1-050 V7
   (T4-481, N4-414), the R1-051 V7 phrase "at most 0.9888" (T4-483), the literal exact optimizer t = 1 and the inward
   007 and 017 displays of draft 53 (T4-482), the unrestricted maximality of the threshold 2.1035e-4, which no draft
   claimed (T4-479, N4-415), the literal scope "every failure factor in this report uses 2.1035e-4" of draft 55 and the
   count of 33 checks for check_v50.py (T4-487), and the universal 2e-13 Taylor tolerance of the frozen NUMERICS_FINAL,
   which no draft states (N4-419, T4-490), and the 013 first-mode reduction "by two to three orders of magnitude" at k
   <= 1000 of section 9.3 item 1 (the factor is 26.8 at k = 128; N4-420), and the rounded scalar cap 3.79e-6 (T4-491, on
   the T2 final summary; section 0 item 7 printed the same figure), the R1-052 V8 phrase "within 3.6e-11" and the sentence
   "Every sharpw forcing factor quoted in this report is against the selected threshold" of drafts 56 to 59 (T4-493;
   review set 52 E13 and E14); section 11 items 83, 84 and 86 to 91. CONFIRMED or AUDITED since draft 38: T4-442 (the T4 theory auditor
   audit of draft 38, sha256 ccaa8623...: CONFIRMS its changed conditional mathematics and the 016 seven-cell
   implication, 548 checks; its six literal repairs are made here, section 11 item 74), T4-443 (CONFIRMS the
   whole-integral bound of the T2 theory worker the T2 falsification review of the endpoint and the report summary revision 1 and its displays, 948 checks; its scope
   repairs are section 11 item 73), N4-360 (the remaining three 016 weak probes) and the 025 package (T4-438 to T4-441,
   accepted in N4-370 and N4-371; T4-444 accepts N4-365; 025 RULED OUT, v130). CONFIRMED or AUDITED since draft 39:
   N4-374 (CONFIRMED by the T4 theory auditor T4-451, 318 checks: with 016's G0 and G1 alone the ten registered scalar sufficient
   forcing conditions fail, smallest ratio above 3542234; P2, the actual H and the fractional upper norms are not used;
   a failed sufficient condition, which neither orders actual norms or distances nor excludes anything; the N4 numerical auditor accepts
   T4-451 in N4-380), the 026 package (the N4 numerical auditor's N4-366 to N4-369, reproduced independently by the T4 theory auditor in T4-446 to T4-450
   and accepted in N4-377 to N4-379; 026 RULED OUT, v132 and v133), T4-456 (the T4 theory auditor audit of draft 43, sha256 a3b59ce9...:
   CONFIRMS its changed mathematics, its 23 distance-table rows and the T4-453 and T4-454 repairs, 263 checks), T4-455
   (the T4 theory auditor audit of theory_v08 preview2: CONFIRMS its changed mathematics, its 24 divisions at the printed targets and
   its factors at the exact family ceilings, 415 checks; the factor table is theory_v08 section 1, and the cap
   distinction it asks to keep is in section 3.4 (G7) (e)), T4-453 (the T4 theory auditor audit of draft 39, sha256 28f5f6ce...:
   CONFIRMS its changed conditional mathematics and its 22 numeric table rows, 237 checks; its 026 status entries were
   stale and are repaired in drafts 40 and 41, its other updates in draft 42, section 11 item 76), T4-454 (CONFIRMS the
   eight family ceiling brackets of the T2 theory worker handoff BE, among them 3.5125e-7 < TB-rebal ceiling < 3.5126e-7, 166 checks;
   section 2.5) and T4-452 (CONFIRMS the five T4-443 repairs in the T2 theory worker the T2 falsification review of the endpoint and the report summary revision 2, 107
   checks; with H_max >= 999745 the largest exact graded cutoff is 0.26945243670784104023856..., below 0.2694533).
   CONFIRMED or AUDITED since draft 37: T4-415 and T4-422 (AUDITED: the review of T4-415 accepted in T4-434), the 016
   seven-cell obstruction in FW-T-DYADIC-Y-v1 (N4-355, conditional) and the acceptance by the N4 numerical auditor of the 024 reproductions
   T4-427 to T4-431 (N4-357 to N4-359). CONFIRMED or AUDITED since draft 36: T4-433 (the T4 theory auditor audit of draft 34, sha256
   febf6c09...: CONFIRMS its changed theorem statements and its exact closure and ratio arithmetic, 79 checks; its eight
   status and wording repairs are made here, section 11 item 72; it leaves OPEN the unrestricted reading of the 1.72
   fallback figure). CONFIRMED or AUDITED since draft 35: T4-425 (AUDITED: The T1/T3 theory worker R1-045, accepted in T4-432), T4-415 and
   T4-422 (CONFIRMED by the T2 theory worker the review of T4-415) and the 024 package (N4-342 to N4-345, reproduced in T4-427 to T4-431; 024
   RULED OUT, v124). CONFIRMED or AUDITED since draft 34: T4-414 (AUDITED: The T2 theory worker the review of T4-414, accepted in T4-423),
   T4-410 (AUDITED: R1-043 accepted in T4-424, with printed repairs, section 11 item 70), the main obstruction of the T2 theory worker
   the review of T4-410 (CONFIRMED in T4-421, which REFUTES its side assertion that a certificate must start at R <=
   r_grad), T4-425 (CONFIRMED by the T1/T3 theory worker R1-045), R1-044 (CONFIRMED by T4-426 with the repairs of section 11 item 70;
   the T1/T3 theory worker accepts T4-426 in R1-045) and the 023 package (T4-416 to T4-420, accepted in N4-348 to N4-350; 023 RULED OUT,
   v122). CONFIRMED or AUDITED since draft 33: T4-402 (AUDITED: the review of T4-402 accepted in T4-413, with the caution that
   the cutoff-radius rooms of its section 4 are necessary, not sufficient), T4-410 (CONFIRMED as stated by the T1/T3 theory worker R1-043,
   review set 41), T4-411 (there exists a valid universal velocity constant below 1.747261; this CONFIRMS the
   folded-kernel bound 1.749109 of the T2 theory worker the review of T4-375 R3) and T4-412 (audit of the published theory_v07; its three
   wording repairs are made here, section 11 item 69). CONFIRMED or AUDITED since draft 32: T4-397 (AUDITED through
   the T1/T3 theory worker R1-042, accepted in T4-409), T4-402 (the limit |V_q[b]| <= (583/1000) H_q on the endpoint subspaces of 007, 013
   and 014, with no finite-radius remainder; CONFIRMED by the T2 theory worker the review of T4-402, AUDITED in T4-413), the 022 audits T4-403
   and T4-405 to T4-408 (shapes and probe separation, point fields and gaps, origin normalization, sector prefix and
   distance, reproducing N4-321, N4-326 and N4-327; T4-403 accepted in N4-331), T4-400 (the complete whole-plane 017
   cover of N4-309, every leaf replayed at 2048 bits: theta <= 2/25 and c + 1 - theta - kappa > 2.00123867; accepted in
   N4-329; section 3.1 (C3)), T4-398 and T4-404 (the T2 theory worker the review of T4-375 revisions 1 and 2 accepted; T4-375 stays AUDITED),
   T4-399 (audit of preview1 of theory_v07), T4-401 (the T2 theory worker the review of T4-381 and T4-384 revision 2 accepted), N4-322 to N4-324
   (the N4 numerical auditor accepts T4-393 to T4-395 and R1-041), N4-328 (audit of numerics_v11), N4-330 (the N3 numerics worker calibration source
   repairs; their execution OPEN) and N4-332 (the registered 016 arithmetic, conditional on the four component norms).
   REFUTED since draft 32: the manifest statement that the added 022 density support is disjoint from the modes through
   31 (mode 31 occurs; T4-403), the legacy the N3 numerics worker X3 displayed ratio as an exact-source transcription (N4-332), and the
   literal sentence of preview1 of theory_v07 that every stationary-only velocity estimate fails on the universal test
   (T4-399; no THEORY_FINAL draft contained it). CONFIRMED or AUDITED since draft 31: T4-375 (AUDITED through the T2 theory worker
   the review of T4-375, accepted in T4-385) with T4-380 (pointwise budget H_(gamma-4) > 999745; CONFIRMED), T4-381 (AUDITED
   through the T1/T3 theory worker R1-040 and T4-391; second review the T2 theory worker the review of T4-381 and T4-384), T4-384 (AUDITED through the review of T4-381 and T4-384
   and T4-396), the N4 numerical auditor reference-difference lemma (sufficient condition (P) for (S); CONFIRMED by the T1/T3 theory worker R1-041 and
   T4-393), the 021 audits T4-387 to T4-389 and T4-392 to T4-395 (accepted in N4-319 and N4-320), and N4-318 (identity
   of the actual 016 production source; the 016 norm values remain OPEN). CONFIRMED or AUDITED since draft 29: R1-038
   (the T1/T3 theory worker TP-6: R-SCREEN under (S), the extended-real distance identity under the fourth cutoff, (b2) conditional on
   (H-cut), the reach condition of the endpoint test and the radius thresholds in norms that dominate H_q*; CONFIRMED by
   T4-379 with the wording repairs of review set 37; section 3.4 (G7)), T4-372 (sharp first-moment constant
   9.15513474115363927... in the homogeneous amplitude class, AUDITED through the T1/T3 theory worker R1-039, review set 36; section 3.4),
   T4-377 (the rational Bernstein range theorem and positive denominator method of N4-285), T4-378 (N4-284, exact global
   representation of the 017 gradient), N4-308 (exact scaled Laurent multiplication on a finite calibration set;
   production 016 and 017 residual norms OPEN). REFUTED since draft 29: the inference in R1-038 (c) (iii) from the
   absence of an ambient X-to-H_q embedding to the absence of every stationary a priori budget (T4-379; erratum 65).
   CONFIRMED or AUDITED since draft 28: T4-359 (annular moment adjustment: an S1 mode-1 annular correction with
   prescribed first moment m, zero density and velocity inside r < R, L^2 and sharpw high norm O(|m| R^-2), which
   changes an endpoint residual only by (m/pi)P; AUDITED through the T2 theory worker the review of T4-359, accepted in T4-370; the T1/T3 theory worker R1-037
   is a second review; section 3.4), T4-371 (the review of T4-359 R2 to R4: the Hoelder moment bound with optimal exponent
   under an L^2 and a weighted amplitude budget, the minimizing endpoint moment, the interior harmonic formulas), T4-373
   (audit of the published theory_v06: all 51 ratios and the closure constants CONFIRMED, R1-037 remarks (a) to (c)
   CONFIRMED; the index l >= 4 and R1-037 remark (d) REFUTED, errata 61 to 64), T4-374 (audit of the NUMERICS_FINAL
   revision: the exclusions through 020 except 011 CONFIRMED, eight wording repairs), T4-376 with N4-307 (full-tensor
   angular rule: N >= 2M + 2 nodes for invariant tensor squares, N >= 2M + 3 for separate Cartesian squares through
   order 2; 180 nodes pass at M = 79), N4-302 and N4-305 (the N3 numerics worker scaled radial integrator and small-field norm
   assembly on an admissible finite test set and one synthetic six-generator fixture; no actual 016 or 017 norm is
   certified), N4-303, N4-304 and N4-306 (the N4 numerical auditor accepts T4-366, T4-367 and T4-369). REFUTED since draft 28: R1-037
   remark (d) and the scaled-block index l >= 4 of theory_v06 (T4-373; errata 61 and 64). CONFIRMED or AUDITED since
   draft 21: T4-346 (018 exact origin normalization), T4-347 (draft 21 audit, all 48 ratios; one phrase REFUTED, erratum
   60), T4-348 (N4-274, abstract mixed-scale potential and density dimension 2426), T4-349 (the 018 bound at (23,
   2400)), T4-350 (T4-335 AUDITED through the T2 theory worker the review of T4-335; section 3.4), T4-351 (R2 and R3 of that review under the
   endpoint hypotheses), N4-280 (019 objective span separation), N4-281 and N4-283 (the N4 numerical auditor accepts T4-348 and T4-349),
   T4-352 (theory_v06 draft audit; held-out has only the narrow meaning of a probe outside the declared analytic
   objective), T4-353 to T4-355 and T4-357 (019 point gaps, origin normalization, sector prefix and distance at (19,
   1800), reproducing N4-279 and N4-282; accepted in N4-287 to N4-290), T4-356 (H12 numerical report repairs partially
   accepted; band-mass lower bounds, section 10), T4-358 (draft 24 audit: the T4-335, T4-351 and T4-339 statements, all
   108 ratio comparisons and the C' requirement of section 2.8), N4-292 (020 shapes and probe separation), T4-360 to
   T4-364 (020 point fields and gaps, origin normalization, sector prefix, distance at (19, 1800) and actual shapes,
   reproducing N4-291 and N4-293), T4-365 (the T2 theory worker the review of T4-338 accepted: the third-cutoff application of T4-338 and
   T4-339 AUDITED; section 2.7), T4-366 (N4-268, Hessian energies and kappa < 0.735053672993720766 for 016 and <
   0.729080538628955349 for 017), T4-367 (N4-273, radial partition of those energies), T4-368 (the T2 theory worker the review of T4-338 R2 to
   R4: two-term endpoint expansion, positive projected inner products, a fourth cutoff with zero first moment), N4-295
   (ideal 180-node angular rule for the 020 and proposed 022 shapes), N4-296 to N4-299 (the N4 numerical auditor accepts T4-360 to T4-363),
   N4-294 with T4-369 (the proposed higher-angular radius-25 extension of N4-294 has independent potentials and
   densities of exact dimension 2414; its 240 functions beyond 016 are supported in the odd modes 31 to 47 with a
   nonzero mode-31 term; no future candidate, conditioning, inverse or existence follows). REFUTED since draft 25:
   N4-300 (the original the N3 numerics worker table calibration of the scaled legqs norms as a domain-valid integral calibration: 45 of
   810 requested moments diverge; the production accumulator is not refuted, the N3 numerics worker norms stay OPEN, and no value of
   this document uses them) and N4-301 (the original 57-panel radial partition of legqs_quadcheck.py, whose panel [0,
   1/2] overlaps the eleven lower panels; the proposed repair with first panel [0, 1/4096] is CONFIRMED as a disjoint
   partition, whose last interval of length 2^-46 is still omitted, and no bound on an actual residual error follows).
   AUDITED since draft 14: T4-322 (density injectivity and density rank 2174 in the R0 = 25 and R0 = 50 spaces; the T1/T3 theory worker
   R1-036, accepted in T4-332; section 3.5). AUDITED since draft 12: T4-314 (far-out tail repair at L^2 cost C_00
   L^(q+1); the T1/T3 theory worker R1-035, accepted in T4-325; section 2.7). CONFIRMED since draft 12: T4-336 (draft 15 audit: the T4-328
   and T4-329 repairs, all 42 ratios, the 010 status and the finite-probe caveats; erratum 57), T4-331 (017 above
   0.00167183069831928 at (19, 1800), N4-257), T4-333 (second review of T4-314, the T2 theory worker the review of T4-314), T4-334 (negative
   Sobolev and H_q costs of the cutoff and the sector agreement; section 2.7), T4-328 (the corrected sector labels
   (2,0), (3,0), (4,0); section 11 erratum 53), T4-330 (the 42 ratios of the section 7 table of draft 12), R1-035 remark
   (b) (T4-326), N4-254 (017 structure and point gaps, T4-319), N4-256 (017 at (23, 2400), T4-320), T4-323 (017 sector
   prefix), N4-248 (016 potential rank 2174 and its mode 17 density coefficient, T4-321), N4-258 (016 sector prefix,
   independently of T4-313), T4-327 (the T2 theory worker's mode-wise Mellin identity, Hardy constant 1/n and Gaussian ratio n/(n + 1),
   under the original assumptions g, r g in L^2). AUDITED since draft 11: T4-295 (exact branch-3 cancellation of the
   sector (4, 1), the T1/T3 theory worker R1-034) and T4-294 (forced integrable tail, the T2 theory worker the review of T4-294), both accepted in T4-315
   (sections 2.7 and 3.4); the T2 theory worker the review of T4-294 R2 (dipole bound and forced (9, 0) tail of R + eta) and R3 (T4-317,
   T4-318). CONFIRMED since draft 11: N4-246 at (19, 1800) (016 above 0.001470360924, T4-311, N4-253), T4-313 (016
   sector prefix), T4-316 (||eta||_2 > 4373.34), N4-252 (007 E_2 and the four N_s failures), N4-255 (017 objective-span
   separation), T4-312 (the 36 theory_v05 table ratios; its four wording repairs are in sections 9.2 and 9.3 here and go
   into the theory_v06 errata). AUDITED since draft 8: T4-242 (p = 2 weighted Hessian bound, constant (1 + sqrt 6)/2;
   the T2 theory worker the review of T4-242, accepted in T4-300), with the S1 refinements 63/32 (CONFIRMED, T4-301) and 185/96 (T4-302,
   AUDITED through the T2 theory worker the review of T4-302 and T4-309; sqrt(185/96) < 1.388195); the T2 theory worker the review of T4-281 R2 (T4-305 and the T1/T3 theory worker
   R1-034). CONFIRMED since draft 8: T4-292 (N4-240, T4-308), T4-297 (015 structure, T4-306), N4-231 (010 dyadic cells,
   T4-303, N4-244), N4-237 at (23, 600) (T4-304, N4-245), N4-238 (the N3 numerics worker's 008 certificates, above 0.0040334973 at K =
   512 and above 0.0363233974 at K = 2048), N4-242 (016 point gaps, T4-307, N4-251), N4-246 at (23, 2400) (016 held-out
   distance above 0.001092633159, T4-310), N4-243 (the 016 held-out probes lie outside the objective span; exact Fourier
   separation), N4-249 (the N3 numerics worker's whole-plane enclosure 0.6355243760 < ||F||_Hdot^-1 < 0.6355322686 for 007). REFUTED
   since draft 9: N4-250, three inferences of numerics_v08 (the span-floor inference, the signed-sum label of its bridge
   table, the density support 19 to 31); its global first-mode maximum 1.73e-4 at k = 12288 is OPEN. AUDITED since draft
   7: T4-281 (no compactly supported L^2 correction for 007, 013 and 014; the T1/T3 theory worker R1-033, review set 30, accepted in
   T4-296); section 5.2 of theory_v04 (the positive amplitude ray is the dilation orbit, T4-287, with the scope of
   T4-288). CONFIRMED since draft 7: T4-291 (T2 the review of T4-249 R3 and the review of T4-234 R3), N4-230 (the K >= 3000000
   cutoff), N4-232 (NC-T-TAILREC coefficients of 006 to 014), N4-233 (015 structure), N4-234 (015 point gaps, T4-299),
   the 015 held-out distance (T4-298). CONFIRMED since draft 5: N4-222 and N4-225 (T4-285; the first-mode test value of
   007 is at most 0.00363271755 for every K >= 3000000, below the mode-7 value; a bound on test values, not on
   distances); N4-216 (T4-282; 007 radii at six large radial indices, from 2.5912e-7 to 2.0962e-4, all below the mode-7
   value; a finite list); N4-195 (T4-275, N4-220) and N4-209 (T4-276, N4-221): the finite FLOAT weak model of
   numerics_v06 omits a nonzero far-field sector at exponent gamma - 8, and its last retained term is no error bound
   (this concerns finite asymptotic-sector Beta models, which need remainder bounds; exact full-polynomial Beta pairings
   in higher modes, such as T4-255 and N4-204, are certified); N4-207 (T4-274, N4-219); N4-213 (T4-279); N4-214
   (T4-280); N4-218. AUDITED: T4-277 (R1-032; second review the T2 theory worker the review of T4-277), T4-259 to T4-262 (the T2 theory worker the review of T4-259,
   T4-283); the conditional forcing comparison of the review of T4-259 R2 (T4-284). AUDITED or CONFIRMED since draft 3: T4-249
   (T4-268), T4-251 (the affine lift of the Taylor repair, the exact affine-feasible particular step for the T4-229
   normal equation; through the T1/T3 theory worker R1-031, accepted in T4-269, numbers CONFIRMED by N4-198), T4-256 (T4-271), T4-255
   (N4-204), N4-200 (T4-263), N4-201 (T4-266, N4-208), N4-191 (T4-267), N4-205 (T4-270, N4-215). T4-234 is AUDITED
   (R1-030, T4-246, N4-192) and T4-235 is CONFIRMED (N4-189, T4-252).

### 9.3 Quantities to measure next (ranked by expected effect on the closure ratio)

1. For every new candidate: the certified fixed-c weak distance with the frozen mode-7 (T4-185) and mode-1 (T4-182)
   probes, plus held-out probes in the odd modes 3, 5, 9 and 11. This is the cheapest decisive filter: a value above the
   budgets of 9.2 item 1 ends the evaluation for every forcing size. Lower bounds from probes tuned to 007 do not order
   the actual distances (T4-219), so a small value is evidence, not a certificate of membership. The first such
   experiment, 013 (27 first-mode pairing rows in the objective; FLOAT, not a certification target; numerics_v06 section
   4), cut the first-mode pairings at k <= 128 by factors from 26.8 (k = 128) to 9359 (k = 12; nearest roundings of
   26.8456... and 9358.8588..., N4-420, T4-492), above 126 for k <= 96 (the k <= 128 range is checked exactly from the
   saved register in N4-420), did not cut them by more than a factor 2.1 at 192 <= k <= 1024 (larger at k = 192 and
   384), and cut the held-out modes 3 to 11 at r <= 10 by one to two orders, while the rows with k >= 1536 (r >= 28)
   barely moved (maximum 1.306e-4 for 007, 1.326e-4 for 013, at k = 2048, r about 29) and the held-out probes of modes
   19 to 31 at r 23 to 32 were unchanged (best 1.12e-3, mode 21). The added objective rows reduced some pairings; the
   tested high-mode pairings remained large. This motivates additional basis functions beyond r of about 25, without
   establishing a lower bound for the minimum residual over the current span (a stalled optimization does not prove zero
   leverage; T4-273). The certified values: the frozen mode-7 and mode-1 probes give only 5.6754744e-5 and 6.590501e-6
   for 013 (T4-253, OPEN peer), the held-out probe n = 21, K = 522 gives 0.00199234339 (T4-255, CONFIRMED by N4-204;
   0.001123713803 with a cruder norm bound, N4-200, CONFIRMED by T4-263), above the graded ceiling by a factor above
   4.357. 014 put this probe and the other angular probes into its objective, and its value at (21, 522) is still above
   0.00198301351067 (N4-214, CONFIRMED by T4-280): putting the probe into the objective left this certified lower bound
   almost unchanged. The N1/N2 numerics worker (NOTES 05:37Z) runs two controlled tests, C1-N1-015 (the 102 rows on the exact quotient basis
   of 013) and C1-N1-016 (252 added functions at radial scale 25 in the blocks j = 1, 2, 3, m = 9 to 15, with held-out
   probes fixed in advance; their density support is the modes 17 to 31, mode 17 included, N4-248 CONFIRMED by T4-321
   and N4-250, not 19 to 31 as numerics_v08 says). In the 016 snapshot (numerics_v08 section 1, FLOAT) the 16 held-out
   values of its table at r 19 to 40 range from 3.26e-5 at (31, 527) to 6.50e-4 at (23, 2400); at 15 of the 16 probes
   they are lower than those of 013 and 014, by factors of about 1.8 to 5.3, and at (19, 521) they are not (1.69e-4
   against 1.60e-4 for 014 and 1.90e-4 for 013); all are above the TB-sharp and sharpw ceilings (factor above 8.5 for
   the smallest), and three, (23, 1800), (23, 2400) and (25, 2400), are above the graded ceiling. The registered probe
   (19, 1800), outside that table, moved the other way: 9.02e-4 for 016 against 7.3e-5 for 013, a factor of about 12
   (numerics_v08 section 1 last line; the N1/N2 numerics worker NOTES 06:59Z). C1-N1-017 (scale 50, FLOAT, same NOTES) gives a similar
   picture, slightly lower at r 28 to 40 and higher at r 19, and 1.03e-3 at (19, 1800) (numerics_v09 section 1b).
   The N4 numerical auditor's certified bounds are higher than these FLOAT values: it finds 016 distances above 0.001092633159 at (23,
   2400) and above 0.001470360924 at (19, 1800) (N4-246, CONFIRMED by T4-310 and T4-311), factors above 2.389 and 3.216
   over the graded ceiling, and the point gaps exclude 016 from the six scalar balls and the original graded box
   (N4-242, CONFIRMED by T4-307). For 017 it finds distances above 0.001068502321536437 at (23, 2400) (N4-256, CONFIRMED
   by T4-320) and above 0.00167183069831928 at (19, 1800) (N4-257, CONFIRMED by T4-331), factors above 2.337 and 3.656,
   and positive point gaps (N4-254, CONFIRMED by T4-319), so 017 is RULED OUT in every registered scalar ball and
   original graded box (matrix v70). Adding basis functions at radial scale 25 lowered the FLOAT pairings, but 016 is
   still excluded from the point-tested balls (T4-307). That a larger span lowers the objective does not show that the
   earlier plateau was the minimum over the earlier span (N4-250, REFUTED as a general inference; the old-space minimum
   is OPEN; the supported reading is a benefit from the tested expanded basis, T4-312), and neither lower-bound family
   shows that the actual distance decreased (the T4 theory auditor team note 131 item 4). Held-out probes test necessary conditions
   that were not explicitly included in the analytic pairing objective; reductions in either family of lower bounds do
   not establish a reduction of the actual distance (T4-312). 015 changes none of the probes at r 23 to 40 (the N1/N2 numerics worker NOTES
   06:33Z; numerics_v08 section 2). A probe whose pairing the optimizer has reduced still gives a valid necessary lower
   bound. Neither design nor held-out probes measure the actual distance; held-out probes are asked for because the
   optimizer did not target them (theory_v04 and theory_v05, R-HOLDOUT).
2. Exact structure, point gaps and a distance from a probe outside the objective for every new snapshot. 015 is settled
   (N4-233, T4-306; point gaps T4-299; held-out distances T4-298 and T4-304). 016 has CONFIRMED point gaps (T4-307) and
   a CONFIRMED objective-span separation of its 25 registered probes (N4-243); its held-out distance at (23, 2400) is
   CONFIRMED (N4-246, T4-310), so 016 is RULED OUT in every registered scalar ball and original graded box; C1-N1-017
   (scale 50, numerics_v09 section 1b) is settled as well: its structure and point gaps (N4-254, T4-319), sector prefix
   (T4-323), span separation (N4-255) and held-out distances at (23, 2400) (N4-256, T4-320) and (19, 1800) (N4-257,
   T4-331) are CONFIRMED (matrix v70), and so is N4-259 (N4-384 with T4-460; outside the 25 registered probes).
   C1-N1-018 (12 more steps of 016, registered 08:02:27Z) has
   positive point gaps (N4-270, CONFIRMED by T4-342), a CONFIRMED sector prefix (T4-343), a CONFIRMED exact origin
   normalization (T4-346) and a CONFIRMED objective-span separation (N4-271); its FLOAT held-out values are 10 to 30
   percent above those of 016 (INDEX), and its registered held-out distance above 0.001655825792 at (19, 1800) (N4-272)
   is CONFIRMED by T4-345, and the one above 0.001328016044 at (23, 2400) is CONFIRMED by T4-349. Matrix v80 (to v88)
   records 018 RULED OUT in every ball of rows 84 and 85, and v85 records 019 RULED OUT in every ball of rows 86 and 87
   (T4-353 to T4-355 and T4-357, accepted in N4-287 to N4-290), v88 records 020 RULED OUT in every ball of rows 88 and
   89 (T4-360 to T4-363, accepted in N4-296 to N4-299), v110 records 021 RULED OUT in every ball of rows 90 and 91
   (T4-387 to T4-389 and T4-392 to T4-395), v116 records 022 RULED OUT in every ball of rows 92 and 93 (T4-403 and
   T4-405 to T4-408), v122 records 023 RULED OUT in every ball of rows 94 and 95 (T4-416 to T4-420, accepted in N4-348
   to N4-350), and v124 records 024 RULED OUT in every ball of rows 96 and 97 (T4-427 to T4-431, accepted in N4-357 to
   N4-359), and v130 records 025 RULED OUT in every ball of rows 99 and 100 (T4-438 to T4-441, accepted in N4-370 and
   N4-371), and v132 records 026 RULED OUT in every ball of rows 101 and 102 (T4-446 to T4-450, reproducing N4-366 to
   N4-369), so every registered scalar ball and every original graded box with a positive top-row budget excludes, at
   the reference c, every snapshot 002 to 026 except 011 (for 002, 003 and 004 through the fixed-c L^2 distances of
   T4-068; section 0 item 1), while 001 is RULED OUT in row 35 as framework inapplicability and, since v140, by its
   exclusion in the affine L^2 class at every real c: T4-458, CONFIRMED by R1-046 and the T2 theory worker's review of T4-458 and accepted
   in T4-465 (section 0 item 1). The 010, 013 and 014 values are CONFIRMED (T4-270, N4-215; T4-255, N4-204; T4-279,
   T4-280). For a snapshot that continues a registered one (021 continues 020, 022 continues 016): a certified upper
   bound tau for ||R' - R_parent||_2 and the check of hypothesis (S) (the sector prefix gives L^2 membership; class
   membership, the canonical velocity and compatible domains are separate checks); R-SCREEN (R1-038, CONFIRMED by
   T4-379) then decides every ball of ceiling b with tau <= d_parent - b (graded radii 1.39820e-3 for 020 and 1.01318e-3
   for 016), and a FLOAT difference norm decides nothing. For 021 the sufficient condition (P) holds (N4-313), but the
   certified ||rho_021 - rho_020||_2 = 0.00734925324971972... (T4-394) exceeds 1.39820e-3, so R-SCREEN decides nothing
   and 021 is excluded by its own certificates. For 022 the difference ||rho_022 - rho_016||_2 = 0.0088109875626...
   (N4-325, the N4 numerical auditor's own computation, replay OPEN) exceeds 1.01318e-3, and 022 is likewise excluded by its own
   certificates. The held-out sets of 021 and 022 were declared at 08:33Z, after their 08:32Z launches (the coordinator 09:01Z
   and 09:27Z; T4-373); for them only the 25-probe register and the proved span separation are held-out evidence.
3. Where the 007 distance is created: the weak pairing of F per dyadic annulus and per odd angular mode (FLOAT is
   enough). 43 percent of ||F||_2^2 lies in 4 <= r < 8 (numerics_v03), and the mode-1 span gives only
   3.1474108e-4 against 0.004769166867 for mode 7, so a design objective must control the higher odd modes.
4. For every damped Gauss-Newton or Newton step h0 in the generator span: ||h0||_2 in the density L^2 metric on the
   admissible tangent (T4-229, AUDITED by T4-239), with the held-out mode-7 pairing of F + L h0. By Lemma W and R9(e)
   (T4-214) a step with ||h0||_2 < 0.0047694 must leave that pairing at least 1.7647e-5 (1 - ||h0||_2/0.0047694) in
   absolute value. Report the step with the redundant directions removed (nullity >= 1060, N4-178, T4-228).
5. The NC-T-ORIGIN-INV seven-cell test for the untested 011 to 014 and 018 to 028 (thresholds in theory_v03 section 9
   item 1; 011 has FLOAT values only). It is done, and every cell fails, for 010 (N4-231, T4-303), 015 (N4-382, T4-461),
   016 (N4-355) and 017 (N4-389, T4-463); section 9.2 item 7. The 009 margin is narrow (minimum ratio > 1.02032822,
   T4-250), so a refined candidate may pass this necessary test.
6. For a Route T-E design with a varying leading profile: a one-parameter family Theta_0 + t Theta_0', with the
   lower profiles slaved by the recurrence of (G6), and the certified weak distance of each member. This is the
   first quantity that could show whether changing the far-field class moves NC-T-DIST at all.
7. Last, and only for a candidate within both budgets: the coefficient lists (B0n), (B4), (B5), (B7) and (B9c).

### 9.4 Priorities for the next campaign

- Priority 1. Numerical refinement of the reference aimed at the fixed-c distance over all odd angular modes, measured
  by held-out exact probes (item 1) and by the per-step test of item 4. The 013 and 014 runs (item 1) motivate basis
  functions concentrated at 20 <= r <= 100 in the odd modes up to about 31, inside the admissible tangent (fixed
  tails, strain and Taylor rows), and a coordinate-invariant damped step (T4-229). The required improvement is above a
  factor 1257 for a scalar ball and above 10.43 for a graded box. No localized or weighted registered norm replaces
  this (section 2.7).
- Priority 2. Sharper matrix floors (all other constants fixed) gain at most 2.2 (sharp) or 1.81 (sharpw) in the
  threshold (T4-119), and re-tuned weights at most a factor 1.1746 over the sharpw ceiling for T2-R3 balls (beta 2) or
  1.0612 over the TB-sharp ceiling for T2-R1 TB-sharp balls with E0 as one component (beta 11/4), in the L^2 budget and
  under the hypotheses of section 2.8 (the T2 theory worker Proposition WU3, CONFIRMED in T4-462 and R1-047). They are not the lever.
- Priority 3 (speculative). A Route T-E chart in which the leading profile varies (item 6). Any new high norm must
  first pass the origin tests of section 6 (s < c - 1, q < c + 1) and the far-field window a < 1 + 1/c.
- This ranking is a planning judgment, not a theorem.

## 10. Failed approaches and counterexamples

Each item names what failed and the certificate.

- FW-T-DYADIC-Y-v1 (weaker high space with dyadic weights): RULED OUT at state 131, d2, 007, 008, 009, 010, 015 and 016
  (T4-248, T4-250, T4-303, N4-382, N4-355) for every a in its window (NC-T-DYADIC-R, NC-T-DYADIC-FLOOR, NC-T-DYADIC-LAP
  with NC-T-ORIGIN-INV; T4-127, CONFIRMED by N4-113 and reviewed in the T1/T3 theory worker R1-015; T4-146 and T4-147, AUDITED through
  the T1/T3 theory worker R1-017). For 007 at a = 1, N_1 > 13.75867597 from modes 1 and 3 alone (projected norm 13.758675979450936...,
  T4-442) against the combined ceiling 1.263642.
- High energies at the origin. An H^q energy with q >= c + 1 has no positive rate (NC-T-ORIGIN, NC-T-ORIGIN-specification),
  and the third-order endpoint E3 of A2 Route U fails for the same reason (NC-T-E3). A dyadic high inverse needs
  s < c - 1 and M >= 1/(c - 1 - s) (NC-T-ORIGIN-INV).
- Finite-rank repair of the high inverse (Chen-Hou TM-05, TM-15 to TM-17): the far-field line Re z = -beta_inf(a)
  (T4-124, T4-131) and the origin strip (NC-T-ORIGIN-specification) survive every compact and graph-compact perturbation.
  TM-17b survives only as a relaxation of (B-L2), which is not binding.
- Hou max-norm and weighted-L^infinity machinery: not used. The S1 far field is algebraic (r^gamma), so the
  Chen-Hou weights would have to be rebuilt; no transfer was attempted beyond the TRANSFER_MATRIX rows (section 5).
- A free exponent in the same chart: no stationary solution in rho + E_a, 0 <= a <= 1 + 1/c, at any c' != c (T4-189,
  AUDITED, T4-200; with T4-210, CONFIRMED). One exponent-tangent column and every finite log-Taylor correction fail to
  represent an exponent change modulo E_a (T4-205, AUDITED).
- One dilation-tangent column: not enough on 0 <= a <= 2 gamma (R1-025 R3, CONFIRMED by T4-221). The finite
  amplitude augmentation does contain the orbit (T4-222), but at a = 0 it adds no solution (G6, R1-030 R3).
- Full-span Gram matrix of the 007 generators (theory_v03 R9(c)): REFUTED, the span contains 007 itself, which is not
  in L^2 (T4-215). Use the admissible tangent (1502, 1501, 1496 dimensions).
- Defect feasibility from mu - A m - B > 0 alone: REFUTED as a sufficient condition (T4-216; counterexample
  A = m = B = 1, mu = 3, epsilon_max = -3/4). Both conditions mu - A m - B > 0 and
  epsilon <= ((mu - A m - B)^2 - 4 A B m)/(4 A) are needed.
- Closed-ball exclusion from |I| >= D b + H b^2: REFUTED as an inference (T4-217; D = 1, H = 0, I = b = m). Strict
  inequality is needed; every certified exclusion has a positive strict gap.
- Euclidean damping on redundant coordinates: changes the physical step (N4-178, T4-228; at lambda = 1 the steps
  are 1/2 and 2/3). The 1060 zero-potential directions are not absorbed by the 426 constraints (dimension
  2556 = 1496 + 1060). The N1/N2 numerics worker's 03:52Z absorption and damping statements are REFUTED. The invariant replacement is
  T4-229 (AUDITED).
- "(B-L2) fails for every current exact candidate" (the T2 theory worker M4): withdrawn; d2, state 131 and 007 satisfy it.
- A universal theta_1 budget as necessary for every weight: REFUTED (T4-169).
- Monotone isolated tail cost in the branch count: REFUTED (N4-103).
- Sharper floors, all other constants fixed: at most a factor 2.2 (sharp) or 1.81 (sharpw) (T4-119).
- Multi-scale inner functions (011): no gain in 20 steps (FLOAT, the N1/N2 numerics worker).
- Four-branch families: the full-residual L^2 floor exceeds the thresholds for every polynomial degree K <= 6886
  (sharp) and K <= 5814 (sharpw) (T4-043, CONFIRMED).
- (L0) from a finite-rank certificate at lambda = 0 alone: REFUTED as a sufficient implication (T4-258; section 2.4).
- "The X_(s,w) forcing space is larger" (drafts 1 to 4): REFUTED as an inclusion (T4-259); the forcing spaces of
  FW-A2-Db and FW-T-T4L2-sharpw-v1 are incomparable.
- Localizing a registered norm to the annulus 20 <= r <= 32 in the odd modes from 19: a 0.55 percent gain (section 2.7;
  artifacts/checks/annulus_admissible.py). Localizing only the low row of a graded box keeps the ceiling 25/54684
  (T4-277). The draft-5 family number 2.835e-6 for annular corrections is REFUTED as a family ceiling (T4-278; repaired
  to 2.839272409e-6, erratum 50, for globally H^2 corrections supported in 20 <= r <= 32 with only sine frequencies n >=
  19; erratum 62).
- numerics_v09 inferences that the held-out rows decide whether the 013 and 014 plateau was a span limit, that the
  residual mass at r 20 to 40 lies in the modes 19 to 31, and that the sweep to n = 31 was sufficient: REFUTED as
  inferences (T4-330, from the counterexamples of T4-312). A finite set of probe values gives no upper bound on the
  unmeasured residual or on the actual distance; the values remain FLOAT observations. The density support of 016 and
  017 includes mode 17 (T4-321). A damped-step residual must say whether it is F + L h or F(R + h), which differ by
  U[h].grad h.
- numerics_v10 statements (the T1/T3 theory worker ACK 08:50Z; theory_v06 R3 items 10 to 16). "Finite probes bound nothing" needs one
  qualification: a certified pairing with a probe phi supported in an angular band B gives the lower bound ||Pi_B
  F||_2 >= |<F, phi>|/||phi||_2 (T4-356, T4-358), with no upper bound on the band mass and no comparison between
  references. The 020 rise at K >= 1200 is 1.107 to 1.583 times, not 10 to 20 percent. No estimate in this program
  supports a forcing norm with a lighter weight at r 10 to 40; such a norm needs its own inverse bound and nonlinear
  constant, and none has been constructed or verified, which is not a nonexistence statement. The gaps to report are the
  certified floors over the ceilings: 3.216 to 3.656 (graded) and above 515 (sharpw) for the legqs family, and 10.43 and
  1673 for 007.
- numerics_v07 inferences that two damped Galerkin trials bracket the undamped step and establish the span floor
  0.338: REFUTED as inferences (T4-273, N4-211); a damped residual is an upper estimate of a minimum. The 014 probes
  (21, 522), (23, 523), (25, 524) are objective rows, not held out (N4-211).
- R1-029 R3 (the T1/T3 theory worker): the identification of the T4-211 repair with an affine linearized step is REFUTED (T4-241), and
  the statement that the repair is outside the 007 span is REFUTED (T4-240). Withdrawn in review set 27.

## 11. Errata to theory_v03 and to earlier the T1/T3 theory worker reviews

Frozen files are not edited; each item replaces the earlier statement. Items 1 to 27 are in theory_v03 section 12.

28. theory_v03 header read window. The end "03:43Z" was typed by hand; the last read before the copy was at 03:41Z.
29. theory_v03 R6(b) (exact L^2 Newton step). The dual formula sup |<F, phi>|/||L* phi||_2 = ||h0||_2 holds for a
    closed densely defined realization L with bounded inverse and a probe space P in D(L*) with dense image L* P
    (T4-214). Neither hypothesis is verified for the S1 transport operator.
30. theory_v03 R9(c). The full-span Gram matrix is undefined (T4-215, item in section 10); the finite-span inverse
    obstruction holds only on an admissible W with proved row domination, and zero modes are stated as
    nullity >= 1060.
31. theory_v03 statements on defect feasibility and closed-ball exclusion: replaced by the two-condition and strict
    forms of section 10 (T4-216, T4-217).
32. theory_v03 summary wording (T4-219). "007 is the closest candidate" is replaced by "007 is the best observed
    candidate"; "every 001 to 007 and refit is excluded from every registered ball" is replaced by the per-row
    statements of closure matrix v44; the dyadic exclusions then covered state 131, d2 and 007 only (008 since
    T4-248, 009 since T4-250); norm domination forces a localized radius above 0.004769166867 but does not forbid
    proving one.
33. R1-025 R3 (review set 21): the sentence that the dilation orbit can only be added as a nonlinear coordinate is
    withdrawn (review set 24 C); the orbit lies in the finite augmentation of T4-222.
34. R1-024 (review set 20): errata of review set 23 (N = num(c) = den(gamma); legq lies in V).
35. R1-029 R3 (review set 25): the eta sentence is withdrawn (review set 27, accepting T4-240 and T4-241).
36. review set 24 B2: the HEURISTIC forcing of the lower tail amplitudes is replaced by (G6) (T4-234, R1-030 R3).
37. The sharpw smallness gap "> 3.48e6" (theory_v03, from G0 and G1 alone) is superseded by > 3596535.57 with all
    complete components (T4-238); the elementary value remains a valid lower bound.
38. theory_v03 R9(e): the numerical form holds with two strict inequalities (section 3.3 (D5); T4-214).
39. theory_v03 R7(a), Lemma S: scope as in (G5) (T4-218).
40. Drafts 1 to 4, section 2.4: the sentence that (L0) reduces to a finite-rank certificate at k = 0 is REFUTED as
    a sufficient implication (T4-258); replaced by section 2.4.
41. Drafts 1 to 4, sections 0, 2.8 and 4: "the forcing space is larger" and "330.8 times larger" as an
    enlargement of one residual ball are REFUTED (T4-259); replaced by the incomparability statements there.
42. Drafts 1 to 4, section 6: "NC-T-DIST does not apply to" the localized route is REFUTED (T4-260); the necessary
    radius transfers with constant 1, and no upper ceiling is proved.
43. Drafts 1 to 4, (C2): the subtraction holds for the parity blocks complementary to S1 only (T4-261); the signed
    S1 repair is the q^2 formula of (C2).
44. "L^2 budget" in theory_v01 to theory_v03 and drafts 1 to 4 means the universal family ceiling, not the L^2
    radius of the stated fixed ball (T4-262; section 2.1 table). No exclusion changes.
45. notes/team note 27: "N4-178 CONFIRMED, T4-228 AUDITED" is replaced by "N4-178 (which REFUTES an exact
    absorption of 38 zero-potential directions), CONFIRMED by T4-228".
46. Drafts 1 to 4 (G4), review set 26 and team note 21 printed the thresholds 1 + e_j rounded up; the exact values
    are 1.5523887..., 1.1047775..., 0.6571663... and 0.2095550... (G4).
47. The T2 theory worker the review of T4-234 R3 (the common affine class of d2, Mpen2, 005 and 007, and the failure of state 131) is the T2 theory worker
    exact arithmetic, not independently re-executed (T4-254); drafts that called it AUDITED are corrected.
48. Draft 5 section 2.7 and the theory_v04 draft R2 item 6: the family ceiling 2.835e-6 for annular corrections is
    REFUTED (T4-278; it used the comparison constant at s = 1/5184, not at the maximizing s); replaced by the
    conservative uniform bound 2.839272409e-6 (erratum 50 for the rounding). The sentence "a weaker norm does not help"
    is withdrawn as a general statement; only the registered norms and the localized-low-row graded boxes (T4-277) are
    covered.
49. Drafts 1 to 5, section 0 item 2 and section 4: "three sectors instead of the eight" mixes two counts (the T2 theory worker
    handoff AI3); both lists contain the sector at exponent gamma, which vanishes identically, so the comparison is
    three conditions against seven.
50. Draft 6 (sections 2.4 and 2.7, errata 48) and theory_v04 printed upper bounds rounded down: the annular family
    ceiling 2.839272408e-6 (now 2.839272409e-6), the fixed annular ball 1.312585971e-6 (now 1.312585972e-6), and in
    the HEURISTIC part 2.168e-3 (now 2.169e-3) and the factor 12.17 (now 12.16); "1029.65" is the lower bound
    1029.647...; section 2.4 wrote X_(s,w) <= 2.01885 N, which does not follow from kappa = 2.0188503652... (now
    2.018851); "25/54684 = 4.5717e-4" is replaced by 50/(651 sqrt(28248)) < 4.5717e-4 < 25/54684. No exclusion
    changes (the T4 theory auditor team note 124 item 2).
51. Drafts 1 to 6, section 9.3 item 1 and section 9.4: "the 007 basis has no leverage" beyond r of about 25 and "a
    probe whose pairing the optimizer has reduced stops measuring the distance". A rigorously violated design probe
    still gives a valid necessary distance, neither design nor held-out probes measure the actual distance, and a
    stalled optimization does not prove zero leverage (the T4 theory auditor team note 124 item 3, T4-273). Reworded.
52. Drafts 1 to 7, section 3.4: the upper endpoints -1.133278617 and -1.790444924 of the weighted exclusions are above
    the exact values 7 gamma - 5 and 4 gamma - 4 and widened the excluded interval; replaced by the exact expressions
    (T4-293).
53. Drafts 12 to 14, sections 0, 2.1, 4 and 9.1: section 1 adopted the convention e = 1 - l delta - 2q, but the X_(s,w)
    far-field conditions kept the labels (1,0), (2,0), (3,0) of the earlier (h, k) convention (l = h + 1). The correct
    labels are (2,0), (3,0), (4,0): the old list contained the automatic sector (1,0) and omitted (4,0) (T4-328, exact
    enumeration; the T1/T3 theory worker repeated it with exact rationals). The count three against seven is unchanged, and no exclusion
    changes, since the eleven EXACT-ZERO sectors of the certified candidates contain all of them.
54. Drafts 12 to 14, section 3.4: the R2 sentence used h both for the total correction from R and for the new correction
    of R + eta. The new correction is now k, with its own hypothesis H_q2(k) < infinity, and h = eta + k; the reference
    growth bounds on U[R] and grad R of the T4-294 statement are stated explicitly (T4-329).
55. Drafts 12 to 14, sections 0 and 2.7: "holds exactly for L above about 45174" is replaced by the exact criterion L >
    (C_00/epsilon)^(1/(-q-1)) and the FLOAT estimate 45174.312 for this cutoff family (T4-329).
56. Drafts 1 to 14, section 2.6 ("Not tested at 010 to 014") and section 9.3 item 5 (the request to test 010): stale
    since T4-303 (T4-330); 010 fails every cell.
57. Drafts 12 to 16, section 2.7: "the exponent of the sector (5, 1), which both cutoffs change" is REFUTED (T4-336):
    the first cutoff changes the (5, 1) coefficient and the second preserves it, since q2 - delta and 2 q2 - 1 are below
    q3 = -1 - 5 delta. No candidate exclusion changes.
58. theory_v05 summary item 5 (last clause), section 6 items 3 and 8 and section R2 item (e): replaced by the T4-312
    forms (theory_v06 sections 1.1 to 1.4): reductions of probe lower bounds do not establish a reduction of the actual
    distance; an optimization record shows a benefit from the tested expanded basis, not a span limit; complete finite
    Beta sums are certificates, truncated sector models need a certified remainder; no framework with decaying low
    weights has been constructed or verified in this program, which is not a nonexistence statement.
59. theory_v05 section 6 item 3 and section R2: the density support of the 016 extension is the modes 17 to 31, not 19
    to 31 (N4-248, CONFIRMED by T4-321; N4-250).
60. Drafts 21 and 22, section 0 item 1: "its positive point gaps for every registered budget" (018) is REFUTED as
    overbroad (T4-347). The point audit T4-342 covers the six tested scalar balls and the original graded bound; the
    exclusion from the remaining registered balls follows from the T4-345 distance. Drafts 21 and 22 also named only
    T4-335 as a condition of T4-339; the analytic application of the third cutoff (T4-344) is the second condition.
    Since T4-350 T4-335 is AUDITED, and since T4-365 the third-cutoff application is AUDITED as well.
61. theory_v06 section 2.1, T4-362 entry: "both 252-function scaled blocks enter only at l >= 4" is REFUTED (T4-373). In
    the convention e(l, q) = 1 - l delta - 2q the blocks enter at q >= 4, with a nonzero density coefficient at (l, q) =
    (2, 4) for j = 1, m = 9. The accepted sixteen-sector prefix, which uses q <= 2, is unchanged.
62. theory_v06 section R3 item 9 and drafts 6 to 28 (section 2.7; section 10; errata 48 and 50): the bound
    2.839272409e-6 of T4-278 holds only for globally H^2 corrections supported in 20 <= r <= 32 with only sine
    frequencies n >= 19 (T4-373); the bare phrase "annular corrections" is replaced by these hypotheses. The
    unrestricted sharpw family ceiling is 2.84957773827575...e-6 (rounded up 2.8496e-6). No exclusion changes.
63. theory_v06 section 6 item 1: "The pre-registered runs C1-N1-021 ... and C1-N1-022" is qualified: their held-out sets
    were declared at 08:33Z, after the 08:32Z launches (the coordinator 09:01Z and 09:27Z; T4-373). For them only the 25-probe
    register and the proved span separation are held-out evidence. This limits provenance and weakens no certified test.
64. The T1/T3 theory worker R1-037 remark (d) (review set 34): "the L^2 change of the residual is O(R^(gamma-3))" is REFUTED (T4-373). The
    drift term |m| A_c R^-2 of estimate (3) of T4-359 is the leading term, A_c >= (c + 1) ||f||_2 > 0, and the complete
    change is asymptotic to |m| A_c R^-2. Replacement text: review set 35 Part 1 (E-R1-037(d)). Remarks (a) to (c) and the
    verdict of R1-037 stand (CONFIRMED in T4-373); theory_v06 and this report did not use remark (d).
65. The T1/T3 theory worker R1-038 (c) (iii) (review set 35): "No budget of the first kind exists" is withdrawn (the T4 theory auditor team note v177 item
    3); T4-379 REFUTES this inference. The cited facts (the X norm controls H_q for no q < -1; the present balls give no
    amplitude budget for q < -3) concern arbitrary corrections and do not exclude an a priori H_q* bound for the
    stationary corrections, which is OPEN. Replacement text: review set 37 item 3, which supersedes review set 36 Part 1. No
    number or verdict changes; draft 29 did not contain the sentence.
66. Drafts 29 and 30, section 3.4 (G7) (repairs required by T4-379; replacement texts review set 37 items 1, 2 and 4): the
    distance identity |dist(R') - dist(R)| <= ||g||_2 is replaced by the two extended-real inequalities, since infinity
    minus infinity is undefined; the parenthetical "in the far field, equal coefficients in the sectors (1, 0) to (4,
    0)" read as if a sector check gave (S), and it only gives L^2 membership; "T4-371 and T4-372 do not change the
    reach" is restricted to exclusion at the ceiling b through the fixed cap. No number or verdict changes.
67. Drafts 31 and 32, section 3.4 (G7) (d) (and any earlier draft stating NC-T-ENDPT-Y): the bound K < 1/H0 was derived
    from t* <= 1/K, which needs K > 0. For K = 0 the majorant is linear, t* = eta and eta > H0 (T4-399). The stated
    conclusions hold in both cases. No number or verdict changes.
68. Draft 33, section 3.4 (G7) (e): the sentence "A remainder built from the C^0 tail bound T4-335 (7) is of order 0.1
    to 0.3 H (an estimate, not a bound)" is withdrawn. The one explicit remainder of this type, T4-410, is at least 2.74
    H at every radius up to 18860 (R1-043 step 9). No number or verdict changes.
69. theory_v07 (repairs requested in T4-412; the same wording issues were found in N4-335): (a) section 2.1, entry
    T4-369: "the binding of the actual 022 coefficients to this family is not yet checked" should say that it is checked
    (N4-321, CONFIRMED by T4-403 and accepted in N4-331); (b) section 5.6 (e): hypothesis (P) and tau for 022 are
    the N4 numerical auditor's own computation in N4-325, whose independent replay is OPEN, while the separate direct 022 exclusion is
    audited (T4-405 to T4-408); (c) section 5.6 (d): "every registered snapshot" should read "every snapshot with a
    certified floor in the cited table" (011 has a FLOAT value only and 023 was untested at publication). Draft 33
    section 3.4 (G7) (a) had the wording of (c); it is repaired here. theory_v07 itself is not edited. No number or
    verdict changes.
70. Drafts 33 and 34, section 3.4 (G7) (e), and R1-043 step 9 (f) and its verdict (review set 41): the requirement "a
    velocity constant on the C^0 tail term below 23.14" (R1-043: "lam < 23.140") holds only for a certificate that
    starts at R <= r_grad; a certificate may start at any R with max(R, r_grad) <= r_beta (T4-421; R1-044 section 2).
    NC-T-TWO-WEIGHT does not use R <= r_grad (R1-043 steps 9 (b) to (e), T4-421, T4-425). Printed digits of R1-043
    repaired outward in T4-424: 0.785064 for 0.785063, the radii 3.16e7, 1.15e7, 4.29e7 and 8.69e7, and lam2 >= 1195.78.
    R1-044 (review set 42; errata in review set 43): its section 4 omitted the part H V/D of the delta term, which comes
    from the reference transport of the correction (E1; T4-426: a smaller velocity constant alone does not remove the
    delta exponent); its printed "Eeff >= 0.7930000" is false, the smallest value being about 0.79299998591, so >
    0.7929999 is used (E2); and the comment in check_R1044.py that calls 0.793 "the smallest admissible value" is wrong,
    since 0.793 is a relaxed value below the audited floor Emin = 0.7930365... (E3). No obstruction or verdict changes.
71. Draft 35, section 3.4 (G7) (a): "023 and 024 have no certified distance" was stale; both have certified floors (023:
    0.002634958245, T4-420; 024: 0.001556067368, T4-431), with graded radii 2.17778e-3 and 1.09889e-3, so the smallest
    graded radius is still that of 015. Draft 35 section 11 printed item 70 before item 69; the order is restored. No
    number or verdict changes.
72. Drafts 34 to 36 (repairs requested in T4-433 section 4; repairs 1 and 2, the 023 and 024 exclusions, the AUDITED
    status of T4-414, T4-410 and T4-425 and the campaign consequence CONFIRMED in T4-421, were already made in draft
    36): (3) section 3.4 (G6) said that the T4 theory auditor acceptance of R1-039 was pending; T4-382 accepts it. (4) 007 was called
    the candidate with the smallest CONFIRMED G0; since N4-341 that is 016 (a later result, not a retroactive
    error). (5) "every universal velocity constant can be taken below 1.747261" should read "there exists a valid
    universal constant below 1.747261"; valid constants are upward closed. (6) The 9.28e-11 cap and the H budget
    comparison use the original T4-335 coefficient E_q* > 133, not the current one. (7) The untested range of
    FW-T-DYADIC-Y-v1 is 011 to 024, not 011 to 020. (8) The lower bound H lambda (5/r)^delta of T4-410 holds for r >=
    max(L0, 5), with H lambda on L0 <= r < 5; the figure 1.72 is an illustration with the fallback Eu = 1.747261, not
    the general bound (Eeff > 0.79303, T4-425, T4-432); the radial-average result is stated with its tail-list premise;
    the kernel thresholds of R1-044 section 3 (c) and T4-426 are necessary conditions (Arb upper bounds with optimistic
    inputs), not a sufficient criterion. No number or verdict changes.
73. Drafts 36 to 38, sections 0, 3.4 and 6 (the T2 theory worker the T2 falsification review of the endpoint and the report summary, revision 1 of 13:19Z, sha256
    6eede464..., with handoff AZ; CONFIRMED with logical repairs in T4-443, which revision 2 of 13:42Z, 660b089b...,
    makes with no number changed): NC-T-UNIV-E said that the T4-351 test with a universal velocity constant reaches no
    registered radius. The cited argument covers the radii from 3.5125e-7 up and 2^-23 when V >= |U_lead(0)|; at the
    FW-A2-Db radii 2^-25 and 6.8626e-8 it proves nothing, and the question is OPEN for an improved valid constant (it is
    not shown false: Etest is a lower bound on valid constants, not a proved admissible one). "E_q* > 133" is written
    "E_q* = 133.004... of T4-335 (i)", the value of an upper-bound formula. The current caps 1.66122e-8 (crude) and
    1.89061e-9 (radial shape), and the whole CI bound 2.66323e-8 for the current tail list, are added. R1-038: 7.9417
    bounds the threshold at the printed target 25/54684, not at the exact graded ceiling (above 7.942167); given a
    budget H_max >= 999745 the velocity condition fails for every valid constant. Presentation: 756.5312630768 is
    printed for 756.53 where the factor 3596535.57 is derived, and section 0 item 1 cites the current matrix version. No
    exclusion changes.
74. Draft 38 (T4-442, research/theory_final_draft38_audit, team note 220): (1) section 3.4 (G7) (e) (i): lambda = 1/2 +
    5 2^(1-q) is 109.60242254..., so "= 109.6024" is replaced by "> 109.6024"; (2) section 9.2 item 6 repeated the bound
    lambda H (5/r)^delta on [L0, 18860], under the R1-044 symbol lam1, without the qualification of section 3.4 (valid
    for r >= max(L0, 5), with lambda H for L0 <= r < 5); (3) section 10: modes 1 and 3 give the projected norm
    13.758675979450936..., so the lower bound is N_1 > 13.75867597, not N_1 >= 13.758676; this concerns the lower
    inference, not the unknown full N_1; (4) section 7: the 023 distance "exceeds the graded ceiling by a factor greater
    than 5.763", not "is 5.763 times"; (5) section 3.4: the factor above 4.34 is the outer comparison without the
    universal fallback, and the fallback version is the separate inequality Eeff > 0.79303648; (6) exclusions in the
    scalar and original graded balls are listed apart from the dyadic statements (section 0 item 1), and the FLOAT
    exponent near 1.05 belongs to the replacement-tail model, not to every stationary estimate. No number used in an
    exclusion changes.
75. Drafts up to 40, section 2.5 table: the FW-T-TB-rebal-v1 L^2 ceiling was printed 3.5125e-7, while its exact value
    3.51254748112...e-7 (the T2 theory worker handoff BE3, Arb; CONFIRMED by the T4 theory auditor T4-454) lies above it, so the display rounded to
    nearest, not up; 3.5126e-7 is printed now. A factor computed against 3.5125e-7 differs by a ratio below 1.0000136
    (BE3); no exclusion in this file uses that ceiling as a divisor, and the NC-T-UNIV-E statements "from 3.5125e-7 up"
    include the exact radius. No verdict changes.
76. Drafts 39 to 41 (T4-453, the audit of draft 39): section 0 item 1 stated the R1-038 velocity condition only as
    "E below 7.9417", a weaker true necessary condition that hides the normalization; it now displays E sqrt(2 pi)
    H_max/B < Emax(b) as in section 3.4 (G7) (c). Its summary of T4-425 now names the four targets of T4-425 and leaves
    an improved valid constant at the FW-A2-Db radii OPEN (T4-443). Section 9.2 item 9 named only G0 and G1 as the
    CONFIRMED 016 components; rF is CONFIRMED too (N4-341), and the actual homogeneous negative norm H is not. Section 0
    item 1 said "every registered scalar and graded ball" once; it now reads "every registered scalar ball and original
    graded box", as elsewhere. No number or verdict changes.
77. Drafts up to 45, sections 0 item 1 and 7 (own H18 check, artifacts/checks/h18_verdicts.py, and the T4 theory auditor
    H18_PREPARATION step 7): "every snapshot C1-N1-001 to C1-N1-026 except 011 is RULED OUT in every registered
    scalar ball and original graded box" overstated two cases. Matrix row 35 excludes 001 only because its residual
    is not in the forcing space, which is framework inapplicability, not an exclusion of exact solutions; and rows
    36, 40 and 42 exclude 002, 003 and 004 only in specified balls. The statement now covers 002 to 026 except 011
    at the reference c, with 002 to 004 carried to every scalar ball and every graded box with a positive top-row
    budget by the CONFIRMED fixed-c L^2 distances of T4-068 (new section 7 rows), and states 001 separately. Every
    matrix verdict cited elsewhere in this file agrees with v135 (154 claims, 0 failures).
78. Drafts up to 45, sections 0 item 8, 2.8, 3.5, 9.4 and 10 (the T2 theory worker H18 result, handoff BH1 and BH4): the T4-119 factors
    2.2 and 1.81 were stated as the limit of "sharper constants" in general. T4-119 bounds only the state 131 matrix
    floors with every other constant fixed, and its values are ceilings, not attainable improvements; changing the
    constants themselves gave factors above 330 and 76 (handoff BH1). The lines now carry that scope, and the weight
    question cites the T2 theory worker's Proposition WU (CLAIMED, factor at most 2.376 in the T2-R3 L^2 budget). No number changes.
    Draft 47 replaces WU by the sharper Proposition WU3 (handoff BJ2; 1.1746 and 1.0612), CONFIRMED at draft 48 by the T4 theory auditor
    T4-462 and, for its exact weight elimination, by the T1/T3 theory worker R1-047; the T2 theory worker the review of T4-462 (handoff BM) and the N4 numerical auditor N4-395
    also CONFIRM it (draft 50).
79. artifacts/checks/check_T4462.py (review R1-047, sha256 prefix 6d8b95ec, frozen by the T4 theory auditor in T4-468): its header
    comment (B) and one print line read "sup over s > 0 of s (mu - C s)^2 is 4 mu^3/(27 C)". Over all s > 0 that
    supremum is infinite (T4-468, team note v245); the value is the supremum over the positive-margin range
    0 < s < mu/C, which is the square of the maximum of t (mu - C t^2) over t > 0. The code checks that unsquared
    concave form and R1-047 uses the correct range, so no check, bound or verdict changes. The script is left unchanged
    because the T4 theory auditor froze its hash.
80. theory_v08 (frozen; repairs from T4-471, T4-473, the coordinator NOTES 16:01Z item 3 and the T2 theory worker handoff BO5). No verdict
    changes.
    - Lines 189 and 413: delta = 0.44764... is wrong. delta = 1 - 1/c0 = 1824676646553933/4076476460239181 =
      0.4476112310... (T4-473; section 1 of this file has 0.447611231).
    - Line 212: "below 2.7e-6" is REFUTED as a common radius cap (T4-471). A TB-sharp ball with s = 1/4096,
      r = 1536/10^6 and positive margin has L^2 radius 3e-6. At the registered fixed weights, the cap is 3.7930e-6.
      The 002, 003 and 004 distances exceed it by factors above 60000.
    - Lines 213, 851 and 1008: row 35 is described as framework inapplicability only. Since v140 it also records the
      affine L^2 exclusion of 001 at every real c (T4-458 with R1-046 and the review of T4-458; AUDITED via T4-465).
    - Lines 853 and 854: "each concerns the fixed c and the stated balls" is false for 001. Read: each concerns a fixed
      c and the stated balls, except 001, whose exclusion holds at every real c in the affine L^2 class.
    - Header INDEX "through C1-N1-027", section 4 and R5: 028 was registered at 15:24:01Z, before v08. It is
      registered, FLOAT, OPEN (rows 107 and 108).
    - Lines 612 to 617 (the T2 theory worker D2, D3): the WU3 hypotheses must be stated (registered state 131 floors M1 >= (9/10) I and
      M2 >= (1/2) I, w1 >= 2, w2 >= 1, C >= K00 > 390.68, c_U >= A' + B' > 1.5871, X(h) >= sqrt(w2) ||h||_2). The
      4.0249e-6 bound (beta 11/4) is for balls of the T2-R1 TB-sharp matrix with E0 as one component, not for T2-R3
      balls. The "Not covered" list must also name separate weights on b and on the H part of E0, other Gram schemes,
      and balls whose L^2 control is not sqrt(w2) ||h||_2.
    - Line 894: "about 0.015 H" is the T1/T3 theory worker's FLOAT estimate (R1-044, review set 41 item 9(g)), not a the T2 theory worker statement.
    - Line 949 (the T2 theory worker D4): "CHECK_T1_v08_FACTORS revision 1, section 3.3" names a section that review does not have.
      v08's own section 3.3 is meant.
    - The T2 theory worker hash prefixes: the handoff 048db91f and the review of T4-459 e140e6c0 cited by v08 are those files as of
      section BM. the review of T4-459 is now revision 2 (714be6bb...).
81. Draft 52, repaired in draft 53. No verdict changes.
    - Lines 151 and 161: the 2.7e-6 cap is replaced by 3.7930e-6. For 001 the radius parenthesis is removed, because
      that exclusion holds at every radius.
    - Lines 153 and 1728: the row 35 scope, as in item 80.
    - Lines 88, 1285, 1513 and 1713: N4-259 (017 at (21, 522)) was called OPEN. It has been CONFIRMED since N4-384,
      accepted in T4-460 at 14:47Z (strict floor 0.000596123050327423), and stays outside the 25 registered probes.
    - Lines 168 to 170: 028 is registered (15:24:01Z).
    - Lines 659, 660 and 667: the WU3 scope, as in item 80.
    - Line 1012: the 0.015 H attribution, as in item 80.
82. review set 46 R1-048 V5 says that the N4 numerical auditor pairing ball "lies inside" the N3 numerics worker's 30-digit display. The stored
    check_N4396.py tests only overlap. A separate Arb test at 16:05Z (not in the stored script) shows containment in
    both modes. The T1/T3 theory worker team note v54 item 5 says "read 15:45Z to 16:10Z"; the reading ended at 16:08Z.
83. Draft 53, repaired in draft 54 (T4-482 unless stated). No verdict changes.
    - Line 1384: "a_n + b_n is about 1e-38, so the optimal t is 1" is literally false. a_n + b_n > 0 in both modes,
      so the exact optimum is t* = -b_n/a_n < 1, with 1 - t* about 2.0e-38 (mode 1) and 1.8e-36 (mode 3), as R1-049
      V9 printed. Choosing t = 1 is valid and changes no floor. The next sentence, "the remaining gap lies in modes 5
      and higher", holds up to about 1e-30 in H^2 and is CONDITIONAL on the N3 numerics worker's displays.
    - Lines 1386 to 1388: the E2(007) range [606.8181535, 606.8202171] and the E2(017) range [605.4068698,
      605.9589545] were rounded inward. The outward displays are [606.8181534, 606.8202172] and [605.4068697,
      605.9589546].
    - Line 1545: "a margin of 1.4 percent" is a rounded display; the certified margin is above 1.39 percent.
    - Lines 1380 to 1383: "the N4 numerical auditor holds the improved value OPEN" and "R1-050 ... is pending" are superseded (N4-407,
      N4-410, T4-480, T4-481, R1-050, R1-051).
    - Section 2.1 did not say that 2.1035e-4 is the threshold at the selected radius only (T4-479); added. Draft 53
      made no maximality claim.
84. Errata to the T1/T3 theory worker reviews since draft 53.
    - review set 47 E1 to E3: R1-048 V5 containment came from a separate Arb test (item 82); R1-049 V6 exponent 7/5, not
      7/10 (T4-477 and N4-408 REFUTE 7/10); team note v54 item 5.
    - review set 48 E4 to E7: decimals in R1-050 V7, R4 and V8 were rounded inward. R2 in [51.061045287604984,
      51.061045287604985]; M2 upper <= 1.129995950; H(016) <= 1.063012677 and <= 0.944106347; E2(016) <= 763.064677
      without the improvement; the loss bounds rounded up. T4-481 REFUTES the inward displays and gives the same safe
      values; the coarse bounds 1.063013, 0.944107 and 722.968760 stand.
    - review set 49 E8 to E10: the margin of R1-048 V7 (above 1.39 percent); the "modes 5 and higher" statements of
      R1-048 R2 and R1-049 V9 (up to about 1e-30 in H^2, CONDITIONAL); R1-050 V4 "coincide only for exact data" (they
      coincide exactly when U_n = L_n for every included n < N, however loose the total upper U is; T4-481).
85. The T1/T3 theory worker team note v56 item 3 names "sections 2.3 and 2.4" for the T4-065 value. It means section 2.3 (draft 53 line
    445) and the section 2.8 table (draft 53 line 657). Corrected in team note v57.
86. Since draft 54. Section 2.1 said "2.1035e-4 is the value selected at r = 1351/10^6" without saying that it uses the
    rounded rate 1557/10000; the exact value at that radius is already above 2.1046e-4 (N4-415), within about 4.741e-11
    of eta*; added. review set 50 E11: R1-051 V7 "modes 1 to 31 carry at most 0.9888 of R2" is false; the share is
    between 0.988805 and 0.988806 (T4-483 REFUTES the literal display; no bound used it). No verdict changes.
87. Since draft 55. Section 2.1 said "Every failure factor in this report uses 2.1035e-4"; the correction-distance
    factors, the other framework ratios and the factor 3594606 against eta* use other denominators (T4-487 REFUTES the
    literal scope). Drafts 56 to 59 read "Every sharpw forcing factor quoted in this report is against the selected
    threshold 2.1035e-4". review set 50 E11 and section 12 gave check_v50.py 33 checks; it runs 20 (13 after Part A, 20
    cumulative after Part B; T4-487, review set 51 E12). The artifacts README still named closure_matrix_v151.md in the
    input columns of row_refs.py and h18_verdicts.py after both had moved to the v153 copy (T4-487); repaired. The
    two-mode 016 displays of draft 55 are valid and are superseded in section 7 by T4-486 and N4-418. N4-419 REFUTES a
    universal 2e-13 Taylor tolerance of the frozen NUMERICS_FINAL for 007 (2.0899e-11 < [y^4] (F/y)(0, y) <
    2.0900e-11); no draft states that tolerance, and the T4-211 projection of section 3.5 (S3) removes such coefficients.
    Section 9.3 item 1 said, after the numerics_v06 reading, that 013 cut the first-mode pairings at k <= 1000 by two
    to three orders of magnitude. The numerics_v06 table gives the factor 26.8 at k = 128, factors below 2.1 or
    increases at 192 <= k <= 1024, and 9359 at k = 12 (FLOAT; N4-420 checks the k <= 128 range exactly and REFUTES the
    corresponding universal statement of the frozen NUMERICS_FINAL); corrected. Section 9.3 item 5 still listed the
    seven-cell test for 012 to 017 as a quantity to measure; it is done, and every cell fails, for 015, 016 and 017
    (section 9.2 item 7), so item 5 now names 011 to 014 and 018 to 028, and 9.2 item 7 says 018 to 028 (not 027). No
    verdict changes.
88. Since draft 56. Sources and acceptances only. The T4 theory auditor's T4-490 CONFIRMS N4-419 from the full origin jet of 007: all
    five nonconstant degree-two and degree-four Taylor coefficients of F/y at the origin exceed 2e-13 in magnitude (the
    smallest, [x^2 y^2], lies in (-2.32866e-12, -2.32865e-12)), so the universal tolerance statement of the frozen
    NUMERICS_FINAL is REFUTED by both audit lanes; no draft states it. T4-489 accepts the T2 theory worker's review of T4-469 revision 2,
    which repairs a necessity claim and leaves the sufficient theorem T4-469 unchanged, and
    the T2 check of T4-479 (report repair). The N4 numerical auditor's N4-421 compares the T4-486 and T4-488 assembly of the 016 enclosure with
    N4-417 and N4-418 (180 checks): equal lower squares and selected floors, upper squares differing by less than
    10^-500. Matrix v157 (v156 joined nine bullets in error; v157 restores them). No verdict or number changes.
89. Since draft 57: the wording findings of the T2 theory worker handoff BS (read on draft 55; checker
    artifacts/arith/bs_draft55_errata_check.py, 29 checks, in the T2 theory worker lane), each checked here against its source.
    (a) Section 2.7 called handoff AJ2 CLAIMED and section 9.2 item 9 listed "the T2 theory worker handoff AJ2 and AK2 (CLAIMED)"
    among the results awaiting review; AJ2 is CONFIRMED by the T4 theory auditor T4-290 (under the unchanged high-row margin and
    norm-domination hypotheses) and AK2, the S1 squared constant 63/32, by T4-301 (already so cited in section 9.2).
    (b) Section 0 and section 9.4 put both WU3 factors in "the T2-R3 L^2 budget": 1.1746 is for T2-R3 balls (beta 2) and
    1.0612 for balls of the T2-R1 TB-sharp matrix with E0 as one component (beta 11/4), as section 2.8 states. (c) The
    closure inequality of section 2.1 omitted the checks beta(r) > 0 and 7/10 - c_s r > 0, which hold at the selected
    radii. (d) The section 2.5 table gave epsilon_max 1.8938e-7 without its box. (e) Section 2.8 and item 80 said
    "fixed state 131 floors" for the WU3 hypotheses; they are the registered floors M1 >= (9/10) I and M2 >= (1/2) I
    (:H3), not the T4-119 floor ceilings (the T2 theory worker erratum BS2 (i)). The T2 theory worker BS2 (ii): the K_H displays 9.6432 and 6.4226 of
    section 2.1 are true upper bounds as printed (the exact 1/beta(r) are about 9.640415 and 6.419185). Wording only;
    no verdict, bound or threshold changes.
90. Since draft 58. (a) Section 0 item 7 required a certified scalar distance lower bound "below 3.79e-6". The T4 theory auditor's
    T4-491 (278 checks, on the T2 theory worker's T2 final summary) REFUTES 3.79e-6 as a uniform scalar-budget cap: the exact TB-sharp
    parameters s = 1/4096, r = 3791/1953125 admit an L^2 budget of 3.791e-6 with positive rate, contraction and slope.
    The valid common upper bound is 3.7930e-6 (T4-454), as section 9.2 item 1 already states; item 7 now prints
    3.7930e-6 and 4.5717e-4. (b) Section 9.3 item 1 and item 87 printed the 013 first-mode factor at k = 12 as 9358; the
    exact value from the saved register is 9358.8588... (N4-420, T4-492), so the upper end of the range is 9359 to the
    nearest unit. (c) Section 9.2 item 3 now records that a complete closure check needs beta(r) > 0 and the slope
    margin, as T4-491 asks; section 2.1 states both since draft 58. (d) Sources: T4-491 also REFUTES 0.99998313 as an
    exact factor and leaves "closest candidate" OPEN as a ranking of actual distances, both in the T2 final summary; this
    document prints neither (section 0 item 3 says best observed candidate, erratum 32). T4-492 accepts N4-420, and N4-423
    CONFIRMS T4-490 and T4-492; N4-422 confirms the N1/N2 numerics worker's NUMERICS_FINAL repairs of 17:25Z except two literal items (the
    attribution of a 024 hash and a "four largest values" phrase), neither of which this document cites. No verdict
    changes.
91. Since draft 59. The T4 theory auditor's T4-493 (535 checks) CONFIRMS draft 58 (31 changed blocks, 186 README hashes, 83 row
    references, 78 directed floors) and R1-052, and REFUTES two literal statements. (a) Section 2.1 of drafts 56 to 59
    said "Every sharpw forcing factor quoted in this report is against the selected threshold 2.1035e-4" and then quoted
    the factor above 3594606 against eta*; it now reads "Unless expressly compared with eta*, the sharpw forcing factors
    in this report use the selected threshold 2.1035e-4"; item 87 now quotes the old sentence as the reading of drafts
    56 to 59. (b) R1-052 V8 said the N3 numerics worker's H lower 0.6167335007 is "within 3.6e-11" of the strict lower HL; the exact
    difference HL - 0.6167335007 is 18225240013184170643/(5 10^29), in (3.64e-11, 3.65e-11) (review set 52 E13;
    check_N4418.py now checks it exactly, 89 checks). No number of this document used that FLOAT position. T4-494
    accepts N4-422. No verdict changes.
92. Since draft 60. The T4 theory auditor's T4-497 (452 checks) CONFIRMS draft 60 and review set 52 with no further wording request.
    Section 7 adds (a) the 017 lower bound H(017) > 0.614419598760 and the mode 1 and 3 enclosures of N4-425 (T4-495,
    N4-426), with the T1/T3 theory worker's R1-053 (review set 53), the check of the residual identity the N4 numerical auditor asked T1 and T2 for at 17:17Z,
    and (b) the sharper 016 uppers H(016) < 0.617899376 and E2(016) < 628.865882 of N4-427 and N4-428 (T4-498), with
    H(007) - H(016) > 0.017625000525836. T4-496 and N4-424 close the NUMERICS_FINAL literal repairs, which this
    document does not cite. The complete H(017) upper, E2(017) and E2(017) < E2(007) stay CLAIMED. No verdict changes.
93. Since draft 61. The section 2.5 table printed the FW-T-T4L2-v1 threshold as 6.1035e-6, a downward rounding of the
    exact 1/163840; it now prints 1/163840 (above 6.1035e-6), as the rebal row prints 3/327680 since draft 60. A
    threshold rounded down overstates a ratio norm/threshold; the N3 numerics worker's 007 record of 05:47Z did that (8.4699902e+7,
    REFUTED as the exact quotient by N4-429; corrected to 8.4699685e+7). No number of this document used the rounded
    value. T4-499 accepts the T2 theory worker's T2 final summary repairs and its decimal sweep (mu < 5.04423 is safe, 5.0442 is
    too small; this document prints 5.04423). No verdict changes.
94. Since draft 62. Section 7 adds the N4 numerical auditor's prefix 63 bounds (N4-430, N4-431: H(016) < 0.617897369, E2(016) <
    628.865389) as the N4 numerical auditor numbers recomposed by the T1/T3 theory worker's R1-054, pending the T4 theory auditor; R1-054 also recomposes N4-427 and
    N4-428, which stay the accepted bounds. T4-500 CONFIRMS N4-429's exact threshold divisions (007 floors 84699685 and
    66246337) and T4-501 accepts R1-053 together with the T2 theory worker's review of the same identity. No verdict changes.
95. Since draft 63. The T4 theory auditor's T4-502 (7564 checks) CONFIRMS N4-430 and N4-431, so section 7 now gives H(016) <
    0.617897369, E2(016) < 628.865389 and H(007) - H(016) > 0.017627007636152 as accepted both ways (draft 63 gave them
    as the N4 numerical auditor numbers pending the T4 theory auditor), and section 0 cites the new H gap. N4-432 and T4-503 accept the 017 residual
    identity from both audit lanes and discharge the T2 theory worker's origin condition R3 for the actual 017 source; the T2 theory worker's revision
        1 (handoff BV) corrects the auxiliary cross bound by the factor n. The H(017) upper, E2(017) and E2(017) < E2(007)
    stay CLAIMED. No verdict changes.
96. Final (since draft 64). The N4 numerical auditor's N4-433 accepts T4-502 reciprocally and the T2 theory worker's revision 1. The H18 checks
    (artifacts/checks/h18_verdicts.py and row_refs.py) now default to the frozen copy
    checks/data/closure_matrix_v170.md of matrix v170 (18:22Z); on this text they give outputs byte-identical to the
    stored ones. The matrix copies v135 to v153 are stored gzip-compressed to keep artifacts under 20 MB. The T4 theory auditor's T4-504
    CONFIRMS R1-054 and REFUTES its V5 reading that the mode gaps sit in the lower bound (review set 55 E15); section 7
    states the gaps as enclosure widths and now cites T4-504. No verdict or number changes.


## 12. Reproduction

- All the T1/T3 theory worker code and small data are in working file artifacts (not published) (about 18 MB). artifacts/README.md gives the exact command for
  each script (relative paths, OMP_NUM_THREADS=1, python -B) and the sha256 of every stored input and output.
  `bash run_all.sh` reruns every script under taskset and nice (the README records the run times);
  `bash run_all.sh OUTDIR` writes the outputs elsewhere for comparison.
- Scripts behind the main numbers of this report:
  - checks/check_T2R3.py: exact Gram and row-sum certificates of the sharp and sharpw constants (section 2.1).
  - checks/check_T4182.py, checks/check_T4185.py: the 007 distance probes (mode 1 and mode 7; section 3.3).
  - checks/check_T4206.py, checks/t4206_angular_sup.py: the weighted velocity constants (section 3.1).
  - checks/check_T4205.py, checks/check_T4222.py, checks/tail_profiles_007.py: tail and dilation geometry (3.4).
  - checks/check_T4234.py, checks/check_T4235x.py: forced lower tails and the 007 cross-check (G6).
  - checks/check_T4199.py, checks/check_T4211.py, checks/check_T4229.py: finite-span structure and damping (3.5).
  - checks/origin_inv_table.py, checks/check_joint_ceiling.py: origin thresholds (section 6).
  - checks/annulus_admissible.py: admitted L^2 mass of localized corrections (section 2.7).
  - transfer_checks/transfer_numbers.py: the numbers quoted from the Hou literature transfer (section 5).
  - checks/check_TP6.py: the R-SCREEN radii and the endpoint reach thresholds of R1-038 (section 3.4 (G7)).
  - checks/check_T4372.py: the review R1-039 of the sharp moment constant of T4-372 (section 3.4 (G6)).
  - checks/check_T4381.py: the review R1-040 of the universal velocity lower bound of T4-381 (section 3.4 (G7) (e)).
  - checks/check_N4refdiff.py: the review R1-041 of the N4 numerical auditor reference-difference lemma (section 3.4 (G7) (a)).
  - checks/check_T4397.py: the review R1-042 of the X_(s,w) ball velocity lower bound of T4-397 (section 3.4 (G7) (e)).
  - checks/check_T4410.py: the review R1-043 of the T4-410 two-weight velocity remainder (section 3.4 (G7) (e)).
  - checks/check_R1044.py: the outer-amplitude bound (R44.1) and the kernel thresholds of R1-044 (section 3.4 (G7) (e)).
  - checks/check_T4425.py: the review R1-045 of the radial averaging obstruction of T4-425 (section 3.4 (G7) (e)).
  - checks/h18_table_ratios.py: exact recomputation of every ratio of the section 7 distance table from the displayed
    floor and the ceilings 3.7930e-6, 2.8496e-6 and 25/54684 (the coordinator 13:41Z item 11; 78 ratios, 0 mismatches at
    drafts 48 to 64 and the final).
  - checks/row_refs.py: every reference "C1-N1-0XX ... row N" of this file names a closure matrix row of that
    snapshot (reading only; with the final and the frozen copy checks/data/closure_matrix_v170.md, 83 references and 0
    mismatches, as with drafts 57 to 64 and the v157 copy; draft 56 had 83 with the v155 copy).
  - checks/h18_verdicts.py: the H18 check of every candidate verdict of sections 0 and 7 against the closure matrix, row
    by row, with the frozen copy checks/data/closure_matrix_v170.md (drafts 57 to 64 used the v157 copy and earlier
    drafts the v135 to v155 copies, each passing; v135 to v153 are stored as .gz, restore with gunzip -k; at the final
    Part B checks 161 claims with 0 failures; Part C, a sentence scan, flags 0 sentences; Part D, the scope of the 001
    to 004 statements, erratum 77, 7 claims).
  - checks/check_T4458.py: review R1-046 of T4-458 (section 0 item 1): the polar formulas (3), (4) and (6) of the PROOF
    against Cartesian differentiation (sympy, exact), and G_0, G_1 and the leading residual coefficient E of 001
    recomputed from the raw generator file by direct differentiation of homogeneous functions with exact rationals,
    equal to the T4 theory auditor table (912 checks; inputs checks/data/C1-N1-001_raw.json and
    checks/data/T4458_leading_coefficients.json).
  - checks/check_T4462.py: review R1-047 of T4-462 (section 2.8): the determinant and numerator identities, the AM-GM
    elimination of both weights and its equality point (sympy, exact), the constants K and v (interval arithmetic), and
    for the seven rows of T4-462 the strict bounds by exact Sturm root counts, with the gain and 007 factors compared
    exactly (48 checks; no input files). Its comment (B) and the matching print line omit the range 0 < s < mu/C
    (section 11 item 79).
  - checks/check_N4396.py: review R1-048 of N4-396 (section 7): admissibility of the 663 test coefficients, the exact
    gradient energies d_1 and d_3 by rational Beta integrals in r (equal to the N3 numerics worker and the N4 numerical auditor rationals), the mode
    floors from the N4-396 pairing balls in Arb at 1200 bits, the exact H and E2 floors against the 007 upper bound,
    and the FLOAT E2 table of numerics_v15 (1368 checks, 140 s; inputs checks/data/N3_016_hdual_m13deep.json,
    N4396_mode_001.json, N4396_mode_003.json, N4396_result.json, N4392_comparison.json, N4252_result.json).
  - checks/check_T4469.py: review R1-049 of T4-469, ERRATA_v01 and the v247 identity (section 7): the right inverse,
    (7) to (11), the pole factor and the r^2 Delta_n label shift in sympy, exact fixtures, a 40-digit quadrature
    comparison (FLOAT), and for 016 the exact a_1, a_3 and the CONDITIONAL mode 1 and mode 3 upper-lower comparison
    (65 checks, 330 s; inputs checks/data/N3_016_hdual_m13deep.json, N4398_mode_001.json, N4398_mode_003.json,
    N4398_result.json).
  - checks/check_T4474.py: review R1-050 of T4-474 and of the tail step of N4-403 (section 7): parity, div A_F = F,
    the cutoff and Parseval steps and a manufactured fixture in sympy; the prefix lemma symbolically and on 204 exact
    lists, the outward and split formulas and the omission counterexamples; the four-mode 016 composition from the
    saved endpoints; the CONDITIONAL mode 1 and 3 comparison with the N3 numerics worker's displays (4783 checks, 7 s; inputs
    checks/data/N4403_result_v01.json, T4474_parameters.json, N4392_comparison.json, N4396_result.json,
    N4398_result.json, N3_016_hdual_m13deep.json). Its displays are directed since review set 48 section E.
  - checks/check_N4409.py: review R1-051 of N4-409 and N4-410 (section 7): bindings, the coverage of the 16 modes 1 to
    31 of 160, the exact tail, M2, H and E2 bounds at N = 33, both N4-410 squares and strict displays, the 007 gap and
    the H(007) comparison (54 checks, under 1 s; inputs checks/data/N4409_result_v02.json, N4410_result.json,
    N4410_parameters.json, N4403_result_v01.json, N4392_comparison.json, N4396_result.json, N4398_result.json,
    N4252_result.json, N3_016_hdual_m13deep.json). Its FLOAT line on the share of R2 in modes 1 to 31 is not directed
    (review set 50 E11).
  - checks/check_v50.py: erratum E11 (the exact share of R2 carried by modes 1 to 31, between 0.988805 and 0.988806)
    and the sharpw values at r = 1351/10^6 of section 2.1 (N4-415), exact (20 checks, under 1 s; inputs
    checks/data/N4409_result_v02.json, N4392_comparison.json).
  - checks/check_N4418.py: review R1-052 of N4-417 and N4-418 (section 7): bindings, the 16 prefix intervals and M2
    upper equal to N4-409's, the 16 selected floors, both H squares, the per-mode width split, both E2 squares, strict
    endpoints, the 007 gaps and the T4-486 displays, and the comparison with N4-410, and the exact distance of the N3 numerics worker's H
    lower below HL (89 checks, under 1 s; inputs checks/data/N4418_result_v01.json, N4417_result_v03.json,
    N4409_result_v02.json, N4410_result.json, N4392_comparison.json, N4398_result.json, N4252_result.json).
  - checks/check_N4425.py: review R1-053 of the residual identity and bounds (1), (2) of the N4 numerical auditor's 017 replay proof
    (sympy for generic profiles; three manufactured fixtures by 50-digit quadrature, FLOAT, and by the exact
    t-formulas) and the exact recomposition of N4-425 (H(017) > 0.614419598760; modes 1 and 3) from the saved strict
    endpoints (79 checks, about 31 s; input checks/data/N4425_extract.json, fields copied from the N4 numerical auditor's result.json,
    mode_001.json and mode_003.json).
  - checks/check_N4427.py: review R1-054, the exact recomposition of N4-427 and N4-428 (prefix 47) and N4-430 and
    N4-431 (prefix 63) for candidate 016 from the saved endpoints: M2 at N = 49 and 65, U2 = M2 upper - J, strict H and
    E2 endpoints, the gaps over 007, nesting and the width split (272 checks, about 0.1 s; input
    checks/data/N4427_extract.json written by checks/make_N4427_extract.py from the four the N4 numerical auditor results, with
    N4418_result_v01.json, N4417_result_v03.json, N4392_comparison.json, N4252_result.json).

- Numbers attributed to other lanes are reproduced in their own artifacts; the source ID (T4-, N4-, the N3 numerics worker) is given
  at each use.
