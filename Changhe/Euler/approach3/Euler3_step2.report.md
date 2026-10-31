# Joint optimization of c_l and omega at angular degree 6 (Euler3, step 2)

Status: final. Outcome C (optimization remains incomplete), with qualifier D (weak parameter identifiability)
validated at the P1 and F2 ends and conditional on the saved factors at the all-azimuthal-mode P3 end. No endpoint
was reached: no examined branch reached credible numerical stationarity, no state qualifies as an approximate
profile, and nothing here proves or disproves the existence of rotating Euler profiles.

## Summary

Verdict. In the completed comparisons, freeing c_l and omega at degree 6 showed little gain, and no branch reached
credible numerical stationarity. Category C with qualifier D holds for the P1 and F2 ends; for the all-azimuthal-mode lineage P3 it is C,
with D conditional on the saved factors. Outcomes A and B are not met. The final test failed by execution and coverage (time caps),
not by a new failed derivative, field or pressure test, so E does not apply; no final ordering of the branches exists.
The verifier validated the category at 15:08 UTC on 30 October.

Proved result (exact scope). For each canonical degree-6 field represented by the following saved states, the curl of the momentum residual R_u
at the origin, evaluated from the saved binary coefficients in exact rational interval arithmetic, excludes zero:
the segment-1 ends of both members of the P1 and P2 pairs, the P1 and P2 segment-4 ends, the F1 and F2 segment-2
ends, the P3 FREE segment-1 end and the seven inputs of the final test (section 8). Since curl grad P = 0 for every
twice differentiable P, none of these represented fields solves the momentum equation for any twice differentiable pressure. This says
nothing about nearby fields and gives no distance to a solution.

Numerical results (with the qualifications in section 6).

- P1, ranked first in the earlier comparison, conditional on the core-resolution test (from the saved state S01 at (c_l, omega) = (0.45, 1.0)): holdout momentum-residual ratio
  rho_u^max 0.0460 / 0.0463 (standard / half-offset shells) at S01 and 0.0376 / 0.0374 at the frozen P1 FREE state
  near (0.448, 1.41), that is 0.82 of the start. The weighted absolute core residual rose by factors 1.85 and 1.93.
- FREE against its matched fixed-parameter control: 0.7 to 6.8 per cent lower rho_u^max in the three pairs
  measured; both members of each pair raised the absolute core residual.
- Identifiability: after elimination of the coefficient directions only 3.5e-6 to 5.6e-6 of the c_l column and
  8.5e-5 to 4.0e-4 of the omega column of the Jacobian remain; reduced 2 x 2 condition numbers 6.2e2 to 8.5e3.
- No common parameter value: the five ends selected for Phase III are distinct branches at omega near 1.41, 1.38,
  1.08, 0.58 and 0.33, c_l 0.447 to 0.461, and omega was still drifting in every lineage.
- 106.90 GPU-hours charged to the optimization side; FREE 80.28 per cent of the registered optimization count (floor
  80), FIXED-CONTROL plus PROFILE 13.05 per cent of the narrow count (ceiling 15).

Remaining gap. Credible stationarity (criterion 7.4 of the specification) fails first at (a): the relative decrease
of the objective O1 over the last 50 accepted iterations must be below 1e-3 and is 1.1e-2 to 6.0e-2 at examined
ends with that history; shorter runs ended without verified stationarity. Also unmet: (d) scaled parameter gradients at most 1e-4 (measured 1.6e-3 to 4.7e-2) and (b) eta(1e-8) at most
1e-3 (measured 0.58 to 0.89) with a reduced predicted decrease at most 1e-4 of O1 (measured 0.048 to 0.14). Outcome A
needs a final-test rho_u^max at most half of the start and of the matched control; the best is 0.82 of the start.
The final test on fresh holdout points did not complete (four primary evaluations hit their 40-min caps under host
load, a safety stop followed, 13 operations were not attempted), so the comparisons rest on the earlier independent
evaluations. Resolution flags on the top radial modes of three far-field blocks are open at every state. Degree 8
was not run; section 10 lists the evidence that would justify it.

End of the run. T0 2026-10-28T20:30:31Z (logged start); T_end 2026-10-30T16:40:38Z (completion of the campaign report); elapsed
44 h 10 min 7 s of the 48-hour budget. Phases I to IV were undertaken, with the final test of Phase IV incomplete by its
caps. The schedule stopped the team at 47 hours (19:30:31Z) so that this write-up would finish inside the budget; the
team finished its work earlier and was stopped at 16:26:44Z, 43 h 56 min after T0. Resources in section 12.

## Findings in detail

Question. With the existing degree-6 representation (main angular degree 6, the radial basis, envelopes, twist,
far-field correction channels and full-space pressure of the previous campaign), how far can the Euler residual be
reduced when c_l, omega and all coefficients are optimized together?

What was done. c_l and omega were optimizer unknowns in every discovery run (label FREE). Their derivatives include the
dependence of the basis, the twist, the tail constraints, the row weights and the full-space pressure, and they were
validated against finite differences before the production search (section 2). Five lineages were optimized, from four
saved degree-6 states of the previous campaign (S01 at (0.45, 1.0); S09 and S05 at (0.45, 0.3); the all-azimuthal-mode
state S20 at (0.45, 1.0)) and from the S01 coefficients kept at moved parameters (0.4597, 1.3389), together with
shorter breadth samples (random, perturbed and moved starts). Matched fixed-parameter controls (label FIXED-CONTROL) ran
on three lineages. FREE runs accounted for 80.3 per cent of the registered optimization count, which adds the
recorded wall hours of coefficient optimization on CPUs and the early test runs to the charged GPU-hours;
FIXED-CONTROL and the profile runs together accounted for 13.1 per cent of the narrower count defined in section
12.

Findings. These are numerical observations except for the exact obstruction for the listed represented fields.

- Not converged. At examined ends with the required history (the rows of sections 4 and 6), O1 was still falling by 1.1 to 6.0 per cent over the last 50 accepted
  iterations; shorter runs ended without verified stationarity, and omega was still drifting in every lineage (P1 from 1.00 to 1.41 at its frozen state, F1 from 0.30 to
  0.58). At every examined end the linearization with the complete Jacobian still predicted a decrease of 4.8 to 14
  per cent of O1, and the scaled parameter gradients were 1.6e-3 to 4.7e-2 against the required 1e-4. Every examined
  end fails the progress, model and gradient criteria of section 6 (the P3 values there are conditional on the saved
  factors or are the lead's values only).
- Weak identifiability. At every examined end the coefficients absorb almost all of the first-order effect of either
  parameter: after elimination of the coefficient directions only 3.5e-6 to 5.6e-6 of the c_l column and 8.5e-5 to
  4.0e-4 of the omega column remain. The reduced two-parameter problem is not singular (condition numbers 6.2e2 to
  8.5e3), but it carries little of the residual.
- Little gain from freeing the parameters. In the three pairs measured independently FREE ended 0.7 to 6.8 per cent
  below its fixed-parameter control in holdout rho_u^max, and both members of each pair raised the absolute core
  residual. After a second P3 segment the optimizer's own end values put FREE 1.5 to 3.2 per cent above its control. The final
  comparison on fresh holdout points was not obtained (section 8).
- No common parameter value across different saved fields. The five lineage ends selected for Phase III are
  pairwise distinct branches by the registered rule, at omega near 1.41, 1.38, 1.08, 0.58 and 0.33, with c_l between
  0.447 and 0.461. The closest two (P1 and F2) started from the same coefficients at different parameters; one F2
  segment later they are on one branch near (0.448, 1.40 to 1.41) by that rule. That F2 end is itself excluded by the
  core rule (below), and the two runs are not independent initial fields.
- The absolute core residual grows. Along every lineage the normalized shell measure fell while the absolute residual
  in the core rose. Four ends were excluded as approximate-profile candidates because their core residual exceeded
  twice the start value.
- The step Jacobian is not shown to be the bottleneck. On P1, a continuation that used the complete Jacobian for its
  steps made no faster progress per accepted iteration than the production step Jacobian, at about 3.6 times the
  optimizer time.
- No reproduction of a stationary point. A restart from a small perturbation of the P1 end returned to parameters
  within the 1 per cent widths, but its O1 ended 3.9 per cent lower: the descent continued past that end (and that
  end is excluded by the core rule, at its margin).
- Widths not checked on the actual objective along the soft direction. Fixed-parameter runs of 40 iterations at the
  points where the reduced model predicts a 1 per cent rise of O1 ended 6.2e3 and 1.3e8 times above the reference on
  the soft direction, so they bound the profile from above only. On the stiff direction (omega) the runs at -1, +1
  and -2 half-widths were 3.1, 5.8 and 10.6 per cent above the reference after the same 7 accepted iterations (1, 1
  and 4 per cent predicted), all runs still limited by their budget. The points at +2 half-widths on the stiff
  direction and +-2 on the soft direction were not run: the registered floor on the FREE share of the optimization
  count refused the stiff point until the last start time, and the two soft points were not reached (section 7).
- No represented field solves the equation exactly. For each saved field examined (section 10), the curl of the
  momentum residual at the origin, evaluated in exact interval arithmetic, excludes zero.
- Open resolution flags. The tests on the top radial modes of three far-field blocks raise a flag at every end and at
  every start, and the diagnostics that could clear these flags were not run. No state of this campaign is therefore
  called an approximate profile.

No result here bears on the existence or nonexistence of rotating Euler profiles. Degree 8 was not run; section 10
lists the evidence that would justify it. The computations ran from 2026-10-28T20:30:31Z to 2026-10-30T15:23:36Z,
when the last GPU job ended (42 h 53 min of real time). The jobs of the optimization side were charged 106.9
GPU-hours (section 12).

## 1. Problem and representation

The campaign seeks smooth, nonzero, non-axisymmetric, decaying profiles U(y) with pressure P(y) such that

    R_u = (1 - c_l) U + W . grad U + omega J U + grad P = 0,   W = (c_l I - omega J) y + U,   J y = (-y_2, y_1, 0),
    div U = 0,   -Delta P = tr((DU)^2),

with P the decaying full-space Newton pressure, 0.4 < c_l < 0.5 and omega > 0. Both parameters were unknowns in
every primary discovery run (label FREE): the optimization variables are X = (a_1, ..., a_N, c_l, omega), where a are all active
toroidal, poloidal and far-field correction coefficients.

The degree-6 representation of the previous campaign was used unchanged: U = curl(T y) + curl curl(S y) with real
solid harmonics up to the main angular degree L = 6; 16 radial Chebyshev functions per block in x = (s - R0)/(s + R0),
s = sqrt(r^2 + R0^2), R0 = 0.3; toroidal and poloidal envelopes with the far-field rate alpha = (1 - c_l)/c_l; the
smooth twist psi(r) = (omega/(2 c_l)) log(1 + r^2/R0^2) and the twisted far-field angle chi = phi + (omega/c_l) log r;
three far-field correction channels (angular degrees 15, 14 and 6, 4 radial functions each); the tail constraints that
cancel forbidden far-field rates; a dilation gauge (unit far-field norm) and an azimuthal phase gauge. Two symmetry
classes were used: even azimuthal modes (1469 optimizer coordinates, of which 2 are parameters) and all azimuthal modes
(2921). The basis depends on both parameters, and every parameter derivative is taken at fixed reduced coefficients,
so it differentiates the radial basis, the twist, the tail-constraint expansion, the row scalings, the gauge row and
the pressure kernels. The optimizer works in z_c (c_l = 0.4 + 0.1 sigmoid(z_c)) and z_omega = log omega. The run rules
did not allow a main degree above 6. At 02:03 on 30 October the saved checkpoints held 52 run configurations, all
with these settings; only the azimuthal class and one recorded channel setting of one lineage varied (checked
independently from the saved metadata; six of the 52 belong to withdrawn runs).

The objective is O1 = (1/2) ||r(X)||^2, the production objective of the previous degree-6 configuration: momentum rows
with nonlinear shell weighting, far radii at 4096, 16384 and 65536 R0 as momentum rows with pressure, closure rows,
the gauge row 100 (||F|| - 1) and quadrature weights. Every state-dependent ingredient is evaluated at the point
itself, and a step is accepted only if O1 recomputed from scratch at the trial point decreases. Two Jacobians are
used. The step Jacobian J_cw (lagged closure) differentiates everything except the closure target and the carried
closure patterns, which it holds at the current point. The complete Jacobian J_c also differentiates those and is used
for every stationarity and sensitivity statement.

O1 values at different parameters are not compared as evidence, because the row weights and the far-field rate depend
on the parameters. States are compared by the registered diagnostics on dyadic shells in the far-field gauge: rho_u(k) =
RMS_k(R_u) / sum_i RMS_k(T_i) for the five-term split T1 = (1 - c_l) U, T2 = c_l (y . grad) U, T3 = omega [J U - (J y .
grad) U], T4 = (U . grad) U, T5 = grad P, and rho_u^max = max_k rho_u(k), on holdout points of two shell families
(standard and half-offset) reported separately; sigma_u^max, the single-term ratio of the residual to (1 - c_l) U
with the core-resolved balls included; sigma_Om, its vorticity counterpart; and a_max, the weighted absolute residual
in the fixed velocity-tail gauge on the core balls. A state is ranked ahead of another only if it has the lower holdout
rho_u^max on both families and its sigma_u^max, sigma_Om and a_max (at a centre and an upper weight) each exceed
the other's by at most 10 per cent;
otherwise the two are not ordered. A state that lowers rho_u^max while its core a_max rises above twice its start
value is excluded as an approximate-profile candidate.
Section numbers such as 6.3, 7.4 or 8.6 refer to the campaign's registered specification, which is versioned with
every amendment dated; it is part of the accompanying artifacts.

## 2. Derivatives and their validation

Protocol. Every parameter column and a registered sample of 20 coefficient columns of each Jacobian was compared with
centred and five-point differences on a ladder of steps from 1e-3 to 1e-7. A pass needs two consecutive passing steps
for both stencils and a passing Richardson value, separately in each radial group (near origin, core and intermediate,
far, far anchors, gauge, closure), with the active set of the nonlinear weights checked at every stencil point. Gate
G3 tests directional derivatives of O1 in nine directions per case; G2, G4 and G5 test the identities, the pressure,
the source, the spatial derivatives and the divergence; G6 is an extended-precision field test; G7 a kill-and-resume
test; G8 five negative controls that each omit one parameter dependence.

Changes forced by the validation, all made before any optimization run used in this report:
(a) an exact rewriting of the linear part of the operator removed the leading cancellation in the far rows (rounding of
the parameter columns there fell by factors of 2200 to 2800);
(b) the gauge row makes a stiff valley (O1 rises by 4.3 per cent for a change of 1e-5 in z_c at the first test state);
a frozen-weight step Jacobian, which had all 20 tested trial steps rejected, was replaced by the lagged-closure
Jacobian J_cw;
(c) more than 99.99 per cent of the small-step error of six coefficient columns lay in the l = 0, 1 parts of the far
pressure; the pressure chain is therefore evaluated in double-double arithmetic for the residual values
(configuration M; anchor noise from about 1.3e-20 to below 1e-25; 45-digit references of the most-changed rows agree
to 5.9e-18 of the block norm; measured cost ratio 1.05 on the GPU), while Jacobians and gradients stay in float64;
(d) float64 derivative tables of the solid harmonics differed from 70-digit references by up to 6e-10 at degrees 4 to
15 and were replaced on every production path by tables computed in double-double (an independent capture of all
2,976,204 consumed entries found every entry within 1.1e-16 of the reference);
(e) the first assembly of the complete Jacobian omitted the parameter dependence of the tail-constraint coefficients,
and its closure-target derivative had a truncation error up to 3.6e-6; after the repair its parameter columns passed
every block on a manufactured case and at S01 and S09 (the sampled coefficient columns at S09 only with the
post-result rules below).

Gate table of the release cases. Counts of directional-derivative passes include absolute-only passes (in
parentheses). Post-result rules, each registered after a failure and before its evaluation, are labelled where they
decide an outcome: "extra step" adds the step 1e-2 times the column's step factor to the coefficient ladder; "small
amplitude" reports a group whose differences stay below 1e-6 of the column norm at every step as not tested (never
for parameter columns); "seven steps" adds two smaller directional steps; "gauge-subtracted" is an estimator that
removes the known gauge contribution exactly.

