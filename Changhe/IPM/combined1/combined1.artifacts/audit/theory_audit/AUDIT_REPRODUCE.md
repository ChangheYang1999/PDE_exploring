# Reproducing the audit calculations

The mathematical arguments are in each topic's `PROOF.md`, with the reading
order in `research/INDEX.md`. `VERDICT_LEDGER.md` distinguishes confirmed,
refuted and open claims. A script result verifies its finite algebra and
numerical enclosure; the proof supplies the analytic implication.

Use Python 3.12.13 at
`python3`. The calculations use the
installed `python-flint` package, and the small Hessian check uses SymPy.
No JavaScript, server, GPU, cluster, Lean or Lake is needed or permitted.
Run at most one busy calculation from this lane at a time, on cores 50 and
51 with niceness 19 and one numerical-library thread.

Accepted outputs should not be overwritten. From the lane directory, stage
a fresh copy with, for example:

```sh
python3 -B tools/stage_reproduction.py candidate017_weak
```

This command only copies the chosen proof, code, frozen sources and required
probe input. It creates an empty output directory under `reproductions/`,
records its real time in `STAGING.json`, and prints the exact commands to run.
Other research topics are linked as existing input dependencies. Run the
printed commands in order. `accept.py`, where present, depends on the newly
produced `check.py` result. The staging helper does not launch a calculation.
Remove unneeded reproduction directories to keep this lane below 3 GB; do
not launch new jobs if the build volume has less than 20 GB free.

The supported selections are:

