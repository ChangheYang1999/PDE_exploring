# Gate II.4 verdict, revision r2 (revised 2026-10-27T11:01:10Z; r1 2026-10-27T10:44:15Z; assembled 2026-10-27T10:07:45Z; verifier re-audit requested by 2026-10-27T15:30Z)

Verdict as assembled. Only explicitly sourced rows are readings. Steering only; nothing here changes an acceptance
threshold of SPEC section 3. Values are marked primary-reported, independent or theory route, and c_l, omega and
omega/c_l are written explicitly in every row. The assembly re-checked every line that carried an assembly bracket in
the draft. Schedule: note d128 AV (2026-10-26T00:10:09Z).

Revision r2 (2026-10-27T11:01:10Z). This revision answers the verifier's re-audit of r1 (report_reviews/
20261027T104710Z_II4_gate_r1_audit/REVIEW.md, items R1-1 to R1-3). The r1 file (sha256
5c1fc7e4378a328efc896649388811af9a156b1500f2092ea9f74074e0fa6499) is kept unchanged; this file replaces it as the gate text. No value, threshold,
label or selection changes. Changes:
- R1-1 (sections 1, 3 and 5): the closure-met state at omega = 1 is ordered ahead only of the nest8nk8 continuation
  among the five states compared in note d128 KH, not among all states at the same parameters. The verifier named the
  section 5 sentence; the same wording in sections 1 and 3 is scoped in the same way. Its wider same-parameter
  ordering (ahead of six degree-6 states under both predicates and of nest6 p1 under 7.3b only) is in section 3.
- R1-2 (header, section 2 and section 5): the r1 all-pairs script also loaded the excluded diagnostic entry
  s11_L6_cl0.45_om+1.0_fixed_cl1ftol. With it removed the census is 60 saved readings and 642 same-parameter pairs, with
  the same 51 predicate differences and no pair ordered by v3 without the same 7.3b ordering; 20 (not 21) saved readings
  are ahead of the all-mode arm froms7c. No other relation quoted in r1 involves the excluded entry.
- R1-3 (section 5, D10): the figure 2.34e-15 is the largest relative change of the shell non-axisymmetric fractions,
  not of all angular comparisons.
- r2 check file (tmp/shift12/gaterev, script / output sha256 prefixes): census_r2.py 2e537885 / .out 70739117.

Revision r1 (2026-10-27T10:44:15Z). This revision answers the verifier's audit of the assembled gate (report_reviews/
20261027T101015Z_II4_assembled_gate_audit/REVIEW.md, items GATE-1 to GATE-5 and the D10 count). The assembled file
(sha256 7b9f60ccc22ac7ebc9d9098bb66a0b149367784af864f5295a298ec3288918c1) is kept unchanged; this file replaces it as the
gate text. No value, threshold, label or selection changes. Changes:
- GATE-1 (section 3 table): the omega = 1 closure-met state is ordered ahead of the nest8nk8 continuation among the
  compared states; the sentence "not ordered against any state of the branch" is withdrawn.
- GATE-2 (section 2 conditions): all four holdout angular counts are stated, and the quadrature condition applies
  whenever the actual quadratures differ, which includes the same-degree relations of row 10.
- GATE-3 (section 1): the campaign-wide exclusion of a divergence-penalty representation is withdrawn and replaced by
  the statement about the inspected representations; per-state formulation lineage stays open (SOL-4).
- GATE-4 (section 3, omega = 1 branch): the producer's four failed angular-consistency checks, its 90 withheld
  per-set readings and the absence of a floating-point error bound or tail estimate are stated beside the reader count.
- GATE-5 (section 2): lead decision on the ordering predicate (below, before the shortlist table). Every relation
  quoted outside the table that the shortlist predicate v3 does not also order is marked "under 7.3b only".
- D10 count (section 5): the 342 passing records per family are itemized, and the two small numbers are labelled as
  relative changes, with the absolute e_F difference.
- Lead scope corrections. The lead re-checked the quoted relations (the 17 pairs cited in the assembled text, and
  every relation of the two nest10 states, the 8-channel states, the two closure-met states and the two all-mode arms)
  against the 60 saved arm readings of states at matching (c_l, omega) (revision r2 removes the excluded diagnostic
  entry that the r1 script also loaded), with exact rational comparisons under both predicates
  ("r1 check" below; standard library only; the files are listed in the last item). Five statements, some repeated in several sections, were too broad and are
  scoped: the 8-channel states are ahead of seven and five degree-6 states (were "ahead of no comparator", sections 1
  and 2 and the section 3 table); nest10 at omega = 0.3 has the lowest holdout of the four GU states, not of the
  branch (section 3); the omega = 1 all-mode arm is ahead of three degree-6 states (were "ahead of no state",
  sections 3 and 5); the omega = 0.3 all-mode arm is ahead of four further degree-6 states (section 5); the
  omega = 0.3 closure-met state is ahead of six degree-6 states (section 3 table).
- r1 check files (tmp/shift12/gaterev, script / output sha256 prefixes):
  all_pairs.py 5f0ad91d / .out b3513407;
  predicates.py 9d281eeb / .out 1d3149bf;
  cited_pairs.py e0074622 / .out 629e7c9f;
  cited_pairs2.py debfcf93 / .out 11509942;
  nk8_ahead.py 41697416 / .out 44457145;
  allmode_rel.py 20b71b30 / .out bcb3ef47;
  nest10_rel.py 500cd159 / .out 31871bd3;
  closure_rel.py c720388f / .out 54ad4300;
  closure_fail.py be9d7284 / .out 17a5010e;

## 1. Gate item (PROMPT II.4)

Either a small set of refinement-stable candidates with independently checked pressure, or a precise failure map
identifying which assumptions or numerical mechanisms prevent convergence. Expected outcome: failure map (no Tier R
candidate with independently checked pressure exists as of 2026-10-26T11:00Z).
- Candidates: none (re-checked at assembly, 2026-10-27T10:07:45Z). No state meets Tier S (SPEC 9), and no Tier R
  candidate with independently checked pressure exists. The lowest primary-reported holdout rho_u^max is 0.02983 /
  0.03130 (the degree-8 closure-met state, c_l = 0.45, omega = 1, omega/c_l = 20/9; not evaluated independently; 2.98
  and 3.13 times the bound of 1e-2). It is not ordered ahead of nest10, because its core-set a_max is 2.02 times that of
  nest10; among the five states compared in note d128 KH, it is ordered ahead only of the nest8nk8 continuation
  (primary-reported, order record 90f7e94e); section 3 gives its wider same-parameter ordering. The lowest independently checked holdout values
  are 0.04082 / 0.04142 (St1, same parameters, 4.1 times the bound).
