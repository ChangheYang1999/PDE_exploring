# Final report: full-plane IPM self-similar profiles with even-x / odd-y symmetry (Setting I)

STATUS: FINAL REPORT; REQUESTED ENDPOINT NOT REACHED. Strong setting P_inf (the question of this follow-up, section 6): NOT REACHED. Neither endpoint was
established: no YES_inf candidate with a smooth centre was computed, and no NO_inf theorem was proved; the exact
remaining gap is stated in 6.5 and summarized below. Weaker problem P_2 (first investigation, unchanged): YES, strong
numerical existence evidence (not an endpoint for the strong setting of the prompt), for the explicitly
distinguished weaker problem P_2 (rho in C^(2,alpha)_loc, a only continuous with a(0) = 1), as stated in section 4. It is numerical evidence and not a proof. The independent verifier
recomputed or checked every number of section 4 as written and confirmed the endpoint against the standard defined
before 4.1; every statement of section 3 was checked by the verifier and by an external referee. The posed strong
setting was not answered by the first investigation (section 4, items (i) and (ii)) and is not answered by the
follow-up (section 6).

UPDATE (follow-up investigation of the strong setting P_inf). T0 = 2026-10-20T00:46:19Z. The run was limited to 24
hours and was stopped at its time cap, 2026-10-21T00:46:19Z; the endpoint assessment remained unchanged at the cap. T_end =
2026-10-21T00:57:29Z (report finalization, after the research cap), so the elapsed time T_end - T0 is 24 h 11 min 10 s (24.19 hours),
and the recorded elapsed span exceeds 24 hours. This span includes finalization and does not by itself verify the required active research time. The content of the report was frozen at its
cutoff, 2026-10-21T00:00:37Z (23 h 14 min 18 s after T0); the verifier's final checks before the cap confirmed the
frozen text and found no later result that changes it, and at finalization only the status lines, the timing
statements, the paragraph below on what this round added and the description of the accompanying artifacts were
edited (no result changed). Neither endpoint of the follow-up was reached. Sections 0 to 5 and the appendix entries up
to 2026-10-19 12:04 retain the published results, with publication wording and references corrected; section 6 states the substantive updates.

What this round added. The first investigation reported evidence for P_2 (YES, numerical evidence) and left P_inf open. The
follow-up (a lead researcher, a numerical researcher and an independent verifier, with external referee audits by a
second model) added section 6: (1) necessary conditions for a smooth centre, proved under stated regularity at the
source P (B_3(c_l, w) = 0, and B_j = 0 at the higher nonresonant odd orders under higher regularity at P), and forced
by the class alone for 1 < c_l <= 3/2; (2) an explicit pair that solves the local equations exactly and is smooth near
0, along the axis segment and near P, so these conditions are locally consistent and a NO theorem must use a global
property; (3) conditional and restricted nonexistence results, none of them NO_inf (a sign criterion, explicit
exclusion balls around reference traces with certified constants, exclusion of the explicit R12 family of axis data
under extra regularity at P, no profile with a fixed finite angular cutoff, a nonzero homogeneous trace at infinity
for every profile); (4) a recomputation of the published candidate with separately written code, reproducing its
residual level and showing that it fails the smooth-centre test (B_3 about 0.31 natural units), so it is a P_2 and not
a P_inf candidate; (5) full collocation solves with the canonical whole-plane inverse at four resolutions and three
domains, which were not brought below a 2-norm residual of about 2e-4 and did not decide whether an exact profile near
the candidate is isolated or part of a family. The follow-up's code and data are in the accompanying artifacts; the accompanying artifacts of the first investigation are unchanged.

In sections 0 to 5, B_3 is the coefficient of the homogeneous solution in R7, which equals the axis functional of R10
when the origin expansion of R10 holds and l_3 = 0 (for A_3 profiles, or when the third transverse trace is bounded at
P). For a profile of P_inf that is only C^(2,alpha) at P, that coefficient is C_0 = l_3 + B_3, with B_3 the finite-part
functional and l_3 the limit at P of 6.3.1 (a), provided the finite-part hypotheses of 6.3.1 (a) hold and that limit
exists; the existence of a finite l_3 is not known for every profile of P_inf with A > 2. So a nonzero value of B_3
alone does not exclude a smooth centre: the inference in the Summary, item (ii), and in section 4, item (ii), from a
nonzero value of B_3 to a centre that is not smooth is valid when l_3 = 0 (which holds for A_3 profiles, under the
Hoelder or cone hypothesis of 6.3.1 (h), and for 1 < A <= 2 by 6.3.1 (m)), or more generally when l_3 is finite and the
cancellation l_3 = -B_3 is excluded.

State of the follow-up at the end of the run, as at the report cutoff (section 6 separates verified results from open questions and from results
that were not checked): neither endpoint has been reached. Here A = 2c_l - 1, and P = (x*, 0) is the hyperbolic source
on the positive x-axis of section 3. In brief: (1) proved necessary conditions at the centre: smoothness near 0 forces
B_3(c_l, w) = 0 when the profile has in addition a bounded third trace at P, or is C^(2,alpha) near P with
alpha > 1 - 2/A, or satisfies a cone form of that hypothesis, with analogues at the higher odd orders under higher
regularity at P, and for 1 < c_l <= 3/2 the class alone forces B_3(c_l, w) = 0; (2) these conditions are locally
consistent: an explicit pair solves the local equations exactly and is smooth near 0, along the axis segment and near P,
so a NO theorem must use a further property of admissible profiles, such as the growth bounds or the canonical velocity
law; (3) conditional and restricted nonexistence results, each under additional hypotheses stated in 6.3.1 and 6.5 and
none of them NO_inf: under the pointwise sign condition (H_-) on the axis data (A > 2), within explicit small balls
around reference traces in specified weighted norms, and for the explicit two-parameter family of axis data of R12
(6.5); and no profile of P_2, smooth at 0 or not, has a density with a fixed finite angular cutoff (6.3.1 (p)); (4)
numerically the published candidate fails the smooth-centre test (trial-data estimates of B_3 about 0.31 natural units),
so it is a P_2 candidate and not a P_inf candidate, and whether an exact profile near it is isolated or part of a family
was not decided: the numerical researcher's full collocation solves were not brought below a 2-norm residual of about
2e-4 (6.4); (5) the remaining gap (6.5): for c_l > 3/2 no argument excludes C_0 = l_3 + B_3 = 0 for profiles with only
the regularity of the class (even the existence of the source limit l_3 is open there, and under the Hoelder hypothesis
at P no global sign or nonvanishing mechanism for B_3 is known); for 1 < c_l <= 3/2, where B_3 = 0 is forced, no further
necessary condition that the known compatible axis data fail is established under the regularity of the class alone; and
no candidate with a smooth centre has been computed. The items below give the precise statements.
- Proved, under the hypotheses stated in 6.3.1: if a profile of the class is C^infinity near 0 and, in addition, d_y^3
  rho(x, 0) stays bounded as x -> x*^-, or rho is C^(2,alpha) near P with alpha > 1 - 2/A
  (0.803 on the computed branch), or a weaker cone form of that Hoelder hypothesis holds, then B_3(c_l, w) = 0
  (6.3.1 (f), (h)). These proofs use the propagation of smoothness from 0 along the open axis segment, proved in 6.3.1
  (f) from textbook facts only; for the bounded-trace statement, and under the Hoelder or cone hypothesis, the
  third-order step along the segment is also proved directly, without that propagation (6.3.1 (f), (m)).
- At the higher odd orders, for odd j >= 5 and a profile of P_inf that is in addition C^(j-1,alpha) near P with
  0 < alpha < 1 and alpha > 1 - (j-1)/A, l_i = 0 for the odd i with 3 <= i <= j, and smoothness near 0 then gives
  B_i(c_l, w) = 0 at the nonresonant orders among them (at a resonant order a logarithmic compatibility condition
  instead; 6.3.1 (h)). These are necessary conditions, not a NO theorem. The local equations do not obstruct smoothness
  at 0: the explicit pair of 6.3.1 (c) solves them exactly and is smooth with the required normalization near 0, along
  the axis segment and near its first source P, and for every A > 1 it has a smooth compactly supported extension with
  the canonical velocity that satisfies (A1) to (A3), the normalization and the profile equation on any bounded region
  fixed in advance, including neighbourhoods of 0, of P and of the axis segment between them, and fails the profile
  equation elsewhere (6.3.1 (c)). These conditions alone are therefore consistent; conditional exclusions under
  additional trace hypotheses remain possible (6.3.1 (k), (n), (o)).
- For A > 2 and axis data that are smooth at 0 and of class C^(2,theta) at P with theta > 1 - 2/A (the trace hypotheses
  of 6.3.1 (k); they hold for a profile of P_inf with that Hoelder hypothesis at P), B_3 is an ordinary convergent
  integral of the axis data, and a profile of P_inf that satisfies these trace hypotheses together with the Hoelder
  hypothesis at P or its cone form (the full Hoelder hypothesis supplies the trace hypotheses; the cone form alone does
  not) cannot satisfy the
  pointwise sign condition (H_-) on its axis data (6.3.1 (k)). This is a proved conditional nonexistence theorem; under
  the stricter reporting convention of 6.1 it is not counted as NO, because (H_-) is an inequality on the profile's own
  axis data that implies the sign of the obstruction and is not known to hold for any class of profiles.
- If the y^3 axis coefficient divided by its homogeneous solution has a finite limit l_3 at P, smoothness near 0 gives
  B_3(c_l, w) = -l_3. In the frozen examples of 6.3.1 (g), within their stated parameter ranges and in particular at the
  computed parameters, C^(2,alpha) regularity with alpha <= 1 - 2/A does not force
  l_3 = 0, and one-sided smoothness does not force l_3 to be finite (6.3.1 (g)). Whether l_3 exists and vanishes for
  every exact profile of P_inf with c_l > 3/2 is open.
- For 1 < c_l <= 3/2 the Hoelder hypothesis is part of the class, so every profile of P_inf there has B_3 = 0 (6.3.1
  (m)), with a further fifth-order condition at c_l = 3/2 (6.4, checked by the verifier); compatible axis data satisfy
  these conditions, so that range is not decided either. For 1 < c_l < 3/2 the compatible data of R12 at the zero of B_3
  have B_5(c_l, w) < 0, so they are not the axis data of a profile of P_inf that is in addition C^(4,alpha) near P for
  some 0 < alpha < 1, or that, with rho and W smooth on the left part of a punctured neighbourhood of P, satisfies the
  summable weighted bound of 6.3.1 (h) on the fourth derivatives of both rho and W = c_l X + U in a left cone at P;
  under the regularity of the class alone such a profile would need the cancellation l_5 = -B_5(c_l, w) > 0, which these
  arguments leave unresolved (the frozen examples of 6.3.1 (j), at specific parameter pairs, do not settle it; transport
  and constant divergence, even with the parities, the source structure, C^3 regularity at P and smoothness on the
  punctured neighbourhood, do not imply l_5 = 0 (6.3.1 (j)); 6.5). With f = rho, r = x* - x and the smoothness to the
  left of P assumed in 6.3.1 (h), the curl identity shows that this weighted hypothesis follows from the additional
  bounds |D^4 f| <= C r^(-p) and |D^5 f| <= C r^(-P_0) on a larger left cone at P, with 0 <= p < 4/(2 c_l - 1) - 1 and
  P_0 finite, for every 0 < alpha < 1 when 1 < c_l <= 7/6, and when alpha > 3 - 4/(2 c_l - 1) for 7/6 < c_l < 3/2 (6.3.1
  (h)). The sign B_5(c_l, w) < 0 of these data is exact for every c_l > 1 with c_l != 3/2 (6.5), and for c_l > 3/2 they
  are excluded in the same way for profiles of P_inf that are C^(4,alpha) near P (with alpha > 1 - 4/(2 c_l - 1) when
  c_l >= 5/2) or that satisfy the summable weighted bound. At c_l = 3/2 (A = 2) and L = 2 the source-selected seventh
  coefficient of these data is exactly B_7(c_l, w) = -23/29059430400 (natural units -23/14189175); with the third- and
  fifth-order conditions this excludes the whole two-parameter family of R12 axis data (A > 1, L > 0) for profiles of
  P_inf that are in addition C^(6,alpha) near P for some 0 < alpha < 1 (6.5). This restricted exclusion concerns one
  explicit family of axis data and is not NO_inf.
- Near an explicit compatible trace at c_l = 5/2, no profile of P_inf with the Hoelder or cone hypothesis at P, first
  source at x* = 4 and an axis trace of class C^(2,3/4) on [1/4, 4] has its trace within an explicit radius (6.3.1 (n);
  certified radii in a weaker weighted norm in 6.3.1 (o)), far too small to bear on the computed branch. At the computed
  c_l an external referee gives such an exclusion with polynomial constants in the weighted norm N of 6.3.1 (o) (for
  |A - A_0| <= 0.06 with A_0 = 10.150725, |x*^(-2) - e_0| <= 0.0003 with e_0 = 0.0135206 for the explicit reference and
  e_0 = 1/8.6000638^2 for the fitted one, and normalized traces w~(u) = w(x* u)/x* in the affine domain of that norm,
  which includes an anchored exponent 9/10 at the source), with each ball centred at (A/A_0) w_0 for its reference trace
  w_0 at A_0: radius 1e-6 for the explicit reference, a compatible trace that is not close to the computed one, and
  certified radius 4.5e-6 for the fitted one, an analytic compatible fit to the computed trace (6.3.1 (o); checked by
  the verifier, and the analytic estimates and the certificate each audited by a further external referee); the trial
  data do not establish that the trace of an exact profile lies within such a radius of any reference, and sampled
  agreement alone cannot (equally good fits are 9 to 67 apart in that norm, sampled).
- No profile of P_2, and hence none of P_inf, has a density whose angular expansion in the physical polar angle has one
  fixed finite cutoff valid for every radius (6.3.1 (p)). The density of the computed candidate is not of this form,
  and this restricted theorem does not exclude an exact profile with infinitely many angular modes, nor its
  approximation by increasing angular cutoffs.
- Every profile of P_2, and hence of P_inf, has a nonzero homogeneous trace at infinity: rho(r theta) = r^(1/c_l)
  F(theta) + O(r^(1/c_l + gamma - 1)) uniformly, where gamma is an exponent from (A3), with F Hoelder continuous and not
  identically zero (6.3.1 (q)). This is
  a necessary far-field datum; it does not say whether F can be prescribed or varies along a family, and it decides no
  endpoint.
- On a left cone at the source the coupled equations have exact analytic solutions whose first nonvanishing higher odd
  transverse coefficient on the axis, of any odd order m >= 3, is C r^(-(m-1)/A) with any prescribed C != 0, r = x* - x
  (6.3.1 (r)). They show that, in its cone formulation, the strict exponent condition alpha > 1 - n/A of the higher
  trace criterion of 6.3.1 (h) (n >= 2 even) cannot be relaxed to equality when A > n; they live on a cone only, with a
  chosen local velocity, and decide no endpoint. For any finite set of odd seeds the construction also gives distinct
  solutions for distinct source-amplitude vectors, real-analytic in the amplitudes, on a common sufficiently small cone
  for each bounded set of amplitudes (6.3.1 (r)); these are not profiles and give no family of profiles of P_inf.
- Numerically, trial-data finite-part estimators of B_3 (they use the trial's g as well as w) give 0.31 +- 0.015 natural
  units on the published candidate (the observed spread over the numerical choices of 6.2), recomputed with separately
  written code, and the trial's own coefficient is 0.046, so it is a P_2 candidate and not a P_inf candidate (6.2); on
  the ten stored trial traces of the first investigation (nine fixed-c_l fits, among them X3, and the free control F3)
  B_3 is about 0.30, with no resolved dependence on c_l (6.3.2 (d)), and 0.28 to 0.30 when the polynomial origin
  coefficients are refitted together with a non-polynomial term (a sensitivity test of the estimator, 6.4). The
  obstruction functional is ill conditioned in the origin layer (6.3.2 (c)).
- Whether an exact profile exists near the computed candidate and, if so, whether it is isolated or part of a family,
  and how B_3 varies along a family, are not decided; the
  analytic relations and the conditional sign criterion above give no unconditional sign mechanism; other branches were
  not computed. What was tried and the exact remaining gap are in 6.4 and 6.5.

## Summary
T0 = 2026-10-17T17:37:12Z (start of the investigation). T_end = 2026-10-19T12:04:44Z. Elapsed time = 42.46 hours.
The recorded elapsed span exceeds 24 hours; elapsed time alone does not verify the required active research time.

YES, strong numerical evidence, for the explicitly distinguished problem P_2 (section 1: P_m with m = 2).

(i) The posed strong setting (a smooth and even near 0) is not answered by this result (see section 6).
(ii) On the computed trial family the B_3 estimator is about 0.30 natural units x*^(2 - p_3): B_3 = 0.299 to 0.303 on
    the candidate (medians over the evaluation configurations of the two forms of the independent evaluator's estimator
    and of the original form of R10; variant extremes 0.291 to 0.311), 0.298 to 0.303 on its control, positive in every
    variant; in either form it changes by less than 0.005 along the angular refinement m <= 100 to m <= 250, under a
    further 20750 iterations and with fit rows to 9000 L (4.1). The trial's own coefficient of y^3 |x|^(p_3) is +0.046
    in the same units (positive; the difference is carried by the trial's defects in the y and y^3 coefficients of the
    equation on the x-axis, 4.1). A C^infinity profile has B_3 = 0 (R7, proved). If an exact profile exists near the
    trials and has a well-defined nonzero B_3, it is not C^infinity near 0 and does not solve the strong setting. The
    estimator value is numerical evidence for this; no estimate transfers it to an exact profile, so it is not proved.
    [Follow-up correction (2026-10-20): here B_3 is the coefficient of the homogeneous solution in R7, while the
    estimator measures the finite-part functional of R10; the two agree when l_3 = 0, for instance for A_3 profiles.
    When the finite-part hypotheses of 6.3.1 (a) hold and the limit l_3 exists, the coefficient equals l_3 plus the
    functional, so a nonzero value of the functional excludes a smooth centre only if l_3 = 0 or the cancellation of the
    two is otherwise excluded; neither the trial estimates nor proximity to the trials establishes this for a nearby
    exact profile (status note at the beginning; 6.3.1 (a), (g)).] It is not a NO theorem, and other branches are not
    excluded.
(iii) The class is stated only as far as proved: P_2 requires rho in C^(2,alpha)_loc and a continuous with a(0) = 1. No
    higher regularity of an exact profile is claimed. The trial satisfies the regularity, parity, normalization and
    growth requirements of P_2; its transport residual is nonzero, so it is an admissible trial density, not a member of
    P_2. The numerical claim is the one of 4.1 (evidence consistent with the existence of an exact profile of P_2 near
    the trial; neither the proximity nor the exponent is established); it is not a proved statement. Uniqueness within
    P_2 is not claimed, and other branches are not excluded.
(iv) The computation does not determine c_l: the tested exponents that the rule of 4.3 does not exclude on the
    candidate's radial basis with angular cap m <= 150 span [5.5524653, 5.5793640] (an observed span, not an enclosure
    of the exponent of an exact profile). The candidate is computed with c_l held fixed at 5.5753626, and its density
    satisfies c_l = (1 + psi_xy(0))/3 with psi computed from it by the canonical inverse (to 3.2e-9). The value
    5.5753626 was selected by rules that compare residual maxima of fits (4.3); the equation does not single it out. Its
    equal-budget free control has c_l = 5.5763712 and is reported next to it. The residual tests do not select a value
    inside an interval containing [5.5524653, 5.5793640] (fixed-c_l fits on the candidate's radial basis with angular
    cap m <= 150, at one iteration budget, 4.3). On that basis, and continued to the candidate's angular cap m <= 200
    (4.3), the tested value 5.6004662 is excluded at the attained level; no value between 5.5793640 and 5.6004662, and
    none above 5.6004662, was tested on that basis, so the largest tested value not excluded is 5.5793640 and the
    smallest tested value above it, 5.6004662, is excluded. At the lower end, the L2 objective, and the whole-box N_f on
    both configurations, at the lowest tested value 5.5524653 are above those at 5.5604082, so the lower end is
    bracketed at this budget (these quantities stop decreasing toward smaller c_l) in the sense of fits from
    transplanted starts (4.3: that fit had not flattened, and its residual maxima are above those of the free reference
    fit F2 while its L2 objective is below), not by a minimum of an objective over c_l. Continued for a further 21500
    iterations at their exponents, the fits at 5.5524653 and 5.5604082 keep that order in the whole-box N_f and in the
    L2 objective, the latter by 0.5 percent, a margin that shrank at every linearization (4.3). The value 5.5524653 is
    not excluded and no smaller value was tested, so the interval of values not excluded has no measured lower end. The
    six-digit values label computed fits; they are not digits of an exact exponent.

Follow-up on the strong setting P_inf (section 6, summarized in the status note at the top): T0 = 2026-10-20T00:46:19Z,
T_end = 2026-10-21T00:57:29Z, elapsed time 24 h 11 min 10 s (24.19 hours), a recorded elapsed span exceeding 24 hours, not an independent verification of active research time; the report's content is that
of its cutoff 2026-10-21T00:00:37Z (6.0). Neither endpoint has been reached for P_inf. Proved, under the hypotheses
stated in 6.3.1: a profile of P_inf has B_3(c_l, w) = 0, with B_3 the finite-part functional of 6.3.1 (a), if in
addition its third transverse trace d_y^3 rho(x, 0) stays bounded as x -> x*^-, or rho is C^(2,alpha) near P with
alpha > 1 - 2/A (A = 2c_l - 1), or a cone form of that Hoelder hypothesis holds; for 1 < c_l <= 3/2 the Hoelder
hypothesis is part of the class, so there every profile of P_inf has B_3 = 0 (whether profiles of P_inf exist in that
range is not decided either). Analogous necessary conditions hold at the higher odd orders under higher regularity at P
(at resonant orders a logarithmic compatibility condition instead; 6.3.1 (h)). These are necessary conditions, not a NO
theorem: a profile of P_inf with B_3(c_l, w) != 0 is excluded by these results only when one of these additional
hypotheses holds at P, and whether such profiles exist for c_l > 3/2 is open. The third-, fifth- and seventh-order
conditions exclude the whole two-parameter family of compatible axis data of R12 (A > 1, L > 0) for profiles of P_inf
that are in addition C^(6,alpha) near P for some 0 < alpha < 1 (6.5); this concerns one explicit family of axis data. On
a left cone at P the coupled equations leave any finite number of source amplitudes free (6.3.1 (r)); these cone
solutions are not profiles and give no family of profiles of P_inf. Trial-data finite-part estimates of B_3 are 0.31 +-
0.015 natural units on the candidate (6.2; the range spans the fit degrees and windows of the follow-up and contains the
0.299 to 0.303 of (ii)) and about 0.30 on the ten stored trial traces of the first investigation (6.3.2 (d)). Whether an
exact profile exists near the computed candidate and, if so, whether it is isolated or part of a family is not decided
(6.4).

The symbols above are defined in the body: P_2 in section 1; the source point P = (x*, 0), the exponent p_3,
the coefficient B_3 and the results R7 and R10 in section 3; the fits (the candidate X3, its control F3, the free
fit F2), the rule of 4.3 and the length unit L in section 4.
Sections: 0 timing and environment; 1 problem; 2 admissible class and velocity law; 3 rigorous results;
4 main deliverable (the statement above with its evidence); 5 reproducibility; 6 the strong setting P_inf
(follow-up investigation); appendix: verification timeline.

## 0. Timeline and environment
- T0 = 2026-10-17T17:37:12Z (start of the investigation).
- T_end = 2026-10-19T12:04:44Z. Elapsed time T_end - T0 = 42.46 hours (42 h 27 min 32 s), a recorded elapsed span exceeding 24 hours; elapsed time alone does not verify the required active research time.
- The independent verifier's final confirmation (11:59 in the appendix) covers this report as of 2026-10-19T11:50:47Z
  and the accompanying artifacts of that time. After it, for publication, only the following changed: the end time
  and the elapsed time, the wording of the status line, the description of the accompanying artifacts in section 5,
  the wording of six earlier appendix entries that referred to earlier versions of the report, and the last two
  appendix entries (12:04). No number of sections 1 to 4 changed.
- The work ran in 8 consecutive sessions of at most six hours between T0 and T_end, with long fits continuing between
  sessions; no time outside that interval is counted.
- Environment: shared Linux x86_64 machine (Intel Xeon Platinum 8275CL; every CPU process single-threaded), Python
  3.9.25 with numpy 2.0.2, scipy 1.13.1 and sympy 1.14.0; one NVIDIA A100-SXM4-80GB GPU, used by the numerical
  workstream through PyTorch 2.8.0 (CUDA 12.8) for the matrix-vector products inside LSQR of the long fits, with the
  LSQR vector updates and the column-scaling probes (5 (b)).
- Organization: a lead researcher (analysis, specification, this report), a numerical researcher (solver), and an independent
  verifier (separately written residual evaluators and audits of all analytic steps). External referee audits were obtained
  for the analytic claims.
- The verification timeline (UTC) is in the appendix at the end of this report.

## 1. Problem
Find rho on R^2 and a real c_l with
   (c_l X + U).grad rho = rho,   U = (-psi_y, psi_x),   -Laplace psi = d_x rho   on R^2,
rho(-x,y) = rho(x,y), rho(x,-y) = -rho(x,y), psi odd in x and in y, rho = x^2 y a(x,y) near 0 with a even in x and y and a(0) = 1,
and c_l = (1 + psi_xy(0))/3.
Two variants are distinguished throughout. Both require rho in C^{2,alpha}_loc(R^2) for some alpha in (0,1), the velocity
law of section 2 and the growth condition (A3). This global regularity is the report's choice of admissible class of
classical profiles: the prompt states the regularity of a near the center only.
- P_inf (the strong setting of the prompt): in addition, a is C^infinity near 0.
- P_2 (a weaker problem, stated explicitly; the prompt allows a weaker condition at the center only if the resulting
  problem is explicitly distinguished): in addition, rho = x^2 y a near 0 with a continuous, even in x and in y, a(0) = 1.
  Only continuity of a is required (a smooth a is allowed). With the common global regularity, P_inf is contained in P_2,
  so numerical evidence for P_2 does not by itself answer the stated problem P_inf. P_2 implies rho = x^2 y + o(|X|^3),
  and the factorization is a strictly stronger local condition than this jet condition (rho = x^2 y + y^5 satisfies the
  jet condition but is not of the form x^2 y a with a continuous; this compares local conditions, not sets of exact
  profiles).
  More generally P_m (m >= 2) denotes the same problem with C^{m,alpha} in place of C^{2,alpha}; sections 2 and 3 are
  stated for general m.

## 2. Admissible class and velocity law
Class A_m (m >= 2 or m = infinity):
- (A1) rho is in C^{m,alpha}_loc(R^2), real, even in x and odd in y.
- (A2) rho = x^2 y a near 0 as above.
- (A3) |rho(X)| + (1+|X|)|grad rho(X)| <= C(1+|X|)^gamma for some gamma < 1.
- (A4) U is given by the canonical law below, and the profile equation holds pointwise.
The canonical velocity law has three equivalent descriptions.
- (V1) Modal Green function. Write d_x rho = sum_{n>=1} f_n(r) sin(2n theta). Then psi = sum psi_n(r) sin(2n theta) with
  psi_n(r) = (1/(4n)) [ r^{-2n} int_0^r s^{2n+1} f_n ds + r^{2n} int_r^inf s^{1-2n} f_n ds ].
- (V2) Symmetric truncation of the singular integral U = lim_{R->inf} [ -rho/2 e_2 + PV int_{|Y|<R} K(X-Y) rho(Y) dY ], with
  K = (K1, K2), K1(Z) = -(1/pi) z1 z2/|Z|^4, K2(Z) = (1/(2pi))(z1^2 - z2^2)/|Z|^4.
- (V3) U is the unique field with div U = 0, curl U = -d_x rho, the stated parities and |U(X)| = o(|X|).
Gauge. The harmonic term lambda x y in psi adds the linearly growing field lambda(-x, y). (V3) excludes it, so psi_xy(0) is a
functional of rho. Under (A2),
   c := psi_xy(0) = int_0^inf rho_1(r) r^{-2} dr = (1/pi) int rho sin(3 theta) r^{-3} dX,
where rho_1 is the sin(3 theta) coefficient of rho.

## 3. Rigorous results (checked by the verifier and by an external referee)
Each item below was rederived by the independent verifier and audited by an external referee; conditions found in those
audits are part of the statements.
R1 (velocity law). For rho with (A1) and (A3), the three descriptions (V1), (V2) and (V3) agree; for
   0 < gamma < 1 (the range in force in R2), |U(X)| <= C(1+|X|)^gamma.
R2 (forced regime). Every nonzero profile in A_m (m >= 2) has 0 < gamma < 1 and c_l >= 1/gamma > 1. Along an escaping
   characteristic with rho(X0) != 0, e^{-c_l s} X(s) converges to a nonzero vector, and |rho(X)| <= C(1+|X|)^{1/c_l} uniformly.
   In particular there is no nonzero profile in the class with c_l <= 1.
R3 (center). 3c_l - c = 1. The origin is a saddle of W = c_l X + U with eigenvalues 1 - 2c_l < 0 (x-axis) and 4c_l - 1 > 0
   (y-axis).
R4 (no cycles). div W = 2c_l > 0, so W has no periodic orbit and no graphic bounding a region. If the zero set of W is finite,
   every backward orbit converges to a zero of W, and the indices of the zeros sum to +1.
R5 (source on the x-axis). Let x* be the first positive zero of w(x) = W_1(x,0). For every A_2 profile, d_x W_1(x*,0) = 2c_l - 1,
   d_y W_2(x*,0) = 1 and rho_y(x*,0) > 0. So P = (x*,0) is a hyperbolic source and psi_xy(P) = 1 - c_l.
R6 (fixed-field rigidity). Write W_2 = y b. On the basin of P in the upper half plane, every C^1 solution of W.grad rho = rho
   vanishing on the x-axis equals rho_y(P) y exp(-int_{-inf}^0 [b(Phi_t X) - 1] dt). This is rigidity for a fixed field W. It is
   not uniqueness of the coupled profile.
R7 (regularity at the center). For A_3 profiles (or C^3 axis data), G_3(x) = d_y^3 rho(x,0)/6 solves a first-order
   linear ODE with a regular singular point at 0 and exponent p_3 = 6 + 2/(2c_l - 1), which lies in (6,8) and is never
   an even integer. If rho is C^infinity near 0, the coefficient B_3 of the homogeneous solution |x|^{p_3} e^{E(x)} in
   G_3 vanishes. The same holds for infinitely many higher odd j. The 2D statement that B_3 != 0 limits rho to C^6 or C^7
   is not proved.
R8 (weighted identities). For phi homogeneous of degree -d with 1/c_l + 2 < d < 5,
   (1 + (2 - d)c_l) int rho phi dX + int rho U.grad(phi) dX = 0.
   For phi = sin(3 theta) r^{-3}: int rho U.grad(phi) dX = pi (c_l - 1)(3c_l - 1).
R9 (positivity). Let rho be in A_2 and assume (Hmin): the zeros of W in the closed first quadrant are exactly 0 and P, and
   W_2(0,y) > 0 for y > 0. Then rho > 0 in the open first quadrant Q, rho(0,y) = 0 and k(y) = d_x^2 rho(0,y)/2 > 0 for all
   y > 0. (On the invariant y-axis, k(y_t) J(t)^2 = e^t k(y_0) with J(t) = exp int_0^t d_x W_1(0,y_s) ds, and k(y) = y a(0,y)
   > 0 near 0.) Positivity holds in Q, not in the whole upper half plane.
R10 (axis constraints and B_3 from the axis). Write w = W_1(x,0), h = d_y W_2(x,0), a2 = d_y^2 W_1(x,0)/2,
   b3 = d_y^3 W_2(x,0)/6, g = rho_y(x,0), A = 2c_l - 1, beta = 2/A, g0 = a(0) = 1.
   - For every A_2 profile: w' + h = 2c_l, h' - 2 a2 = -g', hence a2 = (g' - w'')/2; w g' = (1 - h) g, equivalently
     (w/g)' = A/g; |w(x)|/g(x) = A int_x^{x*} dt/g(t) on (0, x*]; and int_0^{x*} (1/g - 1/(g0 x^2)) dx = 1/(g0 x*).
   - For A_3 profiles (or C^3 axis data) also a2' + 3 b3 = 0, and the homogeneous solution of the G_3 equation is
     H = N g^{3+beta} |w|^{-beta}, N = A^beta / g0^{3+beta}, with H ~ x^{p_3} at 0, and
       B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^{beta - 1} dx,   m = |w|/g.
     So B_3 is determined by c_l and the single function w on [0, x*]. The finite part requires the even integrand factor to
     have an expansion k0 + k2 x^2 + k4 x^4 + O(x^6) at 0 (smooth axis data suffice; C^4 alone does not). At c_l = 3/2
     the integrand is a derivative and B_3 = a2(P)/(6 g(P)^3) = w''(P)(g(P) - 2)/(24 g(P)^3).
R11 (the limit c_l -> infinity is degenerate). The problem (X + U[F]).grad F = 0, F even in x and odd in y,
   psi_xy[F](0) = 3, has no solution with F in C^1, U[F] in C^1, U[F](X) = o(|X|) and finitely many zeros of X + U[F].
   (div(X + U) = 2, so there is no invariant Jordan curve; every alpha-limit set contains an equilibrium, F is constant on
   orbits, so F takes finitely many values and is 0 by oddness.) With F = rho/c_l, profiles with c_l -> infinity can only
   converge to a solution F of this problem, which the statement excludes when the limit field X + U[F] has finitely
   many zeros. This conclusion needs C^{1,alpha}_loc convergence and uniformly small far-field tails
   (sup_n int_{|Y|>R} |F_n|/|Y|^3 dY -> 0); without the tail condition it fails (F_n = R_n f(X/R_n)).
R12 (no local sign for B_3). The axis constraints of R10 do not determine the sign of B_3: for every A > 1 the compatible
   axis data w = -A x (1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L give B_3 = C_A L^{-4-2/A} (1 - S_A/L^2) with C_A > 0 and
   S_A = 6A(4A-3)/(8A-1), so B_3 takes both signs and the value 0. These are compatible axis data, not coupled profiles.

## 4. Main deliverable

YES, strong numerical evidence, for the explicitly distinguished problem P_2 (section 1: P_m with m = 2).

(i) The posed strong setting (a smooth and even near 0) is not answered by this result.
(ii) On the computed trial family the B_3 estimator is about 0.30 natural units x*^(2 - p_3): B_3 = 0.299 to 0.303 on
    the candidate (medians over the evaluation configurations of the two forms of the independent evaluator's estimator
    and of the original form of R10; variant extremes 0.291 to 0.311), 0.298 to 0.303 on its control, positive in every
    variant; in either form it changes by less than 0.005 along the angular refinement m <= 100 to m <= 250, under a
    further 20750 iterations and with fit rows to 9000 L (4.1). The trial's own coefficient of y^3 |x|^(p_3) is +0.046
    in the same units (positive; the difference is carried by the trial's defects in the y and y^3 coefficients of the
    equation on the x-axis, 4.1). A C^infinity profile has B_3 = 0 (R7, proved). If an exact profile exists near the
    trials and has a well-defined nonzero B_3, it is not C^infinity near 0 and does not solve the strong setting. The
    estimator value is numerical evidence for this; no estimate transfers it to an exact profile, so it is not proved.
    [Follow-up correction (2026-10-20): here B_3 is the coefficient of the homogeneous solution in R7, while the
    estimator measures the finite-part functional of R10; the two agree when l_3 = 0, for instance for A_3 profiles.
    When the finite-part hypotheses of 6.3.1 (a) hold and the limit l_3 exists, the coefficient equals l_3 plus the
    functional, so a nonzero value of the functional excludes a smooth centre only if l_3 = 0 or the cancellation of the
    two is otherwise excluded; neither the trial estimates nor proximity to the trials establishes this for a nearby
    exact profile (status note at the beginning; 6.3.1 (a), (g)).] It is not a NO theorem, and other branches are not
    excluded.
(iii) The class is stated only as far as proved: P_2 requires rho in C^(2,alpha)_loc and a continuous with a(0) = 1. No
    higher regularity of an exact profile is claimed. The trial satisfies the regularity, parity, normalization and
    growth requirements of P_2; its transport residual is nonzero, so it is an admissible trial density, not a member of
    P_2. The numerical claim is the one of 4.1 (evidence consistent with the existence of an exact profile of P_2 near
    the trial; neither the proximity nor the exponent is established); it is not a proved statement. Uniqueness within
    P_2 is not claimed, and other branches are not excluded.
(iv) The computation does not determine c_l: the tested exponents that the rule of 4.3 does not exclude on the
    candidate's radial basis with angular cap m <= 150 span [5.5524653, 5.5793640] (an observed span, not an enclosure
    of the exponent of an exact profile). The candidate is computed with c_l held fixed at 5.5753626, and its density
    satisfies c_l = (1 + psi_xy(0))/3 with psi computed from it by the canonical inverse (to 3.2e-9). The value
    5.5753626 was selected by rules that compare residual maxima of fits (4.3); the equation does not single it out. Its
    equal-budget free control has c_l = 5.5763712 and is reported next to it. The residual tests do not select a value
    inside an interval containing [5.5524653, 5.5793640] (fixed-c_l fits on the candidate's radial basis with angular
    cap m <= 150, at one iteration budget, 4.3). On that basis, and continued to the candidate's angular cap m <= 200
    (4.3), the tested value 5.6004662 is excluded at the attained level; no value between 5.5793640 and 5.6004662, and
    none above 5.6004662, was tested on that basis, so the largest tested value not excluded is 5.5793640 and the
    smallest tested value above it, 5.6004662, is excluded. At the lower end, the L2 objective, and the whole-box N_f on
    both configurations, at the lowest tested value 5.5524653 are above those at 5.5604082, so the lower end is
    bracketed at this budget (these quantities stop decreasing toward smaller c_l) in the sense of fits from
    transplanted starts (4.3: that fit had not flattened, and its residual maxima are above those of the free reference
    fit F2 while its L2 objective is below), not by a minimum of an objective over c_l. Continued for a further 21500
    iterations at their exponents, the fits at 5.5524653 and 5.5604082 keep that order in the whole-box N_f and in the
    L2 objective, the latter by 0.5 percent, a margin that shrank at every linearization (4.3). The value 5.5524653 is
    not excluded and no smaller value was tested, so the interval of values not excluded has no measured lower end. The
    six-digit values label computed fits; they are not digits of an exact exponent.

Fits named in this section (all on the formula of 4.2 with 375 radial spline coefficients per angular mode; LSQR
iterations are inner iterations of the Gauss-Newton solver of 4.2):
  F0   free fit, angular cap m <= 150 (c_l from the identity during the fit).
  X1   F0 moved along its softest exponent direction by -1e-3 in c_l, refitted with c_l held at 5.5753626,
       750 LSQR iterations.
  F1   F0 continued with c_l free for the same 750 iterations (equal-budget free control of X1).
  F1r  X1 continued with c_l free for 1000 iterations.
  W1   X1 continued with extra weight on the x-axis between the origin and P (failed variant).
  X2   X1 continued with c_l held fixed for 20750 further LSQR iterations.
  F2   F1 continued with c_l free for the same 20750 iterations (equal-budget free control of X2).
  X3   X2 enriched to angular cap m <= 200 (the added coefficients start at zero) and continued with c_l fixed for 20750
       iterations on a 20480 x 960 grid.
  F3   F2 enriched to m <= 200 and continued with c_l free for the same 20750 iterations (equal-budget free control
       of X3).
The candidate is X3. Below, "the candidate" means X3 and "its control" means F3.
Conventions. Radii written n L are multiples of the length scale L of the trial formula (4.2; L = 7.6514246 on the
candidate, and each fit has its own L); the shape units of the timeline are the same unit. N_f and N_v are the two
normalizations of the residual (4.4). The verifier's evaluator, also called the separate or the independent evaluator,
is the separately written generator and residual evaluator of 5 (d); the third evaluator is the real-space quadrature of
the velocity of 4.5 (5 (e)); the lead's evaluator is the between-node scan of 5 (c). J is the characteristic defect of
4.4b (its spread over the 857 labels of 4.4b unless stated otherwise), and q0 and I(eps) are its axis profile and axis
integral (4.4b). "The standard" is the evidential standard for YES agreed with the verifier before any candidate
existed: normalized residual maxima between the fit nodes near 1e-6 in both normalizations, including next to P, on both
axes and at 0, recomputed by the verifier's own code; at least three resolutions and three domains, with systematic
improvement under refinement; c_l, x* and h(P) stable, with c_l checked by the identity and by one determination not
using it; far-field truncation and inverse errors quantified separately; J reported and decreasing under refinement.
Absolute values are reported too.

The objective (L2 objective) of a fit is the Euclidean norm of its weighted residual vector on its fit grid: the entries
R/(|rho| + |X.grad rho|) at the grid nodes with 1e-4 L <= r < 900 L (the fit radius; 90 L, 300 L or 9000 L for the
domain columns of 4.4) on every second angle of the grid, each multiplied by (14000/n)^(1/2) max(1, (0.04 L/r)^2), n the
number of these entries, together with 20 (h(P) - 1) and the centre defects E_c and D2 of 4.2 with weight 1. It is a
norm, not a mean square, and its value depends on the fit grid. E without index is the elliptic residual of 4.4.

### 4.1 What is claimed
- There is an explicit trial density rho_h (4.2) and the number c_l = 5.5753626 such that, with the canonical velocity
  law (V1)-(V3), the profile equation holds to a normalized residual of at most 7.2e-7 in the flux normalization N_f
  (6.83e-7 to 7.16e-7 over the three finer configurations of the verifier's evaluator; maximum next to P, 0.07 to the
  left of it and 0.06 to 0.07 above the x-axis) and 1.112e-6 in the second normalization N_v (maximum in the far field
  beyond the inverse domain, next to the y-axis at r about 3.7e4, where the candidate has no fit rows; a domain row
  fitted to 9000 L reads 0.03 of it over 1000 L to 9000 L, 4.5; for r <= 1000 at most 2.01e-7 with the evaluation
  columns next to the y-axis excluded and 2.5e-7 at 16875 x 768 without that exclusion), both defined in 4.4, at the
  sampled points of the plane between the fit nodes, including the neighbourhood of the source point P. The lead's scans
  of 5 (c) read the trial in its fit's own convention (the two-term closure at 1000 L, 4.4); next to P they give 6.94e-7
  and 7.27e-7 in N_f and 1.94e-7 and 2.04e-7 in N_v (32768 x 640 and 24576 x 960), and in that convention the verifier's
  evaluator reads 1 percent above its canonical value there. At the same c_l the residual decreases under refinement of
  the angular cap of the trial space in each quantity of the reading fixed before the runs (4.4: m <= 100, 150, 200; at
  the last step the N_v maximum beyond r = 1000 by about the configuration spread). The rows are not at equal total
  iterations (X3 continues X2 by 20750 iterations, and the m <= 250 row continues X3 by 20750); comparisons at equal
  iterations are in the third item of 4.1 and in 4.4 and 4.8. The m <= 250 refinement row, which is not a candidate,
  meets the same reading on all evaluation columns; with the evaluation columns next to the y-axis excluded it is 0.33
  to 0.74 times X3 in the interior maxima and 0.36 to 0.37 in J, and 0.23 to 0.44 percent above X3 beyond r = 1000, more
  than the spread between configurations (4.4). Fits on two smaller domains and on one with rows to 9000 L are compared
  with the candidate by a rule fixed before the runs (4.4: all three agree except at one configuration, where each is
  lower by more than the rule's factor; none is higher by more than that factor). Read under the canonical law (the
  formula continued, no closure) at equal budget, the fits with rows to 300 L, 900 L and 9000 L agree within 0.5 of P to
  a factor 1.4, and their far band follows the extent of their rows and inverse domains (4.4, 4.5); the 90 L fit is not
  an approximate full-plane profile in that reading (4.4). A separately written evaluator reproduces the residuals, and
  a third evaluator reproduces the velocity at sample points on X1, on a free fit of a smaller basis and on X3 (52, 51
  and 52 points; 4.5). The pair satisfies the identity c_l = (1 + psi_xy(0))/3 to 3.2e-9, and the consistency condition
  h(P) = 1 to the evaluator's grid error (|h(P) - 1| = 2.8e-7, 3.1e-8 and 1.8e-8 at 11250, 16875 and 22500 radial
  points). These results are numerical evidence consistent with the existence of an exact profile of P_2 near rho_h.
  They do not establish the proximity of an exact profile or determine its exponent: if such a profile exists and is
  isolated (4.8), its exponent may lie outside the tested span of (iv). It is not a proof.
- The free control at the same LSQR budget, from the free start, has c_l = 5.5763712. On X3 against F3 the candidate is
  lower in whole-box N_f on every configuration (ratio 0.937, 0.935 and 0.938 at 16875 x 512, 16875 x 768 and 22500 x
  512 with the y-axis floor columns excluded; 0.83 at 16875 x 768 without that exclusion, where F3's maximum sits in the
  floor column at r 9.5; next to P 0.935 to 0.938 on all four configurations), lower in N_v for r <= 1000 (ratio 0.935
  to 0.987 with the same floor columns excluded; 0.825 at 16875 x 768 without that exclusion), lower in the 857-label
  characteristic defect J (ratio 0.937 at eps 0.03 and 0.01), and lower in the L2 objective on the fit grid (1.619e-6
  against 1.664e-6, a ratio between 0.960 and 0.973 at every check point of the two runs). In the far field beyond r
  1000 the two agree to 3e-9 (ratio 1.000 to 1.003, the candidate the higher), inside the spread of 2.4e-8 of F3's
  values between configurations; with the y-axis floor columns excluded the candidate is the higher by 4.5e-9 (0.4
  percent) on each configuration with 16875 or more radial points, about twice the spread between those configurations
  (the same offset in favour of the free c_l as in the m <= 250 pair of 4.4). The ratios X3 / F3 are thus 0.935 to 0.938
  in whole-box N_f, 0.937 in J, 0.935 to 0.987 in N_v for r <= 1000, 0.960 to 0.973 in the L2 objective and 1.000 to
  1.003 in the far field, where there is no margin. They are read at one budget and one basis; they are what the
  selection rule reads, not a determination of c_l.
- Raising the angular cap from 150 to 200 at the fixed c_l, with 20750 further iterations, lowered whole-box N_f by
  0.475 to 0.485 (X2: 1.42e-6 to 1.51e-6), N_v for r <= 1000 by 0.48 and J by 0.44; N_v on the outer part of the inverse
  domain (1000 <= r <= 7652, that is 1000 L) by 0.86 only (2.152e-7 against 2.513e-7); the near-P window y >= 1 of 4.4
  changed by the ratios 1.01 (11250 x 384, the under-resolved lobe of 4.3) and 0.81 (16875 x 512); beyond r 1000 L the
  formula's far field reads 1 to 2 percent lower. At equal budget (one linearization of 2500 iterations from X2 on each
  basis) the m <= 200 iterate is 0.71 to 0.72 times the m <= 150 iterate in N_f and 0.62 to 0.69 in J on 185 labels
  (every fourth label of family A of 4.4b); the m <= 150 iterate is 0.999 times X2 in N_f. The two equal-budget runs
  also differ in the number of collocation angles (960 against 720), so the gain is attributed to the m <= 200 setup
  (basis and grid together).
- The candidate is not the fit with the lowest whole-box N_f at every configuration. Rows continued beyond its budget
  are lower in whole-box N_f (columns within 0.006 of the y-axis excluded, as in 4.4) at the configurations read with at
  least 16875 radial points: the budget row and X3 continued with the inverse domain at 1e4 L (4.2, 4.5), the m <= 250
  row, its free control and its continuation with rows to 9000 L (4.4), and the 9000 L row, its free control and its
  continuation (4.4, 4.5); none of these is an equal-budget comparison. X1, the fixed-c_l fit before the long
  continuation, has its maximum next to P 4 to 6 percent below the candidate's at 16875 radial points (6.53e-7 against
  6.84e-7 at 512 angles, 6.70e-7 against 7.16e-7 at 768 angles), equal to it at 22500 x 512 and 2 percent above it at
  11250 x 384; its N_v for r <= 1000 is 2.8 times and its 857-label J twice the candidate's (2.74e-6 against 1.39e-6),
  and it fails the selection rule against its own equal-budget free control on J. All fits compared are listed in 4.3.
  The fixed-c_l fit at 5.5683739 (4.3), not a candidate by the rule fixed before that profile, has whole-box N_f 0.984
  times the candidate's and N_f within 0.5 of P 0.977 times at 16875 x 512, N_v for r <= 1000 1.038 times, and J (at
  16875 x 384) 0.954 (eps 0.03) and 0.882 (eps 0.01) times; at 11250 x 384 its whole-box maximum is 1.289 times the
  candidate's (both at the under-resolved off-axis lobe; within 0.5 of P 1.005 times). The bases differ, so this is a
  fact about two fits. On the candidate's basis, at the candidate's iteration count (the nested pair of 4.3), the fit at
  5.5683739 has a smaller L2 objective (0.820 times the candidate's), a smaller N_f within 0.5 of P (0.591 and 0.588
  times at 11250 x 384 and 16875 x 512) and a smaller J (0.562 at eps 0.03, 0.545 at eps 0.01) than the candidate; its
  whole-box N_f is 1.322 times the candidate's at 11250 x 384, at the off-axis lobe point that grid under-resolves, and
  0.691 times at 16875 x 512. The fixed-c_l fit at 5.5604082 on the m <= 150 basis continued to 43000 iterations (4.3),
  not a candidate, has whole-box N_f 0.922 times the candidate's at 16875 x 512 (at the off-axis lobe), N_f within 0.5
  of P 0.750 times, N_v for r <= 1000 0.924 times, and J (at 16875 x 384) 0.800 (eps 0.03) and 0.774 (eps 0.01) times;
  at 11250 x 384 its whole-box maximum is 1.689 times the candidate's, at the under-resolved off-axis lobe (within 0.5
  of P 0.823 times). It is not an equal-budget comparison. The residual does not distinguish the candidate's exponent or
  basis among the fits computed.
- The evidence concerns P_2. With the common global regularity of section 1, P_inf is contained in P_2, so numerical
  evidence for P_2 does not by itself establish a profile of P_inf (nor does it show that an exact profile near the
  trial fails to be in P_inf; (ii) gives numerical evidence on that, not a proof). Every trial satisfies the
  requirements of P_2 other than the equation: rho = x^2 y exp(H) with H(0) = 0. The integer angular spline terms of H
  are C^(6,1)_loc on the plane (polynomial degree 7 with simple interior knots) and analytic near 0 within the first
  knot interval (4.2). The fractional-power term is |x|^(p_3 - 2) y^2 (L^2 + r^2)^(-p_3/2) T(2q - 1) in Cartesian form.
  It makes H and a exactly C^(4,beta)_loc, with beta = p_3 - 6 = 2/(2 c_l - 1) = 0.19703 on the candidate, and the
  factor x^2 y makes rho_h exactly C^(6,beta)_loc (the least regular term of rho_h is |x|^(p_3) times a smooth factor;
  exact because T is not identically zero).
- Remark (structure, not part of the class). R7 and R10 identify, under their differentiability and finite-part
  hypotheses, a possible fractional homogeneous contribution B_3 |x|^(p_3) (times a smooth factor) to the axis
  coefficient G_3 = d_y^3 rho(x,0)/6, with B_3 an exact functional of the axis velocity w on [0, x*] (R10). No
  two-dimensional expansion of a is asserted. Evaluated on the computed trials by the original form of R10 and by the
  two forms of the independent evaluator's estimator, B_3 = 0.299 to 0.303 on the candidate (medians over the four
  evaluation configurations; the original form of R10 gives median 0.3027, range 0.3010 to 0.3040 over 16 quadrature and
  fit-window variants; the extremes over all variants of the three forms are 0.291 and 0.311) and 0.298 to 0.303 on its
  control. On the angular row of 4.4 (m <= 100, 150, 200, 250 on 375 radial functions), on X3 continued for a further
  20750 iterations and on the domain row with fit rows to 9000 L, the medians of the independent evaluator's
  integration-by-parts form are 0.2985, 0.2992, 0.2996, 0.3012, 0.3000 and 0.2998 and those of its original form
  0.3002, 0.3021, 0.3029, 0.3044, 0.3037 and 0.3032 (method spread within one row up to 0.0035 and 0.015); along the
  angular row each step is within the method spread. Over 136 evaluations of earlier fits by the independent evaluator,
  with c_l from 5.5752 to 5.6001, radial bases from 200 to 375 functions and angular caps 100 to 200, the medians of its
  integration-by-parts form lie between 0.296 and 0.302 and those of the original form of R10 between 0.277 and 0.311;
  every variant is positive (smallest single value 0.151). On earlier fits the value is unchanged when the trial's
  fractional-power functions are switched off and when the centre jet is repaired. A further form, an integration by
  parts with an end piece in closed form, is not quoted: its end piece does not converge in the quadrature order. The
  sign of dB_3/dc_l is not resolved by these values.
  The trial's own coefficient is a second measurement. The fractional-power term of 4.2 contributes
  T(-1) L^(-p_3) y^3 |x|^(p_3) to rho_h at the origin (T(-1) the value of its Chebyshev factor at q = 0), with T(-1) =
  1.6487 to 1.6488 on the candidate, on X2 and on the rows of 4.4 built from them (1.6485 on F3 and on the free control
  of the m <= 250 row): 5.50e-6, or +0.046 in the natural units above. For a trial, the original form of R10 evaluated
  on its axis data equals its own coefficient plus the finite part of int_0^{x*} (T_3 - (3 + beta) (G_3/g) T_1)/(w H)
  dx, with H as in R10 and T_1 = w g' + (h - 1) g, T_3 = w G_3' + (3h - 1) G_3 + a2 g' + b3 g the trial's defects in the
  y and y^3 coefficients of the equation on the x-axis (variation of constants in the G_3 equation; w' + h = 2c_l and
  a2' + 3 b3 = 0 hold for every trial since div U = 0; the finite-part step uses g > 0 on (0, x*] and even expansions
  of g/x^2 and |w|/x at 0, which these trials have; for a profile T_1 = T_3 = 0 and H is the homogeneous solution).
  So the difference, about +0.25, is carried by these defect terms; both measurements are positive. This is an estimator
  value on approximate profiles; B_3 of an exact profile is indicated, not proved.

### 4.2 Candidate
The trial density is given by an explicit formula with stored coefficients (accompanying artifacts). With u = r/L,
q = 1 - (1 + u^2)^(-(1-k)/2) and chi = u^2/(u^2 + r_0^2), r_0 = 0.02,
   rho_h = x^2 y exp(H),
   H = ((k - 3)/2) log(1 + u^2) + sum_{m=0}^{M} chi^max(m-1,0) b_m(q) cos(2 m theta)
       + (u^2/(1 + u^2))^(p_3/2) |cos(theta)|^(p_3 - 2) sin(theta)^2 T(2q - 1),
with M = 200, where b_m are clamped splines of polynomial degree 7 in q on [0, 1] with b_m(0) = 0 (375 coefficients
each; simple interior knots, spacing 0.0165 in r next to P, 6.3e-4 in q), T is a Chebyshev polynomial of degree 5,
p_3 = 6 + 2/(2 c_l - 1), and k = 1/c_l. Hence H(0) = 0, so a(0) = 1 exactly; rho_h is even in x and odd in y by
construction, so its psi under the canonical inverse is odd in x and in y, and U_1 = 0 on the y-axis, U_2 = 0 on the
x-axis and U(0) = 0 by these parities; each angular term is analytic near 0, within the first knot interval, because
there b_m(q(u^2))/u^2 is analytic in u^2 and r^(2m) cos(2 m theta) is a polynomial.
  - c_l = 5.5753626 (held fixed during the fit; 5.575362610641546 to all stored digits); k = 0.17936053; L = 7.6514246.
  - Far field. Since b_m is a polynomial near q = 1 and 1 - q = (1 + u^2)^(-(1-k)/2),
      rho_h = r^k Theta_0(theta) (1 + r^(k-1) Theta_1(theta) + O(r^(2k-2))),
    Theta_0(theta) = L^(3-k) cos(theta)^2 sin(theta) exp(sum_m b_m(1) cos(2 m theta) + T(1) sin(theta)^2
    |cos(theta)|^(p_3-2)), and Theta_1(theta) = -L^(1-k) (sum_m b_m'(1) cos(2 m theta) + 2 T'(1) sin(theta)^2
    |cos(theta)|^(p_3-2)) (b_m' with respect to q, T' with respect to its argument). The bracket extends continuously
    across the axes and the remainder is O(r^(2k-2)) uniformly in theta (the O(r^(-2)) terms from chi, (1 +
    u^2)^((k-3)/2) and (u^2/(1 + u^2))^(p_3/2) are smaller, since 2k - 2 = -1.64 > -2). The leading term is homogeneous
    of degree 1/c_l, the largest growth that the bound |rho| <= C (1 + |X|)^(1/c_l) of R2 allows, and the first
    correction is relative r^(k-1). This is the far-field model. The fit's residual rows are r < 900 L; its own inverse
    is computed on the inverse domain r <= 1000 L with the density replaced beyond it by its two-term exterior extension
    (the two-term closure); the residual at larger r is evaluated from the formula (4.5). In q the last interior knot of
    the radial splines is at r = 446 L, so on r > 446 L each b_m is one polynomial of degree 7 in q; the fit rows cover
    the first 44 percent of that knot interval in q, and the formula beyond 900 L (in particular the far-field band of
    4.5, at 86 percent of the interval) is the unfitted continuation of that polynomial, with b_m(1) and b_m'(1) its
    values at the end.
  - Source point: x* = 8.600064 (lead 8.6000638; independent evaluator's zero of W_1 on the x-axis 8.6000635). h(P) - 1
    is at the evaluator's grid error (2.84e-7, 3.11e-8 and -1.78e-8 at 11250, 16875 and 22500 radial points; lead
    evaluation -8.8e-9 / -5.3e-9 on its two grids). On the evaluation grid there is no further zero of W in the closed
    first quadrant: W_1 on the x-axis vanishes only at x*, W_2/y on the y-axis is at least 5.5756 (attained at y 7.5e6,
    where it tends to c_l), and no cell of the open quadrant has both components changing sign (a sampled check, not a
    validated exclusion); min |W| / (c_l |X|) is 0.0216, 0.0065, 0.0026 at |X - P| = 1, 0.3, 0.1.
  - Centre jet. With a = 1 + delta x^2 + gamma y^2 + O(r^4) and psi = c x y + alpha x y^3 + beta x^3 y + O(r^6),
    the x^4 y and x^2 y^3 coefficients of W.grad rho - rho are the centre defects E_c = beta - 2 (2 c_l - 1) delta
    and D2 = (8 c_l - 2) gamma - 5 alpha, which vanish for a profile; the relative defects are E_c/|beta| and
    D2/(5 |alpha|), with delta and gamma fitted on a window of r. They are at most 6e-9 on the candidate and on
    its control for every fit window inside r <= 0.1 (independent evaluator; windows [1e-3, 0.02] to [5e-3, 0.1];
    the values depend on the window at that level); on X2 at most 8.5e-9 for windows up to r 0.05 and 1.9e-8 on
    [5e-3, 0.1].
  - How it was obtained. F0 (Gauss-Newton with LSQR inner solves on a 20480 x 720 polar grid, c_l from the identity) was
    moved along its softest exponent direction by -1e-3 in c_l and refitted with c_l held fixed (X1, 750 LSQR iterations
    over two linearizations, objective 9.71e-6 to 8.47e-6), then continued at the fixed c_l by a GPU implementation of
    the same LSQR iteration (linearizations of 2500 iterations, damping 1e-8) for 20750 iterations to X2 (objective
    4.097e-6 on the fit grid). X3 is X2 enriched to M = 200 (the new coefficients start at zero, so the start is X2
    itself), continued at the fixed c_l by the same iteration for 20750 iterations on a 20480 x 960 grid: objective
    1.619e-6 on that grid against 4.050e-6 for X2 on the same rows. The objective still fell by about 2 percent per
    linearization at the end. X3 continued at the fixed c_l on its own rows and basis for a further 20750 iterations (a
    budget row, not a candidate) reaches 1.264e-6 on the same grid (0.781 of X3's) and, at 16875 and 22500 radial points
    with the columns next to the y-axis excluded, reads 0.61 to 0.74 times X3's whole-box N_f (its maximum moves from
    next to P to the lobe above P (4.4), where it equals X3's value there to 2.4 percent over four radial sampling
    phases), 0.50 to 0.54 within 0.5 of P, 0.64 to 0.77 in N_v for r <= 1000, 0.99 to 1.01 for r > 1000 and 0.48 (eps
    0.03) and 0.45 (eps 0.01) in J; its centre values are X3's. So X3 is limited by the iteration budget, except beyond
    r = 1000. Every shape is measured by the CPU evaluators of 4.4 and 4.5, not by the GPU code. Solver setting: plain
    damping 1e-8 was kept by a rule fixed before the test (a variant replaces it only if its objective after 2500
    iterations is at least 3 percent lower and its maximum next to P is not higher); damping 1e-12 gave the same
    objective to 6 digits, and reorthogonalization gave 1.3 percent, so neither change of the solver setting lowers the
    objective materially at this budget.

### 4.3 The exponent c_l and the choice of the candidate
Identity on the candidate. The verifier computed c = psi_xy(0) from the density, generated from the formula by its own
code, by its own inverse: (1 + c)/3 = 5.575362607 on every configuration (5.5753626074 at 16875 and 22500 radial points)
against the fixed value 5.5753626106 (difference -3.2e-9). For a fit with c_l held fixed this tests the fit: c_l enters
the transport equation, and psi_xy(0) is computed from rho. Holding c_l fixed does not suspend the identity. With
a(0) = 1 fixed, the fit has to find a density, its length scale L and its shape, whose own psi_xy(0) equals 3 c_l - 1,
and the final pair satisfies the identity to 3.2e-9. What is chosen, and stated here, is the point at which the family
of consistent pairs is sampled. The prompt's condition that c_l is not chosen independently is met in the sense that c_l
and the psi_xy(0) of rho agree; the choice of the sample point is disclosed. The identity-free condition h(P) = 1 avoids
the origin identity but is not an independent test of transport near P: it is the source limit of the normalized
transport equation (4.4a), so a small normalized residual approaching P implies it. Solved for c_l with rho fixed,
h(P) = 1 gives 7.0e-9 above the identity value on X3 (dh/dc_l = 1.079) and 6.3e-8 above it on F3 (identity value
5.576371152, 3e-9 from the stored 5.576371155); on X2 / F2 4.7e-9 below and 4.2e-8 above. It holds at both values, 1e-3
apart, and does not determine c_l at that level. It is a consistency test along the soft direction.

Selection rules. (1) Of each equal-budget pair (fixed c_l against the free control from the free start, same LSQR
count), the fixed fit is kept if its whole-box N_f is lower, its N_v (for r <= 1000 and in the far field separately) is
not higher by more than the spread between the verifier's configurations, and its 857-label J is not higher; otherwise
the free fit is kept.
(2) The candidate is the kept fit with the lowest whole-box N_f, all maxima taken at the same verifier configurations.
(3) The far-field band of rule (1) is all r > 1000 on the verifier's evaluator. Rule (1) was fixed before any residual
scan of X2 or F2 (the L2 objective of X2 after 2000 iterations, 4.993e-6, was known). Rules (2) and (3) were fixed after
the X2/F2 measurements (the earlier wording of (1) did not say where the band ends) and before any residual scan of X3
or F3 (the L2 objective of X3 at iterations 250 to 1000 was known). Read over the band
1000 <= r <= 7652 (that is 1000 L) only, X2's N_v is 2.9 to 3.1 percent higher than F2's (7.2e-9 to 7.5e-9 against a
spread of 2e-10), and by that reading F2 would be kept. Both readings are given here; the outcome of the X2/F2 pair
depends on it. For X3/F3 the two readings agree (that band: X3 2.152e-7 / 2.183e-7, F3 2.157e-7 / 2.195e-7). The reading
of whole-box N_f on the configurations with 16875 or more radial points was fixed by the verifier before any F3 row
existed: at 11250 radial points an off-axis lobe near (8.4, 2.7) (r 8.78, theta 0.31; not the lobe above P of 4.4) is
under-resolved (the residual there oscillates in r with period 0.036, two grid points per period) and pins the whole-box
value at 6.8e-7 to 7.0e-7 on every fit below that level.

Every fit compared by the selection rules (verifier maxima; configurations as stated; L2 objective on the fit grid):
     fit   c_l        cap    LSQR budget            L2          whole-box N_f        N_v r <= 1000      N_v r > 1000       J (857, eps 0.03)
     F0    5.5763624  150    start                  7.65e-6     2.28e-6 to 2.44e-6   6.4e-7 to 6.8e-7   1.12e-6 to 1.15e-6 3.85e-6
     X1    5.5753626  150    750                    8.47e-6     6.5e-7 to 7.0e-7     5.20e-7, 5.32e-7   1.13e-6, 1.15e-6   2.74e-6
     F1    5.5763640  150    750                    7.08e-6     2.09e-6, 2.22e-6     5.90e-7, 6.27e-7   1.46e-6, 1.47e-6   2.27e-6
     F1r   5.5753651  150    X1 + 1000 (free)       7.47e-6     1.04e-6, 1.02e-6     4.26e-7, 4.43e-7   1.09e-6, 1.10e-6   2.24e-6
     W1    5.5753626  150    X1 + reweighted        -           4.5e-6, 5.0e-6 (*)   1.31e-6, 1.45e-6 (box)               -
     X2    5.5753626  150    X1 + 20750             4.097e-6    1.42e-6 to 1.51e-6   3.98e-7 to 4.20e-7 1.10e-6 to 1.13e-6 3.14e-6
     F2    5.5763709  150    F1 + 20750 (free)      4.259e-6    1.57e-6 to 1.64e-6   4.39e-7 to 4.59e-7 1.10e-6 to 1.13e-6 3.41e-6
     X3    5.5753626  200    X2 + 20750             1.619e-6 +  6.83e-7 to 7.16e-7   1.91e-7 to 2.01e-7 1.09e-6 to 1.11e-6 1.39e-6
     F3    5.5763712  200    F2 + 20750 (free)      1.664e-6 +  7.28e-7 to 7.65e-7   1.95e-7 to 2.14e-7 1.09e-6 to 1.11e-6 1.48e-6
  Configurations: F0 over six configurations (11250 x 384, 16875 x 384, 512 and 768, 22500 x 384 and 512; radial x
  angular points); X1, F1, F1r, W1 at 11250 x 384 and 16875 x 512; X2, F2 also at 16875 x 768; X3, F3 at 16875 x 512,
  16875 x 768 and 22500 x 512 for whole-box N_f and at all four configurations of 4.4 otherwise. J is computed at
  16875 x 384 on every fit.
  Whole-box N_f and N_v for r <= 1000 exclude the evaluation columns next to the y-axis (pi/2 - theta < 0.006), where
  the evaluator's value is a cancellation floor; at 16875 x 768 that column holds 8.60e-7 on F3 (r 9.5) and 5.1e-7 on X3
  (r 10 to 100). N_v for r > 1000 is read on all columns.
  (*) W1's maximum sits on the first angle off the x-axis and grows as that angle shrinks: lower bounds of an axis
  limit. (+) on the 20480 x 960 fit grid of the m <= 200 runs (X2 reads 4.050e-6 there); the other L2 values are on
  20480 x 720. Fixed c_l values tried: 5.60 on a 244-function basis (3 h fixed, then 1500 iterations free: c_l moved by
  -8.6e-6; near-P N_f 6.5e-6 against 3.2e-6 for the free fit of that basis; undecided at that level); on the candidate's
  radial basis with angular cap m <= 150, the profile below.
Fixed-c_l profile (375 x m <= 150). Each row starts from F0 moved along the direction of X1 by d in c_l and holds c_l at
the value stored with that start, which is 5.5763624 + d + 0.18 d^2 to within 8e-7 (the table quotes the stored values);
it then runs 21500 LSQR iterations, the budget of F2 (750 + 20750), on the fit grid 20480 x 720. F2, the free fit of the
same lineage, basis, grid and budget, is the reference. Verifier values: L2 objective on the fit grid; whole-box N_f at
11250 x 384 and 16875 x 512 (columns next to the y-axis excluded as above); J at 16875 x 384; ratio to F2 in brackets.
     c_l        d        L2                   whole-box N_f                     J (857, eps 0.03)    reading
     5.5524653  -2.4e-2  3.301e-6 (0.775)     1.792e-6, 1.825e-6 (1.139, 1.159) 3.953e-6 (1.158)     undecided
     5.5604082  -1.6e-2  2.738e-6 (0.643)     1.127e-6, 7.630e-7 (0.716, 0.485) 1.754e-6 (0.514)     undecided
     5.5683739  -8e-3    3.157e-6 (0.741)     8.906e-7, 6.730e-7 (0.566, 0.427) 1.324e-6 (0.388)     undecided
     5.5723653  -4e-3    3.654e-6 (0.858)     1.119e-6, 1.123e-6 (0.711, 0.713) 2.412e-6 (0.707)     not determined
     5.5743631  -2e-3    3.945e-6 (0.926)     1.362e-6, 1.368e-6 (0.865, 0.869) 2.953e-6 (0.865)     not determined
     5.5753626  X2       4.097e-6 (0.962)     1.424e-6, 1.435e-6 (0.905, 0.911) 3.143e-6 (0.921)     (X2, table above)
     5.5763709  F2       4.259e-6             1.574e-6, 1.575e-6                3.414e-6             reference
     5.5783631  +2e-3    4.591e-6 (1.078)     1.791e-6, 1.792e-6 (1.138, 1.138) 3.956e-6 (1.159)     not determined
     5.5793640  +3e-3    4.748e-6 (1.115)     1.909e-6, 1.911e-6 (1.213, 1.214) 4.180e-6 (1.224)     not determined
     5.6004662  +2.4e-2  8.671e-6 (2.036)     4.587e-6, 4.590e-6 (2.915, 2.914) 9.800e-6 (2.871)     excluded
  Reading rule, fixed before these runs: "not determined at this level" if the L2 objective and the whole-box N_f on
  each configuration are within 30 percent of F2's and |h(P) - 1| <= 1e-6; "excluded at this level" if the fit has
  flattened (its objective changes by less than 2 percent over its last 1000 iterations) and its N_f maximum within 0.5
  of P is at least twice F2's on each configuration; "undecided" otherwise. At 16875 x 512 the whole-box maximum of N_f
  lies within 0.5 of P on every row except d = -8e-3, where it is 0.57 left of P on the x-axis side (0.7 percent above
  the maximum within 0.5 of P); at 11250 x 384 it is at the under-resolved off-axis lobe described above at d = -8e-3
  and d = -1.6e-2, and within 0.5 of P on the other rows. On every row N_v for r <= 1000 has, to within 0.03, the same
  ratio to F2's as the whole-box N_f on the same configuration. On every row the identity c_l = (1 + psi_xy(0))/3 holds
  to 3.2e-9. On the rows not excluded |h(P) - 1| is at most 6.9e-7 except at 5.5524653, where it is 1.46e-6 at
  11250 x 384, 2.6e-7 at 16875 x 512 and 6.3e-9 at 22500 x 384 (it falls with the radial resolution of the evaluation,
  as on the candidate); by the 11250 x 384 value that row reads "undecided", and with h(P) taken at 16875 or more radial
  points "not determined". On the excluded row it is 1.07e-6 and 2.45e-7. At equal budget the L2 objective increases
  with c_l from 5.5604082 up, near F2 by about 4 percent per 1e-3 in c_l, and is larger at 5.5524653 than at 5.5604082;
  the whole-box N_f and J increase with c_l from 5.5683739 up and fall faster than the objective from F2 down to
  5.5683739, and they are larger at 5.5604082 and larger again at 5.5524653 (whole-box N_f 0.427, 0.485 and 1.159 of
  F2's at 16875 x 512 at 5.5683739, 5.5604082 and 5.5524653; J 0.388, 0.514 and 1.158). Among the tested rows the L2
  objective is least at 5.5604082 and the residual maxima at 5.5683739. At 5.5524653 the L2 objective is below F2's
  while the residual maxima are above F2's; that fit had not flattened (its objective fell by 2.5 percent over its last
  1000 iterations; at that rate, assumed constant, it would need about 7400 more iterations to reach the objective at
  5.5604082). So every fixed-c_l fit below F2's exponent reaches a lower L2 objective than F2 at the same budget, while
  along the 20750 iterations from F1 to F2 the free c_l stays between 5.5763641 and 5.5763716 (F0: 5.5763624): at this
  budget F2's exponent is set by its start, not by a minimum of the objective; "free branch" in this report names the
  fits with c_l free, not a selected exponent. These are fits from transplanted starts at one budget; they do not locate
  an exponent or a minimum of an objective over c_l. Continued for a further 21500 iterations at their exponents (43000
  in all), the fits at 5.5604082 and 5.5524653 reach L2 objectives 2.2009e-6 and 2.2121e-6 (ratio 1.005) and whole-box
  N_f 1.167e-6 and 1.344e-6 at 11250 x 384 and 6.311e-7 and 1.301e-6 at 16875 x 512, their objectives changing by -0.148
  and -0.338 percent over the last 1000 iterations; by the rule fixed before these runs the bracket is kept at twice the
  budget. Neither continuation is at equal budget with F2 and both may still be falling, so this too concerns fits from
  transplanted starts at a stated budget, not where the objective minimized over shapes at fixed c_l has its minimum
  over c_l. The L2 gap between them fell at every linearization of the continuation, from 5.63e-7 at its start to
  1.12e-8 at its end; each of the four complete linearizations before the last reduced it by more than the 1.12e-8 that
  remains (the last, of 1500 iterations, by 5.9e-9), so the order in L2 is a fact at this budget only.
Nested pair (375 x m <= 200). The rows at 5.6004662 and 5.5683739 continued from their ends on m <= 150 to the
candidate's angular cap as X2 was continued to X3 (c_l held at the stored value, 20750 LSQR iterations on 20480 x 960);
F3, the free fit of that basis at the same budget, is the reference. Verifier values as in the profile above (whole-box
N_f at 11250 x 384 and 16875 x 512, J at 16875 x 384), ratios in brackets.
     c_l        L2 (to F3, to X3)           whole-box N_f (to F3)             J (to F3)            reading
     5.6004662  2.795e-6 (1.680, 1.726)     1.676e-6, 1.825e-6 (2.412, 2.499) 3.612e-6 (2.439)     excluded
     5.5683739  1.328e-6 (0.798, 0.820)     9.132e-7, 4.725e-7 (1.315, 0.647) 7.807e-7 (0.527)     undecided
     5.5753626  1.619e-6 (0.973, 1)         6.909e-7, 6.841e-7 (0.995, 0.937) 1.388e-6 (0.937)     (candidate)
     5.5763712  1.664e-6 (1, 1.028)         6.947e-7, 7.303e-7 (1, 1)         1.481e-6 (1)         reference
  Rule, fixed before these runs: the reading rule of the profile, against F3, for the interval (the reading column); for
  the fit at 5.6004662 the ratio Q of its objective to F3's (4.8). The objective changed by -0.96 percent over the last
  1000 iterations at 5.6004662 and by -0.61 percent at 5.5683739. |h(P) - 1| is at most 7.72e-7 on both fits and both
  configurations, and the identity c_l = (1 + psi_xy(0))/3 holds on both to 3.3e-9. The N_f maximum within 0.5 of P is
  2.412 and 2.499 times F3's at 5.6004662, where both whole-box maxima lie, and 0.554 and 0.551 times F3's (0.591 and
  0.588 times X3's) at 5.5683739, whose whole-box maxima on both configurations are at the off-axis lobe point described
  above (r 8.78, theta 0.30), which the 11250-point radial grid under-resolves.
Reading. Rule (1) keeps X1 against F1 in N_f and N_v but not in J (2.74e-6 against 2.27e-6), so X1 is not kept; X2 is
kept against F2 with the far band read as all r > 1000 (both readings in the paragraph above); X3 is kept against F3
(whole-box N_f 0.94, N_v for r <= 1000 0.94 to 0.99, far field within 3e-9, J 0.94). Rule (2) gives X3: its whole-box
N_f is lower than X2's by a factor 2.1 on every common configuration. F1r is a free continuation without an equal-budget
control and is listed, not ranked. Along the continuation X1 to X2 the L2 objective halves and the near-P maximum
doubles: the residual at the angular cap frequency of the basis (2 M = 300) moves from r 4 to 7.6 toward r 7 to 8.6 and
above P, where the small transport terms near the stagnation point divide it. Along F1 to F2 the L2 objective falls by
40 percent and the near-P maximum falls from 2.1e-6 to 2.3e-6 (range over the configurations) down to 1.6e-6, with the
cap-frequency residual at the same place as on X2. On the m <= 150 basis the long continuation lowered the maximum
residual on the free branch (F1 to F2) and raised it at the fixed c_l (X1 to X2). With the cap raised to 200 the
cap-frequency residual next to the x-axis (r 7.0 to 8.3) moves to angular frequencies 400 to 600 (about 2 M) and is 3.4
times lower at r 8.3; every window near P of 4.4 except y >= 1 falls by a factor 2.1 to 2.5, and the window y >= 1 rises
by 1 percent at 11250 x 384 (the under-resolved off-axis lobe near (8.4, 2.7) described above) and falls by a factor
1.23 at 16875 x 512. Since the minimum is taken over several fits, it is a selection; the table lists the fits compared
by the rules. Not in the table: the budget row (X3 continued on its own rows, 4.2 and 4.4), X3 continued on its own rows
with the inverse domain at 1e4 L (4.5), the m <= 250 refinement row and its free control and the domain columns (4.4),
the free control of the 9000 L row and its continuation (4.5), the m <= 250 row continued with rows to 9000 L (4.4),
none a candidate; the equal-budget m <= 150 iterate of 4.1, the solver-setting arms of 4.2 (damping 1e-12,
reorthogonalization) and the 244-function fit at c_l 5.60 below.

Interval. The quoted interval contains the c_l of the candidate and of its control and every c_l tested on the
candidate's radial basis with angular cap m <= 150 that the rule of the fixed-c_l profile does not exclude at the
attained level (5.5524653 to 5.5793640); 5.6004662 is excluded at that level, and so is its continuation to m <= 200
(the nested pair above: N_f within 0.5 of P 2.412 and 2.499 times F3's). The interval is quoted on the candidate's
radial basis; the 244-function fit at 5.60 (below) is undecided on its smaller basis.
Fits of comparable residual quality exist at c_l values 1e-3 apart, and the free continuations listed here move c_l by
at most 6.9e-6 at these budgets, under 1 percent of that separation (F2: +6.9e-6 in 20750 iterations, F3: +2.2e-7 in
20750, the free control of the m <= 250 row: -6.0e-7 in 20750, the free control of the 9000 L row of 4.5: -1.5e-6 in
20750, F1r: +2.5e-6 in 1000; F1r, started from the fixed value, moves toward the free branch, F2 and F3 away from the
fixed value, and the free controls of the m <= 250 row and of the 9000 L row toward it). This spread measures how weakly
the residual pins c_l; it is not an uncertainty interval for an exact profile, and the available diagnostics do not
calibrate the absolute exponent error. Earlier measurements on smaller bases: the least first-order cost of a unit
change of c_l on the 244-function basis is at most 3.6e-3 of the objective (still falling); the 244- and 302-function
trials moved along the soft direction stay within 30 percent of their fits in every diagnostic at -1e-3; the
244-function fit with c_l held at 5.60 reached 1.97 times the objective of the free fit in 3 h and was still falling;
continued for 1500 further LSQR iterations in the free formulation it kept c_l (5.5999914, a change of -8.6e-6) and
reached 1.36 times (falling 1.6 percent in the last 250 iterations); on the independent evaluator its residual is 2.0
times that of the free fit on that basis next to P, 1.3 to 1.4 times in the whole box and at 10 <= r <= 100, and its J
2.1 times, which is undecided at that level. The independent discretization (4.6) has fixed-c_l states over 5.52 to
5.71; those from 5.556 to 5.596 include both values and do not discriminate between them.

### 4.4 Residual tables
Normalizations. R = W.grad rho - rho with W = c_l X + U. N_f = |W_1 rho_x| + |W_2 rho_y| + |rho| (flux normalization;
it vanishes with W at P, so it is the stricter one next to P) and N_v = |rho| + |X.grad rho| + |U.grad rho| (stricter in
the far field). Every residual below is a maximum of |R|/N over a between-node grid of the verifier's evaluator (its own
generator of rho from the formula, its own inverse to R = 7.652e6), not over fit nodes. Configurations of the
independent evaluator: radial x angular points 11250 x 384, 16875 x 512, 16875 x 768, 22500 x 512 (log-radial points on
r in [7.652e-4, 7.652e6], angular points on the quarter, between fit nodes).

The candidate by region (N_f maxima at 11250 x 384 / 16875 x 512 unless stated; the columns next to the y-axis excluded
where stated):
     |X - P| < 0.5                         6.51e-7 / 6.84e-7 (X2: 1.42e-6 / 1.43e-6)
     strip y < 0.2, 6 <= x < 8.1           5.35e-7 / 5.56e-7
     y < 0.2, x > x*                       2.70e-7 / 1.83e-7
     y 0.2 to 1, |x - x*| < 1              5.34e-7 / 5.68e-7
     y >= 1                                6.91e-7 (under-resolved lobe at 11250 radial points, 4.3) / 4.32e-7
     r <= 0.1                              N_f 4.95e-9, N_v 1.07e-8 (*)
     0.1 <= r <= 2                         N_f 2.48e-8, N_v 4.83e-8 (*)
     2 <= r <= 10                          whole-box N_f maximum (the rows above)
     10 <= r <= 100                        N_f 8.66e-8, N_v 7.10e-8 (*)
     100 <= r <= 1000                      N_f 1.50e-8 to 1.60e-8 (the four configurations), N_v 6.49e-8 (*)
     r <= 1000, N_v                        1.92e-7, 1.92e-7, 2.01e-7, 1.91e-7 (the four configurations; y-axis columns
                                           excluded at 16875 x 768; 2.49e-7 there without that exclusion)
     1000 <= r <= 7652 (= 1000 L)          N_v 2.15e-7 / 2.18e-7 (at r 7647, theta 1.554, on the first; past the fit rows)
     r > 1000 L (formula beyond the fit)   N_v 1.090e-6, 1.101e-6, 1.111e-6, 1.103e-6 (next to the y-axis, r 3.61e4 to
                                           3.72e4); N_f 1.320e-7 to 1.323e-7 (r 3.3e4, theta 0.84)
  (*) 16875 x 512 with the evaluation columns next to the y-axis excluded (pi/2 - theta < 0.006). These maxima sit on
  the first column outside the cut and may still contain part of the evaluator's floor, so they may be raised by that
  floor; they are not floor-free values. Without the exclusion the N_f maxima lie in the floor column on almost every
  configuration: 1.45e-8 to 1.15e-7 for r <= 0.1, 2.20e-8 (at r 2, not in the column) to 1.05e-7 for 0.1 <= r <= 2, and
  1.37e-7 to 5.11e-7 at r 10.0 to 10.3 for 10 <= r <= 100. Off the y-axis (pi/2 - theta >= 0.2) the r <= 0.1 maximum is
  2.4e-11 on the independent evaluator and 2.3e-11 on a between-node scan of the formula, at the same place (r 0.1,
  theta near 0); within 0.2 of the y-axis the independent evaluator reads up to 5e-9 and the scan 3e-12, so the (*)
  values there are set by the evaluator floor. The same holds for 10 <= r <= 100: off the y-axis the two agree (8.2e-8
  against 8.0e-8 at r 13.9, theta 0.92).
Absolute values. The maxima of |R| itself on the same between-node grids (all evaluation columns; candidate, formula
beyond the fit; 16875 x 512 / 22500 x 512) and, as a scale, the maximum of |rho| over the region, which sits at the
outer radius of each region since rho grows like r^3 at the centre and like r^(1/c_l) at large r:
     region                 max |R|                  max |rho|      max |R| / max |rho| (16875 x 512)
     r <= 0.1               1.71e-13 / 1.65e-13      3.85e-4        4.4e-10
     0.1 <= r <= 2          8.92e-8 / 8.91e-8        2.94           3.0e-8
     2 <= r <= 10           6.03e-5 / 5.82e-5        111.7          5.4e-7
     |X - P| < 0.5          1.05e-5 / 1.05e-5        14.80          7.1e-7
     10 <= r <= 100         1.99e-5 / 1.98e-5        208.9          9.5e-8
     100 <= r <= 1000       6.03e-6 / 6.04e-6        319.2          1.9e-8
     1000 <= r <= 7.652e6   1.897e-4 / 1.897e-4      1590           1.2e-7
  The last column is a quotient of two suprema over the region, not a pointwise ratio. At 11250 x 384 and 16875 x 768
  the absolute maxima agree with these to 6 percent, except r <= 0.1 (1.3e-13 to 2.7e-13 over the four configurations,
  round-off level) and 2 <= r <= 10 at 11250 x 384 (1.10e-4, the under-resolved lobe of 4.3). The whole-box absolute
  maximum is the far value 1.897e-4 beyond 1000 L, where the candidate has no fit rows; over r <= 1000 (with or without
  the evaluation columns next to the y-axis) it is 6.03e-5 / 5.82e-5. Scaled by the size of rho the absolute residual is
  at most 7.1e-7 on these two configurations (next to P; 7.5e-7 at 16875 x 768), the order of the normalized maxima
  above.
Elliptic equation. The velocity is computed from rho by the canonical inverse (V1), so -Lap psi = d_x rho carries no
separate fitted residual; the numerical error of the inverse is reported in 4.5. As a check of the evaluator's inverse
(not a property of the trial), re-differentiating its psi (8th-order differences in log r, spectral in theta) gives for
the elliptic residual E = -Lap psi - d_x rho, on the candidate, sup|E| / sup|d_x rho| = 1.49e-6, 3.93e-7, 1.06e-7 on
1 <= r <= 10 at N = 11250, 16875, 22500 (falling with N; quotients of suprema over the region; sup |d_x rho| = 20.0
there, so sup|E| = 2.98e-5, 7.86e-6, 2.12e-6), at most 2.1e-9 for r >= 10 and 1.3e-8 to 5.2e-8 on 0.01 <= r <= 1; on
r <= 0.01 it is round-off of the second difference where psi ~ r^2 (up to 3.15e-4, rising as N^2). X1 and F0 give the
same to 10 percent.

Resolution rows (c_l held at 5.5753626 on each basis, each on its own fit grid; 16875 x 512) and domain columns:
     basis (radial x angular)       whole-box N_f   N_v r <= 1000   J (857, eps 0.03)   h(P) - 1 (11250 / 16875)
     244 x m <= 100                 3.74e-6         1.06e-6         5.58e-6             -2.7e-8, -6.9e-8
     375 x m <= 100                 3.11e-6         8.74e-7         5.28e-6             2.6e-7, 1.5e-8
     375 x m <= 150 (X2)            1.435e-6        4.00e-7         3.14e-6             2.2e-7, 1.6e-8
     375 x m <= 200 (X3)            6.84e-7         1.92e-7         1.39e-6             2.8e-7, 3.1e-8
     375 x m <= 250 (refinement)    4.23e-7 (a)     1.23e-7         5.00e-7             -, 3.2e-8
  (a) With the columns within 0.006 of the y-axis excluded; with them 5.38e-7, the evaluator's floor in the column next
  to the axis (4.4). The value is the lobe above P on the unshifted grid; over four radial sampling phases at 16875 x
  512 it is 4.22e-7 to 4.66e-7, and 4.88e-7 at 22500 x 512 (X3's lobe: 4.27e-7 to 4.74e-7 and 4.95e-7). The
  m <= 250 row is read at 16875 and 22500 radial points only: the exponent H of its density carries angular frequencies
  to 500 (cos(2 m theta), m <= 250), beyond the 479 modes of 11250 x 384; the agreement of 16875 x 512 and 16875 x 768
  (columns next to the y-axis excluded) is the aliasing check.
  Domain columns (c_l held at 5.5753626106; X3 continued 20750 iterations on each domain with the two-term closure at
  100 L, 333 L or 1e4 L beyond the fit radius; ratios to X3 in its own convention on the independent evaluator at 11250
  x 384, 16875 x 512, 22500 x 384):
     fit radius        2-10 N_f max ratio   10-100 N_f ratio raw (cut)  h(P) - 1 (N >= 16875)   J (857, eps 0.03)
     900 L (X3)        1                    1                           3.1e-8, -1.8e-8          1.39e-6
     300 L             0.99, 0.62, 0.74     0.89, 0.76 (cut 0.79), 0.96     5.1e-8, -3.1e-9          8.14e-7
     90 L              1.04, 0.62, 0.72     1.02, 1.23 (cut 0.84), 0.83     5.6e-8, 6.8e-10          5.53e-7
     9000 L            1.02, 0.66, 0.74     0.82, 1.42 (cut 1.05), 1.00     4.8e-8, -5.0e-9          9.11e-7
  ("cut": the columns with pi/2 - theta < 0.006 excluded, at 16875 x 512; the raw 10-100 maxima lie in that column. The
  9000 L row has fit rows to 9000 L and its inverse domain and closure at 1e4 L.)
  The m <= 250 row is a refinement row only (it is not a candidate; reading fixed before its run). Budget: the m <= 150
  and m <= 200 rows are at different budgets (X3 = X2 + 20750); the equal-budget comparison is in 4.1. The m <= 250 row
  is X3 with its angular cap raised to 250 and continued 20750 iterations at the fixed c_l, so it is at the budget
  X3 + 20750. The m <= 100 rows are fixed-c_l fits of their own bases continued for 20750 iterations, as X2 is on its
  basis (c_l 2.1e-9 above X3's at 375 and 1.7e-9 at 244).
Reading rule fixed before the runs: the domains agree if the 2-10 and 10-100 maxima are within a factor 1.5 of the
formula-global fit on the same basis (read two-sided, ratios between 1/1.5 and 1.5; each domain column falls below 1/1.5
at one configuration, being lower, not higher) and |h(P) - 1| < 1e-7; J is reported next to them. Domain fits with a
two-term closure beyond the fit radius are only C^1 across that radius; they are quoted as bounded-domain fits, not as
admissible trial densities. The domain columns hold c_l at the candidate's value and test whether the interior residual
and the consistency condition h(P) = 1 depend on the box in the closed problems; each continues X3 for 20750 iterations
on its own domain, so they also carry that further budget. They are not residuals of the domain fits under the canonical
velocity law. At interior points the velocity of a bounded-domain fit depends on what is assumed beyond its fit radius
(the two-term closure, or the formula's own continuation, which is not fitted there in any bounded-domain fit). In
normalized-residual terms (sampled maxima, earlier domain fits on the 375 x m <= 100 free basis) the dependence is
6.8e-7 (closure at 111 L; separate evaluator) and 8.6e-6 (closure at 100 L; real-space quadrature of the third
evaluator, most of it drift of the unfitted exterior formula over that fit's extra iterations) within 0.5 of P,
comparable to or larger than the interior residual, and 2.2e-8 within 0.5 of P and 2.7e-8 at 0.5 to 2.5 from P for the
closure at 333 L (separate evaluator). For the 90 L fit from X3 the residual within 0.5 of P is 1.9e-7 to 2.3e-7 in N_f
with the closure at 100 L (h(P) - 1 between -5e-9 and +6e-8 over two independent sets of grids) and about 3e-5 with the
formula continued beyond the fit radius (h(P) - 1 about -6e-5); in N_v it is 6.0e-8 with the closure and 9.4e-6 with the
formula continued (11250 x 384), and the real-space quadrature of the third evaluator gives 6.6e-6 at its sampled points
within 0.5 of P when the closure is replaced by the formula continued to infinity, with the closure-convention
denominator held fixed (velocity change 4.2e-4 there); for the 300 L fit the N_f residual within 0.5 of P is 3.9e-7 with
the closure at 333 L and 4.9e-7 with the formula continued (11250 x 384; the lead's evaluator gives 3.5e-7 and 4.0e-7).
By the reading rule the 90 L domain agrees with the candidate on the lead's evaluator (2-10 ratios 0.70 and 0.73, 10-100
ratio 0.82) and on two of the three configurations of the separate evaluator; on the third (16875 x 512) its 2-10
maximum is 0.62 times the candidate's, outside the factor 1.5 on the low side. Where it differs, it is lower: within 0.5
of P its residual is 3 times and its J 2.5 times below the candidate's (the gain sits in the strip next to the x-axis
left of P and in the band y 0.2 to 1; the lobe above P does not move and becomes the 2-10 maximum). That fit carries
both the smaller domain and the further budget, and it solves a different closed problem from its start (the closure at
100 L changes the interior velocity of the X3 shape; start objective 2.3e-4 on its rows), so it shows that X3's near-P
residual is not a floor of the m <= 200 basis in that closed problem; it does not show the same gain for the full-plane
problem. The 300 L domain agrees in the same way: on the lead's evaluator (2-10 ratios 0.74 and 0.72, 10-100 ratios
0.86) and on two configurations of the separate evaluator, with the 2-10 ratio 0.62 at 16875 x 512, where for both
domain columns the 2-10 maximum is the lobe above P (4.27e-7 and 4.23e-7), which no column moves, while the candidate's
lies next to P. The 300 L fit carries the same further budget as the 90 L fit and differs from it in the domain only:
within 0.5 of P its residual is 0.57 to 0.59 times the candidate's and its J 0.59 (eps 0.03; 0.56 at eps 0.01), against
0.32 to 0.33 and 0.40 for the 90 L fit, the strip left of P 0.67 against 0.41, the lobe above P 0.99 against 0.98. The
9000 L fit, whose rows reach 9000 L, carries the same further budget and agrees in the same way (2-10 ratio 0.66 at
16875 x 512, where its 2-10 maximum lies next to P; 10-100 ratio 1.42 there, 1.05 with the cut): within 0.5 of P its
residual is 0.66 to 0.68 times the candidate's and its J 0.66 (eps 0.03; 0.64 at eps 0.01), N_v for r <= 1000 1.02, 0.66
and 0.78 times, the lobe above P 1.00. Among these three domain columns the near-P gain at that budget therefore grows
as the domain shrinks; with the budget row below (900 L) included it is not monotone in the domain. X3 continued on its
own domain and rows for the same iterations (the budget row of 4.2) reads 0.50 to 0.54 times the candidate's within 0.5
of P and 0.48 in J (0.45 at eps 0.01). Against that row, by the reading fixed before it ran (ratios in [0.8, 1.25]
attribute the gain to the budget), the 300 L fit reads 1.08 to 1.09 within 0.5 of P and 1.21 in J (1.254 at eps 0.01,
0.004 above the interval), so its near-P gain over X3 is that of the budget; the 90 L fit reads 0.60 to 0.63 within 0.5
of P (0.82 in J) and the 9000 L fit 1.25 to 1.27 and 1.35 (1.42 at eps 0.01), outside the interval near P on all three
configurations (90 L) or on two of the three (9000 L, inside at 16875 x 512 only; its J is outside), so for these two
the ratios are stated without attribution. The closure and the formula readings of a domain fit measure its sensitivity
to two exterior continuations, not a closure error of a fitted far field. The domain columns are therefore a stability
observation within closed fitting problems, not an upper bound on the full-plane truncation error; they do not establish
domain independence of the full-plane problem (the reading of the same fits under the canonical law follows below). For
the formula-global fits, whose rows are r < 900 L and whose inverse domain is r <= 1000 L, the fits' own inverse
convention (the density replaced by its two-term exterior extension beyond 1000 L) was compared with the formula
continued to the evaluator's outer radius, on one grid of the separate evaluator (11250 x 384), maxima over all grid
points of the open first quadrant. On X1, which holds c_l fixed and therefore sees only the change of velocity, the
residual changes by at most 5.1e-9 in N_f and 1.5e-9 in N_v within 0.5 of P, 1.0e-8 in N_f and 3.2e-9 in N_v at
2 <= r < 10, and at most 2.0e-8 in N_v for r < 1000 (1.6e-8 for r <= 300): about 1 percent of X1's band maxima next to
P, 1.5 percent at 2 <= r < 10 and at most 7 percent at 300 to 1000. In the identity convention c_l also moves, by
3.4e-9. The free fit of the 375 x m <= 100 basis gives the same values to 2 percent. On X3 directly (separate evaluator,
11250 x 384 and 16875 x 512, the two grids agreeing to 3 digits) the changes are the same to two digits, and c_l moves
by 3.4e-9 in the identity convention (the identity in the fit's own convention returns the fixed c_l to 2.2e-10).
Relative to X3's band maxima the changes are 0.8 percent next to P, 1.5 percent at 2 <= r < 10 and 22 to 47 percent in
N_v at 10 <= r < 1000, where X3's band maxima are smaller than X1's; X3's band maxima themselves move by at most 1
percent next to P and at 2 <= r < 10, by at most 10 percent at 10 to 300 and by 18 to 23 percent (lower in the fit's
convention) at 300 to 1000. On X3's rows beyond r = 1000 (131 L to 900 L) the fit's convention reads 0.25 to 0.47 of the
formula reading. The residuals of 4.3 and 4.4, except the domain columns read in each fit's own convention, are the
formula (canonical) reading. These are grid maxima for one closure; they do not exclude other far-field defects.

Domain columns under the canonical law. Without its closure each domain fit is a global trial density (the formula of
4.2 with its own coefficients), so read with the formula continued beyond its fit radius (no closure) its residual is a
full-plane residual under the canonical law, comparable with the candidate's. No reading rule was fixed for this
comparison before it was computed. Independent evaluator (own inverse to 1e6 L) at 11250 x 384 / 16875 x 512 / 22500 x
384, columns within 0.006 of the y-axis excluded; each domain fit continues X3 for 20750 iterations, and the 900 L row
at that budget is the budget row of 4.2:
     fit rows to (iterations after X3)  N_f r <= 1000            N_f |X - P| < 0.5        N_v r <= 1000            N_v r > 1000
     90 L (20750; 11250 x 384 only)     1.02e-4                  3.11e-5                  9.87e-4                  1.32e-2
     300 L (20750)                      7.66e-7/5.28e-7/5.59e-7  4.86e-7/4.88e-7/4.87e-7  4.12e-7/4.14e-7/4.12e-7  3.54e-5/3.53e-5/3.54e-5
     900 L (20750, budget row)          6.97e-7/4.25e-7/4.86e-7  3.54e-7/3.59e-7/3.55e-7  1.94e-7/1.24e-7/1.42e-7  1.077e-6/1.077e-6/1.078e-6
     9000 L (20750)                     7.05e-7/4.49e-7/4.91e-7  4.45e-7/4.49e-7/4.51e-7  1.96e-7/1.26e-7/1.44e-7  3.27e-8/3.31e-8/3.28e-8
     900 L (0, the candidate X3)        6.91e-7/6.84e-7/6.61e-7  6.51e-7/6.84e-7/6.61e-7  1.92e-7/1.92e-7/1.85e-7  1.084e-6/1.074e-6/1.085e-6
Against the 900 L row at the same budget, the 9000 L row reads 1.01, 1.06 and 1.01 in N_f for r <= 1000, 1.25 to 1.27
within 0.5 of P, 1.01 to 1.02 in N_v for r <= 1000 and 0.030 to 0.031 beyond r = 1000; the 300 L row reads 1.10, 1.24
and 1.15, 1.36 to 1.38, 2.1 to 3.3 and 33. Under the canonical law the fits with rows to 300 L, 900 L and 9000 L thus
give the same N_f residual for r <= 1000 to a factor 1.24 and within 0.5 of P to a factor 1.4 (1.3 between 900 L and
9000 L); in N_v for r <= 1000 the 300 L fit is 2.1 to 3.3 times higher, and beyond r = 1000 the band follows the extent
of the fitted rows and of the inverse domain with its closure, which each domain fit has just beyond its rows (3.5e-5,
1.1e-6 and 3.3e-8; for the 9000 L row the inverse domain alone gives the factor 0.27 of its fall, 4.5). The 90 L fit is
not an approximate full-plane profile under the canonical law (3.1e-5 within 0.5 of P, 1.3e-2 beyond r = 1000): its
agreement in the reading of the domain rule holds only with its closure. These are grid maxima on three configurations,
not a convergence study in the domain; the closure readings above remain the sensitivity check of the closed problems.

Free-branch record (c_l from the identity; verifier between-node numbers; J on 857 labels):
     basis               c_l         J spread eps 0.03 / 0.01   I(0.03)     N_f max (**)
     215 x m <= 100      5.5763607   1.940e-5 / 1.940e-5        -2.97e-7    1.86e-5
     244 x m <= 100      5.5763633   4.746e-6 / 4.980e-6        -4.68e-7    4.6e-6
     302 x m <= 100      5.5763609   3.473e-6 / 3.607e-6        +5.08e-7    2.3e-6
     375 x m <= 100      5.5763622   3.679e-6 / 3.669e-6        +4.84e-7    2.44e-6
     375 x m <= 150 (F2) 5.5763709   3.414e-6 / 3.763e-6        -7.04e-7    1.57e-6
     375 x m <= 200 (F3) 5.5763712   1.481e-6 / 1.709e-6        -3.51e-7    6.95e-7 to 7.65e-7
  (**) For the four m <= 100 rows the N_f maximum on 2 <= r < 10, the band containing P (on the 244 row this is the
  whole-box maximum; within 0.5 of P that row reads 3.25e-6, the value compared in 4.3); for F2 the lowest whole-box
  value of the table of 4.3; for F3 the maximum within 0.5 of P over the four configurations.
Domains on 375 x m <= 100 (free; fit radii 900 L, 300 L, 100 L, each read with its own closure): J 3.679e-6, 4.052e-6,
4.000e-6 (eps 0.03); c_l 5.5763622, 5.5763628, 5.5763644.
Reading. Along the radial sequence at m <= 100 the J spread falls by a factor 4 from 215 to 244 functions and by 27
percent from 244 to 302, and rises by 6 percent from 302 to 375; it is not monotone at the last step. At the fixed c_l
(each fit continued for 20750 iterations at that c_l), the step from 244 to 375 radial functions at m <= 100 lowers the
whole-box N_f by the factor 0.83 to 0.86, the N_f maximum within 0.5 of P by 0.95, N_v for r <= 1000 by 0.83 to 0.85
(11250 x 384 and 16875 x 512) and the 857-label J by 0.95 (0.91 at eps 0.01). N_v for r > 1000 is equal within the
configuration spread (1.31e-6 and 1.35e-6 at 244, 1.325e-6 at 375, the maximum at 244 in the column next to the y-axis),
and with the columns next to the y-axis excluded (pi/2 - theta < 0.006) it is 6.4 percent higher at 375 (1.325e-6
against 1.245e-6, both at 3.3e3 to 3.4e3 L, theta 1.541). No reading of this pair was fixed before its run; these are
data. The radial rows at m <= 100 stall at the angular floor (on the 375 x m <= 100 fit, the only one of these rows
where it was measured, the J oscillation across family A is carried by residual at angular frequencies at or above the
cap). The angular rows are the test: at the fixed c_l, J falls from 3.14e-6 (m <= 150) to 1.39e-6 (m <= 200), on the
free branch from 3.41e-6 to 1.48e-6, and at equal budget the m <= 200 iterate has 0.62 to 0.69 times the J of the
m <= 150 iterate on 185 labels (every fourth label of family A). The angular row at the fixed c_l (m <= 100, 150, 200;
the last 20750 iterations of each at the fixed c_l, from different starts) was read by a rule fixed before the runs: the
residual improves systematically if none of whole-box N_f, N_f within 0.5 of P, N_v for r <= 1000, N_v for r > 1000 and
the 857-label J increases from one row to the next by more than the spread between the evaluation configurations. On the
independent evaluator (11250 x 384 and 16875 x 512; J at 16875 x 384) these are, for m <= 100, 150, 200: whole-box N_f
3.12e-6 / 3.11e-6, 1.42e-6 / 1.43e-6, 6.91e-7 / 6.84e-7 (the whole-box maximum lies within 0.5 of P except for m <= 200
at 11250 x 384, where the maximum within 0.5 of P is 6.51e-7); N_v for r <= 1000 (no evaluation column excluded) 8.73e-7
/ 8.74e-7, 3.98e-7 / 4.00e-7, 1.92e-7 / 1.92e-7; N_v for r > 1000 1.325e-6 / 1.325e-6, 1.10e-6 / 1.11e-6, 1.09e-6 /
1.10e-6; J 5.28e-6, 3.14e-6, 1.39e-6 (eps 0.03). Each decreases at both steps on both configurations: from m <= 100 to
150 by factors 0.46 to 0.63 (0.83 to 0.84 for N_v for r > 1000), from 150 to 200 by factors 0.44 to 0.49 except N_v for
r > 1000, which decreases by 1.26e-8 and 1.33e-8 (factor 0.99), about the configuration spreads (1.24e-8 and 1.17e-8).
That maximum is at 3.3e3 L, theta 1.541 for m <= 100 and next to the y-axis at 4.9e3 L for m <= 200 (4.5). The 375 x
m <= 100 fit has the same centre structure (identity c_l to 3.3e-9, h(P) - 1 2.6e-7 and 1.5e-8, a single zero of the
x-velocity on the axis at 8.60006, sampled).

The m <= 250 refinement row (X3 with the angular cap raised to 250, continued 20750 iterations at the fixed c_l; not a
candidate by the reading fixed before its run) is read at 16875 x 512, 16875 x 768 and 22500 x 512, with the ratio to X3
on the same configuration: whole-box N_f 5.38e-7, 9.82e-7, 5.41e-7 (0.79, 1.37, 0.79), N_f within 0.5 of P 2.41e-7,
2.95e-7, 2.26e-7 (0.35, 0.41, 0.33), N_v for r <= 1000 1.23e-7, 3.16e-7, 1.44e-7 (0.64, 1.27, 0.75), N_v for r > 1000
1.096e-6, 1.114e-6, 1.101e-6 (0.995, 1.003, 0.998), and J 5.00e-7 at eps 0.03 and 5.89e-7 at eps 0.01 (0.36 and 0.37;
16875 x 512). Its whole-box maxima on every configuration and its N_v maxima for r <= 1000 at 16875 x 768 and 22500 x
512 lie in the evaluation column next to the y-axis, and its increases over X3 at 16875 x 768 (2.7e-7 in N_f, 6.8e-8 in
N_v) are inside its own configuration spread (4.4e-7 and 1.9e-7), so the reading as fixed is met. In those columns the
values are the evaluator's floor, on X3 as on this row: on two angular resolutions they grow about like the inverse
square of the distance from the axis and change sign between the resolutions, while from distance 0.01 on the two agree
to 3 to 21 percent (to about 10 percent except next to a sign change of R at 0.013) at 1e-8 to 3e-8, which is 0.25 to
0.51 times X3's at the distances the two resolutions share (0.09 to 0.73 over all columns up to distance 0.039). With
the columns within 0.006 of the y-axis excluded, the whole-box N_f is 4.23e-7, 4.27e-7, 4.88e-7 (0.62, 0.60, 0.71; at
the lobe above P, r 8.72 to 8.74, theta 0.194, a maximum that moves with the radial sampling: 4.22e-7 to 4.66e-7 over
four radial sampling phases at 16875 x 512, where X3's lobe is 4.27e-7 to 4.74e-7, the same to 2 percent; 4.95e-7 for X3
at 22500 x 512) and N_v for r <= 1000 is 1.23e-7, 1.24e-7, 1.42e-7 (0.64, 0.62, 0.74). On that reading, whole-box N_f,
N_f within 0.5 of P, N_v for r <= 1000 and J decrease at each step of the row m <= 100, 150, 200, 250 on every
configuration, and N_v for r > 1000 rises at the last step by 2.5e-9 to 4.7e-9 (0.23 to 0.44 percent), more than the
spreads over these three configurations, 6.9e-10 and 2.2e-9, of the m <= 250 and m <= 200 rows (maximum at about 4800 L,
0.0065 to 0.0098 from the y-axis, on the first or second column beyond the cut). Along the row N_v for r > 1000 (ratios
on these three configurations over all evaluation columns 0.84 to 0.85, 0.98 to 0.99, 0.995 to 1.003 per step; at the
last step 1.002 to 1.004 with the columns next to the y-axis excluded) and the first-order far-field coefficient C at
the axis of 4.5 (0.944, 0.988, 0.998) level off: beyond r = 1000 the band is set by the far-field profile, which the
angular refinement leaves at X3's. The m <= 250 row is lower than the candidate in the interior and in J, and the
deliverable does not change. It is at the budget X3 + 20750 iterations, as is X3 continued on its own basis and rows
(4.2). At that budget, on the same three configurations, the m <= 250 row reads 0.97 to 1.00 times the budget row in
whole-box N_f and in N_v for r <= 1000 (columns within 0.006 of the y-axis excluded; for both rows the maximum is at the
lobe above P; in whole-box N_f 0.96 to 0.995 over four radial sampling phases at 16875 x 512), 0.63 to 0.82 within 0.5
of P, 1.001 to 1.002 in N_v for r > 1000 and 0.74 in J (0.82 at eps 0.01), and 0.38 to 0.54 in the bands 0.1 to 2, 10 to
100 and 100 to 1000 (16875 x 512). At the lobe above P the three rows agree to within 4 percent over four radial
sampling phases (the m <= 250 row 0.96 to 0.995 of the budget row, the budget row 0.98 to 1.02 of X3), so the whole-box
maxima of the m <= 250 row and of the budget row are the lobe value, which the further iterations do not lower and the
raised cap lowers by at most 4 percent; their whole-box ratios to X3 come from the fall next to P. Next to P and in the
bands away from P the raised cap lowers the residual further. These ratios at equal budget are stated without an
attribution threshold. Its free control (F3 enriched to m <= 250 and continued with c_l free for the same 20750
iterations; not a candidate) ends at c_l 5.5763706 (the free branch under the angular refinement: F2 5.5763709, F3
5.5763712, then 5.5763706). At m <= 250 and equal budget the free control and the fixed row agree in the whole-box and
r <= 1000 maxima to about 1 percent, with differences of both signs inside the configuration spread; the free control is
lower next to P (by 3 to 11 percent, inside the phase spread of that maximum) and beyond r = 1000 (by 0.1 to 0.4
percent); the fixed row is lower in the 857-label J (by 2 to 3 percent, beyond the spread of J between configurations).
By the selection rule the free control wins this pair on whole-box differences of about 1 percent, below the resolution
of that maximum. The pair is a refinement row and does not change the candidate. The centre values of the m <= 250 row
are X3's: the identity gives c_l 5.5753626074 (the fixed value 3.2e-9 above it, as for X3), h(P) - 1 is +3.2e-8 and
-1.8e-8 at 16875 and 22500 radial points (X3's to 1e-9; 5e-9 from the dense axis traces used for the identity-free root
of h(P) = 1 in 4.3), the x-velocity has a single zero on the axis at 8.600064, and the zero set passes the sampled check
of 4.2 (min |W| / (c_l |X|) 0.0216, 0.0067, 0.0023 at distance 1, 0.3, 0.1 from P). The m <= 250 row continued for 20750
iterations at the fixed c_l with rows to 9000 L and the inverse domain and closure at 1e4 L (a data row, not a
candidate; reading fixed before the run) reads 1.021 and 1.023 times the m <= 250 row in whole-box N_f for r <= 1000 and
0.665 and 0.712 within 0.5 of P (16875 x 512 and 22500 x 512), so the interior gain of the cap is kept with rows to 9000
L (the fall next to P mixes the further budget and the rows), and over 1000 L to 9000 L (formula continued) 0.608 and
0.610 times the 9000 L row continued for the same total iterations (4.5). The difference sits next to the y-axis at the
inner end of that band, where the 9000 L row continued has its maximum (3.29e-8 at 1070 L); the m <= 250 row continued
is at most 2.00e-8 in the band (in the fit convention at 22500 x 512 its largest value next to the y-axis, at 3944 L,
and its largest value away from it, at 8998 L and theta 0.62, agree to 3e-4), and over 9000 L to 1e4 L the ratio is
0.94. Against X3 it reads 0.234 and 0.235 within 0.5 of P and 0.631 and 0.730 in whole-box N_f for r <= 1000; it has
41500 iterations beyond X3, a larger cap and other rows, so this is not an equal-budget comparison.

### 4.4a P_2 consistency checks
For exact P_2 profiles, R5 and R6 give h(P) = 1 (C^(2,alpha) gives psi in C^(3,alpha)_loc, so W is C^2 near P; the local
form also needs rho_y(x,0) > 0 on (0, x*), which the axis equation of R10 supplies). For the trial, with rho = y g and
W_2 = y h near P, R/rho = h - 1 + W.grad log g off the axis; the right side is continuous across the x-axis (rho in
C^2, W in C^1, rho_y(P) > 0), and its value at P is h(P) - 1. So imposing h(P) = 1 enforces the source limit of the
normalized transport equation; near P, N_f is about 2|rho|, so a small N_f residual approaching P implies it. Values:
|h(P) - 1| = 2.8e-7, 3.1e-8 and 1.8e-8 on the candidate at 11250, 16875 and 22500 radial points, and 2.4e-7, 4.2e-8 and
1.9e-8 on its control, falling with the radial resolution of the evaluator (its grid error). These are consistency
checks of the trial, not accuracy bounds.

### 4.4b Characteristic defect
J_eps(X0) = int_{t_eps}^0 (R/rho)(Phi_t X0) dt along the backward characteristic of the trial's own W from X0 to the
cutoff |X - P| = eps. It is the logarithmic ratio log rho(X0) - log rho_tr,eps(X0), where rho_tr,eps(X0) = e^(-t_eps)
rho(Phi_{t_eps} X0) transports the trial's own density on the cutoff section by the frozen trial field W (e^J - 1 is the
difference relative to rho_tr,eps). Backward characteristics off the x-axis approach P along the slow vertical
eigendirection, and under Hoelder regularity J_eps = (h(P) - 1) log(1/eps)/h(P) + C(X0) + o(1) for each fixed off-axis
label; this O(1) is not uniform as labels approach the x-axis. The reported quantity is the spread of J_eps over a named
label set on r = 20: 737 angles uniform on [0.02, pi/2 - 0.02] (family A) and 60 angles at geometric distances 1e-4 to
0.02 from each axis (families B and C). On the candidate the 857-label spread is 1.388e-6 at eps = 0.03 and 1.602e-6 at
eps = 0.01 (family A: 1.341e-6 / 1.563e-6; family B 2.51e-7 / 2.55e-7; family C 7.23e-7 / 8.46e-7); on its control
1.481e-6 / 1.709e-6 (family A 1.432e-6 / 1.670e-6), ratio 0.937 / 0.937. Against X2 (3.143e-6 / 3.462e-6) the ratio is
0.44 / 0.46; it is below 1 on every family (A 0.43 / 0.45, B 0.39 / 0.39, C 0.51 / 0.54). On the candidate the 857-label
spread is estimated, from the sampled labels and their parabolic refinement, to equal the supremum minus the infimum of
J_eps over all labels on r = 20 at distance at least 1e-4 from the axes to about 1e-8 (at 16875 x 384; a parabola
through the sampled maximum and its neighbours peaks 5e-10 above it; the 369-label subset of family A used earlier gives
a spread 0.5 percent lower), and on earlier fits to about 2e-8. Closer to the y-axis J_eps grows like (3
c_l - psi_xy(0) - 1) log(1/d)/(2 c_l - 1), 9.6e-10 per factor e in the distance d from the axis (3
c_l - psi_xy(0) - 1 = 9.8e-9 on the candidate), and by the leading logarithmic term leaves the sampled range only for d
below e^(-1190). The spread removes the common logarithmic term but does not measure a transport error common to all
labels. At |h(P) - 1| of 3.1e-8 and 1.8e-8 on the two finer grids the logarithmic term is below 1.5e-7 at eps = 0.01. On
the candidate and on its control the 857-label maximum is at the family-A label theta0 1.520 (r_min 2.1), whose J
(8.2e-7 at eps 0.03) comes almost all from the disk |X - P| < 0.5. The minimum is at the family-B label theta0 1.555
(r_min 0.93), with J -5.7e-7 from the strip next to the x-axis and that disk in about equal parts. The labels within
about 1e-3 of the y-axis, whose characteristics follow the separatrix (down the y-axis, past the origin, along the
x-axis to P), have J -3.21e-7 to -3.24e-7, close to the axis integral I(0.03) below; farther from the axis family B
decreases monotonically to that minimum, at distance 0.015 from the y-axis. On the 375 x m <= 100 free fit and on X1 the
oscillation of J across family A is carried by angular frequencies at and above the cap; on F1 it is not. On X3 and F3
the residual in the band of angular frequencies 400 to 600 in the strip r 7.0 to 8.3 next to the x-axis is about 3.4
times smaller than on X2. Axis. On the x-axis between the origin and P, rho = 0 and W_2 = 0, and R/rho has an even
continuous limit q0(x); a label on the separatrix gains I(eps) = int_{0.01}^{x* - eps} q0(x)/|W_1(x, 0)| dx on the axis,
a label-free companion of the spread. On X3, I(0.03) = -3.30e-7 and I(0.01) = -4.13e-7 (independent evaluator; lead
-3.40e-7 and -4.04e-7; X2: -6.36e-7, -7.85e-7, independent evaluator); max |q0| = 1.29e-6 at x 6.64 (independent
evaluator; lead 1.33e-6 at x 6.67; X2 3.13e-6 at x 2.80); lead profile of X3: q0 = 3.8e-7 at x 1, 1.07e-6 at 2, 1.19e-6
at 3, 5.7e-7 at 4, -4.3e-7 at 5, -1.17e-6 at 6, -1.30e-6 at 7, -1.04e-6 at 8. |q0| is 0.99e-6 to 1.07e-6 on [8, 8.53]
(1.02e-6 to 1.07e-6 on [8, 8.49]), with its maximum on [8, x*) 1.07e-6 at x 8.36; beyond 8.53 it decreases, with the
ripple, to 9.5e-7 at 8.56, 7.1e-7 at 8.59 and 3.6e-7 at 8.595, the last evaluation node before x*; q0 is negative on
[7.5, x*) with no sign change (independent evaluator, at 33750 radial points, by the spectral axis value, which the
Richardson sequence approaches to 1.8e-8). It is the axis value of the residual ripple at the angular cap frequency
(carried by angular frequencies up to 600); the smooth part next to the axis is about 5e-8. On F3: I(0.03) = -3.51e-7
(independent evaluator; lead -3.61e-7), max |q0| 1.32e-6 (independent evaluator; lead 1.37e-6 at x 6.66). The long
continuation from X1 lowered q0 between the origin and x 5 by a factor 3 at m <= 150 (X1: max |q0| 1.07e-5 at x 3.57,
I(0.03) +2.04e-6), and the cap 200 by a further factor about 2.7 on [0, 5] (max |q0| there 1.16e-6 at x 3 on X3 against
3.13e-6 at x 2.80 on X2; 2.4 for the maxima over the whole segment). So R/rho on the axis segment between the origin and
P reaches 1.3e-6 on the candidate. N_f and N_v are both at least |rho| (each is |rho| plus nonnegative terms), so the
tables above show the same residual at a smaller size next to the axis; R/rho itself enters the report only through
J_eps, I(eps) and q0.

### 4.5 Far field and nonlocal inverse
Far field: the residual for r > 1000 is at most 1.324e-7 in N_f (at r 3.3e4, theta 0.84) and 1.112e-6 in N_v, with the
N_v maximum next to the y-axis at r 3.6e4 to 3.7e4, beyond the inverse domain, where the formula's far-field model (4.2)
is in force and the candidate has no fit rows; inside the inverse domain (1000 <= r <= 7652, that is 1000 L) N_v is at
most 2.15e-7 / 2.18e-7 (11250 x 384 / 16875 x 512). Next to the y-axis in the far field the residual is a residual of
the fit, not the evaluator's floor: on the axis column itself |R| is at most 8.9e-9, and over the first columns off the
axis the N_v maxima are 1.111e-6, 1.096e-6, 1.082e-6, 1.077e-6, 1.073e-6, 1.073e-6, a smooth profile flat to 4 percent
(on X2, R and N_v were measured to grow together as (pi/2 - theta)^2 over those columns). Beyond the fit rows the band
is hardly moved by any fit: without the column exclusion F0, X1, F1r, X2, F2, X3, F3 and the reorthogonalized arm of 4.2
read 1.08e-6 to 1.17e-6 there, F1 1.46e-6 to 1.47e-6 and W1 1.28e-6 to 1.31e-6. These fits have rows only to 900 L
(4.2). The 9000 L domain row of 4.4 (X3 continued for 20750 iterations at its c_l with rows to 9000 L, inverse domain
and two-term closure at 1e4 L; not a candidate) tests the band. Its N_v maximum over 1000 L < r <= 9000 L is 3.20e-8 /
3.04e-8 (16875 x 512 / 22500 x 384), 0.029 / 0.028 of X3's on the same configurations, at 1013 L and 1026 L near the
y-axis (theta 1.563 and 1.548), and over 9000 L < r <= 1e4 L it is 2.40e-8 / 2.41e-8 (0.025) at theta 0.62. Beyond 1e4
L, where it has no rows, its own two-term closure reads 2.3e-5 next to the y-axis at 2.3e4 L (the closure regions of the
300 L and 90 L fits read 5.1e-3 and 2.8e-2, also next to the y-axis), and the formula continued instead reads 3.28e-8
(0.035 of X3's, at 2.2e4 L, theta 0.62). With the formula continued its whole-box N_v maximum is in the interior,
1.256e-7 / 1.435e-7. Its interior is that of 4.4 (2-10 ratios 1.02, 0.66, 0.74; within 0.5 of P 0.66 to 0.68 times
X3's). So X3's far-band value is that of the unfitted continuation of its formula, and continuing X3 with rows to 9000 L
lowers it over 1000 L to 9000 L by the factor 0.028 to 0.029 (the rows, the larger inverse domain with its closure and
the further iterations together). Its equal-budget free control (F3 continued in the same way with c_l free; a data row,
not a candidate) moves c_l by -1.5e-6 in the 20750 iterations and reads 0.029 to 0.030 of F3's over 1000 L to 9000 L;
the 9000 L row's far bands are within 4 percent of it, and the 9000 L row is 0.93 to 0.94 times it within 0.5 of P and
in J, as X3 is against F3. The 9000 L row continued for a further 20750 iterations at its c_l on the same rows and
domain (a data row, not a candidate; reading fixed before the run: ratios in [0.8, 1.25] on both configurations mean
that the budget does not lower the band further, ratios of at most 0.5 that it falls further with the iterations) reads
1.028 and 1.024 of the 9000 L row's values over 1000 L to 9000 L (16875 x 512 and 22500 x 384) and 1.015 in C at the
axis, so the further budget does not lower its far band; within 0.5 of P it reads 0.612 and 0.578 and in J 0.579 (857
labels, eps 0.03, at 16875 x 384) of the 9000 L row's. Against X3 it reads 0.401 and 0.395 within 0.5 of P and 0.645 and
0.756 in whole-box N_f for r <= 1000 (on the same configurations) and 0.380 in J (eps 0.03); it has 41500 iterations
beyond X3, on other rows, so this is not an equal-budget comparison. X3 continued for 20750 iterations on its own rows
reads 0.993 to 1.003 of X3's over 1000 L to 9000 L and 1.0026 of X3's C at the axis. X3 continued for the same
iterations on its own rows with the inverse domain and two-term closure moved to 1e4 L (not a candidate) separates the
other two: the larger inverse domain with its closure, at the same rows and iterations, lowers the band to 0.27 of X3's
(0.266 to 0.273 on the two configurations, with and without the y-axis columns) and removes C at the axis (-0.024 of
X3's); the rows to 9000 L lower it by a further factor of 9 to 10 (the 9000 L row reads 0.10 to 0.11 of this
continuation there); C at the axis is already removed by the inverse domain (-0.024 against 0.035 for the 9000 L row).
Its interior is that of the budget row (same rows and iterations, inverse domain at 1000 L) to 2 percent in the
whole-box maximum and within 0.5 of P and to 8 percent in J (0.89 at 10 <= r <= 100 on one configuration). So the
further iterations alone do not move the band, and the fall of the 9000 L row is not attributable to its rows alone.
Under a termwise differentiable far-field expansion rho = r^k Theta_0 (1 + r^(k-1) Theta_1 + ...) (formal; a compact
change of the core adds multipoles that enter only at relative order r^(-4)), the equation determines Theta_1 from
Theta_0: with psi = r^(k+1) F the homogeneous inverse of r^k Theta_0, (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k
F' Theta_0, and on the y-axis Theta_1 = -(k+2) V_r/(c_l - 1), V_r = -F'. The formula's Theta_1 is set instead by the end
slopes of its radial splines (4.2). On X3 the two differ by 4.08e-3 on the y-axis (-42.5561 against the forced -42.5520,
computed three times independently) and by at most 7.9e-4 for theta < 1.4 (between 1.4 and pi/2 the difference rises to
the axis value); on the seven fits measured the axis difference is 4.07e-3 to 4.31e-3 and the maximum for theta < 1.4 is
7.0e-4 to 1.44e-3. This term alone gives R / N_v -> C r^(k-1) / (1+k) with C = (c_l - 1)(Theta_1 forced - Theta_1 of the
formula) = 0.0187 on the axis, 2.9e-6 at the band maximum, where the measured value is 1.1e-6 with the same sign. The
expansion of the trial to third order, computed three times independently and agreeing to 4 digits or more, gives next
to the y-axis (theta 1.568)
    R / N_v = 0.01582 delta - 88.78 delta^2 + 782.1 r^(-2) + 1.190e5 delta^3 + ...,   delta = r^(k-1);
these four terms give 1.26e-6 at 4700 L and 0.965e-6 at 9500 L against the measured 1.09e-6 and 0.945e-6 (measured /
series 0.59, 0.87, 0.98 at 3000, 4700, 9500 L; inside 2000 L the series is of no use). With the trial's velocity
computed to 1e7 L, the measured R / N_v from 3e4 L to 3e6 L equals the series plus the constant (c_l
k - 1)/(1+k) = -5.2e-10 (c_l the identity value of that inverse) to 1e-3 relative, next to the y-axis and at theta 0.82
(on the verifier's evaluator, which resolves this to about 1e5 L, to 2e-3 at 3e4 and 1e5 L); next to the axis its ratio
to the leading term is 0.92 at 1e5 L and 0.97 to 0.98 at 5e5 L (on the verifier's evaluator on the column 1.5634; its
columns within 0.006 of the axis are not resolved there), as predicted before those radii were evaluated. Off the axis
the ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns toward 1 slowly (1.05 to 1.08 at 5e5 L
with c_l = 1/k). So the band is the sum of inconsistencies of the trial's far field at first, second and third order
(1e-4 relative in Theta_1; next to the y-axis, where the band maximum lies, 0.9 percent of the balancing terms at second
order and 22 percent at third order) and of the r^(-2) terms of 4.2, which are fixed by k, L and the end values b_m(1),
T(1), so that no choice of the end slopes removes them. Next to the y-axis the first- and second-order terms cancel at
the band maximum (2.81e-6 and -2.80e-6 at 4860 L), where the r^(-2) and the third-order terms give 5.7e-7 and 6.7e-7 of
the series sum 1.24e-6 (measured 1.10e-6); all four decay at infinity, the first-order one slowest. The inconsistencies
are common to the fits with rows to 900 L and the inverse domain at 1000 L (at second and third order 0.88 to 0.92
percent and 22 to 23 percent next to the y-axis on six fits); on the 900 L rows with the inverse domain at 1e4 L (C
-0.024 of X3's) they are 2.6e-6, 0.10 percent and 13 percent at orders 1, 2, 3. On the 9000 L domain row C at the axis
is 6.5e-4, 0.035 of X3's (V_r(pi/2) is unchanged, so the formula's Theta_1 moved toward the forced one), and the
inconsistencies at orders 1, 2, 3 next to the y-axis are 3.0e-6, 0.15 percent and 10 percent; its r^(-2) term is X3's,
its second-order coefficient 0.17 of X3's and its third-order coefficient of the opposite sign. At 4858 L next to the
y-axis its four terms (8.8e-8, -4.6e-7, 5.7e-7, -1.9e-7) sum to -2.5e-9, and on six columns within 0.072 of the y-axis
its measured R / N_v at 1000 L and 4701 L is -0.29 to +0.04 times its own first-order term (-0.30 to +0.15 over 11-node
radial windows around those radii; separate evaluator, formula continued): its band value is set by the higher orders,
and its fall is not the removal of the first-order term alone. So the 900 L fits' band value is not a floor of the
family; whether the remaining inconsistencies are is not established. The weighted identity R8 with phi = sin(3 theta)
r^(-3) holds on the candidate and on its control to a relative defect of 1.4e-9, and its integrand per unit log r decays
with the exponent 2k - 2 = -1.6413 of the far-field model (slope -1.64136 over the last decade, deviation 8e-5; the
decade deviations fall by the factor 10^(1-k) of the relative r^(k-1) correction). Inverse. At 52 sample points the
velocity of X1 (lead modal inverse on r <= 76520 with the two-term exterior) differs from the canonical inverse of X1's
density, computed by a third evaluator by real-space quadrature of the analytic source to |Y| = 1e18 (quadrature rules
clustered at P), by 8.4e-10 within 0.5 of P, 4.0e-8 within 0.5 to 2.5 of P, 6e-12, 5e-11, 1.0e-9, 4.6e-9 and 1.4e-8 at
r = 0.1, 1, 20, 100 and 300. The implied change of the normalized residual is at most 6.3e-10 within 0.5 of P and 2.8e-9
at 0.5 to 2.5 from P (median over the points 2.8e-11), against X1's residual maxima within 0.5 of P of 6.8e-7 (N_f) and
1.9e-7 (N_v). The same check on the free fit with 375 x m <= 100 functions (51 points, converged across three angular
rules and two ray rules, and confirmed at three points by a separately written modal inverse of an external referee)
gave the same pattern: 9e-10, 4e-8, 1e-9, 5e-9 and 1.5e-8 in the same regions and at most 3e-9 in the normalized
residual. "Converged" at r >= 100 means that the quadrature rules clustered at P agree with a 16384-angle midpoint rule.
These are sampled comparisons, not uniform bounds. X1 has the radial basis and c_l of the candidate and a lower angular
cap. The same check on the candidate X3 (52 points, the same export convention and quadrature rules) gives 1.0e-9 within
0.5 of P, 3.6e-8 at 0.5 to 2.5 from P, 7.7e-12, 5.1e-11, 9.8e-10, 4.9e-9 and 1.5e-8 at r = 0.1, 1, 20, 100 and 300; the
implied change of the normalized residual is at most 8.6e-10 within 0.5 of P and 2.6e-9 at 0.5 to 2.5 from P (median
2.7e-11), against X3's residual maxima within 0.5 of P of 6.5e-7 to 7.2e-7 (N_f) and 1.8e-7 to 2.0e-7 (N_v) (4.4). The
fit's own velocity (the inverse on r <= 1000 L with the two-term closure beyond) changes X1's residual by at most 5.1e-9
in N_f within 0.5 of P and 2.0e-8 in N_v for r < 1000, and X3's by the same to two digits (grid maxima; 4.4); at the 52
sampled points of X3 the same replacement changes the velocity componentwise by at most 9.2e-8 within 2.5 of P and
3.1e-6 at r = 300, with a frozen-denominator impact of at most 2.0e-9 within 0.5 of P, 3.1e-9 at 0.5 to 2.5 from P and
1.4e-8 at r = 20 to 300. Manufactured test of the separate evaluator: on rho = x^2 y e^(-r^2) with its closed-form
stream function and c_l = 1.3 (an arbitrary value) it gives max |R - R_exact| = 6.8e-10, 2.7e-12 and 2.8e-13 at 400, 800
and 1600 radial points (max |R_exact| = 0.485), max |E| at most 1e-10 and psi_xy(0) - 1/8 = -6e-14. The residuals of 4.3
and 4.4, except the domain columns read in each fit's own convention (4.4), are canonical residuals of the trial: the
verifier's evaluator generates rho from the formula and inverts it to 1e6 L.

### 4.6 Independent discretization
An independent discretization (polar Chebyshev-Radau x Fourier on a disk r <= R with the homogeneous far-field
extension, oversampled least squares with exact Jacobian and QR steps, c_l eliminated through the identity) did not
reach the standard. Its full-plane inverse was validated against the compactified Poisson inverse of the same workstream
(itself exact to 3.4e-15 in the rescaled stream function and 2.1e-14 in the velocity on the manufactured psi = x y (1 +
r^2/L^2)^((gamma-1)/2) (1 + 0.7 (x^2 - y^2)/(1 + r^2)), gamma = 0.6, L = 1.3, with N = 128 radial and 16 angular nodes
per quadrant): relative velocity difference on r <= 5 of 1.0e-6, 5.3e-8 and 2.2e-9 at R = 100, 300 and 1000, psi_xy(0)
to 3e-7, 2e-8 and 7e-10; its Jacobian agrees with finite differences to 5e-9 to 4e-7 relative per column. Between its
nodes its states satisfy the profile equation to a normalized residual of about 1e-6 rms away from P in its own
normalization; on the separate evaluator the maxima at 10 < r < 100 are 3e-5 to 6e-5 in N_v (4e-5 in N_f) for its free
iterates and 1.1e-5 to 1.2e-5 in N_v (6e-6 to 7e-6 in N_f) for its fixed-c_l states. Next to P its maxima are 9e-6 to
1.2e-4 in its own normalization (shell rms 3e-6 to 2e-5). The grids go up to 384 x 96 (unclustered) and 256 x 128
(clustered at P). At that level c_l is weakly constrained. The least first-order residual cost of a unit change of c_l
is 1e-3 to 6e-5, falling with resolution faster than the residual floor. On the clustered 256 x 64 grid, over 5.52 to
5.71 no fixed-c_l fit is worse than the one at 5.5763 by more than a factor 1.5 in its L2 residual or 1.3 in its near-P
maximum, and those above 5.5763 are better (near-P maxima from 3.0e-5 to 8.7e-6 across the range); its L2 residual is
flat to 20 percent over 5.556 to 5.596 and over 5.60 to 5.70. On the unclustered 320 x 80 grid the L2 minimum is near
5.575 and the fit at 5.68 is 25 percent worse; on the clustered 256 x 128 grid the L2 residual falls by 19 percent from
5.556 to 5.596. The discrete L2 minimizer moves by about 0.06 between grids, the zero of h(P) - 1 by 0.1 to more than
0.16. Free iterations, which use different weights and domains and are not one constrained family, drift between 5.29
and 5.59. Extra rows (h(P) = 1, characteristic matching, axis transport, a Taylor patch at P) do not change this.
Levenberg-Marquardt solves of its equations (identity row, c_l free), started from an early trial of the global trial
construction (c_l 5.5763) projected onto its grids, end at c_l between 5.5728 and 5.5823 on grids 128 x 32 to 320 x 80
with R = 1000 to 10000 (one run at R = 30000, marked unreliable there for its radial resolution, is not included),
without convergence under refinement; this is a variant spread, not an error bound. That workstream attributes the
spread to a nearly free far-field direction; the attribution rests on one singular-value computation of that workstream
and is not independently verified. The Gauss-Newton tangent prediction of the exponent step and its residual projection
diminish across the tested discretizations (+0.42 and 26 percent, +0.052 and 18 percent, +0.034 and 5 percent, at near-P
maxima 4.7e-5, 2.4e-5, 1.5e-5). This is a tangent prediction, not a stationarity test, and the nonlinear preferred
exponent of that discretization is grid dependent at the attained residual level. Its exported soft direction, added to
the 302-function trial along a fixed, unrefitted line that is linear in rho, is registered at offsets of 1e-3
(characteristic defect) to a few 1e-3 (near-P maximum). These are upper bounds on the cost of the offset, and the line
is a first-order statement beyond 1e-3. The result is a resolution statement: a least-squares residual of 1e-5 to 5e-5
next to P does not fix c_l to better than about 0.05 to 0.1 in that discretization. It neither establishes a competing
profile nor excludes one near 5.60 to 5.64, and it does not independently confirm the candidate's c_l nor its field at
the 1e-6 level. Its fixed-c_l states at 5.556 to 5.596 include the candidate's 5.5754 and its control's 5.5764 and do
not discriminate between them.

### 4.7 Adversarial checks
Hidden wall conditions: none (full-plane modal Green function, checked against (V2) and a real-space quadrature).
Harmonic gauge: excluded by (V3); c = psi_xy(0) is computed, not fitted. Parity: by construction, machine precision. The
x^2 y jet: a(0) = 1 by construction; centre relations (relative |E_c|, |D2| <= 6e-9 on the candidate, 4.2). Zero state:
excluded by a(0) = 1. Polynomial states: every polynomial density of the normalized class has total degree d >= 3, and
its supremum over the circle |X| = r is comparable to r^d, so it violates the bound |rho| <= C (1 + |X|)^(1/c_l),
1/c_l < 1, of R2; the trial has the leading homogeneous degree k = 1/c_l = 0.179 (4.2). Forgotten far-field terms: the
residuals are those of the canonical velocity of the trial density inverted to 1e6 L (4.4); the far-field residual
beyond the fit rows is measured and expanded term by term in 4.5, and the fits' two-term exterior closure is compared
with the formula continued in 4.4. Finite-box artifacts: the domain columns of 4.4 (closed problems on smaller and
larger fit domains, each with a further iteration budget, and the same fits read under the canonical law) and the
far-field and inverse checks of 4.5. Independence of c_l: 4.3.

### 4.8 Limits
Numerical evidence only. The residual values are maxima over sampled grids, not certified suprema. Neither the existence
of a nearby exact P_2 profile, nor its two-dimensional regularity class, nor a nonzero B_3 for it has been proved.
Residual tests cannot decide B_3; the B_3 value is an estimator value on approximate profiles of one lineage. Two
measurements of B_3 on the trial differ: the estimator from its axis data gives about 0.30, and the trial's own
coefficient of y^3 |x|^(p_3) is +0.046 (4.1); the difference is carried by the trial's defects in the y and y^3
coefficients of the equation on the x-axis, so the trial's own fractional term (+0.046) is about one sixth of the value
its axis data indicate. Both are positive. The trial's own regularity (H and a in C^(4,beta)_loc, rho_h in
C^(6,beta)_loc) follows from its explicit formula (4.1). Every fit has a sharp change of the third derivative of log a
across the characteristic leaving P (about +0.12 at P by separate polynomial fits on each side, changing sign near
height y = 0.5 and reaching about -0.4 at y = 1; on the candidate, its control and X1 by one estimator: +0.11 to +0.12
at P, -0.43 to -0.35 at y = 1; on earlier fits other estimators gave 0.05 to 0.16 at P). The fits are C^6, so this does
not show that a solution fails to be C^3. Under a conormal expansion along that characteristic with a nonzero linear
onset of the amplitude at the axis, a nonzero layer |x - gamma(y)|^lambda has exponent lambda = rho_y(P)/(2 c_l - 1),
about 2.93, and transverse regularity C^(2, lambda - 2), but no finite third-derivative jump (its third derivative
behaves like |x - gamma(y)|^(lambda - 3)). By an external referee's computation, not re-derived by the verifier, on a
regular positive branch its two amplitudes share a positive transport multiplier, so the nonzero leading layer
coefficient seen by a fixed estimator keeps its sign. The observed finite-window sign change does not establish such a
leading coefficient and does not exclude a layer in an exact solution; whether a solution has one is open, and all fits
share one lineage. The candidate was selected by rules that compare residual maxima of fits (rule (1) within
equal-budget pairs, rule (2) across the kept fits, which are at different budgets). In N_f the maximum sits next to P;
in N_v it sits in the far field beyond the inverse domain, where the fits with rows only to 900 L listed in 4.5, other
than F1 and W1, read 1.08e-6 to 1.17e-6; the domain row fitted to 9000 L reads 3.0e-8 to 3.2e-8 over 1000 L to 9000 L
(4.5). The ratios of the pair X3 / F3 read by the selection rule are 0.935 to 0.938 in whole-box N_f, 0.937 in J, 0.935
to 0.987 in N_v for r <= 1000 (y-axis floor columns excluded in N_f and N_v; without the exclusion 0.83 and 0.825 at
16875 x 768), 0.960 to 0.973 in L2 and 1.000 to 1.003 in the far field. X3 is limited by its iteration budget: continued
on its own rows for a further 20750 iterations it reads 0.61 to 0.74 in whole-box N_f, 0.50 to 0.54 within 0.5 of P and
0.48 in J (4.2), and at that budget the m <= 250 row reads 0.97 to 1.00 in whole-box N_f (both maxima are the lobe value
above P, common to X3 and the two rows within 4 percent over four radial sampling phases), 0.63 to 0.82 within 0.5 of P
and 0.74 in J of that continuation (4.4); beyond r = 1000 neither changes N_v by more than 1 percent. So its maxima are
values reached at that budget and cap, not converged values for the basis. X1 has a maximum next to P 4 to 6 percent
below the candidate's at 16875 radial points and equal to it at 22500, with N_v for r <= 1000 2.8 times and J twice the
candidate's. So the choice of the representative value inside the interval depends on the norm, on the band and on the
iteration budget, not on a property of the equation. On the m <= 150 basis the fixed-c_l fits below X2's c_l down to
5.5604082 have smaller L2 objectives and residual maxima than X2 at the same budget, the fit at 5.5524653 a smaller L2
objective but larger residual maxima, and the fit at 5.5683739 has whole-box and near-P maxima below the candidate's at
16875 x 512 (4.1) although its angular cap is lower. The requirement of the standard that c_l be stable holds for the
fitted values along each construction (the free c_l moves by less than 1e-5 over 20750 iterations), not for the exponent
of an exact profile: at equal budget, from transplanted starts, the L2 objective is least at 5.5604082 among the tested
exponents and the residual maxima at 5.5683739. A test fixed before the run at 5.6004662 was to separate two pictures: a
family of P_2 profiles through the free fit parametrized by c_l, and one isolated profile whose linearized operator has
a small singular value in the c_l direction at the resolutions used. Its ratio of objectives to F2 (2.036) would have
favoured the second picture at 2.96 or more and the first at 0.91 or less (thresholds from the ratios 1.97 and 1.36 of
the 244-function fit at 5.60 to its free fit); it does not separate them. At the attained resolution the residual pins
c_l only weakly; whether P_2 contains a family through the candidate or an isolated profile is open. One refinement step
of the experiment that would separate the two was done: the fits at 5.6004662 and 5.5683739 were continued from the
m <= 150 basis to the candidate's m <= 200 basis as X2 was continued to the candidate (4.3). By a rule fixed before the
runs, the ratio Q of the objective at 5.6004662 to F3's would have favoured the second picture at 3.05 or more (1.5
times its ratio 2.036 on m <= 150) and the first at 1.36 or less (2.036 / 1.5), provided the fit had flattened; it is
1.680, between the thresholds, so this step does not separate them either; the rule assigns no reading between the
thresholds, and the decrease from 2.036 to 1.680, one step, is read neither as evidence for either picture nor as a
trend. At 5.5683739 the continued fit, at the candidate's iteration count, has a smaller L2 objective than the candidate
(ratio 0.820, against 0.771 for the same fit to X2 on m <= 150), a smaller N_f within 0.5 of P (0.59 times on both
configurations) and a smaller J (0.56 and 0.55 times at eps 0.03 and 0.01); its whole-box N_f is 1.32 times the
candidate's at 11250 x 384, at the under-resolved off-axis lobe, and 0.69 times at 16875 x 512 (4.1, 4.3). Further steps
(more nested discretizations at several separated exponents, budgets large enough to estimate the optimization error)
were not done (section 5).

## 5. Reproducibility
The accompanying artifacts of sections 4 and 5 are those of the first investigation; the accompanying artifacts of the follow-up (section 6) are separate (6.0). The first investigation's accompanying artifacts are arranged in six parts, (a) to (f). Their guide maps the fits used here (X1, X2, X3, F0 to F3, the rows of 4.3 to 4.5) to the coefficient data and gives the exact commands. The accompanying artifacts also retain the original command recipes; below, programs are described by purpose and their arguments are retained. The records of the research run
itself (work logs, job drivers and queues, per-run solver logs) are not included.
(a) Trial coefficient files. One file per trial named in section 4: the candidate X3 and every fit of the tables of 4.3
    (the nested pair included), the free fit of the same trial space, the resolution rows at the candidate's c_l, the
    free resolution study (215, 244, 302, 375 radial functions with m <= 100, 375 with m <= 150), the soft-direction and
    fixed-c_l studies (with the two continued fits of the fixed-c_l profile, 4.3), the budget row, the m <= 250 row, its
    free control and its continuation with rows to 9000 L (4.4), X3 continued with the inverse domain at 1e4 L (4.5),
    and the bounded-domain fits with the free control of the 9000 L row and the 9000 L row continued (4.4, 4.5). The
    candidate X3 has coefficient data in the accompanying artifacts (md5 15f8095f7e79dbfa0c50d75e5fe8997a) and its control F3 has coefficient data there (md5
    0398af3f08a2a4f75e42c846edbaa375). A file holds the spline knots and order, the coefficient of every
    radial x angular function, the fractional-power coefficients, k = 1/c_l, L, c_l and the origin radius. The files of
    the candidate, its control, X2, F2, F0, F1, X1 and the start of X1 are the verified files byte for byte; in the
    other files a solver restart vector that no evaluator reads was removed for size, every other field unchanged (the
    md5 of each file as published and as verified is listed with them). Start files of continued fits are not included:
    the m <= 200 starts are the m <= 150 ends with the new angular coefficients set to zero, and the shifted starts are
    made by the transplant scripts of (b). The generator that evaluates rho, psi, U and the residuals from a
    coefficient file is in the same part.
(b) The fit: the Gauss-Newton / LSQR solvers (free and fixed-c_l), the GPU driver and the scan and export programs.
    The solvers log the objective, c_l, h(P), x*, centre jet E_c and D2 at each check; these run logs are not included.
    The fits X2, F2, X3, F3, the m <= 100 rows, the domain columns, the free control of the 9000 L row and the 9000 L
    row continued (4.5), the budget row, the m <= 250 row, its free control and its continuation with rows to 9000 L
    (4.4), X3 continued with the inverse domain at 1e4 L (4.5), the fixed-c_l profile with its two continued fits and
    the nested pair of 4.3 were computed with the same iteration, and the solver-setting arms of 4.2 with their stated
    changes, with the matrix-vector products, the vector updates of LSQR and the column-scaling probes carried out on a
    GPU, the products by a port of the CPU operator. Every table of the port is copied from the CPU objects. On the full
    fit grid it agrees with the CPU operator to 3e-14 relative in the products and 1e-13 in the adjoint products. The
    linearization, the acceptance test at each check (the CPU objective) and the saved coefficient files use the CPU
    code. Started from the same shape, the first linearization reproduced the CPU objective to 5e-5 relative after 250
    iterations. LSQR paths differ at the 1e-4 level after hundreds of iterations, so "equal budget" means equal
    iteration counts at the same relinearization schedule on the same backend (on the GPU 2500 iterations per
    linearization, damping 1e-8, check every 250), with two departures. On the CPU X1 ran 750 iterations over two
    linearizations (500 + 250) and F1 750 iterations in one linearization (--inner 2500), both stopped by the 1.8 h cap;
    the pairs X1 / F1, and through their starts X2 / F2 and X3 / F3, are therefore equal in iteration count but differ
    in the relinearization schedule of their first 750 iterations. The fits of the fixed-c_l profile of 4.3 are compared
    with X2 and F2 at equal total count: each runs 21500 iterations on the GPU, while X2 and F2 are the 750 CPU
    iterations of X1 and F1 followed by 20750 on the GPU. The CPU logs record under "predicted" the LSQR estimate
    |phibar|, which omits the damping term. The linear residual of the damped problem is sqrt(phibar^2 + res2), with
    res2 the sum of the squared damping rotations; the GPU logs record that value for every run from F2 on (the log of
    X2 has |phibar| only). The acceptance test always used the true objective. In each linearization the three long-fit
    drivers (free, fixed-c_l and GPU, in the accompanying artifacts) scale the LSQR columns by the inverse square root
    of a stochastic estimate of the squared column norms of the Jacobian from 24 Rademacher probe vectors (seed 8128
    plus the linearization count); a column whose estimate is below 1e-18 of the largest gets scale 0 and is not moved
    in that linearization, and with c_l held fixed the column of k = 1/c_l gets scale 0 in every linearization. Every
    residual quoted is evaluated from the saved files by the evaluators of (c) and (d).
(c) The lead's between-node evaluation (scans by radial band and strip, both normalizations; the scan program is with the fit code of (b) in the accompanying artifacts), the characteristic-defect code and the original-form B_3 evaluator, with
    their outputs for every trial of (a) (the larger outputs xz-compressed); and the far-field diagnostic of 4.5 (the
    forced and the stored first far-field correction from a coefficient file, on seven fits and on the domain fit with
    rows to 9000 L, with its outputs).
(d) The separately written generator and residual evaluator (own differentiation, own full-plane inverse), its audit
    wrappers and auxiliary scripts, the far-field checks of 4.5 in the accompanying artifacts, the reference
    outputs of steps 1 and 2 below on the candidate (the reference outputs in the accompanying artifacts), and the verification record that the appendix
    summarizes, copied after its last entry.
(e) The independent discretization of 4.6: solver, report; and the velocity check of 4.5 by real-space quadrature of the
    analytic source (52 sample points), with its outputs.
(f) The specification of the problem classes and diagnostics, the analysis notes behind section 3 with their audit
    record, and the external referee questions and answers (including the answer on the far-field identity of 4.5).

Reproduction of the headline numbers. All commands are single-threaded on the CPU (OMP_NUM_THREADS=1; the GPU driver of
step 5 also uses one GPU), with the software versions of section 0 (Python 3.9.25, numpy 2.0.2, scipy 1.13.1, and
PyTorch 2.8.0 for the GPU driver); the times are on one core of the machine used for the run. The wrappers of steps 1
and 2 stop a step after 2400 s (residual-table wrapper) or 1200 s (identity, trace and zero checks), so a slower machine may need larger limits. Peak resident memory of the commands of steps 1 to 3 on
the candidate: 13.8 GiB for the residual-table wrapper at 16875 x 768, the configuration with the most evaluation points (12.3 GiB at
22500 x 512, 9.2 GiB at 16875 x 512 and at 22500 x 384, 7.0 GiB at 16875 x 384, 4.7 GiB at 11250 x 384), and at most 7.5
GiB for each command of steps 2 and 3. They ran under an address-space limit of 15.3 GiB (ulimit -v 16000000), and every
output for which an earlier one exists equals it in every number (file names and timings aside): for steps 1 and 2 the
earlier outputs are the reference outputs in part (d) of the accompanying artifacts, for step 3 they are the candidate's scan files in (c). Step 1 at
16875 x 384, which section 4 does not use, had no earlier output; the reference outputs in the accompanying artifacts include the one from this measurement.
<coef> is a coefficient file from (a), <tag> any label. The exact executable commands and working-directory instructions are in the accompanying artifacts; the lines below specify arguments.
1. Residual tables of 4.4 by the separate evaluator (maxima of R/N_f and R/N_v by region, J, h(P) - 1), using the evaluator in part (d) of the accompanying artifacts:
     Residual-table wrapper arguments (accompanying artifacts): <coef> <tag> "7.652e-4 7.652e6 11250 384 479;7.652e-4 7.652e6 16875 384 479;7.652e-4 7.652e6 16875 512 639;7.652e-4 7.652e6 16875 768 959;7.652e-4 7.652e6 22500 384 479;7.652e-4 7.652e6 22500 512 639"
   Each group is one configuration (inner radius, outer radius R of the inverse, radial nodes N, angular nodes, maximal
   mode); 2 to 8 minutes each. Output: the audit data and text output in (d).
2. Identity c_l = (1 + psi_xy(0))/3, the identity-free root of h(P) = 1 at fixed rho, the centre relations E_c and D2,
   and the zeros of W on the axes, using the same part of the accompanying artifacts:
     Identity and trace wrapper arguments (accompanying artifacts): <coef> <tag> "7.652e-4 7.652e6 11250 384 479"
   about 2 minutes; the supplementary audit output is in the accompanying artifacts. The verifier's B_3 estimator on the traces this step writes:
     Independent B_3 estimator arguments (accompanying artifacts): <trace data>
   (the wrapper deletes the generated field and keeps the traces).
   The characteristic defect on the 857-label set of 4.4b and the axis integral I(eps) with the profile q0, using the same part of the accompanying artifacts (the generated field is 52 MB and is deleted afterwards):
     Field generator arguments (accompanying artifacts): <coef> 7.652e-4 7.652e6 16875 384 <generated field>
     Axis evaluator arguments (accompanying artifacts): <generated field> 479 <axis output>
     Dense characteristic evaluator arguments (accompanying artifacts): <generated field> 479 20 737 60 1e-4 <characteristic output>
   about 7 seconds, 2 minutes and 6 minutes; the arguments of the dense characteristic evaluator in the accompanying artifacts are the maximal mode, the label radius, the
   number of uniform labels, the number of labels next to each axis and the smallest geometric distance from the axis.
3. The lead's scans, in (b) with the generator of (a) on the path:
     Between-node scanner arguments (accompanying artifacts): <coef> 32768 640 <output>
     Between-node scanner arguments (accompanying artifacts): <coef> 24576 960 <output>
   under 30 seconds each on the candidate. They read the trial in its fit's own convention (the two-term closure at
   1000 L, 4.4) and on the candidate print whole-box N_f maxima 6.94e-7 and 7.27e-7 next to P (4.1).
4. The lead's characteristic defect (185 uniform labels, a cross-check of step 2) and the original-form B_3 from an
   export (the export is about 1.4 GB and is not included; it is regenerated): with the named coefficient data and the exporter in part (b) of the accompanying artifacts,
     Field exporter arguments (accompanying artifacts): <name> 24576 576
     Characteristic-defect evaluator arguments (accompanying artifacts): <field export> 20 185
     Original-form B_3 evaluator arguments (accompanying artifacts): <field export> mu1only
   (both evaluators are in part (c) of the accompanying artifacts); on the candidate the export took about 80 seconds, the original-form B_3 evaluator in the accompanying artifacts under 15
   seconds and the characteristic-defect evaluator with 185 labels about 30 seconds. The original-form B_3 evaluator prints two forms per variant: "orig", the
   original form of R10, which is the lead value quoted in section 4, and "ibp", an integration by parts whose end piece
   does not converge in the quadrature order n (it moves by about +0.008 from n 40 to n 80 on the candidate); the "ibp"
   values are not quoted.
5. The fit itself, from its start file (the free fit moved by -1e-3 in c_l along its soft direction, also in (a)):
     Fixed-c_l CPU solver arguments (accompanying artifacts): <start> <out> --fix-cl --nr 20480 --nt 720 --hours 1.8 --inner 500 --check 250
   The free control F1 is segment 2 of the free run, from the free fit:
     Free CPU solver arguments (accompanying artifacts): <free fit> <out> --nr 20480 --nt 720 --hours 1.8 --inner 2500 --check 250
   Both were stopped by the 1.8 h cap after 750 iterations, X1 over two linearizations (500 + 250) and F1 in one.
   The continuations X2, F2, X3, F3 use the GPU driver of (b):
     GPU solver arguments (accompanying artifacts): <start> <out> --nr 20480 --nt 720 --hours 4.9 --inner 2500 --check 250 --fix-cl --max-its 20750 --damping 1e-8
   (--nt 960 for X3 and F3; without --fix-cl for F2 and F3). X2 and F2 were run with --hours 0.75 and no --max-its; the
   time cap stopped both at the check after 20750 iterations, the schedule that --max-its 20750 reproduces. The m <= 200
   starts are the m <= 150 ends with the new angular coefficients set to zero (the angular-extension program in part (b) of the accompanying artifacts; the density is
   unchanged, residual difference 1.5e-15). The domain columns of 4.4 are the X3 end continued with the same driver and
   settings at --nt 960 with --fit-radius 90 or --fit-radius 300, and at --nt 960 on a 24576-point radial grid with
   --fit-radius 9000: the rows are then r < fit radius (in units of L) and the inverse domain is the fit radius / 0.9,
   with the two-term closure beyond; without the option the rows are r < 900 L and the inverse domain r <= 1000 L.
6. The velocity check of 4.5, in (e): an export of the coefficient file with the generator of (a)
     Field exporter arguments (accompanying artifacts): <name> 24576 576
   (about 80 seconds; it writes <field export>, regenerable and not included), then
     Real-space velocity checker arguments (accompanying artifacts): cand <coefficient data> <field export> <output> "Smax:1e18,smode:adapt,phimax:0.02,pcluster:1" full
   (about 32 minutes on X3 for the 52 points). It prints, per point, both velocities, their difference and the implied
   change of the normalized residual.
7. The far-field diagnostic of 4.5, in (c), with the generator of (a) on the path:
     Axis far-field diagnostic arguments (accompanying artifacts): <coef>            (axis limit of the forced and the stored first correction; seconds)
     Angular far-field diagnostic arguments (accompanying artifacts): <coef>                 (the angular profile of both; seconds)
     Far-field export checker arguments (accompanying artifacts): <coef> <export>; Far-field export decomposition arguments (accompanying artifacts): <coef> <export>   (comparison with an export of step 6)
     Third-order far-field diagnostic arguments (accompanying artifacts): <coef>                 (the third-order series of R / N_v and its sums at the radii of 4.5; about 1 minute)
   and the measured far residual against that series, with the inverse continued to 1e7 L, using the domain-fit code of (b) and the far-residual evaluator of (c) in the accompanying artifacts (it writes an export and deletes it afterwards; about 3 minutes):
     Far-residual evaluator arguments (accompanying artifacts): <coef> 24576 576 1e7 <output>
   and, in the same way, the far-band maxima of |R| / N_v over 1000 L < r <= 9000 L, 9000 L < r <= 1e4 L and r > 1e4 L,
   with the inverse computed to <Rinv> L and the two-term exterior beyond (1e4 is the own convention of the domain fit
   with rows to 9000 L, 1e6 continues the formula; a cross-check of the band rows of 4.5 from (d); about 80 seconds, 4.8
   GB):
     Far-band evaluator arguments (accompanying artifacts): <coef> 24576 576 <Rinv> <output>
Outstanding experiment (partly done). One refinement step of the experiment that would separate the two pictures of 4.8
was run: the fixed-c_l fits at 5.6004662 and 5.5683739 continued from m <= 150 to m <= 200 (4.3, 4.8); by the rule fixed
before the run its result is undecided (Q = 1.680 against the thresholds 1.36 and 3.05), so the two pictures are not
separated. Further nested discretizations at several separated exponents, with budgets large enough to estimate the
optimization error, were not run. The other rows of the fixed-c_l profile of 4.3 are on one basis (375 x m <= 150) at
one budget (21500 iterations), and the angular sequence m <= 150, 200, 250 at the candidate's c_l mixes approximation
and budget.

## 6. The strong setting P_inf (follow-up investigation)
Status of this section: final; its content is that of the report cutoff, 2026-10-21T00:00:37Z (6.0), and neither endpoint was reached. Section 6.3 contains only statements that the independent
verifier has checked (and, for analytic statements, that an external referee has audited); section 6.4 lists open
questions, additional verified diagnostics and results that were not fully checked by the report cutoff, each with its
verification status.

### 6.0 Timing and organization
- T0 = 2026-10-20T00:46:19Z (start of the follow-up investigation). The investigation was limited to 24 hours.
- T_end and report cutoff: the follow-up was limited to 24 hours from T0 and was stopped at its time cap,
  2026-10-21T00:46:19Z, without reaching an endpoint. T_end = 2026-10-21T00:57:29Z (report finalization, after the research cap), so T_end - T0 = 24 h 11 min 10 s (24.19 hours), and the recorded elapsed span exceeds 24 hours. This span includes finalization and does not by itself verify the required active research time.
  The content of this report was frozen at its cutoff, 2026-10-21T00:00:37Z, 23 h 14 min 18 s (23.24 hours) after T0;
  work in the last 46 minutes before the cap (the verifier's final checks, which confirmed the frozen text, and
  diagnostics of the numerical researcher on a fifth grid that the report does not use) is not reported as a result
  here. At finalization only the status lines, the timing statements, the paragraph on what this round added and the
  description of the accompanying artifacts were edited. The follow-up states no terminal result for P_inf, since
  neither endpoint is reached. The lead researcher, the
  numerical researcher and the verifier each worked in consecutive sessions of at most six hours from T0 (their first
  sessions started at 00:46:19Z, 00:46:21Z and 00:46:23Z), with long computations continuing between sessions; no time
  outside the interval from T0 to the cap is counted.
- Environment: the machine type of section 0 (shared Linux x86_64, Intel Xeon Platinum 8275CL, every CPU process
  single-threaded; NVIDIA A100-SXM4-80GB GPUs). The lead researcher and the numerical researcher used Python 3.9.25 with
  numpy 2.0.2, scipy 1.13.1, sympy 1.14.0 and mpmath 1.3.0, python-flint 0.6.0 for ball arithmetic, and PyTorch 2.8.0
  (CUDA 12.8) for the numerical researcher's residuals, Jacobians and solves; from 13:06:38Z the verifier used Python
  3.12.13 with numpy 2.5.0, scipy 1.18.0, sympy 1.14.0, mpmath 1.3.0, python-flint 0.9.0 and PyTorch 2.13.0; the package
  versions of the verifier's earlier sessions were not recorded.
- Same organization as section 0: a lead researcher (analysis, specification, this report), a numerical researcher
  (solver) and an independent verifier with separately written code; external referee audits for analytic claims. All
  three roles and the external referees were AI language models working in separate sessions. Until 2026-10-20T13:06:38Z
  the verifier was a model of the same family as the lead and numerical researchers; from that time the verifier's work
  was continued, in separate sessions, by the model that also supplied the external referee audits commissioned by the
  lead researcher, so after that time a verifier check and an external referee audit commissioned by the lead researcher
  of the same claim come from the same model, in separate sessions. From that time the verifier also obtained direct
  reviews of some of its own proofs from a model of the same family as the lead researcher (among them its proofs of the
  propagation statement of 6.3.1 (f), item (C1), and its proofs in the item on the frozen kernel at P in 6.4, whose
  reviews are the further external referee audits named there); the verifier checked the reasoning of these reviews,
  corrected its proofs where they found gaps and saved the records of the reviews. The verifier's checks from that time
  use newly written code; confirmations from before that time were inherited by it and are not claimed to have been
  repeated.
- The accompanying artifacts of the follow-up are published beside this report; those of the first investigation in sections 4 and 5 are unchanged. Their guide gives the commands for the certificates, checks, solves and recomputations, organized in three parts. The lead researcher's part holds the
  programs, inputs, outputs and derivations of the exclusion certificates of 6.3.1 (n) and (o) (among them the
  least-squares fit of the reference, the interval and exact rational certificate programs, the explicit remainder-bound
  formulas and an external referee's rerun of the certificate), the evaluators of the axis functional B_3 used in 6.3.2
  and 6.4, and the symbolic and numerical checks of statements of 6.3.1, 6.4 and 6.5. The certificate programs were
  rerun from these copies before publication and reproduced their stored outputs (up to timing fields and the order of
  keys). The accompanying artifacts record these reruns and those of the other programs, of which one long numerical check was not
  rerun (its original output, complete for one of its two parameter values, is included) and one exact check stopped at
  the time limit of 540 s after its first steps; it also records the small library-dependent differences of the
  least-squares fit, which does not enter the certificates (they use the frozen reference). A change log lists every
  edit made to the copies (internal labels, local paths, file names and the path handling of the programs; no
  computation was changed). The numerical researcher's part holds its solvers (the collocation model with
  its canonical modal inverse, the characteristic-map formulation, dense Jacobians, Newton, constrained and Ritz tools),
  the exact command sequences of the full solves, its tests, and the stored states and diagnostic outputs used in 6.4.
  The verifier's part holds its separately written programs with their outputs (among them the generator,
  inverse and residual evaluator of the recomputation in 6.2), and the proofs of the statements attributed to the
  verifier in 6.3 and 6.4 with their symbolic or numerical checks; the accompanying artifacts describe the components. For
  publication, absolute local paths in the copied files were replaced by relative ones, and the research records (work
  logs, job drivers, run logs, report drafts), stored Jacobians and, in the verifier's part, per-piece intermediate
  outputs and eleven data files larger than 500 kB were left out; all of these are regenerated by the included programs.

### 6.1 Question and endpoints
The question is P_inf of section 1 (a C^infinity near 0; rho only C^(2,alpha) elsewhere, in particular at the source
P). The two endpoints, fixed before the work:
- YES_inf (numerical evidence, not a proof): one candidate with B_3 = 0 (axis finite part and the trial's own
  coefficient, two independent estimators, |B_3| below three times its measured accuracy), B_5 and B_7 zero within
  their measured accuracies, and the full P_2 standard of section 4 for that candidate (normalized transport and
  elliptic residuals about 1e-6 including next to P, at least three resolutions and three domains, far-field and
  inverse errors quantified separately, the identity c_l = (1 + psi_xy(0))/3 checked independently, every number
  recomputed by the verifier). [Clarified 2026-10-20: the third-jet test is that the coefficient C_0 = l_3 + B_3 of
  the y^3 homogeneous solution at 0 vanishes (6.3.1 (a), (g)); for a candidate with l_3 = 0, for instance one with
  bounded d_y^3 rho on the axis next to P, this is B_3 = 0 as written. The B_5 and B_7 tests are fixed reporting
  targets: at a nonresonant order j the centre condition is C_(0,j) = l_j + B_j = 0 (6.3.1 (a)), which is B_j = 0 when
  l_j = 0, and at a resonant order B_j need not vanish (6.3.1 (h)); at the computed c_l the orders 5 and 7 are not
  resonant.]
- NO_inf (theorem): no profile of the admissible class is C^infinity (or C^8) near 0, possibly under explicit extra
  hypotheses, with the remaining hypotheses stated exactly. [Clarified 2026-10-20, during the work: for reporting
  purposes this section adopts a convention stricter than the task's allowance for theorems under explicit additional
  hypotheses. A nonexistence theorem whose extra hypothesis is a condition on the profile's own data that implies the
  nonvanishing or the sign of the obstruction (for instance B_3 != 0, or the pointwise condition (H_-) of 6.3.1 (k)) is
  recorded as a conditional sub-result, not as NO_inf, unless that condition is derived for a specified structural class
  of profiles (of the kind of (Hmin) of R9). Likewise, a nonexistence theorem restricted by further hypotheses on the
  source, on traces, to a neighbourhood of a fitted reference or to a fixed finite angular cutoff of the density (for
  instance 6.3.1 (o) and (p)) is recorded as a restricted nonexistence result, not as NO_inf; (p) moreover excludes such
  densities from P_2 as well, whatever their regularity at 0, so it bears on the class of profiles and not on smoothness
  at 0, and the computed candidate is not of its form. NO_inf is reserved here for nonexistence on the full strong class
  or on the full class with a C^8 centre, possibly cut down by an explicit structural hypothesis on the profiles of the
  kind of (Hmin) of R9 (which the task allows when the report states exactly what remains). The convention does not
  dispute the validity of such theorems.]

### 6.2 Recomputation of the published candidate with separately written code
The verifier of the follow-up investigation recomputed the candidate X3 from its coefficient vector with its own
generator and a different inverse (spectral-element collocation of the modal ODEs in log r with exact radiation
conditions, instead of quadrature of the modal Green function), at four discretizations:
- max R/N_f over all evaluation points 6.8e-7 to 7.3e-7, attained next to the x-axis 0.1 from P (published 7.2e-7
  near P); max R/N_v 1.10e-6 (at r about 3.5e4 near the y-axis); max R/N_f below 1e-8 for r < 1 and 1.3e-7 for r > 30;
- (1 + c)/3 = 5.575362607 against c_l = 5.575362611; x* = 8.6000638; h(P) - 1 between -2.0e-8 and -7.6e-9;
- g(P) = rho_y(P) = 29.74949, lambda_P = g(P)/A = 2.93077, (1 + g(P))/A = 3.02929 (A = 2 c_l - 1 = 10.150725), also
  from the axis velocity alone (29.74948);
- B_3 from the recomputed axis velocity w together with the trial's g (two trial-data finite-part forms), with two
  separately written axis inverses (the collocation above at two resolutions, and quadrature of the modal Green
  functions with the exact derivatives of the trial in t = log r): 0.296 to 0.323 natural units over both forms, both
  inverses, inner fit degrees 8 to 16 and every fit window reaching x >= 0.3, i.e. 0.31 +- 0.015; in the published
  outer-window convention 0.2991 to 0.3021 at fit degrees 8 and 12 (0.3066 to 0.3070 at degree 16). Within these windows
  the fit degree changes the value by at most 0.026, the form by at most 0.010 and the inverse by at most 0.007. The
  trial's own coefficient is 0.046. These trial-data values and the trial's own coefficient fail the smooth-centre test,
  so X3 is a P_2 candidate, not a P_inf candidate; this does not certify the value of B_3 for a nearby exact profile
  (6.3.2 (c)). The exact form that uses w alone (g rebuilt from w) cannot be applied directly to the unmodified
  recomputed trace: it needs w'(0) = -A and w'(x*) = A at once, and its terms at x* are driven by the defect of the
  identity for c_l (2e-8). The w-only estimates of 6.3.2 (d) and 6.4 use fitted origin data and explicit treatments of
  the data next to x*; they are model-dependent estimators, not direct evaluations of the exact functional on an
  unmodified trace. This agrees with section 4.1 and does not change it. [Clarified 2026-10-20: an earlier version said
  "from its own axis velocity" and "B_3 is not 0 on X3".] [Corrected 2026-10-20: an earlier version of this item gave
  0.30 +- 0.03 and an outer-window range 0.2928 to 0.3021; the lower values came from one form of the estimator with a
  faulty homogeneous solution, found by the verifier's test on exact data and corrected.] A fit window [x_lo, x_c] is
  used only when its value is stable under the inner fit degree (8, 12 and 16) on every inverse; on X3 these are exactly
  the scanned windows with x_c >= 0.3. Every scanned window ending at x <= 0.2 changes by more than 0.02 with the fit
  degree on at least one inverse (by up to 3.4 at [0.02, 0.12]) and is not used. The B_3 integrand times x^(5 + beta)
  carries a non-smooth component of relative size 1e-13 to 1e-11 in the origin layer (common to both inverses, so
  probably in the trial data), and the finite part amplifies relative errors at x = 0.01 by about 5e11 natural units.
  [Corrected 2026-10-20: earlier versions declared unusable first the windows reaching below x = 0.005, then the windows
  with x_lo <= 0.003 or x_c <= 0.1 (with [0.005, 0.2] given as usable), and gave "0.30 to 0.318 natural units over every
  usable form, fit window and both inverses, i.e. 0.31 +- 0.01" and an outer-window range "0.2991 to 0.3021 over two
  forms, two fit degrees and both inverses". Those rules were drawn from one fit degree and one resolution and do not
  separate stable from unstable windows: [0.02, 0.12] passes the second rule and changes by more than 3 with the fit
  degree. The trial-data estimates of B_3 on X3 are nonzero under every usable version.] The inner fits are polynomial,
  that is they assume an analytic model of the axis data at the origin. On the ten stored traces of 6.3.2 (d), refitting
  the polynomial origin coefficients together with a non-polynomial term at the critical origin order lowers the
  integral form of B_3 from 0.2945 to 0.3016 to 0.2815 to 0.2991 (a sensitivity test of the estimator, 6.4); on the
  stored traces of X3 and of its control F3 the fitted non-polynomial coefficient is consistent with 0 and the values do
  not change. The test has not been repeated on the recomputed traces of this subsection.

### 6.3 Results
Status at the report cutoff. The statements below have been checked by the verifier with its own symbolic or numerical
computations or by hand (the methods and checkers are identified in the items or in the dated entries of the
verification timeline) and, for analytic statements, audited by an external referee; inputs that were not checked are
named where they occur. Statements not fully checked by the report cutoff, and external referee results not checked by
the verifier, are listed in 6.4.

6.3.1 Analytic statements

(a) Axis hierarchy and the obstruction functionals. Along the x-axis write the Taylor jets in y, to the order that the
regularity justifies (the sums are formal jets, not convergent series): rho ~ sum_{j odd} G_j(x) y^j,
W_1 ~ sum_{i even} W1_i(x) y^i and W_2 ~ sum_{i odd} W2_i(x) y^i, with G_1 = g, W1_0 = w, W2_1 = h. The y^j
coefficient of W.grad rho = rho is
  w G_j' + (j h - 1) G_j = F_j := - sum_{i = 2, 4, ..., j - 1} [ W1_i G_{j-i}' + (j - i) W2_{i+1} G_{j-i} ].
From div W = 2 c_l and curl W = -rho_x:
- h = 2 c_l - w';
- W1_i' + (i + 1) W2_{i+1} = 0 for i >= 2;
- W2_j' - (j + 1) W1_{j+1} = -G_j'.
In particular F_3 = -a_2 g' - b_3 g with a_2 = (g' - w'')/2 and b_3 = -a_2'/3. The j = 1 equation is (w/g)' = A/g.
Hence g (normalized by g/x^2 -> 1 at 0), h, a_2 and b_3 are determined by c_l and w on [0, x*]; for a profile each
G_j with j >= 3 is then determined, recursively in j together with W1_(j+1) and W2_(j+2), up to a multiple of its
homogeneous solution H_j, which an endpoint condition fixes (below). [Corrected 2026-10-20: an earlier version said
that all W coefficients and all G_j are determined by c_l and w.]
The homogeneous solution normalized at 0 is H_j = A^(q_j) g^(j + q_j) |w|^(-q_j), with q_j = (j - 1)/A. It behaves as
H_j ~ x^(p_j) at 0, with p_j = 2j + (j - 1)/A, and as H_j ~ C |x* - x|^(-q_j) at P. For j = 3 it is the H of R10.
Assume
  (C1) rho is C^(j+2) near every point of the open segment (0, x*) x {0},
  (C2') G_j/H_j -> 0 as x -> x* (for j >= 5, also G_i/H_i -> 0 for the odd i with 3 <= i < j), and
  (C0) w, g, G_3, ..., G_(j-2) have expansions at 0 in powers of x that define the finite part at 0 (for instance,
       they are smooth near 0).
Then the coefficient of H_j in G_j at 0 is
  B_j = - f.p. int_0^{x*} F_j/(w H_j) dx.
More generally, if G_j/H_j -> l_j at P, this coefficient is C_(0,j) = l_j + B_j, because (G_j/H_j)' = F_j/(w H_j);
B_j always denotes the finite-part functional above, and for j = 3 we write C_0 = l_3 + B_3. [Corrected 2026-10-20:
an earlier version wrote this as B_j = l_j - f.p. int, which changed the meaning of B_j.] Under (C1), (C2') and (C0),
a profile that is C^infinity near 0 has B_j = 0 for every odd j >= 3 with p_j not an even integer. This includes
j = 3 for every A > 1, since 6 < p_3 < 8. (C1) is proved in (f); (C2') is discussed in (f), (g), (h), (j) and 6.4.
Converse (external referee; checked by the verifier). Let A be irrational and let W be a given C^infinity field near 0,
equivariant under the reflections, with DW(0) = diag(-A, 2A + 1). A continuous solution of W.grad rho = rho, even in
x, odd in y, normalized as above and smooth near the points (x, 0) with 0 < x small, is C^infinity near 0 if and only
if its coefficients C_(0,j) vanish for every odd j >= 3; for profiles satisfying (C2') at every odd order,
C_(0,j) = B_j. (For rational A = p/q in lowest terms, p_j is an even integer exactly when j = 1 + 2pn with n a positive
integer.) For coupled profiles this is not a sufficient condition from finite regularity: there curl W = -rho_x, so
smoothness of W near 0 is itself equivalent to smoothness of rho near 0. Whether C_(0,j) = 0 for all j implies
smoothness for a profile known only to be of finite regularity at 0 is open.

(b) For A > 2 and 0 < alpha <= 1 - 2/A, C^(2,alpha) regularity at P alone does not give (C2'). With s = x - x*, the
function y^3 (s^2 + y^2)^(-1/A) is
homogeneous of degree 3 - 2/A, so it is C^(2,alpha) for alpha <= 1 - 2/A (0.803 at A = 10.150725). Its y^3
coefficient on the axis is |s|^(-2/A), which is the H_3 behaviour. This function is not a solution.

(c) No local obstruction. For every A > 1 take k = sqrt(2/A), c_l = (A + 1)/2 and
  w(x) = -(A/k) sin(kx),  g(x) = A (1 - cos(kx)),  rho = g(x) y,  psi = (c_l x - w(x)) y.
These satisfy -Laplace psi = rho_x, W = c_l X + (-psi_y, psi_x) and W.grad rho = rho exactly on R^2.
- The origin is a saddle with DW(0) = diag(-A, 2A + 1).
- P = (pi/k, 0) is a source with DW(P) = diag(A, 1) and g(P) = 2A.
- rho = x^2 y (1 + O(x^2)), and c_l = (1 + psi_xy(0))/3.
- xi = (2/k) tan(kx/2) and eta = y cos^2(kx/2) are exact linearizing coordinates at 0, with rho = xi^2 eta.
- All G_j with j >= 3 vanish, so B_3 = B_5 = ... = 0.
The pair is not a profile of the class: rho grows linearly in y, U_1 = w - c_l x is not sublinear, and psi is a local
stream function, not the canonical velocity law.
Consequence: the equations admit smooth local data with the required normalization near the centre, along the axis
segment and near the first source, so a proof of NO_inf must use a property that this pair does not have, such as the
growth bounds of the class and the canonical velocity law (the far field). By the extension below, (A1) to (A3), the
canonical velocity law and the normalization can hold together with the profile equation on any bounded region fixed in
advance, for a field that is not a profile; these requirements, with the profile equation restricted to such a region,
are consistent. This does not rule out conditional exclusions under additional hypotheses on the axis data, such as (k),
(n) and (o) below, or arguments that derive such hypotheses from the equation elsewhere.
Compact canonical extension (verifier; audited by an external referee; checked by the lead researcher). Fix A > 1, k and
c_l as above and X0, Y0 > 0. There are smooth compactly supported rho and psi on R^2 that coincide with the pair above
on the rectangle |x| < X0, |y| < Y0 and satisfy on all of R^2: -Laplace psi = rho_x, the parities of section 1,
rho = x^2 y a with a smooth, even in x and in y and a(0) = 1, and psi_xy(0) = 3 c_l - 1, where U = (-psi_y, psi_x) is
the canonical velocity of section 2. So (A1) for every m, (A2), (A3) (for any gamma < 1, with a constant depending on
the field), the velocity law of (A4) and c_l = (1 + psi_xy(0))/3 hold, and the profile equation holds on the rectangle.
For X0 > pi/k the extension has the trace of the pair on the axis interval [0, X0), so P = (pi/k, 0) is its own first
positive axial source, and the rectangle contains neighbourhoods of 0, P and the axis segment between them.
Construction: let hbar(x) be odd, smooth, compactly supported and equal to c_l x - w(x) on |x| < X0; q(x) odd, smooth,
compactly supported, zero near [-X0, X0], with int_0^inf q = 1; J(y) odd, smooth, compactly supported and equal to y^3/6
on |y| < Y0. With H0 = hbar'(0) = c_l + A and I = int_0^inf hbar put
  psi = hbar(x) J''(y) + q(x) (H0 J(y) - I J''(y)),   rho(x, y) = -int_0^x Laplace psi(s, y) ds.
Then int_0^inf psi(s, y) ds = H0 J(y) and psi_x(0, y) = H0 J''(y), so int_0^inf Laplace psi(s, y) ds = -psi_x(0, y) + H0
J''(y) = 0 and rho vanishes for large |x|; it vanishes outside the support of J, so it is compactly supported. Further
rho_x = -Laplace psi, and on the rectangle psi is the pair's stream function and rho = (H0 - c_l - A cos(kx)) y = g(x)
y. The smooth function rho is even in x, odd in y and zero on x = 0, which gives the factor x^2 y a, and a(0) = 1
because g(x) = x^2 + O(x^4). U is compactly supported, divergence free, with curl U = -d_x rho and the parities of (V3),
hence it is the canonical velocity. The profile equation fails outside the rectangle, necessarily: rho is nonzero near 0
and compactly supported, so it attains a nonzero extremum, where grad rho = 0, R = -rho and |R|/N_f = |R|/N_v = 1
(normalizations of 4.4). The field is therefore not in the class, whose condition (A4) requires the profile equation on
all of R^2. What is proved is this: for each bounded set K fixed before the field is chosen, (A1) to (A3), the canonical
velocity law, the normalization and the profile equation on a neighbourhood of K are satisfied together by some field,
and K may contain any fixed neighbourhood of 0, of the field's first source P and of the axis segment between them. No
contradiction can be derived from these assumptions alone. The statement concerns regions fixed in advance. A region
chosen from the field after its construction, for instance one containing a nonzero extremum of rho, detects the
failure, and a proof that uses the equation elsewhere to derive a restriction on the axis data and then concludes in a
bounded region is not affected. Exact vanishing of the residual on a bounded region does not certify a small normalized
residual elsewhere: wherever the denominators are positive, |R|/N_f <= 1 and |R|/N_v <= c_l by the triangle inequality,
and the extension attains the value 1 for both. The extension is not a profile and says nothing about the existence of
one.

(d) Structure at the source P (frozen-coefficient models; leading-order statements, not classifications). Use
linearizing coordinates at P, with W = (A xi, y) + ... and rho = g* y + ..., where g* = rho_y(P).
- Conormal balance. A conormal term C |xi|^mu y^j along the weak characteristic {xi = 0} balances only for
  mu_j = (1 + g* - j)/A. At X3, mu_1, mu_3, mu_5, mu_7, mu_9, mu_11 = 2.931, 2.734, 2.537, 2.340, 2.143, 1.946.
  For j = 3, the term needs a companion: a G_1 term xi^(mu_3 + 2) y and a w term xi^(mu_3 + 3). Without them the y^1
  coefficient of the curl equation fails.
- Coupled packets. A high-frequency packet carried along the orbits of W has amplitude rate m = 1 + rho W_2/|W|^2.
  Along the source orbits tangent to the weak direction, on which xi/|y|^A is fixed and finite, this rate tends to
  1 + g* (along the axis it tends to 1), so the packets near P behave as |y|^(1+g*) F(xi/|y|^A), with F smooth and
  compactly supported and the odd extension from y > 0. Such a function is C^(k,alpha) at P if 1 + g* >= (k + alpha) A
  (a sufficient condition). At X3, (1 + g*)/A = 3.0293: the packets are C^(2,alpha) for every alpha < 1 and
  C^(3,alpha) for alpha <= 0.029; a nonzero packet is not C^4, since d_xi^4 of it is |y|^(1+g*-4A) F^(4)(xi/|y|^A)
  and F^(4) is not identically 0. [Corrected 2026-10-20: an earlier version said that the rate tends to 1 + g* at P
  without restricting the orbits.]
- Source motion. The source moves with the solution. Along a differentiable family of exact profiles, or for an
  admissible solution of the linearized problem, a perturbation (dc_l, dw) moves the source by p = -dw(P)/A, and
  dh(P) + p h'(P) = 0. This is the first-order form of h = 1 at the moved source; it does not hold for arbitrary
  perturbations.
- Singular values cannot decide isolation. The operator d_t + (1 - d_s^2)^(-1) from X = {u in L^2(T^2): d_t u in L^2},
  with the graph norm, to L^2(T^2) is injective, its coupling (1 - d_s^2)^(-1) is compact from X to L^2, and it has
  quasimodes with singular values 1/(1 + n^2) -> 0. So a count of small singular values, or their decay with
  resolution, cannot by itself show a family (question Q1).

(e) Fixed-point formulation through the source. On the basin of P, rho = C eta_P[W] with C = rho_y(P) and eta_P[W](X) =
y exp(-int_{-infinity}^0 [b(Phi_t X) - 1] dt), where W_2 = y b and Phi_t is the flow of W (result R6). Its linearization
is the transport-form linearization W.grad d rho - d rho + dW.grad rho = 0 with dW = U[d rho] + dc_l X. The normalization
is dC = d rho_y(P) + p g'(P), with p the source displacement of (d). This holds on the perturbations for which the
orbit integral converges at P; Frechet differentiability in fixed Hoelder spaces is not proved. The formulation
excludes the kernel elements that are not C^1 at P, among them the pure-transport packets (rate 1). The coupled
packets of (d) are not excluded by the C^1 requirement; whether they belong to the kernel of the full coupled
linearization is not proved.

(f) A necessary condition for P_inf.
- (C1) holds for every profile of P_inf: if a profile of the class (rho of class C^(2,alpha), growth exponent below 1,
  canonical velocity law) is C^infinity near 0, then rho is C^infinity on an open neighbourhood of the segment (0, x*) x
  {0}. Proof (external
  referee; audited by a second external referee; checked by the verifier, including the localization of the velocity
  law; the verifier also proved this statement independently, with a resolvent regularization and a weighted energy
  estimate, and that proof was audited by a further external referee): a localized energy estimate for the derivatives
  of order k, iterated in k. One-derivative lemma: let T u = W.grad u + sum_nu B_nu(X) R_nu u + C(X) u, with W real of
  class C_b^(2,alpha), B_nu and C of class C_b^(1,alpha), and R_nu constant Fourier multipliers whose symbols satisfy
  |m| <= C and |grad m(xi)| <= C/|xi|; let u be in L^2 and T u in H^(-1). If a compact nonstationary arc of W has a tube
  on which T u is in H^1_loc, and u is in H^1 near the forward endpoint, then u is in H^1 near every earlier point of
  the arc. For the proof, regularize with J_eps = (1 - eps^2 Delta)^(-1): the identity
  T(J_eps u) = J_eps(T u) - eps^2 J_eps([Delta, T](J_eps u)) is exact, and its commutator, written in divergence form
  and read in the sense of distributions, involves DW, Delta W and only the first derivatives of B_nu and C (no second
  derivatives of B_nu and C and no third derivatives of W). The commutator bound
  ||[chi, R] d_j v||_2 <= C (int |zeta| |chi^(zeta)| d zeta) ||v||_2 holds for cutoffs chi of class C_c^(2,alpha), which
  are built from C^(2,alpha) flow coordinates (t, s) with W.grad = d_t. With the weight
  chi = eta(s) e^(lambda t/2) theta(t) and D = W.grad one has D(chi^2) >= lambda chi^2 - K_e e^2, with e supported where
  u is known to be in H^1, and for lambda large the L^2 norm of chi grad J_eps u is bounded uniformly in eps; weak
  compactness gives chi grad u in L^2. Iteration: let O be the open set of points whose forward trajectories reach the
  smooth neighbourhood of 0 in finite time along a nonstationary arc; rho is in H^2_loc(O). If rho is in H^k_loc(O),
  k >= 2, then for each compact tube in O and a cutoff eta in C_c^infinity(O) equal to one on a neighbourhood of the
  tube, the derivatives u_I = d^I(eta rho), |I| = k, solve, in the sense of distributions (by mollification, under the
  induction hypothesis), a system of this form near the tube, after the coefficients are extended from a compact
  neighbourhood of the tube by a smooth cutoff so that they have the global regularity required by the lemma and agree
  with the original ones near the tube (W itself contains the unbounded term c_l X): the terms with one derivative on W
  give a matrix in DW, the term with all k derivatives on U is grad rho . R u_I plus a locally H^1 term (by the
  localization below), with coefficients B_nu, the components of grad rho, of class C^(1,alpha), and the remaining
  products (d^J U)(grad d^(I - J) rho), 2 <= |J| <= k - 1, are locally H^1 by an interpolation (Gagliardo-Nirenberg)
  product estimate. Hence rho is in H^(k+1)_loc(O); by induction rho is C^infinity on O, which contains the segment
  (0, x*) x {0} because w < 0 there. The referee proves the commutator, interpolation, product and regularization
  estimates; the other inputs are textbook facts of Fourier analysis, distributions, integration, approximation,
  compactness and ODE flows (among them Plancherel and Fourier inversion, the Young and Hoelder inequalities, Fubini's
  theorem and dominated convergence, mollification, the L^2 bound of the maximal function, weak compactness in L^2, the
  regularity of ODE flows and the inverse function theorem), and, in the Localization below, the boundedness of order-0
  Fourier multipliers on Hoelder-Zygmund spaces with a positive exponent. The proof is qualitative: it gives no bound
  uniform as the axis point tends to 0 or to x*.
  [Revised 2026-10-20: an earlier version proved (C1) by paradifferential propagation, with a positive-commutator
  estimate cited from M. E. Taylor, Pseudodifferential Operators and Nonlinear PDE, section 6.1, that was not checked
  against the source; that estimate is no longer used.] Localization (verifier). Let X_0 be a point, delta > 0, chi in
  C_c^infinity with chi = 1 on B(X_0, 2 delta), and f = (1 - chi) rho. On B(X_0, delta), U[rho] is the order-0 Fourier
  multiplier (xi_1 xi_2, -xi_1^2)/|xi|^2 applied to chi rho, plus U[f], and U[f] is C^infinity there with |d^k
  U[f](X)| <= C_k int (delta + |Y - X_0|)^(-2-k) |f(Y)| dY for k >= 1, finite because the growth exponent is below 1.
  For compactly supported data the multiplier is (V2): its components are d_1 d_2 and -d_1^2 applied to the logarithmic
  potential, whose kernels are the principal-value kernels of (V2), the second with the local term. The limit in (V2)
  exists for rho and for chi rho, hence for f; for X, X_1 in B(X_0, delta) the kernel of (V2) is smooth on the support
  of f, so U[f](X) - U[f](X_1) is an absolutely convergent integral, which may be differentiated under the integral
  sign. With the boundedness of order-0 multipliers on Hoelder-Zygmund spaces of compactly supported functions, this
  also gives the local C^(2,alpha) regularity of W used in the lemma above and in (h) and (m).
- Endpoint condition at P. If d_y^3 rho(x, 0) stays bounded as x -> x*^-, then (C2') holds for j = 3, because
  H_3 -> infinity at P. More generally, (C2') for j holds if the rescaled functions R_t(z) = rho(x* - t^A, t z)/t on a
  fixed interval |z| <= z_0 are relatively compact in C^j as t -> 0. Only the derivatives
  d_z^j R_t(0) = j! t^(j-1) G_j(x* - t^A) enter, and the Taylor series in z need not converge. Since R_t(z) -> g* z
  pointwise, every C^j limit point is g* z, so t^(j-1) G_j(x* - t^A) -> 0 for j >= 2; this is (C2'), because
  H_j ~ C t^(-(j-1)) at x = x* - t^A. [Clarified 2026-10-20: an earlier version wrote R_t as its Taylor series in z.]
- Theorem. Let rho be a profile of the class that is C^infinity near 0 and such that d_y^3 rho(x, 0) stays bounded as
  x -> x*^-. Then B_3(c_l, w) = 0. Proof. By (C1) the third axis equation holds on (0, x*), so (G_3/H_3)' = F_3/(w H_3)
  there. By the endpoint condition G_3/H_3 -> 0 at x*, so the improper integral of F_3/(w H_3) up to x* converges
  (F_3 need not be bounded at P) and equals -G_3/H_3(x). At 0, G_3 is smooth and even and H_3/x^(p_3) is smooth, even
  and positive, so G_3/H_3 is a sum of powers x^(2m - p_3), 2m < p_3, plus o(1); since p_3 is not an even integer, the
  finite part removes these powers without a log term, and the constant term B_3(c_l, w) is 0. Without (C1) (external
  referee; checked by the verifier): the limit M = lim K/y of (m) exists on (0, x*) by integration along the
  characteristics, which uses only second derivatives, so d_y^3 rho(x, 0) exists as a transverse limit and the third
  axis equation holds in the sense of distributions (a_2 is in general only Hoelder continuous). If d_y^3 rho(x, 0) is
  bounded at P, then l_3 = 0 and Q_3 - Q_3(x*) = O(x* - x), where Q_3 = a_2/g^3 and m = -w/g are as in (i) (integrate
  dQ_3/dm = -3 A^beta m^(1 - beta) dZ/dm in m, with Z = G_3/H_3 = O(m^beta)); so the convergent form of B_3 displayed in
  (i) converges at P with no Hoelder condition there, and it is 0, because C_0 = l_3 + B_3 holds in this weak form and
  C_0 = 0 by smoothness near 0. This proves the theorem without (C1) for B_3 in the derivative-free form of (i); with
  (C1) the classical form holds as well. At C^(2,alpha) alone this argument does not reach order 5, since it does not
  construct the traces a_4 and b_5.
- For odd j >= 5 the same argument gives B_j(c_l, w) = 0 when p_j is not an even integer, provided the endpoint
  condition (C2') holds for every odd i with 3 <= i <= j (the functional B_j uses G_3, ..., G_(j-2), which must be the
  solutions selected by these conditions, with zero normalized limit at P; they need not be bounded). These conditions
  hold if rho is C^(j-1,alpha) near P with 0 < alpha < 1 and alpha > 1 - (j-1)/A (6.3.1 (h), Higher odd orders).
  [Corrected 2026-10-20: an earlier version said "every odd i <= j" and "bounded at P"; since G_1/H_1 = 1 the conditions
  start at i = 3.]
- This is a necessary condition for a profile of P_inf with bounded d_y^3 rho on the axis next to P. It is not a NO_inf
  theorem: it does not decide whether a profile of the class satisfies it, and it says nothing about profiles with d_y^3
  rho(x, 0) unbounded at P, except under the rescaled compactness criterion above or the hypotheses of (h)
  (for 1 < A <= 2, (m)); see 6.4.

(g) In the frozen coupled model at P, Hoelder regularity with exponent at most 1 - 2/A does not give the endpoint
condition, and one-sided smoothness does not give a finite l_3.
- Frozen model. Freeze the coefficients at P: with s = x - x* and g* = rho_y(P), the linearization of
  W.grad rho = rho about W = (A s, y), rho = g* y is
    L_g v := (A s d_s + y d_y - 1) v + g* U_2[v] = 0,
  where U_2[v] is the second component of the velocity of v (Fourier multiplier -xi^2/(xi^2 + eta^2)).
- Solution (external referee, checked by the verifier). For A > 2 and 3 < g*/(A - 1) < 4 (at X3, g*/(A - 1) = 3.251),
  the function v with Fourier transform
    v-hat(xi, eta) = a-hat(xi) i sgn(eta) |eta|^(2b - 4) (xi^2 + eta^2)^(-b),  a(s) = s_+^(-2/A),  b = g*/(2(A - 1)),
  solves L_g v = 0. It is odd in y, homogeneous of degree 3 - 2/A, of class C^(2, 1-2/A) near P (and not better) and
  smooth on s < 0. On the axis to the left of P its y^3 coefficient is G_3 = |s|^(-2/A)/(12 sin(2 pi/A)), so G_3/H_3
  tends to a nonzero limit at P. On s > 0 it carries the term -(a(s)/(6 pi)) y^3 log|y|. The verifier checked the
  equation symbolically, the constant by a separate physical-space computation (to 20 digits at five values of
  (A, g*)), and the regularity and the one-sided smoothness by reading the argument. The Fourier convention is
  v-hat(zeta) = int e^(-i X.zeta) v(X) dX; the right side above is homogeneous of the non-integer degree 2/A - 5 and
  is taken as its homogeneous distributional extension at zeta = 0.
- Scope. This is a solution of the frozen local model, with growth |X|^(3 - 2/A), not a profile. It shows that an
  argument that uses only C^(2,alpha) regularity at P with alpha <= 1 - 2/A, smoothness to the left of P, and a
  class of forcing terms that contains 0, cannot give the endpoint condition of (f). One-sided smoothness is what (C1)
  gives for a profile: the points of the axis to the right of P flow away from P and do not reach the region of
  smoothness at 0.
- Sign. For an exact profile with the classical third axis equation on (0, x*) (for instance by (C1)), the origin
  hypothesis (C0) of (a) and a finite limit G_3/H_3 -> l_3 at P, integration of the third axis equation over (0, x*)
  gives the coefficient C_0 = l_3 + B_3(c_l, w) of H_3 at 0. So such a profile that is C^infinity near 0 has
  B_3(c_l, w) = -l_3 (checked by the verifier).
- A family of frozen solutions (external referee; checked by the lead researcher and by the verifier). Replace
  s_+^(-2/A) by s_+^(-lambda), lambda = (d - 1)/(A - 1), and the exponent of |eta| by k = 2b - 2 - A lambda, with
  1 < d < min{A, (1 + g*)/A}, d != 2 and d != 3 (then 0 < lambda < 1 and k > -1, and the homogeneous extension at zero
  frequency exists; at X3 the bound is (1 + g*)/A = 3.0293; [corrected 2026-10-20: an earlier version had the bound
  d < (1 + g*)/A only, which does not give lambda < 1 when A^2 < 1 + g*, for instance at A = 2.1, g* = 4.3, d = 2.5
  (external referee; the corrected range and this example checked by the verifier)]; at d = 2 the coefficient c_- below
  has a simple pole and the left axis velocity carries a term s^2 log|s|, while G_3 stays finite). [Corrected
  2026-10-20: an earlier version excluded d = 3 only.] The function solves L_g v = 0, is odd in y, homogeneous of degree
  d and smooth on s < 0; for 2 < d < 3 it is of class C^(2, d - 2) near P (this regularity rests on the mechanism of the
  solution above; the verifier read it and did not recompute it). The solution above is d = 3 - 2/A. On the axis to the
  left of P the velocity of v is U_1[v](s, 0) = c_- |s|^d, and for d != 3 - 2/A, G_3 is a multiple of |s|^(d - 3), so
  G_3/H_3 is a multiple of |s|^(d - 3 + 2/A). At d = 5/2 and the computed parameters, c_- = 0.0205298 > 0 and
  G_3 = 0.0591966541429 |s|^(-1/2) (two separately computed routes, agreeing to 30 digits): this solution is of class
  C^(2, 1/2), smooth on s < 0, and G_3/H_3 tends to infinity at P. At d = 3 - 2/A, instead, c_- = 0: the left axis
  velocity of the solution above is smooth, while its l_3 is finite and nonzero. Reflected in s, such solutions are
  smooth on s > 0 and singular toward the centre; for a profile that is C^infinity near 0 that side is excluded by (C1).

(h) The endpoint condition above the exponent 1 - 2/A (nonlinear problem).
- Theorem (external referee; checked by the lead researcher and by the verifier). Let rho be an exact profile of the
  class that is C^(2,alpha) near P with alpha > 1 - 2/A and smooth near each point of the open axis segment from 0 to
  P. Then |d_y^2 rho(x* - r, y)| <= C |y| r^(alpha - 1) for |y| <= eps_0 r, hence
  |d_y^3 rho(x* - r, 0)| <= C r^(alpha - 1) and G_3/H_3 = O(r^(alpha - 1 + 2/A)) -> 0, so (C2') holds for j = 3 and
  l_3 = 0. With (C1) and the argument of (f): a profile in P_inf that is C^(2,alpha) near P with alpha > 1 - 2/A
  (0.803 on the computed branch) has B_3(c_l, w) = 0.
- Proof. It is local and uses three exact properties of the field W = c_l X + U near P: W is C^(2,alpha) there (the
  velocity law is of order 0 on Hoelder spaces up to a locally smooth far part; this mapping property follows from the
  Localization paragraph of (f) and the boundedness of order-0 multipliers on Hoelder-Zygmund spaces), div W = 2 c_l is
  constant, and W.grad rho = rho. With s = x - x*, W = (a, b), h = rho_y/a and c = 2 b_y - 1, the function
  K = rho_yy - h a_y solves (W.grad + c) K = F, where F contains derivatives of order at most two only: in the transport
  equation differentiated twice in y the term b_yy rho_y, which is only O(|y|^alpha), becomes -a_sy rho_y by the
  divergence identity and is absorbed into the transport derivative of h a_y. After subtraction of the explicit term
  -lambda y/s (lambda = a_yy(P) g*/A) the forcing is O(|y| r^(alpha - 1)) on a cone |y| < kappa r, and integration
  backward along characteristics up to the time theta log(|y|/r), with (1 - alpha)/(1 + alpha) < theta < 1/(A - 1),
  gives the bound; that interval is nonempty exactly when alpha > 1 - 2/A (at X3 and alpha = 0.85 it is (0.081, 0.109)).
  The lead researcher and the verifier checked the identity symbolically for arbitrary a, b and rho, the verifier also
  its leading coefficients on generic Taylor data and the exponent windows, and both the estimates, the characteristic
  integration and the distributional steps by hand. Bounds on the forcing alone do not give l_3 = 0: an explicit thin
  transverse layer, which is not a solution of the coupled problem, satisfies such bounds and has G_3/H_3 -> 1. The
  proof also uses the transport equation and the constant divergence.
- Cone form. The proof uses the Hoelder hypothesis only through C^2 regularity of rho and W near P and the two bounds
  |d_y^2 rho(x, y)| <= C |y|^alpha and |d_y^2 W_1(x, y) - d_y^2 W_1(P)| <= C |(x - x*, y)|^alpha on a cone
  |y| < kappa (x* - x), x* - r_0 < x < x*, with alpha > 1 - 2/A. The theorem holds under this cone form.
- Conormal modes. The conormal terms C |xi|^(mu_j) y^j of (d) with 2 < mu_j < 3 (at X3: j = 1, 3, 5, 7, 9, and
  mu_j - 2 < 1 - 2/A for j = 3 to 9; mu_11 < 2, so that term is not C^2) are of class C^(2, mu_j - 2) on every
  neighbourhood of P and no better; mu_1 - 2 = 0.931 and mu_3 - 2 = 0.734, against 1 - 2/A = 0.803 at X3. A profile that
  carries one of them with 3 <= j <= 9 fails the C^(2,alpha) hypothesis with alpha > 1 - 2/A, for a reason unrelated to
  l_3; the term with j = 1 is compatible with it. All of them satisfy the cone form: on the cone the terms are smooth,
  their contribution to d_y^2 rho is O(|y| (x* - x)^(mu_j + j - 3)), and their contribution to d_y^2 W_1 is
  O(R_P^(mu_j)), R_P = |(x - x*, y)|. In two dimensions their velocity is only C^(2, mu_j - 2) near P; their
  contributions to the axis trace w are of class C^(3, 0.93) or better. On the axis the term of order j adds
  C' |xi(x, 0)|^(mu_j) = const |x - x*|^(mu_j) (1 + O(|x - x*|)) to G_j, which is bounded, and through the y-dependence
  of xi (the curvature of the weak characteristic) a term |s|^(mu_j - k) to G_(j+2k), that is a relative order
  |s|^(g*/A - k(1 - 2/A)) in G_(j+2k)/H_(j+2k) (exponents 2.93, 2.13, 1.32, 0.52, -0.28, -1.08 at X3 for k = 0 to 5). At
  X3 these terms change none of l_3, l_5, l_7, while for j >= 9 the term of order j - 8 enters G_j/H_j at relative order
  |s|^(g*/A - 4(1 - 2/A)), with exponent about -0.28 (when d_y^2 W_1(P) != 0). This is compatibility with the
  hypotheses, not existence of a profile that carries such terms. [Corrected 2026-10-20: an interim version of this
  remark in 6.4 said that the velocity contributions of these terms are of class C^(3, 0.93); that holds for the axis
  trace only. An earlier version of this item listed j = 3, 5, 7, 9 at X3 and omitted j = 1.]
- A weaker statement, the existence of the limit l_3 under the same Hoelder hypothesis, with
  G_3/H_3 = l_3 + O(r^(alpha - 1 + 2/A)) + O(r^(2/A)), was also checked by the verifier; the theorem supersedes it.
- Scope. For A > 2 the Hoelder and cone hypotheses at P are additional to the definition of P_inf; for 1 < A <= 2 every
  profile of the class satisfies the Hoelder hypothesis (6.3.1 (m)). Sharpness of the exponent in the frozen model: (g),
  (j).
- Higher odd orders (external referee; audited by a second external referee; checked by the lead researcher and by the
  verifier). Let j >= 5 be odd and let rho be a profile of P_inf that is of class C^(j-1,alpha) near P with
  0 < alpha < 1 and alpha > 1 - (j-1)/A (at the computed parameters alpha > 0.606 for j = 5 and alpha > 0.409 for
  j = 7). Then |d_y^j rho(x* - r, 0)| <= C r^(alpha - 1), so G_j/H_j = O(r^(alpha - 1 + (j-1)/A)) -> 0, and the lower
  odd traces G_i, 3 <= i < j, are bounded at P. Hence l_i = 0 for every odd i with 3 <= i <= j, and smoothness near 0
  gives B_i(c_l, w) = 0 for each of these i for which p_i is not an even integer. At a resonant order (p_i an even
  integer, that is (i - 1)/A an even integer; for i = 5 only A = 2) smoothness requires instead that the Taylor
  coefficient [x^(p_i)] of x^(p_i + 1) F_i/(w H_i) vanish (otherwise G_i contains a multiple of H_i log x), and B_i need
  not vanish (6.4). In particular, for 1 < A <= 4 every profile of P_inf that is C^(4,alpha) near P for some alpha > 0
  has l_3 = l_5 = 0, B_3 = 0, and B_5 = 0 if A != 2. Proof (notation of the proof above: s = x - x*, r = -s, W = (a, b),
  h = rho_y/a). With n = j - 1, the function K_n = d_y^n rho - h d_y^(n-1) a solves (W.grad + n b_y - 1) K_n = F_n with
  F_n = (a_y d_y^(n-1) a/a - d_y^n a)(rho_s + b h) - sum_(k=1)^(n-1) binom(n, k)
  (d_y^k a)(d_s d_y^(n-k) rho) - sum_(k=2)^(n-1) binom(n, k) (d_y^k b)(d_y^(n+1-k) rho) + (a_s - (n - 1) b_y) h
  d_y^(n-1) a, which contains derivatives of order at most n; for n = 2 this is the equation of the proof above. It is
  the case E = 0, V = 2 c_l of an exact identity for arbitrary smooth a, b, f with a != 0: with E = a f_s + b f_y - f,
  V = a_s + b_y and K_n, F_n formed with f in place of rho, (W.grad + n b_y - 1) K_n - F_n = d_y^n E - (d_y^(n-1) a/a)
  E_y - f_y d_y^(n-1) V; the term (d_y^n b) f_y of the n times differentiated transport equation is carried by the last
  term. For rho and W of class C^n the equation for K_n holds in the sense of distributions, by local mollification in
  this identity on compact sets where a != 0 (its right side then tends to 0 in distributions, while K_n and F_n
  converge locally uniformly), and in flow coordinates the continuous function K_n satisfies its integral form along
  each characteristic. On a cone |y| < kappa r the first and the last term of F_n give (A - n) lambda_n y/s up to
  O(|y| r^(alpha - 1)), with lambda_n = g* d_y^n a(P)/A, the two sums are O(|y|), and
  (W.grad + n b_y - 1)(y/s) = (n - A) y/s + O(|y|); so R_n = K_n + lambda_n y/s satisfies (W.grad + n b_y - 1)
  R_n = O(|y| r^(alpha - 1)) and |R_n| <= C (|y|^alpha + |y| r^(alpha - 1)). Integration backward along the
  characteristic up to the time theta log(|y|/r), with (1 - alpha)/(n - 1 + alpha) < theta < 1/(A - 1), gives |d_y^n
  rho| <= C |y| r^(alpha - 1) on a smaller cone, and (C1) and parity give the bound on the axis. The window for theta is
  nonempty exactly when alpha > 1 - n/A; under this condition the exponential majorant of the forcing integral is
  integrable over the whole backward time, which gives a bound uniform in the time of integration. At the order j, with
  q_j = (j-1)/A, Q_j = W1_(j-1)/g^j and m = -w/g, the hierarchy of (a) gives F_j = L_j + (g^(j+1)/j) Q_j' with L_j
  bounded at P, and an integration by parts writes the integral of F_j/(w H_j) up to P as a boundary term plus two
  absolutely convergent integrals, with integrands O(r^(q_j - 1)) and (Q_j - Q_j(x*))
  m^(q_j - 2)/g = O(r^(q_j + alpha - 2)) (the derivative-free form of (i), as used for j = 3 in (f)); the original
  integral therefore converges as an improper integral. For the lower odd orders F_i/(w H_i) is absolutely integrable at
  P. Cone form: besides C^n regularity of rho and W near P, the proof uses only the two bounds |d_y^n rho| <= C
  |y|^alpha and |d_y^n a - d_y^n a(P)| <= C r^alpha on the cone. For j = 5 and 1 < A < 4, C^4 regularity of both rho and
  W near P suffices (the same argument with alpha = 0 and 1/3 < theta < 1/(A - 1)); the Localization of (f) is a
  statement with a positive Hoelder exponent, so C^4 regularity of W is then a separate hypothesis. Scope: in the
  C^(j-1,alpha) scale the exponent is the frozen threshold of (j), and, by the frozen theorem of (j) with
  beta = 4 + alpha, the frozen fifth-jet example of (j) is not C^(4,alpha) near P for alpha > 1 - 4/A, consistent with
  its C^(2,0.85699) regularity; unlike the third order for 1 < A <= 2 (m), the C^(2,alpha) regularity of the class does
  not give these hypotheses for j >= 5, for any A. The lead researcher checked the identity symbolically for n = 2, 4, 6
  and the estimates, the window and the integration by parts by hand; the verifier checked the identity symbolically
  with its own code for n = 2 to 8, the auxiliary identities and the general proof by hand, the cone estimates including
  the singular lines, the characteristic integration and the window, the hierarchy at order j and the integration by
  parts, the centre finite parts and the resonance condition (at j = 5 and A = 2 the condition L_5[w] = 0 of 6.4), the
  consequences for 1 < A <= 4 and the C^4 variant, and a scalar Hoelder example showing that absolute convergence of the
  original integral does not follow from the Hoelder bound alone.
- Fifth order under summable fourth-derivative growth (external referee; audited by a second external referee; checked
  by the lead researcher and by the verifier). Let 1 < A < 2 and q = 4/A. Suppose that f and W = (a, b) satisfy near P
  the transport equation W.grad f = f and div W = A + 1, with f and b odd and a even in y, W(P) = 0, DW(P) = diag(A, 1),
  f_y(P) = g* > 0, f and W of class C^(2,alpha) with 0 < alpha < 1, and smoothness on the left part of a punctured
  neighbourhood of P; the curl identity is not used. Choose r_0 > 0 and kappa > 0 so small that the cones below lie in
  that region, let R_n = 2^(-n) r_0, let A_n be the set of points (x* - r, y) with R_n/2 <= r <= R_n and |y| <= 2 kappa
  r, and let d_n = R_n^(q-1) sup_(A_n) (|D^4 f| + |D^4 W|), where D^4 denotes all spatial derivatives of total order
  four. If sum_n d_n < infinity, then l_5 exists and equals 0; more precisely, for R_(N+1) < r <= R_N with N large, r^q
  |d_y^5 f(x* - r, 0)| <= C (r^(q-2) + sum_(n >= N-3) d_n). Proof outline: K = f_yyyy - (f_y/a) a_yyy solves
  (W.grad + 4 b_y - 1) K = F_4 with F_4 as in Higher odd orders (n = 4). On a ball of radius c r about a point of the
  cone |y| <= kappa r the fourth derivatives are bounded by M = C r^(1-q) (d_(N-2) + ... + d_(N+2)); interpolation with
  the C^2 bound gives third derivatives O(r^(-1) + M^(1/2)), and parity then gives |F_4| <= C |y| (r^(-q)
  (d_(N-2) + ... + d_(N+2)) + r^(-2)) and |K| <= C r^(1-q) d_N there. Follow the backward characteristic from
  (x* - r, y), y != 0, until |y(t)| = kappa r(t); the exit radius tends to 0 as y -> 0. The relation A q = 4 gives J(t)
  |y(t)|/|y| <= C (r(t)/r)^q for the integrating factor J of 4 b_y - 1, uniformly in the exit time, because the O(r(t))
  errors have bounded time integral, and the time spent in each dyadic annulus is bounded. The exit term tends to 0,
  summability bounds the forcing integral, and q > 2 makes the remaining integral of r(t)^(q-2) finite; dividing by |y|
  and letting y -> 0 gives the bound. In particular a cone bound |D^4 f| + |D^4 W| <= C r^(-p) with p < q - 1 gives
  l_5 = 0 and |d_y^5 f(x* - r, 0)| <= C (r^(-2) + r^(-p-1)); for 1 < A < 4/3 the bound C r^(-2) suffices and gives
  |d_y^5 f(x* - r, 0)| <= C r^(-3), and the bound C r^(alpha - 2) gives l_5 = 0 when alpha > 3 - 4/A. As a regularity
  condition the hypothesis is weaker than C^4 regularity of both fields on a neighbourhood of P: bounded fourth
  derivatives give d_n <= C R_n^(q-1), and unbounded ones are allowed (for instance y (s^2 + y^2)^((2 + theta)/2) with
  0 < theta < 1 is of class C^(3,theta), not C^4, and has fourth derivatives O(r^(theta - 1)) on a left cone; this
  scalar function only compares the conditions and is not claimed to solve the equations). It is sharp in the following
  sense: the transport examples without the velocity law of (j), for 1 < A < 2, satisfy all the hypotheses except the
  summability, with c <= d_n <= C for all large n (|d_y^4 a| is of exact order r^(1-q) at points of the cut-off layer,
  and |D^4 a| <= C r^(1-q), |D^4 f| + |D^4 b| <= C r^(3-q)), and have l_5 = -1; so boundedness of d_n does not suffice
  for the transport equation with constant divergence. This concerns that system, not the coupled equations: whether the
  coupled equations, with the velocity law, imply sum_n d_n < infinity for every profile with only the regularity of the
  class is not established here. The same conclusion holds for every A >= 2 (external referee, in its audit of the
  above; audited by a second external referee; checked by the lead researcher and by the verifier), with the same d_n
  and the remainder r^q in place of r^(q-2): for q <= 2 summability makes the third derivatives of f and W bounded on
  the cone |y| <= kappa r (integrate the fourth derivatives along the rays (x* - r, eta r), |eta| <= kappa; the part of
  the ray in A_m contributes at most C R_m^(2-q) d_m), so |F_4| <= C |y| (r^(-q) (d_(N-2) + ... + d_(N+2)) + 1); the
  integrating-factor bound, which uses only A q = 4, and the exit term are as before, the remaining integral of r(t)^q
  is O(r^q), and r^q |d_y^5 f(x* - r, 0)| <= C (r^q + sum_(n >= N-3) d_n). At A = 2 the theorem still gives l_5 = 0; for
  a profile smooth near 0, compatibility of its fifth transverse trace with smoothness at 0 requires there the
  logarithmic condition L_5[w] = 0 of 6.4, not B_5 = 0. For 1 < A < 4 bounded fourth derivatives imply the hypothesis;
  for A >= 4 the weight R_n^(q-1) is at least 1, so the hypothesis requires the suprema of the fourth derivatives on A_n
  to tend to 0 at a summable weighted rate, and C^4 regularity on a neighbourhood of P alone does not imply it. For the
  transport equation with constant divergence, summability cannot be weakened to d_n -> 0: for every 1 < A < 4,
  replacing the primitive of the transport examples of (j) by F = r^(1-q) v^5 c(log |v|/log r)/(q - 1), with c smooth
  and nondecreasing, c = 0 on (-infinity, 4] and c = 1 on [5, infinity) (F given by its polynomial core value at v = 0,
  and F = 0 for s >= 0), gives pairs of class C^(3,(5-q)/4) near P, smooth on the punctured neighbourhood, with the same
  inner identities, now on |v| <= r^5 (W = (A s, y) and y = v + r^(-q) v^5 there), hence l_3 = 0 and l_5 = -1, and with
  d_n of exact order 1/n; there a - A s = r^(1-q) v^4 (5 (A t - 1) c'(t)/log
  r + ((A t - 1) c''(t) + A c'(t))/(log r)^2)/((q - 1)(1 + F_sv)), t = log |v|/log r. These pairs violate the curl
  identity. Whether a nonsummable rate below 1/n, such as d_n <= C/(n log n), suffices for that system is not decided,
  and for the coupled equations it is not decided whether d_n -> 0 suffices.
- Fifth order under a density bound (external referee; audited by a second external referee; checked by the lead
  researcher and by the verifier). Under the exponent condition below, the curl identity transfers bounds on the density
  alone to the summability hypothesis of the preceding bullet. Let 1 < A < 2, q = 4/A, and let f and W = (a, b) satisfy
  all the hypotheses of Fifth order under summable fourth-derivative growth except the summability, with class exponent
  0 < alpha < 1; assume in addition the curl identity b_s - a_y = -f_s near P, as for every profile of P_inf ((ii) of
  Local source structure in (j)), and, on a larger left cone |y| <= 4 kappa r, |D^4 f| <= C r^(-p) and |D^5 f| <= C
  r^(-P_0) with 0 <= p < q - 1 and P_0 finite. Then |D^4 W| <= C (r^(alpha - 2) + r^(-p) (1 + |log r|)) on the cone
  |y| <= 2 kappa r, hence d_n <= C (R_n^(q + alpha - 3) + (1 + n) R_n^(q - 1 - p)), so sum_n d_n < infinity and l_5 = 0
  if alpha > 3 - 4/A; this covers every class exponent for 1 < A <= 4/3 (at A = 4/3 the condition p < q - 1 is p < 2).
  If in addition D^3 W is bounded on the larger cone |y| <= 4 kappa r, r^(alpha - 2) can be replaced by r^(-1), and for
  1 < A < 2 the condition on alpha is not needed (the class exponent still satisfies 0 < alpha < 1). For p = 2 and
  1 < A < 4/3 the characteristic argument of the preceding bullet gives directly |d_y^5 f(x* - r, 0)| <= C r^(-3)
  (1 + |log r|). Proof outline: the divergence and curl identities give Laplace a = f_sy and Laplace b = -f_ss, so every
  second derivative u of a or b solves Laplace u = G with G a fourth derivative of f; this uses neither the transport
  equation nor a choice of global inverse. Let B be a ball of radius l = c r about a point of the smaller cone,
  contained in the larger one, and let M and L be the suprema of |D^4 f| and |D^5 f| on B. The class regularity gives
  |u - u(Z)| <= C l^alpha on B, with Z the centre; after rescaling B to the unit disc, splitting the principal-value
  integral for the second derivatives of the Newtonian potential at the radius min(1/8, M/(M + l L)) gives sup |D^4
  W| <= C (l^(alpha - 2) + M (1 + log(2 + l L/M))) on the concentric ball of radius l/2 (for M = 0 only the first term
  remains). The product M (1 + log(2 + l L/M)) increases in M and in l L, so the cone bounds can be inserted, and the
  polynomial bound on D^5 f costs only the logarithm; keeping the bound on D^4 f, a bound r^gamma [D^4 f]_gamma <= C
  r^(-p) for the Hoelder seminorm on such balls, 0 < gamma < 1, can replace the bound on D^5 f, by the interior Schauder
  estimate, and then the logarithm is absent. The logarithm cannot simply be dropped: a bound of D^2 u by sup |u| + sup
  |Laplace u| alone is false (smooth bounded right-hand sides equal to 1 - 2 Z_1^2/|Z|^2 on 2 eps < |Z| < 1/4 give d_1^2
  u(0) >= c log(1/eps) - C with u bounded). The j = 5 power-cutoff transport examples of (j), for 1 < A < 2, have |D^4
  f| <= C r^(3-q) and |D^5 f| <= C r^(-q) on a left cone, so they satisfy the density hypothesis with p = max(q - 3, 0)
  and P_0 = q, while |d_y^4 a| >= c r^(1-q) at points of the cut-off layer in every sufficiently small annulus; they are
  of class C^3, so every 0 < alpha < 1 is an admissible exponent for them, and for alpha > 3 - 4/A the velocity bound
  above would contradict this lower bound, consistent with their violating the curl identity directly. Neither part of
  the density hypothesis is established here for every profile with only the regularity of the class (smoothness on each
  punctured annulus gives finite norms there, not a polynomial bound as r -> 0). Without the transport equation the
  hypothesis does not follow: let v = sum_n 2^(-n) h_n^(2 + alpha) F((X - Z_n)/h_n), with F smooth, supported in the
  unit disc, odd in its second variable and with D^4 F not identically 0, Z_n = (x* - 3 R_n/4, 0) and h_n so small that
  the supports lie in the sets A_n and are disjoint; then f = g* y + v and W = (A s, y) + U[v] - T_1 U[v], with U[v] the
  velocity of v given by the multipliers of (ii) of Local source structure and T_1 the affine Taylor polynomial at P,
  are local pairs of class C^(2,alpha) with the source jets, the parities in y, the divergence and the curl identity,
  whose density has fourth-derivative supremum on A_n equal to c_F 2^(-n) h_n^(alpha - 2), c_F = sup |D^4 F| > 0, so
  that d_n can exceed any prescribed sequence; these are local pairs, not profiles. So a deduction of the summability
  hypothesis from the class regularity alone needs information beyond the local velocity identities, and the transport
  equation with constant divergence alone does not suffice either (the transport examples of (j)).

(i) The obstruction functional at nonsmooth axis data (external referee; checked by the lead researcher and by the
verifier). Let A != 2 and let w be an axis trace with the source conditions (w < 0 on (0, x*), w'(0) = -A,
w(x*) = 0, w'(x*) = A), odd near 0 and smooth on (0, x*), with
    w = -A x + d_3 x^3 + d_5 x^5 + d_7 x^7 + R(x),  |R^(i)(x)| <= M x^(7 + sigma - i) (i = 0, 1, 2), beta < sigma <= 2,
on 0 < x <= r for a fixed r, and w of class C^(2,theta) on [r, x*] with theta + beta > 1 (beta = 2/A). Rebuild g from
w (w g' = (w' - A) g, g/x^2 -> 1 at 0) and put Q_3 = a_2/g^3, m = -w/g.
- B_3(c_l, w) exists (a finite part at 0 and an improper integral at x*) and equals the convergent form
    ((beta - 1) A^(1 - beta)/3) f.p. int_0^{x*} (Q_3 - Q_3(x*)) m^(beta - 2) g^(-1) dx.
  (For A = 2, that is beta = 1, the same integration by parts gives B_3 = Q_3(x*)/6.)
- For aligned sources (the same x*) B_3 is locally Lipschitz in the norm
    sum_{j=1,3,5,7} |d_j| + sum_{i<=2} sup_{0<x<=r} x^(i-7-sigma) |R^(i)(x)|
      + sum_{i<=2} ||w^(i)||_{C^(0,theta)([r,x*])}
  (d_1 = w'(0)), also at data that are not smooth. [Corrected 2026-10-20: an interim version of this norm in 6.4
  controlled w only near x*; C^(2,theta) control on the whole interval [r, x*] is needed.]
- For a profile with the classical third axis equation on the open segment and an axis trace with these properties,
  both C_0 and l_3 = lim G_3/H_3 at P exist and C_0 = l_3 + B_3(c_l, w).
- Checks. The verifier derived the convergent form by hand and evaluated the original form, the convergent form and
  its own series values of B_3 on the compatible axis data of 6.3.2 (a) (L = 6, 8.6 and the zero L* of B_3): they
  agree to 4e-30 natural units, and to 15 digits at A = 4 and at A = 3. The lead researcher's evaluation of the
  convergent form agrees with the exact closed form of 6.3.2 (a) to 15 digits. The Lipschitz estimate and the
  existence statement were checked by hand (the Lipschitz estimate not numerically).
- Consequences. (1) For a profile that is C^infinity near 0 the origin hypothesis holds, so l_3 exists as soon as the
  axis velocity w is of class C^(2,theta) on [r, x*] with theta > 1 - 2/A (0.803 on the computed branch). This is a
  hypothesis on the axis trace only; it is compatible with the conormal terms of (h). Existence of l_3 is not its
  vanishing: for the solution of (g) the left axis velocity is smooth while l_3 is finite and nonzero; on the family
  of (g) the left axis velocity is of class C^(2, d - 2) for 2 < d < 3, d != 3 - 2/A. (2) For numerical states: if
  the axis traces converge in that norm, with aligned sources (and, if A varies, converging A and uniform margins
  sigma > beta, theta + beta > 1), B_3 converges, also when the limit is not smooth. Convergence of discrete solutions
  under grid refinement does not by itself give convergence in that norm, and a limit value of B_3 determines C_0 only
  together with l_3.
- Saddle modes. For a profile of P_2 that is not smooth at 0 the origin hypothesis is not known to hold. For an
  isolated mode C |x|^p y^j of the density at the saddle, the induced axis velocity is c_j C sgn(x) |x|^(p + j) plus a
  smooth odd function, with c_j = (-1)^((j-1)/2) j!/((p + 1) (p + 2) ... (p + j)) (checked symbolically by the
  verifier for j = 1, 3, ..., 11 and by the lead researcher for j = 3, 5, 7). For j = 3 and p = 6 + beta this is
  c = -6/((7 + beta)(8 + beta)(9 + beta)), and the mode C |x|^(6 + beta) y^3 satisfies the origin hypothesis.

(j) The frozen model at P: the endpoint theorem and the higher odd jets (external referee; checked by the lead
researcher and by the verifier). Notation of (g).
- Theorem (frozen model). With the dilation D = A s d_s + y d_y, b = g*/(2(A - 1)) and an elliptic Fourier multiplier
  Pi whose symbol is |zeta|^(2b) for |zeta| >= 2, (D + 2b - 1) Pi = Pi L_g up to an operator with compactly supported
  symbol. From this: let A > 1, g* > 0, let beta > 2 be noninteger and let v be odd in y and tempered, with L_g v = f
  near P for a smooth f, v of class C^beta near P and smooth near each point of the axis to the left of P. Then
  (x* - x)^((j-1)/A) d_y^j v(x, 0) -> 0 as x -> x* for every odd j >= 3 with j - (j-1)/A < beta < j (for beta > j
  this is immediate). For j = 3 and beta = 2 + alpha the condition is alpha > 1 - 2/A, so the exponent of the
  solution in (g) is sharp in the frozen model. (h) proves the corresponding statement for exact profiles without the
  frozen-model assumption of a smooth forcing.
- Proof outline. Pi turns the equation into (D + 2b - 1) u = smooth for u = Pi v, of Zygmund class C_*^(beta - 2b) (a
  negative exponent is allowed). Near the axis to the left of P, with r = x* - x > 0, the solutions of (D + c) u = 0 are
  r^(-c/A) phi(y r^(-1/A)), and the Taylor terms of phi have the isotropic exponents theta_m = m - (2b - 1 + m)/A; the
  Hoelder bound excludes those below beta - 2b, and a dyadic decomposition of Pi^(-1) carries the bound back to d_y^j v.
  For j = 3 at the computed parameters beta - 2b < 0 < theta_1 = 0.680, and the steps of the proof for beta - 2b >
  theta_1 are not needed; for j = 5, beta - 2b lies in (1.355, 1.749), above theta_1, and those steps are used (checked
  by hand by the verifier). [Corrected 2026-10-20: an earlier version stated the first clause without the restriction to
  j = 3.]
- Checks. The verifier checked the conjugation identity symbolically on an arbitrary Fourier transform (with a control
  computation in which the identity fails), the homogeneous solutions and their exponents symbolically, the smooth
  particular solution numerically (residual 8.5e-19), and the reduction and the dyadic estimates line by line by
  hand. The lead researcher checked the identity and the exponents.
- Higher odd jets. The sufficient frozen thresholds for the j-th endpoint condition under C^(2,alpha) regularity are
  alpha > j - 2 - (j-1)/A, that is 0.803 for j = 3 and 2.606 for j = 5 at the computed parameters; the threshold for
  j = 5 is 3 - 4/A, which is at least 1 for A >= 2, so for A >= 2, in particular at the computed parameters, this
  sufficient criterion cannot be met in the C^(2,alpha) scale for j = 5 (for 1 < A < 2 it is below 1). [Clarified
  2026-10-20: an earlier version did not state the range of A.] At the computed parameters
  (A = 10.150725214760579, the value of the stored trace, and g* approximately 29.74949) there is an exact frozen
  solution of class C^(2,alpha_f), alpha_f = 2b - 4/A - 2 approximately 0.85699, smooth
  to the left of P, with G_3/H_3 -> 0 but G_5 |x - x*|^(4/A) -> -1/(240 sin(4 pi/A)) approximately -0.00440858698 (so
  the window
  1 - 2/A < alpha <= 0.85699 is nonempty); the verifier confirmed the constant by a physical-space computation that does
  not use the Fourier moment of the referee's derivation (agreement to 15 digits). For j >= 5 the endpoint hypotheses
  (C2') of (a) at the orders 5 <= i <= j are therefore not supplied by the frozen criterion from C^(2,alpha)
  regularity at the computed parameters (the example is a solution of the frozen model, not a counterexample for the
  nonlinear problem), and no endpoint theorem at these orders from C^(2,alpha) regularity alone is established in this
  report; the order 3 is covered by (h) under its Hoelder hypothesis and by (m) for 1 < A <= 2, and in the scale
  C^(j-1,alpha) at P, with 0 < alpha < 1 and alpha > 1 - (j-1)/A, all these endpoint conditions follow from (h), Higher
  odd orders. For a trial whose source jets d_y^i rho(x, 0) with odd 3 <= i <= j stay bounded at P, l_i = 0 for these i;
  for an exact profile with these endpoint limits, smoothness at 0 implies B_j(c_l, w) = 0 for odd j >= 3 with p_j not
  an even integer.
- Fifth-order frozen examples (external referee; audited by a second external referee; checked by the lead researcher;
  checked by the verifier by a separate physical-space proof, an FFT check of cut-off versions and its own computation
  of the jets and Hoelder classes). In the frozen model of (g), L_g v = (A s d_s + y d_y - 1) v + g* U_2[v], let
  V_A(s, y) = int_0^y (s^2 + t^2)^((A-1)/2) dt and Q_A(s, y) = s int_0^y (s^2 + t^2)^((2A-3)/2) dt. The three choices
  V_(5/2), Q_(7/4) and Q_2, with g* = 21/4, 27/8 and 5 respectively, are exact tempered solutions with zero forcing:
  U_2[v] = -(A s d_s + y d_y - 1) v/g* solves -Laplace U_2 = d_s^2 v in the sense of distributions and is the only
  solution homogeneous of the degree of v with its parities. For a cut-off chi equal to 1 near P, U_2[chi v] - U_2[v] is
  harmonic near P, so chi v solves L_g(chi v) = f near P with f smooth, the setting of the frozen theorem above (also
  checked numerically by the verifier). They are odd in y and smooth where s != 0. V_(5/2) and Q_(7/4) are of class
  C^(2,1/2) near P and of no class C^(2,beta) with beta > 1/2; Q_2 is of class C^(2,alpha) for every alpha < 1 but not
  C^(2,1). With G_j = d_y^j v(s, 0)/j! and Z_j(r) = r^((j-1)/A) G_j(-r), whose zero, finite nonzero and divergent limits
  have the meaning of those of G_j/H_j (up to the positive normalizing constant of H_j): for Q_(7/4), Z_3 = -r^(9/14)/12
  and Z_5 = (3/160) r^(-3/14); for Q_2, Z_3 = -r/6 and Z_5 = 1/40; for V_(5/2), Z_3 = r^(3/10)/4 and Z_5 = -(3/160)
  r^(-9/10). So all third limits vanish, while the fifth normalized trace diverges (Q_(7/4), V_(5/2)) or has a finite
  nonzero limit (Q_2). The examples are smooth near each point of the axis to the left of P, but singular on the line
  s = 0 away from P, so they are not smooth on the whole punctured neighbourhood of P. Separately, their fourth
  derivatives do not satisfy the cone bounds that the proof of Higher odd orders in (h) uses; for instance d_y^4
  Q_2(-r, kappa r) = 3 kappa (1 + kappa^2)^(-5/2)/r on every left ray. They satisfy the hypotheses of the frozen theorem
  above (regularity, smooth forcing, temperedness, smoothness to the left of P) but lie below its fifth-order threshold
  alpha > 3 - 4/A (5/7, 1 and 7/5 at A = 7/4, 2, 5/2). So in the frozen model C^(2,alpha) regularity at P with
  smoothness to the left of P does not force l_5 = 0 at these three parameter pairs (alpha = 1/2 at A = 7/4 and 5/2,
  every alpha < 1 at A = 2), including A = 7/4 in the range 1 < A < 2 where the third-order condition holds for every
  profile (m); at A = 2 the fifth-order condition of smoothness at 0 is the logarithmic one (6.4), which does not
  involve l_5, so there Q_2 bears on the source jet only. The examples are consistent with the frozen theorem and do not
  show that its threshold is sharp; for 1 < A <= 4/3 every class exponent alpha > 0 satisfies that threshold. The
  examples are solutions of the frozen model, not profiles: they grow with degrees 5/2, 5/2 and 3, faster than the class
  allows. Nonlinear remainder (verifier; checked by the lead researcher; audited by an external referee): with the
  potentials Phi of these examples (Laplace Phi = v) and U[v] = (Phi_sy, -Phi_ss), the pair f = g* y + eps v, W = (A s,
  y) + eps U[v] satisfies the divergence and curl equations exactly, and its transport defect W.grad f - f is exactly
  eps^2 h with h = U[v].grad v. The function h is odd in y, and at every fixed y != 0 it is, as a function of s across
  s = 0, of class C^(2,1/2) and not C^3 for V_(5/2), of class C^(1,1/2) and not C^2 for Q_(7/4), and of class
  C^(1,alpha) for every alpha < 1 and not C^2 for Q_2 (for y > 0 the singular parts, modulo analytic functions of s, are
  -(2/7) C_V (s^2 + y^2)^(3/4) |s|^(5/2), (2/9) C_Q (y^2 - s^2) (s^2 + y^2)^(1/4) |s|^(3/2) and -(1/10) s^2 (y^2 - s^2)
  (s^2 + y^2)^(1/2) log|s|, with nonzero constants C_V, C_Q from the expansions V_(5/2) = analytic + C_V |s|^(5/2) and
  Q_(7/4) = analytic + C_Q s |s|^(3/2) at fixed y > 0; for y < 0 they have the opposite signs). So none of the three
  gives smooth forcing at second order. For the two Q examples there is the following restricted obstruction: for
  eps != 0 there is no exact solution of W.grad f = f, div W = A + 1 and b_s - a_y = -f_s (W = (a, b)) on a
  neighbourhood of P of the form f = g* y + eps Q_A + w, W = (A s, y) + eps U[Q_A] + Z with w of class C^(3,alpha) for
  some 0 < alpha < 1 and Z of class C^2 (no boundary condition on Z). Indeed div Z = 0 and d_s Z_2 - d_y Z_1 = -w_s make
  Z of class C^(3,alpha); at fixed y0 != 0 the only term of the transport equation that is not C^2 in s is the nonsmooth
  part of eps W_1(0, y0) d_s Q_A (a multiple of |s|^(3/2), respectively s^2 log|s|), so W_1(0, y) = 0 for small y != 0,
  that is Z_1(0, y) = -eps |y|^(2A-1)/((2A-1)(2A+1)), which is not of class C^3 at y = 0 (|y|^(5/2) and |y|^3). This
  concerns additive C^(3,alpha) corrections of the fixed singular-line examples and gives no exclusion for corrections
  in their original class C^(2,alpha) or for configurations whose singular curve moves: if a family has velocity first
  variation exactly U[Q_A], with no further contribution of order eps, a differentiable expansion s = eps
  sigma(y) + o(eps), y > 0, of an invariant singular curve must satisfy y sigma' - A sigma = U_1[Q_A](0,
  y) = y^(2A-1)/((2A-1)(2A+1)), with solutions sigma = y^(2A-1)/((A-1)(2A-1)(2A+1)) + C y^A (particular coefficients
  16/135 at A = 7/4 and 1/15 at A = 2); this is a necessary first-order tangency calculation, not a construction. The
  argument constructs no nonlinear counterpart of the examples and gives no exclusion in the original C^(2,alpha)
  correction class. Further forms of the obstruction and a formal construction (external referee; audited by a second
  external referee; checked by the verifier with its own symbolic computations; the inconsistency at angular index 9 for
  Q_2 and the example in (iii) checked by the lead researcher): (i) for either Q example, with D_A = A s d_s + y d_y,
  the second-order amplitude equation (D_A - 1) w_2 + g* B_2 = -U[Q_A].grad Q_A, with div B = 0 and d_s B_2 - d_y
  B_1 = -d_s w_2, has no pair (w_2, B) of class C^(1,1) near any point (0, y0), y0 != 0, of the fixed line s = 0 (after
  integration against a smooth nonnegative nonzero function of y supported near y0, the left side of the first equation
  is affine in s up to O(s^2), while the integrated forcing contains a nonzero multiple of |s|^(3/2), respectively s^2
  log|s|), so an exact family with the prescribed leading pair has no second-order amplitude expansion in C^2 on a fixed
  neighbourhood; (ii) with R = sqrt(s^2 + y^2), for each fixed eps != 0 no exact local solution f = g* y + eps Q_A + e,
  W = (A s, y) + eps
  U[Q_A] + E satisfies |D^j e| + |D^j E| <= C R^(2d-1-j), j = 0, 1, 2, d = 2A - 1, throughout a punctured neighbourhood
  of P (rescaling near (0, lambda), lambda -> 0, would give a C^(1,1) solution of the equation of (i)); neither
  statement excludes a solution, for instance one with a moving singular line, that fails these amplitude or remainder
  hypotheses, remainders of lower order, or bounds of that order on a left cone only; (iii) for h = O(R^M), M > 1, the
  backward integral I h(s, y) = int_(-infinity)^0 e^(-t) h(e^(A t) s, e^t y) dt converges, is O(R^M) and is the unique
  inverse of D_A - 1 in that order class along characteristics (classical spatial regularity needs a separate argument),
  but it does not preserve smoothness at the left axis: for A = 5/2 and h = y R^3 it gives I h = 2 y [R^5 - |y|^5]/(15
  s^2) for s != 0, which is not of class C^6 at y = 0 for fixed s < 0, although the forcing is smooth on the punctured
  plane; (iv) on a left cone s = -r < 0, |y| < kappa r, 0 < kappa < 1, each of the three examples admits formal
  corrections to every finite order, finite sums of terms r^(p_n) (log r)^l with coefficients analytic in y/r,
  p_n = 1 + (n + 1)(d - 1), where d = 5/2, 5/2, 3 is the degree of V_(5/2), Q_(7/4), Q_2; every finite truncation
  satisfies the divergence and curl equations exactly and the transport equation up to a remainder of increasing order,
  and keeps the limits of Z_3 and Z_5 of the example; within this expansion with analytic angular coefficients, Q_2
  requires a term in log r already at the first correction (degree 5; compatibility defect -1/120 at angular index 9).
  No bound uniform in the order, no convergence and no extension across s = 0 follows, and no exact nonlinear solution
  is obtained. They do not decide whether exact profiles of P_inf have
  l_5 = 0, and their source slopes are not those of the R12 data at the zero of B_3 (6.5).
- Transport examples without the velocity law (external referee; audited by a second external referee; checked by the
  lead researcher and by the verifier). Under the regularity of the class, the transport equation and the constant
  divergence alone do not imply the fifth-order endpoint condition. (Higher odd orders in (h) assumes more: with f and W
  of class C^(4,beta), its fifth-order proof uses the transport equation and the divergence, while the velocity law
  supplies the regularity of W from that of f; the frozen theorem above assumes the frozen velocity relation with smooth
  forcing.) For every 1 < A < 4 there are local solutions near P of W.grad f = f and div W = A + 1, with f and b odd and
  a even in y, W = (a, b), W(P) = 0, DW(P) = diag(A, 1) and f_y(P) = 1, such that f and W are of class C^(3,beta*) near
  P with beta* = (4 - 4/A)/3 (sharp for the pair: a belongs to no class C^(3,beta) with beta > beta*) and smooth on the
  punctured neighbourhood of P, and such that on the left axis G_3 = 0 and G_5(x* - r) = -r^(-4/A). There w = A s and
  g = 1, and with the local normalization H_j = r^(-(j-1)/A) one has l_3 = 0 and l_5 = -1. Construction: with
  s = x - x* = -r, q = 4/A, a smooth even cut-off chi equal to 1 on [-1, 1] and to 0 outside (-2, 2), and
  F(s, v) = r^(1-q) v^5 chi(v/r^3)/(q - 1) for s < 0, F = 0 for s >= 0, one has 1 + F_sv >= 1/2 near P, and u = s + F_v,
  y = v + F_s define an area-preserving change of coordinates; W is the pull-back of the linear field (A u, v) and
  f = v, so both equations hold exactly, also in the cut-off layer. Where |v| < r^3 the relation A q = 4 gives
  W = (A s, y) and y = v + r^(-q) v^5, hence the axis jets. The perturbations are supported in s < 0, |y| <= 2 r^3; with
  Y = y/r^3 they are f - y = r^(15-q) Phi_0, b - y = r^(15-q) Phi_2 and a - A s = r^(13-q) Phi_1 with Phi_i smooth in
  (Y, r^(12-q)) uniformly, each s-derivative costing one power of r and each y-derivative three, so the derivatives of
  order at most two are o(r) and the third derivatives tend to 0, which gives the C^3 extension and the Hoelder
  exponent. At points of the cut-off layer in every fixed left cone |d_y^4 a| is of exact order r^(1-q), so the bounded
  fourth derivatives used in Higher odd orders fail for every 1 < A < 4 (the weaker bound |D^4 W| <= C r^(alpha - 2)
  fails for these examples exactly when alpha > 3 - 4/A). The pairs violate the curl identity b_s - a_y = -f_s of the
  velocity law (in the inner region b_s - a_y = 0, while f_s != 0 off the axis), and no harmonic correction of the
  stream function repairs this while the density is fixed. Nor does f - y solve the frozen equation with smooth forcing:
  in the inner region its transport part vanishes, so its frozen velocity would be a smooth function H with -Laplace
  H = f_ss there, while d_y^5 f_ss(-r, 0) = -120 q(q + 1) r^(-q-2) is unbounded. So these are neither profiles nor
  frozen examples with smooth forcing. They show that the transport equation, the constant divergence, the parities and
  the source structure, C^3 regularity at P and smoothness on the punctured neighbourhood do not imply l_5 = 0; for
  1 < A < 4/3 they also violate the sufficient axis bound |d_y^5 f(x* - r, 0)| <= C r^(-3). With v^j and q_j = (j - 1)/A
  in place of v^5 and q the same construction gives, for every odd j >= 5 and every A > 1 with A != j - 1, pairs of
  class C^3, smooth on the punctured neighbourhood, with G_i = 0 for odd 3 <= i < j and l_j = -1 in the normalization
  H_j = r^(-q_j) (for A > j - 1 the factor 1/(q_j - 1) is negative, which changes nothing). For j = 5 and A > 4 these
  pairs are of class C^4 near P, with sharp common Hoelder exponent (1 - 4/A)/3 of the fourth derivatives (attained by
  a; the density alone is of class C^(4,1 - 4/(3A))), which is below the threshold beta > 1 - 4/A of Higher odd orders;
  they violate the velocity law, which would give W the regularity of f, so this does not contradict that theorem. At
  A = j - 1 (for j = 5 this is A = 4, c_l = 5/2) the primitive F = -log(r) v^j chi(v/r^3), F = 0 for s >= 0, in the same
  construction gives such pairs as well (verifier; audited by an external referee; checked by the lead researcher). In
  its inner region |v| <= r^3 the field W = (A s/J, y + A j r^(-2) v^(2j-1)/J), J = 1 + j r^(-1) v^(j-1), is not linear,
  but W - (A s, y) = (d_y (A f^j), -d_s (A f^j)) is tangent to the level sets of f, so that (A s d_s + y d_y) f = f
  still holds there; at fixed r, f = y - r^(-1) y^j + O_r(y^(2j-1)) gives G_j = -r^(-1) = -H_j, and the curl defect
  b_s - a_y + f_s has the leading term -A j (j - 1) y^(j-2) as y -> 0. For j = 5 this pair is of class C^(3,beta) for
  every 0 < beta < 1, a is not of class C^(3,1), and d_n is of exact order n. So for every A > 1 the transport equation,
  the constant divergence, the parities, the source structure, C^3 regularity at P and smoothness on the punctured
  neighbourhood do not imply l_5 = 0. These local examples do not decide the endpoint condition for profiles.
- Local source structure and what the velocity law controls at P (external referee; audited by a second external
  referee; checked by the lead researcher and by the verifier). Put P at the origin, s = x - x*, r = -s, W = (a, b) = L
  X + R_W with L = diag(A, 1), and let Phi_t be the flow of W; assume the regularity of the class (f and W of class
  C^(2,alpha) near P), the parities and f_y(P) = g* > 0. (i) For 1 < A < 2 the limit Xi(X) = lim_(t -> -infinity)
  e^(-L t) Phi_t X = X - int_(-infinity)^0 e^(-L t) R_W(Phi_t X) dt exists and is a C^1 chart with Xi(0) = 0 and D
  Xi(0) = I that conjugates the flow of W to that of L. The bounds |R_W(X)| <= C |X|^2 and |DR_W(X)| <= C |X| (which
  hold
  for W of class C^(1,1)) justify the convergence and the differentiation of the integral; for W of class C^(1,gamma)
  only, these estimates give the construction only for A < 1 + gamma, but the velocity law with f of class C^(2,alpha)
  gives W of class C^(2,alpha) by (ii). Every classical solution of W.grad f = f that is differentiable at P with
  Df(P) = (0, g*) equals g* Xi_2, so the density is the slow linearizing coordinate of W. Since the chart is only known
  to be C^1, this identity gives no bound on derivatives of order five. (ii) The local equations div W = A + 1 and curl
  W = b_s - a_y = -f_s hold exactly; the velocity law determines W from the density near P up to a field with zero
  divergence and zero curl, locally a harmonic gradient. They give Laplace a = f_sy and Laplace b = -f_ss, and on the
  axis the relations used in the hierarchy of 6.3.1 (a). The velocity multipliers xi eta/(xi^2 + eta^2) and
  -xi^2/(xi^2 + eta^2) are homogeneous of degree 0, so the velocity law alone gives no general gain of derivatives. The
  transport identity for K_4 = f_yyyy - (f_y/a) a_yyy, which uses the transport equation and the constant divergence but
  not the curl, contains derivatives of order four, among them a_yyyy and f_syyy, that the class does not bound at P;
  Higher odd orders in 6.3.1 (h) assumes the additional regularity that bounds them (for the fifth order, f and W of
  class C^(4,beta) with beta > 1 - 4/A), and Fifth order under summable fourth-derivative growth in 6.3.1 (h) needs
  instead a summable weighted bound on the fourth derivatives in a left cone, which the j = 5 transport examples above
  violate. For 1 < A < 2, the curl identity and the additional bounds |D^4 f| <= C r^(-p), |D^5 f| <= C r^(-P_0) on a
  larger left cone imply this weighted summability when 0 <= p < 4/A - 1, P_0 is finite and alpha > 3 - 4/A (Fifth order
  under a density bound in 6.3.1 (h)). An estimate that uses the coupled equations in another way is not excluded. (iii)
  The velocity law does suppress the velocity of thin odd structures: for p(s, y) = M F((s - s0)/r, y/h), with F a
  Schwartz function odd in its second variable and 0 < h <= r, the velocity of p given by the whole-plane velocity
  operator satisfies sup |U_1 p| <= C_F |M| h/r and sup |U_2 p| <= C_F |M| (h/r)^2, with constants depending only on F;
  the oddness supplies the transverse cancellation, and no moment condition in the first variable is needed. For h = r^3
  the factors are r^2 and r^4. In the power-cutoff transport examples without the velocity law above with j = 5 and
  A != 4, the perturbations live in layers of width of order r^3, with a - A s of amplitude r^(13-q), which is r^(-2)
  times the density perturbation amplitude r^(15-q) of f - y, and b - y of the same amplitude as f - y. Those examples
  already violate the curl identity, so they are excluded directly; the suppression estimate suggests (heuristic) that
  the same mechanism cannot survive the coupling. A proof along these lines would need bounds uniform in the shape,
  control of the interactions and control of the smooth local remainder; a bound in terms of amplitude and widths alone,
  uniform over shapes, fails for packets that oscillate horizontally on the scale h (for each fixed F the estimate
  holds). (iv) The additional axis bound |d_y^5 f(x* - r, 0)| <= C r^(alpha - 3) implies l_5 = 0 when alpha > 3 - 4/A:
  the weaker bound C r^(-3) suffices for 1 < A < 4/3, A = 4/3 needs some alpha > 0, and at equality a bound of this form
  gives only boundedness of G_5/H_5. With T_2 f the quadratic Taylor polynomial of f at P, the bound is equivalent to a
  bound, uniform in r, on the fifth transverse derivative at (-1, 0) of (f - T_2 f)(r X)/r^(2 + alpha). The regularity
  of the class and smoothness on the punctured neighbourhood do not imply it: the j = 5 transport examples above have
  |d_y^5 f(x* - r, 0)| = 120 r^(-4/A), which violates it exactly when alpha > 3 - 4/A. No such bound, and no other
  fifth-order endpoint theorem, is established here for every profile with only the regularity of the class; Fifth order
  under summable fourth-derivative growth in 6.3.1 (h) gives l_5 = 0 under an additional weighted hypothesis, and Fifth
  order under a density bound there gives it under density bounds with the curl identity.
(k) Sign criterion for B_3 (external referee; audited by a second external referee; checked by the lead researcher and
  by the verifier). Let A > 2, beta = 2/A, and let w be an axis trace with the source conditions of 6.3.1 (i), smooth
  and odd near 0, w = -A x + d_3 x^3 + d_5 x^5 + d_7 x^7 + O(x^9), smooth on (0, x*) and of class C^(2,theta) at x* with
  theta > 1 - beta. Rebuild g from w, and put Q = (g' - w'')/(2 g^3) (the Q_3 of 6.3.1 (i)) and m = -w/g, which
  decreases from +infinity to 0 (m' = -A/g). Let
    P(m) = pi_5 m^5 + pi_3 m^3 + pi_1 m,  pi_5 = (1 - 3 d_3)/A^5,  pi_3 = -(10 A d_5 + 12 d_3^2 - 3 d_3)/A^4,
    pi_1 = -(168 A^2 d_7 + 324 A d_3 d_5 - 10 A d_5 + 144 d_3^3 - 21 d_3^2)/(8 A^3),
  the divergent part of Q at the centre (Q - P(m) = O(1/m) as m -> infinity). Then B_3 is the ordinary, absolutely
  convergent integral
    B_3 = ((beta - 1)/(3 A^beta)) int_0^infinity [Q(x(m)) - P(m) - Q(x*)] m^(beta - 2) dm.
  This is the convergent form of 6.3.1 (i) in the variable m, after subtraction of P, whose finite-part integral is 0.
  Since beta < 1, the pointwise condition
    (H_-)  Q(x) - P(m(x)) <= Q(x*) for 0 < x < x*, with strict inequality somewhere,
  implies B_3 > 0. With 6.3.1 (h): no profile in P_inf that is C^(2,alpha) near P with alpha > 1 - 2/A has axis data
  satisfying (H_-) (for such a profile the trace hypotheses above hold: smoothness and oddness at 0 by P_inf and the
  symmetry of the class, smoothness on the open segment by (C1) of 6.3.1 (f), the class C^(2,alpha) at x* by the Hoelder
  mapping property of the velocity law used in 6.3.1 (h), and rho_y(x, 0) is the g rebuilt from w, by the order-y part
  of the transport equation and the normalization a(0) = 1; checked by the verifier by hand). On the compatible axis
  data of 6.3.2 (a), x*^5 (Q - P(m) - Q(x*)) = (1 - 6k)(u^5 - 1) + (1 + 2k)(u^3 - 1) with k = A/L^2 and u = x/L, so
  (H_-) holds there exactly when L^2 >= 3A; the zero L^2 = S_A of B_3 lies between 2A and 3A and fails (H_-). For
  1 < A < 2 the same formula holds without the subtraction of Q(x*), and for A = 2 the same computation gives
  B_3 = Q(x*)/6 = w''(x*)(g* - 2)/(24 g*^3). The lead researcher checked the derivation by hand, the coefficients pi_j
  and the polynomial remainder symbolically, and the integral numerically against the closed form of 6.3.2 (a)
  (agreement to 1e-9 relative at L = 7 and 8.6, and to 5e-11 absolute, in natural units, at the zero). The verifier
  checked the coefficients pi_j and the remainder symbolically for general odd w (the x^6 coefficient of x^5 (Q - P(m))
  depends on d_9, so P is exactly the divergent part), the integration by parts, the boundary terms, the vanishing
  finite part of P and the invariance under the change of cutoff by hand, and the integral at 30 digits against an
  independent Beta-function closed form on the compatible data (2e-30 relative for L from 4 to 10 at the computed A, and
  at A = 4, 3, 1.5, 1.25) and against the finite-part value of 6.3.1 (i) on two compatible traces outside that family
  (absolute differences at most 2e-27 natural units at A = 10.150725, at most 1.2e-26 for the form without subtraction
  at A = 1.5, and at most 8e-32 for the formula at A = 2). The second referee confirmed the statement exactly with these
  hypotheses; in particular the nonexistence statement needs A > 2 as an explicit assumption (R2 gives only A > 1).
- Reading. This is a proved conditional nonexistence theorem under an explicit pointwise hypothesis on the axis trace
  of the profile itself and an explicit regularity hypothesis at the source. It is not counted here as NO_inf, under
  the reporting convention of 6.1: (H_-) is an inequality on the profile's own axis data that implies the sign of the
  obstruction functional (it is stronger than B_3 > 0, not equivalent to it); no structural property of profiles
  (velocity law, positivity, growth) is known to imply it; it is supported for the computed branch only by trial data
  (6.4); and compatible axis data with B_3 = 0 that violate it exist. The verifier concurs. One external referee holds
  that the theorem, together with the versions using the weaker tests of 6.4, already meets the permitted form
  "nonexistence under explicit hypotheses"; a second referee classifies it as a conditional exclusion and leaves the
  general question open. A third referee finds the classification defensible and notes that the convention of 6.1 is
  stricter than the task requires. The report does not adopt the first reading, for the reasons just given; the first
  referee also states that no implication from a structural hypothesis such as (Hmin) of R9 to (H_-) or to B_3 != 0 is
  established.
(l) First variation and positivity (external referee; audited by a second external referee; checked by the lead
  researcher and by the verifier). For A > 2 and a compatible reference trace that is smooth through both endpoints (for
  instance the data of 6.3.2 (a)), at fixed A and x*, the derivative of B_3 along compactly supported variations of w
  inside (0, x*) is the pairing with a weight lambda(x) that is singular as x^(-8-beta) at 0. Pulled back to the density
  through the velocity law (U_1 = -R_1 R_2 rho), it is the pairing with Phi(u, v) = (1/2) d_u (P_v * lambda_o)(u),
  v > 0, where P_v is the Poisson kernel of the half-plane and lambda_o is the compactly supported odd distribution on
  [-x*, x*] that represents the derivative on odd variations of the whole axis: it equals lambda/2 on (0, x*), and its
  definition includes the finite parts at 0 and at +-x* and the terms of the three fixed-parameter constraints below
  (lambda itself is not integrable at 0). Phi is the weight of the pairing with the variation of rho over the whole
  plane (4 Phi for the first quadrant). [Corrected 2026-10-20: an earlier version called lambda_o the odd extension of
  lambda, which is neither correctly normalized nor integrable; the sign argument is unchanged.] Since P_v * lambda_o is
  odd in u and decays, int_0^infinity Phi(u, v) du = 0 for every v > 0, while Phi is not identically 0. So Phi takes
  both signs on every horizontal half-line of the first quadrant, and positivity of rho there (R9) cannot by itself give
  a sign to the first variation of B_3. The verifier checked the variation formula symbolically, the weight against a
  finite difference of the exact functional for a compactly supported bump at 34 digits (relative 2e-23), its leading
  behaviour lambda ~ (1 - beta)(6 + beta)(7 + beta)/(6A) x^(-8-beta) at 0 and its behaviour at x*, the kernel identity
  K_1 = (1/2) d_u P_v and the sign argument. The second referee confirmed the statement, with one qualification: it
  concerns the derivative on the tangent space of axis traces at fixed A and x* (odd directions v with v'(0) =
  v(x*) = v'(x*) = 0); positive perturbations of rho that give either sign of the first variation (constructed by that
  referee and not checked by the verifier; 6.4) do not in general solve the linearized transport equation, so neither a
  sign on the tangent space of the coupled problem nor a nonlinear sign for exact profiles is excluded.
(m) The range 1 < A <= 2 (1 < c_l <= 3/2; the lead researcher's reading of 6.3.1 (h) and R10, confirmed by an external
  referee, who gave the direct third-order proof below; checked by the verifier by hand, the formula at A = 2 and the
  pair below also symbolically). For 1 < A <= 2 the exponent 1 - 2/A is <= 0, so the Hoelder hypothesis of 6.3.1 (h) at
  P is part of the class (rho of class C^(2,alpha) near P for some alpha > 0). The other inputs of 6.3.1 (h) and (f) do
  not depend on A: p_3 = 6 + 2/A lies in [7, 8) and is not an even integer, and at A = 2 the resonance of the source
  eigenvalues (2, 1) is not used, since the proof integrates along the characteristics of W in a cone at P. Hence
  l_3 = 0 and B_3(c_l, w) = 0 for every profile of P_inf with 1 < A <= 2, without a bound on d_y^3 rho at P, an extra
  Hoelder hypothesis or (Hmin). The argument uses the transport equation, div W = A + 1, the parity of the class, W and
  rho of class C^(2,alpha) along the open segment and near P, the first-source geometry of R5 (w < 0 on (0, x*),
  w'(P) = A, d_y W_2(P) = 1, g* > 0) and smoothness near 0, which starts the third trace and identifies its finite part
  at the centre; without smoothness near 0 the class P_2 alone does not suffice. The referee gives a direct proof of the
  third-order step that does not use (C1) of 6.3.1 (f): with W = (a, b), D = W.grad and f = rho, the function
  K = f_yy - (f_y/a) a_y satisfies (D + 2 b_y - 1) K = F, where F = (a_y^2/a - a_yy)(f_x + b f_y/a) - 2 a_y
  f_xy + (a_x - b_y)(f_y/a) a_y contains derivatives of W and rho of order at most two (this expression is from a second
  external referee; checked symbolically by the lead researcher with the transport equation and div W = A + 1, and by
  the verifier symbolically for generic fields with the same two identities, together with the continuity of F/y up to
  the axis, the axis limit and the cone step at P by hand); on compact subsegments F/y extends continuously through the
  axis and (D + 2 b_y - 1 + b/y)(K/y) = F/y, and integration along the forward characteristics, which reach the smooth
  neighbourhood of 0, gives the axis limit M = lim K/y = 6 G_3 - 2 g a2/w on the open segment, so d_y^3 rho(x, 0) exists
  there and solves the third axis equation of 6.3.1 (a) in the sense of distributions. Near P, on a cone |y| <= kappa r
  with r = x* - x, the function K + lambda y/s (s = x - x*, lambda = g* d_y^2 W_1(P)/A) solves a transport equation with
  forcing O(|y| r^(alpha - 1)), and integration over a backward time theta log(|y|/r) with
  (1 - alpha)/(1 + alpha) < theta < 1/(A - 1) gives |G_3(x* - r)| <= C r^(alpha - 1), hence
  G_3/H_3 = O(r^(alpha - 1 + 2/A)) -> 0. The conditions on theta and the integrability of the forcing hold exactly when
  alpha > 1 - 2/A, which for A <= 2 is automatic; for A > 2 the same computation gives the third-order step of 6.3.1 (h)
  under its Hoelder hypothesis without (C1). At A = 2 (c_l = 3/2), w g' = (w' - A) g gives g'(x*) = w''(x*) g*/A, and
  6.3.1 (k) gives B_3 = Q(x*)/6 = w''(P)(g* - 2)/(24 g*^3), so every profile of P_inf with c_l = 3/2 satisfies
  w''(P)(g* - 2) = 0. On the pair of 6.3.1 (c) at A = 2 (w = -2 sin x, g = 2(1 - cos x), x* = pi, g* = 4) w''(pi) = 0
  and B_3 = 0. These are necessary conditions; they do not decide existence in this range (6.4, 6.5).
(n) Local exclusion near an explicit compatible trace at A = 4 (external referee; the reference value checked by the
  lead researcher and by the verifier; the Lipschitz estimate, every constant of its chain and the radius checked by the
  verifier, from the referee's analytic bounds for the explicit rational reference, which the verifier checked by hand;
  its own sampled suprema lie below them by factors 2 to 6). At A = 4 the compatible axis data
  w_0(x) = -4x(1 - x^2/16)/(1 + x^2/16), g_0(x) = x^2/(1 + x^2/16) (the family of 6.3.2 (a) at L = 4) have
  B_3(c_l, w_0) = (23/110592) B(7/4, 1/2) at c_l = (A + 1)/2 = 5/2, in the normalization g/x^2 -> 1 at 0, where
  B(a, b) = int_0^1 t^(a-1) (1 - t)^(b-1) dt is the Euler beta function, without the rescaling to natural units (checked
  by the lead researcher against the integral of 6.3.1 (k), to 18 digits; checked by the verifier at 40 digits by two
  routes, from the exact rational remainder R(x) = -(x - 4)(x^4 + 4x^3 - 32x^2 - 128x - 512)/2097152, which is negative
  on (0, 4), and from a closed form, both within 1.1e-22 relative), and B(7/4, 1/2) > 4/7 gives
  B_3(5/2, w_0) > 23/193536 > 1e-4. The referee proves an explicit bound
  |B_3(c_l, w) - B_3(5/2, w_0)| <= e^(3000000) ||w - w_0|| for compatible traces (c_l = (1 - w'(0))/2) with source at
  x* = 4 within distance 1e-6, where the norm is the sum of the differences of the Taylor coefficients of order 1, 3, 5,
  7 at 0, the suprema of x^(i - 8) |d_x^i (R_w - R_w0)| on (0, 1/4] (R_w the remainder after order 7, i = 0, 1, 2) and
  the C^(0,3/4) norms of the differences of w, w', w'' on [1/4, 4], a norm of the type of 6.3.1 (i). Hence B_3 > 1/20000
  when ||w - w_0|| < e^(-10^7), and with 6.3.1 (h) no profile of P_inf that satisfies the Hoelder or cone hypothesis at
  P has its axis trace (with source at 4) in that neighbourhood. The bounds for the reference that enter the constants
  are elementary bounds for explicit rational functions, and the floating-point evaluation of the chain showed relative
  margins of at least 1e-5 (a numerical consistency check, not by itself a rigorous roundoff bound); at the same
  reference, 6.3.1 (o) gives the radii 1e-8 (for |A - 4| <= 0.06 and |x*^(-2) - 1/16| <= 0.0003) and 1e-7 (at A = 4,
  x* = 4) in its weaker norm N, with exact rational certificates. This is a local statement around a trace that is not
  known to be the axis trace of any profile, at A = 4, far from the computed branch (A = 10.15); it is not NO_inf. The
  verifier evaluated the chain of constants both from the reference bounds stated by the referee and from its own
  computed norms of w_0 (the radii given by the formulas are then about e^(-2129580) and e^(-136288); the stated radius
  e^(-10^7) is smaller than both), and recomputed the representation of B_3 used in the proof at 21 digits on compatible
  traces outside the rational family. The norm uses theta = 3/4: it requires the axis trace to be of class C^(2,3/4) on
  [1/4, 4], which the Hoelder hypothesis on rho at P with 1/2 < alpha < 3/4 does not guarantee; profiles whose trace
  lacks it are not covered.
(o) Local exclusion with polynomial constants at the computed A (external referees; checked by the verifier with
  separately written code: both certificates and budgets rerun on copies, every exact constant reassembled in its own
  exact arithmetic from inputs derived by hand, the reference values and parameter derivatives by its own quadrature,
  the reference inventory by its own sampling, the distances by its own evaluator; the explicit estimates and the
  second-order remainder theorem that produce the constants checked by the verifier by hand, including the holomorphy in
  the parameters (a general prescription for the second parameter derivatives is not used: both references replace it by
  a closed form or an interval certificate), and audited by a second external referee, with the qualifications stated
  here; the further statements at the end checked as stated there). Two parts and further statements: an estimate with
  constants polynomial in the reference, with a radius 1e-6 around the trace of 6.3.2 (a), and a certified radius 4.5e-6
  around an analytic compatible fit to the computed trace, with the polynomial q of 6.3.2 (e) of degree 12. Both are
  conditional on 6.3.1 (h) and on membership
  of the trace in the domain of the norm N below; neither is NO_inf, and nothing places the trace of an exact profile in
  either ball.
  First part: the norm, the estimate and the reference of 6.3.2 (a) (the reference values of B_3 and of its first
  derivatives in A and e at both references below, three directional derivatives and the closed-form reconstruction also
  checked by the lead researcher with separately written code, and the exact rational certificate rerun by the lead
  researcher with the same output). Rescale u = x/x*, w~(u) = w(x* u)/x*, g~(u) = g(x* u)/x*^2. Then w~ g~' = (w~' - A)
  g~ with g~/u^2 -> 1 at 0 and Q = x*^(-5) (g~' - e w~'')/(2 g~^3) with e = x*^(-2), so B_3 in natural units is a
  functional B(A, e, w~) of A, of the single scalar e and of the normalized trace on [0, 1], affine in e (for the family
  of 6.3.2 (a), w~ = -A u (1 - u^2)/(1 + u^2) for every L and B = C_A (1 - S_A e)). For compatible directions v (odd and
  smooth near 0, v'(0) = 0, v(1) = v'(1) = 0) write v = c_3 u^3 + c_5 u^5 + c_7 u^7 + R_v near 0, with c_j the Taylor
  coefficients and R_v = O(u^9), and put ||v||_N = |c_3| + |c_5| + |c_7| + sup_(0<u<=r) u^(-5-sigma)
  |R_v''(u)| + sup_[r,1] |v''| + sup_(r<=u<1) |v''(u) - v''(1)|/(1 - u)^theta, on the affine set of compatible traces
  for which these quantities are finite (functions and derivatives match at r, and v is C^2 through 1), with
  0 < sigma <= 2, 0 < theta <= 1, and, for a complex buffer tau > 0 with A_0 - h - tau > 2, sigma > 2/(A_0 - h - tau)
  and theta + 2/(A_0 + h + tau) > 1, where h bounds |A - A_0|. (i) The referee gives the exact first variation of B in
  (A, e, v), with the variation of g written through an adjoint weight, and a second-order remainder bound whose
  constants are rational expressions in explicit norms, suprema and integrals of the reference (among them the infimum
  of -w_0/(u (1 - u)), bounds for g_0/u^2, |Q_0(1)| and the Taylor coefficients at 0) and in the inverses of the
  positive margins (sigma and theta against their thresholds, the buffer tau, A - 2, the positivity margins and the
  cutoffs), once scalar powers are replaced by rational majorants. The large exponential constants of 6.3.1 (n) came
  from absolute Gronwall-type bounds for the reconstruction of g from w; here log(g/g_0) is bounded relative to the
  reference through an origin algebra estimate and the quotients -w/(1 - u) and (A - w')/(1 - u), both removable at
  u = 1, and only exponentials of uniformly small perturbations are bounded by universal constants. The reference
  reconstruction itself (it contains exp(T) below) enters only through its explicit norms. (ii) Write w~(u) = -A u
  (1 - u^2)/(1 + u^2) + u^3 (1 - u^2)^2 q(u^2) as in 6.3.2 (e). At the reference q = 0 (the trace of 6.3.2 (a)) with
  A_0 = 10.150725, e_0 = 0.0135206, h = 0.06, h' = 0.0003, r = 1/2, sigma = 1,
  theta = 9/10 and tau = 1, exact rational arithmetic gives B(A_0, e_0, w_0) >= 0.321857 (the value is 0.3257951),
  ||DB||_(N*) <= 12240, a second-order constant at most 235346 on the ball of radius delta_0 >= 0.1046, and the radius
  eps = 1e-6. If R_v is taken after subtracting c_j phi_j instead of c_j u^j, with the compatible polynomials phi_j of
  (iv), the second referee's corrected constants 12519, 245246 and delta_0 >= 0.10269550 (exact rational arithmetic,
  rerun by the lead researcher with the same output) give a radius above 1.8749e-6, so eps = 1e-6 holds in that norm as
  well. With the input of 6.3.1 (h) (an exact profile that satisfies the Hoelder or cone hypothesis at P and is in P_inf
  has B_3 = 0; this includes its classical third axis equation), no such profile has |A - A_0| <= 0.06, first source
  x* = L with |L^(-2) - e_0| <= 0.0003 and normalized trace in the affine domain of N with ||w~ - (A/A_0)
  w_0||_N <= 1e-6. Membership in that domain (the weighted origin remainder and the anchored source exponent
  theta = 9/10) is a hypothesis: it does not follow from the Hoelder or cone hypothesis at P, whose exponent need only
  exceed 1 - 2/A = 0.803. At A = 4, e = 1/16 (the reference of 6.3.1 (n)) the same method with tau = 1/2 gives 1e-8 for
  the same widths and 1e-7 at fixed A and e, in both conventions for R_v, compared with e^(-10^7) in 6.3.1 (n) (in other
  coordinates and another norm). (iii) The norm displayed in 6.3.1 (i) is not necessary: N controls only R_v'' at the
  origin and
  compares v'' only with its value at the source. A plain C^2 tail norm is not sufficient: choose 0 < gamma <= 1 - beta
  away from the at most one zero of 1/(2A (gamma + 1) g*^2) - e/(2 g*^3), prescribe v''(1 - s) = s^gamma near the
  source, integrate from the source and cut off away from it; for small nonzero amplitudes these compatible C^2
  perturbations keep w~ < 0 but make the source integral defining B diverge, with that first-order coefficient. The
  origin weight of DB is lambda ~ e (1 - beta)(6 + beta)(7 + beta) u^(-8-beta)/(6A), so the method needs sigma > beta,
  and sigma = beta fails for the plain supremum. (iv) Lead checks: at the computed A, B = 0.325795091172477577,
  dB/de = -15.1525473710004066 and dB/dA at fixed w~/A equal to -0.0151217387326; at A = 4, e = 1/16,
  0.153095696660659004, -4.15355281375005299 and -0.0651471618470; DB(phi_3), DB(phi_5), DB(phi_7) = 0.82913517178,
  0.48431395934, 0.21490833993 for the compatible directions phi_j(u) = u^j + ((j - 11)/2) u^9 + ((9 - j)/2) u^11
  (phi_j(1) = phi_j'(1) = 0), by central differences of the exact functional of 6.3.2 (e), in agreement with the
  referee's formulas to 10 digits; the referee's closed form g_0(u) = u^2 H(u^2) exp(T(u^2))/(A_0 (1 + u^2)),
  H(t) = A_0 - t (1 - t^2) q(t), T(t) = (1/2) int_0^t (1 + s)^2 q(s)/H(s) ds, agrees at u = 1 with the numerically
  rebuilt g of 6.3.2 (e) to 20 digits on the K = 12 and K = 18 approximants. The verifier recomputed these values with
  its own code (closed form and two quadratures) and they agree in every printed digit. (v) Scope. The reference q = 0
  differs from the computed trace by about 0.22 in w~ (sampled), and its N-distance to the analytic approximants of
  6.3.2 (e) is 492 to 634 for K = 4 to 18 (530 to 568 for K = 10 to 18, lead researcher and verifier; K = 4, 6, 8
  verifier only; suprema sampled; 571 to the fitted reference below), far outside the ball. The referee also gives an
  exactly compatible reference of the type of 6.3.2 (e) with q of degree 12, fitted to the computed trace (sampled error
  in w~ at
  most 2.7e-7 on 0.02 <= u <= 0.985; w_0 < 0 on (0, 1) and H >= A_0 certified by exact Bernstein bounds), with
  B = 0.2840732 natural units (lead researcher's code; its g(1) agrees with the referee's to 18 digits and gives
  g* = 29.7492 against 29.7495 from the trial data); its exclusion constants are certified in the next part. Fits of
  equal quality (sampled errors in w/u at most 2.4e-6, K >= 10, and the referee's fit) have Taylor coefficients of order
  7 at 0
  between 6.34 (the referee's fit) and 6.86, and their mutual N-distances are 8.8 to 66.7 (lead researcher, suprema
  sampled, not certified full-interval norms; all 15 pairs among the approximants K = 10 to 18 and the fitted reference,
  and the six pairs with the trace of 6.3.2 (a), recomputed by the verifier in both conventions, in agreement; 6.0 to
  55.8 if R_v is taken after subtracting c_j phi_j instead of c_j u^j; the three pairs also computed by the referee of
  the next part agree), mostly from the weighted origin term sup u^(-6) |R_v''| on (0, 1/2]. Sampled fitting errors do
  not place the computed trace, or an exact profile near it, within 1e-6 of any reference in N (the next part shows that
  sampled agreement does not control N among compatible traces). The stored trace also starts at positive x, and smooth
  perturbations supported in the unobserved origin interval change the N-norm without changing any stored value. This is
  a local statement around traces that are not known to be axis traces of any profile; it is not NO_inf.
  Second part: certified ball around the fitted reference (it rests on the estimates of the first part; the verifier
  reran the interval certificate and the budgets, checked the inventory with its own series sums and sampling, assembled
  every constant in its own exact arithmetic and recomputed B, g_0(1) and the parameter derivatives with its own
  quadrature; a third external referee reran the certificate and the budgets (140 checks) and corrected the wording of
  (iii) and (iv), applied here; the lead researcher reran the certificate and the budgets, rederived a few inventory
  entries and the conversion constant 415/4 by hand, checked the parameter derivatives and B at the four corners of the
  parameter box by central differences of a separately written quadrature, all inside the stated enclosures, and
  recomputed the three Taylor separations of (iv) (0.50056, 0.53259, 0.03281)). Let w_0 be the fitted reference of the
  first part (of the form of 6.3.2 (e) with A = A_0 and q(t) = q_0 + q_1 t + ... + q_12 t^12, where
  q_0, ..., q_12 are the exact decimals -3.1086642790748664, 2.8463293854346565, -5.157019170237831, 9.6363849138295752,
  -10.568048035000519, -4.8988855905151825, 78.281466894874512, -247.83555958781369, 462.10389097961377,
  -550.96839996015603, 411.5296756206738, -175.45293252015944, 32.420024447785266; the least-squares fit that produced
  them is in the accompanying artifacts), A_0 = 10.150725,
  e_0 = 1/8.6000638^2, and N the norm of the first part with r = 1/2, sigma = 1, theta = 9/10. (i) Outward-rounded
  interval Taylor arithmetic gives 0.2830400682 < B(A_0, e_0, w_0) < 0.2851567624 (the lead researcher's quadrature
  gives 0.2840732), 0.40222790015 < g_0(1) < 0.40222790016, |dB/dA| < 0.007 and |dB/de| < 7.1 at the reference, and
  |d^2B/dA^2| < 0.007 and |d^2B/dA de| < 1.85 on the parameter box |A - A_0| <= 0.06, |e - e_0| <= 0.0003
  (A at fixed w~/A). Every reference quantity entering the estimates of the first part (origin remainders, suprema on
  the whole tail interval, endpoint data, parameter margins) is bounded by exact rational or interval arithmetic. (ii)
  An exact quadratic budget then gives |B(A, e, w~) - B(A_0, e_0, w_0)| < 0.14 < B(A_0, e_0, w_0)/2 whenever
  |A - A_0| <= 0.06, |e - e_0| <= 0.0003 and ||w~ - (A/A_0) w_0||_N <= 4.5e-6, and whenever A = A_0, e = e_0 and
  ||w~ - (A/A_0) w_0||_N <= 5e-6 (the budgets are 0.13850 and 0.13533). The certificate programs, their inputs and the
  explicit remainder-bound formulas are in the accompanying artifacts; the radius cannot be rederived from this text
  alone. If R_v is taken after subtracting c_j phi_j
  instead of c_j u^j, the norm N' so obtained satisfies ||v||_N <= (415/4) ||v||_(N'), and the radii become 4/415 of
  these. (iii) Consequently, taking the source theorem of 6.3.1 (h) as the only analytic input on the source, there is
  no exact profile in P_inf with all of the following properties: a first source P = (L, 0) of the axis trace
  w(x) = W_1(x, 0) (w < 0 on (0, L), w'(0) = -A, w(L) = 0, w'(L) = A); rho and W smooth near each point of the open axis
  segment 0 < x < L; rho C^(2,alpha) near P with alpha > 1 - 2/A, or the cone form of that hypothesis in 6.3.1 (h); the
  normalized trace w~(u) = w(L u)/L in the affine domain of N (this includes the anchored source exponent theta = 9/10,
  a hypothesis separate from the exponent at P); and |A - A_0| <= 0.06, |L^(-2) - e_0| <= 0.0003 and ||w~ - (A/A_0)
  w_0||_N <= 4.5e-6. At A = A_0 and L^(-2) = e_0 the same holds with 5e-6 in place of 4.5e-6. (iv) The present data do
  not establish that the normalized trace of an exact profile on the computed branch lies in either ball. After the
  K = 12 and K = 18 approximants of 6.3.2 (e) are multiplied by A_0/A_i (A_i = 10.150725214760579, the value of A of the
  stored trace), their Taylor coefficients of orders 3, 5 and 7 alone give exact rational lower bounds above 0.50, 0.53
  and 0.032 for the N-distances of the pairs K = 12 and K = 18, K = 12 and the fitted reference, and K = 18 and the
  fitted reference; so these three equally good fits lie outside each other's balls of both radii. Agreement with
  samples does not control N, among compatible traces: for a nonzero nonnegative chi in C_c^infinity((1, 2)) and
  0 < d < 0.01, the odd extension of v_d(u) = -d^3 chi(u/d) is a compatible perturbation that vanishes on [0.02, 1],
  while ||v_d||_N = d^(-5) sup_(1<s<2) s^(-6) |chi''(s)| tends to infinity as d tends to 0; and for any finite set of
  interior sample points u_i and C > 0, the odd polynomial v_C(u) = -C u^3 (1 - u^2)^2 prod_i (u^2 - u_i^2)^2 is
  compatible, nonpositive on [0, 1] and zero at every sample point, with |c_3| = C prod_i u_i^4 unbounded in C. These
  are not claimed to arise from exact profiles. This is a theorem about a small ball around an explicit trace that is
  not known to be the axis trace of any profile; it is not NO_inf.
  Further statements (external referees; the analytic part of the two-constants estimate audited by the third external
  referee; checked by the verifier: the dual-norm lower estimate and the bump value recomputed with its own code, the
  two-constants estimate audited by hand and its table recomputed, and the example v recomputed). Directional tests give
  a numerical lower estimate of about 8.3e-4 for the dual norm of DB at the reference of 6.3.2 (a), against the proved
  upper bound 12240; these do not determine the dual norm accurately. A sampled evaluation of the weighted origin term
  for a broad bump at u = 1/8.6 gives about 4.28e14 (numerical, not a certified lower bound), consistent with the
  response of up to 1e9 natural units per unit relative change in 6.3.2 (c). For the fitted reference of the second
  part, under an additional hypothesis (v holomorphic in the Bernstein ellipse E_rho with foci 0.02 and 0.985,
  continuous on its closure and bounded there by M, and |v| <= delta <= M on [0.02, 0.985]) a two-constants and Cauchy
  estimate gives ||v||_N <= C(d) M^(1 - lambda(d)) delta^lambda(d) for each admissible tube radius d, with explicit C(d)
  and lambda(d). For rho = 4, M = 10 and d = 0.05, delta <= 1.4492e-31 is sufficient for this estimate to give
  ||v||_N <= 4.5e-6; this is a sufficient condition from one conservative estimate, not a necessary accuracy (v = -1e-9
  u^3 (1 - u^2)^2 satisfies the hypothesis with M = 10 and lies in the ball although |v(1/2)| > 7e-11), and at d = 0.4,
  delta = 1e-7 the estimate gives only ||v||_N < 194408. Such a holomorphy bound and a uniform error bound are not known
  for exact traces, and discrete sample errors alone do not give the uniform bound.

(p) No nonzero exact profile with finitely many physical angular modes (verifier; audited by an external referee;
checked by the lead researcher). Let rho satisfy (A1) with m = 2, (A3) and (A4) for a real constant c_l, and suppose
that there is one fixed odd N >= 1 such that rho(r cos theta, r sin theta) = sum over n = 1, 3, ..., N of h_n(r) sin(n
theta) for every r > 0. Then rho = 0. Neither the normalization (A2) nor c_l > 1 is used; since (A2) excludes rho = 0,
no profile of P_2, and hence none of P_inf, has this form. Proof outline: if rho != 0, let N be the largest index with
h = h_N not identically 0. Angular projection gives h in C^2 for r > 0, h = O(r) and h' bounded near 0 (rho(0) = 0 by
oddness in y), and h = O(r^gamma), h' = O(r^(gamma - 1)) at infinity. Since d_x(h(r) sin(N theta)) = (h' + N h/r)
sin((N - 1) theta)/2 + (h' - N h/r) sin((N + 1) theta)/2, the highest mode of psi in (V1) is T(r) sin((N + 1) theta),
generated by h alone, and an integration by parts in (V1) gives T = -(1/2) r^(-N-1) int_0^r h(t) t^(N+1) dt, hence
T' = -(N + 1) T/r - h/2 (the integrals at 0 converge by local regularity and the integral at infinity because gamma < N;
the boundary terms h(t) t^(N+2) at 0 and h(t) t^(-N) at infinity vanish, and the two terms at t = r cancel). The
dilation term and rho contain no harmonic above N, and among the products of a mode of psi and a mode of rho only the
top pair (indices N + 1 and N) produces sin((2N + 1) theta); so, with U = (-psi_y, psi_x), the coefficient of
sin((2N + 1) theta) in (c_l X + U).grad rho - rho is (N h T' - (N + 1) T h')/(2r), and it vanishes. On a connected
component of {r > 0 : h(r) != 0} let v be the real N-th root of h; then (T/v^(N+1))' = 0, so T = K v^(N+1) with K != 0
(K = 0 would give h = 0 there by the identity for T'), and that identity becomes v' + v/r = -1/(2(N + 1) K), so v = a
r + b/r with a = -1/(4(N + 1) K) != 0. At a finite positive endpoint of the component h = 0 by continuity; there cannot
be two such endpoints, since a r^2 + b has at most one positive zero; if the component starts at 0, then b = 0 because h
is bounded there, and v has no positive zero. So every component reaches infinity, where |h| = |a r + b/r|^N grows like
r^N, against (A3) since gamma < 1 <= N. Hence {h != 0} is empty, contradicting the choice of N. The argument includes
N = 1, uses no analyticity and allows coefficients that vanish on intervals. Scope: the finite cutoff is imposed on the
density itself, in the physical polar angle, and is uniform over all radii. The density of the candidate of 4.2 is not
of this form: its exponent H contains the term in |cos(theta)|^(p_3 - 2) with p_3 - 2 not an integer, whose radial
coefficient vanishes at at most five radii (the polynomial T of 4.2 has degree 5 and is not identically zero), so at the
other radii the density is
not real analytic in theta at theta = pi/2, while a finite trigonometric sum is. The theorem gives no quantitative lower
bound for the residuals of approximations, and does not exclude convergence, as the angular cutoff increases, to an
exact profile with infinitely many angular modes; the argument does not extend to densities whose angular expansion
terminates only for large r (interior modes then generate higher stream-function modes outside). It establishes neither
YES_inf nor NO_inf.

(q) A nonzero homogeneous trace at infinity (verifier; checked by the lead researcher; audited by an external referee).
Let rho be a nonzero profile in A_m, m >= 2, so that c_l > 1 and 0 < gamma < 1 by R2, and put k = 1/c_l. Then
k <= gamma, and there is a function F on the unit circle, even in x and odd in y, Hoelder continuous with exponent
beta_0 = (1 - gamma)/(1 - k) (Lipschitz if gamma = k) and not identically zero, such that rho(r theta) = r^k
F(theta) + O(r^(k + gamma - 1)) uniformly in the unit vector theta as r -> infinity. Moreover |U(X)| <= C (1 + |X|)^k,
improving the growth exponent of R1 when gamma > k and agreeing with it when gamma = k, and r^(-k) U(r theta) ->
U_inf(theta) uniformly, where U_inf is the restriction to the unit circle of the velocity U[rho_inf] given by the
principal-value law of (V2) for the homogeneous density rho_inf(X) = |X|^k F(X/|X|) (well defined away from 0 since F is
Hoelder; homogeneous of degree k). Proof outline. (1) The characteristic argument of R2 gives |rho| <= C (1 + |X|)^k. In
the principal value near X, with |X| = r, the gradient bound of (A3) on |X - Y| < r^(1 + k - gamma)/8 and the density
bound on the rest of |X - Y| < r/2 give |U| <= C r^k (1 + log r); the remaining regions are bounded by C r^k after
pairing Y with -Y (rho is odd under X -> -X). (2) The transport equation and c_l k = 1 give the exact identity d_r
[r^(-k) rho(r theta)] = -k r^(-k-1) U.grad rho, whose right side is O(r^(gamma - 2) log r) uniformly in theta; so r^(-k)
rho(r theta) converges uniformly to a limit F, with error O(r^(gamma - 1) log r), and comparing two angles at distance d
at the radius r = d^(-1/(1-k)) (where the angular Lipschitz constant is O(r^(gamma - k))) gives F a positive Hoelder
exponent. (3) With E = rho - |X|^k F, the local principal value of E near X, split at the radius r^(1 - M) with a fixed
M > gamma - k, is o(r^k), and the other regions are O(r^k); so U = O(r^k), and inserting this in (2) gives the stated
remainder and the exponent beta_0. (4) Scaling Y = r Z, the bound |E(Y)| <= C |Y|^(k + gamma - 1) for large |Y| and the
pairing of the far tail give r^(-k) U[E](r theta) -> 0 uniformly, after choosing the inner and outer cut radii in the
scaled variable and then letting r -> infinity. (5) Along a characteristic with rho(X0) != 0, e^(-c_l t) X(t) -> Q != 0
(R2), and since c_l k = 1, |X(t)|^(-k) rho(X(t)) = |X(t)|^(-k) e^t rho(X0) -> |Q|^(-k) rho(X0) != 0; by the uniform
convergence this limit is F(Q/|Q|). Scope: F is a necessary far-field datum of every profile, and no nonzero profile has
rho = o(r^k) uniformly at infinity. Nothing here shows that F can be prescribed, that different profiles have different
traces, or that F determines the profile, so this gives a precise meaning to the far-field data of question Q1 without
deciding it. The homogeneous density rho_inf has the canonical homogeneous velocity U[rho_inf] but is not shown to be an
exact profile: it satisfies c_l r d_r rho_inf = rho_inf along every ray, and c_l X.grad rho_inf = rho_inf in the sense
of distributions (F is only known to be Hoelder continuous, so no classical angular gradient is asserted), while its
self-advection term, interpreted as div(rho_inf U[rho_inf]), is homogeneous of degree 2k - 1, and the theorem imposes no
condition on it. The compact extension of (c) does not contradict this, since it fails the transport equation outside
the prescribed set. Next far-field balance (verifier; checked by the lead researcher; audited by an external referee).
Suppose in addition that rho(r theta) = r^k F(theta) + r^(2k-1) G(theta) + eta(r, theta), with F and G smooth and
periodic and eta = o(r^(2k-1)), d_r eta = o(r^(2k-2)) and d_theta eta = o(r^(2k-1)), all uniformly in theta. Put S = k
cos(theta) F - sin(theta) F' and let P be the periodic solution, odd in x and in y, of -P'' - (k+1)^2 P = S (its sine
coefficients are P_m = S_m/(m^2 - (k+1)^2), m even; no denominator vanishes since 1 < k + 1 < 2). Then r^(k+1) P is the
canonical stream function of r^k F, with velocity r^k [-P' e_r + (k+1) P e_theta], and the residual R = (c_l X + U).grad
rho - rho satisfies: r^(1-2k) R(r theta) tends uniformly to D = (1 - c_l) G - k F P' + (k+1) P F', so a profile with
such an expansion has G = [-k F P' + (k+1) P F']/(c_l - 1). This is a necessary identity under an expansion hypothesis
that is not proved for every profile; it does not make F or G prescribable, and it does not require the homogeneous
self-advection term -k F P' + (k+1) P F' to vanish. At each fixed angle where N_infinity = lim N_f/r^k = |F| + c_l
(|cos(theta) [k cos(theta) F - sin(theta) F']| + |sin(theta) [k sin(theta) F + cos(theta) F']|) is positive, it also
gives |R|/N_f = r^(k-1) |D|/N_infinity + o(r^(k-1)), uniformly on closed sets of angles where N_infinity is bounded
below by a positive constant. So at such angles the normalized residual of every field with such an expansion tends to 0
at infinity even when D != 0, small normalized residuals at very large radii do not by themselves test the balance, and
the scaled residual r^(1-2k) R does. Where N_infinity = 0 no such statement holds: for an explicit smooth field of this
form with its canonical velocity and c_l = 1/k (not a profile), with F = cos^2(theta) sin(theta) cos^2(2 theta) and
G = cos^2(theta) sin(theta), the normalized residual tends to (c_l - 1)/(c_l + 1) at theta = pi/4. Each fixed saved
nodal representation of the Q1 item of 6.4 has such an expansion, with F and G given explicitly by its coefficients, and
the verifier's floating-point computations give nonzero D for the saved states tested; for the 120 x 48 state and its
re-solution with the residual row that represents infinity moved to radius 1e8 (Q1 item (iv)), at radius 1e10 and the
angles 0.3, 1 and 1.55, the separately evaluated scaled residual differs from the computed D by less than 0.05 percent
of |D|, while |R|/N_f is between 2.1e-11 and 1.2e-9 there (six sampled comparisons, with D from Fourier inversion and
the residual from a real-space quadrature of the velocity; not interval certificates or uniform bounds in the angle).
Neither statement decides YES_inf or NO_inf, and neither says anything about B_3.

(r) Coupled solutions on a left cone at the source, and the endpoints of the source criteria on cones (verifier;
reviewed by the lead researcher, who checked the recurrences with separately written exact code; audited by two external
referees). Put P at the origin, s = x - x* = -r < 0, A = 2 c_l - 1 > 1, g > 0, and write f = g y + v and W = (A s,
y) + V for the density and the dilated velocity, so that the local system is W.grad f = f, div W = A + 1, curl W = -f_s,
with f and V_2 odd and V_1 even in y. (i) Construction. Let m >= 3 be odd, q = (m - 1)/A, p = m - q > 1,
b = g/(2(A - 1)), C a nonzero real number (the source amplitude) and 0 < kappa < (1 + b)^(-1/2). There are R > 0 and
real-analytic fields v, V on the open cone {0 < r < R, |y| < kappa r} that solve the three equations exactly, with V = 0
on the axis, d_y^j v(-r, 0) = 0 for odd j < m, G_m(-r) = C r^(-q) and G_(m+2)(-r) = -b q (q + 1) C
r^(-q-2)/((m + 1)(m + 2)), where G_j = d_y^j v(-r, 0)/j!. The fields are convergent series sum_n r^(p_n) (phi_n,
alpha_n, beta_n)(y/r), p_n = 1 + (n + 1)(p - 1); the linear germ is phi_0(z) = C sum_l (-1)^l (b)_l (q)_(2l) m!
z^(m+2l)/(l! (m + 2l)!) (rising factorials); at every nonlinear level n >= 1 the resonant angular index m + n(m - 1)
lies 2n below the first possible index m + n(m + 1) of the forcing, so no resonance is forced, and a Catalan majorant
with explicit constants gives convergence for small R. On every smaller closed cone the fields are of class C^(k,alpha)
up to the vertex if p = k + alpha with 0 < alpha < 1 (of class C^(p-1,1) if p is an integer), and the density is of no
better Hoelder class there. The velocity is a chosen local solution of the div-curl system (the recurrence sets the axis
velocity to zero; adding a harmonic field does not in general preserve transport); it is not shown to be the canonical
velocity of any density. The construction gives nothing on a neighbourhood of P, at the points (0, y) with y != 0, at
the centre, for the coefficient relation that fixes c_l or at infinity, and the source amplitude C is not a centre
coefficient B_j. For m = 3, A > 2 and 3 < g/(A - 1) < 4, the leading term is that of the frozen Fourier solution of (g),
with C = 1/(12 sin(2 pi/A)). The same construction with finitely many distinct odd seeds 3 <= m_1 < ... < m_d and
arbitrary real amplitudes C_1, ..., C_d (multi-indexed series in which, for every product of two or more seeds, the
resonant index lies strictly below the first possible index of the forcing) gives, on a common sufficiently small cone
for each bounded set of amplitudes, solutions of the same kind that depend real-analytically on the amplitudes; distinct
amplitude vectors give distinct solutions, and, if some amplitude is nonzero, the regularity is that of the smallest
seed with nonzero amplitude (all-zero amplitudes give v = V = 0). For the seeds 3, 5, 7, with lambda = 2/A,
G_3 = C_3 r^(-2/A), G_5 = -b lambda (lambda + 1) C_3 r^(-2/A-2)/20 + C_5 r^(-4/A) and G_7 = b (b + 1)
lambda (lambda + 1)(lambda + 2)(lambda + 3) C_3 r^(-2/A-4)/1680 - [(2 lambda)(2 lambda + 1) b C_5/42 + lambda
(3 - 2 lambda) C_3^2/(40 (A - 1))] r^(-4/A-2) + C_7 r^(-6/A), so C_3, C_5 and C_7 are independent source data (verifier;
rechecked by the lead researcher with separately written symbolic code; audited by an external referee). Thus transport
and the div-curl coupling restricted to a cone leave these finitely many local source parameters free; this is not a
family of profiles, and it says nothing about the centre coefficients. (ii) Criteria on cones. The proofs of the
higher-order trace criterion of (h) (n >= 2 even, C^(n,alpha) regularity with alpha > 1 - n/A gives r^(n/A)
d_y^(n+1) rho(-r, 0) -> 0), of the summable fourth-derivative criterion and of the density-bound criterion of (h) use
only transport and constant divergence on a closed left cone (and, for the last, the curl identity on interior balls),
once the regularity, the source jet and smoothness on the punctured cone are assumed on that cone; the
full-neighbourhood hypotheses of (h) serve only to supply these. (iii) Sharpness on cones. For even n >= 2 and A > n the
construction with m = n + 1 is of class C^(n,1-n/A) on smaller closed cones and has r^(n/A)
d_y^(n+1) f(-r, 0) = (n + 1)! C != 0, so on cones the strict inequality alpha > 1 - n/A cannot be relaxed to equality
(the bound |d_y^(n+1) f(-r, 0)| <= C r^(alpha-1) still holds there). For n = 2 this is an exact coupled counterpart, on
a cone, of the function of (b) (which is not a solution) and of the frozen solution of (g). For m = 5 and 4/3 < A < 2
the construction is of class C^(2,3-4/A) on smaller closed cones, the suprema of |D^4 v| and |D^5 v| over cone annuli at
depth about r are comparable to r^(1-4/A) and r^(-4/A) (no pointwise lower bound is claimed), and r^(4/A) G_5 = C != 0,
so the density-bound criterion fails if both of its strict inequalities (an exponent below 4/A - 1 in the bound on |D^4
f|, and alpha > 3 - 4/A) are replaced by equalities together; whether either can be relaxed while the other stays strict
is open. Scope: these solutions are constructed only on a cone, so the full-neighbourhood hypotheses under which (h) is
stated for profiles are not supplied (whether they extend to a neighbourhood of P is open); they show sharpness only of
the cone formulations, do not produce a profile, do not show that an exact profile can have l_3 != 0 or l_5 != 0, and
decide neither YES_inf nor NO_inf.

6.3.2 Numerical statements
Throughout, B_j in natural units means B_j x*^(p_j - j + 1), in the normalization g/x^2 -> 1 at 0 (for j = 3 this is
the unit x*^(2 - p_3) of section 4).


(a) The B_3 estimator on exact data. Two independently written estimators were run.
- On the pair of 6.3.1 (c) (exact value 0) both return the floating-point floor of each fit window: 1e-10 to 1e-4
  natural units.
- On the compatible axis data w = -A x (1 - u^2)/(1 + u^2), g = x^2/(1 + u^2), u = x/L (from R12, with x* = L), at
  A = 10.150725, both return B_3 = C_A (1 - S_A/L^2) natural units, to 1e-6 in their stable fit windows
  (from x = 0.02 up), for L from 4 to 10. Here C_A = 0.5306666232 and S_A = 6A (4A - 3)/(8A - 1) = 28.5537976. They also
  return the zero at L = sqrt(S_A) = 5.343575. The closed form holds on these data to 40 digits: with C_A and S_A fitted
  from the series values at L = 4 and 10, the series values at four further L between 4 and 10 agree with it to 8e-40,
  and S_A agrees with 6A (4A - 3)/(8A - 1) to all digits printed (a numerical check of the closed form, not a proof).
- On the same data, B_3 and B_5 by two power series that use the same lower-order traces (one centre-selected, analytic
  at 0, and one source-selected, analytic at P; the source-selected solution minus the centre-selected one is B_j H_j),
  with no finite part, fit or quadrature, cross-checked by the finite-part form: B_3 = 0.325791726307172
  natural units at L = 8.6, and at the zero L* = 5.3435753609604 of B_3, B_5 = -7.6894e-5 natural units. For B_5 the
  series value and the finite-part form agree to about 1e-21 (the two series do not give independent values: their
  difference defines it); for B_3 the finite-part form agrees with the series to 20 digits and the
  convergent form of 6.3.1 (i) to 4e-30. [Clarified 2026-10-20: an earlier version attached the agreement 1e-21 to
  both coefficients.] So at the zero L* of B_3 on this one-parameter family B_5 is nonzero: the closed form in 6.5 (the
  item Toward NO_inf for 1 < A <= 2) proves B_5 < 0 exactly for every A > 1 with A != 2, including A = 10.150725 used
  here; the value -7.6894e-5 is numerical (the two series and the finite-part form).
(b) B_3 on the published candidate: 6.2.
(c) Conditioning of the obstruction functional on exact data. On the compatible axis data of (a) with L = x* = 8.6,
perturb w to w (1 + eps b chi), with b(x) = exp(-(ln(x/x0)/sig)^2) and the C^infinity cutoff chi = 1 for x <= 0.8 x*,
chi = 0 for x >= 0.95 x*, and chi = e^(-1/t)/(e^(-1/t) + e^(-1/(1-t))) with t = (0.95 x* - x)/(0.15 x*) in between,
and rebuild g from w (so the perturbed data stay compatible and the source conditions hold). The first-order response
dB_3/deps of the exact functional (natural units; numerical evaluations of its derivative with no fit estimator,
computed by two separately written codes and agreeing to the digits shown) is:

| sig | x0 = 0.5 | x0 = 1 | x0 = 1.5 | x0 = 2 | x0 = 3 |
|---|---|---|---|---|---|
| 0.3 | -4.63e6 | -6.37e4 | | -8.96e2 | -75.7 |
| 0.6 | | | -1.37e5 | | -1.90e3 |
| 1.0 | | -1.31e9 | | -1.78e7 | -1.44e6 |

For a direction analytic near 0, which changes the Taylor coefficients of w at 0, b = x^2 exp(-x^2/8) with the same
cutoff chi, the response of the exact functional is 948.8416 natural units (the verifier's fit-free evaluation, exact
series at 0 and quadrature at 34 digits: 948.84164773481; the lead researcher's double-precision evaluation 948.844
agrees to 2.5e-6 relative); the lead researcher's median estimators of (a) reproduce it to 2e-5 relative, and the
verifier's estimator to about 3.1e-6 relative in its best window and 1.6e-4 across its windows. [Corrected 2026-10-20:
an earlier version gave 948.84 from "two separately written codes: 948.844 and 948.8446" and the verifier's estimator
"to 1e-6 relative in its best window"; 948.8446 is the verifier's estimator value, not an evaluation of the exact
functional, and the 1e-6 was its agreement with 948.844.] So, to first order, a relative change of w of 1e-8 in such a
bump changes B_3 by about -0.046 natural units at x0 = 0.5 and -6.4e-4 at x0 = 1 (sig = 0.3), and by about -13 at x0 = 1
(sig = 1).
[Corrected 2026-10-20: an earlier version said "by 0.05 to 1 natural units".] The functional itself, not only its
numerical estimators, is ill conditioned in the origin layer. A value of B_3 on a numerical candidate is therefore a
statement about that candidate as a trial function. Its relation to a nearby exact profile needs control of w near 0 in
a norm that is strong enough there (6.3.1 (i)).
(d) B_3 on the stored fits of the first investigation (question Q2). On the ten stored trial traces of the first
investigation (nine fixed-c_l fits, among them X3, and the free control F3; c_l from 5.5524653 to 5.6004662), the
verifier's estimator (the form using w alone, integrated by parts, validated on exact data sampled on the same grid to
5e-8) gives, over 7 treatments of the data next to x*, 24 fit windows and degrees and 4 end pieces (6720 values), B_3 in
[0.265, 0.472], with 1 to 99 percent quantiles [0.285, 0.332] and median 0.302 natural units; the medians per trace and
treatment lie in [0.2866, 0.3281]. No variant on any trace comes near 0. The slope of the medians against c_l depends on
the treatment (-0.07 to +0.84 per unit c_l, a change of -0.004 to +0.04 over the range of c_l), so the dependence of B_3
on c_l along these fits is not resolved. The lead researcher's medians on the same traces (one data treatment, 0.2969 to
0.3003) lie inside the verifier's ranges on eight traces and within 0.004 of them on the other two. These are values on
fitted trial traces, not on solutions; by (c), they do not determine B_3 on nearby exact profiles.
(e) The exact functional on compatible analytic approximants of the computed trace (lead researcher; checked by the
verifier with separately written code: B on all K to 2e-17, w_0 < 0 exactly, the fit errors, the Taylor coefficients at
0 in exact arithmetic, and (H_-) and mu_0 on all approximants). The stored axis trace of X3 (A approximately 10.150725,
source x* approximately 8.6000638, located numerically as the zero of the stored trace) was normalized to w~(u) = w(x*
u)/x* on [0, 1] and fitted on
0.003 < u < 1, by weighted least squares in w, w' and w'', with the exactly compatible analytic functions w_0(u) = -A u
(1 - u^2)/(1 + u^2) + u^3 (1 - u^2)^2 q(u^2), q a polynomial of degree K (so w_0 is odd, w_0'(0) = -A, w_0(1) = 0 and
w_0'(1) = A; w_0 < 0 on (0, 1) for every K below). On each w_0, the exact functional B_3 in natural units, as a function
of (A, e, w_0), was evaluated numerically with e = x*^(-2) (after the rescaling u = x/x*, Q = x*^(-5)
(g~' - e w~'')/(2 g~^3), so e is the only remaining scalar): g rebuilt from w_0 with g/u^2 -> 1, the convergent form of
6.3.1 (i), the finite part at 0 and the integrable singularity at u = 1 from Taylor series of order 80 inside the radii
of convergence set by the complex zeros of w_0, and quadrature in between, at 30-digit working precision, with reported
series-tail estimates below 1e-27 (no validated total error bound is stated here). For
q = 0 the code reproduces the closed form of 6.3.2 (a). For K = 4, 6, 8, 10, 12, 14, 16, 18 the values are 0.3434,
0.3396, 0.2936, 0.2717, 0.2675, 0.2756, 0.2884, 0.2997 natural units, all positive; the maximal sampled fit errors on
0.01 <= u < 1 decrease from 1.2e-4 (in w/u), 2.1e-3 (in w') and 0.30 (in w'') at K = 4 to 8.5e-8, about 2e-6 and 3.1e-4
at K = 18. In the variable u the Taylor coefficient of w_0 at 0 of order 1 is -A = -10.1507252 by construction, those of
order 3 round to 17.19 for every K and those of order 5 lie between -11.29 and -11.14, while those of order 7 and 9 do
not agree (5.41 to 7.34 and -5.59 to 6.78): the sampled trace data and these fitting errors do not determine the origin
jets that enter B_3, and the spread of B_3 over K (0.27 to 0.30 for K >= 10, where the fit errors in w/u are at
most 2.4e-6) is consistent with the large origin-layer response of 6.3.2 (c). On each of these approximants, and on the
trace of 6.3.2 (a), the remainder R = Q - P(m) - Q(x*) of 6.3.1 (k) is negative at every sample (400 points on the
quadrature interval, the points u = 1 - 10^(-k), and the Taylor series near 0; R tends to -Q(x*) < 0 at 0 and vanishes
linearly at u = 1), so every tested sample has the sign required by (H_-) (numerical evidence consistent with (H_-), not
a certification of its pointwise inequality), consistent with B_3 > 0 there. With b_0 and b_1 the
contributions of the parts g'/(2 g^3) and -e w''/(2 g^3) of Q to B (so B = b_0 + b_1 and b_0 is the value of B at e = 0;
the convention of the 6.4 item on the reading and size of the sign criterion of 6.3.1 (k)),
mu_0 = -b_1/b_0 = 1 - B/b_0 = 0.465, 0.236, 0.231, 0.293, 0.331, 0.334, 0.316, 0.295 for K = 4 to 18 (0.386 for q = 0,
where the exact value is S_A e = 0.3861); the values for K = 6 to 18 lie in the range 0.22 to 0.34 found on the stored
traces under the analytic origin model, those for K = 4 and q = 0 do not. These are values of the exact functional on
explicit trial functions close to the computed trace, not on solutions; they agree with the trial-data estimates of
6.3.2 and are candidate references for the local version in 6.5 (6.3.1 (o)).

### 6.4 What remains
Status at the report cutoff: neither endpoint has been reached. This subsection collects open questions, additional
verified diagnostics and results that were not fully verified by the report cutoff; each item states its verification
status. [Updated 2026-10-20: the nonlinear endpoint theorem, the remark on conormal modes, the obstruction functional at
nonsmooth axis data, the family of frozen solutions, the frozen theorem and the statements on higher odd jets, listed
here earlier as under check, are now verified and are in 6.3.1 (g) to (j); the sign criterion for B_3 and the first
variation, listed here earlier as under check, are in 6.3.1 (k), (l); the range 1 < A <= 2 and the local exclusion at
A = 4 are in 6.3.1 (m), (n); the local exclusion with polynomial constants at the computed A and the certified ball
around the fitted reference, with the further statements on that exclusion, are in 6.3.1 (o), and the exact functional
on compatible analytic approximants of the computed trace is in 6.3.2 (e).]
- (C2') of 6.3.1 (a) at the source P. For j = 3 the open question is whether G_3/H_3 -> 0, or even has a finite limit
  l_3, for every profile of P_inf with A > 2 (for 1 < A <= 2, l_3 = 0 by 6.3.1 (m)). The zero limit holds if
  (x* - x)^(2/A) d_y^3 rho(x, 0) -> 0 as x -> x*, in particular if d_y^3 rho(x, 0) stays bounded (for instance if rho is
  C^3 near P), under the rescaled compactness of 6.3.1 (f), and, by 6.3.1 (h), if rho is C^(2,alpha) near P with
  alpha > 1 - 2/A or satisfies the cone form of that hypothesis. For the frozen examples of 6.3.1 (g), within their
  stated parameter ranges and in particular at the computed parameters, the zero limit is not implied by C^(2,alpha)
  regularity with alpha <= 1 - 2/A (0.803 on the computed branch), and one-sided smoothness does not give a finite l_3
  (6.3.1 (g)); for exact profiles these implications are open. For odd j >= 5 the analogue of 6.3.1 (h) holds under
  C^(j-1,alpha) regularity at P with 0 < alpha < 1 and alpha > 1 - (j-1)/A (6.3.1 (h), Higher odd orders), and for j = 5
  also under the summable fourth-derivative hypothesis of 6.3.1 (h) or, for 1 < A < 2 and with its exponent condition,
  under its density bounds; the C^(2,alpha) regularity of the class does not supply these hypotheses, no endpoint
  theorem at these orders under that regularity alone is established in this report, and in the frozen model at the
  computed parameters C^(2,alpha) regularity does not suffice (6.3.1 (j)).
- l_3 and the condition at 0. For an exact profile that is C^infinity near 0 and has a finite limit l_3 at P
  (6.3.1 (g), Sign), the condition at 0 is B_3(c_l, w) = -l_3 (the sign is corrected from an earlier interim draft of
  this section). For fixed W and g*, R6 determines rho, and hence l_3 whenever that limit exists; this does not decide
  whether l_3 can parametrize a family of coupled profiles in which W varies. Its existence follows from C^(2,theta)
  regularity of the axis trace w with theta > 1 - 2/A (6.3.1 (i)). Without one of the sufficient endpoint hypotheses
  (bounded third trace, the rescaled compactness of 6.3.1 (f), the Hoelder or cone hypothesis of 6.3.1 (h)), the
  vanishing of l_3 for a general profile of P_inf is open. Nonvanishing of B_3 alone does not exclude a profile that is
  C^infinity near 0: what is needed is l_3 + B_3 != 0, and l_3 = 0 (for instance under one of those hypotheses) is one
  sufficient way to reduce this to B_3 != 0.
- Conditioning (external referee; the origin expansions and the leading-order law checked by the lead researcher and by
  the verifier, the limits along the origin bump family and its source analogue checked by the verifier on the trace of
  6.3.2 (a)). For A != 2 the finite part at 0 uses the Taylor coefficients of w up to x^7, and in the origin layer, to
  leading order, B_3 is the pairing of the perturbation of w with x^(-8-beta). The referee states that B_3 is continuous
  in weighted norms of origin order above 7 + beta, as in the norm of 6.3.1 (i) (a sufficient condition), and gives an
  explicit family of compatible axis data, bumps scaled at the critical origin order 7 + beta, along which B_3 is
  discontinuous in C^m for every integer m < 7 + beta. Continuity in the full norm of 6.3.1 (i) was checked by the
  verifier by hand (6.3.1 (i)); the limit along this family was checked by the verifier on the trace of 6.3.2 (a) at the
  computed A and x* = 8.6: for an odd bump h_eps(x) = t eps^(7 + beta) phi(x/eps), phi >= 0 smooth with support in (1,
  2), which tends to 0 in C^m for every integer m < 7 + beta, the exact differences B_3[w_0 + h_eps] - B_3[w_0] converge
  to t kappa_A int_1^2 phi(u) u^(-8-beta) du, kappa_A = (1 - beta)(6 + beta)(7 + beta)/(6A) (ratio to the limit
  1.0000141 at eps = 0.0125, with the predicted correction of relative order eps^2), and at the source the bump t
  eps^(3 - beta) phi((x* - x)/eps), which tends to 0 in C^(2,theta) for theta < 1 - beta, gives a nonzero limit with
  relative error of order eps (1.0053 at eps = 0.00625). This concerns compatible axis data, not profiles. The family
  does not tend to w_0 in the critical case sigma = beta of the norm of 6.3.1 (i): for i = 0, 1, 2, sup_x
  x^(i - 7 - beta) |h_eps^(i)(x)| = |t| sup_(1<u<2) u^(i - 7 - beta) |phi^(i)(u)| does not depend on eps, so it
  establishes no discontinuity in that norm. [Corrected 2026-10-20: an earlier version called this family a
  discontinuity at the critical origin order without naming the topology; it is a discontinuity in C^m for the integers
  m < 7 + beta.] [Corrected 2026-10-20: an earlier version said that the verifier had checked none of these continuity
  statements.] The leading-order law reproduces the exact responses of 6.3.2 (c) to 0.3 percent at x0 = 0.5 and to 0.02
  percent at x0 = 0.125; the computed ratios of exact response to law are 1.000187, 1.000745, 1.002969, 1.011776 at
  x0 = 0.125, 0.25, 0.5, 1 (sig = 0.3), consistent with an approximately quadratic correction 1 + 0.012 x0^2. For A > 2
  the verifier proves that B_3 is also discontinuous in the critical case sigma = beta of the norm of 6.3.1 (i), with a
  family different from the origin bump family h_eps above (verifier; checked by the lead researcher by hand; audited by
  an external referee). Let w_0 be smooth on [0, x*], odd and analytic near 0, with w_0(0) = w_0(x*) = 0, w_0'(0) = -A,
  w_0'(x*) = A and w_0 < 0 on (0, x*); rebuild g_0 by w_0 g_0' = (w_0' - A) g_0, g_0/x^2 -> 1 at 0, and assume that g_0
  is smooth on [0, x*] and positive on (0, x*]. Fix 0 < r_0 < min(1, x*)/2 and a smooth chi with 0 <= chi <= 1,
  chi(t) = 0 for t <= 0 and chi(t) = 1 for t >= 1, and put v_N(x) = N^(-1) x^(7 + beta) chi(t) chi(N + 2 - t) with
  t = log(r_0/x), N >= 3. For large N, w_0 + v_N is a compatible trace that equals w_0 on [0, r_0 exp(-(N + 2))] and on
  [r_0, x*], and its critical seminorms sup_(0<x<=r_0) x^(i - 7 - beta) |v_N^(i)(x)|, i = 0, 1, 2, are O(1/N); with
  r = r_0 in 6.3.1 (i), the differences of the four Taylor coefficients and of the tail on [r_0, x*] vanish, so
  w_0 + v_N tends to w_0 in the norm of 6.3.1 (i) with sigma = beta. Moreover B_3[w_0 + v_N] - B_3[w_0] tends to
  kappa_A > 0 as N tends to infinity: the amplitude 1/N is spread over a logarithmic interval of length N. The proof
  uses the convergent form of 6.3.1 (i) and a bound C (x + x^(-beta))/N on (0, r_0], uniform in N, for the remainder
  after the leading term -(A^(beta - 2)/2) v_N'' x^(-6-beta) is subtracted from the difference of the integrands in that
  form; the bound is integrable because beta < 1, and the proof uses no numerical value. So for A > 2 the local
  Lipschitz assertion of 6.3.1 (i) cannot hold with sigma = beta, even on smooth compatible traces at fixed A and x*.
  The analogous statement holds at the source for the critical exponent theta = 1 - beta of the tail norm of 6.3.1 (i)
  (verifier; checked by the lead researcher by hand; audited by an external referee). With w_0, g_0 and chi as above,
  let g_* = g_0(x*) and assume g_* != 2A - 2; fix 0 < d_0 < min(1, x*)/2 and put delta = x* - x, t = log(d_0/delta) and
  v_N(x) = N^(-1) delta^(3 - beta) chi(t) chi(N + 2 - t), N >= 3. For large N, w_0 + v_N is a compatible trace that
  equals w_0 on [0, x* - d_0] and on [x* - d_0 exp(-(N + 2)), x*], the C^(2,1-beta) norm of v_N on [0, x*] is O(1/N), so
  that for any fixed 0 < r <= x* - d_0, theta = 1 - beta and beta < sigma <= 2, w_0 + v_N tends to w_0 in the norm of
  6.3.1 (i), and B_3[w_0 + v_N] - B_3[w_0] tends to (1 - beta)(3 - beta)(2 - beta - g_*/A)/(6A g_*^(2 + beta)), which is
  positive for g_* < 2A - 2 and negative for g_* > 2A - 2; the density slope g_N rebuilt from w_0 + v_N satisfies
  g_N = lambda_N g_0 on [x* - d_0 exp(-(N + 2)), x*], with lambda_N = 1 + O(1/N). So for A > 2 and g_* != 2A - 2 the
  local Lipschitz assertion of 6.3.1 (i) cannot in general be extended to theta + beta = 1, even with beta < sigma <= 2
  and smooth compatible traces. The hypothesis g_* != 2A - 2 can be dropped if g(x*) is allowed to move (verifier;
  checked by the lead researcher by hand; audited by an external referee). Let g_* = 2A - 2, fix 0 < d_0 < min(1, x*/4)
  and a smooth f_0 >= 0, not identically 0, supported in (x*/4, x*/2), and put I = int_0^{x*} f_0/w_0^2 dx > 0 and
  u_n(x) = n^(-2) delta^(3 - beta) chi(t) chi(n^3 + 2 - t). Then w_0 + f_0/n + u_n tends to w_0 in C^(2,1-beta)[0, x*],
  the rebuilt g satisfies g(x*) = g_* + A g_* I/n + O(n^(-2)), and B_3[w_0 + f_0/n + u_n] - B_3[w_0] tends to
  -(1 - beta)(3 - beta) I/(6A g_*^(1 + beta)) < 0: the coefficient
  (1 - beta)(3 - beta)(2 - beta - g/A)/(6A g^(2 + beta)) of the statement at the source vanishes at g = 2A - 2 with
  derivative -(1 - beta)(3 - beta)/(6A^2 g_*^(2 + beta)), the interior perturbation f_0/n moves g(x*) by
  A g_* I/n + O(n^(-2)), and the source layer u_n, of amplitude n^(-2) and logarithmic length n^3, contributes
  n + O(n^(-2)) times that coefficient at the moved value, up to O(1/n); multiplying u_n by a constant c != 0 multiplies
  the limit by c. If instead g(x*) = 2A - 2 is kept exactly, there is no jump of this kind for perturbations at the
  source: for each sufficiently small fixed d_0 > 0 there are eps_0, C > 0, depending only on the base and d_0, such
  that |B_3[w_0 + v] - B_3[w_0]| <= C ||v||_(C^(2,1-beta)[0, x*]) for every smooth v compactly supported in
  (x* - d_0, x*) with ||v||_(C^(2,1-beta)[0, x*]) <= eps_0 for which the g rebuilt from w_0 + v satisfies g(x*) = g_*,
  and such v != 0 exist with arbitrarily small norm. The fixed-value bound follows from a more precise estimate for
  perturbations at the source alone, in which the coefficient is taken at the moved value of g(x*) (verifier; checked by
  the lead researcher by hand; audited by an external referee). Let
  K(g) = (1 - beta)(3 - beta)(2 - beta - g/A)/(6A g^(2 + beta)) be the coefficient of the statement at the source, with
  g_* = g_0(x*) now arbitrary. For each sufficiently small fixed d_0 > 0 there are eps_0, C > 0, depending only on the
  base and d_0, such that |B_3[w_0 + v] - B_3[w_0] - K(g_v(x*)) J(v)| <= C e(v) for every smooth v that vanishes on
  [0, x* - d_0] and near x* and satisfies e(v) <= eps_0; here g_v is rebuilt from w_0 + v,
  e(v) = max_(i <= 2) sup_(0<delta<d_0) delta^(i - 3 + beta) |v^(i)(x* - delta)| and
  J(v) = int_0^(d_0) v(x* - delta) delta^(beta - 4) d delta, which is finite for each such v but not bounded in terms of
  e(v). At g_* = 2A - 2 it gives a jump without the interior perturbation: with
  I_s = int_0^(d_0) delta^(3 - beta) chi(log(d_0/delta))/w_0(x* - delta)^2 d delta > 0, the traces w_0 + v_n with
  v_n(x) = n^(-1) delta^(3 - beta) chi(t) chi(n^2 + 2 - t) tend to w_0 in C^(2,1-beta)[0, x*], their rebuilt g satisfies
  g(x*) = g_* + A g_* I_s/n + O(n^(-2)), and B_3[w_0 + v_n] - B_3[w_0] tends to
  -(1 - beta)(3 - beta) I_s/(6A g_*^(1 + beta)) < 0; multiplying v_n by a constant a != 0 multiplies this limit by a^2,
  so sequences of this form give jumps of one sign only. The discontinuity at 0 in the critical case sigma = beta above
  persists when g(x*) and the whole germs of w and g at x* are fixed, for every value of g_* (verifier; checked by the
  lead researcher by hand; audited by an external referee). With w_0, g_0, chi and r_0 as in the statement at 0 above,
  fix a real number a and let p_N(x) = a N^(-1) x^(7 + beta) chi(t) chi(N + 2 - t) with t = log(r_0/x), the family at 0
  above multiplied by a; let f >= 0 be smooth, not identically 0, with support in a fixed compact subinterval of
  (r_0, x*), and let t_N be the small solution of int_0^{x*} [1/(w_0 + p_N + t_N f) - 1/w_0] dx = 0; it exists and is
  unique for large N, with t_N = O(1/N), since the contribution of p_N to this integral is O(1/N) and its derivative in
  t_N at 0 is -int_0^{x*} f/w_0^2 dx < 0. Then w_0 + p_N + t_N f tends to w_0 in the norm of 6.3.1 (i) with sigma = beta
  and r = r_0, equals w_0 near 0 and near x*, has a rebuilt g equal to g_0 on a fixed neighbourhood of x*, and
  B_3[w_0 + p_N + t_N f] - B_3[w_0] = a kappa_A + O(1/N). This does not contradict the estimate at a fixed value
  g(x*) = 2A - 2 above, which concerns perturbations supported near x*. These traces also show that finitely many local
  observations do not determine B_3, even near w_0 (verifier; checked by the lead researcher by hand; audited by an
  external referee). Fix delta in (0, x*), choose r_0 above with r_0 < min(1, delta)/8 and f with support in a compact
  subinterval of (2 r_0, delta), and a compact interval K of values of a. For each fixed N large enough, depending on K,
  the traces w_0 + p_N + t_N f, with p_N and t_N now regarded as functions of a, depend smoothly on a in K, all of them
  agree with w_0 near 0 and on [delta, x*], with rebuilt g equal to g_0 there, the map a -> B_3[w_0 + p_N + t_N f] is
  continuous on K, and B_3[w_0 + p_N + t_N f] - B_3[w_0] - a kappa_A = O(1/N) uniformly for a in K. For every real b and
  every eps > 0, take K = [a_-, a_+] with B_3[w_0] + a_- kappa_A = b - 1 and B_3[w_0] + a_+ kappa_A = b + 1; for N large
  enough, the intermediate value theorem gives a compatible trace w with B_3[w] = b exactly, within eps of w_0 in the
  norm of 6.3.1 (i) with sigma = beta and r = r_0, that agrees with w_0 near 0 and on [delta, x*], with g equal to g_0
  there. Since delta can be chosen below every positive point of any finite set S in [0, x*], every quantity computed
  only from finitely many derivatives of w and g at the points of S has the same value on all these traces, while B_3
  takes every real value on them. The same construction gives closeness in ordinary Hoelder norms at the critical order
  (verifier; checked by the lead researcher by hand; audited by an external referee). With
  ||u||_(C^(k,beta)) = sum_(j <= k) sup |u^(j)| + sup_(x != y) |u^(k)(x) - u^(k)(y)|/|x - y|^beta on [0, x*], the trace
  w of the preceding statement can be chosen, for every real b, every eps > 0 and every delta in (0, x*), so that in
  addition ||w - w_0||_(C^(7,beta)) + ||g - g_0||_(C^(8,beta)) < eps, with g rebuilt from w. The proof bounds, uniformly
  for a in K, |p_N^(j)(x)| by C N^(-1) x^(7 + beta - j) and the derivative of order j of the difference of the rebuilt
  densities by C N^(-1) x^(8 + beta - j), for j <= 9, and uses that a function F, continuous on [0, x*] and
  C^1 on (0, x*], with F(0) = 0, |F(x)| <= e x^beta and |F'(x)| <= e x^(beta - 1) has beta-Hoelder seminorm at most C e.
  So B_3 takes every real value on compatible traces w in every neighbourhood of w_0 in C^(7,beta)[0, x*], even when
  g - g_0 is also required to be small in C^(8,beta)[0, x*] and the germs at 0 and at x* are fixed; the family is
  different from h_eps above, which tends to 0 in C^m for every integer m < 7 + beta but not in C^(7,beta)[0, x*] (for
  eps <= x*/2 the beta-Hoelder seminorm of h_eps^(7) on [0, x*] equals |t| times that of phi^(7) on [0, infinity)). At 0
  this discontinuity has an exact first-order description, and a Dini condition on the derivative of order 7 is
  sufficient for continuity (verifier; checked by the lead researcher by hand; audited by an external referee). With w_0
  and g_0 as in the statement at 0 above, fix 0 < r_0 < min(1, x*)/4 so small that w_0 is odd and analytic on [0, r_0],
  and for smooth v with compact support in (0, r_0) put E(v) = max_(i <= 2) sup_(0<x<=r_0) x^(i - 7 - beta) |v^(i)(x)|,
  M(v) = int_0^(r_0) v(x) x^(-8-beta) dx, omega_v(x) = sup_(0<s<=x) |v^(7)(s)|/s^beta and
  D(v) = omega_v(r_0) + int_0^(r_0) omega_v(x) dx/x. There are eps_0, C > 0, depending only on the base and r_0, such
  that |B_3[w_0 + v] - B_3[w_0] - kappa_A M(v)| <= C E(v) for every such v with E(v) <= eps_0; the constants do not
  depend on where the support of v lies in (0, r_0). The same estimate holds, with constants depending also on f, for
  the trace w_0 + v + t(v) f of the statement with the source germ fixed, where f is supported in a compact subinterval
  of (r_0, x*), |t(v)| <= C E(v) and the rebuilt g equals g_0 near x*. The moment M(v) is finite for each such v but not
  bounded in terms of E(v); the same integral evaluated on p_N above, taken with this r_0, equals
  a + (2a/N) int_0^1 chi(t) dt. Taylor's formula at 0 gives E(v) <= C omega_v(r_0) and
  |M(v)| <= C int_0^(r_0) omega_v(x) dx/x, so |B_3[w] - B_3[w_0]| <= C D(v) for both traces w whenever E(v) <= eps_0,
  and, for beta < gamma < 1, D(v) <= (1 + 1/(gamma - beta)) r_0^(gamma - beta) [v^(7)]_gamma, where [v^(7)]_gamma is the
  gamma-Hoelder seminorm of v^(7) on [0, r_0]. Hence B_3 converges to B_3[w_0] along both traces when v, supported in
  (0, r_0), tends to 0 with D(v), in particular when v tends to 0 in C^(7,gamma) for some gamma > beta, while by the
  preceding statement gamma = beta is not enough; only sufficiency of the Dini condition is asserted. These statements
  concern compatible axis data, not profiles. A small residual of the third axis equation does not control B_3 either
  (verifier; checked by the lead researcher by hand; audited by an external referee). Let A > 2 and let w, g be smooth
  on [0, x*] and analytic near both ends, with w odd and g even near 0, satisfying w g' = (w' - A) g, w < 0 on (0, x*),
  g > 0 on (0, x*], w = -A x + O(x^3) and g = x^2 + O(x^4) at 0, and w(x*) = 0, w'(x*) = A; let h, F_3 and H_3 be as in
  6.3.1 (a), with H_3/x^(6 + beta) -> 1 at 0. For a trace G that is smooth on [0, x*] and even and analytic near 0, let
  r_G = w G' + (3h - 1) G - F_3 be its residual in the third axis equation. Then B_3 = f.p. int_0^{x*} r_G/(w H_3) dx,
  where the finite part is taken at 0 and the integral converges at x*; there is no endpoint term, since the finite part
  of G/H_3 at 0 is zero and G/H_3 -> 0 at x*, and the weight satisfies 1/(w H_3) ~ -(1/A) x^(-7-beta) at 0. On the data
  of R12 with A = 4 and x* = L = 1, where B_3 < 0, let G_* be the solution of the third axis equation that is bounded at
  x* (it is analytic there) and, for small eps > 0, put G_eps = G_* - B_3 H_3 chi(x/eps), with chi fixed and smooth,
  equal to 1 on [0, 1] and to 0 on [2, infinity). Then G_eps is smooth on [0, x*], analytic near both ends and even near
  0, and equals G_* on [2 eps, x*]; its residual r_(G_eps) = -B_3 w H_3 chi'(x/eps)/eps is supported in [eps, 2 eps],
  and ||r_(G_eps)||_(C^j[0, x*]) = O(eps^(6 + beta - j)) for j = 0, ..., 6. These residual norms tend to 0 as eps tends
  to 0 while B_3 is unchanged. So |B_3| cannot be bounded by unweighted C^j norms (j <= 6) of the third-order axis
  residual with a constant that depends only on w and g. This concerns the axis hierarchy, not the residual of a
  two-dimensional state.
- Weaker sign tests and endpoint conditions (external referee results; checked by the lead researcher; the A = 4 trace,
  the crossing count and the moment threshold on the compatible data of 6.3.2 (a), and the endpoint relations at P
  recomputed by the verifier with separately written code and confirmed, the crossing count with a proof and the moment
  threshold numerically; the implications (i) to (iv) and the coverage statements on the compatible data confirmed
  by the verifier by hand). Under all the trace and source hypotheses of 6.3.1 (k), in particular A > 2 and
  theta > 1 - 2/A, write R = Q - P(m) - Q(x*) as a function of m. Each of the
  following conditions implies B_3 > 0; (i) and (ii) are implied by (H_-), (iii) allows one sign change, and (iv) is
  stronger than (H_-) [corrected 2026-10-20: an earlier version said that each is weaker than (H_-) or of a different
  kind]: (i) int_0^m R(t) dt <= 0 for every m, strict somewhere (the integral of 6.3.1 (k) equals (2 - beta)
  int_0^infinity (int_0^m R) m^(beta - 3) dm); (ii) for some delta with max(0, 1 - theta) < delta < beta, the tail
  int_m^infinity R(t) t^(delta - 2) dt is <= 0 for every m and < 0 for some m; (iii) R changes sign once, from positive
  to negative as m increases, and int_0^infinity R m^(delta - 2) dm <= 0 for such a delta (multiplication by the
  increasing factor m^(beta - delta) strengthens the negative part); (iv) Q - P(m) is nondecreasing in x and not
  constant, which implies (H_-). On the compatible data of 6.3.2 (a), the moment in (iii) is <= 0 exactly when L^2 >=
  6A(8 - 3 delta)/(16 - delta), a threshold that decreases to S_A as delta increases to beta; for S_A < L^2 < 3A the
  remainder has exactly one crossing, so test (iii) detects every member with S_A < L^2 < 3A, while (H_-), (i) and (iv)
  hold there exactly when L^2 >= 3A (where the remainder does not change sign, so (iii) in its literal form does not
  apply); together the tests cover every member of the family with B_3 > 0. [Corrected 2026-10-20: an earlier version
  said that test (iii) alone detects every member with B_3 > 0; at L^2 = 4A the remainder is strictly negative.] At P
  the source expansion gives g'(x*) = w''(x*) g*/A and Q(x*) = w''(x*)(g* - A)/(2 A g*^3), and (H_-) implies only
  Q(x*) >= 0: an exact compatible trace at A = 4 (given in the variable m by h(m) = (m^2 + 1 + 1/(m^2 + 1))/16, g = 1/h,
  w = -m/h and x(m) = (1/4) int_m^infinity dt/h(t), x* = x(0)) has g* = 8, w''(x*) = Q(x*) = 0 and R < 0 strictly.
  Neither g* > A nor w''(x*) > 0 follows from the axis equations (compatible counterexamples exist), and both hold at
  the zero L^2 = S_A of 6.3.2 (a), where (H_-) fails, so endpoint signs cannot replace the integral condition. The slope
  condition (Q - P(m))'(x*) >= 0 is necessary for (H_-) only where this derivative exists, which C^(2,theta) regularity
  at x* does not guarantee. The lead researcher checked the endpoint relations, the A = 4 trace (there P(m) = m (m^2 -
  1)^2/2048 and R(m) = -m (8 m^10 + 34 m^8 + 60 m^6 + 52 m^4 + 20 m^2 + 1)/(2048 (1 + m^2)^6), exactly) and the
  counterexample traces symbolically, and the moment threshold numerically to 15 digits. These traces are axis data, not
  profiles.
- (H_-) on the stored fits (lead researcher; recomputed by the verifier with separately written code and confirmed, with
  the scope stated below). On the ten stored trial traces of 6.3.2 (d), with P obtained as the divergent part of Q (a
  fit of Q/m^5 in powers of m^(-2) near 0, twelve fit windows; validated on the compatible data of 6.3.2 (a) at L = 8.6
  and at the zero L*, where it reproduces the exact remainder to 1e-3 and the failure of (H_-) for x/x* > 0.95), the
  sampled values of x*^5 (Q - P(m) - Q(x*)) are negative on 0.06 <= x/x* <= 0.999 for every trace and window: about
  -0.5, -1.2, -0.6 and -0.1 at x/x* = 0.1, 0.5, 0.9 and 0.98, with fitted limit -x*^5 Q(x*) = -0.15 to -0.17 at 0 (below
  x/x* = 0.06 the fitted asymptotic form was used) and an approximately linear approach to 0 at x*. The integral of
  6.3.1 (k) gives B_3 = 0.29 to 0.31 on these traces, consistent with 6.3.2 (d). The verifier's recomputation used two
  routes for P: the fit of Q/m^5 above, and the Taylor coefficients of a polynomial fit of w near 0, which is exact on
  the compatible data of 6.3.2 (a). On all ten traces both routes give x*^5 (Q - P(m) - Q(x*)) < 0 at every sampled
  point of 0 < x/x* <= 0.9995. The maximum on 0.06 <= x/x* <= 0.9995 is -2.5e-3 to -2.4e-3, attained at x/x* = 0.9995.
  This is the linear approach to 0 at x*, with slope 4.74 to 4.99 in x/x*. The two routes differ by at most 0.03 at
  x/x* = 0.06 and 0.1. The integral gives B_3 = 0.2945 to 0.3011. The remainder near 0 is very sensitive to the 1-jet of
  w. The traces have w'(0) + A = 2.4e-11. A polynomial fit that forces w'(0) = -A turns that offset into errors in the
  higher Taylor coefficients that enter P, and these move the value at x/x* = 0.06 by about +6; with the constant left
  free the two routes agree as stated. The lead researcher's earlier second route, a fit with the same constraint
  weighted by x^3, agreed with the first route within 0.08 at x/x* = 0.06; the weight reduces the influence of the
  points near 0, where the offset matters most. [Corrected 2026-10-20: an earlier version of this item attributed the
  shift of the unweighted fit to the sampling error of w; the cause is the forced constant, as found by the verifier.]
  The sign near 0 also depends on the model used for w at the origin, which the data do not determine (verifier, with
  separately written code). Adding one non-polynomial term e x^(k + beta) to the fit of w, for k = 7, 9 or 11, fits the
  data at least as well as one more even power; the differences in the fit residual are at the level of the offset
  2.4e-11, so they do not detect such a term. With k = 9 or 11, and on the stored traces of X3 and F3 in
  every model, the remainder stays negative at all samples. With k = 7 it is positive at x/x* = 0.06 on the eight other
  traces (+0.03 to +0.61), and on one of them also at x/x* = 0.1. For x/x* >= 0.2 it is negative at the samples x/x* =
  0.2, 0.3, 0.5, 0.9, 0.98, 0.995 in every model and on every trace (at most -0.44 at 0.2, 0.3 and 0.5), and the models
  differ by at most 0.02 at x/x* = 0.9. In these tests the fitted non-polynomial term serves only to refit the
  polynomial coefficients d_3, d_5, d_7 that enter P; it is dropped from the series used on 0 < x < 0.06 x*. With the
  refitted coefficients the integral gives B_3 = 0.28 to 0.30 (0.2945 to 0.3016 for the analytic model, over the
  calculation above and these refits). These are sensitivity values of the estimator, not values of the convergent
  integral of 6.3.1 (k) for a trace that carries such a term: the term x^(k + beta) with k = 7 is at the critical origin
  order 7 + beta of the item "Conditioning" above, and a nonzero term e x^(7 + beta) in w down to 0 adds -e
  (7 + beta)(6 + beta) x^(beta - 1)/2 to Q to leading order (g/x^2 -> 1), a multiple of m^(1 - beta), so that the
  integrand of 6.3.1 (k) gains a nonzero multiple of 1/m as m -> infinity and the ordinary integral diverges
  logarithmically; such a trace violates the origin hypothesis of 6.3.1 (k) (lead researcher's computation, prompted by
  an external referee; checked by the verifier by hand and, at A = 4, symbolically). So the sampled values and the
  fitted endpoint models are consistent with (H_-) on these trial traces for x/x* >= 0.2 under every origin model tested
  (densely sampled on 0.2 <= x/x* <= 0.9995 in every model), on 0.06 <= x/x* < 0.2 under the analytic model and the
  models with k = 9 and 11 but not with k = 7, and on 0 < x/x* < 0.06 (series) only under the analytic model; the margin
  vanishes at x*, and there is no enclosure between sample points, so a uniform sign is not certified.
  [Corrected 2026-10-20: an earlier version stated the sign on 0 < x/x* < 0.2 without the dependence on the origin
  model.] [Corrected 2026-10-20: an earlier version said that these trial traces satisfy (H_-).] This is a statement
  about trial traces; unweighted uniform control of the remainder does not preserve its sign near x*, where it vanishes,
  and by 6.3.2 (c) it does not transfer to nearby exact profiles without control of w near 0 in the norm of 6.3.1 (i).
- Reading and size of the sign criterion of 6.3.1 (k) (lead researcher; the identities and the scaling law confirmed by
  the verifier with separately written code; the trace values below are route dependent). On the axis the y^2
  coefficient of W_1 is (g' - w'')/2, so Q = (1/2) d_y^2 W_1/(d_y rho)^3 there, and the forcing of the y^3 equation on
  the axis is (g^4/3) Q' (checked symbolically). So (H_-) is a pointwise upper bound on the transverse curvature of the
  horizontal velocity on the axis, measured against the cube of the axis density gradient. In normalized form (external
  referee; checked symbolically by the lead researcher, and by the verifier by hand and symbolically), with z = G_3/g^3
  and Z = z - z_P, where z_P = -(1/3) sum over j = 1, 3, 5 of j pi_j m^(j - 1)/(j - 1 + beta) is the polynomial solution
  for the forcing P, the y^3 equation reads (m^beta Z)_m = -(1/3) m^(beta - 1) dR/dm: its forcing is the derivative of
  the unknown remainder, and the hierarchy gives no sign. As a measure of margin (not a family of profiles: g and w are
  coupled through the velocity law), replace g by mu g at fixed w; the compatibility condition is preserved. Evaluated
  with H_3 as printed in 6.3.1 (a), without restoring the normalization g/x^2 -> 1 at 0, the finite part becomes
  mu^(-1-beta) (b_0 + b_1/mu) exactly, where b_0 and b_1 come from the parts g'/(2g^3) and -w''/(2g^3) of Q; with the
  normalization restored (H_3 multiplied by g_0^(-3-beta), g_0 = lim g/x^2 = mu) it is mu^2 b_0 + mu b_1. Both vanish
  for mu > 0 exactly at mu_0 = -b_1/b_0, the quantity used here. [Corrected 2026-10-20: an earlier version called the
  first expression B_3(mu) without stating the normalization.] On the compatible data of 6.3.2 (a) at L = 8.6 the
  sampled-data estimate mu_0 = -b_1/b_0 = 0.3855 differs from the exact value S_A/L^2 = 0.3861 by about 0.0006. On these
  data mu_0 = S_A/L^2 and the (H_-) threshold mu = 3A/L^2 hold exactly (verifier). On the ten stored traces of 6.3.2
  (d), under the analytic origin model, mu_0 = 0.22 to 0.34, and the sampled test of (H_-) passes for mu above estimated
  thresholds of 0.45 to 0.55 (not certified thresholds for the uniform condition). These values combine the lead
  researcher's and the verifier's routes, which differ at the 0.05 level because of the sensitivity of the origin layer.
  With the origin models of the previous item counted (verifier, three traces), mu_0 = 0.22 to 0.37; the estimated
  threshold stays at 0.45 to 0.55 for k = 9, and for k = 7 it exceeds 1 on two traces in two of three fit windows, so
  that there the sampled test fails at mu = 1. [Corrected 2026-10-20: an earlier version gave mu_0 = 0.249 to 0.293 from
  one route only.] In these estimator experiments, at fixed axis velocity, the estimated zero corresponds to scaling the
  axis density gradient down by a factor of about 2.7 to 4.5 (1/0.37 to 1/0.22). The integral is concentrated near P: on
  the published candidate about 70 percent of B_3 comes from x/x* > 0.9 and 39 percent from x/x* > 0.995 (69 and 39
  percent on the compatible data at L = 8.6). These are statements about trial traces; by 6.3.2 (c) they do not transfer
  to nearby exact profiles.
- Kernel representation of Q (external referee; the formula checked numerically by the lead researcher to about 1e-12 on
  a test density; confirmed by the verifier by hand, and by a separately written quadrature against two test densities
  with closed-form velocity, one of them not radial, to 6e-10). On the axis, (g' - w'')/2 = g'/4 - (12/pi) I(x), where
  I(x) is the limit as epsilon -> 0 of the integral over the first quadrant, with the half-disk (u - x)^2 + v^2 <=
  epsilon^2 removed, of [J(x - u, v) + J(x + u, v)] rho(u, v), J(t, v) = t v (t^2 - v^2)/(t^2 + v^2)^4, for rho of class
  C^(2,alpha) near (x, 0) with the parity and the growth bound of the class, and the local term g'/4 comes from the
  distributional second derivative of the kernel; the weight has integral 0 along every horizontal half-line, so
  positivity of rho cannot sign Q through the kernel (compare 6.3.1 (l)). Positive bumps that move Q in either direction
  do not in general respect the transport equation, so this does not decide the sign for exact profiles.
- Positivity examples (external referee results; not checked by the verifier; not used elsewhere). The first referee
  of 6.3.1 (l) gives explicit positive densities showing that the velocity law and positivity alone do not fix the
  signs of d_3, d_5, d_7, and the second referee constructs positive perturbations of rho, satisfying the tangent
  constraints of 6.3.1 (l), that give either sign of the first variation. [Moved 2026-10-20 from 6.3.1 (l).]
- Further results of the referee of 6.3.1 (n) (external referee; not checked by the verifier). The same referee gives a
  renormalized representation of B_3 as an integral of rho over the quadrant against a weight that depends on the trace
  itself, with an axis-concentration limit and endpoint terms that diverge separately; it gives no sign. For a test of
  the transport equation against a solution phi of the adjoint equation W.grad phi + (1 + 2c_l) phi = f with f >= 0 (a
  test the lead researcher put to the referee), the referee finds that phi decays only at the critical order
  R^(-2-1/c_l), at which the far-field boundary flux (the integral of rho phi W.n over the quarter circle of radius R)
  is O(1), since rho = O(R^(1/c_l)) by R2, |W| = O(R) and the arc has length O(R). If phi is regular enough for the
  divergence theorem on the punctured quadrant, the other boundary fluxes vanish (for instance for phi with finite axis
  traces and bounded near 0 and P) and rho f is integrable, the limit of that flux is the integral of rho f over the
  quadrant, which is positive when f is nonzero where rho > 0; so the flux cannot be discarded and the test gives no
  sign. [Corrected 2026-10-20: an earlier version assigned the order R^(-2-1/c_l) to the boundary contribution instead
  of the test function, and described the test as proposed by the referee.] Positive fields constructed by the referee
  do not satisfy the transport equation (at the centre their horizontal eigenvalue is near -1 instead of -A), so they do
  not establish either sign of B_3 on exact profiles.
- Local structure at a singular source (external referee; the coefficient identities checked by the lead researcher with
  the referee's symbolic script, which checks the algebra only, and the normalization against 6.3.1 (g) by hand; the
  normalization k, the degrees q + 1 and 2q - 1 of the first corrections, the quadratic-jet constraints, the logarithmic
  axis equations, the constant c, the resonant coefficient J and e = -J/(2(A - 1)) recomputed by the verifier; the
  existence of the corrections and the function-space statements not checked). This concerns a profile of the type left
  open in Q4 below, with l_3 != 0. With the frozen mode V of 6.3.1 (g) normalized by G_3[V]/H_3 -> 1 on the left, its
  right-side expansion carries k s^(-beta) y^3 log|y/s|, k = -2 sin(pi beta) g*^(3 + beta)/pi, and the companion term in
  log s cannot be omitted. The quadratic jets of the smooth part at P are constrained by divergence, curl and transport
  (consistent with g'(x*) = w''(x*) g*/A above). Here l = l_3, since V has unit normalized third-trace limit. Formal
  degree counting places the first correction equations for l V at radial degrees q + 1 and 2q - 1, q = 3 - beta; these
  forced frozen equations have not been solved on a neighbourhood of P (on a left cone, 6.3.1 (r) constructs coupled
  solutions with this leading frozen term in the parameter range stated there, and nothing on a neighbourhood of P). The
  calculation also identifies a possible fifth-jet resonance at quadratic order in l, formally resolved by a term l^2 e
  s^(-2 beta) y^5 (log|y/s|)^2; the coefficient e is a formal coefficient (checked by the verifier); the existence of
  such a correction has not been verified. Full formal consistency (the angular equations, matching across the
  characteristic directions, range conditions, integer resonances) is not established. A root of C_0 = 0 along such a
  construction removes only the third-jet obstruction; P_inf needs the conditions for j = 5, 7, ... as well. On function
  spaces: no Fredholm formulation in specified spaces suitable for this construction is known (the referee states that
  an isotropic Sobolev realization of the transport part is not Fredholm and that the continuum of frozen degrees of
  6.3.1 (g) blocks the usual choice of weights at P; in one Hoelder setting the linearization is not even upper
  semi-Fredholm, item (v) of the next item). If a Fredholm setting exists, bordering it by one scalar unknown (the mode)
  and one scalar equation (the row l + B_3 = 0) through bounded finite-dimensional blocks does not change the index;
  nearby existence would still require control of the complementary equations and of the reduced scalar equation, with
  the transversality number 1 + dB_3/dl nonzero and a quantitative crossing condition. A numerical design with l as an
  extra unknown, the correctors above and that row is proposed by the referee and has not been attempted.
- The frozen kernel at P (lead researcher; the Fourier identity, the general solution on eta != 0, the reproduction of
  the family of 6.3.1 (g) and the quasi-homogeneity degrees confirmed symbolically by the verifier; items (i) to (vii)
  checked by an external referee, who confirmed them in the form given here and refuted the stronger statements listed
  at the end; items (i) to (vii) then rechecked by the verifier, the concrete packet integrals and scaling predictions
  numerically at A = 3 and at rounded X3 parameters, the operator identities and correction arguments by hand, and the
  growth bound (iv) by a proof by hand and numerically; the verifier later proved independently, by a dyadic
  decomposition, by localized Fourier projections and by radial finite parts, the regularity class of (i) with its
  sharpness (class C^(m, alpha) when (m + alpha) A <= h, 0 < alpha < 1, and, for nonzero Phi, not of class C^(m, alpha)
  when (m + alpha) A > h and not C^n when n A >= h), the smoothness off P, the expansion of (ii) to every finite order,
  with its logarithmic terms at the resonant degrees and a C^N remainder for every N, the asymptotic form of G_j
  in (iii) for odd j and noninteger mu_j > 0 (its Taylor coefficients given by beta integrals, except for the
  logarithmic moment defining G_1(0)), the vanishing in (iii) of the normalized limits of every odd order, and the bound
  |v(X)| <= C (1 + |X|)^(1/A) and the failure of the gradient bound in (iv) for nonzero Phi, and these proofs were
  audited by a further external referee). With the convention v-hat(zeta) = int e^(-i X.zeta) v(X) dX, zeta = (xi, eta),
  the frozen equation L_g v = 0 of 6.3.1 (g) becomes (A xi d_xi + eta d_eta + A + 2 + g* xi^2/|zeta|^2) v-hat = 0, a
  first-order equation along the curves (xi_0 e^(A tau), eta_0 e^tau). In the sector odd in y, its general solution on
  eta != 0 is v-hat = Phi(xi/|eta|^A) sgn(eta) |eta|^(2b - A - 2) |zeta|^(-2b), b = g*/(2(A - 1)), Phi arbitrary,
  (distributional solutions supported on eta = 0 need separate treatment; see the end of this item), and the family of
  6.3.1 (g) is Phi(t) = c_+ t_+^(lambda - 1) + c_- t_-^(lambda - 1), with t_+ = max(t, 0), t_- = max(-t, 0) and
  lambda = (d - 1)/(A - 1); these Phi are not compactly supported and the statements below do not apply to them. Take
  Phi smooth with compact support in t != 0, with Phi(-t) = -conj(Phi(t)) (so that v is real) and int Phi dt = 0. Then
  v-hat, taken as the distributional limit of its truncations to |eta| > epsilon, has no residual part at zero
  frequency, and with s = x - x*, r = |eta|, q = 2(A - 1) and h = 1 + g*, v(s, y) = (2i/(2 pi)^2) int_0^inf (sin(y
  r)/r^2) int Phi(t) e^(i s t r^A) (1 + t^2 r^q)^(-b) dt dr, a real continuous solution, odd in y. (i) Regularity. v is
  C^infinity off P: the pieces of v with |eta| comparable to 2^n are 2^(-h n) H_n(2^(A n) s, 2^n y) with H_n uniformly
  Schwartz. [Numerical check by the verifier on the line s = 0 at height y_0 = 1, the only place where smoothness could
  fail: the sampled spectrum in s shows the predicted transition to rapid decay at frequencies of order 1e4 for A = 3,
  g* = 5.5 and of order 1e22 for the rounded X3 test parameters A = 10.15, g* = 29.75, in units where the packet sits at
  |eta| of order 1; below these frequencies v near the vertical line through P behaves like a function of class C^(h/A).
  This is finite-frequency agreement with the smoothness statement, which rests on the dyadic argument.] Near P, v is of
  class C^(m, alpha) when (m + alpha) A <= h, 0 < alpha < 1, and every nonzero such v fails to be C^n near P when
  n A > h. At X3, h/A = 3.0293, so v is C^(3, 0.029) and not C^4. (ii) Expansion. Near P, v is a Taylor polynomial plus
  a finite sum of terms quasi-homogeneous of degree h + 2k(A - 1), k = 0, 1, ..., under (s, y) -> (mu^A s, mu y), plus a
  C^N remainder. [Verifier check at A = 3, g* = 5.5: after the Taylor terms, given by convergent or analytically
  continued beta integrals, are subtracted, v(mu^A s, mu y)/mu^h tends to the finite-part leading term, and the next
  remainder scales with degree h + 2(A - 1), for mu = 1 to 2^(-5); the Taylor terms of degree above h are needed for
  this. This checks these samples, not the general C^N remainder statement.] These terms can carry logarithms; a residue
  can occur when h + 2k(A - 1) = A a_1 + a_2 with a_2 odd, and it is proportional to int Phi(t) |t|^(-2b-2k) t^(a_1)
  dt. (iii) Axis traces. For odd j let G_j(s) = d_y^j v(s, 0)/j! and mu_j = (1 + g* - j)/A. For noninteger mu_j > 0, G_j
  is a polynomial in s of degree below mu_j plus C_(j,+-) |s|^(mu_j) + o(|s|^(mu_j)), with possible logarithms at
  integer degrees, and, for j >= 3 and g* > j - 1, G_j(0) = (2 i^j/((2 pi)^2 j! q)) B((j - 1)/q, (g* - j + 1)/q) int
  Phi(t) |t|^(-(j - 1)/(A - 1)) dt, B the beta function (rederived by the lead researcher for j = 3). The integral
  vanishes for odd real Phi but not in general, so G_3(0) can be nonzero. [Numerical check by the lead researcher at
  A = 3, g* = 3.5, for Phi = i phi with phi(t) = b_1(|t|) - b_2(|t|), where b_a(t) = exp(-1/((t - a)(a + 1 - t))) on (a,
  a + 1) and b_a = 0 elsewhere (so int phi = 0): G_3(s) tends to the predicted G_3(0) = 3.1037e-5, and
  (G_3(s) - G_3(0))/s^(1/2) = -2.87934e-5 at s = 1e-4 against the leading-symbol value -2.87935e-5. The verifier
  confirmed this with independent code (relative error 1.2e-8 at s = 1e-6) and found the same structure at the rounded
  X3 test parameters A = 10.15, g* = 29.75: G_3(0) = 5.418995706e-6 (the formula gives 5.4187303e-6 at A = 10.150725,
  g* = 29.74949, also confirmed by the verifier, by the formula and by direct quadrature), and after G_3(0) + c_2
  s^2 + c_4 s^4 is subtracted the ratio to s^(mu_3) matches the leading-symbol constant to 1.4e-11.] G_j is bounded and
  continuous when g* > j - 1, and in every case |s|^((j - 1)/A) G_j(s) -> 0 as s -> 0 for every odd j >= 3, so the
  normalized endpoint limits l_j of these solutions vanish. [In the numerical check (Phi(t) = sgn(t) b_1(|t|)), the y^3
  coefficient is K s^(1/2) + c_1 s + o(s) as s -> 0+, with K equal to the value predicted by the leading symbol to the
  accuracy of the computation (6.00e-5 at s = 1e-4 against 6.05e-5) and c_1 stable to four digits; there mu_3 = 1/2 and
  G_3(0) = 0 because Phi is odd. The verifier confirmed K to 1e-8 at s = 1e-6 and identified c_1 = -5.2247e-5 as the
  analytically continued beta value. At the rounded X3 parameters the same odd packet has G_3 = c_1 s + K
  s^(2.734) + c_3 s^3 + ..., with c_1 = 8.83e-6 for this bump, so G_3 is not O(|s|^((g* - 2)/A)) there, while |s|^(2/A)
  G_3 -> 0. In the unbounded cases A = 3, g* = 3.5, j = 5, 7 and A = 2, g* = 1, j = 3 the verifier matched the singular
  coefficient of G_j to 1e-8 or better and confirmed the normalized limits.] At X3, mu_3 = 2.734, mu_5 = 2.537,
  mu_7 = 2.340. (iv) Growth. Without a cut-off every nonzero such v satisfies |v(X)| <= C (1 + |X|)^(1/A) with optimal
  exponent, and fails the weighted gradient bound of the profile class for every gamma < 1; only cut-off versions are
  relevant to the profile problem. Hence, when h/A > 3, the frozen equation has an infinite-dimensional space of
  solutions near P of class C^(2,alpha) for every alpha < 1, smooth off P, with l_j = 0 for every odd j >= 3; the
  imaginary even Phi of integral zero already give an infinite-dimensional real subspace. They realize the coupled
  packets of 6.3.1 (d). (v) The full linearization is not upper semi-Fredholm in a one-derivative-losing setting. Let T
  v = W.grad v - v + U[v].grad rho at a profile with W, rho of class C^(2,sigma) near the closure of a bounded domain
  Omega, W(P) = 0, and let K be a compact subset of Omega containing a neighbourhood of P. Then T from {v in
  C^(2,sigma): supp v in K} to C^(1,sigma)(closure of Omega) is not upper semi-Fredholm: the bumps v_eps = eps^(2+sigma)
  phi((X - P)/eps) have C^(2,sigma) norms bounded above and below, tend to 0 in C^2 and satisfy ||T
  v_eps||_(C^(1,sigma)) = O(eps), while a finite-dimensional kernel and closed range would give a convergent
  subsequence. Odd bumps and reflected pairs respect the symmetries; for inputs with the parity of the problem, K must
  also contain neighbourhoods of the points obtained from P by that parity (for P = (a, 0), the point (-a, 0)). For an
  unbounded domain the statement needs separate uniform mapping assumptions, which are not established here. (The lead
  researcher checked the argument by hand; the verifier proved it independently in this setting, and also proved that no
  fixed finite set of bounded linear constraints, output rows or parameter columns makes the operator upper
  semi-Fredholm in the same spaces; that proof was audited by a further external referee.) This does not produce a
  kernel element and does not apply automatically to other norms. (vi) Correction. Whether a cut-off packet q_Phi
  corrects to a kernel element of T is the range condition -T q_Phi in T(Z), with Z a correction class that preserves
  the packet germ (for example, corrections smooth near P). It is open; smoothness of the error does not imply it. Even
  infinitely many independent kernel elements would not give a nonlinear family (F(u) = ||u||^2 on a Hilbert space has
  the whole space as derivative kernel at its isolated zero), and a nonlocal correction need not preserve smoothness at
  the center. (vii) Variable coefficients. For a background of class P_2 (W of class C^(2,alpha)) the cut-off error of a
  packet is in general only known to be in C^(1,sigma), and it need not be small; under the anisotropic scaling a term c
  y^2 d_s becomes c eps^(2 - A) y^2 d_s, which is not small for A > 2. In the lead researcher's reading, a reduction to
  the frozen model in linearizing coordinates of W at P, in which the packets bend along the weak characteristics, needs
  W smooth near P, which P_2 does not give. Q1 is therefore undecided in both P_2 and P_inf on this evidence. A basis
  smooth at P contains none of these solutions exactly, but smooth functions approximate their cut-offs in C^(2,alpha)
  when h/A > 3, so the isolation of a discrete solution does not decide Q1 by itself; what is missing is a continuum
  stability and convergence theorem. If cut-off packets did correct to exact solutions of the nonlinear problem, the
  solutions of P_2 near the computed branch would contain an infinite-dimensional family parametrized by singular data
  at P, with l_3 = 0; B_3 could vary along it only through members that are not smooth near 0 (a member smooth near 0
  with l_3 = 0 has B_3 = 0), and a nonlinear family would need a separate existence and parametrization theorem. This is
  a heuristic reading; it is repeated as such in 6.5 and is not used as a result. Stronger statements that are false
  (external referee): that near P such v is a pure sum of quasi-homogeneous terms (Taylor terms and logarithms occur);
  that its y^3 axis coefficient is O(|s|^((g* - 2)/A)) at P (G_3(0) can be nonzero, although l_3 = 0 holds); that every
  tempered solution is given by the formula above plus conormal terms supported on eta = 0 (characteristic data must be
  allowed to be distributions, and line-supported terms come in triangular systems: for A > 2, mu = (g* - 2)/A,
  a(s) = |s|^mu and the homogeneous primitive E(s) = |s|^(mu + 2)/((mu + 1)(mu + 2)) (E'' = a), L_g[y^3 a] = 6 g* y
  E != 0, while y^3 a - (3 g*/(A - 1)) y E solves the equation); and that an anisotropic dilation of shrinking packets
  gives kernel elements of the full operator (the frozen operator is not anisotropically invariant; under the scaling
  its velocity multiplier becomes -xi^2/(xi^2 + eps^(2A - 2) eta^2)).
- Correction of packets on a smooth background and the first variation of the obstruction (external referee; audited by
  a second external referee, whose added hypotheses are included below; the bending coefficient d, the exponents and the
  product-rule form of the variation checked by the lead researcher by hand; the bending coefficient d and the
  normalized exponents, the first variation (symbolically, and numerically at A = 4 on the data of 6.3.2 (a) with L = 4
  and the direction x^3 (16 - x^2)^2, against finite differences of B_3 to about 1e-12), the variation terms with A
  varying, the structural zero of delta C_(0,j) and the logic of (ii), (iii) and (iv) checked by the verifier; the
  existence of data with nonzero bending coefficients and the construction of Q_N are the referee's and not checked by
  the verifier, and the finite-dimensional quotient hypothesis of (iii) is not established). Assume A > 2, a background
  smooth near P, and no flow resonance (A not an even integer,
  or the coefficient that would require a term Y^A log|Y| vanishes). (i) Packets. In smooth coordinates (S, Y) near P
  with Y = rho/g* and det D(S, Y) = 1, W = A S d_S + Y d_Y. Starting from the frozen packet of the previous item, a
  recursion in the anisotropic degree whose divisors are the positive degree increments gives, for every admissible Phi
  and every finite N, a linear map Phi -> Q_N Phi to functions supported near P and smooth off P whose residual T Q_N
  Phi is of class C^N near P. Homogeneous-extension resonances (degree A a + c, c odd) give logarithms with polynomial
  defects and do not obstruct this; exact nonresonance at the computed parameters cannot be certified from rounded
  values. The regularity threshold (m + alpha) A <= h is that of (i) of the previous item, and distinct data give
  distinct germs modulo C^N when N A > h. Away from the support the residual is U[Q_N Phi].grad rho, which is smooth
  only where rho is. (ii) Physical axis limits. The linearizing coordinate bends along the weak characteristic,
  S = s + d y^2 + ..., with d = (g*/A - 1) w''(P)/(2(A - 2)) (from the y^2 order of W.grad S = A S). Write V_Phi for the
  frozen packet of Phi. If d != 0, g*/A is not an integer and the singular coefficient of the first trace of V_Phi is
  nonzero (such packet data exist), the y^(2a+1) axis coefficient of the bent packet contains (d^a/a!) d_s^a d_Y
  V_Phi(s, 0), whose normalized nonsmooth part is C |s|^((g* - a(A - 2))/A) with C != 0. So the vanishing of the frozen
  limits l_j is not invariant under smooth changes of coordinates; it persists when g* > (j - 1)(A - 2)/2, also after a
  correction that is C^j near P (for example N >= j), and the case of equality needs a separate analysis. At the
  computed parameters this covers j = 3, 5, 7 (normalized exponents 2.128, 1.325, 0.522), while for j = 9 the exponent
  is -0.281, so the normalized y^9 limit of a bent packet diverges unless w''(P) = 0 or the coefficient vanishes, and
  the decomposition C_(0,j) = l_j + B_j would need a different matching there. This is a local conditional calculation,
  not the construction of an exact profile with that bend. (iii) Correction (conditional). Let Z_N be a Banach space of
  corrections embedded in C^N near both sources (N A > h), with the parity, normalization and growth conditions, and Y_N
  a Banach target such that T: Z_N -> Y_N is bounded and Y_N contains the actual residuals T Q_N Phi. If the classes of
  the T Q_N Phi span a finite-dimensional subspace of Y_N/T(Z_N) (for instance if T: Z_N -> Y_N is Fredholm), then on a
  finite-codimension subspace E_0 of any infinite-dimensional space of admissible data the functions Q_N Phi - z_Phi,
  with T z_Phi = T Q_N Phi, form an infinite-dimensional space of kernel elements of T whose nonzero members fail C^n
  near P for n A > h; their regularity at the centre is what Z_N gives. Here E_0 is the kernel of Phi -> [T Q_N Phi] in
  Y_N/T(Z_N), with z_Phi chosen linearly on E_0; Fredholmness gives correctability on a subspace of finite codimension,
  not of every datum, and every datum is correctable exactly when [T Q_N Phi] = 0 for all Phi. The one-derivative-losing
  Hoelder realization is not upper semi-Fredholm ((v) of the previous item), so the hypothesis needs a graph or
  anisotropic realization or an inverse on packet residuals; that, with the required control at the source
  (resonant Taylor jets), at the centre (compatibility conditions), at infinity (growth weights and angular data) and of
  the coupling (its leading multiplier on the packet sector is -g*, which gives D - h, so it is not a compact
  perturbation in equal-order norms), is not proved. For the P_2 conclusion in (v), fix 0 < alpha < 1 and a growth
  exponent gamma < 1 and require Q_N Phi and the corrections to lie in the corresponding admissible perturbation space
  (local C^(2,alpha) regularity, parity, tangent normalization, growth bounds, canonical velocity); this needs
  (2 + alpha) A <= h, which the referee's hypothesis h > 3A gives for every alpha < 1. (iv) Variation. Fix A, x* and the
  centre normalization. Let k = Q_N Phi - z_Phi be the corrected density perturbation and V(x) = U_1[k](x, 0), with
  V'(0) = 0 and V(x*) = V'(x*) = 0. If the required open-axis derivatives exist, the finite parts and the endpoint
  limits are differentiable in the chosen trace topology, N >= 3 and g* > A - 2, then delta l_3 = 0, so delta
  C_(0,3) = delta B_3, and with delta g = g eta, eta' = (V' - (g'/g) V)/w, eta(0) = 0 and F_3 = -a2 g' + a2' g/3,
    delta B_3 = -f.p. int_0^(x*) [delta F_3/(w H_3) - (F_3/(w H_3)) (V/w + (3 + beta) eta - beta V/w)] dx;
  this is the pairing of 6.3.1 (l) (if A varies by a, then w eta' = V' - a - (g'/g) V and delta log H_3 gains the terms
  beta a/A + delta beta log(A g/|w|), delta beta = -2a/A^2, besides the effect of the motion of the source). At a
  smooth-centre base, under the differentiated lower-jet and finite-part hypotheses, a direction of class
  C^(j + ceil(p_j)) near 0 (orders 10, 16, 22 for j = 3, 5, 7 at the computed A) has delta C_(0,j) = 0 when the
  homogeneous term is excluded by regularity and parity (p_j not an even integer), so delta B_j = -delta l_j, and delta
  B_j = 0 only when delta l_j = 0 (for j = 5, 7 this needs N >= 7 and the inequalities of (ii)); if the correction space
  allows centre defects, neither vanishing nor nonvanishing of delta B_3 on the corrected kernel is proved. (v)
  Consequence. Under (i), (iii) and the admissibility and regularity hypotheses at the end of (iii), an exact P_2 base
  smooth near P has an infinite-dimensional linearized kernel; an exact P_inf base has one in its own tangent class only
  if the correction also enforces smoothness at the centre to all orders. A nonlinear family does not follow
  (F(u) = ||u||^2), and a regular local argument that tunes C_(0,3), C_(0,5), C_(0,7) independently to zero would need
  rank three of their derivative map (or a justified sequential transversality argument); neither is proved, and a
  common zero could also occur through dependencies or a degenerate mechanism. None of this has been applied to X3,
  which is a trial and not an exact profile, and P_2 backgrounds need not be smooth near P.
- The range 1 < A <= 2 beyond 6.3.1 (m) (external referee, who derived the fifth-order condition at A = 2 below, and a
  second external referee, who gave the example with B_5 != 0 and the closed form for 1 < A < 2 below, both checked by
  the lead researcher; the residue formula, its values on the three examples and the zero of R12 for 1 < A < 2 rechecked
  by the lead researcher with separately written code; checked by the verifier symbolically and with its own code: the
  hierarchy at order 5, the residue formula computed two ways on the three examples, the exact rational example at
  A = 2, L = 2 including F_5/(w H_5), B_5 and G_5, the closed form and the zero S_A for 1 < A < 2, and B_3 at A = 1.25,
  1.5, 1.8 by two representations against the closed form, to 6e-21). At A = 2 the order j = 5 is resonant
  (p_5 = 12, H_5 = 4 g^7/w^2): the local coefficient of the smooth homogeneous solution H_5 is not constrained by
  smoothness near 0 (it equals C_(0,5) = l_5 + B_5 when this decomposition is defined), and smoothness near 0 instead
  requires that the coefficient of H_5 log|x| in G_5 vanish:
    L_5[w] = (1/120) Res_(x=0) [a2'' - (g a2/w)' + 20 a2^2/w]/g^6 = 0,   a2 = (g' - w'')/2,
  with g rebuilt from w (g/x^2 -> 1), where Res_(x=0) is the coefficient of x^(-1) in the finite Laurent expansion built
  from the centre jets (analyticity is not needed). Here the smooth third trace is G_3 = g a2/(3w), and L_5 depends on
  the centre jet of w up to order 15. The lead researcher computed the residue directly from the hierarchy of 6.3.1 (a)
  (F_5 from G_3, W1_4 and W2_5): L_5 = 0 on the pair of 6.3.1 (c) (where a2 = 0) and on the compatible data of R12 at
  A = 2, L = 2 (g* = 2, w''(P) = 1), and L_5 = -273 eps/2 for the centre germ w = -2x + eps x^15, so the two conditions
  at A = 2 are independent at the level of compatible axis data: perturbations supported near 0 change L_5 without
  changing w''(P), and perturbations supported near P that keep w(P) and w'(P) change w''(P), and hence B_3 at the pair
  of 6.3.1 (c) (g* = 4), without changing the centre jet; this does not prove independence on exact profiles. Both hold
  on the exact local pair of 6.3.1 (c) (g* = 4, w''(P) = 0) and on the compatible data of R12 with L = 2 (axis data
  only, not a two-dimensional solution). On these data (A = 2, L = 2)
    F_5/(w H_5) = 5/(768 x^5) - 103/(960 x^7) + 143/(240 x^9) - 13/(12 x^11),
  so B_5 = -f.p. int_0^2 F_5/(w H_5) dx = 11/1474560 != 0, while the source-selected fifth trace
    G_5 = x^2 (11 x^6 + 88 x^4 - 1872 x^2 + 9984)/(90 (x^2 + 4)^5)
  solves the fifth axis equation, is smooth at 0 and bounded at P, so l_5 = 0: at this resonance a smooth fifth trace
  does not require B_5 = 0. For 1 < A < 2 the compatible data of R12 have B_3 = 0 at
  L^2 = S_A = 6A(4A - 3)/(8A - 1) < 2A, and there Q - P(m) changes sign (lead check by the finite part of 6.3.1 (a) at
  A = 1.25, 1.5, 1.8: the scaled B_3 is linear in A/L^2 to 15 digits and vanishes at S_A to 1e-28). In closed form, with
  beta = 2/A in (1, 2), B_3 = C_A L^(-4-beta) (1 - S_A/L^2), C_A = (beta - 1)(J_5 + J_3)/(3A) > 0, J_n = int_0^1 u^n
  (1/u - u)^(beta - 2) (1 + u^(-2)) du = (n/(n + beta - 1)) B((n - beta + 1)/2, beta - 1) (B the Euler beta function),
  J_5/J_3 = 5(4 - beta)/(3(beta + 4)), and S_A - 2A = 8A(A - 2)/(8A - 1) (the lead researcher checked the recurrence and
  S_A by hand and J_3, J_5 by quadrature at beta = 1.2, 1.5, 1.8). So on the whole range 1 < A <= 2 these are necessary
  conditions that compatible axis data satisfy, and at A = 2 also an exact local solution; they do not decide existence,
  and an exclusion would have to use a further property of admissible profiles, such as the canonical velocity law, the
  growth bounds or the two-dimensional transport. Under the additional C^(4,alpha) regularity of 6.3.1 (h)
  (Higher odd orders), or under its summable fourth-derivative hypothesis, the data of R12 at L^2 = S_A fail the
  fifth-order condition B_5(c_l, w) = 0 for every 1 < A < 2 (6.5).
- Q1 (isolated profile or family). Undecided. The singular-value study of the discretized linearization at X3 does not
  meet its preconditions (stationary base states, several domains), and by 6.3.1 (d) such a study cannot decide the
  question by itself; the singular values of that study in the weighted norm fixed for it beforehand were computed with
  inverted column weights (numerical researcher's erratum), and the reading undecided does not depend on them. A
  formulation that builds in the transport structure at P (6.3.1 (e)) has been solved on a grid of 120 x 48 nodes only
  down to a 2-norm residual of 2.1e-4, where every solver used stalls; no converged solution is available. (i) Jacobians
  assembled with inverses of the elliptic equation coarser than that of the residual had singular values down to about
  3e-7 that the residual does not reproduce (an earlier verification, using its own inverse and the pointwise transport
  residual R = W.grad rho - rho on an off-node grid, found raw responses max |delta R| of 0.096 to 12.4 per unit
  physical-node step along the eight softest directions of the first of them, not normalized like singular values);
  those values are withdrawn. (ii) After a re-solve of a discrete system in which the switch of the orbit step near P is
  smooth (the abrupt switch made the residual only piecewise smooth and spoiled difference quotients), the stalled state
  has residual 2.109e-4 (c_l = 5.574693, x* = 8.577407; 2.108e-4 after a re-solve at half the orbit step, a result of
  the numerical researcher not recomputed independently). Central differences at step 1e-4 on a 24-dimensional candidate
  subspace give Ritz values of the actions, per unit node vector, 1.72e-6, 2.93e-6, 2.87e-5 and 9.29e-5, and six more
  between 1.9e-4 and 1.13e-3 (numerical researcher; the saved matrix spectra and these Ritz values recomputed by the
  verifier from the saved data). They are measured finite-difference quantities on this discretization; without an error
  bound for the actions they are not certified upper bounds for singular values of the Jacobian, and an earlier
  comparison of them with singular values of the scaled matrix mixed two normalizations (verifier). The residual lies
  almost entirely in the image of these directions (its projection on the span of the 24 measured actions has norm
  2.06e-4, verifier); this linear statement concerns the measured subspace only and does not explain the stall, nor show
  that the residual can be removed only along these directions, since other directions may have overlapping images and
  the problem is nonlinear (verifier, with an explicit two-dimensional example). At a selected interior point the
  physical transport actions delta R/N_f of the six softest directions, with the denominator N_f = |rho| + sum_i |W_i
  d_i rho| of 4.4 frozen at the base field, are 1.7e-4 to 4.5e-3, against 0.151 for a calibration direction (verifier,
  with its own reconstruction of the fields and its own inverse), so their measured physical actions there are nonzero;
  no error bound for these actions is supplied, so nonzero actions for the continuum problem are not certified.
  [Corrected 2026-10-20: an earlier version concluded from these measured values that the directions are not physical
  null vectors.] (iii) The stalled state is not a solution of the continuum problem at the accuracy required: the
  verifier's own evaluation gives |R|/N_f = 3.6e-3 and 2.3e-3 at two tested points, stable under angular and radial
  refinement of its inverse and under an outer radius of 1e30 (and an off-node residual of 4.0e-3 in N_f, 3.8e-3 in N_v,
  at the stalled state of the earlier discrete system), and its finite interpolant fails the necessary fifth-order
  smoothness condition at the centre (angular contrast +0.0073, and +0.0072 after the re-solve at half the orbit step).
  In ball arithmetic on the exact interpolant through the saved binary nodal values at ideal Chebyshev-Lobatto (radial)
  and Gauss (angular) nodes, with the saved binary parameters and the exact value k = 1/c_l (verifier), the centre limit
  of G_5 is 290.466 (289.278 after the re-solve), not 0, so the interpolant is not C^5 at the centre, and with rho = x^2
  y + r^5 P(theta) + O(r^7) there, P with sine coefficients p_m, the coefficient of r^5 sin 7theta in the transport
  residual is (5 c_l - 1) p_7 - 7 c p_9 for every divergence-free velocity U = (-c x, c y) + U_3 + o(r^3) with the
  parities, U_3 a cubic polynomial (as for every velocity of class C^3 at the centre), which is 0.011784 (0.011644) at
  the cubic balance c = 3 c_l - 1, so the interpolant solves the transport equation near the centre with no such
  velocity (coefficient identity checked by the lead researcher). These are defects of the representation and do not
  exclude smooth limits. So the discrete system at that resolution is not solved below 2.1e-4, and whether its small
  actions reflect a near-kernel of the continuum problem or softness induced by the discretization is not decided: no
  verified result across resolutions and domains decides it for the present formulation, and such a study alone would
  not identify a continuum kernel without controlled errors of the actions and a stability and convergence argument;
  small actions of one or several directions would in any case be compatible with a family, with an isolated solution
  and with no solution (6.3.1 (d)). (iv) Variations of the discretization (verifier, with its own reconstruction of the
  saved fields, its own full-plane inverse and exact ball arithmetic for the centre tests): a state of the same
  formulation computed on a grid of 96 x 40 nodes (c_l = 5.576238) has |R|/N_f = 0.0036 and 0.0055 at the two test
  points of radius 10, and its interpolant fails the same centre tests; its Ritz values measured in the same way on 24
  directions are 4.24e-6, 6.05e-6, 4.95e-5, 2.00e-4 and six more between 3.9e-4 and 2.9e-3, larger than the ten smallest
  of the 120 x 48 state by factors between 1.72 and 2.54 (numerical researcher; recomputed by the verifier from the
  stored action arrays; without an error bound for the actions this does not show that refinement softens a near-kernel
  of the continuum problem); the 120 x 48 states re-solved at half the orbit step and with 720 angular nodes in the
  inverse have |R|/N_f = 0.0036 and 0.0024 at the two test points, and both fail the centre tests; for the 120 x 48
  formulation, moving the residual row that represents infinity from radius 1e10 to 1e8 (with the state solved again)
  changes the two smallest measured Ritz values by factors 1.14 and 1.42; the spans of the two softest measured
  directions nearly agree (minimum principal cosine 0.99997), while the whole 24-dimensional measured subspaces have
  minimum principal cosine 0.018; between the 96 x 40 and 120 x 48 states the six softest matrix directions, compared
  using the interpolated nodal relative changes delta b/b on a common polar grid, have overlaps 0.993, 0.994, 0.999,
  0.603, 0.978 and 0.945 by index on r < 200, and their spans have smallest principal cosine 0.952 there and 0.933 on
  the whole window 0.02 <= r <= 2e4 (0.942 for the corresponding physical density variations, which include the
  variation of c_l); states solved with c_l fixed at offsets +-0.001 and +-0.01 have |R|/N_f between 0.0025 and 0.0046
  at the same points; and two reduced Gauss-Newton steps of the verifier on the physical residual at sampled points
  reduce it at the fitted points (for instance from 0.0043 to 0.00096 in norm at eight points) while at the full second
  trial step its norm at 18 fresh points grows from 0.0010 to 0.0020; no tested step meets the standard, and the centre
  tests still fail. With the radial scale R_c of the representation halved (R_c = 4 instead of 8; the radial nodes are
  Chebyshev-Lobatto nodes in q = 1 - (1 + r^2/R_c^2)^(-(1 - k)/2), k = 1/c_l, and the density carries the far-field
  factor (1 + r^2/R_c^2)^((k - 3)/2), so R_c changes the representation and the placement of the nodes but not the
  domain, which is the whole plane), the computed state of the 96 x 40 formulation has a 2-norm collocation residual of
  1.9e-3, about five times that at R_c = 8 (c_l = 5.574690; numerical researcher). The verifier's own reconstruction and
  inverse give the source at x* = 8.577249, the self-consistency defect 3 c_l - 1 - psi_xy(0) = 8.6e-7, a maximum of the
  sampled transport residual |R|/N_f of 0.0038 over 58 fixed points, against 0.0055 for the R_c = 8 state at the same
  resolution, and |R|/N_f = 4.8e-7 and 2.4e-4 at (x*, 0.1) and (x*, 1); exact interval tests at the centre show that
  this interpolant is not smooth there and, as in (iii), solves the transport equation near the centre with no velocity
  of class C^3 there, which does not exclude a smooth limit of other trials. Its four smallest Ritz values measured as
  above are 3.7e-6, 6.3e-6, 8.1e-5 and 1.8e-4 (numerical researcher, not recomputed independently). This state does not
  meet the residual standard and does not establish convergence in R_c. With R_c doubled instead (R_c = 16), the
  computed state of the 96 x 40 formulation has a 2-norm collocation residual of 3.4e-4, against 3.6e-4 at R_c = 8, and
  c_l = 5.583653, which differs from the values at R_c = 8 and R_c = 4 by 7.4e-3 and 9.0e-3 (numerical researcher). The
  verifier's own reconstruction and inverse give the source at x* = 8.589582, the self-consistency defect
  3 c_l - 1 - psi_xy(0) = -8.2e-7, a maximum of |R|/N_f of 0.0089 over the same 58 points, against 0.0038 at R_c = 4 and
  0.0055 at R_c = 8, and |R|/N_f = 8.4e-7 and 3.0e-4 at (x*, 0.1) and (x*, 1); the same exact interval tests at the
  centre exclude smoothness and exact transport for this interpolant, again without excluding a smooth limit of other
  trials. Its four smallest Ritz values measured as above are 2.7e-5, 3.5e-5, 7.2e-5 and 9.3e-4, larger than those at
  R_c = 8 (4.2e-6, 6.1e-6, 5.0e-5 and 2.0e-4) by factors between 1.4 and 6.3 (computed from the unrounded values;
  numerical researcher, not recomputed independently). So the maximum sampled residual increases with R_c (0.0038,
  0.0055 and 0.0089 at R_c = 4, 8 and 16) and the smallest measured Ritz values change with R_c, while the collocation
  residual at R_c = 16 is at the same order of magnitude as at R_c = 8; this state does not meet the residual standard
  either, and the three values of R_c do not establish convergence in R_c. On a third, coarser grid of the same
  formulation at R_c = 8, of 72 x 30 nodes, the computed state has a 2-norm collocation residual of 7.6e-4, against
  3.6e-4 and 2.1e-4 on the 96 x 40 and 120 x 48 grids, and c_l = 5.562978, which differs from the value on the 96 x 40
  grid by 1.3e-2; its solve stalled there, and a second pass with a refreshed Jacobian on the soft directions stalled at
  nearly the same value, so this residual may be limited by the solver rather than by the grid (numerical researcher).
  The verifier's own reconstruction and inverse give the source at x* = 8.561000, the self-consistency defect
  3 c_l - 1 - psi_xy(0) = +1.3e-6 (two separately bounded evaluations of the centre integral), a maximum of |R|/N_f of
  0.0059 over the same 58 points, against 0.0055 on the 96 x 40 grid, and |R|/N_f = 7.1e-6 and 1.5e-4 at (x*, 0.1) and
  (x*, 1); the same exact interval tests at the centre exclude smoothness (this interpolant is not C^5 there) and exact
  transport for this interpolant, again without excluding a smooth limit of other trials. Its ten smallest Ritz values
  measured as above are 1.31e-5, 2.88e-5, 1.84e-4, 4.75e-4 and six more between 1.1e-3 and 1.5e-2, larger than those on
  the 96 x 40 grid by factors between 2.38 and 5.29 (computed from the unrounded values; numerical researcher, not
  recomputed independently). So on the grids 72 x 30, 96 x 40 and 120 x 48 the collocation residual and the smallest
  measured Ritz values decrease with refinement, while the maximum sampled residual is about the same on the first two;
  without error bounds for the actions this does not show that refinement softens a near-kernel of the continuum
  problem, this state does not meet the residual standard either, and the three grids do not establish convergence in
  the resolution. On a fourth grid of the same formulation at R_c = 8, of 84 x 35 nodes, the computed state has a 2-norm
  collocation residual of 5.1e-4, between those on the 72 x 30 and 96 x 40 grids, and c_l = 5.600157, larger than on the
  72 x 30, 96 x 40 and 120 x 48 grids by 3.7e-2, 2.4e-2 and 2.5e-2 (numerical researcher). The verifier's own
  reconstruction and inverse give the source at x* = 8.615859, the self-consistency defect
  3 c_l - 1 - psi_xy(0) = +5.2e-7 (two separately bounded evaluations of the centre integral), a maximum of |R|/N_f of
  0.0068 over the same 58 points, against 0.0059 and 0.0055 on the 72 x 30 and 96 x 40 grids, and |R|/N_f = 1.1e-5 and
  2.9e-4 at (x*, 0.1) and (x*, 1); the same exact interval tests at the centre exclude smoothness (this interpolant is
  not C^5 there) and exact transport for this interpolant, again without excluding a smooth limit of other trials. Its
  ten smallest Ritz values measured as above are 1.20e-5, 1.41e-5, 4.10e-4, 5.72e-4 and six more between 8.9e-4 and
  1.3e-2; the third and fourth are larger than on the 72 x 30 grid and the other eight are smaller, and all ten are
  larger than on the 96 x 40 grid by factors between 1.6 and 8.3 (computed from the unrounded values; numerical
  researcher; the verifier recomputed these values and ratios from the stored data, without recomputing the actions). So
  over the four grids the collocation residual decreases with refinement, while c_l and the smallest measured Ritz
  values are not monotone in the resolution, and the maximum sampled residual is larger on the 84 x 35 grid than on the
  72 x 30 and 96 x 40 grids; this state does not meet the residual standard either. None of these is a convergence
  result. Conditionally on a correction theorem in specified spaces and on the admissibility hypotheses stated there, an
  exact P_2 base smooth near P would have an infinite-dimensional linearized kernel (the item on the correction of
  packets above); that would still not decide the nonlinear question. On far-field data: every nonzero exact admissible
  profile has a nonzero homogeneous trace F, with rho(r theta) = r^(1/c_l) F(theta) + O(r^(1/c_l + gamma - 1)) uniformly
  in theta, where gamma is an exponent from (A3) (6.3.1 (q)); this does not determine whether F can be prescribed or
  whether it varies along a family of profiles.
- Q2 (B_3 along a family). No verified family of solutions is available. On the stored fixed-c_l fits of the first
  investigation B_3 is about 0.30, with no resolved dependence on c_l (6.3.2 (d)); these are trial values. On a left
  cone at P the coupled equations leave any finite number of source amplitudes free (6.3.1 (r)); these cone solutions
  are not profiles, do not reach the centre and give no family of P_inf.
- Q4 (other branches). Not studied numerically. For A > 2, a profile that is C^infinity near 0 and has a singular mode
  at the source (l_3 != 0, which by 6.3.1 (h) requires that the profile fails the cone form of the Hoelder hypothesis on
  rho and W at P, in particular that rho is not C^(2,alpha) near P for any alpha > 1 - 2/A) is not excluded by anything
  known; on a left cone at P the coupled equations do have exact analytic solutions with l_3 != 0 that are of class
  C^(2,1-2/A) up to P on the cone (6.3.1 (r), m = 3), and whether such a solution extends to a neighbourhood of P, or to
  a profile, is open; for 1 < A <= 2 there is none in P_inf (6.3.1 (m)). An individual numerical trial with bounded
  third trace at P has l_3 = 0
  and is not such a profile; this does not exclude that smooth trials converge to one. A count of free parameters from
  frozen singular modes at P is not available (external referee): a cut-off frozen mode is not a kernel element of the
  full linearization, no Fredholm setting is known in the needed spaces, a bordered operator gains a kernel dimension
  only if the added direction is in the range, and a linear kernel element need not give a nonlinear family.
- Q3 (analytic relations and obstructions) and NO_inf. The analytic partial results are the hierarchy and obstruction
  functionals of 6.3.1 (a), the local compatibility of 6.3.1 (c), the endpoint condition and the sign criterion of 6.3.1
  (h) and (k), and the first variation of 6.3.1 (l); no global incompatibility is established. No global mechanism is
  known that would exclude C_0 = l_3 + B_3(c_l, w) = 0 for every profile of the class, or
  that would first establish the existence of l_3 and l_3 = 0 in the class considered. By 6.3.1 (c) such a mechanism
  cannot rest only on the local conditions that the exact local pair satisfies; it must use a further property of
  admissible profiles, such as the growth bounds or the canonical velocity law. A local exclusion near X3 along these
  lines needs a certified nonzero B_3 at a compatible reference, a stability estimate in a weighted trace norm (that of
  6.3.1 (i), or the weaker norm N of 6.3.1 (o)), control of l_3 for the nearby exact profiles (for instance l_3 = 0
  under the Hoelder hypothesis of 6.3.1 (h)), and a bound placing the trace of an exact profile in the resulting ball;
  control of the Taylor coefficients at 0 alone does not suffice. The first two are available at the computed A
  (6.3.1 (o)), the third under the Hoelder or cone hypothesis of 6.3.1 (h); the last is not. For A > 2 and profiles with
  the Hoelder hypothesis at P, one sufficient route is to prove that the ordinary integral of 6.3.1 (k) is nonzero, for
  instance through (H_-) or the weaker tests above. No such argument for the coupled profiles is known. Endpoint signs
  at P and positivity of rho (at first order and through the kernel of Q) are shown not to give
  the sign; this rules out the corresponding unrestricted positive-kernel arguments, not a sign mechanism that uses the
  full coupled constraints. Nonconstant monotonicity of Q - P(m) in x would suffice (test (iv)), but it is not
  established for profiles, it fails on compatible axis data with L^2 < 3A, and the sampled values on the stored trial
  traces are not monotone. [Corrected 2026-10-20: an earlier version said that monotonicity of Q - P(m) is shown not to
  suffice.] One sufficient route that is missing is a consequence of the coupled equation that makes one such weighted
  integral strictly negative (or merely nonzero), or, for a local statement, a bound placing the trace of an exact
  profile in one of the balls of 6.3.1 (o).
- B_5 and B_7 (verifier). The formulas are confirmed symbolically. Section 6.3.2 (a) gives a numerical reference value
  of B_5 on analytic axis data at the zero of B_3; its strict negative sign is proved in 6.5. The finite-part functional
  B_5 of 6.3.1 (a) is defined as stated only when G_3 has a power expansion at 0, which on the nonresonant branch with
  l_3 = 0 means B_3 = 0 (otherwise the non-analytic term B_3 H_3 enters F_5 at 0 and the finite part has to remove it as
  well), and B_7 likewise needs a power expansion of G_5, which on the nonresonant branch with l_3 = l_5 = 0 means
  B_3 = B_5 = 0; in general these conditions concern C_(0,i) = l_i + B_i, and at resonant orders they are logarithmic
  compatibility conditions that may allow a nonzero smooth homogeneous coefficient (at A = 2, B_5 != 0 with a smooth
  G_5, in the item on the range 1 < A <= 2 above; qualification added after an external audit); at the zero L* of B_3 in
  6.3.2 (a), where B_5 is negative (exactly, 6.5) and about -7.69e-5 natural units (numerical), the analogous series
  reading of B_7 is not constant in x, as expected. So near X3 (nonresonant, with l_3 = 0 for the trial) B_5 and B_7 are
  needed only at a candidate with B_3 = 0. No numerical profile candidate with B_3 = 0 meeting the profile tests has
  been produced, and no estimator of B_5 or B_7 for sampled trial data has been built. On the R12 axis data at
  A = 2, L = 2 the source-selected seventh coefficient is exactly B_7(c_l, w) = -23/29059430400 (natural units
  -23/14189175), which with the third- and fifth-order conditions excludes the whole R12 family under C^(6,alpha)
  regularity at P (6.5); this restricted exclusion is not NO_inf.

### 6.5 The exact remaining gap
Status at the report cutoff (2026-10-21T00:00:37Z): neither endpoint is reached. The gap is the following; items marked
as heuristic are labelled readings from 6.4 and are not used as results.
- Toward YES_inf. What is needed is a candidate at the full P_2 standard with B_3 = 0 (both estimators) and B_5, B_7
  zero within their measured accuracies (6.1). For a candidate with bounded third trace at P (l_3 = 0), in particular
  for any candidate built from functions smooth at P, this is the general third-jet condition C_0 = l_3 + B_3 = 0, and
  at the nonresonant orders 5 and 7 the tests agree with the smooth-centre conditions when l_5 = l_7 = 0. A generalized
  test allowing nonzero source limits would first have to justify the endpoint limits, the finite parts and the
  lower-jet expansions, then measure C_(0,j) = l_j + B_j for j = 3, 5, 7 with assessed accuracies, and at a resonant
  order test the compatibility coefficient instead; a candidate with B_3 = -l_3 != 0 would not pass the literal test
  B_3 = 0, and an endpoint claimed under the generalized test would have to say so. The only computed candidate, X3, is
  built from functions smooth at P, so l_3 = 0 for the trial; its trial-data finite-part estimators give B_3 = 0.296 to
  0.323 natural units (0.31 +- 0.015, the observed spread over the numerical choices of 6.2, not a certified error
  bound), and its own homogeneous coefficient is 0.046. These fail the smooth-centre test, so X3 is a P_2 candidate and
  not a P_inf candidate; they do not certify a value of B_3 for a nearby exact profile (6.3.2 (c)). Q1: no verified
  numerical continuation through X3 is available, and Q1 remains open (6.4): a sufficiently converged base state, a
  specified function-space formulation, and stable measurements of the kernel or near-kernel dimension and of the
  conditioning across resolutions and domains are missing. Q2: no continuation tracking c_l, B_3, B_5 has been obtained;
  the stored trial fits give B_3 about 0.30 without a resolved dependence on c_l (6.3.2 (d)); no numerical profile
  candidate with B_3 = 0 meeting the profile tests has been produced, so the higher-jet tests have not been carried out
  on such a candidate (the compatible axis data of 6.3.2 (a) with B_3 = 0 are calibration examples, not profile
  candidates). Frozen model (6.4, the frozen kernel at P): an external referee constructs an infinite-dimensional space
  of solutions of the frozen equation at P that are smooth off P, of class C^(2,alpha) at P for every alpha < 1 at the
  computed parameters, and have l_j = 0 for every odd j >= 3; the verifier checked concrete packets and the identities
  and later proved independently the regularity class with its sharpness (for nonzero packets), the smoothness off P,
  the expansion to every finite order with a C^N remainder for every N, and the vanishing of the limits l_j of every odd
  order (these proofs audited by a further external referee). In the conditional local calculation of 6.4 (the
  correction of packets: A > 2, a background smooth near P, the flow nonresonance condition of 6.4 (A not an even
  integer, or the coefficient that would require a term Y^A log|Y| vanishes), and the referee's packet construction; the
  nonzero singular-trace asymptotics there require in addition that g*/A, about 2.931 at the computed parameters, is not
  an integer and that the singular coefficient does not vanish), bending along the weak characteristic preserves l_j = 0
  at the computed parameters for j = 3, 5, 7, also after a correction that is C^j near P, while for j = 9 a nonzero bend
  together with a nonzero singular coefficient of the first trace makes the normalized ninth trace diverge; this is not
  the construction of an exact profile. Whether cut-off versions correct to solutions of the full problem is open (for
  A > 2 and a background smooth near P without flow resonance, an external referee gives linear correctability on a
  subspace of finite codimension of admissible packet data, provided its construction of the correction operator, the
  stated regularity and admissibility conditions and a finite-obstruction hypothesis hold; that construction is not
  checked by the verifier and that hypothesis is not proved; 6.4), and, in the setting of 6.4 (the frozen kernel at P,
  (v)), the full linearization is not upper semi-Fredholm from {v in C^(2,sigma): supp v in K} to C^(1,sigma)(closure of
  Omega), where 0 < sigma < 1, rho and W are C^(2,sigma) near the closure of a bounded domain Omega, W(P) = 0, and K is
  a fixed compact subset of Omega containing a neighbourhood of P (for inputs with the parity of the problem, also of
  the points obtained from P by that parity). At the computed parameters smooth functions approximate their cut-offs in
  C^(2,alpha), although no finite combination of functions smooth at P represents their singular germs exactly, and
  approximation by a particular sequence of trial spaces needs its own justification. So isolation of a converged
  discrete state would not decide Q1 by itself; neither the isolation of a discrete solution near X3 nor a continuum
  stability and convergence theorem has been established. Heuristic: if they did correct to exact solutions and a
  nonlinear existence and parametrization theorem held, the solutions of P_2 near X3 would contain an
  infinite-dimensional family on which B_3 need not be constant (its members need not be smooth near 0; a member smooth
  near 0 with l_3 = 0 has B_3 = 0), and a search for YES_inf would then need a discretization that resolves the
  anisotropic scales at P (S comparable to |Y|^A about the possibly curved weak characteristic S = s + d y^2 + ...,
  A = 10.15). Even on such a family, a regular argument tuning C_(0,3), C_(0,5), C_(0,7) independently to zero would
  need rank three of the derivative of the obstruction map, or a justified sequential transversality argument; neither
  is proved, and a common zero could also occur through dependencies or a degenerate mechanism.
- Toward NO_inf, for profiles that satisfy the Hoelder hypothesis at P (or its cone form). Smoothness near 0 forces
  B_3(c_l, w) = 0 (6.3.1 (h)), and for A > 2, under the trace hypotheses of 6.3.1 (k) (which the full Hoelder hypothesis
  supplies; for the cone form they are an additional assumption), B_3 is a negative multiple of a convergent weighted
  integral of R = Q - P(m) - Q(x*) over the axis data (6.3.1 (k)). One sufficient route is to derive, for the coupled
  profiles under consideration (velocity law, transport, growth, and positivity under (Hmin) of R9 unless positivity is
  proved otherwise), a strict sign or merely the nonvanishing of that integral, for instance through (H_-) or one of the
  weaker tests (i) to (iii) of 6.4; no such argument is known. Other routes (an incompatibility among the higher
  obstructions, or a direct argument on the coupled equation) are not excluded; see the item on what NO_inf has to
  exclude. Endpoint signs at P, first-order positivity of rho and the kernel form of Q are shown not to give the sign
  (6.3.1 (l), 6.4); this rules out the corresponding unrestricted positive-kernel arguments, not a sign mechanism that
  uses the full coupled constraints. Compatible axis data with B_3 = 0 exist (6.3.2 (a)), so the listed axis
  compatibility identities alone do not force nonvanishing: an exclusion needs an additional restriction on admissible
  profiles, which may be expressed in axis data (as (H_-) is) but must then be derived for the coupled profiles or
  stated as an explicit hypothesis. The conditional nonexistence under (H_-) (6.3.1 (k)) is proved and verified; under
  the reporting convention of 6.1 it is not counted as NO_inf.
- Toward NO_inf, for general profiles of P_inf with A > 2. To use the third-jet identity one must in addition justify
  the trace and finite-part limits and establish l_3 + B_3 != 0 (when the limit l_3 exists, smoothness near 0 gives
  B_3 = -l_3), or find another exclusion argument; (C1) is proved (6.3.1 (f)) and smoothness near 0 gives the origin
  expansions, so what is missing is control of the source limit and of the source integral. This is open. An exclusion
  through the third jet must rule out l_3 + B_3 = 0, or handle profiles for which the decomposition is not available.
  The frozen examples of 6.3.1 (g), within their stated parameter ranges and in particular at the computed parameters,
  show that local C^(2,alpha) regularity below the threshold (alpha <= 1 - 2/A, 0.803 on the computed branch) does not
  force l_3 = 0 and that one-sided smoothness does not make l_3 finite; they are not admissible global profiles.
- Toward NO_inf for 1 < A <= 2 (1 < c_l <= 3/2; 6.3.1 (m), verified; the fifth-order condition at A = 2 and the zero of
  R12 from 6.4, rechecked by the lead researcher and checked by the verifier). There the Hoelder hypothesis of 6.3.1 (h)
  is part of the class, so every profile of P_inf has l_3 = 0 and B_3(c_l, w) = 0; at A = 2 this is w''(P)(g* - 2) = 0,
  and smoothness at 0 adds the logarithmic condition L_5[w] = 0 of the resonant order j = 5. These conditions are met by
  compatible axis data (R12 for 1 < A < 2; at A = 2 the data of R12 with L = 2, and the exact local pair of 6.3.1 (c)).
  What is missing is an exclusion that uses the canonical velocity law, the growth bounds or the two-dimensional
  transport, or a further necessary condition that these data fail. One such condition is available under more
  regularity: for 1 < A < 2 and a profile that is in addition C^(4,alpha) near P for some 0 < alpha < 1, 6.3.1 (h)
  (Higher odd orders) gives l_5 = 0 and B_5(c_l, w) = 0. This condition fails on the compatible data of R12 at
  L^2 = S_A, where B_3 = 0, for every 1 < A < 2 (external referee; audited by a second external referee; checked by the
  lead researcher and by the verifier). There the source-selected third trace is G_3 = 10 A u^2/((8A - 1)(1 + u^2)^3),
  u = x/L, which is bounded at P, so l_3 = 0, and, with the normalizations g/x^2 -> 1 and H_5/x^(10 + 4/A) -> 1 at 0,
    B_5(c_l, w) = P(A) B(-4 - 2/A, 4/A)/(15 A (2A - 1)(3A - 2)(4A - 3)(8A - 1) L^(10 + 4/A)),
    P(A) = 1248 A^4 - 548 A^3 + 297 A^2 - 178 A + 84,
  with B the meromorphically continued Euler beta function, which on 1 < A < 2 agrees with the finite part of 6.3.1 (a).
  P(1 + z) has positive coefficients and B(-4 - 2/A, 4/A) < 0 on 1 < A < 2 (from the signs of the gamma factors), so
  B_5(c_l, w) < 0 on the whole range. At A = 5/4, 3/2, 9/5 the values are -0.0018706771467264822603,
  -0.00012758243855414775476 and -0.000018445184402991103820 in this normalization (-0.019611, -0.0062469 and -0.0027733
  in natural units B_5 x*^(p_5 - 4), x* = L); the lead researcher's finite part from the hierarchy of 6.3.1 (a)
  (separately written code: series on [0, L/4], quadrature on [L/4, L]) agrees to the 20 digits shown, and the
  verifier's own series code agrees with the closed form to 3e-33 at nine values of A in (1, 4). As A -> 1 from above
  the closed form tends to -(43/300)(7/6)^7 = -0.42167 (natural units -2107/10800). So, by 6.3.1 (h), Higher odd orders
  with j = 5, these data are not the axis data of a profile of P_inf that is in addition C^(4,alpha) near P for some
  0 < alpha < 1. The same holds for a profile that satisfies instead the summable fourth-derivative hypothesis of Fifth
  order under summable fourth-derivative growth in 6.3.1 (h), which gives l_5 = 0 without C^4 regularity. With f = rho,
  r = x* - x and the smoothness to the left of P assumed in 6.3.1 (h), the curl identity shows that this summability
  hypothesis follows from the additional bounds |D^4 f| <= C r^(-p) and |D^5 f| <= C r^(-P_0)
  on a larger left cone at P, with 0 <= p < 4/A - 1 and P_0 finite, provided the class exponent satisfies
  alpha > 3 - 4/A (Fifth order under a density bound in 6.3.1 (h)); in particular this applies for every 1 < A <= 4/3
  and every 0 < alpha < 1. The j = 5 power-cutoff transport examples of 6.3.1 (j), in this range of A, satisfy these
  density bounds; their violation of the curl identity is consistent with the velocity estimate of that bullet, which
  for a class exponent alpha > 3 - 4/A excludes their growth of fourth derivatives. For a profile of P_inf with these
  axis data and only the regularity of the class, G_3 and F_5 are smooth up to P and F_5/(w H_5) = O((x* - x)^(4/A - 1))
  is integrable there, so the fifth normalized limit l_5 exists, and smoothness at 0 (p_5 = 10 + 4/A lies in (12, 14)
  and is not an even integer) requires l_5 = -B_5(c_l, w) > 0. Under the regularity of the class alone, the present
  arguments do not rule out this cancellation, and they do not show that a profile realizing it exists. The frozen
  examples of 6.3.1 (j) show that the regularity of the class and smoothness near the axis to the left of P do not force
  the fifth-order source condition at three specific parameter pairs, one of them A = 7/4 with alpha = 1/2; for
  1 < A <= 4/3 every class exponent meets the fifth-order threshold of the frozen theorem of 6.3.1 (j), but the frozen
  model with a smooth forcing is not the nonlinear problem, so l_5 = 0 is not established for every profile with only
  the regularity of the class in any part of this range. Obstruction to applying the frozen theorem (external referee;
  audited by a second external referee; checked by the lead researcher and by the verifier): writing f = g* y + v and
  W = (A s, y) + V, the localization of the velocity law gives V = U[v] + S with S smooth near P, and the exact equation
  L_g v = -g* S_2 - V.grad v. The class gives this right side C^(1,alpha) regularity (product estimate), but not the
  smooth forcing that the frozen theorem of 6.3.1 (j) requires, and the negative threshold 3 - 4/A for 1 < A < 4/3 does
  not supply that hypothesis. The transport examples of 6.3.1 (j) show that the transport equation, the constant
  divergence, the parities and the source structure, C^3 regularity at P and smoothness on the punctured neighbourhood
  do not imply l_5 = 0; these examples already fail the curl identity, and what remains unproved is that the coupled
  equations force l_5 = 0 for every profile with only the regularity of the class; the density-bound criterion of 6.3.1
  (h) proves this only under explicit additional hypotheses, which have not been established for every profile. What the
  local source structure and the velocity law do and do not control at P, including a sufficient axis bound for l_5 = 0,
  is recorded in 6.3.1 (j) (Local source structure). The frozen examples do not realize the R12 source data (at its zero
  of B_3, R12 has g* = 3A(4A - 3)/(8A - 1), which is 21/13 at A = 7/4, while the example there has g* = 27/8), and they
  do not settle the question for profiles. As A -> 2 from below the closed form tends to -11/1474560, while the finite
  part at A = 2, L = 2 is +11/1474560 (6.4). The difference, exactly -11/737280, is the contribution of the power that
  becomes logarithmically resonant at A = 2: its coefficient tends to zero, but its contribution to the finite part does
  not; at A = 2 that power has coefficient zero, and the condition for smoothness there is the logarithmic condition
  L_5[w] = 0, not B_5 = 0. Along other directions to (A, L) = (2, 2) the nonresonant B_5 has other limits (verifier), so
  the value -11/1474560 is specific to the curve L^2 = S_A. The same closed form holds for every A > 2 (verifier;
  audited by an external referee; checked by the lead researcher: the derivation uses no upper bound on A, and for
  A > 1, A != 2, the first beta argument -4 - 2/A lies in (-6, -4) and is an integer only at A = 2, so the finite part
  is the continued beta function; the verifier's series values agree with the closed form to 3e-33 at A = 2.5, 3, 3.5
  and 3.9). With z = 2/A in (0, 2), z != 1, the gamma recurrence gives B(-4 - z, 2z) = -Gamma(2 - z) Gamma(2z)
  (2 - z)(3 - z)(4 - z)/(Gamma(1 + z) (1 + z)(2 + z)(3 + z)(4 + z)), in which every gamma argument and every displayed
  factor is positive; so B(-4 - 2/A, 4/A) < 0 and B_5(c_l, w) < 0 for every A > 1 with A != 2, by this formula and not
  by numerical agreement (at A = 10.150725 the natural value is the -7.6894e-5 of 6.3.2 (a)). For 2 < A < 4 the
  C^(4,alpha) hypothesis also gives l_3 = 0 (6.3.1 (h)), so these data fail the same necessary condition there; for
  A >= 4 the same holds for profiles that are C^(4,alpha) near P with alpha > 1 - 4/A (Higher odd orders in 6.3.1 (h)).
  For every A > 2, outside the range of this item, these data are also excluded for profiles that satisfy instead the
  summable fourth-derivative hypothesis of 6.3.1 (h) (lead researcher; checked by the verifier; audited by an external
  referee): for A >= 2 that hypothesis bounds the third derivatives on a left cone at P, so l_3 = 0 and the third trace
  is the displayed G_3, and it gives l_5 = 0; since p_5 = 10 + 4/A lies in (10, 12) and is not an even integer,
  smoothness at 0 would require B_5(c_l, w) = 0, against B_5(c_l, w) < 0. At A = 2, where p_5 = 12 is resonant, B_5 is
  not the obstruction and under the summable hypothesis no such exclusion follows. Under a stronger hypothesis at P the
  seventh coefficient excludes this case, and with it the whole family (verifier, two exact implementations; checked by
  the lead researcher with separately written exact code; audited by an external referee). At A = 2, L = 2 the
  source-selected traces G_3 and G_5 are rational and smooth at 0, the seventh finite part is exactly
  B_7(c_l, w) = -23/29059430400 (natural units -23/14189175; the integrand is a Laurent polynomial with no term x^(-1),
  so no logarithm arises), and p_7 = 17 is odd, so smoothness at 0 with l_7 = 0 would require B_7(c_l, w) = 0. Hence the
  two-parameter family of axis data w = -A x (1 - x^2/L^2)/(1 + x^2/L^2), g = x^2/(1 + x^2/L^2), A > 1, L > 0, admits no
  profile of P_inf that is smooth near 0 (C^24 suffices) and of class C^(6,alpha) near P for some 0 < alpha < 1 (the
  velocity then has the same regularity by the Localization of (f)). Indeed C^(6,alpha) gives C^(4,beta) for every
  beta < 1, so l_3 = l_5 = 0 and, at A = 2, l_7 = 0 (Higher odd orders in 6.3.1 (h), whose threshold for j = 7 at A = 2
  is alpha > -2); since p_3 = 6 + 2/A is not an even integer, smoothness at 0 gives B_3(c_l, w) = 0, and for this family
  B_3(c_l, w) = C_A L^(-4-2/A) (1 - S_A/L^2) with C_A = -(8A - 1) B(-2 - 1/A, 2/A)/(3A (2A - 1)) > 0, so L^2 = S_A; then
  B_5(c_l, w) < 0 excludes A != 2, and B_7(c_l, w) != 0 excludes A = 2. This excludes one explicit family of axis
  functions under a regularity hypothesis at P beyond the class; it says nothing about other axis data and is not
  NO_inf.
- A local version (no profile of P_inf in a specified weighted trace neighbourhood of a reference trace near X3). This
  needs a compatible reference trace w_ref with a certified value B_ref != 0, a quantitative bound
  |B_3(c_l, w) - B_ref| <= K delta on the neighbourhood of radius delta in a weighted trace norm (that of 6.3.1 (i), or
  the weaker norm N of 6.3.1 (o)), and control |l_3| <= ell of the source limit for every profile considered, with K
  delta + ell < |B_ref|; l_3 = 0 by 6.3.1 (h) is one sufficient source condition. If proximity to X3 is inferred from
  residuals or from a weaker norm, its implication for that trace distance must also be proved. At A = 4 an explicit
  positive reference value is proved, and a Lipschitz constant and the exclusion radius e^(-10^7) are checked by the
  verifier (6.3.1 (n)); in the weaker norm of 6.3.1 (o) the radii 1e-8 (with parameter widths 0.06 in A and 0.0003 in e)
  and 1e-7 (at fixed A = 4, e = 1/16) at that reference are certified. These certificates have not been connected to an
  exact profile by a numerical trace enclosure, and their reference parameters A = 4, e = 1/16 are far from those of the
  computed branch. At the computed A, an external referee gives an exclusion with polynomial constants in a weaker
  weighted norm, for A_0 = 10.150725, |A - A_0| <= 0.06 and |x*^(-2) - e_0| <= 0.0003 (e_0 = 0.0135206 for the first
  reference, 1/8.6000638^2 for the second), and for profiles of P_inf with the Hoelder or cone hypothesis of 6.3.1 (h)
  whose normalized trace lies in the affine domain of that norm (a hypothesis that includes an anchored exponent 9/10 at
  the source): with balls measured by ||w~ - (A/A_0) w_0||_N, w~(u) = w(L u)/L, w_0 the reference: radius 1e-6 around
  the explicit compatible trace of 6.3.2 (a), and radius 4.5e-6 over the parameter box (5e-6 at fixed parameters), with
  an interval-arithmetic certificate for the reference value B_ref > 0.28 and every reference constant, around a
  degree-12 analytic compatible fit to the computed trace (6.3.1 (o); checked by the verifier, and the analytic
  estimates and the certificate each audited by a further external referee). Within this restricted class, what remains
  missing near X3 is a bound on the distance in that norm from such a reference to the trace of an exact profile; for
  the general class of P_inf, control of the source limit (or another noncancellation argument) is missing as well. The
  available trial samples alone do not provide that bound: fits of equal quality are 9 to 67 apart in that norm
  (sampled; the three pairs checked exactly differ by more than 0.03 in their Taylor coefficients alone), mostly through
  the weighted origin term, the stored traces leave an origin interval unobserved, and agreement at sample points does
  not control the norm at all; it would need additional analytic information, for example a justified estimate
  converting residual and regularity bounds into control of that norm. The one analytic continuation estimate available
  (a two-constants estimate, under the additional hypothesis that the compatible difference is holomorphic in a
  specified Bernstein ellipse, continuous on its closure and bounded there, which is not known for exact profiles) shows
  that, with ellipse parameter 4, bound M = 10 and tube radius 0.05, uniform agreement to 1.4492e-31 on the whole
  interval [0.02, 0.985] suffices for the 4.5e-6 ball; that is one conservative sufficient estimate, not a necessary
  accuracy, and discrete sample agreement does not supply the uniform bound (6.3.1 (o), further statements; external
  referees, checked by the verifier).
- What NO_inf has to exclude (external referee; the decomposition is 6.3.1 (a)). At every odd order j >= 3 for which the
  endpoint limit l_j, the finite part and the expansions of the lower traces exist, smoothness near 0 requires
  C_(0,j) = l_j + B_j = 0 when p_j is not an even integer, and compatibility conditions at the resonant orders; an
  exclusion through this hierarchy must justify these conditions on its whole scope. NO_inf therefore needs only that
  these conditions have no common solution on the scope claimed. On a specified class on which l_3 = 0 is established,
  it suffices to prove B_3 != 0 throughout that class, or that B_3 = 0 forces the failure of a higher necessary
  condition: a nonzero C_(0,j) = l_j + B_j at a nonresonant order, or a nonzero compatibility coefficient at a resonant
  one (a nonzero B_j alone suffices only where l_j = 0 is known). For the general class with A > 2 the argument must
  also cover profiles with l_3 = -B_3 != 0 and profiles for which l_3 is not known to exist. At nonresonant orders
  j = 5, 7 the conditions reduce to B_5 = B_7 = 0 only when l_5 = l_7 = 0 as well. An exclusion proved on a local family
  is a global exclusion only if that family exhausts the scope claimed.
- Higher jets. For P_inf the conditions for j = 5, 7, ... are needed as well as j = 3. For each odd j the endpoint
  limits and the recursively selected lower jets must be justified before B_j can be used; for nonresonant exponents
  smoothness requires C_(0,j) = l_j + B_j = 0, and rational resonances require their own compatibility conditions. The
  analogue of 6.3.1 (h) holds under C^(j-1,alpha) regularity at P with 0 < alpha < 1 and alpha > 1 - (j-1)/A
  (6.3.1 (h), Higher odd orders); in particular, for 1 < A <= 4, C^(4,alpha) regularity near P with some 0 < alpha < 1
  gives l_3 = l_5 = 0, B_3 = 0, and B_5 = 0 unless A = 2, where the logarithmic condition replaces it, and for j = 5 and
  1 < A < 4, C^4 regularity of both rho and W near P suffices (C^4 regularity of W being then a separate hypothesis);
  for j = 5, l_5 = 0 also follows from the summable fourth-derivative hypothesis of 6.3.1 (h) for every A > 1, and, with
  the curl identity, for 1 < A < 2 from the density bounds there (with their exponent condition). The C^(2,alpha)
  regularity of the class does not supply these hypotheses for j >= 5, for any A, and no endpoint theorem at these
  orders under that regularity alone is established in this report (6.3.1 (j) gives the frozen thresholds).
  Reversible transport, constant divergence, the local source conditions and smooth downstream data do not by themselves
  supply these hypotheses (external referee; audited by a second external referee; checked by the lead researcher and by
  the verifier). For every A > 1, g* > 0 and 0 < alpha < 1 there are exact local solutions near P of W.grad f = f and
  div W = A + 1, with f and b odd in y and a even in y (W = (a, b)) and with W(P) = 0, DW(P) = diag(A, 1) and
  f_y(P) = g*, that have f in C^(3,alpha) and W in C^(2,alpha), are smooth away from P, and equal the linear solution
  f = g* y, W = (A s, y) on a fixed downstream neighbourhood, such that for each of D^4 f and D^5 f no bound C r^(-M)
  with finite C and M holds on any left cone or on any horn |y| <= kappa r^beta with fixed kappa, beta > 0 (s = x - x*,
  r = -s). The failures occur along sequences approaching P; for D^5 f they already occur on the axis. The examples are
  obtained from the linear solution by area-preserving changes of variables supported in packets at the distances
  r = 2^(-n) from P; they violate b_s - a_y = -f_s, so they are neither profiles nor local solutions of the coupled
  system (compare the transport examples of 6.3.1 (j)). For these examples the first derivatives of the outward flow
  have uniform exponential bounds in time, while its fourth and fifth derivatives at the corresponding terminal times
  carry the large density derivatives. This argument neither proves nor excludes a polynomial growth class at P for the
  coupled system, and an unspecified finite growth exponent would not by itself supply the exponent condition p < q - 1
  of the density bounds in 6.3.1 (h). Separately, if nonnegative sequences N_n and e_n satisfy N_n <= theta
  N_(n+k) + e_n with a fixed integer k >= 1, 0 < theta < 1 and sum_n e_n finite, then a bound N_n <= C 2^(beta n) gives
  summability of N_n when theta 2^(beta k) < 1, and N_n = theta^(-n/k), e_n = 0 shows that a finite exponent alone does
  not give this conclusion; no such recurrence has been established for the coupled fields, and the sequence argument
  does not exclude an improvement using the coupled equations. B_5 and B_7
  are defined by 6.3.1 (a) only at traces whose lower traces have power expansions at 0, which on the nonresonant branch
  with l_3 = l_5 = 0 near X3 means B_3 = 0 (respectively B_3 = B_5 = 0; at resonant orders a nonzero smooth homogeneous
  coefficient may be allowed, 6.4), so with the finite-part prescription of 6.3.1 (a) they cannot be evaluated on X3
  (that would need an extension of the prescription to the lower non-integer terms), and no estimator for sampled trial
  data has been built (6.4). The fixed-field converse of 6.3.1 (a) does not prove smoothness of a coupled profile known
  only to have finite regularity at 0, and no separate theorem excluding C^8 centres has been established.
- Q4 (other branches). Not tested numerically: no searches with other numbers or positions of the zeros of W, other x*,
  or other starting fields were made, and nothing about such branches follows from the computations near X3. The
  analysis leaves open in particular profiles that are C^infinity near 0 and carry a singular mode at the source
  (l_3 != 0); for A > 2 such a profile must fail the cone form of the Hoelder hypothesis at P (6.3.1 (h), 6.4), which
  exact solutions of the coupled equations on a left cone at P do (6.3.1 (r), m = 3; whether one extends to a
  neighbourhood of P is open), and for 1 < A <= 2 there is none in P_inf (6.3.1 (m)).

## Appendix. Verification timeline
UTC times; entries before the first dated break are on 2026-10-17. Each entry
records a check or audit as it happened; later entries supersede earlier readings where they say so. Notation is that
of section 4 (the conventions before 4.1). In the entries from 10:51 to 12:26 of 2026-10-18 "the candidate" is
X1, the fixed-c_l fit then under test; from the 16:44 entry of that day on it is X3.
- 17:54 specification v1 written (class, velocity law, lemmas).
- 18:00 to 18:05 verifier audit of specification v1: sound, one formula error in the far-field tail (corrected).
- 18:10 external referee audit of specification v1 received: velocity law confirmed; the proof of one lemma repaired,
  another lemma strengthened; the rigidity lemma replaced by an explicit form; the regularity lemma qualified.
- 18:13 specification v2 (all corrections).
- 18:21 to 18:28 verifier audit of specification v2 and of the analysis notes, sections 1 to 4: all confirmed, with one
  minor repair in the velocity bound; the 2D regularity statement is open.
- 18:45 external referee audit 2 received: positivity argument correct with a repair on the y-axis; the finite-part
  formula for B_3 is conditional on smooth axis data; a numerical defect in the B_3 tool found and fixed.
- 18:49 verifier audit of the first version of the report: only audited claims present.
- 19:22 external referee audit 3 received: closed-form B_3 formula correct with repair; Lemma R11 correct, its use for
  sequences conditional; B_3 has no sign from local axis constraints.
- 19:46 verifier audit (hand rederivation, numerical checks) of the positivity repair, the axis constraints, the
  closed-form B_3 formula, Lemma R11 and the no-sign result: all confirmed with the stated conditions.
- 20:10 verifier pre-candidate checks of the first trial fields of the global trial construction: whole-box residual,
  normalization and parity checks; acceptance list for a candidate agreed (section 4 standards).
- 20:51 verifier audit of the trial construction's final fit: the trial is reproduced by separately written code (its
  generator, inverse, residual evaluator and the identity for c_l); not at the YES standard (residual next to the
  source point, centre jet defect growing under refinement, no second solver).
- 21:28 verifier evaluation of the w-only finite part B_3 on the trial (end-treatment dominated spread).
- 22:02 verifier: plain dynamic rescaling from the trial does not settle (unstable linearized flow); the numerical
  workstream's reproduction is not at the standard; the integrated-by-parts form of the B_3 formula confirmed (with the
  condition 2/(2c_l - 1) not a positive integer); the rule for an explicitly distinguished finite-regularity problem
  agreed with conditions.
- 22:21 verifier: the characteristic defect J of the trial (section 4) recomputed with separate code; values confirmed.
- 22:28 verifier rulings on the standard: a second converged solver is desirable, not required; the independent check is
  the verifier's own residual evaluator on the exported density, the identity for c_l, and one determination of c_l that
  does not use the identity; c_l is quoted with its spread over constructions, which is not an error bound.
- 22:30 verifier hand audit: if rho is C^1 near the source P, W is C^2 there with A = d_x W_1(P) > 1, and rho_y(x,0) > 0
  on (0, x*) (true in P_2 by the axis equation w g' = (1 - h) g of R10; without it the statement fails, e.g. W = (2 xi,
  eta/3), rho = eta^3 in linear coordinates (xi, eta) at P; added 2026-10-18 after an external referee), then h(P) = 1
  and rho is a multiple of the linearizing coordinate eta near P (consistent with R5 and R6 of section 3).
- 22:34 verifier audit of an earlier version of this report: sections 0 to 3 confirmed; one inconsistency in the class
  statement found (resolved 23:43).
- 22:42 verifier audit of the centre-corrected trial: the centre jet defect reduced to about 1e-7 relative, confirmed on
  the export; the residual next to P unchanged; improvements measured only on a fitting grid are not accepted until
  reproduced on an export.
- 22:51 verifier: R/rho at P equals h(P) - 1, so J is reported by distance shells from P.
- 23:16 verifier: the headline "YES, strong numerical evidence, for the explicitly distinguished problem P_2" is
  admissible, under four stated conditions (definition where first used; existence near the trial is the numerical
  claim; P_2 consistency checks reported; uniqueness not claimed).
- 23:36 verifier recomputation of the residual by region and of J by distance shell on the centre-corrected trial:
  confirmed; the residual next to P (1.2e-4 in N_f) remains the obstacle to the standard.
- 23:43 verifier audit of section 1 (definition of P_2): confirmed, with one wording correction (applied).
- 2026-10-18 00:00 verifier evaluation of the locally refined trial between fit nodes (three resolutions, two inverse
  domains, own generator and evaluator): near-P residual lower by a factor of about 7 than on the centre-corrected
  trial; the characteristic defect J falls together with it, as expected for a representation limit;
  still above the standard (1.8e-5 in N_f, 5.1e-6 in N_v near P).
- 00:10 verifier: the method of the bounded-domain fits (equation fitted only inside a fit radius, two-term exterior
  closure outside) reproduced in the verifier's own generator; numbers preliminary.
- 00:14 verifier hand rederivation of the far-field closure error of a disk model (error in c of order R^(2k-2) with a
  one-term exterior and R^(3k-3) with two terms, conditional on the far-field expansion); the verifier's own inverse
  follows the R^(2k-2) law, and its values of c_l and h(P) at the largest domain are converged in domain to about 1e-9.
- 00:16 verifier: along the locally refined fit, c_l rose by 3.4e-5 while the near-P residual fell by a factor of 7;
  the argument that c_l is insensitive to the near-P defect is a heuristic, not a bound.
- 00:20 and 00:51 verifier audits of earlier versions of this report: confirmed, with one wording note; fits closed by
  an exterior expansion are only C^1 across the closure radius and are quoted as bounded-domain fits, not as admissible
  trials.
- 00:45 verifier audit of the domain series (fit radii 200, 300 and 900 shape units): c_l agrees to 1.5e-6 across the
  fit domains at that fit stage and the near-P residual is that of the best trial to 10 percent, but the series does not
  contain the best trial (a fit of the global formula on one domain); standard not met.
- 01:02 verifier: continuing the fit on a fixed radial basis (215 functions) lowered the residual away from P (band
  10 <= r <= 100 from 4.8e-6 to 2.9e-6) but not the near-P maximum (1.86e-5).
- 01:10 verifier map of the near-P residual: it sits on the refined-knot ring 8.2 <= r <= 9.4 near the slow curve above P
  and changes sign from one radial knot interval to the next, with its angular content inside the angular cutoff; read
  as a radial representation error at the knot scale (a numerical reading, to be tested by refinement).
- 01:14 verifier: fits whose c_l differ by 3e-5 have the same near-P residual and differ by a smooth global
  deformation; the spread of c_l over fits (about 3e-5) measures reproducibility, not an error bar (if the exponent is
  unique, one of two such fits is off by at least half the spread); a bracketing test (two starts, same basis, grid
  and budget) requested.
- 01:33 verifier check of an external referee's answer on counting conditions for the linearized problem: an index
  count that treats the linearization as transport plus a compact perturbation is not justified (the velocity term is
  of order zero with nonzero symbol on the transverse covector); whether the normalized profile is isolated is open.
- 01:41 verifier intermediate check of the fit with halved knot spacing near P (244 radial functions) part way through
  a fit segment: near-P maximum lower by a factor of 5.5 and the J spread by 4.5, together; the residual just outside the
  refined band unchanged. Intermediate, not a candidate.
- 01:43 verifier audit of the first-order analysis of the c_l error of a trial (the error is the residual weighted by a
  dual solution, under an unproved invertibility hypothesis for the linearized problem): confirmed as a heuristic, with
  one precision in the decay hypothesis at P (a Hoelder rate, not o(|X - P|)).
- 02:17 verifier audit of an external referee's corrections to a heuristic on why c_l is weakly determined: the
  proposed mechanism (a cheap residual for a shifted exponent) holds for frozen transport only, the nonlocal velocity
  feedback contributing a term without the 1/T decay of the transport term (T the cutoff time of that heuristic); the
  proposed estimator of the c_l error from the characteristic defect is wrong as stated (counterexample); its
  replacement, the Gauss-Newton exponent step of the least-squares problem,
  estimates, to first order, the least-squares minimizer of a trial basis in c_l, not the exponent of the profile; at
  a least-squares floor the residual rises only quadratically along the soft direction. Confirmed, with the condition
  that the six-digit c_l is never quoted without the statement that the spread of fits is a reproducibility number.
- 03:17 verifier audit of the trials with 244 and 302 radial functions after one fit segment each, evaluated between
  the fit nodes with an independent inverse at three resolutions: the measured residuals were confirmed (302 functions:
  flux-normalized maximum 2.3e-6 for 2 <= r <= 100, velocity-normalized maximum 1.4e-6, h(P) - 1 of order 1e-8). The
  reading that the near-P residual is a radial knot-scale error was confirmed for the stem component (the residual in the
  ring 8.2 <= r <= 9.4, 0.1 <= theta <= 0.5 above P) and refuted for the near-P maximum as a whole: on the 302 basis
  that maximum sits in a strip next to the x-axis whose angular content is at the edge of the trial's angular space.
  Neither trial meets the residual standard.
- 03:17 verifier audit of the lead's B_3 estimator: its integrated-by-parts end piece is not converged in the
  quadrature order (the increments grow by a factor about 3 per doubling, explained by a non-integrable remainder); the
  original form is converged to 5e-4 and agrees with the verifier's estimator, B_3 about 0.30 on the three latest bases.
  Values from the unconverged form were withdrawn.
- 03:45 verifier evaluation of fixed-c_l states of the independent discretization over c_l 5.52 to 5.71: at their
  residual level next to P (15 to 60 times that of the 302-function trial) a c_l change of 1e-2 is not detected; every
  near-P diagnostic improves monotonically toward larger c_l in that discretization, a property of its error at P and
  not evidence for a larger exponent.
- 04:34 verifier evaluation of the 302-function trial plus multiples of a fixed c_l direction, not re-optimized: an
  offset of -1e-4 is not detected by the residual for r <= 1000 or by the characteristic defect J (within 4 percent);
  only h(P) - 1 (3.5e-7) moves. At +1e-4 the characteristic defect J is 1.74 times larger. So six-digit c_l values are
  not determined by the residual at that level and any quoted uncertainty is at least 1e-4; along this direction the
  near-P maximum doubles between offsets 1e-3 and 3e-3 (upper bounds on the cost, since nothing was re-optimized).
- 04:56 verifier audit of the trial with 375 radial functions after one fit segment, between the fit nodes: the radial
  step 302 to 375 lowers the band 10 <= r <= 100 by a factor 2.9 to 8.0e-7 and does not lower the near-P maximum
  (2.44e-6, up 7 to 9 percent) or the far-field velocity-normalized maximum (1.46e-6); J did not fall. Not at the
  residual standard.
- 04:56 verifier evaluation of the 244-function trial moved along its optimized soft c_l direction (offsets 1e-4 to
  3e-3, linear tangent shapes, not refitted): at offset -1e-3 every between-node maximum is within 0.76 to 1.06 of the
  fit and |h(P) - 1| = 3.4e-8, so c_l is not determined to 1e-3 at that level. The diagnostics prefer different sides:
  the near-P maximum and J fall toward lower c_l, the linearised least-squares step points to higher c_l.
- 05:06 verifier evaluation of the independent discretization at a doubled angular resolution: three of its near-P
  diagnostics (h(P) - 1, the maximum within 0.5 of P, J at 0.01) now prefer smaller c_l, the reverse of the 03:45
  entry, which confirms that the preferred side at that residual level is a property of that discretization.
- 05:09 verifier audit of the lead's analysis of the soft direction (cost per unit c_l at most 3.58e-3 on the 244
  basis): the facts were confirmed; the claim that the Gauss-Newton exponent step grows like the inverse cost was
  refuted (it is not converged); the reading "the objective resolves c_l only at the 1e-2 level" was refuted: the
  linear model doubles the objective only beyond 8.9e-3, but the measured second-order term doubles it along the tangent
  shapes at about 4.1e-3, and the minimum of a fixed-c fit can only be lower. A third reading was added (the
  second-order term, not the linear one, may pin c_l).
- 05:16 (addendum 05:24) verifier evaluation of the 302-function trial plus multiples of the optimized 244 soft
  direction (field level, not refitted; between-node resolution N 16875, offsets 0 and -1e-3 repeated at N 22500):
  every diagnostic stays within 30 percent of
  the fit for offsets -1.5e-3 to +3e-4 (c_l 5.57486 to 5.57666, |h(P) - 1| <= 4.5e-8); no offset up to -3e-3 or +1e-3
  is excluded. The lower bound on the c_l uncertainty at the 302 level is 1e-3 (lower side 1.5e-3, upper side 3e-4).
- 05:28 verifier check of the start of a fit with c_l held fixed at 5.60 (offset +2.4e-2) on the 244 basis: the start
  objective is dominated by the second-order term of the tangent law (intermediate check, no reading).
- 05:35 verifier audit of the entries 04:34 to 05:16 and of the lead's account of the soft-direction intervals: confirmed
  with wording corrections (applied); both interval widths, 1.3e-3 (244) and 1.8e-3 (302), are lower bounds, and
  nothing shows that the width shrinks with the basis.
- 05:53 verifier evaluation of the trial with 375 radial functions after one fit segment, plus multiples of the
  optimized 244 soft direction (field level, not refitted; between-node resolution N 16875, offsets 0, -1e-3 and -1.5e-3
  repeated at N 22500): at offset -1e-3 (c_l 5.57536) the global between-node maximum falls to 0.73 to 0.74 of the fit
  (1.8e-6 from 2.44e-6; it sits in the strip next to the x-axis left of P), J at 0.01 to 0.68 and the far-field
  velocity-normalized maximum to 0.96; only the bands 10 <= r <= 100 and 0.1 <= r <= 2 rise (by 3 to 16 percent, to
  values at least two times below the global maximum). So along this direction the c_l that minimizes the maximum norm
  of the residual lies about 1e-3 below the least-squares value 5.57636. The lower bound on the c_l uncertainty at the
  375 level is 1.5e-3 below and 3e-4 above the fit value, as at 302; no offset from -3e-3 to +1e-3 is excluded. A
  field-level statement; 1.8e-6 is not at the residual standard.
- 05:53 verifier audit of the trial with 375 radial functions and angular modes up to m = 150 after 500 iterations of its
  first fit segment (intermediate): every band away from P falls (10 <= r <= 100 by a factor 1.8 to 2.2, the far-field
  velocity-normalized maximum to 1.14e-6, the plane rms by 2.1), while the strip next to the x-axis left of P stays at
  2.40e-6 and remains the global maximum, and J from all start angles rises by a factor 2.1 to 2.5 through
  characteristics that start next to the axis. Intermediate, no reading. (The sentence first written here, that the strip
  is not an effect of the angular truncation, was refuted at 06:54.)
- 06:17 verifier check of the soft direction carried exactly into the coefficients of the 375-function trial (a line in
  the trial class, not refitted): the carried direction is the 244-level soft direction as a function on the plane to
  3e-4 relative. Along this line the global between-node maximum is smallest at -1.5e-3 (0.71 of the fit), flat to 4
  percent over -2e-3 to -1e-3; J is smallest at -1.5e-3 (0.64); the least-squares objective is smallest at about +5e-4.
  The field-level line of the 05:53 entry agrees with it at -1e-3 and is a first-order statement only beyond 1e-3.
  Unrefitted lower bound on the c_l uncertainty at the 375 level: 2e-3 below and 3e-4 above the fit value. The same
  field-level test on the trial with angular modes up to m = 150 (iterate 500): the strip moves with c_l as before;
  the global maximum falls by 23 to 25 percent at -1e-3 to -1.5e-3.
- 06:18 verifier check of the proposed account of the independent discretization (section 4.6): confirmed with
  corrections; one sentence (fixed-c_l fits over 5.52 to 5.71 "equally good to 20 percent") refuted as worded. The
  corrected text, with the grid qualifier of 06:56, is the one in section 4.6.
- 06:33 verifier audit of the trial with 375 radial functions and angular modes up to m = 150 after its first fit
  segment (750 iterations): c_l from the identity 5.5763624; |h(P) - 1| <= 1.7e-7 at the largest box (between-node N
  11250 to 22500); global between-node maximum 2.28e-6 to 2.44e-6 in the strip next to the x-axis left of P, 2.44e-6
  converged in the between-node grid (06:54), equal to the m <= 100 trial; plane rms 0.44, band 10 <= r <= 100 0.58 and
  far-field velocity-normalized maximum 0.77 (1.12e-6) of the m <= 100 trial, but J 2.2 to 2.7 times larger (3.1e-6 at
  0.03). Centre jet, the single stagnation point on the x-axis, no other zero of the field on the evaluation grid and
  the lower bound on |W| / (c_l |X|) confirmed as for the m <= 100 trial. The starts of the fixed-c_l fits at -1e-3,
  -3e-3 and -1e-2 (this trial plus the carried direction, not refitted) have global maxima 0.94, 1.44 and 6.0 of the
  fit; the c_l identity holds on them to 3e-7.
- 06:54 verifier audit of the strip next to the x-axis left of P on the trials with angular modes up to m = 100 and up to
  m = 150: the between-node maximum of the m <= 150 trial converges to 2.44e-6 in the between-node grid (as for m <=
  100). Next to the axis the residual oscillates in theta at a local frequency close to the angular cap of each basis (n
  186 to 196 in sin(n theta) for m <= 100, 264 to 306 for m <= 150). Raising the cap from 100 to 150 lowers the
  normalized residual next to the axis by 2.3 to 4.8 times farther than about 0.3 from P and leaves its maximum
  unchanged; the maximum moves toward P. The exponent content added by the cap step is confined to theta < 0.08, has the
  same angular profile at every r from 7.6 to 8.56, grows toward P and changes sign at P; the angular spectrum of the
  exponent there decays algebraically. So the strip is an oscillation at the top of the angular basis and it also moves
  with c_l. The value h(P) - 1 = 2.8e-6 in the characteristic-defect output was an interpolation error; on the exported
  axis trace h(P) - 1 is at the 1e-8 level.
- 06:56 verifier check of the section 4.6 paragraph, version 2: confirmed with one correction (the comparison of
  fixed-c_l fits over 5.52 to 5.71 holds on one grid of the independent discretization only; the replacement sentence is
  in 4.6). 06:58 the numerical researcher confirmed version 2 against the records of the independent discretization.
- 07:11 verifier check of the fit with c_l held fixed 1e-3 below the free fit (c_l 5.5753626, 375 radial functions,
  m <= 150) after 250 iterations (intermediate): global between-node maximum 1.50e-6 (2.43e-6 for the free fit, same
  between-node grid), still in the strip, now 0.07 from P; J 1.5 times lower; the L2 objective 15 percent higher; h(P) =
  1 to 2e-8 at both c_l values; the bands away from P unchanged to 10 to 15 percent. Not yet a c_l effect: the fixed fit
  has 250 more iterations than the free fit; the control is the free continuation at the same iteration count. The
  standard (about 1e-6 including next to P) is not met.
- 07:45 verifier check of the same fixed-c_l fit after 500 iterations (intermediate): global between-node maximum
  9.84e-7 in the finest configuration, J 1.35e-6 at 0.03 and 1.58e-6 at 0.01.
- 07:59 verifier check of the domain study. In the convention of each fit (closure at the fit's own inverse radius)
  the trials fitted to radii 900, 300 and 100 shape units agree inside their fit radii: maxima next to P 2.44e-6,
  2.63e-6 and 2.54e-6, c_l 5.5763622, 5.5763628 and 5.5763644, h(P) = 1 to 5e-8. Numbers computed with the fitted
  formula continued beyond its fit radius are not numbers of the fit and were not used in that check (the same fits
  read with the formula continued are reported in 4.4). The independent velocity check at 51 nodes was confirmed for
  the third quadrature configuration (agreement 1e-9 next to P and 5e-9 at r = 100).
- 08:32 verifier check of a structure shared by all fits at the source point P: the third derivative of log a changes
  sharply across the characteristic leaving P (about +0.12 at P on the x-axis, 0.05 to 0.16 depending on the
  estimator, decaying to 0 by 0.2 from P; off the axis the change follows the characteristic and changes sign near
  height y = 0.5). The fits are C^6, so this does not show that a solution fails to be C^3; whether a solution has a
  singularity there is open. The fits share one lineage, so the agreement between them does not separate a property
  of the fitted family from a property of a solution. The main deliverable does not depend on it.
- 09:05 verifier audit of the fit with c_l held fixed 1e-3 below the free fit, final state (750 iterations after the
  shift along the soft direction), in both normalizations at six evaluator configurations: whole-box maximum 6.5e-7 to
  7.0e-7 in N_f, next to P (free fit 2.28e-6 to 2.44e-6); in N_v 1.13e-6 to 1.17e-6, in the far field next to the y-axis
  (free fit within 3 percent), and at most 5.7e-7 for r <= 1000; J 1.0e-6 on 24 labels (free fit 3.1e-6; corrected at
  10:51 below); identity c_l = (1 + psi_xy(0))/3 to 3.2e-9; h(P) = 1 at both c_l values to the evaluator's grid error.
  In the strip next to the x-axis left of P the fixed fit is lower by a factor 3.4 in both normalizations; next to the
  x-axis at r 2 to 6 it is higher by up to 26 percent. The fits differ in iteration budget, so the share of the
  difference due to c_l is open until the equal-budget free control. The criteria for a fixed-c_l candidate were
  confirmed with six amendments (equal-budget control, both normalizations and J, every fixed c_l tried listed, h(P) = 1
  not used to select, resolution study with J, evaluator floor exclusions stated). The standard is not yet met:
  resolution and domain studies at the fixed c_l are pending.
- 09:14 verifier check of the inverse-error row (confirmed on the free fit with 375 x m <= 100 functions: velocity
  differences 9e-10 within 0.5 of P to 1.5e-8 at r = 300, impact on the normalized residual at most 3e-9) and of the
  effect of the fits' far-field closure (measured with the closure at 111 L and 333 L, the inverse radii of the fits
  with rows to 100 L and 300 L; the domain fits are tests of the closed problems, not residuals under the canonical
  velocity law). It also completed the selection rules for several fits
  (a free continuation's drift of c_l, the number of fits compared, the resolution and domain studies at the chosen
  fit's own c_l) and corrected an earlier version of this section in wording and numbers.
- 10:20 external referee audit of six analytic statements of section 4 received (the trial's regularity class, its
  far-field expansion, the limit of R/rho at P, the characteristic defect J, the exclusion of polynomial states, and
  the reading of the third-derivative feature at P): four correct with qualifications, now in the text (rho_h is in
  C^(6,beta)_loc and log a in C^(4,beta)_loc; J refers to transport by the frozen trial field and its spread over a
  fixed label set does not measure a common transport error); the polynomial-state sentence was wrong as worded and is
  replaced; the inference that the feature at P is not a single conormal layer was not justified and is withdrawn.
- 10:51 (addendum 10:53) verifier evaluation of the equal-budget free control (the free fit continued to the same 750
  iterations as the candidate) and of the characteristic defect on a resolved label set. The 24 labels used until then
  do not resolve J in the start angle; on 857 labels on r = 20 (737 uniform, 60 next to each axis) the candidate has
  J(0.03) = 2.74e-6 and J(0.01) = 2.68e-6 (1.91e-6 and 2.02e-6 on the 737 uniform labels), and every earlier 24-label J
  is a lower bound. The largest values come from labels whose characteristics run along the x-axis between the origin
  and P, where R/rho on the axis reaches 1.04e-5 on the candidate (8.0e-6 on the free control). At the equal budget the
  free control is lower in J and in the L2 objective, the candidate lower in the strip maximum (factor 3.4 in N_f) and in
  the far field in N_v; the two fits are not ordered, and the criterion for a fixed-c_l candidate (residual and J not
  higher than the equal-budget free fit) is not met at 750 iterations. Also confirmed: the six referee wordings of the
  10:20 entry as applied, and the effect of the fits' far-field closure (at most 1 percent of the residual next to P and
  7 percent for r < 1000, maxima over all grid points). The standard is not met. (Corrected by the verification entries
  of 12:09 and 12:26: the maxima of R/rho on the axis are 1.07e-5 on the candidate and 8.2e-6 on the free control, and
  the axis carries only the maximum at a label next to the y-axis; the other extremes take their J from the strip next to
  the x-axis and from the disc around P in comparable parts.)
- 12:09 verifier evaluation of the domain fits, a second fixed-c_l basis and the residual structure next to the x-axis.
  The fits on a domain cut to 90 L (free c_l) and to 300 L (fixed c_l), both at angular cap m <= 100, agree with the
  full-domain fits of the same basis by rules fixed beforehand. Their maxima next to P are 1.07 to 1.11 times those of
  the full-domain fits, the 10 < r < 100 band 0.71 to 0.95 times, and c_l moves by +4.9e-6 for the free fit. The 90 L
  formula continued beyond 90 L is not a solution there. At the fixed c_l, the step from cap m <= 100 to m <= 150 lowers
  every residual band and the spread of J (at unequal iteration budgets). Next to the x-axis, from r about 4 to P, the
  residual oscillates in the angle at the angular frequency of the basis cap. The axis quantities q0 and I(eps) are
  differences of band parts larger than themselves. A domain study at cap m <= 150 does not exist yet.
- 12:26 verifier evaluation of the free continuation of the candidate and of the origin of the J oscillation.
  - The oscillation of J in the start angle is carried by the residual at angular frequencies at or above the basis cap,
    on the candidate and on the m <= 100 fit. On the equal-budget free fit no single frequency band carries it.
  - On the radial nodes of a grid with spacing 0.012, |q0| reaches 1.3e-6 on [8, x*).
  - Continuing the candidate with c_l free for 1000 iterations moves c_l by +2.5e-6. It lowers the L2 objective by 12
    percent and J by 18 percent, and raises the maximum next to P by 1.5 times.
  - The two free fits are 1e-3 apart in c_l, and neither moves measurably toward the other at these budgets, so c_l is
    quoted as an interval of at least [5.5753, 5.5764].
  - A variant with extra weight on the axis between the origin and P failed: its maximum next to P was 6.5 to 7.7 times
    the candidate's.
- 13:41 verifier evaluation of the long continuations: the fixed-c_l fit and its equal-budget free control (the free fit
  at the same 750 iterations), each continued for 20750 further LSQR iterations on the same basis (angular cap m <= 150).
  - By the selection rule fixed before the runs, the fixed-c_l continuation is kept against the free one when the
    far-field band is read as all r > 1000 (inside the configuration spread there). Read over the band
    1000 <= r <= 7652 (1000 L) only, its far-field N_v is higher by about 3 percent, beyond the spread, and the free
    one would be kept. The lead fixed the band as all r > 1000 at 13:54, after these measurements, and both readings
    are reported (4.3).
  - The margins are small: 9 percent in whole-box N_f, 8 percent in J, 0.5 to 3 percent in the far-field N_v.
  - The fixed-c_l continuation halved the L2 objective and doubled the maximum next to P (N_f 6.5e-7 to 7.0e-7 before,
    1.4e-6 to 1.5e-6 after, ranges over the configurations). The free continuation lowered its L2 objective by 40
    percent and its maximum next to P from 2.1e-6 to 2.3e-6 down to 1.6e-6. The fixed-c_l fit before the continuation
    keeps the lowest whole-box N_f of the fits measured by then, with a higher N_v and a lower J than the continued
    one, so the fits are not ordered, and continuing on this basis gives no systematic improvement of the maximum
    residual. On both continuations the residual at the angular cap frequency sits next to the x-axis from r 7 to P.
  - On the fit before the continuation, at half the node spacing, |q0| reaches 1.3e-6 on [8, x*) and stays below 1e-6 on
    [8.4, x*).
  - Along the radial sequence of the free fits at m <= 100, the 857-label J falls from 1.9e-5 to 3.5e-6 and then rises by
    6 percent, to 3.7e-6; it is not monotone at the last step.
  - Neither a lower damping nor reorthogonalization lowered the objective by the 3 percent fixed beforehand, so the
    solver setting was kept.
- 15:31 verifier evaluation of the fixed-c_l continuation at angular cap m <= 200 (the continued m <= 150 fixed-c_l fit,
  enriched to m <= 200 with the new coefficients at zero and continued at the fixed c_l for 20750 LSQR iterations).
  - Whole-box N_f, N_v for r <= 1000 and the 857-label J fell by a factor of about 2: whole-box N_f 6.8e-7 to 7.2e-7
    (0.48 times the m <= 150 fit), N_v for r <= 1000 1.9e-7 to 2.0e-7, J 1.39e-6 (0.44 times). Not every band fell by
    that factor: N_v on the band 1000 <= r <= 7652 (1000 L) fell by 0.86, and the residual in the window y >= 1 above
    P changed by the ratios 1.01 and 0.81 on two grids. Beyond r 1000 the far-field N_v reads 1.09e-6 to 1.11e-6, 1 to
    2 percent lower than on the m <= 150 fit.
  - At equal budget (one linearization of 2500 iterations from the same start on each basis) the m <= 200 iterate is 0.71
    to 0.72 times the m <= 150 iterate in N_f and 0.62 to 0.69 in J on 185 labels (every fourth label of one family of
    the 857).
  - The residual at the angular cap frequency next to the x-axis moved to the band of angular frequencies 400 to 600, two
    to three times the new cap, with its peak at 399, at the lower edge of that band.
  - Next to the y-axis beyond r 1000 the residual is a residual of the fit, not the evaluator's floor, so the far band is
    read on all columns; the columns next to the y-axis are excluded only in the near field. At 11250 radial points an
    off-axis lobe is under-resolved, and whole-box N_f is read on the configurations with 16875 or more radial points
    (fixed at 15:54, before any row of the free control existed).
- 16:44 verifier evaluation of the equal-budget free control at m <= 200 (the continued m <= 150 free fit, enriched to
  m <= 200 and continued with c_l free for 20750 iterations), and the choice of the candidate.
  - By the selection rule fixed before the runs, the fixed-c_l fit is kept on every part and in every fixed reading:
    whole-box N_f 0.83 to 0.94 times the free control's (on the configurations with 16875 or more radial points),
    N_v for r <= 1000 lower, the far-field N_v equal to 3e-9 (inside the
    spread between configurations), 857-label J 0.94 times. By the second rule it becomes the candidate.
  - The free control's c_l moved by +2.2e-7 over its 20750 iterations, so the two fits stay 1e-3 apart.
  - B_3 on the candidate is 0.299 to 0.303 by the converged estimator forms. Values of the integrated form, whose end
    piece does not converge in the quadrature order, are not quoted.
  - On the x-axis |q0| on [8, x*) is at most 1.07e-6 on the candidate, the axis value of the ripple at the angular cap
    frequency.
  - The standard is not met yet: the domain columns at the candidate's basis, the angular row at m <= 100 and the
    report text are outstanding.
- 17:35 verifier evaluation of the first domain column: the candidate continued for 20750 iterations at the same c_l
  with residual rows r < 90 L and its own inverse on r <= 100 L with the two-term closure beyond.
  - By the domain rule fixed before the runs (the N_f maxima on 2 <= r <= 10 and on 10 <= r <= 100 within a factor 1.5
    of the candidate's, read two-sided, and |h(P) - 1| < 1e-7) it agrees on the lead's evaluator (2 <= r <= 10: 0.70
    and 0.73; 10 <= r <= 100: 0.82) and on two of the verifier's three configurations; on the third (16875 x 512) its
    2-10 maximum is 0.62 times the candidate's, outside the factor 1.5 on the low side. The verifier's ratios are
    1.04, 0.62, 0.72 on 2 <= r <= 10 and 1.02, 1.23, 0.83 on 10 <= r <= 100; h(P) - 1 = 5.6e-8 and 6.8e-10 on the
    configurations with 16875 or more radial points. (The verifier first read the rule one-sided and wrote "agree"; it
    corrected this at 18:42.)
  - Where it differs it is lower: next to P its N_f is 0.32 to 0.33 times the candidate's and the 857-label J 0.40
    times (eps 0.03; 0.37 at eps 0.01), while the lobe above P does not move (0.98). The column carries both a smaller
    domain and a further budget, so it does not separate the two; the 300 L column is the control.
  - With the formula continued beyond its fit radius instead of the closure, the 90 L fit has N_f about 3e-5 next to P
    and h(P) - 1 about -6e-5: it is a fit of the closed problem only.
- 17:50 the verifier confirmed from the code that the residual rows of every formula-global fit end at 900 L (the
  earlier version had said 1000 L), and that those of the earlier m <= 100 domain series end at 900, 300, 100 and 90 L.
- 17:59 to 18:25 far field of the trial (4.5). The verifier confirmed the identity
  (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k F' Theta_0 as formal algebra and, with its own inverse of Theta_0
  on the candidate, the axis values (forced -42.5520, stored -42.5561, C = 0.0187 on the axis); the external referee
  audited the formal orders, the formula side and the residual limit (correct, with the qualifications stated in 4.5).
  - Prediction fixed at 18:04, before the radii were evaluated: next to the y-axis the ratio of R / N_v to the leading
    term C r^(k-1) / (1+k) is within 0.15 of 1 at 1e5 L and closer at 5e5 L, and likewise at theta 0.82. Measured by
    the verifier in the formula convention to 1e8 L: 0.921 and 0.981 next to the axis, 1.111 and 1.046 at theta 0.82
    (with c_l = 1/k); confirmed, with the node scatter within 0.006 of the axis not resolving "closer" there.
  - Off the axis the ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns toward 1 slowly; an
    earlier statement (18:13) that off the axis the leading term is reached inside 1e4 L was refuted and withdrawn.
- 18:25 the canonical-inverse check of 4.5 repeated on the candidate itself (52 points) was confirmed against the
  numerical workstream's tables: velocity differences 1.0e-9 within 0.5 of P, impact on the normalized residual at
  most 8.6e-10 there.
- 18:25 re-audit of the section 4 text: confirmed subject to eight wording corrections (C1 to C8), all applied; no
  number read by a selection rule changed.
- 18:33 the verifier confirmed the third-order series of R / N_v of 4.5 with its own code (written from the
  definitions, its coefficients equal to the lead's to 7 digits in the leading one): measured / series 0.59, 0.87,
  0.98 at 3000, 4700, 9500 L; on its evaluator the measured far residual equals the series plus the drift constant to
  2e-3 at 3e4 and 1e5 L (the agreement to 1e-3 out to 3e6 L stated in 4.5 is on the lead's evaluator).
- 18:42 verifier audit of the first port of section 4 into this report and of the first version of section 5: confirmed
  subject to corrections of the far-field paragraph and of four items of section 5, all applied; the reading of the
  domain rule was corrected to two-sided (17:35 entry).
- 19:03 verifier evaluation of the second domain column: the candidate continued for 20750 iterations at the same c_l
  with residual rows r < 300 L and its own inverse on r <= 333 L with the two-term closure beyond, the same further
  budget as the 90 L column.
  - By the domain rule, read two-sided, it agrees on the lead's evaluator (2 <= r <= 10: 0.74 and 0.72;
    10 <= r <= 100: 0.86) and on two of the verifier's three configurations; on the third (16875 x 512) its 2-10
    maximum is 0.62 times the candidate's, on the low side, as for the 90 L column: there both columns' 2-10 maximum
    is the lobe above P, which no column moves, while the candidate's is next to P. The verifier's ratios are 0.99,
    0.62, 0.74 on 2 <= r <= 10 and 0.89, 0.76 (0.79 with the columns next to the y-axis cut), 0.96 on 10 <= r <= 100;
    h(P) - 1 = 5.1e-8 and -3.1e-9 on the configurations with 16875 or more radial points. No domain column run by then
    (90 L, 300 L) is higher than the candidate by more than the factor 1.5 in the bands of the rule (largest ratio
    1.23).
  - Domain against budget: next to P the 300 L fit is 0.57 to 0.59 times the candidate's and its 857-label J 0.59
    (0.56 at eps 0.01), against 0.32 to 0.33 and 0.40 for the 90 L fit at the same budget. In the closed problems the
    near-P gain at that budget grows as the domain shrinks; the budget part for the full-plane problem is not measured
    by these columns.
- 19:10 verifier audit of this report's update: confirmed except two items, both corrected. The decomposition of the
  far-field band in 4.5 had omitted the third-order inconsistency, which next to the y-axis carries, with the r^(-2)
  terms, the band maximum where the first two orders cancel; the verifier withdrew its 18:33 confirmation of that
  sentence. A statement on the domain columns was restricted to the bands of the domain rule.
- 19:35 verifier evaluation of the angular row at the candidate's c_l: the fit with angular cap m <= 100 continued for
  20750 iterations at that c_l, read with the m <= 150 and m <= 200 fits (the last 20750 iterations of each at the
  fixed c_l) by the rule fixed before the runs (none of whole-box N_f, N_f within 0.5 of P, N_v for r <= 1000, N_v
  for r > 1000 and the 857-label J increases from one row to the next by more than the configuration spread).
  - For m <= 100, 150, 200 at 16875 x 512 (J at 16875 x 384): whole-box N_f 3.11e-6, 1.43e-6, 6.84e-7; N_v for
    r <= 1000 8.74e-7, 4.00e-7, 1.92e-7; N_v for r > 1000 1.325e-6, 1.11e-6, 1.10e-6; J 5.28e-6, 3.14e-6, 1.39e-6.
    Every quantity decreases at both steps on both configurations measured, the far-field N_v maximum at the last step
    by about the configuration spread. The m <= 250 refinement row has not run.
- 19:54 verifier evaluation of the radial companion: the fit with 244 radial functions at angular cap m <= 100,
  continued for 20750 iterations at the candidate's c_l, against the 375-function fit of the 19:35 entry. The
  375-function fit is lower in whole-box N_f (0.83 to 0.86 times), next to P (0.95), in N_v for r <= 1000 (0.83 to
  0.85) and in J (0.95); N_v for r > 1000 is equal within the configuration spread, and 6.4 percent higher at
  375 with the columns next to the y-axis excluded. No reading of this pair was fixed in advance; it is reported as
  data.
- 20:03 verifier audit of this report's updates from 19:10 on: confirmed except three items, all corrected: three
  values of the m <= 150 fit rounded up in the third digit, the last far-field step of the angular row described as
  smaller than the configuration spread (it is about equal to it), and the description of the two m <= 100 rows.
- 20:44 verifier evaluation of the domain row fitted to 9000 L (X3 continued for 20750 iterations at its c_l with rows
  to 9000 L and the inverse domain and two-term closure at 1e4 L; not a candidate), read by the rule fixed before the
  run and its addition fixed before the run. Interior: the domain rule holds except at one configuration, where the
  2-10 maximum is lower than the candidate's by more than the factor (0.66), the pattern of the other two domain rows.
  Far band: over 1000 L to 9000 L the N_v maximum falls to 0.028 to 0.029 of the candidate's on both configurations;
  beyond 1e4 L it falls to 0.035 with the formula continued, while the fit's own closure there reads 25 times the
  candidate's value. The first-order mismatch coefficient at the y-axis is 0.035 of the candidate's, and the second-
  and third-order coefficients changed with it (the second-order one to 0.17 of the candidate's, the third-order one
  to the opposite sign); the fall is not the removal of the first-order term alone. The candidate's far-band value is
  therefore that of the unfitted continuation of its formula. Whether the rows or the 20750 further iterations
  produce the fall is not separated by this row.
- 21:02 verifier audit of this report's text on the domain row fitted to 9000 L: confirmed except two items, both
  corrected: one sentence of the 20:44 entry as first written attributed the fall to the removal of most of the
  first-order inconsistency (the higher orders changed as well and set the row's band value), and one comparison of
  an implied velocity change normalized like N_v with the candidate's N_f maxima (its N_v maxima were added); two
  optional wordings were adopted.
- 21:24 verifier closure row measured directly on the candidate (two grids of the separate evaluator): the changes of
  the residual between the fit's inverse convention and the formula continued are those of the earlier row to two
  digits; relative to the candidate's band maxima they are 0.8 percent next to P and 1.5 percent at 2 <= r < 10, but
  22 to 47 percent in N_v at 10 <= r < 1000, so the earlier row's percentages do not transfer beyond r = 10; in
  section 4.4 the sentence carrying them over to the candidate was replaced by the candidate's own numbers, and the
  earlier row keeps its own percentages.
- 21:28 verifier audit of the corrected text of 21:02: confirmed; one rounding and two optional precision notes (the
  column range next to the y-axis, and the row values against their radial windows) were adopted.
- 22:24 verifier audit of the text of 21:24 and 21:28 and of the record of the later reading rules in the
  specification: confirmed; the record of one control's reading omitted that it holds on both configurations with
  16875 or more radial points and that the first-order far-field coefficient is computed as for the 9000 L row; both
  were added, with two optional precision notes.
- 22:28 verifier measurement of the m <= 250 refinement row (not a candidate): the row m <= 100, 150, 200, 250 meets
  the reading fixed before the runs; with the evaluation columns next to the y-axis excluded (shown there to be the
  evaluator's floor on two angular resolutions) its interior maxima are 0.33 to 0.74 times the candidate's and its J
  0.36 to 0.37, and beyond r = 1000 it is 0.23 to 0.44 percent above the candidate. The deliverable does not change.
  The row has 20750 iterations more than the candidate; its comparison at equal budget was open (23:07).
- 22:38 verifier audit of the text of 22:24 and 22:28: confirmed with four range or wording corrections (the far band
  of the m <= 250 row is 0.23 to 0.44 percent above the candidate's rather than within 0.4 percent of it; the
  agreement of the two angular resolutions next to the y-axis, the ratio to the candidate there, and the column of the
  far-band maximum), all applied; the centre values of the m <= 250 row were measured and are the candidate's.
- 23:07 verifier measurement of the budget row (the candidate continued 20750 iterations on its own rows; not a
  candidate): 0.61 to 0.74 of the candidate in whole-box N_f, 0.50 to 0.54 within 0.5 of P, 0.48 in J, unchanged
  beyond r = 1000 (within 1 percent). By the readings fixed before it ran, the far-band fall of the 9000 L row comes
  with its rows, the 300 L row's near-P gain is that of the budget, and the 90 L and 9000 L rows' ratios to it are
  stated; at equal budget the m <= 250 row equals the budget row to 3.2 percent at the lobe above P on the sampled
  grids (to 4 percent over four radial sampling phases, 23:35) and is lower next to P and away from P. Sections 4.2,
  4.3, 4.4, 4.5 and 4.8 were updated.
- 23:18 verifier audit of the text of 23:07: confirmed with two wording corrections (the lobe ratio 0.98 is at one
  radial sampling; the 90 L and 9000 L ratios lie outside the interval on all three and on two of the three
  configurations), both applied. The near-P maximum of the m <= 250 row on the first column off the x-axis was shown
  to be a value of the row (same sign and size on three angular resolutions), not an evaluator floor.
- 23:35 verifier scan of four radial sampling phases at 16875 x 512 for the candidate, the budget row and the m <= 250
  row: the lobe value above P is common to the three within 4 percent (the lobe maximum moves with the sampling by 9
  to 12.5 percent on each row, and lies about 4 percent higher, 3.7 to 4.5, at 22500 x 512); the near-P maxima are
  phase-stable for the candidate and the budget row (within 1 percent), and the m <= 250 row's narrow value on the
  first column off the x-axis varies by 21 percent, the unshifted grid giving the largest, so the near-P ratios stand.
  The whole-box maxima of the budget row and of the m <= 250 row are this lobe value. Sections 4.2, 4.4 and 4.8 were
  updated.
- 23:38 verifier audit of the text of 23:07 to 23:35: confirmed with two corrections (the lobe at 22500 x 512 lies 3.7
  to 4.5 percent higher, not 4 to 5; the raised cap lowers the lobe above P by at most 4 percent over the sampling
  phases, so the lobe is not unchanged by the cap), both applied.
- 23:41 verifier evaluation of B_3 along the rows (its estimator on axis traces from its own inverse; the lead's
  values were reproduced to all printed digits with the same code and traces, a reproduction, not an independent
  recomputation): the medians of the integration-by-parts form are 0.2985 to 0.3012 on the angular row m <= 100 to
  250, on the budget row and on the 9000 L row (original form 0.3002 to 0.3044; method spread within one row up to
  0.0035 and 0.015); each step along the angular row is within the method spread, and B_3 is about 0.30 on every row.
  Item (ii) and 4.1 were updated.
- 2026-10-19 00:16 verifier finding that the report gave normalized residuals only: the maxima of |R| itself by
  region, with the size of rho as a scale, and the absolute elliptic residual were measured and added to 4.4.
- 00:32 verifier audit of the text of 23:41 to 00:16: confirmed as to content, with two formatting corrections, one
  label (the far-band ratios of the angular row are over all evaluation columns), one sentence of the definition of
  the standard ("Absolute values are reported too") and one range ("to 6 percent"), all applied.
- 00:34 verifier check, item by item, of an external referee report on the text of 23:41: three conditions missing
  from statements of section 3 (the velocity bound of R1 holds for 0 < gamma < 1, the range used in R2; R7 and the
  parts of R10 with three y-derivatives need C^3 axis data; the limit statement of R11 needs a finite zero set of the
  limit field), one notation (|cos theta|), one missing quantity (the trial's own B_3 coefficient, +0.046 against the
  estimator's 0.30), a reading of the domain fits under the canonical velocity law (measured by the verifier), and
  wording items. None changes a number of the candidate or the choice of X3. Applied in sections 3, 4 and 5.
- 00:41 verifier measurement of the free control of the m <= 250 row (not a candidate): c_l 5.5763706 (drift -6.0e-7
  in 20750 iterations, toward the fixed value). Against the m <= 250 row the whole-box and r <= 1000 maxima agree to
  about 1 percent with differences of both signs inside the configuration spread, the free control is lower next to P
  and beyond r = 1000, the fixed row lower in J; by the selection rule the free control wins the pair on differences
  below the resolution of that maximum. Recorded; the deliverable does not change. With the columns next to the y-axis
  excluded the candidate's far band is 0.4 percent above its control's, about twice the spread between configurations;
  4.1, 4.3 and 4.4 were updated.
- 00:56 verifier audit of the candidate continued for 20750 iterations on its own rows with the inverse domain and
  two-term closure moved from 1000 L to 1e4 L (not a candidate; reading fixed before the run): over 1000 L to 9000 L
  its far band is 0.266 to 0.273 of the candidate's on both configurations with 16875 or more radial points, the
  branch "falls"; C at the axis -0.024 of the candidate's; its whole-box and near-P maxima are the budget row's to 2
  percent (J to 8 percent). Of the fall of the 9000 L row to 0.029, the inverse domain with its closure gives the
  factor 0.27 and all of C at the axis, the rows the remaining factor 0.10 to 0.11. This refines the reading of 23:07
  (the fall "comes with its rows"): the fall is not attributable to the rows alone. Two wording corrections of the
  prepared text, both applied; 4.1, 4.3, 4.4 and 4.5 were updated. It changes neither the candidate nor its interior
  values.
- 01:13 verifier diff audit of the report as revised at 01:01 (17 items): confirmed in content, with two corrections
  (the component tests quoted in 4.6 belong to the compactified discretization of the same workstream, replaced by the
  disk discretization's own validation; one range in 4.5) and one wording correction in 4.8; applied.
- 01:15 verifier reading of the fixed-c_l fit at d = -2e-3 from F0 on the m <= 150 basis (rule fixed before the run):
  L2 objective 0.926 of F2's, whole-box N_f 0.865 / 0.869, J 0.865 / 0.859, |h(P) - 1| <= 2.8e-7: "not determined at
  this level". It widens the quoted c_l interval down to 5.5743631. At equal budget the profile over d = -2e-3, -1e-3,
  0 is monotone in every measured quantity, so the lower end of the tested span is not bracketed by this fit; two
  fits further down were requested (4.3).
- 01:16 external referee audit of the identity relating the two B_3 measurements of a trial (4.1): with the function
  H of R10 the defect term combines the trial's defects in the y and y^3 coefficients of the equation on the x-axis;
  correct under conditions the trials satisfy (g > 0 on (0, x*], even expansions of g/x^2 and |w|/x at 0). The
  wording of 4.1, 4.8 and (ii) was corrected accordingly; no value changed.
- 01:38 verifier reading of the fixed-c_l fit at c_l 5.5783631 (d = +2e-3) from F0 on the m <= 150 basis: L2 objective
  1.078 of F2's, whole-box N_f 1.138 on both configurations, J 1.159, |h(P) - 1| <= 8.2e-8: "not determined at this
  level". It widens the quoted c_l interval up to 5.5783631. At equal budget every measured quantity increases with
  c_l over the four rows from 5.5743631 to 5.5783631 (4.3).
- 01:51 verifier diff audit of the report as revised at 01:22 (6 items, including the identity of the 4.1 remark and
  its conditions checked on the candidate's axis traces): confirmed.
- 02:45 verifier reading of the fixed-c_l fit at c_l 5.6004662 (d = +2.4e-2) from F0 on the m <= 150 basis: L2
  objective 2.036 of F2's, flattened (-0.49 percent over the last 1000 iterations), N_f within 0.5 of P 2.915 and
  2.914 of F2's: "excluded at this level". It does not widen the interval. The test of 4.8 fixed before the run (ratio
  to the free fit against the reference on the 244-function basis) is undecided at 2.036.
- 02:57 verifier reading of the fixed-c_l fit at c_l 5.5723653 (d = -4e-3): L2 objective 0.858 of F2's, whole-box N_f
  0.711 / 0.713, J 0.707, |h(P) - 1| <= 3.6e-7: "not determined at this level". It widens the quoted interval down to
  5.5723653; the objective still falls toward smaller c_l there, and the fit at d = -8e-3 was run (4.3).
- 03:11 verifier check of an external referee's reading of the fixed-c_l profile: at equal budget the free iteration
  did not move c_l toward the lower objective (its c_l stayed in [5.5763641, 5.5763716] over 20750 iterations), so
  F2's exponent is set by its start at this budget and is not a minimizer of the objective; the experiment that would
  separate a family of profiles from an isolated profile (fixed-c_l fits at separated exponents through nested
  discretizations) is not in the data. Two conditions for the endpoint followed: the wording of 4.1 (evidence
  consistent with existence; neither the proximity of an exact profile nor its exponent is established) and the
  statement in 4.3 that the fixed-c_l fits below F2's exponent reach lower objectives than F2 at equal budget. Both
  were applied; the missing experiment is named in 4.8 and section 5.
- 03:48 verifier reading of the fixed-c_l fit at c_l 5.5793640 (d = +3e-3): L2 objective 1.115 of F2's, whole-box N_f
  1.213 / 1.214, J 1.224, |h(P) - 1| <= 5.5e-8: "not determined at this level". It widens the quoted interval up to
  5.5793640, the largest value tested on the candidate's radial basis that is not excluded; the next value tested on
  it, 5.6004662, is excluded at this level (4.3).
- 04:01 verifier reading of the fixed-c_l fit at c_l 5.5683739 (d = -8e-3): L2 objective 0.741 of F2's, whole-box N_f
  0.566 / 0.427, J 0.388, |h(P) - 1| <= 4.5e-7: below the 30 percent band of the rule on the low side, so "undecided
  at this level" by its letter; it widens the quoted interval down to 5.5683739 and does not bracket the lower end. On
  16875 x 512 its whole-box and near-P maxima are 2 percent below the candidate's and its J is lower, on a smaller
  angular cap; the report does not say that the candidate has the smallest residual maxima among the fits computed.
- 04:03 verifier endpoint statement: the YES endpoint for P_2, as numerical evidence and not a proof, meets the
  standard as written, on conditions carried by the text: the wording of 4.1 and (iv) (the exponent is not determined;
  the interval and its lower end as measured), the statements of 4.3 on the fixed-c_l profile, the limits of 4.8 and
  section 5 (the family and isolated-profile pictures not separated), the status line and timing, the artifacts, the
  variant spread of the independent discretization (4.6), and a diff audit of the final version.
- 04:07 verifier location of the whole-box N_f maxima: within 0.5 of P at 16875 and more radial points on every
  audited fit except the fixed-c_l fit at d = -8e-3 (0.57 left of P on the x-axis side); at 11250 x 384 the candidate
  and that fit have it at the under-resolved off-axis lobe of 4.3.
- 05:03 verifier reading of the fixed-c_l fit at c_l 5.5604082 (d = -1.6e-2): L2 objective 0.643 of F2's, whole-box
  N_f 0.716 / 0.485, J 0.514, |h(P) - 1| <= 6.9e-7: "undecided at this level". It widens the quoted interval down to
  5.5604082. The L2 objective is below that of the fit at d = -8e-3, its residual maxima and J are above it, so the
  lower end is not bracketed; among the tested exponents the residual maxima are least at 5.5683739. Its residual
  maxima are above the candidate's on both configurations.
- 05:51 verifier reading of the equal-budget free control of the fixed-c_l fit with rows to 9000 L (a data row, not a
  candidate): its c_l moves by -1.5e-6 over 20750 iterations, its far bands are within 4 percent of the fixed-c_l
  fit's, and the fixed-c_l fit is 0.93 to 0.94 times it within 0.5 of P and in J, as the candidate is against F3
  (4.5).
- 06:06 verifier reading of the fixed-c_l fit at c_l 5.5524653 (d = -2.4e-2): L2 objective 0.775 of F2's, whole-box
  N_f 1.139 / 1.159, J 1.158; |h(P) - 1| is 1.46e-6 at 11250 x 384 and 2.6e-7 at 16875 x 512, so "undecided at this
  level" by the letter of the rule ("not determined" with h(P) at 16875 or more radial points). It widens the quoted
  interval down to 5.5524653. Its L2 objective and whole-box N_f are above those at 5.5604082, so the lower end is
  bracketed at this budget in the sense of fits from transplanted starts; that fit had not flattened, and its L2
  objective is below F2's while its residual maxima are above F2's (4.3).
- 06:23 verifier diff audit of section 4 with the fixed-c_l profile: every number confirmed; four wording
  corrections required and applied: the computation does not determine c_l (the tested exponents not excluded span an
  observed interval), the class statement aligned with 4.1, the stored exponents of the profile given to within 8e-7,
  and the selection rules stated with their budgets (4 (iii), (iv), 4.3, 4.8).
- 06:23 verifier check of an external referee's hostile audit of the 04:03 endpoint statement: its checkable
  claims confirmed. One clause of that statement was an overstatement: an attained objective bounds the objective
  minimized over shapes only from above, so the fits do not show that a computed c_l fails to minimize it; corrected
  to the wording of 4.3 ("set by its start, not by a minimum of the objective"). The artifacts did not yet contain the
  coefficient files and code of the GPU fits; they were added (section 5).
- 06:36 verifier diff audit of those corrections and of the suggested wordings (the scope of the table and the basis
  of the interval in 4.3, two statements in 4.4b and two earlier entries of this timeline): confirmed; no measured
  value changed. Check of the artifacts as then assembled: the coefficient files of the candidate and its control are
  byte-identical to the audited files, and from a copy of the artifacts the packaged evaluator and the lead's scan
  reproduce the recorded outputs on the candidate (every field identical except the timing and the file name).
- 07:12 and 07:16 verifier diff audits of presentation corrections (item references and point counts in 4.1, the
  wording of the P_inf clause (4.1) and of the domain ordering (4.4), the definition of equal budget and the column
  scaling of the LSQR iterations in section 5): confirmed with one correction, that the free control F1 ran its 750
  CPU iterations in one linearization, not two; applied. No measured value changed.
- 07:55 verifier reading of the nested pair: the fixed-c_l fits at 5.6004662 and 5.5683739 continued from the m <= 150
  basis to the candidate's m <= 200 basis at the candidate's iteration count. At 5.6004662 the L2 objective is 1.680
  times F3's, between the thresholds 1.36 and 3.05 fixed before the run, so the step is undecided and the family and
  isolated-profile pictures are not separated; its N_f within 0.5 of P is 2.41 and 2.50 times F3's, so it is excluded
  at this level as on m <= 150, and the interval is unchanged. At 5.5683739 the L2 objective is 0.820 times the
  candidate's, N_f within 0.5 of P 0.59 times and J 0.56 times; its whole-box N_f is 1.32 times the candidate's at
  11250 x 384 (the under-resolved off-axis lobe) and 0.69 times at 16875 x 512 (4.1, 4.3, 4.8).
- 07:57 verifier diff audit of that correction: confirmed; no measured value changed.
- 08:09 and 08:21 verifier diff audits of the nested-pair statements: confirmed with two corrections, applied: the
  upper end of the tested values not excluded is stated as a reading of tested values (on the candidate's radial basis
  the largest tested value not excluded is 5.5793640 and the next tested value, 5.6004662, is excluded), in item (iv)
  of section 4 and in the 03:48 entry; and one digit of a quoted maximum in the nested-pair table of 4.3. No other
  quoted value changed.
- 09:36 verifier reading of the 9000 L row continued for a further 20750 iterations at its c_l (a data row, not a
  candidate): its N_v maximum over 1000 L to 9000 L is 1.028 and 1.024 times that row's, in [0.8, 1.25] by the rule
  fixed before the run, so the further budget does not lower the far band; within 0.5 of P it is 0.61 and 0.58 times
  and in J 0.58 times that row's (4.5).
- 10:10 verifier reading of the m <= 250 row continued for 20750 iterations with rows to 9000 L and the inverse domain
  and closure at 1e4 L (a data row, not a candidate): whole-box N_f 1.02 times and N_f within 0.5 of P 0.67 and 0.71
  times the m <= 250 row's, so by the rule fixed before the run the interior gain of the cap is kept with rows to
  9000 L; over 1000 L to 9000 L its N_v is 0.61 times that of the 9000 L row continued for the same total iterations,
  outside [0.8, 1.25], so the ratio is stated; the difference sits next to the y-axis at the inner end of that band
  (4.4).
- 10:20 verifier diff audit of the statements on the two data rows: confirmed with one correction, applied (a clause
  on the far band of the m <= 250 row continued is replaced by the two maxima measured, 4.4); the statements of (iv),
  4.1 and 4.3 on the tested exponents and on the fits lower than the candidate checked over the whole text with both
  rows included. Two suggested wording changes applied: the rows continued beyond the candidate's budget that are
  lower in whole-box N_f are named in section 4, and the 13:41 entry reads "of the fits measured by then".
- 10:27 verifier diff audit of those changes: confirmed with one correction, applied (the sentence on the rows
  continued beyond the candidate's budget now gives the column convention and names all eight rows that are lower in
  whole-box N_f at the configurations with at least 16875 radial points).
- 10:29 verifier diff audit of that correction: confirmed.
- 10:30 verifier check of the accompanying artifacts against the report (interim): every file unchanged since the
  08:31 check, and the candidate's scan and residual audit reproduced from a fresh copy; for the final assembly it
  listed the coefficient files of the nested pair and of the two data rows with the log lines of their runs, the final
  copy of the verification record, and the fits to be named in section 5 (a).
- 10:42 verifier check of an external hostile-referee pass on the report: no sentence found that calls the numerical
  evidence a proof, claims convergence to an exact profile or a determined exponent, or says that X3 has the smallest
  residual; the headline numbers consistent. Three corrections required and applied: no definite article for an exact
  profile whose existence is not established (item (ii) of section 4 and 4.1), three upper bounds that had been
  rounded down (4.1, 4.5), and the far-field N_v range of 4.8 restricted to the fits with rows only to 900 L. Three
  recommended wording changes applied (4.1, 4.4b).
- 10:46 verifier check of an external reproduction from the accompanying artifacts: the md5 of the candidate and its
  control, the identity, the root of h(P) = 1, x* and the centre relations reproduced; the residual scans did not run
  under a 2 GB memory cap (a memory failure, not a disagreement; they ran and reproduced the stored outputs under the
  limits of this run). The exit statuses of two evaluator wrappers corrected (numerics unchanged). The software
  versions, the thread setting and the time limits of the wrappers added to section 5.
- 11:06 verifier reading of the fits at 5.5604082 and 5.5524653 on the m <= 150 basis, each continued for a further
  21500 iterations at its exponent (43000 in all): L2 objectives 2.2009e-6 and 2.2121e-6 (ratio 1.005), whole-box N_f
  1.167e-6 and 1.344e-6 at 11250 x 384 and 6.311e-7 and 1.301e-6 at 16875 x 512; by the rule fixed before the runs the
  lower-end bracket is kept at twice the budget. The L2 margin shrank at every linearization (from 5.63e-7 to
  1.12e-8), so the order in L2 is a fact at this budget only. Identity c_l to 3.2e-9 on both, centre relations and the
  condition (Hmin) of R9 checked. The fit at 5.5604082 is below the candidate in whole-box N_f at 16875 x 512 (0.922
  times) and in J (0.800); it is named in 4.1 (not an equal-budget comparison, not a candidate).
- 11:21 verifier diff audit of the presentation rounds and of the reading of the two continued lower-end fits:
  confirmed, with four corrections required and applied: 4.1 names the evaluator whose maxima the bounds 7.2e-7 and
  2.01e-7 are and gives what the lead's scans read in the fit's own convention (6.94e-7 and 7.27e-7 in N_f next to P;
  the same in section 5 step 3); the sentence on the shrinking L2 margin restricted to the complete linearizations;
  two ratios of 4.1 rounded correctly. The bounds 1.112e-6 and 1.324e-7 confirmed for both evaluators.
- 11:31 verifier measurement of the peak memory and wall time of the commands of section 5 steps 1 to 3 on a fresh
  copy of the accompanying artifacts, under an address-space limit of 15.3 GiB: 13.8 GiB for the residual tables at
  16875 x 768 (the configuration with the most evaluation points), at most 7.5 GiB for each command of steps 2 and 3,
  the stated wall times met, every output equal to the stored one. The memory statement added to section 5.
- 11:49 verifier measurement of the three remaining configurations of step 1 (16875 x 384, 16875 x 512, 22500 x 384):
  7.0, 9.2 and 9.2 GiB, the stated wall times met; the outputs at 16875 x 512 and 22500 x 384 equal the earlier ones,
  16875 x 384 had none. The reference outputs of steps 1 and 2 added to (d).
- 11:59 verifier final entry on the report of 11:50:47Z and the accompanying artifacts of that time: the endpoint of
  section 4 confirmed as meeting the standard, with all its stated conditions met.
- 12:04 end of the run (T_end). For publication the accompanying artifacts were reduced to the material the report
  relies on, under 50 MB: the run records (work logs, job drivers and queues, per-run solver logs) and the start files
  of continued fits were left out, the larger scan outputs were compressed, a solver restart vector was removed from
  the coefficient files other than the eight named in section 5 (a), directory prefixes of the machine were removed from
  the scripts and records, and a README with the map of fit names and the commands was added. Section 5 was adjusted
  to describe this. No number of sections 1 to 4 changed.
- 2026-10-20 00:46 start of the follow-up investigation on the strong setting P_inf (section 6; T0 = 00:46:19Z).
- 00:55 to 01:01 verifier validation of its separately written tools for section 6. Generator of the trial from the
  coefficient vector alone: relative difference 7.8e-14 from the published implementation. Full-plane inverse by
  spectral-element collocation of the modal equations in log r, with exact radiation conditions: relative errors
  2e-13 to 2e-12 against quadrature of the Green function. Two-dimensional pipeline with three formulas for
  psi_xy(0): on a manufactured solution, U to 3.2e-12 relative and c to 1e-15, 4e-11 and 7e-9 relative.
- 01:05 verifier recomputation of X3 at four discretizations (6.2): max R/N_f 6.8e-7 to 7.3e-7, next to the x-axis 0.1
  from P; max R/N_v 1.10e-6; the identity for c_l, x* and h(P) - 1 as in 6.2.
- 01:26 external referee audit of the coupled high-frequency packets at P: their construction confirmed in adapted
  coordinates; conclusions about a Fredholm index drawn from them refuted.
- 01:45 verifier recomputation of the source quantities g(P), lambda_P and (1 + g(P))/A of X3 from its own axis
  velocity: agreement to 6 digits.
- 01:50 verifier trial-data estimates of B_3 on X3 from its own axis velocity together with the trial's g: nonzero,
  0.30 +- 0.03 natural units (narrowed at 02:48; final range 0.31 +- 0.015 at 05:16).
- 01:55 to 02:00 verifier audit of the axis hierarchy of 6.3.1 (a), by hand derivation and symbolic checks: confirmed,
  under conditions (C1) and (C2) for the boundary value at P; the conormal balance mu_j and the coupled packets of
  6.3.1 (d) confirmed as formal leading-order statements.
- 01:56 external referee audit: B_j as functionals of (c_l, w); condition (C2) weakened to (C2') with explicit H_j; the
  exact local pair of 6.3.1 (c); a proof of NO_inf must use the canonical velocity law. [Corrected 2026-10-20: as stated
  at 08:44, the exact local pair shows only that a proof of NO_inf must use a further property of admissible profiles,
  such as the growth bounds or the canonical velocity law.]
- 02:12 external referee audit of the linearization at a profile and of its parametrization by data at P (question
  Q1): the source-motion identity and the torus example of 6.3.1 (d); Q1 not decided.
- 02:35 verifier audit: the exact local pair of 6.3.1 (c) confirmed symbolically; explicit H_j and condition (C2')
  confirmed; the example of 6.3.1 (b) confirmed; the linearization of 6.3.1 (e) confirmed, its normalization corrected
  at 02:54.
- 02:41 external referee audit of (C1), (C2') and compatibility at all orders: a proof of (C1) by propagation of
  regularity (under verifier audit, 6.4); (C2') open at the coupled level; the conditional statement of 6.4.
- 02:48 verifier: second axis inverse (quadrature of the modal Green functions), and validation of the B_3 estimator
  on exact data (6.3.2 (a)) to 1e-6. One form of an estimator was found to use a faulty homogeneous solution and was
  corrected. B_3 on X3 narrowed to 0.31 +- 0.01 (6.2, corrected item; widened at 05:16 to 0.31 +- 0.015 under a
  stricter rule for the fit windows).
- 02:49 verifier: axis hierarchy to order y^7 (F_5 and F_7) confirmed symbolically.
- 02:50 verifier reading of the singular-value study of the discretized linearization at X3 on three grids (Q1):
  "undecided" by the rule fixed beforehand. Its preconditions were not met (base states not stationary, one domain),
  and the smallest singular value on the finest grid is at the floating-point floor. A reading "non-Fredholm" was
  refuted as premature.
- 02:52 external referee audit of the conditioning of the obstruction functional: threshold of 7 + beta derivatives of
  w at the origin, an explicit discontinuity at that threshold among compatible axis data, and an adjoint
  representation of B_3 (6.4).
- 02:54 verifier audit of the source-motion identity, of the coupled packets at P (C^3 at X3) and of the torus
  example (6.3.1 (d)): confirmed. Correction of the normalization of 6.3.1 (e) to dC = d rho_y(P) + p g'(P).
- 03:00 verifier recomputation of the exact first-order responses of 6.3.2 (c): confirmed to the digits quoted
  (the entry at sig = 1, x0 = 1 to all three digits at 03:29, with a smaller fit window).
- 03:06 verifier recomputation of the response along the analytic direction of 6.3.2 (c): the verifier's estimator
  value 948.8446 natural units, against the lead researcher's 948.844 (the fit-free exact value of 05:16 is
  948.84165).
- 03:16 external referee audit of the endpoint condition (C2') at P: the frozen-coefficient solution of class
  C^(2, 1 - 2/A) with G_3/H_3 -> 1/(12 sin(2 pi/A)) (6.3.1 (g)) [Corrected 2026-10-20: with H_3 normalized as in 6.3.1
  (a) the limit is 1/(12 sin(2 pi/A) g*^(3 + 2/A)); 1/(12 sin(2 pi/A)) is the coefficient of |s|^(-2/A) in G_3];
  sufficient conditions for (C2'); the sign of the condition at 0 for l_3 != 0. The lead researcher checked the
  solution's constant and exponents symbolically and by quadrature.
- 03:17 verifier audit of the proof of (C1) (6.3.1 (f)): confirmed at the level of a referee report, every order count
  checked; one positive-commutator estimate is cited from the literature and was not checked against the source. [That
  estimate is no longer used: 6.3.1 (f) as revised at 11:01.]
- 03:17 verifier audit of the thresholds at P, the transport lemma at P, the sufficient condition for (C2') and the
  theorem of 6.3.1 (f): confirmed, given (C1); for j >= 5 the endpoint condition is needed for every odd i <= j
  (i >= 3).
  Two arithmetic values of that audit were corrected at 03:27 (an input truncated); the report's values were right.
- 03:17 verifier check of the origin expansions and of the leading-order conditioning law (6.4): confirmed.
- 03:29 verifier: the conditioning law at smaller x0 (ratio of exact response to law about 1 + 0.012 x0^2 for x0 from
  0.125 to 1), the closed form of 6.3.2 (a) exact to 40 digits, and a diff audit of 6.2 to 6.4 and of this timeline
  from 00:46: eight points, none changing a conclusion, all applied (two wording corrections in 6.2; (C1) and the
  theorem moved from 6.4 to 6.3.1 (f)).
- 03:36 external referee audit of the endpoint condition above the exponent 1 - 2/A (6.4): the frozen theorem and its
  sharpness, a thin-layer example showing that bounds on the nonlinear remainder do not suffice, existence of the
  limit l_3 for exact profiles above that exponent, the thresholds for higher odd jets and a fifth-jet frozen
  solution. The lead researcher checked the conjugation identity, the homogeneous solutions, the thresholds and the
  fifth-jet constant symbolically and numerically, and the existence proof for l_3 by hand.
- 03:36 verifier: an independent evaluator for the numerical researcher's states, validated on an unconverged state.
  The identity defect is reproduced exactly; h(P) - 1 from the exact inverse is 6.0e-4, against 1.0e-5 from the
  solver's own discrete inverse. The solver's inverse at P must be refined before h(P) = 1 is read from it.
- 03:42 verifier audit of the frozen solution of 6.3.1 (g) (equation, constant by a separate route to 20 digits,
  regularity and one-sided smoothness) and of the sign B_3(c_l, w) = -l_3: confirmed. Diff audit of 6.3.1 (f): nothing
  beyond the earlier audits; two wording points, applied.
- 03:55 external referee audit of the obstruction functional at nonsmooth data and of the structure at the saddle
  (6.3.1 (g), (i) and 6.4): continuity in the norm of the 7-jet, the weighted origin remainder and C^(2,theta) control
  on the full interval [r, x*], existence of C_0 and l_3 from the axis trace, the velocity coefficient of an isolated
  saddle mode, a family of frozen solutions at P, and why a parameter count from frozen modes is not available. The lead
  researcher checked the identities symbolically (stream functions, axis equation, linear saddle classification,
  logarithmic resonance, the family's Euler identity and inequalities) and the convergent form numerically against the
  exact closed form (15 digits).
- 04:02 external referee audit of the nonlinear endpoint condition (6.3.1 (h)): for an exact profile of P_inf (smooth
  near every point of the open axis segment) that is C^(2,alpha) near P with alpha > 1 - 2/A, a transverse bound at P
  from the transport equation and the constant divergence of W, giving l_3 = 0. The lead researcher checked the
  underlying identity symbolically for arbitrary fields, a model case, and the cone estimates and stopping-time
  exponents by hand.
- 04:14 verifier check of the remark on conormal modes at P (6.3.1 (h)): confirmed for l_3, and extended: these modes
  change none of l_3, l_5, l_7, while for j >= 9 the mode of order j - 8 enters G_j/H_j at relative order
  |s|^(-0.28); the statement C^(2, mu_j - 2) holds for 2 < mu_j < 3 (j = 1 to 9 at X3; corrected at 05:16 from
  j = 3 to 9).
- 04:19 verifier check of the nonlinear endpoint theorem (6.3.1 (h)): confirmed at the level of a referee report (the
  identity symbolically for arbitrary fields, its leading coefficients on generic Taylor data, the exponent windows;
  the characteristic integration and the distributional steps by hand), with the order-0 mapping property of the
  velocity law and (C1) as inputs; the cone form confirmed. One correction: in two dimensions the velocity of a
  conormal mode is only C^(2, mu_j - 2) near P; the class C^(3, 0.93) holds for its axis trace (applied).
- 04:33 external referee audit of section 6 and of the interim paragraph: the conditional results supported,
  including the nonlinear theorem; corrections to endpoint and origin hypotheses, to the coefficient convention
  (C_0 = l_3 + B_3 throughout), to the higher-jet statements (conditions for 3 <= i <= j, sufficient versus necessary
  thresholds), to the conormal regularity, to the exceptional case A = 2 and the full norm of the statement on
  nonsmooth axis data, to numerical wording and to status labels. Checked by the lead researcher and applied at
  04:43. Not adopted: the referee's value 0.856947 for the regularity exponent of the fifth-jet frozen solution is
  the value at rounded parameters; at the computed parameters it is 0.85699, and the report states 0.85699.
- 04:34 verifier recomputation of B_3 on the ten stored fixed-c_l fits of the first investigation (6.3.2 (d)): 6720
  variants in [0.265, 0.472], median 0.302; the dependence on c_l is not resolved. [Corrected 2026-10-20: the ten stored
  trial traces are nine fixed-c_l fits and the free control F3.]
- 04:34 verifier check of the existence of l_3 above the exponent 1 - 2/A (6.3.1 (h), weaker statement): confirmed by
  hand.
- 04:34 verifier check of the obstruction functional at nonsmooth axis data (6.3.1 (i)): the convergent form confirmed
  by independent computation (agreement to 4e-30 on compatible axis data, and checks at A = 4 and A = 3), the
  existence of C_0 and l_3 and the relation C_0 = l_3 + B_3 confirmed, the Lipschitz estimate confirmed by hand. The
  family of frozen solutions (6.3.1 (g)) confirmed, G_3 by two routes at five values of d, with two precisions:
  d != 3 (and d != 2, added at 05:16), and at d = 3 - 2/A the left axis velocity is smooth while l_3 is finite and
  nonzero. The saddle-mode
  velocity coefficients confirmed for j = 1 to 11.
- 04:41 external referee audit of global constraints on the axis data and of a sign mechanism for B_3 (6.4): identities
  from the axis equations; the velocity law and positivity alone fix no sign of the centre jets; B_3 as an ordinary
  integral, the sufficient condition (H_-) for B_3 > 0 and the resulting nonexistence statement under (H_-); the test
  on compatible axis data (H_- exactly when L^2 >= 3A); the first-variation weight pulled back to the density takes
  both signs on every horizontal half-line. Unconditional nonexistence not proved. The lead researcher checked the
  formula, the coefficients, the polynomial remainder, the exceptional case A = 2 and the parity argument
  (symbolically and numerically, to 05:00).
- 04:44 verifier check of the frozen theorem (6.3.1 (j)): the conjugation identity and the homogeneous solutions
  symbolically, the smooth particular solution numerically, the reduction and the dyadic proof by hand; confirmed,
  also for noninteger exponents above 3 with j above the exponent. The fifth-jet frozen solution confirmed: exponent
  0.856992 at the computed parameters (0.856947 at rounded parameters), constant by a physical-space route to 15
  digits.
- 04:49 verifier check of the characterization of smoothness at the saddle and of its converse (6.3.1 (a)): confirmed
  for a given smooth field and irrational A; for coupled profiles the smooth-field hypothesis already implies the
  conclusion, so a converse from finite regularity is open.
- 05:02 lead researcher: the condition (H_-) on the ten stored fixed-c_l fits of the first investigation (6.4): the
  sampled values and fitted endpoint models are consistent with it on every trace and fit window, with a margin that
  vanishes only at x*; the ordinary integral gives B_3 = 0.29 to 0.31. No uniform sign certification; not yet recomputed
  by the verifier. [Corrected 2026-10-20: an earlier version said "holds on every trace and fit window"; the ten stored
  trial traces are nine fixed-c_l fits and the free control F3.]
- 05:16 verifier diff audit of section 6 and of this appendix: agreement with the earlier checks up to seven
  precision points, none of which changes a conclusion (the family of 6.3.1 (g) also needs d != 2; the mode j = 1 in
  the conormal remark of 6.3.1 (h); the restriction to j = 3 of a remark in the proof outline of 6.3.1 (j); A = p/q
  in lowest terms in 6.3.1 (a); three wording points). B_3 on X3 with the fit windows that are stable under the inner
  fit degree: 0.296 to 0.323 natural units, i.e. 0.31 +- 0.015 (6.2). The response of the exact functional along the
  analytic direction of 6.3.2 (c) by a fit-free evaluation at 34 digits: 948.84164773481 natural units.
- 05:26 lead researcher: reading of the sign criterion (Q is half the transverse curvature of the horizontal velocity on
  the axis over the cube of the axis density gradient), its margin on the stored fits under rescaling of the axis
  density gradient at fixed axis velocity (zero at a factor 0.249 to 0.293, per-trace medians; the normalization
  convention is stated in 6.4), and the concentration of the integral near P (6.4). Not yet checked by the verifier.
- 05:35 verifier check of the sign criterion and of the first variation (now 6.3.1 (k), (l)): the coefficients and the
  remainder symbolically for general odd w, the proof by hand, the convergent form at 30 digits against an independent
  closed form and against the finite-part value on traces outside the compatible family, the cases 1 < A < 2 and A = 2,
  the R12 statements, the first-variation weight against a finite difference (2e-23) and the pullback; the listed parts
  confirmed, in the distributional normalization of the referee's proof (the text of 6.3.1 (l) was corrected to it at
  06:01); the referees' positivity examples were not checked (6.4). Opinion on the classification: a conditional
  theorem, not NO_inf, since its hypothesis is a sign condition on the integrand of the obstruction itself.
- 05:35 lead researcher, on two further external referee audits of the sign criterion (6.3.1 (k), 6.4): the criterion
  and the conditional nonexistence statement confirmed exactly with their hypotheses; correction: (H_-) implies only
  Q(x*) >= 0, not Q(x*) > 0 (an exact trace at A = 4 with Q(x*) = 0 satisfies (H_-) strictly); weaker sufficient tests
  by primitives, tails and weighted moments, with an exact threshold on compatible data; endpoint relations at P and
  counterexamples to endpoint-sign deductions; the kernel representation of Q with its local term. Checked by the lead
  researcher symbolically and numerically. The weaker tests, the endpoint counterexamples and the kernel formula have
  not been checked by the verifier; the criterion and the conditional exclusion have (preceding entry). The
  classification of the conditional statement is disputed between the referees; the report does not count it as NO_inf.
- 05:38 lead researcher: the sign criterion and the first variation moved from 6.4 to 6.3.1 (k), (l); the parts
  not checked by the verifier (the referees' positivity examples) were moved back to 6.4 at 06:01.
- 06:01 external referee audit of the interim paragraph, 6.3.1 (h) to (l), 6.3.2, 6.4 and this appendix: the
  conditional results and the numerical comparisons supported as stated; corrections, checked by the lead researcher
  and applied: the normalization of the distribution lambda_o in 6.3.1 (l) (density lambda/2, with finite parts at
  the endpoints and the constraint terms), the normalization of the amplitude rescaling in 6.4, the statement on
  monotonicity in the NO_inf item (monotonicity of Q - P(m) is sufficient, not shown insufficient), the range of test
  (iii) on compatible data, sampled values instead of a uniform sign on the stored fits, verification labels
  (continuity in the full norm of 6.3.1 (i) was checked by the verifier; the referees' positivity examples were not,
  now in 6.4), parameter ranges (A > 2, A >= 2, computed parameters), the NO_inf convention in 6.1, and wording. The
  lead researcher rechecked symbolically the A = 4 remainder, both scaling laws and the remainder at L^2 = 4A.
- 06:14 lead researcher: second route for the sampled remainder of (H_-) on two stored traces (6.4). P was taken from a
  polynomial fit of w near 0 weighted by x^3. It agrees with the first route within 0.08 near the origin and gives the
  same signs. An unweighted fit moves the values near x/x* = 0.06 by up to +6.3. [Corrected 2026-10-20 (06:21 entry):
  the cause is not the sampling error of w but the constraint w'(0) = -A in the fit, while the traces have w'(0) + A =
  2.4e-11.]
- 06:21 verifier, with separately written code: (H_-) on the ten stored traces CONFIRMED with scope (6.4). [Corrected
  2026-10-20: what was recomputed are sampled sign diagnostics for the remainder of (H_-) under the stated origin model;
  they do not certify the uniform condition (H_-), and the model dependence is recorded in the entry of 06:27.] With two
  routes for P, the remainder is negative at every sampled point of 0 < x/x* <= 0.9995 on all ten traces, with maximum
  -2.5e-3 to -2.4e-3 at x/x* = 0.9995 (linear approach to 0 at x*, slope 4.74 to 4.99), margin at least 0.15 in natural
  units away from x*, and B_3 = 0.2945 to 0.3011 from the integral of 6.3.1 (k). The two routes agree within 0.03 at
  x/x* = 0.06 and 0.1 once the fit leaves w'(0) free. These are sampled values on trial traces, not an enclosure. The
  axis identities of the sign criterion (Q as the transverse curvature of the horizontal velocity against the cube of
  the density gradient, the forcing of the y^3 equation, the homogeneous solution H_3) CONFIRMED; the
  amplitude-rescaling law and the exact values mu_0 = S_A/L^2 and threshold 3A/L^2 on the compatible data CONFIRMED; the
  trace range of mu_0 corrected to 0.22 to 0.34 (route dependent at the 0.05 level).
- 06:27 verifier, with separately written code: the dependence on the model of w at the origin (6.4). Adding one term
  x^(k + beta) (k = 7, 9, 11) to the fit of w fits the stored traces at least as well as an extra even power; the data
  do not determine the origin model. The sampled remainder of (H_-) for x/x* >= 0.2 is negative in every model on every
  trace; on 0 < x/x* < 0.2 it is negative under the analytic model and for k = 9, 11, and positive at x/x* = 0.06 on
  eight traces for k = 7. [Corrected 2026-10-20: as stated in 6.4, on 0.06 <= x/x* < 0.2 the sampled remainder is
  negative under the analytic model and for k = 9, 11 (not for k = 7), and on 0 < x/x* < 0.06 only the analytic origin
  model gives a reading, from its series; none of these sampled values certifies a sign between the sample points.] B_3
  from the integral of 6.3.1 (k) is 0.28 to 0.30 over all models. [Corrected 2026-10-20: as stated at 07:41, these are
  sensitivity values of the estimator, obtained after the non-polynomial term is omitted from the origin series; for a
  trace that keeps a nonzero x^(7 + beta) term down to 0 the ordinary integral diverges logarithmically.] The (H_-)
  verdict of 06:21 is restricted accordingly. The amplitude-rescaling law with either normalization CONFIRMED. With the
  origin models counted, mu_0 = 0.22 to 0.37 (three traces).
- 06:38 verifier, with separately written code (exact rationals and arbitrary precision): the A = 4 trace with
  w''(x*) = Q(x*) = 0 and its remainder, the single sign change of the remainder on the compatible data of 6.3.2 (a)
  exactly for 2A < L^2 < 3A (a proof; this contains S_A < L^2 < 3A since S_A > 2A for A > 2) and its strict
  negativity for L^2 >= 3A, the moment threshold (numerically, at four exponents), and the endpoint relations at P,
  all CONFIRMED (6.4).
- 06:42 verifier, by hand and symbolically: the normalized form (m^beta Z)_m = -(1/3) m^(beta - 1) dR/dm of the y^3
  equation CONFIRMED (6.4).
- 06:45 lead researcher: the two preceding entries applied to 6.2, 6.4 and the interim paragraph.
- 06:51 lead researcher: three items added to 6.4 with their labels: a local exclusion near an explicit compatible
  trace at A = 4 and a quadrant representation of B_3 (external referee; reference value checked by the lead
  researcher); the local structure at a singular source (external referee; algebra checked by the lead researcher);
  and the general solution of the frozen equation at P in Fourier variables (lead researcher; Fourier identity checked
  symbolically; analytic steps not yet checked).
- 06:51 to 06:54 verifier, by hand, symbolically and with separately written quadrature: the kernel representation
  of Q CONFIRMED; the implications (i) to (iv) of the weaker sign tests and their coverage on the compatible data
  CONFIRMED; for the singular source, the normalization k, the degree counts and the fifth-jet resonance CONFIRMED,
  the rest OPEN as labelled; for the frozen kernel at P, the Fourier identity, the general solution and the degrees
  CONFIRMED, the regularity reading OPEN as labelled (6.4).
- 07:00 lead researcher: the preceding entry applied to the labels in 6.4.
- 07:02 lead researcher: 6.5 added, a statement of the exact remaining gap assembled from 6.1 to 6.4 (no new claims).
- 07:07 lead researcher: 6.4 "The frozen kernel at P": the argument for smoothness off P named, and the comparison
  with the full linearization in linearizing coordinates added (both not yet checked).
- 07:08 verifier: diff audit of section 6 (versions of 06:00 to 07:02, including 6.5) against the verification record:
  no discrepancy; one wording suggestion for 6.5 (nonvanishing rather than a strict sign). The A = 4 reference value
  B_3(4, w_0) = (23/110592) B(7/4, 1/2) [Corrected 2026-10-20: the first argument is c_l, so this is B_3(5/2, w_0)]
  CONFIRMED at 40 digits by two routes (exact rational remainder, negative on (0, 4)); the Lipschitz chain OPEN. The Q1
  reading of the two softest coarse directions (not near-null once the inverse is resolved) CONFIRMED in substance with
  the verifier's own residual and inverse. [Corrected 2026-10-20: what was confirmed is that the much smaller responses
  predicted by the coarse Jacobian are not reproduced with the more accurate inverse; whether these directions are
  near-null in a fixed, consistently normalized formulation is not decided, and the test gives no lower bound for the
  smallest singular value (6.4).]
- 07:16 lead researcher: external referee audit of the frozen kernel at P received and integrated into 6.4 and 6.5.
  Confirmed after corrections: the Fourier formula with the reality and moment conditions, smoothness off P, the
  regularity rule C^(m,alpha) for (m + alpha) A <= 1 + g* and failure of C^n for n A > 1 + g*, the vanishing of the
  normalized endpoint limits l_j for odd j >= 3, and a theorem that the full linearization is not upper semi-Fredholm
  from compactly supported C^(2,sigma) to C^(1,sigma). Refuted: pure quasi-homogeneity of the expansion (Taylor terms
  and logarithms occur), the bound O(|s|^((g* - 2)/A)) for the y^3 axis coefficient (its value at P can be nonzero;
  the lead researcher rederived the formula for it), the classification of all tempered solutions as stated, and a
  dilation argument for the full operator. Q1 restated as undecided in both classes; the statement that a basis smooth
  at P cannot represent the packets replaced by: contains none exactly, approximates their cut-offs. 6.5: the YES_inf
  item restated accordingly and an item on what NO_inf has to exclude added. Not yet rechecked by the verifier.
- 07:17 lead researcher: the 07:08 verifier entry applied to 6.4 (local exclusion at A = 4, Q1) and 6.5.
- 07:20 lead researcher: 6.4 "B_5 and B_7" and the 6.5 item on higher jets restated from the verifier's record of
  2026-10-20T03:13Z: B_5 is defined by the finite part of 6.3.1 (a) only where B_3 = 0, and B_7 only where
  B_3 = B_5 = 0, so they are not measurable on X3 (no change of results). [Corrected 2026-10-20: as qualified at 08:44,
  the finite-part definitions require power expansions of G_3 for B_5 and of G_5 for B_7; on the nonresonant branch near
  X3 with the relevant source limits zero this means B_3 = 0, respectively B_3 = B_5 = 0, while at a resonant order a
  smooth nonzero homogeneous term is possible (A = 2, B_5 = 11/1474560 with l_5 = 0).]
- 07:23 lead researcher: numerical check of the referee's formula for G_3(0) of a frozen packet with an imaginary even
  Phi of integral zero (A = 3, g* = 3.5): limit and s^(1/2) coefficient agree with the predictions to five digits
  (6.4, the frozen kernel at P, item (iii)).
- 07:25 lead researcher: one status sentence added at the end of the interim paragraph (Q1 to Q4 undecided; 6.4, 6.5).
- 07:41 lead researcher: integrated an external referee audit of the status block and of section 6 (a snapshot taken
  before the 07:16 edits; each finding was checked against the current text). Corrections: the parameter range of the
  family of frozen solutions in 6.3.1 (g) (d < min{A, (1 + g*)/A}; the earlier bound alone does not give lambda < 1
  when A^2 < 1 + g*); the fifth-jet frozen example of 6.3.1 (j) restricted to the computed parameters; the
  origin-model values 0.28 to 0.30 of 6.4 relabelled as sensitivity values of the estimator (the fitted non-polynomial
  term only refits the polynomial coefficients; for a trace that carries a nonzero term e x^(7 + beta) the ordinary
  integral diverges logarithmically, the lead researcher's computation); the sampled (H_-) thresholds marked as not
  certified, and the factor 2.7 to 4.5; the stored traces described as nine fixed-c_l fits and the free control F3;
  the w-only estimator wording of 6.2; the statement on l_3 as a parameter; the role of l_3 in exclusions; the 6.1
  convention restated as stricter than the task; the Q1 reading of the soft directions; the general solution of the
  frozen equation restricted to the sector odd in y; notation (natural units for B_j, the Euler beta function,
  B_3(c_l, w_0) at A = 4, the coefficients pi_j of 6.3.1 (k), t_+, t_-, eta_P[W], r in 6.3.1 (j), j = 1 + 2pn). 6.5
  was restated: the YES item (the B_3 = 0 test and l_3, the estimator spread, Q1 and Q2), the sign step as one
  sufficient route, the axis-data sentence corrected (compatible data with B_3 = 0 show that the listed identities
  alone do not force nonvanishing; an additional restriction may be expressed in axis data), the local version with
  source control, the higher jets, a Q4 item, and a new item on the range 1 < A <= 2 (in 6.4: there the Hoelder
  hypothesis of 6.3.1 (h) is part of the class, so every profile of P_inf has B_3 = 0, and at A = 2 w''(P)(g* - 2) =
  0; the lead researcher's reading, stated independently by the referee, sent to the verifier). The referee confirmed
  the sign relation of 6.3.1 (k), the closed form and zero of 6.3.2 (a) (S_A, C_A, sqrt(S_A) = 5.343575360960 at the
  computed A) and the packet regularity C^(3, 0.029), not C^4.
- 08:04 lead researcher: integrated two external referee answers: on the correction of packets at P and the
  first variation of the obstruction (new labelled item in 6.4; pointers in the Q1 item and in 6.5), and on the range
  1 < A <= 2 (6.4 item rewritten with a direct third-order proof, the fifth-order logarithmic condition at A = 2 and
  compatible examples; 6.5 and the status block). Rechecked by separately written code: the residue L_5 on three
  examples and the zero of R12 for 1 < A < 2. Not yet checked by the verifier.
- 08:12 lead researcher: the verifier checks of the frozen kernel at P (one concrete packet at A = 3 and at X3, and
  the referee's corrections) applied to the label of that 6.4 item, to its items (i) to (iii) and to the Q1 item.
- 08:27 verifier: the Lipschitz estimate at A = 4, every constant of its chain and the radius e^(-10^7) CONFIRMED
  (constants evaluated from the stated reference bounds and from computed norms; suprema by sampling) [Corrected
  2026-10-20: as stated in 6.3.1 (n), the bounds that enter the chain are the referee's analytic bounds for the explicit
  rational reference, which the verifier checked by hand; the sampled suprema are a separate diagnostic, not the bounds
  that certify the result]; the range 1 < A <= 2 (the hypotheses of 6.3.1 (h) and (f) on that range, the formula at
  A = 2 and the pair of 6.3.1 (c) at A = 2), the corrected family range of 6.3.1 (g), the logarithmic divergence at the
  critical origin order 7 + beta and the trace hypotheses of 6.3.1 (k) for profiles CONFIRMED by hand and symbolically.
- 08:34 lead researcher: the preceding entry applied. The range 1 < A <= 2 and the local exclusion at A = 4 moved from
  6.4 to 6.3.1 (m), (n), with their remaining unverified parts kept in 6.4; labels in 6.3.1 (g), (k), in 6.4 and in
  6.5; the status block.
- 08:44 lead researcher: an external audit of the status block and section 6 (the version of 08:12) applied. The range
  1 < A <= 2 survives (its dependencies and the forcing F of the direct proof added to 6.3.1 (m), F checked
  symbolically); hypotheses restored in the 6.4 item on the correction of packets (admissibility, bending, fixed
  parameters, delta C_(0,j) instead of delta B_j, rank three only for a regular tuning argument); the higher-jet
  statements qualified at resonant orders (at A = 2, L = 2 on R12, B_5 = 11/1474560 with a smooth fifth trace and
  l_5 = 0, checked symbolically); verification labels of the frozen kernel and of 6.5 made consistent; the scope of the
  Hoelder hypothesis and of Q4 restricted to A > 2; the statement that NO_inf must use the canonical velocity law
  weakened to the use of a further property of admissible profiles. Also added: a 6.4 item on the exact functional on
  compatible analytic approximants of the computed trace (0.27 to 0.34 natural units). Not yet checked by the verifier.
- 08:52 verifier: the forcing F of the direct third-order step in 6.3.1 (m) (symbolically, with the axis limit and the
  cone step by hand), the fifth-order condition at A = 2 (the residue formula two ways on three examples; the exact
  example with B_5 = 11/1474560 and a smooth fifth trace), the closed form and the zero of the family of 6.3.2 (a) for
  1 < A < 2 (two representations against the closed form, to 6e-21), the bending coefficient and the normalized
  exponents of the correction of packets, the first variation (numerically to 1e-12 at A = 4), the variable-A variation
  terms, the structural zero of delta C_(0,j), the logic of the conditional correction and G_3(0) at the precise
  parameters CONFIRMED.
- 09:06 lead researcher: added a 6.4 item on a local exclusion with polynomial constants at the computed A (external
  referee: radius 1e-6 in a weighted trace norm around the trace of 6.3.2 (a) at A = 10.150725, e = 0.0135206; the
  reference values, three directional derivatives and the closed-form reconstruction checked numerically by the lead
  researcher); the sampled test of (H_-) and the values of mu_0 on the analytic approximants added to the preceding 6.4
  item; 6.5 (local version) and the status block updated. Not yet checked by the verifier.
- 09:08 lead researcher: the 08:52 verifier entry applied (labels in 6.3.1 (m), in the 6.4 items on the correction of
  packets, the frozen kernel and the range 1 < A <= 2, in 6.5 and in the status block); the 6.4 item on Q1 updated with
  a Jacobian with a more accurate inverse (its singular values below about 1e-3 not resolved) and a Newton solve that
  reduced the residual to 9.5e-4 and stalled (numerical researcher; not yet checked by the verifier).
- 09:35 lead researcher: corrected the description of the norm N in the 6.4 item on the local exclusion with polynomial
  constants at the computed A (R_v is the Taylor remainder after c_j u^j; the compatible combinations phi_j enter only
  through the first-variation values) and recomputed the sampled N-distances in that norm (the trace of 6.3.2 (a) to the
  approximants 530 to 571, the fits among themselves 8.8 to 66.7); added the 6.4 item on the certified exclusion ball of
  radius 4.5e-6 around the fitted reference (external referee; certificate rerun by the lead researcher; not yet checked
  by the verifier); 6.5 (A local version) and the status block updated.
- 09:39 lead researcher: an analytic audit of the local exclusion at the computed A by a second external referee applied
  to the two 6.4 items on local exclusion (confirmed in the norm N with the Taylor remainder; the same radii in the
  convention with the compatible polynomials phi_j after corrected constants, rerun by the lead researcher; trace-space
  membership stated as a hypothesis; qualifications of the reconstruction, the C^2 counterexample and the numerical
  dual-norm and bump values). Not yet checked by the verifier. [Corrected 2026-10-20: the same radii hold in that
  convention for the references of the first part of 6.3.1 (o) (q = 0 and A = 4); for the fitted reference the
  conversion multiplies the radii by 4/415.]
- 09:59 lead researcher: an adversarial audit of the 6.4 item on the certified exclusion ball around the fitted
  reference by a further external referee (certificate, budgets and radii confirmed, 140 separate checks; conditional
  theorem confirmed with its hypotheses restated; the analytic continuation threshold is sufficient, not necessary)
  applied to that item, to 6.5 (A local version) and to the status block; the parameter derivatives and corner values
  of B checked by the lead researcher by central differences, and the conversion constant 415/4 by hand. Not yet
  checked by the verifier.
- 10:08 lead researcher: after the verifier's checks of the local exclusion at the computed A (constants assembled in
  its own exact arithmetic from inputs derived by hand, both certificates and budgets rerun, reference values and
  sampled N-distances recomputed with its own code, the analytic estimates audited line by line with two standard steps
  read but not re-derived) and of the exact functional on the compatible analytic approximants, the two 6.4 items on
  local exclusion were moved to 6.3.1 (o) and the item on the approximants to 6.3.2 (e); the numerical dual-norm and
  bump values and the analytic continuation estimate, which the verifier did not check, stay in 6.4 (item "Further
  statements on the local exclusion of 6.3.1 (o)"); the status block, 6.4 and 6.5 (A local version) updated accordingly.
- 10:09 lead researcher: the verifier's diff audit of the same items applied: every number recomputed with its own code
  agrees; the last digit of dB/dA at A = 4 corrected (-0.0651471618470), the K = 18 fit error in w' given as about 2e-6
  (2.02e-6 at the last stored sample) and the bound on the fit errors in w/u for K >= 10 as 2.4e-6; the label of 6.3.1
  (o) now says that the second-order remainder theorem behind the explicit estimates was checked by the verifier only
  through its constants and inputs [corrected 2026-10-20: that wording came from a version of the verifier's record that
  the verifier itself corrected; the theorem was audited by the verifier line by line, and the one step read but not
  re-derived, the holomorphy in the parameters, was re-derived later (entry 10:27)]; the restated hypotheses of 6.3.1
  (o) (iii) were checked by the verifier against 6.3.1 (h), and the example showing that the analytic continuation
  threshold is not necessary was recomputed by the verifier.
- 10:25 lead researcher: an adversarial consistency audit of section 6, the Summary, the status block and the Appendix
  by a further external referee (18 findings) applied: the propagation of smoothness of 6.3.1 (f) labelled with its two
  unchecked inputs in the status block, 6.3, 6.3.1 (a) and (f); a note in the status block that the inferences of
  sections 0 to 5 from a nonzero B_3 need l_3 = 0 for profiles of P_inf that are only C^(2,alpha) at P; the sampled
  reference suprema of 6.3.1 (n) stated as sampled, with the certified radii of 6.3.1 (o) beside them [withdrawn at
  10:27: those bounds are analytic bounds, checked by the verifier by hand]; the conditions of the frozen packets, the
  packet correction and the higher-order statements of 6.5 restated with their existence and nonresonance hypotheses;
  the radii of the two norm conventions for the fitted reference distinguished (factor 4/415); the two parameter centres
  of the boxes of 6.3.1 (o) given separately; the normalized frozen-model limit of G_3/H_3 given with its factor
  g*^(-3 - 2/A); the range of mu_0 in 6.3.2 (e) corrected; corrections recorded in brackets in the Appendix entries
  01:56, 03:16, 04:34, 05:02, 06:27, 07:08, 07:20 and 09:39. Not yet checked by the verifier.
- 10:27 lead researcher: after the verifier's check of that audit: the bounds for the explicit rational reference of
  6.3.1 (n) are analytic bounds, checked by the verifier by hand (the audit had taken them to be sampled), so the 10:25
  wording on sampled suprema in 6.3.1 (n), the status block and 6.5 is withdrawn; the step of the second-order remainder
  theorem of 6.3.1 (o) that the verifier had read but not re-derived (the holomorphy in the parameters) is now
  re-derived by the verifier, and the general prescription for the second parameter derivatives is not used, so the
  label of 6.3.1 (o) says that the theorem was checked by the verifier by hand; the further statements on that exclusion
  (the dual-norm lower estimate, the bump value and the two-constants estimate), now checked by the verifier, moved from
  6.4 to the end of 6.3.1 (o); the count of the distances recomputed by the verifier updated.
- 10:34 lead researcher: after the verifier's proof of the localization of the velocity law (on a ball around any point,
  the velocity is the order-0 multiplier of the cut-off density plus a far part that is C^infinity with explicit
  derivative bounds), that proof was inserted into 6.3.1 (f), whose label now says that the verifier checked the proof
  of (C1) including the localization, with the positive-commutator estimate cited from the literature as its one
  unchecked input (status block, 6.3, 6.3.1 (a), (f) and (h)); the 6.4 item of 10:27 on the same localization was
  removed. Further wording points of the verifier applied: the status block says where l_3 = 0 is known; the N-distances
  of the trace of 6.3.2 (a) to the approximants of 6.3.2 (e) are given for K = 4 to 18 (492 to 634); the label of the
  analytic continuation estimate in 6.5 refers to 6.3.1 (o); the local-exclusion sentence of 6.5 (NO_inf) names the
  ingredients as sufficient and says that the third is available under the Hoelder or cone hypothesis; the 10:25 entry
  bracketed.
- 10:46 lead researcher: after the verifier's diff audit of the versions 10:28 and 10:34 (agreement with its record
  except one sign) and its independent confirmation of a second proof of the localization (through the Cauchy-Riemann
  equations for the far part): the sign of the second component of the multiplier in the Localization paragraph of 6.3.1
  (f) corrected (-d_1^2); after the verifier's check of the discontinuity of B_3 at the critical origin order and of its
  source analogue on the trace of 6.3.2 (a), the label and the text of the 6.4 item Conditioning updated.
- 10:59 lead researcher: an external referee's self-contained proof of (C1) (a one-derivative propagation lemma with
  resolvent regularization and an explicit cutoff commutator estimate, iterated in integer Sobolev orders) and its proof
  of the bounded-third-trace statement of 6.3.1 (f) without (C1), in the derivative-free form of 6.3.1 (i), recorded as
  a 6.4 item, not yet checked by the verifier; the third-order identities and the integration in m checked by the lead
  researcher.
- 11:01 lead researcher: after the verifier's check of that proof of (C1), of the localization and of the direct
  third-order argument (all confirmed; one precision: at order five the products of a Hoelder function with the
  derivative of one are defined when alpha > 1/2, and the conclusion stands because the direct argument does not
  construct the traces of order four and five): the proof of (C1) in 6.3.1 (f) replaced, so that (C1) uses no cited
  estimate; the qualifiers on the cited estimate removed from the status block, 6.3, 6.3.1 (a) and (m); the theorem of
  6.3.1 (f) supplemented by its form without (C1) and the bound Q_3 - Q_3(x*) = O(x* - x); the 6.4 item of 10:59
  removed; the label of the Jacobian with a more accurate inverse in the 6.4 item Q1 updated after the verifier's
  recomputation of the unconverged state and of the response rates.
- 11:04 verifier audit of the changes of 11:01 against the version of 10:46 (every changed passage compared with the
  referee's answer): the replaced proof of (C1), the form of the theorem of 6.3.1 (f) without (C1), the removed
  qualifiers and the label in the 6.4 item Q1 confirmed; no statement needs a change; two optional precisions. 11:08
  lead researcher: both applied (the cutoff in the iteration of (C1) equals one near the tube; a bracket after the 03:17
  entry on the cited estimate).
- 11:10 verifier: the formal coefficients of the 6.4 item on the local structure at a singular source recomputed (the
  quadratic jets at P, the logarithmic axis equations, the constant c, the resonant coefficient J and
  e = -J/(2(A - 1))); the existence of the corrections not checked. 11:19 verifier consistency read of the status block
  and of section 6 (version of 11:08) against the verification record: every statement of 6.3 has a verifier record; the
  label of the singular-source item was stale after the check of 11:10; four statements of the status block omitted
  hypotheses or were too broad (the scope of smoothness near 0 in the B_3 = 0 statement; l_3 is open only for c_l > 3/2,
  by 6.3.1 (m); the hypotheses of 6.3.1 (n) and (o)); one cross-reference was wrong; three optional precisions (the
  multiplier bound on Hoelder-Zygmund spaces among the textbook facts of 6.3.1 (f), a notation clash, a
  cross-reference). 11:34 lead researcher: all applied.
- 11:33 verifier: the growth bound (iv) of the 6.4 item on the frozen kernel at P proved by hand for the stated class of
  packet profiles and every A > 1, and checked numerically in three cases (optimal exponent 1/A; failure of the weighted
  gradient bound). 11:41 lead researcher: label of that item updated.
- 11:28 external referee: a proof of the endpoint condition at the higher odd orders received (for odd j >= 5, a profile
  of P_inf of class C^(j-1,alpha) near P with alpha > 1 - (j-1)/A has l_i = 0 for the odd i with 3 <= i <= j and B_i = 0
  at the nonresonant orders; at a resonant order a logarithmic compatibility condition instead); checked by the lead
  researcher (the exact identity symbolically for n = 2, 4, 6, the estimates by hand). 11:43 verifier: every part
  confirmed with its own symbolic code (the identity for n = 2 to 8) and by hand, including the resonance condition at
  j = 5, A = 2 (the condition L_5[w] = 0 of 6.4) and the scalar Hoelder example; the proposed text confirmed with five
  optional precisions. 11:46 lead researcher: the statement added to 6.3.1 (h) as the item Higher odd orders, with the
  precisions; (j), 6.5 and the summary of the status updated. Necessary conditions under hypotheses additional to P_inf;
  no change to the endpoints.
- 11:57 second external referee: adversarial audit of the proof of (C1) in 6.3.1 (f) and of the item Higher odd orders
  of 6.3.1 (h) with the passages that change with it: both proofs correct after wording changes (the smooth compactly
  supported cutoff and the extension of the coefficients in the iteration; the commutator in divergence form, with DW,
  Delta W and first derivatives of the order-0 coefficients; a non-exhaustive list of the standard facts used; the
  distributional sense of the equation for K_n at C^n regularity; the convergence sentence for the forcing integral
  restricted to the majorant used); in the surrounding passages, the endpoint hypotheses of (f) at the orders j >= 5 are
  not shown to be necessary assumptions, the absence of an endpoint theorem under the regularity of the class is a
  statement about this report, and an estimator for B_5 on sampled data has not been built rather than shown not to
  exist. 11:59 lead researcher: all these changes applied to 6.3.1 (f), (h), (j), 6.4, 6.5 and the summary of the
  status; labels of the two proofs record the second audit.
- 12:07 and 12:11 lead researcher: a third external referee's consistency audit of the status block, the reporting
  convention of 6.1, the exact remaining gap of 6.5 and their cross-references against 6.3 and 6.4
  (on the version of 11:47) received; it finds the conclusion that neither endpoint is reached consistent with the
  labelled results, and lists errors of scope and imprecisions. Applied at 12:11, not yet checked by the verifier: the
  opening sentence of the status block now states that C_0 = l_3 + B_3 needs the finite-part hypotheses and the
  existence of l_3 (not known for every profile of P_inf with A > 2), that the agreement with the functional of R10
  needs the origin expansion of R10 and l_3 = 0, and that the inference from a nonzero B_3 is valid when l_3 = 0 or the
  cancellation l_3 = -B_3 is excluded; in 6.5 the bent-packet statement keeps the conditional scope of the 6.4 item, the
  Q1 sentence no longer presupposes isolation of a discrete solution near X3, and the sufficient routes to NO_inf are
  stated on a class on which l_3 = 0 is established, with nonzero C_(0,j) or a nonzero compatibility coefficient as the
  higher failure; in 6.4 Q1 the sentence on the soft directions no longer reads as an exclusion; the appendix entries of
  06:27 and 07:08 receive dated corrections. The remaining imprecisions are being applied.
- 12:15 lead researcher: the imprecisions found by the same audit applied, not yet checked by the verifier: in 6.5
  Toward YES_inf, the literal endpoint test B_3 = B_5 = B_7 = 0 is distinguished from a generalized test on
  C_(0,j) = l_j + B_j (with compatibility coefficients at resonant orders), the absence of a candidate with B_3 = 0 is
  stated as a search record, and the tuning of three obstructions on a hypothetical family is recorded as unproved; in
  the sign route the trace hypotheses of 6.3.1 (k) are kept for the cone form; the general A > 2 gap is restated (source
  limit and source integral; frozen examples within their parameter ranges); the local version keeps the source
  hypothesis of 6.3.1 (h), the parameter widths, the ball centres (A/A_0) w_0 and the fixed-parameter radii, and its
  statements about numerical traces, trial samples and the two-constants estimate are made precise; 6.5 Higher jets
  records the C^(4,alpha) and C^4 special cases; in 6.3.2 the evaluations of the exact functional are called numerical
  and the R12 closed form a 40-digit numerical check; the appendix entries of 06:21 and 08:27 receive dated corrections.
- 12:16 lead researcher: the 6.4 Q1 item records the state of the solve with the Jacobian built with the inverse of the
  residual (truncated Gauss-Newton residual 2.11e-4, stalled; about nine near-null directions with exactly recomputed
  actions; quadratic growth along the four softest), labelled as the numerical researcher's, with the verifier's own
  off-node residual 4.0e-3 of that state; no change of conclusion.
- 12:17 lead researcher: following the verifier's optional precision, the condition 0 < alpha < 1 is added to the
  C^(j-1,alpha) hypothesis in 6.3.1 (f), 6.4 (the source condition (C2')) and 6.5 (Higher jets).
- 12:17 lead researcher: 6.5 (Toward NO_inf for 1 < A <= 2) records the further necessary condition l_5 = 0,
  B_5(c_l, w) = 0 for 1 < A < 2 under C^(4,alpha) regularity near P (6.3.1 (h), Higher odd orders), following the
  verifier's suggestion; whether the data of R12 at L^2 = S_A satisfy it is not computed.
- 12:20 verifier: the changes of 11:59 (the second external referee's audit applied) checked against the statements they
  rest on: the mollification sentence of Higher odd orders with the integral form along characteristics, the cutoff, the
  extension of the coefficients and the distributional sense in the iteration of (C1), the new sentence of 6.3.1 (j),
  and the wording in 6.4, 6.5 and the status block, all confirmed, with two optional precisions. 12:26 lead researcher:
  both applied (the mollification is local on compact sets where a != 0; the last clause of the higher-jets bullet of
  6.3.1 (j) states the hypothesis 0 < alpha < 1, alpha > 1 - (j-1)/A).
- 2026-10-20 12:33 lead researcher: presentation of the status note and the Summary. The status note at the top is
  regrouped into paragraphs and a bulleted list without changing its sentences (one sentence on the origin moved to the
  bullet on higher odd orders); one definition sentence is added (A = 2c_l - 1 and the source P). The Summary gains a
  reference to section 6 in item (i) and one paragraph on the follow-up, assembled from results already in section 6 and
  the status note. Submitted to the verifier for a check of the changed text.
- 2026-10-20 12:41 lead researcher: 6.4 Q1, following the numerical researcher's correction of 12:29 and the verifier's
  note of 12:32: the actions along the near-null directions were recomputed by central differences at amplitude 0.005,
  accurate to about 5e-4, so the singular values below 5e-4 (not 2e-5) are upper bounds only; the statement on
  quadratic, even growth along the four softest directions rests on a separate amplitude scan and is unchanged.
- 2026-10-20 12:42 verifier and lead researcher: the verifier's audit of the changes of 11:59 to 12:17 (the third
  external referee's consistency findings applied) confirmed every changed statement, with optional precisions; two are
  applied at 12:42: the status note states that the cancellation clause concerns a finite l_3, and the 6.5 sentence on
  bent packets records that g*/A (about 2.931) is not an integer at the computed parameters. The verifier also confirmed
  the regrouping of the status note of 12:33 (format only, and the added definition sentence).
- 2026-10-20 12:44 lead researcher: 6.4 Q1, following the numerical researcher's note of 12:41: the singular values
  1.95e-7 to 1.1e-3 of the soft directions at the stalled state came from central differences at amplitude 0.005, which
  the cubic term of the residual contaminates; the numerical researcher reports larger resolved values, so the earlier
  values are withdrawn (the entry of 12:41 is superseded on this point) until the recomputation with a smaller step has
  been checked by the verifier.
- 12:58 lead researcher: the verifier's optional precisions of 12:41 to the status note and the Summary applied (the
  bounded-trace hypothesis as the one-sided limit x -> x*^- of 6.3.1 (f); for 1 < c_l <= 3/2 the existence of profiles
  is not decided either; the logarithmic alternative at resonant orders; the relation between the two ranges given for
  B_3 on the candidate). No conclusion changed.
- 13:18 lead researcher: fifth-order results at the source added (external referee, audited by a second external
  referee, checked by the lead researcher and by the verifier): the closed form of B_5 on the compatible data of R12 at
  the zero of B_3, negative on 1 < A < 4 without A = 2, so these data are excluded as axis data of profiles that are in
  addition C^(4,alpha) near P, with the exact jump at A = 2 explained (6.5, 6.4, status note); and three exact frozen
  solutions with vanishing third and nonzero or divergent fifth normalized axis limits at A = 7/4, 2, 5/2 (6.3.1 (j)).
  Under the regularity of the class alone the fifth-order condition remains undecided; no endpoint changed.
- 14:16 lead researcher: transport examples without the velocity law added (external referee, audited by a second
  external referee, checked by the lead researcher and by the verifier): for every 1 < A < 4 local pairs of class C^3
  near P satisfying the transport equation and the constant divergence, with the parities and the source structure, have
  l_3 = 0 and l_5 = -1, so these properties alone do not imply the fifth-order endpoint condition; they violate the curl
  identity of the velocity law (6.3.1 (j)). The obstruction to applying the frozen theorem to profiles is stated in 6.5
  and the status note. Under the regularity of the class the fifth-order condition remains undecided; no endpoint
  changed.
- 14:52 lead researcher: 6.3.1 (h) gains the conditional theorem Fifth order under summable fourth-derivative growth
  (for 1 < A < 2, transport, constant divergence, the class regularity and a summable weighted bound on the fourth
  derivatives of f and W in a left cone at P give l_5 = 0; bounded weighted quantities do not suffice for transport and
  divergence alone), and 6.3.1 (j) gains Local source structure and what the velocity law controls at P (linearizing
  chart, local div-curl identities, suppression of thin odd structures, the axis bound that would suffice); 6.5 and the
  status note record that the R12 data at the zero of B_3 are also excluded under the summable hypothesis (external
  referee, audited by a second external referee; checked by the lead researcher and by the verifier). No endpoint
  changed.
- 15:04 lead researcher: the Q1 item of 6.4 rewritten after the verifier's audit: the inference from the
  image projection to the stall removed, the half-step orbit residual attributed to the numerical researcher, the
  earlier raw responses and both residual normalizations qualified, and the centre obstruction of the finite interpolant
  added (ball arithmetic on the exact interpolant at ideal nodes; the fifth-order coefficient (5 c_l - 1) p_7 - 7 c p_9
  of the transport residual is nonzero for every velocity of class C^3 at the centre). Verifier: confirmed with two
  wording precisions, which are applied. No endpoint changed.
- 15:29 lead researcher: 6.3.1 (h) extended (external referees, each audited by a further external referee; checked by
  the lead researcher and by the verifier): the summability theorem holds for every finite A >= 2 as well, with a
  logarithmic cut-off example showing that d_n -> 0 does not suffice for transport and divergence alone; a new bullet
  Fifth order under a density bound shows that, with the curl identity, polynomial bounds on the fourth and fifth
  derivatives of the density alone give the summability hypothesis when alpha > 3 - 4/A (every class exponent for
  1 < A <= 4/3), and that the hypothesis does not follow from the local velocity identities alone. 6.3.1 (j): the
  transport examples extended to every A > 1. 6.5, 6.4 and the status note: the corresponding pointers, and the
  exclusion of the R12 data at the zero of B_3 under the summable hypothesis also for 2 < A < 4 (lead researcher;
  checked by the verifier; audited by an external referee). Under the regularity of the class alone the fifth-order
  condition remains undecided; no endpoint changed.
- 15:42 lead researcher: new item 6.3.1 (p) (verifier; audited by an external referee; checked by the lead researcher):
  a solution of the profile equation in the admissible class whose density has one fixed finite angular cutoff in the
  physical polar angle, valid for every radius, is zero; hence no profile of P_2 or P_inf has this form. The computed
  candidate is not of this form, and the theorem does not exclude profiles with infinitely many angular modes; status
  note: the corresponding bullet. No endpoint changed.
- 15:48 lead researcher: added to 6.3.1 (c) the compact canonical extension of the explicit local pair (verifier;
  audited by an external referee; checked by the lead researcher), with the scope corrections of the audit: the
  consistency statement concerns bounded regions fixed in advance and the global conditions (A1) to (A3), the canonical
  velocity law and the normalization, the field is not in the class, and conditional exclusions under additional trace
  hypotheses are not affected; the status note says the same.
- 16:03 lead researcher: added to 6.5 (Higher jets) the reversible-packet examples (external referee; audited by a
  second external referee; checked by the lead researcher and by the verifier): transport, constant divergence, the
  source conditions and smooth downstream data do not supply the growth hypotheses of the fifth-order criteria; the
  examples violate the curl identity, and the paragraph states that neither a polynomial growth class for the coupled
  system nor its absence is proved, together with the precise sequence statement.
- 16:40 lead researcher: final audit corrections of an external referee (checked by the verifier): the B_3 caveat of the
  trial estimator is repeated at the two summary sites where the estimator is quoted; the packet hypotheses of 6.4 state
  the nonresonance condition and the integrality condition for the singular-trace asymptotics; the NO_inf convention
  records nonexistence results restricted by further hypotheses (for instance 6.3.1 (o) and (p)) separately; the
  coefficients of the fitted reference of the local obstruction certificate are printed; the Q1 item says that the
  resolution question is not decided and adds the verifier's variations of the discretization (a coarser grid, a moved
  far row, cross-grid soft directions, a fixed-c_l family and two correction steps), none of which is a convergence
  result; four smaller precisions of wording. No endpoint changed.
- 17:03 lead researcher: new item 6.3.1 (q) (verifier; checked by the lead researcher; audited by external referees):
  every nonzero profile has a nonzero Hoelder continuous homogeneous trace F at infinity, rho(r theta) = r^(1/c_l)
  F(theta) + O(r^(1/c_l + gamma - 1)), with the velocity limit; under an additional two-term expansion hypothesis the
  next coefficient is determined by F, and at angles with positive limiting normalizer the normalized residual tends to
  0 at infinity whatever the balance (with an example where it does not at an angle with vanishing normalizer); status
  note and Q1 item: the corresponding sentences. In 6.3.1 (j): the nonlinear remainder of the frozen fifth-order
  examples and restricted obstructions to their nonlinear correction, with a formal construction on a left cone
  (external referee and verifier; audited by external referees; checked by the lead researcher). Q1 (iv): the measured
  Ritz values of the coarser grid and two further re-solved states (verifier). No endpoint changed.
- 17:39 lead researcher: corrections from two external audits of the report's internal consistency
  (checked by the verifier): the NO_inf convention now says that a nonexistence theorem may be cut down by an explicit
  structural hypothesis such as (Hmin) of R9 when the report states exactly what remains; the smoothness to the left of
  the source and the two-field fourth-derivative hypothesis are stated where they are used (6.3.1 (h), the summable
  alternative); symbols defined at first use (the operator of 6.3.1 (f), the radius and the remainder of (j), the norm
  and the reference profile of (o)); the computed B_5 of 6.3.2 (a) and 6.4 is labelled as numerical, and floating-point
  margins as not a rigorous roundoff bound; the scope sentences of 6.4 for Q3 and Q4 rewritten. No endpoint changed.
- 17:55 lead researcher: new item 6.3.1 (r) (verifier; reviewed by the lead researcher, who checked the recurrences with
  separately written exact code; audited by two external referees, whose repairs concern proof details only and were
  applied by the verifier; the text checked by the verifier): exact real-analytic solutions of the coupled equations on
  a left cone at P whose first nonvanishing higher odd axis coefficient, of any odd order m >= 3, is C r^(-(m-1)/A) with
  any prescribed C != 0; the source criteria of 6.3.1 (h) hold on closed cones; in that cone formulation the strict
  exponent alpha > 1 - n/A of the higher trace criterion (n >= 2 even, A > n) cannot be relaxed to equality, and the
  density-bound criterion fails if both its strict inequalities become equalities together (m = 5, 4/3 < A < 2). New
  status bullet; Q4 sentences of 6.4 and 6.5 say that on a left cone at P exact solutions with l_3 != 0 exist and that
  their extension to a neighbourhood of P, or to a profile, is open. No endpoint changed.
- 18:04 lead researcher: the R12 fifth coefficient is negative exactly for every A > 1 with A != 2 (verifier; audited by
  an external referee; checked by the lead researcher), by a gamma representation of the beta factor in which every
  factor has a fixed sign, so the computed B_5 at A = 10.150725 is nonzero by proof and only its value is numerical; the
  6.5 item Toward NO_inf for 1 < A <= 2, 6.3.2 (a), 6.4 and the status note updated accordingly, with the exponent
  condition alpha > 1 - 4/A of Higher odd orders for A >= 4 and the summable alternative for every A > 2. No endpoint
  changed.
- 18:04 lead researcher: 6.3.1 (r)(i) extended by the finite family of cone solutions with any finite set of odd seeds
  and independent source amplitudes, real-analytic in the amplitudes on a common small cone for each bounded set of
  amplitudes, with the exact triangular formulas for G_3, G_5, G_7 (verifier; reviewed by the lead researcher; audited
  by an external referee; the text checked by the verifier, whose two quantifier repairs are included), and 6.4 Q2 by
  one sentence; these cone solutions are not profiles and give no family of P_inf. No endpoint changed.
- 18:17 lead researcher: at the exceptional R12 case A = 2 (p_5 = 12 resonant) the seventh coefficient is exactly
  B_7(c_l, w) = -23/29059430400 (natural units -23/14189175) for the source-selected traces, so under C^(6,alpha) of rho
  near P (the velocity then has the same regularity) and smoothness near 0 (C^24 suffices) the whole two-parameter
  family of R12 axis data (A > 1, L > 0) admits no P_inf profile (verifier, two exact implementations; checked by the
  lead researcher with separately written exact code; audited by an external referee; the text checked by the verifier);
  this is a statement about one explicit family of axis functions under a hypothesis at P beyond the class, not NO_inf.
  One precision in 6.3.1 (r)(i). No endpoint changed.
- 18:43 lead researcher: corrections from an external consistency audit of the status note, the Summary, 6.0, 6.1, 6.4
  and 6.5 against 6.3 (checked by the verifier before application): in 6.5 the statement that the full linearization is
  not upper semi-Fredholm now carries its setting (fixed support K, the domain Omega, rho and W of class C^(2,sigma),
  W(P) = 0; 6.4, the frozen kernel at P, (v)); in the 6.4 item on B_5 and B_7 the reference value of B_5 is called
  numerical (its negative sign is exact, 6.5); the exact seventh coefficient at A = 2, L = 2 and the restricted
  exclusion of the whole R12 family under C^(6,alpha) at P, and the finite cone families of 6.3.1 (r), added to the
  status note, the Summary paragraph on the follow-up and that 6.4 item. No result of 6.3 changed.
- 19:19 lead researcher: corrections from two final external audits of 6.3 (checked by the verifier before application):
  in 6.3.1 (n) the explicit bound on |B_3(c_l, w) - B_3(5/2, w_0)| is stated with <= (equality holds at w = w_0); in
  6.3.2 (c) the comparison direction b is called analytic near 0 (it carries the cutoff); in the converse of 6.3.1 (a)
  the identification C_(0,j) = B_j is stated for profiles satisfying (C2') at every odd order; in the conormal remark of
  6.3.1 (h) the relative order for j >= 9 is given by its formula, with its value at X3; in 6.3.1 (r) the lead
  researcher's check of G_5 and G_7 is described as a recheck with separately written symbolic code. No result of 6.3
  changed.
- 19:19 lead researcher: in 6.4 Q1 (iv), the state computed with the radial scale of the representation halved (checked
  by the verifier before application): its collocation residual, the verifier's sampled transport residuals,
  self-consistency defect and centre tests, and its four smallest Ritz values (numerical researcher, not recomputed
  independently). No endpoint changed.
- 19:33 lead researcher: corrections from two final external audits of 6.1, 6.2, 6.4 and 6.5 (checked by the verifier
  before application). In the item "Conditioning" of 6.4 the bump family at the critical origin order 7 + beta is
  described as a discontinuity of B_3 in C^m for the integers m < 7 + beta; it does not tend to 0 in the critical case
  of the weighted norm of 6.3.1 (i), so it gives no discontinuity in that norm (the earlier wording did not name the
  topology). In the further results of the referee of 6.3.1 (n), the critical order R^(-2-1/c_l) is the decay of the
  adjoint test function, at which the far-field flux is of order 1 (its positive limit is stated under explicit
  regularity conditions, as the verifier recommended), and the test is attributed to the lead researcher's question. In
  6.4 Q1 (ii) the measured nonzero physical actions of the six softest directions are no longer read as showing that
  they are not physical null vectors, since no error bound for them is supplied. Clarifications: the B_5 and B_7 targets
  of 6.1 against the centre conditions of 6.3.1 (a) and (h); the unsolved correction equations at a singular source
  against the left-cone construction of 6.3.1 (r); "independently" in place of "simultaneously" for the tuning of
  C_(0,3), C_(0,5), C_(0,7) in 6.5. No endpoint changed.
- 19:59 lead researcher: in the item "Conditioning" of 6.4, two results of the verifier (checked by the lead researcher
  by hand and audited by external referees; the text checked by the verifier before application): for A > 2, B_3 is
  discontinuous on compatible axis data in the critical case sigma = beta of the origin part of the norm of 6.3.1 (i),
  and, when g_* != 2A - 2, in the critical case theta = 1 - beta of its part at the source; both use perturbations of
  amplitude 1/N spread over a logarithmic interval of length N. So the strict inequalities sigma > beta and
  theta + beta > 1 of 6.3.1 (i) cannot in general be relaxed to equalities. No endpoint changed.
- 20:12 lead researcher: in 6.4 Q1 (iv), the state computed with the radial scale of the representation doubled (the
  text checked by the verifier before application): its collocation residual, c_l and four smallest Ritz values
  (numerical researcher, not recomputed independently), and the verifier's independent reconstruction of the same state
  (source position, self-consistency defect, maximum sampled transport residual over the 58 fixed points, values near
  the source and exact centre tests). No endpoint changed.
- 20:12 lead researcher: at the end of the 6.4 item on conditioning, the statement that a small residual of the third
  axis equation does not control B_3: for smooth traces on compatible axis data B_3 equals the finite-part integral of
  the residual against 1/(w H_3), and on the data of R12 at A = 4 a family of traces has residuals tending to 0 in C^j
  for j <= 6 at fixed B_3 < 0 (proof by the verifier, checked by the lead researcher by hand and audited by an external
  referee; the text checked by the verifier before application). No endpoint changed.
- 21:01 lead researcher: in the 6.4 item on conditioning, after the statement at the source, that its hypothesis
  g_* != 2A - 2 can be dropped if g(x*) may move (at g_* = 2A - 2 an interior perturbation of size 1/n together with a
  source layer of amplitude n^(-2) and logarithmic length n^3 tends to w_0 in C^(2,1-beta) while the change of B_3 has a
  nonzero limit), and that for perturbations at the source which keep g(x*) = 2A - 2 exactly the change of B_3 is
  bounded by a constant times the C^(2,1-beta) norm (proofs by the verifier, checked by the lead researcher by hand and
  audited by an external referee); in 6.0, a description of the accompanying artifacts of the follow-up; in 6.4 Q1, two
  precisions on rounded ratios after an external referee audit of the changed passages of 6.4; the text checked by the
  verifier before application. No endpoint changed.
- 21:01 lead researcher: in 6.4 Q1 (iv), the state computed on a third, coarser grid of 72 x 30 nodes at the same radial
  scale (the text checked by the verifier before application): its collocation residual, c_l, the stall of its solve and
  its ten smallest Ritz values (numerical researcher, not recomputed independently), and the verifier's independent
  reconstruction of the same state (source position, self-consistency defect from two separately bounded evaluations,
  maximum sampled transport residual over the 58 fixed points, values near the source and exact centre tests). No
  endpoint changed.
- 21:01 lead researcher: in the 6.4 item on conditioning, after the statement at a fixed value of g(x*), the estimate
  from which it follows, for perturbations at the source alone with the coefficient of the statement at the source taken
  at the moved value of g(x*), and its consequence at g_* = 2A - 2 that a sequence of perturbations at the source alone,
  tending to 0 in C^(2,1-beta), gives a negative limit of the change of B_3 (proof by the verifier, checked by the lead
  researcher by hand and audited by an external referee; the text checked by the verifier before application). No
  endpoint changed.
- 21:35 lead researcher: in the 6.4 item on conditioning, one precision of wording after the external referee audit
  ("The fixed-value bound follows" for "The statement at a fixed value follows"; the text checked by the verifier before
  application). No endpoint changed.
- 21:35 lead researcher: in the 6.4 item on conditioning, after the statements at the source, that the discontinuity at
  0 in the critical case sigma = beta persists when g(x*) and the whole germs of w and g at x* are fixed, for every
  value of g_*, with the limit a kappa_A for every real a (proof by the verifier, checked by the lead researcher by hand
  and audited by an external referee; the text checked by the verifier before application). No endpoint changed.
- 21:35 lead researcher: in the 6.4 item on conditioning, after the statement at 0 with the source germ fixed, that
  finitely many local observations do not determine B_3 near w_0: for every real b there are compatible traces with
  B_3 = b exactly, arbitrarily close to w_0 in the norm of 6.3.1 (i) with sigma = beta, that agree with w_0 near 0 and
  outside a small interval near 0 (proof by the verifier, checked by the lead researcher by hand and audited by an
  external referee; the text checked by the verifier before application). No endpoint changed.
- 21:35 lead researcher: in the 6.4 item on conditioning, after the statement on finite local observations, that the
  same traces can be taken close to w_0 in C^(7,beta) with the rebuilt density close in C^(8,beta), so that B_3 takes
  every real value in every neighbourhood of w_0 in the ordinary Hoelder norm of the critical order 7 + beta (proof by
  the verifier, checked by the lead researcher by hand and audited by an external referee; the text checked by the
  verifier before application). No endpoint changed.
- 22:23 lead researcher: in the 6.4 item on conditioning, after the statement in C^(7,beta), the exact first-order
  description of the discontinuity at 0 (B_3[w_0 + v] - B_3[w_0] = kappa_A M(v) + O(E(v)), uniformly in the support of
  v, also with the source germ fixed) and the sufficient Dini condition on v^(7), which gives continuity under
  C^(7,gamma) perturbations at 0 for every gamma > beta (proof by the verifier, checked by the lead researcher by hand
  and audited by an external referee; the text checked by the verifier before application). No endpoint changed.
- 22:29 lead researcher: in 6.4 Q1 (iv), the state computed on a fourth grid of 84 x 35 nodes at the same radial scale:
  collocation residual 5.1e-4 between those of the 72 x 30 and 96 x 40 grids, c_l larger than on the other three grids,
  and Ritz values that are not monotone in the resolution over the four grids (numerical researcher; values and ratios
  recomputed by the verifier from the stored data); the verifier's independent evaluation of this state (source,
  self-consistency defect, maximum sampled residual 0.0068 over 58 points, centre tests); and the fourth Ritz value on
  the 72 x 30 grid rounded correctly as 4.75e-4 instead of 4.76e-4 (the text checked by the verifier before
  application). No endpoint changed.
- 22:45 lead researcher: in 6.3.1 (f), item (C1), the attribution of the propagation statement now also records the
  verifier's independent proof of the same statement, with a resolvent regularization and a weighted energy estimate,
  audited by a further external referee (the text checked by the verifier before application). No endpoint changed.
- 22:57 lead researcher: in 6.4, the item on the frozen kernel at P, statement (v), and its restatement in 6.5: the
  domain Omega stated as bounded, with the neighbourhoods required by the parity and the need for separate uniform
  mapping assumptions on an unbounded domain; the verifier's independent proof of (v), also with finitely many added
  constraints, output rows or parameter columns, audited by a further external referee, recorded; and, in the item on
  (H_-) on the stored fits, the calculations covered by the analytic range 0.2945 to 0.3016 of B_3 named (the text
  checked by the verifier before application). No endpoint changed.
- 23:16 lead researcher: in 6.4, the item on the frozen kernel at P, and in its summary in 6.5: the verifier's
  independent proofs, audited by a further external referee, of the regularity class with its sharpness for nonzero
  packets, the smoothness off P, the expansion to every finite order with a C^N remainder for every N, the vanishing of
  the normalized limits of every odd order, and the growth statements, recorded (the text checked by the verifier before
  application). No endpoint changed.
- 23:25 lead researcher: in 6.4, the item on the frozen kernel at P: the verifier's independent proof, audited by a
  further external referee, of the asymptotic form of the axis traces G_j for noninteger mu_j > 0, recorded (the text
  checked by the verifier before application). No endpoint changed.
- 2026-10-21 00:00: cutoff of this report. The status note (its first paragraph, the state line and a short overview of
  the outcome, and the statement of the ball centres in its bullet on the exclusion near reference traces), the Summary
  paragraph on the follow-up (T0, the report cutoff and the scheduled end), 6.0 (the report cutoff, its time from T0 and
  to the scheduled end, the environment of each role, and the disclosure that the roles and the external referees were
  AI models, with the change of the verifier's model at 13:06:38 and the direct reviews obtained by the verifier) and
  the status lines of section 6, 6.3, 6.4 and 6.5 restated for the report cutoff (the text checked by the verifier
  before application); no result of 6.3 changed at this step.
- 2026-10-21 00:03 verifier check of the text applied at the cutoff: the wording and the time stamps confirmed as
  checked before application.
- 2026-10-21 00:12 to 00:36 verifier: further diagnostics of the stored states (among them a fifth grid of 108 x 44
  nodes computed by the numerical researcher after the cutoff) and checks of frozen packet examples; none of them
  requested a change of this report, and the report does not use them.
- 2026-10-21 00:41 verifier final endpoint summary: the record and its scope confirmed; YES_inf and NO_inf on the full
  class not established; the report text unchanged since the check of 00:03.
- 2026-10-21 00:46 end of the run at its 24-hour time cap (T0 + 24 h = 00:46:19Z); neither endpoint reached.
- 2026-10-21 00:47 verifier independent check of its archived files after the cap: preservation confirmed; the report
  text unchanged; no further computation pending.
- 2026-10-21 00:57 finalization for publication (T_end = 2026-10-21T00:57:29Z): the status lines, the timing statements (T_end and the elapsed time),
  the paragraph on what this round added and the description of the accompanying artifacts edited; no result changed.