| Topic | What is checked | Expected scale |
|---|---|---|
| `weight_uniform_gram_audit` | Exact determinant, AM-GM and seven Bernstein positivity covers, constants and24 weak inequalities |320 checks; about0.17 seconds;462 |
| `s1_hessian_refinement` | Exact polynomial identities, Young coefficients, parity counterexamples; squared constant 185/96 | Less than a second of computation |
| `candidate015_heldout` | All-mode polar weak witness with n=19, K=600, direct and integration-by-parts pairings, gradient cap | About 35 seconds in the original run |
| `candidate015_heldout23` | The corresponding n=23, K=600 held-out witness | Similar algebraic size to the n=19 calculation |
| `candidate016_weak` | Full polar fields, both registered witnesses n=23,K=2400 and n=19,K=1800 | About two minutes per witness in the original runs |
| `candidate017_weak` | The same full-plane witnesses for the radius-50 candidate | About two minutes per witness; use the ledger for acceptance status |
| `candidate016_sectors` / `candidate017_sectors` | Complete sixteen-sector prefix, exact zeros and four leading profiles | About 25 seconds per candidate |
| `candidate018_weak` | Full polar n=19,K=1800 witness for candidate018 | About 131 seconds; confirmed T4-345 |
| `candidate023_shapes` | All2426 radius25/100 shapes,168 pole witnesses and both67-row objectives | About0.2 seconds;416 |
| `candidate023_point` / `candidate023_origin` / `candidate023_sectors` | Independent023 field values, exact center and full16-row far-field prefix | About2,0.05,22 seconds;417-419 |
| `candidate023_weak` | Full mixed-pole19/1800 witness and all63 moments |146.989 seconds;420; minimum1935 accuracy bits |
| `two_weight_campaign_audit` | Allfour target cutoffs, exact pointwise budgets and uniform remainder obstruction |180 checks; about0.01 seconds;421 |
| `pointwise_profile_radial_cap` | Conditional full radial ceiling with coefficient93/250 and zero errors |59 checks; about0.01 seconds;422 |
| `profile_shape_review_acceptance` | Independent414 review,204 peer bounds and212 acceptance checks | About0.02 seconds;423 |
| `two_weight_review_acceptance` | Full410 review,25 acceptance checks and outward-rounding repairs | About0.003 seconds;424 |
| `numerics_v12_audit` | Exact internal FLOAT-table comparisons and certified-factor rounding |67 checks;50 parsed rows; about0.006 seconds;435 |
| `pointwise_profile_review_acceptance` | Independent angular certificate, optimal-coefficient witnesses, radial caps and rooms |341 checks;78336 rectangles;24576 denominator cells; about7.57 seconds;434 |
| `theory_final_draft34_audit` | Frozen draft34,19 table rows, six new ratios and closure constants |79 checks; about0.009 seconds;433 |
| `radial_average_review_acceptance` | Full R1-045 acceptance, outer-only envelope and all12 targets, source-provenance comparison |190 checks; about0.015 seconds;432 |
| `radial_averaged_remainder_obstruction` | Correct Green average, universal envelope and all12 cutoff comparisons |109 checks; about0.01 seconds;425 AUDITED through432 |
| `candidate022_point` / `candidate022_origin` / `candidate022_sectors` | Actual022 fields, origin normalization and all16 prefix sectors | About2,0.05,22 seconds; confirmed405-407 |
| `candidate022_weak` | All63 whole-plane groups for the registered19/1800 probe | About122 seconds; confirmed408 |
| `candidate022_shapes` | Actual2414 shapes,67 rows and60 probe indices | About0.14 seconds; confirmed403 |
| `folded_velocity_upper_audit` | Complete spatial and direction cover for the universal compensated-velocity constant | About160 seconds;411 confirms E<1.747261 |
| `published_v07_audit` | Full published contract,65 source bindings and nine distance ratios | About0.02 seconds;412 accepts with three repairs |
| `profile_velocity_review_acceptance` | Full independent402 review and46 exact acceptance checks | About0.003 seconds;413 |
| `profile_velocity_shape_cap` | Full radial-shape caps and critical coefficients | About0.013 seconds;94 checks;414 AUDITED through423 |
| `pointwise_profile_velocity` | All61440 projective/physical-angle rectangles for coefficient0.372 | About1.275 seconds;415 AUDITED via434 |
| `profile_specific_velocity` | Exact0.583 angular coefficient and12 identities | About0.55 seconds;402 AUDITED through413 |
| `two_weight_velocity_remainder` | Twenty exact and512-bit remainder identities | About4.45 seconds;410 AUDITED through424 |
| `endpoint_display_repairs` / `fractional_velocity_review_acceptance` | Frozen display repairs and full fractional-ball review acceptance | Documentary stages, no command;404,409 |
| `candidate021_point` / `candidate021_origin` / `candidate021_sectors` | Independent exact021 point, center and complete sector-prefix checks | Confirmed387-389 |
| `candidate021_weak` | Complete mixed-scale n19,K1800 weak certificate for021 | About149 seconds; confirmed392 |
| `candidate021_difference` | All834 angular pairs, exact compatibility and021-minus020 L2 norm | About2.5 seconds; confirmed393-394 |
| `candidate021_shapes` | All2426 actual shapes and81 current analytic rows | About0.1 seconds; confirmed395 |
| `endpoint_review_acceptance` / `velocity_lower_review_acceptance` / `numerics_final_repair_acceptance` | Frozen independent reviews and report-repair acceptance | Documentary stages; no command |
| `candidate020_weak` | Complete two-scale n19,K1800 witness, including all six mixed-pole fixtures | About149 seconds; confirmed363 |
| `candidate020_point` / `candidate020_origin` / `candidate020_sectors` / `candidate020_shapes` | Point, origin, sector and actual dimension/current objective checks | Confirmed360-364 |
| `scaled_hessian_audit` | Independent polar Hessians and full-plane integrals for007,016,017 | About40-49 seconds each, sequential; confirmed366 |
| `hessian_partition_audit` | All exact origin/annulus/far Hessian integrals for016,017 | About50 seconds each, sequential; confirmed367 |
| `annular_moment_adjustment` | Symbolic moment, exterior velocity and scaling identities | Theorem359 AUDITED through370 |
| `higher_mode_rank_audit` | Abstract2414 dimensions and all180 Laurent witnesses | Confirmed369; actual022 binding403 is a separate topic |
| `annular_moment_review_acceptance` | Frozen Opus review and analytic acceptance | Read-only documentary stage; no command is executed |
| `moment_interpolation_audit` | Moment interpolation, exact endpoint projection and conditional weighted budgets | Confirmed371; no supplied weighted budget |
| `sharp_amplitude_moment` | Sharp amplitude-class constant and exact extremizer identities | Theorem372 AUDITED through382 |
| `published_v06_audit` | Complete contract ratios, scaled-index counterexample and closure arithmetic | Confirmed/errata373 |
| `numerics_final_v06_audit` | Report scope, directed rounding, point ratios and angular tensor identities | Confirmed/errata374 |
| `endpoint_gradient_budget` | Weighted angular projection, gradient budget and the conditional CI reach cap |375 AUDITED through385 |
| `angular_tensor_review_acceptance` | Frozen full-tensor angular review and168 exact moments | Documentary stage, no new computation; confirmed376 |
| `rational_bernstein_audit` | Rational Bernstein theorem, independent transform/Taylor fixtures and partial cover geometry | Confirmed377; complete actual cover separate |
| `scaled_background_reconstruction` | All40082 exact candidate017 gradient coefficients, raw origin jet and six points | About73 seconds; confirmed378; copies a129MB polynomial input |
| `endpoint_pointwise_budget` | Three rational-angle gradient bounds, critical E thresholds and conditional caps | Confirmed380; proposed upper E remains separate |
| `scaled_complete_cover_audit` | All247 Bernstein leaves, exact full partition and30381 disjoint pairs | About2209 seconds including pauses; confirmed400; uses the existing129MB coefficient input |
| `normalized_velocity_review_acceptance` / `normalized_review_repairs` / `endpoint_review_repairs` | Frozen independent review acceptances and exact provenance | Documentary stages, no command;396,398,401 |
| `fractional_ball_velocity_lower` | Weighted Bessel constant and12 identities | About0.2 seconds;397 AUDITED through409 |
| `theory_v07_audit` | Full preview and44 exact/Arb inequalities | Less than a second; confirmed with repairs399 |
| `normalized_velocity_lower` | Smooth normalized small-L2 sequence, contact trace and16 identities | 384 AUDITED through396; review repairs accepted401 |
| `universal_velocity_lower` | Exact first-sine test and intrinsic CI limits | 381 AUDITED through391 |
| `sharp_moment_review_acceptance` | Frozen Opus proof review of the sharp amplitude constant | Documentary stage, no command; confirmed382 |
| `reference_screening_audit` | Compatible-chart screening,42 margins and conditional endpoint thresholds | Confirmed with scope repairs379; no supplied difference norm |
| `endpoint_reference_audit` | Two-term projection sign and exact fourth-cutoff coefficients | Consult the latest ledger for acceptance |
| `candidate019_weak` | Full polar n=19,K=1800 witness for candidate019, including all63 moment groups | About129 seconds; confirmed357 |
| `candidate019_point` / `candidate019_origin` / `candidate019_sectors` | Independent point, exact origin and full sector-prefix checks | Confirmed353 to355 |
| `endpoint_closure_inequality` | Moment constant, amplitude projection and the9.28e-11 reach cap | Less than a second; confirmed351 |
| `theory_v06_draft_audit` | All48/51/54 table/prose ratio sets, conditional closure arithmetic and C-prime requirement | Four short commands;352 and358 |
| `candidate018_origin` | Exact quartic jet, normalization and positive slope | Less than a second; confirmed T4-346 |
| `candidate018_point` / `candidate018_sectors` | Independent point fields and the complete sixteen-sector prefix for the new radius-25 continuation | Consult the ledger for completion and acceptance |
| `joint_scaled_rank_audit` | Both scales, 2426 abstract shapes and 168 pole witnesses | Less than a second; confirmed T4-348 |
| `scaled_rank_audit` | Exact branch and pole witnesses for 2174 potential directions; mode 17 support | Less than a second; density extension AUDITED through T4-332 |
| `homogeneous_tail_surgery` | Exact angular inverses for two tail repairs | About a second; theorem AUDITED through T4-337 |
| `cutoff_norm_extensions` | Negative Sobolev scaling, weighted C1 cost and endpoint-sector comparisons | Less than a second; T4-334 |
| `moment_resolved_tail` | Exact kernel identities, endpoint angular projection and Arb coefficient bounds | Less than a second; theorem AUDITED through350 |
| `finite_tail_surgery` | Reconstruct 18 original sectors per candidate, remove the third sector and preserve the endpoint | About 158 seconds in the original run; T4-338 |
| `tail_cutoff_weighted_cost` | Weighted-cost exponents and endpoint | Less than a second |
| `mode_hardy_mellin` | Gaussian factorial ratios and outward special-function examples | Less than a second |
| `theory_final_h12_audit` | Sector indices and all 42 displayed distance ratios | Less than a second |
| `theory_final_draft15_audit` | Draft15, draft17 and draft21 sector indices and displayed ratios | Three short commands; T4-336, T4-341, T4-347 |
| `numerics_final_h12_audit` | Frozen numerical report and standalone analytic counterexamples | Reading only; no calculation is launched or needed |
| `compact_endpoint_audit` | Exact endpoint and dipole profiles for 007, 013, 014, a rational nonproportionality witness, Arb norms | Small exact-rational calculation |
| `scaled_dyadic_reproduction` | Candidate 010, Laplacian modes 1 and 3, eight weights, exact rational partial fractions and whole-plane Arb moments | More than ten minutes in total; use a detached job and poll its log |

