# Current production code guide

All paths here are relative to `research/`; original scientific files are byte-preserved. The compact repository's relocation, verification and Linux launch adapters live in `tools/`, outside that source closure. Some imported files have older stage/version names because the current implementation inherits their functions. Their inclusion is a runtime/hash dependency, not an alternative objective or an additional active campaign.

This guide describes the **implemented 181D baseline only**. The agreed next research sequence is Linux qualification and accepted278 reproduction, followed directly by the unimplemented [860-generator extension](NEXT_RESEARCH_PLAN_860.md). Its [basis/embedding contract](BASIS_860_SPEC.md) requires new versioned modules and a separately validated enlarged chart/checkpoint schema. Existing `--expected-extra 162` and 181-column APIs must not be relabeled as an 860 implementation. See the [receiving prompt](NEW_SERVER_CODEX_PROMPT.md); no prolonged 181D detour is planned.

## Read in this order

1. `absolute_fields.py` and `base/spectral_basis.py`: basis, center and physical fields.
2. `absolute_chart_v2.py`, with `absolute_chart.py`: the 19-dimensional core chart.
3. `absolute_model.py`, `stage13_model_v3.py` and its two parent classes: loss weights and actual cached provider.
4. `whole_axis_mesh.py`, `stage13_integration_v3.py` and `stage13_integration_v2.py`: fixed training rule and independent accuracy gates.
5. `stage13_solver.py`, then `stage13_campaign_v3.py`: full-SVD step, feasible lift, acceptance and recovery.
6. `verification/scripts/`: external residual, Green inverse and derivative assessments.

The live numerical chain is

```text
stage13_campaign_v3.run/recover
  ├─ AbsoluteC5ChartV2 → analytic center + five Taylor equations
  ├─ stage13_model_v3.CachedAbsoluteProblem
  │    ├─ parent cache/model classes → dense weighted r and raw J
  │    ├─ private scalar-exp field namespaces → analytic core/Global fields
  │    └─ highprecision_origin → order20 small-radius algebra
  ├─ stage13_solver.DenseTrustModel → full thin SVD trust step
  ├─ stage13_integration_v3.EpochIntegrator
  │    └─ stateless V2 evaluator + independent origin/tail/quadrature tests
  └─ snapshot → proposal outcome → authoritative commit → state
```

## Data contracts and candidate reconstruction

`absolute_common.py:9–19` derives ROOT/BASE from `__file__`, requires a real `IPM_RESOURCE_SESSION`, and imports numerical dependencies. Do not bypass supervision by assigning a fictitious session. `A_REF` is read from the exact `inputs/candidates.json`. Helper functions hash raw bytes/float64 arrays, write atomic JSON/NPZ, and record environment/thread provenance.

`absolute_fields.prepare_candidate` (`absolute_fields.py:74–100`) deep-copies a case, checks finite dimensions and cl>1, reconstructs analytic c0, and returns prepared arrays, mode list, center-chain derivatives and a per-candidate Taylor cache. It does not solve C5 or write the input. Use `center_chart` convention for actual evaluation; `literal` c0 is a separate arithmetic diagnostic.

| Saved quantity | Meaning |
|---|---|
| `core_parameters` / NPZ `p`, shape(24,) | `[cl,c1,...,c23]` |
| `coefficients`, shape(24,) | `[c0,c1,...,c23]`, no cl |
| `extra_coefficients` / NPZ `extra`, shape(162,) | Exact order of the saved `modes`; never sort independently |
| `coefficients_decimal` | Analytic-center representation; displayed c0 is not a new variable |
| NPZ `residual`, shape(N,) | Weighted training residual, meaningful with its exact mesh/weights |
| `column_scales` | Fixed epoch coordinate scales, distinct from physical coefficients |
| `scaled_coordinate_step` | Trust-space step, not a candidate vector |

