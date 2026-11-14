# Result: substantial continuation, but no validated published full-plane solution

The requested continuation was carried out from the saved **C_01 and C_02 of job 6878470**, preserving their fields at each new initialization. The new campaign executed **45,472 accepted SSBroyden1 updates in 117m42s of measured optimization**, across eleven branches/stages. This is actual optimizer execution, not the requested allocation limit.

The retained main and broad-model finalists substantially improve both image resemblance and independently measured transport errors over C_01/C_02/C_05. They do **not** establish a high-accuracy full-plane reproduction of the published AGD profile. The smallest new raw U residual still exceeds the historical compact benchmark on the same validation set, radial cores narrow substantially, and localized transport peaks persist. No candidate improves every requested accuracy measure while demonstrably matching the published two-dimensional profile.

All experimental artifacts are outside this repository. **R** below is `/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113`. The original data extraction, equations, and earlier experiments are documented in [published_profile.report.md](published_profile.report.md).

## Which checkpoints to retain

1. **Recommended state when every digitized axis point must remain inside its reading envelope:** [C_02 persistent, cycle0022](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_checkpoints/agd-C01-C02-continuations-34bc65673aa5-6885461/C_02_persistent/cycle_0022.npz). It has the lowest declared weighted physics score among the audited new states satisfying that strict pointwise image condition. C=**10.541259913**, U(0,0)=**−37.992096799**. Axis image RMS `(U,Omega,Psi)` is **(.00649939,.000282564,.168014)**. All 1467 points per trace lie inside the deterministic reading envelopes. This is an axis-image-compatible approximation, not a verified identification of the author's full radial profile.
2. **Best new weighted physics/image compromise:** [C01 broad-tube, cycle0009](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/tube_checkpoints/agd-broad-tube-continuation-489d149dbaca-6886426/C01_tube/cycle_0009.npz). C=**18.169556281**, U(0,0)=**−38.046375658**; image RMS **(.140139,.00904407,2.69671)**. Pointwise envelope containment is **99.39%,99.11%,99.39%**, respectively. Its RMS image score is small, but it is not everywhere inside the envelopes.
3. **Best overall weighted PDE score and common sampled raw maximum among all audited old/new candidates:** the preserved [escaped dense final](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/dense_checkpoints/agd-paper-branch-dense-refine-53f3b7110340-6882379/final.npz). Its published-profile fit is poor: C=**305.193777948**, U(0,0)=**−19.060060297**, image RMS **(8.05063,.340708,279.070)**. It is a PDE endpoint of the tradeoff, not the published-branch winner.

The closest match to the digitized pixels alone is [C_02 persistent, cycle0010](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_checkpoints/agd-C01-C02-continuations-34bc65673aa5-6885461/C_02_persistent/cycle_0010.npz), image RMS **(.00626599,.000294575,.160839)**. Cycle0022 improves its transport accuracy with a small image-fit tradeoff. The best new raw U RMS is instead [C02 raw-polish, cycle0005](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/raw_checkpoints/agd-raw-RU-polish-f0d03eaf3af2-6888096/C02_raw/cycle_0005.npz); its vorticity and radial-tail regressions prevent promotion.

There is no metric-independent PDE winner. Among all 35 audited cases, `old_retained_best` has the smallest raw U RMS, while `old_latest` has the smallest rOmega RMS. Exact paths, hashes and every metric are in the [common comparison JSON](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_final_audit/agd-continuation-final-audit-aa26864fab14-6888808/common/comparison.json).

## Common independent physical comparison

The following rows use **the same fresh 32768-point Sobol set**, seed7349911, uniform in `(asinh r,asinh z)` on physical `[0,20000] x [-20000,20000]`. Fields retain their saved signs, amplitudes, C and lengths. No rescaling or sign adjustment was performed. The last column is `max(max|RU|,max|RO|)` on that common set, not a certified global maximum.

| Checkpoint | RU RMS | RO RMS | rRO RMS | Common raw sampled max |
|---|---:|---:|---:|---:|
| Original C_01 | .698142 | .00801282 | 5.57564 | 3.87803 |
| Original C_02 | .479491 | .00569499 | 4.72787 | 3.35127 |
| Original C_05 | .143717 | .00296198 | 5.98751 | 1.46909 |
| Historical ~.0734 compact benchmark | .00237386 | .0104128 | .234121 | .0761194 |
| C_02 persistent0022: strict image endpoint | .0247799 | .000603854 | .266682 | .221947 |
| C01 tube0009: best new weighted physics | .0128540 | .000458111 | .277692 | .102480 |
| C02 raw0005: smallest new RU RMS | .00907213 | .00579868 | .548670 | .0980304 |
| Prior escaped dense final | .00275794 | .000335853 | .317078 | .0300500 |