For the long dyadic calculation, submit the printed command as a detached
shell job with stdout and stderr redirected to a log inside its fresh run
directory, then poll the log. Every interactive shell command must return
within ten minutes. Each completed mode has its own immutable result, so
restarting the same staged command resumes from that mode after checking its
input hashes. No other busy calculation may run from this lane meanwhile.

The candidate015 n=19 witness must enclose a correction radius strictly greater than
0.000351804115950603. The n=23 claim from N4 is strictly greater than
0.001232449584356253; its independent acceptance status is recorded in the
ledger and must be checked there. Candidate016 has confirmed floors
0.001092633159306284 and 0.001470360924123708. Candidate017's n=23 floor is
0.001068502321536437; its n=19 floor is 0.00167183069831928, accepted in T4-331. The 016 and 017 weak-topic stager prints both commands, with the second explicitly selecting n=19,K=1800. The 018 topic prints n=19,K=1800 and n=23,K=2400 commands, with confirmed floors 0.00165582579205606 and 0.001328016044638112 (T4-345 and349). The second command skips only the unchanged scalar fixtures; actual candidate fields and every moment are checked.
The019 topic uses n19,K1800 and must enclose a radius strictly above0.001661806967193251. Its documentation inputs are preflight-checked before the expensive integration. All63 moment groups and the actual point fields are retained.