- Stagnation tests named by PROMPT II.4, each with its arm and reading:
  - alternative bases. Primary route (toroidal-poloidal solid harmonics times shifted Chebyshev radial functions):
    degree ladders 2, 4, 6, 8 and 10 at c_l = 0.45 with omega = 1 (omega/c_l = 20/9) and omega = 0.3
    (omega/c_l = 2/3), and to degree 8 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7; radial ladders with 24 and 32
    radial functions; 4 and 8 far-correction channel functions (nest8nk8 and its continuation). Independent route, a
    different basis (twisted Cartesian vector potentials, U = curl A): degrees 2 to 6, degrees 8 and 10 in machinery
    tests, and the D10 descent at degree 10. Readings: both c_l = 0.45 branches are floored under rule R2 at degree 10
    with 4 channel functions (q_10 = 0.946 / 0.950 at omega = 0.3 and 0.961 / 0.957 at omega = 1); the c_l = 0.42
    branch and the D6 lineage are floored at degree 8; the 8-channel states lower the shell holdout (0.03995 / 0.04040
    for the continuation, primary-reported) at a higher core-set a_max and are ordered ahead of no degree-8 or degree-10 state (they are ahead of seven and
    five degree-6 states of their branch, under both predicates; r1 check). The
    independent route's best fresh values are 0.0574 / 0.0541 (degree 6, c_l = 0.45, omega = 0.3, omega/c_l = 2/3) and
    0.061923 / 0.068983 (the D10 terminal state, same parameters). The degree steps of both routes stopped at their
    iteration or time limits, so the floors mix truncation with budget;
  - primal versus curl formulations. Both velocity representations are divergence-free by construction (primary:
    U = curl(T y) + curl curl(S y); independent: U = curl A). The far-field correction channels enter the same
    potentials (primary: B into T, D and E into S; independent: every channel is a vector potential), so they are
    divergence-free by construction (lead source review and the accompanying solenoidal-representation proof; saved primary div U RMS readings below 2.6e-14, numerical observations, not an enclosure). The residual formulation was varied in the primary
    route: momentum residual R_u (534 of the 892 Stage I result records), vorticity residual R_Omega (357; one record
    used both), and the combined
    vorticity-momentum arm S10 with weights 1 and 10 at c_l = 0.45 with omega = 1 (omega/c_l = 20/9) and omega = 0.3
    (omega/c_l = 2/3); four runs, complete, primary-reported. None improves on its start. At weight 1 the holdout
    rho_u^max rose to 0.2036 / 0.2065 (omega = 1) and 0.2484 / 0.2491 (omega = 0.3); at omega = 0.3 the curl
    residual fell (rho_Om^max by 5.8 per cent, sigma_Om by 28 per cent) while the momentum residual rose 3.7-fold. At
    weight 10 both runs collapsed toward the trivial state (holdout 0.98 and 1.00). Failure-map interpretation
    (primary, not a proved cause): amplitude instability. Both inspected velocity representations impose div U = 0 analytically
    through vector potentials, including their correction channels. Complete per-state historical formulation lineage
    remains open (SOL-4). The computed divergence is the finite reading stated above;
  - randomized continuation. No randomized parameter continuation was performed (re-checked at assembly,
    2026-10-27T10:07:45Z: the numerics run folders changed after 2026-10-26T22:00Z belong to the S5 R0 refit and the
    degree-8 control, the S14 degree-4 and degree-6 jobs, the Stage III smoke and preparation jobs, S15 and the
    registered Stage III jobs R1, R2 and R3; the numerics queue holds no pending job). Randomization entered as seeded
    starts: in the primary route 243 of the 892 Stage I result records carry the random initializer tag (continuations
    and reused initializers occur elsewhere in that census), and the three degree-2 jobs have 60 starts per point from
    six initializer families (ten each tagged random, tail, nonaxi, poloidal, toroidal and affine_core) at c_l = 0.45
    with omega = 0.3 and 1 (omega/c_l = 2/3 and 20/9) and at c_l = 0.42, omega = 0.3 (omega/c_l = 5/7); the best
    endpoint of each job, selected by the larger of the two family values, has holdout rho_u^max 0.10752 / 0.10709,
    0.11328 / 0.11661 and 0.10500 / 0.10875 respectively; in the independent route 282 random-initializer records to
    2026-10-25T05:35Z (of 540 records, with 440 distinct root initializer specifications, which does not establish 440
    independent fields). It also entered as single perturbations of saved states (an m = 1 perturbation of 10 per cent
    of ||U||, all-mode class and S7 (c)). The parameter paths were deterministic warm-start continuations: the S4 omega
    path at c_l = 0.45 (omega = 0.1, 0.2, 0.5 and 2.0, omega/c_l = 2/9, 4/9, 10/9 and 40/9; every arm failed the plateau
    test, no floor or trend in omega), the free (c_l, omega) runs and the warm starts in c_l at omega = 0.3. The S14 arm
    (fresh all-mode starts at degree 4, eight per point, two seeds each from the random, nonaxi, poloidal and toroidal
    initializer families) is a fresh-start arm, not a continuation; its stage (i) reading is in the
    unrestricted-azimuthal-modes item below. The seeded perturbation starts of the Stage III R1 runs are registered
    replication runs, not a Stage II arm. They were released by a dated lead decision (note d128 LI,
    2026-10-27T02:04:53Z) that allowed launch only after the last Stage II numerics job, S15, had ended (JOB DONE
    2026-10-27T06:52:18Z); the first began at 2026-10-27T07:03:20Z. Their readings are not used in this gate. The gain
    to 0.05227 / 0.05368 in the S11 closure-row ladder at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 depended on the
    excursion path of an unsafeguarded lagged iteration; it is not a randomized continuation;
  - unrestricted azimuthal modes. Primary route, primary-reported: the all-mode class S4 at degree 6, three arms of one
    start each (two registered S4 arms and the S7 (c) degree-6 m = 1 seeding arm). The holdout ended between 2.8 per
    cent below and 4.7 per cent above the even-class degree-6 state of the same branch; the odd-mode velocity fractions
    were 8 and 28 per cent of ||U|| in two arms and 3.5 per cent in the third (fractions on the finite training grid,
    not whole-space fractions). At degree 4, S7 (c) met the sampled swirl condition through odd modes without lowering
    the residual. S14, fresh all-mode starts at degree 4 from four initializer families at four parameter points, (c_l,
    omega) = (0.45, 0.3), (0.45, 1), (0.42, 0.3) and (0.48, 1), omega/c_l = 2/3, 20/9, 5/7 and 25/12; eight starts per
    point, two seeds per family, fixed before launch. All 32 ended at the 300-iteration limit with holdout rho_u^max
    between 0.25 and 0.84 on both families and odd-m energy fractions between 0.13 and 0.96 (training grid, unweighted);
    none of the 32 starts meets the registered stationarity diagnostic (absolute V10 at most 1e-3), and all fail Tier S.
    The registered 4 GPU-h cumulative whole-job cap was exceeded (18272 s, about 5.08 h; the starts were not stopped
    when it was passed); the readings stand as data (verifier saved-reading audit 2056 checks passed, its one failed
    check being this cap; lead notes d128 KK, KL and KM). The registered filter promoted start 6, 5, 5 and 7
    respectively to degree 6. Stage (ii), primary-reported and lead-reviewed (notes d128 LD and LE; the verifier's
    saved-record audit of each of the three terminal readings gave 92 confirmed, 0 refuted and 4 registered open checks,
    which establishes the consistency of the recorded values, not an independent field measurement): each promoted start
    was continued at degree 6 with a 300-iteration limit and a 7200 s per-start time limit. The job at (0.48, 1), the
    one point without an even-class degree-6 comparator, was stopped before any reading under the registered priority
    rule of the 10 GPU-hour cumulative cap, so that point keeps only its degree-4 coverage reading. The other three
    stopped at the time limit after 259, 261 and 258 iterations at (0.45, 0.3), (0.45, 1) and (0.42, 0.3) respectively.
    Their holdout rho_u^max is 0.1646 / 0.1648, 0.2268 / 0.2115 and 0.2436 / 0.2486, that is 0.464 / 0.466, 0.897 /
    0.814 and 0.776 / 0.829 of the degree-4 values. V10 is 0.104, 0.0219 and 0.0153; none meets the registered
    stationarity diagnostic (absolute V10 at most 1e-3). No L4-to-L6 collapse flag is set (N_core, N_F, e_core and e_F
    changed by factors of approximately 1.00 to 1.20). The odd-m energy fractions (training grid, unweighted) are 0.359,
    0.767 and 0.942, against 0.371, 0.791 and 0.951 at degree 4. Under 7.3b the even-class degree-6 state of the same
    point is ahead in all three cases, with holdout ratios 2.462 / 2.441, 4.925 / 4.568 and 3.798 / 3.474, conditional
    on the primary core flags and the common sigma_Om quadrature. The budgets differ: each comparator had a
    600-iteration limit and stopped at it, except at (0.45, 0.3), where it stopped at its time limit after 413
    iterations; the comparators' code versions are not recorded. One incident concerns the job at (0.42, 0.3). A second
    process ran on the same device for about 70 s (23:26:31Z to 23:27:42Z, peak device memory 43.0 GB). Its effect on
    this time-limited trajectory, including the number of iterations completed, is not established. The four degree-6
    jobs used 26007 s of whole-job time by their start and end stamps (829 s for the stopped job), 26027 s with a
    cancelled 20 s retry, within the 36000 s cap. None of the three states is a candidate. A separate bounded
    continuation of the (0.45, 0.3) state, S15 (c_l = 0.45, omega = 0.3, omega/c_l = 2/3; degree 6, 16 radial functions,
    all-mode basis), ran from 2026-10-27T01:36:12Z to its end at 06:52:18Z. This continuation was decided after the
    stage (ii) cost histories had been seen, under a criterion recorded before the stage (ii) readings existed
    (time-limit stop, V10 at least 0.05, no collapse flag). It stopped at its 600-iteration limit (LM 18026 s against
    its 19800 s limit; whole job 18966 s against its 21600 s cap). Reading, primary-reported (lead review note d128 NE;
    the verifier's receipt of 2026-10-27T07:33:55Z accepts it as coverage only, under all of the review's G7 wording,
    with no independent field validation): the holdout rho_u^max is 0.09767 / 0.09507, that is 0.593 / 0.577 of the
    stage (ii) end state; the holdout rho_u^max ended at 1.461 / 1.408 times that of the even-class degree-6 state s55s0
    at the same c_l = 0.45 and omega = 0.3, after 859 against 413 LM iterations; no evidence that odd modes lower the
    residual materially; odd-mode states are not excluded. V10 is 0.0194, so the registered stationarity diagnostic
    (absolute V10 at most 1e-3) is not met. No collapse flag is set (N_core, N_F, e_core_holdout and e_F changed by
    factors 0.977, 1.034, 1.008 and 1.012 from the stage (ii) end). The odd-m energy fraction (training grid,
    unweighted) is 0.392, against 0.359 at the stage (ii) end. Under 7.3b the even-class state s55s0 is ahead (holdout
    ratios 1.461 / 1.408, core-set sigma_u^max ratio 1.836, sigma_Om ratio 2.673, core-set a_max ratio 1.224),
    conditional on the primary core flags and the common sigma_Om quadrature. S15 is not a candidate. Its reading is a
    coverage reading at this budget, not evidence against odd-mode profiles. Independent route: the all-mode step-8
    battery V5 at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 is complete (note d128 FH; producer 2307 checks, 0 failed;
    reader 29374 passed, 55 strict comparisons of a cancelled energy-identity defect retained as failures); the step-8
    state has rho_u^max 0.41029 / 0.41483 over its domains (radius 4096 for the standard family, 4096 sqrt(2), about
    5792.6, for the half-offset family); the strict failures stay failures, and their small absolute size is not a
    pressure enclosure. For the present Stage II attempt with the Euler objective, this eight-step run and its V5
    battery are the accepted independent all-mode result: no longer solve, omega = 1 arm or repair was released (note
    d128 EV) and note FH ruled out a V6, so a broader two-parameter, multi-start Stage II independent all-mode arm is
    unexecuted (re-checked at assembly: no dated release and no result after note FH). The route's Stage I all-mode runs
    are separate coverage records (section 3.2). These arms give no evidence that odd modes lower the residual
    materially; they do not exclude odd-mode states.

## 2. Shortlist (best state of each branch group)

Source: the numerics shortlist v3, reports/STAGE1_SHORTLIST.md (sha
528338c3f498acf42e8dba7101443e57e2de1fba7348e1b33f6af1128cf9e79f) and its JSON (sha
ea25da93692aa5ae996b85d2f7c84ab997a7f0ca6b76c40527ed8508af8fc7d6), generated 2026-10-27T08:28Z by
scripts/shortlist_v3.py all (sha 9fbdbf7a; accepted as run in note d128 NM, metadata refutations accepted in note d128
NT). v3 differs from v2 fe54e62c only in the docstring and header string (lead review note d128 KK), and v2 added only
the lineage class 'control' (lead review note d128 KH). This gate cites from v3 only its row values and its order
relations. Its header counts, 660 ranked nontrivial states and 235 descriptor bins, are primary-reported; the bins are
branch-key classes, not shown to be distinct branches. The generator keeps the lowest state of each bin and prints the
first 12 bins, so the table is not a complete frontier: nest10 at c_l = 0.45, omega = 1 shares the bin of row 1 and is
not a row, and no all-mode state is a row. Every value is primary-reported, on the common holdout shells (23 shells on
both families, 138 radii). The primary core-resolved flag is set on every row (primary-reported, not independently
verified). The training normalization is all5far on every row except row 10 (all5).

Conditions (verifier audit II4-GR6). The shortlist is provisional, and no row or representative is a candidate. Every
relation between states whose holdout quadratures differ is conditional on the common sigma_Om quadrature leg (the
holdout angular count is 6380 at degree 10, 4700 at degree 8, 3276 for the degree-6 rows other than row 10, and 1008
for row 10, which is also degree 6; every row has 138 radii), so the condition also applies to the same-degree
relations of row 10, and every relation is conditional on the primary core-resolved flags that enter the core-set comparisons. The one measured exception to the quadrature condition, the
nest10 / cont150 sigma_Om pair on its stated finite domains (note d128 IT), involves no row. A single-level a_eff does
not close core resolution. Row 2 is the end state of a diagnostic continuation that the lead ruled is not a state (note
d128 GU); its values are not quoted and its relations are not used. Ordering predicate (lead decision, revision r1, answering
verifier item GATE-5). SPEC 7.3b orders X ahead of Y when X has the lower holdout rho_u^max on both shell families and
X's sigma_u^max, sigma_Om and a_max each exceed Y's by at most 10 per cent, with sigma_u^max and a_max taken over the
core sets of v1.21 (b). That is the five-ratio reading (two holdout inequalities and three ratio guards: core-set
sigma_u^max, sigma_Om and core-set a_max) of order_73b.py, and it is the 7.3b relation of this gate. The shortlist
generator v3 applies the two holdout inequalities and eight ratio guards (its fields sigma_u_max, sigma_u_max_half,
sigma_Om, a_max, a_max_half, sigma_u_max_core, a_max_core and a_max_core_upper). Its guards contain the three of 7.3b,
so every v3 ordering is also a 7.3b ordering in the same direction, while v3 can leave unordered a pair that 7.3b
orders. r1 check, recounted at r2: over the 642 same-parameter pairs among the 60 saved arm readings of states (the
excluded diagnostic entry s11 cl1ftol removed; with it the raw inventory is 61 entries and 671 pairs) the two
predicates differ on 51 pairs, and no pair is ordered by v3 without the same 7.3b ordering. Among the other 11 rows of the table, v3 orders
26 of the 55 pairs and 7.3b orders 30. The four extra 7.3b pairs are row 4 ahead of rows 6, 9 and 12 and row 9 ahead
of row 12; v3 fails them only on its non-core guards (a_max, a_max_half or sigma_u_max_half), with ratios between
1.108 and 1.134. The 'ahead of rows' and 'behind rows' columns and the 'behind row k' statements of section 5 are the
v3 relation as printed. The accepted v3 artifact is not regenerated and no rule changes. Every other relation in this
gate is stated under 7.3b and is marked 'under 7.3b only' where v3 does not order the pair.

