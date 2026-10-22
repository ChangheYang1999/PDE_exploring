# NUM_REPORT (ipmA-num): validated numerics for the a posteriori analysis of the IPM profile X3

Version 4.1 (final), 2026-10-22T12:38:19Z (shift 10; T0 = 2026-10-20T12:44:25Z, T_end = 2026-10-22T12:38:19Z, elapsed 47.90 h (47 h 53 min, floor of the difference of the two timestamps taken with seconds); 10 shifts of up to 6 h (shifts/shifts.log) with 9 restart gaps between them totalling 270 s; the last shift's end line is written by the loop after this entry; shifts/shifts.log). Sections 2 to 6 are floating point (estimates,
labelled as such). Section 7 states what is enclosed rigorously and by which method; 7.0 collects the notation and definitions. Paths are relative
to the lane numerics. Version 4.0 (2026-10-22, shift 7) applied two internal-consistency referee passes
(astra/numrep1 on sections 1 to 7.3c, astra/numrep2 on 7.4 to 9; notes/astra_numrep{1,2}_answer.md): every rigorous ceiling of 7.2, 7.3, 7.3b, 7.3c
and 7.11 is now a directed (outward) rounding regenerated from the saved per-cell data by src/report_tables.py and src/xnorm_cert.py (Arb), the R2
tail argument was replaced by an explicit integral bound (src/r2_tails.py), stale status lines were replaced by the final dispositions, and the
reproducibility section lists the current source hashes next to the producing ones. Section 1 is a chronological record (one bullet group per shift);
later bullets supersede earlier status statements, and the numbers in it were re-checked against the sections in this version.

## 1. Summary
- The published candidate X3 (c6g_shape.npz, md5 15f8095f7e79dbfa0c50d75e5fe8997a, verified) is reconstructed exactly
  from its coefficients and generator formula (src/x3.py; agreement 1.3e-13 with the published independent generator).
- The published residual tables are reproduced (i) by rerunning the published evaluator (all 1591 non-timing numeric leaves of the reference
  JSON reproduced identically at 11250 x 384) and (ii) by an evaluator written here from scratch (own generator, own modal Green inverse): at
  16875 x 512 and 22500 x 768 the normalized maxima (max |eps|/N_f, max |eps|/N_v) agree with the published values to within 1 percent and the
  absolute maxima of the bands r >= 10 to within 4.2 percent; the absolute maxima in 0.1 <= r <= 2 differ by +18 / +20 percent and in 2 <= r <= 10
  by +15 / -3.6 percent (the lobe maximum is not resolved by either grid, section 3b), and the r <= 0.1 band is at the evaluator's cancellation
  floor (section 3 has the band-by-band table).
- An explicit modal re-representation of X3 was built (section 4): rho~ = x^2 y sum_{m<260} a_m(r) cos(2m theta) with
  a_m exponential-polynomial splines in t = log r. Its canonical velocity and psi_xy(0) are closed-form (section 5),
  the identity c_l = (1 + psi_xy(0))/3 holds exactly by construction (c_l = 1/k, k the stored exponent), the density agrees
  with X3 to 1e-9 in the sampled relative sense of section 4, and its sampled residual agrees with X3's published values region by region up to the
  sampling differences of section 6 (e.g. 5.39e-5 against 6.03e-5 in 2 <= r <= 10, where the lobe maximum is unresolved by the grids, 3b). This is
  the object of the rigorous statements.
- RIGOROUS (section 7): the scalars S1 (c~, c_l, A, x_*, mu~ - 1, g, g', A~, and w'(P) with the divergence identity to 4.6e-12),
  independently confirmed by the verifier; the residual bound R0 on the whole plane in three weighted forms (section 7.3, post-fix code and
  data; ceilings: middle region sup W/m <= 2.5965e-4 at the lobe next to P, (1+u)^{1/2} multiplier form 3.8071e-4; outer region 9.3189e-5
  ((1+u)^{1/2} multiplier 7.3681e-3 at r = 7.7e4, the far-field Theta_1 mismatch band of X3, which is the global value of that form); inner region
  9.1893e-6; tails 1.07e-9 and 2.14e-6; R2 total 6.29e-4 with the tails integrated explicitly), corroborated by the verifier's independent, looser
  certificates (middle W/m < 2.91625e-4; exterior and inner regions) and by their exact re-summations of this lane's saved cells (FINAL_REPORT
  section 8); the derivative norms R1/R3/R5 on the middle region (section 7.3b: r|grad eps~|/m <= 0.4195, r^2|D^2 eps~|/m <= 713.2 at the lobe;
  order-5 Wiener sums on the P-disc up to 1.5e12); the outer and inner derivative norms (shift 4, section 7.3b: on 3413 <= r <= 8.2e10, r|grad eps~|/m <= 4.169e-3 and r^2|D^2 eps~|/m <= 1.122; on
  5.2e-5 <= r <= 0.00765, 2.762e-4 and 1.396e-2; so R1 is bounded on the whole plane except the two tails, with the global suprema 0.4195 and 713.2 at
  the lobe next to P; this lane's rigorous bounds, not independently verified);
  N1' flow certificate for the lead's transport argument over the WHOLE quadrant (section 7.6: V_2/y >= 0.98845, the axis signs of V_1 with
  the single zero x_*, X.V/r^2 >= 3.4957 for r >= 20, T_0 <= 1.2780 and V_1 <= -12.834 on the box B_1, T_0 <= -0.2399 off it; the lead's
  transport-inverse formula evaluated with these ranges gives ||R_-|| <= 6.31 at kappa = 0.2; the verifier confirmed the finite scalar instances,
  conditional on their acceptance of the whole certificate, and later produced their own independent radial and flow certificates, FINAL_REPORT
  section 8). Three resolutions (section 7.3c): v3 and v4 complete, v5 collected in shift 7 (see the shift 6/7 bullets); the outer/inner derivative
  norms are complete (7.3b); the centre-regular trial N7 (section 7.5, data/trial_n7.npz) has its S1 and middle certificate (equal to the trial's
  to the printed digits; the multiplier-form evaluations are discussed in 7.5).
- FLOATING (evidence only; sections 7.4, 7.5): near P the residual is small in value (1.1e-5 on the 0.5-disc) but of order 1 in H^3
  (H^3.06 = 1.21), because of knot-scale radial structure inherited from X3 (direction D^(4,0)); every mode carries knot-scale content
  that the operator sees at the 1e-3 .. 1e-1 level when removed (projection to 2 x .. 10 x coarser knots), and coarse-space
  Gauss-Newton re-solves do not recover the residual. The two external referee reports (astra/jets1, astra/smooth1) confirmed the
  derivative-jet formulas, the norm normalizations and the operator identity, and rejected the inference that this excludes a smooth
  exact solution (only restricted spaces were tested); the fine-knot refits (runs/pdisc/chainR.sh, chainQ) lowered the sup residual near P by
  13 percent and raised the H^3 content (7.5b), and the lead closed the band-restricted branch. Finite sections of L (C2, 7.4) with the
  sup-weighted raw basis are dominated by basis conditioning and the J near-kernel; sections with an X-Gram-orthonormalized basis (7.4b) replace
  that reading (row-density and size refinement in chain8d).
- RIGOROUS (shift 3, section 7.7, lead's N8 for the local source estimate SPEC 3.15): on B_{3 delta}(P) the Frobenius suprema of D^j V
  (j <= 4) and D^j rho~ (j <= 5) are enclosed by Taylor models + Arb angular enclosures + interval polar-to-Cartesian recursion: at
  delta = 0.0165, M_V = sup|D^2 V| <= 0.28728, M_rho = sup|D^2 rho~| <= 0.45337, C_V = 41.7 M_V + 3 M_rho <= 13.34 against the threshold 102.24
  (the threshold is kappa_loc/(2 delta) with the lead's local constant kappa_loc = 3.374; so K_1 = 1/(kappa_loc - E) <= 0.3171 if E <= C_V delta);
  at delta = 0.05, C_V <= 18.16 against 33.74, and the condition is certified up to
  delta = 0.07 (21.24 against 24.1), the largest certified admissible value; the sufficient test fails in floating point from 0.08 on (an
  estimate, not a certified counterexample). The sampled values are within 3 percent of the second-order bounds. FLOATING (7.7c): the cut-off
  residual norm ||tau eps~||_{H^{3.1}} at delta = 0.0165, 0.05, 0.1, 0.2 is 1.56, 1.07, 0.81, 1.37 (grid convergence checked at delta = 0.0165),
  with delta x H^4/H^3 between 26.3 and 36.2 (consistent with a substantial cutoff contribution; the split between cutoff derivatives and residual
  variation is not identified by these norms): a smaller ball does not give a small local forcing norm.
- RIGOROUS (shift 3, section 7.3c): the half-knot-spacing variant v3 reproduces the X3 trial's certified scalars to the printed digits and
  its middle sup bounds to 7 significant digits (2.5965e-4 / 3.8071e-4 as ceilings) and its outer sup bounds to 5 (9.3188e-5 against 9.3189e-5,
  7.3682e-3 against 7.3681e-3), while the integral bounds change by 0.18 percent (middle) and 0.007 percent (outer), so the certified residual level is that of the re-represented X3 at this fit quality (floating evidence of fit stability; the
  certificates remain statements about each specified trial); v4 and v5 followed (shifts 6 and 7). FLOATING (section 7.4b, shifts 3-5): in a column basis orthonormalized
  in the broken-gradient background-relative H^1 Gram (the encoded columns are not exactly conforming, ver 130-132; 7.4b), the M16/s16 finite
  sections of L have smallest singular value 0.1208 / 0.1698 / 0.2067 at 10760 / 18680 / 26600 rows (divided by the square root of the row count:
  1.165e-3 / 1.242e-3 / 1.268e-3, within 9 percent of each other across the three row densities) and NO near-null direction along J, J_inner, the tails
  or KP/TAU (cos^2 below 3e-6; the earlier J near-kernel of 7.4 was an artefact of the sup-weighted raw basis). Under SECTION refinement at the
  same collocation density (M24/s8/Mout32, 5126 retained, 27360 rows) the smallest value falls to 0.1492 (9.018e-4 per square root of the row count, minus 27 percent) while
  the bulk of the spectrum is stable per row; a decrease is expected for this functional, which pairs an H1-type column norm with an L2-type image
  norm and so measures a derivative-gaining inverse that a transport operator cannot have (external referee astra/gram3). The version-3
  diagnostics (H1-type image rows with C^1 joins, continuous reference functions, saved singular vectors and their radial localization; chains
  8e/8f) are complete (7.4b (vi), (vii)); no conclusion about L is drawn from any of these floating sections (lead 12:34Z). FLOATING (7.8, 7.9): X3
  lies within about 1.6e-8 of the trial in the four source jets at P (for h = X3 - trial and delta V = U[h] + c[h] X: delta V_1(P), d_y delta V_2(P),
  h_y(P), h_xy(P); 7.8); the constants R (a
  Wiener-type bound of the cutoff perturbation w of the source linearization) and E = 0.0705 (its energy perturbation) of the lead's auxiliary
  source inverse (SPEC 3.15; formulas in 7.9), its dilated version R~(ell) and the localized forcing N_{1/ell}(tau eps~) (norm defined in 7.10)
  reproduce the lead's values, with the product (inverse bound) x (forcing) at best 11.4 (ell = 0.0035).
- RIGOROUS (shift 4, section 7.10): the localized forcing norm of the lead's local source estimate is certified: ||tau eps~||_{H^{3.1}} <= 1.5700
  and N_500(tau eps~) <= 3.5769 at delta = 33/2000 for the C^4 degree-9 radial cutoff (floating 1.3296 and 3.1128, so the certified bound is within
  18.1 percent), by Hoelder interpolation between certified order-3 and order-4 bounds built from bivariate Taylor models of the residual AND of the
  cutoff near P (two external referee rounds, eight items repaired; this lane's certificate: verifier topic 122 confirmed the finite components
  of the final version v2.2, the physical forcing norm remains OPEN); with the verifier's K_1 < 0.3181 the first term of the local estimate at the
  trial is < 0.4995 (certified). Certified C^4 bounds of eps~ on B_{3 delta}(P): |eps~| <= 9.425e-7, |grad eps~| <= 9.889e-5 (components 7.624e-5,
  6.299e-5), |d_x^4 eps~| <= 311.7 (every quoted certified decimal is an outward ceiling of the stored value).
- Shift 3 corrections: three more inward roundings in the N1' statement fixed (inner V_2/y >= 21.30140, outer tail V_2/y >= 5.575361, x_* radius
  3.0e-13); every other quoted flow decimal re-checked outward against the raw aggregates (WORKLOG 00:45Z).
- Shift 5 (section 3b, 7.4b (vi)-(vii), 7.11): FLOATING locations of all sampled residual maxima of X3 at both resolutions and a far-field closure
  test (outer extent irrelevant on aligned grids; the far continuation matters at the 1 to 14 percent level in the mid and far bands; the lobe's
  absolute maximum at r = 8.8 is not resolved by the grids, 5.6e-5 to 7.2e-5); version-3 finite sections of the full linearization: the
  derivative-balanced quotient (H1-type rows and columns, quadrature-weighted) is unchanged by the radial stride and the image cutoff and decreases
  by 8.6 percent from 16 to 24 angular modes (0.4131 -> 0.3777), with weakest directions at r = 1 to 22 and no content along the named reference
  directions; two referee rounds (astra/gram3, gram4) and verifier topics 127 to 149 shaped the wording; nothing about L follows. RIGOROUS (this
  lane, audit pending; Arb arithmetic since version 4.0): ||eps~||_X <= 0.385655 and ||eps~ - X.grad eps~||_X <= 585.873 in the diagnostic weighted
  H^1 norm (the X norm, weight m^-2 (1+u^2)^-3/2 on f^2 + r^2 |grad f|^2, 7.11) over the three finite certificate regions r_T,in <= r <= r_T,out
  (the two tails are bounded by the verifier's topic 178; whole plane 585.874000000002, conditional on this lane's majorants; the verifier's own
  unconditional whole-plane ceilings are the coarse 245653983.313885103 / 30665526224.248429025 of topic 179 v2, FINAL 08:42Z, refined to
  8.38010956871949018314234 / 2467.95347982509225629694 by topics 180 v2 and 183 exterior, FINAL 10:22Z, and to the final 1.49546805188731021373656 /
  2464.68293019825564964515 by topics 181 v2 and 183 both, FINAL 11:31Z; 7.11). For one operator and
  an admissible K = rho~ - X.grad rho~ any inverse estimate ||h||_X <= C ||L h||_X implies C >= ||K||_X / ||L K||_X; the numerical quotient 7659.08 /
  585.88 = 13.07 is a MIXED-TRIAL DIAGNOSTIC (floating numerator for the STORED trial over a conditional ceiling for the exactly normalized trial, whose
  coefficients differ by 1e-13 relative, no transfer bound stated) and is not asserted as a lower bound of C. FLOATING (shift 6): with analytic t-derivatives of the residual modes (src/xnorm_jets.py) ||eps~||_X = 3.245e-2 and
  ||eps~ - X.grad eps~||_X = 44.91 (98.8 percent of its norm^2 is the second t-derivative of the residual at the knot scale), so the floating
  quotient ||K||_X / ||L K||_X is 170.5; the certified ceilings exceed the floating values by the factors 11.9 and 13.0.
- Shift 6 (7.11 analytic values, B(K, K), 7.4c, 7.3c v4): FLOATING (all K quantities for the STORED trial), refereed (astra/xnorm1, bkk1, kproj1,
  kproj2); the verifier's topics 159, 165, 170 audited the algebra and the saved finite data (identities, literal scalars, exact re-summations), not
  the physical X norms:
  the analytic-derivative X norms above; ||B(K, K)||_X = 2.062e5 = 3.52e-3 ||K||_X^2 (U[K].grad K via the closed-form inverse of K, scaling identity
  psi[K] = 2 psi~ - X.grad psi~ to 1e-13); and the K-projection test of the finite sections (7.4c): the M16/s16 and M24/s16 sections contain
  approximants of the scaling tangent K within 1.8 and 1.2 percent in X norm whose remainder images are amplified 3400 to 4700 times the section
  minimum per unit X norm (||L(PK) - LK||_H1q / ||K - PK||_X against the minima 0.4131 / 0.3777), the representatives' own quotients
  ||L(PK)||/||PK|| being 25.6 / 20.5 (62 / 54 times the minima), while K itself has quotients 3e3 to 5e4 times below the section minima in the same
  row functionals (reproduced by the section's own
  assembler from all 260 modes of K to 5e-5): the section minima are restriction-dependent and carry no lower-bound information outside the span;
  K is in neither the F- class (tail outside it, J(K) = -2) nor the normalized tangent space. RIGOROUS (this lane, audit pending): the third
  resolution v4 (230 angular modes) reproduces the certified residual of the X3 trial to +0.02 percent (middle) and +0.4 percent (outer), the
  x_* and w'(P) to 13 digits (7.3c; the midpoints of mu~ - 1 and g move by 5.7e-13 and 7.0e-12); v5 followed in shift 7.
- Shift 7 (2026-10-22, 00:17Z onward; version 4.0): four referee rounds on this report (astra/numrep1 and numrep2 on the whole report, 59 + 67 items;
  numrep3 and numrep4 on the repaired text, 45 + 38 items; numrep5 and numrep6 targeted at the newest text, 11 + 5 items; notes/astra_numrep*_answer.md;
  applied by notes/repairs/batch1.py .. batch10.py with every old string asserted unique) were applied: all
  certified ceilings of 7.2, 7.3, 7.3b, 7.3c, 7.11 are now directed roundings regenerated from the saved per-cell data (src/report_tables.py,
  src/xnorm_cert.py in Arb); the changes are in the last printed digit (e.g. middle sup W/m 2.5964e-4 -> 2.5965e-4, (1+u)^{1/2} form 3.8070e-4 ->
  3.8071e-4, outer (1+u)^{1/2} form 7.3680e-3 -> 7.3681e-3, inner tail 2.138e-6 -> 2.139e-6) except two corrections of substance: the whole-plane
  (1+u)^{1/2} multiplier value is the outer region's 7.3681e-3 (not the middle region's 3.8071e-4), and the R2 tails are now bounded by explicit
  integrals (src/r2_tails.py; at most 6.51e-16 and 3.82e-20 in norm^2) instead of a 'sup times measure' remark that was invalid for the outer tail. The
  notation block 7.0, the stored-trial scope of every floating K quantity, the finite-region domain of the X-norm ceilings (tails: verifier topic
  178), stale status lines, the N7 and v3/v4 comparison wording, and the section-8 commands and current hashes were added or corrected. RIGOROUS
  (this lane, audit pending): v5 (knot scheme 2, R0 = 1468) reproduces the base trial's middle sup bounds to 5 digits (2.5965e-4 / 3.8071e-4 /
  1.2015e-4; middle L2 +4.7 percent on the shorter middle region); its outer/inner regions and tails are in the 7.3c table (collected 2026-10-22T02:24Z).
- FINAL STATUS (run end). T0 = 2026-10-20T12:44:25Z (first shift start, shifts/shifts.log); T_end = 2026-10-22T12:38:19Z, defined as the time of the last update of this report, at which the reported work of this lane ends (the 48 h limit T0 + 48 h = 2026-10-22T12:44:25Z was not reached at T_end; no cause of the end is asserted; the loop's own end line in shifts/shifts.log is appended after the fact); elapsed 47.90 h (47 h 53 min, floor of the difference of the two timestamps taken with seconds); 10 shifts of up to 6 h (shifts/shifts.log) with 9 restart gaps between them totalling 270 s; the last shift's end line is written by the loop after this entry. After T_end only closing records outside this report were written (RUN_STATUS.md, WORKLOG.md and the refreshed artifacts copy). The status below was written 2026-10-22T02:28Z at the end of shift 7 and re-checked at the run end (shift 8 (06:17:33Z to 12:15:36Z) changed no certified or floating number: it checked the 57 current hashes of section 8 against the lane and the artifacts (runs/hash_check.py), regenerated the four trial files and two test fixtures byte-identically from the published coefficients with the recorded commands (runs/variant_regen.sh, src/truncate_trial.py), reran the summary scripts from a fresh copy of the artifacts (identical outputs), and repaired the 20 defects of a fresh-reader referee round on the reproducibility appendix (notes/astra_repro1_answer.md, notes/repairs/batch13.py: two I/O bugs in flow_summary.py and cert_summary.py when run from the artifacts copy, README commands aligned with section 8, fixtures, external inputs, shipping gaps; section 8 and the README record the details; shift 9 (12:16:06Z to 12:35:05Z) changed no number either: it applied only the verifier's report precisions of 12:17Z to 7.11 and section 1 (notes/repairs/batch22.py: the historical 'Reading' paragraph of 7.11 no longer says that a rigorous lower bound of ||K||_X is not done, the verifier's three-annulus bound being cited above it; 'approximately' on two squared display values; whole-plane against finite-region wording) and the stamp; shift 10 (12:35:35Z to the run end) changed nothing in this report except this stamp, whose session count and restart gaps are rebuilt from shifts/shifts.log; the verifier's FINAL whole-plane X-norm ceilings, topic 179 v2, are cited in 7.11).) RIGOROUS (this
  lane's certificate, Arb + mid-rad arithmetic, directed decimal displays; verifier status as stated in each subsection): the point scalars S1 (7.2);
  the residual bound R0 on the whole plane in three weighted forms with the tails by termwise majorants (7.3: divisor form <= 2.5965e-4, (1+u)^{1/2}
  form <= 7.3681e-3, (1+u)^{1/2-k} form <= 1.4636e-3); the weighted L2 norm R2 <= 6.2899e-4 with explicit tail integrals; the first and second
  derivative norms R1/R5 on the three finite regions r_T,in <= r <= r_T,out and R3 (orders up to five) on the 377 cells meeting the disc |X - P| < x_*/4 (7.3b: r|grad eps~|/m <= 0.4195, r^2|D^2 eps~|/m <= 713.2, sup W_F/m <=
  0.4275); the X-norm ceilings on the same three finite regions, end tails excluded (7.11: 0.385655 / 585.873; the verifier's whole-plane ceilings are also cited there); the flow certificate N1' on the whole quadrant (7.6); the N8 derivative
  bounds on the balls about P up to delta = 0.07 (7.7a); the localized forcing bound (7.10: 1.5700 / 3.5769); and four resolutions of the trial (base,
  v3, v4, v5): the middle sup bounds of the base, v3 and v5 trials agree to 5 digits and v4's differ by +0.02 percent, the outer sup bounds differ by at
  most 0.4 percent, while the inner-region bounds (v3: -41 percent) and the integral upper bounds (up to 5 percent) do change (7.3c; changes of bounds,
  not demonstrated changes of the integrals). FLOATING (evidence only, STORED trial): the finite sections of L and the
  K-projection test (7.4 to 7.4c), the Sobolev norms near P (7.5, 7.7c), the jets and auxiliary constants (7.8, 7.9), the analytic X norms and B(K, K)
  (7.11). NOT ESTABLISHED by this lane: any inverse or operator bound for L, any closing inequality, any statement about the existence or
  nonexistence of an exact profile near X3; the lane's role was the validated numerics (SPEC items S1, R0 to R5, N1', N8 to N10, RES) for the lead's
  analysis, whose verdict is in FINAL_REPORT.md.
- Nothing in this lane bears on the existence of an exact profile beyond the certified residual, derivative, flow and coefficient data of rho~.

## 2. Provenance and formula of X3
File: PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz,
md5 15f8095f7e79dbfa0c50d75e5fe8997a (control F3: c6gF_shape.npz, 0398af3f08a2a4f75e42c846edbaa375); both equal the
values in PROMPT.md section 2. Generator: a_generator/stationary.py with b_fit/solver.py; independent generator
d_evaluator/code/gen_shape.py. Stored scalars: k = 0.17936053129375418, c_l = 1/k = 5.575362610641546,
L = 7.651424601381517, c = 15.726087831924637, origin_radius 0.02 (in units of L), 201 x 375 spline coefficients,
6 Chebyshev coefficients, degree-7 clamped B-splines on 384 stored knots (the stored knots differ from the formula
linspace^1.3 by up to 0.25; 368 interior knots at radii 0.3895 to 3413 = 446.1 L).
Formula (u = r/L): q = 1 - (1+u^2)^(-(1-k)/2), chi = u^2/(u^2 + 0.02^2), s = u^2/(1+u^2), p3 = 6 + 2k/(2-k) = 6.19703,
  H = (k-3)/2 log(1+u^2) + sum_{m<=200} chi^{max(m-1,0)} b_m(q) cos(2m theta) + s^{p3/2} T(2q-1) |cos theta|^{p3-2} sin^2 theta,
  rho_bar = x^2 y e^H;  velocity by the canonical modal Green inverse; c_l fixed at the stored value.
Checked facts: p3 = 6.197030257 (prompt 6.19703); a(0) = e^{H(0)} = 1 to 1e-14 (b_m(0) = 0 because the first B-spline is
omitted); the canonical inverse of rho_bar gives c = 15.72608777 to 15.72608782 (own evaluator / published evaluator),
so (1 + c)/3 = 5.5753625910 to 5.5753626074 against the stored 5.5753626106 (defect 3.2e-9 to 2.0e-8 depending on the
inverse's radial resolution; the published value is 3.2e-9).

## 3. Reproduction of the published residual tables (floating point, sampled maxima)
Published evaluator rerun (runs/pubeval, 11250 x 384, 97 s): all 1591 numeric leaves of the reference JSON reproduced
(only timings differ). Own evaluator (src/x3.py + src/inverse.py + src/x3_resid.py; log-radial grid 1e-4 L to 1e6 L,
6-point Lagrange radial quadrature with exact exponential moments, power-law tail fit; c_l stored; both axis columns
set to their exact zero residual):
| region (X3 fields; entries are maxima of the sampled quotients) | max \|eps\|/N_f 16875x512 | max \|eps\|/N_f 22500x768 | max \|eps\|/N_v 16875 / 22500 | abs max 16875 / 22500 | published |
|---|---|---|---|---|---|
| r <= 0.1 | 2.6e-10 | 2.6e-10 | 5.6e-10 / 5.7e-10 | 3.8e-12 / 3.8e-12 | abs 1.7e-13 (axis-floor excluded there) |
| 0.1 <= r <= 2 | 2.3e-8 | 2.6e-8 | 4.5e-8 / 5.1e-8 | 1.05e-7 / 1.07e-7 | abs 8.9e-8 |
| 2 <= r <= 10 | 6.80e-7 | 7.16e-7 | 1.90e-7 / 2.01e-7 | 6.96e-5 / 5.61e-5 | N_f 6.84e-7 / 7.16e-7, abs 6.03e-5 / 5.82e-5 |
| X-P < 0.5 | 6.80e-7 | 7.16e-7 | 1.90e-7 / 2.01e-7 | 1.045e-5 / 1.12e-5 | N_f 6.84e-7, abs 1.05e-5 |
| 10 <= r <= 100 | 8.9e-8 (cut 8.2e-8) | 8.9e-8 | 7.1e-8 / 6.8e-8 | 1.98e-5 / 2.02e-5 | abs 1.99e-5 |
| 100 <= r <= 1000 | 1.59e-8 | 1.59e-8 | 6.5e-8 / 6.5e-8 | 6.26e-6 / 6.28e-6 | abs 6.03e-6 |
| 1000 <= r <= 1000 L | 1.36e-8 | 1.37e-8 | 2.21e-7 / 2.19e-7 | 3.09e-5 / 3.15e-5 | N_v 2.15e-7 / 2.18e-7 |
| r > 1000 L | 1.31e-7 | 1.32e-7 | 1.091e-6 / 1.095e-6 | 1.881e-4 / 1.893e-4 | N_v 1.09e-6 to 1.11e-6, abs 1.897e-4 |
Scalars: x_* = 8.600063801 (published 8.600063804), h(P) - 1 = 3.4e-8 / -1.6e-8 (published 3.1e-8 / -1.8e-8),
d_x V_1(P) - (2c_l - 1) = 3e-8 / -4e-9. Own inverse tests: psi = xy e^{-r^2} (max velocity error 4e-14, c error 5e-9 at
4000 radii), psi = xy (1+r^2)^{(k-1)/2} (relative velocity error 1e-11 at r = 0.1 to 1.6e-7 at r = 1e5, c error 2e-9).
These are sampled maxima on between-node grids, not bounds.

### 3b. Locations of the sampled residual maxima and far-field closure test (lead 13:17Z, format requirement of FINAL_REPORT section 6; FLOATING; shift 5, 16:45Z)
(a) Locations. The saved outputs of the independent evaluator (src/x3_resid.py; runs/resid_N16875_q512.json, runs/resid_N22500_q768.json) store every
sampled maximum as [value, r, theta]; src/x3_maxloc_table.py prints them (runs/x3_maxloc.md). theta is the polar angle in radians (theta = 0 the
x axis, pi/2 the y axis); 'cut' excludes the near-y-axis columns (pi/2 - theta < 0.006), as in the published tables. The normalized maxima near P
sit at (8.527, 0.0092), near the x axis in the lobe next to P; the absolute maximum of the fitted band at (8.811, 0.288) (the lobe, off-axis); the far
N_v maximum at (36561, 1.5677) (uncut columns) and (37012, 1.5647) (cut), both at 16875 x 512 (the 22500 x 768 locations are in the table) next to the y axis (X3's Theta_1 mismatch band, as the prompt describes); the absolute far maximum at
(40115, 0.6596).
### runs/resid_N16875_q512.json: Nr = 16875, Nt = 512, r in [0.0007651, 7.651e+06], c_l stored 5.575362610642 (x_* = 8.600063801); each cell: value @ (r, theta in rad; theta = pi/2 is the y axis)
| region | max |eps|/N_f | same, axis columns cut | max |eps|/N_v | same, cut | max |eps| |
|---|---|---|---|---|---|
| r<=0.1 | 2.591e-10 @ (0.099867, 0.0031) | 2.591e-10 @ (0.099867, 0.0031) | 5.594e-10 @ (0.099867, 0.0031) | 5.594e-10 @ (0.099867, 0.0031) | 3.776e-12 @ (0.099867, 0.6228) |
| 0.1<=r<=2 | 2.299e-08 @ (1.9991, 0.0031) | 2.299e-08 @ (1.9991, 0.0031) | 4.487e-08 @ (1.9991, 0.0031) | 4.487e-08 @ (1.9991, 0.0031) | 1.049e-07 @ (1.9991, 0.2700) |
| 2<=r<=10 | 6.795e-07 @ (8.527, 0.0092) | 6.795e-07 @ (8.527, 0.0092) | 1.904e-07 @ (8.527, 0.0092) | 1.904e-07 @ (8.527, 0.0092) | 6.959e-05 @ (8.8109, 0.2884) |
| |X-P|<0.5 | 6.795e-07 @ (8.527, 0.0092) | 6.795e-07 @ (8.527, 0.0092) | 1.904e-07 @ (8.527, 0.0092) | 1.904e-07 @ (8.527, 0.0092) | 1.045e-05 @ (8.5387, 0.0491) |
| 10<=r<=100 | 8.874e-08 @ (10.003, 1.5677) | 8.179e-08 @ (10.003, 1.5647) | 7.120e-08 @ (73.145, 1.5616) | 7.120e-08 @ (73.145, 1.5616) | 1.976e-05 @ (13.936, 0.9235) |
| 100<=r<=1000 | 1.589e-08 @ (100.11, 1.5524) | 1.589e-08 @ (100.11, 1.5524) | 6.527e-08 @ (100.11, 1.5524) | 6.527e-08 @ (100.11, 1.5524) | 6.259e-06 @ (646.56, 1.3683) |
| 1000<=r<=1000L | 1.362e-08 @ (7643.1, 1.5094) | 1.362e-08 @ (7643.1, 1.5094) | 2.205e-07 @ (7643.1, 1.5555) | 2.205e-07 @ (7643.1, 1.5555) | 3.088e-05 @ (7643.1, 1.4634) |
| r>1000L | 1.312e-07 @ (32735, 0.8468) | 1.312e-07 @ (32735, 0.8468) | 1.091e-06 @ (36561, 1.5677) | 1.078e-06 @ (37012, 1.5647) | 1.881e-04 @ (40115, 0.6596) |
| r<=1000 | 6.795e-07 @ (8.527, 0.0092) | 6.795e-07 @ (8.527, 0.0092) | 1.904e-07 @ (8.527, 0.0092) | 1.904e-07 @ (8.527, 0.0092) | 6.959e-05 @ (8.8109, 0.2884) |
| all | 6.795e-07 @ (8.527, 0.0092) | 6.795e-07 @ (8.527, 0.0092) | 1.091e-06 @ (36561, 1.5677) | 1.078e-06 @ (37012, 1.5647) | 1.881e-04 @ (40115, 0.6596) |

### runs/resid_N22500_q768.json: Nr = 22500, Nt = 768, r in [0.0007651, 7.651e+06], c_l stored 5.575362610642 (x_* = 8.600063801); each cell: value @ (r, theta in rad; theta = pi/2 is the y axis)
| region | max |eps|/N_f | same, axis columns cut | max |eps|/N_v | same, cut | max |eps| |
|---|---|---|---|---|---|
| r<=0.1 | 2.618e-10 @ (0.099962, 0.0020) | 2.618e-10 @ (0.099962, 0.0020) | 5.652e-10 @ (0.099962, 0.0020) | 5.652e-10 @ (0.099962, 0.0020) | 3.831e-12 @ (0.099962, 0.6218) |
| 0.1<=r<=2 | 2.616e-08 @ (1.9989, 0.0020) | 2.616e-08 @ (1.9989, 0.0020) | 5.106e-08 @ (1.9989, 0.0020) | 5.106e-08 @ (1.9989, 0.0020) | 1.067e-07 @ (1.9989, 0.2536) |
| 2<=r<=10 | 7.157e-07 @ (8.5229, 0.0082) | 7.157e-07 @ (8.5229, 0.0082) | 2.005e-07 @ (8.5229, 0.0082) | 2.005e-07 @ (8.5229, 0.0082) | 5.611e-05 @ (8.8067, 0.2904) |
| |X-P|<0.5 | 7.157e-07 @ (8.5229, 0.0082) | 7.157e-07 @ (8.5229, 0.0082) | 2.005e-07 @ (8.5229, 0.0082) | 2.005e-07 @ (8.5229, 0.0082) | 1.119e-05 @ (8.5317, 0.0573) |
| 10<=r<=100 | 8.904e-08 @ (10.009, 1.5688) | 8.266e-08 @ (13.944, 0.9224) | 6.782e-08 @ (87.986, 1.5626) | 6.782e-08 @ (87.986, 1.5626) | 2.016e-05 @ (13.944, 0.9224) |
| 100<=r<=1000 | 1.590e-08 @ (100.1, 1.5524) | 1.590e-08 @ (100.1, 1.5524) | 6.534e-08 @ (100.1, 1.5524) | 6.534e-08 @ (100.1, 1.5524) | 6.277e-06 @ (646.65, 1.3683) |
| 1000<=r<=1000L | 1.366e-08 @ (7649.1, 1.5094) | 1.366e-08 @ (7649.1, 1.5094) | 2.194e-07 @ (7649.1, 1.5565) | 2.194e-07 @ (7649.1, 1.5565) | 3.145e-05 @ (7649.1, 1.4624) |
| r>1000L | 1.320e-07 @ (32715, 0.8447) | 1.320e-07 @ (32715, 0.8447) | 1.095e-06 @ (36389, 1.5688) | 1.078e-06 @ (37028, 1.5647) | 1.893e-04 @ (40064, 0.6422) |
| r<=1000 | 7.157e-07 @ (8.5229, 0.0082) | 7.157e-07 @ (8.5229, 0.0082) | 2.005e-07 @ (8.5229, 0.0082) | 2.005e-07 @ (8.5229, 0.0082) | 5.611e-05 @ (8.8067, 0.2904) |
| all | 7.157e-07 @ (8.5229, 0.0082) | 7.157e-07 @ (8.5229, 0.0082) | 1.095e-06 @ (36389, 1.5688) | 1.078e-06 @ (37028, 1.5647) | 1.893e-04 @ (40064, 0.6422) |

(b) Far-field closure test at 16875 x 512 (src/x3_closure_table.py; runs/closure/*.json; runs/closure/closure_table.md). Base: the saved
configuration (1e-4 L <= r <= 1e6 L, the Fourier modes of d_x rho continued beyond the grid by the four-power fit r^{k-1}, r^{2k-2}, r^{k-3}, r^{3k-3} on the last
decade). Variants: outer extent 1e5 L and 1e7 L on ALIGNED grids (same spacing and inner end, so the sample radii coincide: Nr 15188 and 18562) and
on SHIFTED grids (Nr 16875 over the new range, so the sample radii move); far continuation by the exact leading power r^{k-1} only; fit window of two
decades. Each cell is the relative change of the sampled maximum against the base (location noted when it moved).
Base: Nr 16875, Nt 512, r in [0.0007651, 7.651e+06], tail powers four on the last 1.0 decade(s); c = psi_xy(0) = 15.726087821661, x_* = 8.600063801.
outer extent 1e5 L (aligned grid, Nr 15188): Nr 15188, r in [0.0007651, 7.656e+05], tail four / 1.0 decades; c = 15.726087821536 (change -1.25e-10), x_* = 8.600063801 (change -5.20e-13)
outer extent 1e7 L (aligned grid, Nr 18562): Nr 18562, r in [0.0007651, 7.647e+07], tail four / 1.0 decades; c = 15.726087821663 (change 2.26e-12), x_* = 8.600063801 (change 3.55e-15)
far continuation r^{k-1} only: Nr 16875, r in [0.0007651, 7.651e+06], tail lead / 1.0 decades; c = 15.726087826177 (change 4.52e-09), x_* = 8.600063804 (change 3.83e-09)
fit window 2 decades: Nr 16875, r in [0.0007651, 7.651e+06], tail four / 2.0 decades; c = 15.726087821661 (change 0.00e+00), x_* = 8.600063801 (change 1.42e-14)
outer extent 1e5 L (shifted grid, Nr 16875): Nr 16875, r in [0.0007651, 7.651e+05], tail four / 1.0 decades; c = 15.726087821706 (change 4.54e-11), x_* = 8.600063801 (change 1.94e-11)
outer extent 1e7 L (shifted grid, Nr 16875): Nr 16875, r in [0.0007651, 7.651e+07], tail four / 1.0 decades; c = 15.726087821647 (change -1.42e-11), x_* = 8.600063801 (change 1.32e-11)

| region | column | base value @ (r, theta) | rel. change: outer extent 1e5 L (aligned grid, Nr 15188) | rel. change: outer extent 1e7 L (aligned grid, Nr 18562) | rel. change: far continuation r^{k-1} only | rel. change: fit window 2 decades | rel. change: outer extent 1e5 L (shifted grid, Nr 16875) | rel. change: outer extent 1e7 L (shifted grid, Nr 16875) |
|---|---|---|---|---|---|---|---|---|
| r<=0.1 | max |eps|/N_f (cut) | 2.642e-10 @ (0.099867, 0.0031) | +4.89e-03 | -9.44e-05 | -4.01e-01 | -1.58e-06 | -1.85e-03 | +1.24e-04 |
| r<=0.1 | max |eps|/N_v (cut) | 5.705e-10 @ (0.099867, 0.0031) | +4.89e-03 | -9.44e-05 | -4.01e-01 | -1.58e-06 | -1.85e-03 | +1.24e-04 |
| r<=0.1 | max |eps| | 3.861e-12 @ (0.099867, 0.6228) | +5.46e-03 | -1.05e-04 | -4.48e-01 | -2.47e-06 | -8.53e-04 | +2.58e-03 |
| 0.1<=r<=2 | max |eps|/N_f (cut) | 2.300e-08 @ (1.9991, 0.0031) | +1.37e-05 | -3.33e-07 | -4.78e-03 | -1.66e-08 | +3.03e-04 | +2.00e-04 |
| 0.1<=r<=2 | max |eps|/N_v (cut) | 4.488e-08 @ (1.9991, 0.0031) | +1.37e-05 | -3.33e-07 | -4.78e-03 | -1.66e-08 | +2.19e-04 | +1.44e-04 |
| 0.1<=r<=2 | max |eps| | 1.053e-07 @ (1.9991, 0.2700) | +2.18e-04 | -4.91e-06 | -7.48e-02 | -1.35e-07 | +2.91e-04 | +1.65e-04 |
| 2<=r<=10 | max |eps|/N_f (cut) | 6.794e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -5.04e-03 | -2.35e-03 |
| 2<=r<=10 | max |eps|/N_v (cut) | 1.904e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -4.87e-03 | -2.51e-03 |
| 2<=r<=10 | max |eps| | 6.960e-05 @ (8.8109, 0.2884) | +1.06e-06 | -1.45e-08 | -3.41e-03 | -1.20e-08 | -1.12e-01 | +3.60e-02 |
| |X-P|<0.5 | max |eps|/N_f (cut) | 6.794e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -5.04e-03 | -2.35e-03 |
| |X-P|<0.5 | max |eps|/N_v (cut) | 1.904e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -4.87e-03 | -2.51e-03 |
| |X-P|<0.5 | max |eps| | 1.045e-05 @ (8.5387, 0.0491) | +1.36e-06 | -1.36e-08 | -4.81e-03 | -1.78e-08 | +1.54e-04 | -9.29e-04 |
| 10<=r<=100 | max |eps|/N_f (cut) | 8.197e-08 @ (10.003, 1.5647) | +6.76e-05 | -1.26e-06 | -2.75e-02 (moved to r=13.94, th=0.923) | -1.79e-07 | -3.80e-03 | -8.84e-03 |
| 10<=r<=100 | max |eps|/N_v (cut) | 7.109e-08 @ (73.145, 1.5616) | -7.31e-06 | +1.23e-07 | +3.42e-02 | +9.69e-08 | +2.15e-06 | -1.84e-06 |
| 10<=r<=100 | max |eps| | 1.977e-05 @ (13.936, 0.9235) | +6.64e-06 | -1.61e-07 | -1.66e-02 | -5.97e-08 | -9.24e-03 | +1.33e-05 |
| 100<=r<=1000 | max |eps|/N_f (cut) | 1.592e-08 @ (100.11, 1.5524) | +6.90e-06 | -1.45e-07 | +2.84e-02 | -1.21e-07 | +3.22e-04 | +1.10e-04 |
| 100<=r<=1000 | max |eps|/N_v (cut) | 6.541e-08 @ (100.11, 1.5524) | +6.90e-06 | -1.45e-07 | +3.07e-02 | -1.21e-07 | +1.04e-04 | +3.75e-05 |
| 100<=r<=1000 | max |eps| | 6.302e-06 @ (646.56, 1.3683) | +1.16e-06 | -1.89e-07 | -1.40e-01 | -3.79e-07 | -1.71e-06 | +2.55e-06 |
| 1000<=r<=1000L | max |eps|/N_f (cut) | 1.366e-08 @ (7643.1, 1.5094) | -6.87e-07 | -1.14e-08 | -5.53e-02 | -1.49e-07 | +1.73e-03 | +2.31e-03 |
| 1000<=r<=1000L | max |eps|/N_v (cut) | 2.211e-07 @ (7643.1, 1.5555) | -6.99e-07 | +1.25e-08 | -5.69e-02 | -1.52e-07 | +1.93e-03 | +2.57e-03 |
| 1000<=r<=1000L | max |eps| | 3.096e-05 @ (7643.1, 1.4634) | -7.15e-07 | -3.49e-08 | -5.52e-02 | -1.47e-07 | +1.68e-03 | +2.24e-03 |
| r>1000L | max |eps|/N_f (cut) | 1.312e-07 @ (32735, 0.8468) | -1.53e-08 | +6.57e-09 | -2.96e-03 | -8.03e-09 | -3.94e-08 | -1.63e-07 |
| r>1000L | max |eps|/N_v (cut) | 1.079e-06 @ (37012, 1.5647) | -2.04e-07 | -1.49e-09 | -1.30e-02 | -3.69e-08 | -2.38e-07 | -4.71e-08 |
| r>1000L | max |eps| | 1.881e-04 @ (40115, 0.6596) | -1.11e-07 | +1.03e-08 | -6.01e-03 | -1.69e-08 | +7.07e-08 | +1.15e-07 |
| r<=1000 | max |eps|/N_f (cut) | 6.794e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -5.04e-03 | -2.35e-03 |
| r<=1000 | max |eps|/N_v (cut) | 1.904e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -4.87e-03 | -2.51e-03 |
| r<=1000 | max |eps| | 6.960e-05 @ (8.8109, 0.2884) | +1.06e-06 | -1.45e-08 | -3.41e-03 | -1.20e-08 | -1.12e-01 | +3.60e-02 |
| all | max |eps|/N_f (cut) | 6.794e-07 @ (8.527, 0.0092) | -8.38e-07 | +6.95e-09 | +2.98e-03 | +8.48e-09 | -5.04e-03 | -2.35e-03 |
| all | max |eps|/N_v (cut) | 1.079e-06 @ (37012, 1.5647) | -2.04e-07 | -1.49e-09 | -1.30e-02 | -3.69e-08 | -2.38e-07 | -4.71e-08 |
| all | max |eps| | 1.881e-04 @ (40115, 0.6596) | -1.11e-07 | +1.03e-08 | -6.01e-03 | -1.69e-08 | +7.07e-08 | +1.15e-07 |

Reading (floating): (1) the outer extent does not matter once the grid is aligned: between 1e5 L, 1e6 L and 1e7 L the maxima near P (2 <= r <= 10, the P disc) and in the far bands (r >= 100) change by less than 7e-6 relative, those in 10 <= r <= 100 by up to 6.8e-5, in 0.1 <= r <= 2 by up to 2.2e-4, and in r <= 0.1 (where |eps| is at the 1e-12 cancellation floor) by up to 5.5e-3; the strain c = psi_xy(0) changes by 1.3e-10 and x_* by 5e-13. The far-field closure of the inverse is converged in the outer extent with the power-law continuation (the lead's own run of this evaluator, notes/sec6closure in the lead's lane, finds an aligned extension to 1e11 L changes nothing beyond 1e-8, a zero continuation multiplies the maxima by 21 to 2900, and a half-step grid shift changes them by at most 1.5 percent; the base, taillead and tail2dec JSONs here agree bitwise with the lead's runs). The four far powers of the continuation are the first four allowed powers of the rho_x modes with remainder O(r^{4k-4}) (verifier item 151, 17:08Z; coefficients may vanish). The closure table uses the CUT normalized columns (axis columns pi/2 - theta < 0.006 excluded); the uncut N_f and N_v maxima (also in the location table above) differ in 10 <= r <= 100 (N_f 8.87e-8 uncut against 8.18e-8 cut) and r > 1000 L (N_v). (2) The far continuation itself matters: continuing the modes by the leading power only changes the
maxima in 100 <= r <= 1000 L by 1 to 14 percent (abs max at r = 647: minus 14 percent; the 1000 to 1000 L band: minus 5.5 percent; r > 1000 L: minus
0.6 to 1.3 percent), the normalized maxima near P by 0.3 percent and the absolute P-disc maximum by 0.5 percent, c by 4.5e-9; the two-decade fit
window changes nothing beyond 4e-7 outside the floor-limited band r <= 0.1 (2.5e-6 there). So the evaluated far
residual depends on how the unfitted exterior is continued at the few-percent level in the mid and far bands, consistent with the prompt's statement
that the far residual is substantially a defect of the exterior continuation, while the near-P values are insensitive (0.3 percent normalized, 0.5 percent absolute). (3) The shifted grids change the absolute maximum of the lobe at r = 8.81 by minus 11 and plus 3.6 percent (6.18e-5 and 7.21e-5 against 6.96e-5; 5.61e-5 at 22500 x 768) and the normalized maxima near P by 0.2 to 0.5 percent: this is the sampling of the knot-scale radial structure of the residual near P (section 7.5), not a closure effect, and it shows that the lobe's absolute maximum is NOT resolved by these grids (it spans 5.6e-5 to 7.2e-5); the far maxima move by less than 3e-3. (4) The rerun base values agree with the shift-1 saved table to 0.7 percent in the fitted band (0.38, 0.22 and 0.69 percent in the bands 0.1-2,
10-100 and 100-1000) and to 2.3 percent in r <= 0.1 (absolute values of order 1e-12 there, at the cancellation floor of the evaluator). Residual values at r <= 0.1 are therefore floor-limited and their locations are
not meaningful.

## 4. The explicit modal trial rho~ (data/trial_v2_h0.008.npz; src/modal_fit.py)
Definition. rho~(r, theta) = x^2 y sum_{m=0}^{M-1} a_m(r) cos(2 m theta), M = 260, with t = log r and
  r < rmin = e^{tmin} (= 1e-3 L up to rounding):  a_m = delta_{m0} + sum_{j=1}^{7} D_mj e^{2j (t - tmin)} + e^{bi (t - tmin)} sum_{i=0}^{6} Ei_mi (t - tmin)^i,
     bi = 50.000000000001066 (the stored double, 1/h_first up to rounding; the certificate uses the stored value);
  rmin <= r <= R0 = e^{t0} (about 446.1 L; X3's last knot): degree-7 B-spline in t on 1565 basis functions (knots: X3's knots mapped
     to t, intervals longer than 0.008 subdivided, uniform spacing 0.02 below X3's first knot);
  r > R0 = e^{t0} (= 446.1 L up to rounding): a_m = sum_q A_mq e^{alpha_q (t - t0)} + e^{-bo (t - t0)} sum_{i=0}^{6} Eo_mi (t - t0)^i,  bo = 125.63601455344173 (stored double),
     alpha_q = (k - 3) - j (1 - k) - 2 l for (j, l) in {(0..5, 0), (0..2, 1), (0, 2)} (X3's own far-field structure
     u^{k-3} (1 + nu + nu^2 + ...)(1 + u^-2 + ...), nu = u^{-(1-k)}).
Center: a_0(0) = 1 exactly and a_m(0) = 0 for m >= 1, so rho~ = x^2 y (1 + O(r^2)) with a continuous (not smooth:
the core polynomial terms r^{2j} cos(2m theta) with m > j are not C^infinity at 0, which is enough for P_2).
Joins: C^6 at rmin and R0 (the local corrections absorb the jet mismatch; without them the C^6 join to slowly decaying
power laws distorts the fit by 3e-7). Normalization (raw strain c_raw[rho~] = psi~_xy(0), written c in 7.2): int_0^oo r (a_0/4 + a_1/8 - a_2/8 -
a_3/8) dr = 3/k - 1 (this is the published identity c = int rho_1 r^-2 dr, rho_1 = R_1 the sin(3 theta) coefficient of rho~ (including r^3), written in the
cosine modes; verified numerically to 1e-8).
Fit: least squares to the cosine modes of e^H of X3 on 80000 log-spaced radii (4096 angles), relative weighting by the
base factor (1+u^2)^{(k-3)/2}, join and normalization constraints exact (nullspace method, column scaling).
Quality (1500 random radii, direct X3 formula; floating point; modal errors |a_m - a_m(X3)| normalized by the base factor (1+u^2)^{(k-3)/2}, section 4 fit weighting): error of a_m 5.1e-10 (values) and 1.3e-9 (t-derivatives)
in the middle region, 1.4e-13 inner, 8.5e-12 outer; dropped modes m >= 260 at most 1.9e-11; sum over modes of the
error 1.3e-9 (values), 8.6e-9 (derivatives). Joins hold to 6e-15; normalization to 1e-14. At each of 1638 sampled radii,
max_theta |rho~ - rho_bar(X3)| / max_theta |rho_bar(X3)| <= 1e-9 (2049 angles; a sampled floating-point comparison, not a pointwise relative
error and not a continuous enclosure). Exactness convention for the certificate: the stored S, D and A (except A_00), the knots, k, L, bi and bo
are the exact definition; Ei, Eo and A_00 are defined by the join and normalization equations and were recomputed in ball arithmetic and
exported as exact dyadic balls (section 7.1(d); they differ from the floating least-squares values by at most 1e-13 relative).

## 5. Closed-form canonical inverse of rho~ (src/expoly.py, src/trial_green.py; float64 here; the Arb version is the certificate of section 7)
Every a_m is a finite sum of e^{alpha tau} tau^j on each radial cell, hence so are the sine coefficients R_j (rho~ = sum_{j=0}^{260} R_j(t) sin((2j+1) theta), the R_j including the factor e^{3t}), the modes f_n of d_x rho~ (sin(2n theta), n <= 261) and the Green
integrals A_n = r^{-2n} int_0^r s^{2n+1} f_n ds, B_n = r^{2n} int_r^oo s^{1-2n} f_n ds, psi_n = (A_n + B_n)/(4n),
psi_n' = (B_n - A_n)/(2r), c = (1/2) int_0^oo f_1/s ds. Convergence conditions at 0 and infinity (exponent > -2n-2,
< 2n-2) hold with margin (at 0: d_x rho~ = 2xy + O(r^4), so f_1 = r^2 + O(r^4) and f_n = O(r^4) for n >= 2; s^{k-1} at infinity). Cell recurrences use exact exponential moments; for
|lam| h < 1.5 the moments are evaluated by 32-node Gauss-Legendre to avoid the catastrophic cancellation of the closed
primitive (the Arb certificate, 256 bits, uses the closed form and switches to the convergent series when |lam| max(|a|, |b|) < 1/2, section 7.3). Validation against the independent grid inverse (src/inverse.py)
applied to the same f_n: relative error of all psi_n, psi_n' at r = 0.003 to 8.6: 1.6e-11 to 8e-11; 2.5e-10 at r = 50,
1e-8 at 3000, 7e-8 at 3e4 (the grid's tail-fit error); c: 15.726087831925 (closed form) against 15.726087783 (grid).
Normalization identity of the trial (raw strain c = psi~_xy(0), floating): 3 c_l - 1 - c = -6.8e-14 with c_l = 1/k (the exact statement is 7.2). The elliptic equation holds exactly
(Lap psi~ = -d_x rho~ mode by mode); there is no elliptic residual to enclose.

## 6. Residual of rho~ (floating point, runs/trial_v2_resid.json; src/trial_resid.py)
eps~ = (c_l X + U~).grad rho~ - rho~ = sum_{N<=521} eps_N(r) sin((2N+1) theta) at 1638 radii (522 sine modes: the 260 cosine modes of rho~ scattered
by the 261 velocity modes); columns: the sup over 2049 angles of |eps~|; the maximum over the region's sampled radii of the pointwise Wiener sum
W(r) = sum_N |eps_N(r)| (>= sup_theta |eps~(r, theta)|); 'W/sup' = the maximum over the region's sampled radii of the pointwise ratio
W(r)/(max over the 2049 sampled angles of |eps~(r, theta)|) (not the ratio of the two preceding columns); 'N_v max' = max of |eps~|/N_v with N_v = |rho~| + |X.grad rho~| +
|U~.grad rho~| (the prompt's second denominator), the near-y-axis columns excluded as in the published tables:
| region | sup eps (sampled) | W max | W/sup | N_v max | X3 published |
|---|---|---|---|---|---|
| r <= 0.1 | 9.0e-14 | 1.9e-13 | 3.1 | 4.8e-11 | abs 1.7e-13 |
| 0.1-2 | 8.90e-8 | 2.02e-7 | 3.5 | 5.5e-8 | abs 8.92e-8 |
| 2-10 | 5.39e-5 (r = 8.79) | 1.05e-4 | 4.5 | 1.99e-7 | abs 6.03e-5 / 5.82e-5, N_v 1.92e-7 / 2.01e-7 |
| 10-100 | 1.89e-5 | 3.68e-5 | 4.4 | 7.1e-8 | abs 1.99e-5 |
| 100-1000 | 6.29e-6 | 1.29e-5 | 3.0 | 6.6e-8 | abs 6.03e-6 |
| 1000-1000 L | 3.01e-5 | 5.37e-5 | 2.8 | 2.10e-7 | N_v 2.15e-7 |
| > 1000 L | 1.895e-4 (r = 4.05e4) | 4.27e-4 | 2.4 | 1.079e-6 | abs 1.897e-4, N_v 1.09e-6 |
So rho~ carries X3's residual (and X3's far-field Theta_1 mismatch; the lead decides whether to force the compatible
far field, whose residual for an M-mode density has angular frequencies up to 4M+3, i.e. 2M+2 odd-frequency sine modes, and is not done; Theta_1 is
the first correction of the far-field expansion rho ~ r^k Theta_0 (1 + r^{k-1} Theta_1 + ...) of PROMPT.md section 2, constrained by Theta_0 through
the compatibility equation (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k F' Theta_0 for psi_0 = r^{k+1} F(theta)). The regional maxima of the
pointwise ratio W(r)/(max over the sampled angles of |eps~|) lie between 2.4 and 4.5.

## 7. Rigorous enclosures (the certificate)
All statements of this section are about the EXACT trial rho~ defined as follows (data/trial_v2_h0.008.npz with
data/cert_coeffs.json): the stored doubles S (spline coefficients, 260 x 1565), D (inner powers, 260 x 7), Aout (outer
power laws, 260 x 10, except A_00) and the knots are the definition; the join abscissae are tmin = knots[0] and
t0 = knots[-1] (stored doubles); L, k, bi = 50.000000000001066 and bo = 125.63601455344173 are the stored doubles; c_l := 1/k. The exact
region boundaries are rmin = e^{tmin}, R0 = e^{t0}, r_T,out = e^{t0 + 17} and r_T,in = e^{tmin - 5}; their decimal displays (rmin = 0.0076514,
R0 = 3413.0 = 446.1 L, r_T,out = 8.2440e10, r_T,in = 5.1555e-5) are approximate throughout this section. The dependent coefficients
Ei (inner corrections), Eo (outer corrections) and A_00 are DEFINED as the unique solutions of the C^6 join equations at
tmin and t0 and of the normalization c[rho~] = 3/k - 1, computed in Arb at 256 bits and exported losslessly as exact dyadic balls
(data/cert_coeffs.json; section 7.1(d); they differ from the floating least-squares values by at most 1e-13 relative).
Consequences holding exactly: rho~ is C^6 across r = rmin and r = R0 and C^infinity elsewhere away from the axes
(C^6 in theta... no: rho~ is a finite trigonometric polynomial in theta times x^2 y, hence smooth in theta; in r it is
C^6 at the two joins and at the spline knots, C^infinity otherwise); a(0) = 1; Lap psi~ = -d_x rho~ with psi~ the closed-form
canonical inverse; c_l = (1 + psi~_xy(0))/3 and c_l k = 1 (so the leading far-field term of the residual vanishes identically).

### 7.0 Notation and definitions used throughout this report (added 2026-10-22, shift 7, after the referee passes astra/numrep1 and numrep2)
- Coordinates and constants: X = (x, y), r = |X|, theta the polar angle (theta = 0 the positive x axis, pi/2 the y axis), t = log r, u = r/L with
  L = 7.651424601381517 (X3's stored scale), k = 0.17936053129375418 (X3's stored exponent), c_l = 1/k = 5.5753626106415.. (the identity
  c_l = (1 + psi~_xy(0))/3 holds for the trial by construction, 7.2). The unit roundoff 2^-53 is written u_mach (7.1(b)) to avoid the clash with u.
- Profiles and fields: rho_bar = the published X3 (section 2); rho~ = the modal trial of section 4 ('the trial'; its exact definition is the
  section 7 preamble); U~ = grad^perp psi~ its canonical velocity (section 5), V = V~ = c_l X + U~ the transport field, eps~ = V.grad rho~ - rho~
  the residual, G = X.grad rho~, K = K~ = rho~ - X.grad rho~ the scaling tangent. Modes: rho~ = x^2 y sum_{m<260} a_m(r) cos(2m theta) =
  sum_{j=0}^{260} R_j(t) sin((2j+1) theta) (261 sine coefficients, each including the factor e^{3t} = r^3 as returned by TrialGreen.rho_modes, so
  R_j = O(r^3) at 0; rho_1 := R_1 is the sin(3 theta) coefficient of the normalization identity of section 4), d_x rho~ = sum_{n<=261} f_n(r) sin(2n theta), psi~ = sum_n psi_n(r) sin(2n theta) with psi_n = (A_n + B_n)/(4n) (section 5),
  eps~ = sum_{N=0}^{521} eps_N(r) sin((2N+1) theta) (522 sine modes with frequencies 2N+1 up to 1043 = 521 + 2 x 261, from the products of the 261
  density modes with the 261 velocity modes; the code carries an identically zero padded slot N = 522). V, P, w, h_axis and g refer to the profile
  under discussion: X3 in sections 2 and 3, the trial everywhere else.
- Points and sets: the origin 0; P = (x_*, 0) with x_* the first positive zero of V_1(x, 0) (7.2); w(x) = V_1(x, 0), h_axis(x) = d_y V_2(x, 0)
  (so h_axis(P) = mu~; 'h(P) - 1' in section 3 is h_axis(P) - 1), g = rho~_y(P); 'the lobe' = the residual maximum at r = 8.8 next to P, inside the
  shell 4 <= r <= 16; 'P-disc' = the disc |X - P| < 0.5 in 7.5, 7.7c and 7.8, and the 377 radial cells meeting |X - P| < x_*/4 in 7.3b (the radius is
  to be read from the subsection: 0.5 in 7.5, 7.7c and 7.8, x_*/4 in 7.3b, 3 delta in 7.7); B_1 = [4.80, 6.82] x [0, 2.85] (7.6). Regions of the certificate: middle [rmin, R0], outer [R0, r_T,out], inner [r_T,in, rmin],
  tails r > r_T,out and r < r_T,in, with the exact boundaries of the section 7 preamble (rmin = e^{tmin}, R0 = e^{t0}, r_T,out = e^{t0+17},
  r_T,in = e^{tmin-5}); decimal radii are approximate displays of these.
- Denominators and weights: N_f = |V_1 rho_x| + |V_2 rho_y| + |rho|, N_v = |rho| + |X.grad rho| + |U.grad rho| (PROMPT.md section 2; sections 3 and 6
  tabulate max |eps|/N_f and max |eps|/N_v, with the near-y-axis columns excluded where stated); m(r) = u^3 (1+u^2)^{(k-3)/2} (the radial size of the
  base factor x^2 y (1+u^2)^{(k-3)/2}: m ~ r^3/L^3 at 0, ~ u^k at infinity); multiplier weights (1+u)^{1/2} and (1+u)^{1/2-k} (the exponent 1/2 - k
  of the stored k; its decimal display 0.3206394687062458... is approximate and is written 0.3206 in some column heads); the X-norm weight w = m^{-2} (1+u^2)^{-3/2} with ||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX
  (7.11; the H1m inner product of 7.4b is the same weight).
- Certificate quantities: W = the certified cell bound of 7.1(c) (max over 4 sub-intervals of sum_N sup_sub|eps_N|, >= sup over the cell and theta of
  |eps~|); W_i_j = the cell majorants of d_t^i d_theta^j eps~ from the derivative certificate: with b_{i,N,s} the certified bound of |d_t^i eps_N| on
  sub-interval s (4 sub-intervals), W_i_j = max_s sum_N (2N+1)^j b_{i,N,s} for i + j <= 2 and W_i_j = sum_N (2N+1)^j max_s b_{i,N,s} for the higher
  orders (so W_0_0 is the derivative run's own subdivided cell bound, the analogue of W);
  m_inf = the cell minimum of m; 'L2 piece' as in 7.3. Diagnostic labels (SPEC items): S1 = the point scalars at 0 and P (7.2); R0 = sup of W/m and
  of the two multiplier forms, by region (7.3); R1 = sup r|grad eps~|/m and sup r^2|D^2 eps~|/m with |D^2 eps~| the maximum over the three second
  partial derivatives (max-entry norm; the Frobenius norm is at most twice it) (7.3b); R2 = (int |eps~/m|^2 dX/(1+u^2))^{1/2} (7.3); R3 = the absolute
  W_i_j up to order 5 on the P-disc cells (7.3b); R4 = sup W/r^5 near the origin (7.3); R5 = sup W_F/m, sup W_K/m, sup W_dtK/m with W_F := W_{eps - d_t eps} the cell majorant of eps~ - d_t eps~ (saved as W_eps_minus_dteps), the
  R0-type norms of eps~ - X.grad eps~ (= L K), of K and of d_t K (7.3b); N1' = the flow certificate (7.6); N8, N9, N10 = the lead's requests of 7.7,
  7.9 and 7.7c/7.10.
- Classes: P_2 = the finite-regularity target class of PROMPT.md section 1: rho in C^{2,alpha}_loc(R^2) for some 0 < alpha < 1, the centre
  factorization rho = x^2 y a with a continuous near 0 and a(0) = 1, the parity, the canonical full-plane velocity law, the growth bound
  |rho| + (1+|X|)|grad rho| <= C (1+|X|)^gamma for some gamma < 1, and the stationary equation pointwise. The trial satisfies the regularity, centre,
  parity, velocity and growth requirements (it is C^6 across both joins and every interior spline knot, smooth between them away from the origin,
  with a continuous centre factor, section 4) but is not a solution: that is what the residual certificates quantify.
- Linearization and strain: L h = V.grad h - h + (U[h] + c[h] X).grad rho~ with -Delta psi[h] = d_x h, U[h] = grad^perp psi[h] and
  c[h] = psi[h]_xy(0)/3 (PROMPT.md (lin), (rank-one)); the raw strain c_raw[h] = psi[h]_xy(0) = 3 c[h] is used in 7.8 and in the B(K, K) check of
  7.11; in sections 4, 5 and 7.2 the symbols c, c~, c[rho~] denote the RAW strain psi_xy(0) of the profile (= 3 c_l - 1 for a normalized profile;
  PROMPT.md 'c = psi_xy(0,0)'). J(h) = the x^2 y coefficient of h at the origin (h = x^2 y (J(h) + o(1)); J(K) = -2); the normalized tangent space
  = {h : J(h) = 0}, the perturbations preserving a(0) = 1. B(h, g) := U[h].grad g is the bilinear part of the nonlinearity (F(rho~ + h) = eps~ + L h +
  B(h, h) + c[h] X.grad h). The scaling identity L K = eps~ - X.grad eps~ holds EXACTLY for every trial that is a C^1 function (no normalization condition is needed),
  with L built from the trial's own field V (differentiate the family lambda^{-1} rho~(lambda X), whose canonical velocity is lambda^{-1} U~(lambda X)
  and whose residual with the same c_l is lambda^{-1} eps~(lambda X), at lambda = 1; c[K] = 0 exactly since psi[K] = 2 psi~ - X.grad psi~); it holds
  in particular for the exactly joined certificate trial of section 7 (verifier topic 138 states it for the exactly normalized trial). The STORED
  coefficient representation (data/trial_v2_h0.008.npz with its floating Ei, Eo, A_00) is NOT such a function: all 260 modal coefficients jump at the
  two joins r = rmin and r = R0 (join defects of order 6e-15 relative, section 4; not H^1_loc there, verifier, FINAL_REPORT), so for it the identity
  holds on each open region only up to an interface term U[M].grad rho~ driven by the jumps M and a strain term (c[K_pw]/3) X.grad rho~ with
  c[K_pw] about 4.5e-18 (lead 02:49Z, verified). Every floating quantity involving K, L K or B(K, K) (7.4c, 7.11) concerns the STORED representation
  evaluated at interior quadrature nodes, so these interface and strain terms enter them only through the nonlocal velocity at the size of the
  jumps, below every printed digit; the printed values are nevertheless statements about the stored representation, not about the exact trial.
- Finite sections (7.4 to 7.4c; floating): the 'F- class' is the lead's column set (SPEC 3.6) assembled by src/c2_fminus.py: for every angular
  mode m < Mh, the inner powers e^{2j tau'} (j = 1..7, tau' = t - tmin; plus the constant for m = 0, the 'J column' x^2 y on r < R0), degree-7
  B-splines on every stride-th knot of the trial, and outer power laws e^{alpha (t - t0)} with growth below r^k; plus the two scalar columns
  KP = x^2 y chi(t) t e^{(k-3)(t-t0)} Theta_0~, the k'-derivative at k' = k of the family x^2 y chi e^{(k'-3) t - (k-3) t0} Theta_0~ (the implemented
  factor is t, not t - t0; the two choices differ by t0 times the leading tail, which is not in the F- span), with Theta_0~ = sum_m A0_m cos 2m theta,
  A0 = the trial's stored leading outer coefficients Aout[:, 0]; TAU = x^2 y chi e^{(k-3)(t-t0)} (Theta_0~ cos 2 theta)_{m < M}, the product projected
  onto the trial's M = 260 modes independently of Mh (mode coefficients B_m; the single omitted coefficient is A0_{M-1}/2 = -3.9e-19 for the base trial); chi = the sum
  of the trial's last 10 B-splines (a C^6 cutoff: 0 well inside R0, 1 near and beyond R0, so that the tail columns live at and beyond the cutoff); the
  'free span' adds the pure tails x^2 y chi e^{(k-3)(t-t0)} cos 2m theta, m < Mh; J_inner = x^2 y on r < rmin. In the lead's sense (SPEC 3.6) the F-
  class is the space of perturbations with far-field growth strictly below r^k (leading tail fixed). The ordinary columns are a piecewise discretization
  of such perturbations (their broken-gradient norm does not by itself place them in the operator's graph domain; the C^0/C^1 join constraints of 7.4b
  are imposed separately), augmented by the KP (growth r^k log r) and TAU (growth r^k) directions, which lie OUTSIDE the strictly-lower-growth class;
  in 7.4b and 7.4c the columns are measured in the broken-gradient H1m Gram norm and the images by the four row functionals; the raw sections of 7.4
  use the sampled sup-proxy column weights described there. Labels: M16/s16/Mout40 = Mh = 16 angular modes, radial stride 16, image
  modes N < Mout = 40; 'ppc' = collocation points per coarse radial cell; NJ0/NJ1 = C^0/C^1 join constraints at tmin and t0; 'retained', 'eigen-cut',
  the row functionals L2/L2q/H1/H1q and ell(Phi) are defined in 7.4b, 7.4c and 7.4 respectively; the per-row normalization of a singular value
  means division by the square root of the row count.
- Local source estimate (7.7, 7.9, 7.10; SPEC 3.15): delta = the ball radius about P (B_{3 delta}(P) is the certification ball; delta = 33/2000 for
  the forcing bound); kappa_loc = 3.374 = the lead's local constant (distinct from the transport parameter kappa = 0.2 / 0.22 of 7.6); M_V = sup|D^2 V|
  and M_rho = sup|D^2 rho~| (Frobenius norms) on B_{3 delta}(P), C_V = 41.7 M_V + 3 M_rho with SPEC's constants (for cutoffs of SPEC's class with
  derivative constant C_theta = 2; the admissibility inequalities producing the coefficients 41.7 and 3 are SPEC 3.15's and are not restated here:
  this lane certifies only M_V and M_rho), E = the perturbation of the source linearization by the cutoff (bounded by E <= C_V delta), the admissibility
  threshold C_V <= kappa_loc/(2 delta) (102.24 at delta = 0.0165), K_1 = 1/(kappa_loc - E); R (a Wiener-type bound of the cutoff perturbation w) and E
  (its energy) enter the auxiliary inverse bound (1/a_s)(1 + R/(a_0 - a_s))^s of 7.9, with alpha_r, beta_r and the dilated R~(ell) defined there; the
  forcing norms are ||f||_{H^s} and N_lambda(f)^2 = int (lambda^2 + |xi|^2)^s |f^(xi)|^2 dxi (lambda = 1/ell; 7.10). Cutoffs: 7.7c uses
  tau = Q((|X-P| - 7 delta/4)/(delta/2)) with Q(u) = e^{-1/(1-u)}/(e^{-1/(1-u)} + e^{-1/u}) on (0, 1), Q = 1 for u <= 0, Q = 0 for u >= 1; 7.10 uses the
  degree-9 polynomial tau = step(1 - (|X-P| - 7 delta/4)/(delta/2)) with step(u) = 126u^5 - 420u^6 + 540u^7 - 315u^8 + 70u^9 on [0, 1], step = 0
  below 0 and 1 above 1 (both: tau = 1 on B_{7 delta/4}(P), supported in B_{9 delta/4}(P)); the N9 cutoff chi of 7.9 is 1 up to 2 delta and 0 beyond
  3 delta; the local cutoff chi_loc of SPEC 3.15 is supported inside B_{7 delta/4}(P), so that tau = 1 on it.
  Sobolev norms: inhomogeneous, ||f||_{H^s}^2 = int (1 + |xi|^2)^s |f^(xi)|^2 dxi with the unitary transform (7.10), equivalently (2 pi)^{-2} int ...
  with the unnormalized transform (7.7c).
- Flow certificate (7.6): s = X.V/r^2, T_0 = -(1 + c_l) + a (V_1/x - s) + b (V_2/y - s) + mu(r) s with a = 129/20, b = 307/100,
  mu(r) = gamma' + (a + b - gamma')/(1 + (r/6)^4), gamma' = 1129/1000; ||R_-|| denotes the operator norm of the lead's transport inverse in SPEC's
  weighted sup norm, and the values 6.31 / 5.76 are the lead's bound ||R_-|| <= kappa^{-1} e^{(1.278 + kappa) t_1}, t_1 = 2.02/12.834 (T_0 <= 1.278 and
  V_1 <= -12.834 on the box B_1 of width 2.02, under the lead's transport hypotheses (Y), (H2')-(H4) of 7.6) evaluated with this lane's certified
  field ranges, not an operator bound proved here; the operator, its boundary condition, domain, codomain and weight are the lead's (SPEC.md,
  transport inverse; FINAL_REPORT section 5) and are not restated in this report, which certifies only the field ranges entering the constants.
- Arithmetic: all rigorous results use either Arb balls (python-flint; 256 bits for the certificate data, 100 to 200 bits in the summaries) or the
  rigorous mid-rad float64 arithmetic of src/midrad.py (7.1(b); each rounded product adds the underflow allowance eta to its radius and each K-term
  sum adds K eta); every printed certified decimal is an outward rounding (ceilings for upper bounds,
  floors for lower endpoints); 'floating' marks ordinary double-precision evaluations, which are evidence only.

### 7.1 Method
(a) Arb (python-flint, 256 bits): exact per-cell Taylor coefficients of the splines (Cox-de Boor derivative recursion);
    A_n(t), B_n(t) (n <= 261) at the 7810 boundaries of radial sub-cells of length <= 0.0019 in t = log r (so that
    2 n h <= 1), by the exact closed-form recurrences; the inner head (r < rmin) and outer tail (r > R0) integrals in
    closed form; c = psi~_xy(0); exactification of Ei, Eo, A_00. Export as (mid, rad) doubles with the conversion error
    added to the radius (src/cert_green.py; 16 min).
(b) Rigorous mid-rad arithmetic in numpy (src/midrad.py): IEEE binary64 round-to-nearest model with the inflation rules of Rump (unit roundoff
    u_mach = 2^-53, beta = u_mach/(1 - u_mach), underflow term eta = 2^-1074 with gradual underflow and no overflow assumed, outward rounding by
    nextafter of every radius operation). Inflation rules by operation: matrix products (mr_matmul) with gamma_{2K} = 2K u_mach/(1 - 2K u_mach) for
    sums of K terms; the residual mode convolutions (cert_resid.conv_scatter) with gamma_K, K = Q + 1, and the explicit underflow allowance 4 (K+1) eta;
    scalar sums (MR.sum) with K eta. Tested against Arb on random data and on exact-integer products.
(c) Taylor models (TM) of degree 12 on every sub-cell [t_a, t_a + h] (src/cert_resid.py): every modal function is enclosed
    by a polynomial in sigma = t - t_a with mid-rad coefficients plus a remainder bound valid on the whole sub-cell:
    exponentials by their Taylor series with the Lagrange remainder (|gamma| h <= 1); the spline part exactly; A_n, B_n by
    the Taylor recursion of the ODEs A' = -2n A + g, B' = 2n B - g from the certified boundary values, with the remainder
    h^{Q+1}/(Q+1)! [(2n)^{Q+1} sup_cell|A_n| + sum_{i=0}^{Q} (2n)^{Q-i} sup_cell|g_n^{(i)}|], Q = 12, g_n(t) = e^{2t} f_n(e^t) the ODE forcing
    (its derivative sups from the exponential-polynomial form of g_n; the sup of the solution over the cell by Y = e^{max(lam, 0) h} (|y(t_a)| +
    h sup|g_n|) with lam = -2n for A_n and +2n for B_n, from the certified boundary value; src/cert_resid.py ode_tm);
    products of TMs with truncation and remainder propagation; the residual modes eps_N (N <= 522) as sums of two mode
    convolutions and the linear part; the sub-cell is split into K = 4 equal sub-intervals, on each the polynomial is re-centred (exact
    binomial shift in mid-rad arithmetic) and sup_sub|eps_N| is bounded by its Bernstein coefficients plus the remainder; the CERTIFIED CELL
    BOUND is W := max over the 4 sub-intervals of sum_N sup_sub|eps_N| (src/cert_resid.py bernstein_sup_sub), which majorizes the sup over the
    cell and over theta of |eps~| and the sup over the cell of the pointwise Wiener sum of section 6 (the symbol W in the cell rows of 7.3 to
    7.3c means this cell bound, built from certified modal upper bounds b_{N,j} >= sup_{sub_j}|eps_N|; in the tail rows W denotes the termwise
    majorant of the tail routines, 7.1(e)); the per-mode values sup_N := max over the sub-intervals of sup_sub|eps_N| enter the L2 pieces (7.3).
    Derivatives d_t^i eps_N (i <= 2 on the three finite regions middle, outer and inner, not on the two tails; i + j <= 5 on the 377 cells
    meeting the disc |X - P| < x_*/4) by the same identities and Leibniz rules (src/cert_resid_deriv.py).
    Angular derivatives: sum_N (2N+1)^j sup|.|. Weights: m(r) = u^3 (1+u^2)^{(k-3)/2} is increasing, so inf over a cell is
    its value at the left end (Arb); far weight (1+u)^{gamma-k} bounded by its value at the right end.
(d) Coefficient transport: the exactified Ei, Eo, A_00 are exported as exact dyadic balls (integer mantissa and
    exponent of the midpoint and of the radius; src/cert_green.ball_dyadic) and re-imported losslessly (load_ball; round-trip
    containment verified for all 3640 coefficients). Two earlier exports (60 digits without radius; 100 digits with a
    5-digit nearest-rounded radius) were not enclosures (verifier 15:18Z, 15:41Z); all results depending on them are
    recomputed (chain4, chain2).
(e) Regions (final configuration): middle [rmin, R0] (7809 sub-cells of length <= 0.0019 in t), outer tau := t - t0 in [0, T_out] with
    T_out = 17 (R0 <= r <= r_T,out = e^{t0 + 17} = 8.2440e10; 8948 sub-cells), inner tau' := t - tmin in [-T_in, 0] with T_in = 5
    (r_T,in = e^{tmin - 5} = 5.1555e-5 <= r <= rmin; 2632 sub-cells); an earlier configuration (T_out = 10, 5263 cells; T_in = 2.5, 1316 cells)
    is historical and appears only in the 'pre-fix' remarks of 7.3. Beyond r_T,out and r_T,in: termwise majorants of the exponential-polynomial
    representation at the last boundary (src/cert_tail.py, src/cert_inner_tail.py). Outer tail: the residual majorant is an exponential polynomial
    in tau = t - t0; for every absolute monomial tau^i e^{beta tau} of its UNWEIGHTED representation the condition beta + i/T_out + delta - k < 0 is
    checked in Arb through sufficient bounds on the exponent/degree families of the multiplied majorant (the outer powers and the products' exponent
    families, which cover every monomial; the code does not enumerate the monomials individually); the factor (1+u)^delta/m, delta = 1/2 - k,
    contributes the growth delta - k at infinity, and tau^i e^{beta tau} is decreasing for tau >= T_out when beta + i/T_out < 0; the worst family gives
    -1/2, i.e. a margin of 1/2 ('monotone_ok'); then the termwise value
    at tau = T_out bounds all tau >= T_out (the exponent-k term of c_l X.grad rho~ - rho~ vanishes identically by c_l k = 1, and the exact
    e^{(2k-1) tau} coefficient of every mode is kept). Inner tail: every term of eps_N has exponent >= 3 in tau' = t - tmin (>= 0 after division
    by m). Polynomial factors |tau'|^i arise (i) from ordinary resonances of the Green primitives (degree 1; e.g. the a-exponent 2 at n = 3 gives a
    term |tau'| e^{7 tau'}) and (ii) from the exp-poly corrections e^{bi tau'} tau'^i (degree up to 8 in the near-resonant branch, up to 14 after the
    product with the degree-6 density correction), with exponents >= bi - 1. A monomial |tau'|^i e^{beta tau'} divided by r^5 (which also covers the
    division by m ~ r^3) is decreasing towards the origin for tau' <= -T_in when beta - 5 - i/T_in >= 0; the code checks the sufficient degree condition
    8/T_in <= bi - 5 for the correction family (margin 43.4; a degree-14 term has the far larger margin 2 bi - 6 - 14/T_in) and the ordinary resonances
    have margins >= 7 - 5 - 1/T_in = 1.8; a complete enumeration of the families is not printed by the code (referee astra/numrep5); the exponent-3 part equals (3 c_l - 1 - c) x (the x^2 y coefficient) and is taken exactly: the scalar
    certificate encloses 3 c_l - 1 - c in a ball of radius 1.7e-50 (7.2) and the tail routine, after its own transport of the coefficients, in a
    ball of radius 2.45e-15 (runs/cert_inner_tail.json 'normalization_defect'), which is the value it uses.
(f) External refereeing: astra (astra/cert1/answer.md, 16:0xZ) confirmed the analytic formulas of (c) and (e) (ODE remainder,
    exponential Taylor remainder, product remainder algebra, Bernstein theorem, tail decay conditions, cubic accounting of
    the inner tail) and found implementation defects (cancellation-unsafe rounding term in the polynomial product, Bernstein
    ratios and powers of h treated as exact in signed transformations, missing underflow allowances, a non-lower-bound
    helper, exponents of the outer basis exported without radius, a non-enclosing coefficient exporter, a missing factor 2
    in the tail majorants); all were repaired (WORKLOG 16:1xZ). A second referee round (astra/cert2/answer.md, 17:1xZ)
    confirmed the repairs, proved the series tail bound, the dyadic transport and the refined outer leading order, and found
    further defects (Bernstein ratio radii, float conversion of the series tail, non-outward summary endpoints, truncation
    underflow amplification, degree conditions of the inner tail, and an execution-order blocker of the middle-region CLI);
    all repaired (WORKLOG 17:1xZ). Every number in this section is from the repaired code unless marked "pre-fix"; the
    middle-region rerun (chain5), the inner/outer regeneration (chain4) and the variants (chain2) run with the final code.
(g) Validation of the machinery: on a 20-mode truncation of the trial the TM bounds reproduce the floating closed-form
    pipeline to 0.1 to 37 percent (sup over a cell against its midpoint value) with remainders <= 1e-12, and the derivative
    TMs reproduce finite differences to 1 percent (src/test_cert_small.py, src/test_cert_deriv.py).

### 7.2 Scalars (S1), rigorous, runs/scalars_full.json
| quantity | enclosure |
|---|---|
| c~ = psi~_xy(0) | 15.72608783192463802666938 +/- 4.6e-24 = 3 c_l - 1 (defect +/- 1.7e-50) |
| c_l = 1/k | [5.575362610641544, 5.575362610641549] |
| A = 2 c_l - 1 | [10.150725221283087, 10.150725221283099] |
| x_* (root of V~_1(x, 0)) | 8.600063805157177 +/- 2.95e-13 (raw radius 2.9402020296740933e-13; interval Newton contracted at radius 1e-12) |
| mu~ - 1 = d_y V~_2(P) - 1 | [-2.25290e-8, -2.25271e-8] (raw [-2.2528936380700347e-8, -2.2527166467961448e-8]) |
| A~ = 2 c_l - mu~ | [10.150725243810255, 10.150725243812036] |
| w'(P) = d_x V~_1(x_*, 0) | [10.150725243807494, 10.150725243814782] (binary64 endpoints 10.150725243807495, 10.150725243814781, displayed outward); w'(P) + mu~ - 2 c_l in [-4.54e-12, 4.53e-12] (raw [-4.538106273755034e-12, 4.523895419039832e-12]; divergence identity, certified consistency) |
| g = rho~_y(P) | [29.749490663330, 29.749490663337] |
| g' = rho~_xy(P) | [0.27341144397680667, 0.2734114439776933] |

### 7.3 Residual norms (R0, R1, R2, R4, R5)
RIGOROUS, POST-FIX (repaired code, chain5 rerun 22:54-23:38Z with the sub-interval Bernstein bound; runs/cert_resid_middle.json, 7809
sub-cells; summaries runs/cert_summary_all.txt (src/cert_summary.py) and runs/report_tables.md (src/report_tables.py, which prints the tables of
this subsection and of 7.3c with DIRECTED rounding: every upper bound is rounded up at the printed digits, interval endpoints outward, locations
'at r' to nearest; shift 7 regeneration after the referee pass astra/numrep1). Definitions: W is the certified cell bound of 7.1(c) (max over the 4
sub-intervals of sum_N sup_sub|eps_N|; W >= sup over the cell and over theta of |eps~|); m(r) = u^3 (1+u^2)^{(k-3)/2} is increasing, and its cell
minimum m_inf is its value at the left end (Arb); 'W/m' means W/m_inf. The three requested forms: the divisor form W/m; the multiplier form
W (1+u)^{1/2}/m; the secondary multiplier form W (1+u)^{1/2-k}/m with the exponent 1/2 - k of the stored k (decimal display 0.3206394687062458...,
approximate; written
0.3206 in some column heads of this report; the SPEC v2 weight m (1+u)^{gamma-k} at gamma = 1/2). The multiplier weights are increasing and are
bounded by their value at the right end of each cell (Arb). The 'L2 piece' of a cell is pi h sup_cell[r^2/(m^2 (1+u^2))] sum_N sup_N^2 (outward
arithmetic, src/cert_resid.py), an upper bound of int_cell int_0^{2 pi} |eps~/m|^2 dX/(1+u^2) by Parseval (int_0^{2 pi} sin^2((2N+1) theta) dtheta = pi);
these entries bound SQUARED norms. Shell rows list the cells meeting the shell (a cell straddling a shell boundary is counted in both rows); the
whole-region totals count each cell once.
| shell of r (cells meeting it) | max W/m (divisor) | at r | max W (1+u)^{1/2}/m | max W (1+u)^{1/2-k}/m | max W (absolute) | sum of L2 pieces |
|---|---|---|---|---|---|---|
| [rmin = 0.0076514, 0.0156) | 2.1899e-8 | 0.007721 | 2.1910e-8 | 2.1906e-8 | 2.251e-17 | 1.191e-21 |
| [0.0156, 0.0625) | 5.1780e-8 | 0.06248 | 5.1991e-8 | 5.1915e-8 | 2.820e-14 | 9.900e-19 |
| [0.0625, 0.25) | 5.1039e-7 | 0.2497 | 5.1867e-7 | 5.1569e-7 | 1.772e-11 | 1.266e-15 |
| [0.25, 1) | 7.0373e-6 | 0.9984 | 7.4835e-6 | 7.3202e-6 | 1.534e-8 | 3.181e-12 |
| [1, 4) | 1.9003e-5 | 3.951 | 2.3412e-5 | 2.1723e-5 | 1.887e-6 | 1.416e-10 |
| [4, 16) | 2.5965e-4 | 8.79 | 3.8071e-4 | 3.3187e-4 | 1.202e-4 | 3.255e-9 |
| [16, 64) | 2.0262e-5 | 16.07 | 3.5695e-5 | 2.9133e-5 | 1.735e-5 | 4.292e-10 |
| [64, 256) | 6.4955e-6 | 117.2 | 3.3222e-5 | 1.7686e-5 | 1.113e-5 | 4.181e-10 |
| [256, 1024) | 6.0920e-6 | 305.9 | 5.6439e-5 | 2.4758e-5 | 1.293e-5 | 4.203e-10 |
| [1024, R0 = 3413.0) | 5.5626e-6 | 3408 | 1.1762e-4 | 3.9363e-5 | 1.661e-5 | 3.087e-10 |
Whole middle region [rmin, R0] = [0.00765142, 3412.97] (7809 sub-cells): sup W/m <= 2.5965e-4, attained on the cell r in [8.7897, 8.7981] (the lobe next to P; the P-shell [x_*/2, 2 x_*] has the same maximum, 2.5965e-4); multiplier forms sup W (1+u)^{1/2}/m <= 3.8071e-4 and sup W (1+u)^{1/2-k}/m <= 3.3187e-4 (same cell); sup W <= 1.2015e-4; sum of the L2 pieces <= 4.9727e-9. Taylor remainders: eps <= 2.11e-11, A <= 9.3e-15, B <= 1.6e-14. (Raw aggregates in runs/cert_summary.json: sup W/m = 0.000259644550938..., so the earlier printed 2.5964e-4 was an inward
rounding; likewise 3.8070e-4 for 0.000380701159...; corrected 2026-10-22, shift 7.) The pre-fix run with the plain Bernstein bound gave 2.926e-4, with
every per-cell bound at or above the verifier's independent middle-region pass, which gives W/m < 2.91625e-4; the post-fix sub-interval bound is
tighter than both, so the verifier's looser certificate corroborates the calculation but does not independently establish the sharper ceiling
2.5965e-4 (their later exact re-summations of this lane's saved cells are reported in section 8 of FINAL_REPORT.md, not here).
Outer and inner regions and tails: table below (chain4, 22:54Z). R2 (whole plane): ( int_{R^2} |eps~/m|^2 dX/(1+u^2) )^{1/2} <= 6.2899e-4
(6.29e-4; exact decimal ceiling of the Arb upper endpoint 6.28982503521e-4, runs/r2_tails.json 'total_R2_upper_endpoint'). Finite regions: the outward
sum of the raw L2 pieces is <= 3.95619e-7 (exact ceiling 3.95618989085e-7; the three pieces' own ceilings 4.9727e-9 (middle), 3.9065e-7 (outer) and
3.4826e-16 (inner) add up to at most 3.9563e-7, verifier topic 182), i.e. as norms outer <= 6.2502e-4, middle <= 7.0518e-5, inner <= 1.8662e-8. Tails (src/r2_tails.py, runs/r2_tails.json; Arb at 200 bits): on r >= r_T,out the
certificate gives W (1+u)^delta / m <= C_out = 1.75412e-6 for every r there (delta = 1/2 - k, runs/cert_tail.json), and sup_theta |eps~| <= W, so the
outer tail contributes at most 2 pi C_out^2 int_{r_T,out}^inf (1+u)^{-2 delta} r dr/(1+u^2) <= pi C_out^2 L^2 U_T^{-2 delta} / delta <= 6.504e-16
(U_T = r_T,out / L = 1.0774e10; u/(1+u^2) <= 1/u and (1+u)^{-2 delta} <= u^{-2 delta}) to the squared norm; on r <= r_T,in, W/m <= C_in =
2.13842e-6 gives at most pi C_in^2 r_T,in^2 <= 3.819e-20 (the boundaries e^{t0 + 17} and e^{tmin - 5} are formed in Arb from the stored knots, not
taken from the rounded r_T of the tail files; L, r_T, delta > 0). (The weighted measure dX/(1+u^2) has infinite mass outside every disc, so 'sup times
measure' is not an argument for the outer tail; the bound above uses the decay of the weighted tail majorant. The earlier text said 'negligible'
without this computation; corrected 2026-10-22, shift 7. Verifier topic 182 (FINAL 01:29Z) confirmed the conditional tail theorem and the ten scalar
enclosures, and found that version 1 of runs/r2_tails.json printed nearest-rounded endpoint displays (3.818317335e-20, 0.000628982503520) that lie
below the exact upper endpoints; version 2 of src/r2_tails.py prints exact decimal ceilings (3.818317336e-20, 6.28982503521e-4) and the ceilings quoted
here, 6.504e-16, 3.819e-20 and 6.2899e-4, are above them.) R4 (origin): sup W/r^5 <= 1.2562e-3 on the inner cells (at r = 5.155e-5) and <= 1.797
on the inner tail majorant.
R1/R3/R5 (derivatives, K~): section 7.3b; S1: section 7.2.
POST-FIX RESULTS OF chain4 (RIGOROUS; repaired code, regenerated inner/outer Arb data with exponent radii, T_out = 17, T_in = 5;
runs/cert_resid_regions.json, cert_tail.json, cert_tail_d05.json, cert_inner_tail.json; chain4 ended 22:53:54Z):
| region (cells) | sup W/m (divisor) | at r | sup W (1+u)^{1/2}/m | at r | sup W (1+u)^{1/2-k}/m | at r | sum of L2 pieces |
|---|---|---|---|---|---|---|---|
| outer: R0 <= r <= 8.244e+10 = r_T,out (8948) | 9.3189e-5 | 3.343e+04 | 7.3681e-3 | 7.711e+04 | 1.4636e-3 | 5.214e+04 | 3.907e-7 |
| outer tail r >= r_T,out = 8.24401e+10 (termwise majorant) | 1.0649e-9 | - | 1.1053e-4 | - | 1.7542e-6 | - | <= 6.51e-16 (r2_tails, norm^2) |
| inner: r_T,in <= r <= rmin (2632) | 9.1893e-6 | 0.007146 | 9.2024e-6 | 0.007146 | 9.1921e-6 | 0.007146 | 3.483e-16 |
| inner tail r <= r_T,in = 5.15549e-05 (termwise majorant) | 2.139e-6 (W/r^5 <= 1.797) | - | - | - | - | - | <= 3.82e-20 (r2_tails, norm^2) |
Outer-region Taylor remainders: eps <= 1.6e-13, A <= 7.5e-5, B <= 1.4e-4; inner: eps <= 1.2e-19, A <= 2.9e-32, B <= 5.5e-32. Inner R4: sup W/r^5 <= 1.2562e-3 at r = 5.155e-05 (cells) and <= 1.797 on the inner tail. (Earlier versions of this table copied the unweighted inner ceiling 9.1893e-6 into the (1+u)^{1/2} column and printed the
tail-ball midpoints 2.138e-6 / 1.796 instead of their upper endpoints; corrected 2026-10-22, shift 7.)
These agree with and are slightly tighter than the verifier's independent exterior certificate (W/m < 9.4957e-5, weighted-half < 7.738e-3
on r >= 3413) and inner certificate (W/m < 9.3285e-6). The post-fix middle rerun (chain5, sub-interval Bernstein bound) is complete and
is the middle table above (sup W/m <= 2.5965e-4 at the lobe; raw aggregates in runs/cert_summary_all.txt, which prints nearest-rounded values, ceilings in runs/report_tables.md).
Outer and inner regions: the first run (chain1) used Arb boundary values for the inner region in which the mode n = 27 was
wrong (the exponent mu = 2 - 2n + bi + 2 is about 1.1e-12 for n = 27 because the stored bi = 50.000000000001066 is not exactly 50, and the closed-form
primitive cancels catastrophically); the integrator now switches to a convergent series for |lam| max(|a|,|b|) < 1/2 and
the inner/outer data are regenerated (chain4). The outer region was unaffected (exponents far from zero): its pre-fix
bounds read W/m <= 5.6e-6 at R0 decreasing to 3.3e-7 at r = 7.5e7, and W (1+u)^0.5/m up to about 4.7e-3 near r = 2e4
(the far-field Theta_1 mismatch of X3, as predicted); superseded by the post-fix results above.
Tails (pre-fix data, repaired tail code): the termwise majorants at the ends of the Taylor-model regions are crude because
they lose the cancellation between the linear and the convolution terms: outer at r = 7.5e7: W/m <= 0.049 (Taylor cell there:
3.3e-7), weighted (1+u)^0.5: 152; inner at r = 6.3e-4: W/m <= 3.2e-4 (Taylor cell: 1.6e-9), W/r^5 <= 1.8. Hence the final
runs extend the Taylor-model regions to r = 8e10 (T_out = 17) and r = 5e-5 (T_in = 5), where the unweighted tail majorants
fall further; moreover the outer tail now keeps the exact e^{(2k-1) tau} coefficient of every residual mode and bounds only
the remaining terms termwise (src/cert_tail.py): on the pre-fix data at T_out = 10 this gives W/m <= 8.3e-7 (crude 0.049;
Taylor cell 3.3e-7) and, with the SPEC v2 weight (1+u)^0.3206, about 1.4e-4 (2.6e-3 with (1+u)^0.5), so the far tail no
longer dominates. Pre-fix picture of R0 by region (runs/cert_summary_prefix.txt): middle sup W/m 2.93e-4 (weighted 3.74e-4,
r = 8.79); outer sup W/m 9.3e-5 at r = 3.3e4, weighted 1.46e-3 at r = 5.2e4 (the Theta_1 mismatch band of X3); far tail as
above; inner: recomputed by chain4 (table above). This pre-fix picture is HISTORICAL and superseded by the post-fix tables above: the
certified R0 of the trial over the WHOLE PLANE is: sup W/m <= 2.5965e-4 in the divisor form (attained next to P); sup W (1+u)^{1/2}/m <= 7.3681e-3
in the (1+u)^{1/2} multiplier form (attained in the outer region at r = 7.7e4, the far-field Theta_1 mismatch band of X3; the middle region alone gives
3.8071e-4, which an earlier version of this sentence wrongly called the global value); sup W (1+u)^{1/2-k}/m <= 1.4636e-3 in the SPEC v2 multiplier
form (attained in the far band r = 5.2e4; middle region 3.3187e-4); the tail majorants lie below these in every form (outer tail: 1.0649e-9
unweighted, 1.1053e-4 in the (1+u)^{1/2} form (runs/cert_tail_d05.json), 1.7542e-6 in the (1+u)^{1/2-k} form; inner tail 2.139e-6).

### 7.3c Three resolutions (RES; chain2/chain7/chain7d; src/variants_summary.py -> runs/variants_summary.txt, .json) (shift 3; v3 complete 04:09Z; v4 complete 22:14Z, shift 6; v5 complete 2026-10-22T02:23Z, shift 7)
The same certificate pipeline is run on independently fitted variants of the trial: v3 (radial knot spacing h = 0.004, half of the X3 trial's
0.008; 8874 middle sub-cells), v4 (230 angular modes instead of 260, same knots h = 0.008, same R0 = 3413; 7809 sub-cells; chain7d, 18:25Z to
22:14Z under a box load of about 48), v5 (knot scheme 2: R0 = 1468 instead of 3413, 1467 knots; complete 2026-10-22T02:23Z, chain7d), and the
centre-regular N7 (S1 and middle done). RIGOROUS results (this lane's certificate, directed rounding, audit pending) of v3, v4 and v5 against the X3
trial (h = 0.008, M = 260):

| quantity (upper bounds rounded up, interval endpoints outward; the r-range endpoints are approximate locations, not bounds) | X3 trial (h = 0.008, M = 260) | v3 (h = 0.004) | v4 (M = 230) | v5 (knot scheme 2, R0 = 1468) |
|---|---:|---:|---:|---:|
| x_* | 8.600063805157177 +/- 3.0e-13 | 8.600063805157177 +/- 3.0e-13 | 8.60006380515718 +/- 2.7e-13 | 8.600063805157173 +/- 3.0e-13 |
| mu~ - 1 | [-2.25290e-8, -2.25271e-8] | [-2.25290e-8, -2.25271e-8] | [-2.25283e-8, -2.25266e-8] | [-2.25290e-8, -2.25271e-8] |
| g = rho~_y(P) | [29.749490663330, 29.749490663337] | [29.749490663330, 29.749490663337] | [29.749490663337, 29.749490663344] | [29.749490663330, 29.749490663337] |
| w'(P) | [10.150725243807, 10.150725243815] | [10.150725243807, 10.150725243815] | [10.150725243807, 10.150725243814] | [10.150725243807, 10.150725243815] |
| middle cells (approximate r range) | 7809 ([0.0076514, 3413]) | 8874 ([0.0076514, 3413]) | 7809 ([0.0076514, 3413]) | 7279 ([0.0076514, 1468]) |
| middle sup W/m (lobe next to P) | 2.5965e-4 | 2.5965e-4 | 2.5971e-4 | 2.5965e-4 |
| middle sup W (1+u)^{1/2}/m | 3.8071e-4 | 3.8071e-4 | 3.8079e-4 | 3.8071e-4 |
| middle sup W (1+u)^{1/2-k}/m | 3.3187e-4 | 3.3187e-4 | 3.3195e-4 | 3.3187e-4 |
| middle sup W | 1.2015e-4 | 1.2015e-4 | 1.2018e-4 | 1.2015e-4 |
| middle sum of L2 pieces | 4.973e-9 | 4.964e-9 | 5.001e-9 | 5.209e-9 |
| outer cells (approximate r range) | 8948 ([3413, 8.244e+10]) | 8948 ([3413, 8.244e+10]) | 8948 ([3413, 8.244e+10]) | 8948 ([1468, 3.5459e+10]) |
| outer sup W/m | 9.3189e-5 | 9.3188e-5 | 9.3574e-5 | 9.3145e-5 |
| outer sup W (1+u)^{1/2}/m | 7.3681e-3 | 7.3682e-3 | 7.3891e-3 | 7.3713e-3 |
| outer sup W (1+u)^{1/2-k}/m | 1.4636e-3 | 1.4636e-3 | 1.4684e-3 | 1.4640e-3 |
| outer sum of L2 pieces | 3.907e-7 | 3.907e-7 | 3.907e-7 | 3.915e-7 |
| inner cells (approximate r range) | 2632 ([5.1555e-05, 0.0076514]) | 2632 ([5.1555e-05, 0.0076514]) | 2632 ([5.1555e-05, 0.0076514]) | 2632 ([5.1555e-05, 0.0076514]) |
| inner sup W/m | 9.1893e-6 | 5.4351e-6 | 9.1892e-6 | 9.1794e-6 |
| inner sup W (1+u)^{1/2}/m | 9.2024e-6 | 5.4429e-6 | 9.2023e-6 | 9.1925e-6 |
| inner sup W (1+u)^{1/2-k}/m | 9.1921e-6 | 5.4367e-6 | 9.1920e-6 | 9.1822e-6 |
| inner sum of L2 pieces | 3.483e-16 | 6.850e-17 | 3.483e-16 | 3.477e-16 |
| outer tail sup W (1+u)^{1/2-k}/m | 1.755e-6 | 1.756e-6 | 1.759e-6 | 2.703e-6 |
| outer tail sup W/m | 1.065e-9 | 1.066e-9 | 1.068e-9 | 2.151e-9 |
| inner tail sup W/m | 2.139e-6 | 2.139e-6 | 2.139e-6 | 2.139e-6 |
| inner tail sup W/r^5 | 1.797 | 1.797 | 1.797 | 1.797 |

Reading (relative changes computed from the raw aggregates of runs/variants_summary.json, not from the rounded ceilings; every entry of the table is
an upper bound, so a relative change between two entries is a change of the certified bounds, not of the underlying quantities, which the bounds
leave free below them; the r-range endpoints of the table are approximate locations, verifier topic 201): the radial refinement v3
(knot spacing halved) changes the middle sup bounds (W/m, both multiplier forms, sup W) by +7e-8 relative, the outer sup W/m by -1.0e-5 relative and
the outer weighted sup by +8e-6, while the integral bounds change by -0.18 percent (middle L2) and +0.007 percent (outer L2); the angular truncation
v4 (230 modes instead of the base trial's 260; X3 itself is not a 260-mode trigonometric polynomial) changes the middle sup bounds by +0.022 percent
(2.59703e-4 against 2.59645e-4), the middle L2 by +0.57 percent, the outer sup W/m by +0.41 percent (9.35736e-5 against 9.31886e-5), the outer
weighted sup by +0.32 percent and the outer L2 by +0.013 percent. Point scalars: x_* and w'(P) agree to 13 digits for v3 and v4 (midpoint changes
<= 6e-13); for v4 the midpoint of mu~ - 1 moves by +5.7e-13 (the certified intervals overlap, so this is a floating midpoint difference, not an
enclosed difference of exact scalars) and the midpoint of g by +7.0e-12 (the raw v4 and base intervals for g in runs/variants_summary.json are
disjoint, although their rounded displays touch at 29.749490663337: g is a property of the fitted
trial, which v4 changes). So the certified residual level of the three trials agrees to 0.02 percent (middle) and 0.4 percent (outer): it is a
property of the re-represented X3 at this fit quality (the floating fit error is 1e-9 relative in the sampled sense of section 4), not of one fit;
this is floating evidence of fit stability, and the rigorous statements remain statements about each specified trial. The inner region (r < rmin,
where the trials' centre expansions differ) is smaller for v3 (-41 percent) and unchanged for v4 (-0.001 percent). v5 (knot scheme 2, R0 = 1468 instead of 3413, 1467 knots; collected 2026-10-22T02:24Z): the middle sup bounds equal the base trial's to 5 digits (raw relative
changes -4.0e-7 for sup W/m and for the (1+u)^{1/2} form, i.e. -4.0e-5 percent); the middle L2 pieces are +4.7 percent larger although the middle region is shorter
([rmin, 1468] against [rmin, 3413], 7279 against 7809 cells); this is a change of the certified UPPER BOUNDS of the integrals (exact relative change
of the bounds 4.7433 percent, verifier topic 201), which permits equal or smaller actual integrals and so does not show that the integral itself moved;
the sup bounds are unchanged; the outer region is [1468, r_T,out] with r_T,out = 1468 e^17 = 3.5459e10 (T_out = 17 from t0 = log 1468; 8948 cells; its sup W/m
9.3145e-5 against the base trial's 9.3189e-5 on [3413, 8.244e10], both attained at r = 3.35e4, the Theta_1 mismatch band; its (1+u)^{1/2} form 7.3713e-3
against 7.3681e-3 and its (1+u)^{1/2-k} form 1.4640e-3 against 1.4636e-3; outer L2 3.915e-7 against 3.9065e-7), the inner region changes by -0.11 percent
(9.1794e-6 against 9.1893e-6), and the tail majorants are 2.703e-6 (outer, (1+u)^{1/2-k} form) and 2.151e-9 (outer, unweighted) against the base trial's
1.7542e-6 and 1.0649e-9 (larger because v5's tail starts at 3.5e10 instead of 8.2e10) and 2.139e-6 (inner, = base), W/r^5 <= 1.797 (= base); point scalars: x_* midpoint -3.6e-15, mu~ - 1 midpoint
-2.0e-14, g midpoint +3.6e-15, w'(P) midpoint +2.0e-14 (all certified intervals overlap the base trial's). R2 for v5 (src/r2_tails.py v5_R0knot2; exact ceiling
of the Arb upper endpoint 6.29776188135e-4): whole plane <= 6.2978e-4 against the base trial's 6.2899e-4 (+0.13 percent). N7 has S1 and middle sup bounds equal to the base trial's to the
printed digits under the same weight evaluation (runs/variants_summary.json; the 3.8079e-4 of 7.5 is the coarser per-cell field evaluation, which
gives the same value for the base trial). Per-variant files: runs/cert_resid_middle_v4_M230.json, scalars_v4_M230.json,
cert_resid_regions_v4_M230.json, cert_tail_v4_M230{,_d05}.json, cert_inner_tail_v4_M230.json (the 291 MB Green file of v4 was deleted after use).

## 7.4 C2 (floating point) status: finite sections of L, F- and free-tail column sets (evidence only)
Code: src/lin_assembly.py + src/lin_fast.py (fast assembly of L on single-mode exponential-polynomial basis functions; tested by the
exact identity L rho~ = 2 eps~ + rho~ - X.grad rho~/3 to 1e-12 and against the earlier finite_section2 Green data to 1e-16),
src/c2_fminus.py (lead's design, NOTES 16:58Z/17:31Z): h = x^2 y sum_{m<Mh} b_m(t) cos(2m theta) with b_m in {inner powers e^{2j tau'},
j = 1..7 (+ the constant for m = 0: the J direction); degree-7 B-splines on every stride-th knot; outer power laws with growth < k},
plus the scalar columns KP = x^2 y chi(t) t e^{(k-3)(t-t0)} Theta_0~ (the k'-derivative at k' = k of the family x^2 y chi e^{(k'-3) t - (k-3) t0} Theta_0~,
stored coefficients held fixed) and TAU = x^2 y chi e^{(k-3)(t-t0)} (Theta_0~ cos 2 theta)_{m < M} (the product projected onto the trial's M = 260 modes, saved as
the vector Bm; the omitted coefficient A0_{M-1}/2 is -3.9e-19), chi = the sum of the last 10 B-splines of the trial (a C^6 cutoff: 0 well inside R0, 1 near and beyond R0; definitions in 7.0). Free section = F- plus the pure tails per mode.
Rows: residual modes N < Mout at 21 inner radii, ppc points per coarse cell, 40 outer radii and (current code) the midpoints of the last ten fine-knot
intervals (ten cutoff radii, so 170 / 467 / 124 radii for the three configurations below; the archived table used the earlier grid without them,
160 / 457 / 114), weighted by (1+u)^{1/2}/m(r); ordinary single-mode columns and pure tails weighted by the sup proxy max over the finite collocation grid t_eval of |b| e^{3t}/m, times (1 + (2m)^2),
the scalar columns KP and TAU by the maximum over t_eval of their radial factor times sum_m |A0_m| resp. sum_m |B_m| (no angular factor; the unrestricted
radial supremum of KP would be infinite, its weighted radial factor growing like |t|).
Results (runs/pdisc/c2f_*.json):
| section | columns | rows | sigma_max | sigma_1 (direction) | count sigma < 1e-6 sigma_max (dominant kinds) |
|---|---|---|---|---|---|
| M16 s16 ppc1 F- | 1955 | 160 x 24 | 1.49e4 | 4.6e-13 (J: 0.71 J + 0.29 mode-0 splines) | 456 (sp 308, out 83, in 64, J 1) |
| M16 s16 ppc1 free | 1971 | 160 x 24 | 1.49e4 | same | 471 (+ tail 8); tail-dominant sigmas 4.1e-4, 3.1e-5, 6.7e-6, 1.2e-7 |
| M16 s16 ppc4 F- | 1955 | 457 x 40 | 9.7e3 | 4.6e-13 (J) | 220 (sp 75, out 81, in 64) |
| M16 s16 ppc4 free | 1971 | 457 x 40 | 9.7e3 | same | 222 (+ tail 1: sigma 5.3e-3) |
| M8 s30 ppc1 F- / free | 611 / 619 | 114 x 16 | 2.9e3 | 1.2e-13 (J) | 90 / 98 |
Reading. (a) sigma_1 ~ 1e-13 is the J direction: J minus the sum of the mode-0 splines is the constant x^2 y on r < rmin alone, whose
image is O(r^5) because (3c_l - 1) x^2 y + U~.grad(x^2 y) = 0 at the origin (the normalization identity), with a large sup-proxy
weight: the unnormalized section has the J near-kernel that SPEC 3.6 describes. (b) The remaining near-null directions are basis
conditioning, not operator properties: the inner powers e^{2j tau'} (all concentrated at tau' = 0) and the 9 outer power laws per
mode are near-collinear in the sampled, sup-weighted matrix (their counts, 64 and 81, do not change with the row density), while
the spline-dominated count falls from 308 to 75 when the collocation density is quadrupled (under-sampling). (c) Tails: with one
point per cell the free section adds one singular value below 1e-6 sigma_max per tail mode (8 of 8; 16 of 16 at M16), as the
lead's formal-kernel picture predicts, but with dense collocation only one tail-dominated near-null direction remains
(sigma = 5.3e-3 = 5e-7 sigma_max for 16 tails), so the prediction is NOT confirmed at this resolution; the sections would need a
well-conditioned (orthonormalized, X-norm-weighted) column basis before the tail question can be read off the spectrum. (d) The
ell(Phi) least-squares test (dk, dtau for tail increments) is not meaningful at this conditioning (values of order 1e5 with rcond
1e-6); not reported as evidence. The production sections M24/s8 and M32/s8 (ppc 1) completed in shift 2 (chainC2, 2026-10-20 21:46Z, WORKLOG) with
the same pattern (M32/s8: 7011 F- columns, 2005 singular values below 1e-6 sigma_max, kinds sp 1704 / out 161 / in 139 / J 1; in the free section 15
of 32 tail columns gave tail-dominated near-null directions, sigma 6e-8 to 1.2e-6); the loose JSON outputs and logs were removed from runs/pdisc when the
sup-weighted raw basis was abandoned in favour of the Gram-orthonormalized sections of 7.4b, but they survive in the archive runs/pdisc.tgz
(c2f_M24_s8.json, c2f_M32_s8.json, their logs, chainC2.sh). ell(Phi) above denotes the weighted least-squares
solution (numpy lstsq, rcond 1e-6, on the sup-weighted columns) of L(chi r^k Phi + g + dk KP + dtau TAU) = 0 at the section's rows over g in the span
of the ordinary function columns (inner powers, splines, outer power laws, J; KP and TAU enter only through the two scalars dk, dtau), for a prescribed
leading-tail increment: the implemented increments are h_Phi = x^2 y chi(t) e^{(k-3)(t-t0)} Phi_b(theta) with Phi_b in {cos 0, cos 2 theta, cos 4 theta,
cos 6 theta, Theta_0~ restricted to m < Mh}, i.e. 'chi r^k Phi' with Phi = e^{(3-k) t0} cos^2 theta sin theta Phi_b (src/c2_fminus.py); it returns
(dk, dtau) and the relative residual.

### 7.4b C2 with a well-conditioned column basis orthonormalized in the broken-gradient H1m Gram (shift 3-5; src/c2_gram.py v2, src/c2_gram2.py v3; FLOATING, evidence only; COMPLETE, final status in (vii))
Method (after the astra review notes/astra_c2gram1_answer.md): the raw finite section of c2_fminus.py (columns h_c = x^2 y f_c(t) a_c(theta):
inner powers e^{2j tau'}, coarse degree-7 B-splines, outer power laws, J = x^2 y on r < R0, the scalar tail columns KP, TAU, and the free tails;
rows = residual modes N < Mout at collocation radii incl. 10 inside the cutoff transition, weight (1+u)^{1/2}/m(r)) is re-expressed in an
basis orthonormalized in the Gram of the inner product <h, g>_X = int (h g + r^2 grad h . grad g) m(r)^{-2} (1 + u^2)^{-3/2} dX with m the background scale (the
encoded column functions are NOT exactly in the H1m space across the piece joins, verifier topics 130/131, so every Gram value, 'X-orthonormal' basis,
'X-orthogonal projection' and 'X-distance' in 7.4b and 7.4c is a BROKEN-GRADIENT (piecewise-gradient) quantity; topic 132 bounds the single-column
repair by a norm ratio below 2.6e-14, and no transfer bound to the repaired space is claimed for spectra or projections; the
same relative normalization as the rows; the separable Gram uses exact angular matrices and composite Gauss-Legendre radial quadrature with
every piece endpoint as a breakpoint, checked against a 48-point rule to 7e-15); columns equilibrated to unit X-norm; C^0 join matching at
tmin and t0 imposed per mode through the constraint nullspace (32 constraints at M16, all independent; the constraint rank is determined by the
relative singular-value test sigma_i > 1e-10 sigma_max of the constraint matrix); eigen-cut: after the restriction to the constraint nullspace and
the equilibration, the eigenvectors of the Gram with lambda_i > 1e-10 lambda_max (RELATIVE threshold) are retained, and 'retained' is the dimension
of their span (they are combinations of columns, not selected original columns); the discarded directions are near-dependent combinations within the Hilbert-matrix-like inner-power and
outer-power families); whitening error checked with the refined quadrature (4e-7); then the SVD of the row-weighted section. Reference
directions for the smallest singular vectors (cos^2 of the X-angle, pseudo-inverse projections): the section's J column, J_inner = x^2 y
1_{t < tmin} (the inner scaling direction, a function outside the section), the free tails, KP/TAU, the kinds and the modes; principal cosines
of the 5 smallest directions against the tail span and J_inner.

First production result (M16/s16/Mout40, ppc 2: 10760 rows, 1955 columns, 1866 retained; runs/c2/c2gram_M16_s16_p2_H1m_NJ0.json):
smallest singular values 0.1208, 0.1441, 0.1516, 0.1650, 0.1827 (F-), 0.1198, 0.1435, 0.1511, 0.1632, 0.1807 (free); quantiles 1% 0.41,
5% 1.18, 25% 6.4, median 25, sigma_max 4.0e4. No direction is near-null: the smallest directions have cos^2 with J_code 3e-11, with J_inner 0,
with the tail span 0, with KP/TAU 0, with the spline span 0.02 (mixed directions); principal cosines of the 5 smallest against the tail span
0.0006 and against J_inner 0.0018; removing J changes nothing (the J column is not a near-kernel direction in this norm: its X-norm is 5.4e9,
J_inner's 5.9). The ell(Phi) least squares does not solve the homogeneous equation (relative residuals 0.08-0.57). Reading (preliminary): the
J near-kernel and the tail near-null directions of 7.4 were artefacts of the sup-weighted raw basis (functions with tiny integral norm but
O(1) sup weight); in the background-relative H^1 norm with the broken-gradient Gram-orthonormalized basis the section is bounded below by about 0.12 at this row density.
Variants at the same row density (ppc 2): with C^1 join matching (NJ = 1; 1847 retained) the smallest singular values are 0.1164, 0.1380,
0.1437, 0.1591, 0.1767 (F-), sigma_max 1.36e4, again no reference-direction content (principal cosines vs tails 0.001, vs J_inner 0.0008); with
the plain face-weighted L^2 inner product (L2y: |y|^{-2} (1+u^2)^{-1.129}, no 1/m^2 normalization) the smallest value is 0.038 against
sigma_max 5.2e13, the spread reflecting the mismatch between the e^{6t} measure and the 1/m row weight rather than the operator (so only the
H1m numbers are read). Per-resolution table (chain8d, started 10:55Z, complete; final table below; FLOATING, evidence only; the column sigma_min/sqrt(rows)
normalizes the discrete least-squares functional by the number of collocation rows, since the row weights carry no quadrature measure, so that
sections of different row density are comparable; the cos^2 columns are the squared X-cosines of the smallest singular directions with the
reference directions, as requested for FINAL_REPORT section 10 next step 1):
| section (M16/s16/Mout40 unless noted) | rows | Gram / joins | retained | 3 smallest singular values (F-) | sigma_min/sqrt(rows) | largest | cos^2 of the 5 smallest directions with the J column (max) | with the tail span (max) | with J_inner, KP/TAU (max) | sigma_min (free tails) |
|---|---:|---|---:|---|---:|---:|---:|---:|---|---:|
| ppc 2 (M16_s16_p2) | 10760 | H1m / NJ0 | 1866 | 0.1208, 0.1441, 0.1516 | 1.165e-03 | 4.01e+04 | 7.3e-11 | 1.6e-07 | 1.6e-06, 6.2e-10 | 0.1198 |
| ppc 2 (M16_s16_p2) | 10760 | H1m / NJ1 | 1847 | 0.1164, 0.1380, 0.1437 | 1.122e-03 | 1.36e+04 | 7.7e-09 | 4.1e-07 | 3.2e-07, 1.8e-09 | 0.1151 |
| ppc 2 (M16_s16_p2) | 10760 | L2y / NJ0 | 1859 | 0.0383, 0.2259, 0.3799 | 3.692e-04 | 5.22e+13 | 5.3e-05 | 2.6e-07 | 1.9e-18, 7.3e-08 | 0.0382 |
| ppc 4 (M16_s16_p4) | 18680 | H1m / NJ0 | 1866 | 0.1698, 0.2028, 0.2131 | 1.242e-03 | 4.10e+04 | 1.7e-10 | 6.1e-07 | 1.6e-06, 2.4e-09 | 0.1667 |
| ppc 4 (M16_s16_p4) | 18680 | H1m / NJ1 | 1847 | 0.1582, 0.1869, 0.1939 | 1.158e-03 | 1.66e+04 | 2.9e-08 | 1.2e-06 | 5.8e-07, 6.2e-09 | 0.1546 |
| ppc 4 (M16_s16_p4) | 18680 | L2y / NJ0 | 1859 | 0.0542, 0.3077, 0.5161 | 3.969e-04 | 5.36e+13 | 5.6e-05 | 2.7e-07 | 1.9e-18, 6.8e-08 | 0.0542 |
| ppc 6 (M16_s16_p6) | 26600 | H1m / NJ0 | 1866 | 0.2067, 0.2471, 0.2594 | 1.268e-03 | 4.27e+04 | 3.1e-10 | 1.3e-06 | 1.6e-06, 5.4e-09 | 0.2015 |
| ppc 6 (M16_s16_p6) | 26600 | H1m / NJ1 | 1847 | 0.1893, 0.2222, 0.2318 | 1.161e-03 | 1.99e+04 | 5.6e-08 | 1.9e-06 | 7.7e-07, 1.1e-08 | 0.1837 |
| ppc 6 (M16_s16_p6) | 26600 | L2y / NJ0 | 1859 | 0.0664, 0.3701, 0.6204 | 4.072e-04 | 5.59e+13 | 5.7e-05 | 2.7e-07 | 1.8e-18, 6.7e-08 | 0.0664 |
| M24/s8/Mout32 ppc 4 (M24_s8_p4) | 27360 | H1m / NJ0 | 5126 | 0.1492, 0.1797, 0.1851 | 9.018e-04 | 4.28e+04 | 2.3e-10 | 2.6e-06 | 2.2e-06, 2.7e-10 | 0.1459 |
CORRECTION (14:50Z, found by the version-3 run): every version-2 'NJ1' row above is MIS-SPECIFIED: in equilibrated coordinates the C^0 constraint
rows at the outer join t0 (r = R0 = 3413) have norms 9e-11 to 1e-9 while the C^1 rows at tmin have norms up to 35, so the relative rank cut (1e-10
of the largest singular value of the unnormalized constraint matrix) dropped all C^0 rows at t0 (constraint rank 48 of 64 at M16, 72 of 96 at M24;
in the NJ0 runs the same rows, norm 9.0e-11 against the cut 8.8e-11, survived, so the NJ0 rows are right). The version-2 'NJ1' sections therefore solved an erroneous truncated constraint system in which value jumps at R0 were permitted (the truncation drops singular directions, not exactly rows, and the derivative rows match the radial coefficient f', so [d_t h] = 3[h] remains when f jumps: the old space is neither C^1 nor derivative-matched at the outer join; such inputs are nonconforming and the piecewise assembler omits their jump distributions; referee astra/gram4 item 4). Read the old numbers as that. Version 3 normalizes the constraint rows before the rank
decision (astra/gram3 item 6) and imposes all of them: at M24/s8 ppc 4 the properly constrained C^1 section (96 constraints, 5078 retained) has
0.1499, 0.1798, 0.1851 against 0.1492, 0.1797, 0.1851 for C^0 (so the lowest L2 values are insensitive to the additional joins, within 0.6 percent), not the 0.1279 of the mis-specified run; at M16/s16 ppc 4 the properly constrained C^1 section gives 0.1708 (C^0 0.1698; mis-specified 0.1582).
Eigen-cut independence (ppc 4, H1m/NJ0): with the Gram threshold 1e-12 (1887 retained) or 1e-8 (1837 retained) instead of 1e-10 (1866) the
three smallest values are 0.1698/0.2027/0.2130 and 0.1699/0.2028/0.2131 (whitening errors 2.6e-5 and 2.4e-8), so the retained dimension does
not affect the small singular values.
Reading (13:05Z; M16/s16 at ppc 2/4/6 complete; M24/s8/Mout32 at ppc 4: the H1m/NJ0 row is in, the NJ1 and L2y rows are now in table 1 (historical status line; chain8d wrote
them, about 14:15Z and 15:10Z):
(i) Row refinement at fixed section (M16/s16, H1m/NJ0): sigma_min grows 0.1208 -> 0.1698 -> 0.2067 (factor 1.71) while sigma_max grows by
1.06 (4.01e4 -> 4.27e4); per row (sigma_min/sqrt(rows)) 1.165e-3 -> 1.242e-3 -> 1.268e-3, stable to 8.8 percent: the per-row value stabilizes over the three row densities at fixed section (sampling stabilization, not a proof of convergence of the functional), and the smallest value does not move downward under row refinement. The version-2 'NJ1' rows
(0.1164 -> 0.1582 -> 0.1893; mis-specified, see the correction under the table: value jumps at R0 allowed) and the L2y rows (0.0383 -> 0.0542 ->
0.0664) share only the growth of sigma_min with the row count (the L2y spectrum is a different quadratic form, see above). The J cos^2 bound 3.2e-10 holds for the C^0 rows (M16 ppc 2/4/6 and M24; version-2 'NJ1' rows 7.7e-9 / 2.9e-8 / 5.6e-8; L2y rows 5.3e-5 to 5.7e-5); over the M16 H1m rows the maxima are J 5.6e-8, tail span 1.9e-6, J_inner 1.6e-6 (including M24: tail span 4.2e-6, J_inner 2.2e-6).
(ii) Section refinement at the same four collocation points per cell (the lead's size test): M16/s16/Mout40 (1955 F- columns = 1953 function columns + KP + TAU, 32 constraints, 1866
retained, 18680 rows) -> M24/s8/Mout32 (5259 F- columns = 5257 function columns + KP + TAU, 48 constraints, 5211 free, 5126 retained, 27360 rows), H1m/NJ0: the three smallest values go 0.1698,
0.2028, 0.2131 -> 0.1492, 0.1797, 0.1851 (minus 12 percent), per row 1.242e-3 -> 9.018e-4 (minus 27 percent), while sigma_max goes 4.10e4 ->
4.28e4 and the bulk of the spectrum is stable per row (1 percent quantile 0.567 -> 0.730, i.e. 4.15e-3 -> 4.41e-3 per row; median 34.9 -> 41.4;
the fraction of singular values below 1e-3 sigma_max 52 -> 51 percent). With the version-2 'NJ1' constraint set (mis-specified: C^0 at t0
dropped, see the correction under the table; rank 72, 5095 retained) the same comparison reads 0.1582, 0.1869, 0.1939 -> 0.1279, 0.1472, 0.1649
(minus 19 percent), per row 1.158e-3 -> 7.735e-4 (minus 33 percent), sigma_max 1.66e4 -> 2.09e4; cos^2 of the five smallest directions with J
<= 3.1e-8, tails <= 4.2e-6, J_inner <= 1.3e-6, KP/TAU <= 2.6e-9 (runs/c2/c2gram_M24_s8_p4_H1m_NJ1.json). The properly constrained C^1 section (version 3, all 96 constraints) gives 0.1499, 0.1798, 0.1851 at M24 (within 1 percent of C^0); its M16 counterpart is 0.1708, 0.2029, 0.2131 (C^0 0.1698). The L2y variant (not read, see above: the e^{6t} measure against the 1/m row weight) goes 0.0542,
0.3077, 0.5161 -> 0.0072, 0.0495, 0.1334 (5115 retained; sigma_max 5.36e13 -> 6.89e13; per row 3.969e-4 -> 4.365e-5, a factor 9; J cos^2 4.9e-5,
tails 2.1e-7; runs/c2/c2gram_M24_s8_p4_L2y_NJ0.json). So under section refinement the smallest singular value DOES move downward, for the C^0
sections, for the (mis-specified) version-2 C^1 sections and for the L2y form, and with two sizes the test gives no stable lower bound. (chain8d
complete 14:08Z.) Three effects are mixed in this comparison: the nominal column spaces are nested (the stride-16 B-spline space lies in the stride-8 one, modes below 16 in modes below 24), so for exact norms the infimum over the larger space could not be larger, but the retained spaces (separate equilibration, constraint nullspaces and eigen-cuts) and the discrete row functionals differ, so this monotonicity is not asserted for the printed pair; the image is
observed on fewer modes (Mout 32 against 40), which by itself can only lower the projected residual; and the row density per retained column
differs (10.0 against 5.3). The intermediate sections M16/s8/Mout40, M24/s16/Mout40 and M24/s16/Mout32 at ppc 4 (chain8f) separate them.
(iii) Reference-direction content of the five smallest singular vectors at M24 (H1m/NJ0): cos^2 with the J column <= 2.3e-10, with the tail span
<= 2.6e-6, with J_inner <= 2.2e-6, with KP/TAU <= 2.7e-10 (as at M16); principal cosines of the five-smallest subspace against the tail span
<= 2.1e-3, against J 2.5e-5, against J_inner 1.9e-3. Nothing aligned with the normalization, tail or scalar directions appears. (The version-2 cos^2 with the
multi-column spans 'kinds' and 'modes', e.g. spline span 0.007 to 0.20 and single-mode spans below 0.005, used an unequilibrated pseudo-inverse of
ill-conditioned sub-Grams and are NOT reliable (astra/gram3, item 6): on the fixture the equilibrated projection gives spline-span cos^2 1.00
where version 2 gave 0.2 to 0.5. Version 3 recomputes them with equilibration; the single-column and tail-span values above are unaffected.) The ell(Phi) least squares again does not solve the homogeneous equation (relative residuals
0.03 to 0.46).
(iv) What this functional measures (and why a decrease of its smallest value under refinement is expected; an expectation, not a proved statement). Here L is the FULL linearization L h = V.grad h - h + (U[h] + c[h] X).grad rho~ with c[h] = psi[h]_xy(0)/3 (the assembler src/lin_assembly.py includes the rank-one scaling term; c[h] is not constrained; referee astra/gram4). The columns are normalized in an H1-type norm X (h and r grad h, weight m^-2 (1+u^2)^-3/2) while the rows are collocation values of L h with the weight (1+u)^{1/2}/m of the SPEC residual norm: no
derivative and no quadrature measure (a discrete proxy of a weighted sup norm of L h; the per-row normalization sigma_min/sqrt(rows) compares row
densities but still depends on the distribution of the collocation radii and on Mout). The smallest singular value therefore estimates the infimum
of ||L h||_{Y-proxy}/||h||_X over the section, an inverse that GAINS one derivative. A first-order transport operator has no such inverse: for
h_n = a cos(n phi) with phi constant along the characteristics, V.grad h_n = (V.grad a) cos(n phi) has an O(1) L2 norm while ||h_n||_X = O(n); the
order-zero nonlocal term U[h].grad rho~ does not change this count (external referee astra/gram3, item 1). Hence a decrease of sigma_min with the
resolution is expected whatever L does at low frequency; the version-2 functional can test only the low-frequency directions (J, tails, KP/TAU,
center) and the convergence in the row density, it cannot certify a lower bound, and its decrease is not evidence of a kernel. Version 3 of the
code (src/c2_gram2.py; chains 8e/8f) adds (a) an H1-type row functional (value rows times sqrt(1 + (2N+1)^2) for the angular derivative plus
radial finite differences between consecutive collocation radii, run with C^1 joins so that L h is continuous across the external joins; the spectrum from a streaming QR factorization, exact to the printed digits; the normal-matrix route is kept as an option), with one derivative on both sides, (b) three continuous
reference functions (x^2 y f(t) with f = 1 for t <= ta, f = 1 - S((t - ta)/(tb - ta)) on [ta, tb], f = 0 for t >= tb, S(s) = 126 s^5 - 420 s^6 +
540 s^7 - 315 s^8 + 70 s^9 the C^4 degree-9 step: ref_J with (ta, tb) = (t0 - 1, t0), the continuous analogue of the J column; ref_Jin with
(tmin - 1, tmin), the analogue of J_inner; ref_wide with (tmin, t0), decaying across the whole band; later ref_wide16 with (t0 - 16, t0), the exactly
representable replacement of ref_wide) with their
H1m norms, the cos^2 of the smallest directions with them and their cos^2 with the retained space, (c) the saved smallest singular vectors with
their radial X-energy profile (src/c2_vec_profile.py). Their results are in (vi) and (vii) below (tables runs/c2/c2gram2_table.md,
c2gram2_rowsH1_table.md).
(v) Caveats (verifier topics 127 to 132; lead 12:34Z). The J column and J_inner jump at a circle and are not in the H1m space, so their cos^2
values above are correlations of piecewise gradients, not X-angles; the central coefficient a(0) is unbounded in H1m (h_eps = x^2 y (1 -
r^2/eps^2)_+^6 has a(0) = 1 and H1m norm below L^3 eps), so this Gram cannot test the center direction by norm control; the saved spline pieces
have value jumps of order 1e-20 at interior piece endpoints (dyadic rounding of the stored coefficients, topic 130), so the encoded columns are
not exactly in H1m and every H1m value in this section is a piecewise-gradient Gram value; the exact continuous (C^0) repair of the pieces has broken-energy norm ratio E_b(h_rep - h)/E_b(h) below 8.5e-15 (M16) and 2.6e-14 (M24) per
column (topic 132; a norm ratio, not a bound on the squared energy), and an exact C^{2,1} repair exists with the same ratio below 3.4e-14 (topic
136); these are far below the quadrature check of the whitening (3e-7), these are per-column statements; coefficient amplification in combinations and the image norms of the repairs are unchecked, so the spectra of a repaired section are not asserted to coincide with the printed ones (no transfer bound is claimed). For the version-3 H1-type rows the verifier's topic 135 (L h is locally H1 iff EVERY radial first-derivative trace of h agrees, internal spline joins included) means that the columns AS ENCODED are not in the domain of the H1-row functional as exact functions (the H1 rows have a rigorous reading only on columns with exactly matching first derivatives, e.g. the verifier's C^2 repair of topic 136); the effect of the rounding-level internal derivative jumps of the saved pieces on the finite-difference rows is not quantified here (verifier topic 140: a scalar jump of 1e-14 can give a model term of order 1e-7, and the 2.5e-14 figure of topic 135 concerns the verifier's exact C^0 repairs, not the saved pieces), while the external joins are made C^1 explicitly (NJ1). Topic 133: the Gram matrices of the repaired columns differ from the broken originals by less than 2.31e-10 in spectral norm (a relative transfer to the spectrum would need a certified lower eigenvalue bound, which nobody has). Topic 134 (encoding of the continuous references): ref_J and ref_Jin have exact binary64 step coefficients and are exactly C^4 and in X; ref_wide (window t0 - tmin = 13.008) has rounded coefficients and an encoded value of about 1.2e-13 at its outer end, so it is not exactly in X and its cos^2 values are broken-energy correlations; the exact replacement ref_wide16 (window [t0 - 16, t0], dyadic width, exact coefficients) is included from 16:50Z on (chain8f2 sections). Even a stable plateau of finite-section values would not prove a continuous lower bound or surjectivity, and a
decreasing sequence would not prove a kernel: the sections restrict the trial space (which raises the infimum) and observe the image on N < Mout
modes only (which lowers it); the finite numbers supply candidate directions and consistency checks, nothing more (astra/gram3, item 5).
FINAL_REPORT draws no conclusion from the C2 sections (lead 12:34Z).
(vi) Version-3 results (src/c2_gram2.py after the referee round astra/gram3 and the verifier's topics 135/136; design and reading rules fixed in
advance in notes/C2_v3_design.md; chains 8e/8f; FLOATING; tables runs/c2/c2gram2_table.md and c2gram2_rowsH1_table.md, vector profiles
runs/c2/profiles.txt, all regenerated by runs/collect_v3.sh). First output, M24/s8/Mout32 ppc 4, L2 rows, C^0 joins (14:33Z;
runs/c2/c2gram2_M24_s8_p4_H1m_NJ0.json, _vec.npz):
- Consistency: the streaming-QR spectrum reproduces the version-2 SVD values to all printed digits (0.149169, 0.179694, 0.185054; join residual of
  the retained basis 1.4e-12; whitening error 2.8e-7).
- Continuous references (X-norms ref_J 1.428e9, ref_Jin 3.129, ref_wide 6.099e5; ref_J and ref_Jin exactly C^4 and in X, ref_wide as encoded has a value jump of about 1.2e-13 at its outer end, verifier topic 134, so its numbers are broken-energy correlations): their squared cosines with the RETAINED constrained space are 1.0000, 0.9297, 1.0000 (floating correlations in the broken-energy form, not containment; the raw F- span gives the same), and the cos^2 of the five smallest singular
  directions with them is at most 9.0e-10, 1.3e-8, 4.3e-7 (principal cosines of the five-smallest subspace 4.8e-5, 1.4e-4, 7.9e-4). So the small singular values are not along the NAMED reference directions (ref_Jin is represented to 93 percent of its squared norm, i.e. 26.5 percent relative distance; the referee's audit of the saved vectors gives, for the joint three-dimensional span of the references, a largest squared principal cosine with the five-smallest subspace below 0.002 in all six L2/H1/H1q runs, so linear combinations of the three are excluded as well); three references do not exhaust the normalization mechanisms, and a(0) is not controlled by the H1m norm (topic 127).
- Localization (X-energy of the saved vectors in t = log r): the smallest direction has its energy median at r = 4.38 (10 to 90 percent between
  1.30 and 9.21; 45 percent in [4, 8)), the second at r = 7.08 (3.93 to 16.6), the third at r = 11.9 (8.81 to 22.3; 69 percent in [8, 16)); all five are overwhelmingly concentrated in the spline span (squared projection 0.99999, relative distance about 2e-3; inner-power and outer-power spans 0.000) and spread over many angular modes. So the weakest tested directions carry most of their X-energy at intermediate radii (r between 1 and 22), a range overlapping the source-radius scale, not at the joins, the cutoff transition, the centre or the far field. Radial shells do not locate them at the point P, and the mechanism is unresolved (astra/gram4 item 2): candidates are the degenerate transport at the source, the derivative-gain obstruction (for the L2 rows), and the row weighting itself, whose ratio to the X measure, w(t)^2/q(t) = (1+u)(1+u^2)^{3/2}/(L^2 u^2), has its minimum at u = 1, r = L = 7.65, so that these weighted functionals favour packets near that radius for any operator. Second output (14:48Z; C^1 joins, all 96 constraints, 5078 retained; runs/c2/c2gram2_M24_s8_p4_H1m_NJ1.json): 0.149878, 0.179765,
0.185069 (within 1 percent of the C^0 values; the mis-specified version-2 'NJ1' run gave 0.1279, see the correction under the table), the same
reference content (cos^2 <= 9.2e-10 / 9.4e-8 / 4.3e-7, retained-space cos^2 1.0000 / 0.9297 / 1.0000) and the same localization (energy medians
4.41, 7.08, 11.9). Third output (15:06Z; H1-type rows, C^1 joins, 54688 rows = 27360 value rows (weight x sqrt(1 + (2N+1)^2)) + 27328 radial
finite-difference rows; runs/c2/c2gram2_M24_s8_p4_H1m_NJ1_rowsH1.json; 1102 s): five smallest 3.0932, 4.0289, 4.3712, 5.2318, 5.7141; largest
4.240e6 (ratio 7.3e-7; quantiles 1 percent 26, median 1.63e3); cos^2 of the five smallest directions with J 2.4e-6, tails 1.8e-6, J_inner 2.1e-6,
KP/TAU 9.3e-7, ref_J 7.5e-6, ref_Jin 1.2e-7, ref_wide 8.6e-4. Localization: energy medians r = 2.78 (10 to 90 percent in [1.07, 11.1]), 5.96
([3.69, 13.4]), 9.97 ([7.13, 18.2]); the smallest direction has a substantial m = 0 component (squared projection 0.86 onto the m = 0 column span; the family Phi_m = cos^2 theta sin theta cos 2m theta is not orthogonal, so truncation energies are not fractions and can exceed one; m = 0 means the angular shape (sin theta + sin 3 theta)/4 times a radial spline profile between r = 1 and 11, not an axisymmetric function); in orthogonal sine harmonics the smallest H1 direction has 0.8687 of its X-energy in N = 0, 1 (verifier item 149 from the saved profile; the m = 0 column-span squared projection 0.8627 is below it, as it must be since Phi_0 lies in span{sin theta, sin 3 theta}), whereas other weak directions are not low-frequency (the third M24 L2-row direction has about 73 percent of its energy in harmonics N >= 16; referee audit astra/gram4, item 1). So with one derivative on both sides the finite section is still weakest at intermediate radii, with no content along the named references. Whether this H1-type smallest value is stable under the section
refinement is the question for the intermediate sections (chain8f; the quadrature-weighted rows H1q make sections of different collocation density
comparable); the intermediate-section comparison is reported in (vii). Fourth output (15:25Z; the same H1-type rows with radial trapezoid weights, H1q; runs/c2/c2gram2_M24_s8_p4_H1m_NJ1_rowsH1q.json): five
smallest 0.3775, 0.4773, 0.5359, 0.5978, 0.6636; largest 2.751e5 (ratio 1.4e-6; quantiles 1 percent 2.57, median 196); cos^2 with J 1.4e-7, tails
1.4e-8, J_inner 5.5e-7, KP/TAU 1.1e-8, ref_J 1.1e-6, ref_Jin 2.0e-8, ref_wide 5.1e-4; localization medians r = 2.80 ([1.15, 9.55]), 6.90 ([3.81,
13.3]), 9.44 ([4.84, 16.8]), the smallest again with a substantial m = 0 component (squared projection 0.8055 onto the m = 0 column span; 0.8095 of its energy in the harmonics N = 0, 1; verifier item 149). The H1q values are the ones to
compare across sections of different collocation density (they approximate the integral functional), so the size test of the H1-type functional
reads: M24/s8/Mout32 ppc 4: 0.3775; the M16/s16, M16/s8 and M24/s16 values are in (vii); M24/s8/Mout40 was skipped (disk space, see (vii)). Summary of the M24 set: in all four functionals (L2 rows C^0 and C^1, H1 rows, H1q rows) the five weakest directions are overwhelmingly in the spline span, carry most of their X-energy at r between 1 and 22 (a range overlapping the source radius x_* = 8.6 and the weight-ratio minimum r = L = 7.65), have varied angular content (the smallest H1 and H1q directions have 0.87 and 0.81 of their energy in the harmonics N = 0, 1 at M24, 0.90 and 0.83 at M16; other weak directions are not low-frequency), and have cos^2 below 1e-3 against the named references (joint reference span: squared principal cosine below 0.002).
M16/s16/Mout40 ppc 4 in version 3 (15:38Z; regenerated section, column pieces byte-identical to the original; four runs of about 1 min each):
L2 rows C^0 0.16978, 0.20276, 0.21306 (identical to version 2); L2 rows C^1 with all 64 constraints (1834 retained) 0.17076, 0.20285, 0.21308
(version 2's mis-specified 'NJ1' gave 0.15822): as at M24, the C^1 joins change the smallest values by less than 1 percent; H1-type rows (37320
rows) 2.4485, 3.2299, 3.2932 (largest 3.45e6); quadrature-weighted H1q rows 0.4131, 0.5200, 0.5465 (largest 2.25e5; 1 percent quantile 1.75,
median 135). References: cos^2 of the five smallest directions with ref_J, ref_Jin, ref_wide at most 9.0e-10 / 3.3e-8 / 4.4e-7 (L2 rows) and
1.4e-6 / 1.4e-8 / 6.9e-4 (H1q); retained-space cos^2 of the references 1.0000 / 0.9297 / 1.0000. Localization: energy medians r = 5.32 / 9.10 /
11.6 (L2 rows), 3.57 / 8.71 / 8.47 (H1q), the smallest H1q direction with squared projection 0.8303 onto the m = 0 column span (0.8344 of its energy in the harmonics N = 0, 1; the smallest H1 direction: 0.8917 and 0.8981; verifier item 149).
SIZE TEST OF THE DERIVATIVE-BALANCED FUNCTIONAL (H1q, the cross-density comparable form; both sections at four collocation points per cell, C^1
joins): M16/s16/Mout40 (1834 retained) 0.4131, 0.5200, 0.5465 -> M24/s8/Mout32 (5078 retained) 0.3775, 0.4773, 0.5359: minus 8.6, 8.2 and 1.9
percent, while the largest value (2.25e5 -> 2.75e5), the 1 percent quantile (1.75 -> 2.57) and the median (135 -> 196) INCREASE. A comparison with the L2-row functional (minus 27 percent per row for the same pair) mixes two different radial measures and angular normalizations and does not show that the added derivative reduced the refinement sensitivity; the proper partner is the quadrature-weighted L2q functional on the same rows (chain8f2, complete; see (vii)). With two sizes neither a plateau nor a collapse is established; the pair also mixes trial-space enlargement, a reduced image cutoff (Mout 32 against 40), changed sampling and independently chosen Gram cuts (the retained spaces are not nested even though the nominal spline and angular spaces are), so no monotonicity is asserted. The intermediate sections (M16/s8/Mout40,
M24/s16/Mout40, M24/s16/Mout32, M24/s8/Mout40; chains 8f/8f2, 15:38Z to 18:24Z) separate the angular, radial and Mout effects; their H1q rows are
in (vii). Final tables (regenerated by runs/collect_v3.sh; table 2 = continuous references, table 3 = H1-type rows):
| section | rows | joins | retained | 3 smallest (F-, version 3) | cos^2 of the 5 smallest directions with ref_J (max) | with ref_Jin (max) | with ref_wide (max) | principal cosine (5 smallest) vs ref_J, ref_Jin, ref_wide | X-norm ref_J, ref_Jin, ref_wide | cos^2 of ref_J, ref_Jin, ref_wide with the F- span |
|---|---:|---|---:|---|---:|---:|---:|---|---|---|
| ppc 4 (M16_s16_p4) | 18680 | C^0 | 1866 | 0.1698, 0.2028, 0.2131 | 7.9e-10 | 3.3e-08 | 4.3e-07 | 5.2e-05, 2.7e-04, 1.0e-03 | 1.428e+09, 3.129e+00, 6.099e+05 | 1.0000, 9.3e-01, 1.0000 |
| ppc 4 (M16_s16_p4) | 18680 | C^1 | 1834 | 0.1708, 0.2029, 0.2131 | 9.0e-10 | 3.2e-08 | 4.4e-07 | 5.3e-05, 2.7e-04, 1.0e-03 | 1.428e+09, 3.129e+00, 6.099e+05 | 1.0000, 9.3e-01, 1.0000 |
| M24/s8/Mout32 ppc 4 (M24_s8_p4) | 27360 | C^0 | 5126 | 0.1492, 0.1797, 0.1851 | 9.0e-10 | 1.3e-08 | 4.3e-07 | 4.8e-05, 1.4e-04, 7.9e-04 | 1.428e+09, 3.129e+00, 6.099e+05 | 1.0000, 9.3e-01, 1.0000 |
| M24/s8/Mout32 ppc 4 (M24_s8_p4) | 27360 | C^1 | 5078 | 0.1499, 0.1798, 0.1851 | 9.2e-10 | 9.4e-08 | 4.3e-07 | 4.8e-05, 3.9e-04, 7.9e-04 | 1.428e+09, 3.129e+00, 6.099e+05 | 1.0000, 9.3e-01, 1.0000 |
| section, row type (H1: collocation rows; H1q: with radial trapezoid weights) | rows (value+angular, radial FD) | retained | 3 smallest (F-, H1-type image norm, C^1 joins) | sigma_min/sqrt(rows) | largest | cos^2 of the 5 smallest with the J column (max) | tail span | J_inner | ref_J | ref_Jin | ref_wide |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ppc 4 (M16_s16_p4), H1 | 37320 | 1834 | 2.4485, 3.2299, 3.2932 | 1.267e-02 | 3.45e+06 | 9.4e-07 | 4.4e-07 | 9.3e-07 | 3.6e-06 | 4.7e-08 | 8.0e-04 |
| ppc 4 (M16_s16_p4), H1q | 37320 | 1834 | 0.4131, 0.5200, 0.5465 | 2.138e-03 | 2.25e+05 | 1.7e-07 | 1.8e-08 | 3.6e-07 | 1.4e-06 | 1.4e-08 | 6.9e-04 |
| M24/s8/Mout32 ppc 4 (M24_s8_p4), H1 | 54688 | 5078 | 3.0932, 4.0289, 4.3712 | 1.323e-02 | 4.24e+06 | 2.4e-06 | 1.8e-06 | 2.1e-06 | 7.5e-06 | 1.2e-07 | 8.6e-04 |
| M24/s8/Mout32 ppc 4 (M24_s8_p4), H1q | 54688 | 5078 | 0.3775, 0.4773, 0.5359 | 1.614e-03 | 2.75e+05 | 1.4e-07 | 1.4e-08 | 5.5e-07 | 1.1e-06 | 2.0e-08 | 5.1e-04 |
(vii) Intermediate sections (chain8f2; version 3 with L2q rows and saved images; FLOATING). RADIAL refinement at fixed M = 16 and Mout 40
(M16/s8/Mout40 ppc 4: 3507 F- columns, 3418 retained with C^0 joins, 3386 with C^1; 34200 collocation rows; 16:09Z to 16:29Z):
- L2 rows C^0: 0.2371, 0.2836, 0.2975 (largest 4.24e4; per row 1.282e-3) against 0.1698, 0.2028, 0.2131 (per row 1.242e-3) at stride 16: the
  smallest L2-row value does not decrease under radial refinement (it rises, by 3 percent per row). The weakest directions are the same functions as
  at stride 16 (energy medians 5.30 / 9.19 / 11.6 against 5.32 / 9.10 / 11.6; harmonic content N = 0, 1: 0.52 for the smallest, the third mostly
  N = 8 to 15).
- H1q rows (C^1): 0.4129, 0.5200, 0.5460, 0.6549, 0.6877 (largest 2.70e5; 1 percent quantile 2.63, median 182) against 0.4131, 0.5200, 0.5465,
  0.6549, 0.6878 at stride 16: identical to three or four digits, with identical localization (medians 3.56 / 8.71 / 8.49 against 3.57 / 8.71 /
  8.47) and m = 0 content (squared projection 0.831 against 0.830; 83 percent of the energy in harmonics N = 0, 1). So at M = 16 the five
  smallest derivative-balanced quotients change by at most 0.09 percent under the stride refinement 16 -> 8 (relative changes 6.4e-4, 4.8e-5, 8.7e-4,
  5.2e-5, 1.7e-4 from the saved values), and the 8.6 percent decrease from M16/s16/Mout40 to M24/s8/Mout32 is separated below by the direct runs
  M24/s16/Mout40 and M24/s16/Mout32 into the angular refinement (M 16 -> 24) and the image cutoff (Mout 40 -> 32).
  H1 collocation rows: 3.3396, 4.4526, 4.5328 (largest 4.18e6; 68360 rows).
- L2q rows (C^1; the quadrature-weighted partner of H1q): 0.02814, 0.03244, 0.03281, 0.03363, 0.03565 (largest 4.50e3). Same-vector evaluation
  (src/c2_img_eval.py, from the saved collocation images): the five L2q-weakest directions have H1q quotients 0.72, 0.94, 4.36, 0.94, 3.83 and H1
  quotients 6.3, 10.9, 70.5, 10.3, 61.4; the third and fifth are radially oscillatory thin-shell functions (the third has 99.6 percent of its
  X-energy in r in [8, 16), 10 to 90 percent in r = 8.58 to 8.97, i.e. at the source radius x_* = 8.600, with mixed harmonics N <= 15) whose
  L2-type image is small and whose H1-type image is large: the derivative-gain obstruction of (iv) made concrete. Conversely the H1q-weakest
  directions have L2q quotients 0.127, 0.100, 0.130, 0.066, 0.057 (2.0 to 4.6 times the L2q minimum 0.02814): the weakest directions of the two
  functionals are different functions. The L2q value at stride 16 (M16/s16 re-run with images) is 0.0281 (7.4b (vii)).
- Reference content in every run: cos^2 of the five smallest directions with J, J_inner, the tails, KP/TAU and the three continuous references
  at most 1.2e-3 (ref_wide, H1 rows), typically below 1e-6.
Eigen-cut sensitivity of H1q at M16/s8 (threshold 1e-12 instead of 1e-10; 3407 instead of 3386 retained; whitening error 4.4e-5): 0.4060, 0.5187, 0.5460 against 0.4129, 0.5200, 0.5460, and at threshold 1e-8 (3357 retained; whitening error 1.7e-8) 0.4148, 0.5204, 0.5460 (runs/c2/c2gram2_M16_s8_o40_p4_H1m_NJ1_rowsH1q_th1e-8.json): the smallest value moves by minus 1.7 percent (1e-12) and plus 0.5 percent (1e-8) with the cut (astra/gram4's warning). ANGULAR refinement at fixed stride 16 and Mout 40 (M24/s16/Mout40 ppc 4: 2931 F- columns, 2798 retained with C^0 joins, 2750 with C^1; 18680
rows; 17:05Z to 17:16Z):
- L2 rows C^0: 0.1070, 0.1283, 0.1326 (largest 4.13e4; per row 7.831e-4) against 0.1698, 0.2028, 0.2131 (1.242e-3) at M = 16: the angular
  refinement lowers the L2-row minimum by 37 percent per row (the radial refinement raised it by 3 percent, and M24/s8/Mout32 gave 0.1492): the
  L2-row minimum depends on every discretization parameter. Weakest directions at the same radii (medians 4.40 / 6.94 / 11.9); the third has 0.75
  of its energy in harmonics N >= 16. L2q (C^1): 0.0178, 0.0206, 0.0211 (M16/s8: 0.0281). H1 (C^1; 37320 rows): 2.2571, 2.9256, 3.2037.
- H1q rows (C^1): 0.3777, 0.4775, 0.5366, 0.5980, 0.6637 (largest 2.29e5; 1 percent quantile 1.73, median 149), with the same localization
  (energy medians 2.81 / 6.92 / 9.45) and m = 0 content (squared projection 0.805; 0.809 of the energy in N = 0, 1) as at M24/s8/Mout32.
SIZE TEST OF THE DERIVATIVE-BALANCED FUNCTIONAL, four sections at four collocation points per cell, C^1 joins (H1q; floating):
| section | retained | H1q five smallest | largest | 1 percent quantile, median |
|---|---:|---|---:|---|
| M16/s16/Mout40 | 1834 | 0.4131, 0.5200, 0.5465, 0.6549, 0.6878 | 2.25e5 | 1.75, 135 |
| M16/s8/Mout40 (radial refinement) | 3386 | 0.4129, 0.5200, 0.5460, 0.6549, 0.6877 | 2.70e5 | 2.63, 182 |
| M24/s16/Mout40 (angular refinement) | 2750 | 0.3777, 0.4775, 0.5366, 0.5980, 0.6637 | 2.29e5 | 1.73, 149 |
| M24/s16/Mout32 (angular refinement, smaller image cutoff) | 2750 | 0.3777, 0.4775, 0.5366, 0.5979, 0.6637 | 2.29e5 | 1.73, 149 |
| M24/s8/Mout32 (both, smaller image cutoff) | 5078 | 0.3775, 0.4773, 0.5359, 0.5978, 0.6636 | 2.75e5 | 2.57, 196 |
Reading (floating; rules of notes/C2_v3_design.md section 3 and the astra/gram4 qualifications): the five smallest H1q values change by at most 0.09 percent under the radial refinement at M = 16 (stride 16 -> 8 at Mout 40: relative changes 6.4e-4, 4.8e-5, 8.7e-4, 5.2e-5, 1.7e-4) and by at most 0.12 percent at M = 24 (stride 16 -> 8 at Mout 32: 5.7e-4, 4.8e-4, 1.2e-3, 1.8e-4, 1.3e-4; ver topic 155 finds the same from the saved images), by less than 3e-5 relative under the image cutoff (Mout 40 -> 32 at M = 24, stride 16: 2.7e-5, 2.1e-5, 1.2e-5, 1.9e-5, 8.1e-6; the other functionals of this pair change by at most 7.8e-5 relative: L2 C^0 0.1070 / 0.1070, L2q 0.0178 / 0.0178, H1 2.2569 / 2.2571, 17:41Z; the two saved M24/s16/Mout40 weakest directions carry between 1.4e-7 and 1.5e-4 of their image energy in the modes N = 32 to 39, ver topic 155: small but nonzero, and nothing is known about N >= 40), and decrease by 8.6, 8.2, 1.8, 8.7, 3.5 percent under the angular refinement (16 -> 24 modes); the weakest directions keep their radial
localization (energy medians 2.8 / 6.9 / 9.4, 10 to 90 percent within r = 1.1 to 17) and their angular content (0.81 to 0.83 of the energy of the
smallest in N = 0, 1). So, among the parameters varied (two strides, two image cutoffs, two angular sizes, and the three row densities below), the five smallest
derivative-balanced quotients of these sections change by more than 0.2 percent only with the angular truncation (and with the eigen-cut, 0.5 to
1.7 percent); this is an observation on the sections computed, not a convergence statement, and whether the angular sequence 0.4131 -> 0.3777
tends to a positive limit or decreases further with more modes cannot be told from two
angular sizes (M = 32 would need about 4 x the columns and is out of reach of the 2 GB lane limit with the present assembler). Nothing follows
about L itself (retained spaces not nested, eigen-cut sensitivity 1.7 percent at threshold 1e-12, floating). L2q against H1q on the SAME rows, joins and grids (the comparison astra/gram4 asked for; M16/s16 ppc 4 re-run 17:53Z, L2 C^0 0.1698 reproduced):
quadrature-weighted L2 minimum L2q: M16/s16 0.0281, 0.0324, 0.0336 | M16/s8 0.0281, 0.0324, 0.0328 (radial refinement: the smallest changes by 1.8e-5 relative and the second by 3.0e-4, the third to fifth by 2.5,
7.4 and 9.1 percent; the earlier rise of
the unweighted L2-row minimum under radial refinement was the per-row normalization of collocation rows, not the functional) | M24/s16 0.0178,
0.0206, 0.0211 (angular refinement: minus 36 to 39 percent for each of the five) | Mout 40 -> 32 at M = 24: relative changes 2.3e-5, 1.5e-5, 2.2e-5,
1.5e-5, 9.2e-6. So on identical rows the angular-refinement sensitivity of the smallest
quotient is minus 37 percent without the derivative (L2q) and minus 8.6 percent with it (H1q), while the stride and the image cutoff change the
smallest L2q and H1q values by less than 0.1 percent. The weakest L2q and H1q directions are different functions (same-vector quotients: the L2q-weakest at M16/s16 have H1q quotients 0.72 to
1.13 against the H1q minimum 0.4131). Row-density check of the quadrature-weighted functionals (M16/s16 in version 3 at ppc 2, 4 and 6, i.e. 10760, 18680 and 26600 collocation rows,
21480, 37320 and 53160 rows with the radial finite differences; ppc 2 18:06Z, ppc 6 18:24Z; runs/c2/c2gram2_M16_s16_p{2,4_re2,6}_H1m_*.json). The
trial space is the same at all three densities: 1955 F- columns, 1866 retained with the C^0 joins (L2 rows) and 1834 with the C^1 joins (L2q, H1,
H1q rows) at the eigen threshold 1e-10 (1887 and 1855 at 1e-12), so only the rows change. Five smallest: L2q 0.02814, 0.03245, 0.03363, 0.03631,
0.03921 at ppc 2, 4 and 6 alike (largest relative change 2.2e-4 from 2 to 4 points per cell and 2.5e-5 from 4 to 6); H1q 0.4130, 0.5200, 0.5463,
0.6548, 0.6877 (ppc 2) | 0.4131, 0.5200, 0.5465, 0.6549, 0.6878 (ppc 4) | 0.41313, 0.52005, 0.54653, 0.65493, 0.68783 (ppc 6) (largest relative
change 3.2e-4 from 2 to 4 and 6.8e-5 from 4 to 6). The unweighted collocation functionals grow with the row count (L2 C^0 0.1208 / 0.1698 / 0.2067,
H1 1.7637 / 2.4485 / 2.9513; relative to the EARLIER value: L2 +40.5 and +21.8 percent, H1 +38.8 and +20.5 percent, ver topic 158) as a count
effect of summing more rows. M24/s8/Mout40 is skipped for disk space and is
redundant for the Mout question.
Nothing above is rigorous; the sections restrict the trial space, observe the image on N < Mout modes and are floating (astra/gram3 item 5).

### 7.4c Does the finite section see the scaling tangent K? (shift 6, 19:34Z; VERSION 2 2026-10-21T20:11Z after the referee round astra/kproj1, wording revised 2026-10-21T21:12Z after astra/kproj2; FLOATING, evidence only; src/c2_Kproj.py; runs/kproj/)
Question (section 9, item 0): the scaling tangent K = rho~ - X.grad rho~ has the floating X-norm quotient ||L K||_X / ||K||_X = 44.9 / 7659 = 5.9e-3
(7.11, with L K = eps~ - X.grad eps~ for the exactly normalized trial, ver topic 138), far below the smallest singular values of the finite
sections of 7.4b (0.17 to 0.41 in the L2 / H1q row functionals), although the F- column set carries no normalization constraint that would exclude
K (the J column is included). Which is it: K not representable in the section, or the section's functional not small on K?
Definitions used below. Section: the F- column set of 7.4b for M16/s16 (Mh = 16 angular modes, radial stride 16: 1953 function columns = coarse
degree-7 B-splines, inner powers, outer power laws with growth below r^k, plus KP and TAU; 4 collocation points per coarse cell, Ne = 467 radii
t_i on 3.8e-4 <= r <= 7.7e5, image modes N < Mout = 40; join constraints C^1 (NJ = 1) at tmin and t0, eigen threshold 1e-10 on the equilibrated
constrained Gram: 1834 retained directions, exactly the section of the H1q row of 7.4b (vii)). Row functionals (c2_gram2.weighted_rows): L2 =
[sum_i,N w_i^2 (Lh)_N(t_i)^2]^(1/2) with w_i = (1+u_i)^(1/2)/m(r_i); L2q with the radial trapezoid weights omega_i; H1 = value rows times
(1+(2N+1)^2)^(1/2) plus the radial finite-difference rows wbar_i ((Lh)_N(t_{i+1}) - (Lh)_N(t_i))/Delta_i between consecutive radii, Delta_i =
t_{i+1} - t_i, wbar_i = (w_i + w_{i+1})/2; H1q = H1 with the value rows multiplied by sqrt(omega_i) (trapezoid weights of the measure dt on the radii
t_i, half weights at the two ends) and the difference rows by sqrt(Delta_i) (src/c2_gram2.py weighted_rows). Quotient of a function h =
row functional of its image divided by ||h||_X, with ||.||_X the H1m norm of 7.4b taken over the Gram's quadrature range (r from 1e-13 to 1e23,
exterior half-lines subdivided; for K this range adds 13 to the truncated-range norm^2 5.86622611e7 of 7.11: 5.86622741e7). The section's smallest
singular value is the minimum of exactly this quotient over the retained span. Comparison minima: L2 0.1698 (C^0 joins, NJ 0, 1866 retained), L2q
0.0281, H1 2.4485, H1q 0.4131 (C^1 joins, 1834 retained), all M16/s16 at 4 points per cell (7.4b (vii)).
Method. (A) The H1m Gram of the 1955 columns is rebuilt from the pickled pieces and the saved angular vectors A0, Bm of KP and TAU with the
quadrature of c2_gram2 (its diagonal reproduces the saved G_diag to 1.1e-15 componentwise; 24 against 48 Gauss nodes per interval 9.8e-15); K is
evaluated as x^2 y sum_m a~_m(t) cos 2m theta, a~_m = -2 a_m - a_m', for ALL 260 modes (vectorized spline / exponential-polynomial evaluation) on
the trial's knot cells added to the breakpoints (8 against 16 nodes per cell: 3.2e-9 of the largest inner product; ||K||_X^2 agrees to 9 digits);
the X-orthogonal projection P K onto the retained span is Q Q^T g with g_i = <K, col_i>_X and Q the X-orthonormal retained basis built exactly as in
c2_gram2 (join residual 1.6e-12, whitening error against the 48-node Gram 3.5e-7). (B) L(P K) is assembled at the section's rows by the section's
own assembler (src/lin_fast.py; one combined column per mode for the single-mode columns, the KP and TAU images assembled separately over all 260
modes), and the four row functionals are evaluated on it and on the direct image L K = (eps~ - X.grad eps~)_N(t_i), N < 40, from the analytic jets
(7.11; identity of ver topic 138). The direct image is independent of the section; the assembled image of P K is the section's own operator.
Results (floating).
- Representation: cos^2(K, retained span) = ||P K||_X^2 / ||K||_X^2 = 0.999670, i.e. ||K - P K||_X / ||K||_X = 0.0182 (1.8 percent; the direct
  evaluation ||K - sum_i x_i col_i||_X on the refined quadrature rules, which does not assume exact orthogonality, gives 0.018178 as well, and
  astra/kproj2's independent integration agrees to 1e-8 percentage points);
  with C^0 joins (NJ 0, 1866 retained) 0.999670; free span (plus 16 pure tails, 1850 retained) 0.999690 (0.0176); M24/s16 (2931 columns,
  2750 retained) 0.999868 (0.0115). So the retained spans contain approximants of K within 1.2 to 1.8 percent of its X norm; the next items show
  that these particular approximants have large computed images.
- Direct image of K: L2 2.865e-02, L2q 6.058e-03, H1 6.120e+00, H1q 4.801e-01; quotients over ||K||_X = 7659.1: L2 3.7e-06, L2q 7.9e-07, H1 8.0e-04,
  H1q 6.3e-05, against the section minima 0.1698, 0.0281, 2.4485, 0.4131: smaller by the factors 4.5e4, 3.6e4, 3.1e3, 6.6e3 (three to five orders
  of magnitude). The H1q value-row energy of L K sits at r = 8.65 to 8.92 (10 to 90 percent; the lobe next to P), 96.7 percent of it in the angular
  modes N >= 8.
- Image of the section's representative P K (M16/s16): L2 1.473e+05, L2q 5.361e+04, H1 1.740e+06, H1q 1.959e+05, quotients over ||P K||_X = 7657.9:
  19.2 / 7.00 / 227 / 25.6; M24/s16: H1q 1.567e+05, quotients 19.6 / 7.14 / 126 / 20.5. The H1q value-row energy of L(P K) lies in the
  far field: 10 / 50 / 90 percent radii 8.48e+04 / 2.55e+05 / 5.81e+05 (both sections; the outermost collocation radii). Raw strains: c_raw[P K] = -1.4e-03, c_raw[K] = 0.
  Free span (M16/s16 plus the 16 pure tails, 1850 retained; KprojB2_M16_s16_NJ1_free.json): L2 4.004e+04, L2q 1.336e+04, H1 1.139e+06, H1q 1.037e+05, quotients
  5.23 / 1.75 / 149 / 13.5: the tail columns lower the representative's quotients by the factors 3.68 / 4.01 / 1.53 / 1.89 but leave them above
  K's by the factors 1.4e6 / 2.2e6 / 1.9e5 / 2.2e5;
  its image sits at the cutoff radius (10 percent radius 3241) and in the far field (50 / 90 percent 3.35e+05 / 6.67e+05).
- Amplification of the remainder: ||L(P K) - L K||_H1q / ||K - P K||_X = 1.959e+05 / 139.2 = 1407 (M16/s16), 1784 (M24/s16), against the
  M16 section minimum 0.4131: about 3400 (M16) and 4300 (M24; about 4700 against M24's own minimum 0.3777) times the section minimum (the section's
  largest singular value is 2.25e5, so the
  remainder is not extreme among span elements; it is extreme relative to the minimum). Signed image difference L(P K) - L K used in the numerator.
Reading (floating; wording after the referee's corrections). (i) The smallest singular value of a section is the minimum of the quotient over the
retained span only. K lies within 1.8 percent (X norm) of the span and has quotient 6e-5, while no span element has quotient below 0.41, so
the section minima carry no lower-bound information about the quotient of L on functions outside the span, not even on functions this close to
it; the mechanism is the large far-field image of the remainder, where the row weight exceeds the X weight by (1+u)^(1/2) e^(-t) (1+u^2)^(3/4)
(about r / L^2: 0.313 at r = 8.6, 17 at r = 1000, 1.7e3 at r = 1e5). Closeness in X norm alone would not imply this; the assembled images
establish it here. (ii) The row functional has finite rank (at most 467 x 40 = 18680 value samples; the difference rows are combinations of them), so on any
infinite-dimensional linear space of sufficiently regular functions on which the samples are defined some nonzero element has zero sampled image:
the positive finite-section minimum is a restriction-dependent quantity (individual quotients outside the span, such as K's, remain meaningful as
numbers). (iii) The sections impose no normalization condition J(h) = 0 (J(h) := the x^2 y coefficient of h at the origin, h = x^2 y (J(h) + o(1)),
defined on the class of perturbations with the centre factorization; the J column of the sections is the function x^2 y on r < R0, a different
object), but this does not make K admissible for them: J(K) = -2, and K's leading
tail (1 - k) A_0 e^{(k-3)(t - t0)} lies outside the F- tail class (KP carries a factor t, TAU the angular vector B_m, which is not proportional to
A_0: astra/kproj2 checked the 2 x 2 determinant exactly from the stored coefficients; ver topic 172 (FINAL 21:44Z) verified it for the STORED trial
and the frozen M16/s16 column recipe, minor in (5.859714460078e-15, 5.859714460080e-15), in each rate convention). Scope: every K in this subsection
is the tangent K_s = rho_s - X.grad rho_s of the stored trial (the coefficients of data/trial_v2_h0.008.npz as stored, c_l = 1/k), which is what
src/c2_Kproj.py and src/xnorm_BKK.py evaluate; the exactly normalized trial of the lead's and verifier's analysis (A_00 adjusted by the
normalization) has a tangent that differs from K_s by that adjustment and is not covered by these computations or by ver 172; for THAT exactly
normalized tangent, ver topic 176 (FINAL 23:14Z, lead 23:21Z) states separately that it lies in neither exterior class of the frozen non-free M16
recipe (tails at k - 3 or at fl(k - 3), lower rates at most mu with the explicit gap; uniform determinant window), with the free-tail and the M24
sections, closures, distances and images not covered. So K_s is in neither the sections' class nor the normalized tangent space (a(0) changes); the lead's zero-strain bumps (ver topic 137) give J = c = 0 elements near K in X norm, whose images were not computed
here, so nothing is said about the normalized problem. (iv) None of this concerns the continuous operator in the lead's target norm; 7.4b's
'nothing follows about L itself' stands.
Stage C (cross-check of the direct image; the section's assembler applied to K's own fine-knot single-mode pieces, c[K] reproduced as 4e-15):
the partial sums over the modes m < 32 have row functionals L2 496, H1q 6787; over m < 60 they are L2 0.02871, L2q
6.06455e-03, H1 6.1465, H1q 0.48237 against the direct 0.02865, 6.05848e-03, 6.1204, 0.48006 (0.2 to 0.5 percent): each mode's
the first 60 modes recover the scale of the small image (norms within 0.1 to 0.5 percent) while the signed image difference still has 3.9 to 5.3
percent of the direct image's functionals, so later modes still change the image appreciably; grouped partial sums do not show that every single
mode's image is large. COMPLETE (2026-10-21T20:53Z; 42 pieces tiling the modes 0 to 260, identical grid, runs/kproj/KC_merge_all.json,
KC_assembled_image_all260.npz): applied to all 260 fine-knot modes of K, the section's assembler reproduces the direct sampled image
(eps~ - X.grad eps~)_N(t_i): maximum absolute difference 1.27e-7 against a maximum of 1.96e-3 (6.5e-5; 2.4e-8 on the lobe 4 <= r <= 16 where the
image peaks; the largest difference at r = 3399, N = 1, near the outer join t0), and the four row functionals of the signed image difference are
4.2e-5 to 5.8e-5 of the direct image's (the functionals themselves agree to 6e-7 to 2e-6: L2 0.0286498 against 0.0286498, H1q 0.480057 against
0.480057). The assembled route evaluates L K without invoking the scaling identity, so the K quotients (6.3e-5 in H1q) are produced by the
section's own operator. Both routes share the TrialGreen background data, so this is a consistency check of the perturbation assembly (lin_fast
piecewise closed-form Green integrals) against the jet evaluation (Green ODEs of trial_jets), with no independent validation of the background
Green solver and no rigorous error bound; the source of the remaining 5e-5 difference was not identified. Verifier topic 170 (FINAL 21:14Z) recomputed
the 42-piece sum and the four difference functionals exactly from the saved arrays: ratios 5.3648319681e-5 / 4.1854006024e-5 / 5.7878592854e-5 /
4.9530161926e-5, against the saved 5.3648319761e-5 / 4.1854006276e-5 / 5.7878592187e-5 / 4.9530161146e-5 (the saved sum differs from the exact one
by at most 7.1e-15 per entry, summation order; the verifier's fixed JSON tolerances flag this, which does not affect the two digits quoted here;
its verdict covers the finite arithmetic only).
History: version 1 of this subsection (19:34Z) used K's modes m < Mh + 2 only (m < 18 for M16, m < 26 for M24) and a span without KP and TAU (the
angular coupling of the Phi_m basis reaches |m - m'| = 3, so these parts are not the full K, and 1 - cos^2 is not a relative distance); its cos^2
values (0.9947, 1.0020) and its '0.5 percent' are superseded by the values above (astra/kproj1, notes/astra_kproj1_answer.md; the quotients of K and
the mechanism are unchanged). Second referee round astra/kproj2 (21:11Z, notes/astra_kproj2_answer.md): all version-2 numbers reproduced
independently (distances to 1e-8 percentage points by direct integration of K - P K; quotients, amplifications 1407.1 / 1783.6, quantiles, stage C
sums and tiling); the wording corrections of this revision are its items (K's tail outside the F- class; 'anything in the span'; the factors; the
60-mode statement; the stage C sentence).
Which image numbers belong to which projection: the version-1 B outputs runs/kproj/KprojB_M16_s16_NJ1.json (quotients of P K 18.6 / 6.78 / 104 /
27.6, free span KprojB_M16_s16_NJ1_free.json H1q 43.5, KprojB_M24_s16_NJ1.json 19.6 / 7.14 / 81 / 21.0) are images of the version-1 projections
(m < 18 resp. m < 26 parts, no KP/TAU) and are NOT used above; every quotient and image radius in the Results list comes from the version-2 files
KprojB2_M16_s16_NJ1.json, KprojB2_M16_s16_NJ1_free.json and KprojB2_M24_s16_NJ1.json (projections Kproj2_*.npz, KP/TAU images KT_images.npz). The direct image of K (runs
KprojB*_img.npz, key img_K) is the same array in both versions (it does not depend on the projection). Verifier topic 165 (2026-10-21 20:15Z):
the energy-to-distance identity confirmed, the v1 'energy ratios above 1' refuted as projections, the v2 distances enclosed as (1.81776, 1.81779)
percent (C^1), (1.81764, 1.81766) (C^0), (1.76198, 1.76201) (free) from the saved floating energies.
Files: runs/kproj/Kproj2_*.npz (stage A v2), KprojB2_*.json and _img.npz (stage B v2), KT_images.npz (KP/TAU images), KC_m*.npz and KC_merge_*.json
(stage C); version-1 files Kproj_*.npz, KprojB_*.json kept for the record.

## 7.5 Residual near the source point P in Sobolev norms (floating point, evidence only; shift 2; all refits in this section are BAND-RESTRICTED, see 7.5b)
Scope note (shift 3, 05:09Z, reworded 05:30Z): the knot-scale attribution of the H^3 content below holds for the 0.5-disc (and larger)
norms; on small cut-off balls (delta = 0.0165) the H^{3.1} norm is consistent with a substantial contribution from the localization (the
cutoff acting on the values of the smooth part of eps~), the split not being identified by the norms (7.7c, decomposition table).
Request of the lead (NOTES 18:05Z, 18:40Z): the F- forcing space at P is H^s on a disc with 3 < s < 3.406, so the residual must be
measured there, not only in sup norm. Method (src/trial_jets.py): analytic (t, theta)-jets of eps~ to order 4 (a_m^{(i)} exact from the
representation, Green functions through A_n' = -2n A_n + g_n, B_n' = 2n B_n - g_n, g_n = e^{2t} f_n, Leibniz over the products), exact
angular derivatives, Cartesian derivatives by the chain-rule recursion; L^2 norms over regions by trapezoid quadrature on polar grids
(src/pdisc_norms.py; dt = 1e-5 to 2e-7, dtheta = 1e-4 to 2e-6); fractional norms of a cut-off patch by FFT (src/pdisc_fft.py).
Validation: order 0 agrees with the modal residual; d_t^i and D^alpha agree with finite differences (7-point, h = 1e-4 / 1e-3) to
1e-7 .. 1e-3 relative through order 4; the formulas were refereed by astra (astra/jets1/answer.md: jet algebra, Green ODEs, recursion,
FFT normalization all confirmed; corrections on norm conventions and interpolation adopted, see WORKLOG 19:40Z).
Results for the trial rho~ (P = (x_*, 0), x_* = 8.600064). Seminorms |eps|_k = (sum_{|alpha|=k} ||D^alpha eps~||^2_{L^2})^{1/2}
(unweighted multi-index sum; the Fourier-side convention with binomial weights is also stored in the JSON files); sup_k = max over
|alpha| = k of the sampled sup:
| region | area | |.|_0 | |.|_1 | |.|_2 | |.|_3 | |.|_4 | sup_0 | sup_3 | sup_4 |
|---|---|---|---|---|---|---|---|---|---|
| disc, X-P < x_*/4 = 2.15 | 14.5 | 1.19e-5 | 1.27e-3 | 2.07e-1 | 37.3 | 6.92e3 | 5.0e-5 | 259 | 5.0e4 |
| disc, X-P < 1 | 3.14 | 5.96e-6 | 3.92e-4 | 5.22e-2 | 9.34 | 1.77e3 | 1.7e-5 | 77 | 1.5e4 |
| disc, X-P < 0.5 | 0.785 | 2.87e-6 | 1.36e-4 | 8.08e-3 | 1.03 | 191 | 1.1e-5 | 11.9 | 2.3e3 |
| disc, X-P < 0.1 | 0.0314 | 1.7e-7 | 8.1e-6 | 8.4e-4 | 0.131 | 23.6 | 3.1e-6 | 2.8 | 552 |
| annulus 2^-3 .. 2^-2 | 0.147 | 9.3e-7 | 4.3e-5 | 3.1e-3 | 0.448 | 81.1 | 7.6e-6 | 5.0 | 953 |
| annulus 2^-7 .. 2^-6 | 5.8e-4 | 1.9e-9 | 4.1e-7 | 5.6e-5 | 9.2e-3 | 1.70 | 2.1e-7 | 0.76 | 152 |
| annulus 2^-11 .. 2^-10 | 2.2e-6 | 8.5e-13 | 2.4e-9 | 2.9e-6 | 3.0e-4 | 0.072 | 1.4e-9 | 0.22 | 52 |
| thin annulus r - x_* < 0.01, theta in [0.2, pi/2] (right half) | 0.47 | 3.2e-6 | 1.8e-4 | 1.4e-2 | 1.91 | 318 | 1.6e-5 | 24 | 4.4e3 |
(full tables with all dyadic annuli j = 2..10: runs/pdisc/norms_A.json, norms_B.json, norms_C.json, norms_D.json; notes/TO_TEAM.md 19:25Z.)
FFT of chi eps~ (chi = 1 on X-P <= 0.4, C^infinity to 0 at 0.5; cubic interpolation of the modes in t, superseded by the degree-7 rerun
in runs/pdisc/fft_r0.5_k7.json): H^3 = 0.89, H^3.03 = 1.04, H^3.06 = 1.21, H^3.1 = 1.48, H^3.2 = 2.47, H^3.4 = 6.95, H^3.5 = 11.7,
H^4 = 160; 87 percent of the H^3 norm squared comes from |xi| > 100 and 27 percent from |xi| > 200 (wavelengths 0.016 to 0.06).
Lower orders (degree-7 interpolation, runs/pdisc/fft_r0.5_lower.json, fft_r1.0_lower.json): 0.5-patch H^2 = 7.34e-3, H^2.25 = 2.28e-2,
H^2.5 = 7.43e-2, H^2.75 = 0.253; 1.0-patch (chi = 1 on 0.8, sup 1.67e-5) H^2 = 4.40e-2, H^2.25 = 0.159, H^2.5 = 0.580, H^2.75 = 2.13,
H^3 = 7.86, H^3.06 = 10.76: a factor 3.2-3.6 per quarter derivative.
Interpretation. The residual is small in value (1e-5 on the 0.5-disc) but its H^3 norm there is of order 1 and H^{3.06} about 1.2,
because the residual has radial structure on the knot scale (knot spacing 0.0019 in t = 0.0165 in r near x_*; dominant direction
D^(4,0), 189 of the 191 of |.|_4). The local H^3 density decreases toward P (annuli), so the structure is not concentrated at P.
Cause (src/axis_diag.py, src/wiggle_diag.py): the fourth derivative of the axis trace g(x) = rho~_y(x, 0) is continuous but swings
between -319 and +708 inside the knot interval containing x_* with alternating per-interval means (-279, +234, +377, -136), against a
smooth level of 10 to 40; X3's own formula reproduces these values by finite differences to 0.03-1 percent, so this is X3's knot-scale
structure, not an artefact of the modal re-representation; there is no power law in |x - x_*| (no cusp signature; a spline cannot show
one anyway). The knot-scale content of the modes a_m(t) is 4.5e-7 relative for a_0, 6.5e-6 of itself for a_1, 1.2e-2 for a_20 and
17-50 percent for m >= 50.
Smoothing experiments (src/smooth_band.py, src/smooth_band2.py; runs/pdisc/chainS.log, chainM.log): projecting the modes on coarser
knots on the band t in [log 6, log 12] (all modes) raises the sup residual from 1.1e-4 (W peak) to 1.3e-2 (spacing 0.01), 1.05e-1
(0.02), 4.5e-1 (0.04); the 0.5-disc |.|_3 becomes 2.35 / 1.90 / 1.65 and |.|_4 87 / 40 / 24. Smoothing a single mode range (every 10th
knot) gives W peak 7.2e-2 for modes 0-9 alone, 9.1e-2 for 10-39, 6.9e-2 for 40-99, 6.8e-2 for 40-259: every mode range carries
knot-scale content that the operator sees at the 1e-1 level, although it is below 5e-7 relative in the lowest modes. So X3's residual
of 1e-4 is achieved by knot-scale adjustments of the density of relative size 1e-7 to 1e-6; whether a trial that is smooth at a coarser
scale can reach a comparable residual was tested by a Gauss-Newton re-solve in the coarse space (src/gn_refit2.py, src/lin_fast.py;
runs/pdisc/chainG2.log): the clean re-solves of the smoothed modes on the coarse spaces recover only 10-25 percent of the weighted
residual increase (runs/pdisc/gnC.log, gnA.log, gnb10.log), and a fine-knot re-solve on X3's OWN knots near P (src/resid_smooth.py:
40 modes, 125 fine-knot functions per mode, 5000 unknowns, full nonlocal L, c[delta] = 0) lowers the weighted residual by only 3-4
percent (coefficient changes 3e-10) (the reading 'X3 is converged on its knots' drawn from this at the time was later withdrawn, see the end of this
subsection and 7.5b); adding a penalty on the residual's third
t-derivative (plus the angular third-derivative proxy) lowers that proxy by at most 13 percent (353 -> 306) at the price of a 2.6-fold
larger residual (data/trial_rs_summary.json; linear predictions). The nonlinear evaluations (runs/pdisc/chainR.log) confirm: lambda = 0 gives W peak
1.093e-4 (reference 1.095e-4) and disc |eps|_3 = 1.071 (reference 1.028); lambda = 1e-14 / 1e-12 / 1e-10 give W peak 1.097e-4 / 1.153e-4 /
1.406e-4 and |eps|_3 = 1.123 / 1.876 / 2.116, i.e. the penalty worsens both. Half-spacing knot refinement on the band (src/refine_knots.py,
exact insertion of 138 midpoints in t in [2.0, 2.33]) followed by one Gauss-Newton step on the refined space (9720 unknowns, modes m < 40):
W peak 1.095e-4 -> 9.50e-5 (13 percent lower; linear prediction of the weighted Wiener measure 39 percent) but disc |eps|_3 1.028 -> 4.946
and |eps|_4 191 -> 1177 (sup_3 11.9 -> 41.3): the re-solve puts half-knot-scale structure into the residual, so finer knots lower the sup
residual and raise the H^3 content (runs/pdisc/chainQ.log; both iterations are in the table of 7.5b). The external referee
(astra/smooth1) correctly notes that these are restricted-space experiments and not an exclusion of a smooth exact solution; they do show
that neither projection nor re-solving on X3's knot resolution yields a residual that is small in H^3 near P.

### 7.5b Trials near P: residual peak and fractional norms on the 0.5-disc (floating; lead's request 22:42Z)
BAND RESTRICTION (lead 22:45Z): every refit in this section (coarse-space re-solves of 7.5, same-knot and half-spacing Gauss-Newton steps)
changed the coefficients only on the band t in [2.05, 2.28] (r in [7.8, 9.8]) and fitted rows only there (plus coarse rows outside in the
gn_refit variants). Every characteristic of V in the open quadrant leaves P and exits that band, so a band-supported correction cannot cancel
a transport residual (along a characteristic from P the correction obeys (d/dt - 1) delta = -(eps + N[delta]); with delta = 0 at the band
exit it is the outflow solution, not C^1 at P unless one condition per characteristic holds; with delta regular at P it is nonzero at the
exit). The rigidity measured here is therefore what transport alone predicts; it does not show that X3 is converged on its knots nor that
the spline space is incompatible with the equation. A global re-solve (all radii, inward axis segment included) is the test that would
decide route (a); its cost is estimated at the end of this subsection.
W peak = sup_r sum_N |eps_N| near r = 8.8 (src/pdisc_explore.py); H^s = FFT norm of chi eps~ with chi = 1 on |X - P| <= 0.4 and 0 at 0.5
(src/pdisc_fft.py, degree-7 interpolation); the same-knot refits are src/resid_smooth.py on X3's knots (40 modes, band t in [2.05, 2.28],
lambda = weight of the residual third-derivative penalty), the half-spacing rows are the Gauss-Newton iterations on the refined knots
(src/refine_knots.py + resid_smooth.py). All entries are filled (the FFT runs are complete; runs/pdisc/fft_r0.5_*.json).
| trial | W peak | H^2.5 | H^3 | H^3.06 |
|---|---|---|---|---|
| X3 trial (reference) | 1.095e-4 | 7.43e-2 | 0.890 | 1.208 |
| same knots, lambda = 0 | 1.093e-4 | 7.74e-2 | 0.942 | 1.280 |
| same knots, lambda = 1e-12 | 1.153e-4 | 0.130 | 1.640 | 2.231 |
| same knots, lambda = 1e-10 | 1.406e-4 | 0.150 | 1.857 | 2.519 |
| half-spacing knots, GN step 1 | 9.50e-5 | 0.299 | 4.397 | 6.086 |
| half-spacing knots, GN step 2 | 9.50e-5 | 0.299 | 4.397 | 6.086 (identical to step 1: stationary) |
(Disc seminorms |eps|_3 without cutoff for the same rows: 1.028, 1.071, 1.876, 2.116, 4.946, 4.946.) The knot-refinement branch is closed
(lead 22:42Z): on this branch, band-restricted, finer knots lower the residual peak and raise its H^3 content.
N7, the centre-regular trial (data/trial_n7.npz, src/make_n7.py; lead 21:17Z/22:03Z): the 1026 inner coefficients D_mj of the non-polynomial
terms r^{2j} cos(2m theta) with m > j, j <= 4 (all <= 2.7e-11; X3's modes vanish like r^{2m}) set to zero and the inner corrections re-solved
from the C^6 joins; inner density change 3.0e-10 of a_0; the inner density is a polynomial through degree 11 plus degree >= 13 terms
(|D[m,4]| <= 6.9e-11) and the O((r/rmin)^{50} log^i) corrections; the degree-5 resonance coefficient (verifier topic 60: H7 = h7/rmin^2 in
(-1.423e-9, -1.421e-9), h7 = -8.32e-14 in the stored coefficients) is exactly zero. RIGOROUS S1 of N7 (runs/scalars_n7.json, Arb data
data/cert_n7_green.npz): identical balls to the original trial to all printed digits (x_*, mu~ - 1, w'(P), g, c = 3c_l - 1 exactly).
RIGOROUS middle R0 of N7 (runs/cert_resid_middle_n7.json, 7809 cells): sup W/m <= 2.5965e-4 at r = 8.79 (raw 2.59644551e-4, the base trial's value to 9 digits), sup W <= 1.2015e-4, multiplier
form <= 3.8079e-4 by the per-cell field W_over_m_far of cert_resid.py (a cruder right-end weight evaluation; the base trial's same field also gives
3.80786e-4) and <= 3.8071e-4 by the cert_summary.py evaluation (runs/variants_summary.json; equal to the base trial's), shells equal to the X3
trial's post-fix table to the printed digits (runs/cert_resid_middle_n7_summary.txt), as expected (the two trials
agree for r >= rmin to 3e-10 and have the same strain c to all printed digits). These are NUMERICAL agreements, not identities: N7's
density differs from the first trial's only for r < rmin, but its exact canonical exterior velocity is not identical to the first trial's
(verifier topic 79: the C^6 rejoin changes the exterior stream coefficient at frequency 522 by r_-^{526} S r^{-522}/16 with S a nonzero
rational, a term of order 1e-1100 that no printed digit can show). Not yet certified for N7: the inner region r < rmin (where it differs) and
the outer region/tails; its FFT residual norms on the 0.5-disc (runs/pdisc/fft_r0.5_n7.json, ESTIMATES, same grid/padding as the X3 trial's
run) are sup|eps| = 1.14e-5, L2 = 2.436e-6, H^2 = 7.339e-3, H^3 = 0.8898, H^3.06 = 1.2078, H^3.1 = 1.4816, H^4 = 160.0: equal to the X3
trial's values to 7 digits (relative difference <= 1e-7; numerical agreement, see above).
Feasibility of a global re-solve in X3's own spline space (estimate): full space 260 modes x 1565 functions = 4.1e5 unknowns, rows 7809
cells x 2 x 522 modes = 8e6: a dense matrix is out of reach; matrix-free LSQR needs one full closed-form Green solve plus residual modes at
all collocation radii per matvec (about 3 min; the adjoint matvec needs the transpose of the Green operator, not implemented) and hundreds of
iterations: tens of hours. Reduced comparison test (lead 22:45Z, optional): modes m < 10 with every second knot (7820 unknowns), rows at one
point per cell for N < 20 (1.56e5 rows): matrix 1.2e9 entries (float32: 4.9 GB), assembly about 1.1 h (0.5 s per column at 7809 radii),
normal equations 9.5e12 flops (about 1 h): roughly 2.5 h of one CPU for the global step, versus minutes for the band step with the same
columns restricted to the band. Not run (the lead closed the band-restricted branch, 22:42Z on 2026-10-20); feasibility and cost estimate only.

Feasibility and cost estimate of a GLOBAL re-solve in the trial's own spline space (lead 22:45Z; estimate only, nothing run). Unknowns: the
trial has 260 modes x 1565 radial spline coefficients (S in data/trial_v2_h0.008.npz; knots 1573, degree 7 in t = log r on [log rmin, log R0])
plus the inner (D, Ei: 260 x 7 each) and outer (Aout 260 x 10, Eo 260 x 7) expansion coefficients: about 4.1e5 unknowns and the scalar c_l.
One linearized-operator matvec (src/lin_fast.py structure: radial Green sweeps O(N_t) per mode for psi[h], angular products as convolutions
O(M^2) or FFT O(M log M) per radius, transport term by exact spline derivatives) costs about N_t M^2 ~ 1600 x 260^2 = 1.1e8 flops with
convolutions (a few 0.1 s in numpy, less with FFT); the normal equations are ill-conditioned (J near-kernel, c_l soft direction, basis
conditioning seen in 7.4), so a matrix-free LSQR/LSMR Gauss-Newton step needs 1e3-1e4 iterations: 0.3-3 h per GN step on one core, several
steps, plus the fitting rows (the residual on a fine (t, theta) grid, 1e6-1e7 rows) and the centre/source constraints. Feasible in principle
(1-2 days of one core, or hours on the GPU with the convolutions as batched matmuls), not within this run under the one-job CPU guard with the
the certificate chains took the CPU and the experiment was not run. Expected effect, if the lead's transport reading is right: a residual near P limited by the spline space and X3's
far-field closure rather than by the band restriction; the band-vs-global comparison with m < 10 (design above) is the cheap test of that
reading; it was not run in this study (feasibility and cost estimates only).

## 7.6 N1': rigorous bounds on the trial velocity field for the lead's global-flow argument (src/cert_flow.py; COMPLETE for the whole quadrant)
Request (lead 20:01Z; notes/global_flow.md section 10): certified (Y) V_2 >= m_0 y on Q = {x > 0, y > 0}; (H2') signs of V_1(x, 0);
(H3) DV(0), DV(P); (H4) X.V >= kappa_0 |X|^2 for |X| >= R_0; V_1 <= -13 and T_0 <= 1.23 on B_1 = [4.80, 6.82] x [0, 2.85];
T_0 <= -0.22 on Q minus B_1, with T_0 = -(1 + c_l) + a (V_1/x - s) + b (V_2/y - s) + mu(r) s, s = X.V/r^2, a = 129/20, b = 307/100,
mu(r) = gamma' + (a + b - gamma')/(1 + (r/R_m)^p), gamma' = 1129/1000, R_m = 6, p = 4.
Formulas (U = grad^perp psi, U_r = -psi_theta/r, U_theta = psi_r, psi = sum_n psi_n(r) sin 2n theta):
  s = c_l - r^{-2} sum_n 2n psi_n cos(2n theta);  V_2/y = s + r^{-1} sum_n psi_r,n C_n(theta);  V_1/x = s - r^{-1} sum_n psi_r,n S_n(theta),
  C_n = cos theta sin(2n theta)/sin theta = 2 cos theta sum_{j<n} cos((2j+1) theta),  S_n = sin theta sin(2n theta)/cos theta
  = 2 sin theta sum_{j<n} (-1)^{n-1-j} sin((2j+1) theta)  (both bounded by 2n; third derivatives bounded by 2n + 6n^2 + 8n^3 + 4n^4).
Method: on each radial sub-cell of the certificate (7809 middle, 8948 outer to r = 8e10, 2632 inner to r = 5e-5) Taylor models in
sigma = t - t_a of 2n psi_n e^{-2t} and psi_r,n e^{-t} from the Arb boundary values (same ODE recursion as the residual certificate);
on each angular cell [th_a, th_b] (200 cells on [0, pi/2], bisected adaptively up to 7 levels where a target inequality fails) a
second-order Taylor model of each angular factor about the centre with the third-derivative remainder; the mode sums are then
polynomials in (sigma, eta) with mid-rad coefficients and a tensor Bernstein enclosure (eta on [-d, d], sigma on 2 sub-intervals)
gives two-sided ranges of s, V_2/y, V_1/x and T_0 on the 2D cell (all operations in the rigorous mid-rad arithmetic of src/midrad.py,
constants from Arb). Box classification of each polar cell against B_1 (in / out / straddling, the latter bisected). Validation:
the floating values at cell midpoints (src/trial_green.py) lie inside the certified ranges on all tested cells; the certified
extrema are within 5e-4 .. 5e-3 of the floating extrema (e.g. r = 8.60: V_2/y min 0.9993 certified vs 0.9998 floating; r = 34.8:
T_0 max -0.2796 vs -0.2805). External audit: astra flow1 (astra/flow1/answer.md, PROOF.md; 18,792 Arb checks of the angular coefficients) confirmed the
mathematics (identities, derivative bounds, tensor Bernstein enclosure, tail formulas, T_0 bounds; the data satisfy every hypothesis)
and listed 16 implementation defects (rounding directions, float trig allowances, interval conversions, endpoint and hypothesis checks,
coverage bookkeeping, a dead branch and missing monotonicity checks in the tails); all were repaired in revision 2 of src/cert_flow.py and
src/cert_flow_tails.py (angular factors in Arb, exact rational constants, Arb cell edges, outward rounding throughout, asserts with
abort). Every number reported here is from the revised code (the tails were rerun: unchanged).
Tails (RIGOROUS, src/cert_flow_tails.py revision 2, Arb 256 bits, runs/flow_tails.json; termwise majorants of the exponential-polynomial
representations with verified monotonicity and nonresonance): for r >= R_T = 8.244e10, |s - c_l| <= 9.84e-8 and |V_2/y - c_l|,
|V_1/x - c_l| <= 1.10e-6, so s >= 5.575362, V_2/y >= 5.575361 (raw 5.5753615; the earlier 5.575362 was inward, corrected 00:5xZ) and T_0 <= -0.2807669 (raw -0.28076698; the limit -(1 + c_l) + gamma' c_l is
-0.280778). For r <= r_T = 5.1555e-5 the leading (a_0 = 1, n = 1) terms are exact (the e^{2 tau'} coefficient of psi_1 comes from the B
transient: 2 psi_1 e^{-2t} -> c with c_lead = 15.726087831925 = c to 12 digits) and the rest is <= 3.54e-9 (raw 3.5322e-9), so V_2/y >= 21.301450
(4c_l - 1), V_1/x <= -10.150725 (1 - 2c_l), T_0 <= -6.652087.
Status: all three finite-region runs (middle, outer, inner) and the tails are complete; results in runs/flow_{middle,outer,inner}.json and
runs/flow_tails.json; aggregation by src/flow_summary.py (runs/flow_summary_all.txt). Tail boundaries: R_T = r_T,out = e^{t0 + 17} (enclosure
[82440053208.41069, 82440053208.41103] in runs/flow_tails.json) and r_T = r_T,in = e^{tmin - 5} (enclosure [5.1554893431607276e-5,
5.155489343160734e-5]); the decimal radii 8.244e10 and 5.1555e-5 below are location descriptions of these exact boundaries, and the cell runs
cover exactly [r_T,in, r_T,out] (no gap).
Certified scalars for N1' (S1, runs/scalars_full.json): x_* = 8.600063805157177 +/- 3.0e-13 (raw radius 2.9402e-13) isolated by a contracting interval
Newton step (so w' != 0 on the isolating interval); w'(P) = d_x V~_1(x_*, 0) in [10.150725243807495, 10.150725243814781];
mu~ = d_y V~_2(P) with mu~ - 1 in [-2.2529e-8, -2.2527e-8]; divergence identity w'(P) + mu~ - 2 c_l in [-4.54e-12, 4.53e-12];
DV(0) = diag(1 - 2c_l, 4c_l - 1) exactly (c~ = 3c_l - 1 certified).
Crossing cell (RIGOROUS, src/cert_axis_cell.py, runs/axis_cell.json; closes the verifier's 21:34Z coverage objection): on the radial
sub-cell containing x_* (r in [8.598670706, 8.606894667]) x^2 w' = dF/dt - F in [750.506, 751.997] over the whole cell, so w' >= 10.1312
there, and x V_1(x, 0) is negative at its left end ([-0.1215927194, -0.1215927193]) and positive at its right end ([0.5964619822, ...]):
exactly one zero of V_1(x, 0) in the cell; all other axis cells receive strict-sign checks in cert_flow.py.
CERTIFIED RESULTS (middle region 0.00765 <= r <= 3413, all of theta in [0, pi/2], 7809 radial x 200 angular cells with adaptive bisection;
plus the tails; the outer and inner cell runs are complete (below); runs/flow_middle.json, runs/flow_summary_all.txt):
  (Y)  V_2/y >= 0.98845 on the middle region (minimum on the cells r in [8.8654, 8.8738] at the x-axis; floating minimum 0.988);
       V_2/y >= 5.575361 for r >= 8.244e10 and >= 21.301450 for r <= 5.1555e-5.
  (H2') V_1/x <= -0.001585 on every axis cell below x_*, >= 0.0077249 on every axis cell above x_* (middle region); the cell containing x_*
       has w' >= 10.1312 and a sign change of x V_1 (section above), so V_1(x, 0) has exactly one zero in [0.00765, 3413];
       V_1/x <= -10.150725 for r <= 5.1555e-5 and >= 5.575361 for r >= 8.244e10.
  (H4) X.V/r^2 >= 3.4957 on the cells with r_hi >= 20 (minimum at r = 20), >= 4.2564 for r >= 30, >= 5.575362 for r >= 8.244e10.
  B_1 = [4.80, 6.82] x [0, 2.85]: T_0 <= 1.2780 on the cells meeting B_1 (maximum at r in [5.7601, 5.7688]); V_1 <= -12.834 on B_1 (maximum
       at the box corner, r in [7.3805, 7.3922]; the requested -13 is not attained there); T_0 <= -0.2399 on the middle region off B_1
       (maximum at r in [67.99, 68.10]), <= -0.2807669 for r >= 8.244e10, <= -6.652087 for r <= 5.1555e-5.
  Bookkeeping: 245 angular sub-cells in 3 radial cells (r in [7.357, 7.392], the box corner) reached the maximal bisection depth without
  meeting the V_1 <= -13 target; their certified maxima are included in the numbers above; no other target failed; 0 axis-sign failures.
  Constants: a = 129/20, b = 307/100, gamma' = 1129/1000 (Arb rationals), R_m = 6, p = 4, c_l := 1/k.
  Domain convention (verifier topic64): every per-cell statement holds on the exact log-cell [t_a, t_b] of the certificate's radial
  partition (abutting cells cover [t_min, t_0] exactly); the printed r_lo, r_hi are outer enclosures of e^{t_a}, e^{t_b} (r_hi uses
  e^h <= 1 + h + h^2, an excess of about 4e-6 at r ~ 8.6) used only to locate cells and for the superset box classification.
  Decimals are rounded outward from the stored aggregates (runs/flow_middle.json glob: T0_max_out = -0.2399542, T0_max_in = 1.2779480,
  axis above min = 0.0077249424; verifier 22:41Z caught three inward roundings in the first printing).
  Independent checks (verifier): topic69 (my modal R, dR, F maps on all 7809 middle cells, 4.9e7 exact comparisons), topic72 (the mid-rad
  matmul error model), topic73 (the angular factors: exact identities, derivative bounds, 51000 angular nodes, 4176 remainders, 519129
  coefficient boxes at 221 centres), topic64 (crossing cell), topic71 (independent inner and far-tail bounds consistent with mine);
  23:03Z: the middle coverage (39046 checks over all 7809 cells, R_0 = 20 crossing) passed; the box-cost
  instances exp((1.278 + 0.2) t_1)/0.2 = 6.3095658 < 6.31 and exp((1.278 + 0.22) t_1)/0.22 = 5.7540536 < 5.76 (t_1 = 2.02/12.834) were
  confirmed in Arb512/iv180, conditional on acceptance of the whole flow certificate (verifier: the finite flow scalars of all 19389 cells
  and the tails are CONFIRMED (topics 71, 75); the full radial Taylor models and the field inequalities remain OPEN on their side).
  OUTER CELLS DONE (runs/flow_outer.json, 8948 cells, complete_region True, 6629 s): on 3413 <= r <= 8.244e10, X.V/r^2 >= 5.55636,
  V_2/y >= 5.56640, V_1/x >= 5.5741 on the axis cells (all above x_*; raw aggregate 5.5741666), T_0 <= -0.2782 (all cells are off B_1), no unresolved cells, no
  axis-sign failures (raw aggregates; rounded outward).
  INNER CELLS DONE (runs/flow_inner.json, 2632 cells, complete_region True, 1789 s): on 5.1555e-5 <= r <= 0.0076514, V_2/y >= 21.30140 (raw aggregate 21.3014052; the earlier 21.30141 was inward, corrected 00:4xZ after the verifier's note),
  V_1/x <= -10.1507 on the axis cells (all below x_*), T_0 <= -6.6519, no unresolved cells, no axis-sign failures.
  WHOLE-QUADRANT STATEMENT (all of Q = {x > 0, y > 0} covered by the two tails and the 19389 radial cells x 200+ angular cells, no gaps;
  runs/flow_summary_all.txt; notes/TO_TEAM.md 23:4xZ): (Y) with m_0 = 0.98845; (H2') axis signs with the single zero x_*; (H3) as above;
  (H4) with R_0 = 20, kappa_0 = 3.4957 (R_0 = 30: 4.2564); B_1: T_0 <= 1.2780, V_1 <= -12.834; off B_1: T_0 <= -0.2399 (middle), -0.2782
  (outer cells), -0.2807669 (outer tail), -6.6519 (inner cells), -6.652087 (inner tail). Implied cost bound (lead's Corollary):
  ||R_-|| <= 6.31 at kappa = 0.2 and <= 5.76 at kappa = 0.22 (verifier-confirmed instances, conditional on their acceptance of the
  whole certificate).

## 7.7 N8: derivative bounds of V and rho~ on B_{3 delta}(P) (RIGOROUS) and cut-off Sobolev norms of the residual (floating) (shift 3)
Request (lead 00:06Z, SPEC v3.17 section 3.15 (S2), (S4)): on the balls B_{3 delta}(P), P = (x_*, 0), delta in {0.0165, 0.05, 0.1, 0.2}, the suprema
M_V = sup ||D^2 V||_F, M_rho = sup ||D^2 rho~||_F, sup ||D^j V||_F (j = 3, 4), sup ||D^j rho~||_F (j = 3, 4, 5), with
||D^j f||_F^2 = sum_{a+b=j} C(j,a) (d_x^a d_y^b f)^2 (Frobenius norm over all index tuples; for V summed over both components), and
C_V = 41.7 M_V + 3 M_rho against kappa/(2 delta) = 1.687/delta; plus the floating ||tau eps~||_{H^{3.1}} for a smooth radial cutoff tau = 1 on
B_{7 delta/4}(P), supported in B_{9 delta/4}(P). Objects: the certified trial rho~ (data/trial_v2_h0.008.npz), V = c_l X + grad^perp psi~ with
psi~ its canonical inverse, c_l = 1/k. Parity: rho~ and psi~ are odd in y, so every |d_x^a d_y^b rho~|, |d_x^a d_y^b psi~| is even in y and the
quadrant theta in [0, theta_max] covers the ball.

### 7.7a RIGOROUS upper bounds (src/cert_n8.py)
Method. (1) Radial sub-cells of data/cert_green.npz (the certified Arb data of the trial: A_n, B_n at every sub-cell start, exact spline
polynomials of the a_m); on each sub-cell [t_a, t_a + h] the Taylor models (degree 12 in sigma = t - t_a, with remainder) of psi_n^{(i)} and
R_j^{(i)}, i <= 5, by exactly the construction of cert_resid._cell_core_deriv (A' = -2n A + g, B' = 2n B - g differentiated exactly; the
R_j^{(i)} are exact exponential-polynomials; the ODE remainder hypothesis 2 Nf h <= 1 is asserted per cell). (2) Each sub-cell is split into KSUB
equal sub-intervals; on each, two-sided ranges of every mode derivative by the re-centred Bernstein enclosure plus remainder (an MR interval per
(sub-interval, mode, i)). (3) Angular cells [theta_k, theta_{k+1}], theta_k = k theta_max/ntheta (exact reals as Arb balls); the ranges of
sin(f theta + l pi/2) (f = 2j+1 for rho~, 2n for psi~, f = 1 for the coordinate factors; l <= 6) are Arb enclosures of sin and cos on the ball
covering the cell (rigorous, second-order tight at critical points). (4) The (t, theta)-jets d_t^i d_theta^l rho~ = sum_j R_j^{(i)} (2j+1)^l
sin((2j+1) theta + l pi/2), and likewise for psi~ with 2n, as rigorous sums (midrad.MR.sum) of interval products over the modes, on every
(sub-interval x angular cell). (5) Cartesian derivatives by the exact recursion d_x = e^{-t}(cos th d_t - sin th d_th),
d_y = e^{-t}(sin th d_t + cos th d_th) applied to the interval jets (the same recursion as the floating TrialJets.polar_to_cart; the coefficient
fields e^{-t}, cos(th + b pi/2), sin(th + b pi/2) are interval ranges over the cell); d^alpha V_1 = -d^alpha psi~_y, d^alpha V_2 = d^alpha psi~_x
for |alpha| >= 2 (plus c_l on the diagonal for |alpha| = 1). (6) Frobenius norms from the magnitudes (|mid| + rad) of the entries, per cell; a cell
counts for the ball B_{3 delta}(P) if a RIGOROUS lower bound of its distance to P is <= 3 delta (over-inclusion is safe): for th1 >= 0 the
distance to P = (x_*, 0) increases with theta at fixed r, so dmin^2 = dist(x_* cos th1, [r1, r2])^2 + (x_* sin th1)^2, evaluated in mid-rad
arithmetic with x_* the certified bracket, cos th1 and sin th1 as Arb enclosures at the exact lower edge of the angular cell and r1, r2 the Arb
bounds of e^t over the radial sub-interval; the maximum over the counted cells is the bound. The radial sub-intervals used for the mode ranges
and for the coordinate factor e^{-t} are the same exact intervals I_kk = [kk hk_f, (kk+1) hk_f], hk_f = succ(h/KSUB), whose union contains
[0, h]. Coverage: r in [7.99935, 9.20025] (sub-cells 4027..4166, abutting; upper(t_start) <= lower(log(x_* - 0.6)), lower(t_end) >=
upper(log(x_* + 0.6))) and theta in [0, theta_max] with theta_max an exact double >= upper(asin(0.6/x_*)) x 1.000001 (= 0.069824; the tangent
angle of the ball seen from the origin) contain B_{0.6}(P) and hence all four balls; a run reports only the balls its cells cover (code v2,
2026-10-21T01:1xZ, after the verifier's preliminary audit; the v1 outputs, archived as runs/n8/*_v1.json, used a floating filter inflated by
1 + 1e-6 and gave the same numbers). All arithmetic: src/midrad.py (mid-rad float64 with outward
rounding; the dot-product model audited by the verifier, topic 72) and Arb (python-flint, 128 bits) for e^{-t}, sin, cos, asin, log.

Results (code v2; runs/n8/cert_n8_full.json: 140 radial sub-cells, KSUB = 4, ntheta = 350, 1030 s wall under the box CPU guard; the 0.0165 row
from the finer pass runs/n8/cert_n8_fine0165.json: 13 sub-cells r in [8.5495, 8.6564], KSUB = 16, ntheta = 160 on [0, 0.005756], 95 s; the
coarse-pass values for the 0.0165 ball are M_V <= 0.30302, M_rho <= 0.47929, C_V <= 14.07, also valid. The v2 outputs agree with the archived v1
outputs (runs/n8/*_v1.json, floating filter inflated by 1 + 1e-6) to 1.3e-10 relative (full) and 4e-11 (fine), with identical counted-cell
numbers 1141 / 10176 / 40395 / 156565 and 24457, which the referee reproduced independently):

| delta | cells counted | M_V = sup\|D^2 V\|_F | sup\|D^3 V\|_F | sup\|D^4 V\|_F | M_rho = sup\|D^2 rho~\|_F | sup\|D^3 rho~\|_F | sup\|D^4 rho~\|_F | sup\|D^5 rho~\|_F | sup\|DV\|_F | C_V | kappa_loc/(2 delta) (rounded down) | |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0.0165 (fine) | 24457 | 2.8728e-1 | 1.3675 | 3.7552e+1 | 4.5337e-1 | 4.3778 | 4.1256e+1 | 5.7777e+3 | 1.02056e+1 | 1.334e+1 | 1.0224e+2 | OK |
| 0.05 | 10176 | 3.9258e-1 | 3.0163 | 3.2099e+2 | 7.5436e-1 | 5.0524 | 3.4049e+2 | 5.6797e+4 | 1.02164e+1 | 1.864e+1 | 3.3740e+1 | OK |
| 0.1 | 40395 | 5.5723e-1 | 3.8805 | 4.4405e+2 | 1.2277 | 5.5480 | 4.7228e+2 | 7.9323e+4 | 1.02183e+1 | 2.692e+1 | 1.6870e+1 | FAIL |
| 0.2 | 156565 | 1.0948 | 4.4771 | 4.5941e+2 | 1.8184 | 5.5758 | 4.8109e+2 | 7.9323e+4 | 1.02229e+1 | 5.111e+1 | 8.4350 | FAIL |
| 0.05 (mid) | 57668 | 3.8293e-1 | 1.6644 | 1.5078e+2 | 7.2941e-1 | 4.4488 | 1.6010e+2 | 2.9289e+4 | 1.02123e+1 | 1.816e+1 | 3.3740e+1 | OK |
| 0.06 (mid) | 82953 | 4.1252e-1 | 2.0303 | 2.1928e+2 | 8.2209e-1 | 4.4488 | 2.3254e+2 | 3.6745e+4 | 1.02131e+1 | 1.967e+1 | 2.8116e+1 | OK |
| 0.07 (mid) | 112816 | 4.4309e-1 | 2.0582 | 2.1935e+2 | 9.1783e-1 | 4.4488 | 2.3290e+2 | 4.0399e+4 | 1.02136e+1 | 2.124e+1 | 2.4099e+1 | OK |
(Regenerated 2026-10-22 by `python3 src/report_tables.py --n8` with directed ceilings of the saved sup bounds and C_V; the threshold column is
kappa_loc/(2 delta) rounded down; the earlier table had about 30 nearest-rounded entries, referee astra/numrep4.)

The three "mid" rows are from runs/n8/cert_n8_mid.json (code v2; 52 radial sub-cells r in [8.38698, 8.81486], KSUB = 8, ntheta = 350 on
[0, 0.024421]; 1105 s wall under the CPU guard); they refine the 0.05 row and extend the certified admissible range of the lead's condition
C_V <= kappa_loc/(2 delta) to delta = 0.07 (21.24 <= 24.1). In floating point the condition fails from delta = 0.08 on (C_V 22.47 against 21.09,
runs/n8/n8_floating_scan.json), so delta = 0.07 is certified admissible and the floating scan places the failure of the SUFFICIENT condition
between 0.07 and 0.08 (a floating exclusion estimate of the test, not a certified counterexample to the underlying condition). Every rigorous entry is >= the sampled supremum
(ratios 1.02-1.03 at order 2, up to 8.4 at order 5 for these KSUB = 8 runs).

All entries are upper bounds, rounded up at the fifth significant digit. Largest Taylor-model remainders over the 140 cells: A, B 1.1e-15;
psi^{(5)} 1.9e-5; R^{(5)} 1.9e-22. Consequences for SPEC 3.15 (if E <= C_V delta as in (S2)): at delta = 0.0165, E <= 0.2202 and
K_1 = 1/(kappa_loc - E) <= 1/(3.374 - 0.2202) <= 0.3171 (E <= C_V delta <= 13.34 x 0.0165 <= 0.2202); at delta = 0.05 the coarse run gives
E <= 18.64 x 0.05 = 0.932 and K_1 <= 1/(3.374 - 0.932) <= 0.40951, the mid run E <= 18.16 x 0.05 = 0.908 and K_1 <= 0.40552; delta >= 0.1 is NOT
certified by this sufficient test (the test fails there, and the sampled values below show the condition itself failing in floating point). Location of the maxima: on the 0.0165 ball |D^2 V| peaks at r in [8.5495, 8.5515], theta in
[0.00100, 0.00120] (the inner edge of the ball near the axis) and |D^2 rho~| at r in [8.5740, 8.5761], theta in [0.00499, 0.00519]; on the
0.05 ball |D^2 V| peaks at r in [8.4496, 8.4517], theta in [0.0024, 0.0026]: M_V grows with delta through the inner (saddle-side) edge, not
through a feature at P.

### 7.7b FLOATING sampled suprema (src/n8_floating.py, runs/n8/n8_floating.json; evidence only)
Polar grid dt = dth = 1e-4 over the same region (1399 x 700 points), analytic jets to order 5 (src/trial_jets.py), sampled suprema on the
grid points inside each ball (no remainder):

| delta | points | M_V | sup\|D^3 V\| | sup\|D^4 V\| | M_rho | sup\|D^3 rho~\| | sup\|D^4 rho~\| | sup\|D^5 rho~\| | sup\|DV\| | C_V |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0165 | 5265 | 0.28222 | 1.2574 | 22.996 | 0.44591 | 4.3116 | 25.185 | 2314.4 | 10.203 | 13.11 |
| 0.05 | 47967 | 0.37361 | 1.2928 | 46.118 | 0.71176 | 4.3116 | 47.054 | 4797.3 | 10.208 | 17.71 |
| 0.1 | 191607 | 0.54008 | 1.6225 | 91.372 | 1.1867 | 4.3116 | 95.244 | 9101.4 | 10.21 | 26.08 |
| 0.2 | 767136 | 1.0808 | 3.1396 | 291.44 | 1.7801 | 4.3695 | 289.71 | 31519 | 10.21 | 50.41 |

Consistency: every rigorous bound is >= the sampled supremum on the same ball (checked programmatically for all entries; the referee
confirmed it for every common entry, see below). Ratios rigorous/sampled: 1.00-1.07 for DV, D^2 V, D^2 rho~ (1.02 on the fine 0.0165 pass);
D^3 rho~ 1.02 (fine) to 1.29; D^3 V 1.09 (fine) to 2.4; D^4 V and D^4 rho~ 1.6 (fine) to 7.2; D^5 rho~ 2.5 (fine) to 11.84. The looseness
at high order comes from the interval widths of the fifth-order jets over the sub-cells (frequency powers magnify the angular widths, modewise
interval products lose cancellation, repeated differentiation adds dependency) and shrinks with KSUB and ntheta, as the fine pass shows.

Referee (astra n8ref1, notes/astra_n8ref1_answer.md, on the v1 code): CONFIRMED the Bernstein re-centring and scaling (and checked all 134676
affected coefficient products against exact rational targets), the angular phase bookkeeping and outward conversions, the mode-sum jets and
the exact representability of f^l (exhaustively compared with integer powers), the Leibniz recursion (agrees with TrialJets.polar_to_cart) and
its pointwise-containment justification, the V derivatives, the Frobenius weights, the e^{-t} union enclosure, the parity reflection, and
independently reproduced the inclusion counts (1141, 10176, 40395, 156565 coarse; 24457 fine) with certified exclusions of all other cells
(squared-distance excess > 1.2e-6 coarse, > 9.65e-8 fine). REFUTED (v1): the fine output's entries for delta > 0.0165 (not covered; a certified
counterexample point Q = (8.60719, 0.14978) has rho~(Q) = 4.45 against the listed 1.48), the floating dmin (overestimate by 3.3e-14, not a lower
bound), the self-comparing adjacency assertion and a dead assertion, and the ball xs built from the double bracket (it misses the printed decimal literals
by 4e-16; the certified object is the pair of doubles stored in runs/axis_cell.json, which the ball does contain; v2 uses a radius one ulp
larger; the decimal literals are display values, not the certified object). All of these are repaired in v2 (entries for delta > delta_max are dropped; rigorous MR
filter; contiguity assertion; dead assertion removed); the v2 fine pass reproduces the v1 numbers exactly.
Referee round 2 (astra n8ref2, notes/astra_n8ref2_answer.md, on the v2 code and the three v2 outputs): CONFIRMED the v2 coverage and filter
changes for all three runs (independent Arb checks of the radial and angular coverage with margin > 2e-5 in t, of every excluded cell with
exact rational arithmetic, 374880 squared-distance steps; counted cells 1141/10176/40395/156565, 24457, 57668/82953/112816 reproduced),
the common sub-interval construction (every shift enclosed; K hk_f = succ(h_up) > h_up by binary scaling), the tangent-angle formula and the
downward rounding of the filter; and gave the clean justification of the sub-interval ranges: at every sigma in J_kk = I_kk n [0, h] the
polynomial part lies in its Bernstein range over I_kk and the Taylor remainder (derived on [0, h_up]) applies, and the union of the J_kk is
[0, h]; the remainder is never used beyond h (the referee's counterexample sigma^13 shows that a Taylor model does NOT automatically extend
to the one-ulp overhang, which is why this restriction matters). Robustness items for general inputs (no effect on the supplied runs, each
verified directly in Arb by the referee): the delta filter tolerance (1 + 1e-12) could admit d one ulp above delta_max; the double
conversions of the coverage bounds t_lo_need/t_hi_need and of r_lo/r_hi were not forced outward (they happened to be exact or inward by
< 2e-16, against margins > 2e-5); the coverage assertion compared a float conversion. These are repaired in code v3 (arithmetic unchanged;
runs/n8/cert_n8_fine0165_v3.json, 88 s: identical sup_bounds, counted cells and per-cell maxima to the v2 file; only the reported r
intervals of the maxima are one ulp wider). The frozen certificate files remain the v2 outputs pinned by the verifier; v3 is the code to use
for any new run. The x_* ball covers the certified double bracket (axis_cell.json) but not the exact decimals of its shortest representation
(4e-16 outside); the double pair is the certified object.

### 7.7c Cut-off residual norms near P (FLOATING, src/pdisc_fft.py; evidence only)
tau(X) = Q((|X - P| - 7 delta/4)/(delta/2)) with Q the C^infty step Q(u) = e^{-1/(1-u)}/(e^{-1/(1-u)} + e^{-1/u}) on 0 < u < 1, extended by Q = 1 for
u <= 0 and Q = 0 for u >= 1 (so tau = 1 on B_{7 delta/4}(P), supp tau in B_{9 delta/4}(P); a different, smooth cutoff from the degree-9 polynomial one of
7.10); f = tau eps~ on a Cartesian grid of
spacing dx = delta/300 (box half-width 1.25 x 9 delta/4, n = 2048), eps~ from the residual modes on a dt = 1e-5 grid (degree-7 interpolation in
t) summed with sin((2N+1) theta); ||f||_{H^s}^2 = (2 pi)^{-2} int (1 + |xi|^2)^s |f^(xi)|^2 dxi with the UNNORMALIZED transform f^(xi) = int f(X)
e^{-i xi.X} dX (the same norm as the unitary-transform formula of 7.10) by FFT (runs/n8/fft_delta*.json):

| delta | sup\|tau eps~\| | L^2 | H^2 | H^3 | H^{3.1} | H^{3.5} | H^4 | H^4/H^3 | fraction of H^3 norm^2 above \|xi\| = 800 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0165 | 3.31e-7 | 8.58e-9 | 7.08e-4 | 0.743 | 1.558 | 32.3 | 1628 | 2190 | 0.843 |
| 0.05 | 3.00e-6 | 1.67e-7 | 1.80e-3 | 0.573 | 1.065 | 13.7 | 394 | 690 | 0.186 |
| 0.1 | 5.84e-6 | 5.98e-7 | 2.95e-3 | 0.476 | 0.811 | 7.16 | 125 | 263 | 0.006 |
| 0.2 | 1.01e-5 | 2.04e-6 | 6.46e-3 | 0.823 | 1.373 | 10.9 | 149 | 181 | 0.000 |

Grid check (delta = 0.0165): dx = delta/100 (n = 1024) and dx = delta/600 (n = 4096) give the same L^2, H^3, H^{3.1}, H^4 to four digits
(8.575e-9, 0.7429, 1.5577, 1628) and the same high-frequency fraction 0.843: the values are converged and are not floating-point roundoff.
Reading: delta x H^4/H^3 is 36.1, 34.5, 26.3 and 36.2 at the four delta (ratios 2190, 690, 263, 181), consistent with a substantial contribution from the localization (the cutoff acting on
the values of the residual; the derivatives of tau scale like (2/delta)^s) rather than from a feature at P; the split between cutoff
derivatives and residual variation is not identified by these norms. Shrinking the ball does not make ||tau eps~||_{H^{3.1}} small: it stays
of order 1 while sup|tau eps~| on the ball falls from 1.0e-5 (delta = 0.2) to 3.3e-7 (delta = 0.0165). A
small local forcing norm in the sense of SPEC 3.15 needs a much smaller sup|eps~| near P (the trial's residual there is 1e-7 .. 1e-5), not a
smaller ball. These are floating values (sampled field, discrete Fourier transform), cited as evidence only.

Decomposition of the localized forcing (lead's N10, 04:57Z; own code src/forcing_decomp.py, runs/n10/*.json; FLOATING): model = least-squares
polynomial in (x - x_*, y), odd in y, degree <= 5, fitted on supp tau. The 'Gaussian window' column is ||w eps~||_{H^s} with w = exp(-|X - P|^2 /
(2 sigma^2)) for the listed sigma, the field set to zero outside the radius min(max(r2, 8 max sigma), 0.999 Lb) of the window box (for the saved run
Lb = 0.16, sigma <= 0.02 this clamp cuts at 7.99 sigma, where the Gaussian is 1.4e-14); a truncated discrete-FFT diagnostic, not a Sobolev
truncation-error estimate.

| scale | ||tau eps~||_{H^3.1} | ||tau model|| | ||tau (eps~ - model)|| | relative rms misfit | Gaussian window ||w eps~|| |
|---|---:|---:|---:|---:|---:|
| delta = 0.0165 (tau: 7/4, 9/4 delta; boxes 0.08/N256 and 0.16/N512 agree) | 1.5521 | 1.5587 | 0.6138 | 0.325 | 0.02878 (sigma 0.01), 0.04218 (sigma 0.02) |
| 0.5-disc (tau = 1 on B_0.39, 0 outside B_0.5; box 0.8/N1024) | 1.4526 | 0.0143 | 1.4520 | 0.996 | 0.260 (sigma 0.1) |

At delta = 0.0165 the linear model y d_y eps~(P) with the certified d_y eps~(P) = (mu~ - 1) g = -6.702e-7 has norm 0.1210; the H^{3.1} energy
fraction above |xi| = 1000 is 0.766 (above 3000: 0.179); ||tau||_{H^3.1} = 7.65e6. The lead's values (1.56, 0.61, 0.029, 0.042, 0.12) are
reproduced. The normalization ratio ||tau eps~||_{H^3.1} / (||tau||_{H^3.1} sup|tau eps~|) is 0.615 at delta = 0.0165 (lead: 0.61-0.65 across
delta = 0.0165, 0.033, 0.066) and 4.28 on the 0.5-disc. Reading (the model/remainder split is not orthogonal, so it does not identify how much
of the norm comes from the derivatives of the cutoff versus the variation of the residual): on the small ball the numbers are consistent with a substantial contribution from the
localization (the cutoff acting on the values of the smooth part of eps~); on the 0.5-disc the polynomial part is 1 percent of the norm and
the non-polynomial knot-scale structure carries it (7.5). The knot-scale attribution of 7.5 therefore applies to the 0.5-disc (and larger)
norms, not to the small cut-off balls.

## 7.8 X3 minus the trial: the four jets at P (FLOATING, evidence only; lead's request 01:51Z; shift 3)
h = X3 - rho~ with X3 from its exact formula (src/x3.py) and rho~ the STORED trial (data/trial_v2_h0.008.npz as stored, floating evaluation; not the
exactly normalized trial of the certificates, whose exactification changes A_00; lead 22:54Z); on a log-polar grid r in [7.65e-4, 7.65e5] (Nr x Nt =
6000 x 256 and 12000 x 512), U[h] and the raw strain c_raw[h] := psi[h]_xy(0) = 3 c[h] (the prompt's c[h] = psi[h]_xy(0)/3 is used everywhere else in
this report; in this subsection 'c[h]' values are raw strains) by the grid modal Green inverse (src/inverse.py, power-law tail fit);
axis jets by modal sums, cubic splines in t at x_* (src/x3_minus_trial_jets.py; runs/jets/x3_minus_trial_N*.json). Definitions: z = h_y(P),
v = h_xy(P), u = W[h]_1(P) = U_1[h](P) + x_* c[h]/3, w = d_y W[h]_2(P) = d_y U_2[h](P) + c[h]/3 (on the axis U_1 = -sum_n 2n psi_n/r,
d_y U_2 = sum_n 2n (psi_n/r)').

| grid | c[h] | z = h_y(P) | v = h_xy(P) | U_1[h](P) | d_y U_2[h](P) | u = W[h]_1(P) | w = d_y W[h]_2(P) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 6000 x 256 | -1.02774e-8 | -5.428e-9 | -3.60e-10 | 4.4761e-8 | 2.194e-9 | 1.5299e-8 | -1.232e-9 |
| 12000 x 512 | -1.03011e-8 | -5.581e-9 | +2.93e-10 | 4.5356e-8 | 2.091e-9 | 1.5826e-8 | -1.343e-9 |

The fine grid's c[h] agrees to five digits with the FLOATING difference c[X3] - c~[rho~] = about -1.0301e-8 (c[X3] from the floating
evaluators of sections 2 and 3, 15.72608777 to 15.72608782; c~ certified in 7.2; no certified enclosure of this X3-minus-trial difference exists); z, u, w are
stable to 3-4 percent between the grids; v is at the resolution floor (sign flips). Reading: in these four quantities X3 lies within about
1.6e-8 of the trial (|u| = 1.6e-8, 0.7 of the radius 2.2e-8 of the lead's trial-centred jet exclusion; |z| = 5.6e-9, |w| = 1.3e-9,
|v| < 4e-10), so X3 is plausibly inside that ball; X3's own canonical source point would sit at x_* - u/w'(P) = x_* - 1.56e-9. sup|h| on the
grid is 1.53e-7 (1.5e-10 of sup|rho|). Floating: the velocity of h is a grid inverse (relative accuracy about 1e-9 on the big fields, which
is why the direct V_1^{X3}(x_*, 0) from the inverse of the full X3 density, 1.7e-7 to 2.3e-7, is not usable; the difference-based u is).

## 7.9 N9: the constants R and E of the auxiliary source inverse at P (FLOATING, independent code; lead's request 02:42Z; shift 3)
src/aux_R.py reproduces, with the trial's modal representation (fine t grid, degree-7 interpolation to the Cartesian points, exact angular
sums) and spectral derivatives, the constants of FR 5(o) / SPEC 3.15 (S2)-(S3) at delta = 0.0165, s = 3.1, cutoff theta = chi(|X - P|) with
chi = 1 on [0, 2 delta], 0 on [3 delta, inf) (e^{-1/t} step), w = theta (V - diag(A_P, mu)(X - P)) with A_P = 10.1507252438 (the floating value of w'(P) = d_x V~_1(P), section 7.2; not A = 2 c_l - 1 of 7.2) and mu = d_y V~_2(P), q = theta (grad rho~ - (0, g)), unitary FFT,
W_r(f) = (2 pi)^{-1} int <k>^r |f^|, P_s(f) = s 2^{s-2} (W_1(f) + alpha_{s-1} ||f||_{H^s}), T_s(w) = s(s-1) 2^{s-4} sum_i (W_2(w_i) + beta_{s-1} ||w_i||_{H^s}) with
alpha_r = 1/(2 sqrt(pi (r-1))) for r > 1 and beta_r = 1/(2 sqrt(pi (r-1)(r-2))) for r > 2 (src/aux_R.py),
R = T_s(w) + P_s(q_1) + P_s(q_2), E = ||div w||_inf/2 + s ||Dw||_{inf,F} + ||q||_inf (runs/n9/aux_R_n{256,512}.json):

| grid | ||q_1||_{H^s} | ||q_2||_{H^s} | ||w_1||_{H^s} | ||w_2||_{H^s} | W_1(q_1), W_1(q_2) | W_2(w_1), W_2(w_2) | T_s(w) | P_s(q_1), P_s(q_2) | R | E |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 256^2 (dx 6.25e-4) | 1.16305e4 | 1.21143e4 | 182.404 | 86.9913 | 5.71982, 6.43428 | 52.3252, 23.5711 | 1064.13 | 2.08250e4, 2.16945e4 | 4.35836e4 | 0.070497 |
| 512^2 (dx 3.125e-4) | 1.16311e4 | 1.21151e4 | 182.417 | 86.9936 | 5.72137, 6.43611 | 52.5176, 23.6390 | 1065.09 | 2.08262e4, 2.16958e4 | 4.35871e4 | 0.070538 |

The lead's values (code/aux_R.py in the lead's lane: 1.163e4, 1.211e4; 182, 87; 5.7, 6.4; 52, 24; 1064; 2.08e4, 2.17e4; R 4.36e4; E 0.0705) are
reproduced to the printed digits; between the two grids R changes by 8.0e-5 relative (4.35836e4 / 4.35871e4) and E by 5.8e-4 (0.070497 /
0.070538), while the Wiener quantities W_2(w_i) differ by up to 0.4 percent (52.3252 / 52.5176). E = 0.0705 here is the actual value of the energy
perturbation for this cutoff (compare the Taylor bound E <= C_V delta <= 0.2202 of section 7.7, an upper bound for every cutoff of the SPEC 3.15
class with derivative constant C_theta = 2, the constant that enters SPEC's coefficient 41.7 of 7.7a);
R = 4.36e4 enters the auxiliary inverse norm bound (1/a_s)(1 + R/(a_0 - a_s))^s of SPEC 3.15 (S6): with a_s = kappa_loc - E = 3.374 - 0.0705 = 3.3035
and d = a_0 - a_s = 1 + (A_P + mu)/2 - kappa_loc + s ||Dw||_inf,F = 3.2553 it is 1.9e12 at s = 3.1 (floating), i.e. the auxiliary inverse is bounded
but with a uselessly large constant in the unscaled H^{3.1} norm. The lead's dilation corollary (V31; verified, FINAL_REPORT timeline 2026-10-21 03:03) rescales the operator
by D_ell u(Y) = u(P + ell Y): R~(ell) uses W_r(f~) = (2 pi)^{-1} int <ell k>^r |f^| dk, ||f~||_{H^s} = ell^{-1} (int <ell k>^{2s} |f^|^2)^{1/2} with an
extra 1/ell for the components of w, and the forcing is measured in N_{1/ell}(f)^2 = int (ell^{-2} + |k|^2)^s |f^|^2 dk. With the same code
(runs/n9/aux_R_n{256,512}.json; tau = 1 on B_{7 delta/4}(P), supported in B_{9 delta/4}(P)):

| ell | R~(ell) | (1 + R~/d)^s/(kappa_loc - E) | N_{1/ell}(tau eps~) | bound x forcing |
|---|---:|---:|---:|---:|
| 1 | 4.3584e4 / 4.3587e4 | 1.879e12 / 1.880e12 | 1.5521 / 1.5576 | 2.92e12 / 2.93e12 |
| 0.0165 | 22.550 / 22.566 | 185.5 / 185.9 | 1.5590 / 1.5645 | 289.2 / 290.8 |
| 0.01 | 11.809 / 11.818 | 34.96 / 35.03 | 1.5716 / 1.5770 | 54.95 / 55.25 |
| 0.005 | 6.0253 / 6.0300 | 7.789 / 7.801 | 1.6437 / 1.6489 | 12.80 / 12.86 |
| 0.0035 | 5.4356 / 5.4389 | 6.355 / 6.362 | 1.7918 / 1.7966 | 11.39 / 11.43 |
| 0.0025 | 6.4672 / 6.4695 | 8.997 / 9.004 | 2.2693 / 2.2731 | 20.42 / 20.47 |
| 0.0015 | 12.382 / 12.384 | 39.26 / 39.27 | 5.9501 / 5.9515 | 233.6 / 233.7 |

(256^2 / 512^2 grids.) The lead's floating values (R~ 22.6, 11.8, 6.0, 5.4; bounds 186, 35, 6.4; forcing 1.565, 1.577, 1.649, 1.797, 2.27, 5.95) are reproduced. The localized forcing is
insensitive to ell for ell >= 0.005 (1.55 to 1.65 on the fine grid: its spectral content sits at |k| ~ 1e3, above 1/ell there, see 7.7c) and rises for smaller
ell (1.80 at 0.0035, 2.27 at 0.0025, 5.95 at 0.0015), so the product "inverse bound x forcing",
which a local closing condition would compare with the radius, is at best 11.4 (ell = 0.0035): not small. Floating evidence only.

## 7.10 Rigorous upper bound of the localized forcing norm at P (this lane's computation, RIGOROUS method; verifier topic 122 on the final v2.2: CONFIRMED finite components, physical forcing norm OPEN; topics 115/117 audited the superseded v1.0; shift 4; src/cert_forcing.py, src/cert_forcing2.py; runs/forcing/)
Quantity (SPEC 3.15, the forcing term of the lead's local source estimate, previously evaluated only in floating point in SPEC/FR; the FR now carries
the conditional certificate values): F_s = ||tau eps~||_{H^s} with
s = 31/10, the inhomogeneous norm ||f||_{H^s}^2 = int (1 + |xi|^2)^s |f^(xi)|^2 dxi (unitary Fourier transform), and the dilated norm
N_lam(f)^2 = int (lam^2 + |xi|^2)^s |f^|^2 at lam = 500 (= N_{1/ell} at ell = 1/500, the scale of the verifier's certified auxiliary inverse
bound, SPEC 3.15 / 7.9). Cutoff: tau(X) = S(sigma), sigma = (|X - P| - 7 delta/4)/(delta/2), S(sigma) = step(1 - sigma),
step(u) = 126 u^5 - 420 u^6 + 540 u^7 - 315 u^8 + 70 u^9 on 0 < u < 1, step = 0 for u <= 0 and 1 for u >= 1 (the lead's tau_poly9; C^4; tau = 1 on B_{7 delta/4}(P), supp tau in B_{9 delta/4}(P),
admissible for SPEC 3.15), delta = 33/2000 exactly, P = (x_*, 0) with x_* in the certified bracket [8.60006380515688, 8.600063805157474] of 7.2
(these are the binary64 numbers of runs/axis_cell.json; the S1 ball 8.600063805157177 +/- 2.9402020296740933e-13 lies inside; asserted in the code). The
residual eps~ is that of the X3 trial rho~ (data/trial_v2_h0.008.npz, Arb data data/cert_green.npz).
Method (docstrings of src/cert_forcing.py (v1) and src/cert_forcing2.py (v2)): (1) Hoelder in the Fourier variable,
(lam^2+|xi|^2)^{3.1} = [(.)^3]^{0.9} [(.)^4]^{0.1}, so N_lam^2 <= I3^{0.9} I4^{0.1} with I3 = lam^2 ||(lam^2 - Lap) f||_2^2 + ||grad (lam^2 - Lap) f||_2^2
and I4 = ||(lam^2 - Lap)^2 f||_2^2 (Plancherel; f = tau eps~ is in W^{4,infty} with compact support). (2) The L^2 norms are bounded by sums over
polar sub-cells about the origin (13 spline sub-cells of the certificate x 16 angular cells, each split 64 x 8) covering B_{3 delta}(P)
(coverage asserted as in 7.7) of area x sup^2, the lower half-plane by parity. (3) The Cartesian derivatives of eps~ (|alpha| <= 4) from
BIVARIATE Taylor models in (t - t_a, theta - theta_c): the per-mode Taylor models of d_t^i eps_N (i <= 4; cert_resid._cell_core_deriv, the same
objects as the derivative certificate 7.3b) summed over the modes with the Taylor coefficients of (2N+1)^j sin((2N+1)(theta_c + phi) + j pi/2) in
phi (Arb values at theta_c; remainder (2N+1)^{j+9} w^9/9!), which keeps the angular cancellation that the Wiener sums W_i_j of 7.3b lose; the
Cartesian recursion of 7.7 applied to the bivariate models; suprema by tensor-Bernstein coefficients on the sub-cells after exact re-centring.
(4) v1: pointwise Leibniz bounds for f = tau g (g = eps~) in terms of products of suprema (tau's radial derivatives from the exact integer
polynomials S^{(j)}, Arb ranges on each sub-cell's sigma range in centred form, rho >= max(dist_min, 7 delta/4)). v2: on each block (2 x 2 per
cell) tau and all its Cartesian derivatives are bivariate Taylor models too (q = |X - P|^2 as a BiTM; q^{-1/2} by the binomial series with a
certified tail; sigma and S^{(j)}(sigma) by exact polynomial composition; d^k/dq^k by Faa di Bruno; D^alpha tau = sum_k S^_k P_{alpha,k}(u, v)
with symbolic integer polynomials), the Leibniz products f, grad f, Lap f, grad Lap f, Lap^2 f are formed exactly as BiTMs and bounded per fine
sub-cell; sub-cells entirely inside (tau = 1) use the bounds of g, sub-cells straddling the ends of the transition use the v1 bounds. All
arithmetic rigorous (src/midrad.py mid-rad float64 with outward rounding; Arb for transcendental values; Arb with the exact exponents 9/20,
1/20 in the final Hoelder step).

RESULTS (delta = 33/2000, cutoff p9; 13 radial cells ci 4096..4108, r in [8.54945, 8.65643], theta_max 0.0057558, 16 angular cells, fine
sub-cells 64 x 8 per cell, Qs = 12, Qp = 8; v2: blocks 2 x 2 per cell, series length 16, regimes inside 26079 / transition 16502 / straddle 1368 /
outside 62547 sub-cells; floating values from src/forcing_float.py, FFT on a 4096^2 grid, dx = 2.27e-5). ROUNDING: every rigorous decimal in the
two tables below is rounded UPWARD (a ceiling of the stored JSON value); the floating values are rounded to nearest and are not bounds:
| quantity | RIGOROUS v2.2 upper bound (runs/forcing/v22_p9_merged.json) | RIGOROUS v1.2 upper bound (runs/forcing/v12_p9_merged.json) | floating (FFT) |
|---|---:|---:|---:|
| ||tau eps~||_{H^3} | 0.7759 | 1.0446 | 0.6646 |
| ||tau eps~||_{H^4} | 893.16 | 1243.17 | 753.65 |
| ||tau eps~||_{H^{3.1}} | **1.5700** | 2.1207 | 1.3296 (lead's floating 1.33 reproduced; Hoelder bound of the floating I3, I4: 1.3428) |
| N_500, order 3 | 1.8107 | 2.1083 | 1.6172 |
| N_500, order 4 | 1638.56 | 2107.72 | 1308.9 |
| N_500(tau eps~), order 3.1 | **3.5769** | 4.2064 | 3.1128 |
Second cutoff shape (same method, v2.2, 26 half-cell runs 09:22Z-09:43Z; runs/forcing/v22_p11_merged.json, SHA-256
48d02b93a9c4d6f2db458df247473c642b61efb3ace66738ab67fef3460e8d1c; floating runs/forcing/float_p11_dx90.json, FFT 2048^2, dx 4.5e-5): the C^5 degree-11
step p11, step(u) = 462 u^6 - 1980 u^7 + 3465 u^8 - 3080 u^9 + 1386 u^10 - 252 u^11 on 0 < u < 1, 0 below and 1 above (same radii 7 delta/4, 9 delta/4). Ceilings (rounded UPWARD) and floating:
| quantity (p11 cutoff) | RIGOROUS v2.2 upper bound | floating (FFT) |
|---|---:|---:|
| ||tau eps~||_{H^3}, H^4, H^{3.1} | 1.4436, 1605.54, **2.9112** | 0.8253, 1015.0, 1.6663 |
| N_500: order 3, order 4, order 3.1 | 2.4697, 2587.88, **4.9508** | 1.7348, 1576.6, 3.3693 |
(stored: 1.4435908732415141, 1605.5390013838633, 2.9111313478268608; 2.46965764535627, 2587.8751684282747, 4.9507091269616197). The steeper C^5 step
has a larger forcing norm (floating 1.67 against 1.33) and a larger sup-based loss (factor 1.75 against 1.18): the p9 cutoff is the better choice
for the local estimate, and both are admissible for SPEC 3.15 (tau = 1 on supp chi_loc, the local cutoff of SPEC 3.15 supported inside B_{7 delta/4}(P),
not the N9 cutoff chi of 7.9; supp tau in B_{9 delta/4}; the (S4) constants use cutoff
derivatives through order 5, which both steps have in W^{5,infty}).
Rigorous suprema (upper bounds, rounded UPWARD) of |d_x^a d_y^b eps~| (identical in all versions v1.1-v2.2; sampled maxima of the floating evaluator on polar
grids in parentheses, rounded to nearest; every sample is inside its bound):
| alpha (a,b) | sup on B_{9 delta/4}(P) | sup on B_{3 delta}(P) |
|---|---:|---:|
| (0,0) | 5.055e-7 (4.997e-7) | 9.425e-7 (9.353e-7) |
| (1,0), (0,1) | 5.429e-5 (5.356e-5), 4.122e-5 (4.039e-5) | 7.624e-5 (7.581e-5), 6.299e-5 (6.221e-5) |
| (2,0), (1,1), (0,2) | 8.311e-3 (8.290e-3), 2.228e-3 (2.228e-3), 2.943e-3 (2.919e-3) | 9.136e-3 (9.082e-3), 2.967e-3 (2.959e-3), 3.535e-3 (3.532e-3) |
| (3,0), (2,1), (1,2), (0,3) | 1.495 (1.486), 0.3289 (0.3289), 0.1381 (0.1381), 0.1985 (0.1981) | 1.648 (1.647), 0.3289, 0.1381, 0.2063 (0.2063) |
| (4,0), (3,1), (2,2), (1,3), (0,4) | 280.9 (280.2), 54.57 (54.57), 13.63 (13.63), 7.371 (7.371), 10.74 (10.67) | 311.7 (311.1), 54.57, 13.63, 7.371, 12.70 (12.68) |
Every certified entry is the 4-significant-digit CEILING of the JSON value (the verifier found 22 of 36 entries of the first version rounded to
nearest, i.e. inward; corrected 08:33Z). Euclidean gradient bounds (from the two component suprema): |grad eps~| <= 6.816e-5 on B_{9 delta/4}(P),
<= 9.889e-5 on B_{3 delta}(P).
So the enclosures of the residual derivatives are tight (1-2 percent), and the rigorous H^{3.1} bound is within 18 percent of the floating
value (the remaining slack is the sup-versus-L^2 bounding on the fine sub-cells and the straddling sub-cells). The stored values behind the
ceilings (v2.2): I3 = 0.60188503371042545, I4 = 797718.94142901117, order-3 0.77581249906818694, order-4 893.15113022881599, order-3.1
1.569905786431367 (lam = 1); 3.2785862643663934, 2684872.1006275327, 1.8106866831029587, 1638.5579332533632, 3.5768864780441523 (lam = 500);
v1.2: 1.0909844782969449, 1545466.3072703849, 1.0445020240750831, 1243.1678516074912, 2.1206614142028606; 4.4446342205920883, 4442472.3427096438,
2.108230115663869, 2107.7173298878683, 4.2063697756527541. The v2.1 -> v2.2 and v1.1 -> v1.2 code changes (below) left the ceilings unchanged.
Consequences (with the verifier's certified constants; the forcing bound itself awaits their audit): K_1 < 0.3181 (ver topic 86) gives for the
first term of the local estimate (S4) at the trial, tau L h = -tau eps~ for the Newton correction, K_1 ||tau eps~||_{H^{3.1}} < 0.3181 x 1.5700
< 0.4995 (floating 0.42); the certified auxiliary inverse bound < 473 in N_500 (ver topic 97) gives ||A^{-1}(tau eps~)||_{N_500} < 473 x 3.5769
< 1691.9 (with the floating forcing: about 1472), an auxiliary-inverse response bound only. These quantify the forcing in the lead's local source
estimate; they are not a closing inequality (the local estimate is a priori, no global inverse exists, FINAL_REPORT section 10). The sup table is
also a rigorous C^4 bound of the residual near P
(for example |eps~| <= 9.425e-7, |d_x eps~| <= 7.624e-5, |d_y eps~| <= 6.299e-5, |grad eps~| <= 9.889e-5 on B_{0.0495}(P)).
History and referee round (shift 4). A first complete run (v1.0, runs/forcing/p9_K64_n16_P8_merged.json, 07:31Z) gave 5.6533 (N_500 8.8718);
the external referee round astra/forcing1 (answer 07:5xZ, astra/forcing1/answer.md) found: (1) N_500 quoted 8.8717 for the JSON value
8.87174795 (inward rounding); (2) the geometric angular sub-cells were shifted by w_up - dtheta/2 ~ 2.7e-20 from the Bernstein sub-cells (the
geometry now IS the Bernstein sub-cell, with the distance minimum at theta = 0 for sub-cells straddling the axis); (3) non-outward float
conversions of Arb bounds in Cutoff.quantities (fixed with outward conversions; its counterexample, a point just inside the outer radius
rejected as outside, no longer occurs); (4) the x_* bracket literals are binary64 numbers (documented and asserted against the S1 ball, above);
(5) a possible amplified underflow of the degree weights in the BiTM truncation bound (asserted away: weights > 2^-900); (6) finish() used a
float pow with the inexact exponent 0.45 (now Arb with the exact exponents 9/20, 1/20, outward); (7) the floating JSON's hoelder_bound fields
had an extra square root (recomputed); (8) merge metadata (radial_cells, partial) copied from the first part and incomplete compatibility checks
(fixed; merge now checks that the parts cover (radial cells x angular cells) exactly once). The referee found no defect in the Hoelder/Plancherel
step, the Leibniz and radial formulas, the cutoff polynomials, the geometry and area formulas, the BiTM/Bernstein algebra, the jets and the
recursion, the assembly, the merge arithmetic and the residual interface, and verified all 43949 saved rows (exact rational recomputation of
every row's contribution below the accumulated outputs). Independently of the referee, the Arb range evaluation of the cutoff polynomials in
monomial form at a ball lost up to five orders of magnitude near sigma = 1 (T0 = sup tau came out as 1.08); it is now evaluated in centred form
(Taylor shift to the sub-interval midpoint), which is tight to 1e-4; this, not the enclosures, was the main loss of v1.0 (5.6533 -> 2.1207).
The verifier's own audit of v1.0 (their topics 115, 117, 07:42Z-08:25Z) confirmed the finite components (all 106496 geometry boxes, the
cutoff ranges, the 43949 row aggregates) and found 22 of 36 display ceilings of the first table rounded to nearest (all tables now carry
ceilings), a gradient statement that mixed the component bound with the Euclidean norm (corrected), the jet-remainder sums' relative-only
rounding rule not outward for subnormal operands (an additive (Nmax + 2) eta allowance was added; the referee of round 2 checked all 390 sums of
v2.1 exactly: outward), and missing per-row Hessian inputs (every G/T factor and every Taylor-model remainder entering a product rule is now
stored per row). Round 2 (astra/forcing2/answer.md, on v1.1/v2.1): "no defect invalidating the supplied p9 v2.1 bounds, conditional on the
upstream residual and regularity hypotheses"; all round-1 repairs pass; the 789 executed series tails, all 832 blocks (largest accepted ratio
0.5954 and largest tail 0.0317 occur in blocks whose fine sub-cells are all inside, where the cutoff model is not used; the largest ratio in a
block with transition sub-cells is 0.3508 with tail 1.1e-6), all 106496 sub-cell geometries, the 15 symbolic Faa di Bruno tables, the Leibniz
expressions, the regime logic (the unclipped outward sigma interval decides the regimes), the alignment identities (exact for 2 x 2 blocks), the
merge (208 pairs) and every saved row were recomputed; four angular cells were fully replayed (2048 rows, all matching). Its general-code items
(the series tail used a float pow; the p11 cutoff path crashed; the block shifts bs hb are exact only for nbs, nbp <= 2; the fine-step coverage
assertion was a float test; the Taylor-model domain convention (remainder valid on parent domain cap block, outward sub-cells overhang by about
1e-19) should be stated) are repaired or stated in v2.2 / v1.2, whose outputs reproduce the v2.1 / v1.1 values.
Other fractional orders from the same pinned integrals (src/forcing_orders.py, runs/forcing/orders.json; Hoelder N <= I3^{(4-s)/2} I4^{(s-3)/2} in
Arb with exact exponents; ceilings with 5 significant digits; this covers the lead's proposed order s = 3.06 and the window [3.05, 3.1] of the
verifier's topic 97 inverse bounds): p9, lam = 1: s = 3.05: 1.1037, s = 3.06: 1.1843, s = 3.1: 1.57, s = 3.5: 26.324; p9, lam = 500: s = 3.05: 2.545, s = 3.06: 2.7243, s = 3.1: 3.5769, s = 3.5: 54.47; p11, lam = 1: s = 3.05: 2.05, s = 3.06: 2.199, s = 3.1: 2.9112, s = 3.5: 48.143; p11, lam = 500: s = 3.05: 3.4967, s = 3.06: 3.7485, s = 3.1: 4.9508, s = 3.5: 79.945; v1.2 (p9), lam = 1: s = 3.05: 1.4883, s = 3.06: 1.5976, s = 3.1: 2.1207, s = 3.5: 36.035.
Floating Hoelder values from the floating integrals for comparison (p9, lam = 1): s = 3.05: 0.9447, 3.06: 1.0135, 3.1: 1.3428, 3.5: 22.38.
Upstream dependencies and hypotheses (what 7.10 inherits; for the verifier's conditional verdict). (i) The per-mode Taylor models of d_t^i eps_N
(i <= 4) on the 13 spline sub-cells ci 4096..4108 come from cert_resid._cell_core_deriv (src/cert_resid.py 1911be77..., identical arithmetic to
the pinned 15a7535d... audited in two astra rounds, cert1/cert2, and used for 7.3/7.3b), evaluated on data/cert_green.npz
(c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1: the Arb boundary values A_n, B_n of the canonical Green functions at the
sub-cell starts and the exact spline polynomials of the trial, src/cert_green.py) and data/trial_v2_h0.008.npz
(a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874). These are the same objects as the R0 certificate of 7.3 (whose middle-region
values the verifier reproduced with their independent second method, topic 122) and the derivative certificate 7.3b; their validity rests on
the Taylor-model method of 7.1 (ODE recursion for A_n, B_n with certified remainders; exponential-polynomial residual products; mid-rad float64
and Arb). (ii) The identification of eps~ = sum_N eps_N(t) sin((2N+1) theta) with the canonical residual of the trial (closed-form canonical
inverse, section 5; normalization c_l = 1/k exact, 7.2). (iii) Regularity: tau in C^4 (p9) or C^5 (p11), eps~ in C^5 between the spline knots and
C^4 across them, so f = tau eps~ is in W^{4,infty} with compact support and the Plancherel identities for the orders 3 and 4 hold. (iv) The
certified bracket of x_* (7.2, S1) and delta = 33/2000 exactly. Everything else (angular Taylor coefficients, Cartesian recursion, cutoff
polynomials, geometry, Bernstein bounds, Hoelder, merge) is internal to cert_forcing2.py and was checked in the two astra rounds and in the
verifier's finite audits (topics 115, 117-122). The astra round-2 verdict is stated conditional on (i)-(iii). Verifier topic 122 (FINAL 10:13Z,
research/forcing_v22 in their lane): "CONFIRMED v2.2 finite components, physical forcing OPEN": all 43949 rows pass two independent aggregations,
the six ceilings pass exact comparisons, all 263694 cutoff range checks pass two methods, nine pinned replays reproduce every result field,
137235 pointwise inequalities and 331 series tails per method pass; OPEN on their side are (i) above (the residual Taylor models, which their
topics 98/99/101 and a residual-jet reconstruction would cover) and the composed F enclosures as mathematical objects, i.e. the statement
"1.5700 bounds the physical norm" remains conditional on the certificate method of 7.1.
Reproducibility: the box CPU guard (bin/cpu_guard.py) allows one running detached python job per lane among those aged at least 120 s and pauses the others (processes in the session of the lane's agent loop are exempt by its code; in shift 4 foreground python pieces of this lane were nevertheless observed paused, so all foreground pieces were kept under 120 s), so the computation is run in pieces (v1: cell by cell, about 50 s each; v2: cell by angular half, about 45 s each) and merged:
```
for ci in $(seq 4096 4108); do python3 src/cert_forcing.py data/cert_green.npz data/trial_v2_h0.008.npz runs/forcing/v12_p9_c$ci.json 33/2000 p9 64 16 8 8 $ci $ci; done
python3 src/cert_forcing.py merge runs/forcing/v12_p9_merged.json runs/forcing/v12_p9_c4*.json
for ci in $(seq 4096 4108); do for q in "0 7" "8 15"; do set -- $q; python3 src/cert_forcing2.py data/cert_green.npz data/trial_v2_h0.008.npz runs/forcing/v22_p9_c${ci}_q$1.json 33/2000 p9 64 16 8 8 2 2 16 $ci $ci $1 $2; done; done
python3 src/cert_forcing2.py merge runs/forcing/v22_p9_merged.json runs/forcing/v22_p9_c4*_q*.json
python3 src/forcing_float.py data/trial_v2_h0.008.npz 0.0165 p9 4.5e-5 runs/forcing/float_p9_dx45.json      # floating comparison, 140 s
```
SHA-256 (runs/forcing/SHA256.txt, 09:16Z; FINAL code and outputs): src/cert_forcing.py (v1.2) 5066d240ea60b89d137025f60fbda4e631b7cf7e67f8ef5968bab307bbeddcd9;
src/cert_forcing2.py (v2.2) 012e106b568ec68876058ee0588aa64cfbe9c846dc44523c164424015c238197; src/forcing_float.py
aa67a9b40ccdbfdce011e76c7ad30bf7c6a5ec75e5ee96617ff340cade748a80; src/cert_resid.py 1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053
(= the pinned version 15a7535d... plus the one-line stash `self._last_eps = eps`, arithmetic unchanged); runs/forcing/v22_p9_merged.json
b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201; runs/forcing/v12_p9_merged.json cc9e187aac3b2b01023ed99363b261c6f0658d5f7a56e87960dee134488fa0b0.
Earlier versions kept for the audit record: v1.0 a2f028c1... / p9_K64_n16_P8_merged.json b681b9c4... (5.6533); v1.1 374e6ce1... / v11_p9_merged.json
a0d2bba0... (2.1207); v2.1 be49284e... / v21_p9_merged.json 20d44c6c... (1.5700). Commands below produce the v1.2 / v2.2 files (names v12_*, v22_*).

## 7.11 X norms of the scaling tangent K, of the residual and of eps~ - X.grad eps~ (lead 13:54Z, after ver topic 138; FLOATING except the Arb ceilings marked RIGOROUS; shift 5, 16:57Z)
SCOPE (lead 22:45Z, 2026-10-21): every floating quantity of this subsection and of the B(K, K) paragraph (K, eps~, L K, B(K, K), rho~) is evaluated
for the STORED trial (data/trial_v2_h0.008.npz as stored, c_l = 1/k; written K_s, eps_s where the distinction matters), not for the exactly normalized
trial of the certificates; the scaling identity L K = eps~ - X.grad eps~ (ver topic 138 for the normalized trial) is exact for the exactly joined
certificate trial; for the STORED representation, which is discontinuous at the two joins (section 4, 7.0), it holds on each open region only up
to an interface term U[M].grad rho~ from the jumps and a strain term (c[K_pw]/3) X.grad rho~, c[K_pw] about 4.5e-18 (lead 02:49Z, verified); the
quadrature nodes below are interior to the cells, and these terms are below every printed digit. The rigorous ceilings below are statements about the
exact trial of section 7 (they use the certified per-cell majorants).
Weight w = m^-2 (1+u^2)^-3/2 (the H1m weight of the C2 Gram, section 7.4b), ||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX = pi int e^{2t} w(t) sum_N
[f_N^2 + (d_t f_N)^2 + (2N+1)^2 f_N^2] dt for f = sum_N f_N(t) sin((2N+1) theta); modes of the trial from the closed-form inverse (src/trial_green.py:
rho_modes, residual_modes), d_t of the residual modes by central differences; src/xnorm_K.py, runs/xnorm/. The integral is taken over 1e-4 <= r <= 1e7
in five pieces of spacing dt = 0.002 in t = log r (the residual's derivative has knot-scale structure, knot spacing 0.008: at dt = 0.0169 and 0.0101
the derivative term is not resolved, see the last two columns), merged in runs/xnorm/xnorm_K_merged.json; the omitted tails are estimated (floating,
from the end densities and the decay; runs/xnorm_jets/full_g4_v2.json) at 0.024 (inner) and 13.0 (outer) in norm^2 for K and 0.006 / 19.3 for rho~
(against 5.9e7 and 4.4e7), and negligible for the residual quantities. K = rho~ - X.grad rho~ is the scaling tangent
(J(K) = -2 with J(h) the x^2 y coefficient of h at the origin (K = x^2 y (1 - 3) + o(r^3)); c[K] = 0; L K = eps~ - X.grad eps~ for the exactly
normalized trial, ver topic 138; for the stored representation only up to the interface and strain terms of the SCOPE paragraph and 7.0).
| quantity | r < 2 | 4 <= r <= 16 | rest (2 <= r < 4 or r > 16) | all (fine, dt = 0.002) | all at dt = 0.0101 | all at dt = 0.0169 |
|---|---:|---:|---:|---:|---:|---:|
| K = rho~ - X.grad rho~ | 2.9419e+03 | 5.1576e+03 | 4.8380e+03 | 7.6591e+03 | 7.6582e+03 | 7.6567e+03 |
| eps~ | 2.7172e-04 | 1.5093e-02 | 3.0948e-03 | 1.5409e-02 | 1.4436e-02 | 1.4199e-02 |
| eps~ - X.grad eps~ | 3.2184e-03 | 2.5790e+00 | 3.0018e-01 | 2.5964e+00 | 5.1542e-01 | 3.6694e-01 |
| rho~ | 1.5209e+03 | 5.0252e+03 | 4.0099e+03 | 6.6064e+03 | 6.6064e+03 | 6.6064e+03 |
CORRECTION (17:04Z): the two derivative-containing rows above (eps~, eps~ - X.grad eps~) are NOT converged and not reliable: their t-derivatives were
taken by finite differences of the residual modes, and the modes carry small-scale evaluation noise that the first and second differences amplify
as the spacing shrinks (on the lobe 2 <= r <= 20: ||eps~ - X.grad eps~||_X = 2.72 at dt = 0.002 and 18.7 at dt = 0.001, while the residual modes
themselves are clean: their Wiener sums stay within the certified per-cell bound W <= 1.21e-4 at every spacing). The K and rho~ rows are fine (smooth,
large; stable to 4 digits across the spacings). RIGOROUS replacement (src/xnorm_cert.py version 2, all arithmetic in Arb balls at 128 bits with
upper endpoints printed by ceiling rounding (version 1 used floating sums with 1e-12 inflation factors without an error budget, referee astra/numrep2;
the version-2 values agree with version 1 to the printed digits); runs/xnorm/xnorm_cert.json; this lane's certificate data, audit pending): from the
per-cell majorants W_i_j of the derivative certificate (7.3b), with sum_N a_N^2 <= (sum_N |a_N|)^2 and the cell maximum of e^{2t} w at the left cell
end (e^{2t} w = L^2 u^-4 (1+u^2)^{3/2-k} is decreasing),
  ||eps~||_X^2 <= pi sum_cells h max(e^{2t} w) [W_0_0^2 + W_1_0^2 + W_0_1^2],   ||eps~ - d_t eps~||_X^2 <= pi sum_cells h max(e^{2t} w) [(W_0_0 + W_1_0)^2 + (W_1_0 + W_2_0)^2 + (W_0_1 + W_1_1)^2]:
  middle region rmin <= r <= R0 (7809 cells): ||eps~||_X <= 3.85651e-1, ||eps~ - X.grad eps~||_X <= 5.85873e+2 (ver topic 152 re-summed the saved
  cells); of which r < 2: 1.42514e-3 / 3.39214e-2 and the lobe annulus 4 <= r <= 16: 3.85195e-1 / 5.85864e+2; outer region R0 <= r <= r_T,out (8948
  cells): 1.68303e-3 / 3.80058e-3; inner region r_T,in <= r <= rmin (2632 cells): 8.86954e-7 / 3.89562e-5; totals over the THREE FINITE REGIONS
  r_T,in <= r <= r_T,out: ||eps~||_X <= 3.85655e-1, ||eps~ - X.grad eps~||_X <= 5.85873e+2. The two tails r < r_T,in and r > r_T,out are NOT included
  (this lane has no derivative majorants there); the verifier's topic 178 bounds the end regions r <= e^{a-5} and r >= e^{b+17} independently
  (||eps~||_X < 2.273735e-6 and < 3.926908e-6, ||eps~ - d_t eps~||_X < 3.5059554e-5 and < 6.445150e-6) and composes the whole-plane ceilings
  0.385656000027 / 585.874000000002, conditional on this lane's annular majorants (FINAL_REPORT section 6). The verifier's topic 179 v2 (FINAL
  2026-10-22T08:42:37Z, research/full_derivative_norm_bound_v2/evidence/verdict.json) removes that condition at the price of much coarser values: by its own
  direct whole-plane computation (7809 middle cells, 7 replays, all tails), for the exactly normalized canonical modal trial in the same weak weighted H^1
  norm, ||eps~||_X < 245653983.313885103 and ||eps~ - X.grad eps~||_X < 30665526224.248429025 (strict decimal ceilings; the coarse exterior term dominates).
  The verifier's topics 180 v2 (exterior cells, FINAL 10:18:52Z) and 183 exterior composition (FINAL 2026-10-22T10:22:57Z,
  research/derivative_norm_regional_composition/evidence/exterior/verdict.json) refine the exterior square and give, as roots of the printed regional
  squares (inner 67.9898116895358306437308 / 16132.4321701281783711136 and middle 2.23642149354638943132127 / 6074661.94639141300035166 from 179,
  outer 0.00000320066173968513189015735 / 0.0000192408718059828130775364 from 180 with the 178 tail included once), the unconditional whole-plane ceilings
  ||eps~||_X < 8.38010956871949018314234 and ||eps~ - X.grad eps~||_X < 2467.95347982509225629694 (report-table-compatible ceilings; the inner and
  middle squares dominate). These are the verifier's bounds for the exactly normalized canonical modal trial, not this lane's; they do not validate
  this lane's per-cell majorants or the conditional composition 0.385656000027 / 585.874000000002. The verifier's topic 181 v2 (FINAL 2026-10-22T11:20:30Z,
  research/inner_derivative_cells_v2/evidence/verdict.json) bounds the inner region r <= e^{a} separately by ||eps~||_X < 0.000002738182 and
  ||eps~ - X.grad eps~||_X < 0.000075224960 (44 cells, the 178 inner tail included once). The composition of all three refined regions (topic 183 both,
  FINAL 2026-10-22T11:31:12Z, research/derivative_norm_regional_composition/evidence/both/verdict.json; inner squares 0.00000000000749763727216539889936543 /
  0.00000000565879455607782317925245, middle and outer squares as above) gives the verifier's final unconditional whole-plane ceilings for the exactly
  normalized canonical modal trial: ||eps~||_X < 1.49546805188731021373656 and ||eps~ - X.grad eps~||_X < 2464.68293019825564964515, dominated by the
  middle region; this lane's finite-region ceilings 0.385655 / 585.873 (the three finite regions r_T,in <= r <= r_T,out, the two end tails excluded, whereas the verifier's ceilings cover the whole plane) concern this lane's per-cell majorants and are not validated by
  them (the middle squares of the two computations differ: 2.2364 against approximately 0.1487 = 0.385651^2 (the middle-region ceiling; 0.385655 is the three-region total), 6.0747e6 against approximately 3.4325e5 = 585.873^2). No inverse estimate, nonlinear closure or distance
  to the published X3 follows from any of these ceilings. The verifier's three-annulus scaling application (FINAL 2026-10-22T11:46:55Z,
  research/scaling_selected_application/evidence/verdict.json) gives the strict lower bound ||K||_X > 170.953964620623929217261 for the same exactly
  normalized canonical modal trial (three full annuli, the omitted integral nonnegative); with ||L K||_X = ||eps~ - X.grad eps~||_X < 2464.68293019825564964515
  (exact scaling identity of the exactly joined trial, 7.0) any same-norm estimate ||h||_X <= C ||L h||_X on a domain containing K, or its normalized
  graph approximants, needs C > 0.069361443018 (rigorous version of the quotient diagnostic above; it excludes no inverse by itself: on the span of K
  alone the constant ||K||_X / ||L K||_X is attained, and the exclusion of every finite C on the broad graph domains is the verifier's quasimode result,
  FINAL_REPORT 5(p)).
Reading (written 2026-10-21, before the verifier's whole-plane ceilings and three-annulus lower bound cited above; retained as the historical reading): ||K||_X = 7.6591e+03 (floating, converged; stored trial) and the rigorous upper bound ||L K||_X = ||eps~ - X.grad eps~||_X <= 5.85873e+2 on
the three finite regions (whole plane 585.874000000002 with the verifier's end-region bounds, topic 178) give, for any estimate
||h||_X <= C ||L h||_X on the graph domain of topic 138 (which contains K and, by the zero-strain bumps of topic 137, elements with J = c = 0
arbitrarily close to K), the abstract inequality C >= ||K||_X / ||L K||_X (one operator, admissible K); the numerical quotient 7659.08 / 585.88 = 13.07 is
reported as a MIXED-TRIAL DIAGNOSTIC only and NOT asserted as 'C >= 13.07' (a floating numerator computed for the STORED trial over a conditional ceiling of
the denominator computed for the exactly normalized trial, coefficients differing by 1e-13 relative; no transfer bound is stated; the Wiener-sum bound of this lane's unaudited derivative certificate (ver topic 152 calls it a conditional scalar sum); a
rigorous lower bound of ||K||_X was not available when this paragraph was written; the verifier's three-annulus scaling application cited above, FINAL 2026-10-22T11:46:55Z, now gives ||K||_X > 170.953964620623929217261 for the exactly normalized canonical modal trial). The lobe annulus carries 100 percent of the upper bound of
||L K||_X^2. B(K, K) = U[K].grad K was computed later (shift 6; paragraph 'B(K, K) ... IN THE X NORM' below: ||B(K, K)||_X = 2.0623e+05, floating). The coarse floating
values 0.0142 / 0.367 of the 16:57Z note are superseded.

ANALYTIC-DERIVATIVE VALUES (shift 6, 18:46Z, revised 2026-10-21T19:09Z after the referee round astra/xnorm1; FLOATING; src/xnorm_jets.py; runs/xnorm_jets/
full_g4_v2.json, lobe_g6_v2.json; this replaces the withdrawn finite-difference rows above). The residual modes eps_N(t), d_t eps_N and d_t^2 eps_N of
the modal trial (c_l = 1/k exactly) are computed by Leibniz on the analytic modal jets of src/trial_jets.py (exact spline / exponential-polynomial
derivatives of the a_m, Green ODEs A_n' = -2n A_n + g_n, B_n' = 2n B_n - g_n for the psi_n), with the same scattering to the frequencies 2j+1 +- 2n
as TrialGreen.residual_modes; no finite differences anywhere. The angular integral is exact (the modal formula above); the radial integral uses
Gauss-Legendre with g nodes on each of the 1558 knot cells of the trial (0.00765 <= r <= 3413; knot spacing 0.0019 to 0.008 in t on the lobe, 0.02
near the inner end) plus 120 and 240 log-spaced cells on 1e-4 <= r < 0.00765 and 3413 < r <= 1e7 (exponential-polynomial ranges), with the region
boundaries r = 2, 4, 16 inserted as cell boundaries (1921 cells; every region below is a union of whole cells). 'All' is the truncated range
1e-4 <= r <= 1e7: the omitted ranges contribute, by the end densities and the decay (integrand ~ e^{2t} inside, ~ e^{-t} outside for K and rho~,
faster for the residual quantities), below 1e-6 relative in norm^2 for K and rho~ and far less for eps~ and eps~ - X.grad eps~.
Checks (`python3 src/xnorm_jets.py --check data/trial_v2_h0.008.npz`, 44 s, with acceptance assertions): order 0 against TrialGreen.residual_modes
1.0e-12 absolute (max |eps_N| 4.0e-6: double-precision roundoff of the O(10 to 1000) constituent terms; the noise proxy |f(t+h) - 2 f(t) + f(t-h)| of
residual_modes at h = 1e-6 is 4e-11, the source of the finite-difference failure above); d_t eps_N against the 5-point finite difference at h = 1e-4:
1.4e-7 absolute (the FD roundoff floor; max |d_t eps_N| 8.7e-4); d_t^2 eps_N against the 5-point second difference at h = 3e-4: 5.4e-4 absolute (max
0.638; FD floor 4e-11 / 9e-8); a manufactured-mode test with artificial jets (M = 0, c_l = 1/3, R_0 = e^{3t}, psi_1 = e^{4t}, for which
eps = e^{5t} (5 sin theta - sin 3 theta) exactly): 9e-13; the modal angular integral against the (t, theta)-grid route of trial_jets (4096
midpoints on the quarter circle) at t = 2.1517: 1.6e-13 relative. Verifier topic 159 (FINAL 19:04Z): independent polar derivation of the
Leibniz/sine-product identities, exact integer checks of eps_mode_jets (10350 synthetic entries, M = 0, 1, 3, 16, 260, orders 0 to 2, exact) and
Arb/rational enclosures of the five literal scalars of full_g4.json (sqrt F2 = 44.91597921437864, sqrt K2 = 7659.129265258358, sqrt E2 =
0.03245335855334, ratio 170.52125767318): CONFIRMED for the identities, the synthetic code checks and the literal scalars only (no quadrature
error bound, no physical norm, tails omitted). Referee round astra/xnorm1 (18:49Z to 18:58Z, notes/astra_xnorm1_answer.md):
the Leibniz kernel and all six scatterings confirmed algebraically and by astra's own 819-case exponential-mode test (worst 1.3e-13); the norm
identity confirmed; three defects found and repaired in the present version (regions were masks on Gauss nodes instead of unions of cells, which
moved the regional values by up to 3e-4 relative while leaving the totals unchanged; the merge lacked consistency checks; the --check lacked the
5-point stencil and assertions). Quadrature: g = 4 against g = 6 on the lobe region 4 <= r <= 16 (99.99 percent of the norm^2 of eps~ - X.grad eps~
and 99.1 percent of that of eps~): norm^2 relative change 3.2e-04 (eps~ - X.grad eps~), 1.5e-04 (eps~), 2e-11 (K), 1e-16 (rho~).
| quantity (norm, floating) | r < 2 | 4 <= r <= 16 | rest (2 <= r < 4 or r > 16) | of which inner r < 0.00765 | of which outer r > 3413 | all, 1e-4 <= r <= 1e7 (g = 4) | all with the g = 6 lobe |
|---|---:|---:|---:|---:|---:|---:|---:|
| K = rho~ - X.grad rho~ | 2.9420e+03 | 5.1575e+03 | 4.8381e+03 | 1.1763e+01 | 1.9387e+02 | 7.6591e+03 | 7.6591e+03 |
| eps~ | 2.7178e-04 | 3.2303e-02 | 3.1035e-03 | 3.4822e-09 | 3.8065e-04 | 3.2453e-02 | 3.2456e-02 |
| eps~ - X.grad eps~ | 3.2227e-03 | 4.4915e+01 | 3.1882e-01 | 8.3262e-07 | 7.0894e-04 | 4.4916e+01 | 4.4909e+01 |
| rho~ | 1.5210e+03 | 5.0253e+03 | 4.0098e+03 | 5.8816e+00 | 2.3684e+02 | 6.6064e+03 | 6.6064e+03 |
Composition of the norm^2 on the lobe (g = 6; value : t-derivative : angular-derivative parts pi int e^{2t} w sum_N f_N^2, (d_t f_N)^2,
(2N+1)^2 f_N^2): eps~ - X.grad eps~ 8.5e-04 : 1993.2 : 23.5 (98.8 percent is the second t-derivative of the residual,
d_t eps_N - d_t^2 eps_N, at the knot scale); eps~ 1.7e-09 : 8.51e-04 : 1.92e-04 (81.6 percent t-derivative); K 2.11e+06 : 1.219e+07 : 1.230e+07;
rho~ 3.07e+06 : 7.54e+06 : 1.464e+07.
Reading: ||eps~||_X = 3.245e-02 and ||eps~ - X.grad eps~||_X = 44.92 (floating) lie below the certified ceilings 0.38566 and 585.88 by the factors
11.9 and 13.0 (the loss of (sum_N |a_N|)^2 >= sum_N a_N^2 and of the cell-maximum weights in the Wiener-sum bound). The floating quotient
||K||_X / ||L K||_X = 7659.1 / 44.92 = 170.5 is a floating lower bound for any C with ||h||_X <= C ||L h||_X on the graph domain of topic 138
(the 13.07 of the paragraph above is likewise a mixed-trial floating-over-conditional diagnostic, not a bound); it says nothing
about an upper bound of C. The 16:57Z coarse values (0.0142 / 0.367) are superseded. Nothing in this paragraph is rigorous.
B(K, K) = U[K].grad K IN THE X NORM (lead 13:54Z 'if cheap'; shift 6, 2026-10-21T19:09Z; FLOATING; src/xnorm_BKK.py; runs/xnorm_jets/BKK_g4_merged_v2.json).
Since rho~ = e^{3t} cos^2 theta sin theta sum_m a_m(t) cos 2m theta, the scaling tangent is K = rho~ - d_t rho~ = e^{3t} cos^2 theta sin theta
sum_m a~_m cos 2m theta with a~_m = -2 a_m - a_m' (degree-7 polynomial on each knot cell, exponential-polynomial outside), so the closed-form
canonical inverse of src/trial_green.py applies to K verbatim with a~_m in place of a_m (class TrialK; per-cell Taylor coefficients and the
inner/outer exponential-polynomial terms transformed exactly). Checks (`python3 src/xnorm_BKK.py --check data/trial_v2_h0.008.npz`, 77 s): the K
modes of the K-Green object agree with R_N - d_t R_N from the rho~ jets to 4.6e-13 (max |K_N| 386); psi[K]_n agrees with the scaling identity
psi[K] = 2 psi~ - X.grad psi~ (the canonical inverse of lambda^-1 rho~(lambda X) is lambda^-2 psi~(lambda X)) to 3.3e-8 absolute against
max |psi[K]_n| = 2.8e5, i.e. 1e-13 relative, an independent test of the K inverse; the raw strain c_raw[K] := psi[K]_xy(0) = 3 c[K] = -1.6e-12 (exactly 0 for the scaling
tangent, 2c - 2c; c_raw[rho~] = 15.726088); with c_l = 0 the residual routine returns U[K].grad K - K, so B(K, K) = that + K (order 0 against the
direct evaluation 4.6e-12); d_t B(K, K) by the jets against the 5-point FD: 4.5e-3 absolute at max |d_t B_N| = 1.1e4 (4e-7 relative).
Values (g = 4 on the same 1921 cells; norms): ||B(K, K)||_X = 2.0623e+05 (r < 2: 3.580e+03; 4 <= r <= 16: 2.0502e+05; rest: 2.201e+04; inner 2.2e-04, outer 6.95),
98.8 percent of the norm^2 on the lobe; composition value : t-derivative : angular-derivative = 1.0 : 64.7 : 34.3 percent; ||K||_X from the same object 7.6591e+03
(agrees with the table). So ||B(K, K)||_X / ||K||_X^2 = 3.515e-03 and ||B(K, K)||_X / ||K||_X = 26.93 (floating). With the floating ||L K||_X = 44.92: for the
one-parameter family rho~ + s K the quadratic term s^2 B(K, K) equals the linear term s L K in X norm at |s| = 2.18e-04 (a scale change of the trial by
that fraction), and ||B(K, K)||_X = 4591 ||L K||_X. Floating, for the lead's nonlinear bookkeeping only; no rigorous content: this compares two X norms along one direction and is not a quadratic
estimate of the nonlinear term in any graph norm (lead 23:40Z).

## 8. Reproducibility (all commands from the lane root; single-threaded; times on this machine)
```
python3 src/x3.py                                              # reconstruction test vs gen_shape.py (0.1 s)
python3 src/inverse.py                                         # manufactured inverse tests (1 s)
python3 src/x3_resid.py 16875 512 1e-4 1e6 runs/resid_N16875_q512.json      # 8 s
python3 src/x3_modes.py 80000 4096 1e-4 1e5 260 data/x3_modes_N80000_q4096_M260.npz   # 34 s, 320 MB (regenerable)
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_v2_h0.008.npz   # 55 s
python3 src/trial_green.py data/trial_v2_h0.008.npz             # closed-form inverse vs grid inverse (2 min)
python3 src/trial_resid.py data/trial_v2_h0.008.npz 1200 runs/trial_v2_resid.json   # 1 min
python3 src/midrad.py; python3 src/cert_spline.py data/trial_v2_h0.008.npz
```
Published evaluator rerun: runs/pubeval/code is an unmodified copy (diff -rq against the clone: no differences, checked 2026-10-22) of the published evaluator
folder d_evaluator/code of the IPM Setting I artifacts, including its gen_audit.sh (`bash gen_audit.sh <shape.npz> <tag> "r0 R N nq Mmax; ..."`, WORKLOG
2026-10-20 12:51Z); it is not shipped: the published artifacts are the folder Changhe/IPM/case1/IPM_Setting_I.artifacts of https://github.com/ChangheYang1999/PDE_exploring.git
(clone used here: commit 701899f69e2e9fa1394357b3d455c80a649d092c). The X3 coefficient file is read by src/x3.py from X3_COEFF_PATH (default: the clone path).
Environment: python 3.9, numpy 2.0.2, scipy 1.13.1, python-flint 0.6.0 (Arb), mpmath 1.3.0; CPU single thread.

#### 7.3b Derivative norms (R1, R3, R5): this lane's RIGOROUS upper bounds (method of 7.1; NOT independently verified, lead 10:24Z); middle region runs/cert_deriv_middle.json (7809 cells, 3.3 h; SHA-256 7408d122c9a8d0a214c48717cf4f43396533d811c992d47d70f1402febabe499), outer region runs/cert_deriv_regions_outer.json (SHA-256 92a27641050b4b9e4ec497237bc83ccc6b643e1b72521f309b52ec4206551f7f), inner region (see below); code src/cert_resid_deriv.py (SHA-256 38e45bcd4400d119fb0a887794c4866bcc1d61eed1c3d69f58616eb7c95d5ac8) with cert_resid._cell_core_deriv, summaries src/cert_deriv_summary.py and src/deriv_region_shells.py (SHA-256 0b96cf4f3a26d116ac1c7f43f7940e2533b3e214a9e93bd5320f9037ecf8cc0d)
Per sub-cell (length <= 0.0019 in t = log r) the Taylor models of d_t^i eps_N give the majorants W_i_j (with b_{i,N,s} the certified bound of
|d_t^i eps_N| on sub-interval s of the 4-way split: W_i_j := max_s sum_N (2N+1)^j b_{i,N,s} for i + j <= 2, := sum_N (2N+1)^j max_s b_{i,N,s} for
i + j > 2; e.g. cell 4124: W_0_0 = 1.1432e-4 subdivided against 1.3097e-4 unsubdivided, referee astra/numrep6)
>= sup over the cell and over theta of |d_t^i d_theta^j eps~| (i + j <= 2 everywhere; i + j <= 5 on the 377 cells meeting the disc
|X - P| < x_*/4, i.e. r in [6.44, 10.75]). Cartesian derivatives follow from d_x = e^{-t}(cos th d_t - sin th d_th),
d_y = e^{-t}(sin th d_t + cos th d_th): r |grad eps~| <= W_1_0 + W_0_1 and r^2 |d^2 eps~| (any second derivative) <=
W_2_0 + 2 W_1_1 + W_0_2 + W_1_0 + 2 W_0_1 pointwise on the cell. Division by the certified cell minimum m_inf of m(r). Maxima per
dyadic shell (summary runs/cert_deriv_summary.txt, src/cert_deriv_summary.py):
| shell of r (cell starts) | W_0_0/m | W_1_0/m | W_0_1/m | W_2_0/m | W_1_1/m | W_0_2/m | W_F/m | W_K/m | W_dtK/m |
|---|---|---|---|---|---|---|---|---|---|
| [rmin, 0.0156) | 2.19e-8 | 2.57e-6 | 8.18e-8 | 9.62e-4 | 9.99e-6 | 3.04e-6 | 2.56e-6 | 4.504e+2 | 1.352e+3 |
| [0.0156, 0.0625) | 5.18e-8 | 2.79e-7 | 2.48e-7 | 5.71e-6 | 2.26e-6 | 4.94e-6 | 2.33e-7 | 4.504e+2 | 1.352e+3 |
| [0.0625, 0.25) | 5.11e-7 | 4.34e-6 | 5.25e-6 | 3.38e-5 | 5.17e-5 | 1.33e-4 | 4.01e-6 | 4.505e+2 | 1.352e+3 |
| [0.25, 1) | 7.04e-6 | 6.39e-5 | 4.09e-4 | 1.37e-3 | 7.64e-3 | 9.86e-2 | 6.06e-5 | 4.505e+2 | 1.350e+3 |
| [1, 4) | 1.91e-5 | 7.40e-4 | 3.04e-3 | 8.98e-2 | 9.48e-2 | 8.43e-1 | 7.68e-4 | 4.508e+2 | 1.330e+3 |
| [4, 16) | 2.60e-4 | 3.79e-1 | 4.23e-2 | 5.86e+2 | 6.16e+1 | 1.03e+1 | 4.28e-1 | 4.189e+2 | 2.119e+3 |
| [16, 64) | 2.03e-5 | 3.94e-3 | 5.03e-3 | 1.09 | 1.05 | 1.51 | 4.33e-3 | 1.952e+2 | 2.613e+2 |
| [64, 256) | 6.50e-6 | 8.82e-5 | 1.64e-3 | 5.00e-3 | 3.04e-2 | 6.34e-1 | 9.10e-5 | 2.118e+2 | 6.754e+1 |
| [256, 1024) | 6.10e-6 | 2.56e-5 | 1.54e-3 | 5.12e-4 | 9.63e-3 | 6.05e-1 | 2.66e-5 | 2.187e+2 | 4.707e+1 |
| [1024, R0) | 5.57e-6 | 1.70e-4 | 1.20e-3 | 5.47e-2 | 5.06e-3 | 4.66e-1 | 1.67e-4 | 2.208e+2 | 4.201e+1 |
(Every entry is a decimal CEILING of the maximum over the cells whose left end lies in the shell of the stored per-cell majorant divided outward by
m_inf; regenerated by `python3 src/report_tables.py --deriv` (runs/report_tables_deriv.md) on 2026-10-22 after the referee pass astra/numrep2 found
about 40 nearest-rounded entries in the earlier table; the earlier W_K, W_dtK columns had 4 digits, here 4 significant digits.)
(W_0_0/m here is the derivative run's own subdivided cell bound; it differs from the R0 table's W of 7.3 in the third digit in the lobe shell (2.60e-4
against 2.5965e-4) because the two runs build their Taylor models separately.)
R1: sup over rmin <= r <= R0 of r |grad eps~| / m <= 4.195e-1 (at r = 8.781) and of r^2 |D^2 eps~| / m <= 7.132e+2 (at r = 8.773; any second partial derivative),
both attained in the shell [4, 16) (the lobe next to P); over the middle cells outside that shell the suprema are 8.559e-3 and 4.516 (shell [16, 64)).
(The earlier '3.7' for the off-lobe second-derivative value was wrong; corrected 2026-10-22.)
R5: ||eps~ - X.grad eps~||_{R0 norm} = sup W_F/m <= 0.4275 (W_F = the saved majorant W_eps_minus_dteps of eps~ - d_t eps~) (middle region; outward ceiling of the saved per-cell maximum, which lies between 0.427 and 0.427444 at row 4124, verifier topic 142; the earlier printed 0.427 was an inward rounding); ||K~||_{R0 norm} = sup W_K/m <= 450.8 with
K~ = rho~ - X.grad rho~ (K~ is of the size of rho~ itself, L^3 m ~ 448 m at small r), ||d_t K~||/m <= 2119.
R3 (the 377 cells with order-5 Taylor models, r in [6.44, 10.76]; absolute certified cell bounds W_i_j, not divided by m; decimal ceilings of the
maxima over these cells): W_0_0 1.21e-4 (r = 8.790), W_1_0 1.75e-1, W_0_1 1.95e-2, W_2_0 2.71e+2, W_1_1 2.85e+1, W_0_2 4.56, W_3_0 4.34e+5, W_2_1 4.43e+4, W_1_2 6.37e+3, W_0_3 1.82e+3,
W_4_0 7.50e+8, W_3_1 6.92e+7, W_2_2 9.84e+6, W_1_3 1.82e+6, W_0_4 6.99e+5, W_5_0 1.45e+12, W_4_1 1.21e+11, W_3_2 1.56e+10, W_2_3 2.82e+9, W_1_4 5.03e+8, W_0_5 2.73e+8 (all attained at r = 8.57 to 8.79,
the lobe; Taylor remainders of d_t^i eps_N on these cells: 2.2e-11, 6.3e-11, 2.6e-9, 2.2e-6, 6.5e-4, 5.5e-1 for i = 0..5); K~: W_K 8.89e+1, W_dtK 9.89e+2. These are upper bounds; the floating direct
evaluation of section 7.5 (sup of D^alpha eps~ on the lobe disc: 6.7e-5, 1.1e-2, 1.87, 330, 6.2e4 for |alpha| = 0..4) shows that
they are within a factor 2-4 of the actual suprema (e.g. r^4 sup|D^4 eps~| ~ 8.8^4 x 6.2e4 = 3.7e8 against W_4_0 = 7.5e8), so the
large high-derivative norms near P are real, not an artefact of the majorants (answering the verifier's 18:12Z caution).
OUTER REGION (R0 <= r <= r_T,out = e^{t0+17} = 8.2440e10, the last cell starting at 8.228e10; RIGOROUS; chain6b/6c, cert_resid_deriv.py regions only, 8948 cells, 18985 s, done 09:27Z; runs/cert_deriv_regions_outer.json;
table runs/cert_deriv_outer_shells.txt from src/deriv_region_shells.py; all entries 4-significant-digit CEILINGS of the certified per-cell values;
wf = the certified cell maximum of the multiplier (1+u)^{1/2}; r|grad eps~| <= W_1_0 + W_0_1 and r^2|D^2 eps~| <= W_2_0 + 2W_1_1 + W_0_2 + W_1_0 + 2W_0_1 as above):
| shell of r (cell starts) | cells | sup W/m | sup r|grad eps~|/m | sup r^2|D^2 eps~|/m | sup wf W/m | sup wf r|grad|/m | sup wf r^2|D^2|/m | sup W_F/m | sup W_K/m | sup W_dtK/m |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [3.4e+03, 1e+04) | 566 | 2.951e-05 | 0.002959 | 0.997 | 0.001068 | 0.1071 | 36.07 | 0.0001416 | 221.6 | 40.63 |
| [1e+04, 1e+05) | 1212 | 9.319e-05 | 0.004169 | 1.122 | 0.007369 | 0.3187 | 77.53 | 9.968e-05 | 222 | 40.16 |
| [1e+05, 1e+06) | 1212 | 6.364e-05 | 0.002778 | 0.6704 | 0.007284 | 0.3179 | 76.73 | 8.942e-05 | 222.1 | 39.88 |
| [1e+06, 1e+07) | 1212 | 1.147e-05 | 0.0005602 | 0.1317 | 0.004149 | 0.2028 | 47.65 | 1.869e-05 | 222.1 | 39.83 |
| [1e+07, 1e+08) | 1212 | 1.738e-06 | 8.835e-05 | 0.02071 | 0.001989 | 0.1012 | 23.7 | 2.855e-06 | 222.1 | 39.83 |
| [1e+08, 1e+09) | 1212 | 2.622e-07 | 1.344e-05 | 0.003148 | 0.0009488 | 0.04864 | 11.4 | 4.303e-07 | 222.1 | 39.83 |
| [1e+09, 1e+10) | 1212 | 3.968e-08 | 2.034e-06 | 0.0004762 | 0.0004542 | 0.02328 | 5.451 | 6.508e-08 | 222.1 | 39.83 |
| [1e+10, 1e+11) | 1110 | 6.089e-09 | 3.085e-07 | 7.201e-05 | 0.0002205 | 0.01117 | 2.607 | 9.945e-09 | 222.1 | 39.83 |
whole file: sup W/m 9.319e-05 at r = 3.343e+04; sup r|grad|/m 0.004169 at r = 2.671e+04; sup r^2|D^2|/m 1.122 at r = 2.083e+04; multiplier forms 0.007369, 0.3187, 77.53; W_F/m 0.0001416; W_K/m 222.1; W_dtK/m 40.63
Taylor remainders of the outer cells: eps 1.6e-13 (i = 0, 1), 5.2e-11 (i = 2); A <= 7.5e-5, B <= 1.4e-4 absolute (the outer A_n, B_n are large; the W bounds include them
and reproduce the R0 certificate's 9.3189e-5). So on the whole exterior R1: r|grad eps~|/m <= 4.169e-3 (at r = 2.67e4) and r^2|D^2 eps~|/m <= 1.122
(at r = 2.08e4), both in the far-field Theta_1 mismatch band of X3; with the (1+u)^{1/2} multiplier 0.3187 and 77.53. R5 on the exterior:
||eps~ - X.grad eps~||/m <= 1.416e-4, ||K~||/m <= 222.1, ||d_t K~||/m <= 40.63.
INNER REGION (5.155e-5 <= r <= 0.007651; this lane's RIGOROUS upper bounds, same method; 2632 cells, 5277 s, done 10:55Z; runs/cert_deriv_regions_inner.json,
SHA-256 5ab4a164ea9424ef64dba4af7296080f035165764545ef91e111404634d21bb4; table runs/cert_deriv_inner_shells.txt; ceilings as above):
| shell of r (cell starts) | cells | sup W/m | sup r|grad eps~|/m | sup r^2|D^2 eps~|/m | sup wf W/m | sup wf r|grad|/m | sup wf r^2|D^2|/m | sup W_F/m | sup W_K/m | sup W_dtK/m |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [5e-05, 0.0001) | 349 | 1.498e-09 | 8.607e-09 | 1.323e-07 | 1.5e-09 | 8.615e-09 | 1.324e-07 | 6.045e-09 | 450.6 | 1352 |
| [0.0001, 0.0002) | 365 | 1.499e-09 | 9.285e-09 | 3.346e-07 | 1.5e-09 | 9.294e-09 | 3.349e-07 | 6.073e-09 | 450.6 | 1352 |
| [0.0002, 0.0005) | 482 | 1.596e-09 | 1.385e-08 | 1.629e-06 | 1.598e-09 | 1.386e-08 | 1.631e-06 | 6.404e-09 | 450.6 | 1352 |
| [0.0005, 0.001) | 365 | 1.73e-09 | 2.377e-08 | 4.763e-06 | 1.732e-09 | 2.38e-08 | 4.768e-06 | 6.624e-09 | 450.6 | 1352 |
| [0.001, 0.002) | 365 | 2.117e-09 | 3.093e-08 | 6.368e-06 | 2.119e-09 | 3.096e-08 | 6.375e-06 | 8.439e-09 | 450.6 | 1352 |
| [0.002, 0.004) | 365 | 2.171e-09 | 2.814e-08 | 4.808e-06 | 2.174e-09 | 2.817e-08 | 4.814e-06 | 1.028e-08 | 450.6 | 1352 |
| [0.004, 0.00766) | 341 | 9.19e-06 | 0.0002762 | 0.01396 | 9.203e-06 | 0.0002766 | 0.01398 | 0.0002583 | 450.6 | 1352 |
whole file: sup W/m 9.19e-06 at r = 0.007146; sup r|grad|/m 0.0002762 at r = 0.006932; sup r^2|D^2|/m 0.01396 at r = 0.007214; multiplier forms 9.203e-06, 0.0002766, 0.01398; W_F/m 0.0002583; W_K/m 450.6; W_dtK/m 1352
Taylor remainders of the inner cells: eps <= 1.1e-18 (i = 0, 1), 1.1e-18 (i = 2); A/B 5.5e-32. On the inner region R1: r|grad eps~|/m <= 2.762e-4 (at
r = 0.00693, the last cells before rmin) and r^2|D^2 eps~|/m <= 1.396e-2 (at r = 0.00721); for r < 0.004 they are below 3.1e-8 and 6.4e-6; R5:
||eps~ - X.grad eps~||/m <= 2.583e-4, ||K~||/m <= 450.6, ||d_t K~||/m <= 1352 (K~ is of the size of rho~ itself at small r, as in the middle region).
R4 (origin): sup W/r^5 = 1.2562e-3 on the inner cells (at r = 5.155e-5; runs/cert_summary_all.txt). With the middle (7809 cells), outer (8948) and
inner (2632) regions, the first and second derivative norms of the residual are now bounded rigorously on the whole plane except the two tails
(r < r_T,in and r > r_T,out, where only the zeroth-order majorants of 7.3 are available): sup over r_T,in <= r <= r_T,out (5.1555e-5 <= r <= 8.2440e10) of r|grad eps~|/m
<= 0.4195 and of r^2|D^2 eps~|/m <= 713.2, both attained at the lobe next to P (r = 8.78); away from the shell [4, 16) the suprema are 8.559e-3 and
4.516 (middle shell [16, 64)), 4.169e-3 and 1.122 (outer), 2.762e-4 and 1.396e-2 (inner). Whole-plane status: chain6 complete (chain6b/6c).

- N8 (shift 3): `python3 src/n8_floating.py data/trial_v2_h0.008.npz runs/n8/n8_floating.json 1e-4 1e-4` (10 s, floating);
  `python3 src/cert_n8.py data/cert_green.npz data/trial_v2_h0.008.npz runs/n8/cert_n8_full.json 4 350 0.2` (400 s, RIGOROUS, all four balls);
  `python3 src/cert_n8.py data/cert_green.npz data/trial_v2_h0.008.npz runs/n8/cert_n8_fine0165.json 16 160 0.0165` (90 s, RIGOROUS, fine pass);
  `bash runs/n8/fft_chain.sh` (the four cut-off FFT norms, 6 min, floating; dx variants: `python3 src/pdisc_fft.py data/trial_v2_h0.008.npz 0.028875 0.037125 0.000165 out.json 1.25`).

- 7.8: `python3 src/x3_minus_trial_jets.py 12000 512 1e-4 1e5 runs/jets/x3_minus_trial_N12000_T512.json` (94 s, floating; 6000 256 for the coarse row).


SHA-256 of the key files at 2026-10-21T02:06Z (shift 3; code and data as used for the certificates of sections 7.2, 7.3, 7.6, 7.7):

| file | SHA-256 |
|---|---|
| src/cert_n8.py | 09849524feda01ba812b65b69f4939a8dd90b196027f5258dc63375c7181eb65 |
| src/midrad.py | 5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e |
| src/cert_resid.py | 15a7535dbe5d7249ea38e089229591591976eef1151f298c932873f9e9dec828 |
| src/cert_green.py | 7f1c067b15d087b0688e3b4f1dc0b3abaf301a421b600ce96f5cedf662d6f8f0 |
| src/n8_floating.py | 01a6e4314655f0db620f935237d37d792e7ebc27a2909d5b2272f803bc72ed70 |
| src/pdisc_fft.py | 0813c9525cef2260da6aa9093ba79e626d07405c143c5a397f0e59b6417bb749 |
| src/x3_minus_trial_jets.py | 28aad784cd26149fa12d43f4cedef9ee963136e89e3efbe8123268e576c5e002 |
| src/xnorm_jets.py (shift 6, after the astra/xnorm1 repairs) | 80febd2e62f103c22fe230775a59adebadb25fe87e7fc3e4d7b037a80970d7ff |
| src/xnorm_BKK.py (shift 6) | ef82b57532ad06b8929a88f4644cde2294aff182a09be798cac1badeee29d475 |
| src/xnorm_cert.py (shift 5) | 4ea4f2717ccfa8c4b6ec5ee223ee39efae22b486138bbd558418e9c4d899f882 |
| src/cert_flow.py | bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6 |
| src/cert_scalars2.py | b048d14fb3fa205c1e88a5f510f901fdc0e72b7de7a914df202f362401aedcd1 |
| data/cert_green.npz | c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1 |
| data/trial_v2_h0.008.npz | a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874 |
| data/trial_n7.npz | d026c5cfa9892683e1d8b07562bbfb506629cab76be20d5b9fa9c0bdf241443f |
| runs/n8/cert_n8_fine0165.json | 451d1e05562e031baa1dee3cda22c904d946c230734dc271a944b02263a01d80 |
| runs/n8/cert_n8_full.json | 0aee537a69b4a15e3c045fe568dd470ffa598ffd9a281a5ae0c7184ec89735ec |
| runs/n8/cert_n8_mid.json | 6c12f7d8a84e168c735c33261e9f08e5c6073885006d1261dfb9c8400f7766a5 |
| runs/n8/cert_n8_fine0165_v3.json | 1e71e1309125eb189648cfbd9f1c5c1abbb5f492cf6efd9ad52e876ec70855e5 |
| runs/n8/n8_floating.json | 61c8f08d9a2e0f61ccb376c9be6868c9a01ef4e41b7116222dcc1c62d375b124 |
| runs/scalars_full.json | c831175d41bde3377869e8461bc32057edff11a6bef1d69aa7f12b4134777fd2 |
| runs/cert_resid_middle.json | 88d2149248eaec2d868c7152859ba71d627e1162e2fa35ae2105a38531e1dd7a |
| runs/cert_resid_regions.json | e8848beb995140e70ee2615ef66a3961234d85e121031edb80d8ae60e6066177 |
| runs/flow_middle.json | 300282f24a6c3ac8e667408de21bc59ded25ea90bda564f6573c5f06c430cac9 |
| runs/flow_outer.json | 897c5021e5c509eac72181d2ff519f7c0ccddfab86867b9beec7c9cf5db78d8e |
| runs/flow_inner.json | c243f6f2f9e86b99e08d4ce370da0ade37ee5ca04dc848d92dcbbbf4a809699f |
| runs/flow_tails.json | c0d4bd4a33566bf4accbeb2554a8f1dc42ba3fda966c28d87ab93c0c8cf75498 |
| runs/axis_cell.json | e4403c8f23ad66544c348fb1f3c2674d6356ab8b8a989b95c73f13f8633b248b |

Note: src/cert_n8.py is now v3 (robustness items, arithmetic unchanged); the v2 outputs runs/n8/cert_n8_{fine0165,full,mid}.json were produced by the v2 source with SHA-256 e7786de0aa6ea802f13aac64856e30134abf02809ddad339f25cce9cbe2549c1 (TO_TEAM 01:34Z); the v3 fine output reproduces them.

- 7.9: `python3 src/aux_R.py 512 0.08 0.0165 3.1 runs/n9/aux_R_n512.json` (42 s, floating; 256 for the coarse row).
- 7.10 (shift 4): the cell-by-cell loops and merge commands are listed at the end of section 7.10 (src/cert_forcing.py v1.2, src/cert_forcing2.py
  v2.2, src/forcing_float.py; about 11, 20 and 2.5 min in total, run as many short foreground pieces: the box CPU guard (bin/cpu_guard.py) allows one running detached python job per lane among those aged at least 120 s and pauses the others (processes in the session of the lane's agent loop are exempt by its code; in shift 4 foreground python pieces of this lane were nevertheless observed paused, so all foreground pieces were kept under 120 s)).
- 7.3b regions (shift 4): `python3 src/deriv_region_shells.py runs/cert_deriv_regions_outer.json 3400 1e4 1e5 1e6 1e7 1e8 1e9 1e10 1e11`
  (per-shell ceilings; seconds), likewise for runs/cert_deriv_regions_inner.json and runs/cert_deriv_middle.json.
- 7.11 (shifts 5-6): `python3 src/xnorm_cert.py` (rigorous Wiener-sum ceilings from the saved certificate cells, seconds; runs/xnorm/xnorm_cert.json);
  `python3 src/xnorm_jets.py --check data/trial_v2_h0.008.npz` (44 s); VERSION 1 (superseded): `python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 4 0 1918
  runs/xnorm_jets/full_g4.json` (110 s, floating; 1918 cells = 120 inner + 1558 knot + 240 outer) and `python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 6 625 965
  runs/xnorm_jets/lobe_g6.json` (53 s); VERSION 2 (the reported *_v2.json values; 1921 cells with the region boundaries r = 2, 4, 16 inserted): `python3 src/xnorm_jets.py
  data/trial_v2_h0.008.npz 4 0 1921 runs/xnorm_jets/full_g4_v2.json` and `python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 6 626 969 runs/xnorm_jets/lobe_g6_v2.json`;
  pieces are summed by `python3 src/xnorm_jets.py --merge out.json piece1.json ...` (coverage and consistency checks included; the v2 files use the
  1921-cell list with the region splits). B(K, K): `python3 src/xnorm_BKK.py --check data/trial_v2_h0.008.npz` (77 s); `python3 src/xnorm_BKK.py
  data/trial_v2_h0.008.npz 4 0 1000 runs/xnorm_jets/BKK_g4_p1_v2.json` and `... 4 1000 1921 ..._p2_v2.json` (61 s each), then `python3 src/xnorm_jets.py --merge runs/xnorm_jets/BKK_g4_merged_v2.json
  runs/xnorm_jets/BKK_g4_p1_v2.json runs/xnorm_jets/BKK_g4_p2_v2.json`. The superseded FD route:
  `python3 src/xnorm_K.py data/trial_v2_h0.008.npz 3450 1e-4 1e7 out.json` (floating, noise-dominated derivative rows).


Added 2026-10-22 (shift 7; after the referee passes astra/numrep2 and numrep4): commands for every script named in sections 7.2 to 7.11; all from the
lane root, single-threaded. Several listed invocations are LONG single processes (cert_green 16 min, cert_resid 35 min, c2_fminus 85 min, cert_flow
75 min, cert_resid_deriv hours); the box CPU guard limits the eligible detached python jobs of a lane aged at least 120 s to one running job (processes sharing the lane
loop's session are exempt), so they must run one at a time (as the chain scripts do); the forcing certificate (7.10), the B(K, K) norm (7.11) and the
K-projection stages (7.4c) are supplied in chunked form with their merge commands. PREREQUISITES: the first
block of this section generates data/x3_modes_N80000_q4096_M260.npz (34 s, 320 MB); the certificate block below generates data/cert_green.npz (16 min,
291 MB), data/cert_outer_green.npz and data/cert_inner_green.npz; all are GENERATED intermediates, not shipped artifacts. External code referred to in the
text (the lead's code/aux_R.py, the box's bin/cpu_guard.py) is infrastructure outside this lane and outside the command coverage claimed here.
```
mkdir -p runs/pdisc runs/kproj runs/c2 runs/n8 runs/n9 runs/n10 runs/xnorm runs/xnorm_jets runs/forcing runs/closure runs/jets     # output directories
# 7.1 to 7.3, 7.3c: the certificate pipeline (RIGOROUS; Green sub-cell length hsub = 0.0019 in t, outer extent T_out = 17, inner extent T_in = 5, 256 bits)
python3 src/cert_green.py data/trial_v2_h0.008.npz 256 0.0019 data/cert                                # Arb boundary values, data/cert_green.npz (16 min, 291 MB)
python3 src/reexport_coeffs.py data/trial_v2_h0.008.npz data/cert_coeffs.json 256                        # exact dyadic export of Ei, Eo, A_00
python3 src/cert_scalars2.py data/cert_green.npz data/trial_v2_h0.008.npz runs/scalars_full.json 8.600063803   # S1 (10 s)
python3 src/cert_resid.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_resid_middle.json 12          # R0 middle, Q = 12 (35 min)
python3 src/cert_green_outer.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json 0.0019 17.0 5.0 data/cert 256   # outer/inner Arb data
python3 src/cert_resid_regions.py data/cert_green.npz data/trial_v2_h0.008.npz data/cert_outer_green.npz data/cert_inner_green.npz runs/cert_resid_regions.json
python3 src/cert_tail.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz 0.5 runs/cert_tail_d05.json 256
python3 src/cert_tail.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz 0.32063946870624582 runs/cert_tail.json 256
python3 src/cert_inner_tail.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_inner_green.npz runs/cert_inner_tail.json 256
python3 src/cert_summary.py > runs/cert_summary_all.txt; python3 src/variants_summary.py                     # summaries (nearest-rounded prints; ceilings: report_tables.py)
# variants (7.3c): the trial files are fits of the same modes file with the parameters h, h_in, M (argument 5) and the X3 knot index of R0 (argument 6; -1 = the last knot 3412.97, -2 = 1467.96):
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.004 0.01 data/trial_v3_h0.004.npz          # v3: h = 0.004, h_in = 0.01 (bi = 100, bo = 250.1; 2820 spline functions; 4 min)
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_v4_M230.npz 230        # v4: modes m < 230
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_v5_R0knot2.npz - -2    # v5: R0 = 1467.96 (knot scheme 2; 1459 spline functions)
# then the same certificate pipeline on each with the output tags of runs/chain7d.sh (and chain2.sh for v3). REPRODUCTION CHECK (shift 8, 2026-10-22T06:23Z to 06:31Z,
# runs/variant_regen.sh, log runs/variant_regen.log, comparison runs/variant_regen/compare.txt): the modes file (an intermediate; its first-shift original was deleted
# unhashed, so its identity is not separately established) and the four trial files (base and v3, v4, v5) were regenerated from the published c6g_shape.npz with the
# commands above; every array of each regenerated trial file equals the stored one exactly, and the regenerated trial files
# are byte-identical to the stored ones (SHA-256 as in the table below; numpy writes a fixed zip date). EVIDENCE RETAINED (runs 2 and 3 of the chain, 07:03Z and 07:12Z, after the verifier's
# 07:01Z note that the first record held only stored-side hashes): runs/variant_regen/compare.txt (regenerated-file SHA-256 against the table: four EQUAL; arrays identical; exit 0) and
# runs/variant_regen/compare_raw_v2_output.json (the verifier's raw byte comparator: PASS, four BYTE_IDENTICAL, distinct inodes); the regenerated files are kept in runs/variant_regen/ (lane only).
# The rc fields of the first two chain logs are not evidence (rc=$? was read after a date substitution; fixed in run 3). The base trial data/trial_v2_h0.008.npz is shipped; the three variant trial files and data/trial_n7.npz are not (15 MB, incompressible).
# 7.4 to 7.4c finite sections (floating)
python3 src/truncate_trial.py data/trial_v2_h0.008.npz 20 data/trial_small_M20.npz; python3 src/smooth_band.py data/trial_v2_h0.008.npz 1.7918 2.4849 0.02 data/trial_s02.npz   # test fixtures (both reproduce the stored files byte-identically; shift 8)
python3 src/lin_assembly.py; python3 src/lin_fast.py                     # assembler self-tests on the 20-mode fixture and the s02 smoothing trial (identity L rho~ = 2 eps~ + rho~ - X.grad rho~/3)
python3 src/c2_fminus.py data/trial_v2_h0.008.npz 16 16 40 runs/c2/c2f_M16_s16_p4_re2.json 4 runs/c2/c2raw_M16_s16_p4_re2.npz   # raw section + _cols.pkl (85 min under the guard; 're2' = the saved regeneration whose pieces are shipped); the 7.4 table has ppc 1 and ppc 4 rows on the earlier grid (no cutoff radii)
python3 src/c2_gram.py  runs/c2/c2raw_M16_s16_p4_re2.npz runs/c2/c2gram_M16_s16_p4_H1m_NJ0.json 1e-10 0 H1m                 # Gram version 2 (7.4b (i)-(iii))
python3 src/c2_gram2.py runs/c2/c2raw_M16_s16_p4_re2.npz runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q.json 1e-10 1 H1m two H1q   # version 3; ROWS = L2|L2q|H1|H1q, NJ = 0|1
python3 src/c2_vec_profile.py runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz runs/c2/c2raw_M16_s16_p4_re2_cols.pkl Fminus 3   # localization of the weakest directions
python3 src/c2_img_eval.py runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz Fminus                                     # the same vectors under the four row functionals
python3 src/c2_gram_table.py; python3 src/c2_gram_summary.py > runs/c2/c2gram_summary.txt; bash runs/collect_v3.sh          # tables of 7.4b
python3 src/c2_Kproj.py A  data/trial_v2_h0.008.npz runs/c2/c2raw_M16_s16_p4_re2_cols.pkl runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz 1 1e-10 runs/kproj/Kproj2_M16_s16_NJ1.npz
for q in "0 90 p1" "90 180 p2" "180 260 p3"; do set -- $q; python3 src/c2_Kproj.py KT data/trial_v2_h0.008.npz runs/c2/c2raw_M16_s16_p4_re2_cols.pkl runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz runs/kproj/KT_$3.npz $1 $2; done
python3 src/c2_Kproj.py KTmerge runs/kproj/KT_images.npz runs/kproj/KT_p1.npz runs/kproj/KT_p2.npz runs/kproj/KT_p3.npz
python3 src/c2_Kproj.py B  data/trial_v2_h0.008.npz runs/c2/c2raw_M16_s16_p4_re2_cols.pkl runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz runs/kproj/Kproj2_M16_s16_NJ1.npz runs/kproj/KprojB2_M16_s16_NJ1.json
python3 src/c2_Kproj.py C  data/trial_v2_h0.008.npz runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz 0 8 runs/kproj/KC_m0_8.npz   # one piece; the 42 consecutive ranges (m_lo, m_hi) actually used (steps of 3 to 8 modes covering 0..260) are the list 'modes' of runs/kproj/KC_merge_all.json (in the lane also the file names `ls runs/kproj/KC_m*.npz`; only two pieces are shipped); Cmerge asserts complete coverage (each piece about 100 s)
python3 src/c2_Kproj.py Cmerge runs/kproj/KprojB2_M16_s16_NJ1_img.npz runs/kproj/KC_m*.npz runs/kproj/KC_merge.json
# 7.5 residual and refit diagnostics near P (floating)
python3 src/trial_jets.py                                                  # analytic jet tests (3 min)
python3 src/pdisc_norms.py data/trial_v2_h0.008.npz A runs/pdisc/norms_A.json   # grids B, C, D likewise
python3 src/pdisc_fft.py data/trial_v2_h0.008.npz 0.4 0.5 1e-3 runs/pdisc/fft_r0.5_k7.json 1.25 7
python3 src/pdisc_explore.py data/trial_v2_h0.008.npz 2.0668 2.2301 1e-5 runs/pdisc/explore_fine.npz   # eps_N(t) at 16331 radii (r = 7.9 .. 9.3; 64 MB, regenerable); input of wiggle_diag.py
python3 src/axis_diag.py data/trial_v2_h0.008.npz; python3 src/wiggle_diag.py
python3 src/smooth_band.py  data/trial_v2_h0.008.npz 1.7918 2.4849 0.0038 data/trial_b0.0038.npz
python3 src/smooth_band2.py data/trial_v2_h0.008.npz 1.7918 2.4849 10 0 10 data/trial_cC_lo10.npz       # coarse knots = every 10th knot, modes 0..9 smoothed (the 'cC' trial); input of gn_refit2
python3 src/gn_refit.py  data/trial_v2_h0.008.npz data/trial_b0.0038.npz 1.7918 2.4849 10 40 1e-3 data/trial_gnA.npz 3
python3 src/gn_refit2.py data/trial_cC_lo10.npz 1.7918 2.4849 10 0 10 100 1e-8 data/trial_gnCc.npz 2
python3 src/refine_knots.py data/trial_v2_h0.008.npz 2.0 2.33 data/trial_ref2.npz                        # exact knot insertion (138 midpoints) on [2.0, 2.33], as reported in 7.5b
python3 src/resid_smooth.py data/trial_v2_h0.008.npz 2.05 2.28 40 50 5e-4 data/trial_rs 0,1e-16,1e-15,1e-14,1e-13,1e-12,1e-11,1e-10   # settings of data/trial_rs_summary.json
python3 src/make_n7.py data/trial_v2_h0.008.npz data/trial_n7.npz 4                                     # the centre-regular trial N7
# 7.6 flow certificate (RIGOROUS; revision 2 of the code)
python3 src/cert_flow.py data/cert_green.npz data/trial_v2_h0.008.npz middle runs/flow_middle.json 200                             # 75 min
python3 src/cert_flow.py data/cert_green.npz data/trial_v2_h0.008.npz outer  runs/flow_outer.json  200 0 - data/cert_outer_green.npz
python3 src/cert_flow.py data/cert_green.npz data/trial_v2_h0.008.npz inner  runs/flow_inner.json  200 0 - data/cert_inner_green.npz
python3 src/cert_flow_tails.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz data/cert_inner_green.npz runs/flow_tails.json 256
python3 src/cert_axis_cell.py data/cert_green.npz data/trial_v2_h0.008.npz runs/scalars_full.json runs/axis_cell.json
python3 src/flow_summary.py > runs/flow_summary_all.txt
# 7.3b derivative certificate (RIGOROUS)
python3 src/cert_resid_deriv.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_deriv                                   # middle: runs/cert_deriv_middle.json (3.3 h)
DERIV_SKIP_MIDDLE=1 python3 src/cert_resid_deriv.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_deriv_regions data/cert_outer_green.npz data/cert_inner_green.npz   # regions only (runs/chain6b.sh): runs/cert_deriv_regions_{outer,inner}.json (5.3 h, 1.5 h)
python3 src/cert_deriv_summary.py runs/cert_deriv_middle.json > runs/cert_deriv_summary.txt
# 7.7 N8 mid run (the certified delta = 0.07 entry was produced with the v2 source, SHA-256 e7786de0..., as runs/n8/cert_n8_mid.json; the current v3 source
# reproduces it numerically (robustness items only); write the reproduction to a distinct file:
N8_DELTAS=0.05,0.06,0.07 python3 src/cert_n8.py data/cert_green.npz data/trial_v2_h0.008.npz runs/n8/cert_n8_mid_v3.json 8 350 0.07
# 7.7c / 7.10 decomposition and fractional orders (floating / post-processing of the certified merges)
python3 src/forcing_decomp.py 512 0.16 0.028875 0.037125 3.1 0.01,0.02 runs/n10/decomp_d0.0165_n512_L0.16.json
python3 src/forcing_orders.py runs/forcing/v22_p9_merged.json
# 7.11 X norms, the version-2 runs (1921 cells; the 1918-cell commands above are the superseded version 1)
python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 4 0 1921 runs/xnorm_jets/full_g4_v2.json; python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 6 626 969 runs/xnorm_jets/lobe_g6_v2.json
# shift 8 (2026-10-22, final): reproducibility checks (no number changed): hash table vs lane and artifacts; byte-identical regeneration of the trial files; clean-room rerun of the summary scripts
python3 runs/hash_check.py; bash runs/variant_regen.sh; python3 runs/variant_regen/compare.py          # 57 rows, 0 failures; 4 trial files regenerated (10 min) and hashed against the table: runs/variant_regen/compare.txt; fixtures: runs/variant_regen/fixtures_check.txt
# fresh-reader referee round on README + this section: astra repro1 (notes/astra_repro1_{question,answer}.md; 20 items repaired by notes/repairs/batch13.py: fixtures, aligned commands,
# flow_summary.py NameError and gz-blind guard, cert_summary.py gz glob, x3.py X3_COEFF_PATH / X3_EVALUATOR_DIR overrides, truncate_trial.py new); confirmation pass astra repro2
# (notes/astra_repro2_{question,answer}.md; 7 new items repaired by notes/repairs/batch14.py: checker scripts usable from the artifacts copy, hashes in the comparison records, wording);
# third pass astra repro3 (notes/astra_repro3_{question,answer}.md: 16 checks pass; 4 residual items repaired by notes/repairs/batch16.py: comparator JSON shipped, modes-file wording, CPU-guard description, one sentence)
# shift 7 (2026-10-22): directed-rounding tables, R2 tails, Arb X-norm ceilings
python3 src/report_tables.py > runs/report_tables.md; python3 src/report_tables.py --deriv > runs/report_tables_deriv.md
python3 src/export_boundaries.py   # cell-boundary balls of the three regions from the Green files -> data/cell_boundaries.npz (shipped, 314 KB)
python3 src/r2_tails.py; python3 src/xnorm_cert.py   # xnorm_cert v3 reads the Green files when present, else data/cell_boundaries.npz
```

SHA-256 of the CURRENT sources and data at 2026-10-22T06:52Z (previous stamps 2026-10-22T04:27Z, 01:47Z, 01:33Z, shift 7; shift 8 changed only flow_summary.py (the _jopen definition moved before its first use, gz-aware existence test), cert_summary.py (glob also *.json.gz) and x3.py (environment overrides X3_COEFF_PATH, X3_EVALUATOR_DIR for the two external paths; arithmetic untouched), and added src/truncate_trial.py and the fixture data/trial_small_M20.npz to the table). The arithmetic of the certificate scripts is unchanged since the producing versions pinned in the table
above and in the subsections, with ONE exception: xnorm_cert.py, whose versions 2 and 3 replaced the floating sums of version 1 by Arb ball arithmetic with exact
binary64 inputs and enclosed cell starts (same printed ceilings; v1 kept as src/xnorm_cert_v1_float.py, v2 as src/xnorm_cert_v2_arb.py). The other differences are:
cert_resid.py (robustness items of shift 4, lines above; the pinned producing hash 15a7535d... is in the table above), xnorm_BKK.py (docstring wording after
astra/bkk1; arithmetic unchanged), pdisc_fft.py / cert_forcing.py / c2_Kproj.py (usage docstrings completed in shift 7), xnorm_cert_v1_float.py (version 1 whose
hash below differs from the 4ea4f271... of the table above only by the gzip-fallback reader added in shift 7), and the summary/K-projection scripts (variants_summary,
cert_summary, cert_deriv_summary, deriv_region_shells, flow_summary, resid_summary_any, c2_Kproj, c2_vec_profile), which received the gzip-fallback file reader in shift 7
(I/O only). The producing version of every certificate output is the one named in its subsection; the per-cell JSON outputs listed here are unchanged since they were written.

| file | SHA-256 (current, 2026-10-22T06:52Z) |
|---|---|
| src/cert_resid.py | 1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053 |
| src/cert_green.py | ca9f6d37ed27bef9fc7f0d438750b4385bd8f53ef3703a2dac9824af893b2bac |
| src/cert_resid_deriv.py | 38e45bcd4400d119fb0a887794c4866bcc1d61eed1c3d69f58616eb7c95d5ac8 |
| src/cert_scalars2.py | b048d14fb3fa205c1e88a5f510f901fdc0e72b7de7a914df202f362401aedcd1 |
| src/cert_tail.py | 664600495e5f47e7bcd82a0dbe82fee338f5d70df092ccec1b3d4902f7ac589a |
| src/cert_inner_tail.py | 65c148e5e9b902242921dbbd8f514c52b8d49bbc1317e3451f75ce4e755c6d80 |
| src/cert_green_outer.py | aed9892b6b89720374c9ff4d6cbf5f455e2ea7c39572376675ea87a387d3b60e |
| src/cert_resid_regions.py | bcc078c9dcd4afeb24e33c3d785639375f16e9d133fd6f10027cf0fe76ad44ea |
| src/midrad.py | 5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e |
| src/cert_n8.py | 09849524feda01ba812b65b69f4939a8dd90b196027f5258dc63375c7181eb65 |
| src/cert_flow.py | bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6 |
| src/cert_flow_tails.py | ed09f5314afb4d08e6b48b7f391cb18393d405706786806ad4ee7bf7a9f784bb |
| src/cert_axis_cell.py | beb17ad73a09c609ac75e7c386914ad72a0039a228b514c0e99b65333ec1cbd2 |
| src/cert_forcing.py | 5355f20b488a59cda1fa14fda03526bb644dc7f73c53a2add1975f80cfd375db |
| src/cert_forcing2.py | 012e106b568ec68876058ee0588aa64cfbe9c846dc44523c164424015c238197 |
| src/xnorm_jets.py | 80febd2e62f103c22fe230775a59adebadb25fe87e7fc3e4d7b037a80970d7ff |
| src/xnorm_BKK.py | dd7f147d9b15111fdcfb73d5ab83439e276ba32c8d7914083b034e25e8855c9f |
| src/xnorm_cert.py | 5e8eb269a07fe6fcc0d57359aed856a99960f371c57aa079fe90d3156b065083 |
| src/xnorm_cert_v1_float.py | fa92858af71f93f4e81789fec52d089a7190472986ef0c9c68bdf95b865f0130 |
| src/r2_tails.py | 28712673383794841cf07f714cc3a1ed81c6f246e61e9c08a002cc252304a724 |
| src/report_tables.py | 13ee2ea37b28581e91179ba0548b8459e59411396e920159ec2df1e7fd3fda31 |
| src/variants_summary.py | 72cb82d0acd728b222d85b05e299c68a97e689cdde036a60cb37039298126f76 |
| src/cert_summary.py | d85e3704c38ab8e3fe010afcd39a460e96a5703183930ec98538d7b9fc0d9a75 |
| src/cert_deriv_summary.py | 46401cc2f33710cea2cf768623dddeaaaf9a68c39bcb113acfab9075410c6778 |
| src/deriv_region_shells.py | bf95b64865190f766bfb59c448816324db63c1fc3fecc347f3d4b74883be1de7 |
| src/flow_summary.py | 95ced265b4bd84a0886cd0ccb0ca4830879b3272416f9f6048527cad22fe3471 |
| src/resid_summary_any.py | b2e10ec3041d31d7b6a773d965520125c103759c2967471cf6bca3203dbcf5da |
| src/c2_Kproj.py | 3b23b8c80c1680b7dbb179265feeae70dac914c5737cb763199ec06fea15d02a |
| src/c2_vec_profile.py | 54f3c1fd1e4777601a9b31a091e0063ded93cf7a257952fa1c16b1991c43aa65 |
| src/c2_gram2.py | a25b610749dc45305e83480864903012d666a568e2db9e6ba082686fac98f3d9 |
| src/c2_fminus.py | a33328e5af7f8a951a0db4b10f71bc27f14333148397f0d80494e72d85f137ae |
| data/trial_v2_h0.008.npz | a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874 |
| data/cert_coeffs.json | 4c9caa2ddf2d2af0ebd2e494a78a8e0ffb18a2b5a1d5949a8e30a2c1f3ab9673 |
| data/trial_v3_h0.004.npz | 1e4ee66f1919e08de07fb0c9e85846aedf973c7872eda50f8881a57194b6a2dd |
| data/trial_v4_M230.npz | 11c97a14ac42f67da2696b440d70db112cbb3b667d06afaa0c1bb8ddfe43bde8 |
| data/trial_v5_R0knot2.npz | 74345bd9957269ad16a433e37a130f940f66cff79a579de01d6faf5cd3523f31 |
| data/trial_n7.npz | d026c5cfa9892683e1d8b07562bbfb506629cab76be20d5b9fa9c0bdf241443f |
| runs/scalars_full.json | c831175d41bde3377869e8461bc32057edff11a6bef1d69aa7f12b4134777fd2 |
| runs/cert_resid_middle.json | 88d2149248eaec2d868c7152859ba71d627e1162e2fa35ae2105a38531e1dd7a |
| runs/cert_resid_regions.json | e8848beb995140e70ee2615ef66a3961234d85e121031edb80d8ae60e6066177 |
| runs/cert_tail.json | 220c02d9276f4521f11ed4d4666d48d3039297ab7fe20e87590b19004273f3cf |
| runs/cert_inner_tail.json | 7d1c7f334d4042c37f282fefdf699f3d3d7ceab2e8754817970edf70917a666d |
| runs/cert_deriv_middle.json | 7408d122c9a8d0a214c48717cf4f43396533d811c992d47d70f1402febabe499 |
| runs/cert_deriv_regions_outer.json | 92a27641050b4b9e4ec497237bc83ccc6b643e1b72521f309b52ec4206551f7f |
| runs/cert_deriv_regions_inner.json | 5ab4a164ea9424ef64dba4af7296080f035165764545ef91e111404634d21bb4 |
| runs/xnorm/xnorm_cert.json | b06ebf67c05393f09f5bae2537f33fd31e28028e8c85daba1287e3c75d875f9b |
| runs/r2_tails.json | 8e4b3c38ce09e631b3bdab21278cfd8cda3d478025f2f6956f5d272f5e07f642 |
| runs/variants_summary.json | 305f98802c7c243a7719af8a3114d094407486a7b95ca9aeb9c06ac613d93b89 |
| src/xnorm_cert_v2_arb.py | f587ffbc5096a938806298f689413667c720bd369336184e87e3477f1e5c7210 |
| runs/report_tables.md | 3866c9372ad5a0d9ef95c588db6b02a7d43b41b57c5923b055093b080a0ec47e |
| runs/report_tables_deriv.md | 38f81d3c5c032fbf37de2a8bc983e06039494ce6a04cfce8d32642f5ab0ede16 |
| runs/report_tables_n8.md | 7d737dd20e74e92981db0abe304bd730c3ecdcc0e6946728ce54635cfe0b379d |
| src/export_boundaries.py | 64a74bc252c77e447c3bb96a54d8ff5931d3fecd590f178eb63808ba84b66e84 |
| data/cell_boundaries.npz | 8a6abb8b83abc508d830fa03f6f6861086f05660ae693a03227473b863b37941 |
| src/truncate_trial.py | 54291191748ae5671e16fd3aa9da0d973e1955c30e87a2857fb164c5a14eb7e0 |
| src/x3.py | 480b6230846092368690585747a8e502227e40f855d192bad61cec6e987308b2 |
| data/trial_small_M20.npz | 7481c3c0d4ec3b1327acfcb6bc3f2bf415525d04c34e0aea948b9b05f7af99ac |

## 9. Open items (numerics lane) (updated shift 7, 2026-10-22T02:37Z; shift 8, 2026-10-22T06:35Z, added no open item: its reproduction check of the four trial files and the clean-room rerun of the summary scripts are recorded in section 8)
0. Status at shift 7 (2026-10-22T02:37Z; the shift-6 text follows, with its statuses updated): C2 Gram (7.4b) complete as far as the report needs it (lead 18:37Z); X norms (7.11) analytic, refereed and repaired,
   B(K, K) done; the K-projection question (does the finite section see the scaling tangent K?) is answered in 7.4c (version 2, refereed by
   astra/kproj1, audited by ver topics 159/165): the sections represent K to 1.2 to 1.8 percent in X norm, K's row quotients (6.3e-5 in H1q) are
   three to five orders below the section minima and are reproduced by the section's own assembler from all 260 modes of K (stage C, 5e-5
   relative), while the sections' representatives of K have quotients 20 to 26 (far-field image of the remainder): the section minima are
   quotients over the span only. v4 is complete (22:14Z, 2026-10-21); v5 is complete (chain7d ended 02:23:19Z, 2026-10-22; collected into 7.3c by
   notes/repairs/collect_v5.py at 02:24Z).
1. Three resolutions (RES, section 7.3c): COMPLETE: v3 (radial refinement), v4 (angular truncation; middle +0.02 percent, outer +0.4 percent) and
   v5 (knot scheme 2, R0 = 1468; middle sup bounds equal to 5 digits; collected 2026-10-22T02:24Z) against the base trial; all tables with directed rounding.
2. N8 (section 7.7): complete; the verifier closed the condition on their own independent bounds (M_V < 0.2972, M_rho < 0.5059).
3. C2 (section 7.4b, floating): COMPLETE for the report (all sections of 7.4b (vii) collected by 18:31Z; M24/s8/Mout40 skipped for disk space,
   redundant for the Mout question; M = 32 out of reach with this assembler: its raw section would exceed both the 2 GB lane disk limit and the
   16 GB process memory limit). No conclusion about the invertibility of
   L follows from any of these sections (restricted trial space, truncated image, floating); the K-projection calculation of item 0 is done (7.4c).
4. Derivative certificate 7.3b and forcing bound 7.10: this lane's rigorous upper bounds; the verifier's queue (46, 98, 99, 101, 107) does not
   verify them at the physical level in this run (ver 11:58Z).
5. Far field: fitted (X3's Theta_1 mismatch retained) vs forced Theta_1 (lead's decision; not done). Band-vs-global Gauss-Newton comparison (7.5b
   design, about 2.5 h CPU) and the N7 inner-region certificate: optional, not started. Conforming B-spline reconstruction of the section
   columns (lead 12:34Z, optional): not started; the verifier's topic 132 quantifies the single-column repair (per-column broken-energy norm ratio
   ||h^ - h||/||h|| < 2.6e-14; not a bound for the squared energy of arbitrary combinations).
6. Rigorous forcing bound at other delta (about 9 x the work at delta = 0.05): routine, not needed for the report (lead 10:24Z).