The endpoint calculation must find an
exact nonzero proportionality determinant for each of 007, 013 and 014.
The dyadic check compares 32 energy/norm scalars and all seven closure cells
with the frozen N4 record. Reproducing those numbers does not remove the
analytic hypotheses of the corresponding exclusion theorem.

The finite-tail calculation must preserve the exact endpoint coefficient
for 007, 013 and 014, leave only sector (1,2) in the retained prefix, and
enclose the common third density coefficient's circle norm between 27840
and 27842. The endpoint projection calculation has lower coefficient
floors 85017, 85018 and 85016. These are angular asymptotic quantities,
not whole-plane distances. The analytic endpoint theorem is AUDITED through the Opus review accepted in350. Its third-cutoff application is now AUDITED through the independent Opus review accepted in365; the arithmetic script remains only the finite part of that argument.

No timing in this document is a claim of continuous run time. Original
completion times and measured elapsed seconds are stored in the individual
JSON outputs. The helper is a convenience for isolating outputs; it is not
part of any mathematical certificate.

Candidate020 must enclose a radius strictly greater than0.001855374677442712. The020 command runs all six mixed-pole scalar fixtures. The Hessian check must reproduce all135 full-plane groups and the partition check all270 radial primitives. Their source-bound manifests require the copied raw data and their declared sibling dependencies.

The sharp-amplitude stage also copies its immutable PREPARE.json input into the fresh verification directory; result.json is created only by the staged command. Its independent analytic review is accepted in382; the finite arithmetic checks alone do not establish that review. The annular review acceptance is documentary and deliberately prints no calculation command.

The017 reconstruction stage must match all40082 nonzero coefficients and all728 clearing identities. It checks the representation only. The rational Bernstein stage rechecks fixtures and the frozen partial partition, not the subsequently completed actual candidate cover. The separate scaled_complete_cover_audit stage reproduces that full cover, accepted in400; it needs no copied second coefficient table because it reads the accepted sibling input. The screening stage checks a conditional theorem and exact margins; it does not manufacture a certified successor difference norm.

Candidate021 must enclose a radius strictly above0.001864696854799172. Its command explicitly selects n19,K1800 and retains every fixture. The difference stage starts without its generated exact_difference.json and reconstructs the full norm0.007349253249719724... before comparing all three transfer allowances. The shape stage uses the accepted020 and joint-rank records as declared dependencies. Its scope is the current recorded021 objective; it does not replay earlier historical launches. Documentary stages copy frozen sources and verification manifests without executing publisher code.

Candidate022 must enclose a radius strictly above0.00135251075726327. Its command selects n19,K1800, tests all six scalar fixtures and recomputes all actual fields and complete moment groups. The shape stage binds only parent016 and both recorded022 stages; it does not independently replay earlier objectives.

The profile-specific and two-weight remainder stages reproduce finite identities and conditional constants. Neither stage supplies a stationary H_q budget, a successful nonlinear test or a numerical convergence radius for a campaign correction. Their proposal-time proof headers are retained to preserve hashes; consult the ledger for later independent acceptance.

The folded-kernel stage must cover every spatial cell, the refined singular cells and all direction intervals. The pointwise-profile stage must cover the entire projective interval with no gaps, and every physical-angle interval in each accepted cell. Witness selection may use floating point, but every acceptance inequality uses Arb with explicit remainder bounds. No finite-radius or nonlinear closure claim follows from these limiting coefficients.

For candidate023, the shape stage must include `old_basis.json` as well as both recorded coefficient snapshots. The weak stage uses `--mode 19 --power 1800`; omitting those arguments selects a different, unavailable probe. Its all63 moment checks, exact CRT replay, both pairings, point calibration and complete critical-point bounds are required. Source symlinks in a reproduction point only to existing inputs in this lane. The helper sets its temporary directory inside this lane.