| row | state | c_l, omega, omega/c_l | degree, radial, channel functions | holdout rho_u^max std / half | holdout rho_nl^max std / half | sigma_u^max std / half (core sets) | a_max std / half (core sets) | sigma_Om | ahead of rows | behind rows |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | nest8_L8_cl0.45_om+1.0_fixed_cl1_sgcont150b | 0.45, 1, 20/9 | 8, 20, 4 | 0.02983 / 0.03130 | 0.3307 / 0.2903 | 0.3577 / 0.3409 (0.5055) | 0.4463 / 0.4246 (1.206) | 0.3965 | 3, 5, 7, 8, 10, 11 | none |
| 2 | s11_L6_cl0.45_om+1.0_fixed_cl1ftol | 0.45, 1, 20/9 | 6, 16, 4 | not quoted (not a state, note d128 GU) | | | | | not used | not used |
| 3 | nest8_L8_cl0.45_om+0.3_fixed_cl1 | 0.45, 0.3, 2/3 | 8, 20, 4 | 0.03739 / 0.03940 | 0.2665 / 0.2821 | 0.3883 / 0.3826 (0.6012) | 0.4861 / 0.4974 (1.435) | 0.4542 | 5, 7, 10, 11 | 1 |
| 4 | s5ctl_L8_cl0.45_om+1.0_fixed_R0p3_ctl | 0.45, 1, 20/9 | 8, 20, 4 | 0.04314 / 0.04288 | 1.148 / 1.08 | 0.4168 / 0.3648 (0.4425) | 0.4999 / 0.4381 (0.6431) | 0.4201 | 5, 7, 8, 10, 11 | none |
| 5 | d6w_L8_cl0.45_om+0.3_fixed | 0.45, 0.3, 2/3 | 8, 20, 4 | 0.04423 / 0.05432 | 1.455 / 1.45 | 1.824 / 1.388 (1.824) | 2.193 / 1.876 (2.193) | 1.377 | none | 1, 3, 4 |
| 6 | s9d_L6_cl0.45_om+1.0_fixed_bal0.000131342_corepin_naxpin_k0.1 | 0.45, 1, 20/9 | 6, 16, 4 | 0.04484 / 0.04433 | 0.3898 / 0.4159 | 0.4247 / 0.3742 (0.45) | 0.4511 / 0.3928 (0.6747) | 0.3925 | 7, 8, 9, 10, 11, 12 | none |
| 7 | s1nk_L6_cl0.45_om+0.3_fixed_Nk32 | 0.45, 0.3, 2/3 | 6, 32, 4 | 0.05078 / 0.07011 | 0.2251 / 0.2081 | 1.795 / 1.52 (1.795) | 1.806 / 1.711 (1.806) | 1.304 | 10 | 1, 3, 4, 6 |
| 8 | s9d_L6_cl0.45_om+0.3_fixed_bal0.000117976_corepin_naxpin_k0.1 | 0.45, 0.3, 2/3 | 6, 16, 4 | 0.05227 / 0.05368 | 0.5492 / 0.5314 | 0.4221 / 0.4031 (0.6156) | 0.4822 / 0.4867 (1.19) | 0.4604 | 10, 11 | 1, 4, 6 |
| 9 | s4om_L6_cl0.45_om+0.5_fixed_from1 | 0.45, 0.5, 10/9 | 6, 16, 4 | 0.05360 / 0.05781 | 1.089 / 1.122 | 0.4528 / 0.4606 (0.5117) | 0.4477 / 0.4558 (0.6188) | 0.4497 | 10, 11 | 6 |
| 10 | d6scan_L6_cl0.47_om+0.3_fixed | 0.47, 0.3, 30/47 | 6, 16, 0 | 0.05552 / 0.07937 | 1.861 / 1.925 | 2.046 / 1.592 (2.046) | 1.86 / 1.67 (1.86) | 1.197 | none | 1, 3, 4, 6, 7, 8, 9 |
| 11 | s12_L6_cl0.42_om+0.3_fixed_rl3 | 0.42, 0.3, 5/7 | 6, 16, 4 | 0.05664 / 0.06078 | 0.5436 / 0.5345 | 0.5126 / 0.5087 (0.7698) | 0.7893 / 0.8212 (2.118) | 0.6498 | none | 1, 3, 4, 6, 8, 9 |
| 12 | s5ctl_L6_cl0.45_om+0.3_fixed_R0p3_ctl | 0.45, 0.3, 2/3 | 6, 16, 4 | 0.06114 / 0.06095 | 1.138 / 1.203 | 0.4263 / 0.4064 (0.582) | 0.4463 / 0.452 (1.019) | 0.4506 | none | 6 |

Representatives (primary-reported unless marked; full sha256 of each job's saved state file starts/start_000.pt and of
the export files where one exists, rehashed at assembly):
- nest10, primary, c_l = 0.45, omega = 1, omega/c_l = 20/9; degree 10, 24 radial functions, 4 channel functions;
  training normalization all5far; 300 iterations (iteration limit), V10 0.0052; holdout 0.041954 / 0.041450; rho_nl^max
  1.129 / 1.126; sigma_u^max 0.4048 / 0.3699 (core sets 0.4236); a_max 0.4934 / 0.446 (core sets 0.5958); sigma_Om
  0.4214; a_eff 0.2647 at one level; core-resolved flag yes (primary; core resolution open). Not a row (it shares the
  bin of row 1). Ordered ahead of cont150, the degree-8 control (row 4), nest8 p0, nest6 p0 (under 7.3b only; v3
  fails on a_max, ratio 1.139) and the all-mode arm froms7c; unordered against nest8nk8, its continuation and the
  closure-met state (all conditional). Verifier:
  saved-data reader 741 / 0, field transfer reproduced to 1.8e-13, common sigma_Om 0.4213 on the finite domain (note
  d128 IT), fixed-field core geometry (note d128 JX; not the core-resolution leg). State
  b2c111728a215c985bc0aaa9c96bcb3df77afd912f02de0dfa132adab4c7ee64; export samples
  ccce6d7168444983b86f668a592f7dabd756a92f9250744006aaa8da1511c531; export coefficients
  ffa53c98481c5f9517a9f57303d22ce16cae982965b8a98a281b3ca2aece0731.
- nest8nk8 continuation (cont150 of nest8nk8), primary, same parameters; degree 8, 20 radial functions, 8 channel
  functions; training normalization all5far; 150 iterations (iteration limit); holdout 0.039953 / 0.040396; rho_nl^max
  0.8319 / 0.891; sigma_u^max 0.4151 / 0.369 (core sets 0.6318); core-set a_max 1.281; V10 0.0046; verifier: saved
  ordering audit 75 / 0 (note d128 JV); ordered ahead of no degree-8 or degree-10 state, ahead of five degree-6 states (s10 both10,
  s12 rl3, s14b s5, the all-mode arm froms7c and s7c m2ecore0.25) and behind the closure-met state, under both
  predicates (r1 check); retained with nest8nk8 (0.04082 / 0.04141, St1,
  independently checked) as a parallel state. State db295a45f929d890113d7e8a1f5af21623a2b7e661fe487716efeb1f26b87855;
  nest8nk8 state a5b158520bbc9cf74ef02e8c3e32db1f3c5972a176e7eeb700d63c42fdac94d0.
- closure-met degree-8 state nest8_L8_cl0.45_om+1.0_fixed_cl1, primary, same parameters; degree 8, 20 radial functions,
  4 channel functions; training normalization all5far; ftol stop after 91 iterations; holdout 0.029828 / 0.031302;
  rho_nl^max 0.3307 / 0.2903; sigma_u^max 0.3577 / 0.3409 (core sets 0.5055); a_max 0.4463 / 0.4246 (core sets 1.206);
  sigma_Om 0.3965; a_eff 0.2475 at one level. Core-set a_max 2.02 times and core-set sigma_u^max 1.19 times nest10's;
  not evaluated independently. Among the five states compared in note d128 KH, it is ordered ahead only of the
  nest8nk8 continuation (order record 90f7e94e), and it is unordered against nest10, nest8nk8 and the degree-8
  control. Over all saved readings at these parameters it is also ahead of six degree-6 states (s10 both10, s12 rl3,
  s14b s5, the all-mode arm froms7c, s7c m2ecore0.25 and s9d k100) under both predicates, and of nest6 p1 under 7.3b
  only (r1 check). Row 1 is its safeguarded continuation sgcont150b, which accepted no step; its end state is
  the aligned parent to rounding on the worker grid (note d128 IX; the principal holdout and enstrophy residual values
  are reproduced, sampled extrema differ by up to 8 per cent). State
  62a6dda02ebf13ea7d6ae99d6171776a54ac9a86bd5bf084f4278d4fb47c1dc4; sgcont150b end state
  2b5194cbb726fd986f30cfb92101e02fb97d323fa64fff70ffe22adc81d3e67a.
- nest10, primary, c_l = 0.45, omega = 0.3, omega/c_l = 2/3; degree 10, 24 radial functions, 4 channel functions;
  training normalization all5far; 300 iterations (iteration limit), V10 0.0084; holdout 0.056501 / 0.056453; rho_nl^max
  2.638 / 2.672; sigma_u^max 0.3896 / 0.3852 (core sets 0.5982); a_max 0.7335 / 0.681 (core sets 1.12); sigma_Om 0.4224;
  a_eff 0.2995; core-resolved flag yes (primary); verifier: saved-scalar reader (note d128 HC). State
  dbc0c75a67b0b9b93f9c706e8dddf06bade4108afa33f1d8109fedae55afdffe; export samples
  2677d66ca25cf07d091d5cb69b28a46f767613bbe17bd829b361b8bcfed730a0.
- closure-met degree-8 sibling nest8_L8_cl0.45_om+0.3_fixed_cl1 (row 3), primary, c_l = 0.45, omega = 0.3, omega/c_l =
  2/3; degree 8, 20 radial functions, 4 channel functions; training normalization all5far; ftol stop after 123
  iterations; holdout 0.03739 / 0.03940; rho_nl^max 0.2665 / 0.2821; sigma_u^max 0.3883 / 0.3826 (core sets 0.6012);
  a_max 0.4861 / 0.4974 (core sets 1.435); core-set a_max 1.21 to 1.39 times that of its four comparators (its own
  degree-6 start, St7a, St7b and the degree-10 rung), so ordered ahead of none of them. In v3 it is ahead of rows 5, 7,
  10 and 11 and behind row 1. State 260776d2015fb651ee71a47e3c58ca236581585a544f03ff24a4c57758117137.
