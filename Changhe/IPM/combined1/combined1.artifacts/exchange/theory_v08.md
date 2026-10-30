# theory_v08 (batch T requirements for batch N; last exchange version)

## Header

- Version: theory_v08. This is the last exchange version of batch T (the coordinator H16 checkpoint, 12:30Z, item 8). The
  final long-form report is working file THEORY_FINAL.md (not published), frozen at 18:30Z and final at 19:00Z.
- UTC: 2026-10-29T15:30:58Z (time of the copy into working file theory_requirements (not published); content frozen at that time).
- Author: The T1/T3 theory worker (batch T publisher; T1 and T3), after consulting the T2 theory worker (handoff through section BM, its reviews
  the review of T4-402, the review of T4-410, the review of T4-414, the review of T4-415, the review of T4-458, the review of T4-459 and the review of T4-462,
  its falsification check the T2 falsification review of the endpoint and the report summary of THEORY_FINAL draft 36 and its revision 3 note) and the T4 theory auditor (the
  audit of the published theory_v07, T4-412, research/published_v07_audit; the audit of THEORY_FINAL draft 34, T4-433,
  research/theory_final_draft34_audit; the ledger through T4-469 (team note 247)). The consultation was the T1/T3 theory worker team note
  v47 (notes/team note 47, 12:50Z), which gave the proposed scope and the 24-row factor table of section 1 and
  asked for comments by 14:30Z. The T4 theory auditor audited that table in T4-437 (research/theory_v08_factors_audit): it REFUTES the
  numerator of row S2, CONFIRMS the corrected 24 comparisons and asks for six scope repairs; all are made here. Its
  audit of THEORY_FINAL draft 38 (T4-442, research/theory_final_draft38_audit) asks for six further repairs, item 74 of
  section 8. Two previews preceded this file and are kept unchanged in working file drafts (not published): preview1 (theory_v08_preview1.md,
  generated 13:29:19Z, sha256 prefix d8c8e8ba, 769 lines), audited by the T4 theory auditor in T4-445, whose seven scope repairs are
  made in preview2; and preview2 (theory_v08_preview2.md, generated 13:55:03Z, sha256 prefix 5940b948, 868 lines),
  audited by the T4 theory auditor in T4-455, which CONFIRMS its changed mathematics and scoped factors and asks for three updates, made
  here (section 3.1), and checked by the T2 theory worker in CHECK_T1_v08_FACTORS revision 2 (the Targets bullet of section 1.1;
  handoff BG).
- Scope. New here: the failed tests for specified certificates at 007, each with the factor by which it fails, and the
  open items without a factor (section 1; the coordinator H16 item 8 asked for "the exact list of unresolved inequalities", and
  T4-437 asks that a failed test of a chosen certificate not be called an unresolved inequality for existence); the
  repairs of theory_v07, including a narrower NC-T-UNIV-E (section 2); the status changes T4-409 to T4-469, N4-333
  to N4-397, the T2 theory worker the review of T4-402 to the review of T4-462 and the T1/T3 theory worker R1-043 to R1-047 (section 3); the candidates 023 to
  027, the affine L^2 exclusion of 001 and the dyadic tests at 015, 016 and 017 (section 4); the endpoint route and the
  obstruction NC-T-TWO-WEIGHT (section 5); the final requests (section 6); the review requests (section 7); errata 67 to
  79 (section 8); and the responses to numerics_v12, numerics_v13 and numerics_v14 (section R5). Sections of theory_v07
  that are not restated hold as published, with the repairs of section 2 and the errata of section 8; in particular
  theory_v07 section 4 (the PROMPT section 6 report) and sections 5.6 and 5.7 (d) are unchanged except as stated in
  sections 1 and 5 below. The section order differs from theory_v07: its sections 1, 2, 3, 5.7, 6, 7, 8 and R4
  correspond to sections 2, 3, 4, 5, 6, 7, 8 and R5 here. The long-form report is working file THEORY_FINAL.md (not published) (draft 52,
  sha256 prefix 82b4d9db1e5e25af at publication); where the two differ, this frozen file is the requirement text.
- Consulted lanes and exact files. Each file is given with the first 16 hex digits of its sha256 (8 for the T1/T3 theory worker
  reviews); Appendix H lists the full values. The files new since theory_v07 were read between 2026-10-29T11:20Z and
  2026-10-29T15:30Z and hashed at publication. The append-only ledgers are cited through the stated entry;
  entries appended after it were not read for this version. Every other file was checked to be unchanged since it
  was read:
  - working file theory_v07.md (not published) (theory_v07 (superseded)), 42eb222a38caadac
  - working file numerics_v12.md (not published) (numerics_v12), 20763c86645a9546
  - working file numerics_v13.md (not published) (numerics_v13), 7ae8af1782e3d8e8
  - working file numerics_v14.md (not published) (numerics_v14), 21c809ab7b3dbf7f
  - working file closure_matrix.md (not published) (closure matrix (v140)), 927f13f5303198d4
  - working file INDEX.md (not published) (snapshot INDEX (through C1-N1-027)), 276ac7ee13c84619
  - working file verdict ledger (not published) (the T4 theory auditor ledger (cited through T4-469)), 0299dffefd791681
  - working file team note 247 (not published) (the T4 theory auditor team note), 4c5a9a7d5e8e68db
  - working file PROOF.md (not published) (T4-409), e6f9f4e3cd51e7c4
  - working file PROOF.md (not published) (T4-410), cd2e6f18fb4b9255
  - working file PROOF.md (not published) (T4-411), e72bc63bf849a60c
  - working file PROOF.md (not published) (T4-412), 5720a3c058165143
  - working file PROOF.md (not published) (T4-413), 3f5da5310fccb4fe
  - working file PROOF.md (not published) (T4-414), 0e0f608d167b2c34
  - working file PROOF.md (not published) (T4-415), 57110fd5b3c62f0f
  - working file PROOF.md (not published) (T4-416), b7848590e9050554
  - working file PROOF.md (not published) (T4-417), 1ad317d8290220cb
  - working file PROOF.md (not published) (T4-418), ec364dc7a9be28ef
  - working file PROOF.md (not published) (T4-419), 025500c420e787e4
  - working file PROOF.md (not published) (T4-420), 5b8f6a0736b5b28b
  - working file PROOF.md (not published) (T4-421), 93f001802c42ef67
  - working file PROOF.md (not published) (T4-422), fb03764b22fd8ab3
  - working file PROOF.md (not published) (T4-423), 865eb8423aeae53e
  - working file PROOF.md (not published) (T4-424), 0c2d360a304f04f5
  - working file PROOF.md (not published) (T4-425), 4d13c623b32b738f
  - working file PROOF.md (not published) (T4-426), 935e166fdaaf4d79
  - working file PROOF.md (not published) (T4-427), 7e76ce5e6951dd47
  - working file PROOF.md (not published) (T4-428), 9801f71f1a470e08
  - working file PROOF.md (not published) (T4-429), b151176fffd24258
  - working file PROOF.md (not published) (T4-430), 5cb2e5fe0e0a3618
  - working file PROOF.md (not published) (T4-431), d0b409da2c491469
  - working file PROOF.md (not published) (T4-432), c2035403ef932424
  - working file PROOF.md (not published) (T4-433), 8f6f8232bc5660c5
  - working file PROOF.md (not published) (T4-434), 8848da16d556cb00
  - working file PROOF.md (not published) (T4-435), 026501ef13ee36dd
  - working file PROOF.md (not published) (T4-436), b4257d03f59aeee2
  - working file PROOF.md (not published) (T4-437), b7c3e467fdc2a8cf
  - working file PROOF.md (not published) (T4-438), 6d795defef60a41d
  - working file PROOF.md (not published) (T4-439), 88b01d4f5e77b8ab
  - working file PROOF.md (not published) (T4-440), 88b9c219728bb134
  - working file PROOF.md (not published) (T4-441), d7689362724aa9ac
  - working file PROOF.md (not published) (T4-442), 6d890545d3384c2e
  - working file PROOF.md (not published) (T4-443), 972ac08e7af86005
  - working file PROOF.md (not published) (T4-444), 630ccc8cbbd1e112
  - working file PROOF.md (not published) (T4-445), 0eb9308dea16756f
  - working file PROOF.md (not published) (T4-446), 97d9a73864ad89d8
  - working file PROOF.md (not published) (T4-447), 41e5dff47ecf8fb1
  - working file PROOF.md (not published) (T4-448), 3d1d4bad28cebe29
  - working file PROOF.md (not published) (T4-449), 78f0caa4275f993e
  - working file PROOF.md (not published) (T4-450), 042beeb993874daf
  - working file PROOF.md (not published) (T4-451), 05028d893c13ae9a
  - working file PROOF.md (not published) (T4-452), 88b0ac35e4607224
  - working file PROOF.md (not published) (T4-453), a2319328ba7b3fdb
  - working file PROOF.md (not published) (T4-454), bba858593cf8d4c9
  - working file PROOF.md (not published) (T4-455), 8c1b6532cf66d1c0
  - working file PROOF.md (not published) (T4-456), 644e6d03ba403ff9
  - working file PROOF.md (not published) (T4-457), 4daf08a6a8b3e769
  - working file PROOF.md (not published) (T4-458), 771ad6b4af564e1b
  - working file PROOF.md (not published) (T4-459), 353fc1575bccca19
  - working file PROOF.md (not published) (T4-460), 3a1dd3017e44b9cf
  - working file PROOF.md (not published) (T4-461), 27cd1dc8f365f769
  - working file PROOF.md (not published) (T4-462), 3c871d7f9ef82ba6
  - working file PROOF.md (not published) (T4-463), 0e32cdb67612d8d6
  - working file PROOF.md (not published) (T4-464), 3e9793dfb4e539a2
  - working file PROOF.md (not published) (T4-465), a3dbba66ab10ccb3
  - working file PROOF.md (not published) (T4-466), 488b4a7207c8cb91
  - working file PROOF.md (not published) (T4-467), dae8594bf2eee8cd
  - working file PROOF.md (not published) (T4-468), 5dd594c0b033ce0a
  - working file PROOF.md (not published) (T4-469), efabe956aa103859
  - working file ERRATA_v01.md (not published) (T4-469 erratum (team note v247)), 45e743dd2ef7ac92
  - working file ERRATA_v01.md (not published) (T4-458 erratum (T4-465)), 00f281c080c5ee4a
  - working file PROOF.md (not published) (T4-381), ca0e008a1bfb7868
  - working file PROOF.md (not published) (T4-397), 9afe571d5720f1bc
  - working file PROOF.md (not published) (T4-402), a98e64b04a4ab8f8
  - working file PROOF.md (not published) (T4-380), 4fcfd14192b17ea5
  - working file PROOF.md (not published) (T4-351), 85e01f1bfab61b07
  - working file PROOF.md (not published) (T4-335 (AUDITED, T4-350)), 99aa80a9b5ce0474
  - working file verdict ledger (not published) (the N4 numerical auditor ledger (cited through N4-397)), 3470e7422509927a
  - working file PROOF.md (not published) (N4-352), 1562433ed593d3f3
  - working file PROOF.md (not published) (N4-354, N4-355), af2715bfbf2369e0
  - working file PROOF.md (not published) (N4-356), fbb936cbf9dd27aa
  - working file PROOF.md (not published) (N4-361), 58d972990c446275
  - working file PROOF.md (not published) (N4-363), 9fa1d42aab6569b2
  - working file PROOF.md (not published) (N4-365), b26e24fdcb627135
  - working file PROOF.md (not published) (N4-366, N4-367, N4-369), c076010696004d25
  - working file PROOF.md (not published) (N4-368), f0ffb789598753cf
  - working file PROOF.md (not published) (N4-370), 79fce8fe5fa3e7eb
  - working file PROOF.md (not published) (N4-371), 7e66a460a0bbd00d
  - working file PROOF.md (not published) (N4-372), 1c0c4d2cc12729d6
  - working file PROOF.md (not published) (N4-373), 4547c192d6a28557
  - working file PROOF.md (not published) (N4-374), ed8f4a073d6242d4
  - working file PROOF.md (not published) (N4-375), b4bb5ba465c472c4
  - working file PROOF.md (not published) (N4-376), 48e64a92735a2129
  - working file PROOF.md (not published) (N4-377 to N4-379), 32ad46f88f6ff3ae
  - working file PROOF.md (not published) (N4-380), 1a5b775112dc1066
  - working file PROOF.md (not published) (N4-381), 8a97d1c987604ca5
  - working file PROOF.md (not published) (N4-382), d7b34632c5722208
  - working file PROOF.md (not published) (N4-383), 0999eeb3dcb8be8f
  - working file PROOF_v02.md (not published) (N4-384), 54283bcc7da74a9b
  - working file PROOF.md (not published) (N4-385), 7239770df00ff938
  - working file PROOF_v02.md (not published) (N4-386), 2ce3839dd7db7d2c
  - working file DISTANCE_PROOF_v02.md (not published) (N4-387), 1dc8284fc54d24ed
  - working file PROOF.md (not published) (N4-388), 56ddc0b28ea714de
  - working file PROOF.md (not published) (N4-389), 55765490eb36dd9d
  - working file PROOF.md (not published) (N4-390), 5ff46adee1191da1
  - working file PROOF.md (not published) (N4-391), 1bca5f408ed60fc2
  - working file PROOF_v02.md (not published) (N4-393), 20f14eeb4b85aa86
  - working file PROOF.md (not published) (N4-394), 1ec0c69865d0408f
  - working file PROOF.md (not published) (N4-395), 8f226a5f1774418f
  - working file PROOF.md (not published) (N4-396), 4a98af09dd96e924
  - working file PROOF.md (not published) (N4-397), bb8e14dd1f9908fb
  - working file T2_to_T1_v01.md (not published) (the T2 theory worker handoff (through section BM)), 048db91f739d49a7
  - working file the review of T4-402 (not published) (the T2 theory worker review of T4-402 (accepted in T4-413)), ffb49200aa127790
  - working file the review of T4-410 (not published) (the T2 theory worker review of T4-410 at the campaign radii (T4-421)), df28b508a9ba2da4
  - working file the review of T4-414 (not published) (the T2 theory worker review of T4-414 (restored 12:30:37Z; accepted in T4-423)), 221b113543dc8153
  - working file the review of T4-415 (not published) (the T2 theory worker review of T4-415 and T4-422 (accepted in T4-434)), ee7b1b1b7d9bc92c
  - working file the T2 falsification review of the endpoint and the report summary (not published) (the T2 theory worker falsification check of THEORY_FINAL draft 36 (revision 2;
    revision 1 audited in T4-443)), 660b089b8e643506
  - working file CHECK_T1_v08_FACTORS.md (not published) (the T2 theory worker check of the section 1 factors (revision 2)), 09e274f641119b9b
  - working file the T2 falsification review of the endpoint and the report summary_NOTE_BE.md (not published) (the T2 theory worker FALSIFY revision 3 note (handoff BI; T4-464)),
    de58845366cdfa39
  - working file the review of T4-459 (not published) (the T2 theory worker review of T4-459 (accepted in T4-462)), e140e6c03aa2ec44
  - working file the review of T4-458 (not published) (the T2 theory worker review of T4-458 (accepted in T4-465)), ca936460537bea92
  - working file the review of T4-462 (not published) (the T2 theory worker review of T4-462 (handoff BM)), 2cb6f7e6aaf78a3f
  - working file team notes (not published) (the coordinator notes (read through the 15:27Z note)), ea27c926dd2795d0
  - working file THEORY_FINAL.md (not published) (THEORY_FINAL draft 52), 82b4d9db1e5e25af
  - working file team note 47 (not published) (the T1/T3 theory worker team note v47 (the theory_v08 consultation)), 1633cd35948398bc
  - working file v08_factors_007.py (not published) (section 1 factors (revision 2)), 2615c95aeb72c0cc
  - working file v08_factors_007.out (not published) (its output), 4ad9ac5a12f18621
  - working file team note 51 (not published) (the T1/T3 theory worker team note v51 (theory_v08 window; numerics_v14 ACK)), 2db9ca22e2c15cdb
  - working file h18_verdicts.py (not published) (H18 verdict and scope check), e941a118de7f2e65
  - working file h18_verdicts.out (not published) (its output (draft 52, matrix v140 copy)), b8facf4cbad2a03e
  - working file check_T4458.py (not published) (R1-046, review of T4-458), cb7eec586031b571
  - working file check_T4458.out (not published) (its output), 8748b2950df75bd8
  - working file check_T4462.py (not published) (R1-047, review of T4-462), 6d8b95ec45526c1a
  - working file check_T4462.out (not published) (its output), c7cb5657de235ba3
  - The T1/T3 theory worker reviews review set 41 93b48e74, review set 42 f4c2e327, review set 43 dcd62d66, review set 44 1b7c425c, review set 45
    b8771fb6