The new radius-dependent obstruction concerns error coefficients chosen from the explicit two-weight estimate and universal norm-class estimates. Its checker reconstructs the full angular data and allfour exact targets. It does not certify a smaller actual velocity, a stationary norm bound, a nonlinear inverse or existence.

Candidate024 uses the same explicit `--mode 19 --power 1800` command and must produce a strict floor above0.001556067368832641, with all63 moment groups, both pairings, actual field checks and six fixtures. Its shape stage includes the exact013 quotient and old basis; it verifies the held-out hash reconstruction and records the two-parameter comparison limitation. The outer_remainder_campaign_audit stage reconstructs all endpoint constants and checks316 inequalities, including the strict fallback bound above0.7929999. It does not turn necessary kernel thresholds into sufficient closure conditions.

New acceptance stage432 was independently staged and executed at 2026-10-29T12:39:54.241007+00:00. All input hashes, Python syntax, JSON, command paths and190 acceptance checks pass. `maintenance/staging_432.json` records the actual time and hashes.

Dated provenance, 2026-10-29T12:50:01.351528+00:00: the pointwise-profile launch/log at11:44:12/13 belong to the retained E=3/8 trial. The final93/250 result records11:45:02 but has no separate historical launch/log. T2's byte-identical replay and434's independently reconstructed alternative certificate now validate the final inequality. Historical files are unchanged.

T4-436 through444 are supported by the stage names candidate025_shapes, theory_v08_factors_audit, candidate025_point, candidate025_origin, candidate025_sectors, candidate025_weak, theory_final_draft38_audit, finite_radius_reach_audit and candidate025_peer_acceptance. The025 weak command must include `--mode 19 --power 1800` and retain all eight fixtures. Its63 complete moment groups yield a strict floor above0.002065801265578052. Do not infer a full norm upper bound from it.

The finite_radius_reach_audit stage uses copied exact endpoint JSON and nine evaluations at three specified radii; it does not rerun a grid search or the peer's code. Expected outcome:948checks, current-list CI<2.66323e-8, and the improved universal-coefficient question still open at the two smallest targets. The candidate025_peer_acceptance stage compares all348 coefficients and all60 iteration records, with392checks; its202-source read-only attestation is preserved as provenance evidence. The correction to the older025 result is that only the initial projection is excluded from the logged mesh-step sum.


T4-445 through450 add the stage names theory_v08_preview1_audit, candidate026_shapes, candidate026_point, candidate026_origin, candidate026_sectors and candidate026_weak. The preview topic uses `sources/` rather than `source/`; the stager copies both conventions. The026 weak command includes `--mode 19 --power 1800` and retains all six fixtures. Its63 complete moment groups have minimum1935 accuracy bits and prove a strict floor above0.001355907204057457. Original runtime122.720949993seconds.

The026 structural check has397 checks and180 Laurent witnesses. The main full-prefix check recomputes all16 rows exactly. Supplemental peer comparisons are recorded separately:641 structure checks with141 read-only source attestations, and287 complete-prefix checks with157 attestations. Their scripts assume the original sibling-lane layout and are not included in the fresh-topic commands. They compare independently generated exact data and frozen peer records; they do not supply a substitute numerical certificate. The weak-topic supplemental import binding identifies two loaded local imports absent from the main result input map. Its recorded hashes preserve the accepted run without editing its result.


For026 shapes, the fresh layout contains `run_root/working file candidate026_shapes (not published)` and a private sibling `run_root/working file candidate_snapshots (not published)/<id>`. The stager copies the six immutable snapshot files and SHA256SUMS, checking every hash. This corrects the relative-path assumption without editing accepted proof or checker bytes. Preflight445-450 passed at13:47:11.893975 on29 October2026: all six topic trees matched, and the three inexpensive preview, structure and origin commands passed. Candidate moment integrals were not repeated.

T4-451 through453 add `candidate016_low_order_forcing_audit`, `endpoint_falsification_repairs` and `theory_final_draft39_audit`. All three commands perform finite source and arithmetic checks. The016 topic also needs its frozen `verification/PEER_SOURCE_ATTESTATION.json`, which the stager now copies. It compares59 attested peer-input hashes and reassembles the saved31 moment groups for each of G0/G1; it does not recompute those integrals or read current peer inputs. Original check counts are318,107 and237, with runtimes0.060085314,0.022993384 and1.808552526seconds. The endpoint topic preserves an initial rejected draft and checker under `verification/initial_failed_*`; those diagnostic files are not required by the accepted reproduction command.


T4-454 and455 add `family_ceiling_brackets` and `theory_v08_preview2_audit`. Each has one finite `code/check.py` command. The former uses rational squares and512-bit Arb values (166checks,0.012317326seconds); the latter reparses24 factors and independently evaluates endpoint coefficients and nine exact-ceiling factors at768bits (415checks,0.032970979seconds). Its manifest binds106inputs including72 matching frozen appendix files; five changed live reports are recorded as historical references. All exact coefficients are JSON inputs. No live peer program or spatial integral is run.