- structurally different primary state: the all-mode state froms7c, selected in section 5 (values and hash there).
- D10 terminal state, independent route, c_l = 0.45, omega = 0.3, omega/c_l = 2/3; degree 10, radial 5 (2130
  coefficients); fresh holdout 0.061923 / 0.068983 (the route's own fresh battery, 2667 of 2668 checks passed);
  rho_nl^max 0.071650 / 0.091422; core-set sigma_u^max 2.3277; core-set a_max 4.0927; sigma_Om 2.0623; single level, so
  the a_eff leg is not evaluated. Terminal arrays c79a8741dd2f53d8f68924face65465ac8e61eb7e06390a91066b6199b346b43;
  terminal coefficient bits 4bb97660d0467e271283870028c8e6443848a0e200fe2d467fac6c1291029708 (note d128 GR); terminal
  battery results c447659d066a400e1fa8ad866c280861c32700ea9237688250ca1093e55b789c. Its non-axisymmetric content is read
  in section 5.

## 3. Failure map (registered format, reports/stage2_plan_draft.md section "Failure map")

One row per arm and branch; "not measured" where a column was not measured; "incomplete at II.4" with the last
reviewed state for arms not read by 2026-10-27T12:00Z. Mechanism reading only from the registered list: core balance;
far balance; global balance; transport degeneracy; amplitude instability; budget-limited; aliasing; near-edge escape.
"Optimizer failure" is a statement about the search, never about existence.
Source of the primary-route rows: the numerics failure map as regenerated at 2026-10-27T00:09:47Z (sha 8d673e2b, 34
rows, every row with the 16 registered cells), with the lead defects list (sha 22c8aa5d) applied by the numerics and
re-checked row by row by the lead (19 checks passed, 0 failed). Two V10 values that the map gives only per arm were
read by the lead from the ledger rows. Holdout values are
rho_u^max on the standard / half-offset shell families. "Iteration limit" and "time limit" mean that the registered
budget ended the run. V10 is the relative objective decrease over the last tenth of the iterations. A row meets the
registered stationarity diagnostic only if the absolute value of V10 is at most 1e-3, and even then this is an
operational label, not a gradient statement. A negative V10 means that the objective rose over the last tenth.
Mechanism cells give the numerics' readings from the registered list (primary-reported) unless a lead note is cited.
A "budget-limited" entry is the lead's reading (3.4) for an arm that ended at its iteration or time limit with V10
above 1e-3; the regenerated map names it in no row. Its row for the (0.42, 0.3) ladder reads "not budget-limited";
that phrase is not used here, because that ladder's last level also ended at the iteration limit above the bound.
"No mechanism named" means that no registered mechanism is attached.

3.1 Primary route, condensed (one line per arm or branch; values primary-reported unless the status cell says
otherwise).

| Arm | c_l, omega, omega/c_l | Levels | Last holdout | Stop; V10 | Reading (registered list or registered rule) | Check status |
|---|---|---|---|---|---|---|
| nest ladder | 0.45, 1, 20/9 | L4 without correction channels; L6 to L10 with channel Nk 4 | 0.04195 / 0.04145 | iteration limit 300; 0.0052 | global balance; far balance; budget-limited. R2: floored at degree 10 (q 0.961 / 0.957) | saved-data reader 741 / 0 (notes HB, HI) |
| nest ladder | 0.45, 0.3, 2/3 | L4 without correction channels; L6 to L10 with channel Nk 4 | 0.05650 / 0.05645 | iteration limit 300; 0.0084 | global balance; far balance; budget-limited. R2: floored at degree 10 (q 0.946 / 0.950) | saved-scalar reader (notes GU, HC) |
| nest ladder | 0.42, 0.3, 5/7 | L4 without correction channels; L6 and L8 with channel Nk 4 | 0.06154 / 0.06718 | iteration limit 150; 0.0043 | global balance; far balance. R2: floored at degree 8 (two steps with q above 0.85; note AW) | primary-reported; degree-8 values read independently (report 5.4) |
| D6 lineage | 0.45, 0.3, 2/3 | L6 without, then with channel Nk 4; L8 with channel Nk 4 | 0.05682 / 0.05867 (lowest on the lineage 0.04423 / 0.05432) | iteration limit 300; 0.082 | core balance; global balance | primary-reported |
| nest8nk8 and its continuation | 0.45, 1, 20/9 | L8, channel Nk 8 | 0.03995 / 0.04040 | iteration limit 150; 0.0046 | far balance (partial gain); core balance (core/far trade-off: core-set a_max 1.53 to 2.15 times the comparators); budget-limited. Ordered ahead of no degree-8 or degree-10 state; ahead of seven (nest8nk8) and five (continuation) degree-6 states at these parameters, under both predicates (r1 check) | ordering audit 75 / 0 (note JV) |
| S10 combined formulation, weight 1 | 0.45, 1, 20/9 | L6 | 0.2036 / 0.2065 | iteration limit 300; -0.010 | amplitude instability (non-axisymmetric content lost). R11: the curl formulation gives no improvement | primary-reported |
| S10 combined formulation, weight 10 | 0.45, 1, 20/9 | L6 | 0.9812 / 0.9807 | iteration limit 300; 0.128 | amplitude instability (collapse to a near-trivial state) | primary-reported |
| S10 combined formulation, weight 1 | 0.45, 0.3, 2/3 | L6 | 0.2484 / 0.2491 | iteration limit 300; -0.019 | amplitude instability. R11: rejected (curl residual lower, momentum residual 3.7 times higher) | primary-reported |
| S10 combined formulation, weight 10 | 0.45, 0.3, 2/3 | L6 | 0.9989 / 0.9995 | iteration limit 300; 0.70 | amplitude instability (collapse toward the trivial state; the R10 (e) guards fail) | primary-reported |
| S11 closure rows | 0.45, 1, 20/9 | L6 | 0.04526 / 0.04457 | ftol after 19 iterations; 1.5e-6 | R12 (a) (note CV wording): the measured first-correction far balance is not what limits the residual at this resolution. No mechanism named | primary-reported |
| S11 closure rows | 0.45, 0.3, 2/3 | L6 | 0.05227 / 0.05368 | ftol after 50 iterations; 8.3e-5 | R12 (a), as above. The gain depended on the excursion of an unsafeguarded lagged iteration | primary-reported |
| S11 closure state at degree 8 | 0.45, 1, 20/9 | L8 | 0.02983 / 0.03130 | ftol after 91 iterations; 0.44 (ledger row) | far closure met (mismatch 2.7e-8). Ordered ahead of the nest8nk8 continuation among the compared same-parameter states, conditionally; unordered against nest10 (core-set a_max 2.0 times nest10's), nest8nk8 and the degree-8 control. Over all saved readings at these parameters it is also ahead of six degree-6 states under both predicates and of one more under 7.3b only (r1 check). No mechanism named | primary-reported |
| S11 closure state at degree 8 | 0.45, 0.3, 2/3 | L8 | 0.03739 / 0.03940 | ftol after 123 iterations; 0.070 | not ordered against nest10, the two nest8 p0 states, the all-mode arm, nest6 p0 or row 8 (core-set a_max guard fails, ratios 1.206 to 1.462); ahead of six degree-6 states of the S8p, S9d and S14 arms at these parameters, under both predicates (r1 check). No mechanism named | primary-reported |
| S12 radial-lambda rows | 0.45, 1, 20/9 | L6 | 0.04166 / 0.04428 | iteration limit 300; 0.062 | R13 (c), inconclusive (note CV): the normalized ratio fell while the weighted momentum RMS rose 23 per cent | primary-reported |
| S12 radial-lambda rows | 0.42, 0.3, 5/7 | L6 | 0.05664 / 0.06078 | iteration limit 300; 0.052 | R13 (c), as above (momentum RMS +25 per cent) | primary-reported |
| S9b balance rows, degree 4 | 0.45, 1, 20/9 | L4 | 0.07131 / 0.07217 | iteration limit 300; 0.019 | global balance tested: R10 (d), balances attained at 1.23 times the start's holdout, inconclusive | primary-reported; independent ratios 1.23173 / 1.23482 |
| S9b balance rows, D6 start | 0.45, 0.3, 2/3 | L6 | 0.2280 / 0.2439 | ftol after 22 iterations; 1.9e-7 | global balance tested: R10 (c), balances not attained, optimizer-limited, inconclusive | primary-reported |
| S9b balance rows, nest start | 0.45, 1, 20/9 | L6 | 0.4479 / 0.4471 | iteration limit 300; 0.67 | global balance tested: R10 (c), optimizer-limited, inconclusive | primary-reported |
| S9d balance-continuation chains | 0.45, 1, 20/9 and 0.45, 0.3, 2/3 | L6, four kappa steps each | 0.05297 / 0.05455 and 0.07143 / 0.07108 at kappa 100 | (0.45, 0.3): ftol after 72 iterations, 3.2e-6 | global balance tested: R10 (c), optimizer-limited, inconclusive (ruled rows below) | saved-scalar check (note GS) |
| S8 viscous continuation, free omega | 0.45, omega free from 1 (end 0.533); 20/9 at the start, 1.18 at the end | L4 | 0.8983 / 0.9097 | iteration limit 300; 0.013 | amplitude instability (the solve collapsed to the tail; omega drifted to 0.533) | primary-reported |
| S8 viscous continuation, pinned | 0.45, 0.3, 2/3 | L6, four rungs (nu 6.5e-5 to 2e-3) | 0.06464 / 0.08224 | iteration limit 300; 0.0067 | R8: viscosity does not remove the floor at any rung (viscous floor 1.00 to 1.39 times the inviscid floor). R7 fails at every rung | primary-reported |
| S8 viscous continuation, pinned | 0.45, 1, 20/9 | L6, two rungs (nu 3.5e-4, 1e-3) | 0.0476 / 0.0471 | iteration limit 300; 0.020 | R8 at both rungs (ratios 1.067 / 1.231). R7 fails | primary-reported |
| S7 (a) tail mean-swirl continuation | 0.45, 0.3, 2/3 | L6 | 0.5526 / 0.5170 | iteration limit 300; 0.0019 | core balance (holding the swirl fraction destroys the state) | primary-reported |
| S7 (b) eddy seeding | 0.45, 0.3, 2/3 | L6 | 0.513 / 0.537 | iteration limit 300; 0.70 | core balance | primary-reported |
| S7 (c) eddy and odd-m seeding, degree 4 | 0.45, 1, 20/9 | L4 | 0.06175 / 0.05975 | iteration limit 300; -0.012 | R6 not met: the swirl condition was met through odd modes without lowering the residual. No mechanism named | primary-reported |
| S7 (c), degree 6, m = 2 boost | 0.45, 1, 20/9 | L6 | 0.448 / 0.556 | iteration limit 300 (did not return); 0.13 (ledger row) | R6 not met. An amplitude excursion of the core, not read as a state | primary-reported |
| All-mode class S4 (three arms, including the S7 (c) degree-6 m = 1 seeding arm) | 0.45, 0.3, 2/3 and 0.45, 1, 20/9 | L6 | 0.06502 / 0.06595; 0.04819 / 0.04745; 0.04593 / 0.04622 | time limit in all three; 0.0025 for the m = 1 arm | budget-limited; global balance and far balance as in the even class. No evidence that odd modes lower the residual materially | primary-reported; the (0.45, 1) arm reproduced by the saved-data reader (note HI) |
| S4 omega path, six arms at c_l 0.45 | omega 0.1, 0.2, 0.5 (two arms), 2.0 (two arms); omega/c_l 2/9, 4/9, 10/9, 40/9 | L6 | 0.07437 / 0.07730; 0.06887 / 0.06976; 0.06474 / 0.06559 and 0.05360 / 0.05781; 0.4979 / 0.6990 (the other omega 2.0 arm is gauge-violated, not a reading) | iteration limit 300 in every arm; all above 1e-3 | optimization-path observations only; no floor or trend in omega. No mechanism named | primary-reported |
| S4 c_l path at omega 0.3 | c_l 0.42 to 0.48; omega/c_l 5/7, 15/22, 15/23, 5/8 | not launched | not measured | not measured | the warm starts violate the dilation gauge by -18.6 to +20.0 per cent (registered 5 per cent rule) | not applicable |
| S14 fresh all-mode starts, stage (i) | (0.45, 0.3), (0.45, 1), (0.42, 0.3), (0.48, 1); omega/c_l 2/3, 20/9, 5/7, 25/12 | L4, 32 starts | 0.25 to 0.84 on both families | iteration limit 300 in all 32; V10 -0.0062 to 0.73 | a coverage reading at this budget. No mechanism named. The registered 4 GPU-h cumulative whole-job cap was exceeded (18272 s) | verifier saved-reading audit 2056 / 1, the failure being the cap (note KL) |
| S14 stage (ii) | 0.45, 0.3, 2/3; 0.45, 1, 20/9; 0.42, 0.3, 5/7 (the 0.48, 1, 25/12 job was stopped before any reading) | L6, three promoted starts read | 0.1646 / 0.1648; 0.2268 / 0.2115; 0.2436 / 0.2486 | time limit after 259, 261 and 258 iterations; 0.104, 0.0219, 0.0153 | a coverage reading at this budget; no collapse flag; the even-class degree-6 state of each point is ahead under 7.3b, conditional on the primary core flags and the common sigma_Om quadrature. Not a standalone citation: the comparator budgets (one stopped at its time limit after 413 of 600 iterations), the unrecorded comparator code versions and the device incident at (0.42, 0.3) are stated in section 1, unrestricted azimuthal modes. No mechanism named | primary-reported; lead terminal checks of all three readings (notes LD, LE); verifier saved-record audits 92 / 0 / 4 each, accepted by the lead (note LF); recorded-value consistency, not field validation |
| S5 robustness, R0 group (i), L8 continuation, far anchors (iii) | 0.45, 1, 20/9 and 0.45, 0.3, 2/3 | L6, L8 | see the ruled rows below | see below | R0-2 and R0-3, Option B at degree 8; far anchors as ruled. No mechanism named | saved-arithmetic audits (ruled rows below) |
| R2d rank-2 gauge-pivot variant | 0.45, 1, 20/9 | six-iteration smoke pair only | not measured as a state | not applicable | dropped before use: the registered replay equality failed. Cause OPEN (section 3.4). No mechanism named | verifier audit 36 / 1; receipts of notes KU and KV |

The Stage I arms are diagnosed in the gate I.4 verdict, section 3, and are not repeated here: the fixed-parameter grids
(5 c_l by 5 omega at degree 6), three nest ladders to degree 8, the d6scan continuation in c_l, free-parameter LM
runs, and the from-scratch multistarts. The regenerated failure map adds no Stage I rows. It points to the same
verdict and to the numerics failure analysis items 1 to 34, of which item 2 covers s1b and items 19 and 20 the S2 and
S3 prototypes. The degree-2 multistart count (60 starts per point from six initializer families) is stated in
section 1; its source is the job result records as counted in the verifier's expanded gate audit (item II4-GR1, sha
e7b92d40).

3.2 Independent route.
- Branch at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (independently checked; report 5.3 (e)): rho_u^max 0.1133,
  0.0846 and 0.0729 / 0.0781 at degrees 2, 4 and 6 (Sigma_Z 0.153, 0.2213, 0.351). A stretching-guided degree-4 state
  meets Sigma_Z 0.99994 at rho_u 0.1072, but its ||R_Omega|| is 3.44 ||Omega|| on |y| <= 1024. The fall of rho_u^max is
  denominator-driven: in the core |y| < 1/4 both nonlinear terms are 8.5 to 84 times the self-similar terms and nearly
  cancel. Reading: core balance (lead reading of the cited values; no registered rule applies to this branch).
- Degree-10 evaluation and D10 descent at the same parameters: the ruled D10 row below. The 12-step state's fresh
  holdout is 0.0621 / 0.0691, within 0.41 per cent of the route's degree-8 state. The D10 terminal state has fresh
  holdout 0.061923 / 0.068983. R10 (c): optimizer- and budget-limited, inconclusive. In the degree-10 evaluation the
  17-polar-point rule failed and the 26-point rule passed. This is a quadrature check, not an aliasing reading.
- All-mode eight-step run with its V5 battery at the same parameters (note FH): rho_u^max 0.41029 / 0.41483. For the
  present Stage II attempt with the Euler objective this is the accepted independent all-mode result; the planned
  240-step continuation and its omega = 1 companion were not released (notes EV, FH). Re-checked at assembly: no dated
  release and no result after note FH. The Stage I all-mode runs of this route at c_l = 0.45, omega = 0.3 and 1 (the
  40-step-cap experiment, four of eight completed; the 16-step physical-normalization integration, six of eight
  completed, two stopped at the 1e-12 tail-mass guard; its bounded continuation, two seeds to step 96 and a third
  stopped after step 85 on a mass-admission failure; holdouts 0.399 to 0.758) are separate coverage records with their
  guard failures retained (gate I.4 verdict, Missing modes item; batch 8 audit B8-11).
- S9b balance arm, independently re-evaluated: holdout ratios to the start 1.23173 / 1.23482. R10 (d), inconclusive.
- Verifier failure analysis (FAILURE_ANALYSIS.md, updated 2026-10-25T22:51Z): the original pressure guard fails in 18
  of 86 regions on a degree-6 nest state (up to 3.3e-6 against the guard 1e-7). In four re-tested regions, source orders
  36 and 48 agree to 8.0e-15. Independent pressure accuracy and full-space coverage remain open for the D10 state.

3.3 Theory route (report 5.7; each item is a necessary condition without a threshold, not a mechanism).
- (a) Whole-space balances. E_ren < 0 on all eleven momentum-only primary exports. H_tot < 0 on ten of them, and one
  degree-6 start at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 has H_tot +4.2915. Exact profiles with the registered
  tail have E_ren = 0 (section 4 (b)). This supports "global balance" as a hypothesis for the even-class floor. It does
  not establish it, because the S9b and S9d arms did not attain the balances (R10 (c), (d)).
- (b) First far coefficient (exact value 1). The energy ratio lies between -2835.41 and +29.74 on the eleven states
  with the term. The mismatch m (0.049 to 4.4) is magnified by 1/c with c from 0.0005 to 0.05456. The S11 rows meet the
  closure (R12 (a)) without lowering the holdout at degree 6.
- (c) Head flux on balls: 0.81 to 0.94 of the requirement at a quarter core radius, and at most 0.46 in magnitude
  beyond one core radius (nine exports).
- (d) A radial multiple lambda(r) U removes 68 to 79 per cent of int |R_u|^2 on the eight nest and balance-arm
  exports, and 15 to 24 per cent on the D6 lineage. The S12 rows act on this share (R13 (c)).
- (e) Origin Taylor residuals (exact value 0) are nonzero on every state where they were computed.
- (f) Swirl ratio: sampled maxima without one-sided bounds. None establishes or excludes Q_sw <= 1.

3.4 Synthesis at the gate.
- Readings under registered rules:
  - R2 floors: both c_l = 0.45 ladders are floored at correction-channel Nk 4 at degree 10, and the (0.42, 0.3) ladder
    at degree 8.
  - R8 "viscosity does not remove the floor" at all six viscous rungs. R7 fails at every rung.
  - R10 (c) on both S9d chains, two S9b arms and D10; R10 (d) on the degree-4 S9b arm.
  - R12 (a) on the S11 closure rows; R13 (c) on S12; R11 "no improvement" or "rejected" on S10; R6 not met in S7 (c).
  - R0-2 and R0-3 in S5 group (i), and Option B at degree 8.
  - S14 stages (i) and (ii) are coverage readings at their budgets (stage (ii) lead-reviewed; verifier saved-record
    audits 92 / 0 / 4 each).
- No mechanism is established as the cause of the floor on any branch.
  - Global balance is a supported hypothesis (3.3 (a); balances of order one on every even-class state), not an
    established one. Every arm that targeted it is R10 (c) or (d).
  - Far balance, in the sense of the measured first correction, is not what limits the residual at degree 6 (R12 (a)).
    At degree 8 the closure-met state at c_l = 0.45, omega = 1, omega/c_l = 20/9 has the lowest primary holdout, 0.02983
    / 0.03130, but its core-set guard fails against every state of the branch that it was compared with except the
    nest8nk8 continuation, which it is ordered ahead of (note d128 KH). Far balance therefore remains a candidate in the
    sense of a core/far trade-off.
  - Core balance is the reading of the arms that forced swirl or eddies (S7 (a), (b)) and of the core side of the
    nest8nk8 and degree-8 closure trade-offs.
  - Amplitude instability is the reading of the arms that changed the formulation or freed omega (S10, S8 free).
  - Budget-limited is the lead's reading for arms that ended at an iteration or time limit. Arms that stopped by the
    function-change tolerance with V10 above 1e-3, such as the degree-8 closure state at omega = 0.3, also stopped
    without meeting the diagnostic. These rows meet the operational V10 label: the S11 degree-6 rows, the S9b D6 arm,
    the last S9d step at omega = 0.3 and the St-A R0 0.6 variant. Even for them, stationarity is not established.
  - Transport degeneracy, aliasing and near-edge escape are not attached to any row.
  - The registered list is not exhaustive.
- Optimizer. The R2d decision uses the wording of note KV, as the verifier's KV receipt amends it and the batch 8 audit
  (B8-13) narrows it to the logged iterations: "A rank-2 gauge-pivot variant was tested before use, from a start
  pre-aligned so that the rank-2 pivot leaves it unchanged. Over six Levenberg-Marquardt iterations, its cost history
  did not reproduce the production rank-1 history up to the rigid rotation, as registered. The relative cost differences
  grew from 6.2e-7 to 2.6e-4, and at the logged iterations 0 and 5 the damping parameter was larger by factors of about
  1000 or more. The extended Stage III arm was therefore not run; the six-iteration smoke pair did run. The two runs
  differ both in the gauge row and in the rotated coordinates the solver works in, and the solver's diagonal damping is
  not rotation-covariant in general; which difference produced the different paths is not established. No conclusion
  about the equations follows." Accepted remark (verifier proof, confirmed in the KV receipt): "In general the
  diagonally damped Levenberg-Marquardt step is not covariant under a rotation of the coordinates, even for an objective
  that is invariant under that rotation; a two-dimensional example with exact arithmetic shows one rotated start
  accepting its trial step and the other rejecting it. This shows that the rotated replay need not reproduce the
  original path. It does not establish why the observed paths differed." Informational replay (verifier saved-log
  receipt of 2026-10-27T01:56Z, lead-reviewed; R2d stays dropped): "A CPU replay of both six-iteration runs reproduced
  all twelve printed seven-digit costs, so the observed difference between the two pivot choices also occurs on CPU at
  that precision. Its cause remains open."