`_core_exponents` (34–39) and `center_data` (42–50) include all cl derivatives. `_decimal_center` (53–71) uses Decimal.from_float and precision90; this reconstructs the exact represented binary input rather than decimal display approximations. The complex-compatible equivalent in `absolute_chart.coefficients` (21–26) supports derivative checks. `hp_report` (49–73) independently recomputes five Taylor defects, Poisson jet identities, a0 and bounds at precision70.

## Analytic fields, axes and complete Jacobian

`base/spectral_basis._radial` (58–84), `_harmonics` (87–109), `_one` (112–135) and `evaluate_modes` (138–160) return per-mode fields and full cl derivatives on flattened broadcast points. Outputs are `(N,K)` float64 arrays. Spatial derivatives through the required order are analytic. Normalized coordinates x/sqrt(R), y/sqrt(R), homogeneous harmonic recurrences and radial envelopes avoid directly forming enormous raw polynomials. Smooth y-quotients are polynomial parity limits, not division by a small y.

`absolute_fields._assemble` (111–120) implements the signs psi=chi_xy and rho=−dyDelta chi. `core_matrices` (123–137) forms all 24 columns. `fields` (140–186) combines core and extra contributions in bounded point/mode blocks, and forms cancellation-safe q by subtracting center strain at the basis level. `residual` (189–205) returns Rf and `(N,186)` raw derivatives. The cl column includes explicit xfx+yfy and all implicit changes in velocity, radial powers, gamma/delta, c0 and q. A derivative holding any of those fixed is not the implemented Jacobian.

`absolute_fields_v2.py:16–52` replaces entries at r≤.02 consistently with order20 Cartesian Taylor fields/residuals/derivatives. `highprecision_origin.radial_series/potential_polynomial/_fields` (73–127) constructs the full potential polynomial in independent Decimal algebra; `field_series/residual_series` (130–198) includes all raw parameter derivatives. `evaluate_series` (201–206) evaluates rounded polynomial coefficients in float64. The method is high-precision coefficient construction, not arbitrary-precision arrays. `origin_diagnostics` (209–233) analytically integrates the squared polynomial, compares truncation orders and diagnoses a constant residual causing logarithmic divergence. A polynomial triangle bound does not bound the omitted analytic remainder.

`field_tests.independent_fields` (16–38) differentiates the complete potential using point-centered Decimal Taylor algebra, independently of the production harmonic/radial recurrence. It is used for origin overlap and spot checks. The canonical inverse is separately reconstructed from rho_x by `source_modes`, `green_once` and `inverse` in `base/stage12_assess.py:154–272`, including its infinite tail. The local Poisson identity is not a replacement for that whole-plane Green check.

## Feasible variables and scales

`AbsoluteC5ChartV2` (`absolute_chart_v2.py:15–70`) constructs the five-by24 constraint Jacobian, scales rows by coefficient-only norms and SVDs the five-by23 coefficient block. All five constraint pairs must resolve. The normal N is 24×5 with zero cl row; the complementary seed F has 19 columns. `absolute_chart.tangent` (119–123) gives

\[
T=F-N(GN)^{-1}GF,\qquad GT\simeq0.
\]

`lift_delta` (125–153) seeds p0+Fq and solves all five nonlinear constraints through normal corrections and backtracking, at most24 Newton steps. It preserves the selected free cl bit pattern, checks bounds and nonzero a0, and rejects infeasible results. Its correction target is3e-12; final C5 tolerance is1e-10.

`stage13_campaign_v3.map_and_model` (229–238) builds

\[
A=[J_{\rm raw,core}T,\ J_{\rm raw,extra}]\,\operatorname{diag}(\text{scales}),
\]

with 181 columns. Initial inverse positive column norms define fixed epoch scales; zero/nonfinite norms stop for diagnosis. `feasible_trial` (241–247) retracts the first19 physical components and adds the remaining162. No scaling/gauge direction is removed. The physical cl and a0 directions remain available.

## Frozen loss rule and selected production cache