T4-456 adds `theory_final_draft43_audit`, one finite `code/check.py` command at768bits. Its263checks take about1.4seconds, dominated by the word comparison. It reuses accepted integral enclosures and performs no spatial integration. The original failed schema lookup and traceback are retained in `verification/development_v01`; the corrected program uses026's documented absolute-path inputs map. The source proof, frozen reports, exact inputs and result are bound by hashes.


T4-457 adds `historical_ratio_floor_audit`, a finite `code/check.py` command using only Python exact fractions, decimal place values and integer square roots. Its233checks take about0.008seconds and verify45 table entries without floating arithmetic or integrations. It records two historical source-hash differences rather than asserting current identity. The stager includes the accompanying `PROSE_COROLLARY.md`.


T4-458 adds `candidate001_affine_exclusion`, a finite exact Python check of all 860 raw generators, the complete leading angular polynomial and the nonzero obstruction. A fresh stage writes its own generated coefficient JSON and result with exclusive creation; do not rerun it in the original accepted folder. T4-459 adds `h18_coverage_audit`, a finite rational check of 24 accepted weak witnesses, 27 exact registry bindings, eight scalar tuples and all 105 frozen matrix rows. It reuses the copied integration certificates and does not evaluate the integrals again. The latter stage copies about 46 MB of frozen evidence. Both commands use the assigned affinity and a single low-priority worker; no server, JavaScript, Lean or remote work is involved.


T4-460 is staged as `late_weak_supplement_audit`. Its finite checker reuses six accepted moment records and independently checks all global probe-gradient extrema, interval comparisons and quadratic margins. T4-461 is staged as `candidate015_dyadic_audit`. It reads compressed exact coefficient and mode-energy JSON, reconstructs the origin and serialization, and checks all seven cells. Neither repeats a field integration. Both require python-flint and the assigned one-worker environment. The accepted original result directories use exclusive creation; stage a new copy before replay. The origin-index failure preceding461 remains archived under that topic's `verification/failed_attempt_v01`.

T4-463 is staged as `candidate017_dyadic_audit`. Its1070-check finite replay reads compressed raw generators, reconstructs the origin, re-sums four complete mode records at two positive weights and checks all seven conditional cells. It takes about0.1seconds and repeats no field integration.

T4-464 is staged as `tb_rebal_endpoint_audit`. Its199checks recompute exact endpoint data, all63 displayed bounds and the exact TB-rebal radius at768bits, about0.013seconds. No integral or peer program is run.

T4-465 is staged as `candidate001_affine_review`. Its957 finite checks verify exact raw branch sums, exponents, angular orthogonality and source bindings for two independent reviews. Runtime is about0.03seconds. The staged command does not execute the copied peer programs or repeat derivative or field calculations. The original T4-458 proof remains unchanged and its correction is frozen in the new source directory.

T4-466 is an analytic review at `audit record negative_norm_dual_audit, proof`, with frozen source hashes and ten explicit verdicts in `verification/analytic_review.json`. It has no numerical checker or replay command. The candidate016 numerical dual certificate remains separate.

T4-467 is staged as `candidate016_complete_forcing_audit`. Its8874 finite checks re-sum complete accepted moment balls, derive tensor counts and all exact scalar comparisons at2048bits, about0.15seconds. The3.3MB production JSON is frozen compressed. Its source graph was rehashed read-only at preparation; staged replay verifies that frozen identity record. No copied peer code or spatial integral executes. The later016 dual values are accepted in T4-470 and their saved-group precision repair in T4-472.

T4-468,469,470 stage as `weight_uniform_review_acceptance`, `divergence_free_negative_norm_upper`, and `candidate016_dual_replay_audit`; all three fresh staged checkers passed. T4-471 stages as `theory_v08_published_audit`,695finite rational checks taking about2.7seconds. It includes compressed exact historical report prefixes; staged replay hashes their decompressed bytes. It does not execute copied peer code or candidate integrals. Frozen source metadata retains the chronological hash receipt. Original accepted output directories use exclusive result creation.

T4-472 stages as `candidate016_cross_archive_audit`. Its3113 finite checks independently reconstruct the exact trial energies, re-sum all262650-digit saved group balls and recover the actual E2 separation. Runtime is about1.8seconds at4096bits. It retains the complete source projection and pole-integration soundness premises and executes no copied peer program. The first external-binding reader failure is archived separately.