| gate | S01 at (0.45, 1.0) | S09 at (0.45, 0.3) | S05 | manufactured, large omega |
|---|---|---|---|---|
| G1 parameter columns (4 per Jacobian, 3 Jacobians) | pass | pass | pass | pass |
| G1 coefficient columns, registered rule (J_f / J_cw / J_c, of 20) | 20 / 20 / 20 | 13 / 15 / 15 | 20 / 20 / 20 | 8 / 10 / 10 |
| G1 with the extra step | not needed | 15 / 15 / 15 | not needed | 13 / 17 / 17 |
| G1 with extra step and small-amplitude rule | not needed | pass | not needed | pass |
| G2, G4, G5 | pass | pass | pass | pass |
| G3, O1, registered five steps (of 9) | 1 (1) | 3 (3) | 2 (2) | 7 (0) |
| G3, O1, seven steps | 8 (4) | 9 (3) | 7 (5) | 7 (0) |
| G3, gauge-subtracted, seven steps | 9 (1) | 9 (0) | 9 (2) | 9 (0) |

J_f is the frozen-weight Jacobian. G6 passed at field level on two parameter pairs, G7 passed 14 of 14 checks, and
each G8 control was detected by at least 100 times the group threshold in a group of non-small amplitude. The
independent checks recomputed the G3 counts of all four cases from the saved differences, evaluated S09 afresh on both
ladders and estimators, evaluated the coefficient columns of J_cw afresh at S01 and S09 on an independent column draw,
and replayed the G2 (c) and G4 (a) decisions from the saved stencil arrays (1044 to 1045 checks per case). They did
not re-evaluate the fields of every case.

What this means. In the four release cases the parameter columns pass the registered rule. The coefficient-column
failures are confined to near-origin columns of very small norm (3e-12 to 3e-9) and to the gauge row of three columns
of one manufactured field; at S09 and at the manufactured field the G1 pass rests on both post-result rules. G3 fails
on the registered five-step ladder at every case. It passes on seven steps with the gauge-subtracted estimator at
every release case; this estimator is a post-result change, and the registered outcome stands beside it.

Other cases of the registered list. Eight further cases (shifted parameters, all-mode fields, small omega, near the
c_l edge) pass every gate under the labelled rules, with three exceptions:
- two saved states moved to other parameters failed G1 under the registered rule in the far-anchor block of the c_l
  column (1.1e-9 to 4.4e-9 of the column norm); both pass a post-result rule that compares such a column with
  differences of a double-double copy of the residual (reproduced independently, two negative controls detected);
- at the manufactured field at (0.42, 0.3) one coefficient column stayed unresolved in the gauge group with the extra step;
  a closed-form derivative of the gauge row agreed with the production entry to 1.8e-15 (independently 1.1e-15);
- at S11 (saved state at (0.42, 0.3)) G3 FAILS in one random direction under every rule: the second-order errors fall
  as h^2 to 2.5e-7 at h = 1e-7 and then rise, so no two consecutive steps pass, while the complete gradient and the
  Jacobian contraction agree to 4.6e-11. The failure stands under the registered rule; its attribution is unresolved, and
  it does not by itself establish an incorrect derivative.

Release. A provisional release (at most two concurrent FREE jobs) was given at 08:50 on 29 October. A full release at
14:31 was withdrawn at 14:44 because one existing record had not been read: the extra-step check at the manufactured
field at (0.42, 0.3), whose gauge group stayed unresolved (listed above; separate from the S11 failure). The runs started under it
were stopped within minutes and are excluded from every result. The full release was posted again at 16:40.

## 3. Main numerical summary (deliverable A)

The final test of the frozen states on fresh holdout points did not complete (section 8), so this table holds the
earlier evaluations: status 08:15Z on 30 October, with the two segment-5 rows of Phase III added later. Holdout rho_u^max is the largest shell value of the RMS
momentum residual divided by the sum of the RMS values of the five terms of section 1, on the dyadic ("standard") and
the half-offset shell families; values
marked "ind." are independently recomputed, the others are the optimizer's end batteries. The core a_max is the
weighted absolute residual maximum in the core with the centre and the outer weight convention. GPU-hours are summed
over the lineage's jobs up to the row's end.

| run (start) | initial (c_l, omega) | final (c_l, omega) | accepted iterations | initial rho_u^max, standard / half-offset | final rho_u^max, standard / half-offset | core a_max, centre / outer | 7.4 label | GPU-hours |
|---|---|---|---|---|---|---|---|---|
| P1 FREE (S01), segment 4 | (0.45, 1.0) | (0.448144, 1.406897) | 587 | 0.04604 / 0.04630 | 0.03762 / 0.03736 ind. | 1.076 / 1.473 | incomplete | 6.57 |
| P1 FREE, segment 5, excluded, diagnostic only | (0.45, 1.0) | (0.447703, 1.462425) | 745 | 0.04604 / 0.04630 | 0.03544 / 0.03610 | 1.238 / 1.692 | incomplete | 8.77 |
| P1 FIXED-CONTROL (S01) | (0.45, 1.0) | fixed | 360 | 0.04604 / 0.04630 | 0.04269 / 0.04306 | 0.765 / 1.056 | incomplete | 1.14 |
| P2 FREE (S09), segment 6, 12-hour budget used | (0.45, 0.3) | (0.460063, 0.330323) | 956 | 0.05227 / 0.07173 | 0.05081 / 0.06333 ind. | 2.061 / 2.061 | incomplete | 12.21 |
| P2 FIXED-CONTROL (S09) | (0.45, 0.3) | fixed | 360 | 0.05227 / 0.07173 | 0.05281 / 0.06824 | 1.967 / 1.967 | incomplete | 1.81 |
| F1 FREE (S05), segment 3 | (0.45, 0.3) | (0.448689, 0.504476) | 386 | 0.06687 / 0.06753 | 0.05090 / 0.05377 ind. | 1.437 / 1.881 | incomplete | 4.77 |
| F1 FREE (S05), segment 4 | (0.45, 0.3) | (0.448272, 0.580171) | 520 | 0.06687 / 0.06753 | 0.04663 / 0.04988 ind. | 1.568 / 2.037 | incomplete | 7.04 |
| F1 FREE (S05), segment 5, parameter-path evidence | (0.45, 0.3) | (0.448169, 0.602807) | 617 | 0.06687 / 0.06753 | 0.04550 / 0.04857 | 1.616 / 2.085 | incomplete | 11.50 |
| F2 FREE (S01 kept at moved parameters), segment 3 | (0.45, 1.0), saved start; entry (0.459677, 1.338884) | (0.447755, 1.323595) | 356 | 0.04604 / 0.04630 (saved start) | 0.04016 / 0.03888 ind. | 0.908 / 1.247 | incomplete | 4.86 |
| F2 FREE, segment 4 | (0.45, 1.0), saved start; entry (0.459677, 1.338884) | (0.447287, 1.375312) | 481 | 0.04604 / 0.04630 (saved start) | 0.03792 / 0.03761 ind. | 1.075 / 1.473 | incomplete | 7.10 |
| F2 FREE, segment 5, excluded, diagnostic only | (0.45, 1.0), saved start; entry (0.459677, 1.338884) | (0.447048, 1.400148) | 557 | 0.04604 / 0.04630 (saved start) | 0.03675 / 0.03697 | 1.161 / 1.589 | incomplete | 10.36 |
| P3 FREE (S20, all-m), segment 2 | (0.45, 1.0) | (0.449844, 1.065675) | 77 | 0.04819 / 0.04745 | 0.04480 / 0.04425 | 2.025 / 2.330 | incomplete | 2.67 |
| P3 FIXED-CONTROL (S20, all-m), segment 2 | (0.45, 1.0) | fixed | 194 | 0.04819 / 0.04745 | 0.04343 / 0.04362 | 2.434 / 2.791 | incomplete | 2.59 |
| P3 FREE (S20, all-m), segment 3 | (0.45, 1.0) | (0.449822, 1.075923) | 110 | 0.04819 / 0.04745 | 0.04436 / 0.04386 | 2.097 / 2.410 | incomplete | 4.11 |
| P3 FREE (S20, all-m), segment 4 | (0.45, 1.0) | (0.449800, 1.084946) | 146 | 0.04819 / 0.04745 | 0.04376 / 0.04329 | 2.206 / 2.532 | incomplete | 7.36 |
| P3 FREE (S20, all-m), segment 5, parameter-path evidence | (0.45, 1.0) | (0.449775, 1.094937) | 176 | 0.04819 / 0.04745 | 0.04279 / 0.04238 | 2.397 / 2.745 | incomplete | 11.47 |
| P1 perturbation repeat (from the P1 segment-4 end), excluded, diagnostic only | (0.45, 1.0); entry: the segment-4 end perturbed | (0.448039, 1.420300) | 587 + 41 | 0.04604 / 0.04630 (S01) | 0.03708 / 0.03705 | 1.115 / 1.526 | incomplete | 9.48 |
| Approach from above (P1 segment-4 coefficients at omega 1.80), excluded, diagnostic only | entry (0.448144, 1.80) | (0.447306, 1.536767) | 34 | 0.04604 / 0.04630 (S01) | 0.03884 / 0.03865 ind. | 1.217 / 1.665 | incomplete | 0.75 |

For F2 the initial values are those of its saved start S01 at its own parameters, the baseline of the outcome rules
(shared with P1). The entry state, the S01 coefficients at the moved parameters, is a separate identity; its
normalized start-reference diagnostic is 0.250, which is not a measurement of the raw entry.

