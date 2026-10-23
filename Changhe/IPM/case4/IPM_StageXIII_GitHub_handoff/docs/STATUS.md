# Current scientific status and proposed next research

This is the accepted 181-variable research state captured on 2026-10-23. The verified findings below are unchanged. The 860-generator extension is a proposed next experiment, **not implemented or validated**. Neither current data nor the plan implies a theorem about the PDE or convergence of the approximation space.

## Authoritative incumbent

`research/campaign/global181_v3/snapshots/accepted_00000278.json` has SHA-256
`812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955`.
No newer accepted candidate was found. The old outer driver is stopped by its24-hour budget, not by a stationary endpoint test. This handoff did not launch an optimizer.

| Quantity | Value |
|---|---:|
| Feasible variables | 181 =19 core +162 Global |
| Potential generators | 186 =24 core +162 Global |
| cl | 1.8089923602744993 |
| Physical a0 | 14.767729990606481 |
| Fixed a_ref | 23.95065822465609 |
| Independent whole-axis J_abs | 4.26837260709488e-9 |
| Integral error diagnostic | about2.88e-19 |
| Maximum five-Taylor defect | 4.88829345686e-14 |
| Frozen sampled E_f maximum | 1.23849639744e-4 |
| Frozen sampled E_rho maximum | 7.16582921424e-5 |
| Locally refined sampled E_f maximum | 1.23863020848e-4 |
| Locally refined sampled E_rho maximum | 7.16586070385e-5 |

Frozen and refined maxima intentionally remain separate. Refined values are still sampled maxima, not continuum upper bounds. Integration uncertainties are numerical refinement/envelope diagnostics, not rigorous interval bounds. Both cl and physical a0 are free parameters; a_ref is fixed solely as the loss reference.

## What was verified

- Reconstruction from the exact saved coefficients and basis manifest, with analytic center elimination.
- Whole-axis absolute-loss integration, origin20/24 checks, high-precision overlap, radial/angular refinement and far-tail diagnostics.
- Physical residuals on predetermined independent32-region grids, additional dense/refined grids, exact-axis limits, large-radius samples and radial bands.
- Five Taylor compatibility equations and numerical agreement with the canonical whole-plane Green inverse.
- All181 analytic feasible derivatives on training/refined meshes, full retained singular spectra, and strict saved-residual replay on the source environment.
- Independent four-point finite differences in seven selected directions at three step sizes, including physical cl/a0 directions. These checks found reliable descent, not stationarity.
- Two diagnostic full-SVD feasible trial points passed independent decrease checks. They were explicitly unpromoted; accepted278 remains the incumbent.

Machine-readable outputs and the verification scripts are included or explicitly assigned to the optional evidence artifact in the inventory. Source-host checks are not automatically valid on a new Linux environment. Repository relocation/hash/smoke validation is a packaging test with its own receipt, separate from those scientific claims.

## What remains unresolved

**Stationarity is not established.** Seven selected-direction checks are not181 independent finite-difference columns, and verified descent directly precludes calling the accepted endpoint stationary. A small scaled gradient or a time-budget stop is not a certificate.

**Errors worsened in some near-origin regions.** On the frozen samples, E_f is4.60954122359e-10 for0≤r<.02 and4.43759851249e-6 for.02≤r<.1. Satisfying center/quadratic/fourth-order relations does not constrain all higher Taylor coefficients or guarantee spatially uniform improvement.

**The original density residual grows at infinity.** Independent asymptotic extraction finds a nonzero coefficient of
\(r^{2/c_l-1}=r^{0.105587864228\ldots}\).
The quotient residual can decay and J_abs can be finite despite this failure. The nonlinear first far-field angular matching relation is not imposed by the present basis/constraints. Exact full angular matching, projected matching with unresolved modes and heuristic tail fitting must be distinguished in future work.

**No exact PDE solution or basis convergence is established.** The current181-dimensional approximation is fixed. A proposed860-generator family has not been implemented. High-dimensional optimization and an existence/convergence argument are different tasks. Extreme-radius binary64 cancellation remains an accuracy concern even where high-precision diagnostics recover the expected asymptotic structure.

## Proposed NEXT research: direct 860-generator expansion

The agreed priority **replaces the previous long 181D continuation plan**. The
complete 181D restart is retained for reproducibility and recovery; it is not a
request to spend another prolonged campaign in that space.

1. Qualify native Linux dependencies, BLAS/LAPACK, resources and provider/derivative/replay gates **before changing numerical code**. Reconstruct accepted278 and independently reproduce its whole-axis objective, physical fields, center/five Taylor checks, canonical inverse, frozen sampled maxima and essential residual diagnostics. A Mac PASS is not a Linux PASS.
2. Go directly to a separate versioned implementation of the proposed 860 potential generators, with exact analytical embedding of the current 186-generator space. Replace coordinates; do not append 860 generators to the old ones. Verify the coefficient map and its complete `c_l` dependence, unique ordering, smoothness, dependencies/rank and unchanged embedded profile. **860 is a generator count, not a verified feasible-variable dimension.**
3. Establish and independently test the enlarged center/C5 chart, genuine spatial-scale gauge, full Jacobian, whole-axis integration/tail accuracy and resource/backend policy. Both `c_l` and physical `a_0` remain free; neither changes under exact spatial dilation and neither can fix that gauge.
4. Only after those gates pass, run a guarded small pilot, validate complete enlarged checkpoint/restart, and then a substantive high-dimensional campaign with the same `J_abs` and strict independently verified per-trial acceptance. Do not insert a prolonged 181D optimization between baseline reproduction and the extension.
5. Track whole-axis loss, independent spatial maxima and radial bands, parameters, higher origin terms and far-field Fourier defects separately. The first enlarged campaign adds **no hard `E_1=E_2=E_3=0` matching, no far-field penalty and no objective change**. Consider further angular closure or dimension growth only if measured results justify it.

The planned uniform cutoff `m<=9` is not closed under nonlinear far-field
interactions: F0/F1 can reach odd density harmonic 19, while the first nonlinear
forcing can reach 39. Unresolved high modes must be reported, not silently
projected away. A nonzero first compatibility defect can retain the growing
original-density residual even with a small quotient loss. The earlier
**0.145222% missing-harmonic fraction was measured at accepted165 only**, not
at current accepted278; it motivates a test and is not a current prediction.
The possible later cutoff `M_j=(9,19,29,39)` is not the first implementation.

See [NEXT_RESEARCH_PLAN_860.md](NEXT_RESEARCH_PLAN_860.md) for the ordered
stop/go milestones, [BASIS_860_SPEC.md](BASIS_860_SPEC.md) for exact definitions
and embedding, and [NEW_SERVER_CODEX_PROMPT.md](NEW_SERVER_CODEX_PROMPT.md) for
the complete standalone Linux instructions. No 860 implementation, enlarged
exact restart, trial or result exists in this handoff merely because this plan
is documented.

Do not fix `c_l` or physical `a_0`, change objective weights, truncate weak
positive singular directions, promote diagnostic trials, or loosen restart
replay tolerances as a shortcut to migration. No optimization or process change
on the original Mac, or automatic GitHub push, is part of this documentation
update.