`FrozenLogMesh` (`absolute_model.py:27–74`) validates positive finite weights/coordinates and bounds, freezes copies, and fingerprints the ordered little-endian binary64 s/theta/weight arrays. Coordinates are exp(s)(cos theta,sin theta). `AbsoluteLossProblem` (100–161) sets `root=sqrt(2*w/(pi*A_REF**2))` and computes r/root-weighted J. `whole_axis_mesh.py:22–68` supplies positive transformed origin/middle/infinity blocks. Actual meshes referenced by the active epoch are under `integration_epochs/epoch0002_v2_w4/meshes/` even though the selected epoch is `epoch0004_v3_w4_released_iofix/epoch.json`; retain both referenced NPZs exactly.

`stage13_model_v3.CachedAbsoluteProblem` inherits the cache implementation in `stage13_model.py:24–161` and the order20 override in `stage13_model_v2.py:21–37`. The cache stores direct-node f/fx/fy/psix/psiy/ratio basis matrices and their cl derivatives plus a cancellation-safe core q matrix, at one **exact** cl. At changed cl, allocations are refilled in blocks1024 with mode blocks32. There is no interpolation or rounded-cl key. Exact p/extra byte keys avoid duplicate last-point work. Public methods scope BLAS threads and return copies.

The selected provider uses `stage13_stable_exp.ScalarExpProxy` (19–48) in private field namespaces (51–91). Explicit float64 exp calls use scalar `math.exp`, with a bounded256-array exact-byte LRU and copy returns. Other NumPy operations are delegated. `stage13_model_v3.py:61–72` installs the unchanged cache-building code object with private globals, while sentinels (24–58) verify the ordinary NumPy/stateless namespaces remain untouched. Production thus differs in arithmetic dispatch from the independent evaluator, not in basis or physical formula. Source/BLAS/libm/thread changes require new qualification.

Production `workers=4` means four BLAS threads in one Python process; it is not a Python process pool. SVD normally runs under one thread. There is no GPU path. Do not infer useful scaling from core count or change the thread policy before fixed-input replay and performance qualification.

## Independent integration and acceptance

`stage13_integration_v3.EpochIntegrator` (49–109) verifies mesh byte hashes and fingerprints and binds the selected source, derivative, replay and provider qualification records. `validate` (111–124) delegates each **new physical trial** to the unchanged stateless V2 integration and checks namespace identity before/after. Reusing saved physical reference values is confined to startup provider qualification, not new-trial acceptance.

`stage13_integration_v2.independent_integral` (81–165) does origin20/24 analytic integration, an85-digit full-potential overlap test, all-angle far-envelope interval expansion, composite radial Gauss refinement, angular Gauss/trapezoidal comparison and combined numerical error diagnostics. `validate` (246–308) also reevaluates the refined rule and all three block integrals. Trial error targets tighten with predicted decrease. Reference+trial uncertainty must be ≤5% of predicted decrease, and independent decrease must exceed that uncertainty. `tail_envelope.py:18–99` / `outer_envelopes.py:32–123` use absolute coefficient bounds, not assumed leading cancellation. Binary64 bounds/refinement indicators are not rigorous outward-rounded enclosures.

The unchanged campaign acceptance gate (`stage13_campaign_v3.py:485–515`) requires positive training decrease exceeding128eps*oldJ, gain ratio>0.1, feasible jets/bounds, passing fresh independent accuracy, no refinement request and independently significant decrease. Gain<.25 quarters radius; gain>.75 with near-boundary step doubles it. Rejections retain the incumbent and can reuse its model at smaller radius. Acceptance invalidates that model and rebuilds the chart/SVD at the new physical point.

## Full-SVD trust region

`stage13_solver.DenseTrustModel` (216–256) forms a full thin SciPy gesdd SVD of the tall finite matrix A; **every positive singular direction is retained**, and diagnostic rank floors do not truncate the step. No normal-equation matrix A.T@A is formed. For multiplier mu=ell²,