The F2 segment-4 independent value is from one completed coarse pressure level: that evaluation reached its 70-min
cap at 07:27 on 30 October before the fine level completed. The four excluded rows raised the core a_max above twice the S01 value while rho_u^max fell (exclusion rule
6.3 (g)); they are kept as diagnostics. The core a_max of the starts (centre / outer weight, from their start
records) is 0.558 / 0.798 for S01, 1.921 / 1.921 for S09, 0.982 / 1.338 for S05 and 1.661 / 1.919 for S20. The profile
runs of section 7 are fixed-parameter runs at prescribed points, not branches, and are listed there. The two
segment-5 rows (F1 and P3) are Phase III parameter-path evidence, not final states; their values are the producer's
end batteries. An independent evaluation of the P3 segment-3 end likewise completed only its coarse pressure level
within its 70-min cap (08:40 on 30 October); at that level it gave 0.04437 / 0.04385, against the optimizer's
0.04436 / 0.04386. The final test added no row.

## 4. Parameter evolution and branch identity (deliverable B)

The accompanying artifacts hold, for every lineage, c_l, omega, omega/c_l, O1 and its
residual blocks, the gradient norms and the checkpoint residuals against accepted iterations, and the paths in the
(c_l, omega) plane, together with every window value quoted here and the hash of every record read. Iterations are counted from the start of the lineage. O1 is
the optimizer objective; O1 values at different parameters are not compared.

Lineages and their latest ends, optimizer-side values.

| lineage (start, class) | start (c_l, omega) | latest end: accepted iterations, (c_l, omega), omega/c_l | O1 at that end | last 50 accepted iterations: fall of O1, change of c_l, change of log omega |
|---|---|---|---|---|
| P1 (S01, even-m) | (0.45, 1.0) | 587, (0.448144, 1.406897), 3.139 (frozen P1 state) | 1.5616e-7 | 5.8 %, -1.8e-4, +0.016 |
| P1, segment 5 (excluded, see below) | | 745, (0.447703, 1.462425), 3.267 | 1.3265e-7 | 4.5 %, -1.2e-4, +0.011 |
| P2 (S09, even-m) | (0.45, 0.3) | 956, (0.460063, 0.330323), 0.718 (12-hour lineage budget used) | 1.0484e-7 | 1.1 %, +2.5e-4, +0.0078 |
| F1 (S05, even-m), segment 4 | (0.45, 0.3) | 520, (0.448272, 0.580171), 1.294 | 2.0390e-7 | 2.4 %, -6.3e-5, +0.023 |
| F1, segment 5 (Phase III, parameter-path evidence) | | 617, (0.448169, 0.602807), 1.345 | 1.9296e-7 | 3.7 %, -7.4e-5, +0.025 |
| F2 (S01 coefficients kept at moved parameters, even-m), segment 4 | (0.4597, 1.3389) | 481, (0.447287, 1.375312), 3.075 | 1.5858e-7 | 6.0 %, -1.8e-4, +0.014 |
| F2, segment 5 (excluded, diagnostic) | | 557, (0.447048, 1.400148), 3.132 | 1.4580e-7 | 5.4 %, -1.5e-4, +0.011 |
| P3 (S20, all-m), segment 3 | (0.45, 1.0) | 110, (0.449822, 1.075923), 2.392 | 2.1649e-7 | 2.3 %, -3.0e-5, +0.012 |
| P3, segment 4 (frozen P3 state) | | 146, (0.449800, 1.084946), 2.412 | 2.1211e-7 | 2.2 %, -2.4e-5, +0.009 |
| P3, segment 5 (Phase III, parameter-path evidence) | | 176, (0.449775, 1.094937), 2.434 | 2.0351e-7 | 5.3 %, -3.7e-5, +0.014 |

- No lineage meets the joint parameter-change criterion; omega continues to move in each. omega moved much more than c_l: +41 per cent in P1 to the frozen
  segment-4 state, +93 per cent in F1 to segment 4 (+101 per cent at segment 5), +10 per cent in P2 and +8.5 per cent
  in P3 to the frozen segment-4 state (+9.5 per cent at segment 5), while c_l stayed between 0.4470
  and 0.4601. F2 moved c_l from 0.4597 to 0.4483 in its first accepted step; its omega fell to 1.19 in the first
  segment and then rose to 1.40.
- Objective blocks. The core and intermediate rows carry most of O1 (96 per cent at the P1 segment-3 end) and fell in
  every segment of every lineage. The far-momentum block (2e-4 to 7e-4 of O1) rose in every segment of P2 to segment
  4 and in P1 segments 1 to 3, and fell in P1 segment 4.
- Segment-end residuals, first to latest end (optimizer end batteries, standard / half-offset holdout). rho_u^max fell
  along every FREE lineage: P1 0.0435 / 0.0425 to 0.0376 / 0.0374; P2 0.0524 / 0.0694 to 0.0508 / 0.0633; F1 0.0647 /
  0.0651 to 0.0466 / 0.0499; F2 0.0428 / 0.0414 to 0.0379 / 0.0376; P3 0.0449 / 0.0444 to 0.0438 / 0.0433. sigma_u^max
  rose in P1 (0.449 to 0.467), P2 (1.906 to 2.012), F2 (0.456 to 0.467) and P3 (0.464 to 0.469) and fell in F1 (0.443
  to 0.425). The core a_max rose in every lineage: P1 0.553 to 1.076 (1.238 at segment 5), P2 1.925 to 2.061, F1
  1.032 to 1.568, F2 0.613 to 1.075, P3 2.000 to 2.206.
- Excluded ends. The registered exclusion (g) (a training-grid rho_u^max below the start value together with a core
  a_max above twice the start value) was raised by the admitted records at the P1 segment-5 end (0.03463 against
  0.04547 at S01, core a_max ratios 2.221 and 2.120 for the two weight conventions) and at the F2 segment-5 end
  (0.0360 against 0.0455, ratios 2.082 and 1.991). Both are diagnostic only and were not continued; the candidates
  are the segment-4 ends (P1 ratios 1.93 and 1.85). The P1 FIXED-CONTROL member grows in the same way (ratios 1.04
  and 1.37 at its two segment ends), so moving the parameters is not necessary for this growth. This is the pattern
  the task description warns about: the normalized residual falls while the absolute core residual grows.

Comparison across initializations. P1 and F2 both started from the S01 coefficients (F2 at moved parameters), so they
are not independent initializations. At their segment-4 ends they were at (0.4481, 1.407) and (0.4473, 1.375), both
rising in omega; one segment later the F2 end, at (0.4470, 1.4001), is on the P1 segment-4 branch by the registered
rule (below). P2 and F1 started at (0.45, 0.3) from different saved fields of the previous campaign and have moved
apart (omega 0.330 against 0.580). P3 is the only all-m lineage. No common parameter value has appeared among lineages
from different saved fields.

Branch identity. Registered rule: two states are one branch only if their parameter difference lies within the
linear-model half-widths of either state (the half-widths at which the model value rises by 1 per cent of O1, along
the two eigen-directions of the reduced parameter matrix) and their field distance (on each dyadic shell, the RMS of
the velocity difference over the RMS of one state's velocity, in the far-field gauge, the larger of the two
directions) is at most 0.10. If the quadratic and pressure terms are negligible in the far field (small U alone does
not imply this), the momentum equation reduces to linear transport, whose solutions have cylindrical components
r^(-alpha) F(theta, phi + (omega/c_l) ln r). For two such fields, with k = omega/c_l, the best per-shell rotation
about the z axis then changes by (k_a - k_b) ln 2 per doubling of the radius whatever the angular shapes (for a
minimizer unique up to a common period), so agreement with this law tests the represented twist, not shape agreement.

| pair | parameter part, half-widths (soft, stiff) | field distance (worst shell) | twist, rad per doubling: predicted; measured | RMS of U remaining after the best rotation per shell | verdict |
|---|---|---|---|---|---|
| P1 segment 4, F2 segment 2 | fails at both states (stiff -1.82 and 1.60) | 0.62 (0.47 after the best common rotation) | 0.1825; 0.1823 to 0.1825 on shells 4 to 8 (independent) | about 0.10 | distinct |
| P1 segment 4, F2 segment 4 | agrees at both (0.045, -0.448 at P1; 0.044, -0.448 at F2) | 0.2809 / 0.2753 (shell 8; 0.141 after the best common rotation) | 0.0448; 0.0446 to 0.0448 on shells 2 to 8 (production-code copy) | 0.0006 to 0.040 | distinct |
| P1 segment 4, F2 segment 5 | agrees at both (0.057, -0.069 at P1; 0.056, -0.069 at F2) | 0.0550 / 0.0536 (shell 8) | 0.00513; 0.00513 to 0.00525 on shells 4 to 8 (copy) | 0.045 to 0.052 | same branch |
| P2 segment 4, F1 segment 2 (F1 counted from its pilot) | agrees at both | 4.30 (core RMS of U differs by a factor 3.3) | not used | 0.59 to 0.65 on shells 2 to 8 | distinct |

- The all-m P3 end carries 0.206 to 0.427 of its per-shell RMS in odd azimuthal modes, which are orthogonal to every
  even-m field and are kept under rotation about the z axis, so its registered distance to any even-m state is at
  least 0.437 (sampled values on the evaluation grid, not a continuum bound).
- The five ends selected for Phase III are pairwise distinct. The independent check reproduced the parameter results
  and the field distances of the first, second and fourth rows with its own reconstruction and quadrature. For the
  third row it confirmed the stored arithmetic, the parameter part from the exact saved optimizer coordinates (0.0557
  and -0.0689 at the F2 state) and the decision, but did not re-evaluate the fields.
- As F2's omega approached P1's, the remaining shape difference fell by more than half and most of the distance was
  twist; at F2 segment 5 the twist difference is small and the remaining distance of about 0.05 is shape. Two runs
  from the same S01 coefficients with initial parameters (0.45, 1.0) and (0.4597, 1.3389) reached one branch near
  (0.448, 1.40 to 1.41). They are not independent initial fields, and the F2 end that joined is excluded by rule (g).
  This describes saved states; it does not test whether either pair lies on one continuous family of solutions.

Other initializations (breadth samples, one pilot allowance of 1800 s each; optimizer-side values unless marked).
- Refit into the moved basis. Weighted least-squares refits of S01 and S09 at moved parameters were ill-conditioned
  (condition estimates 7.6e24 and 5.7e24), and a regularized refit (column-scaled truncated singular value
  decomposition, cutoffs 1e-8 and 1e-6) at the most favourable small move failed both registered acceptance
  conditions. No refit start was used. This shows that these refits failed, not that every refit fails.
- Kept coefficients at moved parameters: S01 at (0.4597, 1.3389) became F2; S09 at (0.4218, 0.8086) reached O1 1.1e-5
  and holdout rho_u^max 0.250 / 0.236 within the allowance.
- Two random initializations at design points, (0.4282, 7.977) and (0.4914, 0.1112), ended at holdout rho_u^max 0.41
  and 0.93 and moved their parameters by less than 1e-2.
- Perturbed S01 starts at (0.45, 1.0). A coefficient change of relative size 1e-3 in the training-grid field (the
  sizing of section 7) returned to the unperturbed path in (omega, c_l, O1) in 34 iterations (O1 2.44e-7 at (0.44962,
  1.07862), holdout rho_u^max 0.0441 / 0.0434); the remaining field difference has the size of the applied change, so
  whether the change was removed is not resolved. A change of 1e-1 took O1 from 0.72 to 2.5e-5 in 39 iterations
  without recovering (holdout rho_u^max 0.24, core a_max 12.7); the field differs from S01 and from its start by 0.34
  to 0.50 of the RMS of U on the shells between r = 0.15 and 1.2.
- Approach from above in omega. The P1 segment-4 coefficients kept at (0.448144, 1.80) ran as a FREE pilot of 1800 s.
  omega fell at each of the 34 accepted steps, to 1.536767 (c_l 0.447306, O1 1.8367e-7). Holdout rho_u^max 0.0388 /
  0.0386 (independently recomputed) is above the P1 segment-4 end. Against its own start the record raises no
  exclusion (core a_max ratios 0.54 and 0.54); against S01 it raises rule (g) (training-grid 0.0382 against 0.0455,
  ratios 2.18 and 2.09), so it was not continued. At its end the linear model still predicted a decrease of 0.089 of
  O1 (eta(1e-8) 0.817), with a model step (+0.056, +0.225) in (c_l, omega) whose c_l part leaves the interval.
These samples show no second parameter region of low residual and no robust return to one field; within single
allowances they decide neither. The Phase III perturbation repeat at the P1 segment-4 end (section 7) came back to
parameters within the widths but continued the descent along the unperturbed continuation.

## 5. FREE against FIXED-CONTROL

Design. Each pair has a FREE member and a FIXED-CONTROL member started from the same state with the same basis,
objective, nominal allowances and validation. The registered pair result is the ratio FREE/FIXED-CONTROL of the
independently recomputed holdout rho_u^max on both shell families, with the differences in sigma_u^max and a_max. O1
ratios at equal accepted iterations and at equal optimizer time (the last accepted iterate within the other member's
count or time, without interpolation; selections reproduced independently) are context, because O1 at different
parameters uses different row weights.