- "Optimizer failure" is a statement about the search. Every branch above is an optimization or budget reading, and
  none is evidence of nonexistence.
- Process defects recorded at the gate. These process violations remain recorded. The readings retained here have
  the separately stated evidence and review scope; that does not retroactively satisfy the violated rules.
  - (i) The S14 stage (i) cumulative whole-job cap was exceeded (18272 s against 14400 s), and the starts were not
    stopped when it was passed (note KL).
  - (ii) The S14 reader tests created six temporary directories outside the numerics lane, in three runs between
    23:34Z and 23:37Z on 2026-10-26 (two odd-m test cases per run). On the lead's instruction (note KT, since withdrawn)
    the numerics then deleted them at 2026-10-26T23:47:01Z (record bde0635a). Both the creation and the deletion
    were boundary violations, and the instruction is recorded as a lead process failure (notes KV, SCOPE_CORRECTION_2).
    No lane makes changes outside its own directory.
  - (iii) Two comparison tools (compare_replay 4b316814, v2 913aa4b7) were run before a lead review (rule-AU defects).
    None of their outputs is cited.


Rows ruled so far (wording fixed in the cited lead note). The S9d values are primary-reported; their saved scalars were
checked against the saved states (note d128 GS). The D10 values come from the verifier's saved-data reader:
- S9d balance-continuation chain, c_l = 0.45, omega = 1, omega/c_l = 20/9 (note d128 GC, 2026-10-26T12:16:36Z).
  Global balance: L6, pinned core, four kappa steps from 0.1 to 100 under the registered budgets. |E_ren| fell from
  1.530 to 0.941 and |H_tot|/int|h| from 0.687 to 0.645, both far above the 0.05 bounds. Over the same steps the
  far-shell rho_nl on [512, 1024) rose from 0.055 to 2.18, and at kappa 100 the holdout rho_u^max rose 17 to 22 per
  cent and the core-set a_max 4.7-fold. R10 (c): optimizer-limited, inconclusive. Far-shell labels: [512, 2048)
  table, [2048, 4096) partly model, [4096, 32768) model (y units).
- S9d balance-continuation chain, c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (note d128 GJ, 2026-10-26T12:45:19Z).
  Global balance: L6, pinned core, four kappa steps from 0.1 to 100 under the registered budgets. |E_ren| fell from
  1.203 to 0.596 and |H_tot|/int|h| from 0.891 to 0.694, both far above the 0.05 bounds; the last step reduced |E_ren|
  only from 0.649 to 0.596. Over the same steps the far-shell rho_nl on [512, 1024) rose from 0.074 to 0.742, and at
  kappa 100 the holdout rho_u^max was 32 to 37 per cent above Z0, rms_mom 58 per cent above and the holdout vorticity
  ratio 1.7 times Z0's. The last step stopped on the function-change tolerance; stationarity is not established.
  R10 (c): optimizer-limited, inconclusive. Far-shell labels as above.
- Both S9d chains: saved-scalar check done (note d128 GS, 2026-10-26). The verifier's audit of the ten saved states
  (764 confirmed, 0 refuted; 6 open rows are display omissions in historical arm readings) and the lead's own
  extraction from the same files agree exactly with every value in the two rows above. This is a consistency check of
  saved values only; it re-evaluates no field and does not validate the pressure.
- D10 fixed-parameter descent, degree 10, radial 5 (2130 coefficients), c_l = 0.45, omega = 0.3, omega/c_l = 2/3
  (note d128 GR, 2026-10-26T13:37:06Z). Budget-limited: the registered Armijo descent stopped at its time cap after
  429 accepted steps without reaching its target. The objective fell 1.99 per cent (1.6785e-4 to 1.6451e-4) while the
  coefficient vector moved by 23 per cent of its norm, and the decrease per step was still slowing. On the target grid
  (not the holdout) rho_u^max is 0.0618 and rho_nl^max 0.0715, both on the shell at radius 0.41; the shells at radius
  0.10 to 0.82 are above 1e-2. Saved-data reader 17996 passed, 0 failed; the lead's recomputation from the saved
  archives agrees with the reported values to the reported digits. Both are saved-data checks only. The trajectory
  objectives are replayed producer values. The verifier's fresh battery on the terminal state (note d128 HG,
  2026-10-26T15:27:56Z; 2667 of 2668 checks passed) gives fresh holdout rho_u^max 0.061923 / 0.068983 on the standard
  and half-offset shell families, rho_nl^max 0.071650 / 0.091422, core-set sigma_u^max 2.3277, core-set a_max 4.0927
  and sigma_Om 2.0623. The largest radial-refinement change in rho_u is 1.39e-3 relative. The one failed check is a
  quadrature-resolution failure of the battery's single grid over the ball |y| < 1, which sets no maximum. The state
  meets no tier, and it is not ordered ahead of nest10 at the same (c_l, omega), being higher on both families
  (measured on different quadratures). The a_eff leg of the SPEC core-resolution rule needs a level ladder and is
  not evaluated for this single-level state. R10 (c): optimizer- and budget-limited, inconclusive.
