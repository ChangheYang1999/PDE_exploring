# Phase IV validation plan, version 2

Registered 2026-10-29T12:40:14.521066+00:00. Supersedes the storage-variant preparation in version1, SHA256 2009806e65070215ae983537dba55b9c8877413db512aec7c5b8375239cddcba. The final cohort, sampling and thresholds are unchanged. This is a prospective operational plan. No final cohort or final holdout seed has been selected, and no final result is asserted here. Segment-one evaluations are development evidence, not the final holdout.

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

Team work stops at 2026-10-30T19:30:31Z. Reserve the final 30 minutes for the report/claim audit and final process state. Never start a job whose bounded duration extends beyond the stop. The report owner then has the separate authorized hour until20:30:31Z.

Observed segment-one evaluations take about 15 to 20 minutes per state on the assigned CPU. The increased pressure grid is provisionally budgeted at25 to35 minutes per state, pending a measured timing at the increased orders. Six primary members therefore need roughly150 to210 minutes for pressure alone; nine need225 to315 minutes. Complementary diagnostics and the report audit need additional time. These are planning estimates, not recorded runtime.

Recommendation to the lead: freeze the primary cohort by 2026-10-30T14:30:31Z, five hours before team stop. A freeze at16:30:31Z leaves only three hours and cannot be presumed sufficient for all requested members and diagnostics. An early primary cohort can be frozen while independent discovery continues, provided its final values do not select or improve that cohort. Work order is input/exact-origin checks, primary paired pressure evaluations, remaining selected pressure evaluations, vorticity/center/axis checks, Cartesian/far checks, energy/helicity and remaining Tier checks, then the report audit. Release-critical derivative checks still take priority before this final window.

The side remains below10 GB; the launch guard is9.9 GB and the shared filesystem reserve20 GiB. Hash large producer arrays in place rather than duplicating them. Preserve accepted evidence and exact recovery instructions. No JavaScript/TypeScript, servers/listeners, remote or paid compute, RLScience cluster use, Lean/Lake builds, external writes, commits, pushes or online posts are authorized.

## Report audit

For every substantive claim in FINAL_REPORT.md, save its exact text and report hash, method, evidence path/hash, actual check time and one verdict: CONFIRMED, REFUTED or OPEN. Distinguish independent physical recomputation, independent arithmetic replay of producer records, unchecked producer assertions and conditional mathematics. Verify all table rows, parameter values, branch identities, time/resource totals, stationarity labels, acceptance claims and scope statements. The final report must name limitations and incomplete work directly. Verifier conclusions are the entries in verification record, newest last.