- Supersedes: theory_v07 (2026-10-29T11:20Z, sha256 42eb222a38caadac911cffc261287892a9f18f60888f211f3e028f560508b320),
  which superseded theory_v01 to theory_v06. Every ID of theory_v01 to theory_v07 keeps its definition. Statements
  replaced in sections 2 and 8 are replaced by the forms given there. Entries of theory_v01 to theory_v07 that are not
  restated are unchanged.
- IDs: new in theory_v08 is NC-T-TWO-WEIGHT (section 5). The row labels D1 to K3 and N1 to N5 of section 1 are labels
  of this file only, not registered IDs. Used: all IDs of theory_v01 to theory_v07, in particular NC-T-DIST,
  NC-T-ORIGIN-INV, NC-T-UNIV-E, NC-T-ENDPT-Y and NC-T-SCREEN.
- Sector convention: as theory_v07 (header). A sector is r^e E(theta) with e = 1 - l delta - 2q, delta = 1 - gamma,
  indexed (l, q), l >= 1, q >= 0.
- Constants used throughout: c = 4076476460239181/2251799813685248, gamma = 1/c, q* = gamma - 4 (written q in sections
  1 and 5), delta = 1 - gamma = 0.44764..., kappa = 4 + delta, D = c kappa = 5c - 1.
- Candidate IDs referred to: those of theory_v07, C1-N1-024-rulem32-legqs25 (024, registered 11:31:32Z; a rule control
  of 016 with the objective on the MID 32 radial rule) and C1-N1-025-combined-heldin1e16 (025, registered 12:50:59Z; a
  combined basis with weighted mid-field rows, a sensitivity run for the 021 question) and
  C1-N1-026-heldin1e16-legqs25-m16to23 (026, registered 13:12:37Z; the 022 state continued with the 81 rows of 025) and
  C1-N1-027-cont60-legqs25-m16to23 (027, registered 14:13:51Z; the control for 026, the 022 state continued with the
  plain 67 rows of 016; INDEX).
- Status labels: as theory_v07. A the T4 theory auditor proof is AUDITED only after a the T1/T3 theory worker or the T2 theory worker review accepted by the T4 theory auditor; the
  review that made each entry AUDITED is named next to it.

## 0. Summary

0. Changes since theory_v07. The three statements of theory_v07 that T4-412 qualifies are repaired (section 2). 023 to
   026 are RULED OUT in every registered scalar ball and original graded box; separately, FW-T-DYADIC-Y-v1 is RULED OUT
   at 015 and 016 (section 4). The profile-specific endpoint coefficients 583/1000 (T4-402) and 93/250 (T4-415), the
   explicit finite-radius remainder of T4-410 and its radius average (T4-425) are AUDITED, and together they block the
   endpoint route with the present tail input at the four targets of T4-425 (the fixed sharpw ball and the sharpw, TB
   and graded ceilings; NC-T-TWO-WEIGHT, section 5). A valid universal velocity constant below 1.747261 exists (T4-411).
1. No closure. No registered framework is shown to close for any candidate, and no exact solution near any candidate has
   been shown to exist. Every snapshot C1-N1-002 to C1-N1-026 except 011 (a FLOAT comparison) has no exact solution at
   its reference c in any registered scalar ball or original graded box with a positive top-row budget (closure matrix
   v140 (2026-10-29T15:22Z); for 002, 003 and 004 outside the specified balls of rows 36, 40 and 42 because the fixed-c
   L^2 distances above 1.56361352, 0.22988134 and 1.40009623 (N4-069, N4-070, CONFIRMED by T4-068) exceed the L^2 radius
   of every registered scalar ball, below 2.7e-6, and of every graded box with a positive top-row budget, below 1/2000
   (T4-070, row 55)). In the matrix, C1-N1-001 is RULED OUT only as framework inapplicability: its residual is not in
   the forcing space (row 35). The exclusion of exact solutions near 001 in the affine class rho + L^2, at every c and
   every radius, is the T4 theory auditor's annular application T4-458, CONFIRMED by the T1/T3 theory worker's review R1-046 (review set 44) and the T2 theory worker's
   the review of T4-458, both accepted in T4-465 (section 4); it does not cover FW-T-DYADIC-Y-v1 or weighted or non-L^2
   repairs. For 026, the N4 numerical auditor's own package (N4-366 to N4-369) is reproduced independently by the T4 theory auditor in T4-446 to T4-450
   (13:45Z), and the N4 numerical auditor accepts the reproductions in N4-377 to N4-379 (13:55Z; section 4).
2. Section 1 lists 24 tests that specified certificates for 007 need and fail, with the factor by which each fails. They
   are not all the inequalities needed for existence, and a different certificate need not meet them (T4-437). Every
   factor is a proved lower bound of the ratio of the 007 quantity to the threshold (exact rational arithmetic in the T1/T3 theory worker
   artifacts/checks/v08_factors_007.py). Rows D1 to D5 are exclusions of 007 in the stated balls, not only failures of a
   certificate (NC-T-DIST): every real S1 correction h in L^2 with F(rho + h; c) = 0 has ||h||_2 > 0.004769166867, at
   least 1257.36 times the largest scalar family ceiling and 10.4318 times the graded one. The smallest factors, 1.0101
   (U1 and A1, the endpoint velocity constant against the fixed sharpw ball), belong to a route that fails further rows
   (R1 to R3, K1 to K3), so a small factor does not mean a route is nearly closed. Five open items have no factor
   (section 1.4).
3. Endpoint route (section 5). For 007, 013 and 014 the T4-351 closure inequality fails at the four targets (fixed
   sharpw ball, sharpw, TB and graded ceilings) with every universal velocity constant (NC-T-UNIV-E; by section 2 (g) it
   also holds at every registered radius at or above 1.421e-7, and at 2^-23 with V >= |U_lead(0)|, while at the FW-A2-Db
   radii 2^-25 and 6.8626e-8 only NC-T-DIST excludes these candidates), with the profile limit 583/1000 at every target,
   with 93/250 at the graded target, and with every finite-radius remainder of the T4-410 type built on the proved tail
   bound T4-335 (7), whether used with a constant, radius-dependent or outer-only coefficient (NC-T-TWO-WEIGHT). The
   missing input is a tail bound for stationary corrections whose exponents gain well over delta on r^q, or a velocity
   or H_q estimate that uses stationarity. None is proved or disproved. This is a statement about the present
   certificates, not a nonexistence result.
4. Final requests (section 6): no new candidate is requested for the present frameworks. A new candidate can enter a
   registered scalar ball or original graded box only if none of its certified distance lower bounds exceeds that
   ceiling, and these ceilings are more than 10.4318 times (graded) and 1257.36 times (scalar) smaller than the proved
   floor of 007 at the same c; this is necessary, not sufficient. These ceilings do not bound the radius of an untested
   dyadic or localized framework. A new input of section 1.4 or 5 (e) would change more than a new candidate.

## 1. Failed tests for specified certificates at 007, with factors, and open items

### 1.1 Reading rules

- Each row is an inequality Q < T that a specified certificate needs; its failure rejects that certificate or that
  choice of estimate only (T4-437). Scopes by group: rows D1 to D5 exclude the stated correction balls under the
  hypotheses of the weak identity, and do not exclude larger or different balls (NC-T-DIST); rows S fail sufficient norm
  tests; O1 is the accepted origin inverse test with all hypotheses of FW-T-DYADIC-Y-v1; rows U concern a universal
  weighted C^1 estimate, not every estimate that uses stationarity; P1 and P3 to P5 use the chosen proved upper
  coefficients 93/250 and 583/1000 and reject those choices in the stated cap formula, so they are not lower bounds on
  every admissible coefficient, while P2 is the lower obstruction for the N/G angular inequality on the whole span; rows
  R compare a specified error majorant with its room and do not bound the actual error; A1 uses the whole majorant class
  of T4-425 and the positive delta term of the tail list; rows K use hypothetical necessary thresholds in the optimistic
  outer-only model, and the lower bound lambda > 109.6024 holds for the present bracket only, not for every kernel
  estimate.
- p is a proved lower bound for the quantity Q at 007, and t is a proved upper bound for the threshold T, both as the
  cited sources print them, rounded outward. The factor printed is p/t rounded down at the displayed precision, 10^(-k)
  floor(10^k p/t) with k = 4 (k = 2 for ratios of 100 or more). Since p <= Q and T <= t, the true ratio Q/T is at least
  the factor; a factor above 1 means the inequality fails for 007.
- Targets. The fixed sharpw ball is the exact radius 1351/1024000000. At the ceilings, t is evaluated at the printed
  rational targets 28496/10^10 (sharpw), 3793/10^9 (TB) and 25/54684 (graded), which are the exact targets of T4-425 and
  T4-414. The exact ceilings are below these targets (BE1), and a smaller radius has a larger threshold. At the exact
  graded ceiling 50/(651 sqrt 28248) < 25/54684 (theory_v04) rows U4, P1 and P2 are at least 2.9432, 2.0544 and 2.0515
  (the T2 theory worker CHECK_T1_v08_FACTORS revisions 1 and 2, handoff BB2; CONFIRMED by the T4 theory auditor T4-455). For the sharpw and TB family
  ceilings, the T2 theory worker handoff BE1 (section stamp 14:00Z; Arb at 256 bits; AUDITED: CONFIRMED by the T4 theory auditor T4-454 with exact
  rational comparisons of squares) evaluates the theory_v03 formula and finds 28495/10^10 < sharpw ceiling < 28496/10^10
  and 37929/10^10 < TB-sharp ceiling < 37930/10^10, so each printed ceiling is the exact one rounded up at the printed
  digit. With this bracket R2 and R3 are at least 46.0752 and 66.5677 at the exact ceilings, and U2, U3, P4 and P5 hold
  there as printed (the T2 theory worker BB2, BE2 and CHECK_T1_v08_FACTORS revision 2; CONFIRMED by the T4 theory auditor T4-455, which rebuilds the
  endpoint coefficients of 007, 013 and 014 from the exact endpoint data and uses the T4-454 brackets). K2 and K3 are
  not evaluated below the printed targets. Rows D are not affected, since their t is an upper bound of the radius. Every
  row still fails.
- Rows R1 to R3 use the room with H >= Phi(theta*) (T4-380), as T4-414 does. With only H >= H0 they are at least
  22.1948, 46.0750 and 66.5674 (the T2 theory worker BA4; CONFIRMED by the T4 theory auditor T4-455).
- Arithmetic: The T1/T3 theory worker artifacts/checks/v08_factors_007.py, exact fractions, no FLOAT step; output
  artifacts/checks/v08_factors_007.out (listed in artifacts/README.md; revision 2, which corrects S2 after T4-437). The
  sources of p and t are the cited proofs; the script only divides them. T4-437 checked every numerator and threshold
  direction against the accepted containing balls and every quotient independently at 512 bits.
- Rows of different groups belong to different certificates and are not comparable. A specified certificate succeeds
  only if every row of its group is reversed and every item of section 1.4 that it uses is resolved.
- Rows U use thresholds that bound those of 007, 013 and 014 together (the largest of the three, the T2 theory worker handoff AU3 and
  T4-404; T4-380 (3)), so they fail for all three. Rows P, R, A and K use the 007 values of the cited sources; their
  factors at 013 and 014 are not computed here. NC-T-TWO-WEIGHT itself holds for all three (section 5 (d)).

### 1.2 Table

| row | inequality needed (certificate) | p, lower bound at 007 (source) | t, upper bound (source) | factor >= |
|---|---|---|---|---|
| D1 | L^2 distance < TB-sharp family ceiling | 0.004769166867 (T4-185) | 3.7930e-6 | 1257.36 |
| D2 | L^2 distance < sharpw family ceiling | 0.004769166867 | 2.8496e-6 | 1673.62 |
| D3 | L^2 distance < sharp family ceiling | 0.004769166867 | 3.0927e-6 | 1542.07 |
| D4 | L^2 distance < fixed sharpw ball radius | 0.004769166867 | 1351/1024000000 (T4-262) | 3614.82 |
| D5 | L^2 distance < graded ceiling | 0.004769166867 | 25/54684 (T4-277) | 10.4318 |
| S1 | :H6, X_(s,w)(F) <= eta, sharpw | 756.5312630768 (N4-180, T4-238) | 2.1035e-4 | 3596535.59 |
| S2 | :H6, X_(s,w)(F) <= eta, sharp | 516.9717852723 (N4-180, T4-238, T4-437) | 7.6219e-5 | 6782715.40 |
| O1 | NC-T-ORIGIN-INV criterion on the seven cells | 1.23427738878510651005 (T4-147) | 1 | 1.2342 |
| U1 | universal E < Ecrit, fixed sharpw ball | 0.793036506422514088 (T4-381) | 0.785064 (T4-380) | 1.0101 |
| U2 | universal E < Ecrit, sharpw ceiling | 0.793036506422514088 | 0.6819391 (T4-404) | 1.1629 |
| U3 | universal E < Ecrit, TB ceiling | 0.793036506422514088 | 0.6471910 (T4-404) | 1.2253 |
| U4 | universal E < Ecrit, graded ceiling | 0.793036506422514088 | 0.2694314 (T4-404) | 2.9433 |
| P1 | profile limit 93/250 < Ecrit_prof, graded | 93/250 (T4-415) | 0.1810598671 (RT415 s6) | 2.0545 |
| P2 | any E with N <= E G on the span < Ecrit_prof, graded | 0.3714757 (RT415 s4) | 0.1810598671 | 2.0516 |
| P3 | profile limit 583/1000 < Ecrit_prof, fixed sharpw | 583/1000 (T4-402) | 0.5275684020 (RT415 s6) | 1.1050 |
| P4 | profile limit 583/1000 < Ecrit_prof, sharpw | 583/1000 | 0.4582680410 (RT415 s6) | 1.2721 |
| P5 | profile limit 583/1000 < Ecrit_prof, TB | 583/1000 | 0.4349170868 (RT415 s6) | 1.3404 |
| R1 | remainder J/H < room left by 93/250, fixed sharpw | 3.452825 (RT415 s7) | 0.1555681 (RT415 s6) | 22.1949 |
| R2 | remainder J/H < room left by 93/250, sharpw | 3.974970 (RT415 s7) | 0.08626771 (RT415 s6) | 46.0771 |
| R3 | remainder J/H < room left by 93/250, TB | 4.188388 (RT415 s7) | 0.06291677 (RT415 s6) | 66.5702 |
| A1 | radius average Eeff(r) < Kcrit/Phi, r <= r_beta | 0.79303 (T4-425 (7)) | 0.785064 (T4-425 (7)) | 1.0101 |
| K1 | kernel constant Lam < threshold, fixed sharpw | 109.6024 (T4-425 s2) | 14.41 (R1-044 s3 (c)) | 7.6059 |
| K2 | kernel constant Lam < threshold, sharpw | 109.6024 | 8.647 (R1-044 s3 (c)) | 12.6751 |
| K3 | kernel constant Lam < threshold, TB | 109.6024 | 7.287 (R1-044 s3 (c)) | 15.0408 |

RT415 is the T2 theory worker the review of T4-415 (sha256 prefix ee7b1b1b, accepted in T4-434). An empty source cell repeats the source of
the row above.

### 1.3 Statements of the rows

(D) NC-T-DIST (theory_v03; AUDITED). Quantity: the fixed-c L^2 distance from rho_007 to the set of exact S1 solutions,
over real S1 corrections h in L^2 with F(rho_007 + h; c) = 0. Proved: every such h has ||h||_2 > 0.004769166867 (T4-185,
AUDITED by the T1/T3 theory worker R1-022, number CONFIRMED by N4-157). Thresholds: the L^2 radius of every admissible ball of
FW-T-TB-sharp-v1, FW-T-T4L2-sharpw-v1 and FW-T-T4L2-sharp-v1 is at most the universal family ceiling 3.7930e-6,
2.8496e-6 and 3.0927e-6 respectively (theory_v03 section 6 and THEORY_FINAL section 6, AUDITED); the fixed sharpw ball
of THEORY_FINAL section 2.1 has L^2 radius r/sqrt(w2) = 1351/1024000000 (T4-262); a graded box of the T4-277 type has
L^2 radius below 25/54684. A ball whose L^2 radius is below the distance contains no exact solution, so these rows are
exclusions of 007 in the stated balls, not only failures of a certificate.