- nest (0.45, 0.3) correction-channel ladder, c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (note d128 GU,
  2026-10-26T13:55:10Z). Primary values, reproduced from the saved states and records by the verifier's saved-scalar
  reader (lead result review, note d128 HC); no fresh-field check. nest10 (L10, correction-channel Nk 4) has holdout
  rho_u^max 0.056501 / 0.056453 on the two shell families against 0.059727 / 0.059403 for its source cont150 (L8),
  so q_10 = 0.9460 / 0.9503. Under rule R2 the ladder is floored at correction-channel Nk 4: both values are above
  0.85 and neither is in (0.85, 0.92), so no L10 channel-Nk 8 rung is triggered. nest10 is 5.65 times the Tier S
  holdout bound of 1e-2 and is not a candidate. Mechanism reading (numerics failure map, primary-reported): global
  balance; far balance. The balances stay at order one along the ladder (nest10: E_ren -1.72 with exact value 0,
  H_tot/int|h| -0.88) and the far closure is unchanged (carried mismatch 0.041); budget-limited as well (lead
  reading, 3.4), since nest10 stopped at the iteration limit (V10 0.0084). Values checked against row 2 of the
  regenerated failure map.
- SPEC 7.3b relations in the same branch (c_l = 0.45, omega = 0.3, omega/c_l = 2/3), from the same values (note
  d128 GU; reproduced from the saved data, note d128 HC). The relation is not transitive and is recorded pair by
  pair:
  - nest10 is ordered ahead of cont150 (core-set sigma_u^max ratio 1.019, sigma_Om 0.997, core-set a_max 1.069);
  - s4allm (L6, all modes) is ordered ahead of its start nest6 p0 (ratios 0.985, 1.004, 1.035);
  - cont150 is ordered ahead of s4allm (under 7.3b only; v3 fails on a_max, ratio 1.124) and of nest6 p0;
  - nest10 is not ordered against s4allm (core-set a_max ratio 1.102) or against nest6 p0 (ratio 1.141), although
    its holdout rho_u^max is lower on both families.
  Of these four states nest10 has the lowest holdout rho_u^max, but among them it is ordered ahead of cont150 only.
  Over all saved readings at these parameters (r1 check), five states have a lower holdout on both families: the
  omega = 0.3 closure-met state (row 3; not ordered against nest10, core-set a_max ratio 1.281), the S11 closure row
  s11_L6_cl0.45_om+0.3_fixed_cl1 and three S9d steps, the first of which is row 8. nest10 is behind row 8 and that S11
  row under both predicates and unordered against the other three.
  The "ahead" relations are conditional on the sigma_Om leg of 7.3b, which requires the same radius and quadrature:
  the four states share the 23 holdout shell edges on both families, but their holdout angular counts are 6380
  (nest10), 4700 (cont150) and 3276 (s4allm, nest6 p0), with 138 radii each. The sigma_Om ratios in the ahead pairs
  lie between 0.961 and 1.004. The two "not ordered" relations are decided by core-set a_max and do not depend on
  this leg (lead review of the verifier's L10 saved-scalar reader, note d128 HA). All relations are also conditional
  on the core-resolved condition of 7.3b (v1.21 (b)). The arm readings flag all four states core resolved
  (primary-reported). For nest6 p0 the flag and the core-set values come from the s4allm arm reading's source row and
  a later nest6 p0 arm reading, because the older nest6 p0 job and ledger rows lack them. The verifier's saved-data
  reader reproduces these values and the pair arithmetic and reads the saved flags (note d128 HC). It closes
  neither the quadrature condition nor the core-resolved condition. Until both are closed, none of these relations
  is an accepted ordering.
- nest (0.45, 1) correction-channel ladder, c_l = 0.45, omega = 1, omega/c_l = 20/9 (note d128 HB). Primary-reported.
  The verifier's saved-data reader of nest10, cont150, nest8nk8, nest6 p0 and the all-mode arm at (0.45, 1) passed
  all 741 of its checks and reproduces these values and the pair arithmetic (note d128 HI). Like the (0.45, 0.3)
  reader, it closes neither the quadrature condition nor the core-resolved condition. Holdout rho_u^max
  on the two shell families: nest6 p0 (L6) 0.04604 / 0.04630, nest8 p0 (L8) 0.04393 / 0.04352, cont150 (L8)
  0.04367 / 0.04331, nest10 (L10, correction-channel Nk 4) 0.04195 / 0.04145. So q_10 = 0.9607 / 0.9571 against
  cont150. Under rule R2 the ladder is floored at correction-channel Nk 4 at degree 10, and no L10 channel-Nk 8 rung
  is triggered. As registered on 2026-10-25T23:09:17Z, the Nk-8 state nest8nk8 is reported beside the floor: against
  cont150 its holdout is 6.5 and 4.4 per cent lower and its core-set a_max 38 per cent higher. nest10 is 4.20 times
  the Tier S holdout bound and is not a candidate. Mechanism reading (numerics failure map, primary-reported): global
  balance; far balance. On nest10, E_ren is -1.57 (exact value 0), H_tot/int|h| -0.70 and the carried far mismatch
  0.056, unchanged along the ladder; the K_E ratio is -4.25 against the exact value 1. Budget-limited as well (V10
  0.0052 at the iteration limit).
- SPEC 7.3b relations in that branch (c_l = 0.45, omega = 1, omega/c_l = 20/9), same sources (note d128 HB):
  - nest10 is ordered ahead of cont150 (core-set sigma_u^max ratio 0.971, sigma_Om 1.000, core-set a_max 0.986), of
    nest6 p0 (under 7.3b only; v3 fails on a_max, ratio 1.139) and of the all-mode arm. cont150 is ordered ahead of
    nest6 p0 (under 7.3b only; v3 a_max ratio 1.144) and of the all-mode arm. The saved-data
    reader reproduces these relations. The relation of nest10 ahead of nest8 p0 is primary-reported only, because
    nest8 p0 is not among the reader's states;
  - nest8nk8 has the lower holdout on both families against nest10 (0.973 / 0.999) and cont150. It is ordered ahead
    of neither, because its core-set a_max is 1.40 and 1.38 times theirs.
  The same two conditions apply as in the (0.45, 0.3) branch. Holdout angular counts: 6380 (L10), 4700 (L8) and 3276
  (L6), with the same 23 shells and 138 radii. Core-resolved flags are primary.
  For nest10 against cont150 the sigma_Om leg is now measured on a common quadrature (note d128 IT,
  2026-10-26T19:29Z: the verifier's common-enstrophy reader passed 5425 of 5425 checks, and the lead's own reduction
  of the saved arrays reproduces all 276 region records bitwise). On the finite domain of radius 32768 (standard
  family) and 23170 (half-offset family), sigma_Om = ||R_Omega||_2/||Omega||_2 is 0.4213 for nest10 and 0.4211 for
  cont150. The ratio is 1.0006 on both families, and each value changes by at most 3.3e-7 relative between radial
  orders 12 and 24. This meets the sigma_Om leg for this pair on that domain only. The relation of nest10 ahead of
  cont150 stays conditional on the core-resolved condition. Both values fail the Tier S bound sigma_Om <= 1e-1 by a
  factor of about 4.2. The reader checks leave the producing evaluation's own record unchanged: there, four
  angular-consistency comparisons of R_Omega at |y| = 32768 failed their 1e-8 criterion (the comparison is
  uninformative at that radius), and 90 cancellation-sensitive per-set accuracy measurements were withheld; both are
  recorded with a correction note. These are finite-domain quadrature values of approximate fields, without a
  floating-point error bound or an infinite-tail estimate. No infinite-domain value is stated.
- nest8nk8 cont150, the continuation of nest8nk8 at c_l = 0.45, omega = 1, omega/c_l = 20/9 (note d128 JV,
  2026-10-26T21:51:15Z). Primary values; the verifier's saved ordering audit (75 checks, 0 failed) and the lead's exact
  recomputation of the order table agree. It ended at the 150-iteration limit; the V10 last-tenth decrease 0.0046 is above
  1e-3, so it is not operationally stationary. Holdout rho_u^max 0.039953 / 0.040396 on the two families, lower than
  nest8nk8, cont150 and nest10 on both, and 4.0 times the Tier S bound. It is ordered ahead of none of them: its core-set
  a_max is 1.53, 2.12 and 2.15 times theirs (core-set sigma_u^max 1.39 to 1.49 times). The S3-12 St-C replacement rule
  therefore does not fire. Not a candidate; core resolution is not verified. Mechanism reading (numerics failure map,
  primary-reported): far balance (partial gain) and core balance (a core/far trade-off: the shell gain comes with a
  core-set a_max 1.53 to 2.15 times higher); budget-limited (150-iteration limit, V10 0.0046).
- All-mode class S4 at degree 6, two arms, one start each (note d128 HB; c_l = 0.45 with omega = 0.3,
  omega/c_l = 2/3 and omega = 1, omega/c_l = 20/9). Primary-reported. Both arms ended by the time limit. Neither meets
  the operational stationarity label of SPEC V6 and V10 (objective fall of at most 1e-3 relative over the last 10 per
  cent of the iterations). That label is a budget reading, not a statement about an exact critical point.
  - The odd modes were retained at 8 and 28 per cent of ||U||.
  - The holdout ended 2.8 / 2.3 per cent below the even start at omega = 0.3, and that arm is ordered ahead of its
    start. At omega = 1 it ended 4.7 / 2.5 per cent above the even-class L6 state, and that arm is ordered ahead of
    three degree-6 states only (s10 both10, s14b s5 and s7c m2ecore0.25; r1 check, both predicates), while the
    even-class L6 state and the arm's start s7c m1rel0.1 are ahead of it. Its core-set a_max is 2.98 times that of
    the even-class L6 state. The omega = 0.3 ordering is conditional in the same way
    as above: the sigma_Om quadrature leg and verified core resolution are open.
  - The global balances and the far closure stayed at order one.
  These two arms give no evidence that odd modes lower the residual materially. They do not exclude odd-mode states.
  Mechanism reading (lead, 3.4; the failure-map row names none): budget-limited (both registered arms ended by the
  time limit and do not meet the registered stationarity diagnostic); global balance and far balance as in the even
  class. Values checked against row 32 of the regenerated failure map.
- Self-consistent continuation sgcont150b, c_l = 0.45, omega = 1, omega/c_l = 20/9 (note d128 IX,
  2026-10-26T19:59:46Z). Primary-reported. The start was the degree-8 closure-met state, aligned consistently, under
  the self-consistent objective with the Z0 weights and the closure target. The LM accepted no step at any damping up
  to 1e10 (|g| 4.04e-9 at cost 5.41e-9), and the end state is the aligned parent state to rounding on the worker grid.
  The verifier confirmed the saved arithmetic of that comparison (89 checks, 0 failures); independent field equality
  is open. The principal holdout and enstrophy residual values of the parent are reproduced; sampled extrema differ
  (lambda_max_S by about 8.7 per cent). This is an optimizer reading, not a stationarity statement, and no ordering
  follows.
  Qualifier: post-launch Z0 equality is not established at full precision. The earlier invalid run sgcont150 stays as
  recorded.
- R0 sensitivity controls (note d128 IX; R0 rules of notes d128 HX item 4 and HZ item 2 (c)). Primary-reported. Each
  control continues its state unchanged at R0 = 0.3 and gives the R0-1 bound (its own holdout) and its own drift (the
  worker-grid aligned field difference from the state, not a SPEC 7.10 distance):
  - St-A, c_l = 0.45, omega = 1, omega/c_l = 20/9: control holdout 0.04377 / 0.04358, drift 0.097;
  - St-B, c_l = 0.45, omega = 0.3, omega/c_l = 2/3: control holdout 0.061136 / 0.060952 (0.914 / 0.903 of St-B),
    drift 0.1245, 2.0 times its holdout; it fails the Tier S limits on rho_u^max, sigma_u^max and sigma_Om, 0.01, 0.1 and 0.1 (sigma_u core 0.582, sigma_Om 0.451).
  - St-A R0 0.6 variant (note d128 JL, 2026-10-26T20:56:17Z; V10 values added in note d128 KA): ended by ftol after 183
    iterations; V10 0.00029 for the variant, below the 1e-3 label (an operational label, not a gradient statement), and
    0.030 for the control, which ended at the 300-iteration limit; holdout rho_u^max
    0.061338 / 0.060223, 1.401 / 1.382 times the control's on the two families, so R0-3: "not returned within budget;
    R0 sensitivity not separable from the start distance". Worker-grid aligned field difference to the control 0.1124
    (a proxy for the SPEC 7.1 domains), start distance 0.078. Code versions differ from the control's (S3-25 (d)
    smoke equality only); post-launch Z0 equality not established at 1e-6. The verifier's saved-arithmetic audit
    reproduces the ratios and the R0-3 reading (41 checks, 0 failed; no field evaluation; lead note d128 JO).
  - St-A R0 0.15 variant (note d128 JP): ended at the 300-iteration limit, as did the control. Neither endpoint is
    operationally stationary under V10: the relative objective decrease over the last tenth of the iterations is
    0.035859 for the variant and 0.029960 for the control, both above 1e-3. Holdout rho_u^max
    0.036039 / 0.039238, 0.823 / 0.900 times the control's on the two families, so the holdout condition holds, but the
    worker-grid aligned field difference to the control is 0.2636 (a proxy for the SPEC 7.1 domains), above the control's
    holdout and 2.7 times its drift: R0-2, "similar residual, different state" ("the R0 change moves the re-solved state by
    more than its residual level"), start distance 0.078. Not ordered ahead of the control (core-set a_max 1.31 times,
    sigma_Om 1.20 times); fails the Tier S limits on rho_u^max, sigma_u^max and sigma_Om. Same code-version and Z0 qualifiers as R0 0.6. The
    verifier's saved-arithmetic audit reproduces the ratios (0.82339 / 0.90034), the distance, the V10 values and
    the R0-2 reading (78 checks, 0 failed; no field evaluation; lead note d128 JS).
  - St-B R0 0.6 variant, c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (note d128 JY): ended at the 300-iteration limit, as
    did the control; V10 0.0013 (variant) and 0.024 (control), both above 1e-3, so neither is operationally stationary.
    Holdout rho_u^max 0.084959 / 0.083531, 1.390 / 1.370 times the control's on the two families, so R0-3: "not returned
    within budget; R0 sensitivity not separable from the start distance". Worker-grid aligned field difference to the
    control 0.1232 (a proxy for the SPEC 7.1 domains), start distance 0.0553, control drift 0.1245. Fails the Tier S limits on rho_u^max,
    sigma_u^max and sigma_Om. Same code-version and Z0 qualifiers as St-A. The verifier's saved-arithmetic audit reproduces the ratios and
    the R0-3 reading (337 checks, 335 passed; the 2 failures are near-zero-reference flags of the DU and Omega proxies on
    far shells, which change no quoted maximum; no field evaluation).
  - St-B R0 0.15 variant, c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (note d128 KA): ended at the 300-iteration limit, as
    did the control; V10 0.019 (variant) and 0.024 (control), both above 1e-3, so neither is operationally stationary.
    Holdout rho_u^max 0.053608 / 0.058574, 0.877 / 0.961 times the control's on the two families, so the holdout
    condition holds, but the worker-grid aligned field difference to the control is 0.3060 (a proxy for the SPEC 7.1
    domains), above the control's holdout 0.0611 and 2.5 times its drift 0.1245: R0-2, "similar residual, different
    state", start distance 0.0554. Not ordered ahead of the control (core-set a_max 1.144 times, core-set sigma_u^max
    1.1004 times, above the 1.10 guard, sigma_Om 1.164 times); fails the Tier S limits on rho_u^max, sigma_u^max and sigma_Om. Same code-version and Z0 qualifiers as St-A.
    The verifier's saved-arithmetic audit reproduces the ratios, the R0-2 reading, the V10 values and the
    non-ordering (349 checks, 0 failed, plus a 10 / 0 core and V10 supplement; no field evaluation).
  Summary of group (i) at L6: at both points R0 0.6 is R0-3 and R0 0.15 is R0-2; no variant is R0-1. Only the St-A
  R0 0.6 variant meets the V10 label, and it did not return (R0-3); the other three variants and both controls ended
  at the 300-iteration limit above it. None of this separates R0 dependence from the start distance and the stopping
  rule. No mechanism is named. The L8 pair is Option B, "R0
  re-expansion failed at L8; sensitivity to R0 not tested".