The historical benchmark's originally reported values, approximately **(.0008472,.0036332,.0734068)**, used a different sampling domain/measure. Its actual saved checkpoint was reevaluated above. Mixing the historical RMS with the new cohort would give an invalid comparison. Its U(0,0)=**+.213809677**, so it also differs substantially from the published amplitude and sign; the comparison preserves those original fields.

For the C01 tube state, relative to the common historical benchmark, RO RMS improves by about 23x, but RU RMS is 5.41x larger, rRO RMS 1.19x larger, and the raw sampled maximum 1.35x larger. Thus a claim of simultaneous improvement over that benchmark is unsupported. Against C_01/C_02/C_05, the same candidate improves all four tabulated physics quantities as well as image resemblance.

The declared ranking score is

`S = sqrt((RMS(RU)/40)^2 + (RMS(RO)/1.1)^2 + .5*(RMS(rRO)/1100)^2)`.

It is **.000845293** for the strict image endpoint, **.000555493** for C01 tube0009, and **.000373523** for the escaped dense final. These field-based conditioning weights are explicit; a lower S is not equivalent to improving both raw residual components. All 208 saved campaign states remain available, with monitoring Pareto histories. The final 35-case audit selects representative image, weighted-physics, raw-RMS and raw-peak endpoints rather than deleting other tradeoffs.

## Why C drifted, and what the continuations changed

Original C_01/C_02/C_05 have C=**−399.2884/−622.6840/−1454.7068**, with image RMS deteriorating from **(1.75561,.116662,32.2565)** to **(7.23002,.292463,392.704)**. In the old driver, setting the image weight to zero also removed the axis transport weight, qualitative surface prior and coefficient regularizer. It was not a pure image-only ablation. The fixed radial dictionaries and coefficient/C conditioning further limited the original exploration.

Holding each original field fixed, a separate regional least-squares C diagnostic gives full-cohort optima about **−398.14,−624.09,−1450.72**. Therefore setting C to10 by itself would not repair those fields. C had adapted to a distorted profile. Outer-region squared C sensitivity is only around 1e-12, versus about 1e-7 near the axis; large changes in C and a broad slowly varying Psi can be poorly distinguished there. The [C diagnostic and original-profile plots](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/drift_diagnostics/agd-C-drift-diagnostics-38f5bc8845d6-6885567/original_C_axis_diagnostics.pdf) document this without refitting the fields.

The persistent-image C_01 and C_02 branches independently recovered C near 12 in their first 250 updates, then near 10.5 after refinement. The trust branches recovered that range more slowly because their moving parameter boxes limited each C displacement. No branch fixed C or constrained it from Psi at the plotting origin.

The formulation remains lambda=.5, `ur=-r*Psi_z`, `uz=2*Psi+r*Psi_r`, and

`Omega=-(Psi_rr+3*Psi_r/r+Psi_zz)`.

All heads are smooth functions of `s=r²,z`; the regular axis formula is `Omega=-8*Psi_s-4*s*Psi_ss-Psi_zz`. Omega is derived from the complete potential, including every broad correction. Signed coefficients and C are trainable. There is no amplitude barrier, exact published-amplitude boundary condition, origin subtraction, or length-eight gauge. Envelopes impose U=O(rho^-2), Psi=O(rho^-1), Omega=O(rho^-3).

The plotting origin remains distinct from a transport/stability origin. For `B=C+z/2+2*Psi(0,z)`, the strict image endpoint has a root at **z*=−358.500986**, with recentered drift **C+z*/2=−168.709233**. Crucially, Psi_z there is **.498594859**, rather than the exact compatibility value .5, and RU is **−.106684** despite the excellent image fit. The broad state reduces this defect, but still has RU≈**−.04647** at its root. Fitting values accurately does not enforce the required derivatives at the transport fixed point.

## Experiments and actual resource use

