# S1 / IPM combined campaign 1: joint closure report

Status: FINAL, not closed. No unconditional existence theorem was reached and no theory-numerics pair closes. Proved
and independently audited: conditional a posteriori existence theorems with explicit residual thresholds. Certified:
the residual norms of one far-field-exact reference profile, which exceed the thresholds of the two main proved
theorems by factors above 3.5 million (weighted sharp) and 5.7 million (Analysis II family). The full-success criterion of the prompt (one profile satisfying every hypothesis of a complete existence
theorem) is not met.

## Summary

For certified norm values, unadorned decimals summarize the enclosures after rounding; directed bounds are marked explicitly.

Verdict. No reference profile was shown to satisfy all hypotheses of an existence theorem. The first inequality that
fails is residual smallness, by more than six orders of magnitude. Separately, certified point gaps and distance
bounds show that no registered scalar correction ball or original graded box around the reference, or around any other snapshot from
002 to 026 except one float-only comparison, contains an exact solution; the last two design controls (027, 028) have
float values only.

Proved (conditional theorems; each proof checked by an independent theory auditor; constants exact):

- Weighted sharp L^2 theorem. At s = 1/5184 and weights w = (2^15, 2^20), with the forcing norm X_(s,w) (no Hdot^-1
  component): if X_(s,w)(F) <= 2.1035e-4 and the background satisfies hypotheses (A) to (D), including the signed L^2
  margin c_l + 1 - theta - kappa >= 2 (B-L2), then rho_bar + h is an exact normalized solution with X_(s,w)(h) <=
  1351/1000000. The exact optimum of this estimate is X_(s,w)(F) <= 40722836401/193491763200000 (about 2.1046e-4),
  with X_(s,w)(h) <= 201799/149299200.
- Sharp theorem in the Analysis II norm family: N_s(F) <= 1.0578e-4 at s = 2^-13, under the background hypotheses of
  Analysis II Theorem D(b). This tolerance is 166 times the Analysis II threshold 6.3578e-7 (which is at s = 2^-18, so the
  factor compares two norms of one family). In the binding component G0 = ||F||_2 both theorems allow about 2.05e-7.
- Neither forcing space contains the other. Better matrix floors with all other constants fixed gain at most a further
  factor 2.2 (sharp) or 1.81 (weighted sharp). The endpoint-obstruction route is blocked with the present inputs: every
  valid universal velocity constant for the centrally odd weighted C^1 estimate is at least 0.7930365, while the
  weighted sharp ball needs E < 0.785064. This does not bound a PDE-specific estimate on stationary solutions.

Certified (two-sided enclosures reproduced by an independent numerical auditor) for the reference
candidate 007 (Analysis II's d2 profile plus two exact stationary far-field branches; 2982 generators; exact
rational coefficients; the rational profile, not its binary64 rounding, is the reference):

- all eleven forbidden far-field sectors vanish exactly, so the residual lies in the N_s and X_(s,w) forcing spaces;
  the margin (B-L2) holds on the whole plane; the other background hypotheses are not all certified;
- X_(s,w)(F) lies in [756.531, 757.852]; the four Analysis II-family norms N_s(F) lie in [604.29, 609.70]; G0 = 0.37669;
- the fixed-c L^2 distance from every exact solution exceeds 0.004769, while the registered scalar balls admit
  corrections of at most 3.8e-6 and the graded boxes at most 4.572e-4.

Later designs lower single norms (candidate 016 has the certified G0 = 0.30889), without a certified improvement in the
complete norm; the audited designs through 026 are ruled out in the same way.

Remaining gap. The first failing inequality is X_(s,w)(F) <= 2.1035e-4 against the certified X_(s,w)(F) >= 756.531,
a factor above 3596535.57. Closing it needs a reference closer to a solution by a factor above 1257 (scalar balls) or
10.43 (graded boxes), or a new ball geometry that certifies an admissible radius above the reference's distance, and
then certification of the remaining background hypotheses for that reference. Next campaign: numerical refinement of
the reference first (in float evaluation 43 percent of its ||F||_2^2 lies in 4 <= r < 8), keeping exact far-field cancellation and putting
the distance, point and (B-L2) filters inside the design loop; a new norm or ball geometry second; sharper inverse
constants last. The eight questions of the prompt are answered in order in the next sections.

## Run record

- Start T0 = 2026-10-28T20:30:31Z (logged). The team was stopped at 2026-10-29T19:30:31Z, 23 hours into the 24-hour
  window, so that this write-up finishes inside it. The write-up started at 2026-10-29T19:32:33Z and ended at
  T_end = 2026-10-29T19:51:41Z, so the elapsed time from T0 to T_end is 23 h 21 min 10 s, of which 23 h 00 min was team
  research time and the rest was write-up by the coordinator alone.
- Agent arrangement actually used: seven agents working concurrently for the whole 23 hours, each in its own working
  area, communicating through versioned theory and numerics publications, immutable candidate snapshots with hashes,
  and a shared closure matrix. The coordinator maintained the contracts, source hashes, closure matrix, checkpoints
  and report. Three theory workers covered the literature and nonlinear closure, weak spaces and sharp linear
  estimates, and independent theoretical audit. Three numerics workers covered far-field asymptotics and candidate
  construction, whole-plane norm certification, and independent numerical reproduction. External model reviews were
  treated as claims requiring verification.
- Each agent ran in sessions of at most six hours restarted by a supervisor, on a few fixed CPU cores at low priority.
  The numerics team worker had one GPU, which was withdrawn from 2026-10-29T00:57:59Z to 02:51:04Z; all other workers were CPU only.
- Rule for this report: only results that an independent audit worker confirmed are stated as proved (labels A2-THEOREM
  and AUDITED) or certified (numbers labeled CONFIRMED). Every other statement is labeled CLAIMED, CONDITIONAL, OPEN,
  HEURISTIC or FLOAT where it appears. Both independent auditors reviewed the frozen copy of this report of
  2026-10-29T19:00Z (the theory auditor confirmed all 108 candidate and status rows in theory audit 512; both requested a few
  repairs, theory audit 512 and numerical audit 441 to numerical audit 443); the repairs were applied and accepted in the 19:14Z version (theory audit 513, numerical audit 446),
  and a later two-line repair was accepted in theory audit 514. After the team stop the coordinator added this summary and run record, removed internal references and
  working-file names, and replaced the run-record and checkpoint sections; no mathematical statement, label or number
  was changed.
- References. Candidate numbers identify immutable profile snapshots. Numbered theory audits, numerical audits and
  closure reviews identify the corresponding evidence in the accompanying artifacts. Frameworks and norms are named
  descriptively below; the accompanying artifacts provide a concordance with their recorded identifiers. The final
  theory and numerics reports, closure matrix and versioned exchanges are also in the accompanying artifacts.

## Answers to the eight questions (final status, closure matrix v185; each answer is expanded in the next two sections)

1. Strongest estimate proved: conditional a posteriori existence theorems only, all AUDITED; no existence result is
   unconditional. The largest numerical residual threshold is that of the sharpw ball; thresholds in different norms
   bound different quantities and do not order residual balls. Weighted sharp L2 framework (the linear-estimates reviewer's linear-estimate result 3): if X_(s,w)(F) <=
   2.1035e-4 (s = 1/5184, w = (2^15, 2^20), forcing norm weighted X norm without an Hdot^-1 component) and the
   background satisfies (A) to (D) of theory audit 019, including the signed L^2 margin (B-L2), then an exact normalized
   solution exists within X_(s,w)(h) <= 1351/1000000. The exact optimum of the same estimate (the g = 0 case of
   the linear-estimates reviewer's L2 defect framework, AUDITED, theory audit 065) is X_(s,w)(F) <= 40722836401/193491763200000, above 2.1046e-4, with
   X_(s,w)(h) <= 201799/149299200 (theory audit 479; CONFIRMED by the linear-estimates reviewer's check of theory audit 479 (sharpw max), accepted in theory audit 485, and by
   the numerical auditor's numerical audit 415). This is the maximum of this one audited sufficient estimate at s = 1/5184 and w = (2^15, 2^20),
   with all background hypotheses retained (theory audit 508). In the Analysis II norm family the best is sharp Sobolev framework, with
   N_s(F) <= 1.0578e-4 at s = 2^-13.
2. Comparison with Analysis II: sharp Sobolev framework tolerates a residual 166 times larger than Theorem D(b) (1.0578e-4
   against 6.3578e-7). The two norms are of the same family but at different s (2^-13 and 2^-18). Weighted sharp L2 framework
   uses a different forcing space, with no Hdot^-1 component, so three far-field sectors must vanish instead of seven;
   neither forcing space contains the other (theory audit 259). In the binding component G0 = ||F||_2 both theorems allow about
   2.05e-7. Better state 131 matrix floors with all other constants fixed raise the sharp and sharpw thresholds by
   less than factors 2.2 and 1.81 (theory audit 119).
3. Best numerical reference: candidate 007 (Analysis II's d2 plus two exact stationary far-field branches,
   balanced objective; 2982 generators, exact rational coefficients). It is the fully certified baseline: its sharpw
   forcing norm, its ||F||_H and its four N_s norms have CONFIRMED two-sided enclosures (numerical audit 180, numerical audit 249, numerical audit 252), and
   it has a CONFIRMED whole-plane theta cover. Later designs lowered single norms. 016 has the smaller CONFIRMED G0
   = ||F||_2 = 0.30889 (numerical audit 341) and 0.6167335007 < H(016) < 0.617897369 < H(007) (numerical audit 430 and numerical audit 431 with theory audit 502,
   accepted both ways; H(007) - H(016) > 0.017627007636152781). But at identical s and weights its sharp, sharpw,
   bL[7/5], bL[1] and trans forcing norms exceed 007's (numerical audit 393 with theory audit 467), its complete E_2 exceeds 007's by more
   than 21.759869526341 (numerical audit 416, accepted in theory audit 486 and at this precision in theory audit 488), all ten registered sufficient
   forcing tests fail for it, and it
   is RULED OUT by distance. The norm-certification team CLAIMS E_2(017) < E_2(007) (only the conditional arithmetic is CONFIRMED, numerical audit 413
   and theory audit 484; the lower bound H(017) > 0.6144195987 is CONFIRMED and accepted both ways, numerical audit 425, theory audit 495, numerical audit 426, and
   does not order 017 against 007), and 017 is RULED OUT by distance as well. No design 013 to 028 has a certified
   value that places it closer to a solution, and certified lower distance bounds do not rank actual distances
   (theory audit 219), so 007 is not claimed to be the closest candidate. The latest accepted case 4 state is still state 131,
   whose residual grows like r^0.1048 and lies in no unweighted forcing space.
4. Regularity and far field: yes, for the rational profile of 007. All eleven forbidden far-field sectors vanish
   exactly (numerical audit 090, CONFIRMED), so its residual lies in the N_s and X_(s,w) forcing spaces; the binary64 rounding of
   its coefficients reintroduces the sector (1,0) (numerical audit 096), so the reference is the rational profile. (B-L2) holds on
   the whole plane (CONFIRMED). The other background hypotheses of theory audit 019 are not all certified.
5. Residual in the theory space: for 007, X_(s,w)(F) lies in [756.531, 757.852] (CONFIRMED, numerical audit 180 with theory audit 238),
   against the allowed 2.1035e-4. Its four Analysis II-family norms N_s(F) lie between 604.29 and 609.70 (CONFIRMED
   two-sided enclosures, numerical audit 252), each above its registered threshold by a factor above 5.7e6.
6. Closure: no pair closes. The first failing inequality is the residual smallness X_(s,w)(F) <= 2.1035e-4, which
   fails for 007 by a certified factor above 3596535.57. Independently of any forcing bound, no registered ball or box
   around 007 contains an exact solution (in 007's affine chart at every c; theory audit 189, theory audit 203): the fixed-c L^2 distance
   of 007 from every exact solution exceeds 0.004769 (CONFIRMED), while the scalar balls admit corrections of at most
   3.8e-6 and the graded boxes at most 4.572e-4. Every snapshot candidate 002 to 026 except the FLOAT comparison 011 is
   RULED OUT in every registered scalar ball and original graded box by CONFIRMED point gaps or fixed-c L^2 distances
   above 1/1000 (theory audit 459; theory audit 462 extends this to every variable-margin L2 framework ball at every allowed weight pair, at the
   registered state 131 floors and under the unweighted margin (B-L2), not under the weighted margin (B-L2-w)).
   candidate 001's residual is not in the forcing space, and no real L^2 correction of it is a stationary solution at any
   real c (theory audit 458, theory audit 465; a statement about rho_001 + L^2 only). The design controls 027 and 028 are OPEN with FLOAT
   values only. The endpoint-obstruction route is blocked with the present inputs: every valid universal velocity
   constant is at least 0.7930365, while the fixed sharpw ball needs E < 0.785064 and the sharpw, sharp Sobolev and graded
   family ceilings need E < 0.682, 0.648 and 0.27 (theory audit 380, theory audit 381; whether an improved constant reaches the radii
   2^-25 or 6.8626e-8 is OPEN); the profile-specific coefficient 583/1000 misses every target even with zero remainder
   (theory audit 414), 93/250 (theory audit 415) would pass only the scalar-ball necessary thresholds with zero remainder, and the only
   proved tail remainder (theory audit 410) is too large for any coefficient (theory audit 421, theory audit 425).
7. Smallest remaining obstacle: the size of the reference residual over the whole inner and mid field (43 percent of
   007's FLOAT ||F||_2^2 lies in 4 <= r < 8). Either the reference must move to within a registered ball budget, which
   for 007 needs a distance reduction above 1257 (scalar balls) or 10.43 (graded boxes), or a new geometry must
   certify an admissible radius above the reference distance. Sharper constants are not shown to close the gap: theory audit 119
   bounds only the gain from better state 131 matrix floors with all other constants fixed (below 2.2 and 1.81), and
   no result bounds the gain from changing the other constants.
8. Priority for the next campaign: numerical refinement of the reference first, with the exact far-field cancellation
   kept and the distance, point and (B-L2) filters inside the design loop. A new ball geometry or norm comes second,
   tested on the actual Newton correction of the refined reference. Sharper inverse constants come last. The
   quantitative evidence is in answer 8 below and in the proposed continuation in the accompanying artifacts.

## The eight answers with their audit references (final status, closure matrix v185)

1. Strongest estimate proved. Conditional existence theorems only, all AUDITED (proof by one theory worker, review by
   another). Among the scalar norms the largest numerical residual threshold is that of the sharpw ball; thresholds in
   different norms are not ordered residual balls. As registered, weighted sharp L2 framework (the linear-estimates reviewer linear-estimate result 3, AUDITED theory audit 042
   with the theory team closure review 006) states: if X_(s,w)(F) <= 2.1035e-4 at s = 1/5184, w = (2^15, 2^20) (weighted X norm, no Hdot^-1
   term) and the background satisfies (A) to (D) of theory audit 019, including the signed L^2 margin c_l + 1 - theta - kappa >=
   2 (B-L2), then rho_bar + h is an exact normalized solution with X_(s,w)(h) <= 1351/1000000. The g = 0 case of
   the linear-estimates reviewer's H-free defect extension L2 defect framework (AUDITED, theory audit 065) has the same hypotheses, s and weights and
   gives the exact optimum X_(s,w)(F) <= 40722836401/193491763200000 (above 2.1046e-4) with X_(s,w)(h) <=
   201799/149299200; at r = 1351/1000000 the estimate already admits 2.1046e-4 (corrected 16:33Z after the theory auditor's theory audit 479;
   CONFIRMED by the linear-estimates reviewer's check of theory audit 479 (sharpw max), 17 exact checks, accepted by the theory auditor in theory audit 485, and by the numerical auditor in
   numerical audit 415). This is the maximum of this one audited sufficient estimate at s = 1/5184 and w = (2^15, 2^20), with all
   background hypotheses retained (theory audit 508). In the Analysis II norm family the best is sharp Sobolev framework (the linear-estimates reviewer linear-estimate result 2,
   AUDITED theory audit 028): N_s(F) <= 1.0578e-4 at s = 2^-13 under the Analysis II background hypotheses of Theorem D(b).
2. Improvement over Analysis II. sharp Sobolev framework allows a residual tolerance 166 times larger than Theorem D(b)
   (1.0578e-4 against 6.3578e-7), in the same norm family but at s = 2^-13 instead of 2^-18, so the factor compares
   tolerances in two different norms. Weighted sharp L2 framework uses a different forcing space: it has no Hdot^-1 component,
   so a residual sector r^e is admissible for e < -1 instead of e < -2 and only three far-field sectors must vanish
   instead of seven (theory audit 033), but it asks for slightly more fractional regularity; at the selected exponents neither
   forcing space contains the other (theory audit 259, AUDITED through the linear-estimates reviewer's review of theory audit 259 and theory audit 283; with the extra
   hypothesis Q3 <= 10^6 E_2 on residuals in E_3, the A2 condition at 163.88 times its tolerance implies the sharpw
   smallness and the converse fails, theory audit 284, CONFIRMED), so its threshold ratio to D(b) is not an enlargement of one
   residual ball. In the common binding component G0 = ||F||_2 both allow about 2.05e-7, about 166 times the Analysis II
   requirement. In the registered Gram schemes, better state 131 matrix floors with all other constants fixed gain
   less than a further factor 2.2 (sharp) or 1.81 (sharpw) (theory audit 119); no result bounds the gain from changing the other
   constants.
3. Best numerical reference. candidate 007 is the chosen reference (Analysis II's d2 plus two exact
   stationary branches, balanced objective; 2982 generators, rational coefficients): the fully certified baseline
   (two-sided CONFIRMED enclosures of its sharpw forcing norm, ratio above 3596535.57, of ||F||_H and of the four N_s
   norms; numerical audit 180, numerical audit 249, numerical audit 252) and the first complete theta cover (017 has a CONFIRMED cover too, numerical audit 309 with
   theory audit 400, but is RULED OUT by distance). 016 has a smaller CONFIRMED whole-plane G0 (0.30889, the norm-certification team with numerical audit 341), a
   CONFIRMED G1 (numerical audit 373) and a CONFIRMED P2 (numerical audit 392); all ten registered sufficient forcing tests fail for it, its
   actual sharp, sharpw, bL[7/5], bL[1] and trans forcing norms exceed 007's at identical s and weights (numerical audit 393 with
   theory audit 467), its complete actual E_2 exceeds 007's (E_2(016) > 608.392385921614 against 007's upper bound 606.820219;
   numerical audit 396, CONFIRMED by theory audit 470 and closure review 048; the upper bounds H(016) < 0.944107 and E_2(016) < 722.969 are CONFIRMED by
   the theory auditor in theory audit 476 and by the numerical auditor in numerical audit 407, and the numerical auditor CONFIRMS the sharper H(016) < 0.619652 and E_2(016) < 629.296113
   from its own integration of modes 1 to 31, numerical audit 410, reproduced by the theory auditor in theory audit 480; so H(016) < H(007), by more than
   0.015873038675998 (numerical audit 412 with theory audit 483), although E_2(016) > E_2(007), by more than 21.759869526341 with the numerical auditor's
   lower bound E_2(016) > 628.580088526341, numerical audit 416, accepted by the theory auditor in theory audit 486 and at this precision in theory audit 488; with
   all 16 corrected modes,
   0.6167335007 < H(016) < 0.6179529539 and E_2(016) < 628.8790248, CONFIRMED independently by the numerical auditor in numerical audit 418 and by
   the theory auditor in theory audit 486 and accepted both ways through theory audit 488; with all 32 complete Hardy modes through frequency 63,
   H(016) < 0.617897369 and E_2(016) < 628.865389, so H(007) - H(016) > 0.017627007636152781, numerical audit 430 and numerical audit 431,
   accepted by the theory auditor in theory audit 502), and it is RULED OUT by distance. The norm-certification team CLAIMS E_2(017) < E_2(007) by at least 0.8591
   (two-sided enclosure; numerical audit 413 and theory audit 484 CONFIRM only its conditional arithmetic, and the source premises are OPEN;
   the numerical auditor's own replay numerical audit 425 CONFIRMS the 16 dual trials and H(017) > 0.6144195987, accepted both ways in theory audit 495 and
   numerical audit 426, but not the upper bound for H(017) or E_2(017)); 017 is RULED OUT by distance as well. Lower distance
   bounds for different candidates do not order their actual distances (theory audit 219), so this is not a claim that 007 is
   the closest to a solution. The latest accepted case 4 state is still state 131, whose residual grows like r^0.1048
   and lies in no unweighted forcing space.
4. Regularity and far field. Yes for candidate 007 with its rational coefficients: all eleven forbidden sectors vanish
   exactly (numerical audit 090, CONFIRMED), so its residual lies in the N_s and X_(s,w) forcing spaces; the binary64 rounding of
   its coefficients reintroduces sector (1,0) at full-circle norm 7.18e-13 (numerical audit 096, CONFIRMED), so the reference is
   the rational profile. (B-L2) holds for it on the whole plane (kappa_HS 0.72816, theta <= 2/25; numerical audit 092, numerical audit 111,
   CONFIRMED by theory audit 111, theory audit 162). The other background hypotheses of theory audit 019 are not all certified for it.
5. Residual in the theory space. For candidate 007 with the sharpw weights, the norm-certification team encloses the whole forcing norm
   X_(s,w)(F) in [756.5312630768, 757.8514372426] from its complete exact components (G0, G1, P2, Q3) and the AUDITED
   two-sided conversion of linear-estimate result 3. The numerical auditor's independent assembly CONFIRMS this (numerical audit 180, accepted in theory audit 238). G0 =
   ||F||_2 = 0.3766893247 and G1 = 3.4391037868 alone (CONFIRMED by numerical audit 139 and numerical audit 153) give the elementary bound (w1
   G1^2 + w2 G0^2)^(1/2) > 732.35, and 1024 G0 alone gives 385.72. The Analysis II norms N_s also need ||F||_H: The norm-certification team
   encloses it in (0.6355243760000922, 0.6355322685705510) (CONFIRMED by numerical audit 249), and the numerical auditor CONFIRMS the norm-certification team's two-sided
   N_s enclosures (numerical audit 252): (606.739447, 606.910169) for Analysis II D(b) framework, (606.818074, 606.820306) for Analysis II D(a) framework, (606.503334,
   607.180020) for rebalanced Sobolev framework and (604.299619, 609.698720) for sharp Sobolev framework, so all four registered N_s
   sufficient tests fail, each by a factor above 5.7e6. (Until 14:11Z this item said that the H enclosure was running;
   numerical audit 381 REFUTES that.)
6. Closure. No pair closes. The first failing inequality is residual smallness: X_(s,w)(F) <= 2.1035e-4 fails for
   candidate 007 by a certified factor above 3596535.57 (numerical audit 180 with theory audit 238). Independently, the fixed-c L^2 distance of
   candidate 007 from every exact solution exceeds 0.004769166867 (n = 7 angular probe theory audit 185, AUDITED through the theory team
   closure review 022 and theory audit 190, CONFIRMED by numerical audit 157), while every ball of the registered scalar families contains only
   corrections with ||h||_2 <= 3.8e-6 and every graded box only corrections with ||h||_2 < 4.57e-4 (budget formula,
   AUDITED theory audit 065; Proposition G, CONFIRMED by theory audit 070): no ball or box of the matrix around candidate 007 contains a
   solution at its c, for any forcing bound (the graded boxes are also excluded by a point value, numerical audit 102). Theory audit 189
   (AUDITED) pins c for every L^2 correction of a reference with a nonzero leading r^gamma profile, and 007 has one
   (theory audit 203, CONFIRMED by numerical audit 165), so in 007's affine chart the exclusion holds at every c. The same holds for every
   exclusion of d2 and candidate 005 to 012, which share 007's leading profile (theory audit 210, CONFIRMED by numerical audit 172), and of 013
   (same leading density, numerical audit 197). A solution with another exponent would need a new reference chart with nonlinear
   tail coordinates (theory audit 205, AUDITED through the theory team closure review 025 and theory audit 220); the fixed-c dilation orbit, by contrast, fits
   in a 4-dimensional finite tail augmentation (theory audit 222, AUDITED through the theory team closure review 027 and theory audit 232; numbers CONFIRMED by
   numerical audit 177). In it the PDE forces every lower nonintegrable tail profile from the leading one (theory audit 234, AUDITED through
   the theory team closure review 030 and theory audit 246) and exact 007 satisfies these relations (theory audit 235, CONFIRMED by numerical audit 189), so fixing the
   leading amplitude loses no solution with positive amplitude up to dilation. candidate 008, 009, 010, 012 and 013 are
   excluded from every scalar ball and graded box by their own CONFIRMED distances above 0.001938714194,
   0.016967603955, 0.022479506978, 0.018641021006 and 0.00199234339 (numerical audit 176 with theory audit 225, numerical audit 179 with theory audit 231, numerical audit 205
   with theory audit 270, numerical audit 182 with theory audit 236, theory audit 255 with numerical audit 204). candidate 014 is excluded from every scalar ball and graded box
   by its CONFIRMED point gaps (numerical audit 213 with theory audit 279) and its CONFIRMED distance above 0.00198301351067 (numerical audit 214 with
   theory audit 280), and candidate 015 by its CONFIRMED point gaps (numerical audit 234 with theory audit 299) and its CONFIRMED distances above
   0.000351804115950603 and 0.001232449584356253 from two held-out probes (theory audit 298 with numerical audit 235; numerical audit 237 with theory audit 304).
   The design test candidate 016 (snapshot 06:46:04Z) is excluded by its CONFIRMED point gaps (numerical audit 242 with theory audit 307 and
   numerical audit 251) and its CONFIRMED distances above 0.001092633159 and 0.001470360924 from the held-out probes (23, 2400) and
   (19, 1800) (numerical audit 246 with theory audit 310, theory audit 311). The scale comparison candidate 017 (07:11:15Z) is excluded in the same way, by
   its CONFIRMED point gaps (numerical audit 254 with theory audit 319) and its CONFIRMED distance above 0.001068502321 from the held-out
   probe (23, 2400) (numerical audit 256 with theory audit 320; the (19, 1800) value above 0.00167183069831928 is CONFIRMED as well, numerical audit 257
   with theory audit 331, accepted in numerical audit 267). candidate 018 (08:02:27Z), a continuation of 016 and not a certification target, is
   excluded by its CONFIRMED point gaps (numerical audit 270 with theory audit 342) and its CONFIRMED distance above 0.001655825792 from the
   held-out probe (19, 1800) (numerical audit 272 with theory audit 345). candidate 019 (08:28:42Z), a continuation of 017 and not a
   certification target, is excluded by its CONFIRMED point gaps (numerical audit 279 with theory audit 353 to theory audit 355) and its CONFIRMED
   distance above 0.001661806967 from the held-out probe (19, 1800) (numerical audit 282 with theory audit 357). candidate 020 (08:46:18Z), a
   two-scale trial comparison and not a certification target, is excluded by its CONFIRMED point gaps (numerical audit 291 with
   theory audit 360 to theory audit 362) and its CONFIRMED distance above 0.001855374677 from the held-out probe (19, 1800) (numerical audit 293 with
   theory audit 363). So every campaign snapshot through candidate 020 except the controlled comparison candidate 011 (OPEN, FLOAT
   values only) is RULED OUT in every registered scalar ball and original graded box. candidate 021 (10:05:34Z), a 40-step
   continuation of 020 and not a certification target, is RULED OUT in every registered scalar ball and original
   graded box as well: The numerical auditor's exact point tests fail for it (numerical audit 314, reproduced by the theory auditor in theory audit 387 to theory audit 389,
   accepted by the numerical auditor in numerical audit 319), and its registered distance above 0.001864696854 from (19, 1800) (numerical audit 316) is
   reproduced independently (theory audit 392, accepted in numerical audit 320). candidate 022 (10:28:22Z), not a certification target, is RULED
   OUT in every registered scalar ball and original graded box by the numerical auditor's exact point tests (numerical audit 326, reproduced by
   the theory auditor in theory audit 405 to theory audit 407) and in every other X_s and X_(s,w) ball of these frameworks by the numerical auditor's registered
   distance above 0.00135251075726327 from (19, 1800) (numerical audit 327, reproduced independently in theory audit 408). candidate 023
   (10:42:28Z) is RULED OUT in every ball of these frameworks by the numerical auditor's point gaps and distance above
   0.002634958245163687 from (19, 1800), reproduced independently by the theory auditor (theory audit 416 to theory audit 420) and accepted by the numerical auditor
   (numerical audit 348 to numerical audit 350). candidate 024 (11:31:32Z), not a certification target, is RULED OUT in the same way: The numerical auditor's point
   gaps and distance above 0.001556067368832641 from (19, 1800) (numerical audit 343, numerical audit 344) are reproduced independently by the theory auditor
   (theory audit 427 to theory audit 431) and accepted by the numerical auditor (numerical audit 357 to numerical audit 359). candidate 025 (12:50:59Z), not a certification target, is
   RULED OUT in the same way: The numerical auditor's point gaps and distance above 0.002065801265578052 from (19, 1800) (numerical audit 362,
   numerical audit 364) are reproduced independently by the theory auditor (theory audit 438 to theory audit 441) and accepted by the numerical auditor (numerical audit 370, numerical audit 371). candidate 026
   (13:12:37Z), not a certification target, is RULED OUT in the same way: The numerical auditor's point gaps and distance above
   0.001355907204057457 from (19, 1800) (numerical audit 367, numerical audit 369) are reproduced independently by the theory auditor (theory audit 446 to theory audit 450) and
   accepted by the numerical auditor (numerical audit 377 to numerical audit 379, 13:55Z). This does not extend to every framework: the dyadic scheme
   dyadic Y framework is tested only for state 131, d2, candidate 007 to 010, candidate 015, candidate 016 and candidate 017 (RULED OUT
   for each under the premises of its row; 015 since matrix v135, numerical audit 382 with theory audit 461; 017 since v138, numerical audit 389 with
   theory audit 463), and the localized route
   is incomplete (theory audit 330). candidate 027 (14:13:51Z) and candidate 028 (15:24:01Z), design controls and not certification
   targets, are OPEN with FLOAT values only (rows 103, 104, 107, 108).
7. Smallest remaining obstacle. The size of the reference residual over the whole inner and mid field. Against
   weighted sharp L2 framework the best candidate falls short by a certified factor above 3596535.57. In the unregularized
   comparison energy E_star^2=P2^2+2^14 G1^2+2^18 G0^2, the weighted G1 term contributes about 72 percent, and the G0
   and P2 terms about 14 percent each (numerical audit 180, corrected by numerical audit 438 and independently accepted in theory audit 509). Lowering
   G0 = ||F||_2 alone (0.377, against about 2e-7 required, a factor 1.83e6) is therefore not enough. This share does
   not identify a difficult operator direction (numerical audit 180). In FLOAT, the damped Galerkin L^2 Newton step from candidate 007
   inside its own span has ||h0||_2 about 1.8e-2 and lowers ||F||_2 only from 0.377 to 0.338, and residual pairings
   localized at r of about 20 to 32 do not move even when they are rows of the objective (numerics exchange 07, candidate 014).
   This suggests that the generator span, not the objective, limits the residual, but it is not a proved floor: damped
   trials bound neither the undamped optimum nor the span's residual from below (numerical audit 211), and the floor is OPEN.
   The numerics team's candidate 016 (snapshot 06:46:04Z, rows 80, 81; RULED OUT by CONFIRMED point gaps and distance) adds 252
   scale-25 functions in density modes 17 to 31 (numerical audit 248); its held-out probes at r about 19 to 40 drop by factors 3 to
   5 and G0 by 18 percent (FLOAT 0.3089 against 0.3767 on the MID 32 rule); the scale-50 comparison candidate 017 behaves
   alike in FLOAT. That is FLOAT design evidence, not a certified value, and it does not show that the earlier plateau
   was a span limit: an enlarged space can improve on a point that is not the minimum of the smaller space, and
   finitely many probe values bound neither the unmeasured residual nor the correction distance (numerical audit 250, theory audit 312,
   theory audit 330 and theory audit 340 REFUTE these inferences in numerics exchange 08, numerics exchange 09 and the 08:02Z the final numerics report in the accompanying artifacts version).
   Twelve further steps from 016 (candidate 018) lower the objective but raise every listed held-out probe again in FLOAT;
   twelve further steps from 017 (candidate 019) change the listed held-out values by less than 10 percent (FLOAT). Adding
   the second scale R0 = 50 to 016 (candidate 020) gives the lowest objective of the campaign, but each of the seven
   registered held-out probes with K >= 1200 listed in numerics exchange 10 is above both 016's and 017's (FLOAT). The
   CONFIRMED distances of 016 and 017 at (19, 1800), above 0.001470360924 and 0.00167183069831928 (theory audit 311, theory audit 331),
   are 3.21 and 3.65 times the graded ceiling and 515.9 and 586.6 times the sharpw family ceiling; a reference
   accepted by a graded box or a scalar ball needs an actual distance below that ceiling. Of the FLOAT ||F||_2^2 of
   candidate 007, 43 percent lies in 4 <= r < 8, so the deficit is in the inner and mid field, not the far field.
8. Priority for the next campaign. Numerical refinement of the reference profile first, keeping the exact far-field
   cancellation and putting the weak-distance and point filters and (B-L2) inside the design loop; ball geometry
   second (a new norm, componentwise boxes, or an inverse theorem with a different admissible radius), tested on the
   actual Newton correction of the refined profile; sharper constants within the present schemes last. Evidence: (a)
   better state 131 matrix floors within the registered Gram schemes, all other constants fixed, gain less than a
   factor 2.2 (theory audit 119), which leaves more than 1.6e6 for candidate 007 against weighted sharp L2 framework; (b) no inverse
   estimate inside the registered scalar ball families
   can accept candidate 007, since its fixed-c L^2 distance exceeds 0.004769166867 (CONFIRMED, theory audit 185 with numerical audit 157; 1257
   times the budget) while every such ball allows at most 3.8e-6 (L2 distance condition); this asks for a better center or another
   geometry, but it does not say how far the residual must fall, because the 3.6e6 smallness gap belongs to a
   sufficient condition; (c) numerical refinement is the only lever that has moved certified numbers (G0 from 4.99 for
   d2 to 0.377 for candidate 007, with eleven far-field sectors cancelled exactly), but that is progress, not a
   convergence forecast: the CPU-only continuations since 00:58Z are at a plateau (whether it is a stationary point or
   a conditioning stall is undecided: on the exact 1922-generator quotient basis 494 of the 1496 admissible directions
   are below binary64 resolution, numerics exchange 07, FLOAT), and removing all FLOAT residual in 4 <= r < 8 would lower G0
   only by a factor 1.33, so the whole inner and mid field must improve; (d) every weighted high-space route tried so
   far is ruled out for the d2 family (dyadic Y framework for state 131, d2, candidate 007, 008, 009 and 010 at every 0 < a
   < 2, the last three by numerical audit 186 with theory audit 248, numerical audit 187 with theory audit 250 and numerical audit 231 with theory audit 303, for 016 by the norm-certification team's
   seven-cell test reproduced by the numerical auditor in numerical audit 355 and for 015 by the numerical auditor's own integration, numerical audit 382 with theory audit 461, and for 017 by the numerical auditor's own integration, numerical audit 389; growing weights by theory audit 094; weighted energy rates capped by TP-3),
   and no quantitative evidence yet supports a norm that absorbs a factor of order 1e6. The distance test now excludes
   007 from every registered scalar ball and graded box (budget at most 4.572e-4 against a distance above 0.004769), so a
   geometry centered at 007 must admit and certify corrections with ||h||_2 above 0.004769; otherwise the center must move. A larger
   certified radius is not ruled out by any result here (theory audit 219). Both batches gave the same ranking in their H8
   lines: batch T's independent alternative is a new chart with nonlinear tail coordinates or the linear-estimates reviewer's localized
   orbit-weight route, batch N's is multi-scale inner functions that resolve the mid field to r of about 1000. The H12
   lines of all six workers (the theory team 08:03Z, the linear-estimates reviewer 07:56Z, the theory auditor handoffs 139 and 140, the numerics team 06:47Z and 08:02Z, the norm-certification team
   07:05Z, the numerical auditor 07:44Z) report no closure margin and keep this ranking. New since H8 on the theory side are
   reference-design operations, not inverses: far-out cutoffs remove the first two residual tails at arbitrarily small
   L^2 cost (theory audit 314, theory audit 324, AUDITED), while the weighted residual cost of this family diverges (theory audit 326) and its H_q
   cost stays bounded below (theory audit 334); finitely many cutoffs clear every sector above a fixed nonresonant exponent
   under stated hypotheses (theory audit 338); a moment-resolved endpoint theorem (theory audit 335, AUDITED through the linear-estimates reviewer's review and
   theory audit 350) would then exclude weighted C^1 corrections decaying faster than r^(gamma - 4) for the three-cutoff
   references (theory audit 339, AUDITED since theory audit 365 accepted the linear-estimates reviewer's review of the third-cutoff application); with the current
   constants its L^2 form cannot prove a distance above 9.28e-11 (theory audit 351; theory audit 375, AUDITED since the theory auditor accepted the linear-estimates reviewer's
   review in theory audit 385, lowers this reach to below 3.752e-16; theory audit 380 CONFIRMS the linear-estimates reviewer's sharper pointwise form, H_q >
   999745 for the three references, under which the inequality reaches the family ceilings only if E < 0.682 (sharpw),
   0.648 (sharp Sobolev) or 0.27 (graded) and the fixed sharpw radius 1351/1024000000 only if E < 0.785064; theory audit 381 Sections
   1 and 2, AUDITED since theory audit 386 accepted the linear-estimates reviewer's independent derivation, show that every universal constant is at
   least 0.7930365). So no universal velocity constant lets this test reach the fixed sharpw ball or these family
   ceilings for these three references: the universal-constant form of the test is RULED OUT as a route to those
   balls. The linear-estimates reviewer's falsification check the falsification review of the endpoint and the report summary (revision 1 13:19Z, sections 1 to 4 audited by
   the theory auditor in theory audit 443; revision 2, saved 13:42:25Z, makes the five wording repairs theory audit 443 asks for, CONFIRMED by theory audit 452)
   finds the same exclusion at every registered radius from the TB-rebal radius 3.51254748...e-7 up (2^-23 only with
   V >= |U_lead(0)|). At the Analysis II D(b) framework radii 2^-25 and 6.8626e-8 every constant from 0.7930365 up to 1.020385 and
   0.8711127 passes the theory audit 414 necessary condition. Theory audit 443 CONFIRMS these numbers and the review's new whole-integral
   bound (with the current coefficient list the reach is below 2.66323e-8 < 2^-25), but REFUTES the inference that
   passing a necessary condition removes the universal obstruction: 0.7930365 is a lower bound on valid constants, not
   a proved admissible one. Whether an improved valid universal constant reaches 2^-25 or 6.8626e-8 is therefore OPEN.
   The proved constant 1.747261 reaches no registered radius, and with the present inputs the route stays blocked at
   every registered radius. A correction-specific velocity expansion is a different test: theory audit 402 (CONFIRMED by the linear-estimates reviewer's
   the review of theory audit 402, ffb49200..., 11:30Z; AUDITED since theory audit 413, 11:38Z) bounds the limiting exterior velocity coefficient
   on the endpoint subspaces of 007, 013 and 014 by (583/1000) H_q, below 0.7930365, under an extra hypothesis on the
   angular tail and with no finite-radius remainder, so that route is OPEN. By the review, a proved remainder below
   about 0.099 H_q (0.064 H_q with the velocity offset) would pass the cutoff-radius test for the sharpw and sharp Sobolev
   family caps, and no remainder can pass it for the graded cap (0.269 < 0.583); theory audit 413 notes that this test is
   necessary, not sufficient, and the theory auditor's theory audit 414 (AUDITED since theory audit 423) finds that with E = 583/1000, zero remainder
   and no velocity offset the complete radial integral reaches at most 7.643e-7, below all four targets (the smallest
   is the fixed sharpw radius 1.319e-6); it would need E below 0.527596 (fixed sharpw ball), 0.458292 (sharpw family),
   0.434940 (TB) or 0.181070 (graded). The linear-estimates reviewer's review of theory audit 414 (12:08Z save 221b1135..., restored by the linear-estimates reviewer at 12:30:37Z)
   CONFIRMS theory audit 414 by an independent Arb recomputation (the theory auditor accepts the review in theory audit 423, so theory audit 414 is AUDITED), so
   the 583/1000 certificate cannot close the route at any remainder; the review withdraws the 'in principle yes' of
   the review of theory audit 402 section 4. The theory auditor's own finite certificate theory audit 415 (AUDITED: CONFIRMED by the linear-estimates reviewer's review of theory audit 415,
   12:37Z, accepted by the theory auditor in theory audit 434, 12:50Z) gives the pointwise coefficient 93/250 = 0.372 on the same endpoint
   spans, below the thresholds for the fixed sharpw ball, the sharpw family and TB, above the graded one; it supplies
   no remainder and no H_q bound. The theory auditor's own theory audit 422 (AUDITED via the same review and theory audit 434) finds that with E =
   93/250 and zero remainder the complete radial integral would reach 8.914e-6, 6.76 times the fixed sharpw radius,
   3.13 times the sharpw family ceiling and 2.35 times TB, but only 0.0195 times the graded ceiling. By the review of theory audit 415
   the constant is close to sharp: no certificate of this bound can use a constant below 0.3714757 (007), 0.3714938
   (013) or 0.3715026 (014); theory audit 434 adds that these lower coefficients concern the angular inequality on the whole
   two-dimensional span, so a stationary restriction or a larger independent lower bound on H could change the
   comparison (none is supplied). Theory audit 410 (AUDITED: CONFIRMED by the theory team's closure review 043, accepted by the theory auditor in theory audit 424) offers a
   finite-radius two-weight remainder; the linear-estimates reviewer's review of theory audit 410 (main obstruction AUDITED by the theory auditor's theory audit 421,
   which REFUTES one side assertion on the starting radius) finds that with the only proved tail input, theory audit 335 (7),
   that remainder is at least 3.97 H_q for 007, 013 and 014, more than 40 times the room 0.099 H_q, for any limiting
   coefficient; the review of theory audit 414 adds that it exceeds even the thresholds themselves, by factors 8.67 (sharpw), 9.63
   (TB), 55.6 (graded) and 6.54 (fixed sharpw radius), and the review of theory audit 415 finds it at least 46.06 times the room that
   93/250 leaves at the sharpw ceiling. The theory auditor's theory audit 425 (AUDITED: CONFIRMED by the theory team's closure review 045, accepted by the theory auditor in
   theory audit 432) extends the obstruction to radius-dependent coefficients, and the theory team's closure review 044 (AUDITED: CONFIRMED by the theory auditor's
   theory audit 426 with two literal repairs) shows that removing the inner part does not help with this tail input, since the
   averaged outer contribution alone is more than 4.34 times the required cutoff. Both bound the stated majorants
   only. The test also needs an a priori H_q budget for stationary solutions: by closure review 038 (c)(ii), CONFIRMED in theory audit 379,
   it can exclude every correction of norm at most b only if E sqrt(2 pi) H_max/B < Emax(b), and no such budget is
   proved, nor is its nonexistence. On the numerical side the multi-scale bases lowered the held-out probes in FLOAT
   in their first 12 steps (016, 017), and 12 more steps (018) raised them again, which the numerics team reads (FLOAT) as the
   balanced objective trading the mid field back for rF. Neither batch has a certified inverse or a converged profile.
   This ranking is a planning judgment from these numbers, not a theorem.

## The eight answers in detail (first written at 2026-10-29T06:52Z; candidate and audit entries updated through closure matrix v185)

1. Strongest a posteriori estimate now proved. Six new conditional theorems, all AUDITED:
   - sharp Sobolev framework (the linear-estimates reviewer result linear-estimate result 2, AUDITED by the theory auditor theory audit 028). Hypotheses: the background hypotheses of
     Analysis II Theorem D(b), namely (B0), (B0n), (B1) to (B5), (B7), (B9c), (B10m). The P8.4 kernel constants are
     computed exactly (C_bg = 402 instead of 4800, c_U = 8/5 instead of 5), with the audited base decay rate 297/1000
     (linear-estimate result 1, theory audit 012). Conclusion: N_s(F) <= 5289/50000000 = 1.0578e-4 at s = 2^-13 (Ns13 norm) gives an exact
     normalized solution rho_tilde + h with N_s(h) <= 43/50000 and c[h] = 0.
   - L2 framework (the theory auditor theory audit 019, independently reviewed by the linear-estimates reviewer, AUDITED as a conditional theorem in theory audit 035).
     Hypotheses (A) to (D), including the signed L^2 margin c_l + 1 - theta - kappa >= 2. Here
     theta = ess sup (|grad rho| - rho_y)/2 and kappa is the Hilbert-Schmidt norm of the symmetric double commutator
     (theory audit 016). Conclusion: X_s(F) <= 1/163840 (about 6.1035e-6) at s = 2^-17 (X3 norm, E^2 = P2^2 + 2^14 G1^2 +
     2^18 G0^2, no Hdot^-1 component) gives an exact solution with X_s(h) <= 2^-14.
   - sharp L2 framework and weighted sharp L2 framework (the linear-estimates reviewer result linear-estimate result 3, AUDITED by the theory auditor theory audit 042; scalar boxes CONFIRMED
     by numerical audit 054). They are L2 framework with the linear-estimate result 2 kernel constants and the weighted norm X_(s,w), E_w^2 = P^2 +
     w1 G1^2 + w2 G0^2. Hypotheses: those of L2 framework. Conclusions: X_(s,w)(F) <= 7.6219e-5 at s = 1/7744,
     w = (2^14, 2^18), gives an exact solution with X_(s,w)(h) <= 147/200000; X_(s,w)(F) <= 2.1035e-4 at s = 1/5184,
     w = (2^15, 2^20), gives one with X_(s,w)(h) <= 1351/1000000.
   - transient-low L2 framework, the theory audit 051 transient-low framework (the theory auditor, reviewed by the theory team closure review 009 with one repair,
     AUDITED in theory audit 057; ID registered in theory exchange 02, with stationary L2 framework[K_L] for the stationary version). It is L2 framework with (B-L2) replaced by (L): ||exp(t A_k)|| <= 2 exp(-t) on L^2 for all
     t >= 0, uniformly on the normalized ball. Conclusion: X_s(F) <= 1/196608 (about 5.0863e-6) at s = 2^-17 gives an
     exact solution with X_s(h) <= 2^-14. By theory team TP-1 (CONFIRMED in theory audit 059), the stationary bound
     (L0), ||A_k^-1|| <= K_L on [0, infinity), may replace (L). Theory audit 067 recomputed the thresholds with certified constants
     and directed rounding (CONFIRMED): 7.959492e-6 at the stated s, R; 1.5344622e-5 for K_L = 2 at s = 1/51984,
     R = 21/100000; 2.4186857e-5 for K_L = 1 and 3.0322015e-5 for K_L = 1/2 (s = 1/51529 and 1/50625). The theory team's
     printed 7.9595e-6 and 2.41869e-5 are rounded up and fail by one unit in the last digit. The finite-rank
     reduction TP-1b is repaired (theory audit 073, CONFIRMED); a Woodbury margin and a K_L certificate for any candidate are
     OPEN.
   - variable-margin L2 framework[beta_L, w] (the theory team rate trade, CONFIRMED conditional by the theory auditor theory audit 113; registered in theory exchange 02). It is
     sharp L2 framework or sharpw-v1 with the normalization 2 of (B-L2) replaced by a positive signed L^2 rate beta_L.
     The fixed Gram certificate needs beta_L above 3829321675/5037023232 (sharp weights) or 15208393675/44307283968
     (sharpw); safe endpoints are 0.76024 and 0.34325. Certified sharpw instances: beta_L = 7/5, s = 1/5476, threshold
     423/2500000 = 1.692e-4, ball 1213/1000000; beta_L = 1, s = 1/6561, threshold 533/5000000 = 1.066e-4, ball
     459/500000. It trades a weaker signed condition for a smaller threshold. Within the same fixed Gram scheme at
     beta_L = 2, better state 131 matrix floors could raise the sharp and sharpw thresholds by less than 2.2 and 1.81
     times (theory audit 119, CONFIRMED with the inherited P96 theorem).
   No existing candidate satisfies the hypotheses of any of these theorems; (L) and (L0) have not been checked for
   any candidate. Theory audit 022 and theory audit 041 are AUDITED (theory audit 045, closure review 008) as conditional low-space theorems only; they give no
   closure. The computed-defect theorem alternative defect framework (theory audit 004, sections 2 to 4) and the linear-estimates reviewer's H-free defect
   extension L2 defect framework are AUDITED conditional theorems (theory audit 062, theory audit 065). With a nonzero correction g they
   need a certified computed defect, which no worker has supplied. At g = 0 the H-free extension needs no defect and
   gives the threshold X_(s,w)(F) <= 40722836401/193491763200000 (above 2.1046e-4) at s = 1/5184, w = (2^15, 2^20),
   with X_(s,w)(h) <= 201799/149299200, the exact optimum of the sharpw estimate (corrected 16:33Z after theory audit 479; the
   earlier text said these theorems have no residual threshold). The scale-adapted weighted closure of theory audit 058 is
   AUDITED conditional (the linear-estimates reviewer review, theory audit 095) on a high resolvent hypothesis (H) that no worker has proved for any
   profile, so it has no threshold either; the origin restriction theory audit 060 (AUDITED conditional, theory audit 091) is a necessary
   condition on high energies, not a closure. The theory auditor's far-field inverse floor M >= 1/(1 + c_l - c_l a) for every
   actual inverse bound (H) (theory audit 097) is AUDITED through the theory team closure review 013 (theory audit 114). With the complete Laplacian tail theory audit 098
   and the cover theory audit 099 (CONFIRMED by numerical audit 093, numerical audit 094 and theory audit 105) it rules out the theory audit 058 scheme for state 131 at every
   a, s and Rw (matrix row 58). The continuous comparison of theory audit 107 is AUDITED through the theory team closure review 014 (theory audit 120), so the
   scheme, registered in theory exchange 02 as dyadic Y framework[a, s, Rw], is also ruled out at d2 for every 0 < a < 2, 0 < s
   < 1 and finite Rw (row 59). For candidate 007 the first and third angular modes give the same exclusion for 4/5 <= a <
   2 (theory audit 127, CONFIRMED by numerical audit 113, proof reviewed by the theory team closure review 015; row 64). For 0 < a < 4/5, the theory auditor's origin results
   (theory audit 145, theory audit 146, AUDITED through the theory team closure review 017) give a smaller ceiling Y(F) < H(c_l - 1)(1 + c_l - c_l a)/(1 + a)
   with H(c_l - 1) = 1.13024 for profiles with origin slope a0 >= 5c_l - 4, and a seven-cell cover of 0 < a < 1 +
   1/c_l for candidate 007 with minimum ratio above 1.2342 (theory audit 147; arithmetic CONFIRMED by numerical audit 128, numerical audit 129, theory audit 150 and
   closure review 017). So the scheme is RULED OUT for candidate 007 at every 0 < a < 2, 0 < s < 1 and finite Rw within the stated
   hypotheses. The floor is spectral: the line Re lambda = -(1 + c_l - c_l a) lies in the approximate point spectrum
   of the stated realization on Y, so no semigroup there decays faster than exp(-(1 + c_l - c_l a) t) (the theory team closure review 013
   remark 3, CONFIRMED by theory audit 124), and compact or finite-rank perturbations keep the resolvent floor (AUDITED through
   the linear-estimates reviewer's review, theory audit 131). These are exclusions of one sufficient scheme, not nonexistence results. A sharper
   sufficient bound on the S1 commutator for (B-L2), the parity budget, is described in the Q4 answer; at that stage its use inside
   (B-L2) had not yet been reviewed.
2. Improvement over Analysis II.
   - sharp Sobolev framework admits a residual tolerance 166 times larger than Theorem D(b) (1.0578e-4 against 6.358e-7).
     The norm family is the same, at s = 2^-13 instead of 2^-18; the A2 conversion inequalities relate the two norms,
     so 166 is a ratio of tolerances in different norms, not an enlargement of one residual ball. The
     separate component requirements on the raw residual become P2 <= 1.0623e-4, G1 <= 8.2986e-7, G0 <= 2.0747e-7 and
     H <= 2.1259e-7.
   - L2 framework has a forcing space with fewer far-field cancellations. It has no Hdot^-1 component, and a residual sector r^e is admissible for
     every e < -1 instead of e < -2. So only three sectors must vanish exactly, instead of seven (theory audit 033 CONFIRMED): (1,0), (2,0), (3,0) in the
     h-index used here, which are (2,0), (3,0), (4,0) under the global index e = 1 - l delta - 2q of the final theory report in the accompanying artifacts
     (theory audit 328). At a common exponent, dropping the Hdot^-1 component strictly enlarges the forcing
     space (theory audit 259); at different exponents the spaces need not be nested. In exchange it needs (B-L2) in place of (B1) to (B3), and its threshold is 9.6 times
     the D(b) threshold (again a ratio of tolerances in different norms).
   - weighted sharp L2 framework keeps these advantages and raises the threshold to 34.46 times that of L2 framework (331 times
     the D(b) number). These are tolerances in different norms: at the selected exponents (t = 1/5184 for sharpw,
     s = 2^-18 for D(b)) neither forcing space contains the other, since sharpw imposes fewer far-field cancellations
     but slightly more fractional regularity (theory audit 259 REFUTES the inclusion stated in the final theory report in the accompanying artifacts version3; its new
     Fourier proof was then awaiting independent review). Its requirement on G0 = ||F||_2 is 2.0542e-7, against 2.0747e-7 for
     sharp Sobolev framework. So the improvement over D(b) in the binding G0 component is about 166 times for both. The linear-estimates reviewer
     FLOAT weight scan puts the best G0 requirement of this method near 2.17e-7 (not a proof of a limit, theory audit 042).
   Intermediate audited results: rebalanced Sobolev framework (14.4 times, theory audit 012), graded Sobolev framework (componentwise boxes,
   theory audit 013) and its no-H version graded L2 framework (theory audit 039).
3. Best numerical reference.
   - state 131 (case 4 state 131) is still the latest accepted state (CONFIRMED by the numerical auditor numerical audit 001). Its residual grows like
     r^0.1048 and lies in no unweighted forcing space.
   - Among the exactly admissible references available at the start, Analysis II's d2 (baseline d2) was the best: G0 = 4.98882, G1 = 1.02914,
     P2 = 20.5368, Q3 = 128.147 (all CONFIRMED; numerical audit 024, numerical audit 026, numerical audit 043, numerical audit 050).
   - The campaign's exact candidates candidate 002 (seven branches) and candidate 003 (eight branches) cancel every
     Hdot^-1-forbidden sector. candidate 004 (four branches) cancels the three X_s-forbidden sectors. All three are
     CONFIRMED by numerical audit 039, numerical audit 044 and numerical audit 048. Their inner residuals are larger than d2's: FLOAT ||F||_2 of 312, 63.2
     and 252. Each is excluded from every specified framework ball, the two linear-estimate result 3 balls included, by a CONFIRMED
     point value (numerical audit 040, numerical audit 045, numerical audit 049, numerical audit 071 with theory audit 037, theory audit 038 and theory audit 055).
   - New snapshot candidate 005 (23:27Z): d2 plus exact branches 6 and 7, optimized for the X3 norm proxy.
     Its exact structure is CONFIRMED (numerical audit 075: 2982 generators, every baseline forbidden sector cancels, first
     survivor (3,1) with exponent -2.79044 and full-circle norm 68190.415). The numerics team's FLOAT values: G0 = 1.563 (3.2
     times smaller than d2), G1 = 7.73, P2 = 378.7, X3 proxy 1328 (d2: 2557.67), ||F||_H = 42.3, sup |F| = 1.54 at
     r = 0.26, theta = 0.0471 (numerics exchange 02 section 5). The numerical auditor computed kappa = 1.35808 from exact whole-plane norms,
     above c_l - 1 = 0.8103, so (B-L2) cannot hold (numerical audit 077, CONFIRMED by theory audit 083). Its point value
     F(0, 1/4) = -1.4096814 and its fixed-c L^2 distance above 0.01625064 are CONFIRMED (numerical audit 076 with theory audit 082), so it
     has no exact solution at its c in any ball or graded box of the matrix (rows 53, 54). Its residual components
     were not certified, so d2 remained the best certified reference at the time.
   - candidate 006: structure CONFIRMED (numerical audit 080; first survivor (3,1), full-circle norm 9125.357); point value
     F(3/7, 1/4) = 6.3536 and L^2 distance above 0.52622 (numerical audit 081, CONFIRMED by theory audit 086); at the same point
     theta_X = 6.4323 > c_l - 1, so (B-L2) fails for every kappa >= 0 (numerical audit 082, CONFIRMED by theory audit 087). It has no exact
     solution at its c in any ball or graded box of the matrix (row 55).
   - candidate 006 (23:31Z): the state-131 eight-branch family reoptimized on the E2 proxy. FLOAT G0 = 17.85,
     H = 10.1, theta 9.25, kappa 14.12; the numerics team assesses it as not a closure candidate.
   - candidate 007 (00:20Z, numerics exchange 03): the candidate 005 basis and exact constraints (2982 generators, 421
     exact rows) reoptimized on a balanced objective (an equal-weight term per dyadic annulus plus a kappa^2 penalty).
     Structure CONFIRMED (numerical audit 090: eleven forbidden sectors exactly zero, first survivor (3,1) with exponent -2.79044
     and full-circle norm 4905.09). The numerics team's FLOAT values: G0 = 0.3767 (13 times smaller than d2), G1 = 3.439, P2 =
     190.8, X3 proxy 517.1, ||F||_H = 0.6355 (d2: 390.2), sup |F| = 0.138, theta = 0.0114; 43 percent of ||F||_2^2
     lies in r in [4, 8). In the weighted norms of the matrix it was the best candidate by FLOAT values when it was
     published (elementary bound about 481 against 2557.67 for d2, because G0 carries the largest weight), although
     its G1 and P2 are larger than d2's (1.029, 20.54). Its G0, G1, P2 and ||rF||_2 are certified (below), and so is
     its ||F||_H, in (0.6355243760000922, 0.6355322685705510) (the norm-certification team, CONFIRMED by numerical audit 249); numerical audit 381 REFUTES this
     report's earlier sentence that only d2 has a certified ||F||_H. Its point value F(1/10, 73/100) = 0.0911432845
     (numerical audit 091, CONFIRMED by theory audit 108) and its fixed-c L^2 distance above 0.004769166867 (degree-7 angular probe theory audit 185,
     AUDITED through the theory team closure review 022 and theory audit 190, CONFIRMED by numerical audit 157 and theory audit 196; earlier probes gave 3.1474108e-4,
     theory audit 182, and 4.3987e-5, numerical audit 091) are certified, so it has no exact solution at its c in any scalar ball or graded
     box (rows 56, 57); a one-point bound uniform over every original graded and gradedL2 box excludes those boxes too
     (numerical audit 102, CONFIRMED by theory audit 122). Its exact sector cancellations hold only for the rational coefficients: binary64
     rounding reintroduces sector (1,0) with norm 7.18e-13 (numerical audit 096, CONFIRMED by theory audit 117). The norm-certification team computed its
     whole-plane G0 = 0.3766893247, ||rF||_2 = 7.8281155857, G1 = 3.4391037868 and P2 = 190.8266911 with exact Beta
     integrals in 512-bit balls; G0 is CONFIRMED by the numerical auditor's independent 2048-bit radial-Fourier assembly (numerical audit 139), and
     rF, G1 and P2 by the numerical auditor's independent polar method (numerical audit 153). The elementary bound X_(s,w)(F) >= (w1 G1^2 + w2
     G0^2)^(1/2) then gives X_(s,w)(F) > 732.35 with the sharpw weights (ratio 3.48e6 against weighted sharp L2 framework;
     1.83e6 from G0 alone). With all complete components (P2 and Q3 included) the norm-certification team's enclosure gives X_(s,w)(F) >
     756.5312630768, a certified ratio above 3596535.57 (CONFIRMED by numerical audit 180 and theory audit 238), from a two-sided enclosure.
     016's whole-plane G0 = 0.30889 (the norm-certification team, CONFIRMED by numerical audit 341) is now the smallest certified G0; 016's four complete
     norms are CONFIRMED (P2 by numerical audit 392), its sharpw ratio exceeds 3542234 from G0 and G1 alone (numerical audit 374 with theory audit 451 and
     numerical audit 380), and at identical s and weights its actual sharp, sharpw, bL[7/5], bL[1] and trans forcing norms exceed
     007's (numerical audit 393 with theory audit 467). 016 is RULED OUT by distance.
   - candidate 008 (00:46:30Z): a controlled comparison with 007 (same basis, exact rows and start, an
     X3-balanced objective without the rF term). The numerics team's FLOAT values are worse in every component: G0 = 1.4230,
     G1 = 4.1801, P2 = 262.92, ||F||_H = 43.03, kappa 0.8450 with (B-L2) margin -0.046. The numerics team keeps the rF term in the
     objective (FLOAT, one comparison). Its structure is CONFIRMED (numerical audit 105: eleven sectors exactly zero, first
     survivor (3,1) with full-circle norm 71468.54). Its point value F(1/10, 73/100) = -0.1061605788 (numerical audit 106,
     CONFIRMED by theory audit 125) excludes it from the stated balls of every framework of the matrix (rows 60, 61), and its
     exact full-space kappa_HS = 0.84604 > c_l - 1 (numerical audit 107, CONFIRMED by theory audit 126) defeats (B-L2) as stated.
   - candidate 009 (01:15:50Z): from 007 with the same generators and exact rows, an X3-balanced objective
     without the rF term and a kappa^2 penalty 3e8. Structure CONFIRMED (numerical audit 114: eleven sectors exactly zero, first
     survivor (3,1) with full-circle norm 7688.45, strain 1 - c_l exactly). The numerics team's FLOAT values: G0 = 1.0960,
     G1 = 2.0856, P2 = 109.76, ||rF||_2 = 43.78, ||F||_H = 7.0014, sup |F| = 0.0935 (the smallest of the campaign),
     theta 0.0113, kappa 0.7120, margin +0.0871. Its G0 is 2.9 times that of 007, so 007 remains the best candidate
     in the G0-dominated norms by FLOAT values. The numerical auditor's point value F(1/10, 73/100) = 0.0607853489 with positive gaps
     in every ball (numerical audit 115) is CONFIRMED by the theory auditor's independent reconstruction (theory audit 144), so 009 is RULED OUT in the
     stated balls (rows 62, 63).
   - candidate 010 (01:36:39Z, numerics exchange 04): the candidate 005 basis plus 960 multi-scale inner
     functions with vanishing far-field moments q < 4 at the scales R0 = 10 and 100 (3942 generators), 39 steps on
     the X3-balanced objective without the rF term. Its structure is CONFIRMED (numerical audit 122, an independent expansion of all
     3942 generators: eleven sectors exactly zero, first survivor (3,1) with full-circle norm 41655.25, every omitted
     exponent at most -3.0285, a0 = 10.06231, strain 1 - c_l exactly). Its point value F(1/10, 73/100) = -0.1176966
     gives positive gaps in every ball of the matrix (numerical audit 123, CONFIRMED by the theory auditor's independent polar
     reconstruction, theory audit 155, and the 29 comparisons of numerical audit 136), so 010 is RULED OUT in the stated balls (rows 65, 66). FLOAT values: G0 = 0.8163, G1 = 5.091, P2 = 318.8, ||F||_H = 27.65,
     sup |F| = 0.206, kappa 0.9219 (margin -0.123). Against 008 (same objective without these functions, 60 steps)
     G0, H and X3 are smaller and sup |F|, P2 and kappa larger (FLOAT, one comparison). 007 keeps the smallest G0.
   - candidate 012 (03:01:34Z): labelled by the numerics team a controlled comparison, not a certification target.
     The 005 basis (2982 generators, 421 exact rows), the balanced E_2 objective plus a kappa penalty 1e7, 30 CPU
     Gauss-Newton steps from 009 on the MID8 radial rule; the objective fell only from 1.83e8 to 1.78e8. FLOAT values
     (MID 32): G0 1.556, G1 12.9, P2 908, ||F||_H 2.84, sup |F| 0.773, kappa 0.878 (margin -0.079), weak distance
     1.50e-2 at k = 8. It is worse than its parent 009 in every FLOAT quantity except H. Its exact structure is CONFIRMED
     (numerical audit 155: eleven sectors zero, first survivor (3,1)), and numerical audit 155's point value F(1/10, 73/100) = 0.0392951615 gives
     positive gaps in every stored ball (CONFIRMED by the theory auditor's independent polar method, theory audit 204, and numerical audit 167), so it is
     RULED OUT in the stated balls (rows 67, 68).
   - candidate 011 (03:27:48Z): also labelled a controlled comparison, not a certification target.
     007's objective and start plus 960 multi-scale functions (3942 generators), 20 CPU steps; the objective fell
     only from 1.711e7 to 1.706e7. FLOAT values (MID 32): G0 0.3745, G1 3.53, P2 196, ||F||_H 0.612, sup |F| 0.153,
     kappa 0.7277, weak distance 5.1e-4 at k = 12 (007: 1.3e-4 in FLOAT). No real gain over 007; nothing about it is
     certified (rows 69, 70, OPEN).
   - candidate 013 (04:39:56Z): labelled by the numerics team a pairing-row experiment, not a certification target.
     007's balanced objective plus 27 first-mode penalty rows sqrt(1e15) I_k, 12 CPU Gauss-Newton steps on the MID 16
     radial rule; same basis and 421 exact rows as 007. FLOAT values (MID 32): G0 0.3722, G1 3.441, P2
     191.2, ||F||_H 0.631, kappa 0.7270; the first-mode pairings for k <= 128 fall by about three orders of magnitude, while
     those for k >= 384 and the held-out angular probes at r about 25 to 30 stay unchanged. Its source, sectors,
     origin identities and the state 131 leading density are CONFIRMED (numerical audit 197); its point value F(1/10, 73/100) =
     0.0908758993 gives positive gaps in the stated balls (numerical audit 201, CONFIRMED by theory audit 266), and its fixed-c L^2 distance
     exceeds 0.00199234339 (held-out probe n = 21, K = 522; theory audit 255, CONFIRMED by numerical audit 204 and theory audit 264), so it is RULED
     OUT in every scalar ball and graded box (rows 71, 72).
4. Regularity and far-field requirements.
   - candidate 014 (05:22:50Z): also a pairing-row experiment, not a certification target. 007's balanced
     objective plus 102 penalty rows sqrt(1e12) I: the 27 first-mode probes and the 75 angular probes
     r v^2 t^K sin(n theta) of numerical audit 160 (n = 3..31 odd, K = (n-1)/2 + {0, 8, 32, 128, 512}); 12 CPU steps on the MID 16
     rule; same basis and 421 exact rows as 007. FLOAT values (MID 32): G0 0.3726, G1 3.440, P2 190.9, ||F||_H
     0.6313, kappa 0.7270. The angular design rows at r <= 10 fall by one to two orders of magnitude (mode 7 best m
     8.4e-6 against 2.87e-3 for 007; design values, not evidence), while every angular probe with K about 520 (r about
     23 to 32, n = 19 to 31) is unchanged from 007 and 013 (n = 21, K = 522: m 1.12e-3). Exact structure
     CONFIRMED (numerical audit 212); positive point gaps at (1/10, 73/100) for every point-tested ball, F = 0.0907733102 (numerical audit 213,
     CONFIRMED by the theory auditor's independent raw-to-polar path, theory audit 279), so 014 is RULED OUT in every point-tested ball and
     every original graded box at every c in the chart (rows 75, 76). The angular probes, n = 21, K = 522 included, were objective rows, not held out
     (numerical audit 211): an exact value there is a valid lower bound but design data. The fixed-c L^2 distance from
     that probe is above 0.00198301351067 (numerical audit 214, CONFIRMED by the theory auditor's independent polar assembly, theory audit 280), 4.337
     times the graded budget, so 014 is RULED OUT in the statL and bL balls as well (row 75).
   - candidate 015 (06:18:19Z): a conditioning control, not a certification target. The same 102 rows as
     014 on the exact 1922-generator quotient basis of 013 (the 1060 exact zero-potential directions removed; start
     state CONFIRMED by numerical audit 218); 12 CPU steps on the MID 16 rule. FLOAT values (MID 32): G0 0.3723, G1 3.434, P2
     191.0, ||F||_H 0.6312, kappa 0.7271; objective plateau 1.7210e7 as for 014; probes at r about 23 to 32 unchanged
     ((21, 522): m 1.136e-3, a design row). Held-out values (first-mode k outside its row list and the theory exchange 04
     held-out rule set) are not yet reported. Structure CONFIRMED (numerical audit 233: a0 about 10.31148346829147, no forbidden
     sector; independently reconstructed in theory audit 297). Point gaps at (1/10, 73/100), F = 0.0902490859, uniform graded
     gap 0.0698458144 (numerical audit 234, CONFIRMED by the theory auditor's independent polar jets, theory audit 299); fixed-c L^2 distance above
     0.000351804115950603 from the probe n = 19, K = 600, outside its documented objective span (theory audit 298 with
     numerical audit 235), 123.4 times the sharpw family ceiling. So 015 is RULED OUT in every registered scalar ball and graded
     box (rows 77, 78). A second registered held-out probe (23, 600) gives distance above 0.001232449584356253
     (numerical audit 237, CONFIRMED by the theory auditor's independent polar path, theory audit 304), which exceeds the graded budget 25/54684 by a
     factor above 2.69, so 015 is excluded from every graded box by distance alone; the registered probe (23, 2400)
     gives > 0.003033479200692 (numerical audit 239, OPEN; chosen within the registered family after a FLOAT screen). The 015
     structure of theory audit 297 is accepted in full against numerical audit 233 (theory audit 306).
     That
     the plateau did not move is an observation about one damped run, not a proof that the span has no better point
     (theory audit 273, theory audit 289).
   - candidate 016 (06:46:04Z; checksum manifest verified by the coordinator at 06:47Z): a design test of mid-field
     resolution, not a certification target. The exact 1922-generator quotient basis of 013 plus 252 multi-scale
     legqs functions at R0 = 25 (four vanishing far-field moments; blocks j = 1, 2, 3, m = 9 to 15, density sine modes
     19 to 31 per the numerics team, 17 to 31 by numerical audit 248); 2174 generators, 421 exact rows; objective 007's balanced E_2 proxy plus 67 pairing rows (27
     first-mode k and the numerical audit 160 angular probes with n <= 17 only); 12 CPU steps on the MID 16 rule. FLOAT values
     (MID 32): G0 0.3089, G1 3.727, P2 218.1, ||F||_H 0.6178, kappa 0.7338. The probes with n >= 19 were fixed before
     the run and are held out; in FLOAT they fall by factors 3 to 5 against 013 ((21, 522): 1.12e-3 to 2.33e-4;
     (23, 2400): 1.80e-3 to 6.50e-4), and the largest remaining is (19, 1800) at 9.02e-4, a registered numerical audit 229
     probe (numerical audit 243). The numerical auditor verifies the structure exactly from all 2174 raw generators (numerical audit 242: primary c and
     Theta_0 of state 131, every forbidden exponent of the complete prefix zero, first surviving exponent
     4 gamma - 5). Its point value F(1/10, 73/100) = 0.0902175690 gives positive gaps for the six registered scalar
     point budgets and a uniform graded gap 0.0698206185 (numerical audit 242, CONFIRMED by the theory auditor's independent polar jets,
     theory audit 307), so 016 is RULED OUT in every point-tested ball and every original graded box (rows 80, 81). Numerical audit 243
     CONFIRMS that the 25 registered numerical audit 229 probes lie outside its objective span (67 rows, all of angular frequency
     at most 17). The numerical auditor finds fixed-c L^2 distances above 0.001092633159 from the registered probe (23, 2400) and
     above 0.001470360924 from (19, 1800) (numerical audit 246, exact R0 = 25 rational fields at 2048 bits). The theory auditor reproduces the
     first by an independent polar path (all 360 density and 360 stream components, t^K kept factored, exact rational
     CRT and Arb hypergeometric moments at 2048 bits; theory audit 310, CONFIRMED, 125 s). It exceeds the graded ceiling
     25/54684 by a factor 2.39 and the sharpw family ceiling by a factor 383.4, so 016 is RULED OUT in the statL and
     bL balls of row 80 as well and hence in every registered scalar ball and graded box. Theory audit 310 calls it one registered necessary witness,
     not an estimate of the correction distance. The theory auditor reproduces the (19, 1800) value by the same path
     (theory audit 311; > 0.001470360924, 3.21 times the graded ceiling), the numerical auditor accepts both reproductions (numerical audit 253), and the theory auditor
     CONFIRMS the 016 sector flags of numerical audit 242 from the raw generators (theory audit 313: nonzero sectors exactly (4,1), (9,0),
     (5,1), (1,2), (10,0), first exponent 4 gamma - 5). Numerical audit 248 (CONFIRMED by theory audit 321)
     finds an exact nonzero mode 17 density coefficient among the 252 new generators, so their density support is
     17, 19, ..., 31; this does not affect the span audit, whose objective rows have frequency at most 17 and whose
     probes have frequency at least 19.
   - candidate 017 (07:11:15Z; checksum manifest verified by the coordinator at 07:15Z; rows 82, 83): the scale
     comparison, identical to 016 except that the 252 functions have scale R0 = 50. RULED OUT in every specified ball
     (below). The norm-certification team's complete whole-plane components (13:04Z, 1024-bit balls, CLAIMED pending the numerical auditor): G0 =
     0.3209330653..., rF = 7.0491564793..., G1 = 3.5377622350..., P2 = 200.5219606715...; E_* without H =
     521.7926901547 (the note's text value 528.3 disagrees with its own record). The norm-certification team's note 13:49Z (CLAIMED pending
     the numerical auditor) adds five of six weak probes with conditional distance floors > 5.0420e-5 and > 2.6736e-5 (frozen n = 7
     and n = 1 vectors), > 5.9604e-4 at (21, 522), > 1.0682e-3 at (23, 2400) and > 1.6711e-3 at (19, 1800), each below
     the numerical auditor's sharper numerical audit 259, numerical audit 256 and numerical audit 257 floors for the same probes. FLOAT values (numerics exchange 09, MID 32): G0
     0.3209, G1 3.538, P2 200.5, ||F||_H 0.6153, kappa 0.7279; held-out (21, 522) 3.36e-4,
     (23, 2400) 6.35e-4, best remaining (19, 1800) 1.03e-3. That probe is 7.32e-5 for 013 and 9.02e-4 for 016, so
     both added scales raise mode 19 at K = 1800 (r about 35) while lowering modes 21 to 31. Four FLOAT held-out
     values exceed the graded budget 4.5717e-4 by factors 1.16 to 2.25. A design experiment, not a certification
     target. The numerical auditor verifies its exact structure from all 2174 raw generators and finds a point value
     F(1/10, 73/100) = 0.0899392743, a uniform original graded gap 0.0695362257 and positive gaps for the six
     registered scalar point budgets (numerical audit 254). The theory auditor reproduces the point fields and all gaps by an independent
     polar path (theory audit 319), so 017 is excluded from every point-tested ball and every original graded box. Numerical audit 255
     CONFIRMS that the 25 registered probes and the diagnostic (21, 522) lie outside the span of its 67 objective
     rows. The numerical auditor's exact R0 = 50 held-out distance exceeds 0.001068502321536437 at (23, 2400) (numerical audit 256, CONFIRMED by
     the theory auditor's independent full polar reconstruction, theory audit 320; 2.34 times the graded ceiling, 375.0 times the sharpw
     family ceiling), which excludes the statL and bL balls as well; the value 0.001671830698 at (19, 1800)
     (numerical audit 257) is CONFIRMED by the theory auditor's independent polar path (theory audit 331); the diagnostic (21, 522), outside the registered set, with a distance above
     0.000596123050 (numerical audit 259), is OPEN. The numerical auditor accepts theory audit 319, theory audit 320 and theory audit 323 (numerical audit 260 to numerical audit 262). The extension to every c of the chart uses the state 131 leading density of 017, verified
     exactly by the numerical auditor (numerical audit 254); the theory auditor reproduces the complete far-field sector prefix of 017 independently (theory audit 323).
   - candidate 018 (08:02:27Z; checksum manifest verified by the coordinator at 08:03Z; rows 84, 85): 016 continued
     by 12 Gauss-Newton steps on the same basis, objective and held-out set (objective 1.4865e7 to 1.4516e7).
     The numerical auditor finds the exact structure and positive point gaps (numerical audit 270, uniform graded gap 0.0754729725), CONFIRMED
     by the theory auditor's independent polar fields (theory audit 342), complete sector prefix (theory audit 343) and exact origin normalization
     (theory audit 346: c + partial_y u2(0) = 1, density slope in (10.3106636255510647, 10.3106636255510648)); the numerical auditor accepts
     these and the theory audit 345 distance (numerical audit 275 to numerical audit 278). The numerical auditor also CONFIRMS that the registered held-out probes lie outside the objective span (numerical audit 271). Its registered
     distance above 0.001655825792 at (19, 1800) (numerical audit 272) is CONFIRMED by the theory auditor's independent polar path (theory audit 345;
     3.621 times the graded ceiling, 581.0 times the sharpw family ceiling); the (23, 2400) value above
     0.001328016044 is CONFIRMED by theory audit 349. So 018 is RULED OUT in every specified scalar ball and graded box (rows 84, 85). FLOAT values (the numerics team index in the accompanying artifacts, MID 32): G0 0.3127,
     G1 3.856, P2 223.6, ||F||_H 0.6153, kappa 0.7348; every held-out probe in its index in the accompanying artifacts entry is above 016's, by 13
     to 35 percent for eight of the nine and by a factor 2.33 at (29, 526) ((21, 522) 2.80e-4, (23, 2400) 7.89e-4,
     (19, 1800) 1.02e-3). The numerics team reads this as the balanced objective trading the mid field back
     for rF after the first gains of the new span (FLOAT interpretation) and keeps 016 as the better reference. A
     design experiment, not a certification target.
   - candidate 019 (08:28:42Z; checksum manifest verified by the coordinator at 08:31Z; rows 86, 87): 017 continued
     by 12 Gauss-Newton steps on the same basis, objective and held-out set (objective 1.4400e7 to 1.42514e7).
     The numerical auditor CONFIRMS the recorded objective provenance and that the registered probes lie outside the span of its 67
     rows (numerical audit 280). Its exact structure, normalization c + partial_y u2(0) = 1, vanishing forbidden residual prefix
     and point gaps at (1/10, 73/100) (numerical audit 279) are reproduced by the theory auditor's independent polar fields (theory audit 353: residual
     in (0.08974395121409148, 0.08974395121409150), uniform graded gap above 0.06934033757930145), origin
     normalization (theory audit 354) and complete sixteen-sector prefix with the leading profiles of 007 (theory audit 355). Its fixed-c
     L^2 distance above 0.001661806967 from the registered probe (19, 1800) (numerical audit 282) is CONFIRMED by the theory auditor's
     independent polar path (theory audit 357; 3.634 times the graded ceiling and 583.1 times the sharpw family ceiling). So
     019 is RULED OUT in every specified scalar ball and graded box (rows 86, 87). FLOAT values (the numerics team index in the accompanying artifacts, MID 32): G0 0.3251, G1 3.587, P2
     202.2, ||F||_H 0.6142, kappa 0.7284; every held-out value in its index in the accompanying artifacts entry differs from 017's by less than 10
     percent ((21, 522) 3.55e-4, (23, 2400) 6.34e-4, (19, 1800) 1.02e-3). The numerics team names it a trial comparison, not a
     certification target, and draws no span, mass or stationarity inference (theory audit 340).
   - candidate 020 (08:46:18Z; checksum manifest verified by the coordinator at 08:50Z; rows 88, 89): 016's basis
     plus 252 legqs R0 = 50 functions in the same blocks (2426 generators, scales 25 and 50; abstract dimension 2426
     by numerical audit 274 with theory audit 348), the same 67 objective rows and held-out set, 12 steps (objective 1.7475e7 to
     1.35019e7, the lowest of the campaign). Numerical audit 292 CONFIRMS that the actual 2426 shapes realize the accepted
     mixed-scale space and that the 25 registered held-out probes and the (21, 522) diagnostic lie outside the
     analytic span of its 67 rows (independently bound by theory audit 364). The numerical auditor's exact computation (numerical audit 291) gives the
     fixed c, the origin normalization, vanishing forbidden sectors, point residual 0.1048053190519705 at
     (1/10, 73/100), positive gaps for the six named point balls and a uniform graded gap 0.0844022623041347;
     the theory auditor reproduces it independently (theory audit 360 point fields and gaps, theory audit 361 origin normalization, theory audit 362 complete
     sector prefix). Its fixed-c L^2 distance above 0.001855374677442712 from the registered probe (19, 1800)
     (numerical audit 293, all 2426 raw generators and both scales) is CONFIRMED by the theory auditor's independent polar path (theory audit 363,
     radius in (0.0018553746774427130, 0.0018553746774427131)): 4.058 times the graded ceiling and 651.1 times the
     sharpw family ceiling. So 020 is RULED OUT in every specified scalar ball and graded box (rows 88, 89). FLOAT values (numerics exchange 10,
     MID 32): G0 0.3201, sup|F| 0.1996, kappa 0.7374; each of the seven registered held-out probes with K >= 1200
     listed in numerics exchange 10 is above both 016's and 017's ((19, 1800) 1.14e-3), and several small-r held-out probes
     in modes 19 to 31 rose by up to 8 times against 016. The numerics team names it a trial comparison, not a certification
     target.
   - candidate 021 (10:05:34Z; checksum manifest verified by the coordinator, last at 10:17Z; rows 90, 91): 020's
     2426 generators with 81 weak rows (020's 67 plus 14 mid-field rows n = 19..31 at K0 = 128, 512, weight 1e12)
     and 40 GPU steps from 020. The numerics team reports that the 14 rows were inert at this weight; theory audit 390 REFUTES that
     inference from the penalty's small share of the objective, so their causal effect is OPEN. Its held-out record (52ba613b...) was written after launch; the 25-probe register
     predates the run. Numerical audit 315 CONFIRMS the 2426 shapes (equal to the accepted 020 space) and the 81 recorded rows.
     The numerical auditor's exact computation (numerical audit 314, CONFIRMED by the theory auditor's independent polar Euler derivatives, theory audit 387, exact
     center relation, theory audit 388, and complete sector prefix, theory audit 389) gives B0n exactly normalized, the
     state 131 leading density, all eight forbidden exponents zero, point residual 0.1004988054901384 at
     (1/10, 73/100), and failure of all six named scalar point inequalities and of the original graded point test
     (uniform gap 0.0800973541730740). Numerical audit 313 encloses ||rho021 - rho020||_2 = 0.00734925324971972..., above
     the screening rule allowance for every registered ceiling (graded about 0.00139820), so the screen transfers no
     exclusion from 020; the theory auditor CONFIRMS the compatibility lemma (theory audit 393) and the pair norm (theory audit 394), both accepted
     by the numerical auditor (numerical audit 322), and the numerical auditor CONFIRMS the theory team's review closure review 041 of the lemma (numerical audit 324); this is the failure of one
     sufficient test only. Numerical audit 316 gives its fixed-c L^2 distance from the registered probe
     (19, 1800) above 0.001864696854799172 (4.078 times the graded ceiling, 654.3 times the sharpw family
     ceiling), CONFIRMED by the theory auditor's independent 2048-bit polar and direct hypergeometric certificate (theory audit 392).
     So 021 is RULED OUT in every ball of rows 90 and 91, including the statL and bL balls. Theory audit 395 CONFIRMS
     numerical audit 315 for the current 81-row objective (registered probes outside its span, (21, 522) inside; accepted in
     numerical audit 323). FLOAT values
     (the numerics team diagnostic record, MID 32): G0 0.2996, sup|F| 0.1398, kappa_inner 0.7313; the largest registered held-out value is
     1.14e-3 at (19, 1800), as for 020, and 8 of the 25 registered values exceed the graded ceiling. The numerics team names it
     a trial comparison, not a certification target.
   - candidate 022 (10:28:22Z; checksum manifest, manifest in the accompanying artifacts sha 14deff3e... and held-out record sha
     52ba613b... checked by the coordinator at 10:38Z; rows 92, 93): 016's 2174 generators plus 240 legqs R0 = 25
     functions in the existing higher blocks j = 1 (m = 16 to 19) and j = 2, 3 (m = 16 to 23), density modes 31 to
     47: 2414 generators, the 67 rows of 016, 40 GPU steps. Nothing is certified. FLOAT values (the numerics team diagnostic record,
     MID 32): G0 0.2816 and sup|F| 0.1276, the lowest of the campaign, kappa_inner 0.7315; the largest registered
     held-out value is 8.30e-4 at (19, 1800), and 7 of the 25 registered values exceed the graded ceiling (016: 7,
     020: 8). Its held-out record was written at 09:13Z, after the 08:32Z launch. The numerics team names it a trial
     comparison, not a certification target. Numerical audit 321, independently replayed by the theory auditor in theory audit 403, CONFIRMS its 2414 actual shapes, the inherited rank
     application, the recorded 67-row objective and that all 25 registered and 35 diagnostic probes lie outside
     that objective's analytic span; it REFUTES the manifest in the accompanying artifacts statement that modes 31 to 47 all lie outside a sweep
     through mode 31 (mode 31 overlaps). The numerical auditor's exact computations: exact c, the center relation and eleven of 16
     computed sectors exactly zero, F = 0.0887596 at (1/10, 73/100) against the original graded point allowance
     0.0203986, failures of all six scalar point budgets (numerical audit 326, CONFIRMED independently by the theory auditor in theory audit 405,
     theory audit 406 and theory audit 407); fixed-c L^2 distance above 0.00135251075726327 from (19, 1800), 474.6 times the sharpw
     family ceiling and 2.958 times the graded ceiling (numerical audit 327, CONFIRMED independently by the theory auditor in theory audit 408);
     ||rho022 - rho016||_2 = 0.0088109875626 with every sufficient transfer screen failing (numerical audit 325, no
     exclusion by itself). RULED OUT in every ball of rows 92 and 93.
   - candidate 023 (10:42:28Z; checksum manifest checked by the coordinator before matrix v112; rows 94, 95):
     016 plus 252 legqs R0 = 100 functions in the blocks m = 9 to 15 (scales 25 and 100, 2426 generators), the 67
     rows of 016, 40 GPU steps. Nothing is certified. FLOAT values (the numerics team diagnostic record, MID 32): rF 5.942, the lowest of
     the campaign, while G0 0.3228 and sup|F| 0.1786 are above 016's, kappa_inner 0.7373; the largest registered
     held-out value is 1.62e-3 at (19, 1800), and 10 of the 25 registered values exceed the graded ceiling. The numerics team
     reads it as a negative design result for scale 100 under this objective (trial comparison). The numerical auditor's numerical audit 336 to
     numerical audit 339 give the exact structure, positive point gaps for all six scalar budgets, a uniform graded point gap
     0.06288, the prefix and a fixed-c L^2 distance above 0.002634958245163687 from (19, 1800), 924.6 times the
     sharpw family ceiling and 5.763 times the graded ceiling; the theory auditor reproduces all of them independently (theory audit 416
     to theory audit 420) and the numerical auditor accepts the reproductions (numerical audit 348 to numerical audit 350). RULED OUT in every ball of rows 94 and 95.
   - candidate 024 (11:31:32Z; checksum manifest checked by the coordinator before matrix v118; rows 96, 97): the
     rule control of 016 (same start, 67 rows and 12 steps, objective on the MID 32 rule instead of MID 16; 2174
     generators). The numerical auditor's own numerical audit 343 and numerical audit 344, reproduced independently by the theory auditor (theory audit 428, theory audit 431), give six positive scalar
     point gaps, the original graded point gap 0.07487 and a fixed-c L^2 distance above 0.001556 from (19, 1800),
     3.403 times the graded ceiling and 546.0 times the sharpw family ceiling, so 024 is RULED OUT in every ball of
     rows 96 and 97 (the numerical auditor accepts the reproductions in numerical audit 357 to numerical audit 359). FLOAT values
     (the numerics team diagnostic record, MID 32): G0 0.3275 and sup|F| 0.1859, both above
     016's, P2 209.6 and G1 3.680 below; the largest registered held-out value is 9.55e-4 at (19, 1800), and 7 of
     the 25 registered values exceed the graded ceiling (016: 7). The numerics team reads it as no gain from the finer rule at
     12 steps (trial comparison). The held-out registration hash cited in the evidence index in the accompanying artifacts (58586004...) does not match the
     file the held-out record for candidate 024 in the accompanying artifacts (e171c051...); the manifest in the accompanying artifacts cites neither. The numerics team states that 58586004... is the
     hash of the first text of the file, before a wording fix 30 seconds later; the numerical auditor's numerical audit 346 reconstructs that
     text from the stated edit and obtains exactly 58586004... with the same 60 probe pairs (the save times are not
     independently witnessed), and numerical audit 342 confirms the current hash and that the probe list is outside the 67
     rows. The theory auditor's theory audit 427 rebinds the shapes, rows and probes, reproduces 58586004... by reversing the edit, and
     notes that two MID16 index labels remain incorrect and that, with both the radial rule and the backend changed
     from 016, no one-variable causal comparison is justified. RULED OUT.
   - candidate 025 (12:50:59Z; checksum manifest checked by the coordinator, five files OK; held-out file
     the held-out record for candidate 025 in the accompanying artifacts 6412b262..., written before the 10:05Z launch; rows 99, 100): 016's start plus scale-50, scale-100
     and higher-block scale-25 functions (2918 generators), with 016's 67 rows at weight 1e12 and 14 held-in mid-field
     rows at weight 1e16 (so the K0 = 128 and 512 probes are objective rows), 60 Gauss-Newton steps on GPU. FLOAT
     (the numerics team diagnostic record, MID 32): G0 0.3051, sup|F| 0.1646, G1 4.067, P2 245.1; the largest registered held-out value is
     1.27e-3 at (19, 1800), and 10 of the 25 registered values exceed the graded ceiling (016: 7). The numerics team reads it as a
     sensitivity run: the weighted rows are met to 1e-8 to 6e-6, while the registered probes at K >= 1200 rise above
     016's (FLOAT trial comparison). The theory auditor's theory audit 436 (13:03Z, proof b4257d03..., 554 checks) CONFIRMS the exact
     structure: 2918 independent potential generators and density images, the 81 analytic objective rows with weights
     1e12 and 1e16, and the 46 diagnostic probes outside that span; it REFUTES the completeness of two manifest in the accompanying artifacts
     fields, which end at 'at weight ' without the value 1e16. The numerical auditor's own numerical audit 361 agrees in every reported number.
     The numerical auditor's numerical audit 362 finds F(1/10, 73/100) = 0.0902711481..., positive gaps for the six registered scalar point budgets
     and a uniform original graded gap 0.0698812708... > 0, with the origin (c + strain = 1, a0 = 10.3085... > 0) and
     the forbidden sectors verified exactly; numerical audit 363 CONFIRMS the complete sixteen-sector prefix through -7/2 (eleven
     zero; first surviving exponent -11375183046454913/4076476460239181, about -2.7904). These are the numerical auditor's own
     results; the numerical auditor's numerical audit 364 (13:10:44Z, result 63c31f68..., 2048 bits, all 63 groups) gives a fixed-c L^2 distance >
     0.002065801265578052 from the registered held-out probe (19, 1800), 4.518 times the graded ceiling and 724.9
     times the sharpw family ceiling (rounded down). The theory auditor reproduces numerical audit 362 to numerical audit 364 independently (theory audit 438 to
     theory audit 441, 13:12Z to 13:15Z; theory audit 441 with 63 moments at minimum accuracy 1933 bits), the numerical auditor accepts the reproductions
     (numerical audit 370, numerical audit 371), numerical audit 365 CONFIRMS theory audit 436, and theory audit 444 accepts numerical audit 365. RULED OUT in every ball of rows 99 and 100;
     not a certification target.
   - candidate 026 (13:12:37Z; checksum manifest checked by the coordinator at 13:25Z, five files OK;
     held-out file the held-out record for candidate 026 in the accompanying artifacts 2016d960..., recorded by the numerics team as written in the launch second 11:31:32Z; rows 101,
     102): the 022 state (2414 generators, no new functions) continued 60 Gauss-Newton steps with the 81 rows of 025
     (016's 67 rows at weight 1e12 and 14 held-in mid-field rows at weight 1e16). FLOAT (the numerics team diagnostic record, MID 32): G0
     0.2788, below 022's 0.2816, sup|F| 0.1558, G1 3.627, P2 223.5; the largest registered held-out value is 8.32e-4
     at (19, 1800), and 9 of the 25 registered values exceed the graded ceiling (022: 7). Against 022, 9 of the 25
     registered values fall and 16 rise (the coordinator's count from the numerics exchange 13 table; FLOAT trial comparison).
     The numerical auditor's own numerical audit 366 to numerical audit 369 (13:15Z to 13:21Z) CONFIRM the structure (2414 shapes in 022's order, 81 rows, 46
     probes outside their span), the complete sixteen-sector prefix through -7/2, the exact origin (c + strain = 1, a0
     = 10.3094... > 0), positive gaps for the six scalar point budgets, a uniform graded gap 0.0594850... > 0 at
     (1/10, 73/100), and a fixed-c L^2 distance > 0.001355907204057457 from (19, 1800), 2.965 times the graded ceiling
     and 475.8 times the sharpw family ceiling (rounded down). The theory auditor reproduces numerical audit 366 to numerical audit 369 independently (theory audit 446
     to theory audit 450, 13:39Z to 13:41Z; theory audit 450 with 63 moments at minimum accuracy 1935 bits, by an independent polar and
     direct hypergeometric path with exact CRT identities that runs no foreign code); the numerical auditor accepts the reproductions
     in numerical audit 377 to numerical audit 379 (13:55:18Z; numerical audit 379 compares all 63 moment groups of both paths, minimum accuracy 1934 bits).
     RULED OUT in every ball of rows 101 and 102; not a certification target.
   - candidate 027 (14:13:51Z; checksum manifest checked by the coordinator by 14:20Z, five files OK; exact JSON
     a3bd6a51..., manifest in the accompanying artifacts 1b13ea7e...; held-out file the held-out record for candidate 027 in the accompanying artifacts c99eb804..., file time 12:28:14Z, before the
     12:34Z launch; rows 103, 104): the control for 026, the 022 state (2414 generators, no new functions) continued
     60 Gauss-Newton steps with the plain 67 rows of 016 and no held-in mid-field rows, so it differs from 026 only by
     the absence of the 14 rows at weight 1e16. FLOAT (the numerics team diagnostic record, MID 32): G0 0.2762 (026 0.2788, 022 0.2816), G1
     3.426, P2 199.7, rF 6.820, H 0.6101, sup|F| 0.1240, kappa_inner 0.7301 ((B-L2) margin +0.0689); the largest
     registered held-out value is 8.25e-4 at (19, 1800), and 7 of the 25 registered values exceed the graded ceiling.
     The numerical auditor's numerical audit 375 confirms the 100 printed values of the numerics team's 13:38Z per-probe table and REFUTES that note's range
     'within x0.83 to x1.17 of 022' (the stored 027/022 ratios run from about 0.826 to 1.343, with 16 decreases and 9
     increases). Its structure, point gaps and distances are not audited. OPEN; not a certification target.
   - candidate 028 (snapshot 15:24:01Z; checksum manifest checked by the coordinator at 15:29Z, five files OK; manifest in the accompanying artifacts
     1aa4d4e8..., exact JSON 70afa847..., sector table bc5cef9d...; held-out file the held-out record for candidate 028 in the accompanying artifacts caf3517a..., file
     time 12:51:53.76Z, before the launch log at 12:51:53.87Z; rows 107, 108): a design control, 022 plus 252 legqs
     functions of scale R0 = 25 and radial degrees 12 to 23 in m = 9 to 15 (2666 generators), 60 Gauss-Newton steps
     (39 accepted) with the plain 67 rows of 016 and no held-in rows, loss 1.280816e7. FLOAT (the numerics team diagnostic record, MID 32): G0
     0.2442, G1 3.260, P2 197.1, rF 6.608, H 0.6104, sup|F| 0.1214, kappa_inner 0.7311 ((B-L2) margin +0.0678); the numerics team
     reports ten nonautomatic EXACT-ZERO sectors (first surviving exponent -2.7904, no audit). The largest registered
     held-out value is 8.15e-4 at (19, 1800), and 6 of the 25 registered values exceed the graded budget (the largest
     by a factor of about 1.78); the largest sampled first-mode FLOAT weak value is 5.49e-4 at k = 512 (an objective
     row). numerics exchange 15 (15:25:44Z) reports that against the matched control 027, 028 moves 11 of the 15 registered
     probes with K <= 1200 outside the 027 against 022 band 0.826 to 1.343, and of the ten K >= 1800 probes only (31,
     1800), and withdraws the numerics team's earlier statement that the registered probes did not respond to any basis change
     beyond 016's scale-25 functions. Its structure, point gaps and distances are not audited. OPEN; not a
     certification target.
   - Membership: N_s-type spaces need seven exact sector cancellations, X3 norm only three.
   - state 131 fails both, because sector (1,0) is nonzero (Theorem E).
   - d2, Mpen2 and b6 satisfy both (CONFIRMED by the numerical auditor numerical audit 007 to numerical audit 009).
   - For L2 framework and its sharp variants, b6 fails (B-L2) because kappa = 1.76062 > c_l - 1 (CONFIRMED). For d2,
     the numerical auditor proved theta <= 2/25 on the whole plane by a 768-bit adaptive cover, so the margin is at least 2.01990 and
     (B-L2) holds (numerical audit 051, CONFIRMED by theory audit 053 with an independent 120-cell cover). The same method gives
     M1 >= (9/10) I on the whole plane for d2 (numerical audit 056, CONFIRMED by theory audit 061 with an independent 326-cell cover). Mpen2 needs theta <= 0.0977, not certified.
   - The new candidates violate (B-L2): theta >= 47.6, 30.9 and 0.88 at rational witness points (numerical audit 046, numerical audit 049,
     CONFIRMED by theory audit 046) for candidate 002 to 004, kappa = 1.35808 > 0.8103 for candidate 005 (numerical audit 077, CONFIRMED by theory audit 083), and theta_X = 6.4323 at
     (3/7, 1/4) for candidate 006 (numerical audit 082, CONFIRMED by theory audit 087).
   - candidate 007 is the first exactly admissible candidate of the campaign for which (B-L2) holds: its exact
     kappa_HS = 0.72816468 (numerical audit 092, CONFIRMED by theory audit 111) requires theta <= 0.08215, and the numerics team's FLOAT theta is 0.0114
     (FLOAT margin +0.072). The numerics team's FLOAT kappa 0.72694 omits the exterior beyond r = 8356 (numerical audit 097, CONFIRMED by theory audit 118). The numerical auditor
     has a complete 768-bit Bernstein and Taylor cover of the compactified plane with 223 cells that gives
     theta <= 2/25 and the signed rate c_l + 1 - theta - kappa > 2.00215453 (numerical audit 111), CONFIRMED by the theory auditor's
     independent 1024-bit cover with 232 closed cells (theory audit 162), so (B-L2) holds for 007 (rate > 2.02568 with the
     AUDITED theory audit 161 radial compression). This is one hypothesis of L2 framework; 007 still fails the residual
     smallness by more than 3596535.57 (certified, numerical audit 180 with theory audit 238) and is excluded from every ball by its CONFIRMED L^2
     distance and point values. candidate 008 fails (B-L2) as stated: its exact kappa_HS = 0.84604 >
     c_l - 1 (numerical audit 107, CONFIRMED by theory audit 126). candidate 009 has the exact full-plane kappa_HS = 0.71321 (numerical audit 121, CONFIRMED
     by theory audit 166), so (B-L2) needs theta <= 0.09710 (FLOAT theta 0.0113); no theta cover yet. candidate 010 fails (B-L2)
     in FLOAT (kappa 0.9219 > c_l - 1). variable-margin L2 framework (theory audit 113) accepts a margin beta_L below 2 at a smaller threshold.
   - Parity budget (the theory auditor theory audit 128; the inequality and the d = 12 matrices for candidate 008 are independently proved and
     reproduced by the numerical auditor, numerical audit 116, CONFIRMED): the double commutator preserves the four parity blocks, so for an
     even-even finite family with Gram matrix G and compression B the S1 operator norm is at most
     sqrt(kappa_HS^2 - tr(G^-1 B G^-1 B)). For candidate 008 this gives 0.82582 at d = 12 (CONFIRMED), 0.81512 at d = 32
     (theory audit 129, CONFIRMED by numerical audit 124) and 0.80747 with 80 tests in three parity blocks (theory audit 132, CONFIRMED by numerical audit 119 through an independent route); the
     last is below c_l - 1 but
     leaves only theta <= 0.00285, against 008's FLOAT theta 0.0114. At d = 12 (theory audit 129, CONFIRMED by numerical audit 133 to
     numerical audit 135): candidate 007 0.70464, candidate 005 1.33242, baseline d2 0.68631, so the rate-two theta allowances are 0.10568
     (007) and 0.12401 (d2), and 005 has none (AUDITED arithmetic with closure review 016, theory audit 161); these are allowances, not
     theta certificates. A signed version (theory audit 133) bounds the
     quadratic form instead of the norm. With the union lemma for overlapping compressions (theory audit 138), the d = 32 radial and 80 angular tests give 0.79218 (theory audit 141, CONFIRMED by numerical audit 125), and the 32-test signed
     compression gives 0.78617627, leaving theta <= 0.02414 for rate 2 (theory audit 143; the matrix inequality qG - B > 0 and
     the combined bound are CONFIRMED by numerical audit 126 and numerical audit 127 as finite computations); 008's FLOAT theta is below
     this budget, but 008 is already excluded by its point value. The theory team closure review 016 CONFIRMS the theorems theory audit 128, theory audit 130,
     theory audit 133 (with its outward LDL criterion) and theory audit 138, so they are AUDITED, and their use in place of kappa_HS in
     (B-L2) (theory audit 128 (2)) is AUDITED conditional on a full-plane theta bound and the completeness and Lipschitz bounds
     of the velocity field. The theory auditor accepts the review and the 008 arithmetic (theory audit 151, theory audit 152), so the 008 signed
     quadratic-form bound 0.78617627 is AUDITED; a rate from it needs a full-plane theta bound below 0.02414294, no
     theta cover exists for 008, and no row of the matrix changes status.
   - All three archived refits violate the derivative cap (W3) of Theorem D_w (CONFIRMED by the numerical auditor).
5. Residual norm in the theory space.
   - State 131: infinite in every unweighted space. Its weighted norm of theory audit 022 is ||w_R F||_2 >= 2.596e10 at
     R = 2^29 (CONFIRMED: numerical audit 038 with theory audit 032). With the weight (1 + r^2)^(-a/2) its residual is finite exactly for
     a > 2/c_l = 1.10479, with ||(1+r^2)^(-a/2) F||_2 = 0.16931885 at a = 6/5 and 0.00738180 at a = 3/2 (theory audit 089,
     CONFIRMED by numerical audit 087). No weighted framework with a threshold exists, so these numbers decide nothing yet.
   - d2: N_s(F) >= 2557.67, X_s(F) >= 2557.67 and, with the sharpw weights, X_(s,w)(F) >= 5111.94, from the
     elementary bound with CONFIRMED components. Also ||F||_H = 390.2168 (numerical audit 020, CONFIRMED by the norm-certification team's independent
     Galerkin enclosure [390.2168349091, 390.2168349356]); with it N_s(F) >= 194183.55 at s = 2^-13 and >= 194891.68
     at s = 2^-16 (the norm-certification team assembly of CONFIRMED components with the A2 conversion). The ratio to the threshold is
     2.43e7 for weighted sharp L2 framework, 3.36e7 for sharp L2 framework and 4.2e8 for L2 framework (no H), and with H
     1.83e9 for sharp Sobolev framework, 2.12e10 for rebalanced Sobolev framework and 3.06e11 for Analysis II D(b) framework (2.4e7, 2.8e8 and 4.0e9
     from G0 and G1 alone).
   - candidate 005 (FLOAT only): the elementary bound with the numerics team's values is about 1272 for w = (2^14, 2^18) and 2126 for
     the sharpw weights, ratios about 1.7e7 (sharp L2 framework) and 1.0e7 (weighted sharp L2 framework); in G0 alone 7.6e6.
   - candidate 007 (certified with all complete components, the norm-certification team, CONFIRMED by numerical audit 180 and theory audit 238): ratios above
     3596535.57 (weighted sharp L2 framework), 6782715.38 (sharp L2 framework), 64965504.96 (transient-low L2 framework at
     s = 2^-17), 4471313.27 and 7097468 (variable-margin L2 framework at beta_L = 7/5 and 1). From the CONFIRMED G0 and G1 alone
     (numerical audit 139, numerical audit 153) the elementary bound exceeds 480.60 for
     w = (2^14, 2^18) and 732.35 for the sharpw weights, ratios above 6.30e6 (sharp L2 framework), 3.48e6
     (weighted sharp L2 framework), 7.87e7 (L2 framework) and 4.54e6 (sharp Sobolev framework, from G0 and G1 alone); with the norm-certification team's
     complete components and directed rounding (05:52Z; its Hdot^-1 enclosure [0.6355243760, 0.6355322686]
     contains the numerical auditor's value numerical audit 156 and is CONFIRMED by the numerical auditor's independent Green-formula path, numerical audit 249), E2 lies in
     [606.8181, 606.8203] and N_s for sharp Sobolev framework exceeds 604.2996, about 5.713e6 times its threshold. The numerical auditor
     CONFIRMS this assembly from the CONFIRMED components (numerical audit 252): strict threshold ratios above 5712796.3
     (sharp Sobolev framework), 66246337.6 (rebal, exact threshold 3/327680), 954318637 (Analysis II D(b) framework) and 1628914871007.2
     (Analysis II D(a) framework). In G0 alone 1.83e6.
   - candidate 008 (FLOAT only): elementary bound about 904 and 1642, ratios about 1.2e7 (sharp) and 7.9e6 (sharpw); the
     E2 proxy 21523 is about 2.0e8 times the sharp Sobolev framework threshold; in G0 alone 6.9e6.
   - candidate 009 (FLOAT only): elementary bound about 621 and 1184, ratios about 8.2e6 (sharp), 5.6e6 (sharpw) and
     1.0e8 (L2 framework); E2 with H is 3554.8, about 3.4e7 times the sharp Sobolev framework threshold; in G0 alone 5.3e6.
   - candidate 010 (FLOAT only): elementary bound about 774 and 1244, ratios about 1.0e7 (sharp), 5.9e6 (sharpw) and
     1.2e8 (L2 framework); E2 with H is 1.384e4, about 1.3e8 times the sharp Sobolev framework threshold; in G0 alone 3.9e6.
   - candidate 012 (FLOAT only): elementary bound about 1833 and 2827, ratios about 2.4e7 (sharp), 1.3e7 (sharpw) and
     3.0e8 (L2 framework); E2 2493 is about 2.4e7 times the sharp Sobolev framework threshold; in G0 alone 7.6e6.
   - candidate 013 (FLOAT only): elementary bound about 480 and 730, ratio about 3.5e6 (sharpw); within 1 to 4 percent
     of 007's FLOAT values except the first-mode pairings.
   - candidate 014 (FLOAT only): elementary bound about 480 and 730, ratio about 3.5e6 (sharpw); E2 605.2, X3 516.5.
   - candidate 015 (FLOAT only): E2 proxy 604.6, X3 proxy 515.8; ratios as for 014.
   - Certified components beyond d2 so far: for candidate 005 the whole-plane G0 = 1.5630624464
     (numerical audit 104), ||rF||_2 = 266.6711896 (numerical audit 112) and ||F||_H = 42.2834585352 (numerical audit 117), Arb, each OPEN pending peer; for candidate 007
     the norm-certification team's G0 = 0.3766893247 (CONFIRMED by numerical audit 139) and ||rF||_2 = 7.8281155857, G1 = 3.4391037868, P2 = 190.8266911
     (CONFIRMED by numerical audit 153), which with Q3 (CONFIRMED by numerical audit 166 and theory audit 207) give the certified ratio above 3596535.57 of the Q3 answer
     (numerical audit 180, theory audit 238).
6. Does the fixed point close? No, for every pair in the matrix.
   - The first failing inequality is residual smallness. For state 131, candidate 001 and (for N_s) candidate 004 it is
     membership in the forcing space.
   - Independently, the AUDITED necessary point test (theory audit 007, theory audit 017) with CONFIRMED point values shows the
     following. d2, Mpen2 and b6 have no exact solution in any ball with positive baseline gap. candidate 002,
     candidate 003 and candidate 004 have no exact solution in the specified framework balls. Mpen2 and b6 have none in the
     two linear-estimate result 3 balls either (CONFIRMED gaps, numerical audit 054), nor do candidate 002 to 004 (gaps 4.33 to 465.81, theory audit 055 with
     numerical audit 071). b6 and Mpen2 have none in the sharp Sobolev framework ball (gaps > 2.9392836 and > 0.0330957, numerical audit 047
     CONFIRMED by theory audit 069). b6 has none in the theory audit 051 ball at any of the seven theory audit 067 parameter pairs (gap >
     2.9392836795, numerical audit 083 CONFIRMED by theory audit 090).
   - candidate 005 has no exact solution at its c in any ball or graded box of the matrix (point gaps 1.4047 to 1.4094
     and L^2 distance > 0.01625064, numerical audit 076 CONFIRMED by theory audit 082).
   - candidate 006 has no exact solution at its c in any ball or graded box of the matrix (point gaps 6.3372 to 6.3528
     and L^2 distance > 0.52622436, numerical audit 081 CONFIRMED by theory audit 086). Every campaign snapshot through candidate 006 is
     therefore RULED OUT in every registered framework: candidate 001 by membership, the others by CONFIRMED fixed-c
     exclusions.
   - candidate 007 (rows 56, 57): its point value gives positive gaps for the Analysis II D(b) framework, rebal, sharp, L2 framework and
     graded (ii) balls (numerical audit 091, CONFIRMED by theory audit 108), and its fixed-c L^2 distance exceeds 0.004769166867 (n = 7
     angular probe theory audit 185, AUDITED through closure review 022 and theory audit 190, CONFIRMED by numerical audit 157 and theory audit 196; earlier probes gave
     3.1474108e-4, theory audit 182 with numerical audit 152, and 4.3987e-5, numerical audit 091 with theory audit 110). So
     it has no exact solution at its c in any scalar ball (L^2 radius below 3.7930e-6 at the registered fixed weights,
     theory audit 471). The graded and gradedL2 boxes
     allow ||h||_2 up to 1/2000, but the numerical auditor's one-point bound, uniform over every original graded and gradedL2 box for
     all allowed s and radii (gap > 0.0707, numerical audit 102, CONFIRMED by theory audit 122), excludes them as well. The distance
     0.004769166867 is also 10.4 times the graded budget 4.5717e-4, so the graded boxes exclude 007 by distance as
     well. So 007 has no exact solution at its c in any ball of the matrix. Nor at any
     other c: theory audit 189 (AUDITED through closure review 023, the linear-estimates reviewer's review and theory audit 200; theory audit 201) pins the similarity exponent of every
     weighted L^2 correction of a reference with a nonzero leading r^gamma profile, and 007 has such a profile
     (theory audit 203, CONFIRMED by the numerical auditor's independent summation numerical audit 165: first sine coefficient between 18 and 19), so every
     exact solution with a correction in a ball of the matrix has c = c_l. This holds in 007's own affine chart; it
     does not exclude solutions with another leading tail. Smallness fails by more than 3596535.57 (certified,
     numerical audit 180 with theory audit 238).
   - candidate 008 (rows 60, 61): its CONFIRMED point value F(1/10, 73/100) = -0.1061606 (numerical audit 106 with theory audit 125) gives
     positive gaps in the stated balls of every framework of the matrix (sharp 0.0934, sharpw 0.0863) and a uniform
     gap 0.0858 over every original graded and gradedL2 box, so it has no exact solution at its c in any of them. The
     re-optimized theory audit 067 balls of the theory audit 051 framework (R = 21/100000) and the variable-margin L2 framework instances are outside
     the recorded point set, but its CONFIRMED fixed-c L^2 distance > 0.001938714194 (frozen degree-7 probe of 007,
     numerical audit 176, reproduced by the theory auditor in theory audit 225; 4.24 times the graded budget and 511 times the largest scalar budget)
     excludes those balls and every graded box as well. The norm-certification team's exact first-sine probes give the stronger CONFIRMED
     distances > 0.0040334973 (K = 512) and > 0.0363233974 (K = 2048; the norm-certification team 05:52Z, reproduced independently by
     the numerical auditor in numerical audit 238), the second 79.4 times the graded budget. Every candidate snapshot through candidate 008 is therefore RULED
     OUT in every specified ball.
   - candidate 009 (rows 62, 63): the same test (numerical audit 115, CONFIRMED by theory audit 144; gaps sharp 0.0480, sharpw 0.0408,
     uniform graded 0.0404) gives no exact solution at its c in the same balls as 008. The statL and bL balls
     are outside its point set, but its CONFIRMED fixed-c L^2 distance > 0.016967603955 (frozen degree-7 probe of
     007, numerical audit 179, reproduced by the theory auditor in theory audit 231; 37.11 times the graded budget) excludes those balls and every graded
     box as well. Every candidate snapshot through candidate 009 is therefore RULED OUT in every specified ball.
   - candidate 010 (rows 65, 66): the same test (numerical audit 123, CONFIRMED by theory audit 155 and numerical audit 136) gives F(1/10, 73/100)
     = -0.1176966, sharp gap 0.1049, sharpw gap 0.0977 and uniform graded gap 0.0973, so 010 has no exact solution at
     its c in the stated balls of every framework and in every graded box. Its statL and bL balls are outside the
     point set; its frozen mode 7 fixed-c L^2 distance > 0.022479506978 (numerical audit 205, CONFIRMED by the theory auditor's independent
     scaled-polar reconstruction, theory audit 270; scaled field engine numerical audit 191 CONFIRMED by theory audit 267 and numerical audit 210; 49.17 times the
     graded budget) excludes them as well. The weaker mode 1 value > 0.00062746942 (numerical audit 207) is CONFIRMED by theory audit 274.
   - candidate 012 (rows 67, 68; controlled comparison): structure CONFIRMED (numerical audit 155); its point value
     F(1/10, 73/100) = 0.0392951615 (numerical audit 155, CONFIRMED by theory audit 204 and numerical audit 167) gives positive gaps in the stated balls
     and a uniform graded gap 0.0190, so it has no exact solution at its c in the same balls as 008; its CONFIRMED
     fixed-c L^2 distance > 0.018641021006 (numerical audit 182, reproduced by the theory auditor in theory audit 236; 40.77 times the graded budget)
     excludes the statL and bL balls as well.
   - candidate 013 (rows 71, 72; pairing-row experiment): source, sectors, origin identities and the state 131 leading
     density CONFIRMED (numerical audit 197); point value F(1/10, 73/100) = 0.0908758993, sharp gap 0.07805, sharpw gap 0.07088 and
     uniform graded gap 0.07047 (numerical audit 201, CONFIRMED by the theory auditor's independent raw-to-polar path, theory audit 266), so it has no
     exact solution at its c in the same balls as 008; its CONFIRMED fixed-c L^2 distance > 0.00199234339 (held-out
     probe n = 21, K = 522; theory audit 255, CONFIRMED by numerical audit 204 and theory audit 264; 4.357 times the graded budget) excludes the statL
     and bL balls and every graded box as well. The frozen 007 probes give only 0.000056754744 (mode 7) and
     0.000006590501 (mode 1) for 013 (theory audit 253, OPEN); lower bounds do not order the distances of 007 and 013 (theory audit 219).
     Every candidate snapshot through candidate 010, candidate 012 and candidate 013 is therefore RULED OUT in every specified
     scalar ball and graded box (for 010 the statL and bL balls by its CONFIRMED distance, numerical audit 205 with theory audit 270).
     candidate 014 (rows 75, 76; pairing-row experiment, not a certification target; structure CONFIRMED by numerical audit 212,
     point gaps numerical audit 213 CONFIRMED by theory audit 279, distance numerical audit 214 CONFIRMED by theory audit 280) is RULED OUT in every specified
     scalar ball and graded box. So is candidate 015 (rows 77, 78; conditioning control; structure CONFIRMED by
     numerical audit 233, point gaps numerical audit 234 CONFIRMED by theory audit 299, held-out distances CONFIRMED by theory audit 298 with numerical audit 235 and by
     theory audit 304 with numerical audit 237). candidate 016 (rows 80, 81; design test, snapshot 06:46:04Z; point gaps numerical audit 242 CONFIRMED by
     theory audit 307 and numerical audit 251; distance numerical audit 246 CONFIRMED by theory audit 310) is RULED OUT in every specified scalar ball and graded
     box, and so is candidate 017 (rows 82, 83; scale comparison, snapshot 07:11:15Z; point gaps numerical audit 254 CONFIRMED by
     theory audit 319; distance numerical audit 256 CONFIRMED by theory audit 320). candidate 018 (rows 84, 85; continuation of 016, snapshot 08:02:27Z;
     not a certification target; point gaps numerical audit 270 CONFIRMED by theory audit 342; distance numerical audit 272 CONFIRMED by theory audit 345) is
     RULED OUT in every specified scalar ball and graded box. candidate 019 (rows 86, 87; continuation of 017, snapshot
     08:28:42Z; trial comparison, not a certification target; point gaps numerical audit 279 CONFIRMED by theory audit 353 to theory audit 355;
     distance numerical audit 282 CONFIRMED by theory audit 357) is RULED OUT in every specified scalar ball and graded box. candidate 020
     (rows 88, 89; two-scale trial comparison, snapshot 08:46:18Z; point gaps numerical audit 291 CONFIRMED by theory audit 360 to
     theory audit 362; distance numerical audit 293 CONFIRMED by theory audit 363) is RULED OUT in every specified scalar ball and graded box. candidate 011 (rows 69, 70; controlled comparison; FLOAT values only;
     not a certification target) is OPEN.
   - The c pinning covers the whole family: state 131, d2 and candidate 005 to candidate 012 share 007's entire nonzero
     leading density profile (theory audit 210, CONFIRMED by the numerical auditor's independent evaluation numerical audit 172, accepted in theory audit 213), and
     so does candidate 013 (numerical audit 197, CONFIRMED; used in theory audit 264). So
     every "no exact solution at its c" statement above for d2, 005, 006, 008, 009, 010, 012 and 013 holds at every c in
     the same chart. Mpen2, b6 and 001 to 004 are not covered, and failed smallness hypotheses are not affected.
   - "Every specified ball" above means the balls of the scalar and graded frameworks. The dyadic scheme
     dyadic Y framework is tested only for state 131, d2, 007, 008, 009, 010, 015, 016 and 017 (rows 58, 59, 64, 73, 74,
     79, 98, 105, 106; the theory auditor theory audit 219), each under the premises of its row (017 by the numerical auditor's numerical audit 389, CONFIRMED by the theory auditor in
     theory audit 463). For 008, 009 and 010
     the seven-cell origin-inverse test fails on every cell, minimum ratios above 4.64864536 (numerical audit 186, reproduced by
     the theory auditor in theory audit 248), above 1.02032822 (numerical audit 187, reproduced in theory audit 250) and above 5.78998557 (numerical audit 231, reproduced by
     the theory auditor's independent exact path in theory audit 303; the cells cover 0 < a < 1 + 1/c and the audited nonpositive far-field
     rate covers 1 + 1/c <= a < 2), so the scheme is RULED OUT for all three. For 016 the norm-certification team's modes 1 and 3
     projections fail all seven cells (minimum ratio above 1.253908386497 on [0, 1/4]); the numerical auditor reproduces the two norms
     J(1/4) and J(7/4) it needs independently (numerical audit 355), and for 1 + 1/c <= a < 2 the low rate is not positive, so the
     scheme is RULED OUT for 016 as well (row 98). The 016 origin hypotheses are the numerical auditor's exact computation (numerical audit 242);
     the theory auditor has not replayed the 016 origin. For 015 the numerical auditor's own complete modes 1 and 3 projections, from an
     integration that does not use the norm-certification team's deleted F cache, fail all seven cells (minimum strict ratio floor
     621461129537/500000000000 = 1.242922259074; numerical audit 382, 14:11:34Z, proof d7b34632..., result record 02 in the accompanying artifacts 24bdc65d...);
     the norm-certification team's fourteen mode energies agree, and numerical audit 382 verifies the origin conditions of the scheme exactly, so the
     scheme is RULED OUT for 015 under the same premises (row 105); the theory auditor reproduces it independently (theory audit 461, 739
     checks). This excludes one sufficient scheme, not a profile, and implies no scalar-distance statement. For 017
     the numerical auditor's own complete modes 1 and 3 projections (numerical audit 389, 14:56Z, proof 55765490..., result 3478699c...) fail all
     seven cells on a two-evaluation cover, J(1/4) on [0, 1/4] and J(7/4) on the six other cells, with minimum strict
     ratio floor 1221854480167/1000000000000 = 1.221854480167 on [1/4, 1/2]; strain 1 - c and a0 > 5c - 4 are
     recomputed exactly, both of the norm-certification team's squared-norm displays contain the numerical auditor's values, and the norm-certification team's first-cell ratio
     1.24497 agrees, while the norm-certification team's minimum 1.244974 from all seven endpoint norms is not reproduced. The scheme is
     RULED OUT for 017 under the same premises (row 106); the theory auditor reproduces it independently (theory audit 463, 1070 checks at
     1024 bits).
   - The weak necessary test (Proposition W, AUDITED theory audit 042) goes further for d2. A fixed-c correction within the
     gradient cap of any of the five balls of Analysis II D(b) framework, sharp Sobolev framework, L2 framework and the two linear-estimate result 3 boxes
     needs ||h||_2 >= 2.7e-3, at least 1600 times what those balls allow (numerical audit 053, CONFIRMED by theory audit 044).
   - Without any gradient cap: no exact solution d2 + h at d2's c, with h a distributional divergence-form
     correction, has ||h||_2 <= 0.29552, and no exact solution Mpen2 + h has ||h||_2 <= 0.55006 (radially localized
     weak probes, numerical audit 065, CONFIRMED by theory audit 064; the single probe of numerical audit 057 with theory audit 048 and numerical audit 061 gives 0.0029919 for
     d2; decimal lower bounds are rounded down). Every scalar ball of the matrix allows ||h||_2 < 3.7930e-6 at the
     registered fixed weights (theory audit 471, which REFUTES the older cap 2.7e-6 as an implication of the high-margin
     algebra), so d2 and Mpen2 have no exact solution in any of them. These are distance bounds at fixed c (for d2 at
     every c in its
     chart, by the pinning below), not nonexistence of a profile.
   - Graded boxes: a positive graded or gradedL2 top-row budget forces ||h||_(H^(2+s)) < 50/(651 sqrt(28248)) < 1/2000
     (the linear-estimates reviewer Proposition G, CONFIRMED by theory audit 070). With the distances above, d2 and Mpen2 have no exact solution in any
     such box; Mpen2 and b6 are also excluded by the uniform graded point test (theory audit 070).
   - For state 131 no exact correction in L^2 exists at any c, with or without a gradient bound, because its
     leading residual sector has exponent 0.1048 >= -1 (numerical audit 055 with theory audit 049; without the gradient bound theory audit 049 with
     numerical audit 062; CONFIRMED). Non-L^2 and weighted correction classes are not excluded. In the weighted dyadic scheme of
     theory audit 058 (AUDITED conditional) no closure is possible for state 131 at any a, s and Rw (theory audit 097 AUDITED, theory audit 114,
     row 58), nor for d2 at any 0 < a < 2 (row 59) or candidate 007 at any 0 < a < 2 (row 64; 0 < a < 4/5 through the
     origin ceiling, theory audit 146, theory audit 147, closure review 017); other high spaces are not excluded.
7. Smallest remaining obstacle: the residual of the reference profile, by a factor above 3596535.57 with certified
   numbers (candidate 007 against weighted sharp L2 framework, all complete components, numerical audit 180 with theory audit 238; d2: 2.43e7), and about 1e7 by the numerics team's FLOAT values for candidate 005 (which fails (B-L2)
   through kappa, numerical audit 077, CONFIRMED by theory audit 083). candidate 007 lowers the gap to more than 3596535.57 (certified) against
   weighted sharp L2 framework, and (B-L2) holds for it (numerical audit 111, CONFIRMED by theory audit 162; rows 56,
   57); its CONFIRMED fixed-c L^2 distance
   0.004769166867 (1257 times the largest scalar budget, 10.4 times the graded budget) excludes it from every scalar
   ball and graded box. In the unregularized comparison energy E_star^2=P2^2+2^14 G1^2+2^18 G0^2, the weighted G1 term
   contributes about 72 percent, and the G0 and P2 terms about 14 percent each (numerical audit 180, corrected by numerical audit 438 and
   independently accepted in theory audit 509); in N_s frameworks H also
   enters.
   - theory exchange 02 states the obstruction as the fixed-c L^2 distance of the candidates, not the linear constants
     (L2 distance condition, budget formula AUDITED by theory audit 065). For a ball family {X(h) <= r} with X(h) >= sqrt(W2) ||h||_2
     and rate mu0 - C s - c_U r/sqrt(s), every correction allowed for any s has ||h||_2 at most
     b_fam = (2 mu0/3) sqrt(mu0/(3C))/(c_U sqrt(W2)): 3.7930e-6 for sharp Sobolev framework, 2.8496e-6 for
     weighted sharp L2 framework, at most 3.8e-6 for every registered scalar family and 4.5717e-4 for the graded boxes. The
     CONFIRMED distances exceed these budgets by 7.791e4 (d2) and 1257 (candidate 007, 0.004769166867, which is 10.4 times
     the graded budget) against sharp Sobolev framework, so
     these references are excluded from every ball of these families for every s and forcing bound. A reference
     with a much smaller fixed-c distance is needed, not only better constants.
   - For d2, G0 is a near- and mid-field quantity: only 1.23e-4 of G0^2 lies beyond r = 1e4 (numerical audit 037, originating with the numerical auditor).
     Meanwhile 99.98 percent of E_2(F)^2 sits in the H component. That is a numerical observation for d2; theory audit 040
     notes that H dominance is not a general property of residuals.
   - On the theory side, the sharp no-H theorems (linear-estimate result 3, AUDITED theory audit 042) raise the X threshold 12.5 and 34.5 times
     over L2 framework, but their G0 requirement (2.0542e-7) equals that of sharp Sobolev framework to within 1 percent. The
     gap in G0 is 2.4e7. That no other inverse estimate can supply the missing factor is a planning judgment about the
     estimates explored so far, not a theorem (theory audit 040, theory audit 042). A stationary L^2 inverse (Woodbury, TM-17b) cannot
     directly replace (B-L2) in the theory audit 019 proof (theory audit 050); theory audit 051 (AUDITED, theory audit 057) replaces it by a semigroup bound
     instead, with a smaller threshold, and TP-1 (theory audit 059) by the stationary bound (L0).
8. Priority for the next campaign (ranking revised at H8, see short answer 8; the items below are the supporting
   work list):
   - (i) Exact PRIMARY-chart families with 8 to 12 stationary branches. All X_s-forbidden sectors, the descendant
     sectors and the interaction sectors h = N + 2, ..., 2N + 1 (theory audit 036) are cancelled exactly. The whole residual
     must reach G0 = ||F||_2 <= 2.05e-7 (weighted sharp L2 framework) with P2 and G1 inside the same box, the inner region
     included, and theta <= c_l - 1 - kappa must be built into the design.
   - (ii) A localized form of (B-L2), and a certified (B-L2) for each new candidate (the d2 cover of numerical audit 051,
     CONFIRMED by theory audit 053, shows that this is feasible). sharp L2 framework and sharpw-v1 are now AUDITED. The
     alternative hypotheses (L) of theory audit 051 and (L0) of TP-1 need low-space resolvent or semigroup certificates that no
     worker has yet; TP-1b reduces (L0) to finite-rank data only under an extra positivity condition (theory audit 059).
     variable-margin L2 framework (theory audit 113) relaxes (B-L2) to c_l + 1 - theta - kappa >= beta_L at a threshold about half that of
     weighted sharp L2 framework for beta_L = 1. The 223-cell theta cover of candidate 007 (numerical audit 111, CONFIRMED by theory audit 162) carries the d2 method
     over to a 2982-generator candidate, and the parity budget (theory audit 128 to theory audit 138, AUDITED through the theory team closure review 016) can lower the kappa
     term inside (B-L2) when a full-plane theta bound is certified.
   - (iii) Use the weak test of Proposition W, its gradient-free and localized forms (numerical audit 057, numerical audit 061, numerical audit 064 to
     numerical audit 066) and the point test as cheap necessary filters before any norm certification.
   - (iv) Certify the separate (B9c) constants U2, R2 and the (B5) constant.
   - (v) Route T-E with weights at R = O(1) instead of 2^29, and the scale-adapted weighted high space of theory audit 058
     (AUDITED conditional, theory audit 095; no concrete high resolvent estimate (H) yet) as a setting for state 131. Energy
     certificates there are capped by TP-3 and TP-4 (CONFIRMED, theory audit 084, theory audit 092) and the closure radius by the linear-estimates reviewer's
     ceiling R < sqrt(8 pi)(1 + c_l - c_l a)/(1 + a) (CONFIRMED, theory audit 096). For state 131 the scheme is RULED OUT
     for every a, s and Rw (theory audit 097 AUDITED through the theory team closure review 013, with theory audit 098 and theory audit 099; theory audit 114), so route T-E for
     state 131 needs a different high space. The same holds for d2 (theory audit 107 AUDITED through the theory team closure review 014; theory audit 120) and for candidate 007
     at every 0 < a < 2 (theory audit 127 with numerical audit 113 and closure review 015 for 4/5 <= a < 2; the origin-ceiling cover theory audit 147 with
     theory audit 145, theory audit 146 AUDITED through the theory team closure review 017 for 0 < a < 4/5). Every d2-warm-start candidate has
     a0 >= 5c_l - 4, so a dyadic route for this family needs Y(F) below the smaller origin ceiling.
   - (vi) theory exchange 02 section 9 asks batch N, in this order, for the weak distance of each new candidate, then point
     tests, then the full N_a cover of 007, then norms. Cheap necessary filters come first.

## Comparison table of theory-numerics pairs

Condensed from the closure matrix in the accompanying artifacts, first at v45 and kept current through v185 (authoritative; it gives
sources, background hypotheses and missing items per row; the coordinator's table check script checks that the
status label and candidate of each row agree with the matrix row of the same number). Ratio = residual lower bound /
threshold, computed from the exact registered threshold before any displayed value is rounded (clarification after
theory audit 479). "No sol. in ball" = the AUDITED necessary point test fails with CONFIRMED numbers. Finite decimal values
shown without an explicit inequality or enclosing interval are rounded summaries of their cited certificates and are
not directed bounds. Ratios use the exact underlying bounds and thresholds (numerical audit 439, theory audit 510).

| # | framework | candidate | in forcing space | residual value or bound | threshold | ratio | status |
|---|---|---|---|---|---|---|---|
| 1 | Analysis II D(b) framework | state 131 | no ((1,0)) | infinite | 6.36e-7 | infinite | RULED OUT (Theorem E) |
| 2 | Analysis II D(b) framework | tail repair R = 2^1024 | yes | 2^1028 | 6.36e-7 | > 2^1048 | RULED OUT |
| 3 | Analysis II D(b) framework | six-branch family, K <= 3675 | yes | H_lb(75) = 2.93e-5 | H <= 1.27e-9 | 22986 at K = 75 | RULED OUT |
| 4 | Analysis II D(b) framework | seven-branch family | yes | none | 6.36e-7 | unknown | OPEN |
| 5 | Analysis II D(b) framework | m10 algebraic repairs | yes, (B1) false | 3.6e6 | 6.36e-7 | > 5.6e12 | RULED OUT |
| 6 | Analysis II Dw1 framework | state 131 | yes | 5.89e24 | 2^-35 | > 2^117 | RULED OUT |
| 7 | Analysis II Dw2 framework | state 131 | yes | 5.89e24 | 2^-30 | > 2^112 | RULED OUT |
| 8 | Analysis II Dw1/2 frameworks | baseline d2 | yes, (W3) false | 5.479 | 2^-30 | > 2^32 | RULED OUT |
| 9 | Analysis II Dw1/2 frameworks | baseline Mpen2 | yes, (W3) false | 12.66 | 2^-30 | > 2^33 | RULED OUT |
| 10 | Analysis II Dw1/2 frameworks | baseline b6 | yes, (W2), (W3) false | 59.586 | 2^-30 | > 2^35 | RULED OUT |
| 11 | Analysis II logarithmic framework | baseline d2 | yes | - | parametric | > 2^243 | RULED OUT |
| 12-14 | every baseline-gap ball | d2, Mpen2, b6 | yes | point gaps 0.0067, 0.064, 2.95 | point test | - | RULED OUT (no sol. in ball) |
| 15 | rebalanced Sobolev framework | state 131 | no | infinite | 9.16e-6 | infinite | RULED OUT |
| 16 | rebalanced Sobolev framework | baseline d2 | yes | 2557.67 | 9.16e-6 | > 2.79e8 | RULED OUT (and no sol. in ball) |
| 17 | rebalanced Sobolev framework | Mpen2, b6 | yes | point gaps | 9.16e-6 | - | RULED OUT (no sol. in ball) |
| 18 | rebalanced Sobolev framework | six-branch family | yes | H_lb(75) = 2.93e-5 | H <= 1.83e-8 | 1596 at K = 75 | RULED OUT K <= 1315 (theory audit 040); OPEN above |
| 19 | rebalanced Sobolev framework | seven-branch family | yes | none | 9.16e-6 | unknown | OPEN |
| 20 | graded Sobolev framework, boxes (i), (ii) | baseline d2 | yes | G0 = 4.99 | G0 <= 3.45e-8 | > 1.4e8 | RULED OUT |
| 21 | graded Sobolev framework, every box | Mpen2, b6 | yes | uniform point gaps 0.0305, 2.94; Mpen2 L^2 distance 0.55006 | box | - | RULED OUT (no sol. in any box with positive budget; theory audit 070) |
| 22 | graded Sobolev framework, every box | baseline d2 | yes | L^2 distance 0.29552 (CONFIRMED) | box | - | RULED OUT (no sol. in any box with positive budget; Proposition G, theory audit 070) |
| 23 | sharp Sobolev framework | state 131 | no | infinite | 1.06e-4 | infinite | RULED OUT |
| 24 | sharp Sobolev framework | baseline d2 | yes | 2557.67; 194183 with H (CONFIRMED) | 1.06e-4 | > 1.83e9 (> 2.4e7 without H) | RULED OUT (smallness; point test inconclusive; weak probe and L^2 distance exclude, CONFIRMED) |
| 25 | sharp Sobolev framework | Mpen2, b6 | yes | Mpen2 4321.48; point gaps 0.0330, 2.93 (CONFIRMED, theory audit 069) | 1.0578e-4 | > 4.08e7 (Mpen2) | RULED OUT (Mpen2 smallness; both no sol. in ball) |
| 26 | sharp Sobolev framework | six-branch family | yes | H_lb(75) = 2.93e-5 | H <= 2.13e-7 | 137.6 at K = 75 | RULED OUT K <= 511 (theory audit 040); OPEN above |
| 27 | sharp Sobolev framework | seven-branch family | yes | none (candidate 002 gap 465.79, CONFIRMED) | 1.06e-4 | unknown | OPEN |
| 28 | L2 framework | state 131 | no | infinite | 6.10e-6 | infinite | RULED OUT (no L^2 correction at any c, numerical audit 055) |
| 29 | L2 framework | baseline d2 | yes, (B-L2) holds (CONFIRMED) | 2557.67 | 6.10e-6 | > 4.19e8 | RULED OUT (and no sol. in ball; L^2 distance) |
| 30 | L2 framework | baseline Mpen2 | yes | point gap 0.063; 4321.48 | 6.10e-6 | > 7.08e8 | RULED OUT (no sol. in ball) |
| 31 | L2 framework | baseline b6 | yes, (B-L2) false | - | 6.10e-6 | - | RULED OUT |
| 32 | L2 framework | four-branch family, K <= 25929 | yes | family floor | 6.10e-6 | 64637 at K = 75 | RULED OUT |
| 33 | L2 framework | five or more branches | yes | floor negligible | 6.10e-6 | unknown | OPEN (most promising) |
| 34 | theory audit 022 weighted L^2 (AUDITED, low space only) | state 131 | yes | 2.596e10 | none | - | OPEN (route only; its registered high space is RULED OUT, row 58) |
| 35 | every unweighted framework | candidate 001 | no | infinite | - | infinite | RULED OUT (residual not in the forcing space, so the frameworks do not apply; that no L^2 solution lies in a ball is theory audit 458's application of theory audit 049, AUDITED in the affine class rho + L^2 at every real c: reviews closure review 046 and the review of theory audit 458, accepted by the theory auditor in theory audit 465; theory audit 459) |
| 36 | Db, rebal, sharp, L2 framework, graded (ii) balls | candidate 002 | yes | F(3/7, 3/16) = -465.88 | point test | about 1e10 (FLOAT) | RULED OUT (no sol. in ball) |
| 37 | graded L2 framework (AUDITED) | baseline d2 | yes | G0 = 4.99 | G0 <= 3.48e-8 | > 1.43e8 | RULED OUT (smallness; no sol. in any gradedL2 box, theory audit 070) |
| 38 | graded L2 framework (AUDITED) | baseline Mpen2 | yes | G0 = 8.42 | G0 <= 3.48e-8 | > 2.42e8 | RULED OUT (smallness; no sol. in any gradedL2 box, theory audit 070) |
| 39 | graded L2 framework (AUDITED) | baseline b6 | yes, (B-L2) false | - | - | - | RULED OUT |
| 40 | Db, rebal, sharp, L2 framework, graded (ii) balls | candidate 003 | yes | F(3/7, 15/32) = 95.72 | point test | 5.3e9 in G0 (FLOAT) | RULED OUT (no sol. in ball) |
| 41 | every N_s framework | candidate 004 | no (H infinite) | infinite | - | infinite | RULED OUT |
| 42 | L2 framework | candidate 004 | yes | point gap 4.354 (CONFIRMED, theory audit 038) | 6.10e-6 | about 2e10 (FLOAT) | RULED OUT (no sol. in ball) |
| 43 | graded Sobolev framework, boxes (i), (ii) | six-branch family | yes | H_lb(K) | phi_H of the box | above 1 up to the cutoff | RULED OUT K <= 1021 (i), K <= 1063 (ii) (theory audit 040); OPEN above |
| 44 | sharp L2, weighted sharp L2 | state 131 | no | infinite | 7.62e-5, 2.10e-4 | infinite | RULED OUT (no L^2 correction at any c, numerical audit 055) |
| 45 | sharp L2 framework | baseline d2 | yes, (B-L2) holds (CONFIRMED) | 2557.67 | 7.62e-5 | > 3.35e7 | RULED OUT (smallness; weak probe and L^2 distance exclude, CONFIRMED) |
| 46 | weighted sharp L2 framework | baseline d2 | yes, (B-L2) holds (CONFIRMED) | 5111.94 | 2.10e-4 | > 2.43e7 | RULED OUT (smallness; weak probe and L^2 distance exclude, CONFIRMED) |
| 47 | sharp L2, weighted sharp L2 | baseline Mpen2 | yes | point gaps 0.0496, 0.0366 | 7.62e-5, 2.10e-4 | > 4.10e7 | RULED OUT (smallness; no sol. in ball) |
| 48 | sharp L2, weighted sharp L2 | baseline b6 | yes, (B-L2) false | point gaps 2.946, 2.939 | 7.62e-5, 2.10e-4 | - | RULED OUT |
| 49 | sharp L2, weighted sharp L2 | four-branch family | yes | family floor | 7.62e-5, 2.10e-4 | above 1 up to K = 6886, 5814 | RULED OUT up to the cutoffs (CONFIRMED cross-worker); OPEN above |
| 50 | sharp L2, weighted sharp L2 | five or more branches; candidate 002 to 004 | yes | snapshots: point gaps 4.33 to 465.81 (CONFIRMED, numerical audit 071); L^2 distances 1.5636, 0.2298, 1.4000 (CONFIRMED, theory audit 068) | 7.62e-5, 2.10e-4 | about 1e9 (snapshots, FLOAT) | OPEN (families, most promising with row 33); snapshots RULED OUT (no sol. in ball) |
| 51 | transient-low L2 / statL (theory audit 051, AUDITED cond.) | d2, Mpen2, b6 | yes; (L) unchecked | d2 2557.67, Mpen2 4321.48; point gaps 0.0065, 0.063, 2.95 | 5.09e-6 stated; 1.53e-5 (K_L = 2), 2.42e-5 (K_L = 1), theory audit 067 | > 5.03e8 (d2) stated; > 1.66e8 (d2), > 2.81e8 (Mpen2) at 1.53e-5 | RULED OUT (no sol. in ball) in the stated version and at all seven theory audit 067 parameter pairs (b6: numerical audit 083, CONFIRMED by theory audit 090) |
| 52 | transient-low L2 / statL (theory audit 051, AUDITED cond.) | four-branch family; five or more branches | yes; (L) unchecked | family floor | 5.09e-6 stated; up to 3.03e-5 (theory audit 067) | above 1 for K <= 25929 (stated version) | RULED OUT K <= 25929 (stated version only); OPEN otherwise |
| 53 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 005 (d2 + branches 6, 7) | yes (numerical audit 075, CONFIRMED); (B-L2) fails: kappa 1.35808 (numerical audit 077, CONFIRMED by theory audit 083) | FLOAT G0 1.563, X3 proxy 1328; F(0, 1/4) = -1.4097 and L^2 distance > 0.01625 (CONFIRMED, theory audit 082) | 6.10e-6 to 2.10e-4 | about 1.0e7 (sharpw, FLOAT) | RULED OUT (no sol. in ball; kappa also fails, CONFIRMED) |
| 54 | Db, rebal, sharp, graded | candidate 005 | yes (numerical audit 075, CONFIRMED) | FLOAT H 42.3, G0 1.563; point gaps 1.405 to 1.409 (CONFIRMED, theory audit 082) | 6.36e-7 to 1.06e-4 | about 1.2e7 (sharp, FLOAT) | RULED OUT (no sol. in ball) |
| 55 | every registered framework | candidate 006 (state-131 eight-branch, E2 objective) | yes (numerical audit 080, CONFIRMED); (B-L2) fails: theta_X 6.4323 > c_l - 1 at (3/7, 1/4) (numerical audit 082, CONFIRMED by theory audit 087) | FLOAT G0 17.85, H 10.1; F(3/7, 1/4) = 6.3536, L^2 distance > 0.526 (numerical audit 081, CONFIRMED by theory audit 086) | 6.36e-7 to 2.10e-4 | about 1.7e8 (sharpw, FLOAT) | RULED OUT (no sol. in ball or graded box) |
| 56 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 007 (d2 + branches 6, 7, balanced objective) | yes (numerical audit 090, CONFIRMED); (B-L2) holds: kappa 0.72816 (numerical audit 092, CONFIRMED by theory audit 111), theta <= 2/25 by a 223-cell cover (numerical audit 111, CONFIRMED by theory audit 162) | FLOAT G0 0.3767 (whole-plane 0.37669 by the norm-certification team, CONFIRMED by numerical audit 139), X3 proxy 517.1; F(1/10, 73/100) = 0.09114 and L^2 distance > 0.004769166867 (theory audit 185, AUDITED, CONFIRMED by numerical audit 157); G1 3.43910 certified (numerical audit 153) | 6.10e-6 to 2.10e-4 | > 3596535.57 (sharpw, certified, numerical audit 180 with theory audit 238) | RULED OUT (no sol. at any c in any ball; c pinned by theory audit 189 with numerical audit 165) |
| 57 | Db, rebal, sharp, graded | candidate 007 | yes (numerical audit 090, CONFIRMED) | H in [0.6355243, 0.6355323] (the norm-certification team, CONFIRMED by numerical audit 249) and E2 in [606.818, 606.821] (the norm-certification team, CONFIRMED by numerical audit 252); point gaps positive incl. sharp 0.0758 and graded (ii) 0.0832 (CONFIRMED, theory audit 108); L^2 distance > 0.004769166867 (CONFIRMED; 10.4 times the graded budget); uniform graded point gap > 0.0707 (numerical audit 102, CONFIRMED by theory audit 122) | 6.36e-7 to 1.06e-4 | about 5.7e6 (sharp, FLOAT); > 4.54e6 certified | RULED OUT (no sol. at any c in any ball or original graded box) |
| 58 | dyadic Y framework (theory audit 058 scheme, AUDITED cond.) | state 131 | only for 2/c_l < a < 1 + 1/c_l | Laplacian tail bound (theory audit 098, CONFIRMED) | ceiling sqrt(8 pi)(1 + c_l - c_l a)^2/(1 + a) (theory audit 097 AUDITED) | squared ratio > 11.2378 (theory audit 099, CONFIRMED) | RULED OUT for every a, s, Rw (theory audit 114; this scheme only) |
| 59 | dyadic Y framework | baseline d2 | not needed | 5^((a-2)/2) J(a), J CONFIRMED (numerical audit 099, theory audit 116); comparison theory audit 107 AUDITED (closure review 014, theory audit 120) | as row 58 | > 1.35446 on seven cells (CONFIRMED, theory audit 116) | RULED OUT for every a, s, Rw (theory audit 120; this scheme only) |
| 60 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 008 (as 007, X3 objective without rF) | yes (numerical audit 105, CONFIRMED); (B-L2) as stated fails: kappa_HS 0.84604 (numerical audit 107, CONFIRMED by theory audit 126) | FLOAT G0 1.423, X3 proxy 941.4; F(1/10, 73/100) = -0.10616 (numerical audit 106, CONFIRMED by theory audit 125); L^2 distance > 0.03632 (first sine, K = 2048; the norm-certification team, CONFIRMED by numerical audit 238) | 6.10e-6 to 2.10e-4 | about 7.9e6 (sharpw, FLOAT) | RULED OUT (no sol. in any ball; statL and bL balls by the CONFIRMED distance > 0.00193, numerical audit 176 with theory audit 225) |
| 61 | Db, rebal, sharp, graded | candidate 008 | yes (numerical audit 105, CONFIRMED) | FLOAT H 43.03, E2 proxy 21523; positive point gaps and uniform graded gap 0.0858 (numerical audit 106, CONFIRMED by theory audit 125) | 6.36e-7 to 1.06e-4 | about 2.0e8 (sharp, FLOAT) | RULED OUT (no sol. in any ball or original graded box) |
| 62 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 009 (from 007, X3 objective without rF, kappa penalty) | yes (numerical audit 114, CONFIRMED); (B-L2) not certified (kappa_HS 0.71321, numerical audit 121, CONFIRMED by theory audit 166; no theta cover) | FLOAT G0 1.096, X3 proxy 631; F(1/10, 73/100) = 0.06079 (numerical audit 115, CONFIRMED by theory audit 144) | 6.10e-6 to 2.10e-4 | about 5.6e6 (sharpw, FLOAT) | RULED OUT (no sol. in any ball; statL and bL balls by the CONFIRMED distance > 0.0169, numerical audit 179 with theory audit 231) |
| 63 | Db, rebal, sharp, graded | candidate 009 | yes (numerical audit 114, CONFIRMED) | FLOAT H 7.001, E2 3554.8; uniform graded gap 0.0404 (numerical audit 115, CONFIRMED by theory audit 144) | 6.36e-7 to 1.06e-4 | about 3.4e7 (sharp, FLOAT) | RULED OUT (no sol. in any ball or original graded box) |
| 64 | dyadic Y framework | candidate 007 | not needed | J(a) from modes 1 and 3 (theory audit 127, CONFIRMED by numerical audit 113; proof reviewed by the theory team closure review 015) | as row 58 | > 1.01380 on four cells covering [4/5, 1 + 1/c_l]; with the origin ceiling of theory audit 146 (AUDITED through closure review 017), > 1.2342 on seven cells covering (0, 1 + 1/c_l) (theory audit 147, arithmetic CONFIRMED by numerical audit 128, numerical audit 129, closure review 017) | RULED OUT for every 0 < a < 2 (this scheme only) |
| 65 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 010 (005 basis plus 960 multi-scale inner functions, X3 objective without rF) | yes (numerical audit 122, CONFIRMED); (B-L2) fails in FLOAT (kappa 0.922) | FLOAT G0 0.8163, X3 proxy 837.2; F(1/10, 73/100) = -0.11770 (numerical audit 123, CONFIRMED by theory audit 155, numerical audit 136) | 6.10e-6 to 2.10e-4 | about 5.9e6 (sharpw, FLOAT) | RULED OUT (no sol. in the stated balls; statL and bL by the distance > 0.0224795, numerical audit 205 with theory audit 270) |
| 66 | Db, rebal, sharp, graded | candidate 010 | yes (numerical audit 122, CONFIRMED) | FLOAT H 27.65, E2 1.384e4; uniform graded gap 0.0973 (numerical audit 123, CONFIRMED by theory audit 155, numerical audit 136) | 6.36e-7 to 1.06e-4 | about 1.3e8 (sharp, FLOAT) | RULED OUT (no sol. in any ball or original graded box) |
| 67 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 012 (controlled comparison from 009, E2 objective plus kappa penalty) | yes (numerical audit 155, CONFIRMED); (B-L2) fails in FLOAT (kappa 0.878) | FLOAT G0 1.556, X3 proxy 2050, weak distance 1.50e-2; F(1/10, 73/100) = 0.03930, point gaps positive (numerical audit 155, CONFIRMED by theory audit 204, numerical audit 167) | 6.10e-6 to 2.10e-4 | about 1.3e7 (sharpw, FLOAT) | RULED OUT (no sol. in any ball; statL and bL balls by the CONFIRMED distance > 0.0186, numerical audit 182 with theory audit 236) |
| 68 | Db, rebal, sharp, graded | candidate 012 | yes (numerical audit 155, CONFIRMED) | FLOAT H 2.84, E2 2493; uniform graded point gap 0.0190 (numerical audit 155, CONFIRMED by theory audit 204, numerical audit 167) | 6.36e-7 to 1.06e-4 | about 2.4e7 (sharp, FLOAT) | RULED OUT (no sol. in any ball or original graded box) |
| 69 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 011 (controlled comparison: 007 plus 960 multi-scale functions, same objective and start) | FLOAT (not CONFIRMED); (B-L2) holds in FLOAT (kappa 0.7277) | FLOAT G0 0.3745, X3 proxy 528, weak distance 5.1e-4; nothing certified | 6.10e-6 to 2.10e-4 | about 3.5e6 (sharpw, FLOAT) | OPEN (not a certification target) |
| 70 | Db, rebal, sharp, graded | candidate 011 | FLOAT (not CONFIRMED) | FLOAT H 0.612, E2 610; nothing certified | 6.36e-7 to 1.06e-4 | about 5.8e6 (sharp, FLOAT) | OPEN (not a certification target) |
| 71 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 013 (pairing-row experiment: 007 plus 27 first-mode penalty rows) | yes (numerical audit 197, CONFIRMED); (B-L2) holds in FLOAT (kappa 0.7270) | FLOAT G0 0.3722; F(1/10, 73/100) = 0.09088, point gaps positive (numerical audit 201, CONFIRMED by theory audit 266); distance > 0.00199234339 (theory audit 255, CONFIRMED by numerical audit 204) | 6.10e-6 to 2.10e-4 | about 3.5e6 (sharpw, FLOAT) | RULED OUT (no sol. in any ball; statL and bL balls by the CONFIRMED distance; not a certification target) |
| 72 | Db, rebal, sharp, graded | candidate 013 | yes (numerical audit 197, CONFIRMED) | FLOAT H 0.631; uniform graded point gap 0.07047 (numerical audit 201, CONFIRMED by theory audit 266); distance 4.357 times the graded budget | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT (no sol. in any ball or original graded box; not a certification target) |
| 73 | dyadic Y framework | candidate 008 | not needed | J(a) from modes 1, 3, 7 (numerical audit 186, CONFIRMED by theory audit 248) | origin ceiling of theory audit 146 | > 4.64864536 on seven cells | RULED OUT for every 0 < a < 2 (this scheme only) |
| 74 | dyadic Y framework | candidate 009 | not needed | J(a) from modes 1, 3, 7 (numerical audit 187, CONFIRMED by theory audit 250) | origin ceiling of theory audit 146 | > 1.02032822 on seven cells | RULED OUT for every 0 < a < 2 (this scheme only) |
| 75 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 014 (pairing-row experiment: 007 plus 27 first-mode and 75 angular penalty rows) | structure CONFIRMED (numerical audit 212); (B-L2) holds in FLOAT (kappa 0.7270) | point gaps positive (numerical audit 213, CONFIRMED by theory audit 279); L^2 distance > 0.001983 (numerical audit 214, CONFIRMED by theory audit 280); FLOAT G0 0.3726, X3 proxy 516.5 | 6.10e-6 to 2.10e-4 | about 3.5e6 (sharpw, FLOAT) | RULED OUT (not a certification target) |
| 76 | Db, rebal, sharp, graded | candidate 014 | structure CONFIRMED (numerical audit 212) | point gaps positive, uniform graded gap 0.07036 (numerical audit 213, CONFIRMED by theory audit 279); L^2 distance > 0.001983 (numerical audit 214, CONFIRMED by theory audit 280); FLOAT H 0.631, E2 605.2 | 6.36e-7 to 1.06e-4 | about 5.7e6 (sharp, FLOAT) | RULED OUT (not a certification target) |
| 77 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 015 (conditioning control: 014's 102 rows on the exact quotient basis of 013) | structure CONFIRMED (numerical audit 233); (B-L2) holds in FLOAT (kappa 0.7271) | point gaps positive (numerical audit 234, CONFIRMED by theory audit 299); L^2 distance > 0.0003518 from held-out probe (19, 600) (theory audit 298 with numerical audit 235) and > 0.0012324 from (23, 600) (numerical audit 237, CONFIRMED by theory audit 304) and > 0.0030334 from (23, 2400) (numerical audit 239, CONFIRMED since matrix v135 through the norm-certification team's complete weak test, accepted in numerical audit 383); FLOAT G0 0.3723, X3 proxy 515.8 | 6.10e-6 to 2.10e-4 | about 3.5e6 (sharpw, FLOAT) | RULED OUT (not a certification target) |
| 78 | Db, rebal, sharp, graded | candidate 015 | structure CONFIRMED (numerical audit 233) | point gaps positive, uniform graded gap 0.0698 (numerical audit 234, CONFIRMED by theory audit 299); L^2 distance > 0.0012324, above the graded budget (numerical audit 237 with theory audit 304), and > 0.0030334 at (23, 2400) (numerical audit 239 with numerical audit 383); FLOAT H 0.631, E2 proxy 604.6 | 6.36e-7 to 1.06e-4 | about 5.7e6 (sharp, FLOAT) | RULED OUT (not a certification target) |
| 79 | dyadic Y framework | candidate 010 | not needed | J(a) from modes 1 and 3 (numerical audit 231, CONFIRMED by theory audit 303) | origin ceiling of theory audit 146 | > 5.78998557 on seven cells covering 0 < a < 1 + 1/c | RULED OUT for this scheme (0 < a < 2, 0 < s < 1, finite Rw) |
| 80 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 016 (design test: 013 quotient basis plus 252 scale-25 functions in modes 17 to 31) | structure verified exactly (numerical audit 242, CONFIRMED by theory audit 313); (B-L2) holds in FLOAT (kappa 0.7338) | point gaps positive (numerical audit 242, CONFIRMED by theory audit 307); L^2 distances > 0.0010926 from (23, 2400) and > 0.0014703 from (19, 1800) (numerical audit 246, CONFIRMED by theory audit 310, theory audit 311; the earlier display 0.0014704 was rounded up, REFUTED by numerical audit 386); whole-plane G0 0.3088864 and \|\|rF\|\|_2 7.1457012 (the norm-certification team, CONFIRMED by numerical audit 341); held-out FLOAT m 3.77e-5 to 9.02e-4 at r about 19 to 40; complete actual E_2(016) > 608.392385921614, above 007's upper bound 606.820219 (numerical audit 396, CONFIRMED by theory audit 470 and closure review 048; replayed from the 650-digit archive numerical audit 399, CONFIRMED by theory audit 472 and numerical audit 402); plain upper bound H(016) < 1.063013 (numerical audit 403, CONFIRMED by the numerical auditor, accepted by the theory auditor in theory audit 476); improved upper bound H(016) < 0.944107, E_2(016) < 722.969 CONFIRMED by the theory auditor (theory audit 476); finite assembly CONFIRMED reciprocally by the numerical auditor (numerical audit 407); sharper H(016) < 0.619652, E_2(016) < 629.296113 from the numerical auditor's own integration of modes 1 to 31 (numerical audit 409, numerical audit 410, CONFIRMED by the numerical auditor and reproduced by the theory auditor in theory audit 480: accepted both ways; the theory team's closure review 051 recomposes them exactly, accepted in theory audit 483), so H(016) < H(007), gap above 0.015873038675998 (numerical audit 412, accepted both ways via theory audit 483), while E_2(016) > E_2(007); lower bounds H(016) > 0.6167335007 and E_2(016) > 628.580088526341 from the numerical auditor's replay of all 16 dual modes 1 to 31 (numerical audit 416, accepted by the theory auditor in theory audit 486 and at this precision in theory audit 488), so E_2(016) - E_2(007) > 21.759869526341; with all 16 modes in the tail formula, H(016) < 0.6179529539 and E_2(016) < 628.8790248, so H(007) - H(016) > 0.017571422145091 (numerical audit 418 and theory audit 486, CONFIRMED independently by both audit workers; accepted both ways through theory audit 488); with all 32 complete Hardy modes through frequency 63, H(016) < 0.617897369 and E_2(016) < 628.865389, so H(007) - H(016) > 0.017627007636152781 (numerical audit 430 and numerical audit 431, accepted by the theory auditor in theory audit 502) | 6.10e-6 to 2.10e-4 | distance 383.4 times the sharpw family ceiling (CONFIRMED); in G0 about 1.5e6 (FLOAT) | RULED OUT in every ball of these frameworks (not a certification target) |
| 81 | Db, rebal, sharp, graded | candidate 016 | structure verified exactly (numerical audit 242, CONFIRMED by theory audit 313) | point gaps positive, uniform graded gap 0.0698 (numerical audit 242, CONFIRMED by theory audit 307); distance > 0.0010926 (CONFIRMED by theory audit 310); FLOAT H 0.618; four held-out FLOAT values at K = 1800, 2400 above the graded budget | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT (not a certification target) |
| 82 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 017 (scale comparison: as 016 with the 252 functions at R0 = 50) | structure verified exactly by the numerical auditor (numerical audit 254; sector prefix CONFIRMED by theory audit 323); (B-L2) holds in FLOAT (kappa 0.7279) | point gaps numerical audit 254 CONFIRMED by theory audit 319; objective span CONFIRMED (numerical audit 255); distance > 0.001068502321 at (23, 2400) (numerical audit 256, CONFIRMED by theory audit 320) and > 0.001671830698 at (19, 1800) (numerical audit 257, CONFIRMED by theory audit 331); FLOAT G0 0.3209; E_2(017) in [605.4068697, 605.9589546] CLAIMED by the norm-certification team (16:14Z); numerical audit 413 and theory audit 484 CONFIRM only its conditional arithmetic, source premises OPEN | 6.10e-6 to 2.10e-4 | distance 586.6 times the sharpw family ceiling (CONFIRMED, (19, 1800)) | RULED OUT in every ball (not a certification target) |
| 83 | Db, rebal, sharp, graded | candidate 017 | as row 82 | point gaps and uniform graded gap 0.0695 (numerical audit 254, CONFIRMED by theory audit 319); distances as row 82; FLOAT H 0.615 | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT in every ball by its point gaps (not a certification target) |
| 84 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 018 (continuation of 016 by 12 steps, same basis, objective and held-out set) | exact structure by the numerical auditor (numerical audit 270; sector prefix CONFIRMED by theory audit 343); (B-L2) holds in FLOAT (kappa 0.7348) | point gaps positive (numerical audit 270, CONFIRMED by theory audit 342); objective-span separation CONFIRMED (numerical audit 271); distance > 0.001655825792 at (19, 1800) (numerical audit 272, CONFIRMED by theory audit 345); (23, 2400) > 0.001328016044 (CONFIRMED by theory audit 349); FLOAT G0 0.3127; held-out (19, 1800) 1.02e-3, (23, 2400) 7.89e-4, (21, 522) 2.80e-4 | 6.10e-6 to 2.10e-4 | distance 581.0 times the sharpw family ceiling (CONFIRMED, (19, 1800)) | RULED OUT (not a certification target) |
| 85 | Db, rebal, sharp, graded | candidate 018 | as row 84 | point gaps and uniform graded gap 0.0754 (numerical audit 270, CONFIRMED by theory audit 342); distance 3.621 times the graded ceiling (numerical audit 272 with theory audit 345, (19, 1800)); FLOAT H 0.615 | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT (point gaps; not a certification target) |
| 86 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 019 (continuation of 017 by 12 steps, same basis, objective and held-out set) | exact structure by the numerical auditor (numerical audit 279; sector prefix CONFIRMED by theory audit 355, origin by theory audit 354); objective span CONFIRMED (numerical audit 280); (B-L2) holds in FLOAT (kappa 0.7284) | point gaps CONFIRMED (numerical audit 279 with theory audit 353); distance > 0.001661806967 at (19, 1800) (numerical audit 282, CONFIRMED by theory audit 357); FLOAT G0 0.3251 | 6.10e-6 to 2.10e-4 | distance 583.1 times the sharpw family ceiling (CONFIRMED, (19, 1800)) | RULED OUT (not a certification target) |
| 87 | Db, rebal, sharp, graded | candidate 019 | as row 86 | point gaps and uniform graded gap 0.0693 (numerical audit 279, CONFIRMED by theory audit 353); distance 3.634 times the graded ceiling (numerical audit 282 with theory audit 357, (19, 1800)); FLOAT H 0.614 | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT (not a certification target) |
| 88 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 020 (016 plus 252 legqs R0 = 50 functions, 2426 generators, same 67 rows and held-out set, 12 steps) | exact structure by the numerical auditor (numerical audit 291; sector prefix CONFIRMED by theory audit 362, origin by theory audit 361); shapes and objective span CONFIRMED (numerical audit 292, theory audit 364); (B-L2) holds in FLOAT (kappa 0.7374) | point gaps CONFIRMED (numerical audit 291 with theory audit 360); distance > 0.001855374677 at (19, 1800) (numerical audit 293, CONFIRMED by theory audit 363); FLOAT G0 0.3201 | 6.10e-6 to 2.10e-4 | distance 651.1 times the sharpw family ceiling (CONFIRMED, (19, 1800)) | RULED OUT (not a certification target) |
| 89 | Db, rebal, sharp, graded | candidate 020 | as row 88 | point gaps and uniform graded gap 0.0844 (numerical audit 291, CONFIRMED by theory audit 360); distance 4.058 times the graded ceiling (numerical audit 293 with theory audit 363, (19, 1800)); FLOAT H 0.611 | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT (not a certification target) |
| 90 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 021 (020 plus 14 held-in mid-field rows at weight 1e12, 81 rows, 40 GPU steps from 020) | origin, state 131 leading density and forbidden prefix by the numerical auditor (numerical audit 314, CONFIRMED by theory audit 388, theory audit 389); shapes and rows CONFIRMED (numerical audit 315); (B-L2) holds in FLOAT (kappa_inner 0.7313) | point inequalities fail (numerical audit 314, CONFIRMED by theory audit 387, accepted in numerical audit 319); screening rule from 020 fails (numerical audit 313 with theory audit 394); distance > 0.001864696854 at (19, 1800) (numerical audit 316, CONFIRMED by theory audit 392, accepted in numerical audit 320; the earlier display 0.001864696855 was rounded up, REFUTED by numerical audit 387); FLOAT G0 0.2996 | 6.10e-6 to 2.10e-4 | distance 654.3 times the sharpw family ceiling (CONFIRMED, (19, 1800)) | RULED OUT (not a certification target) |
| 91 | Db, rebal, sharp, graded | candidate 021 | as row 90 | point tests fail and uniform graded gap 0.08009 (numerical audit 314, CONFIRMED by theory audit 387); distance 4.078 times the graded ceiling (numerical audit 316 with theory audit 392, (19, 1800)); FLOAT H 0.6096 | 6.36e-7 to 1.06e-4 | not evaluated | RULED OUT (not a certification target) |
| 92 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 022 (016 plus 240 legqs R0 = 25 functions in the higher blocks, 2414 generators, the 67 rows of 016, 40 GPU steps) | shapes, rank application and 67-row span CONFIRMED (numerical audit 321, independently theory audit 403); exact c, center relation and sector prefix (numerical audit 326, CONFIRMED by theory audit 406, theory audit 407); (B-L2) holds in FLOAT (kappa_inner 0.7315) | point gaps (numerical audit 326, CONFIRMED by theory audit 405); distance > 0.00135251 at (19, 1800) (numerical audit 327, CONFIRMED by theory audit 408); FLOAT G0 0.2816 | 6.10e-6 to 2.10e-4 | CONFIRMED distance 474.6 times the sharpw family ceiling | RULED OUT (not a certification target) |
| 93 | Db, rebal, sharp, graded | candidate 022 | as row 92 | six scalar point budgets fail and the original graded family has a uniform point gap 0.06836 (numerical audit 326, CONFIRMED by theory audit 405); distance 2.958 times the graded ceiling (numerical audit 327, CONFIRMED by theory audit 408); FLOAT H 0.6119 | 6.36e-7 to 1.06e-4 | point gaps and distance CONFIRMED | RULED OUT (not a certification target) |
| 94 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 023 (016 plus 252 legqs R0 = 100 functions in the blocks m = 9 to 15, 2426 generators, the 67 rows of 016, 40 GPU steps) | shapes, history and 67-row span by numerical audit 336, reproduced by theory audit 416; (B-L2) holds in FLOAT (kappa_inner 0.7373) | six scalar point gaps positive (numerical audit 337, CONFIRMED by theory audit 417); distance > 0.002634958 at (19, 1800) (numerical audit 338, CONFIRMED by theory audit 420); FLOAT G0 0.3228, largest registered held-out value 1.62e-3 at (19, 1800) | 6.10e-6 to 2.10e-4 | point gaps and distance CONFIRMED; distance 924.6 times the sharpw family ceiling | RULED OUT (not a certification target) |
| 95 | Db, rebal, sharp, graded | candidate 023 | as row 94 | six scalar point budgets fail and the original graded family has a uniform point gap 0.06288 (numerical audit 337, CONFIRMED by theory audit 417); distance 5.763 times the graded ceiling (numerical audit 338, CONFIRMED by theory audit 420); FLOAT H 0.6121 | 6.36e-7 to 1.06e-4 | point gaps and distance CONFIRMED | RULED OUT (not a certification target) |
| 96 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 024 (rule control of 016: same start, 67 rows and 12 steps, objective on the MID 32 rule, 2174 generators) | numerical audit 342 and numerical audit 345 (basis equal to 016's, held-out list outside the 67 rows, prefix through -7/2), reproduced by theory audit 427 and theory audit 430; (B-L2) holds in FLOAT (kappa_inner 0.7305) | six scalar point gaps positive (numerical audit 343, CONFIRMED by theory audit 428); distance > 0.001556067 at (19, 1800) (numerical audit 344, CONFIRMED by theory audit 431); FLOAT G0 0.3275, largest registered held-out value 9.55e-4 at (19, 1800) | 6.10e-6 to 2.10e-4 | point gaps and distance CONFIRMED; distance 546.0 times the sharpw family ceiling | RULED OUT (not a certification target) |
| 97 | Db, rebal, sharp, graded | candidate 024 | as row 96 | six scalar point budgets fail and the original graded family has a uniform point gap 0.0748 (numerical audit 343, CONFIRMED by theory audit 428); distance 3.403 times the graded ceiling (numerical audit 344, CONFIRMED by theory audit 431); FLOAT H 0.6187 | 6.36e-7 to 1.06e-4 | point gaps and distance CONFIRMED | RULED OUT (not a certification target) |
| 98 | dyadic Y framework | candidate 016 | not needed | J(a) from modes 1 and 3 (the norm-certification team, CONFIRMED by numerical audit 355) | origin ceiling of theory audit 146 | > 1.253908386497 on seven cells covering 0 < a < 1 + 1/c | RULED OUT for this scheme (0 < a < 2, 0 < s < 1, finite Rw) |
| 99 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 025 (016 plus scale-50, scale-100 and higher-block scale-25 functions, 2918 generators; 14 mid-field rows held in at weight 1e16) | structure CONFIRMED (theory audit 436 with numerical audit 361, numerical audit 365); prefix numerical audit 363, reproduced by theory audit 440; (B-L2) holds in FLOAT (kappa_inner 0.7388) | six scalar point gaps positive (numerical audit 362, CONFIRMED by theory audit 438); distance > 0.002065801 at (19, 1800) (numerical audit 364, CONFIRMED by theory audit 441); FLOAT G0 0.3051, largest registered held-out value 1.27e-3 at (19, 1800) | 6.10e-6 to 2.10e-4 | point gaps and distance CONFIRMED; distance 724.9 times the sharpw family ceiling | RULED OUT (not a certification target) |
| 100 | Db, rebal, sharp, graded | candidate 025 | as row 99 | uniform graded point gap 0.0698 and six scalar point gaps (numerical audit 362, CONFIRMED by theory audit 438); distance 4.518 times the graded ceiling (numerical audit 364, CONFIRMED by theory audit 441); 10 of 25 FLOAT registered held-out values above the graded budget; FLOAT H 0.6251 | 6.36e-7 to 1.06e-4 | point gaps and distance CONFIRMED | RULED OUT (not a certification target) |
| 101 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 026 (022 continued 60 steps with the 81 rows of 025, 14 mid-field rows held in at weight 1e16; 2414 generators) | structure and prefix numerical audit 366 and numerical audit 368, reproduced by theory audit 446 and theory audit 449; (B-L2) holds in FLOAT (kappa_inner 0.7324) | six scalar point gaps positive (numerical audit 367, CONFIRMED by theory audit 447); distance > 0.001355907 at (19, 1800) (numerical audit 369, CONFIRMED by theory audit 450); FLOAT G0 0.2788, largest registered held-out value 8.32e-4 at (19, 1800) | 6.10e-6 to 2.10e-4 | point gaps and distance CONFIRMED; distance 475.8 times the sharpw family ceiling | RULED OUT (not a certification target) |
| 102 | Db, rebal, sharp, graded | candidate 026 | as row 101 | uniform graded point gap 0.0594 and six scalar point gaps (numerical audit 367, CONFIRMED by theory audit 447); distance 2.965 times the graded ceiling (numerical audit 369, CONFIRMED by theory audit 450); 9 of 25 FLOAT registered held-out values above the graded budget; FLOAT H 0.6115 | 6.36e-7 to 1.06e-4 | point gaps and distance CONFIRMED | RULED OUT (not a certification target) |
| 103 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 027 (control for 026: 022 continued 60 steps with the plain 67 rows of 016, no held-in rows; 2414 generators) | The numerics team reports ten nonautomatic EXACT-ZERO sectors (no audit); (B-L2) holds in FLOAT (kappa_inner 0.7301) | no certified bound; FLOAT G0 0.2762, largest registered held-out value 8.25e-4 at (19, 1800) | 6.10e-6 to 2.10e-4 | not certified | OPEN (control for 026, not a certification target) |
| 104 | Db, rebal, sharp, graded | candidate 027 | as row 103 | no certified bound; 7 of 25 FLOAT registered held-out values above the graded budget, the largest by a factor of about 1.80; FLOAT H 0.6101 | 6.36e-7 to 1.06e-4 | not certified | OPEN (control for 026, not a certification target) |
| 105 | dyadic Y framework | candidate 015 | not needed | J(a) from modes 1 and 3 (the numerical auditor's own integration, numerical audit 382; the norm-certification team's mode energies agree; CONFIRMED independently by the theory auditor in theory audit 461) | origin ceiling of theory audit 146 | > 1.242922259074 on seven cells covering 0 < a < 1 + 1/c | RULED OUT for this scheme (0 < a < 2, 0 < s < 1, finite Rw) |
| 106 | dyadic Y framework | candidate 017 | not needed | J(a) from modes 1 and 3 (the numerical auditor's own integration, numerical audit 389, CONFIRMED by the theory auditor in theory audit 463; the norm-certification team's displays contain the numerical auditor's values) | origin ceiling of theory audit 146 | > 1.221854480167 on seven cells covering 0 < a < 1 + 1/c (two-evaluation cover) | RULED OUT for this scheme (0 < a < 2, 0 < s < 1, finite Rw) |
| 107 | L2, sharp L2, weighted sharp L2, transient-low L2 | candidate 028 (design control: 022 plus 252 legqs R0 = 25 functions of radial degrees 12 to 23 in m = 9 to 15, 60 steps with the plain 67 rows of 016, no held-in rows; 2666 generators) | The numerics team reports ten nonautomatic EXACT-ZERO sectors (no audit); (B-L2) holds in FLOAT (kappa_inner 0.7311) | no certified bound; FLOAT G0 0.2442, largest registered held-out value 8.15e-4 at (19, 1800) | 6.10e-6 to 2.10e-4 | not certified | OPEN (design control, not a certification target) |
| 108 | Db, rebal, sharp, graded | candidate 028 | as row 107 | no certified bound; 6 of 25 FLOAT registered held-out values above the graded budget, the largest by a factor of about 1.78; FLOAT H 0.6104 | 6.36e-7 to 1.06e-4 | not certified | OPEN (design control, not a certification target) |

Exponent pinning (theory audit 189 with theory audit 210, CONFIRMED by numerical audit 172 and theory audit 213): for state 131, d2, candidate 005 to candidate 012
and candidate 013 (same leading density, numerical audit 197) every "no sol." entry above holds at every c in that reference's chart, not only at c_l.

## 1. Team, sources and final documents

- Team and timing: see the run record above.
- Sources, read only: Changhe Yang's published IPM case 4 campaign (the case 4 report and its
  artifacts with the accepted states), the IPM Analysis II report (Analysis II) and the Hölder report, each with its
  artifacts, at repository commit bc01007, together with the working files of the teams that wrote Analysis II and the
  Hölder report. They were hashed at 2026-10-28T20:32Z and re-verified at 22:21Z, 23:01Z, 23:59Z, 00:42Z, 01:57Z and
  02:21Z with all file counts and hashes unchanged. No copy of the source data is included in the accompanying
  artifacts; the accompanying artifacts describe the required inputs.
- Final documents, each hashed by the coordinator after the file had been unchanged for at least one minute, and
  published in the accompanying artifacts:
  - the final theory report in the accompanying artifacts (saved 2026-10-29T18:26:10Z, 2459 lines, sha256
    55406b637f5e6c23c0abe0335ec6eab183af73967842a5591c2644663ab61a62 before the publication edits). The theory auditor
    confirmed it in theory audit 506 except one literal sentence of its section 2.5; the repair of that sentence and of one stale
    closure-matrix version number are recorded as errata EF1 and EF2 of the theory worker.
  - the final numerics report in the accompanying artifacts (frozen 18:30:12Z, 249 lines, sha256
    e092a45c0ad96062579c267581a575ff8ae6cc39c07588ea00065c8a687d75c2 before the publication edits; byte-identical to its
    17:35:40Z revision except the header line, confirmed in numerical audit 436).
  - the theory audit material in the accompanying artifacts: the final theoretical synthesis (sha256 006d2852..., frozen through theory audit 505 at
    18:30:22Z), the dated later addenda with the immutable snapshot through theory audit 514 (26abd7c7...) and its
    evidence map (1308af4c...), and the complete verdict ledger of 514 entries.
  - the numerical audit material in the accompanying artifacts: the numerical audit summary (frozen through numerical audit 440 at 18:51:00Z, d9e0c365...),
    the final numerical audit (18:54:37Z, 15dec905...), the later addenda with the
    snapshot through numerical audit 446 (02d65b47...), the evidence indexes and the complete verdict ledger of 447 entries.
  - the final linear-estimates summary in the accompanying artifacts (18:24:30Z, 13cd15cd..., accepted in theory audit 507), and
    the norm-certification summary in the accompanying artifacts (18:32:42Z, 6fb3ce5a...).
  The hashes before the publication edits identify the audited bytes; the published Markdown copies differ from them
  only in the removal of local paths and internal working-file names.

## 2. Contracts

Norms, chart, candidate IDs and file formats: the run contracts in the accompanying artifacts (v01, Amendments v02 sign and radius
corrections, v03 audit independence, v04 confirmation of originating with the numerical auditor numbers by any other worker).

## 3. Theory track (batch T)

theory exchange 02 (the theory team, 01:44:57Z, sha256 45b735907cf4..., 972 lines; read in full by the coordinator) supersedes theory exchange 01
as the registry:
- New framework IDs: transient-low L2 framework (theory audit 051), stationary L2 framework[K_L] (TP-1 and the theory audit 067 instances),
  variable-margin L2 framework[beta_L, w] (theory audit 113), L2 defect framework (the linear-estimates reviewer's H-free defect extension, theory audit 065; largest
  admissible sharpw defect 2.1046e-4 at g = 0), dyadic Y framework[a, s, Rw] (theory audit 058). New norms weighted X norm,
  X7744 norm, weighted X5184 norm, weighted L2 norm[a], weak-test norm[k, a], dyadic Y norm, weighted Laplacian norm[a].
- Necessary conditions L2 distance condition, weighted distance condition, graded L2 budget condition, packet condition, origin condition, weighted rate condition, dyadic radius condition,
  dyadic inverse-floor condition and dyadic Laplacian condition. L2 distance condition gives the family L^2 budgets of the Q7 answer (the coordinator rechecked
  the sharpw and bL arithmetic).
- Section 8 records the theory team's check that the decay argument of the application check extends to the multi-scale
  functions of candidate 010 (CONFIRMED by the theory auditor's independent proof, theory audit 149; normalization and matrix bounds remain
  separate). R4: for candidate 005, variable-margin L2 framework at
  beta_L = 1 would need theta <= about 0.452 (0.47790 with the OPEN theory audit 129 bound); not certified. R5 asks the numerics team to
  drop the refuted section 3b sentence; R7 asks for the weak distance of 009 and later candidates and the 007 N_a
  cover; R10 asks the numerics team to answer theory exchange 02 in numerics exchange 05.
- Scope correction (the theory auditor theory audit 148): the inference of lines 347 to 349 that rate-one transient routes must be posed
  outside Y is REFUTED as an inference from the far-field cap beta <= 1 + c - ca, which permits rate 1 for
  0 < a <= 1 (equality at a = 1). This proves no Y semigroup estimate; the theory auditor asks the theory team to narrow the sentence in
  the next theory version.

theory exchange 01 (the theory team, 22:14:15Z) registers the norms Ns16 norm, Ns13 norm, X3 norm, graded norm,
necessary point-test norm, symmetric point-test norm, dyadic norm, weighted lower-order norm and graded defect norm, together with these
frameworks:

| framework | origin | threshold | status |
|---|---|---|---|
| rebalanced Sobolev framework | The linear-estimates reviewer linear-estimate result 1 (base rate 297/1000) | 3/327680 (about 9.1553e-6), s = 2^-16 | AUDITED (theory audit 012) |
| sharp Sobolev framework | The linear-estimates reviewer linear-estimate result 2 (C_bg = 402, c_U = 8/5) | 1.0578e-4, s = 2^-13 | AUDITED (theory audit 028) |
| graded Sobolev framework | The theory team four-component closure | component boxes | AUDITED (theory audit 013, closure review 005) |
| L2 framework | The theory auditor theory audit 019 (L^2 low metric, no H) | 1/163840 (about 6.1035e-6), s = 2^-17 | AUDITED conditional (the linear-estimates reviewer review, theory audit 035) |
| graded L2 framework | The theory team | component box without H, s = 5 * 2^-18 | AUDITED (theory audit 039) |
| sharp L2 framework | The linear-estimates reviewer linear-estimate result 3 (linear-estimate result 2 constants on theory audit 019) | 7.6219e-5, s = 1/7744 | AUDITED (theory audit 042; box CONFIRMED numerical audit 054) |
| weighted sharp L2 framework | The linear-estimates reviewer linear-estimate result 3 (weights 2^15, 2^20) | 2.1035e-4, s = 1/5184 | AUDITED (theory audit 042; box CONFIRMED numerical audit 054) |
| alternative defect framework | The theory auditor theory audit 004 (linear defect) | (r - m)(mu - A r) >= epsilon + B r | AUDITED conditional, sections 2 to 4 (the linear-estimates reviewer review, theory audit 062); no computed defect |
| fractional framework | The linear-estimates reviewer | expected 1e-5 to 1e-4 | HEURISTIC |
| tail-exponent framework, Woodbury framework | The linear-estimates reviewer, the theory team | none | OPEN |
| variable-margin L2 framework[beta_L, w] (theory exchange 02) | The theory team rate trade (beta_L in place of 2 in (B-L2)) | sharpw weights: 1.692e-4 (beta_L = 7/5, s = 1/5476), 1.066e-4 (beta_L = 1, s = 1/6561) | AUDITED conditional (theory audit 113); safe rate endpoints 0.76024 (sharp), 0.34325 (sharpw); 0.7602 and 0.3432 REFUTED |
| transient-low L2 framework and stationary L2 framework[K_L] (theory exchange 02) | The theory auditor (theory audit 019 with (L) in place of (B-L2)) | 1/196608 (about 5.0863e-6), s = 2^-17; with \|\|A_k^-1\|\| <= K_L (TP-1): 1.5344622e-5 (K_L = 2, s = 1/51984), 2.4186857e-5 (K_L = 1, s = 1/51529), R = 21/100000 | AUDITED conditional (the theory team closure review 009, theory audit 057); K_L thresholds CONFIRMED with directed rounding (theory audit 067) |

Other theory results:
- AUDITED necessary point tests: theory audit 007 (reviewed by the theory team and the linear-estimates reviewer), with the S1 symmetry improvement theory audit 017
  (scope mu <= 3/10).
- Structured Hilbert-Schmidt identity for the signed coupling remainder: theory audit 016 (AUDITED), with the state 131 value
  0.7107535442 (theory audit 018 CONFIRMED).
- Finite-family L^2 floor: theory audit 025 (AUDITED; numbers CONFIRMED by numerical audit 032 and theory audit 027).
- Weak necessary test, Proposition W of linear-estimate result 3 (AUDITED, theory audit 042); its d2 evaluation numerical audit 053 is CONFIRMED by theory audit 044,
  which also proves the cutoff removal independently.
- Gradient-free L^2 distance (the numerical auditor numerical audit 057, CONFIRMED by theory audit 048): for d2 the fixed-c necessary radius exceeds
  0.0027197370, and 0.0029919 with theory auditor's sharper gradient bound (CONFIRMED by numerical audit 061; exact value 0.0029919694...,
  so the earlier "0.0029920" was rounded up and is withdrawn).
- Annular obstruction in the L^2 affine class (the numerical auditor numerical audit 055, CONFIRMED by theory audit 049): a leading sector r^q with q >= -1
  excludes every correction in L^2 with bounded gradient, at any c; it applies to state 131. Theory auditor's version without the
  gradient bound is CONFIRMED by numerical audit 062.
- Weak tail exponent pinning (theory audit 189, AUDITED through the theory team closure review 023 and the linear-estimates reviewer's review of theory audit 189, cited in theory audit 200; theory audit 201
  CONFIRMED): for a reference with a nonzero leading r^gamma profile, 0 < gamma < 1, every stationary correction with
  h and U[h] in L^2((1+r^2)^(-a) dX), 0 <= a <= 1 + gamma, has c = 1/gamma. Theory audit 203 gives 007's leading
  profile (first sine coefficient between 18 and 19), CONFIRMED by numerical audit 165, so the 007 exclusions hold at every c.
  theory audit 210 (CONFIRMED by numerical audit 172, theory audit 213) gives the same entire leading profile for state 131, d2 and 005 to 012, so the
  same holds for their exclusions. Theory audit 199 (AUDITED, the theory team closure review 024 with theory audit 212): the 007 density span has dimension
  1922. Theory audit 205 (AUDITED: The theory team closure review 025, theory audit 220): no finite linear or log-polynomial tail augmentation represents an
  exponent change, so another exponent needs a new chart with nonlinear tail coordinates (Route T-E). Fixed-c
  dilation is different: one tangent direction Lambda rho does not suffice (theory audit 221), but the dilation orbit of 007
  lies in E_a plus a finite span of branch tail amplitudes, of dimension 4 at a = 0 (theory audit 222, AUDITED: The theory team
  closure review 027, theory audit 232; numbers CONFIRMED by numerical audit 177 and theory audit 226). Theory audit 234 (AUDITED: The theory team closure review 030, theory audit 246, numerical audit 192; a second
  review by the linear-estimates reviewer also CONFIRMS it) shows that the PDE forces every lower nonintegrable tail profile from the leading
  one; theory audit 235 (CONFIRMED by numerical audit 189, theory audit 252) finds that exact 007 satisfies these relations, so in the theory audit 222
  augmentation fixing the leading amplitude loses no solution with positive amplitude up to dilation (closure review 030 R3). A
  different leading angular shape lies outside the 007 chart. Theory audit 206 (AUDITED: The theory team closure review 026, theory audit 223): the
  bound ||w D^k U[h]||_2 <= (1 + 2/(k + 1))^(1/2) ||w D^k h||_2 for centrally odd h; the sharp squared constant is
  Lambda_k (theory audit 224, CONFIRMED analytically, eigenvalues FLOAT). Weighted residual-tail obstruction (theory audit 202, AUDITED under its hypotheses): for a <= 2 a residual with a uniform
  nonzero leading power q >= a - 1 excludes every weighted L^2 correction of the affine class. Compact
  corrections (theory audit 281, AUDITED through the theory team closure review 033 and theory audit 296): no compactly supported L^2 correction of 007, 013 or 014 gives an
  exact solution in the canonical fixed-c chart, since each keeps an exactly nonzero branch 4, q1 residual
  coefficient above the decay r^(gamma - 4) that a compact correction can produce outside its support; this says
  nothing about corrections with tails. The linear-estimates reviewer's review of theory audit 281 CONFIRMS theory audit 281 in a second review and adds (R2,
  CONFIRMED by the theory auditor in theory audit 305 with an exact nonzero rational determinant) an endpoint obstruction: an exact compact correction forces the (1, 2) sector at exponent
  gamma - 4 into a dipole form that 007, 013 and 014 do not have (relative residual 0.6294 after the best multiple);
  that sector comes from branch 0 only, so a branch 3 redesign such as theory audit 295 would not remove it. This is a
  necessary condition for exactly compact S1 L^2 corrections at fixed c; it does not exclude the noncompact
  integrable-tail direction of theory audit 295 (theory audit 305). Theory audit 294 (AUDITED: The linear-estimates reviewer the review of theory audit 294, accepted in theory audit 315): under an
  explicit weighted C^1 decay hypothesis the correction must carry the forced integrable tail -r^q Theta at the
  first descendant exponent q of 007, 013 and 014. Theory audit 295 (AUDITED: The theory team closure review 034, accepted in theory audit 315) gives an exact
  branch 3 potential direction that cancels that sector while keeping the leading ladder and the origin
  normalizations (first remaining exponent -3 - epsilon1); it is a reference-design direction, not a candidate, and
  in the weighted spaces E_a it does not evade theory audit 291. Its three particular global repairs have L^2 norms above
  4373.34 (theory audit 316, CONFIRMED; this concerns that formula only). The linear-estimates reviewer's extensions are AUDITED through the theory auditor's
  independent proofs: the forced tail continues to gamma - 4 < q < -3, so after the repair a weighted C^1 correction
  carries a forced (9,0) tail of density circle norm 5428.790031 (theory audit 317), and no exact correction has faster
  weighted C^1 decay than the forced exponent (theory audit 318). Neither excludes arbitrary L^2 corrections. Theory audit 314
  (AUDITED: The theory team review closure review 035, accepted by the theory auditor in theory audit 325; second review by the linear-estimates reviewer, accepted in theory audit 333): a fixed
  smooth radial cutoff of a homogeneous
  potential tail, dilated to radius L, cancels the (4,1) tail of the campaign references at L^2, graded Hessian and
  sharp Hessian costs that tend to zero as L grows (for -3 < q < -1); the repaired reference keeps the interior disk
  and every origin jet and has first residual sector (9,0). It is a reference-design statement, not a stationary
  solution; the FLOAT cutoff radii are not certificates. closure review 035 remark (b), CONFIRMED by the theory auditor (theory audit 326): in a
  weighted residual norm with weight a <= q + 1 the residual of this cutoff family diverges as its L^2 cost tends to
  zero (logarithmically at a = q + 1); in the campaign's range -2 < a <= 4 gamma - 4 the repaired residual is finite
  but grows along the family. This is a tradeoff of this construction, not a lower bound for every repair. Theory audit 334
  CONFIRMS the linear-estimates reviewer's remarks R2 and R3 on it: for q < -2 the cutoff's homogeneous H^(-sigma) cost (0 < sigma <= 1)
  tends to zero, its H_q cost stays above a positive bound independent of the radius, and the residual sectors of
  the cutoff repair and of the global repair agree at and above exponent gamma - 4, including (1,2). Theory audit 324
  (reviewed by the linear-estimates reviewer, the review of theory audit 324, CONFIRMED; AUDITED through the review of theory audit 324, accepted in theory audit 337; reference
  design) states that two successive far-out cutoffs remove both the (4,1) and the (9,0) tails
  of 007, 013 and 014 at arbitrarily small L^2 cost, leaving a residual O(r^(-1 - 5 delta)).
- Weighted signed compact remainder on the odd subspace: theory audit 041, AUDITED as a conditional low-space theorem (the theory team
  review closure review 008, review set 04, 22:55Z). It gives no closure threshold.
- theory audit 022 (weighted L^2 low inverse): AUDITED as a conditional low-space theorem (theory audit 045, from the linear-estimates reviewer's full review).
- alternative defect framework (theory audit 004, sections 2 to 4): AUDITED as a conditional theorem through the linear-estimates reviewer's full review
  (theory audit 062), except the leading-tail sentence under (B11); no computed defect certificate exists. The linear-estimates reviewer's H-free
  defect extension (R3) and commutator constant 24/5 in place of 17 (R4): AUDITED (theory audit 065).
- Origin restriction on contractive high energies: theory audit 060, AUDITED conditional on its coefficient hypotheses
  through the theory team closure review 012 (theory audit 091). A positive H^(2+s) contractive gap needs s < c - 1 (rate at most c + 1 - q); no
  stationary-inverse obstruction follows. Exterior onset table of the linear-estimates reviewer: CONFIRMED (theory audit 063).
- d2 M1 >= (9/10) I: theory audit 061 reproduces numerical audit 056 with an independent 326-cell cover. Localized weak probes: theory audit 064
  reproduces numerical audit 064 and numerical audit 065 (d2 0.29552, Mpen2 0.55006, rounded down). Compact annular probes: theory audit 078
  reproduces numerical audit 066 at R = 8, 16, 32, 16384 (at R = 16, d2 > 0.08512606, Mpen2 > 0.17820407). Snapshot localized
  distances 1.5636, 0.2298, 1.4000 for candidate 002, 003, 004: theory audit 068 reproduces numerical audit 070; theory audit 075 reproduces the numerical audit 069
  first-sine projector exactly (7206 coefficients, d2, Mpen2 and candidate 002 to 005).
- Graded correction budget (the linear-estimates reviewer Proposition G): every positive graded or gradedL2 top-row budget forces
  the bound ||h||_(H^(2+s)) < 1/2000 (theory audit 070, CONFIRMED). Theory audit 070 also recomputes the uniform graded point test (gaps
  0.030548 for Mpen2, 2.93767 for b6). b6 and Mpen2 sharp Sobolev framework point gaps: theory audit 069 reproduces numerical audit 047.
- d2 signed bound theta <= 2/25 on the whole plane: theory audit 053 reproduces numerical audit 051 with an independent 120-cell Bernstein
  cover, so (B-L2) for d2 is CONFIRMED.
- theory team TP-1 (positive-real resolvent continuation, (L0) in place of (L)): CONFIRMED by theory audit 059. TP-1b (finite-rank
  reduction): repaired using raw L^2 high rows, CONFIRMED by theory audit 073; a quantitative Woodbury margin and a K_L
  certificate remain OPEN. Theory audit 051 thresholds as functions of K_L: theory audit 067 (CONFIRMED).
- Exterior negative-norm tail witness theory audit 014: AUDITED through the linear-estimates reviewer's review (theory audit 056).
- Scale-adapted weighted high space with a conditional closure under a high resolvent hypothesis (H): theory audit 058,
  AUDITED conditional on (1), (8), (9), (H), (12) and F in Y through the linear-estimates reviewer's review (theory audit 095); no concrete (H) is
  proved. The linear-estimates reviewer's consequences (theory audit 096, CONFIRMED): radius ceiling R < sqrt(8 pi)(1 + c - c a)/(1 + a); at
  a = 221/200 with the certified rate 0.02181481 the scheme needs M < 1.2613e-12 (M < 7.4294e-11 for any rate at
  that weight; the 1.2613e-12 bound is tied to that prescribed rate). REFUTED as implications: that an origin energy packet forces s < c - 1 in (H), and that a lower rate
  certificate bounds the best rate. The theory auditor's far-field inverse floor M >= 1/(1 + c - c a) (theory audit 097, AUDITED through the theory team closure review 013, theory audit 114) turns
  the linear-estimates reviewer's exclusion of state 131 for every a into the necessary condition
  Y(F) < sqrt(8 pi)(1 + c - c a)^2/(1 + a); the complete state 131 Laplacian tail beyond r = 8192 (theory audit 098) and a
  256-cell cover of 2/c < a < 1 + 1/c (theory audit 099, minimum squared ratio > 11.2378) violate it, both CONFIRMED by numerical audit 093,
  numerical audit 094 and theory audit 105. So the theory audit 058 scheme (dyadic Y framework) is RULED OUT for state 131 at every a, s and Rw
  (row 58). For d2 the lower bound Y(F) >= 5^((a-2)/2)||(1+r^2)^((2-a)/2) Delta F||_2 for 0 < a < 2 (theory audit 107, AUDITED
  through the theory team closure review 014, theory audit 120) with the CONFIRMED norms (numerical audit 099, theory audit 116) gives a seven-cell comparison with ratio >
  1.35446 (theory audit 112, numerical audit 100, CONFIRMED by theory audit 116), so the scheme is RULED OUT for d2 as well (row 59). For
  candidate 007 the exact first- and third-mode projections give ratios > 1.01380, 2.23154, 9.40192 and 393.749 on four
  cells covering 4/5 <= a < 1 + 1/c_l (theory audit 127, CONFIRMED by numerical audit 113, proof reviewed by the theory team closure review 015; row 64);
  0 < a < 4/5 is covered through the origin ceiling (theory audit 146, theory audit 147, AUDITED through the theory team closure review 017), so the scheme is
  RULED OUT for candidate 007 at every 0 < a < 2. Spectral form of the floor: theory audit 124 (CONFIRMS the theory team closure review 013 remark 3); compact and finite-rank
  perturbations: theory audit 131 (AUDITED through the linear-estimates reviewer's review). Other high spaces are not excluded. Sharp weighted odd Beurling bound (2+a)/(2-a) and odd IPM velocity bound 2/(2-a): theory audit 054
  (AUDITED via the theory team closure review 010, theory audit 071). S1 weighted velocity constants 1.616466 to 13.806975 for a = 6/5 to 19/10 (theory team
  TP-2): CONFIRMED by theory audit 072 with rational Schur certificates and by numerical audit 088 (theory audit 103). Neither gives a high inverse or a closure.
- Principal energy obstruction after compact repairs: theory audit 047, AUDITED conditional on its signed-decomposition,
  bounded-coefficient and canonical-velocity hypotheses (the theory team closure review 011, theory audit 080). TM-17b as a direct replacement of (B-L2) in
  theory audit 019: REFUTED (theory audit 050).
- Membership contracts: theory audit 033 (CONFIRMED).
- The answers in theory exchange 01 section R are HEURISTIC arguments:
  - A far-field weight r^(-sigma) at the L^2 level must have sigma < about 1.13.
  - Exponential localization is impossible.
  - Route T-E gives no visible cost gain for the invariant sector.
- The numerics team scaled-generator algebra, moments and interval jets: theory audit 076, theory audit 077 (CONFIRMED under exact rational
  inputs). Theory audit 079 (exact enclosure method for scaled radial factors): CONFIRMED by numerical audit 086 (independent derivation,
  13 closed-form tests).
- candidate 005 point value and localized weak distance: theory audit 082 reproduces numerical audit 076 from independent polar fields (8 point
  fields, 5 gaps, 28 weak-probe components), so the fixed-c exclusions of rows 53 and 54 are CONFIRMED. Its kappa
  1.35808 (numerical audit 077) is CONFIRMED by theory audit 083 (four exact rational energies agree).
- The theory team TP-3 (weighted energy obstruction map at state 131): CONFIRMED by theory audit 084. Every weighted L^2 energy with
  weight exponent a has rate at most c_l + 1 - a c_l at state 131; there is no positive rate for a >= 1.552389 and no
  rate 2 for a > 0.447611; 58 (a, R) entries have a certified point with lambda > c_l + 1. Inverse-based routes are
  not affected.
- The theory team TP-4 (principal-packet energy caps): CONFIRMED by theory audit 092 in an explicit scope (smooth sublinear backgrounds,
  power weights of exponent p < 3 - gamma, every real Bessel order, unweighted homogeneous order 1). The rate of a
  weighted H^q energy is at most inf lambda_min of an explicit principal matrix; A2's (B1), (B4), (B5), (B6), (W2) are
  such matrices. Independent state 131 point caps (theory audit 093): below 0.99116 (B4), 0.63089 (W2, k = 1), 0.61151
  (B5), -1.20662 (B6). The caps bound energy certificates, not inverse norms. Growing weights with p > 2 - gamma violate the
  weighted second-derivative background condition at state 131 (theory audit 094, AUDITED through the linear-estimates reviewer's review, theory audit 179,
  which adds sharp coefficient thresholds; a sign misprint in that review is corrected by theory audit 181 without effect).
- Weighted weak-distance test for H_a = L^2((1+r^2)^(-a) dX), 0 < a < 2: theory audit 081, AUDITED through the linear-estimates reviewer's review (theory audit 109),
  rederived independently by the numerical auditor (numerical audit 085). Values at a = 1 (theory audit 085,
  reproduced by numerical audit 085 in 63 comparisons, CONFIRMED as computations): ||(1+r^2)^(-1/2) h||_2 > 0.0071933 (d2),
  0.0156668 (Mpen2), 0.0061687 (candidate 005). At a = 6/5 (theory audit 088, CONFIRMED by numerical audit 089 in 91 comparisons, theory audit 100): state 131 > 2.9157e-5,
  d2 > 0.0048295, Mpen2 > 0.0091651, candidate 005 > 0.0064650. Larger probe scales give state 131 > 0.0012624 at
  a = 6/5 (numerical audit 095, CONFIRMED by theory audit 106). The linear-estimates reviewer's refined probes (CONFIRMED by theory audit 115 and numerical audit 101): d2 > 0.00781067
  (a = 1, k = 288), Mpen2 > 0.0224266 (a = 1, k = 96), state 131 > 0.000517550 (a = 1, k = 32768). The linear-estimates reviewer's sharpened
  weak proposition weighted estimate 4 is CONFIRMED by theory audit 172 (candidate values OPEN; theory audit 173 REFUTES the claimed downward rounding of
  its decimal table); its first independently checked value is candidate 005 > 0.02436463 at a = 6/5 (theory audit 175), 3.77 times
  the theory audit 088 value. No weighted ball has a threshold, so none of these decides a row.
- Weighted residual of state 131: theory audit 089 (exact polar algebra), CONFIRMED by numerical audit 087 (independent Cartesian
  construction); values in the Q5 answer.
- The theory auditor's self-audited items (theory audit 002, theory audit 003, theory audit 005, theory audit 006, theory audit 009) remain CLAIMED until reviewed; theory audit 094
  is AUDITED through the linear-estimates reviewer's review (theory audit 179).
- The theory team's (B-L2) trade, variable-margin L2 framework: CONFIRMED conditional by theory audit 113. Exact critical rates of the fixed Gram
  certificate: 3829321675/5037023232 (sharp weights) and 15208393675/44307283968 (sharpw); safe endpoints 0.76024
  and 0.34325; the printed 0.7602 and 0.3432 are REFUTED by negative Gram tests. Certified sharpw instances:
  beta_L = 7/5, s = 1/5476, threshold 1.692e-4; beta_L = 1, s = 1/6561, threshold 1.066e-4. Neither rate is an
  optimal operator rate. Ceiling of the fixed Gram scheme (theory audit 119): at beta_L = 2 with all other constants fixed, the
  best possible state 131 matrix floors give at most about 1.6555e-4 (sharp) and 3.8026e-4 (sharpw); these caps do
  not bound d2's matrix floors.
- Parity budget for the S1 commutator: theory audit 128 (the inequality; independently proved, with the d = 12 matrices of
  candidate 008, by numerical audit 116, CONFIRMED), theory audit 129 (larger radial bases; the d = 32 value for candidate 008 CONFIRMED by numerical audit 124,
  the d = 12 values for 007, 005 and d2 CONFIRMED by numerical audit 133 to numerical audit 135), theory audit 130 and theory audit 132 (angular parity blocks, 28
  and 80 tests, CONFIRMED by numerical audit 119), theory audit 133 (signed quadratic-form version, reviewed as valid by the numerical auditor, numerical audit 118, accepted in theory audit 139), theory audit 138 (union of
  overlapping compressions, reviewed as valid by the numerical auditor, numerical audit 120, and in theory audit 142), theory audit 141
  and theory audit 143 (union and signed bounds 0.79218 and 0.78617627 for candidate 008, CONFIRMED as finite computations by
  numerical audit 125 to numerical audit 127); the theory auditor checks numerical audit 116 and numerical audit 119 in
  turn (theory audit 137, theory audit 142). The theory team closure review 016 (review set 12, 01:54Z; incorporated by the numerical auditor in numerical audit 130) CONFIRMS theory audit 128 (1),
  theory audit 130 (1), theory audit 133 (1), the outward LDL criterion and theory audit 138, which are therefore AUDITED; theory audit 128 (2), the use in
  place of kappa_HS inside (B-L2), is AUDITED conditional on a full-plane theta bound and the completeness and
  Lipschitz bounds of V. Values in the Q4 answer.
- Finite angular recursion: every step through order 16 is invertible (1530 exact pivots, theory audit 123, CONFIRMED by
  numerical audit 109, whose independence theory audit 134 checks); order 8 has the small divisor
  s_8 = -116183978028673/4076476460239181 and first-mode velocity amplification 49.9745. This is finite algebra, not
  a convergence statement.
- The shell approximation of theory audit 056 (L^2 membership alone does not raise the minimal exterior Hdot^-1 norm) is
  AUDITED through the linear-estimates reviewer's review, and its order epsilon^(1/2) is sharp for a fixed odd mode (theory audit 135).
- Origin semigroup growth (theory audit 140, the theory auditor; the alpha_v case of theory audit 145, AUDITED with it through the theory team closure review 017): in an
  H^q realization satisfying its smooth-domain and generator hypotheses, ||S(t)|| >= exp((q - c - 1) t), also with bounded finite-rank pinning
  and compact perturbations, so a bound C exp(-beta t) needs beta <= c + 1 - q. It extends the energy restriction
  theory audit 060 to transient bounds; it says nothing about stationary inverses or the dyadic norm Y.
- Origin singular spectrum (theory audit 145, the theory auditor, AUDITED through the theory team closure review 017; each application must check its
  realization): the
  frozen origin gives singular sequences on Re lambda = q - c - 1 and q(2c - 1) - c - 1 - a0 and on the strip
  between them, so a pure H^3 realization has no bounded stationary inverse when 1 < c <= 2 and a0 >= 5c - 4. The
  d2-warm-start candidates have a0 = 10.06 to 10.31, above 5c_l - 4 = 5.0516; no registered framework uses a pure
  H^3 realization.
- Transfer to the dyadic hypothesis (theory audit 146, AUDITED through the theory team closure review 017): for 1 < c < 2 and a0 >= 5c - 4, the actual (H) of theory audit 058 forces
  s < c - 1 and M >= 1/(c - 1 - s), so Y(F) < H(c - 1)(1 + c - ca)/(1 + a), H(d) = max over 0 < s < d of
  (d - s) sqrt(4 pi s(1 + s)), H(c_l - 1) = 1.1302356388 < 57/50. Application to candidate 007 (theory audit 147): exact
  a0 = 10.3119990, seven cells cover 0 < a < 1 + 1/c_l with the certified mode 1 and 3 norms, minimum ratio
  1.2342773887 on [0, 1/4]. The numerical auditor reproduces the origin conditions and the seven cells with the exact maximum of H
  (minimum ratio 1.2449405901, numerical audit 128) and compares all 32 scalar fields with theory audit 147 (numerical audit 129), so the arithmetic is
  CONFIRMED; the theory auditor accepts the reproduction in theory audit 150. The theory team closure review 017 (review set 13, sha256 5cb1c275...) reviews
  theory audit 145, theory audit 146 and the application, including the Y scaling lemma and the forcing hyperplane f_y(0) = 0, and
  reproduces all seven cells (the script for theory audit 146 in the accompanying artifacts, 21 of 21 checks): CONFIRMED. The scheme is therefore RULED OUT for
  candidate 007 at every 0 < a < 2 (row 64). By closure review 017 the origin ceiling is below the theory audit 097 ceiling exactly when
  beta_inf(a) > 0.22546, that is for a < 1.4278 (FLOAT). These are necessary conditions on one linear estimate in
  one registered norm, not statements about solutions near candidate 007. The linear-estimates reviewer gives a second review of theory audit 145 and
  theory audit 146 and a third arithmetic path for theory audit 147 (theory audit 164). The linear-estimates reviewer's joint origin and far-field ceiling (the review of theory audit 146
  Remark review 1, CONFIRMED by theory audit 165): with d = c - 1 and b = 1 + c - ca > 0, Y(F) < b J(d, b)/(1 + a), where
  J = H(d) if b >= d - s* and J = b sqrt(4 pi (d - b)(1 + d - b)) otherwise; it is at most both separate ceilings.
  No row changes.
- Weighted third-order endpoint (theory audit 153, the theory auditor, AUDITED through the theory team closure review 018, accepted in theory audit 160): the theory audit 145 obstruction
  extends to the weighted E3 energy of Analysis II (weight (1 + 4r^2)^(2/5)) with any fixed positive lower-level
  weights, so there is no normalized stationary inverse bound there when 1 < c <= 2 and a0 >= 5c - 4. Analysis II
  claims only growth at E3 and decay in weaker fractional or interpolated spaces, so this does not contradict it.
- FLOAT only: The numerics team's all-mode N_a of candidate 007 (recorded observations in the accompanying artifacts 01:58Z) exceeds even the theory audit 097 ceiling at a = 0, 1/4, 1/2,
  3/4 (68.70 against 39.59 at a = 0), with most of the mass above mode 3. This differs strongly from the theory team's FLOAT
  modes 1 to 15 ratios (0.1275 at a = 0). Row 64 no longer needs these values (the theory review record 11 closes
  theory exchange 02 section 9 item 1).
- Rounded realization (numerical audit 131, CONFIRMED by theory audit 156): replacing every coefficient of candidate 007 by its binary64
  value leaves a nonzero (1,0) residual sector (angular norm about 7.2e-13, exponent 2/c_l - 1), so that function has
  infinite whole-plane W_a and N_a for a <= 2/c_l = 1.10478. The exact rational candidate is a different function and
  is not affected; finite-domain FLOAT diagnostics remain diagnostics.
- candidate 009 point and graded exclusions: theory audit 144 reproduces numerical audit 115 from an independent polar reconstruction (eight
  point fields, scalar balls and the uniform graded gap agree). candidate 010: theory audit 155 reproduces numerical audit 123 the same way
  (1024-bit Taylor reconstruction, 1.94 s), and numerical audit 136 compares the two (29 comparisons, all pass).
- Localized (B-L2) (the linear-estimates reviewer note on the localized (B-L2) margin, 01:52Z; the theory auditor theory audit 157 to theory audit 159). In unweighted L^2_S1 the best
  energy rate of A_0 lies between 1 + c - sup theta - kappa and 1 + c - sup theta (Proposition L1), so an
  unweighted energy rate pays the global supremum of theta. A bounded transport weight w = exp(psi) gives a rate at
  least ess inf(1 + c + g - theta_1) - theta_c - kappa - C_T ||grad theta_1||_2 - omega, g = V.grad psi,
  C_T = 0.26557, omega <= ||grad rho||_inf (exp(osc psi) - 1) (Lemma C and Proposition L2, CONFIRMED by theory audit 157, so
  AUDITED). Theory audit 158 REFUTES the suggested Hilbert-Schmidt bound for [U, w^-1]; theory audit 159 REFUTES the literal everywhere
  derivative of the orbit weight but CONFIRMS the orbit inequality, with compact support OPEN. Proposition L3 (a weighted rate beta
  forces V.grad psi >= theta - (1 + c - beta) a.e. and a matching orbit budget for osc psi) is CONFIRMED by theory audit 168
  for bounded locally Lipschitz psi with V.grad psi in L^inf, so AUDITED. Theory audit 169 REFUTES the claim that the auxiliary
  theta_1 budget cannot be avoided by any weight (counterexample rho = 0, theta = 0 with a theta_1 bump). Theory audit 170
  (compact Lipschitz orbit weight, with an added uniform exterior drift hypothesis) is CONFIRMED by the theory team closure review 020
  (theory audit 180, so AUDITED), with the sharper support radius r2 exp(L_r Theta_1/delta). The theory auditor's symmetric weighted coupling
  bound theory audit 163 (Sym(e^psi Q e^-psi) - Sym Q is Hilbert-Schmidt) is CONFIRMED by the linear-estimates reviewer's review (theory audit 174, so AUDITED) and
  may replace omega by the smaller bound; its annular version theory audit 176 is OPEN. No row moves: for d2, 007 and 009 the binding term is kappa, not sup theta (the linear-estimates reviewer).

## 4. Numerics track (batch N)

Snapshots after numerics exchange 03:
- candidate 008 (00:46:30Z; checksum manifest verified by the coordinator at about 00:51Z): structure CONFIRMED (numerical audit 105),
  point exclusion CONFIRMED (numerical audit 106 with theory audit 125), kappa_HS 0.84604 CONFIRMED (numerical audit 107 with theory audit 126); RULED OUT (rows
  60, 61).
- candidate 009 (01:15:50Z; checksum manifest verified by the coordinator at about 01:25Z, manifest in the accompanying artifacts sha256 fc9895de...
  matches the evidence index in the accompanying artifacts): structure CONFIRMED (numerical audit 114); point exclusion numerical audit 115 CONFIRMED by theory audit 144; RULED OUT in the
  stated balls (rows 62, 63).
- candidate 010 (01:36:39Z; checksum manifest verified by the coordinator at 01:43Z, manifest in the accompanying artifacts sha256 2f1c3fc4...
  matches the evidence index in the accompanying artifacts): the first candidate with multi-scale inner functions; structure CONFIRMED (numerical audit 122); point exclusion
  numerical audit 123 CONFIRMED by theory audit 155 and numerical audit 136; RULED OUT in the stated balls (rows 65, 66). The numerics team asks the norm-certification team whether these functions can be certified with the Beta-integral machinery.
- The numerics team's GPU allocation was revoked at 00:57:59Z; 009 and 010 were finalized exactly on CPU from their last
  checkpoints, and two CPU continuations from 007 are running (E2-balanced, with and without the multi-scale
  functions).
- Certified components of candidate 005 (Arb, each OPEN pending peer): G0 = 1.5630624464 (numerical audit 104), ||rF||_2 = 266.6711896
  (numerical audit 112), ||F||_H = 42.2834585352 (numerical audit 117). candidate 007: whole-plane G0 = 0.3766893247 (the norm-certification team, CONFIRMED by numerical audit 139)
  and ||rF||_2 = 7.8281155857, G1 = 3.4391037868, P2 = 190.8266911 (the norm-certification team, CONFIRMED by numerical audit 153) and a complete theta <= 2/25 cover with 223 cells (numerical audit 111, CONFIRMED by theory audit 162).
- The numerics team's exact stationary recursion through order 16 is CONFIRMED by numerical audit 098 (full-circle E_13 = 54390341.71 to
  E_16 = 1106012053.25; no convergence statement).

numerics exchange 06 (the numerics team, stamped 04:42:22Z, file written 04:43:35Z, sha256 b6b2ce9e..., 225 lines) supersedes
numerics exchange 05 (ACK by the theory team at 04:50Z): calibrations of the numerics team's FLOAT evaluators against certified values (its FLOAT
value at the (7, 131) probe of 007 is 2.866e-3 against the certified 2.8653e-3, numerical audit 160); FLOAT first-mode probes to
k = 65536 for 007 to 012; a far-field probe from the exact sector table (97 to 99.7 percent sector cancellation for
007); the Gauss-Newton spectrum (its count of 1022 zero singular values is a FLOAT threshold count; the exact nullity
is 1060, numerical audit 175 and numerical audit 178, which the numerics team adopts in its 04:48Z note for numerics exchange 07); and the pairing-row experiment
candidate 013 (rows 71, 72): 27 first-mode penalty rows lower the FLOAT first-mode pairings for k <= 128 by about three
orders of magnitude, while held-out angular probes at r about 25 to 30 stay unchanged (best FLOAT m 1.12e-3 at
(21, 522); for that probe the theory auditor later certified a distance > 0.00199234339 for 013, theory audit 255 with numerical audit 204). The numerics team reads this as a reachability radius of about 10 for the 007 basis in every probe family tried
(FLOAT; an interpretation of stalled optimization, which does not prove that the basis has no leverage there, theory audit 289). Pairing rows used in an objective are design rows: a violated row is exclusion evidence, a small one proves
nothing (theory audit 219).

numerics exchange 07 (the numerics team, 05:29:10Z, sha256 8fb65706..., 135 lines) supersedes numerics exchange 06 (ACK by the theory team at
05:34Z, on time). New, all FLOAT: snapshot candidate 014 (angular pairing rows, rows 75, 76); the theory exchange 03 R6(b) Newton-step
diagnostic (Galerkin L^2 step in the constraint null space with Euclidean Levenberg-Marquardt damping, so
basis-dependent: for 007 ||h0||_2 = 1.845e-2 at damping 1e-6 and 1.675e-2 at 1e-4, linearized ||F + J delta||_2 =
0.3383 and 0.3465 from 0.3767; consistent with the CONFIRMED lower bound 0.0047694 for every L^2 Newton step, theory audit 214);
cell-test proxies for 008, 009, 010 (009 cell [0, 1/4] not excluded by modes 1 and 3 alone, ratio 0.89; with mode 7
it is excluded exactly, numerical audit 187 with theory audit 250); the exact
quotient basis (1922 generators) with a physical Gauss-Newton spectrum in which 494 of the 1496 admissible
directions lie below binary64 resolution, so the plateau is not shown to be a stationary point (this supersedes the
numerics exchange 06 wording "genuine"). candidate 015 (pairing rows on the quotient basis from 013) was running at publication.
numerical audit 211 (the numerical auditor's audit of numerics exchange 07) REFUTES three inferences in it: that the two damped trials bracket the
undamped least-squares answer or give a residual floor of the span (so 0.338 is not a proved floor), that the 014
angular probes (21, 522), (23, 523), (25, 524) were held out (they were objective rows), and that the bare high-m
first-branch radial profile is concentrated near r = 1 (it is increasing and unbounded). The family optimum, its
conditioning and any uniform floor are OPEN; the exact bound of theory audit 214 is unaffected.

numerics exchange 05 (the numerics team, 02:32:22Z, sha256 9e569e64..., 359 lines) supersedes numerics exchange 04 (ACK by the theory team at 02:44Z):
- Section 5b (theory exchange 02 cheap tests, FLOAT): fixed-c weak-distance lower bounds over nine probes k = 0 to 8:
  007 3.79e-5, 008 8.12e-5, 010 2.31e-3, 009 6.03e-3; weighted L^2 values and FLOAT N_a of 007 (5^((a-2)/2) N_a =
  68.70 at a = 0). The 007 pairing is a sum of alternating annulus contributions (cancellation between annuli), and the
  objectives that improve the pointwise and (B-L2) numbers (009) or the mid-field L^2 numbers (010) raise the weak
  distance by about two orders of magnitude. The FLOAT value 3.79e-5 is not a bound; the certified single-probe value is 4.3987e-5
  (numerical audit 091, best probe k = 128); the optimized rational span probe gives 3.1474108e-4 (theory audit 182, numerical audit 152) and the degree-7 angular probe
  0.004769166867 (theory audit 185 AUDITED, CONFIRMED by numerical audit 157; an independent 80-probe scan selects the same mode, numerical audit 160, OPEN).
- The numerical auditor numerical audit 145 REFUTES two passages (the attribution of the graded exclusion to this weak-distance bound, which comes
  from the separate point gap of numerical audit 102, and a stale statement that the small-a dyadic case is open) and CONFIRMS the
  corrected scope; numerical audit 146 shows that the 14 percent difference to numerical audit 091 compares different probes (matched
  discrepancies below 3.6e-7) and gives the exact k = 8 bound 3.79309e-5 (OPEN pending peer). Numerical audit 147 gives the complete
  exact weighted Laplacian N(0) = 343.4908 of 007 (CONFIRMED with ten further weights by the norm-certification team, numerical audit 161), agreeing with the numerics team's FLOAT value to 1.8e-9.
- Section 8 next steps: nine weak-pairing rows in the balanced objective from 007 (target weak distance below 3.8e-6
  with G0, kappa margin and sup |F| within 20 percent), snapshots 011 and 012 from the two running CPU continuations
  (both at a plateau), and a request to batch T for a ball not centered at the fixed c. The theory team's ACK answers that
  the prompt fixes c_l and the leading far-field profile, that the scaling family has at most one member at finite
  L^2 distance, and that zeroing nine pairings removes only nine lower bounds (theory exchange 03 section R).
- Format: the header consultation list stops at matrix v31 and the section 5 table header still says float64 GPU
  (the worker is CPU only since 00:57:59Z).

numerics exchange 04 (the numerics team, 01:36:39Z, sha256 1aab4681..., 224 lines) supersedes numerics exchange 03:
- Section 5 residual table for 007 to 010 with pairing and R_nec columns; section 4 records the GPU revocation and
  the 008, 009 and 010 comparisons. Sections 6 and 7 still end at 007, and the header consultation list is stale.
- Section 3b still says that the T = 10 tail cost never decreases with the branch count, which numerical audit 103 refutes
  (943.60 at order 9 against 448.94 at order 10); the theory team's ACK notes this as well.
- Section 8: CPU only; next lever an E2-balanced objective with the multi-scale functions and a kappa penalty near
  1e7; the mid-field accuracy to r of order 100 to 1000 remains the lever for every framework.

numerics exchange 03 (the numerics team, 00:21:10Z) supersedes numerics exchange 02:
- New snapshot candidate 007 (00:20:05Z; checksum manifest verified by the coordinator at 00:32Z) from the balanced
  objective; values in the Q3 to Q6 answers. Its dyadic profile puts 43 percent of ||F||_2^2 in [4, 8); the balanced
  objective removed the near-field peak of 005 (sup |F| 0.138 at r = 2 to 4, FLOAT).
- Section 3b restated after an the second model referee check (a claim, not audited): at onset T = 1000 the pure-exterior tail
  cost is 1.4e-5 for 12 branches and 4.9e-9 for 16; an isolated sector falls below 1e-8 only for onsets above about
  6611 (12 branches) or 881 (16 branches). The convergence radius of about 12 for the stationary tail series is
  HEURISTIC. The numerical auditor REFUTES the literal sentence that the T = 10 cost never decreases with the branch count
  (isolated cost 943.60 at order 9, 448.94 at order 10) and CONFIRMS the finite costs and the onset radii 6611.42 and
  880.73 (numerical audit 103). A closed formula for the exterior Hdot^-1 norm of a zero-extended sector is now reported per surviving
  sector.
- Running (the numerics team): the X3 balanced run from 005, the multi-scale legqs inner functions (R0 = 10, 100), and a kappa
  penalty 3e8 from 007.
- Format: the header "consulted" list and the section 4 prose are carried over from v02 and are stale (flagged in
  recorded observations in the accompanying artifacts).

numerics exchange 02 (the numerics team, 23:36:22Z) supersedes numerics exchange 01:
- Full-circle tail cost table for n = 4 to 12 branches (correcting the v01 examples, as theory exchange 01 review 1 asked) and
  exact rational E_n for orders 9 to 12 (orders 13 to 16 running). With exact sector equality on r > T the
  cost ||F||_(L^2(r>T)) is at least 142.9 at T = 10 for every n, but 3.751 (n = 7) and 0.0895 (n = 12) at T = 100.
  The numerics team concludes that the onset radius T, not the number of branches, binds the L^2 route; the A2 inner basis
  resolves only to r of order 20 (FLOAT).
- Residual, (B-L2) margin, weak pairing and FLOAT point-test tables for d2, candidate 005 and candidate 006, and dyadic
  profiles for 005 and 006. numerics exchange 02 reported FLOAT point-test maxima above every ball radius by 2 to 4 orders of
  magnitude for d2, 005 and 006. This does not extend to later candidates: theory audit 374 records accepted sharpw point
  ratios of 4.558 for 007 and 3.048 for 009.
- Design lessons (FLOAT): warm starts from d2 beat projections of state 131; a balanced objective (log-measure term
  plus a kappa penalty) produced snapshot 007 (numerics exchange 03). numerics exchange 02 reads the candidate 005 dyadic table as
  putting its L^2 mass in r in [0.25, 2). Numerical audit 078 REFUTES that reading from the recorded annular norms: 12.4 percent of
  the recorded ||F||_2^2 lies in [0.25, 2) and 69.2 percent in [8, 256), the largest annulus being [32, 64). What
  sits near the origin is the derivative mass: 66.3 percent of the gradient column and 77.6 percent of the weighted
  second-derivative column lie in r < 2, which is where the point values and kappa are large.
- Hdot^-1 evaluator version statement: the numerical audit 067 factor is repaired; d2 390.2169 against numerical audit 020 390.2168.

numerics exchange 01 (the numerics team, 21:53Z):
- Sector table of state 131.
- Stationary recursion G_0 to G_12 (coefficients through order 12 CONFIRMED exactly by numerical audit 058; E_9 to E_12 =
  628494.74, 910751.02, 3586644.79, 10739524.91). Its fixed-radius tail "lower bounds" and its convergence-radius inference were
  REFUTED by numerical audit 041 and theory audit 036: the formulas are exact only for a pure exterior power. The arithmetic was corrected in
  theory exchange 01 review 1.
- Four snapshots, with every structural claim checked exactly by the numerical auditor:
  - candidate 001 (refit of the 860 basis): (1,0) to (5,0) nonzero, so not admissible (numerical audit 028). Theory audit 458 reproduces the
    leading residual and density exactly; its application of theory audit 049 to every L^2 correction in the affine class rho +
    L^2, at every real c, is AUDITED (reviews closure review 046 and the review of theory audit 458, accepted by the theory auditor in theory audit 465).
  - candidate 002 (seven branches): ten sectors exactly zero (numerical audit 039).
  - candidate 003 (eight branches): every forbidden sector zero; first survivor (3,1), norm 11957.67 (numerical audit 044).
  - candidate 004 (four branches, L^2 design): (1,0), (2,0), (3,0) zero; survivor (4,0), norm 345.672 (numerical audit 048).
- Problems found in the snapshots:
  - The radial-degree fields of the manifests are wrong (numerical audit 044, numerical audit 048).
  - The point residuals of candidate 002 to 004 are 465.9, 95.7 and 4.36 at r of about 0.47 to 0.64. Every specified
    small ball is excluded for 002 and 003 (CONFIRMED; 002 also from the sharp Sobolev framework ball, numerical audit 059) and for 004
    (CONFIRMED, theory audit 038).
- Certified components of d2 from the norm-certification team, CONFIRMED by the numerical auditor (numerical audit 024, numerical audit 026, numerical audit 043): G0 = 4.98881700456802,
  G1 = 1.02914187145367, P2 = 20.53677, Q3 = 128.147363. ||F||_H = 390.2168349 (numerical audit 020, CONFIRMED by the norm-certification team's
  independent VALIDATED enclosure, 23:55Z). Mpen2 G0 = 8.41564351151976,
  G1 = 2.58352962804257 (the norm-certification team, CONFIRMED by numerical audit 060); Mpen2 ||F||_H = 412.368 (numerical audit 068, originating with the numerical auditor).
- candidate 005 (23:27Z; checksum manifest verified by the coordinator): first campaign candidate warm-started from d2.
  Structure CONFIRMED (numerical audit 075); point value and weak distance CONFIRMED (numerical audit 076 with theory audit 082); kappa numerical audit 077
  (CONFIRMED by theory audit 083); FLOAT values in the Q3 answer. The numerical auditor is assembling its full exact residual with a faster exact Laurent packing (numerical audit 079,
  CONFIRMED against the complete d2 residual cache).
- candidate 006 (23:31Z; checksum manifest verified by the coordinator): a controlled comparison from candidate 003 on the E2
  proxy. Structure CONFIRMED (numerical audit 080); point value 6.3536 and L^2 distance 0.52622 (numerical audit 081, CONFIRMED by theory audit 086);
  theta_X = 6.4323 > c_l - 1 at (3/7, 1/4) (numerical audit 082, CONFIRMED by theory audit 087); RULED OUT (row 55). The numerical auditor also reproduced
  the exact origin and forbidden-sector data of 005 and 006 by a direct generator route (numerical audit 084, CONFIRMED). It shows that the state-131-descended family with imposed stationary moments does not recover a good inner
  region within the step budget, whereas the d2 warm start (candidate 005) does (the numerics team, FLOAT).
- The numerics team's floating negative-norm code has a factor 2 error in the outer-outer Green term (numerical audit 067, REFUTED with an
  exact counterexample; CONFIRMED by theory audit 066); the numerics team repaired it at 23:12Z and now reproduces numerical audit 020 in FLOAT
  (390.2169). The exact d2 radial split (numerical audit 072, originating with the numerical auditor) localizes the remaining small discrepancy in the
  interior part.
- The numerical auditor checked the numerics team's multiscale (legqs) generator moments exactly on a 360-generator grid (numerical audit 073, CONFIRMED for
  that comparison; the general formulas CONFIRMED by theory audit 076, theory audit 077) and built an exact first-mode residual projector
  (numerical audit 069, CONFIRMED by theory audit 075), which gives localized L^2 distances 1.5636, 0.2298 and 1.4000 for candidate 002, 003, 004
  (numerical audit 070, CONFIRMED by theory audit 068).
- The numerics team reports that the fixed-tail coefficients grow sharply at branch 8. The cause is the near-resonance 2 p_8
  = -0.0285 of the m = 0 potential inversion. The numerics team therefore limits fixed-tail designs to j <= 7, or frees the
  descendants (FLOAT observation).

## 5. Exchanges and feedback

| item | published | reaction | delay | verdict |
|---|---|---|---|---|
| numerics exchange 01 (the numerics team) | 21:53:10Z | ACK by the theory team at 22:00Z; response theory exchange 01 section R | 7 min | OK |
| theory exchange 01 (the theory team) | 22:14:15Z | ACK by the numerics team at 22:17Z; reaction published as numerics exchange 02 (23:36:22Z, section R) | 3 min | OK |
| numerics exchange 02 (the numerics team) | 23:36:22Z | ACK by the theory team at 23:44Z; response due in theory exchange 02 section R | 8 min | OK |
| numerics exchange 03 (the numerics team) | 00:21:10Z | ACK by the theory team at 00:24Z; response due in theory exchange 02 section R | 3 min | OK |
| numerics exchange 04 (the numerics team) | 01:36:39Z | ACK by the theory team at 01:41Z; response due in theory exchange 02 section R | 5 min | OK |
| numerics exchange 05 (the numerics team) | 02:32:22Z | ACK by the theory team at 02:44Z; response due in theory exchange 03 section R | 12 min | OK |
| theory exchange 03 (the theory team) | 03:41:45Z | ACK by the numerics team at 04:17Z and by the norm-certification team at 04:33Z; responses due in numerics exchange 06/v07 | 35 min | OK |
| numerics exchange 06 (the numerics team) | 04:42:22Z | ACK by the theory team at 04:50Z (its recorded acknowledgments, review record 27); response due in theory exchange 04 section R | 8 min | OK |
| numerics exchange 07 (the numerics team) | 05:29:10Z | ACK by the theory team at 05:34Z; response in theory exchange 04 section R2 | 5 min | OK |
| theory exchange 04 (the theory team) | 06:06:04Z | ACK by the numerics team at 06:08Z (its recorded acknowledgments "ACK theory exchange 04"): held-out rule adopted from candidate 015 on with the suggested held-out set, tangent-step rule end-state steps for 016 and 017, section 6 item 3 tested by candidate 016 (R0 = 25) and candidate 017 (R0 = 50); reaction due in numerics exchange 08 and the final numerics report in the accompanying artifacts. ACK by the norm-certification team at 06:25Z (the norm-certification team recorded observations in the accompanying artifacts): held-out rule accepted for every distance it reports, held-out monomials (21, 900), (25, 1500) named in advance for 015 and 016, 010 dyadic declined | 2 min (the numerics team), 19 min (the norm-certification team) | OK |
| theory exchange 05 (the theory team) | 06:39:59Z | ACK by the numerics team at 07:13Z (its recorded acknowledgments "ACK theory exchange 05"): held-out rule (i) to (iii) adopted as the reporting format from 016 on, the theory audit 273 wording of section 6 item 3 accepted, tangent-step rule end-state steps reported for 016 and 017, theory audit 295 noted as an exact-row design option; numerics exchange 08 and numerics exchange 09 (07:11:15Z) do not list theory exchange 05 among their inputs, so the reaction is due in the final numerics report in the accompanying artifacts. ACK by the norm-certification team at 07:23Z (recorded feedback): held-out rule adopted, fixed held-out set (21,900), (25,1500), (29,1200) for later candidates, 015 held-out block queued, 6.8 done for the 007 first-mode test values; correction at 07:24Z: 016 and 017 (legqs functions) are outside its exact pipeline, the legqs extension is now its main task (target about 13:00Z) | The numerics team 34 min; the norm-certification team 44 min | both OK |
| numerics exchange 09 (the numerics team) | 07:11:15Z | ACK by the theory team at 07:16Z (its recorded acknowledgments "ACK numerics exchange 09 in the accompanying artifacts"), eight items: the 017 FLOAT held-out values are all above the scalar ceilings and four above the graded ceiling (no verdict before the numerical auditor); small values at the tested probes in modes 33 to 47 bound nothing from above, so they do not show that the sweep to n = 31 was sufficient; state whether the tangent-step rule numbers are linear-model or evaluated residuals; section 4 still carries the label numerical audit 250 refutes; section 3 should name its basis; header corrections; 016 should be labeled RULED OUT next to "best design candidate"; the batch T request is answered by theory exchange 05 (L^2 masses 1e-4 to 1e-3 lie above every sharpw ceiling); response in the final theory report in the accompanying artifacts version 12 and theory exchange 06 R3 | 5 min | OK |
| numerics exchange 08 (the numerics team) | 06:46:52Z | ACK by the theory team at 06:52Z (its recorded acknowledgments "ACK numerics exchange 08 in the accompanying artifacts"): the 016 held-out table is above every scalar ceiling and four values above the graded ceiling in FLOAT; header corrections asked for (theory exchange 05 missing, "theory version followed" stale); response in the final theory report in the accompanying artifacts version 9 and theory exchange 06 section R | 6 min | OK |
| theory exchange 02 (the theory team) | 01:44:57Z | ACK by the numerics team at 01:49Z (its recorded acknowledgments "ACK theory exchange 02"); reaction planned as numerics exchange 05 (section 9 order, R5 correction, R10 answer); first FLOAT weak and N_a tests for 007 in the numerics team recorded observations in the accompanying artifacts 01:58Z | 4 min | OK |
| numerics exchange 10 (the numerics team) | 08:47:14Z | ACK by the theory team at 08:50Z (its recorded acknowledgments "ACK numerics exchange 10 in the accompanying artifacts"), seven items: the ratios 3.216, 3.656, 3.621 (graded) and 516.0 (sharpw) checked; the scope sentence narrowed to the certified rows; a certified band pairing gives a band-mass lower bound only; the 020 rise at K >= 1200 is 11 to 58 percent and the (27, 21) rise a factor 38.2; no estimate supports a norm with a lighter mid-field weight; response in theory exchange 06 section R3 | 3 min | OK |
| theory exchange 06 (the theory team) | 09:18:15Z | ACK by the numerics team at 09:19Z (its recorded acknowledgments "ACK theory exchange 06"), seven items: 020 RULED OUT adopted in the final numerics report in the accompanying artifacts and numerics exchange 11; a snapshot is named a target only if every registered held-out FLOAT value is below the graded ceiling; per-step density step norms logged from 024 on (tangent-step rule); seven-cell FLOAT proxy for 011 to 020 queued; wording requests applied in the final numerics report in the accompanying artifacts; requests 8 and 9 out of reach (no candidate within a budget). The theory auditor audit theory audit 373 at 09:31Z (review record173): closure inequalities, 51 ratios, 007 hypothesis repairs, third-cutoff dependencies and the exclusion scope through 020 CONFIRMED; the scaled-block index l >= 4 (correct: q >= 4) and closure review 037 (d) REFUTED; 2.839272409e-6 to be quoted with its hypotheses; 021/022 provenance limitation to be stated. The theory team response at 09:51Z (review record 39): all four points accepted and carried in the final theory report in the accompanying artifacts version 29 (sha256 5f93f02d..., errata 61 to 64) and review set 35 Part 1; the norm-certification team ACK due by 10:18Z, missing then, follow-up note 10:19Z; the norm-certification team ACK at 10:42Z (the norm-certification team recorded observations in the accompanying artifacts 10:42Z): requests 3, 5 and 7 answered, section 1.3 wording adopted, 016 and 017 RULED OUT taken as report-table context, corrections to its 09:03Z note after numerical audit 300 and numerical audit 301 | 1 min (the numerics team), 13 min (the theory auditor), 33 min (the theory team errata), 84 min (the norm-certification team, late) | ACK OK; audit done, errata carried; the norm-certification team ACK late |
| numerics exchange 11 (the numerics team) | 10:45:46Z | The theory team ACK at 10:50Z (the theory team recorded acknowledgments, notes (1) to (6): broken header, stale '020 OPEN', missing floors). The coordinator check (review records, this hour): the header consulted field repeats section 5 twice in place of the theory exchange 06 ACK location and the numerical auditor range; section 0 (a) says 020 is OPEN, while 020 is RULED OUT since matrix v88 (09:09Z) and the numerics team's theory exchange 06 ACK promised that wording; section 4 omits the CONFIRMED 020 and 021 floors and 021 RULED OUT; section 5 item 2 repeats that the 021 held-in rows were inert, the inference theory audit 390 REFUTES; manifest in the accompanying artifacts weak label k = 0..8 for maxima over 27 k; the numerical audit 321 mode-31 refutation (the coordinator note 10:57Z, fixes due 11:45Z). The numerical auditor audit numerical audit 328 (10:59Z, result e14b7398...): defects CONFIRMED; the printed 016 floor 0.0014704 REFUTED (safe: > 0.0014703), '020 OPEN' REFUTED, the inactivity inference REFUTED | 5 min (the theory team ACK), 14 min (the numerical auditor audit) | audit and ACK done; repairs pending (11:45Z) |
| theory exchange 07 (the theory team) | 11:20Z | published after the preview1 window (10:42Z to 11:12Z); records the theory audit 399 repairs, including the REFUTED sentence on stationary-only velocity estimates, and pins the review of theory audit 375 and the review of theory audit 381 and theory audit 384 at revision 2; consulted matrix v115 and the theory auditor through theory audit 408. Audited by the theory auditor in theory audit 412 (11:34Z): CONFIRMED with three wording repairs (stale 022 binding and (P)/tau sentences, scope of 5.6 (d)). ACK by the numerical auditor in numerical audit 335 (11:28Z), with the 023 tests of section 6 item 1 started (numerical audit 336 to numerical audit 338). ACK by the numerics team at 11:52Z (status file, five items: 022 RULED OUT adopted, parents named in every continuation manifest in the accompanying artifacts). ACK by the norm-certification team at 12:25Z (the norm-certification team recorded observations in the accompanying artifacts, five minutes after the hour), whose screening condition proposal the numerical auditor corrects at 12:29Z (theory exchange 07 section 5.6 needs tau >= \|\|rho_child - rho_parent\|\|_2, not a residual difference) | 8 min (the numerical auditor), 32 min (the numerics team), 65 min (the norm-certification team) | OK; the norm-certification team late |
| numerics exchange 12 (the numerics team) | 12:32:15Z | ACK by the theory team at 12:39Z (the theory team recorded acknowledgments: six notes, none changes an exclusion). The coordinator check (matrix v125): the header 'consulted' bullet is spliced with section 6 item 1; sections 0 and 6 say 024 awaits the theory auditor's replay, which had finished at 12:27:53Z (024 RULED OUT since v124); section 0 prints 5.764, 924.7 and 3.404 where the rounded-down factors are 5.763, 924.6 and 3.403; the section 3 heading says 011 to 021 while its table lists 008 to 025. Repairs requested for numerics exchange 13 and the final numerics report in the accompanying artifacts; the numerical auditor announces a source-bound audit | 7 min | OK |
| numerics exchange 13 (the numerics team) | 13:13:19Z | ACK by the theory team at 13:23Z (the theory team recorded acknowledgments, seven notes, none changing an exclusion: the certified floors of section 5 stop at 021; section 6 item 3 calls 025 FLOAT only although numerical audit 362 to numerical audit 364 and theory audit 438 to theory audit 441 exist; the 016 dyadic remark is stale since numerical audit 355; causal wording in section 6 item 1; the unnamed 95 percent share; truncated optimizer lines; header version fields). ACK by the numerical auditor at 13:25:31Z with its audit numerical audit 372 (the numerics v13 audit material in the accompanying artifacts, result 5411f621..., 23 checks): all 300 printed table values match the stored FLOAT sources; it REFUTES the section 6 counts and ranges for 024 (18 increases and 7 decreases in the stored values, not 16 and 9), 025 and 026, the MID16 label of 024, the attribution of certified total density-change bounds to the numerical auditor and the 'FLOAT only' status of 025. The coordinator check (matrix v130): section 6 item 1 prints '025 vs 016: 8 probes fall, factors 0.26 to 0.60' and 'K >= 1800 x1.34 to 1.58', while its section 2 table gives factors 0.034 ((25, 600)) to 0.599 for the 8 falls and 1.408 to 2.841 at K >= 1800; it prints '026 vs 022: 7 fall, factors 0.02 to 0.77', while the section 2b table gives 9 falls with factors 0.022 to 0.965; the 026 index in the accompanying artifacts entry says the K = 600 probes fall by factors 5 to 50, while (19, 600) rises 2.5-fold and (29, 600) and (31, 600) fall by factors 3.3 and 2.1; numerical audit 372's values from the stored sources agree. FLOAT summaries only; repairs requested for the final numerics report in the accompanying artifacts and numerics exchange 14 | 10 min | OK |
| numerics exchange 14 (the numerics team) | 14:44:45Z | ACK by the theory team at 15:02Z (review record v51 item 1: read in full; 027 stays FLOAT data and 028 is a reserved ID, so no theory requirement changes; the numerical audit 388 label repairs are taken as stated; the coordinator checked it within the hour). The numerical auditor reviewed it in numerical audit 388 (14:55:09Z): tables, ratios and the H18 comparison CONFIRMED as FLOAT data; three labels REFUTED (blanket MID 16 labels for 024, the 81-row exception list without 026, the stale 016 seven-cell 'pending' label); three actual-endpoint distance attributions OPEN. Content: numerical audit 372 corrections of numerics exchange 13 (section 0), 027 and 028 per-probe held-out tables (FLOAT), and the numerics team's H18 restriction of its H16 probe statement (028 moves 11 of the 15 K <= 1200 probes outside the 027 against 022 band and only (31, 1800) of the ten K >= 1800 probes; the coordinator recounted both counts from the printed factors) | 18 min | OK |
| numerics exchange 15 (the numerics team) | 15:25:44Z | ACK by the theory team at 15:38Z (review record v53 item 1: read in full from 15:35Z; 028 FLOAT only, rows 107 and 108 OPEN, no theory requirement changes; 6 of 25 registered held-out values above the graded ceiling, the largest 8.15e-4 at (19, 1800); FLOAT E_2 values show that E_2(007) < E_2(016) is pairwise). Content: the 028 snapshot, the withdrawal of the numerics team's H16 probe statement, seven corrected v13 and v14 displays | 12 min | OK |
| theory exchange 08 (the theory team) | 15:30:58Z | last exchange version of batch T. ACKs: The norm-certification team at 15:35Z (note 15:35Z), the numerical auditor at 15:40:19Z (note; 025 and 026 accepted both ways, the 015 to 017 dyadic results accepted, no new candidate optimization, literal corrections: delta = 0.4476112310..., the 2.7e-6 cap, row 35, 028 registration) and the numerics team at 15:43Z (status file 'ACK theory exchange 08'; no new candidate, no run after 028, the wording items of section 6 and R5 checked in the final numerics report in the accompanying artifacts). Audit: The theory auditor's theory audit 471 (15:44:07Z, 695 checks) CONFIRMS its finite mathematics and REFUTES the 2.7e-6 cap and three literal status statements; the theory team repairs them in the final theory report in the accompanying artifacts. The linear-estimates reviewer's linear-estimates reviewer check of theory exchange v08 (16:04Z) agrees with every the linear-estimates reviewer attribution except four wording items (the 2.7e-6 radius, the scope and hypotheses of the WU3 bounds, three not-covered items, a section reference) | 4, 9 and 12 min | OK |
| numerics exchange 16 (the numerics team) | 16:06:03Z | final exchange version of batch N: no new candidate; FLOAT diagnostics only (Newton steps for 027 and 028, seven-cell proxies for 026 to 028, the assembled E_2 proxy); the numerical audit 401 repairs recorded as made in the final numerics report in the accompanying artifacts. ACK by the theory team at 16:34Z (review record v55 item 1: read at about 16:15Z and again at 16:34Z; no new candidate, no request to batch T, no theory requirement change; the FLOAT E_2 proxies agree with the theory team's display arithmetic to within 0.05, with the same six snapshots below 007). The theory team's review record v54 (16:08Z) item 5 had stated that no exchange version came after numerics exchange 15; erratum E3 of review set 47 withdraws it. Audited by the numerical auditor in numerical audit 405 (finite displays and the four numerical audit 401 repairs CONFIRMED; one section 6 sentence REFUTED) | 28 min | OK |

Two-way content so far:
- The theory team corrected numerics exchange 01's tail arithmetic (review 1).
- The theory team answered the three questions of numerics exchange 01 section 8 (R2 to R4).
- The theory team assessed both running candidates (R5).
- The numerics team supplied the fixed-sector norms used for the onset tables of theory exchange 01 section 5.
- The numerics team accepted review 1 and adopted L2 framework as its primary target (objective X3 norm proxy, exact (1,0),
  (2,0), (3,0) at every harmonic, point tests and dyadic profiles for every candidate; the numerics team ACK of theory exchange 01).
- numerics exchange 02 delivered what theory exchange 01 section 9 asked for: the corrected tail table, exact E_9 to E_12, residual
  tables with theta and kappa, dyadic profiles and point tests. Its message to batch T: exact branches are cheap,
  mid-field accuracy to r of order 100 to 1000 is the lever, and (B-L2) is a real design constraint.
- numerics exchange 03 delivered the first candidate built with (B-L2) in the objective (candidate 007). The theory team's ACK announces
  for theory exchange 02 a trade of (B-L2) against the Gram rate (beta_L down to 0.3432 for sharpw) and an answer to the r^-1
  low-weight question of numerics exchange 02 section 8.
- numerics exchange 04 added three controlled comparisons (008 to 010). The theory team's ACK checks that the decay argument of the
  application check extends to the new multi-scale functions (CLAIMED pending review), flags the stale section 3b
  sentence (refuted by numerical audit 103) and states that theory exchange 02 R2 treats the r^-1 low weight as admissible.
- theory exchange 02 answers numerics exchange 02 to v04 in its section R (review 1 to R10) and sets the request order of its section 9
  for batch N (weak distance, point tests, the 007 N_a cover, norms). The numerics team adopted that order (the weak-test script in the accompanying artifacts) and
  reported FLOAT weak distances and N_a values for 007 within 14 minutes; the numerical auditor acknowledged theory exchange 02 in its
  01:51Z note and queued the exact all-mode N_a of 007. The theory team closed theory exchange 02 section 9 item 1 at 02:07Z (closure review 017).

## 6. Unresolved inequalities

- Open rows of the closure matrix (v185) and what each lacks: rows 4, 19 and 27 (seven-branch families in Analysis II D(b) framework,
  rebalanced Sobolev framework and sharp Sobolev framework): a family lower bound or an actual candidate; rows 33 and 50 (families with
  five or more exact stationary branches in L2 framework and its sharp variants): a candidate with validated X_s or
  X_(s,w) components and (B-L2) data; row 34 (the weighted L^2 low space of theory audit 022 at state 131): a high norm, its
  inverse and a nonlinear closure; rows 69 and 70 (candidate 011), 103 and 104 (candidate 027), 107 and 108 (candidate 028): every
  certified quantity (FLOAT controls, not certification targets). Every other row is RULED OUT; no row is PROVED or
  CONDITIONAL.
- candidate 017: the complete upper bound for H(017), the value E_2(017) and E_2(017) < E_2(007) (the norm-certification team CLAIMS a gap of at
  least 0.8591; accepted both ways are only the conditional arithmetic, the 16 dual trials, H(017) > 0.614419598760
  and the residual identity). These would order norms only; 017 stays RULED OUT by its distances.
- candidate 016: how the remaining width of the H(016) enclosure (0.6167335007, 0.617897369) divides between upper-bound
  slack and dual lower-bound slack (theory audit 504, theory audit 505; the exact width identity alone does not determine it). The
  certified bounds and exclusions are unchanged; 016 stays RULED OUT by its distances.
- Distances: CONFIRMED lower bounds on the fixed-c correction distance of different candidates do not order their
  actual distances (theory audit 219), and no upper bound on the distance from any candidate to an exact solution is available,
  since no existence theorem closes.
- Every pair: residual smallness. The best certified case is candidate 007 against weighted sharp L2 framework, short by more
  than 3596535.57 (all complete components, numerical audit 180 with theory audit 238); d2 against weighted sharp L2 framework is short by more than 2.43e7
  (against sharp Sobolev framework by more than 1.83e9 once the CONFIRMED H is included).
- L2 framework and its sharp variants: (B-L2) for Mpen2 (theta <= 0.0977, not certified); for d2 it is CONFIRMED
  (numerical audit 051 with theory audit 053); candidate 005 fails it through kappa (numerical audit 077, CONFIRMED by theory audit 083). Theory audit 051 and TP-1: (L) or a K_L
  certificate for any candidate (TP-1b repaired, theory audit 073; the Woodbury margin is OPEN).
- candidate 007 to 010 and 012 to 017: excluded from every specified scalar and graded ball (CONFIRMED; for 010 the
  statL and bL balls by its distance > 0.022479506978, numerical audit 205 with theory audit 270), and 007 to 010 also from the dyadic
  scheme (rows 64, 73, 74, 79).
- candidate 007: excluded from every ball of the matrix (CONFIRMED). For a successor of the same family: a certified theta
  <= c_l - 1 - kappa (0.08215 with 007's CONFIRMED kappa), certified residual components, and, to pass the selected
  sharpw sufficient residual test with its constants fixed, a smallness gain of more than 3596535.57 (certified lower
  bound); this gain is not a necessary condition for every route to a solution (theory audit 508).
- Endpoint route for the three-cutoff 007, 013, 014 (theory audit 335, theory audit 351): the universal-constant velocity form cannot
  reach the fixed sharpw ball or the sharpw, sharp Sobolev and graded family ceilings (theory audit 375 and theory audit 381 Sections 1 and 2
  AUDITED, theory audit 380 CONFIRMED: E < 0.785064 would be needed and every valid constant is at least 0.7930365). Unresolved
  by the linear-estimates reviewer's falsification check (AUDITED in sections 1 to 4 and in its corrected logical scope, theory audit 443 and theory audit 452;
  exact-radius refinements theory audit 454 and theory audit 464): at the Analysis II D(b) framework radii 2^-25 and 6.8626e-8 no proved obstruction
  excludes an improved universal constant below 1.020385 or 0.8711127; the proved constant 1.747261 reaches no
  registered radius. Still unresolved: an a priori H_q bound for stationary solutions and a correction-specific or
  stationary-only velocity estimate (neither proved nor disproved; theory audit 402, AUDITED since theory audit 413, gives only a limiting
  coefficient of at most 0.583 H_q under an angular-tail hypothesis; by the theory auditor's theory audit 414, AUDITED since theory audit 423, even a
  zero remainder with 0.583 misses all four targets in the complete radial integral, which needs E below 0.527596 for
  the fixed sharpw ball; the theory auditor's own theory audit 415, AUDITED via the linear-estimates reviewer's review of theory audit 415 and theory audit 434, certifies E = 0.372 on the
  endpoint spans, and its own theory audit 422, AUDITED in the same way, shows that this coefficient with zero remainder would
  pass the three scalar thresholds and not the graded one; theory audit 410's explicit remainder is AUDITED (closure review 043, theory audit 424),
  and with the theory audit 335 (7) tail input it exceeds the room by a factor above 40 for any coefficient (the linear-estimates reviewer and closure review 043
  step 9; main obstruction AUDITED by the theory auditor's theory audit 421; the theory auditor's theory audit 425, AUDITED via closure review 045 and theory audit 432, extends this to
  radius-dependent coefficients)). Open for this route: a tail bound with all exponents above about 1.05, or an
  estimate specific to stationary corrections; a separate multipole treatment of the inner part does not suffice with
  the present tail input (closure review 044, AUDITED via theory audit 426).
- (W3) for every archived refit (Theorem D_w).
- Family bounds for seven or more branches in N_s frameworks.
- The K range beyond 1315 (rebalanced Sobolev framework), 511 (sharp Sobolev framework), 1021 and 1063 (graded boxes) for six
  branches (cutoffs CONFIRMED, theory audit 040).
- Every family with five or more branches in L2 framework.

## 7. Audit status

- The theory auditor (verdict ledger in the accompanying artifacts, theory audit 001 to theory audit 267).
  - Independent audits:
    - linear-estimate result 1: theory audit 012.
    - The graded closure: theory audit 013.
    - The HS identity: theory audit 016.
    - Reproductions of the seminorms and points: theory audit 018, theory audit 021, theory audit 024, theory audit 026, theory audit 027, theory audit 029, theory audit 030, theory audit 031.
    - The finite-family floor: theory audit 025.
    - linear-estimate result 2: theory audit 028.
    - The weighted lower bound: theory audit 032.
    - The membership contracts: theory audit 033.
    - The matrix-cover method: theory audit 034.
    - Tail-claim scope: theory audit 036.
    - Candidate point witnesses: theory audit 037, theory audit 038.
    - graded L2 framework and the elementary lemmas of theory exchange 01: theory audit 039.
    - The six-branch cutoffs and the scope of theory exchange 01's general statements: theory audit 040.
    - linear-estimate result 3 (two sharp no-H frameworks, raw conversion, Proposition W): theory audit 042; four-branch cutoffs for them: theory audit 043
      (cross-confirmed with numerical audit 054 at 22:40Z and 22:43Z).
    - numerical auditor results: weak probe theory audit 044, L^2 distance theory audit 048, annular obstruction theory audit 049, snapshot theta witnesses theory audit 046.
    - theory audit 022 via the linear-estimates reviewer's review: theory audit 045. TM-17b transfer: theory audit 050 (REFUTED as a direct substitution).
    - theory audit 041 via the theory team closure review 008 and frozen reviews: theory audit 052. Numerical audit 051 reproduction: theory audit 053. Snapshot gaps and d2
      conversions for the linear-estimate result 3 balls: theory audit 055. Theory audit 014 via the linear-estimates reviewer: theory audit 056. Theory audit 051 via the theory team closure review 009: theory audit 057. theory team TP-1:
      theory audit 059. Numerical audit 056: theory audit 061. Theory audit 004 via the linear-estimates reviewer: theory audit 062. The linear-estimates reviewer exterior onsets: theory audit 063. Numerical audit 064, numerical audit 065: theory audit 064.
      The linear-estimates reviewer R3, R4: theory audit 065. Numerical audit 067: theory audit 066. Theory audit 051 thresholds with certified constants: theory audit 067. Numerical audit 070: theory audit 068.
      numerical audit 047: theory audit 069. The linear-estimates reviewer Proposition G and the uniform graded point test: theory audit 070. theory team TP-2: theory audit 072. theory team TP-1b
      repair: theory audit 073. Numerical auditor's second path for the theory audit 055 gaps: theory audit 074. Numerical audit 069 projector: theory audit 075. The numerics team scaled
      generators: theory audit 076, theory audit 077. Numerical audit 066: theory audit 078. Numerical audit 076: theory audit 082. Numerical audit 077: theory audit 083. theory team TP-3: theory audit 084.
      numerical audit 081: theory audit 086. Numerical audit 082: theory audit 087. Numerical audit 083: theory audit 090. theory team TP-4: theory audit 092, with independent point caps theory audit 093.
      The linear-estimates reviewer's dyadic-radius consequences: theory audit 096. Numerical audit 085, numerical audit 089: theory audit 100. Numerical audit 086: theory audit 101. Numerical audit 087: theory audit 102.
      numerical audit 088: theory audit 103. Numerical audit 084 (analytic): theory audit 104. Numerical audit 093, numerical audit 094: theory audit 105. Numerical audit 095: theory audit 106. Numerical audit 091: theory audit 108, theory audit 110.
      numerical audit 092: theory audit 111. The theory team (B-L2) trade: theory audit 113. The linear-estimates reviewer refined probes: theory audit 115. Numerical audit 099, numerical audit 100: theory audit 116. Numerical audit 096:
      theory audit 117. Numerical audit 097: theory audit 118. Numerical audit 102: theory audit 122. Directed-decimal corrections (theory audit 106, closure review 014): theory audit 121. The theory team closure review 013 remark 3: theory audit 124.
      numerical audit 106: theory audit 125. Numerical audit 107: theory audit 126. The linear-estimates reviewer's review of theory audit 124: theory audit 131. Numerical audit 109: theory audit 134. The linear-estimates reviewer's shell review: theory audit 135.
      numerical audit 113: theory audit 136. Numerical audit 116: theory audit 137. Numerical audit 118 and closure review 015: theory audit 139. Numerical audit 119, numerical audit 120: theory audit 142. Numerical audit 115: theory audit 144.
      theory exchange 02 section 8 (multi-scale decay): theory audit 149 (CONFIRMED). The linear-estimates reviewer the review of theory audit 146 Remark review 1 (joint
      ceiling): theory audit 165. theory exchange 02 lines 347 to 349: theory audit 148 (REFUTED as
      an inference). Numerical audit 128, numerical audit 129: theory audit 150. Numerical audit 124 to numerical audit 127: theory audit 151. closure review 016: theory audit 152.
  - Own proofs reviewed by another worker:
    - theory audit 007, by the theory team and the linear-estimates reviewer.
    - theory audit 017, by the linear-estimates reviewer and the theory team.
    - theory audit 019, by the linear-estimates reviewer (theory audit 035).
    - theory audit 041, by the theory team (closure review 008). Theory audit 051, by the theory team (closure review 009, theory audit 057). Theory audit 014, by the linear-estimates reviewer (theory audit 056). Theory audit 004, by the linear-estimates reviewer
      (theory audit 062). Theory audit 054, by the theory team (closure review 010, theory audit 071). Theory audit 047, by the theory team (closure review 011, theory audit 080). Theory audit 060, by the theory team (closure review 012,
      theory audit 091). Theory audit 058, by the linear-estimates reviewer (theory audit 095). Theory audit 081, by the linear-estimates reviewer (theory audit 109). Theory audit 097, by the theory team (closure review 013, theory audit 114). Theory audit 107, by the theory team
      (closure review 014, theory audit 120). Theory audit 127, by the theory team (closure review 015). The theory audit 056 shell estimate, by the linear-estimates reviewer (theory audit 135). Theory audit 128, theory audit 130,
      theory audit 133 with its LDL criterion and theory audit 138, by the theory team (closure review 016; theory audit 128 (2) AUDITED conditional). Theory audit 145 and
      theory audit 146 with the theory audit 147 application, by the theory team (closure review 017, accepted in theory audit 154; theory audit 140 is the alpha_v case of
      theory audit 145) and by the linear-estimates reviewer (second review, theory audit 164). The linear-estimates reviewer's localized (B-L2) note: theory audit 157 (L1, Lemma C, L2 CONFIRMED), theory audit 158 (REFUTED), theory audit 159 (partial),
      theory audit 168 (L3 CONFIRMED), theory audit 169 (REFUTED as a universal claim), theory audit 170 (OPEN). The linear-estimates reviewer the review of theory audit 145 Remark review 1
      (B > 0 frozen strip is residual spectrum): theory audit 171 (CONFIRMED).
      theory audit 153, by the theory team (closure review 018, accepted in theory audit 160). Theory audit 163 (symmetric weighted coupling), by the linear-estimates reviewer (theory audit 174).
      theory audit 170 (compact orbit weight), by the theory team (closure review 020, theory audit 180). Theory audit 094 (growing-weight obstruction), by the linear-estimates reviewer (theory audit 179;
      sign correction theory audit 181). The linear-estimates reviewer's weighted estimate 4 weak proposition: theory audit 172 (CONFIRMED). The linear-estimates reviewer the review of theory audit 170 review 1 (orbit-weight
      Lipschitz bound under Sym DV >= mu I): theory audit 183 (CONFIRMED). Theory audit 176 (annular coupling), by the linear-estimates reviewer (theory audit 186). Theory audit 182
      (007 optimized weak probe), by the theory team (closure review 021, theory audit 184; number CONFIRMED by numerical audit 152). The linear-estimates reviewer's directed floors:
      theory audit 187 (CONFIRMED at component level). Theory audit 185 (007 n = 7 probe), by the theory team (closure review 022, theory audit 190;
      number CONFIRMED by numerical audit 157, theory audit 196). Theory audit 177 and theory audit 178 (growing-weight velocity, Bessel tail), by the linear-estimates reviewer (theory audit 192,
      theory audit 191). Theory audit 189 (weak tail exponent pinning), by the theory team closure review 023 and the linear-estimates reviewer (theory audit 200); theory audit 201, theory audit 202 CONFIRMED.
      theory audit 197 CONFIRMS the coordinator's sharpw arithmetic for 007. Theory audit 203 (007 leading profile) CONFIRMED by numerical audit 165; theory audit 204
      CONFIRMS numerical audit 155's 012 point values (accepted in numerical audit 167); theory audit 207 CONFIRMS the numerical auditor polar third-tensor method and the
      007 Q3 record. Theory audit 199 AUDITED (the theory team closure review 024, theory audit 212). Theory audit 209
      CONFIRMS numerical audit 164 (constraint rank 426). Theory audit 210 (common leading profile of state 131, d2, 005 to 012) CONFIRMED by
      numerical audit 172 (theory audit 213). Theory audit 211 (exact Taylor repair of 007, density change < 3.424e-12): arithmetic CONFIRMED by
      numerical audit 173 (theory audit 227), theorem CONFIRMED by the theory team closure review 028. Theory audit 205 and theory audit 206 AUDITED (the theory team closure review 025, closure review 026; theory audit 220,
      theory audit 223); theory audit 224 (sharp constant of theory audit 206) CONFIRMED analytically. Theory audit 221 CONFIRMS closure review 025 review 1 and R3; theory audit 222
      (finite tail amplitudes contain the fixed-c dilation orbit of 007) CONFIRMED by the theory team closure review 027, its numbers by
      numerical audit 177 (theory audit 226). Audit of theory exchange 03: theory audit 214 and theory audit 218 CONFIRM; theory audit 215, theory audit 216, theory audit 217 and theory audit 219 REFUTE the
      full-span Gram matrix, the one-condition defect feasibility, the non-strict closed-ball exclusion and three
      summary deductions (the theory team adopts the repairs for theory exchange 04). Theory audit 225 CONFIRMS numerical audit 176 (008 distance); theory audit 228
      CONFIRMS numerical audit 178. Theory audit 229 (coordinate-invariant damping lemma) AUDITED (the theory team closure review 029, theory audit 239); theory audit 222 AUDITED
      (theory audit 232); theory audit 211 AUDITED, with membership in the frozen 007 span at c = c_007 only (theory audit 233); theory audit 194 AUDITED
      (the linear-estimates reviewer review, theory audit 237). Theory audit 230 CONFIRMS numerical audit 175 (exact quotient map); theory audit 231 CONFIRMS numerical audit 179 (009 distance);
      theory audit 236 CONFIRMS numerical audit 182 (012 distance); theory audit 238 CONFIRMS numerical audit 180 (sharpw ratio > 3596535.57) and numerical audit 181. Theory audit 240
      and theory audit 241 REFUTE two statements of the theory team closure review 029 R3 (the theory team accepts both, theory audit 247). Theory audit 234 (forced tail
      profiles) AUDITED (the theory team closure review 030, theory audit 246); theory audit 252 accepts numerical audit 189, so theory audit 235 (007 satisfies them) is CONFIRMED.
      theory audit 243 and theory audit 245 CONFIRM the linear-estimates reviewer's weighted-hierarchy remarks, theory audit 244 REFUTES two unqualified statements of
      them (no verdict changes). Theory audit 248 and theory audit 250 CONFIRM numerical audit 186 and numerical audit 187 (008 and 009 dyadic cells). Theory audit 254
      accepts the linear-estimates reviewer's second review of theory audit 234. 013: theory audit 253 (exact source conversion and frozen probes, OPEN), theory audit 255
      (held-out probe distance, CONFIRMED by numerical audit 204, theory audit 264), theory audit 263 CONFIRMS numerical audit 200, theory audit 266 CONFIRMS numerical audit 201. Theory audit 257
      CONFIRMS numerical audit 190 (accepted in numerical audit 203), theory audit 265 CONFIRMS the theory audit 251 candidate arithmetic (numerical audit 198), theory audit 267
      CONFIRMS numerical audit 191. Audit of the final theory report in the accompanying artifacts version3: theory audit 258, theory audit 259 and theory audit 260 REFUTE a finite-rank Woodbury
      sentence, the selected forcing-space inclusion and the localized-route exception; theory audit 261 CONFIRMS; theory audit 262 asks
      to relabel the scalar budget table as family ceilings (fixed-ball radii 1.435546875e-6 and 1.3193359375e-6).
      theory audit 268 accepts the linear-estimates reviewer's independent review of theory audit 249, so the weighted forced-tail classification is AUDITED.
      theory audit 269 accepts the theory team's independent review closure review 031, so theory audit 251 (affine Taylor lift, every nonzero real c with
      (a-4c+2)(a-8c+4) != 0) is AUDITED. Theory audit 270 CONFIRMS numerical audit 205 (010 mode 7 distance > 0.022479506978) and theory audit 274
      CONFIRMS numerical audit 207 (mode 1, > 0.00062746942). Theory audit 271 accepts the linear-estimates reviewer's review of theory audit 256, so finite
      polynomial-logarithmic tails add no tail parameters (AUDITED); theory audit 272 corrects the scope of one review sentence.
      theory audit 273 REFUTES the numerics exchange 07 inference that two damped trials give a span floor (as numerical audit 211). Theory audit 275
      CONFIRMS numerical audit 195 (the q4 first-sine term omitted by the numerics team's far-field model). Theory audit 276 CONFIRMS numerical audit 209 (whole-plane
      first-sine pairings of 007 and the actual far-field model errors) by an independent polar computation. Theory audit 277
      (AUDITED through the theory team closure review 032 and the linear-estimates reviewer the review of theory audit 277) REFUTES localizing only the low-energy row of a graded box with the original high-row margin (every such box
      has ||h||_2 < 25/54684). Theory audit 278 CONFIRMS the annular lemma of the theory exchange 04 version (fixed-ball bound
      below 1.312585972e-6) and REFUTES its parameter-family ceiling 2.834998772e-6 (repair: below 2.839272409e-6;
      the truncated decimals 1.312585971e-6 and 2.839272408e-6 printed earlier are below the cited right sides, theory audit 286). Theory audit 279
      CONFIRMS numerical audit 213 (014 point gaps) and theory audit 280 CONFIRMS numerical audit 214 (014 distance). Theory audit 281 (AUDITED through the theory team
      closure review 033, theory audit 296): 007, 013 and 014 admit no compactly supported L^2 correction to an exact solution in the canonical
      fixed-c chart (each keeps an exactly nonzero first descendant residual coefficient, while a compact correction
      has exterior velocity of order r^-3); corrections with nonzero tails are not excluded. Theory audit 282 CONFIRMS numerical audit 216
      (six complete large-index 007 weak records, a finite list). Theory audit 283 accepts the linear-estimates reviewer's review of theory audit 259, so theory audit 259 and
      the theory audit 258, theory audit 260 to theory audit 262 repairs are AUDITED. Theory audit 284 CONFIRMS the linear-estimates reviewer's conditional forcing comparison
      (kappa = 2.0188503652... at K = 10^6, so X <= 2.018851 N; enlargement 163.88). Theory audit 285 CONFIRMS numerical audit 222 and numerical audit 225
      (for every integer K >= 3000000 the complete first-sine weak test of 007 is at most 0.00363271755, below the
      mode 7 distance). Audit of theory exchange 04 (theory audit 286 to theory audit 290): all 33 candidate ratios CONFIRMED as strictly
      conservative, also with the exact graded ceiling 25/54684 (theory audit 289); section 5.2 AUDITED (theory audit 287: the positive
      leading-amplitude ray is the dilation class, and the distance from the dilated reference scales by lambda^2);
      theory audit 288 REFUTES dilation invariance of a distance-to-budget ratio from norm homogeneity alone; theory audit 289 REFUTES the
      deductions that optimized probes no longer measure the distance, that stalled optimization proves no basis
      leverage, and that no tail-exponent rule chart exists (none has been constructed in this program); theory audit 286 records three
      downward-rounded decimals; theory audit 290 accepts both reviews of theory audit 277. Theory audit 291 CONFIRMS the linear-estimates reviewer's weighted-tail
      thresholds (the review of theory audit 249 R3): the necessary weighted-tail condition excludes a <= 2 gamma (state 131),
      a <= 7 gamma - 5 (d2, Mpen2) and a <= 4 gamma - 4 (005, 007); theory audit 292 (CONFIRMED by numerical audit 240, accepted in theory audit 308) finds
      threshold 4 gamma - 4 for 006, 008, 009, 012, 013 and 014; theory audit 293 REFUTES the upward-rounded theory exchange 04
      decimals -1.133278617 and -1.790444924 (safe values -1.133278618 and -1.790444925). Theory audit 294 and theory audit 295 (forced
      integrable tail; exact cancelling direction for the first integrable descendant) are AUDITED (theory audit 315).
      theory audit 296 accepts the theory team's closure review 033, so theory audit 281 is AUDITED. Theory audit 297 reconstructs the 015 structure (matched by
      numerical audit 233). Theory audit 298 CONFIRMS the numerical auditor's 015 held-out distance > 0.000351804115950603 (n = 19, K = 600) and theory audit 299
      CONFIRMS numerical audit 234 (015 point gaps).
      theory audit 242 (weighted second-moment Hessian bound ||(1 + r^2/R^2) D^2 U[h]||_2 <= ((1 +
      6^(1/2))/2) ||(1 + r^2/R^2) D^2 h||_2 for real centrally odd compactly supported h): AUDITED (the linear-estimates reviewer the review of theory audit 242 accepted
      in theory audit 300). Theory audit 301 CONFIRMS the review's S1 constant, squared 63/32 (below 1.40313), and its parity
      counterexamples (radial family with squared limit 33/10 > ((1 + 6^(1/2))/2)^2). Theory audit 302 (squared S1 constant
      185/96, so below 1.388195) is AUDITED (the linear-estimates reviewer the review of theory audit 302 accepted in theory audit 309). These are operator constants,
      not inverse estimates. Theory audit 303 CONFIRMS numerical audit 231 (010 dyadic cells), so row 79 is RULED OUT for the scheme.
      theory audit 304 CONFIRMS numerical audit 237 (015 distance > 0.001232449584356253 at (23, 600)); theory audit 305 CONFIRMS the review of theory audit 281 R2;
      theory audit 306 accepts theory audit 297 against numerical audit 233; theory audit 307 CONFIRMS numerical audit 242 (016 point gaps); theory audit 308 accepts numerical audit 240; theory audit 310 CONFIRMS numerical audit 246 at (23, 2400) (016
      distance > 0.001092633159, row 80 RULED OUT in every ball) and theory audit 311 at (19, 1800) (> 0.001470360924);
      theory audit 313 CONFIRMS the 016 sector flags; theory audit 314 (far-out tail repair) is AUDITED through the theory team's closure review 035
      (theory audit 325), and theory audit 326 CONFIRMS closure review 035 remark (b) on its weighted residual cost. Theory audit 315 accepts
      the linear-estimates reviewer the review of theory audit 294 and the theory team closure review 034 (theory audit 294, theory audit 295 AUDITED); theory audit 316 CONFIRMS the theory audit 295 repair norms above
      4373.34; theory audit 317 and theory audit 318 CONFIRM the linear-estimates reviewer's dipole forced-tail extension and decay obstruction. Theory audit 319
      CONFIRMS numerical audit 254 (017 point gaps) and theory audit 320 CONFIRMS numerical audit 256 (017 distance > 0.001068502321 at (23, 2400)),
      so rows 82, 83 are RULED OUT in every ball. Theory audit 321 CONFIRMS numerical audit 248 (016 potential rank 2174, mode 17).
      theory audit 322 (no additional density gauge in the radius-scaled spaces) is AUDITED through the theory team's closure review 036
      (review set 33 sha256 16f47743..., accepted in theory audit 332): both scaled spaces have potential and density rank
      2174. Theory audit 328 to theory audit 330 audit the final theory report in the accompanying artifacts version 12 and numerics exchange 09: all 42 displayed ratios CONFIRMED; the
      indexed list of nonautomatic L^2 cancellations is (2,0), (3,0), (4,0) under the global index (REFUTED as
      written, no exclusion changes); the numerics exchange 09 deductions of an earlier span floor and of a finite mode band
      for the residual mass are REFUTED; the forced second tail needs its growth and H_q2 hypotheses stated, and the
      cutoff radius 45174.312 is FLOAT (theory audit 329). Theory audit 331 CONFIRMS numerical audit 257. Theory audit 323 CONFIRMS the
      complete 017 far-field sector prefix. Theory audit 324 (removal of the (4,1) and (9,0) tails by two cutoffs) has the linear-estimates reviewer's
      independent review (the review of theory audit 324, CONFIRMED; current sha256 81741e5c... after the 08:00Z revision of its
      remark R3) and is AUDITED: The theory auditor accepts the review in theory audit 337 and rechecks the exact 007 coefficient
      reconstruction of both repairs; the numerical cutoff constants and radii remain FLOAT. Theory audit 335 (AUDITED: The linear-estimates reviewer's
      the review of theory audit 335 CONFIRMS every step and the theory auditor accepts it in theory audit 350): for centrally odd C^1 corrections with H_q finite, -5 < q < -3, the canonical velocity is minus the
      first-moment dipole term up to E_q H_q(h) r^q; at q = gamma - 4 this gives the leading coefficient of a
      stationary correction and excludes faster weighted C^1 corrections when A is not in the span of P, under
      endpoint reference hypotheses that no current reference meets yet. Theory audit 336 audits the final theory report in the accompanying artifacts version 15:
      repairs and all 42 ratios CONFIRMED; the sentence that both cutoffs change (5,1) is REFUTED (only the first
      does); version 17 (08:03Z, sha256 b824beaf...) repairs it (its erratum 57), and theory audit 341 CONFIRMS the repair and
      all 42 ratios of version 17. Theory audit 338 CONFIRMS the linear-estimates reviewer's remarks R2 and R3 under explicit finite angular, remainder
      and growth hypotheses: finitely many cutoffs remove every residual sector above a fixed nonresonant exponent at
      arbitrarily small L^2 cost; its third cutoff (the theory auditor's own construction, AUDITED since theory audit 365 accepted
      sections 2 and 3 of the linear-estimates reviewer's review of theory audit 338) removes (5,1) for 007, 013 and 014 and leaves (1,2) as the sole
      leading sector. Theory audit 339 (AUDITED since theory audit 365; its other dependency, theory audit 335, is AUDITED since theory audit 350):
      the three-cutoff references then admit no stationary weighted C^1 correction decaying
      faster than r^(gamma - 4); a fourth cutoff can remove the endpoint, so no obstruction to finite reference
      design is claimed. Theory audit 340 audits the 08:02Z the final numerics report in the accompanying artifacts version: its span-floor, mode-mass, Gauss-Newton
      plateau and quadrature-accuracy statements and its all-snapshot, all-ball scope are REFUTED as inferences; every
      exclusion stands. Theory audit 342 CONFIRMS the 018 point residual (0.09587881446813860 to 0.09587881446813861 at
      (1/10, 73/100)), the six scalar gaps and the uniform graded gap above 0.07547297250468689 by an independent
      polar construction (origin normalization not covered); theory audit 343 CONFIRMS the complete 16-sector prefix of 018.
      theory audit 344 REFUTES the broader readings that the theory audit 338 third-cutoff application and theory audit 339 are AUDITED and that
      equations (6), (7) of theory audit 335 hold below the reference radius (they hold for r >= R0). Theory audit 345 CONFIRMS the 018
      distance from the registered probe (19, 1800): radius in (0.0016558257920560614, 0.0016558257920560616).
      theory audit 346 CONFIRMS the exact origin normalization of 018 (c + partial_y u2(0) = 1, positive density slope; 24
      contributing generators). Theory audit 347 CONFIRMS the final theory report in the accompanying artifacts version 21 and its 48 ratios and REFUTES one phrase (018's
      point gaps cover the six tested scalar balls and the original graded bound; the wider exclusion follows from
      theory audit 345). Theory audit 348 CONFIRMS numerical audit 274: the abstract space with both legqs scales has potential and density dimension
      exactly 2426; shape matching for an actual mixed snapshot is OPEN. Theory audit 349 CONFIRMS the 018 distance from the
      registered probe (23, 2400): radius in (0.0013280160446381137, 0.0013280160446381139), weaker than theory audit 345.
      theory audit 351 CONFIRMS the linear-estimates reviewer's additions R2 and R3 to the theory audit 335 review under the full endpoint hypotheses (|m| <= mu H
      with mu < 5.04423; weighted C^1 budget above 33917 for each angular pair; a two-parameter L^2 closure
      inequality) and shows that with the current constants the inequality cannot prove an L^2 distance above
      9.28e-11, far below the registered budgets; this bounds the reach of the test, not a distance. Theory audit 375
      (CONFIRMED for Sections 1 to 4 by the linear-estimates reviewer's review of theory audit 375 at 10:19Z, repaired with a revision history by 10:46Z
      and accepted again by the theory auditor in theory audit 398, 10:49Z, and its second revision with outward-rounded displays in theory audit 404,
      11:11Z, common displayed Ecrit cap 0.6819391; AUDITED since theory audit 385, 10:20Z, in which
      the theory auditor accepts the review and REFUTES only its inference from a FLOAT minimax grid to an exact saddle) adds the gradient part of the weighted C^1 budget, H_q >= sup sqrt(q^2 b^2 + b'^2),
      giving H_q > 328627 for the three-cutoff 007, 013, 014 data and a reach below 3.752e-16. Theory audit 380 CONFIRMS the
      pointwise form computed in the linear-estimates reviewer's review script (H_q > 999775, 999745, 999748 for 007, 013, 014): the
      inequality reaches the fixed sharpw radius 1351/1024000000 only if E < 0.785064 and the family ceilings only if
      E < 0.682, 0.648, 0.27 (sharpw, sharp Sobolev, graded); these are necessary conditions. Theory audit 381
      (CONFIRMED as stated by the theory team's closure review 040, review set 38; the linear-estimates reviewer's review of theory audit 375 R4 derives the same bound
      independently, and theory audit 386 accepts R4; theory audit 391 accepts closure review 040, so theory audit 381 is AUDITED in full, including the
      retained-delta integral of Section 3) proves the lower bound
      (-q-1)/(2(-q)(-q-3)) = 0.7930365... for every universal constant of
      theory audit 335 (1), from the non-stationary test function y(1+r)^(q-1)/(-q); so this test cannot reach the fixed
      sharpw radius for 007, 013, 014 (crude cap below 1.2485e-6; below 1.421e-7 with the Section 3 shape), while
      PDE-specific estimates stay open. Theory audit 384
      (CONFIRMED by the linear-estimates reviewer's review of theory audit 381 and theory audit 384, 10:38Z, 964eb741...; AUDITED since theory audit 396, 10:42Z) extends this
      to smooth S1 functions with c[h] = 0 and any positive L2 budget (at R = 10000: E > 0.79303648 with
      L2 < 2.028e-11), so normalization and a small L2 budget do not lower the constant; a stationary-only
      estimate remains OPEN. Theory audit 396 also REFUTES the review's claim that every displayed cap is rounded upward;
      the stored intervals and the common caps 1.421e-7 and 1.124e-7 stay valid; theory audit 401 (11:00Z) accepts the
      revised review (5fa23303...). Theory audit 397 (10:45Z; CONFIRMED as stated by the theory team's review closure review 042, 11:13Z,
      review set 40 3c0c801e..., 24 independent checks; AUDITED since theory audit 409, 11:20Z, in which the theory auditor accepts the review) shows that the same constant persists for every 0 < s < 2 in the full fractional
      X_(s,w) ball of any positive radius together with the L2 ball, with any prescribed H_q = Hstar > 0; it uses
      no stationary equation. Theory audit 402 (11:06Z, audit record profile-specific velocity audit in the accompanying artifacts, proof a98e64b0..., result
      b8d33a7e...; CONFIRMED by the linear-estimates reviewer's review of theory audit 402, ffb49200..., saved 11:30Z (earlier report versions cited
      bd0a294b..., a file state read at 11:28Z), with its own exact recomputation and Arb bounds sqrt(max T) <=
      0.5822393; AUDITED since theory audit 413, 11:38Z, proof 3f5da531..., result c2d87d38..., 46 checks) shows, for -5 < q < -3 and h with
      finite H_q whose rescaled tail converges uniformly to a finite odd sine polynomial, the uniform limit of the
      compensated exterior velocity, and bounds its magnitude by (583/1000) H_q on the endpoint subspaces of 007,
      013 and 014; no finite-radius remainder follows. The review computes the room for one: a proved remainder
      rho with rho/H_q < 0.09893906 (V = 0) or 0.06417774 (V >= |U_lead(0)|) would pass the cutoff-radius test for
      the sharpw and sharp Sobolev family caps of theory audit 380, never for the graded cap 0.2694175, and the C0 tail bound of
      theory audit 335 (7) suggests rho/H_q of order 0.1 to 0.3 (not a bound). Theory audit 413 states that this test is necessary, not
      sufficient, for the complete radial integral. Theory audit 414 (11:39Z, audit record profile-velocity cap audit in the accompanying artifacts, proof
      0e0f608d..., result e94368ca..., 94 checks at 768 bits; the theory auditor's own application of the audited identity
      theory audit 381 (8); AUDITED since theory audit 423, below) integrates the positive part of that identity with
      E = 583/1000, zero remainder and V = 0 and finds that the closure inequality reaches at most 7.6399937715e-7
      (007), 7.6421438838e-7 (013) and 7.6407721072e-7 (014), below the smallest target 1.3193359375e-6 (fixed
      sharpw radius); the necessary common upper bounds on E are 0.527596, 0.458292 (sharpw family), 0.434940 (TB)
      and 0.181070 (graded). This limits the 583/1000 certificate only; it is no velocity lower bound and no
      nonexistence statement. The linear-estimates reviewer's review of theory audit 414 (final save 12:08Z, 221b1135..., restored by the linear-estimates reviewer at 12:30:37Z, script the review script for theory audit 414 in the accompanying artifacts
      c94546ab..., 204 checks, results ff9b562e...; the theory auditor's code read, not run) CONFIRMS theory audit 414: the bound and the
      thresholds by hand and exact sympy checks, the application by an independent Arb recomputation agreeing with
      the result record in the accompanying artifacts to relative 1e-35. The theory auditor accepts the review in theory audit 423 (12:12Z, proof 865eb842..., result
      f99be881..., checker 9d88dfc9..., all 212 own checks, all 204 peer numerical comparisons and seven algebraic
      identities), so theory audit 414 and its 583/1000 full-integral obstruction are AUDITED. The theory auditor froze the linear-estimates reviewer's 12:06Z save
      (20ee1bb3...), which differs from the 12:08Z save only in the printed digits of one constant and the save line. The review corrects
      the review of theory audit 402 section 4 (the (F2) room came from the crude cap (7); with (8) the answer for 583/1000 is no)
      and gives the room that 93/250 would leave: at most 0.0863 (sharpw, V = 0), 0.0515 (sharpw, V >= v0), 0.0629
      (TB, V = 0) and 0.1556 (fixed sharpw radius, V = 0), none for graded. Theory audit 415 (11:46Z, audit record pointwise profile-velocity audit in the accompanying artifacts, proof 57110fd5..., result
      bd9d38cb...; the theory auditor's own finite certificate on 61440 rectangles at 192 bits with positive Arb lower gaps,
      AUDITED via the linear-estimates reviewer's review of theory audit 415 and theory audit 434, below) states sup|V_q[f]| <= (93/250) sup sqrt(q^2 f^2 + (f')^2) on the
      exact endpoint spans of 007, 013 and 014, so E = 0.372 may replace 0.583; this is below the theory audit 414 thresholds
      for the fixed sharpw ball, the sharpw family and TB and above the graded threshold 0.181070. It gives no
      finite-radius remainder and no H_q bound. Theory audit 422 (12:03Z, proof fb03764b..., result 2d23b763..., 59 checks
      at 768 bits; the theory auditor's own, CONFIRMED by the review of theory audit 415 with 114 own checks, AUDITED via theory audit 434) integrates the retained shape with E = 93/250, V = 0
      and zero remainder: caps 8.913980874769618785e-6 (007), 8.916489523349172026e-6 (013) and
      8.914888999746365613e-6 (014), about 6.756 times the fixed sharpw radius, 3.128 times the sharpw family
      ceiling, 2.350 times TB and 0.0195 times the graded ceiling; a hypothetical ceiling conditional on theory audit 415,
      not a distance certificate. The linear-estimates reviewer's review of theory audit 415 (the review of theory audit 415 in the accompanying artifacts, saved 12:37Z,
      ee7b1b1b...; script the review script for theory audit 415 in the accompanying artifacts 0604be55..., results 59034a6c...; a rerun of a byte-identical
      worker copy of the theory auditor's the verification script in the accompanying artifacts) CONFIRMS theory audit 415 (1) for 007, 013 and 014 by hand checks of the reduction and
      of the error bounds and by three Arb checks with outward rounding (the rerun reproduces every saved row,
      the linear-estimates reviewer's own F and Q give a positive bound at all 61440 rectangles, and an independent certificate with other
      grids passes); it CONFIRMS the consequence (2) under its hypotheses (asymptotic: no finite radius, no H_q
      bound) and theory audit 422 (114 own checks). No certificate of (1) can use a constant below 0.3714757, 0.3714938 or
      0.3715026 (Arb, one rational direction per reference). With the theory audit 335 (7) tail input the remainder lower
      bound is at least 46.06 times (sharpw ceiling), 66.54 times (TB) and 22.19 times (fixed sharpw radius) the
      room that 93/250 leaves, for R <= r_beta, and theory audit 425 covers larger R. The review replaces the pointwise
      step of the review of theory audit 414 section 4, third bullet, by theory audit 425's radial average (conclusion unchanged), and notes
      that the final theory audit 415 run has no launch record or log of its own, which does not affect validity because
      the rerun reproduces it. The theory auditor accepts the review in theory audit 434 (12:50Z, proof 8848da16..., result
      1b36315e..., checker 006d79dd..., 341 further checks at 384 bits; its own reconstruction of the review's independent
      17-cell certificate passes all 78336 rectangles and 24576 denominator cells), so theory audit 415 and theory audit 422 are
      AUDITED. Theory audit 434 states the scope of the sharpness bound (the whole two-dimensional span; a stationary
      restriction or a larger independent H bound could change the comparison) and distinguishes the review's
      256-bit gaps, which agree with the saved 192-bit gaps to relative 1e-8, from the byte-identical 192-bit
      replay; it dates the 11:44:12Z and 11:44:13Z launch and log to the E = 3/8 trial and asserts no separate
      historical launch or log for the final 11:45:02Z result. Theory audit 410 (11:23Z,
      audit record two-weight velocity-remainder audit in the accompanying artifacts, proof cd2e6f18..., result 4763413e..., 20 checks; CONFIRMED as stated
      by the theory team's closure review 043, review set 41 93b48e74..., 11:55Z, the script for theory audit 410 in the accompanying artifacts a359eff8..., 22 checks; AUDITED since
      theory audit 424, 12:12Z, proof 0c2d360a..., result dec925fb..., checker 219c2c52..., in which the theory auditor accepts the review
      for theory audit 410 (1), (2), (4), (5), (7), (8) and (9), the finite-point values A12, C1 and C2 being FLOAT diagnostics,
      and prints outward rounding repairs to closure review 043 that change no theorem or obstruction) gives an explicit finite-radius error J(R) for the compensated velocity of a
      two-weight remainder; its H and remainder inputs are not supplied for any reference. The linear-estimates reviewer's
      the review of theory audit 410 (df28b508..., 11:53Z; main obstruction AUDITED by theory audit 421) takes the input (6) from
      theory audit 335 (7), the only proved tail bound for these references, and finds J(R)/H_q >= 3.974970 (007), 3.974957
      (013) and 3.974975 (014) at the sharpw ceiling for every R0 >= 2 and R in [L0, r_beta], more than 40 times the
      (F2) room 0.0989, and above Ecrit <= 0.6819391, so the obstruction claimed there holds for any limiting
      coefficient; a tail bound with all exponents above about 1.05 (FLOAT) or a separate multipole treatment of the
      inner part could change it. By the review of theory audit 414 this lower bound also exceeds the necessary thresholds
      themselves (factors 6.54 to 55.6), and a remainder starting beyond r_beta fails as well. The theory auditor's theory audit 421
      (12:03Z, proof 93f00180..., result 54e4b223..., all 180 finite checks at 768 bits) re-derives the lower bound
      and CONFIRMS the main obstruction (J/H >= 3.974970, 3.974957, 3.974975 at the sharpw ceiling, above the
      allowed absolute constants by factors greater than 5.829); it REFUTES the review's assertion that a general
      starting radius must satisfy R <= r_grad (only max(R, r_grad) <= r_beta is necessary, and the main
      obstruction uses only R <= r_beta); the FLOAT threshold searches and the two ways out stay OPEN. closure review 043 step 9
      obtains the obstruction independently (remainder above 3.16 H_q on [L0, 13761.58] and above 2.74 H_q on
      [L0, 18860]). The theory auditor's own theory audit 425 (12:14Z, proof 4d13c623..., result 69f36c4a..., checker a90f3228..., 109
      checks CONFIRMED by its own run; the analytic extension is CONFIRMED by the theory team's closure review 045, 12:27Z,
      review set 43 dcd62d66..., the script for theory audit 425 in the accompanying artifacts a70a1512..., 16 checks; the theory auditor accepts the review in theory audit 432,
      12:34Z, proof c2035403..., result 9c46cc69..., 190 own checks at 768 bits, so theory audit 425 is AUDITED) extends the obstruction to radius-dependent coefficients, including pointwise splicing of theory audit 410
      parameters, by averaging the coefficient in the radial Green integral, without assuming R <= r_grad; by
      closure review 045 remark review 1 it also holds without the hypothesis A410 >= H(1 + L0)^eps, provided V >= 0, G >= g0 and
      E >= Emin; theory audit 432 derives this independently (the average of the outer-only envelope is strictly above
      0.79303648 at each r_beta) and notes that it takes the present tail-list coefficient as an input and that
      dropping the inner amplitude is an optimistic obstruction calculation, not an admissible remainder bound.
      The theory team's closure review 044 (review set 42, locked file f4c2e327..., 12:20:33Z; the script for closure review 044 in the accompanying artifacts e5077202...,
      7 checks) shows that a separate multipole treatment of the inner part does not help with this tail input:
      the radius-averaged outer contribution alone is more than 4.34 times the required cutoff. The theory auditor's theory audit 426
      (12:24Z, audit record outer-remainder audit in the accompanying artifacts, proof 935e166f..., result fd5cc1d1..., checker
      280c4517..., 316 checks at 768 bits) CONFIRMS closure review 044 with two literal repairs (the fallback average with the
      relaxed u = 0.793 is above 0.7929999, not at least 0.7930; 0.793 is a relaxed lower bound, the audited floor
      being 0.7930365064). It binds the theory auditor's copy 54f06c10... of the theory team's 12:20Z save; the theory team states that the locked
      file differs only in one line wrap, one rewording and the cited check outputs, carries the repairs as errata
      and accepts theory audit 426 (review record v46), so closure review 044 is AUDITED; theory audit 432 accepts all four errata, E4 included. Neither result is a lower bound on the velocity or
      a nonexistence statement. Combined (the review of theory audit 375 section 2, closure review 040; accepted by the theory auditor in
      theory audit 385 and theory audit 386): no constant valid in theory audit 335 (1) lets the theory audit 351 inequality reach the fixed
      sharpw radius or the sharpw, sharp Sobolev or graded family ceiling for 007, 013 or 014, so the universal-constant
      form of this test is RULED OUT as a route to those balls. The linear-estimates reviewer's R3 (AUDITED since theory audit 411, 11:32Z: The theory auditor's
      complete independent 128-bit certificate, audit record folded velocity upper-bound audit in the accompanying artifacts, proof e72bc63b..., gives
      E < 1.747261) proves the valid constant E_new <= 1.749109, so the best universal constant lies in
      [0.7930365, 1.747261]; this changes no closure, because the lower bound already exceeds 0.785064. The theory team's closure review 038,
      audited in theory audit 379, gives a screening rule, CONFIRMED under its hypothesis (S) (a certified bound
      tau >= ||R' - R_j||_2 with tau <= d_j - b rules R' out at ceiling b), and the necessary condition E sqrt(2 pi)
      H_max/B < Emax(b) for the theory audit 351 test under an a priori budget H_q* <= H_max, also CONFIRMED; its inference
      that no stationary a priori H_q budget exists is REFUTED (OPEN); the theory team carries the five repairs in review set 37
      and theory audit 383 accepts them. Neither yields a distance or an exclusion
      without a verified (S) and a certified difference norm. Theory audit 352 CONFIRMS
      the mathematical changes and all 51 ratios of the final theory report in the accompanying artifacts version 23 (version 23 repairs the 018 point-test scope
      and names both theory audit 339 dependencies) and the 48 ratios of the unpublished theory exchange 06 version, whose theory audit 339
      dependency list is REFUTED as incomplete (the third-cutoff application must be named). Theory audit 353 to theory audit 355
      CONFIRM the numerical auditor's numerical audit 279 for 019 independently (point fields and gaps, origin normalization, complete
      sixteen-sector prefix). Theory audit 356 reviews the numerics team's revision of the final numerics report in the accompanying artifacts version: the calibration, index,
      summary-scope, design-probe, exact-Newton, no-bracket and plateau-OPEN repairs are CONFIRMED; its completeness
      is REFUTED (surviving point-test and all-ball scope claims, density modes 17 to 31, unsupported old-span
      unreachability), and a new sentence denying any lower bound on angular mass is REFUTED, since a certified
      pairing with a probe in band B gives ||Pi_B F||_2 >= |<F, phi>| / ||phi||_2. No exclusion reverses.
      theory audit 374 audits the complete the final numerics report in the accompanying artifacts revision of 09:19Z (sha256 2aba9267..., 197 lines): it CONFIRMS
      the repaired scalar and original graded exclusions through 020 except 011, the restricted dyadic scope and
      the distinctions about finite probes, calibration and Newton diagnostics, and REFUTES the unrestricted use of
      the specialized annular bound 2.839272409e-6 (the 016 sharpw factor is above 515.9, not 518), the upward
      rounding of the 017 (23, 2400) certificate (safe floor 0.001068502321536437), universal point-gap and radius
      descriptions (accepted sharpw point ratios 4.558 for 007 and 3.048 for 009), causal deductions from finite
      trials, stale 020 summaries and the 021/022 held-out provenance. No exclusion changes. Its section 5
      full-tensor angular rule (ideal quadrant midpoint nodes, N >= 2M + 2 for F^2, |grad F|^2, the Hessian square
      and (Delta F)^2 at each radius; N >= 2M + 3 for separate Cartesian squares) is CONFIRMED by numerical audit 307 and
      accepted in theory audit 376; the adopted 180 nodes meet both at M = 79. It certifies no floating evaluation, radial
      error or continuum norm. The numerics team applied all eight theory audit 374 repairs to the final numerics report in the accompanying artifacts at 10:12Z (sha256
      6648ebd2...), before the 10:37Z due time. Theory audit 390 CONFIRMS requests 1 to 7 and the mathematical part of 8; it
      REFUTES the completion of 8 (the frozen header still says 09:08Z) and the new inference that a penalty of size
      25 against an objective of about 1.3e7 makes the 14 held-in rows of 021 inert (exact quadratic
      counterexample). No exclusion changes.
      theory audit 357 CONFIRMS the numerical auditor's numerical audit 282 for 019 independently (all 360 density and 360 stream polar terms, the 63
      complete moment groups, both pairings and all eight peer scalars; radius in (0.0016618069671932526,
      0.0016618069671932527)); it supplies neither a dyadic exclusion nor existence. Theory audit 358 CONFIRMS the endpoint
      statements of theory audit 335 and theory audit 351, the repaired theory audit 339 dependency, the conditional closure constants (in the
      same family formula with cU = 8/5 and w2 = 2^20, overcoming 007 needs C' < 775390625/2554506927217 < 3.04e-4)
      and all 108 ratio comparisons of the final theory report in the accompanying artifacts version 24 and the second theory exchange 06 preview; it REFUTES the v06
      preview sentence that 007 has all checks except H6 and L2 distance condition, since (A), (B0n), H3 and H4 are unchecked.
      theory audit 433 (12:45Z, proof 8f6f8232..., result e6de0e68..., 79 checks) audits the final theory report in the accompanying artifacts version 34: it CONFIRMS
      the changed theorem statements under their cited hypotheses and the closure and ratio arithmetic (high rate
      63092119/405000000, self-map slack 7/1557000000, family ceiling below 2.8496e-6), leaves OPEN the unrestricted
      reading of the sentence 'effective constant above 1.72' (it holds for the fallback 1.747261 only) and asks for
      eight status and wording repairs, which the theory team applies in version 37 (12:50:05Z, c550ffac...); version 38 (12:57Z,
      ccaa8623...) is audited in theory audit 442 below. Theory audit 437 (13:10:49Z, proof b7c3e467..., result 043acbe3..., 114 checks) audits
      the theory team's 24-factor table for theory exchange 08 (review record 47): it REFUTES the S2 lower bound (at (1/7744, 2^14,
      2^18) the sharp quantity lies in (516.9717852723, 517.5527701453); 756.5312630768 belongs to sharpw, so
      9925756.87 becomes 6782715.40) and the claim that all 24 factors are necessary for every closure proof, since
      chosen coefficients, sufficient tests, ball exclusions, universal-class obstructions and majorant failures have
      different quantifiers; it CONFIRMS the corrected comparisons in their separate scopes. Theory audit 442 (13:20:27Z, proof
      6d890545..., result 3f9e5256..., 548 checks at 512 bits) audits version 38: it CONFIRMS the changed conditional
      mathematics and the 016 seven-cell consequence (minimum ratio > 1.253908386497), REFUTES the printed equality
      lambda = 109.6024 (lambda is greater) and the upward-rounded inference N_1 >= 13.758676 (the two-projection
      value is 13.7586759794..., so the statement is > 13.75867597), and leaves OPEN the unqualified small-radius
      formula of section 9, which needs the piecewise r < 5 statement of section 3.4; six repairs are requested for
      version 39 (review record 220).
      theory audit 443 (13:26Z, the finite radius reach audit material in the accompanying artifacts, proof 972ac08e..., result ee10abf8..., 948 checks at 768
      bits) audits sections 1 to 4 of the linear-estimates reviewer's linear-estimates reviewer falsification review of the endpoint and the report summary revision 1: it CONFIRMS the new
      whole-integral bound and every numerical display, REFUTES three inferences (a coefficient that passes a
      necessary test does not disprove a universal obstruction; the 'exactly when' of section 1 holds in one direction
      only; the lower bound Emin belongs only to the relaxed numerical-envelope class) and leaves OPEN whether an
      improved valid universal constant reaches 2^-25 or 6.8626e-8; review record 221 lists five wording repairs. Theory audit 444
      (13:27:43Z, proof 630ccc8c..., result 9c8c940d..., 392 checks) accepts the numerical auditor's numerical audit 365 comparison of the 025
      structure and its qualification of the 'projection excluded' wording. The linear-estimates reviewer's revision 2 of the review (saved
      13:42:25Z, 224 lines, 660b089b...; the versions of this report from 13:49Z to 13:57Z printed a73eed2c..., the
      hash of an unfinished save) makes the five repairs; the theory auditor's theory audit 452 (13:55:51Z, proof 88b0ac35..., result
      9ab5d432..., 107 checks) CONFIRMS them and the unchanged finite consequences, and leaves OPEN whether an
      improved admissible universal coefficient reaches 2^-25 or 6.8626e-8. Theory audit 445 (13:34:59Z, proof 0eb9308d...,
      result a48fe7d1..., 333 checks) audits the theory team's unpublished theory exchange 08 preview1 (13:29:19Z, d8c8e8ba..., 769
      lines): it CONFIRMS all 24 corrected factors and table cells, the three-candidate kernel thresholds and the
      finite-radius bounds, accepts section 2 (g) (the two small-radius universal-constant questions are OPEN, not
      false) and asks for seven repairs before publication (review record 223), among them that 'every registered ball'
      be restricted to the registered scalar balls and original graded boxes and that rows S and numerics team be stated as
      obligations of the sharp and sharpw certificate only. Theory audit 453 (13:58:51Z, proof a2319328..., result 4fce0c45...,
      237 checks at 768 bits) audits the final theory report in the accompanying artifacts version 39 (13:47Z, 1897 lines, 28f5f6ce...): it CONFIRMS the changed
      conditional mathematics and the 22 numeric table rows, REFUTES the version's '026 OPEN' status (version 41, 13:59Z,
      e08cbf74..., records 026 as accepted both ways) and asks for four publication updates (cite theory audit 451 for 016;
      separate 016's accepted G0, rF and G1 from its P2 and actual H; display the normalized closure review 038 expression in
      section 0; attach the target scope to the radius-dependent obstruction). Theory audit 454 (14:06:02Z, proof bba85859...,
      result 43a549a4..., 166 checks) CONFIRMS the linear-estimates reviewer's exact family ceilings (review record BE): the rebalanced Sobolev framework budget
      is 3.51254748...e-7, so its upward display is 3.5126e-7 and the earlier display 3.5125e-7 was not an upward
      rounding; the six other scalar budgets lie in the one-unit bracket below their printed values and the graded
      ceiling between 45697/10^8 and 25/54684; no exclusion changes. Theory audit 455 (14:12:17Z, proof 8c1b6532..., result
      88262498..., 415 checks at 768 bits) CONFIRMS the changed mathematics of theory exchange 08 preview2 (13:55:03Z, 868
      lines, 5940b948...) and its exact-ceiling factors at 007: U4, P1 and P2 at least 2.9432, 2.0544 and 2.0515; R2
      and R3 at least 46.0752 and 66.5677 under H >= Phi; with only H >= H0, review 1 to R3 at least 22.1948, 46.0750 and
      66.5674. Theory audit 456 (14:19:23Z, proof 644e6d03..., result 60eb4f36..., 263 checks at 768 bits) CONFIRMS the changed
      mathematics of the final theory report in the accompanying artifacts version 43 (14:09Z, 1933 lines, a3b59ce9...), its 23 distance-table rows and the
      theory audit 453 and theory audit 454 repairs. Theory audit 457 (14:22:35Z, proof 4daf08a6..., result 5ab0c3be..., 233 checks) CONFIRMS
      the linear-estimates reviewer's exact floors of the historical ratio tables: 13 of 18 O3 values and 8 of 12 C4 values were one displayed
      unit above the exact floor, every corrected factor exceeds 1, the d2 sharpw factor is 1.03e5, and the graded d2
      quotient lies strictly between 646 and 647; it REFUTES the lower-factor reading of those 21 values and changes
      no exclusion.
      theory audit 458 (14:34:25Z, the theory auditor's own, proof 771ad6b4..., result f367ac93..., 896 exact checks) reconstructs from all
      860 raw rows of candidate 001 a nonzero leading residual at q = 2 gamma - 1 = 427123167131315/4076476460239181 > 0,
      in exact agreement with numerical audit 028, and a nonzero leading density; these exact checks are CONFIRMED. Its application
      of the AUDITED annular theorem theory audit 049, which would exclude every L^2 distributional stationary correction of 001
      at every c, was OPEN until a theory review; it is AUDITED since theory audit 465 (below), and matrix row 35 states it
      beside the nonmembership verdict. The linear-estimates reviewer's
      the falsification review in the accompanying artifacts revision 3 note (14:34:05Z, de588453..., CONFIRMED by theory audit 464) replaces the TB-rebal row of revision 2
      at the exact ceiling: over [3.5125e-7, 3.5126e-7] the threshold with H >= Phi and V = 0 is at most 0.6720590 and
      with V >= v0 lies in [0.6372593, 0.6372977], all below Etest = 0.7930365, so the verdict stands; the old lower
      end 0.6372628 is not a lower end at the exact radius.
      theory audit 459 (14:41:03Z, the theory auditor's own H18 coverage audit, proof 353fc157..., result 3b433eb4..., 806 checks) CONFIRMS
      that every snapshot 002 to 026 except 011 has an accepted fixed-c L^2 distance above 1/1000, above all eight
      scalar ceilings (each below 3793/10^9), the original graded ceiling 25/54684 and every trans and statL choice
      with a positive top margin. It corrects the scope for 001: residual nonmembership shows that the L^2 forcing
      schemes do not apply, not that no solution lies in a ball, so the sentence that no snapshot through 026 except
      011 has an L^2 solution in a registered ball was OPEN until theory audit 458's application was reviewed (AUDITED since
      theory audit 465); answer 6 above is worded accordingly. Theory audit 460 (14:48:10Z, proof 3a1dd301..., result c2d3cbc8..., 257
      checks)
      accepts numerical audit 383 and numerical audit 384, including 015's (23, 2400) floor ||h||_2 > 0.003033479200692324. Numerical audit 386 (14:42:04Z,
      result b808c527...) CONFIRMS the documentary links of all 105 comparison-table rows to the matrix and REFUTES
      this report's row 80 display > 0.0014704 (the accepted floor is 0.001470360924123708; repaired). The linear-estimates reviewer's review record
      BJ (14:43Z) states Proposition WU3, CONFIRMED by theory audit 462: at the registered floors the weight-uniform L^2
      budget is at most 1.1746 times the exact sharpw ceiling (beta 2) and at most 1.0612 times the exact sharp Sobolev
      ceiling (beta 11/4), so 007's distance factors stay above 1424.9 and 1184.9.
      Since matrix v137: theory audit 461 (14:52:08Z, the candidate015 dyadic audit material in the accompanying artifacts, proof 27cd1dc8..., result
      158a939a..., 739 checks) CONFIRMS numerical audit 382, so the 015 dyadic exclusion of row 105 is accepted both ways. Numerical audit 389
      (14:56:17Z) gives the 017 dyadic exclusion of row 106. Numerical audit 387 (14:49:46Z, result distance record 02 in the accompanying artifacts 9db8a391...)
      CONFIRMS the principal strict distance displays of 007, 008, 009, 010 and 012 to 026 against their accepted
      certificates and all 22 selected ratio displays, and REFUTES this report's displays > 0.0014704 (row 80) and >
      0.001864696855 (row 90 and short answer 1), which lay above the accepted roots; both are repaired to 0.0014703
      and 0.001864696854. The coordinator's own sweep for lower bounds printed above their exact values found the same two
      and corrects, in the matrix, the 017 (23, 2400) display to 0.001068502321 and the Ecrit cap to 0.6819391, and
      here the 007 seven-cell ratio to above 1.2342. The linear-estimates reviewer's review of theory audit 459 (14:54:57Z, e140e6c0..., 189 checks,
      review record BK) CONFIRMS theory audit 459 with its scope; its supplement on variable-margin L2 framework (beta_L <= 1 + c, every bL ball
      budget at most 4.1069e-6) is CONFIRMED by theory audit 462 (below).
      Since matrix v138: theory audit 462 (15:00:35Z, the weight uniform gram audit material in the accompanying artifacts, proof 3c871d7f..., result
      61803920..., 320 checks) CONFIRMS WU3 and the linear-estimates reviewer's bL supplement: seven scoped strict L^2 upper budgets hold
      uniformly over the weight pairs of the two stated Gram schemes, the bL budget covers every positive certifiable
      beta_L at every allowed weight pair, and every snapshot 002 to 026 except 011 lies outside those balls by a
      common factor above 243 (007 by at least 1161.2). Full-scheme sharpness stays OPEN; the weighted margin (B-L2-w)
      and the decaying-weight dyadic spaces are outside its scope. Theory audit 463 (15:05:10Z,
      the candidate017 dyadic audit material in the accompanying artifacts, proof 0e32cdb6..., result 96c4b875..., 1070 checks) CONFIRMS numerical audit 389, so the
      017 dyadic exclusion of row 106 is accepted both ways, with minimum ratio above 1.221854480167 on [1/4, 1/2]
      under the scheme's stated hypotheses. Theory audit 464 (15:07:14Z, the tb rebal endpoint audit material in the accompanying artifacts, result 75657839...,
      199 checks) CONFIRMS the falsification review in the accompanying artifacts revision 3 and REFUTES the old 007 lower end 0.6372628 as an exact-radius bound;
      the verdict of the TB-rebal row stands. Numerical audit 390 (15:02:32Z, the h18 coverage peer material in the accompanying artifacts, result record 02 in the accompanying artifacts f73dceb0...,
      825 checks) accepts theory audit 459's finite composition reciprocally and REFUTES reading nine nearest-rounded root lower-bound
      displays of the linear-estimates reviewer's review JSON as strict floors; no exclusion changes. The theory team's closure review 046 (review record v51,
      review set 44 1b7c425c..., the script for theory audit 458 in the accompanying artifacts, 912 exact checks) CONFIRMS theory audit 458 in the affine class rho + L^2 only
      (L^2 frameworks; not dyadic Y framework, weighted or non-L^2 repairs, or a changed far field); the theory auditor accepts it in
      theory audit 465 (below).
      Since matrix v139: The linear-estimates reviewer's review of theory audit 458 (15:06:51Z, ca936460..., 30 checks) CONFIRMS theory audit 458 independently by
      Wirtinger calculus and corrects the changed-c wording (the test must use G0, because E is orthogonal to G0).
      theory audit 465 (15:11:34Z, the candidate001 affine review material in the accompanying artifacts, proof a3dbba66..., result 96c9365d..., 957 checks)
      accepts both reviews, so theory audit 458 is AUDITED: no real L^2 correction of 001 is a stationary solution at any real c
      and any radius, with no symmetry, normalization, trace, smallness or derivative condition, and the same holds
      with a constant background velocity. It REFUTES the reading that changing q alone while keeping E gives the
      changed-c leading pairing, and it covers neither non-L^2 classes nor a changed far field nor a linear
      background. Theory audit 466 (15:13:48Z, the negative norm dual audit material in the accompanying artifacts, analytic audit, no code run) CONFIRMS the
      proof of the numerical auditor's negative-norm dual lower bound, REFUTES reading a dual value below a Hardy upper value as a
      confirmation of that upper value, and keeps every new 016 dual value OPEN. Numerical audit 392 (15:10:11Z, record
      f7e0202b...) CONFIRMS the norm-certification team's 016 P2 enclosure. Numerical audit 393 (15:10:46Z, result record 03 in the accompanying artifacts cb7906f6...), CONFIRMED by theory audit 467
      (15:18:52Z, result 5883ec4d..., 8874 checks at 2048 bits), shows that all ten registered sufficient forcing
      tests fail for 016 and that, at identical s and weights, 007's actual sharp, sharpw, bL[7/5], bL[1] and trans
      forcing norms are smaller than 016's (certified gaps above 30.172542254537, 18.235303194523, 18.306105182355,
      18.513960661750 and 30.726383186740). Numerical audit 394 (15:18:38Z, result bbb5aa62...) REFUTES as a certified inference
      the norm-certification team's statement that 12-digit stability of its 016 mode-1 dual value under a 2.3-fold basis enlargement proves
      intrinsic Hardy slack. The linear-estimates reviewer's review of theory audit 462 (15:15:21Z, 52 checks) CONFIRMS the new content of theory audit 462 under its
      stated hypotheses; the theory auditor accepts it, with the theory team's closure review 047, in theory audit 468 (below).
      Since matrix v140: The theory team's closure review 047 (15:06Z, review set 45 b8771fb6..., the script for theory audit 462 in the accompanying artifacts 6d8b95ec..., 48 checks)
      CONFIRMS theory audit 462 under its hypotheses, and the theory auditor accepts closure review 047 and the review of theory audit 462 in theory audit 468 (15:24:46Z, result
      cea6f1b3..., 364 checks at 768 bits), so theory audit 462 is AUDITED. The numerical auditor's numerical audit 395 (15:20:13Z, 537 checks) CONFIRMS the
      seven budgets 3.3469e-6, 4.0249e-6, 5.0757e-6, 6.1373e-6, 7.5854e-6, 4.0746e-6 and 4.1069e-6 independently, so
      at the registered floors the unweighted bL bound is below 1/1000 by a factor above 243. Theory audit 468 certifies the linear-estimates reviewer's
      six-digit displays 3.34629e-6 to 4.10620e-6 only as approximations to the supremum of the relaxed formula with k
      = 390.68 and u = 1.5871, not as directed bounds, and REFUTES, read without the positive-margin domain, the
      statement that the supremum of s(mu - C s)^2 over all s > 0 is finite (the theory team's erratum 79 concerns its checker
      header only; no bound changes). Numerical audit 396 (15:23:36Z, result e91c096d..., 38 checks at 4096 bits) proves from
      the norm-certification team's exact test vectors the strict mode-1 and mode-3 floors 0.376998030138416982 and 0.371766751200801401,
      H(016) > 0.529469576110512066 and E_2(016) > 608.392385921614 > 606.820219, so the complete actual E_2 satisfies
      E_2(007) < E_2(016) at identical weights; theory audit 470 (15:34:48Z, result 5be9214b..., 2099 checks at 2048 bits)
      CONFIRMS this by rebuilding both exact denominators independently, with numerical audit 396's full 4096-bit pairing run as
      its numerical premise. The separation above 1.572166921614 is a difference of conservative bounds. The norm-certification team's
      values for modes 5 to 31 and its 16-mode floor 0.6167335007 stayed CLAIMED until the numerical auditor's numerical audit 416 (17:03Z)
      CONFIRMED them. Numerical audit 397 (15:30:03Z, 1104 exact checks)
      reproduces 001's exact leading data from the 860 raw generators and CONFIRMS the corrected affine L^2 exclusion
      independently. Theory audit 469 (15:28:38Z, 75 exact checks) proposes a divergence-free correction of the Hardy upper
      bound, H(F)^2 <= M2 - b^2/a; it is CONFIRMED on two exact fixtures, and its general statement is OPEN pending
      the linear-estimates reviewer's review of theory audit 469 and the theory team's closure review 049. candidate 028 (snapshot 15:24:01Z, rows 107, 108) is a design control with
      FLOAT values only; numerics exchange 15 (15:25:44Z) withdraws the numerics team's statement that the registered probes did not
      respond to any basis change beyond 016's scale-25 functions. theory exchange 08 (15:30:58Z, a35184b7...) is the last
      exchange version of batch T. The norm-certification team (notes 15:25Z and 15:31Z) withdraws as certified statements the inferences
      refuted by numerical audit 394 and theory audit 466. The linear-estimates reviewer's review of theory audit 459 revision 2 (15:32Z) repairs nine nearest-rounded displays;
      no verdict changes.
      Since matrix v142: The theory auditor's theory audit 471 (15:44:07Z, result c4c005dc..., 695 checks) CONFIRMS the finite mathematics of
      theory exchange 08 and the final theory report in the accompanying artifacts version 52 and REFUTES the radius cap 2.7e-6 as an implication of the registered
      high-margin algebra (a sharp Sobolev ball with positive margin has L^2 radius 3e-6); the bound for the registered
      fixed weights is 3.7930e-6 and the weight-uniform unweighted bL bound of WU3 is 4.1069e-6; no exclusion changes,
      and this report and matrix v143 now use 3.7930e-6. Theory audit 471 also REFUTES four literal statements of theory exchange 08 and
      version 52 (row 35 as only framework inapplicability for 001, every exclusion as fixed-c and small-ball, 028 as
      unregistered, 017's (21, 522) as OPEN), which the theory team repairs in its successor files. The numerical auditor's numerical audit 398 (15:38:43Z,
      38 checks at 4096 bits) computes the divergence-free cross terms of theory audit 469's construction for the two numerical audit 396
      trial functions (strict improvement floor sum above 0.2386591564), and numerical audit 399 (15:45:14Z, 566 checks) replays
      all four 016 pairings from 650-digit saved group intervals at 1351 to 1387 relative bits; theory audit 472 (15:49:36Z,
      3113 checks) CONFIRMS both, which discharges the archive limitation of theory audit 470. No upper bound of H(016) is
      accepted: the complete 160-mode M2 and the review of theory audit 469's general statement (the linear-estimates reviewer's review of theory audit 469, the theory team's
      closure review 049) are both needed. The numerical auditor notes that delta = 1 - 1/c0 = 0.4476112310..., not the display 0.44764 of
      theory exchange 08.
      Since matrix v143: The linear-estimates reviewer's review of theory audit 469 (15:59Z, 49583d59..., 59 checks) CONFIRMS the general statement of
      theory audit 469 under its hypotheses (F with finitely many sine modes and int r^3 f_n^2 dr finite; psi smooth with
      finitely many modes, grad psi and r Delta psi in L^2), including the positive-pole supplement; its remark R4
      says that a source with infinitely many modes needs a limit step not in the standalone proof in the accompanying artifacts, and that for a truncated
      serialization M2 must be that of the full source. The theory auditor's acceptance and the theory team's closure review 049 are pending, and the
      complete 160-mode M2 of 016 is still being computed by the numerical auditor, so no upper bound of H(016) is accepted. The numerical auditor's
      numerical audit 400 (15:52:07Z, 473 checks) accepts theory audit 466, theory audit 467 and theory audit 470 reciprocally. Numerical audit 401 (15:57:11Z, 68 checks)
      CONFIRMS the FLOAT tables of numerics exchange 15 against their frozen sources and REFUTES four prose statements of its
      section 6 (016 P2 under comparison, 017 dyadic cells CLAIMED, the radial symbol n for l, registered radius 20 to
      50 for about 20 to 40); no stored value is refuted. The theory auditor's theory audit 473 (15:52:46Z, 290 checks) CONFIRMS the linear-estimates reviewer's
      relaxed-supremum displays at the exact K and v and the 56 directed displays of the review of theory audit 459 revision 2, and
      CONFIRMS the numerical auditor's correction delta = 1824676646553933/4076476460239181 = 0.4476112310.... The norm-certification team's two-sided
      H(016) in [0.6167335007, 0.6189603636] (E_2(016) in [628.5800885, 629.1263188]) and its 16-mode lower bound
      H(017) >= 0.6144195987 (E_2(017) >= 605.4068697, which does not order 017 against 007) are CLAIMED pending
      the numerical auditor. No verdict changes.
      Since matrix v144: theory audit 469 is AUDITED under its hypotheses. The theory auditor accepts the linear-estimates reviewer's review of theory audit 469 in theory audit 475
      (16:06:11Z, 193 checks), reproducing every rational example and the positive-pole closed form, and REFUTES the
      review's section 1.5 wording that the ungrouped condition beta_min > 3/2 is necessary (an n = 3 counterexample
      outside theory audit 469's sufficient subfamily; no accepted case changes). The theory team's review set 46 (16:04Z, 349cb718...)
      CONFIRMS theory audit 469 in closure review 049 and CONFIRMS numerical audit 396 in closure review 048 (1368 checks) conditional on its full-precision pairing
      premise, which the theory team did not recompute and which the norm-certification team, theory audit 470 and the numerical audit 399 archive corroborate; closure review 048 adds
      that the ordering is pairwise. The numerical auditor's numerical audit 402 (16:05:20Z, 1280 checks) accepts theory audit 472 reciprocally. The numerical auditor's
      numerical audit 403 (16:05:20Z, 539 checks) proves M2 <= S_N + (||rF||_2^2 - Q_N)/(N+2)^2 for a complete odd prefix n <= N
      and applies it with N = 7 to the full 160-mode 016 field: M2 < 1.129996 and H(016) < 1.063013, CONFIRMED by
      the numerical auditor, with every omitted mode bounded through the accepted rF norm; the theory auditor's theory audit 474 (15:59:00Z, 720 checks)
      states the same prefix bound in general, its analytic corollary pending the linear-estimates reviewer's review. The improved values
      H(016) < 0.944107 and E_2(016) < 722.968760 and any longer prefix stay OPEN. None of this changes a verdict: the
      016 E_2 ordering uses only the lower bound. numerics exchange 16 (16:06:03Z, 070a8c09...) is batch N's final exchange
      version: no new candidate, FLOAT diagnostics only (Newton steps for 027 and 028, seven-cell proxies for 026 to
      028, the assembled E_2 proxy), and the numerical audit 401 repairs recorded as made in the final numerics report in the accompanying artifacts; the theory team's ACK is due by
      17:06Z. The linear-estimates reviewer's linear-estimates reviewer check of theory exchange v08 (16:04Z) finds four wording items in theory exchange 08 (the 2.7e-6 radius, the
      scope and hypotheses of the WU3 bounds, three not-covered items, a section reference), for the theory team's successor
      files.
      Since matrix v145: The theory auditor's theory audit 476 (16:13:02Z, 2297 checks at 8192 bits) audits the numerical auditor's numerical audit 403 prefix of modes 1,
      3, 5, 7 of the full 160-mode 016 field (124 saved groups, 1360 branch records, 140 source bindings, the exact
      rational endpoint composition) and CONFIRMS the plain bound H(016) < 1.063013 and, through theory audit 472's strict
      two-mode cross floor and the AUDITED theory audit 469 theorem, 0.529469576110512066 < H(016) < 0.944107 and
      608.392385921614 < E_2(016) < 722.969, under the accepted source-specific construction, positive-pole moment and
      outward-serialization premises. Every uncomputed mode is bounded through the accepted total rF norm, so the
      finite-mode case needs neither theory audit 474's infinite-series corollary nor the theory team's reciprocal review. The numerical auditor's numerical audit 404
      (16:13:35Z, 77 checks) CONFIRMS the linear-estimates reviewer's review of theory audit 469 (the 16:04Z revision) and the finite-source hypothesis of
      its remark R4 for 016, and holds the improved numerical upper value OPEN on its side until its own
      complete-field assembly and the reciprocal review are bound. The theory team's review record v54 (16:08Z) states the
      composition H(016)^2 <= U - sum b_n^2/a_n for any upper bound U of the complete M2, takes theory audit 474 and numerical audit 403's
      tail step as closure review 050 (target 17:10Z), and ACKs the theory exchange 08 repairs for the final theory report in the accompanying artifacts version 53 (target 16:50Z).
      The norm-certification team CLAIMS (16:14Z) two-sided enclosures H(017) in [0.6144195987, 0.6165956396] and E_2(017) in [605.4068697,
      605.9589546], below the CONFIRMED E_2(007) range by at least 0.8591, pending the numerical auditor; that would give the pairwise
      order 017 < 007 < 016 of the actual E_2 values, which orders neither correction distances nor closure margins.
      017 stays RULED OUT by its CONFIRMED distances. No verdict changes.
      Since matrix v146: The theory auditor's theory audit 477 (16:17:52Z, 209 checks) accepts the theory team's closure review 048 and closure review 049 reciprocally, so
      theory audit 469 is reviewed independently by the linear-estimates reviewer and the theory team and accepted by the theory auditor, and the pairwise gap E_2(016) -
      E_2(007) > 1.572166921614 stands under numerical audit 396's source-pairing premise; it REFUTES one transcription in closure review 049
      (V6: the FLOAT example uses the exponent 7/5, not 7/10), which affects no theorem or candidate value. The numerical auditor's
      numerical audit 405 (16:16:17Z, 206 checks) CONFIRMS the finite displays of numerics exchange 16 and the four numerical audit 401 repairs, and
      REFUTES the section 6 phrase that calls 028 diagnostic record the last computation. The numerical auditor's numerical audit 406 (16:19:22Z, 65 checks)
      CONFIRMS theory audit 475's cancellation counterexample to the necessity wording of the review of theory audit 469 section 1.5
      reciprocally; the review needs a sufficient hypothesis or a noncancelling-leading-term qualification there, and
      no candidate norm changes. The final theory report in the accompanying artifacts version 53 (16:16:52Z, 2183 lines, 51647b68...) carries the theory exchange 08
      errata (the cap 3.7930e-6, the affine 001 exclusion, the exact delta, the linear-estimates reviewer's D1 to D4) and the 016 upper bounds
      of theory audit 476; the theory auditor's audit is pending. No verdict changes.
      Since matrix v147: The numerical auditor's numerical audit 407 (16:21:14Z, 438 checks) re-adds the dyadic endpoints of all 124 650-digit
      group balls as exact rationals and CONFIRMS the theory auditor's theory audit 476 finite interval assembly and its omitted-mode
      coverage: the plain bound H(016) < 1.063013 covers all 160 modes, and the improved assembly gives H(016) <
      0.944107 and E_2(016) < 722.969. The numerical auditor keeps its announced gate and promotes the improved value only after
      the theory team's reciprocal review (closure review 050, target 17:10Z). These bound one residual norm of one candidate and order no
      correction distances. No verdict changes.
      Since matrix v148: The theory auditor's theory audit 478 (16:23:59Z, 44 checks) CONFIRMS that the positive-coefficient and the split
      upper formulas for the 016 four-mode prefix both keep H(016) < 0.944107 and E_2(016) < 722.969 (the split form
      is the larger one by the interval widths), and REFUTES a reversed comparison in the linear-estimates reviewer's unfinished review of
      theory audit 474; no completed review, certificate or theorem is affected. Display repair (16:26Z): five endpoints that
      the report quoted from the norm-certification team's prose between 16:16Z and 16:24Z were rounded inward. They now follow the
      directional records: E_2(007) in [606.8181534, 606.8202172] (numerical audit 252, as in matrix row 80), H(017) >=
      0.6144195987 and E_2(017) in [605.4068697, 605.9589546]. The gap of at least 0.8591 is unchanged. No verdict
      changes.
      Since matrix v149: The numerical auditor's numerical audit 408 (16:26:34Z, 834 checks) accepts the theory team's closure review 048 and closure review 049 reciprocally and
      REFUTES only the closure review 049 V6 exponent attribution, as theory audit 477 did. From its own exact integration of the odd modes
      1 to 31 and the accepted ||rF||_2, the numerical auditor bounds the whole 160-mode field: H(016) < 0.789068 (numerical audit 409, 2063
      checks) and, with the accepted mode 1 and 3 corrections, 0.529469576110 < H(016) < 0.619652 and 608.392385921614
      < E_2(016) < 629.296113 (numerical audit 410, 44 checks, 16:28:19Z). The numerical auditor no longer waits for the theory team's closure review 050, which stays an
      additional review; the theory auditor's replay of numerical audit 409 and numerical audit 410 is pending. Since H(007) > 0.6355243760, H(016) < H(007),
      while E_2(007) < E_2(016) by more than 1.572166921614. Both are statements about one norm each and order no
      correction distances. No verdict changes.
      Since matrix v150: The theory auditor's theory audit 480 (16:36:20Z, 4463 checks) reproduces numerical audit 409 from all 484 saved groups at 8192
      bits, so H(016) < 0.789068 over all 160 modes and, with the accepted two-mode correction, 0.529469576110512066 <
      H(016) < 0.619652 and 608.392385921614 < E_2(016) < 629.296113 are accepted both ways; they do not use theory audit 474's
      infinite-series corollary. That corollary is CONFIRMED under its hypotheses by the linear-estimates reviewer's review of theory audit 474 (16:28:42Z)
      and the theory team's closure review 050 (review set 47, 4783 checks), written independently; the theory auditor's acceptance of both (theory audit 481) is in
      progress, and the theory auditor's review record v261 asks the theory team to mark three narrow decimal steps of closure review 050 V7 as approximate
      or round them upward (no verdict changes). The theory team ACKed numerics exchange 16 at 16:34Z, 28 minutes after its stamp. The
      frozen copy of 16:26:57Z was audited by the theory auditor (theory audit 479, 823 checks) and the numerical auditor (numerical audit 411, 2455 checks): both CONFIRM
      all 108 statuses and candidate associations. Theory audit 479 REFUTES the unrestricted maximality wording of answer 1
      (repaired at 16:33Z) and asks for the two clarifications now made in the table legend and in row 25. Numerical audit 411
      REFUTES the frozen lines that named closure review 050 as the gate of the numerical auditor's improved 016 upper bound (those lines were
      already rewritten at 16:30Z) and the row count of my 16:28Z note: the table has 106 physical rows, 105
      single-numbered rows and the combined row 12-14, covering all 108 matrix rows. The norm-certification team's final tables (16:37Z)
      keep every 017 record and its own 016 interval CLAIMED; its 016 interval lies inside the accepted enclosure. No
      verdict changes.
      Since matrix v151: The theory auditor accepts both independent reviews of theory audit 474, the linear-estimates reviewer's review of theory audit 474 and the theory team's closure review 050,
      in theory audit 481 (16:42:29Z, 263 checks), so the general prefix Hardy bound theory audit 474 is AUDITED under its hypotheses (F
      real, locally integrable, even in x, odd in y, rF in L^2, every odd n < N included, correction tests of distinct
      frequencies). Theory audit 481 REFUTES only the directed-bound attribution of three intermediate decimals and the R2
      endpoint display in closure review 050 V7; the theory team repairs them in errata E4 to E7 of review set 48, and the bounds 1.063013,
      0.944107 and 722.968760 stand. The theory team's closure review 051 (review set 48, 54 checks) recomposes numerical audit 409 and numerical audit 410 exactly from
      their saved endpoints and CONFIRMS them, as an additional review that recomputes no mode integral. The numerical auditor's
      numerical audit 412 CONFIRMS H(007) - H(016) > 0.015873038675998 and E_2(016) - E_2(007) > 1.572166921614: two actual norms
      order the pair in opposite directions, and neither orders correction distances. The numerical auditor's numerical audit 413 (441 checks)
      CONFIRMS only that the norm-certification team's 017 source records imply the 017 H and E_2 enclosures and the gap above 0.8591; the
      source premises are OPEN, so those records stay CLAIMED. The theory auditor's theory audit 482 (77 checks) audits the final theory report in the accompanying artifacts version
      53: it CONFIRMS the changed scopes and the strict E_2(007) < E_2(016), with a certified margin above 1.39
      percent, and REFUTES the literal statement that t = 1 is the exact optimizer of the two-mode correction (t* < 1
      by less than 1e-34; no bound changes) and the version's inward 007 and 017 endpoint displays. The norm-certification team now labels its
      017 gap 0.8591 and its 016 gap 21.75 as CLAIMED, separately from the accepted gap 1.572166921614. No verdict
      changes.
      Since matrix v152: The theory auditor's theory audit 483 (16:50:38Z, 131 checks) accepts the theory team's closure review 051, numerical audit 410's complete upper
      composition and numerical audit 412, so 0.529469576110 < H(016) < 0.619651337324093367770781451079, 608.392385921614 <
      E_2(016) < 629.296112162914, H(007) - H(016) > 0.015873038675998 and E_2(016) - E_2(007) > 1.572166921614 are
      accepted both ways; it REFUTES only closure review 051 V7's literal 'at most 0.9888' for the share of R2 carried by modes 1
      to 31 (the exact fraction lies in (0.988805, 0.988806)). The theory auditor's theory audit 484 (16:56:09Z, 2982 checks) accepts numerical audit 413
      as conditional finite arithmetic and checks the analytic residual and dual identities that the numerical auditor's queued 017
      replay uses; it accepts no actual 017 norm, and the source premises C1 to C3 stay OPEN, so the narrow 017 H and
      E_2 and the order 017 < 007 stay CLAIMED. The numerical auditor's numerical audit 414 (16:52:47Z, 411 checks) CONFIRMS the theory audit 474 review
      chain, theory audit 481 and theory audit 480's 016 prefix arithmetic reciprocally. The theory team publishes the final theory report in the accompanying artifacts version 54 (16:55Z,
      2255 lines, 1be0dece...) with the theory audit 482 repairs (the theory auditor's audit pending) and review set 49 with errata E8 to E10:
      H(016) > 0.522193054 is sufficient, not necessary, for the E_2 ordering, with a margin above 1.39 percent.
      The linear-estimates reviewer's linear-estimates reviewer check of theory audit 479 (report repair) (12 checks) CONFIRMS the repaired lines of answer 1, short answer 1 and
      the defect paragraph of this report. No verdict changes.
      Since matrix v153: The numerical auditor's numerical audit 416 (17:03:31Z, 6925 checks, 2130 groups at 4096 bits) rebuilds the 16 proposed
      dual and divergence-free tests of 016's odd modes 1 to 31 from the raw source and CONFIRMS all 16 of the norm-certification team's
      dual displays, H(016) > 0.616733500736450480026368341286 and E_2(016) > 628.580088526341, so E_2(016) -
      E_2(007) > 21.759869526341 against the accepted 007 upper bound 606.820219 (CONFIRMED by the numerical auditor; the theory auditor's replay
      pending). With the upper bounds accepted both ways, 0.6167335007 < H(016) < 0.6196513374. The norm-certification team's narrower
      values from modes 33 to 63 stay CLAIMED. These bound one residual norm of one candidate; 016 stays RULED OUT by
      distance. The theory auditor's theory audit 485 (57 checks) accepts the linear-estimates reviewer's check of theory audit 479 (sharpw max) and the g = 0 repair of this
      report (the 16:52Z version), and the numerical auditor's numerical audit 415 (72 checks) CONFIRMS theory audit 479 and the three repaired blocks: the
      exact optimum 40722836401/193491763200000 at r* = 201799/149299200 is AUDITED and CONFIRMED by both audit workers,
      as the maximum of this one sufficient estimate at s = 1/5184 and w = (2^15, 2^20). The theory team publishes the final theory report in the accompanying artifacts
      version 55 (17:01Z, 2269 lines, aa2d3063...; the theory auditor's audit pending) and erratum E11 (review set 50): the exact share
      of R2 carried by modes 1 to 31 lies in [0.988805059517, 0.988805059518]. No verdict changes.
      Since matrix v154: The theory auditor's theory audit 486 (17:04:42Z, 13380 checks) accepts numerical audit 416, so H(016) > 0.6167335007 and
      E_2(016) > 628.580088526341 are accepted both ways (theory audit 486 printed 628.580088525 and 21.759869525; the printed
      precision is accepted in theory audit 488 and theory audit 502). Putting all 16 corrected modes 1 to 31 into the
      positive-coefficient tail formula, with the other 144 source modes retained, the numerical auditor (numerical audit 417, numerical audit 418, 4430 checks)
      and the theory auditor (theory audit 486) each CONFIRM 0.6167335007 < H(016) < 0.6179529539 and 628.580088526341 < E_2(016) <
      628.8790248, hence H(007) - H(016) > 0.017571422145091 and E_2(016) - E_2(007) > 21.759869526341. The theory auditor's formal
      acceptance of numerical audit 418 is pending. These bound one residual norm of one candidate; 016 stays RULED OUT by
      distance. The theory auditor's theory audit 487 (492 checks) accepts the mathematics of the final theory report in the accompanying artifacts version 55 and errata E8 to E11 and
      asks the theory team for three wording and provenance repairs (a too broad sentence on failure factors in section 2.1, the
      check count of the arithmetic check 50 in the accompanying artifacts, and the matrix version in two artifact guide input columns). The numerical auditor's numerical audit 419 (3005 checks)
      REFUTES the final numerics report in the accompanying artifacts statement that the five Taylor equations hold to 2e-13 for every saved candidate: for
      007, 2.0899e-11 < [y^4]R_f(0,y) < 2.0900e-11. This report already states that 007's Taylor residuals are
      nonzero, of order 1e-11. No verdict changes.
      Since matrix v155: The theory auditor's theory audit 488 (17:15:12Z, 121 exact checks) accepts numerical audit 417 and numerical audit 418 reciprocally, so
      0.6167335007 < H(016) < 0.6179529539, 628.580088526341 < E_2(016) < 628.8790248, H(007) - H(016) >
      0.017571422145091 and E_2(016) - E_2(007) > 21.759869526341 are accepted both ways. The theory auditor's theory audit 490 (3181 checks)
      CONFIRMS numerical audit 419 from the full exact origin jet of 007: all five nonconstant Taylor coefficients of R_f = F/y
      exceed 2e-13 in magnitude, so the final numerics report in the accompanying artifacts tolerance statement is REFUTED by both audit workers. The theory auditor's
      theory audit 489 (86 checks) accepts the linear-estimates reviewer's review of theory audit 469 revision 2 and the linear-estimates reviewer check of theory audit 479 (report repair). Matrix v156
      (17:23Z) joined nine bullets into one by a the coordinator edit-script error; v157 (17:24Z) restores them with
      unchanged text. No verdict changes.
      Since matrix v157: The numerical auditor's numerical audit 421 (180 checks) reconciles the two complete 016 enclosures of the theory auditor (theory audit 486,
      theory audit 488) and the numerical auditor (numerical audit 416 to numerical audit 418): lower squares and floors agree exactly and the upper squares differ by a
      positive amount below 10^(-500). The numerical auditor's numerical audit 420 (626 checks) CONFIRMS all 600 printed probe values of the
      the final numerics report in the accompanying artifacts frozen at 17:02Z and REFUTES four literal statements of scope (the thousandfold first-mode
      reduction for 013, whose full register ranges from 26.85 to 9358.86; the range 27 to 314; the 023 phase range;
      the 024 hash attribution); the numerics team's revision of 17:25:34Z repairs them, and the numerical auditor's numerical audit 422 (233 checks) CONFIRMS
      those repairs except two remaining literal attributions (the 024 hash and the 'four largest values' phrase).
      The theory auditor's theory audit 491 (278 checks) audits the linear-estimates reviewer's linear-estimates reviewer final summary: the necessary scalar cap 3.79e-6 is REFUTED (exact
      scalar parameters admit 3.791e-6; the valid common upper bound is 3.7930e-6, consistent with the 3.8e-6 of
      answer 6), 0.99998313 is the nearest rounding of an exact factor in (0.99998312568, 0.99998312569), and 'closest
      candidate' is OPEN as a ranking of actual correction distances, as answer 3 already says for 007. The final theory report in the accompanying artifacts
      versions 56 and 57 (17:22Z, 17:28Z) make theory audit 487's repairs; the theory team's closure review 052 CONFIRMS the recomposition of numerical audit 417 and
      numerical audit 418 and erratum E12 corrects a check count. No verdict changes.
      Since matrix v158: The theory auditor's theory audit 492 (1340 checks) accepts numerical audit 420 and the numerical auditor's numerical audit 423 (4128 checks) CONFIRMS theory audit 490
      and theory audit 492 from its own exact reconstruction of 007's origin jet, so the refutation of a universal 2e-13 Taylor
      tolerance for the saved 007 and the 600 probe displays of the final numerics report in the accompanying artifacts are accepted both ways. The numerics team's
      revision of 17:35:40Z repairs the two literal attributions left by numerical audit 422 (the 024 held-out hash and the
      selection of the four listed 023 probes). The final theory report in the accompanying artifacts version 58 (17:31Z) applies the linear-estimates reviewer's review record BS wording
      repairs. The section "Answers in brief" was condensed at 17:35Z to one short paragraph per question with the
      same verdicts and audit references; the former text is kept in
      an earlier version (not published). No verdict changes.
      Since matrix v159: The theory auditor's theory audit 493 (535 checks) accepts the final theory report in the accompanying artifacts version 58 and the complete 016 recomposition
      of the theory team's closure review 052, with two literal repairs requested (the gap from 0.6167335007 to the strict H lower bound is
      between 3.64e-11 and 3.65e-11; the sentence that every sharpw forcing factor uses 2.1035e-4 must exempt the
      explicit eta* comparison). The theory auditor's theory audit 494 (294 checks) accepts numerical audit 422, so the final numerics report in the accompanying artifacts repairs of
      17:25:34Z and the two remaining literal corrections are accepted both ways. No verdict changes.
      Since matrix v160: The numerical auditor's numerical audit 425 (5704 checks) replays the norm-certification team's 017 duality and residual trials from its own
      exact projected residuals and CONFIRMS the 16 dual trials, the full-plane lower bound H(017) > 0.6144195987 and
      the residual-mode enclosures of the modes 1 and 3; the complete upper bound for H(017), E_2(017) and the claimed
      order E_2(017) < E_2(007) stay OPEN, and 017 stays RULED OUT by distance. The numerical auditor's numerical audit 424 (226 checks) CONFIRMS
      the numerics team's the final numerics report in the accompanying artifacts revision of 17:35:40Z. The final theory report in the accompanying artifacts version 59 (17:38Z) states the scalar distance
      condition as below 3.7930e-6 and prints the 013 first-mode factor as 9359; the theory team's review set 52 records errata
      E13 and E14 (found by theory audit 493). No verdict changes.
      Since matrix v161: The theory auditor's theory audit 495 (10450 checks) accepts numerical audit 425 and the numerical auditor's numerical audit 426 (984 checks) accepts theory audit 495,
      so H(017) > 0.6144195987 and the residual-mode enclosures of the modes 1 and 3 are accepted both ways; 14
      residual trials, 158 Hardy squares and G0, G1, P2 of 017 are not reproduced, so the complete H(017) upper bound,
      E_2(017) and the order E_2(017) < E_2(007) stay OPEN. The theory auditor's theory audit 496 (310 checks) accepts numerical audit 424, so the numerics team's
      the final numerics report in the accompanying artifacts revision of 17:35:40Z is accepted both ways for its two literal repairs. No verdict changes.
      Since matrix v162: The numerical auditor's numerical audit 427 and numerical audit 428 tighten the complete 016 upper bounds with 24 complete Hardy modes
      through frequency 47 (0.616733500 < H(016) < 0.617899376, 628.580088 < E_2(016) < 628.865882); these are the numerical auditor
      numbers pending the theory auditor's audit at the numerical auditor's final prefix 63, so this report keeps the accepted bounds of numerical audit 418 and
      theory audit 486. The framework table prints the rebalanced Sobolev framework threshold as 3/327680 (about 9.1553e-6), as the numerical auditor
      (17:53Z) and the linear-estimates reviewer's review record BT3 ask; the decimal is a display only. The linear-estimates reviewer's linear-estimates reviewer final summary carries the four
      theory audit 491 repairs (review record BT), and the final theory report in the accompanying artifacts version 60 (17:44Z) makes the two theory audit 493 repairs. No verdict
      changes.
      Since matrix v163: The theory auditor's theory audit 498 (6234 checks; an independent 8192-bit resummation of all 708 source-certified
      groups) accepts numerical audit 427 and numerical audit 428, so 0.6167335007 < H(016) < 0.617899376, 628.580088526341 < E_2(016) <
      628.865882, H(007) - H(016) > 0.017625000525836 and E_2(016) - E_2(007) > 21.759869526341 are accepted both
      ways; the answers and the comparison table now use these bounds, and the numerical audit 418 bounds stay valid. The theory auditor's
      theory audit 497 (452 checks) accepts the final theory report in the accompanying artifacts version 60 and review set 52 with no further wording request. The theory team's
      closure review 053 (review set 53, 79 checks) CONFIRMS the residual identity behind the numerical auditor's numerical audit 425 and recomposes its 017
      bounds; the complete H(017) upper bound and E_2(017) stay CLAIMED. The norm-certification team now divides by the exact thresholds
      3/327680 and 1/163840 in its registered tables, which lowers one 007 ratio display (8.4699902e+7 to 8.4699685e+7
      for L2 framework); the numerical auditor's numerical audit 429 (37 checks) CONFIRMS the repaired floors, and the old displays were not used
      in this report. No verdict changes.
      Since matrix v164: The theory auditor's theory audit 499 (80 checks) accepts the linear-estimates reviewer's repaired final linear-estimates summary (5398df04...) and
      review record BT, which closes the four theory audit 491 requests (the common scalar bound 3.7930e-6, the approximate factor
      0.99998313, no closest-candidate claim, 4.5717e-4 as an upper bound) and the moment coefficient in
      (5.04422709906931, 5.04422709906932). The theory auditor's theory audit 500 (83 checks) accepts numerical audit 429, so the norm-certification team's exact-threshold 007
      floors 84699685 and 66246337 are accepted both ways. At the theory team's request (review record v63), this report now prints
      the L2 framework and transient-low L2 framework thresholds as 1/163840 (about 6.1035e-6; the decimal is below the exact
      value) and 1/196608 (about 5.0863e-6). The final theory report in the accompanying artifacts version 62 (18:08Z, d29ea4fa...) carries the prefix 47 016
      bounds and the closure review 053 017 paragraph; the theory auditor's audit of it is pending. No verdict changes.
      Since matrix v165: The numerical auditor's final 016 composition from the complete prefix 63 (numerical audit 430, numerical audit 431; 32 complete Hardy
      modes, the other 128 modes in the tail bound) gives 0.616733500 < H(016) < 0.617897369, 628.580088 < E_2(016) <
      628.865389 and H(007) - H(016) > 0.017627007636152781. These are the numerical auditor numbers pending the theory auditor's replay; the
      answers keep the prefix 47 bounds accepted in theory audit 498. The linear-estimates reviewer's linear-estimates reviewer check of numerical audit 017 (residual identity) (18 checks)
      CONFIRMS the numerical audit 425 residual identity and the bounds (2) under the stated hypotheses; the numerical auditor finds a missing
      factor n in one auxiliary absolute-convergence bound of that review, which does not affect the identity or any
      017 endpoint. No verdict changes.
      Since matrix v166: The theory auditor's theory audit 501 (398 checks) accepts both reviews of the numerical audit 425 residual identity, the theory team's
      closure review 053 and the linear-estimates reviewer's check, after the same missing-n correction (an exact n = 3 example is off by a factor 3
      without it; the corrected bound still gives absolute convergence), and derives the origin integrability needed
      for 017 from the accepted smooth finite potential. The complete H(017) upper bound, E_2(017) and E_2(017) <
      E_2(007) stay OPEN. No verdict changes.
      Since matrix v167: The numerical auditor's numerical audit 432 (2290 checks) accepts both reviews with the same correction and discharges the
      origin condition from the 2174 exact 017 generators, so the residual identity behind numerical audit 425 is accepted both
      ways. No 017 endpoint and no verdict changes.
      Since matrix v168: The theory auditor's theory audit 502 (7564 checks; all 920 source-certified groups resummed at 8192 bits) accepts
      numerical audit 430 and numerical audit 431, so the prefix 63 bounds 0.6167335007 < H(016) < 0.617897369, 628.580088526341 < E_2(016) <
      628.865389 and H(007) - H(016) > 0.017627007636152781 are accepted both ways and replace the prefix 47 upper
      ends in the answers and in table row 80; the theory team's closure review 054 (272 checks) recomposes numerical audit 427, numerical audit 428, numerical audit 430 and
      numerical audit 431 exactly from their saved endpoints. 016 stays RULED OUT by its distances, and these norm bounds order no
      correction distances. The linear-estimates reviewer's check revision 1 (18:14:51Z) prints the corrected auxiliary bound. No verdict
      changes.
      Since matrix v169: The numerical auditor's numerical audit 433 (1099 checks) accepts theory audit 502, so the prefix 63 016 bounds are accepted
      reciprocally, and the theory auditor's theory audit 503 (4710 checks) and numerical audit 433 accept the linear-estimates reviewer's revision 1; theory audit 503 also inspects all
      2174 raw 017 generators and confirms the origin condition. The complete H(017) upper bound, E_2(017) and
      E_2(017) < E_2(007) stay OPEN. The final theory report in the accompanying artifacts version 64 (18:20Z, e505fc3d...) gives the prefix 63 bounds as
      accepted both ways; the theory auditor's audit of it or of the 19:00Z final is pending. No verdict changes.
      Since matrix v170: The theory auditor's theory audit 504 (473 checks) accepts the theory team's closure review 054 and its exact width identity, and refutes
      one inference of it: that most of the remaining width of the H(016) enclosure comes from the dual floors. Each
      mode gap is the sum of a lower and an upper slack, which the identity does not separate; the theory team accepts this as
      erratum E15. No 016 endpoint and no verdict changes.
      Since matrix v171: The numerical auditor's numerical audit 434 (23 checks) confirms the same width split and refutes the same inference with
      an exact counterexample, and the theory auditor's theory audit 505 accepts E15 with one literal repair. Whether most of the actual 016
      width is dual error stays OPEN. No 016 endpoint and no verdict changes. Matrix v172 is the state at the H22
      freeze.
      Since matrix v172: the final documents of the theory team, the numerics team, the linear-estimates reviewer and the theory auditor are published (section 1). The numerical auditor's
      numerical audit 435 checks the byte integrity of its final evidence index (49 accepted roots, 7497 direct local bindings, 0
      errors); it is not a new mathematical audit. The theory team's erratum E16 makes the literal repair that theory audit 505 asks for.
      No number and no verdict changes (matrix v173). The numerical auditor's numerical audit 436 then confirms that the frozen the final numerics report in the accompanying artifacts
      differs from the revision audited in numerical audit 424 only in its header line, so numerical audit 424's findings transfer to the final
      (matrix v174). The theory auditor's theory audit 506 (828 checks) CONFIRMS the final the final theory report in the accompanying artifacts and E16 and REFUTES only the sentence
      "This document quotes neither ratio." of its section 2.5, which the preceding sentence contradicts by printing
      84699685 and 66246337 (matrix v175). The theory team keeps the final theory report in the accompanying artifacts unchanged and records that repair as erratum EF1
      (read "These corrected ratios do not alter any earlier norm bound.") and a stale matrix version in section 0 as
      EF2 (review record 67). The theory auditor's theory audit 507 (73 checks) accepts the final linear-estimates summary, and the theory auditor records that
      its frozen receipt counts 3977 checks, not 3976 (count erratum 01 in the accompanying artifacts). The numerical auditor's numerical audit 437 (3278 checks) checks the
      frozen copy of this report (the frozen copy of this report of 1837Z, 7fd963af...) against matrix v175: all 108 row statuses,
      19 principal distance floors, 22 selected ratios and the selected 007 and 016 norms agree; it is not an audit of
      every narrative number (matrix v176). The numerical auditor's numerical audit 438 (29 exact checks) REFUTES this report's attribution of
      numerical audit 180's shares 72, 14 and 14 percent to the squared sharpw norm: they are shares of the unregularized
      comparison energy E_*^2 with weights 2^14 and 2^18, and in the squared sharpw norm (weights 2^15 and 2^20, with
      the multiplier J^s) the weighted G0 term alone carries more than one quarter by the exact bound of numerical audit 438. Both
      passages now carry the numerical auditor's wording. No norm, ratio, distance or verdict changes (matrix v177). The theory auditor's theory audit 508
      (1083 checks, 474 cited audit IDs) checks the theory labels of the same frozen copy: all 108 rows agree and no
      bound or verdict changes. It asks for six repairs, all applied: the sharpw maximum is that of one audited
      sufficient estimate at s = 1/5184 and w = (2^15, 2^20), and thresholds in different norms do not order residual
      balls (answers 1); theory audit 324 is AUDITED through the review of theory audit 324 and theory audit 337 (section 3); the linear-estimates reviewer's endpoint
      falsification check is AUDITED (theory audit 443, theory audit 452, theory audit 454, theory audit 464), not CLAIMED, and the gain above 3596535.57 is
      what the selected sharpw test needs, not a necessary condition for every route (section 6); the open allocation
      of the 016 H width is listed in section 6; and 628.580088526341 and 21.759869526341 are cited to theory audit 488 for
      their printed precision. The theory auditor CONFIRMS EF1 and EF2 (matrix v178). The theory auditor's theory audit 509 (95 checks) CONFIRMS numerical audit 438
      independently, including the share of more than one quarter, and the numerical auditor's numerical audit 440 (83 checks) accepts theory audit 509; both
      passages carry the wording that both workers request. The numerical auditor's numerical audit 439 (342 checks), CONFIRMED in this respect by
      the theory auditor's theory audit 510 (59 checks), finds that the comparison table column "residual LB" holds rounded displays that are
      not lower bounds (d2's G0 = 4.99 in rows 20 and 37 exceeds its certified upper end 4.988817004568..., and
      016's ||rF||_2 = 7.1457012 in row 80 exceeds 7.145701175364457...); the column is renamed "residual value or
      bound" and the table caption states the display convention. No ratio or verdict changes (matrix v179). The theory team
      reruns all 69 jobs of its artifacts on a copy: 51 outputs are byte-identical, 18 differ only in run times, clock
      stamps or a final "rc=0" line, and none differs in a mathematical number, a check count or a verdict (theory team
      note v69, in the reading of review record v72). This is a rerun by the producing worker, not an independent audit
      (matrix v180). The theory auditor's theory audit 511 (532 checks) and the numerical auditor's numerical audit 442 (329 checks) each CONFIRM the comparison from
      copied files without running a the theory team program: all 69 jobs appear once with rc=0 in the log; 51 outputs are
      byte-identical, 3 differ only in a final rc=0 line and 15 only in elapsed seconds or UTC stamps. This confirms a
      comparison of saved files, not the execution, the wall time or the core affinity. The numerical auditor's numerical audit 441 (63 checks)
      accepts theory audit 510. The linear-estimates reviewer (review record BZ) finds no statement by the linear-estimates reviewer of the corrected shares and reads its two printed
      values of d2's G0 as nearest displays. The diff check of the 19:00Z frozen copy names two literal source-record
      corrections (the numerical auditor, 19:01:36Z; the second also the theory team, review record v71), both applied: the final hash of the numerical auditor's
      the final numerical audit in section 1 and the three final rc=0 lines in section 8 (matrix v181). The theory auditor's
      theory audit 512 (1433 checks) and the numerical auditor's numerical audit 443 (4970 checks) complete the check of the 19:00Z copy: every earlier
      repair is applied and all 108 rows agree with the matrix; numerical audit 443 also CONFIRMS the section 8 hashes and file
      counts. Their further repairs are applied: "mathematical number" in the sentence above (theory audit 512 F1), the
      immutable the theory auditor addenda snapshots in place of a live file hash in section 1 (numerical audit 443), "static checks of the
      selected final evidence" and the audited exclusion of candidate 007 in section 8 (theory audit 512 C1 and C2) (matrix v182).
      The numerical auditor's numerical audit 444 (5464 checks) freezes a separate byte-integrity index of its postfreeze audits numerical audit 436 to numerical audit 443.
      numerical audit 445 (26 checks) finds that two intervals in the numerics team's optional 18:51Z share note are rounded summaries, not
      directed enclosures; the share above 1/4 follows from its premises, and neither interval is used in this report.
      The theory team checked the 54 hash tokens printed after the theory team file names, and the linear-estimates reviewer the hash prefixes of its files, in
      the 19:00Z copy; neither found anything to repair (matrix v183, in the wording of theory review record v75). The theory auditor's
      theory audit 513 (717 checks) and the numerical auditor's numerical audit 446 (928 checks) accept every repair of theory audit 512 and numerical audit 443 in the report state
      of 19:09Z (sha256 12638987...) and request no further repair. Both acceptances are bound to those bytes; the
      later edits (the items of matrix v183 and v184, the status stamps and the final copy) are outside them. The numerical auditor's
      numerical audit 447 (5633 checks) extends its postfreeze integrity index through numerical audit 446, and the theory auditor's validation receipt 08 in the accompanying artifacts
      (5442 checks) covers its addenda through theory audit 513 (matrix v184). The theory auditor's theory audit 514 (88 checks) CONFIRMS that the
      wording of the theory team prefix check above states that check's scope, and REFUTES only the completeness of a fixed
      240-character window rule on arbitrary texts; it shows no missed citation in this report, and exhaustive
      coverage stays OPEN. The linear-estimates reviewer states the scope of its check in review record CB: a wrong prefix for a file of the linear-estimates reviewer is
      caught only where the linear-estimates reviewer or linear-estimates reviewer is named nearby (matrix v185).
      theory audit 359 (AUDITED since theory audit 370 accepted the linear-estimates reviewer's review of theory audit 359; the theory team's closure review 037 also CONFIRMS it) gives a compact
      mode-1 annular correction with a prescribed first moment m, no effect on r < R, L^2 and sharpw high norm
      O(|m| R^-2) and H_q cost diverging for q < -3, so the present high norm controls neither the first moment nor
      H_q. It is reference design, not existence. Theory audit 371 CONFIRMS the linear-estimates reviewer's remark R2: for q < -3 an L^2 bound beta
      and a weighted amplitude bound |h| <= H(1+|X|)^q give |first moment| <= Csplit beta^theta H^(1-theta) with
      theta = d/(d+2), d = -q-3, and the exponent is optimal; the first moment is controlled only when both budgets
      are supplied, and the present balls supply no amplitude budget. The step from R3's drift comparison to the
      complete annular residual change is OPEN. Theory audit 373 CONFIRMS closure review 037 remarks (a) to (c) (no bounded embedding of
      the sharpw high norm into H_q for q < -1; invariance of the endpoint part orthogonal to P under compact changes;
      the optimal power R^-2) and REFUTES remark (d): the complete residual change of h_R is asymptotic
      to |m| A_c R^-2 with A_c >= (c+1)||f||_2 > 0, not O(R^(gamma-3)). Theory audit 372 (the optimal constant 9.155134741... for the
      theory audit 371 amplitude inequality, sharp only in the homogeneous amplitude class) is AUDITED: The theory team's closure review 039 CONFIRMS
      it and theory audit 382 accepts that review. Theory audit 360 to theory audit 362 reproduce the numerical auditor's numerical audit 291 for 020 independently (all eight point fields
      and six scalar gaps, uniform graded gap positive; origin normalization; complete sixteen-sector prefix with the
      same five nonzero sectors as 019), theory audit 363 CONFIRMS numerical audit 293 (020 distance from (19, 1800), radius in
      (0.0018553746774427130, 0.0018553746774427131), both scales jointly, six mixed-pole fixtures run) and theory audit 364
      binds the 2426 actual shapes and the current objective span. Theory audit 365 accepts sections 2 and 3 of the linear-estimates reviewer's
      the review of theory audit 338, so the third-cutoff application of theory audit 338 and theory audit 339 are AUDITED (weighted asymptotic
      consequence for the repaired references, not an L^2 exclusion). Theory audit 368 CONFIRMS the linear-estimates reviewer's remarks R2 to R4 in
      part (exterior dipole bookkeeping, the two-term asymptotic expansion, positive projected inner products, and a
      fourth cutoff that removes the endpoint coefficient with zero first moment and arbitrarily small L^2 cost); a
      finite-radius bound on the complete remainder is OPEN. Theory audit 369 CONFIRMS numerical audit 294 (abstract dimension 2414 of the
      proposed higher-angular radius-25 extension). Theory audit 373 audits the published theory exchange 06 in full: it CONFIRMS the
      closure inequalities, all 51 table ratios, the repaired unchecked hypotheses of 007, the third-cutoff
      dependencies and the exclusion scope through 020, and REFUTES the section 2.1 index of the scaled legqs blocks
      (they enter at q >= 4, not l >= 4; the accepted sixteen-sector prefix is unchanged). It asks that
      2.839272409e-6 be quoted with its hypotheses (globally H^2 corrections supported in 20 <= r <= 32 with sine
      frequencies >= 19; the unrestricted sharpw family ceiling is 2.84957773827575...e-6) and that section 6 state
      that the 021 and 022 held-out declaration followed their launches.
      theory audit 366 CONFIRMS numerical audit 268 (complete-plane Hessian energies and structured norms of 007, 016 and 017 by an
      independent polar second-derivative path; the kappa bounds for 016 and 017 are upper bounds, with no global
      theta bound and no inverse) and theory audit 367 CONFIRMS numerical audit 273 (radial partition of the 016 and 017 Hessian energies).
      theory audit 333 accepts the linear-estimates reviewer's second review of theory audit 314; theory audit 334 CONFIRMS its remarks R2 and R3 (negative Sobolev
      cutoff cost, H_q lower bound, residual sectors at and above gamma - 4). Theory audit 327 CONFIRMS the linear-estimates reviewer's mode-wise Mellin identity and optimal Hardy constant 1/n
      under the original domain assumption (the 007 application is smooth). Audit of
      theory exchange 05 (theory audit 312): all 36 table ratios CONFIRMED; REFUTED are the deductions that reductions of held-out
      or design probe values establish a reduction of the actual distance, that optimization records establish a
      span floor or a span limit of the earlier basis, that finite exact Beta sums are only FLOAT (they are
      certificates when the polynomial is the complete integrand), and the R2(e) sentence "no such framework
      exists" (none has been constructed or verified in this program); a the theory auditor summary decimal is corrected to
      25/54684 < 0.000457173. No candidate exclusion changes.
      OPEN pending review: theory audit 188. Theory audit 193 and theory audit 195 CONFIRM numerical audit 150 and numerical audit 158; theory audit 198 is a FLOAT diagnostic.
    - Own computations reproduced by the numerical auditor: theory audit 079 (numerical audit 086), theory audit 085 (numerical audit 085), theory audit 089 (numerical audit 087), theory audit 088 (numerical audit 089),
      theory audit 098 and the theory audit 099 cover (numerical audit 093, numerical audit 094), the theory audit 107 norms and the theory audit 112 cover (numerical audit 099, numerical audit 100), theory audit 123 (numerical audit 109), theory audit 127 (numerical audit 113), the theory audit 128 inequality and
      d = 12 matrices (numerical audit 116), the theory audit 129 d = 32 value (numerical audit 124), theory audit 141 (numerical audit 125), theory audit 143 (numerical audit 126, numerical audit 127), and the
      abstract theory audit 133 and theory audit 138 theorems (numerical audit 118, numerical audit 120, reviews by the numerical auditor), the theory audit 147 cover arithmetic (numerical audit 128,
      numerical audit 129).
  - OPEN own results awaiting a the theory team or the linear-estimates reviewer review: none of the origin series (theory audit 140, theory audit 145, theory audit 146, theory audit 153 are
    AUDITED). Theory audit 161 accepts numerical audit 133 to numerical audit 135.
  - Peer reproductions of numerical auditor results: numerical audit 111 (theory audit 162), numerical audit 123 (theory audit 155), numerical audit 131 (theory audit 156), numerical audit 121 (theory audit 166),
    numerical audit 137 (theory audit 167).
  - Other own proofs remain CLAIMED.
- The numerical auditor (verdict ledger in the accompanying artifacts, numerical audit 001 to numerical audit 206).
  - Reproductions of A2 and case 4: numerical audit 001 to numerical audit 016.
  - Point exclusions: numerical audit 017, numerical audit 022, numerical audit 023, numerical audit 034, numerical audit 040, numerical audit 045.
  - d2 components: numerical audit 024, numerical audit 026, numerical audit 043, numerical audit 050.
  - Global d2 matrix covers: numerical audit 031, numerical audit 035.
  - Background seminorms: numerical audit 030.
  - The four-branch family floor: numerical audit 032.
  - Weighted state 131 bound: numerical audit 038.
  - Candidate audits: numerical audit 039, numerical audit 044, numerical audit 048.
  - linear-estimate result 3 scalar boxes and point gaps: numerical audit 054 (CONFIRMED).
  - Stationary recursion through order 12: numerical audit 058 (CONFIRMED). candidate 002 sharp-ball gap: numerical audit 059 (CONFIRMED).
  - Mpen2 G0, G1: numerical audit 060 (CONFIRMED). Reproductions of theory auditor results: numerical audit 061 (theory audit 048 sharper radius), numerical audit 062 (theory audit 049
    without the gradient bound), numerical audit 063 (theory audit 047 witness points), numerical audit 071 (theory audit 055 snapshot gaps).
  - The numerics team generator moments: numerical audit 073. Scaled Cartesian jet evaluator: numerical audit 074. Both CONFIRMED, the general formulas
    through theory audit 076 and theory audit 077.
  - candidate 005: structure numerical audit 075 (CONFIRMED); point value and weak distance numerical audit 076 (CONFIRMED by theory audit 082); energies
    and kappa numerical audit 077 (CONFIRMED by theory audit 083); sharp-ball point gaps numerical audit 082 (CONFIRMED by theory audit 087). candidate 006: structure
    numerical audit 080 (CONFIRMED); point value and weak distance numerical audit 081 (CONFIRMED by theory audit 086); sharp-ball gaps and the signed
    obstruction theta_X = 6.4323 numerical audit 082 (CONFIRMED by theory audit 087). Direct generator route for 005, 006: numerical audit 084
    (CONFIRMED). b6 in the theory audit 067 boxes: numerical audit 083 (CONFIRMED by theory audit 090). Exact branch-specific Laurent packing: numerical audit 079 (CONFIRMED against the d2 residual cache).
    candidate 007: structure numerical audit 090 (CONFIRMED); point value and weak distance numerical audit 091 (CONFIRMED by theory audit 108, theory audit 110), exact
    kappa numerical audit 092 (CONFIRMED by theory audit 111), binary64 rounding numerical audit 096 (CONFIRMED by theory audit 117), the kappa discrepancy numerical audit 097
    (CONFIRMED by theory audit 118) and the one-point graded exclusion numerical audit 102 (CONFIRMED by theory audit 122). TP-2 velocity constants: numerical audit 088
    (CONFIRMED). Stationary recursion through order 16: numerical audit 098 (CONFIRMED). d2 weighted Laplacian norms numerical audit 099 and
    seven-cell cover numerical audit 100 (reproduce theory audit 107, theory audit 112). The linear-estimates reviewer refined probes: numerical audit 101 (CONFIRMED). numerics exchange 03 tail-cost sentence: numerical audit 103 (REFUTED;
    finite costs CONFIRMED). Full-plane G0 of candidate 005: numerical audit 104 (OPEN pending peer).
    candidate 008: structure numerical audit 105 (CONFIRMED), point value numerical audit 106 (CONFIRMED by theory audit 125), kappa numerical audit 107 (CONFIRMED by
    theory audit 126). Tail exponent self-correction: numerical audit 108. Finite angular recursion and the order-8 divisor: numerical audit 109 (CONFIRMS
    theory audit 123; checked by theory audit 134). Candidate driver regression: numerical audit 110. candidate 007 theta cover: numerical audit 111 (CONFIRMED by theory audit 162).
    candidate 005 ||rF||_2 and ||F||_H: numerical audit 112, numerical audit 117 (OPEN). candidate 007 DYADIC-Y modes: numerical audit 113 (CONFIRMS theory audit 127). candidate 009:
    structure numerical audit 114 (CONFIRMED), point value numerical audit 115 (CONFIRMED by theory audit 144). Parity budget: numerical audit 116 (CONFIRMS theory audit 128 and the d = 12
    matrices). Signed compression: numerical audit 118 (CONFIRMS theory audit 133 as an abstract theorem). Angular parity
    compression of candidate 008: numerical audit 119 (CONFIRMS theory audit 130 and theory audit 132 for the finite matrices; also checks closure review 015).
    Overlapping compressions: numerical audit 120 (CONFIRMS theory audit 138). candidate 009 full-plane kappa_HS: numerical audit 121 (CONFIRMED by theory audit 166).
    candidate 010: structure numerical audit 122 (CONFIRMED), point value numerical audit 123 (CONFIRMED by theory audit 155; comparison numerical audit 136). candidate 008 d = 32, union, signed and combined
    compressions: numerical audit 124 to numerical audit 127 (CONFIRM theory audit 129 at d = 32, theory audit 141 and theory audit 143 as finite computations).
    candidate 007 origin-ceiling cover: numerical audit 128 (independent cells with the exact H) and numerical audit 129 (CONFIRMS the theory audit 147
    arithmetic). closure review 016 incorporated: numerical audit 130. Rounded 007 realization: numerical audit 131 (CONFIRMED by theory audit 156). closure review 017
    incorporated: numerical audit 132. Theory audit 129 d = 12 values for d2, 005 and 007: numerical audit 133 to numerical audit 135 (CONFIRM). Theory audit 155
    comparison: numerical audit 136. Multi-scale moment enclosures (infrastructure): numerical audit 137 (CONFIRMED by theory audit 167).
    candidate 007 whole-plane G0: numerical audit 139 (CONFIRMS the norm-certification team). Theory audit 162 accepted: numerical audit 140. Theory audit 166 accepted: numerical audit 141.
    candidate 007 angular rule: numerical audit 142 (the ideal 180-point midpoint rule integrates |Lap F|^2 exactly; 160 odd modes,
    highest 319; this does not validate the FLOAT sample values or the radial quadrature). Theory audit 167 accepted: numerical audit 143.
    candidate 007 weighted Laplacian: first eight modes numerical audit 144 (CONFIRMED, partial norm 25.2509 at a = 0, a lower bound),
    all 160 modes numerical audit 147 (CONFIRMED by numerical audit 161 for eleven weights). numerics exchange 05 scope: numerical audit 145; matched weak probes: numerical audit 146 (k = 1 to 8 values OPEN).
    Polar Hessian calibration on state 131: numerical audit 148 (CONFIRMED). Gauss-Newton weak-pairing row algebra: numerical audit 149
    (CONFIRMED). Extended single probes and normalization: numerical audit 151 (OPEN). 007 span probe: numerical audit 152 (CONFIRMS theory audit 182).
    007 rF, G1, P2: numerical audit 153 (CONFIRMS the norm-certification team). 007 radial annuli modes 17 to 31: numerical audit 154 (OPEN). candidate 012 structure:
    numerical audit 155 (CONFIRMED; point screen CONFIRMED by theory audit 204, numerical audit 167). 007 ||F||_Hdot^-1 = 0.6355297981: numerical audit 156 (inside the norm-certification team's independent enclosure [0.6355243760, 0.6355322686], VALIDATED 05:52Z; the enclosure is CONFIRMED by numerical audit 249). Mode-7 probe: numerical audit 157
    (CONFIRMS theory audit 185). Exact basis rank 1922, kernel 1060 zero-potential directions: numerical audit 158 (CONFIRMED by theory audit 195,
    numerical audit 163). Radial quadrature errors: numerical audit 159 (CONFIRMS theory audit 193). 80-probe scan: numerical audit 160 (OPEN). Weighted Laplacian
    at eleven weights: numerical audit 161 (CONFIRMS the norm-certification team). Third polar tensor calibration on state 131: numerical audit 162 (CONFIRMED).
    Constraint differential rank 426 at 007 (Taylor residuals nonzero, about 1e-11): numerical audit 164 (CONFIRMED by
    theory audit 209, numerical audit 171). 007 leading
    density harmonic: numerical audit 165 (CONFIRMS theory audit 203). 007 Q3 = 5599.0968130: numerical audit 166 (CONFIRMS the norm-certification team). 012 point values:
    numerical audit 167 (accepts theory audit 204). 007 dyadic cells with lower-endpoint logic: numerical audit 169 (CONFIRMS the norm-certification team's dyadic Laplacian condition
    cells, ratio > 1.38601388). Theory audit 207 polar method: numerical audit 170 (CONFIRMS). Common leading profile of state 131, d2 and
    005 to 012: numerical audit 172 (CONFIRMS theory audit 210). Taylor repair of 007: numerical audit 173 (CONFIRMS the theory audit 211 arithmetic; distance >
    0.004769166863 for the repaired potential), numerical audit 174 (combined norm 3.2646e-12, OPEN). Exact 1922-coordinate
    representation of 007: numerical audit 175 (CONFIRMED by theory audit 230, accepted in numerical audit 185). 008 frozen probes: numerical audit 176 (CONFIRMED by theory audit 225; mode 7 >
    0.001938714194, mode 1 > 0.000264056894). 007 branch tail harmonics: numerical audit 177 (CONFIRMS the theory audit 222 numbers).
    009 frozen probes: numerical audit 179 (CONFIRMED by theory audit 231, accepted in numerical audit 183; mode 7 > 0.016967603955, mode 1 >
    0.001882466902). 007 complete-component norm comparisons: numerical audit 180 (CONFIRMS the norm-certification team; sharpw ratio > 3596535.57;
    accepted in theory audit 238). 012 frozen probes: numerical audit 182 (CONFIRMED by theory audit 236; mode 7 > 0.018641021006, mode 1 >
    0.007136211144). independent reviews of the Taylor projection and the finite dilation chart accepted: numerical audit 184. 008
    seven-cell dyadic test: numerical audit 186 (CONFIRMED by theory audit 248; every cell ratio above 4.64864536); 009: numerical audit 187
    (CONFIRMED by theory audit 250; above 1.02032822). Numerical audit 188 accepts theory audit 236 (012 floors 0.018641021007 and 0.007136211145).
    007 lower-tail recurrence: numerical audit 189 (CONFIRMS theory audit 235); numerical audit 192 accepts theory audit 234. Numerical audit 193 accepts theory audit 248 and theory audit 250. 010 weak-test
    backend: numerical audit 190 (CONFIRMED by theory audit 257, accepted in numerical audit 203), numerical audit 191 (CONFIRMED by theory audit 267, accepted in numerical audit 210), numerical audit 196
    (polynomial specialization, reproduces 007), numerical audit 205 and numerical audit 207 (010 frozen mode 7 and mode 1 distances
    above 0.022479506978 and 0.00062746942; numerical audit 205 CONFIRMED by theory audit 270 and bound in numerical audit 215, whose two
    display mantissas numerical audit 217 corrects; numerical audit 207 CONFIRMED by theory audit 274, accepted in numerical audit 219). 013: numerical audit 197 (source,
    sectors, origin identities), numerical audit 199 (007 calibration of the n = 21, K = 522 probe), numerical audit 200 (distance >
    0.001123713803, CONFIRMED by theory audit 263), numerical audit 201 (point gaps, CONFIRMED by theory audit 266, accepted in numerical audit 208), numerical audit 204 (CONFIRMS theory audit 255). Numerical audit 198
    CONFIRMS the theory audit 251 candidate arithmetic. Numerical audit 195 (a q4 sector omitted by the numerics team's finite far-field weak model) is
    CONFIRMED by theory audit 275 (accepted in numerical audit 220). Numerical audit 209 (CONFIRMED by theory audit 276, accepted in numerical audit 221): the exact whole-plane first-sine pairings of 007 at 15 large indices differ from the numerics team's
    finite 30-sector far-field model by relative errors from 6060.9 (K = 3162) to 1.4e-13 (K = 1e10), and the last
    retained model term is smaller than the actual error at every one of them, so it is no error bound. Numerical audit 211
    REFUTES three numerics exchange 07 inferences (damped-trial bracket and span floor, 014 held-out provenance, bare-profile
    localization). 014: numerical audit 212 (exact structure, CONFIRMED by independent arithmetic), numerical audit 213 (point gaps, CONFIRMED by theory audit 279) and
    numerical audit 214 (distance > 0.00198301351067 from the design probe n = 21, K = 522, CONFIRMED by theory audit 280). Numerical audit 222
    (OPEN): an explicit uniform ceiling on the separated first-mode weak test of 007 for all K >= 10^8
    (m_K < 9.5229795649224e-5); it bounds a test value, not a correction distance; numerical audit 225 extends it to the
    complete test with the combined denominator (both CONFIRMED by theory audit 285, which gives U(3000000) = 0.00363271755).
    numerical audit 223 and numerical audit 224 accept the theory auditor's independent 014 paths (theory audit 279, theory audit 280). Numerical audit 226 (OPEN): an exact moment
    primitive with positive radial poles (a = 624 represents radius 25), no candidate evaluated yet. Numerical audit 146, numerical audit 151
    and the k-part of numerical audit 091 are reproduced exactly by the norm-certification team (06:09Z), so CONFIRMED by the contract rule.
    numerical audit 227 (OPEN review): a scaled factored weak backend for radii 1, 10, 25, 100, calibrated by reproducing the
    accepted 013 root 0.00199234339099; no new candidate. Numerical audit 228 and numerical audit 230 accept theory audit 282 and theory audit 285, and numerical audit 230
    reproduces theory audit 285's cutoff K0 = 3000000 independently. Numerical audit 229 (OPEN): 25 held-out probes registered at
    06:10:00Z before 015 and 016 were inspected. Numerical audit 231 (CONFIRMED by theory audit 303): 010 dyadic cell witnesses (row 79). Numerical audit 232
    CONFIRMS the numerics team's statement that 006 to 014 share 007's first four profiles, all 90 tail-recurrence condition coefficients
    zero (a finite list, not a remainder certificate). Numerical audit 233 CONFIRMS the 015 structure; numerical audit 234 gives its
    point gaps (CONFIRMED by theory audit 299). Numerical audit 235 CONFIRMS that the 25 registered probes lie outside the documented 015
    objective span. Numerical audit 238 CONFIRMS the norm-certification team's first-sine distances for 008 (> 0.0040334973 at K = 512, > 0.0363233974 at
    K = 2048). Numerical audit 239 (OPEN) gives the 015 distance > 0.003033479200692 at (23, 2400). Numerical audit 237 (015
    distance > 0.001232449584356253 at (23, 600)) is CONFIRMED by theory audit 304. Numerical audit 240 CONFIRMS theory audit 292 (six weighted-tail
    extensions). Numerical audit 241 accepts theory audit 299 and theory audit 298. Numerical audit 242 verifies the 016 structure and point gaps (gaps CONFIRMED
    by theory audit 307). Numerical audit 243 CONFIRMS that the 25 registered probes lie outside the 016 objective span and corrects a
    coordinator note: (19, 1800) is a registered probe. Numerical audit 244 and numerical audit 245 accept theory audit 303 and theory audit 304. Numerical audit 246 gives 016
    distances > 0.001092633159 at (23, 2400) (CONFIRMED by theory audit 310) and > 0.001470360924 at (19, 1800) (CONFIRMED by theory audit 311). Numerical audit 247 (OPEN) calibrates
    an R0 = 50 backend for 017. Numerical audit 248 (CONFIRMED by theory audit 321): exact potential rank 2174 for 016 and a nonzero mode 17
    density coefficient. Numerical audit 249 CONFIRMS the norm-certification team's whole-plane 007 enclosure of ||F||_Hdot^-1. Numerical audit 251 accepts
    theory audit 307's 016 point proof. Numerical audit 252 CONFIRMS the norm-certification team's complete 007 E_2 and N_s assembly. Numerical audit 253 accepts theory audit 310 and
    theory audit 311 (both 016 distances). Numerical audit 254 verifies the exact 017 structure and finds positive gaps for every
    registered point budget (F(1/10, 73/100) = 0.0899392743, uniform graded gap 0.0695362257; point part CONFIRMED by
    theory audit 319). Numerical audit 255 CONFIRMS that the 25 registered probes and (21, 522) lie outside the 017 objective span. Numerical audit 256:
    017 distance > 0.001068502321536437 at (23, 2400) (CONFIRMED by theory audit 320). Numerical audit 257: > 0.00167183069831928 at
    (19, 1800) (CONFIRMED by theory audit 331; the numerical auditor accepts the reproduction, numerical audit 267). Numerical audit 258 reproduces theory audit 313 (016 sector
    prefix). Numerical audit 259: 017 diagnostic (21, 522), outside the registered 25-probe family, distance > 0.000596123050
    (1.303 times the graded ceiling; CONFIRMED since matrix v136 through the numerical auditor's numerical audit 384, accepted by the theory auditor in theory audit 460).
    numerical audit 260, numerical audit 261 and numerical audit 262 accept theory audit 319, theory audit 320 and theory audit 323.
    numerical audit 263 CONFIRMS theory audit 321 and its R0 = 50 specialization (potential dimension 2174 at both scales). Numerical audit 264 (OPEN
    review): a backend for snapshots that mix the scales 25 and 50; it passes its fixtures and certifies no snapshot.
    numerical audit 265 (OPEN): 016 diagnostic (21, 522) distance > 0.000412454461, below the graded ceiling (0.902 times); the
    registered 016 distances (numerical audit 246 with theory audit 310, theory audit 311) already exclude every ball of rows 80 and 81. Numerical audit 266
    (OPEN): complete envelope bounds for the probes (19, 1800), (21, 522), (23, 2400) of 016 and 017 match the
    FLOAT diagnostics to relative 2e-7; the complete-test root exceeds the envelope root by a factor 1.6295 to
    1.7728, chiefly through the conservative envelope denominator. No verdict changes. Numerical audit 268 (CONFIRMED by
    theory audit 366): complete-plane Hessian norms of 016 and 017 and strict upper bounds kappa < 0.735053672993720766
    (016) and kappa < 0.729080538628955349 (017) under the audited gradient-commutator theorem; no global theta
    bound, so no signed margin follows. Numerical audit 269 accepts theory audit 322 (density rank 2174 at R0 = 25 and 50). Numerical audit 270 (CONFIRMED
    by theory audit 342 and theory audit 343): 018 exact structure and point gaps (above). Numerical audit 271 CONFIRMS the 018 objective-span
    separation. Numerical audit 272: 018 registered distances above 0.001655825792 at (19, 1800) (CONFIRMED by theory audit 345)
    and 0.001328016044 at (23, 2400) (CONFIRMED by theory audit 349), both above the graded ceiling. Numerical audit 273 (CONFIRMED by theory audit 367): exact radial partition of
    the 016 and 017 Hessian energies; the exact annulus kappa differs from the saved FLOAT value by less than 1.7e-12
    and more than 99.998 percent of the omitted squared kappa lies beyond the outer mesh radius. Numerical audit 274 (CONFIRMED by
    theory audit 348): abstract potential and density dimension 2426 of the space with both legqs scales 25 and 50 (the basis
    of candidate 020, snapshot 08:46:18Z); the actual 020 shapes are bound to it by numerical audit 292. Numerical audit 275 to numerical audit 278 accept the theory auditor's 018 reproductions:
    point fields and gaps (theory audit 342), the (19, 1800) distance (theory audit 345), the complete sector maps (theory audit 343) and the
    origin normalization (theory audit 346). Numerical audit 279 (CONFIRMED by theory audit 353 to theory audit 355): 019 exact structure, normalization and point gaps.
    numerical audit 280 CONFIRMS the 019 objective provenance and span separation. Numerical audit 281 accepts theory audit 348. Numerical audit 282 (CONFIRMED by
    theory audit 357): 019 distance above 0.001661806967193251 from the registered probe (19, 1800). Numerical audit 283 accepts theory audit 349
    (018 distance above 0.001328016044638112 from (23, 2400)). Numerical audit 287 to numerical audit 290 accept the theory auditor's 019 reproductions
    (theory audit 353, theory audit 354, theory audit 355, theory audit 357). Numerical audit 291 (CONFIRMED by theory audit 360 to theory audit 362): 020 fixed c, origin, vanishing
    forbidden sectors and positive point and uniform graded gaps. Numerical audit 292 CONFIRMS the 020 actual shapes and objective span separation.
    numerical audit 284 (CONFIRMED by theory audit 378, accepted in numerical audit 311): exact whole-plane representation of the 017 density gradient. Numerical audit 285: its
    rational Bernstein range method is CONFIRMED by theory audit 377 and numerical audit 310 accepts that review. Numerical audit 309 completes the cover (247 leaves, none pending):
    theta <= 2/25 and c + 1 - theta - kappa > 2.00123867 for 017, CONFIRMED by the theory auditor's independent replay of
    all 247 leaves at 2048 bits (theory audit 400, result 373804ee...; accepted by the numerical auditor in numerical audit 329, result ecb83651...). No inverse follows. 017 stays RULED OUT
    by its distance certificates. Numerical audit 286 (OPEN): analytic spans of the proposed 021 and 022 objectives. Numerical audit 293 (CONFIRMED by theory audit 363): 020
    distance above 0.001855374677442712 from (19, 1800). Numerical audit 294 (CONFIRMED by theory audit 369): abstract dimension 2414 of a
    proposed higher-angular radius-25 family. Numerical audit 295 CONFIRMS that the 180-node angular midpoint rule is exact at each fixed
    radius for the residual derivative squares through order 2, the density Hessian squares and the odd weak
    pairings n <= 47 of the actual 020 shapes and the proposed 022 shapes (ideal nodes only; no bound on floating
    evaluation, radial quadrature or the omitted domain). Numerical audit 296 to numerical audit 299 accept the theory auditor's 020 reproductions
    (theory audit 360, theory audit 361, theory audit 362, theory audit 363). Numerical audit 300 REFUTES the test-A table calibration of the norm-certification team's legqs norm extension
    as a domain-valid integral calibration (45 of 810 requested moments diverge; the production accumulator is not
    refuted) and numerical audit 301 REFUTES the original 57-panel partition of its quadrature check (overlapping origin panels;
    the repair is CONFIRMED); the norm-certification team's legqs norms stay OPEN. Numerical audit 302 CONFIRMS the scaled radial integrator and the
    small-field norm assembly on an admissible finite test set (2383 comparisons) and numerical audit 305 CONFIRMS one complete
    six-generator synthetic fixture (fields, residual derivatives through order 2, four whole-plane norm
    enclosures); neither certifies an actual 016 or 017 norm. Numerical audit 308 CONFIRMS the numerical auditor's own exact scaled Laurent
    multiplication and derivative code on 24 manufactured pairs and the six-generator fixture (1530 exact
    identities); the production 016/017 residual norms stay OPEN. Numerical audit 303, numerical audit 304 and numerical audit 306 accept theory audit 366, theory audit 367 and
    theory audit 369, so numerical audit 268 (kappa_007 < 0.728164680182325428, kappa_016 < 0.735053672993720766, kappa_017 <
    0.729080538628955349; upper bounds only), numerical audit 273 and numerical audit 294 are CONFIRMED in both directions.
    numerical audit 312 CONFIRMS the numerical auditor's closed density-difference norm fixtures (the verification inputs in the accompanying artifacts 9dd42edd...). Numerical audit 313 (general
    compatibility lemma CONFIRMED by theory audit 393; actual pair norm CONFIRMED by theory audit 394, result 5ec95333...; both
    accepted by the numerical auditor in numerical audit 322, result 6b2e9d95...; the theory team's review closure review 041 of the lemma CONFIRMED in numerical audit 324)
    encloses ||rho021 - rho020||_2 in an interval about 0.0073492532497197 at 1875 bits (result 51a12910...): the screening rule
    comparisons fail for the graded, sharpw and TB ceilings, which transfers no exclusion. Numerical audit 314 (result
    f6711daf...; CONFIRMED by the theory auditor's theory audit 387, point fields and gaps, results 42b8ef6e..., theory audit 388, center relation,
    213afe32..., and theory audit 389, sixteen-sector prefix, fe7c0a0b...; the numerical auditor accepts all three in numerical audit 319, result
    0c7f6048...): 021 origin normalization, forbidden prefix and failed point tests.
    numerical audit 315 CONFIRMS the actual 021 shapes and the 81 recorded rows (result db86063a...); theory audit 395 CONFIRMS the span
    application for the current recorded objective (result e7da2cea...), accepted by the numerical auditor in numerical audit 323 (result
    c202d977...).
    numerical audit 316 (result cf4855e5...; CONFIRMED by theory audit 392, proof a93de1e5..., result a2524cf4...; accepted in numerical audit 320, result 9008a8e6...): 021 fixed-c L^2 distance
    from (19, 1800) above 466174213699793/250000000000000000, 63 exact radial groups at 2048 bits, minimum 1934 bits.
    numerical audit 317 (OPEN pending independent reproduction; evidence 09a34d21...): for the exact 021 field the recorded MID16,
    MID24 and MID32 radial rule errors of the mode-19 pairings at K = 137, 521, 1800 are positive and about 2e-14
    (relative at most 1.67e-8); no bound for other modes or iterates follows.
    numerical audit 321 (result 44ee4cd4...): actual 022 shapes, inherited rank application and recorded 67-row objective span
    CONFIRMED; the manifest in the accompanying artifacts statement on modes 31 to 47 REFUTED (mode 31 overlaps). Theory audit 403 (result 9dea5cb7..., proof
    475e61a8...) replays this independently and CONFIRMS it for parent 016 and both recorded 022 stages; the numerical auditor
    accepts theory audit 403 in numerical audit 331 (result 81f34093...).
    numerical audit 325 (result 0ed0a375...), numerical audit 326 (result 0a97a301...) and numerical audit 327 (result fb9f8033...), the numerical auditor's own exact
    computations for 022, each CONFIRMED as its own calculation (numerical audit 326 independently CONFIRMED by the theory auditor: point
    fields and gaps theory audit 405, result 25ef41a6...; center relation and density slope theory audit 406, result 1f043e39...;
    complete sixteen-sector prefix theory audit 407, result f7bd59c9...; numerical audit 327 independently CONFIRMED by the theory auditor's theory audit 408,
    result 0fcd89ad...; the numerical auditor accepts theory audit 405 to theory audit 407 in numerical audit 333, 11:22Z, result c598de89..., and theory audit 408 in numerical audit 334,
    11:23Z, result 7515f75f...; numerical audit 325 OPEN pending replay): the 022
    minus 016 density difference norm 0.0088109875626 (all three sufficient transfer screens fail); exact c,
    c + strain = 1, a0 = 10.31182777938, eleven of 16 sectors exactly zero, first surviving exponent about minus
    2.79044, F = 0.08875964290 at (1/10, 73/100) against the graded point allowance 0.02039863807; fixed-c L^2
    distance above 0.00135251075726327 from (19, 1800).
    numerical audit 335 (11:28Z, result 3e6fabd0...): The numerical auditor checks the published theory exchange 07's numerical scope, nine ratios and 65
    Appendix H bindings and ACKs it; it finds the same two stale 022 status sentences as the theory auditor's theory audit 412.
    numerical audit 336 to numerical audit 338 (11:33Z to 11:38Z; the numerical auditor's computations for 023, reproduced independently by the theory auditor in theory audit 416
    to theory audit 420 and accepted in numerical audit 348 to numerical audit 350, 12:07Z, results 3fc79b7b..., b9f961dd..., a3c8ef02...):
    actual 023 shapes and both recorded stages on the same 67 rows as 016, all 60 probes outside the analytic span
    (numerical audit 336, result 12ea208e...); F = 0.083280868582953659827... at (1/10, 73/100), all six scalar point gaps
    positive, original graded gap 0.062882815459541270946..., c + strain = 1, a0 = 10.30469840811666... (numerical audit 337,
    result cc9fad61...); fixed-c L^2 distance above 0.002634958245163687 from (19, 1800), 5.763 times the graded
    ceiling (numerical audit 338, result 89695b56...).
    numerical audit 339 (11:41Z, result 804abf8a...; the numerical auditor's own, reproduced independently by the theory auditor in theory audit 419): the complete 023 prefix
    through exponent -7/2, eleven of sixteen sector labels zero, the five nonzero labels as in 016, and the first
    four potential, density and stream coefficients equal to 007's.
    numerical audit 347 (12:01Z, result 3f217ca5...): the numerical audit 341 production's field and norm routines are the numerical auditor's own; its
    fixture helper imports frozen copies of peer modules, so the flag “foreign code executed: false” is to be read with
    the saved flag “frozen peer modules imported for own fixture helpers: true”; numerical audit 341 is unchanged.
    numerical audit 343 to numerical audit 345 (the numerical auditor's own, reproduced independently by the theory auditor in theory audit 427 to theory audit 431, review record 212, 12:30Z,
    results d9dbfdf5..., e252fb1a..., d0e99fd9..., c42057b9..., ee1d08b9...; the distance by a polar
    reconstruction from the frozen raw list with all 63 complete moments at 2048 bits, minimum accuracy 1937 bits):
    for 024, F = 0.0952808775288636068... at
    (1/10, 73/100) with all six scalar point gaps positive and the original graded gap 0.0748700396..., a0 =
    10.3120028633... > 0 and all eight forbidden sectors zero (numerical audit 343, evidence 8a07d77b...); a fixed-c L^2
    distance above 0.001556067368832641 from (19, 1800), 546.06 times the sharpw family ceiling and 3.403 times the
    graded ceiling (numerical audit 344, evidence 7da0b4ff...); the prefix through exponent -7/2 with eleven of sixteen labels
    zero (numerical audit 345, result f897d69d...). Numerical audit 346 (result 490ad1a4...) reconstructs the earlier held-out hash
    58586004... byte for byte from the numerics team's stated single edit; the two save times are not independently witnessed.
    numerical audit 342 (11:52Z, result a0f6be30...; the numerical auditor's own): the 024 basis (2174 exact shapes equal to 016's), rows and
    history (5 accepted and 7 rejected updates); the current held-out hash e171c051... and all 60 probe pairs outside
    the 67 rows; index in the accompanying artifacts's MID16 loss labels are wrong (the optimizer used MID 32), and 024 ran on CUDA while 016 ran
    on CPU. The numerical auditor accepts the theory auditor's reproductions in numerical audit 357 (point fields, origin and prefix: 45, 13 and 159 checks,
    proof f3968243...), numerical audit 358 (shapes, rows, probes, history and the reverse-edit hash: 21 checks, 50 bindings,
    proof bcb28f09...) and numerical audit 359 (the complete weak distance: 349 comparisons, root
    0.00155606736883264282..., proof 2d20fc50...), all completed at 12:48Z.
    numerical audit 330 (result 000a7199...): The norm-certification team's two calibration source repairs (admissible testA exponents; quadrature
    panels covering [0, 1] exactly once) CONFIRMED. Numerical audit 340 (11:42Z, result 51574b9e...) CONFIRMS the repaired
    calibration runs (813 moment instances at 1536 bits; synthetic G0 and rF agree to about 1.1e-16) and REFUTES
    two readings: that the quadrature's residual point values are exact rationals, and that both saved Boolean
    tests passed (N0 is false, numerics team true); a truncation and rounding certificate for that quadrature stays OPEN.
    The norm-certification team (10:00Z): candidate 016 whole-plane G0 in [0.30888644514252473677..., 0.30888644514252473678...] at 1024 bits,
    the first complete norm of a legqs candidate; rF = 7.1457011753644571831... (10:42Z note); both CONFIRMED by
    the numerical auditor's independent exact production numerical audit 341 (11:46Z, comparison 31b509e0..., minimum 1739 bits, no spatial
    quadrature): G0 in [0.308886445142524736777066916039, 0.308886445142524736777066916042] and ||rF||_2 in
    [7.145701175364457183129953068728, 7.145701175364457183129953068731]. G1 = 3.7269069480198839980... (10:42Z note,
    1024 bits, CLAIMED); P2 in [218.104089397824118537999, 218.104089397824131729927] (record COMPLETE 10:51:04Z,
    sha256 7e5b1df9..., CONFIRMED by numerical audit 392); E_* about 547.861, above 007's 517.10. Numerical audit 332 (result 5aa239d9...)
    CONFIRMS the
    registered 016 arithmetic conditional on these four intervals (E_* in [547.86114589649582760,
    547.86114589649583286]) and REFUTES the frozen legacy X3 lower-comparison ratio 89738515.78 as an exact-source
    transcription (exact-source ratio about 89738286.04); G1 is CONFIRMED by numerical audit 373 (13:28Z); P2 is CONFIRMED by
    numerical audit 392 (15:10Z: strict interval (218.104089397824118537999059607229, 218.104089397824131729926375547616), 45648
    ordered branch pairs, minimum 1690 bits). Numerical audit 374 (13:37:41Z), CONFIRMED by the theory auditor's theory audit 451 (13:53:53Z, 318 checks
    at 1024 bits;
    accepted by the numerical auditor in numerical audit 380, 13:56:22Z), uses
    only G0, G1 and Plancherel to show that every registered scalar forcing test fails for 016 (directed ratios above
    790483392 for A2-Db, 4751141 for sharp Sobolev, 6593837 for sharp L2 and 3542234 for sharpw); this is a failed
    sufficient test, not an exclusion or a nonexistence result, and lower bounds for different candidates do not order
    them. The norm-certification team's second arithmetic path (note 13:49Z, CLAIMED) gives a G0 ball overlapping the production enclosure;
    rF, G1 and P2 follow.
    numerical audit 318 CONFIRMS that the norm-certification team's four frozen production source modules match its production record (source audit in the accompanying artifacts
    a3328767...) and keeps the norm values OPEN.
    The norm-certification team (12:15Z note, CLAIMED pending the numerical auditor): for 016, six exact weak probes, a mode-wise Hardy bound
    H <= 0.7890225617 (FLOAT H 0.6178), hence E_2 in [547.861, 674.967], and all seven origin inverse condition cells
    excluded (minimum ratio above 1.2539 on [0, 1/4]). Numerical audit 351 (12:23Z) finds that the note's summary table drops eleven
    negative exponents kept in the JSON (e7157577...) and asks for the conditional distance wording; this is a
    transcription correction, not an acceptance. Numerical audit 353 (12:35Z, result f80a4f27...) CONFIRMS the norm-certification team's three
    complete weak comparisons at (21, 522), (23, 2400) and (19, 1800) and their coarser-cap distance floors
    (> 0.0004124170686079752, > 0.001092320910098932, > 0.001469803668568211). Numerical audit 360 (13:04:31Z, proof
    85941979..., result 08ee4718...) CONFIRMS the remaining three (frozen n7 and n1 vectors and the first mode at
    K = 2048; floors > 0.000031482656587838, > 0.000092553708437694, > 0.000232238534078884; the norm-certification team's displays
    3.1482656587840e-5 and 2.3223853407889e-4 round the roots up), so all six probes are reproduced; the Hardy
    bound stays CLAIMED. Numerical audit 352 REFUTES the reading of screening condition with a residual difference (tau must bound
    \|\|rho_child - rho_parent\|\|_2). Numerical audit 355 (completed 12:46:27Z, proof af2715bf..., result 16a4a6ac..., 2048 bits, 704.7 s,
    after the 007 calibration numerical audit 354) computes J(1/4) = 19.914089787522834591... and J(7/4) =
    11.176463132526294910... for 016 independently; the norm-certification team's displayed squared-norm intervals contain them, and
    with J nonincreasing in a all seven cells fail (ratios above 1.253908386497 to 174.316921039151), so the
    seven-cell test is CONFIRMED, conditional on the origin-inverse, realization, plateau, dyadic partition and
    absorption hypotheses of its proof; the norm-certification team's five other endpoint norms are not reproduced. Numerical audit 356 (12:47Z,
    proof fbb936cb..., result 0729f9cf...) audits numerics exchange 12: it REFUTES the blanket summaries 'K = 600
    probes fall by factors 3 to 30' (n = 19 worsens by a factor 24.94; n = 29, 31 improve by less than 3) and
    'K >= 1200 probes rise by 25 to 40 percent' (ratios 3.491 and 0.3323 occur), notes that the 14-row table
    reports m proxies, that the 024 MID16 labels remain wrong, that rounded FLOAT step sums are not certified
    density-difference bounds and that rounded-up lower-bound factors must be rounded down, and CONFIRMS the
    source-level distinctions; no exclusion changes. The theory auditor's theory audit 435 (12:56Z, proof 026501ef..., 67 checks)
    REFUTES the same universal FLOAT ranges independently, with further counterexamples ((31, 1800) rises 1.57-fold
    for 024 and 3.37-fold for 023), and finds the same defect in the 026 section of the final numerics report in the accompanying artifacts ((19, 600)
    rises 2.508-fold; (23, 900) rises 3.36-fold); it CONFIRMS the corrected comparisons and the rounded-down
    witness factors.
    For 015, numerical audit 383 (14:14:52Z, the candidate015 three weak peer material in the accompanying artifacts, result c9350681..., 23 checks) accepts the norm-certification team's
    complete weak tests at (19, 600), (23, 600) and (23, 2400) against the numerical auditor's own numerical audit 237 and numerical audit 239, with the global
    probe-gradient cap of numerical audit 253 (sharp strict floor at (23, 2400) 0.003033479200692324, so the numerical audit 239 distance is
    CONFIRMED; its first-mode part stays OPEN). Numerical audit 382 (14:11:34Z) gives the 015 dyadic exclusion of row 105. For 017,
    numerical audit 384 (14:21:08Z, result 4f49a7b9..., 26 checks) adds the independent reproduction of the norm-certification team's (21, 522) weak
    test, a diagnostic outside the registered 25-probe family, to the two registered 017 tests accepted earlier; the
    sharp strict floors are 0.000596123050327423, 0.001068502321536437 and 0.00167183069831928. CLAIMED pending the numerical auditor
    (the norm-certification team, 14:08Z to 14:22Z): the sixth 017 probe (first mode, K = 2048, m >= 1.931752174483e-4), the mode-wise Hardy
    bound H <= 0.787447783373 for 017 with E_2(017) in [521.792690154, 653.510428201], the 017 seven-cell test
    (superseded by the numerical auditor's own numerical audit 389 with theory audit 463, row 106) and the second-path 016 rF and G1, which overlap the
    production enclosures.
    The norm-certification team's H18 result for 016 (note 15:05Z, CLAIMED pending the numerical auditor): a duality lower bound ||F||_H >= 0.6167335007
    from the 16 odd modes 1 to 31, below the Hardy bound, so H(016) lies in [0.6167335007, 0.7890225617] and E_2(016)
    in [628.58, 674.97]; the numerical auditor replays modes 1 and 3 in numerical audit 396 (below), and the 16-mode floor stayed CLAIMED until
    numerical audit 416 (17:03Z, CONFIRMED by the numerical auditor). The norm-certification team's
    deep run (note 15:16Z) gives mode-1 and mode-3 lower values 0.376998030138416 and
    0.371766751200801 with exact rational test vectors; by theory audit 467, independent floors 0.376 and 0.371 for these two
    modes would give E_2(016) > 608.121275, above the accepted 007 upper bound 606.820219. Numerical audit 396 proves both floors
    (strict floors 0.376998030138416982 and 0.371766751200801401, E_2(016) > 608.392385921614 > 606.820219), CONFIRMED
    by the theory auditor in theory audit 470. Numerical audit 394 REFUTES the
    inference that their basis stability proves intrinsic Hardy slack.
    numerical audit 391 (15:07:46Z, result record 03 in the accompanying artifacts e1c86db1..., 28 checks) CONFIRMS the repaired 007 Q3 status of the norm-certification team's final tables
    (numerical audit 166) and REFUTES two blanket citation scopes there (Mpen2 under numerical audit 024/026; 001's finite P2 and Q3 columns
    under numerical audit 028); those finite values stay OPEN, not numerically refuted.
    numerical audit 250 audits numerics exchange 08 (refutations below; the stated global first-mode maximum
    0.000173 at k = 12288 is OPEN, since numerical audit 230's all-k tail bound does not fix the maximum below its cutoff). Numerical audit 236 CONFIRMS the norm-certification team's
    complete 007 norms ||D^2 F||_2 about 83.43567352, ||r D^2 F||_2 about 114.87118375 and ||(1 + r^2)^(-1/10) grad F||_2 about 2.92405175.
    numerical audit 216 (CONFIRMED by theory audit 282, finite list): complete 007 weak
    distances at six large radial indices, all below the CONFIRMED mode 7 value 0.004769166867; the numerics team's frozen C
    envelope estimates are not upper bounds there. Numerical audit 218 CONFIRMS the numerics team's exact quotient starting states for 007
    and 013 (coordinates only).
  - Refutations:
    - The numerics exchange 01 tail inferences (numerical audit 041).
    - The norm-certification team decimal coefficient conversion (numerical audit 042).
    - The manifest radial degrees.
    - The numerics team negative-norm outer-outer factor (numerical audit 067).
    - The numerics exchange 02 radial-mass reading for candidate 005 (numerical audit 078).
    - Two numerics exchange 05 status passages (numerical audit 145) and the reading of its 14 percent difference as a quadrature error (numerical audit 146).
    - The MID8 radial rule for the low-k weak pairings of 007 (numerical audit 150; signs reverse at k = 0 to 2).
    - The general upper-endpoint exclusion logic of the norm-certification team's frozen the dyadic Laplacian script in the accompanying artifacts (numerical audit 168); the 007 cells stand
      (numerical audit 169).
    - The numerics team's 03:52Z statements that the 426 physical constraints absorb 38 of the 1060 zero-potential directions and
      that damping makes physical steps independent of redundant coordinates (numerical audit 178, CONFIRMED by theory audit 228).
    - Generic direction preservation of the norm-certification team's nearest-decimal endpoint helper (numerical audit 181, accepted in theory audit 238); the
      published intervals stand.
    - The two exact interpretations in numerics exchange 06 (exact nullity and damping, numerical audit 194), withdrawn by the numerics team.
    - Its own numerical audit 196 schema description (numerical audit 202) and two recorded decimal displays (numerical audit 206); stored results unaffected.
    - Three numerics exchange 08 statements (numerical audit 250): that improvement after adding independent basis directions shows the
      earlier plateau was a span limit (exact nested-space counterexample; the actual old-space optimum is OPEN), the
      signed-sum label of the bridge table (magnitudes are stored; at k = 1e5 and 1e6 both exact signed pairings are
      negative), and the description of the new 016 density support as modes 19 to 31 (mode 17 occurs).
    - Two sentences of this report (frozen 13:57Z save, a86713e5...): that the H enclosure of 007 was still running
      with only lower N_s bounds certified, and that only d2 had a certified ||F||_H (numerical audit 381, 14:02:21Z, result
      5cde7b12..., 22 checks). Numerical audit 381 also finds the phrase 'smallest certified forcing-norm ratio' OPEN: 007's
      ratio comes from a two-sided enclosure, 016's only from a lower bound, and lower bounds do not order actual
      ratios. All three passages are repaired in this version.
    - Three sentences of the norm-certification team's 015 weak-test record (numerical audit 383) and the same three in its 017 record (numerical audit 384): a
      generic relative change below 1e-5, a generic Bernstein label for monomial rows, and 'distance from F' (the
      distance is from the reference density). The floors stand.
  - Confirmed by the theory auditor: numerical audit 051 (theory audit 053), numerical audit 053 (theory audit 044), numerical audit 055 (theory audit 049), numerical audit 056 (theory audit 061), numerical audit 057 (theory audit 048),
    numerical audit 064 and numerical audit 065 (theory audit 064), numerical audit 067 (theory audit 066), the numerical audit 046 and numerical audit 049 theta witnesses (theory audit 046), the numerical audit 054 cutoffs
    (theory audit 043 record) and d2 conversions (theory audit 055), numerical audit 047 (theory audit 069), numerical audit 066 at four radii (theory audit 078), numerical audit 069 (theory audit 075),
    numerical audit 070 (theory audit 068), numerical audit 076 (theory audit 082), numerical audit 077 (theory audit 083), numerical audit 081 (theory audit 086), numerical audit 082 (theory audit 087), numerical audit 083 (theory audit 090),
    numerical audit 085 and numerical audit 089 (theory audit 100), numerical audit 086 (theory audit 101), numerical audit 087 (theory audit 102), numerical audit 088 (theory audit 103), numerical audit 093 and numerical audit 094 (theory audit 105),
    numerical audit 095 (theory audit 106), numerical audit 091 (theory audit 108, theory audit 110), numerical audit 092 (theory audit 111), numerical audit 099 and numerical audit 100 numbers (theory audit 116), numerical audit 096 (theory audit 117),
    numerical audit 097 (theory audit 118), numerical audit 102 (theory audit 122), numerical audit 106 (theory audit 125), numerical audit 107 (theory audit 126), numerical audit 109 (theory audit 134), numerical audit 113 (theory audit 136), numerical audit 116 (theory audit 137), numerical audit 119 and numerical audit 120 (theory audit 142), numerical audit 115 (theory audit 144), numerical audit 111 (theory audit 162), numerical audit 123 (theory audit 155), numerical audit 131 (theory audit 156, accepted in numerical audit 138), numerical audit 133 to numerical audit 135 (theory audit 161), numerical audit 121 (theory audit 166), numerical audit 137 (theory audit 167), numerical audit 128 (agrees with the
    independent theory audit 147 computation, compared in numerical audit 129).
  - Confirmed by the norm-certification team: numerical audit 020 (d2 ||F||_H, independent Galerkin enclosure, 23:55Z); numerical audit 139 agrees with the norm-certification team's
    independent Beta-integral G0 of candidate 007; numerical audit 153 agrees with the norm-certification team's rF, G1 and P2; numerical audit 161 agrees with the norm-certification team's eleven
    weighted Laplacian norms and numerical audit 166 with the norm-certification team's Q3 of candidate 007; numerical audit 180 with the norm-certification team's complete-component
    comparisons for candidate 007.
  - Still originating with the numerical auditor: numerical audit 037, numerical audit 066 at its other radii, numerical audit 068 (Mpen2 ||F||_H), numerical audit 072, the endpoint value
    J(1 + 1/c_l) of numerical audit 099, numerical audit 104, numerical audit 112, numerical audit 117.

## 8. Resumable checkpoints and verification scripts

The accompanying artifacts contain the following reproducibility material.

- Reference candidate: candidate 007, exact rational coefficients in
  the accompanying artifacts (sha256
  ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21), with its manifest, checksum manifest, diagnostic record and
  sector table in the accompanying artifacts. Its registered norms are all CONFIRMED (answer 3); the registered scalar and
  graded correction balls about it contain no exact solution (closure matrix rows 56 and 57), and its dyadic scheme is
  also excluded under that scheme's stated premises (row 64; theory audit 512 C2).
- All snapshots candidate 001 to candidate 028 (157 files) were frozen at hour 22 by a manifest with sha256
  a08248330fb4f61b0dece8c40987440a9824d68f3e98ff0a1c742b7606fe6c4d (all 157 files verified at 18:39Z; no snapshot file
  is newer than 15:24:01Z). The snapshot guide in the accompanying artifacts states which snapshots are included in full and lists the sha256 of
  every data file of the others.
- Restarting an optimization: the final numerics report in the accompanying artifacts section 8. The optimizer state of a snapshot is its exact
  coefficient file plus the binary64 warm start, run with the matching ordered basis (the accompanying artifacts).
- Independent verification scripts: the reproduction guide in the accompanying artifacts section 2 (one numerical-audit script per certified number,
  with inputs, precision, running time and expected result) and section 3 (exact arithmetic of the theory workers and
  of the theory auditor). The theory auditor's static validators (the evidence validator in the accompanying artifacts with validation receipt 09, 5551 checks, addenda through theory audit 514) and the numerical auditor's evidence indexes check hashes
  and links only; the mathematics is checked by the per-result scripts. The theory team's check-suite script in the accompanying artifacts reruns all 69 of its jobs; a rerun on a copy at 18:31Z to 18:53Z agreed with every stored output
  up to run times, clock stamps and, in three outputs, the stored final rc=0 line (confirmed in theory audit 511 and numerical audit 442).
- The record of every verdict: the closure matrix in the accompanying artifacts (final version v185; earlier versions were never edited),
  the two verdict ledgers in the accompanying artifacts, and the theory workers' review sets cited by number in section 7.
- What remains to prove: section 6, the exact list of unresolved inequalities; the proposed continuation in the accompanying artifacts orders the work.