| pair (start) | allowance | accepted iterations FREE / FIXED | FREE end (c_l, omega) | O1 ratio at equal iterations / equal time | rho_u^max FREE/FIXED, standard / half-offset | sigma_u^max FREE minus FIXED, standard / half-offset |
|---|---|---|---|---|---|---|
| P1 (S01) | 360 iterations, 3 h | 228 / 360 | (0.448987, 1.262588) | 0.969 / 1.104 | 0.975 / 0.932 | +0.0063 / +0.0007 |
| P2 (S09) | 360 iterations, 3 h | 280 / 360 | (0.452729, 0.304015) | 0.921 / 1.148 | 0.993 / 0.991 | +0.0105 / +0.0038 |
| P3 (S20, all-m), segment 1 | 120 iterations, 1 h | 44 / 108 | (0.449853, 1.061848) | 0.987 / 1.013 | 0.986 (common physical shells) | -0.0073 |
| P3, segment 2 | 120 more iterations, 1 h more | 77 / 194 | (0.449844, 1.065675) | 0.989 / 1.079 | 1.032 / 1.015 (optimizer values) | -0.0085 / - (optimizer values) |

The P1 and P2 holdout values are independently recomputed (an independent Cartesian field evaluation and an
independent full-space radial Green route for the pressure, at the finer of two pressure quadratures); the P3
segment-1 values are from the same independent route on the common physical shells; the P3 segment-2 holdout ratios are the optimizer's end batteries and its O1 ratios are
optimizer values from the saved checkpoints and logs, with the selections reproduced independently (the ratio at equal
time compares the last saved samples within the common 7200 s allowance, at 7109 s FREE and 7189 s FIXED-CONTROL; at
the common final time, 7230 s, it is 1.081). These are ratios of the optimizer's O1, not of independently evaluated
residuals.
- In the three independently measured comparisons FREE ends lower than FIXED-CONTROL on rho_u^max (by 0.7 to 6.8
  per cent); after the second P3 segment the optimizer's end batteries put FREE above FIXED-CONTROL by 3.2 and 1.5
  per cent (no independent value), and in
  all four FREE reaches a lower O1 per accepted iteration, but a higher O1 per unit of optimizer time, because a FREE iteration costs 2.4 to 2.6 times a
  FIXED-CONTROL iteration in the even-m class (section 9). In P1 and P2 FREE ends higher on the dyadic sigma_u^max in
  both families.
- Neither member improved uniformly on the start. At P1 both raised the weighted absolute maximum and the core-ball
  residual well above the start (core-ball RMS momentum residual 0.0177 at the start, 0.0706 FIXED-CONTROL, 0.0670
  FREE); at P2 both ended above the start in rho_u^max on the standard shells and below it on the half-offset shells,
  and sigma_u^max near 1.9 means that on one dyadic shell the RMS residual exceeds the RMS of (1 - c_l) U in every
  state. In P3 FREE had the lower RMS residual than FIXED-CONTROL on 7 of 13 common physical shells and on all four
  balls, and both ends had a higher ball residual than the start.
- The members were equal in nominal allowances but not in realized iterations or time (P1: 10861 s against 7032 s of
  optimizer time; P2: 10866 s against 5359 s; part of P1 FREE ran alone on its GPU), so these are not matched-compute
  or causal comparisons. In P3 segment 2 the median LM damping was 3.8e-2 for FREE against 9.5e-4 for FIXED-CONTROL:
  the FREE member took both fewer and smaller steps.
- The measured pair differences exceed the summed pressure-refinement changes by factors of at least 19 (P1, P2) and
  1.05e4 (P3); these are consistency checks, not error bounds.
- The final test, which was to compare the frozen FREE, FIXED-CONTROL and start states of P1 on fresh holdout
  points, did not complete (section 8), so the comparisons above are the only ones of this campaign.

## 6. Stationarity and reduced parameter sensitivity

Each examined end was linearized with the complete Jacobian J_c in scaled optimizer coordinates (gauge row included).
eta(t) = ||P_t r||^2 / ||r||^2, where P_t projects onto the left singular directions with singular values above t times
the largest; the reduced quantities eliminate the coefficients at the cutoff 1e-12 and describe the two parameters.
Credible stationarity (registered criterion 7.4) requires all of: (a) progress: a relative decrease of O1 below 1e-3
over the last 50 accepted iterations and over the last 25 per cent of the branch's wall time (or, for a branch that
terminates sooner, a verified termination in which (b) to (d) hold and a line search along the full Gauss-Newton
direction gives no decrease above 1e-4 relative); (b) eta(1e-8) at most 1e-3 and a reduced predicted decrease at most
1e-4 of O1; (c) ranges of c_l and log omega over the window of (a) at most 1e-4 and 1e-3; (d) the complete scaled
gradient ||g||_inf / ||r|| and both scaled parameter gradients at most 1e-4; (e) a restart from a perturbation (the
coefficients by a relative 1e-3, and z_c and z_w each by 1e-3) returns to parameters within the 1 per cent widths and
to O1 within 1 per cent. A branch failing (a)
is "incomplete". A branch meeting (a) but failing (b) or (d) is "conditioning-limited" if eta(1e-10) or eta(0) exceeds
1e-2 while eta(1e-8) is at most 1e-3, and "not stationary" otherwise. The values were computed by the lead's tool from
the saved factors and reproduced independently with a different factorization route (largest relative discrepancy
7.8e-11 on the first four records), except where marked.

| end | O1 | eta(0) / eta(1e-8) | scaled parameter gradients (c_l, omega) | absorption cosines (c_l, omega) | cond S, correlation | reduced Gauss-Newton step (dc_l, domega) | predicted decrease / O1 | 7.4 |
|---|---|---|---|---|---|---|---|---|
| P1 FREE, segment 2 | 2.0762e-7 | 0.851 / 0.849 | 0.041, 0.041 | 5.6e-6, 2.5e-4 | 2.2e3, 0.25 | 0.063, 0.205 | 0.140 | incomplete |
| P1 FREE, segment 3 | 1.9160e-7 | 0.831 / 0.829 | 0.035, 0.035 | 5.6e-6, 2.4e-4 | 2.1e3, 0.32 | 0.061, 0.210 | 0.135 | incomplete |
| P1 FREE, segment 4 | 1.5616e-7 | 0.794 / 0.790 | 0.039, 0.039 | 5.4e-6, 2.2e-4 | 2.2e3, 0.48 | 0.056, 0.211 | 0.108 | incomplete |
| P1 FREE, segment 5 (excluded end, diagnostic) | 1.3265e-7 | 0.761 / 0.756 | 0.030, 0.030 | 5.1e-6, 2.0e-4 | 2.1e3, 0.55 | 0.054, 0.218 | 0.096 | incomplete |
| P2 FREE, segment 2 | 1.4911e-7 | 0.632 / 0.614 | 0.0041, 0.0041 | 5.5e-6, 2.6e-4 | 2.3e3, -0.09 | 0.037, 0.067 | 0.056 | incomplete |
| P2 FREE, segment 3 | 1.2591e-7 | 0.606 / 0.588 | 0.0045, 0.0045 | 5.3e-6, 3.1e-4 | 3.5e3, -0.08 | 0.036, 0.069 | 0.058 | incomplete |
| P2 FREE, segment 4 | 1.1434e-7 | 0.601 / 0.584 | 0.0036, 0.0035 | 5.1e-6, 3.5e-4 | 4.8e3, -0.08 | 0.036, 0.068 | 0.057 | incomplete |
| P2 FREE, segment 5 | 1.0863e-7 | 0.603 / 0.587 | 0.0018, 0.0018 | 5.0e-6, 3.8e-4 | 5.8e3, -0.09 | 0.036, 0.066 | 0.056 | incomplete |
| P2 FREE, segment 6, end of the 12-hour budget | 1.0484e-7 | 0.603 / 0.587 | 0.015, 0.015 | 4.9e-6, 4.0e-4 | 6.9e3, -0.09 | 0.036, 0.062 | 0.054 | incomplete |
| F1, segment 2 | 2.6494e-7 | 0.861 / 0.857 | 0.039, 0.039 | 3.5e-6, 1.1e-4 | 1.2e3, -0.33 | 0.056, 0.120 | 0.050 | incomplete |
| F1, segment 3 | 2.3129e-7 | 0.834 / 0.829 | 0.036, 0.036 | 3.5e-6, 9.4e-5 | 7.7e2, -0.20 | 0.049, 0.132 | 0.048 | incomplete |
| F2, segment 2 | 1.9915e-7 | 0.838 / 0.836 | 0.0016, 0.0016 | 5.6e-6, 2.2e-4 | 1.7e3, 0.32 | 0.061, 0.206 | 0.136 | incomplete |
| F2, segment 3 | 1.8415e-7 | 0.821 / 0.818 | 0.0043, 0.0042 | 5.6e-6, 2.1e-4 | 1.7e3, 0.38 | 0.059, 0.206 | 0.125 | incomplete |
| F2, segment 4 | 1.5858e-7 | 0.793 / 0.789 | 0.0074, 0.0074 | 5.4e-6, 2.0e-4 | 1.8e3, 0.48 | 0.056, 0.206 | 0.106 | incomplete |
| P1 FIXED-CONTROL, end | 1.9910e-7 | 0.837 / 0.834 | 0.0049, 0.0049 | 4.8e-6, 2.7e-4 | 3.3e3, 0.17 | 0.069, 0.177 | 0.130 | incomplete |
| P2 FIXED-CONTROL, end | 1.5379e-7 | 0.639 / 0.618 | 0.0023, 0.0023 | 5.5e-6, 2.3e-4 | 1.8e3, -0.08 | 0.038, 0.061 | 0.057 | incomplete |
| P3 FIXED-CONTROL, segment 1 (all-m) | 2.1936e-7 | - / 0.884 | 0.0095, 0.0094 | 3.8e-6, 3.4e-4 (cutoff 1e-8) | 8.0e3, - | 0.063, 0.270 | 0.095 | incomplete |
| P3 FREE, segment 1 (all-m), conditional | 2.2227e-7 | - / 0.890 | 0.0037, 0.0037 | 3.9e-6, 3.1e-4 (cutoff 1e-8) | 6.5e3, - | 0.062, 0.256 | 0.088 | incomplete |
| P3 FREE, segment 2 (all-m), conditional | 2.2032e-7 | 0.891 / 0.889, not determined (see below) | 0.016, 0.016 | 3.9e-6, 3.1e-4 (cutoff 1e-8) | 6.5e3, 0.06 | 0.061, 0.257 | 0.087 | incomplete |
| P3 FREE, segment 3 (all-m), lead values only | 2.1649e-7 | 0.888 / 0.886 | 0.010, 0.010 | 3.9e-6, 3.1e-4 (cutoff 1e-8) | 6.4e3, 0.07 | 0.061, 0.255 | 0.085 | incomplete |
| P3 FIXED-CONTROL, segment 2 (all-m), values of the independent check | 2.0402e-7 | - / 0.876 | 0.0069, 0.0069 | 3.8e-6, 3.5e-4 (cutoff 1e-8) | 8.5e3, - | 0.060, 0.261 | 0.092 | incomplete |
| F1, segment 4 | 2.0390e-7 | 0.806 / 0.799 | 0.013, 0.013 | 3.5e-6, 8.5e-5 | 6.2e2, -0.14 | 0.040, 0.152 | 0.048 | incomplete |
| F2, segment 5 (excluded end, diagnostic) | 1.4580e-7 | 0.775 / 0.771 | 0.0067, 0.0067 | 5.2e-6, 1.9e-4 | 1.8e3, 0.52 | 0.054, 0.208 | 0.099 | incomplete |
| P1 perturbation repeat, end after 41 accepted steps | 1.5007e-7 | 0.786 / 0.782 | 0.0041, 0.0040 | 5.3e-6, 2.1e-4 | 2.2e3, 0.50 | 0.055, 0.212 | 0.105 | incomplete |
| P3 FREE, segment 4 (all-m), frozen P3 state, conditional | 2.1211e-7 | 0.886 / 0.884 | 0.047, 0.047 | 3.9e-6, 3.1e-4 (cutoff 1e-8) | 6.4e3, 0.09 | 0.059, 0.251 | 0.083 | incomplete |

The FIXED-CONTROL states are linearized at their fixed parameters with the free-parameter model, so their parameter entries are slopes those runs
did not use. In the all-m factors twelve columns are exactly zero by construction (the l = 1 columns of a far-correction
block) and are excluded. The P3 FREE segment-1, segment-2 and segment-4 factors failed the registered consistency
check of their largest singular value (relative 1.15e-12, 1.13e-12 and 1.004e-12 against 1e-12), so their values
describe the saved factors only and are conditional. At
the P3 FREE segment-2 end the singular-value gap at the cutoff 1e-8 is below the registered margin filter (normalized
margin 3.0e-12 against 1e-11), so eta(1e-8) there is not determined; the reduced values at the coefficient cutoff 1e-8,
whose margin passes, were reproduced independently. The P3 FREE segment-3 row has the lead's values only (the
independent attempts on this record reached their wall limits). There the gaps at the cutoffs 1e-10 and 1e-12 are
below the margin filter (1.1e-12 and 1.4e-13) and the gap at 1e-8 passes (2.8e-10), so the reduced values are given at
the coefficient cutoff 1e-8; at the P3 FREE segment-4 end the same holds (1.6e-12 and 1.2e-13; 5.0e-10 at 1e-8). The rows
marked "lead values only" have not been reproduced independently.