T4-473 stages as `constant_display_successors_audit`. Its290 finite checks take about0.03seconds at1024bits. They recompute the exact gamma-function constants, check seven relaxed budget rounding cells,48 directed lower and8 directed upper displays, and the exact delta prefix. No spatial integral is repeated. Both stages have passed one fresh-copy replay.

T4-474 stages as `partial_mode_hardy_certificate`. Its720 exact rational checks take about0.13seconds and use accepted total-component and cross-floor inputs. It evaluates no candidate mode integral. The manufactured prefix and omitted-mode identities, directed upper inputs and the N=33 loss bound all pass, including one fresh-copy replay. General analytic review and current candidate prefix certificates remain separate.

T4-475 stages as `divergence_free_upper_review_acceptance`. Its193 finite checks use rational polynomial beta moments and one512bit elementary Arb expression, about0.07seconds. All T2 rational fixtures and a complete2x2 Gram block are reconstructed without executing peer code. An exact rational antiderivative checks the pole3 example. The candidate016 pole624 integrals are not recomputed. One fresh-copy replay passed.

At 2026-10-29T16:06:41.229804+00:00, six redundant completed-stage sector JSONs were replaced by relative links to the byte-identical original frozen inputs within this lane. All staged paths and hashes remain valid; outputs and logs remain separate. Receipt: `maintenance/deduplicate_staged_inputs_1606.json`. This recovers 83108610 bytes without deleting verification evidence.

T4-476 stages as `candidate016_prefix_hardy_audit`. Its2297 checks independently add exact dyadic endpoints of124 source-certified group intervals and combine them with a containing8192bit pi/2, about0.23seconds. Every prefix endpoint and directed H/E2 bound is independently checked. It uses the accepted complete residual construction and moment enclosures; no field integration or foreign program executes. One fresh-copy replay passed. Both initial overly strong source-output comparisons are archived.

T4-477 stages as `reciprocal_hardy_review_acceptance`. Its209 rational checks and non-executing AST/source-map comparisons take about0.05seconds. Nine peer numerical sources are matched to accepted originals; no candidate integral repeats. Both full peer scripts are read, never executed. One fresh-copy replay passed.

T4-478: `tools/stage_reproduction.py prefix_endpoint_order_audit` stages the44check exact interval-order audit. No candidate integrals; source-specific476 premises retained.

T4-479 stages as `frozen_report_1630_audit`. Its823 exact and text-binding checks take about0.15seconds, with no field integration. It freezes the official16:30 report and matrixv149, expands all108table entries and recomputes the earlier g=0 defect tolerance. One fresh staged replay passed.

T4-480 stages as `candidate016_prefix31_hardy_audit`. Its4463checks independently sum484650-digit group intervals as exact dyadic fractions at8192bits and check complete omitted-mode coverage, about0.69seconds. No candidate moment is repeated. Both Opus reviews of469 are bound through477. One fresh-copy replay passed.

T4-481 stages as `partial_hardy_review_acceptance`.263checks, about.069seconds,30bindings; both review programs parsed only, beta fixtures and exact endpoints independently computed. One fresh replay passed.

T4-482 stages as `theory_final_draft53_audit`.77checks,26bindings,.028seconds. Exact rational a and accepted650digit b intervals show nonunit optimizer. ERRATA_v01 is copied by the helper. Failed own preparation records retained.

T4-483 stages as `prefix31_review_acceptance`.131checks,27bindings,.091seconds. Saved exact endpoints and both normative source definitions, no new integral. The frozen peer programs are parsed only.

T4-484 stages as `candidate017_conditional_acceptance`.2982checks,19bindings,.185seconds. Source JSON is losslessly compressed. The source integral premises remain OPEN; exact finite arithmetic and a manufactured identity are checked.

T4-485 stages as `sharpw_maximum_review_acceptance`.57checks,14bindings,.013seconds. Read PROOF with ERRATA_v01. Peer programs are parsed only; no candidate integration.

T4-486 stages as `candidate016_multimode_replay_audit`.13380checks,2130savedgroups,70bindings,1.86seconds. Every moment integral is imported through its accepted certificate and independently resummed; no candidate integration repeats. Two reader failures remain in verification/FAILED_v01 and v02.

T4-487 stages as `theory_final_draft55_audit`.492checks,34bindings,180losslesslyarchivedsourcehashes,83references,78factors. No foreignprogram or candidateintegral executes.

T4-488 stages as `candidate016_complete_bounds_reciprocal`.121checks,20bindings; original proof and two failed comparisons preserved. No new field integral.

T4-489 stages as `review_repairs_acceptance`.86checks,19bindings; exact polynomial energies and report arithmetic. One own schema failure archived.