(S) :H6 of FW-T-T4L2-sharpw-v1 and FW-T-T4L2-sharp-v1 (THEORY_FINAL section 2.1, AUDITED conditional through T4-042 and
R1-006). Quantity: X_(s,w)(F), F = F(rho_007; c), in NORM-T-Xw5184-v1 = XSW[1/5184, 2^15, 2^20] and NORM-T-X7744-v1 =
XSW[1/7744, 2^14, 2^18]. Proved: X_(s,w)(F) > 756.5312630768 in NORM-T-Xw5184-v1 and X_(s,w)(F) > 516.9717852723 in
NORM-T-X7744-v1, the lower comparisons (1 - 48 s/25) E_w(F) <= X_(s,w)(F) with the complete components (the N3 numerics worker, CONFIRMED
in N4-180 and N4-181, accepted in T4-238; the sharp value is checked in T4-437, which REFUTES the use of 756.5312630768
for the sharp norm in team note v47, since the sharp upper comparison is below 517.5527701453). Thresholds: eta =
4207/(2 10^7) = 2.1035e-4 and 76219/10^9 = 7.6219e-5.

(O1) NC-T-ORIGIN-INV for FW-T-DYADIC-Y-v1 (T4-146, AUDITED through the T1/T3 theory worker R1-017). Under the hypotheses of the origin
inverse theorem (0 < s < c - 1, M >= 1/(c - 1 - s), beta <= 1 + c - c a, C_U >= 1, and the realization, canonical
velocity, dyadic partition, plateau and absorption hypotheses of T4-146), a certificate at the window parameter a with
0 < a < 1 + 1/c needs
  5^((a-2)/2) N_a(F) < H(c - 1) (1 + c - c a)/(1 + a),  N_a(F) = ||(1 + r^2)^((2-a)/2) Delta F||_2,
  H(d) = max over 0 < s < d of (d - s) sqrt(4 pi s (1 + s)).
Proved for 007: on the seven cells [0, 1/4], [1/4, 1/2], [1/2, 3/4], [3/4, 1], [1, 5/4], [5/4, 3/2] and [3/2, 1 + 1/c]
the ratio of the left side (lower bound from angular modes 1 and 3 alone) to the right side (upper bound with H(c -
1) <= 57/50) is at least 1.23427738878510651005, the minimum, on [0, 1/4] (T4-147, AUDITED through R1-017, independently
reproduced by the N4 numerical auditor in N4-128 and N4-129 and accepted in T4-150; the T1/T3 theory worker artifacts/checks/check_T4146.py). For 1 + 1/c <=
a < 2 the audited nonpositive far-field rate excludes the scheme separately (NC-T-WRATE).

(U) NC-T-UNIV-E (theory_v07 section 5.7; AUDITED). Quantity: a constant E valid in the universal far-field velocity
estimate T4-335 (1) on the whole S1 norm class. Proved: every valid E satisfies E >= Emin = (-q-1)/[2(-q)(-q-3)] =
0.793036506422514088... (T4-381, AUDITED through the T1/T3 theory worker R1-040 and T4-391; it persists on the full fractional ball of
X_(s,w) with any prescribed H_q, T4-397, AUDITED through R1-042 and T4-409). Thresholds: the T4-351 closure inequality
reaches the target only if E < Ecrit, with Ecrit < 0.785064 at the fixed sharpw ball (T4-380 (3), digits repaired in
T4-424) and Ecrit <= 0.6819391, 0.6471910 and 0.2694314 at the sharpw, TB and graded ceilings (the T2 theory worker handoff AU3, the
common cap over 007, 013 and 014, T4-404). The best valid constant lies in [Emin, 1.747261] (T4-411). Neither T4-381 nor
T4-397 bounds an estimate that uses stationarity or the tail class (T4-437). The rows concern the four targets; the
scope of NC-T-UNIV-E at the other registered radii is section 2 (g).

(P) Profile-specific limit coefficients (section 5). Quantity: a coefficient Eprof with |U[h] + DK M[h]| <= (Eprof +
o(1)) H s^q as s tends to infinity on the endpoint spans of 007. Here DK is the derivative of the velocity kernel K (not
a product with the scalar D = 5c - 1) and M[h] = integral X h(X) dX is the moment. Proved: Eprof = 583/1000 from the
mean gradient (T4-402, AUDITED through the T2 theory worker the review of T4-402 and T4-413) and Eprof = 93/250 from the pointwise inequality
N(z) <= (93/250) G(z) for all real z (T4-415, AUDITED through the review of T4-415 and T4-434). Every constant E with N(z) <= E
G(z) for all real z is at least 0.3714757 at 007 (the review of T4-415 section 4); this bounds the angular inequality on the
whole span only, and a stationary restriction on t or a larger independent lower bound on H could change the comparison
(T4-434 remark 1). Thresholds: with zero remainder and V = 0, the complete radial integral of the T4-351 test (T4-414
bound (2), AUDITED through the review of T4-414 and T4-423) reaches the target only if Eprof < Ecrit_prof, with Ecrit_prof <=
0.5275684020, 0.4582680410, 0.4349170868 and 0.1810598671 at 007 for the fixed sharpw ball and the sharpw, TB and graded
ceilings (the review of T4-415 section 6). 93/250 passes the first three (it is not a row) and fails the graded one. These
limits give no finite radius; rows R, A and K concern the finite-radius remainder.

(R) Finite-radius remainder with 93/250. Quantity: J(R)/H, the T4-410 bound on the compensated error r^(-q) |U[h] + DK
M[h] - r^q V_q[b]|/H at a starting radius R <= r_beta, with amplitude weight q - epsilon forced to epsilon <= delta by
the tail list T4-335 (7). Proved: J(R)/H >= 3.452825, 3.974970 and 4.188388 at the fixed sharpw, sharpw and TB targets
(the T2 theory worker the review of T4-410, main obstruction CONFIRMED in T4-421; values from the review of T4-415 section 7). Threshold:
the room Ecrit_prof - 93/250 with H >= Phi, at most 0.1555681, 0.08626771 and 0.06291677 (the review of T4-415 section 6). At
the graded ceiling the room is negative (at most -0.1909308), so no remainder helps. Starts R > r_beta are row A1.

(A1) Radius-dependent coefficients (T4-425, AUDITED through the T1/T3 theory worker R1-045 and T4-432). Premise: the tail list T4-335
(7) with its strictly positive term C_delta r^(q-delta), C_delta = H (V + E G)/D. Quantity: Eeff(r) = kappa r^kappa
times the integral of E(s) s^(-kappa-1) over (r, infinity), for any coefficient E(s) chosen from T4-410 estimates with
any R0 and epsilon, their envelopes and any norm-class universal constant. Proved: E(s) >= min(Emin, lambda (5/s)^delta)
for s >= 2, lambda = 1/2 + 5 2^(1-q), and Eeff(r) >= Emin [1 - delta/(kappa + delta) (r/r_u)^kappa] > 0.79303 for r <=
18860, r_u = 302748.40... Threshold: positivity of the CI integrand at R <= r <= r_beta needs Eeff(r) < (r/r_beta)^delta
Kcrit/Phi < 0.785064, and every r_beta is below 18860. With the outer amplitude alone the same holds with Eeff >
0.79303648 provided V >= 0, G >= g0 and E >= Emin (T4-432).

(K) Kernel constant (the T1/T3 theory worker R1-044 section 3 (c), CONFIRMED by T4-426 with repairs). Quantity: a constant Lam replacing
the bracket of T4-410 (2), C_a + L_a (1 + log_+(k s^epsilon)) >= lambda = 1/2 + 5 2^(1-q) = 109.60242254... > 109.6024
(T4-425 section 2; the equality "lambda = 109.6024" of THEORY_FINAL draft 38 is false, T4-442). Thresholds: with Eprof =
93/250 the CI needs Lam below 13.27 at the fixed sharpw ball (14.41 with the universal fallback; the row uses 14.41, so
its factor holds for both readings), 8.647 at the sharpw ceiling and 7.287 at the TB ceiling, with no room at the graded
ceiling. These thresholds are Arb upper bounds computed with deliberately optimistic inputs (Eprof = 93/250, the
outer-only amplitude, the allowed relaxed fallback); they are necessary only in this model, passing them would not prove
closure, and lambda is a lower bound for the present bracket only, not for every kernel estimate (T4-437). A smaller Lam
alone does not remove the delta exponent, since the coefficient contains H V/D (T4-426).

### 1.4 Unresolved items without a factor

- N1. Inverse hypotheses. :H1 (A) (far-field decay of D^j rho, j <= 2), the A2 (B0n) list, :H3 (M1 >= (9/10) I, M2 >=
  (1/2) I, (B4), (B5), (B7)) and :H4 (the (B9c) component sums) are not checked for 007 (closure matrix row 56). They
  matter only for a reference that passes rows D and S.
- N2. Localized orbit-weight route (the T2 theory worker note on the localized (B-L2) margin, THEORY_FINAL section 2.7; ingredients, no
  framework). Its admissible radius must exceed 0.004769166867 at 007 by norm domination with constant 1 (T4-219,
  T4-260). No upper ceiling on that radius is proved and no radius is certified, so there is no factor.
- N3. Route T-E (THEORY_FINAL section 8.2). No framework is constructed. Its four requirements (a subcritical
  remainder, a continuous normalization, an inverse that respects T4-124, Lipschitz bounds) are unmet.
- N4. A priori bound. No upper bound on H_q(h) for stationary corrections h is proved. The proved lower bound is
  H_q(h) > 999745 for every stationary correction of the three-times repaired 007, 013 and 014 references with finite
  H_q (T4-380), so a framework in a norm Y >= H_q needs a radius above 999745 (NC-T-ENDPT-Y).
- N5. Tail exponent. A remainder of the T4-410 type becomes small only with a tail bound for stationary corrections
  whose exponents gain well over delta = 0.44764... on r^q; the FLOAT estimate of the review of T4-410 puts the needed
  gain near 1.05. The only proved list, T4-335 (7), contains the exponent q - delta itself. The threshold is FLOAT and
  specific to that model, not a universal necessary exponent; a new remainder argument could change it (T4-437). No
  factor is given.

## 2. Repairs of theory_v07

The audit of the published theory_v07 (T4-412, research/published_v07_audit, PROOF 5720a3c0...) CONFIRMS its
mathematical statements and asks for three repairs; the N4 numerical auditor found the same three points (N4-335). theory_v07 itself is
not edited. Each repair below replaces the cited sentence; no number or verdict changes.

- (a) Section 2.1, entry T4-369: "the binding of the actual 022 coefficients to this family is not yet checked" is
  replaced by: the binding is checked (N4-321, CONFIRMED by T4-403 and accepted in N4-331).
- (b) Section 5.6 (e): hypothesis (P) and tau for 022 against 016 are the N4 numerical auditor's own computation in N4-325, whose
  independent replay is OPEN; the separate direct exclusion of 022 in every registered scalar ball and original graded
  box is AUDITED (T4-405 to T4-408, accepted in N4-333 and N4-334).
- (c) Section 5.6 (d): "every registered snapshot" is replaced by "every snapshot with a certified distance floor in
  the cited table"; 011 has a FLOAT value only, and 023 was untested when theory_v07 was published.

Three statements of theory_v07 are superseded by later results, not repaired:

- (d) Sections 2.1 and 2.3: the folded-kernel upper constant E <= 1.749109 of the T2 theory worker the review of T4-375 R3 "awaits a
  separate audit". T4-411 (research/folded_velocity_upper_audit) CONFIRMS it with its own certificate E < 1.747261,
  valid for every nonzero X under its exact hypotheses (central oddness, C^1, finite H_q). So a valid universal
  constant below 1.747261 exists, and the best universal constant lies in [Emin, 1.747261].
- (e) Section 3, 016: the whole-plane G0 in [0.30888644514252473677, 0.30888644514252473678] was a the N3 numerics worker report; it is
  CONFIRMED by the N4 numerical auditor's independent production (N4-341), so the smallest CONFIRMED G0 is that of 016, not 007
  (0.37668932, N4-139). It changes no verdict, since 016 is RULED OUT in every registered scalar ball and original
  graded box by its distance.
- (f) Sections 0 and 3: "C1-N1-023 is untested" is replaced by section 4 below (023 RULED OUT, v122).

One statement of theory_v07 is too broad and is narrowed here (the T2 theory worker reviews/the T2 falsification review of the endpoint and the report summary, revision 2
of 13:42Z, sha256 prefix 660b089b, which makes the five wording repairs of T4-443; revisions 0 and 1 of 13:10Z and
13:19Z (6eede464) have the same numbers; handoff AZ and BC):