What the records show.
- No examined end is near credible stationarity. Every one fails (a) and is therefore "incomplete": O1 still fell by
  1.1 to 6.0 per cent over the last 50 accepted iterations (the P3 FREE segment-1 end, with 44, and the perturbation
  repeat, with 41, had fewer than 50 and ended at their budgets without a verified stationarity termination). Every one also fails (b) and (d), so meeting (a) later would not by itself give stationarity; at the P3
  FREE segment-2 end, where eta(1e-8) is not determined, (b) fails through the conditional reduced predicted decrease
  (0.087 of O1) and (d) through the complete scaled gradient. Every FREE
  end with 50 accepted iterations fails (c): c_l and omega were still drifting, mostly monotonically.
- The coefficients absorb almost all of the first-order effect of either parameter: before elimination the two
  parameter columns are almost parallel (cosine 0.999998 at P1 FREE segment 2); after it, 3.5e-6 to 5.6e-6 of the c_l
  column and 8.5e-5 to 4.0e-4 of the omega column remain. The reduced parameter matrix has condition number 6.2e2 to 8.5e3, so the
  parameters are not singular in the linear model, but their effect is carried by a small residue of each column.
- The linear model still offers large decreases: the predicted decrease of the reduced step is 4.8 to 14 per cent of
  O1, and, at the ends where it is determined, 0.58 to 0.89 of ||r||^2 lies along singular directions above 1e-8 of the largest. At the even-m ends the
  remaining 0.14 to 0.40 of ||r||^2 lies in the complement of the stored orthogonal factor's column space; that is the share outside the range
  of the linearization only if the stored factor has full rank, which small positive singular values in floating point
  do not establish.
- The reduced step is a quantity of the linear model, not an admissible update. At the P1, F2 and P3 ends and the F1 segment-2
  end its c_l component would take c_l above 0.5, outside the parameter map; at the P2 ends and the F1 segment-3 and
  segment-4 ends the model minimizer lies inside, at c_l 0.488 to 0.498. The measured c_l drift over 50 accepted iterations is of
  order 1e-4, so the model step is far outside the range in which the optimizer has moved.
- Linear-model widths at 1 per cent of O1 (P1 segment 4): the soft direction, mostly c_l, moves c_l by 0.019 and omega
  by 0.037; the stiff direction, mostly omega, moves omega by 0.068 (+0.041 and -0.043 in log omega). At P2 segment 4
  the stiff half-width in log omega is 5.3 to 8.4 times that of P1. These are widths of the linear model about its
  minimizer, which lies outside the admissible interval in most cases; they are not widths of a branch.
- At the four pair ends of P1 and P2, changing the coefficient cutoff from 1e-12 to 1e-8 changes the predicted
  decreases by 3 to 7 per cent and leaves every label unchanged.