- Same-budget L8 continuation of St-C (s5ctl_L8, the Stage III R1 control; c_l = 0.45, omega = 1, omega/c_l = 20/9;
  note d128 KB; primary-reported): St-C (ftol at 83 of 150 iterations) continued unchanged for 150 iterations, stopped
  at the iteration limit; V10 0.0053 (St-C 0.0021), so neither is operationally stationary. Holdout rho_u^max
  0.043136 / 0.042878, 0.988 / 0.990 times St-C's; core-set sigma_u^max 1.014 times, core-set a_max 1.065 times,
  sigma_Om 0.997 times. Worker-grid aligned field difference St-C to control 0.0244 (U proxy), 0.57 times its
  holdout. The order_73b.py record (82a6a09b; the lead recomputed its five ratios exactly from the saved scalars, note
  d128 KE) orders the control ahead of St-C under 7.3b: lower holdout on both families, core-set guards at most 1.065
  times, both core resolved (primary flags), same degree and quadrature. It continues the same branch from St-C; it is a
  distinct saved endpoint; St-C stays cont150 as the registered R1 base (S3-12 does not fire). The verifier's saved-record audit L8C-4
  reproduces the five ratios bitwise (77 checks, 0 failed; note d128 KJ); the relation is conditional on the primary
  core-resolved flags. Code-version and Z0
  qualifiers as for the L6 controls; St-C's code era is a provenance statement, since its arm record stores no code
  versions. Fails the Tier S limits on rho_u^max, sigma_u^max and sigma_Om. The verifier's saved-arithmetic audit confirms the values, the drift and
  the V10 readings (131 checks, 0 failed; no field evaluation; the ordering tool was not run).
- Far-anchor group (iii), c_l = 0.45, omega = 1, omega/c_l = 20/9 (s5far; both variants start from St-A exactly
  embedded and are read against the St-A control, holdout 0.04377 / 0.04358, drift 0.0969; lead result review note
  d128 KJ). At degree 6, dividing the far anchor radii by 4 returned the control: both runs reached the 300-iteration
  limit, the holdout ratios to the control are 1.0000001 and 0.99999995, and the worker-grid U-proxy difference is
  about 3.6e-7. Multiplying the radii by 4 gave an ftol stop after 23 iterations with holdout 1.046 and 1.025 times
  the control's, and a U-proxy difference of 0.0989, about 1.02 times the control's own continuation drift of 0.0969,
  so this change is not separable from continuation drift. The registered far-field proxy is met at 1/4 and not met
  at 4. It does not test the stability of the fitted pressure multipole coefficients, so the literal SPEC 7.11 X3
  criterion is not evaluated. The radii place far residual rows in a compactified basis and are not a matching
  boundary. The holdout domains differ between the runs, and the comparison is descriptive, not a convergence study
  or an error bound. No variant meets Tier S. Saved-record audit 530 / 0. Not citable: that the quarter-radius far
  rows are inactive (no block cost was measured), any DU or Omega proxy value, or any mechanism.

## 4. Restricted analytic results bearing on the map (verifier-checked only)

Source: the condensed report, section 2 item 23 (provenance T; (e) and (f) I), as installed after the switch and
audited (notes d128 FV, FW). How each item bears on the rows:
- (b) An exact profile with unit leading tail and the stated remainder has E_ren = 0. This is why both S9d rows read
  |E_ren| as a balance defect against the 0.05 bound. For an approximate state, E_ren needs a quantified tail
  remainder, so the rows give E_ren as a primary-reported diagnostic, not as a bound.
- (e) A small relative residual on a fixed ball does not control pointwise residuals or concentration (comparison
  family at c_l,n = 1/2 - 1/n^2, omega/c_l,n = 2 omega n^2/(n^2 - 2)). This is one reason the shortlist ranks by the
  shellwise holdout rho_u^max on both shell families and reports rho_nl^max, and not by one L2 residual on a fixed
  ball. Both are maxima over shells of shell RMS ratios (SPEC 7.2), not pointwise maxima. Pointwise concentration is
  tested separately (pi_u, pi_nl and the maximum-search readers).
- (f) For a z-independent vertical shear core, ||R_u||_(L2(B_R)) >= (1 - 2 c_l)||U||_(L2(B_R)) for every omega when
  the pressure boundary work is nonnegative. It restricts such cores only; it is not an estimate for general fields.
- (a) and (d) concern the edge c_l -> 1/2 and an explicit pure swirl; no row of section 3 cites them (checked at
  assembly).
None of these is an obstruction at 2/5 < c_l < 1/2, so none moves the label toward D.
No row of section 3 cites any other item of the condensed report's section 2 (checked at assembly).

## 5. Stage III

Plan: reports/stage3_plan_draft.md, current revision 94539282 (amended in note d128 LI item 2 (d); earlier revisions
d153bec0 at skeleton time and c551bcb5, posted in note d128 HU; registration S3-1 to S3-25 in notes d128 IE, IF, II and
IK). No discovery arm starts after II.4. The registered Stage III replication jobs released by note d128 LI started
after S15 had ended (section 1); their readings are not used in this gate. Accepted checkpoints are immutable from this
gate on (plan section 2).

Selection. The verifier's protocol selects up to three states for full verifier work: the best eligible primary field
under every required comparison, a structurally different balance or symmetry branch, and an independent-route field
with resolved non-axisymmetric content. No unconditional best primary field exists under 7.3b: at c_l = 0.45, omega = 1,
omega/c_l = 20/9, nest10 is unordered against both nest8nk8 states and the closure-met state, and the closure-met state
is ordered ahead of the nest8nk8 continuation but not of nest10 (order_73b.py record 90f7e94e, primary-reported; the
lead recomputed its ten relations exactly, note d128 KH); the verifier's extended saved-record audit reproduces all ten
relations and fifty ratios (206 checks, 0 failed; note d128 KM); the relations are conditional on the primary
core-resolved flags and the across-degree sigma_Om leg, and the literal independently validated relation is open.
- First (best eligible primary field): nest10 at c_l = 0.45, omega = 1, omega/c_l = 20/9 (state
  b2c111728a215c985bc0aaa9c96bcb3df77afd912f02de0dfa132adab4c7ee64; export samples
  ccce6d7168444983b86f668a592f7dabd756a92f9250744006aaa8da1511c531), the selected primary representative. Reasons: the
  lowest holdout among the states it is ordered against; ordered ahead of cont150, the degree-8 control, nest8 p0, nest6
  p0 (under 7.3b only) and the all-mode arm froms7c (conditional on core resolution); and the most verifier evidence already bound (field
  transfer, common sigma_Om on the finite domain, fixed-field core geometry). The closure-met state, which has the
  lowest primary-reported holdout (0.02983 / 0.03130), neither replaces it nor takes the second slot: it is unordered
  against nest10 and, among the five states compared in note d128 KH, ordered ahead only of the nest8nk8
  continuation (section 3 gives its wider same-parameter ordering); its
  core-set a_max is 2.02 times nest10's (a shell gain with a core loss); it has no independent evaluation, and its
  safeguarded continuation accepted no step (note d128 IX). It stays in the omission list below.
- Second (structurally different symmetry branch): the all-mode state froms7c (job
  s4allm_L6_cl0.45_om+1.0_fixed_froms7c) at c_l = 0.45, omega = 1, omega/c_l = 20/9; degree 6, 16 radial functions, 4
  channel functions, all-mode basis, training normalization all5far (state
  5093bad5b72aad6a64380b610dc150f12d2ded4bb97dd2372421867b8bcf19cf). Primary-reported: holdout 0.048188 / 0.047447,
  1.047 / 1.025 of the even-class degree-6 state nest6 p0; 28 per cent of ||U|| in odd modes retained (training grid;
  numerics failure map eec839a3); core-set sigma_u^max 0.7737, core-set a_max 1.661, sigma_Om 0.4934; time-limit stop
  after 265 iterations, V10 0.045, so not stationary; ordered ahead of three degree-6 states of its branch only (s10 both10, s14b
  s5 and s7c m2ecore0.25), and 20 saved readings of states at these parameters are ahead of it, among them nest10, cont150, the
  closure-met state, nest8 p0, both nest8nk8 states, nest6 p0 and its start s7c m1rel0.1 (r1 check, recounted at r2, both predicates;
  conditional). Reasons: of the read states it keeps a substantial odd-mode content, and
  it has the lowest holdout among states with such content (the S14 stage (ii) states and S15 have holdout at least
  0.0950 on both families; the S7 (c) degree-6 seeding arm, at 0.04593 / 0.04622, kept 3.5 per cent of ||U|| in odd
  modes, and the omega = 0.3 all-mode arm about 8 per cent). It is selected as a symmetry-branch representative, not as
  an improvement; its full verifier work tests whether the odd-mode content survives an independent evaluation. The
  D6-lineage state d6w_L8 (row 5) is not selected: its core is unbalanced (a_eff 0.129, core-set sigma_u^max 1.824,
  sigma_Om 1.377), it is behind rows 1, 3 and 4 (row 2 not counted), and the third selection already represents a state
  with core-set sigma_u^max and sigma_Om above 1.
