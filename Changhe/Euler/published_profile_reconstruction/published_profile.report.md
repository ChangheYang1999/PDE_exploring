# Result: published-profile reconstruction remains incomplete

The experiments recovered the published axis curves, constructed regular two-dimensional initializations with exact differential Poisson coupling, and found **image-compatible axial traces with small independent transport errors**. They did **not** produce a validated high-accuracy full-plane reproduction of the Euler profile in [Ganeshram, Duruisseaux, and Anandkumar](https://arxiv.org/html/2609.10867v2). Closely matching two-dimensional candidates retain transport peaks; removing the image penalty repeatedly improves selected residuals while substantially changing the profile. No claim of the same solution branch, stability, or singularity formation follows.

This report covers the completed original reconstruction and its boosted/dense follow-ups through job **6882379**. The later user-requested independent continuations from original checkpoints C_01/C_02 are a separate follow-up, recorded in [checkpoint_continuation.report.md](checkpoint_continuation.report.md). The later report contains the completed continuation and its final validation.

All artifacts are outside the prompt/report repository. Below, **R** denotes `/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113`.

## Published data and extraction

A bounded search of the paper, source/supplement, and linked public repository recovered no usable model weights, numerical spline coefficients, or evaluation tables. The linked [lean-dojo/Euler](https://github.com/lean-dojo/Euler) repository contained formal derivations: the audited tree had 99 entries and no release assets. This is an availability finding for the checked sources, not proof that no unpublished data exist. Evidence and source hashes are retained in [PROVENANCE.md](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/paper_data/PROVENANCE.md).

The author-source figure PDFs embed RGB rasters. Tick calibration and extraction of the blue curve yielded **1467 samples per field** over physical z∈[−5000,5000]. The extraction script reproduces the three original CSVs byte-for-byte. Expanded sensitivity files include stroke extent, tick-calibration perturbations, and fixed-z reading effects; they are deterministic reading envelopes, not statistical sigmas or author-model error bars.

| Axis feature | Approximate reading | Value sensitivity |
|---|---|---:|
| U minimum | −38.77 at z≈−218 | ±.16 |
| Ω maximum / minimum | 1.100 at z≈−764 / −.361 at z≈1078 | ±.0062 / ±.0063 |
| Ψ shallow minimum | −155.94 at z≈−3199 | ±4.0 |
| Ψ at plotted z=0 | 259.93 | ±14.1 |

U's connected absolute half-height interval is approximately [−1104,1892], width 2996. The visible traces are asymmetric. Ψ reaches about 803 at the right image boundary; this is not its global maximum. The finite plots cannot establish decay at infinity. Surface views give qualitative radial constraints, with narrow U/Ω and a much broader Ψ, but projection and resolution prevent precise recovery of radial data.

## Equations, origin, and axial reconstruction

Use U=uθ/r, Ω=ωθ/r, Ψ=ψθ/r. With λ=.5 and jointly trainable C,

\[
u^r=-r\Psi_z,\qquad u^z=2\Psi+r\Psi_r,
\]
\[
R_U=U+r(\lambda-\Psi_z)U_r+(C+\lambda z+2\Psi+r\Psi_r)U_z-2U\Psi_z,
\]
\[
R_\Omega=(1+\lambda)\Omega+r(\lambda-\Psi_z)\Omega_r
 +(C+\lambda z+2\Psi+r\Psi_r)\Omega_z-2UU_z,
\quad
R_P=-\Psi_{rr}-3\Psi_r/r-\Psi_{zz}-\Omega.
\]

These signs and reduced-variable conventions were checked against the paper and existing implementation. For V=U(0,z), W=Ω(0,z), P=Ψ(0,z), and B=C+z/2+2P,

\[
R_U=V+BV'-2VP',\qquad R_\Omega=\tfrac32W+BW'-2VV',
\qquad \Psi=P+b r^2+O(r^4),\quad b=-\frac{W+P''}{8}.
\]

The plotting origin is **not** the recentered stability origin. The latter uses a root z* of B and drift C̄=C+z*/2. No constraint C=−2Ψ(0,0) was imposed. At a root with V≠0, exact axial compatibility requires P′=.5.

Independent smoothing alone did not resolve compatibility. Actual joint axial refinement, CPU job **6881295**, used 96 quintic B-spline controls per trace, analytic sparse Jacobians, 513 collocation points, and five decreasing image-prior weights. Its final C is **10.71007869**. Raw image RMS errors `(U,Ω,Ψ)` are **(.00886143,.000443733,.190885)**, and every sampled value remains inside the audited reading envelopes.

A fresh 4096-point axis Sobol set gives `(R_U,R_Ω)` RMS **(2.53567×10⁻⁴,2.20617×10⁻⁵)**; staggered-grid/local checks find maxima **(.0013322,.00012633)**. At z*=−358.487154, V=−37.970822 and P′=.499992106. Thus the images admit highly compatible finite-interval axis traces. This does not determine a radial extension or full-plane tails. Coefficients, curves, and separate validation are in the [axial refinement report](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/axis_refinement/agd-axis-compatible-refine-5477a64fbf7e-6881295/report.md).

## Two-dimensional construction and actual optimization

The first representation uses q=1+r²/a²+(z−c)²/b², U=Σuᵢqᵢ⁻¹ and Ψ=Σpᵢqᵢ⁻¹ᐟ². Ω is always derived from the **complete** Ψ. Three radial extensions multiplied U widths `(30,100,300)` and Ψ widths `(30,100,300,3000,10000,30000)` by `.6,1,1.6`; training criteria selected 1.6. Six axial widths and seven translated centers represent the asymmetric traces. These are plausible model extensions, not recovered author radial coefficients.

All coefficients and C are signed/free. No amplitude hinge, U(0,0)=1 constraint, length-eight gauge, or independent field rescaling was used. The model is even in r, regular at the axis, and imposes U=O(ρ⁻²), Ψ=O(ρ⁻¹), Ω=O(ρ⁻³). These admissible decay powers are a representation assumption; finite images cannot confirm the author's complete asymptotics.

The boosted representation adds a zero-initialized 3→16→16→2 tanh correction with regular compact features and separate radial/axial coordinate scales. It initially preserves the rational model exactly and derives Ω by differentiating the combined Ψ. Existing Adam, dense SSBroyden1, FP64 GPU differentiation, exports, and independent NumPy jets were reused.

| Job | Executed numerical work | Scheduler elapsed |
|---|---|---:|
| 6878470 | Three radial seeds; 5500 Adam + 900 SSB updates | 5m16s |
| 6879747 | Boost from original stage A; 14000 Adam + 2000 SSB updates | 29m08s |
| 6882379 | Continuation of retained boosted `ssb_03`; **3815 accepted** SSB updates | 9m10s |
| 6881295 | Five-stage sparse axial refinement | 7s |
| 6879044 / 6879395 | Common comparison / canonical axis audit | 3m53s / 1m36s |

The dense run budgeted 5000 updates; two blocks accepted none because of precision-loss termination, and another accepted 315. It must not be reported as 5000 executed updates. It used 8192 random rows, 512 high-residual rows, a denser multiscale pool, and training-only locally refined peak replay. Its production program took 527s, including final diagnostics. These completed allocations did not provide two hours of actual optimization; the later continuation task addresses that explicitly. Initial launch 6878310 failed before production because an invalid checkpoint placeholder was supplied; its records remain preserved.

## Shape gains versus PDE gains

The first initialization's raw axis image RMS was **(.302639,.00670703,1.42941)**. On the same 32768-point held-out Sobol cohort used for the older compact candidates, uniform in `(asinh r,asinh z)` over physical `[0,20000]×[−20000,20000]`, the results were:

| Saved candidate | Axis image RMS U / Ω / Ψ | R_U RMS | R_Ω RMS | rR_Ω RMS |
|---|---|---:|---:|---:|
| Previous latest120 | 18.646 / .390834 / 491.991 | .0130316 | .0136184 | .0773500 |
| Previous post09 | 18.683 / .390506 / 494.665 | .00138147 | .00416580 | .440006 |
| Previous post04 | 18.659 / .390568 / 492.319 | .00168917 | .00667430 | .639365 |
| New initialization | .302639 / .006707 / 1.42941 | 4.88635 | .386802 | 19.8205 |
| New stage A | .360311 / .011466 / 5.07787 | 4.12075 | .207855 | 10.4926 |
| New stage B | 2.11471 / .108146 / 47.2680 | 1.44067 | .0436023 | 6.83644 |
| New rational final | 7.23002 / .292463 / 392.704 | .143760 | .00295638 | 5.98149 |

Matching the published initialization greatly improves resemblance, but does not itself reduce the old candidates' residuals. Subsequent PDE optimization reduces errors relative to that initialization while sacrificing the image fit. Old candidates retain their saved signs, amplitudes, C and spatial scales in this comparison. These computational-coordinate RMS values are not physical-area or full-space volume norms; historical benchmarks on different domains cannot be compared directly. [Common comparison and figures](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/comparisons/agd-reconstruct-comparison-d0973d1c2050-6879044/previous_comparison.pdf).

The retained boosted and dense checkpoints improve this tradeoff, without achieving high accuracy:

| Checkpoint | C; U(0,0) | Image RMS U / Ω / Ψ | Independent RMS R_U / R_Ω / rR_Ω | Observed/local peak magnitudes |
|---|---|---|---|---|
| Boosted `ssb_03` | 11.8909; −38.1088 | .046351 / .008277 / .791121 | .061386 / .00162788 / .845056 | .791280 / .0135123 / 27.5926 |
| Dense `ssb_03` | 10.6156; −37.9308 | .025287 / .011543 / .357319 | .0250107 / .00172721 / .340557 | .306951 / .0521270 / 10.3228 |
| Dense final | 305.194; −19.0601 | 8.05063 / .340708 / 279.070 | .00275905 / .000335981 / .317134 | .0298265 / .00397946 / 3.05759 |

The two retained rows use the same fresh 4096-point seed 7349813. The final row uses a separate 32768-point seed 7349841 and denser grids; it is not a common-cohort ranking against those rows. Dense `ssb_03` improves U and weighted-vorticity RMS over its parent but develops a larger Ω peak. Its image fit also trades improved U/Ψ errors against worse Ω error. The zero-prior final loses the published amplitude and shape. The earlier boosted final likewise escapes, with image RMS `(3.59866,.262655,64.0559)` despite independent transport RMS `(.00588893,.000367888,.546669)`.

The original rational final has observed peaks approximately `(1.54,.0418,406.46)` and wide physical-dr-dz rRΩ RMS 17.94. Hence its differential Poisson RMS near 6×10⁻¹⁶ is not evidence of an accurate Euler solution. The later neural candidates' Poisson residuals also cancel structurally.

## Canonical checks, secondary strategies, and limits

A generic whole-space Green rule initially underresolved the highly anisotropic signed mixtures. An adapted basis-wise whole-radial-halfline integration then agreed with the rational final at z=−1000,0,1000 to maximum Ψ error **2.8422×10⁻¹²** and Ψ_z error **4.1078×10⁻¹⁵**, with refinement and anisotropic manufactured checks. [Canonical audit](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/canonical_audit/agd-rational-canonical-axis-6ab701cfa14b-6879395/canonical_axis.json). This is an axis-only floating-point check, not a uniform certificate. It does not numerically validate the added neural source; no completed boosted Green result is claimed here. The globally decaying structural representation supplies the analytic canonical-inverse rationale, separately from numerical implementation checks. Finite far-field rays through 10⁹ test decay and residual behavior, not global accuracy.

The paper's convection continuation was checked: ε multiplies the physical-convection velocity only, replacing radial transport by r(λ−εΨ_z) and axial transport by C+λz+ε(2Ψ+rΨ_r). The source/stretching terms and Poisson equation remain unchanged. All executed primary runs use ε=1, λ=.5. No ε continuation or free-λ campaign was executed, and no invented homotopy was substituted.

The evidence rules out a simple claim that the digitized axis curves are incompatible. The unresolved difficulty is extending that information into a sufficiently accurate radial solution while controlling nonlinear branch drift and moving residual peaks. The available images do not uniquely determine that extension. Repeated penalty removal exposes this weakness; it does not demonstrate nonexistence of the published branch.

## Deliverables and reproduction

The seven requested deliverables are retained:

1. **Data:** `R/paper_data/axis_{U,Omega,Psi}.csv`, calibration/source hashes, and `extraction_audit/*_uncertainty.csv`.
2. **Initial 2D profile:** [initial.npz](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/checkpoints/agd-published-reconstruction-ffbd655e16d1-6878470/initial.npz).
3. **Before-optimization comparisons:** [initial comparison.pdf](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/results/agd-published-reconstruction-ffbd655e16d1-6878470/initial/initial_comparison.pdf).
4. **Independent results:** per-stage `validation.json`, grids, peak searches, axis geometry, and decay records under `results`, `boosted_results`, and `dense_results`.
5. **Paper/final plots:** [dense final comparison.pdf](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/dense_results/agd-paper-branch-dense-refine-53f3b7110340-6882379/final/final_comparison.pdf); the final is explicitly an escaped branch. The retained dense `ssb_03` has its own comparison PDF.
6. **Previous-candidate comparison:** common axes, held-out coordinates, residual JSON, and PDF linked above.
7. **Code/checkpoints/configurations:** [REPRODUCE.md](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/REPRODUCE.md), pickle-free NPZ exports, native PT states, exact argv, and immutable source snapshots under central SLURM records.

Useful shape-retaining state: `R/dense_checkpoints/agd-paper-branch-dense-refine-53f3b7110340-6882379/ssb_03.npz`; lower-residual escaped state: the same directory's `final.npz`. Neither meets the combined objective. Load with `boosted_rational_profile.load_export` / `BoostedRationalProfile.from_export`; coordinates are `asinh([[r,z],…])`, returned derivatives are physical. Native Hessian continuation checks exact model/scaling agreement but does not restore the old Adam/cohort/line-search trajectory.

Seven rational/validator tests and two boosted preservation/jet/export/gradient tests passed on the allocated compute hardware. They check implementations, not PDE accuracy. Reproduce using the frozen source associated with each central plan, the existing FP64 Torch environment, and the prescribed Resnick SLURM workflow. The prompt/report repository contains no experimental code or intermediate artifacts.