- (g) NC-T-UNIV-E (header gloss "no universal velocity constant lets the endpoint closure inequality reach a registered
  radius" and section 5.7 "below every registered family ceiling"). The proof gives: for every constant valid in T4-335
  (1) and v0 = 0, the square root of the right side of (CI) is below 1.421e-7 with the radial shape (T4-381 (8),
  AUDITED). So (CI) reaches no registered L^2 radius at or above 1.421e-7. This cap is for one constant coefficient; for
  the radius-dependent coefficients of T4-425 with the floor Etest, H >= H0 and V = 0, the T2 theory worker bounds the whole CI value
  below 1.43912e-7 (section 2 (c) of the review), a different statement (T4-455). Three registered radii are below it:
  the FW-T-T4L2-trans-v1 fixed ball 2^-23 and the FW-A2-Db fixed ball 2^-25 and family ceiling 6.8626e-8 (theory_v03
  section 6, theory_v04). The argument says nothing there, and NC-T-UNIV-E is withdrawn at these three radii. The T2 theory worker
  finds, and the T4 theory auditor confirms independently (T4-443, 948 checks at 768 bits), that the obstruction holds at 2^-23 under
  the T4-414 hypothesis V >= |U_lead(0)| = 0.99148... (with H >= Phi the whole CI value is below 1.14141e-7), that at
  2^-25 and 6.8626e-8 the T4-414 thresholds are at least 1.020385 and 0.8711127, above Emin, and that the current list
  with the floor min(1.747261, lambda (5/s)^delta) reaches none of the thirteen printed targets (whole CI value below
  2.66323e-8 < 2^-25). At 2^-25 and 6.8626e-8 the obstruction for an improved universal constant is OPEN, not false:
  Emin is a lower bound on valid constants, not a proved admissible constant, so a threshold above Emin shows no valid
  constant that passes (T4-443 repairs 1 and 2). The T1/T3 theory worker checked in FLOAT that the V = 0 thresholds scale as
  beta^(-delta/(-q-1)), which reproduces the T2 theory worker's 1.570143 (crude) and 1.055202 (retained shape) at 2^-25 from the fixed
  sharpw values. This narrows a necessary condition on one certificate and changes no exclusion: 007 is excluded from
  these balls by NC-T-DIST, since 0.004769166867 > 6.8626e-8.

## 3. Status changes since theory_v07

### 3.1 the T4 theory auditor entries T4-409 to T4-469

- T4-409: accepts the T1/T3 theory worker R1-042, so T4-397 (the universal lower bound E >= Emin on the full fractional ball with any
  prescribed H_q) is AUDITED.
- T4-410 (research/two_weight_velocity_remainder): an explicit finite-radius bound for the compensated velocity of a
  centrally odd C^1 remainder with amplitude weight a and gradient weight q, -5 < a < -3, a < q < 0. CONFIRMED by
  the T1/T3 theory worker R1-043 and accepted in T4-424, so AUDITED, with the outward digit repairs 0.785064 for 0.785063, the radii
  3.16e7, 1.15e7, 4.29e7 and 8.69e7, and lam2 >= 1195.78.
- T4-411: CONFIRMED folded-kernel bound, E < 1.747261 (item (d) of section 2).
- T4-412: audit of the published theory_v07 (section 2).
- T4-413: accepts the T2 theory worker the review of T4-402, so T4-402 (the profile limit 583/1000) is AUDITED. The cutoff-radius rooms of
  that review are necessary, not sufficient, for the complete radial integral.
- T4-414 (research/profile_velocity_shape_cap): with 583/1000, V = 0 and zero remainder the complete radial integral of
  the T4-351 test reaches at most 7.643e-7 at 007, 013 and 014, and reaching the targets needs a coefficient below
  0.527596, 0.458292, 0.434940 and 0.181070. Accepted with the T2 theory worker the review of T4-414 in T4-423, so AUDITED.
- T4-415 (research/pointwise_profile_velocity): on each endpoint span of 007, 013 and 014, sup |V_q[f]| <= (93/250) sup
  sqrt(q^2 f^2 + (f')^2). AUDITED through the T2 theory worker the review of T4-415 and T4-434. T4-434 adds that the lower bounds 0.3714757,
  0.3714938 and 0.3715026 concern the angular inequality, not every stronger stationary estimate.
- T4-416 to T4-420: independent reproduction of the 023 structure, point gaps, origin, prefix and distance, accepted
  by the N4 numerical auditor in N4-348 to N4-350 (section 4).
- T4-421: CONFIRMS the main obstruction of the T2 theory worker the review of T4-410 with all 180 finite checks (at sharpw J/H >=
  3.974970, 3.974957, 3.974975) and REFUTES its side assertion that a certificate must start at R <= r_grad: only
  max(R, r_grad) <= r_beta is necessary.
- T4-422: the complete radial integral with 93/250, V = 0 and zero remainder has caps about 8.914e-6, which pass the
  three scalar necessary thresholds and not the graded one. AUDITED through the review of T4-415 and T4-434. This is a
  hypothetical ceiling, not a distance certificate.
- T4-423, T4-424: acceptances of the review of T4-414 and of the T1/T3 theory worker R1-043 (above).
- T4-425 (research/radial_averaged_remainder_obstruction): radius-dependent coefficients spliced with any norm-class
  universal constant do not rescue the T4-410 remainder (row A1 of section 1). AUDITED through the T1/T3 theory worker R1-045 and T4-432.
- T4-426: CONFIRMS the T1/T3 theory worker R1-044 (the outer amplitude bound R44.1 and the kernel thresholds of rows K1 to K3) with
  repairs: the printed bound ">= 0.7930" is false (the smallest value is about 0.79299998591), 0.793 is a relaxed
  value, not an admissible universal coefficient, and the coefficient contains H V/D, so a smaller velocity constant
  alone does not remove the delta exponent.
- T4-427 to T4-431: independent reproduction of the 024 structure, point gaps, origin, prefix and distance, accepted
  by the N4 numerical auditor in N4-357 to N4-359 (section 4). T4-427 REFUTES a one-variable reading of 024 against 016 (the radial rule
  and the backend both changed).
- T4-432: accepts the T1/T3 theory worker R1-045, so T4-425 is AUDITED; it extends the conclusion to any majorant that keeps the outer
  amplitude alone, with averaged floor above 0.79303648 at each r_beta, under the list hypothesis V >= 0, G >= g0 and
  universal coefficient >= Emin.
- T4-433 (research/theory_final_draft34_audit): CONFIRMS the changed mathematics of THEORY_FINAL draft 34 (79 checks)
  with eight status and wording repairs, all made in draft 37; the unrestricted reading of the 1.72 illustration stays
  OPEN (its fixed-fallback calculation does not prove it).
- T4-434: accepts the review of T4-415 (78336 rectangles at 384 bits, 24576 denominator cells, 341 checks).
- T4-435: REFUTES the blanket FLOAT ranges and the all-MID16 label of numerics_v12, CONFIRMS its corrected internal
  comparisons and witness factors; reporting repairs only, no exclusion changes (section R5).
- T4-436: CONFIRMS the 025 dimension 2918 and its 81-row analytic objective (10^12 weight on 67 rows, 10^16 on 14),
  with all 46 diagnostic probes outside the objective span; REFUTES the completeness of the two manifest descriptions
  (both stop at "at weight " and omit 10^16). No norm or distance result. Accepted by the N4 numerical auditor in N4-365.
- T4-437 (research/theory_v08_factors_audit): audit of the factor table of team note v47 (114 checks, 512 bits). REFUTES
  the S2 numerator (756.5312630768 is the sharpw value; the sharp norm satisfies 516.9717852723 < X < 517.5527701453)
  and the global reading of the 24 rows as necessary for every closure proof; CONFIRMS the corrected 24 comparisons
  within the scopes now stated in section 1.1. Section 1 includes all its repairs.
- T4-438 to T4-441 (research/candidate025_point, candidate025_origin, candidate025_sectors, candidate025_weak):
  independent reproduction of the N4 numerical auditor's 025 point gaps, origin normalization, complete prefix and distance floor (section
  4); accepted by the N4 numerical auditor in N4-370 and N4-371.
- T4-453 (research/theory_final_draft39_audit; 14:02Z, team note 227; 237 checks at 768 bits): audit of THEORY_FINAL
  draft 39 (13:47Z, 28f5f6ce...). CONFIRMS its changed conditional mathematics, the exact sharpw rate 63092119/405000000
  and slack 7/1557000000, its 22 numeric table rows, the six 007/013/014 factors above 28895 at the two small FW-A2-Db
  targets, lambda and the projected norm 13.75867597; REFUTES as current status its 026 OPEN entries (repaired in drafts
  40 and 41). Its three updates are made in draft 42: T4-451 is cited with N4-374, the accepted 016 components G0, rF
  and G1 are separated from P2 and the actual H, section 0 displays the normalized condition E sqrt(2 pi) H_max/B <
  Emax(b) of R1-038, and the section 0 summary of T4-425 is limited to its four targets.
- T4-452 (research/endpoint_falsification_repairs; 13:56Z, team note 226; 107 checks at 768 bits): CONFIRMS the five
  T4-443 repairs in the T2 theory worker the T2 falsification review of the endpoint and the report summary revision 2 (660b089b...) with the 13 numerical rows unchanged.
  With H_max >= 999745 the largest exact graded cutoff is 0.26945243670784104023856... (013), below 0.2694533 and below
  Emin. OPEN: whether an improved valid universal constant reaches 2^-25 or 6.8626e-8. T4-452 still treats the sharpw
  and TB one-unit brackets as conditional; the T2 theory worker BE evaluates them, and T4-454 CONFIRMS them (section 1.1).
- T4-454 (research/family_ceiling_brackets; 14:06Z, team note 228; 166 checks): independent audit of the T2 theory worker handoff BE.
  The six scalar family ceilings other than TB-rebal lie strictly in the one-unit brackets below their printed values,
  the graded ceiling lies in (45697/10^8, 25/54684), all seven scalar ceilings are below 3.7930e-6, and the TB-rebal
  ceiling 3.51254748112091806496...e-7 lies in (3.5125e-7, 3.5126e-7). CONFIRMED; REFUTES the old statement that
  3.5125e-7 is the TB-rebal ceiling rounded up. An upper bound of a cutoff that decreases with the radius persists at
  the exact TB-rebal radius; an old two-sided interval need not.
- T4-455 (research/theory_v08_preview2_audit; 14:12Z, team note 229; 415 checks at 768 bits): exact-file audit of
  preview2 (sha256 prefix 5940b948, 868 lines, 127 changed word blocks). The seven T4-445 repairs are made. CONFIRMS the
  changed mathematics in its stated certificate scopes, the 24 divisions at the printed targets, the nine new factors at
  the exact ceilings (U4, P1 and P2 at least 2.9432, 2.0544 and 2.0515; R2 and R3 at least 46.0752 and 66.5677 with H >=
  Phi) and the three factors with H >= H0 only (R1, R2 and R3 at least 22.1948, 46.0750 and 66.5674); the T2 theory worker bracket
  assumptions of BB2 and BE2 are discharged by T4-454. U2, U3, P4 and P5 keep their printed values, and K2 and K3 stay
  at the printed targets. It asks for three updates of the successor of preview2, made here: the reciprocal 026
  acceptance N4-377 to N4-379 (section 4), the citation of T4-451 and T4-454 (this section and section 1.1), and the
  TB-rebal upper ceiling 3.5126e-7 (T4-454 above; THEORY_FINAL section 11 item 75). It finds the constant-coefficient
  cap below 1.421e-7 and the cap below 1.43912e-7 of the radius-dependent class of T4-425 correctly kept apart (section
  2 (g)). It proves no existence, inverse or unrestricted nonexistence statement.
- T4-456 (research/theory_final_draft43_audit; 14:19Z, team note 230; 263 checks at 768 bits): audit of THEORY_FINAL
  draft 43 (14:09Z, a3b59ce9..., 48 changed word blocks against draft 39). CONFIRMS its changed mathematics, its 23
  distance-table rows (026: factors above 357.4, 475.8 and 2.965) and the T4-453 and T4-454 repairs: the reciprocal 026
  acceptance through N4-379, the normalized R1-038 condition E sqrt(2 pi) H_max/B < Emax(b), the TB-rebal upper ceiling
  3.5126e-7, the four-target scope of T4-425 and the separation of the accepted 016 components from the actual H. It is
  not the H18 falsification of the matrix, and N4-382 postdates it.
- T4-451 (research/candidate016_low_order_forcing_audit; 13:53Z, team note 225; 318 checks at 1024 bits): independent
  audit of N4-374. For F in H^1(R^2), s >= 0 and positive weights, X_(s,w)(F) > sqrt(w1 l1^2 + w2 l0^2) when ||F||_2 >
  l0 > 0 and ||DF||_2 > l1 > 0 (unitary Plancherel); with the accepted 016 G0 and G1 the ten registered scalar
  sufficient forcing tests fail (smallest ratio above 3542234, sharpw). CONFIRMED. This is a failed sufficient test, not
  a distance exclusion; P2 and the Hardy bound are unused and stay OPEN.
- T4-446 to T4-450 (research/candidate026_shapes, _point, _origin, _sectors, _weak; 13:45Z, team note 224): independent
  reproduction of 026: 2414 potential and density directions, the ordered 022 basis, with 81 objective rows and the 46
  probes outside their span (T4-446); F(1/10, 73/100) = 0.079901987643040288729..., graded gap
  0.059485034360572262525... and six positive scalar gaps (T4-447); c + strain = 1 exactly (T4-448); the sixteen-row
  prefix through -7/2 with nonzero labels (4, 1), (9, 0), (5, 1), (1, 2), (10, 0) (T4-449); and every correction under
  the weak fixed-c hypotheses has L^2 norm above 0.001355907204057457 (T4-450). CONFIRMED, agreeing with N4-366 to
  N4-369. No dyadic exclusion follows.
- T4-445 (research/theory_v08_preview1_audit; 333 checks): exact-file audit of preview1 (sha256 prefix d8c8e8ba, 769
  lines). CONFIRMS the 24 corrected factors and table cells, the three kernel threshold rows, the finite-radius bounds
  and the section 2 (g) distinction (the two smallest-radius universal-constant questions are OPEN, not false). Asks for
  seven scope repairs, made here: unrestricted "every registered ball" becomes "every registered scalar ball and
  original graded box" (sections 0, 3.2, 4); 025 opens with its RULED OUT status (section 4); the seven-cell test of
  section 6 item 2 is not promised a verdict; the ceilings of section 0 item 4 and section 6 item 5 belong to the scalar
  and original graded families, and rows S and N1 to the specified sharp and sharpw certificates; section 7 states what
  T4-443 has audited; errata 67 to 72 change no candidate exclusion; DK is defined on first use (section 1.3 (P)).
- T4-444 (research/candidate025_peer_acceptance; 392 checks): accepts N4-365, so the 025 structure result holds in both
  directions; REFUTES only the phrase "projection ... excluded" of the T4-436 JSON, which should read "initial
  projection ... excluded".
- T4-443 (research/finite_radius_reach_audit; 948 checks, 768 bits): CONFIRMS the whole-integral bound of the T2 theory worker
  the T2 falsification review of the endpoint and the report summary revision 1 section 2 (c) and its numerical displays; REFUTES the reading that a
  threshold above Emin disproves the universal obstruction (section 2 (g)).
- T4-442 (research/theory_final_draft38_audit; 548 checks, 512 bits): audit of THEORY_FINAL draft 38 (sha256 prefix
  ccaa8623). CONFIRMS the changed conditional mathematics and the 016 two-endpoint seven-cell implication (minimum ratio
  above 1.253908386497 under the full origin-inverse hypotheses); REFUTES the equality "lambda = 109.6024" (lambda =
  109.60242254... > 109.6024) and the lower inference "N_1 >= 13.758676 from modes 1 and 3", whose two-mode value is
  13.758675979450936... (so N_1 > 13.75867597); OPEN the unqualified bound lambda H (5/r)^delta of draft 38 section 9
  item 6 on r < 5. It asks for six repairs, listed as item 74 of section 8.

- T4-457 (research/historical_ratio_floor_audit; 14:22Z; 233 checks): exact floors of the ratio tables of the T2 theory worker's
  summary. CONFIRMS the T2 theory worker's counts (13 of 18 historical O3 factors and 8 of 12 C4 factors exceed the exact quotient by
  one displayed unit; the 15 current summary factors are exact floors; d2/sharpw is 1.03e5) and REFUTES the lower-factor
  reading of the 21 historical values; the graded d2 quotient lies between 646 and 647. No statement here uses them.
- T4-458 (research/candidate001_affine_exclusion; 14:34Z; 896 exact checks): the exact leading residual of 001 at q = 2
  gamma - 1 > 0 is r^q E(theta) with E nonzero (sine modes 21 to 39), so by the annular theorem T4-049 no h in L^2(R^2)
  solves the correction equation in distributions at any real c. CONFIRMED by the T1/T3 theory worker R1-046 and the T2 theory worker the review of T4-458
  (section 3.3), both accepted in T4-465.
- T4-459 (research/h18_coverage_audit; 806 checks; CONFIRMED by the T2 theory worker the review of T4-459, accepted in T4-462): every
  snapshot 002 to 026 except 011 has fixed-c L^2 distance above 1/1000 by its accepted weak inequality (least floor
  0.001232449584, 015), above the eight scalar ceilings, the original graded ceiling 25/54684 and, under m2 > 0, the
  trans/statL radius 25/(54684 512) < 8.93e-7. 001 needs a separate reason (T4-458); 011 and 027 are OPEN; dyadic
  schemes are not covered.
- T4-460 (research/late_weak_supplement_audit; 257 checks): CONFIRMS the six weak floors of N4-383 and N4-384: 015 at
  0.000351804115950603, 0.001232449584356253 and 0.003033479200692324, 017 at 0.000596123050327423,
  0.001068502321536437 and 0.00167183069831928 (the 017 (21, 522) row stays outside the registered 25-probe family);
  REFUTES a generic relative-change sentence for all six rows.
- T4-461 (research/candidate015_dyadic_audit; 739 checks at 1024 bits): reproduces N4-382; every FW-T-DYADIC-Y-v1 cell
  fails at 015, minimum ratio above 1.242922259074, under that scheme's hypotheses, so row 105 holds in both
  directions (v138). No high inverse is constructed and no exact-profile nonexistence follows.
- T4-462 (research/weight_uniform_gram_audit; 320 checks): CONFIRMS the T2 theory worker's Proposition WU3 (T2-R3 balls at every weight
  pair have ||h||_2 < 3.3469e-6 for beta 2 and < 4.0249e-6 for beta 11/4, at most 1.1746 and 1.0612 times the sharpw and
  TB-sharp ceilings) by an exact elimination of both weights, w2 >= [1440 p + (6 O + 5 a)^2]/((beta - mu) p a^2), and
  the bL cap of handoff BK2 (every bL ball permitted by the unweighted margin has ||h||_2 < 4.1069e-6). The sampled
  near-sharpness concerns the relaxed algebraic problem only; full-scheme sharpness is OPEN. Not covered: the weighted
  margin (B-L2-w), other floors or constants, a dyadic ball. Its elimination is CONFIRMED by the T1/T3 theory worker R1-047 and the T2 theory worker
  the review of T4-462 (handoff BM), both accepted in T4-468.

- T4-463 (research/candidate017_dyadic_audit; 15:05Z; 1070 checks at 1024 bits): reproduces N4-389 from the raw
  generators (strain 1 - c, a0 = 10.3115982158... >= 5c - 4, projected norms 19.7722109806... at 1/4 and
  10.6505742957... at 7/4); every FW-T-DYADIC-Y-v1 cell fails at 017, minimum ratio above 1.221854480167 on [1/4, 1/2]
  (two-endpoint cover), under that scheme's hypotheses, so row 106 holds in both directions (v139). The N3 numerics worker's
  seven-endpoint minimum is a separate claim. No high inverse, full norm or profile nonexistence follows.
- T4-464 (research/tb_rebal_endpoint_audit; 15:07Z; 199 checks at 768 bits): CONFIRMS the T2 theory worker's FALSIFY revision 3 row
  at the exact TB-rebal radius b = 3.5125474811...e-7: retained-shape cutoff at most 0.6720573 and, with V >= v0,
  enclosure [0.6372611, 0.6372960] (on the bracket [3.5125e-7, 3.5126e-7]: at most 0.6720590 and [0.6372593,
  0.6372977]), all below Emin = 0.7930365...; REFUTES the old 007 lower end 0.6372628 as an exact-radius bound
  (the old upper ends stay conservative). The crude cutoff stays above Emin and is inconclusive. No verdict changes.
- T4-465 (research/candidate001_affine_review; 15:11Z; 957 checks): accepts the T1/T3 theory worker R1-046 and the T2 theory worker the review of T4-458; the
  exclusion of every real L^2 correction around 001 is CONFIRMED at every real c and every radius, with no trace,
  symmetry, smallness or derivative hypothesis, and so is R1-046's extension to an added constant background velocity.
  For c != c0 the test function is R^-1 eta(r/R) G0(theta): the angular factor G0 (sine modes 1 to 19) replaces E,
  which is orthogonal to G0 (T4-458 ERRATA_v01, from the T2 theory worker BL2; R1-046 uses G0). REFUTES the reading that changing q
  alone while keeping E gives the changed-c leading pairing. Not covered: non-L^2 classes, a changed far field, a
  linear background, existence.

