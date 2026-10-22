# Complete verification timeline (UTC)

Companion to section 7 of the final report, which gives the dated milestones. Section and result numbers refer to
the final report. P n is the proof or check packet of the independent verification whose written proof and summary
are in verification/proofs/ in the folder whose name begins with n; E, R and A identifiers (independent evaluation
reports, independent runs, and analytic consultations with the external referee) refer to records of the unpublished
working archives, and their verdicts are stated where they are cited. The entries of the first list were written
alongside the report as the events occurred, up to the entry for 4.41 (2026-10-22 00:44), and give every verification
event up to that time in full. The second list, at the end of this file, was added in one pass at 2026-10-22 11:05; it
reproduces verbatim the section 7 milestones of every result or group of results whose last event is after 00:44 on
2026-10-22. The itemized record of those later events is in the work logs of the analysis and of the verification,
which belong to the unpublished working archives. File names quoted inside entries are names of working files.

Entries of the first list are ordered by their first time; an entry may summarize later events and refer back to
earlier ones, whose times are given in the entry. The entry beginning "Grouped recap" is a grouped recap of the
independent numerical audits and is not part of this ordering.
- 2026-10-20 12:44 Start of the investigation (analysis, numerical computation and independent verification carried out separately).
- 2026-10-20 12:55-13:16 Independent verification rederived (B2-P), the reduced equations and the center identities
  (confirmed), and built and tested an independent modal Biot-Savart evaluator on manufactured fields.
- 2026-10-20 13:03 Specification of the admissible class, canonical inverse and diagnostics fixed.
- 2026-10-20 13:12 An independent Cartesian whole-plane inverse (Duffy quadrature plus compactified
  exterior) reproduced manufactured velocities to rounding error, including a slowly decaying field.
- 2026-10-20 13:23 Independent analytic referee: Theorem A, Propositions B (structure on the basin of the origin) and C
  (local beta = 2 arc), center identities and the vorticity representation VALID or VALID WITH FIXES (fixes adopted).
- 2026-10-20 13:25 Independent verification: Theorem E CONFIRMED under its hypotheses (with scope repairs); temperature integrability
  exclusion (4.5) proved independently.
- 2026-10-20 13:34 Independent verification: Theorem A, Proposition B, Proposition C CONFIRMED.
- 2026-10-20 13:42 Independent analytic referee: Theorem E VALID WITH FIXES, with the stronger conclusion stated in 4.6;
  a second referee report derived the temperature integrability exclusion independently and proposed the vorticity
  mass lower bound 4.8, which was then checked in the analysis.
- 2026-10-20 13:46 Independent verification: vorticity mass lower bound CONFIRMED (independent derivation); material-center translation
  eigenmode of the dynamic-rescaling linearization CONFIRMED (exact unstable direction, rate 1 + 3 beta/2).
- 2026-10-20 13:49 Check, in the analysis, of the independently derived beta = 2 analytic exclusion and flat-jet proof (4.7): VALID.
- 2026-10-20 14:03-14:29 Extension of 4.8 to sublinear velocity only (Omega not in L^p, 1 <= p <= beta): derived and
  CONFIRMED by independent verification (with an additional independent review), checked in the analysis (14:03) and VALID
  by an independent analytic referee (14:29).
- 2026-10-20 14:04 Independent analytic referee: 4.7(i) VALID WITH FIXES (minor), 4.7(ii) VALID, 4.8 VALID WITH FIXES
  (fixes adopted in the statement above).
- 2026-10-20 14:04-14:15 Temperature far field 4.10: proposed with proof by an independent analytic referee (14:04) and
  independently derived in the verification (14:15).
- 2026-10-20 14:18 Circulation identity and the slow-tail mass bound 4.9 derived in the analysis for all beta >= 2 (generalizing
  a beta = 2 argument from an independent analytic referee report).
- 2026-10-20 14:28-14:34 Independent verification: 4.9 CONFIRMED with repairs by an independent derivation (positive-part form of the
  signed conclusion; trajectory interpretation only conditional), including the critical exponent p = 2 beta under
  sublinear velocity alone.
- 2026-10-20 14:32-14:35 Independent verification: sector form of the circulation bound (4.11(i)) derived, including the regular-level
  escape argument at beta = 2 (that step also reviewed by an additional independent reviewer at 14:35). Earlier (14:03) independent verification had
  confirmed the flatness of Omega in 4.7(ii).
- 2026-10-20 14:33 Independent analytic referee: 4.9 Steps 1-3 VALID, the mass bound VALID, one signed half-ball claim
  INVALID (replaced by the positive-part statement above), the critical p = 2 beta case and the upgrade from sublinear to
  power-bounded velocity VALID.
- 2026-10-20 14:51 Independent referee review of the full interim report: the principal arguments sound under the class A
  hypotheses; required clarifications (velocity constant and drift in (A5), standing hypotheses, a proof outline for
  4.3(ii), details in 4.6-4.8, scope of the restrictions section) adopted in this version.
- 2026-10-20 14:58 Check, in the analysis, of 4.11(i) and of the corollaries 4.11(ii)-(iii) and 4.7(ii) (flat Omega); sent to an
  independent analytic referee.
- 2026-10-20 15:00-15:04 Independent verification: scattering under the orbit-integral hypothesis (D) without a separate power bound on
  the velocity (independent derivation, also reviewed by an additional independent reviewer): CONFIRMED.
- 2026-10-20 15:06 Independent analytic referee: 4.11(i) (all steps, including the beta = 2 regular-level lemma), 4.11(ii),
  the sector-mass remark and the flatness of Omega VALID; 4.11(iii) and the positive-sign drift statement VALID WITH FIXES
  (uniform crossing constants; "every sufficiently large R"; the gauge meaning of v0), adopted.
- 2026-10-20 15:07 Independent verification: 4.11(ii) and (iii) CONFIRMED (independent check, agreeing with the referee's scope
  qualifications).
- 2026-10-20 15:12-15:22 Axis structure 4.13: positive-vorticity version and the one-equation example proposed by an
  independent analytic referee report; the analysis extended (i)-(iii) to the sign-free case and checked the example's
  center jet.
- 2026-10-20 15:22-15:41 Axis structure 4.13(v)-(vii) (analysis); independent proofs (on axis zeros and
  global axis parity) CONFIRMED by 16:07, with the homogeneous q mode read relative to a smooth particular solution.
- 2026-10-20 15:26-16:07 Independent verification: 4.13(i)-(iii), the parity statement, the center imbalance and the one-equation example
  CONFIRMED by independent proofs.
- 2026-10-20 15:28 Independent analytic referee: (D)-scattering, the transport identities and the exclusion of 4.6 under
  (D) VALID (one exponent inequality in the L^p bookkeeping corrected, adopted); (D) not implied by smoothness,
  sublinearity, parity and the center data (shear example, adopted in the scope remark). 4.6 restated with (D) in place
  of the power bounds (H1).
- 2026-10-20 15:28 Independent analytic referee: 4.13(i)-(iii) VALID, with the stronger arithmetic (d and r = beta d
  integers) and the parity of r + d (adopted, checked in the analysis 15:32).
- 2026-10-20 15:35-15:50 Literature 4.14: primary texts retrieved and quoted in the analysis.
- 2026-10-20 15:53 An independent analytic referee report proposed 4.12(a)-(c) with a proof (steps (1)-(4)); every step
  was rederived in the analysis (15:55-16:00).
- 2026-10-20 16:02 Independent verification: 4.12 CONFIRMED by an independent second proof (Hoelder estimate for the transported
  temperature on rescaled annuli and a second integration by parts) and by an independent rederivation of the referee's
  proof, including the uniform polar tail (d) and the sharp rate (e).
- 2026-10-20 16:04 Class reduction 4.15 under vorticity tending to zero (analysis). 16:18 Independent analytic referee: VALID
  WITH FIXES (sublinearity of the canonical integral must be shown before harmonic uniqueness; adopted), with the
  extensions to bounded vorticity and to beta = 2 without a vorticity assumption; the moving-frame
  identities were checked in the analysis (16:24). 16:27-16:31 Independent verification: all three cases CONFIRMED by an independent proof (local inverse and
  moving-frame gradient argument).
- 2026-10-20 16:06 Independent analytic referee audit of 4.12: (a)-(c) VALID WITH FIXES (exponent bound (0) placed first,
  absolutely convergent form of the far strain integral, frozen cutoffs, profile-dependent constants); the uniform polar
  tail (d) VALID WITH FIXES (global bijectivity of the scattering map, uniform remainder bound in step (7)); scope VALID
  (no nonexistence follows; the leading-order equations alone do not constrain the leading homogeneous terms). Fixes adopted.
- 2026-10-20 16:07 Independent verification: literature verdicts CONFIRMED with corrections (wall wording, the rotational hypothesis of
  Abe-Ginsberg-Jeong, the extra Euler identity in Chae-Tsai). 16:08 Independent analytic referee: verdicts VALID WITH
  FIXES, one decay inference INVALID as written (corrected). Both sets of corrections adopted (16:15).
- 2026-10-20 16:15 Independent verification: second far-field terms 4.16 CONFIRMED (independent proof via the local regularity theorem of
  Chae and Wolf, hypotheses checked against the primary text, and a local derivative-propagation lemma); 16:37
  independent analytic referee: VALID (editorial clarifications only, adopted).
- 2026-10-20 16:27 Independent analytic referee: 4.13(v), (vi) VALID WITH FIXES (keep the smooth factor in the
  asymptotics; components of {b != 0}; analyticity on a neighbourhood of the whole axis; the nonzero-a hypothesis), (vii)
  VALID. Fixes adopted.
- 2026-10-20 16:27 Independent verification and independent analytic referee: the sign statement 4.12(f) CONFIRMED and VALID.
- 2026-10-20 16:31-16:47 Independent verification: velocity terms of 4.16 CONFIRMED (independent proof; a manufactured inverse test
  reproduces a prescribed relative velocity to 2.05e-12 and the beta = 2 constant C = -0.4 to 2.2e-16 for three cutoff
  scales). 17:11 Independent analytic referee: VALID (all items, no correction). Entered 17:12.
- 2026-10-20 16:37 Independent verification: extension of 4.15 to polynomially bounded vorticity CONFIRMED (local strain bound
  C[M + A/r] log(2 + M) and finite exponent iteration). 16:47 Independent analytic referee: VALID (all steps), with one
  wording fix (only U - U(0) is identified with the canonical integral; adopted). Analysis check of the exponent
  iteration 16:53.
- 2026-10-20 16:44 beta = 2 arc structure and the critical flux identity derived by an independent analytic referee
  (research question, no closure); check and generalization in the analysis of the identity to every beta >= 2, 16:44-16:48. 16:58
  Independent analytic referee (audit of the stated results): arc structure, endpoint flatness, analytic exclusion
  near the arc and the critical identity VALID; endpoint alternative VALID WITH FIXES (the outgoing open set is built
  from backward limits, not from an assumed foliation; adopted). 17:02 Independent verification: 4.7(iii), 4.7(iv)(b) (by an elementary
  backward-invariant wedge) and 4.12(g) CONFIRMED by independent proofs. Entered 17:05.
- 2026-10-20 17:21 Global-source subclass derived by an independent analytic referee (research question, no closure):
  global area-preserving coordinates with a triangular normal form, two shape-restricted exclusions, decay and quadratic identities in the subclass; check in the
  analysis 17:21-17:24 (the parity argument for the coordinates by uniqueness of the linearization proposed there was
  wrong, see 17:27).
  17:27 Independent verification: K = {0} CONFIRMED; the uniqueness argument REFUTED (an explicit second C^1 conjugacy) and the
  coordinates CONFIRMED by an explicit area-coordinate construction. 17:37 Independent analytic referee (audit): all items
  VALID, the coordinates VALID WITH FIXES (constructive parity, even resonances only); the decay with axis factor, the
  quadratic identities and the critical-weight identity extend to all of class A with beta > 2. 17:39 Independent verification: the
  shape exclusions, decay and identities CONFIRMED, including the class A extension. Analysis check of the class A
  extension and of the axis elimination 17:40. Entered as 4.17 and 4.18 at 17:44.
- 2026-10-20 17:34 beta = 2 zero-set structure (Z = gamma), the analytic boundary exclusion and the scattering
  identities derived by an independent analytic referee (research question, no closure); checked in the analysis
  17:34-17:40. 17:52 Independent analytic referee (audit): all items VALID, two VALID WITH FIXES (explicit local
  endpoint basin argument; the analyticity hypothesis concerns the germ at the endpoint), adopted. 18:01 Independent
  verification: all items CONFIRMED by independent proofs, including a separate complex-reflection proof of 4.7(vi).
  Entered as 4.7(v)-(vii) at 18:13.
- 2026-10-20 17:56 Second independent referee review of the full interim report (state of 17:37): required
  clarifications and scope corrections (standing hypotheses of 4.7(iii)-(iv), 4.9(iii) and 4.10; the notation for the
  trajectory amplitude; the global basin and smoothness of the example of 4.13 and the third-order condition it fails;
  the derivative-propagation lemma in 4.16; the observer convention; the definitions and limitations of the numerical
  residuals; the wording of sections 5 and 6). Adopted 17:57-18:10.
- 2026-10-20 18:01 beta = 2 strict-sign exclusion (a maximum orbit of the temperature with zero vorticity, and a zero of
  the angular vorticity tail in the open right semicircle): independent verification, CONFIRMED by its own proof; checked
  in the analysis 18:13. 18:23 Independent analytic referee (audit): all steps VALID; the corollary VALID with the
  scattering map and uniform tail of 4.12 as explicit inputs; the analogue for beta > 2 INVALID. Entered as 4.7(viii)
  at 18:23.
- 2026-10-20 18:16 Weak-sign consequences (no horizontal escaping orbit, beta >= 2; degenerate critical points of h,
  beta = 2): independent verification, CONFIRMED by its own proof (with an additional independent review); checked in
  the analysis 18:24. 18:34 Independent analytic referee (audit): both parts VALID WITH FIXES (sign convention of the
  stream-function coefficient, uniform angular convergence at a varying angle, boundedness of Omega), adopted; the
  angular part does not extend directly to beta > 2. Entered as 4.7(ix) at 18:36.