- Third (independent route, resolved non-axisymmetric content): the D10 terminal state at c_l = 0.45, omega = 0.3,
  omega/c_l = 2/3; twisted Cartesian vector-potential basis, degree 10, five radial channels with even m, 2130
  coefficients (terminal arrays c79a8741dd2f53d8f68924face65465ac8e61eb7e06390a91066b6199b346b43; terminal coefficient
  bits 4bb97660d0467e271283870028c8e6443848a0e200fe2d467fac6c1291029708, note d128 GR). Its non-axisymmetric content was
  read at assembly from the verifier's terminal battery (results
  c447659d066a400e1fa8ad866c280861c32700ea9237688250ca1093e55b789c; 2667 of 2668 checks passed). The m != 0 energy
  fraction of the far-field profile is e_F = 0.2608. On the standard shell family the shell fractions rise from 6.4e-4
  in the innermost shell to 0.518 on [0.125, 0.25) and settle at 0.261 at large radii; the half-offset family peaks at
  0.645 on [0.177, 0.354). Under the angular refinement from 26 x 52 to 32 x 64 nodes every record of both families passes
  (342 per family: 190 angular comparisons, 19 shells times 10 quantities, among them the 19 non-axisymmetric-fraction
  rows; 76 finiteness checks; 38 pressure-source checks; 38 reverse-triangle checks), with largest relative change of
  the shell non-axisymmetric fractions 2.34e-15, and the tail rows pass (relative change of e_F 6.39e-16, absolute difference 1.67e-16). The content is therefore resolved in this finite-quadrature sense. It is even-m
  by construction of the class (odd m vanishes by symmetry and was not measured), no per-|m| split was measured, and the
  core non-axisymmetric fraction was not compared across levels. The battery's one failure, the unit-ball core-doubling
  momentum RMS check (0.10050 against 0.1), stays a failure. The third slot therefore goes to D10, not to the
  independent all-mode step-8 state (rho_u^max 0.41029 / 0.41483).

Order of work. The first selection's evaluations come first on the verifier's critical path (verifier record
2026-10-27T09:42:43Z, corrected 09:48:14Z); the second and third follow only as time allows before the refinement end at
2026-10-28T04:00Z. An evaluation that is not completed is listed as omitted in the final report, with its reason.

Omitted from full verifier work. For each, the omitted evaluations are the full Stage III set: independent pressure and
residual evaluation on the SPEC domains, core-resolution evidence with a_eff stability across levels, the maximum-search
readers, the input manifest and the clean-process tests. Each keeps its failure-map row. State hashes are the full
sha256 of each job's saved state file, rehashed at assembly.
- nest10 at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (state
  dbc0c75a67b0b9b93f9c706e8dddf06bade4108afa33f1d8109fedae55afdffe; export samples
  2677d66ca25cf07d091d5cb69b28a46f767613bbe17bd829b361b8bcfed730a0): the same structure as the first at another omega;
  retained with its saved-scalar evidence (note d128 HC).
- the closure-met state nest8_L8_cl0.45_om+1.0_fixed_cl1 at c_l = 0.45, omega = 1, omega/c_l = 20/9 (state
  62a6dda02ebf13ea7d6ae99d6171776a54ac9a86bd5bf084f4278d4fb47c1dc4) and the end state of its safeguarded continuation
  sgcont150b, row 1 (state 2b5194cbb726fd986f30cfb92101e02fb97d323fa64fff70ffe22adc81d3e67a): reasons in the first
  selection.
- the closure-met sibling nest8_L8_cl0.45_om+0.3_fixed_cl1 at c_l = 0.45, omega = 0.3, omega/c_l = 2/3, row 3 (state
  260776d2015fb651ee71a47e3c58ca236581585a544f03ff24a4c57758117137): ordered ahead of none of its four comparators
  (core-set a_max 1.21 to 1.39 times theirs); not evaluated independently.
- nest8nk8 (state a5b158520bbc9cf74ef02e8c3e32db1f3c5972a176e7eeb700d63c42fdac94d0) and its continuation (state
  db295a45f929d890113d7e8a1f5af21623a2b7e661fe487716efeb1f26b87855) at c_l = 0.45, omega = 1, omega/c_l = 20/9:
  unordered against the first; core-set a_max 1.40 and 2.15 times nest10's. nest8nk8 is the independently checked St1.
- cont150, the St-C control state nest8_L8_cl0.45_om+1.0_fixed_p0_cont150 at c_l = 0.45, omega = 1, omega/c_l = 20/9
  (state 76d4624af76070eb2be9c42cdcf2f4cd652a47dd9d3763d59e05d96bc4e9e83e): ordered behind nest10, conditionally.
- the degree-8 R1 control s5ctl_L8, row 4 (state 684ee3f8f314044721fc5002fd77d678e6e3c37b691ddfdf569634545e52d668): it
  continues the same branch from St-C and is a distinct saved endpoint; ordered ahead of St-C on a primary record, and
  behind nest10 on a primary record that is conditional on the sigma_Om leg across degrees; unordered against both
  nest8nk8 states and the closure-met state, whose core-set a_max is 1.300 to 1.991 times the control's.
  Under 7.3b only it is also ahead of rows 6, 9 and 12 (section 2); against row 6 v3 fails on a_max (ratio 1.108) and
  a_max_half (1.115).
- the all-mode arm s4allm_L6_cl0.45_om+0.3_fixed_m1rel0.1 at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (state
  7fb4572730689fb01c14ddc7022ec7e45054cbd384fd0f3879bc13b40e46792f): about 8 per cent of ||U|| in odd modes, less than
  the second selection; among the four states of note d128 GU it is ordered ahead of its start only. Over all saved
  readings at these parameters (r1 check) it is also ahead of four degree-6 states (s14b s6, S15, s5r0 R0p6 and s9d
  k100), behind the S11 row s11 cl1e-1 and the St-B control (row 12) under both predicates, and behind nest8 p0 and
  cont150 under 7.3b only.
- the D6-lineage state d6w_L8, row 5 (state 5923dbac327ea55da47a408801306020556a8940d8ecbff91df02b0d627072af): reasons
  in the second selection.
- the independent all-mode step-8 state at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (accepted state
  a2debe979369541d7b41aebb52453f03c4f32b600360a3d1d7a9deaa9089a8a6; export
  6a708c45905370349c6c5acf6b19ba25945e1d5e502a0ebcc024f5d9f1fd9968): rho_u^max 0.41029 / 0.41483; its V5 battery is
  complete (note d128 FH).
- row 2, s11_L6_cl0.45_om+1.0_fixed_cl1ftol at c_l = 0.45, omega = 1, omega/c_l = 20/9 (file
  9e773713e942cb755ec206ccf7789915216310ed018904ce21fafe67ccc0e23c): not a state (note d128 GU).
- row 6, the balance-continuation step s9d at c_l = 0.45, omega = 1, omega/c_l = 20/9, degree 6 (state
  f40bfda1d6028c88c7db4213103f3d6ade4d4c8d1453f772007005d3b1b64317): nest10 is ahead of it on the primary values under 7.3b
  only (lead computation at assembly: holdout lower on both families; nest10's core-set sigma_u^max, sigma_Om and
  core-set a_max are 0.941, 1.073 and 0.883 times row 6's), conditional on the degree leg and the core flags. This is
  not the shortlist relation: v3 does not order the pair, because nest10's a_max_half is 1.1355 times row 6's. Row 4
  is also ahead of row 6 under 7.3b only.
- row 7, s1nk_L6_cl0.45_om+0.3_fixed_Nk32 at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (state
  e03774d0cd6bc386fbc33c2a7085c3d9393386a1ff120696febd84102d8fb596): core-set sigma_u^max 1.795 and sigma_Om 1.304, an
  unbalanced core; behind rows 1, 3, 4 and 6 (row 2 not counted).
- row 8, the balance-continuation step s9d at c_l = 0.45, omega = 0.3, omega/c_l = 2/3, degree 6 (state
  d3b5deb1333df0e24c414c87dd172609619c2b14ead2859b2f6d879f65e84026): 7 iterations from the S11 closure-row end state at
  that point, whose gain depended on the excursion path of an unsafeguarded lagged iteration (section 1). On the primary
  values it is ahead of nest10 at c_l = 0.45, omega = 0.3 under both predicates (lead computation at assembly: holdout lower on both families;
  its core-set sigma_u^max, sigma_Om and core-set a_max are 1.029, 1.090 and 1.062 times nest10's), conditional on the
  degree leg and the core flags. That point is represented in Stage III by the third selection.
- row 9, s4om_L6_cl0.45_om+0.5_fixed_from1 at c_l = 0.45, omega = 0.5, omega/c_l = 10/9 (state
  62d5c704acc0ef14e14e05ccd4d7961c57fd852e3c7aae12fff52caca602a763): an S4 omega-path arm, which failed the plateau
  test; behind row 6, and under 7.3b only also behind row 4.
- row 10, d6scan_L6_cl0.47_om+0.3_fixed at c_l = 0.47, omega = 0.3, omega/c_l = 30/47 (state
  78621e2d54868e9d364d1ee9344a2fde44a08b3b7bff5753be37607aefa94dff): no channel functions, training normalization all5,
  core-set sigma_u^max 2.046; behind 7 rows (row 2 not counted).
- row 11, s12_L6_cl0.42_om+0.3_fixed_rl3 at c_l = 0.42, omega = 0.3, omega/c_l = 5/7 (state
  47b2fa50e1ba3c682957a04221fd58731422c28eae2c88961452a2669f761d28): core-set a_max 2.118; behind 6 rows (row 2 not
  counted).
- row 12, the St-B control s5ctl_L6_cl0.45_om+0.3_fixed_R0p3_ctl at c_l = 0.45, omega = 0.3, omega/c_l = 2/3 (state
  5d1d7a00c84365d18f54cdc99245e0f4d7164f48397e8ae5472ddd7f82455c8c): a control, with its own drift 0.125 (note d128 IX); behind
  row 6, and under 7.3b only also behind rows 4 and 9.

Maximum-search batch (verifier planning record ce423074): not run as of this gate. If run, it covers one field only,
nest10 at c_l = 0.45, omega = 1, omega/c_l = 20/9. It uses level caps 16/24/32, about 2.4 GPU-h, inside the 8 GPU-h
envelope for core, origin, axis and maximum studies, with frozen coefficients and frozen selected-pressure objects. It
launches only after the selected-pressure worker for nest10 has an accepted lead result review, and under its own rule
AU source review; the earlier watcher be5f96ef is not reused unrepaired. Latest launch 2026-10-28T06:00Z, end by 09:00Z,
lead result review by 10:00Z. Its result is a finite local-search observation, not a supremum bound, and it cannot
change label C. If these conditions are not met by the latest launch, it is recorded as not run, with that reason.

Plan audit status. The verifier's audit of plan c551bcb5 (2026-10-26T21:35:10Z) confirms its text (HP-C1 to HP-C4) and
leaves HP-C5 and HP-C6 open. HP-C5, current statuses in place of the plan's snapshot wording: the nest10 / cont150
sigma_Om pair is measured on the finite domains only (note d128 IT); sgcont150b accepted no step and its end state is
the aligned parent to rounding on the worker grid (note d128 IX); the omega = 0.3 closure-met sibling is read and is
ordered ahead of none of its four comparators; the S14 stage (ii) states and S15 are read as coverage (notes d128 LD, LE
and NE); the shortlist is regenerated as v3 (section 2); core resolution is open for every state. HP-C6: pressure and
residual evaluation, core-resolution evidence with a_eff stability, manifests, clean-process tests and resource
accounting are prospective; the primary-geometry run is fixed-field geometry only and is not a core-resolution pass.

## 6. Readings and label

Label: C (provisional). No state meets Tier S (SPEC 9), and no Tier R candidate with independently checked pressure
exists; the II.4 outcome is the failure map of section 3. The final label needs the verifier's validation after Stage
III.
