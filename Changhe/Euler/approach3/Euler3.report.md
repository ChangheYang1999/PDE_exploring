# Rotating backward self-similar Euler profiles, 2/5 < c_l < 1/2, omega != 0: a 96-hour numerical investigation

## Summary

Status: C, search unsuccessful in a precisely documented class (not a nonexistence result). Endpoints A and B were not
reached and no rigorous obstruction (D) was found. The independent verifier validated label C on the final audited text
(23 checks confirmed, none refuted, 3 left open as substantive limits: exact resource consumption and process
termination, candidate validation beyond the documented checks, and a review of the primary route's final daily report).

Proved results (section 2; each entered only after independent confirmation; they concern exact profiles):
- Finite energy is excluded: a smooth bounded L^2 profile with the full-space pressure is zero for c_l > 2/5 (item 3).
- Axisymmetric C^2 profiles with U = o(|y|) are constant, for 0 < c_l < 1/2 and any omega (item 7); axisymmetric
  profiles are non-rotating, so rotating profiles must be non-axisymmetric (item 2).
- Decay dichotomy: for 2/5 < c_l < 1/2, a C^2 profile with the full-space pressure and |U| <= C(1 + r)^(-alpha) is zero
  or has ball energy growing exactly like R^(3 - 2 alpha) (item 6).
- The formal far-field structure and the first far-field energy and helicity laws hold under the stated tail
  assumptions (items 4, 18, 30, 34); for exact C^2 profiles with U = o(|y|) uniformly, no closed vortex line carries
  nonzero vorticity, and vorticity zeros are degenerate (item 35).
None of these excludes the rotating class; the non-rotating Liouville argument does not transfer (item 5).

Best numerical evidence (approximations on finite bases; no exact profile established; a/b = holdout rho_u^max on the standard
/ offset shell family; the discovery tier, Tier S, needs at most 1e-2 on both):
- c_l = 0.45, omega = 1, omega/c_l = 20/9: lowest independently checked holdout 0.04082/0.04142 (4.1 times the bound,
  a channel test state); the selected Stage III state, a degree-10 rung, reads 0.04195/0.04145 (primary values,
  reproduced from saved data by the verifier's reader). A degree-8 far-closure rung reads 0.02983/0.03130
  (primary-reported, not evaluated independently, ranked ahead of none of its five comparison states).
- c_l = 0.45, omega = 0.3, omega/c_l = 2/3: 0.05973/0.05939; c_l = 0.42, omega = 0.3, omega/c_l = 5/7: 0.06154/0.06718
  (degree 8, independently checked). Single-term ratios (shell maxima) are 3.7 to 5.0 times their bound at degree 8.
- Refinement stalls: holdout factors per degree step lie between 0.867 and 0.969 (primary-reported; weak above 0.85),
  so each refined branch is floored at degree 8 or 10 at the tested optimizer and budget (an operational reading).
- Each state on which they were evaluated misses at order one the whole-space energy and helicity balances or the
  far-field coefficient conditions that every exact profile in the assumed class satisfies; the selected field has a
  nonzero axial vorticity residual at the origin in exact arithmetic, so it is not an exact profile.

Remaining gap. For A and B the first missing implication is Tier S at the finest level (holdout rho_u^max <= 1e-2 on
both shell families with the single-term, core-resolution and Poisson requirements); the best independently checked
state is about 4 times above it, and the last degree steps lowered the holdout by only about 4 to 5 per cent
(factors 0.946 to 0.961). B then
needs a total reduction by 10 under three refinements, independent re-evaluation within a factor 3 and stable guards;
independent pressure accuracy for the selected state and three meaningful aligned refinements were not established.
For D no complete obstruction was established: the rotating Bernoulli function is not monotone along W, by the
sign-indefinite rotation term (item 8), and a compact zero-free alpha-limit set of vortical points is not excluded (item 17).

Run record. Logged campaign start T0 = 2026-10-24T17:09:12Z. Work covered Stages I (to hour 30), II (to hour 72) and III
(verification, to hour 96), with the candidate-validation requirements still unmet. The planned 96-hour period elapsed,
with measured campaign time 96.00 h to the job supervisor's exit at 2026-10-28T17:09:25Z. Publication completion:
T_end = 2026-10-28T17:40:21Z, 96.52 h after T0 (4 d 0 h 31 min). The publication edits made then (this summary, the run
record, removal of internal references) changed no result; the independent verifier did not re-audit those edits. This
is the first report on this prompt; the companion non-rotating study covers omega = 0 only.

## Detailed summary

Outcome label: C. No numerical state meets the discovery tier (Tier S), and no complete obstruction covering the
searched target class has been supplied. Labels A and B both require Tier S at the finest level, in particular
holdout rho_u^max <= 1e-2 on both shell families (section 3); no state meets it. Label D requires a complete,
independently confirmed obstruction proof covering the stated class; none has been supplied, and an optimizer failure
is never an obstruction. Hence C; the label was set at the Stage III freeze from independently checked results only.
Every state below is a numerical approximation on a finite basis, never an exact profile (for the selected state this
is shown in exact arithmetic: its axial vorticity residual at the origin is nonzero, 6.9 (s)); a/b denotes the
holdout rho_u^max on the standard / offset shell family, and St1 to St12 are the state IDs of Table A (section 5).

Closest states.
(a) c_l = 0.45, omega = 1, omega/c_l = 20/9. The lowest independently checked holdout values, 0.04082/0.04142 (4.1 times
    the bound on both families), belong to a test state (St1) with 8 instead of 4 radial functions in the far-correction
    channels of the continued degree-8 rung of the balanced-core ladder. St1 is not ranked ahead of that continued rung
    (St2, 0.0437/0.0433, 4.4 and 4.3 times the bound; independent reconstruction and reassembly, agreeing at the
    displayed precision): under the registered ordering rule its centre-weighted a_max on the two core balls at the
    vorticity maximum is 38 and 48 per cent larger (primary-reported; not evaluated independently). The degree-10 rung
    started from St2 has 0.04195/0.04145 (4.2 and 4.1 times the bound; primary values, reproduced from the saved data by
    the verifier's reader, not a fresh evaluation) and, by the ordering rule applied to saved values, is ranked ahead of
    St2, conditionally on core resolution (section 5.4). On the standard common quadrature over |y| < 32768, computed
    independently from the saved coefficients, sigma_Om is 0.4213 for the degree-10 rung and 0.4211 for St2; the ratio is
    1.0006 on both this family and the half-offset family, whose outer radius is 23170.475, so that leg of the ordering
    rule holds; both values are 4.2 times the Tier S bound. A degree-8 rung started
    from the far-closure state of 5.6 (c) at these parameters has 0.02983/0.03130 (2.98 and 3.13 times the bound;
    primary-reported, not evaluated independently), the lowest primary-reported shell holdout among the five states it
    was compared with (its training momentum RMS is only 7.4 per cent below its start's), but its core-set a_max is 2.02
    times that of the degree-10 rung, so by the ordering rule it is not ranked ahead of any of them (section 8, item 2).
    Over all saved readings of states at these parameters it is ranked ahead of St1 continued for 150 iterations
    (0.03995/0.04040, primary-reported, iteration limit; itself ranked ahead of no degree-8 or degree-10 state) and of
    seven degree-6 states, conditionally on core resolution (the verifier reapplied the inequalities to the saved values).
(b) c_l = 0.45, omega = 0.3, omega/c_l = 2/3. The degree-8 rung of the same ladder (St7a) has 0.06129/0.06085
    (independently checked), continued to 0.05973/0.05939 (St7b, independently checked); its degree-10 rung has
    0.05650/0.05645 (primary values, reproduced from the saved data by the verifier's reader, not a fresh evaluation).
    The degree-8 D6-lineage states have 0.0456/0.0554 (St11b; independent readout of primary samples, not a fresh
    evaluation) and 0.0442/0.0543 (St10, primary-reported); their cores are unbalanced. The independent route's own
    degree-6 state (St12) has 0.0574/0.0541 (fresh evaluation, independently checked). A degree-8 rung started from the
    far-closure state of 5.6 (c) at these parameters has 0.03739/0.03940 (3.74 and 3.94 times the bound;
    primary-reported, not evaluated independently), lower than each of the four states it was compared with (its own
    degree-6 start, St7a, St7b and the degree-10 rung), but its core-set a_max is 1.21 to 1.39 times theirs, so by the
    ordering rule it is not ranked ahead of any of them (section 8, item 2); over all saved readings at these parameters
    it is ranked ahead of six degree-6 states. By the ordering rule applied to saved primary values, the degree-10 rung
    is ranked behind two degree-6 states: the weight-1 closure-row state from St8a (primary values 0.05227/0.05368;
    5.6 (c)) and a seven-iteration balance continuation of it (the same values to four digits; ratios to the
    degree-10 rung 0.925 and 0.951 on the two holdouts and 1.029, 1.090 and 1.062 on the core-set sigma_u^max, sigma_Om
    and core-set a_max). Both relations are conditional on core resolution and on the sigma_Om comparison across
    degrees, and the closure-row gain depended on the excursion of an unsafeguarded lagged iteration (section 8, item 2
    (iii)). The verifier reapplied these inequalities to the saved values.
(c) c_l = 0.42, omega = 0.3, omega/c_l = 5/7. The degree-8 rung (St9a) has 0.06217/0.06746, continued to
    0.06154/0.06718 (St9b) (both independently checked).
Single-term ratios RMS(R_u)/RMS((1 - c_l)U), bound 1e-1: the per-family shell maxima on the three degree-8 rungs are
0.375 to 0.499 (independently checked), and the core-ball values that the registered maximum also includes are larger
where computed (0.43 on St3 and 0.58 on St7a, primary-reported). On St12, sigma_u^max is 3.13 and sigma_Om over |y| <
1024 (a resolved-region value) is 2.46 (independently checked); on the three independent-route states measured, the
single-term ratios are 20 to 32 times their bound (independently checked).

Refinement. A resolution step whose factor q (holdout rho_u^max at the new degree over the previous one) exceeds 0.85 is
weak; two successive weak steps floor a branch at the tested optimizer and budget (an operational classification, not a
statement about the cause). Degree 6 to 8, standard/offset (primary-reported factors from independently read endpoints):
0.916/0.901 at c_l = 0.45, omega = 0.3, omega/c_l = 2/3; 0.954/0.940 at c_l = 0.45, omega = 1, omega/c_l = 20/9,
recomputed to 0.887 on the standard family because the channel test lowered that holdout by 6.5 per cent (more than the
registered 5 per cent); 0.969/0.943 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7, after a weak degree-4 to degree-6 step
(0.867/0.957), so that branch is floored at degree 8, as is the D6 lineage. Each c_l = 0.45 branch has one weak step, at
the iteration limit, and its degree-10 rung, read against the continued degree-8 state with the same 4 far-correction
channel functions, gives a second: 0.946/0.950 at omega = 0.3 (omega/c_l = 2/3) and 0.961/0.957 at omega = 1
(omega/c_l = 20/9) (primary values, reproduced from the saved data by the verifier's reader, not a fresh evaluation).
Both branches are therefore floored at degree 10 with 4 channel functions; the degree-10 states also stopped at the
iteration limit (V10 0.0084 and 0.0052, above the stationarity bound 1e-3, primary-reported), so these factors mix
truncation with budget.

Structural defects. Each state on which they were evaluated misses condition (a) or (b) at order one; every exact
profile in the assumed class (nonzero differentiated leading tail with the full-space pressure, section 2) satisfies
both. Condition (c) is only sampled.
(a) Whole-space balances E_ren = 0 and H_tot = 0. E_ren < 0 on all eleven momentum-only primary exports and H_tot < 0 on
    ten of them (theory route; the values listed in section 5.7 (a) independently checked). The one positive H_tot
    (+4.29, H_tot / int |h| = +0.89, independently checked, on a degree-6 start at c_l = 0.45, omega = 0.3, omega/c_l =
    2/3) shows that the sign belongs to the states. The balance arm (St6) reduced both balance defects far below the
    registered 0.05 bounds (independent values E_ren +1.31e-4, H_tot about -3.1e-5 and H_tot / int |h| -7.2e-6,
    finite-quadrature estimates with integration and rounding errors not enclosed; no exact balance is established) at
    residual ratios 1.232/1.235 to its start and fails both far-coefficient conditions at order one. An
    independent-route state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 ends at E_ren +1.40 and H_tot -5.70 with
    holdout 0.423/0.420 (independently checked).
(b) Far-field coefficient conditions (carried over required first far coefficient, exact value 1). On fifteen states
    checked independently the energy ratio lies between -2835 and +29.7 on the eleven that carry a rate-(2 alpha + 1)
    term and is 0 on the four that do not; it is -0.279 on St7a and -5.18 on St3. After the channel test it is +0.243
    on St1 (primary-reported; right sign, about four times too small). With far-closure rows at weight 1, at the end
    of the two-rung ladder that started from St4 (c_l = 0.45, omega = 1, omega/c_l = 20/9), the independent evaluation
    finds 0.99998 (helicity ratio 0.999998, vector mismatch 3.8e-6), while the finite-radius pressure guard fails and
    the core-ball a_max is 1.10 times that of St4. At c_l = 0.45, omega = 0.3, omega/c_l = 2/3 the weight-1 state from
    St8a meets the reading as well (energy ratio 1.000001, helicity ratio 0.999995, mismatch 2.1e-6) and passes all
    registered guards, with holdout rho_u^max 0.0523/0.0537, 5.2 and 5.4 times the Tier S bound, and core-ball a_max
    1.19 against the primary-reported 0.98 of St8a. Neither is a candidate (5.6 (c)).
(c) Swirl ratio. The sampled Q_sw is above 1 on the degree-4 balanced-core states (2.0009 at c_l = 0.45, omega = 1,
    omega/c_l = 20/9, independently checked) and below 1 on the degree-6 and degree-8 rungs (for example 0.6427 on St3
    and 0.3871 on St7a, independently checked); this neither establishes nor excludes Q_sw <= 1.

Rigorous results (section 2, each independently checked). Finite-energy profiles are trivial (item 3); axisymmetric
profiles with sublinear velocity are constant, hence zero under decay (item 7); C^2 profiles with the full-space
pressure and |U| <= C(1 + r)^(-alpha) are zero or have ball energy growing exactly like R^(3 - 2 alpha) (item 6); the
far-field structure and the first energy and helicity laws are derived (items 4, 18, 30 and 34); the non-rotating
Liouville argument does not transfer, since rotation adds a non-gradient term (item 5); vortex lines of an exact
profile cannot close and its vorticity zeros are degenerate (item 35). None excludes the class.

Campaign time. Measured start 2026-10-24T17:09:12Z. Measured end 2026-10-28T17:09:25Z, 96.00 h after the measured
start (the last job stop, section 0). The audited text was installed at 2026-10-28T17:27:01Z, 96.3 h after the measured
start and after the end of the 96-hour budget at 2026-10-28T17:09:12Z (system clock). Stage I ended at
2026-10-25T23:09:12Z (hour 30) without a candidate. The Stage II gate was posted at 2026-10-27T11:12:39Z (hour 66.06)
with a failure map (section 7); Stage II time is counted to 2026-10-27T17:09:12Z (hour 72), and Stage III
(verification) ran to 2026-10-28T17:09:12Z (hour 96).
The run ended at T_end = 2026-10-28T17:40:21Z, 96.52 h (4 d 0 h 31 min) after the measured start, when this report
was finalized for publication.

What would change the label. Label B needs a state that meets Tier S at the finest level, lowers rho_u^max by a total
factor of at least 10 under at least three refinements without stalling, is re-evaluated independently within a
factor 3 and has stable guards N1 to N6; label A needs in addition every Tier A requirement, with the independent
route's own refinement converging to the same field; label D needs a complete, independently confirmed obstruction
proof covering the searched class. The lowest independently checked values are a factor of about 4 above Tier S, and
the one measured doubling of the far-correction channels gained 4 to 7 per cent, which fixes no rate; the two
degree-10 rungs lowered the holdout by about 4 to 5 per cent (section 5.4). Degree-8 rungs from far-closure states at
c_l = 0.45 read 0.02983/0.03130 at omega = 1, omega/c_l = 20/9, and 0.03739/0.03940 at omega = 0.3, omega/c_l = 2/3
(primary-reported), about 3 and 4 times above Tier S, and neither is ranked ahead of the degree-10 rung of its branch
(section 8, item 2). The Stage III replication runs at c_l = 0.45, omega = 1, omega/c_l = 20/9 are read in 6.7 (three
perturbations of St2, and a perturbation pair on the degree-10 state as a late result) and in 6.8 (four single-change
runs from St2). The Stage III verification of the three states selected at the Stage II gate (section 7) is recorded
in 6.9; the next experiments are listed in section 8. The bounded degree-6 continuation of the fresh all-mode start
at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 ended at 0.09767/0.09507, behind the even-class degree-6 state at that
point (primary-reported coverage reading, 5.6 (j)).

## 0. Campaign record and coverage

Measured start T0 = 2026-10-24T17:09:12Z (UTC, from the system clock). Stage boundaries: Stage I (foundations and
broad discovery) to 2026-10-25T23:09:12Z, Stage II (refinement, continuation, matching, free parameters, odd
azimuthal wavenumbers) to 2026-10-27T17:09:12Z, Stage III (independent replication and adversarial validation, no new
discovery) to 2026-10-28T17:09:12Z. Measured end: 2026-10-28T17:09:25Z (hour 96.00), the logged exit of the primary
route's job supervisor; the independent route's resource monitor wrote its end-of-loop record at 17:09:18 UTC, and
its disk guard, which has no end record, had exited by 17:09:53.048 UTC; the audited text of this report was installed
at 2026-10-28T17:27:01Z, and the report was finalized for publication at T_end = 2026-10-28T17:40:21Z.
At the end of the budget only this campaign's jobs were checkpointed and stopped: no job of the
primary route was running or pending at 2026-10-28T17:09:12Z, so none needed a checkpoint: its last queue job ended
at 2026-10-28T01:08:17Z, and its job supervisor, which launches jobs, stopped itself at its own 96-hour budget check,
counted from the supervisor's logged start 2026-10-24T17:09:14Z, and logged its exit at 2026-10-28T17:09:25Z; a
heartbeat helper that only refreshes the heartbeat files of running jobs and launches nothing was left running
(primary-reported). The independent route's last scheduled resource commands, a resource snapshot and its independent
reader, ended at 16:30:34 UTC, and its stop attempt at 16:42 UTC was skipped at its admission check, so it signaled
nothing; its resource monitor and disk guard, configured to end at 17:09:12Z, were observed at 17:08:51 UTC and were
absent at 17:09:53.048 UTC, and the monitor wrote its end-of-loop record at 17:09:18 UTC.
Of the independent route's Stage III verification runs and controls (6.9), two failed for infrastructure reasons,
with no result: the first R3 source attempt at 2026-10-27T16:36:20Z, by a disk-accounting race in its watcher (8400
core-seconds and 8400 GPU-seconds stay charged), and the first Group B control at 2026-10-27T17:25:08Z, by an
import-audit rejection (960 recovery core-seconds stay charged), after which the other two Group B controls were not
attempted (6.9 (d), (i)). The independent Newton agreement was not run, by a decision of the campaign lead at
2026-10-27T17:28:28Z, and its metadata control was withdrawn before installation, so neither was charged (6.9 (j)).
Every ledger-derived count of primary-route starts made after the resume test of 6.9 (l) states whether it includes
that test's two disposable starts, which add two to the ledger's count of start results (990 at hour 72).

Hardware: one node with eight NVIDIA A100-SXM4-80GB GPUs, four used by the primary numerical route and two by the
independent route; the other two belonged to other projects. CPU work (specification, derivations, theory-route
diagnostics, report) ran at low priority. During Stage III an operator limit on the shared machine reduced the CPU
allocation: from 2026-10-28 at about 01:50 UTC (the time the operator stated; the configuration files changed at
about 01:46 UTC) the primary numerical route had two CPU cores with at most two single-threaded worker processes, and
the independent route and the report work shared one core. The comparison reader of the degree-10 control and
perturbed continuation pair at c_l = 0.45, omega = 1, omega/c_l = 20/9, started at 01:44:22 UTC before the limit,
kept the thread settings it was launched with (three threads each for the OpenMP and MKL libraries). It wrote no
output and was stopped at 06:07:30 UTC by order of the campaign lead (6.7). GPU allocations did not change. Processes
of other projects shared some GPUs; a coincident out-of-memory failure was recorded as an environment failure, not as
a result.

Artifacts. The primary route's artifact package was written once, at 2026-10-28T03:45:04Z, and is frozen: 701 files
totalling 19,313,119 bytes, holding its code, configurations, run ledger, status summaries, reports, candidate
coefficients and documentation, the test records of section 8 (items 13 to 15), the reader records of the Stage III
readings of 6.7 and 6.8 and the operator's CPU limit. A sha256 manifest covers its other 700 files, and a copy check
compares the 104 copied files with their sources; the campaign lead and, independently, the verifier recomputed every
hash in both and found all equal. The package holds no reading of the degree-10 control and perturbed continuation
pair at c_l = 0.45, omega = 1, omega/c_l = 20/9. The published folder of accompanying artifacts is that package with
these changes, all documented in the accompanying artifacts: absolute local paths replaced by relative ones (so
changed files no longer match the frozen manifest, which is kept, and a new manifest covers the published bytes); the closing records of hour
96 added (final ledger and status summary, Stage III coverage snapshot, final daily report and tables); work logs,
hand-over notes, superseded drafts and backups removed; the registered acceptance specification, the derivation and far-field
audit documents and copies of the independent verifier's final records added. The saved start file of the degree-10
rung is published as a copy whose two parent-path fields were made relative and whose other contents are equal to the
original, so its hash differs from the one cited in 6.9 (m).

Resource usage. Stage I, primary route: 120.0 allocated GPU-hours (four GPUs for 30.0 h; independently checked); its
ledger gives 114.9 busy GPU wall-hours and 145.4 process-hours (activity proxies, not summed; primary-reported), and the
recorded starts account for 99.9 process-hours. Independent route, Stage I boundary account from its own sampled
monitor (independently recomputed from the frozen monitor record): allocation 60 GPU-hours over its two GPUs and 90
CPU-core-hours over three cores (elapsed allocations, not consumed compute); sampled device activity proxies of 16.07 h
and 8.26 h on the two GPUs, which include any activity of other processes; observed process CPU counters of 60.56 CPU-
hours (counter increments within the stage 56.54 CPU-hours); an identified CPU-only subset of 2.95 CPU-hours over 71
processes. The first 1829 s and the final 14 s of the stage were not sampled. These are different measures and are not
added; the route's consumed GPU use is open.
Independent route, cumulative snapshot from T0 to hour 72 (Stages I and II) from its own sampled monitor (16824
samples; the first 1829.0139997005463 s unobserved and one 75.08547329902649 s gap excluded): reserved capacity of
144 GPU-hours and 216 CPU-core-hours (an allocation, not usage), device activity proxies of 18.97254220955471 h on
GPU 6 and 10.429719867259264 h on GPU 7 and power integrals of 6.2199223333958775 kWh and 5.817000361342315 kWh,
which may include idle draw and the activity of other processes, and incomplete observed CPU sums of
86.37815833333333 h (summed maximum counters) and 81.43791944444445 h (within-sample increases) over 2074 keys; none
of these figures is added to another, and historical attribution and CPU completeness are open. The independent
route's production balance, exact, was 35995.669011125807078 core-seconds and 26442.377990569919 GPU-seconds after
the charge of the second R3 source attempt and the return of its unused reservation; 35970.889880651608468
core-seconds after the charge of the R3 pressure run (24.77913047419861 core-seconds, 0 GPU-seconds) and the return
of its unused reservation, accepted at 2026-10-27T19:43:46Z; and 16170.889880651608468 core-seconds and
6642.377990569919 GPU-seconds after the reservation of the cap of the R4 source (19800 core-seconds and 19800
GPU-seconds) before its launch at 2026-10-27T20:04:37Z. After the charge of the R4 source (11767.576421019156
core-seconds and the same in GPU-seconds, for its whole watch) and the return of the unused 8032.423578980844 of each
reservation, accepted at 2026-10-27T23:25:32Z, the balance was 24203.313459632452468 core-seconds and
14674.801569550763 GPU-seconds. The cap of the R4 pressure run (1800 core-seconds) was allocated at
2026-10-27T23:45:06Z, leaving 22403.313459632452468 core-seconds. The run was charged 17.865782154724002
core-seconds, for its whole watch, and no GPU-seconds; the unused 1782.134217845275998 core-seconds were returned on
its acceptance at 2026-10-27T23:55:38Z, leaving 24185.447677477728466 core-seconds and 14674.801569550763
GPU-seconds. The moments reducer was allocated its watch cap of 300 core-seconds and no GPU-seconds at its launch at
2026-10-28T00:28:44Z, leaving 23885.447677477728466 core-seconds and 14674.801569550763 GPU-seconds; the full 300
core-seconds stay charged, with no return, and its measured use of 15.998475897591561 core-seconds is a separate
record (accepted at 2026-10-28T00:41:00Z). The last consumer, the comparisons reducer, was allocated its watch cap of
300 core-seconds and no GPU-seconds at its launch at 2026-10-28T01:10:51Z, leaving 23585.447677477728466 core-seconds
and 14674.801569550763 GPU-seconds; the full 300 core-seconds stay charged, with no return, and its measured use of
7.405944517813623 core-seconds is a separate record (accepted at 2026-10-28T01:25:37Z). The independent route's
recovery reserve went from 156090 core-seconds through debits of 30, 30 and 30 (the readers of leg R2), 600 (the
hour-72 snapshot), 1060 (the recovery and replay of the degree-10 state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3
in section 8, item 1), 960 (the failed Group B control), 300 (the disk-wrapper control) and 30 and 30 (the two
readers of the second R3 attempt) to 153020 core-seconds at 2026-10-27T19:18:00Z, through a debit of 30 (the reader
of the R3 pressure result) to 152990 core-seconds at 2026-10-27T19:49:44Z, through a debit of 90 (the exact reader of
the leading tail of the selected state, 6.9 (o)) to 152900 core-seconds at 2026-10-27T20:41:04Z, and through a debit
of 90 (the exact gauge reader of the leading tail of the selected state, 6.9 (o)) to 152810 core-seconds at
2026-10-27T21:04:00Z, through two debits of 30 (the two readers of the R4 source) to 152750 core-seconds at
2026-10-27T23:32:07Z, through a debit of 30 (the reader of the R4 pressure, 6.9 (h)) to 152720 core-seconds at
2026-10-27T23:58:03Z, through a debit of 90 (the exact table reader, 6.9 (p)) to 152630 core-seconds at
2026-10-27T23:59:37Z, and through a debit of 32 (the exact origin reader, 6.9 (s)) to 152598 core-seconds at
2026-10-28T04:11:26Z, through a debit of 302 (the closing resource snapshot) to 152296 core-seconds at
2026-10-28T16:30:14Z, and through a debit of 302 (its independent reader) to 151994 core-seconds at
2026-10-28T16:30:31Z. The idle hours of primary-route GPU 5 are reduced by the resume test from 2026-10-27T17:48:57Z
to 17:56:58Z (481 s of wall time), and the run ledger records no launch on GPU 5 from then to the campaign end
(primary-reported; the resume test ran outside the queue and has no ledger launch row). Stage II, primary route, as
differences of the cumulative coverage snapshots of its run ledger at hours 30 and 72: 168.0 allocated GPU-hours
(four GPUs for 42.0 h), 137.51 busy GPU wall-hours and 140.42 process-hours (activity proxies, clipped at the stage
boundaries, not summed; primary-reported). Stage III, primary route, as differences of the snapshots at hours 72 and
96: 96.0 allocated GPU-hours (four GPUs for 24.0 h), 15.61 busy GPU wall-hours and 15.61 process-hours, the two
activity proxies coming from the two degree-10 jobs that were running at hour 72 and completed at 00:47:03 and
01:08:17 UTC on 2026-10-28; no job was launched from the queue in Stage III (primary-reported). The primary route's
queue ran no CPU-only job in Stages II and III (every launch row of its ledger names a GPU; primary-reported); its
CPU-only work outside the queue (readers, records and report chains) has no recorded hour total. Sampled maxima, such
as the peak number of jobs sharing a GPU, are not differenced. For the independent route in Stage II, the differences
of the hour-72 and hour-30 cumulative sampled summaries (one producer, nested log prefixes) are 2.91 h and 2.17 h of
device activity proxy on GPUs 6 and 7 and 24.90 CPU-hours in the all-process counter-increase totals; its reserved
capacity in Stage II was 84 GPU-hours and 126 CPU-core-hours. These differences are not Stage II consumption: the
device proxies can include foreign activity and at most 14.2 s per GPU of interpolated activity before hour 30, and
they omit one rejected 75.1-second sample gap inside Stage II and the last 10.5 s before hour 72; the counter
difference is neither the CPU time in the stage nor a bound on it. Capacity, proxies and counters are not added. For
the independent route in Stage III, the differences of the closing and hour-72 cumulative sampled summaries (matching
GPU integration and CPU counter definitions, nested log prefixes; the closing summary is cumulative to 16:30:00Z on
2026-10-28, and an independent reader rechecked its arithmetic and evidence consistency with 7918 checks passed and
none failed) are 1.20523 h and 0.01318 h of device activity proxy on GPUs 6 and 7 and 4.60737 CPU-hours in the
all-process counter-increase totals. These differences are not the route's consumption in the stage: the device
proxies can include foreign activity and at most 10.5 s per GPU of interpolated activity before hour 72, the last
6.06 s before 16:30:00Z and the 39 min 12 s from 16:30:00Z to 17:09:12Z are unmeasured, and the counter difference is
neither the CPU time in the stage nor a bound on it. The CPU allocation after the CPU limit of 2026-10-28 01:50 UTC
is not established. The disk guard measured working-directory size but could not stop CPU 61 workers; launch-time checks and a
302-second timeout bounded each run. Peak memory by scientific job class was not independently established. The
primary route's job supervisor samples the resident set size of each job's worker process tree every 20 s; the
largest sampled host maximum over all its completed jobs from the campaign start to hour 96 is 16.1 GiB, and the two
Stage III queue jobs reached 11.44 GiB and 11.42 GiB (primary-reported sampled maxima, not class peaks; the field
max_rss_GB divides bytes by 2^30; GPU memory is not summarized by job class). Disk use at the end, observed once
after the budget end and after the primary route's closing summary run, at 2026-10-28T17:15:18Z to 17:15:19Z: the
primary route's working directory held 1615112313 apparent bytes (du -sb), the lead's working directory 2342778888
apparent bytes (du -sb), and the independent route's working directory 23808287489 bytes as the sum of st_size over
its 110283 regular file paths (hard links counted per path, symbolic links not followed, directories excluded; no
walk error). These are observations at those times, not peaks and not allocated space, and they are not added.

Table C. Coverage by stage: the census at the Stage I boundary by route, the Stage II activity to 2026-10-26T01:19Z,
and the whole of Stage II and Stage III. "missing": not recorded in the sources. The census is independently checked
as a finite accounting; the rest is primary-reported unless marked.

| Item | Primary route | Independent route |
|---|---|---|
| Experiments, Stage I | 212 experiments, 892 starts | 540 to 2026-10-25T05:35Z; at the boundary 545 result records (13 failures retained; not distinct starts; census independently checked) |
| Stop reasons | tolerance 346, iteration limit 490, stalled 47, time limit 9 | missing |
| Main-block angular degree | 2 (187 starts), 4 (43), 6 (642), 8 (16), 10 (4) | 2 to 6 (8 and 10 in machinery tests only) |
| Radial functions | 4 to 32 per domain; far-correction channels 4 (8 in one test) | own representation (4.3) |
| Azimuthal wavenumbers | even: 888 starts; all: 4 | even, and all in separate runs |
| Formulation | vorticity 357, momentum 534, combined 1 | momentum residual |
| Parameters | fixed 883, free 9 | fixed |
| Seeds | note (1) | random 282, affine core 158 (to 05:35Z) |
| Parameter points | 49 (Table C1) | 27 parameter pairs (result-record census) |
| Optimizers | Levenberg-Marquardt, L-BFGS, Newton tests | Levenberg-Marquardt, Gauss-Newton, L-BFGS |
| Budgets | note (2) | note (2) |
| Ranked states | 573 (320 from the latest solver) in 214 bins (bin count primary-reported, not independently reconstructed); note (3) | missing |
| Lowest holdout a/b | 0.04082/0.04142 (St1, independently read) | 0.0574/0.0541 (St12) |
| Resources, Stage I | 120.0 allocated GPU-h; busy 114.9; process 145.4 | 60 allocated GPU-h, 90 CPU-core-h; activity proxies 16.07 and 8.26 h (including any foreign activity); consumed use open |
| Stage II to 2026-10-26T01:19Z | note (4) | note (4) |
| Stage II, 2026-10-25T23:09:12Z to 2026-10-27T17:09:12Z | 67 experiments, 98 starts (tolerance 12, iteration limit 77, stalled 2, time limit 7); 168.0 allocated GPU-h; busy 137.51; process 140.42; differences of the cumulative snapshots at hours 30 and 72 | 84 allocated GPU-h, 126 CPU-core-h; differences of the hour-72 and hour-30 cumulative sampled summaries: activity proxies 2.91 h (GPU 6) and 2.17 h (GPU 7), including any foreign activity, with one 75.1-second gap unmeasured; difference of all-process counter-increase totals 24.90 CPU-h (not CPU time in the stage, no bound); consumed use open |
| Stage III, from 2026-10-27T17:09:12Z | 0 experiments, 4 starts (iteration limit 4; 2 of them the resume test's disposable starts, 2 from the two jobs running at hour 72); 96.0 allocated GPU-h; busy 15.61; process 15.61; differences of the cumulative snapshots at hours 72 and 96 | CPU allocation not established; differences of cumulative sampled summaries: activity proxies 1.20523 h (GPU 6) and 0.01318 h (GPU 7), including any foreign activity, and 4.60737 CPU-h in all-process counter-increase totals (not CPU time in the stage, no bound), to 16:30:00Z; the 39 min 12 s to 17:09:12Z unmeasured; consumed use open |

Notes. (1) Primary seeds (starts): random 243, non-axisymmetric core 134, tail-only 127, poloidal 124, toroidal 114,
saved states 100, exact affine core 50. (2) Primary: degree-8 rungs ran to the 300-iteration limit (not stationary by
the registered test), continuations up to 150 more; the radial ladder 300 iterations at 24 radial functions and the 7200
s limit at 32. Independent route: four times its degree-4 and degree-6 budgets, 400 Gauss-Newton steps and 2500 L-BFGS
iterations. (3) Excluded before ranking: 40 disposable runs, 8 free-parameter runs and 271 trivial endpoints. The 214
descriptor bins are not shown to be distinct branches; no ranked state meets Tier S. (4) Primary: the degree-10 rungs at
c_l = 0.45, omega = 1, omega/c_l = 20/9 and c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (started in Stage I, running about
8 h at that time; both read later in Stage II, section 5.4); an arm with the combined vorticity and momentum formulation
(three of four runs read by 2026-10-26T01:16Z, primary-reported: none is a candidate or ordered ahead of its start,
their holdout rho_u^max rose to 0.20 to 0.98 and one collapsed toward the trivial state; the fourth was running then;
the complete arm is in section 8, item 4); a degree-6 continuation with closure-row weight 0.1 from the first degree-6
rung at c_l = 0.45, omega = 1, omega/c_l = 20/9 (running then; read later as the first rung of the two-rung far-closure
ladder from St4, section 5.6 (c)); 897 starts completed. Independent route: a 12-step degree-10 optimization (completed
2026-10-25T23:55Z) and a degree-8 radial test with replay, both machinery evidence only; all-mode fresh baseline and
terminal batteries registered before any result (the eight-step run and its battery completed in Stage II, 5.6 (j); the
broader independent all-mode arm was not released). No Stage II reading has produced a candidate.

Table C1. Parameter points of the primary route at the Stage I boundary (49 points), as omega (omega/c_l) per c_l.

| c_l | omega (omega/c_l) |
|---|---|
| 0.41 | -3 (-300/41), -0.3 (-30/41), 0.1 (10/41), 0.3 (30/41), 1 (100/41), 3 (300/41), 10 (1000/41) |
| 0.42 | 0.3 (5/7; 65 starts) |
| 0.43 | -3 (-300/43), -0.3 (-30/43), 0.1 (10/43), 0.3 (30/43), 1 (100/43), 3 (300/43), 10 (1000/43) |
| 0.45 | -3 (-20/3), -0.3 (-2/3), 0.1 (2/9), 0.3 (2/3; 131 starts), 1 (20/9; 154 starts), 3 (20/3), 10 (200/9) |
| 0.45, single starts | 0.2065 (0.4589), 0.3014 (0.6698), 0.3232 (0.7182), 0.533 (1.1844), 0.9205 (2.0456) |
| 0.46 | 0.3 (15/23) |
| 0.47 | -3 (-300/47), -0.3 (-30/47), 0.1 (10/47), 0.3 (30/47), 1 (100/47), 3 (300/47), 10 (1000/47) |
| 0.475 | 0.3 (12/19) |
| 0.48 | 0.3 (5/8) |
| 0.49 | -3 (-300/49), -0.3 (-30/49), 0.1 (10/49), 0.3 (30/49), 1 (100/49), 3 (300/49), 10 (1000/49) |
| 0.4498, 0.4509, 0.4518 | 0.9015 (2.0042), 1.0001 (2.218), 0.368 (0.8145), one start each |
| 0.4707, 0.499 | 0.9965 (2.1171), 0.2702 (0.5415), one start each |

Of the starts at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 and c_l = 0.45, omega = 1, omega/c_l = 20/9, 115 and 96 are
ranked. The single-start points are mostly the final parameters of runs with free parameters (sections 5.2 (e) and 5.6
(e)). Negative omega was run only as a reflection check (section 1.6). Not searched: 2/5 < c_l < 0.41 and 0.49 < c_l <
1/2 (apart from the free-parameter endpoint c_l = 0.4990, omega = 0.2702, omega/c_l = 0.5415), and the positive ranges
0 < omega < 0.1 and omega > 10.

## 1. Problem, conventions and search class

1.1 Equation. We seek smooth, decaying, non-trivial profiles U(y), P(y) on R^3 with div U = 0 and

    R_u := (1 - c_l) U + (W . grad) U + omega J U + grad P = 0,    W = (c_l I - omega J) y + U,    J y = (-y_2, y_1, 0),

for 2/5 < c_l < 1/2 and omega != 0, with P the decaying full-space solution of -Delta P = tr((DU)^2) (no harmonic
pressure is added or fitted; no condition at a finite radius). With E(s) = exp(omega s J), tau = T - t and s = -log tau,
the field u(x, t) = tau^(c_l - 1) E(s) U(E(s)^T x tau^(-c_l)) is an Euler solution exactly when R_u = 0; it blows up at
time T while rotating about e_3 at rate omega in the logarithmic time s. The vorticity form R_Omega = Omega + (W . grad)
Omega + omega J Omega - (Omega . grad) U, Omega = curl U, satisfies curl R_u = R_Omega when div U = 0.

1.2 Context. Constantin, Ignatova and Vicol (arXiv:2602.17570; CIV below) prove that a smooth finite-energy Euler
blowup with a self-similar vorticity-gradient bound needs c_l >= 2/5 (a physical-time statement with no similarity
ansatz, so it does not restrict omega), and that a non-rotating (omega = 0) profile whose transport field c_l y + U
satisfies a local outgoing condition at its finitely many zeros needs c_l >= 1/2 (under their decay and normalization
hypotheses). The target range lies between these bounds. A companion non-rotating study states a Liouville theorem for
0 < c_l < 1/2 with a proof its authors call informal; no unconditional result, label or search decision uses it as
verified input, and the one consequence that uses it (item 16 (c)) is stated as conditional on it. Rotation adds the
non-gradient term (1 - 2c_l) omega J y to the Bernoulli form of R_u, so its Bernoulli-Lyapunov argument does not
transfer. The rotating case is open.

1.3 Notation. alpha = (1 - c_l)/c_l, so 1 < alpha < 3/2 and 1/c_l = alpha + 1. chi = phi + (omega/c_l) log r is the
twisted azimuth (phi the true azimuth). Every state is labelled by c_l, omega and omega/c_l.

1.4 Far-field search class (a search assumption, not a theorem). The leading tail is U_0 = r^(-alpha) F(theta, chi),
carried by two smooth scalars on the sphere (the leading parts of curl(T y) + curl curl(S y) with T = r^(-alpha) tau and
S = r^(1 - alpha) sigma). The linear part of R_u annihilates every such U_0, so F is free formal data, fixed only by
matching with the core. The first nonlinear correction U_1 = r^(-(2 alpha + 1)) G[F] and the pressure term r^(-2 alpha)
Q[F] are determined by F; later terms include pure-tail products at rates n/c_l - 1 and harmonic pressure multipoles of
degree l >= 2 at velocity rate l + 2, whose coefficients are global moments of the full-space source. This formal
classification does not establish a complete expansion with a controlled remainder. Every nonzero decaying profile in
the target range has infinite energy (section 2, item 3).

1.5 Normalization and gauges. Exactly one dilation gauge, integral_{S^2} |F|^2 dS = 1 (an optimizer may use a core-scale
gauge instead, provided integral |F|^2 is monitored and every reported number is converted to this gauge); exactly one
azimuthal phase gauge, fixing the argument of one nonzero coefficient with m != 0 and requiring its real part to be
positive after every accepted step; the pressure constant through P -> 0 at infinity. No vorticity, DU(0) or core-radius
normalization is imposed in addition.

1.6 Symmetry restrictions. Rotations about e_3 and dilations map profiles to profiles with the same c_l and omega (the
two null directions fixed by the gauges). The reflection diag(1, -1, 1) maps omega to -omega, so only omega > 0 is
searched, with reflection checks at omega = -3 and -0.3 (Table C1); diag(1, 1, -1) is not imposed. The two-fold
equivariance exp(pi J) (even azimuthal wavenumbers, m = 0 included) is imposed in most runs, odd ones being admitted in
separate runs (Table C). Axisymmetric states are excluded by requirement, since for an axisymmetric U the rotation drops
out of R_u and the problem is the non-rotating one; non-axisymmetry is measured by the derivative-weighted indices
N_core, N_F and the m != 0 energy fractions e_core, e_F of the core shells and the tail (thresholds in section 3).

1.7 What counts as a profile here. A numerical state is a candidate only if it meets the acceptance tiers of section 3
on fresh holdout points of two dyadic shell families, with the full-space pressure, and is reproduced by the independent
route from the exported coefficients. A numerical candidate is an approximation, never an exact profile. Training losses
and optimizer costs are never used as acceptance evidence or as a ranking key.

## 2. Checked mathematical results

Entries were added only after the independent route confirmed them. They concern exact profiles or exact continuum
constructions; none is a statement about a computed state unless so marked.

1. Identities. R_u = grad Be - W x Omega + (1-2c_l)(c_l y+U) with an explicit Bernoulli function Be. At a nonzero global
   maximum of |Omega| of an exact smooth decaying profile, Omega.sym(DU)Omega = |Omega|^2 (CIV, Proposition 3.3, for
   omega = 0). Checked symbolically and with manufactured fields.
2. Symmetries. Rotation about e_3 and the dilation U_L(y) = LU(y/L), P_L = L^2P(y/L) preserve (c_l, omega); y_2 -> -y_2
   reverses omega, so omega > 0 suffices. Axisymmetric profiles are non-rotating, so rotating profiles must be
   non-axisymmetric.
3. Finite energy is excluded. A smooth, bounded L^2 profile with the full-space pressure is zero for c_l > 2/5, so every
   nonzero profile in the target range has infinite energy; for the natural tail, integral_{B_R}|U|^2 =
   (c_l/(5c_l-2))R^((5c_l-2)/c_l) integral_{S^2}|F|^2dS (1+o(1)).
4. Far field (formal, for a smooth tail differentiable term by term). The linear part of R_u multiplies twisted fields
   r^(-k)G(theta,chi) by c_l(alpha-k), so U_0 = r^(-alpha)F(theta,chi) is in its kernel for any F obeying one divergence
   constraint. G[F] and Q[F] (section 1.4) are locally determined by F. Logarithmic pressure terms can arise only for
   rational c_l (exhibited for c_l = 3/7 at the orders analyzed, reproduced exactly by the independent check). A nonzero
   exact leading tail cannot have identically vanishing leading vorticity H (pointwise zeros remain possible).
5. Literature. The companion study's Liouville theorem (section 1.2) does not apply when omega != 0. D. Chae and T.-P.
   Tsai (arXiv:1304.7414) do not cover the tail class (their integrability or L^2 hypotheses fail). L. Xue's
   Theorem 1.1(1) (arXiv:1408.6619) applies under its C^3 and full-space-pressure hypotheses, but its alternative
   "zero velocity or ball energy growing like R^(3-2alpha)" is met by the natural tail: a compatibility condition, not
   an exclusion (hypothesis map checked independently; re-check against any candidate). D. Chae (J. Differential
   Equations 377, 2023) could not be read (not assessed).
6. Decay dichotomy. For 2/5 < c_l < 1/2, a C^2 profile with the full-space pressure and |U| <= C(1+r)^(-alpha) has
   integral_{B_R}|U|^2 = LR^(3-2alpha) + O(R^(2-3alpha)) with L > 0 unless U = 0; so U = o(r^(-alpha)) uniformly forces
   U = 0, with no assumption on derivatives or pointwise pressure decay. L is a normalized energy, not a pointwise
   angular profile (the existence of F is assumed); it concerns exact profiles only, not approximate states.
7. Axisymmetric profiles. For 0 < c_l < 1/2 and any omega, an axisymmetric C^2 profile with U = o(|y|) is constant (zero
   under decay), without using the companion study's theorem. Since the omega terms vanish for axisymmetric U (item 2),
   this is the non-rotating statement; the argument is that of CIV, Theorem 4.5 and Remark 4.6, with their decay
   hypothesis (3.8) replaced by U = o(|y|).
8. Dynamics. Backward W-trajectories are trapped; a vortical periodic W-orbit is a saddle with Floquet multipliers 1,
   e^((1+c_l)T), e^((2c_l-1)T). Exact non-decaying examples show that no H_0 + a(Jy).U + b|y|^2/2 (H_0 the self-similar
   Bernoulli function; a, b fixed) is monotone along W for all smooth rotating profiles; the decaying class and other
   functions are open.
9. Global identities. Exact profiles with a smooth differentiated natural tail satisfy weighted energy, enstrophy and
   helicity identities (consistency diagnostics). The ball identity integral_{B_R}(|U|^2+3P)dy = R
   integral_{dB_R}(U_r^2+P)dS holds for every R and any divergence-free field with its exact full-space pressure, so it
   tests the pressure computation only; with the energy law it gives a vanishing finite part of integral P.
10. Backward stretching. On the open invariant set, of full measure in {Omega != 0}, where W and Omega are linearly
    independent, the backward W-flow stretches some direction at least like e^((1-2c_l)t); so vortical points converging
    backward to a single equilibrium or with a single periodic orbit as alpha-limit form a null set. A necessary
    structural condition, not a classification of invariant sets or an obstruction. With DU bounded and U -> 0, a
    compact invariant set on which W x Omega does not vanish is uniformly hyperbolic for the backward flow (rates
    e^(-(1+c_l)t), 1, e^((1-2c_l)t)), and every nonzero profile carries an ergodic measure of the backward flow with
    largest exponent at least 1 - 2c_l, possibly supported in {Omega = 0}. Neither statement
    guarantees the existence of a nonempty compact invariant set on which W x Omega does not vanish, and the support
    of that measure may meet {W x Omega = 0}. For C^1 uniformly sublinear U (no Euler equation), every invariant
    probability of the W-flow is supported in the compact set of points with bounded forward W-orbit, which is
    Lebesgue-null when div U = 0.
11. Total stretching. A nonzero exact profile with the natural differentiated tail satisfies integral
    Omega.sym(DU)Omega dy = (1-3c_l/2) integral|Omega|^2dy > 0 (absolutely convergent). Sigma_Z, the left side over
    the right side (exact value 1), is dilation invariant and proportional to the amplitude for a weak field, so it
    separates nonlinear states from weak near-linear ones.
12. Critical points and zeros of W. For a C^2 exact profile, Omega.sym(DU)Omega = |Omega|^2 at every critical point
    of |Omega|^2 with Omega != 0. If U = o(|y|) uniformly, W has a zero; at a vortical zero, Omega is an eigenvector of
    DW with eigenvalue 1+c_l, the other two summing to 2c_l-1 < 0. Necessary local conditions.
13. Self-similar Kelvin law. For an exact profile, circulation around loops carried by W and vorticity flux through
    carried surfaces scale like e^(-(1-2c_l)s), so circulation around periodic W-orbits is zero (CIV (3.24)-(3.28) for
    omega = 0). Necessary conditions, not an obstruction.
14. Outgoing conditions with rotation. CIV's outgoing quantities are unchanged by rotation. (a) For any omega, a
    vortical zero of W never satisfies the local outgoing inequality when c_l < 1/2 + c*. (b) A C^2 profile with
    W.y >= c*|y|^2 everywhere, c* > 0 (Elgindi's Hypothesis 6.7, ICM 2026), has zero vorticity; with
    decay, U = 0. (c) Under local outgoing at finitely many zeros of W, vortical alpha-limit sets are compact,
    invariant and zero-free; for omega = 0 the Bernoulli function excludes them (CIV, Theorem 3.9), for omega != 0 no
    substitute is known.
15. Lower bound. The CIV bound C_p||grad Omega||_inf^(3/(p+3))||Omega||_p^(p/(p+3)) >= 1, p > max(3c_l,1), holds for
    every nonzero decaying rotating profile with |Omega| <= C(1+r)^(-1/c_l) and bounded grad Omega (C_2 =
    2(162/pi)^(1/5) = 4.40051). Values computed from sampled suprema or unresolved enstrophies are estimates, not
    certified bounds.
16. Localized strength and non-axisymmetry. (a) Every nonzero exact profile has lambda_max(sym DU) >= 1 somewhere in
    |y| <= max|U|/c_l. (b) With max|U| = 1, B the ball of radius 2/c_l+4 and KU = JU - (Jy.grad)U (zero exactly for
    axisymmetric fields), nonzero exact profiles obeying a given bound on first and second derivatives on B have
    max_B|KU| >= delta > 0, and none obeys it for |omega| > omega_0; delta and omega_0 depend only on c_l and the
    bound (compactness; no numerical value). (c) Under uniform normalized C^{2,beta} bounds on R^3 and a uniform
    decaying envelope (core bounds alone do not suffice), exact profiles with omega -> 0 have a subsequence converging
    locally in C^2 to a nonzero decaying non-rotating C^2 profile at the same c_l (whole-sequence convergence is not
    shown); nonexistence for small omega is only conditional on that companion theorem, which is not used as verified
    input.
17. Zero-free invariant sets (compactly supported W-invariant probability measures). (a) Under local outgoing at
    finitely many zeros, W has exactly one zero, with vorticity vanishing on a ball around it. (b) On a zero-free
    support with positive mean of |c_l y+U|^2, the mean swirl has the sign of omega; for omega = 0 no zero-free compact
    invariant set exists. None of this excludes a compact zero-free alpha-limit set of vortical points.
18. Angular degree of the first nonlinear far-field coefficient. If r^(-alpha)F is the curl of a twisted homogeneous
    potential whose angular part is a degree-d vector polynomial in the rotating frame, G[F] has spherical-harmonic
    degree at most 2d+3 and is the curl of a twisted potential of degree at most 2d+2; this is attained, so a
    correction space of degree below 2d+2 cannot carry G[F] for every leading tail of degree d. Both routes derived
    this. An analytic example, the axisymmetric potential with angular part n_3^d e_3, attains both bounds; a check
    using symbolic derivatives and numerical harmonic projection for d = 1, 2, 3 (c_l = 0.45, omega = 0.3,
    omega/c_l = 2/3) supports the intermediate degree counts. It concerns a formal far-field coefficient, not the
    existence of a profile.
19. Residual identities for approximate states. For any C^2 divergence-free U with |D^jU| <= C(1+r)^(-alpha-j) (j = 0,
    1, 2) and |grad P| <= C(1+r)^(-alpha), with no smallness assumed (normalized forms such as Sigma_Z require
    positive denominators; a zero denominator gives no quotient bound): (a) integral R_u.curl Omega dy =
    (1-3c_l/2)(1-Sigma_Z)Z, Z = integral|Omega|^2, so a stretching defect forces a weighted momentum residual, but a
    small defect does not force a small residual; (b) with B = U.W - |U|^2/2 + P, (1-2c_l) integral f(B)U.Omega dy =
    integral f(B)Omega.R_u dy for every continuous f.
20. Finite-shell residual ratios are not proximity certificates (continuum statement). Adding copies of compactly
    supported steady Euler flows (arXiv:1810.08020; arXiv:1903.11699) to a smooth background with fixed tail, gauge
    and phase makes the five-term and nonlinear-balance ratios on finitely many fixed shells, and the ratios of the
    shell maximum of the residual to those two sums, arbitrarily small (the ratios of that maximum to the self-similar
    and smaller sums are not made small), while one further steady flow keeps the family a fixed positive local L2
    distance from every exact profile. What resists: ||R_Omega||_2/||Omega||_2 (limit at least 1-3c_l/2, 0.325 at
    c_l = 0.45), the single-term ratio RMS(R_u)/RMS((1-c_l)U), the fixed-gauge absolute residual, the residual peak
    factor and the maximum speed; the single-term ratios are not shown to certify proximity either. Not an obstruction
    to profiles.
21. Homogeneous steady fields of degree -alpha (continuum statement; 1 < alpha < 2). Let u = r^(-alpha)f be a smooth
    divergence-free steady Euler field on R^3 minus the origin, with radial coefficient b and Bernoulli function
    r^(-2alpha)h. (a) The sphere integrals of b Phi(h) and of the radial vorticity times Phi(h) vanish for every bounded
    Borel Phi. (b) If u != 0, then h >= 0, positive somewhere and zero somewhere. (c) u = 0 if h^(-(alpha-1)/(2alpha))
    is integrable on {h > 0}, not implied by smoothness alone. (d) u = 0 for Beltrami, irrotational, axisymmetric,
    tangential and zero-radial-vorticity fields. Several are earlier results of R. Shvydkoy (arXiv:1510.03378v1); no
    novelty claimed. The general non-axisymmetric case is open; not an obstruction.
22. Twisted homogeneous steady fields (continuum statement). For steady fields homogeneous of degree -alpha under
    dilations combined with rotations about e_3 at rate k (1 < alpha < 2), item 21(a), h >= 0, the impossibility of h >
    0 everywhere, 21(c) and 21(d) hold for every k (zero radial vorticity without integrability assumption), and alpha =
    1 is excluded; the general non-axisymmetric case is open. A profile's tail has k = -omega/c_l. Not an obstruction;
    no novelty claimed.
23. The edge c_l -> 1/2 and the finite part of the energy (continuum statements). (a) A smooth twisted-homogeneous
    steady field of degree -1 on R^3 minus the origin vanishes, which excludes an exactly homogeneous outer limit at the
    edge (reaching one from profiles with c_l -> 1/2 would need a retained nonzero angular norm). (b) For smooth
    divergence-free U with its decaying pressure, int_(B_R)U.R_u = beta_0 E(R) + (c_l R/2)E'(R) + int_(S_R)H U.n, E(R) =
    int_(B_R)|U|^2, H = P+|U|^2/2, beta_0 = 1-5c_l/2; an exact profile with unit leading tail, remainder O(r^(-alpha-1))
    and P = O(r^(-2alpha)) has E(R) = R^p/p + E_ren + o(1), p = 3-2alpha, with E_ren = 0 (for an approximate state E_ren
    needs a quantified tail remainder). (c) Compact steady Euler seeds fail the first solvability condition of one
    regular small-core expansion. (d) An explicit axisymmetric pure swirl with exact unit-gauge tail has a_eff =
    0.096566 at c_l = 0.45 and 0.054912 at c_l = 0.48. (e) A non-axisymmetric comparison family (fields, not profiles):
    for fixed omega != 0 and c_l,n = 1/2 - 1/n^2 (omega/c_l,n = 2 omega n^2/(n^2 - 2)), smooth divergence-free fields
    made of a compact axial jet and a disjoint unit-gauge azimuthal-mode-2 spiral tail on r >= 8n (which solves the
    leading linear equation exactly), with their decaying Newton pressures, have zero rotation average about e_3 and
    zero total helicity; on every fixed ball B_R, int_(B_R)|U|^2 tends to 2 pi R and ||R_u||_(L2(B_R)) = O(n^(-1/2)),
    while max|U|, max|Omega| and max|R_u| on B_R diverge and |U|^2 dy concentrates on the axis. So a small fixed-ball
    relative residual does not control pointwise residuals or concentration; nothing is established at fixed c_l. (f) A
    vertical shear gap (fields, not profiles): for U = f(x_perp)e_z on a ball B_R with a smooth pressure P,
    int_(B_R)U.R_u = (1-2c_l)E(R) + (c_l/(2R))int_(S_R)|x_perp|^2 f^2 + int_(S_R)P f z/R, so ||R_u||_(L2(B_R)) >=
    (1-2c_l)||U||_(L2(B_R)) for every omega whenever the pressure boundary work is nonnegative (for example P even in
    z); the planar constant is sharp. This restricts a z-independent vertical shear core at fixed c_l and is why (e)
    needs c_l,n -> 1/2; it is not an estimate for general fields. None is an obstruction at 2/5 < c_l < 1/2.
24. Backward-transport form of the profile equation (continuum statements). (a) Gf(y) = int_(-inf)^0
    e^((1-c_l)s)R(omega s)f(e^(c_l s)R(-omega s)y)ds is the unique inverse of the linear part of R_u with outputs
    bounded near the origin and preserves divergence-free fields. (b) For divergence-free U in the symbol class of
    order -alpha with its decaying full-space pressure, the profile equation is equivalent to U = -GN(U), N(U) =
    (U.grad)U + grad P. (c) Plain unit-tail normalized fixed-point iteration is unstable whenever a nonzero profile
    exists (eigenvalue 2). (d) For a fixed smooth divergence-free background U_b in the symbol class of (b), for
    which (c_l I - omega J)y + U_b has a stagnation point y_0 != 0, steady Euler copies concentrated at y_0 drive
    delta_G = RMS(GR_u)/RMS(U) on the ball of radius a_eff/2 at the vorticity maximum to zero. Neither an obstruction
    nor a proximity certificate.
25. Eddy generation of the mean swirl. Let <.> be the azimuthal average, u' = U-<U>, Gamma_0 = <(Jy).U>, W_0 = c_l
    y + <u_rho>e_rho + <u_z>e_z and S = -div(rho<u'u'_phi>). (a) For every smooth divergence-free U, pressure and omega,
    rho<R_u.e_phi> = (1-2c_l)Gamma_0 + W_0.grad Gamma_0 - S. (b) For 0 < c_l < 1/2, bounded U and DU and an exact
    profile, the mean swirl, tail included, is generated entirely by S along backward W_0 trajectories, and
    (1-2c_l)sup|Gamma_0| <= sup|S|. Not an obstruction; the numerical mean-swirl findings (sections 5.3 (c), 5.6 (d) and
    5.7 (f)) are statements about approximate states.
26. Pressure-free mean-swirl tail defect. For every C^1 U, single-valued C^1 P and omega, E = <R_u.e_phi> = c_l(alpha
    v + r d_r v) + A, v = <U.e_phi>, A = <e_phi.(DU)U>. If U = O(r^(-alpha)), DU = O(r^(-alpha-1)) and the mean-swirl
    tail is F_0phi, then (1/c_l) int_0^R r^(alpha-1)E dr tends to D_0phi = F_0phi + (1/c_l) int_0^inf r^(alpha-1)A dr,
    which vanishes for an exact profile and needs no pressure.
27. Mean angular-momentum results (notation of item 25; f the mean azimuthal part of the leading tail). (a) With p_0 =
    3c_l/(1-2c_l) (13.5 at c_l = 0.45) and T_0 = int_(S^2)|sin(theta)f|^(p_0) > 0, every exact profile with that tail
    obeys ((1-2c_l)/3)T_0 = int S Gamma_0|Gamma_0|^(p_0-2)dy. (b) For exact profiles, a fixed nonzero mean-swirl tail
    needs eddy content bounded below in explicit weighted sup norms. Neither is an obstruction.
28. Constructive lower bound on non-axisymmetric content. Assume max|U| = 1, U -> 0 at infinity (needed) and finite
    global weighted bounds A on DU and B on D^2U. Then ||<U>||_inf is bounded by explicit powers of weighted eddy
    norms delta_j and mean-residual sup norms, with constants independent of omega, so an exact profile has
    delta_0 >= delta_*(c_l,A,B) > 0, a numerically vacuous threshold (delta_* = 9.9e-10 at c_l = 0.45 and the
    unattained boundary A = alpha, B = 1). With sigma = sup|rho<R_u.e_phi>|, sigma >= (1-2c_l)max|Gamma_0| - max|S|
    for every such field, which equals max|S|(Q_sw-1) when max|S| > 0. On sampled maxima the right side is a
    consistency check, not an enclosed bound: 0.011 on the degree-4 balanced-core state at c_l = 0.45, omega = 1,
    omega/c_l = 20/9 (the sampled Q_sw is above 1) and negative on the other seven exported states (the sampled Q_sw
    is below 1); this neither establishes nor excludes Q_sw <= 1. Not an obstruction.
29. Artificial viscosity, used only to design a labelled continuation device (section 5.6 (e)), never as Euler results.
    For R^nu = R_u - nu Delta U = 0 with constant nu > 0, a differentiated tail U = r^(-alpha)F + O(r^(-alpha-delta)),
    delta > 3-2alpha, and P = O(r^(-2alpha)): exact solutions have beta_0 E_ren + nu int|grad U|^2 = 0, beta_0 < 0, so
    E_ren > 0 if U != 0, while the ten independent-route states of section 6.4 have E_ren from -1.021 to -0.519 (no
    quantitative distance to viscous solutions follows); and C^3 solutions with U, Omega decaying and sup|DU| < 1 vanish
    (no claim in terms of sup|U| alone). None of this says anything about existence for either equation.
30. First far-field energy coefficient. Let U_0 = r^(-alpha)F be a smooth divergence-free twisted-homogeneous field on
    R^3 minus the origin, P_0 = r^(-2alpha)Q its unique twisted-homogeneous pressure and U_1 = (U_0.grad)U_0 + grad
    P_0 = r^(-2alpha-1)G. (a) Without any profile equation, int_(S^2)F.G dS = (2-3alpha)Phi_F, Phi_F =
    int_(S^2)F_r(|F|^2/2+Q)dS. (b) A smooth exact profile with its decaying whole-space pressure and |D^j(U-U_0)| =
    O(r^(-alpha-1-j)), j = 0, 1, has s^(2alpha) int_(S^2)|U(sn)|^2dS = int|F|^2 + K_1 s^(-(alpha+1)) + O(s^(alpha-4)),
    K_1 = 2(2-3alpha)Phi_F (s^(alpha-4) is the first allowed remainder rate, not a term known to be nonzero). Nothing
    here concerns existence.
31. Local vorticity representation and helicity flux rate. For C^2 divergence-free U and C^2 single-valued P near a
    closed ball B centred at the origin, Omega on B is an explicit backward-time integral of curl(U x Omega) + curl R_u,
    so sup_B|curl R_u| >= sup_B|Omega| - sup_B|curl(U x Omega)| (sampled maxima do not certify it). With differentiated
    twisted-homogeneous tails and P = O(r^(-2alpha)), the leading helicity flux cancels the exterior helicity, so an
    exact profile has H_tot = 0. A local necessary condition and diagnostic, not an obstruction.
32. Representation bounds for the primary basis (fixed finite sums of its channels). Explicit bounds beyond a radius R
    satisfying the Cauchy-disk condition of the proof bound the omitted exterior finite-part energy and helicity after
    their leading terms, without any profile equation; they are small because the endpoint derivatives q'(1) are small
    (at most 1.8e-11 on the exports). Statements about the representation, not the equation; none bounds a
    finite-domain quadrature.
33. Reflection. For any C^4 divergence-free U and C^3 P (no equation assumed), U_new(y) = SU(Sy), P_new(y) = P(Sy), S =
    diag(1,-1,1), with omega replaced by -omega and c_l unchanged, give R_u_new(y) = SR_u(Sy). Norms, residual ratios,
    non-axisymmetric fractions, N_F, e_F and E_ren are unchanged; the signed helicity, H_F and H_tot change sign. All
    evaluated states have omega > 0. H_tot < 0 on the seven independent-route states of section 6.4 is a finding about
    those states, not a sign fixed by the equation: the independent reconstruction of a primary degree-6 rung at
    c_l = 0.45, omega = 0.3, omega/c_l = 2/3 gives H_tot = +4.29 (section 5.7 (a)).
34. First far-field helicity coefficient (notation of item 30; Omega_0 = curl U_0 = r^(-alpha-1)H). (a) For C^2 U and P,
    with h = U.Omega and N = (U.grad)U + grad P, U.curl N + N.Omega = div(hU + (P-|U|^2/2)Omega), with no divergence
    condition and no profile equation. (b) Without any profile equation, int_(S^2)(F.curl U_1 + U_1.H)dS = K_H :=
    (1-3alpha)Psi_F, Psi_F = int_(S^2)[(F.H)F_r + (Q-|F|^2/2)H_r]dS. (c) Under the hypothesis of item 30 (b), an exact
    profile has s^(2alpha+1) int_(S^2)h(sn)dS = H_F + K_H s^(-(alpha+1)) + O(s^(alpha-4)). (d) For an approximate field
    with rate-(2alpha+1) part V_1, the carried/required ratios of the energy and helicity coefficients equal 1 for an
    exact profile whenever the required value is nonzero; they are different projections of V_1 - U_1, and equality of
    either does not imply V_1 = U_1. Nothing here concerns existence.
35. Vorticity flow and vorticity zeros. For an exact C^2 profile with U = o(|y|) uniformly and any omega/c_l,
    D Omega W - DW Omega = -(1 + c_l) Omega, so the backward W-flow maps vortex lines to vortex lines with parameter
    scaled by e^(-(1+c_l)t) inside one ball. (a) No closed vortex line carries nonzero vorticity (the periods would
    tend to 0, below the Lipschitz bound 4/L). (b) On compact sets invariant under the vorticity flow its derivative
    grows subexponentially and its entropy is zero; no such nontrivial set is asserted. (c) At a vorticity zero p,
    (D Omega(p))^3 = 0, so det D Omega(p) = tr((D Omega(p))^2) = 0. (d) If a C^2 field V has, on a ball B of radius r
    about q and for an invertible M, |M curl V(q)| <= eta and sup_B ||I - M D curl V|| <= k with k < 1 and
    eta < (1 - k) r, then a C^2 neighbourhood of V, given by verified bounds on D(U - V)(q) and sup_B |D^2(U - V)|,
    contains no exact profile. No saved state has been tested against (d). Necessary conditions only.
36. Vorticity-amplitude identities. For C^2 divergence-free U, a = |Omega|, R_Omega the curl of the momentum residual
    (no pressure), and e = Omega/a and s = e.DU e on {a > 0}: W.grad a = (s - 1)a + e.R_Omega there, and the products
    with psi(a) or psi'(a) below are set to zero where a = 0. If a -> 0 at infinity, integral [3c_l psi(a) + (s - 1)a
    psi'(a)] dy = -integral psi'(a) e.R_Omega dy for psi in C_c^1((0, infinity)), which, when ||psi'(a)|| > 0, bounds
    ||R_Omega|| below on the support of psi'(a) for exact integrals (on a bounded domain B the flux integral_dB psi(a)
    W.n dS is subtracted from the left side); for an exact profile the 1/|grad a|-weighted average of s on a regular
    level a = t with t > 0 and {a > t} nonempty is 1 - 3c_l V(t)/(t rho(t)) < 1. Identities with the residual
    retained, not an obstruction.

## 3. Acceptance norms (registered before any candidate was selected; never relaxed)

This section is a compact introduction. The binding acceptance conditions are those of the registered specification
among the accompanying artifacts (version v1.24 of 2026-10-25T09:54:00Z); every condition there applies, including those
not restated here, and the formulas of N_core, N_F, the origin jet floors, E_F, E_G, E_H, E_D and the two field
comparison norms are taken from it. pi_u and pi_nl are the shell maxima of |R_u| divided by the same RMS term sums as
rho_u and rho_nl, and peak = pi_u / rho_u on each shell; A_u and A_Om divide the weighted residual by the reference
scales Lambda_u = max_k (1 + r_k)^(2 alpha + 1) RMS_k(U)^2 / r_k and Lambda_Om = max_k (1 + r_k)^(2 alpha + 2)
RMS_k(U)^2 / r_k^2.

Diagnostics are taken in the gauge integral_{S^2} |F|^2 = 1, on a core ball and dyadic shells. The standard family is
[2^j, 2^(j+1)), the offset family [2^(j+1/2), 2^(j+3/2)); r_k is the geometric midpoint of shell k (r_k = 0 for the
origin ball). The shell ratio rho_u is RMS(R_u) divided by the sum of the RMS of the five frame-invariant momentum terms
T1 = (1 - c_l)U, T2 = c_l (y . grad)U, T3 = omega[JU - (Jy . grad)U], T4 = (U . grad)U and T5 = grad P; rho_u^max is its
maximum over shells. Every threshold must hold on both families. Core sets: inner shells down to a_eff/16 and the balls
B(y_*, a_eff/2) and B(y_*, a_eff/4) at the vorticity maximum y_*, a_eff = 2 sqrt(2) max|U| / max|Omega|.

Table B. Notation of the diagnostics (exact value for a profile; Tier S bound where one exists).

| Quantity | Numerator / denominator | Domain | Exact; Tier S |
|---|---|---|---|
| rho_u, rho_u^max | RMS_k(R_u) / (RMS_k(T1) + ... + RMS_k(T5)) | each shell; maximum per family | 0; 1e-2 |
| rho_nl^max | RMS_k(R_u) / (RMS_k(T4) + RMS_k(T5)) | all shells | 0; 1e-1 |
| rho_sp^max | max(rho_nl, RMS_k(R_u) / (RMS_k(T1) + RMS_k(T2) + RMS_k(T3))) | all shells; abs(y) < 1 | 0; 1e-1 |
| sigma_u^max | RMS(R_u) / RMS((1 - c_l)U) | shells of both families, ball abs(y) < 1, core sets | 0; 1e-1 |
| sigma_Om | L2 norm of R_Omega / L2 norm of Omega | resolved shells (+ exterior); domain stated | 0; 1e-1 |
| a_max | max of (1 + r_k)^(2 alpha + 1) RMS_k(R_u), fixed gauge | shells and core sets | 0; Tiers R, A |
| rho_P^max | RMS_k(R_P) / (RMS_k(Delta P) + RMS_k(tr (DU)^2)) | shells | 0; 1e-3 |
| rho_div^max | RMS_k(div U) / RMS_k(abs(DU)) | shells | 0; 1e-8 |
| N_core, N_F | derivative-weighted non-axisymmetry indices | core shells; tail | none; >= 1e-2 |
| e_core, e_F | m != 0 energy fractions | core shells; tail | none; >= 1e-4 |
| E_ren, H_tot | finite part of the ball energy; total helicity with exterior term | whole space | 0; reported |
| K_E, K_H ratios | carried / required first far-field energy and helicity coefficients | far field | 1; reported |
| Q_sw | (1 - 2 c_l) max abs(Gamma_0) / max abs(S) on sampled maxima (2, item 25) | sampled points | global-supremum version <= 1; sampled value reported |
| tau_F, delta_G | tail-generation defect; backward defect (2, item 24) | far spheres; core balls | 0; reported |
| q | rho_u^max at one degree / rho_u^max at the previous degree | per family | weak if > 0.85 |

On the core balls a_max uses the centre weight r_k = |y_*| (the analogue of the shell midpoint); the upper-radius value
(1 + |y_*| + radius)^(2 alpha + 1) RMS(R_u) is reported alongside, and the decrease requirement below must hold with
both weights. sigma_Om values on |y| < 1024 are resolved-region values, not whole-space norms. Nontriviality guards: N1,
the tail gauge holds to 1e-8; N2, the strain ratio Omega.S Omega/|Omega|^2 at max|Omega| (exact value 1, also at the
three next local maxima) and lambda_max(S) there (exact >= 1); N3, the indices N_core, N_F, e_core, e_F; N4, core
location, width and amplitudes, with the core at least four octaves inside the sampled range; N5, the tail onset radius
(flagged above 2^8 core radii or if growing by more than 2 per level); N6, spectral decay (energy fraction in the top 20
per cent of angular degrees and radial modes).

Three nested tiers: Tier S (discovery tier, Stage I), Tier R (refinement-stable, values at the finest of three levels)
and Tier A (required for label A). Each tier includes every requirement of the lower tiers, evaluated at its own level.

| Quantity | Tier S | Tier R | Tier A |
|---|---|---|---|
| rho_u^max (shell relative RMS of R_u) | 1e-2 | 1e-4 | 1e-6 |
| rho_nl^max (far-field nonlinear balance) | 1e-1 | 1e-3 | 1e-5 |
| rho_sp^max (residual over the smaller group sum) | 1e-1 | 1e-3 | 1e-5 |
| single-term ratio sigma_u^max | 1e-1 | 1e-3 | 1e-5 |
| sigma_Om (vorticity form, global norm ratio) | 1e-1 | 1e-3 | 1e-4 |
| rho_P^max (Poisson residual) | 1e-3 | as Tier S | 1e-7 |
| rho_div^max (divergence) | 1e-8 | as Tier S | 1e-10 |
| rho_Om^max (vorticity form), pi_u^max (pointwise) | not required | not required | 1e-5, 1e-4 |
| Taylor residuals at the origin tau_0, tau_1, tau_2 | not required | not required | 1e-5 |
| non-axisymmetry N_core, N_F and e_core, e_F | at least 1e-2 and 1e-4 | not collapsing | not collapsing |
| guards N1 to N6 | no flag (N2: lambda_max(S) >= 0.9) | stable | stable |
| independent re-evaluation of pressure and momentum | not required | within a factor 3 | within a factor 3 |
| resolution | one level | three levels, rho_u^max falling by >= 10 | three improving levels |
| independent refinement in its own representation | not required | not required | same field to 1e-4 |

All quantities are evaluated on holdout points that were not used in training, with the full-space pressure.
Model-selection holdout points (used for ranking, early stopping and the choice of levels) are distinct from final-test
points, which are drawn with a fresh recorded seed after the coefficients are frozen (by the independent route for Tiers
R and A) and used only for acceptance. Tier A also requires A_u <= 1e-5, A_Om <= 1e-4, pi_nl^max <= 1e-3, the energy and
helicity identities to hold within their error estimates, the vorticity-maximum identity to 1e-4, and the bound on every
omitted tail term to lie below each threshold.

Further registered requirements, each added before any state met the discovery tier, each only tightening: in the
refinement and label-A tiers a_max must fall by a factor of at least 10 over the three levels, and from the second to
the third level the maximum speed, the maximum vorticity and the L2 norm on the unit ball may grow by at most 10 per
cent; sigma_u^max and a_max are also taken on the core sets, and on each core set RMS(R_u) and RMS((1 - c_l)U) must each
change by less than 10 per cent when the radial and angular node counts are doubled (the core doubling test; a stable
ratio is not enough), with a_eff changing by less than 10 per cent from the second to the third level; a state whose
m != 0 content falls by more than a factor 2 per level is flagged as collapsing. Also registered: a_max decreases
monotonically over the three levels and, on every shell, peak grows by at most a factor 2 from the second to the third
level (Tier A keeps the peak bound 30, with an explanation required above it); each Tier R level raises the angular
degree and the radial degrees of freedom by at least 1.3 times and the nonlinear quadrature by at least 1.5 times, the
gauge-aligned field differences decrease in both registered norms, the parameter drift decreases, and the exterior
closure tests X1 and X4 are done (three evaluation quadratures of one fixed state are not three levels); Tier A adds
rho_Om_nl^max <= 1e-4 and rho_Om_sp^max <= 1e-4, E_F, E_H and E_D decreasing at their predicted rates, E_G <= 1e-2
after subtracting the fitted quadrupole velocity term, X1 to X5 passed, float64 and extended-precision far checkpoints
in agreement, and the 1e-4 independent field comparison in both norms with the parameters agreeing within the stated
uncertainty. A flagged denominator is a failure until resolved, and no epsilon is inserted; for the grouped ratios the
evaluation error of R_u on a shell must be at most 0.1 times the tier threshold times the smaller group sum. The two
shell families and the added balls are distinct domains, and a sphere or a point is not a volume shell. A state within
0.02 of either end of the c_l interval is near edge and supports label A or B only if a_eff, the enstrophy containment
radius R_90 and the tail-fit onset radius each change by at most a factor 2 between the second and third levels.

Ordering rule: a state ranks ahead of another only if it has the lower holdout rho_u^max on both shell families and its
sigma_u^max, sigma_Om and a_max each exceed the other's by at most 10 per cent; otherwise, or if a quantity is missing
for either state, the two are reported as not ordered.

Ladder rules. Promotion: a branch goes to the next angular degree only if its core passes the doubling test and its
holdout rho_u^max is at most 0.1. Resolution step: a step with factor q > 0.85 is weak, and two weak steps in succession
floor a branch at the tested optimizer and budget (operational only). If a continuation or test at the same degree
lowers a holdout by more than 5 per cent, the factor is recomputed. A factor taken at the iteration limit, where the
relative cost decrease V10 over the last tenth of the iterations exceeds the registered stationarity bound 1e-3, mixes
truncation and budget and is read together with its V10. Stall rule: a branch is stalled if over the last two refinement
levels rho_u^max decreases by less than a factor 2 while rho_u^max >= 1e-3; a stalled branch cannot be labelled B.

Labels. A: a Tier A candidate, verified by the independent route (not a proof of existence). B: a candidate that passes
Tier S at the finest level, decreases rho_u^max by a total factor of at least 10 under at least three refinements
without stalling, has an independent re-evaluation within a factor 3 and stable N1 to N6, but fails some Tier A item,
with all defects stated quantitatively. C: otherwise, with the precise searched class; not nonexistence. D: only a
complete, independently confirmed proof covering the stated class; an optimizer failure never gives D.

Necessary conditions reported without threshold (exact profiles satisfy them; approximate states are measured against
them): E_ren = 0 and H_tot = 0; K_E = K_H = 1; Q_sw <= 1, which is only ever sampled at finitely many points, so a
sampled value below or above 1 neither establishes nor excludes the condition.

## 4. Methods

Two numerical routes were written from the problem statement with no shared code, both in float64 and both evaluating
the original momentum residual R_u with the full-space pressure. A third, CPU-only line of work (the theory route) wrote
the specification, derived the identities of section 2 and computed diagnostics from exported samples; its computations
are labelled as such and are not independent evaluations.

4.1 Primary route: representation. U = curl(T y) + curl curl(S y), with T and S expanded in real orthonormal spherical
harmonics written as regular solid harmonics (exact Cartesian polynomials, so U is smooth at the origin and on the
axis), times shifted Chebyshev polynomials in x = (s - R_0)/(s + R_0), s = (r^2 + R_0^2)^(1/2), with envelopes
(s/R_0)^(-(alpha + l)) for T and (s/R_0)^(-(alpha + l - 1)) for S and the twist phi + (omega/(2 c_l)) log(1 +
r^2/R_0^2). This carries the exact leading tail r^(-alpha) F and its twist. Separate radial channels, damped in the
core, carry the twisted rate 2 alpha + 1 of the first nonlinear correction (at angular degrees up to 2L + 3, so that
they can represent G[F]) and untwisted harmonic pressure-driven terms. Even azimuthal wavenumbers are the default. L
denotes the angular degree of the main blocks.

4.2 Primary route: residual, objective and solver. Residuals are evaluated in Cartesian components on a product grid
(Chebyshev-Gauss radial nodes, Gauss-Legendre in theta, uniform in phi). The objective is the least-squares residual
norm on a core ball and dyadic shells, scaled by (1 + r^2/R_0^2)^(alpha/2), with each shell divided by the sum of the
RMS of the five momentum terms (a scale normalization: normalization alone does not prevent lowering these ratios by
inflating the core or by added compact structures, section 2, item 20, so the fixed-gauge absolute residual, the
single-term ratio and the nontriviality guards are read beside it), an added far-shell weight and the two
gauge rows. Optional rows: closure rows tying the carried first correction to G[F]; the two whole-space balances; pins
on the core amplitude and the m != 0 energy fractions. The solver is Levenberg-Marquardt with a forward-mode
automatic-differentiation Jacobian and Cholesky-solved normal equations; at degree 10 J^T J is accumulated from column
blocks, and on a degree-8 test the two paths agree to 4.6e-11 in the two-step displacement (primary-reported). L-BFGS
served as a comparison. Free (c_l, omega) runs rebuild the pressure kernels after accepted steps.

4.3 Independent route. U = curl A with twisted Cartesian vector potentials A_b(y) = q^((1 - alpha)/2) exp(-psi J) e_j
M_b(exp(psi J) y / q^(1/2)) (R_0^2/q)^p, q = R_0^2 + r^2, psi = (omega/(2 c_l)) log(q/R_0^2), with M_b Cartesian
monomials and powers p chosen for the leading tail, its regularization and the rate 2 alpha + 1. The untwisted
channels, of velocity rate k + 1 for k >= 3, use untwisted coordinates and components, that is psi = 0 in those
channels (for k = 3, p = (4 - alpha)/2). Velocity and Jacobian come from an explicit second-order jet implementation,
checked against automatic differentiation. The pressure is the full-space ray integral grad P(x) = (1/(4 pi))
integral_{S^2} n integral_0^infinity f(x + rho n) d rho dS, f = tr((DU)^2), with a Gauss-Legendre angular rule and the
compactification rho = R_0 t/(1 - t), so the whole exterior is included and no boundary value is fitted. The route
also has a separately written scalar spherical Green source and pressure implementation, used in its degree-8 and
degree-10 fresh batteries and in the five-export pressure comparison of 6.3; each result below names the method used.
Agreement between two source orders within one implementation is same-method agreement, not method independence and
not an error enclosure. A core and tail Gram matrix removes numerical null directions. Optimizers: damped
Levenberg-Marquardt with an analytic Jacobian, Gauss-Newton and L-BFGS. The route rebuilds exported states from their
written basis descriptions. Separate scalar readers reassemble quantities from the saved Cartesian arrays in extended
precision; in the degree-8 export re-reads of 6.2 a scalar passes if it agrees with the producer's value to 1e-11 in a
unit-floored relative sense; later registered readers state their own guards (for example 1e-8 on a recomputed
energy-identity defect).

4.4 Pressure and exterior treatment. In the primary route the pressure is computed per spherical harmonic from the Green
formula P_lm(r) = (1/(2l + 1)) [r^(-l-1) integral_0^r s^(l+2) f_lm ds + r^l integral_r^infinity s^(1-l) f_lm ds], in the
true azimuth, with composite Gauss quadrature in log r that resolves the oscillation s^(i m omega/c_l) of twisted source
terms; integrals beyond the last radial node use the analytic tail model termwise. In the primary route's tests
against its ray-integral cross-check (primary-reported) pressure agreed to 1e-13 with three radial quadrature nodes
per radial basis function and to 4e-3 with 1.5; the tested sources, parameter range and norm are not stated in that
record, so this is an observed passing rule for those tests, not a guarantee for every state. Discovery runs used 2.5
nodes per function and validation runs 3.
The independent route's ray integral is the early cross-check (agreement 1e-13 on manufactured sources). The later
direct comparison on five degree-8 exports is separate: it used the route's radial Green pressure (radial orders 24,
36 and 48, source angular degree 44 on a 48 by 96 grid, the leading homogeneous exterior source integrated
analytically, source moments 0 and 1 set to their proved value 0), and 243 of 270 comparisons pass at 1e-11
(independently checked, section 6.3). The whole-space balances include exterior parts: E_ren is the finite part of the
ball energy after the divergent R^((5 c_l - 2)/c_l) term is removed. In the primary route's values H_tot includes the
exterior helicity term K_H R^(1 - 3 alpha)/(3 alpha - 1) fixed by the first far coefficient, and both are reported
with their change over the last two radial octaves as an exterior error estimate. In the independent route's degree-8
fresh battery H_tot includes only the leading exterior term (the angular helicity of the leading tail times
R^(2 - 2 alpha)/(2 alpha - 2)), with the omitted exterior error open, while E_ren integrates the represented energy
difference over exterior panels to 2^32 and carries an exact bound on the omitted tail beyond. None of these estimates
encloses finite quadrature or roundoff.

4.5 Holdout evaluation and exchange. The acceptance residuals of the fresh batteries are holdout evaluations separate
from training; saved-sample readouts (marked S), training-only values and partial pilot quantities are labelled where
they occur. A holdout set is a
core ball and two dyadic shell families with Gauss radii and exact volume weights, a rotated, denser angular grid, and
the pressure recomputed at the holdout points from the full-space source. States pass between routes in a fixed exchange
format (basis conventions, coefficients, and the field, its derivatives, the pressure and its gradient on 105 spheres,
at random points, on the axis and at the origin, with checksums).

4.6 Tolerances and tests. Production field evaluations are float64; reassembly checks use extended precision, and the
wider-precision and multiprecision controls are recorded separately where they are cited. Primary code tests
(primary-reported; last run as a suite on 2026-10-26, in Stage II, and not rerun from a clean process in Stage III;
the Stage III software tests are those of 6.9 (l), (m) and (n)): field assembly against an independent symbolic
construction (4e-16) and divergence (1e-15); curl R_u = R_Omega; the Green solver on manufactured and twisted sources
(1e-13 to 5e-15); dilation and rotation covariance (1e-15); the reflection omega to -omega (exact); annihilation of
the leading tail (1e-16); interruption and resume (the literal test of the worker of 24 October over the registered
window of iterations 13 to 22 meets the registered 1e-10, with maximum relative coefficient difference 1.36e-14; the
iterates are not bitwise identical, and the costs are bit-equal at 7 of the 10 steps; independently checked; in a
repeated software test on 27 October the deployed worker v2.4 resumed from its checkpoint after kill -9 and completed
a disposable two-start job, 6.9 (l)); the Jacobian against finite differences. On the end state of the independent
route's 12-step degree-10 optimization (c_l = 0.45, omega = 0.3, omega/c_l = 2/3), fourth-order central differences
of the coded fields at 31 points, with steps max(R_0, |y|) 2^-p for p = 4 to 12, reproduce the coded DU, curl R_u =
R_Omega, div U, div R_u + R_P and the Poisson residual of the pressure to best normalized errors 2.58e-12 to
1.37e-10; over the coarser steps the ratios of successive step differences lie between 14.48 and 16.01, fourth order
giving 16 (independently computed; the fourth-order readings were recomputed by the theory route from the saved
samples). Four strict reader checks at the two finest steps fail (1.64e-11 to 3.03e-11 against 1e-11) and are kept,
the second-order stencils miss the registered tolerances for three of the five quantities (the other two are
undecided), and the test bounds no residual, pressure or source error. The other operator tests of the independent
route were audited in Stage III from their saved values and test sources, not rerun: 16 operator predicates on finite
manufactured fields, two stable basis checks of the linear vorticity and an aggregate Taylor and covariance test at
the origin pass their saved criteria, with the manufactured forcing retained (independently checked as saved records;
the original runtime provenance of these records is incomplete). No complete clean-process final suite of the
independent route is established.

## 5. Search coverage and results

Status labels. "(independently checked)": confirmed by the independent route, by recomputation with its own
reconstruction, pressure and residual code, by a fresh holdout of its own state, or by an independent readout where so
stated; "(primary-reported)": a value no other route re-evaluated; "(theory route)": computed by the theory route from
the primary route's exported samples or coefficients; such values count as primary-reported. a/b is holdout rho_u^max on
the standard/offset shell family. No training loss is evidence; no state below is a candidate. Notation as in Table B,
and m is the relative L2 mismatch of the carried rate-(2 alpha + 1) angular profile, c the absolute cosine between the
required profile and F (defined only when it is nonzero), and |energy ratio - 1| <= m/c, a sufficient bound, not a
necessary condition; E_F(s) = s^(2 alpha) int_(S^2) |U(s n)|^2 dS.

Tables A and D were split on 2026-10-26 so that each row is one saved state: the earlier combined rows St5, St7,
St8, St9 and St11 are now St5a/b, St7a/b, St8a/b, St9a/b and St11a/b, and the independent tau_F, Q_sw and
pointwise swirl checks that earlier text attributed to the degree-8 state with free channels belong to St11b.

Table A. State legend. Nest ladder: the primary route's own random starts promoted from degree 2 through degrees 4, 6
and 8 (balanced cores). D6 lineage: primary-route continuations of the independent route's degree-6 state. A balanced
core means that the self-similar and nonlinear groups balance in the core; it is not a pass of Tier S. Record status:
the rank on the primary candidate leaderboard (LB), where listed, and whether an independent copy exists. The mapping
from state IDs to saved records is in the accompanying artifacts; St12 is the independent route's own state.

| ID | State | c_l, omega, omega/c_l | Degree | Record status |
|---|---|---|---|---|
| St1 | nest ladder: St2 with 8 instead of 4 far-correction radial functions (channel test) | 0.45, 1, 20/9 | 8 | not on the LB; independent copy |
| St2 | nest ladder: St3 continued with a 150-iteration budget (stopped on ftol after 83 iterations) | 0.45, 1, 20/9 | 8 | LB rank 1; independent copy |
| St3 | nest ladder: degree-8 rung | 0.45, 1, 20/9 | 8 | LB rank 3; independent copy |
| St4 | nest ladder: first degree-6 rung | 0.45, 1, 20/9 | 6 | LB rank 7; independent copy |
| St5a | nest ladder: degree-4 state from start p1 | 0.45, 1, 20/9 | 4 | LB rank 30; not exported, no independent copy |
| St5b | nest ladder: degree-4 state from start p0 | 0.45, 1, 20/9 | 4 | LB rank 31; independent copy |
| St6 | balance arm: a degree-4 state with weighted balance rows, guarded run | 0.45, 1, 20/9 | 4 | LB rank 45; independent copy |
| St7a | nest ladder: degree-8 rung | 0.45, 0.3, 2/3 | 8 | LB rank 35; independent copy |
| St7b | nest ladder: St7a continued for 150 iterations | 0.45, 0.3, 2/3 | 8 | LB rank 32; independent copy |
| St8a | nest ladder: first degree-6 rung (start p0) | 0.45, 0.3, 2/3 | 6 | LB rank 44; independent copy |
| St8b | nest ladder: second degree-6 rung (start p1) | 0.45, 0.3, 2/3 | 6 | LB rank 43; independent copy |
| St9a | nest ladder: degree-8 rung | 0.42, 0.3, 5/7 | 8 | LB rank 38; independent copy |
| St9b | nest ladder: St9a continued for 150 iterations | 0.42, 0.3, 5/7 | 8 | not on the LB; independent copy |
| St10 | D6 lineage: degree-8 state with free correction channels | 0.45, 0.3, 2/3 | 8 | LB rank 4; independent copy |
| St11a | D6 lineage: degree-6 state with correction channels at degree L | 0.45, 0.3, 2/3 | 6 | LB rank 23; independent copy |
| St11b | D6 lineage: degree-8 state with correction channels at degree L | 0.45, 0.3, 2/3 | 8 | LB rank 6; independent copy |
| St12 | independent route: own state after 400 Gauss-Newton steps | 0.45, 0.3, 2/3 | 6 | independent state; no primary copy |

Table D. Screening of the shortlisted states. I: independently checked; P: primary-reported; S: independent readout
or reassembly of primary samples; --: missing. sigma_u^max and a_max are maxima over the complete registered sets
(shells of both families, the unit ball and the core sets); where only shell or ball values exist they are given in
brackets and the complete value is missing. A bound ">= x P" is the largest primary value over the sets the primary
run evaluated (both shell families and the balls of radius a_eff/2 and a_eff/4 at the vorticity maximum; a_max with
the centre weight), rounded down; it is not the complete value. Check: F, fresh evaluation of the independent route's
own state; R, independent reconstruction of the exported coefficients with its own pressure and residual; S,
independent readout or reassembly of primary samples (not a fresh field evaluation); --, no independent check of this
saved state.
An I entry confirms numerical reproduction of the displayed quantity; it does not state that every validation
guard passed.

| ID | rho_u^max a/b | sigma_u^max | sigma_Om | a_max | Core | Check |
|---|---|---|---|---|---|---|
| St1 | 0.04082/0.04142 I | >= 0.45 P (shells 0.416/0.369 I) | -- | >= 0.83 P (shells 0.449/0.413 I) | worse than St2 | R, shells |
| St2 | 0.0437/0.0433 I | >= 0.43 P (shells 0.418/0.371 I) | 0.421, abs(y) < 32768 I | >= 0.60 P (shells 0.495/0.447 I) | balanced | R |
| St3 | 0.04393/0.04352 I | >= 0.43 P (shells 0.419/0.375 I) | -- | >= 0.58 P (shells 0.488/0.454 I) | doubling passed P | R |
| St4 | 0.04604/0.04630 I | 0.446 I (core sets; shells 0.432/0.400) | 0.406, abs(y) < 1024 I | 0.558 I (core, upper weight 0.798; shells 0.433/0.419) | balanced | R; original pressure guard: 18 of 86 regional checks fail, not resolved |
| St5a | 0.0578/0.0584 P | -- (shells 0.528/0.571 P) | -- | -- (shells 1.31/1.33 P) | balanced | -- |
| St5b | 0.0579/0.0584 P | -- (shells 0.528/0.571 P) | -- | -- (shells 1.31/1.33 P) | balanced | R, diagnostics |
| St6 | 0.0713/0.0722 I | 0.697 I (shells; core sets 0.450, unit ball) | 0.649, abs(y) < 1024 I | 2.85 I (half-offset shell, both weightings; core sets 0.210, upper weight 0.312) | guards I | R |
| St7a | 0.06129/0.06085 I | >= 0.59 P (shells 0.409/0.390 I) | -- | >= 1.03 P (shells 0.738/0.731 I) | doubling passed P | R |
| St7b | 0.05973/0.05939 I | >= 0.58 P (shells 0.406/0.390 I) | -- | >= 1.04 P (shells 0.740/0.692 I) | doubling passed P | R |
| St8a | 0.0669/0.0675 P | -- (shells 0.436/0.412 P) | -- | -- (shells 0.676/0.698 P) | balanced | R, balances |
| St8b | 0.0644/0.0657 P | -- (shells 0.437/0.448 P) | -- | -- (shells 0.957/0.953 P) | balanced | R, balances |
| St9a | 0.06217/0.06746 I | >= 0.67 P (shells 0.499/0.464 I) | -- | >= 1.02 P (shells 0.646/0.661 I) | doubling passed P | R |
| St9b | 0.06154/0.06718 I | >= 0.68 P (shells 0.500/0.451 I) | -- | >= 1.09 P (shells 0.674/0.638 I) | doubling passed P | R |
| St10 | 0.0442/0.0543 P | >= 1.8 P (core) | -- | -- (shells 2.19/1.88 P) | unbalanced | R, Q_sw and far coefficients |
| St11a | 0.0552/0.0748 I | >= 1.99 P (core) | -- | -- (shells 2.01/1.87 P) | unbalanced | R |
| St11b | 0.0456/0.0554 S | >= 1.85 P (core) | -- | -- (shells 2.23/1.87 P) | unbalanced | S; R, tau_F |
| St12 | 0.0574/0.0541 I | 3.13 I | 2.46, abs(y) < 1024 I | -- (shells 5.14/5.22 I) | near-steady (5.3(e)) | F |

The St6 core values are independent (core-set rho_u 0.0649, sigma_u 0.450); on St12 the added core sets give sigma_u
1.896 (independently checked), below the shell value. Values that the primary run ledger lists per ladder level without
a stated domain are not used. Lower bounds (>=) are rounded down; bracketed values are rounded to the nearest digit
shown. Core entries without a status letter are primary readings; for St1 the entry compares primary values of St1
and St2. Under the ordering rule no pair in Table D with a missing entry is ordered.

5.1 Coverage and budgets. See Table C and Table C1 (section 0). Primary runs used degree 6 in the sweep and degrees 2 to
10 in continuations, channels to degree 19 at degree 8, and even azimuthal modes in all but four starts; none of the
ranked states meets Tier S (primary-reported).

5.2 Where the searches end (primary-reported unless marked).
(a) A weak axisymmetric state, the same for every omega (max|U| about 0.03, relative residual of order one).
(b) Numerically near-axisymmetric nonlinear states (relative residual 0.10 to 0.16) at c_l = 0.47, omega = 1,
    omega/c_l = 100/47 and at c_l = 0.49 with omega = 1 and 10 (omega/c_l = 100/49 and 1000/49); they fail the
    registered non-axisymmetry guard (the exact results of section 2, items 7 and 16 (b), do not apply to them).
(c) Stalled non-axisymmetric endpoints: holdout >= 0.54, Sigma_Z about 0 (exact value 1), weak (items 11 and 12).
(d) Starts with Sigma_Z = 1 imposed: 0.35 to 0.44 at degree 6, the best 0.346 with the repaired pressure (far rho_nl
    9.6e7); the first (affine core, c_l = 0.45, omega = 1, omega/c_l = 20/9) was refuted: rho_u^max 0.488, far rho_nl
    2.4e9 from a forbidden rate alpha + 1 term (norm 284), grad P error 3.4e-3 (independently checked).
(e) Free parameters. From the degree-6 state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 one arm drifted to c_l =
    0.4990, omega = 0.2702, omega/c_l = 0.5415 as the holdout rose from 0.0552 to 0.0611 (not ranked); D6-lineage runs
    ended at c_l = 0.4500, omega = 0.3014, omega/c_l = 0.6698 (0.0535, budget-limited) and c_l = 0.4518, omega = 0.368,
    omega/c_l = 0.8145 (0.0538). Free runs from the two Sigma_Z = 1 states at omega = 1 (c_l = 0.45 and 0.47,
    omega/c_l = 20/9 and 100/47; holdouts 0.405 and 0.359) ended at c_l = 0.4498, omega = 0.9015, omega/c_l = 2.004
    (0.424, above its start) and c_l = 0.4707, omega = 0.9965, omega/c_l = 2.117 (0.247). Warm starts at omega = 0.3
    give 0.0613 and 0.0555 at c_l = 0.46 and 0.47 (omega/c_l = 15/23 and 30/47); the jumps to c_l = 0.48 and 0.49
    (omega/c_l = 5/8 and 30/49) lose the basin (0.298 and 0.61), and a finer step from the c_l = 0.47 state to c_l =
    0.48, omega = 0.3, omega/c_l = 5/8 gave 0.0632/0.0897 (tolerance stop, above its start 0.0555).
(f) Sixty degree-2 random starts at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 give 50 nontrivial endpoints, the best
    0.108/0.107, 0.121/0.126 and 0.127/0.133 (single-term ratios 0.9 to 1.3, not ordered); the same protocol gives 0.113
    at c_l = 0.45, omega = 1, omega/c_l = 20/9 and 0.105 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7.

5.3 Branch groups (primary-reported unless marked; not ordered against each other under the ordering rule).
(a) D6 lineage (St10, St11a, St11b; degree-L channels, free channels or closure rows). Degree 8: free-channel state
    0.0442/0.0543 and degree-L state 0.0456/0.0554 (arrays confirmed independently, not by a fresh field evaluation).
    The lineage step from degree 6 is 0.0552/0.0748 to 0.0456/0.0554 (factors 0.83/0.74), and the free-channel state
    continues the 0.0456 state. The degree-8 closure-row rung ended at 0.0568/0.0587, above its degree-8 start
    0.0442/0.0543, and the lineage is floored at degree 8. Continuations at omega = 0.3 and c_l = 0.46, 0.47, 0.48
    (omega/c_l = 15/23, 30/47, 5/8): 0.055 to 0.063 (offset 0.079 to 0.090). Core single-term ratio 1.8 to 2.1 (18 to 21
    times its bound), a_max 1.7 to 2.2, tau_2 2.9e-2 to 3.9e-2. The residual lies between 1/4 and 4 core radii, where
    the core-generated tail has 0.74 to 0.84 of the required norm at 114 to 121 degrees to it (theory route).
(b) Nest ladders (balanced cores; St2 to St5b, St7a to St9b) at c_l = 0.45, omega = 1, omega/c_l = 20/9; c_l = 0.45,
    omega = 0.3, omega/c_l = 2/3; and c_l = 0.42, omega = 0.3, omega/c_l = 5/7: degree-4, 6 and 8 rungs above degree-2
    parents, and second degree-6 starts from other degree-4 states at c_l = 0.45 with omega = 0.3 and 1
    (omega/c_l = 2/3 and 20/9), 0.0644/0.0657 and 0.0516/0.0512. Degree 4: single-term ratios 0.53 to 0.64, a_max 1.3
    to 2.7. First degree-6 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9: single-term ratios 0.43/0.40, a_max
    0.43/0.42, rho_nl^max 0.97, tau_F 0.58. Over all registered sets of this rung, core balls included, the
    single-term ratio is 0.4465 (independent route), 4.46 times the Tier S bound 0.1; the D6-lineage core ratios
    in (a) are 18 to 21 times that bound.
(c) Degree-2 m = 2 states: four nest-ladder states of the shortlist of 2026-10-25T05:41Z with dominant m = 2 tails (one
    at c_l = 0.42, omega = 0.3, omega/c_l = 5/7, 0.1231/0.1160; two at c_l = 0.45, omega = 1, omega/c_l = 20/9; one at
    c_l = 0.45, omega = 0.3, omega/c_l = 2/3). Core eddy energy fractions 0.81 to 0.96, holdout 0.12 to 0.16 on the
    standard family, single-term ratio 1.05 to 1.81 as the standard-family shell maximum and 1.36 to 2.81
    over the complete registered sets; the sampled Q_sw
    is below 1 (0.070 to 0.196); this neither establishes nor excludes Q_sw <= 1.
(d) From-scratch floor states: the endpoints of 5.2 (c), (d) and (f) (0.54 or more, 0.346 to 0.44, 0.105 to 0.127),
    all above (a) and (b).
(e) Independent-route branch at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (independently checked): rho_u^max 0.1133,
    0.0846 and 0.0729/0.0781 at degrees 2, 4 and 6 (Sigma_Z 0.153, 0.2213, 0.351). A stretching-guided degree-4 state
    meets Sigma_Z 0.99994 at rho_u 0.1072, but its ||R_Omega|| is 3.44 ||Omega|| on |y| <= 1024. The fall of rho_u^max
    is denominator-driven: in the core |y| < 1/4 both nonlinear terms are 8.5 to 84 times the self-similar terms and
    nearly cancel. A degree-8 primary-basis fit of the degree-6 state reproduces its holdout (0.07295/0.07806), but its
    sampled single-term maxima move by 10 to 14 per cent under refinement. A primary-basis continuation of a fit (the
    degree-6 D6 state) reads 0.0552/0.0748 (rho_nl 3.18; far limit 0.40 without a rate-(2 alpha + 1) channel).

5.4 Resolution ladders. Nest ladders (primary-reported unless marked; q: step factor, standard/offset):

| c_l, omega, omega/c_l | degree 4 | degree 6 | degree 8 (i) | degree 8 continued | degree 10 (e) | q, 4 to 6 | q, 6 to 8 | q, 8 to 10 (e) |
|---|---|---|---|---|---|---|---|---|
| 0.45, 0.3, 2/3 | 0.0941/0.0878 | 0.0669/0.0675 | 0.0613/0.0609 | 0.0597/0.0594 | 0.05650/0.05645 | 0.711/0.769 | 0.916/0.901 | 0.946/0.950 |
| 0.45, 1, 20/9 | 0.0578/0.0584 (b) | 0.0460/0.0463 | 0.0439/0.0435 | 0.0437/0.0433 | 0.04195/0.04145 | 0.796/0.793 | 0.954/0.940 (d) | 0.961/0.957 |
| 0.42, 0.3, 5/7 | 0.0740/0.0748 | 0.0641/0.0715 | 0.0622/0.0675 | 0.06154/0.06718 (c) | -- | 0.867/0.957 | 0.969/0.943 | -- |

Notes. Factors are computed from unrounded values. (i) Independent readings: 0.04604/0.04630 at degree 6;
0.06129/0.06085, 0.04393/0.04352 and 0.06217/0.06746 at degree 8 by row; the continued state at c_l = 0.45, omega = 1,
omega/c_l = 20/9 reproduced at the displayed precision. (b) Ladder parent: the first degree-4 start, 0.0578/0.0584; the
balance arm (5.6 (a)) starts from a degree-4 state with 0.0579/0.0584 (which of the two degree-4 starts is not recorded;
the second matches). (c) Independent reading at the finest of three rules (primary values agree), 1.0 and 0.4 per cent
below the start. (d) After the channel test (5.6 (c)) the standard-family factor is 0.887 under the 5 per cent rule; the
offset factor stays 0.940. (e) Primary values, reproduced from the saved data by the verifier's reader (not a fresh
evaluation); the factor is taken against the continued degree-8 state. Readings under the rule: Summary and section 8,
item 1. The degree-10 rungs of both c_l = 0.45 branches are read against the continued degree-8 states, which have the
same 4 channel functions, so a floor there is one at 4 channel functions; a 3-iteration degree-10 smoke run is not a
reading. Degree-10 readings (300 iterations each, stopped at the iteration limit with V10 0.0084 at omega = 0.3 and
0.0052 at omega = 1, above the stationarity bound 1e-3; primary-reported): both steps are weak, so both c_l = 0.45
branches are floored at degree 10 with 4 channel functions (operational only), and neither factor lies in the band 0.85
to 0.92 that was set to trigger a degree-10 rung with 8 channel functions, so none was run. At c_l = 0.45, omega = 1,
omega/c_l = 20/9 the velocity, velocity gradient and vorticity of the saved degree-10 state agree with the independent
route's evaluator at 225 points to 1.8e-13 (independently checked); no independent momentum residual norm, full-space
pressure accuracy, full-space vorticity residual norm or core resolution has yet been established for either degree-10
state (pointwise field and derivative controls are recorded separately in the accompanying artifacts; the omega = 1
finite-domain vorticity residual reading below is the exception, and it is not a full-space value). Primary-reported
diagnostics at omega = 0.3 and omega = 1: E_ren -1.719 and -1.570 and H_tot / int |h| -0.876 and -0.699, each within 1.3
per cent of the continued degree-8 value; mismatch m 0.041 and 0.056; the 4-function channel blocks keep last
coefficients 0.13 to 0.59. By the ordering rule applied to saved values (reproduced by the verifier's reader), each
degree-10 state is ranked ahead of its degree-8 source; this is conditional on a common quadrature for sigma_Om (the
holdout angular rules differ between degrees) and on core resolution (the core-resolved flags are primary-reported).
At omega = 1 the common-quadrature condition is now met: the verifier evaluated Omega and R_Omega from the saved
coefficients of the degree-10 state and of St2 on 23 dyadic regions out to |y| < 32768 (standard family; 23170.475 for
the half-offset family) with radial orders 6, 12 and 24 and a 2209-direction angular rule (5425 registered reader checks
pass, and the region integrals were reproduced bitwise by a second reduction of the saved arrays). The reader checks
leave the producing evaluation's own record unchanged: there, four angular-consistency comparisons of R_Omega at
|y| = 32768 failed their 1e-8 criterion (the comparison is uninformative at that radius), and 90 cancellation-sensitive
per-set accuracy measurements were withheld; both are recorded, with a correction note, in the accompanying
artifacts. At order 24, sigma_Om is
0.42132 (degree 10) and 0.42106 (St2), ratio 1.000637 on both families, and each value changes by at most 3.3e-7
relative between orders 12 and 24 (independently checked). These are finite-domain quadrature values of approximate
fields, without a floating-point error bound or a tail estimate; both fail the Tier S bound 1e-1 by a factor of 4.2.
On the standard family about 92 per cent of ||R_Omega||_2^2 lies in 0.25 <= |y| < 1 for both states (0.923 and 0.918),
a region that holds about 65 per cent of ||Omega||_2^2; inside 0.25 <= |y| < 0.5 the regional ratio is 0.548 and 0.568
(independently checked). At omega = 0.3 the common quadrature has not been computed, and core resolution is open at
both rotation rates. At omega = 1 the degree-10 state and St1 are not ranked against each other: St1 is lower on both families
(ratios 0.973/0.999) and its core-set a_max is 1.40 times larger.

Degree-8 diagnostics in table row order (primary-reported unless marked): rho_nl^max 2.68/2.89 (independently
2.67/2.88), 1.115/1.147 and 1.121/1.259 (independently checked); per-family shell maxima of the single-term ratio 0.41
(independently 0.409/0.390), 0.419/0.375 and 0.499/0.464 (independently checked), the complete sigma_u^max being missing
(Table D); shell a_max 0.74, 0.488/0.454 (independently checked) and 0.65/0.66; mismatch m 0.049 and 0.069
(independently checked; 0.40 and 0.35 at degree 6) and 0.210 (theory route, awaiting independent check; 0.34888 at
degree 6, independently checked).

Radial ladder (primary-reported; degree 6 with 16, 24 and 32 radial functions per domain). D6 state with closure rows at
c_l = 0.45, omega = 0.3, omega/c_l = 2/3: 0.0527/0.0695, 0.0528/0.0724, 0.0508/0.0701. First degree-6 nest rung at c_l =
0.45, omega = 1, omega/c_l = 20/9: 0.0460/0.0463, 0.0451/0.0445, 0.0451/0.0451. The holdout changes by about 4.2 per
cent at most, less than the registered 5 per cent threshold; these finite tests do not identify the cause of the
degree-6 floors. The 4-function channel blocks keep last coefficients 0.12 to 0.53 here and on the two degree-8 rungs
(St3, St7a): the far closure is not radially resolved.

Independent ladder at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (independently checked). At the original budgets (5.3
(e)) factors are 0.75 and 0.86; at four times the budgets degrees 4 and 6 reach 0.0708/0.0785 and 0.0581/0.0609, factors
1.19 and 1.25 between the registered bounds 1.15 and 1.5 (inconclusive). The capped degree-6 to degree-4 ratio 0.82/0.78
is in the split band 0.6 to 0.85; over the last two levels rho_u^max fell by a factor 1.55 (1.95 with the capped
degree-6 value), below 2: stalled in the registered sense. Single-term maxima, capped states: 3.04 and 2.52 (offset 3.18
and 2.39). 400 Gauss-Newton steps from the capped degree-6 state gave St12, 0.0574/0.0541 (factors 1.01 and 1.12;
locally floored, an operational label), as a_max rose from 4.40 to 5.14 and the single-term ratio from 2.52 to 3.13.

5.5 Continuations (primary-reported). Up to 150 further iterations lowered the degree-8 holdout by under 1 per cent at
c_l = 0.45, omega = 1, omega/c_l = 20/9 (cost-change stop after 83) and by 2.6 and 2.5 per cent at c_l = 0.45, omega =
0.3, omega/c_l = 2/3 (to the limit, not stationary by the registered test); for the third table row see note (c). All
changes are below the registered 5 per cent threshold, so the factors stand; these finite tests do not rule out
optimizer trapping.

5.6 Structural arms.
(a) Balance arm (St6): weighted rows for E_ren and H_tot / int |h| on a degree-4 nest state at c_l = 0.45, omega = 1,
    omega/c_l = 20/9 (start 0.0579/0.0584). At weight 1 it reduced both defects below 1e-3 (E_ren from -2.10 to -0.0009,
    H_tot / int |h| from -0.83 to -0.0005) at 0.0646/0.0632 by becoming nearly axisymmetric (m != 0 energy fractions
    4.7e-9 and 4.5e-9; not a reading). The guarded run reached 0.0713/0.0722 (independently checked), residual ratios
    1.232/1.235 to the start (inconclusive band 1.2 to 1.5), and reduced both defects far below the registered 0.05
    bounds (independent values E_ren +1.31e-4, H_tot about -3.1e-5 and H_tot / int |h| -7.2e-6, finite-quadrature
    estimates with integration and rounding errors not enclosed; no exact balance is established; the primary display
    -0.0000 of E_ren is a rounding, not a zero measurement, and is not reproduced), via an E_F overshoot to 1.312 at 8
    core radii (theory route) and a reversed leading helicity coefficient (H_F -1.134 to +0.275). Guards
    (independently checked): N_core 0.489, e_core 0.0574, N_F 0.400, e_F 0.0370; rho_nl^max 5.8 (start 3.6;
    primary-reported). The sampled Q_sw is below 1 at 0.9951 (independently checked) and above 1 at 1.10 on the export
    radii (theory route); this neither establishes nor excludes Q_sw <= 1. Lacking a rate-(2 alpha + 1) term it fails
    both far-coefficient conditions at order one (carried 0 against required K_E 0.054 and K_H 0.393).
(b) The same rows at weight 1 elsewhere (primary-reported; optimizer-limited, inconclusive): on the degree-6 D6-lineage
    state it stalled at 0.228/0.244 (4.3 and 3.5 times the start's 0.0527 and 0.0695; E_ren -1.04 to -0.84, H_tot /
    int |h| -0.83 to -0.47); on the first degree-6 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9 it reduced the energy
    defect from E_ren -1.54 to +0.003 but not the helicity defect (-0.71 to -0.19), at 0.448/0.447 (9.7 times the
    start), rho_nl^max 141.
(c) Closure channels. The fit error of the required first correction G[F] falls to 3.9e-15 at degree 6 for a degree-2
    tail and to 7.4e-14 at degree 10 for a degree-4 tail, as degree 2d + 2 requires (section 2, item 18; independently
    checked). With channels the transferred degree-6 state lowered far rho_nl from 3.1 to 0.56 at rho_u^max 0.0552 to
    0.0528 (primary-reported), but its carried coefficient misses the required one by 1.42 times the required norm
    (independently checked). Channel test (St1): 8 instead of 4 radial channel functions on St2 (c_l = 0.45, omega =
    1, omega/c_l = 20/9), 150 iterations to the limit (not stationary by the registered test): 0.04082/0.04142, 6.5
    and 4.4 per cent lower (independently checked; rho_nl^max 0.853/0.930); mismatch 0.067 to 0.0079, far-energy ratio
    -4.94 to +0.243 (right sign, about four times too small), far-helicity ratio 1.051 to 1.005 (primary-reported).
    The core got worse (primary-reported): on the two balls of radius a_eff/2 and a_eff/4 at the vorticity maximum the
    centre-weighted a_max rose from 0.604 to 0.836 and from 0.549 to 0.810 and sigma_u from 0.436 to 0.455 and from
    0.373 to 0.417; at the maximum the strain ratio fell from 0.985 to 0.394 (exact value 1) and tau_2 rose from 0.157
    to 0.233. The sampled Q_sw is below 1 at 0.60; this neither establishes nor excludes Q_sw <= 1. By the ordering
    rule St1 is not ranked ahead of St2; the one measured doubling gained 4 to 7 per cent and fixes no resolution
    limit or rate. Far-closure rows (S11), weight 1 at the end of the two-rung ladder from St4 (independently
    evaluated): mismatch 3.8e-6, far-energy and far-helicity ratios 0.99998 and 0.999998; shell rho_u^max
    0.04526/0.04457 (0.983 and 0.963 times St4); core-set rho_u^max and core-ball a_max 1.10 times St4. The order 18
    versus 27 pressure guard fails on 21 of 86 regions, and 59 reader recomputations on far spheres fail (traced by
    the theory route, and confirmed independently on the saved arrays, to float64 against long-double assembly of a
    residual whose surface rms(U)/rms(R_u) reaches 2e14; an observed arithmetic sensitivity, not an accuracy bound,
    with all 420 budget verdicts unchanged). The state is not resolved under the registered guards, not ordered
    against St4 and not a candidate. At c_l = 0.45, omega = 0.3, omega/c_l = 2/3, weight 1 at the end of the ladder
    from St8a (independently evaluated, reviewed by the theory route): all five registered common guards pass
    (pressure guard 1.8e-8 against 1e-7), so the readings are resolved under the registered guards; shell rho_u^max
    0.05228/0.05368 (5.2 and 5.4 times the Tier S bound), sigma_u^max 0.422/0.403; core-set rho_u^max 0.0758 and
    core-ball a_max 1.19 (centre weight), against the primary-reported 0.98 of St8a, so by the ordering rule it is not
    ranked ahead of St8a (no independent ordering, since St8a has no independent evaluation on the same sets);
    mismatch 2.1e-6, far-energy and far-helicity ratios 1.000001 and 0.999995; truncated E_ren -1.203 and
    H_tot / int |h| -0.891 (exact value 0 for both). The 45 reader failures on far spheres have the same arithmetic
    cause, and on 55 of 105 export spheres the primary main pressure differs from the primary extra and independent
    order-27 pressures by more than 1e-7 of rms(R_u) (largest 5.02e-3; those two agree to within 2.73e-5); all
    failures are retained. The primary route reports a stop on the function-change criterion after an unsafeguarded
    lagged-iteration excursion, so stationarity is not established. Not a candidate.
(d) Swirl and all-m probes (primary-reported). On the D6 lineage (tail mean-swirl energy fraction about 0.84) holding
    the fraction at 0.8 raised the holdout from 0.055 to 0.150. The core-share probe, which raised the non-axisymmetric
    core share of the degree-6 D6 state from 0.155 to 0.25, reached holdout 0.162 with the sampled Q_sw below 1 at 0.10.
    On the second degree-4 nest state at c_l = 0.45, omega = 1, omega/c_l = 20/9 (0.0579/0.0584) an m = 2 boost relaxed
    back in 69 iterations,
    and a 10 per cent m = 1 perturbation with all azimuthal wavenumbers moved the sampled Q_sw from 2.0 (above 1) to
    0.416 (below 1) at 0.0617/0.0597 and tau_F 0.629 (from 0.664), short of its promotion rule (tau_F halved). No
    sampled value here establishes or excludes Q_sw <= 1.
(e) Viscous continuation (section 2, item 29), omega free, from the degree-4 nest state at c_l = 0.45, omega = 1,
    omega/c_l = 20/9: at nu = 3.8e-3 (record checked independently) max|U| fell from 1.14 to 0.034, ending at c_l =
    0.45, omega = 0.2065, omega/c_l = 0.4589, viscous share 0.91 of the residual terms; at nu = 3.8e-2
    (primary-reported) the viscous share was 0.99, ending at c_l = 0.45, omega = 0.533, omega/c_l = 1.184. Both failed.
(f) Square formulations and optimizer tests. Bordered Newton steps on the Galerkin-projected backward defect lowered the
    holdout from 0.1075 to 0.1011 at degree 2 and raised it at degrees 4 and 6 (0.0552 to 0.0707 at degree 6;
    primary-reported). Jacobian condition numbers of the three states (field norm independently checked; raw and
    column-scaled primary-reported):

| Degree and state | raw coefficients | column-scaled | field norm |
|---|---|---|---|
| 2, at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 | 2.3e5 | 1.3e3 | 1.3e3 |
| 4, at c_l = 0.45, omega = 1, omega/c_l = 20/9 | 1.3e8 | 1.3e5 | 2.5e4 |
| 6, at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 | 2.5e13 | 1.5e7 | 3.8e5 |

Registered optimizer test (known degree-6 solution, 2500 L-BFGS iterations; independently checked): forced residual
ratio 0.0126 from the embedded degree-4 start and 2.0e11 and 4.1e11 from two random starts, all above the bound 1e-2, so
optimizer-limited. Fixed-target control: 0.0017 from the embedded start, inside the band 1e-4 to 1e-2, so inconclusive;
random starts stalled at 0.039 and 0.055 (field distances 1.02 and 1.00).
(g) Sphere rows against lambda(r) U (S12; primary-reported, inconclusive). Rows with weight w = 3 penalize the
    projection of the momentum residual onto U on each radial training sphere (5.7 (d)). From the degree-6 nest-ladder
    states at c_l = 0.45, omega = 1, omega/c_l = 20/9 (St4) and at c_l = 0.42, omega = 0.3, omega/c_l = 5/7, both
    stopped at the 300-iteration limit: holdout 0.0460/0.0463 to 0.0417/0.0443 and 0.0641/0.0715 to 0.0566/0.0608,
    with the lambda(r) U share of the training residual 0.748 to 0.305 and 0.793 to 0.397. The unnormalized weighted
    training momentum RMS rose by 23 and 25 per cent while max|U| grew by 27 and 34 per cent (no cause is
    established); the holdout vorticity ratio, the core-set a_max (0.56 to 1.35; 0.92 to 2.12) and the far mismatch m
    rose; rho_nl^max and rho_lin^max fell; the sampled Q_sw fell from about 0.7 to 0.2, still below 1. The changes are
    consistent with redistribution among diagnostics, no mechanism is established, and incomplete optimization remains
    possible. Neither end state is ordered ahead of its start; neither is a candidate.
(h) Parameter path in omega at fixed c_l = 0.45 (S4; primary-reported, not independently evaluated). From the degree-6
    state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (holdout 0.06687/0.06753), with omega changed and held fixed and
    closure rows at weight 1e-3, each arm stopped at the 300-iteration limit and failed the registered plateau test
    (relative cost decrease over the last tenth 0.0206, 0.0274 and 0.154 at omega = 0.1, 0.2 and 0.5, above 1e-3). The
    holdout ended at 0.07437/0.07730 at omega = 0.1 (omega/c_l = 2/9), 0.06887/0.06976 at omega = 0.2
    (omega/c_l = 4/9) and 0.06474/0.06559 at omega = 0.5 (omega/c_l = 10/9), with e_core 0.117, 0.138 and 0.175 (start
    0.142). At omega = 0.5, rho_nl^max rose from 2.75 to 7.05 and the core-set a_max from 0.98 to 1.75. The
    omega = 2.0 (omega/c_l = 40/9) arm from the same start is not a reading: its warm start violated the dilation
    gauge by 24 per cent. From the degree-6 state at c_l = 0.45, omega = 1, omega/c_l = 20/9 (holdout
    0.04604/0.04630), the arm to omega = 0.5 (omega/c_l = 10/9) also failed the plateau test (0.0135) and ended at
    0.05360/0.05781, so the two arms at omega = 0.5 end at different non-stationary states and neither determines a
    value there; the arm to omega = 2.0 (omega/c_l = 40/9) from that state (warm start 4.1 per cent from the gauge)
    also failed the plateau test (0.142) and ended at 0.4979/0.6990, 10.8 and 15.1 times its start, with rho_nl^max
    95.0 and core-set a_max 33.1 (0.56 at the start), keeping its non-axisymmetric content. Under a rule registered on
    2026-10-26 a warm start more than 5 per cent from the gauge is not launched, so the four planned arms in c_l at
    omega = 0.3, to c_l = 0.42, 0.44, 0.46 and 0.48 (omega/c_l = 5/7, 15/22, 15/23 and 5/8), were not launched (warm
    starts -18.6 to +20.0 per cent from the gauge). These are optimization-path observations at degree 6, with no
    floor or trend in omega and no candidate.
(i) Robustness re-solves at c_l = 0.45 (primary-reported; the verifier reproduced the saved arithmetic of every
    reading in this item, with no field evaluation: 41, 78, 337, 349, 131, 77 and 530 checks, all passing except two
    of the 337, which flag near-zero reference values of derivative proxies and change no quoted number). Each variant
    changes one setting, refits its start where needed and is re-solved; a control continues the same state unchanged
    for the same budget. Rule registered before the readings: a variant "returned" if its holdout rho_u^max is within
    1.1 times the control's on both shell families and its worker-grid aligned field difference to the control is at
    most the control's holdout; within 1.1 times but farther is "similar residual, different state"; above 1.1 times
    on either family is "not returned within budget". The field difference is computed on the worker grids and is a
    proxy, not the registered distance of section 3. V10 is read against the registered stationarity bound (absolute
    V10 at most 1e-3); meeting it is an operational label, and stationarity is not established for any run in this
    item. Radial map radius R_0 (section 4) at degree 6, changed from 0.3 to 0.6 and to 0.15, from St4 (omega = 1,
    omega/c_l = 20/9; start distance 0.078) and from St8a (omega = 0.3, omega/c_l = 2/3; start distance 0.055). A
    first re-expansion of all channels to the new R_0 failed as a re-solve (both runs stopped after one accepted step;
    the refitted coefficients were a cancelling combination with norms about 1e4 times the control's) and is not a
    reading; the variants below start from regularized refits (fit errors 0.020 to 0.036). The controls end at
    0.04377/0.04358 (field difference from St4 0.0969) and at 0.06114/0.06095, 0.914 and 0.903 times St8a's (field
    difference 0.1245). At R_0 = 0.6 neither variant returned: from St4 the holdout is 1.401/1.382 times the
    control's, and this is the only run of the R_0 group that meets the stationarity bound (it stopped on the
    function-change criterion after 183 iterations, V10 2.9e-4); from St8a it is 1.390/1.370 times. At R_0 = 0.15 both
    variants reached a similar residual at a different state: holdout 0.823/0.900 and 0.877/0.961 times the control's,
    field differences 0.2636 and 0.3060, 2.7 and 2.5 times the control's own; neither is ranked ahead of its control
    (core-set a_max 1.31 and 1.14 times; core-set sigma_u^max 1.1004 times for the second, above the 1.10 guard). The
    other three variants and both controls stopped at the 300-iteration limit with V10 from 1.3e-3 to 3.6e-2, above
    the bound, so these readings are budget statements. They do not separate R_0 dependence from the start distance
    and the stopping rule, and no mechanism is named. At degree 8 the re-expansion of St2 to another R_0 failed, so
    R_0 sensitivity was not tested there. Far anchor radii at degree 6, from St4 (both variants start from St4 exactly
    embedded and are read against the St4 control above; the far anchors are the far residual rows of the compactified
    basis, not a matching boundary). Dividing the radii by 4 returned the control: both runs stopped at the
    300-iteration limit, the holdout ratios to the control are 1.0000001/0.99999995 and the field difference is about
    3.6e-7. Multiplying them by 4 gave a function-change stop after 23 iterations with V10 -4.5e-6, which meets the
    stationarity bound, at 1.046/1.025 times the control's holdout and a field difference of 0.0989, 1.02 times the
    control's own drift of 0.0969, so this change is not separable from continuation drift. The registered far-field
    proxy is met at 1/4 and not met at 4: both variants keep the holdout and rho_nl^max within a factor 2 of the
    control's, but at 4 the velocity difference on the three far spheres (0.0766, above the control's holdout) and the
    changes of the carried far-energy and far-helicity ratios (10.4 and 0.169, above 0.1) fail its tail condition. The
    proxy does not test the stability of the fitted pressure multipole coefficients, so the corresponding registered
    far-field criterion is not evaluated. The holdout domains differ between the three runs (23 standard shells to
    radius 32768 for the control, 21 to 8192 and 25 to 131072 for the variants), so the comparison is descriptive, not
    a convergence study or an error bound; the maxima occur in the shared shell 0.25 <= |y| < 0.5. Same-budget
    continuation of St2 at degree 8 (omega = 1, omega/c_l = 20/9; the same-budget reference registered for the Stage
    III replication runs from St2): St2 continued unchanged for 150 iterations with the current code (one default-path
    smoke test showed that the pivot option added since St2 was computed leaves this path unchanged, but the original
    St2 record stores no code versions, and equality of the starting coefficients after launch with the saved St2
    state is not established at 1e-6; the same qualifiers apply to the R_0 variants and controls above) stopped at the
    iteration limit, V10 5.3e-3 (St2 2.1e-3). Its holdout is 0.04314/0.04288, 0.988 and 0.990 times St2's, with
    core-set sigma_u^max 1.014, core-set a_max 1.065 and sigma_Om 0.997 times St2's, and its field difference from St2
    is 0.0244, 0.57 times its holdout. By the ordering rule it is ranked ahead of St2: the verifier reproduced the
    five ratios of the ordering record bitwise from the saved results, the two states share the degree and the holdout
    quadrature, and the relation is conditional on the primary-reported core-resolution flags. It continues the same
    branch from St2; it is a distinct saved endpoint. This lowers the recorded objective under this budget; it neither
    establishes nor excludes stationarity of St2. Every variant and control fails the Tier S limits on rho_u^max,
    sigma_u^max and sigma_Om (0.01, 0.1 and 0.1); none is a candidate.
(j) Unrestricted azimuthal wavenumbers (Stage II). Primary route, primary-reported: three degree-6 arms with all
    azimuthal wavenumbers, one start each. At c_l = 0.45, omega = 0.3, omega/c_l = 2/3 the start was the even-class
    degree-6 state with an m = 1 perturbation of 10 per cent of ||U||; at omega = 1, omega/c_l = 20/9 it was the
    degree-4 m = 1 state of 5.6 (d) promoted to degree 6, and the even-class degree-6 state with the same m = 1
    perturbation. All three stopped at the time limit. The holdout ended at 0.06502/0.06595, 0.04819/0.04745 and
    0.04593/0.04622, between 2.8 per cent below and 4.7 per cent above the even-class degree-6 state of the same
    branch (V10 0.045 and 0.0025 for the two arms at omega = 1, above the stationarity bound), and the odd-mode
    velocity fractions ended at 8, 28 and 3.5 per cent of ||U|| respectively (fractions on the finite training grid,
    not whole-space fractions). The values of the arm promoted from degree 4 were reproduced from the saved data by
    the verifier's reader, which also ranks the even-class degree-6 state at omega = 1 ahead of that arm by the
    ordering rule. Fresh all-mode starts at degree 4 (primary-reported; the verifier reproduced the saved readings,
    2056 checks passed, its one failed check being the budget cap below): four parameter points, (c_l, omega) = (0.45,
    0.3), (0.45, 1), (0.42, 0.3) and (0.48, 1), that is omega/c_l = 2/3, 20/9, 5/7 and 25/12, with eight starts per
    point, two seeds from each of four initializer families (random, non-axisymmetric, poloidal and toroidal) fixed
    before launch. All 32 ended at the 300-iteration limit with holdout rho_u^max between 0.25 and 0.84 on both
    families and odd-m energy fractions between 0.13 and 0.96 (training grid, unweighted); none meets the stationarity
    bound (V10 from -0.0062 to 0.73), and all fail Tier S. At the three points with an even-class degree-4 state, the
    promoted start's holdout is 4.0 to 4.5 times that state's on each family (context, not an ordering; independently
    checked from the saved result records). The registered cumulative whole-job cap of 4 GPU-hours for these starts
    was exceeded (18272 s, about 5.08 h), and the starts were not stopped when it was passed; this process violation
    remains recorded, and the readings retained here have the separately stated evidence and review scope, which does
    not retroactively satisfy the cap. The registered filter promoted one start per point to degree 6: a
    poloidal-family start at (0.45, 0.3), non-axisymmetric-family starts at (0.45, 1) and (0.42, 0.3), and a
    toroidal-family start at (0.48, 1). The degree-6 job at (0.48, 1), the one point without an even-class degree-6
    comparator, was stopped before any reading under the registered priority rule of the 10 GPU-hour cumulative cap
    for the four degree-6 jobs, so that point keeps only its degree-4 coverage reading. The degree-6 stage of the
    other three promoted starts (stage (ii)) is primary-reported and reviewed by the lead; the verifier's saved-record
    audit of each terminal record confirmed the recorded values (92 checks confirmed, 0 refuted and 4 registered scope
    items open per record), which is a consistency check of recorded values, not an independent field measurement.
    Each start was continued at degree 6 with a 300-iteration limit and a 7200 s time limit, and all three stopped at
    the time limit, after 259, 261 and 258 iterations at (0.45, 0.3), (0.45, 1) and (0.42, 0.3) respectively. Their
    holdout rho_u^max is 0.1646/0.1648, 0.2268/0.2115 and 0.2436/0.2486, that is 0.464/0.466, 0.897/0.814 and
    0.776/0.829 of the degree-4 values. V10 is 0.104, 0.0219 and 0.0153, and none meets the stationarity bound
    (absolute V10 at most 1e-3). No degree-4 to degree-6 collapse flag is set: N_core, N_F, e_core and e_F changed by
    factors of approximately 1.00 to 1.20. The odd-m energy fractions (training grid, unweighted) are 0.359, 0.767 and
    0.942, against 0.371, 0.791 and 0.951 at degree 4. By the ordering rule the even-class degree-6 state of the same
    point is ahead in all three cases, with holdout ratios 2.462/2.441, 4.925/4.568 and 3.798/3.474; the order is
    conditional on the primary core-resolution flags and the common sigma_Om quadrature. The budgets differ: each
    comparator had a 600-iteration limit and stopped at it, except at (0.45, 0.3), where it stopped at its time limit
    after 413 iterations, and the comparators' code versions are not recorded. One incident, on 2026-10-26, concerns
    the job at (0.42, 0.3). A second process ran on the same device for about 70 s (23:26:31Z to 23:27:42Z, peak
    device memory 43.0 GB). Its effect on this time-limited trajectory, including the number of iterations completed,
    is not established. The four degree-6 jobs used 26027 s of whole-job time by their start and end stamps, including
    the stopped job's 829 s and a cancelled 20 s retry, within the registered cap of 36000 s. None of the three states
    is a candidate. A bounded continuation of the (0.45, 0.3) state ran from 2026-10-27T01:36:12Z to
    06:52:18Z and stopped at its 600-iteration limit (V10 0.0194, so not stationary by the registered test; no collapse
    flag). Its holdout rho_u^max is 0.09767/0.09507 (primary-reported; accepted by the verifier as a coverage reading,
    with no independent field validation), 0.593/0.577 of the stage (ii) end state and 1.461/1.408 times that of the
    even-class degree-6 state at the same point, after 259 + 600 = 859 LM iterations against that state's 413 and time
    limits of 7200 + 19800 s against its 7200 s (it stopped at its time limit; its code versions are not recorded).
    That state is ranked ahead of it by the ordering rule (conditional on the
    primary core flags and the common sigma_Om quadrature); its odd-m energy fraction (training grid, unweighted) is
    0.392. It is not a candidate; it is a coverage reading at this budget, not evidence against odd-mode profiles.
    This continuation was decided after the stage (ii) cost histories had been seen, under a criterion recorded
    before the stage (ii) readings existed (time-limit stop, V10 at least 0.05, no collapse flag). Independent route:
    the eight-step all-mode run at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 and its terminal battery are complete
    (producer 2307 checks, 0 failed; reader 29374 passed, with 55 strict comparisons of a cancelled energy-identity
    defect retained as failures, whose small absolute size is not a pressure enclosure); the step-8 state has
    rho_u^max 0.41029/0.41483 over its domains (radius 4096 for the standard family and 4096 sqrt(2), about 5792.6,
    for the half-offset family). For the present Stage II attempt with the Euler objective, this run and its battery
    are the accepted independent all-mode result; the planned 240-step continuation and its omega = 1 companion were
    not released, so a broader Stage II independent all-mode arm with several starts and parameter points was not
    executed. The independent route's Stage I all-mode runs at c_l = 0.45, omega = 0.3 and 1 (omega/c_l = 2/3 and
    20/9) are separate coverage records, with their guard failures retained: a 40-step-cap experiment with eight
    starts (four completed, holdout rho_u^max 0.42 to 0.70; four stopped at the rotation-phase normalization step), a
    16-step integration in the physical normalization from eight reused starts (six completed, holdout 0.43 to 0.70;
    two stopped at the 1e-12 tail-mass guard) and a bounded continuation of three of these runs, of which two reached
    step 96 (holdout 0.399 and 0.758) and the third stopped after step 85 on a mass-admission failure (holdout 0.608).
    The physical-normalization integration and its bounded continuation reuse the eight starts of the 40-step-cap
    experiment and add no distinct start. None of the three experiments gives a candidate. These arms give no evidence
    that odd modes lower the residual materially. They are coverage readings at their budgets and do not exclude
    odd-mode states.

5.7 Failure modes. Each is a necessary condition without threshold (section 3).
(a) Whole-space balances. E_ren < 0 on all eleven momentum-only primary exports and H_tot < 0 on ten (theory route).
    Independently checked (H_tot, H_tot / int |h|, E_ren): degree-4 nest state at c_l = 0.45, omega = 1, omega/c_l =
    20/9: -3.8537661, -0.827, -2.1003151; first and second degree-6 nest starts there: -4.53483, -0.71073, -1.54296
    and -4.0824, -0.7884, -1.9222; first and second degree-6 nest starts at c_l = 0.45, omega = 0.3, omega/c_l =
    2/3: -4.0275, -0.8879, -1.7369 and +4.2915, +0.8915, -2.0682; degree-6 rung at c_l = 0.42, omega = 0.3, omega/c_l =
    5/7: -3.0270, -0.7892, -3.8952. Theory route: E_ren -1.45 to -0.98 on the D6 lineage, -1.58 to -3.94 on the five
    degree-8 nest exports and -4.53 on the degree-4 nest state at c_l = 0.42, omega = 0.3, omega/c_l = 5/7. Ten
    independent-route states have E_ren < 0 (6.4), but a later one at c_l = 0.45, omega = 0.3, omega/c_l = 2/3, started
    at H_tot 1.9e-8, ends after 400 steps without balance rows at H_tot -5.701 and E_ren +1.399 (rho_u 0.423/0.420
    against 0.0821/0.0922 from the plain start; independently checked). The one positive H_tot (omega > 0 throughout)
    shows that its sign belongs to the states. The degree-6 run with balance rows (5.6 (b)) has E_ren +0.003
    (primary-reported) and the balance arm E_ren +1.31e-4 (independent finite-quadrature estimate; no exact balance).
(b) First far coefficient (exact value 1; independently checked on fifteen states). Energy ratio on the eleven with the
    term: -3.25, -15.2, -434.479 and -2835.41 (D6 lineage); -8.98, +19.08, -32.6 and +29.74 (degree-6 nest starts);
    5.38178 (degree 6 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7); -0.27909 and -5.18473 (degree 8 at c_l = 0.45 with
    omega = 0.3 and 1, omega/c_l = 2/3 and 20/9). Helicity ratio on the same states: 0.18233 to 4.24159 (1.27644 and
    1.05365 on the two degree-8 rungs). The energy ratio is 0 on the four without the term (a third degree-6 D6 state,
    both degree-4 nest states, the balance-arm state). At degree 8 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7 the
    ratios are 3.876 and 1.214 (theory route, awaiting independent check). m is 0.049 to 4.4 and c 0.0005 to 0.05456
    (0.0239 on St7a and 0.0077 on St3), so the energy ratio can magnify a vector defect by 1/c.
(c) Head flux on balls (ratio to the requirement, exact value 1; independently checked). Degree-4 nest state at c_l =
    0.45, omega = 1, omega/c_l = 20/9: 0.873, 0.682, 0.270, 0.048, 0.013 at 1/4, 1/2, 1, 2, 4 core radii, opposite sign
    at 8 and 16; first degree-6 rungs at c_l = 0.45 with omega = 0.3 and 1 (omega/c_l = 2/3 and 20/9): 0.892 and 0.848
    at 1/4 core radius, 0.457 and 0.217 at the core radius. Theory route on nine exports: 0.81 to 0.94 at 1/4 core
    radius and at most 0.46 in magnitude beyond one core radius. E_F approaches 1 from below on the D6-lineage and
    degree-4 nest states (theory route).
(d) Residual along U (theory route). A radial multiple lambda(r) U removes 68 to 79 per cent of int |R_u|^2 on the eight
    nest and balance-arm exports and 15 to 24 per cent on the D6 lineage; on the first degree-6 rung at c_l = 0.45,
    omega = 1, omega/c_l = 20/9 the radial share is 0.7274 (independently checked).
(e) Origin Taylor residuals (exact value 0) are nonzero on every state where they were computed (5.3 (a), (b) and
    (e)), with tau_2 0.60 and 0.16 on the degree-8 rungs at c_l = 0.45 with omega = 0.3 and 1 (omega/c_l = 2/3 and
    20/9). On the selected degree-10 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9 the axial vorticity residual at
    the origin is enclosed away from zero in exact arithmetic (6.9 (s)).
(f) Swirl ratio. All values are sampled maxima without one-sided bounds; none establishes or excludes Q_sw <= 1. The
    sampled Q_sw is above 1 on: the degree-4 nest states, 2.0009 at c_l = 0.45, omega = 1, omega/c_l = 20/9
    (independently checked) and 2.63 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7 (primary-reported); three degree-2 nest
    states at c_l = 0.45, omega = 1, omega/c_l = 20/9, 1.22 to 1.35 (primary-reported); the second degree-6 start there,
    1.1829 (independently checked). The sampled Q_sw is below 1 on (independently checked unless marked): the D6
    lineage, 0.1494 and 0.2848, others 0.15 to 0.44 (primary-reported); the degree-6 starts at c_l = 0.45, omega = 0.3,
    omega/c_l = 2/3, 0.4915 and 0.385 (primary-reported); the first degree-6 rung at c_l = 0.45, omega = 1, omega/c_l =
    20/9, 0.669; degrees 6 and 8 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7, 0.7314 and 0.530 (primary-reported);
    degree 8 at c_l = 0.45 with omega = 0.3 and 1 (omega/c_l = 2/3 and 20/9), 0.3871 (0.366 continued, primary-reported)
    and 0.6427. Along backward trajectories (theory route) the eddy part Gamma^S of the mean swirl Gamma_0 is
    anti-aligned with Gamma_0 on the computed nest states (the residual carries their mean swirl), aligned only outside
    the core on the degree-6 D6 states (cosine 0.61 to 0.76) and on all four bands on the balance-arm state (+0.74
    to +0.94), and anti-aligned on one degree-8 D6 state (-0.75 to -0.78).

## 6. Validation

6.1 Routes and exchange. The primary and independent routes share no code. A state passes between them in the exchange
format of 4.5; the receiver rebuilds the field from the basis description alone and computes the full-space pressure and
residual with its own code. A route's values for its own states count only from a fresh holdout.

6.2 Agreement. The first exchanged primary state was rebuilt to 1.5e-15 relative in U, DU and Omega (5.2 (d)); in
reverse, the primary route rebuilt the independent degree-2 state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 to 2.2e-14
and after a basis fit (error 6e-5) obtained rho_u^max 0.11328 against 0.11329. On the independently re-read degree-8
states strict reassembly at 1e-11 fails in 52, 59 and 60 of 2341 far-shell scalars on the rungs (table row order of
5.4), and in 54 and 63 on the continuations at c_l = 0.45, omega = 1, omega/c_l = 20/9 and c_l = 0.42, omega = 0.3,
omega/c_l = 5/7 (largest 8.9e-9), all on shells 15 to 18, traced to cancellation of the linear term rebuilt in wider
arithmetic (with the saved linear term it agrees to 1.6e-15); the failures are retained. The reflection omega to -omega
gives zero difference on nine exports (theory route, with the independent route's evaluator).

6.3 Pressure. The independent ray-integral pressure agrees with the primary Poisson solution at sampled points to 6e-8
and 2.8e-6. On the first degree-6 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9 the strict regional guard fails in
18 of 86 regions (up to 3.3e-6, guard 1e-7); in four re-tested regions source orders 36 and 48 agree to 8.0e-15, so
the order-18 rule carries the failure; the other 82 were not re-tested. In the separate five-export comparison the
independent route's radial Green pressure (4.4), at 224 points on each of five degree-8 exports, passes 243 of 270
checks at 1e-11: 12 of 54 fail on both the rung and the continuation at c_l = 0.45, omega = 1, omega/c_l = 20/9
(largest 4.6e-9) and 3 of 54 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7 (2.0e-11). On the continuation at c_l = 0.45,
omega = 1, omega/c_l = 20/9, P and grad P differ by 2.7e-11 and 9.2e-10 in global relative L2, on far spheres mostly
via a spurious monopole of the 60-node primary source (about -4.09e-12, 1.36e-12 of the absolute radial quadrature
sum; absent from the exact source), whose pressure gradient decays like r^-2 (the pressure itself like r^-1). With 60,
120 and 180 nodes single-sphere rho_u and rho_nl change by at most 1.3e-11 and 3.4e-6, but the routes differ by a
factor 3 on the monopole change between 120 and 180 nodes, so its amplitude is unresolved (no correction applied). At
c_l = 0.45, omega = 0.3, omega/c_l = 2/3 doubling the source nodes changes shell ratios by at most 1.95e-7 relative.
No holdout reading changes; failures are retained. On a fixed degree-8 state of the independent route at c_l = 0.45,
omega = 0.3, omega/c_l = 2/3, a full-space pressure with unconstrained low source moments, at 50 and 100 digits with a
separate 140-digit reader, is stable to 2.8e-4 relative between Gauss orders 12 and 18 per panel at r <= 0.3 but
changes by 0.05 to 1.65 relative at r = 4915.2 = 2^14 R_0, while the angular and precision repeats agree to 6.6e-57
and 1.7e-41 relative; 38 radial comparisons fail the prospective 1e-3 threshold and are retained (a finite sensitivity
test of one state, not an error bound; the production pressure was not tested).

6.4 Balances (independently checked). Capped degree-4 independent state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3:
E_ren = -0.7896266673066, beta_0 E_ren = +0.0987; quadrature doubling changes E_ren by 5.8e-11, the rational bound on
the omitted energy beyond 2^40 is 4.6e-10, and the ball identity (a check of fields and quadratures only) gives
0.0987033334568816 against 0.0987033334568821. Nine other independent-route states have E_ren from -1.02124 to -0.5192;
seven have H_tot -3.773 to -10.536 and ratios -0.625 to -0.995. On the primary exports the omitted energy beyond 2^28 is
bounded by 1.6e-9 to 2.02e-6 and the helicity by 1.3e-17 to 2.35e-14. None of these encloses a finite-ball quantity. On
a degree-8 state of the independent route at c_l = 0.45, omega = 0.3, omega/c_l = 2/3, the vorticity-amplitude identity
of section 2, item 36, was evaluated for 18 bins of a = |Omega| in 19 balls (independently computed; the classification
was recomputed by the theory route from the stored rows). Eight bin and ball pairs, the bins [16, 64] and [32, 64] in
balls of radius 0.0078 to 0.0625 (0.0055 to 0.0442 on the half-offset family), meet the citation rule: on both families
the two sides agree within 10 per cent and change by at most 1 per cent between the two finest rules. On them the two
sides agree to between 2.3e-15 and about 2.81e-4 relative, and the implied lower bounds for ||R_Omega||_(L2) on the bin
support, 0.0017 to 0.252 in the saved gauge, are quadrature estimates, not certified bounds. The other 242 pairs active
at the finest quadrature rule do not meet the citation rule, and all 4157 failed reader checks are retained.

6.5 Tail generation (independently checked; exact value 0). tau_F 1.99505979724, 2.3184 and 2.4564 on the capped
degree-4 and degree-6 and Gauss-Newton independent states (delta_G 0.0264, 0.0167, 0.0510 on the core ball, 0.4287,
0.767, 0.853 at the vorticity maximum); 0.9183 on St11b, 0.66380 on the degree-4 nest state at c_l = 0.45, omega = 1,
omega/c_l = 20/9 (delta_G 0.0057 and 0.336) and 0.635 on St6; theory route 0.898 to 0.968 on the D6 lineage.

6.6 Defects found by validation, all before any candidate was offered: (a) primary grad P lost accuracy off the
quadrature panel edges (3.4e-3; panels now split at each evaluation radius); (b) the primary far field carried a
forbidden rate alpha + 1 term (norm 284; removed by linear conditions, confirmed independently); (c) the primary
free-parameter Jacobian omitted the pressure-kernel derivatives (fixed; search only); (d) a normalization and weighting
defect let 30 of 37 early starts collapse to U = 0 (excluded); (e) an early primary pressure solver mis-resolved twisted
sources (grad P errors 1e-3 to 1e-1; earlier rankings unused); (f) an early dilation gauge omitted the twist energy of
the poloidal tail; (g) both routes carried the first nonlinear coefficient with too few angular degrees (5.6 (c)); (h)
the independent route's first stretching integrals were under-resolved (Sigma_Z 1.031 to 0.99994 and 0.245 to 0.2213 on
refinement); (i) a primary weighting by the nonlinear terms alone was lowered by inflating the core (runs unused); (j)
the theory route's pointwise swirl ratio 0.83 on St11b was wrong (independently 0.768).

6.7 Stage III replication: perturbation response (primary route; the verifier checked the saved records, the distance
arithmetic and the registered reading; no field was re-evaluated independently). At c_l = 0.45, omega = 1, omega/c_l
= 20/9 (degree 8, even class), three random perturbations of St2 of relative size 0.01, 0.03 and 0.1 (training-grid
quadrature L2 norm of U; 0.0055, 0.0158 and 0.0606 in the unweighted sampled-holdout norm; seeds fixed in advance)
were each continued for 150 iterations, the budget of the same-budget continuation of St2 (5.6 (i)), which serves as
the control (holdout 0.04314/0.04288; its own field difference from St2 is 0.0244). All three stopped at the
iteration limit with V10 0.0055, 0.0057 and 0.105, so none meets the stationarity diagnostic. The field distance used
here is the maximum over the holdout shells and far spheres of the shell RMS ratio of U after an estimated best
rotation (an estimated minimum over the rotation angle, not a certified one); it is a proxy on that domain, not the
acceptance norm of section 3. It was 0.0152, 0.0489 and 0.160 from St2 at the start and 0.0023, 0.0087 and 0.212 from
the control at the end. The holdout ratios to the control are 1.001/1.001, 0.995/0.995 and 4.19/4.30. By the reading
registered before these runs, the two smaller perturbations returned within the residual level (holdout at most 1.1
times the control's on both families, and end distance below the control's holdout 0.0431), and the largest did not
return within this budget, so its sensitivity cannot be separated from its start distance. All three reached the
150-iteration limit with finite saved diagnostics, so the early-stop and finiteness failure tests did not fire. The
registered maximum-velocity doubling test remains open in the independent audit: the available start and end maxima
use different sample grids. The return classification above is conditional on this unverified failure screen; this
does not assert that any run doubled. The squared tail norm differed from its normalized value 1 by 7.27e-9, 6.23e-9
and 2.11e-7 (sizes 0.01, 0.03 and 0.1) in the optimizer's end state and by 2.22e-16, 4.44e-16 and 1.11e-16 after the
end-state projection; the projection factor was not saved, so its distance from one is open. By the ordering rule the
0.03 case is ranked ahead of the control and the control ahead of the other two (conditional on the primary core
flags and the common sigma_Om quadrature); this changes no selection. This is a local reading at 150 iterations from
three starts on one branch. It establishes no basin size, uniqueness, convergence or stability, and all four states
fail Tier S.

The degree-10 rung of selection (1) of section 7, at the same point, was read by the same rule as a late result: its
reading ended at 06:07:30 UTC, after the 06:00 UTC limit that the campaign lead had set for it, although every input
of the classification below was written by 01:26:29 UTC (primary route; the campaign lead reviewed the record, and
the verifier checked its saved scalars, hashes and classification arithmetic; no field was re-evaluated
independently). One random perturbation of the rung of relative size 0.01 (0.0054 in the unweighted sampled-holdout
norm; seed fixed in advance) and the unchanged continuation of the rung as control were each run for 150 iterations,
the same budget, and both stopped at the iteration limit. The holdout was 0.04124/0.04099 for the perturbed run and
0.04124/0.04097 for the control (holdout ratios to the control 1.0002/1.0004), and V10 was 0.0041 for the perturbed
run and 0.0042 for the control, so neither meets the stationarity diagnostic. In the field distance above, the
perturbed start was 0.0145 from the rung, and the two end states were 0.0012 apart, below the control's holdout
0.0412, so by the registered reading the perturbation returned within the residual level. The control's own field
difference from the rung is 0.0208. The perturbed run's difference from its own start was not computed: its
comparison reader wrote no output in about 4.4 hours and was stopped by order of the campaign lead; that value
decides no part of the reading. The early-stop and finiteness tests did not fire on the saved records (the early-stop
reading rests on the solver source bound to the runs, since the executed code and the history of accepted steps were
not captured independently; finiteness refers to the saved values). The registered maximum-velocity doubling test did
not fire on the saved sampled values: the maximum went from 1.2634 to 1.274 in the perturbed run and from 1.2613 to
1.275 in the control (the start and end values use different sample grids); neither value is a certified supremum. No
ordering of the two states is drawn from this reading. It is a local reading at 150 iterations from one start; it
establishes no basin size, uniqueness, convergence or stability, and both states fail Tier S.

6.8 Stage III replication: discretization, truncation, weight and odd-mode changes (primary route; the verifier
checked the saved records, the distance arithmetic and the registered reading; no field was re-evaluated
independently). At c_l = 0.45, omega = 1, omega/c_l = 20/9 (degree 8), four further runs repeated the continuation of
St2 with one change each: the radial collocation density (a), the far-field truncation order (b) and the far-anchor
weight (c), each with the control's 150-iteration budget, and an odd-mode start (d), time-limited. Each was read
against the same-budget continuation of St2 (5.6 (i)) as the control (holdout 0.04314/0.04288), with the field
distance of 6.7; (a) to (c) also use its reading rule. None meets the stationarity diagnostic (V10 at most 1e-3), and
all fail Tier S.
(a) Radial collocation density, 60 to 90 training nodes. The start is the St2 coefficient file itself (distance 0
    before the gauge projection, by construction); the projection changed it by 9.16e-16 relative, and no start
    comparison was run. The run stopped at the 150-iteration limit with V10 0.0046. Its holdout is 0.04331/0.04324,
    0.4 and 0.8 per cent above the control's, and its end state is 0.0048 from the control's end state, 0.111 of the
    bound 0.04314, so by the rule of 6.7 it returned within the residual level. The ratio of the last coefficient to
    the block maximum, end state over control end state, changed by +5.741 and -4.234 per cent in the two blocks of
    20 radial coefficients and by -1.051, +0.975 and -3.847 per cent in the three blocks of 4, so the five ratios
    changed by less than 6 per cent in magnitude. This is a decay diagnostic, not a truncation error estimate; full
    radial convergence stays open. The ordering tool places the control ahead (ratios 1.004, 1.008, 0.998, 1.012 and
    1.003; the core-set sigma_u ratio 0.998 is below 1); that is the tool output only. The terminal cost, the
    training momentum residual and the rotation-content diagnostic are weighted by the training nodes, which differ
    between 90 and 60 radial nodes, so they are not compared.
(b) Far-field truncation order, 4 to 6 channel functions in each carried channel (channel degrees unchanged). The
    start is St2 embedded into the larger channels with the new coefficients exactly zero; its projected start cost
    blocks equal the control's to 1.6e-16 relative (one unit in the last place each), and no start distance was
    measured. The run stopped by the relative cost-decrease test after 148 iterations, with V10 0.0048. The holdout
    changed by -3.0 and +1.5 per cent on the two families, inside the registered factor 1.1 on both but with opposite
    signs, and the end state is 0.0429 from the control's end state, 0.994 of the bound 0.04314 (0.6 per cent inside
    it). So by the rule of 6.7 it returned within the residual level, with that qualification. The carried closure
    quantities changed (m 0.0624 to 0.0234; K_E ratio -4.5 to -1.3, sign unchanged): the carried far-field
    coefficients depend on the truncation order, measured, not explained. The ordering tool reports the pair as not
    ordered (holdout 0.970/1.015, core-set sigma_u 0.952, sigma_Om 0.992, core-set a_max 0.984); the a_max ratio
    compares maxima in different centre sets (quarter-ball for this run, half-ball for the control). This is not a
    convergence statement.
(c) Far-anchor weight, 1 to 3. The start is the St2 coefficient file itself, and no start comparison was run.
    Tripling the far-anchor weight changed the projected start cost by 1.7e-9 relative. The run stopped at the
    150-iteration limit with V10 0.0053. The end state is 2.1e-9 from the control's end state in the field distance
    of 6.7, and its holdout agrees with the control's to 1.6e-9 relative, so by the rule of 6.7 it returned within
    the residual level. The holdout pair, the core-set sigma_u and a_max, the tail mismatch m and the K_E and K_H
    identity ratios agree with the control's to less than 1.1e-7 relative (largest: the K_E ratio, 1.01e-7). The
    rotation-content diagnostic (0.6376 against 0.6397) uses the far weight in its node weights, so the two values
    use different measures and are not compared; the training costs are not compared for the same reason. The
    ordering tool's five ratios are within 1.6e-9 of 1, so its printed relation carries no ordering information and
    is not cited. This change has almost no leverage at this state and says nothing about shell weights in general.
(d) Odd-mode start. In the basis with all azimuthal wavenumbers (192 odd of 387 modes), the run started from St2 plus
    a kernel-projected odd-wavenumber perturbation of registered size 0.1 in the training-grid quadrature norm of U
    (seed fixed in advance). The measured unweighted odd fraction of U at the start is 0.0934; the two measures are
    not equated, and the training-grid norm stays open. The start is 0.148 from St2 in the field distance of 6.7. The
    run was time-limited at 119 iterations (14400 s solver limit, against the control's 150 iterations under 9000 s);
    processes of another project were seen on its GPU from 07:23:08 to 07:57:43 UTC on 27 October, with unknown
    effect on the iteration count and elapsed time, so iteration counts and times are not compared at face value. V10
    is 0.0060. The holdout is 0.04371/0.04338, 1.3 and 1.2 per cent above the even-class control's, and the training
    momentum residual is 0.0866 against 0.0860. The odd part fell by a factor 3.5 in amplitude (12 in energy) and is
    retained at the time limit at 2.7 per cent of U in the same unweighted training-grid measure (0.07 per cent of
    the energy). The end state is 0.0447 from the control's end state, 0.30 of its start distance; the rule of 6.7 is
    not the registered reading of this run, which is a scope record only. No odd-mode state with a lower residual was
    found at this budget, from one start, at fixed degree 8, time-limited. Odd-mode states are not excluded.

6.9 Stage III verification of the selected state: the independent pressure chain and the other Stage III checks
(status at 2026-10-28T17:27:01Z; decisions of the campaign lead to 2026-10-28T17:27:01Z; every statement below rests
on a dated lead note or review). The verifier runs one registered finite pressure validation of selection (1) of
section 7, the degree-10 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9, with R_0 = 0.3; its registration
(5a37faf9) and freeze (d3bcd800) are among the accompanying artifacts. The pressure is evaluated on
a local block of 32 targets including the origin, with four models (constrained and unconstrained, at partial order
112 and 160), from fixed source legs run in sequence. Each leg has a source run, a snapshot reader and a matrix
reader of the saved source, then a pressure run and a pressure reader of the saved pressure. Items (a) to (j), all of
the independent route, cover legs R2, R3 and R4 and the controls the run depends on; items (k) to (s) are the other
Stage III checks, each of the route named in it. Leg R2 and the first R3 attempt ((a) to (d)), the review of the
first wrapper version in (e), the Group B release in (i), the source acceptance in (j) and the launch in (m) took
place before the Stage III start at 2026-10-27T17:09:12Z, at the times given; they are reported here as parts of the
same verification. Times are UTC on 27 October 2026 unless another day is named. Charges are in core-seconds and
GPU-seconds of the verifier's production budget, except those marked recovery, which come from its separate recovery
reserve. No result of the readers of the second R3 attempt, the R3 pressure, the R4 leg, the moments reducer, the
comparisons reducer or the test in (n) is cited before its lead review; (h) uses the progress records of the second
R3 attempt only for disk planning. Nothing here is a pressure accuracy statement, a momentum norm of the registered
specification, a candidate validation or evidence of an Euler solution, and nothing here changes the label, which
stays C.
(a) Source R2. The R2 source leg (finite order 96, exterior order 192, 27 panels) was launched at 14:48:04.160Z and
    completed at 15:54:49.066960Z with return code 0, after 4005.5307916859165 s of its 8100 s watch, with 2978
    events and 2977 fresh rows, none cached. It was accepted as a completed fixed source leg with its saved
    diagnostics; it is not a pressure or Euler result. Charge: 4005.531444699038 core-seconds and the same number of
    GPU-seconds, against a reservation of 8100 core-seconds and 8100 GPU-seconds; the unused 4094.468555300962 s
    returned.
(b) Readers of the R2 source. The snapshot reader and the matrix reader of the saved R2 source ran once each, from
    16:03:26.98Z to 16:03:32.35Z and from 16:03:35.48Z to 16:03:35.84Z, with exit 0 and exactly the counts that the
    lead's dry runs gave on the same files: 3259 CONFIRMED / 0 REFUTED and 256 CONFIRMED / 0 REFUTED. They were
    accepted as completed finite saved-data checks, in the scope of saved source consistency only. Charge: 30
    recovery core-seconds each.
(c) Pressure R2. The pressure run on the R2 source was launched at 16:12:25.68Z and completed at 16:12:42.66Z with
    return code 0, after 17.484618240967393 s of its 1800 s watch. It was first accepted as a completed run, not yet
    usable. Charge: 17.48530997429043 core-seconds and 0 GPU-seconds; the unused 1782.51469002570957 core-seconds
    returned. Its pressure reader started at 16:19:33.80Z and exited 0 in 0.96 s with 332 CONFIRMED / 0 REFUTED,
    exactly the expected count (charge: 30 recovery core-seconds). The lead then accepted R2 as a completed,
    internally consistent pressure result on the 32 local targets (the campaign lead's final review). All 32 targets, among
    them the origin, and all four models are present and finite. The four models agree with each other to at most
    6.7e-15 in P and 1.5e-14 in a grad P component; that agreement is sensitivity to the two model choices only, not
    an error estimate. P at the origin is -0.648556. In the accepted scope this gives no pressure accuracy, no
    moment-study verdict, no source refinement verdict, no eligibility of the constrained models, no independent
    Newton agreement, no domain momentum norm of the registered specification, no exact profile and no label A. The
    comparison of R2 with the earlier leg R1 is reported in (r), as a difference of saved pressure models only.
(d) Source R3, attempt 1: FAILED. Launched at 16:26:43Z on one CPU and one GPU, it failed at
    16:36:20Z by an infrastructure fault. The watcher's 30 s disk sample ran du -s over the verifier's working tree,
    and du exited 1 because a temporary row file (a .part file) disappeared through the writer's os.replace during
    the traversal. The watcher then stopped its own worker (worker elapsed 575.86 s). No scientific result exists.
    This was a traversal and rename race, not a capacity breach: the last disk sample, at 16:35:50Z, was within the
    disk projection limit. The full reservation of 8400 core-seconds and 8400 GPU-seconds stays charged, with no
    refund; the 577.5811080466956 s observed by the accounting script is recorded next to it. It was not retried
    unchanged. The source runs up to this failure had recorded 340 good 30 s disk samples and this 1 failure; if the
    per-sample failure rate were a constant 1 in 341, an unchanged watcher would survive an 8400 s run with
    probability about 0.44 and the 19800 s R4 source with probability about 0.14, a rough estimate from one event.
(e) Recovery by a bounded du wrapper. No registered or frozen file was changed. The recovery adds one executable
    named du, placed first in PATH, which runs the system du with unchanged arguments and passes its output and exit
    status through unchanged, except that when du exits 1 and every error line reports a vanished path, it waits 0.2
    s and runs du again, at most three runs in total. After a third such failure the last result passes through, so
    the watcher still fails closed. The wrapper ends within 25 s, inside the callers' 30 s timeout. Version v3 was
    NOT ACCEPTED: it started the system du with the full program path as argv[0], so du's error lines began with that
    path and never matched the vanish pattern, which needs each line to start with "du: cannot access"; it would
    never have retried a real race. In the lead's probe, which replicated the verifier's churn writer, a byte copy of
    v3 failed 56 of 200 calls with 0 retries (plain du failed 6 of 200), and a copy changed only in argv[0] failed 0
    of 200 calls with 51 retries and a largest wall time of 0.464 s (plain du failed 8 of 200). Version v4
    (e84b82c7, in the accompanying artifacts), byte-identical to that probed copy, was accepted. Its control PASSED and was accepted: it ran on one
    CPU from 17:29:36Z to 17:30:38Z, with exit 0 and 27 CONFIRMED / 0 failed / 0 inconclusive over 447 calls in the
    designed order. All 221 wrapper calls on real trees exited 0 (largest wall time 1.021237995941192 s), while the
    paired plain du calls under the same churn failed 14 times, 7 on the scratch tree and 7 on the verifier's whole
    working tree. Every vanished path lay under the control's own temporary directory. The four designed failure
    cases (a missing path, a persistent vanish stub, a permission stub and a sleep stub) failed closed within 25 s;
    the sleep stub exited 124 after 24.039830587804317 s. The verifier's standing disk guard, which stops its
    eligible workers once its total disk use reaches 24e9 bytes, was paused for at most 62.978129 s during the
    control. In the accepted scope this is a finite disk-accounting software control in which one writer churned two
    trees on one filesystem for about 62 s; it gives no failure-rate bound and says nothing about pressure. Charge:
    300 recovery core-seconds. The standing disk guard was then replaced: the old process was ended by SIGTERM at
    17:44:22.258649Z, and the unchanged guard program was started with an environment that differs from the old one
    only in PATH, with the wrapper directory first (shown by hash), so that its du resolves to the wrapper. The
    replacement was accepted. The guard's own retry count is not observable, because the guard captures and discards
    the wrapper's retry notices on a successful scan; retry lines counted in the worker and watcher logs are emitted
    counts, not complete counts.
(f) Source R3, attempt 2. It was released for one attempt, with attempt 1's argv apart from the
    permit name and with the wrapper directory added at the front of PATH, to launch by 22:00Z and complete by
    2026-10-28T00:21Z. A first admission at 17:54:00Z was blocked before any permit or launch, because its check for
    other processes matched the primary route's agent session, whose processes are not numerical processes; the check
    was narrowed in a dated record before the repeat. The narrowed check's code is not bound by hash, and the lead
    accepted the repeat on the lead's own process listings. The run was launched at 17:55:00.157Z on one CPU and one
    GPU at nice 19, and the launch was accepted. It completed at 19:02:37Z, after 4057.39 s of its 8400 s watch, with
    return code 0 and no failure record. It wrote 3073 source rows (3072 requests and the leading row), all computed
    fresh and none reused, under one new cache identity; the 14508 earlier cache files of three directories and the
    926 files of attempt 1 rehash unchanged. Peak resident memory was 2277429248 bytes (the whole-run maximum
    reported by the operating system) and observed GPU memory 847249408 bytes, below the 8 GiB and 2 GiB caps; one
    resident-memory sample is missing, and its cause (a sample taken after the worker had exited) is plausible, not
    shown. The worker log and the watcher log, which received the watcher's standard output and standard error, are
    empty, so no wrapper retry line was emitted; the guard's own retries are not observable. The run directory grew
    248090624 bytes, below the 313786368 bytes of the size model applied to this run. The lead accepted the result at
    19:08:08Z as fixed finite source data of leg R3 only; it is not a pressure result, a pressure accuracy statement,
    a source refinement verdict, a momentum norm of the registered specification or evidence of an Euler solution,
    and the content of the source arrays is checked only by the two readers. Charge: 4057.390503915958 core-seconds
    and the same in GPU-seconds; the unused 4342.609496084042 of the reservation was returned.
(g) Readers of the R3 source and pressure R3. The snapshot and matrix readers of the second R3 attempt were released
    at 19:14:02Z, after the lead's review of the R3 source result, for one attempt each in sequence on one CPU with
    no GPU (30 s timeout, no retry), at 30 recovery core-seconds each. The reader programs of the earlier legs would
    have rejected the name of the second attempt; the lead's earlier review of the reader drafts missed this, and the
    verifier found it before any reader ran. Each reader therefore ran a new version that differs from the earlier
    one by one line, which maps the second attempt's record name to leg R3; the earlier versions are unchanged. A first
    admission stopped before any allocation or run, because its guard test read a field name that the guard's record
    does not use; the test was corrected in a dated record before the repeat, on the same condition. The snapshot
    reader ran at 19:17:45Z for 5.40 s with exit 0 and 3355 checks confirmed and none refuted; the matrix reader ran
    at 19:18:00Z for 0.24 s with exit 0 and 256 checks confirmed and none refuted. The 21917 input files rehash
    unchanged after both, by the verifier's and the lead's rehash. The lead accepted both results at 19:26:31Z in
    their scope: the saved R3 source files reproduce, their operands are finite, the registered source geometry holds
    and the saved matrix products are consistent. This is not a statement of node, projection, source, quadrature or
    pressure accuracy. The R3 pressure run was released at the same time for one attempt (one CPU, no GPU, worker
    1740 s, watch 1800 s, no retry), to launch by 01:29Z and complete by 02:00Z on 28 October, and its launch
    requires the verifier's total disk use to be below 23884876736 bytes, so that twice the output size of an earlier
    pressure run plus twice the highest background growth measured that day over the 1800 s watch stays below 24e9
    bytes. Charge: 60 recovery core-seconds for the readers; 1800 core-seconds reserved for the pressure run.
    Pressure result: the run was launched at 19:28:26Z on one CPU and no GPU and completed at 19:28:51Z with return
    code 0, after 24.77443973813206 s of its 1800 s watch. It was first accepted as a completed run, not yet usable
    (19:43:46Z). Charge: 24.77913047419861 core-seconds and 0 GPU-seconds; the unused 1775.22086952580139
    core-seconds returned. The verifier's audit of the saved metadata gave 309 CONFIRMED / 0 REFUTED. Its pressure
    reader started at 19:49:44Z after a second processor admission (the first was refused because a process of
    another project was running on the reader's CPU; a refused admission is not a reader attempt) and exited 0 in
    0.97 s with 332 CONFIRMED / 0 REFUTED, exactly the expected count (charge: 30 recovery core-seconds). The lead
    then accepted R3 as a completed, internally consistent pressure result on the 32 local targets (the campaign lead's final
    review, 19:53:14Z). The four saved models are finite and match their recorded hashes. The two constraint
    choices agree to at most 6.7e-15 in P and 1.5e-14 in a grad P component, and the two partial orders to at most
    3.9e-16 in P and 4.1e-15 in a grad P component; that agreement is sensitivity to these two model choices only,
    not an error estimate. P at the origin is -0.648556. The comparison of R3 with R2 is reported in (r), as a
    difference of saved pressure models only. In the accepted scope this gives no pressure accuracy, no exterior
    uncertainty, no moment-study verdict, no source refinement verdict, no eligibility of the constrained models, no
    independent pressure agreement, no domain momentum norm of the registered specification, no exact profile and no
    label A.
(h) Leg R4: the disk-limit plan, the source run and the pressure run. The verifier's standing disk guard stops
    eligible workers once the verifier's total disk use reaches the registered soft limit of 24e9 bytes; a run
    directory has a registered maximum of 1610612736 bytes, and the hard cap is 30e9 bytes. None of these is raised.
    A first lead projection (18:11:55Z), from the saved progress records of the second R3 attempt, applied the R3
    byte rate to the full 19800 s cap of the R4 source and found no fit; the lead later recorded (18:31:28Z) that
    this overstates a normally completing leg, whose output is set by its row count, not by its cap. The verifier's
    finite-output disk plan was then accepted as the planning basis for the R4 source request, not as an admission.
    It models the run growth as 40960 bytes per row with stated allowances, and gives a launch ceiling of 23530237952
    bytes for the verifier's total disk use (24e9 bytes less a minimum size allowance of 320 MiB and a minimum
    background allowance of 128 MiB). On the second R3 attempt from 17:55:32Z to 18:30:21Z the run grew by 41636.6
    bytes per manifest event, 1.65 per cent above the model, and the background growth (growth not due to the run)
    averaged 4104 B/s. On the completed attempt the run grew 248090624 bytes, 0.79 of the model applied to it, so the
    size allowance stays at its minimum. At 19:11:52Z the guard read 23453069312 bytes, 77168640 bytes below the
    launch ceiling; the lead estimated (not a bound) that at a background of 3.9 kB/s plus about 20 MB of reader and
    R3 pressure outputs the ceiling would be reached near 23:15Z, planned the R4 source request for 22:00Z, and
    required that requests bind earlier records by path and sha256 instead of copying them. At 19:20:33Z the
    verifier's first planning observation under the rules below (metadata arithmetic, not an admission) gave a total
    of 23455105024 bytes, background rates of 5998.57 B/s over the last 2 h and 9478.43 B/s over the last 30 min, a
    background allowance of 246677171 bytes (the larger rate over 21600 s, rounded up, plus 40 MiB of planned
    outputs) and a projected total 37326515 bytes above 24e9: no fit at that time. The launch ceiling of 23530237952
    bytes holds only with the minimum allowances; a larger background allowance lowers it. The request must meet
    these rules: a guard stop during R4 is a failed leg, not a partial result; the size allowance is scaled up if the
    actual growth of the second R3 attempt exceeds the model applied to it; the background allowance is at least its
    minimum and covers, over the R4 source and pressure caps (19800 s plus 1800 s), the larger of the background
    rates over the last 2 h and over the last 30 min before the request, plus the planned outputs after the entry,
    each sized from its equivalent in an earlier leg, where the background is the growth of the verifier's total disk
    use less the growth of released runs and jobs measured by their own records (19:15:00Z); the projected total
    stays below 24e9 bytes and the run below its maximum, each with a positive margin stated in bytes. If the plan
    does not fit, the only further option is a deletion list of files that nothing binds, deleted only after a dated
    lead review of the list; there is no compression or raise. An earlier R4 entry, before the R3 pressure run, was
    proposed and not accepted (18:37:19Z): that order changes the projected total only by the background over the
    delay, under about 15 MB for a delay under 1 h, while an R4 guard stop would then leave no room for the R3
    pressure run. The R4 source request may be submitted with the R3 pressure result once the R3 pressure processes
    have exited; the lead reviews the R3 pressure result first, and the R4 launch follows its acceptance. The last R4
    source launch is 2026-10-28T03:00:00Z, and the R4 chain must complete by 11:00Z on 28 October. If nothing fits by
    03:00Z, R4 is not run, and this report then states the reason and the measured numbers. Status at this version:
    the R4 source, which keeps the finite and exterior orders of R2 (96 and 192) and raises the angular grid from 47
    x 93 to 71 x 141, so that R4 against R2 is an angular sensitivity test and not a nested refinement after R3, was
    released at 20:02:23Z for one attempt on one CPU and one GPU at nice 19 with a 19800 s watch, after a disk plan
    that fitted with 49229824 bytes below the launch ceiling at 20:00:30Z. It was launched at 20:04:37.882921Z, when
    the verifier used 23481430016 bytes, 48807936 bytes below the launch ceiling of 23530237952 bytes (24e9 bytes
    less the minimum size and background allowances), and the launch was accepted at 20:13:06Z. Charge: 19800
    core-seconds and 19800 GPU-seconds reserved. Result: the run completed at 2026-10-27T23:20:45Z, after 11767.566 s
    of its 19800 s watch, with return code 0 and no failure record. It wrote 2977 source rows (2976 requests and the
    leading row), all computed fresh and none taken from the cache, under one new cache identity; afterwards all
    22022 bound inputs of the request and the 237 frozen files rehashed unchanged, and the 6007 files newly bound by
    the result request (row files, archives and records) rehashed unchanged. Peak resident memory was 4204138496
    bytes (the watcher's whole-run high-water value) and observed GPU memory 847249408 bytes, below the 8 GiB and 2
    GiB caps. The worker log was empty; the watcher log held two retry notices of the bounded disk-usage wrapper,
    each for a temporary row file renamed during a scan, and successful retries of the guard are not observable. The
    run directory grew 240779264 bytes, 0.7176 of the minimum size allowance of 320 MiB (335544320 bytes), and the
    verifier's total disk use was 23745069056 bytes at the end, 254930944 bytes below 24e9; the guard did not stop
    the run. The lead accepted the result at 2026-10-27T23:25:32Z as fixed finite source data of leg R4 only; it is
    not a pressure result, a pressure accuracy statement, a source refinement verdict, a momentum norm of the
    registered specification or evidence of an Euler solution, and the content of the source arrays is checked only
    by the two readers. Charge: 11767.576421019156 core-seconds and the same in GPU-seconds, for the whole watch; the
    unused 8032.423578980844 of each reservation was returned. The two readers of the saved source were released at
    2026-10-27T23:31:05Z, one attempt each, and ran on one CPU without GPU, each charged 30 recovery core-seconds.
    The snapshot reader confirmed all 3259 of its checks (reproducibility of the saved source files, finite operands
    and the registered source geometry) in 5.50 s of wall time, and the matrix reader confirmed all 256 of its checks
    (the saved matrix products recomputed in exact rational arithmetic from the saved binary64 inputs; the largest
    scaled error was below 2.56e-16, against a tolerance of 2^-43) in 0.42 s; both exited with code 0. The lead
    accepted both results at 2026-10-27T23:42:21Z as finite internal consistency of leg R4 only; they do not test
    source or derivative accuracy, quadrature convergence or pressure accuracy. The R4 pressure run was released at
    2026-10-27T23:42:46Z for one attempt and launched at 2026-10-27T23:45:06Z on one CPU without GPU. It completed at
    2026-10-27T23:45:24Z, after 17.865 s of its 1800 s watch, with return code 0 and no failure record; it wrote 28
    output files (18493440 bytes allocated), its peak resident memory was 959021056 bytes, below the 8 GiB cap, and
    the verifier's check of its saved metadata confirmed all 335 of its checks. The lead accepted it at
    2026-10-27T23:55:38Z as a completed run of leg R4, an angular sensitivity comparison with leg R2; it is finite
    pressure data at the 32 local points and is not a pressure accuracy statement, a refinement verdict, a momentum
    norm of the registered specification or evidence of an Euler solution. Charge: 17.865782154724002 core-seconds
    and no GPU-seconds; the unused 1782.134217845275998 core-seconds were returned. Its saved-output reader was
    released at 2026-10-27T23:56:18Z for one attempt; the run becomes usable only after that reader passes and a
    final review by the lead. Reader result: the reader started at 23:58:03Z on one CPU without GPU, after a clear
    processor admission, and exited 0 in 1.06 s of wall time with 332 CONFIRMED / 0 REFUTED, exactly the expected
    count (charge: 30 recovery core-seconds). The lead then accepted R4 as a completed, internally consistent
    pressure result on the 32 local targets (2026-10-28T00:08:29Z). The four saved models are finite and match their
    recorded hashes. The two constraint choices agree to at most 6.1e-15 in P and 1.4e-14 in a grad P component, and
    the two partial orders to at most 4.8e-16 in P and 3.2e-15 in a grad P component; that agreement is sensitivity
    to these two model choices only, not an error estimate. P at the origin is -0.648556. Leg R4 is then usable by
    the two final consumers of the source and pressure validation chain, each under its own release: the moments
    reducer ((q)), which reads the source legs and their raw low moments, and the comparisons reducer ((r)), which
    reads the saved pressure models. The comparison of R4 with R2 is reported in (r), as a difference of saved
    pressure models only. In the accepted scope of R4 this gives no pressure accuracy, no exterior uncertainty, no
    source convergence or refinement verdict, no moment-study verdict and no eligibility of the constrained models
    (both come only from the moments reducer, (q)), no independent pressure agreement, no domain momentum norm of the
    registered specification, no exact profile and no label A.
(i) Group B controls: FAILED and CLOSED. The registration of the independent Newton agreement needs the reviews of
    three manufactured software controls, identified in the accompanying artifacts, on fixtures at c_l = 0.4375, omega
    = -0.75, omega/c_l = -12/7 and c_l = 0.46875, omega = 1.25, omega/c_l = 8/3, not at the selected state. They were
    released one attempt each, in that order, on one CPU. The first control FAILED with exit code 1 at 17:25:08Z.
    Its cause, by the verifier's static diagnosis, which the lead found plausible, is that the control's import audit
    rejected a synthetic module filename that the installed torch library sets in one of its modules.
    This is an infrastructure failure, with no result. Its 960 recovery core-seconds stay charged, with no refund.
    The other two controls were NOT ATTEMPTED, and the sequence is CLOSED, with no recovery
    path.
(j) Independent Newton agreement: NOT RUN. This is the registered comparison of the pressure legs with Newton legs
    (it loads the fields, the moments, every pressure leg and every Newton leg). Its source revision was accepted for
    one capped metadata-control attempt, unexecuted, and its control registration was accepted, with a
    cross-registration provenance proof accepted as a conditional software argument. Independent Newton production
    was NOT RUN, by a lead decision at 17:28:28Z, ahead of the 2026-10-28T04:00Z decision cutoff, for these reasons:
    its registration needs the Group B control reviews, and the Group B sequence is closed; a recovery would need a
    new import-audit source, its review and release, three new control runs (2880 recovery core-seconds), three
    result reviews and then the Newton registration; even then, Newton production would be 3700.231505514123
    GPU-seconds short with full caps; and Stage III time goes to the pressure chain. The release of its metadata
    control was withdrawn before installation; nothing was allocated, and its 60 production core-seconds were not
    charged.
(k) Resource snapshot of the independent route at hour 72, accepted with residuals and cited in its accepted
    corrected wording only. It is the cumulative T0-to-hour-72 snapshot over Stages I and II, built on 16824 monitor
    samples. It leaves the first 1829.0139997005463 s unobserved and excludes one 75.08547329902649 s gap. The
    reserved capacity is 144 GPU hours and 216 CPU core hours; that is an allocation, not usage. The device activity
    proxies are 18.97254220955471 h on GPU 6 and 10.429719867259264 h on GPU 7. The power integrals are
    6.2199223333958775 kWh and 5.817000361342315 kWh. The power integrals include idle draw; both device-level
    measures may include foreign activity. The CPU sums are incomplete observed sums: 86.37815833333333 h of summed
    maximum counters and 81.43791944444445 h of within-sample increases, over 2074 keys. None of these figures may be
    added to one another. Historical attribution and CPU completeness stay open, and the non-overlap of the
    snapshot's runs with other work holds at admission level only. Charge: 600 recovery core-seconds.
(l) Resume test repetition (primary route), accepted in this scope only. The deployed worker v2.4
    (2edbd00c, in the accompanying artifacts), run directly outside the queue on one disposable job (degree 4, Nk 10,
    c_l = 0.45, omega = 1, omega/c_l = 20/9, two starts, 400 iterations, 30 s checkpoints) on GPU 5, was stopped by kill -9 at 17:50:59Z,
    resumed from its checkpoint at iteration 230 and completed both starts; the run lasted from 17:48:57Z to
    17:56:58Z (481 s of wall time). This is one software restart test. It is not evidence about any state, and it
    gives no failure-rate bound. Its isolation from the other primary-route jobs held at admission only, not for the
    whole run. It makes the interruption-and-resume statement current for the deployed worker; the record of 24
    October stays citable for the worker of that date.
(m) Single-command validation of the saved file of the selected state (primary route): the full validation command
    in the accompanying artifacts, applied to the saved start file (b2c11172) of the degree-10 rung at c_l = 0.45,
    omega = 1, omega/c_l = 20/9, run once on GPU 0 from a clean process, with unchanged code (27 module hashes equal to the recorded ones)
    and no training. Its wall cap was amended from 3600 s to 18000 s, on the estimate, made before the launch, that
    the full battery includes two ray pressure checks of about 50 min each; the run's output is buffered and
    unstamped and gives no per-check times. The command released for the test was launched at 16:45:11Z after a
    passing preflight at 16:44:55Z and exited 0 at 18:42:07Z, after 7016 s. The lead accepted it at 19:16:57Z as a
    reproduction of the saved diagnostics from a clean process, in that scope only. Of the 89 rows, 81 agree within
    1e-6 relative (57 identical, 21 to rounding and 3 close), among them the two holdout rho_u^max values of this
    state that this report cites, 0.04195 and 0.04145 (5.4); 1 row is definitional (the holdout Tier S flag, false in
    both runs); 7 differ. The 7 are: rho_u_bal, an unweighted RMS of rho_u over the valid shells, on the training and
    holdout grids, by about 5 per cent; three Gram shell lists with 21 entries against 23, which agree on the 21
    common shells to at most 2.4e-16; and two closure quantities at the rounding floor in both runs. The cause of the
    rho_u_bal difference is open: the code text and the ratios of the squared values (19/17 and 23/21) are consistent
    with two extra valid shells per grid in the saved run, from far nodes that the training worker adds to its model
    and the validation script does not, but no record shows that the saved battery ran with that model, and this
    report cites no rho_u_bal value. The sections of the run's output that have no saved counterpart are unreviewed
    and are not cited. This is not new evidence about the state.
(n) Supervisor recovery test (primary route): the stop command followed by the start command in the accompanying
    artifacts, from a new login shell.
    It passes if the restarted supervisor is alive, heartbeats within its usual interval and shows the same accepted
    queue and ledger state as before the stop. It was run once on 2026-10-28 from 02:49:02Z to 02:55:48Z, after both
    jobs of the degree-10 control and perturbed continuation pair at c_l = 0.45, omega = 1, omega/c_l = 20/9 had
    written their completion records and their cap watchers had exited, with no job pending or running (8 jobs stayed
    held). The supervisor was stopped with the stop command (it exited at its next poll, within 20 s) and
    restarted from a new login shell with the start command. The restarted supervisor was alive and wrote
    its first heartbeat 123 s after its start line; its first two heartbeat intervals (123 s and 121 s) were longer
    than its usual 61 to 80 s and the third was 61 s, all far inside its staleness limit of 1500 s. The queue counts
    (no job pending or running, 270 done, 30 failed, 8 held) were unchanged, the 2405-row ledger was byte-identical
    before and after, and the leaderboard rows saved before and after (three each) were identical. One status-file
    display value changed. The campaign lead attributed it to a superseded copy of the leaderboard module held in
    memory by the old supervisor process, consistent with the recorded source history and with the two rankings
    reproduced from the ledger; the memory of that process was not captured. No ledger row changed, and the test did
    not hash every saved solver state before and after. The review of the record by the campaign lead
    (2026-10-28T03:04:31Z) found the pass criteria met, with the two longer intervals recorded as observations inside
    the staleness limit. This is a software test of stop and restart, not evidence about any solver state.
(o) Exact non-axisymmetry of the represented leading tail of the selected state (independent route, on the saved file
    of the primary route). A reader of the verifier, released after a lead review of its source and of the proof of
    its energy formula, read the stored leading-tail coefficients of the degree-10 rung of selection (1) of section 7
    (c_l = 0.45, omega = 1, omega/c_l = 20/9, R_0 = 0.3) as exact rationals, summed them at the far end of the radial
    basis to obtain the represented leading tail profile F, and evaluated in exact arithmetic three quadratic forms
    E, E_nonaxis and E_derivative: the total energy, the non-axisymmetric energy (the part with azimuthal order m !=
    0) and the derivative energy (the energy of the azimuthal derivative, in which each order is weighted by m^2) of
    F, each with the common factor R_0^(2 alpha) removed. It did this in two parameter conventions: alpha = (1 -
    c_l)/c_l and omega/c_l taken as exact quotients of the stored double-precision parameters (alpha =
    9907919180215091/8106479329266893 and omega/c_l = 18014398509481984/8106479329266893, close to but not equal to
    11/9 and 20/9), and taken as the rounded double-precision values of alpha and omega/c_l. It ran once, at
    20:41:04Z on one CPU, with exit 0; its 15 controls passed, and it was charged 90 recovery core-seconds. In both
    conventions the m != 0 energy is positive, with the mode ell = 2, m = 2 as a nonzero witness, so the represented
    leading tail is non-axisymmetric about the rotation axis. In both conventions the non-axisymmetric energy
    fraction e_F = E_nonaxis/E lies in [0.073669154969, 0.073669154970] and N_F^2 = E_derivative/E lies in
    [0.403041604945, 0.403041604946], well above the tail guard thresholds e_F >= 1e-4 and N_F >= 1e-2. The active
    azimuthal orders are m = 0, 2, 4, 6, 8, 10, all even, and N_F^2 >= 4 e_F holds, as it must for even orders. The
    lead reproduced every reported rational with its own decoding of the saved file. In both parameter conventions,
    the values of e_F and N_F saved with the selected state by the primary route (0.07366915496933443 and
    0.6348555780219913) agree with the exact values to within 7.1e-16 relative, comparing N_F through its square
    (independently checked). A second reader of the verifier, released after a lead review of its source and of the
    proof of its enclosure, then enclosed the registered dilation gauge integral of |F|^2 over the unit sphere, which
    equals E times R_0^(2 alpha), by exact rational series bounds, with R_0 the stored double-precision value. It ran
    once, at 21:04:00Z on one CPU, with exit 0; its 15 controls passed, and it was charged 90 recovery core-seconds.
    The integral lies in [1.000000000000000800, 1.000000000000000801] with the exact quotients of the stored
    parameters and in [1.000000000000000417, 1.000000000000000418] with the rounded values, so the registered gauge
    (this integral equal to 1) holds to within 1e-15 in each convention, though not exactly; an independent 80-digit
    decimal evaluation by the lead fell inside each enclosure. A static proof of the verifier, reviewed by the lead,
    extends the non-axisymmetry to the complete represented field. For the exact real interpretation of the stored
    coefficients and all five radial channels of the representation, U(r n) = r^(-alpha) F(theta, chi) +
    O(r^(-alpha-1)) uniformly on the unit sphere, with one angular derivative, where chi = phi + (omega/c_l) log r.
    Together with the positive m != 0 energy this implies that the complete represented velocity is not invariant
    under rotation about the axis (J U - DU J y is not identically zero), and that its normalized sphere ratios tend
    to e_F and N_F^2 as r tends to infinity. No finite radius or error constant is computed, and floating-point
    evaluation of the field is not covered. This concerns the finite represented field only. It is not a statement
    about an Euler solution, the pressure, the azimuthal phase gauge, a core non-axisymmetry threshold or persistence
    under refinement, and it does not change the label.
(p) Exact algebraic results on the source calculation (independent route). Six exact results of the verifier, each
    reviewed by the lead, describe the source calculation, and (3) also reports an exact reader result on a
    reconstructed table; (4) to (6) concern its pressure and the momentum residual. (1) Let U_t be the velocity that
    the structured evaluator forms from the stored, separately rounded angular tables (values, gradients and
    Hessians), and D_t the velocity-gradient matrix it forms from the same tables; D_t need not be the true Jacobian
    DU_t of U_t. The source tr(D_t^2) has spherical-harmonic degree at most 46 in exact arithmetic for the selected
    state, whose toroidal and poloidal tables reach angular degrees 23 and 22. Thus the 47 x 93 angular grid of R2
    projects this source exactly through degree 46, and the 71 x 141 grid of R4 exactly through degree 94. Neither
    statement bounds floating-point error. (2) U_t agrees with the canonical curl field when every stored angular
    polynomial H is harmonic and the stored gradient and Hessian tables equal grad H and the Hessian of H; this
    condition is sufficient, not necessary. With consistent tables, a poloidal term with a homogeneous H of degree
    ell and a radial factor g(q) of q = |y|^2 has the velocity defect g(q) y Delta H and the divergence ((ell+1)g +
    2q g') Delta H, with g' = dg/dq; toroidal terms have no such defect, and for a finite sum the defects add. For
    the actual Jacobian DU_t, a pressure solve with source tr((DU_t)^2) leaves div R_u = d + W.grad d, where d = div
    U_t, so the pressure solve alone does not establish incompressibility. (3) For separately rounded tables,
    explicit identities express the additional gradient and Hessian defects in the divergence, the supplied Jacobian,
    the vorticity, the pressure source and the momentum residual. A reader of the verifier, released after a lead
    review of its source and of its proof, computed these defects exactly for a fresh binary64 reconstruction of the
    selected angular polynomial table (283 harmonic labels, ell = 1 to 23). It ran once, at 23:59:37Z on one CPU,
    with exit 0; its 17 controls passed, and it was charged 90 recovery core-seconds. The lead accepted its result at
    2026-10-28T00:16:10Z after a recomputation with its own derivative tables and exact algebra (sharing only the
    reader's coefficient formula), which reproduced every saved row. For a polynomial H of the table with gradient
    table h and Hessian table K, the six exact rational defects h - grad H, K - Dh, Laplacian H, K - K^T, div(h -
    grad H) and curl(h - grad H) are nonzero in 270, 273, 266, 184, 267 and 265 labels, and their largest absolute
    coefficient-l1 bounds on the unit sphere are at most 2.8e-7, 4.8e-6, 6.8e-5, 4.4e-6, 1.1e-6 and 2.7e-6, all at
    ell = 23. These are exact properties of the rounded tables. They give no radial-factor bound, no floating
    evaluation enclosure and no field, source or pressure error. The fresh tables were not compared byte for byte
    with the tables used by the historical runs, so the size of such defects in the stored tables, and their effect
    on the selected field, are not known. (4) Let U be a C^2 field with divergence d and let D_t = DU + E be a
    continuous supplied matrix field, with U = O(r^(-alpha)) and DU, E = O(r^(-alpha-1)) outside a ball, uniformly in
    angle, for some 1 < alpha < 3/2; this is the range of alpha = (1-c_l)/c_l for 2/5 < c_l < 1/2. The source
    tr(D_t^2) then has mass integral of d^2 + Q and dipole integral of y d^2 + 2 d U + y Q, where Q = 2 tr(DU E) +
    tr(E^2). Its Newton pressure has a monopole and dipole expansion with remainder O(r^(-2 alpha)), and its gradient
    one with remainder O(r^(-2 alpha-1)). Without incompressibility, zero source mass and dipole are not implied; a
    compactly supported gradient field is a counterexample. A local hypothesis on D_t is needed, since the decay
    bounds do not control local singularities: with U = 0, a supplied matrix equal to |y|^(-2) times the identity
    near the origin gives a source of infinite mass. Continuity supplies such a hypothesis but is not necessary: with
    U = 0, D_t equal to the identity on the unit ball and 0 outside is discontinuous, and its source has mass 4 pi,
    zero dipole and exterior Newton pressure exactly 1/r. (5) Let R_u be the momentum residual of section 1 formed
    from U with its actual Jacobian DU and a C^2 pressure P. With no divergence condition, R_u satisfies div R_u =
    d + W.grad d - Q when P solves -Delta P = tr(D_t^2). Under the decay of (4), with P = O(1) and grad P =
    O(r^(-alpha)), the whole-space helicity identity integral curl U . R_u = (1 - 2 c_l) integral U . curl U holds,
    and the factor (1 - 2 c_l) is 1/10 at c_l = 0.45. (6) If two bounded integrable pressure sources differ by h,
    with m = ||h||_1 and M = ||h||_inf, their decaying Newton pressures differ by at most (1/2)(3/(4 pi))^(2/3)
    M^(1/3) m^(2/3) at every point, and their gradients by at most (3/(4 pi))^(1/3) M^(2/3) m^(1/3). For the sources
    tr(D_t^2) and tr((DU)^2) of (4), |h| <= 2 ||DU||_F ||E||_F + ||E||_F^2 pointwise, so replacing, in R_u, the
    Newton pressure of tr((DU)^2) by that of the supplied source, with U and DU unchanged, changes R_u pointwise by
    at most that gradient bound. This bound concerns the replacement of the pressure alone; a residual formed with a
    supplied field and matrix differs by further terms. No size of d or E, exact moment value, m or M has been
    computed for the selected field (the coefficient bounds in (3) are not field bounds, and the moment guards in (q)
    are finite readings of the numerical source representation), so (4) to (6) give no pressure or residual error
    bound. These results establish neither an Euler solution nor pressure accuracy, and they do not change the label.
(q) Low-mode moment guards of the source legs (independent route). The moments reducer, the first of the two final
    consumers of the source and pressure validation chain, reads the saved source legs and their raw low moments, not
    the pressure models. It evaluated the registered operational guards M1 and M2 on the four low modes (ell at
    most 1) of the numerical source representation of the selected state (c_l = 0.45, omega = 1, omega/c_l = 20/9,
    R_0 = 0.3), from the five source legs R0 to R4 (R0 and R1 are the two legs run before R2). For each leg and mode
    (ell, m), M_lm is the computed low moment of the pressure source for that mode and D_lm the matching absolute
    moment, computed with the absolute value of the integrand, so that |M_lm| <= D_lm for exact quantities; D_star is
    the larger of D_00 and the three D_1m divided by R_0. M1 requires |M_lm| to be at most 1e-7 times the larger of
    D_lm and the resolution cutoff 1e-2 R_0^ell D_star, and a mode is resolved when D_lm reaches that cutoff. M2
    requires the relative differences of D_star, and of D_lm for every mode resolved in either leg, to be at most
    1e-3 between the two legs of each registered pair. The constrained pressure models are eligible under the
    registered rule only if M1 passes on every leg and M2 on every pair. The reducer was released at
    2026-10-28T00:26:29Z for one attempt on one CPU without GPU and ran once, from 2026-10-28T00:28:44Z for 16.12 s
    of wall time, with return code 0. The lead accepted the result at 2026-10-28T00:41:00Z after recomputing both
    guards with its own code from the saved raw moments; the recomputation agreed with the saved values exactly in
    every status, D_star, D_lm, resolution flag and pair relative difference, and within a relative 2e-16 in |M_lm|,
    the M1 bounds, the cutoffs and the raw ratios. Guard M1 passed on all five legs; the largest ratio of |M_lm| to
    its M1 bound is at most 5.8e-7. Guard M2 passed on the four registered pairs (R1/R0, R2/R1, R3/R2 and R4/R2); the
    relative differences of D_star are at most 1.9e-5, and those of the resolved D_lm at most 5.4e-5, both maxima for
    R1/R0. In every leg exactly the modes (0,0) and (1,0) are resolved; the modes (1,-1) and (1,1) lie below the
    cutoff, so the M2 relative-D test does not gate them; they pass M1, and their raw ratios |M_lm|/D_lm are between
    0.66 and 0.78, so these modes show no relative cancellation. The constrained pressure models are therefore
    eligible under the registered rule. Charge: 300 core-seconds, the full watch cap, with no return, and no
    GPU-seconds; the measured use, 15.998475897591561 core-seconds, is a separate record. This is an operational
    status of the numerical source representation. It gives no exact moment cancellation, no error bound, no pressure
    accuracy, no exterior uncertainty, no momentum norm of the registered specification, no independent pressure
    agreement, no exact profile and no evidence of an Euler solution, and it does not change the label. The
    comparisons reducer, the second final consumer, is item (r).
(r) Comparisons of the saved pressure models (independent route). The comparisons reducer, the second final consumer
    of the source and pressure validation chain, reads the saved pressure models of the five source legs R0 to R4 of
    the selected state (c_l = 0.45, omega = 1, omega/c_l = 20/9, R_0 = 0.3), with the common velocity operands at the
    targets and the moment status of (q), not the source arrays. It compared them at the 32 local targets, which
    include the origin, and on their 19-point exterior subset (the targets with |y| >= R_0), in all 72 registered
    contexts: 20 constraint contexts (constrained against unconstrained model), 20 partial-order contexts (order 160
    against order 112) and 32 source contexts (R1 against R0, R2 against R1, R3 against R2 and R4 against R2, for
    each of the four models). Let A_num be the saved common velocity-only sum: on the 32 targets the direct sum of
    the four supplied velocity terms, and on the exterior subset the remainder-based sum, whose linear terms are
    evaluated on the supplied remainder field and its supplied derivative and whose advection term uses the supplied
    full velocity and its supplied full matrix. Its intended continuum target is (1 - c_l) U + (W . grad) U +
    omega J U, the part of R_u without the pressure; correspondence to that expression has not been certified for
    these supplied operands. Let P_b be the reference model of a context (the unconstrained model, the order 112
    model or the earlier leg). M3 is the RMS difference of the two pressure gradients over RMS(A_num + grad P_b), and
    M4 is the RMS pressure difference over R_0 times that same RMS. The reducer was released at 2026-10-28T01:07:50Z
    for one attempt on one CPU without GPU and ran once, from 2026-10-28T01:10:51Z for 7.53 s of wall time, with
    return code 0. The lead accepted the result at 2026-10-28T01:25:37Z after recomputing with its own code, from the
    saved norms, every ratio, bound, difference, slack, status and flag of the 72 contexts; every value agreed
    exactly. The saved norms equal those of a lead rerun of the same guard code on the same saved arrays, which is a
    reproduction, not an independent method. Every M3 and every M4 passed the operational threshold 1e-7; the largest
    M3 is at most 5.6e-14 and the largest M4 at most 7.7e-14, both in exterior constraint contexts. No
    constraint-sensitive flag was set, every sensitivity bound is defined and no ungated slack is negative. The
    reference residual RMS(A_num + grad P_b) itself is about 0.1455 on the 32 targets and about 0.1564 on the
    exterior subset, and relative to D_b, the sum of the RMS sizes of the four original supplied velocity terms and
    of grad P_b, it is about 0.036 and about 0.051. In the contexts of R2 against R1 and of R3 against R2 the saved
    models differ by at most 1.8e-34 in RMS gradient and 3e-30 in P at any target, so the pressure models of R1, R2
    and R3 are nearly identical at these points; R4 against R2 is the angular sensitivity pair of (h). So the saved
    pressure models agree with each other to rounding level at these points. This says nothing about how small the
    momentum residual is, and it is not a convergence or refinement statement. Charge: 300 core-seconds, the full
    watch cap, with no return, and no GPU-seconds; the measured use, 7.405944517813623 core-seconds, is a separate
    record. It gives no pressure accuracy, no error bound, no exterior uncertainty, no momentum norm of the
    registered specification, no independent pressure agreement, no exact profile and no evidence of an Euler
    solution, and it does not change the label.
(s) Exact axial vorticity residual at the origin of the selected state (independent route, on the saved file of the
    primary route). A reader of the verifier, released after a lead review of its source and of the proof of its
    origin formula, read the stored coefficients of the degree-10 rung of selection (1) of section 7 (c_l = 0.45,
    omega = 1, omega/c_l = 20/9, R_0 = 0.3, with the stored double-precision values as the inputs) as exact rationals
    and enclosed, in exact rational interval arithmetic, the axial component R_Omega,3 of the vorticity residual
    R_Omega of section 1 at the origin. Every azimuthal order of the stored state is even, so at the origin the
    velocity, the vorticity and R_Omega are axial, and the optional channels of the representation vanish there.
    There R_Omega,3 = Omega_3 + U_3 d_3 Omega_3 - (d_3 U_3) Omega_3, with U_3 and Omega_3 the axial velocity and
    vorticity and d_3 the axial derivative: the terms in c_l y and omega J y vanish at y = 0, and omega J Omega
    vanishes for an axial vorticity. These four origin values are fixed by four sums of the stored radial
    coefficients of the modes ell = 1 and 2 with m = 0. It ran once, at 2026-10-28T04:11:29Z on one CPU, with exit 0;
    its 26 controls passed, and it was charged 32 recovery core-seconds. R_Omega,3(0) lies in [2.918353012521,
    2.918353012522] and Omega_3(0) in [9.686140439066, 9.686140439067], so their ratio lies in [0.301291627029,
    0.301291627030]: the transport and stretching terms, together about -6.768, reduce the linear term Omega_3(0) to
    about 30 per cent of its value but not to zero. The lead reproduced the four coefficient sums with its own
    decoding of the saved file, and an independent 90-digit decimal evaluation by the lead fell inside each of the
    three enclosures. Since curl R_u = R_Omega for divergence-free U and any pressure, the represented field of the
    selected state is not an exact stationary profile: no pressure makes R_u vanish near the origin. This is one
    point value of the residual of one fixed field. A proof of the verifier, reviewed by the lead, turns it into a
    statement about the values at the origin of other fields, compared at the same centre and axis. For any C^2
    divergence-free field near the origin and every c_l and omega, R_Omega,3(0) = Omega_3 + U.grad Omega_3 -
    Omega.grad U_3 at the origin, which reduces to the formula above for the represented field. Take the twelve
    numbers given by the velocity, the vorticity, the gradient of U_3 and the gradient of Omega_3 at the origin. If
    each of them lies within delta of the corresponding number of the represented field, then, with rational bounds
    on the four enclosed origin values, R_Omega,3(0) is greater than 1459/500 - (3213/100) delta - 6 delta^2, which
    is 14183/16000 = 0.8864375 at delta = 1/16. So no exact profile, for any c_l and omega, has all twelve numbers
    within 1/16 of those of the represented field. The twelve numbers are within 1/16 whenever the velocity and its
    first and second derivatives at the origin each differ by at most 1/32 from those of the represented field. The
    exclusion also holds after a positive dilation and a rotation about the axis (a further proof of the verifier,
    reviewed by the lead): if W is an exact profile, then so is L^-1 Q^T W(L Q y), for L > 0 and Q a rotation about
    the axis, with the same c_l and omega, so none of these fields has all twelve numbers within 1/16 of those of the
    represented field. In particular, the field rescaled by the unique dilation that makes the registered gauge
    integral exactly 1, a dilation factor within 801/(4 x 10^18) of 1, has the same R_Omega,3(0) and the same ratio
    to Omega_3(0), so it is not an exact profile either (a further proof of the verifier, reviewed by the lead).
    Shifted centres and tilted axes are not covered. This pointwise comparison uses second derivatives (a further
    proof of the verifier, reviewed by the lead). For a C^2 divergence-free field with U_3(0) nonzero and any chosen
    value, zero included, adding a suitable compactly supported divergence-free swirl sets R_Omega,3(0) to that
    value. The swirl vanishes outside a small ball around the origin, vanishes with its first derivatives at the
    origin, and can be taken arbitrarily small in its values and first derivatives. The new field is not thereby an
    exact profile. These pointwise estimates provide no evaluated lower bound in the field distance of 6.7 or in
    continuum velocity norms. A weak form of the momentum equation does give a local separation, without numerical
    values (a further proof of the verifier, reviewed by the lead). Let phi be a smooth nonnegative radial function
    of unit integral supported in a small ball around the origin, and pair the momentum residual R_u with the curl of
    phi e_3, where e_3 is the axial unit vector. After integration by parts the pressure drops out, every omega term
    cancels because phi is radial, and the pairing involves the velocity only through its values and their products,
    not its derivatives. It is zero for an exact profile with parameters c_l and omega. For the represented field,
    with the same c_l, it is the integral against phi of Omega_3 + U.grad Omega_3 - Omega.grad U_3 + c_l y.grad
    Omega_3, whose value at the origin is R_Omega,3(0); for a small enough ball it is at least half of 2.918353012521
    for every c_l with 2/5 <= c_l <= 1/2. Hence there are a radius R > 0 and positive numbers delta_2 and
    delta_infinity, depending only on the represented field, such that every exact profile with 2/5 <= c_l <= 1/2 and
    any omega differs from the represented field by at least delta_2 in the L^2 norm of the velocity difference over
    the ball of radius R about the origin, and by at least delta_infinity in the maximum of its magnitude over the
    ball. The same holds after a positive dilation and a rotation about the axis as above. R, delta_2 and
    delta_infinity have not been evaluated and could be very small, so this gives no number in the field distance of
    6.7 or in any sampled or quadrature norm, and nothing to compare with a threshold. Nothing is shown outside that
    ball: there is no bound on the residual elsewhere, nothing about a refined or other state, no existence result
    for exact profiles and no nonexistence result beyond the local statements above, nothing that bears on outcome D,
    and no change to the label.

## 7. Outcome label and justification

Final label: C, set at the Stage III freeze from independently checked results only. No state reaches
Tier S: the lowest independently checked holdout, 0.04082/0.04142 (St1), is 4.1 times the bound on both families, and
St1 is not ranked ahead of St2 because its centre-weighted core-ball a_max is 38 and 48 per cent larger
(primary-reported); the single-term ratios are 3.7 to 5.0 times their bound (per-family shell maxima on the degree-8
rungs) and 20 to 32 times (three independent-route states, sigma_Om over |y| < 1024). Tier S is necessary for A and B,
so its failure withholds both. No complete obstruction covering the searched target class has been supplied: the
results of section 2 are partial (items 3, 5 and 7), a compact zero-free alpha-limit set of vortical points is not
excluded (item 17), and the necessary conditions failed by the leading states concern those states, not all profiles.
Optimizer readings (5.4, 5.6 (f)) characterize the tested runs and, under the registered rule, give operational floors
for the tested branches; they are not a bound on all represented fields and not an existence statement, and an
optimizer failure is never an obstruction.

Class statement. Label C asserts only that within the class below no state was found that meets Tier S on both shell
families together with the single-term, core-resolution and Poisson requirements; it does not assert that no profile
exists in the class or outside it.
(a) Equation and parameters: R_u = 0 with A = c_l I - omega J and the full-space pressure, at the 49 parameter points of
    Table C1 (c_l from 0.41 to 0.499, omega from 0.1 to 10, omega/c_l from 10/49 to 1000/41, with the reflection checks
    at omega = -3 and -0.3), not all points at every degree, and with the unsearched ranges listed under Table C1.
(b) Fields: on the primary route U = curl(T y) + curl curl(S y) with regular solid harmonics of main-block degree up to
    10 (four degree-10 starts; the two ladder rungs of 5.4 were read in Stage II), channels to degree 19 at degree 8 and
    to degree 23 at degree 10, radial Chebyshev expansions carrying the exact leading tail r^(-alpha) F and its twist,
    optional rate-(2 alpha + 1) channels, and even azimuthal modes in 888 of 892 Stage I starts; on the independent
    route its own representations of degree 2 to 6 with even and with all modes, and at c_l = 0.45, omega = 0.3,
    omega/c_l = 2/3 a degree-8 state and a degree-10 optimization (12 steps, then a bounded continuation of 429 accepted
    steps that did not reach its target; section 8, item 1), none of them a converged solve or a certified
    representation ladder; the gauge int_(S^2) |F|^2 = 1.
(c) Searches: least squares on R_u by Levenberg-Marquardt (both routes), Gauss-Newton and L-BFGS (independent route),
    with the seeds and budgets of Table C; levels optimizer-limited, stalled, floored in the operational sense or
    inconclusive (5.4, 5.6 (f)).
(d) What was found: all leading states fail Tier S, the lowest independently checked at 4.1 times the bound on both
    families (St1, not ranked ahead of St2 at 4.4 and 4.3 times); the degree-10 rung from St2 reads 4.2 and 4.1 times
    (primary values, reproduced from the saved data by the verifier's reader, not a fresh evaluation), and a degree-8
    rung from a far-closure state reads 2.98 and 3.13 times (primary-reported) and is not ranked ahead of its
    degree-10 rung (section 8, item 2).
    The D6 lineage has an unbalanced core (single-term ratio 18 to 21 times its bound) and a mismatched far coefficient;
    the nest ladders have balanced cores. The sampled Q_sw is above 1 on their degree-4 states, their tested
    near-axisymmetric degree-2 parents and the second degree-6 start at c_l = 0.45, omega = 1, omega/c_l = 20/9, and
    below 1 on the other degree-6 and degree-8 rungs; this neither establishes nor excludes Q_sw <= 1. The eleven
    momentum-only exports miss both whole-space balances at order one (E_ren < 0 on all, H_tot < 0 on all but one); the
    balance-arm state reduces both far below the registered 0.05 bounds (finite estimates, no exact balance) at residual
    ratios 1.232/1.235 to its start and fails both far-coefficient conditions at order one.

Stage II gate (failure map). The Stage II deliverable was posted at 2026-10-27T11:12:39Z (hour 66.06), after the
verifier's audit of its text. No state meets Tier S and no refinement-stable candidate with independently checked
pressure exists, so the deliverable is a failure map: one row per arm and branch, with mechanism readings taken from the
registered list (core balance, far balance, global balance, transport degeneracy, amplitude instability,
budget-limited, aliasing, near-edge escape). The readings are interpretations, not proved causes; the list is not
exhaustive, and no mechanism is established as the cause of the floor on any branch. In brief (primary-reported
unless marked):
(a) Global balance is a supported hypothesis for the even-class floor: E_ren < 0 on all eleven momentum-only primary
    exports and H_tot < 0 on ten (theory route; Structural defects (a)), but the arms that targeted the balances
    either did not attain them (optimizer-limited) or, in the degree-4 balance arm, attained them only at 1.23 times
    the start's holdout, so it is not established.
(b) Far balance, in the sense of the represented first correction. At degree 6 the far-closure rows met the closure
    diagnostic while the residual stayed above Tier S; their holdouts are 0.983/0.963 times their start at omega = 1
    (omega/c_l = 20/9) and 0.782/0.795 times their start at omega = 0.3 (omega/c_l = 2/3) (5.6 (c)). This is the
    registered reading "far closure compatible with the floor"; it does not exclude unresolved correction modes,
    other far-field terms, matching defects or optimizer limits. The omega = 1 state fails the order 18 versus 27
    pressure guard and is not ordered against its start; the omega = 0.3 state passes the registered guards but is
    not ranked ahead of its start, because its core-ball a_max is higher (5.6 (c)). At degree 8 the closure states
    lower the shell holdouts (primary-reported) but fail a core-set guard against the five (omega = 1) and four
    (omega = 0.3) original comparison states listed in section 8, item 2, including their degree-10 rungs; their
    wider conditional ordering, including St1 continued for 150 iterations at omega = 1 and several degree-6 states
    at both points, is given there.
(c) Core balance is the reading of the arms that forced swirl or eddies (5.6 (d)) and of the core side of the
    trade-offs of St1 and of the degree-8 closure states.
(d) Amplitude instability is the reading of the combined vorticity and momentum formulation (four runs at c_l = 0.45,
    omega = 1, omega/c_l = 20/9 and omega = 0.3, omega/c_l = 2/3; at weight 10 both runs collapsed toward the trivial
    state) and of the viscous continuation with free omega at c_l = 0.45 (omega drifted from 1 to 0.533, omega/c_l
    from 20/9 to 1.184, and the solve collapsed to the tail).
(e) Budget-limited is the reading of the arms that ended at an iteration or time limit, among them both degree-10
    rungs at c_l = 0.45 and the three degree-6 all-mode arms; the resolution floors therefore mix truncation with
    budget. Arms that stopped on the function-change criterion with V10 above 1e-3 did not meet the stationarity
    diagnostic either.
(f) Artificial viscosity did not remove the floor at any of the six viscous rungs at c_l = 0.45 (four at omega = 0.3,
    omega/c_l = 2/3, and two at omega = 1, omega/c_l = 20/9).
(g) Transport degeneracy, aliasing and near-edge escape are attached to no row.
Selection for Stage III, frozen at the gate:
(1) the degree-10 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9 started from St2 (0.04195/0.04145): it has the
    lowest holdout among the states it is ordered against, it is ranked ahead of St2, St3, St4 and state (2), among
    others, conditionally on core resolution, and it has the most independent evidence already bound; it comes first
    in the independent pressure and momentum evaluation;
(2) the degree-6 all-mode state at the same parameters (0.04819/0.04745; 28 per cent of ||U|| in odd modes on the
    training grid; time-limit stop after 265 iterations, V10 0.045, so not stationary), a symmetry-branch
    representative, not an improvement;
(3) the independent route's degree-10 terminal state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (the route's fresh
    holdout 0.061923/0.068983). Its m != 0 energy fraction of the far-field profile is 0.2608, read from the
    verifier's terminal battery (2667 of 2668 checks passed) and resolved under its angular refinement; the content
    is even-m by construction of the class. The one failed check, the unit-ball core-doubling momentum RMS check
    (0.10050 against 0.1), stays a failure.
The degree-8 closure state at omega = 1 is not selected: it is not ordered against the degree-10 rung, its core-set
a_max is 2.02 times the rung's, and it has no independent evaluation. The gate text and the verifier's audits of it are
among the accompanying artifacts.

## 8. Remaining uncertainties and next experiments

1. Flooring. Under the resolution-step rule the branch at c_l = 0.42, omega = 0.3, omega/c_l = 5/7 (0.867/0.957, then
   0.969/0.943) and the D6 lineage are floored at degree 8. The two c_l = 0.45 branches had one weak step each, and
   their degree-10 rungs give a second (0.946/0.950 at omega = 0.3, omega/c_l = 2/3; 0.961/0.957 at omega = 1,
   omega/c_l = 20/9; primary values, reproduced from the saved data by the verifier's reader, not a fresh evaluation),
   so both are floored at degree 10 with 4 far-correction channel functions. In each of these steps the finer state
   stopped at the iteration limit, so the factors mix truncation with budget, and the 4-function channel blocks are
   radially unresolved; whether more channel functions, a larger budget or another optimizer at degree 10 would lower
   the step factor is not tested. In the independent degree-10 evaluation the tested 17-polar-point rule failed (it
   moves the objective by 3.3e-7 relative, registered 1e-8) and the tested 26-point rule passed; this does not show that
   every smaller rule fails or that 26 is a minimum. Its first 12-step optimization, at c_l = 0.45, omega = 0.3,
   omega/c_l = 2/3, is machinery evidence only; a fresh evaluation of its end state gives rho_u^max 0.0621/0.0691 on the
   two shell families (all 1892 producer checks pass; 50 strict energy-identity reader checks fail and are kept), within
   0.41 per cent of the route's degree-8 state and not a candidate. A bounded continuation from it ended at its soft
   wall-clock cap after 429 accepted steps (858 attempts) without reaching its target. A fresh battery of its end state
   gives holdout rho_u^max 0.06192/0.06898 (0.21 and 0.19 per cent below the 12-step state) and rho_nl^max
   0.07165/0.09142, with core-set sigma_u^max 2.328, core-set a_max 4.093 and finite-volume sigma_Om about 2.062, so no
   tier is met (independently checked; 2667 battery checks pass, and the unit-ball radial and angular doubling check
   fails at 0.1005 against 0.1, while recomposition from the saved shells changes that ball value by a relative 5.05e-4;
   the saved-data reader passes 30744 checks and keeps 58 strict energy-identity failures). Independent pressure
   accuracy and full-space coverage remain open for it. The degree-10 representative state at c_l = 0.45, omega = 0.3
   (omega/c_l = 2/3), a failed representative and not a candidate, was recovered from its typed checkpoint in a fresh
   isolated CPU process. Its typed values, terminal arrays, random-generator state and normalization data agree with
   the saved state; the serialized bytes differ by 6 bytes. Its finite field values at 33 points (17 distinct) were
   recomputed at 100 decimal digits. All 33 values and both header lines agree byte for byte with the earlier record;
   only the timing line differs. This rehearses recovery and finite reproducibility only. It validates no profile and
   makes no momentum, pressure or enclosure claim. No run was shown to be the registered clean-process check of the
   final selected package (item 13).
2. Far closure. The 4-function channels are radially unresolved; doubling them helped the far closure but worsened the
   core (5.6 (c)). By |energy ratio - 1| <= m/c, at c = 0.04 a mismatch m <= 4e-4 suffices for a ratio within 0.01 of 1;
   it is not necessary. Far-closure rows at weight 1 met the far-closure reading on St4 with the core worse (5.6 (c)).
   Later primary readings at c_l = 0.45 (primary-reported, not evaluated independently): (i) the degree-8 rung from the
   far-closure state at omega = 1, omega/c_l = 20/9 (5.6 (c)), with closure rows at weight 1 (mismatch 2.7e-8), has
   0.02983/0.03130, the lowest primary-reported shell holdout among the five states it was compared with (the degree-10
   rung, St1, St2, St3 and its own degree-6 start), and a training momentum RMS 7.4 per cent below its start's; its
   core-set a_max is 1.206 (2.02 times the degree-10 rung's and 1.97 times its start's) and its core-set sigma_u^max
   1.19 times the degree-10 rung's, so by the ordering rule it is ranked ahead of none of the five (the verifier
   reapplied the inequalities to the saved scalars); over all saved readings at these parameters it is ranked ahead of
   St1 continued for 150 iterations (0.03995/0.04040, primary-reported) and of seven degree-6 states (the verifier
   reapplied these inequalities as well). It stopped on the function-change criterion after an unsafeguarded
   lagged-iteration excursion, so stationarity is not established. Its three finite-radius far-energy coefficients
   (0.672, 0.892 and 0.967 at 2^12, 2^14 and 2^16 R0) move toward the required value 1; successive deviation ratios are
   0.329 and 0.303, compared with the predicted 0.340; a next-radius value would be an extrapolation, and independent
   far-source and extended-precision checks remain open. The sibling degree-8 rung from the far-closure state at omega =
   0.3, omega/c_l = 2/3 (primary-reported; the verifier reapplied the inequalities to the saved scalars) has
   0.03739/0.03940, lower than each of the four states it was compared with (its own degree-6 start, St7a, St7b and the
   degree-10 rung), and rho_nl^max 0.2665/0.2821; its core-set a_max is 1.435, 1.21 to 1.39 times theirs, so it is
   ranked ahead of none of them; over all saved readings at these parameters it is ranked ahead of six degree-6 states
   (verifier-checked on the saved values). It stopped on the function-change criterion after 123 iterations at 0.615
   times its projected initial objective, after a logged excursion to 2237 times that value, so stationarity is not
   established.
   Its three finite-radius far-energy coefficients (1.212, 1.073 and 1.019 at 2^12, 2^14 and 2^16 R0) move toward 1 from
   above; the two deviation ratios are 0.344 and 0.261, compared with 0.340; the limiting coefficient and rate remain
   unvalidated. A safeguarded continuation of the omega = 1 rung under the self-consistent objective, started from the
   consistently aligned rung state with the same weights and closure target, accepted no step at any damping up to 1e10
   (gradient norm 4.0e-9 at cost 5.4e-9); its end state is the aligned start to rounding on the worker grid
   (primary-reported; the verifier checked the saved arithmetic of the comparison, not the fields). This is an optimizer
   reading, not a stationarity statement, and no ordering follows. (ii) Continuing the far-closure state at omega = 1
   with a stricter stopping tolerance found a plateau (the cost fell by at most 0.04 per cent in its first 88
   iterations) and then an excursion that ended at 42 times the start's cost: an optimizer diagnostic, not a state.
   (iii) A safeguarded replay of the far-closure arm at omega = 0.3, omega/c_l = 2/3, met the weight-1 closure rows from
   its weight-0.1 start with the reported holdout and training RMS at the start's level (0.05795/0.05781), 10.9 and 7.7
   per cent above the primary values of the unsafeguarded end state (0.05227/0.05368; 5.6 (c)); by the registered
   reading, that arm's gain depended on its excursion path (the arithmetic was checked by the verifier on the saved
   records). The independent route's four Stage I training pilots at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (degree 6)
   that carry the missing angular degrees and eliminate the first nonlinear far-coefficient equation exactly (defect 6.6
   (g)) completed fresh holdouts at one pressure order: 0.1004/0.1238, 0.1090/0.1129, 0.1154/0.1250 and 0.1147/0.1276
   (independently checked; each has 386 passing saved-array checks). Pressure convergence and representation ordering
   remain open for them, and their training values establish no ranking.
3. Pressure and optimizer. The monopole amplitude between 120 and 180 source nodes is unresolved and 82 of 86 guard
   regions were not re-tested (6.3). The optimizer test is optimizer-limited, the fixed-target control inconclusive, the
   Gauss-Newton floor operational only, and every degree-8 rung stopped at its limit, so truncation floors are not
   separated from optimizer trapping; extrapolating the independent ladder to Tier S (degree 24 at 0.82, degree 20 at
   0.78) is a heuristic, not a convergence bound. A rank-2 gauge-pivot variant was tested before use, from a start
   pre-aligned so that the rank-2 pivot leaves it unchanged. Over six Levenberg-Marquardt iterations, its cost history
   did not reproduce the production rank-1 history up to the rigid rotation, as registered. The relative cost
   differences grew from 6.2e-7 to 2.6e-4, and at the logged iterations 0 and 5 the damping parameter was larger by
   factors of about 1000 or more. The extended Stage III arm was therefore not run; the six-iteration smoke pair did
   run. The two runs differ both in the gauge row and in the rotated coordinates the solver works in, and the solver's
   diagonal damping is not rotation-covariant in general; which difference produced the different paths is not
   established. A CPU replay of both six-iteration runs reproduced all twelve printed seven-digit costs, so the observed
   difference between the two pivot choices also occurs on CPU at that precision. Its cause remains open. No conclusion
   about the equations follows. In general the diagonally damped Levenberg-Marquardt step is not covariant under a
   rotation of the coordinates, even for an objective that is invariant under that rotation; a two-dimensional example
   with exact arithmetic shows one rotated start accepting its trial step and the other rejecting it (independently
   checked). This shows that the rotated replay need not reproduce the original path. It does not establish why the
   observed paths differed.
4. Structural arms and swirl. The balance arm is inconclusive (1.232/1.235), the other balance runs optimizer-limited.
   The all-m probe brought the sampled Q_sw below 1 at nearly unchanged residual; this neither establishes nor excludes
   Q_sw <= 1. The combined vorticity-momentum formulation arm is complete (four runs by 2026-10-26T03:08Z,
   primary-reported): none counts as an improvement on its start; at weight 1 the holdout rho_u^max rose from 0.046 and
   0.067 to about 0.20 and 0.25, and at weight 10 both runs collapsed toward the trivial state (no reading). The
   all-mode arms are summarized in 5.6 (j): three primary degree-6 arms with all azimuthal wavenumbers ended at their
   time limits with holdouts between 2.8 per cent below and 4.7 per cent above the even-class degree-6 states, the fresh
   all-mode starts promoted to degree 6 at three parameter points ended with holdouts between 0.164 and 0.249, between
   2.44 and 4.93 times those of the even-class degree-6 state of the same point (a summary of 5.6 (j), whose
   qualifications apply: saved-record audit scope only, the comparator budgets and unrecorded comparator code versions,
   and the device incident at c_l = 0.42, omega = 0.3, omega/c_l = 5/7), and the independent route's Stage II all-mode
   result is its eight-step run (rho_u^max 0.41029/0.41483); the planned longer continuation and its omega = 1 companion
   were not released and have no result. The independent route's Stage I all-mode runs (holdouts 0.399 to 0.758) are
   separate coverage records with their guard failures retained.
5. Parameters. Whether profiles, if any, form open sets, curves or points in (c_l, omega) is unknown, so a floor at
   fixed parameters is not a floor for the problem. Open: residual maps along parameter paths, finer c_l steps beyond
   c_l = 0.48, omega = 0.3, omega/c_l = 5/8, and the effect of the bound handling of the free-parameter runs (5.2 (e)).
6. Viscous continuation. Next runs fix omega as well as c_l and pin the core amplitude; every nonzero exact
   constant-viscosity solution satisfying the tail and pressure hypotheses of section 2, item 29 has positive E_ren
   (for a localized viscosity -nu(y) Delta U the identity has no such sign conclusion), and viscous states are never
   Euler candidates.
7. Theory. The rotating analogue of the non-rotating exclusion argument is open: its Bernoulli function loses
   monotonicity along W through the sign-indefinite rotation term (section 2, item 8). No complete obstruction covering
   the searched target class has been supplied.
8. Radial decay. On eight primary exports the last radial coefficient is 1.4e-3 to 2.9e-2 of the toroidal block maximum
   (theory route); this does not separate approximation of non-integer powers from core under-resolution.
9. Independent pressure, leg R2. The accepted R2 pressure result (6.9 (c)) gives no pressure accuracy, no
   moment-study verdict, no source refinement verdict, no eligibility of the constrained models, no independent
   Newton agreement, no domain momentum norm of the registered specification, no exact profile and no label A, and
   its comparison with the earlier leg R1 is reported in 6.9 (r), as a difference of saved pressure models only.
10. Independent pressure, legs R3 and R4, and the final consumers. Leg R3: the second R3 source attempt completed and
   was accepted as finite source data of leg R3 only (6.9 (f)); its two readers passed and were accepted in their
   scope; the R3 pressure run completed and was accepted as a completed, internally consistent pressure result on the
   32 local targets, which gives no pressure accuracy, no exterior uncertainty and no independent pressure agreement
   (6.9 (g)). Leg R4: the R4 source, an angular sensitivity leg relative to R2, was launched at 2026-10-27T20:04:37Z
   under a dated disk plan (6.9 (h)); it completed at 2026-10-27T23:20:45Z and was accepted as finite source data of
   leg R4 only; its two readers, released at 2026-10-27T23:31:05Z, confirmed all 3259 and all 256 of their checks and
   were accepted at 2026-10-27T23:42:21Z as finite internal consistency of leg R4 only; its pressure run was released
   at 2026-10-27T23:42:46Z, completed at 2026-10-27T23:45:24Z with return code 0 and was accepted at
   2026-10-27T23:55:38Z as a completed run; its saved-output reader passed with all 332 of its checks confirmed, and
   the lead accepted R4 at 2026-10-28T00:08:29Z as a completed, internally consistent pressure result on the 32 local
   targets, which gives no pressure accuracy, no exterior uncertainty and no independent pressure agreement (6.9
   (h)). The low-mode moment guards of the five source legs passed, so the constrained pressure models are eligible
   under the registered rule; this is an operational status of the numerical source representation, accepted at
   2026-10-28T00:41:00Z, and it gives no exact moment cancellation, no error bound and no pressure accuracy (6.9
   (q)). The comparisons reducer compared the saved pressure models of the five legs at the 32 targets and on their
   19-point exterior subset in all 72 registered contexts; every gradient and pressure ratio passed the operational
   threshold 1e-7, the largest at most 5.6e-14 and 7.7e-14, so the saved models agree with each other to rounding
   level at these points. This was accepted at 2026-10-28T01:25:37Z; it gives no pressure accuracy and no error
   bound, and the reference residual RMS(A_num + grad P_b), built from the supplied velocity operands, is itself
   about 0.1455 on the 32 targets (6.9 (r)).
11. Independent Newton agreement. It was not run, because its registration needs the reviews of the Group B controls,
   whose sequence closed after its first control failed for an infrastructure reason, and because even a recovered
   sequence would have left Newton production 3700.231505514123 GPU-seconds short with full caps (6.9 (i), (j)).
12. Disk accounting. The bounded du wrapper absorbed every vanish race observed in one finite control of about 62 s,
   which gives no failure-rate bound, and the standing guard's own retry count is not observable, so retry lines
   counted in the logs are emitted counts, not complete counts (6.9 (e)).
13. Single-command validation. The one clean-process run of the full validation command in the accompanying
   artifacts on the saved start file of the degree-10 rung at c_l = 0.45, omega = 1, omega/c_l = 20/9 (6.9 (m))
   reproduced 81 of the 88 compared saved
   diagnostics within 1e-6 relative, including the two holdout rho_u^max values cited in this report. It shows only
   that the saved diagnostics reproduce from a clean process, it is no new evidence about the state, and it is not
   shown to be the registered clean-process check of the final selected package in item 1. The cause of the
   difference of about 5 per cent in rho_u_bal on the training and holdout grids is open, and no rho_u_bal value is
   cited.
14. Interruption and resume. The repeated resume test (6.9 (l)) shows that the deployed worker v2.4 resumed from its
   checkpoint after kill -9 and completed one disposable two-start job; it is one software test, not evidence about
   any state, and it gives no failure-rate bound.
15. Supervisor recovery. The stop-and-restart test of the primary route's supervisor (6.9 (n)) ran once on
   2026-10-28, with no job pending or running, and met its pass criteria: the restarted supervisor was alive and
   heartbeating, the queue counts were unchanged and the 2405-row ledger was byte-identical. It is a software test of
   stop and restart, not evidence about any solver state, and it gives no failure-rate bound.
16. Exactness of the selected field. The represented field of the selected state has a nonzero axial vorticity
   residual at the origin, enclosed in exact arithmetic (6.9 (s)), so it is not an exact profile. No exact profile,
   for any c_l and omega, has its velocity, vorticity and the gradients of U_3 and Omega_3 at the origin all within
   1/16 of those of this field, before or after a positive dilation and a rotation about the axis. This pointwise
   comparison uses second derivatives at the origin. A weak form of the momentum equation also gives a ball around
   the origin and a positive amount, the same for every exact profile with 2/5 <= c_l <= 1/2 and any omega, by which
   each such profile differs from this field in the L^2 norm and in the maximum magnitude of the velocity difference
   over that ball, before or after a positive dilation and a rotation about the axis; neither the radius nor the
   amount has been evaluated. Whether an exact profile lies near this field in the field distance of 6.7 is open, and
   no bound on the residual away from the origin is computed.
