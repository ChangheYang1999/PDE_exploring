# Phase IV validation plan, version 3

Registered 2026-10-29T23:49:59.299767+00:00. Supersedes version2, SHA256 8cad6dc86085cb271c963822797db46d24a272fa4efda3531fab0b67313bfe26, only for the capacity forecast and ordering below. The exact-input rules, randomization after freezing, quadrature, thresholds and mathematical scope are unchanged. the lead's 23:42:57Z note supplies the new ordering. Eight measured development timings at the intended primary grids are retained in artifacts/phase_iv_plan_v3/timing_audit.json. No final cohort or final random seed is chosen here.

## Binding requirements and scope

The campaign specification is the lead's specification.md, SHA256 e5251d44ef7531ab687fc5fbb3dfa3561d31ba50eb52cd813094140f4dd6c1ee. The inherited requirements are registered/e3_specification_v1.24_sections_7_to_10.md, SHA256 9d89e4d93ab9eb6ad175b66f304f0b4721fddbbc9e714cd064b64d0726dbbe70. These documents govern the acceptance thresholds. This plan does not change them. The informal mathematical dependencies are the adjacent holdout_quadrature/PROOF.md and the pressure_consistency, vorticity_holdout, canonical_origin_vorticity, displaced_ball_quadrature, pressure_cartesian_difference and energy_helicity topic proofs in the research index. Numerical quadrature changes are observations, not error bounds.

Only the existing degree-six main basis and each checkpoint's existing radial counts and correction channels are evaluated. Tier R and Tier A cannot be attained under the campaign's fixed main-degree restriction. A failed necessary Tier S condition establishes that Tier S is not met for the evaluated state; other unmeasured conditions remain OPEN.

## Freeze before final sampling

The lead selects approximately three to five structurally distinct branches from the discovery evidence. A final cohort manifest records, for each selected FREE endpoint, its original B0 and a matched FIXED control where one exists. A missing control remains missing. The manifest records absolute read-only checkpoint paths, full SHA256 values, physical parameters, basis and channel metadata, start identity, the precise end-current or best-state convention, selection rationale, and actual freeze time. Each pair uses the same convention. No member is replaced after its final holdout is seen.

The complete coefficient exchange must round-trip bitwise to the selected checkpoint. Import does not rescale, regauge, project, refit or align the field. Existing exact input archives may be reused only by full checkpoint identity. If a representation is unsupported by the independent route, that limitation is recorded rather than silently changing the field.

After both the cohort manifest and the final evaluator/source binding are frozen, draw a seed from local operating-system randomness and save its bytes, timestamp and the manifest hash. Derive distinct seeds for the holdout angles, pressure-source phase, vorticity and Cartesian checks. Use the same holdout geometry within each comparison. No final test value feeds later optimization or selection into that cohort. A later discovery cohort requires its own freeze and fresh seed, and is reported separately.

## Primary independent pressure and momentum evaluation

Use the qualified independent potential and pressure route, with 12 radial nodes per evaluation domain and a 42 by 84 angular grid at a fresh phase. Increase pressure radial orders from 20/32 to 24/40 and pressure angular orders from 48/64 to 64/80 in mu, with 128/160 azimuthal points. Save both levels, all component norms, flags and observed changes. Recheck source and complete-input hashes before and after every state.

Each comparison uses its B0 reference core scale, physical R0=0.3, both standard and half-offset shell families, and the same 13 physical shells indexed -4 through 8. The registered origin-centered small ball has radius reference_core/32; the distinct origin ball has radius reference_core/256. Include the unit ball, its composite partition and the registered far thin annuli. Report unweighted physical RMS residuals and field norms on the common domains beside weighted diagnostics using each state's actual c_l. A change of c_l changes the exponent and weighting and is not itself physical improvement.

The side currently has about 9.83 GB of accepted evidence. The existing scripts/verify_holdout_v7_cpu.py already holds angular tables in memory and uses GridSource directly with cache_dir=None. Its storage-only change was qualified in V222 with87 controls, artifact holdout_storage_variant_v3/qualification.json. Reuse that unchanged driver, SHA256 c91ff671bc2f38fde920c246748f589c3e7bf00a9a54070e32d39a8265cf2dbd, and bind a final-cohort auditor before execution. No new cache variant or repeat of the storage qualification is needed. The version1 statement that a new storage variant remained necessary is corrected by this source inspection. Do not alter the already bound segment-one scripts. At most one busy computation runs on CPU 35, with one thread and a 48 GB memory limit. GPU 7 can be used only through a separately qualified source path and after checking available memory.

If an observed pressure change is comparable to a claimed improvement, the stronger claim remains OPEN until a further common refinement resolves it. Do not choose a pressure level, domain subset or state after looking at the result. Additional refinements use the same rule for all members of the affected comparison.

## Complementary diagnostics

