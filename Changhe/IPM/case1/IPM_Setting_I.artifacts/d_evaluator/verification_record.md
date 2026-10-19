# VERIFY_REPORT (verifier, independent verifier)

T0 (team run start) = 2026-10-17T17:37Z. This file lists every item checked, the method, the result and a verdict
(CONFIRMED / REFUTED / OPEN), with dates (UTC). Newest items are appended at the end of each section.

## Summary verdict (current, 2026-10-19T04:04:12Z, amended 2026-10-19T05:03:25Z, 2026-10-19T06:07:04Z, 2026-10-19T06:24:07Z, 2026-10-19T06:36:25Z, 2026-10-19T07:16:23Z, 2026-10-19T07:55:35Z, 2026-10-19T08:10:51Z, 2026-10-19T08:21:40Z, 2026-10-19T09:36:24Z, 2026-10-19T10:11:06Z, 2026-10-19T10:20:58Z, 2026-10-19T10:27:49Z, 2026-10-19T10:29:16Z, 2026-10-19T11:07:17Z, 2026-10-19T11:24:14Z, 2026-10-19T11:31:18Z, 2026-10-19T11:34:50Z, 2026-10-19T11:49:50Z and 2026-10-19T11:59:41Z)
- Candidate: X3 = c6g (375 radial functions x angular cap m <= 200, c_l held at 5.5753626), designated by the
  pre-registered rule (G74). On my generator and full-plane inverse: whole-box N_f 6.83e-7 to 7.16e-7 on N16875 q512,
  N16875 q768, N22500 q512 and 6.60e-7 on N22500 q384 (sampled maxima; maximum next to P), N_v <= 2.01e-7 for r <= 1000 [2.0e-7 corrected to 2.01e-7 in G145 (b)] and 1.07e-6 to 1.09e-6 (y-axis columns excluded; 1.09e-6 to 1.111e-6 on all columns, G145 (b)) in the far field beyond the
  inverse domain (no fit rows there), J 1.39e-6 / 1.60e-6 (eps 0.03 / 0.01), identity c_l to 3.2e-9, h(P) - 1 at my grid
  error, x* 8.6000638.
- Endpoint (G120): the YES endpoint for P_2, as numerical evidence and not a proof, meets the standard as written, on the
  conditions C1 to C8 of G120 (C3 amended by G123 and G126; one clause of G120 (3) corrected in G129). DONE was OPEN until
  I had audited the text that carries them; it is given in G152 (last item of this block). FINAL_REPORT 822f368d (G128, G131): C1, C2, C3 and C7 MET. Rounds A3 to
  A6 (d569d377, abb3e037, 654b09d5, b74e084a; G131 addendum, G133, G134, G136) CONFIRMED; the F1-schedule correction of
  G133 (j) is in b74e084a (G136). Round B (50bec0ba, G137) and round B2 (ad925d3f, G138) CONFIRMED; the two G137
  corrections are in. C4 MET on ad925d3f. Round D (e4ca7b49, G141) CONFIRMED except one clause of 4.4 (lines 1337 to
  1338, "flat to 3e-4 ...", to be reworded or dropped); C3 met with rows 49 and 50 included. Round E (35da90ae, G142)
  CONFIRMED except the new 4.1 sentence (lines 809 to 812): it needs the y-axis-column convention and must drop the count
  "Four rows" or name all eight rows continued beyond X3's budget that are lower in whole-box N_f. Round E2 (2fd94697,
  G143) CONFIRMED: both corrections are in, C3 MET on 2fd94697.
- c_l is not determined by the residual at this level: fixed-c_l rows on 375 x m <= 150 at equal budget are not excluded at
  every tested value in [5.5524653, 5.5793640] (G109, G111, G115, G118, G119, G123, G126), 5.6004662 is excluded at this
  level (G114) and at m <= 200 (56, G135). The lower end is bracketed at this budget by SPEC v4.15 (row 55 above row 54 in L2 and whole-box N_f on both
  configurations; row 55 not flattened, G126). Among the tested rows the L2 objective is smallest at 5.5604082 (row 54) and
  the residual maxima at 5.5683739 (row 53). F2's free c_l is set by its start at this budget (G117). (P1) family and (P2)
  isolated profile are not separated; the nested pair 56 / 57 on m <= 200 (one refinement step) reads "undecided" by the
  rule fixed before the runs (Q_200 = 1.680; G135). On m <= 200, 57 (5.5683739) has L2 0.820 x X3 and N_f next to P 0.59 x X3.
- Row 49 dom9000g2 (G139): "the budget does not lower the 9000 L row's far band further" (1.028 / 1.024; C at the axis
  1.015); near-P 0.61 / 0.58 and J 0.58 / 0.54 of dom9000g, without attribution. Not a candidate.
- Row 50 c6h9000 (G140): (a) "the interior gain of the m <= 250 cap is kept with rows to 9000 L" (1.021 / 1.023; near P
  0.665 / 0.712 of c6h); (b) far band 1000 L to 9000 L 0.61 of dom9000g2 on both configurations, stated (outside [0.8,
  1.25]); the difference sits next to the y-axis at the inner end of the band. Not a candidate.
- Rows 58 / 59 (G147): "kept at twice the budget" by SPEC v4.18 (L2 59/58 1.0051; whole-box N_f 59/58 1.152 and 2.062).
  The L2 margin shrank at every linearization (5.63e-7 to 1.12e-8), so the order is a fact at 43000 iterations only.
  58 (5.5604082, m <= 150, 43000 iterations) is below X3 at 16875 x 512 (whole-box N_f 0.92, near P 0.75, J 0.80) and
  must be named in the 4.1 bullet of lower rows. Not candidates.
- External checks (G145 astra fin9, G146 astra repro9): required wordings G145 (a), (b), (d); repro9 reproduced md5,
  identity, h(P) root, x* and centre defects from the artifacts; scans failed only at its 2 GB cap; my wrappers fixed.
- FINAL_REPORT 34d41433 (rounds F, F2, C; G148): CONFIRMED except three required corrections. (1), (2) The bounds
  7.2e-7 (N_f) and 2.01e-7 (N_v, r <= 1000) of 4.1 hold for my canonical evaluator only; the lead's scans of section 5
  step 3 read the fit's own convention and print 7.27e-7 and 2.04e-7 at 24576 x 960 (6.94e-7 and 1.94e-7 at 32768 x
  640); 4.1 and step 3 must say whose reading each value is. 1.112e-6 and 1.324e-7 bound both evaluators. (3) Two
  errors of my own G147 (d) are in the text: the 4.3 sentence "each of the last four linearizations" (the last, partial
  one reduced the gap by 5.9e-9, less than the 1.12e-8 left) and the 4.1 ratios 0.925 / 0.775 (exact 0.924 / 0.774).
  Errata to G145 (b) (my "required" 1.111e-6 / 1.323e-7 were below my own maxima; the installed 1.112e-6 / 1.324e-7 are
  right).
- Peak memory (G149): gen_audit at 16875 x 768 needs 13.8 GiB resident (the maximum of steps 1 to 3); all steps ran
  under ulimit -v 16000000 and reproduced the stored outputs exactly (stored in my record, not in the artifacts; G151).
- FINAL_REPORT e240e4b6 (rounds H, G; G150): the four G148 corrections are in, CONFIRMED; the memory sentence of
  section 5 CONFIRMED for its values, its scope over three unmeasured step-1 configurations OPEN until G151 (running).
- Remaining step-1 configurations and C8 audit of f6a93ab4 (G151): 16875 x 384, 16875 x 512, 22500 x 384 need 7.0, 9.2,
  9.2 GiB; 13.8 GiB at 16875 x 768 is the maximum of steps 1 to 3. The stored outputs of steps 1 and 2 are not in the
  artifacts (d_evaluator/runs is empty) and 16875 x 384 had none: required (R1) ship my ref_outputs/c6g as
  d_evaluator/runs/reference (INDEX, 5 (d)), (R2) the section 5 memory sentence as worded in G151, (R3) an appendix
  entry, (R4) the SPEC status wording on D9. Everything else of f6a93ab4 CONFIRMED: finalize step, banner, Summary,
  T_end 11:34:31Z / 41.96 h, PROMPT mapping (6, 14, 25, 62, 104 to 111, 115, 121 MET), C1 to C5 and C7 MET, C6 MET on
  the 11:36Z tree (manifest, code, smoke tests) with (R1).
- DONE (G152, 2026-10-19T11:59:41Z): FINAL_REPORT 1daeb3b3 (T_end 2026-10-19T11:50:47Z, 42.23 h) differs from f6a93ab4 by (R1) to
  (R3), T_end and the elapsed time only; the tree of 11:50:58Z (1449 files, manifest checked) has runs/reference and the
  (R4) SPEC wording. C1 to C8 MET. The YES endpoint for P_2 (numerical evidence, not a proof; P_inf not answered; c_l
  not determined beyond [5.5524653, 5.5793640] at the stated budget) is CONFIRMED as meeting the standard of G120.
- The team may finish.

## Summary verdict (2026-10-18, superseded by the block above; kept for the record)
2026-10-18T00:01Z, amended 2026-10-18T00:20Z (c_l bullet, G31; FINAL_REPORT 00:08Z audited, G32) and 2026-10-18T01:03Z (FINAL_REPORT
00:43Z audited, G34; c6a segment 1, G35) and 2026-10-18T01:42Z (c6b intermediate, G39; external index count, G38, OPEN), 2026-10-18T02:17Z (analysis 13.10/13.11, FINAL_REPORT 02:06Z, G41), 2026-10-18T03:18Z (c6b/c6c segment 1, G42; lead B_3 ibp, G43; FINAL_REPORT 02:49Z, G44), 2026-10-18T03:46Z (numerics-lane exports and m(s) curve, evaluator tail exponent, G45; FINAL_REPORT 03:36Z, G46), 2026-10-18T04:35Z (cost of c_l offsets along the numerics direction on c6c, the lead's fixed-c reading rule, G47), 2026-10-18T04:56Z (c6d segment 1, G48; c6b tangent shapes, G49; SPEC v4.5, G50), 2026-10-18T05:24Z (c6c plus the 244 tangent, G51; numerics (256,128) fixed-c states, G52; analysis 13.12, section 4 draft 04:43Z and FINAL_REPORT 04:47Z, G53), 2026-10-18T05:54Z (fixed-c 5.60 start and first check, G54; FINAL_REPORT 05:28Z, section 4 05:28Z, analysis 13.13, G55; c6d plus the 244 tangent, G56; c6f iteration 500, G57), 2026-10-18T06:19Z (coefficient-level 244 direction on c6d, G58; 4.3 paragraph, G59), 2026-10-18T06:34Z (c6f segment 1 end and fxs1 transplants, G60, intermediate), 2026-10-18T06:54Z (c6f grid spread, angular structure of the strip, cd-file h(P), G61; section 4.3 version 2, G62), 2026-10-18T07:46Z (fixed c_l 1e-3 below on c6f, iterates 250 and 500, G63), 2026-10-18T07:52Z (domain study dom300 / dom100 in the fit's closure convention, export convention, closure-radius point, ray check B, G64), 2026-10-18T08:00Z (quick_scan convention for domain fits, dom90 rule, ray check C, analysis 13.15 (c), FINAL_REPORT 4.3 and timeline, G65), 2026-10-18T08:33Z (lead analysis 13.16, structure of the fits at P along the characteristic, G66), 2026-10-18T09:05Z (final fixed-c_l fit fixc_c6f_m1.0e-03, equal-budget control at 250, y-axis evaluator floor, SPEC v4.7, G67), 2026-10-18T09:14Z (inverse-error row, closure row of the fit inverse, lead reading rules, section 4 draft v3, G68), 2026-10-18T10:51Z (c6f segment 2 iterates 500 / 750 against the fixed-c_l fit, M2 rule, J on resolved label sets and the axis integral, dom90 segment 1, closure row direct, 244 free part, section 4 v3 wordings, G69), 2026-10-18T12:09Z (dom90 segment 2, fxd1, fxd300, cap ripple, G70), 2026-10-18T12:26Z (J band split, q0 next to P, fxfr1, s2w1, G71), 2026-10-18T13:41Z (the decisive pair s2g / seg3g, free-branch J, q0 at N33750, G72), 2026-10-18T14:39Z (c6g start and first iterate, q768 rows of the pair, configuration spread of the near-P maximum, G73 intermediate), 2026-10-18T15:31Z (c6g end, A5 rows on the decided pair, equal-budget angular row, G73), 2026-10-18T16:44:56Z (c6g / c6gF pair, candidate c6g, B_3 and q0 on c6g, G74; the q0 range of G74 (k) corrected at 2026-10-18T16:52:02Z), 2026-10-18T16:55:17Z (pre-audit of section 4 v5, J extremes on X3, G75), 2026-10-18T17:22:16Z (formal audit of section 4 v5 full, G76; item (a) corrected 2026-10-18T17:42:13Z), 2026-10-18T17:35:12Z (dom90g domain column, G77; off-axis 10-100 addendum 2026-10-18T17:48:26Z), 2026-10-18T17:36:19Z (FINAL_REPORT 16:53:20Z timeline diff, G78), 2026-10-18T17:50:01Z (fit rows end at 900 L, G79), 2026-10-18T17:58:16Z (c6g baseline for the dom9000g far-band reading, G80), 2026-10-18T17:59:17Z (far-field first-correction identity, algebra, G81): no endpoint is confirmed,
and the team may NOT finish. The 24-hour minimum is not a gate (SHIFT_PROMPT line 5;
G20 (0)). The report must still record T0, T_end and the elapsed time truthfully.
- Best candidate now (G42): c6c segment 1 (302 radial functions; lead/work/c6/c6c_seg1_shape.npz). Between nodes, my
  generator and inverse at R 7.652e6, N 11250 to 22500: flux max 2.3e-6 (2 <= r <= 10, |X - P| < 0.5 and 10 <= r <= 100
  alike), N_v max 8.3e-7 for 2 <= r <= 10 and 1.41e-6 overall (far-field angular ripple), J spread 1.2e-6, h(P) - 1 about
  -2e-8, c_l 5.5763609 (identity). c6b segment 1 (244): flux 4.6e-6, N_v 1.4e-6, J 3.3e-6, c_l 5.5763632. Lead scans agree.
  Remaining limits on the 302 basis: the angular band edge (m <= 100) in a strip next to the x-axis left of P (2.2e-6,
  N_f) and in the far field next to the y-axis (1.4e-6, N_v), and the unrefined radial band 9.7 <= r <= 11 (2.3e-6). The
  G36 knot reading holds for the stem component (factors 3.9, 4.7 per halving) but not for the near-P maximum as a whole
  (1.46 at the second halving). Not YES-level (G20 b1: about 1e-6 in both normalizations).
  c6d segment 1 (375 radial functions, G48): the band 9.7 <= r <= 100 falls to 8.0e-7, but the near-axis strip rises to
  2.44e-6 (flux, N 22500), the far N_v to 1.456e-6, and J to 1.46e-6. h(P) - 1 is -2.0e-8 and c_l 5.5763622. It is not
  better than c6c in the global maxima, and the G42 (c) prediction is CONFIRMED.
  Lowest field so far (G56, field level, not a basis shape): c6d plus -1e-3 times the 244 soft tangent (c_l 5.5753622):
  global flux max 1.8e-6 (0.73 to 0.74 of c6d at N 16875 and 22500; the axis strip falls), J 1.0e-6, far N_v 1.40e-6,
  h(P) - 1 +5.3e-8 (N 22500). c6f at LSQR iteration 500 (angular 150, G57, intermediate): every band away from P falls
  (10-100 4.4e-7, far N_v 1.14e-6, rms by 2), but the axis strip stays at 2.4e-6 and J at 0.03 / 0.01 rises by 2.1 to
  2.5. In the trial class (lead coefficient-level transplant, G58): c6d plus d t at d = -1.5e-3 has global flux max
  1.72e-6 (0.71), J 9.4e-7 (0.64), h(P) - 1 +2.1e-7 (N 16875). c6f segment 1 end (it750, G60): the same picture as it500.
  rms 2.4e-8, strip 2.44e-6 converged in the between-node grid (G61 (a); equal to c6d), J 3.1e-6 / 3.5e-6 (2.2x / 2.7x
  c6d). The strip residual oscillates just below the angular cap for m <= 100 and m <= 150 alike; the cap step removes
  it farther than about 0.3 from P, but its maximum moves toward P and keeps its value (G61, a reading). Not YES-level.
  Lead fixed-c_l fit at 5.5753626 (1e-3 below c6f segment 1), LSQR iterate 500 (G63, intermediate): between-node maximum
  of R/N_f 9.8e-7 (q512; 9.0e-7 at q384), J 1.35e-6 / 1.58e-6, N_v near P 2.8e-7, far N_v 1.11e-6, h(P) - 1 -1.7e-8; its
  L2 objective is 12 percent above the free fit. It is the first shape below 1e-6 in R/N_f everywhere. It is one
  resolution and one domain, an intermediate iterate, without its free control (c6f segment 2) yet. Not yet YES-level.
  Domain series on c6d segment 1 (G64, fit radii 1000 / 300 / 100 shape units, read with the fit's closure): c_l 5.5763622
  / 5.5763628 / 5.5763644, h(P) = 1 to 5e-8, near-P maximum 2.4e-6 to 2.6e-6, J 1.5e-6 to 2.1e-6. The far-field truncation
  does not limit the near-P residual. The export_fit.py exports of domain fits close at 1e4 shape units and are not the
  fitted field; for dom100 they give c_l +1.6e-6, h(P) - 1 +6.4e-6 and J 2.9e-5. The export U of c6d_seg1 agrees with the
  numerics lane's real-space inverse to 1.2e-8 relative (6e-9 in residual terms).
  The numerics lane's quick_scan.py closes every shape at 1000 shape units (G65): its dom100 rows (2x worse next to P, 4x
  at 10-100) describe the unfitted continuation, not the dom100 fit, and are REFUTED as dom100's numbers. In the fit's
  convention dom100 and dom300 are within 0.86 to 1.05 of c6dS1 inside their fit radii. The dom90 rule must be read in
  the fit's convention. Ray check C: near P 1e-9, r 100 5e-9, r 300 about 3e-7 (check-limited); impact at most 6e-9.
  Structure at P (G66, lead analysis 13.16): the fits' H''' (H = log a) changes by about +0.12 across P on the axis
  (estimator dependent, 0.05 to 0.16), within about 0.1 of P; it decays to 0 by xi = 0.2 (no plateau). Off the axis the
  feature follows the characteristic leaving P, and the step changes sign near y = 0.5 (about -0.4 at y = 1): not the
  profile of a single lambda-mode (heuristic). The fits are C^6; "not C^3 at P" is REFUTED as a first-line statement.
  Final fixed-c_l fit fixc_c6f_m1.0e-03 (G67, c_l fixed at 5.5753626, c6f basis 375 x m <= 150): N_f whole box 6.5e-7
  to 7.0e-7 over my six configurations (outside a y-axis evaluator floor column at M 959), N_v 1.13e-6 to 1.17e-6 (far
  field) and at most 5.7e-7 for r <= 1000, J 1.0e-6 / 1.2e-6, h(P) - 1 at my grid error, identity to 3e-9. First audited
  shape at the G20 (b1) residual level, on one basis and one domain. The strip falls by 3.4 in both N_f and N_v. At an
  equal LSQR budget of 250 the free continuation (c6f segment 2) lowers the strip by 1.51 and the fixed fit by 1.65, so
  the attribution of the fall to c_l is OPEN until the free iterates 500 / 750. Resolution and domain studies at this
  c_l are pending. SPEC v4.7 CONFIRMED with amendments A0 to A5.
  G68: the inverse-error row (5e-9 at r 100, 1.5e-8 at r 300, impact at most 3e-9, on c6d_seg1) is CONFIRMED with
  qualifiers. The fit's own closure at 111 L is 6e-6 at r 20 to 300 (numerics), so the domain columns test the closed
  problems; the audited residuals (inverse to 1e6 L) are unaffected. In the draft of section 4 the normalization
  sentence of 4.8 is REFUTED as stated (the strip factor is 3.4 to 3.6 in both normalizations; what changes is where
  the whole-box maximum sits). The verifier values for its tables are supplied.
  G69: at the equal LSQR budget of 750 the free control (c6f segment 2) has its strip maximum at 2.31e-6 / 2.27e-6 (M2,
  CONFIRMED), so by the 09:16Z rule the fall of the strip is a c_l effect at that budget (one pair, one budget, the free
  strip maximum not monotone in the budget). The free control is lower in J and in the L2 objective, the candidate in
  the strip, near P and in the far N_v: the two fits are not ordered, and A1 fails at 750. My 24-label J spreads were
  lower bounds: on 737 / 857 labels the candidate has 1.91e-6 / 2.74e-6 at eps 0.03 (G67's 1.0e-6 is corrected) and
  the free control 1.29e-6 / 2.27e-6. The largest J values come from R/rho on the x-axis between the origin and P (at
  most 1.04e-5 on the candidate, 8.0e-6 free) [corrected in G70: this holds for the family-B maximum only, and the
  maxima are 1.07e-5 / 8.2e-6]; the label-free axis integral is 2.04e-6 / 1.54e-6. The six section 4
  wordings of 10:24Z are CONFIRMED; the 4.4b label-set sentence needs replacement.
  G70: dom90 segment 2 and fxd300 are "agreeing" by the 07:23Z and 08:17Z rules (CONFIRMED, qualifiers in G70 (a), (e));
  fxd1 (m <= 100 at the fixed c_l) is 1.29 times lower next to P than c6dS1, and the step to m <= 150 (the candidate)
  lowers every band and the J spread (one step, unequal budgets). Next to the x-axis from r about 4 to P the residual
  oscillates at the frequency of the angular cap on both caps; q0 and I(eps) are differences of band parts larger than
  themselves, and I(eps) is not a proxy for the J spread. Section 4 v3: candidate column CONFIRMED, max |q0| corrected
  to 1.07e-5 / 8.2e-6, the 4.4b sentences on the J extremes REFUTED as general (they hold for the family-B maximum).
  G71: J on the family-A labels is carried by the residual at and above the angular cap frequency (CONFIRMED for c6dS1
  and the candidate as "k >= m_max"); q0 next to P reaches 1.3e-6 on [8, x*) (G72 (c): 1.30e-6 at x 8.35, resolved at
  N33750; below 1e-6 on [8.4, x*)). fxfr1 (free continuation of the candidate) and s2w1 do not replace the candidate.
  G72: the decisive pair of lead NOTES 12:02Z item 3 (20750 LSQR its each): by that rule s2g (fixed c_l) is the
  candidate of the pair: N_f 1.42e-6 / 1.44e-6 against seg3g 1.57e-6, N_v r <= 1000 lower, r > 1000 within the spread,
  857-label J 3.14e-6 against 3.41e-6; seg3g's c_l drift +6.9e-6 resolves no slope. This holds with the far band read
  as all r > 1000, the band the lead stated at 13:54Z after the rows; on the fit-region band 1000 <= r <= 1000 L
  s2g's N_v is 3 percent higher, beyond the spread, and that reading gives seg3g (G72 (a) addendum 14:07Z).
  Both continuations end with a near-P maximum about twice the pre-continuation candidate's (fxm1o2i250: N_f 6.5e-7 to
  7.0e-7, J 2.74e-6, N_v higher): the fixed-c_l one raised its own start's (to 1.42e-6), the free one lowered its own
  (F1, c6f segment 2 at 750: 2.09e-6 to 2.33e-6, G69 (e); seg3g 1.57e-6 to 1.64e-6). So the fits are not ordered, and
  the fixed-c_l continuation shows no systematic improvement of the maximum (G20 b1). Free-branch J at m <= 100:
  1.94e-5, 4.75e-6, 3.47e-6, 3.68e-6 for 215 / 244 / 302 / 375 radial functions (not monotone at the last step).
  G73 (intermediate): the m <= 200 start of c6g reproduces s2g on my evaluator; c6g after its first 2500 iterations has a
  near-P N_f maximum 0.70 to 0.72 times s2g's on the same configurations (1.00e-6 to 1.05e-6), J spreads 0.60 to 0.66
  times, far N_v 1.2 to 1.5 percent higher, and the cap ripple at omega 399. At q768 the pair reading s2g / seg3g is
  unchanged. Near-P N_f maxima carry a configuration spread of about 5 percent (s2g 1.42e-6 to 1.51e-6).
  G73 (c6g end, 20750 iterations): whole-box N_f 6.83e-7 to 7.16e-7 on four configurations (0.475 to 0.485 times s2g on the
  three common ones), N_v r <= 1000 1.9e-7 to 2.0e-7 (0.48 times), 857-label J 1.39e-6 / 1.60e-6 (0.44 / 0.46 times s2g;
  half of fxm1o2i250's), centre jet, c_l (identity -3.2e-9 from the fixed value), h(P) and zeros unchanged. Beyond r 1000
  it is 1 to 2 percent below s2g (A5 does not apply in the far field: the residual next to the y-axis there is not the
  evaluator floor, G73 (g)). Equal-budget angular row (2500 iterations from the s2g end): m <= 200 gives 0.71 to 0.72 times
  the m <= 150 N_f and 0.62 to 0.69 times its J. A5 applied to the decided pair leaves s2g / seg3g unchanged. c6g is the
  candidate if it wins its pair against c6gF (running).
  G74: c6g wins its pair against c6gF (step 32) by every part of the 12:02Z rule in every fixed reading: whole-box N_f
  0.83 to 0.94 times c6gF's on N >= 16875, N_v r <= 1000 lower, far N_v within 3e-9 (inside the spread), 857-label J
  0.937 times. By the 14:02Z rule c6g is the candidate, and the domain pair runs from it (dom_start.txt). B_3 on c6g is
  0.299 to 0.303 by the converged forms; the lead's integrated-form values (median 0.3077) are the unconverged end piece
  of G43. On c6g |q0| on [8, x*) is at most 1.07e-6 (spectral; the two-point Richardson is low by up to 6e-8) and is not
  below 1e-6 on [8.4, x*). fxm1o2i250's whole-box N_f maximum at N16875 q512 is next to P, 4 to 6 percent below c6g's at
  N16875 and equal at N22500 q512. Not an endpoint: domain columns, fxd1g and the report text are outstanding.
  G75 (pre-audit of section 4 v5, 16:48:02Z): the filled [P] values, the objective ratio (0.960 to 0.973 over 83 check
  points), the B_3, X1 and h(P) sentences agree with G74. Three corrections: the q0 range on [8, 8.52] (my error in G74
  (k), corrected there: 0.99e-6 to 1.07e-6), the I(0.03) provenance on F3 (-3.61e-7 is the lead's; mine -3.51e-7), and
  the J-extreme sentence (on X2, X3 and F3 the extremes are at family-A theta0 about 1.52 and family-B 1.555, not at the
  separatrix label, whose J is close to I(0.03)).
  G76 (formal audit of section 4 v5 full, md5 d5738bdd, 17:22:16Z): the lead's [V] items (a) to (g) are CONFIRMED
  except the attribution of the three-point modal inverse (the referee's, not mine). 29 text
  corrections are listed (margins are not about 6 percent in every norm, far N_v has none; F1 row values; the B_3
  range over 136 audits is 0.296 to 0.302 by the converged form; several provenance and configuration points). Four
  of my own earlier wordings are corrected (G73 (c), G73 (h), G75 (e), E10 / G74 (i)). G20 (b4) OPEN; [A], [D], [TBD]
  rows wait on dom90g / dom300g and the m <= 250 row.
  G76 addendum (2026-10-18T17:42:13Z): item (a) corrected. The r <= 0.1 value 2.3e-11 is the lead's scan (work/c6/c6g_scanfit.json), not
  an inverse-impact value; my map of r <= 0.1 gives 2.43e-11 at the same place for pi/2 - theta >= 0.2, so it is CONFIRMED
  off the y-axis; within 0.2 of the y-axis my evaluator reads up to 4.95e-9 (A5), the lead's scan 3.1e-12.
  G77 (dom90g, 17:35:12Z): AGREE with c6g by A4 on my rows at three configurations (2-10 ratios 1.04 / 0.62 / 0.72,
  10-100 1.02 / 1.23 / 0.83 raw, 0.84 with A5; h(P) - 1 5.6e-8 and 6.8e-10 on N >= 16875). Near P 3 times lower, 857-label
  J 0.40 / 0.37 of c6g, lobe above P unchanged; domain and the 20750-iteration budget are not separated (dom300g is the
  control). Formula convention: near-P N_f 3.1e-5, h(P) - 1 -5.95e-5 (the lead's 2.9e-5 / -5.6e-5 CONFIRMED in size).
  G77 addendum (2026-10-18T17:48:26Z): off the y-axis the lead's 10-100 middle sub-band reproduces on my evaluator (c6g 8.18e-8 /
  dom90g 6.64e-8 at r 13.94, ratio 0.81; lead 7.99e-8 / 6.65e-8); within 0.006 of the y-axis mine reads up to 3.3e-7.
  G78 (FINAL_REPORT 16:53:20Z, timeline 15:31 / 16:44): "every band fell by about 2" is false for the N_v fit band (0.86)
  and the window above P; the c6g / c6gF whole-box ratio is 0.83 to 0.94, not 0.94; the rest CONFIRMED.
  G79 (17:50:01Z): the lead's fit-row correction CONFIRMED from centre_fit.py and c6g_shape.npz (rows r < 900 L,
  inverse domain r <= 1000 L, last interior knot 446.1 L; m <= 100 series 900 / 300 / 100 L, G79 (b)); my own "fit domain" for r <= 1000 L reads "inverse domain".
  G80 (17:58:16Z): c6g baseline for the lead's step-44 (b) reading: N_v 1.10e-6 / 1.09e-6 on 1000 L < r <= 9000 L,
  9.3e-7 on r > 1e4 L (band edge), N16875 q512 / N22500 q384; data, no verdict. Addendum: 900 L < r <= 1000 L 2.19e-7 /
  2.16e-7 at r 7644-7650 (the lead's 2.15e-7 reproduced).
  G81 (17:59:17Z): numerics referee's far-field identity (c_l - 1) B = k V_r A + V_theta A' and its axis limit
  -(k + 2) V_r/(c_l - 1) CONFIRMED as algebra under the assumed expansion; the c6g numbers built on it are OPEN.
  G82 to G92 (18:24Z to 20:54Z, digest; details in the entries):
  G82: own far-field inverse (code/far1_ver.py) closes the G81 item; prediction P measured on seven fits. G83: section 4 v5
  CONFIRMED subject to C1 to C8. G84: far-field third-order series by my own code (code/far2_ver.py), 4.5 bracket CONFIRMED
  with qualifications. G85: FINAL_REPORT port 308eeb82 CONFIRMED subject to a2; A4 is read two-sided (G77 corrected). G86:
  dom300g by two-sided A4: no domain column is worse by more than 1.5; at 16875 x 512 the 2-10 ratio is below 1/1.5 (lower).
  G87: c6g 9000 L-1e4 L baseline. G88: diff to 88f0ae94 CONFIRMED except the 4.5 decomposition sentence (REFUTED as
  written; my G84 (d) withdrawn). G89: fxd1g (m <= 100), every quantity decreases 100 -> 150 -> 200; full row waits for
  c6h (m <= 250). G90: diffs to 1f63bb44 CONFIRMED except three roundings and two wordings. G91: dom9000g (rows to 9000 L):
  A4 holds except 16875 x 512 on the low side (0.656); 1000 L-9000 L band falls to 0.028-0.029 of c6g's; r > 1e4 L does not
  fall in its own (closure) convention (24.7 times) and falls in the formula reading (0.035); C at the axis 0.035 of c6g's;
  not a candidate; budget and domain not yet separated (c6g2). G92: FINAL_REPORT 3b0d8888 (G90 items applied) CONFIRMED;
  the lead's dom9000g numbers CONFIRMED, near-axis ptest agreement OPEN on my evaluator (resolution), two wording limits.
  G93: FINAL_REPORT f66fa76b CONFIRMED except the timeline 20:44 sentence "not a balancing of higher orders" (REFUTED: on
  dom9000g the band value is about a tenth of its own first-order term, and q2, q3 changed with C) and one like-for-like
  comparison (N_v, not N_f, for the D_v-normalized ray impact); F3 band baselines; numerics X3 fit-convention ray data.
  G93 addendum: X3 closure row measured directly: absolute changes equal X1's to two digits (CONFIRMED); X1's percentages do
  not transfer beyond r = 10 (on X3 band maxima move up to 10 percent at 10-300 and 18-23 percent at 300-1000).
  G94: FINAL_REPORT 13845d9c (G93 applied, dom90g ray sentence) CONFIRMED; two optional precision notes; the G93 addendum
  item on 4.4 (X1 percentages) not yet applied.
  G95: FINAL_REPORT c2fd67e4 (G93 addendum and G94 notes applied) CONFIRMED; SPEC v4.9 section 8 record CONFIRMED except one
  omitted qualifier ("on both N >= 16875 configurations", 18:04:24Z item 5).
  G96: c6h (m <= 250 refinement row) CONFIRMED; the row 100 -> 250 improves systematically by the 15:14:26Z rule (raw); on A5
  values interior and J decrease at every step (c6g -> c6h near P 0.33-0.41, J 0.36), N_v r > 1000 flat (+0.2-0.4 percent);
  c6h's raw whole-box maximum is my y-axis floor column (scratch/axis_cols.py at M 959 / 1279), not the trial.
  G97: FINAL_REPORT c90fa579 (G95, G96 applied) CONFIRMED with four range or wording corrections in the c6h text (three of them
  correct my G96 wording: resolution agreement 3 to 21 percent, c6h / c6g 0.25 to 0.51 from 0.01 on, far maximum on the first
  or second column beyond the cut) and "0.2 to 0.5 percent" for "within 0.4 percent"; SPEC 00ed1007 CONFIRMED; c6h centre
  values (identity c_l, h(P) - 1, jet, zero set) as X3's.
  G98: c6g2 (budget row X3 + 20750, not a candidate) CONFIRMED: interior A5 0.61-0.77 of X3, near P 0.50-0.54, J 0.48 / 0.45,
  beyond r = 1000 and C unchanged (0.993-1.006, C 1.0026), so the far fall of dom9000g comes with its rows (21:10:51Z (i));
  (ii) dom300g's near-P gain is the budget's, dom90g 0.60-0.63 and dom9000g 1.25-1.27 of c6g2 stated; c6h / c6g2 lobe
  0.97-1.00, near P 0.63-0.82, bands away from P 0.38-0.54, J 0.74: the lead's equal-budget numbers CONFIRMED except the
  narrow "1000 L band" ratio (not on my bands).
  G99: FINAL_REPORT 4d36c535 (G97 applied) CONFIRMED.
  G100: FINAL_REPORT 9cd594cd (G98 applied) CONFIRMED with two wording notes (lobe 0.98 at 16875 x 512 only; "not inside
  ... on every configuration" for 9000 L); c6h's near-P maximum on the first column off the x-axis is a value of the row
  (2e-7 to 3e-7 on three angular resolutions, same sign), not a floor.
  G101: lobe phase scan: the lobe above P is common to X3, c6g2, c6h within 4 percent over four radial phases (spread 9-12.5
  percent per row); whole-box falls of c6g2 / c6h against X3 are the fall next to P; FR 4.4 / 4.2 / timeline lobe wording to
  correct (item 5 (b)-(d)); near-P readings phase-stable.
  G102: FINAL_REPORT 6b749206 (diff from 9cd594cd) CONFIRMED with two wording corrections (23:35 timeline 3.7 to 4.5
  percent; 4.4 the raised cap lowers the lobe by at most 4 percent).
  G103: B_3 on the rows (fxd1g, s2g, c6g, c6h, c6g2, dom9000g): ibp medians 0.2985 to 0.3012, original 0.3002 to 0.3044;
  unchanged to about 0.003 CONFIRMED (lead's numbers reproduced, same code and traces).
  G104 PRELIMINARY: c6hF / c6h on three configurations (A5 whole box 0.988 to 1.003, near P 0.89 to 0.97, far 0.996, J 1.019); OPEN.
  G104 (final): c6hF / c6h CONFIRMED as measured; by the letter of the 12:02Z rule c6hF wins on whole-box differences of 1 percent (unresolved); item 3 answer NO (J 1.019 to 1.026 and A5 far 0.996 beyond the spread); wording and the X3 / F3 A5 far clause requested; candidate unchanged.
  G108: c6gR4 (47) far band 1000 L-9000 L 0.266 to 0.273 of X3 on both N >= 16875 configurations ("falls"), C -0.024, q1 / q2 / q3 -0.027 / 0.113 / -0.373 of X3; interior = c6g2 to 1-2 percent; 4.5 wording corrections (closure with the inverse domain; decomposition 0.27 x 0.10; "and the inverse domain at 1000 L"); CONFIRMED with corrections.
  G105: absolute residuals were missing from FINAL_REPORT; X3 table of max |R| by region given; applied in fad52bb2 (G106).
  G106: FINAL_REPORT 4e8feb68 and fad52bb2 CONFIRMED in content; corrections: two formatting defects, all-column label of
  the 4.4 far ratios, Conventions sentence on absolute values, "to 6 percent"; sup|E| on 1 <= r <= 10 2.98e-5 / 7.86e-6 / 2.12e-6.
  G107: external referee ref7, 18 items: 3, 4, 5, 6, 13 CONFIRMED (R1 range of gamma, C^3 for R7 / R10, R11 finite zero
  set, |cos|, trial's own B_3 +0.046 not reported); canonical-law domain table (300 L / 900 L / 9000 L at equal budget:
  interior within 1.4, far band 3.5e-5 / 1.1e-6 / 3.3e-8; 90 L fails) proposed for item 7; the rest wording. OPEN.
  G110: FINAL_REPORT 516a80a8 (diff from fad52bb2, 17 items) CONFIRMED in content; corrections: 4.6 component tests are
  of the compactified discretization (replacement text given), 4.5 N_v near P "1.8e-7 to 2.0e-7", 4.8 "about one sixth".
  G109: row 37 fxm2g (d = -2e-3): L2 0.926 of F2, whole-box N_f 0.865 / 0.869, J 0.865 / 0.859, h(P) - 1 <= 2.8e-7: reading (a)
  "not determined at this level"; widens the c_l interval to 5.5743631; profile monotone over d = -2e-3, -1e-3, 0.
  G111: row 38 fxu2g (d = +2e-3): L2 1.078 of F2, whole-box N_f 1.138 / 1.138, J 1.159 / 1.160, h(P) - 1 <= 8.2e-8: reading (a);
  widens the c_l interval up to 5.5783631; profile monotone increasing in d over -2e-3 to +2e-3.
  G112: SPEC v4.12 CONFIRMED (v4.10 / v4.11 rules as applied; D12 correction rederived); precision: row exponents are
  5.5763624 + d + 0.18 d^2 (fxv24g 5.6004662, not 5.6003624); the report quotes the stored values.
  G113: FINAL_REPORT 5c15c44d (G110 corrections, row 37 timeline, B_3 identity with R10's H) CONFIRMED, items 1 to 6;
  identity rederived; g > 0 and the even expansions hold structurally and on the X3 traces.
  G114: row 39 fxv24g (d = +2.4e-2, c_l 5.6004662): L2 2.036 of F2, near-P N_f 2.915 / 2.914, J 2.871 / 2.938, flattened:
  reading (b) "excluded at this level"; Q = 2.036, undecided by the Q rule (4.8 wording: the test does not separate (P1), (P2)).
  G115: row 52 fxn4g (d = -4e-3, c_l 5.5723653): L2 0.858 of F2, whole-box N_f 0.711 / 0.713, J 0.707 / 0.699, h(P) - 1 <=
  3.6e-7: reading (a); widens the interval down to 5.5723653; lower end still not bracketed (row 53 running).
  G116: SPEC v4.13 (row exponents quoted as stored) CONFIRMED.
  G117: astra clprof checked: at equal budget and identical objective F2's free c_l stays within 1e-5 of its start while fixed
  rows below it reach lower objective, so F2's exponent is not a minimiser (CONFIRMED); (P1)/(P2) not separated by single-level rows.
  G118: row 40 fxu3g (d = +3e-3, c_l 5.5793640): L2 1.115 of F2, whole-box N_f 1.213 / 1.214, J 1.224 / 1.226, h(P) - 1 <= 5.5e-8:
  reading (a); interval up to 5.5793640; 5.6004662 excluded at this level (G114).
  G119: row 53 fxn8g (d = -8e-3, c_l 5.5683739): L2 0.741 of F2, whole-box N_f 0.566 / 0.427, J 0.388 / 0.375, h(P) - 1 <= 4.5e-7:
  reading (c) by the letter (below the 30 percent band); widens the interval to 5.5683739; below row 52 in L2 and N_f: not
  bracketed. At N16875 q512 its whole-box N_f is 0.984 of X3's and its J 0.95 / 0.88 of X3's (smaller basis, lower c_l).
  G120: endpoint statement: the YES endpoint for P_2 (numerical evidence, not a proof) meets the standard as written, on
  conditions C1 to C8 (4.1 wording, 4.3 F2 statement, rows and interval, (P1)/(P2) not separated, banner and T_end,
  artifacts, numerics spread, my audit of the final text). DONE OPEN until those are verified.
  G121: location of the whole-box N_f maximum: within 0.5 of P on both configurations for F3, X2, F2 and rows 37, 38, 39, 40,
  52; X3 at N16875 q512 yes, at N11250 q384 at the under-resolved lobe point; row 53 at neither (0.573 from P at N16875 q512).
  G122: SPEC v4.14 to v4.16 (rows 54, 55, nested pair 56 / 57, rules fixed before the runs) CONFIRMED; two wording points.
  G123: row 54 fxn16g (d = -1.6e-2, c_l 5.5604082): L2 0.643 of F2, whole-box N_f 0.716 / 0.485, J 0.514 / 0.522, h(P) - 1 <=
  6.9e-7: reading (c); interval [5.5604082, 5.5793640]. L2 below row 53, but N_f and J ABOVE row 53 on both configurations:
  the maxima are smallest at row 53 among the tested rows; L2 not bracketed (row 55 running). Above X3 in every maximum.
  G124: the C7 sentence (LM spread 5.5728 to 5.5823) matches NUM_REPORT 3.12; it must mention the excluded R = 30000 row.
  G125: dom9000gF (48, data row): free c_l moves -1.5e-6 from F3 over 20750 its with rows to 9000 L; far bands as dom9000g
  (0.025 to 0.036 of F3, formula reading); pair dom9000g / dom9000gF: near P 0.93 to 0.94, J 0.94, far bands 1.00. No decision.
  Open for the endpoint: c6hF (42), c6gR4 (47); dom9000gF (48) is a data row; the lobe phase scan of c6h.
- Previous best candidate: construct4 c4_r1 after its last chunk (18), which is also the start shape of the lead fit c6a (G28).
  Measured between fit nodes, on my own grids from my re-implementation of the trial formula:
  - near-P residual 1.8e-5 (flux, 2 <= r <= 10 band maximum) and 5.1e-6 (N_v); elsewhere <= 4.8e-6 (flux);
  - resolution independent to 3 percent; R = 7.652e4 and 7.652e6 for my inverse;
  - c_l 5.5763638 (identity, mine, R = 7.652e6), x* 8.600842, h(P) - 1 = -1.0e-6; the c_l root of h(P) = 1 with rho fixed
    is 9.5e-7 higher (1.7e-7 on c6a segment 1); D14 centre relations to 2e-8 relative; B_3 IBP 0.3013 [0.3005, 0.3024];
  - the lead's quick_scan of the same shape agrees to the digits shown (G28 (c)).
  - Continued fit c6a (same 215 radial functions, segment 1 final, G35): near-P flux 1.86e-5, N_v 5.2e-6, 10-100 band
    2.9e-6 (from 4.8e-6), J spread 1.7e-5, c_l 5.5763607. The near-P maximum did not fall: it is at a plateau for this
    basis. Fits with 244 (c6b) and 302 (c6c) radial functions are running in the lead lane.
  - Intermediate c6b shape (244 functions, LSQR iteration 500 of segment 1; G39): near-P flux 3.4e-6, N_v 9.7e-7, J spread
    3.9e-6, a factor 4.5 to 5.5 below c6a; the 10 <= r <= 100 band (2.5e-6, outside the refined knots) did not change.
    Not a candidate; the segment-end shapes decide (G36 prediction).
  This is a factor of about 7 better than c4_centre near P. It is NOT YES-level: the standard is about 1e-6 near P in
  both normalizations (G20 b1). Domain series (construct5, R_fit 200/300/900, G33): c_l agrees to 1.5e-6 across fit
  domains and the near-P residual is the same as on c4_r1, but those fits are at an earlier stage and their c_l is
  3.2e-5 below c4_r1's. The series does not include c4_r1.
- Decision test of analysis 13.4b (G28 (d)): from c4_centre to c4_r1 the J spread fell from 1.5e-4 to 1.5e-5 to 1.9e-5
  (by domain of my inverse), while the near-P flux maximum fell from 1.22e-4 to 1.7e-5 to 1.8e-5. J falls with the
  residual, as expected for a representation or solver limit. This is a consistency check, not a proof.
- Evaluator limits, to be stated wherever my numbers are quoted (G28 (b), (e)):
  - my inverse needs an outer radius R >= 7.65e4. Its domain error follows R^(2k-2) (analysis 11.1, G30): in h(P) it is
    1.6e-6 at R = 7.65e4 and about 1e-9 at R = 7.65e6, so I quote the R = 7.65e6 values;
  - bounded-domain fits (construct5) are evaluated with the lead's two-term exterior closure (G29);
  - my Poisson check relE on [r0, 0.01] (about 1e-4) is rounding error of my evaluator, shown on a manufactured field
    with E = 0. It is not a defect of the candidate.
  - the default far-field tail exponent is 1/c_l of a pass without tails; on fields with R of order 1e3 this is
    inconsistent by up to 1.8e-3 in k. The option k_self (G45 (d)) iterates it to 1/c_l; it changes nothing at
    R 7.652e6 and is used for all exports with R <= 7.652e4 from G45 on.
- Earlier candidates: construct1 final_candidate (Part 11; c_l 5.5763219) and c4_centre (G22, G26; c_l 5.5763301, near-P
  flux 1.22e-4) are superseded. The c4_centre centre repair (D14) is kept in c4_r1.
- Standards (G20, binding):
  - A second converged solver is not required. The independent check is my residual evaluator, the c_l identity, and a
    c_l determination that does not use the identity (b1 to b4).
  - The independent solvers did not converge to the candidate: plain DR is unstable about it (G15), and the numerics
    lane's states are at 1e-5 to 4e-3 between nodes with c_l off by up to 6e-3 (G16; with the consistent tail exponent of
    G45 (d) the G16 state has c_l 5.5786399, exporter 5.5786423). Their later exports (G45) are at 3e-6 for r <= 2 and
    3e-5 to 5e-4 next to P. This must be stated.
- B_3 (G17): the integrated-by-parts identity is CONFIRMED (condition beta != 1 added). The trial's w-only B_3 is about
  0.30 natural units in every variant (0.2997 to 0.3013 on construct4 shapes, 0.2957 to 0.2965 on construct5 (G33);
  0.316 on the numerics LM state). On c6a/c6b/c6c: 0.298 to 0.301 (my estimator; lead orig form 0.298 to 0.301). The lead's
  ibp end piece is not converged in the Gauss-Jacobi order (it grows like n^1.6; G43); its values must not enter a quoted
  B_3 or spread. B_3 of a true solution is OPEN.
- c_l (G20 (c) as amended by G31): across constructions 5.57624 to 5.57637 (c4_r1: 5.5763638, at the upper end). That
  is a variant spread, not an error bound. Along the c4_r1 fit c_l rose by 3.4e-5 while the near-P residual fell by a factor 7,
  and it was still moving at the end (G31). The c6a fit then moved it -3.1e-6 to 5.5763607 (G35). Fits whose c_l differs by 3e-5 have the same near-P maximum and differ
  by a global smooth deformation (G37): the spread measures reproducibility, not an error bar; if the exponent is unique, one of two fits Delta apart is off by at least Delta/2 (G41 (d)). c6b and c6c segment 1 ends: 5.5763632 and 5.5763609 (G42 (f)). A c_l bracketing test
  on the final basis is requested (G37). In the numerics discretization (near-P level 3e-5 to 1.3e-4) fixed-c_l fits over
  5.52 to 5.71 are equally good or better, and every near-P diagnostic improves toward larger c_l (G45 (c)); on their
  (256,128) grid the near-P diagnostics prefer smaller c_l instead and the zero of h(P) - 1 moves by at least 0.16 (G52),
  so that preference is discretization error; a 1e-2
  change along their cheapest direction is not detected (G45 (a)). That level is 15 to 60 times above c6c, so the test
  that decides is a nonlinear fixed-c re-solve on the 302/375 basis at c_l 5.60 and 5.65 (G45 (e)); until it is done, the
  uniqueness of c_l at the 1e-6 level is untested. On c6c segment 1, an offset of 1e-4 along the numerics direction,
  not re-optimized, is not detected for r <= 1000 or in J; only h(P) - 1 = -3.5e-7 separates it (G47 (d)). So any c_l
  uncertainty quoted at the 302 level must be at least 1e-4. The lead's fixed-c reading rule (04:00Z) is CONFIRMED with
  the corrections G47 (e1) to (e4): read h(P) in absolute terms; excluding 5.60 does not bound the interval; equal budget
  or a flattened objective; state the level. On the 244 basis the lead's tangent shapes at dc = -1e-3 keep every
  between-node maximum within 0.76 to 1.06 of c6b, with |h(P) - 1| 3.4e-8 and the objective +2.9 percent. The
  diagnostics prefer different signs of dc. So c_l is not determined to 1e-3 at the 244 level (G49). Unless the 302
  tests narrow it, quote c_l = 5.576 with an uncertainty of at least 1e-3 (244) and at least 1e-4 (302). Superseded at
  the 302 level by G51: c6c plus multiples of the lead's 244 tangent, as fields, keeps every between-node diagnostic within
  30 percent of c6c, with |h(P) - 1| <= 4.5e-8, for offsets -1.5e-3 to +3e-4 (N 16875, -1e-3 repeated at N 22500). So
  quote c_l = 5.576 with an uncertainty of at least 1e-3 at both the 244 and the 302 level. Along the 244 tangent the
  objective doubles at about 4.1e-3 once its measured quartic term is included, not at 9e-3 (G53 (b)). At the 375 level
  (c6d plus the same direction, G56) the max-norm optimum along this direction is about 1e-3 below the L2-fit c_l: the
  global flux maximum is 0.73 there. So the fitted six-digit c_l is not the max-norm optimum of the trial family, and the
  uncertainty is at least 1.5e-3 below and 3e-4 above the fit value at the 302 and 375 levels (field level).
  G58: in the trial class (coefficient-level transplant, unrefitted) the lower side at 375 stays inside every band to
  -2e-3, and the upper side leaves the J band at +5e-4. Field-level lines are first-order statements, valid to |d| <= 1e-3
  only. So at the 375 level the uncertainty is at least 2e-3 below and 3e-4 above, and it is asymmetric.
  The fixed-c 5.60 fit on 244 (G54, intermediate) restores h(P) - 1 to 1.3e-7; its reading waits for the flattened end and
  the ctrl_c6b control. The earlier quoting rule (5.5763 with the spread, or six digits with the disclaimer of analysis 13.11 (d), G41 (d)) is superseded by the G49 sentence above; the disclaimer is still required for any value with more digits. On each candidate the c_l from h(P) = 1 at fixed rho agrees with the identity value to 1e-6 to 3e-6 (G22, G28).
  This is a consistency check, not a second solver. Independent-solver agreement is only at the numerics lane's accuracy.
- P_2 (G18 as amended by G20 (a) and G25 (a)):
  - A full-standard result for the explicitly distinguished problem P_2 (rho in C^(2,alpha), rho = x^2 y a with a
    continuous) is an admissible endpoint, under the four conditions of G25 (a).
  - The first lines of FINAL_REPORT must say that the strong setting (a smooth) is not answered, and that B_3 is nonzero
    (numerical evidence that the branch is not C^infinity, not a NO theorem).
- FINAL_REPORT (mtime 00:43Z) and notes/final_sec4_draft.md (00:43Z): CONFIRMED (G34), with one wording note (4.4b) and
  one caveat: a closure-extended field is only C^1 across r = R_shape L, so it is not an admissible trial density and may
  be quoted only as a bounded-domain fit. The formula-global shapes (c4_r1, c6a) are in C^{4,beta}_loc, beta = p3 - 6.
  Earlier versions: G23, G27, G28 (f), G32. The G21 lemma is amended: it needs rho_y(x,0) > 0 on (0, x*) (G34 (b)).
- J and h(P) (G24): R/rho at P equals h(P) - 1, so J diverges logarithmically as eps_P -> 0 unless h(P) = 1. J is
  reported by distance shell (G25 (c)).
- Quadrature overfit (G22): improvements measured on a fit grid are accepted only after my evaluator reproduces them
  between nodes. For c4_r1 this is now done (G28), and the lead's fit grid sees the near-P maximum to 2 percent.
- Verdict OPEN.
- Audits are current:
  - SPEC v1 to v4.5 (Parts 3, 4, 10, 12, G35 (d), G50: v4.5 with amendments);
  - analysis.md sections 1 to 4, 7.1 to 7.3, 8, 9, 11, 12, 13.4 to 13.12 (Parts 4, 9, 12, G30, G34, G35 (c), G40, G41,
    G53: 13.12 (c) second claim REFUTED, (e) conclusion REFUTED, (f) incomplete; G55: 13.13 (a) to (c), (e) CONFIRMED
    with amendments, (c) "did not shrink" not supported; G56: 13.13 (d) premise CONFIRMED at field level on c6d; G58: 13.14 table and (d) reading CONFIRMED in my evaluator,
    transplant exact to 3e-4);
  - FINAL_REPORT up to 05:28Z and the section 4 draft 05:28Z (Part 6, G23, G27, G28, G32, G34, G41, G44, G46, G53, G55:
    05:06 and 05:16 timeline entries need small wording amendments); the proposed 4.3 paragraph of 05:55Z (G59: CONFIRMED
    with corrections, one claim REFUTED as worded);
  - the lead's B_3 tool notes/b3_ibp/b3_ibp.py (G43: ibp end piece not converged);
  - construct1 PROOF.md (Parts 7 and 11).
  - The Lemma 5 2D regularity claim stays OPEN; only "C^infinity implies B_3 = 0" is proved.
- Numerics lane timestamps (Part 5): P1, P1b and P1c RESOLVED.
Earlier summaries: 00:20Z (scratch/summary_0020.txt), 23:39Z (scratch/summary_2339.txt), 22:02Z (scratch/summary_2202.txt), 21:27Z (scratch/summary_2127.txt),
20:52Z (scratch/summary_new.txt), 20:11Z, 19:29Z, 18:28Z, 18:05Z.

## Part 1. Verifier tools (independent of the numerics lane)

T1. Polar-mode full-plane inverse (code/vpolar.py). 2026-10-17.
Method: rho = sum_{m odd} f_m(r) sin(m t), psi = sum_{n even} p_n(r) sin(n t) with the derivative-free Green formula
  p_n = (1/2)[ r^n int_r^inf s^{-n} f_{n+1} ds - r^{-n} int_0^r s^n f_{n-1} ds ],
uniform grid in u = log r, exponentially weighted cumulative quadrature (order 8, exact exponential weights), analytic
power-law tails at r < r0 and r > R; c = psi_xy(0) = int_0^inf f_3 r^{-2} dr (formula C3, derived in notes/analysis_v1.md).
Tests (code/test_vpolar1.py, test_vpolar2.py, test_vpolar3.py):
 - rho = x^2 y e^{-r^2}: p_2, p_4 vs closed form (incomplete gamma): rel. error 5e-13 at N=800; c = 1/8 to 6e-14.
 - same field: U vs FFT on periodic box [-60,60]^2 (2048^2): agreement 4e-8..2e-7 (FFT image/interpolation error level);
   -Lap psi - d_x rho = 1.3e-10 (relative to max|d_x rho| = 0.25) with independent 8th-order FD in u and spectral theta.
 - growing rho = x^2 y (1+r^2)^{(k-3)/2}, k = 0.6 (~ r^k at infinity): c = 1/(4(1-k)) reproduced to 2e-13 (R = 1e5);
   Poisson residual rel. 3e-12 on r in [0.01, 1000]; gauge: p_2/r^{1+k} -> const, p_2/r^2 -> 0, p_2/r^2 -> c/2 at r -> 0.
Verdict: CONFIRMED (tool validated) for data with growth k < 1.

T2. Residual evaluator, method A (code/vresid.py). 2026-10-17T18:10Z.
Method: rho samples on the log-polar grid -> U from T1; R = c_l r rho_r + (psi_r rho_t - psi_t rho_r)/r - rho with rho_t by FFT
and r rho_r by 8th-order FD in u; E = -(psi_uu + psi_tt)/r^2 - d_x rho with psi re-differentiated by FD/FFT (not the Green
formula's p_n'). Manufactured test (code/test_vresid1.py): rho = x^2 y e^{-r^2}, exact psi = p2 sin2t + p4 sin4t with
p2 = (e^{-s}(s^2+s+1)-1)/(8s), p4 = (e^{-s}(s^3+3s^2+6s+6)-6)/(16s^2), s = r^2, c_l = 1.3 (arbitrary):
  N=400/Nt=32: max|R - R_exact| = 6.8e-10;  N=800/64: 2.7e-12;  N=1600/64: 2.8e-13 (max|R_exact| = 0.485);
  max|E| = 1e-10 / 3e-12 / 7e-12; c - 1/8 = -6e-14. Verdict: CONFIRMED (tool validated).

T3. Method B: target-centered polar quadrature (code/vquad.py, GPU/torch, float64). 2026-10-17T18:12Z.
Method: weakly singular forms U_1 = -(1/2pi) int sin(phi) int_0^{L(phi)} d_x rho(X + t e_phi) dt dphi, U_2 = +(1/2pi) int cos(phi) ...,
over the centered disc |Y| < RB (trapezoid in phi, Gauss-Legendre panels in an exponential ray variable), plus the exact
multipole tail psi_tail = sum_n (r^n/(2n)) T_n sin(n t), T_n = int_RB^inf s^{1-n} F_n ds (radial GL quadrature to RF and an
analytic power tail). No modal Green recursion, no FFT on the disc: independent of T1. Tests (code/test_vquad1.py):
  rho = x^2 y e^{-r^2}, 64 targets in [-3,3]^2: max|U_B - U_exact| = 4e-17..7e-17 (max|U| = 0.054);
  growing rho = x^2 y (1+r^2)^{(k-3)/2}, k = 0.6, 24 targets r in [0.05,10]: max|U_B - U_A| = 7.9e-12 (max|U| = 2.4) for
  RB = 50, 100, 200 (the tail part changes from 1.03 to 0.60 while the sum is unchanged). Verdict: CONFIRMED; methods A and B
  agree to 8e-12 on growing data, which also cross-checks the gauge (both are the sublinear, symmetric-truncation inverse).

T4. Axis traces and B_3 by the finite-part formula (code/vb3.py; tests code/test_vb3.py, code/test_axis.py). 2026-10-17T19:07Z.
Method: from polar modes, G1 = sum m f_m/x, G3 = x^-3 sum[-f_m(m/3 + m^3/6) + x f_m' m/2], the same for Psi1, Psi3;
w = c_l x - Psi1, h = c_l + Psi1', W1_2 = -3 Psi3, W2_3 = Psi3', F3 = -W1_2 G1' - W2_3 G1. x* = first - to + zero of w;
mu1 = w'(x*), mu2 = h(x*) by local fits; p3 = (3 lambda2 - 1)/|lambda1| from the traces at small x. B_3 = f.p. int_0^{x*} J,
J = -F3/(w H), with both poles of (1-3h)/w (at 0 and x*) removed analytically before the spline; an even-polynomial fit of
J t^(p3-1) on [0.01 x*, 0.3 x*] gives the finite part at 0; Gauss-Legendre in log x in the middle; near x*,
J = (x*-x)^(kappa-1) Q with kappa = (3 mu2 - 1)/mu1 and the substitution x* - x = s^(1/kappa). A second estimate,
f.p. int_0^x J + G3(x)/H(x) at x = 0.3, 0.5, 0.7 x*, uses G3 and so checks the axis ODE.
Tests:
 (a) Manufactured axis data with known answer: x* = 1, w = A x(x^2-1)/(1+x^2), h = A+1-w' (mu1 = A, mu2 = 1),
     H = x^p3 |1-x^2|^(-2/A) (1+x^2)^(-3) exactly, G3 = x^2 e^(-x^2) + 0.7 chi H with a smooth cutoff chi (1 on [0, 0.32],
     0 on [0.78, inf)), F3 := w G3' + (3h-1) G3. For c_l = 1.3, 1.5, 2.2 and N = 1200, 2400: x*, mu1, mu2, p3 to 1e-7 or
     better; |B3 - 0.7| <= 3.1e-6; the second estimate agrees to the same level.
 (b) rho = x^2 y e^(-x^2-2y^2), psi = x y e^(-x^2-2y^2) (non-radial, many modes), M = 31 and 63: all traces agree with the
     analytic ones to 6e-7 relative or better (worst: W2_3 on [0.01, 0.1], which loses about 1/r^2 to cancellation).
Limitations found in testing: the near-0 and middle pieces cancel strongly (about 1e5 each when t_c = 0.1 x*), so
t_c = 0.3 x* is used; the end fit assumes the data are smooth on [0.9 x*, x*].
Verdict: CONFIRMED (tool validated). Written without reading the lead's scripts/b3_diag.py.

## Part 2. Verifier's own analytic observations (to be refereed; not team claims)
See notes/analysis_v1.md. Summary:
V1 (sign/kernel conventions): U = (-R1R2 rho, R1^2 rho); U_1^ = xi1 xi2/|xi|^2 rho^, U_2^ = -xi1^2/|xi|^2 rho^; checked numerically
   (T1, FFT comparison). CONFIRMED.
V2 (c_l identity): coefficient of x^2 y gives 3c_l - c = 1 (independently rederived), and c = psi_xy(0) = int_0^inf f_3 r^{-2} dr
   for growth k < 1 (formula C3). Numerically confirmed on two test fields (T1). CONFIRMED (formula); proof sketch in notes.
V3 (gauge): for |rho| = O(r^k), |grad rho| = O(r^{k-1}), k < 1, the odd/odd solution with psi = o(r^2) (equivalently
   U = o(|X|), by interior gradient estimates) is unique; lambda x y is excluded. Astra referee (astra/lemS, 2026-10-17T18:00Z):
   CORRECT, with one correction adopted: for k >= 1 the n = 2 integral is not necessarily divergent (convergence then depends
   on cancellations in the actual mode; e.g. a field equal to y outside a disc has compactly supported d_x rho). The correct
   statement: growth k < 1 guarantees convergence; for k >= 1 the gauge is not fixed by growth alone. CONFIRMED (as corrected).
V4 (growth Liouville, Lemma G): if U is sublinear (|U| <= eps(|X|)|X| + C, eps -> 0) and |rho| <= C(1+|X|)^k with c_l k < 1
   (any c_l if c_l <= 0), then rho == 0. Proof: rho(Phi_s X) = e^s rho(X) and |Phi_s X| <= C e^{(c_l+delta)s}.
   Consequence: in the sublinear (canonical gauge) class, nonzero profiles need c_l >= 1/k > 1.
V5 (Lemma S, sonic point): for c_l > 1/2, rho in C^2 and E(x) = V_1(x,0) > 0 for some x > 0, the first zero x_* of E on the
   positive x-axis satisfies d_x V_1(x_*,0) = 2c_l - 1, d_y V_2(x_*,0) = 1, rho_y(x_*,0) > 0. Astra referee (astra/lemS):
   CORRECT, and supplied a shorter proof using only E, h in C^1 and div V = 2c_l: with alpha = 2c_l - 1 the axis ODE is
   E h' = (E' - alpha) h; h > 0 on (0,x_*); if mu = E'(x_*) < alpha then h' > 0 near x_*, h(x_*) > 0 and the endpoint
   equation gives (mu - alpha) h(x_*) = 0, contradiction; if h(x_*) = 0 then d/dx log(h/(-E)) = -alpha/E integrates to
   +infinity, contradicting h in C^1; hence h(x_*) > 0 and mu = alpha. I checked this argument line by line. Existence of
   x_* is a hypothesis (it holds when U_1(x,0) = o(x), e.g. in the sublinear class). CONFIRMED.
V6 (regularity heuristic): near the saddle at 0, generic solutions contain |xi|^{q_3} eta^3 with q_3 = 6 + 2/(2c_l-1) in (6,8)
   for c_l > 1, so C^infinity smoothness of a(x,y) is a nontrivial extra condition. Astra referee: exponents CORRECT; for an
   already smooth profile a smooth symmetric linearization with rho = xi^2 eta exists (no nonresonance needed; proof in
   astra/lemS/answer.md, which I have read but not yet checked in full); in a fixed smooth linearization smoothness forbids
   every incoming coefficient b_n with q_n not an even integer (infinitely many). GAP: these are not shown to be independent
   conditions on the coupled problem. Genericity of finite regularity is an unproved heuristic. OPEN (heuristic only).

## Part 3. Audit of the lead's SPEC.md v1 (2026-10-17T17:54Z version), audited 2026-10-17T18:00Z-18:05Z
Method: line-by-line rederivation by hand (independent of the lead's scripts), cross-checked with my notes/analysis_v1.md,
the astra referee astra/lemS/answer.md, and the numerical tests T1.

S0 (conventions, kernels, parity, eigenvalues 1-2c_l and 4c_l-1, 3c_l - c = 1). Same as my V1, V2. CONFIRMED.
   Remark: near 0 one has U = (-cx, cy) + O(r^3) by parity (SPEC says O(r^2), which is true but weaker).
S1 (scaling). rho -> L rho(X/L) maps solutions to solutions, U -> L U(X/L), a(0) -> a(0)/L^2; L = -1 acts trivially on the
   parity class, so a(0) = +1 and a(0) = -1 are distinct problems. I also checked that the reflections y -> -y and x -> -x
   combined with rho -> -rho do not give a symmetry that would identify them (the U.grad rho term changes sign). CONFIRMED.
   Physical scaling: rho = tau^alpha P(X/tau^{1+alpha}) gives c_l = (1+alpha)/alpha, alpha = 1/(c_l - 1), with the outer
   state |Z|^{1/c_l} Theta matching (exponents checked). CONFIRMED.
S2 (class A). Coherent. Note that (A3) bounds grad rho as well as rho; this is what makes the interior-estimate argument
   for U = o(|X|) work. No hidden wall condition: the class is posed on R^2 with parity only. CONFIRMED as a definition.
S3 (velocity law). V1 normalization: psi_n = (1/(4n))[...] for the sin(2n t) mode agrees with my p_N = (1/(2N))[...], N = 2n.
   d_x of f(r) sin((2m+1)t) formula: rederived, correct. c = (1/2) int f_1/s ds = int rho_1 r^{-2} dr
   = (1/pi) int rho sin(3t) r^{-3} dX: same as my C3, checked numerically to 2e-13 on a growing field (T1). V3 uniqueness proof
   (D_1 - i D_2 entire, Liouville, parity): correct. V2 (symmetric truncation converges for gamma < 1): correct (also
   confirmed by astra). V1 = V3: V1 gives psi = o(r^2) and by the interior gradient estimate U = o(|X|); both satisfy div,
   curl and parity, so V3 uniqueness identifies them. CONFIRMED.
   The paragraph "Physical justification" (no lambda x y from the outer region) is a heuristic matching argument, not a proof.
   It is not needed for any lemma. Flag: HEURISTIC.
S4.1 (Lemma 1, c_l >= 1/gamma > 1). Same as my V4: rho(Phi_s X) = e^s rho(X), |Phi_s X| <= C e^{(c_l+delta)s}; the case
   of bounded orbits gives rho = 0 there. The flow is global and unique for rho in C^1 (U log-Lipschitz, linear growth).
   CONFIRMED. The secondary statement "rho grows like |X|^{1/c_l} along escaping characteristics" also holds in class A
   (d|X|/ds = c_l|X| + O(|X|^gamma), so |X(s)| ~ C e^{c_l s}).
S4.2 (Lemma 2). No periodic orbits (Bendixson, div W = 2c_l > 0): CONFIRMED. Index sum +1 on a large circle (W ~ c_l X):
   CONFIRMED. "Every backward orbit converges to a stagnation point": backward orbits are bounded (correct), but the
   alpha-limit set could a priori be a graphic (stagnation points joined by orbits). A graphic bounding a region is excluded
   by the same flux argument (int div W > 0 against zero flux), but the SPEC does not state finiteness/isolatedness of
   stagnation points as an assumption of the lemma. Verdict: CONFIRMED under the explicit extra hypothesis "finitely many
   stagnation points"; the SPEC writes this in parentheses, which is acceptable.
S4.3 (Lemma 3). Agrees with my V5. Two improvements: (i) the degenerate case mu1 = 0 is excluded for rho in C^1 (then
   1 - mu2 = 1 - 2c_l < 0 and (1 - mu2)/W_1 is positive and non-integrable at x*, so g -> infinity); (ii) the C^2 conclusion
   needs only E, g in C^1 (astra proof, see V5). The claim "rho in C^1 forces mu2 <= 1" is correct: for mu2 > 1 the same
   non-integrability makes g unbounded. CONFIRMED.
S4.4 (Lemma 4, rigidity at the source P). Resonance check: i(2c_l - 1) + j = 1 has only (i,j) = (0,1) for c_l > 1.
   Uniqueness for fixed W: if two C^1 solutions agree to first order at P their difference w = o(|z|) satisfies
   w(z0) = e^t w(Phi_{-t} z0) with |Phi_{-t} z0| <= C e^{-t} (min eigenvalue 1), so w = 0. Hypothesis needed: W in
   C^{1,gamma} near P (true for rho in C^{1,gamma} locally). The SPEC's "N > 1/min(mu1,mu2)" is sufficient but more than
   needed. CONFIRMED. Consequence (correct): if P, -P and 0 are the only stagnation points, every orbit in Q comes from P,
   so rho > 0 in Q (sign of rho_y(P) > 0).
S4.5 (Lemma 5). Exponents p_j = 2j + (j-1)/(2c_l - 1) agree with my q_n and astra; p_3 in (6,8), not an even integer, for
   c_l > 1. [REVISED 2026-10-17T18:27Z, see Part 4, item L5.] My original entry here read: "The conclusion 'rho is C^6 but
   not C^8' if B_3 != 0 is correct as stated (the exact class of |x|^{p_3} is C^6 for p_3 <= 7 and C^7 for p_3 in (7,8))".
   That confirmation was an ERROR on my part: it treated the regularity of the trace G_3(x) = d_y^3 rho(x,0)/6 as the
   regularity of rho itself. (i) The trace argument loses three derivatives: G_3 not in C^q only gives rho not in C^{q+3}.
   (ii) The positive half ("rho is C^6") needs a 2D expansion through the saddle, and no one has written it. The exponents
   are CONFIRMED. The 2D claim "C^6 but not C^8" is OPEN. What is proved appears in Part 4, item L5.
S5 (N3a far-field tail formula). ERROR (typo-level, but it would bias the velocity if implemented literally): for the
   homogeneous extension rho = (r/R)^k Theta_R(t), r > R, one has d_x rho = (r/R)^k r^{-1} [k cos t Theta_R - sin t Theta_R'],
   so with F_n the sin(2n t) coefficient of the bracket,
       int_R^inf s^{1-2n} f_n(s) ds = F_n R^{-k} int_R^inf s^{k-2n} ds = F_n R^{1-2n}/(2n - k - 1),
   not F_n R^{2-2n}/(2n-k-1). (Equivalently R^{2-2n} f_n(R)/(2n-k-1) with f_n(R) = F_n/R.) REFUTED as written; corrected
   formula above. My own code uses the equivalent tail in terms of the rho-modes: QN = A R^{k+1}/(n - k - 1).
S6 (D6 weighted identity). Rederived: integrating W.grad rho = rho against phi = r^{-d} sin((2m+1)t) gives
   (1 + (2-d)c_l) int rho phi + int rho U.grad phi = 0; integrability and vanishing boundary terms at 0 need d < 5
   (rho ~ r^3), at infinity need d > k+2. With d = 3, m = 1: pi(1-c_l)c + int rho U.grad(sin(3t) r^{-3}) = 0. CONFIRMED.
S7 (out-of-class regimes). Statements are consistent with Lemma 1 (c_l <= 1 forces growth >= r in the sublinear-U logic,
   hence that class needs a separate gauge rule). The origin is a source for 1/4 < c_l < 1/2: correct. CONFIRMED.
Overall SPEC v1 verdict: sound, one formula error (S5, N3a tail), one heuristic paragraph to keep labeled (S3), Lemma 3
can be strengthened (S4.3). No hidden wall condition, no gauge leak, c_l is not fitted independently in the formulation.

## Part 4. Audit of SPEC.md v2 (18:13Z) and lead notes/analysis.md v1 (18:08Z), sections 1 to 4. Audited 2026-10-17T18:21Z-18:28Z
Method: I rederived every step by hand and compared it with my own notes (notes/analysis_v1.md) and with the astra lemS
answer. Numerical cross-checks are cited where they exist.

A1.1 (|U| <= C(1+|X|)^gamma, analysis 1.1). The conclusion is correct, but one step is wrong as written. On
   A = {|X-Y| < s} the proof bounds |rho(Y) - rho(X)| using "sup_{B_2s} |grad rho| <= C(1+s)^{gamma-1}". Because gamma - 1 < 0,
   the sup of (1+|Y|)^{gamma-1} over B_2s is attained at Y = 0 and equals 1. The disc A touches the origin, so this step gives
   only C s.
   Repair: split A at |X-Y| = s/2.
    - For |Z| < s/2 the segment [X, X+Z] stays in |Y| >= s/2, which gives C s (s/2)^{gamma-1} = C' s^gamma.
    - For s/2 <= |Z| < s, use |K| <= C|Z|^{-2} and |rho(Y) - rho(X)| <= C s^gamma, which gives C s^gamma log 2.
   The B and C_R parts are correct as written: the K(-Y) term vanishes by parity, and |K(X-Y) - K(-Y)| <= C s|Y|^{-3}.
   CONFIRMED after this repair (minor).
A1.2 (equations, local Schauder). Standard. Parities checked: psi odd/odd, U_1 odd-x/even-y, U_2 even-x/odd-y. CONFIRMED.
A1.3 (uniqueness). f = D_1 - i D_2 gives d_zbar f = (1/2)(div D - i curl D), so f is entire; o(|z|) and the Cauchy estimate make
   f constant; parity makes it zero. Odd/odd harmonic polynomials are exactly Im z^{2n}: checked, Im z^d is odd in x only for
   even d. CONFIRMED.
A1.4 (V1 = 1.1). psi is odd/odd: the stream function of U, normalized by psi(0) = 0, has psi(x,y) + psi(-x,y) with zero
   gradient. Integrating along arcs from the axes gives |psi| <= C r^{1+gamma}. The homogeneous r^{2n} is excluded at infinity
   and r^{-2n} at 0. CONFIRMED.
A1.5 (c formula). Rederived. The sin 2t coefficient of d_x rho is (1/2)(rho_0' - rho_0/r) + (1/2)(rho_1' + 3rho_1/r), and the
   integration by parts gives c = (1/4)([rho_0/s] + [rho_1/s]) + int rho_1 s^{-2} ds.
    - The boundary terms vanish under (A2).
    - Without (A2), [rho_0/s]_0^inf = -rho_y(0), which gives SPEC v2's general form c = int rho_1 r^{-2} - rho_y(0)/4.
    - Check of rho = y e^{-r^2}: psi = p(r) sin 2t with p'' + p'/r - 4p/r^2 = r^2 e^{-r^2}, so p ~ -(r^2/4)(1/2) and
      psi_xy(0) = -1/4. Matches.
   Numerical cross-checks: T1 and test_vpolar3 (c = 1/(4(1-k)) to 2e-13). CONFIRMED.
A2.1 (Lemma 1, both the notes and SPEC v2). (d/ds) log r = c_l + O(r^{gamma-1}).
    - Escape follows because e^s|rho(X0)| is unbounded and rho is bounded on bounded sets.
    - The O(r^{gamma-1}) term is integrable in s along escaping orbits, so e^{-c_l s} X(s) -> V != 0. The angle also
      converges, since d theta/ds = U_theta/r = O(r^{gamma-1}).
    - Uniform bound |rho| <= C(1+|X|)^{1/c_l}: every X outside B_R0 reaches |Y| = R0 in backward time s with
      |X| >= R0 e^{c_l s - C''}. The constant C'' is uniform because the correction integral is bounded once r grows
      exponentially.
   CONFIRMED.
A2.2 (center, 3c_l - c = 1). Correct. A minor point: with only C^{2,alpha} the expansions are W_1(x,0) = lambda1 x +
   O(x^{2+alpha}) and m = lambda2 + O(x^{1+alpha}), not O(x^3) and O(x^2). The argument is unchanged.
   In the lambda1 = 0 branch, also note that W_1(.,0) has no zeros accumulating at 0: at a zero, (1-m)g = 0 would force g = 0.
   CONFIRMED.
A2.3 (backward-invariant disc, no cycles or graphics, alpha-limits, index). Correct.
    - (iii) uses the standard Poincare-Bendixson trichotomy for finitely many equilibria. A limit set that contains a regular
      point is a graphic. Each closed loop of it bounds a region where the flux is 0 but int div W = 2c_l|D| > 0.
    - Finiteness of the zero set is a hypothesis (SPEC v2 states this).
    - (v): the homotopy between W and c_l X on |X| = R is nonvanishing for R large. Index +1.
   CONFIRMED (conditional on finitely many zeros, as stated).
A2.4 / SPEC Lemma 3 (mu2(P) = 1 from C^2). Rederived. Near x*, g = K t^beta (1 + O(t^alpha)), with t = x* - x,
   beta = (1-mu2)/mu1 and K > 0.
    - beta < 0 makes g unbounded.
    - 0 < beta < 1 makes g' unbounded, since g' = g(1-m)/w = beta K t^{beta-1}(1+o(1)) directly from the ODE.
    - beta >= 1 is equivalent to 1 >= mu1 + mu2 = 2c_l, which contradicts Lemma 1.
   So mu2 = 1 and mu1 = 2c_l - 1 > 1. DW(P) is diagonal by parity, so P is a hyperbolic source.
   The nondegeneracy hypothesis mu1 > 0 in analysis 2.4 is removable, and SPEC v2 removes it. If mu1 = 0, then
   |w| <= C t^{1+alpha} and 1 - m(x*) = 1 - 2c_l < 0 with w < 0, so (log g)' >= (2c_l-1)/(C t^{1+alpha}) is not integrable
   and g -> +infinity. This was my S4.3 remark.
   CONFIRMED (2.4(a), (b), (c), and SPEC v2 Lemma 3 as stated).
A2.5 (positivity under Hmin). Correct.
    - For X in Q the alpha-limit is 0 or P. The global unstable manifold of the saddle is contained in the invariant y-axis,
      so the alpha-limit is P. Then rho(X) = e^s rho(Phi_{-s}X) > 0.
    - On the y-axis, rho(0,y) = 0 follows from the transport ODE with zero data near 0. This needs W_2(0,y) > 0, which (Hmin)
      gives. Parity alone does not give it.
    - h = d_x^2 rho(0,y): I differentiated the equation twice in x at x = 0. The terms W_{1,xx} rho_x, W_{2,x} rho_xy and
      W_{2,xx} rho_y vanish (parity and rho(0,y) = 0), leaving W_2 h' = (1 - 2 d_xW_1(0,y)) h with h ~ 2y.
    - Index count -1 + 1 + 1 = 1: consistent.
   CONFIRMED (conditional on Hmin; needs rho in C^3 for the h statement, as written).
A2.6 / SPEC Lemma 4 (rigidity at P).
   (a) Notes version, via a C^1 linearization. Homogeneity gives d_xi rho~(lambda^{mu1} xi, lambda eta) =
       lambda^{1-mu1} d_xi rho~(xi, eta) with 1 - mu1 = 2 - 2c_l < 0, so d_xi rho~ = 0. A C^1 linearization of a C^2 field
       at a hyperbolic equilibrium in 2D is Hartman's theorem (1960), so the hypothesis holds in A_2.
   (b) SPEC v2 version, eta_P = y exp(-I), I(X) = int_{-inf}^0 [b(Phi_t X) - 1] dt.
    - I checked eta_P(Phi_t X) = e^t eta_P(X) directly from y' = y b, so W.grad eta_P = eta_P.
    - I converges and is C^1 near P: b is C^{1,alpha}, and the backward flow contracts at rate >= 1 since the eigenvalues
      are 2c_l - 1 > 1 and 1.
    - grad eta_P(P) = (0,1).
    - w = rho - rho_y(P) eta_P is o(|X-P|) and satisfies w(X) = e^t w(Phi_{-t}X). The rate needed is |Phi_{-t}X - P| <= C e^{-t}
      exactly, and it holds. The eigenvalues are 1 (weak) and 2c_l - 1 > 1 (strong), with no resonance: i(2c_l-1) + j = 1
      only for (0,1). In C^1 linearizing coordinates the backward orbit is (e^{-mu1 t} xi, e^{-t} eta). So
      e^t o(e^{-t}) -> 0 and w = 0.
   CONFIRMED. This is rigidity for fixed W only, as SPEC v2 says.
L5 / A3.1 (Lemma 5, axis hierarchy and B_3).
    - ODEs: rederived from the y^1 and y^3 coefficients. They match the notes and SPEC v2 (F_3 = -W_1^(2) G_1' - W_2^(3) G_1).
    - Exponents: p_3 = (3 lambda2 - 1)/|lambda1| = 6 + 2/(2c_l - 1). The general p_j = 2j + (j-1)/(2c_l-1) is never an even
      integer for j = 3. CONFIRMED.
    - "C^infinity => B_3 = 0": the particular solution is a formal series in x^2 with denominators 2 + 2k - p_3 != 0, and
      Borel/Taylor-matching gives a smooth even particular solution. Every solution is G_3^sm + B_3 |x|^{p_3} e^E. This is
      not C^{ceil p_3} at 0 when B_3 != 0. For p_3 = 7 (c_l = 3/2) this uses evenness: |x|^7 is not C^7.
      CONFIRMED (PROVED).
    - Trace version: B_3 != 0 => rho not in C^10 (p_3 <= 7) or not in C^11 (p_3 in (7,8)). The derivative count is right
      (G_3 in C^{q-3} when rho in C^q). The step that needs care is that the particular solution has the required finite
      regularity when the coefficients are only finitely smooth: rho in C^{11,alpha} gives F_3/(x w) in about C^7 and
      G_3^sm in C^8. I checked this count but did not write out the remainder estimates. The borderline case p_3 = 7
      needs a log check. Verdict: PLAUSIBLE, routine; not independently proved by me.
    - 2D statement "C^6 but not C^8": OPEN (see revised S4.5). Two remarks:
      (1) The referee counterexample x^2 y + B x^2 y^3 r^{p-2} is homogeneous of degree p+3, so it is about C^{p+2} in 2D
          while its y^3 trace B|x|^p is only C^{floor p}. So the trace exponent alone does not determine the 2D class.
          Agreed.
      (2) In linearizing coordinates near the saddle, the transported structure is rho = sum_j c_j eta^j |xi|^{p_j}. The
          c_3 term is non-smooth across the whole unstable manifold xi = 0 (the y-axis), not only at 0. I checked by direct
          transport along the y-axis: a singular part S = B(y)|x|^p satisfies W_2 B' = (1 - p d_xW_1(0,y)) B, so the
          exponent p is preserved. This independently agrees with the lead's note of 18:08Z (item 2).
      This suggests the 2D class is limited by |x|^{p_3} across the y-axis, so rho would not be C^{ceil p_3}. But it needs a
      C^k linearization with k >= 8, or a saddle-passage expansion with remainder bounds. Not proved.
      Diagnostic consequence (agreed with the lead): at every fixed r the angular modes f_m(r) decay like m^{-(p_3+1)} if
      B_3 != 0. A C^infinity candidate must show faster decay.
A3.2 (B_3 as a finite-part integral). Rederived.
    - (G_3/H)' = F_3/(W_1^(0) H), and H ~ t^{-2/mu1} at P, which is unbounded since 3mu2 - 1 = 2. So boundedness at P gives
      G_3 = -H int_x^{x*} F_3/(W_1^(0) H) dt. The integrand is O(t^{2/mu1 - 1}), which is integrable.
    - Near 0, f.p. int_0^x has no constant term (non-resonant), and neither does G_3^sm/H. So B_3 = -f.p. int_0^{x*}
      F_3/(W_1^(0) H) dt with H ~ x^{p_3}.
    - Hypothesis: rho in C^4 near the segment. "mu1 > 0, mu2 = 1" is automatic in A_2.
   CONFIRMED. The sign convention is to be validated numerically on a manufactured case before it is used on a candidate.
A3.3 (structure in C^infinity): conditional on Sternberg, which fails at resonant c_l (lambda2/|lambda1| rational). The
   heuristic count is labeled as heuristic. CONFIRMED as labeled.
A3.3b (astra lemS, smooth linearization for an already smooth profile). Checked line by line on 2026-10-17 at 18:38Z.
   Notation: alpha = 2c_l - 1 and beta = 2alpha + 1.
   Statement: if W and rho are C^infinity near 0, with the symmetries, W rho = rho, div W = alpha + 1 and rho = x^2 y a with
   a(0) = 1, then there are smooth symmetric coordinates, tangent to the identity, with W = -alpha xi d_xi + beta eta d_eta and
   rho = xi^2 eta. No non-resonance hypothesis is needed.
   The steps I checked:
    - Coordinates u = x sqrt(a), v = y, so rho = u^2 v. Then W = uP d_u + vQ d_v with P, Q, m even/even, P(0) = -alpha,
      Q(0) = beta and m(0) = 1.
    - Transport gives 2P + Q = 1. Divergence gives d_u(muP) + d_v(mvQ) = (alpha+1)m.
    - Compatibility: A(mP) - B(-mQ) = (alpha+1)m(1 - 2P - Q) = 0, with A = u d_u - beta and B = v d_v - alpha. I verified
      this using 1 + beta = 2(alpha+1).
    - z d_z - sigma is invertible on smooth even germs when sigma is not in 2N_0. I checked the remainder formula:
      (z d_z - sigma) int_0^1 t^{-sigma-1} R(tz) dt = R.
    - alpha and beta are never both in 2N_0. The second equation for w follows from commutation and injectivity, and
      w(0) = 1.
    - W w = (beta P + alpha Q) w = (P + alpha) w.
    - xi = u/w and eta = v w^2 give W xi = -alpha xi, W eta = beta eta and xi^2 eta = rho.
    - The Jacobian is w - u w_u + 2v w_v = m(Q + 2P) = m > 0.
   CONFIRMED. Consequence: for a C^infinity profile, the Sternberg condition in analysis 3.3 can be dropped.
   Correction to 3.3's wording: in a FIXED smooth linearization, C^infinity forces the forbidden Taylor coefficients c_j to
   vanish (q_j not in 2N_0). It does not force rho = c_1 xi^2 eta exactly, because flat terms are allowed. Astra's example
   is xi^2 eta exp(-1/(|xi|^{2beta/alpha} eta^2)). The exact form rho = xi^2 eta holds in the coordinates constructed above.
   Astra also notes that this does not apply to a finitely regular candidate that is being tested for smoothness.
A4.1 (weighted identity). div(rho W phi) = rho phi (1 + 2c_l - d c_l) + rho U.grad phi. The boundary fluxes are
   O(R^{k+2-d}) and O(eps^{5-d}), and the integrand rho U.grad phi is integrable at infinity for d > k + gamma + 1, which
   k + 2 covers. CONFIRMED (= my S6).
A4.2 (div(W |rho|^{-2c_l}) = 0) and A4.3 (c > 2, psi_xy(P) = 1 - c_l < 0). CONFIRMED.
SPEC v2 changes not covered above:
    - Amplitude scaling: sigma = lambda rho solves with (lambda c_l, lambda c_rho). Checked. CONFIRMED.
    - N3(a) tail: now F_n R^{1-2n}/(2n-k-1) = f_n(R) R^{2-2n}/(2n-k-1), which matches my S5 correction. CONFIRMED.
    - Section 1 scaling L rho(X/L): a(0) -> L^{-2} a(0), and the sign of a(0) is invariant. CONFIRMED.
    - Section 7 examples: rho = y^q, U = 0, c_l = 1/q is exact. A sin 5t mode feeds only sin 4t and sin 6t of d_x rho.
      CONFIRMED.
    - Global-factor note: if W_2(0,y) > 0 for all y > 0, then rho(0,y) = 0 by transport and rho_x(0,y) = 0 by parity, so
      rho = O(x^2) on the y-axis. CONFIRMED.
    - Minor wording: D8 says "the available a priori bound is U = O(r^k log r)" while V2 says |U| <= C(1+r)^gamma with no
      log. These do not conflict: gamma is the (A3) gradient exponent, and k = 1/c_l <= gamma comes from Lemma 1. Suggest
      stating both exponents explicitly in SPEC.
Overall verdict on SPEC v2 and analysis.md sections 1 to 4: sound. One proof step was wrong but its conclusion holds
(A1.1, repaired above). Analysis 2.4's nondegeneracy hypothesis is removable (already done in SPEC v2). Analysis 2.2's
expansion orders are slightly overstated for C^{2,alpha}. The finite-regularity trace statement of Lemma 5 is PLAUSIBLE,
not independently proved. The 2D regularity claim is OPEN. No hidden wall condition and no gauge freedom. c_l is never
fitted independently in the formulation.

Part 4 addendum: notes/analysis.md v2 (header 18:19Z, file mtime 18:20:32Z). The audit above was of v1 plus SPEC v2.
I compared v2 with v1 (diff of notes/analysis_v1_backup.md and notes/analysis.md) and checked every changed item on
2026-10-17 at 18:43Z-18:46Z.
 - 2.1 (repaired proof with the uniform bound). Same argument as SPEC v2 Lemma 1, checked in A2.1. CONFIRMED.
 - 2.2 (new proof by rescaling). rho_eps(X) = rho(eps X)/eps^3 -> x^2 y and W_eps(X) = W(eps X)/eps -> DW(0)X locally
   uniformly, and W_eps.grad rho_eps = rho_eps holds exactly. div W_eps = 2c_l, so the weak form passes to the limit.
   DW(0) = diag(c_l - c, c_l + c) because psi_xx(0) = psi_yy(0) = 0 by parity. CONFIRMED. It needs W in C^1 and a continuous.
 - 2.4 (v2 proof). From w' + h = 2c_l, 1 - h = w' - A with A = 2c_l - 1.
    - mu1 = 0: near x*, (w' - A)/w >= (A/2)/|w| >= A/(2 eps t), so g -> infinity.
    - mu1 > 0: log g = alpha log t + o(|log t|) with alpha = 1 - A/mu1 < 1. Then g(x*) = 0 contradicts g <= M t. So
      g(x*) > 0, h(x*) = 1 from the ODE at x*, and mu1 = A from the trace.
   CONFIRMED. This is cleaner than my A2.4 route and reaches the same conclusion.
 - 2.5 (v2). Uses 2.6: rho = C eta_P with C = g(x*) > 0. The equivalent form of (Hmin) is right: W_1 = 0 on the y-axis and
   W_2 = 0 on the x-axis by parity, and W_2(0,y) > 0 for small y since lambda2 > 0. CONFIRMED (conditional on Hmin).
 - 2.6 (v2 proof). Along an orbit, (rho/y)' = (1 - b)(rho/y). Integrating from t to 0 and letting t -> -infinity, with
   rho/y -> rho_y(P), gives rho = rho_y(P) y exp(-I). CONFIRMED (same as A2.6(b)).
 - 3.1 (v2).
    - Denominators: for G_3 = x^{2n} the operator gives (3 lambda2 - 1 - 2nA) x^{2n} = A(p_3 - 2n) x^{2n}. CONFIRMED.
    - (iii) p_{2l+1} = 4l + 2 + 2l/A, which is even iff l/A is an integer. If A = p/q in lowest terms, this happens iff p
      divides l. So infinitely many j are nonresonant. CONFIRMED.
    - The 2D statement is marked NOT proved, in agreement with my OPEN.
 - 3.2 (v2, explicit H).
    - H'/H = (1 - 3h)/w gives H ~ x^{p_3} at 0 and H ~ t^{-2/A} at P. The integrand is O(t^{2/A - 1}).
    - (G_3/H)' = F_3/(wH), and G_3/H -> 0 at P.
    - G_3^sm/H has no x^0 term.
   CONFIRMED (same as A3.2).
 - 3.3 (v2, transversal formulation).
    - The general solution |xi|^{1/lambda1} Fhat(eta |xi|^{-lambda2/lambda1}) and the exponents p_j = (j lambda2 - 1)/|lambda1|
      (p_1 = 2) check.
    - The other invariants xi_P xi (A - A = 0) and eta |xi|^{2 + 1/A} ((2A+1) - (2+1/A)A = 0) check.
    - Wording to correct: "C^infinity iff F is LINEAR" and "this first integral is CONSTANT" hold only modulo flat terms
      in a fixed smooth chart; astra's flat example is xi^2 eta exp(-1/(|xi|^{2beta/alpha} eta^2)). They hold exactly in the
      chart of A3.3b, where rho = xi^2 eta. The correct statement is "C^infinity iff F - F'(0) eta is flat at 0". Then
      "C^infinity iff there is a smooth symmetric linearizing chart in which F is linear".
   CONFIRMED with this correction.
 - 3.4 (counting) is labeled HEURISTIC, correctly.
 - 4.4: c = (1/pi) int rho sin 3t r^{-3}, and the integrand is even/even, so the integral equals 4 int_Q. c > 2 follows from
   4.3. CONFIRMED. Wording: under (Hmin), rho(0,y) = 0, so "rho > 0 in the upper half plane" should read "rho > 0 in Q and
   its mirror image".
 - Section 5: "a in C^4 but not C^infinity" is the trace-level count (p_3 - 2 in (4,6)). It should carry the same "unproved
   in 2D" qualifier as the line before it.
 - Section 6 (a) to (g): all of these are covered by the items above.
Verdict on analysis.md v2: sound, with two wording corrections (3.3 flat terms; section 5 qualifier).

## Part 5. Process and honesty checks
P1 (2026-10-17T18:27Z). Future timestamps in the numerics lane. At date -u = 18:27:16Z:
    - numerics/NUM_REPORT.md says "Last update: 2026-10-17T18:45Z"; its file mtime is 18:16:50Z.
    - numerics/WORKLOG.md has entries headed "2026-10-17T18:50Z" and "2026-10-17T19:05Z"; its mtime is 18:19:58Z.
   These times are in the future, so they are not real. The prompt forbids invented timestamps. The numerics lane must
   correct them, using date -u, before any of its results can be cited with times. The content of the entries is a
   separate question and is checked on the data when a candidate appears. (I made the same mistake twice in my own lane
   earlier this shift and corrected it; see WORKLOG.)
P1 status (2026-10-17T18:49:23Z). The numerics lane added a dated correction at 18:34Z (WORKLOG lines 44-54). It gives real times from file
   mtimes, and the old headers are left visible and marked wrong. I spot-checked it against mtimes: tests/test_basic.py
   18:13:21Z, tests/test_poisson.py 18:14:00Z, src/ipm1.py 18:15:48Z, tests/test_newton.py 18:17:13Z. These agree.
   The NUM_REPORT and RUN_STATUS headers now say 18:35Z, which matches their mtime of 18:35:42Z. P1 is RESOLVED for the
   entries it covers.
P1b (2026-10-17T18:49:23Z). New future timestamp in the numerics lane. numerics/WORKLOG.md line 57 has the header
   "## 2026-10-17T18:58Z  (real time)". The file mtime is 18:45:11Z, and date -u is 2026-10-17T18:49:23Z. So the header was written at
   least 13 minutes before the time it states, even though it is labeled "real time".
   Its body mentions src/charac.py "(18:4xZ)", whose mtime is 18:39:45Z, and tests/test_charac.py "(18:40Z-18:45Z)", whose
   mtime is 18:35:42Z. The test file may have been run later than its mtime, so only the header is certainly wrong.
   Requested: correct it the same way as P1. OPEN.
P1b status (2026-10-17T19:07:09Z). Not yet corrected: numerics/WORKLOG.md line 57 still reads "## 2026-10-17T18:58Z  (real time)";
   the file was last modified at 18:53:45Z. OPEN.
P1c (2026-10-17T19:07:09Z). Another future timestamp in the numerics lane. numerics/NUM_REPORT.md line 3 reads
   "Last update: 2026-10-17T19:08Z". Its mtime is 19:05:41Z, and I read it at date -u 19:06:44Z, two minutes before the time
   it states. Requested: replace with the date -u time of the edit. OPEN.

P1c status (2026-10-17T19:29Z). numerics/NUM_REPORT.md now reads "Last update: 2026-10-17T19:25Z" and its mtime is
   19:25:03Z: consistent. RESOLVED. P1b (2026-10-17T19:29Z): WORKLOG line 57 still "## 2026-10-17T18:58Z  (real time)". OPEN.
P1b status (2026-10-18T00:52Z). numerics/WORKLOG.md has a dated entry "2026-10-17T19:45Z CORRECTION of two more wrong
   headers (flagged by the verifier, P1b/P1c)" (lines 173 to 179). It states that the 18:58Z header is wrong, that the
   entry was written at about 18:45Z (the date -u of its own command), and that the label "(real time)" was false; the old
   header is left visible. This is the same treatment as P1, and 18:45Z agrees with the file mtime I recorded (18:45:11Z).
   Later numerics headers are generated by date -u. RESOLVED.

## Part 6. Audit of the lead's FINAL_REPORT.md draft (file mtime 18:33:15Z), checked 2026-10-17T18:49:23Z
F1. Sections 0 to 3 contain only items that I have audited.
    - R1: A1.1-A1.4. I rederived the V1 Green function in the FINAL_REPORT form: for -(psi'' + psi'/r - nu^2 psi/r^2) = f
      with nu = 2n, G(r,s) = (s/(2nu)) (r_</r_>)^nu, which gives the 1/(4n) prefactor and the exponents as written.
    - R2: A2.1. R3: A2.2 and the v2 rescaling proof. R4: A2.3, conditional on finitely many zeros, as stated. R5: A2.4.
    - R6: A2.6(b). R7: L5/A3.1 and v2 3.1 (i) and (iii); the 2D statement is correctly marked not proved. R8: A4.1.
    - The "pending external audit" items (positivity under Hmin, B_3 finite part) are A2.5 and A3.2.
    The section 0 timeline entries 18:00-18:05 and 18:21-18:28 for the verifier audits match my report.
    CONFIRMED: no unaudited claim appears in sections 1 to 3.
F2. Wording. R7 says "The same holds for infinitely many higher odd j". This is correct for C^infinity profiles, where
    each G_j is smooth and p_j is nonresonant for infinitely many j (Part 4 addendum, 3.1(iii)). No change needed.
F3. T0. The draft gives T0 = 17:37:12Z, the lead's first shift start. The other lanes started at 17:37:14Z (numerics) and
    17:37:16Z (verifier). The earliest, 17:37:12Z, is the right team T0.

## Part 7. Audit of lead/astra/construct1/PROOF.md ("Method identities and scope", mtime 19:21:59Z), audited 2026-10-17T19:28Z
Scope. The note says it does not prove existence of a profile. I checked each identity by hand derivation.
C1. Dynamic normalization. With rho = x^2 y e^H and rho_tau = b rho - (dX + U).grad rho, b = 3d - c:
    H_tau = b - (2W_1/x + W_2/y) - W.grad H, and 2W_1/x + W_2/y = 3d + 2U_1/x + U_2/y; X.grad H = H_t,
    U.grad H = (U_r/r) H_t + (U_theta/r) H_theta. At 0, U_1/x -> d_xU_1(0) = -c and U_2/y -> d_yU_2(0) = c, so the constant
    term is -c + 2c - c = 0 and H(0) is preserved. CONFIRMED.
C2. Rescaling of a stationary dynamic state (b > 0). Using U[alpha rho(./L)](X) = alpha U[rho](X/L) (degree 0), with
    alpha = L/b: ((d/b)X + U~).grad rho~ = (alpha/b)(dY + U).grad rho(Y) = alpha rho(Y) = rho~. Cubic coefficient
    1/(b L^2) = 1 for L = b^{-1/2}; psi~_xy(0) = (alpha/L) c = c/b; 3(d/b) - c/b = 1. CONFIRMED.
C3. Log-radius Green law. For -Delta psi_m = f sin(m theta): q_m = psi_m/r^2 = (A_m + B_m)/(2m),
    v_m = (d_t psi_m)/r^2 = (B_m - A_m)/2, with the stated exponential kernels; U_r/r = -sum m q_m cos(m theta),
    U_theta/r = sum v_m sin(m theta). Same Green function as my V1 rederivation (Part 6, F1). Power-law exterior
    f ~ f(R) a^{k-1}: B_m(log R) = f(R)/(m - 1 - k). CONFIRMED.
C4. Stationary shape normalization. rho = L^3 F(X/L) gives a(0) = 1, U = L^3 V(X/L), c = L^2 c_F; with
    L^2 = (3/k - 1)/c_F the center identity 3 c_l - c = 1 holds with c_l = 1/k. The transport equation divided by rho is
    the stated H-equation (I rederived it from c_l z.grad F/F + L^2 V.grad F/F = 1). Gauge and fitting check: c is the
    canonical Green value, c_l is tied to the far-field exponent k, and L is the scaling that the equation admits
    (rho -> L rho(./L) is a symmetry; a(0) = 1 fixes L). This is a reparametrization, not an independent fit of c_l.
    The restriction c_l = 1/k with 0 < k < 1 places every trial in the sublinear class c_l > 1 (V4 class). CONFIRMED.
C5. Trial spaces. Each regular summand r^{2m} cos(2m theta) x (smooth function of r^2) is smooth at 0; the B-spline in q
    is a polynomial in q on the first knot interval and vanishes at q = 0, hence O(r^2). The singular term:
    s^{p/2}|cos theta|^{p-2} sin^2 theta = |x|^{p-2} y^2/(1 + r^2)^{p/2}, and p = 6 + 2k/(2-k) equals p_3 = 6 + 2/A with
    A = 2/k - 1. The leading |x|^p y^3 coefficient is L^{-p} sum_j (-1)^j b_j (T_j(-1) = (-1)^j). CONFIRMED.
    Regularity remark: rho is C^{6,alpha}_loc for alpha < p - 6, as stated. H itself (through the |x|^{p-2} y^2 term) is only
    C^{4,alpha}; this does not matter for the density claim but any residual written in terms of H inherits it.
C6. Compatibility at P: differentiating W.grad rho = rho in y on the axis gives w g' + h g = g, hence h(P) = 1 when
    g(P) != 0 (same as SPEC Lemma 3 and my axis ODE in code/vb3.py). CONFIRMED.
C7. Two-term exterior: B = (T - kD)/(k - 1), A = D - B (value and t-derivative matched with q_2 = 2k - 1). Exterior bound:
    |sin(m theta)| <= m|cos theta| and <= m|sin theta| for even m, so |sin(m theta) tan theta| <= m and
    |sin(m theta) cot theta| <= m; with q_t = v - 2q, v_m = sum (k_j + 1) Q a^{k_j - 1} - m D a^{-m-2}; for a >= 1 all
    powers are <= 1. The bound on |U_i/X_i| follows for the finite modal representation. CONFIRMED.
C8. Exported axis jets. From a = W_1/x = c_l + U_r/r - (U_theta/r) tan theta and b = W_2/y = c_l + U_r/r +
    (U_theta/r) cot theta, with q_t = v - 2q and v_t = m^2 q - 2v - f (from psi_tt - m^2 psi = -r^2 f):
    a_t, b_t, a_thth, b_thth are as stated (sin(m th) tan th = m th^2 + O(th^4); sin(m th) cot th = m - (m^3 + 2m) th^2/6 +
    O(th^4)). With t = log(x/L) + y^2/(2x^2) + O(y^4), theta = y/x + O(y^3): A_2 = (a_t + a_thth)/(2x) and
    B_3^W = (b_t + b_thth)/(2x^2), i.e. my W1_2 and W2_3; G_3 = e^H (H_t + H_thth)/2 is my G3. CONFIRMED.
Verdict: the note is a correct statement of method identities, it claims no theorem beyond them, and its caveats
(finite least squares is not a proof; inner-radius continuation is a truncation error) are accurate. Nothing in it is an
endpoint. Any candidate from construct1 still needs the independent checks of Part 1 (residuals A and B, three
resolutions and three domains, h(P) = 1, B_3, collapse and finite-box checks).

## Part 8. Verifier's own dynamic-rescaling numerics (numerical, heuristic; not evidence for either endpoint), 2026-10-17T19:28Z
D1. Setup: code/vdr.py (log-polar, odd sine modes m <= M, own inverse, ghost jet x^2 y at r0, power-law ghosts at R,
    RK4), driver code/diag_dr2.py; initial data rho = x^2 y (1 + r^2/L2)^{(k0-3)/2}, k0 = 0.67, L2 = 4.67.
D2. Angular resolution: M31 without filter is not converged after tau about 2.5. M31 with hyperviscosity [50,4], M63 and
    M127 agree on c_l(tau) to about 3 digits up to tau 5 (plateau c_l about 0.63 at tau 3.5 to 5.5). This agreement is for
    c_l only; the near-axis layers at r >= 100 (angular half-width about 0.6 deg in M127 from tau 4) are under-resolved
    at M127 and smoothed at M31-hv.
D3. The plateau is not a profile: c_l about 0.63 < 1 contradicts the sublinear-class bound (Part 2, V4), the far field keeps
    the initial exponent, and h(P) levels near 1.03-1.04 (M127, corrected diagnostic), not 1.
D4. All runs leave the plateau at tau about 5.6 to 6.8 with c_l rising past 5 (M31-hv, M63, M127, N2600, R = 1e8 agree to
    2 digits in c_l at tau 5.8 where compared). Mechanism observed: on the x-axis beyond the source P, h = d_yW_2(x,0)
    falls below 0 in x about 20 to 60, and rho_y there grows along an outgoing characteristic; the c-contribution of
    r in [10,100] grows from 0.22 (tau 4) to 9.5 (tau 6.1). Not a radial-resolution, outer-radius or inner-radius artifact;
    whether it is a property of the DR equation or of the unresolved near-axis layers is OPEN.
D5. Conclusion for the team: my DR gives no candidate. It does not support YES and is not a NO argument.
D6 (2026-10-17T19:47Z). Dependence on the initial data (runs/diag3/hL1, hL20; M31-hv [50,4], N1300, R 1e12; only L2 changed):
    L2 = 1: c_l = 0.672, 0.624, 0.615, 0.614, 0.623, 0.863, 2.19 at tau = 2, 4, 5, 6, 7, 8, 8.17, then blowup;
    L2 = 4.67 (D2): plateau about 0.631 (tau 3.5 to 5.5), leaves at tau about 5.6;
    L2 = 20: c_l = 1.338, 0.735, 0.722 at tau = 0.47, 2.0, 2.26, then 2.92 at tau 4.0, 30 at tau 4.2, blowup.
    The plateau value depends on the initial data (0.614, 0.631, about 0.72), and its duration does too. So it is a slow
    transient, not an attractor of the DR, and nothing in the DR singles out c_l about 0.63. This answers the lead's
    RUN_STATUS item 'far-field-closure dependence to be tested by the verifier' for the initial-data part. The lead's
    Newton attractor near 0.63 is a separate computation that I have not checked. Verdict on 'c_l about 0.63 is a
    special value': REFUTED for my DR.

D7 (2026-10-17T20:18Z). Far-field-only change, as requested by the lead (NOTES_FOR_TEAM 19:32Z item 4). Setup: runs/diag3/hk*, M31-hv
    [50,4], N1300, R 1e12, L2 4.67. Only the initial far-field exponent k0 is changed: rho_0 = x^2 y (1 + r^2/L2)^{(k0-3)/2},
    which is the same as the D2 datum for r << 2. The closure exponent kcl is used for the velocity tail beyond R and for
    the outer ghosts. c_l at tau = 2, 3, 4, 5, 6:
      k0 = 0.5,  kcl = 0.5 :  0.811, 0.769, 0.799, 2.18 (tau 5), blowup by 5.2
      k0 = 0.5,  kcl = 0.67:  the same to 3 digits
      k0 = 0.67, kcl = 0.67:  0.695, 0.632, 0.631, 0.638, 3.3 (D2, run hd1300)
      k0 = 0.85, kcl = 0.85:  0.618, 0.537, 0.537, 0.520, 0.523; rises from tau 6.5, blowup after tau 8
      k0 = 0.85, kcl = 0.67:  0.624, 0.560, 0.560, 0.547, 0.545; 0.619 at tau 8, 0.68 at tau 10 (no blowup by 10)
    The plateau value moves with the far-field data alone: 0.77, 0.63, 0.53 to 0.56 for k0 = 0.5, 0.67, 0.85. The closure
    exponent matters only when k0 is close to 1, through the tail term R^{k-1}, which is 0.016 at k = 0.85 and R = 1e12.
    So the plateau value is set by how the far field is prescribed, as the lead expected for c_l < 1 states. It is not
    a property of the profile equation. CONFIRMED (numerical, for my DR). The lead's Newton attractor near 0.63 is not
    checked by this run.

## Part 9. Audit of lead notes/analysis.md sections 7.2, 7.3, 8, 9 (file mtime 19:24:19Z), hand rederivation before 2026-10-17T19:42Z, recorded 2026-10-17T19:46Z
The lead requested this audit (NOTES_FOR_TEAM 19:32Z) before these items enter FINAL_REPORT. Notation as in analysis.md:
w = W_1(x,0), h = d_yW_2(x,0), a2 = d_y^2W_1(x,0)/2, b3 = d_y^3W_2(x,0)/6, g = rho_y(x,0), A = 2c_l - 1, beta = 2/A.
E1. 7.2 axis constraints. div W = 2c_l at orders y^0, y^2 gives w' + h = 2c_l and a2' + 3 b3 = 0; curl W = curl U = -rho_x at
    order y gives h' - 2 a2 = -g'. Eliminating h: a2 = (g' - w'')/2. CONFIRMED (hand). Numerical: my own axis traces of the
    construct1 trial spline60 give mu1 + h(P) - 2c_l = 2.3e-12 (Part 10).
E2. 7.3 closed form H = N g^{3+beta}|w|^{-beta}, N = A^beta/g0^{3+beta}. The G_1 equation w g' = (1 - h) g with h = 2c_l - w'
    is w g'/g = w' - A, so w H'/H = (3 + beta)(w' - A) - beta w' = 3w' - 3A - 2 = 1 - 3h. Near 0, g ~ g0 x^2 and w ~ -A x, so
    H ~ x^{6+2/A} = x^{p3}. CONFIRMED.
    -F3 = a2 g' + b3 g = -(g^4/3)(a2/g^3)' (using b3 = -a2'/3). On (0, x*), w = -|w|, so -F3/(wH) = (1/(3N)) q' m^{beta-1},
    q = a2/g^3, m = |w|/g; (w/g)' = A/g gives m' = -A/g, m'/m = A/w. CONFIRMED, including the sign.
    IBP form for 1 < A < 2: integrating q' m^{beta-1} by parts and using (beta - 1)A = 2 - A gives
    B_3 = -((2 - A)/(3N)) f.p. int_0^{x*} q m^{beta-1}/w; the boundary term at x* vanishes because beta - 1 > 0. CONFIRMED.
    I agree with the audit3 repair that this form must not be used for A > 2.
    A = 2: beta = 1, B_3 = (1/(3N)) [q(x*) - f.p. q(0)] with N = 2/g0^4. The finite part of q at 0 is 0 because q is odd
    (a2 odd, g even). Differentiating the G_1 equation at P gives A g'(P) = w''(P) g(P), hence
    B_3 = g0^4 a2(P)/(6 g(P)^3) = w''(P)(g(P) - 2)/(24 g(P)^3) at g0 = 1. CONFIRMED.
    The finite part needs the expansion of the even integrand factor to order x^4 (audit2/audit3 repair); this condition is
    stated in the note. CONFIRMED as stated.
E3. 9.3 sign of B_3 on compatible axis data (not coupled profiles). Numerical check, code/test_audit3_sign.py.
    Method: build w = -A x(1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L with sympy, take h, a2, b3 from E1, then evaluate B_3
    with my independent tool vb3.b3 (not the lead's b3_diag.py), with G3 = 1e-300 as filler. The compatibility residual is
    at most 2.5e-14.
    Results at A = 2: B_3(1) = -1.0000038 against the exact (L^2 - 4)/(3L^7) = -1, and B_3(3) = 7.62078e-4 against 7.62079e-4.
    S_A was fitted from B_3(L) L^{4+2/A} = C_A (1 - S_A/L^2) and compared with the formula S_A = 6A(4A - 3)/(8A - 1):
      A  | S_A fitted | S_A formula | C_A fitted
      1.6 | 2.766116  | 2.766102    | 0.32369
      2.0 | 4.000008  | 4           | 0.333334
      3.4 | 8.253441  | 8.253435    |
    B_3 changes sign at L = sqrt(S_A), so all three signs occur. CONFIRMED.
E4. 8.2 Lemma 8, using the 9.2 proof.
    Rederivation: V = X + U[F] has div V = 2, so area grows under the flow as e^{2t}. V.X >= R^2 - |U|R > 0 for large R
    (this needs U = o(|X|)), so backward orbits stay in a disc and the flow is complete (|V| <= C(1 + |X|)).
    An invariant Jordan curve is impossible, since the enclosed invariant region would have constant area. By the
    Poincare-Bendixson trichotomy for a bounded orbit with finitely many equilibria, every alpha-limit set therefore
    contains an equilibrium E. F(Phi_t X) = F(X), and continuity along Phi_{t_n} X -> E gives F(X) = F(E). So F takes
    finitely many values, hence F is constant, hence F = 0 by oddness, which contradicts psi_xy[F](0) = 3. CONFIRMED.
    Hypotheses used: U[F] in C^1 (local Lipschitz flow), U[F] = o(|X|), and finitely many zeros of V. All are in the
    lemma's statement.
    Sequence use (9.2): CONDITIONAL, as the note says. I checked the counterexample: F_n = R_n f(X/R_n) gives
    psi[F_n](X) = R_n^2 psi_f(X/R_n), so psi_xy[F_n](0) = c_f, while F_n = O(|X|^3/R_n^2) -> 0 in C^infinity_loc when f
    vanishes to third order at 0. CONFIRMED.
E5. 9.4 finite-part identity f.p. int_0^{x*} dx/g = 0. Integrating (w/g)' = A/g from x to x* gives |w|/g = A int_x^{x*} 1/g.
    Since w/g is odd, its expansion at 0 is A/(g0 x) + O(x) with no constant term; equating constant terms gives the claim.
    CONFIRMED (hand). Numerical check on the exported construct1 axis data (code/chk_fp_g.py), stated as the relative defect
    of int_0^{x*}(1/g - 1/x^2) dx = 1/x*:
    - spline60: defect 1.7e-4; spline120: defect 3.6e-4.
    - In both cases the defect equals the integral of the exported axis-ODE defect (w/g)' - A/g to 3 digits
      (-2.04e-4 vs -2.03e-4 and -4.20e-4 vs -4.20e-4), so the identity holds to the accuracy of the trial.
    - For spline120 most of the defect comes from x in [0.01, 1], where 1/g ~ 1/x^2 amplifies the small near-center
      axis residual. This makes the identity a sensitive regression check for near-center accuracy.
    Nonlocal axis-strain formula: c_l - w'(x) = psi_xy(x,0), and the local term -g(x)/4 is the small-circle boundary term in
    the principal value. Rederived. CONFIRMED.
E6. 7.1 positivity repair (y-axis step, requested in NOTES_FOR_TEAM 19:32Z item 5).
    Setup: W_1 is odd in x, so the y-axis is invariant. Along the orbit from the origin, rho(0, y_t) = e^t rho(0, y_0) and
    rho(0, y) = 0 near 0, so rho(0, y) = 0 on the whole orbit; hence rho_y(0, y) = 0 there.
    Derivation: differentiate W_1 rho_x + W_2 rho_y = rho twice in x at x = 0. The terms with W_1, rho_x, W_{2,x} or
    rho_y(0, y) vanish (parity and the previous line), leaving W_2 k' = (1 - 2 W_{1,x}(0, y)) k for k = rho_xx(0, y)/2.
    Along dy/dt = W_2(0, y) this is dk/dt = (1 - 2W_{1,x}) k, so k(y_t) J(t)^2 = e^t k(y_0) with
    J = exp int W_{1,x}(0, y_s) ds. Near 0, k(y) = y a(0, y) > 0 for small y > 0, so k > 0 on the orbit.
    Hypotheses: rho in C^2, W in C^1, and W_2(0, y) > 0 for y > 0, so that the orbit from 0 is the whole positive y-axis;
    the last is part of Hmin. CONFIRMED.
Verdict: sections 7.1 (positivity repair), 7.2, 7.3, 8 and 9 are correct as stated, with the conditions the notes already give: the finite part
needs smooth axis data, the IBP form holds only for 1 < A < 2, and the sequence use of Lemma 8 is conditional. They may
enter FINAL_REPORT with these conditions. None of them is an endpoint.

## Part 10. Pre-candidate checks of the construct1 trial fields (astra construct1 in the lead lane: spline60 and spline120 preliminary exports, field files of 19:22:46Z and 19:39:48Z), recorded 2026-10-17T20:10Z
These exports are trial fields of a spline-ansatz Newton/Krylov fit, not a published candidate (no REPORT.md,
final_candidate.npz or final_shape.npz exists). The checks below are what any construct1 candidate will be held to.

F1. Independent evaluation (code/vcand.py). Method: only the sampled rho of the export is read. Odd sine modes by exact DST,
    m <= 319 (spline60) or 479 (spline120), on 4(nq - 1) angles; own polar inverse (T1); own c by formula C3 with own power-law
    tails; c_l = (1 + c)/3 (identity, the exporter's c_l is not used); own derivatives; R = W.grad rho - rho, normalized by
    sup(|rho| + |X.grad rho| + |U.grad rho|) in each radial band (relsup) and pointwise (relpt); E = -Lap psi - d_x rho with
    psi re-differentiated by FD/FFT. spline120 at m <= 239 and m <= 479 gives the same numbers to all printed digits.
    Results (spline60 N 1024 / spline120 N 1536, r in [7.65e-4, 7652]):
      c: 15.726177 vs exporter 15.726118 / 15.729126 vs 15.729082 (rel. 4e-6 / 3e-6)
      c_l (identity): 5.575392 vs exporter 5.575373 / 5.576375 vs 5.576361
      parity defect 7e-14 / 7e-14; reconstruction of the exported rho from my modes 6e-12 / 7e-13
      a = rho/(x^2 y) at r0: 1 - 7e-9 (all three exports); rho > 0 in the open quadrant (all grid points)
      x* = 8.60120 / 8.60093; mu1 = 10.1507 / 10.1527; h(P) = 1.000047 / 1.000055; w' + h - 2 c_l at P: 2e-12 / 2e-12
      no other zero of W_1(x,0) for x > 1.5 x* (Hmin on the x-axis, within the box)
      relsup (relpt) by band, spline60:  [r0,1e-2] 8e-10, [1e-2,1] 1.5e-6, [1,10] 1.0e-3 (1.8e-3), [10,100] 3.2e-4 (1.2e-3),
                                         [100,1e3] 8.7e-5, [1e3,R] 7.1e-5 (2.3e-4)
      relsup (relpt) by band, spline120: [r0,1e-2] 7e-9, [1e-2,1] 5.0e-8, [1,10] 7.9e-5 (1.3e-4), [10,100] 1.4e-5 (7.0e-5),
                                         [100,1e3] 3.1e-5 (8.4e-5), [1e3,R] 1.89e-3 (2.08e-3)
      my U vs exporter U, relative by band: 3e-6 for r < 10, 2e-5 to 1.4e-4 for 10 < r < 1e3, 1.0e-3 to 1.2e-3 for r > 1e3
      (far-field closure difference; it changes the residual by less than 1e-6 because U/(c_l r) is about 6e-4 there).
    Verdict: the exporter's c, c_l, U and residual are reproduced by independent code; c_l is the identity value
    (3 c_l - c - 1 = 0 by construction in my evaluation and agreement with the exporter's c_l to 3e-6), the x^2 y jet with
    a(0) = 1 and the parity are exact, h(P) = 1 to 5e-5, no hidden wall condition (the transport is outflow at r = R and
    the velocity is the full-plane modal law with the canonical gauge, verified by the agreement of U). CONFIRMED.

F2. Finite-box artifact in spline120. Method: band residuals above, plus the exporter's own residual array. The exporter's
    headline regions are inner r <= 2 and annulus 2 <= r <= 10 (diagnose.py); its "whole" value is 1.32e-3. Exporter
    residual profile (max over angle / band normalization): 1.2e-6 at r = 1008, 2.0e-6 at 2017, 6.9e-5 at 3005,
    1.03e-3 at 5243, 2.12e-3 at r = R = 7652 (at theta = 0.61). My evaluation gives 1.89e-3 on [1e3, R].
    The residual is smooth and grows toward R, so it is not noise: the field does not satisfy c_l r rho_r = rho + O(U) near
    R. spline60 and spline80 do not show this growth. The likely cause is the fitting setup of krylov_free_120x100 (its
    run_configuration has no fit_radius; the 160x100 run sets fit_radius 1000), not an equation property.
    Verdict: the small spline120 residual holds on r <~ 3000 only. "Small residual" read on the 2 <= r <= 10 annulus is not
    a global statement. Any claim that spline120 solves the equation at the 1e-4 level on its whole box is REFUTED
    (whole-box residual 1.3e-3 to 2.1e-3).

F3. Residual level across the trials (band 2 <= r <= 10, exporter values, confirmed by me for 60 and 120):
    1.0e-3 (spline60), 2.1e-4 (spline80), 8.4e-5 (spline120). The radial and angular grids are already converged for each
    trial (my M239 = M479), so the residual is the fit error of the ansatz. It is 1.5 to 3 decades above the prompt's
    1e-6 level. Verdict: no trial field meets the YES threshold. OPEN (not a candidate).

F4. Regularity, B_3. Method: (a) the exporter's diagnostics; (b) my axis B_3 from my own traces (code/vb3.py) and from the
    exported axis arrays (code/b3_export.py); (c) the tool's accuracy at the trial's parameters (code/test_vb3_A10.py).
    (a) The ansatz contains a singular basis term |x|^{p-2} y^2 (1 + r^2)^{-p/2} T_j(cos theta) (global, not localized), with
        leading coefficient B3_ansatz = L^{-p} sum (-1)^j b_j = 5.50e-6, stable between trials. Its homogeneous part
        B3 H is 8 to 43 percent of G_3 on [0, x*]. The lead's own fitted B3 values (-2.65, -0.55, -0.36, 0.92) are
        ill-conditioned and carry no information.
    (b) My finite-part estimates: 2.4e-5 (spline60, m <= 319), 4.9e-5 (spline120, m <= 479). The pieces cancel: fp0 3.6e-4,
        middle -3.0e-4, end -9e-6. The hybrid estimates B_3(x) = f.p. int_0^x J + G_3(x)/H(x) at x = 0.3, 0.5, 0.7 x* vary
        from 1.6e-5 to 4.5e-5 (spline120) and from -2.8e-5 to 1.3e-5 (spline60). With the exported arrays the estimates
        range from -4e-5 to 1.5e-4 depending on the window.
    (c) On compatible axis data with the same A = 10.15, x* = 8.6 and the export's log grid, vb3 reproduces an mpmath
        reference B_3 = 3.8978e-5 to 7e-7 relative (other cases: A = 10.15, x* = 3: 1.4e-5; A = 3.4, x* = 8.6: 1.4e-5).
    So the scatter comes from the data, not the quadrature. If B_3(x) were x-independent (which holds exactly for a
    solution), the hybrid values would agree. Their spread says the y^3 transport equation on the axis,
    w G_3' + (3h - 1) G_3 = -a2 G_1' - b3 G_1, holds only to the trial's fit error. Measured on the exported arrays, its
    residual relative to the size of its terms is 3e-4 to 3e-3 for x < 0.1 and 1e-2 to 1e-1 on 0.5 < x < x*.
    Verdict: B_3 of the trial fields is not measured; it is not resolved even in sign. What is proved (SPEC v3 Lemma 5) is
    C^infinity implies B_3 = 0. The ansatz carries a nonzero |x|^p y^3 coefficient by design. So a construct1 limit with
    B_3 != 0, if it is confirmed, is not smooth: it would be at most a YES for an explicitly distinguished finite-regularity
    class (the exact class is OPEN, Part 4 S4.5 withdrawn), not for the prompt's setting (a smooth). Showing B_3 -> 0
    needs a control fit with the singular basis term switched off (--singular 0) at the same resolution: if that fit
    reaches the same residual, the singular term is not forced; if it stalls, B_3 != 0 is evidence (not proof) that the
    smooth problem has no solution near this branch. OPEN.

F5. Requirements before construct1 output can be called a candidate (verifier's acceptance list, from the prompt):
    - whole-box residual (all r in [r0, R], all angles), not only the 2 <= r <= 10 annulus, normalized as in F1;
    - three resolutions (radial and angular) and three domains (R or L varied by a factor of at least 10, SPEC D11 does
      not apply at c_l = 5.58 but the far-field closure must still be varied), with c_l, x*, h(P), B_3 stable;
    - normalized residual near 1e-6, evaluated by my code on the exported rho;
    - B_3 reported with the --singular 0 control (F4), and D9, D10 values;
    - an explicit statement of the class (smooth versus finite regularity) matching the measured B_3.

## Part 11. Audit of the construct1 final candidate (lead lane astra/construct1: final_candidate.npz, final_shape.npz, REPORT.md, PROOF.md), recorded 2026-10-17T20:51Z
G1. Generator re-implementation (code/gen_shape.py). Method: the global trial formula of PROOF.md and stationary.py, coded
    again from the parameters stored in final_shape.npz only (k, L, spline coefficients, singular coefficients, origin
    multiplier eps = 0.02). It reproduces final_shape rho to 3.9e-14 and final_candidate rho (2560 x 641, r to 76520) to
    4.2e-14 (relative to max |rho|). So the exported field is exactly the global formula; it is defined for all r, with
    rho / r^k tending to a fixed angular profile with corrections of order r^(k-1). No exterior closure is needed for the
    density, and the field can be evaluated on any domain. CONFIRMED.

G2. Independent evaluation of final_candidate.npz (code/vcand.py, code/vprof.py; only the sampled rho is read; odd modes
    m <= 639 by exact DST on 2560 angles; own inverse, own c by formula C3 with an own one-term power tail beyond
    R = 76520; c_l = (1 + c)/3; own derivatives; normalization as in Part 10 F1).
      reconstruction of the exported rho from my modes 1.2e-13; top-mode share 5.6e-15; parity defect 1.0e-13
      c = 15.7289669 (exporter 15.7289656, relative 8e-8); c_l = 5.5763223 (exporter 5.5763219)
      x* = 8.6008822, mu1 = 10.1526468, h(P) = 0.99999777, w' + h - 2 c_l at P: -2e-12, no other zero of W_1(x, 0)
      U against the exporter's U, relative by band: 8e-8 [r0, 0.01], 8e-8 [0.01, 1], 3.4e-7 [1, 10], 6.5e-7 [10, 100],
      4.2e-6 [100, 1e3], 1.8e-4 [1e3, R] (the last is the one-term versus two-term closure next to R)
      residual by band, relsup (relpt):
        [r0, 0.01]  2.1e-8 (7.1e-8)
        [0.01, 1]   1.3e-7 (5.7e-6)
        [1, 10]     1.72e-5 (3.23e-5)   the maximum is next to P
        [10, 100]   1.4e-6 (3.6e-6)
        [100, 1e3]  1.7e-6 (4.5e-6)
        [1e3, R]    1.27e-6 (5.9e-6)
      residual profile divided by the global denominator (875.33, the same number in my evaluation and the exporter's):
      mine 4.8e-10 (r = 1), 1.3e-7 (r = 5), 1.1e-6 (r = 10), 2.7e-7 to 1.2e-6 on [30, 7.2e4]; exporter's 4.8e-10, 1.4e-7,
      9.9e-7, 1.2e-7 to 7.8e-7. They agree within a factor 2; mine is larger for r > 30 (closure, as in Part 10).
      relE (Poisson check) 1.2e-4 on [r0, 0.01] (my FD re-differentiation next to r0) and 1.2e-6 or less elsewhere.
    Verdict: the exporter's c, c_l, U, x*, h(P) and residual are reproduced by independent code. The residual is near 1e-6
    away from P and 1.7e-5 (band) / 3.2e-5 (pointwise) next to P. CONFIRMED as stated in REPORT.md and in the lead's
    20:14Z note; the target 1e-6 is NOT met next to P.

G3. c_l identity on an extended domain (code/taylor5_meas.py on gen_shape output, r in [1e-4 L, 1e7 L], own tails beyond
    7.65e7): own c = 15.7289656161 against the nominal 3/k - 1 = 15.7289656266, relative 6.7e-10, so c_l from my own
    inverse is 5.5763218720 (REPORT.md: 5.576321872040). The trial imposes c_l = 1/k and fixes c = 3/k - 1 through the scale
    L; the agreement shows that the canonical strain of the field itself satisfies 3 c_l - c = 1. c_l is not fitted
    separately from rho. Under basis refinement (lead, 20:14Z, each export on its own grid) c_l = 5.5763606, 5.5763231,
    5.5763219 (degrees 120, 160, 200). CONFIRMED.

G4. D9 (axis integral identity with defect, PROOF.md). My evaluation of the left side minus 1/x* gives 8.642e-4 (REPORT.md
    8.64e-4). By the defect form (1/A) int e/g^2, the weight g^-2 ~ x^-4 amplifies the axis transport defect near the
    centre, so this number measures the centre layer (G7), not the residual near P. CONFIRMED value; it is not small.

G5. D10 (weighted identity Q3 = pi (c_l - 1) c): relative defect -2.6e-7 (Q3 226.134364 against 226.134422, power tail
    beyond R 2.0e-5). CONFIRMED.

G6. D13 (lead 20:20Z). Rederived: psi_xy(P) = (1/pi) PV int rho(P + Z) sin(3 arg Z) |Z|^-3 dZ - g(P)/4 (K2 = d_x d_y G =
    sin 2phi / (2 pi r^2), d_x K2 = -sin 3phi / (pi r^3), small-circle term -g(P)/4), and psi_xy(P) = h(P) - c_l. So D13 is
    the source condition h(P) = 1 computed by a direct PV quadrature. With my h(P) its defect is pi (h(P) - 1) = -7.0e-6
    (absolute, relative 7.8e-7); the lead's quadrature gives -1.9e-5 (relative 2.1e-6), consistent within the stated
    quadrature agreement of 1e-6 relative. CONFIRMED as an identity; it is not evidence independent of D3, and h(P) = 1 is
    a penalty row of the construct1 objective.

G7. D14 (centre Taylor relations, lead 20:26Z). code/taylor5_ver.py (sympy): with a = 1 + delta x^2 + gamma y^2 and
    psi = c xy + alpha xy^3 + beta x^3 y, Poisson gives alpha + beta = -1/3, and the residual has x^4 y coefficient
    E = beta - 2 A delta and x^2 y^3 coefficient D2 = (4A + 2) gamma - 5 alpha. code/taylor5_meas.py measures delta, gamma
    from H on rays at r = 1e-3 and 2e-3 (Richardson) and alpha, beta from my inverse (p_4 / r^4 -> (beta - alpha)/8,
    with (p_2 - c r^2/2)/r^4 -> -1/12 checked). Final: alpha -0.100876, beta -0.232457, delta -0.011821, gamma -0.012130,
    E +0.00758, D2 -0.01250 (lead: +0.0076, -0.0125). Under basis refinement (krylov_free exports, my code):
      basis     E          D2
      80x60     0.00130   -0.00119
      120x100   0.00244   -0.00320
      160x100   0.00532   -0.00877
      200x100   0.00758   -0.01250
    while beta - alpha agrees to 7 digits. The objective's rows start at shape radius 0.04 (physical 0.31), so the centre
    jet is not constrained and drifts away from the required values as the basis is refined. CONFIRMED (D14), and
    FINDING: the fifth-order centre jet does not converge under refinement; it gets worse.

G8. y^3 axis transport (T3, lead 20:14Z item 5e). Own traces on [0, x*] (code/vprof.py, R3 = (w G3' + (3h - 1) G3 - F3)
    divided by |w G3'| + |(3h - 1) G3| + |F3|): -1.0e-2 (x = 0.03), -6.0e-3 (0.1), -3.7e-3 (0.15), -2.8e-3 (0.2), -7.8e-3
    (0.3), +2.2e-2 (0.5), +1.1e-1 (1.0), maximum 0.20 at x = 0.76, -2.3e-2 to -3.2e-2 on [2, 6], -4.4e-2 to -7.9e-2 on
    [7, 8.4], -5.6e-2 and -4.8e-2 on either side of P; 6.8e-4 at x = 10 and below 1.4e-5 for x > 20. For x < 0.01 my third
    derivatives next to r0 are not accurate and are not reported. For x much smaller than 0.15 the Taylor terms predict
    D2 / (2A|gamma| + (12 c_l - 4)|gamma| + 5|alpha|) = -0.0083, the same size as the values on [0.03, 0.2]. The linear axis
    equation R1 (w G1' = (1 - h) G1) holds to 2e-8 to 1e-5 on [0.01, 7] and 3e-4 to 8e-3 within 0.25 of P. So the trial's
    y^3 coefficient satisfies its transport equation only to 1 to 20 percent on [0.3, x*]. The 2D residual is small because
    it does not see the high angular derivative (the residual has angular content up to the trial's mode 200). OPEN item
    for B_3, not a contradiction of G2.

G9. B_3. vcand on final_candidate: B_3 = 5.12e-5 (0.43 in the lead's natural units B_3 x*^(p3 - 2), factor 8361), hybrid
    values at 0.3, 0.5, 0.7 x*: 0.19, 0.37, 0.40. With the exported axis arrays, window (t_lo, t_c) and H formula varied
    (natural units):
      H formula   (0.01,0.3)  (0.02,0.3)  (0.005,0.4)  (0.01,0.4)  (0.01,0.2)
      h            0.428       0.213       0.386        0.313       1.346
      h_eff       -0.002       0.140       0.188        0.201      -1.229
      w-only      -0.030       0.135       0.175        0.194      -1.396
    The lead's 20:44Z estimate 0.30 +- 0.03 is the spread between exports with one method. On one export the spread over
    methods and windows is -0.03 to 0.43 without the (0.01, 0.2) window and -1.4 to 1.35 with it. By the interpretation
    identity (CONFIRMED, Part 10 and WORKLOG 20:39Z) the finite part equals the trial's own B_3 (0.046 natural units) plus
    f.p. int D/(wH), and G8 shows D is 1 to 20 percent of its terms; G7 shows the centre layer, which the near-0 fit sees,
    worsens with refinement. The lead's own caveat ("an error common to the family") applies. Verdict: B_3 of construct1 is
    NOT measured; the +- 0.03 error bar is NOT SUPPORTED. The sign of B_3 is undetermined. OPEN.
    SUPERSEDED by G14: the window and method spread above is largely an artifact of the endpoint piece of vb3.b3
    (degree-5 extrapolation next to x*). With a corrected estimator the w-only value is about 0.33 +- 0.06.

G10. PROOF.md (mtime 20:08:22Z), re-audited in full: dynamic normalization and rescaling; log-radius Green formulas
    q = (A + B)/2m, v = (B - A)/2, B(log R) = f/(m - 1 - k); the Gaussian closed forms A_2, B_2, A_4, B_4 and c = 1/8; the
    shape normalization equation; the matched coordinate q; smoothness of the origin multiplier (r^2/(r^2 + eps^2))^(m-1);
    the singular coefficient L^-p sum (-1)^j b_j; the two-term exterior and the quotient bound (|sin m t tan t| <= m, m
    even); the axis jet formulas a_t, b_t, a_tt, b_tt, A_2, B_3^W, G_3; D9 with defect and the D10 equivalence. All
    identities check. CONFIRMED as method identities. PROOF.md claims no existence, and none is implied.

G11. The prompt's verifier checklist, for final_candidate:
    - hidden wall boundary conditions: none. The density is a global formula (G1); the transport is outflow at the outer
      radius (W.n = c_l r + U_r with |U_r| / (c_l r) about 6e-4 far out); the velocity is the full-plane modal law with
      decaying tails, reproduced by my inverse (G2). CONFIRMED absent.
    - harmonic-gauge freedom: canonical law, no lambda xy and no added homogeneous solution; my c from formula C3 agrees
      (G2, G3). CONFIRMED.
    - forgotten far-field terms: my c with tails on a domain to 7.65e7 agrees to 6.7e-10 (G3); U differences next to the
      export's R are one-term versus two-term closure and change the residual by less than 1e-6 there. CONFIRMED for this
      fixed trial; the residual on the extended domains is G12 (pending).
    - wrong parity: even in x, odd in y by construction; parity defect 1e-13. CONFIRMED.
    - wrong x^2 y jet: H(0) = 0 exactly (the first spline is omitted), a(r0) = 1 - 7e-9. CONFIRMED. The fifth-order jet is
      inconsistent with the equation (G7).
    - independent fitting of c_l: not present (G3). CONFIRMED.
    - convergence to the zero state: rho = x^2 y a with a(0) = 1 and rho > 0 in the open quadrant. CONFIRMED nonzero.
    - finite-box artifacts: the spline120 growth near R (Part 10 F2) is absent; the band residual is flat near 1.2e-6 to
      2.2e-6 on [1e3, 7.2e4]. CONFIRMED absent to r = 7.65e4; G12 extends this.

G12. Extended-domain residual of the same trial (code/gen_shape.py field on r in [7.652e-4, 7.652e7], N 3520, 641 angles,
    M639, own tail beyond 7.65e7; vprof, recorded 2026-10-17T20:59Z).
      c = 15.7289656161 (nominal 3/k - 1 = 15.7289656266), c_l = 5.5763218720; parity 3.6e-13; top-mode share 7.8e-15
      D10 relative defect 4.1e-10 (on the export box it was -2.6e-7, limited by the power-tail extrapolation)
      x* = 8.6008814, mu1 = 10.1526479, h(P) = 0.99999582 (export box with my one-term tail: 0.99999777; so the far-field
      closure moves h(P) by 2e-6, and h(P) - 1 = -4.2e-6 is the better value), no other zero of W_1(x, 0)
      B_3 (vb3) 5.09e-5, hybrid 2.28e-5, 4.43e-5, 4.78e-5: the same as on the export box
      residual by band, relsup (relpt):
        [r0, 0.01] 2.1e-8 (6.7e-8);   [0.01, 1] 1.3e-7 (5.7e-6);   [1, 2] 1.0e-7 (1.7e-6);   [2, 10] 1.79e-5 (3.37e-5);
        [10, 100] 1.3e-6 (3.3e-6);    [100, 1e3] 8.8e-7 (2.6e-6);  [1e3, 1e4] 1.2e-6 (2.9e-6);
        [1e4, 1e5] 6.7e-7 (1.9e-6);   [1e5, 1e6] 3.3e-7 (1.0e-6);  [1e6, 7.65e7] 4.2e-8 (2.0e-7)
      per-r maximum over angles divided by the per-r norm: 9.3e-7 (r = 1e4), 5.0e-7 (1e5), 9.2e-8 (1e6), 1.5e-8 (1e7),
      3.3e-9 (7e7). The residual decays outward, roughly like r^-0.6 for r > 1e4.
    Verdict: on a domain 1000 times larger than the export, the trial has no finite-box artifact, the far field satisfies the
    equation better than the interior, D10 holds to 4e-10 and c_l is unchanged. The binding defect stays next to P
    (1.8e-5 band, 3.4e-5 pointwise). CONFIRMED (far field); the near-P defect is unchanged. The near-P and axis-band
    statistics come from the R = 7.65e5 run (new vprof), still running.

G12 addendum (recorded 2026-10-17T21:27Z). Resolution series of my evaluation on a domain to r = 7.652e5 (gen_shape field, r0 =
    7.652e-4, 641 angles; N 2880 with M639 and N 2160 with M479), vprof with near-P disks and axis bands:
      run                          c               c_l            x*           mu1          h(P)         D10
      N2880 M639 (R 7.65e5)        15.7289656457   5.5763218819   8.60088146   10.15264774  0.99999602   -5.4e-9
      N2160 M479 (R 7.65e5)        15.7289656461   5.5763218820   8.60088210   10.15264223  1.00000153   -5.5e-9
      N3520 M639 (R 7.65e7, above) 15.7289656161   5.5763218720   8.60088142   10.15264792  0.99999582    4.1e-10
    Band residuals relsup (relpt), N2880 / N2160:
      [r0, 0.01] 2.1e-8 (6.8e-8) / 2.1e-8 (6.4e-8);    [0.01, 1] 1.3e-7 (5.7e-6) / 1.3e-7 (5.7e-6);
      [1, 2] 1.0e-7 (1.7e-6) / 9.2e-8 (1.65e-6);       [2, 10] 1.76e-5 (3.31e-5) / 1.39e-5 (2.66e-5);
      [10, 100] 1.3e-6 (3.2e-6) / 7.8e-7 (2.6e-6);     [100, 1e3] 9.0e-7 (2.65e-6) / 8.9e-7 (2.60e-6);
      [1e3, 1e4] 1.2e-6 (3.0e-6) / 1.2e-6 (2.9e-6);    [1e4, 1e5] 6.7e-7 (1.8e-6) / 6.7e-7 (1.8e-6);
      [1e5, 7.65e5] 3.5e-7 (9.4e-7) / 3.5e-7 (9.4e-7)
    Near P: disk |X - P| < 1 relsup 1.5e-5, relpt 1.7e-5 at r = 8.68 (N2880) and 1.8e-5 at r = 8.71 (N2160); disk of
    radius 0.25 relsup 1.0e-5 / 1.1e-5. x-axis band (|sin t| < sin 0.05): [r0, 1] 4.2e-7 (3.2e-6 at r = 0.142), [2, 10]
    4.8e-6 (1.7e-5), [100, R] 2.3e-7 (5.9e-7). y-axis band: [r0, 1] 1.8e-7 (5.7e-6 at r = 0.148), [2, 10] 3.7e-7 (7.1e-7),
    [10, 100] 1.2e-6 (2.6e-6), [100, R] 1.1e-6 (3.0e-6).
    Reading: the residual does not change between N2160/M479, N2880/M639 and N3520/M639 except where the grid points fall
    next to P (25 percent in the [2, 10] band), so it is a property of the trial and not of my evaluation. The largest
    defect is on the x-axis next to P. The pointwise maxima in [0.01, 1] are at r = 0.142 to 0.148, the scale of the
    trial's origin multiplier (shape radius 0.02 times L = 0.153). CONFIRMED: resolution independent; the near-P defect
    1.5e-5 to 1.8e-5 is a property of construct1.

G13. Verdict on construct1 final against the YES standard (prompt; SPEC v4 section 8 = Part 10 F5):
    - normalized residual about 1e-6: met away from P, NOT met next to P (1.7e-5 band, 3.2e-5 pointwise, by my code);
    - systematic improvement under refinement: next to P the series 1.4e-4, 6.0e-5, 3.3e-5 (degrees 120, 160, 200) falls
      roughly like degree^-2.8, which would need degree near 700 for 1e-6 (an extrapolation, not a measurement); the
      centre jet gets worse under the same refinement (G7);
    - stable normalization and c_l: yes (a(0) = 1 exact, c_l stable to 1.2e-6 between the last two degrees, G3);
    - nonlocal and far-field checks: c and U reproduced, D10 to 2.6e-7, D13 to 2e-6, D9 8.6e-4 (G4);
    - second independent solver: not yet (numerics lane assigned, lead 20:30Z);
    - class: the trial contains a singular |x|^p y^3 term by design and B_3 is not measured (G9), so no class statement
      (smooth or finite regularity) is supported.
      Update (G14): the trial's w-only B_3 is about 0.33 +- 0.06 natural units and positive. Whether this is B_3 of a
      solution is open, so the class statement is still not supported.
    construct1 final_candidate is a strong approximate profile whose numbers are independently reproduced: c_l = 5.5763219,
    x* = 8.60088, h(P) = 1 - 4.2e-6. It is not YES-level evidence: the residual target is missed next to P by a factor 17
    to 32, the centre jet diverges under refinement, there is no second solver and the class is undetermined. OPEN. The
    team may NOT finish on this candidate.

G14. w-only B_3 (lead analysis 7.3, scripts/b3_wonly_export.py; lead notes 20:44Z and 20:57Z), evaluated independently
    with code/vb3w.py, code/vb3c.py and scratch/b3_end.py. Recorded 2026-10-17T21:27Z.
    (a) Input. w = W_1(x, 0) comes from my own inverse on my gen_shape fields. Relative difference from the lead's export
        (final_diagnostic_fields.npz): 1.7e-12 (x = 0.003), 4e-12 (0.15), 5.9e-12 (0.5), 2.2e-11 (1.5), -5.6e-11 (4),
        -1.9e-9 (6), 3.2e-8 (8), 8.3e-8 (8.5); c_l 5.576321872025 against 5.576321872040. The R 7.65e5 N2160 field
        differs by a uniform factor 1.46e-9 (its c_l) and by 6e-8 next to P. CONFIRMED.
    (b) The lead's estimator (b3_ls.fp_ls through b3_wonly_export, run read-only on my traces in their export format)
        reproduces their table on my data:
          delta 0.4: 0.328 0.318 0.308 0.290 0.270 (degree 8, 10, 12, 14, 16)
          delta 0.5: 0.341 to 0.300
          delta 0.3: 0.314 to 0.111
        I then dropped every least-squares point with |u| < u_lo (u = x/x*), for u_lo = 0.005 to 0.06; the origin layer is
        u < 0.018. The values stay at 0.30 to 0.34 for delta 0.4 and 0.5, and delta 0.3 becomes stable (0.30 to 0.32 for
        u_lo >= 0.03). So the lead's value is not produced by the unfitted origin layer. CONFIRMED.
    (c) Correction of my own estimator. My first w-only runs (vb3w.closed_form and vb3.b3) gave -0.85 to 0.88 across
        windows. Two defects of my code caused this spread:
        (i) the endpoint piece extrapolated a degree-5 fit of the factor next to x*, where my pole-removed traces
            oscillate (a2' at the grid points within 0.2 of x*); it gave +0.31 instead of about -0.2;
        (ii) some windows started inside the origin layer.
        The spread is therefore an artifact of my estimator, not a property of the data. vb3.b3 uses the same endpoint
        method, so the G9 spread (-0.03 to 0.43, and -1.4 to 1.35 with the (0.01, 0.2) window) is not a valid error
        estimate either. G9's verdict ("not measured") is replaced by this item.
    (d) Corrected estimator (code/vb3c.py). Write Phi(u) = q(x* u) = (1 - u)^(beta - 1) phi(u) with beta = 2/A, so that
        B_nat = f.p. int_0^1 u^(1 - p3) Phi(u) du. The integral is split three ways:
          [0, uc]: an even polynomial fitted on u in [u_lo, uc], with its exact finite part;
          [uc, ue]: Gauss-Legendre quadrature of the data;
          [ue, 1]: phi continued from [uf, ux] by a low-degree polynomial (or by the lead pipeline's own phi), with a
                   Gauss-Jacobi weight.
        The integrands of the two pipelines agree to 1e-7 to 3e-5 relative on x in [0.02, 6] and to 1 percent up to
        u = 0.95. For u > 0.96 my pole-removed traces are noisy, while the lead's spline-regularized traces are smooth.
        phi has real structure on [0.8, 1]: -0.048 at u = 0.7, -0.011 at 0.94, -0.028 next to 1.
        I ran 6 near-0 windows (u_lo 0.03 to 0.06, uc 0.3 to 0.5, K 6 to 8) times 6 end treatments (ue 0.94 to 0.96):
          field                          my traces                  lead pipeline on my w
          gen_shape R 7.65e7 N3520 M639  0.281 to 0.395 (med 0.334)  0.280 to 0.395 (med 0.333)
          gen_shape R 7.65e5 N2160 M479  0.278 to 0.395 (med 0.337)  0.281 to 0.395 (med 0.333)
          final_candidate.npz M479       0.281 to 0.395 (med 0.335)  0.280 to 0.395 (med 0.333)
          construct3b s0 checkpoint M639 0.232 to 0.396 (med 0.326)  0.232 to 0.396 (med 0.325)
        The near-0 window moves the value by about 0.01. The end treatment moves it by about 0.11 (0.28 to 0.40); this is
        how phi is continued over the last 5 percent before x*, i.e. within 0.43 of P. With the lead's own end
        continuation the values are 0.304 to 0.325.
    Verdict:
      - The w-only finite part of construct1 is reproduced by independent code from an independent w: about 0.33 natural
        units (3.9e-5 physical), positive in all 288 variants, with an extraction uncertainty of about +-0.06 that is
        dominated by the data next to P.
      - The lead's 0.31 +- 0.03 is CONFIRMED in value. The error bar is too narrow by about a factor 2.
      - OPEN, not confirmed: that this number is B_3 of a true solution. The w-only traces are not exactly consistent at
        x*: the pole residue eps = (mu1 - A)/mu1 is -1.3e-5 to -1.8e-5, i.e. h(P) - 1 is of that order. The end piece is
        set by the region where the 2D residual is largest (G12) and where the y^3 transport defect is 5 percent (G8).
        The decisive test remains a second discretization (lead request 21:01Z; my vdr re-solve).
      - If the value carried over to a solution, B_3 would be nonzero. By the proved implication (C^infinity implies
        B_3 = 0) that solution would not be C^infinity, so it would belong to the weaker finite-regularity class.
        This is a conditional reading, not a theorem about solutions.

## Part 12. DR re-solve, numerics-lane reproduction, integrated-by-parts B_3, SPEC v4.2 section 8, recorded 2026-10-17T22:02Z

G15. DR re-solve from construct1 (lead request 21:01Z: does the trial settle under dynamic rescaling?).
    Method: code/vdr.py (rho_tau = rho - W.grad rho, 7th-order upwind-biased differences in log r, spectral in theta, RK4,
    ghost jet f1 = f3 = r^3/4 inside r0, power-law outer ghosts), started from the construct1 global trial formula
    (code/vdr_c1.py on final_shape.npz), r0 1e-3, R 1e5. Runs:
      A: N1500, M255, cfl 1, c_l = (1 + c)/3 each step;   B: as A with N1000;
      C: as B with c_l frozen at 5.5763220841 (new option cl_fixed), snapshots every 100 steps;
      D: as C with M127 (time step 5e-4, twice that of C);   E: as C with cfl 0.5 (time step 1.25e-4).
    Results (rtrel = sup|rho - W.grad rho| normalized as in Part 8):
      tau     0.025    0.05     0.10     0.15     0.20     0.30     0.40
      C       3.05e-5  5.92e-5  1.96e-4  -        1.45e-3  6.77e-3  2.65e-2
      D M127  -        5.75e-5  1.98e-4  5.79e-4
      E cfl/2 3.05e-5  5.92e-5  1.96e-4
    A and B agree with C in the linear phase (B: 5.915e-5 and 1.964e-4 at tau 0.05 and 0.10, the same as C).
    - Growth: the norm of F - F0 (each radius weighted by the profile scale) grows by 1.84 to 1.99 per 0.025 tau for tau in
      [0.05, 0.2], a rate of 24 to 28 per unit tau, falling to 18 by tau 0.4. DMD on the C snapshots (scratch/dmd_C.py) gives
      leading continuous eigenvalues with real part 16 to 22 and complex pairs whose imaginary parts change with the
      snapshot window. The DMD is not clean, so I quote only the rate, 25 +- 5, and no specific eigenvalue.
    - Shape at tau 0.2: perturbation relative to the profile scale 2.4e-4 in r in [3, 10), 8.8e-5 in [10, 30), at most
      7.4e-6 for r < 3 and 5e-7 for r >= 30. Angular modes m = 11 to 27 dominate (m > 100 at 4e-3 of the maximum). D and C
      have the same shape (cosine 0.947 on m <= 127 at tau 0.15, norm ratio 1.07).
    - Nonlinear phase (B): c_l 5.418 and h(P) 2.08 at tau 0.55; c_l 3.78, h(P) 3.21, rtrel 0.31 at tau 0.98. C was stopped at
      tau 0.40.
    Verdict: CONFIRMED that plain DR does not settle at the trial. The growth does not depend on N (1000, 1500), M (127,
    255), the time step (factor 4) or the c_l coupling, and the mode is smooth and sits around P. So it belongs to the
    linearized DR flow about the trial, not to my grid. This agrees with the numerics lane (NUM_REPORT line 72) and with the
    diverged dynamic runs of construct1 (REPORT lines 300 to 370). It neither confirms nor refutes the candidate, since an
    unstable steady state is still a steady state. Consequence: plain DR cannot be the second independent solver. A
    stabilized method would be needed (Newton-Krylov on the steady equation, or Newton-Picard on the time-T map with the
    unstable subspace treated by Newton). I have not run one.

G16. Numerics-lane reproduction rep_fields_N256M64R3000L10 (NUM_REPORT 3.12), evaluated by my code.
    Method: code/vnum_import.py resamples the export to my log-uniform grid, N1500 on [1e-3, 3000] with 642 angles.
    - It interpolates the exporter's unknown b = a/w: exact cos(2 k theta) synthesis from the midpoint angles, and
      barycentric interpolation in the Chebyshev-Radau variable t, tested to 2.7e-15.
    - Interpolating a instead of b gives a spurious far field (local exponents of 45 at r = 2900), because b carries a
      Chebyshev tail of 4e-8 to 1e-5.
    - Then code/vcand.py with Mmax 131.
    Result:
    - c = 15.735976, c_l = 5.5786587 by the identity (exporter 5.5786423), x* = 8.603162, h(P) = 1.00028, D10 defect -2.4e-5.
    - relsup by band:

      | band | relsup |
      |---|---|
      | [1e-3, 1e-2] | 1.5e-6 |
      | [1e-2, 1] | 7.4e-6 |
      | [1, 2] | 1.2e-5 |
      | [2, 10] | 4.6e-5 |
      | [10, 100] | 7.2e-4 |
      | [100, 1e3] | 3.8e-3 |
      | [1e3, 3e3] | 2.8e-4 |

    - The exporter's 2.3e-8 is a value at the collocation nodes. The top angular share of b is 1.35e-4.
    Verdict: CONFIRMED that this reproduction is not a second solver at the YES standard. Between nodes the residual is
    1e-5 near P and up to 4e-3 in the far field, and its c_l differs from construct1 by +2.3e-3, which is within its own
    error. The lead's 21:29Z and 21:49Z notes reach the same conclusion from the non-converged LM runs.

G17. Lead analysis.md section 12 (integrated-by-parts w-only B_3; lead notes 21:39Z).
    (a) Identity, by hand.
        - With m = -w/g and g'/g = (w' - A_g)/w, m' = -A_g/g, so d(m^(beta-1)) = (1 - beta) m^(beta-2) (A_g/g) dx. kappa
          is constant, so (a2/g^3)' = (a2/g^3 - kappa)'. Integrating by parts on [eps, x* - eta] gives the stated form plus
          boundary terms.
        - At x* - eta: a2/g^3 - kappa = O(eta) and m^(beta-1) = O(eta^(beta-1)), so the term is O(eta^beta) -> 0.
        - At eps: (a2/g^3) m^(beta-1) = eps^(-4-beta) times an even series, and kappa m^(beta-1) = eps^(1-beta) times an
          even series. The finite part discards all these powers unless an exponent vanishes: -4 - beta + 2j = 0 (beta even)
          or 1 - beta + 2j = 0 (beta odd).
        - Likewise the integrands, J1 = x^(-5-beta) (even) and J2 = x^(-beta) (even), have no 1/x term (no logarithm)
          under the same condition.
        - So the identity needs beta not a positive integer. For A > 1, beta lies in (0, 2) and the only excluded value
          is beta = 1 (A = 2, c_l = 1.5). It comes from the kappa term and is not covered by the lead's wording "not an
          even integer".
        - At beta = 0.197 the identity holds.
        - A_g only has to be the same in g and in the identity. For a solution with h(P) = 1, mu1 = A and A_g = A. For
          the trial, (mu1 - A)/A = 3.3e-7 (construct1, my traces) and -2.5e-8 (construct3b).
        - Correction to G14: the residue eps = -1.3e-5 to -1.8e-5 quoted there came from a local polynomial fit of w on
          +-0.1 x* and is biased. The spline of the analytic w' at x* gives h(P) - 1 = A - mu1 = -3.4e-6, consistent with
          the -4.2e-6 that vcand obtains from the density traces.
        CONFIRMED, with the correction beta != 1 in the stated conditions.
    (b) Own implementation code/vb3ibp.py, independent of notes/b3_ibp/b3_ibp.py.
        - g: cumulative integration of a spline in u = log x on my log grid.
        - Near 0: Legendre least squares of x^(5+beta) J1 and x^beta J2 in (x/xc)^2, with exact finite parts.
        - Middle: Gauss-Legendre in u on a spline restricted to [xc, xe].
        - End: J = (x* - x)^(beta-1) S, with S fitted by a degree-6 polynomial or a spline on [xe - 0.03 x*, x*), then
          the substitution s = (x* - x)^beta with Gauss-Legendre in s (not Gauss-Jacobi).
        - 32 variants: xc/x* in {0.25, 0.35}, xlo/x* in {0.02, 0.04}, K in {6, 8}, xe/x* in {0.85, 0.92},
          end in {polynomial, spline}. w'' is taken from both the finite difference and the mode ODE.
        - The original form (1/(3N)) f.p. int (a2/g^3)' m^(beta-1) is evaluated with the same pieces, with a2' from the
          spline.
        Manufactured test, on the lead's w = -A x (1 - x^2)/(1 + x^2) (1 + 0.3 x^2 (1 - x^2)), x* = 1:
        - c_l = 5.5763218720, N3000: IBP median 14.410146, original form 14.410121, all variants in [14.40952, 14.41016].
          The lead has 14.41017.
        - c_l = 2.2: both forms give 2.109471.
        So the two forms agree numerically to about 1e-6, and my quadrature agrees with the lead's.
        My traces (own inverse, runs/ibp/tr_*.npz), natural units:

        | field | x* | (mu1 - A)/A | IBP median [range] | original form median [range] |
        |---|---|---|---|---|
        | gen_shape R1e5 N2160 M255 | 8.600881 | 3.3e-7 | 0.3060 [0.2981, 0.3450] | 0.319 [0.219, 0.689] |
        | construct1 final_candidate M479 | 8.600882 | 3.3e-7 | 0.3049 [0.2970, 0.3438] | 0.316 [0.216, 0.683] |
        | construct3b s0 deg160 M639 | 8.600881 | -2.5e-8 | 0.3067 [0.2788, 0.3723] | 0.319 [-0.015, 0.772] |
        | construct3b s6 deg160 M639 | 8.600876 | -2.5e-8 | 0.3067 [0.2788, 0.3719] | 0.319 [-0.014, 0.770] |

        - The choice of w'' (FD or ODE) changes nothing at these digits.
        - The near-0 finite part sets the range. With the fits of residual <= 6e-7 (xlo = 0.04 x*), the IBP values are
          0.298 to 0.306 (R1e5) and 0.279 to 0.306 (construct3b).
        - The maxima, 0.34 to 0.37, come from xlo = 0.02 x*, K = 8, xc = 0.25 x*. The near-0 piece is 1.41 to 1.48 against
          a total of 0.30, and its x^(-1-beta) coefficient is amplified by 1/beta, about 5. This matches the lead's
          sensitivity statement (21:49Z, item 3).
        - The original form is badly conditioned (a2' at small x), which confirms the reason for the IBP form.
        - The lead's code on my w (runs/ibp/lead_code_on_my_*.txt): R1e5 0.3025 [0.3000, 0.3034], R1e7 0.3021
          [0.2996, 0.3030], final_candidate 0.3024 [0.2999, 0.3032], construct3b 0.3049 [0.2994, 0.3060].
    Verdict:
      - CONFIRMED: the trial's w-only B_3 is about 0.30 natural units. My code gives a median of 0.305, and the lead's
        code on my w gives 0.302 to 0.305.
      - It is positive in all 128 IBP variants of my code on four fields. The extraction spread is about -0.03/+0.07 and
        is dominated by the near-0 fit window.
      - This replaces the +-0.06 of G14, whose spread came from the end piece of the original form.
      - OPEN: B_3 of a true solution. With a sensitivity of about 1e6 per unit relative error of w near 0, w must be right
        to about 1e-8 relative near 0 for an accuracy of +-0.01. No second solver has established that accuracy.

G18. SPEC v4.2 section 8, the proposed rule for an unmeasured B_3 (problem P_B; SPEC lines 262 to 266).
    I agree, with four conditions.
    (1) P_B is an explicitly distinguished problem in the sense of PROMPT line 62, and it is weaker than the posed strong
        setting (a smooth and even). Evidence for P_B is not a YES for the posed problem. The report must say so in its
        first lines, and must say that the strong setting is not answered. Given PROMPT lines 8, 25 and 123, I will not
        count a P_B result as one of the two requested deliverables. It may be reported as the strongest result
        established, with the gap stated.
    (2) Every YES standard applies to P_B in full: normalized residual about 1e-6 including next to P, refinement, stable
        normalization and c_l, far-field checks, and an independent second solver.
    (3) The trial's B_3 is now measured (G17: about 0.30, positive in every variant), so the "not measured" clause does not
        apply to the trial; the clause of line 256 applies. If a second solver confirms B_3 != 0, the report must state
        that the computed profile is not C^infinity (by the proved implication that C^infinity gives B_3 = 0). That is
        numerical evidence against a smooth profile on this branch. It is not a NO theorem.
    (4) The asserted form a = a_0 + B_3 |x|^(p3 - 2) y^2 a_1 + ... rests on the Lemma 5 expansion, whose 2D regularity
        claim is OPEN (Parts 9 and 11). The class is to be described only as far as proved (SPEC lines 258 to 261).
    Verdict: AGREED, with conditions (1) to (4).
    [Amended 2026-10-17 by G20: the last two sentences of (1) and "an independent second solver" in (2) are replaced by
    G20 (a) and (b).]

G19. Characteristic defect J (lead analysis 13.4, notes 21:55Z), recomputed independently, recorded 2026-10-17T22:21Z.
    Method: code/vchar.py.
    - R, U and c_l come from my evaluator (vcand.main, Mmax 479, sampled rho only). The exporter's W, residual and axis
      data are not used.
    - R/rho is formed on the half-shifted angular grid by exact Fourier interpolation, so no 0/0 is taken on the axes.
    - Quintic tensor splines in (log r, theta).
    - Backward integration by DOP853 at rtol 1e-9 and 1e-11, 24 start angles on r = 20 (lead: 8 angles, cubic splines,
      their own solve_ivp). J is recorded at |X - P| = 0.3, 0.1, 0.03 and 0.01.
    Result, construct1 final_candidate.npz (runs/char/fc_r20.json):
    - J at eps_P = 0.03 ranges from -1.273e-4 to +1.63e-5, spread 1.44e-4. The lead has -1.28e-4 to +1.6e-5, spread 1.4e-4.
    - Spread 1.16e-4, 1.19e-4, 1.44e-4, 1.51e-4 at eps_P = 0.3, 0.1, 0.03, 0.01. The tolerance effect is at most 4e-9.
    - R/rho above P at y = 1e-3, 1e-2, 0.1, 0.5, 1, 2: -3.3e-6, -3.8e-6, -3.4e-5, +4.5e-6, -1.19e-4, +1.07e-4. The lead has
      -1.3e-4 at y = 1 and +1.1e-4 at y = 2. As y -> 0 the value approaches h(P) - 1 (-2.2e-6 in my evaluation).
    - Below eps_P = 0.3 the extra contribution is nearly common to all labels (about -3.5e-5). The exception is the label
      next to the y-axis (theta0 = 1.55), which passes the origin (rmin 1.1) and reaches P along the axis.
    Verdict: the diagnostic and its values are CONFIRMED by independent code and data. I accept the reading as a heuristic
    reporting rule, but not as an error bound: quote c_l = 5.576 with an uncertainty of order 1e-3 until the near-P defect
    is reduced.
    - Converting a defect of 1e-4 into an error of c_l assumes a well-conditioned linearization, and that is not
      established. The numerics lane reports a numerically singular Jacobian (smallest singular values down to 4e-9,
      with a c_l component; NOTES_FOR_LEAD 22:02Z). Plain DR about the trial is linearly unstable (G15). The true
      uncertainty may therefore be larger.
    - The 1e-7 stability of c_l within one construction is not an accuracy. The PROMPT's "stable normalization and c_l"
      must be shown by agreement of independent converged solvers.
    [Amended by G20 (b), (c): the c_l wording and the solver requirement are replaced there.]

G20. Standards rulings asked by the lead (NOTES_FOR_TEAM 22:08Z (a), (b); 22:05Z item 3; 22:06Z), recorded 2026-10-17T22:28Z.
    These rulings are binding for DONE. They replace G18 (1), the second-solver clause of G18 (2) and the last sentence
    of G19.
    (0) The 24-hour line. SHIFT_PROMPT.md line 5 prevails over PROMPT.md where they conflict. It waives the 24-hour minimum
        as a gate: a verified endpoint may finish early. The report must record the real T0, T_end and elapsed time, and
        must not claim the 24-hour requirement was met if it was not. My summary sentence that made PROMPT line 25 a gate
        was wrong. It is withdrawn. Verdict: CORRECTED.
    (a) Is an explicitly distinguished finite-regularity result the YES? The position of F5 (Part 10) and SPEC 8 bullet 4
        holds, and G18 (1) is amended. Reasons:
        - PROMPT line 62 has a specific provision: the weaker condition may be used if "the resulting problem" is
          explicitly distinguished. A specific provision governs the general lines 8 and 123.
          - Line 8 concerns formal identities, perturbative calculations, theorems in artificially narrow classes,
            single low-resolution computations and unverified residuals.
          - Line 123 concerns incomplete evidence.
          - A result that meets every standard for an explicitly distinguished problem is neither of these.
          - Line 25 is not a gate here (item 0).
        - P_B is not enlarged ad hoc to make a YES easy. Its singular term B_3 |x|^(p3 - 2) y^2 a_1 is the one forced by
          the centre expansion, and the exponent p3 = 6 + 2/A is fixed by the equation.
        - G18 (1) contradicted F5, which I had set and which was adopted as SPEC 8. The only new fact was the measured
          B_3, and that changes the required wording (G18 (3)), not admissibility.
        Ruling: a result for P_B that meets the standards of item (b) and of G18 (2) to (4) is an admissible endpoint, and
        the team may finish on it once I confirm it. The deliverable must call it "YES, strong numerical evidence, for the
        explicitly distinguished problem P_B". The first lines of FINAL_REPORT must say:
          (i) the posed strong setting (a smooth and even) is not answered by it;
          (ii) the computed branch has B_3 = (value, with its spread) natural units, nonzero. Since C^infinity implies
               B_3 = 0 (proved), this is numerical evidence that the computed branch is not C^infinity, so it is not a
               solution of the strong setting. It is not a NO theorem, and other branches are not excluded;
          (iii) the class is stated only as far as proved (SPEC lines 258 to 261; G18 (4)).
        Advice, not a gate: such an endpoint leaves the strong setting open. Time left after it is best spent on that
        question (a branch with B_3 = 0, or a NO theorem in the smooth class).
    (b) Second solver. I do not require a second converged solver at 1e-6. PROMPT line 108 asks for "different
        differentiation/integration methodology or a separately implemented residual evaluator". Line 105 asks for an
        independent check of the c_l identity. Neither asks for two converged solvers, so G18 (2) was stricter than the
        prompt. The standard for a YES (strong setting or P_B) is:
        (b1) Residuals. My evaluator (vcand/vquad: own differentiation, own full-plane inverse) on the exported rho, over
             the whole sampled domain, by fixed region and pointwise. The regions include the bands next to P, next to
             both axes and around 0. Far-field truncation and inverse errors are quantified separately. At least three
             distinct resolutions and three domains. Normalized residual about 1e-6 including next to P, with systematic
             improvement under refinement. Absolute values are reported too.
        (b2) c_l.
             (i) The identity is checked on each deliverable field by my own psi_xy(0) (G3).
             (ii) Stability under refinement within one construction, and the spread across constructions, are both
                  reported; the spread is called a variant spread, not an error bound.
             (iii) At least one determination that does not use the identity, with its accuracy stated. Examples:
                  h(P) - 1 measured by me on the deliverable (a C^1 condition at P, independent of the identity), and the
                  numerics lane's map Psi or its solver.
             (iv) The numerics lane's spread (5.5728 to 5.5823) is reported. Its explanation (a near-null far-field mode)
                  is labelled a hypothesis unless verified.
        (b3) The characteristic defect J (G19) is reported for the deliverable and decreases under refinement.
        (b4) FINAL_REPORT says plainly what the independent check is:
             - the candidate comes from one construction family (lead constructions 1 to 4);
             - it is checked by a separately implemented residual evaluator;
             - the independent solvers (numerics-lane collocation, my DR) did not converge to it. The numerics-lane
               states have c_l within 6e-3 of it; DR is unstable about it (G15).
             A second converged solver remains desirable but is not required.
    (c) The c_l statement (22:06Z). Method: key c_l of each export, and my own identity value where I have one.
        - Exports at degree >= 120:
          - construct1: spline120 5.5763606, spline160 5.5763231, final 5.5763219;
          - construct2: basis1 5.5763187, basis2 5.5762428, basis3 5.5762481;
          - construct3b: s0 deg120 5.5763605, s6 deg120 5.5763022, s0 deg160 5.5763270, s6 deg160 5.5763219;
          - construct4: c4_centre 5.5763297.
        - Range [5.5762428, 5.5763606], spread 1.18e-4. CONFIRMED.
        - The spread is between constructions. construct2 basis2 and basis3 lie about 8e-5 below construct1, 3b and 4.
        - My identity values on final, c3b s0 deg160, c3b s6 deg160 and c4_centre agree with the export keys to 4e-7:
          5.5763222, 5.5763274, 5.5763222 and 5.5763300.
        - Under refinement within construct1, c_l moves by 3.7e-5 and then 1.2e-6, while the J spread goes 6.2e-4, 2.2e-4,
          1.4e-4.
        Verdict: I accept the withdrawal of "about 1e-3" and the proposed wording. Quote c_l = 5.57632 with a variant
        spread of about 1.2e-4 across constructions (5.57624 to 5.57636). This is not an error bound. Independent-solver
        agreement is only at the numerics lane's accuracy. The G19 sentence "quote c_l = 5.576 with an uncertainty of order
        1e-3" is replaced by this.

G21. Lead analysis 13.6 (C^1 at P forces h(P) = 1 and Phi constant; sketch, 22:05Z), audited by hand, recorded 2026-10-17T22:30Z.
    Claim: if rho is C^1 near the source P, then h(P) = 1, and rho = C eta in linearizing coordinates.
    Check:
    - In C^1 linearizing coordinates W = (A xi, h eta), and any solution of W.grad rho = rho on xi != 0 has the form
      rho = |xi|^(1/A) F(t) with t = eta |xi|^(-h/A).
    - Then d_xi rho = (1/A) sgn(xi) |xi|^(1/A - 1) (F - h t F'). This is correct.
    - At fixed t, the point tends to P as xi -> 0. Since A > 1, a bounded d_xi rho forces F = C_pm |t|^(1/h), so
      rho = C_pm |eta|^(1/h) on each side. Oddness in y gives C_- = -C_+.
    - If h > 1, rho is not C^1 unless C = 0.
    - If h < 1, then d_eta rho = 0 on eta = 0. The fast manifold of P is unique and the x-axis is invariant, so eta = 0 is
      the axis. Hence g = d_y rho(x, 0) vanishes on an interval left of x*. The axis equation w g' = (1 - h(x)) g is linear
      with w != 0 on (0, x*), so g = 0 on (0, x*). That contradicts g ~ x^2 at 0. The argument is correct.
    Hypotheses to state:
    - The planar C^1 linearization (Hartman) needs W in C^2 near P, not just rho in C^1. Since U is a Riesz-type
      transform of rho, a sufficient condition is rho in C^(2,alpha) near P, together with the decay assumed for the
      velocity law.
    - A > 1 and h(P) > 0 (P a hyperbolic source).
    - P_B profiles (non-smooth only through the |x|^(p3 - 2) term at the y-axis near 0) are smooth near P, so the result
      applies to them.
    Verdict: CONFIRMED as a lemma under the stated hypothesis (W in C^2 near P). Consequence: the near-null directions with
    h(P) != 1 or non-constant Phi are not admissible profiles in C^(2,alpha), so the count "identity, h(P) = 1, a(0) = 1"
    applies. The closing reading (infinitely many conditions B_j = 0 for smoothness at 0, so the strong setting is expected
    to fail generically) is a heuristic, as the lead labels it. It is not a NO argument.
    Amendment 2026-10-18T00:51Z (G34 (b)): the Claim line above is stated as local and is false as a local statement
    (W = (2 xi, eta/3), rho = eta^3). The check above uses the global facts g ~ x^2 at 0 and w != 0 on (0, x*), i.e.
    rho_y(x,0) > 0 on (0, x*). That is an additional hypothesis of the lemma; it holds for every A_2 profile (R5, R10).

G22. construct4 step 1: the c4_centre export (lead construct4 REPORT, "Step 1 completed"), audited 2026-10-17T22:42Z.
    Method:
    - code/vcand.py, Mmax 479, on c4_centre_fields.npz. Only rho is read; own inverse, own c, c_l by the identity, residual
      with N_v. Output runs/cand/c4_centre_M479.json.
    - code/vchar.py, r_start 20, 24 angles. Output runs/char/c4c_r20.json.
    - code/vd14.py (new). The D14 jets come from the sine modes f_1, f_3, f_5 of rho at small r. alpha and beta come from
      my own p_2 and p_4; these are exact with modes m <= 9, because d_x couples m only to m +- 1. Output
      runs/cand/c4_centre_d14.json.
    - The IBP B_3 on my own traces (runs/ibp/vb3ibp_c4c.json).
    - scratch/cl_from_h.py (new): c_l from h(P) = 1 with the sampled rho held fixed.
    - Comparison: construct1 final (G2, G7, G12, runs/char/fc_r20.json).
    Results:
    - Basic quantities:
      - c = 15.7289904 (exporter 15.7289891, relative 8e-8).
      - c_l = 5.5763301 (export 5.5763297). This is 7.8e-6 above construct1 final.
      - x* = 8.6008811, mu1 = 10.1526622, h(P) = 0.99999805 (lead 0.999997083 on its common grid).
      - parity 1e-13, top-mode share 1.9e-14.
      - D10 defect -2.5e-7 on the export box (construct1: -2.6e-7).
    - D14 (the G7 finding):

      | quantity | mine | lead |
      |---|---|---|
      | alpha | -0.1008763626 | -0.1008763602 |
      | beta | -0.2324569707 | -0.2324569731 |
      | delta | -0.0114480808 | -0.0114480821 |
      | gamma | -0.0118369907 | -0.0118369917 |

      - a(0) = 1.0000000000 from both f_1 and f_3, and the r^3 sin 5t coefficient is 3e-18, so the x^2 y jet is correct.
      - On fit windows with fit error <= 8e-7: E = -2.4e-8 to -4.8e-8 and D2 = +2.0e-8 to +6.1e-8 (relative <= 2.1e-7).
      - Wider windows (fit error 3e-6) give -1.5e-7 to -1.8e-7. That is truncation of the fit.
      - Lead: E -4.6e-8, D2 +9.6e-8. Construct1 final (G7): E +7.6e-3, D2 -1.25e-2.
      CONFIRMED: the centre relations hold to about 1e-7 relative on c4_centre. The G7 finding is resolved for this fit.
      Whether the jet stays fixed under further refinement is checked on each later fit.
    - Residual with N_v, relsup (relpt) by band:

      | band | c4_centre | construct1 final (G2) |
      |---|---|---|
      | [r0, 0.01] | 6.4e-12 (8.5e-9) | 2.1e-8 (7.1e-8) |
      | [0.01, 1] | 3.0e-8 (9.5e-7) | 1.3e-7 (5.7e-6) |
      | [1, 10] | 1.72e-5 (3.24e-5) | 1.72e-5 (3.23e-5) |
      | [10, 100] | 1.35e-6 (3.3e-6) | 1.4e-6 (3.6e-6) |
      | [100, 1e3] | 1.46e-6 (3.9e-6) | 1.7e-6 (4.5e-6) |
      | [1e3, R] | 1.17e-6 (5.5e-6) | 1.27e-6 (5.9e-6) |

      - relE is 5.8e-5 on [r0, 0.01] (my FD re-differentiation at r0; construct1 1.2e-4) and <= 1.3e-6 elsewhere.
      - The centre repair lowers the residual for r <= 1 by factors of 4 to 3000. It leaves the band next to P unchanged.
        This agrees with the lead's flux table (2 <= r <= 10: max 1.25e-4 after, 1.27e-4 before).
    - J (vchar), Jmin -1.33e-4, Jmax +1.7e-5; R/rho just above P (y = 1e-3) is -2.9e-6.

      | eps_P | 0.3 | 0.1 | 0.03 | 0.01 |
      |---|---|---|---|---|
      | J spread, c4_centre | 1.13e-4 | 1.20e-4 | 1.43e-4 | 1.50e-4 |
      | J spread, construct1 final | 1.16e-4 | 1.19e-4 | 1.44e-4 | 1.51e-4 |

      Lead 12.7 says "unchanged, 1.44e-4". CONFIRMED.
    - B_3, IBP on my own traces, 32 variants: median 0.3006, range [0.2823, 0.3037]. The lower end comes from the variants
      with finite-part window xc = 0.25 x*, xlo = 0.02 x*, K = 8. Construct1 final: 0.3049 [0.2970, 0.3438]. Lead:
      0.3005 [0.2965, 0.3017]. CONFIRMED within the variant spread; quote about 0.30 with range [0.28, 0.31].
    - c_l without the identity (G20 b2 (iii), on the candidate itself). Hold rho, and hence Psi_1, fixed and solve
      h(P) = c_l + Psi_1'(x*(c_l)) = 1 for c_l. The slope dh/dc_l at fixed rho is 1.080.

      | construction | c_l from h(P) = 1 | identity c_l | difference |
      |---|---|---|---|
      | c4_centre | 5.5763327 | 5.5763300 | +2.7e-6 |
      | construct1 final | 5.5763253 | 5.5763222 | +3.1e-6 |
      | construct1, extended domain to r = 7.65e5 | 5.5763250 | 5.5763219 | +3.2e-6 |
      | construct3b s0 | 5.5763271 | 5.5763274 | -2.3e-7 |
      | construct3b s6 | 5.5763220 | 5.5763222 | -2.3e-7 |

      The two determinations agree to 3e-6, i.e. 5e-7 relative. This is about the far-field-closure uncertainty of h(P),
      which moves by 2e-6 between domains (G12).
      This is a consistency check of each candidate with a necessary condition (13.6), not an independent solver.
      CONFIRMED as a second determination of c_l at the 3e-6 level for this construction family.
    - c4_r1 grid failure (construct4 REPORT). Not re-run; recorded as an observation. The lead found that the fit
      quadrature (2048 x 480) was overfit after knot insertion.
      - construct5 initial_grid shows the same for c4_radialtest: objective 9.66e-5 at 2048 radial points against
        2.59e-4 at 4096 and 2.70e-4 at 6144, with h(P) moving from 1.000000004 to 0.99998793.
      - So the near-P improvement claimed for c4_radialtest (flux max 3.2e-5) is not established. It must be measured by my
        evaluator on an export at a grid independent of the fit grid.
      - Later exports (c4_r1, construct5) will be evaluated only that way.
    - Numerics lane (NOTES_FOR_LEAD 22:22Z, 22:35Z). Recorded as reported, not re-run:
      - h-row c_l: 5.5780418 at (256,64) R 3000; 5.5837333 at (192,48) R 1000 (not converged).
      - Psi map on its own (256,64) state: c_l(Psi) = 5.5771531, |Psi(rho) - rho|/rho up to 1.4e-3.
      - These differ from 5.57633 by 1.7e-3, 7.4e-3 and 8.2e-4. They are not determinations of the candidate's c_l, and
        Psi has not yet been applied to the candidate (lead request (i)).
    Verdict:
    - CONFIRMED: c4_centre repairs D14 and the residual inside r <= 1, and leaves c_l, B_3 and J unchanged within their
      spreads.
    - The binding defect is still next to P: relsup 1.7e-5 and pointwise 3.2e-5 (N_v); flux max 1.25e-4 (lead).
    - The YES standard (G20 b1: about 1e-6 normalized everywhere) is NOT met by c4_centre.

G23. FINAL_REPORT.md draft (mtime 22:11Z) and notes/final_sec4_draft.md (22:06Z), audited 2026-10-17T22:34Z.
    Method: read in full and compared against SPEC 8, G18, G20 and my earlier audits (Parts 3, 4, 9). R5 (psi_xy(P) =
    1 - c_l) and the c_l = 3/2 closed form of R10 were rederived by hand. Since A = 2 there,
    g'(P) = w''(P) g(P)/A gives a2(P) = w''(P)(g(P) - 2)/4.
    Results:
    - Section 0 states the waiver correctly: the 24 hours are not a gate, and the elapsed time will be stated exactly.
      CONFIRMED.
    - Sections 1 to 3 contain only claims audited earlier. Their conditions are stated: R7 says the 2D regularity is not
      proved; R10 says the finite part needs an expansion of the integrand factor at 0; R11 states the tail condition.
      CONFIRMED.
    - Inconsistency (must be fixed before any YES). The weaker problem has two different names and definitions.
      - FINAL_REPORT section 1 defines P_m: rho in C^(m,alpha) for some m >= 2, a continuous.
      - final_sec4_draft 4.1 and SPEC 8 bullet 4 use P_B: a = a_0 + B_3 |x|^(p3 - 2) y^2 a_1 + ..., stated by the
        expansion and not by a Holder exponent.
      The deliverable must name one class and use it throughout. Either is acceptable as an explicitly distinguished
      problem (G20 (a)), under two conditions:
      - for P_m, no m above what is shown may be claimed. The candidate is C^(2,alpha) by construction, and the only
        proved consequences of B_3 != 0 are "not C^infinity" and the trace statement "not C^10 (p3 <= 7)";
      - for P_B, the draft's sentence "the trial lies in P_B by construction" is true for the singular-on fits. A
        singular-off fit (construct3b s0) is smooth, so it lies in P_B only as a member of P_inf.
    - final_sec4_draft: its headline and 4.1 follow G20 (a): YES only for the distinguished problem, and the strong
      setting not answered.
      - 4.3 matches G20 (c).
      - 4.4 uses the Cartesian-flux normalization; my evaluator now reports it as well (code/vaudit.py).
      - 4.7 lists the limits.
      - 4.1 still quotes "0.33 +- 0.06 by the external check of the direct form". My G17 replaced that error bar. Quote
        the IBP value with its variant spread, and the direct form only as superseded.
    Verdict: CONFIRMED except for the class inconsistency (OPEN until fixed).

G24. Combined audit tool code/vaudit.py; first application to the numerics lane's (256,64) R 3000 LM state, recorded 2026-10-17T22:51Z.
    Method:
    - code/vaudit.py makes one evaluation with vcand.main (only rho read; own inverse, own c, c_l by the identity). It then
      reports:
      - |R| in two normalizations, on the open first quadrant with axis points and 8 radial end points excluded, by
        physical band and in regions around P:
        - N_v = |rho| + |X.grad rho| + |U.grad rho| (my Part 10 F1 norm);
        - N_f = |W_1 rho_x| + |W_2 rho_y| + |rho| (the lead's construct4 Cartesian flux);
      - x-axis traces from the same inverse and the IBP B_3 (vb3ibp, 32 variants, both w'' routes);
      - J (vchar.run_ev).
    - Input: runs/numchk/n256R3000_N1500b.npz (G16 import of artifacts/data/rep_fields_N256M64R3000L10.npz), Mmax 131,
      r_start 20. Log runs/audit/n256R3000.log; run time 154 s.
    Results:
    - The vcand part reproduces G16 exactly: c_l 5.5786587, h(P) 1.000279, relsup by band 1.5e-6 to 3.8e-3. So vaudit
      agrees with vcand.
    - |R|/N, max (rms):

      | region | flux N_f | N_v |
      |---|---|---|
      | r <= 0.1 | 1.4e-5 (1.4e-6) | 3.0e-5 |
      | 0.1 <= r <= 2 | 1.4e-5 | 2.8e-5 |
      | 2 <= r <= 10 | 3.8e-4 (3.1e-5) | 1.4e-4 |
      | 10 <= r <= 100 | 1.3e-3 (1.9e-4) | 2.0e-3 |
      | 100 <= r <= 1000 | 3.1e-3 (7.5e-4) | 5.3e-3 |
      | r >= 1000 | 1.6e-4 | 5.0e-4 |
      | \|X - P\| < 0.5 | 1.26e-4 | 3.8e-5 |

      - N_f is the stricter norm next to P (factor 3.3 here). N_v is stricter in the far field, because N_v has no
        factor c_l on the X term. Both are reported from now on.
    - B_3 (IBP): median 0.316, range [0.276, 0.322], fit 1.3e-5 (the original form scatters from -2.8 to 0.96).
      - This state is not an independent solve. It is an LM solution started from the projected construct1
        (NUM_REPORT 3.12).
      - Still, the w-only B_3 stays near 0.3 after a different discretization has moved c_l by 2.3e-3. This is weak
        evidence that B_3 about 0.3 is not an artifact of the lead's trial basis.
    - J and h(P): J spread 2.7e-4, 2.7e-4, 4.0e-4, 6.6e-4 at eps_P = 0.3, 0.1, 0.03, 0.01. R/rho just above P is
      +2.78e-4, which equals h(P) - 1 = +2.79e-4.
      - Reason: next to P, rho = y F(xi) + ..., so W.grad rho / rho -> h(P) and R/rho -> h(P) - 1.
      - Consequence: J diverges like (h(P) - 1) log(1/eps_P)/lambda, where lambda is the approach rate (about 1 along
        eta and A along xi). The J spread therefore grows as eps_P -> 0 unless h(P) = 1.
      - For c4_centre, R/rho above P is -2.9e-6 against h(P) - 1 = -2e-6 to -3e-6 (G22), and J converges as eps_P -> 0.
      - So J and h(P) - 1 are consistent diagnostics of the same defect at P. A YES candidate needs both small
        (G20 b3).
    - D14 on this state (code/vd14.py): not measurable from the import. The fits of f_m/r^3 on [1e-3, 0.1] have
      errors of 8e-2 to 5e-1 because of small-r noise in the interpolated b. The numerics lane's own centre fit
      (NUM_REPORT 3.12: +2.3e-7, -3.1e-7) is not checked by me.
    - NUM_REPORT section 4 says "normalised transport residual 1e-8 .. 1e-6". For this state that holds only at the
      collocation nodes (G16). Between nodes, my evaluator gives 1.4e-5 to 3.1e-3 in N_f and 3e-5 to 5.3e-3 in N_v.
      FINAL_REPORT must not quote the nodal figure as the residual of the numerics states.
    Verdict:
    - CONFIRMED: vaudit works, and the numerics state is not YES-level (far field 1e-3).
    - FINDING: R/rho at P equals h(P) - 1, so the J spread as eps_P -> 0 is governed by h(P) - 1.

G25. Lead requests 22:42Z (items 2 and 4) and 23:05Z (item 1), recorded 2026-10-17T23:16Z.
    (a) The class P_2 replaces P_B (the lead's 22:42Z item 2; SPEC 8 v4.3). Binding.
      - CONFIRMED. The headline "YES, strong numerical evidence, for the explicitly distinguished problem P_2" replaces the
        P_B title of G20 (a). The P_2 problem is: the profile equation, parity, velocity law and growth class of the
        strong setting, with "a smooth near 0" replaced by "rho in C^(2,alpha)_loc(R^2), rho = x^2 y a near 0 with a
        continuous, even/even, a(0) = 1".
      - Reason. This is the weaker, cubic-jet-type condition that PROMPT line 62 allows only when it is explicitly
        distinguished. It claims no regularity beyond what the trials have by construction. The expansion
        a = a_0 + B_3 |x|^(p3 - 2) y^2 a_1 + ... then stays a remark, which resolves G23.
      - Conditions; all are needed for DONE:
        1. FINAL_REPORT defines P_2 in full where it is first used. It says in words that P_2 is the weaker problem of
           PROMPT line 62 (a only continuous, not smooth) and that a P_2 result does not answer the stated problem.
        2. The first lines (i) to (iii) are as in SPEC 8 v4.3. In (iii), membership in P_2 holds for the trial by
           construction. That the exact profile near the trial is in P_2 is the numerical claim, not a proved statement.
        3. Analysis 13.6 (G21) applies inside P_2. C^(2,alpha) gives psi in C^(3,alpha) locally (Schauder), hence
           W in C^2 near P. So h(P) = 1 and Phi constant are necessary conditions in P_2. The reported h(P) - 1, R/rho at P
           (G24) and J are therefore P_2 consistency checks and must be listed as such.
        4. Uniqueness within P_2 is not claimed, and other branches are not excluded.
    (b) c_l with rho fixed (the lead's 22:42Z item 4). My scratch/cl_from_h.py (own traces, spline of Psi_1 and Psi_1' in
        log x, x* re-solved for each c_l) gives:

      | field | c_l(h = 1) - c_l(identity), mine | lead | dh/dc_l at fixed rho, mine |
      |---|---|---|---|
      | construct1 final | +3.1e-6 | +1.6e-6 | 1.0796 |
      | c4_centre | +2.7e-6 | +4.2e-6 | 1.0795 |
      | construct3b s0 | -2.3e-7 | +3.2e-7 | 1.0796 |

      The lead's dh/dc_l = 1 - h'(P) x*/A = 1.080 agrees with mine. The differences between the two evaluations,
      up to 2e-6, are the size of the h(P) uncertainty (G12: 2e-6 between domains).
      CONFIRMED, with the lead's limitation: two scalar conditions agree on one trial to a few 1e-6. That does not bound
      the c_l error of the exact profile. It is to be reported beside the variant spread 1.2e-4 and the numerics values.
    (c) J split by distance from P (the lead's 23:05Z item 1). From now on code/vchar.py records J at d = |X - P| =
        4, 2, 1, 0.3, 0.1, 0.03, 0.01. Each new export audit reports the increments per distance shell and their
        spread over the start angles, with the axis-adjacent start angles listed separately.

G26. c4_centre export (lead astra/construct4/c4_centre_fields.npz), flux and N_v residual by region and J by distance
shell, compared with the lead's construct4 REPORT table and the lead's jsplit (NOTES_FOR_TEAM 23:05Z), recorded 2026-10-17T23:36Z.
  Method: code/vaudit.py, Mmax 479, r_start 20, 24 start angles (runs/audit/c4_centre_v3.log/json). It uses my own
  inverse and differentiation; only the sampled rho is read. Open first quadrant, axis points and 8 end nodes excluded,
  nodal values only. psi_modes is now vectorized (same weights; matches the old loops to 4e-17 relative).
  Own c_l 5.5763301 (identity), x* 8.6008808, h(P) 0.99999706.
  Residual |R|/N, max over nodes (flux N_f = |W1 rho_x| + |W2 rho_y| + |rho|; N_v = |rho| + |X.grad rho| + |U.grad rho|):
      region         flux max (mine)   lead flux   N_v max (mine)
      r <= 0.1       1.28e-8           2.7e-9      2.77e-8
      0.1 - 2        1.12e-6           1.2e-6      2.19e-6
      2 - 10         1.23e-4           1.25e-4     3.36e-5
      10 - 100       5.16e-6           4.4e-6      3.53e-6
      100 - 1000     6.71e-7           4.8e-7      3.89e-6
      1000 - R       6.37e-7           5.8e-7      5.39e-6
      |X - P| < 0.5  6.10e-5           -           1.75e-5
      all, rms       1.15e-6           1.24e-6     8.54e-7
  In five of six bands my flux max is within a factor 1.4 of the lead's. In the r <= 0.1 band mine is 4.7 times larger,
  at r 0.013, theta 1.5675, next to the y axis; both values are below 2e-8. The worst flux point (1.23e-4) is at
  r 8.67, theta 0.245, at distance 2.1 from P. The far field under N_v is 4e-6 to 5e-6, because N_v has no c_l factor.
  J: total spread over start angles at d = 4, 2, 1, 0.3, 0.1, 0.03, 0.01:
    1.7e-6, 5.6e-5, 8.0e-5, 1.13e-4, 1.20e-4, 1.44e-4, 1.50e-4 (the lead's total is 1.52e-4).
  Shell increments, spread over all start angles (lead in brackets):
      d >= 4: 1.7e-6 [1.4e-6]
      [2,4): 5.6e-5 [4.9e-5]
      [1,2): 7.8e-5 [7.2e-5]
      [0.3,1): 4.1e-5 [3.0e-5]
      [0.1,0.3): 3.1e-5 and [0.03,0.1): 2.4e-5 [together 5.6e-5]
      [0.01,0.03): 6.4e-6
  Over the interior start angles the same shells give
    9.8e-7, 5.6e-5, 7.8e-5, 4.1e-5, 1.0e-5, 8.4e-9, 4.2e-14.
  Closer than d = 0.1, all interior characteristics share one stem. The growth of the spread from 1.13e-4 to 1.50e-4
  below d = 0.3 comes only from the two start angles next to the axes.
  R/rho just above P (y = 1e-3) is -2.95e-6; h(P) - 1 = -2.94e-6. This agrees with G24.
  B_3 IBP 0.2996 [0.2816, 0.3024], the same for both w'' routes (G22: 0.3006 [0.2823, 0.3037]).
  Verdict: the lead's construct4 flux table and jsplit are CONFIRMED, independently and within the factors above.
  Two caveats, CONFIRMED: the spread reached by d = 0.3 (1.13e-4) is 75 percent of the final 1.50e-4, so most of it builds up in 0.3 <= d < 4, the region of the 2 - 10 flux
  maximum; and the near-P residual 1.2e-4 (flux) is still the obstacle to the YES standard. The figures are nodal
  values on the fit grid. By G22 and G24 they do not establish the between-node residual.

G27. FINAL_REPORT.md (mtime 23:22Z) section 1 (definition of P_2) and notes/final_sec4_draft.md (23:22Z), audited
2026-10-17T23:43Z. Lead request NOTES_FOR_TEAM 23:23Z item 1.
  Method: diff against the lead's notes/FINAL_REPORT_backup_2322.md (the 22:11Z text audited in G23) and reading in full.
  Only section 1 (the P_m paragraph replaced by a P_2 paragraph) and the last paragraph of section 4 changed. Sections 0,
  2 and 3 are as audited in G23.
  Checks:
  - G25 (a) condition 1. P_2 is defined in full where it is first used: same equation, parities, velocity law and growth
    class; "a smooth near 0" is replaced by "rho in C^(2,alpha)_loc(R^2), rho = x^2 y a near 0 with a continuous,
    even/even, a(0) = 1". The text says that a is only continuous, that P_2 is weaker than P_inf, and that a P_2 result
    does not answer P_inf. CONFIRMED.
  - The identity 3c_l - c = 1 holds in P_2 (rederived by hand). Write the equation as div(W rho) = (1 + 2c_l) rho and
    rescale: rho_l(X) = l^-3 rho(lX) tends to x^2 y locally uniformly as l -> 0, because a is continuous with a(0) = 1.
    W(lX)/l tends to DW(0)X in C^1_loc, because W is C^2 (psi in C^(3,alpha)). In the distributional limit,
    DW(0)X.grad(x^2 y) = (3c_l - c) x^2 y = x^2 y. So the identity needs no differentiability of a. CONFIRMED.
  - "P_2 is stronger than prescribing only the cubic jet of rho at 0". This is true for the Peano jet,
    rho = x^2 y + o(|X|^3): the factorization with a continuous implies it, and rho = x^2 y + y^5 shows that the
    converse fails. A Taylor cubic jet presupposes rho in C^3, which P_2 does not require. In that reading the two
    conditions are not nested. Suggested wording: "P_2 implies rho = x^2 y + o(|X|^3) and is strictly stronger than
    this jet condition". This is a wording point, not an error. CONFIRMED with this note.
  - Membership of the trials in P_2 by construction (section 4 and the draft 4.1), checked on the construct4 formula
    (my code/gen_shape.py now reads the explicit spline_knots; c4_r1 snapshot of 23:34Z):
    - Near 0, the term m of H is B_(j+1)(q(r)) chi^(m-1) cos(2m theta) with j >= 0. With clamped knots,
      B_(j+1)(q) = O(q^(j+1)) and q = O(r^2), so the radial factor is r^(2m) times a smooth function of r^2.
      Each such term is smooth at 0, and H(0) = 0, so a(0) = e^0 = 1.
    - The singular functions are s^(p3/2) T_j(2q - 1) |cos t|^(p3 - 2) sin^2 t = |x|^(p3 - 2) y^2 times a smooth
      function, with p3 = 6.197. They are C^(4,0.19).
    - The interior knots of c4_r1 are simple (multiplicity 1; only the 8-fold end knots repeat). So the order-7
      splines are C^6 in q.
    - The growth is rho ~ r^k with k = 0.179, which is in (A3).
    So the trial is C^(4,alpha) and lies in P_2 (and in A_4). CONFIRMED.
  - Section 4 says that existence of an exact P_2 profile near the trial is the numerical claim, and that uniqueness is
    not claimed (G25 (a) conditions 2 and 4). CONFIRMED. The draft 4.4a lists h(P) - 1, R/rho at P and J as P_2
    consistency checks (condition 3). CONFIRMED.
  - Draft 4.1 no longer quotes 0.33 +- 0.06 as an error bar. It is mentioned only as superseded. CONFIRMED (G23 point
    closed).
  Verdict: FINAL_REPORT section 1 CONFIRMED, with the wording note on the cubic jet. G23's class inconsistency is closed.

G28. construct4 c4_r1 (chunk-17 shape copied 23:40Z, and the final chunk-18 shape, which is also the start shape of the
lead fit c6a) and c4_centre, evaluated between fit nodes on my own grids; decision test of analysis 13.4b; relE near
the origin; far-field closure of my inverse. Recorded 2026-10-18T00:00Z.
  Method. code/gen_shape.py (my re-implementation of the lead's trial formula) now reads explicit spline_knots
  (construct4 and later). Check: from c4_centre_shape.npz it reproduces the lead's c4_centre export rho to 5.4e-14
  relative. It generates rho on a grid uniform in log r on [7.652e-4, R] with N points and nq + 1 equispaced angles on
  [0, pi/2]. These grids share no nodes with the lead's fit grids (6144 x 480 and others) except the axes. Then
  code/vaudit.py (Mmax = 479 for nq = 384, 319 for nq = 256, 639 for nq = 512; r_start 20, 24 start angles). Driver:
  code/gen_audit.sh. Logs in runs/audit/c4r1s17_*, c4r1fin_*, c4cen_*. Lead numbers are not used anywhere in the
  computation.
  (a) Resolution and domain series, c4_r1 chunk 17 (flux N_f, max over nodes, 2 <= r <= 10 band, which contains the
      global maximum; N_v likewise; J = total spread over all start angles at d = 0.01):
      grid (N, nq, R)             c_l (identity)  h(P) - 1   flux max   N_v max    flux rms |X-P|<0.5   J spread
      6000, 256, 7.652e4          5.5763640       +6.8e-7    1.70e-5    4.89e-6    2.54e-6              1.93e-5
      9000, 384, 7.652e4          5.5763640       +6.0e-7    1.74e-5    4.90e-6    2.54e-6              1.93e-5
      13500, 512, 7.652e4         5.5763640       +5.8e-7    1.71e-5    4.90e-6    2.55e-6              1.93e-5
      11250, 384, 7.652e6         5.5763636       -1.0e-6    1.82e-5    5.12e-6    2.40e-6              1.58e-5
      7875, 384, 7.652e3          5.5763820       +7.0e-5    5.12e-5    1.85e-4    3.48e-5              3.87e-4
      The evaluation is resolution independent: a factor 2.25 in N and 2 in nq changes the band maximum by at most 3 percent
      and the J spread by less than 0.5 percent. On every grid the worst flux node is at r 8.71 to 8.80, theta 0.228 to
      0.236, at distance about 2.0 from P. CONFIRMED.
  (b) Far-field closure of my inverse. At R = 7.652e3 my one-term tail closure is not accurate enough at this level:
      c_l moves by 1.8e-5, h(P) - 1 by 7e-5, the far-field N_v rises to 1.9e-4 and the J spread to 3.9e-4. From
      R = 7.652e4 to 7.652e6, c_l moves by 4e-7 and h(P) - 1 by -1.6e-6 (the same shift, -1.7e-6, is seen on c4_centre).
      So my evaluator needs R >= 7.65e4 for work at the 1e-6 level, and its domain error in h(P) at R = 7.65e4 is about
      1.6e-6. The R = 7.652e6 values are the ones to quote. This is a property of my inverse, not of the candidate. The
      lead's trial formula is defined for all r; R here is only the outer radius of my inverse.
  (c) c4_r1 final (chunk 18; the shape coefficients differ from chunk 17 by at most 2.6e-6):
      grid (N, nq, R)             c_l (identity)  h(P) - 1   flux max   N_v max    J spread (all / interior)
      9000, 384, 7.652e4          5.5763642       +6.0e-7    1.72e-5    4.93e-6    1.92e-5 / 1.54e-5 (d=0.01)
      11250, 384, 7.652e6         5.5763638       -1.0e-6    1.80e-5    5.06e-6    1.54e-5 / 1.54e-5
      Bands at R = 7.652e6 (flux max / N_v max): r <= 0.1 1.4e-8 / 3.0e-8; 0.1-2 1.1e-7 / 2.1e-7; 2-10 1.80e-5 /
      5.06e-6; 10-100 4.8e-6 / 2.0e-6; 100-1000 4.2e-7 / 9.5e-7; 1000-R 4.1e-7 / 1.8e-6; |X - P| < 0.5 9.4e-6 /
      2.7e-6; all, rms 1.4e-7 / 2.0e-7.
      The lead's quick_scan of the same shape (NOTES_FOR_TEAM 23:49Z item 2, 12288 x 640) gives h(P) - 1 = -1.01e-6,
      2-10 flux max 1.80e-5 and N4 max 5.06e-6. My R = 7.652e6 values agree to the digits shown. CONFIRMED.
      x* 8.600842. R/rho just above P (y = 1e-3) is -1.03e-6 against h(P) - 1 = -1.02e-6 (G24).
      Identity-free c_l (scratch/cl_from_h.py on my traces, R = 7.652e6): the root of h(P) = 1 with rho fixed is
      5.5763647, which is 9.5e-7 above the identity value (dh/dc_l = 1.08 at fixed rho). On c4_centre this difference
      was 3e-6 (G22).
      D14 centre relations (code/vd14.py, five fit windows): E from -2.2e-9 to +3.2e-9 and D2 from 2e-11 to 1.0e-8,
      relative 4e-11 to 2e-8. On c4_centre they were about 1e-7 relative (G22). a0 = 1 to 10 digits.
      B_3 IBP (w'' by the mode ODE; the FD route agrees to 4 digits): 0.3013 [0.3005, 0.3024], on both domains. The
      original form gives 0.3041 [0.3021, 0.3073]. On c4_centre: 0.2997 [0.2815, 0.3025].
  (d) Decision test of analysis 13.4b, like for like (same generator, grids and evaluator for both shapes):
      shape        R          flux max 2-10   N_v max 2-10   J spread at d = 0.3 / 0.01   ratio J(0.01) / flux max
      c4_centre    7.652e4    1.224e-4        3.34e-5        1.13e-4 / 1.50e-4           1.23
      c4_r1 fin    7.652e4    1.720e-5        4.93e-6        1.41e-5 / 1.92e-5           1.12
      c4_centre    7.652e6    1.225e-4        3.34e-5        1.15e-4 / 1.58e-4           1.29
      c4_r1 fin    7.652e6    1.798e-5        5.06e-6        1.54e-5 / 1.54e-5           0.86
      The c4_centre figures on my grids equal those on the lead's export nodes (G26: 1.23e-4, 3.36e-5, 1.50e-4). From
      c4_centre to c4_r1 the near-P residual fell by a factor 6.6 to 7.1 and the J spread by a factor 7.8 to 10.3. The J spread did
      not stay near 1.5e-4. It falls together with the near-P residual, and their ratio stays of order 1. Shell
      increments (c4_r1 fin, R = 7.652e6, spread over all start angles): d >= 4: 8.2e-7; [2,4): 5.5e-6; [1,2): 1.0e-5;
      [0.3,1): 6.7e-6; [0.1,0.3): 6.1e-6; [0.03,0.1): 2.8e-6; [0.01,0.03): 3.9e-7. The spread is still built up in
      0.3 <= d < 4, the region of the flux maximum. Below d = 0.1 the interior characteristics again share one stem
      (interior increments 1.7e-9 and 2e-17).
      Reading: this is what one expects if the J spread is caused by the residual of the trial, which is a
      representation and solver limit. It is not what one expects from a defect that persists for every trial near
      the branch. CONFIRMED as a numerical observation. It is a consistency check (G25 (c)), not a proof of existence.
  (e) relE (my Poisson check) near the origin. On every candidate my relE is about 1e-4 in [r0, 0.01] and below 1e-7
      beyond. Test (scratch/test_relE_small_r.py): the manufactured field rho = x^2 y (1 + r^2/50)^((k-3)/2)
      (1 + 0.3 x^2/(1 + r^2)), k = 0.18, has E = 0 exactly. On my evaluator it gives relE
      5.5e-3 to 8.7e-3 on [r0, 1e-3], 6.9e-4 to 1.0e-3 on [1e-3, 3e-3], 6.0e-5 to 9.7e-5 on [3e-3, 1e-2], and
      2e-10 to 9e-9 beyond (N = 6000 and 9000, 64 and 256 angles). The small-r values grow with N (by a factor 1.5 from
      6000 to 9000), which is the behaviour of rounding error amplified by re-differentiation, not of truncation error.
      So relE on [r0, 0.01] measures my evaluator, not the candidate, and it must not be quoted as a defect of the
      candidate. An attempt to subtract the harmonic part analytically made the band [0.01, 1] worse; it was reverted
      (scratch/vresid_pre_Esub.py). CONFIRMED (evaluator limitation).
  (f) FINAL_REPORT.md (mtime 23:48:45Z) against my G27 text (lead backup notes/FINAL_REPORT_backup_2348.md): the only
      change is the cubic-jet sentence of section 1. "P_2 implies rho = x^2 y + o(|X|^3) and is strictly stronger than
      this jet condition (rho = x^2 y + y^5 satisfies the jet condition but is not of the form x^2 y a)." Check:
      x^2 y (a - 1) = o(|X|^3) because a is continuous with a(0) = 1. y^5 = o(|X|^3), it has the parities, and
      y^5/(x^2 y) = y^4/x^2 is unbounded near the y axis, so no continuous a exists. CONFIRMED.
  Verdict: c4_r1 is a CONFIRMED improvement over c4_centre by a factor of about 7 in the near-P residual, measured
  between fit nodes, at three resolutions and on two domains of my inverse. The J-spread decision test is answered: J
  falls with the residual. Not YES-level: the near-P residual is 1.8e-5 (flux) and 5.1e-6 (N_v), against the standard of
  about 1e-6 (G20 b1). The domain series of the fit itself (construct5 dom100, dom300, dom900) is still missing. OPEN.

G29. Bounded-domain fits (construct5) need the lead's exterior closure in my generator; first application to dom100
chunk 13; SPEC N3(a) "Equivalently" (numerics NOTES_FOR_LEAD 00:03Z item 3). Recorded 2026-10-18T00:10Z.
  (a) construct5 fits the equation only for r <= R_fit (shape units 100, 300, 900; physical R_fit L = 765, 2296, 6887).
      Its inverse uses, for r > Rc = R_shape L with R_shape = R_fit/0.9, the two-term extension
        rho = (rho_c - S)(r/Rc)^k + S (r/Rc)^(2k-1),  S = (r rho_r|_c - k rho_c)/(k - 1)
      (construct5 REPORT and tail_control.py; this matches rho and r rho_r at Rc, so it is C^1). The trial formula itself
      is not fitted beyond R_fit. Evaluated as a formula on all of R^2, the dom100 chunk-13 shape has flux residual
      8.2e-4 and N_v 2.0e-3 for r > 1000, and this moves my identity c_l to 5.5763513 and h(P) - 1 to +3.8e-5
      (runs/audit/d100c13_*). So a bounded-domain fit is only meaningful with its closure. I added the closure to
      code/gen_shape.py (7th argument 'closure'; re-implemented from the definition above, r rho_r at Rc by a 5-point
      stencil in log r). Check on dom100: rho is continuous at Rc to 6e-14 relative, and the log-derivative just outside
      is 0.17984266 for both the closure and the formula. code/vaudit.py adds the regions r <= R_fit and r > R_fit when
      VAUDIT_RFIT is set; code/gen_audit.sh takes R_fit (physical) as a 4th argument.
      Control: c4_r1 final with its own closure (Rc = 7652, R_fit 6887) gives the same interior numbers as the
      formula-global field to 3 digits or better (c_l 5.5763638, h(P) - 1 = -1.0e-6, flux max 1.797e-5, J spread
      1.538e-5). Beyond R_fit its closure field has N_v up to 9.4e-4 next to the y axis, while the formula itself has
      1.8e-6 there. For c4_r1 the formula is the better global field. CONFIRMED.
  (b) dom100 chunk 13 (copy runs/gen4/dom100_c13_shape.npz of the lead file of 23:49:59Z, preliminary: the fit is still
      running), with closure, N 9000 / 11250, nq 384:
      R (my inverse)  c_l (identity)  h(P) - 1   flux max r<=R_fit   N_v max r<=R_fit   flux max |X-P|<0.5   J spread d=0.01
      7.652e4         5.5763416       +1.1e-6    1.97e-5             5.66e-6            1.43e-5              3.40e-5
      7.652e6         5.5763412       -5.1e-7    1.88e-5             5.39e-6            1.50e-5              4.26e-5
      The lead's stored values for this shape are c_l 5.57634118, h(P) - 1 = +2e-9 (dom100_status.json). My c_l agrees
      to 1e-8, and my h(P) agrees to within the domain error of my inverse (G28 (b)). Inside R_fit the residual is at the
      level of c4_r1, but the J spread is 2.8 times larger (4.3e-5 against 1.5e-5). Outside R_fit the closure field is not a solution
      (flux 1.7e-3, N_v 2.4e-2 at r about 1900 next to the y axis). This is expected and is not a defect of a
      bounded-domain fit, but it means construct5 fields are not candidates on R^2 as they stand. c_l differs from c4_r1
      (fit radius 900) by -2.26e-5. B_3 IBP 0.2975 [0.2843, 0.2994].
      Verdict: method CONFIRMED; numbers preliminary. The domain series is to be tabulated when dom100, dom300 and dom900
      are final.
  (c) SPEC N3(a): "Equivalently, f_n(R) R^(2-2n)/(2n-k-1), with f_n(R) the mode of d_x rho at r = R." For the
      homogeneous extension, d_x rho = (r/R)^k r^(-1) [k cos t Theta_R - sin t Theta_R'] for r > R, so
      int_R^inf s^(1-2n) f_n ds = F_n R^(1-2n)/(2n-k-1) = f_n(R+) R^(2-2n)/(2n-k-1) with f_n(R+) the EXTERIOR limit.
      The interior value f_n(R-) uses r rho_r(R-) in place of k rho(R). The two agree only if the data are homogeneous at R.
      The sentence is correct only if f_n(R) means the exterior limit, and it is wrong for the interior derivative. This
      CONFIRMS the numerics lane's point. Fix: say "the mode of d_x of the extension at r = R+", or delete the sentence.
      My inverse is not affected. Its tail is A_m r^k fitted to the last 8 values of each rho mode, and d_x is
      integrated by parts (psi_n is built from the rho modes n +- 1), so no radial derivative at R enters. Its closure
      error is the value mismatch at R, which G28 (b) measures directly.
  (d) (Hmin) on c4_r1 final (new code/vzeros.py, my inverse, formula-global field, N 11250, nq 384, R 7.652e6, grid
      evidence only, recorded 2026-10-18T00:14Z). The only sign change of W_1(x, 0) is at x = 8.6008417 (x* 8.6008420 by my
      root finder). W_2(0, y)/y >= 5.57657 on the whole y axis, with no sign change; the minimum is at the outer end,
      where U is negligible and the ratio tends to c_l. In the open quadrant no grid cell has a sign change of both W_1
      and W_2. min |W|/(c_l |X|) over |X - P| >= delta is 2.16e-2, 6.5e-3 and 2.5e-3 for delta = 1, 0.3 and 0.1. This is
      linear in delta, as expected for the single source P (mu_2 = 1). On the grid the zeros of W in the closed
      quadrant are 0 and P only. CONFIRMED as grid evidence, not a proof.

  (e) Added 2026-10-18T00:15Z. construct5 REPORT (00:12Z) rejects dom100: the closure error in c, recomputed after refitting, is
      -3.02724420272e-5. Independent value: my c with the closure field minus my c with the formula on all of R^2, at
      R = 7.652e6, is -3.02724e-5 (-3.02843e-5 at R = 7.652e4). This agrees with the lead to 6 digits. The final domain
      series is R_fit = 200, 300, 900. CONFIRMED.

G30. Lead notes/analysis.md section 11 (far-field closure error of a disk model, 21:24Z, marked "not audited"), and
the domain error of my own inverse. Recorded 2026-10-18T00:14Z.
  (a) 11.1, rederived by hand. Assume rho_1 = theta_0 r^k + theta_1 r^(2k-1) + O(r^(3k-2)) (the sin 3t coefficient).
      The homogeneous extension beyond R is (r/R)^k rho_1(R) = theta_0 r^k + theta_1 R^(k-1) r^k + ..., so true minus
      model is theta_1 (r^(2k-1) - R^(k-1) r^k). Against r^(-2) on (R, inf) this gives
      theta_1 [R^(2k-2)/(2-2k) - R^(2k-2)/(1-k)] = -theta_1 R^(2k-2)/(2-2k), as stated. With a two-term exterior the
      first neglected term is r^(3k-2), and the error is O(R^(3k-3)). CONFIRMED, conditional on the expansion, as marked.
  (b) 11.2 arithmetic: 1.338e-3/3.058e-5 = 43.75 and 3.058e-5/1.262e-6 = 24.23, against 10^1.641 = 43.75 and
      7^1.641 = 24.37. CONFIRMED.
  (c) Independent check with my inverse. Its tail is one term (A_m r^k fitted to the last 8 values of each rho mode), so 11.1
      predicts an error ratio 10^(2-2k) = 43.79 per decade of R (k = 0.179328). On the c4_r1 chunk-17 shape, with
      R = 7.652e6 as reference: c(7.652e3) - c(ref) = 5.544e-5 and c(7.652e4) - c(ref) = 1.265e-6, ratio 43.84;
      h(P) differences 7.104e-5 and 1.623e-6, ratio 43.77. c4_centre gives the same 1.265e-6 at R = 7.652e4. So my
      domain error follows R^(2k-2), and at R = 7.652e6 it is smaller than at 7.652e4 by about 43.8^2 = 1.9e3: c to
      about 7e-10, c_l to 2e-10, h(P) to 9e-10. My R = 7.652e6 values of c_l and h(P) are converged in domain to
      about 1e-9, well below the 1e-6 level that matters. This sharpens G28 (b). CONFIRMED.

G31. c_l along the construct4 c4_r1 fit, and the reading of lead analysis 13.4a (c_l insensitive to the near-P defect).
Recorded 2026-10-18T00:16Z.
  Data: the lead's chunk records astra/construct4/c4_r1_chunk1..18.json (last history entry: fit norm, stored c_l, h(P),
  x*), and my own c_l at R = 7.652e6 for the start and end shapes (G28).
      chunk   fit norm    c_l (stored)   x*
      1       9.23e-5     5.57632966     8.6008802
      6       7.90e-5     5.57633406     8.6008761
      12      6.30e-5     5.57634078     8.6008686
      13      3.66e-5     5.57635941     8.6008479
      16      3.36e-5     5.57636211     8.6008445
      17      3.25e-5     5.57636355     8.6008425
      18      3.19e-5     5.57636375     8.6008420
  My values: c4_centre 5.5763297 and c4_r1 final 5.5763638 (identity, R = 7.652e6), so the move is +3.41e-5. The lead's
  stored values agree with mine at both ends to within the 1e-7 rounding of my quoted values.
  (a) c_l increases monotonically over all 18 chunks. The objective decreases over every chunk except chunk 5, where it
      rises by 3e-8. The last two chunks moved c_l by +1.4e-6 and +2.0e-7, so c_l has not settled at the 1e-6 level and
      the fit has not converged.
  (b) 13.4a (notes/analysis.md, lead 22:06Z) takes construct1 under radial refinement 120/160/200: c_l moved by
      -3.9e-5 while its J spread fell by 4.8e-4. Its "ratio of about 0.015" is the relative change of c_l (7e-6)
      divided by the absolute change of J. In absolute units the construct1 ratio is 3.9e-5/4.8e-4 = 0.081. On c4,
      from c4_centre to c4_r1 (like for like, G28 (d), R = 7.652e6), the J spread fell by 1.43e-4 and c_l rose by
      3.41e-5. That is 0.24 absolute or 0.043 in the 13.4a units, about 3 times the construct1 ratio, and with the
      opposite sign. 13.4a concluded that "the remaining near-P defect, scaled by the ratio above, suggests an effect
      of order 1e-5 on c_l". At the time of 13.4a the best J spread was about 1.4e-4, so that estimate is about
      1.1e-5 (absolute ratio) or 6e-6 (13.4a units). Reducing that defect by a factor 10 has since moved c_l by
      3.4e-5. The 13.4a estimate was therefore too small by a factor of about 3 to 6, and the sign of the response
      depends on the family. The ratio is a heuristic, not a bound: REFUTED as a bound, and accurate in order of
      magnitude only to within a factor of a few. Extrapolating the c4 ratio linearly to J = 0 from the present
      spread of 1.5e-5 gives a further move of a few 1e-6. This is a guess, not an estimate, since the ratio is
      not constant.
  (c) construct5 uses the same basis as c4_r1: 21722 coefficients, radial degree 215, 100 angular functions and
      6 singular functions (checked in the shape files). It differs in its starting point (c4_radialtest), its fit
      domain r <= R_fit and the two-term closure. c4_r1 itself is formula-global (R_shape = 1000, no R_fit). The
      construct5 fits, as stored at 00:18Z, are dom200 (fit norm 8.91e-5, c_l 5.5763298), dom300 (8.32e-5, 5.5763321)
      and dom900 (chunk 4, 8.52e-5, 5.5763315). c4_r1 at a similar norm (chunks 2 to 5, 9.0e-5 to 8.2e-5) has c_l
      5.5763302 to 5.5763337. The construct5 objectives are restricted to r <= R_fit, so the norms are not strictly
      comparable. Read with that caveat, c_l at a given stage of the fit varies by about 2e-6 across fit domains, while
      it drifts by 3.4e-5 along the c4_r1 fit. The leading uncertainty in c_l is therefore fit convergence, not the fit
      domain. The construct5 runs were still in progress at 00:18Z (dom900 chunk 5 running).
  (d) c_l against the lead's fit norm along c4_r1: the slope dc_l/dnorm is -0.38 over chunks 1 to 12, -0.70 over the step
      12 to 13 (where the norm fell from 6.3e-5 to 3.7e-5), and -0.93 over chunks 13 to 18. It does not decrease as the fit
      improves. A straight line through chunks 13 to 18 meets norm 0 at c_l = 5.57640. That extrapolation has no
      justification (the norm of a fixed basis does not go to 0), and it is quoted only to show the size of what is
      unresolved: a further move of order 3e-5 is consistent with these data. The numerics lane's new least-squares solver
      (NOTES_FOR_LEAD 00:03Z item 2) also finds c_l to be a soft direction of its discrete system. That is consistent with
      this item, though at its own much lower accuracy (a few 1e-2).
  Consequence for reporting (G20 (c), amended): the variant spread is now 5.57624 to 5.57637, and the best fit lies at its
  upper end and is still moving. A report may quote c_l = 5.5763 with this spread. It must say that the best fit's c_l
  rose by 3.4e-5 while its near-P residual fell by a factor 7, and that c_l was still changing at the end of that fit.
  Six or more significant digits of c_l are not supported by the present evidence. CONFIRMED (numerical observation).

G32. FINAL_REPORT.md (mtime 00:08Z; diff against notes/FINAL_REPORT_backup_2348.md) and notes/final_sec4_draft.md
(23:22Z) 4.3, audited 2026-10-18T00:20Z.
  Method: diff of the two FINAL_REPORT versions; each new provenance line checked against the G entry it cites.
  (a) The new verifier lines 22:21 (G19), 22:28 (G20 (b4)), 22:30 (G21), 22:34 (G23), 22:42 (G22), 22:51 (G24),
      23:16 (G25 (a)), 23:36 (G26), 23:43 (G27) and 00:00 (G28) state what those entries say. CONFIRMED.
      One omission, not an error: the 22:30 line ("rho C^1 near the source P and W C^2 there") leaves out the hypothesis
      A = d_x W_1(P) > 1 that G21 uses. Since div W = 2 c_l, A = 2 c_l - h(P), so A > 1 holds whenever h(P) < 2 c_l - 1
      (10.15 here). Adding "(A = d_x W_1(P) > 1)" would make the line complete.
  (b) Section 1 jet sentence: "P_2 implies rho = x^2 y + o(|X|^3)" holds, since rho - x^2 y = x^2 y (a - 1) and
      a is continuous with a(0) = 1. The example rho = x^2 y + y^5 is even in x and odd in y, has the cubic jet x^2 y, and
      does not vanish on x = 0 for y != 0, so it is not of the form x^2 y a. CONFIRMED.
  (c) final_sec4_draft 4.3 (bracketed reading, still TBD) says "the near-P defect affects c_l at an estimated order
      1e-5". G31 (b) refutes this as a bound. Reducing the near-P residual by a factor 7 (c4_centre to c4_r1) moved c_l by
      +3.4e-5, and c_l was still moving at the end of that fit. Required change when 4.3 is filled in: quote c_l = 5.5763
      with the variant spread 5.57624 to 5.57637. State that the best trial's c_l rose by 3.4e-5 under the c4_r1 local
      refinement and had not settled, and that the 13.4a sensitivity ratio is not a bound. The draft's "three
      constructions" now has to include construct4 (5.5763297 to 5.5763638) and construct5.
  Verdict: FINAL_REPORT 00:08Z CONFIRMED as far as it goes (sections 0 to 3 and provenance). 4.3 needs the G31 change.

G33. construct5 domain series (fit radii 200, 300, 900 shape units), final shapes, audited between fit nodes, 2026-10-18T00:45Z.
  Provenance: construct5 ended by timeout at 00:30Z (exit file 124). There are no dom*_fields exports and no stagnation
  record (operational_stagnation false in all three status files). The last saved shapes were copied at 00:31Z to
  runs/gen4/c5_dom{200,300,900}_final_shape.npz. Each shape's stored history agrees with its status file:
      dom200 after 2 chunks, fit norm 8.65e-5;  dom300 after 6 chunks, 8.21e-5;  dom900 after 5 chunks, 8.39e-5
  (c4_r1: 3.19e-5). Same basis as c4_r1 (G31 (c)); R_fit L = 1530.4, 2295.6, 6886.8.
  Method: code/gen_shape.py with the two-term closure beyond R_shape L (G29); code/vaudit.py on two inverse domains,
  R = 7.652e4 (N 9000) and R = 7.652e6 (N 11250), 385 angles per quadrant, Mmax 479, with regions r <= R_fit L and
  r > R_fit L; code/extra_checks.sh (identity-free c_l, D14, Hmin) at R = 7.652e6. Values at R = 7.652e6 unless noted.

      quantity                         dom200        dom300        dom900        c4_r1 (G28, formula-global)
      c_l (identity, mine)             5.5763311     5.5763326     5.5763321     5.5763638
      c_l stored by the lead           5.5763311     5.5763326     5.5763321     5.5763638
      h(P) - 1                         -6.4e-7       -5.9e-7       -9.1e-7       -1.0e-6
      c_l(h(P) = 1) - c_l(identity)    +5.9e-7       +5.5e-7       +8.5e-7       +9.5e-7
      flux max 2 <= r <= 10            2.03e-5       1.82e-5       1.82e-5       1.80e-5
      flux max |X - P| < 0.5           1.77e-5       1.68e-5       1.72e-5
      N_v max 2 <= r <= 10             5.84e-6       5.22e-6       5.25e-6       5.06e-6
      flux max 10 <= r <= R_fit L      3.40e-6       3.11e-6       3.20e-6
      N_v max 10 <= r <= R_fit L       2.44e-6       2.52e-6       2.33e-6
      flux max r > R_fit L             5.81e-4       3.10e-4       5.28e-5
      N_v max r > R_fit L              9.09e-3       5.08e-3       9.38e-4
      J spread, shell d = 0.01         5.69e-5       4.95e-5       5.12e-5       1.54e-5
      J spread, d = 0.01 (R = 7.652e4) 4.87e-5       4.09e-5       4.26e-5       1.92e-5
      B_3 IBP (w''_ode), median        0.2957        0.2965        0.2965        0.3013
        [setting range]                [0.2776, 0.2984] [0.2811, 0.2988] [0.2811, 0.2988] [0.3005, 0.3024]
      D14 centre relations, max rel    8.9e-7        7.5e-7        7.3e-7        2e-8
      Hmin: W_1(x,0) zeros             8.6008804     8.6008782     8.6008783     8.6008417
            min W_2(0,y)/y; open cells 5.57653; 0    5.57654; 0    5.57654; 0    5.5766; 0
  At R = 7.652e4, c_l differs from the R = 7.652e6 value by at most 5e-7 and the near-P maxima (2 <= r <= 10) by at most
  5 percent. In 10 <= r <= 1000 the R = 7.652e4 maxima are up to 2 times larger (N_v 3.9e-6 against 1.9e-6 in
  100 <= r <= 1000), and h(P) - 1 is +7e-7 to +1.0e-6. Both come from my inverse's domain error (G28 (b), G30).
  (a) Domain independence inside the fit region, at the stage these fits reached: c_l spread 1.5e-6 over R_fit = 200 to
      900; h(P) - 1 within 1e-6 of 0 on all three; near-P flux 1.8e-5 to 2.0e-5, N_v 5.2e-6 to 5.8e-6; J 4.9e-5 to
      5.7e-5; B_3 0.2957 to 0.2965; Hmin holds on the grid. The lead's stored c_l agrees with mine to 1e-7 on each.
      CONFIRMED as a three-domain series in the sense of G20 (b1). It does not meet the residual standard of G20 (b1):
      the near-P residual is 1.8e-5 (flux) and 5.2e-6 (N_v), against about 1e-6.
  (b) The closure exterior r > R_fit L is not a solution. Its flux maximum falls with R_fit by 1.88 (200 to 300),
      5.87 (300 to 900) and 11.0 (200 to 900), against (R ratio)^(2 - 2k) = 1.95, 6.07 and 11.8. N_v falls by
      1.79, 5.42 and 9.69. The maxima sit next to the y axis (theta 1.5675) at r = 3884, 5813 and 1.77e4. The domain
      error this induces in c_l is below the 1.5e-6 spread of (a).
  (c) Comparison with c4_r1: the near-P residual maxima are the same to 10 percent (flux 1.82e-5 against 1.80e-5, N_v
      5.2e-6 against 5.1e-6). Yet c_l is lower by 3.1e-5 to 3.3e-5, the J spread is larger by a factor 3.2 to 3.7,
      B_3 is lower by 0.005, and D14 is 35 to 45 times larger. So the near-P residual maximum (the G20 (b1) metric) does not
      determine c_l at the 1e-5 level. Fits with the same near-P maximum differ in c_l by 3e-5. Of the measures
      tabulated, the J spread and the fit stage separate them; the near-P maximum does not. This supports G31: c_l is
      unresolved at about 3e-5, and the quoted spread must include both 5.57633 (construct5) and 5.57636 (c4_r1).
  (d) B_3: with construct5 the trial values are 0.2957 to 0.3013 (median IBP), still about 0.30 natural units.
  Verdict: (a) CONFIRMED (domain independence at 1.5e-6 in c_l for this fit stage); standard not met; (c) CONFIRMED as
  an observation. The domain series does not include the best trial (c4_r1 is formula-global, one domain).

G34. Lead request 00:44Z: FINAL_REPORT.md (mtime 00:43Z) against notes/FINAL_REPORT_backup_0018.md (the version of G32),
notes/final_sec4_draft.md (00:43Z) against notes/final_sec4_draft_backup_0043.md, lead analysis 13.8, and the A used in my
identity-free c_l. Recorded 2026-10-18T00:51Z.
  (a) Section 1. Both problems now require rho in C^{2,alpha}_loc(R^2), the velocity law and (A3); P_inf adds "a is
      C^infinity near 0", P_2 adds "rho = x^2 y a near 0 with a continuous, even/even, a(0) = 1". The problem statement at
      the top of section 1 already contains the factorization, so with the common regularity P_inf is a subset of P_2.
      The global C^{2,alpha} requirement is labelled as the report's choice (the prompt fixes the regularity of a near 0
      only). The y^5 sentence now compares local conditions only. (A1) reads C^{m,alpha}_loc(R^2). CONFIRMED.
  (b) Timeline line 22:30 and my G21. Counterexample checked: W = (2 xi, eta/3), rho = eta^3 gives
      W.grad rho = (eta/3)(3 eta^2) = rho; P is a source with A = 2 > 1 and h = 1/3, and rho is smooth. So the Claim line
      of G21, read as a local lemma, is false. My G21 check used, in the case h < 1, the global facts g ~ x^2 at 0 and
      w != 0 on (0, x*); the cases h > 1 and h = 1 with C = 0 need the same facts (C = 0 gives rho = 0 near P, so g = 0 near
      x*, which the axis ODE w g' = (1 - h) g propagates to (0, x*)). With g = rho_y(x,0) > 0 on (0, x*) as a hypothesis the
      conclusion h(P) = 1, rho = C eta, C > 0 holds in all three cases. In P_2 this hypothesis holds: g solves a linear
      first-order ODE with nonvanishing coefficient w on (0, x*), so g is never zero there or identically zero, and
      g ~ x^2 > 0 near 0. The lead's 13.8 (b) proof (f_xi(e^{At} xi, e^{ht} eta) = e^{(1-A)t} f_xi(xi, eta), bounded as
      t -> -inf, so f_xi = 0) is correct and shorter than mine. The averaging step of 13.8 (a): with the 1-periodic
      integrand e^{uB} K(Phi_{-u} z), H(Phi_{-s} z) = e^{-sB} H(z) and DH(0) = I if DK(0) = I. Checked. Hartman's C^1
      linearization of a C^2 planar contraction is the right citation (no resonance condition). The new 22:30 line
      states A > 1 and the hypothesis rho_y(x,0) > 0 on (0, x*) with its P_2 justification. CONFIRMED. G21 amended in place.
  (c) Section 4 current assessment and draft (ii), (iii), 4.1, 4.2, 4.4a, 4.4b, 4.7.
      - Trial regularity, checked on the shape files and on my generator (code/gen_shape.py, which reproduces the lead
        trial to 5.4e-14): c4_r1 final, c4_centre and construct5 dom900 have spline order 7 (polynomial degree 7), end
        knot multiplicity 8 and all 208 interior knots simple, so each radial profile is C^{6,1} in q, and q is analytic
        in r^2. origin_radius 0.02 > 0; the first B-spline is omitted, so b_m(q) = q times a polynomial on the first knot
        interval, and b_m chi^(m-1) cos(2 m theta) = [b_m/r^2] Re(z^(2m)) / (L^(2m-2) (rr^2 + r_or^2)^(m-1)) is analytic at
        0 for m >= 2 (m = 0, 1 directly). The fractional term: s^(p3/2) |cos t|^(p3-2) sin^2 t = |x|^(p3-2) y^2 (L^2 + r^2)^(-p3/2),
        as stated, and |x|^(4 + beta) is C^{4,beta} with beta = p3 - 6 = 0.197. So H, a = e^H and rho = x^2 y e^H are in
        C^{4,beta}_loc(R^2) (rho is better near x = 0, but the claim is only C^{4,alpha}). a(0) = e^{H(0)} = 1 exactly.
        Parities hold term by term. Growth: rho ~ r^k with k = 1/c_l < 1. T(-1), the coefficient of the fractional term at
        the origin, is 1.648523 on c4_r1 final (1.648384 on c4_centre and dom300), as the lead states. CONFIRMED for these
        formula-global shapes. Caveat: a closure-extended field (construct5, or any shape used with the two-term exterior
        of G29) is only C^1 across r = R_shape L (it matches rho and r rho_r only). Such a field is not in C^{2,alpha}_loc,
        so it is not an admissible trial density as it stands. It may be quoted only as a bounded-domain fit. Any later
        shape (c6a, c6b, c6c, c7) must be re-checked for simple knots.
      - "admissible trial density, not a member of P_2": correct (nonzero residual). CONFIRMED.
      - (ii) is conditional ("if the exact profile ... has a well-defined nonzero B_3"), says the estimator value is
        evidence and not proof, and is not a NO. It meets G20 (a). CONFIRMED.
      - 4.4a: R5 gives h(P) = 1 for every A_2 profile; R/rho near the axis is (w g' + (h - 1) g)/g + O(y^2), so it extends
        continuously to the axis segment near P with value h(P) - 1 at P (w(x*) = 0, g(x*) > 0). CONFIRMED.
      - 4.4b: along a characteristic, d/dt log rho = 1 + R/rho and d/dt log rho_tr = 1, so J_eps = log rho(X0) - log
        rho_tr,eps(X0) with rho_tr,eps = rho on the cutoff section, and e^J - 1 is the relative difference. CONFIRMED.
        Wording note: "A nonzero h(P) - 1 adds (h(P) - 1) log(1/eps)/h(P) to every label" holds per label as eps -> 0, up
        to an eps-independent constant, for labels whose backward orbit enters P along the slow direction. Labels close to
        the x axis approach P along the fast direction first (rate A = 10.15 against h = 1) and reach this regime only at
        smaller eps; that is where my G24/G25 shells showed the h(P) - 1 growth. Suggested: "adds (h(P) - 1) log(1/eps)/h(P)
        + O(1) to each label off the x axis as eps -> 0".
      - (iii), 4.1, 4.2, 4.7 wording ("no additional zero detected on the stated grid and domain (a sampled check, not a
        validated exclusion)"; "sampled numerical diagnostics, not certified suprema"; 2D expansion withdrawn). CONFIRMED.
  (d) 13.7 and 13.8 (c). My identity-free c_l (scratch/cl_from_h.py) keeps Psi_1 = psi_y(x,0) fixed and computes, for
      each trial c, x*(c) from c x = Psi_1(x) and h(P; c) = c + Psi_1'(x*(c)), which is 2c - w'(x*), i.e. A = 2c - h(P).
      It does not use A = 2c_l - 1. The derivative: dx*/dc = -x*/A and dh/dc = 1 - Psi_1''(x*) x*/A = 1 - h_x(P) x*/A,
      as in 13.8 (c) (h_x = Psi_1'' on the axis). My measured dh/dc_l = 1.08 (G28 (c)) means h_x(P) x*/A = -0.08.
      CONFIRMED.
  Verdict: the 00:43Z FINAL_REPORT and the section 4 draft are CONFIRMED, with one wording note (4.4b) and one caveat
  (closure-extended fields are C^1 only at R_shape L). G21 is amended (hypothesis rho_y(x,0) > 0 on (0, x*)).

### G35. c6a (215 radial functions) between nodes: mid-segment it2250 and segment 1 final; slow curve at P; SPEC v4.4. Recorded 2026-10-18T01:02Z
  Shapes: lead/work/c6 c6a it2250 export (copied 00:53Z as runs/gen4/c6a_it2250_shape.npz) and c6a_seg1_shape.npz
  (mtime 00:56Z, copied 00:58Z). c6a ended after segment 1 (lead decision, c6a_driver.log 00:57:34Z). Both shapes: degree
  215, spline order 7, 224 knots with end multiplicity 8 and all interior knots simple (C^{6,1} in q, as G34 (c)
  requires), angular 100, singular 6, origin radius 0.02, compact 'matched', 2 tail terms. The c6b (244) and c6c (302)
  start shapes also have simple interior knots (253 and 311 knots).
  Method: code/gen_shape.py + code/vaudit.py (own generator, own differentiation, own full-plane inverse), r0 7.652e-4,
  nq 384, Mmax 479; R 7.652e6 (N 11250) quoted, R 7.652e4 (N 9000) as the inverse-domain check. extra_checks.sh on
  seg1 (R 7.652e6). Columns: flux max on 2 <= r <= 10, flux max on 10 <= r <= 100, N_v max on 2 <= r <= 10, J spread
  (labels at d = 0.01), B_3 (IBP estimator, range).

    shape            c_l        hP-1      flux 2-10  flux 10-100  N_v 2-10  J spread  B_3 [range]
    c4_r1 final      5.5763638  -1.0e-06  1.798e-05  4.772e-06    5.058e-06 1.539e-05 0.3013 [0.3005, 0.3024]
    c6a it2250       5.5763603  -1.8e-07  1.813e-05  3.132e-06    5.162e-06 1.708e-05 0.3006 [0.2990, 0.3013]
    c6a seg1         5.5763607  -1.9e-07  1.861e-05  2.891e-06    5.236e-06 1.733e-05 0.3006 [0.2991, 0.3012]
    c6a seg1 R7.6e4  5.5763611  +1.4e-06  1.859e-05  2.842e-06    5.359e-06 1.658e-05 0.3006 [0.2991, 0.3012]

  Lead scansum on its own evaluator (c6a_seg1_scan.json, nr 12288, nt 640): c_l 5.57636071, hP-1 -1.69e-07, 2-10 flux
  1.85e-05, N4 5.22e-06, 10-100 2.89e-06; it2250: 1.81e-05, 5.15e-06, 3.20e-06. My values agree to 1 to 2 percent.
  seg1 extra checks: identity-free c_l (h(P) = 1 with Psi_1 fixed) 5.576360883, diff +1.72e-07 from the identity value,
  dh/dc_l 1.0785; D14 centre relations: a0 = 1, 8 p4/r^4 = beta - alpha to 4e-9 relative at r = 2e-3, E -9.0e-09 and
  D2 +9.5e-09 (relative -3.9e-08, +1.9e-08) on [1e-3, 0.02]; one zero of W_1 on the positive x axis (8.6008410, x* from
  the identity 8.6008413), no zero of W_2 on the y axis, no open-quadrant cell with both components changing sign,
  min |W|/(c_l |X|) 0.0025 at |X - P| < 0.1 (sampled, not a validated exclusion).
  Findings:
  (a) Continued fitting at 215 radial functions lowers the residual away from P (10-100 band 4.8e-6 -> 2.9e-6, fit
      norm 2.60e-5 -> 2.49e-5) but not near P: the 2-10 flux maximum rose 1.80e-5 -> 1.86e-5 and N_v 5.06e-6 -> 5.24e-6.
      The J spread rose 1.54e-5 -> 1.73e-5. This confirms the lead's 00:41Z reading (item 3) at the segment end. The
      near-P maximum is at a plateau for this basis; whether more radial functions (c6b 244, c6c 302) lower it is the
      open question.
  (b) c_l moved -3.1e-6 over c6a (5.5763638 -> 5.5763607), after rising 3.4e-5 along c4_r1 (G31). The c4_r1 and c6a
      values with near-P maximum 1.8e-5 to 1.9e-5 span 5.5763603 to 5.5763638; the construct5 domain fits (G33) span
      5.5763311 to 5.5763326. c_l is still determined only to about 3e-5. Quote c_l = 5.57634 +- 3e-5 at most, as
      numerical evidence.
  (c) Slow invariant curve at P (analysis 13.5a, code/vslow.py on c4_r1 final, R 7.652e6 field): a2 0.0892492,
      A 10.152684, kappa = a2/(2h - A) = -0.0109474 (-0.0109472 with h = 1). The lead quotes -0.011. CONFIRMED. (h in
      this run is 1 + 5.5e-5 from vcand's own differencing; kappa is insensitive to it at 1.5e-7.)
  (d) SPEC v4.4 (00:35Z), diff against notes/SPEC_backup_v4.3.md: the only change is the N3(a) tail formula. The
      'equivalent' form now uses the exterior derivative of the homogeneous extension: R d_x rho_ext = k cos(theta)
      Theta_R - sin(theta) Theta_R' at r = R. It is not the interior d_x rho(R-), because R rho_r(R-) differs from
      k rho(R) unless rho is exactly homogeneous of degree k at R. Rederived from d_x = cos(theta) d_r - sin(theta) r^-1
      d_theta and rho_ext = (r/R)^k Theta_R(theta). CONFIRMED. No criterion changed.
  Verdict: CONFIRMED (lead's c6a values and reading; kappa; SPEC v4.4). Overall status unchanged: near-P residual 1.86e-5
  flux and 5.2e-6 N_v against the 1e-6 standard (G20 b1); the team may NOT finish.

### G36. Structure of the near-P residual on c6a segment 1 (where it sits, at what scale). Recorded 2026-10-18T01:10Z
  Method: code/vresmap.py (new; one vcand.main evaluation, own inverse, R 7.652e6, N 11250, 1920 angles per circle)
  saves R, N_f, N_v on r in [4, 16], theta in [0, pi/2] (runs/audit/c6aS1full_resmap.npz; driver scratch/run_resmap.sh).
  e = |R|/N_f. Radial knots from spline_knots mapped to r by q = 1 - (1 + (r/L)^2)^(-(1-k)/2).
  Results:
  (a) Location. Inside the ring 8.2 <= r <= 9.4 and theta <= 0.5 the maximum of e is 1.86e-5 (theta 0.20 to 0.25), 1.2e-5
      (theta 0.10 to 0.15 and 0.25 to 0.30), 8.1e-6 (theta <= 0.02, i.e. next to P on the axis). Outside the ring, e <= 2.9e-6
      at every angle. The maximum is at r 8.7124, theta 0.2291, i.e. (x, y) = (8.485, 1.978), x - x* = -0.116: on the stem above
      P at y about 2, where the lead reports a dip of H_xx near x* - 0.1 (NOTES 00:08Z item 2). The same grid point is the
      maximum on c4_r1 final and c6a it2250.
  (b) Radial scale. The ring is the refined-knot zone: knot spacing 0.066 in r on [7.74, 9.74] (0.10 to 0.15 outside). At fixed
      theta (0.03, 0.10, 0.23, 0.30, 0.45) the detrended R on 7.8 <= r <= 9.7 has its spectral peak at a wavelength of 2.0 to 2.9
      knot intervals: R changes sign from one knot interval to the next (the highest radial frequency the spline space has
      near P), and max over theta of e has one peak per knot interval (peaks 8.432, 8.501, 8.571, 8.641, 8.712, 8.80, 8.874,
      8.947, 9.021; knots 8.428, 8.493, 8.558, 8.624, 8.690, 8.757, 8.824, 8.891, 8.959, 9.028). |R| is about 25 percent larger
      next to knots than mid-interval.
  (c) Angular scale. sin(n theta) coefficients of R on circles r = 8.61, 8.71, 8.80: 96 to 99 percent of the norm is in n < 200,
      1 to 4 percent in 201 <= n < 251, none above 251. The angular cut (cos(2 m theta), m <= 100) is not where the residual
      piles up.
  Reading (numerical; not a proof): the near-P residual of the 215-function basis is a knot-scale radial representation error
  on the stem zone r = 8.2 to 9.4, theta <= 0.5. This supports the lead's 00:41Z reading that this radial basis is the limit.
  Test that c6b (spacing 0.033 on [7.74, 9.67], 244 functions) and c6c (0.016, 302 functions) decide: halving the spacing
  from c4_centre (0.131, 200 functions, 2-10 flux 1.22e-4) to c4_r1 (0.066, 1.80e-5) gave a factor 6.8. If the profile is
  smooth at these scales the next halving should give a comparable or larger factor, and the residual peak should again
  alternate at the new knot scale. A factor below 2, or a peak that stays at about 0.07 to 0.15 in r, would mean the limit
  is not the knot spacing (a solution feature, the fit, or the representation in theta). Knot check of c6b and c6c start
  shapes: all interior knots simple (G35).
  Verdict: OPEN (diagnostic recorded; decision on the c6b/c6c segments).
  Addendum 2026-10-18T01:13Z: c6c start shape (work/c6/c6c_start_shape.npz, 302 radial functions obtained from c6a segment 1 by two
  rounds of knot insertion; lead transfer residual 1.24e-11) audited with gen_audit.sh at R 7.652e6: c_l 5.5763607, hP-1
  -1.9e-07, every flux and N_v band maximum equal to c6a segment 1 to the 4 digits printed (2-10 flux 1.861e-05, N_v
  5.236e-06). The transfer is exact between nodes, and my generator and evaluator handle the 302-function basis. Any
  change in the c6c segments is therefore due to the fit.

### G37. The c_l soft direction on the lead's trials, and a c_l bracketing request. Recorded 2026-10-18T01:14Z
  Question: the numerics lane reports (NOTES_FOR_LEAD 00:03Z to 00:55Z) that its PDE rows hardly pin c_l (a valley), and that
  along the cheapest c_l direction dh(P)/dc_l is only 1.26e-3. Is there a similar soft direction on the lead's trials, and
  what does it mean for the quoted c_l?
  Method: own evaluator values (G28, G33, G35) and the difference log(rho_A/rho_B) of two fitted shapes computed with
  code/gen_shape.shape_rho (no inverse needed) on 1200 log-spaced radii in [0.01, 2000] and 239 interior angles.
  Data (R 7.652e6, my evaluator):

    fit            c_l        h(P)-1    x*         2-10 flux  N_v 2-10
    c5 dom300 fin  5.5763326  -5.9e-07  8.6008785  1.82e-05   (G33)
    c4_r1 final    5.5763638  -1.0e-06  8.6008420  1.80e-05   5.06e-06
    c6a segment 1  5.5763607  -1.9e-07  8.6008413  1.86e-05   5.24e-06

  (a) Between dom300 and c4_r1: dc_l = 3.1e-5, dh(P) = -4e-7, near-P maximum unchanged to 1 percent. The fitted rho moves
      with c_l so that h(P) = 1 is kept: |dh/dc_l| along this pair is about 0.013, against 1.078 at fixed rho (cl_from_h).
      This is the same kind of direction the numerics lane reports.
  (b) Where the two fits differ: log(c4_r1/dom300) is 1.5e-9 (mean) on r < 0.1, 1e-6 on 0.1 to 1, and 1e-5 to 2e-5 (mean),
      up to 5e-5 (max), on every band from r = 1 to 2000, with an angular spread of 7e-6 to 1.6e-5. It is a global, smooth
      deformation with |d log rho| / |dc_l| of order 1. It is not localized near P. Between c4_r1 and c6a segment 1 (dc_l =
      -3.0e-6) the difference is 1e-6 (mean) and up to 1.1e-5, also global.
  (c) Reading (numerical; not a proof): at the present near-P floor (1.8e-5 flux), trials whose c_l differs by 3e-5 are
      equally good everywhere. The rest of the plane (rms 1e-7) does not distinguish them, and the near-P ring that does
      the selecting is under-resolved (G36). The quoted c_l spread of fits (about 3e-5) is a lower bound on the
      uncertainty: each fit stays near the c_l of its start (construct5 inherited 5.57633 from c4_radialtest, lead
      00:41Z item 2; c6a moved only -3e-6 from c4_r1). It is not an error bar.
  Request to the lead (for the final basis, before any c_l is quoted beyond 5.5763): a bracketing test. Fit the final
  basis (c6b or c6c knots) from two starts whose c_l differs by at least 3e-5, for example c6a segment 1 (5.5763607)
  and the construct5 dom300 final (5.5763326) transferred by knot insertion, with the same fit grid, weights and budget.
  Report both c_l values, the near-P maxima, and h(P) - 1. If the two c_l values move together by much more than the
  residual-limited amount, c_l is pinned at the new resolution. If each stays near its start, c_l is undetermined at
  that level, and the report must say so. I will audit both between nodes.
  Verdict: OPEN (c_l is determined only to the spread of the starts, about 3e-5 or worse).

### G38. Counting conditions for P_2 (isolated profile, family, or overdetermined): external answer and my checks. Recorded 2026-10-18T01:33Z
  Question (astra_q/count1.md, asked because of the soft direction of G37): does a count of kernel, cokernel and scalar
  conditions for the linearization DF at a P_2 profile say whether the normalized profile is isolated, lies in a family,
  or is overdetermined? Answer: astra/count1/answer.md (external, treated as a set of claims). What I checked, and how:
  (a) Sign in my question. I wrote rho_y(x,0) ~ |x - x*|^((h-1)/A). The answer corrects it to (1 - h(P))/A. Check: with
      w = W_1(x,0), h = d_y W_2(x,0), g = rho_y(x,0), parity gives W_2(x,0) = 0, and d_y of the equation at y = 0 gives
      w g' + h g = g, so g'/g = (1 - h)/w with w ~ A (x - x*). The answer is right. The typo is only in the question: my
      C6, SPEC.md (lines 96, 195) and FINAL_REPORT (lines 45, 131) all state w g' = (1 - h) g. Nothing to amend.
      Verdict: CONFIRMED (the correction); no report text affected.
  (b) Claim: K f = U[f].grad rho_0 is not compact relative to L_0 = W.grad - 1 on standard Holder spaces. Check by hand:
      U[f] has symbol (xi_1 xi_2, -xi_1^2)/|xi|^2 (from psi = (-Delta)^{-1} d_x f, U = (-psi_y, psi_x)), so K is of order 0
      with symbol (xi_1 xi_2 rho_x - xi_1^2 rho_y)/|xi|^2. On the transverse covector xi = (-W_2, W_1), where the symbol
      i W.xi of L_0 vanishes, W.grad rho = rho gives sigma_K = -W_2 rho/|W|^2, as stated. It is nonzero wherever W_2 rho
      is nonzero, so K is not a lower-order perturbation there. Verdict: CONFIRMED (the symbol computation). Consequence:
      an index count that treats DF as L_0 plus a compact operator is not justified as it stands.
  (c) Claim: the two scalar conditions (at 0 and at P) do not suffice for solvability of L_0 f = g at continuous-quotient
      regularity. Counterexample in the answer: g = chi rho b(|X|), b(r) = 1/log(e r_0/r). Check: on the axis the answer's
      relation (r/q)' = g_y(x,0)/(w q) becomes (r/q)' = chi b/w ~ -1/(d x log(e r_0/x)) near 0, whose integral diverges as
      log log(1/x), so the divided coefficient of f has no limit at 0, while both scalar functionals of g vanish. The
      algebra is right. I did not check the claimed C^{2,alpha} bound on g. Verdict: CONFIRMED for the divergence;
      the regularity of g is as claimed by the answer, unchecked.
  (d) Claim: the count is only conditional. With kernel dimension 1 and cokernel dimension 2, the normalized index is -1
      (answer table, lines 289 to 294), but the Fredholm premises are unproved: L_0 is not Fredholm on the standard
      spaces (transverse oscillations, answer lines 120 to 186), and the far-field weight r^k is resonant (the r^k log r
      tangent is not a free parameter). An index -1 would mean generic nonsolvability under perturbation of the equation.
      It would not exclude an isolated solution of this particular equation. I agree with this reading; I did not verify
      the cokernel count. Verdict: OPEN (no index theorem is available to the team; nothing may be quoted from it).
  (e) Working conjecture (the answer's words): "Conditional on an exact solution existing, my working conjecture would be
      an isolated but poorly conditioned normalized profile. That is a conjecture, not a consequence of an index theorem."
      It is compatible with G37 and with the numerics lane's valley; so are a family and an approximation with a small
      irreducible defect. The report may cite it only as a conjecture of an external reviewer, if at all.
  (f) Quantitative remark, checked against the inputs I gave: with the numerics lane's sensitivities (3e-3 in l2 residual
      and 1.26e-3 in h(P) per unit c_l along the cheapest direction), dc_l = 3e-5 gives d||F|| about 9e-8 and dh about
      3.8e-8. Both are far below the present floors (near-P flux maximum 1.8e-5; h(P) to 1e-6). So equal residuals at two
      c_l values 3e-5 apart do not discriminate between isolation and a family. This supports the G37 reading: the c_l
      spread is a lower bound on the uncertainty.
  (g) Suggested test (answer lines 298 to 340): a fixed-c residual curve m(c) = inf over normalized admissible rho of
      ||F(rho, c)||, refined at each c. If sigma_c > 0, m(c0 + delta) ~ sigma_c |delta| near the minimum. A family needs
      m = 0 on an interval with a bounded tangent solving A v + X.grad rho_0 = 0, N(v) = 0, and a second-order condition.
      Added to the G37 request as an optional follow-up: if the c6d/c6e bracketing pair (lead NOTES 01:26Z item 4) ends
      with distinct c_l values, a few fits at fixed c_l (for example c_0 + {-3e-4, -1e-4, 0, 1e-4, 3e-4}) on the same
      basis would show whether the near-P maximum has a V-shaped minimum in c_l above the floor. Expected slope with the
      numerics lane's l2 sensitivity: a rise of 1e-6 needs |delta| of order 3e-4, so smaller offsets will be inconclusive.
  Verdict: (a) to (c) CONFIRMED as computations; (d), (e) OPEN. No analytic claim in the team's reports depends on G38.

### G39. c6b (244 radial functions) at LSQR iteration 500 of segment 1: intermediate check of the G36 prediction. Recorded 2026-10-18T01:41Z
  File: lead/notes/c6b_mid/it500_shape.npz (lead NOTES 01:26Z: intermediate, not a candidate), copied to
  runs/gen4/c6b_it500_shape.npz at 01:33Z. Knots: 253, simple (no repeated interior knot), minimum spacing 1.06e-3 in q.
  Method: code/gen_audit.sh at r0 7.652e-4, R 7.652e6, N 11250, nq 384, Mmax 479 (runs/audit/c6bM500_N11250_q384_R7.652e6.log);
  residual map code/vresmap.py on 6 <= r <= 14, all angles (runs/audit/c6bM500_resmap.npz), analysed with
  scratch/ana_resmap.py (axes excluded, where N_f = 0). Same evaluator and grid as the c6a segment 1 rows of G35 and G36.

    quantity                         c6a seg1 (215)   c6b it500 (244)   ratio
    c_l (identity)                   5.5763607        5.5763608
    h(P) - 1                         -1.9e-07         -3.2e-08
    flux max 2 <= r <= 10            1.861e-05        3.388e-06         5.5
    N_v max 2 <= r <= 10             5.236e-06        9.689e-07         5.4
    flux max 10 <= r <= 100          2.891e-06        2.504e-06         1.15
    J spread (|X - P| <= 0.3)        1.733e-05        3.862e-06         4.5
    B_3 (ibp)                        0.3006           0.2985
    ring 8.2-9.4, th <= 0.5: max     1.861e-05        3.388e-06         5.5
                             rms     2.514e-06        6.313e-07         4.0
    band 9.7-11 (knots unrefined)    2.891e-06        2.504e-06         1.15
    sign changes along r at the
      angle of the maximum, 7.2-10.2 27 (median 0.075)  54 (median 0.037)
    median knot spacing 8.2-9.4      0.0671           0.0335

  Lead scan (16384 x 640): 2-10 flux 3.67e-6, 10-100 flux 2.53e-6 at r 10.06, theta 0.6725; mine 3.39e-6 and 2.50e-6 at
  r 10.055, theta 0.674. Agreement within the grid difference.
  Findings: (a) halving the knot spacing on the refined ring has lowered the near-P maximum by 5.5 and the J spread by
  4.5 after 500 of the segment's iterations. Both fall together, as the lead's rule (analysis.md 13.4b) requires for a
  representation limit. (b) The radial sign alternation of the near-P residual halves its spacing with the knots (0.075 to
  0.037; the map's r step is 0.018, so this is near its resolution, but the count doubles). (c) The residual outside the
  refined band (r about 10.05 on the stem, knot spacing 0.157) is unchanged and is now as large as the near-P maximum.
  The lead's c6d plan (refine 9.70 < r < 13.5 and 6.8 < r < 7.70) targets it. (d) c_l moved +1e-7 from its start, as
  in G37.
  Verdict: CONFIRMED as an intermediate result. The G36 prediction (factor of order 6.8 per halving; a factor below 2 would
  refute the knot reading) holds so far. The segment-end shape decides; it will be audited at three resolutions.

### G40. Audit of analysis.md 13.9 (lead, 01:22Z: what controls the c_l error of a trial). Recorded 2026-10-18T01:43Z
  Method: hand derivation of each step.
  (a) First-order perturbation. With F(rho*, c*) = 0, F(rho, c) = R, D_c F = X.grad rho and l0(rho*) = l0(rho) = 1, the
      expansion gives Lb(rho* - rho, c* - c) = (-R, 0), hence c* - c = -<phi, R> with phi the first component of
      Lb^{-*} e_c. Correct under the stated (unproved) invertibility of Lb. The citation G33 (c) is right (equal near-P
      maxima, c_l differing by 3.2e-5; also G37). CONFIRMED (conditional, as labelled).
  (b) Transport inverse. v(s) = e^{-s} u(Phi_s X) gives v' = e^{-s} g(Phi_s X): correct. At P, W = 0 and by parity
      DW(P) = diag(A, h(P)) and grad rho(P) = (0, rho_y(P)), so grad R(P) = (DW(P)^T - I) grad rho(P) = (0, (h(P) - 1)
      rho_y(P)): correct. With h(P) = 1 < A the backward flow approaches P along eta at rate e^{s}, and e^T u(Phi_{-T} X)
      -> u_eta(P) eta_inf(X): correct. The first-order relation u = -rho J (1 + O(J)) + K rho follows from
      rho(Phi_s X) = e^s rho(X) exp(-int_s^0 R/rho) (I checked it; the kernel element of the frozen operator is
      rho e^{-J}, equal to rho to first order). CONFIRMED with one precision note:
      the hypothesis "g = o(|X - P|) at P" is not enough for the integral to converge. Since |Phi_s X - P| ~ eta e^{s}
      as s -> -inf, g ~ |X - P| / log(1/|X - P|) gives an integrand of order eta/|s| and a divergent (log) integral.
      The statement needs g = O(|X - P|^{1+alpha}) for some alpha > 0, or a Dini condition. For a C^2 trial with
      h(P) = 1 the residual satisfies this, so the conclusions of 13.9 are unaffected. (Same mechanism as the log log
      example of G38 (c).)
  (c) Correct and correctly hedged: c* - c is a functional of the transport correction and its nonlocal feedback, and no
      bound follows without an estimate of |Lb^{-1}|. CONFIRMED.
  (d) Reporting criterion (c_l with the spread over fits; the change of c_l between successive fits should shrink with
      the J spread and the near-P maximum; a consistency criterion, not an error bound): agrees with G37 and G31.
      CONFIRMED.
  Verdict: 13.9 CONFIRMED as a labelled heuristic, with the precision note in (b) (replace o(|X - P|) by
  O(|X - P|^{1+alpha})).
  G39 addendum (2026-10-18T02:01Z): the full segment-audit pipeline (scratch/seg_audit.sh; tag c6bM5b) on the same intermediate shape,
  three domains of my inverse and two resolutions at the largest:

    config (r0 7.652e-4)          c_l        hP-1      flux 2-10  N_v 2-10  flux 10-100  N_v r>=1000  flux r<=0.1  J spread
    N 9000  q384 M479 R 7.652e4   5.5763612  +1.6e-06  4.00e-06   1.16e-06  2.44e-06     4.43e-06     1.5e-08      9.9e-06
    N 10125 q384 M479 R 7.652e5   5.5763608  +8.9e-09  3.32e-06   9.51e-07  2.51e-06     1.37e-06     1.6e-08      3.8e-06
    N 11250 q384 M479 R 7.652e6   5.5763608  -3.2e-08  3.39e-06   9.69e-07  2.50e-06     1.44e-06     1.5e-08      3.9e-06
    N 16875 q512 M639 R 7.652e6   5.5763608  -6.9e-08  3.57e-06   1.02e-06  2.53e-06     1.45e-06     6.0e-08      3.9e-06

  (J spread at the smallest distance, 0.01.) Readings:
  - R 7.652e4 carries my inverse's known domain error (h(P) - 1 = 1.6e-6, G28 (b), G30); its J spread at eps 0.01 is
    larger for that reason (log divergence, G24). R 7.652e5 and 7.652e6 agree to 3e-8 in h(P) and to 2 percent in the
    near-P maximum, as the R^(2k-2) law predicts.
  - The finer grid (N 16875, q512, M639) sees a 5 percent higher near-P maximum (sampling between nodes) and a larger
    r <= 0.1 value (6e-8 flux, 1.3e-7 N_v), which goes with my Poisson relE on [r0, 0.01] rising from 7e-5 to 2e-4
    (rounding in my evaluator, G28 (e)). Both are far below 1e-6.
  - Far field r >= 1000: N_v maximum 1.44e-6 near r = 2.9e4, theta 0.9, the same at R 7.652e5 and 7.652e6 and at both
    resolutions. So it belongs to the trial, not to my inverse. In the flux normalization it is 3.6e-7. (N_v = |rho| +
    |X.grad rho| + |U.grad rho| is close to 1.2 |rho| in the far field, where the flux norm is several times larger.) It
    was 1.84e-6 on c4_r1 and 1.50e-6 on c6a seg1. For a YES at "about 1e-6 in both normalizations" this band must be
    reported. It is near the threshold, not a blocker by itself.
  - extra_checks (R 7.652e6): identity c_l 5.576360786; c_l from h(P) = 1 at fixed rho 5.576360831 (difference
    +4.6e-8; c6a seg1 1.7e-7, c4_r1 9.5e-7); D14 centre relations to 9e-8 relative; min W_2/y on the y-axis 5.5766 > 0;
    no cell of the open quadrant where both components of W change sign.
  G39 addendum 2 (2026-10-18T02:04Z): where the far-field N_v maximum sits. Residual map on 1000 <= r <= 3e5, all angles
  (runs/audit/c6bM5bfar_resmap.npz, R 7.652e6, N 11250). The N_v maximum 1.444e-6 is at r = 2.35e4, theta = 1.5413,
  next to the y-axis (the "at r 2.9e4, theta 0.90" printed by vaudit is the flux argmax). It is nearly constant in r
  (max per range: 1.16e-6 on 1e3 to 3e3, 1.26e-6 to 1e4, 1.44e-6 on 1e4 to 4e4, 1.35e-6 to 1e5, 0.92e-6 to 3e5), with no
  sign change in r over [r/3, 3r]. In theta it is a ripple with period about 0.031 (local maxima at 1.420, 1.450, 1.479,
  1.512, 1.541, 1.568), that is cos(2 m theta) with m about 100, the trial's angular cap. Its amplitude relative to N_v
  grows toward the axis because rho vanishes like cos^2 theta there. The flux normalized value at the same point is
  8.9e-8 (N_f/rho = 20 next to the axis, against N_v/rho = 1.23). Reading: the far-field N_v maximum is the angular
  truncation of the trial (m <= 100) seen in the stricter normalization next to the y-axis. Radial refinement (c6b to
  c6e) will not change it; a larger angular cap would. To the lead: for the YES standard (about 1e-6 in both
  normalizations, regions next to both axes, G20 b1) this band must be quoted as N_v 1.4e-6 next to the y-axis for
  r >= 1000. It is near the threshold and is not by itself a blocker.

### G41. Audit of analysis.md 13.10 and 13.11 (soft c_l, external referee astra/softcl1), of FINAL_REPORT (mtime 02:06Z) and of the section 4 draft (02:06Z); corrections to G38 (f), (g). Recorded 2026-10-18T02:17Z
  Method: hand derivation of each formula; diff of FINAL_REPORT against notes/FINAL_REPORT_backup_0150.md and of
  notes/final_sec4_draft.md against notes/final_sec4_draft_backup_0159.md; a slow-curve computation (scratch/slowcurve.py).
  (a) 13.11 (a), coupled identity. With rho~ = rho_d e^{-phi}, f = rho~ - rho_d, W_d = c X + U[rho_d]: W~ = W_d + U[f]
      (linearity of the velocity law), grad rho~ = rho~ (grad log rho_d - grad phi) and W_d.grad rho_d = rho_d give
      F(rho~, c)/rho~ = -W_d.grad phi + U[f].grad log rho~. Correct. F(k rho, c) = k (k - 1) U[rho].grad rho for an exact
      rho: correct. Gaussian example: for rho = x^2 y e^{-a r^2} the sin(2 theta) coefficient of d_x rho is
      e^{-a r^2}(r^2 - a r^4/2), and psi_xy(0) = (1/2) int_0^inf f_2(s)/s ds = (1/2)(1/(2a) - 1/(4a)) = 1/(8a); also
      (1/4) int r e^{-a r^2} dr from the sin(3 theta) coefficient r^3 e^{-a r^2}/4. With a = 1 + eps the centre defect is
      1/8 - 1/(8(1 + eps)) = eps/(8(1 + eps)). Correct. So 13.10 (a) is a frozen-field mechanism only: CONFIRMED.
  (b) 13.11 (b). If B(u, d) = (L u + d q, N u) is an isomorphism and l is the exponent component of B^{-1}(., 0), then
      l(L u + d q) = d for N u = 0, so |d| <= |l| |L u + d q|, and {L u : N u = 0} = ker l is closed. Correct. Model
      y u' = 0, u(0) = d, u(1) = 0: only u = 0, d = 0; u_T = d chi(log y / T) has sup |y u_T'| <= C |d|/T and C^1 norm of
      order e^T/T. Correct. Arithmetic: (1/A) log(1/h) = 6.908/10.1527 = 0.680 at h = 1e-3, and log 2 / A = 0.0683 per
      halving. Correct. Reading (softness in c_l is a property of the weak residual norms and of the trial space's
      resolution near P, neither evidence for nor against a family): agrees with G37 and G38 (d). CONFIRMED.
  (c) 13.11 (c). Counterexample F(a, d) = (a, d), J = (a + d, -a - d): fixed-d least squares gives a = 0, S = (1, -1);
      the trial (eps, 0) has exponent error 0 and estimate <J, S>/<S, S> = eps. Correct, so the J-pattern estimator of
      13.10 (c) is rightly withdrawn. Replacement: with v = argmin |M v + b| and s = M v + b, M^T s = 0 gives <s, b> =
      |s|^2 - <M^T s, v> = |s|^2 and <s, M e + b d> = d |s|^2 for every e, so dk = -<f, s>/|s|^2 is the exponent part of
      the Gauss-Newton step. Correct. The stated limitation (it locates the least-squares minimizer of a basis in c_l,
      not c* of the profile) is right. CONFIRMED.
  (d) 13.11 (d). At a least-squares floor m0 the objective along the soft direction is m(delta)^2 = m0^2 + sigma^2 delta^2
      to second order (at the minimum <f0, s> = 0). With sigma 3.2e-3 and m0 6e-4: m rises by (sigma delta)^2/(2 m0) =
      8.2e-12 at delta = 3.1e-5. Correct. This corrects my G38 (f) and (g): the linear rise sigma_c |delta| (about 9e-8
      at delta = 3e-5) holds only next to an exact solution (m0 = 0). At a floor the rise is quadratic, so equal residuals
      discriminate even less than G38 (f) says, and the G38 (g) offset rule ("a rise of 1e-6 needs |delta| of order
      3e-4") is withdrawn. The right rule is that m(c) stays flat until sigma |delta| is comparable to m0, and sigma
      must be measured on the basis itself (soft_tangent.py, lead NOTES 01:50Z). The approved wording ("representative
      fitted exponent c_l = 5.57636 (approximately) ... spread measures empirical reproducibility, not an uncertainty
      interval ... diagnostics do not yet calibrate the absolute exponent error or the accuracy of the last quoted
      digits") is accurate. I accept it in place of my G35 (b) "5.57634 +- 3e-5 at most", on one condition: the
      six-digit value never appears without the disclaimer sentence (first lines, abstract, tables). Also accepted: "the
      spread measures reproducibility; if the exponent is unique, one of two fits Delta apart is off by at least Delta/2"
      in place of my informal "lower bound" (G37 (c)).
  (e) FINAL_REPORT 02:06Z, timeline 00:10 to 01:43 (new lines summarizing G29 to G40). Each line matches the item it
      cites. One precision for the 01:10 line ("sits on the refined-knot ring ... on the slow curve above P"). Check:
      bisection for the slow trajectory from P in my W (c6a seg1 and c6b it500 maps) gives x - x* = -0.0110 at y = 1.0
      and -0.020 at y = 1.5 (kappa y^2: -0.0109, -0.025); beyond y about 1.5 the trajectory cannot be followed (separation
      rate A = 10.15). The c6a residual is elevated within about 0.1 in x of that curve at y = 1 (1.1e-5 at offsets -0.1
      to 0), and its maximum (y 1.978, x - x* -0.116) is about 0.08 left of the extrapolated curve (about -0.035 there).
      "Near the slow curve above P" is accurate. "On the slow curve" is acceptable as a description, not as a location.
      No other change in FINAL_REPORT since 01:43Z. CONFIRMED.
  (f) Section 4 draft 02:06Z, c_l accuracy paragraph (still [TBD]): the default wording is (d); the plan (o), (i) to
      (iii) is sound. The rule "quote c_l only to the offset at which the best fixed-c_l fit has a near-P maximum
      clearly above the candidate's; the tangent trials give only an upper estimate of the least cost at an offset"
      is correct: a cheap tangent trial at offset delta shows c_l is not pinned to better than delta; an expensive one
      shows nothing. CONFIRMED.
  Verdict: 13.10 as superseded and 13.11 CONFIRMED (computations and readings); G38 (f), (g) corrected as in (d);
  FINAL_REPORT 02:06Z and the section 4 draft CONFIRMED, with the precision note in (e) and the condition in (d).

### G42. c6b (244) and c6c (302 radial functions) at the end of segment 1: between-node audit, the G36 test, J at two cutoffs. Recorded 2026-10-18T03:17Z
  Files: lead/work/c6/c6b_seg1_shape.npz (mtime 02:44:14Z) and c6c_seg1_shape.npz (02:44:44Z), copied to
  runs/gen4/c6bS1_shape.npz, c6cS1_shape.npz at 02:52Z. Knots: 253 and 311, all interior knots simple. Knot spacing in r
  (median): 7.7 to 9.7: 0.062-0.072 (c6a), 0.031-0.036 (c6b), 0.0155-0.0181 (c6c); 9.7 to 11: 0.157 on all three.
  Method: scratch/seg_audit.sh (my generator code/gen_shape.py, my inverse and evaluator code/vaudit.py) at r0 7.652e-4 and
  (R, N, nq, Mmax) = (7.652e4, 9000, 384, 479), (7.652e5, 10125, 384, 479), (7.652e6, 11250, 384, 479),
  (7.652e6, 16875, 512, 639); for c6c also (7.652e6, 22500, 384, 479), because its knot spacing near P (0.0155) is below the
  N 11250 grid step (0.0176 at r 8.6; 0.0085 at N 22500). Residual maps code/vresmap.py on 6 <= r <= 14 (N 11250, and
  N 22500 for c6c on 7 <= r <= 11.5), analysed with scratch/ana_resmap.py and scratch/ang_split.py (new: splits R(r, .)
  into sin(n theta) with n < 195 and n >= 195 and reports max |R_part|/N_f per region). Lead scans read with the lead's
  scripts/scansum.py.
  (a) Table, R 7.652e6, N 11250 unless marked (c6a: G35).

    quantity                          c6a seg1 (215)  c6b seg1 (244)  c6c seg1 (302)       factor a->b, b->c
    c_l (identity, mine)              5.5763607       5.5763632       5.5763609
    h(P) - 1 (N 16875; c6c N 22500)   -1.9e-07 (N11250) -6.4e-08      +8.5e-09 / -1.9e-08
    flux max 2 <= r <= 10             1.861e-05       4.642e-06       2.227e-06 (N22500 2.285e-06)   4.0, 2.1
    flux max |X - P| < 0.5            8.110e-06       3.248e-06       2.227e-06 (2.285e-06)          2.5, 1.46
    N_v max 2 <= r <= 10              5.236e-06       1.374e-06       8.250e-07                       3.8, 1.67
    flux max 10 <= r <= 100           2.891e-06       3.196e-06       2.292e-06 (2.323e-06)
    N_v max, all r                    5.236e-06       1.374e-06       1.409e-06 (1000 <= r <= R)
    J spread at |X - P| = 0.03 / 0.01 1.733e-05 / 1.733e-05  3.086e-06 / 3.289e-06  1.127e-06 / 1.200e-06   5.3, 2.7
    B_3 (mine, wpp_ode ibp / orig)    0.3006 / 0.3002 0.2989 / 0.3004 0.2983 / 0.2989

  Resolution: on c6b the three configurations with R >= 7.652e5 agree to 7 percent in every band maximum with r >= 0.1
  (2-10 flux 4.64e-6 to 4.95e-6); at R 7.652e4 the 2-10 flux is 5.34e-6 and the far-field N_v 4.35e-6, the known domain
  error of my inverse at its smallest R (G28 (b), G30). On c6c the band maxima with r >= 0.1 at N 11250, 16875, 22500
  agree to 3 percent; h(P) - 1 at N 11250
  (+2.7e-7) is an evaluation error (grid step comparable to the knot spacing), so for c6c and finer bases I quote h(P)
  from N >= 16875. The lead's scans (16384 x 640, 32768 x 640) agree with mine: 2-10 flux 4.93e-6 / 2.28e-6, 10-100
  3.19e-6 / 2.37e-6, N4 1.41e-6 / 8.41e-7, h(P) - 1 -4.55e-8 / -7.99e-9.
  (b) Where the residual sits on the 302 basis (N 11250 map; the N 22500 map agrees to 5 percent):
    - stem ring 8.2 <= r <= 9.4, 0.1 <= theta <= 0.5 (the c6a maximum of G36): all 1.86e-5 / 4.64e-6 / 1.37e-6 on
      c6a / c6b / c6c; its n < 195 part 1.86e-5 / 4.79e-6 / 1.02e-6 (factors 3.9 and 4.7 per halving); its n >= 195 part
      1.24e-6 / 1.62e-6 / 1.23e-6 (no change). On c6b the radial sign alternation at the angle of the maximum has median
      spacing 0.0368 (knot spacing 0.0335): the residual follows the new knot scale.
    - strip next to the x-axis left of P, theta <= 0.1 (y about 0.13 to 0.28, x - x* from -0.9 to -0.1): 2.87e-6 /
      2.78e-6 / 2.17e-6 for 6 <= r <= 8.2 and 8.14e-6 / 3.25e-6 / 2.23e-6 for 8.2 <= r <= 9.4. On c6c, at r 7.69 to 8.50,
      92 to 95 percent of the angular energy of R lies in 150 <= n < 210, and the spectrum windowed to theta < 0.15 peaks
      at n = 201 to 213. The trial's angular space (cos(2 m theta), m <= 100, times cos^2 sin) ends at n = 203. This
      component did not fall when the knot spacing on 7.7 <= r <= 8.2 was divided by 4 (factor 1.3 from c6a to c6c).
      On c6a at r 8.43 and 8.71 the same windowed spectrum peaked at n = 13 to 19 (radial knot error).
    - unrefined band 9.7 <= r <= 11 (stem at y 6, x - x* about -0.7): 2.89e-6 / 3.20e-6 / 2.29e-6; the n < 195 part
      alone gives 2.22e-6 of the 2.29e-6 (radial).
      This is the global maximum on c6c (r 10.075, theta 0.671), where the lead's map also puts it. c6d refines it.
    - far field (G39 addendum 2): the N_v maximum 1.41e-6 at r about 2e4, next to the y-axis, is the m = 100 angular ripple.
  (c) The G36 test. Prediction: if the near-P residual is the knot-scale radial representation error, each halving of the
      knot spacing lowers it by a factor of order 6.8, and a factor below 2 refutes that reading. Result:
      - for the component the prediction was about (stem ring, radial, n < 195) the factors are 3.9 and 4.7, and the
        alternation follows the knots: the knot reading is CONFIRMED for it. The factors are below the 6.8 of
        c4_centre to c4_r1.
      - for the near-P maximum as a whole the second halving gives 1.46, below 2. The reason is not the stem: on the 302
        basis the near-P maximum has moved to the near-axis strip, which sits at the angular band edge and does not
        respond to radial refinement. As a description of the whole near-P residual on the 302 basis, the knot
        reading is REFUTED; the remaining limits are angular (m <= 100: the near-axis strip, 2.2e-6 in N_f, and the
        far-field ripple, 1.4e-6 in N_v) and the unrefined radial band 9.7 to 11 (2.3e-6).
      This is a statement about the trial space, not about the profile. c6d (radial refinement on 9.70 to 13.5 and 6.8
      to 7.70) addresses the last item only. My expectation, recorded before its result: c6d leaves the near-axis strip
      near 2e-6 and the far-field N_v near 1.4e-6, so it cannot reach the G20 (b1) standard of about 1e-6 in both
      normalizations without more angular modes. I have not checked whether more angular modes suffice.
  (d) Analysis 13.4b rule (near-P maximum and J fall together): J spread at d = 0.01 fell by 5.3 and 2.7 and the near-P
      flux maximum by 2.5 and 1.46. Both fall; J falls faster. Consistent with a representation limit.
  (e) Lead request (b), J at two cutoffs: on c6c (N 22500) my J spread is 1.157e-6 at |X - P| = 0.03 and 1.252e-6 at 0.01
      (N 11250: 1.127e-6, 1.200e-6). From 0.03 to 0.01 Jmin goes -1.496e-6 to -1.652e-6 and Jmax -3.39e-7 to -4.00e-7:
      a common shift of -0.6e-7 to -1.6e-7 over a backward time of about ln 3 near P, i.e. R/rho of order -1e-7 there
      (G24: R/rho at P equals h(P) - 1; my h(P) - 1 is -1.9e-8 at N 22500, the rest is the residual next to P). The
      spread changes by 8 percent between the cutoffs, so on c6c it is the accumulated transport residual along the
      paths, not h(P) - 1. (c6b, N 16875: 3.09e-6 and 3.29e-6.) The lead's J split (r0 20, 10 angles) gives 8.46e-7 total
      spread; my 24 angles give 1.16e-6 at 0.03. Same order, different angle sets.
  (f) c_l: +2.5e-6 during c6b segment 1 and +2.3e-7 during c6c segment 1. The two segment-1 ends differ by 2.3e-6, and the
      one with the smaller residual (c6c) is at 5.5763609. These are reproducibility numbers (analysis 13.11 (d)).
  Verdict: c6b and c6c segment 1 ends CONFIRMED as measured above (independent between-node evaluation agrees with the
  lead's scans). G36 knot reading: CONFIRMED for the stem component, REFUTED for the near-P maximum as a whole on the 302
  basis, where an angular band-edge component next to the x-axis now dominates. Neither is at the YES standard (c6c: 2.3e-6
  in N_f, 1.4e-6 in N_v).

### G43. The lead's B_3 estimator (notes/b3_ibp/b3_ibp.py): the integrated-by-parts form does not converge in the quadrature order. Recorded 2026-10-18T03:17Z
  Observation: in the lead's outputs (notes/b3_ibp/c6a_seg1_out.txt, c6b_seg1_out.txt, c6c_seg1_out.txt) the ibp value
  depends on the Gauss-Jacobi order n of the end piece [xc, x*], while the orig form does not:
    ibp(n 80) - ibp(n 40) = +0.0035 to +0.0040 (c6a), +0.0068 to +0.0077 (c6b), +0.0107 to +0.0121 (c6c);
    orig(n 80) - orig(n 40) is below 1.2e-4 on all three.
  The ibp n 40 values are 0.3021 to 0.3032 on all three bases; the n 80 values move with the basis (0.306, 0.309, 0.313).
  The "drift apart of the two forms under near-P refinement" (lead NOTES 02:47Z item 2) is therefore the n 80 end piece.
  Check: a copy of the lead script (scratch/lead_b3_copy/b3_ibp_ncheck.py; only the loop over n extended, xc 0.3,
  xlo 0.05, K 7), run on lead/work/c6/c6c_seg1_fields.npz with A_g = mu1:
    n      20      40      80      160     320     640
    orig   0.29855 0.29809 0.29812 0.29813 0.29812 0.29813
    ibp    0.29899 0.30254 0.31321 0.34570 0.44459 0.74559
  The ibp increments grow by a factor 3.0 to 3.1 per doubling of n. Reading: with m = -w/g ~ (x* - x) the ibp end-piece
  integrand is (a2/g^3 - kappa) m^(beta - 2) A_g/g. It is integrable only if a2/g^3 - kappa = O(x* - x). If the numerical
  a2/g^3 tends to a value other than kappa, the integrand behaves like delta (x* - x)^(beta - 2), which is not
  integrable. Gauss-Jacobi nodes reach x* - x of order n^(-2), so the sum grows like n^(2(1 - beta)) = n^1.61, a factor
  2^1.61 = 3.05 per doubling, as observed. The mismatch delta comes from the 0/0 quotient (w' - A_g)/w near x*, which
  divides the trial's knot-scale structure in w' by w ~ mu1 (x - x*). That explains why it grows under near-P refinement.
  The identity orig = ibp (G17) is not in question; this is the implementation of the ibp end piece.
  Consequences:
  - the lead's ibp numbers at n >= 40 are not converged quadratures and must not enter a quoted B_3 or its spread.
    In particular the medians 0.3042 / 0.3060 / 0.3081 and the range "[0.29, 0.32]" from NOTES 02:47Z should not be used;
  - the orig form (converged in n to 5e-4) and my estimator agree: lead orig median 0.3014 / 0.2991 / 0.2980; mine (ibp
    / orig) 0.3006 / 0.3002, 0.2989 / 0.3004, 0.2983 / 0.2989 on c6a / c6b / c6c. B_3 about 0.30 (0.298 to 0.301 on
    these bases) stands, positive in every variant;
  - fix (suggestion): subtract the local limit exactly (expand a2/g^3 - kappa at x* from the w-Taylor data, or end the
    Gauss-Jacobi piece at x* - eps with an analytic remainder). Alternatively quote the orig form only.
  Verdict: lead ibp implementation REFUTED as a converged estimate (n dependence shown); B_3 about 0.30 CONFIRMED from the
  orig form and from my estimator.

### G44. FINAL_REPORT (mtime 02:49:37Z) and section 4 draft (02:49Z). Recorded 2026-10-18T03:17Z
  Method: diff against notes/FINAL_REPORT_backup_0252.md and notes/final_sec4_draft_backup_0254.md.
  (a) The 01:10 line now reads "near the slow curve above P" (G41 (e)). New timeline line 02:17 summarizing G41: it
      matches G41 (a) to (d). "The nonlocal velocity feedback contributing a term without decay" means the term has no
      factor 1/T (analysis 13.11 (a)). The sense is right. More precise: "without the 1/T decay of the transport term".
  (b) Six-digit c_l: FINAL_REPORT contains none. The section 4 draft quotes 5.57636 only inside the disclaimer sentence
      and now states the G41 (d) condition. Its "Old notes" paragraph contains 5.5763607, 5.5763297, 5.5763638 and
      5.57624 to 5.57637 without the disclaimer sentence next to them. That is acceptable in a draft note; in the final
      text each such number must follow the disclaimer or be removed.
  (c) Section 4 draft line 10 (B_3 "[TBD: about 0.30] ... with variant spread [TBD]"): fill the spread from the orig form
      or from my estimator, not from the lead's ibp end piece at n >= 40 (G43).
  Verdict: CONFIRMED with the notes (a) to (c).

### G45. Numerics-lane exports (NOTES_FOR_LEAD 02:02Z, 02:08Z, 03:02Z, 03:20Z) in my evaluator; tail-exponent correction of my evaluator. Recorded 2026-10-18T03:45Z
  Method (own code only; the exporters' files are read as data):
  - code/vnum_import3.py puts each export on my log grid:
    - b = a/w is interpolated barycentrically in the computational variable s, on the Chebyshev-Radau nodes
      s_j = -cos(2 pi j/(2N+1));
    - the map is r = L (1+t)/(1-t+a)^p with t = T(s) (cluster), as defined in the exporter's docstring;
    - in angle it uses the exact cos(2 k theta) series;
    - it reads state files (key b) as well as field files.
  - Checks:
    - r(T(s)) at my points to 5e-13;
    - node radii of field files to below 1e-10 (asserted);
    - agreement with code/vnum_import2.py on the unclustered S0 to 8e-15;
    - clustered field files without a cluster key (fields_npw_*) are refused (node check 0.08); the state files carry
      the key.
  - vaudit at N 3000, 1282 angles, Mmax 255, r_start 20, with the tail-exponent option of (d). N 1500 / 642 / 131 was run
    for comparison; the N 3000 values are quoted.
  - Logs: runs/numchk2/<tag>_vaudit.log (tags valS_*, lsqS*, mcS_s*). Tabulator: scratch/tab_numchk2.py.
  - All residuals below are maxima of |R|/N (flux N_f / N_v) unless marked rms.
  (a) Valley perturbation fields (02:08Z), R 3000, (256,64) unclustered:

      | state | c_l (mine, identity) | x* | h(P) - 1 | \|X-P\| < 0.5 | \|X-P\| < 2 | 10-100 | 100-1000 | J(0.01) |
      |---|---|---|---|---|---|---|---|---|
      | S0 | 5.57646 | 8.6011 | +2.3e-4 | 1.1e-4 / 3.1e-5 | 3.5e-4 / 1.0e-4 | 1.6e-4 / 3.3e-5 | 7.9e-6 / 3.4e-5 | 6.5e-4 |
      | S0 + 0.001 v_cl, S0 - 0.001 v_cl | 5.57746, 5.57546 | 8.6017, 8.6005 | +2.3e-4 | as S0 to 2 digits | as S0 | as S0 | as S0 | 6.5e-4 |
      | S0 + 0.01 v_cl | 5.58646 | 8.6068 | +1.4e-4 | 1.5e-4 / 4.2e-5 | 3.9e-4 / 1.1e-4 | 1.6e-4 / 3.3e-5 | 8.5e-6 / 3.9e-5 | 7.0e-4 |
      | S0 - 0.01 v_cl | 5.56646 | 8.5954 | +1.3e-4 | 1.5e-4 / 4.4e-5 | 3.8e-4 / 1.1e-4 | 1.6e-4 / 3.3e-5 | 8.6e-6 / 3.9e-5 | 7.0e-4 |

      - My identity c_l equals the exporter's in all five states to the 5 printed decimals. The perturbations move it by
        +-1.000e-2 and +-1.000e-3, so they are identity-consistent.
      - At +-0.01 the residual rises by about the same amount in both directions:
        - by 35 to 42 percent in |X-P| < 0.5;
        - by at most 15 percent in every other band (|X-P| < 2: 11 percent);
        - J(0.01) by 8 percent.
        This is the quadratic rise at a floor. h(P) - 1 falls from +2.3e-4 to +1.3e-4 / +1.4e-4 in both directions.
      Verdict: CONFIRMED in substance:
      - A c_l change of 1e-2 along v_cl is not detected by the residual, J or h(P), at a near-P level of 1e-4 (N_f) or
        3e-5 (N_v).
      - The 02:08Z criterion "agree to within a few percent" holds away from P but not in |X-P| < 0.5, where the change is
        35 to 42 percent. Their own measure gave 12 percent in |X-P| < 2; mine gives 11 percent there.
  (b) The 02:02Z pair (unpinned LSQ):

      | state | c_l mine (exporter) | h(P) - 1 mine (exporter) | \|X-P\| < 0.5 | \|X-P\| < 2 | 0.1-2 | 10-100 | 100-1000 | 1000-R | J(0.01) |
      |---|---|---|---|---|---|---|---|---|---|
      | lsq R 3000 | 5.59338 (5.59339) | -4.0e-4 (-4.1e-4) | 1.9e-4 / 5.2e-5 | 3.2e-4 / 9.1e-5 | 3.0e-6 / 5.8e-6 | 4.1e-5 / 3.0e-5 | 2.7e-6 / 3.0e-5 | 1.4e-5 / 2.1e-4 | 1.6e-3 |
      | lsq R 1000, p 1.5 | 5.29227 (5.29226) | -5.2e-4 (-5.6e-4) | 2.4e-4 / 7.0e-5 | 5.0e-4 / 1.4e-4 | 2.6e-6 / 5.1e-6 | 4.0e-5 / 5.6e-5 | 2.7e-5 / 2.9e-4 | (R = 1000) | 2.4e-3 |

      - rms values, N_f / N_v:
        - R 3000: 10-100 2.7e-6 / 9.0e-6; 100-1000 1.8e-6 / 1.1e-5; 1000-R 2.2e-6 / 1.7e-5.
        - R 1000: 10-100 6.0e-6 / 2.2e-5; 100-1000 4.6e-6 / 2.6e-5.
      Verdict on the 02:02Z prediction:
      - "the same residual level as each other": CONFIRMED. The two states are within a factor 1.6 of each other next to
        P, with c_l 0.30 apart.
      - "1e-5 .. 1e-4 next to P": CONFIRMED for N_v (5e-5 to 1.4e-4). In N_f the maxima are 2e-4 to 5e-4.
      - "about 1e-6 elsewhere": CONFIRMED for r <= 2 (3e-6 max, 4e-7 rms). REFUTED in my evaluator for r >= 10:
        - maxima 3e-5 to 6e-5 at 10-100, and 2e-4 to 3e-4 (N_v) in the outermost band;
        - rms 2e-6 to 3e-5.
        The outermost-band maxima sit next to R (r 964, 2883) and may contain the closure kink at R. The 10-100 values
        (at r 10.05 and 10.17, next to the stem) do not.
  (c) Fixed-c_l states of the m(s) curve (03:02Z, 03:20Z):
      - (256,64) clustered at P, R 3000. State files mc_N256M64cl_s*.npz and mc2_N256M64cl_s*.npz, 13 values
        s = 5.5163 to 5.7063.
      - h(P) - 1 of the exporter is from runs/mc_N256M64cl.log and runs/mc2_N256M64cl.log.

      | s | c_l mine | h(P) - 1 mine (exporter) | \|X-P\| < 2, N_f / N_v | J(0.03) / J(0.01) | flux rms, all r |
      |---|---|---|---|---|---|
      | 5.5163 | 5.51630 | -2.7e-4 (-2.70e-4) | 1.3e-4 / 3.5e-5 | 4.6e-4 / 7.0e-4 | 1.73e-6 |
      | 5.5563 | 5.55630 | -2.2e-4 (-2.29e-4) | 1.0e-4 / 2.9e-5 | 3.5e-4 / 5.6e-4 | 1.31e-6 |
      | 5.5763 | 5.57630 | -1.9e-4 (-1.94e-4) | 9.3e-5 / 2.6e-5 | 3.0e-4 / 4.8e-4 | 1.17e-6 |
      | 5.5963 | 5.59630 | -1.6e-4 (-1.66e-4) | 8.3e-5 / 2.4e-5 | 2.5e-4 / 3.9e-4 | 1.03e-6 |
      | 5.6263 | 5.62630 | -1.3e-4 (-1.42e-4) | 6.9e-5 / 2.1e-5 | 1.8e-4 / 3.1e-4 | 8.65e-7 |
      | 5.6563 | 5.65630 | -8.3e-5 (-8.45e-5) | 5.0e-5 / 1.5e-5 | 1.2e-4 / 1.9e-4 | 8.10e-7 |
      | 5.7063 | 5.70630 | -1.8e-5 (-1.93e-5) | 3.2e-5 / 1.1e-5 | 5.1e-5 / 6.5e-5 | 7.80e-7 |

      - The other six values (5.5363, 5.5663, 5.5713, 5.5813, 5.5863, 5.6063) follow the same monotone trend in every
        column.
      - Away from P the residual hardly changes with s:
        - 0.1-2: 2.2e-6 to 2.4e-6 (N_f);
        - 10-100: 6.7e-6 to 8.1e-6 (N_f) and 9.6e-6 to 1.2e-5 (N_v);
        - 100-1000: N_v 1.2e-5 to 1.3e-5;
        - 1000-R: N_v 5.7e-5 to 6.0e-5.
      - My identity c_l equals s to 1e-5 in every state, and my h(P) reproduces the exporter's to 1.2e-5.
      - My N_v maximum next to P agrees with the exporter's shell maximum to about 10 percent:
        - exporter 2.4e-5 / 2.3e-5 / 1.35e-5 / 8.7e-6 at 5.5763 / 5.5863 / 5.6563 / 5.7063;
        - mine 2.6e-5 / 2.5e-5 / 1.5e-5 / 1.1e-5.
      Verdict:
      - "near-P maximum flat over +-0.02" (03:02Z) and "near-P maximum and h(P) - 1 keep improving up to 5.71" (03:20Z):
        CONFIRMED in my evaluator. In this discretization every near-P diagnostic (max, J, h(P)) improves monotonically
        toward larger s over 5.52 to 5.71, by a factor 4 (max) and 11 (J).
      - "L2 minimum near 5.64" (03:20Z): not reproduced in my plane rms. That rms falls monotonically to 5.71. It is a
        different functional (my area weighting on the log grid), so this is not a refutation of their L2 statement.
      - Consequences:
        - The candidate's 5.5763 is not distinguished at this level.
        - These states are worse next to P than c6c segment 1 (G42: flux 2.2e-6, J 1.2e-6, |h(P) - 1| <= 1.9e-8) by a factor
          15 to 60 in the near-P flux maximum and 50 to 600 in J. They say nothing about whether the c6c level fixes c_l.
        - The direction of the trend is a property of this discretization's error at P, not evidence for a larger exponent.
          The lead's c6c state has |h(P) - 1| <= 1.9e-8 at c_l 5.5763609.
  (d) Correction to my evaluator (vresid.evaluate).
      - The default tail exponent was k_far = 1/c_l of a first pass without tails. The fixed point is k = 1/c_l of the
        final identity value.
      - Effect on the numerics exports (R 1e3 to 3e3), default against fixed point, N 3000:
        - c_l changes by up to 1.1e-4 (lsq R 1000: 5.29238 against 5.29227);
        - h(P) - 1 changes by up to 4.4e-4 (lsq R 1000: -8.2e-5 against -5.2e-4);
        - the near-P maximum changes by up to a factor 2.2 (s = 5.7063: N_f 7.0e-5 against 3.2e-5);
        - N_v at 10-100 changes by a factor 9 (about 1.0e-4 against 1.1e-5).
      - Under the default, the m(s) J(0.01) had an interior minimum (3.7e-4, 2.0e-4, 2.3e-4, 3.7e-4 at 5.5163, 5.5763,
        5.6563, 5.7063), and h(P) - 1 crossed 0 between 5.6563 and 5.7063. Both are artifacts of the inconsistent tail.
        With the fixed point my c_l and h(P) reproduce the exporter's, so the tables above use it.
      - New option {"k_self": true}:
        - available through the vcand cfg, the 6th argument of vaudit, and scratch/gen_audit_cfg.sh with env VAUDIT_CFG;
        - it iterates k = 3/(1 + c) six times;
        - backups: code/vresid_pre_kself.py, vcand_pre_kself.py, vaudit_pre_kfar.py;
        - the default is unchanged so that earlier logs reproduce.
      - Effect on the lead's candidates:
        - R 7.652e6: c6b segment 1 rerun with k_self agrees with G42 to one unit in the last printed digit:
          - flux 2-10 4.642e-6 (unchanged);
          - N_v 1.374e-6 -> 1.373e-6;
          - J(0.01) 3.289e-6 -> 3.288e-6;
          - c_l changes by 5e-11.
        - R 7.652e4: c6b rerun gives:
          - far-field N_v 4.35e-6 -> 3.64e-6;
          - 2-10 flux 5.338e-6 -> 5.224e-6;
          - J(0.01) 1.106e-5 -> 9.27e-6;
          - h(P) - 1 +1.57e-6 -> +1.23e-6;
          - c_l 5.57636367 -> 5.57636358.
          So the G42 domain effect at R 7.652e4 is partly this inconsistency and partly the domain error of G28 (b).
        - R 7.652e5: not rerun; the effect lies between the two above. G42 quotes R >= 7.652e5 values, and those stand.
      - Numerics LM state of G16/G24 (R 3000, runs/numchk2/g16S_vaudit.log), rerun with k_self:
        - c_l 5.5786399 (exporter 5.5786423; G16 had 5.5786587);
        - h(P) 1.000206 (G16: 1.000279);
        - band maxima change by at most 26 percent: |X-P| < 0.5 1.26e-4 -> 9.3e-5 N_f; 2-10 3.8e-4 -> 4.1e-4; 10-100
          1.3e-3 and 100-1000 3.2e-3 (N_f) unchanged.
        The G16 and G24 verdicts stand. Their c_l and h(P) digits carry evaluator errors of 1.6e-5 and 7.3e-5.
  (e) Consequence for the team: the c_l statement needs a fixed-c test at the c6c level.
      - Requested test:
        - a nonlinear re-solve, not only the linear tangent, at fixed c_l = 5.60 and 5.65 (or 5.70) on the 302 or 375 basis;
        - compare the between-node near-P max, J and h(P) with c6c.
      - If a fixed-c fit 0.02 to 0.1 away reaches the c6c level, c_l is not determined at the YES standard, and it must be
        quoted with that interval.
      - Until then:
        - c_l = 5.5763609 is where the lead's family has its residual;
        - its uniqueness at the 1e-6 level is untested;
        - at the 1e-4 level (numerics discretization) it is refuted by (a) and (c).
  (e, addendum) Lead NOTES 03:36Z item 5 plans the pilot: free fits from the c6b tangent shapes at c_l offsets +-3e-3
      (244 basis, after about 06:00Z), and c6e on the 375 basis after the 302 tangent.
      - The pilot tests pinning at the 3e-3 scale only. The numerics valley (a), (c) is at the 2e-2 to 1e-1 scale, and
        its near-P diagnostics prefer the larger-c_l side. So a pilot that returns from +-3e-3 does not answer (c).
      - Please add one fixed-c (or free-from-offset) run at c_l = 5.60 (offset +2.4e-2) on the 302 or 375 basis. If its
        near-P max, J and h(P) stay at the c6c level, c_l is not pinned at the 1e-6 standard.
      - Item 7 (i) of the same note (the numerics fits at s near 5.5763 have h(P) - 1 about 1e4 times the lead's) agrees
        with my numbers: -1.9e-4 in my evaluator at s 5.5763, against -1.9e-8 on c6c (G42).

### G46. FINAL_REPORT (mtime 03:36:36Z) and notes/final_sec4_draft.md (03:36:26Z) against the 02:49Z texts of G44. Recorded 2026-10-18T03:48Z
  Method: diff against lead/notes/FINAL_REPORT_backup_0337.md and final_sec4_draft_backup_0337.md (the 02:49Z
  texts audited in G44); copies of the new texts in scratch/FINAL_REPORT_lead_0336.md, scratch/final_sec4_draft_lead_0336.md.
  Changes and checks:
  (a) Line 96, "without the 1/T decay of the transport term": the G44 wording note, applied. CONFIRMED.
  (b) New timeline item "03:17 verifier audit of the trials with 244 and 302 radial functions":
      - 302 basis: flux maximum 2.3e-6 for 2 <= r <= 100 (G42: 2.227e-6 at 2-10 and |X-P| < 0.5, 2.292e-6 at 10-100);
        N_v maximum 1.4e-6 (G42: 1.409e-6, at 1000 <= r <= R); h(P) - 1 of order 1e-8 (G42: +8.5e-9 at N 16875, -1.9e-8
        at N 22500);
      - "three resolutions" (G42: N 11250, 16875, 22500);
      - the knot reading confirmed for the stem component and refuted for the near-P maximum as a whole, with the
        maximum in a strip next to the x-axis at the edge of the angular space;
      - "neither trial meets the residual standard".
      CONFIRMED against G42.
  (c) New timeline item "03:17 verifier audit of the lead's B_3 estimator":
      - increments grow by a factor about 3 per doubling (G43: 3.0 to 3.1);
      - "non-integrable remainder" (G43: delta (x* - x)^(beta - 2));
      - original form converged to 5e-4 (G43: 0.29855 to 0.29809 over n 20 to 640, 4.6e-4);
      - agreement with my estimator and B_3 about 0.30 on the three latest bases;
      - the unconverged values withdrawn.
      CONFIRMED against G43.
  (d) Section 4 draft: B_3 placeholders now cite only the original form and my estimator:
      - lead 0.3014 / 0.2991 / 0.2980 and mine 0.3006 / 0.3002, 0.2989 / 0.3004, 0.2983 / 0.2989 (G42 table, G43);
      - older values are marked for recheck; the ibp end piece is not quoted.
      CONFIRMED.
  Requirement for the final text (from G45; not yet due, since the c_l item is a placeholder):
  - The c_l paragraph must state the result of the fixed-c test at the level of the final basis (G45 (e)), or state
    that uniqueness of c_l at that level is untested.
  - It must also state that in the numerics discretization (near-P level 3e-5 to 1.3e-4), fixed-c_l fits over 5.52 to
    5.71 are equally good or better (G45 (c)).
  The existing condition (six-digit c_l only with the reproducibility statement, G41 (d)) stands.
  Verdict: the 03:36Z texts CONFIRMED.

### G47. c6c segment 1 plus eps times the numerics-lane c_l direction: what a c_l offset costs at the 302 level; audit of the lead's fixed-c reading rule (NOTES_FOR_TEAM 04:00Z). Recorded 2026-10-18T04:34Z
  Method:
  - Field: my generator applied to lead/work/c6/c6c_seg1_shape.npz (r0 7.652e-4, R 7.652e6, N 16875, q 384,
    M 479), plus eps times the direction v of numerics/runs/valley_N256M64R3000_direction.npz (delta_b_per_unit_cl),
    transplanted by scratch/dir_on_shape.py:
    - inside the numerics R = 3000: barycentric interpolation on their Radau grid (map read from
      fields_valley_N256M64R3000_S0.npz), cos(2 k theta) series on their midpoint angles, delta_rho = r^3 cos^2 sin w delta_b.
      Checked against the imported valley fields: 1.6e-14;
    - beyond 3000: their disk closure (r/R)^k rho(R, theta), k = 1/c_l, linearized in c_l. Checked against a finite
      difference of the closure: 9e-6.
  - Each field is evaluated between nodes with code/vaudit.py (driver scratch/dir_c6c.sh, table scratch/tab_dir.py;
    logs runs/dirc6c/e<eps>_N16875.log). v is one fixed direction, not re-optimized.
  - This is not the lead's basis: c6c + eps v is a field-level sum, so the numbers bound what a c_l offset costs among
    fields. They do not bound the 302-basis curve m(c).
  (a) Results. "near-P" is the flux maximum for |X - P| < 0.5; J is the characteristic defect at |X - P| = 0.03 and 0.01;
      bands are in r; ratios are to eps = 0.

      | eps | c_l (identity) | h(P) - 1 | near-P flux (ratio) | 10-100 | 100-1000 | J(0.03) | J(0.01) (ratio) |
      |---|---|---|---|---|---|---|---|
      | -1e-2 | 5.5663609 | -1.32e-4 | 6.96e-5 (30.5) | 2.47e-5 | 1.43e-6 | 3.94e-4 | 5.21e-4 (417) |
      | -3e-3 | 5.5733609 | -1.93e-5 | 1.10e-5 (4.82) | 2.55e-6 | 3.58e-7 | 5.05e-5 | 6.90e-5 (55) |
      | -1e-3 | 5.5753609 | -4.47e-6 | 3.26e-6 (1.43) | 2.39e-6 | 2.61e-7 | 1.03e-5 | 1.45e-5 (11.6) |
      | -1e-4 | 5.5762609 | -3.52e-7 | 2.220e-6 (0.97) | 2.322e-6 | 2.48e-7 | 1.20e-6 | 1.20e-6 (0.96) |
      | 0 | 5.5763609 | +8.5e-9 | 2.283e-6 (1) | 2.316e-6 | 2.49e-7 | 1.15e-6 | 1.25e-6 (1) |
      | +1e-4 | 5.5764609 | +3.50e-7 | 2.342e-6 (1.03) | 2.309e-6 | 2.49e-7 | 1.76e-6 | 2.18e-6 (1.74) |
      | +1e-3 | 5.5773609 | +2.55e-6 | 2.45e-6 (1.07) | 2.255e-6 | 2.57e-7 | 5.02e-6 | 7.59e-6 (6.1) |
      | +2e-3 | 5.5783609 | +3.15e-6 | 3.83e-6 (1.68) | 2.235e-6 | 2.89e-7 | 6.10e-6 | 9.31e-6 (7.4) |
      | +3e-3 | 5.5793609 | +1.82e-6 | 6.69e-6 (2.93) | 2.211e-6 | 3.45e-7 | 1.14e-5 | 1.14e-5 (9.1) |
      | +3.63e-3 | 5.5799909 | -1.3e-8 | 8.98e-6 (3.93) | 2.86e-6 | 3.91e-7 | 1.75e-5 | 1.75e-5 (14) |
      | +4.5e-3 | 5.5808609 | -3.81e-6 | 1.28e-5 (5.62) | 4.42e-6 | 4.71e-7 | 3.28e-5 | 3.62e-5 (29) |
      | +6e-3 | 5.5823609 | -1.38e-5 | 2.12e-5 (9.27) | 7.91e-6 | 6.48e-7 | 7.27e-5 | 8.55e-5 (68) |
      | +1e-2 | 5.5863609 | -6.17e-5 | 5.37e-5 (23.5) | 2.23e-5 | 1.37e-6 | 2.49e-4 | 3.08e-4 (246) |

      In the 0.1 <= r <= 2 band the maximum moves only from 2.34e-7 to 1.76e-7 (eps -3e-3 to +6e-3). x* moves
      linearly, at 0.568 per unit eps.
  (b) Checks:
      - My identity c_l moves by exactly eps (to the 7 decimals printed, relative 1e-5 at eps = 1e-2). This CONFIRMS the
        numerics lane's normalization of v (dc_l = 1 per unit), in my inverse at R 7.652e6.
      - h(P) - 1 = 8.5e-9 + 3.511e-3 eps - 0.969 eps^2 (least squares on eps = 0, +-1e-4, +-1e-3; the two pairs alone
        give the same coefficients to 4 digits). The other eight values deviate from the law by at most 3e-8 for
        |eps| <= 6e-3 and by 1.5e-7 (0.2 percent, an odd term of about 0.14 eps^3) at |eps| = 1e-2. The curvature agrees
        with the numerics valley value -1.0 (G45 (a)).
      - h(P) = 1 holds at eps = -2.4e-6 and at eps = +3.626e-3 (from the measured -1.33e-8 at 3.63e-3 and the slope
        there). The maximum of h(P) - 1 along v is 3.2e-6, at eps = 1.81e-3.
  (c) Far field: an artifact of my extension of v. With eps != 0 the N_v maximum over r > 1000 sits at r 3006, just
      outside the numerics R. It is linear in eps, at 0.081 to 0.0875 per unit eps: 8.75e-6 at 1e-4, 8.2e-5 at 1e-3,
      8.2e-4 at 1e-2. The c6c value is 1.41e-6.
      - scratch/kink_check.py measures r d_r delta_rho / delta_rho on both sides of R = 3000 at five angles. It jumps by
        5e-4 to 2.7e-2 (theta = 1.2: -1.5265 inside, -1.4991 outside), so the transplanted direction is only C^0 there.
      - Beyond R, v is not defined by the export. My closure does not solve the linearized far-field equation.
      The far-field maximum therefore measures my extension, not the softness of c_l. It is left out of (d) and (e). A
      consistent far-field extension of v was not built.
  (d) Reading:
      - At the c6c level, for r <= 1000 and in J, offsets of 1e-4 along v cannot be told apart from c6c, which is not
        re-optimized:
        - eps = -1e-4: near-P maximum 0.97 of c6c, J(0.01) 0.96, J(0.03) 1.04, the bands within 0.5 percent;
        - only h(P) - 1 (-3.5e-7) separates the two, and it is below the 1e-6 standard.
      - Therefore the residual at the c6c level does not fix c_l to better than about 1e-4. This bound comes from one
        direction and holds for r <= 1000 only, given (c). It is a lower bound on the c_l uncertainty at this level,
        not an error bar. It agrees with the lead's c6b tangent at LSQR iteration 2500 (tan_driver.log 04:33Z), where
        dcl* = +1.95e-4 lowers the linearized objective by only 0.07 percent (m_lin_min 1.8523e-5 vs m0 1.8536e-5).
      - J and h(P) are the sensitive diagnostics. At +1e-4, J(0.01) is 1.74 times larger. At +-1e-3 the near-P maximum
        is 1.07 / 1.43 times larger and J is 6 / 12 times larger.
      - Along v, the factor 2 in the near-P maximum is crossed between +2e-3 and +3e-3 and between -1e-3 and -3e-3. At
        1e-2 the factors are 23 and 30. No re-optimization was done, so these are upper bounds on the cost of these
        offsets: they bound how bad the offsets must be, not how bad they are.
      - h(P) = 1 alone does not fix c_l along v: it holds again 3.63e-3 away, where the near-P maximum is 3.9 times
        larger and J 14 times larger.
  (e) The lead's reading rule (NOTES_FOR_TEAM 04:00Z item 4; fixed-c_l fit at 5.60, c6b 244 basis and c6c 302 basis).
      - It was stated before the result, it has three outcomes (not determined / excluded / inconclusive), and it
        includes J. CONFIRMED as a procedure, with four corrections:
      - (e1) h(P) - 1 "within 30 percent" is ill-posed. On c6c segment 1, h(P) - 1 is at my evaluator's resolution:
        +8.5e-9 at N 16875 and -1.9e-8 at N 22500, so even its sign is not resolved. Along v, eps = -1e-4 moves it
        by a factor 40 while nothing else moves by more than 4 percent. Read h(P) in absolute terms, for example
        |h(P) - 1| <= 1e-6 (the standard), on my evaluator at N 16875 and 22500.
      - (e2) "Excluded at that level" for 5.60 excludes that one point at the 302 level, not the open interval
        between. Without a curve m(c) there is no bound |c_l - 5.5763| < 2.4e-2. FINAL_REPORT may then state only
        that c_l = 5.60 is excluded at that level.
      - (e3) The free fit used for comparison must have had the same budget on the same basis and fit grid, or the
        fixed-c fit must have flattened, as the rule requires for the exclusion branch. For the 302 test the
        comparison shape is c6c segment 1. I will audit both shapes between nodes with the same configs (R 7.652e6;
        N 16875 and 22500), and the rule is read on those numbers.
      - (e4) The test is at the 302 floor (near-P 2.3e-6), not at the 1e-6 standard. The rule says "at that level";
        FINAL_REPORT must say so too.
  Verdict:
  - The normalization of v and the quadratic h(P) law: CONFIRMED.
  - The size of the c_l offset that the residual at the c6c level cannot detect is at least about 1e-4 (one direction,
    r <= 1000; OPEN for r > 1000, see (c)).
  - Six-digit c_l values are not determined by the residual at the 302 level. Any c_l uncertainty quoted from the 302
    or later bases must be at least 1e-4, unless a later basis shows otherwise.
  - The reading rule: CONFIRMED with (e1) to (e4).

### G48. c6d segment 1 (375 radial functions, m <= 100) between nodes; the G42 (c) prediction; lead numbers of NOTES_FOR_TEAM 04:39Z item 1. Recorded 2026-10-18T04:56Z
  Method:
  - scratch/seg_audit.sh on lead/work/c6/c6d_seg1_shape.npz (mtime 04:32:14Z), tag c6dS1:
    - knot check;
    - my generator and vaudit at N 9000 / R 7.652e4, N 10125 / R 7.652e5, N 11250 / R 7.652e6 and N 16875 q512 M639 /
      R 7.652e6;
    - extra_checks and the residual map (N 11250);
  - plus N 22500 at R 7.652e6 (G42 (a)) and scratch/ang_split.py.
  - Logs runs/audit/c6dS1_*. c6c segment 1 (G42) at the same configs for comparison.
  (a) Knots: 384, interior knots simple. Minimum spacing 6.1e-4, the same as c6c, so the knots next to P are unchanged.
      Identity c_l 5.5763622 at every R >= 7.652e5 (lead 5.57636217; c6c 5.5763609). c_l from h(P) = 1 at fixed rho:
      5.576362133, 3.7e-8 below the identity.
  (b) Between nodes, R 7.652e6, values for c6d (c6c in brackets):

      | quantity | N 11250 | N 16875 q512 | N 22500 |
      |---|---|---|---|
      | h(P) - 1 | +5.5e-7 (+2.7e-7) | +7.4e-8 (+8.5e-9) | -2.0e-8 (-1.9e-8) |
      | flux max 2 <= r <= 10 = \|X-P\| < 0.5 | 2.424e-6 (2.227e-6) | 2.409e-6 (2.261e-6) | 2.444e-6 (2.285e-6) |
      | flux max 10 <= r <= 100 | 7.54e-7 (2.292e-6) | 9.49e-7 (2.335e-6) | 8.03e-7 (2.323e-6) |
      | N_v max 2 <= r <= 10 | 6.78e-7 (8.25e-7) | 6.75e-7 (8.38e-7) | 6.84e-7 (8.32e-7) |
      | N_v max 1000 <= r <= R | 1.456e-6 (1.409e-6) | 1.456e-6 (1.409e-6) | 1.456e-6 (1.409e-6) |
      | flux max 0.1-2 / 100-1000 / 1000-R | 2.17 / 2.48 / 2.63 e-7 | 2.22 / 2.52 / 2.63 e-7 | 2.17 / 2.48 / 2.63 e-7 |
      | J spread at \|X-P\| = 0.03 / 0.01 | 1.365 / 1.254 e-6 (1.127 / 1.200) | 1.465 / 1.432 e-6 (1.154 / 1.247) | 1.478 / 1.458 e-6 (1.157 / 1.252) |

      - h(P) - 1 at N 11250 and 16875 is evaluation error, as on c6c (G42 (a)); the N 22500 value -2.0e-8 is the one to
        quote.
      - The 2-10 maximum is at r 8.30, theta 0.016 (x 8.29, y 0.14): the near-axis strip left of P.
      - The 10-100 maximum moved from r 10.06, theta 0.67 (c6c) to r 10.13, theta 1.568, next to the y-axis. The N 16875
        q512 grid samples closer to the axis, which explains its larger value.
      - The far N_v maximum is at r 2.0e4, theta 1.06.
      - At R 7.652e5 the band maxima agree with R 7.652e6 to 1 percent (2-10 flux 2.440e-6). At R 7.652e4 my inverse has
        its known domain error (h(P) - 1 2.2e-6, J 1e-5, far N_v 4.4e-6; G28 (b)).
      - B_3: my estimator 0.2967 to 0.2972. The orig form in my evaluator gives 0.2897 to 0.2979, with wide intervals;
        the lead's orig median is 0.2972 [0.2935, 0.2997].
  (c) Residual map (N 11250, window 6 <= r <= 14, theta <= 1.6). Region maxima, c6c in brackets:
      - strip theta <= 0.1: 2.39e-6 (2.17e-6) for 6 <= r <= 8.2 and 2.42e-6 (2.23e-6) for 8.2 <= r <= 9.4;
      - stem ring 8.2 <= r <= 9.4, 0.1 <= theta <= 0.5: 1.53e-6 (1.37e-6), with n < 195 part 1.28e-6 (1.02e-6) and
        n >= 195 part 1.27e-6 (1.23e-6);
      - 8.2-9.4 with theta >= 0.5, 9.4-9.7, 9.7-11 and 11-14: 9.3e-7, 9.4e-7, 9.7e-7 (2.29e-6), 4.3e-7. All four maxima
        are at theta 1.568, next to the y-axis.
      - The n < 195 / n >= 195 split is ill-conditioned in regions that reach an axis: the parts are 1e-5 to 4e-4 and
        cancel, as on c6c. Only the stem-ring split is read.
  (d) The G42 (c) prediction, recorded before the result: c6d leaves the near-axis strip near 2e-6 and the far-field
      N_v near 1.4e-6. Result: 2.4e-6 (up 7 to 9 percent) and 1.456e-6 (up 3 percent). CONFIRMED.
  (e) Lead numbers (04:39Z item 1; scans 32768 x 640), against mine:
      - agree: 2-10 flux 2.43e-6 (mine 2.41e-6 to 2.44e-6), N4 6.8e-7 (6.75e-7 to 6.84e-7), 0.1-2 band 2.3e-7
        (2.17e-7 to 2.22e-7), r > 100 2.5e-7 (2.48e-7 to 2.63e-7), h(P) - 1 -1.3e-8 (-2.0e-8 at N 22500), c_l, x*
        8.600842;
      - 10-100 band 7.3e-7: mine is 7.5e-7 at N 11250, 8.0e-7 at N 22500 and 9.5e-7 at N 16875 q512 (next to the axis).
        The fall factor is 3.0 / 2.9 / 2.5 in mine, against 3.3 in the lead's numbers.
      - "leaves the near-P maximum and J where they were": CONFIRMED for the near-P maximum (+7 to 9 percent). In my
        J spread at |X - P| = 0.03 and 0.01, J rose by 15 to 28 percent at N 16875 and 22500 (by 21 and 4 percent at
        N 11250), and the lead's own J spread rose by a factor 2
        (5.3e-7 to 1.1e-6). So J did not fall, but it did not stay where it was either. Wording note: say "did not fall".
  Verdict:
  - c6d segment 1 is the best shape in the band 9.7 <= r <= 100 (8.0e-7) and in N_v for 2 <= r <= 10 (6.8e-7). It is
    not better near P or in the far field.
  - Its global flux maximum is the near-axis strip, 2.44e-6 at N 22500, against 2.32e-6 for c6c. Its global N_v maximum
    is 1.456e-6, against 1.409e-6. Not YES-level.
  - The remaining limits on c6d are the angular band edge (strip and far field, m <= 100) and the stem ring 1.5e-6. c6f
    (angular enrichment) tests the first.

### G49. The c6b soft-tangent shapes (244 basis, final tangent at LSQR iteration 2500) between nodes: c_l is not determined to 1e-3 at the 244 level. Recorded 2026-10-18T04:56Z
  Method:
  - scratch/tan_audit.sh tan_c6b: the 8 shapes lead/work/c6/tan_c6b_tan<dc>_shape.npz (mtime 04:33:15Z to
    04:33:25Z), dc = +-1e-4, +-3e-4, +-1e-3, +-3e-3, each c6b segment 1 plus dc times the lead's fixed-c tangent.
  - My generator and vaudit at N 11250, R 7.652e6, q384, M479 (logs runs/audit/tan_c6b<dc>_N11250_q384_R7.652e6.log,
    table runs/audit/tan_c6b_tan_table.txt). Base: c6bS1 at the same config (G42).
  - The lead's objective of the same shapes (fit grid, linear tangent model / nonlinear) is taken from NOTES_FOR_TEAM
    04:39Z item 3, not recomputed.
  (a) Ratios to c6b segment 1 at N 11250. Base values: global flux max = 2-10 max 4.642e-6 (stem ring, r 8.86,
      theta 0.33); |X-P| < 0.5 3.248e-6; 10-100 3.196e-6; N_v max 1.374e-6; J(0.03) / J(0.01) 3.086e-6 / 3.289e-6;
      h(P) - 1 -5.5e-8.

      | dc | c_l (identity) | global flux max | \|X-P\| < 0.5 | 10-100 | N_v max | J(0.03) | J(0.01) | h(P) - 1 | lead objective (nonlinear) |
      |---|---|---|---|---|---|---|---|---|---|
      | -3e-3 | 5.5733632 | 1.11 | 0.72 | 1.25 | 1.19 | 0.78 | 0.94 | +6.8e-7 | 1.42 |
      | -1e-3 | 5.5753632 | 0.99 | 0.85 | 1.06 | 1.02 | 0.79 | 0.76 | +3.4e-8 | 1.029 |
      | -3e-4 | 5.5760632 | 1.00 | 0.96 | 1.02 | 1.00 | 0.90 | 0.90 | -4.5e-8 | 1.004 (linear) |
      | -1e-4 | 5.5762632 | 1.00 | 0.99 | 1.01 | 1.00 | 0.97 | 0.97 | -5.3e-8 | 1.001 (linear) |
      | +1e-4 | 5.5764632 | 1.00 | 1.01 | 0.99 | 1.00 | 1.04 | 1.04 | -5.5e-8 | 0.9995 (linear) |
      | +3e-4 | 5.5766632 | 0.99 | 1.04 | 0.98 | 1.00 | 1.11 | 1.11 | -5.1e-8 | 0.9996 (linear) |
      | +1e-3 | 5.5773632 | 1.07 | 1.15 | 0.96 | 1.03 | 1.45 | 1.46 | +1.2e-8 | 1.015 |
      | +3e-3 | 5.5793632 | 1.36 | 1.64 | 0.93 | 1.31 | 2.90 | 3.04 | +6.2e-7 | 1.40 |

      (The lead lists values for +-1e-4 and +-3e-4 without saying whether they are linear or nonlinear; they are marked
      "linear" here as an assumption. At +-1e-3 and +-3e-3 both are given and the nonlinear value is used.)
  (b) Checks:
      - The identity c_l of each shape is c6b's 5.5763632 plus dc, to the 7 printed decimals: the tangent's c_l
        normalization is CONFIRMED.
      - x* moves 0.77 per unit dc.
      - h(P) - 1 stays below 7e-7 on the whole range, because the tangent fit includes the h(P) row.
      - The far N_v maximum stays at 1.33e-6 to 1.43e-6.
  (c) Reading:
      - At dc = -1e-3 (c_l 5.5753632) every between-node maximum is within 0.76 to 1.06 of c6b's, |h(P) - 1| = 3.4e-8,
        and the lead's objective rises 2.9 percent. By the lead's 04:00Z rule with G47 (e1), c_l is therefore not
        determined to 1e-3 at the 244 level on the lower side.
      - On the upper side, +3e-4 is inside every 30 percent band. +1e-3 fails only J, at a factor 1.46.
      - These are tangent shapes, not nonlinear fixed-c fits. A fixed-c refit lowers the objective further, but its
        maxima must be measured.
      - The diagnostics prefer different directions:
        - the maximum next to P falls monotonically toward negative dc (0.72 at -3e-3);
        - J(0.01) is lowest near -1e-3 (0.76);
        - the global maximum is flat on [-1e-3, +3e-4];
        - the lead's linearized objective has its minimum at dc +1.95e-4, where it is lower by 0.07 percent;
        - the numerics lane's m(s) improves toward larger c_l (G45 (c)).
        No c_l in about [5.57536, 5.57666] is preferred by the residual at the 244 level.
      - Consistent with G47: at the 302 level an offset of 1e-4 along an unoptimized direction is already undetected.
        The 302 tangent (lead queue, run_tan302.sh) and the fixed-c fits at 5.60 decide the 302 level.
  (d) Consequence for FINAL_REPORT: the lead's sentence (04:39Z item 3) that the six-digit c_l is a reproducibility
      number of the solver path and not a determination is CONFIRMED. At the 244 level it is stronger: the fourth
      decimal is not determined. Unless the 302 tests narrow it, quote c_l = 5.576 with an uncertainty of at least 1e-3
      at the 244 level and at least 1e-4 at the 302 level (G47). Values with more digits may appear only as
      reproducibility numbers.
  Verdict:
  - c_l normalization of the tangent: CONFIRMED.
  - "c_l not stationary at the 2e-4 level on the 244 basis" (lead 04:39Z title): CONFIRMED in my evaluator, in the
    stronger form that the between-node maxima do not determine c_l to 1e-3 at that level.

### G50. SPEC v4.5 (mtime 04:01:42Z), section 8 item on c_l determinacy. Recorded 2026-10-18T04:57Z
  Method: diff against lead/notes/SPEC_backup_v44.md; copy in scratch/SPEC_lead_v45.md. The only changes are the
  version line, the new section 8 item and its change-log entry.
  Checks of the item:
  - "fits 3e-5 apart are equally good on the lead bases": true (G37, G41), but it now understates the softness. On the
    244 basis, tangent shapes 1e-3 apart are equally good in every between-node maximum (G49). On c6c, an unoptimized
    offset of 1e-4 is not detected (G47).
  - "in the numerics discretisation ... fixed-c_l fits over 5.52 to 5.71 are equally good or better": G45 (c). CONFIRMED.
  - Requirements (1) to (3): reproducibility sentence, nonlinear fixed-c test at offset >= 2e-2 on the quoted basis and
    grid read by the 04:00Z rule or "untested", numerics statement. These are the G45 (e) / G46 requirements.
    CONFIRMED.
  - "quoted as an interval containing the tested values" if the offset is not excluded: CONFIRMED. "Stable as an
    interval, not as a digit string": CONFIRMED.
  Amendments required:
  - (i) The rule must be read with G47 (e1) to (e4): h(P) in absolute terms; equal budget or flattened objective; state
    the level.
  - (ii) If the offset is excluded, that excludes one point. It gives no interval |c_l - 5.5763| < 2e-2 (G47 (e2)).
  - (iii) The measured lower bounds on the c_l uncertainty must be stated with any quoted c_l: at least 1e-3 at the 244
    level (G49) and at least 1e-4 at the 302 level (G47), until a test on the quoted basis narrows them.
  Verdict: SPEC v4.5 CONFIRMED with amendments (i) to (iii).

### G52. Numerics-lane (256,128) clustered fixed-c_l states (NOTES_FOR_LEAD 04:07Z, 04:12Z) in my evaluator, against the (256,64) states of G45 (c). Recorded 2026-10-18T05:06Z
  Method:
  - State files numerics/runs/mc_N256M128cl_s{5.5563, 5.5663, 5.5763, 5.5863, 5.5963}.npz, read as data by
    code/vnum_import3.py (N 3000, R 3000, cluster key from the file, node check 0, r(T(s)) check 5e-13).
  - vaudit N 3000, 1282 angles, Mmax 383, r_start 20, option k_self (G45 (d)).
  - Driver scratch/num_m128.sh; logs runs/numchk2/m128S_s*_vaudit.log; table from scratch/tab_numchk2.py and the
    "all" and "q above P" lines.
  - The (256,64) values are those of G45 (c) (runs/numchk2/mcS_s*_vaudit.log), at the same five s.
  (a) Table. Maxima of |R|/N_f / |R|/N_v unless marked; M128 first, M64 in brackets.

      | s | h(P) - 1 mine (exporter) | \|X-P\| < 0.5 | \|X-P\| < 2 | J(0.03) / J(0.01) | flux rms, all r |
      |---|---|---|---|---|---|
      | 5.5563 | +2.66e-5 (+2.0e-5) [-2.24e-4] | 3.7e-5 / 1.05e-5 [1.04e-4 / 2.9e-5] | 7.3e-5 / 2.1e-5 [1.04e-4 / 2.9e-5] | 1.4e-4 / 1.4e-4 [3.5e-4 / 5.6e-4] | 1.20e-6 [1.31e-6] |
      | 5.5663 | +5.71e-5 (+5.1e-5) [-2.09e-4] | 3.5e-5 / 9.9e-6 [1.01e-4 / 2.8e-5] | 6.8e-5 / 1.9e-5 [1.01e-4 / 2.8e-5] | 1.3e-4 / 1.9e-4 [3.2e-4 / 5.2e-4] | 1.13e-6 [1.25e-6] |
      | 5.5763 | +8.86e-5 (+8.1e-5) [-1.93e-4] | 4.2e-5 / 1.2e-5 [9.3e-5 / 2.6e-5] | 6.1e-5 / 1.8e-5 [9.3e-5 / 2.6e-5] | 1.5e-4 / 2.3e-4 [3.0e-4 / 4.8e-4] | 1.06e-6 [1.17e-6] |
      | 5.5863 | +1.157e-4 (+1.1e-4) [-1.77e-4] | 5.4e-5 / 1.6e-5 [8.6e-5 / 2.5e-5] | 6.1e-5 / 1.8e-5 [8.6e-5 / 2.5e-5] | 1.5e-4 / 2.6e-4 [2.7e-4 / 4.4e-4] | 1.00e-6 [1.10e-6] |
      | 5.5963 | +1.508e-4 (+1.4e-4) [-1.61e-4] | 6.7e-5 / 1.9e-5 [8.3e-5 / 2.4e-5] | 6.7e-5 / 1.9e-5 [8.3e-5 / 2.4e-5] | 1.6e-4 / 3.0e-4 [2.5e-4 / 3.9e-4] | 9.45e-7 [1.03e-6] |

      - In 0.1-2 the M128 states are 3 to 5 times lower than the M64 states: 4.8e-7 to 7.8e-7 (N_f), rising with s,
        against 2.2e-6 to 2.3e-6.
      - For r >= 10 the M128 states equal the M64 states to 15 percent and change little with s:
        - 10-100: 6.0e-6 to 7.2e-6 (N_f), 1.1e-5 to 1.2e-5 (N_v);
        - 100-1000: N_v 1.2e-5;
        - 1000-R: N_v 6.0e-5 at r 2883, next to R.
      - My identity c_l equals s to the 5 printed decimals in all five states, and x* equals the exporter's to 4
        decimals.
  (b) Checks of the 04:07Z and 04:12Z claims:
      - h(P) - 1: mine exceeds the exporter's by 6e-6 to 1.1e-5 in all five states (M64: by at most 1.2e-5, G45 (c)).
        "positive, growing with s; at (256,64) negative, shrinking with s": CONFIRMED.
      - "rms decreasing monotonically through the range": CONFIRMED for my flux rms (1.20e-6 to 9.45e-7, -21 percent;
        theirs -19 percent). My N_v rms falls by 1.5 percent only.
      - "near-P maximum flat at 1.6e-5": CONFIRMED for my N_v maximum in |X-P| < 2 (1.8e-5 to 2.1e-5, flat within 17
        percent). Not true for |X-P| < 0.5: the N_f maximum is 3.5e-5 at 5.5663 and 6.7e-5 at 5.5963 (factor 1.9), and N_v
        changes by the same factor. From 5.5763 on that maximum sits on the axis next to P (r 8.612, theta 0.0041). There
        the residual is the pointwise residual at P: the ratio q at y = 1e-3 above P equals h(P) - 1 to 2 digits in all
        five states.
      - Their shell rms in |X-P| < 0.5 rises by 17 percent over the range; my N_v rms there rises by 12 percent
        (3.9e-6 to 4.4e-6). CONFIRMED.
      - "the minimum does not move toward 5.5763": CONFIRMED for the L2 functional.
  (c) The near-P diagnostics reverse their preference between the two grids:
      - (256,64): every near-P diagnostic improves toward larger s (G45 (c)).
      - (256,128): h(P) - 1, the |X-P| < 0.5 maximum and J(0.01) improve toward smaller s:
        - J(0.01) rises from 1.4e-4 to 3.0e-4 (factor 2.1);
        - J(0.03) stays flat (1.3e-4 to 1.6e-4).
      - h(P) - 1 is linear in s on both grids. Over the five states (least squares, deviation below 3e-6):
        - (256,128): slope 3.07e-3 per unit s, zero at 5.548 (extrapolated 0.009 below the range);
        - (256,64): slope 1.59e-3, still -1.8e-5 at 5.7063 (G45 (c)), so its zero lies above 5.706.
        The zero moves by at least 0.16 between grids that differ only in the angular resolution.
      - At equal s = 5.5763, refining 64 to 128 angles:
        - lowers the |X-P| < 2 maximum from 9.3e-5 to 6.1e-5;
        - lowers J(0.01) from 4.8e-4 to 2.3e-4;
        - changes h(P) - 1 from -1.9e-4 to +8.9e-5;
        - lowers 0.1-2 by a factor 3.7 (2.29e-6 to 6.2e-7);
        - leaves the bands r >= 10 unchanged to 10 percent.
        The M128 states are still 15 to 30 times above c6c segment 1 in the |X-P| < 0.5 maximum (flux 2.28e-6, G42), and
        110 to 240 times above it in J(0.01) (1.25e-6).
      Verdict:
      - The statement of 04:25Z, that a residual level of 1e-5 to 5e-5 next to P does not discriminate c_l within +-0.05
        because the preferred side depends on the grid: CONFIRMED in my norms.
      - The preference reverses under angular refinement alone, and h(P) - 1 is a near-P measure, not only the L2
        functional. Over +-0.02 (M128) every near-P diagnostic changes by at most a factor 2.1.
      - G45 (c) said that the direction of the M64 trend is a property of that discretization's error at P, not evidence
        for a larger exponent. CONFIRMED by the reversal.
  (d) Note for the audit of the lead's fixed-c tests (fixc_c6b_560_*, fixc_c6c_560):
      - In both numerics grids the fixed-c re-solves leave h(P) - 1 linear in s, with slope 1.6e-3 to 3.1e-3 per unit
        c_l. Along the unoptimized v_cl on c6c the slope is 3.5e-3 (G47 (b)).
      - A re-solve at 5.60 that does not restore the condition at P would have |h(P) - 1| between 4e-5 and 8e-5. That
        point is excluded by G47 (e1).
      - So h(P) - 1 of those runs is the first number to read. Whether the 244 and 302 bases restore it is what the test
        decides; this note is not a prediction of the outcome.

### G53. Lead analysis 13.12 (mtime 04:43:26Z), NOTES_FOR_TEAM 04:47Z and 04:56Z, FINAL_REPORT timeline entries 03:45 and 04:34 (mtime 04:47:08Z). Recorded 2026-10-18T05:09Z
  Method: arithmetic on the lead's published numbers (NOTES 04:39Z item 3, 04:56Z item 2, 13.12 (a) to (c)), with my
  G47 and G49 tables. Copy of analysis.md in scratch/analysis_lead_0443.md. Nothing was recomputed on the lead's fit grid.
  (a) 13.12 facts.
      - (a) "sigma_244 <= 3.58e-3, an upper bound": CONFIRMED as logic. Every LSQR iterate is a feasible shape
        correction, so the minimum over the basis is at most the last value.
      - (b) "the linear model matches the nonlinear objective to 0.5 percent up to |d| = 1e-3": CONFIRMED (0.37
        percent on both sides). "To 20 percent at 3e-3": the ratios are 1.21 and 1.23, so "to 23 percent".
      - (c) "3.8 percent of f0 lies along r": CONFIRMED. sqrt(1 - 0.99929^2) = 0.0377, and dcl* sigma / m0 = 0.0379 at
        iteration 2500, so |r| = sigma is consistent.
      - (c) "dcl* grew roughly like 1/sigma": REFUTED for iterations 1500 to 2500. Over that range 1/sigma grows by a
        factor 1.8 and dcl* by a factor 15. The fraction of f0 along r/|r| (dcl* sigma / m0) grows linearly with no
        sign of levelling: 0.45, 1.24, 2.14, 3.02, 3.79 percent at 1500, 1750, 2000, 2250, 2500. On the 20480 x 640
        warm continuation (04:56Z item 2, 150 iterations) dcl* sigma is constant to 4 percent (5.4e-7 to 5.6e-7), so the
        claim holds there, over a 3 percent change of sigma [withdrawn in G55: over 300 iterations dcl* sigma rises 10
        percent from iteration 50, so the claim fails on that grid too]. Consequence: dcl* is not converged on the 10240 x 480
        tangent. Its iteration-2500 value is not a lower bound or an estimate of the limit.
      - (d) the location fractions of |s|^2 are the lead's tool output. They are not rechecked here. They are
        consistent with the 04:56Z repeat on 20480 x 640.
  (b) 13.12 (e), the linear reading.
      - sqrt(3) m0 / sigma = 8.97e-3 and sqrt(0.21) m0 / sigma = 2.37e-3. These are lower bounds, so they should be
        written ">= 8.9e-3" and ">= 2.3e-3" (the text has 9.0e-3 and 2.4e-3, rounded up).
      - The statement is about the linear model only. The measured nonlinear values of (b) give more:
        - the nonlinear excess m_nl^2 - m_lin^2 per d^4 is 2.67 and 2.63 at -1e-3 and +1e-3, and 2.74 and 2.79 at -3e-3
          and +3e-3;
        - so along the tangent shapes, m_nl^2 = m_lin^2 + |q|^2 d^4 with |q|^2 = 2.76 to 5 percent between the two
          offsets [parenthesis withdrawn in G55: rho = e^H is not polynomial in d, the d^4 law is a measured fit];
        - with this law the tangent objective reaches 2 m0 at |d| = 4.1e-3 and 1.1 m0 at 1.8e-3, not at 9.0e-3 and 2.4e-3;
        - at the fixed-c offset 2.4e-2 the tangent shape has m = 52 m0 (the linear model gives 4.7 m0).
      - A fixed-c fit at c_fit + d has the tangent shape as a feasible point. So its objective is at most m_nl(d) if it
        is solved at least as well as that point. Then the factor 2 in the fixed-c objective lies at |d| >= 4.1e-3 (if
        sigma_244 = 3.58e-3), and there is no upper bound.
      - "On the 244 basis the L2 objective resolves c_l only at the 1e-2 level": not supported as stated. Along the
        tangent the factor 2 is at 4.1e-3. The fixed-c objective can only be lower, so the true scale lies between
        4.1e-3 and an unknown upper value.
      - My between-node maxima on the same shapes (G49) do not reach a factor 2 at +-3e-3 except J(0.01) at +3e-3
        (3.04). This agrees with 4.1e-3 for the objective.
      - "The six-digit agreement over 215 to 375 is a property of the solver path": CONFIRMED (G37, G47, G49).
  (c) 13.12 (f), the two readings, is incomplete. It omits a third case:
      - sigma tends to 0 under iteration and refinement (non-closed range), but the quadratic term pins c_l. The
        residual is exactly quadratic in rho. If the second-order part that a fixed-c fit cannot absorb stays of
        order |q_res|, the fixed-c objective doubles at about (sqrt(3) m0 / |q_res|)^(1/2). With the unabsorbed
        |q| = 1.66 above, that is 4.4e-3.
      - So "the fit norm does not determine c_l at all" in the second reading holds only if the second-order term is
        also absorbed.
      - At 2.4e-2 the tangent objective is dominated by the quadratic term, by a factor 11 in m. So the fixed-c fit at 5.60
        measures how much of that term the basis absorbs, and its result does not separate readings 1 and 2 (both are
        about sigma). The 302 tangent (sigma_302 against sigma_244, both at a converged or equal budget) separates
        them.
      - On the 244 tangent the linear term dominates the objective excess for |d| <= 1e-3 (82 percent at 1e-3), but
        the objective changes there by only a few percent. The quadratic term dominates from 3e-3 on (66 percent at
        3e-3, 96 percent at 1e-2). So the planned fixed-c points at +-3e-3 and +-1e-2 (04:47Z item 2), like 5.60,
        measure how much of the second-order term the basis absorbs.
  (d) 13.12 (g), the reporting rule (no more than three decimals without the fixed-c result; six digits only with the
      13.11 (d) disclaimer): CONFIRMED. G50 (iii) still applies: the lower bounds 1e-3 (244, G49) and 1e-4 (302, G47)
      must be stated with the three-decimal value.
  (e) NOTES_FOR_TEAM 04:47Z item 1, the reading rule as corrected: it now contains (e1) (|h(P) - 1| <= 1e-6 absolute,
      on my evaluator at N 16875 and 22500), (e2) (single point), (e3) (flattened: under 2 percent over the last 1000
      LSQR iterations; same basis and fit grid) and (e4) (the level is stated). CONFIRMED.
      - Item 2 (fixed-c points at +-3e-3 and +-1e-2 on the 302 basis): agreed. With (b), +-3e-3 is near the factor-1.4
        point of the 244 tangent and +-1e-2 beyond its factor 2. Together they bracket the scale.
      - For the 302 basis G51 gives the analogous field-level numbers.
  (f) NOTES_FOR_TEAM 04:56Z item 1 (G48 accepted; "J did not fall"; my spread rose 15 to 28 percent at N 16875 and
      22500): CONFIRMED against G48. At N 11250 the rise is 4 to 21 percent; the lead quotes the two finer resolutions,
      which is correct.
  (g) FINAL_REPORT timeline:
      - 03:45 entry: CONFIRMED against G45 (c). G52 strengthens it: the preferred side reverses on the (256,128) grid.
        A later entry may say so.
      - 04:34 entry: one error. "Only h(P) - 1, at 3.5e-7, and the characteristic defect J change" is true for +1e-4,
        where J(0.01) is 1.74 times larger, but not for -1e-4, where J is within 4 percent. "Not detected" holds only
        for -1e-4. Suggested wording: "an offset of -1e-4 is not detected by the residual for r <= 1000 or by J (within
        4 percent); only h(P) - 1 (3.5e-7) moves. At +1e-4 the characteristic defect J is 1.74 times larger." The rest
        of the entry (uncertainty at least 1e-4; factor 2 between 1e-3 and 3e-3; upper bounds since not re-optimized):
        CONFIRMED.
  (h) notes/final_sec4_draft.md (mtime 04:43:52Z; diff against the 03:36Z copy: lines 67 to 71 only; copy in
      scratch/final_sec4_draft_lead_0443.md). FINAL_REPORT (04:47:08Z) differs from 03:36Z only by the two timeline
      entries of (g); copy in scratch/FINAL_REPORT_lead_0447.md.
      - "the least cost per unit c_l is at most 3.58e-3 (LSQR iterate, still falling)": CONFIRMED ((a)).
      - "the linearised objective stays below twice the fit's objective for c_l offsets up to at least 9e-3": write
        8.9e-3 ((b)). The sentence must add that along the tangent shapes the measured nonlinear objective doubles at
        about 4.1e-3. Otherwise the reader takes 9e-3 for the scale of the objective.
      - "six-digit agreement ... is a solver-path property": CONFIRMED.
      - "c_l is quoted to three decimals with this statement": CONFIRMED. The lower bounds of G50 (iii) must be added:
        at least 1e-3 at the 244 level (G49) and, from G51, at the 302 level.
  Verdict:
  - 13.12 facts (a), (b), (d) and the first part of (c): CONFIRMED.
  - (c) "dcl* like 1/sigma": REFUTED on 10240 x 480 for iterations 1500 to 2500.
  - (e): CONFIRMED for the linear model, with lower bounds to be rounded down. The conclusion "resolves c_l only at the
    1e-2 level" is REFUTED as a statement about the objective. The measured nonlinear terms give 4.1e-3 along the
    tangent, and the fixed-c scale is not bounded from above by this section.
  - (f): incomplete (third case).
  - (g): CONFIRMED.
  - Rule 04:47Z: CONFIRMED.
  - FINAL_REPORT 04:34 entry: one wording error, to be corrected.
  - Section 4 draft lines 67 to 71: CONFIRMED with two amendments (nonlinear doubling at 4.1e-3; lower bounds stated).

### G51. c6c segment 1 plus eps times the lead's 244 soft tangent (an optimized c_l direction) between nodes: at the 302 level c_l is not determined to 1e-3 on the lower side. Recorded 2026-10-18T05:16Z
  Method:
  - Direction t = (rho[tan_c6b+1e-3] - rho[tan_c6b-1e-3]) / 2e-3: central difference of the lead's tangent shapes
    (work/c6/tan_c6b_tan+-1e-3_shape.npz, copies in runs/gen4), each put on my grid by my generator (r0 7.652e-4,
    R 7.652e6, N 16875, q 384).
    - The lead's tangent is linear in dc in coefficient space, but rho = L^3 rr^3 cos^2 sin e^H is not linear in the
      coefficients. So t is the derivative of the tangent family at dc = 0 up to a relative O(h^2) error, and
      c6c + eps t is a linear sum of fields, not a shape of either basis.
  - Field c6c + eps t: scratch/tan_on_c6c.py. It asserts identical grids and drops c and c_l so that both come from my
    identity.
  - Evaluation: vaudit, M 479, r_start 20, default tail (R 7.652e6, G45 (d)). Driver scratch/tan_c6c.sh; logs
    runs/tanc6c/e<eps>_N16875.log; table scratch/tab_dir.py.
  - Like G47 this is a field-level sum, not a 302-basis shape and not re-optimized. Unlike the numerics direction of
    G47, t is optimized on the 244 basis and fit grid. It includes the h(P) row and has a consistent tail, so the far
    field is not an artifact here.
  - eps = 0 reproduces c6c segment 1 of G47 to all printed digits.
  (a) Table. Ratios to eps = 0 in brackets. Base values: |X-P| < 0.5 flux max 2.283e-6 (strip, r 8.435, theta 0.0164);
      global flux max 2.316e-6 (10-100 band); global N_v max 1.409e-6; J(0.03) / J(0.01) 1.15e-6 / 1.25e-6; plane flux
      rms 5.56e-8; h(P) - 1 +8.5e-9.

      | eps | c_l (identity) | h(P) - 1 | \|X-P\| < 0.5 | global flux max | 0.1-2 | 10-100 | N_v max | J(0.03) / J(0.01) | flux rms |
      |---|---|---|---|---|---|---|---|---|---|
      | -3e-3 | 5.5733609 | +3.5e-7 | 2.162e-6 (0.95) | 3.94e-6 (1.70) | 3.28e-7 (1.45) | 3.63e-6 (1.57) | 1.50e-6 (1.06) | 3.13e-6 / 3.13e-6 (2.72 / 2.50) | 1.27e-7 (2.28) |
      | -1e-3 | 5.5753609 | +3.6e-9 | 1.710e-6 (0.75) | 2.55e-6 (1.10) | 2.62e-7 (1.16) | 2.55e-6 (1.10) | 1.35e-6 (0.96) | 1.15e-6 / 1.15e-6 (1.00 / 0.92) | 5.60e-8 (1.01) |
      | -3e-4 | 5.5760609 | -5.2e-9 | 2.084e-6 (0.91) | 2.36e-6 (1.02) | 2.37e-7 (1.05) | 2.36e-6 (1.02) | 1.40e-6 (0.99) | 1.13e-6 / 1.13e-6 (0.98 / 0.90) | 5.49e-8 (0.99) |
      | 0 | 5.5763609 | +8.5e-9 | 2.283e-6 | 2.32e-6 | 2.26e-7 | 2.32e-6 | 1.41e-6 | 1.15e-6 / 1.25e-6 | 5.56e-8 |
      | +3e-4 | 5.5766609 | +3.3e-8 | 2.490e-6 (1.09) | 2.49e-6 (1.08) | 2.15e-7 (0.95) | 2.26e-6 (0.97) | 1.41e-6 (1.00) | 1.49e-6 / 1.62e-6 (1.30 / 1.30) | 5.69e-8 (1.02) |
      | +1e-3 | 5.5773609 | +1.29e-7 | 3.002e-6 (1.31) | 3.00e-6 (1.30) | 1.89e-7 (0.84) | 2.15e-6 (0.93) | 1.38e-6 (0.98) | 2.52e-6 / 2.79e-6 (2.19 / 2.23) | 6.25e-8 (1.12) |

      - 100-1000 band 2.33e-7 to 2.73e-7; far N_v 1.33e-6 to 1.41e-6 at r 2.4e4 to 3.2e4.
      - At -3e-3 the global maximum moves to the stem ring (r 8.74, theta 0.34). At -1e-3 and -3e-4 the 2-10 maximum
        is at r 9.95, theta 0.67, outside |X-P| < 0.5. Otherwise it is the axis strip of G42.
      - B_3 (orig form) 0.2968 to 0.2986.
  (b) Checks:
      - My identity c_l is c6c's plus eps to the 7 printed decimals: the tangent's normalization carries over to c6c.
      - x* moves 0.77 per unit eps, as on c6b (G49).
      - |h(P) - 1| <= 3.5e-7 on the whole range, below the 1e-6 standard.
  (c) Reading, by the 04:47Z rule with (e1) to (e4), at field level:
      - eps = -1e-3 (c_l 5.5753609), against c6c:
        - every quantity is within 30 percent: near-P maximum 0.75, global maximum 1.10, J 1.00 / 0.92, N_v 0.96,
          plane rms 1.01, |h(P) - 1| = 3.6e-9;
        - the field is better than c6c next to P.
        So at the 302 level the residual does not determine c_l to 1e-3 on the lower side. This raises the G47 lower
        bound (1e-4, from an unoptimized direction) to 1e-3 at the 302 level, the same as G49 at the 244 level.
      - eps = +3e-4 is inside every band, J at the edge (1.30).
      - eps = +1e-3 is inconclusive: J 2.2, near-P maximum 1.31.
      - eps = -3e-3 is inconclusive: the near-P maximum is 0.95, but the global maximum is 1.70, 10-100 is 1.57 and J is
        2.5 to 2.7.
      - No point is excluded: the near-P maximum stays below 2 at all six offsets.
      - Same pattern as G49 on the 244 basis:
        - the near-P maximum falls toward negative eps (244: 0.85 at -1e-3; 302: 0.75);
        - the upper side costs more in J (244: 1.46 at +1e-3; 302: 2.23).
        The lead's linearized L2 step on 244 points the other way (dcl* +1.95e-4), and the numerics M64 / M128 curves
        point in either direction (G52). The diagnostics disagree on the preferred side by more than 1e-3.
      - Field level only: t + c6c need not lie in the 302 basis, and nothing was re-optimized. A fixed-c fit on the
        302 basis at 5.5753609 would decide whether the 302 basis itself reaches this field's level. Since this field
        exists at the c6c level, the statement "the residual at the c6c level does not determine c_l to 1e-3" holds
        for fields, which is the relevant class for the YES standard.
  Verdict:
  - A c_l offset of -1e-3 is not detected at the c6c (302) level by any between-node diagnostic (field-level, along
    the lead's 244 tangent; N 16875). CONFIRMED.
  - The lower bound on the c_l uncertainty at the 302 level is therefore at least 1e-3, replacing 1e-4 in G47 and
    G50 (iii), pending the N 22500 repeat and the offsets -1.5e-3, -2e-3, +6e-4 (running).
  (d) Addendum, recorded 2026-10-18T05:24Z (PIDs 2949686, 2949840; same method; logs runs/tanc6c/e<eps>_N16875.log and
      e<eps>_N22500.log):

      | eps | N | c_l | h(P) - 1 | \|X-P\| < 0.5 | global flux max | 0.1-2 | 10-100 | N_v max | J(0.03) / J(0.01) | flux rms |
      |---|---|---|---|---|---|---|---|---|---|---|
      | -2e-3 | 16875 | 5.5743609 | +1.16e-7 | 1.574e-6 (0.69) | 3.01e-6 (1.30) | 2.96e-7 (1.31) | 3.01e-6 (1.30) | 1.24e-6 (0.88) | 1.48e-6 / 1.48e-6 (1.29 / 1.18) | 7.55e-8 (1.36) |
      | -1.5e-3 | 16875 | 5.5748609 | +4.5e-8 | 1.594e-6 (0.70) | 2.76e-6 (1.19) | 2.79e-7 (1.23) | 2.76e-6 (1.19) | 1.29e-6 (0.91) | 1.13e-6 / 1.13e-6 (0.98 / 0.90) | 6.21e-8 (1.12) |
      | +6e-4 | 16875 | 5.5769609 | +6.7e-8 | 2.705e-6 (1.18) | 2.71e-6 (1.17) | 2.04e-7 (0.90) | 2.18e-6 (0.94) | 1.40e-6 (0.99) | 1.89e-6 / 2.07e-6 (1.64 / 1.66) | 5.86e-8 (1.05) |
      | 0 | 22500 | 5.5763609 | -1.86e-8 | 2.285e-6 | 2.32e-6 | 2.26e-7 | 2.32e-6 | 1.41e-6 | 1.16e-6 / 1.25e-6 | 5.56e-8 |
      | -1e-3 | 22500 | 5.5753609 | -1.90e-8 | 1.733e-6 (0.76) | 2.55e-6 (1.10) | 2.62e-7 (1.16) | 2.55e-6 (1.10) | 1.35e-6 (0.96) | 1.15e-6 / 1.15e-6 (0.99 / 0.92) | 5.60e-8 (1.01) |

      - N 22500 reproduces eps = 0 (G42: c6c at N 22500) and eps = -1e-3 (every ratio within 0.01 of N 16875). At
        N 22500, h(P) - 1 is -1.9e-8 at both offsets, so the h(P) difference at N 16875 is evaluation error.
      - The global maximum at -1.5e-3 and -2e-3 is the 10-100 band (r 10.2), next to the unrefined radial band of G42.
  (e) Reading of the addendum (04:47Z rule, field level):
      - Inside every 30 percent band: eps in [-1.5e-3, +3e-4], that is c_l in [5.57486, 5.57666]. In this range
        |h(P) - 1| <= 4.5e-8. Along this direction the residual at the c6c level leaves an interval of width 1.8e-3
        undetermined.
      - -2e-3 is at the edge: the global maximum, 0.1-2 and J(0.03) are at 1.29 to 1.31, and the flux rms is 1.36.
      - +6e-4 and +1e-3 are inconclusive. Only J exceeds the band (1.65, 2.2).
      - No offset is excluded.
      Verdict (replaces the pending clause above): CONFIRMED at N 16875 and 22500. The lower bound on the c_l
      uncertainty at the 302 level is 1e-3 (lower side 1.5e-3, upper side 3e-4), replacing 1e-4 of G47 and G50 (iii).

### G54. Fixed-c_l fit at 5.60 on the 244 basis (lead work/c6/run_fixc.sh, started 05:11:41Z): start and first check (intermediate, no reading). Recorded 2026-10-18T05:28Z
  Method:
  - The lead's logs: fixc_driver.log, fixc_c6b_560_make.log, fixc_c6b_560.log.
  - My audit of the working shape after the first check: work/c6/fixc_c6b_560_shape.npz, mtime 05:23:28Z, 250 LSQR
    iterations at fixed c_l. Copied to runs/gen4/fixc/fixc_c6b_560_it250_shape.npz; run_configuration says long_solve
    LSQR fixed c_l, 10240 x 480.
  - Audit: code/gen_audit.sh at N 11250, R 7.652e6, q 384, M 479 (log
    runs/audit/fixc560i250_N11250_q384_R7.652e6.log), against c6bS1 at the same config (G42).
  (a) The start (make_fixc_start.py: z0 + dk (e0 + v), dk = 1/5.60 - 1/c0 = -7.569e-4, i.e. dc = +2.364e-2 along the
      final c6b tangent):
      - lead objective 9.271e-4 = 50.0 m0;
      - the naive start (k only) has 0.159 = 8600 m0;
      - start h(P) - 1 = +4.29e-5.
      - Check of G53 (b): the law m^2 = m0^2 + sigma^2 d^2 + 2.76 d^4, fitted at |d| <= 3e-3, predicts 9.33e-4 = 50.3 m0 at
        d = 2.364e-2, within 0.6 percent of the measured start. The linear model alone gives 4.7 m0. So at the 5.60 offset
        the start objective is the quadratic term, as G53 (b), (c) said. The nonlinear tangent law extrapolates by a factor 8
        in d.
  (b) After 250 LSQR iterations at fixed c_l = 5.60:
      - lead objective 9.514e-5 = 5.13 m0, lead h(P) - 1 = -4.0e-9 (the solver restored the P condition within the
        first 250 iterations).
      - Between nodes (mine, N 11250), ratios to c6bS1:

      | quantity | fixc 5.60, it 250 | c6bS1 | ratio |
      |---|---|---|---|
      | c_l (identity) | 5.6000000 | 5.5763632 | |
      | h(P) - 1 | -1.3e-7 | -5.5e-8 | |
      | \|X-P\| < 0.5 flux max | 2.626e-5 | 3.248e-6 | 8.1 |
      | global flux max | 2.626e-5 | 4.642e-6 | 5.7 |
      | 10-100 flux max | 6.55e-6 | 3.20e-6 | 2.0 |
      | N_v max, all (fixc: in 1000-R; c6bS1: in 2-10) | 9.80e-6 | 1.37e-6 | 7.1 |
      | 1000-R flux max / N_v max | 4.27e-6 / 9.80e-6 | 3.20e-7 / 1.37e-6 | 13 / 7.2 |
      | J(0.03) / J(0.01) | 4.85e-5 / 4.95e-5 | 3.09e-6 / 3.29e-6 | 15.7 / 15.0 |
      | flux rms, all | 5.50e-7 | 6.67e-8 | 8.2 |
      | B_3 orig | 0.3057 | 0.3004 | |

  (c) Status:
      - This is the state after 250 of about 4000 planned iterations (3 h at about 680 s per 250). It has not flattened,
        so the 04:47Z rule gives no reading yet.
      - The same-budget free control run_ctrl244.sh (queued next, G47 (e3)) and the fixed-c end shape
        (fixc_c6b_560_fixed_shape.npz, expected about 08:15Z) decide.
      - Two facts can already be stated:
        - |h(P) - 1| is restored to the 1e-7 level at fixed c_l = 5.60, so h(P) will not decide this test (G52 (d) asked
          for it to be read first: it is at 1.3e-7 here, inside the 1e-6 standard);
        - the cost so far sits next to P (factor 8.1), in J (15) and in the far band 1000-R (flux 13, N_v 7.2); the
          10-100 band carries less (factor 2.0). The source moved from x* 8.6008 to 8.6191.

### G55. Lead FINAL_REPORT (mtime 05:28:24Z) timeline entries 04:34 (corrected) to 05:16; section 4 draft (05:28:34Z) lines 68 to 77; analysis 13.13 (05:29:44Z). Correction to my G53 (a), (b). Recorded 2026-10-18T05:35Z
  Method:
  - Diffs against the lead's backups notes/FINAL_REPORT_backup_0528.md, final_sec4_draft_backup_0528.md and
    analysis_backup_0529.md. Copies in scratch/FINAL_REPORT_lead_0528.md, final_sec4_draft_lead_0528.md and
    analysis_lead_0529.md.
  - Checked against G48, G49, G51, G52, G53, against work/c6/tan_c6b_g20480x640_dwr.jsonl (final, 300 iterations) and
    fixc_c6b_560_make.log, and by arithmetic. Nothing was recomputed on the lead's grid.
  (a) FINAL_REPORT timeline.
      - 04:34 entry, corrected: it is the G53 (g) wording. CONFIRMED.
      - 04:56 entry, c6d. Against G48:
        - 10-100 band lowered by a factor 2.9 to 8.0e-7 (N 22500: 2.323e-6 to 8.03e-7);
        - near-P maximum 2.44e-6, up 7 to 9 percent;
        - far N_v 1.46e-6;
        - J did not fall.
        CONFIRMED.
      - 04:56 entry, 244 tangent shapes. Against G49 (a), (c): at -1e-3 the ratios are 0.76 to 1.06 and h(P) - 1 is
        3.4e-8; the sides are those of G49 (c). CONFIRMED.
      - 05:06 entry, numerics (256,128): CONFIRMED with one precision.
        - Three near-P diagnostics prefer smaller c_l: h(P) - 1, the maximum within 0.5 of P and J(0.01).
        - The maximum within 2 of P is lowest at s = 5.5763 to 5.5863, and J(0.03) is flat to 20 percent (G52 (a), (c)).
        - Suggested: "three of its near-P diagnostics (h(P) - 1, the maximum within 0.5 of P, J at 0.01) now prefer
          smaller c_l".
        - "Confirms that the preferred side at that residual level is a discretization property": CONFIRMED for that
          discretization (G52 verdict).
      - 05:09 entry, G53: CONFIRMED. "It is not converged" now also holds on the warm continuation ((c) below).
      - 05:16 entry (addendum 05:24), G51: CONFIRMED with one wording amendment. "At two between-node resolutions" holds
        only for offsets 0 and -1e-3. The other offsets, including the end points -1.5e-3 and +3e-4, are at N 16875
        only. Suggested: "(N 16875; offsets 0 and -1e-3 repeated at N 22500)".
  (b) Section 4 draft, lines 68 to 77.
      - The two amendments of G53 (h) are in: 8.9e-3, the nonlinear doubling at 4.1e-3, and the lower bounds 1e-3 at
        244 and 302 (lower side 1.5e-3). The preferred-side sentence matches G49 (c) and G51 (c). CONFIRMED.
      - "audited by the verifier" for 13.13: parts (a) to (c), (e) are audited here. Part (d) is marked unaudited by the
        lead, and the draft does not use it. Correct.
      - "a refitted fixed-c objective can only be lower": true of the minimum over the basis at fixed c_l. A computed
        fit is lower only if it is solved at least as well as the tangent shape, which 13.13 (a) says.
        Suggested: "the minimum of a fixed-c fit can only be lower".
  (c) Analysis 13.13 (a).
      - dcl* up by 15, 1/sigma up by 1.8, the fraction 0.45 to 3.79 percent: CONFIRMED (G53 (a)).
      - Warm continuation 20480 x 640, iterations 0 to 300 (jsonl), CONFIRMED:
        - sigma 3.531e-3 to 3.294e-3 (-6.7 percent);
        - dcl* sigma 5.615e-7 to 5.921e-7 (+5.5 percent; the text says 6).
      - Further, from iteration 50 the product rises monotonically: 5.39, 5.44, 5.58, 5.67, 5.82, 5.92e-7 at 50 to 300.
        That is +10 percent while sigma falls 5.7 percent. So dcl* grows faster than 1/sigma on the warm continuation as
        well, and it is not converged there either.
        - Correction to G53 (a): its sentence "the claim holds there" used 150 iterations and is withdrawn. Over 300
          iterations the claim fails on both grids.
      - ">= 8.9e-3", ">= 2.3e-3": CONFIRMED.
      - "|q|^2 = 2.67 to 2.79": the four values of G53 (b) are 2.67, 2.63, 2.74, 2.79 (at -1e-3, +1e-3, -3e-3, +3e-3), so
        write 2.63 to 2.79.
      - Tangent objective 1.02, 1.13, 1.41, 1.97 m0 at 1e-3, 2e-3, 3e-3, 4.1e-3: CONFIRMED. The law with |q|^2 = 2.76 and
        sigma = 3.58e-3 gives 1.022, 1.130, 1.409, 1.974. The values at 2e-3 and 4.1e-3 come from the fitted law; the
        shapes exist at 1e-3 and 3e-3 only. Say so.
      - Feasible-start argument and "nothing bounds it from above": CONFIRMED (G53 (b)).
      - Wording note on G53 (b): CORRECT, and it corrects my report.
        - The parenthesis in G53 (b), "(R is quadratic in rho, so the shape family is exactly quadratic in d)", is
          wrong and is withdrawn.
        - Along a coefficient-space tangent, rho = L^3 rr^3 cos^2 sin e^H is analytic in d, not polynomial. So R(d) is
          not quadratic and the d^4 law is a measured fit at |d| = 1e-3 and 3e-3.
        - R is quadratic in rho, as G53 (c) says, but that does not make the d-family quadratic. The third case of G53 (c)
          stands, with "second-order part" read as the d^2 coefficient of R(d).
      - Check at the fixc start: d = 2.3637e-2 and m_lin = 8.66e-5 = 4.67 m0, CONFIRMED.
        - With |q|^2 = 2.74 the law gives 9.29e-4; the start has 9.271e-4 (G54 (a): 50.3 against 50.0 m0 with 2.76).
          The value at 2.4e-2 corresponds to |q|^2 = 2.73.
        - "Holds to 0.2 percent" overstates the precision. Over 2.63 to 2.79 the law gives 9.10e-4 to 9.37e-4 (-1.8 to
          +1.1 percent). Write "within the 2 percent set by the spread of |q|^2".
        - The agreement holds out to 8 times the fitted offsets, so the terms above d^4 are small up to 2.4e-2 along
          this tangent.
        - Factor 11 in m: 9.271e-4 / 8.66e-5 = 10.7. CONFIRMED.
      - Third case: CONFIRMED as G53 (c).
        - Amendment to my G53 (c) and to 13.13 (a) "the 302 tangent at a budget equal to the 244 one does": at an equal
          budget, sigma_302 against sigma_244 separates readings 1 and 2 only if both are close to their limits.
        - sigma_244 still falls about 1 percent per 50 iterations on both grids. So sigma_302 < sigma_244 at equal
          budget is evidence for reading 2 only together with run_tancont244.sh (does sigma_244 level off).
  (d) Analysis 13.13 (b) and (c).
      - (b) intervals: CONFIRMED with two corrections.
        - The bound |h(P) - 1| <= 4.5e-8 is the 302 one. The 244 shapes inside the bands have up to 5.5e-8 (N 11250,
          G49 (a)). Both are far below 1e-6.
        - "No offset excluded (near-P maximum below 2 times throughout)": CONFIRMED (244: at most 1.64, at +3e-3; 302: at
          most 1.31, at +1e-3). Under (e3) no tangent shape or field-level sum can be excluded anyway, since none is a
          flattened fit. The near-P criterion is the content.
      - (c) pattern: the numbers are CONFIRMED:
        - near-P maximum 0.85 / 0.72 (244) and 0.75 / 0.70 / 0.69 (302);
        - 1.30 at -2e-3 is the 10-100 band at r 10.2;
        - J 1.46 (244) and 2.2 (302) at +1e-3;
        - dcl* +1.8e-4 is the final warm value, 1.7976e-4.
        Two wording points:
        - On 244 the global maximum is at the stem ring at every offset (base r 8.86, theta 0.33; -3e-3 r 9.02,
          theta 0.33). It does not move there; it rises (1.11 at -3e-3).
        - "The width of the undetermined interval did not shrink from 244 to 302": NOT SUPPORTED as stated.
          - Both widths are lower bounds. On 244 it is [-1e-3, +3e-4], 1.3e-3, with -1.5e-3 and -2e-3 not tested. On 302
            it is [-1.5e-3, +3e-4], 1.8e-3, along a direction optimized on 244, not on 302.
          - Lower bounds cannot show that a width did not shrink.
          - Valid form: "the tested intervals are at least 1.3e-3 (244) and 1.8e-3 (302) wide; nothing shows a
            shrinkage".
  (e) Analysis 13.13 (d), marked unaudited by the lead; its factual premises:
      - "Lowers it by 25 to 30 percent": holds on 302 (25, 30, 31 percent at -1e-3, -1.5e-3, -2e-3). On 244 it is 15
        percent at -1e-3 and 28 percent at -3e-3.
      - "On 302 the region that rises is the 10-100 band, which the 375 basis removed": CONFIRMED (G51 (d), G48 (b)).
      - The hypothesis can be tested at field level now: c6d segment 1 + eps t with the same t as G51 (G56, running
        since 05:33Z).
      - "The coefficient-space transplant is exact since the c6c, c6d and c6f bases contain the 244 basis": OPEN.
        Knot containment for 302 is checked by run_fixc302.sh. For 375 and c6f I have not checked it.
  (f) Analysis 13.13 (e), reporting: CONFIRMED. It matches G50 (iii) and G51 (e).
  Verdict:
  - FINAL_REPORT entries 04:34 to 05:16: CONFIRMED, with two wording amendments (05:06: three of the near-P diagnostics;
    05:16: which offsets are at N 22500).
  - Section 4 lines 68 to 77: CONFIRMED (one qualifier suggested).
  - 13.13 (a) to (c), (e): CONFIRMED, with these corrections:
    - |q|^2 range 2.63 to 2.79;
    - "0.2 percent" should read "within 2 percent";
    - the h(P) bound on 244 is 5.5e-8;
    - "did not shrink" is not supported, since both widths are lower bounds.
  - 13.13 (d): unaudited reading. Its premises are correct; the test is running (G56).
  - My report:
    - G53 (a) "holds there" is withdrawn;
    - the G53 (b) parenthesis "exactly quadratic in d" is withdrawn;
    - G53 (c) "equal budget separates" is amended.

### G56. c6d segment 1 plus eps times the 244 soft tangent (field level, as G51): test of analysis 13.13 (d). On c6d the global maximum falls by 27 percent at c_l 1e-3 below the fit. Recorded 2026-10-18T05:53Z
  Method:
  - As G51, with base c6d segment 1 (runs/gen4/c6dS1_shape.npz = lead/work/c6/c6d_seg1_shape.npz, mtime 04:32:14Z)
    instead of c6c.
  - t is the same field-level central difference of tan_c6b+-1e-3.
  - Driver scratch/tan_on_base.sh, which is tan_c6c.sh with the base shape as an argument.
  - Logs runs/tan_c6dA, tan_c6dB (N 16875) and tan_c6dC (N 22500), each e<eps>_N<N>.log. vaudit q384, M 479, R 7.652e6.
  - Field-level sums, not 375-basis shapes, nothing re-optimized (G51 method notes apply).
  - eps = 0 reproduces G48 at N 22500 to every printed digit: 2.444e-6, h(P) - 1 -1.96e-8, J 1.478e-6 / 1.458e-6.
  (a) Table, N 16875. Ratios to eps = 0 in brackets.
      - Base values: global flux max 2.436e-6 (the axis strip, r 8.31, theta 0.016); 10-100 8.07e-7; 0.1-2 2.17e-7;
        N_v max 1.456e-6 (far field, r 2.0e4); J(0.03) / J(0.01) 1.46e-6 / 1.43e-6; plane flux rms 5.40e-8.
      - h(P) - 1 at N 16875 carries evaluation error on this family (G48 (b)); read it from N 22500 below.

      | eps | c_l (identity) | global flux max (where) | \|X-P\| < 0.5 | 10-100 | 0.1-2 | N_v max | J(0.03) / J(0.01) | flux rms |
      |---|---|---|---|---|---|---|---|---|
      | -3e-3 | 5.5733622 | 3.95e-6 (1.62, stem ring r 8.92 theta 0.29) | 1.88e-6 (0.77) | 1.96e-6 (2.43) | 3.18e-7 (1.47) | 1.35e-6 (0.93) | 3.00e-6 / 3.00e-6 (2.05 / 2.10) | 1.25e-7 (2.32) |
      | -2e-3 | 5.5743622 | 2.45e-6 (1.00, stem ring r 8.76 theta 0.30) | 1.55e-6 (0.64) | 1.13e-6 (1.40) | 2.86e-7 (1.32) | 1.25e-6 (0.86) | 1.54e-6 / 1.54e-6 (1.05 / 1.08) | 7.33e-8 (1.36) |
      | -1.5e-3 | 5.5748622 | 1.97e-6 (0.81, stem ring r 8.76 theta 0.30) | 1.66e-6 (0.68) | 9.21e-7 (1.14) | 2.69e-7 (1.24) | 1.34e-6 (0.92) | 1.19e-6 / 1.19e-6 (0.82 / 0.83) | 5.98e-8 (1.11) |
      | -1e-3 | 5.5753622 | 1.79e-6 (0.73, strip r 8.40 theta 0.016) | 1.79e-6 (0.73) | 8.32e-7 (1.03) | 2.52e-7 (1.16) | 1.40e-6 (0.96) | 9.91e-7 / 9.91e-7 (0.68 / 0.69) | 5.38e-8 (1.00) |
      | 0 | 5.5763622 | 2.44e-6 (strip) | 2.44e-6 | 8.07e-7 | 2.17e-7 | 1.46e-6 | 1.46e-6 / 1.43e-6 | 5.40e-8 |
      | +3e-4 | 5.5766622 | 2.64e-6 (1.08, strip) | 2.64e-6 (1.08) | 7.72e-7 (0.96) | 2.06e-7 (0.95) | 1.46e-6 (1.00) | 1.79e-6 / 1.77e-6 (1.23 / 1.24) | 5.54e-8 (1.03) |
      | +1e-3 | 5.5773622 | 3.14e-6 (1.29, strip) | 3.14e-6 (1.29) | 8.38e-7 (1.04) | 1.79e-7 (0.82) | 1.43e-6 (0.98) | 2.79e-6 / 2.86e-6 (1.91 / 2.00) | 6.14e-8 (1.14) |

      - h(P) - 1 at N 16875: +7.4e-8 (eps 0), +1.26e-7 (-1e-3), +1.97e-7 (-1.5e-3), +2.98e-7 (-2e-3), +5.93e-7 (-3e-3),
        +8.2e-8 (+3e-4), +1.41e-7 (+1e-3).
      - The far N_v maximum stays at r 2.0e4 to 3.4e4 and falls toward negative eps (1.25e-6 at -2e-3).
      - 100-1000 stays at 2.2e-7 to 2.7e-7.
  (b) N 22500 repeat (chain c6dC):
      - eps = 0: global 2.444e-6, h(P) - 1 -1.96e-8, 10-100 8.03e-7, J 1.48e-6 / 1.46e-6, N_v 1.456e-6, rms 5.40e-8.
      - eps = -1e-3: global 1.805e-6 (0.74, strip r 8.46, theta 0.016), h(P) - 1 +5.3e-8, 10-100 8.70e-7 (1.08), 0.1-2
        2.52e-7 (1.16), J 9.98e-7 / 9.98e-7 (0.67 / 0.68), N_v 1.398e-6 (0.96), rms 5.38e-8 (1.00).
      - So N 22500 reproduces N 16875 to 1 percent in the maxima, and to 5 percent in the 10-100 band.
      - eps = -1.5e-3 at N 22500: running; see (e).
  (c) Reading, 13.13 (d):
      - On c6d, moving c_l down along the 244 soft direction lowers the global flux maximum, since the strip next to P
        is the region that falls (0.73 at -1e-3, 0.64 at -2e-3). The region that rises on c6c, the 10-100 band, starts
        here at 8.1e-7 and reaches only 8.3e-7 to 8.7e-7 at -1e-3.
      - The global maximum (flux) over the offsets: 2.44 (0), 1.79 to 1.81 (-1e-3), 1.97 (-1.5e-3), 2.45 (-2e-3) e-6. Its
        minimum along this line lies between -1.5e-3 and -5e-4. There the maximum changes from the strip to the stem ring
        (r 8.76, theta 0.30).
      - J(0.01) is also lowest at -1e-3 (0.68), and so is the far N_v near there (0.96, falling further to 0.86 at -2e-3).
      - So the 13.13 (d) premise holds at field level on the 375 level:
        - the max-norm optimum in c_l along this direction is about 1e-3 below the L2-fit value 5.5763622;
        - at c_l = 5.5753622 the field c6d + (-1e-3) t is better than c6d in the global flux maximum (0.73), in J
          (0.68) and in the far N_v (0.96);
        - it is worse only in 10-100 (1.03 to 1.08) and 0.1-2 (1.16), both at least 2 times below the global maximum;
        - h(P) - 1 = +5.3e-8 at N 22500.
      - Field level, not a fit: whether the 375 basis itself reaches this field at fixed c_l = 5.5754 needs a fixed-c fit.
        The field's maxima are an existence statement for the trial class used in the YES standard (fields), not for
        the basis.
      - 1.8e-6 is not at the 1e-6 standard. It is the lowest global flux maximum measured so far on any field in my
        evaluator (c6c 2.32e-6, c6d 2.44e-6; G42, G48). J 1.0e-6 is the lowest J (c6c 1.25e-6).
  (d) Consequences:
      - The L2-fit c_l (5.57636) is not the max-norm optimum of the trial family at the 375 level, and the six-digit c_l
        of the L2 fits is not a determination (13.12 (e), G49, G51).
      - The tested values give these intervals at the 375 level along this direction (field level, N 16875):
        - inside every 30 percent band: eps -1e-3 and -1.5e-3, also +3e-4 (J 1.23, at the edge);
        - -2e-3 is at the edge (0.1-2 1.32, 10-100 1.40, rms 1.36);
        - +1e-3 is inconclusive (J 1.9 to 2.0);
        - -3e-3 is inconclusive (global 1.62, 10-100 2.43, J 2.05 to 2.10, rms 2.32);
        - no offset is excluded (near-P maximum below 2 at every offset).
      - Lower bound on the c_l uncertainty at the 375 level: 1.5e-3 below and 3e-4 above the fit value, the same as at
        302 (G51). The max-norm optimum lies inside, at about -1e-3.
  (e) Addendum 2026-10-18T05:54Z: eps = -1.5e-3 at N 22500:
      - global flux max 2.080e-6 (0.85; stem ring r 8.76, theta 0.30; 5.6 percent above its N 16875 value 1.970e-6);
      - |X-P| < 0.5 1.653e-6 (0.68), 10-100 9.20e-7 (1.15), J 1.19e-6 / 1.19e-6 (0.80 / 0.82), N_v 1.336e-6 (0.92);
      - h(P) - 1 +1.35e-7.
      So the minimum of the global maximum along this line is nearer -1e-3 than -1.5e-3 (0.74 against 0.85 at
      N 22500). Readings (c), (d) unchanged. The same test on c6f is running (chain c6fA on the c6f iteration-500
      working shape).
  Verdict:
  - 13.13 (d) premise "the max-norm (near-P) optimum in c_l of the trial family may lie 1e-3 to 2e-3 below the fitted
    5.57636": CONFIRMED at field level on the 375 level (c6d), along the 244 soft direction, at about -1e-3 (global flux
    maximum 0.73 to 0.74 at N 16875 and 22500).
  - Not a statement about the profile. Not YES-level (1.8e-6).

### G57. c6f working shape after 500 LSQR iterations of segment 1 (angular 150, 375 radial, 56632 columns), between nodes (intermediate). Recorded 2026-10-18T05:53Z
  Method:
  - Copy of lead/work/c6/c6f_shape.npz (mtime 05:42:30Z, history call 3, lead objective 7.983e-6, c_l
    5.576362236) in runs/gen4/c6fi500_shape.npz.
  - code/gen_audit.sh at N 11250 q384 M479 and N 16875 q512 M639, R 7.652e6 (logs
    runs/audit/c6fi500_N*_R7.652e6.log, .json). J = the char summary 'spread' entries at 0.03 / 0.01 (as in G42, G48).
    The log line "J spread, interior start angles" is a different quantity (start angles away from the axis).
  - Compared with c6d segment 1 (G48) at the same configs.
  (a) Values, N 11250 q384 / N 16875 q512 (c6d in brackets):

      | quantity | N 11250 q384 | N 16875 q512 |
      |---|---|---|
      | c_l (identity) | 5.5763622 | 5.5763622 |
      | h(P) - 1 | +2.9e-7 (+5.5e-7) | +4.8e-8 (+7.4e-8) |
      | global flux max = strip (r 8.28 to 8.36, theta 0.012 to 0.013) | 2.419e-6 (2.424e-6) | 2.403e-6 (2.409e-6) |
      | flux max 10-100 | 4.18e-7 (7.54e-7) | 4.41e-7 (9.49e-7) |
      | flux max 0.1-2 / 100-1000 / 1000-R | 1.47e-7 / 6.5e-8 / 2.20e-7 (2.17 / 2.48 / 2.63 e-7) | 1.54e-7 / 6.8e-8 / 2.21e-7 (2.22 / 2.52 / 2.63 e-7) |
      | N_v max 2-10 | 6.77e-7 (6.78e-7) | 6.71e-7 (6.75e-7) |
      | N_v max 1000-R (global N_v max) | 1.142e-6 (1.456e-6) | 1.143e-6 (1.456e-6) |
      | flux rms, all | 2.60e-8 (5.38e-8) | 2.61e-8 (5.40e-8) |
      | J(0.03) / J(0.01) | 3.00e-6 / 3.18e-6 (1.365 / 1.254 e-6) | 3.03e-6 / 3.26e-6 (1.465 / 1.432 e-6) |
      | J, interior start angles (0.01) | 4.96e-7 (9.28e-7) | 4.57e-7 (9.83e-7) |
      | B_3 (my estimator) | 0.2977 | 0.2982 |

  (b) Reading (intermediate shape; segment 1 ends about 06:22Z):
      - The angular step 100 to 150 lowers every band away from P:
        - 10-100 by 1.8 to 2.2;
        - 100-1000 by 3.7 to 3.8;
        - far N_v by 1.27 (to 1.14e-6);
        - plane rms by 2.1;
        - J from interior start angles by 1.9 to 2.2.
        It does not lower the axis strip left of P (2.40e-6 to 2.42e-6, unchanged to 1 percent), which is the global
        maximum.
      - J at 0.03 / 0.01 from all start angles rose by a factor 2.1 to 2.5 (2.20 / 2.54 at N 11250, 2.07 / 2.28 at N 16875). The interior part fell, so the rise comes
        from characteristics starting next to the axis, the same place as the strip.
      - The G48 hypothesis "the strip and the far field are angular band-edge (m <= 100) effects" is REFUTED for the strip
        at this iterate and supported for the far field (1.46e-6 to 1.14e-6). An unfinished segment can still change the
        strip; the segment end decides.
      - The lead objective fell by 2.3 (1.867e-5 to 7.98e-6) while the global maximum did not move. The L2 objective and
        the max norm are decoupled at this level: the max norm is held by the strip, and the strip moves with c_l (G56).
      - The q384 and q512 values agree to 1 to 5 percent except 10-100 (5 percent, next to the axis). The m <= 150 content
        is resolved by both.
  Verdict:
  - Intermediate, no reading by the rule.
  - c6f iteration 500 is better than c6d away from P and in L2. It is not better at the global flux maximum (the strip,
    2.4e-6) and it is worse in J at |X - P| = 0.03 / 0.01 (factor 2.1 to 2.5). Not YES-level.

### G58. The 244 soft direction at coefficient level on c6d (lead work/c8 transplants, analysis 13.14, NOTES_FOR_TEAM 05:52Z item 3) in my evaluator; exactness of the transplant; c6f iteration 500 plus eps t (field level). Recorded 2026-10-18T06:17Z
  Method:
  - The lead's shapes work/c8/trd_<d>_shape.npz (c6d segment 1 plus d t in coefficient space, t the 244 soft direction,
    not refitted) were copied to runs/gen4/trd and run through my generator and vaudit at N 16875, q384, M479
    (scratch/trd_chain.sh; logs runs/audit/trd<d>_N16875_q384_R7.652e6.log). Base: the same c6d file (md5 equal to
    lead work/c6/c6d_seg1_shape.npz), G56 row eps 0.
  - Exactness: my generator's fields of c6d, trd_-1e-3, trd_-3e-3 and tan_c6b+-1e-3 at N 3375, q96 (runs/trchk). I
    compared D_d = log(rho_trd(d) / rho_c6d) / d with D_t = log(rho_+ / rho_-) / (2h), h = 1e-3, over 1e-2 < r < 2e3,
    interior angles.
  - c6f: scratch/tan_on_base.sh on runs/gen4/c6fi500_shape.npz (tag c6fA), N 16875 q384, as G56.

  (a) Exactness of the transplant (G55 (e) OPEN item).
      - max |D_d - D_t| = 5.7e-5 (d = -1e-3) and 8.4e-5 (d = -3e-3) against max |D_t| = 0.30 (relative 1.9e-4 / 2.8e-4; rms
        relative 7e-5 / 3e-4). The largest difference is at the stem ring (r 8.9, theta 0.34). In 0.01 < r < 2 the difference is
        1.5e-6 to 1.7e-6 against max |D_t| 1.05e-2.
      - The remainder is O(h^2) in D_t plus the change of L along the line (L 7.65205, 7.65142, 7.65017 at d = 0, -1e-3,
        -3e-3), which makes rho_trd(d) not exactly rho_c6d e^(d D_t).
      - The c6d field and the midpoint of the c6b pair agree to 2.1e-6 in log rho over the same region.
      Verdict: the transplanted direction is the 244 soft direction as a function on the plane, to 3e-4 relative:
      CONFIRMED for the 375 basis. For c6f I have not checked it. The lead's argument (zero angular coefficients, c6f_make
      rho_rel_diff 0.0) is CONFIRMED as a premise. The fxf shapes are to be checked when they exist.

  (b) The coefficient line in my evaluator, N 16875. Ratios are to d = 0 (global 2.436e-6, J 1.46e-6 / 1.43e-6, 10-100
      8.07e-7, rms 5.40e-8). "obj" is the lead's objective at 20480 x 480 (trd_obj.jsonl), as a ratio to 1.887e-5.

      | d | global max (location) | abs(X-P) < 0.5 | J(0.03) / J(0.01) | 10-100 | rms | h(P) - 1 | obj |
      |---|---|---|---|---|---|---|---|
      | -3e-3 | 2.164e-6 (0.89; r 8.63 th 0.16) | 0.68 | 1.43 / 1.46 | 1.48 | 1.20 | +7.19e-7 | 1.45 |
      | -2e-3 | 1.774e-6 (0.73; r 8.63 th 0.16) | 0.64 | 0.74 / 0.76 | 1.03 | 1.02 | +3.42e-7 | 1.17 |
      | -1.5e-3 | 1.723e-6 (0.71; r 8.81 th 0.24) | 0.68 | 0.64 / 0.65 | 0.97 | 0.99 | +2.13e-7 | 1.09 |
      | -1e-3 | 1.792e-6 (0.74; strip r 8.28 th 0.016) | 0.74 | 0.68 / 0.69 | 0.94 | 0.98 | +1.24e-7 | 1.04 |
      | -5e-4 | 2.099e-6 (0.86; strip) | 0.86 | 0.69 / 0.71 | 0.95 | 0.99 | +7.27e-8 | 1.016 |
      | 0 | 2.436e-6 (strip r 8.31 th 0.016) | 1 | 1 / 1 | 1 | 1 | +7.40e-8 | 1 |
      | +5e-4 | 2.784e-6 (1.14; strip) | 1.14 | 1.38 / 1.41 | 1.01 | 1.06 | +8.70e-8 | 0.994 |
      | +1e-3 | 3.167e-6 (1.30; strip) | 1.30 | 1.89 / 1.99 | 0.91 | 1.11 | +1.52e-7 | 1.000 |

      - Lead's 13.14 table (scans at 32768 x 640) against mine:
        - 2-10 maximum agrees to 5.5 percent; theirs is the higher one at -1.5e-3 to -3e-3.
        - 10-100 agrees to 4 percent except at +5e-4 (13 percent) and at d = 0. Their d = 0 value is from a different
          scan grid (16384 x 640).
        - h(P) - 1 agrees to within 9e-8. Mine is higher throughout, which is the size of my N 16875 h(P) offset (G56:
          +7.4e-8 at N 16875, -2.0e-8 at N 22500 for d = 0).
        The 10-100 maximum sits at r 10.0 to 10.2, theta 1.561 to 1.5675, next to the y axis at the inner edge of the band.
        It moves non-monotonically by up to 10 percent between neighbouring offsets, so differences below 10 percent in
        that column are not significant. Verdict: the 13.14 table is CONFIRMED in my evaluator.
      - 13.14 (d) reading:
        - "max-norm optimum 1e-3 to 1.5e-3 below the L2 fit's c_l": CONFIRMED. Among the tested offsets the minimum of the
          global maximum is at -1.5e-3 (0.71), flat to 4 percent over -2e-3 to -1e-3; J has its minimum at -1.5e-3 (0.64).
        - "L2 optimum about 5e-4 above": CONFIRMED for the lead's objective. A parabola through d = 0, +5e-4, +1e-3 has
          its minimum at +5.0e-4. My area-weighted plane rms has its minimum near -1e-3 (0.98) instead, a different
          functional.
        - Both are minima along one fixed direction, not refitted.

  (c) Field level against coefficient level (correction to G56 (c)).
      - The two lines differ at second order. Relative difference in rho: 4.0e-8 at d = -1e-3 and 5.4e-7 at d = -3e-3,
        against estimates d^2 D_t^2 / 2 of 4.5e-8 and 4.1e-7. The base mismatch (c6d against c6b in the field-level
        tangent) is 3e-10 to 9e-10.
      - At -1e-3 the readings agree: global 1.788e-6 against 1.792e-6, J 9.91e-7 against 9.86e-7. Beyond that they do not:
        - -1.5e-3: global 1.970e-6 against 1.723e-6;
        - -2e-3: 2.445e-6 against 1.774e-6;
        - -3e-3: 3.949e-6 against 2.164e-6;
        - J: 1.19 / 1.54 / 3.00 e-6 against 0.94 / 1.08 / 2.09 e-6.
      - At the 1e-6 residual level, a relative density change of 5e-7 moves the global maximum by 1.8e-6. A field-level
        (linear in rho) line is a first-order statement, adequate for |d| <= 1e-3 only. It is not a line in the trial class.
      - Consequences:
        - G56 (c), offsets beyond 1e-3: superseded by the coefficient line. -2e-3 is inside the bands (obj 1.17, near-P
          0.64, J 0.74 / 0.76, h(P) - 1 3.4e-7). -3e-3 is outside unrefitted on obj (1.45) and J (1.43 / 1.46), with
          near-P 0.68: inconclusive, a refit decides.
        - Upper side: at +5e-4 J is outside the 30 percent band unrefitted (1.38 / 1.41) while near-P is 1.14 and obj
          0.99. At +1e-3 near-P is 1.30 and J 1.89 / 1.99. "Not determined" holds on the upper side only to +3e-4
          (G56, J 1.23 / 1.24). Between +5e-4 and +1e-3 it is inconclusive (unrefitted).
        - G51 (302, field level) readings at 1e-3 stand: the second-order difference there is 4e-8 relative, which is the
          case that agreed here. G47's "registered at offsets of a few 1e-3" refers to a linear (field-level) line. It is
          not a statement about the trial class beyond 1e-3.
      Verdict: lower bound on the c_l uncertainty at the 375 level, unrefitted: 2e-3 below, 3e-4 above. The interval is
      asymmetric: the lower side is the soft one.
      Addendum 2026-10-18T06:25Z: the exponential form of the field line does not repair it. On c6d, rho_c6d e^(d D_t) (scratch/tan_exp.py,
      runs/tanx_c6dX) gives:
      - at -3e-3: global 3.835e-6 (stem ring r 9.01 th 0.36), J 3.50e-6 / 4.09e-6, h(P) - 1 +9.1e-7;
      - at -2e-3: 2.388e-6, J 1.70e-6 / 1.73e-6.
      Against the transplant (2.164e-6, 1.774e-6) these are worse than the linear field line. Along the transplant L moves
      (dL / L = 8.2e-5 per 1e-3 of c_l), so log rho is not linear in d. The terms this omits are at most 2.5e-7 in log rho
      at -3e-3 ((a)), yet they change the global maximum by 1.7e-6 at the stem ring. At the 1e-6 level only the
      coefficient-level transplant is a trial-class line. Every line gives an upper bound on the fixed-c_l cost, by
      exhibiting a density with that c_l, so the best line (the transplant) sets the bound above. The exp-line chain on
      c6f was stopped after one point (-3e-3: global 3.68e-6, J 5.2e-6 / 6.3e-6, h(P) - 1 +1.09e-6; not trial-class). The lead's coefficient-level c6f
      transplants (fxs1_<d>, d = -1e-3, -3e-3, -1e-2, base c6f_seg1, the starts of the lead's fixed-c fits) are being
      evaluated instead (G60).

  (d) c6f iteration 500 plus eps t (field level; c6fA). Ratios to eps = 0 (global 2.431e-6, strip r 8.36 th 0.013; J
      3.03e-6 / 3.26e-6; 10-100 4.25e-7; rms 2.60e-8):

      | eps | global (all at the strip) | J(0.03) / J(0.01) | 10-100 | rms | h(P) - 1 |
      |---|---|---|---|---|---|
      | -2e-3 | 2.214e-6 (0.91) | 0.89 / 0.99 | 1.82 | 2.35 | +4.13e-7 |
      | -1.5e-3 | 1.812e-6 (0.75) | 0.79 / 0.85 | 1.54 | 1.63 | +2.78e-7 |
      | -1e-3 | 1.873e-6 (0.77) | 0.78 / 0.82 | 1.30 | 1.19 | +1.72e-7 |
      | -5e-4 | 2.145e-6 (0.88) | 0.86 / 0.88 | 1.13 | 1.01 | +9.55e-8 |
      | +5e-4 | 2.730e-6 (1.12) | 1.18 / 1.17 | 0.94 | 1.10 | +2.85e-8 |

      - The strip of c6f moves with c_l as on c6d. The global maximum falls by 23 to 25 percent at -1e-3 to -1.5e-3.
        That is less than on c6d (29 percent on the coefficient line), and J falls by 15 to 22 percent.
      - J stays above c6d's base value at every offset: 2.36e-6 at -1e-3 against 1.46e-6.
      - The far bands of c6f are lower than c6d's, so their relative rise is larger: 10-100 rises 1.30 to 1.54 at -1e-3 to
        -1.5e-3, against 0.94 to 0.97 on the c6d coefficient line.
      - Field level, so beyond 1e-3 these values are not trial-class values ((c)). The exponential form of the same line
        on c6f was stopped (see the (c) addendum); the coefficient-level fxs1 transplants replace it (G60).
      Verdict: intermediate, no reading.

  (e) Lead slot-2 plan. NOTES_FOR_TEAM 05:52Z item 4 (run_fixc_c6f.sh) was superseded at 06:12Z by work/c6/run_c6f_fixc.sh
      (mtime 06:11:54Z; NOTES 06:12Z item 2). Its order: c6f segment-1 post-processing; transplant onto c6f_seg1; fixed c_l
      at d = -1e-3; segment 2 (free); fixed c_l at d = -1e-2; segment 3; fixed c_l at d = -3e-3. Fixed fits use inner 500,
      segments inner 2500. Comments:
      1. Schedule. The fixed fits get one relinearization more than their free control. The lead states this caveat with
         every reading (06:12Z item 2 (c)). Agreed: an "excluded" reading stays conservative, and a "not determined"
         reading carries the caveat. Compare at equal LSQR iteration counts; both logs have checks every 250.
      2. Premise of 06:12Z item 2 (a), "the identity holds at fixed c_l (c_l enters through the scale L)". On the
         transplants my identity c_l equals the shape's value to 2e-7: 5.5733636 against 5.5733638 at d = -3e-3, and
         5.5753622 against 5.5753624 at -1e-3. CONFIRMED for these shapes; to be checked again on the fitted state.
         The choice of -1e-3 is inside the flat part of the max-norm valley ((b): 0.74 at -1e-3, 0.71 at -1.5e-3, 0.73 at
         -2e-3). If that state is adopted, "c_l chosen by the maximum norm" must be said, as the lead proposes, and the
         value is then fixed by the choice, to within the valley width of at least 1e-3.
      3. h(P) clause. h(P) - 1 at the unrefitted -3e-3 shape is +7.2e-7 (mine) / +7.0e-7 (lead), close to the rule's
         1e-6 bound. Every reading must quote the fitted h(P) - 1.
      4. Missing side. The plan has no fixed fit above the L2 value. The unrefitted coefficient line (b) leaves the J band
         first on the upper side (+5e-4: J 1.38 / 1.41), while the lower side stays inside to -2e-3. Relative to a -1e-3
         candidate, the free control (d = 0) is the only point above, at +1e-3. I recommend a fixed fit at +2e-3 to
         +3e-3 in place of, or after, the d = -3e-3 step (7). It is the only place where an "excluded" reading at the
         few-1e-3 scale looks reachable at this basis. The -1e-2 step bounds the soft side, where the readings so far are
         all "not determined".
      5. Control start. With base c6f_seg1, c6f segment 2 (unshifted) is the right control for the reading rule. A free fit
         from the shifted start would test whether c_l returns, a different and optional question.
      6. J must be computed with the same eps_P list and the same export grid (24576 x 576) as for the control.

### G59. Proposed FINAL_REPORT 4.3 paragraph on the independent discretization (NOTES_FOR_TEAM 05:55Z, notes/final_sec4_43_numerics.md). Recorded 2026-10-18T06:18Z
  Method: each number checked against NUM_REPORT 3.16, 3.17 and section 4, NOTES_FOR_LEAD 05:38Z / 05:52Z, and my G45,
  G47 and G52. A read-only helper extracted the source lines. I re-read the decisive lines myself (NUM_REPORT lines 376 to
  404, 420 to 432, 484 to 511; VERIFY_REPORT G45 table and G52 table).
  Result, claim by claim:
  1. Method description; three-step tangent table (+0.42 / 26 percent, +0.052 / 18 percent, +0.034 / 5 percent at
     4.7e-5, 2.4e-5, 1.5e-5); "tangent prediction, not a stationarity test"; "grid dependent"; "neither establishes ...
     nor excludes ... 5.60 to 5.64; does not confirm": CONFIRMED (NUM 3.17 rows; +0.415 rounds to +0.42).
  2. "fixed-c_l fits over 5.52 to 5.71 are equally good to 20 percent": REFUTED as worded.
     - NUM 3.16 item 4d: the rms runs 8.16e-7 (5.5163) to 3.53e-7 (5.6263 / 5.6563), a factor 2.3. It is flat to 20 percent
       only over 5.5563 to 5.5963 (19 percent) and over 5.60 to 5.70. The maxima run 3.0e-5 to 8.7e-6.
     - My G45 (c): every near-P diagnostic improves monotonically toward larger s over 5.52 to 5.71, by a factor 4 (max)
       and 11 (J).
     Suggested wording: "flat to 20 percent in that discretization's L2 residual over +-0.02 around 5.5763 and over 5.60
     to 5.70; over 5.52 to 5.71 no fixed-c_l fit is worse than the one at 5.5763 by more than a factor 1.5 (L2) or 1.3
     (maximum), and those above it are better".
  3. "maxima 3e-5 to 6e-5 at 10 < r < 100 in the verifier's normalization": CONFIRMED only for the two free iterates of
     G45 (a) (c_l 5.5934, 5.2923), and the range mixes N_f and N_v (4.1e-5 / 3.0e-5 and 4.0e-5 / 5.6e-5). For the fixed-c_l
     states my values are 6.7e-6 to 8.1e-6 (N_f) / 9.6e-6 to 1.2e-5 (N_v) at (256,64) (G45 (c)) and 6.0e-6 to 7.2e-6 /
     1.1e-5 to 1.2e-5 at (256,128) (G52). Suggested: "3e-5 to 6e-5 for the free iterates and 6e-6 to 1.2e-5 for the
     fixed-c_l states".
  4. "about 1e-6 rms away from P in its own normalization": CONFIRMED with the qualifier (NUM 3.16: 3.7e-7 to 1.25e-6).
     The qualifier must stay: G45 (a) refuted "1e-6" as a maximum in my evaluator.
  5. "1.5e-5 to 1e-4 next to P": the lane's own maxima are 8.7e-6 to 1.2e-4 (NUM 3.16, NOTES_FOR_LEAD). My values: N_v 1e-5
     to 3.5e-5, N_f 3.2e-5 to 1.3e-4 for the fixed-c_l states; N_v 5e-5 to 1.4e-4, N_f 2e-4 to 5e-4 for the free
     iterates. Approximately right in the lane's normalization. Say "in its own normalization" here too.
  6. "grids up to 384 x 96 and 256 x 128 with radial clustering at P": (384,96) is unclustered (NUM section 4, line 488).
     It is not in 3.16 / 3.17, and I have not evaluated it. Suggested: "(384,96) unclustered and (256,128) clustered at P".
  7. "least first-order residual cost ... 1e-3 to 6e-5": CONFIRMED (NUM section 4: 9.9e-4 at (256,64) to 6.1e-5 at
     (384,96)). The 6e-5 end is from section 4, not 3.16 / 3.17. Cite section 4.
  8. "free iterations drift between 5.29 and 5.60": the upper end is 5.5934 (NUM 3.16; my G45 (a) 5.59338). Should read
     "5.29 and 5.59". NUM section 4 adds "these runs use different weights/domains and are not one constrained family".
     That caveat belongs here.
  9. "extra rows ... do not change this": CONFIRMED as a first-order statement (NUM 3.16: none approaches the factor
     needed; the Taylor patch raises the cost by up to 5.5x).
  10. "The linearized exponent step toward that discretization's minimizer": conflicts with NUM 3.17 (05:50Z correction:
      dk* "is neither a nonlinear minimiser location nor a parameter error estimate"; the (320,80) +0.42 is contradicted by
      that grid's own m(s) minimum near 5.575). Suggested: "the Gauss-Newton tangent prediction of the exponent step".
  11. "Its exported soft direction, added to the 302-function trial, is registered at offsets of a few 1e-3": approximately
      right for the near-P maximum (G47: factor 2 crossed between +2e-3 and +3e-3 and between -1e-3 and -3e-3). J reacts
      already at 1e-3 (6x / 12x), and only about 1e-4 is undetectable. Two caveats must be added:
      - the direction is fixed and the shapes are not refitted, so these are upper bounds on the cost (G47);
      - it is a field-level (linear in rho) line, a first-order statement beyond 1e-3, not a line in the trial class (G58 (c)).
      Suggested: "registered at offsets of 1e-3 (characteristic defect) to a few 1e-3 (near-P maximum) along that fixed,
      unrefitted direction".
  12. "a least-squares residual of 1e-5 next to P does not fix c_l to better than about 0.05 to 0.1": the sources give the
      level as 1e-5 to 5e-5 (NUM 3.16, my G52). Suggested: "of 1e-5 to 5e-5 next to P".
  13. "did not converge to the candidate at the standard": correct, but it could be read as "found a different c_l". Its
      fixed states at 5.5763 show no motion in a free fit (NUM 3.16). Suggested: "did not reach the standard".
  Verdict: CONFIRMED with corrections. Item 2 must be changed (REFUTED as worded). Items 3, 6, 8, 10, 11 and 12 need the
  suggested wording; items 5 and 7 need a qualifier or citation.

### G60. c6f segment 1 final shape (it750) and the lead's fxs1 transplants (c6f_seg1 + d t at coefficient level, the starts of the run_c6f_fixc.sh fixed-c fits), between nodes (intermediate). Recorded 2026-10-18T06:33Z
  Method:
  - Copy of lead/work/c6/c6f_seg1_shape.npz (mtime 06:21:04Z; lead it750 objective 7.6528e-6, c_l 5.57636243108287)
    in runs/gen4/c6fS1_shape.npz. scratch/seg_audit.sh (gen_audit N9000/R7.652e4, N10125/R7.652e5, N11250/R7.652e6,
    N16875 q512 M639, then extra checks); logs runs/audit/c6fS1_N*.log.
  - Lead transplants fxs1_<d>_shape.npz (transplant.py, fxs1_make.json; copied to runs/gen4/fxs1) at N16875 q384 M479
    through scratch/gen_audit_cfg.sh; logs runs/audit/fxs1<d>_N16875_q384_R7.652e6.log. Table:
    python3 scratch/tab_any.py <logs>.
  (a) c6f it750 at N 11250 q384 R 7.652e6, compared with c6f it500 (G57) and c6d segment 1 (G48) at the same config:

      | quantity | c6f it750 | c6f it500 | c6d seg1 |
      |---|---|---|---|
      | c_l (identity) | 5.5763624 | 5.5763622 | 5.5763622 |
      | h(P) - 1 | +1.73e-7 | +2.9e-7 | +5.5e-7 |
      | global flux max (strip) | 2.276e-6 (r 8.47 theta 0.013) | 2.419e-6 (r 8.28 theta 0.013) | 2.424e-6 (r 8.30 theta 0.016) |
      | flux max 0.1-2 / 10-100 / 100-1000 | 1.54e-7 / 4.37e-7 / 6.7e-8 | 1.47e-7 / 4.18e-7 / 6.5e-8 | 2.17e-7 / 7.54e-7 / 2.48e-7 |
      | flux rms, all | 2.39e-8 | 2.60e-8 | 5.38e-8 |
      | J(0.03) / J(0.01) | 3.08e-6 / 3.39e-6 | 3.00e-6 / 3.18e-6 | 1.37e-6 / 1.25e-6 |
      | N_v max (far) | 1.12e-6 | 1.14e-6 | 1.46e-6 |

      Domain / resolution sequence for c6f it750 (global max, J.03, h(P) - 1, N_v max): N9000 R7.652e4 3.06e-6, 1.00e-5,
      +1.83e-6, 3.79e-6 (finite-box, as in G45 (d)); N10125 R7.652e5 2.295e-6, 3.15e-6, +2.2e-7, 1.03e-6; N11250 R7.652e6
      as above. The two large-R configs agree to 1 percent in the global max and 2.3 percent in J.
      Extra checks (scratch/seg_audit.sh, runs/audit/c6fS1_extra.log, N 11250 q384):
      - identity c_l 5.576362428; on the traces h(P) = 0.999999941, and c_l from h(P) = 1 differs by +5.4e-8;
      - center jet: 8 p4 / r^4 = beta - alpha = -0.13158 to 7e-7 for r in [2e-3, 2e-2], and 4 (p2 - c r^2/2) / r^4 -> -1/3;
        E and D2 are relative 2e-8 to 1e-7 on all five fit windows;
      - a single x-axis zero of W1 at 8.6008413 (x* 8.6008416); no y-axis zero of W2; min W2/y on the y axis 5.5766;
        no open-quadrant cell where both components change sign;
      - min |W| / (c_l |X|) over |X - P| >= 1 / 0.3 / 0.1 is 0.0216 / 0.0065 / 0.0025 (attained at the inner edge).
      All as for c6d and c6f it500: CONFIRMED.
  (b) Reading:
      - At N 11250 q384, iterations 500 to 750 lower the strip maximum by 6 percent and the rms by 8 percent. At N 16875
        q512, the strip is 2.424e-6 (r 8.47, theta 0.0123) against it500's 2.403e-6, so it is 0.9 percent higher. The
        it750 strip value thus moves by 6.5 percent between the two configs (theta grid points 0.0131 against 0.0123),
        so no iteration change in the strip can be read at this level (G42: the strip maximum is between-node and
        q-sensitive). The rms at q512 is 2.39e-8 (it500 2.61e-8), so the 8 percent fall holds on both configs. Every
        other band is unchanged to 5 percent. J does not fall: +3 / +7 percent at q384, and at q512 J.03 / J.01 =
        3.11e-6 / 3.46e-6 against 3.03 / 3.26 e-6, so +3 / +6 percent. h(P) - 1 at q512 is +3.2e-8.
      - c6f it750 against c6d: global max 0.94, rms 0.44, 10-100 band 0.58, far N_v 0.77, but J 2.2x (0.03) and 2.7x
        (0.01). The lower objective of the angular-150 / degree-375 basis is not a lower characteristic defect.
      - Lead's c6f_seg1_cd.txt gives J(eps_P 0.03) per start angle (max 2.449e-6 at theta0 0.02, min -6.05e-7 at theta0
        1.5508, spread 3.054e-6). My spread at N11250 is 3.08e-6: agreement to 1 percent, CONFIRMED. Its h(P) =
        1.0000028 (from c6f_fields.npz, export grid not read yet) is not reproduced at large R: mine is +1.7e-7 at
        N11250 R7.652e6, but +1.8e-6 at N9000 R7.652e4. The 2.8e-6 is therefore probably a finite-box or field-grid value.
        The lead's own c6f_seg1_export.log gives, at the x-axis root x 8.6008416, mu2 = 0.99999998716 (error 1.3e-8),
        from the trial formula. So the 2.8e-6 comes from the sampled field c6f_fields.npz. OPEN until its grid is read.
      - G42 (b) angular split of the residual map (python3 scratch/ang_split.py c6fS1 195 / 295; resmap N 11250 q384,
        414 x 489; sin(n theta) with n odd; normalized by N_f). In the strip (r 8.2 to 9.4, theta < 0.1) the total is
        2.28e-6. The parts are 2.98e-6 (n < 195) and 3.04e-6 (n >= 195), and 8.5e-6 and 9.3e-6 with the cut at 295. All
        part maxima lie on the first row, theta 0.003. Near theta = pi/2 the parts reach 1e-5 to 2e-4 against totals of
        5e-7. The two parts cancel each other where N_f is small, so the split does not place the c6f strip residual
        above or below either cut. No reading; the tool is inconclusive on this shape (lead NOTES 06:12Z item 3: answered
        in this form).
  (c) fxs1 transplants at N16875 q384 M479. The d = 0 row is c6f it750 itself at the same config (scratch/c6fS1_follow2.sh,
      finished 06:39:00Z):

      | d | c_l (mine; lead fxs1_make.json) | global (loc) | J.03 / J.01 | 10-100 | rms | h(P) - 1 | N_v far |
      |---|---|---|---|---|---|---|---|
      | 0 | 5.5763624 (5.5763624) | 2.313e-6 (strip r 8.47 theta 0.013) | 3.11e-6 / 3.46e-6 | 4.41e-7 | 2.39e-8 | +3.2e-8 | 1.12e-6 |
      | -1e-3 | 5.5753625 (5.5753626) | 2.176e-6 (strip r 8.47 theta 0.010) | 2.27e-6 / 2.69e-6 | 5.14e-7 | 2.74e-8 | +1.41e-7 | 1.04e-6 |
      | -3e-3 | 5.5733639 (5.5733640) | 3.338e-6 (strip r 8.40 theta 0.036) | 2.84e-6 / 3.84e-6 | 9.23e-7 | 5.31e-8 | +8.40e-7 | 1.05e-6 |
      | -1e-2 | 5.5663800 (5.5663803) | 1.390e-5 (stem ring r 9.02 theta 0.39) | 2.88e-5 / 3.66e-5 | 6.74e-6 | 3.53e-7 | +8.28e-6 | 1.82e-6 |

      Against the c6d coefficient line (G58 (b), same config): at -1e-3, c6d gives global 1.792e-6, J 9.9e-7 / 9.9e-7;
      at -3e-3, global 2.164e-6, J 2.09e-6. On c6f the strip stays the global maximum at both offsets. At -3e-3 the strip
      rises by 1.5x relative to -1e-3; on c6d the global max moved to the stem ring. The c6f field line (G58 (d),
      it500 base) at -1e-3 gave 1.873e-6, J 2.36e-6 / 2.67e-6; the transplant J agrees with it to 4 percent. Its strip value
      is 16 percent higher, with a different base iterate (it500 against it750).
      - Ratios to d = 0 (global, J.03 / J.01, 10-100, rms): -1e-3 0.94, 0.73 / 0.78, 1.17, 1.15; -3e-3 1.44, 0.91 / 1.11,
        2.10, 2.22; -1e-2 6.0, 9.3 / 10.6, 15, 15. On c6d (G58 (b)) the same offsets gave global 0.74 / 0.89 and J 0.68 /
        1.43. On c6f the strip barely moves at -1e-3, while J falls by 22 to 27 percent.
      - Read with the lead's rule (G47 (e)) as unrefitted upper bounds. The -1e-3 start is already within 30 percent of the
        free fit in the near-P max and J, with h(P) - 1 1.4e-7 (the objective is not computed by me). The -3e-3 start is 1.44x
        in the near-P max: outside 30 percent but below 2x, so neither reading applies before refitting.
      - The -1e-2 start is 6.0x the base in the global max and 9x in J (h(P) - 1 8.3e-6). The fixed fit at -1e-2 must
        remove that before it can be compared.
      - The c_l identity matches the lead's values to 1e-7 at -1e-3 and -3e-3 and to 3.4e-7 at -1e-2 (identity premise of run_c6f_fixc.sh
        CONFIRMED on c6f, as on c6d in G58 (e) 2).
      - These are unrefitted starts. Each gives only an upper bound on the fixed-c_l cost at its offset; the fixed fits
        decide (fixc_c6f_m1.0e-03 started 06:23:21Z).
  Verdict (intermediate): (a), the extra checks and the J comparison CONFIRMED. The source of the cd-file h(P) figure is
  OPEN (the trial value meets the standard). (c): the c_l identity is CONFIRMED. The starts are recorded; the fixed fits
  decide the c_l reading on c6f.

### G61. c6f segment 1: between-node grid spread completed (G60 (a)); angular structure of the strip next to the x-axis left of P; h(P) in c6f_fields.npz (G60 (b) OPEN item); FINAL_REPORT entries 05:53 and 06:33. Recorded 2026-10-18T06:54Z
  Method:
  - G60 follow job (scratch/c6fS1_follow.sh, pid 3350844, ended 06:52:49Z): code/gen_audit.sh on runs/gen4/c6fS1_shape.npz
    at R 7.652e6 with N 22500 q384 M479, N 16875 q768 M959, N 22500 q512 M639. Logs runs/audit/c6fS1_N*_R7.652e6.log;
    table python3 scratch/tab_any.py <logs>.
  - Residual maps runs/audit/{c6cS1,c6dS1,c6fS1}_resmap.npz (code/vresmap.py, the maps of G42, G48 and G60). New tools,
    all in scratch/ and reading only those maps or the shape files:
    - strip_freq.py <tag> 8.2 8.6 0.15: at every third r row, the local angular frequency of R/N_f on 0 < theta <= 0.15,
      from the median spacing of its zeros and from the peak of a sin^2-windowed periodogram over n = 20 to 900 (n is the
      frequency in sin(n theta); the trial mode cos(2 m theta) has n = 2m, so the caps are n = 200 for m <= 100 and
      n = 300 for m <= 150).
    - strip_env.py <tags>: max |R| and max |R / N_f| per r bin of width 0.1 and per theta band.
    - hspec.py <shape>: |H_m(r)| at fixed radii, the angular profiles of the trial exponent H evaluated directly from the
      shape coefficients (scipy BSpline on spline_knots in q, the trial's origin factor), block rms over 5 modes.
    - hhigh.py <shape> 80: max over theta bands of |sum_{m >= 80} H_m(r) cos(2 m theta)|.
  (a) Between-node grid spread for c6f it750 (completes G60 (a); global flux max, location, J.03 / J.01, h(P) - 1):

      | N | q | global (r, theta) | 10-100 | J.03 / J.01 | h(P) - 1 | N_v far |
      |---|---|---|---|---|---|---|
      | 11250 | 384 | 2.276e-6 (8.466, 0.0131) | 4.37e-7 | 3.08e-6 / 3.39e-6 | +1.73e-7 | 1.12e-6 |
      | 16875 | 384 | 2.313e-6 (8.470, 0.0131) | 4.41e-7 | 3.11e-6 / 3.46e-6 | +3.24e-8 | 1.12e-6 |
      | 16875 | 512 | 2.424e-6 (8.470, 0.0123) | 4.47e-7 | 3.11e-6 / 3.46e-6 | +3.24e-8 | 1.12e-6 |
      | 16875 | 768 | 2.442e-6 (8.470, 0.0115) | 4.46e-7 | 3.11e-6 / 3.47e-6 | +3.24e-8 | 1.15e-6 |
      | 22500 | 384 | 2.331e-6 (8.463, 0.0131) | 4.39e-7 | 3.12e-6 / 3.48e-6 | -1.72e-8 | 1.12e-6 |
      | 22500 | 512 | 2.433e-6 (8.463, 0.0123) | 4.49e-7 | 3.12e-6 / 3.48e-6 | -1.72e-8 | 1.13e-6 |

      - The strip maximum converges in q: +4.8 percent from q384 to q512 and +0.7 percent from q512 to q768. Its location
        moves to the axis with the theta nodes (0.0131, 0.0123, 0.0115). The N step 16875 to 22500 changes it by 0.4 to
        0.8 percent. The converged value is 2.44e-6, equal to c6d segment 1 at N 22500 (2.44e-6, G48) and to c6f it500
        (2.40e-6 to 2.42e-6, G57). The 6 percent fall from it500 to it750 at q384 (G60 (b)) is a sampling effect of
        the coarser theta grid; the strip has not moved from c6d to c6f it750.
      - J, the 10-100 band and N_v are stable to 1 to 3 percent across all six configurations. h(P) - 1 depends on N at
        the 1e-7 level (+1.7e-7, +3.2e-8, -1.7e-8 for N 11250, 16875, 22500) and not on q. |h(P) - 1| <= 1.7e-7.
      CONFIRMED (grid convergence of the c6f it750 audit). This replaces the "2.28e-6 to 2.42e-6" range of G60 with
      "2.28e-6 to 2.44e-6, converged 2.44e-6".
  (b) Local angular frequency of R / N_f next to the axis (strip_freq.py, theta <= 0.15; zero spacing / periodogram peak):

      | r | c6c (cap n 200) | c6d (cap n 200) | c6f it750 (cap n 300) |
      |---|---|---|---|
      | 8.21 | 187 / 186 | 190 / 188 | 236 / 200 |
      | 8.31 | 188 / 188 | 190 / 188 | 234 / 202 |
      | 8.36 | 190 / 188 | 189 / 190 | 258 / 208 |
      | 8.41 | 190 / 190 | 190 / 190 | 264 / 306 |
      | 8.47 | 191 / 192 | 193 / 192 | 274 / 300 |
      | 8.52 | 194 / 192 | 191 / 194 | 272 / 278 |
      | 8.57 | 193 / 194 | 193 / 196 | 263 / 268 |

      The near-axis oscillation of the residual sits just below the cap of each basis: n 186 to 196 for the m <= 100
      trials, n 264 to 306 for the m <= 150 trial where its residual is largest (r 8.41 to 8.57). At r <= 8.36 on c6f
      the periodogram peak stays at n 200 to 208, where its residual is 2.5 times smaller (row maxima 8.7e-7 to 9.2e-7
      against 2.28e-6 at r 8.47).
  (c) Envelope (strip_env.py), c6d segment 1 against c6f it750, same resmap configuration:

      | r bin | max abs R, theta < 0.05 | max abs R, 0.05-0.15 | max R/N_f, theta < 0.05 | max R/N_f, 0.05-0.15 |
      |---|---|---|---|---|
      | 7.9-8.0 | 3.74e-5 / 4.16e-6 | 4.90e-5 / 1.24e-5 | 2.21e-6 / 5.04e-7 | 1.49e-6 / 3.09e-7 |
      | 8.1-8.2 | 4.08e-5 / 8.11e-6 | 5.66e-5 / 1.68e-5 | 2.39e-6 / 7.12e-7 | 1.69e-6 / 4.90e-7 |
      | 8.2-8.3 | 4.48e-5 / 8.44e-6 | 6.64e-5 / 1.94e-5 | 2.42e-6 / 9.81e-7 | 1.78e-6 / 5.23e-7 |
      | 8.3-8.4 | 4.79e-5 / 1.55e-5 | 7.35e-5 / 2.60e-5 | 2.41e-6 / 1.84e-6 | 1.81e-6 / 5.34e-7 |
      | 8.4-8.5 | 4.73e-5 / 2.39e-5 | 8.46e-5 / 2.44e-5 | 2.29e-6 / 2.28e-6 | 1.75e-6 / 6.15e-7 |
      | 8.5-8.6 | 4.09e-5 / 2.21e-5 | 8.28e-5 / 2.65e-5 | 2.11e-6 / 2.11e-6 | 1.70e-6 / 7.07e-7 |
      | 8.6-8.7 | 2.34e-5 / 1.20e-5 | 6.71e-5 / 2.92e-5 | 9.33e-7 / 1.03e-6 | 1.24e-6 / 5.27e-7 |
      | 8.7-8.8 | 9.60e-6 / 6.53e-6 | 4.54e-5 / 1.37e-5 | 4.66e-7 / 4.08e-7 | 6.11e-7 / 1.88e-7 |

      (x* = 8.6008.) From c6d to c6f the absolute near-axis residual falls by 1.5 to 9 times on 7.9 <= r <= 8.8. R / N_f
      falls by 2.5 to 4.4 times in theta < 0.05 for r < 8.3 and by 2.3 to 4.8 times in 0.05 to 0.15 everywhere. It does
      not fall in theta < 0.05 for 8.4 <= r <= 8.7 (2.29e-6, 2.11e-6, 0.93e-6 against 2.28e-6, 2.11e-6, 1.03e-6). The
      normalized strip has contracted to within about 0.3 of P on its left and about 0.05 rad of the axis, while its
      maximum stayed. The absolute residual halves there, but N_f is small there (N_f vanishes on the axis by the odd
      parity in y and is small near the stagnation point), so the normalized maximum is unchanged.
      In absolute terms the near-P maximum is not in the strip on either trial: theta 0.15 to 0.6 at r 8.6 to 8.9 carries
      1.2e-4 to 2.3e-4 (c6d) and 3.2e-5 to 1.2e-4 (c6f).
  (d) Angular spectrum of H (hspec.py; |H_m| block rms at m = 80 / 90 / 100 / 120 / 140 / 150):
      - c6d (cap m 100), r 8.00 / 8.30 / 8.47: m 80 5.0e-8 / 7.2e-8 / 6.7e-8, m 90 2.1e-8 / 3.3e-8 / 4.9e-8, m 100 2.4e-9 /
        3.9e-9 / 5.7e-9. From m 90 to m 100 the blocks fall by 8.5 to 8.8 times (taper at the cap); on c6f the same
        step is 1.4 to 1.6 times.
      - c6f (cap m 150), same radii: m 80 5.5e-8 / 7.2e-8 / 6.7e-8, m 100 2.4e-8 / 3.1e-8 / 4.0e-8, m 120 9.3e-9 / 1.5e-8 /
        1.4e-8, m 140 5.9e-10 / 5.2e-9 / 5.3e-9, m 150 9.4e-12 / 4.0e-10 / 1.2e-9. Up to m 80 the two spectra agree
        to 10 percent at every radius r >= 8 listed (at r 6 the m 60 and m 80 blocks differ by 40 to 70 percent, at
        1e-9 to 2e-8). The modes 100 to 120 that c6d could not carry are present on c6f at 1e-8 to
        4e-8, and the taper has moved to m 140 to 150.
      - At r 8.47 on c6f, m 60 to 120: 1.5e-7, 6.7e-8, 4.0e-8, 1.4e-8, about m^-3.4. No sign of exponential decay before
        the taper. At r 8.60 (P) the modes m >= 95 are 1.7 to 16 times smaller than at r 8.47 (1.1e-8 to 1.9e-10), and at
        r >= 8.75 smaller again.
      - hhigh.py, the part m >= 80 of H by theta band: maximal on the axis for every r listed. c6d, r 8.00 to 8.47:
        4.6e-7 to 8.3e-7 at theta < 0.01, falling by 10 to 15 percent to the band 0.05 to 0.10. c6f, same radii: 1.2e-6
        to 1.9e-6 at theta < 0.01 (2.2 to 2.6 times c6d), falling 2.4 to 2.8 times to the band 0.05 to 0.10. At r 8.60 on
        c6f it is 1.7e-7 on the axis (max 5.5e-7 at theta 0.055). Right of P (r 8.65) both carry 1.1e-6 to 1.2e-6 on the
        axis, unchanged by the cap.
  (e) Reading:
      - The strip next to the x-axis left of P is a band-edge effect in each basis tested: the residual oscillates just
        below the angular cap (m <= 100 and m <= 150 alike). With the higher cap the fit puts more high-mode content into
        H, concentrated within about 0.05 rad of the axis at r 7.5 to 8.55, with an algebraic spectrum (about m^-3.4) that
        is not converged at m 120. The normalized strip is removed farther than about 0.3 from P, but its maximum moves
        toward P (r 8.30 to 8.47) and keeps its value (2.44e-6 converged on both).
      - (Revised 06:59Z by (h) below.) First version: "consistent with a near-axis feature whose angular width shrinks as r
        tends to x*". (h) does not support the shrinking width: the H content the cap step added has the same angular
        profile at every r from 7.6 to 8.56. Revised reading: left of P the trial needs H content above m 100 within about
        0.05 rad of the axis; that content has a fixed angular profile, grows toward P and ends within about 0.06 of P.
        Each cap tried (100, 150) leaves a residual oscillation at its own top modes. The normalized maximum sits next to
        P because there the content is largest and N_f is smallest. This is a reading: c6f also differs from c6d in its
        fit history (750 LSQR iterations from a transplanted start). It predicts that a further cap step lowers the strip
        away from P and adds content above m 150 in the same place. A test that does not need a new basis: track the
        hspec / hhigh / hdiff numbers at r 8.0 to 8.5 through c6f segment 2 and rw_c6f.
      - Correction to G57 (e): "the G48 hypothesis (the strip is an angular band-edge effect) is REFUTED for the strip" is
        withdrawn as worded. Correct statement: raising the angular cap from 100 to 150 does not lower the strip maximum,
        but the strip residual sits at the band edge of whichever cap is used, and the cap step removes it away from P.
        The strip depends on the angular truncation; it does not fall with it.
      - For rw_c6f (lead NOTES 06:42Z): long_solve_rw.py reweights by |res / den| after a max filter, a normalized value,
        so it targets the strip rather than the absolute maximum at theta 0.15 to 0.6. Under the reading above, a
        reweighted fit can lower the strip only by spending the top modes on it; whether that holds under refinement is
        the same question. I will apply (a) to (d) to rw_c6f and to segment 2 when they end.
  (f) G60 (b) OPEN item, h(P) = 1.0000028 in c6f_seg1_cd.txt (lead NOTES 06:46Z item 4). Checked from c6f_fields.npz
      (axis_x, axis_w, axis_h; 24576 axis nodes, spacing 6.447e-3 at x*):
      - Root of axis_w by a local cubic: x* = 8.60084159 (G60: 8.6008416).
      - Node values h - 1 on the four nodes around x*: +8.8e-4, +2.6e-4, -3.3e-4, -9.1e-4. Linear interpolation gives
        h(x*) - 1 = +2.814e-6, the cd-file value.
      - The 4-point cubic through the same nodes gives -3.2e-9. Least-squares cubics over 6, 8 and 12 nodes give +7.6e-8,
        +2.7e-7 and +1.2e-6, so a wider stencil is worse: h is not a cubic over 0.03 to 0.08.
      - The lead's -1.28e-8 (local cubic) and my -3.2e-9 differ by the stencil, and both are at the 1e-8 level. The linear
        error matches h''/2 times the product of the distances to the two nodes for h'' about 0.56.
      The 2.8e-6 is an interpolation error of the cd-file header (the c6d value 2.87e-6 likewise). CONFIRMED: the G60 (b)
      OPEN item is closed. h(P) - 1 of c6f it750 is at most 1.7e-7 in my evaluator (a) and at the 1e-8 level on the
      export axis trace.
  (g) FINAL_REPORT (mtime 06:47Z) status lines:
      - 05:53 entry (c6f it500): "The strip is not an effect of the angular truncation; it moves with c_l (previous entry)"
        is REFUTED as worded, by (b) to (e). Proposed: "The strip is an oscillation at the top of the angular basis (local
        frequency just below the cap for m <= 100 and for m <= 150). Raising the cap removes it farther than about 0.3
        from P but does not lower its maximum, which moves toward P. It also moves with c_l (previous entry)."
      - 05:53 entry (c6d field line): "no offset from -3e-3 to +1e-3 is excluded" is a field-level statement. The 06:17
        entry already says that the field line is first-order only beyond 1e-3, so no change is needed.
      - 06:33 entry (G60): "2.28e-6 to 2.42e-6 ... depending on the between-node grid" should read "2.28e-6 to 2.44e-6,
        2.44e-6 converged in the between-node grid (equal to the m <= 100 trial)". "h(P) - 1 = +1.7e-7 at the largest box"
        should read "|h(P) - 1| <= 1.7e-7 at the largest box (N 11250 to 22500)".
  (h) Addendum 06:59Z: what the cap step added (scratch/hdiff.py A B [mcut]: H_B - H_A at fixed r and theta, regular part of
      H, modes m >= mcut; A = c6d segment 1, B = c6f it750):
      - All modes: on 7.6 <= r <= 8.56 the difference is an oscillation in theta confined to theta < 0.08. It has zeros
        near theta 0.007, 0.022 and 0.04 at every r, values -9.3e-7 / +9.7e-7 / -7.2e-7 at theta 0 / 0.015 / 0.03 for
        r 8.47, and below 3e-8 for theta >= 0.12. Its amplitude grows toward P: theta = 0 values -4.2e-7 (7.6), -5.8e-7
        (8.0), -7.6e-7 (8.3), -9.3e-7 (8.47), -7.1e-7 (8.56), -3.0e-7 (8.59). It changes sign at P: +2.0e-7 (8.62), +1.2e-7
        (8.70). With mcut 60 the table is the same to 20 percent, so the change sits in m >= 60.
      - Modes m >= 101 only (absent from c6d, so this is c6f's own top part): the same theta profile, amplitude -1.9e-7
        (7.6), -4.0e-7 (8.0), -7.2e-7 (8.47), -3.4e-7 (8.59), -6.8e-8 (8.62), 3e-8 (8.66 to 8.70).
      - Local decay exponent p of the H_m block rms (|H_m| ~ m^-p; 9-mode blocks, fits over m windows 60-90, 80-110 and
        100-130) on c6f: 2.1 to 5.8 for 7.6 <= r <= 8.56, and 5.6 to 14 for 8.62 <= r <= 10. The windows scatter, so the
        m^-3.4 of (d) is a rough figure for r 8.47, not a law. The slow decay is confined to the axis segment left of P.
      - Cross-check of the hdiff evaluation against my full trial generator (code/gen_shape.py, log(rho_c6f / rho_c6d),
        which includes the singular terms and the small differences in L (2.3e-7 relative) and k (8e-9)): at r 8.0 and
        8.47 for theta 0.0025 to 0.03 the two agree up to a constant offset of +4e-8 (for example at r 8.47, theta 0.015:
        1.01e-6 against 9.71e-7; at theta 0.03: -6.81e-7 against -7.24e-7). The offset is smooth in theta, so it does not
        affect the oscillation.
      - The angular profile of the added content does not narrow toward P. The (e) reading is revised accordingly.
  Verdict:
  - (a) and (f): CONFIRMED.
  - (b) to (d) and (h): measured, CONFIRMED as stated.
  - (e) is a reading, not a demonstration. The G57 wording is withdrawn, and the FINAL_REPORT 05:53 sentence is REFUTED as
    worded.
  - c6f it750 does not improve on c6d at the global between-node maximum (2.44e-6 both, converged), and its J is 2.2 to
    2.7 times larger. Not YES-level.

### G62. Section 4.3 paragraph version 2 (lead notes/final_sec4_43_numerics.md, mtime 06:45Z; NOTES_FOR_TEAM 06:46Z item 5). Recorded 2026-10-18T06:56Z
  Method: every sentence checked against the G59 items, NUM_REPORT 3.16 item 4d (lines 375 to 404, re-read for this item),
  NUM_REPORT section 4 lines 568 to 571, and the numerics lane's NOTES_FOR_LEAD 06:20Z item 1.
  Result:
  - G59 items 1, 3 to 13 are taken in the suggested form: the "did not reach the standard" opening (13); the qualifier
    "in its own normalization" (4, 5); 3e-5 to 6e-5 (free) and 6e-6 to 1.2e-5 (fixed-c_l) at 10 < r < 100 (3); near-P
    maxima 9e-6 to 1.2e-4 with the lane's shell rms 3e-6 to 2e-5 (5, numerics 06:20Z (a)); 384 x 96 unclustered (6);
    5.29 to 5.59 with the "not one constrained family" caveat (8); "Gauss-Newton tangent prediction" (10); the
    unrefitted, linear-in-rho line with "1e-3 (characteristic defect) to a few 1e-3 (near-P maximum)" and the two caveats
    (11); "1e-5 to 5e-5" (12). CONFIRMED.
  - "The least first-order residual cost ... 1e-3 to 6e-5, falling with resolution faster than the residual floor":
    NUM section 4 line 570 gives 9.9e-4 / 2.9e-4 / 6.1e-5 at floors 1.2e-3 / 4.7e-4 / 2.3e-4 for (256,64) / (320,80) /
    (384,96), so the cost falls 16 times while the floor falls 5 times. CONFIRMED.
  - Correction needed (it applies to my own G59 item 2 wording, which the lead adopted): "Over 5.52 to 5.71 no fixed-c_l fit
    is worse than the one at 5.5763 by more than a factor 1.5 in its L2 residual or 1.3 in its near-P maximum, and those
    above 5.5763 are better ... The L2 residual is flat to 20 percent over 5.556 to 5.596 and over 5.60 to 5.70" holds on
    the clustered 256 x 64 grid only (factors 1.54 at 5.5163 and 1.27 at 5.5363). On the unclustered 320 x 80 grid
    (5.5263 to 5.6763), the fit at 5.6763 is worse than at 5.5763 by 1.25 in L2 (1.563e-6 against 1.246e-6) and by 1.23 in
    its maximum (5.8e-5 against 4.7e-5), and the minimum is near 5.575. So "those above 5.5763 are better" is false on that
    grid. On the clustered 256 x 128 grid (5.5563 to 5.5963 only) the L2 residual falls monotonically by 19 percent and
    the maximum is flat. G59 item 2 suggested wording is withdrawn. Replacement: "On the clustered 256 x 64 grid, over 5.52
    to 5.71 no fixed-c_l fit is worse than the one at 5.5763 by more than a factor 1.5 in its L2 residual or 1.3 in its
    near-P maximum, and those above 5.5763 are better (near-P maxima from 3.0e-5 to 8.7e-6 across the range); its L2
    residual is flat to 20 percent over 5.556 to 5.596 and over 5.60 to 5.70. On the unclustered 320 x 80 grid the L2
    minimum is near 5.575 and the fit at 5.68 is 25 percent worse; on the clustered 256 x 128 grid the L2 residual falls
    by 19 percent from 5.556 to 5.596. The discrete minimizer moves by 0.06 to 0.1 between grids."
  - Minor: "near-P maxima falling from 3.0e-5 to 8.7e-6 as c_l increases" is not monotone in detail (3.03e-5 at 5.5363
    above 2.96e-5 at 5.5163; 1.95e-5 at 5.6263 above 1.91e-5 at 5.6063): "across the range" is accurate, "as c_l increases"
    is not. "In the verifier's normalization" for the 10 < r < 100 maxima: the ranges mix the flux and the velocity
    normalizations (G59 item 3), so "normalizations" is accurate.
  - FINAL_REPORT (06:47Z) timeline entry 06:18 says "The corrected text is the one in section 4.3", but section 4 of
    FINAL_REPORT has no 4.3 yet (the paragraph is only in notes/). The reference holds once the paragraph is inserted.
  - Timeline entries 06:17 and 06:18 otherwise agree with G58 and G59; the 06:18 entry should also take this item's grid
    qualifier when the paragraph is inserted.
  Verdict: CONFIRMED with one correction (the grid qualifier above) and two minor wording notes. With these the paragraph
  may enter FINAL_REPORT 4.3 as far as the verifier is concerned.

### G63. Lead fixed-c_l fit at c_l = 5.5753626 (1e-3 below c6f segment 1), LSQR iterates it 250 and it 500 (intermediate; it 500 added 07:45Z). Recorded 2026-10-18T07:11:58Z
  Item: lead work/c6/fixc_c6f_m1.0e-03_shape.npz as written at the it-250 check (06:58Z; copy runs/gen4/fixcf/fxm1_it250_shape.npz,
  md5 6b42ef94...). Start = transplant fxs1_-1.0e-03 (G60). Lead jsonl: objective 9.707e-6 at the start, 8.765e-6 at it 250
  (c6f segment 1: 7.653e-6). Intermediate shape; check only.
  Method: my generator and evaluator between nodes (gen_audit_cfg.sh), configs N 16875 q384 M479 and N 22500 q512 M639,
  R 7.652e6; scratch/tab_any.py; scratch/hdiff.py against the start shape.
  Result:
    config / shape            global max R/N_f (location)      J(0.03)   J(0.01)   h(P) - 1    far N_v   band 10-100
    q384  c6f segment 1       2.313e-6 (r 8.47, th 0.013)      3.11e-6   3.46e-6   +3.2e-8     1.12e-6   4.41e-7
    q384  fxs1 -1e-3 (start)  2.176e-6 (r 8.47, th 0.010)      2.27e-6   2.69e-6   +1.4e-7     1.04e-6   5.14e-7
    q384  fixed -1e-3 it 250  1.405e-6 (r 8.528, th 0.013)     2.01e-6   2.31e-6   +2.5e-8     1.10e-6   4.62e-7
    q512  c6f segment 1       2.433e-6 (r 8.463, th 0.012)     3.12e-6   3.48e-6   -1.7e-8     1.13e-6   4.49e-7
    q512  fixed -1e-3 it 250  1.504e-6 (r 8.532, th 0.012)     2.01e-6   2.32e-6   -1.7e-8     1.11e-6   4.66e-7
    q384  fixed -1e-3 it 500  8.99e-7 (r 8.504, th 0.065)      1.35e-6   1.57e-6   +2.7e-8     1.11e-6   4.28e-7
    q512  fixed -1e-3 it 500  9.84e-7 (r 8.550, th 0.022)      1.35e-6   1.58e-6   -1.7e-8     1.11e-6   4.46e-7
  (it 500: lead jsonl objective 8.574e-6 at 07:32Z; copy runs/gen4/fixcf/fxm1o1i500_shape.npz, md5 4b30fbc4..., by
  scratch/fxm1_follow.sh.)
  (the q384 to q512 step raises the strip maximum by 7 percent here and by 5 percent on c6f segment 1; G61 (a) found q512 to
  q768 adds 0.7 percent on c6f segment 1.)
  In the N_v normalization the near-P maximum (|X - P| < 0.5) is 4.22e-7 (c6f segment 1: 6.80e-7, q512); the N_v global
  maximum stays the far-field ripple, 1.11e-6 at r 3.5e4 (G39).
  The global maximum is still the near-axis strip left of P, now 0.07 from P instead of 0.14. The bands away from P are
  unchanged to 10 to 15 percent. The refit change in the exponent near the axis (hdiff, it 250 minus start) is at most
  1.5e-7 (r 7.6, theta 0) with the G61 (h) angular profile and the opposite sign (it removes about a third of the near-axis
  packet the cap step added); right of P it is below 4e-8.
  Residual map (run_resmap.sh, N 11250 q384, window r 6 to 14, theta <= 1.6; scratch/strip_env.py, strip_freq.py):
    r band     max R/N_f theta < 0.05: c6f seg 1 / fixed it 250     max |R| theta < 0.05: c6f seg 1 / fixed it 250
    8.2-8.3    9.8e-7 / 7.6e-7                                      8.4e-6 / 1.37e-5
    8.3-8.4    1.84e-6 / 1.03e-6                                    1.55e-5 / 1.66e-5
    8.4-8.5    2.28e-6 / 1.23e-6                                    2.39e-5 / 2.05e-5
    8.5-8.6    2.11e-6 / 1.36e-6                                    2.21e-5 / 2.14e-5
    8.6-8.7    1.03e-6 / 8.1e-7                                     1.20e-5 / 1.34e-5
  The normalized strip falls 1.3 to 1.9 times, while the absolute band maximum (which sits near theta 0.05, not at the
  normalized peak near theta 0.012) is unchanged to 20 percent and grows at r 8.2 to 8.3. The strip oscillation is still at
  the band edge of the m <= 150 basis (zero-crossing frequency 246 to 281 in sin(n theta) for r 8.2 to 8.57; periodogram
  peaks n 278 to 302, and n 216 to 220 at r 8.47 to 8.52), so the refit lowers its amplitude without changing its character.
  Addendum it 500 (resmap at N 11250 q384): max R/N_f by r band, theta < 0.05 / 0.05 to 0.15: 3.7e-7 / 3.9e-7 (r 8.2-8.3),
  3.8e-7 / 5.1e-7 (8.3-8.4), 5.3e-7 / 8.5e-7 (8.4-8.5), 8.5e-7 / 9.0e-7 (8.5-8.6), 6.0e-7 / 4.8e-7 (8.6-8.7). The near-axis
  strip is no longer the dominant feature: the theta 0.05 to 0.15 band next to P is as large. The remaining oscillation is
  still at the band edge (zero-crossing frequencies 226 to 292 in sin(n theta)). N_v near P (|X - P| < 0.5) 2.76e-7. The
  exponent change from the start (hdiff) has grown to 3.2e-7 at r 8.0, theta 0, with the same angular profile as at it 250.
  h(P) = 1 holds to 2e-8 at both c_l values (5.5763624 free, 5.5753626 fixed). The identity h(P) = 1 alone does not separate
  c_l values 1e-3 apart after a refit (consistent with G52 (d)).
  Reading: after 250 LSQR iterations at c_l fixed 1e-3 below the free fit, the between-node maximum is 1.6 times lower than
  c6f segment 1 (1.50e-6 against 2.43e-6, q512) and J is 1.5 times lower, while the L2 objective is 15 percent higher.
  After 500 iterations it is 2.5 times lower (9.8e-7, q512; 9.0e-7, q384), J(0.03) / J(0.01) 2.3 / 2.2 times lower, and the
  L2 objective is 12 percent higher (8.574e-6 against 7.653e-6). In the free c6f fit the strip did not change between it 500
  and it 750 (G61 (a): 2.44e-6 at both, converged in q) while its objective fell 4 percent; this favours the c_l reading,
  but it is not the controlled comparison. This
  agrees in direction with G56 and G58 (the max-norm optimum lies 1e-3 to 2e-3 below the L2 c_l). It is NOT yet a c_l
  effect: the fixed fit has 250 more iterations than c6f segment 1. The control is c6f segment 2 (free, from c6f segment 1,
  same grid) at it 250. Until that is read, the decrease may come from the extra iterations.
  Verdict: measured (intermediate). The fixed -1e-3 it-500 iterate is the first lead shape whose between-node maximum of
  R/N_f is below 1e-6 everywhere in my evaluator (q384 and q512, R 7.652e6). In the N_v normalization the global maximum is
  the far-field ripple at 1.11e-6 (r 3.5e4, G39), unchanged by the fit. This is one resolution, one domain and an
  intermediate iterate; J still grows from eps_P 0.03 to 0.01. The G20 (b1) standard is not yet met. What it needs: the final
  shape of this fit at the q384 / q512 / q768 configs; the free control c6f segment 2 at equal iterations; the domain study
  and the far-field N_v at this c_l; and a c_l quoted with the interval implied by G58 and this item (the identity
  h(P) = 1 holds at both 5.5763624 and 5.5753626).

### G64. Domain study on c6d segment 1 (numerics lane, leadcode/c7 dom300 and dom100); the export convention of export_fit.py for domain fits; the closure-radius metadata point; ray check B. Recorded 2026-10-18T07:49:31Z
  (a) Domain fits. Items: numerics/leadcode/c7/dom300_seg1_shape.npz (fit radius 300 shape units = 2295.6 physical,
  R_shape 333.33, closure radius R_shape L = 2550.68, stored c_l 5.57636282004) and dom100_seg1_shape.npz (fit radius 100 =
  765.2, R_shape 111.11, closure 850.23, stored c_l 5.57636442828). Both start from c6d_seg1 and ran 1000 LSQR iterations
  on 20480 x 480 with the lead's long_solve.py --fit-radius (copies runs/gen4/dom/, md5 4f918d89..., a4eacaaf...).
  Method: my generator with the two-term closure at R_shape L, which is the fit's own convention (gen_shape.py 'closure');
  my inverse to R 7.652e6 with k_self; regions r <= Rfit and r > Rfit (VAUDIT_RFIT); configs as for c6dS1; extra_checks with
  closure (scratch/dom_audit.sh, dom_audit2.sh). c6dS1 (R_shape 1000) is evaluated formula-global as in G48.
    N 22500 q384 [N 16875 q512]   c6dS1 (1000)           dom300                  dom100
    c_l (identity, my inverse)    5.5763622              5.5763628               5.5763644
    c_l from h(P) = 1, minus it   -3.7e-8                +2.6e-10                -1.5e-8
    h(P) - 1                      -2.0e-8 [+7.4e-8]      -3.5e-9 [+2.1e-8]       -1.6e-9 [+5.1e-8]
    max R/N_f, r <= Rfit (strip)  2.444e-6 [2.409e-6]    2.630e-6 [2.604e-6]     2.544e-6 [2.495e-6]
    flux max, 10 <= r <= Rfit     8.03e-7 (10 to 100)    6.86e-7 [7.51e-7]       7.04e-7 [7.08e-7]
    N_v max, r <= Rfit            6.8e-7 (r <= 1000)     1.03e-6 [1.07e-6]       7.10e-7 [6.97e-7]
    (c6dS1: N_v 1.456e-6 at r 2.0e4, outside 1000 L, is the far ripple of G39.)
    J(0.03) / J(0.01)             1.48e-6 / 1.46e-6      2.00e-6 / 2.12e-6       1.76e-6 / 1.84e-6
    B_3 (IBP)                     0.2976                 0.2969                  0.2966
  D14 centre relations hold to 5e-8 relative on both domain fits; one zero of W_1 on the x-axis, none of W_2 on the y-axis,
  no open-quadrant cell where both components change sign. The residual for r > Rfit is that of the closure (dom300 up to
  3.1e-4 in N_f and 5.1e-3 in N_v; dom100 up to 1.7e-3 and 2.4e-2). These fields are bounded-domain fits, C^1 at R_shape L
  (G34), and are not admissible trial densities on the plane.
  Reading: c_l moves by +6e-7 from domain 1000 to 300 and by +2.2e-6 from 1000 to 100. h(P) = 1 holds to 5e-8 on all three.
  The near-P maximum is 2.4e-6 to 2.6e-6 on all three, and J is 1.5e-6 to 2.1e-6. The comparison mixes the domain change with
  1000 extra iterations on another grid, so the drift is not a pure domain effect. It is three orders of magnitude below the
  c_l interval of order 1e-3 (G58, G63). The far-field truncation does not limit the near-P residual at this level.
  (b) Export convention. export_fit.py calls diagnostic(shape, nr, nt, 10000., export=..., tail="two-term"): for every
  R_shape the exported field is the trial formula out to 1e4 shape units, closed only there. For a domain fit the formula
  between R_shape and 1e4 is not fitted. My evaluator with the closure moved to 1e4 L (gen_shape.py 'closure=10000',
  scratch/gen_audit_clo.sh) reproduces the exports: c_l 5.5763627679 for dom300 (export 5.5763627677) and 5.5763660133 for
  dom100 (export 5.5763660131); for dom100, h(P) - 1 = +6.41e-6 (export mu2 - 1 = +6.09e-6). Effect at N 11250 q384, export
  convention against fit convention: dom100 near-P max 5.34e-6 against 2.47e-6, band 10 to 100 3.29e-6 against 7.0e-7,
  J(0.03) / J(0.01) 2.87e-5 / 3.46e-5 against 1.75e-6 / 1.77e-6, c_l +1.6e-6; dom300 near-P max 2.457e-6 against 2.553e-6,
  J 1.30e-6 / 1.19e-6 against 1.96e-6 / 2.05e-6, c_l -5e-8.
  Consequence: the export-based dom100 diagnostics in leadcode/c7 (dom100_seg1_cd.txt with h(P) 1.0000061 and J(0.03)
  about 2.7e-5, _jsplit, _map, _b3, dom100x_diagnostic.json with cl 5.5763660) describe a field that was not fitted. They
  must not be quoted as dom100's numbers. For dom300 the export changes J by a factor of 1.5. The domain study should be
  read in the fit's convention (the table in (a)) or re-exported with the inverse domain R = R_shape. For c6d_seg1 the
  same convention leaves 1000 to 1e4 shape units unfitted, but the effect is small: c_l 3.2e-9 (item (c)), and my
  formula-global flux on 1000 <= r <= R is 2.6e-7.
  J depends on the exterior continuation through U: on dom300, moving the closure from R_shape to 1e4 changes J by 1.5 times
  and the near-P maximum by 4 percent. For a bounded-domain fit, J must be quoted with its closure stated.
  (c) Closure-radius metadata point (numerics NOTES 06:46Z item 2). My formula-global inverse on c6dS1 at R 7.652e6 gives
  c = 15.7290865097, c_l = 5.5763621699 (N 11250 to 22500 agree to 1e-12). The export gives 5.5763621697 (closure at
  76520.5), the referee's formula-global value is c = 15.729086509081 (mine is 6.6e-10 above, the R 7.652e6 truncation),
  and the shape's stored 5.5763621731 comes from the fit's closure at 7652. CONFIRMED. The 3.2e-9 difference does not affect
  any quoted digit.
  (d) Ray check, configuration B (numerics runs/ray/chain_full.log; Gauss-Legendre phimax 0.01, amin 1e-5, nglphi 24,
  adaptive radial ang 0.015, kfac 1, ngl 24; 51 targets on c6d_seg1). Max |dU| 7.97e-7 at r 300, theta 1.37; max
  |dU|/|U| 1.17e-8; max |dU . grad rho| / D 5.6e-9; median 3.4e-11. Configuration A gave 1.67e-6, 4.7e-8, 5.3e-9. The
  far-node |dU| halves from A to B, as expected from the referee's finding that A's far-node differences are ray
  quadrature, while the residual impact stays at 5e-9. Configuration C was still running at the time of this entry.
  Verdict: (a) measured; the domain series shows no far-field truncation effect on the near-P residual above 2e-7, and a c_l
  drift of 2.2e-6. (b) CONFIRMED: the export field of a domain fit is not the fitted field. dom100's export diagnostics are
  REFUTED as dom100 numbers, should they be quoted. (c) CONFIRMED. (d) inverse-error row: CONFIRMED at configuration B
  (export U of c6d_seg1 correct to 1.2e-8 relative, 6e-9 in the normalized residual); C to be added.

### G65. The quick_scan convention for domain fits (numerics 07:20Z table, NUM_REPORT item 2); the dom90 reading rule; ray check C; lead analysis 13.15 (c); FINAL_REPORT 4.3 and timeline 06:33 to 07:11; SPEC v4.6. Recorded 2026-10-18T07:59:57Z
  (a) Which field the numerics 07:20Z table describes. leadcode/c7/quick_scan.py calls load_shape(path, nr, nt) without
  fit_radius, so CentreShape is built with the default R = 1000 shape units and the two-term closure sits at 1000 L for
  every shape, also for dom300 (R_shape 333) and dom100 (R_shape 111). It also uses the stored c_l (1/z[0]). The J, jsplit,
  map and B_3 rows come from the exports, closed at 1e4 L (G64 (b)). So for a domain fit both the scan rows and the J rows
  evaluate the fitted formula continued, unfitted, from R_shape L to 1000 L or 1e4 L. Method: my generator with the closure
  moved to 1000 L (gen_shape.py 'closure=1000', scratch/dom_clo1000.sh), my inverse to R 7.652e6 with k_self, N 11250 q384,
  identity c_l; same configuration as the fit-convention and closure-1e4 rows of G64. c6dS1 formula-global at the same
  configuration for reference: 2-10 2.424e-6, 10-100 7.54e-7, J 1.37e-6 / 1.25e-6.
    N 11250 q384                  fit convention (R_shape L)  closure 1000 L        closure 1e4 L (export)  numerics scan
    dom100 c_l                    5.5763644                   5.5763659             5.5763660               5.57636443 (stored)
    dom100 h(P) - 1               +3.2e-7 (-1.6e-9 at N22500) +6.07e-6              +6.41e-6                +5.56e-6
    dom100 2-10 flux max / N_v    2.472e-6 / 6.90e-7          5.178e-6 / 1.70e-6    5.340e-6 / 1.80e-6      5.15e-6 / 1.64e-6
    dom100 10-100 flux max        7.01e-7                     3.139e-6              3.285e-6                3.21e-6
    dom100 100-1000 flux max      8.05e-4 (r > Rfit 765)      2.67e-5               2.68e-5                 2.71e-5
    dom100 J(0.03) / J(0.01)      1.75e-6 / 1.77e-6           2.72e-5 / 3.27e-5     2.87e-5 / 3.46e-5       cd 2.86e-5
    dom300 2-10 flux max          2.553e-6                    2.461e-6              2.457e-6                2.54e-6
    dom300 10-100 flux max        6.45e-7                     7.28e-7               7.30e-7                 7.39e-7
    dom300 h(P) - 1               +1.7e-7                     -2.4e-8               -3.0e-8                 -1.9e-7
    dom300 J(0.03) / J(0.01)      1.96e-6 / 2.05e-6           1.32e-6 / 1.22e-6     1.30e-6 / 1.19e-6       cd 7.8e-7
  (My J and the lead's char_defect J use different label sets and are compared within a column only.) My closure-1000 rows
  reproduce the scan's dom100 bands to 1 to 3 percent (the remaining difference: identity against stored c_l, grid). In
  the fit's own convention dom100 is within 1.02 (2-10) and 0.93 (10-100) of c6dS1 at the same configuration, and dom300
  within 1.05 and 0.86. The numerics reading "R = 111 is 2x worse next to P and 4x at 10-100 (c_l +2.3e-6, h(P) - 1
  5.6e-6)" is a statement about the unfitted continuation of the dom100 formula beyond R_shape L, not about the dom100
  fit. As a statement about the dom100 fit it is REFUTED. The 2x / 4x are not evidence of an unconverged fit either: the
  fit in its convention is at the c6dS1 level. For dom300 the convention matters less (4 percent near P, J 1.5 times).
  The c_l change from c6dS1 to dom100 is +2.2e-6 in the fit convention (G64 (a)) and +3.8e-6 in the export convention.
  (b) dom90 reading rule (lead NOTES 07:23Z item 1). The rule compares the interior bands 2-10 and 10-100 with c6d_seg1's
  at a factor 1.5. On dom100 the convention changes these by 2.1 and 4.5, so the outcome of the rule depends on the
  convention. run_dom90.sh uses the same quick_scan.py and export_fit.py, so its dom90_seg{1,2}_scan.json, cd, jsplit, map
  and b3 files will describe dom90's formula closed at 1000 L and 1e4 L, with the fit domain at R_shape = 100. The rule
  should be applied in the fit's convention: quick_scan with load_shape(..., fit_radius=90) (load_shape already supports
  it: R = fit_radius / 0.9), and an export with R = R_shape, or my fit-convention rows. I audit both dom90 segments in all
  three conventions (scratch/dom_audit_seg.sh via dom90_chain.sh; fit convention at N 11250 q384 and N 16875 q512 for
  segment 1, three configurations plus extra_checks for segment 2; closure 1000 L and 1e4 L at N 11250 q384). Under the
  fit convention dom100 segment 1 already meets the rule (1.02, 0.93, c_l +2.2e-6).
  Recommendation for the report: quote the domain study in the fit's convention, state the closure radius of every
  number, and do not quote the dom100 column of the numerics 07:20Z table or of NUM_REPORT item 2 as dom100's numbers.
  (c) Ray check, configuration C (numerics runs/ray/c6d_full_C.json, trapezoid 8192 angles, adaptive radial ang 0.03,
  kfac 2, ngl 16; 51 targets on c6d_seg1; my reduction of the json, |dU| as the Euclidean norm): max |dU| 3.43e-7 at
  r 300; max |dU|/|U| 7.3e-9; max impact |dU . grad rho| / D 3.0e-9; median 2.9e-11. By region (A / B / C): within 0.5
  of P 9.9e-10 / 9.9e-10 / 1.0e-9; 0.5 to 2.5 from P 4.29e-8 in all three; r near 0.1 8e-12; r near 1 6e-11; r near 20
  6.1e-9 / 1.0e-9 / 1.0e-9; r near 100 1.9e-6 / 1.65e-8 / 4.9e-9; r near 300 4.1e-7 / 8.1e-7 / 3.4e-7. Near P and out to
  r 100 the three quadratures agree to their own differences; at r 300 they scatter at 3e-7 to 8e-7 and are not
  converged, as the numerics lane states. The residual impact is at most 6e-9 in all three. The P-clustered variations
  (runs/ray/chain_C_vary.log, fineP and fineP005) are still running; the numerics lane will post the row after them.
  CONFIRMED as far as C: the export U of c6d_seg1 agrees with an independent quadrature to 1e-9 near P and 5e-9 at r 100;
  at r 300 the agreement is about 1e-6 absolute, limited by the check. The row text is checked when posted.
  Addendum 2026-10-18T08:02:22Z: the row text (NUM_REPORT 3.17 item 7 "FINAL INVERSE-ERROR STATEMENT", posted 07:54Z) checked against
  c6d_full_{A,B,C}.json and vary_{base,fine,fineP}.json. Near P, 0.5 to 2.5 from P, r 0.1, 1, 20: A, B and C agree, as
  stated (9e-10, 4.3e-8, 1.0e-9). r 100: C 4.9e-9 at both nodes, equal to the P-clustered variation (5e-9 / 4.9e-9) and
  to the referee's CPU values (4.1e-9 / 4.8e-9): CONFIRMED. Maximum impact 3.0e-9 at (8.551, 1.994): this is C's maximum
  (A and B had 5.3e-9 and 5.6e-9 at far nodes, from their own quadrature); CONFIRMED as stated for C. One qualifier:
  "1.4e-8 at r = 300" is the P-clustered value at one of the four r 300 nodes, (58.52, 294.22), where C gives 8.9e-8. C
  gives 1.5e-8 at (294.22, 58.52) and (249.43, 166.66), and 3.4e-7 at (166.66, 249.43), which was not rerun with P
  clustering. Suggested: "1.4e-8 at the r = 300 node rerun with P-clustered panels (1.5e-8 to 3.4e-7 at the other three
  in configuration C)". Also, "converged across three angular rules and two ray rules" holds for r <= 20; at r 100 the
  convergence is C plus the P-clustered rerun and the referee's CPU values. With these qualifiers the row is CONFIRMED.
  (d) Lead analysis 13.15 (c), the one new measured fact (lead NOTES 07:17Z item 2). Method: code/vresmap.py maps of
  trd_+1.0e-03, trd_-1.0e-03, trd_-3.0e-03 (runs/gen4/trd, the unrefitted coefficient line on c6d) and the c6dS1 map, all
  N 11250 q384; signed R/N_f on theta < 0.08 at the nearest map row to r 8.40 / 8.47 / 8.52 (rows 8.397 / 8.466 / 8.518;
  map theta step 0.0033, coarser than the lead's 5.5e-4, so lobe peaks may read up to a few percent low);
  scratch/lobe_c.py.
    d = +1e-3: +2.94e-6 / -2.67e-6 / +2.51e-6   (lead 2.9e-6 / 2.7e-6 / 2.4e-6)
    d = 0:     +2.32e-6 / -2.15e-6 / +1.84e-6   (lead 2.2e-6 at 8.47)
    d = -1e-3: +1.77e-6 / +1.76e-6 / -1.46e-6   (lead 1.8e-6 / 1.8e-6 / 1.4e-6)
    d = -3e-3: +1.03e-6 / +1.35e-6 / +8.7e-7, mostly positive, 2 to 5 sign changes in theta < 0.08 (lead: the alternating
               pattern breaks up, lobes 1.0e-6 to 1.4e-6, mostly positive)
  Zero spacing for d = +1e-3, 0, -1e-3: 0.0164 to 0.0172 (lead 0.0164 to 0.0175 on c6d). CONFIRMED.
  (e) FINAL_REPORT section 4.3 (file mtime 07:15Z) is the G62 replacement inserted as stated. One refinement, from the
  numerics lane (NOTES 07:23Z) and NUM_REPORT 3.16 line 403: the "0.06 to 0.1" in my G62 sentence mixes two quantities.
  The L2 minimizer moves by about 0.06 between grids (5.64 on clustered 256 x 64, near 5.575 on unclustered 320 x 80; on
  clustered 256 x 128 it lies above the scanned 5.5963), and the zero of h(P) - 1 by about 0.1 (about 5.72 against 5.58 to
  5.63). Suggested sentence, the numerics lane's: "The discrete L2 minimizer moves by about 0.06 between grids, the zero
  of h(P) - 1 by about 0.1." The same applies to the SPEC v4.6 section 8 c_l item ("its discrete minimizer moves by 0.06 to
  0.1 between grids"). Wording only.
  Timeline entries: 06:33 agrees with G61 (a) (2.28e-6 to 2.44e-6, 2.44e-6 converged; |h(P) - 1| <= 1.7e-7 over N 11250 to
  22500). 06:54 agrees with G61 (b) to (h) except one figure: away from P the cap step lowers R/N_f next to the axis by
  2.3 to 4.8 times (G61 (c): 2.5 to 4.4 in theta < 0.05 for r < 8.3, 2.3 to 4.8 in 0.05 to 0.15), not 2.5 to 4.8. 06:56
  agrees with G62. 07:11 agrees with G63 at iterate 250 (1.50e-6 against 2.43e-6 at N 22500 q512; J 1.5 times lower; L2 15
  percent higher); iterate 500 (G63, 07:45Z: 9.84e-7 at N 22500 q512, J 1.35e-6 / 1.58e-6) is not yet in the timeline.
  The 05:53 sentence is replaced as G61 (g) asked.
  Verdict: (a) the numerics domain-study rows for dom100 are REFUTED as dom100's numbers (they are closure-1000 and
  closure-1e4 numbers of an unfitted continuation); in the fit convention dom100 and dom300 match c6dS1 inside their fit
  radii. (b) the dom90 rule needs the convention named; fit convention recommended. (c) CONFIRMED to configuration C. (d)
  CONFIRMED. (e) CONFIRMED with one refinement and one figure.

## G66 Lead analysis 13.16 (structure of the fits at the source point P): independent check of (a) to (f), and the off-axis structure along the characteristic (2026-10-18T08:32Z)

Item: lead notes/analysis.md 13.16 (a) to (f) and the proposed first-line summary "not C^3 at the source point P
(numerical, [H'''] about 0.12)" (lead NOTES 07:53Z and 08:17Z). H = log a, rho = x^2 y a.

Method. scratch/pjump.py evaluates H pointwise from the shape file by my own formula (B-spline profiles in q, angular
factor chi^(m-1) for m > 1, singular terms; re-coded from my gen_shape formula, not from the lead's code). Third
x-derivative by a 7-point central difference, O(h^4), h = 1e-3 or 2e-3 physical (validated on sin 3x + x^3: error
1.3e-6). Three step estimators at a centre x_c:
  E1 the lead's form (separate degree 6 or 7 polynomial fits of H on each side, third derivative at x_c), windows
     (0.05, 0.5), (0.1, 0.8), (0.2, 1.2) as in notes/lambda_mode/axisjump.py, and smaller windows (0.03, 0.3), (0.05, 0.3);
  E2 quadratic least-squares fits of the finite-difference H''' on each side, extrapolated to x_c (scratch/pjump_win.py,
     inner edge a from 0.02 to 0.25, outer edge a + 0.4);
  joint one smooth Legendre polynomial of degree D = 6, 8, 10, 12 on |xi| < 0.8 plus J xi_+^3 / 6, with a gap |xi| < g
     excluded, g = 0 to 0.3 (scratch/pjump_joint.py).
Manufactured controls on the same grids: a lambda-mode C |xi|^lambda (lambda = 2.9306) and a pure cubic step, both
scaled to J = 0.12 at xi = 0.1 (E1 and E2 both return 0.12 to 0.13 on both, flat in a). [h'''] from my velocity: the
traces of code/mk_traces.py (h = 2 c_l - w'), same estimators. Shapes c6b, c6d, c6f (segment-1 finals) and fxm1o2i250
(= lead fixc_c6f_m1.0e-03 final, md5 equal).

(a) Derivation of the exponent from the axis system w q' = (1 - h) q, w' + h = 2 c_l, h' + q' = 2 a_2: h'(x*) = -A q'(x*)/g*
with A = 2 c_l - 1 = 10.15272, g* = q(x*) = 29.7538, and the local transport of a perturbation of H along the axis gives
|xi|^lambda with lambda = g*/A. The algebra is CONFIRMED. It is a heuristic for the axis restriction only: the 2D local
structure is not determined by it. Near P the characteristics are xi ~ y^A times a constant (the source is a node), and the
homogeneous local solutions are rho_s = y^(1 + g*) F(xi / y^A) with F arbitrary, which contains line layers along a single
characteristic and point-supported structures as well as the axis |xi|^lambda mode. The axis exponent does not select one.
Remarks: (i) the curl identity forces [h'''] = -[H'''] times a factor near 1 whenever a_2 is C^2, so the ratio does not
test the reading (lambda-mode control -1.00, cubic control -1.02); (ii) the L2 cost of a lambda-mode against a cubic step
of the same size differs by the factor (3 - lambda) = 0.07 at leading order, so a fit is nearly indifferent between them.

(b) lambda = g*/A = 2.9306 from the c6d numbers. CONFIRMED.

(c) Numbers at P on the axis, E1 with the lead's three windows:
  c6f +0.119 / +0.115 / +0.126 (lead +0.120 / +0.115 / +0.126), c6d +0.124 / +0.116 / +0.127 (lead identical).
  Controls with E1, window (0.05, 0.3), at x* +- 0.5, +- 0.8, +- 1.5: at most 0.002 at y = 0, 0.3, 0.7, 1.0. Controls whose
  window reaches P (x* +- 0.3, or the large windows at x* +- 0.8) are not valid controls and were not used.
  [h''']: c6d -3.467 / -3.317 / -3.049 (lead -3.37 / -3.33 / -2.99), ratio [h''']/[q'''] -0.936 / -0.955 / -0.803 (lead
  -0.91 / -0.95 / -0.79); c6f ratio -0.949 / -0.968 / -0.810; c6b -0.937 / -0.956 / -0.806. CONFIRMED against the lead's
  values to 3 percent (my velocity, not the export; remark (i) applies).
  The size of the step depends on the estimator: E2 falls from 0.16 (a = 0.02) to 0.06 (a = 0.25); E1 stays at 0.11 to
  0.15; the joint fit gives 0.05 to 0.14, rising with D and falling with the gap; with |xi| >= 0.3 excluded no step is
  needed (the joint fit returns J consistent with 0). The numbers are CONFIRMED; "[H'''] about 0.12" is one estimator.

(d) and (f) Axis profile of H''' (c6d, h = 1e-3): -0.129 at xi = -0.006, +0.229 at +0.016, +0.066 at +0.03, +0.089 at
+0.06, +0.033 at +0.1, 0.000 at +0.2, -0.022 at +0.5. The extremes next to P agree with the lead's. The right side does
not settle at 0.10 to 0.14: it decays to 0 by xi = 0.2. For |xi| > 0.13 c6b, c6d and c6f agree to 0.003. Inside
|xi| < 0.1 the transient depends on the basis: right peak 0.145 / 0.229 / 0.174 and left dip -0.038 / -0.129 / -0.111 for
c6b / c6d / c6f. The plateau sentence of (f) is REFUTED.

New verifier finding: the off-axis structure. scratch/pjump_off.py and pjump_char.py. At fixed y the location of
max |H''''| near x* is xi = -0.0100 / -0.0150 / -0.0230 / -0.0460 for y = 1 / 1.25 / 1.5 / 2. The characteristic leaving P,
xi_c = -a_2 y^2 / (A - 2) with a_2 = q'(x*)(1 - 1/lambda)/2 = 0.0897, predicts -0.011 / -0.0172 / -0.0248 / -0.044; the
circle r = x* (a radial knot line) is at -0.058 / -0.091 / -0.132 / -0.236. The sharp feature lies on the characteristic,
not on a radial knot line. Step of H''' across the characteristic (E1 a = 0.05, 0.1, 0.2, degree 6; joint D 10, gap 0.05
and 0.15; centre x* + c y^2, c = -0.011):
  y <= 0.3  +0.12
  y = 0.4   +0.05 to +0.10
  y = 0.5   about 0
  y = 0.6   -0.09 to -0.12
  y = 0.7   -0.17 to -0.24
  y = 0.85  -0.29 to -0.37
  y = 1.0   -0.35 to -0.43
The values agree to 0.01 between c6b, c6d, c6f and fxm1o2i250. These four share one lineage (all continue c4_r1 / c6a), so
the agreement does not separate a property of the fitted family from a property of a solution.
Consequence for the reading of (a) and (d) (heuristic). Two local pictures fit the axis data.
  (1) A layer along the characteristic: a C^(2, lambda - 2) singularity across the curve xi = xi_c(y). The jump
  coefficient on each side obeys a linear homogeneous first-order ODE along the curve, with the same coefficient on
  both sides at leading order (the velocity has the same regularity as rho, but for a singularity across a curve its
  leading singular part is local, U_s = -n_x n^perp rho_s, so it only adds a smooth term proportional to the same
  coefficient). Hence the ratio of the two side coefficients is constant along the curve and the step keeps its
  sign. Near P this layer is the F(t) = C_+- |t|^lambda member of (2), rho_s = C y |xi - xi_c|^lambda, whose step in H
  is constant in y at leading order. The measured step changes sign near y = 0.5 and grows to about -0.4 at y = 1. This picture is contradicted.
  (2) A point singularity at P: rho_s = y^(1 + g*) F(xi / y^A) with F smooth at finite argument and |t|^lambda tails.
  At fixed y > 0 it is smooth, varying on the scale y^A (below 1e-3 for y >= 0.5, unresolved by any fit), and appears
  as a step whose size is independent of y at leading order. A sign change at y = 0.5 then needs O(1) relative
  corrections at distance 0.5 from P. Not excluded, but not the leading-order picture.
  So the single lambda-mode reading of (a) and (d) is NOT CONFIRMED. Other readings (a smooth steep layer of the fitted
  family along the characteristic, a combination of local modes, a property of the shared lineage) are not excluded by
  anything measured here.

Proposed first-line summary "not C^3 at the source point P (numerical, [H'''] about 0.12)": REFUTED as wording. Every fit
is C^6 (order-7 B-splines), so the fits are C^3 at P; what is measured is a change of H''' over a distance of about 0.02
to 0.1 that is not resolved into a jump (the estimators disagree by a factor 3 and the step vanishes when |xi| < 0.3 is
excluded). Nothing measured shows that a solution is not C^3. Suggested body wording, not first-line: "every fit has a
sharp change of the third derivative of log a across the characteristic leaving P (about +0.12 at P by separate
polynomial fits on each side, changing sign near height y = 0.5 and reaching about -0.4 at y = 1); whether a solution has
a C^(2, lambda - 2) singularity there is open."
Separating test (recommended): a refit from a start in which this structure has been removed (for example H''' smoothed
across the characteristic in |y| < 1.5, then refitted to the same objective). If the structure returns with the same
signs and sizes it is a property of the objective's minimizer in this class; if not it is lineage.

Verdict: (a) CONFIRMED as a heuristic for the axis, with remarks (i) and (ii) and the non-uniqueness of the 2D local
structure. (b) CONFIRMED. (c) numbers CONFIRMED; the step size is estimator dependent (0.05 to 0.16). (f) "settles at
0.10 to 0.14 on the right" REFUTED. (d) single lambda-mode reading NOT CONFIRMED (sign change along the characteristic).
First-line "not C^3 at P" REFUTED as wording; body wording suggested above. No endpoint is confirmed; the team may NOT
finish.
Addendum (same shift). The lead withdrew the request at 08:19Z (NOTES_FOR_TEAM) and keeps 13.16 out of the report on
the strength of an external referee answer (analysis 13.16 (g)). G66 was computed before I read that note; it agrees
with the decision. Two points of 13.16 (g) are checked by G66: (i) the invariant curve gamma = x* + beta y^2 with
beta = a_2(P)/(2 - A) = -0.0110 (marked "claim, not checked" by the lead) is CONFIRMED by the location of max |H''''|
off the axis (-0.0100 at y = 1, -0.0460 at y = 2 against -0.0110 and -0.0440); (iii) the cost factor 3A - g* = 0.704 is
A (3 - lambda), my remark (ii). The "decisive test" recorded in 13.16 (g) is the separating test above.

## G67 Final lead fixed-c_l fit fixc_c6f_m1.0e-03 (outer 2, iterate 250): audit in the G20 (b) set, both normalizations by band and strip, the y-axis evaluator floor, the first equal-budget free control, and SPEC v4.7 (2026-10-18T09:05Z)

Item: lead NOTES 08:17Z item 1 (result and reading) and item 2 (verifier first priority), 08:23Z (N_f and N_v by band and
for the strip, both shapes), 08:19Z (SPEC v4.7 proposed item, confirm or amend before the audit verdict).
Shape: work/c6/fixc_c6f_m1.0e-03_shape.npz, copied as runs/gen4/fixcf/fxm1o2i250_shape.npz (md5 equal), c_l fixed at
5.575362610641546. Comparison: c6f segment 1 final (c6fS1, c_l 5.57636243).
Method: my generator (code/gen_shape.py) and evaluator (code/vaudit.py: own differentiation, own full-plane inverse),
R = 7.652e6, between fit nodes, six configurations N 11250 q384, 16875 q384 / q512 / q768, 22500 q384 / q512 (the same six
on c6fS1); code/extra_checks.sh at N 11250 q384 (identity-free c_l, D14 centre relations, zeros); residual maps
(code/vresmap.py) at N 11250 q384 on r 6 to 12, theta < 0.6 and on r 2 to 10, theta 0 to pi/2, and at N 16875 q768 on
r 8 to 11, theta 0 to pi/2 (scratch/strip_nv.py, band_nv.py, yaxis_look.py). Normalizations: N_f = |W_1 rho_x| +
|W_2 rho_y| + |rho| (flux, the report's); N_v = |rho| + |X.grad rho| + |U.grad rho| (the lead's N4).

(a) Table, R/N_f maxima unless marked N_v; fixed fit first, c6fS1 second; J spread over all start angles.
  config       whole box (r, theta)        |X-P|<0.5 N_f / N_v    2-10 N_f / N_v       0.1-2     10-100 N_f / N_v    far N_v   J 0.03 / 0.01      h(P)-1
  N11250 q384  6.98e-7 (8.784, 0.308)      6.66e-7 / 1.87e-7      6.98e-7 / 5.20e-7    1.72e-7   4.37e-7 / 2.86e-7   1.13e-6   9.9e-7 / 1.12e-6   (+2.5e-7)
               2.28e-6 (8.466, 0.013)      2.28e-6 / 6.36e-7      2.28e-6 / 6.36e-7    1.54e-7   4.37e-7 / 2.80e-7   1.12e-6   3.08e-6 / 3.39e-6  (+1.7e-7)
  N16875 q384  6.70e-7 (8.321, 0.023)      6.70e-7 / 1.88e-7      6.70e-7 / 5.20e-7    1.72e-7   4.42e-7 / 2.86e-7   1.13e-6   1.03e-6 / 1.20e-6  +2.5e-8
               2.31e-6 (8.470, 0.013)      2.31e-6 / 6.46e-7      2.31e-6 / 6.46e-7    1.54e-7   4.41e-7 / 2.80e-7   1.12e-6   3.11e-6 / 3.46e-6  +3.2e-8
  N16875 q512  6.53e-7 (8.516, 0.022)      6.53e-7 / 1.83e-7      6.53e-7 / 5.32e-7    1.81e-7   4.48e-7 / 2.93e-7   1.15e-6   1.03e-6 / 1.20e-6  +2.5e-8
               2.42e-6 (8.470, 0.012)      2.42e-6 / 6.77e-7      2.42e-6 / 6.77e-7    1.62e-7   4.47e-7 / 2.89e-7   1.12e-6   3.11e-6 / 3.46e-6  +3.2e-8
  N16875 q768  1.22e-6 (9.382, 1.5692)*    6.70e-7 / 1.88e-7      1.22e-6* / 5.71e-7   1.88e-7   5.27e-7* / 2.92e-7  1.17e-6   1.03e-6 / 1.20e-6  +2.5e-8
               2.44e-6 (8.470, 0.012)      2.44e-6 / 6.83e-7      2.44e-6 / 6.83e-7    1.68e-7   4.46e-7 / 2.89e-7   1.15e-6   3.11e-6 / 3.47e-6  +3.2e-8
  N22500 q384  6.82e-7 (8.317, 0.023)      6.82e-7 / 1.91e-7      6.82e-7 / 5.20e-7    1.72e-7   4.46e-7 / 2.86e-7   1.14e-6   1.04e-6 / 1.21e-6  -1.7e-8
               2.33e-6 (8.463, 0.013)      2.33e-6 / 6.51e-7      2.33e-6 / 6.51e-7    1.54e-7   4.39e-7 / 2.80e-7   1.12e-6   3.12e-6 / 3.48e-6  -1.7e-8
  N22500 q512  6.83e-7 (8.515, 0.022)      6.83e-7 / 1.91e-7      6.83e-7 / 5.32e-7    1.81e-7   4.57e-7 / 2.93e-7   1.16e-6   1.04e-6 / 1.21e-6  -1.7e-8
               2.43e-6 (8.463, 0.012)      2.43e-6 / 6.80e-7      2.43e-6 / 6.80e-7    1.62e-7   4.49e-7 / 2.89e-7   1.13e-6   3.12e-6 / 3.48e-6  -1.7e-8
  * evaluator floor next to the y-axis, see (c). Lead scans (32768 x 640 / 24576 x 960): 2-10 6.77e-7 / 6.87e-7, 10-100
  4.43e-7, N4 2-10 6.04e-7 / 6.04e-7. CONFIRMED to 4 percent (N_f), 14 percent (N4 against my N_v, different sampling).
  100-1000: 6.9e-8 to 7.1e-8 on both shapes. Interior-start J spread (fixed fit, N16875 q512 and q768): 3.3e-7 at every
  shell below 1 (c6fS1 4.0e-7).

(b) Strip and band maps (N 11250 q384; map theta step 0.0033).
  region                               c6fS1 N_f / N_v (r, theta)             fixed fit N_f / N_v (r, theta)           ratio
  strip r 7.9-8.6, theta <= 0.08       2.28e-6 / 6.36e-7 (8.466, 0.013)       6.66e-7 / 1.87e-7 (8.312, 0.023)        0.29 / 0.29
  right of P r 8.6-9.4, theta <= 0.08  1.03e-6 / 2.92e-7 (8.606, 0.013)       4.06e-7 / 1.15e-7 (8.606, 0.010)        0.39 / 0.39
  r 8.2-9.4, theta 0.08-0.5            7.90e-7 / 2.17e-7 (8.784, 0.288)       6.98e-7 / 1.94e-7 (8.784, 0.308)        0.88 / 0.89
  r 2-6 (maxima on the x-axis side)    4.09e-7 (5.353, 0.013) / 4.45e-7 (4.657, 0.013)   5.16e-7 (5.703, 0.013) / 5.20e-7 (4.872, 0.013)   1.26 / 1.17
  r 6-10, theta > 1.4 (y-axis side)    5.43e-7 / 8.4e-8 (9.711, 1.558)        5.57e-7 / 8.5e-8 (9.711, 1.558)         1.03 / 1.01
  So the strip falls by the same factor 3.4 in N_f and in N_v, and the region right of P by 2.5 in both. The off-axis
  lobe at theta about 0.3 falls by 12 percent and becomes the N_f maximum on the coarsest grid. The x-axis side at r 2 to
  6 rises by 26 percent (N_f) / 17 percent (N_v), and there the fixed fit has its 2-10 N_v maximum (5.2e-7 at r 4.87). The
  y-axis side near r 10 and the far field rise by 1 to 3 percent.
  Lead 08:23Z "the factor 3.6 is in N_f only": REFUTED as stated. In the strip the fall is the same in N_v. The N_v (N4)
  maximum of the 2-10 band falls by only 12 to 21 percent because it moves from the strip to the x-axis at r about 4.9,
  where the fixed fit is worse than the free fit. "The fixed-c_l fit differs from the free fit mainly in that strip":
  CONFIRMED (and right of P, factor 2.5). "Both maxima sit in the strip ... r 8.51, theta 0.022": CONFIRMED for N_f at
  q512 (8.515, 0.022); the fixed fit's 2-10 N_v maximum is on the x-axis at r about 4.9, not in the strip.

(c) The q768 rows. At N 16875 q768 the fixed fit's whole-box N_f maximum is 1.22e-6 at r 9.382, theta 1.5692, the
  evaluation column nearest the y-axis (pi/2 - theta = 0.00164; my evaluation grid has Nt = 4 (M + 1) angles, so this column exists only with M 959; with
  M 639 the nearest column is at 0.00245, with M 479 at 0.0033); 10-100 5.27e-7 at
  the same column. The y768 map shows that this is my evaluator's floor, not the fit: on the y-axis itself, where R = 0
  exactly by symmetry, my R is -1.9e-9 / -3.3e-10 / +2.6e-9 / +5.5e-10 / -1.8e-9 at r 8.50 / 9.01 / 9.38 / 9.74 / 10.49
  (rho there is -2e-12: the cancellation floor of the odd sine series at theta = pi/2), and at pi/2 - theta = 0.00164 the
  computed R is the same number to 0.1e-9 (2.70e-9 at r 9.382) while N_f is only 2.2e-3. R minus its on-axis value gives
  R/N_f of about 5e-8 there. The next columns (0.0033, 0.0049) give 4.1e-7 and 3.3e-7, and the y-axis side maximum
  beyond 0.006 is 5.65e-7 (r 9.735). The same floor is on c6fS1 (same map: on-axis |R| up to 2.3e-9, 7.55e-7 at the
  nearest column, r 9.472; 5.42e-7 beyond 0.006). It is a property of my evaluator, common to both shapes.
  Consequence for earlier rows: any q768 value quoted at theta = 1.5692 is floor limited. The c6fS1 q768 whole-box value
  is the strip (2.44e-6) and is unaffected.

(d) Centre, h(P), c_l, zeros (extra_checks N 11250 q384; traces).
  D14: E -9.6e-9, D2 1.5e-8 (relative -4e-8 / 3e-8) on [1e-3, 0.02]; lead -9.4e-9 / 1.47e-8. CONFIRMED.
  h(P) - 1: +2.5e-8 (N 16875), -1.7e-8 (N 22500), equal to c6fS1's at the same grids (+3.2e-8, -1.7e-8), i.e. my grid
  error; N 11250 gives +2.5e-7 on both shapes and is not quoted (G42 (a)). Lead -8.1e-9 / -4.9e-9: consistent.
  c_l: identity value from my psi_xy(0) 5.5753626075 (N 16875 q512 and N 11250), against the fixed input 5.5753626106:
  -3.2e-9. My inverse c 15.7260878223 against 3 c_l - 1 = 15.7260878319. As a test of the fit (SPEC v4.7 (4)) CONFIRMED
  to 3e-9. Identity-free root of h(P) = 1 with rho fixed: 5.575362614 (+3.4e-9 from the input; dh/dc_l 1.079). On c6fS1
  the same root is 5.576362482 (+5.4e-8 from its identity value). So h(P) = 1 holds at c_l 5.5753626 on this fit and at
  5.5763624 on the free fit: the identity-free condition is met by both fits, 1e-3 apart, and does not select c_l. It is a
  consistency test along the soft direction, not a determination.
  Zeros: one W_1 zero on the x-axis at 8.6000682 (x* 8.6000686); W_2 / y on the y-axis at least 5.57557 > 0; no open
  quadrant cell with both components changing sign; the same as c6fS1.
  B_3 (my estimator, N 16875 q512): ibp 0.2980 [0.2955, 0.2998], orig 0.2953 [0.2721, 0.3071]; c6fS1 at q768 0.2982
  [0.2956, 0.3001] / 0.2936. Same to 0.002.

(e) First equal-budget free control (G63; scratch/c6fs2_follow.sh). The free c6f segment 2 restarts from c6f_seg1 with a
  new linearization, the same grid and checks, as the fixed fit did from c6f_seg1 + d t. At LSQR iterate 250 of each
  (N 16875 q384):
    c6f_seg1 (start)             2.31e-6 strip   J 3.11e-6 / 3.46e-6   10-100 4.41e-7   rms 2.39e-8   objective 7.653e-6
    free segment 2, it 250       1.53e-6 strip   J 2.86e-6 / 3.21e-6   10-100 3.83e-7   rms 2.20e-8   objective 7.532e-6
    fixed -1e-3, it 250          1.41e-6 strip   J 2.01e-6 / 2.31e-6   10-100 4.62e-7   rms 2.40e-8   objective 8.765e-6
    fixed -1e-3, outer 1 it 500  8.99e-7         J 1.35e-6 / 1.57e-6   10-100 4.28e-7   rms 2.22e-8   objective 8.574e-6
    fixed -1e-3, outer 2 it 250  6.70e-7         J 1.03e-6 / 1.20e-6   10-100 4.42e-7   rms 2.18e-8   objective 8.474e-6
  N 22500 q512: start 2.43e-6, free it 250 1.66e-6, fixed it 250 1.50e-6 (factors 1.47 / 1.62); J 0.01 3.23e-6 /
  2.32e-6; 10-100 4.00e-7 / 4.66e-7. Strip map (N 11250 q384) of the free it 250: N_f 1.52e-6 / N_v 4.25e-7 (r 8.536).
  At equal budget (250) the free continuation lowers the strip by a factor 1.51 and the fixed fit by 1.65: most of the
  first fall is the new LSQR segment, not c_l. The fixed fit is ahead in J (2.31e-6 against 3.21e-6) and behind in the
  10-100 band and in rms. The free iterates 500 and 750 (about 09:20Z and 09:55Z) decide the attribution at the fixed
  fit's final budget; until then "the fall from 2.4e-6 to 6.8e-7 is due to c_l" is OPEN.

(f) Verdict on the lead reading (NOTES 08:17Z item 1: "the max-norm candidate for the report becomes the fixed-c_l fit
  and its continuation, if your recomputation agrees").
  - The recomputation agrees: N_f whole box 6.5e-7 to 7.0e-7 on five of my six configurations and on the sixth outside
    the y-axis floor column; N_v whole box 1.13e-6 to 1.17e-6 (far field, r about 3.5e4), at most 5.7e-7 for r <= 1000;
    J 1.0e-6 / 1.2e-6 (2.9 times below c6fS1), interior-start J 3.3e-7; h(P) - 1 at my grid error; identity to 3e-9.
    CONFIRMED as numbers.
  - The residual level of G20 (b1) ("about 1e-6 in both normalizations, including next to P") is reached on this one
    basis and domain: N_f <= 7e-7, N_v <= 1.2e-6 (far field) and <= 5.7e-7 for r <= 1000. This is the first audited
    shape that meets it.
  - Not yet a YES endpoint. Open: (1) the equal-budget free control at iterates 500 and 750 ((e)); (2) the resolution
    study at the same c_l with systematic improvement (G20 (b1)) and J decreasing (G20 (b3)): fixc_c6d_m1.0e-03,
    fixc_c6b_m1.0e-03; (3) the domain study at the same c_l (numerics fxd300, fxd90, fit convention); (4) the candidate
    itself if it is the continuation fixc_c6f_m1.0e-03_s2 (this audit is repeated on it); (5) the report text for the
    choice of c_l (SPEC v4.7 below).

(g) SPEC v4.7 (proposed item "Candidate at a fixed c_l"): CONFIRMED with amendments.
  A0 Entry test. "a lower whole-box maximum than the free L2 fit in N_f": the free fit must be the free continuation with
     the same LSQR budget from the same start (here c6f segment 2 at the fixed fit's iteration count), measured by the
     verifier at the G20 (b) configurations; otherwise the report says that the budgets differ. (e) shows why: at 250
     iterations most of the fall is budget.
  A1 "a whole-box maximum in N_v that is not higher": on this candidate the whole-box N_v maximum is the far field
     (r about 3.5e4), 0.9 to 2.7 percent above c6fS1 at equal configurations, which is inside the spread of my
     configurations (3 percent). As written the condition fails. Proposed: "not higher by more than the spread over the
     verifier's configurations, for r <= 1000 and for the far field separately", plus "and a characteristic defect J
     that is not higher" (G20 (b3)).
  A2 Item (2): the report lists every fixed c_l that was tried with its maxima and objective, including undecided ones
     (fixc_c6b_560 at 5.60), so the max-norm selection is visible.
  A3 Item (5): the report says that the identity-free condition h(P) = 1 holds at the fixed value on the candidate (3e-9)
     and at the free value on the free fit (5e-8), so it does not determine c_l at the 1e-3 level.
  A4 Item (3): the resolution study includes J at each basis; the domain study is read by the rule fixed at 08:17Z (fit
     convention, interior bands within a factor 1.5 of fixc_c6d_m1.0e-03, h(P) - 1 below 1e-7).
  A5 Quoted maxima exclude evaluation points within the evaluator floor next to the y-axis ((c)); every such exclusion is
     stated.
  Items (1) and (4) as proposed.

Verdict: numbers of the fixed-c_l fit CONFIRMED; first shape at the G20 (b1) residual level on one basis and one domain;
attribution of the fall to c_l OPEN (equal-budget control at 250 favours budget); "factor 3.6 in N_f only" REFUTED;
q768 y-axis value is an evaluator floor; SPEC v4.7 CONFIRMED with amendments A0 to A5. No endpoint is confirmed; the
team may NOT finish.

## G68 Lead NOTES 09:05Z (fixc_c6b_560 free part, slot 2 order, reading rules, SPEC v4.7 extension), draft section 4 v3, the inverse-error row, and the numerics closure row of 09:04Z (2026-10-18T09:14Z)

Items: lead NOTES_FOR_TEAM 09:05Z items 1 to 4 and 08:38Z item 2 (check the inverse-error row); lead
notes/final_sec4_v3_text.md (09:02Z, not yet in FINAL_REPORT); numerics NOTES_FOR_LEAD 09:04Z (far-field truncation error
of the fit's own inverse). Method: reduction of the numerics json and table files; my audit logs and json of G67 (six
configurations per shape, per-band maxima and the per-band elliptic residual relE = sup|E| / sup|d_x rho| that vcand.py
records); the candidate's shape file (work/c6/fixc_c6f_m1.0e-03_shape.npz, copy runs/gen4/fixcf/fxm1o2i250_shape.npz);
the lead's fixed-fit log work/c6/fixc_c6f_m1.0e-03.log.

(a) Inverse-error row (section 4.5; lead 08:38Z item 2). runs/ray/c6d_far_BP.json (P-clustered fine rules, 8 far nodes of
  c6d_seg1): |dU| at r = 100 is 4.91e-9 to 4.95e-9, at r = 300 1.47e-8 to 1.48e-8 (recomputed from U_ray - U_lead; equal to
  the stored dU), relative 7e-11 to 1.1e-9, impact at most 6.4e-11. runs/ray/vary_table.txt: at the far nodes the three
  P-clustered rules (fineP, fineP005, baseP) and the 16384-angle midpoint rule agree (4.9e-9 to 5.8e-9 at r 100, 1.4e-8 to
  1.5e-8 at r 300); the unclustered rules scatter up to 3.4e-6, as stated in NUM_REPORT 3.17 (ix). Together with G65 (c)
  (near P 9.9e-10 / 1.0e-9, 0.5 to 2.5 from P 4.29e-8, r 20 1.0e-9, maximum impact 3.0e-9 at (8.551, 1.994)) the row text
  "9e-10 within 0.5 of P, 4e-8 within 0.5 to 2.5 of P, 1e-9 at r = 20, 5e-9 at r = 100 and 1.5e-8 at r = 300 (all eight
  far nodes); the implied change of the normalized residual is at most 3e-9" is CONFIRMED. Qualifiers that must stay in
  the text: measured on the free fit c6d_seg1 (375 x m <= 100) and its export with the formula density to 1e4 L, not on
  the candidate; "converged" at r >= 100 means agreement of the P-clustered rules with the 16384-angle midpoint rule.
  The draft 4.1 sentence "a third evaluator reproduces the velocity and the residual at sample points" is true of
  c6d_seg1 only; it needs "on the free fit" or the same 51-node check on the candidate.

(b) Closure row of the fit's own inverse (numerics 09:04Z). Reduction of runs/ray/dom300f_table.txt and dom100f_table.txt:
  the numbers are as posted, with one label to correct. The column "impact within 0.5 of P" quotes the maximum over 0.5
  to 2.5 from P (2.68e-8 at 333 L, 8.14e-7 at 111 L); within 0.5 of P the maxima are 2.23e-8 and 6.77e-7. The ratio
  111 L / 333 L of the impact is 30 (next to P), 30 (r 20), 31 (r 100) and 35 (r 300): from two radii this is an exponent
  3.1 to 3.2 per factor 3. The values quoted for 1000 L (1e-9 next to P, 7e-9 at r 20 to 300) are an extrapolation from
  two radii, not a measurement; the direct measurement on c6d_seg1 in the fit convention is still running.
  Consequences. (i) None for the audited residuals of the candidate and the free fit: my evaluator generates rho from the
  formula and inverts to 7.652e6 (1e6 L), so the numbers of G67 and of section 4.4 are canonical residuals of the trial;
  the closure only affects how closely the fit's own objective represents the canonical problem. (ii) For the domain
  columns: at the 51 nodes the canonical residual of the 111 L fit at r 20 to 300 is set by the closure (6.1e-6 to 7.0e-6
  against 4.6e-8 to 1.8e-7 in the fit convention), and at 333 L the closure term (2.0e-7) equals or exceeds the fit
  convention residual there. The domain columns therefore test whether c_l and the interior residual depend on the box
  in the closed problems; they are not residuals of the domain fits under the canonical velocity law. The report text
  of 4.4 already says the domain fits are bounded-domain fits and not admissible trials; it should add this sentence
  with the two numbers.

(c) Lead 09:05Z item 1 (fixc_c6b_560 freed at c_l 5.60). Recorded as the lead's observation; my fixcb_follow audit of the
  free part runs at its end (about 10:20Z). Two consequences for the text, already true on the lead's numbers.
  (i) The free formulation moves c_l by less than 1e-5 in 1000 LSQR iterations from 5.60, while the objective falls by a
  quarter. So on these bases a free fit keeps the c_l of its start to within the budget, and the agreement of the free
  branch to 2.5e-6 in c_l over 215 to 375 radial functions (section 4.4 table) is the c_l of one start (c4_r1) carried
  through one lineage. The draft's "the six-digit values label computed fits" is right; nowhere should the free fit's
  5.5763624 be read as selected by the L2 objective.
  (ii) The Q rule of analysis 13.17 (c) uses Q(244) = 1.97, the objective of the fixed part at its end. The free part
  takes the same c_l to 1.45 m0 and is still falling by about 10 percent per 250 iterations, so Q(244) is not a converged
  reference. Under the rule's own "still falling by more than 2 percent per 250 iterations" clause any comparison with it
  is undecided until a 244 fit at 5.60 stops falling. The draft 4.3 sentence "reached 1.97 times the objective of the free
  fit in 3 h and was still falling" should add "and 1.45 times after 1000 further iterations in the free formulation at c_l
  5.59999 (still falling)".

(d) Lead 09:05Z items 2 and 3 (slot 2 order and reading rules).
  - (b) fxfr drift rule. The rule covers |drift| < 1e-4 and drift >= +3e-4. It does not cover 1e-4 <= drift < 3e-4 or
    drift <= -1e-4. Proposed completion: in those cases the drift is reported as measured, the reading is undecided,
    and the interval contains the start and end values. Since (c) (i) gives a rate below 1e-5 per 1000 iterations at the
    244 level, |drift| < 1e-4 is the expected outcome. It shows that the free solver does not resolve a slope within the
    budget; it does not show that the objective has none. The report should word it that way.
  - Candidate choice among all fits (SPEC v4.7 extended). Conditions needed: (1) the amendments A0 to A5 of G67 (g) (equal
    LSQR budget for the free comparison or a stated difference, N_v tolerance equal to the configuration spread with
    r <= 1000 and the far field separate, J not higher, every fit tried listed, h(P) = 1 not used to select, the y-axis
    floor exclusions stated); (2) the chosen fit carries its own resolution rows and domain columns at its own c_l before
    it can be the candidate (otherwise the selection picks a fit that has not been through G20 (b1) to (b3)); (3) all
    maxima compared at the same verifier configurations; (4) the report states the number of fits compared, since the
    minimum over many fits is a selection; (5) for a reweighted fit (rw) the objective row of the table names the
    weighted objective, and its L2 objective is given as well.
  - (c) rw rule. "If rw reaches a whole-box N_f maximum <= 1.0e-6 with N_v not higher, the strip is a weighting effect
    at the free c_l, and rw becomes the candidate by the same rule" is inconsistent with the rule it cites: the extended
    rule picks the lowest whole-box N_f maximum, and the fixed-c_l fit has 6.5e-7 to 7.0e-7 (G67), so rw at 9e-7 would
    not be chosen. Proposed: "rw at <= 1.0e-6 shows that the strip is not forced by the free c_l; the candidate is then
    chosen by the extended rule". The reading "weighting effect" also needs the other bands (r 2 to 6 next to the x-axis,
    10 to 100, far N_v) and J not higher than the free fit's, since a reweighted fit can move the maximum elsewhere.

(e) Draft section 4 v3 (notes/final_sec4_v3_text.md). Checked against G66, G67 and the shape file.
  E1 Formula and class (4.1 third bullet, 4.2). CONFIRMED against the shape file and my generator: 375 radial functions
     per angular term (376 clamped B-splines of polynomial degree 7, 384 knots, first dropped so b_m(0) = 0), m = 0 to 150,
     T of degree 5 (6 coefficients), r_0 = 0.02, all interior knots simple, 56632 coefficients = 1 + 151 x 375 + 6, k and L
     to the stored digits; the H formula, the Cartesian form of the fractional term, beta = p_3 - 6 = 2/(2 c_l - 1) =
     0.197, the class C^(4,beta)_loc, H(0) = 0, analyticity of each angular term at 0, and the far-field expansion with
     remainder O(r^(2k-2)) (the r^-2 terms from log(1 + u^2), chi^(m-1) and s^(p_3/2) are smaller). One unit to add:
     "spacing 0.0165 next to P" is in r (6.3e-4 in q).
  E2 4.2 "The objective fell from 8.77e-6 to 8.47e-6": the fixed fit's start objective is 9.707e-6 (lead log, start and
     outer-1 linearize events); 8.765e-6 is the first check (outer 1, iterate 250). Should read "from 9.71e-6 (start)
     to 8.47e-6 in 750 LSQR iterations over two linearizations".
  E3 4.2 values [V]: x* = 8.6000686 (stored) and my W_1 zero 8.6000682: CONFIRMED to 1e-6. h(P) - 1: +2.5e-8 / -1.7e-8 at
     my two finest grids, equal on the free fit at the same grids (+3.2e-8 / -1.7e-8), so |h(P) - 1| < 3.5e-8 on both, at
     my grid error; the lead's -8.1e-9 / -7.1e-9 are inside it. Centre jet: E -9.6e-9, D2 1.5e-8 CONFIRMED. Zeros: one W_1
     zero on the closed first quadrant axes and no open quadrant cell with both components changing sign, on my N 11250 q384
     grid of r in [7.652e-4, 7.652e6] (sampled, not a validated exclusion; G67 (d)).
  E4 4.3 identity [V]: my c = psi_xy(0) = 15.7260878224, (1 + c)/3 = 5.5753626075 against 5.5753626106: -3.2e-9 absolute
     (5.7e-10 relative). Identity-free root of h(P) = 1 at fixed rho: 5.575362614 (candidate) and 5.576362482 (free fit);
     these numbers belong in the paragraph that says h(P) = 1 does not discriminate.
  E5 4.3 table [V] (my six configurations, ranges; candidate first, free fit second):
       max N_f, strip next to the x-axis left of P   6.5e-7 to 6.8e-7      2.28e-6 to 2.44e-6
       max N_v, 2 <= r <= 10                         5.20e-7 to 5.71e-7   6.36e-7 to 6.83e-7
       max N_f, 0.1 <= r <= 2                        1.72e-7 to 1.88e-7   1.54e-7 to 1.68e-7
       max N_f, 10 <= r <= 100                       4.37e-7 to 4.57e-7   4.37e-7 to 4.49e-7  (5.27e-7 at q768 is the y-axis floor)
       max N_f, 100 <= r <= 1000                     6.9e-8 to 7.1e-8     6.7e-8 to 7.0e-8
       max N_f, r >= 1000                            1.86e-7 to 1.87e-7   2.72e-7 to 2.75e-7
       max N_v, far field (r about 3.5e4)            1.13e-6 to 1.17e-6   1.12e-6 to 1.15e-6
       J spread, eps 0.03 / 0.01                     9.9e-7 to 1.04e-6 / 1.12e-6 to 1.21e-6    3.08e-6 to 3.12e-6 / 3.39e-6 to 3.48e-6
       h(P) - 1                                      +2.5e-8 / -1.7e-8    +3.2e-8 / -1.7e-8
     The lead's r >= 100 N_f row (7.3e-8 / 7.2e-8) is the 100 to 1000 band; for r >= 1000 my N_f maxima are 1.9e-7 and
     2.7e-7 (the far-field maxima of N_f sit at r about 3.5e4, as for N_v).
  E6 4.4 candidate by region [V] (N_f / N_v, six configurations):
       |X - P| < 0.5      6.5e-7 to 6.8e-7 / 1.83e-7 to 1.92e-7
       r <= 0.1           1.6e-8 to 1.1e-7 / 3.4e-8 to 2.4e-7 (grows with N and q on both shapes, maxima next to the
                          y-axis at r about 0.01: evaluator floor, not quoted as the trial's)
       0.1 <= r <= 2      1.72e-7 to 1.88e-7 / 3.36e-7 to 3.66e-7
       2 <= r <= 10       6.5e-7 to 7.0e-7 / 5.20e-7 to 5.71e-7
       10 <= r <= 100     4.37e-7 to 4.57e-7 / 2.86e-7 to 2.94e-7
       100 <= r <= 1000   6.9e-8 to 7.1e-8 / 2.83e-7 to 2.94e-7
       r > 1000           1.86e-7 to 1.87e-7 / 1.13e-6 to 1.17e-6
     grid: my evaluator, r in [7.652e-4, 7.652e6] with N = 11250 to 22500 log-radial points, q = 384 to 768 angular
     points on the quarter, M = 479 to 959, between fit nodes; the q768 column next to the y-axis excluded (G67 (c)).
     Elliptic residual [V]: E = -Lap psi - d_x rho is zero by construction for the modal inverse; what I measure is the
     consistency of my psi with its own re-differentiation (8th-order differences in log r, spectral in theta):
     sup|E| / sup|d_x rho| per band 1.5e-6 / 3.7e-7 / 9.8e-8 on 1 <= r <= 10 at N 11250 / 16875 / 22500 (falls with N: the
     differentiation error next to P), at most 2.3e-9 for r >= 10, 1.4e-8 to 6.1e-8 on 0.01 <= r <= 1 and up to 3.2e-4 on
     r <= 0.01 (rises as N^2: round-off of the second difference where psi ~ r^2). The same on the free fit to 10 percent.
     Quote it as a check of the evaluator's inverse, not as a property of the trial.
  E7 4.1 second bullet "larger by a factor 3.6 in N_f and [V] in N_v, in a strip ... Away from that strip both pairs are at
     the same level": [V] is 3.4 (G67 (b), strip 6.36e-7 against 1.87e-7). "Away from that strip ... the same level" is
     not accurate. Measured: right of P (r 8.6 to 9.4, theta <= 0.08) the free fit is higher by 2.5 in both
     normalizations; J by 3.0 (eps 0.03) and 2.9 (0.01); next to the x-axis at r 2 to 6 the candidate is higher by 1.26
     (N_f) / 1.17 (N_v), and on 0.1 <= r <= 2 by 1.12 (N_f); the far N_f is lower on the candidate (1.9e-7 against
     2.7e-7); elsewhere within 12 percent. Suggested: "Its maximum residual is larger by a factor 3.4 to 3.6 (both
     normalizations) on the x-axis side left of P and by 2.5 right of P, and its characteristic defect J by 3; next to
     the x-axis at r 2 to 6 the candidate is higher by up to 26 percent; elsewhere the two agree within 12 percent." Also
     add the budget qualifier until the c6f segment 2 control is in: the two fits differ in LSQR budget (750 iterations
     after the move for the candidate).
  E8 4.8 last sentence "That comparison depends on the normalization (factor 3.6 in N_f, 1.12 in the normalization
     c_l |X| |grad rho| + |rho| [V for N_v])": REFUTED as stated. Region by region the strip factor is the same in N_f
     and N_v (3.6 and 3.4). What depends on the normalization is where the whole-box maximum sits: in N_f next to P,
     where the candidate is lower by 3.4; in N_v in the far field next to the y-axis (r about 3.5e4), where the two agree
     within 3 percent. The 1.12 is the ratio of the 2-10 band maxima in the lead's scan, whose N_v-type maximum moves from
     the strip to the x-axis at r 4.9. The normalization c_l |X| |grad rho| + |rho| is not defined anywhere else in
     section 4; use only N_f and N_v. Suggested: "The comparison is between whole-box maxima. In N_f the maximum sits next
     to P, where the fixed-c_l fit is lower by a factor 3.4; in N_v it sits in the far field next to the y-axis, where the
     two fits agree within 3 percent. So the choice of the representative value inside the interval depends on the norm
     in which the maximum is taken [and on the iteration budget], not on a property of the equation."
  E9 4.8 layer sentence. "If a solution has a layer of the form |x - gamma(y)|^lambda along that characteristic, the
     exponent is lambda = rho_y(P)/(2 c_l - 1), about 2.93, and such a layer is C^(2, lambda - 2) but not C^3" is correct
     as a conditional (lambda = g*/A with g* = q(x*) = rho_y(P), G66 (a), (b)). Placed after the measured step it reads as
     support. Add: "A single layer of this form keeps the sign of the step along the curve; the measured step changes
     sign near y = 0.5, so the fits' feature is not of this form at leading order."
  E10 4.1 remark B_3 "[V: candidate, free fit] and 0.297 to 0.307 over all fits": my values are 0.2980 (ibp) / 0.2953
     (original form) on the candidate and 0.2982 / 0.2936 on the free fit (G67 (d)). My original-form values lie below
     0.297; the lead's original-form value on c6f_seg1 is 0.2999 against my 0.2936 (the two implementations differ by 2
     percent). Suggested range: "0.294 to 0.307 over the two estimators and all fits".
  E11 4.3 "Fits of comparable residual quality differ in c_l by at least 1e-3": suggested "fits of comparable residual
     quality exist at c_l values 1e-3 apart".
  E12 4.7 adversarial checks: polynomial states are not mentioned. Suggested addition: "Polynomial states: x^2 y and every
     polynomial density grow at least like r^3; the trial grows like r^k with k = 1/c_l = 0.179 (4.2), the degree required
     by R2."
  E13 4.4a and 4.4b. CONFIRMED: R/rho -> h(P) - 1 at P; backward characteristics off the axis approach P along the slow
     eigendirection (eigenvalues A = 2 c_l - 1 = 10.15 along the axis and h(P) = 1 across it), so the time to the cutoff
     is log(1/eps)/h(P) + O(1) and the term (h(P) - 1) log(1/eps)/h(P) follows.
  E14 4.3 identity paragraph. The disclosure is adequate as written ("what is chosen ... is the point at which the family
     of consistent pairs is sampled"). With E4's numbers it meets PROMPT section 1 ("c_l must not be chosen independently")
     in the sense stated there; the text must keep saying that c_l was set by the fit design (free value minus 1e-3) and
     reached consistency through rho.

Verdict: (a) inverse-error row CONFIRMED with qualifiers. (b) closure row CONFIRMED as measured at 111 L and 333 L, label
corrected, the 1000 L values are an extrapolation; no effect on the audited residuals; domain columns to be described as
closed-problem tests. (c) recorded; Q(244) is not a converged reference. (d) drift rule incomplete (completion proposed);
SPEC v4.7 extension needs five conditions; rw rule inconsistent with the extended rule. (e) draft 4 v3: [V] values supplied
(E3 to E6, E10); E2, E7, E8 corrections; E8 REFUTED as stated; E9 and E12 additions. No endpoint is confirmed; the team may
NOT finish.

## G69 c6f segment 2 at iterates 500 and 750 against the final fixed-c_l fit (M2 of the 09:16Z rule), J on resolved label sets, dom90 segment 1, the closure row checked directly, the 244 free part at 5.60, and the six section 4 v3 wordings (2026-10-18T10:51Z)

Requests answered: lead NOTES_FOR_TEAM 10:04Z item 5 (measure c6f_seg2_shape.npz; decides items 2 and 3), 10:24Z item 2
(the six replacement wordings), 09:05Z item 1 (244 free part); numerics NOTES_FOR_LEAD 09:18Z items 1 and 2 and 09:53Z.
Throughout: "candidate" is fixc_c6f_m1.0e-03 at its end (outer 2, iterate 250; my tag fxm1o2i250; c_l fixed at
5.575362610641546), "free iterate 750" is c6f segment 2 at its end (c6fs2i750). Lead numbers are marked as such.

(a) dom90 segment 1, fit convention (numerics 09:18Z item 1). Method: my generator with the lead's two-term closure at
    R_shape 100 (Rc = 765.2, fit radius 688.68) and my evaluator (k_self), N11250 q384 and N16875 q512, against c6dS1 at
    the same configurations (formula to 7.652e6). Result (dom90 / c6dS1): near P (|X-P| < 0.5, the whole-box maximum inside
    the fit radius) 2.713e-6 / 2.424e-6 and 2.729e-6 / 2.409e-6 (1.12x and 1.13x); 10 <= r <= 100 7.47e-7 / 7.54e-7 and
    8.38e-7 / 9.49e-7; 0.1 <= r <= 2 1.98e-7 / 2.17e-7 and 2.03e-7 / 2.22e-7; c_l 5.5763667 against 5.5763622 (+4.5e-6);
    J(0.01) 2.20e-6 / 1.25e-6 and 2.30e-6 / 1.43e-6 (1.6x to 1.8x). In the clo1e3 and clo1e4 conventions (closure at 1000 and
    10000 shape units) the dom90 fit has 3.9e-5 and 4.0e-5 next to P, as for dom100 and dom300 in G65: a bounded-domain fit is
    small only in its own convention. Verdict: numerics 09:18Z item 1 (2.75e-6, 1.13x, 10-100 1.04x, c_l +4.6e-6) CONFIRMED
    on my evaluator. The 07:23Z rule does not read J; J is 1.6x to 1.8x higher on dom90 than on c6dS1 and the report should
    give it next to the rule's three numbers. The rule is applied after segment 2.

(b) c6f segment 2 at iterate 500 (free continuation from c6f segment 1, equal LSQR count with fxm1o1i500). Method: as
    G67 (c6fs2_follow.sh), shape copied at the lead's check line (md5 e902ca30...). Result, whole-box N_f maximum, all of
    it in the strip next to the x-axis left of P or at its edge (free / fixed): iterate 250 1.529e-6 / 1.405e-6 (N16875 q384)
    and 1.658e-6 / 1.504e-6 (N22500 q512), ratio 1.09 and 1.10; iterate 500 1.293e-6 / 8.99e-7 and 1.278e-6 / 9.84e-7,
    ratio 1.44 and 1.30. On the resmap (N11250 q384), strip maximum: start (c6fS1) 2.276e-6; iterate 250 1.515e-6 / 1.360e-6;
    iterate 500 1.242e-6 / 8.95e-7; fixed iterate 750 6.66e-7. Per 250 iterations the free strip falls by 0.67 then 0.82,
    the fixed by 0.60 then 0.66 (then 0.74 after the relinearization at 500). Free c_l 5.5763626 -> 5.5763629 (it 500),
    J(0.01) 3.21e-6 -> 2.01e-6 (fixed 2.31e-6 -> 1.57e-6). Far-field N_v equal to 1 percent (1.10e-6 to 1.12e-6 both).
    Verdict: at equal LSQR count the gap opens from 1.1x at 250 to 1.3x to 1.4x at 500; M2 (iterate 750) in (e).

(c) Free part of fixc_c6b_560 (244 x m100 basis, freed at 5.60 after 3 h fixed; lead NOTES 09:05Z item 1). Method: shape
    copied after "free solve done" (md5 b919931b...), audited at N11250 q384 and N16875 q512 (k_self) and extra_checks.
    Result: c_l 5.5999914 (identity on my inverse 5.599991440, -3.4e-9 from the stored value; root of h(P) = 1 at fixed rho
    5.599991516, +7.6e-8): c_l moved 8.6e-6 over the free part. Near P 6.589e-6 / 6.514e-6 (fixed part 8.687e-6 / 8.754e-6;
    c6bS1 at 5.5763632 3.248e-6 / 3.303e-6, 2.0x); whole box (2-10) 6.59e-6 / 6.51e-6 against c6bS1 4.64e-6 / 4.95e-6 (1.42x,
    1.32x); 10-100 4.56e-6 / 4.58e-6 against 3.20e-6 (1.43x); J(0.01) 6.81e-6 against 3.29e-6 (2.07x); N_v whole box 1.84e-6
    against 1.37e-6 / 1.45e-6. D14 on [1e-3, 0.02]: E -1.3e-9, D2 -1.3e-8. Zeros: one zero of W_1 on the x-axis (8.6191274),
    W_2/y on the y-axis at least 5.6002, no open-quadrant cell with both components changing sign. Verdict: the lead's
    "c_l kept to 9e-6 over 1000 iterations" CONFIRMED (8.6e-6). The identity and h(P) = 1 hold at 5.60 as at 5.5764 and
    5.5754 (A3 now covers three values over 2.5e-2). The free formulation does not move c_l at this budget, so the free c_l
    of every fit is inherited from its start (G68 (c)); at the 244 level the 5.60 fit is 1.3x to 2.1x above c6bS1 in every
    measured quantity after 3 h fixed plus 1000 free iterations, and still falling.

(d) Closure row, direct check (numerics 09:18Z item 2). Method: new code/clo_diff.py. One shape, two fields on the same grid
    (N11250 q384, R 7.652e6): A from the formula to R, B with rho replaced by the two-term exterior extension beyond
    R_shape = 1000 L (the fits' inverse convention); both evaluated by my inverse with c_l from the identity on each field.
    Inside 1000 L the densities agree, so R_B - R_A is the closure's effect; it is split into the velocity part
    (U_B - U_A).grad rho at fixed c_l (the fixed-c_l fit's convention) and the c_l part. Maxima over the open first quadrant
    (all grid points, axes excluded), c6dS1 / candidate fxm1o2i250:
      c_l shift from the identity: +3.44e-9 / +3.39e-9.
      max |U_B - U_A|: 9.4e-8 / 9.3e-8 within 0.5 of P; 2.1e-7 at 10-20; 1.0e-6 at 20-100; 3.1e-6 / 3.1e-6 at 100-300;
      1.0e-5 at 300-1000 (numerics: 9.2e-8, 2.0e-7 at r = 20, 1.0e-6 at 100, 3.0e-6 at 300).
      |X-P| < 0.5: total N_f 6.9e-9 / 6.8e-9, N_v 2.1e-9 / 2.1e-9; velocity part N_f 5.1e-9 / 5.1e-9, N_v 1.6e-9 / 1.5e-9.
      0.5 <= |X-P| < 2.5: total N_f 6.9e-9 / 6.8e-9, N_v 4.5e-9 / 4.5e-9; velocity part N_v 4.0e-9 / 4.0e-9.
      2 <= r < 10: velocity part N_f 1.0e-8 / 1.0e-8, N_v 3.3e-9 / 3.2e-9 (the total, 6.9e-9 / 6.8e-9, peaks at r 9.11, theta 0.0033).
      10 <= r < 1000: N_f at most 6.1e-9 / 6.0e-9 (velocity part 9.1e-9 / 9.0e-9 at 10-20), N_v 1.6e-8 to 2.0e-8 (2.0e-8 at
      300-1000, both shapes).
      0.1 <= r < 2: below 6e-10 in both normalizations.
      With k_self on field B the candidate values change by 1.5 percent.
    Relative to the candidate's residual (band maxima, G67): next to P 1.0 percent (N_f) and 1.1 percent (N_v); at 2-10
    1.5 percent (velocity part, N_f); at 10-1000 up to 6 percent (N_f, 300-1000) and 7 percent (N_v, 300-1000).
    The numerics' "impact" is |dU.grad rho| / D at their sample points (src/raycheck.py line 401), with D the lead
    export's normalization: their "lead |R|/D" within 0.5 of P on c6d_seg1 is 6.82e-7, which is my N_v maximum there
    (6.78e-7; my N_f maximum is 2.42e-6). So their row is the velocity part in N_v. Their values against mine (N_v,
    velocity part): next to P 2.3e-9 / 1.6e-9; 0.5-2.5 3.1e-9 / 4.0e-9; r = 20 to 300 1.3e-8 / 1.6e-8 (my band maxima
    over all angles); r = 0.1 and 1: 5e-10 / 6e-10. Their dU is the lead export minus the ray integral, so it also contains
    the lead inverse's own discretization error; mine is the closure alone.
    Verdict: the closure row is CONFIRMED in order and size, with corrections for the report: (i) state that the
    numbers are in N_v (the lead's N4); in N_f the effect next to P is 5e-9 (velocity part) to 7e-9, not 3e-9; (ii) "at
    most 1.3e-8 (r <= 300)" rests on sample points; over all grid points of r < 1000 the N_v maximum is 2.0e-8 (1.6e-8 for
    r <= 300); (iii) "0.4 to 10 percent of the residual" agrees with my 1 to 7 percent of the band maxima; (iv) the c_l
    shift of 3.4e-9 belongs only to the identity convention, the fixed-c_l fit sees the velocity part alone. Consequence:
    none for my audited residuals (my inverse goes to 1e6 L); the fit's own closure moves its residual by at most 7 percent
    of the band maxima for r < 1000 and 1 percent next to P, so the fit and my audit measure the same function there.
    Numerics 09:53Z items 1 and 2 (their corrected inner maxima and the referee wording for 4.5). Their inner (|X - P| <
      0.5) impact at 1000 L on c6d_seg1, 2.33e-9, against mine 1.6e-9 (velocity part, N_v) and 2.1e-9 (total, N_v):
      CONFIRMED in order. "Up to 1.3e-8 at the sampled radii 20, 100 and 300" is correct for their 50 sample nodes; over
      all grid points my maximum is 1.6e-8 for r <= 300 and 2.0e-8 for r < 1000. Their percentages (0.34 near P, 9 to 14
      at r = 20, 100, 300) are relative to sampled regional maxima of c6d_seg1; mine (1.0 to 1.1 near P, at most 7 at 300
      to 1000) are relative to full-grid band maxima of the candidate, whose near-P N_v is 3.6 times lower than c6d_seg1's.
      The two sets are consistent; the report should give one of them with its reference set named.


(e) c6f segment 2 at iterate 750 against the candidate (lead NOTES_FOR_TEAM 10:04Z items 1 to 3 and 5; M2 of the 09:16Z
    rule). Method: shape copied by c6fs2_follow.sh at the lead's iterate-750 check line (md5 a1a7a209..., equal to
    work/c6/c6f_seg2_shape.npz, the segment-end state); my generator and evaluator in the G20 (b) set (N11250 q384, N16875
    q384 / q512 / q768, N22500 q384 / q512, R 7.652e6), extra_checks, resmap (N11250 q384); the candidate's rows are those
    of G67. Result, free iterate 750 / candidate:
      c_l 5.5763640 (identity; lead 5.576364040) / 5.5753626. h(P) - 1 +1.7e-8 and -1.9e-8 (N16875 q384, N22500 q512;
      +2.0e-7 at N11250, the known grid floor). D14 on [1e-3, 0.02]: E -3.8e-9, D2 +8.7e-9 (lead -3.7e-9, +8.3e-9). Zeros:
      no open-quadrant cell with both components of W changing sign; W_2/y on the y-axis at least 5.5766.
      Whole-box N_f maximum (all at r 8.52 to 8.53, theta 0.0556 to 0.0565, the strip next to the x-axis left of P, about
      0.48 from P): N11250 q384 2.087e-6; N16875 q384 2.307e-6; N16875 q512 2.220e-6; N16875 q768 2.307e-6; N22500 q384 2.327e-6;
      N22500 q512 2.271e-6. Lead scans 2.28e-6 / 2.33e-6. Candidate 6.53e-7 to 6.98e-7 at the same configurations (at N16875 q768 outside the y-axis floor column of A5, where it has 1.22e-6 at theta 1.5692).
      Bands, N_f (N16875 q384; N22500 q512): 0.1-2 1.37e-7 / 1.72e-7 (1.44e-7 / 1.81e-7); 10-100 3.73e-7 / 4.42e-7
      (5.89e-7 / 4.57e-7; the free 5.89e-7 sits at theta 1.568, in the y-axis floor column of A5; at q384 3.7e-7 to
      4.3e-7); 100-1000 6.1e-8 / 6.9e-8 (6.3e-8 / 7.1e-8).
      N_v by region (N16875 q384; N22500 q512): |X - P| < 0.5 6.52e-7 / 1.88e-7 (6.42e-7 / 1.92e-7); 2-10 6.52e-7 /
      5.20e-7 (6.42e-7 / 5.32e-7); 0.1-2 2.68e-7 / 3.36e-7 (2.80e-7 / 3.54e-7); 10-100 2.71e-7 / 2.86e-7 (2.75e-7 /
      2.94e-7); 100-1000 2.50e-7 / 2.83e-7 (2.59e-7 / 2.94e-7); far field (r >= 1000) 1.459e-6 / 1.135e-6 (1.473e-6 /
      1.160e-6).
      L2 objective (lead log): 7.077e-6 / 8.474e-6.
    M2 reading (09:16Z item 3). M2 = 2.31e-6 (N16875 q384) and 2.27e-6 (N22500 q512), CONFIRMED against the lead's 2.28e-6
      / 2.33e-6, and >= 1.5e-6 at every configuration (2.09e-6 to 2.33e-6). By the rule as registered the fall of the strip
      maximum from c6f segment 1 to the candidate is a c_l effect at equal LSQR budget. Qualifiers the report must carry
      with it: (i) the free strip maximum is not monotone in the budget: 1.53e-6 (250), 1.29e-6 (500), 2.31e-6 (750) at
      N16875 q384, while the objective fell 7.53e-6, 7.39e-6, 7.08e-6; at 500 the free / fixed ratio was 1.3 to 1.4, at
      750 it is 3.4; (ii) "equal budget" holds in LSQR iterations, not in linearizations (free: one linearization of 750;
      fixed: 500 + 250 over two); (iii) the iterate-750 maximum is a ripple at the top angular modes next to the x-axis
      (resmap: m about 145 to 150 and about 118), the angular cap of the basis; (iv) it is one pair at one budget. The rule
      outcome is therefore "c_l effect at the 750 budget", not a statement that the strip would stay higher at a larger
      budget; the 1500 comparison (seg 3 against fixc_c6f_m1.0e-03_s2) tests it.
    J and the label set (new in this item; code/vchar_dense.py). Method: the evaluation, splines and DOP853 integrator of
      code/vchar.py (G20 (e)), each label integrated at rtol 1e-9 and 1e-11 (difference at most 2.2e-8 on every label),
      backward from r = 20 until |X - P| = eps. Label families on r = 20: A, theta0 uniform on [0.02, pi/2 - 0.02] (737
      labels; every second label, 369, gives the same spread within 1 percent); B, theta0 = pi/2 - delta, and C, theta0 =
      delta, with delta geometric in [1e-4, 0.02) (60 each). Grid: N16875 q384 for all 857 labels; N22500 q512 for 400 A
      labels in [1.40, 1.5508] and for B and C, which agree label by label with N16875 q384 within 1.3e-8 (6e-9 after
      interpolation in theta0). Spread (max - min over the set) at eps 0.03 / 0.01, candidate / free iterate 750:
        lead's 8 labels (lead numbers)          1.03e-6 / 3.19e-7 (ratio 3.2)
        24 labels (G20 set, theta0 0.02 to 1.55) 1.032e-6 / 5.58e-7 at 0.03 (1.85); 1.196e-6 / 5.58e-7 at 0.01 (2.15)
        185 labels (A, every fourth)            1.813e-6 / 1.283e-6 at 0.03; 1.957e-6 / 1.283e-6 at 0.01
        737 labels (A)                          1.910e-6 / 1.294e-6 at 0.03 (1.48); 2.016e-6 / 1.294e-6 at 0.01 (1.56)
        857 labels (A, B, C)                    2.738e-6 / 2.267e-6 at 0.03 (1.21); 2.684e-6 / 2.165e-6 at 0.01 (1.24)
      Where the spread comes from. For theta0 < 1.35 J varies slowly (neighbour differences 1.5e-9 to 1.3e-8) and
      the range is at most 5.2e-7 on either fit. The extremes of A lie in theta0 in [1.45, 1.57), where the labels pass
      near the origin (closest approach 1.5 to 3) and then run along the x-axis to P; there neighbour differences are
      5.6e-8 (candidate) and 1.0e-7 (free), and 49 of the 737 labels fall in that bin, which is why 24 labels miss the
      extremes. A minimum: candidate theta0 1.5383 (J(0.03) -6.76e-7), free 1.4905 (-6.35e-7). The B family converges as
      delta -> 0 (labels on the separatrix: down the y-axis, through the origin, along the x-axis from the left) to
      J(0.03) +2.06e-6 (candidate) and +1.63e-6 (free). Decomposition along the trajectory (code/vchar_traj.py, same
      evaluation, rtol 1e-11, J summed by region on 20001 points; label delta = 1e-4), candidate / free: y-axis strip (x <
      0.5, y > 0.5) +1.2e-8 / +8.1e-8; origin disk r < 0.5 +2.9e-8 / +2.2e-8; x-axis strip (y < 0.5, x >= 0.5, |X - P|
      >= 0.5) +2.17e-6 / +1.39e-6, of which x in [0.5, 2) +4.9e-7 / +3.5e-7, [2, 4) +8.1e-7 / +6.3e-7, [4, 6) +6.0e-7 /
      +4.0e-7, [6, 7.6) +2.2e-7 / +4.5e-8; disk |X - P| < 0.5 -1.5e-7 / +1.4e-7. So the largest J values measure R/rho on
      the x-axis between the origin and P (the residual of the axis equations, weighted by 1/|W_1|), not a defect near P.
      Generic labels (theta0 = 0.3 and 1.0) gain the same +8.69e-7 (candidate) and +2.48e-7 (free) in the disk |X - P| <
      0.5, which the spread removes; the A minimum of the candidate (theta0 1.5383, J -6.76e-7) gains -5.4e-7 on the
      x-axis strip, mostly at x in [4, 6). The C family (labels next to the x-axis right of P) converges to -5.0e-8 /
      -1.5e-8; its range (to 1.14e-6 / 4.1e-7) comes from delta 0.007 to 0.02.
      Label-free check (code/vaxis.py): on the x-axis rho = 0 and W_2 = 0, R/rho has the even limit q0(x) (Richardson in
      y^2 from the half-shifted angles pi/Nt and 3 pi/Nt; correction at most 5.9e-7 against max |q0| 1.04e-5), and a
      label on the separatrix gains I(eps) = int_{0.01}^{x* - eps} q0/|W_1(x, 0)| dx on the axis. I(0.03) / I(0.01):
      candidate 2.039e-6 / 1.986e-6, free 1.544e-6 / 1.537e-6. The B limit minus its y-axis and origin parts agrees with
      I(0.03) within 2e-8 on both fits, and the C limit with the integral from the right, int_{x* + 0.03}^{20}, within
      1e-9 (-4.94e-8 / -1.45e-8). Profile of q0 on the axis, candidate / free: 3.1e-6 / 2.2e-6 at x = 1, 1.02e-5 / 7.8e-6
      at 3, 1.04e-5 / 8.0e-6 at 4, 4.6e-6 / 2.1e-6 at 6, below 1e-6 in absolute value on [8, x*) and below 2e-8 for x >=
      10. So R/rho on the axis segment between the origin and P is at most 1.04e-5 on the candidate and 8.0e-6 on the
      free fit (lower by 1.3); this is the quantity behind the largest J values. I(eps) needs no labels and is the
      residual of the axis reduction weighted by the transit time, so it is a better-defined companion of the J spread
      than any finite label set.
      So the referee's caution (S4: the O(1) term is not uniform as labels approach the x-axis) is borne out in the
      sense that the spread depends on the label set; with the two near-axis families added it is bounded on both fits.
    Reading. (i) "J of the free fit is lower at 750" (lead 10:04Z; A1 fails at the 750 budget) is CONFIRMED on every
      label set, with a ratio between 1.21 and 3.2 depending on the set. (ii) Neither fit has a J spread near 1e-6 on a
      resolved label set: 1.9e-6 to 2.7e-6 on the candidate, 1.3e-6 to 2.3e-6 on the free fit. (iii) All my earlier J
      spreads (G20 onward, 24 labels) are lower bounds of the label-resolved spread; in particular the candidate values of
      G67 (1.03e-6 / 1.20e-6) are corrected to 1.91e-6 / 2.02e-6 (737 labels) and 2.74e-6 / 2.68e-6 (857 labels). (iv)
      The two fits are not ordered at 750: the candidate is lower in the N_f strip maximum (3.4), in N_v near P (3.5) and
      in the far N_v (1.29); the free fit is lower in J (1.2 to 1.6 on resolved sets) and in the L2 objective (1.20).
      Recommendation: from now on A1, SPEC b3 and every J value in the report are read on a named dense label set; I
      propose A (737) plus B and C (60 each), as above, with the 737-label A value quoted separately, and next to it
      I(0.03), I(0.01) and max |q0| on (0, x*).

(f) Draft section 4 v3, the six replacement wordings (lead NOTES_FOR_TEAM 10:24Z item 2; notes/final_sec4_v3_text.md at
    10:29:21Z). Method: each statement re-derived by hand from the generator formula (code/gen_shape.py, the H formula
    re-coded in scratch/pjump.py) and the shape file of the candidate (spline_order 7, 375 radial, m <= 150, 6 singular
    terms, origin_radius 0.02); numbers from G66 to G69.
      S1 (regularity). beta = p3 - 6 = 2/(2 c_l - 1) = 0.19703 on the candidate: CONFIRMED (2 k/(2 - k) = 2/(2 c_l - 1)
        with k = 1/c_l). The singular terms of H are |x|^(p3 - 2) y^2 times a function smooth in r^2 (s^(p3/2) |cos|^(p3-2)
        sin^2 = |x|^(p3-2) y^2 / (L^p3 (1 + (r/L)^2)^(p3/2))), so H is exactly C^(4,beta)_loc wherever the Chebyshev sum T
        is not zero on the y-axis; rho_h = x^2 y times that term is |x|^p3 y^3 times a smooth function, exactly
        C^(6,beta)_loc: CONFIRMED. The integer angular spline terms: degree-7 B-splines in q (C^6 with bounded seventh
        derivative across simple knots), q analytic in r^2, and the first basis function is dropped, so prof_m(q) = q
        times a polynomial on the first knot interval and prof_m chi^(m-1) cos(2 m theta) = Re((x + i y)^(2m)) times a
        function analytic in r^2 there: C^(6,1)_loc on the plane, analytic near 0 within the first knot interval
        (q < 0.00106, r < 0.39): CONFIRMED.
      S2 (far field). Theta_1 = -L^(1-k) (sum_m b_m'(1) cos(2 m theta) + 2 T'(1) sin^2 |cos|^(p3-2)), remainder
        O(r^(2k-2)) uniformly in theta: CONFIRMED (q = 1 - (r/L)^(k-1) + O(r^(2k-2)); first-order Taylor of prof_m and of
        T(2q - 1) at q = 1, the factor 2 from d(2q - 1)/dq; chi^(m-1) and s^(p3/2) are 1 + O(r^-2), smaller than r^(2k-2)
        since 2k - 2 = -1.64 > -2).
      S3 (R/rho at P). With rho = y g, W_2 = y h: R = W.grad rho - rho = y (W.grad g + (h - 1) g), so R/rho = h - 1 +
        W.grad log g, continuous across the axis where g > 0 and W is C^1; value h(P) - 1 at P. Near P, W_1 rho_x = W_1 y
        g_x = o(|rho|) and W_2 rho_y = h rho + O(y^2), so N_f/|rho| -> h(P) + 1 = 2: CONFIRMED.
      S4 (J). rho_tr,eps = e^(-t_eps) rho(Phi_{t_eps} X0) with the frozen trial field and J = log rho(X0) - log rho_tr,eps
        (from d/dt log rho(Phi_t X) = 1 + R/rho): CONFIRMED; the expansion for fixed off-axis labels and the
        non-uniformity: CONFIRMED (G68 E13; (e) above shows the label dependence). The label-set sentence and the values
        need the correction below.
      S5 (polynomial states). A nonzero polynomial with the required parity and center jet x^2 y has total degree d >= 3;
        its top homogeneous part is nonzero on some ray, so sup over |X| = r is comparable to r^d, which violates |rho| <=
        C (1 + |X|)^(1/c_l) with 1/c_l = 0.179: CONFIRMED. This is the check of convergence to polynomial states required
        of the verifier; the trial grows like r^k, k = 1/c_l = 0.179 (the term (k - 3)/2 log(1 + (r/L)^2) of H with the
        factor x^2 y), so it is not near a polynomial state.
      S6 (layer). Replacement accepted; it supersedes and withdraws my G68 E9 addition ("the measured step changes sign
        near y = 0.5, so the fits' feature is not of this form at leading order"), which inferred a leading coefficient
        from a finite-window estimate. lambda = rho_y(P)/(2 c_l - 1), about 2.93, and the blow-up of the third
        derivative like |x - gamma(y)|^(lambda - 3) are CONFIRMED (G66 (a), (b)); the shared positive transport multiplier
        of the two amplitudes on a regular positive branch is the referee's claim, read but not re-derived by me.
    4.4b correction (REFUTED as a description of the defect, the numbers are correct for the set named). "The reported
      quantity is the spread ... over a fixed set of 24 labels on the circle r = 20 (angles 0.02 to 1.55)" with "9.9e-7
      to 1.04e-6 at eps = 0.03 and 1.12e-6 to 1.21e-6 at eps = 0.01 on the candidate (free fit 3.1e-6 and 3.4e-6 to
      3.5e-6)": the 24-label spread is a lower bound of the label-resolved spread by a factor 1.9 on the candidate and
      2.3 on the free iterate 750 ((e)); the free numbers are those of c6f segment 1, not of the equal-budget control.
      Suggested: "The reported quantity is the spread of J_eps over a named label set on r = 20: 737 angles uniform on
      [0.02, pi/2 - 0.02] and 60 angles at geometric distances 1e-4 to 0.02 from each axis. On the candidate it is
      1.91e-6 (737 angles) and 2.74e-6 (all 857) at eps = 0.03, and 2.02e-6 and 2.68e-6 at eps = 0.01; on the equal-budget
      free fit (c6f segment 2, 750 iterations) 1.29e-6 and 2.27e-6 at eps = 0.03, and 1.29e-6 and 2.17e-6 at eps = 0.01
      [V]. On 24 angles the spread is about half of these values; the extremes lie at labels whose characteristics pass
      near the origin, and the limits at both axes exist." The sentences on the common logarithmic term stay.

    Correction to earlier items. The J spreads of G20 to G68 were taken on 24 labels (G20 set) or fewer and are lower
      bounds of the label-resolved spread. On the two shapes measured here the factor is 1.85 (candidate, 737 labels) and
      2.3 (free iterate 750); for the shapes of G42 to G66 it was not measured. The candidate values of G67 ("J 1.0e-6 /
      1.2e-6") are replaced by 1.91e-6 / 2.02e-6 (737 labels) and 2.74e-6 / 2.68e-6 (857 labels). Ratios between shapes
      taken on the same 24 labels (G67 (b), G68 E7, (a) and (b) of this item) remain comparisons on that set only.

Verdict: (a) numerics 09:18Z item 1 CONFIRMED on my evaluator; dom90 J is 1.6x to 1.8x c6dS1 (24 labels). (b) the gap
at equal LSQR count opens from 1.1x (250) to 1.3x to 1.4x (500). (c) the free formulation keeps c_l to 8.6e-6 at 5.60
(CONFIRMED). (d) the closure row CONFIRMED in order and size with four corrections. (e) M2 = 2.31e-6 / 2.27e-6 CONFIRMED;
by the 09:16Z rule the strip fall is a c_l effect at the 750 budget, with qualifiers (i) to (iv); "J of the free fit is
lower" CONFIRMED on every label set (ratio 1.21 to 3.2), so A1 fails at 750; the two fits are not ordered; my 24-label J
values are lower bounds by about 2 (corrected above). (f) the six wordings S1 to S6 CONFIRMED (S6 accepted, my G68 E9
addition withdrawn); the 4.4b label-set sentence and its values are REFUTED as a description of the defect and need the
replacement given. No endpoint is confirmed; the team may NOT finish.

G69 addendum (g) (2026-10-18T10:53Z): lead NOTES_FOR_TEAM 10:46Z item 3 (reading of J for the 1500-iteration comparison and
the report). CONFIRMED with two amendments. (1) The set is A (737) plus B and C (60 each), 857 labels, the set of (e), on
every fit; I run it on s2, seg 3 and fxfr when announced, and on c6dS1, c6fS1 and fixc_c6d now (scratch/jref.sh). The
737-label A value is quoted next to it. (2) "A spread over labels approaching an axis need not stay bounded, so the value
is a property of the stated set": on both fits measured the limits at both axes exist (B: J(0.03) at delta = 1e-4 equals
the separatrix value, the axis integral I(0.03) plus the y-axis and origin parts, within 2e-8; C: the integral from the
right within 1e-9), and J is resolved in theta0 at this density (369 against 737 labels within 1 percent; N22500 q512
window within 1.3e-8). So on these fits the 857-label spread equals sup minus inf of J_eps over all labels on r = 20 to
about 2e-8, and the report may say so for the fits on which it is measured, with the label-free I(eps) as companion. The
referee's statement concerns the general case and stays as a caution. The lead's 8-label withdrawal (10:46Z item 2) is
noted; my G69 (e) row "lead's 8 labels" carries the lead's numbers only for that reason.

## G70 dom90 segment 2 by its rule, the cap ripple behind J and the axis quantities, fxd1 (m <= 100 at the fixed c_l), the values for draft section 4 v3, and fxd300 (2026-10-18T12:09:25Z)

Shapes copied read-only from the lead and numerics lanes with md5 checks; every number below is from my generator and
evaluator unless marked as a lead or numerics value. Labels: c6dS1 = c6d segment 1 (375 x m <= 100, free c_l), the
candidate = fixc_c6f_m1.0e-03 (outer 2, iterate 250; 375 x m <= 150 at c_l 5.5753626), c6fS1 / c6fs2i750 = c6f segment 1 /
segment 2 at iterate 750 (free), fxd1 = fixc_c6d_m1.0e-03, dom90S2 = dom90 segment 2, fxd300 = fixed c_l on the dom300
basis.

(a) dom90 segment 2 by the lead's 07:23Z rule (numerics NOTES 11:07Z: "agreeing"). Method: shape leadcode/c7/
    dom90_seg2_shape.npz copied at 11:03:06Z (md5 0aa4ec11...); my generator with the lead's two-term closure at R_shape =
    100 (Rc 765.2, fit radius 688.68) and my evaluator (k_self) at N11250 q384, N22500 q384 and N16875 q512, against c6dS1
    (formula to 7.652e6) at the same configurations; extra_checks at N11250 q384; the objective from the numerics solver
    log (leadcode/c7/dom90_seg2.log); J on the 857-label set (code/vchar_dense.py, fit convention, N16875 q384).
    Result (dom90 segment 2 / c6dS1, the three configurations in the order above):
      N_f maximum for r <= Rfit, next to P in both (it is also the 2-10 band maximum): 2.596e-6 / 2.424e-6,
      2.643e-6 / 2.444e-6, 2.594e-6 / 2.409e-6 (ratios 1.07, 1.08, 1.08).
      10 <= r <= 100: 6.62e-7 / 7.54e-7, 6.66e-7 / 8.03e-7, 6.70e-7 / 9.49e-7 (0.88, 0.83, 0.71).
      0.1 <= r <= 2: 2.07e-7 / 2.17e-7, 2.07e-7 / 2.17e-7, 2.13e-7 / 2.22e-7.
      c_l: identity on my inverse 5.576367026 (stored 5.576367026); root of h(P) = 1 at fixed rho 5.576366999; against
      c6dS1 5.5763622, +4.9e-6. h(P) - 1: +2.7e-7, +1.7e-9, +4.3e-8.
      Objective (fit rows, r < 90 L), segment 2: 1.44512e-5 at the start, 1.43461e-5, 1.42665e-5, 1.42019e-5 and
      1.41143e-5 at iterates 250 to 1000, so -2.33 percent over the segment (-0.73, -0.55, -0.45, -0.62 percent per 250
      iterations; no slowing). c_l moved +3.1e-7 over segment 2 and +4.5e-6 over segment 1.
      J spread on 857 labels, eps 0.03 / 0.01: 4.315e-6 / 4.455e-6 against c6dS1 3.679e-6 / 3.669e-6 (1.17, 1.21); 737
      labels: the same values (both extremes are in the uniform family, theta0 1.5071 and 1.5446). The 185-label subset
      gives 4.258e-6 (numerics 11:07Z: 4.19e-6, 1.6 percent lower). The 24-label values 2.07e-6 / 2.15e-6 are lower bounds.
      Axis (vaxis, fit convention, N16875 q384): I(0.03) -1.56e-7, I(0.01) -2.87e-7; the same integral of |q0| 3.31e-6
      (eps 0.03); max |q0| 1.03e-5 at x 2.90; q0 is positive up to x 5 (2.41e-6 there) and negative from x 6 (-2.90e-6 at
      6, -4.88e-6 at 7, -3.94e-6 at 8.4). The signed integral is small by cancellation between the two parts of the axis.
      D14 on [1e-3, 0.02]: E -6.0e-9, D2 +1.5e-8. One zero of W_1 on the x-axis (8.6008438), W_2/y >= 5.5766 on the
      y-axis, no open-quadrant cell where both components change sign.
      Segment 1 to segment 2 (N11250 q384): next to P 2.713e-6 -> 2.596e-6, 10-100 7.47e-7 -> 6.62e-7.
      Numerics 11:07Z (their scan, 32768 x 640): 2-10 2.63e-6 (1.08), 10-100 6.70e-7 (0.92), c_l +4.9e-6, objective -2.3
      percent; their bands agree with mine to 2 percent.
    Exterior. The two-term closure beyond R_shape L is part of the dom90 problem. Moving it to 1000 L (field B, same grid,
    code/clo_diff.py, k_self on both; the densities agree inside 765.2): c_l from the identity +4.17e-5; next to P
    max |R_B - R_A| / N_f 8.3e-5 (velocity part at fixed c_l 6.2e-5, c_l part 2.3e-5; N_v 2.5e-5, velocity part 1.9e-5),
    max |U_B - U_A| 1.1e-3 within 0.5 of P. With the closure at 1000 L or 1e4 L the dom90 residual next to P is 8.32e-5
    / 8.67e-5 after segment 2 against 3.87e-5 / 4.04e-5 after segment 1 (2.15 times): segment 2 lowered the residual of
    the closed problem by 4 percent and raised that of the continued formula by a factor 2.15. The split on segment 1
    (same code): c_l +1.93e-5; next to P 3.86e-5 (velocity part 2.89e-5, c_l part 1.05e-5; N_v 1.17e-5, velocity part
    8.8e-6). Segment 2 roughly doubled each part. The numerics' estimate of
    the exterior effect, "about 1e-5 in normalized-residual terms next to P" (11:07Z caveat), is of the order of my
    velocity part in N_v (1.9e-5) and below the N_f values by 3 to 6 times. For r > Rfit my N_f reaches 2.0e-3 (r 1694,
    theta 1.5675), the closure's own residual (as for dom100 in G64); the numerics' 100-1e3 entry 1.92e-5 is not
    comparable (different radial range or convention) and the rule does not read it.
    Verdict: by the 07:23Z rule dom90 is "agreeing": CONFIRMED on my evaluator (interior bands 1.07 to 1.08 and 0.71 to
    0.88 times c6dS1, c_l +4.9e-6 < 1e-5, objective -2.3 percent per segment < 5 percent). Qualifiers for the report:
    (i) the rule compares closed-box problems on r <= 90 L and r <= 1000 L; (ii) J on the 857 set is 1.17 to 1.21 times
    c6dS1 (within the rule's factor 1.5 if J were read); (iii) dom90 shows that cutting the fitted domain from 1000 L to
    90 L changes the near-P residual in the fit convention by under 10 percent and c_l by +4.9e-6. It does not show that
    the exterior is irrelevant to the whole-plane problem: the dom90 formula continued past 90 L is not a solution there
    (residual 8e-5 next to P, c_l shifted 4.2e-5), and segment 2 moved it further from one.

(b) What sets J, I(eps) and q0: the residual next to the x-axis at the angular frequency of the basis cap. Question:
    G69 found that the 857-label J oscillates with the label theta0 in family A (theta0 1.43 to 1.55) and attributed the
    largest values to the axis residual q0 between the origin and P (adopted in the lead's 11:00Z item 3 and in 4.4b).
    Method (my code, N16875 q384, R 7.652e6, fits c6dS1 (cap m <= 100), the candidate fxm1o2i250 and c6fs2i750 (m <= 150),
    plus c6fS1, fxd1 and the domain fits dom90S2 and fxd300 (fit convention, closure) for the axis split):
      code/vstrip.py: q = R/rho on the half-shifted angles theta < 0.12 at r = 1, 2, ..., 8, 8.3, fitted by an even
      polynomial in theta (4 terms in theta^2); the remainder is the ripple; its sign changes give a half period and an
      angular frequency pi / (half period). Sine spectrum of R(r, .) over the circle, RMS by band of k.
      code/vchar_traj.py: the J integral along single characteristics split by region (y-axis strip x < 0.5, y > 0.5;
      r < 0.5; x-axis strip y < 0.5, x >= 0.5, |X - P| >= 0.5; disk |X - P| < 0.5; rest).
      code/vq0band.py: q0 = d_theta R(r, 0) / d_theta rho(r, 0) = sum_k k R_k / rho_theta split by band of k with
      Ktop = 2 m_max (low [1, Ktop/2), mid [Ktop/2, Ktop - 40), top [Ktop - 40, Ktop + 40), high above), and the axis
      integral of each part. Check: the spectral q0 agrees with the Richardson value of vaxis to 1.6e-8 to 7.8e-8 (1.5e-3
      to 7.5e-3 of max |q0|). Radial resolution: c6dS1 at N22500 q512 gives every band integral within 2.2e-8 at eps 0.03
      (5.3e-8 at eps 0.01) and the low, mid and top band maxima within 4e-10 of N16875 q384.
    Result.
      Ripple. c6dS1 (Ktop 200): at r 4 to 8.3 the remainder has half period 0.0154 to 0.0175 (k 180 to 204) and amplitude
      3.7e-6 to 1.1e-5; the R spectrum peaks in the band 150 <= k < 250 (3.1e-6 at r 4 rising to 3.3e-5 at r 8.3; the band
      1 <= k < 50 has 9.3e-7 to 7.2e-6); above k = 250 below 2e-9. Candidate (Ktop 300): half period 0.0104 to 0.0111 (k
      282 to 291) at r 4 to 8, amplitude 5.2e-7 to 1.07e-5; the band 290 <= k < 310 has 1.6e-6 to 5.8e-6 at r 4 to 7.6
      against 5.8e-7 to 1.8e-6 for 1 <= k < 50, and k >= 310 is at most 1.2e-7; at r 8 and 8.3 the band 1 <= k < 50 is as
      large or larger (4.4e-6 and 3.9e-6 against 4.3e-6 and 1.7e-6). c6fs2i750 (Ktop 300): k 291 to 302 at r 4 to 7,
      amplitude 1.7e-6 to 8.4e-6, band 290-310 1.2e-6 to 3.7e-6; at r 7.6 to 8.3 the bands below 250 are larger. At r 1
      and 2 the remainder of the 4-term fit has a longer period (k 90 to 93) on all three, and also at r 3 on the
      candidate and c6fs2i750 (c6dS1 at r 3: k 155); at r 1 to 3 every band of the R spectrum is at most 1.3e-6.
      At r 4 the candidate's q0 (1.04e-5) is the crest of the ripple: the smooth fit is -6.3e-7 at theta 0.02. This is
      expected for an odd R: near theta = 0, q is about sum_k R_k sin(k theta) / (rho_theta theta), which is largest at
      theta = 0 and oscillates at frequency k away from it, so q0 weights each R_k by k.
      Axis split (I(0.03) = low + mid + top; the high band is at most 1.3e-9 in absolute value):
        candidate      2.039e-6 = -2.89e-7 - 2.57e-7 + 2.596e-6   top part of q0 up to +1.98e-5 (x 5.09)
        c6fs2i750      1.544e-6 = -4.74e-7 + 1.137e-6 + 8.88e-7   top up to +1.58e-5 (x 4.90)
        c6fS1          1.102e-6 = +7.6e-8 + 1.769e-6 - 7.42e-7    top up to -2.05e-5 (x 8.53)
        c6dS1          4.83e-7  = +1.24e-7 + 1.381e-6 - 1.023e-6  top up to +2.04e-5 (x 4.35)
        fxd1           1.270e-6 = +1.10e-7 + 4.64e-7 + 6.96e-7    top up to +2.42e-5 (x 4.51)
        dom90S2        -1.56e-7 = +2.90e-7 + 1.563e-6 - 2.012e-6  top up to +1.86e-5 (x 4.23)
        fxd300         1.117e-6 = +1.31e-7 + 6.18e-7 + 3.67e-7    top up to +2.32e-5 (x 4.47)
      On every fit the top-band part of q0 reaches 1.6e-5 to 2.4e-5, above max |q0| (8.2e-6 to 1.36e-5), and the low plus
      mid part reaches 1.25e-5 to 1.68e-5; at the sampled x = 4, 5, 6, 7, 8, 8.4 the two have opposite signs on every fit
      (one exception, dom90S2 at x 6); at x = 0.5 and 1 the low plus mid part is positive and the larger one, at x 2
      both are positive. The candidate at x 4: q0 1.04e-5 = low -5.4e-6 + mid +7e-8 + top +1.58e-5.
      Characteristics (A-family labels): on c6dS1 theta0 1.5071, J = +1.89e-6 with +9.8e-7 from the x-axis strip and
      +8.5e-7 from the disk at P; theta0 1.5425, -1.79e-6 (-1.01e-6 and -5.9e-7). Candidate theta0 1.5071, +1.23e-6
      (+1.65e-7 and +1.06e-6); theta0 1.5383, -6.76e-7 (-5.42e-7 and -8.2e-8). c6fs2i750 theta0 1.5154, +6.59e-7 (+2.64e-7
      and +3.58e-7); theta0 1.4905, -6.35e-7 (-2.26e-7 and -3.94e-7). None of these labels enters r < 0.5 or the y-axis
      strip; the candidate labels theta0 1.4634 and 1.4842 take 9.7e-7 of 9.8e-7 and 7.1e-7 of 6.2e-7 from the disk.
    Reading. (1) Next to the x-axis, from r about 4 to P, R/rho is dominated by an oscillation in theta at the angular
    frequency of the basis cap (within 10 percent of 2 m_max) on both caps. The strip residual of G61 is the same feature.
    (2) The axis quantities q0 and I(eps) are differences of band parts each larger than the result: I is the top-band
    part minus a low-pass part of comparable size, and its sign differs between fits (top part from -2.0e-6 to +2.6e-6).
    The signed I is not a proxy for the J spread: c6dS1 4.8e-7 against 3.68e-6, dom90S2 -1.6e-7 against 4.32e-6, c6fS1
    1.10e-6 against 3.85e-6, fxd1 1.27e-6 against 3.14e-6, fxd300 1.12e-6 against 3.04e-6, candidate 2.04e-6 against
    2.74e-6, c6fs2i750 1.54e-6 against 2.27e-6. (3) The oscillation of J across family A is consistent with labels
    sampling the cap ripple at different phases; the band split of J along the same characteristics (code/vjband.py,
    queued in scratch/jA.sh) will test this. (4) The band split does not predict what a change of cap does: the k
    weighting of q0 emphasizes the top band, and the low-pass part is of the same size with the opposite sign, so
    removing the cap ripple would not by itself make q0 small.
    Corrections. My G69 sentence "the largest J values come from R/rho on the x-axis between the origin and P", the
    lead's 11:00Z item 3 ("J is dominated by the axis residual q0") and the two 4.4b sentences hold for the family-B
    maximum only (d). For the s2w design (axis weight on 1 <= x <= 6.8): a lower q0 there does not bound the family-A
    extremes, which take half or more of their J from the disk at P and from the strip at heights y up to 0.5.
    Recommendation for 4.4b and A1: report with the 857 spread the family-A range on theta0 in [1.45, 1.55], the top-band
    part of I(0.03) and the ripple amplitude at r 4 to 8, so that a fall of J can be attributed to the cap ripple or to
    the rest.
    Verdict (b): the cap-frequency ripple next to the x-axis CONFIRMED on three fits and both caps (my measurement), the
    band composition of q0 and I(eps) on seven fits; the attribution of the A-family J oscillation to the ripple is
    consistent with the data and OPEN until the vjband split; the G69 / 11:00Z / 4.4b sentence on the origin of the
    largest J REFUTED as a general statement.

(c) fxd1 = fixc_c6d_m1.0e-03 (375 x m <= 100 at the candidate's c_l 5.5753626; lead 11:19Z item 1). Method:
    scratch/resstudy_follow.sh copied the lead's final shape at 11:12:22Z (md5 14865271..., equal to the lead's and to the
    md5 the lead quotes); my audit at N11250 q384, N16875 q512 and N22500 q384 (formula to 7.652e6), extra_checks at N11250
    q384, residual map; J on the 857-label set and vaxis at N16875 q384 (scratch/jref.sh). Against c6dS1 (same basis,
    c_l from the identity) at the same configurations and against the candidate (375 x m <= 150, same c_l).
    Result (fxd1 / c6dS1, configurations in the order above):
      N_f maximum in the box, next to P in both (fxd1 at r 8.33, theta 0.0164): 1.885e-6 / 2.424e-6, 1.878e-6 / 2.409e-6,
      1.894e-6 / 2.444e-6, so c6dS1 is 1.29, 1.28 and 1.29 times higher. Lead (32768 x 640): 1.89e-6 against 2.43e-6,
      1.29. CONFIRMED.
      10 <= r <= 100: 7.66e-7 / 7.54e-7, 8.69e-7 / 9.49e-7, 8.14e-7 / 8.03e-7. 0.1 <= r <= 2: 2.51e-7 against 2.17e-7
      (1.16 times higher at the fixed c_l; lead 2.64e-7 / 2.29e-7). 2-10 N_v: 6.80e-7 and 7.10e-7 against 6.84e-7 and
      6.75e-7. N_v in the box: 1.34e-6, 1.39e-6, 1.35e-6 against 1.46e-6 (far field next to the y-axis in both).
      r >= 1000, N_f: 3.10e-7 (r 2.66e4) against 2.63e-7. The lead's 2.45e-7 / 2.55e-7 come from a different radial
      sampling; the order is reversed in mine, and the rows differ by under 20 percent.
      c_l: identity on my inverse 5.575362609 (stored 5.575362613). h(P) = 1.000000058 at the stored c_l; the root of
      h(P) = 1 at fixed rho is 5.575362556 (-5.3e-8). One zero of W_1 on the x-axis (8.6000684); W_2/y >= 5.5756 on the
      y-axis; no open-quadrant cell with both components changing sign. D14 on [1e-3, 0.02]: E -5.8e-9, D2 +1.3e-8.
      J, 857 labels, eps 0.03 / 0.01: 3.142e-6 / 3.188e-6 (c6dS1 3.679e-6 / 3.669e-6, so 0.85 and 0.87 times); 737
      labels 2.835e-6 / 2.835e-6. Maximum in family B (1.474e-6 at theta0 1.570554), minimum in family A at theta0 1.4759
      (-1.668e-6). The A-family oscillation of (b) has the phase of c6dS1 (maximum at 1.5071, minima at 1.4759 and 1.540).
      Axis (vaxis): I(0.03) 1.270e-6, I(0.01) 1.224e-6; the same integral of |q0|, 3.13e-6 (eps 0.03); max |q0|
      1.36e-5 at x 3.28 (c6dS1 1.13e-5 at 3.18); q0 changes sign at x about 6.5 (-2.2e-6 at x = 7); partial integrals
      F(a) from -9.3e-7 to 1.27e-6.
    Reading (G20 (b1)-(b3) at the fixed c_l; two of the three bases, fxb1 = 244 x m <= 100 pending):
      fxd1 (m <= 100) to the candidate (m <= 150): next to P 1.89e-6 -> 6.7e-7 (2.8 times lower); 10-100 7.7e-7 to 8.7e-7
      -> 4.4e-7 to 4.6e-7; 0.1-2 2.5e-7 -> 1.7e-7 to 1.8e-7; N_v in the box 1.34e-6 to 1.39e-6 -> 1.13e-6 to 1.17e-6;
      857 J 3.14e-6 / 3.19e-6 -> 2.74e-6 / 2.68e-6 (eps 0.03 / 0.01); max |q0| 1.36e-5 -> 1.07e-5; I(0.03) 1.27e-6 ->
      2.04e-6. Every residual band and the J spread fall; the signed axis integral rises (it is a difference of band
      parts, (b)). The LSQR budgets differ (fxd1 ended at outer 2, iterate 500 of its 1.8 h solve from the shifted c6d_seg1;
      the candidate at outer 2, iterate 250 from the shifted c6f start), so this is one refinement step at unequal
      budgets, not a convergence rate.
    Verdict (c): fxd1 numbers CONFIRMED; the lead's 1.29 CONFIRMED; first fixed-c_l refinement step (m 100 -> 150)
    improves every band and the J spread, with I(eps) the exception. G20 (b1) and (b3) need the third basis (fxb1) and the
    domain rows (fxd300, fxd90).

(d) Values and wording for draft section 4 v3 (lead notes/final_sec4_v3_text.md, file mtime 11:28:54Z). Method:
    my 857-label J (code/vchar_dense.py), vaxis at node level (code/vaxis.py, the ax2 runs) and vq0band, all at N16875
    q384 on my generator and evaluator; the table's free column is c6f segment 1 (c6fS1, c_l 5.5763624) and the text's
    equal-budget free fit is c6f segment 2 at iterate 750 (c6fs2i750).
    Table of 4.3, free column [V pending] (c6fS1): J spread on 857 labels, eps 0.03 / 0.01, 3.85e-6 / 4.14e-6; on the
      737 uniform labels the same values (both extremes in family A, theta0 1.5030 with +2.786e-6 and 1.5425 with
      -1.063e-6); I(0.03) / I(0.01) 1.10e-6 / 9.45e-7; max |q0| on (0, x*) 9.48e-6 at x 3.53.
    Candidate column: 857 labels 2.738e-6 / 2.684e-6, 737 labels 1.910e-6 / 2.016e-6, I 2.039e-6 / 1.986e-6: CONFIRMED.
      max |q0| "1.04e-5 (x about 4)" is to be replaced by 1.07e-5 (x 3.57). My G69 value 1.04e-5 was the largest of the
      tabulated values q0(x) at x = 0.5, 1, 2, ..., 8 (it is q0(4)); the maximum over the radial nodes on (0.01, x* - 0.03)
      is 1.066e-5 at x 3.566 (ax2 run; vq0band gives 1.07e-5 at 3.57). The error was mine.
    4.4b, equal-budget free fit: J 1.29e-6 / 2.27e-6 (eps 0.03) and 1.29e-6 / 2.17e-6 (eps 0.01): CONFIRMED (1.294e-6 /
      2.267e-6, 1.294e-6 / 2.165e-6). I(0.03) = I(0.01) = 1.54e-6: CONFIRMED (1.544e-6, 1.537e-6). max |q0| = 8.0e-6 is to
      be replaced by 8.2e-6 (8.24e-6 at x 3.72).
    4.4b, candidate profile: q0 3.1e-6 at x 1, 1.02e-5 at 3, 1.04e-5 at 4, 4.6e-6 at 6: CONFIRMED (3.12e-6, 1.019e-5,
      1.042e-5, 4.56e-6). "Below 1e-6 in absolute value on [8, x*)": at x 8 I have 4.6e-7 and at x 8.4 -9.4e-7, so the
      bound is close to the sampled value at 8.4, and (8.4, x*) is not sampled in my runs: OPEN (a node-level profile on
      [7.5, x*) is queued). "Below 2e-8 for x >= 10": at the sampled x 10 and 15, -9.6e-9 and -1.96e-8; the second is at
      the bound. Suggest "below 1e-6 at x = 8 and 8.4" and "about 1e-8 to 2e-8 at x = 10 and 15", or wait for the profile.
      With the corrected maximum the lead's export (1.07e-5 at x 3.56) agrees with mine to 0.4 percent, not 3.1 percent;
      I(0.03) / I(0.01) 2.058e-6 / 2.014e-6 against 2.039e-6 / 1.986e-6, 0.9 and 1.4 percent. The closing sentence "reaches
      1.04e-5" becomes "reaches 1.07e-5".
    4.4b, two sentences on where the J extremes come from (they repeat my G69 reading, which was too general):
      "the extremes lie at labels whose characteristics pass near the origin": REFUTED as a general statement. Traced
      characteristics (code/vchar_traj.py): every family-A label with theta0 from 1.43 to 1.5425 crosses y = 1 at x 1.04
      to 5.50 and never enters r < 0.5 or the y-axis strip x < 0.5, y > 0.5 (traced on c6dS1, the candidate and
      c6fs2i750). The 857-label extremes in family A are at theta0 1.4759 to 1.5446 on every fit measured (candidate
      minimum 1.5383; c6fS1 1.5030 and 1.5425; c6fs2i750 minimum 1.4905; c6dS1 and fxd300 1.5071 and 1.5425; dom90S2
      1.5071 and 1.5446; fxd1 minimum 1.4759). Only the 857-label maximum of the candidate, of c6fs2i750 and of fxd1
      (family B, theta0 1.5706, pi/2 - theta0 about 2e-4) runs down the y-axis, through the origin and along the x-axis to
      P.
      "The largest values come from the x-axis between the origin and P": true for that family-B maximum, whose J agrees
      with the axis integral (candidate 2.062e-6 against I(0.03) 2.039e-6; c6fs2i750 1.632e-6 against 1.544e-6; fxd1
      1.474e-6 against 1.270e-6). For the
      A-family extremes the strip y < 0.5 next to the x-axis (|X - P| >= 0.5) and the disk |X - P| < 0.5 contribute in
      comparable parts (c6dS1 theta0 1.5071: +9.8e-7 and +8.5e-7 of J = +1.89e-6; candidate theta0 1.5071: +1.65e-7 and
      +1.06e-6 of +1.23e-6, theta0 1.5383: -5.42e-7 and -8.2e-8 of -6.76e-7; c6fs2i750 theta0 1.4905: -2.26e-7 and -3.94e-7
      of -6.35e-7). Proposed wording: "On the candidate and on the equal-budget free fit the 857-label maximum is at a label
      next to the y-axis whose characteristic follows the separatrix (down the y-axis, through the origin, along the
      x-axis to P), and its J_eps is close to the axis integral I(eps) below. The other extremes are at labels with theta0
      from 1.47 to 1.55, which stay at r > 0.5; their J comes from the strip next to the x-axis and from the disk
      |X - P| < 0.5 in comparable parts. Along every label the integrand R/rho oscillates at the angular frequency of the
      basis cap (G70 (b))."
    4.5, "against sampled candidate residuals of 1.5e-7 within 0.5 of P [V pending]": 1.5e-7 is a value at the ray-check
      sample points, not a maximum. The between-node maxima within 0.5 of P over my six configurations are 6.53e-7 to
      6.83e-7 (N_f) and 1.83e-7 to 1.92e-7 (N_v) (G67 (a), rechecked from the six audit files). Suggest "against
      candidate residual maxima within 0.5 of P of 6.8e-7 (N_f) and 1.9e-7 (N_v)". The conclusion holds either way: the
      inverse changes the normalized residual by at most 2.8e-9, below 1.5 percent of the smallest of these values.
    Lead reading of the free branch (11:00Z, "the residual oscillates in theta just below the angular cap"): it holds for
      the candidate as well (G70 (b)): on both the strip ripple and the R spectrum peak within 40 of 2 m_max.
    Verdict (d): the candidate column, the equal-budget free values and I(eps) CONFIRMED; two maxima corrected (1.07e-5
    at 3.57, 8.2e-6 at 3.72); the free column values supplied; the bound on [8, x*) OPEN; the two label sentences
    REFUTED as general and replacement wording given; the 4.5 comparison value corrected, its conclusion CONFIRMED.

(e) fxd300 (numerics NOTES 11:33Z: fixed c_l 5.5753626 on the dom300 basis, fit radius 300 L, fit convention; their
    reading "agreeing" by the lead's 08:17Z rule). Method: scratch/fxd300_chain.sh copied numerics leadcode/c7/
    fxd300_seg1_shape.npz at 11:46:45Z (md5 bf137206..., equal to the source); my generator with the two-term closure at
    R_shape L (fit convention) and my evaluator (k_self, fit radius 2295.4 for the region split) at N11250 q384 and
    N16875 q512; on one N16875 q384 field the 857-label J and vaxis. Against fxd1 (= fixc_c6d_m1.0e-03, the rule's
    reference, G70 (c)) and dom300 segment 1 (free c_l, same basis, G64) at the same configurations.
    Result (fxd300 / fxd1, N11250 q384 then N16875 q512):
      2-10 N_f maximum, next to P (r 8.33, theta 0.016): 2.053e-6 / 1.885e-6, 2.094e-6 / 1.878e-6 (1.09, 1.11).
      10-100: 7.06e-7 / 7.66e-7, 8.23e-7 / 8.69e-7 (0.92, 0.95). 0.1-2: 2.45e-7 / 2.51e-7, 2.51e-7 / 2.56e-7.
      100-1000: 1.68e-7 / 2.27e-7, 1.68e-7 / 2.30e-7. N_v within 0.5 of P 5.74e-7 / 5.27e-7, 5.85e-7 / 5.25e-7.
      Against dom300 segment 1 (free): 2-10 2.55e-6 and 2.60e-6, so the fixed c_l lowers the near-P maximum by 1.24 on
      this basis (numerics 1.24; fxd1 against c6dS1 1.29).
      c_l: identity on my inverse 5.5753625998 against the stored 5.5753625996 (+1.8e-10). h(P) - 1: +4.0e-7 at q384 and
      +4.1e-8 at q512 (my quadrature error at P, the same pattern as fxd1: +3.9e-7 and +3.5e-8). D10 relative defect
      -8.8e-9. B_3 (integrated form) 0.2976 and 0.2974.
      J on 857 labels, eps 0.03 / 0.01: 3.036e-6 / 3.055e-6 (fxd1 3.142e-6 / 3.188e-6: 0.97, 0.96); the 737-label values
      are the same (extremes in family A at theta0 1.5071 and 1.5425, the phase of c6dS1). Axis: I(0.03) 1.117e-6,
      I(0.01) 1.076e-6 (fxd1 1.270e-6, 1.224e-6); the integral of |q0| 3.08e-6; max |q0| 1.31e-5 at x 3.21 (fxd1 1.36e-5
      at 3.28).
      For r > Rfit the residual is that of the closure (N_f up to 3.1e-4, N_v 5.1e-3), as for dom300 in G64.
      Numerics (their scan, 32768 x 640): 2-10 2.12e-6 (1.12), 10-100 7.13e-7 (0.95), h(P) - 1 -9.3e-9. My ratios agree
      to 3 percent.
    Verdict (e): by the 08:17Z rule fxd300 is "agreeing": CONFIRMED on my evaluator (interior bands 1.09 to 1.11 and
    0.92 to 0.95 times fxd1; my h(P) - 1 is at my grid error at P, and the numerics' -9.3e-9 is below 1e-7). J (857) is
    0.96 to 0.97 times fxd1. Cutting the fitted domain from 1000 L to 300 L at the fixed c_l changes the near-P residual
    by about 10 percent, as on the free branch (dom300 against c6dS1, 1.05 to 1.08). Both rows are at m <= 100; the
    domain row at the candidate's basis (m <= 150) does not exist.

Verdict G70: no endpoint is confirmed and the team may NOT finish. Confirmed: dom90 and fxd300 are "agreeing" by their
rules (07:23Z, 08:17Z), with the qualifiers of (a) and (e); the fxd1 numbers and the first fixed-c_l refinement step (m
100 -> 150), which lowers every residual band and the J spread at unequal budgets; the candidate column and the
equal-budget free values of section 4 v3. Corrected: max |q0| 1.07e-5 (candidate) and 8.2e-6 (equal-budget free fit);
my G69 sentence and the lead's 11:00Z item 3 on where the largest J comes from (true for the family-B maximum only).
Measured: next to the x-axis from r about 4 to P the residual R/rho oscillates in theta at the frequency of the angular
cap on both caps, and q0 and I(eps) are differences of band parts larger than themselves; I(eps) is not a proxy for the
J spread. OPEN: the attribution of the A-family J oscillation to the cap ripple (vjband queued), the bound on q0 over
[8, x*), the third basis fxb1 and a domain row at m <= 150, and A1 at a large equal budget (now the s2g / seg3g pair of
lead NOTES 12:02Z).

## G71 The band split of J along the family-A labels (G70 (b) OPEN item), the q0 profile next to P (G70 (d) OPEN item), fxfr1 (free continuation of the candidate), s2w1, and the reproduction notes of section 5 v2 (2026-10-18T12:26:25Z)

Every number is from my generator and evaluator (N16875 q384 fields at R 7.652e6 unless stated) except where marked as a
lead value. Labels as in G70; fxfr1 = fxfr_c6f_m1.0e-03 (the candidate continued with c_l free for 1000 LSQR iterations,
lead 11:53Z), s2w1 = s2w at iterate 250 (the axis-weighted fixed-c_l variant the lead stopped as failed at 11:53Z).

(a) Which part of the residual carries the oscillation of J in the start angle (family A). Method: code/vjband.py on
    c6dS1 (m <= 100, Ktop 200), the candidate fxm1o2i250 and c6fs2i750 (m <= 150, Ktop 300): J_eps along each of 73
    uniform labels with theta0 in [1.40, 1.5508] (the window holding the 737-label extremes of all three fits) and 20
    geometric labels, with R/rho split by the sine frequency k of R in the bands of G70 (b) (low [1, Ktop/2), mid
    [Ktop/2, Ktop - 40), top [Ktop - 40, Ktop + 40), high above). Check: the band parts sum to J within 1.5e-12 on every
    label. Reduction (scratch/jb_ana.py, scratch/jb_combo.py): from J(theta0) and from each band part remove the
    least-squares quadratic in theta0 over the window; the remainder is the oscillation; report its rms, and the
    correlation of each band remainder (and of each pair of bands) with the J remainder.
    Result (eps 0.03; eps 0.01 in brackets where the reading differs):
                       J range over the window   J remainder rms   corr low / mid / top   corr mid+top   corr low+mid
      c6dS1            -1.79e-6 .. +1.89e-6       9.31e-7           0.55 / 0.86 / 0.69     0.97 [0.99]    0.84 [0.73]
      candidate        -6.76e-7 .. +1.23e-6       3.02e-7          -0.13 / 0.38 / 0.65     0.93 [0.97]    0.19 [0.22]
      c6fs2i750        -6.33e-7 .. +6.57e-7       3.45e-7           0.15 / 0.35 / 0.05     0.45 [0.50]    0.28 [-0.03]
    On c6fs2i750 the band parts are much larger than J and cancel: top +6.1e-6 at most (1.27e-5 at eps 0.01), low down to
    -5.1e-6 (-9.7e-6), against |J| at most 6.6e-7. On the candidate the top-band remainder (rms 3.8e-7) exceeds the J
    remainder and the mid band takes part of it back. The high band is below 3e-8 on every fit. The J remainder half
    period is 0.028 (c6dS1), 0.044 (candidate) and 0.020 (c6fs2i750) in theta0.
    Reading. (1) On c6dS1 and on the candidate the oscillation of J in theta0 comes from the part of the residual at
    frequencies k >= m_max (mid plus top), with correlation 0.93 to 0.99; the band within 40 of 2 m_max alone correlates
    0.65 to 0.69. (2) On the equal-budget free fit no band or pair of bands carries it (at most 0.50). (3) From m <= 100 to
    m <= 150 the oscillation falls by a factor 2.7 to 3.1 in rms and the window range by 1.9 to 2.9.
    Verdict (a): the G70 (b) OPEN item is decided. "The A-family J oscillation is the cap ripple": CONFIRMED in the wider
    form "the residual at frequencies at or above the angular cap" for c6dS1 and the candidate, REFUTED for c6fs2i750, so
    REFUTED as a statement about all fits; the band within 40 of 2 m_max alone does not carry it on any of the three. Wording
    for 4.4b if used: "On the candidate and on the m <= 100 fit the oscillation of J in the start angle is carried by the
    residual at angular frequencies at or above the cap of the basis; on the equal-budget free fit it is not carried by
    one frequency band." The fall from m <= 100 to m <= 150 is one refinement step on two fits with different c_l and
    budgets, not a rate.

(b) q0 next to P (G70 (d): the 4.4b sentence "below 1e-6 in absolute value on [8, x*)"). Method: code/vq0prof.py on the
    candidate: q0 at every radial node with 7.5 <= r <= 8.7, Richardson from the two half-shifted angles next to the axis
    and spectral (sum_k k R_k / rho_theta), maxima over [a, x* - eps] for a = 7.5, 8, 8.4 and eps = 0.1 to 0.003.
    Result. Node spacing 0.0117 (the candidate's spline knots, mapped to r, are 0.0154 to 0.0166 apart there).
    q0 is +1.13e-6 at x 7.50, +4.5e-7 at 8.00, +6e-8 at 8.15, changes sign three times between 8.163 and 8.208, and is
    negative from 8.21 to beyond x*: -1.26e-6 at 8.355 (Richardson; spectral -1.28e-6), -9.4e-7 at 8.481, -7e-8 and
    -1.1e-7 at the nodes 8.598 and 8.610 on either side of x* = 8.60007, and at most 2.2e-7 in absolute value from 8.70 to
    8.9. The maximum of |q0| over [8, x* - eps] is 1.261e-6 at x 8.355 for every eps from 0.1 to 0.003, and over
    [8.4, x* - eps] 9.42e-7 at 8.481. Neighbouring nodes differ by up to 3.6e-7 (8.355 to 8.366): the profile varies on
    the knot scale and the node spacing does not resolve it, so the node maximum is a lower bound for the maximum over
    the interval. A run at N33750 (node spacing 0.0058) is queued (scratch/one_slot.sh, tag qp33750).
    Verdict (b): "below 1e-6 in absolute value on [8, x*)" REFUTED (node value -1.26e-6 at x 8.355). Wording until the
    N33750 profile: "|q0| reaches 1.3e-6 on [8, x*) (at x 8.36) and 9.4e-7 on [8.4, x*), at the radial nodes of a grid
    with spacing 0.012".

(c) fxfr1 (free continuation of the candidate). Method: shape lead work/c6/fxfr_c6f_m1.0e-03_shape.npz copied
    12:00:42Z (md5 3f4218ff..., equal to the lead's); my audit at N11250 q384 and N16875 q512; extra_checks at N11250 q384;
    857-label J, vaxis and vq0band (Ktop 300) at N16875 q384. Against the candidate at the same configurations.
    Result (fxfr1 / candidate; N11250 q384, then N16875 q512):
      N_f maximum in the box, next to P (2-10 band): 1.036e-6 / 6.98e-7, 1.020e-6 / 6.53e-7 (1.48 and 1.56 times higher).
      Lead scan (32768 x 640) 1.07e-6 against 6.77e-7: mine 0.95 to 0.97 of the lead's.
      10-100: 3.52e-7 / 4.37e-7, 5.11e-7 / 4.48e-7 (lead 3.49e-7). 0.1-2: 1.44e-7 / 1.72e-7, 1.51e-7 / 1.81e-7 (lead
      1.61e-7). 100-1000: 6.96e-8 / 6.87e-8, 7.24e-8 / 7.13e-8.
      N_v: box maximum (far field, r > 1000) 1.091e-6 / 1.132e-6, 1.101e-6 / 1.152e-6; r <= 1000 4.26e-7 / 5.20e-7,
      4.43e-7 / 5.32e-7 (2-10 band in both); within 0.5 of P 2.92e-7 / 1.87e-7, 2.87e-7 / 1.83e-7.
      c_l: identity on my inverse 5.575365143 (lead 5.575365146; +2.5e-6 from the candidate in 1000 iterations); root of
      h(P) = 1 at fixed rho 5.575365125 (-1.7e-8). h(P) - 1 +2.5e-7 (q384) and +2.0e-8 (q512), my quadrature pattern at
      P. D14 on [1e-3, 0.02]: E -5.0e-9, D2 +1.1e-8. One zero of W_1 on the x-axis (8.6000691), W_2/y >= 5.57557 on the
      y-axis, no open-quadrant cell with both components changing sign. B_3 (integrated form) 0.2984 / 0.2985.
      J on 857 labels, eps 0.03 / 0.01: 2.236e-6 / 2.416e-6 (candidate 2.738e-6 / 2.684e-6); 737 labels 2.236e-6 at eps
      0.03 (candidate 1.910e-6); family B 1.578e-6, family C 1.022e-6; both extremes in family A (+1.585e-6 at theta0
      1.5071, -6.51e-7 at 1.5404).
      Axis: I(0.03) 1.461e-6, I(0.01) 1.372e-6 (candidate 2.039e-6, 1.986e-6); top-band part of I(0.03) 1.565e-6
      (candidate 2.596e-6); max |q0| 8.90e-6 at x 3.58 (candidate 1.066e-5 at 3.57).
      Lead objective 7.4703e-6 against the candidate's 8.475e-6 (lead values).
    Reading. Continuing the candidate with c_l free lowers the L2 objective by 12 percent, the 857-label J by 18 percent
    and the axis integral by 28 percent, and raises the near-P maximum in N_f by 1.5 times and N_v within 0.5 of P by
    1.6 times; c_l moves by +2.5e-6, below the 1e-4 line of the lead's 12:02Z drift reading (no slope resolved). The
    candidate and fxfr1 are not ordered (the same split as the candidate against c6fs2i750 in G69).
    Verdict (c): the lead's fxfr numbers CONFIRMED (near-P N_f to 5 percent, c_l to 3e-9); fxfr1 is not a better
    candidate by the A1 rule (higher near-P N_f), and the candidate does not dominate it (higher J). The 737-label spread
    of fxfr1 is 1.17 times the candidate's: on the uniform labels alone the order of J is reversed.
    The lead's 11:56Z c_l reading (two free fits about 1e-3 apart in c_l, neither drifting toward the other, so c_l is
    quoted as an interval of at least [5.5753, 5.5764]): CONFIRMED on my values. Identity / root of h(P) = 1 at fixed rho:
    fxfr1 5.575365143 / 5.575365125; c6fs2i750 5.576364037 / 5.576364073 (G69); difference 9.99e-4. Over their last
    segments the drifts are +2.5e-6 (fxfr1, 1000 iterations, toward the other fit) and +1.6e-6 (c6fS1 5.576362428 to
    c6fs2i750, my identity values, 750 iterations, away from it), each below 3e-3 of the gap: neither moves measurably
    toward the other at these budgets.

(d) s2w1 (lead 11:53Z: stopped as failed, 2-10 N_f 5.75e-6 on the lead scan). Method: my audit at N11250 q384 and N16875
    q512. Result: N_f maximum in the box 4.527e-6 / 5.048e-6, at the first angle off the x-axis (theta 0.0033 at q384) at
    r 8.03; 10-100 1.21e-6 / 1.32e-6; 0.1-2 7.7e-8 / 8.4e-8; N_v maximum 1.31e-6 / 1.45e-6 (2-10). The maximum sits on the
    axis and grows as the first angle shrinks (q384, q512, the lead's 640 angles: 4.53e-6, 5.05e-6, 5.75e-6), so the
    three values are lower bounds of the same axis limit; the 10-100 values (lead 1.61e-6) differ for the same reason.
    Verdict (d): failed variant CONFIRMED on my evaluator (near-P N_f 6.5 to 7.7 times the candidate's).

(e) Text audits.
    FINAL_REPORT timeline entry "10:51 (addendum 10:53)" (lines 236-246 of the 11:43Z file): the sentence "The largest
    values come from labels whose characteristics run along the x-axis between the origin and P, where R/rho on the
    axis reaches 1.04e-5 on the candidate (8.0e-6 on the free control)" repeats my G69 reading, which G70 (b), (d)
    corrected: the maxima are 1.07e-5 and 8.2e-6, and the sentence holds for the family-B maximum only. A timeline
    entry may keep what was said at 10:51 if the report marks it as superseded; suggested addition after it: "(Corrected
    by VERIFY_REPORT G70 (b), (d): the maxima of R/rho on the axis are 1.07e-5 and 8.2e-6, and the axis carries only the
    family-B maximum; the family-A extremes take their J from the strip next to the x-axis and the disk at P, G71 (a).)"
    Its closure sentence (1 percent next to P, 7 percent for r < 1000) agrees with G69 (d): CONFIRMED.
    notes/final_sec5_v2_text.md (12:05Z), the [TBD] values that are mine: the generated field at N16875 q384 is 52 MB
    (52114788 bytes); gen_shape.py takes about 5 s there, vchar_dense.py on the 857 labels about 6 minutes (fxfr1:
    12:06:35Z to 12:12:38Z including the generation), vaxis.py about 2 minutes (12:12:38Z to 12:14:47Z), vq0band.py about
    2 minutes. The argument description of vchar_dense.py is correct. Reproducibility defect found and fixed in my lane at
    12:16Z: scratch/mk_traces.py (called by extra_checks.sh) inserted an absolute path to my code/ directory, so a copy of
    the artifacts would have imported my lane's files instead of its own; it now resolves ../code relative to its own
    location. The lead's notes/assemble_artifacts.sh must be re-run to pick up the fixed file.
    Verdict (e): the 10:51 entry needs the correction above (OPEN until entered); the section 5 v2 values supplied; the
    artifacts copy OPEN until re-assembled.

Verdict G71: no endpoint is confirmed and the team may NOT finish. Decided: the G70 (b) attribution (CONFIRMED for c6dS1
and the candidate in the form "k >= m_max", REFUTED in general) and the G70 (d) bound (REFUTED; q0 reaches 1.26e-6 on
[8, x*) at the nodes). fxfr1 and s2w1 CONFIRMED as the lead reports them; neither replaces the candidate. Pending: the
decisive pair s2g / seg3g of lead NOTES 12:02Z (jQ queue), the N33750 q0 profile, the free-branch 857-label J (dom300S1,
dom100S1, c6a/c6b/c6c S1) and the GPU chain 2 rows (jR queue).

## G72 The decisive pair s2g / seg3g by the lead's 12:02Z rule, what the long fixed-c_l continuation did to the candidate, q0 next to P at N33750, the free-branch 857-label J, and the solver-setting arms (2026-10-18T13:41:04Z)

Every number is from my generator and evaluator (code/gen_audit.sh, vchar_dense.py, vaxis.py, vq0band.py, vstrip.py,
vresmap.py, vjband.py, vq0prof.py; R 7.652e6) unless marked as a lead or numerics value. Tags: s2g, seg3g, reo_* as in
the numerics gpu_chain.log (numerics/leadcode/gpu); the candidate = fxm1o2i250 (fixc_c6f_m1.0e-03, outer 2, iterate 250).

(a) The decisive pair of lead NOTES 12:02Z item 3: s2g (the candidate continued at the fixed c_l 5.5753626) against seg3g
    (the free control c6f segment 2 continued with c_l free), same schedule and budget (20750 LSQR iterations each on the
    numerics GPU port). Method: both shapes copied from numerics/leadcode/gpu with the md5 checked against the "step N
    done" lines (s2g e3c529cca959e2c8b7e0e3fecfb3543d, seg3g 7536c587566834e14b780a7e086819fc); code/gen_audit.sh at
    N11250 q384 M479 and N16875 q512 M639 (the two configurations), vchar_dense (857 labels), vaxis, vq0band (Ktop 300) and
    vstrip at N16875 q384, extra_checks. The rule is applied by scratch/pair_rule.py: "not higher beyond the
    configuration spread" means A - B <= |B(config 1) - B(config 2)| on each configuration.
    Result (s2g / seg3g; two values are the two configurations):
      N_f box maximum                         1.424e-6, 1.435e-6 / 1.574e-6, 1.575e-6   both at (r 8.449 / 8.435, theta 0.0098)
      N_f 10 <= r <= 100                      2.62e-7, 3.59e-7 / 2.36e-7, 3.19e-7
      N_v r <= 1000                           3.975e-7, 4.005e-7 / 4.394e-7, 4.395e-7
      N_v r > 1000                            1.102e-6, 1.115e-6 / 1.097e-6, 1.108e-6     spread of seg3g 1.1e-8
      857-label J, eps 0.03 / 0.01            3.143e-6 / 3.462e-6 against 3.414e-6 / 3.763e-6
      I(0.03), I(0.01)                        -6.36e-7, -7.85e-7 / -7.04e-7, -8.68e-7
      max |q0| on (0, x*)                     3.13e-6 at x 2.80 / 3.21e-6 at x 2.85
      strip ripple R/rho, theta < 0.05        seg3g 3 to 5 percent above s2g on every row r 1 to 8.3
      identity c_l                            5.575362607 / 5.576370932
      root of h(P) = 1 minus identity c_l     -4.7e-9 / +4.2e-8
      h(P) - 1                                2.2e-7, 1.6e-8 / 1.5e-7, 2.0e-8
      solver objective at 20750 its           4.0967e-6 / 4.2586e-6 (numerics log)
      residual map |R|/N_f (N11250 q384), max  |X - P| < 0.5: 1.424e-6 / 1.574e-6; y < 0.2, x 6 to 8.1: 1.280e-6 / 1.346e-6;
                                              y 0.2 to 1, |x - x*| < 1: 1.211e-6 / 1.341e-6; y >= 1: 6.83e-7 / 6.22e-7
      theta spectrum of R/N_f, r 7 to 8.6     peak at omega 304 on both (2 m_max = 300), amplitude seg3g 4 to 11 percent higher
      family-A J remainder rms (vjband)       4.80e-7 / 5.24e-7; corr top 0.90 / 0.89, mid+top 1.00 / 1.00
    The rule: whole-box N_f lower for s2g on both configurations (ratio 0.905, 0.911); N_v for r <= 1000 not higher
    (0.905, 0.911; on both fits this maximum is in the band 2 <= r <= 10 next to P); N_v beyond 1000 higher by 5e-9 and 7e-9, inside the spread 1.1e-8, so not higher beyond it; J lower
    (0.92 at both eps). Every part holds: s2g is the candidate of the pair. The iteration counts are equal, so the
    10-percent clause does not apply; the numerics objectives at equal counts (2500 to 20750) favour s2g from 5000 its on
    (ratio 0.962 from 15000 on). seg3g's c_l drift over the continuation is +6.9e-6 (5.576364040 to 5.576370935, almost
    all in its first linearisation, then within 7e-7), below the 1e-4 line of the rule: no slope of c_l is resolved, and
    the drift points away from 5.5753626. The lead's and the numerics lane's scans (NOTES 12:52Z item 5, NOTES 13:29Z
    item 1: seg3g 2-10 N_f 1.59e-6, s2g 1.44e-6) agree with mine to 1 to 2 percent.
    What the rule does not decide. It compares s2g with seg3g only. Both continuations end with the near-P maximum above the
    pre-continuation candidate fxm1o2i250 (seg3g lowered its own start's, see G73 (e)): N_f 6.98e-7, 6.53e-7 there,
    a factor 2.0 to 2.4 lower than either member of the
    pair; the candidate is higher in N_v (5.20e-7 for r <= 1000, 1.132e-6 beyond) and lower in J (2.738e-6). By the same
    rule neither s2g nor seg3g replaces fxm1o2i250 and fxm1o2i250 does not replace them (N_v higher beyond the spread): the
    fits are not ordered. The long L2 continuation lowers the bulk and the axis from the origin to x 5 and raises the strip
    next to the x-axis from r 7 to P on both arms alike ((b) below); the residual maps of s2g and seg3g have the same
    structure, the same maximum point and the same cap frequency, seg3g 5 to 11 percent higher next to P and 9 percent
    lower for y >= 1.
    Far-field band (added 2026-10-18T14:07Z, after lead NOTES 13:36:38Z item 2: the lead's own scans, whose r >= 1000 band stops
    at the fit radius 1000 L = 7651, give s2g 6 percent higher there, which by the rule as written gives seg3g). Method: the same
    audits with VAUDIT_RFIT = 1000 L exported and no closure (scratch/ffband.sh; tags s2gFF, seg3gFF; code/vaudit.py adds the
    region 1000 <= r <= Rfit). Result (s2g / seg3g, N11250 q384 and N16875 q512):
      N_v max, 1000 <= r <= 1000 L (inside the fit domain)   2.513e-7, 2.514e-7 / 2.441e-7, 2.439e-7   at r about 6440, theta 1.136
      N_v max, r > 1000 L (the trial formula beyond the fit domain)   1.102e-6, 1.115e-6 / 1.097e-6, 1.108e-6   at r about 3.3e4
    Inside the fit domain s2g is higher by 2.9 and 3.1 percent (7.2e-9, 7.5e-9), against a configuration spread of 2e-10 for
    seg3g: higher beyond the spread. Over all r > 1000 the maximum lies beyond the fit domain, where s2g is higher by 0.5 and
    0.6 percent, inside that band's spread 1.1e-8. My values inside the fit domain are 2.4 times the lead's (the lead's scan
    closes the field at the fit radius; mine is the global formula). The sign of the difference agrees with the lead's; its
    size is half.
    Verdict (a), corrected the same hour: the 12:02Z rule does not fix the outer limit of its "r > 1000" band, and the outcome
    depends on it. Read as the maximum over all r > 1000 (my far field, to R 7.65e6), every part holds and s2g is the candidate
    of the pair. Read over 1000 <= r <= 1000 L (the region the fits were fitted on, and the lead's band), s2g's N_v is higher
    beyond the spread and seg3g is the candidate. Both are CONFIRMED as measurements. The band was not fixed in advance
    for this pair: the lead's NOTES 13:36:38Z item 2 says the rule is read on the verifier's far-field region, but my
    seg3g audit logs existed from 13:27:47Z and 13:31:36Z (runs/audit/jS.log), and the band "all r > 1000" was stated
    explicitly at 13:54:37Z, after the measurements, as the lead's FINAL_REPORT timeline (mtime 14:07:58Z, entry 13:41)
    itself says. I accept the decision s2g as the outcome of the rule under one admissible reading of an under-specified
    band, not as an outcome fixed beforehand. For the m <= 200 pair the band is fixed in advance: the lead's 14:04:12Z
    addendum (all r > 1000 decides, the fit band reported next to it) predates the first c6g iterate written to disk
    (c6g_shape.npz after outer 1, mtime 14:05:41Z) (CONFIRMED). The report must give both readings with their regions
    and say that under the fit-region reading the pair goes to seg3g. The margins are small in every part: s2g is lower
    in N_f by 9 to 10 percent and in J by 8 percent; the far N_v differ by 0.5 to 3 percent. The pair is one budget and
    one basis; its margin is one the rule reads, not a determination of c_l. For G20 (b1) the lowest whole-box N_f of
    all measured fits remains the pre-continuation candidate fxm1o2i250.

(b) What the long fixed-c_l continuation did to the candidate (s2g against fxm1o2i250; both at c_l 5.5753626, same
    basis: degree 375, m <= 150, the same 384 knots; max |z_s2g - z_cand| 4.8e-4). Method: as (a), plus the residual map
    (code/vresmap.py, N11250 q384 M479, window r 6 to 12, theta <= 0.6) compared with the candidate's map of G67 by
    scratch/cmp_resmap.py, vstrip (ripple next to the x-axis, N16875 q384) and vjband (73 + 20 labels, Ktop 300).
    Result (s2g / candidate):
      solver objective (numerics log, L2 on 20480 x 720)   4.097e-6 / 8.474e-6
      N_f box maximum, N11250 q384 / N16875 q512            1.424e-6 / 6.98e-7, 1.435e-6 / 6.53e-7
        its location                                        (x 8.449, y 0.083), next to the x-axis 0.15 left of P / (x 8.37, y 2.66)
      |R|/N_f on the map, max and rms over |X - P| < 0.5    1.424e-6, 6.0e-7 / 6.66e-7, 2.3e-7
        strip y < 0.2, 6 <= x < 8.1                         1.28e-6 / 5.0e-7
        y 0.2 to 1, |x - x*| < 1                            1.21e-6 / 6.6e-7
        y >= 1                                              6.8e-7 / 7.0e-7
      N_f 10-100 (N11250 q384)                              2.62e-7 / 4.37e-7
      N_v r <= 1000, r > 1000 (N11250 q384)                 3.98e-7, 1.102e-6 / 5.20e-7, 1.132e-6
      857-label J, eps 0.03 / 0.01                          3.143e-6 / 3.462e-6 against 2.738e-6 / 2.684e-6
        737 uniform labels, eps 0.03                        3.143e-6 / 1.910e-6
      I(0.03), I(0.01)                                      -6.36e-7, -7.85e-7 / +2.039e-6, +1.986e-6
      max |q0| on (0, x*)                                   3.13e-6 at x 2.80 / 1.07e-5 at x 3.5
      ripple R/rho next to the x-axis (theta < 0.05)        r 3 to 5: 2.3e-6 to 3.4e-6 / 8.2e-6 to 1.07e-5
                                                            r 7 to 8.3: 3.0e-6 / 1.1e-6 to 2.2e-6
      family-A J remainder (vjband), rms; corr top / mid+top 4.80e-7; 0.90 / 1.00 against 3.02e-7; 0.65 / 0.93
      identity c_l; root of h(P) = 1; h(P) - 1 (N11250)     5.575362607; -4.7e-9 from it; +2.2e-7 / 5.575362607; +2.5e-7
    The theta spectrum of R/N_f along r = 8.0 to 8.6 peaks at omega 304 on s2g (2 m_max = 300), and the R spectrum of the
    strip rows peaks in 290 to 310 from r 4 to 8.3 (on the candidate from r 4 to 7.6).
    The lead's scan of s2g (NOTES 12:52Z item 5: 2-10 N_f 1.444e-6 at r 8.37, theta 0.0123; 1.51e-6 at 960 angles; max
    |q0| 3.14e-6 at 2.81; I(0.03) -6.24e-7, I(0.01) -7.55e-7): CONFIRMED to 1.5 percent (N_f), 0.3 percent (max |q0|)
    and 2 to 4 percent (I).
    Reading. 20750 further LSQR iterations at the fixed c_l halved the L2 objective and lowered the residual on the
    x-axis from the origin to x 5 by a factor 3 (q0, I(eps)), and moved the residual at the angular cap frequency next to
    the x-axis to r 7 to 8.6 and above P, where it is divided by the small transport terms near the stagnation point:
    the near-P N_f maximum doubled and the 857-label J rose by 15 percent (64 percent on the uniform labels). The L2
    objective and the quantities G20 (b) reads are not ordered the same way along this continuation (the lead's 12:52Z
    point; numerics NUM_REPORT 3.18). For G20 (b1): continuing the candidate on its own basis at fixed c_l does not give a
    systematic improvement of the maximum residual; the candidate remains the lowest whole-box N_f of all fits measured.
    Verdict (b): measurements CONFIRMED (two evaluator resolutions agree to 0.8 percent on the near-P maximum); s2g is not
    an improvement of the candidate in N_f or J.

(c) q0 next to P at node spacing 0.0059 (G71 (b) follow-up). Method: code/vq0prof.py on the candidate generated at N33750
    q384 (radial node spacing 0.00586 near P, half the N16875 spacing), Richardson and spectral as in G71 (b).
    Result. Maximum of |q0| over [8, x* - eps], eps 0.1 to 0.003: 1.3030e-6 at x 8.3526 (spectral 1.3207e-6); the parabola
    through the maximal node and its neighbours gives 1.3031e-6 at 8.3524. Over [8.4, x* - eps]: 9.340e-7 at 8.4847 at
    the nodes, 9.452e-7 at 8.4823 by the parabola. At N16875 the same parabola gives 1.2734e-6 at 8.3523 and 9.420e-7 at
    8.4817. The two profiles differ by at most 3.07e-8 at the N16875 nodes below x* (N33750 interpolated). The largest
    difference of neighbouring nodes is 2.26e-7 at N33750 against 3.98e-7 at N16875: it halves with the spacing, so the
    profile is smooth on the node scale and the G71 (b) concern (a peak between nodes) is removed. Three sign changes in
    (8.166, 8.206), as at N16875.
    Verdict (c): the maximum of |q0| on [8, x*) is 1.30e-6 (at x 8.35; resolutions agree to 3e-8) and on [8.4, x*)
    9.5e-7 (at x 8.48): CONFIRMED. Wording for 4.4b: "|q0| reaches 1.3e-6 on [8, x*) (at x 8.35) and stays below 1e-6 on
    [8.4, x*)". The G71 (b) node-level wording is replaced.

(d) Free-branch 857-label J (G71 pending item). Method: vchar_dense (857 labels), vaxis at N16875 q384 on the m <= 100
    segment-1 shapes c6a (215 radial functions, fit grid 6144 x 480, 1.2 h), c6b (244, 10240 x 480, 1.8 h), c6c (302,
    20480 x 480, 1.8 h), c6d (375, 20480 x 480, 1.8 h; G70), and the domain fits dom300S1 and dom100S1 (c6d basis, fit
    convention with the lead's closure).
    Result (J spread eps 0.03 / 0.01; families A, B, C at eps 0.03; I(0.03); identity c_l):
      c6a S1   1.940e-5 / 1.940e-5   A 1.94e-5  B 2.04e-6  C 5.0e-7   -2.97e-7   5.576360711
      c6b S1   4.746e-6 / 4.980e-6   A 4.75e-6  B 1.76e-6  C 3.2e-7   -4.68e-7   5.576363250
      c6c S1   3.473e-6 / 3.607e-6   A 3.47e-6  B 2.01e-6  C 1.02e-6  +5.08e-7   5.576360941
      c6d S1   3.679e-6 / 3.669e-6   A 3.68e-6  B 1.95e-6  C 7.2e-7   +4.84e-7   5.576362170
      dom300S1 4.052e-6 / 4.185e-6   A 4.05e-6  B 1.92e-6  C 6.2e-7   +1.54e-7   5.576362820
      dom100S1 4.000e-6 / 4.087e-6   A 4.00e-6  B 1.89e-6  C 7.0e-7   +1.54e-7   5.576364428
    Reading. Along the radial sequence at m <= 100 the J spread falls by a factor 4 from 215 to 244 functions and by 27
    percent from 244 to 302, and rises by 6 percent from 302 to 375 (budgets equal from c6b on). The family-A labels carry
    the spread on every row; family B stays at 1.8e-6 to 2.0e-6 on all six. The domain rows at fit radii 300 and 100 are
    10 and 9 percent above c6dS1, within the variation of the radial sequence.
    Verdict (d): "J decreases under radial refinement at m <= 100" holds for the first two steps and fails at the last
    (302 to 375): REFUTED as a monotone statement, CONFIRMED as "J falls from 1.9e-5 to 3.5e-6 to 3.7e-6 and then stays
    within 6 percent". With G71 (a) (J on these fits is carried by residual at frequencies at or above the angular cap),
    the radial rows at m <= 100 are expected to stall at the angular floor; the angular row (c6g, m <= 200) is the test.

(e) The solver-setting arms (lead NOTES 12:52Z rule, numerics reotest2.sh steps 21, 22, 24 after the 12:58Z addendum;
    from the s2g end, one linearisation of 2500 its, fixed c_l). Method: copy with md5 check, gen_audit.sh N11250 q384 M479
    and N16875 q512 M639 (jT queue); objectives are the "actual" values of the "step N done" lines; the rule is read
    against the plain 1e-8 arm reo_plain8 (the production setting run for the same 2500 its).
    Result (objective at 2500 its; N_f box maximum = 2-10 maximum, next to P at r 8.48, theta 0.0098; N11250 q384, then
    N16875 q512 where measured):
      reo_plain8   (step 21, plain 1e-8)    4.07127e-6           N_f 1.423e-6, 1.434e-6   10-100 2.46e-7   N_v r > 1000 1.083e-6, 1.092e-6
      reo_reorth8  (step 22, CGS2 1e-8)     4.01919e-6 (0.9872)  N_f 1.348e-6, 1.388e-6   10-100 2.15e-7   N_v r > 1000 1.128e-6, 1.147e-6
      reo_plain12  (step 24, plain 1e-12)   4.07126e-6 (1.0000)  N_f 1.423e-6             10-100 2.59e-7   N_v r > 1000 1.084e-6
    (s2g, the common start: 4.0967e-6, N_f 1.424e-6.) reo_reorth8 has the lower 2-10 N_f (0.947, 0.968) but its objective
    is 1.3 percent lower, not 3 percent; reo_plain12 equals reo_plain8 to 3e-6 relative in the objective and to 0.1
    percent in N_f (damping is not the limit, as the lead's 12:58Z analysis states). Neither arm meets both parts of the
    rule. The numerics lane's setting.txt (13:52Z) is "--damping 1e-8", and chain 3 started with it (13:53:16Z).
    Verdict (e): by the 12:52Z rule no arm replaces plain damping 1e-8: CONFIRMED on my evaluator. Reorthogonalisation
    lowers the near-P maximum by 3 to 5 percent per 2500 its at a 4 to 5 percent higher far N_v; that is a reading of one
    linearisation, not a test of the setting over a full budget.

(f) Text audit of FINAL_REPORT (mtime 12:59:31Z; copy scratch/FINAL_REPORT_lead_1259.md). Method: each number of the new
    timeline entries against the G70 and G71 entries. The 10:51 entry now carries the correction suggested in G71 (e)
    ("Corrected by the verification entries of 12:09 and 12:26: the maxima of R/rho on the axis are 1.07e-5 on the
    candidate and 8.2e-6 on the free control ..."): resolved. The 12:09 entry: maxima next to P 1.07 to 1.11 times the
    full-domain fits (G70 (a): 1.07, 1.08; (e): 1.09 to 1.11), the 10-100 band 0.71 to 0.95 (G70 (a): 0.71 to 0.88; (e):
    0.92 to 0.95), c_l +4.9e-6 for the free fit, the m <= 100 to 150 step "at unequal budgets", the cap-frequency
    oscillation from r about 4 to P, q0 and I(eps) as differences of larger band parts, no domain study at m <= 150:
    CONFIRMED. The 12:26 entry: the J oscillation carried at or above the cap on the candidate and the m <= 100 fit and by
    no single band on the equal-budget free fit (G71 (a)); |q0| reaches 1.3e-6 on [8, x*) on the node grid of spacing
    0.012 (G71 (b): 1.26e-6; G72 (c) resolves the profile at spacing 0.0059: 1.30e-6); fxfr1 c_l +2.5e-6, L2 objective
    -12 percent (lead value), J -18 percent, near-P maximum 1.5 times (G71 (c): 1.48, 1.56); the interval of at least
    [5.5753, 5.5764]; the axis-weighted variant 6.5 to 7.7 times the candidate (G71 (d)): CONFIRMED. Sections 4 and 5
    remain [OPEN] with the 4.3 text audited before (G59 and later). The artifacts copy of scratch/mk_traces.py
    (lead/artifacts/d_evaluator/scratch/mk_traces.py, 10:42) still has the absolute path to my code/ directory.
    Verdict (f): the two new timeline entries CONFIRMED; the 10:51 correction entered; the artifacts copy OPEN until
    notes/assemble_artifacts.sh is re-run.

Verdict G72: no endpoint is confirmed and the team may NOT finish. Decided: by the 12:02Z rule s2g is the candidate of
the decisive pair ((a), CONFIRMED on my evaluator with the far band read as all r > 1000; on the fit-region band the rule
gives seg3g, see the (a) addendum); this rests on one budget and one basis, and it does not make s2g the
best fit: the pre-continuation candidate fxm1o2i250 keeps the lowest whole-box N_f measured (6.5e-7 to 7.0e-7 against
1.4e-6), with higher N_v and lower J, so the fits are not ordered and G20 (b1) "systematic improvement" is not shown by
the continuation ((b)). q0 next to P resolved ((c), CONFIRMED: 1.30e-6 on [8, x*), below 1e-6 on [8.4, x*)). The
free-branch J sequence at m <= 100 is not monotone at the last radial step ((d), REFUTED as monotone); the angular row
c6g (m <= 200) is the pending test of G20 (b3). The arms of (e) leave the setting at plain 1e-8, so chain 3 runs
without the s2gr / seg3gr re-run. Pending: chain 3 (the c6g / c6gF m <= 200 pair, the domain columns dom90c / dom300c,
fxd1g, fxb1g, the c_l profile rows).
Recommendation to the lead (G20 (b1), three domains): the domain rows exist at m <= 100 only (free: c6dS1, dom300S1,
dom100S1 / dom90; fixed c_l: fxd1, fxd300, fxd90). The candidate is at m <= 150, and gpu_chain2.sh has no
domain row at m <= 150. Whichever fit is put forward (fxm1o2i250 or s2g), a fixed-c_l domain pair at
its own basis and c_l (fit radii about 300 and 100, read with the fit's closure as in G64 / G70 (a), (e)) is required
before (b1) can be read at the candidate level. (Added after the check of gpu_chain3.sh: its steps 33 dom90c and 34
dom300c are this pair, fit radii 90 and 300 from the chosen candidate's end shape; my jU queue audits them in the fit
convention.)

## G73 (intermediate) The m <= 200 start and the first c6g iterate on my evaluator, q768 rows of the decisive pair, the configuration spread of the near-P maximum, and the FINAL_REPORT timeline entry 13:41 (2026-10-18T14:39:21Z)

Context: lead NOTES 14:02:21Z (c6g, fixed c_l, m <= 200, 20480 x 960, from the s2g end enriched to m <= 200, objective 42
percent lower after 1000 iterations; chain 5 order c6g, c6gF, domain pair) and 14:04:12Z (the far band of the m <= 200 pair
is all r > 1000, the fit band reported next to it). c6g has not finished; this entry is about its start and its first outer
iterate, and is not a reading of the pair. Evaluator: mine (code/gen_audit.sh: gen_shape.py, vaudit.py), R 7.652e6, between
fit nodes, k_self off, no closure, as in G72 (a).

(a) The start shape. c6g_start_shape.npz (md5 9dd60daff7e327234e401c9b2c07bb48, copied as runs/gen4/gpu/c6gst_shape.npz):
    75381 coefficients against s2g's 56631; the 18750 new ones (angular index 151 to 200) have size at most 2.0e-8, and the
    common ones differ from s2g's by at most 2.0e-8 (relative 3e-9). Same c_l, k, c, degree 375, R_shape 1000. At N11250 q384
    M479: whole-box N_f 1.419e-6 (s2g 1.424e-6) at the same point (8.449, 0.0098), N_v 2-10 3.962e-7 (3.975e-7), far N_v
    1.092e-6 (1.102e-6), 185-label J spread at 0.03 2.634e-6 (2.652e-6). The 10-1000 band maxima differ by 1 to 8 percent:
    the new coefficients are small but not zero. Verdict: my evaluator reads the enriched basis (angular index to 200) and
    reproduces s2g on it. CONFIRMED.

(b) The first outer iterate. c6g_shape.npz as written after outer 1 (2500 LSQR iterations, objective 1.991840e-6; file mtime
    14:05:41Z, md5 26afa89f2b5efdbeaefa61790e240261, copied as runs/gen4/gpu/c6go1_shape.npz). This is an intermediate
    iterate, not an end shape. Rows (whole-box N_f with location; N_f within |X - P| < 0.5; N_v 2-10; far N_v r > 1000;
    185-label J spread at |X - P| = 0.03 and 0.01):
      N11250 q384 M479    1.009e-6 (8.466, 0.0164)   1.009e-6   2.819e-7   1.118e-6   1.587e-6  1.876e-6
      N16875 q512 M639    1.033e-6 (8.470, 0.0172)   1.033e-6   2.888e-7   1.128e-6   1.653e-6  1.974e-6
      N16875 q768 M959    1.047e-6 (8.470, 0.0164)   1.047e-6   2.926e-7   1.148e-6   1.653e-6  1.974e-6
      N11250 q1024 M1279  1.206e-6 (9.058, 1.5696)*  9.999e-7   2.987e-7   1.151e-6   1.587e-6  1.877e-6
    (* the y-axis floor column of G67 (c); the near-P value is the one to read.) identity c_l 5.575362607 at all four; s2g
    5.575362607. Against s2g on the same configurations the near-P maximum is 0.70 to 0.72 times s2g's, N_v 2-10 0.70 to
    0.72 times, and the J spreads 0.60 to 0.66 times; the far N_v is 1.2 to 1.5 percent higher (1.118e-6 against 1.102e-6 at
    N11250 q384, 1.128e-6 against 1.115e-6 at N16875 q512, 1.148e-6 against 1.132e-6 at q768). Residual map at N11250 q384
    (code/vresmap.py, scratch/cmp_resmap.py): the ripple next to the x-axis peaks at omega 399 (s2g 304), that is at twice
    the new angular cap, with amplitude 8.3e-8 at r 8.449 (s2g 1.59e-7). Verdict: on its first outer iterate the m <= 200
    fit lowers the near-P maximum and J with the objective, and the cap ripple moves to the new cap frequency at half the
    amplitude. This supports the lead's reading that the m <= 150 fits were limited by the angular basis. It says nothing
    yet about the end of c6g, about c6gF, or about the pair. CONFIRMED as a measurement of the iterate.

(c) The q768 rows of the decisive pair (N16875 q768 M959; runs/audit/{s2g,seg3g}_N16875_q768_R7.652e6.log):
      s2g    whole-box N_f 1.505e-6 at (8.401, 0.0115); N_v 2-10 4.200e-7; far N_v 1.132e-6; J spread 0.03 / 0.01 2.678e-6 / 2.997e-6
      seg3g  whole-box N_f 1.643e-6 at (8.435, 0.0115); N_v 2-10 4.587e-7; far N_v 1.125e-6; J spread 0.03 / 0.01 2.885e-6 / 3.235e-6
    On this row too s2g is lower in N_f (0.916 times), N_v r <= 1000 and J, and its far N_v (+7e-9) lies inside the spread of
    seg3g over the three configurations (1.097e-6, 1.108e-6, 1.125e-6). The 12:02Z pair reading of G72 (a) (band all
    r > 1000) is unchanged. CONFIRMED.

(d) The configuration spread of the near-P maximum. The sampled near-P maximum moves with the grid by more than the two
    G72 (a) configurations showed:
      s2g    1.424e-6 (N11250 q384), 1.435e-6 (N16875 q512), 1.505e-6 (N16875 q768): spread 5.7 percent
      seg3g  1.574e-6, 1.575e-6, 1.643e-6: spread 4.4 percent
      c6go1  1.009e-6, 1.033e-6, 1.047e-6, and 9.999e-7 at N11250 q1024: spread 4.7 percent, not monotone in q
    The quantity is the maximum over grid points of a residual that oscillates at the cap frequency next to P, so every grid
    reads it low by an amount that depends on where the samples fall. In G72 (a) the N_f spread was 0.8 percent because only
    two configurations were read (seg3g: 0.1 percent). Consequences: (1) N_f values should be quoted as the range over at
    least the three configurations of (b) (N11250 q384, N16875 q512, N16875 q768), and fits compared configuration by
    configuration; (2) no N_f maximum is known to better than about 5 percent; (3) none of this changes an ordering found so
    far, since the differences between fits are larger than 5 percent (s2g against seg3g 8 to 10 percent; c6go1 against s2g
    28 to 30 percent). CONFIRMED.

(e) FINAL_REPORT timeline (mtime 14:08:27Z; copy scratch/FINAL_REPORT_lead_1408.md), entry 13:41 (the verifier evaluation of
    the long continuations). Checked against G72, its (a) addendum and G69 (e): the pair kept by the rule with the far band
    all r > 1000; on the fit band 1000 <= r <= 1000 L the fixed-c_l fit 3 percent higher beyond the spread, which would keep
    the free one; the band fixed by the lead at 13:54, after the measurements; margins 9 percent (N_f), 8 percent (J), 0.5
    to 3 percent (far N_v); the fixed-c_l continuation halved the objective and doubled the near-P maximum (6.5e-7 to 7.0e-7
    before, 1.4e-6 after); the free continuation lowered its objective by 40 percent and its near-P maximum from 2.1e-6 to
    2.3e-6 (F1, G69 (e): 2.087e-6 to 2.327e-6 over six configurations) to 1.6e-6 (seg3g 1.574e-6 to 1.643e-6); the fit
    before the continuation keeps the lowest whole-box N_f, so the fits are not ordered; the cap-frequency residual next to
    the x-axis from r 7 to P on both continuations; |q0| 1.3e-6 on [8, x*) and below 1e-6 on [8.4, x*); the arms did not
    change the setting. The 14:07:58Z version had said that both continuations doubled the near-P maximum; the lead
    corrected it at 14:08:27Z (NOTES 14:12:59Z item 2), and my G72 summary line and G72 (a) had the same ambiguity ("raised
    to twice the pre-continuation candidate's"), corrected now. Two wordings remain: the free-branch 857-label J "then stays
    within 6 percent" (3.47e-6 to 3.68e-6 is 6.1 percent): "within about 6 percent" or "rises by 6 percent"; and "1.4e-6
    after" is the q384 / q512 value of s2g, 1.5e-6 at q768 ((d)). Verdict: CONFIRMED with these two wordings.

Verdict G73 (intermediate): no endpoint is confirmed and the team may NOT finish. The m <= 200 start reproduces s2g on my
evaluator; the first outer iterate of c6g lowers the near-P maximum by 28 to 30 percent and the J spreads by 34 to 40 percent
against s2g, with the cap ripple moved to omega 399. Pending: the end of c6g (step 31) and c6gF (step 32), their pair by the
12:02Z rule with the band fixed at 14:04:12Z, the G20 (b3) angular row s2g / c6g on the 857-label J, and the domain pair.
The near-P N_f maxima carry a configuration spread of about 5 percent, to be quoted as a range.

## G73 c6g end (the m <= 200 fixed-c_l continuation of s2g) on my evaluator, s2g and seg3g with the A5 rows, and the equal-budget angular row (2026-10-18T15:30:51Z)

Method. c6g_shape.npz copied from the numerics leadcode/gpu/c6g/ at 2026-10-18T15:05:56Z, md5 15f8095f7e79dbfa0c50d75e5fe8997a,
equal to the md5 in the chain line "2026-10-18T15:05:48Z step 31 done" (20750 LSQR iterations from c6g_start, objective
1.6192702e-6 on 20480 x 960, fixed c_l 5.575362610641546, m <= 200, damping 1e-8). My generator and evaluator (code/gen_shape.py,
code/vaudit.py: own differentiation, own full-plane inverse) at N11250 q384 M479, N16875 q512 M639, N16875 q768 M959 and
N22500 q512 M639, all R 7.652e6; code/extra_checks.sh at N11250 q384; the 857-label J (code/vchar_dense.py, N16875 q384),
vstrip and the q0 band split from the same run; the far field split at the fit radius 1000 L (scratch/ffband.sh, tag c6gFF).
Addenda (g), (h) entered 2026-10-18T15:54:16Z; (i) entered 2026-10-18T15:55:20Z.
New in vaudit.py (2026-10-18T14:51Z and 14:59Z, backups code/vaudit_pre_A5.py, code/vaudit_pre_A5b.py): the rows of A5 of
G67 (g), i.e. the maxima with the evaluation columns pi/2 - theta < 0.006 next to the y-axis excluded ('all,ya>=0.006',
'r<=1000,ya>=0.006', 'r>1000,ya>=0.006', and with VAUDIT_RFIT the fit-band variants), and the location of each N_v maximum
in the JSON. s2g and seg3g were re-audited with these rows on the three configurations of G73 (intermediate) (d) (tags s2gA,
seg3gA; the other rows reproduce G72 (a) and G73 (intermediate) (c) to the printed digits). scratch/pair_rule.py reads the A5
rows and prints the 12:02Z rule with and without them.

(a) s2g against seg3g with the A5 rows (the decided pair, G72 (a)). Result, N11250 q384 / N16875 q512 / N16875 q768:
      whole-box N_f, A5               s2g 1.424e-6, 1.435e-6, 1.505e-6   seg3g 1.574e-6, 1.575e-6, 1.643e-6   (= without A5)
      N_v r <= 1000, A5               s2g 3.975e-7, 4.005e-7, 4.200e-7   seg3g 4.394e-7, 4.395e-7, 4.587e-7   (= without A5)
      N_v r > 1000, without A5        s2g 1.102e-6, 1.115e-6, 1.132e-6   seg3g 1.097e-6, 1.108e-6, 1.125e-6   ratio 1.005-1.006
      N_v r > 1000, A5                s2g 1.068e-6, 1.063e-6, 1.069e-6   seg3g 1.070e-6, 1.064e-6, 1.071e-6   ratio 0.998-0.999
    Without A5 the far N_v maximum of both fits is in the column nearest the y-axis (theta 1.5692 at q768, r 3.4e4 to 3.6e4);
    with A5 it moves to theta 1.5643, the first column past the cut (r 3.7e4 to 3.8e4). The rule gives s2g with and without
    A5. Whether A5 applies in the far field is settled by (g): it does not (there the residual next to the y-axis is 24 to 84
    times the on-axis floor and R/N_v has a smooth limit at the axis), so the far band is read without A5, as in G72 (a):
    s2g 0.5 percent higher, inside seg3g's configuration spread. CONFIRMED (the pair decision is unchanged).

(b) c6g rows against s2g, configuration by configuration (A5 applied; where it changes a value, the value without A5 is given):
      configuration      whole-box N_f (at r, theta)          N_v r <= 1000         N_v r > 1000 A5 (without)   185-label J 0.03 / 0.01
      N11250 q384 M479   c6g 6.909e-7 (8.784, 0.3076)         1.920e-7              1.084e-6 (1.090e-6)         1.232e-6 / 1.424e-6
                         s2g 1.424e-6 (8.449, 0.0098)         3.975e-7              1.068e-6 (1.102e-6)         2.652e-6 / 2.942e-6
      N16875 q512 M639   c6g 6.841e-7 (8.528, 0.0074)         1.917e-7              1.074e-6 (1.101e-6)         1.271e-6 / 1.493e-6
                         s2g 1.435e-6 (8.435, 0.0098)         4.005e-7              1.063e-6 (1.115e-6)         2.678e-6 / 2.997e-6
      N16875 q768 M959   c6g 7.156e-7 (8.528, 0.0082)         2.005e-7 (2.485e-7)   1.077e-6 (1.111e-6)         1.270e-6 / 1.492e-6
                         s2g 1.505e-6 (8.401, 0.0115)         4.200e-7              1.069e-6 (1.132e-6)         2.678e-6 / 2.997e-6
      N22500 q512 M639   c6g 6.832e-7 (8.524, 0.0074)         1.914e-7              1.075e-6 (1.103e-6)         1.274e-6 / 1.502e-6
    Ratios c6g / s2g on the three common configurations: N_f 0.475 to 0.485; N_v r <= 1000 0.477 to 0.483; 185-label J 0.46 to
    0.50; far N_v without A5 0.981 to 0.989, with A5 1.007 to 1.015 (s2g's A5 spread over the three: 6e-9). By (g) the far
    band is read without A5: c6g is 1.1 to 1.9 percent below s2g beyond r 1000. The N_f maximum of c6g is next to P at q512
    and q768 (|X - P| < 0.5: 6.505e-7, 6.841e-7, 7.156e-7); at q384 the whole-box value 6.909e-7 is at x 8.37, y 2.66, the place of fxm1o2i250's maximum (G72 (b)). The
    four configurations of c6g give N_f 6.83e-7 to 7.16e-7 (spread 4.7 percent, within the 5 percent of G73 (intermediate)
    (d)), J 1.23e-6 to 1.27e-6 at 0.03. At q768 the y-axis floor columns hold 2.485e-7 (N_v, r <= 0.1) and 5.1e-7 (N_f, 10 to
    100, theta 1.5692), below the near-P values. CONFIRMED as measurements.

(c) Fit band. c6gFF (VAUDIT_RFIT = 1000 L = 7651.4, no closure, N11250 q384 / N16875 q512): N_v on 1000 <= r <= 1000 L 2.152e-7
    at r 7647, theta 1.554 (same with A5), against s2g 2.513e-7 / 2.514e-7 and seg3g 2.441e-7 / 2.439e-7 (G72 (a) addendum;
    re-run with the A5 rows as tags s2gAFF, seg3gAFF at N11250 q384 / N16875 q512: unchanged by A5); beyond 1000 L 1.090e-6
    (A5 1.084e-6). Beyond the fit radius every fit measured here reads 1.06e-6 to 1.15e-6 (s2g, seg3g, c6g, the reo arms of
    G72 (e), fxm1o2i250 1.132e-6): that band is hardly moved by the fit, and the differences between fits there are 0.5 to 2
    percent (their sign with A5 differs, but A5 does not apply there, (g)). Inside the fit radius c6g is the lowest of the
    three. CONFIRMED.

(d) The 857-label J (N16875 q384; G20 (b3) angular row). c6g: spread 1.388e-6 / 1.602e-6 at eps 0.03 / 0.01 (family A 737
    labels 1.341e-6 / 1.563e-6, B 2.51e-7 / 2.55e-7, C 7.23e-7 / 8.46e-7); s2g 3.143e-6 / 3.462e-6 (A 3.143e-6 / 3.462e-6, B
    6.46e-7 / 6.54e-7, C 1.405e-6 / 1.560e-6); fxm1o2i250 2.738e-6 / 2.684e-6 (G72 (b)). Ratio c6g / s2g 0.44 / 0.46 on the
    857 labels; by family A 0.43 / 0.45, B 0.39 / 0.39, C 0.51 / 0.54, below 1 on every family (wording corrected
    2026-10-18T16:26:28Z after the lead's 16:23:45Z item 1, which reads it correctly). c6g is the first audited
    fit with both the lowest whole-box N_f range (level with fxm1o2i250's 6.5e-7 to 7.0e-7) and a J below fxm1o2i250's (by
    a factor 2.0).
    Budget. c6g is s2g plus 20750 iterations, so the s2g / c6g row mixes refinement and budget. Equal-budget row, all from the
    s2g end at the same fixed c_l, plain damping 1e-8, one linearisation of 2500 iterations, on my evaluator:
      reo_plain8 (m <= 150, 20480 x 720; G72 (e))   N_f 1.423e-6 / 1.434e-6    185-J 0.03 / 0.01 2.554e-6 / 2.804e-6, 2.577e-6 / 2.854e-6
      c6go1      (m <= 200, 20480 x 960; G73 (i))   N_f 1.009e-6 / 1.033e-6    185-J 0.03 / 0.01 1.587e-6 / 1.876e-6, 1.653e-6 / 1.974e-6
    (N11250 q384 / N16875 q512.) At equal budget the m <= 200 iterate is 0.71 to 0.72 of the m <= 150 one in N_f and 0.62 to
    0.69 in J; the m <= 150 iterate is 0.999 times s2g in N_f and 0.95 to 0.96 in J. The two runs also differ in the number of
    collocation angles (960 against 720), so the row attributes the gain to the m <= 200 setup (basis and grid together), not to
    the basis alone. The angular row of G20 (b3) is therefore: J falls from m <= 150 to m <= 200 at the fixed c_l, both at the
    end of the run (0.44) and at equal budget (0.62 to 0.69). The m <= 100 member (fxd1g, step 35) is pending. CONFIRMED for the
    two members measured.

(e) Centre, c_l, zeros (extra_checks N11250 q384; all configurations for the identity). Identity c_l 5.575362607 on every
    configuration (fixed value 5.575362611: difference -3.2e-9, as on s2g); c_l from h(P) = 1 at fixed rho 5.575362614
    (+6.95e-9 from the identity; s2g -4.66e-9), dh/dc_l 1.079; c 15.72608782, A 10.1507252, beta - alpha -0.13158031 (s2g:
    the same to 1e-9). h(P) - 1: 2.84e-7 (N11250), 3.11e-8 (N16875), -1.78e-8 (N22500), at my grid error (s2g 2.15e-7,
    1.55e-8). W_1 on the x-axis vanishes only at x* 8.6000635; min W_2/y on the y-axis 5.5756 (at y 7.5e6); no open-quadrant
    cell where both W components change sign; min |W|/(c_l |X|) 0.0216 / 0.0065 / 0.0026 at |X - P| 1 / 0.3 / 0.1. CONFIRMED.

(f) The cap ripple. vstrip (N16875 q384, the strip next to the x-axis, r 7.0 to 8.3): the angular spectrum of R is carried by
    the band 400 to 600 (1.2e-6 to 3.9e-6), against 290 to 310 for s2g (3.1e-6 to 1.3e-5): the ripple sits at about 2 m_max on
    both and is 3.4 times lower at r 8.3. The x-axis q0 maximum is 1.29e-6 at x 6.64 (s2g 3.13e-6 at x 2.80). The residual
    map near P (scratch/cmp_resmap.py against s2g) is in (h). CONFIRMED for the rows given.

(g) Does A5 apply in the far field? A5 (G67 (g)) was introduced for the N_f floor of the odd sine series next to the y-axis
    near r 9 (G67 (c)), where the residual at the column next to the axis is set by the on-axis value. Method: residual map
    of s2g by code/vresmap.py at N16875 q768 M959 (tag s2g_fary768), window r 1e4 to 1e5 (1688 radii), the full quadrant (961
    angles, step 0.00164), read by scratch/fary_look.py: the on-axis column (theta = pi/2, where R, rho and N_v vanish
    exactly), and per band of pi/2 - theta the N_v maximum, its location, and the floor-subtracted ratio |R - R_axis(r)| / N_v.
    Result. On the axis column |R| <= 9.46e-9, |rho| <= 2.8e-11, N_v <= 1.7e-9 (the evaluator floor). N_v maxima by band of
    pi/2 - theta: [0, 0.003) 1.132e-6 (r 3.43e4), [0.003, 0.006) 1.106e-6, [0.006, 0.01) 1.069e-6, [0.01, 0.02) 1.065e-6,
    [0.02, 0.05) 1.053e-6, [0.05, 0.2) 7.5e-7, beyond 2.9e-7; the floor-subtracted values equal the raw ones to 4e-9 in every
    band. At the column next to the axis R = 2.21e-7 against the on-axis R(r) 2.6e-9 (84 times; the band maximum of |R| is 24
    times the on-axis maximum), and R and N_v both grow as (pi/2 - theta)^2 over the first columns (R 2.21e-7, 8.67e-7,
    1.92e-6; N_v 0.195, 0.783, 1.77), so R / N_v has a finite limit at the axis. The column profile of N_v is smooth
    (1.132, 1.106, 1.086, 1.069, 1.054, 1.045, 1.042, 1.045, 1.052, 1.060, 1.065, 1.063 e-6 over the first twelve columns).
    The far N_v next to the y-axis is therefore a residual of the fit, not the evaluator floor, and A5 does not apply beyond
    r 1000: the far band is read without A5 (as in G72 (a) and the lead's scans), A5 stays for the N_f floor near r 9 where
    G67 (c) shows it. Consequences, already entered in (a) to (c): s2g / seg3g far N_v ratio 1.005 to 1.006 (inside the
    configuration spread; the pair decision is unchanged), c6g / s2g 0.981 to 0.989. The A5 column of scratch/pair_rule.py
    is kept as a printed row and does not decide. CONFIRMED (A5 limited to the near-field N_f).

(h) The residual map next to P (lead NOTES 15:11Z item 5) and the N11250 lobe. code/vresmap.py on c6g and s2g (window r 6
    to 12, theta <= 0.6) at N11250 q384 M479 (tags c6g, s2g), N16875 q384 M479 (c6g16384), N16875 q512 M639 (c6g512,
    s2g512) and N22500 q512 M639 (c6g22512), read with scratch/cmp_resmap.py. Result, R/N_f maxima N11250 q384 / N16875 q512
    (s2g -> c6g):
      |X - P| < 0.5                 1.424e-6 -> 6.505e-7 (rms 6.0e-7 -> 2.5e-7) / 1.435e-6 -> 6.841e-7 (rms 6.1e-7 -> 2.6e-7)
      strip y < 0.2, 6 < x < 8.1    1.280e-6 -> 5.35e-7 / 1.334e-6 -> 5.56e-7
      y < 0.2, x > x*               5.80e-7 -> 2.70e-7 / 4.52e-7 -> 1.83e-7
      y 0.2 to 1, |x - x*| < 1      1.211e-6 -> 5.34e-7 / 1.239e-6 -> 5.68e-7
      y >= 1                        6.83e-7 -> 6.91e-7 (both at x 8.372, y 2.660) / 5.32e-7 -> 4.32e-7
    The theta spectrum of R/N_f on the rows r 7.0 to 8.6 peaks at omega 304 on s2g and 399 on c6g (2 m_max), with amplitude
    2.6 to 3.1 times lower on c6g, on both grids. So near P every window falls by a factor 2.1 to 2.5, except y >= 1 at
    N11250. That point (r 8.784, theta 0.3076, N_f 159, R -1.1e-4) gives 6.83e-7 / 6.91e-7 / 6.98e-7 on s2g / c6g /
    fxm1o2i250 at N11250 q384, the same within 2 percent on three different fits, and it is the whole-box N_f maximum of c6g
    at N11250 q384 (6.909e-7 in (b)). The lobe maximum (r 8.63 to 8.93, theta 0.265 to 0.345) is 4.15e-7 at N16875 q384,
    4.13e-7 at N16875 q512 and 3.95e-7 at N22500 q512 on c6g (s2g 4.27e-7 at N16875 q512). It follows the radial evaluation
    grid, not the angular one. Along theta 0.3076 the c6g residual oscillates in r with period about 0.036 and amplitude
    about 2e-7, the same phase on N16875 and N22500 (signs + - + - at r 8.776, 8.794, 8.812, 8.836). On N11250, with spacing
    0.018 (two points per period), it appears as a grid-scale alternation +4.5e-7, -6.9e-7, +3.4e-7 at r 8.766, 8.784, 8.802.
    The N11250 lobe value is therefore an under-resolution artifact of my N11250 radial grid, 1.7 times the value at
    N >= 16875. Consequences:
    (h1) The c6g rows in (b) stand as measurements. On N >= 16875 the whole-box N_f of c6g is the near-P maximum (6.54e-7 at
         N16875 q384, 6.84e-7 / 7.16e-7 / 6.83e-7 at N16875 q512 / q768, N22500 q512). G67 (b), "the off-axis lobe ... becomes
         the N_f maximum on the coarsest grid", is amended to: on the coarsest grid it is resolution-limited.
    (h2) For any fit whose near-P maximum is below about 7e-7, the N11250 q384 whole-box N_f is pinned at 6.8e-7 to 7.0e-7 by
         this artifact and does not separate fits. Fixed at 2026-10-18T15:54:16Z, before any c6gF row exists, for the c6g / c6gF pair
         (12:02Z rule) and for the angular row of 15:14:26Z: I report every configuration. The whole-box N_f comparison
         decides on the configurations with N >= 16875 (N16875 q512, N16875 q768, and N22500 q512, which I run for c6gF
         through scratch/c6gF_a3_wait.sh). If the N11250 row and the N >= 16875 rows disagree, the N >= 16875 reading decides
         and both readings are printed. scratch/pair_rule.py prints both (backup scratch/pair_rule_preG73h.py). The N_v
         rows are not affected (c6g N_v r <= 1000 1.920e-7 at N11250 against 1.917e-7 at N16875).
    (h3) c6g far field next to the y-axis (as (g), tag c6g_fary768): the axis column floor is |R| <= 8.9e-9. The N_v maximum
         is 1.111e-6 at the column next to the axis (r 3.67e4; floor-subtracted 1.123e-6), against s2g's 1.132e-6
         (ratio 0.981). Column profile 1.111, 1.096, 1.082, 1.077, 1.073, 1.073 e-6. As on s2g it is a residual of the fit.
    CONFIRMED (near-P windows and spectrum); the reading (h2) is fixed for the pair and the row.

(i) Quotes of this entry. numerics/NUM_REPORT.md (mtime 15:35Z) section 4 (l) item 5 and its last paragraph quote the 15:30:51Z
    text correctly, but (g) supersedes two of its statements. First, "far N_v (all r > 1000) 1.074-1.084e-6 with A5 against
    s2g 1.063-1.069e-6 (c6g HIGHER by 0.7-1.5 percent ...)" and "0.7-1.5 percent above s2g with the evaluator's A5
    correction". The far band is read without A5: c6g 1.090e-6 / 1.101e-6 / 1.111e-6 against s2g 1.102e-6 / 1.115e-6 /
    1.132e-6, 1.1 to 1.9 percent lower. Second, "A5 = the far-field correction of their evaluator". A5 is not a correction. It
    excludes the evaluation columns with pi/2 - theta < 0.006, and it is justified only for the near-field N_f floor of
    G67 (c). The rest of the quoted rows (whole-box N_f, N_v r <= 1000, fit band, 185 and 857 J, equal-budget row) match (b)
    to (d). One addition from (h): the N11250 q384 whole-box values 6.909e-7 (c6g) and 6.98e-7 (fxm1o2i250, G72 (b)) are
    the under-resolved N11250 lobe. At N16875 q512 the whole-box values are 6.841e-7 (c6g, next to P) and 6.53e-7
    (fxm1o2i250).

Verdict G73 (c6g end): the measurements are CONFIRMED. c6g lowers the whole-box N_f by a factor 2.1 against s2g on every
common configuration (to 6.8e-7 to 7.2e-7), N_v for r <= 1000 by 2.1 and the 857-label J by 2.3, with the centre jet, c_l,
h(P) and the zero set unchanged; beyond r 1000 it is 1 to 2 percent below s2g (read without A5, (g)). By the lead's 14:02Z
rule c6g becomes the candidate if it wins its pair against c6gF (step 32, running; 12:02Z rule, far band all r > 1000 fixed
at 14:04:12Z; whole-box N_f read on N >= 16875 by (h2)): on my rows its whole-box N_f is lower than s2g's on every
configuration. This is not yet an endpoint: G20 (b1) needs the domain pair at the candidate's basis and three resolutions,
and (b4) the report text. The team may NOT finish.

### G74. The m <= 200 pair c6g / c6gF (step 32) on my evaluator; candidate; lead requests 16:23:45Z item 4. Recorded 2026-10-18T16:44:40Z
Method. c6gF_shape.npz (step 32, done 16:09:14Z, 20750 iterations; md5 0398af3f08a2a4f75e42c846edbaa375, the same on the
chain line, the lead's copy and NUM_REPORT item 7) through my chain as c6g in G73: code/gen_audit.sh (own generator and
inverse, formula to R 7.652e6) at N11250 q384 M479, N16875 q512 M639, N16875 q768 M959 and N22500 q512 M639; extra_checks
(N11250 q384); vchar_dense (857 labels), vaxis, vq0band and vstrip at N16875 q384; the fit band (VAUDIT_RFIT = 1000 L, tag
c6gFFF); residual maps (code/vresmap.py, tags c6gF, c6gF512) compared window by window with c6g's on the same grids
(scratch/cmp_resmap.py). Reading by scratch/pair_rule.py c6g c6gF: the 12:02Z rule with the far band all r > 1000
(14:04:12Z), read without A5 (G73 (g)), whole-box N_f decided on N >= 16875 (G73 (h2), fixed 15:54:16Z before any c6gF
row); the candidate by the 14:02Z rule.

(a) Rows c6g / c6gF (A5 applied where it changes a value; the value without A5 in brackets):
      configuration      whole-box N_f (at r, theta)                  N_v r <= 1000         N_v r > 1000 (no A5)  185-label J 0.03 / 0.01
      N11250 q384 M479   c6g  6.909e-7 (8.784, 0.3076; N11250 lobe)    1.920e-7              1.090e-6              1.232e-6 / 1.424e-6
                         c6gF 6.947e-7 (8.501, 0.0164)                 1.945e-7              1.087e-6              1.316e-6 / 1.535e-6
      N16875 q512 M639   c6g  6.841e-7 (8.528, 0.0074)                 1.917e-7              1.101e-6              1.271e-6 / 1.493e-6
                         c6gF 7.303e-7 (8.528, 0.0074)                 2.047e-7              1.098e-6              1.353e-6 / 1.590e-6
      N16875 q768 M959   c6g  7.156e-7 (8.528, 0.0082)                 2.005e-7 (2.485e-7)   1.111e-6              1.270e-6 / 1.492e-6
                         c6gF 7.652e-7 next to P (8.599e-7 at 9.524, 1.5692)  2.144e-7 (3.012e-7)  1.111e-6       1.352e-6 / 1.590e-6
      N22500 q512 M639   c6g  6.832e-7 (8.524, 0.0074)                 1.914e-7              1.103e-6              1.274e-6 / 1.502e-6
                         c6gF 7.280e-7 (8.524, 0.0074)                 2.039e-7              1.101e-6              1.358e-6 / 1.603e-6
    Ratios c6g / c6gF. Whole-box N_f on N >= 16875: 0.937, 0.832 (A5 0.935), 0.938; at N11250 q384 0.995 (the lobe of
    G73 (h); next to P 0.936). Next to P (|X - P| < 0.5) 0.935 to 0.938 on all four configurations. N_v r <= 1000 0.936 to
    0.987 at q384 and q512, 0.825 at q768 (A5 0.935). Far N_v 1.000 to 1.003: c6g is above c6gF by at most 3e-9,
    against c6gF's configuration spread 2.4e-8 (with A5, not used: 1.004 to 1.005, 5e-9 against 1.0e-8). 185-label J
    0.928 to 0.939.
    The q768 whole-box maximum of c6gF is in the column next to the y-axis at r 9.5 (theta 1.5692, the evaluator floor
    of G67 (c)); with A5 it is next to P. The 10 <= r <= 100 band maxima of both fits are in the floor columns (theta
    1.5675 to 1.5692 on every configuration), so the ratio 1.42 in that band at N22500 q512 (4.30e-7 / 3.02e-7) compares
    floors; the band rms there is 4.04e-9 / 4.05e-9.
    Rule (pair_rule.py): N_f(c6g) < N_f(c6gF) on every configuration with N >= 16875 (and on all four), N_v for r <= 1000
    not higher, N_v for r > 1000 not higher beyond the spread; the same with A5. Every part holds in every reading.
    CONFIRMED.

(b) Fit band (reported, does not decide; 14:04:12Z). N_v on 1000 <= r <= 1000 L: c6gFFF 2.157e-7 / 2.195e-7 at N11250
    q384 / N16875 q512, c6g 2.152e-7 / 2.183e-7 (ratio 0.998 / 0.995).

(c) 857-label J (N16875 q384): c6gF 1.481e-6 / 1.709e-6 at eps 0.03 / 0.01 (family A, 737 labels: 1.432e-6 / 1.670e-6);
    c6g 1.388e-6 / 1.602e-6 (A 1.341e-6 / 1.563e-6). Ratio 0.937 / 0.937. CONFIRMED.

(d) Residual maps. N16875 q512 (c6g512 / c6gF512): whole box 6.841e-7 / 7.303e-7, both at (x 8.527, y 0.063); next to P
    with y >= 0.2 5.680e-7 / 6.091e-7; y < 0.2, x 6 to 8.1 5.562e-7 / 5.821e-7; y < 0.2, x > x* 1.830e-7 / 2.295e-7 (0.80);
    y >= 1 4.321e-7 / 4.254e-7 (c6g 1.6 percent higher there, away from P and below both near-P values). N11250 q384:
    the same windows 0.94 to 0.95 next to P and 0.86 beyond x*; y >= 1 6.909e-7 / 6.357e-7 (the N11250 lobe of G73 (h),
    the only window where c6g is clearly higher, and an artifact of that grid). The angular peak is at omega 399 on both,
    with amplitude 1 to 13 percent lower on c6g for r 7 to 8.6. CONFIRMED.

(e) Centre, c_l, zeros (extra_checks N11250 q384). Identity c_l 5.576371152 on every configuration (stored value
    5.576371155; difference 3e-9). c_l from h(P) = 1 at fixed rho 5.576371215 (+6.3e-8 from the identity; c6g +7.0e-9),
    dh/dc_l 1.0788. c 15.72911346, A 10.1527423, beta - alpha -0.13158034 (c6g -0.13158031). x* 8.6008445 (c6g 8.6000638;
    the free c_l is 1.0e-3 above the fixed value). h(P) - 1: 2.42e-7 (N11250), 4.16e-8 (N16875), -1.87e-8 (N22500), at my
    grid error (c6g 2.84e-7, 3.11e-8, -1.78e-8). W_1 on the x-axis vanishes only at x* (8.6008442); min W_2/y on the
    y-axis 5.5766 (at y 7.5e6); no open-quadrant cell where both W components change sign; min |W|/(c_l |X|) 0.0216 /
    0.0065 / 0.0025 at |X - P| 1 / 0.3 / 0.1. c_l drift over the run +2.2e-7 (5.576370935 to the stored 5.576371155), far
    below 1e-4. CONFIRMED.

(f) Axis and strip (N16875 q384). x-axis maximum of |q0| 1.322e-6 (c6g 1.288e-6). vstrip: the R spectrum in the strip
    next to the x-axis (r 7.0 to 8.3) is carried by the band 400 to 600 (1.23e-6 to 4.03e-6; c6g 1.22e-6 to 3.86e-6),
    with the ripple at k 384, half period 0.0082 in theta, as on c6g. CONFIRMED.

(g) Teammates' values. Lead scans (16:12:59Z item 2; 640 / 960 angles): whole-box N_f ratio 0.94 at the same point,
    N_v r <= 1000 0.94, 185-label J 1.154e-6 / 1.231e-6 (0.937), fit band 6.81e-8 / 6.90e-8. NUM_REPORT item 7 (32768 x
    640): c6g lower in every band except r > 1e3 (equal), by 6 percent next to P. Final objectives 1.6192702e-6 /
    1.6641961e-6 (0.973). These agree with (a) to (d). NUM_REPORT item 7 still contains the placeholders "16:3xZ" and
    "[pending at 16:1xZ]"; they must be replaced by real times or removed.

(h) Pair verdict. By the 12:02Z rule with the readings fixed in advance (14:04:12Z, G73 (g), G73 (h2)), c6g wins its pair.
    Its whole-box N_f is lower on every configuration (0.83 to 0.94 on N >= 16875), and so is its N_v for r <= 1000. Its far
    N_v is within 3e-9 (0.3 percent) of c6gF's, inside c6gF's spread, and its 857-label J is lower (0.937). By the 14:02Z
    rule the candidate is the pair winner with the lowest whole-box N_f on my configurations. That is c6g: 6.83e-7 to
    7.16e-7 on N >= 16875, against s2g's 1.44e-6 to 1.51e-6. The lead's dom_start.txt = "c6g" (16:10:57Z, read by the chain at
    16:11:14Z) agrees with this reading, so the domain pair dom90g / dom300g starts from the right end. CONFIRMED.
    Status: this is not an endpoint. G20 (b1) still needs the domain columns at the candidate's basis, at three resolutions
    (dom90g, step 33, running; dom300g, step 34). The angular row for (b3) needs fxd1g (step 35). (b4) needs the report text;
    section 4 v5 has not been posted for audit. The team may NOT finish.

(i) Lead request 4 (a): B_3 on c6g and c6gF, both forms of my estimator (code/vb3.py, run in every audit). Medians over
    the variants per configuration (N11250 q384 / N16875 q512 / q768 / N22500 q512), with the variant extremes over all
    four in brackets; wpp_ode and wpp_fd agree to 1e-4:
      c6g   ibp  0.2996 / 0.3003 / 0.3003 / 0.2998 [0.2985, 0.3023];  orig 0.3029 / 0.3017 / 0.3017 / 0.2995 [0.2906, 0.3110]
      c6gF  ibp  0.2991 / 0.3007 / 0.3007 / 0.2999 [0.2978, 0.3029];  orig 0.3024 / 0.3011 / 0.3011 / 0.2982 [0.2868, 0.3122]
    (s2g: ibp 0.2992 to 0.2994, orig 0.3002 to 0.3021.) My two forms agree with each other to 3.3e-3 on every
    configuration. They also agree with the lead's original form: median 0.3027 on c6g (range 0.3010 to 0.3040), 0.3030
    on c6gF (0.3014 to 0.3044).
    The lead's "integrated form" values (work/c6/c6g_b3.txt, c6gF_b3.txt; on c6g median 0.3077, range 0.3033 to 0.3127)
    come from the ibp end piece of b3_ibp.py. G43 showed that this end piece does not converge in the Gauss-Jacobi order,
    and work/c6/b3_ibp.py is unchanged since 2026-10-17T22:56Z. On c6g its value moves from n 40 to n 80 by +0.0075 to
    +0.0085 in each of the 8 window variants (0.3033 to 0.3042 at n 40, 0.3112 to 0.3127 at n 80); on c6gF it moves by
    +0.0064 to +0.0073. Over the same step the original form moves by 1.0e-4 to 1.4e-4. The integrated-form median is a
    median over two orders of a sum that does not converge, so by G43 its values must not enter a quoted B_3 or a
    cross-fit range. This affects two places in section 4 v5, which should drop them or use the converged forms instead:
    (ii) "0.303 to 0.313 by the integrated form", and the remark's "integrated form median 0.3077, range 0.3033 to 0.3127;
    control ... 0.3068". Suggested wording: "B_3 = 0.299 to 0.303 on the candidate (medians over configurations of both
    forms of the verifier's estimator and of the lead's original form; variant extremes 0.291 to 0.311), 0.298 to 0.303
    on its control". On E10 ("0.294 to 0.307 over the two estimators and all earlier fits"): that range is a range of
    medians. It is the lead's "0.297 to 0.307" extended down to my original-form value on c6f segment 1 (0.2936, G67 (d)).
    The m <= 200 pair lies inside it (medians 0.2982 to 0.3030). The lead's integrated-form values 0.3095 on X2 and
    0.3127 on X3 are variants of the unconverged end piece and do not belong in it.

(j) Lead request 4 (b): fxm1o2i250's whole-box N_f maximum at N16875 q512 (6.533e-7) is at r 8.516, theta 0.0221 (x
    8.514, y 0.188, |X - P| 0.21): it is next to P. The comparison with the candidate, next to P, is:
      - N16875 q512: 6.533e-7 against c6g 6.841e-7 (0.955);
      - N16875 q768: 6.703e-7 against 7.156e-7 (0.937); fxm1o2i250's whole-box value there is the floor column, 1.223e-6 at
        r 9.38, theta 1.5692, in a log written before the A5 rows;
      - N22500 q512: 6.833e-7 against 6.832e-7 (1.000);
      - N11250 q384: 6.664e-7 against 6.505e-7 (1.024).
    So "about 5 percent lower than the candidate's at one configuration" needs a correction. It is 4 to 6 percent lower at
    both N16875 configurations, equal at N22500 q512 and 2 percent higher at N11250 q384, every time next to P. Elsewhere
    fxm1o2i250 is the higher of the two: N_v for r <= 1000 is 5.2e-7 to 5.7e-7 (2 <= r <= 10), against c6g's 1.9e-7 to
    2.0e-7 (2.7 to 2.8 times); far N_v is 1.13e-6 to 1.17e-6, against 1.09e-6 to 1.11e-6; 857-label J is 2.74e-6, against
    1.39e-6. Suggested wording: "X1's maximum next to P is 4 to 6 percent below the candidate's at N16875 (q512, q768) and
    equal to it at N22500 q512; its N_v for r <= 1000 is 2.8 times and its 857-label J twice the candidate's".

(k) Lead request 4 (c): |q0| on [8, x*) on c6g.
    Method. Two codes on the same fields. code/vq0prof.py at N33750 q384 (radial node spacing 0.0059 next to P, as in
    G72 (c)). code/vq0est.py (new, run 16:36Z on c6g and fxm1o2i250 at N33750 q384) computes q = R/rho at the half-shifted
    angles h/2, 3h/2 and 5h/2 (h = 2 pi / 1920), the two-point and three-point Richardson values, and the spectral value
    sum_k k R_k / sum_m m F_m with its partial sums over k <= K.
    Result.
      - The Richardson sequence converges to the spectral value. Over [7.5, 8.597] the largest |estimate - spectral| for
        q(h/2), the two-point and the three-point value is 2.34e-7, 6.19e-8 and 1.78e-8 on c6g (1.28e-7, 1.89e-8 and
        3.18e-9 on fxm1o2i250). The spectral value is therefore the axis value of the discrete field. The two-point
        Richardson of G71 / G72 (c) is low by up to 6.2e-8 on c6g and 1.9e-8 on fxm1o2i250. G72 (c)'s values 1.30e-6 /
        9.5e-7 stand to 2 percent (spectral 1.321e-6 / 9.46e-7).
      - The axis value is carried by k <= 600 on c6g and by k <= 400 on fxm1o2i250. On c6g the partial sum to K = 400
        differs from the full sum by up to 1.0e-5, the sum to K = 600 by 3e-10. So q0 is the axis value of the ripple at
        the cap frequency 2 m_max (G70, G73 (f)), a difference of band parts up to 9e-6. The smooth part of q(theta) next
        to the axis (vstrip fit over theta < 0.02) is 4.1e-8 to 5.8e-8 on c6g.
      - On c6g (spectral) q0 is negative on [7.5, x*), with no sign change. Values:
          - -1.176e-6 at 7.50 and -1.036e-6 at 8.00;
          - between -1.03e-6 and -1.07e-6 on [8, 8.52];
          - -1.066e-6 at 8.358, the maximum of |q0| on [8, x* - 0.003];
          - -1.053e-6 at 8.479, the maximum on [8.4, x* - 0.003];
          - -9.5e-7 at 8.560 and -7.1e-7 at 8.590.
        The three-point Richardson values at 8.358 and 8.479 are -1.049e-6 and -1.036e-6.
      - On fxm1o2i250 (spectral): 1.321e-6 at 8.353 on [8, x*), 9.46e-7 at 8.485 on [8.4, x*), three sign changes in
        (8.166, 8.20).
      - The q0 band split of the G73 run (vq0band, N16875 q384) agrees: -9.80e-7 at 8.0 and -9.86e-7 at 8.4 in the
        two-point form, spectral minus Richardson at most 6.2e-8, and the x-axis maximum 1.288e-6 at x 6.64. Its bands k 200
        to 360 and k 360 to 440 give +5.8e-6 and -6.9e-6 at 8.40.
    Verdict (k). On c6g, |q0| on [8, x*) is at most 1.07e-6 (1.066e-6 at x 8.36), and on [8.4, x*) at most 1.05e-6. It is
    not below 1e-6 on [8.4, x*), so the fxm1o2i250 sentence of G72 (c) does not carry over to the candidate. Wording for
    4.4b on the candidate: "|q0| is 1.03e-6 to 1.07e-6 on [8, 8.52], with its maximum on [8, x*) 1.07e-6 at x 8.36, and
    decreases over the last 0.05 before x*. It is the axis value of the residual ripple at the angular cap frequency. The
    smooth part next to the axis is about 5e-8." CONFIRMED.
    Correction 2026-10-18T16:52:02Z (found while reading the lead's v5 draft against runs/audit/c6g_N33750_q384_R7.652e6_qe.json):
    the range "between -1.03e-6 and -1.07e-6 on [8, 8.52]" above and the same range in the suggested wording are wrong.
    On the 93 nodes of [8, 8.52] the spectral |q0| is 9.87e-7 to 1.066e-6. It is 1.023e-6 to 1.066e-6 on [8, 8.49], dips to
    9.93e-7 / 9.87e-7 at x 8.496 / 8.502 and is 1.005e-6 to 1.045e-6 at 8.508 to 8.525. Beyond 8.53 it decreases with
    the ripple: 9.5e-7 to 9.9e-7 at 8.531 to 8.560, 7.9e-7 to 8.6e-7 at 8.566 to 8.584, 7.1e-7 at 8.590 and 3.6e-7 at
    8.595, the last node before x* (8.6001). The maxima (1.066e-6 at 8.358 on [8, x*), 1.053e-6 at 8.479 on [8.4, x*)),
    the sign (negative on [7.5, x*)) and the verdict sentence stand. Corrected wording for 4.4b: "|q0| is 0.99e-6 to
    1.07e-6 on [8, 8.53] (1.02e-6 to 1.07e-6 on [8, 8.49]), with its maximum on [8, x*) 1.07e-6 at x 8.36; beyond 8.53
    it decreases, with the ripple, to 9.5e-7 at 8.56, 7.1e-7 at 8.59 and 3.6e-7 at 8.595. It is the axis value of the
    residual ripple at the angular cap frequency. The smooth part next to the axis is about 5e-8."

Verdict G74: the measurements are CONFIRMED. On my evaluator, c6g wins its pair against c6gF by every part of the 12:02Z
rule, in every fixed reading (far band all r > 1000 without A5; whole-box N_f on N >= 16875; also with A5 and on all four
configurations). By the 14:02Z rule c6g is the candidate. The domain pair runs from c6g, as dom_start.txt says. B_3 on the
candidate is 0.299 to 0.303 by the converged forms; the lead's integrated-form values are the unconverged end piece of G43
and must not be quoted. fxm1o2i250's whole-box N_f maximum is next to P. On c6g |q0| on [8, x*) is at most 1.07e-6 and not
below 1e-6 on [8.4, x*). This is not an endpoint: the domain columns (G20 (b1)), fxd1g (b3) and the report text (b4) are
outstanding. The team may NOT finish.

### G75. Pre-audit of section 4 v5 (lead/notes/final_sec4_v5_text.md, mtime 16:48:02Z, with the G74 values filled); where the 857-label extremes sit on X3 and F3. Recorded 2026-10-18T16:55:17Z
The lead has not yet posted v5 for audit (NOTES_FOR_TEAM 16:46:59Z item 2: target 17:35Z). This entry checks the
values the lead filled from G74 now, so that the formal audit only has to read the changes. The [A] and [D] markers and
the "[rest unchanged]" placeholders are not read here.
Method. Every filled value compared with G74 and with my outputs (runs/audit/c6g*, c6gF*). The L2 objective ratio
recomputed from the check lines of numerics/leadcode/gpu/c6g/c6g.log and c6gF/c6gF.log (83 common check points). New:
code/vchar_traj.py (G69 (e); same evaluation, splines and integrator as vchar_dense) on fresh N16875 q384 exports of
c6g and c6gF (scratch/traj_c6g.sh, run 16:51:27Z to 16:53:49Z, exports deleted after), for four labels from |X| = 20:
the family-A maximum theta0 1.5195980, the family-A runner-up 1.4821601, the family-B minimum 1.5554509 and the
separatrix label 1.5706. Regions as in G69 (e): y-axis strip (x < 0.5, y > 0.5), origin disk (r < 0.5), x-axis strip
(y < 0.5, x >= 0.5, |X - P| >= 0.5), the disk |X - P| < 0.5, the rest. eps_P 0.03.

(a) Values that agree with G74. 4.1 X3 / F3 paragraph: whole-box N_f ratios 0.937 / 0.935 / 0.938 with the floor columns
    excluded and 0.83 without at 16875 x 768, the F3 maximum in the floor column at r 9.5, next to P 0.935 to 0.938; 857-label
    J 0.937 at eps 0.03 and 0.01; far field within 3e-9 (1.000 to 1.003, the candidate the higher), inside F3's spread
    2.4e-8. Table rows X3 and F3 (whole-box N_f 6.83e-7 to 7.16e-7 and 7.28e-7 to 7.65e-7, N_v r <= 1000 1.91e-7 to 2.01e-7
    and 1.95e-7 to 2.14e-7, far N_v 1.09e-6 to 1.11e-6, J 1.39e-6 / 1.48e-6). Free-branch record F3: J 1.481e-6 / 1.709e-6
    and next to P 6.95e-7 to 7.65e-7 (the four configurations; at N11250 q384 the F3 maximum is next to P). 4.4a: |h(P) - 1|
    2.8e-7 / 3.1e-8 / 1.8e-8 on X3 and 2.4e-7 / 4.2e-8 / 1.9e-8 on F3 (absolute values; the N22500 values are negative).
    h(P) solved for c_l: +7.0e-9 on X3 and +6.3e-8 on F3, identity value 5.576371152. 4.4b family spreads on X3: A
    1.341e-6 / 1.563e-6, B 2.511e-7 / 2.547e-7, C 7.231e-7 / 8.455e-7. B_3 (ii) and the remark: as G74 (i). The X1 sentence
    (4.1, 4.3 and 4.8): as G74 (j), with 6.703e-7 against 7.156e-7 at 768 angles. CONFIRMED.

(b) L2 objective ratio c6g / c6gF on the fit grid at equal iteration counts: 0.9599 at the first check point (250
    iterations) and 0.9720 to 0.9730 from 11750 iterations to the end; range 0.9599 to 0.9730 over the 83 common check
    points; final 1.6192702e-6 / 1.6641961e-6. "A ratio between 0.960 and 0.973 at every check point" holds. CONFIRMED.

(c) N_v for r <= 1000, "ratio 0.935 to 0.987": this holds with the floor columns excluded at 16875 x 768 (A5). Without A5
    the q768 values are 2.485e-7 / 3.012e-7 (0.825). The rule reads hold either way, since every ratio is below 1. The
    ratio range and the table note should say that the 16875 x 768 N_v values of X3 and F3 also exclude the floor
    columns, as the note already says for N_f. Wording only.

(d) I(0.03) provenance. The v5 text quotes on X3 the lead's I(0.03) -3.40e-7 (marked lead), on X2 -6.36e-7 / -7.85e-7,
    which are my values (lead -6.24e-7), and on F3 "-3.61e-7 ... (independent evaluator ...)". -3.61e-7 is the lead's
    value (work/c6/c6gF_ax.txt, -3.6078e-7). Mine (vaxis, N16875 q384) are:
      - X3: I(0.03) -3.300e-7, I(0.01) -4.131e-7;
      - F3: I(0.03) -3.507e-7, I(0.01) -4.365e-7.
    The two evaluators differ by 3 percent. The F3 sentence and the I(0.03) column of the free-branch record (headed
    "verifier between-node numbers") should use one source and say which, for example "On F3: I(0.03) = -3.51e-7
    (independent evaluator; lead -3.61e-7), max |q0| 1.32e-6 (independent evaluator; lead 1.37e-6 at x 6.66)".
    Correction needed.

(e) Where the 857-label extremes sit (v5 keeps the v4 sentences under "[V: confirm on X3]"). The v4 sentence is my wording
    of G70 (d) for the candidate of that time (fixc_c6f_m1.0e-03, whose maximum was the family-B label 1.5706 with J
    2.062e-6 against I(0.03) 2.039e-6). It puts the 857-label maximum at a label next to the y-axis that follows the
    separatrix, with J close to I(eps). On my evaluator this holds neither on X3 and F3 nor on X2: on s2g (runs/audit/s2g_N16875_q384_R7.652e6_jd2.json) the maximum is at
    the family-A label theta0 1.5134 (r_min 2.27, 1.914e-6) and the minimum at the family-B label 1.5525 (r_min 1.05,
    -1.230e-6), with the separatrix labels at -5.85e-7. On X3 and F3 (vchar_dense and vchar_traj, eps 0.03):
      - Maximum, family A theta0 1.5196 (r_min 2.10, the same label on F3): J 8.17e-7 (F3 8.83e-7). Of this, 7.53e-7
        comes from the disk |X - P| < 0.5 and 6.7e-8 from the x-axis strip; nothing comes from the y-axis strip or the
        origin.
      - Runner-up, A theta0 1.4822: 7.62e-7, of which 8.07e-7 from the disk and -4.5e-8 from the strip.
      - Minimum, family B theta0 1.5555 (r_min 0.93, the same label on F3): J -5.71e-7 (F3 -5.98e-7). The x-axis strip
        gives -2.83e-7, the disk -2.68e-7 and the y-axis strip -2.0e-8.
      - Separatrix label theta0 1.5706 (r_min 0.031): J -3.21e-7 (F3 -3.43e-7). The disk gives -2.78e-7, the x-axis strip
        -7.6e-8 and the y-axis strip +3.0e-8. This is within 3 percent of my I(0.03) (-3.30e-7). The B labels next to the
        y-axis all have J -3.21e-7, inside the range and not at an extreme.
    Suggested wording: "On the candidate and on its control the 857-label maximum is at the family-A label theta0 1.520
    (r_min 2.1), whose J (8.2e-7 at eps 0.03) comes almost all from the disk |X - P| < 0.5. The minimum is at the
    family-B label theta0 1.555 (r_min 0.93), with J -5.7e-7 from the x-axis strip and that disk in about equal parts.
    The labels next to the y-axis, which follow the separatrix, have J -3.2e-7, close to the axis integral I(0.03), and
    are not extremes." The last v4 sentence, on the oscillation at the cap frequency along every label, was not rechecked
    on X3. G70 (b) checked it on the fits of that time, and G73 (f) / G74 (f) show the cap ripple in the strip on X3 and
    F3.
    Correction needed.

(f) q0 on [8, x*). v5 quotes the wording of G74 (k), and the range in that wording is wrong (my error; correction
    2026-10-18T16:55:17Z under G74 (k)). On [8, 8.52], |q0| is 9.87e-7 to 1.066e-6, not 1.03e-6 to 1.07e-6. The corrected wording is
    given there. The other new q0 values in v5 agree with runs/audit/c6g_N33750_q384_R7.652e6_qe.json: -9.5e-7 at 8.56,
    -7.1e-7 at 8.59; negative on [7.5, x*) with no sign change; the partial sum to k 600 within 3e-10 of the full sum,
    against 1.0e-5 at k 400; the Richardson sequence within 1.8e-8 of the spectral value. On F3, max |q0| 1.32e-6 is mine
    (1.322e-6). Correction needed (the range).

Verdict G75 (pre-audit): the filled [P] values, the objective ratio, the B_3, X1 and h(P) sentences are CONFIRMED. Three
corrections are needed before the formal audit: the q0 range ((f), my error in G74 (k)), the I(0.03) provenance ((d)),
and the J-extreme sentence on X3 ((e)). Item (c) is a wording point. v5 still has [A], [D] and placeholder markers, so
G20 (b4) is OPEN. The team may NOT finish.

## G76. Formal audit of section 4 v5 full text against G67 to G75; [V] items (a) to (g) of lead NOTES 16:52:51Z item 2; cap-ripple sentence of NOTES 16:57:14Z

Date: 2026-10-18T17:22:16Z. Text audited: lead/notes/final_sec4_v5_full.md, md5 d5738bdd4b75eca8fbbcf7a0df7a5a7a, 426 lines,
mtime 2026-10-18T16:57:00Z (snapshot scratch/final_sec4_v5_full_1657.md, same md5 at the time of writing). Line numbers
below (L...) refer to that snapshot.

Method. Every number, configuration and attribution in the text was compared with my own audit files (code/vaudit.py,
my evaluator; no code of the numerics lane is used) and with the G entries the text cites. New runs for this entry:
band rows with the A5 cut (env VAUDIT_BANDA5, runs/audit/c6gBA5_N16875_q512_R7.652e6.json, done 17:04:22Z); the D10
tail on c6g and c6gF (code/d10tail.py, runs/audit/{c6g,c6gF}_N11250_q384_R7.652e6_d10.json); D14 windows on c6g, c6gF
and s2g (runs/audit/{c6g,c6gF,s2g}_extra.log); 857-label J (jd2) and axis files on c6g, c6gF and s2g at N16875 q384; a
file-level read of the numerics lane's X1 ray file numerics/runs/ray/cand_fixc_c6f_m1e-3_BP.json (read only). Fit
names: F0 c6fS1, X1 fxm1o2i250, F1 c6fs2i750, F1r fxfr1, W1 s2w1, X2 s2g, F2 seg3g, X3 c6g, F3 c6gF.

(a) Band rows on X3 (c6g), lead item 2 (a). N_f maxima at N16875 q512, raw / with A5 (pi/2 - theta >= 0.006):
  r <= 0.1:      4.45e-8 (floor column, r 0.057, theta 1.568) / 4.95e-9 (r 0.0069, theta 1.563).
                 Raw on N11250 q384 / N16875 q768 / N22500 q512: 1.45e-8 / 1.15e-7 / 7.30e-8, all in the floor column.
  0.1 <= r <= 2: 4.79e-8 (floor column, r 0.34) / 2.48e-8 (r 2.0, theta 0.0025). Raw N11250 q384 2.20e-8 at r 2;
                 raw N16875 q768 1.05e-7 and N22500 q512 6.26e-8 in the floor column.
  2 <= r <= 10:  6.84e-7 at r 8.528, theta 0.0074 (next to P), unchanged by A5.
  10 <= r <= 100: 2.64e-7 (floor column, r 10.3) / 8.66e-8 (r 10.04, theta 1.563). Raw 1.37e-7 / 5.11e-7 / 4.30e-7 on
                 the other three configurations, every one in the floor column at r 10.0 to 10.3.
  100 <= r <= 1000: 1.56e-8 at theta 1.554, unchanged by A5; 1.50e-8 / 1.60e-8 / 1.56e-8 on the other three.
  r > 1000:      1.320e-7 at r 3.3e4, theta 0.844, unchanged by A5; 1.3196e-7 / 1.320e-7 / 1.3233e-7 / 1.3203e-7 on the
                 four configurations N11250 q384, N16875 q512, N16875 q768, N22500 q512.
  N_v with A5 at N16875 q512 for r <= 0.1, 0.1 to 2, 10 to 100, 100 to 1000: 1.07e-8, 4.83e-8, 7.10e-8, 6.49e-8; far
  (r > 1000) 1.074e-6 with A5, 1.101e-6 raw.
  [Withdrawn 17:42:13Z, see the G76 addendum.] Verdict: the lead's r <= 0.1 value 2.3e-11 is REFUTED as a residual: its only source is the inverse-impact value of
  NUM_REPORT lines 549 / 568, which is a different quantity. On my evaluator the band maximum is 4.95e-9 with A5 and
  1.45e-8 to 1.15e-7 raw. The lead's 0.1 to 2 value 2.9e-8 is CONFIRMED in size (2.48e-8 with A5, 2.20e-8 raw at
  N11250). The A5 maxima at theta 1.563 lie on the first column outside the cut and may still contain part of the
  floor; they are upper bounds for the A5 band, not floor-free values.

(b) D14 on X3, F3 and X2 (lead item 2 (b)), relative E and D2 on my evaluator, windows in r:
  window          c6g (E, D2)            c6gF (E, D2)           s2g (E, D2)
  [1e-3, 0.02]    -1.30e-9, +5.11e-9     -7.37e-10, +5.35e-9    -6.55e-9, +8.33e-9
  [1e-3, 0.05]    -1.94e-9, +4.88e-9     -1.44e-9, +5.13e-9     -8.37e-9, +7.43e-9
  [2e-3, 0.05]    -1.99e-9, +4.88e-9     -1.48e-9, +5.10e-9     -8.49e-9, +7.38e-9
  [1e-3, 0.1]     -5.18e-9, +3.70e-9     -4.79e-9, +3.91e-9     -1.72e-8, +3.33e-9
  [5e-3, 0.1]     -5.91e-9, +3.40e-9     -5.56e-9, +3.61e-9     -1.92e-8, +2.32e-9
  The lead's values (c6g -2.29e-9, 5.83e-9 / -5.2e-10, 2.49e-9; X2 -4.8e-9, 8.0e-9 / -3.1e-9, 4.2e-9) are window
  dependent in the same way. CONFIRMED in size: |E|, |D2| <= 6e-9 on X3 and F3 for every window up to r 0.1, and
  <= 8.5e-9 on X2 for windows up to r 0.05 (X2 reaches 1.9e-8 on [5e-3, 0.1]). Suggested text: quote a bound over the
  windows ("at most 6e-9 on X3 and F3 for windows inside r <= 0.1") rather than one window's pair.

(c) F0 J (lead item 2 (c)). From G70 (d): 857-label J on F0 is 3.85e-6 at eps 0.03 and 4.14e-6 at eps 0.01. F0's
  values over the six configurations: N_v on r <= 1000 6.359, 6.464, 6.774, 6.825, 6.514, 6.797 e-7; whole-box N_f
  2.276e-6 to 2.442e-6; far N_v 1.118e-6 to 1.146e-6. CONFIRMED as above; the text does not state F0's configurations.

(d) sup minus inf on X3 (lead item 2 (d)), from runs/audit/{c6g,c6gF}_N16875_q384_R7.652e6_jd2.json.
  Family B, J at eps 0.03 against distance from the y-axis (c6g): flat at -3.208e-7 to -3.24e-7 from 1e-4 to about
  1.1e-3, then decreasing monotonically (-3.42e-7 at 2.6e-3, -4.19e-7 at 6.3e-3, -5.02e-7 at 9.9e-3) to the minimum
  -5.715e-7 at 0.01535 (rmin 0.93), then -5.539e-7 at 0.0183. Family C next to the x-axis: about -1.06e-8 at eps 0.03.
  Both axis limits exist to 1e-9 in the sense that J is constant to 1e-9 over the innermost labels.
  Subset check: the 369-label subset of family A gives a spread 0.55 percent lower than the 857-label spread (c6gF 0.88
  percent) at eps 0.03 and 0.48 / 0.76 percent lower at eps 0.01, that is 7.4e-9 (c6gF 1.25e-8).
  Peak check: a parabola through the maximum and its neighbours (7.988, 8.167, 8.093 e-7) peaks 5e-10 above the sampled
  maximum.
  857-label spread at eps 0.03 / 0.01: c6g 1.3882e-6 / 1.6019e-6; c6gF 1.4808e-6 / 1.7093e-6. The family-A minimum
  is -5.239e-7 at the A end (theta0 1.5508); the family-C maximum is 7.03e-7 at theta0 0.0183.
  CONFIRMED: on the 857 labels the spread equals sup minus inf over labels to about 1e-8. Qualifier: N16875 q384 only;
  the N22500 label window was not repeated on X3.

(e) D10 tail (lead item 2 (e)). c6g, 2k - 2 = -1.6412789: decade slopes of the Q3 integrand per d log r are -1.94644
  (10 to 100), -1.75026, -1.65907, -1.64400, -1.64169 (1e5 to 1e6), and -1.64135 from 1e6 to R; the last decade gives
  -1.6413591 (deviation -8.01e-5). The decade deviations -0.305, -0.109, -0.0178, -0.00272, -0.000413 fall by ratios
  6.1, 6.54, 6.59 against 10^(1-k) = 6.62, so the correction is the relative r^(k-1) term of D10; deviation divided by
  r_mid^(k-1) is 13.3 to 13.9 with no sign change. c6gF is the same to 2e-4 (2k - 2 = -1.6413438, last decade
  -1.6414239). D10 relative defect 1.355e-9 on both. CONFIRMED.

(f) H''' step on X3 (lead item 2 (f)), E1 estimator across the characteristic leaving P, three configurations:
  +0.120 / +0.112 / +0.120 at P; +0.012 / +0.012 / -0.008 at y 0.5; -0.429 / -0.399 / -0.354 at y 1 (joint fit
  -0.397 / -0.376). F3 and X1 agree with X3 to 0.004. On c6g at y 1 the pjump_off scan puts the feature at xi -0.01 to
  -0.02, that is on the characteristic to the grid resolution. CONFIRMED with the qualifier that this is one
  estimator; G66 (c) gave 0.05 to 0.16 at P by the other estimators.

(g) Re-differentiation and the X1 ray check (lead item 2 (g)).
  Re-differentiation on X3: on 1 <= r <= 10 the difference is 1.49e-6 / 3.93e-7 / 1.06e-7 at N 11250 / 16875 / 22500;
  on r >= 10 at most 2.1e-9; on 0.01 <= r <= 1 1.3e-8 to 5.2e-8; on r <= 0.01 up to 3.15e-4. X3 equals X1 here to 8
  percent. Suggested text: quote X3 directly. The closure row on X1 suffices for X3 (same R_shape, closure and c_l; the
  reported residuals are the canonical ones).
  X1 52-point ray check (NUM_REPORT (xii)), audited at file level on cand_fixc_c6f_m1e-3_BP.json (baseP rules, 52
  rows): |X-P| < 0.5, 20 rows, max |dU| 8.36e-10, max impact 6.27e-10; 0.5 to 2.5 from P, 12 rows, max |dU| 3.98e-8,
  max impact 2.83e-9; max |dU| at r 0.1, 1, 20, 100, 300: 6.2e-12, 4.9e-11, 1.04e-9, 4.56e-9, 1.36e-8. Overall maximum
  impact 2.83e-9 at (8.550, 1.994), median 2.84e-11. The numbers at text lines 356 to 360 are CONFIRMED. Two
  corrections: (1) L362 "confirmed by the verifier's modal inverse at three points" is misattributed; the three-point
  CPU modal inverse is the external referee's (astra raycheck, NUM_REPORT lines 562 to 566 and 650); my audits G64 (d),
  G65 (c) and the 08:02:22Z addendum compared files. (2) The 2.8e-9 is attained 0.5 to 2.5 from P but is set against
  the near-P residual maxima; within 0.5 of P the impact is 6.3e-10.

(h) Corrections to the text (snapshot line numbers).
   1. L160, rule (1): the 12:02Z pair rule applies the spread to N_v only, not to J.
   2. L162 to 164: "before any X2/F2 result existed" and "before any X3/F3 measurement" should read "before any
      residual scan"; the objectives (s2g at 2000 iterations 4.993e-6; c6g at iterations 250 to 1000) were known.
   3. L66 and L421, "margins about 6 percent": measured X3 / F3 ratios are N_f 0.935 to 0.938, J 0.937, N_v on
      r <= 1000 0.936 to 0.987, L2 0.960 to 0.973, far N_v 1.000 to 1.003 (candidate higher). The far band has no margin.
   4. L68 to 69, "every band ... factor about 2": the fit band ratio is 0.86 (2.152e-7 against 2.513e-7); the y >= 1
      window is 1.01 / 0.81.
   5. L71 to 72, "0.62 to 0.69 in J": these are 185-label J values (G73 (d)); state the label set.
   6. L203, "every window near P falls by 2.1 to 2.5": false for y >= 1 (1.01 at N11250 q384, 1.23 at N16875 q512).
   7. L51: needs the A5 qualifier (raw 2.485e-7 at q768).
   8. L176, F1 row: at the stated configurations whole-box N_f is 2.09e-6 and 2.22e-6 and N_v on r <= 1000 is 5.90e-7
      and 6.27e-7 (six configurations 5.90e-7 to 6.57e-7; "6.4e-7 to 6.5e-7" matches no configuration); far 1.459e-6,
      1.472e-6 CONFIRMED. X1 far at the stated configurations 1.13e-6, 1.15e-6 (six configurations 1.13 to 1.17e-6).
      F1r rows CONFIRMED.
   9. The configuration note omits that J is computed at N16875 q384.
  10. L242 and L352, "2.15e-7": that is the N11250 value; N16875 gives 2.183e-7.
  11. L243, "r 3.4e4 to 3.7e4": the far N_v argmax on X3 is at r 3.61e4 to 3.72e4 over the four configurations.
  12. L201, "no continuation gives systematic improvement": contradicts F1 to F2 (whole-box N_f 2.1e-6 to 2.3e-6
      down to 1.6e-6).
  13. L190 against L215: 1000 against 1500 iterations for the 244 fit at c_l 5.60. L216 "1.3 to 1.4 times": my G68
      (c), at the 1000-iteration state, gives 2.0 near P, 1.42 / 1.32 whole box, 1.43 on 10 to 100, 2.07 in J.
  14. L198, "r 4 to 7": r 4 to 7.6 (G72).
  15. L208 to 209, "do not drift toward each other": F1r moved by +2.5e-6 toward the other branch; F2 moved +6.9e-6,
      F3 +2.2e-7.
  16. L267, "8.6e-6 (100 labels)": a numerics-lane value (NUM_REPORT line 681), by NUM_REPORT lines 684 to 686 mostly
      drift of the unfitted exterior formula; not mine. The 6.8e-7 (111 labels) and 2.2e-8 / 2.7e-8 (333 labels)
      values are mine.
  17. L332, "largest contributions from the x-axis between origin and P": on X3 the P disk dominates (7.53e-7 of
      8.17e-7 at the maximum label; for the separatrix label -2.78e-7 of -3.21e-7 comes from the disk). As written it
      contradicts L325 to 327.
  18. L327 to 329 (my G75 (e) wording): "labels within 1e-3 of the y-axis", see (d).
  19. L344, "factor 2.4": that is the ratio of whole-segment maxima (3.13e-6 / 1.29e-6). On [0, 5] the X3 q0 is
      1.163e-6 at x 3 and 1.059e-6 at x 2, against s2g 3.127e-6 at x 2.80: a factor about 2.7.
  20. L354, "every fit reads 1.06e-6 to 1.15e-6" (also L420 to 421): without A5, F0, X1, F1r, X2, F2, X3, F3 and the
      reorthogonalized fit read 1.08e-6 to 1.17e-6, but F1 reads 1.459e-6 to 1.473e-6 and W1 1.28e-6 to 1.31e-6.
  21. L353, "(pi/2 - theta)^2 growth": measured on X2. On X3 (G73 (h3)) the axis floor is at most 8.9e-9 and the far
      column profile is 1.111, 1.096, 1.082, 1.077, 1.073, 1.073 e-6, flat to 4 percent.
  22. L362: misattribution, see (g).
  23. L95, B_3 "0.294 to 0.307": over the 136 audit files with c_l in [5.5752, 5.6001] my integration-by-parts
      medians are 0.2957 (c5d200) to 0.3020 (fxb560fixed); the original-form medians are 0.2767 (c5d200) to 0.3113
      (fxb560fixed), the low ones c4cen 0.2803, c5d900 / c5d300 0.2805, d100c13 0.2848, c6fS1 N22500 0.2878. Every
      variant is positive (minimum 0.151, c5d200). The fxs1-1.0e-02 transplant (0.2928) lies outside that c_l range.
      Suggested text: "0.296 to 0.302 by the converged form over 136 audits; every variant positive".
  24. L383, "zero of h(P) - 1 by about 0.1": G52 gives at least 0.16 for 256x64 against 256x128; "0.1 to more than
      0.16".
  25. L374, "verifier's normalization": name it (N_f or N_v).
  26. L416, "positive transport multiplier": the referee's claim, not re-derived by me (G68 S6); attribute it.
  27. L82 to 86, regularity: the argument is structural and applies to X3. On X3 the T coefficients are (-1.12e-8,
      -2.768, 4.114, 6.517, -0.453, 1.420) and T(-1) is about -1.51, nonzero. CONFIRMED.
  28. L204, "full list": the table omits the equal-budget m <= 150 iterate, the reorthogonalization and damping arms
      and the 244 fit; say "list of the fits compared" or add them.
  29. L293 to 295, "stall ... (parenthesis)": supported by G71 (a) on c6dS1 only; say so.

(i) Corrections of my own earlier entries.
  G73 (h), VR line 5368: "near P every window falls by a factor 2.1 to 2.5, except y >= 1 at N11250" should read: every
  window except y >= 1, which is 1.01 at N11250 q384 and 1.23 at N16875 q512.
  G73 (c), VR line 5305: "every fit measured here reads 1.06e-6 to 1.15e-6": 1.06e-6 was an A5 value. Without A5 the
  named fits read 1.083e-6 (reo_plain8) to 1.172e-6 (fxm1o2i250 q768); F1 and W1 are higher, see (h) 20.
  G75 (e): "the B labels next to the y-axis all have J -3.21e-7" holds only for labels within 1e-3 of the y-axis, see
  (d).
  E10 (G68, VR near line 4362) and G74 (i) (VR lines 5505 to 5506): "0.294 to 0.307 over the two estimators and all
  fits" was based on the G67 values only; the full range over 136 audits is in (h) 23.
  Logging: the exit codes written to runs/audit/jS.log by the jA, jS, jV and traj_c6g scripts are the status of date,
  not of the job (echo "$(date -u ...) ... exit $?"). Every result I used was read from its output file, not from the
  logged code. Fixed in scratch/d10tail_c6g.sh; the running scripts were not edited.

(j) Cap-ripple sentence (L329 to 331, NOTES 16:57:14Z).
  First half (J oscillation across family A carried by frequencies at the cap): my G70 (d) wording, supported by G70
  (b) reading (1) on c6dS1 and X1 (next to the x-axis from r 4 to P, within 10 percent of 2 m_max). G71 (a): on c6dS1
  and X1 the family-A oscillation is carried by frequencies >= cap, but on F1 by no band, so as a statement about all
  fits it is REFUTED.
  Second half (the ripple on X3 is smaller): supported by G73 (f) / G74 (f) for the strip r 7.0 to 8.3, band 400 to 600
  (X3 1.22e-6 to 3.86e-6, F3 1.23e-6 to 4.03e-6), 3.4 times lower than X2 at r 8.3. R/rho along labels on X3 was not
  measured.
  Suggested wording: "On c6dS1 and X1 the oscillation of J across family A is carried by angular frequencies at and above
  the cap (G70, G71); on F1 it is not. On X3 and F3 the band 400 to 600 in the strip r 7.0 to 8.3 is about 3.4 times
  smaller than on X2 (G73, G74)." CONFIRMED with this wording.

Verdict G76. Items (a) to (g): (a) CONFIRMED for 0.1 to 2, REFUTED for the r <= 0.1 value 2.3e-11 [withdrawn in the G76 addendum 17:42:13Z] (replace by the
values in (a)); (b), (c), (d), (e) CONFIRMED with the stated bounds and qualifiers; (f) CONFIRMED as one estimator;
(g) CONFIRMED except the attribution at L362. The 29 corrections in (h) and the cap-ripple wording in (j) are needed
before the text is ported; none changes the classification of the result (strong numerical evidence, not a proof, no
NO theorem). The text still contains [A], [D] and [TBD] rows that wait on dom90g / dom300g and the m <= 250 angular row,
so G20 (b4) stays OPEN. The team may NOT finish.

## G77. Domain column dom90g (chain step 33) on my evaluator: the A4 rule (07:23Z / 08:17Z) against X3 = c6g; lead NOTES 17:17:55Z item 3 and 17:20:44Z item 1

Date: 2026-10-18T17:35:12Z.

Method. Shape numerics/leadcode/gpu/dom90g/dom90g_shape.npz, copied by scratch/jV.sh at 17:15:11Z, md5
7f989938b5e9a6434fe4e7bd195647b4 (equal to the md5 on the chain line "step 33 done"). dom90g continues c6g for 20750
iterations at the same fixed c_l 5.5753626106, fit rows r < 90 L, inverse domain R_shape = 100 L (L = 7.65142). My
generator (code/gen_shape.py) with the lead's two-term closure at Rc = 765.142 (R_shape 100 L; "closure at Rc = 765.142,
6750 radii replaced" in every log) and my evaluator (code/vaudit.py, k_self), with the extra regions r <= Rfit and r > Rfit
for Rfit = 90 L = 688.63. Three configurations N11250 q384, N16875 q512, N22500 q384, as in G70 (a). Base: c6g in its own
(formula-global) convention at the same three configurations (c6g at N22500 q384 run for this entry, tok_run c6g_a3, done
17:32:20Z). Further rows: band rows with A5 at N16875 q512 on both (VAUDIT_BANDA5;
runs/audit/dom90g_N16875_q512_R7.652e6_BA5.json against c6gBA5_N16875_q512_R7.652e6.json); residual map near P (code/vresmap.py,
window r 6 to 12, theta <= 0.6, with the closure, scratch/run_resmap_clo.sh; scratch/cmp_resmap.py against c6g512) at
N16875 q512; 857-label J (code/vchar_dense.py, labels started at r 20, inside the fit rows) and vaxis at N16875 q384 with the
closure; the formula convention (no closure, formula continued to 7.652e6) at N11250 q384 (suffix _frm).

Result, dom90g / c6g, configurations N11250 q384, N16875 q512, N22500 q384:
  2 <= r <= 10, N_f maximum: 7.200e-7 / 6.909e-7 (1.04), 4.227e-7 / 6.841e-7 (0.62), 4.774e-7 / 6.605e-7 (0.72). At N11250
    q384 both maxima are at r 8.784, theta 0.3076, the N11250 lobe point of G73 (h) (a property of that radial grid). At
    N >= 16875 the dom90g maximum is the lobe above P (r 8.74, theta 0.193 to 0.196, y about 1.7), c6g's is next to P.
  10 <= r <= 100, N_f maximum raw: 1.400e-7 / 1.368e-7 (1.02), 3.254e-7 / 2.644e-7 (1.23), 1.631e-7 / 1.954e-7 (0.83), all in
    the floor column (theta 1.568, r 10.0 to 10.4). With A5 at N16875 q512: 7.26e-8 / 8.66e-8 (0.84).
  0.1 <= r <= 2: raw 1.57e-8 / 2.20e-8, 4.28e-8 / 4.79e-8, 3.87e-8 / 3.43e-8 (floor column except c6g at N11250); with A5 at
    N16875 q512 1.64e-8 / 2.48e-8 (0.66). r <= 0.1: raw 1.43e-8 / 1.45e-8, 5.06e-8 / 4.45e-8, 3.22e-8 / 2.87e-8; with A5
    5.44e-9 / 4.95e-9 (1.10).
  Next to P (|X - P| < 0.5), N_f: 2.124e-7 / 6.505e-7 (0.33), 2.271e-7 / 6.841e-7 (0.33), 2.141e-7 / 6.605e-7 (0.32).
  Map split at N16875 q512 (R / N_f maxima): strip y < 0.2, 6 < x < 8.1: 2.31e-7 / 5.56e-7; y < 0.2, 8.1 <= x < x*: 2.27e-7 /
    6.84e-7; y 0.2 to 1, |x - x*| < 1: 2.65e-7 / 5.68e-7; y >= 1 (the lobe, maximum at (8.57, 1.705) / (8.55, 1.68)): 4.23e-7 /
    4.32e-7 (0.98); y < 0.2, x > x*: 1.87e-7 / 1.83e-7. The cap ripple next to the x-axis is at omega 399 on both, with
    amplitude 1.46e-8 / 2.90e-8 at r 8.0, 2.17e-8 / 6.11e-8 at r 8.45, 1.19e-8 / 6.01e-8 at r 8.6.
  N_v: r <= Rfit (covers r <= 600) 2.001e-7, 1.234e-7, 1.395e-7, in each case at the 2-10 maximum; c6g on r <= 1000 with A5
    1.920e-7, 1.917e-7, 1.851e-7.
  h(P) - 1: +3.62e-7 / +2.84e-7, +5.61e-8 / +3.11e-8, +6.8e-10 / -1.78e-8.
  c_l by the identity on my inverse: 5.5753626108 at every configuration (fixed value 5.5753626106); c6g 5.5753626074.
  857-label J, eps 0.03 / 0.01: 5.531e-7 / 5.886e-7 against 1.3882e-6 / 1.6019e-6 (0.40 / 0.37). Extremes: maximum family A,
    theta0 0.0658 (2.91e-7), minimum family B, theta0 1.5555 (-2.62e-7); on c6g family A 1.5196 (8.17e-7) and family B 1.5555
    (-5.71e-7).
  Axis (vaxis): I(0.03) -1.061e-7, I(0.01) -1.372e-7 (c6g -3.300e-7, -4.131e-7); max |q0| on the segment left of P 7.96e-7 at
    x 6.15 (c6g 1.288e-6 at x 6.64).
  B_3, integration-by-parts median: 0.3001, 0.3006, 0.3002 (c6g 0.2996, 0.3003, 0.2998).
  Formula convention (N11250 q384, formula continued to 7.652e6, not fitted beyond 90 L): next to P N_f 3.11e-5, 2-10 3.12e-5,
    10-100 2.76e-5, h(P) - 1 = -5.95e-5, c_l identity 5.5753470 (-1.56e-5 from the fixed value).

Reading by A4 (2-10 and 10-100 N_f maxima within a factor 1.5 of the base, |h(P) - 1| < 1e-7). The 2-10 ratios are 1.04,
0.62, 0.72; the 10-100 ratios 1.02, 1.23, 0.83 raw and 0.84 with A5. h(P) - 1 is 5.6e-8 and 6.8e-10 on N >= 16875. At
N11250 q384 it is +3.6e-7 on dom90g and +2.8e-7 on c6g; this configuration is biased for h(P) on both fits (G70 (a) found
+2.7e-7 for dom90 segment 2 there), so the h(P) part is read on N >= 16875. Verdict: AGREE on my rows; the lead's A4
reading (work/c6/dom90g_a4.txt: 2-10 0.728 / 0.695, 10-100 0.816 / 0.822, h(P) - 1 -5.3e-9 / -2.7e-9) is CONFIRMED.
Lead's 0.1-2 value 0.666 CONFIRMED with A5 (0.662).

What the column shows and what it does not.
  (1) The interior gain sits in the strip next to the x-axis left of P (factor 2.4 to 3) and in the band y 0.2 to 1
      (factor 2.1); the lobe above P does not move (0.98) and becomes the 2-10 maximum. The lead's description (strip 6.94e-7
      to 2.31e-7, lobe 4.81e-7 to 5.05e-7) is CONFIRMED in kind; on my map the lobe ratio is 0.98 against the lead's 1.05.
  (2) J falls by 2.5 to 2.7 and the axis integral I(0.03) by 3.1.
  (3) dom90g carries both a smaller fit domain and 20750 further iterations, so it does not separate domain from budget
      (the lead says so). The start objective on its rows was 2.345e-4 (NUM_REPORT item 8): the closure at 100 L changes the
      interior velocity of the c6g shape, so dom90g solves a different closed problem from the start. dom300g (fit radius
      300 L, same budget) is the control. What can be said now: in the closed 90 L problem the m <= 200 basis at 20480 x 960
      reaches a near-P residual 3 times and a J 2.5 times below c6g's; c6g's near-P residual is therefore not a floor of
      the basis in that problem. Whether the global problem allows the same gain is not shown by this column.
  (4) The rule's "within a factor 1.5" is met because dom90g is lower, not because the two agree to the factor; the
      domain columns are a stability observation in closed problems (v5 4.4 says so) and not a truncation bound.

v5 4.4 sentence of 17:20:44Z ("For the 90 L fit from X3 the residual within 0.5 of P is 1.9e-7 in N_f with the closure at
100 L and 2.9e-5 with the formula continued to 1000 L (h(P) - 1 = -5.3e-9 and -5.6e-5)"): CONFIRMED in order of magnitude.
My values: 2.12e-7 to 2.27e-7 with the closure (three configurations) and 3.11e-5 with the formula continued to 7.652e6 (one
configuration); h(P) - 1 = +5.6e-8 and +6.8e-10 (N >= 16875) with the closure and -5.95e-5 with the formula. Suggested
text: "1.9e-7 to 2.3e-7 in N_f with the closure at 100 L (h(P) - 1 between -5e-9 and +6e-8 over the lead's and the
verifier's grids) and about 3e-5 with the formula continued beyond the fit radius (h(P) - 1 about -6e-5)". The words
"interior residual ... does not depend on the box" should not be used: the near-P residual changes by a factor 3 together
with the budget.

Also checked: NUM_REPORT.md (mtime 17:23:24Z, copy scratch/NUM_REPORT_1723.md) item 8 is consistent with the above (md5, end
17:14:27Z, objective 1.062127e-6). Its item 7 repeats two wordings corrected in G76: "beyond it every fit reads 1.06-1.15e-6"
(F1 reads 1.459e-6 to 1.473e-6 and W1 1.28e-6 to 1.31e-6 without A5; G76 (h) 20) and "0.62-0.69 x in J" (185-label J;
G76 (h) 5). Item 7 placeholders of G74 (g) were not rechecked in this entry.

Verdict G77: dom90g AGREES with c6g by the A4 rule on my rows (CONFIRMED); its near-P residual is 3 times lower and its J 2.5
times lower, with domain and budget not separated. G20 (b1) for the candidate needs dom300g (step 34, expected about
18:20Z). The team may NOT finish.

## G78. FINAL_REPORT.md diff of mtime 16:53:20Z (timeline entries 15:31 and 16:44) against G73, G74, G76

Date: 2026-10-18T17:36:19Z. File ../lead/FINAL_REPORT.md, md5 48cf7eb7541d05b23e7d2565ad048dd4, mtime 2026-10-18T16:53:20Z (copy
scratch/FINAL_REPORT_lead_1653.md). The only change against my copy of 16:16:02Z (scratch/FINAL_REPORT_lead_1616.md) is the
insertion of two timeline entries (new lines 287 to 311).

15:31 entry (G73).
  "Every band inside the fit domain fell by a factor of about 2": not true for every band. The N_v fit band (1000 <= r <=
  1000 L) is 0.86 (2.152e-7 against 2.513e-7) and the window y >= 1 above P is 1.01 at N11250 q384 and 0.81 at N16875 q512
  (G76 (h) 4 and 6). Suggested: "whole-box N_f, N_v for r <= 1000 and the 857-label J fell by a factor of about 2".
  Whole-box N_f 6.8e-7 to 7.2e-7 (0.48 times), N_v r <= 1000 1.9e-7 to 2.0e-7, 857-label J 1.39e-6 (0.44 times), far N_v
  1.09e-6 to 1.11e-6 (1 to 2 percent lower; my ratios 0.981 to 0.989): CONFIRMED.
  "0.71 to 0.72 times ... in N_f and 0.62 to 0.69 in J": the J values are on the 185-label set (G73 (d)); state the label set.
  "angular frequencies 400 to 600, about twice the new cap": the band is 400 to 600, two to three times the cap 200; the
  peak is at 399 (G73 (f), (h)). Wording point.
  Far band read on all columns, whole-box N_f on N >= 16875 "fixed at 15:54, before any row of the free control existed":
  CONFIRMED (G73 (g), (h2), entered 15:54:16Z; the first c6gF task started 16:09:27Z).
16:44 entry (G74).
  "whole-box N_f 0.94 times the free control's": on N >= 16875 the ratios are 0.937, 0.832 and 0.938 (G74); write "0.83 to
  0.94". N_v r <= 1000 lower, far N_v equal to 3e-9 inside the spread, 857-label J 0.94 (0.937), c_l of the free control
  +2.2e-7 and the 1e-3 separation, B_3 0.299 to 0.303 by the converged forms, |q0| on [8, x*) at most 1.07e-6, "standard is
  not met yet": CONFIRMED.
Verdict G78: two corrections (the "every band" sentence and 0.94 -> 0.83 to 0.94) and two wording points; the rest
CONFIRMED. G20 (b4) OPEN. The team may NOT finish.

### G76 addendum (2026-10-18T17:42:13Z): item (a), the r <= 0.1 value 2.3e-11, corrected

Lead NOTES 17:30:05Z item 2 states that the 2.3e-11 came from the lead's own between-node scan, not from NUM_REPORT. Checked:
../lead/work/c6/c6g_scanfit.json, band "r<=0.1/all": max 2.2731e-11 at r 0.09999, theta 0 (6350387 samples);
"x_strip" the same; "middle" 2.141e-11 at theta 0.0515; "y_strip" 3.06e-12 at r 0.076, theta 1.5683. My statement in G76
(a) that its only source is the NUM_REPORT inverse-impact value was wrong, and so was the verdict REFUTED.
New measurement: residual map of c6g on r <= 0.1, the full quadrant (code/vresmap.py window r 7e-4 to 0.1, theta <= pi/2,
N16875 q512 M639, 3571 radii x 641 angles; runs/audit/c6g512r01_resmap.npz, read by scratch/r01_look.py; the exact axis
column, where R and N_f both vanish, is left out). Maxima of R / N_f:
  r >= 0.001, pi/2 - theta >= 0.2: 2.43e-11 at r 0.098, theta 0.0025 (the lead's 2.27e-11 at r 0.1, theta 0);
  r >= 0.001, pi/2 - theta >= 0.05: 1.07e-10 at r 0.021, theta 1.519;
  r >= 0.001, pi/2 - theta >= 0.012: 1.71e-9; >= 0.006 (A5): 4.95e-9 at r 0.0069, theta 1.563;
  the innermost rows (r < 0.001, next to r0 = 7.652e-4): up to 5.7e-9 at pi/2 - theta >= 0.006 and 4.0e-10 at >= 0.05.
So off the columns next to the y-axis the two evaluators agree (2.43e-11 against 2.27e-11, at the same place). The larger
values on my evaluator sit within 0.2 of the y-axis and grow toward it (1.1e-10, 1.7e-9, 4.95e-9), where the lead's y-strip
reads 3.1e-12. That is the near-axis behaviour of my sine-series evaluation (G67 (c)), not a residual both evaluators see.
Corrected verdict for (a), r <= 0.1: the lead's 2.3e-11 is CONFIRMED as the band maximum away from the y-axis (pi/2 - theta >=
0.2); in the columns within 0.2 of the y-axis my evaluator gives upper bounds up to 4.95e-9 (A5) that the lead's scan does
not reproduce. Suggested row: "r <= 0.1: 2.3e-11 (lead scan; verifier 2.4e-11 for pi/2 - theta >= 0.2); within 0.2 of the
y-axis the verifier's evaluator reads up to 5e-9, the lead's scan 3e-12". The lead's plan (17:30:05Z item 2) to drop its
number and quote only mine as upper bounds is also correct but loses the agreement off the axis. The other items of G76 are
unchanged.

## G77 addendum (2026-10-18T17:48:26Z). Off-axis 10-100 band of dom90g and c6g on my evaluator against the lead's sub-band scan

Method. The maps c6g512r10 and dom90g512r10 (my evaluator, N 16875, q 512, M 639, window 10 <= r <= 100 and
0 <= theta <= pi/2, 1688 radii by 641 angles; dom90g in the closure convention with Rfit 688.63, c6g as in G77) were read
with scratch/band_look.py (maxima of |R|/N_f by bands of pi/2 - theta) and by angle windows matching the lead's sub-bands.

Result.
- Middle band (0.6 <= theta <= 1.2): c6g 8.175e-8 at r 13.94, theta 0.9228; dom90g 6.637e-8 at r 13.94, theta 0.9449;
  ratio 0.812. The lead's scan gives 7.985e-8 at r 13.94, theta 0.923 and 6.652e-8 at r 13.93, theta 0.945, ratio 0.816.
  The locations agree to the grid spacing and the values to 2.4 percent (c6g) and 0.2 percent (dom90g).
- For pi/2 - theta >= 0.012 the maximum of either map is this middle-band point. For 0.006 <= pi/2 - theta < 0.05 the
  maxima are 8.659e-8 (c6g) and 7.248e-8 (dom90g), both at r about 10.05, theta 1.5634, ratio 0.84. These are the A5
  numbers of G77 (7.26e-8 / 8.66e-8) to the digits shown.
- Inside the A5 cut (pi/2 - theta < 0.006) the maxima are 2.644e-7 (c6g, r 10.28) and 3.253e-7 (dom90g, r 10.06). These
  are the raw floor-column values of G77 (2.644e-7 / 3.254e-7). The lead's y-strip value for c6g, 8.149e-8 at theta
  1.5708, is a factor 3.2 lower. This is the same near-axis discrepancy that the G76 addendum records for r <= 0.1.
- x strip (theta < 0.1): c6g 8.99e-9, dom90g 3.70e-9; the lead's c6g x-strip value is 3.59e-9. Both are at least a
  factor 9 below the middle band and do not affect the band maximum.

Verdict. CONFIRMED: off the y-axis the lead's 10-100 sub-band maxima and the dom90g/c6g ratio (0.82) reproduce on my
evaluator. Within 0.006 of the y-axis my evaluator reads up to 3.3e-7. The A5 cut was introduced for this column (cap
ripple, G76 (j)) and the reading of G77 is unchanged. The two evaluators disagree only within 0.006 of the y-axis, as for r
<= 0.1. Rows of section 4 that quote a 10-100 value should state whether the A5 cut is applied.

## G79 (2026-10-18T17:50:01Z). Fit rows of the formula-global fits end at 900 L (lead NOTES 17:42:41Z item 3)

Method. Read lead/artifacts/b_fit_domain/centre_fit.py lines 41-42 and 183-184, and the shape file
runs/gen4/gpu/c6g_shape.npz (my md5-checked copy) with my own loader. Shape coordinates are in units of L: R_shape is 1000
for c6g and 100 for dom90g, whose fit radius 90 is the 90 L of G77.

Result.
- centre_fit.py line 41 sets fit_radius = 0.9 R when it is not given, and line 42 takes the rows 1e-4 <= r < fit_radius.
  The run configuration stored in c6g_shape.npz has "fit_radius": null, so the c6g rows are r < 900 L and its inverse domain
  is r <= 1000 L. For dom90g it is "fit_radius": 90.0 with R_shape 100.
- The four largest interior knots of the radial basis in q are 0.97328, 0.97994, 0.98662, 0.99330, which give r = 82.6,
  117.2, 191.9, 446.1 L by q = 1 - (1 + r^2)^(-(1-k)/2), k = 0.179360531. The next knot is q = 1. For r = 900, 1000, 4700 L,
  q = 0.996237, 0.996548, 0.99903, which lie at 0.438, 0.485, 0.855 of the last knot interval. These are the lead's numbers.
- Consequence for my entries. Where G-entries up to G78 call 1000 <= r <= 1000 L "inside the fit domain" (G72 table,
  lines near 5055-5059 of this file; G78 "N_v fit band"), the correct term is "inverse domain": the fit rows end at 900 L
  (r 6886). The maxima quoted there (r about 6440, i.e. 842 L) lie inside the fit rows, so no number changes. The lead's
  2.15e-7 at r 7647 (999.4 L) lies past the fit rows and inside the inverse domain, as the lead now states.

Verdict. CONFIRMED: the lead's correction (fit rows r < 900 L, inverse domain r <= 1000 L, knot positions and fractions)
holds for c6g.

G79 (b) (2026-10-18T17:53:54Z). The 375 x m <= 100 domain series. Shape files read with my loader: c6dS1 (runs/gen4/c6dS1_shape.npz)
R_shape 1000, no fit_radius key (run of the older long_solve, whose centre_fit.py in lead/artifacts/a_generator and
b_fit has line 41 rows = r < 0.9 R, no option); dom300_seg1 R_shape 333.33, fit_radius 300; dom100_seg1 R_shape 111.11,
fit_radius 100; dom90_seg1 / seg2 R_shape 100, fit_radius 90; all angular 100, 37882 coefficients, 370 distinct knots. So
the series has fit rows r < 900 L, 300 L, 100 L (and 90 L for dom90), as the lead's text now states. CONFIRMED. The
dependence on which centre_fit.py the c6dS1 run imported is not checked beyond both copies having the same line 41.

## G80 (2026-10-18T17:58:16Z). Baseline on c6g for the lead's reading (44) (b) of dom9000g (lead NOTES 17:42:41Z item 4); data, no verdict

Method. New option of code/vaudit.py: VAUDIT_RBANDS='a:b,c:inf' adds the regions a < r <= b in physical r, each also with
A5 (pi/2 - theta >= 0.006). Tested on a coarse c6g run (N4500 q192, runs/audit/c6g_N4500_q192_R7.652e6_rbtest.*, test only).
c6g in its own (formula) convention, k_self, R 7.652e6, bands 1000 L < r <= 9000 L (7651.4 < r <= 68862.8) and r > 1e4 L
(r > 76514.2), at the two configurations with N >= 16875 that I use for far-band rows: N16875 q512 M639 and N22500 q384 M479
(scratch/c6g_rb44.sh, files runs/audit/c6g_N*_R7.652e6_rb44.json).

Result (N_v maxima; N16875 q512 / N22500 q384).
- 1000 L < r <= 9000 L: 1.102e-6 at r 3.72e4 (4858 L), theta 1.5683 / 1.094e-6 at r 3.70e4, theta 1.5675. With A5:
  1.075e-6 / 1.086e-6. The unrestricted values equal those of my r > 1000 band (1000 <= r <= R row), so on c6g the far-band
  maximum lies inside 1000 L to 9000 L, within 0.003 of the y-axis.
- r > 1e4 L: 9.34e-7 / 9.28e-7, with A5 9.17e-7 / 9.22e-7, in each case at r 7.66e4 to 7.67e4, the inner edge of the band.
- h(P) - 1: +3.1e-8 / -1.8e-8; c_l (identity) 5.5753626074.
Use. For (44) (b) the ratio dom9000g / c6g is to be read against these numbers on the same two configurations, dom9000g in its
own convention (closure at R_shape 1e4 L, VAUDIT_RFIT 9000 L) and also with the formula continued. The lead's c6g value
"1.09e-6 to 1.11e-6" for the inner band is CONFIRMED on these two configurations. For r > 1e4 L the c6g value is 9.3e-7. Since
the maximum sits on the band edge, the reading should also give the dom9000g maximum location.

## G81 (2026-10-18T17:59:17Z). Far-field first-correction identity of the numerics referee (NUM NOTES_FOR_LEAD 17:51:20Z item 2 (d)); algebra only

Claim (astra/farrow, through the numerics lane). If rho = r^k A(theta) + r^(2k-1) B(theta) + o(r^(2k-1)) and U = r^k V(theta) +
o(r^k), termwise differentiable, with V the homogeneous inverse of r^k A, then c_l k = 1 and (c_l - 1) B = k V_r A + V_theta A'.
At the quadratic zero of A on the y-axis, B/A tends to -(k + 2) V_r(pi/2)/(c_l - 1).

Method. Substituted the expansion into c_l r d_r rho + U_r d_r rho + r^(-1) U_theta d_theta rho = rho.
- Order r^k: (c_l k - 1) A = 0.
- Order r^(2k-1): c_l (2k - 1) B + k V_r A + V_theta A' = B. With c_l k = 1, c_l (2k - 1) - 1 = 1 - c_l, which gives the
  stated identity. The velocity correction carried by B enters at order r^(3k-2), which is lower since k < 1.
- Axis limit, with delta = pi/2 - theta: A = a delta^2 + O(delta^4) (even in x), so A'/A = -2/delta + O(delta). V_theta is
  odd about theta = pi/2, and div U = 0 gives (k + 1) V_r + V_theta' = 0, so V_theta = (k + 1) V_r(pi/2) delta + O(delta^3).
  Then V_theta A'/A tends to -2 (k + 1) V_r(pi/2), and B/A tends to (k - 2k - 2) V_r(pi/2)/(c_l - 1) = -(k + 2) V_r(pi/2)/(c_l - 1).
- With the referee's V_r(pi/2) = 89.3339213, k = 0.179360531, c_l = 5.5753626106: -42.551998, the referee's "required" value.

Verdict. CONFIRMED as a formal identity under the stated expansion hypothesis (it is not a theorem about the profile, whose
far-field expansion is assumed). Not checked: the referee's V_r(pi/2) and stored Theta_1 = -42.556083 on c6g, and the size
estimates (2.9e-6, -2.9e-6, +6e-7) built from them. OPEN for a later shift: compute V_r(pi/2) from my own inverse on c6g's
Theta_0 and the stored Theta_1 from b_m(1), b_m'(1), and compare r^(1-k) R/rho at large r with its predicted angular limit.

G80 addendum (2026-10-18T18:04:17Z). Split at c6g's own collocation boundary 900 L (numerics NOTES 17:51:20Z item 2 (a)); scratch/c6g_rb44r.sh,
same two configurations, files runs/audit/c6g_N*_R7.652e6_rb44r.json. N_v maxima (N16875 q512 / N22500 q384):
- 900 L < r <= 1000 L (past the fit rows, inside the inverse domain): 2.186e-7 at r 7644, theta 1.5561 / 2.157e-7 at r 7650,
  theta 1.5544; the same with A5. This reproduces the lead's 2.15e-7 at r 7647 (999.4 L) on my evaluator, at the outer
  edge of the inverse domain.
- 900 L < r <= 9000 L: identical to the 1000 L < r <= 9000 L row (1.102e-6 / 1.094e-6 at r 3.7e4), so the c6g maximum beyond
  its fit rows is the one at about 4860 L.

## G82 (2026-10-18T18:24:12Z). G81 OPEN item closed (own inverse of Theta_0 on c6g); prediction P measured (lead NOTES 18:04:24Z item 2); seven fits

Code. code/far1_ver.py (new, from the definitions only): Theta_0 = L^(3-k) cos^2 t sin t exp(H(q = 1, t)) with b_m(1) from the
B-splines (extrapolate on) and the singular terms at s = 1, q = 1; Theta_0' analytically (the |cos t|^(p3-2) factor
differentiated by hand) and checked against the FFT derivative; g = k cos t Theta_0 - sin t Theta_0'; F_n = G_n/(n^2 - (k+1)^2)
on the full circle; V_r = -F', V_theta = (k+1) F; forced Theta_1 = (k V_r Theta_0 + V_theta Theta_0')/((c_l - 1) Theta_0) with
c_l = 1/k, axis limit -(k+2) V_r(pi/2)/(c_l - 1); stored Theta_1 = -L^(1-k) dH/dq(1, t). Checks on c6g: ODE residual 6.5e-16,
odd-n part of g 9e-16, two derivative routes 4.5e-12 (relative). Outputs runs/far1/<fit>_nt*.json and _prof.npz.

(a) c6g (X3), nt = 16384 and 65536 identical to the digits shown: V_r(pi/2) = 89.3339213, Theta_1 forced -42.5519983, stored
-42.5560826, C(pi/2) = (c_l - 1)(forced - stored) = +0.0186871, C/(1+k) = +0.0158451. |forced - stored| is at most 4.1e-5 on
0 < theta < 0.05, at most 7.91e-4 on 0.05 < theta < 1.4 (at 1.3999), and rises to the axis value between 1.4 and pi/2
(2.36e-3 at 1.5, 4.03e-3 at 1.56, 4.084e-3 at pi/2). C/(1+k) at theta 0.1001, 0.3001, 0.6, 0.818, 1.0, 1.2, 1.3999, 1.5,
1.5501, 1.565: -2.329e-4, -1.065e-3, -1.949e-3, -1.724e-3, -1.120e-3, -1.368e-4, +3.059e-3, +9.144e-3, +1.486e-2, +1.576e-2.
These equal the numerics referee's and the lead's values (lead NOTES 18:04:24Z item 2) to all digits given (+3.059e-3 at
1.3999 against the lead's +3.067e-3, the lead's row being at 1.4000). The G81 OPEN item is CONFIRMED. The 4.5 number "2.9e-6
at the band maximum" is CONFIRMED: C r^(k-1)/(1+k) = 2.89e-6 at r 3.6e4 on the column theta 1.5683.
Note: in ../lead/work/far/far1_multi.json the key "C_axis" (0.018585 on X3) is C at theta 1.565, not at pi/2 (0.018687);
not quoted in the text.

(b) Seven fits, nt = 16384 (axis |forced - stored|; maximum on 0.05 < theta < 1.4; C(pi/2)/(1+k)):
     c6g (X3)        4.084e-3   7.87e-4   1.5845e-2
     c6gF (F3)       4.073e-3   7.55e-4   1.5806e-2
     s2g (X2)        4.136e-3   6.99e-4   1.6045e-2
     seg3g (F2)      4.108e-3   7.11e-4   1.5939e-2
     fxm1o2i250 (X1) 4.312e-3   1.164e-3  1.6727e-2
     c6fS1 (F0)      4.179e-3   1.441e-3  1.6218e-2
     dom90g          4.116e-3   7.94e-4   1.5968e-2
  The axis values agree within 6 percent (4.07e-3 to 4.31e-3; the lead's 4.30e-3 for X1 is a grid maximum next to the axis,
  and its far1_multi.json bulk maxima 7.0e-4 to 1.44e-3 equal mine). The off-axis maxima do NOT agree within 6 percent
  (7.0e-4 to 1.44e-3, F0 and X1 1.5 to 1.8 times X3).

(c) Prediction P. scratch/farP.py: gen_shape (formula convention, no closure) -> vcand (own inverse, k_self tails, identity
c_l) -> signed R/N_v on the evaluator columns theta_j = 2 pi j/2560 (M 639), times r^(1-k), over the predicted C(theta_j)/(1+k)
(far1_ver on 40960 angles, so the angles coincide). Window = min to max over the 11 radial nodes centred on the row. Also
with c_l = 1/k (R + (1/k - c_l,ev) X.grad rho). Runs (tok_run, jS.log 18:15:55Z to 18:20:12Z, rc 0, max RSS 7.4 GB / 8.8 GB):
runs/farP/c6g_N16875_q512_R7.652e6.json (R = 1e6 L) and c6g_N20250_q512_R7.652e8.json (R = 1e8 L, the same radial spacing).
Identity c_l: 5.5753626074 / 5.5753626072, delta = c_l,ev - 1/k = -3.26e-9 / -3.43e-9, which leaves the constant
k delta/(1+k) = -5.0e-10 / -5.2e-10 in R/N_v (r-independent, it does not decay).
Ratio measured / predicted, R = 1e8 L, identity c_l (c_l = 1/k in brackets where it differs by more than 0.01):
   theta     pred        4701 L  9504 L  3e4 L   1e5 L          3e5 L          5e5 L          window at 1e5 / 5e5 L
   0.8173   -1.742e-3   0.716   1.005   1.153   1.131 (1.111)  1.119 (1.069)  1.122 (1.046)  1.12-1.13 / 1.10-1.13 (1/k: 1.10-1.11 / 1.02-1.06)
   1.56343  +1.572e-2   0.375   0.581   0.810   0.921          0.966          0.981 (0.990)  0.92-0.92 / 0.96-0.98
   1.56589  +1.578e-2   0.376   0.580   0.815   0.918          1.017          1.027 (1.035)  0.91-0.93 / 0.87-1.06
   1.56834  +1.583e-2   0.379   0.582   0.822   0.927          1.001          1.055 (1.063)  0.89-0.95 / 0.80-1.08
  R = 1e6 L gives the same to 0.005 up to 1e5 L; at 3e5 and 5e5 L it reads lower (1.56343: 0.949, 0.930), the outer tail
  being within a factor 2 to 3, so the 1e8 L run is the one read there.
  P (within 0.15 of 1 at 1e5 L, and closer to 1 at 5e5 L than at 1e5 L, near 1.565 and at 0.818): holds at every named
  column, in both c_l conventions, at the row nodes. CONFIRMED, with these qualifications: (i) on the two columns within
  0.006 of the y-axis (1.56589 is the one nearest 1.565; 1.56834) the node-to-node scatter at 3e5 to 5e5 L (0.80 to 1.08) is
  larger than the change from 1e5 L, so "closer" is not resolved there; on 1.56343, the first column outside that strip, the
  windows separate (0.96-0.98 against 0.92-0.92). (ii) At 0.8173 with the identity c_l the windows overlap (1.10-1.13 against
  1.12-1.13); with c_l = 1/k they separate (1.02-1.06 against 1.10-1.11). The difference is the constant of the identity
  defect, which is 7.5 percent of the predicted first-order term at 0.818 at 5e5 L and would dominate it beyond about 1e7 L
  on that column. (iii) Beyond 1e6 L the scatter grows on every column (3e6 L: windows 0.5 to 1.4 near the axis, 0.9 to 1.4
  at 0.8173), so the evaluator does not follow the limit past about 1e6 L at this resolution.
  Lead's far2_X3.txt (second order, not audited) gives sum/leading 0.924 and 0.979 at 1e5 and 5e5 L on theta 1.56811; mine
  on 1.56834 is 0.927 at 1e5 L, and 0.981 at 5e5 L on 1.56343.

(d) Lead NOTES 18:13:30Z item 3, "off the axis the leading term is reached inside 1e4 L": REFUTED as worded. My 4701 and
9504 L values at 0.8173 reproduce the lead's (0.716, 1.005 against 0.72, 1.007), but the ratio does not stay at 1: it
overshoots to 1.15 at 3e4 L and comes back slowly (1.11, 1.07, 1.05 at 1e5, 3e5, 5e5 L with c_l = 1/k). Columns 0.6 and 1.0
do the same (1.17 at 3e4 L, 1.06 / 1.08 at 5e5 L with c_l = 1/k). Where C is small the higher orders dominate longer: 0.1006
reads 1.73 at 3e4 L and 1.42 at 1e5 L, 1.2002 (next to the sign changes of C at 1.227 to 1.241) 2.4 and 1.8. Suggested: "off the axis the
ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns toward 1 slowly (1.05 to 1.08 at 5e5 L)".

(e) Not audited: the lead's far2 (second-order) analysis; the referee's PROOF.md beyond the identity of G81.

## G83 (2026-10-18T18:25:24Z). Re-audit of section 4 v5 full (lead NOTES 17:37:53Z list, 17:42:41Z items 1-3, 18:04:24Z items 3 and 7, 18:13:30Z item 1)

Files. ../lead/notes/final_sec4_v5_full.md md5 908fb9d27ebce0056cf3ecfe56f7f53f (501 lines, copy
scratch/final_sec4_v5_full_1805_908f.md), then md5 5d09482e1b7043928b9c1a168d725bad (504 lines, 18:13Z, copy
scratch/final_sec4_v5_full_1817_5d09.md). Method: diff of 908f against _pre_G76 (= my scratch/final_sec4_v5_full_1721.md) and
_post_G76; every changed sentence checked against G76 (h) 1-29, G77, G78, G79 and the source JSONs; diff 908f -> 5d09 is
the 4.5 inverse paragraph only (X3 ray check). Line numbers below are of 5d09.

CONFIRMED: the G76 (h) corrections 1-29 as applied (17:37:53Z list), with the exceptions below; G77 / G78 / G79 items
(17:42:41Z items 1-3: fit rows r < 900 L in 4.2, domain table, timeline); the G76 / G77 addenda as applied (18:04:24Z item 7,
L270-273 and the "raw (cut)" column); the 4.5 identity and axis limit (G81) and "0.0187 on the axis, 2.9e-6 at the band
maximum ... 0.38 ... 0.58 at 9500 L" (G82 (a), (c)); the last sentence of 4.5 [V, A] (the referee's wording) is a correct
statement of what is not established. X3 ray [V] (L435-439): CONFIRMED against ../numerics/runs/ray/x3_c6g_table.txt and
x3_c6g_BP.json: 52 targets; max |dU| 9.96e-10 (P < 0.5), 3.62e-8 (0.5 to 2.5), 7.68e-12, 5.13e-11, 9.81e-10, 4.87e-9,
1.46e-8 (r = 0.1, 1, 20, 100, 300); max impact 2.573e-9, median 2.719e-11; export convention (export_fit.py, 24576 x 576,
inverse domain 1e4 shape units with the two-term closure) the same as X1's (NUM_REPORT 3.17 item 7 (xiii)); 6.5e-7 to 6.8e-7
is the 4.4 row |X - P| < 0.5 (6.51e-7 / 6.84e-7).

Corrections (wording; no number read by a selection rule changes):
 C1. L72-74 (4.1, cap bullet): "lowered whole-box N_f by 0.475 ... and the near-P window y >= 1 of 4.4 by 1.01 and 0.81": in
     a list of factors "lowered by", 1.01 is a rise. Suggested: "...; the near-P window y >= 1 of 4.4 changed by the ratios
     1.01 (11250 x 384, the under-resolved lobe of 4.4) and 0.81 (16875 x 512)".
 C2. L218-220 (4.3 reading): "every window near P of 4.4 except y >= 1 falls by a factor 2.1 to 2.5, and the window y >= 1 by
     1.01 (11250 x 384) and 1.23 (16875 x 512)". At 11250 x 384 that window rises by 1 percent (s2g 6.83e-7 -> c6g 6.91e-7,
     G73 (h)); at 16875 x 512 it falls by the factor 1.23 (5.32e-7 -> 4.32e-7). The error is mine: G76 (h) 6, the G76
     addendum ("1.01 at N11250 q384 and 1.23 at N16875 q512") and G78 mix the ratio 1.01 with the factor 1.23. Suggested:
     "and the window y >= 1 rises by 1 percent at 11250 x 384 (the under-resolved lobe of 4.4) and falls by a factor 1.23 at
     16875 x 512". G76 (h) 6 and the G76 addendum are corrected by this item.
 C3. L498-499 (4.8): "0.935 to 0.938 in whole-box N_f, ... 0.935 to 0.987 in N_v for r <= 1000" need "(y-axis floor columns
     excluded)"; without the exclusion 0.83 and 0.825 at 16875 x 768, as 4.1 L61-64 says. (L67-68 follows the qualified
     sentence with "thus" and can stay.)
 C4. L100 (4.1 remark): "radial bases from 215 to 375 functions" should read "200 to 375": the 136 audits include c4cen
     (c4_centre_shape.npz, 200 radial functions, identity c_l 5.57633), whose original-form median 0.2803 is one of the low
     values quoted in G76 (h) 23.
 C5. L321: "the formula-global fits, whose formula is fitted out to 1000 L" contradicts L127 and G79 (rows r < 900 L).
     Suggested: "whose rows are r < 900 L and whose inverse domain is r <= 1000 L".
 C6. L416-418 (4.5 [V, A]): "by at most 7.9e-4 elsewhere" holds on 0 < theta < 1.4 only; between 1.4 and pi/2 the difference
     rises to the axis value (2.36e-3 at 1.5, 4.03e-3 at 1.56). "and by the same amount within 6 percent on the seven fits
     measured" holds for the axis value (4.07e-3 to 4.31e-3), not for the off-axis maximum (7.0e-4 to 1.44e-3; F0 1.44e-3, X1
     1.16e-3) (G82 (b)). Suggested: "... and by at most 7.9e-4 for theta < 1.4; on the seven fits measured the axis
     difference is 4.07e-3 to 4.31e-3".
 C7. L294 (domain table, 90 L row): "1.02, 1.23, 0.83 (0.84)" places the cut value after the 22500 x 384 entry, but it is the
     16875 x 512 value (G77: 7.26e-8 / 8.66e-8). Suggested: "1.02, 1.23 (cut 0.84), 0.83".
 C8. L437-439 (X3 ray): the impact 2.6e-9 is at (8.550, 1.994), 0.5 to 2.5 from P; within 0.5 of P the impact is at most
     8.6e-10 (20 of the 52 targets; 12 targets at 0.5 to 2.5, recomputed from x3_c6g_BP.json with P = (8.6001, 0)). Since the
     comparison is with the N_f maxima within 0.5 of P, suggested: "at most 8.6e-10 within 0.5 of P and
     2.6e-9 at 0.5 to 2.5 from P (median 2.7e-11)".
 Optional, from G82 (c), (d): after "the ratio rises to 0.58 at 9500 L" the verifier's measurement can be cited: "and, in the
     formula convention to 1e8 L, to 0.92 at 1e5 L and 0.98 at 5e5 L next to the axis (prediction P, fixed before the
     measurement, holds); off the axis the ratio crosses 1 near 9500 L, overshoots to 1.15 at 3e4 L and returns to 1.05 at
     5e5 L". The lead's 18:13:30Z item 3 sentence "off the axis the leading term is reached inside 1e4 L" should not enter.

Verdict. Section 4 v5 full (5d09482e): CONFIRMED subject to C1 to C8. It is still not ported to FINAL_REPORT.md; [TBD] / [D] /
[A] slots remain (300 L domain, 244 and 250 rows, fixed-c_l scan, a fit with rows to 9000 L). Team may NOT finish.

## G84 (2026-10-18T18:33:04Z). Far-field third-order series (lead NOTES 18:19:06Z items 2-3, 18:24:48Z items 1-3); section 4 md5 cff2d3d0

Code. code/far2_ver.py (new; from the definitions and my code/gen_shape.py only, not from far2.py or the referee's script).
Terms indexed (n, p), exponent a = k + n (k - 1) - 2 p, delta = r^(k-1), eps = r^-2 (physical r). Density from the formula:
log rho = log Theta_0 + k log r + lam1 delta + lam2 delta^2 + lam3 delta^3 + lamh eps + O(delta eps), lam_j = (-1)^j
d^j H/dq^j(1)/j! L^(j(1-k)) (B-spline derivatives at q = 1, Chebyshev derivatives for the singular terms), lamh = L^2 [(k-3)/2 -
r0^2 sum_{m>1} (m-1) b_m(1) cos 2mt - (p3/2) T(1) v] (gen_shape.py applies chi^(m-1) only for m > 1, so the lead's max(m-1, 0) is
right). Velocity of each density term by its own homogeneous inverse (F'' + (a+1)^2 F = -(a cos A - sin A'), even sine
series; no resonance). R = c_l r d_r rho + U.grad rho - rho at c_l = 1/k; U^(n1,p1).grad rho^(n2,p2) of order (n1+n2+1, p1+p2);
N_v with each absolute value expanded about the sign of its leading coefficient; R/N_v by series division. Checks: parity of
the three sources (odd-n parts 7.5e-13 to 3.3e-12), R at order (0,0) zero; nt = 32768 and 65536 agree to 7 digits.

(a) Coefficients on c6g (X3), nt 65536, at the lead's columns:
     theta     q1              q2          qh          q3           R1 / R2 / R3                   h
     1.56811   +1.58216590e-2  -88.78237   +782.1024   +1.190005e5  +1.8659e-2 / -101.87 / 1.2424e5  -82.719
     1.56265   +1.57024031e-2  -88.67412   +782.0859   +1.188710e5  +1.8519e-2 / -101.79 / 1.2428e5  -82.718
     1.54625   +1.45499034e-2  -82.79100   +781.9324   +1.057428e5  +1.7160e-2 / -95.281 / 1.1115e5  -82.701
     0.81819   -1.71803916e-3  -29.33804   +2388.506   -1.422910e5  -2.0262e-3 / -34.602 / -1.6784e5 -252.62
  These equal ../lead/work/far/far2_X3.txt (nt 65536 rows) to every digit printed (q1 to 7 digits). h(pi/2) = -82.7196 and
  qh(pi/2) = -2 c_l h/(1+k) = 782.104 (lead's request (i): expected -82.72, 782.1): CONFIRMED. Second order at 1.56811: the
  three parts of R2 / A0 are -1.1526e4 ((c_l a - 1) A2), +1.1368e4 (U0 on A1), +56.8 (U1 on A0); R2 = -101.87 is 0.88 percent of
  the largest: "0.9 percent of the terms it balances" CONFIRMED next to the axis. At 0.818 there is no near-cancellation
  (-5.8, -19.3, -9.5, sum -34.6), so that phrase holds next to the axis only. First order: |forced - stored| / |Theta_1| =
  4.08e-3 / 42.55 = 9.6e-5 ("1e-4 relative in Theta_1") CONFIRMED. h involves only k, L, r0 and the end values b_m(1), T(1)
  (no end slope): "no choice of the end slopes removes them" CONFIRMED.

(b) Lead's request (ii): series against my own evaluator (runs/farP/c6g_N20250_q512_R7.652e8.json, formula convention, my
  inverse to 1e8 L; scratch/farS.py, series at the evaluator's exact columns, output runs/far2/farS_c6g_R1e8.json).
  Measured / series, with c_l = 1/k (that is, the identity constant k delta/(1+k) = -5.22e-10 removed); window = 11 nodes:
     theta     3000 L  4700 L  9504 L  3e4 L           1e5 L           3e5 L           5e5 L
     0.8173    0.362   0.727   0.956   0.998 (.997-.999) 1.001 (.995-1.003) 1.007 (.978-1.008) 1.002 (.981-1.013)
     1.56343   0.591   0.867   0.981   1.0005 (.997-1.001) 1.0001 (.996-1.003) 1.004 (.993-1.005) 1.012 (.986-1.012)
     1.56589   0.594   0.868   0.977   1.006 (.990-1.006) 0.996 (.990-1.009) 1.057 (.88-1.08)  1.058 (.90-1.09)
     1.56834   0.597   0.870   0.978   1.013 (.986-1.014) 1.005 (.970-1.026) 1.039 (.92-1.04)  1.086 (.83-1.11)
  With the identity c_l (constant kept) the 0.8173 column reads 1.005, 1.019, 1.054, 1.074 at 3e4 to 5e5 L, so the constant is
  needed there, as the lead says. Measured values at 4700 / 9504 L on 1.56834: 1.0947e-6 / 9.434e-7 (lead 1.092e-6 / 0.945e-6);
  my four-term sums there 1.2593e-6 / 9.653e-7 (lead's text 1.26e-6 / 0.965e-6 at 1.568). CONFIRMED.
  "Measured equals series plus constant to 1e-3 from 3e4 L to 3e6 L": on my evaluator CONFIRMED to 2e-3 at 3e4 and 1e5 L on
  the two resolved columns (0.8173, 1.56343), to 1.2e-2 at 3e5 and 5e5 L (inside the node scatter of 1 to 3 percent); on the
  two columns within 0.006 of the axis it is resolved only to 1e5 L (to 1.3e-2); beyond 1e6 L my evaluator does not resolve
  it (G82 (c) (iii)). The 1e-3 statement to 3e6 L rests on the lead's evaluator alone (work/far/ptest.py, not audited).

(c) Lead NOTES 18:24:48Z item 2: P on my evaluator in the formula-continued convention is G82 (c): raw and constant-removed
  ratios are both there (the "(...)" values are c_l = 1/k, which removes (c_l k - 1)/(1+k) exactly at leading order; my
  constant is -5.22e-10 at R 1e8 L, -5.0e-10 at R 1e6 L). My outer radius for the read values is 1e8 L, so 5e5 L is not near the
  boundary; 3e5 L is in the G82 table (1.56343: 0.966 raw, 0.972 c_l = 1/k; 0.8173: 1.119 / 1.069).

(d) Section 4 md5 cff2d3d051ab824544f63703bd0e3dda (513 lines, copy scratch/final_sec4_v5_full_1829_cff2.md; the lead's
  NOTES 18:24:48Z names b4fd3095, the file on disk at 18:29Z is cff2d3d0). Diff against 5d09482e: the 4.5 far bracket only.
  C6 of G83 is applied (seven-fit axis 4.07e-3 to 4.31e-3, off-axis 7.0e-4 to 1.44e-3). Checked sentence by sentence:
  - "computed three times independently" (-42.5561 / -42.5520): lead, referee, mine (G82 (a)). CONFIRMED.
  - "by at most 7.9e-4 elsewhere": still unqualified; G83 C6 first half stands: "for theta < 1.4" (it rises to 2.36e-3 at 1.5).
  - "(formal; ... multipoles ... relative order r^(-4))": a multipole psi ~ r^-2 sin 2t gives U ~ r^-3 and U.grad rho / rho ~
    r^-4. CONFIRMED (formal).
  - The series line, its coefficients and "computed twice independently and agreeing to 4 digits": CONFIRMED; with mine it is
    three times, agreeing to 7 digits in q1 and to all digits printed otherwise (a).
  - "these four terms give 1.26e-6 at 4700 L and 0.965e-6 at 9500 L against the measured 1.09e-6 and 0.945e-6 (inside 2000 L the
    series is of no use)": CONFIRMED (b). For a reader, "of no use inside 2000 L" leaves 2000 to 4700 L open: on my evaluator
    measured / series is 0.59 at 3000 L and 0.87 at 4700 L. Suggested: "(measured / series 0.59, 0.87, 0.98 at 3000, 4700, 9500
    L; inside 2000 L the series is of no use)".
  - "With the trial's velocity computed to 1e7 L ... to 1e-3 relative, next to the y-axis and at theta 0.82": the lead's
    evaluator only; suggested: add "(on the verifier's evaluator, which resolves this to about 1e5 L, to 2e-3 at 3e4 and 1e5 L)".
  - "0.92 at 1e5 L and 0.97 to 0.98 at 5e5 L on two separately written evaluators": on mine 0.92 at 1e5 L on all four columns
    within 0.01 of the axis; 0.98 at 5e5 L on 1.56343 (0.99 with c_l = 1/k), while the two columns within 0.006 of the axis read
    1.03 and 1.05 there with node scatter 0.80 to 1.08 (G82 (c) (i)). Suggested: "0.97 to 0.98 at 5e5 L (on the verifier's
    evaluator on the column 1.5634; its columns within 0.006 of the axis are not resolved there)".
  - "Off the axis the ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns toward 1 slowly (1.05 to
    1.08 at 5e5 L with c_l = 1/k)": G82 (d) wording. CONFIRMED.
  - "So the band is the sum of a first-order and a second-order inconsistency ... (1e-4 relative in Theta_1; 0.9 percent of the
    balancing terms at second order) and of the r^(-2) terms of 4.2": CONFIRMED next to the axis, where the band maximum lies
    ((a); the 0.9 percent is an axis statement). "all three decay at infinity, the first-order one slowest": CONFIRMED
    (delta^1 = r^-0.82 against r^-1.64 and r^-2).
  - "its origin is not established ... does not establish an intrinsic floor": CONFIRMED as a statement of what is open.
  Verdict for the 4.5 far bracket: CONFIRMED subject to the G83 C6 first half and the two suggested qualifications above.
  G83 C1 to C5, C7, C8 are not yet applied in cff2d3d0 (they are outside the bracket); they stand.

## G85 (2026-10-18T18:42:51Z). FINAL_REPORT port (md5 308eeb82) and section 5 v4 (md5 8b71d4f3); correction of the G77 reading of A4
Lead NOTES 18:32:23Z item 4 (a), (c). Port: FINAL_REPORT.md md5 308eeb826544129c3dec9ad2dc6be313 (copy
scratch/FINAL_REPORT_lead_1835_308e.md) against notes/FINAL_REPORT_pre_port4.md md5 900550b8 (copy
scratch/FINAL_REPORT_pre_port4_9005.md) and section 4 v5 1a0472e1 (scratch/final_sec4_v5_full_1833_1a04.md). Line numbers
are those of 308eeb82.

(a) Port, section 4.
  a1. G83 C1 to C8 are applied: C1 L291-294 and L496-498, C2 L646-647, C3 L486 and L938, C4 L526, C5 L751, C6 L850-851,
      C7 L724, C8 L876-877. CONFIRMED. The marker conversion ([A], [D], [TBD] to [OPEN]; [V] brackets removed) is faithful
      outside the items below.
  a2. 4.5 far paragraph (L853-860). The port carries the shorter text without the series line and without the constant
      sentence of v5 1a0472e1 L424-431, and ends the first-order statement with "[OPEN: the third-order expansion]".
      - "Next to the axis the measured value is 0.38 of the leading term at 4700 L and 0.58 at 9500 L": CONFIRMED (G82 (c):
        0.375 to 0.379 and 0.580 to 0.582 on the four columns within 0.01 of the axis).
      - "with the formula continued to 1e8 L the ratio is 0.92 at 1e5 L and 0.98 at 5e5 L, as predicted before those radii
        were evaluated": 0.92 CONFIRMED on the four columns (0.918 to 0.927). 0.98 at 5e5 L holds on theta 1.56343 (0.981;
        0.990 with c_l = 1/k); the two columns within 0.006 of the axis read 1.03 and 1.06 with node scatter 0.80 to 1.08
        (G82 (c) (i)). Suggested: "0.98 at 5e5 L (theta 1.5634; the columns within 0.006 of the axis are not resolved
        there)".
      - "(1.05 to 1.08 at 5e5 L)": REFUTED as written. The values hold with c_l = 1/k (mine at theta 0.8173: 1.046, window
        1.02 to 1.06). With the identity c_l of the inverse mine reads 1.122 (window 1.10 to 1.13); the difference is the
        r-independent constant k(c_l - 1/k)/(1+k) = -5.2e-10, which the port no longer mentions. v5 1a0472e1 L432 had "with
        c_l = 1/k"; the port dropped it. Suggested: "(1.05 to 1.08 at 5e5 L with c_l = 1/k; with the identity value of c_l
        of the inverse, an r-independent constant k(c_l - 1/k)/(1+k) = -5.2e-10 is added and the ratio at theta 0.82 reads
        1.12)".
      - "next to the axis it accounts for nine tenths of the far residual from 1e5 L outward": inexact. Measured / first-order
        term is 0.92 to 0.98 at 1e5 to 5e5 L, so the first-order term is 1.02 to 1.09 times the far residual, not nine
        tenths of it (the remainder, mainly the delta^2 term, is negative). "Outward" goes past the radii read (my rows at 1e6
        and 3e6 L were not read, G82 (c)). Suggested: "next to the axis the far residual is 0.92 to 0.98 of it from 1e5 L to
        5e5 L".
      - "while at the band maximum the higher orders of the trial's expansion are comparable to it": CONFIRMED (measured /
        leading 0.38 to 0.58 at 4700 to 9500 L; the delta^2 term is -0.42 to -0.62 of the leading one there, G84 (a)).
      - "[OPEN: the third-order expansion]": no longer open. G84 (a) and (b) confirm the series with an independent code
        (code/far2_ver.py) and the measured / series ratios on my evaluator. Either the v5 1a0472e1 series text L424-431
        is ported with the G84 (d) qualifications, or the marker is removed and the short text kept with the corrections
        above.
  a3. Timeline entry 17:35 (L318-327) and the domain table and rule (L722-728).
      - "residual rows r < 90 L and its own inverse on r <= 100 L with the two-term closure beyond": CONFIRMED
        (dom90g_shape.npz: R_shape 100, run_configuration fit_radius 90; gpu_long_solve.py: inverse radius = fit radius / 0.9
        unless --inverse-radius is given).
      - Numbers "1.04, 0.62, 0.72", "1.02, 1.23, 0.83", "h(P) - 1 = 5.6e-8 and 6.8e-10": CONFIRMED (G77).
      - "By the domain rule fixed before the runs (... within a factor 1.5 of the candidate's ...) it agrees on the three
        configurations": REFUTED as written. The rule fixed at 08:17Z says "within a factor 1.5"; in its plain reading the
        ratio must lie in [1/1.5, 1.5] = [0.667, 1.5]. The 2-10 ratio 0.62 (N16875 q512, my evaluator) is outside it on the
        low side. The lead's own rows (2-10: 0.695 and 0.728; 10-100: 0.816 and 0.822) and my other two configurations are
        inside it. The error is mine: G77 read the rule one-sided and wrote AGREE; see (c). Suggested: "By the domain rule
        fixed before the runs (...) it agrees on the lead's evaluator (2 <= r <= 10: 0.70 and 0.73; 10 <= r <= 100: 0.82)
        and on two of the verifier's three configurations; on the third (16875 x 512) its 2-10 maximum is 0.62 times the
        candidate's, outside the factor 1.5 on the low side. h(P) - 1 = ...". At L728, after "within a factor 1.5", add:
        "(read two-sided; the 90 L column falls below it at one configuration, being lower, not higher)".
      - "next to P its N_f is 0.32 to 0.33 times the candidate's": CONFIRMED (0.33, 0.33, 0.32).
      - "the 857-label J 0.40 times": 0.40 at eps 0.03 and 0.37 at eps 0.01 (G77). Since the table's J (5.53e-7 against
        1.39e-6) is the eps 0.03 value, "0.40 times (eps 0.03; 0.37 at eps 0.01)" is exact. Minor.
      - "the lobe above P does not move (0.98)": CONFIRMED (my map 0.98; the lead's 1.05).
      - "With the formula continued beyond its fit radius ... N_f about 3e-5 next to P and h(P) - 1 about -6e-5": CONFIRMED
        (3.11e-5, -5.95e-5).
      - Entries 17:50, 17:59 to 18:25 (0.921 / 0.981; 1.111 / 1.046 with c_l = 1/k; ray 1.0e-9 and 8.6e-10; C1 to C8):
        CONFIRMED.
  a4. Readability, not an error: L293 and L497 "1000 <= r <= 1000 L" mixes physical r and units of L; "1000 <= r <= 7652
      (= 1000 L)" reads unambiguously.

(b) Section 5 v4 (notes/final_sec5_v4_text.md, md5 8b71d4f3e55b88c3d7f6a7922ac3b09e).
  b1. Part (b) of the layout. "3e-14 relative in the products and 1e-13 in the adjoint products": CONFIRMED (gpu_chain.log
      step 1: matvec 3.16e-14 and 1.99e-14, rmatvec 1.73e-14 and 1.01e-13). "reproduced the CPU objective to 5e-5 relative
      after 250 iterations": CONFIRMED (step 2: 8.764888e-6 against 8.765359e-6, 5.4e-5; 9.5e-5 at 500). "the GPU logs
      record that value for every run from F2 on (the log of X2 has |phibar| only)": CONFIRMED (linres in seg3g.log,
      c6g.log, dom90g.log and dom300g.log; none in s2g.log).
  b2. Step 1. Wrapper usage and the six configurations: CONFIRMED (code/gen_audit.sh usage shape tag "r0 R N nq Mmax;..."
      [Rfit_phys]). "2 to 6 minutes each": the 16875 x 768 configuration took 7.5 minutes in my runs. Suggested "2 to 8
      minutes each".
  b3. Step 2. Commands and arguments: CONFIRMED against the usage lines (gen_shape.py shape r0 R N nq out [closure]; vaxis.py
      field Mmax out; vchar_dense.py field Mmax r_start n_uni n_geo dmin out). 737 + 2 x 60 = 857: n_geo is per axis (groups B
      and C), as the text says. "about 5 seconds" for gen_shape: 7 seconds in my runs (minor).
  b4. Step 5, the GPU command. It is the command logged for X3 (c6g, step 31), F3 (c6gF, step 32) and the domain columns
      (steps 33, 34; gpu_chain3.sh to gpu_chain6.sh, "--hours 4.9 --inner 2500 --check 250 $fix --max-its $its $SET",
      setting.txt "--damping 1e-8"). It is NOT the command of X2 and F2: those were run by the first chain
      (run_gpu_chain.sh L24 and L29) as "gpu_long_solve.py <in> <in> --nr 20480 --nt 720 --hours 0.75 --inner 2500
      --check 250 [--fix-cl]", without --max-its and with the default damping 1e-8; the wall-clock cap stopped both at the
      check of outer 9, it 750 (s2g.log and seg3g.log: total 20750 iterations, wall 2646 s). --max-its 20750 gives the same
      schedule (a check is forced there); whether a rerun reproduces the iterate bit for bit is not tested. Suggested, after
      the command: "(X2 and F2 were run with --hours 0.75 and no --max-its; the time cap stopped both at the check after
      20750 iterations, the schedule that --max-its 20750 reproduces)".
  b5. Step 5, "The m <= 200 starts are the m <= 150 ends with the new angular coefficients set to zero (...; the density is
      unchanged, residual difference 1.5e-15)": CONFIRMED. c6g_start_shape.npz against s2g_shape.npz: k, the m <= 150 block,
      the fractional-power block and the knots are identical, the m 151 to 200 block is zero; make_angular records
      res_max_diff 1.34e-15 (X3 start) and 1.47e-15 (F3 start), rho_rel_diff 0. Note: the stored L is a derived quantity of
      the lead's evaluation and depends on the grid on which a file was saved (7.651424586597564 in s2g_shape.npz at
      20480 x 720, 7.651424526080845 in c6g_start_shape.npz at 2048 x 960, relative 7.9e-9). My generator reads the stored
      L, so in my convention the two files differ at that level; this does not affect X3, whose own stored L is used.
  b6. Step 5, the domain sentence ("the rows are then r < fit radius (in units of L) and the inverse domain is the fit radius
      / 0.9 ...; without the option the rows are r < 900 L and the inverse domain r <= 1000 L"): CONFIRMED (a3; G79).
  b7. Steps 3, 4, 6, 7 and the CPU command of step 5 are the lead's codes and were not rerun for this entry.
  b8. Part (d) should name the far-field checks of 4.5 that 4.5 cites as separately computed: code/far1_ver.py (first
      correction), code/far2_ver.py (third-order series) and scratch/farP.py (measured against predicted, prediction P).
      Suggested addition to (d): "and the far-field checks of 4.5 (far1_ver.py, far2_ver.py, farP.py)".
  Verdict for section 5 v4: CONFIRMED subject to b2, b4 and b8 (b3 minor).

(c) Correction of G77. G77 applied A4 one-sided ("within a factor 1.5" met because dom90g is lower, G77 (4)) and wrote
  "AGREE on my rows". In the plain reading of the rule as fixed at 08:17Z the ratio must lie within [0.667, 1.5]. Corrected
  verdict: dom90g agrees with c6g by A4 on the lead's rows and on two of my three configurations (N11250 q384, N22500 q384);
  at N16875 q512 its 2-10 N_f maximum is 0.62 times c6g's, outside the factor on the low side. The rest of G77 stands. For
  dom300g and the later domain columns I apply the rule two-sided and report on which side a ratio leaves it.

Verdict G85: port CONFIRMED subject to a2 (the "c_l = 1/k" qualifier, "nine tenths", the column qualifier, the [OPEN]
marker) and a3 (the two-sided A4 reading; J 0.40 at eps 0.03). Section 5 v4 CONFIRMED subject to b2, b4, b8. G77 corrected
as in (c). The team may NOT finish.

## G86 (2026-10-18T19:03:52Z). Domain column dom300g (chain step 34) on my evaluator: the A4 rule, two-sided (G85 (c)), against X3 = c6g; with dom90g
Run. dom300g: c6g end continued 20750 iterations at the fixed c_l, 20480 x 960, fit radius 300 L (rows r < 300 L, inverse
r <= 333.3 L, two-term closure beyond), step 34 done 18:43:41Z, objective 1.314892e-6, md5 54ea57a7a472755d1b94af398278ee52
(copy runs/gen4/gpu/dom300g_shape.npz, md5 checked against the chain line by jV, 18:43:49Z). Same budget as dom90g (G77).
Method as G77: fit convention (closure at R_shape, k_self, Rfit = 300 L = 2295.43), configurations N11250 q384, N16875 q512,
N22500 q384 (jV a1, dom3_wait a3); BA5 at N16875 q512; 857-label J and vaxis with the closure at N16875 q384 (jV jr); residual
map near P with the closure at N16875 q512 (dom300g512, scratch/cmp_resmap.py against c6g512); formula convention at N11250
q384 (_frm). Base c6g in its own (formula-global) convention, the G77 rows. All runs rc 0 (runs/audit/jS.log 18:43:49Z to
19:02:33Z).

Result, dom300g / c6g (N11250 q384, N16875 q512, N22500 q384):
  2 <= r <= 10, N_f maximum: 6.867e-7 / 6.909e-7 (0.994), 4.272e-7 / 6.841e-7 (0.624), 4.889e-7 / 6.605e-7 (0.740). At N11250
    both maxima are at the N11250 lobe point r 8.784, theta 0.3076 (G73 (h)); at N >= 16875 the dom300g maximum is the lobe
    above P (r 8.74, theta 0.193, y about 1.7) and c6g's is next to P, as for dom90g.
  10 <= r <= 100, N_f maximum raw: 1.215e-7 / 1.368e-7 (0.888), 2.002e-7 / 2.644e-7 (0.757), 1.881e-7 / 1.954e-7 (0.963), in the
    floor column (theta 1.5675 to 1.5683, r 10.1 to 10.4) at N >= 16875. With A5 at N16875 q512: 6.803e-8 / 8.659e-8 (0.786).
  h(P) - 1: +3.47e-7 / +2.84e-7 (N11250, biased on both, G77), +5.08e-8 / +3.11e-8, -3.07e-9 / -1.78e-8.
  Next to P (|X - P| < 0.5), N_f: 3.860e-7 / 6.505e-7 (0.593), 3.892e-7 / 6.841e-7 (0.569), 3.863e-7 / 6.605e-7 (0.585).
  857-label J (eps 0.03 / 0.01): 8.144e-7 / 9.031e-7 against 1.3882e-6 / 1.6019e-6 (0.587 / 0.564).
  Map at N16875 q512 (R / N_f maxima, dom300g / c6g): strip y < 0.2, 6 < x < 8.1: 3.71e-7 / 5.56e-7 (0.67); y < 0.2,
    8.1 <= x < 8.6: 3.89e-7 / 6.84e-7 (0.57); y 0.2 to 1, |x - x*| < 1: 3.44e-7 / 5.68e-7 (0.61); y >= 1 (the lobe):
    4.27e-7 / 4.32e-7 (0.99); right of x*: 1.56e-7 / 1.83e-7. Cap-frequency ripple (omega 399) at r 8.447: 3.89e-8 / 6.11e-8.
  Within the fit domain: N_v on 1000 <= r <= Rfit 6.4e-8 to 6.5e-8; beyond Rfit the closure gives N_v 5.1e-3 (r 5815,
    theta 1.568): the closed problem's exterior, not a trial (4.4).
  Formula convention (N11250 q384, formula continued to 7.652e6): next to P 4.86e-7, 2-10 7.66e-7, 10-100 2.06e-7,
    h(P) - 1 +1.33e-7, c_l (identity) 5.5753626, far N_v 3.6e-5 (dom90g: 3.1e-5 next to P, h(P) - 1 -5.95e-5).
Lead's reading (work/c6/dom300g_a4.txt, 18:45:02Z, lead scans 32768 x 640 / 24576 x 960): 2-10 0.738 / 0.721, 10-100 0.860 /
  0.859, h(P) - 1 -8.2e-9 / -4.8e-9, "A4 AGREE". My N22500 q384 row (0.740, 0.963) is close to it; my N16875 q512 row is
  lower in 2-10.

Reading by A4, two-sided (ratios in [0.667, 1.5]; |h(P) - 1| < 1e-7 on N >= 16875). 2-10: 0.994 and 0.740 inside, 0.624 at
N16875 q512 outside on the low side. 10-100: all inside (0.888, 0.757 raw and 0.786 with A5, 0.963). h(P): inside on
N >= 16875 (5.1e-8, 3.1e-9). Verdict: dom300g AGREES with c6g on the lead's rows and on two of my three configurations; at
N16875 q512 its 2-10 maximum is 0.62 times c6g's, outside the factor on the low side. This is the same pattern as dom90g
(G85 (c)): at that configuration both columns' 2-10 maximum is the lobe above P (4.27e-7 and 4.23e-7), which no column moves,
while c6g's is next to P. The lead's "A4 AGREE" is CONFIRMED on the lead's rows and on my N11250 and N22500 rows only.

Budget against domain. dom90g and dom300g carry the same further budget (20750 iterations from c6g at the same c_l, grid and
schedule) and differ in the domain only. Next to P: 0.32 to 0.33 (90 L) against 0.57 to 0.59 (300 L) times the candidate's;
857-label J 0.40 / 0.37 against 0.59 / 0.56; the strip left of P 0.41 against 0.67; the lobe above P 0.98 against 0.99. So in
the closed problems the near-P gain at that budget depends on the domain and grows as the domain shrinks. Whether the global
problem (rows to 900 L, inverse to 1000 L, formula beyond) gains at that budget is the question of step 45 (c6g2, the same
budget on the candidate's own domain); without it the budget part is not measured. Stated as data: at equal budget the
residual next to P of the closed 300 L problem is 0.58 of the candidate's, and that of the closed 90 L problem 0.33.

G20 (b1) for the candidate: both domain columns agree by A4 on the lead's rows; on my rows each falls below the factor 1.5 at
one configuration (N16875 q512), on the low side; no column is higher than the candidate by more than the factor anywhere
(largest ratio 1.23, dom90g 10-100 at N16875). The candidate's residual values are therefore not raised by the box; its
near-P value is not a floor of the basis in the closed problems. G20 (b1) is CONFIRMED in the one-sided sense ("no domain
column is worse by more than 1.5"), and NOT met in the two-sided sense of the 08:17Z text at N16875 q512. The report should
state the ratios and the side, not "agree", for that configuration.

Verdict G86: as above. The team may NOT finish (no endpoint; c6g2, dom9000g and c6gR4 pending).

G86 addendum (2026-10-18T19:04:45Z). Numerics NOTES_FOR_LEAD 18:40:12Z (dom90g exterior sensitivity by the ray method) against my evaluator.
My dom90g rows at N11250 q384 (G77; runs/audit/dom90g_N11250_q384_R7.652e6.log and _frm.log), N_v maxima (grid maxima, not
nodes): within 0.5 of P 6.03e-8 with the closure at 100 L, 9.42e-6 with the formula continued to 7.652e6 (ratio 156); within 2
of P 1.71e-7 / 1.67e-5; 10 <= r <= 100 4.8e-8 / 7.4e-5. The numerics' node values (closure residual 6.4e-8 within 0.5 of P;
impact 6.7e-6 there, 8.0e-6 at 0.5 to 2.5 from P, 6.3e-5 to 6.5e-5 at r 20 to 300) agree with these in order of magnitude, the
node maxima lying below the grid maxima as expected for 20 nodes. CONFIRMED in order of magnitude. In the suggested sentence,
"100 to 1000 times its interior residual in the closure convention" is correct if "interior residual" means the residual near P or the largest interior residual: 6.7e-6 / 6.4e-8 = 105 and 8.0e-6 / 3.7e-8 = 216 near P on their nodes, 6.5e-5 /
2.0e-7 = 325 at r 20 to 300 against my largest interior N_v (2 <= r <= 10). Against the local residual at r 20 to 300 (6e-10 to
2e-9 in their table) the factor is 3e4 to 1e5. Against the largest interior N_v (2.0e-7) the near-P impact is 34 times.
Suggested: "about 100 times its residual near P, and 30 to 300 times its largest interior residual (2e-7), in the closure
convention", or name the reference residual. My formula-convention maximum within 0.5 of P (N_f 3.1e-5, formula
to 7.652e6) agrees with the lead's 2.9e-5 (formula to 1000 L) in order, as the numerics state.

## G87 (2026-10-18T19:07:14Z). c6g baseline for 9000 L < r <= 1e4 L (step 44 reading (b)); data, no verdict

Method. scratch/j44.sh part 1: c6g in its own (formula) convention, k_self, R 7.652e6, VAUDIT_RBANDS 68862.82 < r <= 76514.25
(9000 L to 1e4 L, L of the stored file), N16875 q512 M639 and N22500 q384 M479; files runs/audit/c6g_N*_R7.652e6_rb44s.json.
Result (N_v maxima, N16875 q512 / N22500 q384): 9.680e-7 at r 6.925e4 (9050 L), theta 1.5683 / 9.644e-7 at r 6.892e4 (9008 L),
theta 1.5675; with A5 9.533e-7 / 9.609e-7. The rows below r = 1e4 L in these runs repeat the G80 values to the digits shown.
So on c6g the far N_v maximum decreases outward from about 4860 L: 1.10e-6 (1000 L to 9000 L), 9.7e-7 (9000 L to 1e4 L),
9.3e-7 (r > 1e4 L, at the inner edge), each within 0.003 of the y-axis.
Note on my logs. The "at r ... th ..." field printed by code/vaudit.py is the location of the flux maximum, not of the N_v
maximum; the N_v location is in the JSON (Nv_argmax_r, Nv_argmax_theta). G80's locations were taken from the JSON. For the
dom9000g reading the N_v locations are read from the JSON.
On the lead's proposed bracket (NOTES_FOR_TEAM 19:06:05Z, 18:53:42Z item 4): "changes the normalized residual by at most 7e-6
within 0.5 of P and 6.5e-5 at r 20 to 300, sampled maxima" is correct for the 52 nodes. On my grid (N11250 q384, every grid
point within 0.5 of P) the formula convention gives N_v 9.4e-6 there against 6.0e-8 with the closure, so the grid maximum of
the change is about 9e-6 (N_f 3.1e-5). The bracket should keep "sampled maxima", or read "about 7e-6 (9e-6 on the verifier's
grid)". CONFIRMED with that qualifier.

## G88 (2026-10-18T19:10:20Z). FINAL_REPORT diff 308eeb82 -> 88f0ae94 (lead NOTES_FOR_TEAM 19:06:05Z item 2); correction of G84 (d)

Method. Copies scratch/FR_308e.md (= lead/notes/FINAL_REPORT_308e.md, md5 308eeb82) and scratch/FR_88f0.md (=
lead/FINAL_REPORT.md, md5 88f0ae9430d91badac2769ca0bd5a16c); word diff by difflib (scratch/diff_308e_88f0.txt, 52
changed spans). Every changed span was read against G77, G84, G85, G86 and my logs.

(a) Domain columns (4.1, 4.4, timeline 17:35 and 19:03).
  - 90 L sentences and timeline 17:35: G85 a3 applied as suggested (two-sided; lead's 0.70 / 0.73 and 0.82; 0.62 at 16875 x
    512 on the low side; "0.40 times (eps 0.03; 0.37 at eps 0.01)"; the note on my first one-sided reading). CONFIRMED.
  - 300 L table row "0.99, 0.62, 0.74 | 0.89, 0.76 (cut 0.79), 0.96 | 5.1e-8, -3.1e-9 | 8.14e-7": G86. CONFIRMED.
  - "for the 300 L fit it is 3.9e-7 with the closure at 333 L and 4.9e-7 with the formula continued (11250 x 384 ...)": my
    |X-P| < 0.5 N_f maxima 3.860e-7 and 4.864e-7 (runs/audit/dom300g_N11250_q384_R7.652e6{,_frm}.log). CONFIRMED.
  - "(4.27e-7 and 4.23e-7)", "0.57 to 0.59", "J 0.59 (eps 0.03; 0.56 at eps 0.01)", "0.32 to 0.33 and 0.40", "the strip left of
    P 0.67 against 0.41, the lobe above P 0.99 against 0.98": G86 and G77 (strip 2.31e-7 / 5.56e-7 = 0.415). CONFIRMED.
  - "whether the full-plane problem gains at the same budget is measured by X3 continued on its own domain for the same
    iterations [OPEN]": correct as a statement of what is open (step 45).
  - 4.1 "(4.4: both agree except at one configuration, where each is lower by more than the rule's factor; neither is
    higher by more than that factor)": both exceptions are 16875 x 512 (0.62 and 0.624). CONFIRMED.
  - Timeline 19:03, "No domain column is higher than the candidate by more than the factor 1.5 anywhere (largest ratio
    1.23)": the 1.23 is dom90g 10-100 at 16875 x 512 (G77), the largest of the rule's ratios on both evaluators. "Anywhere"
    is too broad: outside the rule's bands the domain columns are much higher in their closure regions (dom90g N_v
    1.56e-2 on my 100 <= r <= 1000 row and 2.78e-2 beyond, the closure starting at r 765; dom300g N_v 5.1e-3 at 826 L on my 16875 x 512
    row, the closure starting at 333 L; on the lead's scan, which stops at R_shape, 2.37e-7 against 6.8e-8 at r 2550, its
    18:46:42Z item 2). Suggested: "in the bands of the rule" in place of "anywhere".
(b) 4.5 far paragraph.
  - "(1.05 to 1.08 at 5e5 L with c_l = 1/k)" together with the new sentence on the constant (c_l k - 1)/(1+k) = -5.2e-10:
    G85 a2 first item met. The "nine tenths" sentence is gone, the [OPEN] marker is replaced by the series text with the
    G84 (d) qualifications. CONFIRMED.
  - "So the band is the sum of a first-order and a second-order inconsistency of the trial's far field (...) and of the
    r^(-2) terms of 4.2 ...; all three decay at infinity": G84 (d) CONFIRMED this next to the axis. That was wrong, and I
    correct it here. G84 checked the two parentheses (1e-4 relative in Theta_1; 0.9 percent at second order) but not whether
    the terms listed make up the band. They do not. The third-order coefficient q3 = 1.190e5 (theta 1.568) is mostly the
    order-(3,0) residual itself (scratch/far2_parts.py on c6g, nt 65536): R3 / Theta_0 = +1.242e5, the sum of (c_l a_3 - 1)
    A_3 / Theta_0 = +5.589e5, U_0.grad A_(2,0) -4.286e5, U_1.grad A_(1,0) -6.01e3 and U_2.grad A_0 -61. That is 22 percent of
    the largest term it balances, so it is a third-order inconsistency and not an effect of the series division (which
    contributes 1.4e4 of q3). At theta 0.818 R3 / Theta_0 = -1.678e5, almost all from (c_l a_3 - 1) A_3. Next to the y-axis
    the four terms (q1 delta, q2 delta^2, qh r^-2, q3 delta^3) are:
        3000 L: +4.17e-6, -6.18e-6, +1.48e-6, +2.19e-6 (sum 1.66e-6)
        4700 L: +2.89e-6, -2.96e-6, +6.05e-7, +7.24e-7 (sum 1.26e-6)
        4858 L: +2.81e-6, -2.80e-6, +5.66e-7, +6.67e-7 (sum 1.24e-6; the band maximum, measured 1.10e-6)
        9500 L: +1.62e-6, -9.32e-7, +1.48e-7, +1.28e-7 (sum 9.65e-7)
    At the band maximum the first two orders cancel to 9e-9, and the band value is the r^-2 term plus the third-order term
    (plus higher orders: measured / series 0.89 there). So the sentence is REFUTED as written. Suggested: "So the band is the
    sum of inconsistencies of the trial's far field at first, second and third order (1e-4 relative in Theta_1; next to the
    y-axis, where the band maximum lies, 0.9 percent of the balancing terms at second order and 22 percent at third order)
    and of the r^(-2) terms of 4.2, which are fixed by k, L and the end values b_m(1), T(1), so that no choice of the end
    slopes removes them. Next to the y-axis the first two cancel at the band maximum (2.81e-6 and -2.80e-6 at 4860 L), where
    the r^(-2) and the third-order terms give 5.7e-7 and 6.7e-7 of the series sum 1.24e-6 (measured 1.10e-6); all four decay
    at infinity, the first-order one slowest." The third-order term involves the end derivatives of the radial splines up to
    order 3 (lam3, lam1 lam2, lam1^3), so the end-slope remark applies to the r^(-2) terms only, as written.
(c) Section 5 (new in the report, the v5 text 9793a69f): b2 "2 to 8 minutes each", b3 "about 7 seconds", b4 the X2 / F2
    note, b8 "(far1_ver.py, far2_ver.py, farP.py)" are present; the domain-column sentence of step 5 matches G85 b6/b7
    ("--fit-radius 90 or --fit-radius 300 ... fit radius / 0.9, with the two-term closure beyond"). CONFIRMED.
(d) Timeline 18:33 and 18:42 entries: "coefficients equal to the lead's to 7 digits in the leading one", "0.59, 0.87, 0.98",
    "to 2e-3 at 3e4 and 1e5 L", "confirmed subject to corrections ... all applied" (four items of section 5: b2, b3, b4, b8):
    CONFIRMED. The 18:33 entry says "the verifier confirmed the third-order series"; the series and its sums are confirmed,
    the decomposition sentence of 4.5 is not (b).

Verdict G88: the diff is CONFIRMED except two items: the 4.5 decomposition sentence (REFUTED as written; my G84 (d)
confirmation of it is withdrawn), and "anywhere" in the 19:03 timeline entry (too broad). The team may NOT finish (G86: the
budget control, step 45, and the 9000 L fit, step 44, are open).
(e) Scan of FINAL_REPORT 88f0ae94 for other uses of the decomposition (2026-10-18T19:16:21Z): the far-field statements of 4.1 (N_v maximum
    1.11e-6 beyond the inverse domain next to the y-axis at r about 3.7e4, that is 4836 L; my band maximum at 4858 L), of 4.2
    (remainder O(r^(2k-2)) uniformly in theta, the r^(-2) terms smaller since 2k - 2 = -1.64 > -2; first correction relative
    r^(k-1)) and the 18:04 to 18:25 timeline entries do not use the "first and second order" decomposition; only 4.5 lines
    903 to 906 of scratch/FR_88f0.md do. Nothing to add to the two items above.
(f) Build process of 88f0ae94 (2026-10-18T19:28:03Z): the lead's RUN_STATUS (19:06:13Z, RESUME_HERE item 1) builds the report with
    "python3 notes/port_report.py FR_new.md; cp FR_new.md FINAL_REPORT.md", and FR_new.md exists (111791 bytes,
    19:05:35Z, the size of FINAL_REPORT.md). The run instructions allow writes only inside the lane directory, so the build
    should write its temporary file inside the lead's lane (for example notes/FR_new.md). This does not affect the content.

## G89 (2026-10-18T19:35:14Z). fxd1g (chain 6 step 35, m <= 100, fixed c_l): the first row of the angular row fxd1g / s2g / c6g / c6h
Item: the angular row at fixed c_l (lead NOTES item 4 of the c6h request: whole-box N_f, near-P N_f (|X - P| < 0.5), N_v
for r <= 1000, N_v over r > 1000, 857-label J; "systematic improvement" = none of these increases from one row to the next
by more than the configuration spread). Method: my evaluator (code/gen_audit.sh, cfg {}, formula-global convention) on
N11250 q384 M 479 and N16875 q512 M 639, the 857-label J at N16875 q384, extra_checks (identity, h(P), D14, zeros) at N11250
q384; scratch/row_read.py fxd1g s2g c6g -c N11250_q384,N16875_q512.
(a) Run: "step 35 done" 19:23:16Z, outer 9 it 750 = 20750 iterations (equal to s2g, step 3, and c6g, step 31), objective
    1.6286e-5; md5 3334859a386607f210052e98b3ba50af (my copy matches). Start: fixc_c6d_m1.0e-03 (m <= 100), 20480 x 480. The
    rows share the last-segment budget of 20750 iterations, not the start: s2g continued fixc_c6f_m1.0e-03 (m <= 150), c6g
    continued the s2g end enriched to m <= 200, fxd1g continued fixc_c6d_m1.0e-03.
(b) Values (N11250 q384 / N16875 q512):
                         fxd1g (100)            s2g (150)              c6g (200)
    whole-box N_f        3.121e-6 / 3.113e-6    1.424e-6 / 1.435e-6    6.909e-7 / 6.841e-7
    near-P N_f           3.121e-6 / 3.113e-6    1.424e-6 / 1.435e-6    6.505e-7 / 6.841e-7
    N_v, r <= 1000       8.727e-7 / 8.738e-7    3.975e-7 / 4.005e-7    1.920e-7 / 1.917e-7
    N_v, r > 1000        1.325e-6 / 1.325e-6    1.102e-6 / 1.115e-6    1.090e-6 / 1.101e-6
    J (eps 0.03 / 0.01)  5.283e-6 / 5.484e-6    3.143e-6 / 3.462e-6    1.388e-6 / 1.602e-6
    (N_v r <= 1000 is the maximum over the five inner bands, without the y-axis column exclusion, as for s2g, whose audits
    predate that region.) The fxd1g whole-box maximum is next to P (flux argmax r 8.31 / 8.24, near-P band); its far N_v
    maximum is at 3323 / 3306 L, theta 1.5413, not next to the y-axis (c6g: 4858 L, theta 1.5683). q0 on the x-axis band
    (vq0band, max |q0|): 9.30e-6, 3.13e-6, 1.29e-6.
(c) Ratios row to row: 100 -> 150: whole-box and near-P N_f 0.456 / 0.461, N_v r <= 1000 0.456 / 0.458, N_v r > 1000 0.832 /
    0.841, J 0.595 / 0.631. 150 -> 200: 0.485 / 0.477 (near-P 0.457 / 0.477), 0.483 / 0.479, 0.989 / 0.988, J 0.442 / 0.463.
    Every quantity decreases at both steps and on both configurations; the configuration spreads are 1e-10 to 3.4e-8, far
    below every change except the far-field step 150 -> 200 (-1.3e-8 against spreads 1.2e-8: equal within the spread).
(d) fxd1g centre and consistency: identity c_l 5.5753626094 against 1/k = 5.5753626127 (-3.3e-9, as c6g's -3.2e-9); h(P) - 1
    +2.6e-7 (N11250 q384), +1.5e-8 (N16875 q512); c_l from h(P) = 1 differs from the identity value by -4.1e-8 (c6g +7.0e-9);
    D14 relative defects |E| <= 5.0e-8, |D2| <= 1.7e-8 (c6g <= 5.9e-9 and 5.1e-9); W_1 on the x-axis vanishes only at 8.6000582,
    W_2/y on the y-axis >= 5.57557, no open-quadrant cell with both components changing sign (sampled check).
Verdict G89: fxd1g's values CONFIRMED as listed; on the three rows measured (m <= 100, 150, 200) every quantity of the
reading decreases from row to row (far field 150 -> 200 within the configuration spread). The reading of the full row
waits for c6h (m <= 250, step 41), which my j41 audits at q512 / M 639 and q768 / M 959 because its density has sine modes up
to n = 503, above the M = 479 of the q384 grids (N11250 q384 is run for the table and marked). OPEN until then.
G89 addendum (2026-10-18T19:54:13Z): fxb1g (chain 6 step 36, 244 radial functions x m <= 100, fixed c_l), the radial companion of fxd1g
(375 x m <= 100). Run: "step 36 done" 19:42:55Z, outer 9 it 750 = 20750 iterations, start fxt_fixc_c6b_m1.0e-03_-1.0e-03
(md5 3083263a), 10240 x 480; md5 9e9a67abbe690118c532916075314c6d (my copy matches). Same method as G89; scratch/row_read.py
fxb1g fxd1g -c N11250_q384,N16875_q512.
                         fxb1g (244)            fxd1g (375)            fxd1g / fxb1g
    whole-box N_f        3.642e-6 / 3.743e-6    3.121e-6 / 3.113e-6    0.857 / 0.832
    near-P N_f           3.282e-6 / 3.269e-6    3.121e-6 / 3.113e-6    0.951 / 0.952
    N_v, r <= 1000       1.029e-6 / 1.057e-6    8.727e-7 / 8.738e-7    0.848 / 0.826
    N_v, r > 1000        1.311e-6 / 1.346e-6    1.325e-6 / 1.325e-6    1.011 / 0.985
    same, ya >= 0.006    1.245e-6 / 1.245e-6    1.325e-6 / 1.325e-6    1.064 / 1.064
    J (eps 0.03 / 0.01)  5.577e-6 / 6.040e-6    5.283e-6 / 5.484e-6    0.947 / 0.908
    fxb1g's whole-box maximum is not next to P: flux argmax r 8.73, theta 0.334 (the lobe above P; 10-100 band 2.52e-6 at r
    10.05, theta 0.67); fxd1g's is next to P (r 8.31 / 8.24, theta 0.017). fxb1g's far N_v maximum without the column exclusion
    is in the column next to the y-axis (4154 / 3921 L, theta 1.5675 / 1.5683; spread 3.5e-8 between configurations); with
    the exclusion it is 1.245e-6 at 3427 L, theta 1.5413, where fxd1g's maximum also lies (3323 / 3306 L), and there fxd1g is
    higher by 8.0e-8, far beyond both configuration spreads (9e-12, 1.1e-10). q0 max 9.20e-6 (fxd1g 9.30e-6). Identity c_l
    5.5753626091; h(P) - 1 -2.7e-8 / -6.9e-8; c_l from h(P) = 1 differs by +4.2e-8; D14 |E| <= 6.4e-8, |D2| <= 1.3e-8; W_1
    vanishes on the x-axis only at 8.6000581, W_2/y >= 5.57557.
Verdict: values CONFIRMED as listed. At m <= 100 the 375-function fit is lower than the 244-function fit in every quantity
of the reading except the far-field N_v: equal without the y-axis column exclusion (within fxb1g's spread), 6.4 percent
higher with it. No reading of this row has been fixed in advance (lead NOTES: "[TBD] 244 x m <= 100 row"); these are data.

## G90 (2026-10-18T20:03:33Z). FINAL_REPORT diffs 88f0ae94 -> fecb9d7f -> b025f900 -> 1f63bb44 (lead NOTES 19:34:02Z item 4, 19:40:30Z item 4, 19:58:50Z items 1-4)
Method. Copies scratch/FR_88f0.md, FR_fecb.md, FR_b025.md, FR_1f63.md (= lead/FINAL_REPORT.md, md5
1f63bb447f522fa69fc62aeaf6a32457, 19:58:35Z); line diffs scratch/diff_88f0_fecb.txt (19 lines), diff_fecb_b025.txt (37),
diff_b025_1f63.txt (44). Every changed statement read against G84, G88, G89 and its addendum, the audit JSONs (values to 7
digits from runs/audit/<tag>_<cfg>_R7.652e6.json), scratch/row_read.py, scratch/read_fit.py and scratch/far2_rel.py.
(a) 88f0 -> fecb.
  - Timeline 19:03, "in the bands of the rule (largest ratio 1.23)": G88 (a) as suggested. CONFIRMED.
  - Timeline 19:10 entry: two items, both corrected; G84 is dated 18:33:04Z, so "withdrew its 18:33 confirmation" is right;
    "carries, with the r^(-2) terms, the band maximum where the first two orders cancel" is G88 (b). CONFIRMED.
  - 4.5 decomposition: my G88 (b) text, with "the first two" written "the first- and second-order terms" (same meaning) and
    the last sentence made plural with "(at second and third order 0.88 to 0.92 percent and 22 to 23 percent next to the
    y-axis on six fits)". Six-fit check, my own code (scratch/far2_rel.py, which imports code/far2_ver.py; nt 32768, theta
    1.56811), relative orders |R_j| / max(|pure|, |velocity|) for j = 1, 2, 3 and the series sum at 4858 L:
        X3 9.595e-5 0.0088 0.2223 1.2421e-6;  F3 9.566e-5 0.0088 0.2215 1.2384e-6;  X2 9.681e-5 0.0089 0.2237 1.2576e-6;
        F2 9.630e-5 0.0088 0.2224 1.2505e-6;  X1 1.001e-4 0.0092 0.2330 1.2968e-6;  F0 9.821e-5 0.0090 0.2281 1.2721e-6.
    These equal the lead's work/far/far2_multi.json in every digit shown: 0.88 to 0.92 percent and 22.2 to 23.3 percent
    ("22 to 23"). CONFIRMED.
(b) fecb -> b025 (the m <= 100 row of G89).
  - 4.4 table row "375 x m <= 100  3.11e-6  8.74e-7  5.28e-6  2.6e-7, 1.5e-8" (16875 x 512: 3.1128e-6, 8.7382e-7; J 5.283e-6;
    h(P) - 1 +2.61e-7 at 11250, +1.46e-8 at 16875) and "c_l 2.1e-9 above X3's" (1/k 5.5753626127 against 5.5753626106,
    +2.05e-9): CONFIRMED.
  - 4.4 reading: the rule as fixed; 3.12e-6 / 3.11e-6, 6.91e-7 / 6.84e-7, 6.51e-7, 8.73e-7 / 8.74e-7, 3.98e-7, 1.92e-7,
    1.325e-6 / 1.325e-6, 1.09e-6 / 1.10e-6, J 5.28e-6, 3.14e-6, 1.39e-6; "0.46 to 0.63" (my ratios 0.456 to 0.631, far N_v
    excluded), "0.83 to 0.84" (0.832 / 0.841), "0.44 to 0.49" (0.442 to 0.485), "3.3e3 L, theta 1.541" and "4.9e3 L", the
    centre clause (3.3e-9, 2.6e-7 and 1.5e-8, 8.60006): CONFIRMED.
  - Three m <= 150 values are rounded up from my 4-digit G89 table and are 1 too high in the third digit. To 7 digits:
    whole-box N_f 1.434734e-6, N_v r <= 1000 4.004690e-7, N_v r > 1000 1.114685e-6 (s2g, 16875 x 512). Corrections: in the
    4.4 reading "1.42e-6 / 1.44e-6" -> "1.42e-6 / 1.43e-6", "3.98e-7 / 4.01e-7" -> "3.98e-7 / 4.00e-7", "1.10e-6 / 1.12e-6"
    -> "1.10e-6 / 1.11e-6"; in the timeline 19:35 entry "1.44e-6" -> "1.43e-6", "4.01e-7" -> "4.00e-7", "1.12e-6" ->
    "1.11e-6". The X2 table row's "4.01e-7" (unchanged in these diffs) is the same value and should read "4.00e-7"; its
    "1.435e-6" is right to 4 digits.
  - "-1.3e-8 (factor 0.99) against configuration spreads of 1.2e-8, equal within the spread" (4.4), "at the last step the
    N_v maximum beyond r = 1000 by less than the configuration spread" (4.1) and "by less than the configuration spread"
    (timeline 19:35). The decreases are 1.26e-8 (11250 x 384) and 1.33e-8 (16875 x 512); the spreads are 1.24e-8 (m <= 150)
    and 1.17e-8 (m <= 200). So the decrease is 1.0 to 1.1 times the larger spread, not less than it; "equal within the
    spread" was my G89 (c) wording and is loose in the same way (corrected here). The rule (no increase by more than the
    spread) is met either way. Suggested: 4.4 "which decreases by 1.26e-8 and 1.33e-8 (factor 0.99), about the
    configuration spreads (1.24e-8 and 1.17e-8)"; 4.1 and timeline 19:35 "by about the configuration spread".
  - 4.1 sentence otherwise (each quantity decreases, [OPEN: and the m <= 250 refinement row]): CONFIRMED.
(c) b025 -> 1f63 (the 244 x m <= 100 row of the G89 addendum).
  - 4.4 table row "244 x m <= 100  3.74e-6  1.06e-6  5.58e-6  -2.7e-8, -6.9e-8": 3.742666e-6, 1.057496e-6, J 5.577e-6;
    h(P) - 1 -2.69e-8 at 11250 x 384 and -6.88e-8 at 16875 x 512, in the order of the column header (lead's check request,
    19:58:50Z item 2). CONFIRMED.
  - 4.4 reading: "0.83 to 0.86" (0.832 / 0.857), "0.95" next to P (0.951 / 0.952), "0.83 to 0.85" (0.826 / 0.848), J "0.95
    (0.91 at eps 0.01)" (0.947, 0.908), "1.31e-6 and 1.35e-6 at 244, 1.325e-6 at 375, the maximum at 244 in the column next
    to the y-axis", "6.4 percent higher at 375 (1.325e-6 against 1.245e-6)". Check request (i): my region ya >= 0.006 is
    (pi/2 - theta) >= 0.006 on the evaluation columns (code/vaudit.py line 45), so the excluded columns are pi/2 - theta <
    0.006 as written. (ii): fxb1g 3427 L, fxd1g 3323 / 3306 L, theta 1.5413 for both: "3.3e3 to 3.4e3 L, theta 1.541" is
    right. "No reading of this pair was fixed before its run; these are data": as G89 addendum. CONFIRMED.
  - Timeline 19:54 entry (same numbers, "reported as data"): CONFIRMED.
  - The sentence below the table, "The m <= 100 row is a fixed-c_l fit of its own basis ... (c_l 2.1e-9 above X3's)", now
    has two m <= 100 rows. Suggested: "The m <= 100 rows are fixed-c_l fits of their own bases continued for 20750
    iterations, as X2 is on its basis (c_l 2.1e-9 above X3's at 375 and 1.7e-9 at 244)"; fxb1g 1/k 5.5753626123, +1.70e-9.
Verdict G90: the three diffs are CONFIRMED except (1) three third-digit roundings of m <= 150 values (4.4 reading, timeline
19:35, and the X2 table row's N_v), (2) "less than" / "equal within" the spread for the far-field step 150 -> 200, which is
a decrease of about the spread (my G89 (c) wording corrected), and (3) the singular m <= 100 sentence under the table.
None of these changes a verdict or the rule's outcome. The team may NOT finish: step 45 (budget control, G86), step 44
(9000 L fit) and the m <= 250 row (step 41) are open.

## G91 (2026-10-18T20:44:09Z). dom9000g (chain 7 step 44, fit rows to 9000 L, R_shape 1e4 L, fixed c_l): reading by lead NOTES 17:42:41Z (44) and 18:04:24Z item 4
Run: "step 44 done" 20:21:48Z, outer 9 it 750 = 20750 iterations, objective 1.33439e-6 on its rows (r < 9000 L); md5
269865efab75bc778dab2a4407f7feba (my copy matches). Start: c6g end (md5 15f8095f), 24576 x 960. Shape: R_shape 1e4, angular 200,
1/k 5.5753626106 (= c6g), L 7.6514243163 (c6g 7.6514246014, relative -3.7e-8).
Method: my evaluator in dom9000g's own convention (fit convention: two-term closure at R_shape = 1e4 L, 3375 radii replaced at
N 16875; VAUDIT_RFIT 9000 L; k_self) at N11250 q384 M 479, N16875 q512 M 639, N22500 q384 M 479, with band regions 1000 L-9000 L,
9000 L-1e4 L, r > 1e4 L; the formula-continued reading (no closure, suffix _frm44) at N16875 q512 and N22500 q384; BA5 at N16875
q512; the 857-label J with the closure at N16875 q384 (scratch/jr_one.sh); vaxis; extra_checks (N11250 q384, formula convention);
the residual map near P (closure, N16875 q512); code/far1_ver.py and code/far2_ver.py. c6g baselines: c6g_<cfg>_R7.652e6.json,
_rb44 and _rb44s (bands, G80 / G87), c6g512 map, runs/far1/c6g_nt16384.json. Reading: scratch/read_fit.py dom9000g c6g "" "" _clo
"" and with _frm44 _rb44; scratch/cmp_resmap.py c6g512 dom9000g512.
(a) Interior, A4 read two-sided (ratios dom9000g / c6g):
        config         2-10 N_f max             10-100 N_f max                       h(P) - 1 (c6g)
        11250 x 384    7.046e-7 / 6.909e-7 1.020 in   1.117e-7 / 1.368e-7 0.817 in       +3.4e-7 (+2.8e-7; N < 16875, not in the rule)
        16875 x 512    4.485e-7 / 6.841e-7 0.656 LOW  3.742e-7 / 2.644e-7 1.415 in        +4.8e-8 (+3.1e-8)
        22500 x 384    4.912e-7 / 6.605e-7 0.744 in   1.945e-7 / 1.954e-7 0.996 in        -5.0e-9 (-1.8e-8)
    At 16875 x 512 the raw 10-100 maximum is in the column next to the y-axis (r 10, theta 1.5683); with the columns pi/2 - theta
    < 0.006 excluded it is 9.087e-8 against c6g's 8.659e-8 (1.049). So A4 holds except at 16875 x 512, where the 2-10 maximum is
    lower than c6g's by more than the factor (0.656 < 0.667), the same pattern as the 90 L and 300 L columns (0.62 there; G77, G86);
    |h(P) - 1| < 1e-7 on both N >= 16875 configurations. The 2-10 maximum lies next to P at 16875 x 512 (r 8.458, theta 0.0074) and
    in the lobe above P at the q384 configurations (r 8.78, theta 0.308; r 8.74, theta 0.193).
    Near-P N_f (|X - P| < 0.5): 4.451e-7 / 4.485e-7 / 4.512e-7 against 6.505e-7 / 6.841e-7 / 6.605e-7, ratios 0.684 / 0.656 / 0.683.
    857-label J: 9.106e-7 / 1.0199e-6 (eps 0.03 / 0.01) against 1.3882e-6 / 1.6019e-6, ratios 0.656 / 0.637.
    N_v for r <= 1000 (five inner bands): 1.958e-7 / 1.256e-7 / 1.435e-7 against 1.920e-7 / 1.917e-7 / 1.850e-7 (1.020 / 0.655 / 0.776).
    Map near P (16875 x 512): |X - P| < 0.5 4.49e-7 against 6.84e-7; window y >= 1 4.30e-7 against 4.32e-7 (1.00). The fall is next
    to P; the lobe above P is unchanged.
    Centre: identity c_l 5.5753626108 (1/k 5.5753626106; c6g -3.2e-9); c_l from h(P) = 1 differs by -1.8e-8; D14 |E| <= 6.7e-9,
    |D2| <= 3.2e-9; W_1 on the x-axis vanishes only at 8.6000642; W_2/y >= 5.57557 on the y-axis; no open-quadrant cell with both
    components changing sign (sampled); vaxis x* 8.6000645 (c6g 8.6000638). BA5 inverse check per band on r <= 1000 as c6g's
    (relsup 1.1e-11, 8.6e-10, 6.8e-8, 2.9e-8, 1.2e-8 against 1.1e-11, 9.7e-10, 6.9e-8, 2.9e-8, 1.6e-8).
(b) Far bands, N_v maxima (16875 x 512 / 22500 x 384):
                        dom9000g own convention   dom9000g formula continued   c6g (formula-global)     ratios own; formula
        1000 L-9000 L   3.202e-8 / 3.038e-8       3.199e-8 / 3.035e-8          1.1018e-6 / 1.0937e-6    0.029 / 0.028; 0.029 / 0.028
        9000 L-1e4 L    2.401e-8 / 2.411e-8       2.407e-8 / 2.412e-8          9.680e-7 / 9.644e-7      0.025 / 0.025; 0.025 / 0.025
        r > 1e4 L       2.307e-5 / 2.302e-5       3.281e-8 / 3.284e-8          9.338e-7 / 9.279e-7      24.7 / 24.8; 0.035 / 0.035
    Locations: dom9000g 1000 L-9000 L at 1013 / 1026 L (theta 1.5634, the first column outside the cut / 1.5479), 9000 L-1e4 L at
    9984 / 9968 L (theta 0.6185); r > 1e4 L own convention at 2.32e4 / 2.35e4 L next to the y-axis, in the closure; formula
    continued at 2.16e4 / 2.17e4 L, theta 0.6185. c6g: 4858 / 4830 L and 1.001e4 L, next to the y-axis. With the column exclusion
    the dom9000g values are the same except r > 1e4 L own (2.257e-5 / 2.269e-5); c6g's 1.075e-6 / 1.086e-6 (1000 L-9000 L).
    Whole box, formula reading: N_f 4.485e-7 / 4.912e-7 (0.656 / 0.744 of c6g), N_v 1.256e-7 / 1.435e-7 (0.114 / 0.131), maxima in
    the interior. Own convention: whole-box maxima in the closure region (N_f 1.233e-6 / 1.231e-6, N_v 2.31e-5 / 2.30e-5).
    Reading: 1000 L < r <= 9000 L FALLS (0.028 to 0.029 on both N >= 16875 configurations). r > 1e4 L DOES NOT FALL in dom9000g's own
    convention (24.7 / 24.8): there the two-term closure has N_v 2.3e-5, 25 times c6g's formula. In the formula-continued reading
    it falls (0.035 / 0.035).
(c) C at the axis (code/far1_ver.py, nt 16384): +6.465e-4 against c6g's +1.86871e-2 (0.035 of it). V_r(pi/2) 89.33394 (c6g
    89.33392), so the forced Theta_1 is unchanged and the stored Theta_1 moved onto it; off the axis max |forced - stored| on 0.05 <
    theta < 1.4 is 4.6e-4 at 0.603 (c6g 7.9e-4 at 1.400). So the condition of 18:04:24Z item 4 ("C at the axis within 10 percent of
    c6g's") does not hold: the fit to 9000 L removed most of the first-order inconsistency on the axis. Higher orders (code/far2_ver.py,
    nt 32768, theta 1.56811; runs/far2/dom9000g_rel.txt, dom9000g_far2.json): q1 4.94e-4 (c6g 1.582e-2), q2 -14.65 (-88.78), qh 782.10
    (782.10; fixed by k, L and the end values), q3 -3.46e4 (+1.190e5); relative inconsistencies at orders 1, 2, 3: 3.0e-6, 0.15
    percent, 10 percent (c6g 9.6e-5, 0.88 percent, 22 percent). No prediction of r > 1e4 L from C was fixed and none is made here.
Consequences for the report: (1) 4.5's "The inconsistencies are common to the fits measured (... on six fits)" holds for fits
with rows to 900 L only; on the 9000 L fit the second- and third-order ones next to the y-axis are 0.15 and 10 percent and C at
the axis is 29 times smaller, so the 900 L fits' band value is not a floor of the family (the sentence's last clause allows
this). (2) dom9000g is c6g + 20750 iterations, so the interior falls (near-P 0.66 to 0.68, J 0.64 to 0.66) may be budget, not
domain; c6g2 (step 45, the control) decides. (3) Not a candidate (lead 17:42:41Z (44)).
Verdict G91: values CONFIRMED as listed (my evaluator). Readings: (a) A4 holds except at 16875 x 512 on the low side (0.656);
(b) 1000 L-9000 L falls (0.028 to 0.029); r > 1e4 L does not fall in the own convention (closure, 25 times higher) and falls in
the formula-continued reading (0.035); C at the axis 0.035 of c6g's. The team may NOT finish: c6g2 (45) and c6h (41) are open.
G91 addendum (2026-10-18T20:45:09Z): the closure region across the three domain fits (own convention, 16875 x 512, my JSONs, maximum of N_v
beyond R_shape): dom90g 2.783e-2 at 266.6 L (2.67 R_shape, R_shape 100 L), dom300g 5.091e-3 at 826.4 L (2.48 R_shape, 333 L),
dom9000g 2.307e-5 at 2.324e4 L (2.32 R_shape, 1e4 L), each next to the y-axis (theta 1.5683). Log-slopes in R_shape: -1.41 (100 L
to 333 L) and -1.59 (333 L to 1e4 L), against 2 - 2k = 1.64. Data only: I have not derived the error of the two-term closure, and
the first-order term C r^(k-1) / (1+k) alone is far smaller there (about 3e-5 at 266.6 L for C = 0.0187), so these values are
not explained by C.

## G92 (2026-10-18T20:54:00Z). FINAL_REPORT 3b0d8888 against 1f63bb44; the lead's dom9000g numbers (NOTES 20:28:25Z, 20:39:59Z) against G91 and new rows
(A) FINAL_REPORT md5 3b0d888847bd734d8108febaca203de5 (mtime 2026-10-18T20:04:38Z; copy scratch/FR_3b0d.md, diff
scratch/diff_1f63_3b0d.txt, 51 lines). Every G90 correction is applied: the m <= 150 values 1.43e-6, 4.00e-7, 1.11e-6 in 4.1, 4.4,
the X2 rows of the 4.4 table and the near-P line; "by about the configuration spread" in 4.1 and in the summary list; the 4.4
reading "decreases by 1.26e-8 and 1.33e-8 (factor 0.99), about the configuration spreads (1.24e-8 and 1.17e-8)"; "The m <= 100
rows are ... (c_l 2.1e-9 above X3's at 375 and 1.7e-9 at 244)"; "The 375 x m <= 100 fit has the same centre structure". The new
timeline entry 20:03 describes G90 correctly (G90 is 20:03:33Z; three items, all corrected). No other change; no dom9000g text
yet. CONFIRMED.
(B) Lead numbers on dom9000g.
 1. The verifier rows requested in 20:28:25Z item 5 ((i) A4 with A5, near-P, J; (ii) far bands with location and A5 in both
    conventions; (iii) far2_ver) are in G91 (a), (b), (c); dom9000g's own N_v for r <= 1000 (20:39:59Z item 3) is in G91 (a):
    1.958e-7 / 1.256e-7 / 1.435e-7 (11250 x 384 / 16875 x 512 / 22500 x 384).
 2. Interior scans (20:28:25Z item 2): the same pattern as mine (lead 2-10 ratios 0.72 / 0.65; mine 1.020 / 0.656 / 0.744). The
    10-100 ratio differs (lead 0.97 on both; mine 1.415 raw at 16875 x 512, where the maximum is in the column next to the axis,
    1.049 with that column excluded, 0.996 at 22500 x 384); within the rule on both. The case fixed in item 4 applies on my rows:
    2-10 below 1/1.5 at one N >= 16875 configuration (0.656 at 16875 x 512, lower), 10-100 and h(P) within the rule, so 4.5 states
    the far-band fall with the measured interior ratios as data and without "the interior is preserved". CONFIRMED.
 3. Centre coefficients (item 2): on my extra_checks (11250 x 384) alpha -0.1008765066 / -0.1008765104, beta -0.2324568268 /
    -0.2324568229, gamma -0.0118391593 / -0.0118391598, delta -0.0114502571 / -0.0114502569 (dom9000g / c6g): equal to 3.9e-9,
    CONFIRMED for these four. Mine also: c 15.7260878324 / 15.7260878221 (1.0e-8), A 10.150725222 / 10.150725215 (7e-9),
    beta - alpha 7.7e-9; I do not know which quantity the lead's "moment" is, so that word is not checked.
 4. C at the axis (item 3): lead -1.4129e-4 against c6g -4.0843e-3; mine +6.465e-4 against +1.86871e-2. The two conventions
    differ by the factor -(c_l - 1) = -4.57536 (6.465e-4 / 4.57536 = 1.4130e-4, 1.86871e-2 / 4.57536 = 4.0843e-3), so they
    agree; factor 0.0346 in both. Relative to Theta_1(pi/2): 1.4129e-4 / 42.55 = 3.3e-6. CONFIRMED.
 5. Series coefficients, relative inconsistencies (item 3): CONFIRMED in G91 (c). Series terms at 4858 L, theta 1.56811, from
    my runs/far2/dom9000g_far2.json: +8.772e-8, -4.623e-7, +5.661e-7, -1.940e-7, sum -2.48e-9; at 1000 L sum -2.009e-6.
    CONFIRMED (the leading term no longer dominates at 4858 L).
 6. ptest (item 3), my evaluator: scratch/farP.py (formula continued, k_self) on dom9000g at N16875 q512 M639 R 1e6 L and N20250
    q512 M639 R 1e8 L, then scratch/farS.py (signed R / N_v against my series at the same columns; runs/far2/farS_dom9000g_R1e6.json,
    _R1e8.json):
    - column 0.8173: measured / series at 3e4 L 1.008 / 1.004, 1e5 L 1.016 / 0.997, 3e5 L 1.030 / 0.982 (R 1e6 L / R 1e8 L
      boxes), 5e5 L 1.021, 1e6 L 1.035, 3e6 L 0.966 (R 1e8 L); measured 2.466e-8 / 2.455e-8 at 3e4 L (lead +2.5e-8). CONFIRMED to
      4 percent.
    - columns 1.56098, 1.56343, 1.56589, 1.56834 (the four next to the axis at q512): measured 1e-9 to 1.4e-8, with a node-to-node
      scatter of the same order. In the R 1e8 L box the centre-node ratios are 0.94 to 1.10 at 3e4 L and 0.61 to 1.08 at 1e5 L,
      but the 11-node windows span about 0.3 to 2.2, and from 3e5 L out the measured value changes sign within the window. So on
      my evaluator the series is resolved next to the y-axis only to the order of magnitude (resolution floor about 1e-9 to 2e-9
      in R / N_v there). The lead's "measured / series 0.99 to 1.00 for r >= 3e4 L on all four columns" is CONFIRMED on 0.818
      and OPEN on the near-axis columns (not contradicted at the centre nodes out to 1e5 L). Lead values at 1.56807 against
      mine at 1.56834 (R 1e6 L / R 1e8 L): 1000 L 8.2e-9 / +1.13e-8; 4699 L 2.9e-9 / +2.57e-9; 9500 L 7.4e-9 / +3.66e-9, +9.10e-9;
      3.0e4 L 8.9e-9 / +1.26e-8, +8.83e-9; 1e5 L 5.3e-9 / +9.42e-9, +4.76e-9; same order to 1e5 L, beyond that mine is at the floor.
    - 1000 L: measured -3.1e-8 to +1.1e-8 against series -2.0e-6 on the near-axis columns (ratios 0.006 to 0.015). CONFIRMED:
      the series is not an approximation there.
 7. band_nv (20:39:59Z item 2) against G91 (b) (16875 x 512 / 22500 x 384, formula continued): 1000 L-9000 L 3.133e-8 against
    3.199e-8 / 3.035e-8; 9000 L-1e4 L 2.375e-8 / 2.378e-8 against 2.407e-8 / 2.412e-8; r > 1e4 L 3.245e-8 at 2.18e4 L, theta 0.603
    against 3.281e-8 / 3.284e-8 at 2.16e4 / 2.17e4 L, theta 0.6185. Values agree to 3 percent; the c6g baselines agree (item 1 of
    the note against G80). "The same with and without A5": CONFIRMED (my A5 values equal the raw ones on all three bands, formula
    reading). Two wording points for 4.5:
    - "they are no longer next to the y-axis" is right in the A5 sense (no maximum in the excluded columns). The 1000 L-9000 L
      maximum is still at the inner edge within 0.05 rad of the axis (theta 1.5634 / 1.5479 on mine, pi/2 - theta = 0.007 / 0.023;
      1.524 on the lead's), so "outside the columns next to the axis" is accurate and "away from the axis" is not.
    - "falls ... by a factor about 30 to 40 in both conventions": my factors are 34 / 36 (1000 L-9000 L), 40 / 40 (9000 L-1e4 L) in
      both conventions and 28 / 28 (r > 1e4 L) in the formula reading only. Beyond 1e4 L the own convention does not fall (24.7 /
      24.8 times c6g, the closure; G91 (b)), and the lead's tool has no own-convention value there, so "both conventions" must
      be limited to the two bands inside 1e4 L.
 8. Step 48 (20:41:00Z): reading fixed before the result, noted. My task set scratch/j48.sh is armed (as j44, plus far2_ver,
    far2_rel and extra_checks). F3 far-field baseline on my tools (c6gF_shape.npz, md5 0398af3f): C at the axis +1.86404e-2,
    V_r(pi/2) 89.36522; q1 +1.5779e-2, q2 -88.589, qh 782.40, q3 +1.1854e5 at theta 1.56811; relative inconsistencies 9.57e-5,
    0.88 percent, 22 percent (runs/far2/c6gF_rel.txt, c6gF_far2.json); band baseline _rb48 running.
Verdict G92: (A) CONFIRMED. (B) values CONFIRMED except the near-axis ptest agreement (OPEN on my evaluator, resolution) and
two wording limits for 4.5 (item 7). The team may NOT finish: c6g2 (45) and c6h (41) are open.
G92 addendum (2026-10-18T20:56:19Z): lead notes/analysis.md 14.11 (20:29:16Z, mtime 20:29:21Z), audited against my code/far2_ver.py
output (runs/far2/dom9000g_far2.json) and G91 / G92.
- Coefficients at theta 1.56811 and the factors 0.031 (q1), 0.165 (q2): CONFIRMED. At theta 0.818 (mine at 0.81819): q1 +1.4410e-3,
  q2 -44.543, qh 2388.5, q3 -1.1201e5 against the lead's +1.440e-3, -44.55, 2388.9, -1.120e5: CONFIRMED (qh to 2e-4, the column
  offset).
- Series table next to the axis (mine, orders 1, 2, r^-2, 3, sum): 4701 L +9.01e-8 -4.879e-7 +6.045e-7 -2.103e-7, -3.59e-9;
  9503 L +5.06e-8 -1.537e-7 +1.479e-7 -3.72e-8, +7.64e-9; 1e5 L +7.33e-9 -3.23e-9 +1.34e-9 -1.1e-10, +5.33e-9; 5e5 L +1.96e-9
  -2.30e-10 +5.3e-11 -2e-12, +1.78e-9. CONFIRMED to the digits given.
- C at the axis, relative inconsistencies: CONFIRMED (G92 (B) 4, 5). "Measured / series 0.99 to 1.00 for r >= 3e4 L on the four
  columns": CONFIRMED on theta 0.818 (0.97 to 1.04 on mine), OPEN on the near-axis columns (G92 (B) 6).
- "The r^-2 term is unchanged": CONFIRMED (qh 782.10 on both; L moves by -3.7e-8 relative).
- Reading [numerical]: "rows reaching 9000 L lower the first-order coefficient on the axis about 30-fold" is right as a
  measurement of dom9000g against c6g (q1 factor 32, C factor 29). The attribution to the rows assumes the 20750 extra
  iterations alone (rows to 900 L) do not lower C; that is untested until c6g2 (step 45, same budget, same rows as c6g) has
  its C at the axis (my j45 runs far1_ver on it). Until then the sentence should read "dom9000g (rows to 9000 L, c6g + 20750
  iterations) has a first-order coefficient about 30 times smaller", with the attribution to rows OPEN. "Consistent with end
  slopes that rows ending at 900 L constrain only weakly" is a labelled heuristic; not checked.

## G93 (2026-10-18T21:02:26Z). FINAL_REPORT f66fa76b against 3b0d8888 (lead NOTES 20:54:14Z item 2, 20:56:36Z); F3 band baselines; data of the X3 fit-convention ray check
(A) FINAL_REPORT md5 f66fa76b3542c8c698eed9903d5c409e (mtime 2026-10-18T20:56:29Z; copy scratch/FR_f66f.md, diff
scratch/diff_3b0d_f66f.txt, 205 lines). Checked against G91, G92 and the lead's list.
 1. 4.1 N_v sentence ("where the candidate has no fit rows; a domain row fitted to 9000 L reads 0.03 of it there, 4.5"): CONFIRMED
    (0.029 / 0.028 rounded). "there" means the band 1000 L-9000 L: X3's maximum is at 4858 L (r 3.72e4), dom9000g's at 1013 L.
    Optional: "over 1000 L to 9000 L" instead of "there".
 2. 4.1 domain sentence ("all three agree except at one configuration, where each is lower by more than the rule's factor; none is
    higher by more than that factor"): CONFIRMED. The configuration is 16875 x 512 for all three (2-10 ratios 0.62, 0.62, 0.656);
    the largest ratio of dom9000g is 1.415 (10-100, raw), inside 1.5.
 3. 4.4 caption ("100 L, 333 L or 1e4 L beyond the fit radius") and the row "9000 L  1.02, 0.66, 0.74 | 0.82, 1.42 (cut 1.05), 1.00
    | 4.8e-8, -5.0e-9 | 9.11e-7" with its note: CONFIRMED against G91 (a) (1.020 / 0.656 / 0.744; 0.817 / 1.415 (1.049) / 0.996;
    +4.8e-8 / -5.0e-9; J 9.106e-7).
 4. 4.4 domain paragraph (9000 L sentence): CONFIRMED (2-10 maximum next to P at 16875 x 512, r 8.458, theta 0.0074; near-P 0.66 to
    0.68; J 0.656 / 0.637; N_v r <= 1000 1.020 / 0.655 / 0.776; lobe 1.00). "the near-P gain at that budget grows as the domain
    shrinks": near-P 0.66-0.68 / 0.57-0.59 / 0.32-0.33 and J 0.66 / 0.59 / 0.40 for 9000 L / 300 L / 90 L, monotone; all three at
    20750 further iterations. CONFIRMED. The comparison with X3 still mixes budget and domain; the text keeps that [OPEN] (c6g2).
 5. 4.5 band text: every number CONFIRMED against G91 (b) and the G91 addendum (3.20e-8 / 3.04e-8, 0.029 / 0.028, 1013 L / 1026 L,
    theta 1.563 / 1.548; 2.40e-8 / 2.41e-8, 0.025, theta 0.62; own closure 2.3e-5 at 2.3e4 L; 5.1e-3 and 2.8e-2 for the 300 L and
    90 L closure regions; formula 3.28e-8, 0.035, 2.2e4 L, theta 0.62; whole-box N_v 1.256e-7 / 1.435e-7; interior ratios).
    "fitting to 9000 L lowers it over 1000 L to 9000 L by the factor 0.028 to 0.029": CONFIRMED as a description of the operation
    (rows to 9000 L together with 20750 iterations). Which of the two produces the fall is not claimed and is OPEN until c6g2's
    bands (j45, suffix _rb45) are read; any sentence that attributes it to the rows waits for that.
 6. 4.5 far-field paragraph: CONFIRMED (C 6.465e-4, 0.035; V_r(pi/2) 89.33394 against 89.33392; 3.0e-6, 0.15 percent, 10 percent;
    qh 782.10 on both). "the formula's Theta_1 moved onto the forced one" is exact to the stated factor only: on the axis the stored
    Theta_1 moved to within 0.035 of X3's difference (optional: "toward"). "So the 900 L fits' band value is not a floor of the
    family" CONFIRMED: dom9000g has X3's basis and reads 3.0e-8 to 3.2e-8 there, whatever the cause.
 7. 4.8 ("3.0e-8 to 3.2e-8 over 1000 L to 9000 L"): CONFIRMED.
 8. Section 5: (c) "on seven fits and on the domain fit with rows to 9000 L" and step 5 ("--nt 960 on a 24576-point radial grid
    with --fit-radius 9000") match the run (24576 x 960, fit radius 9000 L, inverse and closure at 1e4 L). Step 7: work/far/band_nv.py
    exists (mtime 20:34:31Z) with outputs band_nv_c6g_R1e6.json, band_nv_dom9000g_R1e6.json, band_nv_dom9000g_own.json (values
    against mine in G92 item 7); run time and memory not checked.
 9. Timeline 20:44: the first five sentences CONFIRMED (0.66; 0.028 to 0.029; 0.035 formula, 25 times in the own closure). The
    sentence "The first-order mismatch coefficient at the y-axis is 0.035 of the candidate's, so the fall is removal of most of the
    first-order inconsistency, not a balancing of higher orders over the longer fit range." REFUTED as an explanation of the fall.
    (i) Logic: the reading fixed at 18:04:24Z item 4 was one-sided ("If the band falls while C at the axis is within 10 percent of
        c6g's, the fall is the rows balancing higher orders"). That its condition fails does not establish the opposite.
    (ii) Series (lead far2 coefficients, confirmed in G91 (c) and G92 item 5; theta 1.568): on X3 at its band maximum (4860 L) the
        first- and second-order terms nearly cancel (+2.81e-6, -2.80e-6), and the band value comes from the r^(-2) and third-order
        terms (5.7e-7, 6.7e-7; sum 1.24e-6). Removing the first-order term alone, with X3's other coefficients, would leave
        -2.80e-6 + 5.7e-7 + 6.7e-7 = -1.56e-6, larger in size than X3's value. On dom9000g q2 is 0.165 of X3's (-14.65 against
        -88.78) and q3 has the opposite sign (-3.46e4 against +1.190e5); at 4858 L its four terms are +8.77e-8, -4.62e-7, +5.66e-7,
        -1.94e-7, sum -2.5e-9, which is 35 times smaller than its own first-order term. The series value there is a cancellation
        among the orders 2, r^(-2) and 3.
    (iii) Measured (my evaluator, scratch/farP.py, dom9000g, 16875 x 512, formula continued to 7.652e6; runs/farP/
        dom9000g_N16875_q512_R7.652e6.json): at 1000 L on the six columns theta 1.4996 to 1.5683, R / N_v is -3.1e-8 to +1.1e-8,
        which is -0.13 to +0.035 times the first-order term C(theta) r^(k-1) / (1+k) on the same columns (+2.3e-7 to +3.3e-7),
        with the opposite sign on five of the six; at 4701 L it is -1.9e-8 to +2.6e-9, ratios -0.30 to +0.15 over the 11-node
        windows. Except the column 1.56834 at 4701 L (+2.6e-9, inside the A5 cut) these values are above the resolution floor of
        about 1e-9 to 2e-9 (G92 item 6) by factors 2.5 to 30. So dom9000g's band maximum
        (3.2e-8 at 1013 L) is about a tenth of its own first-order term and is set by the higher orders.
    The fall over 1000 L-9000 L therefore comes with changes at the first, second and third orders; the fall of C alone would not
    produce it. Suggested wording: "The first-order mismatch coefficient at the y-axis is 0.035 of the candidate's, and the second-
    and third-order coefficients changed with it (0.17 of the candidate's, and of the opposite sign); the fall is not the removal of
    the first-order term alone." The last timeline sentence ("The candidate's far-band value is therefore that of the unfitted
    continuation of its formula.") is CONFIRMED.
(B) F3 band baselines for step 48 (my evaluator, c6gF formula-global, k_self, VAUDIT_RBANDS at 1000 L, 9000 L, 1e4 L of F3's L
7.6520572; runs/audit/c6gF_<cfg>_R7.652e6_rb48.json; raw / with A5; 16875 x 512 ; 22500 x 384):
        1000 L-9000 L   1.0981e-6 at 4587 L, theta 1.5683 / 1.0703e-6 at 4785 L, theta 1.5585 ; 1.0908e-6 at 4900 L / 1.0814e-6 at 4805 L
        9000 L-1e4 L    9.651e-7 at 9050 L / 9.486e-7 at 9001 L                              ; 9.607e-7 / 9.564e-7 at 9008 L
        r > 1e4 L       9.264e-7 at 1.001e4 L / 9.125e-7                                    ; 9.229e-7 / 9.205e-7 at 1.002e4 L
    All next to the y-axis; within 1 percent of c6g's (1.1018e-6 / 1.0937e-6, 9.680e-7 / 9.644e-7, 9.338e-7 / 9.279e-7). Interior
    of the same JSONs: whole-box N_f 7.302e-7 / 7.062e-7 next to P (r 8.53, theta 0.007 / 0.016), N_v r <= 1000 2.046e-7 / 1.979e-7.
(C) X3 fit-convention ray check of the numerics lane (../numerics/runs/ray/x3_c6g_fit_BP.json, mtime 20:57:02Z; export c6gfx, c_l
5.5753626106; 52 nodes; their note not yet posted). My summary by region from the file (max over nodes; impact = their
frozen-gradient change normalized by the exported D_v): within 0.5 of P max |dU| 9.2e-8, impact 2.0e-9; 0.5 to 2.5 from P 1.0e-7,
3.1e-9; r about 0.1 / 1 / 20 / 100 / 300: impact 5.2e-10 / 5.3e-10 / 1.4e-8 / 1.4e-8 / 1.4e-8. The canonical export (x3_c6g_BP.json,
c6gx) gives 8.6e-10 / 2.6e-9 / 1.3e-11 / 1.6e-12 / 7.0e-11 / 6.8e-11 / 6.8e-11. So the fit-convention velocity changes the D_v-
normalized residual by at most about 2e-9 near P and 1.4e-8 at r 20 to 300, the same size as my X1 closure row (G69: 1.5e-9 N_v within
0.5 of P, 1.6e-8 N_v for r <= 300). My own X3 closure row (code/clo_diff.py on c6g, 11250 x 384 and 16875 x 512; scratch/
clo_diff_x3.sh) is running; it is reported when done.
(D) Numerics 20:51:37Z item 2 (a) touches 4.5: the X3 sentence of the inverse paragraph says "against X3's N_f maxima within 0.5 of
P of 6.5e-7 to 6.8e-7"; the implied change is D_v-normalized (an N_v-type quantity), so the like-for-like comparison is X3's N_v
maximum within 0.5 of P, 1.82e-7 / 1.92e-7 / 1.85e-7 on my three configurations (c6g_<cfg>_R7.652e6.json). Suggested: "against X3's
residual maxima within 0.5 of P of 6.5e-7 to 6.8e-7 (N_f) and 1.8e-7 to 1.9e-7 (N_v)", as the X1 sentence already does.
Verdict G93: f66fa76b CONFIRMED except the timeline 20:44 sentence (A) 9 (REFUTED as an explanation; wording given) and the
like-for-like comparison (D); two optional wordings ((A) 1, 6). The team may NOT finish: c6g2 (45), c6h / c6hF (41 / 42), c6gR4 (47)
are open; dom9000gF (48) is a data row.
G93 addendum (2026-10-18T21:24:07Z): the X3 closure row, measured directly on X3 (for 4.4 "The row applies to the candidate" and the lead's
open item "X3 closure-convention ray check").
 Method 1 (code/clo_diff.py, scratch/clo_diff_x3.sh; logs runs/audit/c6g_clodiff_N11250_q384.log, _N16875_q512.log): one shape
 (c6g, md5 15f8095f), field A = formula to 7.652e6, field B = gen_shape closure=1000 (two-term exterior beyond R_shape = 1000 L,
 3375 / 5063 radii replaced); both inverted by my inverse, c_l from the identity on each; R_B - R_A split into the velocity part
 at fixed c_l and the c_l part. Maxima over all grid points of the open first quadrant. The two configurations agree to 3 digits:
   c_l (identity): A 5.5753626074, B 5.5753626109, shift +3.434e-9 (X1: +3.39e-9); B is 2.2e-10 above the fixed value
     5.5753626106, so the identity in the fit's own convention returns the fixed c_l, and the -3.2e-9 of the formula reading is
     the closure.
   |X-P| < 0.5: total N_f 6.85e-9, N_v 2.08e-9; velocity part N_f 5.13e-9, N_v 1.55e-9; max |dU| 9.37e-8.
   0.5 <= |X-P| < 2.5: total N_f 6.87e-9, N_v 4.53e-9; velocity part N_v 4.01e-9; max |dU| 1.14e-7.
   2 <= r < 10: velocity part N_f 1.03e-8, N_v 3.25e-9 (total 6.87e-9 / 3.77e-9).
   10-20 / 20-100 / 100-300 / 300-1000: velocity part N_v 1.59e-8 / 1.59e-8 / 1.58e-8 / 2.04e-8; max |dU| 2.06e-7 / 1.03e-6 /
     3.09e-6 / 1.05e-5.
   With k_self on B: the same to 1.5 percent.
 These equal X1's row (G69 (d): 5.1e-9 / 1.5e-9 near P, 1.0e-8 / 3.2e-9 at 2-10, 2.0e-8 N_v for r < 1000, 1.6e-8 for r <= 300,
 c_l 3.4e-9) to two digits, and agree with the numerics' fit-convention ray data (G93 (C): max |dU| 9.2e-8 / 1.0e-7 / 2.06e-7 /
 1.03e-6 / 3.09e-6 at their nodes; impact 2.0e-9 / 3.1e-9 / 1.4e-8 against my velocity part in N_v 1.55e-9 / 4.0e-9 / 1.6e-8).
 Method 2 (direct band maxima; scratch/c6g_rbclo.sh and scratch/c6g_rbcloB.sh; runs/audit/c6g_<cfg>_R7.652e6_rbclo.json, formula
 continued, and _rbcloB.json, own convention with closure at 1000 L, VAUDIT_RFIT 900 L; cfg {}; bands in physical r). Ratio own /
 formula of the band maxima at 11250 x 384 ; 16875 x 512:
   |X-P| < 0.5      N_f 0.990 ; 1.009     2 <= r <= 10   N_f 0.993 ; 1.009
   10 < r <= 20     N_v 1.026 ; 0.985     20 < r <= 100  N_v 1.071 ; 1.070     100 < r <= 300  N_v 1.099 ; 1.047
   300 < r <= 1000  N_v 0.770 ; 0.821 (X3's 4.50e-8 / 4.36e-8 against 3.46e-8 / 3.58e-8)
   1000 < r <= 3826 (131 L to 500 L)  N_v 0.474 ; 0.472     3826 < r <= 6886 (500 L to 900 L)  N_v 0.248 ; 0.250
   r > 900 L (own convention: the closure region) N_v 9.38e-4 / 9.40e-4 at 1.83e4 (2.40 R_shape), next to the y-axis.
 Relative to X3's own band maxima the velocity-part changes of Method 1 are 0.81 to 0.85 percent (N_v) and 0.75 to 0.79 percent
 (N_f) next to P,
 1.5 percent (N_f) at 2-10, and 22 to 47 percent (N_v) at 10 <= r < 1000 (X3's N_v band maxima there, 4.0e-8 to 7.4e-8, are
 smaller than X1's, while the change is the same); the actual band maxima move by at most 1 percent next to P and at 2-10, by at
 most 10 percent at 10 to 300 and by 18 to 23 percent (downward) at 300 to 1000.
 Consequences for 4.4: the absolute values of the X1 closure row hold for X3 (CONFIRMED directly, to two digits). The sentence
 "The row applies to the candidate, which has X1's radial basis, closure radius and c_l" is CONFIRMED for those absolute values;
 the percentages "about 1 percent of X1's band maxima next to P, 1.5 percent at 2 <= r < 10 and at most 7 percent at 300 to 1000"
 do NOT transfer to X3 beyond r = 10: on X3 the same change is up to 47 percent of its N_v band maxima at 10 <= r < 1000, and the
 band maxima themselves move by up to 10 percent at 10 to 300 and by 18 to 23 percent at 300 to 1000. Suggested: "On X3 directly
 (separate evaluator, 11250 x 384 and 16875 x 512) the changes are the same to two digits; its band maxima move by at most 1
 percent next to P and at 2 <= r < 10, at most 10 percent at 10 to 300 and 18 to 23 percent (lower in the fit's convention) at
 300 to 1000." My earlier consequence in G69 ("the fit and my audit measure the same function there") holds for X3 next to P
 and at 2 <= r < 10 only. Beyond r = 1000 (131 L to 900 L, still on the fit rows) the fit's own convention reads 0.25 to 0.47
 of the formula reading; the audited residuals of 4.3 / 4.4 are the formula (canonical) reading, so they are not affected.
 Closure regions across R_shape (adds X3 to the G91 addendum): 100 L 2.78e-2 (2.67 R_shape), 333 L 5.09e-3 (2.48), 1000 L
 9.4e-4 (2.40), 1e4 L 2.31e-5 (2.32); log-slopes -1.54 (333 L to 1000 L) and -1.61 (1000 L to 1e4 L). Data only.
 Numerics 20:51:37Z item 1 / 2 (a) (same-region ratios of the canonical X3 ray check, x3_c6g_BP.json): max impact over max
 sampled |R| / D within 0.5 of P 8.64e-10 / 1.849e-7 = 0.47 percent, at 0.5 to 2.5 from P 2.57e-9 / 5.49e-8 = 4.7 percent, 51 of
 52 nodes with D > 0: CONFIRMED from the file. The fit-convention file gives 1.09 and 5.5 percent by the same rule.

## G94 (2026-10-18T21:28:18Z). FINAL_REPORT 13845d9c against f66fa76b (lead NOTES 21:10:51Z item 2, 20:59:29Z)

Method: diff scratch/FR_f66f.md scratch/FR_1384.md (scratch/diff_f66f_1384.txt, 69 lines; copy scratch/FR_1384.md, md5
13845d9ca41092cdae83e05708dd4201). Seven changed passages, each checked against its source.
 1. 4.1 "0.03 of it over 1000 L to 9000 L, 4.5": G93 (A) 1 adopted. CONFIRMED.
 2. 4.4 dom90g sentence (20:59:29Z): "in N_v it is 6.0e-8 with the closure and 9.4e-6 with the formula continued (11250 x 384)"
    matches G86 addendum (6.03e-8 / 9.42e-6, grid maxima within 0.5 of P). "6.7e-6 at its sampled points within 0.5 of P ...
    (velocity change 4.2e-4 there)": recomputed from ../numerics/runs/ray/dom90g_BP.json with P = (8.600065, 0): the 20 nodes
    with |X - P| < 0.5 are the region of their table row "P<0.5"; max impact 6.647e-6 (their table prints 6.65e-6), max
    component of dU 4.158e-4. The region is the stated one: CONFIRMED. Rounding only: 6.647e-6 is 6.6e-6 to two digits
    (optional). "with the closure-convention denominator held fixed" describes their impact (dU.grad rho / D with D from the
    closure-convention export). CONFIRMED.
 3. 4.5 "continuing X3 with rows to 9000 L lowers it ... by the factor 0.028 to 0.029 (the rows and the further iterations
    together; X3 continued on its own rows for the same iterations separates them [OPEN])": dom9000g starts from the c6g end
    (numerics 18:45:42Z, md5 15f8095f verified there); the parenthesis is the G93 (A) 5 qualification. CONFIRMED.
 4. 4.5 far-field paragraph: "moved toward" (G93 (A) 6 optional) adopted. "its second-order coefficient 0.17 of X3's and its
    third-order coefficient of the opposite sign" (q2 -14.65 / -88.78 = 0.165; q3 -3.46e4 against +1.190e5), "four terms (8.8e-8,
    -4.6e-7, 5.7e-7, -1.9e-7) sum to -2.5e-9", "-0.30 to +0.15 times its own first-order term", "its band value is set by the
    higher orders, and its fall is not the removal of the first-order term alone": CONFIRMED (G93 (A) 9 (ii), (iii)). Two
    precision notes from runs/farP/dom9000g_N16875_q512_R7.652e6.json, optional: the six columns are theta 1.49962 to 1.56834,
    the first 0.0712 from the y-axis ("within 0.072", or "at theta 1.500 to 1.568"); the range -0.30 to +0.15 is over the rows
    and their 11-node radial windows, the row values themselves being -0.132 to +0.035 at 1000 L and -0.286 to +0.028 at 4701 L
    (the +0.15 is the window value of the column 1.56834 inside the A5 cut).
 5. 4.5 inverse paragraph: "against X3's residual maxima within 0.5 of P of 6.5e-7 to 6.8e-7 (N_f) and 1.8e-7 to 1.9e-7 (N_v)":
    G93 (D) adopted (1.82e-7 / 1.92e-7 / 1.85e-7). CONFIRMED.
 6. Timeline 20:44: the replacement follows the G93 wording; "Whether the rows or the 20750 further iterations produce the fall
    is not separated by this row." CONFIRMED (c6g2 open).
 7. Timeline 21:02: "confirmed except two items, both corrected ... two optional wordings were adopted" describes G93 (A) 9 and
    (D) and the optional (A) 1 and (A) 6. CONFIRMED.
Not yet in the report (written after 21:10:51Z): the G93 addendum. The 4.4 sentence "about 1 percent of X1's band maxima next to
P, 1.5 percent at 2 <= r < 10 and at most 7 percent at 300 to 1000 ... The row applies to the candidate" stands in 13845d9c; by
the G93 addendum the absolute values transfer to X3 but the percentages do not beyond r = 10 (up to 47 percent of X3's N_v band
maxima at 10 <= r < 1000). Wording is in the addendum.
Verdict G94: 13845d9c CONFIRMED as a correction of f66fa76b (two optional precision notes in 4, one rounding in 2). The G93
addendum item on 4.4 is outstanding. The team may NOT finish: c6g2 (45), c6h / c6hF (41 / 42), c6gR4 (47) are open.

## G95 (2026-10-18T22:24:17Z). FINAL_REPORT c2fd67e4 against 13845d9c (lead NOTES 21:27:32Z items 1-3, 21:39:34Z items 1-3); SPEC v4.9 section 8 record (21:50:31Z item 5)

Copies: scratch/FR_c2fd.md (md5 c2fd67e47f5afd1aaadbc626c54b3d6f), diff scratch/diff_1384_c2fd.txt (four hunks); SPEC
scratch/SPEC_v49.md (md5 a497b3d6), diff against the lead's notes/SPEC_pre_v49.md (one added item in section 8, one history line).
1. 4.4 closure row on X3 (21:27:32Z item 1): every number checked against my G93 addendum: two grids agree to 3 digits; changes
   equal X1's to two digits; c_l +3.434e-9 in the identity convention, the fit's own convention 2.2e-10 above the fixed value;
   0.75 to 0.85 percent next to P ("0.8 percent"), 1.5 percent at 2-10, 22 to 47 percent in N_v at 10-1000; X3's band maxima
   move by at most 1 percent next to P and at 2-10, at most 9.9 percent at 10-300 (upward), 18 and 23 percent lower at 300-1000;
   131 L to 900 L: 0.248 to 0.474 ("0.25 to 0.47"). The X1 sentence with its own percentages is kept and reads as X1's row.
   CONFIRMED.
2. 4.5 inverse paragraph (21:27:32Z item 2): "X3's by the same to two digits (grid maxima; 4.4)": CONFIRMED (velocity part N_f
   5.13e-9 within 0.5 of P, N_v 2.04e-8 for r < 1000, against X1's 5.1e-9 / 2.0e-8). The 52-node numbers recomputed from
   ../numerics/runs/ray/x3_c6g_fit_BP.json: componentwise max |dU| 9.17e-8 within 0.5 of P and 9.18e-8 at 0.5 to 2.5 from P
   ("at most 9.2e-8 within 2.5 of P"), 3.06e-6 at r 250-350 ("3.1e-6 at r = 300"); impact 2.03e-9 / 3.09e-9 / 1.44e-8 at r 20
   to 300. CONFIRMED as componentwise maxima, which is the numerics lane's measure ("componentwise max |dU|"). The Euclidean
   norm of dU is 1.007e-7 at 0.5 to 2.5 from P: my G93 (C) "1.0e-7" was that norm, not a disagreement. Optional: "(componentwise)".
3. Timeline 21:24 (21:27:32Z item 3): CONFIRMED in substance. Optional precision: in 4.4 the X1 percentages were kept as X1's row
   and the sentence carrying them over to the candidate was replaced; "were replaced in section 4.4 by the candidate's own
   numbers" can be read that way.
4. 21:39:34Z item 1: 6.6e-6 (6.647e-6): CONFIRMED.
5. 21:39:34Z item 2: "within 0.072 of the y-axis", "-0.29 to +0.04 times its own first-order term (-0.30 to +0.15 over 11-node
   radial windows ...)": the row values on runs/farP/dom9000g_N16875_q512_R7.652e6.json are -0.1323 to +0.0346 at 1000 L and
   -0.2857 to +0.0281 at 4701 L; windows -0.3024 to +0.1521. CONFIRMED (+0.04 is an outward rounding of +0.0346, so the stated
   range contains the values).
6. Timeline 21:28: CONFIRMED (G94 at 21:28:18Z, one rounding and two optional notes, all adopted).
7. SPEC v4.9 section 8 record against the notes it cites:
   - Angular row: matches 15:14:26Z item 4 (five quantities, no increase beyond the configuration spread, each row reported;
     m <= 250 pair a refinement row; "if lower than the candidate the report says so and the deliverable does not change").
   - Two-sided A4: matches G85 and 20:28:25Z item 4.
   - Budget row: matches 17:42:41Z (45) and 21:10:51Z item 3 (i)-(iii), including the [0.8, 1.25] reading of the domain columns
     against c6g2 and the 0.8 / 0.5 thresholds on the 1000 L-9000 L band (formula continued, N >= 16875) and on C at the axis.
   - R_shape 1e4 L control: 18:04:24Z item 5 says "on both N >= 16875 configurations" for both "~ c6g" and "falls", and that the
     same C-at-the-axis computation is made; the record omits both. Suggested: "ratios in [0.8, 1.25] on both N >= 16875
     configurations read as 'about X3', at most 0.5 on both as 'falls'; C at the axis computed as for the 9000 L row".
   - Free 9000 L control: matches 20:41:00Z item 2 (data only).
   - "No change of standard": CONFIRMED (no other line of SPEC changed).
Verdict G95: c2fd67e4 CONFIRMED; SPEC v4.9 record CONFIRMED with one omission (item 7, 18:04:24Z item 5 qualifier). The team may
NOT finish: c6g2 (45; fit done 22:23:35Z, audit set starting), c6h row (41; G96 to follow), c6hF (42), c6gR4 (47) open.

## G96 (2026-10-18T22:28:07Z). The m <= 250 refinement row c6h (chain 6 step 41) and the angular row 100 / 150 / 200 / 250 at the fixed c_l (lead NOTES 15:14:26Z item 4, 21:50:31Z item 4, 22:11:22Z)

Item: c6h = the c6g end enriched to m <= 250 (start md5 4dafef26), 20750 iterations at the fixed c_l 5.5753626106 on 20480 x
1200 rows; chain line 21:42:32Z, my copy runs/gen4/gpu/c6h_shape.npz md5 5b192f613fe8a0b80f8eda6a944db6b5 (matches), L
7.651424486640698, R_shape 1000 L. A refinement row, not a candidate (15:14:26Z item 4).
Method: my generator (code/gen_shape.py, formula continued) and evaluator (code/vaudit.py, own inverse to 7.652e6), cfg {} as the
row audits, on the three configurations shared by all four rows: 16875 x 512 (M 639), 16875 x 768 (M 959), 22500 x 512 (M 639).
c6h's density has sine modes to n = 2 x 250 + 3 = 503, so 11250 x 384 (M 479) does not resolve it: whole-box N_f 2.6e-4 there; it
is not a row value, and the q384 J run (c6h_jr, running) is flagged the same way. Quantities: whole-box N_f, N_f within 0.5 of P,
N_v r <= 1000 (max over the five inner bands), N_v over all r > 1000, each raw and with the A5 cut (pi/2 - theta >= 0.006,
G67); 857-label J (jset2, r_start 20, Ktop 500) at 16875 x 512 for c6g and c6h (runs/audit/c6{g,h}_N16875_q512_R7.652e6_jd2.json);
far1_ver C at the axis; scratch/row_read.py and the table script in the WORKLOG entry of this time.
(a) The row (16875 x 512 ; 16875 x 768 ; 22500 x 512), values and the ratio to the previous row:
  whole-box N_f raw     fxd1g 3.113e-6 ; 3.127e-6 ; 3.114e-6     s2g 1.435e-6 ; 1.505e-6 ; 1.438e-6 (0.461 ; 0.481 ; 0.462)
                        c6g 6.841e-7 ; 7.156e-7 ; 6.832e-7 (0.477 ; 0.475 ; 0.475)  c6h 5.380e-7 ; 9.820e-7 ; 5.412e-7 (0.786 ; 1.372 ; 0.792)
  whole-box N_f A5      c6g as raw (maximum next to P)   c6h 4.228e-7 ; 4.271e-7 ; 4.875e-7 (0.618 ; 0.597 ; 0.714), at the lobe
                        above P (r 8.716 ; 8.716 ; 8.736, theta 0.194)
  N_f within 0.5 of P   fxd1g, s2g, c6g as whole box   c6h 2.407e-7 ; 2.949e-7 ; 2.256e-7 (0.352 ; 0.412 ; 0.330), on the first
                        column off the x-axis in each configuration (theta 0.0025 ; 0.0016 ; 0.0025, r 8.586)
  N_v r <= 1000 raw     fxd1g 8.738e-7 ; 8.765e-7 ; 8.743e-7   s2g 4.005e-7 ; 4.200e-7 ; 4.014e-7 (0.458 ; 0.479 ; 0.459)
                        c6g 1.917e-7 ; 2.485e-7 ; 1.914e-7 (0.479 ; 0.592 ; 0.477)   c6h 1.232e-7 ; 3.161e-7 ; 1.443e-7 (0.643 ; 1.272 ; 0.754)
  N_v r <= 1000 A5      c6g 1.917e-7 ; 2.006e-7 ; 1.914e-7   c6h 1.232e-7 ; 1.244e-7 ; 1.424e-7 (0.643 ; 0.620 ; 0.744)
  N_v r > 1000 raw      fxd1g 1.325e-6 ; 1.329e-6 ; 1.325e-6   s2g 1.115e-6 ; 1.132e-6 ; 1.117e-6 (0.841 ; 0.852 ; 0.843)
                        c6g 1.101e-6 ; 1.111e-6 ; 1.103e-6 (0.988 ; 0.982 ; 0.987)   c6h 1.096e-6 ; 1.114e-6 ; 1.101e-6 (0.995 ; 1.003 ; 0.998)
  N_v r > 1000 A5       c6g 1.0744e-6 ; 1.0765e-6 ; 1.0746e-6   c6h 1.0786e-6 ; 1.0790e-6 ; 1.0793e-6 (1.004 ; 1.002 ; 1.004)
                        (s2g -> c6g at 22500 x 512, the one shared A5 value: 1.011)
  857-label J (eps 0.03 / 0.01)  fxd1g 5.283e-6 / 5.484e-6, s2g 3.143e-6 / 3.462e-6, c6g 1.388e-6 / 1.602e-6 (at 16875 x 384;
                        at 16875 x 512 1.3877e-6 / 1.6014e-6), c6h 5.0015e-7 / 5.8860e-7 at 16875 x 512 (0.360 / 0.368 of c6g)
  C at the axis (far1_ver)  2.003519e-2, 1.892287e-2, 1.868707e-2, 1.865728e-2 (ratios 0.944, 0.988, 0.998)
  Configuration spreads (max - min over the three): c6g / c6h whole-box N_f 3.2e-8 / 4.4e-7 (raw), 3.2e-8 / 6.5e-8 (A5); near P
  3.2e-8 / 6.9e-8; N_v r <= 1000 5.7e-8 / 1.9e-7 (raw), 9.1e-9 / 1.9e-8 (A5); N_v r > 1000 9.8e-9 / 1.9e-8 (raw), 2.2e-9 /
  6.9e-10 (A5); J one configuration each (c6g q384 against q512: 5e-10).
(b) c6h's raw whole-box maximum and its raw N_v r <= 1000 at 16875 x 768 lie in the column next to the y-axis (theta 1.5683 at M
  639, 1.5692 at M 959, r 9.27 to 9.51): the evaluator floor of G67 (c). Check (scratch/axis_cols.py; runs/axc/*.json): for the
  columns s = 1..24 from the y-axis, max over r in [1, 20] of |R| / N_f, on two angular resolutions:
    distance from the axis   0.00123   0.00164   0.00245   0.00327   0.00491   0.00982   0.01473   0.01963   0.02945
    c6h 11250 x 768 (M 959)     -      5.67e-7      -      1.73e-7   9.74e-8   2.83e-8   1.03e-8   2.75e-8   2.11e-8
    c6h 7500 x 1024 (M 1279) 9.95e-7      -      2.27e-7      -      7.91e-8   2.55e-8   1.24e-8   2.67e-8   2.23e-8
    c6g 7500 x 1024 (M 1279) 7.33e-7      -      2.55e-7      -      1.37e-7   7.89e-8   3.04e-8   5.31e-8   8.46e-8
  Next to the axis the value grows about like (distance)^-2 and R / rho changes sign between resolutions (c6h +1.14e-6 at
  0.00164, -1.99e-6 at 0.00123; c6g +2.03e-6 at 0.00123): an absolute error of R that does not vanish on the axis, where the exact
  R is O(x^2) (parity) and |R| / N_f has a finite limit. At distances 0.0098 and beyond the two resolutions agree to about 10
  percent (1e-8 to 3e-8 on c6h). So the raw c6h maxima at 0.0016 and 0.0025 are the evaluator floor, not the trial; the A5
  values are its readings. Beyond the floor, c6h's near-axis residual is 0.26 to 0.58 times c6g's at the same distance (M 1279,
  distances 0.0049 to 0.029; c6h's maxima at r 9.24 to 9.68, c6g's at r 8.58 to 9.83), consistent with the lead's scans on the axis itself (22:11:22Z: 4.24e-8 at r 9.31 against
  c6g's 1.02e-7 at r 9.56). CONFIRMED: the lead's reading "the evaluator's cancellation floor, not a trial defect".
(c) Reading by the 15:14:26Z item 4 rule.
  - Literally, on the raw values: no quantity increases from one row to the next by more than the configuration spread. The c6h
    increases at 16875 x 768 (whole-box N_f +2.7e-7, N_v r <= 1000 +6.8e-8) are inside c6h's own spread, which is set by the
    floor column of (b), and N_v r > 1000 changes by -5.7e-9 / +3.2e-9 / -2.3e-9 (spreads 9.8e-9 / 1.9e-8).
  - On the A5 values (floor columns excluded, as G67 A5 asks for every quoted maximum): whole-box N_f, near-P N_f, N_v r <= 1000
    and J decrease at every step on every configuration (c6g -> c6h 0.60 to 0.71, 0.33 to 0.41, 0.62 to 0.74, 0.36 / 0.37). N_v
    r > 1000 rises by 2.5e-9 to 4.7e-9 (0.2 to 0.4 percent), above c6h's and c6g's A5 spreads (6.9e-10, 2.2e-9); its maximum is
    on the first column beyond the cut (theta 1.5610 to 1.5643, r 3.65e4 to 3.79e4, about 4800 L). So with A5 the far quantity
    does not decrease at the last step (it did not at 150 -> 200 either, 1.011 at the one shared configuration).
  - The far quantity saturates along the row (raw 0.84, 0.98 to 0.99, 0.995 to 1.003), as C at the axis does (0.944, 0.988,
    0.998): the band value beyond 1000 is set by the far-field profile, which the angular refinement leaves at X3's.
  Verdict on (c): systematic improvement holds for the interior quantities and J on every reading; for N_v r > 1000 the row is
  flat at the last step (within the raw spread, +0.2 to +0.4 percent with A5). The rule as written (raw values) is met.
(d) Against the lead's numbers (21:50:31Z items 2, 3): J 0.354 on 185 labels against my 0.360 / 0.368 on 857 labels: CONFIRMED. Whole
  box at the lobe above P 0.685 / 0.700 of c6g (r 8.73, theta 0.194) against my A5 0.618 / 0.597 / 0.714 at the same place:
  agreement within my configuration spread; c6h's lobe maximum moves with the radial sampling (4.23e-7 at 16875, 4.88e-7 at 22500,
  r 8.716 / 8.736; c6g's moves by 0.1 percent), so a sampling-phase scan (scratch/phase_scan.sh) is queued. C at the axis 0.99841
  of c6g's on mine, -4.0778e-3 / -4.0843e-3 = 0.99841 on the lead's (lead C = -mine / (c_l - 1): 1.865728e-2 / 4.575362611 =
  4.0778e-3): CONFIRMED to all digits. Far band (lead 1000 L-9000 L 1.0885e-6 against 1.092e-6, 0.997) against my N_v r > 1000
  raw 0.995 to 1.003: CONFIRMED. h(P) - 1: lead -9.0e-9 / -5.4e-9; mine waits for c6h_x (extra_checks 16875 x 512, queued).
(e) Still open on this row (addenda): h(P) - 1 and the identity c_l (c6h_x); the near-P maximum on the first column off the x-axis
  (scratch/xside_run.sh: columns next to the x-axis near P at M 959 / 1279; no cancellation floor there since every sine mode
  vanishes on the x-axis); the lobe phase scan; the residual map c6h512.
Verdict G96: c6h numbers CONFIRMED; the row 100 -> 150 -> 200 -> 250 improves systematically by the 15:14:26Z rule on the raw values
(interior quantities and J also on the A5 values; N_v r > 1000 flat at the last step). c6h is lower than the candidate in the
interior and J, as the rule anticipates; it is a refinement row, so the deliverable does not change. Not an endpoint; the team may
NOT finish (c6g2, c6hF, c6gR4 open).
(G97 item 6 (b) to (d) corrects three statements of (b) and (c) above: resolution agreement, the c6h / c6g range from 0.01 on,
and the column of the far maximum.)

## G97 (2026-10-18T22:38:52Z). FINAL_REPORT c90fa579 against c2fd67e4 and SPEC 00ed1007 (lead NOTES 22:32:29Z items 1, 2); G96 addenda (c6h centre values, c6g at M 959) and corrections to my own G96 wording

Copies: scratch/FR_c90f.md (md5 c90fa579c03833b8993d2de9089d49a0), diff scratch/diff_c2fd_c90f.txt (seven hunks); SPEC
scratch/SPEC_00ed.md (md5 00ed100701564415ee916f154568e2bd) against scratch/SPEC_v49.md: one changed item, nothing else.
Method: every number in the diff checked against G95, G96 and the source files runs/audit/c6{g,h}_N{16875_q512,16875_q768,
22500_q512}_R7.652e6.json (band maxima and their positions), runs/audit/c6h_N16875_q512_R7.652e6_jd2.json, runs/axc/*.json
(the near-axis columns of G96 (b), now with c6g at M 959), runs/audit/c6h_extra.log and c6h_zeros.json (c6h_x).
1. SPEC 00ed1007: the record of the R_shape 1e4 L control now carries "on both N >= 16875 configurations" and "C at the axis
   computed as for the 9000 L row" (G95 item 7). CONFIRMED; no other line changed.
2. Timeline 21:24 (reworded) and 4.5 "componentwise": the G95 item 2 and 3 optional notes as I wrote them. CONFIRMED.
3. Timeline 22:24 (G95): CONFIRMED.
4. Resolution table, row 375 x m <= 250 (table at 16875 x 512): 4.23e-7 (A5 4.228e-7, at the lobe r 8.716, theta 0.194),
   1.23e-7 (1.232e-7; raw equals A5 there, maximum at the lobe), 5.00e-7 (J 5.0015e-7 at eps 0.03), footnote 5.38e-7 raw
   (theta 1.5683, the column next to the y-axis, r 9.33): CONFIRMED. "read at 16875 and 22500 radial points only ... n = 503":
   CONFIRMED (G96). Wording of footnote (a): the cut (pi/2 - theta >= 0.006) removes the columns within 0.006 of the y-axis,
   which at 16875 x 512 (M 639, spacing 0.00245) are two (distances 0.00245 and 0.00491), not one; the raw maximum is in the
   first. Suggested: "(a) With the columns within 0.006 of the y-axis excluded (the cut of (*)); with them 5.38e-7, the
   evaluator's floor in the column next to the axis (4.4)." The [OPEN] h(P) - 1 entry can now be filled from item 9:
   "-, 3.2e-8" (no 11250 value, since 11250 x 384 does not resolve the row).
5. Budget note ("X3 with its angular cap raised to 250 and continued 20750 iterations at the fixed c_l, so it is at the budget
   X3 + 20750"): CONFIRMED (G96 item; start md5 4dafef26, 20750 iterations at 5.5753626106).
6. New 4.4 paragraph, values: whole-box N_f 5.38e-7, 9.82e-7, 5.41e-7 (0.79, 1.37, 0.79); near P 2.41e-7, 2.95e-7, 2.26e-7
   (0.35, 0.41, 0.33); N_v r <= 1000 1.23e-7, 3.16e-7, 1.44e-7 (0.64, 1.27, 0.75); N_v r > 1000 1.096e-6, 1.114e-6, 1.101e-6
   (0.995, 1.003, 0.998); J 5.00e-7 / 5.89e-7 (0.36 / 0.37); A5 whole box 4.23e-7, 4.27e-7, 4.88e-7 (0.62, 0.60, 0.71), r 8.72
   to 8.74, theta 0.194; A5 N_v r <= 1000 1.23e-7, 1.24e-7, 1.42e-7 (0.64, 0.62, 0.74); increases at 16875 x 768 2.7e-7 and
   6.8e-8 against spreads 4.4e-7 and 1.9e-7; rise of N_v r > 1000 2.5e-9 to 4.7e-9 against spreads 6.9e-10 and 2.2e-9; C
   0.944, 0.988, 0.998: all CONFIRMED. Positions: the raw whole-box maxima are in the column next to the y-axis on all three
   configurations (theta 1.5683, 1.5692, 1.5683; r 9.33, 9.51, 9.27), and the raw N_v r <= 1000 maxima at 16875 x 768 and
   22500 x 512 are there too (band 0.1-2, r 0.33 and 0.25); at 16875 x 512 the raw N_v r <= 1000 maximum is at the lobe:
   CONFIRMED. Four statements need a correction; (b) to (d) came from my G96 wording, so they are corrections of my record too:
   (a) "within 0.4 percent of X3 beyond r = 1000" (4.1 and timeline 22:28): on the A5 values c6h / c6g is 1.00392, 1.00233,
       1.00438, so 0.23 to 0.44 percent above; on the raw values 0.99485, 1.00289, 0.99789 (-0.52 to +0.29 percent).
       Suggested: "0.2 to 0.5 percent above X3 beyond r = 1000" (or "within 0.5 percent"). In the 4.4 paragraph "(0.2 to 0.4
       percent)" is my one-digit rounding of 0.23 to 0.44 and may stay or read "0.2 to 0.44".
   (b) "from distance 0.01 on the two agree to about 10 percent": at the distances the two resolutions share (0.0098, 0.0147,
       0.0196, 0.0245, 0.0295) c6h's values differ by 11, 21, 3.1, 8.1, 5.7 percent; the 21 percent at 0.0147 is next to a
       sign change of R (between 0.0123 and 0.0135 at M 1279). Suggested: "agree to 3 to 21 percent (to about 10 percent
       except next to a sign change of R at 0.013)".
   (c) "which is 0.26 to 0.58 times X3's at the same distances" (attached to "from distance 0.01 on"): my G96 range covered
       0.0049 to 0.029. From 0.0098 on, at the shared distances, c6h / c6g is 0.249 to 0.507 at M 959 and 0.264 to 0.502 at
       M 1279; over every column from 0.0098 to 0.039 it is 0.09 to 0.73 (largest at 0.016 to 0.017, where X3's R changes
       sign; smallest at the outer columns). Suggested: "which is 0.25 to 0.51 times X3's at the distances the two
       resolutions share (0.09 to 0.73 over all columns to 0.039)".
   (d) "(maximum at about 4800 L on the first column beyond the cut)": the c6h A5 maxima of N_v r > 1000 are at theta 1.5610,
       1.5643, 1.5610, that is 0.0098, 0.0065, 0.0098 from the y-axis: the second column beyond the cut at M 639 (16875 x 512,
       22500 x 512; the first is at 0.0074) and the first at M 959; r 4772, 4944, 4825 L (3.65e4 to 3.78e4; my G96 "3.79e4"
       should read 3.78e4). Suggested: "(maximum at about 4800 L, 0.0065 to 0.0098 from the y-axis, on the first or second
       column beyond the cut)". c6g's is on the first column beyond the cut at 16875 x 512 and 16875 x 768 (theta 1.5634,
       1.5643) and on the third at 22500 x 512 (theta 1.5585, 0.0123 from the axis).
   Optional: "ratios 0.84" for fxd1g -> s2g is 0.841, 0.852, 0.843 ("0.84 to 0.85"); my G96 (c) has the same rounding.
7. 4.1 sentence after the angular row: same numbers as item 6, CONFIRMED except (a). "has 20750 iterations more than X3":
   CONFIRMED.
8. Timeline 22:28 (G96): CONFIRMED except (a); "(shown there to be the evaluator's floor on two angular resolutions)" and "its
   comparison at equal budget is open" are correct.
9. G96 addendum, c6h centre values (c6h_x, extra_checks at 16875 x 512, M 639; and vcand of the three audits):
   identity c_l 5.5753626074279 (16875) and 5.5753626074287 (22500), against X3's 5.5753626074262 / 5.5753626074270: the fixed
   5.5753626106 is 3.21e-9 above, as for X3. h(P) - 1 on the grid route of the table column: +3.19e-8 (16875 x 512 and x 768),
   -1.79e-8 (22500 x 512), against X3's +3.11e-8 / -1.78e-8 on the same configurations: the evaluator's grid error, equal to
   X3's within 1e-9. Dense-trace route (mk_traces / cl_from_h): h(P) = 1 + 5e-9, c_l from h(P) = 1 is 5.575362603 (4.8e-9
   below the identity value; X3 +7.0e-9 on 11250 x 384). x* = 8.6000641 (X3 8.6000638). Centre jet (vd14): a0 = 1 to 10
   digits, 4(p2 - c r^2/2)/r^4 -> -1/3 (-0.333310 to -0.333332 at r 0.002 to 0.02), as X3. Zero set (vzeros): one zero of
   W1 on the x-axis (8.6000640), none of W2 on the y-axis (min W2/y 5.5756), no open-quadrant cell, min |W| / (c_l |X|)
   at distance >= 1.0 / 0.3 / 0.1 from P 0.0216 / 0.0067 / 0.0023 (positive; X3's centre jet -0.333353 to -0.333333). The lead's -9.0e-9 / -5.4e-9 are on the lead's
   evaluator; every route gives |h(P) - 1| < 1e-7. CONFIRMED: the m <= 250 row has X3's centre values.
10. G96 (b) addendum, c6g at M 959 (runs/axc/c6g_N11250_q768.json, the last of the four column runs): c6g's floor also
   changes sign between resolutions (R/rho -1.1e-6 at 0.00164 on M 959, +2.0e-6 at 0.00123 on M 1279), and from 0.0049 on
   the two resolutions agree to 0.04 to 12 percent (3.3, 0.5, 12.4, 2.0, 2.9, 0.04 percent at the shared distances). This
   supports the floor reading of (b) on the candidate as well.
Verdict G97: FINAL_REPORT c90fa579 CONFIRMED with corrections (a) to (d) of item 6 (four wording or range corrections, none
changes a reading or the deliverable; (b) to (d) correct my G96 text too) and the footnote wording of item 4; SPEC 00ed1007
CONFIRMED. c6h centre values CONFIRMED (item 9). The team may NOT finish: c6g2 (45; audit set running), c6hF (42), c6gR4 (47)
open.

## G98 (2026-10-18T23:07:17Z). c6g2 (chain 7 step 45: X3 continued 20750 iterations on its own rows, m <= 200, fixed c_l; the budget row, not a candidate): readings of lead NOTES 21:10:51Z item 3 (i) to (iii); the values requested in 22:32:29Z item 4 (with the 22:50:22Z correction); the lead's numbers of 22:32:29Z items 3, 4 and 22:50:22Z

Inputs. runs/gen4/gpu/c6g2_shape.npz, md5 0072c9ea (equal to the chain line "step 45 done"), k 0.17936053129375418 (X3's),
L 7.651424191117591 (X3 7.651424601381517), angular 200, fixed c_l 5.5753626106. Audit set of scratch/j45.sh (done 22:58:08Z):
gen_audit at 11250 x 384, 16875 x 512, 16875 x 768, 22500 x 384, 22500 x 512 (formula-global, own convention, cfg {}, as the X3
baseline rows); far bands _rb45 (k_self) at 16875 x 512 and 22500 x 384; BA5 at 16875 x 512; 857-label J (jset as X3, 16875 x
384, strip); extra_checks at 11250 x 384; residual map near P (c6g2512, 16875 x 512). Readers: scratch/c6g2_tab.py (output
scratch/c6g2_tab_out.txt), scratch/read_fit.py, scratch/c6g2_read.py, scratch/jshell.py, scratch/cmp_resmap.py. Own evaluator
throughout (code/vcand.py, vresid; own discretization and full-plane inverse).

1. Checks of the field (vcand, 16875 x 512): parity defect 2.3e-13, top-mode share 6.9e-15, divergence check -4.4e-12, c
   15.7260878223 (exporter 15.7260878319), identity c_l 5.5753626074287 (X3 5.5753626074262; the fixed 5.5753626106 is 3.2e-9
   above, as for X3), mu1 / A - 1 = -3.5e-9, no other axis zeros. As X3 on every item.
2. The five quantities of 15:14:26Z item 4 on the three shared configurations 16875 x 512 (M 639) ; 16875 x 768 (M 959) ; 22500
   x 512 (M 639). Values are c6g2's; in brackets c6g2 / X3, then c6h / c6g2.
   - Whole-box N_f, raw: 4.770e-7 ; 7.274e-7 ; 5.362e-7 (0.697 ; 1.017 ; 0.785 | 1.128 ; 1.350 ; 1.009). The c6g2 maxima are in
     the column next to the y-axis (theta 1.5683 ; 1.5692 ; 1.5683, r 9.24 ; 9.70 ; 9.48), the evaluator's floor (G96 (b), G97
     item 10), as for c6h. X3's raw maxima are next to P (r 8.53, theta 0.0074 ; 0.0082 ; 0.0074).
   - Whole-box N_f, A5: 4.249e-7 ; 4.366e-7 ; 5.036e-7 (0.621 ; 0.610 ; 0.737 | 0.995 ; 0.978 ; 0.968), at the lobe above P (r
     8.72 to 8.74, theta 0.194 to 0.195), as for c6h. X3's A5 maximum is next to P (6.841e-7 ; 7.157e-7 ; 6.832e-7), so this
     c6g2 / X3 compares c6g2's lobe with X3's region next to P. At the lobe itself (map of item 7, 16875 x 512) c6g2 / X3 is
     4.249e-7 / 4.321e-7 = 0.983.
   - Near-P N_f (|X - P| < 0.5; the y-axis cut does not reach it): 3.594e-7 ; 3.599e-7 ; 3.596e-7 (0.525 ; 0.503 ; 0.526 | 0.670
     ; 0.819 ; 0.627). c6g2's maxima are left of P (r 8.32 ; 8.17 ; 8.33, theta 0.017 ; 0.008 ; 0.017), c6h's at r 8.59, theta
     0.002 to 0.003, X3's at r 8.53.
   - N_v r <= 1000, raw: 1.238e-7 ; 2.930e-7 ; 1.503e-7 (0.646 ; 1.179 ; 0.785 | 0.995 ; 1.079 ; 0.960). At 16875 x 768 and 22500
     x 512 the c6g2 maxima are in the column next to the y-axis (r 0.0067 and 2.05), floor.
   - N_v r <= 1000, A5: 1.238e-7 ; 1.276e-7 ; 1.471e-7 (0.646 ; 0.636 ; 0.769 | 0.995 ; 0.975 ; 0.968), at the lobe.
   - N_v r > 1000, raw: 1.1008e-6 ; 1.1175e-6 ; 1.1048e-6 (0.9994 ; 1.0057 ; 1.0017 | 0.995 ; 0.997 ; 0.996), column next to the
     y-axis, r 3.4e4 to 3.8e4.
   - N_v r > 1000, A5: 1.0774e-6 ; 1.0773e-6 ; 1.0777e-6 (1.0028 ; 1.0007 ; 1.0029 | 1.0011 ; 1.0017 ; 1.0015), theta 1.5561
     (0.0147 from the y-axis), r 3.54e4 to 3.59e4 (4630 to 4690 L).
   - J (857 labels, 16875 x 384): spread 6.7240e-7 at eps 0.03 and 7.1989e-7 at eps 0.01, against X3's 1.3882e-6 / 1.6019e-6
     (0.484 / 0.449). X3 at x 512 gives 1.3877e-6 / 1.6014e-6 (0.04 percent from x 384), so x 384 resolves the m <= 200 rows.
     c6h (x 512; x 384 does not resolve it, G96) / c6g2: 5.0015e-7 / 6.7240e-7 = 0.744 and 5.8860e-7 / 7.1989e-7 = 0.818.
   - On the other two configurations, c6g2 / X3: 11250 x 384: whole box 1.009 (raw = A5; both maxima at the same point, r 8.78,
     theta 0.308), near P 0.544, N_v r <= 1000 1.009, N_v r > 1000 0.9993 (A5 0.9934); 22500 x 384: 0.736 (raw = A5, lobe),
     0.538, 0.768, 0.9992 (A5 0.9929).
   - Per band (BA5, 16875 x 512, A5), N_f then N_v, c6g2 / X3 and c6h / c6g2: r <= 0.1 1.184 and 0.838 (both values 5e-9 to
     6e-9); 0.1-2 0.862 and 0.381; 2-10 0.621 / 0.646 and 0.995 (the lobe); 10-100 1.013 / 0.776 and 0.436 / 0.491; 100-1000 0.789
     / 0.779 and 0.533 / 0.541; r > 1000 N_f 1.018 and 0.963, N_v 1.003 and 1.001.
3. Centre values (extra_checks at 11250 x 384, and the vcand of the audits). h(P) - 1 on the grid route: +3.54e-8 (16875 x 512
   and x 768), -1.79e-8 (22500 x 512), +3.45e-7 (11250 x 384), against X3's +3.11e-8, -1.78e-8, +2.84e-7: the evaluator's grid
   error, as for X3 and c6h. Dense-trace route: h(P) = 1 + 1.6e-8, c_l from h(P) = 1 is 5.575362592 (1.5e-8 below the identity
   value). x* = 8.6000649 (X3 8.6000638). Zero set (vzeros): one zero of W1 on the x-axis (8.6000645), none of W2 on the
   y-axis, no open-quadrant cell, min |W| / (c_l |X|) at distance >= 1.0 / 0.3 / 0.1 from P 0.0216 / 0.0065 / 0.0026 (positive).
   Centre jet (vd14): a0 = 1, 4 (p2 - c r^2 / 2) / r^4 from -0.333353 to -0.333333 at r 0.002 to 0.02 (limit -1/3). As X3.
4. Reading 21:10:51Z item 3 (i), far band 1000 L to 9000 L, c6g2 / X3 (_rb45 against X3's _rb44): raw 0.9994 (16875 x 512),
   0.9992 (22500 x 384); A5 1.0028, 0.9929. Other bands: 900 L-1000 L 1.041 / 1.038; 9000 L-1e4 L raw 1.0001 / 1.0008, A5
   0.9941 / 0.9920; r > 1e4 L raw 0.9948 / 0.9962, A5 0.9929 / 0.9929. C at the axis (far1_ver, nt 16384): 1.873515e-2 against
   X3's 1.868707e-2, ratio 1.0026. All above 0.8 on both N >= 16875 configurations: by (i), the fall of the 9000 L row (dom9000g,
   G91) in the far band and in C comes with its rows; the budget does not produce it.
5. Reading 21:10:51Z item 3 (ii). Interior c6g2 / X3: A5 whole box 0.61 to 0.74, near P 0.50 to 0.54, N_v r <= 1000 A5 0.64 to
   0.77, J 0.484 / 0.449 (item 2). Domain rows against c6g2 (near-P N_f on 11250 x 384 ; 16875 x 512 ; 22500 x 384, then J at
   eps 0.03 / 0.01):
   - dom90g: 0.601 ; 0.632 ; 0.603 (below 0.8 on all three), J 0.823 / 0.818 (inside). The ratio is stated: near P the 90 L row
     is 0.60 to 0.63 of the budget row, so its near-P gain over X3 is more than the budget's; its J is in [0.8, 1.25].
   - dom300g: 1.092 ; 1.083 ; 1.087 (inside on all three), J 1.211 (inside) / 1.254 (0.004 above 1.25). By (ii) its near-P gain
     over X3 is the budget's (on near-P N_f and on J at eps 0.03; the ratio at eps 0.01 is 1.254).
   - dom9000g: 1.259 ; 1.248 ; 1.270 (inside only at 16875 x 512), J 1.354 / 1.417 (above). The ratio is stated: near P the 9000
     L row is 1.25 to 1.27 times the budget row and its J 1.35 to 1.42 times.
6. Reading (iii): c6g2 is the budget row, not a candidate; X3 stays the candidate. CONFIRMED that nothing in the audit set
   changes this (no check of item 1 or 3 differs from X3's).
7. Residual map near P (c6g2512 against c6g512, 16875 x 512, same grid): window maximum 4.249e-7 at the lobe (x 8.553, y 1.679)
   against X3's 6.841e-7 next to P (x 8.527, y 0.063); within 0.5 of P 3.594e-7 at (8.320, 0.143) against 6.841e-7; x > x*, y <
   0.2 unchanged (1.826e-7 against 1.830e-7); y >= 1 4.249e-7 against 4.321e-7 (0.983). The theta oscillation at omega 399 next
   to the x-axis falls to 0.39 to 0.68 of X3's amplitude at r 8.0 to 8.6 (unchanged at r 8.8, omega 94). These are the evaluator
   values of item 2 on an independent grid (vresmap).
8. Lead numbers of 22:32:29Z item 3 (lead tools, formula continued, 24576 x 576, inverse to 1e6 L): C at the axis -4.0948e-3
   against -4.0843e-3 (1.0026) equals -1.873515e-2 / (c_l - 1) (4.575362611) on my far1_ver: CONFIRMED. Band 1000 L-9000 L
   0.9997 (A5 1.0039), 9000 L-1e4 L 0.9994, r > 1e4 L 0.9994: consistent with item 4 (0.999 to 1.003, 0.992 to 1.001, 0.993 to
   0.996): CONFIRMED as a cross-check; the reading in item 4 is on my rows.
9. Lead numbers of 22:32:29Z item 4 and 22:50:22Z, c6h / c6g2 (lead fit-convention scans 32768 x 640 ; 24576 x 960):
   - whole box (lobe above P) 0.978 ; 0.961: CONFIRMED (mine 0.995 ; 0.978 ; 0.968, item 2).
   - 0.1-2 0.428 ; 0.428, 10-100 0.460 ; 0.464, 100-1000 0.509 ; 0.470: consistent with mine at 16875 x 512 (0.381; 0.436 N_f /
     0.491 N_v; 0.533 / 0.541). "the cap lowers the bands away from P by about 2": CONFIRMED (0.38 to 0.54 on my bands).
   - "1000 L band 0.719 ; 0.702": not reproduced on my bands; my r > 1000 band is 0.963 (N_f A5) and 1.001 (N_v A5, maximum at
     about 4700 L next to the y-axis). The lead's band is narrower; the ratio is the lead's.
   - J (22:50:22Z correction, 185 labels, r0 20, eps 0.03): c6g 1.257e-6, c6g2 5.998e-7 (0.477 of X3), c6h 4.450e-7 (0.354),
     c6h / c6g2 0.742: CONFIRMED against my 857 labels (c6g2 / X3 0.484, c6h / X3 0.360, c6h / c6g2 0.744 at eps 0.03).
   - Shells. The 22:32:29Z shell split is on the lead's 10 labels (22:50:22Z). On my 857 labels (scratch/jshell.py, spreads over
     labels of J(eps) differences; X3 x 384, c6g2 x 384, c6h x 512): [4, inf) 2.867e-7, 2.416e-7, 9.73e-8 (c6h / c6g2 0.40);
     [2, 4) 1.756e-7, 1.505e-7, 1.407e-7 (0.93); [1, 2) 2.718e-7, 2.378e-7, 1.904e-7 (0.80); [0.3, 1) 3.801e-7, 3.327e-7,
     2.471e-7 (0.74); [0.03, 0.3) 1.037e-6, 3.738e-7, 3.837e-7 (1.03, higher, as the lead's 1.14); [0.01, 0.03) 2.438e-7,
     8.69e-8, 1.563e-7 (1.80). Same pattern as the lead's (largest fall in the outer shell, none in [0.03, 0.3)); the labels and
     the shell definition differ, so the lead's shell ratios are the lead's.
   - The lead's conclusion "the fall of the m <= 250 row at the lobe above P is almost all the budget's, and the cap lowers the
     bands away from P by about 2": CONFIRMED on my rows. Near P the budget gives 0.50 to 0.53 of X3 and the cap a further 0.63
     to 0.82; beyond r = 1000 neither changes anything by more than 0.6 percent (A5 0.07 to 0.29 percent).
10. Lead's E2 numbers of 22:50:22Z (fit-convention 2-10 / lobe maxima of the domain rows against c6g2): not recomputed; the (ii)
   reading of item 5 uses my near-P N_f and 857-label J, as 22:50:22Z states.
Verdict G98: c6g2's audit numbers CONFIRMED (items 1 to 3, 7); 21:10:51Z item 3 (i): the far fall of dom9000g comes with its
rows (band 0.993 to 1.003, C 1.0026); (ii): dom300g's near-P gain over X3 is the budget's (J at eps 0.01 1.254, stated),
dom90g (0.60 to 0.63) and dom9000g (1.25 to 1.27, J 1.35 to 1.42) have their ratios stated; (iii) c6g2 is not a candidate. The
lead's numbers of 22:32:29Z items 3 and 4 and of 22:50:22Z CONFIRMED except the "1000 L band" ratio, which my bands do not
reproduce (item 9). The team may NOT finish: c6hF (42) and c6gR4 (47) are open, and FINAL_REPORT 4d36c535 is not yet audited.

## G99 (2026-10-18T23:08:01Z). FINAL_REPORT 4d36c535 against c90fa579 (lead NOTES 22:40:38Z item 1); SPEC unchanged (00ed1007)

Method: copy scratch/FR_4d36.md, diff against scratch/FR_c90f.md (scratch/diff_c90f_4d36.txt, 62 lines, five hunks: timeline
22:28 and a new 22:38 entry, 4.1, the 4.4 resolution table row and footnote, the 4.4 paragraph on the m <= 250 row). Nothing
else changed.
1. G97 item 6 (a): 4.1 "0.23 to 0.44 percent above X3 beyond r = 1000", 4.4 "(0.23 to 0.44 percent)", timeline 22:28 "0.23 to
   0.44 percent above the candidate": applied as suggested; on the A5 reading of the paragraph. CONFIRMED.
2. (b) "agree to 3 to 21 percent (to about 10 percent except next to a sign change of R at 0.013) at 1e-8 to 3e-8", (c) "0.25
   to 0.51 times X3's at the distances the two resolutions share (0.09 to 0.73 over all columns to 0.039)", (d) "(maximum at
   about 4800 L, 0.0065 to 0.0098 from the y-axis, on the first or second column beyond the cut)", optional "0.84 to 0.85":
   applied verbatim. CONFIRMED.
3. "the evaluator's floor, on X3 as on this row": supported by G97 item 10 (X3's floor column also changes sign between M 959
   and M 1279; agreement 0.04 to 12 percent from 0.0049 on). CONFIRMED.
4. Table row "-, 3.2e-8" and footnote (a) "With the columns within 0.006 of the y-axis excluded; with them 5.38e-7, the
   evaluator's floor in the column next to the axis (4.4)": as G97 item 4. CONFIRMED. (Cosmetic: a line break after "(4.4).
   The" splits the footnote's second sentence; it renders as one paragraph.)
5. Centre values sentence: c_l 5.5753626074 with the fixed value 3.2e-9 above it; h(P) - 1 +3.2e-8 and -1.8e-8 (mine +3.19e-8
   and -1.79e-8; X3's +3.11e-8 and -1.78e-8, so "X3's to 1e-9" holds, largest difference 8e-10); 5e-9 on the dense-trace route;
   a single zero of the x-velocity on the axis at 8.600064; min |W| / (c_l |X|) 0.0216, 0.0067, 0.0023 at distance 1, 0.3,
   0.1: all as G97 item 9. Leaving out the centre-jet limit is correct (4.2's D14 is a different quantity). CONFIRMED.
6. Timeline 22:38: "confirmed with four range or wording corrections (...), all applied; the centre values of the m <= 250
   row were measured and are the candidate's": CONFIRMED (the footnote wording of G97 item 4 is a fifth, smaller change, also
   applied).
7. "[OPEN: the two compared at equal budget]" in the 4.4 paragraph and in the timeline 22:28 entry is now answered by G98
   (c6h / c6g2 on the three shared configurations; the lead's numbers CONFIRMED except the "1000 L band" ratio). The lobe
   sampling-phase scan is still running (scratch/phase_scan.sh; two of three maps done).
Verdict G99: FINAL_REPORT 4d36c535 CONFIRMED; SPEC 00ed1007 unchanged. The team may NOT finish: c6hF (42) and c6gR4 (47) open.

## G100 (2026-10-18T23:18:32Z). FINAL_REPORT 9cd594cd against 4d36c535 (lead NOTES 23:11:51Z item 2); G96 (e) addendum: c6h next to the x-axis near P

A. Diff (copy scratch/FR_9cd5.md; scratch/diff_4d36_9cd5.txt, 135 lines, 8 hunks; nothing else changed). Every new number
is from G98; checked against G98 items 2, 4, 5, 9 and scratch/c6g2_tab_out.txt.
1. Timeline 22:28 ("was open (23:07)") and the new 23:07 entry: 0.61 to 0.74 whole-box N_f (A5 0.610 to 0.737 at N >= 16875),
   0.50 to 0.54 within 0.5 of P (0.503 to 0.538), 0.48 in J, within 1 percent beyond r = 1000 (0.9929 to 1.0057), the three
   readings of 21:10:51Z item 3, and "equals the budget row to 3.2 percent at the lobe above P and is lower next to P and away
   from P" (0.968 to 0.995; 0.63 to 0.82; 0.38 to 0.54): CONFIRMED.
2. 4.2 (E1): objective 1.264e-6, 0.781 of X3's (numerics 22:26:28Z: 1.619270e-6 -> 1.263892e-6): CONFIRMED. 0.61 to 0.74,
   0.50 to 0.54, 0.64 to 0.77 (A5 0.636 to 0.769), 0.99 to 1.01 for r > 1000, 0.48 / 0.45 in J, "centre values are X3's":
   CONFIRMED. "(its maximum moves from next to P to the lobe above P, where it is 0.98 times X3's value there)": the 0.983 is
   measured at 16875 x 512 only (map of G98 item 7), and the lobe maximum moves with the radial sampling (G101 to follow, c6h
   lobe 4.22e-7 to 4.66e-7 over four radial phases); suggested "(... where it is 0.98 times X3's value there at 16875 x 512)"
   until G101 gives the ratio over the phases. "So X3 is limited by the iteration budget, except beyond r = 1000": CONFIRMED.
3. 4.3 "Not in the table: the budget row ... and the m <= 250 refinement row (4.4), neither a candidate": correct (the 4.3
   table lists the fits compared by the rules; the m <= 250 row is in the 4.4 resolution table). CONFIRMED.
4. 4.4 domain paragraph (E2): 0.50 to 0.54 and 0.48 (0.45); 300 L 1.08 to 1.09 (1.083 to 1.092) and 1.21 in J (1.254 at eps
   0.01, 0.004 above the interval), "so its near-P gain over X3 is that of the budget"; 90 L 0.60 to 0.63 (0.82 in J); 9000 L
   1.25 to 1.27 and 1.35 (1.42): CONFIRMED. Wording: "not inside the interval near P on every configuration" can be read as
   "outside on every configuration", which is false for the 9000 L row (1.248 at 16875 x 512 is inside). Suggested: "outside
   the interval near P on all three configurations (90 L) or on two of the three (9000 L, inside at 16875 x 512 only; its J
   is outside), so for these two the ratios are stated without attribution".
5. 4.4 m <= 250 paragraph: 0.97 to 1.00 in whole-box N_f and N_v for r <= 1000 (0.968 to 0.995, both at the lobe), 0.63 to
   0.82 within 0.5 of P, 1.001 to 1.002 for r > 1000 (A5 1.0011 to 1.0017), 0.74 in J (0.82 at eps 0.01), 0.38 to 0.54 in the
   three bands at 16875 x 512, "within 3.2 percent of the budget row" at the lobe, stated without a threshold: CONFIRMED on the
   sampled grids. The [OPEN] on the lobe sampling phase stays until G101 (c6g2 and X3 maps at the same phases are running).
6. 4.5: "reads 0.993 to 1.003 of X3's there and 1.0026 of X3's C at the axis, so the fall comes with the rows": CONFIRMED (G98
   item 4).
7. 4.8 (E4): "beyond r = 1000 neither changes N_v by more than 1 percent": CONFIRMED and better than my 0.6 percent, which
   covered only the three shared configurations; with 11250 x 384 and 22500 x 384 the budget row's largest change is 0.71
   percent (A5 0.9929), the m <= 250 row's against the budget row 0.5 percent (raw 0.995). The 4.8 sentence as a whole
   (budget continuation 0.61 to 0.74, 0.50 to 0.54, 0.48; m <= 250 against it 0.97 to 1.00, 0.63 to 0.82, 0.74; "values
   reached at that budget and cap, not converged values for the basis"): CONFIRMED.

B. G96 (e) addendum: c6h next to the x-axis near P (scratch/xside_run.sh, scratch/axis_cols.py with AXC_SIDE=x; columns s = 1
to 24 from the x-axis, r in [8, 9.2]; runs/axc/x_*.log; and the four radial phases of the c6h map, G101).
8. c6h, maximum of |R| / N_f on the first column off the x-axis: 2.41e-7 (dtheta 0.00245, M 639, N 16875; 1.90e-7 to 2.41e-7
   over the four radial phases), 2.55e-7 (dtheta 0.00164, M 959, N 11250; 2.95e-7 at N 16875 in G96), 2.15e-7 (dtheta 0.00123,
   M 1279, N 7500), always at r 8.58 to 8.59 (0.01 to 0.02 left of x*), with the same sign of R on every resolution (R/rho
   -4.3e-7 at M 1279, -5.1e-7 at M 959; R/N_f -2.4e-7 at M 639). The second column is about half (1.33e-7, 1.34e-7, 1.50e-7).
   So the value does not grow as the column approaches the axis and keeps its sign: unlike the y-axis floor (G96 (b)) it is a
   value of the row, about 2e-7 to 3e-7, and the near-P readings of G96 and G98 stand.
9. N 7500 is not a reading configuration: for c6h it gives 2.1e-7 to 3.2e-7 on columns 5 to 12 (theta 0.006 to 0.015), about
   twice the N 11250 x 768 and N 16875 x 512 values there (1.0e-7 to 1.7e-7, which agree with each other); for X3 it gives the
   same pattern as N 16875 (the angular oscillation at omega 399, peak 7.5e-7 at theta 0.0086 against 6.84e-7 at 0.0074).
   X3's first column off the x-axis is 2.72e-7 (M 639) and 5.30e-7 (M 1279), below its oscillation peak at both resolutions.
Verdict G100: FINAL_REPORT 9cd594cd CONFIRMED with two wording suggestions (item 2: "at 16875 x 512" for the lobe 0.98; item 4:
the "not inside ... on every configuration" sentence). c6h's near-P maximum on the first column off the x-axis is a value of
the row, not an evaluator floor (item 8). The team may NOT finish: c6hF (42), c6gR4 (47) open; G101 (phase scan) to follow.

## G101 (2026-10-18T23:35:04Z). Radial sampling-phase scan of the lobe above P and of the near-P maximum: c6h, c6g2, X3 (the [OPEN] of FINAL_REPORT 4.4)

Method. scratch/phase_scan.sh (c6h) and scratch/phase_more.sh (c6g2, X3): vresmap at 16875 x 512 (M 639) with the log-radial
grid shifted by 0.25, 0.5, 0.75 of its step (r0 and R times exp(f h), h = ln(1e10) / 16874), window r 7.5 to 10.5, theta <= 0.6,
besides the unshifted maps <tag>512 (same theta columns). Reader scratch/phase_sup.py: per map the sampled maximum of |R| / N_f
near P (|X - P| < 0.5) and at the lobe (r 8.5 to 9.0, theta 0.12 to 0.30); on the union of the four maps per column (radial
spacing a quarter step) the maximum with a three-point parabolic refinement in r. Own evaluator (vresid).
1. Lobe above P, per phase 0 / 0.25 / 0.5 / 0.75 (union):
   X3     4.321e-7 / 4.604e-7 / 4.267e-7 / 4.744e-7 (4.749e-7), spread 10.0 percent;
   c6g2   4.249e-7 / 4.684e-7 / 4.278e-7 / 4.857e-7 (4.857e-7), spread 12.5 percent;
   c6h    4.228e-7 / 4.574e-7 / 4.218e-7 / 4.656e-7 (4.664e-7), spread 9.4 percent.
   Union maxima at r 8.737, theta 0.1939 on all three rows. At equal phase: c6g2 / X3 0.983, 1.017, 1.003, 1.024 (union 1.023); c6h /
   c6g2 0.995, 0.976, 0.986, 0.959 (union 0.960); c6h / X3 0.978, 0.993, 0.988, 0.981 (union 0.982). At 22500 x 512 (one phase):
   X3 4.954e-7 (map c6g22512), c6g2 5.036e-7, c6h 4.875e-7 (A5 maxima, G98): 1.017 and 0.968.
2. Shape of the lobe maximum. The union profile of R / N_f along theta 0.1939 is smooth across the four grids: a radial
   oscillation of period about 0.036 in r (about 3 steps of the N 16875 grid; it is not locked to any one grid), so a single
   grid samples between about 0.87 and 1.00 of the union maximum (lowest phase: X3 0.90, c6g2 0.87, c6h 0.90). The 22500 x 512
   values lie above the 16875 union by 3.7 to 4.5 percent (X3 4.95e-7 against 4.75e-7, c6g2 5.04e-7 against 4.86e-7, c6h
   4.88e-7 against 4.66e-7), so the lobe value also depends on the radial resolution at that level.
3. Near P, per phase (union): X3 6.841e-7 / 6.785e-7 / 6.803e-7 / 6.843e-7 (6.847e-7), spread 0.8 percent; c6g2 3.594e-7 /
   3.595e-7 / 3.590e-7 / 3.586e-7 (3.596e-7), 0.3 percent; c6h 2.407e-7 / 2.331e-7 / 1.903e-7 / 2.131e-7 (2.421e-7), 20.9
   percent (its maximum is on the first column off the x-axis, G100 item 8, a narrow feature at r 8.586). The phase-0 values
   are within 0.1 percent of the union for X3 and c6g2 and 0.6 percent for c6h (the largest of its four), so the near-P readings (c6g2 / X3 0.525, c6h / c6g2 0.67,
   c6h / X3 0.354 on the union) are not sampling artefacts.
4. Reading. The lobe above P is the same on the three rows to within 2.4 percent of X3 (union) and 4.1 percent between c6h and
   c6g2 (any one phase), on 16875 x 512, and within 3.2 percent at 22500 x 512. Neither the 20750 further iterations nor the
   raised cap lowers it. The whole-box maxima of c6g2 and c6h are this lobe value; X3's whole-box maximum is next to P (6.84e-7)
   and its lobe is 0.62 to 0.69 of that. So the whole-box fall of c6g2 and c6h relative to X3 (A5 0.60 to 0.74) is the fall
   next to P, down to the level of the lobe, and not a fall at the lobe.
5. Consequences for FINAL_REPORT 9cd594cd (to be applied; they correct readings, not the deliverable):
   (a) 4.4 table and m <= 250 paragraph, "[OPEN: sampling-phase scan of the lobe]": the lobe maximum of the m <= 250 row at
       16875 x 512 is 4.22e-7 to 4.66e-7 over four radial sampling phases (the table's 4.23e-7 is the phase-0 grid value) and
       4.88e-7 at 22500 x 512; X3's lobe is the same to 2 percent (4.27e-7 to 4.74e-7; 4.95e-7).
   (b) 4.4 m <= 250 paragraph, "So at the lobe above P the m <= 250 row is within 3.2 percent of the budget row and its fall
       there relative to X3 is matched by the budget": at the lobe there is no fall relative to X3 to match (c6h / X3 0.98, c6g2
       / X3 1.00 to 1.02 over the phases); within 3.2 percent holds on the sampled grids, 4.1 percent over the phases.
       Suggested: "At the lobe above P the three rows agree to within 4 percent over four radial sampling phases (m <= 250 row
       0.96 to 0.995 of the budget row, the budget row 0.98 to 1.02 of X3), so the whole-box maxima of the m <= 250 row and of
       the budget row are the lobe value, which neither the further iterations nor the raised cap lowers; their whole-box
       ratios to X3 come from the fall next to P."
   (c) 4.2 "(its maximum moves from next to P to the lobe above P, where it is 0.98 times X3's value there)": over the four
       phases 0.98 to 1.02 (union 1.02) at 16875 x 512 and 1.02 at 22500 x 512. Suggested "(... where it equals X3's value
       there to 2.4 percent)".
   (d) The 23:07 timeline entry ("equals the budget row to 3.2 percent at the lobe above P"): "to 4 percent, over four radial
       sampling phases" and, if (b) is adopted, "the lobe value is common to X3, the budget row and the m <= 250 row".
   (e) 4.8: "the m <= 250 row reads 0.97 to 1.00 in whole-box N_f ... of that continuation": correct on the sampled grids; with
       (b) the whole-box ratio is that of a common lobe value, 0.96 to 0.995 over the phases.
   (f) Item 4 of G96 / G98 numbers are unchanged; the 4.4 statement that the lobe maximum "moves with the radial sampling" is
       CONFIRMED (9 to 12.5 percent at 16875 x 512 on all three rows).
Verdict G101: lobe phase scan DONE; the lobe above P is common to X3, c6g2 and c6h within 4 percent; near-P readings phase-stable
(except c6h's narrow first-column value, 21 percent, phase 0 the largest). Text corrections (b) to (d) of item 5 needed. The
team may NOT finish: c6hF (42) and c6gR4 (47) open.

## G102 (2026-10-18T23:37:59Z). Diff audit of FINAL_REPORT 9cd594cd -> 6b749206 (through 96646bcd; lead NOTES 23:22:05Z and 23:36:51Z)

Method. Copies scratch/FR_9cd5.md and scratch/FR_6b74.md (md5 6b7492064bc85f31d88276601a582d01, 1297 lines), diff
scratch/diff_9cd5_6b74.txt: six hunks (timeline 23:07 / 23:18 / 23:35; 4.2; 4.4 table footnote (a); 4.4 domain columns;
4.4 m <= 250 paragraph; 4.8). No other line changed. Each number checked against G98, G100 and G101 (phase_sup.py rerun after
the first write of G101 gives the per-phase values of G101 items 1 and 3 to all quoted digits).
Note on G101. Item 2, 3 and 4 of G101 were corrected in place within minutes of the first write, before this audit, against
the rerun: the 22500 x 512 lobe lies 3.7 to 4.5 percent (not 4 to 5) above the 16875 union; a single grid samples 0.87 to
1.00 (not 0.90 to 1.00) of the union; the phase-0 near-P value is within 0.1 percent of the union for X3 and c6g2 and 0.6
percent for c6h; the 22500 x 512 agreement is 3.2 percent (not 3.3); the whole-box fall is A5 0.60 to 0.74 (c6h / X3
included). The lead's 23:36:51Z note quotes the first version in one place (item 1 (d)).
1. Timeline 23:07 "to 3.2 percent at the lobe above P on the sampled grids (to 4 percent over four radial sampling phases,
   23:35)": CONFIRMED (c6h / c6g2 0.968 to 0.995 sampled; 0.959 to 0.995 over phases).
2. Timeline 23:18: CONFIRMED (G100 items 2, 4 and 8).
3. Timeline 23:35: CONFIRMED except "lies 4 to 5 percent higher at 22500 x 512": 3.7 to 4.5 percent (X3 4.95 / 4.75, c6g2
   5.04 / 4.86, c6h 4.88 / 4.66). Suggested "lies about 4 percent higher (3.7 to 4.5) at 22500 x 512". "within 1 percent"
   (0.8 and 0.3), "varies by 21 percent, the unshifted grid giving the largest" and "the whole-box maxima of the budget row
   and of the m <= 250 row are this lobe value": CONFIRMED.
4. 4.2 "where it equals X3's value there to 2.4 percent over four radial sampling phases": CONFIRMED (c6g2 / X3 0.983 to
   1.024).
5. 4.4 footnote (a): CONFIRMED (c6h 4.218e-7 to 4.656e-7 per phase, 4.875e-7 at 22500 x 512; X3 4.267e-7 to 4.744e-7 and
   4.954e-7).
6. 4.4 domain sentence "outside the interval near P on all three configurations (90 L) or on two of the three (9000 L,
   inside at 16875 x 512 only; its J is outside)": CONFIRMED (G98 item 5, G100 item 4; J 1.35 / 1.42).
7. 4.4 m <= 250 paragraph. "4.22e-7 to 4.66e-7 ... X3's lobe is 4.27e-7 to 4.74e-7, the same to 2 percent": per phase c6h /
   X3 is 0.978 to 0.993 (union 0.982), so "to 2.2 percent" is exact; "to 2 percent" is a rounding, acceptable.
   "in whole-box N_f 0.96 to 0.995 over four radial sampling phases at 16875 x 512": CONFIRMED. "the three rows agree to
   within 4 percent ... (the m <= 250 row 0.96 to 0.995 of the budget row, the budget row 0.98 to 1.02 of X3)": CONFIRMED.
   "which neither the further iterations nor the raised cap lowers" (my G101 suggestion): too strong for the cap. The raised
   cap lowers the lobe by 0.5 to 4.1 percent over the phases (union 0.960) and by 3.2 percent at 22500 x 512, with the same
   sign at every phase; the further iterations change it by -1.7 to +2.4 percent. Suggested: "which the further iterations
   do not lower and the raised cap lowers by at most 4 percent". "their whole-box ratios to X3 come from the fall next to
   P" and the kept sentence "Next to P and in the bands away from P the raised cap lowers the residual further":
   CONFIRMED (G98 items 2, 3; G101 items 3, 4).
8. 4.8 "(both maxima are the lobe value above P, common to X3 and the two rows within 4 percent over four radial sampling
   phases)": CONFIRMED.
Verdict G102: FINAL_REPORT 6b749206 CONFIRMED with two wording corrections (item 3: 3.7 to 4.5 percent; item 7: the raised
cap lowers the lobe by at most 4 percent). The team may NOT finish: c6hF (42) and c6gR4 (47) open.

## G103 (2026-10-18T23:40:54Z). B_3 along the angular row, under the budget row and with rows to 9000 L (lead NOTES 23:30:53Z item 2)

Method. scratch/b3rows.sh: code/vb3ibp.py (own code) on the own traces runs/gen4/<tag>_traces.npz (x-axis traces of w, w',
w'' from the own inverse via scratch/mk_traces.py; Mmax 479, c6h at Mmax 639 since its density has modes to n = 503), both
w'' routes (ODE, finite difference), the 32-row method table of vb3ibp (near-0 fit range, end treatment, end point).
Outputs runs/ibp/b3r_<tag>.json. Median over the method table, [min, max] in brackets, wpp_ode route:
     row                          ibp form                    original form               x*         A = 2 c_l - 1
     fxd1g (m <= 100)             0.2985 [0.2975, 0.2993]     0.3002 [0.2927, 0.3051]     8.600058   10.150725219
     s2g (m <= 150)               0.2992 [0.2985, 0.3006]     0.3021 [0.2971, 0.3070]     8.600064   10.150725215
     c6g = X3 (m <= 200)          0.2996 [0.2985, 0.3020]     0.3029 [0.2985, 0.3096]     8.600064   10.150725215
     c6h (m <= 250)               0.3012 [0.3001, 0.3032]     0.3044 [0.2983, 0.3130]     8.600064   10.150725215
     c6g2 (budget row)            0.3000 [0.2989, 0.3020]     0.3037 [0.2994, 0.3098]     8.600065   10.150725215
     dom9000g (rows to 9000 L)    0.2998 [0.2987, 0.3020]     0.3032 [0.2989, 0.3098]     8.600065   10.150725222
The wpp_fd route gives the same medians to 1e-4. The lead's numbers (work/b3rows/*_vb3.json, the same code run read-only on
the same traces) are reproduced to all printed digits; this is a reproduction with the same code and traces, not an
independent recomputation (the independence of vb3ibp from the lead's tool is Part 12 (b), G17; the two forms on c6g, G74 (a)). dom90g and dom300g have no
traces in this lane; they are not evaluated.
Reading. The ibp medians of the six rows lie in 0.2985 to 0.3012 (spread 0.0027); the method spread within one row is 0.0018
to 0.0035. Along the angular row 100 -> 150 -> 200 -> 250 the ibp median rises monotonically by 0.0007, 0.0004, 0.0016, each
step within the method spread of the rows it joins. The budget row and the 9000 L row are within 0.0004 of X3.
Verdict G103: the statement "B_3 is unchanged to about 0.003 along the angular row 100 -> 250, under the budget row and with
rows to 9000 L" is CONFIRMED (0.2985 to 0.3012 in the ibp form, 0.3002 to 0.3044 in the original form; the original form's
method spread, up to 0.015, is larger than its row-to-row change). B_3 is about 0.30 on every row, far from
zero on this measure. The team may NOT finish: c6hF (42; GPU done 23:39:43Z, audit set running) and c6gR4 (47) open.

## G104 PRELIMINARY (2026-10-18T23:58:25Z). c6hF (chain 6 step 42: free control of the m <= 250 row c6h) against c6h, three configurations; set incomplete

Status: OPEN. Values so far (own evaluator, scratch/read_fit.py c6hF c6h; copy md5 b8a9a3fc matches the chain line 23:39:43Z):
     configuration     A5 N_f r <= 1000   A5 N_v r <= 1000   N_f within 0.5 of P   N_v r > 1000 (ya >= 0.006)
     16875 x 512       0.990              0.992              0.947                 0.996
     16875 x 768       1.003              1.006              0.966                 0.996
     22500 x 512       0.988              0.988              0.889                 0.996
   (ratios c6hF / c6h; both A5 maxima at the lobe above P, r 8.72 to 8.74, theta 0.194.) 857 J at 16875 x 512, M 639: 1.019
   (eps 0.03, 5.0986e-7 / 5.0015e-7) and 1.019 (eps 0.01). c6hF: c_l (1/k) 5.5763705557, identity 5.5763705525 (-3.2e-9, as
   X3), start 5.576371155, drift -6.0e-7 (below 1e-4: no slope resolved); L 7.6520567; h(P) - 1 +4.39e-8 / -1.89e-8 (16875 /
   22500; c6h +3.19e-8 / -1.79e-8); x* 8.600844; C at the axis 0.998 of c6h. GPU objective 5.2220e-7 against c6h 5.2063e-7.
   Raw maxima next to the y-axis (column theta 1.5683 / 1.5692) differ in both directions (the evaluator floor, G96 (e)).
Pending: BA5 (running), phase scan (scratch/phase_c6hF.sh, maps at 0.25 / 0.5 / 0.75 of the radial step; the A5 differences
of 1 percent lie inside the 9 percent phase spread of the lobe, G101), jr, extra_checks, map c6hF512, N11250 q384 (row table
only). No reading by the 12:02Z rule yet: whole-box changes sign across configurations, near P and far favour c6hF, J favours c6h.
The team may NOT finish: c6hF (42) and c6gR4 (47) open.

## G105 (2026-10-19T00:16:31Z). FINAL_REPORT 6b749206 reports no absolute residual values (PROMPT: "Compute both meaningful absolute and normalized residual norms"; SPEC (N4); my G20 (b1))

Method: grep of FINAL_REPORT 6b749206 for absolute values of R or E (none: 4.4 gives only maxima of |R|/N_f and |R|/N_v,
4.4 "Elliptic equation" gives sup|E| / sup|d_x rho|). Absolute values from my own audits of X3 (c6g, formula convention,
runs/audit/c6g_<cfg>_R7.652e6.json, field abs_max = max |R| over the region on the between-node grid of my evaluator,
own generator and own inverse to R = 7.652e6). Scale: max |rho| over the band from code/gen_shape.shape_rho on a tensor grid
of 1200 log-r x 513 theta points per band (formula convention as in the audits).
Result (X3; max |R| at 11250 x 384 / 16875 x 512 / 16875 x 768 / 22500 x 512; max |rho| over the band; their quotient at
16875 x 512, a sup-to-sup scale, not a pointwise ratio):
     region               max |R|                                        max |rho|     quotient
     r <= 0.1             1.28e-13 / 1.71e-13 / 2.67e-13 / 1.65e-13      3.85e-4       4.4e-10
     0.1 <= r <= 2        8.82e-8 / 8.92e-8 / 8.93e-8 / 8.91e-8          2.94          3.0e-8
     2 <= r <= 10         1.10e-4 / 6.03e-5 / 6.08e-5 / 5.82e-5          111.7         5.4e-7
     |X - P| < 0.5        1.05e-5 / 1.05e-5 / 1.10e-5 / 1.05e-5          14.80         7.1e-7
     10 <= r <= 100       1.92e-5 / 1.99e-5 / 1.99e-5 / 1.98e-5          208.9         9.5e-8
     100 <= r <= 1000     6.04e-6 / 6.03e-6 / 6.06e-6 / 6.04e-6          319.2         1.9e-8
     1000 <= r <= R       1.8950e-4 / 1.8968e-4 / 1.8966e-4 / 1.8969e-4  1590 (at R)   1.2e-7
   (max |rho| per band sits at the outer radius of the band, since rho grows like r^(1/c_l) at large r and like r^3 at the
   centre; 11250 x 384 is the under-resolved lobe of 4.3.) The whole-box absolute maximum is the far value 1.897e-4 at
   r > 1000 L (formula beyond the fit); restricted to r <= 1000 with the y-axis columns excluded it is 1.10e-4 / 6.03e-5 /
   6.08e-5 / 5.82e-5. Regional sup ratios max |R| / max N_v (vcand bands): [1, 10] 1.25e-7 / 6.89e-8 / 6.95e-8 / 6.65e-8,
   [10, 100] 2.76e-8 to 2.86e-8, [100, 1000] 1.59e-8 to 1.60e-8, [1000, R] 1.01e-7, [0.01, 1] 9.7e-10 to 9.8e-10,
   [7.65e-4, 0.01] 8e-12 to 3.4e-11.
Reading: absolute and normalized values tell the same story. The absolute residual is largest where rho is largest (the
far field and the band 2 to 10 containing P and the lobe); scaled by the size of rho it is at most 7e-7 (next to P), the
same order as the normalized maxima of 4.4. The absolute values are stable across the four configurations to 2 to 5
percent except 2 <= r <= 10 at 11250 x 384.
Verdict: OPEN (presentation gap, blocks finishing). The prompt asks for both absolute and normalized norms and my G20 (b1)
requires the absolute values. Requested of the lead: a short table in 4.4 with the absolute max |R| by region (the rows
above, or at least 16875 x 512 and 22500 x 512) and the band scale max |rho|, and the absolute sup|E| next to the ratio
sup|E| / sup|d_x rho| (or a sentence that the ratio is of sups, hence the absolute value is the ratio times sup|d_x rho|).
The numbers may be copied from this entry; the c6h row can be added from my c6h_<cfg> files if wanted (same fields).

## G106 (2026-10-19T00:32:18Z). Diff audit of FINAL_REPORT 6b749206 -> 4e8feb68 -> fad52bb2 (lead NOTES 00:15:42Z item 1, 00:23:15Z items 1 and 2)

Method: diff of my copies scratch/FR_6b74.md, scratch/FR_4e8f.md (md5 4e8feb68, 1331 lines) and scratch/FR_fad5.md
(md5 fad52bb2, copied at 2026-10-19T00:32:18Z); every changed number traced to its VERIFY entry or recomputed; the D14 relations re-derived.
(a) 4e8feb68 against 6b749206, 26 hunks. CONFIRMED:
  - timeline 23:38 (G102) and 23:41 (G103) lines; 4.2 B_3 row: medians 0.2985, 0.2992, 0.2996, 0.3012, 0.3000, 0.2998
    (ibp) and 0.3002, 0.3021, 0.3029, 0.3044, 0.3037, 0.3032 (original), method spreads up to 0.0035 and 0.015 (G103);
  - 4.2 centre jet (D14): with a = 1 + delta x^2 + gamma y^2 and psi = c x y + alpha x y^3 + beta x^3 y, the x^4 y and
    x^2 y^3 coefficients of W.grad rho - rho are E = beta - 2 (2 c_l - 1) delta and D2 = (8 c_l - 2) gamma - 5 alpha (my
    own expansion, using c = 3 c_l - 1 at second order); "at most 6e-9" on X3 and F3 over the five windows (my
    extra_checks logs: X3 up to 5.91e-9, F3 up to 5.56e-9, both rel E on [5e-3, 0.1]), X2 8.49e-9 up to r 0.05 and 1.92e-8 on [5e-3, 0.1] (s2g_extra.log);
  - 4.3 footnote (**): 215 / 244 / 302 / 375 values, F2 lowest whole-box, F3 6.95e-7 to 7.65e-7 next to P (G43, G56, G76);
  - 4.4 N_v r > 1000 last step of the angular row: rise 2.5e-9 to 4.7e-9 (0.23 to 0.44 percent), A5 spreads 6.9e-10
    (m <= 250) and 2.2e-9 (m <= 200) (G97 (a): c6g 1.0744e-6, 1.0765e-6, 1.0746e-6; c6h 1.0786e-6, 1.0790e-6, 1.0793e-6);
  - 4.4 domain paragraph: only "closure at" labels added (111 L, 100 L, 333 L); no number changed;
  - 4.5 sentence on the artifacts of the domain columns and section 5 "single-threaded on the CPU (the GPU driver of
    step 5 also uses one GPU)", "domain columns of 4.4" (was 4.3): correct.
  Presentation defects (no number involved):
  - line 701: "min |W| / (c_l |X|) is 0.0216, 0.0065, 0.0026 at |X - P| = 1, 0.3, 0.1.  - Centre jet (D14)." The bullet
    "- Centre jet (D14)." has merged into the end of the previous bullet; it needs its own line.
  - lines 658 to 662: the inserted angular-row text of the B_3 bullet lost its two-space indent, and "with c_l from 5.5752
    to 5.6001, radial" is a broken line.
  - 4.4 line 1005 to 1009 (ref7 item 9, G107): "rises at the last step by 2.5e-9 to 4.7e-9" is the A5 reading, while
    "ratios on these three configurations ... 0.995 to 1.003 per step" two lines later are all-column ratios (G97 (a):
    c6h / c6g raw 0.995, 1.003, 0.998; A5 1.004, 1.002, 1.004). Label the parenthesis "(all columns)" or give the A5
    ratios 1.002 to 1.004 next to it.
  - Conventions, definition of "the standard": G20 (b1) ends "Absolute values are reported too", which the definition
    omits; add it (the values are now in 4.4).
(b) fad52bb2 against 4e8feb68, two hunks (G105 applied).
  Lead question (a): my G105 band rows are over all evaluation columns (regions "2<=r<=10" etc. of the vaudit JSON), not
  A5. For the absolute maxima the exclusion makes no difference: in every one of the four configurations "all" equals
  "all,ya>=0.006" (1.895e-4 to 1.897e-4) and the maximum over r <= 1000 equals "r<=1000,ya>=0.006" (1.097e-4 / 6.028e-5 /
  6.075e-5 / 5.821e-5), because max |R| lies where rho is large, not in the columns next to the y-axis. Suggested text:
  "over r <= 1000 (with or without the evaluation columns next to the y-axis) it is 6.03e-5 / 5.82e-5", and the table
  head may say "all evaluation columns".
  Lead question (b): "to 5 percent" is slightly too tight. Against the 16875 x 512 / 22500 x 512 values the other two
  configurations differ by: 0.1 <= r <= 2 at most 1.1 percent; 2 <= r <= 10 at 16875 x 768 0.8 / 4.4 percent;
  |X - P| < 0.5 at 16875 x 768 1.104e-5 against 1.049e-5 / 1.048e-5, that is 5.2 / 5.4 percent (11250 x 384: 0.2
  percent); 10 <= r <= 100 at 11250 x 384 1.924e-5 against 1.992e-5 / 1.982e-5, 3.4 / 2.9 percent; 100 <= r <= 1000 at
  most 0.5 percent; far at most 0.1 percent. So "to 6 percent" (or "to 5.4 percent") with the same two exceptions.
  The sentence "Scaled by the size of rho the absolute residual is at most 7.1e-7 (next to P)" holds on both tabulated
  configurations (22500 x 512: 1.048e-5 / 14.80 = 7.08e-7; 2 <= r <= 10 5.2e-7); at 16875 x 768 the near-P quotient is
  7.5e-7, so "at most 7.1e-7 (next to P; 7.5e-7 at 16875 x 768)" if the other configurations are meant too.
  Lead item 2, absolute sup|E| on 1 <= r <= 10: sup |d_x rho| there is 19.989 on X3 (code/gen_shape.shape_rho on tensor
  grids 2400 x 1025 and 4800 x 2049 over log r in [0, log 10] and theta in [0, pi/2], fourth-order differences; the two
  grids agree to 7 digits; maximum at r 9.93, theta 1.157). The ratios of my vcand JSONs (c6g_<cfg>_R7.652e6.json, band
  [1, 10], relE = max |E| / max |d_x rho| over the same points) are 1.491e-6 (11250 x 384), 3.934e-7 (16875 x 512),
  3.933e-7 (16875 x 768), 1.046e-7 (22500 x 384), 1.059e-7 (22500 x 512), so sup|E| on 1 <= r <= 10 is 2.98e-5, 7.86e-6,
  7.86e-6, 2.09e-6, 2.12e-6. Suggested text: "sup|E| = 2.98e-5, 7.86e-6, 2.12e-6 on 1 <= r <= 10 (sup |d_x rho| = 20.0
  there)". The evaluator grid maximum of |d_x rho| is below the continuum value by less than 1e-5 relative at these N.
  The other parts of the two hunks (table values, max |rho| column, quotient column, "quotient of two suprema", the
  r <= 0.1 and 11250 x 384 exceptions, far value "where the candidate has no fit rows") match G105. CONFIRMED with the
  "to 6 percent" correction.
Verdict: 4e8feb68 and fad52bb2 CONFIRMED as to content, with the corrections above (two formatting defects, the
all-column label of the 4.4 far ratios, the Conventions sentence, "to 6 percent"). G105 is CLOSED by fad52bb2 once
"to 6 percent" is applied. The G107 items (ref7) are separate.

## G107 (2026-10-19T00:34:16Z). Check of the external referee report astra/ref7 (hostile referee on FINAL_REPORT 6b749206), item by item, against fad52bb2

Method: each claim of astra/ref7/answer.md treated as a claim to check: re-read of the cited FINAL_REPORT text in
fad52bb2 (scratch/FR_fad5.md), my own computations where a number is involved, my VERIFY entries. Line numbers below
are those of fad52bb2.
 1. Banner (STATUS: DRAFT, YES pursued for P_2). Valid only as a reminder: the banner already says no endpoint is
    verified. It must be replaced in the final presentation pass, and the scoped YES must keep the sentence that P_inf is
    not answered. No defect now. OPEN until the final pass.
 2. "determines c_l only to an interval". Valid wording. Suggested: "the tested span of exponents admitting comparably
    accurate fits (not an enclosure of the exponent of an exact profile)". Wording, not blocking.
 3. R1 bound |U| <= C(1+|X|)^gamma. CONFIRMED as a statement defect. For gamma below -3 it is false: rho = x^2 y chi(r^2)
    with compact support satisfies A3 for every gamma, but int x y d_x rho dX = -int x^2 y^2 chi dX != 0 gives psi an
    r^(-2) mode and U an r^(-3) tail. R1 is used only through R2, where 0 < gamma < 1 is in force, so the fix is to state
    the bound for 0 < gamma < 1, the range R2 uses. The rest of R1 and R2 is unaffected.
 4. R7 / R10 regularity. CONFIRMED. G_3 = d_y^3 rho(x,0)/6, b3 = d_y^3 W_2(x,0)/6, the relation a2' + 3 b3 = 0 and the
    B_3 formula need three y-derivatives on the axis (rho in C^3, W in C^3 near the axis), which A_2 (C^(2,alpha)) does
    not give. The identities w' + h = 2 c_l, h' - 2 a2 = -g', a2 = (g' - w'')/2 and w g' = (1 - h) g need only C^2.
    Fix: R7 and the b3 / B_3 parts of R10 "for A_3 profiles (or C^3 axis data)", the rest "for every A_2 profile".
 5. R11 limit statement. CONFIRMED (omission). The nonexistence statement assumes finitely many zeros of X + U[F]; the
    convergence sentence "profiles with c_l -> infinity can only converge to such an F" needs that hypothesis for the
    limit field too (SPEC Lemma 6 lists it). Add "and a finite zero set of the limit field".
 6. |cos theta|. CONFIRMED (notation). Lines 675 and 685 write cos(theta)^(p_3 - 2); line 686 and the code
    (code/gen_shape.py, np.abs) use |cos(theta)|^(p_3 - 2). Same on the first quadrant; the even extension needs |.|.
 7. Domain study. Partly valid. The report says itself (4.4) that the domain columns are closed problems that do not
    establish domain independence. The referee's fix ("a common evaluation of global trial densities across at least
    three fitting domains, with comparable budgets and fixed interior regions") is available from my audits: each domain
    fit is a global trial density (the formula of 4.2 with its own coefficients), and read with the formula continued
    (canonical law, no closure) it is a full-plane residual. Own evaluator, formula continued, k_self as in the audits,
    11250 x 384 / 16875 x 512 / 22500 x 384 (runs/audit/<row>_<cfg>_R7.652e6[_frm|_frm44].json, scratch/domtab.py; the
    dom300g reading at 16875 x 512 and 22500 x 384 and the dom9000g reading at 11250 x 384 are new, scratch/jdomfrm.sh):
      row (fit rows; iterations after X3)   N_f A5 r <= 1000        N_f |X-P| < 0.5         N_v A5 r <= 1000        N_v r > 1000 (A5)
      dom90g (90 L; 20750)                  1.02e-4 (11250 only)    3.11e-5                 9.87e-4                 1.32e-2
      dom300g (300 L; 20750)                7.66e-7/5.28e-7/5.59e-7 4.86e-7/4.88e-7/4.87e-7 4.12e-7/4.14e-7/4.12e-7 3.54e-5/3.53e-5/3.54e-5
      c6g2 (900 L; 20750, budget row)       6.97e-7/4.25e-7/4.86e-7 3.54e-7/3.59e-7/3.55e-7 1.94e-7/1.24e-7/1.42e-7 1.077e-6/1.077e-6/1.078e-6
      dom9000g (9000 L; 20750)              7.05e-7/4.49e-7/4.91e-7 4.45e-7/4.49e-7/4.51e-7 1.96e-7/1.26e-7/1.44e-7 3.27e-8/3.31e-8/3.28e-8
      X3 (900 L; 0)                         6.91e-7/6.84e-7/6.61e-7 6.51e-7/6.84e-7/6.61e-7 1.92e-7/1.92e-7/1.85e-7 1.084e-6/1.074e-6/1.085e-6
    At equal budget against the 900 L row: 9000 L reads 1.01 / 1.06 / 1.01 (whole box), 1.25 to 1.27 (near P), 1.01 to
    1.02 (N_v r <= 1000) and 0.030 to 0.031 beyond r = 1000; 300 L reads 1.10 / 1.24 / 1.15, 1.36 to 1.38, 2.1 to 3.3 and
    33. So under the canonical law the three domains 300 L, 900 L, 9000 L give the same interior to a factor 1.4 near P
    (1.3 between 900 L and 9000 L), and the far band beyond r = 1000 is set by the extent of the fitted rows (3.5e-5,
    1.1e-6, 3.3e-8). The 90 L fit is not a full-plane approximate profile under the canonical law (3e-5 near P, 1.3e-2
    far): its interior agreement holds only with its closure. Proposal to the lead: one paragraph and this table in 4.4
    as "the domain columns read under the canonical law", replacing nothing; the closure readings stay as the
    sensitivity check they are. With it, G20 (b1) "three domains" is met by full-plane residuals (300 L, 900 L, 9000 L),
    which removes the blocking part of item 7; the 90 L column is then reported as failing under the canonical law.
 8. "systematic improvement". Partly valid. Each step of the angular row (m <= 100, 150, 200, 250) is a continuation
    with a further 20750 iterations, so cap and cumulative budget rise together; the matched comparisons (m <= 250 row
    against the budget row c6g2 at equal iterations: 0.97 to 1.00 whole box, 0.63 to 0.82 near P, 0.74 in J; 4.8) exist
    but the 4.1 sentence does not point to them. Fix: in 4.1 add "(each step also adds iterations; at equal iterations
    see 4.8)".
 9. Far-field labels. Valid (see G106 (a)): 4.4 lines 1005 to 1009 mix the A5 rise (0.23 to 0.44 percent) with
    all-column per-step ratios (0.995 to 1.003). Also line 1101 "no fit has rows" is false for the 9000 L domain row,
    whose rows reach 6.9e4 > 3.7e4; write "the candidate has no fit rows" (as lines 599 and 864 already do).
10. "upper bounds". Valid wording. Lines 842 and 848 call A5 maxima "upper bounds" because they may contain part of
    the evaluator floor; a sum of a residual and a floor need not exceed the residual. Suggested: "may be raised by the
    evaluator floor" / "floor-contaminated", not "upper bounds". Line 124 and line 1200 ("upper bounds on the cost")
    concern unrefitted offsets and are correct as written.
11. J over all labels (4.4b: "equals the supremum minus the infimum of J_eps over all labels on r = 20 to about 1e-8").
    Valid in the strict sense, immaterial numerically. On X3 lim_{X->0} R/rho = 3 c_l - psi_xy(0) - 1 = +9.8e-9 (my
    extra_checks: c_l 5.575362610642 from k, c = psi_xy(0) 15.726087822141, so 3 c_l - c - 1 = 9.78e-9; equivalently 3
    times the identity defect 3.26e-9 quoted in 4.1). Near the saddle the backward flow expands x at rate 2 c_l - 1 =
    10.15, so a label at angular distance d from the y-axis spends log(1/d)/10.15 + O(1) in the neighbourhood of 0 and
    J_eps(d) = J_axis + (9.6e-10) log(1/d) + O(1): unbounded as d -> 0. This is consistent with the report's family B:
    the labels within 1e-3 of the y-axis span -3.21e-7 to -3.24e-7 (predicted change over d from 1e-4 to 1e-3: 2.2e-9).
    To leave the sampled range (maximum 8.2e-7) d must be below about e^(-1190). Suggested text: "over all labels on
    r = 20 at distance at least 1e-4 from the axes; closer to the y-axis J grows like (3 c_l - psi_xy(0) - 1)
    log(1/d)/(2 c_l - 1), 9.6e-10 per factor e in d, and leaves the sampled range only for d below e^(-1190)". Also
    "through the origin" (the separatrix sentence) should be "past the origin": no characteristic through a point
    other than 0 reaches the stagnation point 0 in finite time.
12. "sine modes to n = 503" (line 885; also my own RUN_STATUS wording). Valid. exp(H) is not band-limited; H carries
    cos(2 m theta) for m <= 250, so rho has significant content to about n = 503 and a decaying tail beyond. Suggested:
    "its exponent carries angular frequencies to 500 (cos 2 m theta, m <= 250), beyond the 479 modes of 11250 x 384; the
    agreement of 16875 x 512 and 16875 x 768 is the aliasing check".
13. B_3 of the trial. CONFIRMED with numbers. SPEC D12 requires both the axis-data estimator and the trial's own
    coefficient; the report gives only the estimator (about 0.30). The trial's own coefficient of y^3 |x|^(p_3) at the
    origin is T(-1) L^(-p_3) (T the Chebyshev sum of the 6 fractional coefficients, z[-6:]); in the natural units of the
    estimator (B_3 x*^(p_3 - 2)):
      fxd1g, s2g, c6g (X3), c6h, c6g2, dom9000g   T(-1) = 1.64875 (fxd1g 1.64878), raw 5.503e-6, natural +0.0460
      c6hF                                        T(-1) = 1.64853, natural +0.0460
    The fit leaves the fractional coefficients essentially where construct1 / construct4 put them (G9: 1.648523 on
    c4_r1, natural 0.046). So the trial's own coefficient is +0.046 against the estimator's +0.30 (same sign, factor about
    6.5); by the D12 identity the remainder, about +0.25, is the finite-part jet-defect term f.p. int D/(w H). Request:
    report both in 4.2 / 4.8 with that sentence; the claim "nonzero B_3" (of the estimator) is unaffected.
    Correction of my G76 item 27: the X3 T coefficients are (-2.7682, 4.1136, 6.517, -0.4526, 1.4199, -0.1411), not
    (-1.12e-8, -2.768, ...), and T(-1) = +1.6487, not about -1.51 (I had sliced the coefficient vector one place early).
    The verdict there ("nonzero") stands; FINAL_REPORT never quoted -1.51.
14. Absolute residuals and manufactured fields. Absolute values: CONFIRMED and now fixed (G105, G106 (b)). Manufactured
    fields: partly valid. The report validates the inverse on the candidate itself (third evaluator, 52 points, 4.5) but
    does not cite the manufactured-solution tests: my evaluator on rho = x^2 y e^(-r^2) with closed-form psi gives
    max |R - R_exact| 6.8e-10, 2.7e-12, 2.8e-13 at N 400, 800, 1600 (T2, code/test_vresid1.py), and the numerics lane's
    Poisson and Newton tests (NUM_REPORT). Suggested: one sentence in 4.6 or 5 (d) citing them. Not blocking.
15. Definitions. D14 E and D2 are now defined (line 701 to 704, G106). Still valid: (i) E collides with the elliptic
    residual E of 4.4; rename the centre quantity (for example E_c) or say "the centre defect E (not the elliptic
    residual)"; (ii) the "objective" / "L2 objective" (4.1, 4.2, 4.8) is never defined. From the fit code it is the
    Euclidean norm of the weighted residual vector of the fit grid plus the auxiliary rows (gpu_long_solve.py: |s.fun(z)|),
    not a mean square. One sentence with the weights and the rows included is needed. Should fix.
16. "so the setting is not the limit" (line 724). Valid wording. Suggested: "so neither change of the solver setting
    lowers the objective materially at this budget".
17. Manifest. Partly valid: section 5 (a) describes the coefficient files but gives no file name or checksum for X3.
    Suggested: name and md5 of the candidate file (c6g_shape.npz, md5 15f8095f...) and of F3 in 5 (a). The objections
    to GPU use and 4.8 GB do not apply under the rules of this run (one GPU is allowed; the limit is 16 GB per process).
18. Waiver. The report says the 24 hour minimum "was waived as a gate by the instructions of this run" and records T0
    and T_end; that is accurate and sufficient. No change needed.
Verdict: 3, 4, 5, 6, 13 CONFIRMED (defects to fix: three statement conditions in section 3, one notation, one missing
quantity); 2, 8, 9, 10, 11, 12, 15, 16 valid wording or labelling fixes; 7 and 17 partly valid, with the canonical-law
domain table above as the proposed remedy for 7; 14 fixed for absolute values; 1 and 18 need nothing now. None of the
items changes a number of the candidate or the choice of X3. Status: OPEN until the lead applies (or answers) items 3 to
17. Items 3, 4, 5, 7 and 13 are required for the YES endpoint; the others are presentation.

## G104 (final, 2026-10-19T00:41:24Z). c6hF (free control at m <= 250) against c6h by the 12:02Z rule, for the record; lead NOTES 23:48:05Z item 3

Method: own generator, own inverse to R 7.652e6, own evaluator (runs/audit/c6h{,F}_<cfg>_R7.652e6.json at 16875 x 512,
16875 x 768, 22500 x 512; 11250 x 384 is below the mode content n = 503 of both and is not a row value); 857-label J
(code/vchar_dense.py, eps 0.03 / 0.01) at 16875 x 512 and 22500 x 512, both M 639 (runs/audit/c6h{,F}_N{16875,22500}_q512_
R7.652e6_jd2.json, scratch/jd2_ana.py); phase scan (scratch/phase_sup.py, four radial phases at 16875 x 512); BA5 at 16875 x 512;
extra_checks. Readings as fixed for the m <= 200 pair (G73 (g), G73 (h2), G74): whole-box N_f on N >= 16875, far band all
r > 1000 without the y-axis exclusion and with the spread over the configurations; A5 values given as well.
(a) Values, c6hF / c6h:
     quantity                               16875 x 512     16875 x 768     22500 x 512     configuration spread (c6h; c6hF)
     whole-box N_f, A5                      0.990           1.003           0.988           6.5e-8 = 15 percent; 6.3e-8
     whole-box N_f, all columns             0.778 (floor)   0.892 (floor)   1.013           4.4e-7; 4.6e-7
     N_v r <= 1000, A5                      0.992           1.006           0.988           1.9e-8 = 15 percent; 1.8e-8
     N_f within 0.5 of P                    0.947           0.966           0.889           6.9e-8 = 31 percent; 8.4e-8
     N_v r > 1000, all columns              0.9987          0.9964          0.9983          1.9e-8; 1.6e-8
     N_v r > 1000, A5                       0.9957          0.9965          0.9956          6.9e-10; 1.25e-9
     857-label J, eps 0.03                  1.019           -               1.023           3.8e-9 = 0.8 percent; 5.6e-9 = 1.1 percent
     857-label J, eps 0.01                  1.019           -               1.026           8.8e-9 = 1.5 percent; 1.32e-8 = 2.2 percent
   Absolute: whole-box A5 c6h 4.227e-7 / 4.270e-7 / 4.875e-7, c6hF 4.184e-7 / 4.285e-7 / 4.818e-7 (all at the lobe above P,
   r 8.72 to 8.74, theta 0.194); far all columns c6h 1.09572e-6 / 1.11442e-6 / 1.10055e-6, c6hF 1.09427e-6 / 1.11036e-6 /
   1.09873e-6; far A5 c6h 1.07858e-6 / 1.07903e-6 / 1.07927e-6, c6hF 1.07397e-6 / 1.07522e-6 / 1.07450e-6; J (eps 0.03)
   c6h 5.002e-7 / 5.040e-7, c6hF 5.099e-7 / 5.155e-7; J (eps 0.01) c6h 5.886e-7 / 5.974e-7, c6hF 5.999e-7 / 6.131e-7.
   Phase scan (16875 x 512): lobe 4.6549e-7 / 4.6636e-7 (0.998; per-map phase spreads 10.0 / 9.4 percent); near P (union and
   parabola windows) 2.4030e-7 / 2.4211e-7 (0.993; phase spreads 23.6 / 20.9 percent). BA5 (16875 x 512): 2 <= r <= 10 A5
   4.184e-7 / 4.227e-7; 10 <= r <= 100 A5 4.862e-8 / 3.824e-8 = 1.27 (one configuration only; a band 9 times below the
   whole-box maximum; the raw A4 HIGH 1.787 there is the floor column theta 1.5683). J at 16875 x 384 (M 479 < 503, flagged,
   not used): 1.030 / 0.958.
   Centre and c_l (c6hF): identity c_l 5.5763705524 (stored 5.5763705557, difference -3.2e-9 as on X3); c_l drift over the
   run -6.0e-7 (toward the fixed value; |drift| < 1e-4, no slope resolved); h(P) - 1 +4.39e-8 / -1.89e-8 at 16875 / 22500
   (c6h +3.19e-8 / -1.79e-8); W_1 on the x-axis vanishes only at x* 8.6008442; no open-quadrant cell; rel E / D2 at most
   4.59e-9; C at the axis 0.998 of c6h. GPU objective 5.2220e-7 against 5.2063e-7 (1.003).
(b) Rule, for the record (the pair is a refinement row, not a candidate: lead NOTES 15:14:26Z item 4). The fixed row c6h
   would win if its whole-box N_f were lower on every configuration with N >= 16875 and its other quantities not higher.
   Its whole-box N_f is lower only at 16875 x 768 (A5; all columns only at 22500 x 512), so by the letter of the rule the free
   control c6hF wins the pair. The deciding differences are 0.3 to 1.2 percent, inside both the configuration spread (15
   percent) and the radial-phase spread (9 to 10 percent) of that maximum, so the pair is not resolved in the deciding
   quantity. The other quantities point both ways: near P and in the far field c6hF is lower, in J c6h is lower.
(c) Answer to item 3. No: the pair does not differ by less than the configuration spread in every quantity of the rule.
   Inside the spread: whole-box N_f (A5 and all columns), N_v for r <= 1000, N_f within 0.5 of P, and the far N_v in the fixed
   reading (all columns: differences 1.5e-9 to 4.1e-9 against 1.6e-8). Beyond it: the 857-label J (c6h lower by 1.9 to 2.6
   percent against J spreads of 0.8 to 1.1 percent at eps 0.03 and 1.5 to 2.2 percent at eps 0.01; on the lead's 185 labels
   1.017, the same direction) and the far N_v with A5 (c6hF lower by 0.35 to 0.44 percent, 3.8e-9 to 4.8e-9 against A5
   spreads of 6.9e-10 and 1.25e-9). So the sentence "the fixed and the free c_l give the same residual to about 1 percent" is
   not supported. A wording these numbers support: "At m <= 250 and equal budget the free control (c_l 5.5763706) and the
   fixed row agree in the whole-box and r <= 1000 maxima to about 1 percent, with differences of both signs inside the
   configuration spread; the free control is lower next to P (by 3 to 11 percent, inside the phase spread of that maximum)
   and beyond r = 1000 (by 0.1 to 0.4 percent); the fixed row is lower in the 857-label J (by 2 to 3 percent, beyond the
   spread of J between configurations). By the selection rule the free control wins this pair on whole-box differences of
   about 1 percent, below the resolution of that maximum. The pair is a refinement row and does not change the candidate."
   The last two clauses (consistent with the c_l interval of 4 (iv); candidate unchanged, G74 decided at m <= 200) CONFIRMED:
   c6hF's c_l 5.5763706 lies inside the interval, and the candidate is read only from the m <= 150 and m <= 200 pairs.
(d) Same lens on the m <= 200 pair (G74), so that the two pairs are reported alike. With A5, F3's far N_v is lower than X3's
   by 4.5e-9 to 4.6e-9 (ratio X3 / F3 1.0042 to 1.0043) on each configuration with N >= 16875, where the A5 spreads are 2.2e-9
   (X3) and 2.1e-9 (F3); over all four configurations the F3 A5 spread is 1.0e-8 (11250 x 384: 1.0798e-6). G74 read the far
   band without A5 over the four configurations (fixed in advance, G73 (g)): difference at most 3e-9 against 2.4e-8, so
   G74's verdict and the candidate stand. FINAL_REPORT fad52bb2 lines 622 to 626 give only that reading. Requested (one
   clause, disclosure): "with the y-axis floor columns excluded the candidate is the higher by 4.5e-9 (0.4 percent) on each
   configuration with 16875 or more radial points, about twice the spread between those configurations". Both pairs show the
   same 0.4 percent far-field offset in favour of the free c_l.
Verdict G104: measurements CONFIRMED; lead's cross-check (pair within 0.992 to 1.014 on the lead's scans, J 1.017) agrees in
direction and size. Answer to item 3: NO (J and the A5 far band differ beyond the configuration spread); the wording in (c)
and the clause in (d) are requested. Neither changes the candidate. The team may NOT finish (G107, c6gR4 (47) open).

## G108 (2026-10-19T00:56:16Z). c6gR4 (chain 7 step 47: X3 continued 20750 iterations on its own rows r < 900 L, inverse domain and two-term closure at 1e4 L; not a candidate); lead NOTES 00:21:41Z items 2 to 4

Method: md5-checked copy (766635b1, as the chain line 00:10:38Z; keys R_shape 1e4, L 7.651424208, m <= 200); own generator
and own inverse. Formula convention (no closure, formula continued to R 7.652e6, k_self, bands 900 L-1000 L, 1000 L-9000 L,
9000 L-1e4 L, r > 1e4 L) at 16875 x 512 (M 639) and 22500 x 384 (M 479): runs/audit/c6gR4_<cfg>_R7.652e6_frm47.json, read
by the new scratch/c6gR4_read.py against X3's baselines _rb44r / _rb44 / _rb44s (same bands, same k_self, same
configurations) and dom9000g _frm44. Fit convention (closure at 1e4 L, VAUDIT_RFIT 900 L) at 11250 x 384, 16875 x 512,
22500 x 384, BA5 at 16875 x 512, 857-label J with the closure at 16875 x 384, residual map near P (closure, 16875 x 512):
interior against the budget row c6g2 (X3 + 20750 iterations on its rows, inverse at 1000 L). C at the axis: code/far1_ver.py,
nt 16384. Series next to the y-axis: scratch/far2_rel.py 32768 at theta 1.56811 (runs/far2/c6gR4_rel.txt).
(a) Far band, c6gR4 / X3, formula continued (N_v maxima; raw / A5):
     band              16875 x 512          22500 x 384          c6gR4 maximum at                  dom9000g / X3 (raw)
     900 L-1000 L      0.2194 / 0.2194      0.2187 / 0.2187      999 L, theta 1.563 / 998 L, 1.548  -
     1000 L-9000 L     0.2662 / 0.2729      0.2686 / 0.2706      4279 L / 4382 L, theta 0.643       0.0290 / 0.0278
     9000 L-1e4 L      0.2448 / 0.2486      0.2460 / 0.2469      9001 L / 9008 L, theta 0.643       0.0249 / 0.0250
     r > 1e4 L         0.2398 / 0.2443      0.2417 / 0.2433      1.00e4 L, theta 0.642              0.0351 / 0.0354
   Absolute 1000 L-9000 L: c6gR4 2.933e-7 / 2.938e-7 against X3 1.102e-6 / 1.094e-6 (raw). The maximum of c6gR4 is off the
   y-axis (theta 0.64), where X3's is in the column next to the axis; so the A5 values equal the raw ones for c6gR4.
   c6gR4 / dom9000g in 1000 L-9000 L: 9.17 / 9.68 (numerics' 9.1 in the common closure is the same order).
   Reading (in force, numerics 17:51:20Z item 4, thresholds 18:04:24Z item 5): 0.266 to 0.273 on both N >= 16875
   configurations, at most 0.5 on both: "falls". The inverse-domain change is part of the fall of the 9000 L row, and that
   row's gain (G91) is not attributable to its rows alone. CONFIRMED; the lead's cross-check (0.268 all columns, 0.272 A5,
   0.248, 0.241 at 24576 x 576 with the inverse to 1e6 L) agrees to 1 percent.
(b) C at the axis (my convention C = (c_l - 1)(Theta_1 forced - Theta_1 stored)): c6gR4 -4.4239e-4 against X3 +1.86871e-2,
   ratio -0.0237 (dom9000g +6.465e-4, 0.0346; c6g2 1.0026). V_r(pi/2) 89.33394 (X3 89.33392): the forced Theta_1 is unchanged,
   the stored one moved onto it. In the lead's convention -C / (c_l - 1): +9.669e-5 against -4.0843e-3, the lead's numbers.
   CONFIRMED.
(c) Series next to the y-axis (theta 1.56811), c6gR4 against X3 (ratio): q1 -4.296381e-4 against 1.582166e-2 (-0.0272);
   q2 -10.00988 against -88.78237 (0.1127); qh 782.1023 against 782.1024 (1.0000; fixed by k, L and the end values); q3
   -4.436201e4 against 1.190005e5 (-0.3728). Relative inconsistencies at orders 1, 2, 3: 2.6e-6, 0.10 percent, 12.6 percent
   (X3 9.6e-5, 0.88 percent, 22 percent; dom9000g 3.0e-6, 0.15 percent, 10 percent). The four terms at 4858 L: -7.6e-8,
   -3.2e-7, +5.7e-7, -2.5e-7, sum -7.5e-8 (lead: the same four values). CONFIRMED.
(d) Interior against c6g2 (same rows, same iterations, inverse at 1000 L), 11250 x 384 / 16875 x 512 / 22500 x 384:
   A5 whole box 6.989e-7 / 4.245e-7 / 4.892e-7, ratios 1.002 / 0.999 / 1.006 (maxima at the lobe above P, r 8.74, theta
   0.194; at 11250 x 384 the lobe of that grid, r 8.78, theta 0.31); within 0.5 of P 3.591e-7 / 3.624e-7 / 3.612e-7, ratios
   1.016 / 1.008 / 1.016; BA5 (16875 x 512) 0.1-2 1.004, 10-100 0.89, 100-1000 1.03; 857-label J (16875 x 384) 7.093e-7 /
   7.772e-7 at eps 0.03 / 0.01 against 6.724e-7 / 7.199e-7 (1.055 / 1.080). Residual map near P (16875 x 512, same
   grid): every window within 0.97 to 1.06 of c6g2's (window maximum 4.246e-7 against 4.249e-7 at the lobe; within 0.5 of P
   3.623e-7 against 3.594e-7; the omega 399 ripple amplitude 0.95 to 1.14 of c6g2's). h(P) - 1 +3.6e-7 / +4.9e-8 / -4.9e-9
   (grid error, as X3); identity c_l 5.5753626108 (stored 5.5753626106). So the interior does not see the inverse-domain
   change; dom9000g's interior changes against c6g2 (near P 1.25 to 1.27, J 1.35 to 1.42; G98 item 5) come with its rows
   (dom9000g / c6gR4 near P 1.24 to 1.25, J 1.28 / 1.31).
(e) The lead's prepared 4.5 text, checked. With <RB> = "0.27 (0.266 to 0.273 on the two configurations, with and without
   the y-axis columns)" and <RC> = "-0.024", every number is CONFIRMED. Two wording corrections:
   - "the larger inverse domain alone lowers it": the closure moved with the inverse domain, so write "the larger inverse
     domain with its closure, at the same rows and iterations, lowers it to 0.27 and removes C at the axis";
   - the decomposition should be stated, since it is measured: "the rows to 9000 L lower it by a further factor of 9 to 10
     (dom9000g / c6gR4 0.10 to 0.11), to 0.028 to 0.030 of X3's; C at the axis is already removed by the inverse domain
     (-0.024 against 0.035 for the 9000 L row)". Then "the fall of the 9000 L row is not attributable to its rows alone" is
     CONFIRMED as written.
   The 4.5 sentence "The inconsistencies are common to the fits with rows to 900 L (at second and third order 0.88 to 0.92
   percent and 22 to 23 percent next to the y-axis on six fits)" is now false without the qualifier: c6gR4 has rows to
   900 L and reads 0.10 percent and 12.6 percent. With "and the inverse domain at 1000 L" added it is CONFIRMED. The next
   sentence on the 9000 L row may add "and on the 900 L rows with the inverse domain at 1e4 L (C -0.024 of X3's; orders 1, 2,
   3: 2.6e-6, 0.10 percent, 13 percent)".
(f) Correction of my G98 item 4 wording ("the fall of the 9000 L row ... comes with its rows; the budget does not produce
   it"): the second half stands (c6g2 is 0.993 to 1.003 of X3); the first half is refined by (a) to (c): of the fall to 0.029,
   the inverse domain with its closure gives the factor 0.27 and all of C at the axis, the rows the remaining factor 0.10 to
   0.11. FINAL_REPORT fad52bb2 line 434 (timeline 23:07) quotes the G98 reading as it was; the 4.5 text above supersedes it,
   and a timeline line for c6gR4 is needed.
Verdict G108: CONFIRMED with the corrections in (e). The reading is "falls". c6gR4 changes neither the candidate nor the
interior values of X3 (the interior is insensitive to the inverse-domain change to 1 to 2 percent, J to 8 percent).

## G110 (2026-10-19T01:13:29Z). Diff audit FINAL_REPORT fad52bb2 -> 516a80a8 (lead NOTES 2026-10-19T01:01:34Z, 17 items)
Method. My copies: scratch/FR_fad5.md (fad52bb2) and scratch/FR_516a.md (516a80a8, md5 checked against lead/FINAL_REPORT.md
at 2026-10-19T01:13:29Z); the 677-line diff read in full. Each item checked against my G entries, my audit files (runs/audit), my code
(code/test_vresid1.py), the lead's and the numerics lane's code and logs (read only), and a direct derivation where marked.
One read-only subagent checked the objective, the GPU sentence and the environment (items 1, 7); its scratch file is
scratch/agent_tmp/check_objective.py (it rebuilt R/(|rho| + |X.grad rho|) x weight from the evaluate() fields and matched
s.fun to 2.5e-16 relative at 2048 x 96 and 2048 x 97 with fit radius 90). Another checked 4.6 against the numerics lane's
tests (item 15); its claims were re-read in NUM_REPORT.md and tests/ by grep.

 1. (*) Environment. python3 on this box: Python 3.9.25, numpy 2.0.2, scipy 1.13.1, sympy 1.14.0, torch 2.8.0+cu128 (CUDA
    12.8); CPU Intel Xeon Platinum 8275CL @ 3.00GHz; all 24 start events of the GPU logs name NVIDIA A100-SXM4-80GB. CONFIRMED.
    GPU sentence: gpu_long_solve.py (numerics/leadcode/gpu, md5 f26dde2d) runs on the GPU the products J v and J^T u inside
    LSQR, and also the LSQR vector updates and norms, the 24 random J^T probes of the column scaling and one diagnostic J v per
    check; the residual, the acceptance test (s.fun), the linearization (CentreDerivative) and the scalar Givens recurrences
    run on the CPU. "matrix-vector products inside LSQR" is correct; it is exact with "(with the LSQR vector updates and the
    column-scaling probes)". Optional precision, no correction needed. Side observation for the numerics lane's own artifact
    tree: numerics/artifacts/src/gpu/gpu_long_solve.py (md5 9f750eff) is gpu_long_solve_pre_invrad.py, without
    --inverse-radius (used by c6gR4 and step 50). The lead's assemble_artifacts.sh copies numerics/leadcode/gpu/*.py, where
    gpu_long_solve.py is the run version f26dde2d, so the lead's artifacts are not affected.
 2. R1, R7, R10, R11 (G107 items 3 to 5): CONFIRMED. Answer to the question: the A_2 bullet is correct without C^3. It needs
    rho in C^2 and W in C^2; A_2 gives rho in C^(2,alpha), so psi in C^(3,alpha) by Schauder and W in C^(2,alpha). On the
    x-axis: div W = 2 c_l gives w' + h = 2 c_l; the y-derivative of curl W = -d_x rho gives h' - 2 a2 = -g', so with
    h' = -w'' a2 = (g' - w'')/2; the y^1 coefficient of the equation gives w g' = (1 - h) g. The integral identities use
    g > 0 on (0, x*] (linear ODE, g = g0 x^2 (1 + O(x^(1+alpha))) at 0, and R5) and the integrability of 1/g - 1/(g0 x^2)
    = O(x^(-1+alpha)) at 0 (from g'/g = (1 - h)/w with w = -A x + O(x^(2+alpha))). a2' + 3 b3 = 0 uses a third
    y-derivative and is correctly placed in the A_3 bullet.
 3. Timeline 19:03 "No domain column run by then (90 L, 300 L) is higher ...": agrees with G86 (dom90g and dom300g were the
    only domain columns at 19:03; dom9000g ended at 20:21:48Z, chain log). CONFIRMED.
 4. Timeline 00:16, 00:32, 00:34, 00:41, 00:56: agree with G105, G106, G107, G104 (final) and G108 ("to 0.029" against
    0.028 to 0.030; "the factor 0.27 and all of C at the axis, the rows the remaining factor 0.10 to 0.11"). CONFIRMED.
 5. (ii) and the 4.1 paragraph on the trial's own coefficient.
    T(-1) list: recomputed from the stored fractional-power coefficients: 1.64875 on c6g, s2g, c6h, c6g2, dom9000g, c6gR4,
    dom90g, dom300g; 1.64878 on fxd1g; 1.64853 on c6hF and also on c6gF (F3); raw 5.5027e-6, natural +0.0460. CONFIRMED
    ("1.6485 on the free control of the m <= 250 row" holds for F3 as well; adding it is optional).
    Identity, derived directly (SPEC D12, a lead elementary item): with the trial's own axis data (w, h, a2, b3, g, G3) and
    the canonical velocity, w' + h = 2 c_l and h' - 2 a2 = -g' hold exactly, and the y^3 coefficient of the equation is
    D = T3 = w G3' + (3h - 1) G3 + a2 g' + b3 g. With H the solution of H'/H = (1 - 3h)/w, variation of constants gives
    G3 = H (const - int (a2 g' + b3 g)/(w H) dx + int D/(w H) dx), so the direct-form estimator from (w, h, a2, b3, g) equals the
    trial's own coefficient plus f.p. int_0^{x*} D/(w H) dx. CONFIRMED for that form. The closed form of R10,
    H = N g^(3+beta) |w|^(-beta), uses w g' = (1 - h) g, which the trial satisfies only to its y^1 defect T1 = w g' + (h - 1) g;
    the two differ by the factor exp(int (3 + beta) T1/(g w) dx), with no derivative of the defect, and the w-only estimators
    (code/vb3ibp.py, the lead's b3_ibp.py "orig") rebuild g from w through T1 = 0. Suggested clause after "homogeneous
    solution of R10": "(of the trial's own G_3 equation; the closed form of R10 equals it up to a factor set by the trial's
    defect in the y coefficient, which does not enter differentiated)". Optional; the statement is correct as an identity.
    4.8 wording: "so the trial does not itself contain the fractional term that its axis data indicate" reads as if the
    trial had no such term. Correction: "so the trial's own fractional term (+0.046) is about one sixth of the value its axis
    data indicate".
 6. (iv) "(the tested span of exponents admitting comparably accurate fits, not an enclosure of the exponent of an exact
    profile)": CONFIRMED (G107 item 2).
 7. (*) Objective definition, against numerics/leadcode/c7/centre_fit.py (the copy gpu_long_solve.py imports; the c6 copies
    differ only in hard-coding the fit radius 0.9 R) and stationary.py, solver.py: objective "log", entries
    res/(1 + |3 + H_theta|) = R/(|rho| + |X.grad rho|) (rho = x^2 y e^H > 0 off the axes); rows 1e-4 <= r < fit radius in
    units of L (strict upper bound; default 0.9 R = 900, --fit-radius FR sets R = FR/0.9); columns arange(0, nt+1, 2), both
    axes included for the even nt used; weight sqrt(14000/n) max(1, (0.04/r)^2) with n = rows x columns (pweight, aweight
    = 1 in every run configuration); extra entries 20 (h(P) - 1) (h(P) = d_y W_2 at the zero of W_1 on the x-axis), E_c and
    D2 with weight 1 (E_c = beta - 2 A delta, D2 = (4A + 2) gamma - 5 alpha, A = 2 c_l - 1: the 4.2 formulas); Euclidean
    norm, not squared. CONFIRMED. Two precisions, optional: at the axis nodes (rho = 0) the entry is the continuous
    extension of the quotient; in the objective E_c and D2 are evaluated by the fit's own discrete estimator (spline
    derivative at 0, moment at r = 1e-4), the formula of 4.2 with a different estimator from the evaluator's window fit.
    The log field "l2_unweighted" equals "actual" in all 2521 GPU check events (aweight = 1); it is the weighted norm.
    "Absolute values are reported too" and the rename E -> E_c with "E without index is the elliptic residual of 4.4":
    CONFIRMED.
 8. 4.1: rows not at equal total iterations; m <= 250 "on all evaluation columns" and "more than the spread between
    configurations" (c6h / c6g A5 far 1.003919, 1.002332, 1.004383, differences 4.2e-9, 2.5e-9, 4.7e-9 against spreads
    6.9e-10 and 2.2e-9); canonical-law sentence; "on X3 (52 points; 4.5)"; X3 / F3 A5 far "+4.5e-9 (0.4 percent) ... about
    twice the spread" (G104 (d)); "lobe of 4.3". CONFIRMED.
 9. 4.2: |cos(theta)| twice; parity sentence: rho even in x and odd in y gives d_x rho odd in x and odd in y, so psi under the
    canonical inverse is odd in x and in y; U_1 = -psi_y is odd in x, hence 0 on the y-axis; U_2 = psi_x is odd in y, hence 0
    on the x-axis; U(0) = 0 follows. Centre-jet line and the solver-setting sentence (G107 item 16). CONFIRMED.
10. 4.3: "Not in the table" additions; [OPEN] list; drift -6.0e-7 "toward it" (G104 final); "fixed-c_l states over 5.52 to
    5.71; those from 5.556 to 5.596 include both values" agrees with the 4.6 text. CONFIRMED.
11. 4.4: floor notes (G107 item 10); absolute values block; sup|d_x rho| = 20.0, sup|E| = 2.98e-5, 7.86e-6, 2.12e-6 (G106
    (b)); m <= 250 aliasing sentence (G107 item 12); far-band label (G106); H3 free-control paragraph (my G104 (c) wording);
    free branch 5.5763709, 5.5763712, 5.5763706. CONFIRMED.
12. 4.4 "Domain columns under the canonical law": the table is G107 item 7. On the question: yes. The stored R_shape is 100 L,
    333.3 L, 1000 L and 1e4 L for the fits with rows to 90 L, 300 L, 900 L and 9000 L (dom90g, dom300g, c6g2, dom9000g),
    i.e. the inverse domain is the fit radius / 0.9 with the two-term closure beyond it (code: load_shape sets R = FR/0.9;
    c6gR4 is the exception, rows to 900 L and inverse at 1e4 L, and it is described as such in 4.5). CONFIRMED.
13. 4.4b: "at distance at least 1e-4 from the axes", the growth of J_eps next to the y-axis (9.6e-10 per factor e; 3 c_l -
    psi_xy(0) - 1 = 9.8e-9; d below e^(-1190)), "past the origin": G107 item 11. CONFIRMED.
14. 4.5. "the candidate has no fit rows" (beyond 900 L): CONFIRMED. "6.5e-7 to 7.2e-7 (N_f)": my c6g audits within 0.5 of
    P give 6.505e-7, 6.841e-7, 7.157e-7, 6.605e-7, 6.832e-7 (11250 x 384, 16875 x 512, 16875 x 768, 22500 x 384, 22500 x
    512). CONFIRMED. Correction: the N_v range in the same sentence (report line 1278) must include the same 16875 x 768
    configuration: N_v within 0.5 of P is 1.821e-7, 1.917e-7, 2.006e-7, 1.851e-7, 1.914e-7, so "1.8e-7 to 2.0e-7 (N_v)", not
    "1.8e-7 to 1.9e-7". Manufactured test: c_l = 1.3, max |R - R_exact| 6.8e-10, 2.7e-12, 2.8e-13 at 400, 800, 1600 radial
    points, max |R_exact| = 0.485, max |E| 1e-10 / 3e-12 / 7e-12 (at most 1e-10), psi_xy(0) - 1/8 = -6e-14 (exact value 1/8
    since p2 = r^2/16 + O(r^4)): T2 of this report. CONFIRMED. c6gR4 texts: my G108 (e) wording and numbers. CONFIRMED.
    (*) "to 2 percent in the whole-box maximum and within 0.5 of P and to 8 percent in J (0.89 at 10 <= r <= 100 on one
    configuration)": G108 (d) has A5 whole box 1.002 / 0.999 / 1.006 and within 0.5 of P 1.016 / 1.008 / 1.016, J 1.055 /
    1.080 (eps 0.03 / 0.01) and BA5 10-100 0.89 at 16875 x 512. CONFIRMED.
15. 4.6 (*). CORRECTION (attribution). The quoted component tests are of the numerics lane's compactified discretization,
    not of the disk least-squares discretization that the paragraph describes: tests/test_poisson.py imports ipm1
    (IPM1.poisson_modes, the compactified inverse; NUM_REPORT line 48 "N=128,M=16: 3.4e-15, 2.1e-14") and tests/test_newton.py
    imports ipm1 and solve (solve.Newton); the disk discretization is src/ipm1disk.py and src/ipm1lsq.py (tests/test_lsq.py),
    which share helpers with ipm1 only. The disk's own checks in NUM_REPORT: its inverse against the compactified Poisson
    solve on a smooth test density, relative velocity error on r <= 5 of 1.0e-6, 5.3e-8, 2.2e-9 at R = 100, 300, 1000 and
    psi_xy(0) to 3e-7, 2e-8, 7e-10 (lines 166 to 168); the exact Jacobian against finite differences, 5e-9 to 4e-7 relative
    per column (line 306). I found no manufactured Newton test of the disk solver. Proposed text: "Its full-plane inverse was
    validated against the compactified Poisson inverse of the same lane (itself exact to 3.4e-15 on the manufactured psi =
    ..., gamma = 0.6, L = 1.3, at 128 x 16 nodes): relative velocity difference on r <= 5 of 1.0e-6, 5.3e-8 and 2.2e-9 at
    R = 100, 300 and 1000, psi_xy(0) to 3e-7, 2e-8 and 7e-10; its Jacobian agrees with finite differences to 5e-9 to 4e-7
    relative per column." Precisions if the compactified numbers stay: 3.4e-15 is the maximal error of the rescaled stream
    function (velocity 2.1e-14); 128 x 16 is N = 128 (N + 1 radial points) and M = 16 angles per quadrant; U(0) = 0 holds by
    construction; the Newton 3e-15 is the residual |F|_inf of the compactified solver (N 24, M 6, L 1, c_l* 1.6). Reruns by
    the subagent: 3.89e-15 and 1.25e-14 at 128 x 16, Newton |F| 2.22e-15.
16. 4.7: "|E_c|" and "and the same fits read under the canonical law". CONFIRMED.
17. Section 5 (a): md5 c6g_shape.npz 15f8095f7e79dbfa0c50d75e5fe8997a and c6gF_shape.npz 0398af3f08a2a4f75e42c846edbaa375 in
    my copies, in lead/work/c6 and in numerics/leadcode/gpu; E -> E_c twice; "the m <= 250 row and its free control".
    CONFIRMED as text. The artifact tree lead/artifacts is dated 2026-10-18T10:42Z and does not yet contain c6g, c6gF,
    any GPU fit or the GPU driver; notes/assemble_artifacts.sh (rebuild from scratch; work/c6/*_shape.npz into (a),
    numerics/leadcode/gpu/*.py into b_fit_gpu) makes (a) and (b) true once it is run (lead plan item 4). I will check md5s
    in the assembled tree (c6g, c6gF, gpu_long_solve.py f26dde2d) at the final pass.

Verdict G110: 516a80a8 CONFIRMED in content, with two corrections: item 15 (the 4.6 component tests belong to the
compactified discretization; replacement text above) and item 14 (N_v within 0.5 of P "1.8e-7 to 2.0e-7"); one wording
correction in 4.8 (item 5); optional precisions in items 1, 5 and 7. None changes a number of the candidate, the choice of
X3 or the reading of any row.

## G109 (2026-10-19T01:15:46Z). Row 37 fxm2g (fixed c_l at d = -2e-3 on 375 x m <= 150; chain step 37) by the lead rule of NOTES 2026-10-19T00:25:51Z
Run. fxm2g: F0 + d t transplant (start fxm_-2.0e-03_shape.npz, md5 a39a2c70...), --fix-cl, 20480 x 720, inner 2500, check 250,
damping 1e-8, 21500 iterations (step 37 23:39:43Z to 00:38:32Z); end shape md5 5ac32e3170621f73cce85698613aa9b4, copied to
runs/gen4/gpu/fxm2g_shape.npz with the md5 checked against the chain line (j41, 00:39:13Z); R_shape 1000 L, angular cap 150,
stored c_l 5.574363148663909. Reference F2 = seg3g (free, same lineage, basis, grid; budget 750 + 20750) and X2 = s2g (d = -1e-3).
Method. My evaluator (code/gen_audit.sh, own differentiation and own full-plane inverse to 7.652e6 = 1e6 L, formula
continued) at N11250 q384 M 479 and N16875 q512 M 639; seg3g and s2g re-audited on the same two configurations in the current
format with the A5 regions (scratch/jA5.sh, files *_a5.json, 01:02:31Z to 01:13:41Z, rc 0). 857-label J at N16875 q384 with
the profile q0 (jset, no closure); code/extra_checks.sh at N11250 q384; code/far1_ver.py (C at the axis); the L2 objective is
the last check value "actual" in numerics/leadcode/gpu/<tag>/<tag>.log. Profile table by scratch/fx_profile.py.

Result (ratio to F2 in brackets; configurations N11250 q384 / N16875 q512):
  d       row     L2 objective          whole-box N_f (A5)            N_v r <= 1000 (A5)          h(P) - 1
  -2e-3   fxm2g   3.944751e-6 (0.926)   1.3616e-6 / 1.3678e-6 (0.865 / 0.869)   3.800e-7 / 3.821e-7 (0.865 / 0.869)   +2.83e-7 / +1.05e-8
  -1e-3   s2g     4.096686e-6 (0.962)   1.4238e-6 / 1.4347e-6 (0.905 / 0.911)   3.975e-7 / 4.005e-7 (0.905 / 0.911)   +2.15e-7 / +1.55e-8
   0      seg3g   4.258616e-6 (1)       1.5738e-6 / 1.5748e-6               4.394e-7 / 4.395e-7               +1.54e-7 / +1.97e-8
  857-label J (eps 0.03 / 0.01): fxm2g 2.9533e-6 / 3.2310e-6 (0.865 / 0.859), s2g 3.1434e-6 / 3.4620e-6 (0.921 / 0.920), seg3g
  3.4137e-6 / 3.7628e-6. C at the axis: +0.0187733, +0.0189229, +0.0187975.
  Every whole-box maximum is within 0.5 of P (equal to the near-P maximum; N_f maxima at r 8.41 to 8.47, theta 0.0098, on all six audits), so
  whole-box, A5 and near-P N_f coincide on these three rows. Last 1000 iterations: -0.145, -0.143, -0.145 percent (flattened by the 2 percent test). Iterations in the
  logs: 21500, 20750, 20750 (the lead counts the 750 free iterations before seg3g into F2's budget).
  fxm2g extra checks (N11250 q384): identity c_l 5.5743631455 (stored 5.5743631487, -3.2e-9); h(P) 1.000000062 at x* 8.5992899;
  c_l from h(P) = 1 at fixed rho 5.574363088 (-5.8e-8); one zero of W_1 on the x-axis (8.59929), none of W_2 on the y-axis
  (min W_2/y = 5.5746 at y 7.5e6), no open-quadrant cell with both components changing sign; min |W|/(c_l |X|) 0.0216, 0.0065,
  0.0027 within 1, 0.3, 0.1 of P; centre jet E_c, D2 relative to their terms at most 1.70e-8 and 8.1e-9 over five windows;
  8 p4/r^4 = -0.131580 (relative variation 3.3e-6 over 2e-3 <= r <= 0.02) and 4(p2 - c r^2/2)/r^4 within 6e-5 of -1/3 there.
  The lead's scans (NOTES 01:07:09Z: 1.385e-6, 1.444e-6, 1.585e-6) give the same ratios to 1 percent (0.874, 0.911).

Reading by the 00:25:51Z rule. (a): L2 within 30 percent of F2's (0.926), whole-box N_f (A5) within 30 percent on each
configuration (0.865, 0.869), |h(P) - 1| <= 1e-6 (2.8e-7, 1.1e-8): all hold. (b) would need near-P N_f >= 2 x F2's; it is 0.87.
Verdict: row 37 is (a), "not determined at this level". CONFIRMED. By SPEC v4.5 it widens the quoted c_l interval of (iv) down
to 5.5743631. The profile at equal budget is monotone over d = -2e-3, -1e-3, 0 in every measured quantity (L2 0.926, 0.962, 1;
whole-box 0.87, 0.91, 1; J 0.86, 0.92, 1): the objective is still falling toward smaller c_l at d = -2e-3, so the lower end
of the tested span is not bracketed by this row (rows 52, 53 requested in NOTES 01:07:09Z; my set is scratch/j52.sh).

## G111 (2026-10-19T01:38:00Z). Row 38 fxu2g (fixed c_l at d = +2e-3 on 375 x m <= 150; chain step 38) by the lead rule of NOTES 2026-10-19T00:25:51Z
Run. fxu2g: F0 + d t transplant (start fxu_+2.0e-03_shape.npz, md5 e4f451ca...), --fix-cl, 20480 x 720, inner 2500, check 250,
damping 1e-8, 21500 iterations (step 38 00:38:32Z to 01:24:02Z); end shape md5 55937d343186869e3cc02618784a1dae, copied to
runs/gen4/gpu/fxu2g_shape.npz with the md5 checked against the chain line (j41); stored c_l 5.578363148128243.
Method. As G109 (same evaluator, configurations N11250 q384 M 479 and N16875 q512 M 639 with the A5 regions, J at N16875 q384,
extra checks at N11250 q384, far1_ver, scratch/fx_profile.py); audits 01:25:25Z to 01:37:02Z, every rc 0.

Result (ratio to F2 = seg3g in brackets; N11250 q384 / N16875 q512):
  d       row     L2 objective          whole-box N_f (A5)                      N_v r <= 1000 (A5)                  h(P) - 1
  +2e-3   fxu2g   4.590838e-6 (1.078)   1.7913e-6 / 1.7921e-6 (1.138 / 1.138)   5.008e-7 / 5.012e-7 (1.140 / 1.140)   +8.23e-8 / +2.20e-8
  857-label J (eps 0.03 / 0.01): 3.9561e-6 / 4.3632e-6 (1.159 / 1.160). C at the axis +0.0186955 (seg3g +0.0187975).
  Whole-box maximum = near-P maximum, at r 8.484 / 8.493, theta 0.0098 (0.11 left of P on the x-axis side). N_v beyond r = 1000
  1.102e-6 at r 3.2e4 (unfitted far field, as on every row). Last 1000 iterations -0.150 percent (flattened).
  Extra checks (N11250 q384): identity c_l 5.578363145 (stored 5.578363148, -3.2e-9); h(P) 0.999999896 at x* 8.6023866; c_l
  from h(P) = 1 at fixed rho 5.578363241 (+9.6e-8), dh/dc_l 1.078; one zero of W_1 on the x-axis, none of W_2 on the y-axis
  (min W_2/y = 5.5786 at y 7.5e6), no open cell; min |W|/(c_l |X|) 0.0216, 0.0065, 0.0024 within 1, 0.3, 0.1 of P; centre jet
  E_c, D2 relative at most 2.0e-8 over five windows; 4(p2 - c r^2/2)/r^4 within 2.0e-5 of -1/3 for 2e-3 <= r <= 0.02 (3e-6 for
  r >= 5e-3).

Reading by the 00:25:51Z rule. (a): L2 within 30 percent of F2's (1.078), whole-box N_f (A5) within 30 percent on each
configuration (1.138, 1.138), |h(P) - 1| <= 1e-6 (8.2e-8, 2.2e-8): all hold. (b) would need near-P N_f >= 2 x F2's; it is 1.14.
Verdict: row 38 is (a), "not determined at this level". CONFIRMED. It widens the quoted c_l interval of (iv) up to 5.5783631.
Profile at equal budget over d = -2e-3, -1e-3, 0, +2e-3, monotone increasing in d in every quantity: L2 0.926, 0.962, 1,
1.078; whole-box N_f 0.87, 0.91, 1, 1.14; J (0.03) 0.865, 0.921, 1, 1.159. The squared objective L2^2 (units 1e-12) 15.561,
16.783, 18.136, 21.076 is convex in d; the quadratic through the first three predicts 21.24 at +2e-3 (measured 21.08, 0.8
percent lower). This is a statement about fits at one budget from transplanted starts; it does not locate an exponent.

## G112 (2026-10-19T01:40:07Z). SPEC v4.10 to v4.12 (md5 863e060d; diff against my copy of v4.6, scratch/SPEC_00ed.md; copy scratch/SPEC_v412.md)
Method. diff; the v4.12 D12 correction rederived by hand; the row c_l values read from the GPU logs ("cl" of the last check line).
(a) v4.10 and v4.11 (section 8 reading rules for rows 37 to 40, 52, 53, the Q settlement, c6h9000; G105 presentation item):
  identical in content to lead NOTES 00:25:51Z items 2, 3 and 01:07:09Z, which I applied in G109 and G111 before reading the
  results. One factual precision: v4.10 writes the row exponents as c_l = 5.5763624 + d. The transplants F0 + d t carry
  c_l = 5.5763624 + d + 0.18 d^2 to the digits shown (stored values: d = -8e-3 5.5683739, -4e-3 5.5723653, -2e-3 5.5743631,
  +2e-3 5.5783631, +2.4e-2 5.6004662). The difference is 7e-7 at |d| = 2e-3 but 1.04e-4 at d = +2.4e-2 (5.6004662 against
  5.6003624). The report and the interval of (iv) must quote the stored values. CONFIRMED with this precision.
(b) v4.12 D12 correction. With rho = g y + G3 y^3 + O(y^5) on the x-axis, W_1 = w + a2 y^2 + ..., W_2 = h y + b3 y^3 + ...,
  w' + h = 2 c_l (div U = 0, exact for every trial), trial defects T1 = w g' - (1 - h) g and T3 at order y^3, and
  beta = 2/(2 c_l - 1): H = N g^(3+beta) |w|^(-beta) gives H'/H = (3 + beta) g'/g - beta w'/w = (1 - 3h)/w + (3 + beta) T1/(g w),
  using beta (1 - 2 c_l) = -2. The homogeneous solution of w G3' + (3h - 1) G3 = 0 has H_h'/H_h = (1 - 3h)/w, so H/H_h =
  exp((3 + beta) int_0^x T1/(g w) dt) as stated. With G3 = H phi: w H phi' = (source) + T3 - (3 + beta)(G3/g) T1, so the
  defect is D = T3 - (3 + beta)(G3/g) T1 as stated, and R10's formula on trial data equals B_own plus the finite part of
  int_0^{x*} D/(wH), under the stated conditions (g > 0 on (0, x*], g(x*) > 0, even expansions at 0). Near x*, w ~ w'(x*)(x - x*)
  and H_h ~ |x - x*|^((1 - 3h(x*))/w'(x*)), which blows up when h(x*) > 1/3 (w'(x*) = 2 c_l - h(x*) > 0), so lim G3/H_h = 0 for
  bounded G3. CONFIRMED. It agrees with the factor I gave in G110 item 5 (optional precision). No change of standard or criterion.
Verdict G112: SPEC v4.12 CONFIRMED, with the precision (a) on the stored row exponents.

## G113 (2026-10-19T01:51:55Z). Diff audit FINAL_REPORT 516a80a8 -> 5c15c44d (lead NOTES 2026-10-19T01:23:32Z, items 1 to 6)
Method. diff of scratch/FR_516a.md (= lead/notes/FINAL_REPORT_516a.md, md5 516a80a8) against the new file (copy
scratch/FR_5c15.md, md5 5c15c44d, 1486 lines); 7 hunks, all at the places named; sources NUM_REPORT section 2, my G110, G112;
item 5 by hand (below) and on my X3 axis traces (runs/gen4/c6g_traces.npz, from my generator and inverse at N11250 q384).
 1. 4.6: the replacement text of G110 item 15 with the precisions "3.4e-15 in the rescaled stream function and 2.1e-14 in
    the velocity ... N = 128 radial and 16 angular nodes per quadrant": NUM_REPORT section 2 lists N=128, M=16: max |Psi~ err|
    3.4e-15, relative velocity error on r <= 5 2.1e-14, and its angular grid is M nodes on the open quadrant. The dropped
    phrases (Newton 3e-15, U(0) = 0 exactly) belonged to the compactified solver. CONFIRMED.
 2. 4.5: "1.8e-7 to 2.0e-7" (N_v within 0.5 of P), the only occurrence. CONFIRMED.
 3. 4.8 "about one sixth" (0.046 against 0.30); 4.1 T(-1) list "(1.6485 on F3 and on the free control of the m <= 250 row)"
    (my G110: 1.64853 on c6gF and c6hF). CONFIRMED.
 4. Section 0 GPU sentence (G110 optional item 1). CONFIRMED.
 5. B_3 identity with R10's H. (a) Identity: with F_3 = -a2 g' - b3 g (SPEC D12), T_1 = w g' + (h - 1) g, T_3 = w G_3' +
    (3h - 1) G_3 + a2 g' + b3 g and H = N g^(3+beta) |w|^(-beta), H'/H = (1 - 3h)/w + (3 + beta) T_1/(g w) (G112 (b)), so
    w H (G_3/H)' = w G_3' + (3h - 1) G_3 - (3 + beta)(G_3/g) T_1 = T_3 + F_3 - (3 + beta)(G_3/g) T_1, that is
    -F_3/(w H) = -(G_3/H)' + (T_3 - (3 + beta)(G_3/g) T_1)/(w H), as written. w' + h = 2 c_l and a2' + 3 b3 = 0 are the
    y^0 and y^2 coefficients of div(c_l X + U) = 2 c_l on the x-axis. CONFIRMED.
    (b) Conditions on X3. g = rho_y(x, 0) = x^2 exp(H(x, 0)) for every trial of the formula (the fractional term carries
    sin^2 t and vanishes on the axis), so g > 0 on (0, x*] and g/x^2 = exp(H(|x|, 0)) is even and analytic near 0 within
    the first knot interval (q and chi are analytic in r^2) for every trial, not only X3. |w|/x is even by parity (w is odd
    in x). On my X3 traces: w < 0 on [1e-3, 8.5] (max -1.0e-2 at x = 1e-3, where w is about (1 - 2 c_l) x), one zero of W_1 on the x-axis at x*
    (extra checks, G74), so |w| > 0 on (0, x*) and H = infinity at x* (G_3/H -> 0 there); polynomial fits of |w|/x on
    [1e-3, X], X = 0.02, 0.05, 0.1, degrees 4 to 6: 10.1507 - 0.2325 x^2 + 2.0e-3 x^4 with the x and x^3 coefficients
    1e-9 and at most 1.5e-4, falling with the window and the degree (fit noise; misfit <= 2e-12), a0 = 2 c_l - 1 to the
    digits shown. CONFIRMED.
    (c) The 4.1 remark text (lines 733 to 740), (ii) and 4.8 "the trial's defects in the y and y^3 coefficients of the
    equation on the x-axis": agree with (a), (b). "for a profile T_1 = T_3 = 0 and H is the homogeneous solution": with
    T_1 = 0, H/H_h is constant (G112 (b)). CONFIRMED. No value changed in these hunks.
 6. Timeline 01:13 (G110), 01:15 (G109), 01:16 (external audit of item 5; the conditions quoted are those of (b)): agree
    with my entries. CONFIRMED.
Verdict G113: 5c15c44d CONFIRMED (items 1 to 6). Still [OPEN] in the file: T_end and elapsed (section 0), later timeline
entries, the (iv) interval and the 4.3 / 5 lists of the fixed-c_l rows (rows 37, 38 read: G109, G111; 39, 40, 52, 53 to
come). When the rows are entered, the stored exponents of G112 (a) are to be used.

## G114 (2026-10-19T02:45:29Z). Row 39 fxv24g (fixed c_l at d = +2.4e-2 on 375 x m <= 150; chain step 39) by the rule of NOTES 00:25:51Z, and the Q rule (item 3)
Run. fxv24g: F0 + d t transplant (start fxv_+2.4e-02_shape.npz, md5 0da3b3b0...), --fix-cl, 20480 x 720, inner 2500, check
250, damping 1e-8, 21500 iterations (step 39 01:24:02Z to 02:31:56Z, in parallel with step 52 from 01:29Z); end shape md5
f0b98ad7d780f0baffc990f577287be4, copied with the md5 checked against the chain line (j41, 02:32:32Z); stored c_l
5.600466164352696 (my identity value 5.600466161).
Method. As G109 and G111; audits 02:32:33Z to 02:44:53Z, every rc 0.

Result (ratio to F2 = seg3g in brackets; N11250 q384 / N16875 q512):
  d        row      L2 objective          whole-box N_f (A5)                      N_v r <= 1000 (A5)                  h(P) - 1
  +2.4e-2  fxv24g   8.671252e-6 (2.036)   4.5870e-6 / 4.5895e-6 (2.915 / 2.914)   1.287e-6 / 1.287e-6 (2.928 / 2.927)   -1.07e-6 / -2.45e-7
  857-label J (eps 0.03 / 0.01): 9.7995e-6 / 1.1053e-5 (2.871 / 2.938). C at the axis +0.0180677 (seg3g +0.0187975).
  Whole-box maximum = near-P maximum (r 8.536 / 8.528, theta 0.0098; P at x* 8.6195). N_v beyond r = 1000 1.081e-6 at r 3.2e4.
  Last 1000 iterations -0.486 percent, last 250 -0.091 percent (flattened by the 2 percent test).
  Extra checks (N11250 q384): identity c_l 5.600466161 (stored 5.600466164, -3e-9); h(P) 0.999999312 at x* 8.6194830; c_l
  from h(P) = 1 at fixed rho 5.600466802 (+6.4e-7); one zero of W_1 on the x-axis, none of W_2 on the y-axis (min W_2/y =
  5.6007), no open cell; min |W|/(c_l |X|) 0.0215, 0.0065, 0.0025 within 1, 0.3, 0.1 of P; centre jet relative at most
  2.8e-8 over five windows.

Reading by the 00:25:51Z rule. (a) fails (L2 2.036 > 1.3; whole-box 2.91). (b): flattened (-0.49 percent over the last 1000
iterations) and N_f within 0.5 of P 2.915 and 2.914 times F2's on the two configurations (>= 2 on each): both hold.
Verdict: row 39 is (b), "excluded at this level" (375 x m <= 150, 21500 iterations from F0 + d t). CONFIRMED. It does not
widen the interval of (iv); the upper end of the tested span lies between 5.5783631 (row 38, (a)) and 5.6004662, with row
40 (d = +3e-3) to come.
Q rule (NOTES 00:25:51Z item 3, SPEC v4.10): Q(375) = 8.671252e-6 / 4.259e-6 = 2.036. (P2) needs Q >= 2.96, (P1) needs Q <=
0.91; 2.036 is between, so the reading is "undecided" (the 2-percent-per-250 clause is not needed: -0.09 percent). Within the
fixed rules, 4.8 says the test does not separate the two pictures at this level. CONFIRMED as computed.
Observation (not a rule): at 4.3 times the |d| of rows 37 and 38 beyond their side, the near-P and J ratios (2.9) are larger
than the L2 ratio (2.04). At this budget the L2 objective increases with c_l over every row read so far (d = -2e-3 to
+2.4e-2), and its growth from +2e-3 (1.078) to +2.4e-2 (2.036) is consistent with the convexity in d of G111.

## G115 (2026-10-19T02:57:03Z). Row 52 fxn4g (fixed c_l at d = -4e-3 on 375 x m <= 150; chain 8 step 52) by the rule of NOTES 01:07:09Z (= 00:25:51Z (a) / (b) / (c))
Run. fxn4g: F0 + d t transplant (start work/c6/fxn_-4.0e-03_shape.npz, md5 16ecb489...), --fix-cl, 20480 x 720, inner 2500,
check 250, damping 1e-8, 21500 iterations (step 52 01:29:03Z to 02:40:41Z, in parallel with steps 39 and 40); end shape md5
9d5ddd3a89d904d4d539c0eb37ebf4b4, copied with the md5 checked against the chain line (j52, 02:41:49Z); stored c_l
5.572365299328851 (my identity value 5.572365296).
Method. As G109 (scratch/j52.sh: same audit set); audits 02:41:50Z to 02:56:35Z, every rc 0.

Result (ratio to F2 = seg3g in brackets; N11250 q384 / N16875 q512):
  d       row     L2 objective          whole-box N_f (A5)                      N_v r <= 1000 (A5)                  h(P) - 1
  -4e-3   fxn4g   3.654235e-6 (0.858)   1.1194e-6 / 1.1225e-6 (0.711 / 0.713)   3.123e-7 / 3.135e-7 (0.711 / 0.713)   +3.62e-7 / -1.8e-10
  857-label J (eps 0.03 / 0.01): 2.4123e-6 / 2.6314e-6 (0.707 / 0.699). C at the axis +0.0187831.
  Whole-box maximum = near-P maximum (r 8.414 / 8.458, theta 0.0098; P at x* 8.5977). N_v beyond r = 1000 1.10e-6 / 1.11e-6
  at r 3.2e4. Last 1000 iterations -0.187 percent (flattened). The L2 objective went below row 37's final value (3.944751e-6)
  after 10000 iterations, so row 53 runs (chain 8, from 02:40:41Z).
  Extra checks (N11250 q384): identity c_l 5.572365296 (stored 5.572365299, -3e-9); h(P) 1.000000142 at x* 8.5977429; c_l
  from h(P) = 1 at fixed rho 5.572365165 (-1.3e-7); one zero of W_1 on the x-axis, none of W_2 on the y-axis (min W_2/y =
  5.5726), no open cell; min |W|/(c_l |X|) 0.0217, 0.0065, 0.0029 within 1, 0.3, 0.1 of P; centre jet relative at most
  1.6e-8 over five windows.

Reading. (a): L2 within 30 percent of F2's (0.858), whole-box N_f (A5) within 30 percent on each configuration (0.711,
0.713), |h(P) - 1| <= 1e-6 (3.6e-7, 1.8e-10): all hold. Verdict: row 52 is (a), "not determined at this level". CONFIRMED.
It widens the quoted c_l interval of (iv) down to 5.5723653.
Profile at equal budget (21500 or 20750 iterations), ratios to F2:
  d          c_l (stored)   L2      whole-box N_f (2 configs)   J (0.03 / 0.01)    reading
  -4e-3      5.5723653      0.858   0.711 / 0.713               0.707 / 0.699      (a)
  -2e-3      5.5743631      0.926   0.865 / 0.869               0.865 / 0.859      (a)
  -1e-3 X2   5.5753626      0.962   0.905 / 0.911               0.921 / 0.920      (X2)
   0    F2   5.5763709      1       1                           1                  (F2)
  +2e-3      5.5783631      1.078   1.138 / 1.138               1.159 / 1.160      (a)
  +2.4e-2    5.6004662      2.036   2.915 / 2.914               2.871 / 2.938      (b)
The objective is still falling toward smaller c_l at d = -4e-3, and the whole-box and J ratios fall faster there than
between -2e-3 and 0 (0.71 against 0.87). The lower end is not bracketed by this row; row 53 (d = -8e-3) is running.
These are fits from transplanted starts at one budget; they do not locate an exponent.

## G116 (2026-10-19T03:11:41Z). SPEC v4.13 (md5 6dd7feda; diff against my copy of v4.12, scratch/SPEC_v412.md; copy scratch/SPEC_v413.md)

Method: diff of the two files. Result: two hunks, the version line and the section 8 v4.10 item, which now quotes the row
exponents as stored (5.5743631, 5.5783631, 5.6004662 at d = -2e-3, +2e-3, +2.4e-2; 5.5723653, 5.5683739 at -4e-3, -8e-3),
the values I recomputed in G112 (a) from 5.5763624 + d + 0.18 d^2 and read from the shapes (G109, G111, G114, G115). The log
line says "No change of standard", which the diff confirms. Verdict: CONFIRMED.

## G117 (2026-10-19T03:11:41Z). Check of the astra answer astra/clprof (question scratch/q/clprof.md: what separates (P1) and (P2), whether the 4.1 sentence is defensible, whether the monotone row profile undermines existence)

The answer is a claim to check. Item by item:

(1) "A fully minimized free objective cannot exceed a fixed-exponent minimum in the same trial space; F2's worse performance
    shows that its exponent is not selected by completed minimization." Method: I compared the stored configurations of
    seg3g (F2) and the rows (seg3g_shape.npz.long.json against fxn4g and fxu2g): the only differences are fix_cl, the start,
    the wall-clock cap and max_its (21500); probes, weights, grid 20480 x 720, inner 2500, check 250 and damping 1e-8 are
    the same, and the basis is the same 375 x m <= 150. From seg3g.log the free c_l stays in [5.5763641, 5.5763716] over
    the 20750 iterations (it starts at F0's 5.5763624), while at the same budget the fixed rows at 5.5723653, 5.5743631
    and 5.5753626 (X2) end at 0.858, 0.926 and 0.962 of F2's objective. Result: the claim holds for this budget: the free
    iteration did not move c_l toward the lower objective, so F2's exponent is set by its start at this budget and is not a
    minimiser of the objective. CONFIRMED. The report already says the free-continuation spread "measures how weakly the
    residual pins c_l; it is not an uncertainty interval" (5c15c44d, line about 880), which is consistent; the words "the
    free branch" (lines about 865, 879, 1144) must not be read as a selected exponent, and once the rows are entered the
    report should state that fixed-c_l fits below F2's exponent reach a lower objective at equal budget than F2 (condition
    (C2) of the endpoint statement).
(2) The predicted signatures (P1: R_h(c) = O(eps_h) at each fixed c; P2: R_h(c) about kappa |c - c*| + O(|c - c*|^2 + eps_h),
    floors at wrong c exposed by refinement) are the standard ones and conditional on the stated hypotheses (consistent
    approximation, transverse isolated solution). Our rows are at a single discretization and budget, so neither signature
    is tested; the near-linear fall of L2 in d over [-4e-3, +2e-3] is compatible with both (with c-dependent constants
    under (P1), or |c - c*| larger than the discretization width under (P2)). CONFIRMED as stated; it agrees with G114
    (Q = 2.036, undecided).
(3) The discriminating experiment (fixed-exponent fits at several separated exponents through nested discretizations,
    warm-started, budgets large enough to estimate the optimisation error) is not in the team's data: every row is at
    375 x m <= 150 and K = 21500, and the angular sequence 150 / 200 / 250 mixes approximation and budget. I agree with
    the answer that this is the experiment that would separate (P1) and (P2); it is a gap to be named in section 5, not a
    defect of what is reported.
(4) Proposed 4.1 wording: "X3 is an approximate profile with independently sampled normalized residuals of order 1e-6,
    satisfying the imposed scalar and jet constraints to the reported tolerances. These results provide numerical evidence
    consistent with existence of an admissible P_2 profile. They do not establish proximity to an exact profile or
    determine its exponent. Under the isolated-profile interpretation, the exact exponent may lie outside the tested span.
    This is not a proof." I adopt its content as condition (C1) of my endpoint statement; the residual size quoted must be
    the measured one (near-P N_f about 7e-7, whole-box and far band about 1.1e-6, my G-entries).
(5) Judgement "promising numerical evidence for existence, substantial uncertainty about the exponent, insufficient support
    for an unqualified strong claim of nearby admissible existence": this is an opinion, not a checkable claim. It agrees
    with my reading of the data (G115: the objective at this budget decreases toward the lowest tested exponent; the far
    band attribution and the regularity at P are measured, not proved).
The answer's last line records that a second consultation failed for lack of credentials; that has no bearing on the
content. Verdict: items (1) to (3) CONFIRMED; (4) adopted as a condition; (5) recorded as an opinion.

## G118 (2026-10-19T03:48:06Z). Row 40 fxu3g (fixed c_l at d = +3e-3 on 375 x m <= 150; chain 6 step 40) by the rule of NOTES 2026-10-19T00:25:51Z

Data: GPU chain line "2026-10-19T03:32:54Z step 40 done", 21500 iterations, md5 40584466fe24712f2f66af4fb38d6f6d; my copy
runs/gen4/gpu/fxu3g_shape.npz has the same md5 (j41 log 03:34:23Z). Stored c_l 5.579364045 (5.5763624 + d + 0.18 d^2 =
5.5793640; G112 (a)). Method: my generator and evaluator (gen_audit) at N11250 q384 M479 and N16875 q512 M639, R = 7.652e6,
regions with A5; 857-label J at N16875 q384 (jset); extra_checks at N11250 q384; far1_ver; table scratch/fx_profile.py.
Results (configurations N11250 q384 / N16875 q512; ratios to F2 = seg3g on the same configurations):
- L2 objective 4.748455e-6 = 1.115 x F2's 4.258616e-6; change over the last 1000 iterations -0.182 percent (flattened).
- Whole-box N_f (A5) 1.9087e-6 / 1.9112e-6 (1.213 / 1.214); the same with all columns. Maximum next to P on the x-axis side
  left of it (r 8.484 / 8.470, theta 0.0098), so the near-P maximum equals the whole-box maximum.
- N_v for r <= 1000 (A5) 5.336e-7 / 5.340e-7 (1.214 / 1.215); N_v beyond r = 1000: 1.086e-6 / 1.096e-6 (all columns), the
  far band of every row (1.06e-6 to 1.11e-6 over the rows read), not moved by c_l.
- h(P) - 1 = +5.46e-8 / +1.86e-8. Identity c_l 5.579364042 (3e-9 below the stored value); the c_l root of h(P) = 1 at fixed
  rho 5.579364147 (+1.06e-7); x* 8.6031614 (both configurations to 1e-9). Parity defect 2.4e-13, D10 relative defect 1.3e-9.
- J (857 labels, N16875 q384): 4.1801e-6 at eps 0.03, 4.6132e-6 at eps 0.01 (1.224 / 1.226). C at the axis +0.0186450.
Reading: L2 within 30 percent (1.115), whole-box N_f within 30 percent on each configuration (1.213, 1.214), |h(P) - 1| <=
5.5e-8 <= 1e-6: (a) "not determined at this level". Verdict: CONFIRMED. The interval of (iv) now contains [5.5723653,
5.5793640] (row 53 pending for the lower end); 5.6004662 is excluded at this level (G114).
Profile at equal budget, by stored c_l: L2 / F2 = 0.858, 0.926, 0.962, 1, 1.078, 1.115, 2.036 at d = -4e-3, -2e-3, -1e-3, 0,
+2e-3, +3e-3, +2.4e-2; whole-box N_f / F2 (N16875 q512) 0.713, 0.869, 0.911, 1, 1.138, 1.214, 2.914. Both increase with c_l
over every row read; the upper end of the not-excluded range lies between 5.5793640 and 5.6004662 at this level and is not
located further by these rows.

## G119 (2026-10-19T04:01:07Z). Row 53 fxn8g (fixed c_l at d = -8e-3 on 375 x m <= 150; chain 8 step 53) by the rule of NOTES 00:25:51Z item 2, and the bracket statement of NOTES 03:13:52Z item 3

Data: GPU chain line "2026-10-19T03:41:15Z step 53 done", 21500 iterations, md5 1489e81e0d43b3c54a1e470fb5b12a5d, the same
md5 as my copy runs/gen4/gpu/fxn8g_shape.npz. Stored c_l 5.568373894 (5.5763624 + d + 0.18 d^2 = 5.5683739). Method as G118
(gen_audit N11250 q384 M479 and N16875 q512 M639, R = 7.652e6, A5 regions; jset J at N16875 q384; extra_checks; far1_ver;
scratch/fx_profile.py). Results (N11250 q384 / N16875 q512; ratios to F2 on the same configuration):
- L2 objective 3.157027e-6 = 0.741 x F2 (0.771 x X2); change over the last 1000 iterations -0.442 percent (flattened).
- Whole-box N_f (A5) 8.906e-7 (0.566) / 6.730e-7 (0.427), the same with all columns. At N11250 q384 the maximum is at r 8.784,
  theta 0.3011, the off-axis lobe point above P that G73 (h) showed to be under-resolved by my N11250 radial grid; at N16875
  q512 the maximum is on the x-axis side at r 8.031, theta 0.0123 (0.56 left of P). Within 0.5 of P: 6.537e-7 (0.415) /
  6.684e-7 (0.424).
- N_v for r <= 1000 (A5) 2.472e-7 (0.563) / 1.990e-7 (0.453); beyond r = 1000 1.106e-6 / 1.120e-6 (the common far band).
- h(P) - 1 = +4.50e-7 / +2.74e-8. Identity c_l 5.568373891 (3e-9 below the stored value); the c_l root of h(P) = 1 at fixed rho
  5.568373772 (-1.19e-7); x* 8.5946518. Parity defect 2.3e-13, D10 relative defect 1.35e-9, B_3 IBP median 0.2978 [0.2963, 0.2984].
- J (857 labels, N16875 q384) 1.3244e-6 at eps 0.03, 1.4122e-6 at eps 0.01 (0.388 / 0.375). C at the axis +0.0188820.
Reading by the letter of item 2: (a) needs the whole-box N_f within 30 percent of F2's on each configuration; it is 0.566 and
0.427 times F2's, outside the 30 percent band on the LOW side (the row is better than F2 by more than the band); (b) fails
(near-P N_f 0.415 / 0.424 of F2, not >= 2). So the reading is (c) "undecided at the 375 x m <= 150 level after 21500
iterations". The rule did not anticipate a row below the band; (a) and (c) both widen the interval (SPEC v4.5: every tested
value that is not excluded), so the outcome for (iv) is the same. Verdict: CONFIRMED as (c); the interval of (iv) now contains
[5.5683739, 5.5793640]. My predictions recorded before the result (WORKLOG 02:58Z: 0.708 linear, 0.737 quadratic in L2, 0.745
quadratic in L2^2) bracket the measured 0.741.
Bracket statement (NOTES 03:13:52Z item 3): the L2 objective of 53 is below 52's (3.157027e-6 < 3.654235e-6) and its whole-box
N_f is below 52's on both configurations (8.906e-7 < 1.1194e-6; 6.730e-7 < 1.1225e-6). The lower end of the tested span is
not bracketed by row 53.
Comparison with the candidate X3 (m <= 200, c_l 5.5753626) on the same configurations, for the report's 4.1 / 4.3 statements
(the bases differ, so this is a fact about two fits, not an equal-basis comparison): whole-box N_f 1.289 (N11250 q384, both
maxima at the lobe point) / 0.984 (N16875 q512); within 0.5 of P 1.005 / 0.977; N_v r <= 1000 1.288 / 1.038; J 0.954 (eps
0.03) / 0.882 (eps 0.01); far band 1.015 / 1.017. So on the finer configuration a fit on the smaller basis m <= 150 at c_l
5.5683739 has whole-box and near-P N_f maxima 2 percent below the candidate's and a smaller J. The report must not say or
imply that the candidate's exponent or basis gives the smallest residual maxima among the fits computed.
Profile at equal budget (stored c_l; whole-box N_f at N16875 q512): d = -8e-3, -4e-3, -2e-3, -1e-3, 0, +2e-3, +3e-3, +2.4e-2:
L2 / F2 = 0.741, 0.858, 0.926, 0.962, 1, 1.078, 1.115, 2.036; N_f / F2 = 0.427, 0.713, 0.869, 0.911, 1, 1.138, 1.214, 2.914;
J / F2 (eps 0.03) = 0.388, 0.707, 0.865, 0.921, 1, 1.159, 1.224, 2.871. The residual maxima fall faster than the L2 objective
toward lower c_l on this interval.

## G120 (2026-10-19T04:03:44Z). Endpoint statement (lead NOTES 2026-10-19T01:01:34Z, end: "Please state, when rows 37-40 are read, whether in your judgement the YES endpoint for P_2 meets the standard as written in 4.1 and section 0")

Rows 37 to 40 are read (G109, G111, G114, G118), and 52 and 53 (G115, G119). Rows 54 and 55 (NOTES 03:13:52Z, 03:46:06Z)
can change only the numbers of condition C3 below, and the nested pair 56 / 57 (NOTES 03:54:45Z) only the wording of C4.
The standard is the one in FINAL_REPORT 4 (Conventions) and my G20 (b1) to (b4), G25 (a), agreed before any candidate.

Judgement. In my judgement the YES endpoint for P_2, stated as numerical evidence and not as a proof, meets the standard as
written, on the conditions C1 to C8 below. I will confirm DONE only after auditing the text that carries them. Item by item
(my measurements unless marked):
(1) Residuals (G20 (b1)). X3 on my generator and inverse: whole-box N_f 6.8e-7 to 7.2e-7 on the configurations with 16875
    or more radial points, the maximum next to P; N_v at most 2.0e-7 (2.5e-7 without the y-axis column exclusion) for r <=
    1000 and 1.10e-6 in the far field beyond the inverse domain, where X3 has no fit rows (G74, G75, G76, G96, G104, G110).
    Both axes, the neighbourhood of 0 and of P are in the regions read. Absolute values: G105, G106. MET.
(2) Three resolutions and three domains with systematic improvement (G20 (b1)). Angular cap m <= 100 / 150 / 200 / 250 at the
    fixed c_l, each prescribed diagnostic decreasing (G89, G90, G96; the m <= 250 step lowers the interior by 0.33 to 0.74 and
    leaves the far band 0.2 to 0.4 percent higher); radial 215 / 244 / 302 / 375 on the free fits; evaluator 11250 / 16875 /
    22500 radial and 384 / 512 / 768 angular points. Domains 300 L / 900 L / 9000 L agree within 0.5 of P to a factor 1.4
    under the canonical law at equal budget and their far bands follow the extent of their rows (G107 item 7); 90 L fails that
    reading and is reported as such. MET by the rules fixed before the runs; the angular rows are not at equal iterations
    (stated in 4.1).
(3) c_l, x*, h(P) (G20 (b2)). (i) Identity to 3.2e-9 with my psi_xy(0) on X3 and to 3e-9 on every row. (ii) The fitted
    values are stable along each computed branch (free fits 5.5763709 / 5.5763712 / 5.5763706 at m <= 150 / 200 / 250; X3
    fixed). (iii) The c_l root of h(P) = 1 at fixed rho agrees with the identity to about 1e-7 on X3 and on every row; x* of X3
    is 8.6000638 to 2e-10 over my four configurations. (iv) The numerics spread 5.5728 to 5.5823 must be reported (C7). MET as
    written. But the residual does not determine the exponent at this level: every tested value in [5.5683739, 5.5793640] is
    not excluded, 5.6004662 is excluded (G114), the L2 objective and the residual maxima at equal budget decrease toward the
    lowest tested exponent, and the lower end is not bracketed by 53 (G119). Also, at equal budget and identical objective
    the free fit F2 keeps its c_l within 1e-5 of its start while fixed fits below it reach a lower objective (G117 (1)), so no
    computed c_l is a minimiser of the objective [overstated; corrected in G129 (1): so at this budget F2's c_l is set by its
    start, not by a minimum of the objective]. Hence "stable c_l" (PROMPT line 111) holds for the fitted values along the
    branches, not for the exponent of an exact profile, and the report must say so (C3).
(4) Far-field truncation and inverse errors quantified separately: 4.5 (G81 to G93, G98, G108). MET.
(5) J reported and decreasing under refinement: the angular row (G89, G90, G96). MET.
(6) Independent check paragraph (G20 (b4)): one construction family, separately written evaluator and inverse, a third
    evaluator for the velocity at 52 points, no second converged solver (4.6, 4.7). To be checked in the final text (C8).

What the evidence supports, and what it does not. It supports: an explicit trial density X3 with sampled normalized
residuals below 1e-6 next to P and in the interior, decreasing under the angular refinement at its fixed c_l, reproduced by
separately written code, satisfying the identity, h(P) = 1 and the centre jet to the stated tolerances. It is numerical
evidence consistent with the existence of an admissible P_2 profile. It does not establish the proximity of an exact
profile to X3 in any norm, nor the exponent: under (P2) the exact exponent may lie below the tested span, under (P1) the
computed fits may belong to a family; the rows at one level do not separate the two (G114 Q rule, G117 (2)). Fits at a
lower c_l on a smaller basis reach residual maxima at or below X3's on one configuration (G119), so X3's exponent and basis
are not distinguished by the residual. The far-field N_v band of X3 lies in its unfitted continuation.

Conditions before DONE:
C1 4.1: the "numerical evidence that an exact profile of P_2 exists near rho_h" sentence replaced by the G117 (4) content with
   the measured sizes (accepted, lead NOTES 03:46:06Z item 5).
C2 4.3: every fixed-c_l fit below F2's exponent reaches a lower L2 objective than F2 at equal budget; F2's c_l range over its
   iterations; "free branch" names the free fits, not a selected exponent (accepted, same item).
C3 (iv) and the 4.3 list: the rows entered with their stored exponents and readings as measured (G109, G111, G114, G115,
   G118, G119, and 54 / 55 if read before the presentation pass); the interval of (iv) contains every tested value not
   excluded (at present [5.5683739, 5.5793640]), 5.6004662 excluded at this level; whether the lower end is bracketed, by the
   rule of NOTES 03:46:06Z item 4; the statement that the objective and maxima decrease toward lower c_l over the tested
   span; and the G119 comparison (a fit at 5.5683739 on m <= 150 has whole-box N_f 0.984 of X3's at 16875 x 512 and J 0.95 /
   0.88 of X3's), so the report neither says nor implies that X3 has the smallest residual among the fits computed.
C4 4.8 and section 5: (P1) and (P2) are not separated; the discriminating experiment (fixed exponents through nested
   discretizations, G117 (3)) named as not done, or as one step done if 56 / 57 are read by the rule of NOTES 03:54:45Z.
C5 STATUS DRAFT banner replaced (G107 item 1); no [OPEN] placeholder left; T0 = 2026-10-17T17:37:12Z, T_end and the elapsed
   time recorded as measured.
C6 Artifacts assembled with the md5s on file (c6g_shape.npz 15f8095f, c6gF_shape.npz 0398af3f, gpu_long_solve.py f26dde2d),
   checked by me in the final tree.
C7 The numerics spread 5.5728 to 5.5823 (G20 (b2)(iv)) reported as a variant spread.
C8 My diff audit of the version that goes to DONE (every number against the G-entries; no proof language for numerics).
Weak points the report must name (most are already in it): c_l only an interval with the lower end open; maxima are
budget-limited values for the basis, not converged limits; one construction family and no second converged solver; the
far band beyond the fit rows; regularity at P measured, not proved; the strong setting (a smooth) not answered (B_3 != 0
on the computed branch, G20 (a)).
Verdict: the YES endpoint for P_2 (numerical evidence, not a proof) is CONFIRMED as meeting the standard as written, subject
to C1 to C8; DONE is OPEN until C1 to C8 are verified in the final text.

## G121 (2026-10-19T04:07:38Z). Location of the whole-box N_f maximum on every audited fit (lead NOTES 2026-10-19T04:02:23Z item 2: the sentence "on every row the whole-box maximum of N_f is the maximum next to P" restricted to the rows where it holds)

Method: scratch/wb_loc.py on my audits (gen_audit, R = 7.652e6, A5 region 'all,ya>=0.006'; the _a5 re-audits for s2g and
seg3g). For each fit and configuration: the argmax (r, theta) of N_f, its distance to P = (x*, 0), and whether it equals the
maximum over |X - P| < 0.5 (and over |X - P| < 2). The value with all columns ('all') has the same argmax on every line.
Result (N11250 q384 / N16875 q512):
- Within 0.5 of P on both configurations (distance 0.12 to 0.21, on the x-axis side, theta 0.0074 to 0.0164): F3 = c6gF,
  X2 = s2g, F2 = seg3g, rows 37 fxm2g, 38 fxu2g, 39 fxv24g, 40 fxu3g, 52 fxn4g.
- X3 = c6g: at N16875 q512 within 0.5 of P (r 8.5277, theta 0.0074, distance 0.096); at N11250 q384 NOT: the maximum
  6.909e-7 is at r 8.784, theta 0.3076 (distance 2.67 from P), the off-axis lobe point that G73 (h) showed to be
  under-resolved by my N11250 radial grid; the maximum within 0.5 (and within 2) of P there is 6.505e-7.
- Row 53 fxn8g: on neither configuration. N11250 q384: at the same lobe point (r 8.784, theta 0.3011, distance 2.61),
  8.906e-7, against 6.537e-7 within 0.5 of P. N16875 q512: 6.730e-7 at r 8.031, theta 0.0123, distance 0.573 from P on the
  x-axis side (left of P), inside |X - P| < 2 but outside 0.5; the maximum within 0.5 of P is 6.684e-7 (0.7 percent lower).
Verdict: CONFIRMED as stated. The sentence holds, on configurations with 16875 or more radial points and with "next to P"
meaning within 0.5 of P, for every audited fit except row 53 (distance 0.573). On N11250 q384 it fails for X3 and row 53
(lobe point, a grid artifact of that configuration). If the report keeps "within 0.5 of P" as the meaning of "next to P",
it must exclude 53 on both configurations; with "within 2 of P" and N >= 16875 it holds for every audited fit. Rows 54, 55,
56, 57 will be given with their entries.

## G122 (2026-10-19T04:10:39Z). SPEC v4.14 to v4.16 (md5 ef79c2d7; diff against my copy of v4.13, scratch/SPEC_v413.md; copy scratch/SPEC_v416.md)

Method: diff of the two files; each change compared with the NOTES entry it cites and with the GPU chain log times.
Result: three changes, all in section 8 (the v4.10 item and one new item) and the version list:
- v4.14 (03:14:02Z): row 54 at 5.5604082 (d = -1.6e-2), run only if L2(53) < L2(52), the rule of NOTES 00:25:51Z, and the
  verifier's below-the-preceding-row statement for 53 and 54. Matches NOTES 03:13:52Z item 3. Fixed before 54 started
  (chain line 03:41:15Z).
- v4.15 (03:46:06Z): row 55 at 5.5524653 (d = -2.4e-2), run only if L2(54) < L2(53); bracketed only if L2 and whole-box N_f
  of the lowest row are above the next row's on both configurations. Matches NOTES 03:46:06Z. Row 55 has not started.
- v4.16 (03:55:00Z): the nested pair 56 / 57 on m <= 200 and its reading. Matches NOTES 03:54:45Z item 3 in substance; two
  points of wording: (1) it cites "NOTES_FOR_TEAM 2026-10-19T03:55:00Z", the NOTES heading is 03:54:45Z; (2) "flattened and
  Q_200 >= 3.05: isolated; Q_200 <= 1.36: family; otherwise undecided" can be read as not requiring flattening for the family
  branch; the NOTES text ("otherwise, or if 56 has not flattened: undecided") requires it for both, and I read 56 by the
  NOTES text (scratch/ns_profile.py). Neither 56 nor 57 has started.
Each item says "No change of standard", which holds: the standard of 4.1 / section 0 and the reading rules already applied
are unchanged; the additions fix readings of new rows before their runs.
Verdict: CONFIRMED, with the two wording points (1), (2) to be fixed in the next version or carried as read by the NOTES text.

## G123 (2026-10-19T05:03:17Z). Row 54 fxn16g (fixed c_l at d = -1.6e-2 on 375 x m <= 150; chain 8e step 54) by the rule of NOTES 00:25:51Z item 2, the bracket statement (NOTES 03:13:52Z item 3, SPEC v4.15), the X3 comparison and the location of the maxima (NOTES 04:02:23Z item 2)

Data: GPU chain line "2026-10-19T04:46:54Z step 54 done", 21500 iterations, md5 65d87bb7c4aa2be6c17263a033fc38c5, the same
md5 as my copy runs/gen4/gpu/fxn16g_shape.npz (runs/audit/jS.log 04:47:58Z). Stored c_l 5.56040821 (5.5763624 + d + 0.18 d^2
= 5.5604082). Method as G118 / G119 (gen_audit N11250 q384 M479 and N16875 q512 M639, R = 7.652e6, A5 regions; jset J at
N16875 q384; extra_checks; far1_ver; scratch/fx_profile.py, scratch/wb_loc.py). Results (N11250 q384 / N16875 q512; ratios
to F2 on the same configuration):
- L2 objective 2.737838e-6 = 0.643 x F2; change over the last 1000 iterations -1.721 percent (flattened by the 2 percent test,
  but not by much). My prediction recorded before the result (WORKLOG 04:08Z): 0.62 to 0.75; lead heuristic 0.633.
- Whole-box N_f (A5) 1.1271e-6 (0.716) / 7.630e-7 (0.485), the same with all columns. At N11250 q384 the maximum is at the
  under-resolved lobe point (r 8.766, theta 0.3109, 2.69 from P; G73 (h)); at N16875 q512 it is within 0.5 of P (r 8.5626,
  theta 0.0098, distance 0.088). Within 0.5 of P: 7.684e-7 (0.488) / 7.630e-7 (0.485).
- N_v for r <= 1000 (A5) 3.141e-7 (0.715) / 2.144e-7 (0.488); beyond r = 1000 (all columns) 1.141e-6 / 1.162e-6.
- h(P) - 1 = +6.90e-7 / +7.38e-8. Identity c_l 5.560408209 (the stored value to 1e-9); the c_l root of h(P) = 1 at fixed rho
  5.560408263 (+5.4e-8); x* 8.5884804, the only zero of W_1 on the x-axis; no zero of W_2 on the y-axis; no open-quadrant
  cell. Parity defect 2.4e-13, D10 relative defect 1.35e-9, B_3 IBP median 0.2969 [0.2952, 0.2984] / 0.2964 [0.2938, 0.2989].
- J (857 labels, N16875 q384) 1.7539e-6 at eps 0.03, 1.9658e-6 at eps 0.01 (0.514 / 0.522). C at the axis +0.0195301.
Reading by the letter of item 2: (a) fails (L2 0.643 and whole-box N_f 0.716 / 0.485 of F2, below the 30 percent band); (b)
fails (near-P N_f 0.488 / 0.485 of F2). Reading (c) "undecided at the 375 x m <= 150 level after 21500 iterations".
Verdict: CONFIRMED as (c); the interval of (iv) now contains [5.5604082, 5.5793640].
Bracket statement (54 against 53): the L2 objective of 54 is BELOW 53's (2.737838e-6 < 3.157027e-6); its whole-box N_f is
ABOVE 53's on both configurations (1.1271e-6 > 8.906e-7 at N11250 q384, both at the lobe point; 7.630e-7 > 6.730e-7 at
N16875 q512), and so are its N_f within 0.5 of P (7.684e-7 > 6.537e-7; 7.630e-7 > 6.684e-7) and its J (1.7539e-6 >
1.3244e-6; 1.9658e-6 > 1.4122e-6). By SPEC v4.15 the lower end is not bracketed by 54 (L2 still falls); row 55 is running
(chain line 04:47:28Z). Among the tested rows the residual maxima (whole-box N_f, near-P N_f, J) are smallest at row 53
(5.5683739), while the L2 objective still decreases at 5.5604082. So the G119 sentence "the residual maxima fall faster than
the L2 objective toward lower c_l" holds on [5.5683739, 5.5763624] only; the report must not say that the maxima decrease
toward the lowest tested exponent.
Comparison with X3 (m <= 200, c_l 5.5753626; different bases, a fact about two fits): whole-box N_f 1.631 / 1.115; within 0.5
of P 1.181 / 1.115; N_v r <= 1000 1.636 / 1.119; far band beyond r = 1000 1.047 / 1.055 (all columns; A5 1.041 / 1.051); J
1.263 (eps 0.03) / 1.227 (eps 0.01). Row 54 is above X3 in every one of these maxima on both configurations (and in L2:
2.738e-6 against 1.619e-6, on different bases).
Location for the report's sentence (G121): row 54 joins X3 (within 0.5 of P at N16875 q512, the lobe point at N11250 q384).
Profile at equal budget (stored c_l; whole-box N_f at N16875 q512): d = -1.6e-2, -8e-3, -4e-3, -2e-3, -1e-3, 0, +2e-3,
+3e-3, +2.4e-2: L2 / F2 = 0.643, 0.741, 0.858, 0.926, 0.962, 1, 1.078, 1.115, 2.036; N_f / F2 = 0.485, 0.427, 0.713, 0.869,
0.911, 1, 1.138, 1.214, 2.914; J / F2 (eps 0.03) = 0.514, 0.388, 0.707, 0.865, 0.921, 1, 1.159, 1.224, 2.871.
G120 C3 amended by this entry: the interval of every non-excluded tested value is now [5.5604082, 5.5793640] (rows 55 to 57
may widen it), and "the decreasing objective and maxima" reads "the L2 objective decreasing to the lowest tested row; the
residual maxima smallest at 5.5683739 among the tested rows, with row 54 above row 53 in whole-box N_f, near-P N_f and J".

## G124 (2026-10-19T05:14:33Z). The C7 sentence for 4.6 (lead NOTES 2026-10-19T05:03:21Z item 2) against NUM_REPORT 3.12; lead scans of row 54 (item 1)

Method: the sentence compared number by number with the LM table of numerics/NUM_REPORT.md section 3.12 and its text.
Result:
- "started from an early trial of the global trial construction (c_l 5.5763) projected onto its grids": the table's start is
  construct1 (c_l 5.5763219, x* 8.60088), projected by cubic interpolation of log a. Correct.
- "end at c_l between 5.5728 and 5.5823 on grids 128 x 32 to 320 x 80 with R = 1000 to 10000": the nine rows other than
  R = 30000 have c_l 5.58134, 5.57869, 5.57944 (L = 20), 5.57278, 5.57688, 5.58022, 5.57864, 5.58233, 5.57993; minimum
  5.57278, maximum 5.58233; grids (128,32) to (320,80); R 1000, 3000, 10000. Correct.
- "without convergence under refinement": 3.12 says c_l "does NOT converge with resolution at the LM floor (5.5813, 5.5787,
  5.5802, 5.5823)" at R = 1000. Correct.
- "variant spread, not an error bound": correct description.
- "attributes the spread to a nearly free far-field direction; the attribution is a hypothesis, not verified": 3.12 bases the
  attribution on one SVD of the Jacobian at the (192,48) LM state (smallest singular value 1.3e-7 against 8.8e3, c_l
  component -0.065, 89 percent of the right singular vector in r > 10). "Not verified" is accurate for an independent check
  (I have not reproduced it); the sentence would be more precise as "rests on one singular-value computation of that
  workstream and is not independently verified". Suggestion, not a condition.
- The R = 30000 row (c_l 5.6311, marked unreliable for radial resolution in 3.12) is left out without mention. Condition for
  C7: the sentence says that one run at R = 30000, marked unreliable by that workstream, is not included (otherwise a reader
  of NUM_REPORT finds a value outside the stated range).
Lead scans of row 54 (item 1; not readings): h(P) - 1 = -2.5e-8 (32768 x 640), -1.7e-8 (24576 x 960); mine +6.90e-7 at
N11250 q384 and +7.38e-8 at N16875 q512, falling with my radial resolution as in G73; consistent at the grid error. B_3 orig
median 0.2957 (lead) against my orig medians 0.3011 [0.2927, 0.3082] and 0.3029 [0.2907, 0.3132] (IBP 0.2969, 0.2964): inside
my ranges.
Verdict: C7 numbers CONFIRMED; C7 met when the excluded R = 30000 row is mentioned.

## G125 (2026-10-19T05:51:10Z). dom9000gF (chain 7d step 48: F3 = c6gF continued 20750 iterations, FREE c_l, fit rows r < 9000 L, inverse and two-term closure at 1e4 L, 24576 x 960; a DATA row, not a candidate) by the reading of lead NOTES 2026-10-18T20:41:00Z item 2

Run: GPU chain "2026-10-19T05:26:29Z step 48 done", outer 9 it 750 = 20750 iterations, objective 1.366938e-6 on its rows;
md5 cc1a5517 (my copy matches, jS.log 05:27:27Z). Shape: R_shape 1e4, angular 200, L 7.6520559, stored c_l 5.5763696769.
Method as G91 (j48: own convention with the closure at N11250 q384, N16875 q512, N22500 q384, VAUDIT_RFIT 9000 L, k_self,
band regions; formula-continued _frm48 at N16875 q512 and N22500 q384; F3 band baseline _rb48 at the same two; BA5; 857-label
J with the closure; extra_checks; far1_ver, far2_ver; scratch/read_fit.py, scratch/pair_rule.py).
(a) c_l: end 5.5763696769 (identity on my inverse 5.5763696770; c_l root of h(P) = 1 5.576369718, +4.1e-8). Against F3's end
    5.5763711550: -1.478e-6 over 20750 iterations (GPU check trace 5.5763711435 at the first check, 5.5763703016 at outer 5,
    5.5763696769 at the end, monotone). Against the fixed value 5.5753626106: +1.0071e-3. So the free c_l of a fit whose rows
    reach 9000 L moves by 1.5e-6, less than the at most 6.9e-6 of the free continuations on 900 L rows, and by 0.15 percent
    of its distance to the fixed value. Data only.
(b) Far field. C at the axis (far1_ver, nt 16384): +6.503e-4, against dom9000g +6.465e-4 (1.006) and F3 +1.8640e-2 (0.035).
    Next to the y-axis (far2_ver, nt 32768, theta 1.56811): q1 4.949e-4 (dom9000g 4.938e-4, F3 1.5779e-2), q2 -14.669
    (dom9000g -14.651, F3 -88.589), qh 782.40 (F3 782.40), q3 -3.465e4 (dom9000g -3.461e4, F3 +1.185e5); relative
    inconsistencies at orders 1, 2, 3: 3.0e-6, 0.15 percent, 10.1 percent (dom9000g the same to the digits shown).
    Band N_v maxima, formula-continued (16875 x 512 / 22500 x 384), against F3 formula-global (_rb48):
        1000 L-9000 L   3.291e-8 / 3.142e-8   against 1.098e-6 / 1.091e-6   ratios 0.030 / 0.029
        9000 L-1e4 L    2.415e-8 / 2.417e-8   against 9.651e-7 / 9.607e-7   ratios 0.025 / 0.025
        r > 1e4 L       3.285e-8 / 3.293e-8   against 9.263e-7 / 9.229e-7   ratios 0.035 / 0.036
    Own convention (closure): 1000 L-9000 L 3.293e-8 / 3.144e-8; 9000 L-1e4 L 2.418e-8 / 2.417e-8; r > 1e4 L 2.306e-5 /
    2.301e-5 next to the y-axis in the closure (dom9000g 2.307e-5 / 2.302e-5). The free c_l changes none of the G91 far-band
    readings of dom9000g by more than 4 percent (1000 L-9000 L 1.028 / 1.035 of dom9000g's).
(c) The pair dom9000g / dom9000gF (fixed / free at equal budget on the same rows; 12:02Z quantities as ratios, no decision):
    whole-box N_f, own convention 1.001 / 1.001 / 1.001 (both maxima in the closure at about 2.3e4 L, next to the y-axis);
    formula-continued 0.920 / 1.000 (16875 x 512 / 22500 x 384); within 0.5 of P 0.931 / 0.937 / 0.935; N_v r <= 1000 1.073 /
    0.940 / 1.001; N_v beyond 1000 L 1.000 (closure) and 0.973 / 0.997 (formula); J 0.937 (eps 0.03: 9.106e-7 / 9.722e-7) and
    0.937 (eps 0.01: 1.0199e-6 / 1.0881e-6); L2 objective 0.976 (1.33439e-6 / 1.366938e-6). h(P) - 1 of dom9000gF +3.05e-7 /
    +6.02e-8 / -6.30e-9. Centre of dom9000gF: x* 8.6008441 (vaxis W_1 zero 8.6008438, the only one), W_2/y >= 5.57657 on the
    y-axis, no open-quadrant cell. The N_v maxima of dom9000gF for r <= 1000 lie next to P (1.105 L, theta 0.0074, at 16875 x
    512) or in the lobe above P (1.148 L, theta 0.3076 at 11250 x 384; 1.142 L, theta 0.1931 at 22500 x 384).
Verdict: values CONFIRMED as listed (my evaluator). The pair repeats the X3 / F3 pattern on rows to 9000 L: the fixed-c_l fit
is lower next to P (0.93 to 0.94) and in J (0.94), equal in the far bands; the free c_l stays at its F3 value to 1.5e-6.
Not a candidate; no decision attached (lead 20:41:00Z).

## G126 (2026-10-19T06:06:44Z). Row 55 fxn24g (fixed c_l at d = -2.4e-2 on 375 x m <= 150; chain 9 step 55) by the rule of NOTES 00:25:51Z item 2, the bracket statement of SPEC v4.15 (NOTES 03:46:06Z item 4), the X3 comparison and the location of the maxima (NOTES 04:02:23Z item 2, 05:52:35Z item 3)

Data: GPU chain line "2026-10-19T05:48:09Z step 55 done", 21500 iterations (outer 9 it 1500), md5 e52a8be0f977eaa6398fb9d27302453d,
the same md5 as my copy runs/gen4/gpu/fxn24g_shape.npz (runs/audit/jS.log 05:49:05Z). Stored c_l 5.55246529 (5.5763624 + d +
0.18 d^2 [only to 8e-7: 7.9e-7 below it; corrected in G128 (c)]). Method as G123 (gen_audit N11250 q384 M479 and N16875 q512 M639, R = 7.652e6, A5 regions; jset 857-label J at
N16875 q384; extra_checks at N11250 q384; far1_ver; scratch/fx_profile.py, scratch/wb_loc.py), plus two extra configurations
for h(P): extra_checks at N16875 q512 (tag fxn24gN16875) and gen_audit at N22500 q384. Results (N11250 q384 / N16875 q512;
ratios to F2 on the same configuration):
- L2 objective 3.300646e-6 = 0.775 x F2; change over the last 1000 iterations -2.498 percent: NOT flattened by the 2 percent
  test (rows 52 / 53 / 54: -0.19 / -0.44 / -1.72 percent). Lead prediction recorded before the result: 0.80 to 0.87.
- Whole-box N_f (A5) 1.7917e-6 (1.139) / 1.8250e-6 (1.159), the same with all columns; N22500 q384 1.8571e-6. Both maxima
  within 0.5 of P (r 8.5184 / 8.5277, theta 0.0098, distance 0.106 / 0.100), so N_f within 0.5 of P is the same value.
- N_v for r <= 1000 (A5) 5.017e-7 (1.142) / 5.114e-7 (1.163); beyond r = 1000 1.1525e-6 / 1.1526e-6 (A5), 1.1525e-6 /
  1.1685e-6 (all columns).
- h(P) - 1 = +1.46e-6 / +2.61e-7, and +6.3e-9 at N22500 q384: it falls with my radial resolution as in G73 (lead scans
  -4.2e-8 / -2.7e-8 at 32768 x 640 / 24576 x 960). Identity c_l 5.552465285 (the stored value to 3e-9). The c_l root of
  h(P) = 1 at fixed rho: 5.552464421 (-8.6e-7) at N11250 q384, 5.552465223 (-6.2e-8) at N16875 q512; the N11250 value is
  the largest on any row and is the same grid error. x* 8.5823236, the only zero of W_1 on the x-axis; no zero of W_2 on the
  y-axis (W_2/y >= 5.55267); no open-quadrant cell. Centre: a0 = 1 to 1e-10, D2 relative defect at most 1.0e-8.
- J (857 labels, N16875 q384) 3.9530e-6 at eps 0.03, 4.5375e-6 at eps 0.01 (1.158 / 1.206). C at the axis +0.0195607.
Reading by the letter of item 2: (a) needs L2 within 30 percent of F2's (0.775: yes), whole-box N_f within 30 percent on each
configuration (1.139 / 1.159: yes) and |h(P) - 1| <= 1e-6; my N11250 q384 value is 1.46e-6, so (a) fails by the letter on
the prescribed configurations; (b) fails (not flattened; near-P N_f 1.139 / 1.159 of F2, below 2). Reading (c) "undecided at
the 375 x m <= 150 level after 21500 iterations". With h(P) taken at the radial resolutions that resolve it (N >= 16875, or
the lead's scans) the row reads (a). Both readings widen the interval.
Verdict: CONFIRMED as (c) by the letter ((a) on resolved h(P)); the interval of (iv) now contains [5.5524653, 5.5793640].
Bracket statement (SPEC v4.15, 55 against 54): the L2 objective of 55 is ABOVE 54's (3.300646e-6 > 2.737838e-6; 1.206 times),
and its whole-box N_f is ABOVE 54's on both configurations (1.7917e-6 > 1.1271e-6 at N11250 q384, 1.8250e-6 > 7.630e-7 at
N16875 q512). By SPEC v4.15 the lower end of the tested span is bracketed at this budget: CONFIRMED. Two facts belong with
it: (i) row 55 has not flattened (-2.50 percent over its last 1000 iterations), and at its last-1000 rate it would need
about 7400 more iterations (constant rate assumed) to reach 54's L2, so the bracket is a statement about fits from transplanted starts at one
budget (the start norm of 55 was 1.48e-3 against 8.41e-4 for 54, NOTES 03:13:52Z / 03:46:06Z), not about where an
objective over c_l has its minimum; (ii) 55 is below F2 in L2 (0.775) but above F2 in whole-box N_f (1.14 / 1.16), N_v
r <= 1000 and J (1.16 / 1.21), so on this row the L2 objective and the residual maxima disagree.
Profile at equal budget (stored c_l; whole-box N_f at N16875 q512): d = -2.4e-2, -1.6e-2, -8e-3, -4e-3, -2e-3, -1e-3, 0,
+2e-3, +3e-3, +2.4e-2: L2 / F2 = 0.775, 0.643, 0.741, 0.858, 0.926, 0.962, 1, 1.078, 1.115, 2.036; N_f / F2 = 1.159, 0.485,
0.427, 0.713, 0.869, 0.911, 1, 1.138, 1.214, 2.914; J / F2 (eps 0.03) = 1.158, 0.514, 0.388, 0.707, 0.865, 0.921, 1, 1.159,
1.224, 2.871. Among the tested rows the L2 objective is smallest at row 54 (5.5604082) and the residual maxima (whole-box N_f,
near-P N_f, J) at row 53 (5.5683739).
Comparison with X3 (m <= 200, c_l 5.5753626; different bases): whole-box N_f 2.593 / 2.668; within 0.5 of P 2.754 / 2.668;
N_v r <= 1000 2.613 / 2.668; far band beyond r = 1000 1.063 / 1.073 (A5), 1.058 / 1.061 (all columns); J 2.848 (eps 0.03)
/ 2.833 (eps 0.01). Row 55 is above X3 in every one of these maxima on both configurations (and in L2: 3.30e-6 against
1.62e-6, on different bases).
Location for the report's sentence (G121): row 55 has its whole-box maximum within 0.5 of P on both configurations.
N_v ratio against N_f ratio (NOTES 05:52:35Z item 3; the report says they agree to within 0.03 on every row): N_v r <= 1000
(A5) / F2 minus whole-box N_f (A5) / F2 over the ten rows and both configurations: at most 0.025 in absolute value (row 53
at N16875 q512: 0.453 against 0.427); 0.013 for row 39, 0.003 / 0.004 for row 55, below 0.004 on every other row.
CONFIRMED.
G120 C3 amended by this entry: the interval of every non-excluded tested value is [5.5524653, 5.5793640]; the lower end is
bracketed at this budget by SPEC v4.15 (with facts (i) and (ii)); "the L2 objective smallest at 5.5604082 and the residual
maxima smallest at 5.5683739 among the tested rows".

## G127 (2026-10-19T06:06:44Z). SPEC v4.17 (md5 37a19cac; diff against my copy of v4.16, scratch/SPEC_v416.md; copy scratch/SPEC_v417.md)

Method: diff. Result: two changes, both the G122 wording points: the v4.16 item cites the NOTES time 03:54:45Z, and the
flattening clause now governs both readings of 56 ("if 56 has flattened ...: Q_200 >= 3.05 ... , Q_200 <= 1.36 ...;
otherwise, or if 56 has not flattened, undecided"), which is the NOTES text I read by. Version line and change log updated.
"No change of standard" holds. Verdict: CONFIRMED.

## G128 (2026-10-19T06:23:06Z). Diff audit FINAL_REPORT 5c15c44d -> f62755aa (lead NOTES 2026-10-19T06:17:14Z, hunks (a) to (i)): C1, C2, C3 and C7 of G120

Method: diff of my copies scratch/FR_5c15.md and scratch/FR_f627.md (md5 f62755aa, 1486 -> 1618 lines; the changed hunks are
the nine listed in the NOTES, no others). Every number of the changed text compared with my G-entries; for the fixed-c_l
profile also with a fresh run of scratch/fx_profile.py on my audits, which reproduces every value of the 4.3 table to the
printed digits, and with the stored c_l of each shape file in runs/gen4/gpu. Line numbers are those of f62755aa.
(a) (iv), lines 662-674. Interval [5.5524653, 5.5793640] on 375 x m <= 150 at one budget, 5.6004662 excluded at the attained
    level, lower end bracketed at this budget with facts (i) and (ii) of G126, no measured lower end: numbers CONFIRMED (G126).
    Wording: the first sentence, "The computation determines c_l only to an interval (the tested span of exponents admitting
    comparably accurate fits, ...)", disagrees with the last ("so the interval has no measured lower end") and with G120 (3)
    ("the residual does not determine the exponent at this level"): a tested span whose lower end is not measured is not a
    determination to an interval. Required (C3): for example "The computation does not determine c_l: the tested exponents
    that the rule of 4.3 does not exclude span [5.5524653, 5.5793640] (an observed span, not an enclosure of the exponent of
    an exact profile)". The rest of (iv) stands.
(b) 4.1. Lines 732-734 (C1): "numerical evidence consistent with the existence of an exact profile of P_2 near rho_h. They do
    not establish the proximity of an exact profile or determine its exponent: if the exact profile is isolated (4.8), its
    exponent may lie outside the tested span of (iv). It is not a proof." This is the content of G117 (4), with the measured
    sizes in the same bullet (6.83e-7 to 7.16e-7, 1.11e-6, 2.0e-7): C1 MET in 4.1. The X1 bullet, lines 763-767: 0.984,
    0.977, 1.038, 0.954 / 0.882, 1.289 and 1.005 CONFIRMED (G119; N_v 1.038 is the 16875 x 512 value, as the sentence says).
    Rows 54 and 55 are above X3 in every maximum (G123, G126), so the first sentence of that bullet stands. Remaining C1 point,
    (iii), line 660: "That an exact profile near the trial exists in P_2 is the numerical claim, not a proved statement" still
    states the claim as proximity, which 4.1 now says is not established. Required: for example "The numerical claim is the
    one of 4.1 (evidence consistent with the existence of an exact profile of P_2 near the trial; neither the proximity nor
    the exponent is established); it is not a proved statement."
(c) 4.3, fixed-c_l profile, lines 919-958. All ten rows (55, 54, 53, 52, 37, X2 = s2g, F2 = seg3g, 38, 40, 39): stored c_l to
    seven decimals, L2 and its ratio, whole-box N_f on both configurations and ratios, J and ratio: CONFIRMED. Readings ((a)
    for 52, 37, 38, 40; (c) for 53, 54 and, by the letter, 55; (b) for 39): CONFIRMED (G109, G111, G114, G115, G118, G119,
    G123, G126). The rule as quoted is NOTES 00:25:51Z item 2: CONFIRMED. Location of the maxima (row 53 at 16875 x 512:
    whole-box 6.7297e-7 against 6.6836e-7 within 0.5 of P, 0.7 percent; at 11250 x 384 the lobe on rows 53 and 54; within
    0.5 of P on every other row): CONFIRMED (G121, G123, G126). N_v ratio within 0.03 (at most 0.025): CONFIRMED. Identity to
    3.2e-9 on every row (row 55: 3.1e-9): CONFIRMED. h(P): at most 6.9e-7 off row 55 (row 54: 6.90e-7); row 55 1.46e-6 /
    2.61e-7 / 6.3e-9; row 39 1.07e-6 / 2.45e-7: CONFIRMED. Monotonicity: L2 ratio 0.643, 0.741, 0.858, 0.926, 0.962, 1, 1.078,
    1.115, 2.036 from 5.5604082 up, about 4 percent per 1e-3 near F2 ((1.078 - 0.926)/4 = 3.8 percent), 0.775 at 5.5524653;
    N_f and J increasing from 5.5683739 up on both configurations, below the L2 ratio from F2 down to 5.5683739, larger at
    5.5604082 and larger again at 5.5524653 (16875 x 512: 0.427, 0.485, 1.159; 11250 x 384: 0.566, 0.716, 1.139; J 0.388,
    0.514, 1.158): CONFIRMED. L2 least at 5.5604082, maxima least at 5.5683739: CONFIRMED. Row 55 not flattened (-2.5
    percent) and about 7400 iterations at a constant rate: CONFIRMED (G126). C2 (lines 953-958): every fixed-c_l fit below
    F2's exponent has a lower L2 objective than F2 at the same 21500 iterations (ratios 0.643 to 0.962); F2's c_l in
    [5.5763641, 5.5763716] over its 20750 iterations (G117 (1)); "free branch" names the free fits; the last sentence ends
    "they do not locate an exponent or a minimum of an objective over c_l": C2 MET.
    Correction required (C3, numbers): line 920, "holds c_l at the value stored with that start, which is 5.5763624 + d +
    0.18 d^2", holds only to 8e-7. Stored c_l minus that expression: -7.92e-7 (d = -2.4e-2), -2.68e-7 (-1.6e-2), -2.6e-8
    (-8e-3), +1.9e-8 (-4e-3), +2.9e-8 (-2e-3), +2.8e-8 (+2e-3), +2.5e-8 (+3e-3), +8.4e-8 (+2.4e-2). The table quotes the
    stored values, which are correct; the sentence needs "to within 8e-7" or "approximately". The same imprecision is in my
    own G112 precision note and in the Data line of G126 ("Stored c_l 5.55246529 (5.5763624 + d + 0.18 d^2)"); both are
    corrected here: the stored value of row 55 is 5.552465288, 7.9e-7 below that expression. No reading depends on it.
(d) Interval paragraph, lines 977-980, and the spread sentence after it: interval and exclusion CONFIRMED; the free control
    of the 9000 L row, -1.5e-6 in 20750 iterations, toward the fixed value: CONFIRMED (G125 (a): -1.478e-6). Suggestion:
    "every c_l tested on the candidate's radial basis" should add "with angular cap m <= 150", as (iv) does (the
    candidate's own cap is 200).
(e) 4.5, lines 1337-1340: 0.029 to 0.030 of F3's over 1000 L to 9000 L, far bands within 4 percent, 0.93 to 0.94 within 0.5
    of P and in J: CONFIRMED (G125 (b), (c)).
(f) 4.6, lines 1434-1439 (C7): the spread 5.5728 to 5.5823 on 128 x 32 to 320 x 80 with R = 1000 to 10000, the R = 30000 run
    named as not included, "a variant spread, not an error bound", and the attribution "rests on one singular-value
    computation of that workstream and is not independently verified": CONFIRMED (G124). C7 MET.
(g) 4.8, lines 1494-1507: the fits below X2's c_l down to 5.5604082 are lower than X2 in L2 (0.643 to 0.926 against 0.962)
    and in the maxima (N_f 0.427 to 0.869 against 0.905 / 0.911; J 0.388 to 0.865 against 0.921) at the same 21500
    iterations; 5.5524653 is lower in L2 (0.775) and higher in the maxima (1.139 / 1.159, J 1.158); the fit at 5.5683739 is
    below X3 at 16875 x 512 (0.984 / 0.977): CONFIRMED. The "stable c_l" sentence is the reading of G120 (3): CONFIRMED. The
    thresholds 2.96 / 0.91 and the ratio 2.036: G114, CONFIRMED. The discriminating experiment named as not done: C4 met for
    now (56 / 57 to follow). Correction required (C3; text unchanged since 5c15c44d but now in scope): line 1481, "The
    candidate was selected by rules that compare residual maxima of fits at equal budgets". Rule (1) compares equal-budget
    pairs, but rule (2) compares the kept fits X2 and X3, which are not at equal budget (X3 = X2 + 20750 iterations). For
    example: "by rules that compare residual maxima of fits (rule (1) within equal-budget pairs, rule (2) across the kept
    fits, which are at different budgets)".
(h) Section 5 (b), the GPU list, and the "Not done" paragraph (lines 1615-1618: one basis, one budget; the angular sequence
    mixes approximation and budget, as in G120 (2)): CONFIRMED.
(i) Timeline 01:38 to 06:06: each entry checked against G111, G113, G114, G115, G117, G118, G119, G120, G121, G123, G125 and
    G126: CONFIRMED (01:38 h(P) <= 8.2e-8; 02:45 -0.49 percent; 02:57 3.6e-7; 03:48 5.5e-8; 04:01 4.5e-7 and "2 percent
    below"; 05:03 6.9e-7, its maxima above X3's on both configurations, 1.127e-6 / 7.63e-7 against X3's 6.91e-7 / 6.84e-7 at 11250 x 384 / 16875 x 512).
    The 04:03 entry matches G120 as amended by G126.
Scope wording (suggestion, from G129): the table head "Every fit compared" (line 896) and "the table lists the fits compared
by the rules" (line 972). The "Not in the table" list (lines 972-975) omits the domain columns of 4.4 and the free control of
the 9000 L row (4.5). Those fits are compared with the candidate by their own rules. Either add them to the list, or head
the table "Every fit compared by the selection rules".
Proof language: f62755aa has no sentence that calls numerics a proof. Every use of "proved" or "establish" outside section
3 is a disclaimer or concerns the explicit trial formula.
Verdict:
- C2 MET.
- C7 MET.
- C1 MET in 4.1; (iii), line 660, must be aligned.
- C3 MET in every number. Three corrections are required: the first sentence of (iv); "to within 8e-7" at line 920; "at
  equal budgets" at line 1481.
- No number of the changed text is wrong.
- C4 waits for 56 / 57; C5, C6 and C8 wait for the presentation pass.
- The team may NOT finish yet.

## G129 (2026-10-19T06:23:44Z). Check of the astra answer astra/verd8: a hostile referee of my endpoint judgement G120 (question astra_q/verd8.md; it audited FR_5c15.md)

The answer (exit 0, 108 lines) is a documentary audit. Its line numbers refer to FR_5c15.md (5c15c44d); I map them to
f62755aa (G128). Item by item:
(1) Verdict "defensible only with stated changes". It separates three things: consistency of c_l (identity), stability along
    a construction, and determination by the equation. It finds the first two supported and the third not, and it accepts
    the G120 (3) reading of "stable c_l" as a defensible interpretation of G20 if it is stated wherever the endpoint is
    announced. I agree; this is G120 (3). Its required changes:
    - "does not determine c_l; the span of tested values not excluded is ...": adopted, G128 (a).
    - Use the span [5.5524653, 5.5793640], with 5.6004662 excluded by the rule at this level: already in f62755aa.
    - State that the least objective is at 5.5604082 and the least maxima at 5.5683739, and that the bracket concerns
      finite-budget fits from transplanted starts: already in f62755aa (iv) and 4.3.
    - Remove both proximity claims. 4.1 now says "consistent with the existence ... near rho_h" and then "do not establish
      the proximity". I judge that not to be a proximity claim, so I do not require the word "near" to go. (iii) does state
      proximity as the claim: required, G128 (b).
    - Domain comparisons as sensitivity evidence: present (4.4: not a domain convergence study; 4.1: agreement to a factor
      1.4): CONFIRMED that no change is needed.
    It also finds an overstatement in G120 (3): "so no computed c_l is a minimiser of the objective". CONFIRMED as an
    overstatement. What G117 (1) shows is two things:
    - at equal budget, the objective attained at F2's c_l is above the objective attained at every fixed c_l below it;
    - the free iteration did not move c_l toward those values.
    An attained objective only bounds from above the reduced objective (the minimum over shapes at fixed c_l). So this does
    not show that F2's c_l, or any computed c_l, is not a local minimiser of the reduced objective. Corrected wording of that
    clause of G120 (3): "so at this budget F2's c_l is set by its start, not by a minimum of the objective". This is the
    report's wording (4.3, line 957), which I confirmed in G128 (c). The conclusion of G120 (3) is unchanged.
(2) Requirements of PROMPT lines 104 to 109 and 121 against the draft:
    - Present: representation, parity, normalization, the identity check, absolute and normalized R, E, three resolutions,
      three domains with fixed interior regions, far field, manufactured tests, parity checks, conditioning. I agree; each
      was audited in earlier entries (G20 mapping, G76, G105, G106, G110).
    - Absent from 5c15c44d but now in f62755aa: C1, C2, C3, C4 (pending 56 / 57) and C7 (G128).
    - The phrase "every tested c_l at which a fit meets the standard" is replaced by the non-exclusion wording in f62755aa,
      line 977: CONFIRMED.
    - Artifacts: my listing of lead/artifacts at 06:2x UTC agrees with the answer. a_coefficients holds no
      c6g_shape.npz and no c6gF_shape.npz, and there is no b_fit_gpu part with gpu_long_solve.py. So section 5's "arranged
      in seven parts" describes the intended package. C6 stays OPEN, and I check it in the final tree.
    - The answer asks that the final audit (C8) keep a requirement-by-requirement mapping to PROMPT lines 104 to 109 and 121,
      not only C1 to C8. Adopted: my DONE audit will include that mapping.
(3) The answer finds no literal claim that numerics prove existence (my grep of f62755aa agrees, G128). Its flagged
    sentences, in f62755aa numbering:
    - Line 660 (iii), proximity: required (G128 (b)).
    - Line 662 (iv), "determines c_l only to an interval": required (G128 (a)).
    - Line 1481, "at equal budgets": required (G128 (g)). Rule (2) compares X2 and X3 across budgets.
    - Lines 896 and 972, scope of "Every fit compared": suggestion (G128). Line 883, rule (2) ("the kept fit with the lowest
      whole-box N_f"), is a rule definition scoped by "kept"; no change.
    - Line 977 (old "meets the standard"): replaced in f62755aa.
    - Line 105, timeline: "the Gauss-Newton exponent step ... locates the least-squares minimizer of a trial basis in c_l".
      Suggestion: "estimates, to first order". It is a step of a linearization, as 4.6 says ("a tangent prediction, not a
      stationarity test").
    - Line 186, timeline: "no other zero of the field ... confirmed". Suggestion: "on the evaluation grid", as 4.2 says (a
      sampled check, not a validated exclusion).
    - Line 1195, "stall at the angular floor": the parenthesis already says it was measured on one row; no change needed.
    - Lines 1283 to 1288: "equals the supremum minus the infimum of J_eps over all labels ... to about 1e-8" and "leaves the
      sampled range only for d below e^(-1190)". Both are sampled or leading-order statements and the parentheses give the
      method. Suggestion: "on the sampled labels and their parabolic refinement" and "by the leading logarithmic term".
    None of these suggestions changes a number.
(4) The P_2 distinction is acceptable under PROMPT line 62, and the definition and the "not answered" statement for the smooth
    setting are adequate. CONFIRMED; this agrees with G20 (a). Section 4 opens "YES, strong numerical evidence, for the
    explicitly distinguished problem P_2" followed by "(i) The posed strong setting ... is not answered". "Strong numerical
    existence evidence" is the name the prompt gives the deliverable (PROMPT line 121), so the label is not hype.
Verdict: the answer's checkable claims are CONFIRMED (artifacts absent; overstatement in G120 (3); the flagged sentences
exist as quoted). Its required changes are either already applied in f62755aa or required in G128, except one: the word
"near" in 4.1 is not required to go. The G120 judgement stands with the corrected clause.

## G130 (2026-10-19T06:23:56Z). SPEC v4.18 (md5 f81f003c; diff against my copy of v4.17, scratch/SPEC_v417.md; copy scratch/SPEC_cur.md) and lead NOTES 2026-10-19T06:18:36Z

Method: diff. Result: one new item in section 8 and a change-log line. Steps 58 fxn16gb and 59 fxn24gb continue rows 54 and
55 for 21500 iterations each at the stored c_l, with the same settings (43000 in all). They are read on my two
configurations:
- "kept at twice the budget" if L2(59) and the whole-box N_f of 59 on both configurations are above 58's;
- "not kept" if L2(59) is below L2(58);
- otherwise "the objective and the maxima disagree".
The last-1000 changes are stated. The single-budget profile, its readings and the interval are unchanged. These are not
candidates and there is no change of standard. The text matches the NOTES. The three cases are exhaustive apart from equal
L2. The reading is fixed before the runs: the lead's prediction (L2(59)/L2(58) in 1.00 to 1.15) is recorded in the NOTES
and the steps have not started (chain10 is passive until 49 and 50 end).
One limit, to be stated with the reading: neither continuation is at equal budget with F2, and both rows may still be
falling. So "kept at twice the budget" is again a statement about fits from transplanted starts at a stated budget, not
about where a reduced objective over c_l has its minimum (G129 (1)).
My audit waiters for 58 / 59 are started: scratch/jrow.sh fxn24gb 59 (timeout wrapper PID 2519162, bash 2519164) and
scratch/jrow.sh fxn16gb 58 (2519161 / 2519163), each under timeout 11h.
Verdict: CONFIRMED.

## G131 (2026-10-19T06:36:06Z). Diff audit FINAL_REPORT f62755aa -> 822f368d (lead NOTES 2026-10-19T06:31:30Z, round A2) and an interim C6 check of the artifacts tree
Method. Copy scratch/FR_822f.md (md5 822f368dc0249975e539042b99ed8758, 1624 lines). The lead's saved copy
notes/FINAL_REPORT_f62755aa.md has md5 f62755aa, the file of G128. A word diff (tr -s ' \n' '\n\n' on scratch/FR_f627.md
and scratch/FR_822f.md, then diff) shows only the words listed below. The line diff consists of refills of the same
paragraphs.
(a) G128 (a), (iv), lines 664-666: "The computation does not determine c_l: the tested exponents that the rule of 4.3 does not
    exclude on the candidate's radial basis with angular cap m <= 150 span [5.5524653, 5.5793640] (an observed span, not an
    enclosure of the exponent of an exact profile)." The words "admitting comparably accurate fits" are removed. The basis
    qualifier added by the lead is true (rows 37 to 40 and 52 to 55 are on 375 x m <= 150; G109 to G126). CONFIRMED.
(b) G128 (b), (iii), lines 661-663: my wording verbatim ("The numerical claim is the one of 4.1 (evidence consistent with the
    existence of an exact profile of P_2 near the trial; neither the proximity nor the exponent is established); it is
    not a proved statement."). It agrees with 4.1, lines 732-734. CONFIRMED; C1 MET in full.
(c) G128 (c), line 923: "5.5763624 + d + 0.18 d^2 to within 8e-7 (the table quotes the stored values)". This matches my G128 (c)
    computation (largest deviation -7.92e-7, at d = -2.4e-2). CONFIRMED.
(d) G128 (g), 4.8, lines 1486-1487: "by rules that compare residual maxima of fits (rule (1) within equal-budget pairs, rule (2)
    across the kept fits, which are at different budgets)".
    - Rule (1), line 882, compares each equal-budget pair.
    - Rule (2), line 886, compares the kept fits, and X2 and X3 differ in budget by 20750 iterations.
    CONFIRMED.
(e) G128 (d) suggestion, Interval paragraph, line 981: "with angular cap m <= 150" is added. Taken.
(f) G128 scope suggestion:
    - The table head (line 899) now reads "Every fit compared by the selection rules".
    - The "Not in the table" list (lines 977-979) adds the domain columns (4.4) and the free control of the 9000 L row (4.5).
    Taken.
(g) G129 (3) suggestions, all taken:
    - timeline line 105: "estimates, to first order, the least-squares minimizer";
    - timeline line 186: "no other zero of the field on the evaluation grid";
    - 4.4b: "to about 1e-8, on the sampled labels and their parabolic refinement" and "by the leading logarithmic term
      leaves the sampled range".
(h) No measured value changed. The tokens with digits in the word diff are:
    - section references (4.1, 4.3, 4.5), rule numbers (1) and (2), P_2;
    - the cap 150 and the 9000 L label;
    - the interval of (a), already quoted in the old (iv);
    - the "8e-7" of (c);
    - punctuation-only changes of "d^2" and "1e-8".
    CONFIRMED.
Result: C3 MET in full (the three required wordings of G128 are in); C1 MET in full.
Interim C6 check (NOTES 06:31:30Z item 2; the final tree will be checked again at the presentation pass):
(i) Tree lead/artifacts: 123 MB, 13 directories at the top (a_coefficients, a_generator, b_fit, b_fit_domain, b_fit_gpu,
    c_diagnostics, c_diagnostics_code, c_farfield, d_evaluator, e_independent, f_referee, f_spec, g_logs), 1343 files.
    md5:
    - a_coefficients/c6g_shape.npz 15f8095f7e79dbfa0c50d75e5fe8997a;
    - a_coefficients/c6gF_shape.npz 0398af3f08a2a4f75e42c846edbaa375;
    - b_fit_gpu/gpu_long_solve.py f26dde2d557150021b8b4660af2dcc8a.
    These are the values stated in section 5. The two coefficient files are byte-identical to the files I audited
    (runs/gen4/gpu/c6g_shape.npz and c6gF_shape.npz have the same md5).
(ii) Every script named in section 5 exists in the tree (24 names checked with find).
    d_evaluator/code holds 74 files of my code/ directory. 72 are byte-identical. The other two are gen_audit.sh and
    extra_checks.sh, where the one difference is the cd line, made relative ("$(dirname "$(readlink -f "$0")")/../code").
(iii) Reproduction from a copy of the tree. I copied the parts to scratch/c6smoke, because I write only in my lane.
    - Step 3 of section 5: "python3 quick_scan.py c6g_shape.npz 32768 640 out.json", in b_fit with a_generator on
      PYTHONPATH, single-threaded. It ran in 16 s, and its output equals the stored c_diagnostics/c6g_scan.json in every
      field except the file name.
    - Step 1: "bash gen_audit.sh <c6g> c6smk '7.652e-4 7.652e6 11250 384 479'", in a copy of d_evaluator. It ran in 106 s,
      exit 0. Its JSON has the same 1679 keys as my audit runs/audit/c6g_N11250_q384_R7.652e6.json, and all 1510 float
      fields are identical except the timing field t_eval.
    So the packaged evaluator and the lead's scan run from the tree as documented and reproduce the recorded outputs on X3.
(iv) Not yet in the tree, as the lead states: the final reassembly after the last GPU rows (56 / 57, 58 / 59).
    Suggestion: a top-level index file listing the seven parts with their directories (the section 5 text names parts,
    not directory names; for example b_fit_domain and c_diagnostics_code are not named there).
Verdict: CONFIRMED (round A2). C6 interim: MET on the current tree, to be re-checked on the final tree.

## G131 addendum (2026-10-19T06:40:43Z). FINAL_REPORT 822f368d -> d569d377 and artifacts INDEX.txt
Method: line diff of scratch/FR_822f.md against scratch/FR_d569.md (md5 d569d377), plus a listing of lead/artifacts.
(a) Three timeline entries were added (06:23, 06:23, 06:36), lines 555 to 568. Each was compared with G128, G129 and G131:
    - 06:23, first entry: "every number confirmed; four wording corrections required and applied". G128 required four
      wordings: (iii), (iv), the 8e-7 qualifier and the budgets of the selection rules. CONFIRMED.
    - 06:23, second entry, the referee check: "its checkable claims confirmed". This is the G129 verdict line. The corrected
      clause of G120 (3) is quoted as in G129 (1). "The artifacts did not yet contain the coefficient files and code of
      the GPU fits" is what G129 (2) found. CONFIRMED.
    - 06:36 entry: it matches G131 (a) to (h) and (iii), including "every field identical except the timing and the file
      name". CONFIRMED.
(b) Section 5, line 1530: "the file INDEX.txt at their top level lists the directories of each part". INDEX.txt (06:39:29Z,
    1622 bytes) maps each of the 13 top-level directories to one of the parts (a) to (g); all 13 are named (checked with
    grep). This closes the suggestion of G131 (iv).
(c) d_evaluator/VERIFY_REPORT.md in the tree has md5 438d044d, which is this file at G131. For the final tree, this copy must
    be refreshed after my DONE entry, or section 5 must say that the verification record continues in the verifier's lane.
(d) Suggestion (not a condition): g_logs holds the lead's WORKLOG.md and RUN_STATUS.md only. PROMPT line 14 asks for logs
    that let a reader assess the timeline, including verifier activity. VERIFY_REPORT.md is timestamped entry by entry and
    is in (d). Adding my WORKLOG.md and numerics/WORKLOG.md to (g) would make the timeline complete. I can name the
    files; I do not write in the lead's tree.
Verdict: CONFIRMED.

## G132 (2026-10-19T06:50:36Z). A dangling reference in section 0, and the conditioning item of the C8 mapping
Method: I compared FINAL_REPORT d569d377 with the lead's helper notes/final_pass/prompt_map_draft.md, and grepped the
report and the packaged fit drivers.
(a) Line 17, section 0 (environment): "with the LSQR vector updates and the column-scaling probes (5 (b))". Section 5 (b) does
    not mention probes or column scaling; "probe" occurs in the report only on line 17. The drivers do it:
    - b_fit_gpu/gpu_long_solve.py, lines 94 to 99: the LSQR columns are scaled by 1/sqrt of a stochastic estimate of diag(J^T J)
      from --probes 24 Rademacher vectors (seed 8128 + outer). Columns whose estimate is below 1e-18 of the largest get
      scale 0, so they are not moved in that linearization.
    - b_fit/long_solve_fixcl.py, docstring line 9: "Column scaling: stochastic diagonal of J^T J (Rademacher probes)".
    Required (wording): either add to 5 (b) one sentence stating this scaling, including that columns below the cut are
    frozen for that linearization, or drop "(5 (b))" from line 17.
(b) C8 mapping, PROMPT line 108 ("Examine conditioning"). The helper cites "5 (b) (column-scaling probes)" for conditioning.
    The probes are a preconditioner of LSQR, not a conditioning test, so I do not count them. In my mapping, the conditioning
    item is carried by three things:
    - the weak constraint of the c_l direction: 4.6 (least first-order residual cost of a unit change of c_l, 1e-3 to 6e-5;
      one singular-value computation of that workstream, stated as not independently verified), 4.3 and 4.8;
    - the cancellation floor of the evaluator next to the y-axis (4.3, 4.4);
    - the round-off of the second difference on r <= 0.01 for E (4.4).
    No condition number of the main Gauss-Newton operator is reported. PROMPT line 108 does not ask for one, so this is
    not a condition.
Verdict: (a) wording required (minor); (b) recorded for C8.

## G133 (2026-10-19T07:12:37Z). Diff audit FINAL_REPORT d569d377 -> abb3e037 (lead NOTES 2026-10-19T07:10:49Z, round A4); round A3 is G131 addendum
Round A3 (d569d377: the timeline entries 06:23, 06:23, 06:36 and the INDEX.txt sentence) was audited in the G131 addendum
before the A4 note arrived; CONFIRMED there.
Method: copy scratch/FR_abb3.md (md5 abb3e037). Word diff against scratch/FR_d569.md, as in G131: 174 changed tokens, which
are items (a) to (k) of the note and nothing else. Checks of the cited values:
(a) Line 736, "in the second item below": the second item of 4.1 (line 751, "The free control at the same LSQR budget ...")
    is the equal-iteration comparison. CONFIRMED.
(b) Line 746, "(52, 51 and 52 points; 4.5)": 4.5 gives 52 points on X1 (line 1408), 51 on the free fit with 375 x m <= 100
    functions (line 1414) and 52 on X3 (line 1419). That free fit has a smaller angular cap than X3, so "a free fit of a
    smaller basis" is right. "(4.4, 4.5)" for the far band of the domain fits: the domain columns are in 4.4. CONFIRMED.
(c), (d), (e), (f), (h), (k): wording only, each checked against its context:
    - (c) "(ii) gives numerical evidence on that, not a proof" is accurate: (ii) is the B_3 estimator statement.
    - (e) section 3 states the growth bound R2 and no far-field expansion, so the deleted reference was inaccurate.
    - (f) D14 is not defined in the report; the sentence keeps the centre relations E_c, D2.
    - (k) the free control of step 5 starts from the free fit.
    No objection.
(g) 4.4, line 1141. Within 0.5 of P, ratios of N_f maxima to X3 recomputed from my audit files, at 11250 x 384 / 16875 x 512 /
    22500 x 384:
    - dom90g 0.326 / 0.332 / 0.324;
    - dom300g 0.593 / 0.569 / 0.585;
    - dom9000g 0.684 / 0.656 / 0.683;
    - budget row c6g2 (900 L) 0.544 / 0.525 / 0.538, and 0.503 / 0.526 at 16875 x 768 / 22500 x 512.
    So 0.32 to 0.33, 0.57 to 0.59, 0.66 to 0.68 and 0.50 to 0.54 as quoted. Among 90 L, 300 L and 9000 L the ratio grows
    with the domain. With the 900 L row (0.50 to 0.54, below 300 L's 0.57 to 0.59) the sequence is not monotone.
    CONFIRMED.
(i) 4.8, line 1502: "the fits listed in 4.5 other than F1 and W1 read 1.08e-6 to 1.17e-6". 4.5 lists F0, X1, F1r, X2, F2, X3,
    F3 and the reorthogonalized arm at 1.08e-6 to 1.17e-6, with F1 at 1.46e-6 to 1.47e-6 and W1 at 1.28e-6 to 1.31e-6
    (G96, G104). CONFIRMED. "follows from its explicit formula (4.1)" for C^(6,beta)_loc is weaker wording than "is
    proved", and 4.1 derives it from the formula (the least regular term |x|^(p_3) times a smooth factor). No objection.
(j) 5 (b), lines 1550 to 1557:
    - Rows 37 to 40 and 52 to 55 ran 21500 iterations on the GPU. b_fit_gpu/gpu_chain8.sh line 6 says "21500 iterations",
      and line 27 calls gpu_long_solve.py with --inner 2500 --check 250 --max-its $its, with K2 = 21500. gpu_chain6.sh line
      5 says "37-40 (c_l profile, K + 750)" with K = 20750.
    - X2 (s2g) continues the CPU fit fixc_c6f_m1.0e-03 (gpu_chain.log line 6), and F2 (seg3g) continues c6f_seg2 (line 8).
      X1 is the 750-iteration fit at 500 per linearization (outer 2, iterate 250; G67).
    - The exception is stated as such.
    - AMENDED 2026-10-19 (the first version of this item read CONFIRMED in full; I had not re-read the F1 log). The
      clause "X1 and F1 ran on the CPU at 500 per linearization" is REFUTED for F1. Evidence, b_fit/:
      . c6f_seg2.log (F1): one "linearize" event (outer 1), checks at outer 1, it 250, 500, 750, then "end"; c_l
        5.576364040, objective 7.0768e-6. The command is run_c6f.sh line 27, long_solve.py ... --hours 1.8 --inner 2500
        --check 250: 750 iterations in ONE linearization, stopped by the 1.8 h cap (last check at wall 6091 s).
      . fixc_c6f_m1.0e-03.log (X1): linearize outer 1, checks it 250, 500; linearize outer 2 (wall 4225 s), check it
        250, then "end": 500 + 250 over two linearizations, also stopped by the 1.8 h cap (wall 6196 s).
      This is what G69 (ii) recorded ("one linearization of 750; fixed: 500 + 250 over two"). Section 4.2 (line 865,
      X1 "750 LSQR iterations over two linearizations") is right. The same inaccuracy is in section 5, step 5 (lines
      1607 to 1609): "The free control is the same command run from the free fit, without --fix-cl" does not reproduce
      F1, which ran long_solve.py with --inner 2500.
      Required wording (5 (b)), or equivalent: "X1 ran on the CPU 750 iterations over two linearizations (500 + 250) and
      F1 750 iterations in one linearization (--inner 2500), both stopped by the 1.8 h cap. The pairs X1 / F1, and
      through their starts X2 / F2 and X3 / F3, are therefore equal in iteration count but differ in the relinearization
      schedule of their first 750 iterations." The "one exception" sentence must then not imply that the schedules
      are otherwise equal; for example "Apart from these first 750 iterations, and the fixed-c_l profile of 4.3 ...".
      Required in step 5: give the F1 command (long_solve.py <free fit> <out> --nr 20480 --nt 720 --hours 1.8 --inner
      2500 --check 250, segment 2 of run_c6f.sh).
      Effect on the conclusions: none on a measured value. It bears on the reading of 4.1's equal-budget comparison
      X1 / F1 (and X2 / F2, X3 / F3) only as a disclosure: the counts are equal, the schedules are not.
    REFUTED in part (the F1 schedule); the rest CONFIRMED.
Verdict: CONFIRMED (round A4) except (j): one wording correction required in 5 (b) and 5 step 5 (F1 ran 750 iterations
in one linearization at --inner 2500, not 500 per linearization). No measured value changed.

## G134 (2026-10-19T07:16:12Z). Diff audit FINAL_REPORT abb3e037 -> 654b09d5 (lead NOTES 2026-10-19T07:12:49Z, round A5: G132 (a))
Method: copy scratch/FR_654b.md (md5 654b09d523b1aff16d31b02f134fece3, 1645 lines). Word diff against scratch/FR_abb3.md:
one insertion, in 5 (b) before "Every residual quoted is evaluated ...". The sentence says that in each linearization the
long-fit drivers scale the LSQR columns by the inverse square root of a 24-probe Rademacher estimate of the squared column
norms of the Jacobian (seed 8128 plus the linearization count), that a column below 1e-18 of the largest gets scale 0, and
that with c_l fixed the column of k = 1/c_l gets scale 0 in every linearization. Nothing else changed.
Checks against the code in lead/artifacts:
- b_fit_gpu/gpu_long_solve.py lines 94 to 100 and b_fit/long_solve_fixcl.py lines 59 to 65: rng seed 8128 + outer; --probes
  default 24 (gpu line 25, fixcl line 26); diag accumulates (J^T p)_j^2 / probes over Rademacher p, whose expectation is the
  squared norm of column j. cut = max(1e-18 * max(diag), 1e-24); scale = 1/sqrt(max(diag, cut)) with scale 0 where diag <
  cut; with --fix-cl, scale[0] = 0. Column 0 is k = 1/c_l (the logs print cl = 1/z[0]). A column with scale 0 is not moved
  by the update scale * u. CONFIRMED.
- b_fit/long_solve.py lines 55 to 58, the free CPU driver (it ran F1, c6f_seg2, and the c6f segments): the same probes,
  seed and cut. So the sentence holds for all three long-fit drivers, but "both" counts two. Once 5 step 5 names the F1
  command (G133 (j)), "both" reads wrong; required with that correction: "the long-fit drivers" or "all three long-fit
  drivers (long_solve.py, long_solve_fixcl.py, gpu_long_solve.py)".
- The cut also has an absolute floor 1e-24. That matters only if the largest estimate is below 1e-6; I did not check
  this, and the wording is not required to change.
- Section 0, line 17: "the column-scaling probes (5 (b))" now has its target. G132 (a) is CLOSED.
Verdict: CONFIRMED (round A5). Still outstanding: G133 (j), the F1 schedule in 5 (b) and 5 step 5, with the word "both"
of this entry.

## G135 (2026-10-19T07:55:19Z). Nested pair 56 nst24g (c_l 5.6004662) / 57 nsn8g (5.5683739) on 375 x m <= 200, read by the rule of NOTES 2026-10-19T03:54:45Z item 3 (SPEC v4.16 / v4.17); C4
Method. GPU chain lines (numerics/leadcode/gpu/gpu_chain.log): "step 56 done" 07:24:30Z, md5 98b033aa6433a56b943356e0245844a4;
"step 57 done" 07:25:22Z, md5 29f70bbc0660d7c11f359885e7cc0086; copies md5-checked by scratch/jrow.sh (jS.log 07:25 / 07:26).
Settings from the fit logs: 20480 x 960, ncol 75382, fix_cl true, inner 2500, check 250, damping 1e-8, 9 linearizations, 20750
iterations (last check outer 9, it 750). These are the settings of step 31 (X3 = c6g) and step 32 (F3 = c6gF). Iteration
counts: 56 = row 39 (21500) + 20750, 57 = row 53 (21500) + 20750, X3 = F3 = 750 + 20750 + 20750, so 42250 each (the first
750 of X3 and F3 differ in schedule, G133 (j)). L2 objective = last "actual" of each log (scratch/ns_profile.py); F3
1.6641961056e-6 from its chain log; X3 1.6192702e-6. Audits with my generator and full-plane inverse
(code/gen_audit.sh, A5 regions) at N11250 q384 and N16875 q512, J (857 labels) at N16875 q384, extra_checks at N11250
q384 (jrow sets); one extra audit of 57 at N22500 q512 (07:48:58Z to 07:54:14Z, outside the rule).
Results (ratios to F3 / to X3 on the same configuration):
- 56 nst24g: L2 2.795041e-6 = 1.680 x F3 (1.726 x X3); change over the last 1000 iterations -0.956 percent, so flattened
  (< 2 percent). Whole-box N_f (A5) 1.6757e-6 (2.412 / 2.425) at N11250 q384, 1.8249e-6 (2.499 / 2.668) at N16875 q512,
  both maxima within 0.5 of P (|X - P| 0.163 / 0.093). Within 0.5 of P: 2.412 / 2.576 and 2.499 / 2.668. N_v r <= 1000:
  4.704e-7 (2.419 / 2.450), 5.123e-7 (2.503 / 2.672). Far band r > 1000: 1.054e-6 / 1.066e-6 (0.955 / 0.969 x X3), the
  common far level. J 3.6120e-6 (2.439 / 2.602) at eps 0.03, 4.4214e-6 (2.587 / 2.760) at eps 0.01. h(P) - 1 = -7.72e-7 /
  -1.82e-7. Identity c_l 5.6004661611 (the stored value 5.600466164 less 3.3e-9); a(0) = 1.0000000000 on the K3 to K5 jet
  fits; x* 8.6194830, the only zero of W_1 on the x-axis, no zero of W_2 on the y-axis, no open-quadrant cell with both
  components changing sign; B_3 (IBP) 0.2982 [0.2936, 0.3082]; C at the axis 0.0182470.
- 57 nsn8g: L2 1.328223e-6 = 0.798 x F3 (0.820 x X3); change over the last 1000 iterations -0.610 percent (flattened).
  Whole-box N_f (A5): 9.1325e-7 (1.315 / 1.322) at N11250 q384, 4.7247e-7 (0.647 / 0.691) at N16875 q512. Both maxima are at
  the off-axis lobe point r 8.784 / 8.788, theta 0.301 / 0.304 (|X - P| 2.61 / 2.64), the point that G73 (h) showed to be
  under-resolved by my N11250 radial grid; row 53 had its N11250 q384 maximum there too (G119: r 8.784, theta 0.3011).
  At N22500 q512 (outside the rule) the maximum is again there, 5.1188e-7 (0.703 / 0.749). Within 0.5 of P: 3.8471e-7
  (0.554 / 0.591), 4.0252e-7 (0.551 / 0.588), and 4.0381e-7 (0.555 / 0.591) at N22500 q512. N_v r <= 1000: 2.535e-7 (1.303 /
  1.320), 1.348e-7 (0.659 / 0.703). Far band r > 1000: 1.096e-6 / 1.107e-6 (1.007 / 1.009 x X3). J 7.8073e-7 (0.527 / 0.562)
  at eps 0.03, 8.7344e-7 (0.511 / 0.545) at eps 0.01. h(P) - 1 = +4.76e-7 / +2.84e-8. Identity c_l 5.5683738906 (3.2e-9 below
  the stored value); a(0) = 1.0000000000; x* 8.5946518, the only zero of W_1 on the x-axis, no zero of W_2 on the y-axis, no
  open-quadrant cell; B_3 (IBP) 0.2984 [0.2967, 0.2989]; C at the axis 0.0187634.
Reading, item 3 (i) (56): flattened, and Q_200 = L2(56) / L2(F3) = 1.680 lies between 1.36 (Q_150 / 1.5) and 3.05 (1.5
  Q_150), with Q_150 = 2.036. By the rule: "undecided". The near-P ratio asked for is 2.412 / 2.499 to F3 (row 39 to F2:
  2.915 / 2.914).
Reading, item 3 (ii) (57): the condition "L2 and whole-box N_f of 57 below X3's on both configurations" fails at N11250 q384
  (whole-box 1.322 x X3), so the report gives the ratios. The ratio asked for: L2(57) / L2(X3) = 0.820 against L2(53) /
  L2(X2) = 0.771. No decision, as the rule says.
Reading, item 3 (iii) (interval rule of NOTES 00:25:51Z item 2 at the m <= 200 level against F3; two-sided 30 percent band,
  as for every earlier row):
  - 56: (b) "excluded at this level": flattened, and the N_f maximum within 0.5 of P is 2.412 and 2.499 times F3's, >= 2
    on each configuration. So 56 does not widen the interval. The tested values not excluded remain those of
    [5.5524653, 5.5793640] (G126), and 5.6004662 is excluded at m <= 150 (G114) and at m <= 200.
  - 57: (a) fails (whole-box N_f 1.315 and 0.647 times F3's, outside the band on both sides; L2 0.798 and |h(P) - 1| <=
    4.8e-7 are inside); (b) fails (near P 0.554 / 0.551). So (c) "undecided at the 375 x m <= 200 level after its
    iterations". 5.5683739 is inside the interval, which does not change.
Verdict: CONFIRMED. 56: "undecided" (item 3 (i)) and "excluded at this level" (interval rule). 57: ratios only (item 3 (ii));
  (c) by the interval rule. Neither is a statement about P_2, and the candidate stays X3 (G74).
Wording required for C4, and for 4.1 / 4.3 / 4.8 / section 5 where they use these rows:
  (1) 4.8 and the "Not done" paragraph of section 5: one refinement step of the discriminating experiment was done (56, 57:
      the m <= 150 rows at 5.6004662 and 5.5683739 continued on m <= 200 at the budget of X3 and F3). By the rule fixed
      before the runs the result is undecided (Q_200 = 1.680; thresholds 1.36 and 3.05). (P1) and (P2) are not separated.
      Q_150 = 2.036 and Q_200 = 1.680 may be stated as measured. The decrease from 2.036 to 1.680 must not be read as
      favouring a family or as a trend: it is one step, and the rule assigns no reading between the thresholds.
  (2) Interval: 5.6004662 is excluded at m <= 200 as well (near P 2.41 / 2.50 x F3). The interval of tested values not
      excluded is unchanged.
  (3) 57 against the candidate. The following may be stated: L2 0.820 x X3; within 0.5 of P 0.59 x X3 on each
      configuration; J 0.56 / 0.55 x X3; whole-box N_f 1.32 x X3 at N11250 q384 (the under-resolved lobe point) and 0.69 x X3
      at N16875 q512. "57 has smaller residual maxima than the candidate" must not be stated without the N11250 q384
      exception. Under C3 (G123, G126) the report must say that on m <= 200 a fit computed at another fixed c_l has a smaller
      L2 objective, smaller N_f next to P and a smaller J than X3 at equal iteration count. It must not imply that X3 has
      the smallest residual of the fits computed.
  (4) If the N22500 q512 values of 57 are quoted, they must be marked as outside the rule.

## G135 addendum (2026-10-19T07:57:02Z). Table for round B (lead NOTES 2026-10-19T07:30:27Z item 3)
My values on the same configurations (scratch/ns_profile.py; L2 = last "actual" of each GPU log; whole-box N_f with A5;
J with 857 labels at N16875 q384; ratios to F3 in brackets):
| fit (c_l)          | L2 (last 1000 its)       | whole-box N_f N11250 q384 / N16875 q512 | J eps 0.03 / 0.01            | h(P) - 1 (two configs) | reading (4.3 rule vs F3) |
|--------------------|--------------------------|------------------------------------------|------------------------------|------------------------|--------------------------|
| X3 c6g (5.5753626) | 1.6192702e-6 [0.973] (-0.742%) | 6.9091e-7 [0.995] / 6.8410e-7 [0.937] | 1.3882e-6 [0.937] / 1.6019e-6 [0.937] | +2.84e-7 / +3.11e-8 | (a) not determined |
| F3 c6gF (free; 5.5763712 by the identity) | 1.6641961e-6 [1] (-0.756%) | 6.9470e-7 / 7.3033e-7 | 1.4808e-6 / 1.7093e-6 | +2.42e-7 / +4.16e-8 | reference |
| 56 nst24g (5.6004662) | 2.7950409e-6 [1.680] (-0.956%) | 1.6757e-6 [2.412] / 1.8249e-6 [2.499] | 3.6120e-6 [2.439] / 4.4214e-6 [2.587] | -7.72e-7 / -1.82e-7 | (b) excluded |
| 57 nsn8g (5.5683739) | 1.3282227e-6 [0.798] (-0.610%) | 9.1325e-7 [1.315] / 4.7247e-7 [0.647] | 7.8073e-7 [0.527] / 8.7344e-7 [0.511] | +4.76e-7 / +2.84e-8 | (c) undecided |
N_f within 0.5 of P (N11250 q384 / N16875 q512): X3 6.5052e-7 / 6.8410e-7; F3 6.9470e-7 / 7.3033e-7; 56 1.6757e-6 /
1.8249e-6 [2.412 / 2.499]; 57 3.8471e-7 / 4.0252e-7 [0.554 / 0.551]. Identity c_l (my inverse, (1 + psi_xy(0)) / 3): 56
5.6004661611 against the stored 5.600466164 (-3.3e-9); 57 5.5683738906 against 5.568373894 (-3.2e-9); X3 5.5753626074
against 5.5753626106 (-3.2e-9). Flattened (< 2 percent over the last 1000 iterations): all four.
The X3 row is read here against F3 by the same rule only for completeness. It is not a reading of the candidate, which
G74 designates.

## G136 (2026-10-19T07:57:13Z). Diff audit FINAL_REPORT 654b09d5 -> b74e084a (lead NOTES 2026-10-19T07:39:01Z, round A6: G133 (j), G134)
Method: copy scratch/FR_b74e.md (md5 b74e084adff6a4ee43a1e0e4ce649816, 1651 lines). Word diff against scratch/FR_654b.md: the
changed tokens are the two hunks of the note and nothing else.
(a) 5 (b), lines 1551 to 1564. "Equal budget" is now defined with two departures:
    - On the CPU, X1 ran 750 iterations over two linearizations (500 + 250) and F1 750 in one (--inner 2500), both
      stopped by the 1.8 h cap. So the pairs X1 / F1, and through their starts X2 / F2 and X3 / F3, are equal in
      iteration count but differ in the schedule of their first 750 iterations.
    - The fixed-c_l profile is compared with X2 / F2 at equal total count (21500 against 750 CPU + 20750 GPU).
    Checked against b_fit/fixc_c6f_m1.0e-03.log and b_fit/c6f_seg2.log (G133 (j) amendment: the linearize events, the
    checks and the last check at wall 6196 s and 6091 s) and run_c6f.sh line 27. The cap: --hours 1.8 = 6480 s. The LSQR
    loop breaks once the wall time passes the deadline less 60 s (long_solve.py lines 69 to 71, the same test in long_solve_fixcl.py; "end" at 6420 s and 6426 s).
    Only a check saves an iterate, so the iterations after the 750-iteration check were computed and discarded, and the
    saved fits are the 750-iteration checks. "the three long-fit drivers (long_solve.py,
    long_solve_fixcl.py and gpu_long_solve.py)" is as G134 required. CONFIRMED.
(b) 5, step 5, lines 1616 to 1620. "The free control F1 is segment 2 of the free run (run_c6f.sh in (b)), from the free fit:"
    with the command "python3 long_solve.py <free fit> <out> --nr 20480 --nt 720 --hours 1.8 --inner 2500 --check 250".
    This matches run_c6f.sh line 27, whose segments read and write c6f_shape.npz in place, so segment 2 starts from the
    segment 1 end. It also matches run_c6f_fixc.sh lines 8 to 12 and 69 to 73: X1 is "c6f_seg1 + d t", d = -1e-3, and "c6f
    segment 2 (free, from c6f_seg1 ...)" is the same-budget free control. So "the free fit" is the c6f segment 1 end in
    both commands. The start c_l agree: X1 5.575362611, F1 5.576362431, a difference of 9.998e-4. "Both were stopped by
    the 1.8 h cap after 750 iterations, X1 over two linearizations (500 + 250) and F1 in one" agrees with the logs.
    CONFIRMED.
Verdict: CONFIRMED (round A6). G133 (j) and the G134 "both" item are CLOSED. No measured value changed.

## G137 (2026-10-19T08:09:20Z). Diff audit FINAL_REPORT b74e084a -> 50bec0ba (lead NOTES 2026-10-19T08:01:19Z, round B: G135, C4)
Method: copy scratch/FR_50be.md (md5 50bec0ba1795ca7d646869dddb5ea5b1, 1698 lines); diff and word diff against
scratch/FR_b74e.md (scratch/diff_b74e_50be.txt): eight hunks, 24 changed token runs, all in items (a) to (g) of the note.
Every value checked against G135 and its addendum, and the 4-digit values against the unrounded numbers from
scratch/ns_profile.py.
(a) Timeline, lines 569 to 580. The entries 07:12 / 07:16 (G133, G134 heading times) and 07:55 / 07:57 (G135, G136) are
    right. "the free control F1 ran its 750 CPU iterations in one linearization, not two" is G133 (j). The 07:55 entry
    quotes 1.680, 2.41 / 2.50, 0.820, 0.59, 0.56, 1.32 and 0.69 as in G135. "J 0.56 times" is the eps 0.03 value (0.55 at
    eps 0.01). CONFIRMED.
(b) (iv), lines 697 to 705. "On that basis, and continued to the candidate's angular cap m <= 200 (4.3), the tested value
    5.6004662 is excluded at the attained level" is right (G114, G135 (2)). The next clause is REFUTED as worded: "no
    value between 5.5793640 and 5.6004662 was tested, so the upper end of the values not excluded lies in that gap".
    - Exclusion is a reading of tested values only. Read as "tested values not excluded", the upper end is 5.5793640,
      the left end of the gap. Read as all c_l, the clause asserts two things not measured:
      . that the values not excluded form an interval;
      . that the untested values above 5.6004662 are excluded.
    - Required, or equivalent: "no value between 5.5793640 and 5.6004662 was tested, and none above 5.6004662, so the
      largest tested value not excluded is 5.5793640 and the smallest tested value above it, 5.6004662, is excluded". The
      lower-end clause ("5.5524653 is not excluded and no smaller value was tested, so the interval has no measured lower
      end") is right as it stands.
(c) 4.1, lines 797 to 802: 0.820; 0.591 / 0.588; 0.562 / 0.545; 1.322 at 11250 x 384 (lobe point) and 0.691 at 16875 x
    512. All as G135 (3). "The residual does not distinguish the candidate's exponent or basis among the fits computed"
    meets C3. CONFIRMED.
(d) 4.3, nested-pair block, lines 996 to 1011.
    - Table checked against the unrounded values: 56 L2 2.79504e-6, whole-box 1.67571e-6 / 1.82486e-6, J 3.61200e-6;
      57 L2 1.32822e-6, whole-box 9.132499e-7 / 4.724736e-7, J 7.8073e-7; X3 1.61927e-6, 6.909148e-7 / 6.841004e-7,
      1.3882e-6; F3 1.66420e-6, 6.946974e-7 / 7.303302e-7, 1.4808e-6. Ratios 1.680 / 1.726, 2.412 / 2.499, 2.439, 0.798 /
      0.820, 1.315 / 0.647, 0.527, 0.973, 0.995 / 0.937, 0.937 and 1.028 (F3 / X3) are right.
    - One digit is wrong: 57's whole-box N_f at 11250 x 384 is 9.132e-7 (9.1324986e-7), not 9.133e-7. The cause is my
      G135 print, 9.1325e-7. Required: 9.132e-7.
    - Lead's point (i): the whole-box values of G135 are the A5 region "all, ya >= 0.006" (scratch/ns_profile.py, key
      'all,ya>=0.006'). Evaluation columns next to the y-axis are excluded, the convention of the profile above. So
      "Verifier values as in the profile above" is right.
    - Lead's point (ii): no N22500 q512 value of 57 is quoted (G135 (4)). CONFIRMED.
    - The sentences on the rule, the last-1000 changes (-0.96 / -0.61 percent), |h(P) - 1| <= 7.72e-7, the identity to
      3.3e-9, the near-P ratios and the lobe point (r 8.78, theta 0.30, on both configurations) match G135. CONFIRMED.
(e) 4.3 Interval paragraph, lines 1033 to 1035: "and so is its continuation to m <= 200 (... 2.412 and 2.499 times F3's)".
    CONFIRMED.
(f) 4.8, lines 1561 to 1572:
    - "One refinement step ... was done".
    - The thresholds 3.05 = 1.5 x 2.036 and 1.36 = 2.036 / 1.5, with "provided the fit had flattened" (it had,
      -0.96 percent, 4.3).
    - "1.680, between the thresholds, so this step does not separate them either", with the decrease read neither as
      evidence nor as a trend.
    - 57: 0.820 against 0.771; 0.59; 0.56 / 0.55 (0.545 rounds to 0.55); 1.32 / 0.69.
    This is G135 (1) and (3). CONFIRMED.
(g) Section 5. (b) adds "and the nested pair of 4.3" to the runs computed with the same GPU iteration. The last paragraph
    says "Partly done ... undecided (Q = 1.680 against the thresholds 1.36 and 3.05) ... Further nested discretizations
    ... were not run", and "The other rows of the fixed-c_l profile of 4.3 are on one basis (375 x m <= 150) at one budget
    (21500 iterations)" (56 and 57 are on m <= 200 at 42250). CONFIRMED.
C4 is MET on 50bec0ba, given (b) and (d): (P1) and (P2) are not separated, and one step of the experiment is reported as
done and read by the rule fixed before the run.
Verdict: CONFIRMED except two corrections: (b) the (iv) clause on the upper end, and (d) the digit 9.133e-7 -> 9.132e-7. No
other measured value is misquoted.

## G138 (2026-10-19T08:21:40Z). Diff audit FINAL_REPORT 50bec0ba -> ad925d3f (lead NOTES 2026-10-19T08:11:17Z, round B2: G137 (b), (d))
Method:
- Copy scratch/FR_ad92.md (md5 ad925d3f9936cb55a8ebce9822519979, 1699 lines). diff against scratch/FR_50be.md gives three
  hunks and no other change (scratch/diff_50be_ad92.txt). [OPEN] count 4, no trailing spaces, no em-dash.
- To check "none above 5.6004662 was tested on that basis", I listed every seven-decimal value of c_l in 5.55 to 5.61
  that occurs in the report. On the candidate's radial basis the fixed-c_l values are 5.5524653, 5.5604082, 5.5683739,
  5.5723653, 5.5743631, 5.5753626, 5.5783631, 5.5793640 and 5.6004662; the other values are free-fit c_l near 5.57636
  and 5.57637. The only other value above 5.5793640 is 5.5999914, the free-formulation continuation of the 244-function
  fit at 5.60 (4.3, line 1047), which is on another radial basis.
- The 136 earlier evaluations of line 825 span c_l 5.5752 to 5.6001, and the independent discretization of 4.6 is a
  separate construction. Neither is "that basis".
(a) (iv), lines 698 to 706: "no value between 5.5793640 and 5.6004662, and none above 5.6004662, was tested on that basis,
    so the largest tested value not excluded is 5.5793640 and the smallest tested value above it, 5.6004662, is
    excluded". Factual, and scoped to the basis as the list above requires (the 244-function value 5.5999914 lies in
    the gap, so the scope is needed). The lower-end clause is unchanged. CONFIRMED.
(b) 4.3 nested-pair table, line 1003: 9.132e-7 (9.1324986e-7). CONFIRMED.
(c) Timeline 03:48 entry, lines 525 to 527: "It widens the quoted interval up to 5.5793640, the largest value tested on the
    candidate's radial basis that is not excluded; the next value tested on it, 5.6004662, is excluded at this level
    (4.3)." This is true at 03:48 (row 39 had been read in G114) and now. Row 40 is on 375 radial functions with m <= 150,
    so "radial basis" (not "trial space") is the right scope. CONFIRMED. The old wording "lies between 5.5793640 and
    5.6004662" had the fault of G137 (b), and the lead found it.
Verdict: round B2 CONFIRMED. The two G137 corrections are in. C4 is MET on ad925d3f.

## G139 (2026-10-19T09:36:12Z). Row 49 dom9000g2 (dom9000g + 20750 iterations at its fixed c_l, rows to 9000 L): reading by lead NOTES 2026-10-18T23:22:40Z item 2
Run:
- gpu_chain.log "2026-10-19T09:17:16Z step 49 done": outer 9 it 750, total 20750 iterations, 24576 x 960. Solver objective
  1.11254e-6 on its rows, against dom9000g's 1.33439e-6 (0.834). The change over the last 1000 iterations is -0.21 percent.
- md5 1f5806c9ddb8d833db777299abfbbc45; my copy matches the chain line. R_shape 1e4 L, angular cap 200, L 7.6514239917,
  1/k 5.5753626106 (as c6g and dom9000g).
Method:
- My evaluator in dom9000g2's own convention (two-term closure at 1e4 L, k_self, VAUDIT_RFIT 9000 L, bands 1000 L to 9000
  L, 9000 L to 1e4 L, r > 1e4 L) at N11250 q384, N16875 q512 and N22500 q384.
- The formula-continued reading (no closure, suffix _frm49) at N16875 q512, N22500 q384 and N22500 q512 (the last for
  row 50).
- The 857-label J with the closure at N16875 q384 (jr_one.sh), vaxis, extra_checks at N11250 q384, code/far1_ver.py (nt
  16384) and scratch/far2_rel.py (nt 32768).
- dom9000g baselines: the same files of G91 (_frm44 for the formula reading). Readers: scratch/read_fit.py, and
  scratch/read4950.py (new; A5 regions with the arg max of N_f and N_v).
(a) Far band, the reading quantity. N_v maximum over 1000 L to 9000 L, formula continued, dom9000g2 / dom9000g:
    - 16875 x 512: 3.290e-8 / 3.199e-8 = 1.028 (at 1070 L, theta 1.5634);
    - 22500 x 384: 3.109e-8 / 3.035e-8 = 1.024 (at 1160 L, theta 1.5250).
    In the own convention: 1.028 and 1.023, and 1.018 at 11250 x 384.
    C at the axis (far1_ver): 6.559e-4 against 6.465e-4, ratio 1.015 (c6g 1.869e-2).
    Every ratio is in [0.8, 1.25] on both N >= 16875 configurations, so by the rule fixed before the run: "the budget does
    not lower the 9000 L row's far band further".
    The other bands follow the same way:
    - formula continued: 9000 L to 1e4 L 1.005 / 1.005; r > 1e4 L 1.002 / 1.002;
    - own convention, r > 1e4 L (in the closure): 2.30e-5, ratio 1.000.
    Higher orders at theta 1.56811 (far2_rel): q1 4.961e-4, q2 -14.656, q3 -3.461e4, relative 3.0e-6, 0.15 and 10.1 percent.
    dom9000g had 4.94e-4, -14.65, -3.46e4 and 3.0e-6, 0.15, 10 percent.
    The lead's own numbers (NOTES 09:25:04Z: 1.017 on 1000 L to 9000 L, 1.005 on 9000 L to 1e4 L, on other grids) agree with
    the reading.
(b) Ratios stated without attribution (rule: "ratios stated, no attribution"):
    - near-P N_f (|X - P| < 0.5), dom9000g2 / dom9000g:
      . 16875 x 512: 2.743e-7 / 4.485e-7 = 0.612;
      . 22500 x 384: 2.609e-7 / 4.512e-7 = 0.578;
      . 11250 x 384: 2.595e-7 / 4.451e-7 = 0.583.
    - 857-label J at 16875 x 384 with the closure: 5.275e-7 / 9.106e-7 = 0.579 (eps 0.03) and 5.474e-7 / 1.0199e-6 = 0.537
      (eps 0.01).
(c) Other values, for the record.
    - Whole-box N_f in the A5 region r <= 1000 (y-axis columns excluded; own convention, formula the same to 4 digits):
      . 16875 x 512: 4.411e-7, 0.984 of dom9000g. The maximum moved from next to P (dom9000g, r 8.458, theta 0.0074) to the
        lobe above P (r 8.74, theta 0.196);
      . 22500 x 384: 4.995e-7, 1.017 (lobe, r 8.736, theta 0.193);
      . 11250 x 384: 7.237e-7, 1.027 (lobe, r 8.784, theta 0.308).
      So the fall is next to P and the lobe above P is unchanged, as in G91 for dom9000g against c6g.
    - Against X3 (c6g) on the same configurations:
      . near-P 0.401 (16875 x 512) and 0.395 (22500 x 384);
      . whole-box r <= 1000 0.645 and 0.756;
      . J 0.380 / 0.342.
      dom9000g2 has 20750 + 20750 GPU iterations beyond X3, on other rows, so it is not an equal-budget comparison.
    - The raw maximum over all columns at 16875 x 512, 2 <= r <= 10, is 5.501e-7, in the column next to the y-axis (r 9.344,
      theta 1.5683). This is the evaluator's cancellation floor (4.3, 4.4), and A5 excludes it.
    - Centre (11250 x 384 extra_checks):
      . identity c_l 5.5753626108 (fixed 1/k 5.5753626106);
      . c_l from h(P) = 1 differs by -4.4e-8;
      . |E_c| <= 1.4e-9, |D2| <= 1.7e-9 over the five windows;
      . W_1 on the x-axis vanishes only at 8.6000651;
      . W_2/y >= 5.57557 on the y-axis; no open-quadrant cell with both components changing sign;
      . vaxis x* 8.6000654 (dom9000g 8.6000645).
    - h(P) - 1: +4.9e-8 (16875 x 512), -4.8e-9 (22500 x 384), +3.9e-7 (11250 x 384, N < 16875).
Verdict G139: values CONFIRMED as listed (my evaluator). Reading (a): "the budget does not lower the 9000 L row's far band
further" (1.028 / 1.024; C 1.015). (b): near-P 0.61 / 0.58 and J 0.58 / 0.54 of dom9000g, stated without attribution. Not
a candidate; no number of X3 changes.
- For the report (round D): if 4.4 or 4.5 lists fits whose residual maxima are below X3's, dom9000g2 is one (near P 0.40 of
  X3). It differs from X3 in budget and rows, so C3 (no implication that X3 has the smallest residual) must cover it.

## G140 (2026-10-19T10:10:51Z). Row 50 c6h9000 (c6h + 20750 iterations at its fixed c_l, m <= 250, rows to 9000 L): reading by lead NOTES 2026-10-19T00:16:58Z item 2
Run:
- gpu_chain.log "2026-10-19T09:43:55Z step 50 done": outer 9 it 750, total 20750 iterations, 24576 x 1200. Solver
  objective 4.70905e-7 on its rows; the change over the last 1000 iterations is -0.52 percent.
- md5 8eed5634a745e1329220b78086512c73; my copy matches the chain line. R_shape 1e4 L, angular cap 250, L 7.6514243984,
  1/k 5.5753626106.
- c6h9000 and dom9000g2 (G139) have equal total iterations (c6g + 41500) and the same rows. They differ in the angular
  cap (250 against 200). Their objectives on the rows are 4.709e-7 against 1.1125e-6.
Method:
- My evaluator in the fit convention (closure at 1e4 L, k_self, VAUDIT_RFIT 9000 L, bands as G139) and the
  formula-continued reading (_frm50), each at N16875 q512 and N22500 q512 (q512 throughout because m <= 250).
- The 857-label J with the closure at both configurations (jset2), vaxis, extra_checks at N16875 q512, far1_ver and
  far2_rel.
- Baselines: c6h (41; G96, G97) on the same two configurations; dom9000g2 _frm49 at N16875 q512 and N22500 q512 (the
  latter run for this comparison). Readers: scratch/read4950.py, plus a direct listing of the band regions with arg max.
(a) Interior, c6h9000 / c6h (rule: at most 1.1 on both N >= 16875 configurations in both quantities):
        config         A5 whole-box N_f, r <= 1000                 N_f within 0.5 of P
        16875 x 512    4.317e-7 / 4.228e-7 = 1.021 (lobe r 8.74)    1.602e-7 / 2.407e-7 = 0.665
        22500 x 512    4.988e-7 / 4.875e-7 = 1.023 (lobe r 8.736)   1.605e-7 / 2.256e-7 = 0.712
    The formula-continued reading gives the same values to 4 digits. All four ratios are at most 1.1, so by the rule fixed
    before the run: "the interior gain of the m <= 250 cap is kept with rows to 9000 L".
    - Both whole-box maxima are at the lobe above P (theta 0.19 to 0.20), as for c6h.
    - c6h9000 is c6h plus 20750 iterations on other rows, so the fall next to P (0.67 / 0.71) mixes budget and rows. The
      rule's wording "is kept" claims no more than the bound.
    - The lead's scans (whole-box 1.035 and 0.923 of c6h, other grids) do not contradict the reading.
(b) Far band, c6h9000 / dom9000g2. N_v maximum over 1000 L to 9000 L, formula continued (rule: [0.8, 1.25] on both means
    "the cap does not move the far band"; otherwise the ratio is stated):
    - 16875 x 512: 1.999e-8 / 3.290e-8 = 0.608;
    - 22500 x 512: 2.004e-8 / 3.282e-8 = 0.610.
    Outside [0.8, 1.25], so the ratios are stated: 0.61 on both. The lead's 0.621 (24576 x 576) agrees.
    Arg max, as the lead asked:
    - c6h9000: 8989 L, theta 0.633 (16875 x 512) and 8998 L, theta 0.621 (22500 x 512), at the outer end of its rows.
    - dom9000g2: 1070 L and 1141 L, theta 1.5634, the first evaluation column outside the y-axis cut (pi/2 - theta
      0.0074), at the inner end of the band.
    - In c6h9000's fit convention at 22500 x 512, the band maximum over all columns is 2.0033e-8 at 3944 L, theta 1.5683
      (next to the y-axis). With the y-axis columns excluded it is 2.0028e-8 at 8998 L. So these two maxima of c6h9000's
      band agree to 3e-4 (amended in G141: the earlier wording "the band is flat to 3e-4" was not measured).
    - Where the difference sits: next to the y-axis in the inner part of the band, dom9000g2 reaches 3.29e-8, and
      c6h9000 is at most 2.00e-8 everywhere in the band (at most 0.61 of dom9000g2's value there). Near the outer end the
      two rows are close: 9000 L to 1e4 L 2.272e-8 / 2.418e-8 = 0.940 and 2.289e-8 / 2.432e-8 = 0.941, both at about 9980
      to 9999 L, theta 0.62.
    - Beyond 1e4 L (formula continued): 0.975 / 0.977. In the own convention r > 1e4 L is in the closure (2.31e-5 for both).
    - C at the axis: 6.000e-4 against dom9000g2's 6.559e-4 (0.915) and c6h's 1.8657e-2 (0.032).
    - far2_rel at theta 1.56811: q1 4.690e-4, q2 -14.624, q3 -3.462e4; relative 2.8e-6, 0.15 and 10.1 percent, as
      dom9000g2.
(c) Ratios for the record.
    - 857-label J, c6h9000 / c6h:
      . 16875 x 512: 3.833e-7 / 5.002e-7 = 0.766 (eps 0.03) and 3.833e-7 / 5.886e-7 = 0.651 (eps 0.01);
      . 22500 x 512: 3.886e-7 / 5.040e-7 = 0.771 and 3.886e-7 / 5.974e-7 = 0.650.
      c6h9000's spread is the same at eps 0.1, 0.03 and 0.01, and largest at eps 0.3 (4.06e-7 / 4.11e-7).
    - Against X3 (c6g) on the same configurations: near-P 0.234 / 0.235; whole-box r <= 1000 0.631 / 0.730. Not equal
      budget: c6h9000 has 41500 GPU iterations beyond X3, a larger cap and other rows.
    - Centre (16875 x 512 extra_checks):
      . identity c_l 5.5753626108 (fixed 1/k 5.5753626106);
      . c_l from h(P) = 1 differs by -2.2e-8;
      . |E_c| <= 3.6e-10, |D2| <= 1.1e-9 over the five windows;
      . W_1 on the x-axis vanishes only at 8.6000642;
      . W_2/y >= 5.575565 on the y-axis; no open-quadrant cell with both components changing sign;
      . vaxis x* 8.6000643.
    - h(P) - 1: +5.3e-8 (16875 x 512), -5.1e-9 (22500 x 512).
Verdict G140: values CONFIRMED as listed (my evaluator). Reading (a): "the interior gain of the m <= 250 cap is kept with rows
to 9000 L" (1.021 / 1.023; near P 0.665 / 0.712). Reading (b): the ratio is stated, 0.61 on both N >= 16875 configurations
(outside [0.8, 1.25]). The difference sits next to the y-axis at the inner end of the band, where dom9000g2 has its
maximum. Not a candidate (lead 00:16:58Z item 1); no number of X3 changes.
- For the report (round D; the rule's item (c) allows it, since this audit exists before the presentation pass): any list of
  fits with residual maxima below X3's must include c6h9000 (near P 0.23 of X3), under C3 as for G139.

## G141 (2026-10-19T10:20:34Z). Diff audit FINAL_REPORT ad925d3f -> e4ca7b49 (lead NOTES 2026-10-19T10:16:17Z, round D: G139, G140)
Method:
- Copy scratch/FR_e4ca.md (md5 e4ca7b49, 1731 lines). The diff against scratch/FR_ad92.md has four hunks and no other
  change (scratch/diff_ad92_e4ca.txt: 581a582,596; 1029,1030c1044,1046; 1315c1331,1340; 1397,1416c1422,1448).
  [OPEN] count 4, as before. Every number in the hunks was compared with G137 to G140.
- For C3 I searched the whole file for "smallest", "lowest", "least", "minimum", "best" and "below X3", and read each
  hit in context.
(a) Timeline, lines 582 to 596.
    - 08:09 / 08:21 entry: matches G137 and G138 (two corrections, applied; no other quoted value changed). CONFIRMED.
    - 09:36 entry: 1.028 / 1.024 in [0.8, 1.25], "the further budget does not lower the far band"; near P 0.61 / 0.58;
      J 0.58. These are G139's values and its reading. CONFIRMED.
    - 10:10 entry: whole-box 1.02 (1.021 / 1.023); near P 0.67 / 0.71 (0.665 / 0.712); "kept"; far band 0.61, outside
      [0.8, 1.25], ratio stated; the difference sits next to the y-axis at the inner end of the band. These are G140's
      values and its reading. CONFIRMED.
(b) 4.3 list, lines 1044 to 1046. The free control of the 9000 L row (48), its continuation (49) and the m <= 250 row
    continued (50) are added, each marked "none a candidate". CONFIRMED.
(c) 4.4, lines 1331 to 1340 (row 50). Checked against G140:
    - 1.021 / 1.023; 0.665 / 0.712; "kept";
    - "the fall next to P mixes the further budget and the rows" (correct: 50 differs from c6h in both);
    - 0.608 / 0.610 against the 9000 L row continued at equal total iterations;
    - 3.29e-8 at 1070 L; at most 2.00e-8 (1.999e-8 / 2.004e-8); 0.94 over 9000 L to 1e4 L (0.940 / 0.941);
    - against X3: 0.234 / 0.235 and 0.631 / 0.730, with the statement that this is not an equal-budget comparison.
    One clause is not supported: "flat to 3e-4 from next to the y-axis to the outer end of its rows". What I measured
    (G140 (b), fit convention, 22500 x 512 only) is two maxima: the largest value over all columns, 2.0033e-8 at 3944 L,
    theta 1.5683 (next to the y-axis), and the largest value with the y-axis columns excluded, 2.0028e-8 at 8998 L. Two
    maxima that agree to 3e-4 do not make the band flat: values between them were not compared and may be lower. The
    error came from my own G140 wording ("the band is flat to 3e-4 between a point next to the y-axis and the outer
    end"), which is amended above. Required change: either drop the clause, or write for example "in the fit
    convention at 22500 x 512 its largest value next to the y-axis (3944 L) and its largest value away from it (8998 L,
    theta 0.62) agree to 3e-4". Either form is acceptable.
(d) 4.5, lines 1422 to 1448 (row 49). Checked against G139: 1.028 / 1.024 (16875 x 512, 22500 x 384); C 1.015; "does
    not lower its far band"; near P 0.612 / 0.578; J 0.579 (857 labels, eps 0.03, 16875 x 384); against X3 0.401 /
    0.395 near P, 0.645 / 0.756 whole box, 0.380 in J, with "not an equal-budget comparison". "X3 continued for 20750
    iterations on its own rows reads 0.993 to 1.003 of X3's over 1000 L to 9000 L and 1.0026 of X3's C at the axis":
    as in G98 and the earlier rounds. The pre-registered rule is quoted correctly. CONFIRMED.
(e) C3, the lead's question whether the two sentences against X3 meet my request. They do. 49 and 50 are each stated
    against X3 with the budget caveat, and the 4.3 list names them. The search finds no sentence saying that X3 has the
    smallest residual among the fits computed:
    - line 532 says the opposite;
    - lines 804 to 818 open with "The candidate is not the fit with the lowest whole-box N_f at every configuration"
      and end with "The residual does not distinguish the candidate's exponent or basis among the fits computed";
    - line 936 is selection rule (2), fixed before the X3 scans, which picks among kept fits of equal-budget pairs;
    - line 288 is a dated timeline entry (13:41, m <= 150 fits).
    Two optional suggestions (not conditions):
    - Line 804: "not the fit with the lowest whole-box N_f at every configuration" understates. The rows continued
      beyond X3's budget that the report compares with X3 are below it in whole-box N_f at the configurations read with
      at least 16875 radial points: the budget row and the m <= 250 row (4.4: lobe value against X3's maximum next to
      P), the m <= 250 row continued (0.631 / 0.730) and the 9000 L row continued (0.645 / 0.756). A clause such as
      "the rows continued beyond its budget (4.4, 4.5) are lower at the configurations with at least 16875 radial
      points" would say so.
    - Line 288: "keeps the lowest whole-box N_f measured" could read "of the fits measured by then".
Verdict: round D CONFIRMED except the clause of (c), which must be reworded or dropped. C3 is met with rows 49 and 50
included. No number of X3 changes.

## G142 (2026-10-19T10:27:29Z). Diff audit FINAL_REPORT e4ca7b49 -> 35da90ae (lead NOTES 2026-10-19T10:23:34Z, round E: G141 (c), (e))
Method:
- Copy scratch/FR_35da.md (md5 35da90ae, 1739 lines). The diff against scratch/FR_e4ca.md has four hunks and no other
  change (scratch/diff_e4ca_35da.txt: 285,290c285,290; 596a597,601; 804,818c809,825; 1338,1340c1345,1348).
- To check the claim of (b) as worded, I listed from my audit JSONs the whole-box N_f maximum of every fit with an audit
  at 16875 or 22500 radial points, divided by X3's on the same configuration. Three readings were taken: all evaluation
  columns ("all"); columns within 0.006 of the y-axis excluded ("A5"); and r <= 1000 with that exclusion. For the rows
  with an inverse domain at 1e4 L I used the canonical reading (formula continued, no closure; files _frm44 / 47 / 48 /
  49 / 50). The report's 4.3 and 4.4 residuals are that reading.
(a) 4.4, lines 1345 to 1348: "(in the fit convention at 22500 x 512 its largest value next to the y-axis, at 3944 L, and
    its largest value away from it, at 8998 L and theta 0.62, agree to 3e-4)". This is the wording required by G141 (c)
    and matches G140 (b) as amended. CONFIRMED.
(b) 4.1 bullet, lines 809 to 825: "Four rows continued beyond its budget are lower in whole-box N_f at the configurations
    read with at least 16875 radial points: the budget row and the m <= 250 row (4.4), the m <= 250 row continued with
    rows to 9000 L (4.4) and the 9000 L row continued (4.5); none of these is an equal-budget comparison." The rest of
    the bullet is unchanged in words (word diff). For the four rows named, the claim holds with the columns next to the
    y-axis excluded. As worded it is not correct, for two reasons. Both trace back to my own G141 (e) suggestion, which
    listed only four rows and omitted the convention.
    (1) Convention. At 16875 x 768, over all evaluation columns, the budget row reads 7.274e-7 (1.016 times X3's
        7.156e-7) and the m <= 250 row 9.820e-7 (1.372 times), both at theta 1.5692. That is the column next to the
        y-axis, the evaluator's cancellation floor of 4.4 note (a). With the columns within 0.006 of the y-axis excluded
        they read 0.610 and 0.597. X3's maximum is next to P, so for X3 the two readings agree. The claim therefore
        needs the qualifier "(columns within 0.006 of the y-axis excluded, as in 4.4)".
    (2) Count. "Four rows" reads as a complete count, but more rows continued beyond X3's budget are lower. Whole-box
        N_f, columns within 0.006 of the y-axis excluded, canonical reading, ratio to X3 at the configurations read with
        at least 16875 radial points:
          budget row c6g2 (4.2, 4.4)                       0.621 (16875 x 512), 0.610 (16875 x 768), 0.736 (22500 x 384), 0.737 (22500 x 512)
          X3 continued, inverse domain at 1e4 L, c6gR4 (4.5)  0.621, 0.741 (22500 x 384)
          m <= 250 row c6h (4.4)                           0.618, 0.597, 0.714
          its free control c6hF (4.4)                      0.612, 0.599, 0.705
          its continuation, rows to 9000 L, c6h9000 (4.4)  0.631, 0.730
          9000 L row dom9000g (4.4, 4.5)                   0.656, 0.744
          its free control dom9000gF (4.5)                 0.700, 0.743
          its continuation dom9000g2 (4.5)                 0.645, 0.756, 0.759
        Eight rows, every one below X3 at every configuration read with at least 16875 radial points. (For c6gR4,
        c6h9000, dom9000g, dom9000gF and dom9000g2 the all-column canonical reading is also below 1: at most 0.817.)
        The 300 L domain row is lower for r <= 1000 only (0.772, 0.846). Its whole box under the canonical law is 3.1
        times X3's, beyond r = 1000 (4.4). The 90 L row is higher everywhere. The nested-pair fit at 5.5683739 (0.691
        at 16875 x 512) is at the candidate's iteration count and is already in the bullet. A count of four implies that
        the others are not lower, which in the direction of C3 is the wrong implication.
    Required change: give the convention and either drop the count or name all eight. For example: "Rows continued
    beyond its budget are lower in whole-box N_f (columns within 0.006 of the y-axis excluded, as in 4.4) at the
    configurations read with at least 16875 radial points: the budget row and X3 continued with the inverse domain at
    1e4 L (4.2, 4.5), the m <= 250 row, its free control and its continuation with rows to 9000 L (4.4), and the 9000 L
    row, its free control and its continuation (4.4, 4.5); none of these is an equal-budget comparison."
(c) Timeline 13:41 entry, lines 285 to 290: "keeps the lowest whole-box N_f of the fits measured by then". The bullet is
    refilled, unchanged in other words. At 13:41 the fits measured were those on 244 and 375 x m <= 100 / 150, and X1
    (6.5e-7 to 7.0e-7) was the lowest. CONFIRMED.
(d) Timeline, lines 597 to 601, the 10:20 entry. The time is G141's (10:20:13Z), and the entry records the one correction
    and the C3 check. "the rows continued beyond the candidate's budget that are lower in whole-box N_f are named in
    section 4" will be correct once (b) is fixed. CONFIRMED subject to (b).
Verdict: round E CONFIRMED except (b), which must give the convention and either drop the count or name the eight rows.
No number of X3 changes.

## G143 (2026-10-19T10:29:16Z). Diff audit FINAL_REPORT 35da90ae -> 2fd94697 (lead NOTES 2026-10-19T10:28:45Z, round E2: G142 (b))
Method: copy scratch/FR_2fd9.md (md5 2fd94697, 1744 lines). The diff against scratch/FR_35da.md has two hunks
(scratch/diff_35da_2fd9.txt: 601a602,604; 809,825c812,830). A whitespace-token word diff shows only the two changes below.
[OPEN] count 4, trailing spaces 0, no em-dash.
(a) 4.1 bullet, lines 812 to 830: "Rows continued beyond its budget are lower in whole-box N_f (columns within 0.006 of the
    y-axis excluded, as in 4.4) at the configurations read with at least 16875 radial points: the budget row and X3
    continued with the inverse domain at 1e4 L (4.2, 4.5), the m <= 250 row, its free control and its continuation with
    rows to 9000 L (4.4), and the 9000 L row, its free control and its continuation (4.4, 4.5); none of these is an
    equal-budget comparison." This is the G142 (b) wording. It names the eight rows of the G142 table (c6g2, c6gR4, c6h,
    c6hF, c6h9000, dom9000g, dom9000gF, dom9000g2), and each is below X3 at every configuration listed there. The rest
    of the bullet is unchanged in words. CONFIRMED.
(b) Timeline, lines 602 to 604, the 10:27 entry: G142's time (10:27:29Z) and its one correction, as applied. CONFIRMED.
Verdict: round E2 CONFIRMED. The open text items of G141 and G142 are closed. C3 is met on 2fd94697.

## G144 (2026-10-19T10:30:52Z). Interim C6 check of the artifacts tree against 2fd94697: items for the final reassembly
Method: md5 of every file under lead/artifacts (1344 files), compared with my 08:31 manifest:
- identical (scratch/artifacts_manifest_now.txt, written 10:21:25Z);
- smoke tests of G131 (iii) rerun on a fresh copy (scratch/c6_rerun.sh, scratch/c6smoke2; gen_audit.log written 10:22:51Z):
  . quick_scan reproduces c_diagnostics/c6g_scan.json in all 13939 fields except the file name;
  . gen_audit reproduces my runs/audit/c6g_N11250_q384_R7.652e6.json in all 1679 keys except labels, file names and the
    timing field t_total.
Then I listed a_coefficients (90 files) against the fits named in section 4 of 2fd94697.
Missing, against 5 (a) "One file per trial named in section 4: the candidate X3 and every fit of the 4.3 table, ...":
- the nested pair of the 4.3 table, nst24g (56, c_l 5.6004662 on m <= 200; my copy md5 98b033aa6433a56b943356e0245844a4)
  and nsn8g (57, c_l 5.5683739; md5 29f70bbc0660d7c11f359885e7cc0086). Only their start shapes nst24_start / nsn8_start
  and their GPU logs (b_fit_gpu/runs/nst24g, nsn8g) are in the tree;
- the two data rows of 4.4 / 4.5, dom9000g2 (49, md5 1f5806c9ddb8d833db777299abfbbc45) and c6h9000 (50, md5
  8eed5634a745e1329220b78086512c73), and their GPU logs;
- when they end, the continuations 58 fxn16gb and 59 fxn24gb if the report states them.
Also for the final tree:
- d_evaluator/VERIFY_REPORT.md is the 06:39Z copy. INDEX.txt (d) and section 5 (d) call it "the verification record". It
  must be the final file (after my DONE entry), or section 5 must give its date and say that the current record is in
  the verifier's lane.
- b_fit_gpu/gpu_chain.log must contain the step 49, 50, 58 and 59 lines.
- 5 (a) lists the files by group ("the m <= 250 row and its free control, and the bounded-domain fits"). The data rows
  49 / 50, X3 continued with the inverse domain at 1e4 L (c6gR4, present), the nested pair and 58 / 59 should be named or
  covered by a group.
Verdict: C6 stays MET on the files present (md5 and reproduction unchanged). The final C6 check needs the missing shapes,
with md5 equal to the GPU chain lines, and the refreshed verification record. I will recheck by md5 against my copies.

## G145 (2026-10-19T10:42:39Z). External hostile-referee pass on FINAL_REPORT 2fd94697 (astra fin9), checked; items for the presentation pass
Method: question astra_q/fin9.md (overclaims, internal consistency of the headline numbers, scope in the opening lines, PROMPT
coverage); answer astra/fin9/answer.md (10:40Z). I checked each claim against scratch/FR_2fd9.md (= 2fd94697) and, for the
numbers, against my audit files runs/audit/c6g_N*_R7.652e6.json. Line numbers are of 2fd94697.
The referee found no sentence that calls the numerical evidence a proof, claims convergence to an exact profile, a domain
convergence study or a determined exponent, or says that X3 has the smallest residual (it reads 948 "the kept fit with the
lowest whole-box N_f" as restricted to the selection rules, and 812-829 as naming the lower fits). Its consistency table
agrees with mine: identity 3.2e-9 (717, 785, 932-935), span [5.5524653, 5.5793640] (715, 720, 990-999, 1060-1062), J ratio
0.937, whole-box N_f 6.83e-7 to 7.16e-7. It found no PROMPT requirement for the YES deliverable unaddressed. My checks of
its remaining points:
(a) Presupposition of an exact profile. 704-705 (item (ii)): "If the exact profile near the trials has a well-defined
    nonzero B_3, it is therefore not C^infinity". 786-788 (4.1): "if the exact profile is isolated (4.8), its exponent may
    lie outside the tested span". Both use the definite article for a profile whose existence is not established. Item
    (ii) is copied verbatim into the Summary by the finalize step. CONFIRMED as a wording defect. Required: "If an exact
    profile exists near the trials and has a well-defined nonzero B_3, it is not C^infinity near 0 and does not solve the
    strong setting." and "if such a profile exists and is isolated (4.8), its exponent may lie outside the tested span of
    (iv)."
(b) "at most" with values rounded down. 764-769: "at most 7.2e-7 in ... N_f (...) and 1.11e-6 in the second normalization
    N_v (...); for r <= 1000 at most 2.0e-7 with the evaluation columns next to the y-axis excluded". My maxima: N_v whole
    box 1.1112e-6 (16875 x 768, all columns, r 3.67e4, theta 1.5692); N_v r <= 1000 with the exclusion 2.0055e-7 (16875 x
    768, at P). The report's own table (1101-1105) has 2.01e-7 and 1.111e-6. 1413: "at most 1.32e-7 in N_f ... and 1.11e-6
    in N_v"; my far N_f maximum is 1.3233e-7 (16875 x 768, r 3.33e4, theta 0.846; table 1105: 1.320e-7 to 1.323e-7).
    The excess is 0.01 to 0.3 percent, but "at most" is then literally false. CONFIRMED. Required: 764-768 "and 1.111e-6
    in N_v", "at most 2.01e-7"; 1413 "at most 1.323e-7 in N_f ... and 1.111e-6 in N_v" (or "maximum" with the rounded
    value). The same applies to my own Summary block, which said "N_v <= 2.0e-7 for r <= 1000"; corrected there now.
    N_f "at most 7.2e-7" (max 7.1565e-7) and "2.5e-7 without that exclusion" (2.4848e-7) are correct as upper bounds.
(c) 831: "The problem answered is P_2." Read alone, "answered" suggests the problem has been settled. The sentence goes on
    to explain that the evidence for P_2 does not establish a profile of P_inf. Recommended: "The evidence concerns P_2."
(d) 1584-1585 (4.8): "in N_v it sits in the far field beyond the inverse domain, where the fits listed in 4.5 other than F1
    and W1 read 1.08e-6 to 1.17e-6". The 1.08e-6 to 1.17e-6 list of 4.5 (1418-1420) is of the fits with rows only to 900
    L. Section 4.5 also lists the rows to 9000 L and the inverse-domain continuation, which are not in that range. CONFIRMED
    as too broad. Required: "where the fits with rows only to 900 L listed in 4.5, other than F1 and W1, read 1.08e-6 to
    1.17e-6".
(e) 1377-1380: "the 857-label spread equals the supremum minus the infimum of J_eps over all labels on r = 20 at distance
    at least 1e-4 from the axes to about 1e-8, on the sampled labels and their parabolic refinement". The basis is stated,
    but "equals ... to about 1e-8" reads as a bound. Recommended: "is estimated, from the sampled labels and their
    parabolic refinement, to equal ... to about 1e-8".
(f) 773-775: "comparisons at equal iterations are in the second item below": the equal-iteration angular comparison is
    in the third bullet of 4.1 ("Raising the angular cap ..."). The lead's own presentation review (item 1.3) says the
    same. Recommended: "in the third item of 4.1".
(g) Opening lines: the referee notes that the first 60 lines name P_2 without defining it or saying that the posed strong
    setting is not answered. The finalize step (notes/finalize_report.py) puts the deliverable line and items (i) to (iv)
    of section 4 under the title, and the final STATUS text (notes/final_pass/status_final.txt) says the strong setting is
    not answered. With that step the point is met. I will check it on the final text.
Verdict: (a), (b) and (d) are required for C8 (accuracy of the final text); (c), (e) and (f) are recommended. None changes
a number of the endpoint. The lead may put these into the presentation pass.

## G146 (2026-10-19T10:46:12Z). External reproduction from the artifacts tree (astra repro9), checked; wrapper exit statuses fixed
Method: question astra_q/repro9.md (rerun section 5 of FINAL_REPORT from unchanged copies of the artifacts tree, single
thread, outer timeout 540 s); answer astra/repro9/answer.md with REPRODUCTION.md and evidence/commands.jsonl. The external
runs used Python 3.9.25, NumPy 2.0.2, SciPy 1.13.1 and an address-space cap of 2.0e9 bytes (ulimit -v 1953125), stricter
than the 16 GB of this run.
(a) Reproduced. md5 of a_coefficients/c6g_shape.npz 15f8095f7e79dbfa0c50d75e5fe8997a (X3) and c6gF_shape.npz
    0398af3f08a2a4f75e42c846edbaa375 (F3), as in section 5 (a). From d_evaluator/code/extra_checks.sh at 11250 x 384:
    identity c_l 5.575362607380289 (stored 5.575362610641546, difference -3.26e-9); c_l from h(P) = 1 5.575362614332569
    (+6.95e-9 above the identity value); x* 8.600063803562309 from the traces; centre defects E_c <= 5.91e-9 and
    D2 <= 5.11e-9. These agree with my own runs (G131, runs/audit/c6g_extra.log) and with the report. CONFIRMED.
(b) Not reproduced externally: quick_scan.py 32768 640 and 24576 960 (b_fit), vaudit.py inside gen_audit.sh, and
    vzeros.py inside extra_checks.sh. Each failed allocating a 160 to 180 MiB array under the 2 GB cap, after 2 to 85 s.
    This is a memory failure, not a numerical disagreement. Under ulimit -v 16000000 here, quick_scan 32768 640 and
    gen_audit.sh ran from a copy of the tree and reproduced the stored outputs (G131 (iii)), and vzeros.py completed on
    X3 in my lane (runs/audit/c6g_extra.log, runs/audit/c6g_zeros.json, 2026-10-18T15:12Z). OPEN only in the sense that section 5 does not state the memory needed; I am
    measuring the peak RSS of these three commands on a fresh copy of the artifacts (scratch/rss_measure.sh, queued after
    the 58 / 59 audits) and will give the numbers in a later entry.
(c) CONFIRMED defect in my wrappers. code/gen_audit.sh and code/extra_checks.sh ran their python steps in sequence without
    checking exit codes and returned 0. gen_audit logged 'echo "$(date -u ...) end <name> exit $?"'; bash expands $?
    after the $(date) substitution in the same word list, so it is the status of date (0), and the log read "exit 0"
    even when vaudit failed (checked: 'false; echo "$(date) exit $?"' prints exit 0). Fixed now in my code/ (old versions kept as scratch/gen_audit_pre_rc.sh and
    scratch/extra_checks_pre_rc.sh): each python step's exit code is written to the log (gen_audit: "end <name> exit
    gen_shape <rc> vaudit <rc>"; extra_checks: "<script> exit <rc>" per step), and the script exits 1 if any step failed.
    Nothing else changed; the numerics are untouched. The same logging pattern is in most of my job scripts under
    scratch/ (jset_fn.sh, jrow.sh, j4x.sh, j5x.sh and others), so every "exit 0" line in runs/audit/jS.log and the other
    job logs carries no information. None of my verdicts depended on those lines: each reading used the JSON or log
    contents, and a failed step leaves no JSON. Check made now: every "start <name>_jr" in jS.log has its _jd2.json and
    _ax.json, and every "end <name>" in runs/audit/gen_audit_*.log has its <name>.json (the only exceptions are the
    58 jset run started at 10:46:52Z, still running); the only python traceback in runs/ is runs/gen/prof_shape_R1e7_N3520.log
    (2026-10-17T20:58Z, an exploratory profile never cited in this report). The copies in the artifacts tree
    (d_evaluator/code) are the old versions; the lead should re-copy these two files at the final assembly (the
    assembler's relative-cd rewrite applies unchanged, since the first lines are the same).
(d) Recommended for section 5: state (1) the dependency versions already given in section 0 (Python 3.9.25, NumPy 2.0.2,
    SciPy 1.13.1) and the single-thread settings (OMP_NUM_THREADS=1 etc.); (2) the memory needed, from (b); (3) that the
    internal timeouts of the evaluator wrappers are 1200 s (mk_traces, vd14, vzeros) and 2400 s (vaudit), so a rerun
    should allow up to that time per step.
Verdict: the identity, h(P) root, source location and centre checks are reproduced externally from the artifacts; the
residual scans are not contradicted, they did not run at 2 GB. (c) is fixed. (d) is a presentation item for section 5.

## G147 (2026-10-19T11:06:52Z). Budget continuations 58 fxn16gb / 59 fxn24gb: reading by SPEC v4.18 (G130), and 58 against X3
Method: GPU chain steps 58 / 59 (lead's gpu_long_solve.py, 20480 x 720, inner 2500, damping 1e-8) continue rows 54 fxn16g
(c_l 5.5604082) and 55 fxn24g (c_l 5.5524653) for 21500 iterations each at the stored c_l (43000 in all). "step 58 done"
10:45:23Z, "step 59 done" 10:46:40Z; both logs have an "end" event at total_its 21500. My copies runs/gen4/gpu/
fxn16gb_shape.npz md5 0c57669fc0f4c24894a09043ade11306 and fxn24gb_shape.npz md5 3ef7078f95aaba2c943bdedd836a1878 match
the chain lines. Audits by scratch/jrow.sh with the corrected wrappers (G146 (c); every python step logged exit 0):
gen_audit at 11250 x 384 and 16875 x 512 (A5 regions), 857-label J at 16875 x 384 (jset), extra_checks at 11250 x 384,
far1_ver. Reading by scratch/read5859.py; the L2 objective is the "actual" value of the last check in each GPU log.
Comparison with X3 by scratch/cmp_x3.py on the same audit files.
(a) Values for round C:
      L2 objective at 43000 iterations: 58 2.2009e-6, 59 2.2121e-6 (ratio 59/58 1.0051; the lead's prediction, recorded
        before the runs, was 1.00 to 1.15).
      Whole-box N_f, 11250 x 384 and 16875 x 512 (columns within 0.006 of the y-axis excluded; the same values over all
        columns): 58 1.167e-6 and 6.311e-7; 59 1.344e-6 and 1.301e-6 (ratios 59/58 1.152 and 2.062).
      Change of the objective over the last 1000 iterations (20500 to 21500): 58 -0.148 percent, 59 -0.338 percent.
    So L2(59) > L2(58) and the whole-box N_f of 59 is above 58's on both configurations: by SPEC v4.18 the reading is
    "kept at twice the budget". In the template of notes/edit_round_s7c.py: L58 '2.2009e-6', L59 '2.2121e-6', NF58
    '1.167e-6, 6.311e-7', NF59 '1.344e-6, 1.301e-6', CH58 '-0.148', CH59 '-0.338', VERDICT 'kept', DISAGREE_CFG ''.
    The other measures agree in direction: 59/58 is 2.42 / 2.54 within 0.5 of P, 1.16 / 2.06 in N_v for r <= 1000, and
    2.31 / 2.38 in J (eps 0.03 / 0.01). Against their starts, 58/54 is 0.804 in L2 and 59/55 0.670.
(b) The margin in L2 is small and has shrunk at every linearization. L2(59) - L2(58) at the outer boundaries of the
    continuation (iterations 0, 2500, ..., 20000, then 21500): 5.63e-7 (ratio 1.206, rows 54 / 55), 3.34e-7, 2.46e-7,
    1.82e-7, 1.37e-7, 9.87e-8, 6.80e-8, 4.05e-8, 1.71e-8, 1.12e-8. Over each of the last four complete linearizations it
    fell by 3.8e-8, 3.1e-8, 2.8e-8 and 2.3e-8, each more than the 1.12e-8 that remains; over the last 2500 iterations 59
    fell by 0.72 percent and 58 by 0.32 percent. The rule fixed before the runs reads "kept", and that reading stands. The
    order in L2 is a fact at 43000 iterations only. These numbers do not show that it would persist one linearization
    further. The order in whole-box N_f has a large margin (1.15 and 2.06) but was measured only at the end.
(c) The G130 limit, to be stated with the reading: neither continuation is at equal budget with F2, and both rows may still
    be falling. So "kept at twice the budget" concerns fits from transplanted starts at a stated budget. It does not say
    where an objective minimized over shapes at fixed c_l has its minimum over c_l. The template's C43 sentence says this.
(d) Required for C8 (accuracy of round C):
    (1) 4.3 (C43 sentence): add the margin and its history, for example "The L2 gap between them fell at every
        linearization of the continuation, from 5.63e-7 at its start to 1.12e-8 (ratio 1.005); each of the last four
        linearizations reduced it by more than what remains, so the order in L2 is a fact at this budget only."
    (2) (iv) (IVC sentence, copied into the Summary by the finalize step): "keep that order in the L2 objective and the
        whole-box N_f" is true but, read alone, implies a margin it does not have. For example: "Continued for a further
        21500 iterations at their exponents, the fits at 5.5524653 and 5.5604082 keep that order in the whole-box N_f
        and in the L2 objective, the latter by 0.5 percent, a margin that shrank at every linearization (4.3)."
    (3) 4.1, the bullet "The candidate is not the fit with the lowest whole-box N_f at every configuration": 58 is lower
        than X3 at the one configuration with at least 16875 radial points read for it. On my audit files (ratios to X3
        on the same configuration): at 16875 x 512 whole-box N_f 0.9225 (6.311e-7 against 6.841e-7; columns next to the
        y-axis excluded or not, the same values; 58's maximum is at the off-axis lobe, r 8.80, theta 0.304), N_f within
        0.5 of P 0.750, N_v for r <= 1000 0.925, N_v beyond r 1000 1.025; J at 16875 x 384 0.800 (eps 0.03, 1.110e-6
        against 1.388e-6) and 0.775 (eps 0.01). At 11250 x 384 its whole-box maximum is 1.689 times X3's, at the
        under-resolved off-axis lobe (r 8.77, theta 0.311); within 0.5 of P 0.823. The bullet names every row lower
        in whole-box N_f at these configurations (G142 (b)). It must name 58 as well, for example after the 5.5683739
        sentence: "The fixed-c_l fit at 5.5604082 on the m <= 150 basis continued to 43000 iterations (4.3), not a
        candidate, has whole-box N_f 0.92 times the candidate's at 16875 x 512 (at the off-axis lobe), N_f within 0.5
        of P 0.75 times, N_v for r <= 1000 0.92 times and J (at 16875 x 384) 0.80 (eps 0.03) and 0.77 (eps 0.01) times;
        at 11250 x 384 its whole-box maximum is 1.69 times the candidate's, at the under-resolved off-axis lobe. It is
        not an equal-budget comparison." 59 is above X3 on every measure (whole-box N_f 1.95 / 1.90, J 1.85).
        The closing sentence of the bullet ("The residual does not distinguish the candidate's exponent or basis among
        the fits computed") already covers the point and stays true.
(e) Checks on the two fields (extra_checks at 11250 x 384, far1_ver). Identity c_l against the stored value: 58
    5.560408209 against 5.5604082120, 59 5.552465285 against 5.5524652878 (both -3.2e-9). c_l from h(P) = 1 on the
    traces: 58 +5.1e-8, 59 -7.5e-7 from the identity value (h(P) - 1 = +6.2e-7 / +1.27e-6 at 11250 x 384 and +6.3e-8 /
    +2.2e-7 at 16875 x 512, consistent with their fixed c_l). x* 8.5884800 / 8.5823221. Centre relations (vd14, five
    windows): |E| <= 2.3e-9 and |D2| <= 3.7e-9 absolute, relative defects <= 1.0e-8. (Hmin) on the evaluation grid
    (vzeros): no open-quadrant cell where both components of W change sign, min W_2/y on the y-axis 5.5606 / 5.5527
    (> 0). C at the axis (far1_ver, 16384 angles) +0.019190 / +0.019605 (54 / 55 +0.019530 / +0.019561; X3
    +0.018687). Both are ordinary fields of the fixed-c_l profile; neither is a candidate (SPEC v4.18).
Verdict: CONFIRMED by the rule fixed before the runs: "kept at twice the budget". (d) (1) to (3) are required wordings
for round C. The interval of tested c_l values not excluded, [5.5524653, 5.5793640], and the exclusion of 5.6004662 are
unchanged (these rows are not equal-budget comparisons). No number of X3 changes.

## G148 (2026-10-19T11:21:52Z). Diff audit FINAL_REPORT 2fd94697 -> 897d2ab3 -> 34d41433 (lead NOTES 10:55:55Z rounds F / F2, 11:10:32Z round C)
Method: word diffs (git diff --no-index --word-diff, whitespace re-wrapping not shown) scratch/fr_wd_2fd9_34d4.txt and
scratch/fr_wd_897d_34d4.txt of my copies scratch/FR_2fd9.md, FR_897d.md, FR_34d4.md (md5 2fd94697, 897d2ab3, 34d41433);
every changed word read against the review item it answers. Numbers against my audit files runs/audit/c6g_N*_R7.652e6.json,
the G147 audit files (scratch/cmp_x3.py, six-digit ratios recomputed), the lead's scans of X3 in lead/artifacts
(c_diagnostics/c6g_scan.json, c6g_scan960.json; c_farfield/band_nv_c6g_R1e6.json), and the lead's quick_scan run by me on
the copy scratch/rss (scratch/qs_cmp.sh; outputs scratch/qs_cmp/qs_<nr>_<nt>.json, empty stderr) at the radial and
angular counts of my configurations. Line numbers of 34d41433 unless stated.
(a) Round F (a) to (h): every hunk listed in the NOTES is present and does what the review item asks; the word diff shows
    no other change. Checked in particular: the 07:59 entry ("were not used in that check (the same fits read with the
    formula continued are reported in 4.4)"); "1000 <= r <= 7652 (1000 L)" twice; the 10:20 entry now names what was
    checked; the evaluator names defined once in the conventions; the two-term closure defined at first use in 4.2;
    "the under-resolved off-axis lobe near (8.4, 2.7)" (X3's 11250 x 384 maximum at r 8.784, theta 0.3076 is
    (8.37, 2.66)); "ratios between 1/1.5 and 1.5" (the 2-10 ratio 0.62 is below 1/1.5); "the N_f residual within 0.5 of
    P is 3.9e-7" for the 300 L fit; the two "except the domain columns read in each fit's own convention" sentences; the
    4.7 "Forgotten far-field terms" sentence (pointers only; "inverted to 1e6 L" is my R = 7.652e6); "read by the
    selection rule" for "decisive"; 5 (a) to (d) lists. 5 (b) "the vector updates of LSQR and the column-scaling probes
    carried out on a GPU": gpu_long_solve.py (md5 f26dde2d) forms the probe sums, the scaling and the LSQR vectors as
    torch tensors on the device; the probe signs are drawn by numpy (seed 8128 + linearization). CONFIRMED.
(b) Round F2 (i), (k), (m): the G145 (a), (c), (d), (e), (f) wordings as required or recommended; the 10:29, 10:30, 10:42
    and 10:46 timeline entries agree with G143, G144, G145 and G146 (10:30: "every file unchanged since the 08:31 check",
    the fresh-copy reproduction and the listed items of G144; 10:42: three required corrections and three recommended
    changes in 4.1 and 4.4b; 10:46: a memory failure under the 2 GB cap, not a disagreement). (l): Python 3.9.25, numpy
    2.0.2, scipy 1.13.1 and torch 2.8.0 are the versions of the python3 used here; the time limits 2400 s (vaudit.py in
    gen_audit.sh) and 1200 s (mk_traces.py, vd14.py, vzeros.py in extra_checks.sh) are those of code/ and of the
    artifacts copies. CONFIRMED.
(c) Round F2 (j), the bounds of 4.1 and 4.5 against both evaluators.
    Erratum to G145 (b): the values I gave as required, 1.111e-6 and 1.323e-7, are themselves below my maxima 1.1112e-6
    and 1.3233e-7. The installed 1.112e-6 and 1.324e-7 are correct upper bounds; the 4.4 table entries (1.111e-6 as one of
    four configuration values, 1.320e-7 to 1.323e-7 as a range) are roundings of single values and are right as they are.
    - N_v 1.112e-6 (all r, all columns): my maxima 1.0897e-6, 1.1014e-6, 1.1112e-6, 1.0932e-6, 1.1029e-6 (11250 x 384,
      16875 x 512, 16875 x 768, 22500 x 384, 22500 x 512); the lead's far-field scan (band_nv, 24576 x 576, inverse to
      1e6 L) 1.0922e-6 over 1000 L to 9000 L, 9.65e-7 at 9000 L to 1e4 L and 9.27e-7 beyond. The lead's quick_scan stops at
      r = 1000 L. Bounds both. CONFIRMED.
    - N_f 1.324e-7 for r > 1000: my maxima 1.3196e-7 to 1.3233e-7 (r 3.24e4 to 3.33e4, theta 0.844 to 0.846). The lead's
      scans read 1.30e-8 over 1000 <= r <= 1000 L and have no N_f reading beyond 1000 L. Bounds every reading that exists.
      CONFIRMED.
    - N_f 7.2e-7 (whole box) and N_v 2.01e-7 (r <= 1000, columns next to the y-axis excluded): they bound my evaluator
      (7.1565e-7 and 2.0055e-7, both at 16875 x 768, r 8.5277, theta 0.00818), NOT the lead's scans. The lead's scans
      read, at the same place: N_f 6.9355e-7 (32768 x 640, r 8.5259, theta 0.00736) and 7.2695e-7 (24576 x 960, r 8.5267,
      theta 0.00818); N_v over r <= 1000 L 1.9432e-7 and 2.0370e-7 (all columns; the lead's scan has no y-axis floor, its
      y-strip N_v is 7.5e-8). Section 5 step 3 tells the reader to run exactly these two scans, which print 7.27e-7
      against "at most 7.2e-7".
    Cause: the convention, not the sampling. My 16875 x 512 and 16875 x 768 configurations evaluate on 2560 and 3840
    angles on the circle, i.e. the same angles as the lead's 640 and 960 intervals on the quarter. At my radial counts the
    lead's scan reads 6.9335e-7 (16875 x 640, r 8.5293), 7.2490e-7 (16875 x 960) and 6.9451e-7 (22500 x 640), 1.013,
    1.013 and 1.016 times my maxima at the same angles; over the radial count its values at 640 angles agree to 0.2
    percent (6.9335e-7, 6.9451e-7, 6.9355e-7 at 16875, 22500, 32768 radial points, r 8.526 to 8.529), as do mine at the
    same angles (6.8410e-7, 6.8324e-7 at 16875, 22500). The scan evaluates the trial in the fit's own convention:
    centre_fit.load_shape builds the shape with R = 1000 (L) and Shape.evaluate computes the velocity on r <= 1000 L with
    the exterior tail of exponent k. My evaluator in that convention (G93 addendum, runs/audit/c6g_N16875_q512_
    R7.652e6_rbcloB.json, closure at 1000 L) reads 6.9059e-7 in N_f and 1.9351e-7 in N_v at the point of my canonical
    maximum (canonical 6.8410e-7 and 1.9170e-7, ratio 1.0095); the lead's 16875 x 640 value is 1.004 times that. In the
    same convention the two evaluators agree to 0.4 percent; the canonical law, which is the claim of 4.1, reads at most
    7.16e-7 on my configurations.
    Required for C8 (a reader who runs step 3 must not find a value above a stated "at most"):
    (1) 4.1, 794-799: say whose reading the bounds are, for example "(6.83e-7 to 7.16e-7 over the three finer evaluation
        configurations of the verifier's evaluator; ...)" and add after the sentence that ends "including the
        neighbourhood of the source point P.": "The lead's scans of 5 (c) read the trial in its fit's own
        convention (the two-term exterior beyond 1000 L, 4.4); at the same point they give 6.94e-7 and 7.27e-7 in N_f and 1.94e-7 and 2.04e-7 in N_v
        (32768 x 640 and 24576 x 960), and in that convention the verifier's evaluator reads 1 percent above its
        canonical value there."
    (2) Section 5 step 3: state the convention and what the scans print on the candidate, for example "they read the
        fit's own convention (4.4) and on the candidate print whole-box N_f maxima 6.94e-7 and 7.27e-7 next to P".
    Not affected: 4.4 states that its residuals are the verifier's evaluator; 4.8 (X3's maxima within 0.5 of P 6.5e-7 to
    7.2e-7, pointing to 4.4) and the 4.3 table are on my evaluator; the timeline entries quote my evaluator.
(d) Round C (G147). Installed values equal G147 (a): L2 2.2009e-6 / 2.2121e-6 (ratio 1.005), whole-box N_f 1.167e-6 /
    1.344e-6 (11250 x 384) and 6.311e-7 / 1.301e-6 (16875 x 512), -0.148 / -0.338 percent, "kept at twice the budget",
    the gap 5.63e-7 to 1.12e-8, identity 3.2e-9; (iv) is my G147 (d) (2) wording and "that order" refers to the preceding
    sentence (L2 objective and whole-box N_f at 5.5524653 above those at 5.5604082); the timeline time 11:06 is G147's;
    5 (a), (b) name the two continued fits. Two of the installed statements carry my own errors and must be corrected:
    (1) 4.3, 1066-1067: "each of the last four linearizations reduced it by more than what remains" is false as written.
        The continuation has nine linearizations, eight of 2500 iterations and a last one of 1500. The gap fell by
        3.79e-8, 3.07e-8, 2.75e-8 and 2.34e-8 over the last four complete ones (as G147 (b) says) and by 5.9e-9 over the
        last one (1.7104e-8 to 1.1241e-8), which is less than the 1.12e-8 that remains. My G147 (d) (1) example dropped
        "complete". Required: "each of the four complete linearizations before the last reduced it by more than the
        1.12e-8 that remains (the last, of 1500 iterations, by 5.9e-9), so the order in L2 is a fact at this budget only."
    (2) 4.1, 861-865: two three-digit ratios are mis-rounded (G147 (d) (3) gave them from four-digit displays). Exact:
        whole-box N_f 0.922489, within 0.5 of P 0.750239, N_v for r <= 1000 0.924469, J 0.799918 (eps 0.03) and 0.774485
        (eps 0.01), at 11250 x 384 1.688600 and 0.823419. Required: "N_v for r <= 1000 0.924 times" and "0.774 (eps 0.01)";
        the others are right. (N_v for r <= 1000 needs no column qualifier: on both 58 and X3 at 16875 x 512 the value is
        the same with and without the y-axis columns.)
    Recommended: the timeline 11:06 entry uses "(Hmin)", defined in R9 of section 3; "(the minimal configuration, R9)"
    would help a reader of the timeline.
Verdict: rounds F and F2 CONFIRMED; (j) CONFIRMED for 1.112e-6 and 1.324e-7 on both evaluators, and for 7.2e-7 and
2.01e-7 on the verifier's evaluator only, with (c) (1), (2) required. Round C CONFIRMED except (d) (1), (2), required
(both are my errors in G147 (d)). No number of the endpoint changes. Peak memory of the section 5 steps: separate entry
(measurement running; 14.4 GB for gen_audit at 16875 x 768).

## G149 (2026-10-19T11:31:07Z). Peak memory and wall time of the commands of FINAL_REPORT section 5 steps 1 to 3 (G146 (b), (d))
Method: a fresh copy of the lead's artifacts tree (a_generator, b_fit, d_evaluator, a_coefficients/c6g_shape.npz, md5
15f8095f) in scratch/rss; every command of steps 1 to 3 on the candidate run there as written, one at a time, under
/usr/bin/time -v (GNU time; "Maximum resident set size" is the largest resident set of any single process of the
command, in KiB), with OMP_NUM_THREADS=1 and an address-space limit ulimit -v 16000000 (KiB, 15.3 GiB). Scripts
scratch/rss_measure.sh, scratch/rss_measure2.sh; log scratch/rss/rss.log, GNU time records scratch/rss/*.time. Step 1
was run per configuration for the two largest configurations and the smallest (gen_audit.sh runs the configurations
of one call one after the other, so the peak of the full step-1 call is the largest single configuration). Every
command exited 0.
    step  command (on c6g)                            peak RSS (KiB)   (GiB)   wall
    1     gen_audit.sh 11250 384 479                      4913308       4.69   1:41
    1     gen_audit.sh 16875 768 959                     14433968      13.77   7:49
    1     gen_audit.sh 22500 512 639                     12845080      12.25   5:16
    2     extra_checks.sh 11250 384 479                   3746996       3.57   1:46
    2     vb3ibp.py <tag>_traces.npz                        69460       0.07   0:02
    2     gen_shape.py 16875 384                           269944       0.26   0:07
    2     vaxis.py 479                                    5566052       5.31   2:06
    2     vchar_dense.py 479 20 737 60 1e-4               5811468       5.54   5:10
    3     quick_scan.py 32768 640                         7000672       6.68   0:15
    3     quick_scan.py 24576 960                         7768408       7.41   0:17
The peak RSS of gen_audit is 1.11 to 1.14 KiB per evaluation point (N x angular points) at the three measured
configurations, so the three not measured (16875 x 384, 16875 x 512, 22500 x 384) need about 7 to 9.5 GiB; this is
an extrapolation, not a measurement. The wall times are within the stated ones ("2 to 8 minutes each", "about 2
minutes", "about 7 seconds, 2 minutes and 6 minutes", "under 30 seconds each").
Outputs (scratch/rss_cmp.py, all numeric and string leaves of each JSON except file names and timings): the three
gen_audit JSONs equal my stored runs/audit/c6g_N11250_q384, c6g_N16875_q768, c6g_N22500_q512 JSONs exactly (1674
leaves each, no difference); the vaxis and vchar_dense JSONs equal c6g_N16875_q384_R7.652e6_ax.json and _jd2.json
exactly (54 and 16302 leaves); the vzeros JSON equals c6g_zeros.json; the extra_checks log equals runs/audit/
c6g_extra.log line by line after removal of timestamps and the tag; vb3ibp.py on the new traces equals vb3ibp.py on
runs/gen4/c6g_traces.npz exactly; the two quick_scan outputs equal the lead's c_diagnostics/c6g_scan.json and
c6g_scan960.json exactly (13938 and 10522 leaves).
Erratum to G148 and the 11:24 WORKLOG / RUN_STATUS lines: "14.4 GB" and "14.43 GB" read the KiB count as 1e6 bytes per
GB; the value is 14433968 KiB = 13.77 GiB (14.78e9 bytes).
Statement for section 5 (CONFIRMED by the above as a statement of fact on this machine): "The largest step, gen_audit.sh
at 16875 x 768, needs 13.8 GiB of resident memory (12.3 GiB at 22500 x 512, 4.7 GiB at 11250 x 384, at most 7.5 GiB for each
command of steps 2 and 3); all steps ran under an address-space limit of 15.3 GiB (ulimit -v 16000000) and reproduced the stored
outputs exactly." Any wording that states the 13.8 GiB maximum and the limit under which the steps ran is acceptable;
a wording that names only the 2 GB failure (G146 (b)) is not wrong but leaves the reader without the requirement.
Verdict: CONFIRMED (peak memory measured; every reproduced output equals the stored one).

## G150 (2026-10-19T11:34:14Z). Diff audit FINAL_REPORT 34d41433 -> 7fe24302 -> e240e4b6 (lead NOTES 11:25:36Z round H, 11:32:16Z round G)
Method: word diffs scratch/fr_wd_34d4_e240.txt (6 hunks) and the two single-step diffs (5 hunks for round H, 2 for round
G) of my copies scratch/FR_7fe2.md, scratch/FR_e240.md (md5 7fe24302, e240e4b6); every changed word read against G148
and G149. Line numbers of e240e4b6. Checks: [OPEN] 4 lines (5, 7, 11, the "[OPEN] later entries" line), forbidden
strings 0, trailing spaces 0, lines over 120 characters 99 (the lead's count).
(a) Round H, G148 (c) (1), 4.1 lines 804-812: "over the three finer configurations of the verifier's evaluator" and the
    sentence on the lead's scans. Checked: the fit's own convention of quick_scan is the two-term closure at 1000 L
    (centre_fit.load_shape sets tail_terms = 2 and R = 1000; the 4.2 definition at line 938 is the same); 6.94e-7,
    7.27e-7, 1.94e-7, 2.04e-7 are the lead's 6.9355e-7, 7.2695e-7, 1.9432e-7, 2.0370e-7; "next to P" holds for both
    normalizations (on my evaluator both maxima are at r 8.5277, theta 0.00736, 0.073 left of P and 0.063 above the
    axis, with ratio N_f / N_v 3.569 there; the lead's scan prints only the N_f location, and its ratio of the two
    maxima is also 3.569); "1 percent" is my 1.0095. CONFIRMED.
(b) Round H, G148 (c) (2), section 5 step 3, 1764-1765: "They read the trial in its fit's own convention (the two-term
    closure at 1000 L, 4.4) and on the candidate print whole-box N_f maxima 6.94e-7 and 7.27e-7 next to P (4.1)." The
    "whole box" of the scan is r <= 1000 L; the scan's maximum over its box is the printed all/all value, as stated.
    CONFIRMED.
(c) Round H, G148 (d) (2), 4.1 line 873: 0.924 and 0.774. CONFIRMED.
(d) Round H, G148 (d) (1), 4.3 lines 1077-1078: "each of the four complete linearizations before the last reduced it by
    more than the 1.12e-8 that remains (the last, of 1500 iterations, by 5.9e-9)". True: 3.79e-8, 3.07e-8, 2.75e-8,
    2.34e-8 and 5.86e-9. CONFIRMED.
(e) Round H, timeline 626-633: "the condition (Hmin) of R9" in the 11:06 entry (my recommendation); the 11:21 entry
    (G148 at 11:21:52Z: four corrections required, 1.112e-6 and 1.324e-7 confirmed for both evaluators) agrees with
    G148. CONFIRMED.
(f) Round G, timeline 634-637 (the 11:31 entry) and section 5, 1738-1742 (the memory sentence): the values are those of
    G149 (13.8 GiB at 16875 x 768, 12.3 GiB at 22500 x 512, 4.7 GiB at 11250 x 384, at most 7.5 GiB for each command
    of steps 2 and 3, limit 15.3 GiB = ulimit -v 16000000 KiB, wall times within the stated ones, outputs equal).
    "The configuration with the most evaluation points" is right (16875 x 768 has 12.96e6 points, the next 22500 x 512
    11.52e6). One gap, mine: G149 ran three of the six configurations of step 1, so "Peak resident memory of the
    commands of steps 1 to 3" and "reproduced the stored outputs exactly" are measured for those three only; for the
    other three (16875 x 384, 16875 x 512, 22500 x 384) G149 gave an extrapolation (about 7 to 9.5 GiB). I am running
    them now on the same copy under the same limit (scratch/rss_measure3.sh, started 11:33:41Z, about 15 minutes);
    G151 will confirm the sentence as written or give the correction. Note: my record has no stored candidate output
    at 16875 x 384 (step 1 lists that configuration; 4.4 reports the candidate at the other five), so for that one
    the comparison can only be against a second run.
Verdict: round H CONFIRMED (all four G148 corrections in, as required). Round G CONFIRMED for the values stated;
the scope of the sentence over the three unmeasured step-1 configurations is OPEN until G151.

## G151 (2026-10-19T11:49:26Z). The three remaining step-1 configurations (G150 (f)); the reference outputs; C8 DONE audit of FINAL_REPORT f6a93ab4 (lead NOTES 11:34:55Z, 11:36:45Z)
(a) Measurement (scratch/rss_measure3.sh, 11:33:41Z to 11:43:17Z, the same copy and limit as G149; scratch/rss/rss.log):
    step  command (on c6g)                            peak RSS (KiB)   (GiB)   wall
    1     gen_audit.sh 16875 384 479                      7331048       6.99   2:26
    1     gen_audit.sh 16875 512 639                      9659916       9.21   3:50
    1     gen_audit.sh 22500 384 479                      9657804       9.21   3:20
    All exited 0. With G149 every configuration of step 1 is now measured; 1.11 to 1.14 KiB per evaluation point on all
    six; the maximum of steps 1 to 3 is 13.77 GiB at 16875 x 768 as stated. The wall times are within "2 to 8 minutes
    each". Outputs (scratch/rss_cmp.py, out: scratch/rss/rss_cmp_out3.txt): 16875 x 512 and 22500 x 384 equal my
    runs/audit/c6g_N16875_q512 and c6g_N22500_q384 JSONs in all 1674 leaves; the eight G149 comparisons repeat
    unchanged. 16875 x 384 has no earlier output in my record (section 4 does not use its step-1 output; the J values
    at 16875 x 384 come from step 2, compared in G149), so for it there is nothing to compare.
(b) Finding (mine, in my G149 wording): the "stored outputs" of steps 1 and 2 are not among the artifacts. INDEX.txt (d)
    says "empty output directories (runs/)", and d_evaluator/runs/audit and runs/gen4 of the tree have no files; the
    outputs I compared with are in my working record. Section 5 ("reproduced the stored outputs exactly") and the 11:31
    appendix entry ("every output equal to the stored one") therefore name files a reader does not have, and for 16875
    x 384 there was none. The step-3 references are in the tree (c_diagnostics/c6g_scan.json, c6g_scan960.json).
    I have put the reference outputs in one directory of my lane: ref_outputs/c6g (18 files, README.txt, MD5SUMS; 816 KB;
    md5 of MD5SUMS 65e5c92e, of README.txt 552cb911): the five earlier step-1 outputs (.json and .log), the 16875 x 384
    output of (a) (tag rssd, said so in README.txt), and the step-2 outputs (c6g_extra.log, c6g_zeros.json, the printed
    output of vb3ibp.py, the _ax and _jd2 JSONs). No local paths occur in these files.
Required (R1 to R4); the lead rebuilds, finalizes with a new T_end and posts the diff:
(R1) Copy ref_outputs/c6g of my lane to d_evaluator/runs/reference in the tree, unchanged (check against its MD5SUMS).
     INDEX.txt (d): "empty output directories (runs/)" -> "empty output directories (runs/audit, runs/gen4) and the
     reference outputs of section 5 steps 1 and 2 on the candidate (runs/reference, with README.txt and MD5SUMS)".
     5 (d): after "the far-field checks of 4.5 (far1_ver.py, far2_ver.py, farP.py)," insert "the reference outputs of
     steps 1 and 2 below on the candidate (runs/reference),".
(R2) Section 5, from "Peak resident memory" to "reproduced the stored outputs exactly." (1169-1172 of f6a93ab4), replace
     by: "Peak resident memory of the commands of steps 1 to 3 on the candidate: 13.8 GiB for gen_audit.sh at 16875 x
     768, the configuration with the most evaluation points (12.3 GiB at 22500 x 512, 9.2 GiB at 16875 x 512 and at
     22500 x 384, 7.0 GiB at 16875 x 384, 4.7 GiB at 11250 x 384), and at most 7.5 GiB for each command of steps 2 and
     3. They ran under an address-space limit of 15.3 GiB (ulimit -v 16000000), and every output for which an earlier
     one exists equals it in every number (file names and timings aside): for steps 1 and 2 the earlier outputs are in
     runs/reference of (d), for step 3 they are the candidate's scan files in (c). Step 1 at 16875 x 384, which section
     4 does not use, had no earlier output; runs/reference holds the one from this measurement."
(R3) Appendix, a new entry after the 11:31 entry: "- 11:5x verifier measurement of the three remaining configurations
     of step 1 (16875 x 384, 16875 x 512, 22500 x 384): 7.0, 9.2 and 9.2 GiB, the stated wall times met; the outputs at
     16875 x 512 and 22500 x 384 equal the earlier ones, 16875 x 384 had none. The reference outputs of steps 1 and 2
     added to (d)." (11:5x: the time of this entry, to the minute.) In the 11:31 entry "the stored one" may stay (it
     now has a referent) or read "the earlier one".
(R4) SPEC.md status line 6: "D9 checked on the trials (G4)" says more than my record: G10 checked the D9 identities
     (with defect) as identities, and G4 evaluated D9 on one early trial (8.64e-4, a measure of the centre layer). Write
     "D9 checked as identities (G10) and evaluated on one early trial (G4)"; D9 is not used in FINAL_REPORT. The rest of
     v4.19 is right: E6 (positivity repair), G107 item 5 (R11 with a finite zero set assumed), and the section 8 item
     (line 408) agree with G114 (row 39 "excluded at this level"), G126 (row 55 "undecided" by the letter, "not
     determined" on resolved h(P); span [5.5524653, 5.5793640]; lower end bracketed at this budget by v4.15), G135 (56
     flattened, Q_200 = 1.680, "undecided"; 56 "excluded at this level" by the interval rule; 57 ratios only) and G147
     ("kept at twice the budget"). Its endpoint state ("C6 ... final check pending", "C8 ... open") is dated 11:36:03Z
     and may stay as a dated record.
(c) C8 audit of f6a93ab4 apart from (b):
    - Finalize step e240e4b6 -> f6a93ab4 (lead (a) to (e)): the appendix is the section 0 timeline of e240e4b6,
      de-indented by two spaces, text unchanged (616 lines), "[OPEN] later entries." removed; its preamble is right ("the
      candidate" is X1 in the entries 10:51 to 12:26 of 2026-10-18 and X3 from the 16:44 entry on). Summary items (i) to
      (iv) equal those of section 4 word for word; every symbol of the notation sentence is defined where it says (P_2
      in section 1; P in R5, p_3 in R7, B_3 and R10 in section 3; X3, F3, F2, the rule of 4.3 and L in section 4, L in
      the conventions at line 213). T_end 2026-10-19T11:34:31Z, elapsed 41h57m19s = 41.96 h; "8 consecutive sessions of
      at most six hours" agrees with the lead's shift log (8 starts, gaps of 30 s, the 8th at 10:57:59Z). The waiver
      sentence is true and claims no 24 h by itself; the elapsed time exceeds 24 h. 5 (d) cross-reference right. Checks
      on f6a93ab4: [OPEN] 0, forbidden strings 0, trailing spaces 0; no proof language for numerics (every "establish",
      "proved", "certified" in the body is negated or refers to section 3).
    - STATUS banner: "recomputed or checked every number of section 4 as written" holds by the diff audits of every
      round that wrote section 4 (each new or changed number checked against my G-entries or recomputed; through G150
      and this entry); "confirmed the endpoint against the standard
      defined before 4.1" becomes true with my DONE entry; section 3 is checked by me and by the referee (G107; the
      section 3 heading carries the same statement since the rounds audited before).
    - C6 on the final tree (11:36Z, 1430 files): every md5 of work/build/artifacts_manifest_1136.txt matches the tree
      (md5sum -c, 0 failures; 1430 files); c6g 15f8095f, c6gF 0398af3f, gpu_long_solve.py f26dde2d; all shape md5s in
      the GPU chain log (scratch/chain_md5.py: 31 ok, 0 differ, 0 missing); d_evaluator/code equals my code/ file by
      file except the cd line of gen_audit.sh and extra_checks.sh (relative to the script); e_independent/NUM_REPORT.md
      423e5957 equals the numerics lane's current file; g_logs/RUN_STATUS.md equals the lead's current file and
      g_logs/WORKLOG.md is the 11:36Z copy (records). Smoke tests on a fresh copy (scratch/c6_rerun.sh, 11:43Z to
      11:45Z): md5 15f8095f; quick_scan 32768 x 640 equal to c_diagnostics/c6g_scan.json in all 13939 keys;
      gen_audit 11250 x 384 equal to my c6g_N11250_q384 JSON except labels, paths and t_total. MET, with (R1).
    - PROMPT mapping on f6a93ab4 (scratch/anchor_lines.py, out scratch/anchors_f6a9.txt; line numbers of f6a93ab4):
      6 explicit candidate, reproducible, not a proof: 4.2 348 "explicit formula with stored coefficients"; 5 1113
        (INDEX.txt); 4.1 261 "It is not a proof."; STATUS 3-7. MET.
      14 T0, T_end, elapsed: Summary 10; section 0 58-59. MET.
      25 gate: STATUS FINAL; section 0 60 (waiver; elapsed 41.96 h > 24 h). MET.
      62 strong vs weak setting: Summary 14 and 4 161, item (i). MET.
      104 parity, x^2 y jet, zero state, polynomial states, gauge, U(0): 4.7 1043-1047; 4.2 357 "U(0) = 0 by these
        parities"; 2 102 "Gauge.". MET.
      105 c_l identity by an independent method: Summary (iv) and 4.1 (3.2e-9, the h(P) root); 4.3; 4.7 1052. MET.
      106 R and E, absolute and normalized, near and away from the axes: 4.4 568 "Normalizations.", 601 "Absolute
        values.", 619-622 "Elliptic equation."; 4.4b 880 "Axis.". MET.
      107 three resolutions, three domains, fixed interior regions, far field and inverse separately: 4.4 resolution
        rows and 660 domain columns; 4.5 899-. MET.
      108 independent evaluator, manufactured tests, parity, conditioning, cancellation, aliasing: 4.5 997; 4.6 1003-;
        4.7 1043; 4.4 640 "is the aliasing check"; 4.3 557; 5 1131 (column scaling). MET.
      109 candidate, scripts, parameters, tables, far-field model, global vs finite domain: 4.2 368 "This is the
        far-field model."; 4.7 1050 "Finite-box artifacts:"; 4.4, 4.5; 5 and the artifacts, with (R1). MET with (R1).
      111 normalized residual about 1e-6, improvement under refinement, stable c_l, not a proof: 4.1 261; 4.4 resolution
        rows; 4.8 1090. MET.
      115 verifier checklist (walls, gauge, far-field terms, parity, jet, independent c_l, zero state, finite box): 4.7
        1042-1052, each named. MET.
      121 YES deliverable: 4.1 to 4.8 and 5. MET.
    - G120 conditions on f6a93ab4: C1, C2, C3, C4, C7 MET (G128, G131, G137, G138, G143, G150); C5 MET (banner, T_end,
      elapsed, [OPEN] 0); C6 MET with (R1); C8: f6a93ab4 audited in full by the chain of diff audits and this entry,
      except (b).
Verdict: f6a93ab4 CONFIRMED except (R1) to (R4). DONE is OPEN on this entry: I give DONE on the next build if its diff
from f6a93ab4 is (R1) to (R4), T_end, the elapsed time and the session count only, and the tree has runs/reference with
the MD5SUMS of (b).

## G152 (2026-10-19T11:59:41Z). DONE audit: FINAL_REPORT f6a93ab4 -> 1daeb3b3 (lead NOTES 11:51:59Z, G151 (R1) to (R4)) and the final artifacts tree
Method: line diff of my copies scratch/FR_f6a9.md and scratch/FR_1dae.md (md5 1daeb3b35ebd6a082842109f85b5a80f, 1878
lines; diff scratch/fr_d_f6a9_1dae.txt, 5 hunks); line numbers of 1daeb3b3.
(1) Lines 10 and 59: T_end = 2026-10-19T11:50:47Z, elapsed 42.23 hours (11:50:47Z - T0 2026-10-17T17:37:12Z = 42 h 13 min
    35 s = 42.226 h). Session count 8 unchanged: the lead's shift log has 8 starts, the 8th at 10:57:59Z with no end
    before T_end. CONFIRMED.
(2) 5 (d), 1157-1159: the (R1) insertion word for word. CONFIRMED.
(3) Section 5, 1172-1178: the (R2) sentence word for word; the start of the sentence (1170-1171) unchanged. CONFIRMED.
(4) Appendix, 1876-1878: the (R3) entry, timed 11:49 (G151 11:49:26Z). CONFIRMED.
No other change in the text. Checks on 1daeb3b3 (scratch/final_check.sh): [OPEN] 0, forbidden strings 0, trailing
spaces 0, banner unchanged, every shape file named in the report present in a_coefficients. The PROMPT mapping of G151
holds with the same line numbers (every anchor lies before line 1157).
Tree (reassembled 11:50:58Z; 1449 files, 137 MB; manifest work/build/artifacts_manifest_final.txt): md5sum -c against
the manifest 0 failures over 1449 files. Against the 11:36Z manifest the changes are exactly: INDEX.txt ((d) now names
runs/audit, runs/gen4 and runs/reference with README.txt and MD5SUMS); d_evaluator/VERIFY_REPORT.md (f530a46f, my
file as of G151); d_evaluator/runs/reference (19 files, equal to my ref_outputs/c6g by diff -r; md5sum -c MD5SUMS 0
failures; MD5SUMS 65e5c92e, README.txt 552cb911); d_evaluator/scratch/rss_cmp.py (equal to mine);
e_independent/NUM_REPORT.md (6da841d6, equal to the numerics lane's current file; its changes since 11:16Z are in
that lane's own items 26, 30, 32 and (p), its status line and the closing paragraph (p) (6); none touches what 4.6 of
FINAL_REPORT quotes); f_spec/SPEC.md (67922f84: only line 6, the (R4) wording; the version stamp stays v4.19, whose
change-log line already names the D9 status line); g_logs/WORKLOG.md. No code changed, so the 11:43Z smoke tests of
G151 stand. c6g 15f8095f, c6gF 0398af3f, gpu_long_solve.py f26dde2d; chain md5 31 ok, 0 differ, 0 missing.
G120 conditions on 1daeb3b3 with this tree: C1, C2, C3, C4, C5, C6, C7 and C8 MET.
Verdict: DONE. FINAL_REPORT 1daeb3b3 with the artifacts tree of 11:50:58Z carries the endpoint as verified: YES, strong
numerical evidence for the explicitly distinguished problem P_2, not a proof; the strong setting P_inf is not answered;
c_l is not determined beyond the observed span [5.5524653, 5.5793640] at the stated budget. It meets the standard of
G120 as written. The team may finish. This verdict covers 1daeb3b3 and this tree, with only the record copy of this
file changed in the tree; any other change to either needs a new diff audit.