- T4-466 (research/negative_norm_dual_audit; 15:13Z; analytic audit, no code): CONFIRMS the analytic dual inequality
  H^2 >= sum p_n^2/d_n behind the N4 numerical auditor's prospective 016 negative-norm certificate (distinct modes, strictly positive
  complete test energies, beta > 3/2 and 3 + 2k >= n); REFUTES the inference that a lower H witness below an upper H
  display confirms the upper bound. Every new 016 dual value, H floor and E2 ordering is OPEN until computed
  independently.
- T4-467 (research/candidate016_complete_forcing_audit; 15:18Z; 8874 checks at 2048 bits): CONFIRMS N4-392 and N4-393:
  the four complete 016 norms, all ten registered forcing-test failures and the five orderings 007 < 016 of the actual
  same-parameter XSW forcing norms (gaps above 30.17, 18.23, 18.30, 18.51 and 30.72 for sharp, sharpw, bL[7/5], bL[1]
  and trans), under the accepted moment and commutator premises. OPEN: the actual 016 H, the E2 ordering, Q3 and
  fractional upper bounds; no distance ranking or existence follows.
- T4-468 (research/weight_uniform_review_acceptance; 15:24Z; 364 checks at 768 bits): accepts the T1/T3 theory worker R1-047 and the T2 theory worker
  the review of T4-462, and proves that the equality weights satisfy w1 > 2 and w2 > 1 on each whole mu interval. It certifies
  the seven six-digit displays of handoff BM2 (3.34629e-6, 4.02421e-6, 5.07475e-6, 6.13623e-6, 7.58412e-6, 4.07386e-6,
  4.10620e-6) as the rounding cells containing the supremum of the scalar relaxed formula (8) with the rounded
  constants k = 390.68 and u = 1.5871; they are neither exact suprema of the problem with the exact K and v nor
  directed bounds, and the strict ceilings of T4-462 are unchanged. Sharpness of the weight-dependent scheme stays
  OPEN. REFUTED: the reading that the supremum of s (mu - C s)^2 over all s > 0 is finite (it is infinite). The
  header and one print line of the T1/T3 theory worker's check_T4462.py state it that way; the code and R1-047 use the unsquared concave
  function on the correct range, so the result stands (erratum 79).
- T4-469 (research/divergence_free_negative_norm_upper; 15:28Z; 75 exact fixture checks; erratum ERRATA_v01, team note
  v247): a proposed improvement of the Hardy upper bound for the negative norm H. For F with finitely many sine modes
  and rF in L^2, the angular right inverse A_F is corrected by a divergence-free field Z = A_(Delta psi) - grad psi,
  giving H(F)^2 <= M2 - b^2/a when a > 0, with every omitted mode kept in M2, so no basis-completeness premise is
  needed. The fixtures are CONFIRMED; the general statement is OPEN pending independent review (the T2 theory worker primary, the T1/T3 theory worker
  checking domains and signs). No candidate integral has been evaluated, and no upper value for 016 changes.

### 3.2 the N4 numerical auditor entries N4-333 to N4-397

- N4-333, N4-334: accept T4-405 to T4-408, so 022 is RULED OUT in every registered scalar ball and original graded box
  with independent reproduction in both directions.
- N4-335: numerical consistency audit of the published theory_v07 (12 checks): nine distance ratios conservative;
  the three repairs of section 2.
- N4-336 to N4-339: The N4 numerical auditor's own 023 structure, point gaps, origin, distance and prefix; N4-342 to N4-346: the same for
  024, with the byte reconstruction of its held-out hash. Both packages were reproduced by the T4 theory auditor (section 3.1).
- N4-340: CONFIRMS the repaired the N3 numerics worker calibration runs; REFUTES the claim that the quadrature point values are exact
  rationals. N4-341: first independently CONFIRMED actual 016 whole-plane norms (G0, section 2 (e)); G1 is CONFIRMED in
  N4-373; P2, H and the four-component assembly stay OPEN. N4-347: provenance clarification of the 016 production.
- N4-348 to N4-350 and N4-357 to N4-359: accept the T4 theory auditor reproductions of 023 and 024.
- N4-351: REFUTES the faithful transcription of a the N3 numerics worker 016 summary (eleven dropped negative exponents); no verdict
  changes. N4-352: REFUTES the identification of the residual difference ||F_child - F_parent||_2 with the density
  quantity tau of NC-T-SCREEN; tau bounds ||rho_child - rho_parent||_2, and no transfer follows without a proved
  inverse estimate.
- N4-353: CONFIRMS three complete the N3 numerics worker 016 weak tests ((21, 522), (23, 2400), (19, 1800)) with coarser-cap floors.
- N4-354, N4-355: the two-mode dyadic calibration on 007 and the 016 seven-cell test (section 4).
- N4-356: audit of numerics_v12 (section R5).
- N4-360: CONFIRMS the remaining three the N3 numerics worker 016 weak tests, so all six the N3 numerics worker probes of 016 are independently
  reproduced; two published lower-bound displays round upward and need downward rounding; the Hardy bound stays CLAIMED
  (matrix row 80).
- N4-361 to N4-364: The N4 numerical auditor's own 025 structure, point gaps, complete prefix and distance (section 4). N4-365: accepts
  T4-436. N4-370 and N4-371: accept T4-438 to T4-441, so the 025 package holds in both directions.
- N4-366 to N4-369: The N4 numerical auditor's own 026 structure, point gaps, origin, complete prefix and distance (section 4), reproduced
  by the T4 theory auditor in T4-446 to T4-450.
- N4-372: audit of numerics_v13 (section R5 (m)).
- N4-373: CONFIRMS the N3 numerics worker's 016 whole-plane G1 in [3.726906948019883998020959016407, 3.726906948019883998020959016410] by
  an independent exact production. N4-374: with G0 and G1 alone and the Plancherel bound X_(s,w)(F) >= sqrt(w1 G1^2 + w2
  G0^2), the ten registered scalar forcing conditions fail for 016 (every factor above 3542234, the sharpw one); this is
  a failed sufficient condition, not an exclusion beyond the distance result of section 4, and P2 and the Hardy bound
  stay OPEN. The T4 theory auditor CONFIRMS N4-374 independently in T4-451, and the N4 numerical auditor accepts T4-451 in N4-380.
- N4-377 to N4-379: accept the T4 theory auditor's 026 reproductions T4-446 to T4-450 (structure, point gaps, origin, prefix and the
  weak distance), so the 026 package holds in both directions (v133). N4-380: accepts T4-451.
- N4-375: REFUTES the range 0.83 to 1.17 stated in the N1/N2 numerics worker's 13:38Z note for the 027 against 022 FLOAT probe ratios (the
  stored ratios run from about 0.826 to 1.343); 027 was then a FLOAT trial comparison; it is registered as a snapshot at
  14:13:51Z (section 4). N4-376: an integrity check of fifteen selected final evidence records and their 1378 direct
  edges, CONFIRMED; it promotes no OPEN condition. N4-381 (research/final_scope_audit): an audit of selected passages of
  the coordinator's joint closure report (13:57Z); it REFUTES two stale 007 norm-status sentences there, leaves OPEN a global ranking
  read from quoted lower factors (lower bounds do not order actual norms) and CONFIRMS the scope of the 016
  sufficient-test passage. No statement of this file depends on it.
- N4-382 (research/candidate015_dyadic_peer; 14:11Z): independent whole-plane reproduction of the N3 numerics worker's exact mode 1 and
  mode 3 projected energies of 015 (the N3 numerics worker NOTES 13:27Z), with every contributing background mode retained, at 2048 bits;
  all fourteen mode energies and seven totals agree, and all seven cells of FW-T-DYADIC-Y-v1 have positive directed
  gaps. CONFIRMED under the hypotheses of the FW-T-DYADIC-Y-v1 argument; a projection lower witness, not a complete
  norm, a scalar distance, an inverse or a nonexistence result. The dyadic verdict for 015 is the matrix's (section 4).
- N4-383 (research/candidate015_three_weak_peer; 14:14Z): The N3 numerics worker's complete weak tests of 015 at (n, K) = (19, 600), (23,
  600) and (23, 2400) agree with the N4 numerical auditor's N4-237 and N4-239; the conditional sharp floors are above 0.000351804115950603,
  0.001232449584356253 and 0.003033479200692324. CONFIRMED; it REFUTES three wording items of the source (a generic
  relative-change sentence, a generic Bernstein label, and "distance from F", which is the distance from the reference
  density). 015 stays RULED OUT in rows 77 and 78; no new exclusion follows.

- N4-384 (14:21Z): CONFIRMS the N3 numerics worker's three complete 017 weak tests against N4-256, N4-257 and N4-259, with the sharp
  floors 0.000596123050327423 at (21, 522), 0.001068502321536437 at (23, 2400) and 0.00167183069831928 at (19, 1800)
  (the first is a diagnostic outside the registered family). N4-385: documentary status refresh of the N4 numerical auditor's own summary.
- N4-386 and N4-387 (14:42Z, 14:49Z): the 105 final-report row IDs link to their matrix rows; the nineteen principal
  distance displays are supported by accepted certificates, except two report displays: row 80 (016) printed >0.0014704
  and row 90 (021) printed >0.001864696855, both above their accepted roots (use >0.0014703 and >0.001864696854).
  Neither occurs in this file, and no exclusion changes.
- N4-388 (14:55Z): CONFIRMS the numerics_v14 tables, ratios and labels as FLOAT data and REFUTES three of its labels
  (section R5).
- N4-389 (research/candidate017_dyadic_preparation; 14:56Z): The N4 numerical auditor's own complete computation of J(1/4) and J(7/4) at
  017 confirms the N3 numerics worker's seven-cell record: every cell of FW-T-DYADIC-Y-v1 fails, minimum ratio above 1.221854480167
  (two-evaluation cover), under the hypotheses of that scheme; matrix row 106 (v138) records 017 RULED OUT there; T4-463
  reproduces it (v139).

- N4-390 (15:02Z; 825 checks): accepts the T4-459 finite composition reciprocally (the eight scalar ceilings are below
  3793/10^9, the original graded bound is 25/54684 and the trans/statL bound 25/27998208, all below 1/1000); REFUTES
  reading nine nearest-rounded root_lower displays of the T2 theory worker's review JSON (004, 006, 010, 015, 017, 018, 021, 025,
  026) as strict floors. The T2 theory worker's exact common-floor proof does not use them; this file uses only the directed floors.