1. Apply the qualified exact canonical-origin formula to every supported endpoint. Record its exact-input semantics and outward intervals. Excluding a particular finite field as an exact solution says nothing about nearby profiles or existence.
2. Re-evaluate all five vorticity-residual terms on fresh common shell grids at two levels. Include axis caps, origin and unit balls, and balls centered at each state's sampled vorticity maximum. The latter generally differ physically between states and must be labelled. The finite radius-1024 partition is not a full-space norm.
3. On the strongest supported state or states, adapt the qualified Cartesian pressure/Poisson check and targeted far-field pressure check to the frozen coefficients and fresh points. Keep pressure/source consistency distinct from agreement between two reconstructions of the same source.
4. Evaluate centered momentum residuals, finite-ball energy and helicity identities, far-field matching and the applicable non-axisymmetry, nontriviality, resolution and spectral diagnostics using qualified routes. Record every requested quantity that is still missing. A finite-ball integral is not E_ren or H_tot without the required exterior justification.
5. The full Tier S checklist includes all inherited requirements, including N1 through N6, resolved core sets, divergence, pressure-Poisson, origin Taylor, non-axisymmetry and tail conditions. No surrogate or missing value receives PASS. Unavailable higher-degree evidence remains OPEN.

## Stationarity and parameter interpretation

Audit the lead's complete stationarity evidence against specification 7.4, including both progress windows, full J_c at the same point, the registered rank rule, eta values, reduced predicted decrease, physical and optimizer parameter gradients, oscillation ranges and a perturbation restart. J_cw and J_f are model diagnostics and cannot alone establish stationarity. The coefficient projector must remove the actual phase-orbit tangent in reduced coordinates. Scaling norms must come from the stated Jacobian at the same point. Sensitivity widths are not statistical uncertainty intervals. A small training loss, a time limit or a flat trajectory does not establish a basis floor.

For outcome A, apply every registered common-domain improvement and exclusion rule and require the registered independent FREE branches. For B, require the complete stationarity test. C describes incomplete optimization; D requires measured non-identifiability or degeneracy. Apply E to affected results whose derivative, field or pressure validation is insufficient. Do not turn failure of the search into a nonexistence claim.

## Capacity and stop schedule

The primary freeze is2026-10-30T14:30:31Z. Primary and complementary computation stops at19:00:31Z, leaving30min for final evidence/report review before the team stop19:30:31Z. The report owner has a separate hour to20:30:31Z. A controller must stop rather than cross its applicable cutoff.

Actual observed durations on CPU35, one thread, at exactly the primary and pressure grids above, including any recorded pauses:

- Six even-m development members:1419.04 to1599.33seconds, or23.65 to26.66min. These are P1/P2 segment2,3,4.
- Two all-m development members:2691.51 and2967.01seconds, or44.86 and49.45min. These are P3FREE and P3INITIAL. P3FIXED remains running at registration and is not assigned a made-up duration.

Prospective planning charges are30min per even-m primary member and50min per all-m primary member. They replace the provisional25-to35min common estimate. They are estimates, not guarantees or recorded runtime. Include explicit time for input/origin checks and complementary diagnostics in the same plan. The usable computation window is270min: at most240min is planned, with30min held as margin. Do not silently spend that margin in the advertised cohort.

The lead's ordering is:

1. Rank1 FREE, then its original B0, then its FIXED control if one exists.
2. Other selected branches in rank order, each FREE then B0.
3. Remaining FIXED controls in rank order.
4. Complementary diagnostics.

The exact list, mode class, planned minutes and cumulative sum are fixed with the08:30Z selection and restated with hashes at the14:30:31Z freeze. A member whose addition exceeds the240min plan receives exact-input and origin checks only, with final sampled evaluation OPEN. No quadrature is reduced. Complementary diagnostics require their own remaining allowance; qualification runtimes are not silently treated as zero. If actual runtime forces an earlier stop, every unfinished member remains OPEN.

Deduplicate B0 only by the complete represented input, including checkpoint bytes, physical parameters, layout, and the actual fresh-entry projection convention. A shared source file alone is insufficient if the same coefficients are used at different parameters or projected differently. The final cohort import always freezes the actual represented B0. This preserves the existing exact-input requirement and prevents deduplicating P1 and F2 merely because both were initialized from S01.

No final result is used to choose or alter a cohort member. An earlier independent freeze can support a larger cohort if the lead registers it before final sampling and keeps its samples out of subsequent selection. New discovery may continue separately.

The side remains below10GB; the launch guard is9.9GB and the shared filesystem reserve20GiB. Preserve exact accepted evidence and recovery pointers. No JavaScript/TypeScript, servers/listeners, remote or paid compute, RLScience cluster use, Lean/Lake builds, external writes, commits, pushes or online posts are authorized. At most one busy computation runs on CPU35.

## Report audit

For every substantive claim in FINAL_REPORT.md, save its exact text and report hash, method, evidence path/hash, actual check time and one verdict: CONFIRMED, REFUTED or OPEN. Distinguish independent physical recomputation, independent arithmetic replay of producer records, unchecked producer assertions and conditional mathematics. Verify all table rows, parameter values, branch identities, time/resource totals, stationarity labels, acceptance claims and scope statements. The final report must name limitations and incomplete work directly. Verifier conclusions are the entries in verification record, newest last.