T4-490 stages as `candidate007_taylor_tolerance`.3181checks,14bindings; exact harmonic and Cartesian polynomial paths, all five Taylor tolerance counterexamples.

T4-491 stages as `t2_final_summary_audit`.278checks,19bindings. Exact source excerpts, scalar parameter counterexample, factor and defect/rate display scope.

T4-492 stages as `numerical_literal_review_acceptance`.1340checks,26bindings. Finite FLOAT register arithmetic, phase labels, source provenance and incomplete far-tail scope.

T4-493 stages as `theory_final_draft58_audit`.535checks,30manifestbindings,186archiveentries,83references and78floors. Reuses own frozen487archive and accepted488inputs; no integration repeated.

T4-494 stages as `numerical_repair_successor_acceptance`.294checks17bindings. Complete25probe ranking, selected subset ratios,600display transfer and source-attribution check.

T4-495 stages as `candidate017_partial_replay_audit`. Expected10450 checks,1472 coefficients,1424 ordered energy pairs and1339 saved groups;59 manifest bindings. It replays containing intervals and exact energies without repeating field integrals. Full017 H upper and E2 remain OPEN.

T4-496 stages as `numerical_literal_completion`. Expected310 checks and12 bindings. Exactly two changed report lines,600 unchanged displays, complete probe-selection and source-attribution checks.

T4-497 stages as `theory_final_draft60_audit`:452checks,22bindings; reads inherited source metadata, two changed producer files and the frozen matrix. No candidate integration or peer code execution.

T4-498 stages as `candidate016_prefix47_replay_audit`:6234 checks,47 bindings,708 source-group endpoint sums at8192 bits. Eight new mode records are frozen; sixteen earlier ones and complete accepted source premises are reused. No candidate integration or peer code execution.

T4-499 stages as `t2_summary_repair_acceptance`:80checks,14bindings,21independent exact/Arb decimal classifications. Producer checker is read as text only.

T4-500 stages as `final_threshold_division_acceptance`:83 checks,17 bindings, exact Fraction quotients. Producer checker is read as text only.

T4-501 stages as `candidate017_residual_review_acceptance`:398 checks,21 bindings, exact finite radial monomial integrals and the own495 frozen endpoints. No peer program or candidate integral runs.

T4-502 stages as `candidate016_prefix63_replay_audit`:7564 checks,57 bindings,920 exact saved-group endpoint sums at8192bits. Twenty-four previously frozen mode files are reused, eight new files copied. Read ERRATA_v01 for the prose count; no source integral or peer program runs.

T4-503 stages as `candidate017_review_repair_acceptance`:4710checks,19bindings,257 producer-source hash records and every2174 raw generator. Exact fixtures reused from501, no integrals or peer programs rerun.

T4-504 stages as `prefix63_opus_review_acceptance`:473checks,19bindings; no integrals. Checks all extracted endpoint fields against frozen sources and the exact retained-mode width split.

T4-506 stages as `theory_final_frozen_audit`:828checks/53bindings; source hashes, exact report arithmetic and H18ASTcomparison only. No peer program or candidate integral runs. Fresh reproduction receipt maintenance/staging_506.json.

T4-507 stages as `t2_final_frozen_audit`:73checks/19bindings; source hashes and finite rational identities only. Fresh receipt maintenance/staging_507.json.

T4-508 stages as `frozen_report_1837_audit`:1,083 checks,38 input bindings, no candidate integrals. Fresh receipt maintenance/staging_508.json. The first literal-check and staging-list failures are retained with their errata.

T4-509 stages as `energy_share_attribution_acceptance`:95 checks,17 manifest bindings, no new integrals. Receipt maintenance/staging_509.json. Peer code is inert input.

T4-510 stages as `rounded_table_display_audit`: 59 checks, 13 manifest bindings and no new integrals. Fresh receipt maintenance/staging_510.json.

T4-511 stages as `theory_final_replay_comparison`: 532 checks and 157 bindings. It compares all 69 saved output pairs and three JSON pairs; it does not rerun their programs. Receipt maintenance/staging_511.json.

T4-512 stages as `frozen_report_1900_diff_audit`:1433checks,39bindings,18diff hunks,29changed blocks,108rows. Fresh-stage receipt maintenance/staging_512.json. No unchanged historical paragraph or producer process receives a new audit.

T4-513 stages as `final_report_repairs_acceptance`:717checks23bindings13changed blocks108rows. Fresh-stage receipt maintenance/staging_513.json. The line-window and staging-copy preparation errors are retained. No new integral or peer program runs.

T4-514 stages as `final_prefix_scope_review`:88 checks,12 bindings, a54-row output partition and a finite selection-window counterexample. Fresh-stage receipt maintenance/staging_514.json. No producer program executes.