- N4-391 (15:07Z): component scope of the N3 numerics worker's final tables; CONFIRMS the repaired 007 Q3 status and interval and
  REFUTES two blanket citation scopes (N4-024 and N4-026 cited for Mpen2, though they concern d2; N4-028 cited for
  001's finite P2 and Q3 columns, though it supports only its snapshot and divergent sectors). No norm changes here.
- N4-392 (15:10Z): CONFIRMS the N3 numerics worker's complete 016 P2 enclosure (218.1040893978241185..., 218.1040893978241317...), so
  G0, rF, G1 and P2 of 016 are all CONFIRMED; H and Q3 are separate. N4-393 (15:10Z): CONFIRMS ten named sufficient
  forcing-test failures of 016 and five orderings 007 < 016 of XSW forcing norms at identical parameters, from
  conservative bounds; no E2 ordering, distance ordering, dyadic result or existence follows.

- N4-394 (15:18Z): REFUTES as a certified inference the claim that 12-digit agreement after a 2.3-fold basis enlargement
  shows the 016 mode-1 dual-to-Hardy ratio is intrinsic slack (an exact three-dimensional counterexample); the
  observation stays numerical evidence, and no exclusion changes.
- N4-395 (research/weight_uniform_budget_peer; 15:20Z; 537 checks): CONFIRMS the seven necessary algebraic budget
  ceilings of T4-462 (3.3469e-6 and 4.0249e-6 for the original R3 and TB floors, three hypothetical larger-floor rows,
  and 4.0746e-6 and 4.1069e-6 for bL at 1 + c0 and 57/20) for every admissible weight pair under its fixed floors,
  uniform constant restrictions and norm embedding, and that the original-floor unweighted bL bound lies below 1/1000
  by a factor strictly greater than 243, so every one of the 24 references 002 to 026 except 011 lies outside that
  common fixed-c ball under its accepted complete weak-certificate hypotheses. The larger-floor rows are conditional
  sensitivity data. Not covered: weighted low equations (B-L2-w), sharper constants, other floors, dyadic or non-L^2
  corrections, varying-c exclusions; the T2 theory worker's finer supremum displays (BM2) were not reproduced.
- N4-396 (research/candidate016_dual_lower; 15:23Z; 38 checks at 4096 bits): from the N3 numerics worker's 338 mode 1 and 325 mode 3
  test coefficients, taken as exact rational data, CONFIRMS H(016) > 0.529469576110512066428681 and E2(016) >
  608.392385921614, above the accepted 007 upper bound 606.820219, so E2(007) < E2(016) under identical energy weights
  (a difference of conservative bounds). This settles the E2 ordering left OPEN in T4-466 and T4-467 in the N4 numerical auditor's own
  computation; the N4 numerical auditor has asked the T1/T3 theory worker and the T2 theory worker for analytic reviews. No H ordering, distance ordering, inverse or
  existence follows.
- N4-397 (research/candidate001_affine_peer; 15:30Z; 1104 exact checks): The N4 numerical auditor's own reproduction of the 001 leading
  data from the 860 raw generators (G0 with sine modes 1 to 19, E with 21 to 39, every coefficient nonzero; the
  degree-gamma residual vanishes and the degree-q residual is exactly E) and of the corrected annular argument (test E
  at c = c0, G0 at c != c0). It CONFIRMS that no real h in L^2 solves the stationary equation around 001 at any real c,
  also with a constant background velocity; it does not cover non-L^2 corrections, another far field or reference,
  linear backgrounds or self-similar IPM profiles in general.

### 3.3 Batch T reviews since theory_v07

- The T2 theory worker the review of T4-402 (accepted in T4-413), the review of T4-410 (main obstruction CONFIRMED in T4-421, side assertion
  REFUTED), the review of T4-414 (accepted in T4-423; restored to its 12:08Z bytes 221b1135... at 12:30:37Z; its section 4
  corrects the answer "in principle yes" for 583/1000 in the review of T4-402 section 4) and the review of T4-415 (sha256 prefix
  ee7b1b1b, accepted in T4-434). The T2 falsification review of the endpoint and the report summary (revision 1, sha256 prefix 6eede464: finite arithmetic
  and split-integral theorem CONFIRMED in T4-443; revision 2, 660b089b, makes the five wording repairs of T4-443,
  accepted by the T2 theory worker in handoff BB3 and BC, with no number changed) and CHECK_T1_v08_FACTORS revision 1 (sha256 prefix
  35a42457; the check of section 1 requested in team note v47: every factor is an exact floor of p/t, and the radius at
  which t is taken is stated in section 1.1, handoff BA and BB) and its revision 2 (sha256 prefix 09e274f6, 14:13Z; the
  Targets bullet of preview2 and the bullet on H >= H0: every number and inequality is correct, handoff BG1).
- The T1/T3 theory worker R1-043 (review set 41; CONFIRMS T4-410; accepted in T4-424), R1-044 (review set 42; the outer amplitude bound and
  the kernel thresholds; CONFIRMED by T4-426 with repairs; errata E1 to E3 and the binding note E4 in review set 43,
  accepted in T4-432) and R1-045 (review set 43; CONFIRMS T4-425; accepted in T4-432).

- The T2 theory worker handoff BH to BM (14:31Z to 15:16Z): its H18 result restates the T2 final summary section 0 item 2 with the scope of
  T4-119 (state 131 matrix floors with all other constants fixed; ceilings, not attainable improvements); the FALSIFY
  revision 3 note (BI); Proposition WU3 (BJ2; CONFIRMED in T4-462); the review of T4-459 (BK1, sha256 prefix e140e6c0, 189
  checks; CONFIRMS T4-459, accepted in T4-462); the bL cap beta_L <= 1 + c < 57/20 (BK2; CONFIRMED in T4-462); and
  the review of T4-458 (BL, sha256 prefix ca936460, 30 checks; CONFIRMS T4-458 by Wirtinger calculus, with the G0 wording
  correction BL2; accepted in T4-465); and the review of T4-462 (BM, sha256 prefix 2cb6f7e6, 52 checks; CONFIRMS T4-462 under
  its hypotheses, with the conflict of interest stated, since T4-462 audits the T2 theory worker's own WU3). BM2 displays the
  suprema of the relaxed budget to six digits, 3.34629e-6 (R3) and 4.02421e-6 (TB), 1.7e-4 to 1.9e-4 relative below the
  WU3 bounds, which remain valid upper bounds; T4-468 certifies these displays for the relaxation with the rounded
  constants k = 390.68 and u = 1.5871 only. BM3 records WU, WU3 and the bL cap as AUDITED by T4-462.
- The T1/T3 theory worker R1-046 (review set 44, sha256 prefix 1b7c425c; CONFIRMS T4-458 in the affine class rho + L^2 only, with an
  independent exact check artifacts/checks/check_T4458.py, 912 checks) and R1-047 (review set 45, sha256 prefix b8771fb6;
  CONFIRMS the exact weight elimination, the constants and the seven bounds of T4-462, with
  artifacts/checks/check_T4462.py, 48 checks). Its H18 check artifacts/checks/h18_verdicts.py compares every candidate
  verdict of THEORY_FINAL sections 0 and 7 with the matrix row by row (158 claims, 0 failures against v140; errata 77
  and 78). The T4 theory auditor accepts R1-046 in T4-465 and R1-047 in T4-468 (team note v245, erratum 79).
## 4. Candidates

The exclusion table with every certified floor and factor is THEORY_FINAL section 7; it is not repeated here.

- C1-N1-023 (016 plus 252 radius-100 functions in j = 1 to 3, m = 9 to 15; 2426 generators; registered 10:42:28Z):
  RULED OUT in every ball of matrix rows 94 and 95 (v122). Point gap F(1/10, 73/100) = 0.083280868582953659827...,
  original graded gap 0.062882815459541270946..., exact origin normalization, complete prefix, and distance above
  0.002634958245163687 at the registered probe (19, 1800), at least 5.763 times the graded ceiling (N4-336 to N4-339,
  reproduced in T4-416 to T4-420, accepted in N4-348 to N4-350).
- C1-N1-024 (the rule control of 016; 2174 generators; registered 11:31:32Z): RULED OUT in every ball of rows 96 and 97
  (v124). F(1/10, 73/100) = 0.0952808775288636068..., original graded gap 0.074870039634554045..., distance above
  0.001556067368832641 at (19, 1800), at least 3.403 times the graded ceiling (N4-342 to N4-346, reproduced in T4-427
  to T4-431, accepted in N4-357 to N4-359). No one-variable comparison with 016 follows (N4-342, T4-427).
- C1-N1-016 and C1-N1-015, FW-T-DYADIC-Y-v1: 016 is RULED OUT conditional on the hypotheses of the origin inverse
  theorem (row 98, v126). The N4 numerical auditor's own complete computation of the mode 1 and 3 norms gives J(1/4) = 19.914089787... and
  J(7/4) = 11.176463132..., which verify the N3 numerics worker's CLAIMED record. Since J is nonincreasing in a, J(1/4) bounds the first
  cell and J(7/4) the other six, and all seven cells fail with minimum ratio above 1.253908386497 (N4-355, after the 007
  calibration N4-354). At 015 the N4 numerical auditor's N4-382 (14:11Z) independently reproduces the N3 numerics worker's seven-cell record of 13:27Z
  (exact mode 1 and mode 3 projected energies, every contributing background mode retained, 2048 bits): every cell
  fails, minimum ratio above 1.242922259074, CONFIRMED under the hypotheses of the FW-T-DYADIC-Y-v1 argument; closure
  matrix row 105 (v135) records 015 RULED OUT in FW-T-DYADIC-Y-v1 for every 0 < a < 2, 0 < s < 1 and finite Rw under the
  audited framework hypotheses and the candidate hypotheses checked in N4-382. The T4 theory auditor's T4-461 (14:52Z) reproduces N4-382
  independently (739 checks). At 017 the N4 numerical auditor's N4-389 (14:56Z) CONFIRMS the N3 numerics worker's seven-cell record (CLAIMED, 14:22Z) by its
  own complete computation of J(1/4) and J(7/4): under the same hypotheses every cell of 0 < a < 1 + 1/c fails, minimum
  ratio above 1.221854480167 (two-evaluation cover); closure matrix row 106 (v138) records 017 RULED OUT in
  FW-T-DYADIC-Y-v1 on this basis, one sufficient scheme removed, not a profile; the T4 theory auditor's T4-463 (15:05Z, 1070 checks at
  1024 bits) CONFIRMS N4-389 independently, so row 106 is accepted both ways (v139). The NC-T-ORIGIN-INV test is not
  reported at 011 to 014 and 018 to 027; numerics_v13 section 3 gives FLOAT two-mode proxies for 008 to 025, with no
  verdict.
- C1-N1-025 (016's exact JSON plus 744 functions; 2918 generators; registered 12:50:59Z; rows 99 and 100): RULED OUT in
  every registered scalar ball and original graded box of rows 99 and 100 (matrix v130, 13:27Z). Its dimension and
  objective are CONFIRMED in both directions (N4-361, T4-436, N4-365). The N4 numerical auditor's own results: F(1/10, 73/100) =
  0.0902711481553922827..., graded gap 0.0698812708067483536... and positive gaps for the six registered scalar point
  budgets (N4-362), the complete sixteen-sector prefix through exponent -7/2 (N4-363), and distance above
  0.002065801265578052 at (19, 1800) (N4-364), more than 4.518 times the graded ceiling and 544.6 times the TB-sharp
  family ceiling (the T1/T3 theory worker arithmetic with exact fractions). The T4 theory auditor reproduces all four independently in T4-438 to T4-441
  (13:18Z), and the N4 numerical auditor accepts the reproductions in N4-370 and N4-371 (13:22Z). The dyadic row of 025 is untested.
- C1-N1-026 (the 022 state, 2414 generators, continued 60 steps with the 81 rows of 025; registered 13:12:37Z;
  numerics_v13 section 2b): RULED OUT in every registered scalar ball and original graded box of rows 101 and 102
  (matrix v132, 13:47Z). The N4 numerical auditor's own results: 2414 shapes, the same ordered list as 022, with 81 objective rows and all
  46 probes outside their span (N4-366); F(1/10, 73/100) = 0.0799019876430402887..., graded gap 0.0594850343605722625...
  and positive gaps for the six scalar point budgets, exact origin normalization (N4-367); the complete sixteen-sector
  prefix through -7/2 (N4-368); and distance above 0.001355907204057457 at (19, 1800) (N4-369), more than 2.965 times
  the graded ceiling, 357.4 times the TB-sharp and 475.8 times the sharpw family ceiling (the T1/T3 theory worker arithmetic with exact
  fractions). The T4 theory auditor reproduces all of them independently in T4-446 to T4-450 (13:45Z), with the same strict floor
  0.001355907204057457 at (19, 1800) (T4-450: 63 whole-plane moments at 2048 bits, no spatial truncation). The N4 numerical auditor accepts
  the reproductions in N4-377 to N4-379 (13:55Z; matrix v133). The dyadic row of 026 is untested.
- C1-N1-027-cont60-legqs25-m16to23 (the 022 state, 2414 generators, continued 60 steps with the plain 67 rows of 016, a
  control for 026; registered 14:13:51Z; the N1/N2 numerics worker NOTES 14:13Z): FLOAT values only (G0 0.2762 at MID 32; 7 of the 25
  held-out probes above the graded ceiling, the largest 8.25e-4 at (19, 1800)); untested, and not a certification
  target.
- So every snapshot C1-N1-002 to C1-N1-026 except 011 has no exact solution at its reference c in any registered scalar
  ball or original graded box with a positive top-row budget in closure matrix v140 (2026-10-29T15:22Z) (for 002, 003
  and 004 beyond the specified balls of rows 36, 40 and 42 through the fixed-c L^2 distances of T4-068 and the radius
  caps of row 55), 001 is RULED OUT in the matrix only as framework inapplicability (row 35) and has no L^2 correction
  at any c by T4-458 with R1-046 and the review of T4-458 (accepted in T4-465), 027 is untested (rows 103 and 104 OPEN), and
  028 is a reserved ID without a registered snapshot (numerics_v14). No exclusion is a nonexistence statement: each
  concerns the fixed c and the stated balls.

## 5. The endpoint route and NC-T-TWO-WEIGHT

theory_v07 section 5.7 (a) to (e) hold as published, with the status updates below. Its item (d) (ii), a
correction-specific expansion of U[k] from the tail profile of k, is the route of items (c) to (e) here: with the
present tail input it certifies no target. Its items (d) (i) and (iii) remain neither proved nor excluded.

(a) Setting. The T4-351 radial test certifies a lower bound on the correction size from the endpoint projection
B of the angular data, given an upper bound ehat(r) on the error |e(r, theta)|/r^q. Its compensated-velocity part is
a coefficient E times H = H_q(h) s^q in the forcing; integrating the stationary radial equation for r^(-gamma) h from r
to infinity gives the error contribution (H G/D) r^(q-delta) Eeff(r) (T4-425 (4)). The test reaches the target beta
only if the integrand [B - sqrt(2 pi) ehat(r)]_+^2 r^(2q+1) is positive on part of [R, r_beta].

(b) Universal coefficients (NC-T-UNIV-E, rows U1 to U4). Every universal constant is at least Emin = 0.79303650642...,
above Ecrit at each of the four targets; the best one lies in [Emin, 1.747261] (T4-381, T4-397, T4-411). At the FW-A2-Db
radii no such obstruction is proved (section 2 (g)).

(c) Profile coefficients (rows P1 to P5). The limits 583/1000 (T4-402) and 93/250 (T4-415) hold only as s tends to
infinity. With zero remainder, 93/250 would pass the three scalar thresholds and not the graded one (T4-422), and no
angular certificate on the whole span can go below 0.3714757 at 007 (the review of T4-415).

(d) NC-T-TWO-WEIGHT (new; AUDITED in its parts). Let h be a real C^1 S1 correction with finite H > 0 satisfying the
hypotheses of T4-335, whose only proved tail list, T4-335 (7), contains the strictly positive term C_delta r^(q-delta),
C_delta = H (V + E G)/D. Then no certificate of the T4-351 test built from the following majorants reaches any of the
four targets (fixed sharpw ball, sharpw ceiling, TB ceiling, graded ceiling) for 007, 013 or 014:
  - (i) the T4-410 remainder with any R0 >= 2 and 0 < epsilon <= delta, added to 93/250 or 583/1000 with a constant
    coefficient at a starting radius R <= r_beta (rows R1 to R3; R1-043 step 9, the review of T4-410, T4-421,
    the review of T4-415 section 7);
  - (ii) any radius-dependent coefficient chosen from these T4-410 estimates, their envelopes and any norm-class
    universal constant, from any starting radius (row A1; T4-425, AUDITED through R1-045 and T4-432);
  - (iii) any majorant that keeps the outer amplitude alone, with V >= 0, G >= g0 and universal coefficient >= Emin
    (R1-044, CONFIRMED by T4-426; extension in T4-432);
  - (iv) a constant Lam in place of the bracket of T4-410 (2), unless Lam is below the Arb upper bounds 13.27 (14.41
    with the fallback), 8.647 and 7.287; T4-410 has Lam >= 109.6024 (rows K1 to K3; necessary only).
At the graded ceiling there is no room even for zero remainder. The statement bounds the stated majorants; it is not a
lower bound on the actual velocity, a nonexistence result or an unconditional candidate exclusion (T4-425 section 4,
T4-426, T4-432).

(e) What would lift it. A tail bound for stationary corrections whose exponents all gain well over delta on r^q (FLOAT
estimate near 1.05; with exponents near q + 5 the inner part would be about 0.015 H, FLOAT), or a velocity or H_q
estimate that uses stationarity or the tail class, or a different norm or method. The T1/T3 theory worker (R1-044 section 4), the T2 theory worker
(12:10Z) and the T4 theory auditor (H16 checkpoint) judge that neither is worth hours 16 to 22, and the coordinator accepts this (12:30Z item
2). NC-T-ENDPT-Y (H_q > 999745 for every stationary correction with finite H_q, T4-380) is unchanged.

## 6. Final requests to batch N

These replace theory_v07 section 6. They are ranked by effect on the matrix, not on a closure ratio: section 1 shows
that no present framework is near closure for 007, the reference with the most complete hypothesis record.

1. C1-N1-025 (and any further snapshot named a target): the point gaps, the origin normalization, the sixteen-sector
   prefix and the registered-probe distance, as N4-342 to N4-345 with T4-427 to T4-431 for 024. Probes are taken from
   the public register. Both directions are complete for 025 (N4-362 to N4-364 and T4-438 to T4-441, accepted in N4-370
   and N4-371), which is RULED OUT in v130 (section 4). For 026 both directions are complete (N4-366 to N4-369 and
   T4-446 to T4-450), it is RULED OUT in v132, and the N4 numerical auditor accepts T4-446 to T4-450 in N4-377 to N4-379 (v133). Two
   independent directions suffice for a RULED OUT entry.
2. The seven-cell test NC-T-ORIGIN-INV for FW-T-DYADIC-Y-v1 at 011 to 014 and 018 to 027 (015 is RULED OUT by N4-382,
   matrix row 105, reproduced by T4-461; 017 is RULED OUT by N4-389, matrix row 106; section 4), in the
   two-evaluation form of N4-355 (J(1/4) on [0, 1/4] and J(7/4) on the other six cells, valid since J is nonincreasing
   in a), after a calibration on 007 as N4-354. This tests the remaining dyadic rows and does not establish a closure.
   Where every cell ratio is above 1, the test refutes the necessary inequality and the snapshot is RULED OUT in
   FW-T-DYADIC-Y-v1; where it is not, the test is inconclusive, as at 009, whose FLOAT two-mode bound does not exclude
   while the exact all-mode N_a excludes every cell. No dyadic verdict is promised in advance, and none follows from the
   scalar and original graded exclusions.
3. R-TAIL (theory_v06 section 5.5) for any reference used in a closure attempt.
4. No request for a sharper universal velocity constant (rows U1 to U4: none can be below 0.79303650642, and at the
   FW-A2-Db radii, where the U rows say nothing, NC-T-DIST excludes 007, 013 and 014 by factors above 28895, the
   distance floors of T4-185, T4-255 and N4-214 divided by the radius; the T2 theory worker CHECK_T1_v08_FACTORS section 3) or for a
   sharper angular profile coefficient on the whole span (row P2: none can be below 0.3714757 at 007). A new endpoint
   certificate needs a stationary tail input of section 5 (e); batch T does not pursue it in hours 16 to 22.
5. A new candidate can enter a registered scalar ball or original graded box only if none of its certified distance
   lower bounds at the registered probes exceeds the ceiling of that family; these ceilings are more than 10.4318 times
   (graded) and 1257.36 times (scalar) smaller than the proved floor of 007 at the same c (rows D5 and D1). They do not
   bound the radius of an untested dyadic or localized framework. A smaller floor is necessary, not sufficient: a
   closure with the specified sharp or sharpw certificates then still needs rows S and item N1 of section 1, which are
   requirements of those certificates, not of every framework. No lane should spend hours 18 to 22 improving a candidate
   that already has a rigorous obstruction above its threshold (the coordinator 13:01Z item 6).
6. NUMERICS_FINAL wording: replace every blanket FLOAT range by statements for each probe (N4-356, T4-435, the coordinator
   13:01Z item 2); round lower-bound factors down (5.763, 924.6 and 3.403); state 024 as RULED OUT (v124); add the
   certified floors of 022, 023 and 024 to the floors section; say next to the 009 row that the FLOAT "NO" is the
   weak two-mode bound while the exact all-mode N_a excludes every cell (the coordinator 12:46Z item 4).
7. theory_v06 section 6 items 4, 6, 7, 8 and 9 hold unchanged (per-step reporting, the NUMERICS_FINAL wording,
   far-field remainders by complete finite Beta sums, D-TE, the hypothesis list last); its item 5 (the seven-cell test)
   is item 2 here.

## 7. Review requests and assignments

- The T4 theory auditor: the exact-file audit of the published version, as T4-412 (preview1 is audited in T4-445, whose seven repairs
  are made, and preview2 in T4-455, whose three updates are made); the 24 rows of section 1 and their sources are
  audited in T4-437, and the repaired S2 row and scope texts of section 1.1 need a check; draft 38 is audited in T4-442,
  and draft 39 (13:47Z) is audited in T4-453, whose updates are in draft 42, and draft 43 (14:09Z) in T4-456, which
  CONFIRMS them; later drafts change only the T4-455 citations and the cap distinction of section 3.4 (G7) (e), the 015
  dyadic reproduction N4-382, the registration of 027, the matrix version, the sources and two reproduction entries
  (the T1/T3 theory worker team note v50 gives the lines); the 025 checks of section 6 item 1 are done (T4-438 to T4-441), and so are the
  026 checks (T4-446 to T4-450).
- The T2 theory worker: the check of section 1 asked in team note v47 is done (CHECK_T1_v08_FACTORS revision 1, section 3.3); so is the
  check of the Targets bullet of section 1.1 (CHECK_T1_v08_FACTORS revision 2, 14:13Z, sha256 prefix 09e274f6, handoff
  BG1: every number and inequality is correct; its wording suggestions BG2 are taken, with the status labels of T4-454
  and T4-455); its falsification check is used in section 2 (g) and item 73. The T4 theory auditor T4-443 has audited its finite
  arithmetic and its split-integral theorem; its revision 2 (13:42Z, sha256 prefix 660b089b) makes the five wording
  repairs of T4-443, CONFIRMED in T4-452 (among them: Emin is a lower bound on valid constants, not a proved admissible
  constant, and passing a necessary test does not refute the obstruction). The one-unit brackets below the printed
  sharpw and TB family ceilings, assumed in revision 2 and in CHECK revision 1, are evaluated in the T2 theory worker handoff BE
  (section stamp 14:00Z) and CONFIRMED by the T4 theory auditor in T4-454 (section 1.1); FALSIFY revision 3 (handoff BI, sha256 prefix
  de588453) cites BE and T4-454 and is CONFIRMED by the T4 theory auditor in T4-464. BE3 finds the TB-rebal ceiling 3.51254748...e-7
  above its printed 3.5125e-7 (a display rounded to nearest); THEORY_FINAL now prints 3.5126e-7 (its section 11 item
  75), and no verdict changes, since the thresholds decrease as the radius grows.
- The N4 numerical auditor: the review of the remaining the N3 numerics worker 016 records (the Hardy bound and the full duality bound H(016) >=
  0.6167335007, CLAIMED, row 80 of v140; the six probes are reproduced, N4-353 and N4-360, G0, rF, G1 and P2 are
  CONFIRMED in N4-341, N4-373 and N4-392, and the actual homogeneous negative norm H is not) and of the 017 records G0,
  rF, G1 and P2 (the coordinator 13:01Z item 5); three complete 017 weak tests are CONFIRMED (N4-384, T4-460).
- The T1/T3 theory worker: the final THEORY_FINAL (freeze 18:30Z, final 19:00Z) with this content (draft 52, 15:29Z, sha256 prefix
  82b4d9db, is current); the review of any new the T4 theory auditor theorem on a stationary velocity or H_q estimate; the analytic
  review of N4-396 that the N4 numerical auditor requests and the check of domains and signs of T4-469 that the T4 theory auditor requests. R1-046 (T4-458)
  and R1-047 (T4-462) are done (section 3.3).

## 8. Errata

Numbering continues THEORY_FINAL section 11, where items 67 to 72 are stated in full. Item 69 is the repair of
theory_v07 and is section 2 (a) to (c) here. The others concern THEORY_FINAL drafts and the T1/T3 theory worker reviews:

- 67: the bound K < 1/H0 of NC-T-ENDPT-Y needs K > 0; for K = 0 the majorant is linear, t* = eta and eta > H0 (T4-399).
  The conclusions hold in both cases.
- 68: the estimate "of order 0.1 to 0.3 H" for a remainder built from T4-335 (7) is withdrawn (row R).
- 70: the requirement "a velocity constant on the C^0 tail term below 23.14" of R1-043 holds only for a certificate
  that starts at R <= r_grad (T4-421); the printed digits of R1-043 are repaired outward in T4-424; the errata E1 to
  E3 of R1-044 (the part H V/D of the delta term; "Eeff >= 0.7930000" false, > 0.7929999 used; 0.793 is a relaxed
  value, not admissible).
- 71: the stale sentence "023 and 024 have no certified distance" of draft 35.
- 72: the eight repairs of T4-433, among them "there exists a valid universal constant below 1.747261" (valid
  constants are upward closed) and the scope of the 1.72 illustration (the fixed fallback Eu = 1.747261, not the
  general bound Eeff > 0.79303).
- 73 (new; the T2 theory worker the T2 falsification review of the endpoint and the report summary against draft 36): the scope of NC-T-UNIV-E (section 2 (g)) in
  THEORY_FINAL sections 0 and 6; "E_q* > 133" (already scoped to the original T4-335 coefficient in draft 38, item 72
  (6)) is written "E_q* = 133.004... of T4-335 (i)", the value of an upper-bound formula, not a lower bound on valid
  constants; with E = 1.747261 and H >= 999745 the caps are below 1.66122e-8 (crude) and 1.89061e-9 (radial shape),
  below every registered radius (the T2 theory worker; CONFIRMED by the T4 theory auditor T4-443); R1-038's velocity condition fails for every valid
  constant once H_max >= 999745 (needs E below 0.2694533 at the printed graded target 25/54684, the T2 theory worker); and two
  presentation defects (756.53 for 756.5312630768, and the matrix version cited in section 0 item 1).
- 74 (new; T4-442 against draft 38): (1) section 3.4 (G7) (e) (i): lambda = 1/2 + 5 2^(1-q) is 109.60242254..., so "=
  109.6024" is replaced by "> 109.6024"; (2) section 9 item 6 repeats the bound lambda H (5/r)^delta on [L0, 18860]
  without the qualification of section 3.4 (valid for r >= max(L0, 5), with lambda H for L0 <= r < 5); (3) section 10:
  modes 1 and 3 give the projected norm 13.758675979450936..., so the lower bound is N_1 > 13.75867597, not N_1 >=
  13.758676; this concerns the lower inference, not the unknown full N_1; (4) section 7: the 023 distance "exceeds the
  graded ceiling by a factor greater than 5.763", not "is 5.763 times"; (5) section 3.4: the factor above 4.34 is the
  outer comparison without the universal fallback, and the fallback version is the separate inequality Eeff >
  0.79303648; (6) exclusions in the scalar and original graded balls are listed apart from dyadic statements, and the
  FLOAT exponent near 1.05 belongs to the replacement-tail model, not to every stationary estimate.
- 75: the FW-T-TB-rebal-v1 ceiling, printed 3.5125e-7 up to draft 40, is 3.51254748...e-7 (the T2 theory worker handoff BE3,
  CONFIRMED in T4-454); 3.5126e-7 is printed now. No verdict changes.
- 76 (T4-453 against draft 39): section 0 item 1 now displays the normalized R1-038 condition E sqrt(2 pi) H_max/B <
  Emax(b), names the four targets of T4-425, lists rF among the CONFIRMED 016 components (N4-341) and reads "every
  registered scalar ball and original graded box". No number or verdict changes.
- 77 (own H18 check): "every snapshot 001 to 026 except 011 is RULED OUT in every registered scalar ball and original
  graded box" overstated two cases: row 35 excludes 001 only as framework inapplicability, and rows 36, 40 and 42
  name specified balls for 002 to 004, which reach the other balls through the T4-068 distances. 001 is now stated
  separately (T4-458 with R1-046 for the affine L^2 class).
- 78 (the T2 theory worker H18 result): the T4-119 factors 2.2 and 1.81 bound only the state 131 matrix floors with every other
  constant fixed; the weight question in the T2-R3 L^2 budget is bounded by WU3 (T4-462). No number changes.
- 79 (T4-468, team note v245): the header comment (B) and one print line of the T1/T3 theory worker's artifacts/checks/check_T4462.py
  (sha256 prefix 6d8b95ec, frozen by the T4 theory auditor) read "sup over s > 0 of s (mu - C s)^2 is 4 mu^3/(27 C)". Over all s > 0
  that supremum is infinite; the stated value is the supremum over 0 < s < mu/C, the positive-margin range, equal to
  the square of the maximum of t (mu - C t^2) over t > 0. The code checks that unsquared concave form and R1-047 uses
  the correct range, so no check, bound or verdict changes; the script stays unchanged because the T4 theory auditor froze its hash.

Items 67 to 72 change no candidate exclusion or verdict (item 70 repairs displayed digits outward). Item 73 and section
2 (g) narrow NC-T-UNIV-E and change no exclusion. Item 74 corrects one false equality, one upward rounding and four
scope statements and changes no exclusion. Items 75 to 79 correct one display, three scope statements and one comment of
a the T1/T3 theory worker check script and change no matrix verdict. No erratum to theory_v01 to theory_v06 is new.

## R5. Response to numerical reports

numerics_v12 (the N1/N2 numerics worker, stamped 2026-10-29T12:32:15Z, sha256
20763c86645a954697bb617b57efc7d81f7afbbcd3aa173d5ee4d00d352bae9c, 234 lines) was ACKed by the T1/T3 theory worker at 12:39Z (status file
ACK log). Its sections 3 and 6 item 1 are worded as FLOAT trial comparisons with no verdict, as required. Two
independent audits REFUTE literal summaries and change no exclusion: N4-356 (the blanket K = 600 and K >= 1200 ranges
fail, for example at (19, 600), a 24.94-fold increase for 025; MID16 labels wrong for 024) and T4-435 (67 checks; the
same counterexamples and the 026 K = 600 mode 19 increase by 2.508; the corrected internal comparisons and witness
factors are CONFIRMED). Repairs asked for numerics_v13 and NUMERICS_FINAL, all literal (numerics_v13 makes (b), (c),
(d), (f), (g) and the header part of (a)):

- (a) The "consulted" header bullet is spliced with section 6 text, and the two "Optimizer report" lines lost their
  leading digits (the T1/T3 theory worker ACK note 1; the coordinator 12:46Z item 4 (a)).
- (b) 024 is RULED OUT since matrix v124, not awaiting the T4 theory auditor's replay (ACK note 2; item 4 (b)); every snapshot 001 to
  024 except 011 is then RULED OUT.
- (c) Lower-bound factors are rounded down: 023 reads 5.763 and 924.6, 024 reads 3.403 (ACK note 3; item 4 (c)).
- (d) The section 3 heading says 011 to 021 while its table lists 008 to 025 (item 4 (d)).
- (e) The certified floors section stops at 021; add 022 > 0.0013525, 023 > 0.0026349 and 024 > 0.0015560 at (19,
  1800) (ACK note 4).
- (f) The section 1 heading should cite both held-out hashes of 024, 58586004... and the current e171c051... (ACK
  note 5; N4-346).
- (g) Every blanket FLOAT range is replaced by per-probe statements (N4-356, T4-435, the coordinator 13:01Z item 2).

numerics_v13 (the N1/N2 numerics worker, stamped 2026-10-29T13:13:19Z, sha256
7ae8af1782e3d8e80205d16104dda60ee086152e87f074be8aaefba968b11952, 280 lines) was ACKed by the T1/T3 theory worker at 13:23Z (status file
ACK log). It adds the MID 32 norms of 025 and the new snapshot 026, all FLOAT, and states every comparison per probe. It
changes no requirement and no exclusion. Repairs for NUMERICS_FINAL, all literal:

- (h) numerics_v13 section 5 still stops at 021 (item (e)); add also 025 > 0.0020658 at (19, 1800), RULED OUT in v130
  (N4-364, T4-441).
- (i) Section 6 item 3 says that 025 has FLOAT values only. The N4 numerical auditor's own N4-362 to N4-364 (13:10:44Z, before the stamp)
  and the T4 theory auditor's T4-438 to T4-441, accepted in N4-370 and N4-371, give its point gaps, prefix and distance (section 4). For
  026, the N4 numerical auditor's own N4-366 to N4-369 (13:21Z, after the stamp) and the T4 theory auditor's T4-446 to T4-450 (13:45Z) give the same
  package in both directions.
- (j) The section 3 remark that the 016 FLOAT row agrees with the N3 numerics worker's exact values "CLAIMED pending the N4 numerical auditor" is stale:
  N4-355 is the N4 numerical auditor's own complete computation, and matrix v126 row 98 records FW-T-DYADIC-Y-v1 RULED OUT at 016,
  conditional on the origin inverse hypotheses.
- (k) Section 6 item 1 uses causal wording that its own header excludes ("responded only to the scale-25 functions",
  "new mid-field freedom goes into rF first"); only the per-probe changes should be stated. The rF share is 94 percent
  in section 0 (g) and about 95 percent in section 6 item 1; the candidate and rule should be named.
- (l) The three "Optimizer report" lines again lost their leading digits (the rest of item (a)); the header names
  theory_v06 as the version followed and cites matrix v110 in the coord-notes bullet.
- (m) the N4 numerical auditor's audit N4-372 (13:25Z, research/numerics_v13_audit) CONFIRMS that every checked table value matches its
  stored FLOAT source and REFUTES literal counts and ranges of section 6: 024 has 18 increases and 7 decreases in the
  stored values; the 025 decrease ratios run from about 0.0341788 to 0.598336 and its ten K >= 1800 ratios from about
  1.40496 to 2.84680; 026 has 9 decreases and 16 increases. It also finds the MID16 labels on 024's MID32 run and three
  unsupported attributions of a certified total density-change bound. NUMERICS_FINAL should use the corrected counts,
  which remain FLOAT observations.

numerics_v14 (the N1/N2 numerics worker, stamped 2026-10-29T14:44:45Z, sha256
21c809ab7b3dbf7f1292013275a865aef5b6d28087346cb97c8393630960b15d) was ACKed by the T1/T3 theory worker at 15:02Z (team note v51 item 1;
status file ACK log). 027 stays FLOAT data (matrix rows 103 and 104 OPEN); 028 is a reserved ID with no registered
snapshot; it names no certification target, so no theory requirement changes. The N4 numerical auditor's N4-388 CONFIRMS its tables, ratios
and labels as FLOAT data and REFUTES three of its labels; the repairs are those recorded in matrix v138 and v139. No
request to batch N follows from it beyond those literal repairs for NUMERICS_FINAL.

## Appendix H. Full sha256 of the consulted files

Paths are relative to working file r6 (not published) Hashes were computed at publication.

- ea27c926dd2795d0e43f61f2f413f226887d4e3496c6929ac2fbdf7330a65087 working file team notes (not published)
- 3470e7422509927ae5e456dd9bbbfcff80aa3b50c81a274c47125dc044148334 working file verdict ledger (not published)
- bb8e14dd1f9908fba8a994325dbb215f79c677d3ea7b04348fdf81d2c4d1b9eb working file PROOF.md (not published)
- d7b34632c5722208dcb28cfeaa984aa7170116f8c9a2a62ced4a0b2a71c11ca0 working file PROOF.md (not published)
- 0999eeb3dcb8be8f0577c651f708263e6cd2935cf8f28c7c48119c7efae3467c working file PROOF.md (not published)
- 4a98af09dd96e9245aa0bee8a718eb19b3943f1e7dd7f7fdd702519f4c7eabca working file PROOF.md (not published)
- 20f14eeb4b85aa866f73ef9a3ec10834273ad80241bcf6058089823379a3b3fb working file PROOF_v02.md (not published)
- ed8f4a073d6242d4648074b92f2803a1a598538aaddea8083fe2700f2dc18abf
  working file PROOF.md (not published)
- 1a5b775112dc10663ff59d9722079cfa95056102529eb1b5d730625d2b568fff
  working file PROOF.md (not published)
- 4547c192d6a285575f7f932227301fd6d24927ea366cedb00f20dafa59071509 working file PROOF.md (not published)
- 55765490eb36dd9de1f20386dedbaf61b11767d1f32cd74899539d2b9013155b
  working file PROOF.md (not published)
- 54283bcc7da74a9bf2ed31c9c1ab5b5c4566b7de820ca3e5e4adf17b45ead156
  working file PROOF_v02.md (not published)
- 58d972990c4462758b0414699d9d571ab2f8697dc0f5e8c262994dcfde0e11a1 working file PROOF.md (not published)
- 79fce8fe5fa3e7ebf98a85adb378ab9b3f5a9b78a353b07e5a1cffeaaf9663c3 working file PROOF.md (not published)
- 9fa1d42aab6569b220de406bcdd12fda2d4edb2d68ad26d78ab3b0ee3ef8f4a6 working file PROOF.md (not published)
- b26e24fdcb627135aca6dbe52c6178fd9cbb266a83d47014014b9b3f40e49a91 working file PROOF.md (not published)
- 7e66a460a0bbd00d664a5eea7248c65a8e052d83304f34a2488af1e46fbb7b06 working file PROOF.md (not published)
- c076010696004d25d4a288ce1bd0fd3e132ec9dc17b043697e42fd00c2dec0e7 working file PROOF.md (not published)
- 32ad46f88f6ff3aeee5e4575a63d480e992532741b9854f802f6fe20f85af1f3 working file PROOF.md (not published)
- f0ffb789598753cf5fa546937632a6b56ce5814b04056413e364c8b0301a1b12 working file PROOF.md (not published)
- b4bb5ba465c472c463a19d3c1121d4d614fa07f0c09fbef9c8c77566eabf6b82 working file PROOF.md (not published)
- 1ec0c69865d0408fa4f11752d5e10c3485202d85742cfd2658e7a378f8de8207 working file PROOF.md (not published)
- 48e64a92735a21299655089efb872bdddcd2bfaf66d34640471edc168a1f2265 working file PROOF.md (not published)
- 7239770df00ff938cdfd3eb926d23d3d5ba889b54790a42ac90ab612f4a634cb working file PROOF.md (not published)
- 8a97d1c987604ca5c786e44f0fd04aa4abce88760fc0f0da044004fc95dcffa3 working file PROOF.md (not published)
- 1dc8284fc54d24ed1fff21d3c4349aee7731d87247e5d1ca815cf47547880e19
  working file DISTANCE_PROOF_v02.md (not published)
- 2ce3839dd7db7d2ca351e53243bd3a6e9bf1d05e55b3a436c96dd1e0281b2f5a working file PROOF_v02.md (not published)
- 5ff46adee1191da1c3809e920f3ca13dffc5670a38d2f74c86a53a2805e7d3b7 working file PROOF.md (not published)
- af2715bfbf2369e02e6f1818bdc167de0f82a852c6584a2d707f8a662b0f7dab working file PROOF.md (not published)
- 1bca5f408ed60fc274cb98b067e6a925cba2dd927048ad5f9ef511c372f4aee8 working file PROOF.md (not published)
- fbb936cbf9dd27aa5b7cfa11c8fc9416893089f94a7268c29c590d982cf71f78 working file PROOF.md (not published)
- 1c0c4d2cc12729d6eb6a0420e6bda1b2180dcc72b9be77fe748379f99d9e6e5c working file PROOF.md (not published)
- 56ddc0b28ea714de41e3b7a66f7f3f7ab90bf1d7c881c56652e402f9cce8476a working file PROOF.md (not published)
- 1562433ed593d3f3163210a5736a2412bf140ef27aece407ba8cc5d6ba286f2b working file PROOF.md (not published)
- 8f226a5f1774418ff3e857a1be6b58047c9a3974be1c67d85c2b66ea6ba4c351 working file PROOF.md (not published)
- 276ac7ee13c84619d19179b40bf740adb701905103d1df1ed7cb3270c5850455 working file INDEX.md (not published)
- 927f13f5303198d430b46f39b8fc4d679c3556764ca1ce954ec6888975536e94 working file closure_matrix.md (not published)
- 20763c86645a954697bb617b57efc7d81f7afbbcd3aa173d5ee4d00d352bae9c working file numerics_v12.md (not published)
- 7ae8af1782e3d8e80205d16104dda60ee086152e87f074be8aaefba968b11952 working file numerics_v13.md (not published)
- 21c809ab7b3dbf7f1292013275a865aef5b6d28087346cb97c8393630960b15d working file numerics_v14.md (not published)
- 42eb222a38caadac911cffc261287892a9f18f60888f211f3e028f560508b320 working file theory_v07.md (not published)
- 82b4d9db1e5e25af3add32fedc87ae469191044735f2f749f4c80033c8f57451 working file THEORY_FINAL.md (not published)
- 8748b2950df75bd88aa4175dd2a3a6c1ab5e42a708012817a88caf95feacc664 working file check_T4458.out (not published)
- cb7eec586031b571ab022aef7337b2729fa3684b40188b7bf15b30b70483b1bc working file check_T4458.py (not published)
- c7cb5657de235ba3cc78a33bbd1b56a6b1c204064b01f352760ba2af68a71b5c working file check_T4462.out (not published)
- 6d8b95ec45526c1a97f914ae1257b05473d9a055b1e84a1e10dfd225c2ed7435 working file check_T4462.py (not published)
- b8facf4cbad2a03e3d37b0fe6052c01de232579c88f70e8086c6186842bad1c7 working file h18_verdicts.out (not published)
- e941a118de7f2e65a3c006a2c2d0facd9a78c3a7c214f3e4b2da53c1da4d3eb3 working file h18_verdicts.py (not published)
- 4ad9ac5a12f18621dbed9c620f07217dfbdfde24d3f4f9534dc0d250503585a6 working file v08_factors_007.out (not published)
- 2615c95aeb72c0cc5967d7a0a8d2d9e7de0a2700192fa1bb9fdd878d95727fcf working file v08_factors_007.py (not published)
- 93b48e74ace27c438b094520379d7d547640d377f22172c41593b531c05841bf working file review set 41 (not published)
- f4c2e3270bb971b8c0e13a14775741caadfb0ef3b2f3c4cc8a0658c0466dc5f2 working file review set 42 (not published)
- dcd62d661e4bb18b72277843a819d3574bf1a70332d546de09a0013f2bac66f1 working file review set 43 (not published)
- 1b7c425c77edfaade35aa73b5316a9fd3c4e1b052b56f6c8acfb446dbbb9a11d working file review set 44 (not published)
- b8771fb6432261ea60da9c8ccb00fabbc45b8687d25b7bdd2a87c0b38160fe4c working file review set 45 (not published)
- 1633cd35948398bc69d8b20f1f44ccb5e98fbd7e8ab94ae5f542c9fc6c978cac working file team note 47 (not published)
- 2db9ca22e2c15cdb08a0e7adeff61c86e5ac6a603f899546ccf1a96a619e4ee9 working file team note 51 (not published)
- 048db91f739d49a7ce616fc95a025a64fa7ba450a81df34d202c334fe52e17f0 working file T2_to_T1_v01.md (not published)
- 09e274f641119b9b8de9a378629d6a3e04537e5447b99de436038f8468e14d45 working file CHECK_T1_v08_FACTORS.md (not published)
- 660b089b8e6435065918f020a45d971cce4d82e8210675944322f3d7c47dd7f5 working file the T2 falsification review of the endpoint and the report summary (not published)
- de58845366cdfa397f0fb47e496db574aed2fa1a584c42c09962f6372d21dfc8
  working file the T2 falsification review of the endpoint and the report summary_NOTE_BE.md (not published)
- ffb49200aa1277900c8db4e7749a7a79a193d59ff4c3b0f514c190f22421c9af working file the review of T4-402 (not published)
- df28b508a9ba2da4ddd269d29125b8cf7df0950a6d7f5ebd83c48e2dff12bd11 working file the review of T4-410 (not published)
- 221b113543dc815315d771563c9c0b9618919663db794720f55887169221ab51 working file the review of T4-414 (not published)
- ee7b1b1b7d9bc92c2fba61324c25b39aa4178c75a42296bbe7b444c8959671e8 working file the review of T4-415 (not published)
- ca936460537bea92ba0b2e0ddd1add8af2614341b20f9e5613cd898d4660229a working file the review of T4-458 (not published)
- e140e6c03aa2ec4487ac18da011853e9819c387787aa48b5e4ecb4485052d87f working file the review of T4-459 (not published)
- 2cb6f7e6aaf78a3fda6ef5c39e500669e4bc4e913079380a53d99598dcbd7da0 working file the review of T4-462 (not published)
- 4c5a9a7d5e8e68db8b9686a7ef4cdd29b2e7f741872b35a5f631ba6a7da7e8ad working file team note 247 (not published)
- 0299dffefd79168135219839d28b7890dc1ebd4c4d23f94441f9989b02c32b09 working file verdict ledger (not published)
- 00f281c080c5ee4af1b3d12f30bb2681b97789e16ff2c4544357124ca226bea0
  working file ERRATA_v01.md (not published)
- 771ad6b4af564e1b3a0acf1284184fd8f36c15d2dd090212370122d433789a3e working file PROOF.md (not published)
- a3dbba66ab10ccb3be109e9c9afd3dfbfb545397ed10e18bd96c58562fdc3083 working file PROOF.md (not published)
- 27cd1dc8f365f769542257c309a0fb5a602da580985487c8cb269e09abb0c163 working file PROOF.md (not published)
- dae8594bf2eee8cd5b9bf6d9356b1be9b34a3fe51c5c95440202dffb813fd39b
  working file PROOF.md (not published)
- 05028d893c13ae9a813a63a8d720ec8cba770aa52bbe96b096a54f4b77180941
  working file PROOF.md (not published)
- 0e32cdb67612d8d6ca21188aaae63c5f9fda2e096f920633ff319bd9457e399d working file PROOF.md (not published)
- ec364dc7a9be28ef0c9b3795c1ca367cbbccd96c0ff0b1ca7643fd95b5b55609 working file PROOF.md (not published)
- 1ad317d8290220cb417ea3e5ecbdb82760e31ae0a0cb8e85f1690a26aa82cbdb working file PROOF.md (not published)
- 025500c420e787e4f8c072f54dbc15e04215559065998fa1c53348d6f9a43ba6 working file PROOF.md (not published)
- b7848590e905055458f72616a9d27f55a30c68c9b3c47203f0bdfccfb5457b44 working file PROOF.md (not published)
- 5b8f6a0736b5b28bd51753fd617b68314df9f39a350b97124fa38e521ed09cfa working file PROOF.md (not published)
- b151176fffd242583f9fee5ece5d5acd8e948788774575f8e180b01fb8c2d357 working file PROOF.md (not published)
- 9801f71f1a470e080a325204c1c84cfbaab479e030d51288fe43d1d9243c29ac working file PROOF.md (not published)
- 5cb2e5fe0e0a36186bb6e8d892f7720e5d27ce6a6bd1710d5ac0289a541e42dd working file PROOF.md (not published)
- 7e76ce5e6951dd47249c17687d5d664f1da3b09dca8c05cf902465c58ea4c7fc working file PROOF.md (not published)
- d0b409da2c491469be4e3d4333251bf2af614691395d95804c52ce9ac18f8cc3 working file PROOF.md (not published)
- 88b01d4f5e77b8abb91eabf30ca6d8b8161346f5fd988589b25580ec35c7f821 working file PROOF.md (not published)
- 630ccc8cbbd1e1128dc75cb8778b0755dfd63ee3284d475f70bfb930ef84689f working file PROOF.md (not published)
- 6d795defef60a41d14b32c2ff77ce03bb3a8666e894e7e7be38802148b3ab04f working file PROOF.md (not published)
- 88b9c219728bb13448468ca5d064a0262f6b0cc55d8a73cbeee187e28b2213bf working file PROOF.md (not published)
- b4257d03f59aeee241404a618c7d16b6c07716fc5e521bbb42804dbb53069f20 working file PROOF.md (not published)
- d7689362724aa9ac9c3de761a54e75173bef191ae9d76c583e8a9a643ebaef46 working file PROOF.md (not published)
- 3d1d4bad28cebe297fa3207a936764faa7147732062a0c4f730c3809fbf8049c working file PROOF.md (not published)
- 41e5dff47ecf8fb11dc075b6a0a6a7e29cbc306e5aeb67be19dbd9d702978934 working file PROOF.md (not published)
- 78f0caa4275f993e35dd94b409df00600ee4123bfb81d6c6378d4ec6f871db69 working file PROOF.md (not published)
- 97d9a73864ad89d86602c7c1f56cf844b9e8e38d96c0b285316bb224e77575dc working file PROOF.md (not published)
- 042beeb993874daf236c7423c1a1546b7c57c307555c9fe252c189a93932bfd8 working file PROOF.md (not published)
- 45e743dd2ef7ac929a5a4f8b5ec89c8e0dfb0c480e8ae164f909ae8c10840037
  working file ERRATA_v01.md (not published)
- efabe956aa103859e42f8240f270217a1738a732d590d0dd1f01be11377c2cbf
  working file PROOF.md (not published)
- 85e01f1bfab61b078138120f3ec6011b76ace5cd45d7436d7cdd5ca35251fc34 working file PROOF.md (not published)
- 88b0ac35e46072242a94e57b198470d16b100a8bd77b744bf626e18f8d35c4f6
  working file PROOF.md (not published)
- 4fcfd14192b17ea5816132716b3ded2fbbdb3cbe0ae81ca217cd3f3d67a7a92c working file PROOF.md (not published)
- bba858593cf8d4c98d2e8a430dbf6751bd151767ecc5452e14e64e0eebf1c53a working file PROOF.md (not published)
- 972ac08e7af8600550f83cbc03e8e6bf327fc166ebcb2eea91f881506ae56c6a working file PROOF.md (not published)
- e72bc63bf849a60c5d7df86317d012c78c57a5f2f984f79c65809fb0fa874426 working file PROOF.md (not published)
- 9afe571d5720f1bc304c712c8fb4331ca148f83bcc55f842f06abc4943ae2330
  working file PROOF.md (not published)
- e6f9f4e3cd51e7c434bb337489901a40be6dbd7782df3a14f859ca4e7415621d
  working file PROOF.md (not published)
- 353fc1575bccca1927be976d646b9ff886ee5fb87c99a090c8fce0c0b3d9f650 working file PROOF.md (not published)
- 4daf08a6a8b3e769fee56cc450d5a5490693ce2c12c829033b4cf1ca82e29d6f working file PROOF.md (not published)
- 3a1dd3017e44b9cfd57bca4a6ac19f08f4603622715e64dfc30d54b696149474 working file PROOF.md (not published)
- 99aa80a9b5ce0474e26c8a53e53218b2b1bb628f0283eab5eb62b4aeefead6df working file PROOF.md (not published)
- 488b4a7207c8cb917cce25b674bfac8dcdcbb40326318551ec115ebc14858668 working file PROOF.md (not published)
- 026501ef13ee36ddf79f98725e55c32d204d2c0639d41afdbef9a36e0346dc26 working file PROOF.md (not published)
- 935e166fdaaf4d79fbb421117803cc780845bb30d9ab02bbcbf43b6da3234aa4
  working file PROOF.md (not published)
- fb03764b22fd8ab33a6da10b2422d0678a36bc3951fc2fac643204a3f2b45302 working file PROOF.md (not published)
- 8848da16d556cb0089a56a3fb41d09f9b98dc3a2e0d4985843f59300e0075674
  working file PROOF.md (not published)
- 57110fd5b3c62f0fa06b6e6194c53e6d9cf1fac091e89a8a3cd514f38ac9fab6 working file PROOF.md (not published)
- 865eb8423aeae53ee84452d8fcb06348d2829c295f913578ec1eba009e7d5232
  working file PROOF.md (not published)
- a98e64b04a4ab8f8e46f311c028d55138e9483f761d84e140ed550066e5ab3d9 working file PROOF.md (not published)
- 3f5da5310fccb4feb8dd117dcd4b9f1789e3eccda089a9bdc5d79dc8ba14d32e
  working file PROOF.md (not published)
- 0e0f608d167b2c3453568d06ccc4ba8319e67e5c2d066e4c4ee6854c8fb3a66b working file PROOF.md (not published)
- 5720a3c058165143cbc622f7de0806c95a44860979da73bc3a611d7af4b37304 working file PROOF.md (not published)
- c2035403ef932424d6fc797376675919702bae7f86ef3c46ce0874af29fc4e8c
  working file PROOF.md (not published)
- 4d13c623b32b738f78fe7963b67fe4548b5617f24b839be5dc2fe35383155bf3
  working file PROOF.md (not published)
- 3e9793dfb4e539a225a70d554d6cd3814aae068d654754b306d340140a8edecf working file PROOF.md (not published)
- 8f6f8232bc5660c56ec7765349794eb5e66a9f8c386e5a68bbc38b67442cf502 working file PROOF.md (not published)
- 6d890545d3384c2e8c0d407d693dda837b4cad7b25d5498fa393c0ec10285399 working file PROOF.md (not published)
- a2319328ba7b3fdb59d460237483c016accc38eaf6ec27127e4b7a6d51033d6d working file PROOF.md (not published)
- 644e6d03ba403ff966c50b1b8c72b51f71e6fde41af63c9a47de672cc3c1cc85 working file PROOF.md (not published)
- b7c3e467fdc2a8cf664453730a84c2dd49122063bc5459ef9fcd2b8abc92e48d working file PROOF.md (not published)
- 0eb9308dea16756f9896dff4c1ea5b438c9075517adf35b1d9742778372f1ca0 working file PROOF.md (not published)
- 8c1b6532cf66d1c05fe5a919c92dfe8b3233e1ba37697816c0b2222c6ab8ea07 working file PROOF.md (not published)
- 93f001802c42ef67be3f4ddfdd599b299dec0c57d8637a86d6c6e7f289e317a9 working file PROOF.md (not published)
- 0c2d360a304f04f5b022144f7d9c42b3b681fa4dab3a00de68a5de4d27f04ceb working file PROOF.md (not published)
- cd2e6f18fb4b9255503e988e220709cb258338a8b4829080910ca8a11797bde6 working file PROOF.md (not published)
- ca0e008a1bfb7868fb1242af0a0eeb1897552a574dc27f7b1a9ad36e1a0b30b9 working file PROOF.md (not published)
- 3c871d7f9ef82ba6b6fb925cf73a31cda678805cadc2c8a91f9659b2e2f3030c working file PROOF.md (not published)
- 5dd594c0b033ce0a2b7d6bcb9343d5aa1b18ab2357f615c86e6ae719b49bb487
  working file PROOF.md (not published)