- 2026-10-20 18:17 Zeros of W off the center (beta > 2): derived by an independent analytic referee (research
  question, no closure); checked in the analysis 18:19. 18:27 Independent analytic referee (audit): all items VALID,
  two with proof completions (graph coordinates for limit sets; Theta = x^2 H by Taylor's integral formula), adopted,
  and the strengthening to nondegenerate axis zeros. 18:32 Independent verification: CONFIRMED by its own proof (with
  additional independent reviews). Entered as 4.19 at 18:37.
- 2026-10-20 18:26 Finite-order critical directions under a weak sign (beta = 2): derived in the analysis (draft 18:32).
  18:45 Independent analytic referee (audit): VALID WITH FIXES (symmetric contraction in the jet equations, symmetry of
  DW at the backward limit, strict saddle threshold, flatness stated for h and for the physical fields, the sign
  alternative fixed by Omega_x(0) = 2a0), adopted. 18:56 Independent verification: CONFIRMED by its own proof (exact
  symbolic checks of the product rule, explicit backward estimate, exact local fields, not profiles, for which the
  backward-growth step fails at the saddle threshold). Entered as 4.7(x) at 19:03.
- 2026-10-20 18:32 to 23:33 Sign accumulation on interior fibres at beta = 2, 4.7(xi): complete proof by the
  independent verification (18:32); main theorem CONFIRMED by the verification 18:39 and the conditional monotonicity
  corollary 18:54; drafted for the report by the analysis and audited by a referee (VALID, 23:13; clarifications
  adopted: the orbit of alpha_* lies in {x > 0}, the accumulation argument is applied at every orbit point, the
  corollary uses local angle maps only); the draft text CONFIRMED against the full proof by the independent
  verification 23:21, including the no-constant-subarc hypothesis and the restricted scope of the endpoint example;
  entered at 23:33 with its scope paragraph and the summaries in Q1 and section 6; the entered text CONFIRMED by the
  independent verification 23:39.
- 2026-10-20 18:34 Critical points of Theta on escaping orbits under a weak sign, every beta >= 2: the vanishing of the
  physical Hessian along the orbit was proposed by an independent analytic referee in the audit of the beta = 2 weak-sign
  results. 18:56 Independent verification: CONFIRMED by its own proof, together with the extension to odd finite order
  at a backward limit without a negative eigenvalue. 19:07 statement drafted in the analysis. 19:16 Independent analytic
  referee (audit): VALID WITH FIXES (completeness of the flow from the linear growth bound |W| <= C(1 + |X|); the
  odd-degree vorticity Taylor term described as forced to vanish rather than as a nonzero leading term; the backward
  limit cannot be the center; the sign alternative fixed by the sign of a0; no existence of such orbits asserted),
  adopted. Entered as 4.20 at 19:19.
- 2026-10-20 18:42 Independent verification of 4.19: CONFIRMED with a required scope correction (necessary arithmetic
  conditions do not establish full resonant configurations); corrected 18:53. 18:47 and 18:54 independent convention
  audits: the stream function in the proof of 4.18(c) had the wrong sign (the velocity used, and the exclusion, were
  correct), corrected 19:01; the attribution of a self-source inverse check corrected to Table 6.1b, 19:00.
- 2026-10-20 19:29 Citation details of 4.14(a) (arXiv versions, theorem numbers, equation numbers of the constants and
  of the decay bounds), requested by an independent analytic referee: checked in the analysis against the primary text
  of 2210.07191v4 and v3; the v3 constants differ in the seventh (c_l) and ninth (c_omega) significant digits and
  are recorded alongside.
- 2026-10-20 19:33 Axis tails and the vertical slopes of the angular tail in G: derived by an independent analytic referee
  (research question, no closure of G); re-proved in the analysis 19:39 for every class A profile on a half-axis
  without a zero of W (rates), with the slopes in G via the scattering map. 19:43 Independent analytic referee (audit):
  VALID WITH FIXES (compact-set bounds, positivity of the diagonal of D Phi on the axis, a product difference quotient,
  sharpness only for beta > 2), adopted. 19:47 Independent verification: CONFIRMED by its own proof, with a
  strengthening (the slopes and h'' on every half-axis without a zero of W, for every class A profile, from the C^j
  expansions of 4.16), adopted. 19:58 Independent analytic referee (audit of the final text): VALID WITH FIXES (scope
  of the sharpness statement, the flow derivative factor in the Remark, wording of the numerical test), adopted.
  Entered as 4.21 at 20:00.
- 2026-10-20 19:37 Second independent re-read of 4.7(x), 4.9(iii), 4.13, 4.16(2) and 4.20 as entered: no substantive
  gap at the stated hypotheses; three wording repairs adopted (the answer to Q1 in section 5 called both global coordinates
  eigen-coordinates, which fails in the resonant case; a slot count in the proof of 4.7(x); a one-way implication in the
  specification summary of 4.19).
- 2026-10-20 19:53 The temperature tail in G (representation through the scattering map, positivity off the vertical
  directions, two-sided bound for Theta/x^2, level-curve asymptotics, angular area identity in the linearizable case,
  and an explicit map showing that this geometry alone does not give Theta_x >= 0): Independent verification,
  CONFIRMED by its own proof (recorded 19:56); re-derived in the analysis 19:54. 20:00 Independent verification of the
  draft text: CONFIRMED, with one dependency to state (smoothness of the scattering map), supplied. 20:03 Independent
  analytic referee (audit): (a)-(c) VALID, (d) VALID WITH FIXES (the normalization xi_x(0) = 1 and the smoothness of
  the scattering map), the example VALID with a narrower scope sentence, adopted. Entered as 4.22 at 20:06.
- 2026-10-20 20:14 Independent verification of 4.21, 4.22 as entered (including the smoothness proof of the scattering
  map and the exact inequality of the example): CONFIRMED; the Q1 summary sentence REFUTED as worded (sign of the lower
  slope, and positivity only in the right semicircle). Q1 corrected at 20:15.
- 2026-10-20 20:19-21:06 Homogeneous-weight identities and the strain identity (4.23): derived in the analysis 20:19;
  independent derivation (with completeness, the two-blob sign example and the restricted exclusions) 20:36;
  independent verification 20:46: CONFIRMED, with two scope repairs (consistency shown for the single identity only;
  radial blobs), adopted; independent analytic referee (audit) of the draft 20:50: VALID WITH FIXES (bounds, strips,
  kernel grouping, flux sign, angular factor), adopted. Final text: independent verification 20:59 CONFIRMED and
  independent referee 21:01 VALID for (a)-(d), (f), each with the same two corrections: the sign inference in (e) was
  corrected (the zero integral forces a positive product a0 C_m P somewhere without a fixed sign of P; a separate far-field
  argument supplies a point where both factors have the required signs), and the scope paragraph may not assert
  nonexclusion; both corrected. Entered as 4.23 at 21:06.
- 2026-10-20 20:43 Independent verification of the literature items 4.14(f), (g) (arXiv:2604.01868 and
  arXiv:2310.19780): CONFIRMED with two repairs, adopted; 21:04 independent literature referee: both VALID WITH FIXES
  (the meaning of "regular" in the first, the conditional status of its Lemma 6.1, the explicit change of coordinates
  in the second), adopted. Entered at 21:06.
- 2026-10-20 21:41 Third independent referee review of the full interim report (20 items; no YES or NO supported).
  Checked item by item in the analysis and adopted at 21:50: a stream-function description in 4.7(ix)(A); the backward
  convergence step of 4.7(v) (integrating factor on the side u > 0); the analytic reflection step of 4.7(vi) (an analytic
  P with zero Cauchy data on the analytic curve, so the Dirichlet trace of H is not used); step (2) of 4.7(viii) (no
  invariance of the axis under its weaker hypotheses); the equality case of 4.7(x) (the earlier claim of examples for the
  even-order conclusion withdrawn; explicit local fields for the failure of the backward-growth step stated); the
  rotation J_+ in 4.19(c); the normalization a0 > 0 in 4.7(v), (vii), Q1, Q2(c) and section 6; the beta ranges for G;
  the signed circulation wording in Q1; the scope of 4.23(c) in sections 6 and 6.2; the heading of 6.2; notation
  collisions; definition and reference targets; the scope of 4.15; the zero-denominator wording of 6.1; this
  timeline's order. The artifact manifest and the final time accounting are completed at the end of the run.
- 2026-10-20 21:57 Independent verification of the referee repairs of 21:50 (the four proof repairs and the sign and
  normalization wording): CONFIRMED, with one precision in step (3) of the proof of 4.7(v)-(vii) (the backward basin of
  an outgoing endpoint also contains the two branches of its strong unstable curve), adopted at 22:05.
- 2026-10-20 22:14 to 22:43 Second construction of 4.23(c) (smooth nonprofile fields with exact (T) on the whole plane,
  exact (S), the center, decay and flow conditions, failing (V) on an interval): complete proof by the independent
  verification 22:14; checked by the analysis 22:25 (local fields, radial bound, the moment formula by hand and by
  quadrature); VALID WITH FIXES in an independent referee audit 22:38 (surviving angular interactions and boundary
  terms stated; strip of k; the flow condition of G stated precisely, these fields not being profiles; the vorticity
  of the second construction changes sign; only one identity of the first family is established); fixes adopted and
  entered at 22:43, with the scope paragraph of 4.23 and the summaries in Q1, section 6 and 6.2.
- 2026-10-20 22:18 Two wording corrections from the independent audit of section 6.1 adopted at 22:20: the starting state
  of the additive-source path is not an exact root at lambda = 1 (it carries the residual of its fitted seed) and the
  source is re-projected when beta changes; the completion table states that no small-residual (B2-P) state has been
  found (not that none exists).
- 2026-10-20 22:20 and 22:23 Literature items 4.14(h)-(j) (Type I criteria of Chae-Wolf and Chae-Constantin, the
  half-plane Liouville statement of Zhang, the numerical wall profiles of Wang et al.): the derivations (center
  pressure Hessian, direction limits, failure of every quantitative criterion, unbounded velocity by Stokes' theorem,
  the local qualitative hypotheses, the parameter translations) CONFIRMED by independent verification against
  independently retrieved primary texts, and VALID WITH FIXES in an independent referee audit; the corrections (dilation
  comparability rather than invariance of the dyadic Besov norm; Zhang's exponent relation matches B2 for beta > 2, his
  conditions compare two radial suprema and do not require an interior maximum; condition (iv) fails through its
  vorticity integral only; Type I gradient rates outside the global Sobolev class; the residual meaning in Wang et al.)
  adopted, and the items entered at 22:25.
- 2026-10-20 22:28 Independent evaluation of the additive-source state at lambda = 0.97 (forced residuals 0.036/0.050
  for the intended fixed source, (B2-P) residuals 0.75/0.48; REFUTED as a small-residual (B2-P) state), of a further
  beta = 2.25 state and of three forced states with a second external dipole (forced 0.012 to 0.016 / 0.019 to 0.025,
  (B2-P) 0.91 to 1); regional absolute and normalized maxima produced from the saved raw arrays of 35 states; audit of
  Table 6.1c: rows correct with the stated scope, except that the Jacobian row omitted recorded singular-value
  diagnostics (REFUTED as worded) and the far-field row omitted measured exponents; both rows and the additive-path
  sentence of 6.1 corrected and Table 6.1d added at 22:36. The audit also CONFIRMED the entered text of 4.14(h)-(j).
- 2026-10-20 22:34 to 23:01 Exclusion of finite angular Fourier support, 4.24: complete proofs by the independent
  verification (stream and temperature support 22:34, vorticity support with the Fourier division lemma 22:41), with
  partial referee audits of the highest-mode ODE (22:40) and of the division lemma (22:43) found VALID; every step
  re-derived by the analysis 22:46 to 22:49 (highest-mode coefficients and reflection phases, the three signs of the
  first case, the tail and endpoint analysis of the second case with the matching of constants, the division lemma,
  the step from vorticity to stream function); CONFIRMED without gaps in an independent referee audit of both full
  texts 22:57; entered at 23:01 with its scope paragraph and the summaries in Q1, section 6 and 6.1.
- 2026-10-20 22:42 to 22:50 Independent evaluation of two further forced states with the second external dipole
  (a0 = 12 and 15; forced 0.017/0.027 and 0.019/0.030, (B2-P) 1/0.99; REFUTED as small-residual (B2-P) states); the
  entered text of 4.23(c) CONFIRMED by the independent verification (22:50); the step-change sentence of Table 6.1d
  found too imprecise and replaced by the separate global and regional values at 22:52.
- 2026-10-20 23:09 to 23:33 Nonstationarity of the homogeneous far-field limit, 4.25: derived by the analysis 23:09;
  referee audit VALID WITH FIXES (the identification with the physical limit as t -> 0 is the locally uniform limit of
  step (1) of 4.16, and one citation was replaced by the uniqueness of f; adopted 23:17); CONFIRMED by an independent
  complete proof of the verification 23:21 (including beta = 2, arbitrary zero sets of f and bounded a); entered at
  23:33 with the summaries in Q1 and section 6; the entered text CONFIRMED by the independent verification 23:39.
- 2026-10-20 23:10 to 23:37 Independent evaluation (separate evaluator, 34 s) of the beta-free stage eps = 0.025 (beta
  = 2.4402; forced 0.19/0.14, (B2-P) 0.86/0.54) and of the second-dipole state at a0 = 20 (eps = 0.010962; forced
  0.020/0.032, (B2-P) 1/0.99), all inverse flags zero, reported 23:17; no candidate; entered in section 6.1 at 23:37.
- 2026-10-20 23:12 to 23:33 Third construction of 4.23(c) (smooth nonprofile fields with Omega > 0 on {x > 0}, exact
  (T) on the whole plane, W.X >= kappa |X|^2, a slow tail and (S) exact, for which (V) fails on the far positive
  x-axis): complete proof by the independent verification 23:12; re-derived by the analysis 23:17; referee audit VALID
  WITH FIXES 23:27 (value of DW at the origin only, the moment bound applied to xi^2 so that it holds where a0 = 0,
  the passage from trajectory asymptotics to the fixed horizontal ray spelled out), adopted 23:28; theorem CONFIRMED
  by the independent verification 23:21, which REFUTED one local estimate of the draft (the integrand of the
  eigen-coordinate is O(|X|), not O(|X|^2); the weaker bound suffices for every conclusion), corrected 23:31; entered
  at 23:33 with the scope paragraph of 4.23 and the summaries in Q1, section 6 and 6.2; the entered text CONFIRMED by
  the independent verification 23:39, with one editorial precision (the circle diffeomorphism is the normalized map
  Z/|Z|), made at 23:44.
- 2026-10-20 23:17 to 23:43 Second temperature coefficient on a free half-axis, second part of 4.25 (d is not
  identically zero if one half-axis carries no zero of W, any beta >= 2): proposed by the independent verification
  23:17 and CONFIRMED there 23:25 (complete proof, exact symbolic checks); re-derived by the analysis with a symbolic
  check of the Taylor coefficients, the reflection and the beta = 8 example 23:36; referee audit VALID 23:42
  (clarification adopted: on each component of {f != 0} the constant in h = C |f|^{m/k} may differ); entered at 23:43
  with the scope sentence of 4.25 and the summaries in Q1 and section 6; the draft wording had been CONFIRMED against
  the full proof by the independent verification 23:39.
- 2026-10-20 23:27 to 23:45 Independent evaluation (separate evaluator, 72 s) of the beta-free stage eps = 0.03 (beta
  = 2.3886; forced 0.23/0.16, (B2-P) 0.88/0.61) and of the two fixed-source additive-forcing states at lambda = 0.99
  (beta = 3.0019 with 12 and 3.0020 with 16 angular modes; forced 0.037/0.051 and 0.0060/0.011, (B2-P) 0.75/0.49 and
  0.75/0.48), all inverse flags zero, effective sources reproduced exactly; REFUTED as small-residual (B2-P) states,
  reported 23:40; entered in section 6.1 at 23:45.
- 2026-10-20 23:35 to 23:56 Exact endpoint expansion of the stored representations of six archived states (independent
  verification: own derivation and exact rational arithmetic on the stored coefficients, 0.84 s, CONFIRMED); formulas re-derived in
  the analysis with a symbolic check at 23:48 and audited by an independent referee (VALID WITH FIXES at 23:56; the fixes
  are precisions of the hypotheses: differentiated remainder bounds, which the spline and Fourier representation
  supplies, the knot convention of the endpoint slope, and rational weights of the velocity source); entered in
  section 6.1 at 23:56.
- 2026-10-20 23:45 to 2026-10-21 00:08 Third far-field terms and the constant velocity, 4.26: derived and CONFIRMED by
  the independent verification (written 23:45; exact Cartesian identities at beta = 7/3, 5/2, 8/3 and 4 and a
  manufactured inverse with a known constant velocity, 23:51); re-derived step by step by the analysis 23:58 to 00:00;
  independent analytic referee VALID WITH FIXES at 00:07 (the exponent support of the representation in (c) made
  explicit, adopted; a center-correction formula of the manufactured test needs a factor a0 and is not used here); the
  draft wording, before the added derivation of the exponents in (c), CONFIRMED against the full proof by the
  independent verification 00:06; entered at 00:08 with the summaries in Q1 and Table 6.1c.
- 2026-10-20 23:53 to 2026-10-21 00:23 The resonance at beta = 3, 4.27: derived and CONFIRMED by the independent
  verification (written 23:53; 30 exact Cartesian checks and a manufactured inverse with a known constant); the
  example (d) written 00:09 and CONFIRMED by 9 exact Cartesian identities and 3 exact examples (00:20); re-derived by
  the analysis 00:13 to 00:16 with symbolic checks of the integration identity, the mode-1 inverse, the logarithmic
  velocity, the manufactured source and its moments, and the formula of (d); independent analytic referee VALID at
  00:21 (precision: the rescaled expansions are used in spatial C^j norms on annuli, stated in the proof); the draft
  wording CONFIRMED by the independent verification 00:20 (with "may contain logarithms" in Q1, adopted); entered at
  00:23 with the summaries in Q1, Table 6.1c and the endpoint paragraph of section 6.1.
- 2026-10-20 23:56 to 2026-10-21 00:09 Independent evaluation (separate evaluator, 67 s) of the beta-free stage eps =
  0.035 (beta = 2.3465; forced 0.30/0.20, (B2-P) 0.89/0.68) and of the two fixed-source additive-forcing states at
  lambda = 0.98 (beta = 3.0027 with 12 and 3.0029 with 16 angular modes; forced 0.036/0.050 and 0.0063/0.010, (B2-P)
  0.75/0.49 and 0.75/0.47), all inverse flags zero; REFUTED as small-residual (B2-P) states, reported 00:05; entered
  in section 6.1 at 00:09. In the same report the paragraph of section 6.1 on the exact endpoint expansion was
  CONFIRMED with two wording fixes (the expansion is that of the signed residual R_Theta; the normalized limits are
  those of |R_Theta|/N_Theta and |R_Omega|/N_Omega) and the beta value 3.0020 CONFIRMED; fixes adopted at 00:09.
- 2026-10-21 00:17 Independent evaluation (separate evaluator, 21 s) of the 12-mode fixed-source additive-forcing
  state at lambda = 0.97 (beta = 3.0037; forced 0.036/0.050, (B2-P) 0.75/0.48), inverse checks passed; REFUTED as a
  small-residual (B2-P) state, reported 00:20; entered in section 6.1 at 00:23. The same report corrects the start of
  the evaluation of the eps = 0.035 and lambda = 0.98 states to 23:56 (adopted at 00:23).
- 2026-10-21 00:24 to 03:09 Later lambda-path stages (section 6.1): independent evaluations of the 16-mode states with
  the source fixed in its seed basis at lambda = 0.97 (00:24) and 0.96 (01:11), with exact positivity certificates for
  their temperatures, F > 0 and 2F + x F_x > 0 on R^2 (01:46; CONFIRMED), and of the 12-mode state at lambda = 0.96
  (00:48; REFUTED as a candidate; entered in section 6.1 at 03:33); independent evaluation of the 16- and 24-mode
  states at lambda = 0.96 stored in the basis of their own beta, with exactly nonzero temperature tail coefficients
  and exact C2 enclosures (02:58; CONFIRMED; no candidate; the rounded E_T values of these two states rounded from the
  exact rational witnesses). Independent re-read 02:54 of the restructured Q1 and section 6 openings:
  scopes CONFIRMED; the phrase "(V) beyond its center jet" replaced in five places by "(V) beyond the leading center
  identities" and the axis coefficient a of the 6.2 axis bullet distinguished from the angular tail, as requested.
  Entered 03:09.
- 2026-10-21 00:31 to 01:22 (beta = 3 resonance coefficient of the stored states). Independent verification: the stable
  logarithmic constant of a stored beta = 3 representation (written 00:31, checks complete 00:37: 21
  manufactured cases, 114 exact endpoint checks, high-radius whole-plane inverse cross-check); its alpha values for the
  two beta = 3 states with 20 modes are exact rational evaluations. Check in the analysis 01:16: first-cosine projection and
  alpha = L^2 S''(1)/2 rederived; the spline combination re-extracted from the stored arrays agrees bit for bit with
  the inputs of the verification, and a separate rational derivative recursion reproduces -9.22571252614018 and
  -12.324566941468. Independent analytic referee 01:21: VALID WITH FIXES (the exterior expansion holds beyond the radius of the last interior spline knot,
  with remainder O(r^{-5/3}), which meets the hypothesis of 4.27(c); the phrase "even if its residual vanished at
  every finite point" replaced by the statement that the residuals cannot all vanish identically). Entered in
  section 6.1 at 01:22, together with the same rewording of the 4.26(c) sentence on the four beta-free states.
- 2026-10-21 00:32 to 00:37 Independent evaluation (separate evaluator, 18 s) of the beta-free stage eps = 0.04
  (beta = 2.3119; forced 0.41/0.24, (B2-P) 0.90/0.75, all inverse flags zero), REFUTED as a candidate; closed form
  for the constant C of the stored representation (2 < b < 3) derived and CONFIRMED by the independent verification
  with an exact identity check, re-derived by the analysis (00:26, numerical cross-check about 4e-9), independent
  analytic referee VALID WITH FIXES (00:34; fixes adopted by the verification 00:37); the verification established
  b = beta exactly for the four stored eps states and computed their constants C (00:37); entered in section 6.1 at
  01:00.
- 2026-10-21 01:00 to 02:23 (transport-exact generating-function representation, section 6.2). Mixed-chart formulas
  CONFIRMED by the verification (01:13, including the resonant-term correction); pilot closed 01:37 with no
  candidate; independent evaluation of the three saved states by separate high-precision differentiation (02:03):
  REFUTED as candidates (residual ratios 0.97 to 1.0, Omega < 0 at points of x > 0). Entered in 6.2 at 02:23.
- 2026-10-21 01:03 to 01:52 (noninteger beta > 3 analogue of 4.26(c), 4.26(d)). Independent verification with its own proof
  (written 01:03; scoped statement CONFIRMED 01:06 after 54 exact exponent checks and 8 Cartesian algebraic checks, with
  the identification of the inverse by distributional harmonic uniqueness added); independent analytic referee 01:30 to 01:38: VALID,
  the first step valid with fixes (Ns < 1 gives absolute convergence
  and continuity at 0; global uniqueness by harmonic derivative estimates; no derivative bound on the vorticity
  remainder is needed for the inverse estimate), failure at integer beta in two places recorded, and a smooth field
  satisfying the vorticity equation alone with these expansions and C = 0 given (so (d) excludes nothing beyond fields
  with C != 0). Independent verification of the drafted entry 01:47 (inverse exponents, distributional uniqueness, separation of
  C.grad(r^{-s} a) from the ladder): CONFIRMED with the stated scope. Entered as 4.26(d) at 01:52, with the matching
  change of the 4.26 scope paragraph. Independent re-read of the entered text 02:03: CONFIRMED with the stated scope.
- 2026-10-21 01:48 to 02:11 (exact constants of the four beta-free states). Independent verification (written 01:48, CONFIRMED
  01:56): rational cell primitives and rational series bounds for the powers v^{3-b} give outward enclosures of C2
  for the four stored states, checked against the stored binary data; 55 manufactured controls and two tamper
  rejections pass. The closed form used is the one audited at 00:34 (fixes adopted 00:37). Section 6.1 changed at 02:11 from a conditional
  to an unconditional statement about the four stored fields.
- 2026-10-21 01:55 to 02:42 Two further methods, both failed (section 6.2): a dynamic-rescaling pilot (time stepping,
  steady Newton and homotopy), its time-stepping failure reproduced independently at 02:33, and a slow-tail defect of
  its compactified inverse found independently at 02:31 (strain 1.526 instead of 1.5 for an exactly known field);
  and an independently implemented smooth stream-function trial space with sixteen least-squares fits (02:16 to 02:41)
  and manufactured controls (02:25), all REFUTED as candidates. Entered 02:44.
- 2026-10-21 02:15 to 02:55 Retied lambda-path states and their constants (section 6.1): five states with the unknowns
  stored in the basis of their own beta evaluated independently (01:38 to 02:22), with exactly nonzero temperature
  tail coefficients making the absolute temperature residuals unbounded; the constant C2 of the four 16-mode states
  for 3 < b_rep < 4 by a formula with three subtracted terms, proved and certified in exact rational arithmetic
  independently at 02:36 and audited by an independent analytic referee (VALID WITH FIXES: smoothness of S, the radius
  beyond the last knot, the conditional form of the exclusion and the scope sentence, all adopted); the draft re-read
  independently at 02:49 (CONFIRMED with two wording changes, adopted). Axis subsystem in G (section 6.2, now 4.35):
  construction and Beta-function formula for Q_+ proved independently 02:07 to 02:18 (the Q_+ formula at 02:12;
  CONFIRMED), audited by an independent analytic referee (VALID WITH FIXES: normalization by scaling, consistency
  rather than nonexclusion, the class of weights; corrected paragraph adopted). Independent re-read 02:49 of the
  fourth referee changes: the displayed C = 0 field of 4.26(d) CONFIRMED (it satisfies (V) and fails (T)); knot
  convention of 6.1, two wordings in 6.2 and the environment of section 8 corrected. Entered 02:55.
- 2026-10-21 02:18 to 02:38 Fourth independent referee review of the full interim report (state of 02:11), concentrating
  on 4.7(xi), 4.23(c)-4.27, sections 5 and 6 and the timeline: the new theorems survive with their stated
  hypotheses; required changes adopted 02:38: the opening of 4.27(d) (positivity and parity of the leading data do not
  force alpha to vanish; the data do determine it), an explicit definition of the stored representation in 6.1 with
  the basis exponent b_rep and the constants C_rep, alpha_rep of stored fields, the explicit field behind the scope
  sentence of 4.26(d) (now displayed), the solution hypothesis in Q4, renamed letters in 4.7(xi) and 4.26(d), the
  envelope sentence and the inverse-truncation sentence of 6.1 and 6.2, rounded values marked as rounded, and the
  wording of sections 7 and 8. Shortening of sections 5 to 7 is pending.
- 2026-10-21 02:57 to 03:13 Free-beta fits in the independently implemented stream-function trial space (section 6.2):
  ten fits from five starting values of beta, all stopping at the imposed lower bound beta = 2.02 with order-one
  held-out residual ratios, with exact certificates of nonzero fractional far-field residual terms of the ten stored
  fields; all REFUTED as candidates (03:13). Entered 03:23.
- 2026-10-21 03:00 to 03:11 Independent analytic referee of 4.5, 4.10, 4.11 and 4.12(f) (with sections 2 and 3, 4.6,
  4.9 and the rest of 4.12 as premises), the first referee verdict for 4.5 and 4.10 and an additional confirmation for
  4.11 and 4.12(f) (first verdicts 2026-10-20 15:06 and 16:27): 4.5 VALID, 4.10 VALID, 4.12(f) VALID, 4.11 VALID WITH
  FIXES (all of (i) to (iii) hold; the sides xi = u, v of the rectangle contribute nothing to the boundary term with
  dTheta but in general do contribute to oint Theta dy, and the derivative of Theta_infty in remark (b) is
  distributional); both fixes adopted. Entered 03:11.
- 2026-10-21 03:07 to 03:16 Independent verification of the 24-mode state at lambda = 0.955 stored in the basis of its
  own beta (beta = 3.0082; forced maxima 0.00039/0.0014, (B2-P) maxima 0.74/0.46; exactly nonzero temperature tail
  coefficients and an exact C2 enclosure; CONFIRMED; no candidate; its rounded E_T rounded from the exact rational
  witnesses), and re-read 03:07 of the 02:55 entries: CONFIRMED, with one scope repair adopted (the
  residual expansion of section 6.1 holds in the displayed form for a forced problem only when the source is stored
  with the same basis exponent). Entered 03:16.
- 2026-10-21 03:21 Re-read by the independent verification of the entries of 03:09 to 03:16: CONFIRMED (the eight
  native pairs, the three E_T values, the C2 enclosures, the display-scope repair and the two 4.11 fixes), with two
  bookkeeping corrections and one history correction, all adopted: the regional maxima cover 60 saved states with
  distinct archives, not 35 (the smallest interval maximum is then 0.309, so the bound of section 6.1 reads 0.30); one
  forced state was fitted at three map scales, not two (third scale L = 2.5 evaluated independently 01:32: forced
  maxima 0.030/0.043, (B2-P) 0.76/0.83; REFUTED as a candidate); and the 03:00 to 03:11 review is the first referee
  verdict only for 4.5 and 4.10. Entered 03:29.
- 2026-10-21 03:32 to 04:04 Independent verification of the 24-mode step to lambda = 0.95 (03:32 to 03:39; rejected by
  the acceptance rule of the computation) and of the 32-mode state at lambda = 0.95 (04:00 to 04:04), both stored in
  the basis of their own beta (beta = 3.0114; forced maxima 0.0015/0.0043 and 0.00025/0.00086, (B2-P) maxima
  0.74/0.46; exactly nonzero temperature tail coefficients, with E_T 11.8 and 9.82 from the exact
  witnesses, and exact C2 enclosures; CONFIRMED as diagnostics, REFUTED as candidates). Entered 04:19.
- 2026-10-21 03:36 to 03:54 Fractional-tail variant of the stream-function trial space (section 6.2): twelve fits run
  by the independent verification (completed 03:39); exact rational check of the twelve stored fields (03:54, 60
  independent polynomial expansions and differentiations, 3 polynomial controls, 7 tamper tests): the third-order
  center coefficients are nonzero, so the fields are REFUTED as local solutions. Entered 04:07.
- 2026-10-21 03:37 to 04:02 Center Taylor conditions of (V), 4.28: derived by the analysis with exact self-checks in
  rational arithmetic (03:38 at beta = 4, a0 = 1: degree-two residual of the example 17/15, equal to the 4.13 value;
  corrections D_4 = 17 x y^3/810 and D_5 = 157 x^3 y^2/19440 - 17957 x y^4/5443200; residual zero through degree 6;
  03:46 the same at beta = 9); CONFIRMED by the independent verification 03:55 (own exact recursion at beta = 4, 9
  and 25/9 through degree 12 of R_Omega, D_4 and D_5 reproduced; own proof of the smoothness of xi to all orders, the
  positivity margin, the basin and the canonical inverse), with two wording requests adopted (the scope separates the
  unchanged example from the class it represents; the complements are specified); independent analytic referee 03:54:
  (a) VALID, (b) and the Scope VALID WITH FIXES, all adopted (the linear term of the example is removed before the
  formal series is built; the complements are fixed explicitly; the basin estimate, the smoothness of xi and the
  polynomial temperature bound are written out; the scope conclusion is narrowed; the exterior axis obstruction for
  the particular configurations is added, with the exact value F_e'(0) = 119/15 at beta = 4); the referee independently
  reproduced D_4 to D_8 and the zero residual through degree 6. Entered 04:02; the entered text was sent to the
  independent verification for re-reading.
- 2026-10-21 03:44 to 04:37 Realizations near the center and along the axis, 4.29: (b) to (d) obtained in an
  independent analytic research consultation (03:44 to 03:59) and checked by the analysis; (e) derived by the analysis
  (draft 04:00, revised 04:10; symbolic checks of the axis identity, of the cubic correction formula and of the axis
  recurrences); independent analytic referees: 04:11 (e) VALID WITH FIXES, 04:13 (b) to (d) VALID with a scope
  distinction (the disk and the reference g1 = g1^e cannot both be kept); all fixes adopted. Independent verification:
  04:19 (a) to (d) CONFIRMED (own recurrences of the axis jets, cutoff formula, exact base jets and derivatives of
  F_e); 04:28 (e) CONFIRMED (own proof; two independent ODE formulations agree to 3e-10 in log values; exact center
  controls at three rational (beta, a0) pairs; exact finite-regularity cutoff controls; the limits of Q/q^e quoted in
  (e) are its floating-point values); 04:33 the combined text CONFIRMED, with one request adopted (the definition of a
  configuration states the center data). Entered 04:37; the entered text was sent to the independent verification for
  re-reading.
- 2026-10-21 04:00 Re-read by the independent verification of the entries of 03:29 to 03:40: CONFIRMED, with three
  corrections, all adopted: the (B2-P) maxima of the forced state fitted at three map scales are 0.76/(0.83 to 0.84)
  (0.836 at L = 1.5); the coefficient map of the stream-function trial space can have kernels at integer beta,
  depending on the radial degree; the entry "three fit domains not done" of Table 6.1c refers to (B2-P). Entered
  04:18.
- 2026-10-21 04:24 to 05:20 Independent verification of the 32-mode state at lambda = 0.945 (04:24 to 04:33) and of
  the 32-mode step to lambda = 0.94 and the 40-mode state at lambda = 0.95 (05:15 to 05:20), all stored in the basis
  of their own beta (beta = 3.0163, 3.0239 and 3.0114; forced maxima 0.00069/0.0021, 0.0036/0.0074 and
  0.00024/0.00032, (B2-P) maxima 0.74/0.46, 0.74/0.45 and 0.74/0.46; own whole-plane inverse and Cartesian
  differences, exact C2 enclosures and exactly nonzero temperature tail coefficients; CONFIRMED as diagnostics,
  REFUTED as candidates; the convergence under angular refinement reported by the computation at lambda = 0.95 not yet
  independently confirmed at that time). Entered 05:26.
- 2026-10-21 04:27 to 05:15 The whole axis, large disks and analytic exteriors, 4.30 to 4.32. 4.30: obtained in the
  independent verification (CONFIRMED 04:42: own proof with a weighted localization on a noncompact partition of the
  axis; exact rational localization controls on 20 cells at degrees 5 to 11; six ODE cases for the disk reference, two
  formulations agreeing to 1.5e-10 in log values; two written external audits checked, one inequality of an external audit
  corrected from b' >= l to b' >= l/2) and, by a second route (symbol classes of the axis coefficients and conic
  cutoffs), in an independent analytic research consultation (04:27 to 04:42); checked by the analysis. 4.31: obtained
  in an independent analytic research consultation (04:29 to 04:39) and checked by the analysis; independent analytic
  referee 04:59: VALID, with fixes, all adopted (the comparison with 4.29(b), (c) narrowed to their exactness
  conclusions; the scaling quantifiers made explicit; the axis obstruction for the anisotropic exterior added, with
  q_L'(0) = c (3 (beta + 1) + 2 eta)/(beta (beta + 1) L^2); the dependence of all constants on R stated); CONFIRMED by
  the independent verification 05:03 (own proof; general Laplacian identity, four exact rational cases, symbolic flow
  and PDE checks, derivative, orbit, tail and inverse controls). 4.32: obtained in the independent verification
  (CONFIRMED 04:51: no-division elimination of Theta; exact [x^2 y]E_comp = 476/5 at beta = 4, a0 = 1 and a positive closed
  form for all beta > 2, a0 > 0; two written external audits checked); the closed form was reproduced by the analysis in
  exact rational arithmetic and extended to the anisotropic family (8127/160, 1746927/100000 and 408093191/28800000 at
  (beta, q0, L^2) = (4, 1, 36), (4, 1, 100) and (9, 1/2, 400)); the verification reproduced 8127/160 and the formula
  for q_L'(0) at 05:03. Independent analytic referee of 4.30 and 4.32, 05:12: 4.30 VALID (the second route VALID WITH
  FIXES: its exclusion of logarithms restricted to the leading order); 4.32(a), (b) VALID, the four exact coefficients
  of E_comp reproduced; (c) VALID; the Scope of 4.32 INVALID as written (a compactly supported odd vorticity perturbation
  can leave the relative velocity unchanged outside a compact set) and replaced; the tails of 4.29(e) and 4.30 agree
  with that of the example uniformly in theta, not with angular derivatives (adopted, also in 4.29(e)); the
  combination of 4.30 with the large disks of 4.31 VALID for the reference configuration of 4.31 (entered as 4.31(b),
  next entry). All fixes adopted. The re-read of the entered 4.29 by the independent verification (04:52: CONFIRMED)
  asked to drop the remark that the higher axis conditions need decay bounds and to cite 4.32 for the nonprofile label
  of section 6; both adopted. Entered 05:15; the entered text was sent to the independent verification for re-reading.
- 2026-10-21 05:11 to 05:20 Whole axis together with a prescribed disk, 4.31(b). Obtained in the independent
  verification (CONFIRMED 05:11, own proof: every correction of the whole-axis construction vanishes on the band |y| <
  D, so the explicit backward orbits from the prescribed disk and the exact fields on it are unchanged; an ODE lemma
  in symbol classes for all axis coefficients, with no summation of a divergent series; corrections confined to a cone
  of prescribed aperture, C^infinity angular limit and Theta <= C (1 + |X|)^{1-2/beta}; own Cartesian recurrences
  through a_10 and w_9, symbol exponent arithmetic through a_20 and w_21, and 60 rational weighted derivative
  polynomials checked at 45 digits; two written external audits checked, a third without a written audit not counted).
  Independent analytic referee 05:12: the combination VALID for the reference configuration of 4.31. The statement and
  proof outline were written by the analysis from both; the summaries in 4.13, 4.30, 4.32(c), sections 5 and 6 now
  cite 4.31(b). Entered 05:20; sent to the independent verification for re-reading.
- 2026-10-21 05:23 to 06:12 Exterior exactness, 4.34. A first external research consultation (05:23 to 05:39) gave no
  construction (a derivative loss in the transport of the velocity difference, and smoothness at one gluing radius
  unproved). A second (05:46 to 06:12) derived the construction of 4.34: a contraction of a strong weighted Hoelder ball
  in a weaker metric, and weighted energy estimates for the smooth iterates with a coupling coefficient independent of
  the derivative order, so that one gluing radius serves for all orders. Partial check by the analysis (scaling,
  residual identity, parity, inverse at 0, energy algebra, absorption, div-curl bound, recurrence).
- 2026-10-21 05:25 Re-read by the independent verification of the entered 4.30, 4.31(a), (b) and 4.32: CONFIRMED (own
  derivations, exact polynomial and conic checks; also the lower-axis asymptotics of H for Psi_L and the band
  uniqueness in 4.31(b)), except one sentence of the Scope of 4.32, REFUTED: an odd compactly supported stream
  perturbation phi leaves the relative velocity unchanged outside its support only if grad phi(0) = 0 (for phi = x chi
  with a radial cutoff chi the relative velocity changes by a nonzero constant outside the support). Corrected 05:29;
  every construction of the report has grad phi(0) = 0, so no conclusion changes.
- 2026-10-21 05:28 to 05:44 Independent adversarial analytic referee of the entered 4.31(b), against 4.30, 4.31(a) and
  the verification's proof packet: VALID WITH FIXES, statement unchanged. The proof of (b) had cited the conic
  construction of 4.30 without checking its inputs for the anisotropic reference; it now states them (symbol bounds of
  every order and the homogeneous limit of the reference, differentiated axis asymptotics, the normalization of a_2 by
  a_2(0) = a0 rather than by boundedness, a sign-sensitive first cutoff of variable width with its derivative
  identity, weighted seminorms for the higher terms, and the summability that passes the angular limit through the
  infinite sum, since symbol bounds alone do not give an angular limit). The Scope of 4.31 now says that the
  compatibility holds for each bounded set fixed in advance, that it does not classify the possible exclusion
  arguments, and that the construction supplies no fixed exterior and no uniform estimates; the limit as R -> infinity
  is sharpened to convergence in C^infinity_loc to q0 x. The referee reproduced the obstruction coefficient [x^2 y]E_comp =
  q0 (2 beta + 4) lambda2 M q_L'(0) > 0 of 4.32 (476/5 at beta = 4, a0 = 1 for the example). The corresponding wording
  in Q2(f) and 6.2 was narrowed, and a local letter of 4.31(a) was renamed (N for the radius 2D, distinct from M = 2
  beta + 1). Checked by the analysis (derivative identity of the variable-width cutoff, exponent arithmetic of the
  forcing terms, cone inclusion, the coefficient value). Entered 05:52; sent to the independent verification for
  re-reading.
- 2026-10-21 05:33 to 05:37 Independent common-grid comparison of the 24-, 32- and 40-mode states at lambda = 0.95
  (own value reader and analytic angular derivatives, 61 radii from 1e4 to 1e8, three angular grids): the refinement
  reported by the computation CONFIRMED as a finite sampled refinement at fixed forcing, with the norm stated in 6.1
  (no convergence proof, no candidate); re-read of the 6.1 additions of 05:26 and of the 4.32 Scope correction of 05:29:
  CONFIRMED. Entered 05:41.
- 2026-10-21 05:39 to 06:04 Fifth independent referee review of the full interim report (state of 05:39),
  concentrating on 4.28 to 4.32 and their summaries: no YES or NO supported; seventeen requested changes. Adopted
  06:06 to 06:12: in 4.29(c) the coefficients of the reference (with the normalization a_2(0) = a0) replace those of
  the example; the 4.29 Scope refers to 4.30 and 4.31(b) for the combinations it had listed as open and keeps the
  hypotheses of 4.29(d) (a0 > 0, Theta = a0 xi^2 on its own whole-plane backward basin, the canonical relative
  inverse) wherever 4.29(d) is summarized (4.13, Q1); the 4.30 conic variant points to the estimates written out in
  the proof of 4.31(b); mu > 0 in the scaling of 4.31(a) and distinct letters for the patch error and the local
  radius; the Scope of 4.32 restricted to stream perturbations with grad phi(0) = 0; the Q1 identities bullet states
  beta >= 2 for 4.12(g) and beta > 2 for 4.17; the description of subclass G in section 6 and 6.2 now says that all
  class A restrictions apply to G and that none excludes all profiles in G; the vorticity tail of 4.30 and 4.31 is
  written a_tail(theta), with Omega(r e(theta)), and the compatibility expression of 4.32 E_comp, to avoid clashes
  with the temperature tail A(theta) and the elliptic residual; workflow wording removed from the timeline; the
  artifact manifest and the final time accounting are marked as pending. Remaining items (numbered statements for the
  axis assertions of 6.2, traceability of the section 4 opening, shortening of repetitions) are editorial and are
  scheduled before completion.
- 2026-10-21 05:46 and 06:17 Independent verification of the horizontal primitive reformulation and of the angular
  compatibility criterion with its conditional application (now 4.33), by exact rational and symbolic controls:
  CONFIRMED (the reformulation and the homogeneous criterion at 05:46, the axis normalization hypotheses and the
  conditional application at 06:17).
- 2026-10-21 05:54 to 06:28 Independent numerical audits of the 40-mode states at lambda = 0.945 and 0.94 and of the
  32-to-40 angular comparisons at these values (6.1): CONFIRMED as measurements; both states REFUTED as profiles.
- 2026-10-21 06:01 Re-read of the revised proof of 4.31(b) by the independent verification, paragraph by paragraph
  (reference symbol bounds, coefficients and their normalization, the variable-width first cutoff, the higher
  coefficients, cone inclusion and angular limit, basin, temperature, disk and inverse): CONFIRMED.
- 2026-10-21 06:04 to 06:20 External audit of the horizontal primitive reformulation and angular compatibility
  (4.33): VALID WITH FIXES. Theta(0, .) = 0 is forced near 0, and on
  the whole axis under the stated conditions on the zeros of b, but not by the axis equation alone, so the single
  equation is a reformulation of the normalized subclass; the exterior hypotheses of the conditional application are
  not supplied by the slow-tail notation. Adopted in 4.33 at 06:26.
- 2026-10-21 06:09 Independent numerical search in the horizontal primitive representation: 18 fits (fixed beta 2.25,
  2.75 and 3.5 and free beta, three resolutions), all refuted as exact fields by a nonzero rational thermal Taylor
  coefficient of degree at most 4 and nonzero leading angular primitive moments; free beta stays at its lower bound
  2.05; no candidate.
- 2026-10-21 06:14 to 06:25 External adversarial audit of the 4.34 proof: VALID WITH FIXES (two missing signs in the
  reference expansions; the gluing radius beyond the analytic-exterior radius of the reference, so that 4.32 applies;
  an existential tail constant; the Lipschitz hypothesis kept in the order-zero transport estimate).
- 2026-10-21 06:14 to 06:28 Independent verification of 4.34 by its own standalone proof and exact algebra controls:
  CONFIRMED, with the same corrections and one gluing radius for all derivative orders; a compactly forced
  configuration, not a profile (4.32). The same re-read found one leftover notation in 4.31(b) (A(0) for a_tail(0)),
  corrected. 4.34 entered at 06:32.
- 2026-10-21 06:17 Re-read of the changes of 06:06 to 06:10 by the independent verification (4.29(c) and Scope, the
  4.30 pointer, 4.31(a) letters and scaling, 4.32 reference and Scope, the Q1 identities bullet, the subclass G
  sentences): CONFIRMED.
- 2026-10-21 06:45 Re-read of the entered 4.33 and 4.34, the sentences on them in Q1, Q2(f), 6.2 and 6.3, the 6.1
  rows at lambda = 0.945 and 0.94 and the timeline windows by the independent verification: CONFIRMED, with one scope
  clarification in 4.31 (exactness on a disk and on an exterior domain together is consistent with the conditions
  listed there other than whole-axis flatness, which 4.34 does not assert), adopted at 06:51.
- 2026-10-21 06:55 Re-read of 4.35 (a) to (d), the first bullet of 6.3 and the 4.31 Scope clarification by the
  independent verification, with the axis uniqueness, the selection of the bounded solution q, the decomposition into
  completely monotone terms, the scaling, the properness and both endpoints of the weighted integrals checked
  independently: CONFIRMED. Summary of findings: CORRECTIONS REQUIRED (no distance to the solution set is established;
  the continuation states are approximate solutions of forced problems; the growth of Theta is that of its supremum on
  circles; the open core includes vorticity of either sign; the nondegeneracy and nearest-zero hypotheses of the axis
  integrality conditions are to be stated), all adopted at 07:01; the numerical ranges of the Summary CONFIRMED
  against the archived independent audits.
- 2026-10-21 06:59 Independent physical audit of the three fixed-beta fits (beta = 2.25, 2.75, 3.5) of the second
  search in the horizontal primitive representation (run started 06:33; center data, leading tail identities and the
  Taylor conditions of (T) through degree 4 imposed exactly), with own seven-point differences and a separately
  implemented full-plane inverse agreeing with the stream velocity to 1.2e-10: large temperature residuals CONFIRMED
  (maximal pointwise ratios 0.50, 0.61, 0.89 at three common points), stable under two step sizes; no candidate. The
  same three fields have a nonzero horizontal offset (4.33(e), by exact rational arithmetic) and a nonzero Taylor
  coefficient of E_comp of degree 5 (verification 06:45 and 07:03); the search is still running.
- 2026-10-21 06:26 to 07:14 Separate research consultation on removing the compact residual of 4.34 (asked 06:26,
  answered 06:49, read 07:14): no obstruction identity and no cokernel element found; the linearization of the coupled
  problem and its formal adjoint were written out, the moment of R_Omega against the strain kernel x y/r^4 was shown
  (by a compact area-preserving conjugacy that preserves (T), the center data and all exterior fields) not to be
  determined by the center and tail data, and surjectivity of the coupled operator, a tame inverse and global
  deformation estimates are left open. Not entered as a result; the conjugacy computation is requested from the
  verification.
- 2026-10-21 06:46 to 07:16 Separate audit of the numbered result 4.35 (asked 06:46, answered 06:56, read 07:14):
  (a), (b), (d) and the Scope VALID WITH FIXES, (c) VALID. Fixes (normalization D(xi, eta)(0) = I of the coordinates
  of 4.18(b), the precise converse in (a), the small-t asymptotics and the kernel bounds of (b), the threshold A_* and
  the gradient bound before the Liouville step, surjectivity of the coordinates and the radial rate in (d), three
  Scope rewordings) adopted 07:16.
- 2026-10-21 06:45 to 07:17 Verification packets on compatibility, each CONFIRMED: 06:45 horizontal offsets vanish for
  a profile with Theta(0, .) = 0 (the three stored final fields of the second search in the horizontal primitive
  representation have offsets H(1) = -6.71230, -0.322460, -12.1595 at beta = 2.25, 2.75, 3.5); 06:54 the identity
  E_comp = L_1 f + M t for any smooth temperature, with a compact lower bound for the residual of 4.34 at a fixed
  reference; 07:03 the first jet of E_comp for nonflat J and beta > 2 and the analytic converse (the three stored
  final fields have nonzero E_comp at degree 5); 07:17 smooth local sufficiency when Psi_xxx(0) != 0. Lead checks
  07:11 (exact symbolic check of the identity and of the leading jet) and 07:23 (the counterexample with J = 0).
- 2026-10-21 07:13 to 07:25 Separate audits of the drafts of 4.32(d), 4.33(e) and a sentence for the Scope of 4.34
  (asked 07:13:56, answered 07:20): VALID WITH FIXES for each part (flat cases separated and the normalization wording
  in 4.32(d); beta > 2 and a leading part smooth off 0 in 4.33(e); matching of the relative velocity in the 4.34
  sentence); and of the smooth local statement 4.32(d)(i) (asked 07:18:59, answered 07:22): VALID, with Psi_xxx(0) != 0
  not implied by the center data (counterexample Psi = c x y - (q0/2) x y^2). Fixes adopted; entered 07:25 (4.30 to
  4.35 regenerated, diff confined to 4.32, 4.33 and the Scope of 4.34); references in the Summary, Q1, 6.3 and Table
  8.1 updated 07:27.
- 2026-10-21 07:28 to 07:58 Whole-report review (separate referee, asked 07:28:59, answered 07:46): the checks of
  4.32(d), 4.33 and 4.35 passed; ten items. Adopted 07:52 to 07:58: Table 8.2 extended to every exact certificate
  cited in 6.1 and 6.2 (identifiers R added for independent runs of the verification); the two stale cross-references
  (6.1 to the velocity interpolation rule of 6.2; the Scope of 4.33 to the eighteen horizontal-primitive fits)
  corrected; the leading-balance wording in 6.2 (Decay and integrability) and in the first item of 6.3 made precise; a
  compact state table (Table 6.1e) added; the proof outline of 4.34 expanded (weighted Hoelder norms with 0 < alpha <
  1, the transport problem with trace on |z| = 1, completeness of the strong ball in the weak metric, the weighted
  energies and the coefficient-one weighted div-curl estimate, subsequential weak limits identified with derivatives
  of the fixed point, the angular-limit equation for r^s Omega; notation clashes removed: R_ref, Res_*, N(theta), M_1,
  M_2, Omega_c). Separate audit of the revised outline asked 07:57. Item 7 (headline) deferred to completion; item 9
  (software names) not adopted, because the versions belong to the reproduction record.
- 2026-10-21 07:36 to 07:46 Compact conjugacy in the polynomial disk of 4.34 (verification packet, CONFIRMED 07:36):
  conjugation by the area-preserving flow of grad^perp(eps eta), eta odd and supported in two mirror disks, preserves
  (T), the parity, the center data, the canonical inverse, positivity, the basin and all exterior fields, and the
  moment int p0 R_Omega (p0 = x y/r^4) has first variation int eta A p0 with A p0(x, 0) = -3 q0 (17 beta + 28)/(2 x^3);
  vector-adjoint derivation, 8 exact controls, 9 quadratures (relative agreement 1.05e-13), a first expanded-bump run
  lost to cancellation and retained. Separate audit (asked 07:37:52, answered 07:43): VALID WITH FIXES (nonzero
  variation for a suitable generator; restriction to configurations with a nonzero residual; the new residual is
  supported in the old support and the disks). Entered in 6.3 at 07:45. Verification read 07:38 of the 07:25 and
  07:27 changes (4.32(d), 4.33(e), the 4.34 Scope sentence, 4.35, Summary, Q1, 6.3, Table 8.1): CONFIRMED, with
  beta > 2 to be stated in the specification for the global analytic converse; adopted 07:46.
- 2026-10-21 07:47 to 07:58 State table of section 6.1 (Table 6.1e): 57 stored states with independent residual
  evaluations, values taken from the evaluation packets; prose of 6.1 corrected against it at 07:56 (largest inverse
  discrepancy 2.2e-10 at the points of Table 6.1a and 2.9e-10 on the regional raw arrays; 1.31e-4; forced residuals;
  the range 0.38 to 0.97; the count of saved states, now 69; the regional lower bound 0.29). The 32-mode state at beta
  = 3.0315, lambda = 0.936736 (verification 07:49: REFUTED as an unforced profile; forced ratios 0.00957, 0.0181;
  exact thermal-tail witnesses; C2 in [-4537.558, -4537.557]) entered 07:58.
- 2026-10-21 07:52 to 07:58 Compact-conjugacy sentence of 6.3 and SPEC v27: verification 07:52: CONFIRMED, with one
  definition clarification (W_eps = (Phi_eps)_* W, Theta_eps = Theta o Phi_eps^{-1}, Omega_eps = -curl(W_eps - beta
  X); the vorticity is recomputed from the new drift), adopted 07:58.
- 2026-10-21 07:57 to 08:04 Revised proof outline of 4.34 (after the whole-report review): separate audit 07:57 to
  08:02: VALID WITH FIXES. Weighted norms, transport with inflow trace on |z| = 1, completeness of the strong ball in
  the weak metric, the coercivity coefficient (beta eps = 1/4), the order-independent condition 32 delta^2 M_2 <= 1,
  the coefficient-one div-curl estimate, identification of limits and the angular limit: valid. Fixes adopted 08:04:
  seminorm domain B(z, |z|/8) intersected with {|y| >= 1} and the zero-order norm defined; potential operator renamed
  Q and P_inf = grad theta_e; auxiliary vorticity source versus actual vorticity change R^{-2s}(e + b[e]); uniform
  Lipschitz bound of the angular flow from int sup |d_theta b| d tau < infinity; Hilbert-Schmidt tensor norms and
  M_1, M_2 uniform in n and R; weak-limit identification stated; Scope: R1 = 8R and "not identically zero".
  Verification 08:07: the expanded outline CONFIRMED against the complete proof; the referee6 revisions (items 1 to 6
  of the 08:00 request) CONFIRMED, with two repairs adopted 08:09: the Table 6.1e caption states the exception for
  blam1_lambda0p97 (intended fixed source), and the whole-report review list includes the sixth review.
- 2026-10-21 08:00 to 08:21 Invariant x-moment of a compact residual (verification packet, CONFIRMED 08:00): for two
  smooth configurations with exact (T) whose relative streams and temperatures differ by compactly supported chi and
  tau, int delta R_Omega = int y delta R_Omega = 0, int x delta R_Omega = int tau and int delta R_Theta = -(3 beta -
  2) int tau, so int x R_Omega is unchanged by such modifications, the compact conjugacies included; 11 exact and 15
  quadrature controls (largest error 7.41e-14). Separate audit (asked 08:07:52, answered 08:12): VALID WITH FIXES (the
  drift and the temperature, not the physical velocity, fixed outside a compact set, since a compact physical change
  of U(0) changes the relative fields everywhere; a necessary condition only; the moment equals a boundary integral of
  the exterior fields, whose value is not established). Entered in 6.3 at 08:16. Verification 08:21 of the entered
  sentences: CONFIRMED (a relative drift fixed outside a compact set supplies a compact chi; the four identities and
  the necessary-only scope correct).
- 2026-10-21 08:13 to 08:40 Large-R x-moment of the residual of 4.34. Separate audit (asked 08:13:25, answered 08:23):
  the scaled residual identity, the moment cancellation of the compact compensator and the homogeneous cosine moment
  VALID; the asymptotic VALID WITH FIXES (0 <= rho <= 1 explicit, so that C_rho > 0; an L^1(B_8) bound O(delta^2) of
  the temperature difference; then int x R_Omega dX = R^{3-2s}[C_rho m1 + O(R^{-s})]). A wider claim that both signs
  of m1 are realizable uses compact interpolation without positivity and is not entered. Verification packet 08:36:
  the boundary formula for arbitrary fields, the scaled residual, the compensator moment and the asymptotic CONFIRMED
  for a fixed reference with 0 <= rho <= 1 (the transported reference temperature r^m A + O(r^{m-s}); the C^1 and
  L^1(B_8) temperature bounds from the estimates of 4.34; 29 controls). The value of m1 for an actual reference is not
  computed. Entered in 6.3 at 08:40.
- 2026-10-21 06:31 to 08:52 Second search in the horizontal primitive representation, completed (run by the
  verification 06:31:00 to 08:48:21, 8241 s; final summary 08:50): nine fixed-beta fits (2.25, 2.75, 3.5) and nine
  free-beta fits from the same starting values, three levels n = 4, 5, 6 with the fit radius 10, 30, 100 increased
  together (not an isolated convergence study), every stage at the cap of 90 evaluations. Exact rational
  reconstruction: the center equations, both imposed leading angular moments and the Taylor coefficients of the
  residual of (T) through degree 4 hold exactly in all eighteen; every field has a nonzero degree-5 coefficient; all
  eighteen held-out maximal ratios for (T) equal 1; the six final fields have exactly certified nonzero offsets H(1) =
  -6.712, -0.322, -12.16 (fixed beta 2.25, 2.75, 3.5) and -1.357, -1.075, 0.1798 (free, final beta 2.1459, 2.1338,
  2.1241), with zero logarithmic coefficient; a separately implemented whole-plane inverse and Cartesian differences
  confirm substantial sampled residuals of (T). Verdict REFUTED for these fields; no statement about nearby streams.
  Entered at the end of 6.2 at 08:52 (with the 4.33 Scope reference to the first search made specific and the
  corresponding row of Table 8.1 extended).
- 2026-10-21 08:27 to 09:05 4.36 Renormalized impulse under a far-field expansion. Research consultation (asked
  08:27:19, answered 08:37): the boundary formula for int x R_Omega correct with its signs; the critical set Z_crit =
  {M/N > 2 : gcd(M, N) = 1, N <= 3} of exponent collisions; for beta not in Z_crit the formula 2 pi (1 - 3 beta) D and
  D = 0 for profiles; positivity alone does not fix the sign of D (items VALID or VALID WITH FIXES). Draft written
  08:38. Separate audit of the draft (asked 08:41:31, answered 08:50): VALID WITH FIXES (integer indices and j >= 0;
  harmonic exceptional terms without logarithms, equal (e, j) combined; the coefficient [rho^0 (log rho)^0] of the
  substituted boundary integral valid for every beta > 2, the reduction to D only outside Z_crit; logarithm wording;
  the harmonic pair (1, -1) of power -1; (a) restricted to beta not in Z_crit; (b) reworded, with the range of D and
  the violation of (V) far out; global (T) essential, with a counterexample; x R_Omega in L^1 suffices), all adopted
  08:53. Verification 09:01: the revised version CONFIRMED by an independent proof and 184 exact controls, including
  the example of (b) (one fix: j a nonnegative integer, adopted). Entered as 4.36 at 09:02 (letters local to 4.36
  named 09:03); cross-references in the Summary, Q1 and 6.3 at 09:04.
- 2026-10-21 08:54 to 09:17 Beta-parameterized 32-mode run (beta fixed per stage, lambda solved): the states at beta =
  3.04 and 3.05 (lambda = 0.934345, 0.932636; verification 08:54) and 3.062 (lambda = 0.931684; verification 09:14),
  each evaluated on 15456 points to r = 1e8 by the independent inverse and Cartesian differences: REFUTED as unforced
  profiles (forced ratios 0.0204/0.0366, 0.0397/0.0674, 0.0678/0.109; (B2-P) ratios 0.734/0.447, 0.732/0.449,
  0.730/0.744; exact positive-power thermal-tail witnesses; C2 in [-4664.378, -4664.377], [-4821.233, -4821.232],
  [-4979.108, -4979.107]). Entered in Table 6.1e, the C2 list of 6.1, a 6.1 paragraph on the run, a Summary sentence
  and the reproduction row of Table 8.2, 09:15 to 09:17. The entered 4.36 and its cross-references were re-read by
  the verification at 09:14: CONFIRMED.
- 2026-10-21 09:05 to 09:57 4.37 (finite exterior expansions): the verification's standalone proof (09:05) that the
  exact exterior equations and full symbol bounds give finite power-logarithmic expansions to every depth mu in (3, 4)
  outside E, with its 82 controls (Poisson inversions of power and logarithmic sources at ordinary and resonant
  weights, scalar Euler inversions, exponent schedules, radial source controls), CONFIRMED 09:23 together with the
  class A application by rescaling the annular regularity of 4.16; continuation of the induction to 4 - s < mu < 4
  written in the energy packet (09:47); the draft of the analysis (09:40) checked by the verification 09:47: CONFIRMED
  with one normalization fix (the Poisson remainder stream odd in x, since a constant violates the decaying remainder
  for mu > 2), adopted 09:50; separate audit of the draft asked 09:40, answered 09:52: VALID WITH FIXES (the expansion
  and remainder hypotheses of 4.36 are supplied, but its identity also needs global (T) and beta not in Z_crit, with
  the example of a compactly supported temperature and Psi = 0; the unique odd smooth remainder stream; an explicit
  weight schedule with increments in (s/3, 2s/3) avoiding E and {1, 3} and a last step to the prescribed depth;
  coefficient uniqueness after combining equal powers and the log-free convention at resonances; 3 in E exactly for
  beta in Z_crit), all adopted 09:53; entered 09:55, with the Scope of 4.36 (the expansion hypothesis now proved for
  class A) and the cross-references in the Summary, Q1, 6.3 (the configurations of 4.34 need in addition derivative
  bounds of Theta) and section 8 updated 09:55 to 09:57.
- 2026-10-21 09:21 to 09:55 4.38 (renormalized energy): research consultation asked 09:21, answered 09:31: identity
  VALID; power count VALID WITH FIXES (the cubic flux Psi Omega V.n had been omitted from the request); Z_E VALID;
  reduction to -2 pi beta C D VALID WITH FIXES; sign question VALID WITH FIXES (both signs only under Theta >= 0, not
  for strictly positive temperature); draft of the analysis written 09:35 with the cubic flux; separate audit asked
  09:36, answered 09:45: VALID WITH FIXES (the sign statement of (d) by explicit examples, the Scope sentence on the
  scaling exponent and on observer and cutoff conventions, the comparison with 4.36 limited to what was checked),
  adopted 09:47 together with the remainder depth 4 - s < mu < 4 and a compactly supported vorticity residual;
  verification 09:47: CONFIRMED by its own proof and 181 exact controls (polynomial disk identities at three values of
  beta, a nonzero cubic flux 4 pi R^6, the harmonic C D coefficient, 112 rational collision checks, the radial
  finite-part algebra, the negative quadratic bump coefficient, D = 0 concentration bounds and the exterior residual),
  including fields with D = 0 of either energy sign that violate (V) on every exterior annulus; entered 09:55.
- 2026-10-21 09:24 to 09:37 Regional residual reduction extended to 72 saved states with distinct coefficient
  archives (verification 09:24, a reduction of the independent evaluator's stored summaries, no new solve): the
  entered 60-row Table 6.1e and the new rows at beta = 3.04, 3.05, 3.062 CONFIRMED; the overall (B2-P) range 0.73
  to 1 CONFIRMED for 72 states (minimum 0.73199 at beta = 3.05); the lower bound 0.29 on the four outer intervals
  REFUTED for 72 states (0.288964 at beta = 3.04, interval 300 to 1e8) and replaced by 0.2889; the beta-run paragraph
  CONFIRMED, with the remark that the growing forced residuals do not by themselves separate insufficient resolution
  from insufficient nonlinear convergence; wording of 6.1 and the Summary changed accordingly at 09:37.
- 2026-10-21 09:38 to 09:55 First state of a second forced path (24 modes, lambda = 0.99, beta = 3.0866746, a0 = 1,
  b_rep = beta; seed the eps = 0 state of an external Gaussian dipole at y0 = 2.5, whose fixed source carries most of
  the center strain), evaluated by the independent inverse and Cartesian differences (verification 09:38): REFUTED as
  an unforced profile (forced ratios 2.53e-4/2.59e-4, (B2-P) ratios 0.745/0.420, absolute (B2-P) maxima 18.5/2.68,
  exact positive-power thermal-tail witnesses, C2 in [-425.908, -425.907]); the regional reduction extended to 73
  states (verification 09:42): the bound 0.2889 REFUTED for 73 states and replaced by 0.0987 (the outer interval of
  the new state, 0.098754), 0.2889 CONFIRMED for the other 72, overall range 0.73 to 1 CONFIRMED; entered in Table
  6.1e (61 rows), a 6.1 paragraph, the regional sentence, Table 6.1c, the Summary and the reproduction row of Table
  8.2, 09:48 to 09:55.
- 2026-10-21 10:01 to 10:04 Verification re-read of the text entered 09:55 (4.37, 4.38, the Scope of 4.36, the Summary and Q1 cross-references, 6.3, the L2 paragraph, Table 6.1e row and caption, the 73-state regional sentence, Table 6.1c, Tables 8.1 and 8.2): CONFIRMED WITH WORDING FIXES: (1) in 4.37 distinguish the identity of 4.36 (requires (T) on R^2 and x R_Omega in L^1, automatic under (V) outside a ball) from its reduction to 2 pi (1 - 3 beta) D (requires beta not in Z_crit); (2) add L2 to the sampling list of Table 6.1e; both adopted 10:03 to 10:04 (the Table 8.1 row of 4.37 adjusted accordingly). The verification also noted that 4.34(iii) may state |D^k Theta| <= C_k (1 + |X|)^{m-k} for every k (proved in the gluing packet), which would remove the added hypothesis in 6.3; sent to a separate audit 10:07 together with the zero-moment glued configurations and the variation of the finite-part energy.
- 2026-10-21 10:07 to 10:20 Section 6.3 and 4.34(iii). Verification 09:30 (147/148: the glued configurations with vorticity of both signs and int R_Omega = int y R_Omega = int x R_Omega = 0, nonprofiles) and 09:59 (152: E_fp'(0) = -int eta [R_Omega + (4 beta - 1) Omega + 2 Theta_x], equal to -4 a0 (5 - 1/beta) int x eta on the polynomial patch; 18 exact and 9 finite-twist controls): CONFIRMED. Verification 10:01: the bounds |D^k Theta| <= C_k (1 + |X|)^{m-k} for every k are proved in the gluing packet. Drafts A1 to A3 (4.34(iii) and the proof sentence), B (the zero-moment configurations) and C (the finite part) sent to a separate audit 10:07 (answered 10:15): A1, A2, A3, B VALID; C VALID WITH FIXES (the comparison with 4.38(c) only for beta not in Z_E; eta supported in two mirror disks; the list of retained properties), all adopted. Verification of the same drafts 10:11: CONFIRMED (k = 0 from the strong-ball and transport bound, k >= 1 from the derivative bounds of P_inf after scaling; no gluing radius depending on k), with the restriction "for beta not in Z_E" made explicit in C. Entered 10:17 to 10:20: 4.34(iii) with the temperature derivative bounds and the proof sentence, the end of the 6.3 bullet (the additional temperature hypothesis removed; the zero-moment configurations; the non-invariance of the finite part), the Table 8.1 row of 4.34.
- 2026-10-21 10:01 to 10:24 Whole-report review (separate referee, asked 10:01:10, answered 10:16:35), eight items. 4.37 and 4.38 survive (signs of (4 beta - 2) f.p. E = -2 pi beta C D - int Psi R_Omega checked); no YES or NO supported. Adopted 10:17 to 10:24: (1) the identity of 4.36 separated from its reduction (already adopted 10:04); (2) 4.38(c): "If beta is not in Z_E, then beta is not in Z_crit, so D = 0 by 4.37(a)"; (3) the L2 paragraph: "The larger of its (B2-P) maxima of R_F/N_F and R_G/N_G decreases with the radius", compared with the other 72 states of the regional comparison, and the failed L2 state marked as not among the 73; (4) "Table 8.3" corrected to "Table 8.2" in section 7; (5) three line-initial list markers in 4.9 and section 4 removed; (6) the Checks of 4.38 reworded without attribution; (7) "most advanced" removed from the Table 6.1a caption and section 7. Not adopted: moving the software versions out of section 8 (the problem statement requires them in the report). Item 8 (end time, elapsed time, manifest and registry, headline) deferred to the end of the run.
- 2026-10-21 10:11 to 10:25 Saved failed stage of the second path at lambda = 0.98 (verification 10:21, audit launched 10:11:56): beta = 3.04154706006714, 24 modes, flags converged = 0 and continuation_accepted = 0; mixed center strain 2.491833857825281 against the target 2.520773530033570 (mismatch -0.02894), the moment inverse and a separate Cartesian Duffy inverse agreeing to 2.45e-8; forced ratios 0.0270342/0.00942513, (B2-P) ratios 0.751733/0.422583, absolute (B2-P) maxima 14.64/2.719 (forced 0.782/0.0499); exact distinct thermal powers, so both absolute temperature residuals are unbounded; C2 in [-228.011, -228.010]. CONFIRMED failure of the center-strain condition; REFUTED as an unforced profile. Only one of the seven reported inner states of that stage was available for the audit; a root in beta between the samples, a fold, and the continuation of the component to lambda = 0 are not decided. Entered 10:24 to 10:25 in the L2 paragraph of 6.1, Table 6.1e (62 rows), the Summary and the reproduction row of Table 8.2 (E354).
- 2026-10-21 10:34 Verification re-read of the text entered 10:17 to 10:26 (4.34(iii) with the temperature derivative bounds, the end of the 6.3 bullet with the zero-moment configurations and the variation of the finite part, 4.38(c) with the restriction to beta not in Z_E, the L2 paragraph of 6.1, the Table 6.1e row of the failed L2 state and the 62-row caption, the 73-state regional sentence, the Summary clause, the timeline entries and E354 in Table 8.2), and of the twist draft sent to a separate audit at 10:31: CONFIRMED (the twist orientation correct; every finite real parameter retains the listed properties, with constants of the derivative bounds depending on the parameter).
- 2026-10-21 10:13 to 10:48 Section 6.3: every real value of the finite part. Verification 154 (proof written 10:13:38, 9 exact and 9 numerical manufactured controls with 72 finite twists passed 10:17, CONFIRMED 10:23:59): two mirror twists of disks inside the polynomial core, exact for every real eps, with E_fp(eps) = a eps^2 + O(1 + |eps|), a = int |B|^2 >= 2 pi beta^2 int kappa'^2 r^5 dr > 0, potential change bounded uniformly in eps, affine residual moments and exterior unchanged; a sign-changing radial profile can make the first variation vanish. Verification 155 (proof written 10:26:25; first controls 10:32 FAILED: 9 exact identities passed, but the 96-node radial quadrature on [1, 2] gave integration-by-parts discrepancies 1.37e-4 to 1.70e-4 above tolerance; quadrature refined to the exact support [1.1, 1.9] with 48/96/192 nodes, controls PASS 10:33 (discrepancy <= 8.65e-14); CONFIRMED 10:38): far-annulus conjugacies by the flow of grad^perp(R^{2-s} h(X/R)), h = chi Omega_inf, change the finite part by R^{4-2s}(eps A + eps^2 B_2/2 + o(1)) with A = -(4 beta - 1) int chi Omega_inf^2 < 0, so E_fp -> -infinity; with the twists and the intermediate value theorem every real value, including 0, is attained, with D = 0 outside Z_crit and all affine residual moments 0, on nonprofiles. The external written reviews requested by the verification for 155 returned no audit text and are not counted. Separate audits: the twist draft (asked 10:31:23, answered 10:38): VALID, no replacement text; the combined draft (asked 10:35:48, answered 10:44): VALID (the lower bound a(theta) >= c cos theta correct, a not identically zero sufficient; constants of 4.34(iii) depend on the deformation). The draft (D) of 10:31 ("no negative value and no zero") was superseded by the combined text before entry. The verification read the complete combined text against its proofs 154 and 155 (10:47:09): CONFIRMED, no change (each target value uses a fixed finite annulus before the twist family, so no joint uniformity is needed). Entered 10:46 to 10:48: the last two sentences of the 6.3 bullet replaced, one clause in the Summary (consistency of partial conditions), one sentence in the Scope of 4.38, and P154, P155, E363, A97, A98 in the Table 8.1 row of 4.34 (E368 added 10:50).
- 2026-10-21 10:31 to 10:56 Numerics: the 40-mode checkpoint of the fixed-beta run at beta = 3.0315 (solver stage done 10:31; lambda 0.936737 against 0.936736 with 32 modes). Independent evaluation 10:34 to 10:39 (own evaluator, full-plane radial inverse, seven-point differences with two steps on 15456 points to r = 1e8; four pipeline steps exit 0 in 77.4 s): forced F/G ratios 0.00240/0.00559 against 0.00957/0.0181 for the 32-mode state; (B2-P) ratios 0.736/0.449 at both resolutions; absolute maxima 7.96/0.00888 (forced) and 192.9/11.23 ((B2-P)); exact thermal tail coefficients 0.0104 and 0.00693 at positive powers, so the full-plane absolute thermal residual is infinite for both problems; C2 in [-4541.890, -4541.889]; center strain error 3.5e-7; lambda differs by 6.0e-8 between the two resolutions; initial and stopping histories differ, so a finite pair comparison only, no limit, fold or emptiness claim; the 73-state regional aggregate unchanged. REFUTED as a profile. Entered 10:55 to 10:56: one 6.1 sentence, the Table 6.1e row (63 states), the C2 list, one Summary clause, the Table 8.2 reproduction row (E365).
- 2026-10-21 11:05 Verification re-read of the 6.3 text entered 10:46 to 10:48 (every real finite part) and of the 40-mode entries of 10:55 to 10:56 (6.1 sentence, Table 6.1e row and the 63-row caption, the C2 list, the Summary clause, Table 8.2): CONFIRMED; the accepted continuation flag of the 40-mode stage is stored as continuation_accepted = 1 (acceptance effectively disabled, accept_factor = 1e9); no convergence or profile acceptance follows.
- 2026-10-21 10:41 to 11:06 Section 6.3, beta = 2, local realization. Verification 156 (CONFIRMED 10:49:37; 17 exact and 22 flow controls; two requests to a separate model returned no written audit): base Psi0 = x p0(y) chi(I), I = x g0(y), Theta0 = F(I), zero set of W a segment of the x-axis; the compact Hamiltonian shear (x, y) -> (x, y + F(x)/4) near the segment gives Psi = 2xy - a0 x^3/3, Theta = a0 x^2 on a prescribed disk, (T) on R^2, canonical inverse with U(0) = 0 and U = O(1/r), (V) on a neighbourhood of the open zero arc, every residual jet zero along the arc, Omega and Theta - L flat at the endpoints; exterior residual R_Omega = x[12 m2/y^3 + 16 m2^2/y^5 - 2 a0 m1^2/y^2] (nonprofile, noncompact residual). Lead claim (E): for x > A, W = (2x(1 - chi), 2(y - L/4)(1 + a_chi)), Omega = -2(y - L/4) a_chi'(x), Theta = L, a_chi' < 0 near A, R_Omega = -2Y[v a'' + (3 + 2a) a']; if (V) held on the invariant set then Omega(phi_{-u} X) = e^u Omega(X) would contradict the bounded backward limit. Verification 158 (written 11:01:48, own proof, 12 exact checks passed 11:02:40, published 11:05): claim (E), the arc frame DW = (4n + ell tau) tensor n, endpoint matrix 4 n tensor n, the ray limit -2 a0 m1^2 kappa sqrt(1 + kappa^2) < 0. Separate audit (asked 10:52:46, answered 11:02): VALID WITH FIXES, the replacement text for the 6.3 and Summary insertions adopted. Verification of the draft 11:05:08 (E379): CONFIRMED with one wording precision ('a nonempty open invariant set O of orbits with backward limit at an endpoint', adopted); the strong unstable curve of the construction is straight, so 4.7(vi) is not met (sentence added). Entered 11:06: end of the 6.3 bullet, the Summary open core, the Table 8.1 row of 4.7(iii)-(iv).
- 2026-10-21 11:11:44 Verification re-read of the 156/158 text entered 11:06 (6.3, Summary open core, Table 8.1, timeline): CONFIRMED; the strong unstable curves are the vertical segments x = +-A near (+-A, M/4), where W = (0, 4(y - M/4)); timing precision for 158 adopted (12 controls at 11:02:40, published 11:05).
- 2026-10-21 11:02 to 11:18 Numerics: the 40-mode stage of the fixed-beta run at beta = 3.04 (stored 11:02:35; lambda 0.9343447896, K40 - K32 difference 2.27e-8). Independent evaluation 11:05 to 11:09 (own evaluator, adaptive whole-plane inverse, seven-point Cartesian differences with two steps on 15456 points to r = 1e8; four steps exit 0 in 78.9 s): forced F/G ratios 0.00633/0.0154 against 0.0204/0.0366 for the 32-mode state; (B2-P) ratios 0.734/0.447 at both resolutions; absolute maxima 15.0/0.0157 (forced) and 216.9/11.11 ((B2-P)); exact thermal tail coefficients at positive powers 0.0132 and 0.00877, so the full-plane absolute thermal residual is infinite for both problems; C2 in [-4681.595, -4681.594]; center strain error 9.9e-7; stored flags converged = 1, continuation_accepted = 1 (acceptance effectively disabled). REFUTED as a profile; finite pair comparison only. Entered 11:18: the 6.1 passage extended to beta = 3.04, the Table 6.1e row (64 states), the C2 list, the Summary sentence, the Table 8.2 reproduction row (E377).
- 2026-10-21 11:01:24 to 11:18 Targeted review (separate referee, answered 11:15:44) of the text entered since 10:01 (4.34(iii), the 6.3 energy part, Summary, Scope of 4.38, 6.1 L2 and K40, Tables 6.1e, 8.1, 8.2, section 7): no incorrect exponent, coefficient or exceptional-set restriction; the arbitrary-energy configurations are nonprofiles. Adopted 11:18: (1) the exact zero x-moment in 6.3 derived explicitly (continuous reference family with common exterior stream and uniform symbol bounds, continuity of the glued fixed point at fixed radius by the uniform contraction, opposite signs of the leading moment coefficient at the two ends, intermediate value theorem); (2) the Summary numerics sentence with the qualifications of 6.1 (different initial and stopping histories, comparisons at two values of beta, the continuation log reports seven failed states, the saved state fails the center-strain condition on independent evaluation); (3) the timeline ranges 09:30 to 10:34 and 10:11 to 10:34 (likewise 10:13 to 11:05, 10:31 to 11:05, 10:41 to 11:11); (4) c_tail, h_ann, h_ann,R and a locality sentence in the far-annulus construction; (6) the 48-hour requirement worded as in the problem. Not adopted: (5) removal of the software versions from section 8 (machine and software versions are required).
- Grouped recap. Independent numerical audits (separate evaluator, no solver code imported): 13:46 the 42 rational-fit trials
  of one method REFUTED as candidates; 14:11 an intermediate state of the numerical solver REFUTED as a smooth candidate
  (non-smooth center terms), and the compact-cutoff polynomial trap CONFIRMED as a finite-box artifact; 15:13 a defect
  of the solver's velocity interpolation CONFIRMED (repaired 16:05, revised rule still open); 15:43 the eps = 0
  starting states evaluated for their forced transport; 16:49 the three eps = 0.34 states REFUTED as
  candidates (Table 6.1a); 17:12 audit of section 6.1: the eps = 0 evaluation of 15:43 had used the external forcing
  velocity, the true (B2-P) residuals of those states were computed (Table 6.1b), two center labels were corrected and
  an unsupported equation count was withdrawn; 17:15 interpolation defects of the saved sources (velocity jumps across
  cells and a spurious affine far-field tail) CONFIRMED as stable numerical defects, causal role in the stalls open.
  18:09 grouped normalizers of Table 6.1a recomputed (row 2 R_G/N_G 0.743); 18:07 (reported 18:12) self-source
  check of the independent whole-plane inverse on the two eps = 0 states of Table 6.1b (sampled -curl V - Omega about
  2e-11, center strain about 1e-11 or better), empirical values, no change to the residuals; 18:47 this check was
  found attributed to Table 6.1a in an earlier version of this report, and the attribution was corrected. 20:07, 20:49,
  21:14 and 21:29 independent evaluation of the forced continuation states at fixed beta (two to three resolutions on
  both sides of the sampled maximum of eps, two map scales): forced residuals 1e-3 to 7e-3, (B2-P) residuals 0.76 to 0.95,
  REFUTED as candidates, turning of the fitted states CONFIRMED as an empirical property, continuum branch OPEN; 21:29
  the first beta-free state evaluated (forced residuals 0.15/0.12, not a converged root); 21:50 the third amplitude at
  the highest resolution, three states at beta = 3.5 and one at beta = 2.25 evaluated (the last, flagged converged by
  the solver, has forced residuals 0.79/0.37 and is REFUTED as a small-residual forced state).
- 2026-10-21 11:14 to 11:39 Section 6.3, beta = 2: nonanalytic strong unstable curves (P159; proof written 11:14:04 before code or controls, revised 11:21:09 after review 247 with the explicit two-sided transverse jets along the old segment x = A). A compact flat Hamiltonian h_+ = H(Y) chi((x - A)/Y) zeta(Y/delta), H' = eta = (delta/100) exp(-delta^2/Y^2), supported in {|x - A| <= |Y|/2}, odd reflection; time-one flow Phi with Phi(A, M/4 + Y) = (A - eta(Y), M/4 + Y); new strong unstable germ x = A - eta(Y), not a regular real analytic germ. Verification 11:23:30 (own 10 exact, 56 flow and 24 finite-difference Jacobian controls, 1.033 s; written reviews 247/248; E385): CONFIRMED; explicit Omega_new = -4(eta' + Y eta''), R_Omega,new = -4 eta' - 36 Y eta'' - 16 Y^2 eta''' = -16 epsilon delta^2 exp(-delta^2/Y^2)(8 delta^4/Y^7 - 27 delta^2/Y^5 + 11/Y^3) != 0 on both punctured branches. Analysis 11:28: own symbolic check of (3), (4) and of the sign (8z^2 - 27z + 11 > 0 for z >= 4). Separate audit A102 (asked 11:27:28, answered 11:37:56): claims 2, 3 VALID; 1, 4, 5 VALID WITH FIXES: the outgoing wedge must be the shrunken wedge c_w v(x) < (x - A)/4; the invariant set Phi(union_{t >= 0} phi_t(N)) carries R_Omega not identically zero (it contains points with Y = 0, x > A where the residual vanishes); "every other property" refers to the constructed configuration; "The construction deforms" changed to "The original configuration is obtained by deforming" and "this first map". Entered 11:39 (work/enter159.py; backup notes/FINAL_REPORT_backup_159pre.md): 6.3 bullet beta = 2, Table 8.1 row 4.7(iii)-(iv) (P159, A102).
- 2026-10-21 11:07 to 11:47 Numerics: second path (L2), lambda = 0.98: the seven inner states of the failed stage (outer secant samples 2.832303, 3.041547, 3.086675, 3.106601, 3.116675, 3.206650, 3.473375) recomputed and stored with beta fixed at 2.8323, 3.0415, 3.0867, 3.1066, 3.1167, 3.2067, 3.4734 (lead request 09:59; stored 11:07:21 to 11:37:31; MSCAN_DONE; all ok = False, inner converged). Verification 11:40:20 (P160, formula written 11:27:30 before code; certificates E388, E391, E393; separate integer checker 0.065 s; 48 angular and 18 B-spline manufactured controls): exact forced m = c_mix - 1 - beta/2 = -0.134870, -0.028943, -0.028998, -0.030989, -0.032420, -0.056132, -0.205728 (enclosures of width 1e-15), self m from -2.0902 to -1.9134, a > 0, forced R_F(0) = -2 m a from 0.0579 to 0.411: CONFIRMED center failure, REFUTED as profiles; no beta-interval exclusion, fold or branch endpoint. Entered 11:47 (work/enterL2scan.py; backup notes/FINAL_REPORT_backup_L2scanpre.md): 6.1 L2 paragraph, Summary numerics, Table 8.2 row (P160).

- 2026-10-21 11:48 Targeted referee review (tenth pass) of the changes since 11:01 asked (6.3 beta = 2 with P159, the 6.3 zero x-moment, 6.1 K40 3.04 and the L2 lambda = 0.98 states, Tables 8.1 and 8.2, section 7 from 10:41).
- 2026-10-21 11:49 Verification re-read of the lead entries of 11:18 and 11:39: CONFIRMED (6.1/Table 6.1e K40 3.04 row, 64-state caption, 6.3 zero x-moment paragraph against P147/P148, c_tail/h_ann notation, section 8 wording, P159 scope); one precision fix: Summary "at most 6e-8" to "at most 6.1e-8" (actual 6.01887516494e-8), "factors of about 2.4 to 4" (2.3805 to 3.9809). Adopted 11:50.
- 2026-10-21 11:49 Verification audit of the numerical checklist (numerics report): finite-difference steps (native wide-grid evaluator two steps, older evaluator three), the wide-grid inverse is an adaptive physical-radius sine-mode inverse (not Duffy), lambda = 0.95 K40 solve was started from the K32 state with changed strain tolerance (same stored beta; K24 differs by 2.0758e-6), no equal-budget study. Section 6.1 opening, the lambda = 0.95 sentence and the Table 6.1c resolution row corrected 11:51 to 11:52.
- 2026-10-21 11:47 Verification: P161 (harmonic local outgoing side near each endpoint at beta = 2, nonprofile, (V) fails in every full endpoint neighbourhood) CONFIRMED, 209 controls. Not entered; separate audit to be asked.
- 2026-10-21 11:56 Verification: P162 (no terminal plateau of Theta at an outgoing endpoint, beta = 2) CONFIRMED (12 exact and 60 flow controls); this checks draft 4.7(xii)(b).
- 2026-10-21 11:58 Verification re-read of the 11:55 drafts (4.7(xii), the P161 6.3 paragraph) and the 11:51 method descriptions: CONFIRMED; one precision fix in 6.1: the seven recomputed lambda = 0.98 states have beta within 5.1e-5 of the logged sample values (not "rounded to four decimals"). Adopted 12:00.
- 2026-10-21 12:04 Tenth targeted referee review (asked 11:48) collected: no incorrect formula; fixes adopted 12:04 to 12:06: 4.7 Scope of (iii)-(iv) and 6.3 (Theta - L and Omega vanish on O and to every order on its boundary; vanishing on a neighbourhood across the boundary is not established), 6.3 "(V) does not hold identically on O", 6.3 zero x-moment paragraph (construction of the signed one-parameter family by angular area-preserving maps, and the continuity of the fixed point and of the moment in the parameter, from P147 and P148); software record kept in section 8 (required by the problem); completion items at the end of the run.
- 2026-10-21 12:08 Verification re-read of the 12:06Z note items (E408): boundary flatness wording, '(V) does not hold identically on O', the 5.1e-5 precision, and the P147/P148 summary CONFIRMED with two summary repairs: delete 'compactly supported' before the angular diffeomorphism; replace 'Concentrating g'' by 'making g' small on a chosen strict-sign interval, while keeping it bounded below outside a slightly larger such interval'. Adopted 12:12 to 12:14.
- 2026-10-21 12:09 audit161 (A104) answered (asked 11:55): claims 1 to 4 VALID ((xii)(a), (xii)(b) with the trapping bound, the terminal-subarc equivalence, the P161 construction); 5 VALID WITH FIXES (the exception '(V) is not asserted to fail on O' removed: with u_* = 5 delta/2, Omega = f_+''(u_*) Y != 0 at nearby points of O); 6 VALID WITH FIXES (notation b, B, rho, N_p, Gamma_p; boundary statement). Entered 12:11 to 12:14 (work/enter161/enter.py; backup notes/FINAL_REPORT_backup_1211_pre161.md): 4.7(xii), Scope of (iii)-(iv) sentence, 6.3 beta = 2 bullet (paragraph, '(at the endpoint itself they do not, by 4.7(xii))', last sentence), Summary open core and Q1 index, Table 8.1 rows 4.7(iii)-(iv) (P161, E401, A104) and 4.7(xii) (P162, E401, A104), row 4.34 (E408).
- 2026-10-21 12:23 Verification re-read of the 12:11 to 12:14 entries (E415): 4.7(xii), both boundary statements, the
  terminal-subarc equivalence, the exp(-B rho/4) rectangle, the P161 paragraph and the 147/148 summary repairs
  CONFIRMED; the independent proof that the chosen invariant set O at each endpoint carries nonzero Omega supplied
  (P161 section 7). Clarity suggestion ("the invariant set O at each endpoint can be chosen so that Omega is not
  identically zero on O") adopted in 6.3 at 12:28; Table 8.1 rows 4.7(iii)-(iv) and 4.7(xii) updated.
- 2026-10-21 12:36 audit166 (A106) answered (asked 12:31): claims 1 to 6 VALID (wedge slices, identity theorem and harmonicity, the
  holomorphic Cauchy-data field, Cauchy uniqueness by zero extension, the analytic reduced field, the polynomial case and
  Scope); 7 VALID WITH FIXES (notation: separate the wedge width from the square width, rename the trace and auxiliary
  fields); the analytic normal derivative trace is redundant (div-curl on s = 0 determines it from the value trace).
- 2026-10-21 12:35 Verification: P166 (an analytic value trace on the normal line and analytic curl on the parallel lines
  beyond an outgoing endpoint are incompatible) CONFIRMED (101 exact and 2 negative controls, written review); P164 (the
  polynomial case) CONFIRMED 12:18.
- 2026-10-21 12:44 4.7(xii)(c) entered with the weaker hypothesis (value trace only) and the Schwarz reflection step; heading
  of (xii), Scope of (xii), Summary, section 5, 6.3 (one sentence on the conditional continuation, one on the two local
  consultations A101 and A105, neither a local solution nor an obstruction) and Table 8.1 row 4.7(xii) updated.
- 2026-10-21 12:06, 12:28, 12:44 (verification) P163 and extensions: exact rational center certificates of the eleven
  states of the beta-prescribed continuation of the second path (beta = 3.088 to 3.2): normalized (B2-P) thermal
  center limits 0.6363 to 0.6144 (all > 3/5), REFUTED as unforced profiles; forced center mismatch -6.13e-6 to
  +1.25e-5. Regional audits E409 (beta = 3.105, 12:12) and E429 (beta = 3.2, 12:44): REFUTED (forced 3.09e-4/3.15e-4
  and 6.21e-4/7.14e-4, self 0.742/0.419 and 0.727/0.414, positive thermal tail powers, C2 enclosures).
- 2026-10-21 12:48 (verification) P167: continuation inference audited; sampled minimum near (3.095, 0.98997) only; no
  fold, no branch continuity, no exclusion of roots between samples; wording repairs to section 7l of the numerics report requested.
- 2026-10-21 12:52 Beta-prescribed continuation of the second path entered: 6.1 paragraph (after the lambda = 0.98
  stage), Table 6.1c regional row, Table 6.1e (66 states, two rows L2K24_beta3.105 and L2K24_beta3.2), Summary
  numerics bullet, Table 8.2 (new P163 row; E409, E429 in the tail and C2 row), section 7 entry.
- 2026-10-21 13:00 referee11 (targeted review of the text since 11:48, asked 12:46:19): 4.7(xii)(a)-(c) valid (Schwarz
  reflection with continuity only suffices); six items. Adopted 13:03 (the pre-adoption backup was overwritten by the 13:03 rounding-fix backup; the pre-adoption text is
  notes/FINAL_REPORT_backup_1252.md plus the 12:52 entry of work/enterL2/enter.py): (1)
  6.3 signed family "vorticity taking negative values somewhere in {x > 0}"; (2) heading of (xii) "No harmonic
  neighbourhood of an endpoint; no isothermal neighbourhood and no analytic transverse data at an outgoing endpoint";
  Scope of (iii)-(iv) and Scope of (xii): the Theta - L exclusion only for profiles with an outgoing endpoint; (3) "does
  not continue" replaced by "no continuation established" (Scope of (iii)-(iv), 6.3); (4) consultations sentence: Omega
  = -curl W added, "neither a local solution nor a general obstruction; reductions and restricted obstructions"; (5)
  6.1: the seven beta values are the fixed values, within 5.1e-5 of the logged ones. Item (6) (completion items) at the
  end of the run.
- 2026-10-21 13:00 (verification) the 12:52 entry checked in the actual report: all eleven lambda values, the forced
  mismatch enclosure, the > 3/5 verdict, Table 6.1e (66 rows), the regional rows, tails, C2 and the 73-state scoping
  CONFIRMED; one repair: "between 0.614 and 0.636" is not a literal enclosure (0.61437 to 0.63632); adopted 13:05 as
  "approximately 0.614 to 0.636" (backup notes/FINAL_REPORT_backup_1303.md is the state just before this fix).
- 2026-10-21 12:46 to 13:13 (whole-report review, separate referee, asked 12:46, answered 13:04) verdict UNRESOLVED
  confirmed; one incorrect example (Scope of 4.7(xii): the shear t = z - k(s) translates each line s = const, so the
  hypotheses of (c) are preserved) and several scope and wording issues. Adopted 13:13 (backup
  notes/FINAL_REPORT_backup_131307.md; script work/ref12/apply.py): items 1 to 8, 10 to 12, 14 and the beta > 0 and
  "for some delta > 0" parts of 9 (section 1 and the completion class statement). Not adopted: item 15 (software names
  and versions stay in section 8: the problem asks for them), items 16, 17 (shortening; restructuring of 6.3). Item 13:
  the completion script now also refuses while the active time is under 48 h; the manifest is rebuilt after the last
  change at completion.
- 2026-10-21 12:54, 13:04 (verification) second path at beta = 3.25 (lambda = 0.998139): exact center certificate
  (E433): normalized (B2-P) thermal center limit 0.605594726508 > 3/5, forced mismatch -7.19e-6; regional audit (E440):
  forced 7.89e-4/1.53e-3, self 0.720/0.412, exact positive tail powers 1/13 and 2/39, C2 in [-1871.948, -1871.947],
  outer interval maxima 0.306, 0.144, 0.0863 (so not appendable to the 73-state corpus). beta = 3.3 (E439): no accepted
  stage (requested lambda 1.002067, 1.002834 clipped to 1); the two frozen intermediate evaluations (lambda 1, 0.999)
  have exact forced mismatch -0.0120, -0.0162 and self center ratios 0.598133, 0.598420 (nonzero), so they are neither
  forced roots nor profiles. Entered 13:20 (work/enterL2b/enter.py; backup notes/FINAL_REPORT_backup_132005.md): 6.1
  paragraph, Table 6.1c row (three later states), Table 6.1e (67 rows, L2K24_beta3.25), Summary numerics bullet, Table
  8.2 (P163 row extended with E433, new beta = 3.3 row E439, tail/C2 row with E440), section 7.
- 2026-10-21 13:18 audit168 asked (P168: the value-trace hypothesis of 4.7(xii)(c) is not implied by its curl
  hypothesis and the local structure; draft sentences for the Scope of (xii) and the 6.3 beta = 2 bullet).
- 2026-10-21 13:26 audit168 (A109) answered: P168 VALID with fixes (the full value trace U(0, z) is not flat, its normal
  component has derivative 2 at 0; only W_s(0, .) and the remainder of W_z(0, .) are flat; orientation of the normal);
  D1/D2 entered 13:27 with the fixes, reworded without the labels "curl hypothesis" and "value-trace hypothesis"
  (Scope of 4.7(xii), 6.3 bullet beta = 2, Table 8.1 row 4.7(xii), section 7). Backup notes/FINAL_REPORT_backup_132750.md;
  fragments at the edited lines rejoined by hand (whitespace only).
- 2026-10-21 13:20 VER: K32 states of the second path at beta = 3.0925 and 3.085 REFUTED as profiles (E447 regional,
  E448 exact center: own strain 0.6426/0.6388 vs 2.54625/2.5425, thermal center 0.635/0.637 > 3/5, forced mismatch
  -4.0e-7/-7.8e-7; lambda at 3.0925 inherited from K24, accepted after three inner iterations); P169: stored fields of
  both and of K24 3.0925 not C^5 at the 55 interior knots (exact). Entered 13:32 (work/enterK32/enter.py; backup
  notes/FINAL_REPORT_backup_133233.md).
- 2026-10-21 13:28 verification E446: referee12 adoption CONFIRMED item by item; two scope repairs (Table 6.1c far-field row;
  Scope of 4.26 clause on noninteger beta > 3) adopted 13:32; SPEC 4.7(xii) summary repaired in v41.
- 2026-10-21 13:33 referee13 asked (seventh whole pass on the completion preview); 13:39 incoming1 asked (research
  consultation: incoming and accumulating endpoints at beta = 2; nothing enters without verification + audit).
- 2026-10-21T13:51:45Z lead: K32 beta = 3.1, 3.11 center checks (verification E455, 13:40) entered 13:51 in 6.1, Summary, Table 8.2, section 7; Scope of 4.26 wording per verification E456 (vanishing conclusion C = 0 under the pure-ladder expansions). Re-read requested.
- 2026-10-21T13:52:20Z incoming1 answered (research): no counterexample, no exclusion at incoming endpoints; flatness along the strong unstable curve C (all types); conditional (xii)(c) when C meets {s>0}; arc index (eps_-+eps_+)/2, incoming => exterior degree 2; isolated exterior zeros => off-axis source pair with Theta const, Omega = 0 nearby. Not entered.
- 2026-10-21T13:55:19Z referee13 answered: UNRESOLVED confirmed; five items. Adopted 13:57 (items 1, 2, 3, part of 5); item 4 (remove software versions) not adopted (prompt requires them).
- 2026-10-21T13:58:21Z audit_inc1 asked (candidate 4.7(xiii), incl. lead's own sigma = kappa'(0) z^3/18 claim). 2026-10-21T13:58:37Z verification asked to verify (xiii)(a)-(c) and to re-read the referee13 adoption.
- 2026-10-21T14:03:22Z audit_sigma asked 14:03 (sigma_{2j+3} = (-1)^j kappa^(2j+1)(0)/((2j+3)(2j+3)!)); verification note 14:04.
- 2026-10-21T14:11:34Z audit_sigma answered (A112): C1-C3, C5 VALID; C4 VALID WITH FIXES (my linearized recurrence had epsilon inserted twice; corrected: Lap q = 4 z f'', q_3 = (2/3) f'', homogeneous recurrence from l >= 2; c_j = (-1)^j/((2j+3)(2j+3)!) confirmed; SymPy 1.14.0 constants to degree 15). Flat case: infinite-order contact, entry into s > 0 undecided (examples on s = 0, entering, staying in s < 0).
- 2026-10-21T14:12:28Z audit_inc1 answered (A113; incoming1 is A110, referee13 A111): (a) VALID; (b) VALID WITH FIXES (potential and Fermi computation formal only; accumulating case: the contradiction is that a positive zero interval extends gamma beyond p; curvature convention tau' = kappa n, arclength toward p; H(p) = 0); (c) VALID (degree 2 forces exterior zeros without isolation; isolation needed for N_{+1} - N_{-1} = 2 and the source pair). Proof outline and scope remark proposed. Entry waits for VER.
2026-10-21T14:34:49Z audit_xiii_text answered 14:33:43 (A114 after the next registry update): VALID WITH FIXES (local invariance of C; the incoming case of the count in (d); induced boundary orientation; the curvature polynomial step and the linearized constant c_j with the corrected recurrence written out; compactness of Z minus U_gamma; the axis index inequality I <= i case by case; the local entry quantifier 'in every neighbourhood' in the summaries; 'no comparable open region has been established'; 'no general exclusion'; formal potential wording; 'in general' in the last Scope sentence). All adopted in work/enter_xiii/enter.py; preview regenerated 2026-10-21T14:34:49Z (word diff: only the intended insertions). Not yet entered: waiting for the verification verdict on research/174 and 175.

<2026-10-21T14:38:10Z> 4.7(xiii) ENTERED 14:37 (backup notes/FINAL_REPORT_backup_143742.md): verification research/174 CONFIRMED (a), (c), (d) and the cubic term of (b); research/175 CONFIRMED the general odd-order formula of (b), both SUMMARY 14:27:27; audits A112, A113, A114 VALID with fixes, all adopted. Registry update: A114 = audit_xiii_text, P175, P176 (smooth finite spline counterexample). Entered text = the preview written at 14:34 except the verification cell of the Table 8.1 row and the section 7 entry. finalize preview: hazards 0. SPEC v43. Re-read requested.

<2026-10-21T14:42:03Z> ENTERED 14:41 (backup notes/FINAL_REPORT_backup_144148.md): eight K24 downward states of the second path, beta 3.0865 to 3.06 (verification 13:53 E461, 14:31 E477: center limits 0.6366 to 0.6425 > 3/5, REFUTED as profiles; forced mismatch nonzero, <= 8.0e-7; K24-K32 lambda at 3.085 = 3.29e-7) in 6.1, the Summary, Table 6.1c, Table 8.2; K32 history wording repaired per verification 14:34 (E479). Re-read requested.

2026-10-21T14:57:57Z incoming2 (research consultation, asked 14:25, answer and PROOF final 14:54, closed 14:57; A115): finite-sector theorem under incoming endpoints and isolated zeros off gamma (finitely many zeros, singleton backward limits, K a finite tree without Jordan curve, both exterior sectors in int B(q) for a source or index-0 zero; Theta = L, Omega = 0 beyond C); consequences: (xii)(b) analogue (two sectors), (xii)(c) conclusion without the condition on C (one sector), whole germ of C not analytic (two sectors), Theta(R^2) = Theta(gamma), no extra axis zero when all exterior zeros are nondegenerate; planar field (not a profile) with alpha(C_+) a saddle; no exclusion of incoming profiles. Not independently checked by the consultation. Lead check of PROOF sections 2 to 10 agrees. Candidate 4.7(xiv) drafted (work/enter_xiv/enter.py, preview 14:56); audit_xiv asked 14:57 on the frozen preview; verification asked (team note 14:57:23) for P177 to cover (a) to (f) and the planar field.

<2026-10-21T15:25:01Z> ENTERED 15:24 (backup notes/FINAL_REPORT_backup_152448.md): last four K24 downward states of the second path, beta 3.05, 3.04, 3.02, 3.0 (verification 14:58 E485 and 15:18 E493: center limits 0.6448, 0.6472, 0.6523, 0.6579 > 3/5, REFUTED as profiles; forced mismatch nonzero, <= 3.06e-6; inner residuals 1.1e-4 at 3.02 (stagnation) and 3.76e-5 at 3.0, both above 3e-5; at 2.95 requested lambda 1.012330 clipped to 1, run stopped after ten inner iterations, no root claim; beta 3.0 state close to but not identical with the seed fb30y25g24_eps0_a01 (coefficient differences 1.63e-5 cF, 3.73e-5 cG), no continuous connection inferred) in 6.1, the Summary, Table 8.2 and the timeline; 14:59 re-reading E488 noted in Table 8.2.

<2026-10-21T15:26:37Z> ENTERED 15:26 (backup notes/FINAL_REPORT_backup_152630.md): 4.7(xiv) (incoming endpoints, isolated zeros off gamma; (a) to (f)) with the related (iv), Scope of (iii)-(iv), (xii), (xiii), Summary, section 5, 6.3, Table 8.1 and timeline changes. A115 (incoming2) derivation; A116 (audit_xiv, asked 14:57, answered 15:07) VALID with fixes, adopted; verification P177 (15:12, conclusion of (b), (d), (e)) and P178 (15:24, (a), sector clause of (b), (c), (f), checked against the frozen 15:20 text = entered text, word-identical) CONFIRMED. The planar field example of the Scope (four sources, two saddles, saddle as alpha-limit of C_+) NOT entered: verification 15:24 says it is not checked by P178; held back (EXAMPLE = False in work/enter_xiv/enter.py) until verified.

<2026-10-21T15:40:00Z> audit_xv (referee audit of 4.7(xv), asked 15:21, answered 15:32; A117): VALID WITH FIXES; fixes adopted in the entry script (Q'' and E, interval step, position of (s, k(s)), openness of F, Scope: no exclusion of a harmonic extension of the restriction of U to the basin side). Frozen v2 text consultations/audit_xv_candidate_v2.md sent to verification for packet 179 (OPEN).

<2026-10-21T15:40:00Z> ENTERED 15:39 (backup notes/FINAL_REPORT_backup_153917.md): 84-radial-interval states of the second path at beta 3.0925, 3.085, 3.105 (verification 15:18 E493 and 15:30 E498): center limits 0.635, 0.637, 0.633 > 3/5, REFUTED as unforced profiles; stored lambda equal to the 56-interval values to six digits; C2 negative in every stored field, changed 15.8 percent by the refit and 53.1 percent after re-solving at 3.0925; entered in 6.1, the 3 < b_rep < 4 C2 paragraph, Table 6.1c, Table 8.2 and the timeline.

<2026-10-21T15:48:59Z> ENTERED 15:46 (backup notes/FINAL_REPORT_backup_154647.md): 4.7(xv), beta = 2 (no neighbourhood of a point of the strong unstable orbits on which Theta - L or Omega vanishes, at outgoing endpoints and at incoming ones with isolated zeros off gamma; for Z = gamma the endpoint basins are components of int{Omega = 0} and int{Theta = L}). verification P179 CONFIRMED 15:39 (independent proof, own argument for W_2 = 0); audit A117 VALID WITH FIXES, adopted (v2 text). Related sentences in Summary, section 5, Scopes of (iii)-(iv), (xiii), (xiv), 6.3, Table 8.1, timeline.

<2026-10-21T15:48:59Z> ASKED audit_xvi (referee audit of candidate 4.7(xvi), global decomposition for Z = gamma), 15:48; verification packet 181 requested.

<2026-10-21T16:03:11Z> audit_xvi (A118, answered 15:59) and audit_xvid (A119, answered 16:00): candidate 4.7(xvi) (a) to (d) VALID WITH FIXES; all fixes adopted in work/enter_xvi/text.md (v2 frozen as consultations/audit_xvi_text_v2.md, sha256 0d3c52d39ed08cd2a836d9a4b917bd1b93a0524d43f8c7daec60f8deab239142); verification packet 182 requested.

<2026-10-21T16:03:11Z> ENTERED 16:00 (backup notes/FINAL_REPORT_backup_160054.md): planar field example in the Scope of 4.7(xiv) (verification P180 CONFIRMED 15:49; from A115), with 6.3, Table 8.1 row of (xiv), timeline.

<2026-10-21T16:03:11Z> ENTERED 16:02 (backup notes/FINAL_REPORT_backup_160250.md): verification 15:51 (E507): inherited-lambda acceptance at beta = 3.0925 (84 intervals and tight tolerances), lambda differences, tight-tolerance states (center limits 0.635, 0.634 > 3/5, REFUTED; C2 change < 1e-5 relative), matched-mode C2 change 52.6 percent at 3.085; 6.1, Table 6.1c, Table 8.2, timeline.

<2026-10-21T16:08:13Z> ASKED zgamma1 (research consultation, Z = gamma at beta = 2: free boundary structure of O_+, F next to C^_+, global identities; snapshot consultations/zgamma1_report_snapshot.md).

<2026-10-21T16:19:39Z> verification packet 182 CONFIRMED 16:17 (research/182_beta2_global_three_region_decomposition; 44 exact + 4 negative controls; checks the v2 text sha256 0d3c52d3...) with one wording fix to the proof of (a) (the backward tails of the strong orbits lie exactly on {u = 0}), adopted.
<2026-10-21T16:19:39Z> ENTERED 16:19 (backup notes/FINAL_REPORT_backup_161923.md): 4.7(xvi) (Z = gamma: C^_+- disjoint properly embedded lines; F, O_+, O_- the three simply connected components; Theta = L, Omega = 0 off F; directions of O_+ = int I_+), with Summary, section 5, 6.3, Table 8.1 row (P182; A118, A119), timeline. Entered text consultations/xvi_entered_text.md sha256 8caf13531451e0dcb9815aea4c1f8136fc697f755273fe979d616b98d3d1d2a9.
<2026-10-21T16:20:35Z> ASKED referee14 (eighth whole pass, completion preview consultations/referee14_report_snapshot.md, diff from the 13:33 version).
<2026-10-21T16:24:44Z> zgamma1 answered 16:22: no exclusion or counterexample under Z = gamma; necessary conditions only (notes/zgamma1_assessment.md); not entered as an item; one factual 6.3 sentence planned with the referee14 batch.
<2026-10-21T16:37:25Z> candidate 4.7(xvii) (quasianalytic Denjoy-Carleman classes at beta = 2; lead derivation; frozen consultations/audit_xvii_text.md sha d771e153...): audit_xvii ASKED 16:37; verification packet requested 16:39.
<2026-10-21T16:53:22Z> referee14 answered 16:39 (verdict UNRESOLVED and class confirmed; seven required changes): items 1, 2, 3, 5, 7 ENTERED 16:50 together with E517 (five R84/tight regional grids) and E525 (K40 3.05) (work/ref14/apply.py; backup notes/FINAL_REPORT_backup_165026.md); item 4 deferred to the final freeze; item 6 not adopted.
<2026-10-21T16:53:22Z> audit_xvii answered 16:50: VALID WITH FIXES (exact compact-interval Denjoy-Carleman statement, A, B > 0 and disk rename, (c) hypotheses, explicit jet transport along C^, summation step and proof of the constant-8 bound, wording of the Scope). Adopted in v2 consultations/audit_xvii_text_v2.md (sha e60c5a96...); verification asked to verify v2.
<2026-10-21T16:56:54Z> ASKED endlocal1 (research: local solvability of the beta = 2 system near an outgoing flat endpoint).
<2026-10-21T17:01:45Z> verification packet 185 CONFIRMED 16:57 (on v1 d771e153...; requires the same summation step j = k + 2 and the proof of the constant-8 bound as A122; both are in v2). 4.7(xvii) ENTERED 17:00 from v2 (sha e60c5a96...; work/enter_xvii/enter.py; backup notes/FINAL_REPORT_backup_170028.md): item, Summary, section 5, 6.3 beta = 2 (including the zgamma1 sentence), Table 8.1 row (P185, A122), timeline entry. verification asked to re-read the entered text.
<2026-10-21T17:04:19Z> E530 (verification 16:59, K40/K32 at beta = 3.062: both REFUTED as unforced profiles; lambda difference 2.39e-8; C2 K40 [-5096.426, -5096.425], K32 [-4979.108, -4979.107]; exact center m K40 6.10e-6, K32 8.33e-7; recomputed certificates used, not the stored strain_mismatch metadata) ENTERED 17:03 (work/enter_k40_3062/apply.py; backup notes/FINAL_REPORT_backup_170351.md): 6.1 sentence (fourth finite comparison; C2 relative differences 0.1, 0.4, 1.0, 2.4 percent), C2 list, Summary (four values of beta, factors 1.4 to 4, vorticity ratio exception 0.58/0.74 at 3.062), Table 6.1c regional row (twelve later states), Table 6.1e row (76 states), Table 8.2 tail row (E530), timeline entry.
<2026-10-21T17:08:30Z> ASKED audit_xviid 17:08 (candidate 4.7(xvii)(d): on a dense set (complement meager) of lines of one transverse family near an arc of C^, Theta - L and Omega are flat nonzero germs, so in no C{m}, and U is in no C{m}; from verification packet 186 (directional quasianalytic obstructions; VER's own review found it correct, two wording corrections adopted: one parallel family at a time, smooth arcs of C^ instead of graph patches of C^); frozen text consultations/audit_xviid_text.md sha a7e323ef...).
<2026-10-21T17:14:42Z> endlocal1 ANSWERED 17:11 (exit 0): outcome (C), an exact local reduction at an outgoing endpoint (normal form X(a, r) on the arc side with W o X = 4 r X_r and unit Jacobian, Theta o X = theta(a), Omega by an explicit averaging of theta' y_r, one curl equation; basin-side Cauchy problem Lap H = 4, d_nu H = 0 and prescribed H on C; formal normal jets along gamma unobstructed), no local solution and no general local obstruction. Lead check notes/endlocal1_assessment.md. Candidate 4.7(xviii) to be drafted, audited and verified before any entry.
<2026-10-21T17:14:42Z> verification packet 186 CONFIRMED 17:09 (independent proof: on a residual set of lines of one fixed transverse family near a smooth arc of C^, Theta - L and Omega flat nonzero germs in no quasianalytic class; U, as a vector function, in no C{m} for each fixed m and for countably many m simultaneously; a single line can be exceptional). Matches candidate (xvii)(d) (vector membership for U, one family at a time). Entry waits for audit_xviid.
<2026-10-21T17:19:49Z> audit_xviid (A124) ANSWERED 17:18: VALID with wording fixes (open arcs of C^ as relative interiors of short compact subarcs; nondegenerate compact intervals with relative closedness; the scalar example concerns the argument, not a profile; a fixed sequence m in the nonmeager exclusion); all adopted (v2 consultations/audit_xviid_text_v2.md, sha 341b6efe...). 4.7(xvii)(d) ENTERED 17:19 (work/enter_xviid/enter.py; backup notes/FINAL_REPORT_backup_171940.md): item (d), its proof outline and Scope inside 4.7(xvii), Summary (per class and per transverse family, meager exceptional sets), section 5, Table 8.1 row (P186, A124), timeline entry. Registry 939 items (A123 = endlocal1, A124 = audit_xviid). verification asked to re-read the entered text.
<2026-10-21T17:22:59Z> ASKED audit_xviii 17:22 (candidate 4.7(xviii), exact local reduction at an outgoing endpoint, from endlocal1 (A123): (a) normal form X(a, r) with W o X = 4 r X_r, unit Jacobian, Theta o X = theta(a), Omega o X by the averaging formula, the curl equation (E), the identification of X(R) n D, converse; (b) basin side W = grad H, Lap H = 4, d_nu H = 0, grad H = 4 r c' on C, gluing converse; (c) formal normal expansion along gamma with multiplier d_m = 4m + 1 - tau_y theta'/(4(m+1)); Scope: equivalence of local solutions with these data, locality of (xii)(a), (b), (xv)(a), (b)); frozen text consultations/audit_xviii_text.md sha 50434b9e....
<2026-10-21T17:25:02Z> verification audit of the entered 4.7(xvii)(d) (17:23, frozen report ac5c19ae...): item, proof outline and Scope of (d) equal v2 341b6efe... after whitespace, CONFIRMED; main Summary and Table 8.1 row CONFIRMED; REPAIR required in the section 5 clause and the 17:03 to 17:19 timeline entry (the U statement holds for each fixed class, not for all classes at once). Repair APPLIED 17:24 (work/fix_xviid_q/fix.py, backup notes/FINAL_REPORT_backup_172440.md); re-check asked 17:24.
<2026-10-21T17:30:35Z> verification E542 (17:26): common-grid comparison of the stored K32/K40 states at beta = 3.0315, 3.04, 3.05, 3.062 (224 radii 1e-6 to 1e8, up to 3083 angles; radiuswise relative discrepancy of G 0.0100, 0.0165, 0.0246, 0.0344 and of dphi G 0.0677, 0.0967, 0.1266, 0.1566, all at r = 1e8; 64 FD controls pass), CONFIRMED as finite sampled distances. ENTERED 17:30 (work/enter_e542/apply.py; 6.1 sentence, Summary clause, Table 6.1c row, timeline; backup notes/FINAL_REPORT_backup_173029.md); compared with the radiuswise derivative value 0.003872 at lambda = 0.95 (same definition, verification 05:33).
<2026-10-21T17:31:50Z> ASKED referee15 17:31 (ninth full pass on the completion preview, snapshot consultations/referee15_report_snapshot.md, diff from referee14; focus 4.7(xvii) with (d), the 6.1 40-mode sentences and E542). Both the external referee slots in use (audit_xviii, referee15).
<2026-10-21T17:36:00Z> verification re-check of the (d) quantifier repair (17:30, verification/entered_xviid_repair_20261021T1731Z): CONFIRMED.
<2026-10-21T17:36:00Z> audit_xviii (A125) ANSWERED 17:34: (a), (b), (c) correct; required justifications (unit-speed extension of the frame, radius with |b| <= 3/2, smooth dependence via the implicit function theorem in weighted spaces, chart argument for the disk coverage, H unique up to a constant, arclength in (c)) and a Scope repair (outgoing sign requirement in the equivalence, with an example; the consequence of a local solution restated). All adopted: text v2 consultations/audit_xviii_text_v2.md sha 3cbd47e1... (17:35); sent to verification for P188 (note 2026-10-21T17:36:10Z).
<2026-10-21T17:47:00Z> ENTERED E548 (verification 17:42, K40 state at beta = 3.076: forced 0.056/0.12, (B2-P) 0.73/0.95, C2 [-5289.577, -5289.576]) at 17:46 in 6.1, C2 list, Summary, Tables 6.1c/6.1e/8.2, section 7 (work/enter_k40_3076/apply.py; backup 174654).
<2026-10-21T17:49:32Z> verification 17:47: entered E542 comparison CONFIRMED (verification/entered_E542_20261021T1748Z; no repair). verification 17:46: axis audit of K40 3.076 (finite comparisons of the forced axis functional; not entered, consistent with 3.062: the report does not carry the forced axis functional values).
- 2026-10-21T17:57:04Z ninth whole-report review (referee15) adoptions entered (items 1, 2, 4, 5, 6, 8); item 3 deferred to the final freeze; item 7 not adopted (software versions required). Re-read asked of the verifier.
<2026-10-21T17:59:28Z> ENTERED 4.7(xviii) v3 (sha 2d613940...; verification P188 CONFIRMED 17:55 with two Scope repairs, adopted in v3; A125 VALID 17:34) (work/enter_xviii/enter.py; backup 175928).
<2026-10-21T18:00:40Z> ENTERED E557 (verification 17:55, K40 state at beta = 3.092: lambda 0.932671, forced 0.088/0.15, (B2-P) 0.72/0.97, C2 [-5279.508, -5279.507]) in 6.1, C2 list, Summary, Tables 6.1c/6.1e/8.2, section 7 (work/enter_k40_3092/apply.py; backup 180040).
<2026-10-21T18:06:43Z> verification 18:02 (verification/entered_xviii_wording_20261021T1804Z): entered 4.7(xviii) and the 17:56 referee15 wording pass CONFIRMED; label repair requested ('Neumann problem' -> one-sided potential Cauchy problem with the full gradient trace) in the Summary, section 5 and the (xviii) timeline entry; applied 18:06 (work/fix_xviii_label/fix.py; backup 180643). verification 17:58: P187 exact full-plane L2 distances published (not entered yet). verification 17:59: axis audit of K40 3.092 (not entered; same policy as 3.062/3.076).
<2026-10-21T18:08:22Z> ENTERED P187 (verification 17:58, whole-plane L2 distances of G and d_phi G between the 32- and 40-mode states at beta = 3.0315 to 3.062) in 6.1, Table 8.2 and section 7 at 18:08 (work/enter_p187/apply.py).
<2026-10-21T18:38:47Z> verification re-reads recorded: E557 entry CONFIRMED 18:08:55, P187 entry and Cauchy labels CONFIRMED 18:12:32 (clauses added to their section 7 entries at 18:38).
<2026-10-21T18:38:47Z> referee16 (tenth whole-report review, launched 18:20, answered about 18:35; consultations/referee16/answer.md): no mathematical error in 4.7(xvii), (xviii); numbers consistent; literature claims L1-L5 of the proposed 4.14(j) sentence supported by the primary text. Adopted 18:38 (work/enter_ref16/apply.py, backup notes/FINAL_REPORT_backup_183834.md): items 1 (antecedent), 2 (Summary splits, local reduction as its own paragraph), 3 (Summary d_phi G sentence, section 5 beta = 2 list split at item boundaries), 4 (Table 6.1e caption: rounding scope, no definite article). Item 5 not adopted (software versions required by the prompt). Item 6 is part of the completion steps.

- 2026-10-21T18:42:50Z 4.14(j) addition (arXiv:2201.06780v3, Wang, Lai, Gomez-Serrano and Buckmaster): verifier packet P192 (primary
  text, L1-L5) CONFIRMED 18:40; tenth whole-report review A127 (18:20 to 18:36) found L1-L5 supported and proposed a
  two-sentence wording, adopted; scope phrase "a reported numerical spread, not an enclosure" from P192 added. Entered
  18:42 (backup notes/FINAL_REPORT_backup_184235.md). Verifier re-read requested.

- 2026-10-21T18:50:18Z Correction of review labels in the report (lead, from the question files): the review asked 10:01 (A96) was a
  targeted pass on the text changed since 09:06, not a whole-report review; the full passes of 17:31 (A126) and 18:20
  (A127) are the tenth and eleventh full passes (an earlier request was numbered 'sixth full pass' although it was the
  seventh). Section 8 now lists all whole-report reviews (A09, A28, A43, A61, A76, A85, A108, A111, A121, A126, A127)
  and the targeted reviews (A91, A96, A100, A103, A107). Script work/fix_reviews/apply.py.

- 2026-10-21T18:59:37Z 6.3 beta = 2, exact local solutions (fourth outgoing-endpoint consultation A128): audit A129 (18:40 to 18:44)
  VALID WITH FIXES, all adopted in v2; verifier P195 (18:48 to 18:58) CONFIRMED J1-J6 (its 18:51 note refuted the v1
  parenthetical 'center data fail', already superseded by v2). Entered 18:59 (work/enter_int1/apply.py, backup
  notes/FINAL_REPORT_backup_185925.md); Table 8.1 row 4.7(xviii) cites P195 and A129. Verifier re-read requested.
  Verifier re-read of the entered 4.14(j) addition (P192): CONFIRMED 18:48.
- 2026-10-21T19:27Z 4.7(xii)(d) (no finite separated representation of W beyond the strong unstable curve at an
  outgoing endpoint) with Scope, Summary, Q1 and 6.3 sentences, and the 6.3 type statement of the equations of
  4.7(xviii)(a) (fifth outgoing-endpoint consultation A130, 18:47 to 19:03): audit A131 (19:10 to 19:16) VALID WITH
  FIXES (domain S_+ with max(0, sigma), trace of the auxiliary field V, symbol determinant and r = 0, regularity
  qualifiers), all adopted in v2; verifier P199 (19:14 to 19:24) CONFIRMED K1-K6 of v2 (sha 8f83b20a..., which includes
  the K4 rewording "excludes in particular the polynomial case of (c)"); hash identity confirmed in the 19:27:04 note.
  Entered 19:27 (work/enter_xiid/apply.py, backup notes/FINAL_REPORT_backup_192723.md); Table 8.1 rows 4.7(xii) and
  4.7(xviii) cite P199, A130, A131. Registry kinds of A91, A96, A100, A103, A107 repaired to "targeted review"
  (verifier 19:11:56 REFUTED, repair CONFIRMED 19:27:04). Verifier re-read requested.
- 2026-10-21T20:09Z 4.7(xix) (no real analytic field equal to W on a positive-area subset of the basin side at an
  outgoing endpoint; no directional Gevrey-2 bounds for W on the basin side up to the endpoint or for Omega on a
  neighbourhood; the support of Omega in whole fibres with accumulation directions the closed half circle when the
  tangent is not vertical) with Scope, Summary, Q1, 6.3 and Scope of (xvii), (xviii) sentences (sixth outgoing-endpoint
  consultation A132, endlocal4, 19:23 to 19:36): audit A133 (19:51 to 19:58) G1 to G6 VALID, G7, G8 VALID WITH FIXES
  (blanket non-exclusion for parts of O replaced by the tangent-disk sentence and the sector/line non-exclusion;
  "of U or of Omega on a neighbourhood of the endpoint" in X8, X10(i), X11; "general obstruction", "among other
  conclusions" in X12; kappa(s) in D_M), all adopted in v2; verifier P203 (19:51 to 20:04:52) CONFIRMED G1 to G8 for
  v2 (sha c7972a01...), v1 blanket statement REFUTED as written and repaired in v2. Entered 20:09
  (work/enter_xix/apply.py, backup notes/FINAL_REPORT_backup_200954.md; the first application at 20:09:42 had point
  times for the audit and verification and was rolled back from the backup and reapplied with intervals). Table 8.1
  row 4.7(xix) cites P203, A132, A133. Verifier re-read requested.
- 2026-10-21 20:02 to 20:35 4.7(xix)(e) (statements (a) to (c) of 4.7(xix) at incoming endpoints with isolated zeros
  off gamma; heading, Scope, summary, 6.3 and Scope of (xvii) sentences). Lead derivation 20:02 (work/enter_xixe/
  text_v1.md); separate audit audit_xixe (A134) 20:03 to 20:09 VALID WITH FIXES (the Scope clause "none of (a) to (c)
  excludes profiles without an outgoing endpoint" contradicts (e) and is deleted), adopted in v2; v3 (20:11) reflow
  anchors only; verifier P204 (20:09 to 20:29:54) CONFIRMED H1 to H4 for v3 (sha 8b473871...). Entered 20:35
  (work/enter_xixe/apply.py, backup notes/FINAL_REPORT_backup_203528.md). Table 8.1 row 4.7(xix) now cites P204 and
  A134. Verifier re-read requested.
- 2026-10-21 20:13 to 20:56 4.7(xx) (accumulating endpoints: (a) Theta - L vanishes on no neighbourhood of the
  endpoint; under "no arc of zeros of W off gamma near the endpoint", (b) Theta = L, Omega = 0 beyond the strong
  unstable curve and isolation of the zeros off gamma, (c) the analogues of (xii)(b), (xii)(c), (vi) and (xiv)(d), (e),
  (d) (xix)(a) to (c)), with Scope, summary, Q1, 6.3 and Scope of (xii), (xiii), (xiv), (xvii), (xix) sentences.
  Research consultation endacc1 (A135) 20:13 to 20:27 (center-phase proof); lead proof outline by a backward invariant
  barrier made of the strong unstable curve of a nearby zero (work/enter_xx/text_v1.md); separate audit audit_xx
  (A136) 20:42 to 20:49 J1 to J6 VALID; v2 (E8 wording), v3 (C_1 constructed in the original coordinates at q_1, trace
  4 at q_1 by conjugacy, as asked by the verifier); verifier P206 (20:42 to 20:55:27) CONFIRMED J1 to J6 for v3 (sha
  bebc94b3...), with both proofs written independently. Entered 20:56 (work/enter_xx/apply.py, backup
  notes/FINAL_REPORT_backup_205627.md). Table 8.1 row 4.7(xx) cites P206, A135, A136. Verifier re-read requested.
- 2026-10-21 20:57 to 21:17 4.7(xxi) (open sets on which Theta is constant: the union V of the orbits through such a
  set is open and invariant, Theta is constant and Omega = 0 on V, U is harmonic on V; hence Theta - L vanishes on no
  neighbourhood of an endpoint of any type), with Scope, summary, Q1, 6.3 and Scope of (iii)-(iv), (xii), (xv), (xx)
  sentences. Lead derivation (work/enter_xxi/text_v1.md, sha 8118e73d...); separate audit audit_xxi (A137) 20:58 to
  21:03: K1 VALID, K2 INVALID (novelty: the conclusion also follows from (vii) and the density of the escaping set),
  K3 VALID WITH FIXES (F2, F4, Scope of (xv)); v2 (work/enter_xxi/text_v2.md, sha 49379c35...) adopts these; second
  audit audit_xxi2 (A138) 21:05 to 21:09: K1 to K3 VALID, with a correction of the Q1 sentence on the scattering
  identities ((vii) does not need Z = gamma), adopted on entry as F9. Verifier P207: v1 CONFIRMED 21:02:26, scope
  verdict withdrawn 21:08:21, v2 K1 to K3 CONFIRMED 21:14:39 (own proof and 36 controls; the cubic control is not
  x-symmetric, and a symmetric quadratic control shows the same limitation). Entered 21:17
  (work/enter_xxi/apply.py, backup notes/FINAL_REPORT_backup_211729.md). Table 8.1 row 4.7(xxi) cites P207, A137,
  A138. Verifier re-read requested.
- 2026-10-21 21:01 to 21:35 Twelfth referee pass (referee17, targeted, on the changes since the eleventh; asked 21:01,
  answered 21:15): no mathematical error, UNRESOLVED confirmed, seven wording and format items. Adopted (work/ref17/
  text_v1.md, sha b3b6f666...): R1 the section 7 description of 4.7(xix); R2 the harmonic extension through the
  endpoint in the Scopes of (iii)-(iv) and (xiv); R3 the measure condition in the Scope of (xix); R4 the quantifiers in
  the proof of (xx)(c); R5 the Summary sentence splits and the removal of two Summary clauses covered by (xxi); R6 role
  labels removed from section 7; R7 line-break repairs. Not adopted: the temperature list (superseded by (xxi)) and
  the short last lines of section 7 entries. Verifier P209 M1 to M4 CONFIRMED 21:32:29 (35 controls). Entered 21:35
  (work/ref17/apply.py, backup notes/FINAL_REPORT_backup_213548.md); a line of the new section 7 entry starting with
  "0)" was reworded in the entry list ("the constancy of Theta on the invariant line") and section 7 rebuilt, hazards
  7. Verifier re-read requested.
- 2026-10-21 18:11 to 22:05 Finite-difference Jacobian of the inner fixed-point map at the second-path state
  (beta, lambda) = (3.0952, 0.989973) (numerics computation 18:11 to 21:22; frozen array jac_L2v.npz, sha b3440290...).
  Verifier P208 matrix audit 21:23 to 21:32 CONFIRMED the numbers as linearized diagnostics (own full-plane weighted
  metric; contraction, Newton-distance and neutral-scaling inferences refuted). Report text work/j1/text_v2.md (sha
  a0dd0e03...; v1 had the audit start 21:22 and an implicit metric) CONFIRMED by P211 at 21:58:34 (33 controls).
  Entered 22:05 (work/j1/apply.py, backup notes/FINAL_REPORT_backup_220502.md): N1 sentence in 6.1, Table 6.1c row,
  section 7 entry; hazards 7. Verifier re-read requested.
- 2026-10-21 21:30 to 22:18 4.7(xxii), beta = 2: (a) no straight segment of zeros of W on which Theta is constant;
  (b) to (d) at an endpoint with Theta = L on a subarc of gamma ending there (Theta = L, Omega = 0 on the arc side of
  C; incoming: no constant neighbourhood of a point of C_+; accumulating: arcs of zeros off gamma with nonconstant
  Theta in every neighbourhood). Research consultation subarc1 (A140) asked 21:30, answered 21:43 (neither remaining
  case decided). Candidate v1 (work/enter_xxii/text_v1.md, sha cb8941da...) to the separate audit audit_xxii1 (A141,
  21:53 to 22:10: VALID, no replacement text) and to the verifier (P214, 21:54; v1 21:59 H1-H4 CONFIRMED, one H5 Scope
  repair). v2 (sha 35e95667...; the Scope's last sentence and the orientation in (a)) CONFIRMED by P214 22:14 (39/39
  controls at 22:11:32). Entered 22:18 (work/enter_xxii/apply.py, backup notes/FINAL_REPORT_backup_221803.md), equal
  to the verified preview outside section 7; hazards 7; Table 8.1 row 4.7(xxii) cites P214, A140, A141. Verifier
  re-read requested.
- 2026-10-21 21:26 to 22:49 Equal-count comparison of the forced problem at lambda = 0.95 (24, 32 and 40 angular modes,
  common transplanted seed, prescribed beta = 3.0113961, 20 map evaluations each; runs 21:26:44 to 21:48:13).
  Verifier audit P215 (histories and seeds 22:11, final states on the independent evaluator with exact center and tail
  checks 22:20: literal B2 fields REFUTED, finite comparison CONFIRMED). Report text work/eqb/text_v1.md (sha
  e0e571c0...) CONFIRMED by P219 22:39 (31 controls, no mandatory repair); the optional wording "controls the number of
  iterations" recommended by P219 adopted as text_v2.md (only change). Entered 22:49 (work/eqb/apply.py, backup
  notes/FINAL_REPORT_backup_224925.md): E1 in 6.1, Table 6.1c row, section 7 entry; hazards 7. Verifier re-read
  requested.
- 2026-10-21 22:19 to 23:08 Whole-report review of the completion preview (thirteenth; separate referee, asked
  22:19:10, answered 22:35:43): UNRESOLVED confirmed, no mathematical error or circularity in 4.7(xxi) and (xxii).
  Adoption text work/ref18/text_v1.md (sha c10f5ec6...), preview regenerated after the equal-count entry (sha
  eaaaaed6...), CONFIRMED by P221 (proof 22:51, checker 22:52:57, 74 controls, published 23:00; no mandatory repair).
  Entered 23:08 (work/ref18/apply.py, backup notes/FINAL_REPORT_backup_230850.md); the actual report equals the
  verified preview with the times substituted; hazards 7. Item 6 (session count, active duration) is part of the
  finalization. Verifier re-read requested.

- 2026-10-21 22:30 to 23:32 4.7(xxiii), beta = 2 (no temperature H(x/rho(y)) with H' nonzero at arbitrarily large
  arguments, or with H nonconstant and rho bounded above on a half-line). (a): verification proof P218 (written 22:30,
  eleven symbolic controls 22:36, CONFIRMED 22:39, published 22:39:55). Referee audit audit_xxiii1 (A143; asked 22:54,
  answered 23:03): (a) VALID, two Scope sentences to be fixed, derivation of (b) and of the plateau example; adopted
  23:05 (text_v2). Review audit_xxiii2 (A144; asked 23:05, answered 23:12): VALID WITH FIXES (S' = 4 rho in the proof
  of (b); "portions of rays issuing from (0, -b/a)"); adopted 23:13 (text_v3, sha 2f096e21...). Verification P222
  23:02 to 23:31 (v3 mathematics K1 to K3 and G1 to G3 confirmed 23:20; preview 2788e959 omitted the section 7 entry,
  flagged 23:17, corrected preview edb63301 with the entry built from entries_preview.txt CONFIRMED 23:30:50).
  Entered 23:32 (work/enter_xxiii/apply.py, backup notes/FINAL_REPORT_backup_233249.md); report sha b7129982...,
  5948 lines; the actual report equals the verified preview with the placeholders replaced by 23:32 and "23:02 to
  23:31"; hazard count unchanged. Verifier re-read requested.

- 2026-10-21 23:17 to 2026-10-22 00:01 4.7(xxiv), beta = 2 (no temperature H(x/rho(y)) on a neighbourhood of the whole
  axis, any rho > 0 and H, under (V)). Derivation by the analysis 23:17 to 23:32 (working notes). Referee audit
  sepV1 (A145; asked 23:33, answered 23:41): VALID WITH FIXES (Step 0 rescaling H(k/rho_0)), adopted 23:42; independent
  exact checks PASS. Text review audit_xxiv1 (A146; asked 23:45, answered 23:54): VALID WITH FIXES (Z0 and the first two
  sentences of Z3), adopted in text_v2 (sha d8d2e84f...) with the two verification clarifications (domain of H; F(y, Z*) = 0).
  Verification P227 23:40 to 23:59 (53 exact algebra controls, 35 entry controls on v1, 41 controls on the v2 preview
  1f54180a; CONFIRMED 23:59:27). Entered 00:01 (work/enter_xxiv/apply.py, backup notes/FINAL_REPORT_backup_000135.md);
  report sha 38d2abd7..., 6009 lines; equals the v2 preview with "23:35 to 23:52" -> "23:40 to 23:59" and the times
  99:99 -> 00:01 (2026-10-22 00:01 in the heading of the entry). Verifier re-read requested.

- 2026-10-21 23:31 to 2026-10-22 00:25 4.39 ((a) no temperature polynomial in x of bounded degree, any beta > 0; (b) for
  beta > 2 no temperature H(x/rho(y)) on R^2, rho > 0). Verification P226 ((b); proof written 23:31, 34 controls 23:33,
  CONFIRMED 23:35:20) and P228 ((a); proof written 23:44, 49 controls 23:45:26 to 23:45:27, CONFIRMED 23:47:48). Referee
  audit audit_p226_228 (A147; asked 23:59, answered 00:05:19): both VALID as written, 19 symbolic checks, two examples on
  the hypotheses. Entry text v1 (work/enter_439/text_v1.md, preview 6bf59a91) sent 00:12:45; verification P232 00:17:27 accepted
  the mathematics and asked two repairs (explicit full smooth B2 setting of 4.7(iii) in the beta = 2 Scope sentence;
  P228 controls 23:45), adopted in text_v2 (sha c32741ea..., preview 834489f2) sent 00:20:29; P232 CONFIRMED 00:23:22
  (51 + 13 controls, interval 00:17 to 00:23). Entered 00:25 (work/enter_439/apply.py, backup
  notes/FINAL_REPORT_backup_002551.md); the interval in the section 7 entry was then shortened from "2026-10-22 00:17
  to 00:23" to "00:17 to 00:23" (entries file and rebuild only); report sha 12e62cee..., 6072 lines; hazard count
  unchanged (5). Verifier re-read requested.

- 2026-10-21 23:56 to 2026-10-22 00:34 4.40 (beta > 2: no temperature H(x/rho(y)) on a neighbourhood of the whole axis
  under (S); class A through 4.37 step (5)). Verification P229 (proof written 23:56, 53 exact controls 23:57, 23 controls
  of the rescaling and of the dependencies 00:03, CONFIRMED 00:04:57). Referee audit audit_p229 (A148; asked 00:08,
  answered 00:16): VALID, 36 symbolic checks. verification 00:19:17 confirmed that 4.37 step (5) supplies (S) for class A. Entry
  text v1 (work/enter_440/text_v1.md, sha b3ddb794...), preview on the actual report after 4.39 de66fe5a sent 00:26:58;
  P233 CONFIRMED 00:33:37 (61 controls, interval 00:24 to 00:33). Entered 00:34 (work/enter_440/apply.py, backup
  notes/FINAL_REPORT_backup_003409.md); only the placeholders differ from the preview; report sha e6b76dfe..., 6144
  lines. Verifier re-read requested.
- 2026-10-22 00:09 to 00:44 4.41 ((a) beta > 2: under the axis bounds (S_f) on W_2 and Theta_xx(0, .) without zeros,
  the even axis derivatives of Theta of orders 4 to M = 2N + 4 do not all vanish; class A: some I_j, 2 <= j <= N + 2,
  is nonconstant; (b) beta = 2: I_2 and I_3 are not both constant). Verification P230 ((a); proof written 00:09, 81
  controls 00:10:15 to 00:10:23, CONFIRMED 00:13:11) and P231 ((b); proof written 00:14, 32 controls 00:15:34 to
  00:16:31, CONFIRMED 00:18:08). Referee audits audit_p230 (A149; asked 00:17:50, answered 00:25): VALID, 64 checks;
  audit_p231 (A150; asked 00:20:50, answered 00:29:03): VALID, 37 checks. Lead checks of N, M and the thresholds
  (work/enter_441/check_orders.py) 00:22. Entry text v1 (work/enter_441/text_v1.md 52ec7c79...), chained preview
  d7c436cc sent 00:32:33, preview on the actual report 1ebac043 sent 00:35:03; P235 CONFIRMED 00:37:08 (92 controls,
  interval 00:35 to 00:37). Entered 00:44 (work/enter_441/apply.py; backup notes/FINAL_REPORT_backup_004442.md); the
  section 7 interval was then shortened from "2026-10-22 00:09 to 2026-10-22 00:44" to "2026-10-22 00:09 to 00:44"
  (entries file and rebuild only); report sha dbe89412..., 6209 lines; hazard count 5. Verifier re-read requested.

## Second list: milestones after 2026-10-22 00:44

Second list (added 2026-10-22 11:05). Section 7 milestones, verbatim and in the order of section 7 (by first time), of
every result or group of results whose last event is after 2026-10-22 00:44. Each milestone covers the whole range of
its result, including any events before 00:44, which may also be recorded in the first list. For the itemized events
see the work logs named at the head of this file.
- 2026-10-21 18:00 to 2026-10-22 03:12 Sampled stagnation search of six stored fields and next-order far-field
  coefficients of six stored forced states (computation from 18:00; referee corrections of the far-field computation
  adopted 18:56): verification on a separate grid (P194): sampled positivity CONFIRMED 18:59, the inference from
  samples to the absence of zeros between them REFUTED by a manufactured field; verification of the far-field
  coefficients (P196): CONFIRMED 19:05, the implication that the missing mixed powers force the observed differences
  REFUTED; verification of the entry text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-21 18:33 to 2026-10-22 03:12 Three map scales (L = 1, 1.5 and 2.5) for the two states of the Jacobian
  diagnostics, re-solved at fixed (beta, lambda) (computation 18:33 to 21:26): independent evaluation 22:26 to 22:43
  (P217): CONFIRMED as finite diagnostics of forced states, every field REFUTED as a profile; verification of the
  entry text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-21 21:48 to 2026-10-22 03:12 Finite-difference Jacobian at the 24-mode state of the first path at lambda =
  0.96 (computation 21:48 to 2026-10-22 01:09): audit of the frozen matrix 01:06 to 01:07 (P234): CONFIRMED as
  linearized diagnostics (own full-plane weighted metric); scope repairs of the account 01:16 to 01:36 (P241, P244):
  CONFIRMED after repair, the causal explanation of the convergence of the run REFUTED; verification of the entry text
  02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-22 00:05 to 03:12 Sign-changing two-lobe external sources at eps = 0 (computation 00:05 to 00:40):
  verification 00:43 to 01:02 (P236): the bracket of the strain match for the weakly signed family CONFIRMED
  numerically, c_out = 0 for the antisymmetric pair CONFIRMED under its hypotheses, the negative transported G not
  reproduced for the literal sources; exact certificate of two further zeros of W_2(0, .) for the incomplete case
  (P238): CONFIRMED 01:01; exact rank of the temperature fit (P239): CONFIRMED 01:12; negative values reproduced
  through the fitted temperature and positive values by direct transport (P240, P247): CONFIRMED 01:46 and 01:58;
  verification of the entry text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-22 00:38 to 01:40 4.42 (the component J of {Theta_xx(0, .) != 0} containing 0: its ends are the zeros of
  W_2(0, .) nearest to 0; at beta = 2, I_2 and I_3 are not both constant on J; for beta > 2 and J unbounded, the
  statements of 4.41(a) on J, with the bounds at one infinite end): derivation in the analysis with symbolic checks,
  00:38 to 00:39; referee audit (asked 00:39, answered 00:47): VALID; proof by the verification, written 00:50, 52
  exact controls 00:51, CONFIRMED 00:54; verification of the entry text 01:26 to 01:31: CONFIRMED; entered 01:40.
- 2026-10-22 00:45 to 02:09 4.43 (beta > 2: I_2 and I_3 are not both constant on the axis component J, without
  additional derivative bounds at infinity or class A): derivation in the analysis with exact computer algebra, 00:45
  to 01:19; referee audit (asked 01:19, answered 01:37): VALID; proof by the verification, 01:19 to 01:52 (101 exact
  controls; exact certificate of 563 checks 01:48 to 01:49), CONFIRMED 01:52; verification of the entry text 01:43 to
  02:00: CONFIRMED; entered 02:09.
- 2026-10-22 01:09 to 03:12 40-mode states of the second path at beta = 3.0925, 3.085, 3.1, 3.11 and 3.076
  (computation 01:09 to 02:08): independent regional, exact center and tail evaluations 01:57 to 02:13 (P248) and
  02:19 to 02:25 (P251): CONFIRMED as finite diagnostics, every field REFUTED as a profile; verification of the entry
  text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-22 01:52 to 05:15 Diagnostics of the 40-mode state of the second path at beta = 3.085: curl and divergence
  defects of the inverse, sampled transport geometry and next-order endpoint coefficients (computation 01:52 to
  01:53): independent checks 02:28 to 02:34 (P253): CONFIRMED as finite diagnostics, no error bound for the inverse
  and no exclusion of unsampled stagnation points; verification of the entry text 05:07 to 05:13 (P279, 309 controls):
  CONFIRMED after the three exact wording corrections on the fit-growth multiplier; entered 05:15.
- 2026-10-22 01:54 to 02:27 Referee consistency review of 4.39 to 4.43 with the Summary, the Q1 bullet and Table 8.1
  (asked 01:54, answered 02:07): no error in the statements or proofs; adopted: integrality and parity conditions in
  the Summary, the sublinearity of W - beta X in the Scope of 4.39, the hypotheses of the first paragraph in 4.42 and
  4.43, the Taylor coefficients and the chart 1 and t = 0 polynomials in 4.43 (3) and (4), the reflection symbol S_y
  in 4.7(xxiv), completed letter lists of 4.7(xxiv) and 4.40 to 4.43, and a shorter Summary sentence and Q1 bullet;
  verification of the corrections P250 (02:14 to 02:18): CONFIRMED; entered 02:27.
- 2026-10-22 02:10 to 05:15 48-mode states of the second path at beta = 3.085 (an evaluation at the inherited lambda)
  and 3.1 (computation 02:10 to 02:27): independent regional, exact center and tail evaluations 02:33 to 02:40 (P254):
  CONFIRMED as finite diagnostics, both fields REFUTED as profiles; the acceptance flags of the fifteen earlier
  fixed-beta states of the second path in Table 6.1e marked y* (the fit-growth multiplier was set to 1e9 in their
  runs); verification of the entry text 05:07 to 05:13 (P279, 309 controls): CONFIRMED after the three exact wording
  corrections on the fit-growth multiplier; entered 05:15.
- 2026-10-22 02:30 to 05:15 48-mode states of the first path at beta = 3.076 (the inherited lambda, with the fields
  reoptimized) and 3.092 (computation 02:30 to 03:30): independent regional, exact center and tail evaluations 03:17
  to 03:23 (P262) and 03:46 to 03:52 (P267): CONFIRMED as finite diagnostics, both fields REFUTED as profiles; the
  sampled rise of lambda from 3.076 to 3.092 reproduced to within 1e-6, a finite comparison, not a fold statement;
  verification of the entry text 05:07 to 05:13 (P279, 309 controls): CONFIRMED after the three exact wording
  corrections on the fit-growth multiplier; entered 05:15.
- 2026-10-22 02:40 to 03:12 4.44 (beta > 2: I_2 has no nonzero finite limit at an infinite end of the axis component
  J, without derivative bounds at infinity or class A): derivation in the analysis with exact symbolic checks, 02:40
  to 02:42; referee audit (asked 02:42, answered 02:50): VALID WITH FIXES, fixes adopted; proof by the verification,
  02:48 to 02:51 (42 exact controls), CONFIRMED 02:51; verification of the entry text 03:04 to 03:10: CONFIRMED;
  entered 03:12.
- 2026-10-22 02:53 to 03:51 4.45 (for every beta >= 2 and s > -1 + 2/beta, |I_2| is not bounded below by a positive
  multiple of |y|^s near an infinite end of the axis component J; for beta > 2 every finite or infinite limit of I_2
  there is 0): proof by the verification of (a) and of the monotone case of (b), 02:53 to 02:58 (59 exact controls),
  CONFIRMED 02:58; derivation in the analysis for the positive sign of a0 I_2 with exact symbolic checks, 02:58 to
  03:05; referee audit (asked 03:04, answered 03:17): VALID WITH FIXES, the fix being the referee's proof for the
  negative sign, adopted; proofs by the verification for the positive sign, 03:11 to 03:14 (61 exact controls),
  CONFIRMED 03:14, and for both signs, 03:24 to 03:28 (50 exact controls), CONFIRMED 03:28; re-derivation in the
  analysis for the negative sign with exact symbolic checks, 03:27 to 03:28; verification of the entry text 03:36 to
  03:49 (one repair, the range beta >= 2 stated in the opening, adopted): CONFIRMED; entered 03:51.
- 2026-10-22 03:27 to 04:01 4.46 (the exponent -1 + 2/beta of 4.45 is optimal for the axis relations used there, for
  either sign of a0 I_2, and at beta = 2 every finite limit of I_2 is compatible with them; an example of axis data,
  not a profile): construction by the verification for L < 0 and for beta = 2, 03:27 to 03:38 (48 + 22 exact
  controls), CONFIRMED 03:38; exact symbolic checks in the analysis of the construction, 03:35 to 03:39, and
  derivation of the concave variant with exact symbolic checks, 03:39 to 03:41; referee audits of the construction
  (asked 03:38, answered 03:47) and of the variant (asked 03:40, answered 03:48): VALID; verification of the variant
  03:48 to 03:55 (57 exact controls): CONFIRMED; verification of the entry text 03:56 to 03:58 (203 controls):
  CONFIRMED; entered 04:01.
- 2026-10-22 03:34 to 05:51 48-mode states of a second 48-mode run of the first path, started from the 48-mode state
  at beta = 3.092, at beta = 3.076 and 3.062 (computation 03:34 to 04:51): independent regional, exact center and tail
  evaluations 04:48 to 04:54 (P277) and 04:59 to 05:05 (P280): CONFIRMED as finite diagnostics, both fields REFUTED as
  profiles; lambda solved at 3.076, 5.7e-7 above the 40-mode value, and the stored 48-mode values of lambda smallest
  at 3.076, a finite comparison, not a fold statement; verification of the entry text 05:44 to 05:45 (P284, 206
  controls): CONFIRMED; entered 05:51.
- 2026-10-22 03:50 to 04:36 4.47 (logarithmically enhanced critical tails I_2 = L y^{-m} (log y)^ell for the axis
  relations of 4.46: L < 0 for every beta >= 2 and either sign for beta > 2, examples of axis data, not profiles; at
  beta = 2, A I_2 does not tend to +infinity at an infinite end of the axis component): P266, P270 and P271
  independently proved and checked; A157 VALID (27 checks), A158 VALID WITH FIXES (37 checks), A159 VALID (24 checks);
  entry verified P274 CONFIRMED, 236 controls, 2026-10-22 04:29 to 04:31; entered 04:36.
- 2026-10-22 04:12 to 04:53 4.48 (critical limits of the axis ratios at an infinite end of the axis component: I_2 = L
  |y|^{-m} + O(|y|^{-m - eps}) under bounds on W_2(0, y) - beta y and its second derivative; for class A profiles,
  hence for every profile at beta = 2, |y|^{(n - 1) m} I_n has a finite limit for every n; for axis data the bound on
  the second derivative cannot be omitted): P272 (79 exact controls) and P275 (91 exact controls), CONFIRMED; A160,
  VALID WITH FIXES, and A158, VALID WITH FIXES (37 exact checks), with their repairs adopted; independent verification
  of the complete entry 04:44 to 04:47: P276, 273 controls, CONFIRMED after the exact p_n notation correction; entered
  04:53.
- 2026-10-22 04:31 to 05:37 4.49 (a bounded axis component is consistent with all axis equations: smooth fields of
  compact support with the canonical inverse, not profiles, satisfy (T) and (V) to every order on the axis, at every
  beta >= 2, with J = (-3, 3) and A I_2 -> -infinity at both ends of J): independent proofs of the bounded axis data
  and endpoint limits (P273, 65 exact controls) and of the smooth fields with all axis jets (P278, 93 exact controls,
  15 scope controls and 25 + 16 supplementary controls): CONFIRMED; referee audits A161 (VALID WITH FIXES, 36 exact
  checks) and A162 (correct, with editorial fixes), with their fixes adopted; independent verification of the complete
  entry text 05:32 to 05:35 (P282, 223 controls): CONFIRMED with two exact wording corrections; entered 05:37.
- 2026-10-22 05:23 to 06:21 4.50 (exact temperature transport is consistent with a bounded axis component: smooth
  fields, not profiles, with Psi and Omega of compact support and the canonical inverse, satisfy (T) on R^2 and (V) to
  every order on the axis, at every beta >= 2, with J = (-3, 3) and A I_2 -> -infinity at both ends of J): independent
  proof of the fields (P283, 55 controls, of which 45 exact or literal and 10 numerical quadratures of the correction
  without error bounds, and 15 supplementary exact controls): CONFIRMED; referee review A162, which proposed the
  correction along the flow, and referee audit A164 (valid with clarifications, adopted); independent verification of
  the complete entry text 06:02 to 06:04 (P290, 165 controls): CONFIRMED; entered 06:21.
- 2026-10-22 05:23 to 06:59 restarts of six stored stages of the two paths with 48 Gauss points per radial quadrature
  cell of the computation's inverse (computation 05:23 to 05:44) and the runtime velocity norms reported by the
  computation (05:45): independent regional, exact center, tail and inverse-constant evaluations 05:53 to 06:15
  (P287): CONFIRMED as finite diagnostics, all six fields REFUTED as profiles, every inherited lambda accepted and
  none redetermined; independent full-plane relative velocity norms at the same angles 06:11 to 06:17 (P291):
  CONFIRMED as a finite comparison, a conditional diagnostic and not an error bound, the runtime difference arrays not
  reproduced; verification of the entry text 06:41 to 06:56 (P298): CONFIRMED, 468 controls; entered 06:59.
- 2026-10-22 05:50 to 07:50 redeterminations of lambda for the 32-mode stage of the first path at beta = 3.062 with 12
  and 48 Gauss points per radial quadrature cell of the computation's inverse (computation 05:50 to 06:21):
  independent regional evaluations 06:26 to 06:31, with exact center and tail checks and summary by 06:37 (P294, 141
  controls): CONFIRMED as finite diagnostics, both fields REFUTED as profiles, the two values of lambda 1.76e-8 apart,
  without establishing existence of exact discrete roots at both orders or a difference between them; verification of
  the entry text 07:26 to 07:38 (P305): CONFIRMED, 342 controls; six wording corrections; entered 07:50.
- 2026-10-22 05:52 to 06:31 4.51 (finite ends of the axis component at which the axis velocity vanishes to a finite
  order p >= 2: the axis flow moves toward the end, T, Omega_x(0, .) and d_x^4 Theta(0, .) are flat there, D/T = -(3
  d0/beta) p (p - 1) s^{-2} (1 + o(1)) and A I_2 -> -infinity; necessary conditions, realized by local solutions of
  the four axis relations): independent proof (P286, 114 exact controls): CONFIRMED; referee audit A166 (VALID, 53
  exact checks, precision in step (3) adopted); independent verification of the complete entry text 06:20 to 06:27
  (P292, 152 controls): CONFIRMED with scope repairs; entered 06:31.
- 2026-10-22 06:01 to 06:31 4.52 (ends of the axis component at which the axis velocity vanishes to infinite order:
  local solutions of the four axis relations with b = sgn(y_*) exp(-1/s) (2 + sin(s^{-2})), flat at the end, for which
  A I_2 has subsequences tending to +infinity and to -infinity, and with b = sgn(y_*) exp(-1/s), for which A I_2 ->
  -infinity; so 4.51 (b) does not extend to such ends on the strength of these relations): independent proof (P289, 51
  exact controls): CONFIRMED; referee audit A165 (VALID, 37 exact checks); independent verification of the complete
  entry text 06:23 to 06:28 (P293, 158 controls): CONFIRMED with the local scope correction; entered 06:31.
- 2026-10-22 06:40 to 07:33 Whole-report review of the completion preview (fourteenth, A168): UNRESOLVED confirmed; no
  mathematical error found in 4.7(xxiii), (xxiv) and 4.39 to 4.52; adopted: the finite ends of the axis component
  (4.51 to 4.53) in the Q1 bullet on restricted temperature representations, the wording of the Scope of 4.50 on 4.49,
  the word "earlier" in the entry on the 48-mode states of the second path (fifteen flags were changed there; the two
  new states were stored with y*), and a split of the Summary bullet on temperature and the axis; not adopted: the
  replacement of the software versions in section 8 (they are part of the required documentation) and the joining of
  short source lines before displayed formulas; the controlling run instructions cap the wall-clock run at 48 h;
  finalization records the real elapsed time and the gaps between sessions separately, without counting gaps as active
  research; verification of the changes 07:22 to 07:30 (P307): CONFIRMED, 81 controls; one duration correction;
  entered 07:33.
- 2026-10-22 06:43 to 07:27 4.53 (ends of the axis component at which the axis velocity has a simple zero: I_2 has a
  limit in [-infinity, infinity]; if b''(y_*) != 0, D/T is asymptotic to -6 n sgn(y_*) b''(y_*) (4 beta + 3
  kappa)^{-1} s^{-1}; local polynomial and real analytic solutions of the four axis relations with every finite limit
  of I_2 and both infinite limits of A I_2, at beta = 2 with the signs and integrality of 4.13 and for every beta > 0
  without them): independent proofs P296, P299 and P303: CONFIRMED; referee audits A167 (VALID) and A169 (VALID with
  scope corrections); complete-entry verification 07:11 to 07:21 (P304, 167 controls): CONFIRMED with the seven
  wording corrections; entered 07:27.
- 2026-10-22 07:16 to 08:19 4.54 (the next vorticity relation at a simple end of the axis component, beta = 2: in the
  family of 4.53 (e) it has a smooth solution only if H = -k^7/231, which with the signs of a profile gives A k < 0
  and I_2 -> +infinity from below; other local real analytic solutions of the five axis relations, with the signs and
  integrality of 4.13, have every finite limit of I_2 and both infinite limits of A I_2): independent proofs P306 and
  P311: CONFIRMED; referee audit A170 (VALID with three corrections); complete-entry verification 08:08 to 08:16
  (P312, 242 controls): CONFIRMED, three wording corrections; entered 08:19.
- 2026-10-22 07:26 to 08:50 4.55 (two further axis relations at a simple end of the axis component, beta = 2: in the
  family of 4.54 (a) with H = -k^7/231 the relations for the coefficients of x^6 in Theta and of x^5 in Omega on the
  axis have smooth solutions for exactly one choice of the two free constants of D and gamma, the coefficient matrix
  of the two residues having determinant -27 C^2 k^2/125): independent proof P308: CONFIRMED; referee audit A171
  (VALID; one intermediate display corrected in its adjudication P320); complete-entry verification 08:42 to 08:49
  (P319, 129 controls): CONFIRMED; entered 08:50.
- 2026-10-22 08:36 to 09:26 4.56 (the axis relations of every order at a simple end of the axis component, beta = 2:
  in the family of 4.54 (a) with H = -k^7/231 the relations (T_n), (V_n) and the curl relation of 4.49 (2) of every
  order have solutions that are real analytic on one interval about the end for exactly one choice of the two free
  constants at each order, the coefficient matrix at order n having determinant -54 C^2 k^2/(25 n (2 n + 1)); formal
  in x, no convergence, no profile): independent proofs P321 (192 controls) and P326 (88 controls): CONFIRMED; referee
  audits A173 (VALID) and A174 (VALID); complete-entry verification 09:13 to 09:22 (P325, 611 controls): CONFIRMED;
  entered 09:26.
- 2026-10-22 09:05 to 09:57 4.57 (the leading part of the temperature series at a simple end of the axis component,
  beta = 2: in the family of 4.56 the series Theta in x^2 and u = y_* - y has no term of total degree below 11, and
  its part of degree 11 is (C/2) x^2 (u - k x^2/11)^10; formal, no zero curve, no convergence, no profile):
  independent proof P328 (156 controls): CONFIRMED; referee audit A175 (VALID for the proof); complete-entry
  verification 09:35 to 09:49 (P332, 1983 controls): CONFIRMED, one correction of the Scope; entered 09:57.
- 2026-10-22 09:26 to 10:16 4.58 (a factorization of the temperature series at a simple end of the axis component,
  beta = 2: in the family of 4.56, Theta = (C/2) x^2 Z^10 with a formal series Z in x^2 and u = y_* - y whose part of
  degree 1 is u - k x^2/11, Z being u - h(x^2) for a formal invariant curve times a formal unit, and Theta = (C/2) I^2
  for the odd formal first integral I = x Z^5; formal, no convergence, no off-axis zero curve, no profile):
  independent proof P331 (184 controls): CONFIRMED; referee audit A176 (VALID); complete-entry verification 10:02 to
  10:15 (P336, 1107 controls): CONFIRMED; entered 10:16.
- 2026-10-22 10:00 to 10:33 4.59 (the temperature near a simple end of the axis component, necessary conditions, every
  positive beta: near (0, y_*), Theta = (C_u/2) x^2 Z^n with Z = (u - H(x)) L, L > 0 smooth and u = H(x) the smooth
  unstable curve of W, H = k x^2/(4 beta + 3 kappa) + O(x^4); Theta vanishes there exactly on the axis and on this
  curve, has the sign of C off them if n is even and changes sign across the curve at its points with x != 0 if n is
  odd; no profile): independent proofs P334 (beta = 2, kappa = 1, 53 controls) and P337 (74 controls): CONFIRMED;
  referee audit A177 (VALID with two fixes, both adopted); complete-entry verification 10:14 to 10:33 (P338, 271
  controls): CONFIRMED; entered 10:33.
- 2026-10-22 10:16 to 10:43 4.60 (the vorticity near a simple end of the axis component, necessary conditions, beta at
  least 2: near (0, y_*), Omega = E_u x Z^m Y with Y smooth and positive, Z and the curve u = H(x) as in 4.59 and m =
  1 + (2 beta + 1)/kappa; Omega vanishes there exactly on the axis and on the same curve as Theta, to the order m off
  the axis, and x Omega Theta is positive off the two curves; no profile): independent proof P339 (183 controls):
  CONFIRMED; referee audits A178 (VALID, no corrections) and A179 (the text of the entry, VALID, no corrections);
  complete-entry verification 10:27 to 10:42 (P342, 533 controls): CONFIRMED; entered 10:43.
- 2026-10-22 10:46 to 10:59 Summary and section 5 sentences on 4.57 to 4.60 (the formal factorization of the
  temperature series at beta = 2 and the factorizations of Theta and Omega near a simple end of the axis component):
  referee audit A180 (VALID, no corrections); complete-entry verification 10:55 to 10:57 (P345, 246 controls):
  CONFIRMED, two wording clarifications; entered 10:59.
- 2026-10-22 12:43 Completion of the report: the headline (UNRESOLVED; neither accepted endpoint reached), the
  finalization cutoff as the end time, the elapsed wall-clock time, the recorded session durations and the position of
  the cutoff relative to the 48 h wall-clock cap; the artifact manifest (Table 8.3) records the archive build
  completion time and checksums, with the registry measured separately at finalization. The remaining editorial items
  of the fifth referee review are settled as follows: the section 4 results are traced to their packets and
  consultations in Table 8.1, and the timeline is condensed in this section (the complete timeline is among the
  artifacts).