| SLURM job | Continuation | Accepted SSB updates | Measured optimizer time | Scheduler walltime |
|---|---|---:|---:|---:|
|6885461|Six branches: each original C_01/C_02 with persistent, trust-box and wider corrections|38,072|80m10s|87m08s|
|6886426|Three broad-radial uncertainty-envelope continuations from retained descendants|6,000|30m16s|33m04s|
|6888096|Two raw-U-emphasis continuations from completed broad descendants|1,400|7m15s|8m43s|

All three scheduler states are **COMPLETED,0:0**. The central workflow used one H200 per allocation, 2 CPUs and 16 GiB host memory, immutable source snapshots and distinct output directories. Some runs overlapped, so aggregate optimizer time differs from elapsed calendar time. Startup, mining, checkpoint I/O and independent monitoring are excluded from the measured optimizer intervals.

Separate U/Psi radial groups, head axial dilations, and neural radial/axial lengths remain trainable. A smooth numerical admissibility parameterization restricts each dilation to **[.1,10]** times its reference length. These are search restrictions, not a physical normalization; active lower limits are a material limitation below.

The six main branches use 16-wide or 32-wide two-layer corrections. Image weights decrease geometrically to positive floors: **.01→.001**, **.003→.0003**, **.001→.00003**. Trust steps use `theta=anchor+radius*tanh(eta)`, with moving boxes adapted from actual reduction and boundary use. This is not a Hessian predicted-reduction trust-ratio method; Hessians are reset when the trust coordinates change, while persistent branches warm-start their inverse Hessians.

Broad refinement adds two initially zero 12-wide corrections at radial lengths 3000/15000 and axial lengths 3000/10000. The original fields are preserved exactly at initialization. The image term uses a squared exterior reading-envelope penalty plus weak interior centering, with positive prior **.02→.002**. Raw polishing emphasizes RU with training scales **(1,1.1,100)** for RU/RO/rRO and prior **2→.2**. Neither stage removes the image constraint. Capacity and objective change together in the broad experiment, so its improvement is not an isolated proof of a capacity bottleneck.

Every block saves physical NPZ fields, native PT model/Hessian state, parameter scales or trust anchor, training coordinates and RNG information. Adaptive sampling uses a separate multiscale training grid, random rows, high-residual rows, local training-only searches and replay. Independent monitoring uses seed7349891; final seed7349911 was not used until all GPU optimization ended. No held-out residual peaks were fed into training.

## Independent limits and remaining obstacles

The final audit adds 4096 physical near-axis points on r∈[0,5], z∈[−6000,6000], 8192 intermediate points, 4096 physical outer points, a 32689-node composite grid with physical `dr dz` quadrature, full digitized-axis checks, radial slices, symmetry tests, rays through 1e9 and selected bounded local peak searches. All residuals use independent NumPy physical derivatives rather than Torch AD. Finite-box computational RMS, regional RMS and physical-area RMS are distinct quantities.

For the strict image state, local searches find **|RU|=.226372** near **(r,z)=(8.194,−562.56)**, **|RO|=.00619609**, and **|rRO|=2.91868**. C01 tube0009 improves the raw peak to about **.102597** near **(4.328,−382.93)**, but its weighted-vorticity peak reaches **5.22733** near **(2588.4,774.6)**. Its near-axis RU RMS is **.0199026**, versus common computational RMS .012854. Its physical-area RMS is **(.00338776,.0000984943,.293405)** for RU/RO/rRO; that broad-box norm cannot replace the core checks.

The broad state's U/Omega radial half-amplitude widths at z=0 are about **5.89/6.37**. Psi remains much broader, with a first axis half-amplitude crossing near 10546 and an off-axis maximum. These widths are physical diagnostics, not the basis length parameters. Surface figures do not resolve them well enough to identify the author's radial solution. The strict image endpoint has a sampled positive off-axis U lobe of **3.375** near **(82.93,-125)**, although its entire digitized axis is negative; the broad endpoint has a smaller positive lobe around **.411**. Axis agreement therefore does not establish agreement with the published two-dimensional surfaces. In several main states, a U dictionary dilation reaches the numerical .1 floor; the broad finalist also approaches that floor. Hence radial-scale convergence is not established. Large signed coefficient cancellations also create conditioning concerns, but there is no evidence that floating-point precision alone explains the much larger transport defects.