- Smallest singular values (7.3 (e)). At every examined end the 20 smallest singular values of the column-scaled J
  run from the rounding level (1e-16 of the largest) up to 1.1e-12 to 1.4e-11 of the largest. In each of the 20
  corresponding right singular vectors as computed (lead's values, not reproduced independently), the parameter part
  has squared norm at most 8e-13 in the column-scaled coordinates, so a unit vector in their span has at most 1.6e-11
  if the computed vectors are exactly orthonormal (1.6e-11/(1 - delta) if their Gram matrix differs from the identity
  by delta < 1 in norm). This concerns these computed vectors only: it does not exclude a small direction outside their span and does not
  convert directly into physical parameter units. Within that scope the computed nearly singular directions are
  predominantly coefficient directions, and the weak identifiability is carried by absorption.
- Verdict per selected branch: P1, F2, P3, F1 and P2 are each "incomplete" at every examined end. The check of the widths
  on the actual objective by fixed-parameter profile runs is in section 7.

## 7. Phase III: deep investigation of the selected branches

Selection. The branches for Phase III were selected at 06:48 on 30 October, before the end of Phase II at 08:30, and
the selection was amended at 07:12 after the verifier found that the first ordering had used the dyadic-shell values of
sigma_u^max and a_max instead of the core-resolved ones. Each lineage was represented by its latest end with a complete
end record. The ordering uses holdout rho_u^max on both shell families (the independent value where one
existed, otherwise the optimizer's end battery), sigma_u^max and a_max on the core-resolved sets (a_max at both the
centre and the upper weight), and sigma_Om. The core-resolution test passed its node-doubling part at all five ends
(largest relative change 2.5e-5). Its other part needs higher angular degrees and cannot be run in this campaign, so
every ordering statement below is conditional on it.

| end | (c_l, omega) | holdout rho_u^max, standard / half-offset | sigma_u^max | sigma_Om | a_max, centre / upper weight |
|---|---|---|---|---|---|
| P1 segment 4 | (0.448144, 1.406897) | 0.03762 / 0.03736 (independent) | 0.507 | 0.509 | 1.076 / 1.473 |
| F2 segment 4 | (0.447287, 1.375312) | 0.03792 / 0.03761 | 0.506 | 0.510 | 1.075 / 1.473 |
| P3 segment 3 (all-m) | (0.449822, 1.075923) | 0.04436 / 0.04386 | 0.856 | 0.542 | 2.097 / 2.410 |
| F1 segment 4 | (0.448272, 0.580171) | 0.04663 / 0.04988 (independent) | 0.631 | 0.575 | 1.568 / 2.037 |
| P2 segment 6 | (0.460063, 0.330323) | 0.05081 / 0.06333 (independent) | 2.012 | 1.359 | 2.061 / 2.061 |

The order is partial:
- P1 segment 4 is ahead of the other four ends, and F2 segment 4 is ahead of P3, F1 and P2.
- F1 segment 4 is ahead of P2 segment 6.
- P3 segment 3 is not ordered against F1 segment 4: its sigma_u^max is 1.36 times F1's.
- P3 segment 3 is not ordered against P2 segment 6: its a_max at the upper weight is 1.17 times P2's.

Unordered states both stay on the shortlist when either would, so all five ends were selected. P2 had used its 12-hour
lineage budget and received no further optimization; its Phase III measurements are the records of its last end. The
two excluded ends (P1 segment 5 and the approach from above in omega) were not eligible. A state with an open
radial-resolution flag could be ranked and selected but could not be an approximate-profile or outcome-A candidate.
The flags on the top two radial modes of the far blocks B, D and E are raised at every end and every start, and the
tests prepared to clear them were not run, so no end of this campaign is such a candidate. Beyond that common set, P1
and F2 carry one flag on the highest radial modes of block C, F1 carries four more, and P3 and P2 none.

The five ends are pairwise distinct by the registered field rule (section 4; the independent check reproduced the
closest pair, P1 segment 4 and F2 segment 4 at 0.281 / 0.275, most of it twist). The other pairs are at 0.71 to 4.30,
and apart from the closest pair no shell of any pair agrees to within 0.20 of the RMS of U. F2 is a second path from
the S01 coefficients, not an independent initialization; without it, four distinct branches remain.
- Each selected end is far from axisymmetric. Measured at unit far-field norm (optimizer end batteries):

  | end | max abs U | m != 0 share of the coefficient norm | m != 0 share of the far-field energy |
  |---|---|---|---|
  | P1 | 1.59 | 0.574 | 0.107 |
  | F2 | 1.59 | 0.572 | 0.116 |
  | P3 | 1.53 | 0.733 | 0.063 |
  | F1 | 1.52 | 0.832 | 0.137 |
  | P2 | 2.73 | 0.894 | 0.024 |

Allocation. The final validation set fixed before the selection (section 8) was not changed. Its third lineage is P3,
not F1: P3 is the only branch outside the even-m class and had no radial-resolution flag beyond the common set, while
F1 had four; as P3 and F1 are not ordered, this was a scheduling decision. Phase III time went, in order, to the
segments and end records of the final set, a perturbation repeat and the profile runs on P1, a further FREE segment of
F1, and continuations that are evidence for the parameter paths only. No breadth sample and no continuation in
(c_l, omega) was started: no end met the stationarity criteria, so there was no family of nearly stationary states to
follow.

Strategy comparison on P1. From the same P1 segment-4 state, one continuation used the production step Jacobian J_cw
with lagged closure (P1 segment 5) and the other the complete Jacobian J_c, with everything else unchanged. At each of
the 44 equal accepted counts the J_c run had the higher O1, by 0.12 to 0.80 per cent, at parameters agreeing to 1.3e-5
in c_l and 4.1e-4 in omega. It needed about 6540 s of optimizer time for its 44 accepted iterations against 1841 s for
the first 44 of segment 5 (3.6 times; the two runs shared the host with different jobs, so the ratio combines the cost
of the method with the sharing). Its worker then produced no further output and was stopped; its last state is a
periodic checkpoint without an end record and is reported as a diagnostic. On this branch and segment the comparison
gives no sign that the lagged closure of the step Jacobian is what slows the optimization; it does not test the step
Jacobian elsewhere.

Continued segments. All Phase III segments ran while processes outside the team occupied the shared host cores (from
about 06:00 on 30 October), and a Jacobian took 200 to 530 s instead of about 30 s. Wall-time caps therefore gave
fewer iterations per segment than in Phase II.
- F2 segment 5 (7200 s): 76 accepted iterations, O1 from 1.586e-7 to 1.458e-7 (8.1 per cent), omega from 1.3753 to
  1.4001 and c_l from 0.44729 to 0.44705. Its end battery gave holdout rho_u^max 0.03675 / 0.03697 (optimizer
  values), below P1 segment 4, with core a_max 1.161 / 1.589, that is 2.08 and 1.99 times the S01 values. By the
  registered branch rule it is on the P1 segment-4 branch (section 4). Its end record raised the registered exclusion
  (g) against S01 (training-grid rho_u^max 0.0360 against 0.0455, core a_max ratios 2.082 and 1.991), as for P1
  segment 5 and the approach from above; against its own entry state it raised nothing. It is a diagnostic end, the
  F2 lineage was not continued, and F2 segment 4 stayed the F2 member of the final set.
- P3 segment 4 (3600 s, all-m): 36 accepted iterations, O1 from 2.165e-7 at entry to 2.121e-7 (2.0 per cent), omega
  from 1.0759 to 1.0849, ending at (0.449800, 1.084946). Its end battery gave 0.04376 / 0.04329 (optimizer values;
  1.3 per cent below segment 3), with core a_max 2.206 / 2.532, 1.33 and 1.32 times the S20 start. Its end record
  raised no exclusion (training-grid rho_u^max 0.907 times the start), and it replaced segment 3 as the P3 member of
  the final set. A fifth segment (allowance 3600 s; recorded optimizer time 4361 s) started at 10:00 from this end; it is evidence for the parameter path only
  and could not be a final state. It ended by its time limit after 30 accepted iterations, O1 from 2.121e-7 to
  2.035e-7 (4.1 per cent), omega from 1.0849 to 1.0949 and c_l from 0.44980 to 0.44978 (optimizer values). The
  producer's end battery, evaluated on the end state normalized to unit far-field norm, gave holdout
  rho_u^max 0.04279 / 0.04238 (segment 4: 0.04376 / 0.04329), training-grid rho_u^max 0.04225, sigma_u^max 0.473 /
  0.418 and core a_max 2.397 / 2.745, about 1.44 and 1.43 times the S20 start (standard / half-offset shells,
  centre / upper weight for a_max). Its end record raised no exclusion against the P3 start (training-grid
  rho_u^max 0.886 times the start; checked independently), and the flags on the top radial modes of far-field blocks B, D and E stayed raised.
- F1 segment 5 (allowance 7200 s; recorded optimizer time 7431 s): 97 accepted iterations, O1 from 2.039e-7 to 1.930e-7 (5.3 per cent), omega from 0.5802 to
  0.6028 and c_l from 0.44827 to 0.44817 (optimizer values). The producer's end battery, evaluated on the end state
  normalized to unit far-field norm, gave holdout rho_u^max 0.04550 / 0.04857 (segment 4: 0.04663 / 0.04989),
  sigma_u^max 0.427 / 0.458 and core a_max 1.616 / 2.085 (standard / half-offset shells, centre / upper weight for
  a_max). F1 is not in the final set (section
  8), so this segment is evidence for the parameter path only. Its end record raised no exclusion against the F1
  start (core a_max 1.65 and 1.56 times the start, training-grid rho_u^max 0.696 times the start; checked
  independently), and the flags on the top radial modes of the far-field blocks stayed raised.

Perturbation repeat on P1 (criterion 7.4 (e)). The P1 segment-4 end was perturbed (the coefficients so that the
training-grid field changes by a relative 1e-3, z_c and z_w by 1e-3) and run as a fresh FREE job under the segment time
cap (optimizer values). Entry O1 was 7.15e-4, 99.97 per cent of it from the gauge row; after 41 accepted steps O1 was
1.501e-7 at (0.448039, 1.420300). The parameters stayed within the 1 per cent widths (log omega +0.0095, about 0.2 of
the stiff half-width; c_l -1.0e-4), but O1 ended 3.9 per cent below the segment-4 value: the repeat continued the
descent instead of returning, as the label "incomplete" of section 6 implies. At equal accepted steps it tracked the
unperturbed continuation (P1 segment 5): O1 ratios 1.0082 to 1.0069 from 12 to 41 steps, parameters within 4e-5 in c_l
and 3.2e-3 in omega. Its end (holdout rho_u^max 0.03708 / 0.03705) raised exclusion (g) against S01 at the margin:
training-grid rho_u^max 0.0364 against 0.0455 and core a_max 2.0003 and 1.912 times the S01 values; against its own
perturbed start it raised nothing (1.033 and 1.032). The independent check reproduced the classification and the
margin (0.014 per cent of the threshold) from the stored values. The margin has no error bound for quadrature,
maximization or field evaluation, so this is a registered classification, not a certified one. It is a diagnostic end
and changes no member of the final set.

Reduced sensitivity at the selected ends: section 6 (P1 segment 4, F2 segment 4, P3 segment 4, F1 segment 4, P2
segment 6); every selected end fails (b) and (d) of criterion 7.4. The fixed-budget profile at P1 below found no point
lower than the reference run after equal accepted iterations.


Profile design. On the top-ranked branch nine FIXED runs were planned with the same budget (at most 40 iterations and
1800 s each), the same objective, map, gauge and grids: a reference run at the base parameters and one run at each of +-1 and +-2 times
the 1 per cent half-width along both eigen-directions of the reduced parameter matrix. Every run starts from the base
coefficients kept, the eliminated tail coefficients following the parameters. A linear-response start (the
coefficients moved by the linearized response to the parameter change) was considered and evaluated at iteration 0 at
all eight points before any run, and was not used: it moved the reduced coefficients by 24 to 118 per cent and the
field by 7 to 809 per cent, far outside the validity of its own linear model, and its lower iteration-0 O1 at the soft
points came only from the gauge row, while its non-gauge O1 was 2.3 to 2100 times that of the kept start at every point.
The kept start enters with a non-gauge O1 of 28 to 232 times the base value at the soft points and 1.3 to 2.3 times at
the stiff points. The values reported are therefore "profile values after a fixed budget", not profile minima; a point
counts as lower than the base only if its value after the budget is below that of the reference run, and a higher
value at a soft point may be limited by the budget.

Profile values after a fixed budget (O1 in total, with the part outside the gauge row in parentheses; k* = 7 is the
smallest accepted count among the completed points, that of stiff -2, so every point is read after 7 accepted
iterations and at the end of its budget; optimizer values):

| point | (c_l, omega) | entry O1 (outside gauge) | accepted, stop | O1 after 7 (outside gauge) | O1 at end (outside gauge) | reading |
|---|---|---|---|---|---|---|
| reference | (0.448144, 1.406897) | 1.5616e-7 (1.513e-7) | 12, time | 1.5543e-7 (1.5541e-7) | 1.5455e-7 (1.5454e-7) | reference |
| soft -1 | (0.467414, 1.443544) | 74.35 (1.42e-5) | 40, iterations | 58.73 (1.52e-3) | 19.51 (5.54e-3) | not lower; budget-limited |
| soft +1 | (0.428874, 1.370250) | 68.78 (4.24e-6) | 40, iterations | 1.234e-3 (1.18e-3) | 9.60e-4 (9.59e-4) | not lower; budget-limited |
| stiff -1 | (0.448149, 1.339223) | 3.033e-2 (1.953e-7) | 39, time | 1.6028e-7 (1.6027e-7) | 1.5771e-7 (1.5771e-7) | not lower; still falling |
| stiff +1 | (0.448139, 1.474572) | 3.328e-2 (2.002e-7) | 10, time | 1.6450e-7 (1.6447e-7) | 1.6441e-7 (1.6441e-7) | not lower; budget-limited |
| stiff -2 | (0.448154, 1.271548) | 0.1157 (3.203e-7) | 7, time | 1.7197e-7 (1.7165e-7) | 1.7197e-7 (1.7165e-7) | not lower; budget-limited |

The independent check reproduced the stored arithmetic of all six completed points and of the comparison at the
common count of 7 accepted iterations from their saved checkpoints, histories and entry records, without recomputing
a field. Neither soft point gives a profile value. At soft -1 the run was still removing the gauge-row
defect of the kept start after 40 accepted iterations (gauge row 74.35 to 19.50) while the rest of O1 rose by a factor
390. At soft +1 the gauge row was removed within about 12 iterations, after which the rest of O1 stayed four orders
above the reference (7.6e3 times at 7 iterations, 6.2e3 times at 40); it had risen by a factor 226 from entry. The
battery of each end, evaluated on the end coefficients divided by their far-field norm (a 5.9 per cent rescaling at
soft -1, below 1e-5 elsewhere; rescaling is not a symmetry of the residual, so these are values of a nearby field, not
of the optimizer end), gave holdout rho_u^max 0.80 and 0.57 against 0.0375 at the reference. The reduced quadratic
model places the soft points at a rise of 1 per cent, so these runs bound the fixed-parameter minimum from above only
and do not check the soft width on the actual objective. The reference run itself lowered O1 by 1.0 per cent in 12
accepted iterations at the base parameters, a further sign that the coefficient part of the P1 segment-4 end is not
converged.

On the stiff direction the kept start is close to the base field and the runs give readable values. The points at -1,
+1 and -2 half-widths (omega 1.3392, 1.4746 and 1.2715, c_l unchanged to 1e-5) removed the gauge row within the first
iterations. After the same 7 accepted iterations their O1 was 3.1, 5.8 and 10.6 per cent above the reference (10.4 at
-2 outside the gauge row), against 1, 1 and 4 per cent predicted by the reduced model. At its end stiff -1 was 2.0 per
cent above the reference's end after 39 against 12 accepted iterations, still falling by 0.2 per cent per 10
iterations; stiff +1 and stiff -2 had only 10 and 7 accepted iterations within their time caps. All these runs are
limited by the budget, so the values are upper bounds of the fixed-parameter minima, and their differences bound the
stiff width in neither direction. What they show is that after seven accepted iterations the reference run reads lower than every
stiff neighbour, by 3.1, 5.8 and 2.7 times the rise that the reduced model predicts at these three points. Their normalized-state
batteries gave holdout rho_u^max 0.0380 / 0.0379 (stiff -1), 0.0374 / 0.0370 (stiff +1) and 0.0387 / 0.0387 (stiff -2)
against 0.0375 / 0.0373 at the reference, so the residual measure of the report moves by at most 1.6 per cent at +-1
and by 3.2 and 3.8 per cent at -2, where O1 moves by 3 to 11 per cent. The points stiff +2, soft -2 and soft +2
were not run: the registered rule that keeps FREE runs at 80 per cent or more of the optimization count (section 12)
refused every start of stiff +2, retried every 5 min, up to the last start time of the profile queue (15:36 on 30
October, so that a run would end within Phase III); the queue then ended at 15:38 without starting it, and the two
soft points queued after it were not reached (checked independently).

## 8. Final validation (Phase IV)

Design. The final set was frozen once, at 12:23 on 30 October, and evaluated by the independent route only. The frozen
cohort has eight role entries and seven distinct inputs: the frozen FREE states of P1, F2 and P3; the saved starts of
P1 (S01) and P3 (S20), with S01 entered a second time as the start of F2 (the same checkpoint); and the fixed-parameter
controls of P1 (360 accepted iterations at (0.45, 1.0)) and P3 (194 accepted iterations). Six distinct inputs were
scheduled for primary evaluation: the three FREE states, the two saved starts and the P1 FIXED-CONTROL end, which is
the denominator of the outcome-A test for P1. The F2 start entry was to take the value of the S01 evaluation, after an
audit that the two inputs are identical. The P3 control entered only the origin test of the prelude and had no
primary evaluation, for lack of time, so P3 has no final FREE against FIXED-CONTROL comparison. Each state entered as its saved coefficients,
checked bitwise against its checkpoint, with no rescaling, regauging or refit. After the set and the evaluator were
frozen, a seed was drawn from operating-system randomness and recorded; the holdout angles, the pressure-source phase
and the vorticity points were derived from it. No final value fed any later optimization or selection.

The primary evaluation computes the full-space pressure and the momentum residual by the independent route at 12
radial nodes per evaluation domain on a fresh 42 by 84 angular grid, at two pressure levels: (radial order, angular order,
azimuthal points) = (24, 64, 128) and (40, 80, 160). It reports rho_u^max on the standard and the half-offset dyadic
shell families; RMS residuals on a separate set of 13 common physical shells (from 0.3 2^j to 0.3 2^(j+1), j = -4 to
8); origin-centred core balls (radii r_core/32 and r_core/256 with the common reference core radius r_core, the unit
ball and the innermost ball of each family); and unweighted physical RMS residuals beside the weighted values at each
state's own c_l. These core balls are centred at the origin. They are not the balls centred at the vorticity maximum
on which the core a_max of sections 3 and 7 is measured; no final operation recomputes that a_max, and the final
check of those displaced balls was not made. Separate operations evaluate the far-field blocks (P1
FREE only), the five vorticity-residual terms, the finite-ball energy and helicity identities and the first nonlinear
far-field coefficient (each FREE state), and a Cartesian pressure-Poisson check (P1 FREE). A prelude evaluates the curl
of the momentum residual at the origin in exact interval arithmetic for all seven distinct inputs. The 17 operations
were scheduled to run one after another, each under a fixed time cap (40 min for an even-m primary, 50 min for an
all-m one, 55 min for the far blocks, 1 to 10 min for the others; 364 min in all, within one 397-min aggregate with a
hard stop at 19:00:31). A value whose operation reached its cap is reported as partial and is not used for the
outcome category. Where the change between the two pressure levels is comparable to a claimed difference, that
difference is not claimed.

The caps were sized from two completed runs of this evaluator at these pressure levels on 29 October, 23.6 and 25.0
min for two P1 states (even-m), before processes outside the team loaded the host (section 12). At 07:38 on 30
October, after a development run of the same evaluator for the F2 FREE state (even-m) had used its whole 70-min cap
under that load and completed only its first pressure level, the registered caps, aggregate and order were
retained, with no retry or extension; the cohort itself was sealed later, from 12:10. The final evaluator ran on
one CPU core with one thread; the host load average, sampled every 10 minutes during the final test, was 75 to 361.

Before the freeze, at 10:04 on 30 October, a launch check found that the admitted common driver could not start its
operations: the operation script accepted only one form of its parent process, and the driver's launcher used another.
The repair changed that parent condition and the hash bindings of the files that depend on it (driver, guard and
timer), and no evaluator, grid, cap, role or time of the schedule. The lead compared each repaired file with its
predecessor after the registered renames: apart from the plan document, only the parent condition and one binding
statement differ. The repaired chain
was accepted at 10:15 and admitted by the verifier at 10:18. The timer that seals the set and starts the driver was
armed at 11:31 on the verifier's CPU core, with no GPU visible to it. The seal ran from 12:10:07 to 12:11:21 and
selected the P1, F2 and P3 segment-4 ends with the saved starts and the retained controls, all with the common
reference core radius 0.41928. Idle checks at 12:10:04, 12:20:00 and 12:23:23 found no competing process among
the processes the verifier could inspect; processes it could not inspect were counted and are outside the check. The same process became the driver at
12:23:31. Its prelude froze the set and the evaluator (completed at 12:23:36.7), drew the seed immediately after the
freeze and ran the origin test; it took 8.6 s by its own record (12:23:34.9 to 12:23:43.6; 11.3 s between the
driver's start and end entries for it).

Results. None of the primary evaluations completed. Four were attempted, one after another, and each reached its
40-min cap (2400 s, which includes a reserve for cleanup) before its second pressure level; at the cap each
operation's processes were stopped and its partial output was kept as partial evidence only. The verifier's
post-exit review of the receipts admits a value only if its operation completed under its cap with matching,
unchanged receipts, so no final value of rho_u^max, of the RMS residuals or of the core balls is available.

| role | frozen state (checkpoint SHA-256 prefix) | primary evaluation (UTC, 30 October) | stage reached |
|---|---|---|---|
| P1 FREE | P1 segment-4 end (1b16c729) | 12:24:12 to 13:04:08, cap reached (2396 s) | pressure source of level 1 assembled (13:01:41); no level completed |
| P1 and F2 start | S01 (83aa4c6e) | 13:04:08 to 13:44:04, cap reached (2396 s) | level 1 completed (13:43:21); level 2 begun |
| P1 FIXED-CONTROL | 360-iteration end (7d3bc6ea) | 13:44:04 to 14:24:01, cap reached (2397 s) | pressure source of level 1 assembled; no level completed |
| F2 FREE | F2 segment-4 end (9bc23af7) | 14:24:01 to 15:04:00, cap reached (2399 s) | pressure source of level 1 assembled (14:51:02); no level completed |
| P3 FREE | P3 segment-4 end (7bb8add5) | not attempted | none |
| P3 start | S20 as entered by the P3 runs (000bc907) | not attempted | none |

One completed level does not give the two-level comparison that the evaluation requires, so the level-1 value of
S01 is not reported. After the fourth cap the driver's cleanup of that operation returned after 4.05 s without
confirming that the last process of the evaluator had ended. By design the driver then stopped the sequence,
at 15:04:00, instead of starting a further operation beside a process that might still be running; its closing
cleanup confirmed within 0.2 s that the process had ended. The remaining 13 operations were not attempted: in the
order of the plan, the eight complementary operations of the P1 and F2 FREE states, the primaries of the P3 FREE state
and the P3 start, and the three complementary operations of the P3 FREE state. The rulings in force (no retry, extension,
reordering, resampling or added operation, from 13:09; no relaunch, from 15:08) kept this as the result of the final
test. The final comparison of FREE, FIXED-CONTROL and start states on fresh holdout points was therefore not
obtained. The FREE, FIXED-CONTROL and start comparisons of sections 3 and 5 rest on the earlier independent
evaluations at their own holdout points; they are not final-test values.

The hash prefixes identify the checkpoint files in the accompanying artifacts, except for the P3 start: that is the initial state saved by the P3 runs, which an
independent provenance check of 73 items tied to the S20 start file (5093bad5) and found bitwise common to the P3
FREE and FIXED-CONTROL runs. Its decoded coefficient vector, with the hash of that checkpoint, is in
the accompanying artifacts.

None of the complementary operations (far blocks of P1 FREE; vorticity terms, energy and helicity identities and
first nonlinear coefficient of each FREE state; Cartesian check of P1 FREE) ran. Those of P1 and F2 depended on a
completed primary evaluation of their state; those of P3 were scheduled after the P3 primaries.

At the origin (the prelude, which completed; its receipts and values were checked independently after the exit, 526
checks) the residual curl excludes
zero at all seven inputs. At the even-m states only its axial component is nonzero; relative to the axial vorticity
it is 0.94 at the P1 FREE state, 0.29 at S01, 0.69 at the P1 FIXED-CONTROL end and 0.95 at the F2 FREE state. At the
all-m states all three components are nonzero; the axial ratio is -0.078 at the P3 FREE state, -0.018 at S20 and -0.109
at the P3 fixed-parameter control.

Outcome category. E is not raised. The time and cleanup limits of the final test leave its coverage incomplete; they
do not themselves establish a new derivative, field-consistency or pressure-accuracy failure (no final
pressure-accuracy test completed), and the separately validated evidence of sections 2 to 7 keeps its dated scope. A needs completed final-test values for two
independently initialized FREE runs, and was in any case excluded by the open far-block flags of section 7. No
selected end meets the stationarity criteria of section 6, so B is not met. The three frozen ends (P1, F2 and P3)
are therefore in category C: at each, O1 was still falling by 2.2 to 6.0 per cent over the last 50 accepted iterations
and the complete scaled gradient was 0.025 to 0.047. The qualifier D holds at the P1 and F2 ends, where after
elimination of the coefficient directions 5.4e-6 of the c_l column and 2.0e-4 to 2.2e-4 of the omega column remain;
at the P3 end the corresponding values (3.9e-6 and 3.1e-4) are conditional on the saved factors (section 6). The F1 and P2 ends, which were not in the final set, fail
the same criteria in the section 6 records and show the same absorption. The campaign category is C with qualifier
D. No ordering of the branches by the final protocol was established; the ordering of section 7 rests on the earlier
values and is conditional on the core-resolution test. The verifier confirmed this category at 15:08 on 30 October,
from the receipts of the final test and the section 6 records.


## 9. Performance (deliverable C)

Resources. The optimization side had two A100-SXM4-80GB GPUs (shared with other projects) until 00:57:59Z on
29 October, none until 02:51:04Z, three from then and seven from 17:09:05Z; the independent checks had one GPU
throughout except in the withdrawal. Both sides were limited to four and one CPU cores, and the optimization side to
four concurrent computations, so the seven GPUs let each job run alone on a device but added no concurrent jobs.
Of the 207.5 GPU-hours assigned to the optimization side up to 15:24 on 30 October, when its last GPU job ended (no
job ran after it), 106.9 were charged to its jobs of all labels. The difference is assigned time not charged to any
job, not a measured utilization; it arose mostly because at most four computations could run at once while seven
GPUs were assigned, for about two hours because restored GPUs were not noticed, and in part because the GPU work
before the withdrawal of 29 October was not charged by label (section 12).

GPU cost of one iteration (S01, 1469 coordinates, 433,009 residual rows, configuration M, one job alone on an A100):
44.0 s per accepted iteration over 5 iterations (38.7 to 41.0 s after the first). Components: step-Jacobian build over
all coordinates 28.6 to 30.4 s, the two separately computed parameter columns 7.7 to 8.2 s, normal equations 0.13 s,
linear solve 0.003 to 0.016 s, 1.2 s per trial evaluation (residual and double-double pressure chain). Peak GPU memory
was 26.2 GB in this test; the production jobs recorded 24.3 to 25.4 GiB (even-m) and 40.4 to 40.5 GiB (all-m). The
earlier profiling run recorded a mean utilization of 20 per cent of the whole device (including other projects) in a
float64 timing run of one job. From 08:40 on 30 October the device utilization and memory and the host load were sampled every 10 minutes (in
the accompanying artifacts). In the 41 samples up to the end of the last job (08:40 to 15:21), one to four of the
seven optimization-side GPUs held memory at each sample, a device that held memory showed a mean utilization of 9
per cent (median 2 per cent), and the mean over all seven devices was 3.6 per cent; at most 47,933 MiB (46.8 GiB) of
memory was in use on one device. The device of the independent checks showed no use at any sample. The host load average was 39 to
361 (median 158). The low device use is consistent with jobs limited by the contended host cores (section 12); no
matched measurement isolates this. The complete Jacobian J_c costs about 70 s to complete from J_cw on a GPU. The production searches of Phases I and II
used J_cw for their steps, and J_c was evaluated separately at segment ends; in one smoke run, an LM step with J_c as
the model took 121 s (an upper bound from one iteration that included an optional 5 GB save), about 3 times a
production step.

FREE against FIXED-CONTROL cost. Over the paired segments the cumulative optimizer time per accepted iteration was 47.7 s
(FREE) against 19.6 s (FIXED-CONTROL) at P1 and 38.8 s against 14.9 s at P2, ratios 2.4 and 2.6. The two parameter
columns account for about 8 s of the 28 s difference at P1 and a longer step-Jacobian build for about 17 s; the cause
of the longer build (the FREE graph keeps the parameter dependence of the basis, maps, tail constraint and row
scalings live) is a reading of the code that no matched profile has tested. In the all-m class the mean Jacobian time
per step was 76 s (FREE, including 8.9 s for the parameter columns) against 29.8 s (FIXED-CONTROL) in the first hour,
and 81 to 90 s plus 12 to 14 s against 35 s in the second, when all four host slots carried heavy jobs.

Throughput. FREE jobs alone on a GPU made 88 to 93 accepted iterations per hour in the even-m class; while two jobs
shared a GPU, 72 to 84 per hour (the periods are not matched, so the effect of sharing was not isolated). FIXED-CONTROL
members made 184 to 246 per hour. The all-m FREE member made 44 and then 33 accepted iterations per hour. Within equal
nominal allowances the FREE members therefore stopped on the time limit with fewer iterations than their controls.

CPU (S01, one thread, configuration M): projected 2414 s per accepted iteration (2396 s in float64); the step Jacobian
dominates (74 per cent). A measured repetition on one thread gave 2525 s per iteration. The GPU iteration (44.0 s) was therefore about 55
(projected) to 57 (measured) times faster than the one-thread CPU iteration; multi-thread CPU scaling was not
measured, so this is not a statement about a 55-thread CPU run. With four heavy jobs on the host the GPU
per-iteration times rose by 20 to 40 per cent; contention for the four host cores is the proposed explanation, not
isolated by a matched experiment.

Totals. Charged GPU-hours by label: FREE 65.25, FIXED-CONTROL 5.65, PROFILE 4.22, SMOKE 2.01, VALIDATION 26.63 and
EVAL 3.14, 106.90 in all (section 12). Supervised optimization jobs: 64 attempts of 55 distinct jobs, of which 48
attempts ended with the worker's completion flag set (section 12). Peak GPU memory per production job: 24.3 to 25.4
GiB (even-m) and 40.4 to 40.5 GiB (all-m).

## 10. Conclusions (deliverable D)

1. Did freeing c_l and omega materially improve the optimization? Not by the registered measure. In the three
   measured pair comparisons FREE ended 0.7 to 6.8 per cent below FIXED-CONTROL in holdout rho_u^max, with a higher
   sigma_u^max in P1 and P2, and both members raised the absolute core residual above the start. The outcome A margins
   (final-test rho_u^max at most half of the start and of the matched control) are far from met: the lowest
   optimizer-side holdout value of any admissible end, 0.0376 (P1 segment 4), is about 0.82 of the independently
   recomputed P1 start value 0.0460 (a quotient of two different protocols, context only). The final test that was
   to measure this on fresh holdout points did not complete (section 8), so the answer rests on the earlier
   independent values.
2. Are the parameter values reproducible across starts? Not across independent starts. The five ends selected for
   Phase III are pairwise distinct branches by the registered rule. The two lineages that started from the same S01
   coefficients at different parameters, P1 at (0.45, 1.0) and F2 at (0.4597, 1.3389), reached one branch near
   (0.448, 1.40 to 1.41) one F2 segment later (field distance 0.055, parameter difference within the widths at both
   states); they are not independent initializations, and the F2 end on that branch is excluded by the core rule. The
   two that started at the same parameters from different saved states (P2, F1) moved apart in omega (0.33 against
   0.58), and the all-m P3 lineage stays near omega 1.08. Every lineage was still drifting in omega at its latest end,
   so these are positions along unfinished descents, not reproduced parameter values.
3. Did the joint optimizer reach credible stationarity? No. Each examined end fails the progress criterion (a) of
   7.4 and carries the label "incomplete"; each also fails (b) and (d) (section 6; at one end (b) fails through the
   reduced predicted decrease alone, because eta(1e-8) is not determined there). The perturbed restart of the P1
   segment-4 end (criterion (e)) stayed within the 1 per cent parameter widths but did not return to the O1 of that
   end: it continued downhill along the unperturbed continuation, to an O1 3.9 per cent lower after 41 steps. At fixed parameters, the reference profile run lowered O1
   by a further 1.0 per cent in 12 iterations, so even the coefficient part of that end is not converged.
4. Which terms or regions dominate the remaining residual? In O1 the core and intermediate rows (about 96 per cent at
   the P1 segment-3 end). In the independent evaluations the maxima of sigma_u and of the weighted absolute residual of
   P1 lie on displaced core balls, and at P2 on one dyadic shell where the RMS residual exceeds the RMS of
   (1 - c_l) U. Along every lineage the normalized shell measure fell while the absolute core residual rose. For each
   saved field examined (the segment-1 ends of both members of the P1 and P2 pairs, the P1 and P2 segment-4 ends,
   the F1 and F2 segment-2 ends and the P3 FREE segment-1 end), the curl of the momentum residual at the origin, evaluated exactly from the saved binary
   coefficients in rational interval arithmetic, excludes zero; since the curl of grad P vanishes for every twice
   differentiable pressure, none of these represented fields satisfies the momentum equation exactly for any such
   pressure. Its axial component relative to the axial vorticity at the origin grew in magnitude along P1 (0.28 to
   0.94 at segment 4) and P2 (-0.42 to -0.74) while O1 fell. These statements concern the listed saved fields only;
   they exclude no nearby field and give no distance to a solution. At the frozen states (section 8) the axial ratio is
0.94 at the P1 FREE state against 0.29 at its start and 0.69 at the P1 FIXED-CONTROL end, so the growth is not
specific to free parameters; at the P3 states it is -0.078 (FREE), -0.018 (start) and -0.109 (control), with nonzero
transverse components.
5. What does the evidence point to? To an incomplete optimization of a badly conditioned problem (outcome C), not to
   a measured representation limit. O1 still fell at every segment end; the linear model at every end offers a
   decrease of 4.8 to 14 per cent of O1; the coefficients absorb almost all of the first-order effect of c_l and
   most of that of omega (qualifier D: weak parameter identifiability), while the 20 computed right singular vectors
   of the smallest singular values have parameter content at most 8e-13 each in column-scaled coordinates (section 6). The pressure and derivative validation found no
   open failure that decides a result, except the S11 directional-derivative failure, whose attribution is open
   (section 2). On P1, a continuation that used the complete Jacobian for its steps made no faster
   progress per iteration than the production continuation and used about 3.6 times as much optimizer time (section
   7), so the lagged closure of the step Jacobian is not shown to be the cause of the slow decrease.
6. What would justify degree 8? Each of the following would be needed and none exists at degree 6 now: (a) a branch
   that meets credible stationarity with a residual materially above the discovery threshold; (b) the same stationary
   state, within its parameter widths and to 10 per cent in the field, reached from two independent initializations;
   (c) evidence that the residual left at that state is carried by angular structure that degree 6 cannot represent
   (for example the share of the residual outside the range of the linearization concentrated at the highest
   represented degree, or angular energy at degree 6 not decaying); (d) no open derivative, pressure or field
   consistency failure. Degree 8 was not run.

## 11. Reproducibility (deliverable E)

The accompanying artifacts include layout descriptions, exact commands and checksum lists. Their provenance
record relates the published files to the byte-exact originals accepted by the verifier and records publication
changes. Local machine paths in text were replaced by relative labels; the resume helper also resolves the
relabeled starting-state paths. The binary checkpoints are unchanged. Historical scripts that require the original
experiment tree cannot all run from the published subset alone. The accompanying artifacts contain:

- Optimization records: the production code of the campaign (representation, residual, pressure solver, optimizer, job
  worker, queue and slot control), copied from the previous campaign's frozen code with versioned changes and a
  hash for every production file; the derivative-gate, end-record (6.3 (a)), stationarity (complete Jacobian) and
  branch-distance records; the immutable starting states; for every job its configuration, its worker log (one line
  per accepted iteration: O1, damping, parameters, timing; end-of-segment batteries) and its end record; the job
  ledger and the GPU-hour accounting; the status of every lineage segment with the hash of its
  end state. Periodic checkpoints are not included.
- Checkpoints: the segment-end checkpoint (coefficients, parameters and optimizer state) of every
  selected or frozen end: the inputs of the final test, frozen at 12:23:36, and
  additional selected, superseded, excluded or later Phase III ends and the P3 fixed-parameter control, listed for
  information after the final cohort was sealed; these additions do not change the final cohort.
- Independent checks: a subset of the independent verifier's archive: the review and sign-off of the outcome
  category; the frozen cohort, registered plan and observed operations of the final test; the independent holdout
  recomputations, freezes, widths, pair comparisons and origin checks of the end states quoted here; the decoded P3
  initial coefficients; the independent field, pressure and residual code; the mathematical arguments with their
  verification notes. The complete archive (15,616 files, 349 MB, built at 16:12 on 30 October after the final test
  ended at 15:04) was checked by the verifier but is too large to publish; its manifest digest is in the accompanying artifacts.
- Analysis outputs: the outputs of the analysis of sections 4 to 6, together with
  the scripts that made them and their self-tests (python 3.12 with numpy; the field-distance and sensitivity tools
  also need torch; no GPU).
- Specification: the registered specification with every dated amendment.
- Detailed validation history: the long working report of the campaign as of 02:12 on 30 October (Phases I and II),
  with the intermediate values, derivations and corrections that sections 2 to 6 condense; it was not updated later,
  and where it differs from this report, this report holds.
- Data-custody receipt: the raw arrays of the Phase I directional-derivative test at S09 (141 files, 806 MB with
  hard-linked aliases, 419 MB of distinct data) are not included because of their size. During the run they were
  copied byte for byte out of the independent-check storage, with each hash checked before and after, to make room
  for the final validation, and the originals were then removed. The receipt lists every file with its size and
  SHA-256; the copies are kept with the campaign's working files, not in the artifacts. The derivative-gate results
  that cite these arrays are summarized in section 2 and recorded in the complete independent-check archive; the gate
  records of the optimization side are in the accompanying artifacts.

The accompanying artifacts give exact relative paths for these checkpoints and the saved starts, with the
SHA-256 prefixes of the frozen files listed in section 8.

Environment. The optimization code runs under python 3.9 with torch 2.8 for CUDA 12.8 on A100-SXM4-80GB GPUs (the
environment of the previous campaign, unchanged). The independent checks run on one CPU core with one numerical
thread. Pressure values that enter the optimization residuals use the double-double chain (configuration M).

Resuming a run. The accompanying artifacts give an exact command to continue a published end state using the
Python environment above. Its arguments are the end state, the GPU index (or cpu), the number of further LM iterations
requested, a new scratch directory and the LM time allowance in seconds. The helper copies the code, the starts and
the end state into the scratch directory (it refuses an existing one), writes the job file with relative paths and
the label SMOKE, and runs the worker, which resumes from the checkpoint by its production path, logs the initial O1
and requests the further iterations. Three caveats apply. The number given requests outer LM iterations; it does not
guarantee accepted ones, since a rejected trial changes the damping and the counters and may use up an iteration.
The allowance is checked between iterations and covers neither the initial objective nor the end battery. The
production worker limits every LM segment by a fixed campaign stop time (keeping 25 min for the end battery and
allowing at least 60 s); in the scratch copy of the worker the helper replaces that fixed stop by a stop one year
after the command starts, and records the original and patched hashes alongside the resumed job. The
published code is not modified. Two tests of this procedure on the P1 segment-4 end were made during the run: the
first with an earlier helper that lacked this patch, which was not needed before the stop, and the second with the
campaign helper before publication path changes (one GPU, 20 min of wall time on the loaded host, of which 562 s were LM and 212 s the
end battery). Both resumed at iteration 587 with the recorded counters, with initial O1 1.56157196650390341e-7, the
objective recorded for the saved iterate, and their one accepted step reached O1 1.5581166e-7 at (0.44814122,
1.40728638), the first accepted iterate of the production continuation (P1 segment 5). An independent check of both
tests confirmed that they end at the same coefficient vector; the full vector of the production step was not kept,
so its equality with that step is checked only through its recorded digest and scalar values. The accompanying
artifacts also give commands for the original experiment tree: the worker run on a run directory, and a
continuation segment through the enqueue script. The publication path correction has not been tested by rerunning
the optimizer.

The final status of every lineage segment (ended, excluded, frozen, selected, control or diagnostic), with the hash of
its end state, is in the accompanying artifacts (final version of 15:46 on 30 October).

## 12. Time and resources

Real start 2026-10-28T20:30:31Z. The last GPU job ended at 2026-10-30T15:23:36Z (42 h 53 min after the start); after
it only the accounting, the packaging of the artifacts and this report were completed, the report at 2026-10-30T16:16Z
(43 h 45 min after the start), and was accepted by the independent verifier. The schedule stopped the team at 47
hours of the 48-hour budget (19:30:31Z) so that the write-up would finish inside it; the team had finished earlier and
was stopped at 2026-10-30T16:26:44Z (43 h 56 min after the start). The campaign report, with a shorter summary and
the published artifacts reduced to under 50 MB (no new computation), was completed at 2026-10-30T16:40:38Z (44 h 10 min 7 s after
the start), within the 48-hour budget. Phases I to IV were undertaken; the final test of Phase IV ended incomplete by
its caps (section 8). The GPU time used by the independent checks on their one GPU was not charged by label and is not
in the totals below. Hardware: A100-SXM4-80GB GPUs shared with other
projects, as in section 9; the optimization side had four CPU cores and at most four concurrent computations, the
independent checks one core, coordination one core at low priority. The largest host memory in the memory logs of the optimization
side is 27.4 GB, for a one-thread CPU iteration; the logs do not cover every process. At 15:30 on 30 October the
working directories of the optimization side, the independent checks and coordination held 9.7, 8.8 and 0.5 GiB; the
free space of the shared file system, used mostly by other work, was never below 50 GiB in the readings of the run
(lowest at 05:44 on 30 October). All GPUs were withdrawn for other work from 00:57:59Z to 02:51:04Z on 29 October; no
production optimization had started, and the restored GPUs were not noticed until 04:37Z to 04:55Z, so about two
hours of GPU time went unused while CPU-only work continued.

GPU-hours by label, final (checked independently against the recorded events): FREE 65.25, FIXED-CONTROL 5.65, PROFILE 4.22, SMOKE 2.01, VALIDATION 26.63 and EVAL 3.14,
106.90 in all. They are charged to supervised jobs, hand-launched runs and launcher commands from the restoration of
the GPUs at 02:51 on 29 October, and to two supervised resume tests of 28 October; each failed attempt is closed at
its first terminal event, and launcher commands are paired with their ends by their exact command text. (Pairing
each end with the earliest open command instead, as an earlier version of the accounting did, lengthened three
validation commands and dropped a fourth; the correction removed 0.48 GPU-hours of VALIDATION and changed neither
share below.) The GPU
work before the withdrawal of 00:57:59Z on 29 October (smoke, gate, derivative-test and profiling runs on two GPUs)
is listed by job in the accompanying artifacts and is not in these totals, except that its 2.53 hours of recorded
optimizer work (2.16 interval hours of optimizer runs and 0.37 measured hours of three LM trajectories) are in the
registered count below. The registered denominator of the queue mix is all coefficient optimization of any label: FREE, FIXED-CONTROL, PROFILE, DIAG, refits of initial states (three least-squares coefficient refits of saved fields, 0.46 GPU-hours, run under the label VALIDATION) and optimizer runs made as tests (SMOKE jobs and validation trajectories), with the wall hours of coefficient optimization on CPUs added. At the end it was 81.28 hours, of which FREE was
80.28 per cent and FIXED-CONTROL and PROFILE together 12.13 per cent. The count was not complete during the run. When the early hand-launched test runs of 28 October, the validation LM trajectories and the CPU hours were added to the record, FREE was 78.9 per cent of the recorded count at 03:53Z on 30 October, below the floor, and by the queue rule only FREE jobs were started until it was above 80 per cent again. It crossed 80 per cent between 04:39Z and about 05:00Z (an independent capture near 05:00Z gave 80.25 per cent; the first write of the campaign ledger at or above 80 per cent was at 05:24Z, 80.5 per cent). 78.9 per cent at 03:53Z is the lowest value found in the dated ledger records of the run; the share at every earlier moment under the final, complete record was not reconstructed. Without the test runs and the CPU hours the denominator is smaller, so the FIXED-side share computed that way bounds the registered one from above; it was 11.9 per cent at 03:53Z and 13.05 per cent at the end (narrow denominator 75.58 hours, FREE 86.34 per
cent), below the ceiling of 15 per cent. Supervised optimization jobs (FREE, FIXED-CONTROL, PROFILE and SMOKE) made 64
attempts of 55 distinct jobs: FREE 47 attempts of 40 jobs, FIXED-CONTROL 9 of 7, PROFILE 6 of 6 and SMOKE 2 of 2. Of
the 64 attempts, 48 ended with the worker's completion flag set, 10 ended without it and 6 with a job error; 7 of the
55 jobs never set it. A job that is resumed after a stop counts again as an attempt. Launcher-side validation and
evaluation commands and hand-launched runs are outside these counts.

The optimization side's limit of four concurrent computations was exceeded by one computation in seven reported
intervals, 27 min 7 s in total by the reported times (06:17:51 to 06:21:35Z, 08:02:11 to 08:04:22Z, 08:04:43 to
08:07:02Z, 22:08:46 to 22:12:29Z, 23:20:44 to 23:27:14Z and 23:54:45 to 23:57:39Z on 29 October, and 02:40:05 to
02:45:51Z on 30 October), each from a launch guard that missed one kind of process or a race between two chains (the
last: a loop of short computations whose gaps let a second launch pass); each cause was corrected after its
interval, and jobs are enqueued under one lock from 00:10Z on 30 October. In the fifth and sixth intervals the limit
was restored by pausing the computation that started last; one pause stopped a pilot for 3 min 51 s while its wall
allowance kept running. In the seventh the last-started computation, a diagnostic scan, was stopped.
The independent checks paused and resumed their own long evaluations for short audits, and the recorded wall times
of those evaluations include the pauses.

Host contention. From about 06:00 on 30 October, processes outside the team (proof-assistant builds of another user)
ran at normal priority on the four host cores of the optimization side. The load average was 220 to 314. The team's
low-priority workers received about 30 per cent of a core each, and the Jacobian of an iteration took 3 to 18 times
longer than before. Caps were wall-time caps and were not extended, so the segments of this period made fewer
iterations, and the independent checks of the same period ran longer. The final test ran in this period (section
8): on one CPU core with one thread, the work from the construction of the first field grid through the assembly of
the first pressure source took 36 min at the P1 FREE state and 27 min at the F2 FREE state (of which the pressure
stage took 23 min each), against 23.6 and 25.0 min for complete two-level evaluations of P1 states by the same
evaluator on 29 October, and no primary evaluation completed within its 40-min cap. The outside processes were still running when the last
job ended, at a lower load average (54 at 15:21).