\[
q_i=-\frac{s_i(U^Tr)_i}{s_i^2+\ell^2},\qquad d=Vq.
\]

If the undamped step fits the radius, ell=0; otherwise scalar longdouble bracketing/bisection selects the feasible side. Exact-zero singular coordinates use minimum norm0. Returned step/rotation and physical arrays remain float64; longdouble width is platform-dependent. `trust_region_step` (67–209) and `DenseTrustModel.step` (235–248) check finiteness, original-matrix prediction and trust KKT; campaign refuses original-matrix KKT residual>1e-8. `compare_lsmr` (258–292) is a same-matrix comparison, not the selected backend. Small scaled coordinate gradients alone do not certify stationarity.

## Durable state, replay and restart

`export_candidate/snapshot` (`stage13_campaign_v3.py:145–180`) writes paired JSON/NPZ with physical p/extras, analytic coefficients, weighted residual, objective/error, source/epoch binding and counters. Existing/orphan names get unique retry suffixes. `proposal_snapshot` (183–210) saves a complete physical trial **before** independent validation. An outcome is a separate immutable record. A saved snapshot alone does not establish accepted lineage.

`commit` (213–220) writes a never-overwritten event containing trial and **post_state**, then mutable state, then the redundant trajectory. `recover` (329–372) treats commits as authoritative: it can promote a later complete commit when state lags but rejects state ahead of commits, wrong incumbent/map/epoch/hash, parent/start mismatches or inconsistent workers/modes. JSON/NPZ writers fsync and rename individual files. This is file-level atomicity, not a database or universal multi-file power-loss guarantee.

Recovery loads saved scales and complete state, rebuilds the production training residual, and requires

\[
\|r_{fresh}-r_{saved}\|\le64\epsilon\max(\|r_{fresh}\|,\|r_{saved}\|,10^{-300}).
\]

This threshold must not be relaxed to claim a successful Linux migration. Candidate p/extras alone suffice to evaluate the physical profile; exact optimizer recovery additionally requires state, authoritative commits, parent bindings, epoch/meshes, coordinate map and unchanged source/qualification closure. See the handoff inventory, [RESTART.md](RESTART.md) and [DEPLOY_LINUX.md](DEPLOY_LINUX.md) for what is tracked, materialized or optional.

Stopping on a slice/time budget does not mean convergence. The original24-hour campaign is exhausted. A future resume must explicitly supply a new authorized budget through the portable guarded entry point; it must not reset old ledgers or silently extend the old driver. Production refinement stops request a newly qualified immutable mesh epoch, not an in-place mesh rewrite. No automatic basis expansion is implemented.

## Independent endpoint evidence

`verification/scripts/independent_residual_assessment.py:37–102,156–235` reads exactly32 frozen regions, evaluates absolute/relative residuals on identical points, records axis limits, and leaves zero relative denominators undefined. It also uses independent dense grids, radial bands, local peak refinements, very large radii and high-precision peak checks. Sampled maxima are not certified suprema.

`verification/scripts/stationarity_assessment.py:123–239` computes all181 analytic feasible columns on training/refined meshes, raw186 gradients, full singular spectra and strict endpoint replay; it compares refined production values with stateless values. `probes_phase` (272–352) tests seven physically normalized directions using three halved steps and four-point centered differences. `descent_phase` (355–428) tests two full-SVD proposals with independent accuracy gates but never promotes them. Its outputs explicitly reject stationarity. Full independently differenced181-column validation has not been completed.

The source-host numerical results retained with this handoff are evidence to reproduce, not new-host qualification. New environment tests must bind the actual interpreter, packages, BLAS, source and mesh hashes, thread policy and fresh resource baseline. The relocation adapter translates decoded path strings without changing frozen bytes or numerical values and is tested without original research-path access. Its structural audit is not an executed optimization iteration.