Raw polishing illustrates the danger of promoting one residual. Cycle0005 lowers RU RMS to .00907213 but raises RO RMS to .00579868; local RO and rRO peaks are about **.09943/13.1328**. A later state develops a sampled positive off-axis U lobe of about **4.83**, despite a negative plotted-axis profile. These are retained diagnostics, not recommended published-branch replacements.

Differential Poisson residuals are near floating-point precision by construction and do not certify Euler accuracy. Complete-source canonical Green checks separately integrate the rational parent and all neural sources over the whole radial half-line. Refinement orders 12/20/32 give the following maximum saved-potential discrepancies at axis z=−1000,0,1000:

| Complete checkpoint source | max error in Psi | max error in Psi_z |
|---|---:|---:|
| C_02 persistent0022 |8.15e-10|9.45e-13|
| C01 tube0009 |2.94e-11|1.33e-15|
| C02 raw0005 |4.32e-12|1.94e-15|

Constituent errors and refinement changes are retained separately, so large component cancellations are not hidden. These are on-axis floating-point implementation diagnostics, not uniform certificates, stability proofs or proofs of singularity formation. Final CPU job 6888808 completed successfully with exit 0, scheduler walltime 13m47s.

The next numerical questions are the fixed-point derivative defect, narrow radial cores and active scale bounds, intermediate-radius rRO peaks, and conditioning under joint image/physics constraints. More unconstrained training loss reduction alone would not resolve those issues. The experiments do not show nonexistence of the published branch.

## Files and reproduction

- Final35-case comparison, exact held-out coordinates, field/region statistics, image containment, scales, local peaks and checkpoint hashes: [final common audit](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_final_audit/agd-continuation-final-audit-aa26864fab14-6888808/common/comparison.json).
- Exact commands, model loading, objective schedules, snapshot hashes and checkpoint-state qualifications: [CONTINUATION_REPRODUCE.md](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/CONTINUATION_REPRODUCE.md).
- Image/physics Pareto comparison: [PDF](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_final_audit/agd-continuation-final-audit-aa26864fab14-6888808/common/pareto.pdf). Trajectories, C, amplitudes, scales and per-field errors are under the adjacent `progress_0`, `progress_1`, `progress_2` directories.
- Actual fields, digitized-axis comparisons, narrow-core and wide residual maps, and far rays: [strict image endpoint PDF](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_final_audit/agd-continuation-final-audit-aa26864fab14-6888808/fields_run0_C_02_persistent_cycle_0022/run0_C_02_persistent_cycle_0022_comparison.pdf), [broad endpoint PDF](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_final_audit/agd-continuation-final-audit-aa26864fab14-6888808/fields_run1_C01_tube_cycle_0009/run1_C01_tube_cycle_0009_comparison.pdf), [raw-polish PDF](/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113/continuation_final_audit/agd-continuation-final-audit-aa26864fab14-6888808/fields_run2_C02_raw_cycle_0005/run2_C02_raw_cycle_0005_comparison.pdf). The narrow-core maps use a stated symlog radial axis; field amplitudes and physical coordinates are not rescaled.
- Final audit job **6888808**, source SHA256 **70ee8e48d0ddae22203a39d87efdf3164433397dbaf6f2255bd63a8cf8b03592**, has its immutable source under central SLURM records. Main/broad/raw source hashes and exact output roots are in `R/{CONTINUATION,TUBE,RAW}_STATE.json`.

Load the strict image state with `scaled_boosted_profile.ScaledBoostedProfile.from_export`, broad/raw states with `multi_scale_profile.MultiScaleProfile.from_export`, and the older escaped state with `BoostedRationalProfile.from_export`. Independent evaluators take `asinh([[r,z],...])` and return physical derivatives. Multiscale exports deliberately reject older single-correction evaluators. Native PT files retain block optimizer information; they alone do not bitwise restore the complete round-robin scheduler.

Ten model/trust tests and real GPU objective/gradient/SSB smokes passed for the main production launch; three additional multiscale tests passed for each supplementary launch. The raw launch also loaded its actual physical restart files. Final CPU smoke adds canonical-component decomposition/assembly tests. A separate earlier CPU canonical launch 6887243 failed before production because an imported module was missing from its snapshot; corrected job 6887347 completed its full-source check. All failure records and earlier checkpoints remain preserved.

Only prompt/report Markdown belongs in this repository. All source code, data, logs, figures, optimizer states and validation arrays remain in the external experimental workspace.
